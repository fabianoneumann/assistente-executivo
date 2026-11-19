"""Os hooks do git do projeto, para pessoas e agentes. Só a biblioteca padrão.

  python .githooks/hooks.py pre-commit          o formatador no conteúdo do índice e o log em ordem (recusa: código 3)
  python .githooks/hooks.py pre-push <remoto>   avisa quando a branch está atrás da base do remoto (nunca recusa)
  python .githooks/hooks.py log [arquivo]       confere o log da base no disco (o CI roda este; recusa: código 3)
  python .githooks/hooks.py instalar            liga os hooks neste clone (core.hooksPath), uma vez por clone

A configuração (a base, o formatador, as extensões) está em .githooks/config.json; o porquê, em knowledge/travas.md.
O hook do formatador não reescreve nada: quem preparou só parte de um arquivo perderia o resto.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RECUSA = 3
CABECALHO = "# Log da base"
ENTRADA = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\] [a-zà-ú-]+ \| \S.*$")


def config() -> dict:
    return json.loads((AQUI / "config.json").read_text(encoding="utf-8"))


def git(*args: str, entrada: bytes | None = None) -> tuple[int, bytes]:
    r = subprocess.run(["git", *args], input=entrada, capture_output=True)
    return r.returncode, r.stdout


def formatar(cmd: list[str], conteudo: bytes) -> tuple[int, bytes, bytes] | None:
    """Roda o formatador com o conteúdo no stdin: (código, saída, erro), ou None quando ele não está instalado."""
    exe = shutil.which(cmd[0])
    if not exe:
        return None
    try:
        r = subprocess.run([exe, *cmd[1:]], input=conteudo, capture_output=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.returncode, r.stdout, r.stderr


# ---- o log ------------------------------------------------------------------------------------------------------
def erros_do_log(texto: str) -> list[str]:
    """O cabeçalho intacto e cada entrada no formato fixo, com data que existe. A ordem não se confere aqui: com o
    `merge=union`, duas branches que escrevem no fim juntam as entradas na ordem do merge, e não na das datas."""
    linhas = texto.replace("\r\n", "\n").split("\n")
    erros = []
    if not linhas or linhas[0].strip() != CABECALHO:
        erros.append(f'a primeira linha do log não é "{CABECALHO}" (o cabeçalho partiu?)')
    for n, linha in enumerate(linhas, 1):
        if not linha.startswith("## "):
            continue
        m = ENTRADA.match(linha)
        if not m:
            erros.append(f"linha {n}: a entrada não está no formato `## [AAAA-MM-DD] <tipo> | <assunto>`")
            continue
        try:
            dt.date.fromisoformat(m.group(1))
        except ValueError:
            erros.append(f"linha {n}: a data {m.group(1)} não existe")
    return erros


def entradas(texto: str) -> list[str]:
    return [linha.strip() for linha in texto.replace("\r\n", "\n").split("\n") if linha.startswith("## ")]


def erros_de_ordem(antes: str, depois: str) -> list[str]:
    """A entrada nova vai no fim: as entradas que já estavam continuam, na mesma ordem, no começo do log."""
    velhas, novas = entradas(antes), entradas(depois)
    if novas[: len(velhas)] != velhas:
        return ["uma entrada foi inserida no meio, apagada ou mudou de lugar; a entrada nova vai no fim do log"]
    return []


# ---- os hooks ---------------------------------------------------------------------------------------------------
def pre_commit(cfg: dict, git=git, formatar=formatar, sem: set[str] = frozenset()) -> tuple[int, list[str]]:
    """Devolve (código, mensagens). O conteúdo conferido é o do índice, que é o que vai no commit."""
    msgs: list[str] = []
    _, saida = git("diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    preparados = [p for p in saida.decode("utf-8", "replace").split("\0") if p]
    fora: list[str] = []
    if "formato" not in sem:
        for caminho in [p for p in preparados if Path(p).suffix in cfg.get("extensoes", [])]:
            codigo, conteudo = git("show", f":{caminho}")
            if codigo:
                continue
            cmd = [a.replace("{arquivo}", caminho) for a in cfg["formatador"]]
            r = formatar(cmd, conteudo)
            if r is None:
                msgs.append(f"[pre-commit] o formatador ({cfg['formatador'][0]}) não está instalado: o formato não foi conferido.")
                break
            if r[0] != 0:
                erro = (r[2].decode("utf-8", "replace").strip().splitlines() or ["sem mensagem"])[-1]
                msgs.append(f"[pre-commit] o formatador falhou em {caminho} ({erro}): o formato dele não foi conferido.")
            elif r[1].replace(b"\r\n", b"\n") != conteudo.replace(b"\r\n", b"\n"):
                fora.append(caminho)
    if fora:
        msgs.append("[pre-commit] fora do formato: " + ", ".join(fora) + f". Rode `{cfg.get('comando_formatar', 'o formatador')}`, prepare de novo e commite.")
    log = cfg.get("log", "knowledge/log.md")
    erros = []
    if "log" not in sem and log in preparados:
        codigo, conteudo = git("show", f":{log}")
        if not codigo:
            depois = conteudo.decode("utf-8", "replace")
            erros = erros_do_log(depois)
            em_merge = git("rev-parse", "-q", "--verify", "MERGE_HEAD")[0] == 0  # o merge junta por união, na ordem dele
            c_antes, antes = git("show", f"HEAD:{log}")
            if not em_merge and not c_antes:
                erros += erros_de_ordem(antes.decode("utf-8", "replace"), depois)
            msgs += [f"[pre-commit] {log}: {e}" for e in erros]
    return (RECUSA if fora or erros else 0), msgs


def pre_push(cfg: dict, remoto: str, refs: str, git=git) -> list[str]:
    """Só avisa: a cópia de uma branch em andamento é legítima, e quem recusa o PR atrasado é o hook do agente e o CI."""
    base = cfg.get("base", "main")
    codigo, saida = git("ls-remote", remoto, f"refs/heads/{base}")
    if codigo:
        return [f"[pre-push] não consegui ler {remoto}/{base}: a sincronização não foi conferida."]
    if not saida.split():
        return []  # a base ainda não existe no remoto (o primeiro push): não há com o que comparar
    ponta = saida.split()[0].decode()
    msgs = []
    for linha in refs.splitlines():
        partes = linha.split()
        if len(partes) != 4 or not partes[2].startswith("refs/heads/") or partes[2] == f"refs/heads/{base}":
            continue
        if set(partes[1]) == {"0"}:
            continue  # a branch apagada
        if git("merge-base", "--is-ancestor", ponta, partes[1])[0] != 0:
            msgs.append(f"[pre-push] {partes[2][11:]} está atrás de {remoto}/{base}: antes do PR, `git fetch` e `git merge origin/{base}`.")
    return msgs


def instalar(git=git) -> tuple[int, str]:
    if os.environ.get("CI"):
        return 0, ""
    codigo, saida = git("config", "--get", "core.hooksPath")
    atual = saida.decode().strip()
    if atual == ".githooks":
        return 0, "Os hooks do git já estão ligados neste clone."
    if atual:
        return 0, (f"Este clone já usa outro core.hooksPath ({atual}): não mexi. Para juntar, chame os hooks de "
                   ".githooks/ a partir dos seus, ou troque com `git config core.hooksPath .githooks`.")
    if git("config", "core.hooksPath", ".githooks")[0]:
        return 1, "Não consegui ligar os hooks (isto é um clone do git?)."
    return 0, "Os hooks do git estão ligados neste clone (core.hooksPath = .githooks)."


def main(argv: list[str]) -> int:
    acao = argv[1] if len(argv) > 1 else ""
    if acao == "instalar":
        codigo, texto = instalar()
        print(texto)
        return codigo
    if acao == "log":
        arquivo = Path(argv[2]) if len(argv) > 2 else Path(config().get("log", "knowledge/log.md"))
        erros = erros_do_log(arquivo.read_text(encoding="utf-8"))
        for e in erros:
            print(f"ERRO {arquivo}: {e}")
        print(f"{arquivo}: {len(erros)} erro(s)")
        return RECUSA if erros else 0
    if acao == "pre-commit":
        codigo, msgs = pre_commit(config())
        for m in msgs:
            print(m, file=sys.stderr)
        return codigo
    if acao == "pre-push":
        for m in pre_push(config(), argv[2] if len(argv) > 2 else "origin", sys.stdin.read()):
            print(m, file=sys.stderr)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
