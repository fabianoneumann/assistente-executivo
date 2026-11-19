"""Prepara o GitHub de um projeto montado pela skill `project-kit`. Separado do `montar.py` porque usa a rede.

  python -X utf8 github.py --pasta <projeto> --repo <dono>/<nome> [--criar] [--publico]
         [--milestone "<título>" --prazo AAAA-MM-DD --criterio "<o que fecha>"] [--simular]

Cada passo confere antes de agir, e rodar de novo não duplica nada:
  1. (com --criar) o repositório, privado por padrão, com o push do main já commitado;
  2. os rótulos: na conta pessoal, os de prioridade e o `defeito` (o Type e a Priority nativos são de organização);
  3. o Dependabot de segurança (os alertas e as correções automáticas);
  4. a regra de tag `tags-imutaveis` (nas tags v*: não move, não apaga); na conta pessoal com repositório privado,
     não se cria (pede o GitHub Pro) e vale a regra escrita no CLAUDE.md. Se o plano não a oferece, avisa e segue;
  5. (com --milestone) a primeira milestone, com o critério e a busca "o que pegar agora" na descrição.
Com --simular, só diz o que faria. Código 0 quando tudo passou ou ficou só em AVISO; 1 com ERRO.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

ROTULOS_PESSOAIS = [
    ("prioridade:urgente", "b60205", "Eisenhower: prazo externo próximo, ou defeito numa versão instalada"),
    ("prioridade:alta", "d93f0b", "Eisenhower: o último bloqueio aberto de outra issue"),
    ("prioridade:media", "fbca04", "Eisenhower: numa milestone aberta, sem urgência"),
    ("prioridade:baixa", "c2e0c6", "Eisenhower: sem milestone"),
    ("defeito", "d73a4a", "Algo já entregue que não faz o que deveria"),
]
ROTULOS_SEMPRE = [("dependencies", "0366d6", "Atualização de dependência (seção própria nas notas da versão)")]
REGRA_DE_TAG = {
    "name": "tags-imutaveis", "target": "tag", "enforcement": "active",
    "conditions": {"ref_name": {"include": ["refs/tags/v*"], "exclude": []}},
    "rules": [{"type": "deletion"}, {"type": "update"}],
}


class GitHub:
    def __init__(self, simular: bool):
        self.simular = simular
        self.erros: list[str] = []
        self.avisos: list[str] = []

    def gh(self, *args: str, entrada: str | None = None, escreve: bool = False) -> tuple[int, str, str]:
        if escreve and self.simular:
            print(f"[simular] gh {' '.join(args)}")
            return 0, "{}", ""
        r = subprocess.run(["gh", *args], input=entrada, capture_output=True, text=True, encoding="utf-8")
        return r.returncode, r.stdout, r.stderr

    def passo(self, nome: str, ok: bool, detalhe: str = "", aviso: bool = False) -> None:
        if ok:
            print(f"ok    {nome}{': ' + detalhe if detalhe else ''}")
        elif aviso:
            self.avisos.append(f"{nome}: {detalhe}")
            print(f"AVISO {nome}: {detalhe}")
        else:
            self.erros.append(f"{nome}: {detalhe}")
            print(f"ERRO  {nome}: {detalhe}")


def preparar(args) -> GitHub:
    g = GitHub(args.simular)
    repo, dono = args.repo, args.repo.split("/")[0]
    existe = g.gh("repo", "view", repo, "--json", "name")[0] == 0
    if args.criar and not existe:
        visibilidade = "--public" if args.publico else "--private"
        c, _, e = g.gh("repo", "create", repo, visibilidade, "--source", str(args.pasta), "--remote", "origin", "--push", escreve=True)
        g.passo("o repositório", c == 0, e.strip() or repo)
        if c:
            return g
    elif not existe:
        g.passo("o repositório", False, f"{repo} não existe; rode com --criar")
        return g
    else:
        g.passo("o repositório", True, f"{repo} já existe")

    c, saida, _ = g.gh("api", f"users/{dono}", "--jq", ".type")
    conta = "org" if saida.strip() == "Organization" else "user"
    rotulos = (ROTULOS_PESSOAIS if conta == "user" else []) + ROTULOS_SEMPRE
    for nome, cor, desc in rotulos:
        c, _, e = g.gh("label", "create", nome, "--repo", repo, "--color", cor, "--description", desc, "--force", escreve=True)
        g.passo(f"o rótulo {nome}", c == 0, e.strip())

    for rota, nome in (("vulnerability-alerts", "os alertas do Dependabot"), ("automated-security-fixes", "as correções de segurança do Dependabot")):
        c, _, e = g.gh("api", "-X", "PUT", f"repos/{repo}/{rota}", escreve=True)
        g.passo(nome, c == 0, e.strip())

    if conta == "user" and not args.publico:
        g.passo("a regra de tag", True, "conta pessoal com repositório privado: vale a regra escrita no CLAUDE.md do projeto (a regra de tag pede o GitHub Pro)")
        return milestone(g, args, repo)
    c, saida, e = g.gh("api", f"repos/{repo}/rulesets")
    nomes = [r.get("name") for r in json.loads(saida)] if c == 0 and saida.strip().startswith("[") else []
    if "tags-imutaveis" in nomes:
        g.passo("a regra de tag", True, "tags-imutaveis já existe")
    else:
        c, _, e = g.gh("api", "-X", "POST", f"repos/{repo}/rulesets", "--input", "-", entrada=json.dumps(REGRA_DE_TAG), escreve=True)
        indisponivel = "403" in e or "Upgrade" in e or "not available" in e.lower()
        g.passo("a regra de tag", c == 0, (e.strip().splitlines() or [""])[0] + (
            " (o plano não oferece regra de tag neste repositório: vale a regra escrita em knowledge/versao-e-dependencias.md)"
            if indisponivel else ""), aviso=indisponivel)
    return milestone(g, args, repo)


def milestone(g: GitHub, args, repo: str) -> GitHub:
    if args.milestone:
        c, saida, _ = g.gh("api", f"repos/{repo}/milestones?state=all", "--jq", "[.[].title]")
        if c == 0 and args.milestone in json.loads(saida or "[]"):
            g.passo("a milestone", True, f"{args.milestone} já existe")
        else:
            busca = f'is:issue is:open no:assignee -is:blocked milestone:"{args.milestone}"'
            desc = (f"Fecha quando: {args.criterio}\n\nO que pegar agora: "
                    f"https://github.com/{repo}/issues?q={quote(busca)}")
            campos = ["-f", f"title={args.milestone}", "-f", f"description={desc}"]
            if args.prazo:
                campos += ["-f", f"due_on={args.prazo}T23:59:59Z"]
            c, _, e = g.gh("api", "-X", "POST", f"repos/{repo}/milestones", *campos, escreve=True)
            g.passo("a milestone", c == 0, e.strip() or args.milestone)
    busca = quote("is:issue is:open no:assignee -is:blocked")
    print(f"\nO que pegar agora: https://github.com/{repo}/issues?q={busca}")
    return g


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--pasta", type=Path, required=True)
    p.add_argument("--repo", required=True)
    p.add_argument("--criar", action="store_true")
    p.add_argument("--publico", action="store_true")
    p.add_argument("--milestone")
    p.add_argument("--prazo")
    p.add_argument("--criterio", default="o critério da milestone, no knowledge/plano.md")
    p.add_argument("--simular", action="store_true")
    args = p.parse_args(argv)
    g = preparar(args)
    print(f"{len(g.erros)} ERRO, {len(g.avisos)} AVISO")
    return 1 if g.erros else 0


if __name__ == "__main__":
    sys.exit(main())
