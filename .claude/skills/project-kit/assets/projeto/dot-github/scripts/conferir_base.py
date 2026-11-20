"""Confere, no CI, que o roteador e a base não derivaram do repositório.

  python3 .github/scripts/conferir_base.py [raiz]

ERRO (código 1):
- o caminho citado em crase no CLAUDE.md ou no AGENTS.md que não existe;
- o comando da seção "Stack e comandos" do CLAUDE.md que aponta para o que não existe (o script do package.json, o
  arquivo que o python roda);
- o passo do CI (o formato, o lint, o smoke, os testes) cujo comando o CLAUDE.md não lista, ou que sumiu ou mudou de
  nome: um dos dois derivou;
- a falta do knowledge/index.md, e a página dele que não existe.
AVISO (código 0):
- a página de knowledge/ que o index.md não lista (a órfã);
- o caminho de código citado em crase na base que não existe mais (a base fala de um arquivo que saiu ou mudou de
  nome). É aviso, e não erro, porque a base também descreve o que ainda vai existir.
Não confere: o que tem marcador (NNN, <...>, *, X.Y.Z, AAAA), o que o texto perto do caminho diz que ainda vai
existir ("quando houver", "quando ela existir", "nasce no primeiro"), o .env, e o log da base, que é histórico.
Só a biblioteca padrão, para rodar no CI sem instalar nada.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

CRASE = re.compile(r"`([^`\n]+)`")
ARQUIVO = re.compile(r"^[\w.-]+\.(?:md|py|json|ya?ml|html|toml|txt|sh|js|ts|css)$")
MARCADOR = re.compile(r"NNN|<|>|\*|X\.Y\.Z|AAAA|\{|\}|\$")
# O que diz que o caminho ainda vai existir, lido só perto dele (VIZINHANCA letras de cada lado) e como palavra
# inteira: "a criar" não casa dentro de "para criar".
AINDA_NAO = re.compile(r"(?i)(?<!\w)(?:quando houver|quando ela existir|quando existir|nasce no primeiro|a criar|"
                       r"ainda não existe|se houver)(?!\w)")
VIZINHANCA = 80
FORA_DO_GIT = {".env", ".env.local", ".env.production", ".claude/settings.local.json"}  # existem só na máquina de cada um
# Pastas que o projeto tem ou costuma ter: o caminho que começa por uma delas é do repositório, mesmo que ela ainda
# não exista; o que começa por outra coisa (origin/main, owner/repo) não é caminho deste repositório.
PASTAS = {"knowledge", "onboarding", "docs", ".github", ".claude", ".githooks", "src", "app", "test", "tests",
          "spike", "scripts"}
PULAR = {".git", "node_modules", ".venv", "__pycache__", "dist"}
PASSOS_DO_CI = ("O formato", "O lint", "O smoke", "Os testes")


def texto(arq: Path) -> str:
    try:
        return arq.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def candidato(alvo: str, raiz: Path) -> bool:
    """O trecho em crase é um caminho deste repositório?"""
    # a barra no começo é rota (`/health`) ou comando (`/code-review`), e não caminho do repositório
    if (" " in alvo or "://" in alvo or alvo.startswith(("-", "/")) or MARCADOR.search(alvo)
            or alvo in FORA_DO_GIT):
        return False
    if "/" in alvo:
        primeira = alvo.split("/")[0]
        return primeira in PASTAS or (raiz / primeira).is_dir()
    return bool(ARQUIVO.match(alvo))


_NOMES: dict[Path, set[str]] = {}


def nomes(raiz: Path) -> set[str]:
    """Os nomes de arquivo e de pasta do repositório, numa passada só, sem entrar em node_modules, .git e afins."""
    if raiz not in _NOMES:
        achados = set()
        for pasta, subpastas, arquivos in os.walk(raiz):
            subpastas[:] = [d for d in subpastas if d not in PULAR]
            achados.update(subpastas)
            achados.update(arquivos)
        _NOMES[raiz] = achados
    return _NOMES[raiz]


def existe(alvo: str, raiz: Path, perto: Path) -> bool:
    limpo = alvo.rstrip("/").split(":")[0]
    if (raiz / limpo).exists() or (perto / limpo).exists() or (raiz / "knowledge" / limpo).exists():
        return True
    if "/" not in limpo:  # o nome sozinho (`000-modelo.md`): vale se existe em algum lugar do repositório
        return limpo in nomes(raiz)
    return False


def caminhos(arq: Path, raiz: Path):
    """(linha, alvo) de cada caminho citado em crase que não existe, fora o que o texto perto dele diz que ainda vai
    existir."""
    em_codigo = False
    for n, linha in enumerate(texto(arq).splitlines(), 1):
        if linha.lstrip().startswith("```"):
            em_codigo = not em_codigo
            continue
        if em_codigo:
            continue
        for m in CRASE.finditer(linha):
            alvo = m.group(1).strip()
            perto = linha[max(0, m.start() - VIZINHANCA):m.end() + VIZINHANCA]
            if AINDA_NAO.search(perto):
                continue
            if candidato(alvo, raiz) and not existe(alvo, raiz, arq.parent):
                yield n, alvo


def secao(md: str, titulo: str) -> str:
    m = re.search(rf"^## {re.escape(titulo)}\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    return m.group(1) if m else ""


def comandos_do_claude(md: str) -> list[str]:
    return [m.group(1).strip() for m in CRASE.finditer(secao(md, "Stack e comandos")) if " " in m.group(1).strip()]


def conferir_comando(cmd: str, raiz: Path) -> str | None:
    partes = cmd.split()
    if partes[0] == "npm":
        resto = [p for p in partes[1:] if not p.startswith("-")]  # as flags (--silent, -s) não são o script
        if not resto:
            return None
        if resto[0] in {"run", "run-script"}:
            if len(resto) < 2:
                return None
            nome = resto[1]
        elif resto[0] in {"test", "start", "stop", "restart"}:  # os atalhos do npm para o script de mesmo nome
            nome = resto[0]
        else:  # install, ci, audit, exec...: subcomando do npm, e não script do projeto
            return None
        try:
            dados = json.loads(texto(raiz / "package.json") or "{}")
        except ValueError:
            return "o package.json não é JSON válido"
        scripts = dados.get("scripts", {}) if isinstance(dados, dict) else None
        if not isinstance(scripts, dict):
            return "o package.json não tem um objeto scripts"
        return None if nome in scripts else f"o package.json não tem o script {nome!r}"
    if partes[0] in {"python", "python3", "py"}:
        if "-m" in partes or "-c" in partes:  # roda um módulo ou um trecho, e não um arquivo
            return None
        arquivo = next((p for p in partes[1:] if not p.startswith("-") and p != "utf8"), None)
        if arquivo and arquivo.endswith(".py") and not (raiz / arquivo).is_file():
            return f"o arquivo {arquivo} não existe"
    return None


def escalar(valor: str) -> str:
    """O valor de uma linha do YAML sem as aspas: as duplas com os escapes do JSON, as simples com o '' do YAML."""
    if valor.startswith('"'):
        try:
            return json.loads(valor)
        except ValueError:
            return valor
    if valor.startswith("'") and valor.endswith("'") and len(valor) > 1:
        return valor[1:-1].replace("''", "'")
    return re.sub(r"\s+#.*$", "", valor)  # sem aspas, o " #" abre um comentário do YAML


def passos(ci: str):
    """As linhas de cada passo de uma lista de `steps:`, do `- ` até o próximo `- ` na mesma coluna."""
    linhas = ci.splitlines()
    inicio = [(i, len(l) - len(l.lstrip())) for i, l in enumerate(linhas) if re.match(r"^\s*-\s", l)]
    for k, (i, col) in enumerate(inicio):
        fim = len(linhas)
        for j in range(i + 1, len(linhas)):
            l = linhas[j]
            recuo = len(l) - len(l.lstrip())
            if l.strip() and (recuo < col or (recuo == col and l.lstrip().startswith("- "))):
                fim = j
                break
        yield col, linhas[i:fim]


def comandos_do_ci(ci: str) -> list[tuple[str, list[str]]]:
    """(passo, comandos) dos passos do CI que o CLAUDE.md também lista. No `run: |`, cada linha do bloco conta."""
    achados = []
    for col, bloco in passos(ci):
        nome = run = None
        for n, linha in enumerate(bloco):
            corpo = linha.strip().removeprefix("- ").strip()
            m = re.match(r"^(name|run):\s*(.*?)\s*$", corpo)
            if not m:
                continue
            if m.group(1) == "name":
                nome = escalar(m.group(2))
            elif m.group(2) in {"|", ">", "|-", ">-"}:
                run = [l.strip() for l in bloco[n + 1:] if l.strip()]
            else:
                run = [escalar(m.group(2))]
        if nome in PASSOS_DO_CI and run:
            achados.append((nome, run))
    return achados


def paginas_do_indice(md: str) -> list[str]:
    """A página de cada linha da tabela do índice: o primeiro caminho em crase da primeira célula, ou o alvo do link."""
    paginas = []
    for linha in md.splitlines():
        if not linha.startswith("|") or re.match(r"^\|[\s:|-]*$", linha):
            continue
        celula = linha.split("|")[1]
        m = re.search(r"`([^`]+)`", celula) or re.search(r"\]\(([^)#\s]+)", celula)
        if m:
            paginas.append(m.group(1))
    return paginas


def conferir(raiz: Path) -> tuple[list[str], list[str]]:
    erros, avisos = [], []
    _NOMES.pop(raiz, None)  # a lista de nomes vale para uma rodada, e não para a seguinte
    for nome in ("CLAUDE.md", "AGENTS.md"):
        arq = raiz / nome
        if not arq.is_file():
            erros.append(f"falta o {nome}")
            continue
        for n, alvo in caminhos(arq, raiz):
            erros.append(f"{nome}:{n}: cita `{alvo}`, que não existe")
    claude = texto(raiz / "CLAUDE.md")
    cmds = comandos_do_claude(claude)
    for cmd in cmds:
        problema = conferir_comando(cmd, raiz)
        if problema:
            erros.append(f"CLAUDE.md: o comando `{cmd}` não roda: {problema}")
    normal = {" ".join(c.split()) for c in cmds}
    do_ci = comandos_do_ci(texto(raiz / ".github/workflows/ci.yml"))
    for passo, cmds_do_passo in do_ci:
        if not any(" ".join(c.split()) in normal for c in cmds_do_passo):
            erros.append(f"ci.yml: o passo {passo!r} roda `{' / '.join(cmds_do_passo)}`, que o CLAUDE.md (\"Stack e comandos\") não lista: um dos dois derivou")
    for passo in sorted(set(PASSOS_DO_CI) - {p for p, _ in do_ci}, key=PASSOS_DO_CI.index):
        erros.append(f"ci.yml: falta o passo {passo!r} (com esse nome), e o CLAUDE.md diz que o CI o roda")
    base = raiz / "knowledge"
    if not (base / "index.md").is_file():
        erros.append("falta o knowledge/index.md, a entrada da base")
    indice = texto(base / "index.md")
    listadas = paginas_do_indice(indice)
    for pagina in listadas:
        if not (base / pagina).exists():
            erros.append(f"knowledge/index.md lista `{pagina}`, que não existe")
    if base.is_dir():
        for p in sorted(base.glob("*.md")):
            if p.name != "index.md" and p.name not in listadas:
                avisos.append(f"knowledge/{p.name} não está no index.md (a página órfã não se acha)")
        for p in sorted(base.rglob("*.md")):
            rel = p.relative_to(raiz).as_posix()
            if rel == "knowledge/log.md" or "analysis" in p.relative_to(base).parts[:1]:
                continue
            for n, alvo in caminhos(p, raiz):
                if not alvo.endswith("/"):  # a pasta citada pela base (`docs/`, `spike/`) nasce quando precisa
                    avisos.append(f"{rel}:{n}: cita `{alvo}`, que não existe (a base derivou do código?)")
    return erros, avisos


def main(argv: list[str]) -> int:
    raiz = Path(argv[1]) if len(argv) > 1 else Path(".")
    erros, avisos = conferir(raiz)
    for e in erros:
        print(f"ERRO: {e}")
    for a in avisos:
        print(f"AVISO: {a}")
    print(f"{len(erros)} ERRO, {len(avisos)} AVISO")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
