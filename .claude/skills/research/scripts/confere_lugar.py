"""Confere se o que é de terceiro está no lugar (`references/projeto.md`, "Onde fica o que é de terceiro"), sem mover nada.

  python -X utf8 .claude/skills/research/scripts/confere_lugar.py <pasta versionada da rodada> [<outra> ...]
  python -X utf8 .claude/skills/research/scripts/confere_lugar.py --repo        (da raiz do projeto)

A regra deste projeto: o que é de terceiro e não pode ir ao git (texto protegido inteiro, nota com citação longa,
mensagem ou dado pessoal de terceiro) fica numa pasta `originals/` ao lado do que o usa, fora do git pela linha
`originals/` do `.gitignore`, e nunca fora do projeto. O resto vai ao git.

Na rodada (`knowledge/research-rounds/<rodada>/`, o caminho da pasta), aponta:
  - DESVIO: `originals/` fora do `.gitignore` (iria ao git), ou arquivo de `originals/` já no git;
  - DESVIO: `originals/fontes/` com arquivos e sem `fontes/protegidas.json` (sem as linhas, nada cobra a cópia);
  - DESVIO: texto com linha em `fontes/protegidas.json` dentro da pasta versionada: em `fontes/`, ou fora dela com o
    nome do campo `arquivo` ou com o id e extensão de página baixada (.html, .htm, .pdf, .vtt, .srt);
  - DESVIO: texto com linha em `protegidas.json` sem cópia em `originals/` (o texto lido se guarda, mesmo o que
    se baixa de novo);
  - DESVIO: arquivo em `fontes/` (fora `protegidas.json`) sem linha em `licencas.json` nem em `protegidas.json` pelo
    nome (`<id>.<ext>`, o campo `arquivo`, ou o `arquivo` de `licencas.json` que é uma pasta): ou a licença não foi
    registrada, ou o nome não deixa achar o texto;
  - AVISO: nota em `notas/` com trecho entre aspas ou bloco de citação (linhas `>` seguidas, juntas) de mais de 25
    palavras (a nota com citação longa vai inteira para `originals/`; a busca não sabe de quem é o trecho).
Com --repo (rodar no checkout principal, não numa cópia de trabalho), aponta:
  - DESVIO: arquivo ignorado pelo git fora de `originals/` e dos derivados que se regeram (caches, imagens exportadas);
  - DESVIO: arquivo em `originals/` dentro de `.claude/worktrees/` (some quando a cópia de trabalho é removida);
  - AVISO: rodou numa cópia de trabalho (o `originals/` dela não é o do checkout principal);
  - AVISO: arquivo que o git ainda não vê, fora de `originals/`, com extensão de página, mídia, transcrição ou
    legenda, ou qualquer arquivo não `.md` em `knowledge/sources/` (se é de terceiro, vai para `originals/`);
  - AVISO: ficha nova de `knowledge/sources/` (que o git ainda não vê) sem a seção `## Texto integral` (é ficha de
    obra protegida: a de licença aberta leva o integral), sem arquivo de mesmo nome em `knowledge/sources/originals/`
    e sem a URL em nenhum `protegidas.json` das rodadas.
`--vault` é aceito como sinônimo de `--repo`.
Código de saída: 0 sem desvio, 1 com desvio, 2 com erro de entrada (as outras rodadas seguem sendo conferidas).
O teste sem rede, com os casos que têm de reprovar: `teste_conferidores.py`, nesta pasta.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

RODADAS = "knowledge/research-rounds"

# Lugares fora do git que a regra aceita, e os derivados que se regeram (imagens exportadas, caches). Caminho
# relativo à raiz, com barras.
PERMITIDOS = [
    r"(^|/)originals/",
    r"^marketing/social-media/(carousels|stories)/.*/images/",
    r"(^|/)__pycache__/", r"\.py[cod]$", r"(^|/)\.?venv/", r"\.egg-info/", r"(^|/)\.pytest_cache/",
    r"^\.claude/settings\.local\.json$",  # só na raiz, como a regra do `.gitignore`
    # O estado local do Claude Code (tarefas agendadas, rotinas, cópias de trabalho, checkpoints, caixa de mensagens,
    # registro dos agentes). A lista é fechada de propósito: uma linha nova no `.git/info/exclude`, que fica fora do
    # git e da revisão, não cala a conferência; o que ela tirar do git aparece como desvio até entrar aqui.
    r"(^|/)\.claude/worktrees/",
    r"(^|/)\.claude/scheduled_tasks\.(lock|json)$", r"(^|/)\.claude/routines/\.state/",
    r"(^|/)\.claude/(checkpoints|mailbox|agent-memory-local)(/|$)",
    r"(^|/)\.claude/(agent-registry\.json|first-run|assistant-daemon-state\.json)$",
    r"(^|/)\.env(\.|$)",
    r"(^|/)(Thumbs\.db|Desktop\.ini|\.DS_Store)$",
]
PAGINA = {".html", ".htm", ".pdf", ".vtt", ".srt"}
MIDIA = PAGINA | {".txt", ".mp4", ".m4a", ".mp3", ".wav", ".webm", ".mov", ".jpg", ".jpeg", ".png", ".webp",
                  ".gif", ".epub", ".docx"}


class Entrada(Exception):
    """Erro de entrada: sai com código 2, sem parar as outras rodadas."""


def git(raiz, *args):
    r = subprocess.run(["git", "-C", str(raiz), "-c", "core.quotepath=off", *args],
                       capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout


def git_lista(raiz, *args):
    """Saída de um `git ls-files -z`, um caminho por item, sem aspas nem escapes; falha do git é erro, não lista vazia."""
    cod, out = git(raiz, *args, "-z")
    if cod != 0:
        raise Entrada(f"git {' '.join(args)} falhou (código {cod})")
    return [p for p in out.split("\0") if p]


def raiz_de(p):
    cod, out = git(p, "rev-parse", "--show-toplevel")
    if cod != 0:
        raise Entrada(f"{p} não está num repositório git")
    return Path(out.strip())


def entradas_protegidas(arq):
    """As linhas de protegidas.json, nos formatos aceitos: lista de objetos com `id` (e `arquivo`); objeto com
    `arquivos` ou `textos` (lista de objetos ou de nomes); ou objeto com o id como chave."""
    d = json.loads(arq.read_text(encoding="utf-8"))
    if isinstance(d, dict):
        if "arquivos" in d or "textos" in d:
            d = list(d.get("arquivos") or []) + list(d.get("textos") or [])
        elif not d:
            d = []
        elif all(isinstance(v, dict) for v in d.values()):
            d = [{"id": k, **v} for k, v in d.items()]
        else:
            raise Entrada(f"{arq}: formato de protegidas.json desconhecido")
    saida = []
    for e in d:
        if isinstance(e, str):
            saida.append({"id": Path(e).name.split(".", 1)[0], "arquivo": e})
        elif isinstance(e, dict) and (e.get("id") or e.get("arquivo")):
            i, a = e.get("id"), e.get("arquivo")
            if (i is not None and not isinstance(i, str)) or (a is not None and not isinstance(a, str)):
                raise Entrada(f"{arq}: linha com id ou arquivo que não é texto: {e!r:.80}")
            saida.append(e)
    return saida


EXT = re.compile(r"(\.(?:[a-z]{2}(?:-[a-z]{2})?|html?|pdf|txt|mdx?|vtt|srt|json|xml|csv|epub|docx|py|raw|png|jpe?g|webp|gif|mp4|m4a|mp3|webm))+", re.I)


def de_id(p, i):
    """O arquivo é o texto do id `i`: `<id>` seguido só de extensões conhecidas (`.html`, `.en.vtt`, `.pdf.txt`); o id
    pode ter ponto, e `artigo` não casa com `artigo.v2.html`."""
    n = p.name if isinstance(p, Path) else p
    if n == i:
        return True
    return n.startswith(i + ".") and bool(EXT.fullmatch(n[len(i):]))


def arquivos(pasta, fora=()):
    if not pasta.is_dir():
        return []
    return [p for p in pasta.rglob("*") if p.is_file() and not any(x in p.relative_to(pasta).parts[:1] for x in fora)]


def acha(lista, e, so_pagina=False):
    """Os arquivos da lista que são o texto da linha `e`: pelo nome em `arquivo`, ou pelo id; com `so_pagina`, o
    casamento pelo id vale só para extensão de página baixada (uma nota nossa pode ter o nome do id)."""
    nome = Path(e["arquivo"]).name if e.get("arquivo") else None
    achados = []
    for p in lista:
        if nome and p.name == nome:
            achados.append(p)
        elif e.get("id") and de_id(p, e["id"]) and (not so_pagina or p.suffix.lower() in PAGINA):
            achados.append(p)
    return achados


def citacoes_longas(texto):
    trechos = re.findall(r"“([^”\n]+)”", texto) + re.findall(r'"([^"\n]+)"', texto)
    bloco = []
    for l in texto.splitlines() + [""]:
        s = l.lstrip()
        if s.startswith(">"):
            bloco.append(s.lstrip("> "))
        elif bloco:
            trechos.append(" ".join(bloco))
            bloco = []
    return [t for t in trechos if len(t.split()) > 25]


def confere_rodada(pasta):
    pasta = Path(pasta).resolve()
    raiz = raiz_de(pasta)
    try:
        rel = pasta.relative_to(raiz.resolve()).as_posix()
    except ValueError:
        raise Entrada(f"{pasta} fora da raiz {raiz}")
    if not rel.startswith(RODADAS + "/"):
        raise Entrada(f"{rel} não é uma pasta de {RODADAS}/")
    desvios, avisos = [], []
    cod, _ = git(raiz, "check-ignore", "-q", f"{rel}/originals/teste.txt")
    if cod != 0:
        desvios.append("o .gitignore não deixa `originals/` fora do git (falta a linha originals/)")
    no_git = [l for l in git_lista(raiz, "ls-files", f"{rel}/originals") if not l.endswith("/README.md")]
    if no_git:
        desvios.append(f"{len(no_git)} arquivo(s) de originals/ no git, ex.: {no_git[0]}")
    fontes, originais = pasta / "fontes", pasta / "originals"
    em_originais = arquivos(originais)
    em_fontes = [p for p in arquivos(fontes) if p.name != "protegidas.json"]
    resto = arquivos(pasta, fora=("originals", "fontes"))
    prot = fontes / "protegidas.json"
    ids_prot = set()
    if prot.exists():
        for e in entradas_protegidas(prot):
            ids_prot.add(e.get("id") or Path(e["arquivo"]).name)
            dentro = acha(em_fontes, e) + acha(resto, e, so_pagina=True)
            for p in dentro:
                desvios.append(f"texto protegido na pasta versionada: {p.relative_to(pasta).as_posix()}")
            if not acha(em_originais, e):
                desvios.append(f"texto lido sem cópia em originals/: {e.get('id') or e.get('arquivo')}")
    elif arquivos(originais / "fontes"):
        desvios.append(f"originals/fontes/ com {len(arquivos(originais / 'fontes'))} arquivo(s) e sem fontes/protegidas.json")
    lic = pasta / "licencas.json"
    ids_lic, pastas_lic = set(), set()
    if lic.exists():
        d = json.loads(lic.read_text(encoding="utf-8"))
        if isinstance(d, dict):  # o id como chave
            ids_lic |= set(d)
        for e in (d.values() if isinstance(d, dict) else d):
            if isinstance(e, dict):
                ids_lic.add(e.get("id"))
                a = e.get("arquivo")
                if isinstance(a, str) and a:
                    a = a.replace("\\", "/").strip("/")
                    a = a[len("fontes/"):] if a.startswith("fontes/") else a
                    ids_lic.add(Path(a).name)
                    pastas_lic.add(a)
            elif isinstance(e, str):
                ids_lic.add(Path(e).name)
    conhecidos = {i for i in ids_lic | ids_prot if i}
    for p in em_fontes:
        partes = p.relative_to(fontes).parts
        prefixos = {"/".join(partes[:k]) for k in range(1, len(partes))}
        if p.name in conhecidos or any(de_id(p, i) for i in conhecidos) or prefixos & pastas_lic:
            continue
        desvios.append(f"texto em fontes/ sem linha em licencas.json pelo nome: {p.relative_to(pasta).as_posix()}"
                       " (nome `<id>.<ext>` ou campo `arquivo` na linha; se é protegido, vai para originals/)")
    for p in arquivos(pasta / "notas"):
        if p.suffix in {".md", ".txt"}:
            longas = citacoes_longas(p.read_text(encoding="utf-8", errors="replace"))
            if longas:
                avisos.append(f"possível citação longa em {p.relative_to(pasta).as_posix()}: "
                              f"\"{longas[0][:70]}...\" ({len(longas[0].split())} palavras)")
    return desvios, avisos


def confere_repo():
    raiz = raiz_de(Path.cwd())
    desvios, avisos = [], []
    _, comum = git(raiz, "rev-parse", "--git-common-dir")
    _, proprio = git(raiz, "rev-parse", "--git-dir")
    if Path(raiz, comum.strip()).resolve() != Path(raiz, proprio.strip()).resolve():
        avisos.append("rodou numa cópia de trabalho: o originals/ dela some com a cópia; leve-o ao mesmo caminho no "
                      "checkout principal e rode o --repo lá")
    wt = raiz / ".claude" / "worktrees"
    if wt.is_dir():
        for o in wt.glob("*/**/originals"):
            n = [x for x in o.rglob("*") if x.is_file() and x.name != "README.md"]
            if n:
                desvios.append(f"originals/ dentro de uma cópia de trabalho do Claude Code, com {len(n)} arquivo(s): "
                               f"{o.relative_to(raiz).as_posix()}")
    for l in git_lista(raiz, "ls-files", "--others", "--ignored", "--exclude-standard"):
        if not any(re.search(p, l) for p in PERMITIDOS):
            desvios.append(f"fora do git e fora de originals/: {l}")
    novos = git_lista(raiz, "ls-files", "--others", "--exclude-standard")
    for l in novos:
        if "/originals/" in f"/{l}":
            continue
        suf = Path(l).suffix.lower()
        if suf in MIDIA or (l.startswith("knowledge/sources/") and suf != ".md"):
            avisos.append(f"página, mídia ou transcrição fora do git e fora de originals/: {l}")
    urls = set()
    for prot in (raiz / RODADAS).glob("*/fontes/protegidas.json"):
        try:
            urls |= {(e.get("url") or "").rstrip("/") for e in entradas_protegidas(prot)}
        except (Entrada, json.JSONDecodeError):
            pass
    urls.discard("")
    orig_fichas = [p for p in arquivos(raiz / "knowledge/sources/originals") if p.name != "README.md"]
    fichas_novas = {l for l in novos if re.fullmatch(r"knowledge/sources/[^/]+\.md", l)} - {"knowledge/sources/README.md"}
    for l in sorted(fichas_novas):
        f = raiz / l
        url = (frontmatter(f).get("url") or "").rstrip("/")
        integral = re.search(r"^## Texto integral", f.read_text(encoding="utf-8", errors="replace"), re.M)
        if not integral and not any(de_id(o, f.stem) for o in orig_fichas) and not (url and url in urls):
            avisos.append(f"ficha de obra protegida sem original guardado: {f.name} (knowledge/sources/originals/"
                          f"{f.stem}.<ext>, ou o texto no originals/ da rodada)")
    return desvios, avisos


def frontmatter(p):
    t = p.read_text(encoding="utf-8", errors="replace")
    if not t.startswith("---"):
        return {}
    fim = t.find("\n---", 3)
    if fim < 0:
        return {}
    campos, ultimo = {}, None
    for l in t[3:fim].splitlines():
        m = re.match(r"([a-z_]+):\s*(.*)", l)
        if m:
            ultimo = m.group(1)
            campos[ultimo] = m.group(2).strip().strip("\"'")
        elif ultimo and l.startswith((" ", "\t", "-")) and l.strip() and not campos[ultimo]:
            campos[ultimo] = "(bloco)"
    return campos


def principal():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    alvos = [("repositório", None)] if args in (["--repo"], ["--vault"]) else [(Path(a).name or a, a) for a in args]
    total, erro = 0, False
    for nome, caminho in alvos:
        try:
            if caminho is None:
                desvios, avisos = confere_repo()
            elif not Path(caminho).is_dir():
                raise Entrada(f"pasta não encontrada: {caminho}")
            else:
                desvios, avisos = confere_rodada(caminho)
        except (Entrada, json.JSONDecodeError, UnicodeDecodeError, TypeError, AttributeError, KeyError) as e:
            print(f"== {nome}: erro de entrada: {e}")
            erro = True
            continue
        print(f"== {nome}: {len(desvios)} desvio(s), {len(avisos)} aviso(s)")
        for d in desvios:
            print("  DESVIO", d)
        for a in avisos:
            print("  aviso ", a)
        total += len(desvios)
    return 2 if erro else (1 if total else 0)


if __name__ == "__main__":
    sys.exit(principal())
