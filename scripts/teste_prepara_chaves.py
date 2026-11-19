#!/usr/bin/env python3
"""Casos do prepara_chaves.py, sem rede: cria quando falta, não toca quando existe, nunca imprime valor.

Uso, da raiz: python -X utf8 scripts/teste_prepara_chaves.py
Cada caso monta uma raiz temporária com os dois exemplos do repositório e roda o script sobre ela.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts/prepara_chaves.py"
EXEMPLOS = [".env.example", ".claude/settings.local.example.json"]
PLANTADO = "valor-plantado-" + "9f3e1c" * 4  # nenhum caso pode imprimir isto


def montar(tmp: Path) -> Path:
    for rel in EXEMPLOS:
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(RAIZ / rel, tmp / rel)
    return tmp


def rodar(raiz: Path, *args: str) -> subprocess.CompletedProcess:
    amb = dict(os.environ, PYTHONUTF8="1", PERPLEXITY_API_KEY=PLANTADO)
    return subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), "--raiz", str(raiz), *args],
                          capture_output=True, text=True, encoding="utf-8", env=amb)


def main() -> int:
    falhas: list[str] = []

    def confere(nome: str, ok: bool, r: subprocess.CompletedProcess) -> None:
        saida = r.stdout + r.stderr
        if PLANTADO in saida:
            ok, nome = False, nome + " (imprimiu o valor plantado)"
        print(("ok    " if ok else "FALHA ") + nome)
        if not ok:
            falhas.append(nome)
            print("      " + saida.replace("\n", "\n      "))

    with tempfile.TemporaryDirectory() as t:
        raiz = montar(Path(t))
        r = rodar(raiz)
        confere("cria o .env quando falta, cópia exata do exemplo",
                r.returncode == 0 and (raiz / ".env").read_bytes() == (raiz / ".env.example").read_bytes(), r)

    with tempfile.TemporaryDirectory() as t:
        raiz = montar(Path(t))
        antes = f"PERPLEXITY_API_KEY={PLANTADO}\r\nGEMINI_API_KEY={PLANTADO}\n".encode()
        (raiz / ".env").write_bytes(antes)
        r = rodar(raiz, "--skill", "research")
        confere("não toca no .env que existe (byte a byte) e diz que já existe",
                r.returncode == 0 and (raiz / ".env").read_bytes() == antes and "já existe" in r.stdout, r)

    with tempfile.TemporaryDirectory() as t:
        raiz = montar(Path(t))
        r = rodar(raiz, "--settings")
        destino = raiz / ".claude/settings.local.json"
        try:
            dados = json.loads(destino.read_text(encoding="utf-8"))
            valido = isinstance(dados.get("env"), dict) and "PERPLEXITY_API_KEY" in dados["env"]
        except (OSError, ValueError):
            valido = False
        confere("--settings cria o settings.local.json com JSON válido e o bloco env", r.returncode == 0 and valido, r)

    with tempfile.TemporaryDirectory() as t:
        raiz = montar(Path(t))
        destino = raiz / ".claude/settings.local.json"
        antes = json.dumps({"permissions": {"allow": []}, "env": {"GEMINI_API_KEY": PLANTADO}}).encode()
        destino.write_bytes(antes)
        r = rodar(raiz, "--settings", "--skill", "image-gen")
        confere("--settings não toca no settings.local.json que existe",
                r.returncode == 0 and destino.read_bytes() == antes and "já existe" in r.stdout, r)

    with tempfile.TemporaryDirectory() as t:
        raiz = montar(Path(t))
        r = rodar(raiz, "--skill", "research")
        linhas = (raiz / ".env.example").read_text(encoding="utf-8").splitlines()
        n = next(i for i, l in enumerate(linhas, 1) if l.startswith("PERPLEXITY_API_KEY="))
        confere("--skill research lista as variáveis dela, com a linha",
                r.returncode == 0 and "PERPLEXITY_API_KEY" in r.stdout and "GEMINI_API_KEY" in r.stdout
                and f"linha {n}" in r.stdout, r)

    with tempfile.TemporaryDirectory() as t:
        raiz = montar(Path(t))
        r = rodar(raiz, "--skill", "nao-existe")
        confere("skill desconhecida sai com 2 e não cria nada", r.returncode == 2 and not (raiz / ".env").exists(), r)

    print("TODOS OK" if not falhas else f"{len(falhas)} FALHA(S)")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
