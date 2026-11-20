"""Confere um projeto montado pela skill `project-kit`, antes do primeiro commit e depois de cada ajuste no kit.

  python -X utf8 conferir.py <pasta do projeto>

ERRO barra o commit; AVISO se lê e se diz. Confere: nenhum marcador `{{X}}`, `[kit:` ou `<!-- kit:` sobrou; os YAML
e os JSON são válidos; o `CLAUDE.md` tem até 150 linhas; nenhum caminho absoluto nem menção ao ambiente de onde o kit
veio; as ações do CI fixadas por hash; o Dependabot só de segurança; o `.gitattributes` com `eol=lf` e o log em
`merge=union`; o `settings.json` com o `deny` e sem `ask`; as cascas em LF; os arquivos que o fluxo cita existem; e,
no projeto com imagem, que as peças dela vieram juntas (o `Dockerfile` não nasce sem o vigia, nem o vigia sem ele) e
que o Trivy do vigia está fixado pelo hash.
Código 0 sem ERRO, 1 com ERRO.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

OBRIGATORIOS = [
    "CLAUDE.md", "AGENTS.md", "README.md", ".gitattributes", ".gitignore", ".editorconfig",
    ".github/ISSUE_TEMPLATE/spec.md", ".github/ISSUE_TEMPLATE/defeito.md", ".github/ISSUE_TEMPLATE/config.yml",
    ".github/PULL_REQUEST_TEMPLATE.md", ".github/dependabot.yml", ".github/release.yml", ".github/workflows/ci.yml",
    ".claude/settings.json", ".claude/hooks/fluxo.py", ".claude/hooks/fluxo.sh", ".claude/hooks/test_fluxo.py",
    ".githooks/pre-commit", ".githooks/pre-push", ".githooks/hooks.py", ".githooks/test_hooks.py", ".githooks/config.json",
    "knowledge/README.md", "knowledge/index.md", "knowledge/log.md", "knowledge/processo.md", "knowledge/metadados.md",
    "knowledge/travas.md", "knowledge/versao-e-dependencias.md", "knowledge/plano.md", "knowledge/arquitetura.md",
    "knowledge/decisions/000-modelo.md", "onboarding/index.html",
    "onboarding/diagramas/travas.html", "onboarding/diagramas/prioridade.html", "onboarding/diagramas/sequencia.html", "onboarding/diagramas/elk.bundled.js",
    "onboarding/diagramas/elk-LICENSE.md", "onboarding/diagramas/tokens.css", "onboarding/diagramas/esquema.py",
]
SOBRAS = [re.compile(r"\{\{[A-Z_]+\}\}"), re.compile(r"\[kit:"), re.compile(r"<!--\s*kit:")]
ABSOLUTO = re.compile(r"(?<![\w/])[A-Za-z]:[\\/][\w. -]|(?<![\w.])/(?:Users|home|mnt/[a-z])/\w")
ORIGEM = re.compile(r"assistente-executivo", re.I)
ISSUE = re.compile(r"(?:\b(?:a|na|da|issue|PR|PRs)\s+#|\(#)\d{2,5}\b")  # número de issue de outro repositório nos modelos de página
VAULT = re.compile(r"\bvault\b", re.I)  # só AVISO: um projeto pode ter um "Vault" de verdade (o de segredos)
SHA = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.M)
# As peças da imagem saem dos próprios modelos (assets/docker/comum, mais o Dockerfile da stack), para a lista não
# divergir quando o kit ganhar uma peça.
_MODELOS_DOCKER = Path(__file__).resolve().parents[1] / "assets" / "docker" / "comum"
DOCKER = ["Dockerfile"] + sorted(
    "/".join(("." + p[4:]) if p.startswith("dot-") else p for p in arq.relative_to(_MODELOS_DOCKER).parts)
    for arq in _MODELOS_DOCKER.rglob("*") if arq.is_file() and "__pycache__" not in arq.parts)
SEM_TETO = {"knowledge/log.md", "knowledge/index.md", "onboarding/diagramas/elk-LICENSE.md"}  # a licença é texto de terceiro


def texto_de(arq: Path) -> str | None:
    try:
        return arq.read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def conferir(pasta: Path) -> tuple[list[str], list[str]]:
    erros, avisos = [], []
    for rel in OBRIGATORIOS:
        if not (pasta / rel).is_file():
            erros.append(f"falta {rel}")
    for numero, tema in (("001", "a arquitetura e a stack"), ("002", "o ferramental")):
        if not list((pasta / "knowledge/decisions").glob(f"{numero}-*.md")):
            erros.append(f"falta o ADR {numero} ({tema}) em knowledge/decisions/")

    arquivos = [p for p in pasta.rglob("*") if p.is_file() and ".git" not in p.relative_to(pasta).parts[:1]
                and not {"node_modules", ".venv", "__pycache__"} & set(p.parts)]
    for arq in arquivos:
        rel = arq.relative_to(pasta).as_posix()
        texto = texto_de(arq)
        if texto is None:
            continue
        for padrao in SOBRAS:
            m = padrao.search(texto)
            if m:
                linha = texto[: m.start()].count("\n") + 1
                erros.append(f"{rel}:{linha}: sobrou o marcador {m.group(0)!r} do kit")
        m = ABSOLUTO.search(texto)
        if m:
            erros.append(f"{rel}:{texto[: m.start()].count(chr(10)) + 1}: caminho absoluto ({m.group(0)!r}); cite pelo nome ou pelo caminho relativo")
        m = ORIGEM.search(texto)
        if m:
            erros.append(f"{rel}:{texto[: m.start()].count(chr(10)) + 1}: menção ao ambiente de onde o kit veio ({m.group(0)!r}); o projeto não o cita")
        if rel.startswith("onboarding/") and rel.endswith(".html"):
            m = ISSUE.search(texto)
            if m:
                erros.append(f"{rel}: o número de issue {m.group(0)!r} veio do modelo; o projeto não o cita")
        m = VAULT.search(texto)
        if m:
            avisos.append(f"{rel}:{texto[: m.start()].count(chr(10)) + 1}: a palavra {m.group(0)!r}; se fala do ambiente de onde o kit veio, tire (o projeto não o cita)")
        if rel.endswith(".md") and rel not in SEM_TETO and rel != "CLAUDE.md" and texto.count("\n") > 150:
            avisos.append(f"{rel} tem {texto.count(chr(10))} linhas, acima do teto de ~150")
        if (rel.endswith(".sh") or rel.startswith(".githooks/pre-")) and "\r" in texto:
            erros.append(f"{rel}: a casca está em CRLF, e o sh do git não a roda")

    claude = texto_de(pasta / "CLAUDE.md") or ""
    if claude.count("\n") > 150:
        erros.append(f"CLAUDE.md tem {claude.count(chr(10))} linhas, acima de 150")

    conferir_yaml(pasta, erros, avisos)
    conferir_json(pasta, erros)
    conferir_ci(pasta, erros, avisos)
    conferir_docker(pasta, erros)
    attrs = texto_de(pasta / ".gitattributes") or ""
    if "eol=lf" not in attrs:
        erros.append(".gitattributes sem eol=lf")
    if not re.search(r"^knowledge/log\.md\s+merge=union", attrs, re.M):
        erros.append(".gitattributes sem o knowledge/log.md em merge=union")
    if (pasta / ".git").exists():
        r = subprocess.run(["git", "config", "--get", "core.hooksPath"], cwd=pasta, capture_output=True, text=True)
        if r.stdout.strip() != ".githooks":
            avisos.append("o core.hooksPath deste clone não é .githooks: os hooks do git estão desligados")
    return erros, avisos


def conferir_yaml(pasta: Path, erros: list[str], avisos: list[str]) -> None:
    try:
        import yaml
    except ImportError:
        avisos.append("sem o PyYAML: os YAML não foram validados (o GitHub os valida no primeiro push)")
        return
    for arq in sorted(pasta.glob(".github/**/*.y*ml")):
        try:
            dados = yaml.safe_load(arq.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            erros.append(f"{arq.relative_to(pasta).as_posix()}: YAML inválido ({str(e).splitlines()[0]})")
            continue
        if arq.name == "dependabot.yml":
            for u in (dados or {}).get("updates", []):
                if u.get("open-pull-requests-limit") != 0:
                    erros.append(f"dependabot.yml: {u.get('package-ecosystem')} sem open-pull-requests-limit: 0 (só segurança)")
                if "groups" in u:
                    erros.append(f"dependabot.yml: {u.get('package-ecosystem')} com groups (um PR por pacote)")


def conferir_json(pasta: Path, erros: list[str]) -> None:
    for rel in (".claude/settings.json", ".githooks/config.json", "package.json", "tsconfig.json"):
        arq = pasta / rel
        if not arq.is_file():
            continue
        try:
            dados = json.loads(arq.read_text(encoding="utf-8"))
        except ValueError as e:
            erros.append(f"{rel}: JSON inválido ({e})")
            continue
        if rel == ".claude/settings.json":
            perm = dados.get("permissions", {})
            if perm.get("ask"):
                erros.append(".claude/settings.json tem ask: as travas recusam e dizem o que falta, nunca perguntam")
            if "Read(**/.env)" not in perm.get("deny", []):
                erros.append(".claude/settings.json sem o deny do .env")
            if not any("--no-verify" in r for r in perm.get("deny", [])):
                erros.append(".claude/settings.json sem o deny do --no-verify")
            if perm.get("allow"):
                erros.append(".claude/settings.json tem allow: o kit não libera nada por padrão")


def conferir_ci(pasta: Path, erros: list[str], avisos: list[str]) -> None:
    for wf in sorted(pasta.glob(".github/workflows/*.y*ml")):
        for m in SHA.finditer(texto_de(wf) or ""):
            ref = m.group(1)
            if not re.search(r"@[0-9a-f]{40}$", ref):
                erros.append(f"{wf.name}: a ação {ref} não está fixada pelo hash do commit")
    ci = texto_de(pasta / ".github/workflows/ci.yml") or ""
    teto = re.search(r"timeout-minutes:\s*(\d+)", ci)
    if not teto:
        avisos.append("ci.yml sem timeout-minutes (o teto do CI é de 3 minutos)")
    elif int(teto.group(1)) > 3:
        avisos.append(f"ci.yml com teto de {teto.group(1)} minutos, acima dos 3 de partida")


def conferir_docker(pasta: Path, erros: list[str]) -> None:
    """A imagem vem inteira ou não vem: o Dockerfile sem o vigia é a imagem base sem ninguém olhando, e o vigia sem a
    imagem varre o que não existe."""
    presentes = [rel for rel in DOCKER if (pasta / rel).is_file()]
    if not presentes:
        return
    for rel in DOCKER:
        if rel not in presentes:
            erros.append(f"o projeto tem {presentes[0]} e falta {rel}: a imagem vem inteira (montar.py --docker)")
    ci = texto_de(pasta / ".github/workflows/ci.yml") or ""
    if "docker build --pull" not in ci:
        erros.append("ci.yml sem o build da imagem (docker build --pull): a verificação que mora no build precisa dele")
    vigia = texto_de(pasta / ".github/workflows/vigiar-imagem.yml") or ""
    if not re.search(r"^\s*TRIVY_SHA256:\s*[0-9a-f]{64}\s*$", vigia, re.M):
        erros.append("vigiar-imagem.yml sem o TRIVY_SHA256 de 64 caracteres: o Trivy baixado não seria conferido")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    pasta = Path(argv[1])
    erros, avisos = conferir(pasta)
    for e in erros:
        print(f"ERRO: {e}")
    for a in avisos:
        print(f"AVISO: {a}")
    print(f"{len(erros)} ERRO, {len(avisos)} AVISO em {pasta}")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
