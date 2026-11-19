#!/usr/bin/env python3
"""Procura dado pessoal, dado sensível e conteúdo de terceiro no repositório inteiro, antes de subir.

Uso, da raiz:
  python -X utf8 scripts/confere_dados.py                          # só os padrões genéricos
  python -X utf8 scripts/confere_dados.py --termos ../termos.txt    # e os termos de quem mantém

O que procura sempre (padrões deste arquivo), só no que iria num commit (com o git: os arquivos dele e os novos
fora do .gitignore; o `.env` e as pastas `originals/` ignoradas ficam fora, porque é o lugar delas):
- valor com cara de chave (sk-, pplx-, AIza, ghp_, EAA..., chave privada, atribuição longa a KEY/TOKEN/SECRET,
  sequência hexadecimal de 32 ou mais);
- e-mail fora dos domínios de exemplo, telefone brasileiro, caminho de usuário do Windows (`C:\\Users`);
- id com cara de conta da Meta e do Instagram (17 a 18 dígitos começando por 17 ou 18, `act_<número>`),
  endereço público de bucket R2 (`pub-<hex>.r2.dev`);
- conteúdo de terceiro fora da régua: pasta `originals/` que iria ao git, `sources/archive/`, ficha sem o campo `licenca`,
  ficha de licença não livre com "Texto integral", ficha de prática própria;
- o autor e o e-mail de cada commit do histórico;
- a privacidade: se há registro pessoal (um arquivo de `finance/`, `health/`, `maps/` ou `partners/` que iria num
  commit e não é o modelo, caminho a caminho: os READMEs, os guias de `maps/guides/`, as páginas em branco de
  `maps/board/` e o modelo de `partners/template/`) e algum remoto do GitHub é público, para com [PARE] e diz como deixar o repositório privado.
  Roda sempre, também com pastas. Pede o `gh` com login: quando há registro pessoal e a visibilidade de um remoto
  do GitHub não pôde ser conferida (sem o `gh`, sem login, sem acesso) ou os remotos não puderam ser lidos, sai
  com 3 ("não conferiu") e diz o que falta. O remoto fora do GitHub só gera aviso.

Os termos próprios (nomes de pessoas, de clientes, ids de conta, nomes de curso pago) NÃO ficam neste arquivo,
porque escrevê-los aqui seria levar o dado junto. Ficam num arquivo de texto fora do repositório, um termo por
linha (`#` comenta; o termo casa sem diferença de maiúscula e de acento), passado por `--termos` ou pela
variável CONFERE_DADOS_TERMOS. A linha `!texto` é exceção em todo o repositório (um nome de terceiro que contém
o termo); a linha `!arquivo::texto`, só naquele arquivo (o titular da licença no `LICENSE`).

Sai com 0 quando não acha nada e com 1 quando acha, listando arquivo, linha, tipo e o trecho com o valor
mascarado; com 3 quando não acha nada mas não conseguiu conferir a visibilidade do repositório que tem registro
pessoal (o achado vence: com achado, sai com 1 mesmo assim); com 2 em erro de entrada.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
IGNORAR_PASTAS = {".git", "__pycache__", "node_modules", ".venv", "dist"}
BINARIOS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".mp3", ".wav", ".zip", ".pdf", ".woff", ".woff2", ".ttf", ".otf", ".ico", ".pyc"}
DOMINIOS_OK = ("example.com", "example.org", "example.invalid", "exemplo.com", "anthropic.com", "users.noreply.github.com")
LICENCAS_LIVRES = re.compile(r"\b(CC[- ]?BY(?![- ]?NC)(-SA|-ND)?|CC0|MIT|Apache|BSD|dom[ií]nio p[uú]blico|public domain|governo dos EUA|US government)\b", re.I)

PADROES = [
    ("chave", re.compile(r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}")),
    ("chave", re.compile(r"\bpplx-[A-Za-z0-9]{20,}")),
    ("chave", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}")),
    ("chave", re.compile(r"\b(?:ghp|gho|ghu|ghs)_[A-Za-z0-9]{20,}|\bgithub_pat_[A-Za-z0-9_]{20,}")),
    ("chave", re.compile(r"\bEAA[A-Za-z0-9]{30,}")),
    ("chave", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("chave", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("chave", re.compile(r"(?i)\b[A-Z0-9_]*(?:KEY|TOKEN|SECRET|PASSWORD|SENHA)\b\s*[=:]\s*[\"']?(?!COLE_)[A-Za-z0-9/+_.=-]{20,}")),
    ("chave", re.compile(r"\b[0-9a-f]{32,}\b")),
    ("e-mail", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("e-mail", re.compile(r"\{[^{}\n]*\}\s*@\s*[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),  # {ana, bia}@dominio, como nos artigos
    ("telefone", re.compile(r"(?:\+55\s?)?\(?\b\d{2}\)?\s?9\d{4}[-\s]?\d{4}\b")),
    ("caminho de usuário", re.compile(r"(?i)\b[A-Z]:[\\/]+Users[\\/]|/[a-z]/Users/|\\AppData\\|/AppData/")),
    ("id de conta da Meta", re.compile(r"\b1[78]\d{15,16}\b|\bact_\d{6,}\b")),
    ("endereço de bucket", re.compile(r"\bpub-[0-9a-f]{16,}\.r2\.dev\b")),
]
# as duas regras genéricas de chave (atribuição a KEY/TOKEN e hex longo), as que casam por acaso em código minificado
CHAVES_GENERICAS = [rx for tipo, rx in PADROES if tipo == "chave"][-2:]


def normalizar(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


EXCECOES: list[str] = []
EXCECOES_ARQ: dict[str, list[str]] = {}


def ler_termos(arq: str | None) -> list[str]:
    """Um termo por linha; a linha que começa com `!` é exceção (um nome de terceiro que contém o termo).

    `!arquivo::texto` é a exceção só naquele arquivo, pelo caminho relativo à raiz (o titular da licença no
    `LICENSE`, por exemplo): o mesmo texto em outro arquivo segue acusado."""
    if not arq:
        return []
    termos = []
    for linha in Path(arq).read_text(encoding="utf-8-sig").splitlines():
        linha = linha.split("#", 1)[0].strip()
        if linha.startswith("!") and "::" in linha:
            caminho, texto = linha[1:].split("::", 1)
            EXCECOES_ARQ.setdefault(caminho.strip(), []).append(normalizar(texto.strip()))
        elif linha.startswith("!"):
            EXCECOES.append(normalizar(linha[1:].strip()))
        elif linha:
            termos.append(normalizar(linha))
    return termos


def acha_termo(t: str, texto_norm: str, rel: str = "") -> bool:
    """O termo como palavra inteira (sem casar um nome curto dentro de uma palavra maior), fora das exceções."""
    for e in EXCECOES + EXCECOES_ARQ.get(rel, []):
        texto_norm = texto_norm.replace(e, " ")
    return re.search(r"(?<![a-z0-9])" + re.escape(t) + r"(?![a-z0-9])", texto_norm) is not None


ACAO_COM_HASH = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@$")


def acao_fixada_por_hash(linha: str, m: re.Match) -> bool:
    """O commit de 40 caracteres que fixa uma ação do GitHub (dono/acao@hash), exigido pelo kit (D7).

    Só passa o hash de exatamente 40 caracteres colado no @ de dono/acao; qualquer outra sequência longa segue acusada.
    """
    return len(m.group(0)) == 40 and bool(ACAO_COM_HASH.search(linha[: m.start()]))


SHA256_ANTES = re.compile(r"(?i)sha-?256\W{0,4}$")
VENDORIZADO = (".bundled.js", ".min.js")


def soma_de_verificacao(linha: str, m: re.Match) -> bool:
    """O SHA-256 de 64 caracteres que confere um arquivo baixado ("SHA-256 `b103...`"), não uma chave."""
    return len(m.group(0)) == 64 and bool(SHA256_ANTES.search(linha[: m.start()]))


def generica_em_vendorizado(rel: str, rx: re.Pattern) -> bool:
    """Código de terceiro minificado (`*.bundled.js`, `*.min.js`, que vai com a licença ao lado) casa as regras
    genéricas de chave por acaso (`key:"..."`); nele só valem as de prefixo conhecido (sk-, ghp_, AIza...)."""
    return rel.endswith(VENDORIZADO) and rx in CHAVES_GENERICAS


URL = re.compile(r"https?://[^\s)\]>\"']+|doi:\s*\S+|10\.\d{4,}/\S+")


def dentro_de_url_publica(linha: str, pos: int, anterior: str = "") -> bool:
    """O valor está dentro de uma URL ou DOI citada (o hash de um artigo, o id de um gist), não solto.

    A URL de bucket R2 (`r2.dev`, `r2.cloudflarestorage.com`) não ganha essa folga: ela é da conta."""
    for u in URL.finditer(linha):
        if u.start() <= pos < u.end():
            return not re.search(r"r2\.dev|r2\.cloudflarestorage", u.group(0))
    # o pedaço de URL de artigo quebrado em outra linha de um texto integral (".../<hash>-Paper.pdf", "10.1080/<id>")
    antes, depois = linha[:pos], linha[pos:]
    if (antes.rstrip().endswith("/") or re.match(r"[0-9a-f]{32}-", depois)
            or (not antes.strip() and anterior.rstrip().endswith(("/", "=")))):
        return True
    return False


def mascarar(trecho: str) -> str:
    trecho = trecho.strip()
    return trecho[:3] + "…" + f"({len(trecho)} car.)" if len(trecho) > 6 else trecho[:1] + "…"


def no_commit() -> set[str] | None:
    """O que iria num commit: os arquivos do git e os novos fora do .gitignore. None quando o git não responde
    (o modelo baixado em ZIP, sem repositório): aí se confere a pasta inteira."""
    try:
        r = subprocess.run(["git", "-C", str(RAIZ), "ls-files", "-co", "--exclude-standard"],
                           capture_output=True, text=True, encoding="utf-8")
    except OSError:
        return None
    if r.returncode != 0:
        return None
    return {x for x in r.stdout.splitlines() if x.strip()}


def arquivos(pastas: list[str] | None = None, so_o_que_vai: bool = True) -> list[Path]:
    """Os arquivos a conferir. Com o git, só o que iria num commit: o que o .gitignore tira (o `.env`, as pastas
    `originals/` com o laudo e o extrato) fica fora, porque é o lugar certo dele."""
    saida = []
    vai = no_commit() if so_o_que_vai else None
    bases = [RAIZ / x for x in pastas] if pastas else [RAIZ]
    for p in (q for b in bases for q in ([b] if b.is_file() else b.rglob("*"))):
        rel = p.relative_to(RAIZ)
        if any(parte in IGNORAR_PASTAS for parte in rel.parts):
            continue
        if vai is not None and rel.as_posix() not in vai:
            continue
        if p.is_file():
            saida.append(p)
    return saida


def frontmatter(texto: str) -> str:
    m = re.match(r"^---\r?\n(.*?)\r?\n---", texto, re.S)
    return m.group(1) if m else ""


def conferir_ficha(rel: str, texto: str, achados: list):
    fm = frontmatter(texto)
    m = re.search(r"^licenca:\s*(.+)$", fm, re.M)
    if not m:
        achados.append((rel, 1, "terceiro", "ficha sem o campo `licenca` (classificar antes de levar)"))
        return
    lic = m.group(1)
    if re.search(r"(?i)pago|curso comprado", lic):
        achados.append((rel, 1, "terceiro", "ficha de material pago"))
    if re.search(r"^tipo:\s*pratica-propria", fm, re.M):
        achados.append((rel, 1, "terceiro", "ficha de prática própria (é de quem a escreveu, não do modelo)"))
    if re.search(r"(?im)^#+\s*texto integral", texto) and not LICENCAS_LIVRES.search(lic):
        achados.append((rel, 1, "terceiro", f"texto integral com licença não livre ({lic.strip()[:40]})"))


def conferir(termos: list[str], pastas: list[str] | None = None) -> list[tuple]:
    achados = []
    for p in arquivos(pastas):
        rel = p.relative_to(RAIZ).as_posix()
        partes = rel.split("/")
        if "originals" in partes:
            achados.append((rel, 0, "terceiro", "arquivo dentro de uma pasta originals/"))
        if "/sources/archive/" in f"/{rel}":
            achados.append((rel, 0, "terceiro", "arquivo em sources/archive/ (material pago)"))
        nome_norm = normalizar(rel)
        for t in termos:
            if acha_termo(t, nome_norm):
                achados.append((rel, 0, "termo próprio", f"no nome do arquivo: {mascarar(t)}"))
        if p.suffix.lower() in BINARIOS:
            continue
        try:
            texto = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            achados.append((rel, 0, "ilegível", "arquivo que não é UTF-8 nem binário conhecido: conferir à mão"))
            continue
        if rel.startswith("knowledge/sources/") and p.suffix == ".md" and p.name != "README.md":
            conferir_ficha(rel, texto, achados)
        linhas = texto.splitlines()
        for n, linha in enumerate(linhas, 1):
            if rel == "scripts/confere_dados.py" and "re.compile(" in linha:
                continue  # as próprias expressões deste arquivo
            for tipo, rx in PADROES:
                for m in rx.finditer(linha):
                    v = m.group(0)
                    if tipo == "e-mail" and v.lower().endswith(DOMINIOS_OK):
                        continue
                    if tipo == "chave" and (acao_fixada_por_hash(linha, m) or soma_de_verificacao(linha, m)
                                            or generica_em_vendorizado(rel, rx)):
                        continue
                    if tipo in ("chave", "id de conta da Meta") and dentro_de_url_publica(linha, m.start(), linhas[n - 2] if n > 1 else ""):
                        continue
                    achados.append((rel, n, tipo, mascarar(v)))
            if termos:
                ln = normalizar(linha)
                for t in termos:
                    if acha_termo(t, ln, rel):
                        achados.append((rel, n, "termo próprio", mascarar(t)))
    return achados


def conferir_git(termos: list[str]) -> list[tuple]:
    try:
        saida = subprocess.run(["git", "-C", str(RAIZ), "log", "--all", "--format=%an <%ae>|%cn <%ce>"],
                               capture_output=True, text=True, encoding="utf-8").stdout
    except OSError:
        return []
    achados = []
    for autor in sorted(set(x for linha in saida.splitlines() for x in linha.split("|") if x)):
        email = autor.rsplit("<", 1)[-1].rstrip(">").lower()
        if not email.endswith(DOMINIOS_OK) or any(acha_termo(t, normalizar(autor)) for t in termos):
            achados.append(("(histórico do git)", 0, "autor de commit", mascarar(autor)))
    return achados


# partners/ guarda dado de terceiro (parceiros, clientes) e segue a mesma regra: só em repositório privado
PASTAS_PESSOAIS = ("finance", "health", "maps", "partners")
# o modelo em branco, caminho a caminho: o que estiver fora desta lista, nestas pastas, é registro de quem usa
MODELO_PESSOAL = {
    "finance/README.md", "finance/personal/README.md",
    "health/README.md", "health/training/README.md", "health/nutrition/README.md",
    "health/medical/README.md", "health/psychological/README.md",
    "maps/README.md", "maps/board/index.html", "maps/board/tokens.css",
    *(f"maps/guides/{g}.md" for g in ("big-five", "erec", "ikigai", "okr", "roda-da-vida", "swot", "vision-board")),
    "partners/README.md",
}
# o modelo da pasta de um parceiro: tudo dentro dele é esqueleto, sem dado de ninguém
MODELO_PREFIXOS = ("partners/template/",)
# a página do quadro só é modelo enquanto traz o aviso de modelo em branco; preenchida no lugar, vira registro
QUADRO_EM_BRANCO = {"maps/board/roda-da-vida.html", "maps/board/ikigai.html"}
MARCA_EM_BRANCO = "Modelo em branco"
GITHUB = re.compile(r"(?:^|[@/])(?:www\.)?github\.com[:/]+([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?/*$", re.I)


def _candidatos() -> tuple[list[str], str | None]:
    """Os arquivos das pastas pessoais que iriam num commit: os do git e os novos fora do .gitignore.

    Sem o git (o modelo baixado em ZIP), cai na varredura da pasta e diz isso no aviso."""
    pastas = [x for x in PASTAS_PESSOAIS if (RAIZ / x).is_dir()]
    if not pastas:
        return [], None
    try:
        r = subprocess.run(["git", "-C", str(RAIZ), "ls-files", "-co", "--exclude-standard", "--", *pastas],
                           capture_output=True, text=True, encoding="utf-8")
        if r.returncode == 0:
            return [x for x in r.stdout.splitlines() if x.strip()], None
    except OSError:
        pass
    return [p.relative_to(RAIZ).as_posix() for p in arquivos(pastas)], "não deu para perguntar ao git o que vai num commit; contei os arquivos da pasta"


def e_modelo(rel: str) -> bool:
    if rel in QUADRO_EM_BRANCO:
        try:
            return MARCA_EM_BRANCO in (RAIZ / rel).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return False
    return rel in MODELO_PESSOAL or rel.startswith(MODELO_PREFIXOS)


def registros_pessoais() -> list[str]:
    """Os arquivos de finance/, health/, maps/ e partners/ que não são o modelo em branco: o registro de quem usa."""
    return sorted(rel for rel in _candidatos()[0] if not e_modelo(rel))


def remotos() -> list[str] | None:
    """As URLs dos remotos; None quando o git não respondeu."""
    try:
        r = subprocess.run(["git", "-C", str(RAIZ), "remote", "-v"], capture_output=True, text=True, encoding="utf-8")
    except OSError:
        return None
    if r.returncode != 0:
        return None
    return sorted({linha.split()[1] for linha in r.stdout.splitlines() if len(linha.split()) >= 2})


def visibilidade(repo: str) -> str | None:
    """PUBLIC, PRIVATE ou INTERNAL pelo `gh`; None quando não deu para saber (sem o gh, sem login, sem acesso)."""
    try:
        r = subprocess.run(["gh", "repo", "view", repo, "--json", "visibility", "--jq", ".visibility"],
                           capture_output=True, text=True, encoding="utf-8", timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    v = r.stdout.strip().upper()
    return v if r.returncode == 0 and v in ("PUBLIC", "PRIVATE", "INTERNAL") else None


def conferir_privacidade() -> tuple[list[tuple], list[str], list[str], bool]:
    """Registro pessoal num repositório com remoto público vira achado; o que não deu para conferir vira aviso.

    Devolve os achados, os avisos, os repositórios públicos (para a mensagem do [PARE]) e se ficou sem conferir
    (os remotos não puderam ser lidos, ou a visibilidade de um remoto do GitHub não pôde ser sabida)."""
    candidatos, aviso_git = _candidatos()
    registros = sorted(rel for rel in candidatos if not e_modelo(rel))
    if not registros:
        return [], [], [], False
    achados, avisos, publicos, nao_conferiu = [], ([aviso_git] if aviso_git else []), [], False
    urls = remotos()
    if urls is None:
        avisos.append("há registro pessoal e não deu para ler os remotos do git: confira à mão se o repositório é privado")
        nao_conferiu = True
        urls = []
    vistos = set()
    pastas = sorted({r.split("/")[0] + "/" for r in registros})
    for url in urls:
        m = GITHUB.search(url)
        if not m:
            avisos.append(f"um remoto fora do GitHub ({mascarar(url)}): confira à mão se ele é privado")
            continue
        repo = f"{m.group(1)}/{m.group(2)}"
        if repo.lower() in vistos:
            continue
        vistos.add(repo.lower())
        v = visibilidade(repo)
        if v == "PUBLIC":
            publicos.append(repo)
            achados.append(("(remoto)", 0, "repositório público",
                            f"{repo} é público e há {len(registros)} registro(s) pessoal(is) em {', '.join(pastas)}"))
        elif v is None:
            avisos.append(f"não deu para conferir se {repo} é privado (o `gh` está instalado e com `gh auth login`?)")
            nao_conferiu = True
    return achados, avisos, publicos, nao_conferiu


NAO_CONFERIU = ("[NÃO CONFERIU] Há registro pessoal (finanças, saúde, mapas ou parceiros) e não deu para saber se o repositório\n"
                "é privado. Instale o `gh` e rode `gh auth login`, e rode de novo; ou confira à mão no GitHub\n"
                "(Settings > General > Danger Zone) que o repositório é privado antes do push.")


def pare_publico(repos: list[str]) -> str:
    comandos = "\n".join(f"  gh repo edit {r} --visibility private --accept-visibility-change-consequences" for r in repos)
    return ("[PARE] Há registro pessoal (finanças, saúde, mapas ou parceiros) e o repositório no GitHub é público.\n"
            "Não faça push. Deixe o repositório privado antes:\n" + comandos + "\n"
            "ou no GitHub: Settings > General > Danger Zone > Change repository visibility > Private.\n"
            "Se um registro pessoal já foi enviado enquanto ele era público, considere que pode ter sido copiado.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--termos", default=os.environ.get("CONFERE_DADOS_TERMOS"),
                    help="arquivo, fora do repositório, com os termos próprios, um por linha")
    ap.add_argument("pastas", nargs="*", help="só estas pastas ou arquivos, relativos à raiz (padrão: o repositório inteiro e o histórico)")
    a = ap.parse_args(argv)
    if a.termos and Path(a.termos).resolve().is_relative_to(RAIZ):
        print("[ERRO] o arquivo de termos está dentro do repositório: ele mesmo levaria o dado. Mova-o para fora.")
        return 2
    termos = ler_termos(a.termos)
    achados = conferir(termos, a.pastas) + ([] if a.pastas else conferir_git(termos))
    # a privacidade vale para o repositório inteiro, também quando só algumas pastas foram conferidas
    privacidade, avisos, publicos, nao_conferiu = conferir_privacidade()
    achados += privacidade
    if publicos:
        print(pare_publico(publicos))
    for aviso in avisos:
        print(f"[AVISO] {aviso}")
    for rel, n, tipo, trecho in sorted(achados):
        print(f"{rel}:{n}: [{tipo}] {trecho}")
    print(f"-- {len(achados)} achado(s); {len(termos)} termo(s) próprio(s) conferido(s)"
          + ("" if termos else " (rode com --termos para os nomes e ids)"))
    if achados:
        return 1
    if nao_conferiu:
        print(NAO_CONFERIU)
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
