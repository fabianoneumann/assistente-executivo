"""Monta um projeto novo a partir dos modelos da skill `project-kit`.

Copia `assets/projeto/` (o `dot-x` vira `.x`, e o sufixo `.modelo` sai), põe por cima os arquivos da stack
(`assets/stacks/<stack>/`) e os da base escrita na conversa (`--base`, que leva `arquitetura.md`, `plano.md` e os
ADRs 001 e 002 em `decisions/`), troca os marcadores `{{X}}`, mantém só os blocos `[kit:chave=valor]...[kit:fim]`
que casam, grava os diagramas do onboarding em `onboarding/diagramas/` (as travas em camadas, a prioridade e a sequência, cada
um com o modelo de `assets/diagramas/` e os dados embutidos), grava tudo em LF, faz o `git init`, liga o
`core.hooksPath` e prepara os arquivos (sem commitar). Com `--docker`, o projeto ganha também a imagem (o `Dockerfile` da
stack, o `.dockerignore`, o job `imagem` no CI, a publicação na tag e o vigia semanal da imagem base, com a página
`knowledge/imagem-base.md`); sem ele, nada de Docker nasce.

Uso:
  python -X utf8 montar.py --destino <pasta> --nome <nome> --descricao "<frase>" --stack python-fastapi|node-ts|outra
         --dono <usuário ou organização> --base <pasta> [--conta user|org] [--responsavel <usuário>]
         [--comandos <arquivo.json>] [--docker] [--data AAAA-MM-DD] [--ramo main] [--sem-git]

Para `--stack outra`, o `--comandos` traz os mesmos campos de `assets/stacks.json` (references/stacks.md).
Código 0 quando montou; 2 quando faltou ou sobrou algo (a mensagem diz o quê), sem deixar a pasta pela metade.
"""

from __future__ import annotations

import argparse
import html
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
MODELOS = SKILL / "assets" / "projeto"
STACKS = SKILL / "assets" / "stacks"
DOCKER = SKILL / "assets" / "docker"
CAMPOS = ["STACK_DESCRICAO", "CMD_INSTALAR", "CMD_CI_INSTALAR", "CMD_FORMATAR", "CMD_FORMATAR_CHECK", "CMD_LINT",
          "CMD_TESTES", "CMD_SMOKE", "CMD_E2E", "FORMATADOR", "EXTENSOES", "ECOSSISTEMA"]
EXECUTAVEIS = [".claude/hooks/fluxo.sh", ".githooks/pre-commit", ".githooks/pre-push"]
DIAGRAMAS = SKILL / "assets" / "diagramas"
# Os diagramas que o projeto recebe em onboarding/diagramas/ (o padrão: assets/diagramas/LEIA.md): cada dado vira uma página com o modelo certo e a cópia embutida, ao lado do motor, dos tokens e da licença.
DIAGRAMAS_DO_PROJETO = {"travas.html": "travas.json", "prioridade.html": "prioridade.json",
                        "sequencia.html": "sequencia.json"}  # a sequência leva os nós da arquitetura embutidos
ARQUIVOS_DOS_DIAGRAMAS = ["elk.bundled.js", "elk-LICENSE.md", "tokens.css"]
BLOCO_LINHA = re.compile(r"^[ \t]*(?:#|//|<!--)?[ \t]*\[kit:(\w+)=([^\]]+)\][ \t]*(?:-->)?[ \t]*\n(.*?)"
                         r"^[ \t]*(?:#|//|<!--)?[ \t]*\[kit:fim\][ \t]*(?:-->)?[ \t]*\n", re.M | re.S)
BLOCO_DENTRO = re.compile(r"\[kit:(\w+)=([^\]]+)\](.*?)\[kit:fim\]", re.S)
MARCADOR = re.compile(r"\{\{([A-Z_]+)\}\}")


class Falta(Exception):
    pass


def nome_final(rel: Path) -> Path:
    partes = [("." + p[4:]) if p.startswith("dot-") else p for p in rel.parts]
    if partes[-1].endswith(".modelo"):
        partes[-1] = partes[-1][: -len(".modelo")]
    return Path(*partes)


