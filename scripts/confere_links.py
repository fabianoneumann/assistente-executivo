#!/usr/bin/env python3
"""Confere os links internos dos markdown: `[texto](caminho)`, os `[[ficha-ou-síntese]]` e os caminhos citados em crase.

Uso, da raiz:  python -X utf8 scripts/confere_links.py [pastas...]

- link markdown relativo: o arquivo tem de existir (a âncora `#...` não se confere);
- `[[nome]]`: tem de existir um `nome.md` em algum lugar de `knowledge/`;
- caminho em crase que começa por uma pasta do repositório (`knowledge/`, `decisions/`, `context/`,
  `marketing/`, `scripts/`, `.claude/`) ou por uma área da base (`content-design/`, `agent-engineering/`..., lida a
  partir de `knowledge/`) e termina em `.md`, `.py`, `.json`, `.css`, `.js` ou `.html`: tem de existir, salvo quando
  tem marcador (`<...>`, `*`, `AAAA`) ou o trecho em volta dele (umas 80 letras de cada lado) diz que é proposto
  ("quando houver", "a criar", "proposto", "precisa ter", "não existe").

As fichas de `knowledge/sources/` ficam fora: o texto integral de uma fonte traz os links relativos dela.

Sai com 1 se achar link quebrado.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
IGNORAR = {".git", "__pycache__", "node_modules", ".venv", "dist", "originals"}
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
WIKI = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
AREAS = sorted(d.name for d in (RAIZ / "knowledge").iterdir() if d.is_dir() and d.name != "sources")
CRASE = re.compile(r"`((?:knowledge|decisions|context|marketing|scripts|\.claude|" + "|".join(map(re.escape, AREAS))
                   + r")/[^`\s]+?\.(?:md|py|json|css|js|html))(?::[\d-]+)?`")
VIZINHANCA = 80  # quantas letras antes e depois do caminho se leem para achar o "proposto"
FORA_DO_GIT = {".claude/settings.local.json"}  # existe só na máquina de cada pessoa
PROPOSTO = re.compile(r"(?i)quando houver|a criar|propost|propõe|precisa ter|não existe|ainda não|segunda versão|se houver|crie|criar")


def main(argv: list[str]) -> int:
    bases = [RAIZ / a for a in argv] or [RAIZ]
    nomes_base = {p.stem for p in (RAIZ / "knowledge").rglob("*.md")}
    quebrados = []
    for base in bases:
        for p in ([base] if base.is_file() else base.rglob("*.md")):
            if IGNORAR & set(p.relative_to(RAIZ).parts) or p.relative_to(RAIZ).as_posix().startswith("knowledge/sources/2"):
                continue
            rel = p.relative_to(RAIZ).as_posix()
            em_codigo = False
            for n, linha in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                if linha.lstrip().startswith("```"):
                    em_codigo = not em_codigo
                    continue
                if em_codigo:
                    continue
                for alvo in MD_LINK.findall(linha):
                    if re.match(r"^[a-z]+:|^#|^mailto:", alvo):
                        continue
                    caminho = (p.parent / alvo.split("#")[0]).resolve()
                    if alvo.split("#")[0] and not caminho.exists():
                        quebrados.append((rel, n, "link", alvo))
                for nome in WIKI.findall(linha):
                    if nome.strip() not in nomes_base and not re.match(r"^(\.\.\.|nome)", nome.strip()):
                        quebrados.append((rel, n, "[[...]]", nome.strip()))
                for m in CRASE.finditer(linha):
                    alvo = m.group(1)
                    perto = linha[max(0, m.start() - VIZINHANCA):m.end() + VIZINHANCA]
                    if re.search(r"<|\*|AAAA|\{", alvo) or PROPOSTO.search(perto):
                        continue
                    skill = re.match(r"(\.claude/skills/[^/]+)/", rel)
                    if (alvo in FORA_DO_GIT or (skill and (RAIZ / skill.group(1) / alvo).exists())
                            or (p.parent / alvo).exists() or (RAIZ / "knowledge" / alvo).exists()):
                        continue
                    if not (RAIZ / alvo).exists():
                        quebrados.append((rel, n, "caminho", alvo))
    # os agentes têm duas cópias: .claude/agents/ (o clone) e agents/ (o plugin); as duas têm de ser iguais
    for ag in sorted((RAIZ / ".claude/agents").glob("*.md")):
        par = RAIZ / "agents" / ag.name
        if not par.exists() or par.read_bytes() != ag.read_bytes():
            quebrados.append(("agents/" + ag.name, 0, "cópia do agente", "difere de .claude/agents/" + ag.name + " (ou falta)"))
    for rel, n, tipo, alvo in quebrados:
        print(f"{rel}:{n}: [{tipo}] {alvo}")
    print(f"-- {len(quebrados)} link(s) quebrado(s)")
    return 1 if quebrados else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
