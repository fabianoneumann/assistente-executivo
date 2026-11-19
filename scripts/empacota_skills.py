#!/usr/bin/env python3
"""Empacota as skills em ZIP para subir à conta do claude.ai (Customize > Skills), a rota da conversa do app (o chat, sem pasta; ainda por testar).

Uso, da raiz:
  python -X utf8 scripts/empacota_skills.py                    # todas, em dist/
  python -X utf8 scripts/empacota_skills.py idea-capture review # só estas

O upload à conta aceita só seis campos no frontmatter (name, description, license, compatibility, metadata,
allowed-tools): outro campo faz o envio falhar. Este script tira os outros (por exemplo `context`, `agent` e
`background` das skills de subagente) e avisa o que muda com isso. Avisa também quando a skill usa a injeção
`!` ou variáveis do Claude Code, que a conversa do claude.ai não roda.

O ZIP leva a pasta da skill inteira, menos `__pycache__`, `.venv` e `originals/`. A pasta `dist/` fica fora do git.
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SKILLS = RAIZ / ".claude/skills"
CAMPOS_ACEITOS = ("name", "description", "license", "compatibility", "metadata", "allowed-tools")
FORA = {"__pycache__", ".venv", "originals", "node_modules"}


def separar(texto: str) -> tuple[list[str], str]:
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", texto, re.S)
    if not m:
        raise SystemExit("SKILL.md sem frontmatter")
    return m.group(1).splitlines(), texto[m.end():]


def limpar_frontmatter(linhas: list[str]) -> tuple[list[str], list[str]]:
    """Mantém só os campos aceitos (com as linhas de continuação deles); devolve (linhas, campos tirados)."""
    saida, tirados, manter = [], [], False
    for linha in linhas:
        m = re.match(r"^([A-Za-z_-]+):", linha)
        if m:
            manter = m.group(1) in CAMPOS_ACEITOS
            if not manter:
                tirados.append(m.group(1))
        if manter:
            saida.append(linha)
    return saida, tirados


def empacotar(nome: str, dist: Path) -> list[str]:
    pasta = SKILLS / nome
    skill_md = pasta / "SKILL.md"
    if not skill_md.is_file():
        return [f"[ERRO] {nome}: sem SKILL.md"]
    fm, corpo = separar(skill_md.read_text(encoding="utf-8"))
    fm, tirados = limpar_frontmatter(fm)
    avisos = []
    if tirados:
        avisos.append(f"{nome}: tirados do frontmatter {', '.join(tirados)}"
                      + (" (na conta, a skill roda na conversa principal, não num subagente isolado)" if "context" in tirados else ""))
    if re.search(r"^!`|\s!`", corpo, re.M):
        avisos.append(f"{nome}: usa a injeção `!`, que a conversa do claude.ai troca por um aviso")
    if "${CLAUDE_" in corpo:
        avisos.append(f"{nome}: usa variáveis ${{CLAUDE_...}}, que a skill da conta não substitui")
    if (pasta / "scripts").is_dir():
        avisos.append(f"{nome}: tem scripts; na conta, eles rodam só com \"Code execution and file creation\" ligado, "
                      "e as chaves do .env não vão junto (teste na conversa do app antes de prometer)")
    dist.mkdir(exist_ok=True)
    destino = dist / f"{nome}.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{nome}/SKILL.md", "---\n" + "\n".join(fm) + "\n---\n" + corpo)
        for p in sorted(pasta.rglob("*")):
            rel = p.relative_to(pasta)
            if p.is_dir() or p == skill_md or FORA & set(rel.parts):
                continue
            z.write(p, f"{nome}/{rel.as_posix()}")
    return [f"[OK] {destino.relative_to(RAIZ).as_posix()}"] + [f"  aviso: {a}" for a in avisos]


def main(argv: list[str]) -> int:
    nomes = argv or sorted(p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())
    erro = False
    for n in nomes:
        for linha in empacotar(n, RAIZ / "dist"):
            erro |= linha.startswith("[ERRO]")
            print(linha)
    print("Para subir: claude.ai > Customize > Skills > enviar o ZIP (uma skill por ZIP). Ver README, caminho 2, \"Ainda por testar\".")
    return 1 if erro else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
