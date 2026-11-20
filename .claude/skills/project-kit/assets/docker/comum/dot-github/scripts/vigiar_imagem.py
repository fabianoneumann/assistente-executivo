"""A vigilância da imagem base: a imagem da última versão publicada tem falha de segurança conhecida?

  python3 .github/scripts/vigiar_imagem.py            varre e abre ou atualiza a issue
  python3 .github/scripts/vigiar_imagem.py --previa   só varre e imprime

Roda da raiz do clone, pelo workflow `vigiar-imagem.yml` (toda semana) ou à mão: a mesma regra nos dois lugares. O
porquê de cada escolha e a regra de quando um achado vira versão nova estão em `knowledge/imagem-base.md`.

O que se varre: a imagem do Release marcado "Latest", no ghcr.io. Duas perguntas, porque uma não cobre a outra:
- o runtime da imagem está atrás de uma versão nova da mesma linha? O runtime da imagem oficial é um binário copiado
  ou compilado, e não um pacote do sistema, e a varredura não o vê;
- o Trivy acha falha alta ou crítica com correção disponível?

A imagem com achado tem uma issue (`[imagem-base] <nome>`, rótulo `imagem-base`). A rodada seguinte só comenta quando
algo mudou (achado novo, achado que saiu, imagem limpa), porque o mesmo aviso toda semana vira ruído. Fechar é da
triagem, e a issue fechada só reabre com achado novo. Uma falha da rodada nunca vira issue: o job fica vermelho.

Precisa de docker (logado no ghcr.io com leitura de pacotes), gh (com escrita em issues, fora da --previa) e trivy.
Do ambiente, opcional: RESPONSAVEL, o login do GitHub a quem a issue se atribui.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

# [kit:stack=node-ts]
RUNTIME = "node"
# [kit:fim]
# [kit:stack=python-fastapi]
RUNTIME = "python"
# [kit:fim]
# O ruído permanente que sai da varredura, cada um com o motivo ao lado (knowledge/imagem-base.md): sem isso, a issue
# nunca fica limpa e ninguém mais a lê. Opções do `trivy image`, por exemplo "--skip-files", "usr/local/bin/x".
IGNORAR: list[str] = []
VERSAO = re.compile(r"^v\d+\.\d+\.\d+$")
MARCA = re.compile(r"^<!-- (achados|resolvidos|limpa): ?(.*?) ?-->$", re.M)


class Falha(Exception):
    pass


def rodar(*cmd: str) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise Falha(f"{' '.join(cmd[:3])}: {(r.stderr or r.stdout).strip()[:500]}")
    return r.stdout


def baixar(url: str) -> str:
    try:
        with urllib.request.urlopen(url, timeout=30) as resposta:
            return resposta.read().decode("utf-8")
    except OSError as e:
        raise Falha(f"não consegui baixar {url}: {e}") from e


def numeros(versao: str) -> tuple[int, ...]:
    return tuple(int(x) for x in versao.lstrip("v").split("."))


# --- as duas perguntas -------------------------------------------------------------------------------------------

def achados_do_trivy(dados: dict) -> list[tuple[str, ...]]:
    """Um achado por linha: o id, a severidade, o pacote, a versão na imagem, a corrigida e onde."""
    achados = set()
    for resultado in dados.get("Results") or []:
        for v in resultado.get("Vulnerabilities") or []:
            achados.add((v["VulnerabilityID"], v["Severity"], v["PkgName"], v.get("InstalledVersion", ""),
                         v.get("FixedVersion", ""), v.get("PkgPath") or resultado.get("Target", "")))
    return sorted(achados)


def runtime_atrasado_node(indice: list[dict], na_imagem: str) -> tuple[str, ...] | None:
    """O Node contra a lista oficial (nodejs.org/dist/index.json), que marca cada versão com `security`."""
    linha = na_imagem.split(".")[0] + "."
    da_linha = [v for v in indice if v["version"].startswith(linha)]
    if not da_linha:
        raise Falha(f"a lista do Node não tem a linha {linha[:-1]}: o formato dela mudou?")
    ultima = max(da_linha, key=lambda v: numeros(v["version"]))["version"]
    seguranca = [v["version"] for v in da_linha if v.get("security")]
    if not seguranca:
        return None
    ultima_seguranca = max(seguranca, key=numeros)
    if numeros(ultima_seguranca) <= numeros(na_imagem):
        return None
    return (f"node-{ultima_seguranca}", "SECURITY RELEASE", "node", na_imagem, ultima, "o binário do Node")


def runtime_atrasado_python(listagem: str, na_imagem: str, pasta=None) -> tuple[str, ...] | None:
    """O Python contra as versões publicadas da mesma linha (a pasta de downloads do python.org). Na linha que já está
    só em correção de segurança, toda versão nova é de segurança; na que ainda corrige bug, o aviso pode ser de uma
    versão sem falha corrigida, e a triagem lê as notas antes de cortar versão."""
    linha = ".".join(na_imagem.split(".")[:2])
    publicadas = set(re.findall(rf'href="({re.escape(linha)}\.\d+)/"', listagem))
    if not publicadas:
        raise Falha(f"a pasta de downloads do python.org não tem a linha {linha}: o formato dela mudou?")
    # A pasta de uma versão nasce com o alfa, o beta ou o rc: conta só a que já tem o código-fonte final
    # (Python-X.Y.Z.tgz), da mais nova para a mais velha. `pasta(v)` devolve a listagem da pasta da versão.
    ultima = None
    for candidata in sorted(publicadas, key=numeros, reverse=True):
        if numeros(candidata) <= numeros(na_imagem):
            break
        if pasta is None or f'href="Python-{candidata}.tgz"' in pasta(candidata):
            ultima = candidata
            break
    if ultima is None:
        return None
    return (f"python-{ultima}", "VERSAO NOVA DA LINHA", "python", na_imagem, ultima, "o Python da imagem")


# --- o estado do aviso, que mora nos comentários da issue ---------------------------------------------------------

def em_aberto(historico: list[str]) -> set[str]:
    """O que está avisado e em aberto: em ordem, `achados` soma, `resolvidos` tira, `limpa` zera. Um achado que volta
    depois de sair é novo outra vez."""
    aberto: set[str] = set()
    for texto in historico:
        for tipo, ids in MARCA.findall((texto or "").replace("\r\n", "\n")):
            if tipo == "limpa":
                aberto.clear()
            elif tipo == "achados":
                aberto |= set(ids.split())
            else:
                aberto -= set(ids.split())
    return aberto


def plano(estado: str | None, avisados: set[str], achados: list[tuple[str, ...]]) -> dict:
    """O que fazer: `nada`, `abrir` ou `comentar` (com `reabrir` na issue fechada)."""
    atuais = {a[0] for a in achados}
    if estado is None:
        return {"acao": "abrir" if achados else "nada", "reabrir": False, "novos": achados, "resolvidos": []}
    novos = [a for a in achados if a[0] not in avisados]
    resolvidos = sorted(avisados - atuais)
    if not novos and not resolvidos:
        return {"acao": "nada", "reabrir": False, "novos": [], "resolvidos": []}
    # Na fechada, o que saiu também se grava (um comentário, sem reabrir), para o achado que voltar depois ser novo
    # outra vez; só o achado novo a reabre.
    return {"acao": "comentar", "reabrir": estado == "CLOSED" and bool(novos), "novos": novos, "resolvidos": resolvidos}


def tabela(achados: list[tuple[str, ...]]) -> str:
    linhas = ["| Achado | Severidade | Pacote | Na imagem | Corrigida em | Onde |", "|---|---|---|---|---|---|"]
    return "\n".join(linhas + ["| " + " | ".join(a) + " |" for a in achados])


def corpo_novo(ref: str, achados: list[tuple[str, ...]]) -> str:
    return (f"A vigilância da imagem base achou falha conhecida em `{ref}` (a última versão publicada).\n\n"
            f"{tabela(achados)}\n\nCorrige-se com uma versão nova: a imagem publicada não muda, e a base nova só entra "
            "ao construir outra. A triagem e a regra de quando isso vira versão de correção: `knowledge/imagem-base.md`."
            f"\n\n<!-- achados: {' '.join(a[0] for a in achados)} -->\n")


def corpo_comentario(ref: str, p: dict, achados: list[tuple[str, ...]]) -> str:
    if not achados:
        return (f"Na `{ref}` não há mais achado. Se ela já está instalada onde a falha importava, a issue pode fechar."
                f"\n\n<!-- limpa: {ref.rsplit(':', 1)[-1]} -->\n")
    partes = []
    if p["novos"]:
        partes.append(f"Achado novo em `{ref}`:\n\n{tabela(p['novos'])}")
    if p["resolvidos"]:
        partes.append(f"Saíram de `{ref}` (a correção já está na imagem): " + " ".join(f"`{r}`" for r in p["resolvidos"]))
    partes.append(f"Ainda em aberto: {len(achados)} achado(s).")
    marcas = []
    if p["novos"]:
        marcas.append(f"<!-- achados: {' '.join(a[0] for a in p['novos'])} -->")
    if p["resolvidos"]:
        marcas.append(f"<!-- resolvidos: {' '.join(p['resolvidos'])} -->")
    return "\n\n".join(partes + marcas) + "\n"


# --- a rodada ----------------------------------------------------------------------------------------------------

def varrer(ref: str, pasta: Path) -> list[tuple[str, ...]]:
    rodar("docker", "pull", "-q", ref)
    saida = pasta / "trivy.json"
    rodar("trivy", "image", "--quiet", "--scanners", "vuln", "--severity", "HIGH,CRITICAL", "--ignore-unfixed",
          *IGNORAR, "--format", "json", "--output", str(saida), ref)
    achados = achados_do_trivy(json.loads(saida.read_text(encoding="utf-8")))
    na_imagem = rodar("docker", "run", "--rm", "--entrypoint", RUNTIME, ref, "--version").strip()
    if RUNTIME == "node":
        if not VERSAO.match(na_imagem):
            raise Falha(f"a versão do Node na imagem é ilegível: {na_imagem!r}")
        atrasado = runtime_atrasado_node(json.loads(baixar("https://nodejs.org/dist/index.json")), na_imagem)
    else:
        m = re.fullmatch(r"Python (\d+\.\d+\.\d+)", na_imagem)
        if not m:
            raise Falha(f"a versão do Python na imagem é ilegível: {na_imagem!r}")
        na_imagem = m.group(1)
        atrasado = runtime_atrasado_python(baixar("https://www.python.org/ftp/python/"), na_imagem,
                                           lambda v: baixar(f"https://www.python.org/ftp/python/{v}/"))
    print(f"{RUNTIME} na imagem: {na_imagem}", file=sys.stderr)
    return sorted(achados + ([atrasado] if atrasado else []))


def avisar(repo: str, nome: str, ref: str, achados: list[tuple[str, ...]]) -> str:
    titulo = f"[imagem-base] {nome}"
    issues = json.loads(rodar("gh", "issue", "list", "-R", repo, "--state", "all", "--label", "imagem-base",
                              "--limit", "100", "--json", "number,title,state"))
    mesmas = sorted((i for i in issues if i["title"] == titulo), key=lambda i: i["number"])
    issue = mesmas[-1] if mesmas else None
    historico = []
    if issue:
        dados = json.loads(rodar("gh", "issue", "view", str(issue["number"]), "-R", repo, "--json", "body,comments"))
        historico = [dados.get("body") or ""] + [c.get("body") or "" for c in dados.get("comments") or []]
    p = plano(issue["state"] if issue else None, em_aberto(historico), achados)
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        corpo = Path(f.name)
    try:
        if p["acao"] == "abrir":
            rodar("gh", "label", "create", "imagem-base", "-R", repo, "--color", "B60205", "--force",
                  "--description", "falha conhecida na imagem base")
            corpo.write_text(corpo_novo(ref, achados), encoding="utf-8")
            extra = ["--assignee", os.environ["RESPONSAVEL"]] if os.environ.get("RESPONSAVEL") else []
            rodar("gh", "issue", "create", "-R", repo, "--title", titulo, "--body-file", str(corpo),
                  "--label", "imagem-base", *extra)
            return "issue aberta"
        if p["acao"] == "comentar":
            if p["reabrir"]:
                rodar("gh", "issue", "reopen", str(issue["number"]), "-R", repo)
            corpo.write_text(corpo_comentario(ref, p, achados), encoding="utf-8")
            rodar("gh", "issue", "comment", str(issue["number"]), "-R", repo, "--body-file", str(corpo))
            return f"comentado na #{issue['number']}"
        return f"nada novo desde o último aviso (#{issue['number']})" if issue else "limpa, sem issue"
    finally:
        corpo.unlink(missing_ok=True)


def main(argv: list[str]) -> int:
    previa = argv[1:] == ["--previa"]
    if argv[1:] and not previa:
        print(__doc__, file=sys.stderr)
        return 2
    try:
        repo = os.environ.get("GITHUB_REPOSITORY") or rodar("gh", "repo", "view", "--json", "nameWithOwner",
                                                            "-q", ".nameWithOwner").strip()
        try:
            tag = rodar("gh", "release", "view", "-R", repo, "--json", "tagName", "-q", ".tagName").strip()
        except Falha as e:
            if "not found" not in str(e).lower():
                raise
            print("Ainda não há versão publicada: nada a vigiar.")
            return 0
        if not VERSAO.match(tag):
            raise Falha(f"o Release 'Latest' não é uma versão: {tag!r}")
        nome = repo.split("/")[1]
        ref = f"ghcr.io/{repo.lower()}:{tag}"
        with tempfile.TemporaryDirectory() as tmp:
            achados = varrer(ref, Path(tmp))
        resumo = f"A imagem base da {tag}: {len(achados)} achado(s)\n\n" + (tabela(achados) if achados else "")
        print(resumo)
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
                f.write(resumo + "\n")
        if not previa:
            print(avisar(repo, nome, ref, achados))
    except (Falha, ValueError, KeyError) as e:
        print(f"vigiar_imagem: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