def blocos(texto: str, ctx: dict[str, str]) -> str:
    def manter(m: re.Match) -> str:
        chave, valores, corpo = m.group(1), m.group(2).split("|"), m.group(3)
        if chave not in ctx:
            raise Falta(f"o bloco [kit:{chave}=...] não tem chave conhecida (as chaves: {', '.join(ctx)})")
        return corpo if ctx[chave] in valores else ""
    return BLOCO_DENTRO.sub(manter, BLOCO_LINHA.sub(manter, texto))


def trocar(texto: str, valores: dict[str, str], arquivo: Path) -> str:
    desconhecidos = sorted({m.group(1) for m in MARCADOR.finditer(texto)} - set(valores))
    if desconhecidos:
        raise Falta(f"{arquivo}: marcador sem valor: {', '.join(desconhecidos)}")
    return MARCADOR.sub(lambda m: valores[m.group(1)], texto)


def valores_de(args, comandos: dict) -> dict[str, str]:
    v = {
        "NOME": args.nome, "DESCRICAO": args.descricao, "DONO": args.dono, "REPO": f"{args.dono}/{args.nome}",
        "ASSIGNEES": (f"    assignees:\n      - {args.responsavel}\n" if args.responsavel else ""), "DATA": args.data, "STACK": args.stack, "BASE": args.ramo,
        "RESPONSAVEL": args.responsavel or "", "PORTA": str(comandos.get("PORTA", "")),
    }
    for campo in CAMPOS:
        if campo not in comandos:
            raise Falta(f"a stack {args.stack} não traz o campo {campo} (references/stacks.md)")
        valor = comandos[campo]
        v[campo] = valor if isinstance(valor, str) else json.dumps(valor, ensure_ascii=False)
    v["FORMATADOR_JSON"], v["EXTENSOES_JSON"] = v.pop("FORMATADOR"), v.pop("EXTENSOES")
    for chave in list(v):
        if not chave.endswith("_JSON"):  # a forma JSON serve também de string entre aspas no YAML e no TOML
            v[chave + "_JSON"] = json.dumps(v[chave], ensure_ascii=False)
            v[chave + "_HTML"] = html.escape(v[chave])
    return v


