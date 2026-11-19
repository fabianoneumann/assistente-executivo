"""Leitura das chaves do ambiente, com o `.env` local como fonte.

Cópia idêntica deste arquivo vai na pasta `scripts/` de cada skill que usa chave
(`research`, `image-gen`, `r2-storage`, `slides-export`), para a skill funcionar
também instalada como plugin noutro projeto. O `scripts/confere_ambiente.py`
confere que as cópias estão iguais a esta.

A ordem: o que já está no ambiente com valor (o bloco `env` do `.claude/settings.local.json`,
ou a variável do sistema) vence; o que falta, ou está vazio ou com o marcador `COLE_...`,
se lê do `.env` da pasta de trabalho ou da primeira pasta-pai que tiver um. O valor nunca
se imprime.
"""
from __future__ import annotations

import os
from pathlib import Path

MARCADORES = ("COLE_", "cole_", "<", "sua-chave", "SUA_CHAVE")


def achar_env(inicio: Path | None = None) -> Path | None:
    """O `.env` mais próximo, subindo da pasta de trabalho até a raiz do repositório."""
    pasta = (inicio or Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())).resolve()
    for p in [pasta, *pasta.parents]:
        if (p / ".env").is_file():
            return p / ".env"
        if (p / ".git").exists():
            return None
    return None


_LIDOS: set[Path] = set()


def _interpretar(valor_bruto: str) -> str:
    """O valor de uma linha `NOME=valor`: entre aspas, o que está dentro; sem aspas, até o ` #` do comentário."""
    v = valor_bruto.strip()
    if v[:1] in ("'", '"'):
        fim = v.find(v[0], 1)
        return v[1:fim] if fim > 0 else v[1:]
    return v.split(" #", 1)[0].split("	#", 1)[0].strip()


def carregar_env(inicio: Path | None = None) -> Path | None:
    """Põe no ambiente as variáveis do `.env` que ainda não estão lá (ou que lá estão vazias ou com o
    marcador). Lê cada arquivo uma vez só por processo. Devolve o arquivo lido."""
    arq = achar_env(inicio)
    if not arq or arq in _LIDOS:
        return arq
    _LIDOS.add(arq)
    for linha in arq.read_text(encoding="utf-8-sig").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        nome, bruto = linha.split("=", 1)
        nome = nome.removeprefix("export ").strip()
        v = _interpretar(bruto)
        atual = os.environ.get(nome, "").strip()
        if nome and v and (not atual or atual.startswith(MARCADORES)):
            os.environ[nome] = v
    return arq


def valor(nome: str) -> str:
    """O valor da variável, ou "" quando falta ou ainda é o marcador do `.env.example`."""
    carregar_env()
    v = os.environ.get(nome, "").strip()
    return "" if (not v or v.startswith(MARCADORES)) else v
