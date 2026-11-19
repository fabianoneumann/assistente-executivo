"""Roda localmente as linhas `run:` do CI de um projeto montado pelo kit, em ordem, e diz o código de cada uma.

  python -X utf8 ci_local.py <pasta do projeto> [--python <interpretador>]

Serve para provar o `ci.yml` do kit sem o `act` (que baixaria as imagens do runner). Os passos `uses:` (o checkout, o
setup da linguagem) ficam de fora: a máquina já tem a linguagem, e o `--python` aponta o interpretador (o de um venv,
por exemplo), que entra no lugar do `python3` e do `python` das linhas. Cada linha roda no shell (o `sh` do Git, no
Windows), com um prazo de 10 minutos. Não imita o `if:`, o `env:`, o `working-directory` nem as expressões `${{ }}`
do GitHub: a linha com expressão é recusada, para a prova local não divergir calada do runner. O `ci.yml` do kit não
usa nenhum deles. Código 0 quando todas saíram em 0.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import yaml


def linhas_run(ci: Path) -> list[tuple[str, str]]:
    dados = yaml.safe_load(ci.read_text(encoding="utf-8"))
    passos = []
    for job in dados["jobs"].values():
        for i, passo in enumerate(job.get("steps", []), 1):
            if "run" in passo:
                passos.append((passo.get("name", f"passo {i}"), passo["run"]))
    return passos


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("pasta", type=Path)
    p.add_argument("--python", default=sys.executable)
    args = p.parse_args(argv)
    sh = shutil.which("sh") or shutil.which("bash")
    if not sh:
        print("ERRO: sem sh no PATH")
        return 2
    pasta_py = str(Path(args.python).resolve().parent)
    env = {**os.environ, "PATH": pasta_py + os.pathsep + os.environ.get("PATH", ""), "PYTHONUTF8": "1", "CI": "true"}
    falhas = 0
    for nome, linha in linhas_run(args.pasta / ".github/workflows/ci.yml"):
        if "${{" in linha:
            print(f"ERRO {nome}: a linha usa uma expressão do GitHub, que este script não imita: {linha}")
            falhas += 1
            continue
        comando = linha.replace("python3 ", "python ")
        t0 = time.time()
        try:
            r = subprocess.run([sh, "-c", comando], cwd=args.pasta, env=env, capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=600)
        except subprocess.TimeoutExpired:
            print(f"ERRO tempo {nome}: passou de 10 minutos")
            falhas += 1
            continue
        print(f"{'ok  ' if r.returncode == 0 else 'ERRO'} {r.returncode:>3}  {time.time() - t0:5.1f}s  {nome}: {linha}")
        if r.returncode:
            falhas += 1
            print((r.stdout + r.stderr)[-1500:])
    print(f"{falhas} passo(s) com código diferente de 0")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
