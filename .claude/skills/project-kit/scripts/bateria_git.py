"""A bateria de efeito real dos hooks do git num clone de um projeto montado pelo kit.

  python -X utf8 bateria_git.py <pasta do projeto montado, ainda sem commit> [--python <interpretador com o formatador>]

Copia o projeto para uma pasta temporária ao lado, com um remoto nu, e faz os commits e os pushes de verdade, cada um
com o resultado esperado: o primeiro commit passa; o arquivo fora do formato no índice é recusado sem ser reescrito;
o índice formatado com a árvore suja passa; o log com a entrada no meio é recusado, e no fim passa; o log fora do
formato é recusado; o push da branch atrás da base avisa e envia; sem Python no PATH, o hook avisa e deixa passar.
Código 0 quando todos os casos deram o esperado. A cópia se apaga no fim (com --manter, fica).
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FEIO = "x=1\n"
BONITO = "x = 1\n"


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("projeto", type=Path)
    p.add_argument("--python", default=sys.executable)
    p.add_argument("--manter", action="store_true")
    args = p.parse_args(argv)
    raiz = Path(tempfile.mkdtemp(prefix="bateria-", dir=args.projeto.parent))
    clone, remoto = raiz / "clone", raiz / "remoto.git"
    shutil.copytree(args.projeto, clone)
    pasta_py = str(Path(args.python).resolve().parent)
    env = {**os.environ, "PATH": pasta_py + os.pathsep + os.environ["PATH"], "PYTHONUTF8": "1"}
    env.pop("CLAUDECODE", None)
    resultados = []

    def rodar(*cmd: str, ambiente=None) -> subprocess.CompletedProcess:
        return subprocess.run(cmd, cwd=clone, env=ambiente or env, capture_output=True, text=True, encoding="utf-8", errors="replace")

    def caso(nome: str, r: subprocess.CompletedProcess, espera_ok: bool, trecho: str = "") -> None:
        saida = r.stdout + r.stderr
        ok = (r.returncode == 0) == espera_ok and (trecho in saida)
        resultados.append(ok)
        print(f"{'ok  ' if ok else 'FALHOU'} {nome}: código {r.returncode}" + ("" if ok else f"\n{saida[-800:]}"))

    def escrever(rel: str, texto: str) -> None:
        (clone / rel).write_bytes(texto.encode("utf-8"))

    caso("o primeiro commit passa", rodar("git", "commit", "-qm", "o projeto nasce"), True)
    escrever("app/feio.py", FEIO)
    rodar("git", "add", "app/feio.py")
    caso("o arquivo fora do formato é recusado", rodar("git", "commit", "-qm", "feio"), False, "fora do formato")
    resultados.append((clone / "app/feio.py").read_text(encoding="utf-8") == FEIO)
    print(f"{'ok  ' if resultados[-1] else 'FALHOU'} o hook não reescreveu o arquivo")
    escrever("app/feio.py", BONITO)
    rodar("git", "add", "app/feio.py")
    escrever("app/feio.py", FEIO)
    caso("o índice formatado passa, com a árvore suja", rodar("git", "commit", "-qm", "bonito no índice"), True)
    rodar("git", "checkout", "--", "app/feio.py")

    log = (clone / "knowledge/log.md").read_text(encoding="utf-8")
    cabeca, primeira = log.split("\n## ", 1)
    escrever("knowledge/log.md", cabeca + "\n## [2026-11-18] nota | no meio\n\n## " + primeira)
    rodar("git", "add", "knowledge/log.md")
    caso("a entrada no meio do log é recusada", rodar("git", "commit", "-qm", "meio"), False, "no fim")
    escrever("knowledge/log.md", log.rstrip("\n") + "\n\n## [2026-11-18] nota | no fim\n")
    rodar("git", "add", "knowledge/log.md")
    caso("a entrada no fim do log passa", rodar("git", "commit", "-qm", "fim"), True)
    escrever("knowledge/log.md", log.rstrip("\n") + "\n\n## [2026-11-18] nota | no fim\n\n## 18/11 sem formato\n")
    rodar("git", "add", "knowledge/log.md")
    caso("a entrada fora do formato é recusada", rodar("git", "commit", "-qm", "formato"), False, "formato")
    rodar("git", "reset", "-q", "--hard")

    subprocess.run(["git", "init", "-q", "--bare", str(remoto)], check=True, capture_output=True)
    rodar("git", "remote", "add", "origin", str(remoto))
    rodar("git", "push", "-q", "origin", "main")
    rodar("git", "checkout", "-qb", "12-tema", "HEAD~1")
    escrever("app/novo.py", BONITO)
    rodar("git", "add", "app/novo.py")
    rodar("git", "commit", "-qm", "novo")
    caso("o push da branch atrás da base avisa e envia", rodar("git", "push", "-u", "origin", "12-tema"), True, "atrás de origin/main")
    enviado = rodar("git", "ls-remote", "origin", "refs/heads/12-tema").stdout.strip() != ""
    resultados.append(enviado)
    print(f"{'ok  ' if enviado else 'FALHOU'} a branch chegou ao remoto")

    def tem_python(pasta: str) -> bool:
        try:
            return any(Path(pasta).glob("python*")) or (Path(pasta) / "py.exe").exists()
        except OSError:
            return False

    sem_python = {**env, "PATH": os.pathsep.join(p for p in env["PATH"].split(os.pathsep) if not tem_python(p))}
    escrever("app/feio2.py", FEIO)
    rodar("git", "add", "app/feio2.py", ambiente=sem_python)
    caso("sem Python, o hook avisa e deixa passar", rodar("git", "commit", "-qm", "sem python", ambiente=sem_python), True, "sem Python")

    if not args.manter:
        shutil.rmtree(raiz, ignore_errors=True)
    print(f"{sum(resultados)} de {len(resultados)} casos deram o esperado")
    return 0 if all(resultados) else 1


if __name__ == "__main__":
    sys.exit(main())