def copiar(origem: Path, destino: Path) -> list[Path]:
    feitos = []
    for arq in sorted(p for p in origem.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
        alvo = destino / nome_final(arq.relative_to(origem))
        alvo.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(arq, alvo)
        feitos.append(alvo)
    return feitos


def diagramas(destino: Path) -> list[Path]:
    """As páginas dos diagramas do onboarding (as travas em camadas, a prioridade, a sequência do pedido ao PR), que
    abrem do disco."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from diagrama_render import pagina_para_projeto
    destino.mkdir(parents=True, exist_ok=True)
    feitos = []
    for nome in ARQUIVOS_DOS_DIAGRAMAS:
        shutil.copyfile(DIAGRAMAS / nome, destino / nome)
        feitos.append(destino / nome)
    for pagina, dados in DIAGRAMAS_DO_PROJETO.items():
        (destino / pagina).write_bytes(pagina_para_projeto(DIAGRAMAS / dados).encode("utf-8"))
        feitos.append(destino / pagina)
    # o esquema dos dados vai junto, para o CI do projeto conferir a cópia embutida de cada página sem navegador
    shutil.copyfile(Path(__file__).resolve().parent / "diagrama_esquema.py", destino / "esquema.py")
    feitos.append(destino / "esquema.py")
    return feitos


def conferir_base(base: Path) -> None:
    faltam = [n for n in ("arquitetura.md", "plano.md") if not (base / n).is_file()]
    for numero in ("001", "002"):
        if not list((base / "decisions").glob(f"{numero}-*.md")):
            faltam.append(f"decisions/{numero}-<slug>.md")
    if faltam:
        raise Falta(f"a base escrita na conversa ({base}) não tem: {', '.join(faltam)} (SKILL.md, etapas 2 e 3)")


def git(pasta: Path, *args: str) -> None:
    r = subprocess.run(["git", *args], cwd=pasta, capture_output=True, text=True)
    if r.returncode:
        raise Falta(f"git {' '.join(args)}: {r.stderr.strip()}")


def montar(args) -> Path:
    destino = Path(args.destino)
    if destino.exists() and any(destino.iterdir()):
        raise Falta(f"o destino {destino} já existe e não está vazio")
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", args.nome):
        raise Falta(f"o nome {args.nome!r} não serve de nome de repositório (minúsculas, números, '.', '_' e '-')")
    if args.stack == "outra":
        if not args.comandos:
            raise Falta("a stack outra pede --comandos <arquivo.json> com os campos de assets/stacks.json")
        comandos = json.loads(Path(args.comandos).read_text(encoding="utf-8"))
    else:
        comandos = json.loads((SKILL / "assets" / "stacks.json").read_text(encoding="utf-8"))[args.stack]
    if args.docker and not (DOCKER / args.stack).is_dir():
        raise Falta(f"o --docker não tem modelo para a stack {args.stack}: monte sem ele e escreva o Dockerfile à mão, "
                    "a partir dos modelos de assets/docker/ (references/stacks.md, \"A imagem\")")
    base = Path(args.base)
    conferir_base(base)
    valores = valores_de(args, comandos)
    ctx = {"stack": args.stack, "conta": args.conta, "docker": "sim" if args.docker else "nao"}
    destino.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destino.parent) as tmp:
        obra = Path(tmp) / "obra"
        copiar(MODELOS, obra)
        if (STACKS / args.stack).is_dir():
            copiar(STACKS / args.stack, obra)
        if args.docker:
            copiar(DOCKER / "comum", obra)
            copiar(DOCKER / args.stack, obra)
        copiar(base, obra / "knowledge")
        diagramas(obra / "onboarding" / "diagramas")
        for arq in sorted(p for p in obra.rglob("*") if p.is_file()):
            bruto = arq.read_bytes()
            try:
                texto = bruto.decode("utf-8")
            except UnicodeDecodeError:
                continue
            texto = trocar(blocos(texto.replace("\r\n", "\n"), ctx), valores, arq.relative_to(obra))
            arq.write_bytes(texto.encode("utf-8"))
        if not args.sem_git:  # o git ainda na obra: se falhar, o destino fica como estava
            git(obra, "init", "-q", "-b", args.ramo)
            git(obra, "config", "core.hooksPath", ".githooks")
            git(obra, "add", "-A")
            for exe in EXECUTAVEIS:
                git(obra, "update-index", "--chmod=+x", exe)
        destino.mkdir(parents=True, exist_ok=True)
        for item in obra.iterdir():
            shutil.move(str(item), destino / item.name)
    return destino


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--destino", required=True)
    p.add_argument("--nome", required=True)
    p.add_argument("--descricao", required=True)
    p.add_argument("--stack", required=True, choices=["python-fastapi", "node-ts", "outra"])
    p.add_argument("--dono", required=True)
    p.add_argument("--base", required=True, help="a pasta com arquitetura.md, plano.md e decisions/001-*.md e 002-*.md")
    p.add_argument("--conta", choices=["user", "org"], default="user")
    p.add_argument("--responsavel", help="opcional: o usuário do GitHub atribuído aos PRs do Dependabot e, com --docker, às issues do vigia da imagem (sem ele, o aviso chega a quem acompanha o repositório)")
    p.add_argument("--comandos")
    p.add_argument("--docker", action="store_true", help="o projeto publica imagem: o Dockerfile, o build no CI, a publicação na tag e o vigia da imagem base")
    p.add_argument("--data", default=dt.date.today().isoformat())
    p.add_argument("--ramo", default="main")
    p.add_argument("--sem-git", action="store_true")
    args = p.parse_args(argv)
    try:
        destino = montar(args)
    except (Falta, OSError, ValueError) as e:
        print(f"ERRO: {e}", file=sys.stderr)
        return 2
    print(f"Montado em {destino}. Agora: python -X utf8 {SKILL / 'scripts' / 'conferir.py'} {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
