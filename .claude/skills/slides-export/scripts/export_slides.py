#!/usr/bin/env python3
"""Exporta os slides de um carrossel (slides.html) como imagens, via shot-scraper.

Substitui o exportar-slides.yaml copiado por post: le o slides.html, conta as
<section class="slide"> de verdade, gera a config do shot-scraper no diretorio
temporario e roda. Saida em JPEG por padrao (exigencia da API do Instagram).

Uso:
  python export_slides.py <pasta-do-post>                 # todos os slides -> images/slide-NN.jpg
  python export_slides.py <pasta> --only 3,5              # regera so os slides 3 e 5
  python export_slides.py <pasta> --format png            # PNG para revisao visual
  python export_slides.py <pasta> --out-dir <dir>         # saida em outro lugar (teste)
  python export_slides.py <pasta> --upload <bucket> <prefixo>   # sobe a saida via r2-storage
  python export_slides.py <pasta> --sem-conferir          # pula as conferencias de conferir_telas.py
  python export_slides.py <pasta> --upload <bucket> <prefixo> --motivo "<o que mudou>"   # peca ja publicada
  python export_slides.py <pasta> --sem-video --out-dir <dir>   # a tela com data-video em imagem (o quadro final), so revisao

Tela em video: a <section class="slide"> com data-video="<segundos>" sai em images/slide-NN.mp4, gravada pelo
tela_em_video.py ao lado, com a animacao guiada por window.quadro(t, idx) da pagina; as outras seguem em JPEG. So no
carrossel. O MP4 e conferido contra os limites da API (codec, quadros, duracao, moov no comeco, sem lista de edicao;
pede o ffprobe) e, fora deles, barra o --upload. --som-mudo poe uma faixa AAC muda; --sem-video nao vale com --upload,
nao apaga nada e nao grava na legenda.md.

Depois de publicada (o criterio esta em references/projeto.md da skill: o carrossel inteiro com **Publicado:** na
legenda.md; nos Stories publicados por API, tela a tela, os que tem linha na tabela "Publicada pela API" do roteiro.md;
nos Stories pelo app, a sequencia inteira pelo estagio ou pelo bucket), nada se sobrescreve no bucket e o registro so
cresce: a tela publicada sobe para <prefixo>/versoes/versao-N/ (N = o proximo; a versao 1 e a publicada, que fica onde
esta), com --motivo, sem reescrever **Imagens:** nem ## Slides, e com uma linha na secao "## Versões depois de
publicada" da legenda.md (carrossel) ou do roteiro.md (Stories).

Credenciais: so o --upload pede as do R2 (pela skill r2-storage: R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY,
R2_BUCKET_<APELIDO> e R2_PUBLIC_BASE_<APELIDO>). Sem elas, o --upload para antes de exportar, com a mensagem do que
falta e de como configurar; a exportacao local segue sem chave e avisa, uma vez, que a protecao do publicado pelo
bucket ficou desligada.

Antes da foto, roda as conferencias da forma (o conferir_telas.py da skill visual-form) na peca inteira, mesmo com
--only, porque ela vai ao ar inteira: ERRO, ou conferencia que nao rodou, nao impede exportar para revisao, mas impede
o --upload. O travessao so barra quando a voz de quem usa (context/sobre-mim.md) pede texto sem travessao.
"""
from __future__ import annotations

import argparse
import datetime
import functools
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path



def raiz_do_projeto() -> Path:
    """A raiz do projeto: a que contem esta skill (.claude/skills/slides-export/scripts/), ou, instalada como plugin,
    a pasta do projeto aberto (CLAUDE_PROJECT_DIR) ou a pasta de trabalho."""
    aqui = Path(__file__).resolve()
    if len(aqui.parents) > 4 and aqui.parents[2].name == "skills" and aqui.parents[3].name == ".claude":
        return aqui.parents[4]
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd()).resolve()


ROOT = raiz_do_projeto()
R2 = ROOT / ".claude/skills/r2-storage/scripts/r2.py"
SLIDE_RE = re.compile(r"<section\b[^>]*\bclass\s*=\s*[\"'][^\"']*\bslide\b[^\"']*[\"']", re.I)
SECTION_RE = re.compile(r"<section\b[^>]*>", re.I)
# data-video com aspas duplas, simples ou sem aspas, como o DOM le (a conferencia le pelo dataset.video)
VIDEO_RE = re.compile(r"\bdata-video\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s\"'>]+))", re.I)
EXT_ITEM = (".jpg", ".jpeg", ".png", ".mp4")  # o que conta como tela exportada, na pasta e no bucket


def telas_em_video(texto_html: str) -> dict[int, float]:
    """{tela (a partir de 1): segundos} das <section class="slide"> com data-video, na ordem das telas."""
    out, n = {}, 0
    for tag in SECTION_RE.findall(texto_html):
        if not SLIDE_RE.match(tag):
            continue
        n += 1
        m = VIDEO_RE.search(tag)
        if m:
            valor = next(g for g in m.groups() if g is not None)
            try:
                out[n] = float(valor.replace(",", "."))
            except ValueError:
                die(f"tela {n}: data-video=\"{valor}\" nao e um numero de segundos")
    return out


@functools.lru_cache(maxsize=None)
def carregar_tv():
    """O tela_em_video.py ao lado (gravacao e conferencia do MP4), carregado uma vez."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("tela_em_video", Path(__file__).with_name("tela_em_video.py"))
    tv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tv)
    return tv

# Limites da API de publicacao do Instagram (confira na documentacao da Meta antes de mudar):
# so JPEG, 8 MB, largura 320..1440 px, proporcao entre 4:5 (0.8) e 1.91:1.
IG_MAX_BYTES = 8 * 1024 * 1024
IG_MIN_W, IG_MAX_W = 320, 1440
IG_MIN_RATIO, IG_MAX_RATIO = 0.8, 1.91

# Antialiasing em tons de cinza: sem a flag, o Chromium desta maquina (Windows) desenha o texto com subpixel, e a
# borda das letras sai com franja azul e laranja. Num carrossel medido, a moldura tinha 43% dos pixels de tinta fora
# do cinza sem a flag e 4% com ela, com a mesma escuridao total.
# O -webkit-font-smoothing nao serve: so age no macOS.
BROWSER_ARGS = ["--browser-arg", "--disable-lcd-text"]

# window.prepararSlide, se a peca definir, ajusta a tela antes da foto (ex.: assentar o texto
# nas linhas do papel de uma serie); o page.evaluate espera a promessa.
# As fontes da tela se pedem antes e depois do prepararSlide (fontes.py): sem o script da serie (os Stories), nada
# pedia a fonte antes da foto. Quem acusa a que nao carregou e a conferencia (ERRO fonte_nao_carregada, que barra o
# --upload); aqui so se pede, para a foto sair na fonte da peca. As chaves do JS do fontes.py vao dobradas para o format.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fontes import CARREGAR_FONTES  # noqa: E402
import ambiente  # noqa: E402  (copia identica de scripts/ambiente.py da raiz: as chaves do ambiente ou do .env)

JS = """
(async () => {{
const carregarFontes = """ + CARREGAR_FONTES.replace("{", "{{").replace("}", "}}") + """;
document.querySelectorAll('.slide').forEach((s,i) => s.classList.toggle('active', i==={idx}));
const st = document.getElementById('stage'); if (st) st.style.transform = 'none';
for (const id of ['prev','next']) {{ const el = document.getElementById(id); if (el) el.style.display = 'none'; }}
document.querySelectorAll('.pager').forEach(p => p.style.display = 'none');
const tela = document.querySelectorAll('.slide')[{idx}];
await carregarFontes(tela);
if (window.prepararSlide) await window.prepararSlide({idx});
await carregarFontes(tela);
{previa}}})()
"""


def die(msg: str) -> None:
    print(f"[ERRO] {msg}", file=sys.stderr)
    sys.exit(2)


def validate(f: Path) -> list[str]:
    """Confere o arquivo contra os limites do Instagram; devolve avisos (vazio = ok)."""
    problems: list[str] = []
    size = f.stat().st_size
    if size > IG_MAX_BYTES:
        problems.append(f"{size / 1024 / 1024:.1f} MB, acima de 8 MB")
    try:
        from PIL import Image
    except ImportError:
        return problems + ["Pillow ausente: dimensoes e formato nao conferidos"]
    with Image.open(f) as im:
        w, h = im.size
        fmt = im.format
    if f.suffix.lower() == ".jpg" and fmt != "JPEG":
        problems.append(f"formato {fmt}, esperado JPEG")
    if fmt != "JPEG":
        problems.append("nao e JPEG: o Instagram nao aceita para publicar (use --format jpg)")
    if not (IG_MIN_W <= w <= IG_MAX_W):
        problems.append(f"largura {w}px fora de {IG_MIN_W}..{IG_MAX_W} (a API reescala)")
    ratio = w / h
    if not (IG_MIN_RATIO - 0.005 <= ratio <= IG_MAX_RATIO + 0.005):
        problems.append(f"proporcao {ratio:.3f} fora de 4:5..1.91:1")
    return problems


@functools.lru_cache(maxsize=None)
def load_r2():
    """O r2.py da skill r2-storage (o bucket e a URL publica), carregado uma vez; sem a skill, para com a mensagem."""
    import importlib.util
    if not R2.is_file():
        die(f"o --upload pede a skill r2-storage, que nao esta em {R2.parent.parent.as_posix()}: instale-a no projeto "
            "(ela sobe os arquivos e monta a URL publica)")
    spec = importlib.util.spec_from_file_location("r2", R2)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def qtos_videos(names: list[str]) -> str:
    """', 1 delas em vídeo (MP4)' quando ha tela em video; vazio quando nao ha."""
    n = sum(Path(x).suffix.lower() == ".mp4" for x in names)
    return f", {n} delas em vídeo (MP4)" if n else ""


def mesma_tela_outro_formato(names: list[str]) -> list[str]:
    """Os arquivos cujo numero de tela se repete com outra extensao (slide-02.jpg e slide-02.mp4)."""
    por_n: dict[str, list[str]] = {}
    for x in names:
        m = re.match(r"slide-(\d+)\.", Path(x).name)
        if m:
            por_n.setdefault(m.group(1), []).append(x)
    return sorted(x for v in por_n.values() if len(v) > 1 for x in v)


def sem_repetidas(nomes: list[str], atuais: set[str] | None) -> list[str]:
    """Tira da lista o arquivo de uma tela repetida (slide-02.jpg e slide-02.mp4, ou .jpg e .png) que nao e o desta
    exportacao. Tela repetida sem nenhum arquivo desta exportacao (com --only, uma tela que nao foi regerada) fica
    inteira: nao ha como saber qual vale. `nomes` sao chaves ou nomes; `atuais`, os nomes desta exportacao."""
    if atuais is None:
        return nomes
    repetidas = set(mesma_tela_outro_formato(nomes))
    numero = lambda k: Path(k).name.split(".")[0]
    com_atual = {numero(k) for k in repetidas if Path(k).name in atuais}
    return [k for k in nomes if not (k in repetidas and numero(k) in com_atual and Path(k).name not in atuais)]


def record_in_legenda(post: Path, out_dir: Path, bucket: str | None, prefix: str | None,
                      subidos: set[str] | None = None) -> None:
    """Escreve na legenda.md da peca o rotulo **Imagens:** e a secao ## Slides com embeds.

    Enviadas ao bucket -> embeds pela URL publica. So locais -> embeds pelo caminho relativo. `subidos`: os nomes desta
    exportacao; o arquivo de outro formato com o mesmo numero que ficou no prefixo ou na pasta (a tela que virou video,
    ou deixou de ser; o PNG de revisao ao lado do JPEG) nao entra no registro.
    """
    leg = post / "legenda.md"
    if not leg.is_file():
        print(f"[--] {post.name}/legenda.md nao existe; nada registrado na peca")
        return
    today = datetime.date.today().isoformat()
    if bucket and prefix:
        r2 = load_r2()
        b = r2.bucket(bucket)
        s3 = r2.client()
        keys = []
        for page in s3.get_paginator("list_objects_v2").paginate(Bucket=b, Prefix=prefix + "/"):
            keys += [o["Key"] for o in page.get("Contents", [])]
        keys = sem_repetidas(sorted(k for k in keys if "/" not in k[len(prefix) + 1:]), subidos)
        urls = [r2.public_url(b, k) for k in keys]
        if not all(urls):
            # o r2.public_url ja avisou no stderr qual variavel falta e onde se pega
            print(f"[AVISO] bucket `{r2.alias_of(b)}` sem URL publica (falta R2_PUBLIC_BASE_{r2.alias_of(b).upper()}): "
                  "os embeds da legenda.md nao foram escritos; configure e exporte de novo com --upload")
            return
        names = [Path(k).name for k in keys]
        label = (f"**Imagens:** {len(urls)} no bucket `{r2.alias_of(b)}`, prefixo `{prefix}/`{qtos_videos(names)}, "
                 f"enviadas em {today}. Embeds na seção Slides; a cópia em `images/` é de trabalho e fica fora do git.")
    else:
        files = sorted(p for p in out_dir.glob("slide-*.*") if p.suffix.lower() in EXT_ITEM)
        # um slide-03.png de revisao ao lado do slide-03.jpg novo fica na pasta, mas nao no registro
        files = [out_dir / n for n in sem_repetidas([p.name for p in files], subidos)]
        if not files:
            return
        rel = out_dir.relative_to(post).as_posix()
        urls = [f"{rel}/{p.name}" for p in files]
        names = [p.name for p in files]
        nv = sum(p.suffix.lower() == ".mp4" for p in files)
        fmt = next((p.suffix.lstrip(".").upper() for p in files if p.suffix.lower() != ".mp4"), "")
        fmt = f"telas ({len(files) - nv} {fmt} e {nv} em vídeo, MP4)" if nv else fmt
        label = (f"**Imagens:** {len(files)} {fmt} em `{rel}/`, exportadas em {today}, fora do git e "
                 f"ainda não enviadas ao bucket. Embeds na seção Slides.")

    bruto = leg.read_bytes().decode("utf-8")  # em binario: o modo texto trocaria o CRLF por LF antes da deteccao
    nl = "\r\n" if "\r\n" in bruto else "\n"  # preserva o fim de linha do arquivo
    s = bruto.replace("\r\n", "\n")
    if re.search(r"^\*\*Imagens:\*\*.*$", s, re.M):
        s = re.sub(r"^\*\*Imagens:\*\*.*$", lambda m: label, s, count=1, flags=re.M)
    elif re.search(r"^\*\*Prefixo no bucket:\*\*.*$", s, re.M):
        s = re.sub(r"^(\*\*Prefixo no bucket:\*\*.*\n)", lambda m: m.group(1) + label + "\n", s, count=1, flags=re.M)
    else:
        s = re.sub(r"^(# .*\n)", lambda m: m.group(1) + "\n" + label + "\n", s, count=1, flags=re.M)
    if bucket and prefix and not re.search(r"^\*\*Prefixo no bucket:\*\*", s, re.M):
        s = re.sub(r"^(\*\*Imagens:\*\*.*\n)", lambda m: f"**Prefixo no bucket:** `{prefix}/`\n" + m.group(1), s, count=1, flags=re.M)
    s = re.sub(r"^\*\*Slides locais:\*\*.*\n", "", s, flags=re.M)

    section = "## Slides\n\n<!-- gerado pela skill slides-export; não editar à mão -->\n"
    section += "\n".join(f"![{n}]({u})" for n, u in zip(names, urls)) + "\n"
    if re.search(r"^## Slides\s*$", s, re.M):
        s = re.sub(r"^## Slides\s*\n.*?(?=^## |\Z)", section, s, count=1, flags=re.S | re.M)
    else:
        s = s.rstrip("\n") + "\n\n---\n\n" + section
    leg.write_text(s.replace("\n", nl), encoding="utf-8", newline="")
    nome = leg.relative_to(ROOT).as_posix() if leg.is_relative_to(ROOT) else str(leg)  # copia fora do projeto (teste)
    print(f"[OK] {nome}: rótulo **Imagens:** e seção Slides com {len(urls)} embed(s)")


def conferir(post: Path, html: str, janela: tuple[int, int], publicada: bool | frozenset = False) -> list[str]:
    """Roda as conferencias de conferir_telas.py e imprime os achados; devolve os tipos de ERRO achados.

    Se a conferencia falhar (dependencia ausente, erro no navegador), a exportacao para revisao segue com um aviso,
    e o tipo "nao_rodou" impede o --upload: peca sem conferencia nao sobe. `publicada` vem de quem chama (True para a
    peca inteira, ou o conjunto das telas publicadas, nos Stories pela API): na tela publicada, hashtags, regras da
    casa e as de area segura, zona proibida e travessao, que ja foram ao ar, viram AVISO.
    """
    try:
        ct = carregar_ct()
        leg = post / "legenda.md"
        md = leg.read_text(encoding="utf-8") if leg.is_file() else ""
        legenda = ct.texto_da_legenda(md) if md else None
        achados = ct.conferir(post, html, legenda, janela, publicada=publicada or ct.publicada(md), exportacao=True)
    except Exception as e:  # noqa: BLE001 - qualquer falha da conferencia vira aviso, nao derruba a exportacao
        print(f"[AVISO] conferencias nao rodaram ({type(e).__name__}: {e}); o --upload fica bloqueado")
        return ["nao_rodou"]
    linhas, resumo = ct.relatorio(achados)
    print("\n".join(linhas + [f"[..] conferencias: {resumo}"]))
    return sorted({x["conferencia"] for x in achados if x["nivel"] == "ERRO"})


# ---------- peca ja publicada: versoes, sem sobrescrever (o registro do que foi ao ar so cresce) ----------
SECAO_VERSOES = "## Versões depois de publicada"


def registro_da_peca(post: Path) -> Path | None:
    """O arquivo que registra a peca: legenda.md no carrossel, roteiro.md nos Stories."""
    for nome in ("legenda.md", "roteiro.md"):
        if (post / nome).is_file():
            return post / nome
    return None


@functools.lru_cache(maxsize=None)
def carregar_ct():
    """O conferir_telas.py ao lado (carrega sem numpy nem Pillow; eles so entram ao conferir), uma vez so: o
    ids_no_bucket chama a cada objeto do bucket, e cada carga reexecutava o modulo e crescia o sys.path."""
    import importlib.util
    arq = ROOT / ".claude/skills/visual-form/scripts/conferir_telas.py"
    if not arq.is_file():
        raise FileNotFoundError(f"as conferencias da forma moram na skill visual-form, que nao esta em {arq.as_posix()}")
    spec = importlib.util.spec_from_file_location("conferir_telas", arq)
    ct = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ct)
    return ct


def frontmatter(s: str) -> dict:
    fm = re.match(r"---\n(.*?)\n---", s, re.S)
    return dict(re.findall(r"^(\w+):\s*(.*?)\s*$", fm.group(1), re.M)) if fm else {}


def ja_publicada(reg: Path | None) -> bool | frozenset:
    """O que o registro diz que ja foi ao ar (o criterio em references/projeto.md). Carrossel: True com **Publicado:**
    preenchido (o publicada() do conferir_telas.py, o mesmo criterio de quem publica). Stories: o conjunto dos Stories
    com linha na tabela "Publicada pela API" do roteiro.md, quando ela existe; senao, True com estagio publicado ou
    medido. False no resto. Sem a visual-form, a mesma leitura por aqui, sem a tabela da API, com aviso."""
    if reg is None:
        return False
    s = reg.read_text(encoding="utf-8").replace("\r\n", "\n")
    try:
        ct = carregar_ct()
    except FileNotFoundError as e:
        print(f"[AVISO] {e}; o publicado se le so pelo **Publicado:** da legenda.md ou pelo estagio do roteiro.md")
        if reg.name == "legenda.md":
            m = re.search(r"^\*\*Publicado:\*\*[ \t]*(.*)$", s, re.M)  # [ \t]*: o \s* engoliria a quebra de linha
            return bool(m and m.group(1).strip())
        est = re.search(r"""^estagio:[ \t]*["']?([A-Za-z-]+)""", s, re.M)
        return bool(est and est.group(1).lower() in ("publicado", "medido"))
    if reg.name == "legenda.md":
        return ct.publicada(s)
    return ct.publicada_do_roteiro(s)


JANELA_STORIES = datetime.time(5, 0)  # a janela de postagem dos Stories comeca as 5h de Brasilia


def inicio_da_janela(dia: datetime.date) -> datetime.datetime:
    """05:00 de Brasilia do dia, com fuso (o horario de verao nao existe desde 2019; o fixo -3 e a reserva)."""
    try:
        from zoneinfo import ZoneInfo
        fuso = ZoneInfo("America/Sao_Paulo")
    except Exception:  # noqa: BLE001 - sem a base de fusos no sistema
        fuso = datetime.timezone(datetime.timedelta(hours=-3))
    return datetime.datetime.combine(dia, JANELA_STORIES, tzinfo=fuso)


def ids_no_bucket(dia: datetime.date, apelido: str) -> set[str] | None:
    """Stories: os ids dos Stories do dia que uma coleta de metricas guardou em stories/publicado/<dia>/ no bucket de
    apelido `apelido` (<id>.jpg, <id>.mp4 ou <id>-miniatura.jpg; o id sai sem o sufixo, id_do_objeto do
    conferir_telas.py), so os objetos gravados a partir das 5h de Brasilia daquele dia. O objeto so e gravado depois da
    postagem, entao um LastModified antes das 5h prova que o Story saiu antes da janela: um avulso de madrugada, que nao
    marca a sequencia. Assim a protecao nao depende de `git pull` do roteiro, que a coleta marca no remoto. Devolve None
    quando o bucket nao responde (sem rede, ou sem as chaves, com a mensagem do que falta); conjunto vazio quando nada
    do dia foi ao ar."""
    r2 = load_r2()
    falta = r2.faltas(apelido)
    if falta:
        print("[AVISO] a protecao do publicado pelo bucket nao rodou: falta " + "; ".join(falta) + " " + r2.COMO_POR)
        return None
    try:
        s3 = r2.client()
        prefixo = f"stories/publicado/{dia.isoformat()}/"
        desde = inicio_da_janela(dia)
        ids = set()
        for page in s3.get_paginator("list_objects_v2").paginate(Bucket=r2.bucket(apelido), Prefix=prefixo):
            ids |= {carregar_ct().id_do_objeto(o["Key"]) for o in page.get("Contents", []) if o["LastModified"] >= desde}
        return ids
    except (Exception, SystemExit):  # o r2.py sai com SystemExit quando falta algo; aqui vira "nao respondeu"
        return None


def decidir_stories(publicada, tabela: dict | None, ids: set[str] | None) -> tuple[bool | frozenset, str]:
    """O que conta como publicado numa sequencia de Stories na hora do --upload (o criterio em references/projeto.md),
    e a mensagem. `publicada` vem do roteiro (ja_publicada), `tabela` e a da API ({Story: id}, ou None),
    `ids` os do bucket (None sem resposta).
    - Com a tabela: vale a tabela, tela a tela, e nao o estagio. Id no bucket que nao esta na tabela (um Story
      publicado sem gravar a linha, ou a sequencia que mistura a API e o app) leva ao criterio do app: a sequencia inteira.
    - Sem a tabela: o estagio, e o bucket quando o roteiro local esta atrasado (a coleta marca no remoto)."""
    if tabela is not None:
        if ids is None:
            return publicada, ("[AVISO] o bucket nao respondeu (sem rede, ou sem a configuracao acima): vale so a tabela da API do "
                               "roteiro.md, tela a tela; um Story no ar fora dela nao aparece")
        fora = sorted(ids - set(tabela.values()))
        if fora:
            return True, (f"[--] o bucket tem Story do dia fora da tabela da API ({', '.join(fora)}): vale o criterio do "
                          "app, a sequencia inteira conta como publicada")
        return publicada, f"[--] Stories pela API: publicados (tela a tela, pela tabela do roteiro.md) {sorted(publicada)}"
    if publicada:
        return publicada, ""
    if ids is None:
        return False, ("[AVISO] o bucket nao respondeu (sem rede, ou sem a configuracao acima): a decisao de publicada segue so "
                       "pelo roteiro.md, que pode estar atrasado; se a sequencia ja foi ao ar, fazer `git pull` antes")
    if ids:
        return True, ("[--] o bucket tem Stories publicados do dia, a partir das 5h (stories/publicado/<dia>/): a sequencia "
                      "conta como publicada, embora o roteiro.md diga outro estagio (se a coleta marca o roteiro no "
                      "remoto, um `git pull` traz a marcacao)")
    return False, ""


def prefixo_registrado(reg: Path) -> str | None:
    """O **Prefixo no bucket:** da legenda.md (onde a versao 1 esta), sem crases nem barra no fim."""
    m = re.search(r"^\*\*Prefixo no bucket:\*\*[ \t]*(.*)$", reg.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip().strip("`").strip().strip("/") if m and m.group(1).strip() else None


def versoes_registradas(reg: Path) -> list[int]:
    s = reg.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.search("^" + re.escape(SECAO_VERSOES) + r"\s*$(.*?)(?=^## |\Z)", s, re.S | re.M)
    return [int(x) for x in re.findall(r"^\|\s*(\d+)\s*\|", m.group(1), re.M)] if m else []


def versoes_no_bucket(bucket: str, prefix: str) -> list[int]:
    r2 = load_r2()
    s3 = r2.client()
    achadas = set()
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=r2.bucket(bucket), Prefix=prefix + "/versoes/"):
        for o in page.get("Contents", []):
            m = re.match(re.escape(prefix) + r"/versoes/versao-(\d+)/", o["Key"])
            if m:
                achadas.add(int(m.group(1)))
    return sorted(achadas)


def registrar_versao(reg: Path, n: int, motivo: str, links: list[str], incompleta: str = "") -> None:
    """Acrescenta a linha da versao na secao "## Versões depois de publicada" (criada no fim do arquivo na 1a vez)."""
    bruto = reg.read_bytes().decode("utf-8")  # em binario: o modo texto trocaria o CRLF por LF antes da deteccao
    nl = "\r\n" if "\r\n" in bruto else "\n"
    s = bruto.replace("\r\n", "\n")
    hoje = datetime.date.today().isoformat()
    motivo = re.sub(r"\s+", " ", motivo).strip().replace("|", "\\|")  # quebra de linha e barra vertical partiriam a tabela
    if incompleta:
        motivo += f" (incompleta: {incompleta})"
    linha = f"| {n} | {hoje} | {motivo} | {' '.join(links)} |"
    m = re.search("^" + re.escape(SECAO_VERSOES) + r"\s*$(.*?)(?=^## |\Z)", s, re.S | re.M)
    if not m:
        s = (s.rstrip("\n") + "\n\n" + SECAO_VERSOES + "\n\n"
             "A versão 1 é a que foi ao ar, no prefixo da peça, e não se sobrescreve. Cada versão seguinte fica em "
             "`<prefixo>/versoes/versao-N/` e leva só as telas regeradas; as outras seguem da versão anterior. "
             "Tabela gerada pela skill `slides-export`.\n\n"
             "| Versão | Data | Motivo | Imagens |\n|---|---|---|---|\n" + linha + "\n")
    else:
        corpo = m.group(1)
        linhas = corpo.split("\n")
        ult = max((i for i, l in enumerate(linhas) if l.startswith("|")), default=None)
        if ult is None:
            linhas.insert(1, "| Versão | Data | Motivo | Imagens |\n|---|---|---|---|\n" + linha)
        else:
            linhas.insert(ult + 1, linha)
        s = s[:m.start(1)] + "\n".join(linhas) + s[m.end(1):]
    reg.write_text(s.replace("\n", nl), encoding="utf-8", newline="")
    print(f"[OK] {reg.name}: versão {n} registrada em '{SECAO_VERSOES}'")


def voz_pede_sem_travessao() -> bool | None:
    """A voz de quem usa (context/sobre-mim.md) pede texto sem travessao? None quando o arquivo nao existe; False quando
    ele nao diz isso (o roteiro em branco so traz o travessao como exemplo de pergunta, "se o travessao e proibido"): a
    conferencia nao inventa regra que a voz nao tem."""
    arq = ROOT / "context" / "sobre-mim.md"
    if not arq.is_file():
        return None
    s = arq.read_text(encoding="utf-8")
    pede = (r"(sem|nada de|evit\w*|(nunca|n[aã]o)( use| usa| usar| uso)?)\s+(o |os |de )?travess"
            r"|(?<!se o )travess\w*\s+(é|e|são|sao|fica|ficam)\s+(proibid|fora)")
    return bool(re.search(pede, s, re.I))


def parse_only(spec: str | None, total: int) -> list[int]:
    if not spec:
        return list(range(1, total + 1))
    out: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.extend(range(int(a), int(b) + 1))
        elif part:
            out.append(int(part))
    bad = [n for n in out if n < 1 or n > total]
    if bad:
        die(f"slide(s) fora do intervalo 1..{total}: {bad}")
    return sorted(set(out))


def main() -> None:
    # linha a linha: num pipe, a saida em bloco saia depois da do r2.py (subprocesso) e da mensagem de erro (stderr)
    sys.stdout.reconfigure(line_buffering=True)
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("post_dir", help="pasta do post, contendo slides.html")
    p.add_argument("--only", help="slides a regerar, ex.: 3,5 ou 2-4")
    p.add_argument("--format", choices=["jpg", "png"], default="jpg")
    p.add_argument("--quality", type=int, default=95, help="qualidade JPEG (padrao 95)")
    p.add_argument("--out-dir", help="pasta de saida (padrao: <post>/images)")
    p.add_argument("--html", default="slides.html")
    p.add_argument("--selector", default="#stage")
    p.add_argument("--width", type=int, default=1280, help="janela larga o bastante para fit() nao encolher o stage")
    p.add_argument("--height", type=int, default=1560)
    p.add_argument("--previa", action="store_true",
                   help="poe a classe 'previa' no body: nos Stories, simula os adesivos do app por cima (stories/adesivos.css); so para conferir, nunca para publicar")
    p.add_argument("--upload", nargs=2, metavar=("BUCKET", "PREFIXO"), help="sobe a saida via r2-storage")
    p.add_argument("--sem-conferir", action="store_true", help="pula as conferencias de conferir_telas.py")
    p.add_argument("--motivo", help="peca ja publicada: o que mudou na versao nova (obrigatorio com --upload)")
    p.add_argument("--bucket-publicado", metavar="APELIDO",
                   help="Stories: o apelido do bucket onde a coleta guarda o que foi ao ar (padrao: o do --upload)")
    p.add_argument("--sem-video", action="store_true",
                   help="a tela com data-video sai em imagem, no estado parado (o quadro final); so para revisao e portao")
    p.add_argument("--som-mudo", action="store_true", help="o MP4 da tela em video leva uma faixa AAC muda")
    p.add_argument("--fps", type=int, default=30, help="quadros por segundo da tela em video (padrao 30)")
    a = p.parse_args()
    if a.upload and a.sem_conferir:
        die("--sem-conferir nao vale com --upload: o que sobe passa pelas conferencias (regra 7 da skill)")
    if a.upload and a.sem_video:
        die("--sem-video nao vale com --upload: a tela em video sobe em MP4 (o --sem-video e so para revisao)")

    # as credenciais antes de tudo: com --upload, sem a configuracao do R2, para antes de exportar, com a mensagem
    if a.upload:
        faltas = load_r2().faltas(a.upload[0], com_url=True)
        if a.bucket_publicado and a.bucket_publicado.lower() != a.upload[0].lower():
            faltas += [f for f in load_r2().faltas(a.bucket_publicado) if f not in faltas]
        if faltas:
            print("[PARE] o --upload nao roda sem a configuracao do R2. Falta:", file=sys.stderr)
            for f in faltas:
                print(f"  - {f}", file=sys.stderr)
            print(load_r2().COMO_POR.replace("--skill r2-storage", "--skill slides-export --upload"), file=sys.stderr)
            print("Sem --upload, a exportacao local roda sem chave nenhuma.", file=sys.stderr)
            sys.exit(1)
    else:
        sem = [k for k in ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY") if not ambiente.valor(k)]
        if sem:
            print("[AVISO] protecao do publicado pelo bucket desligada: faltam " + ", ".join(sem) + " (skill "
                  "r2-storage). A exportacao local segue; o que ja foi ao ar se reconhece so pelo registro da peca "
                  "(**Publicado:** da legenda.md, estagio e tabela do roteiro.md), e nada sobe ao bucket. Para ligar, "
                  "configure as chaves: python -X utf8 scripts/confere_ambiente.py --skill slides-export --upload")

    post = Path(a.post_dir).resolve()
    reg = registro_da_peca(post)
    publicada = ja_publicada(reg)   # True (a peca inteira), False ou o conjunto dos Stories ja publicados pela API
    data, fm = None, {}
    if a.upload and reg is not None and reg.name == "roteiro.md":
        texto_reg = reg.read_text(encoding="utf-8").replace("\r\n", "\n")
        fm = frontmatter(texto_reg)
        try:
            data = datetime.date.fromisoformat(fm.get("data", "").strip().strip("'\"")[:10])
        except ValueError:
            data = None
        tabela = carregar_ct().tabela_da_api(texto_reg)
        # o roteiro local pode estar atrasado (a coleta marca no remoto), e o --so publica sem gravar na tabela: o
        # bucket diz o que foi ao ar. Com o estagio ja publicado e sem tabela, nao precisa perguntar
        if not data:
            ids = None   # sem data legivel, o bucket nao foi perguntado: "nao conferido" nao e "nada publicado"
            print(f"[AVISO] o roteiro.md nao tem um 'data:' legivel (AAAA-MM-DD): a protecao dos Stories ja publicados "
                  "pelo bucket nao rodou; acerte a data no frontmatter antes de subir")
        elif tabela is not None or not publicada:
            ids = ids_no_bucket(data, a.bucket_publicado or a.upload[0])
        else:
            ids = None   # o estagio ja diz que a sequencia inteira saiu: nao se pergunta ao bucket
        publicada, msg = decidir_stories(publicada, tabela, ids)
        if msg:
            print(msg)
    if a.upload and reg is not None and reg.name == "roteiro.md" and not publicada:
        if data and data < datetime.date.today():
            die(f"a sequencia e de {data} e o estagio do roteiro.md e '{fm.get('estagio', '')}': se ela foi ao ar, "
                "acerte 'estagio: publicado' no roteiro.md e rode de novo (o upload vira uma versao nova, sem "
                "sobrescrever a publicada); se nao foi, acerte a data")
    html = post / a.html
    if not html.is_file():
        die(f"nao encontrei {html}")
    if not shutil.which("shot-scraper"):
        die("shot-scraper nao esta no PATH. Como instalar: python -m pip install shot-scraper && shot-scraper install")

    if publicada is True and a.upload and reg.name == "legenda.md":
        registrado = prefixo_registrado(reg)
        if registrado and registrado != a.upload[1].strip("/"):
            die(f"o prefixo pedido ({a.upload[1].strip('/')}) nao e o da peca publicada ({registrado}, o "
                "**Prefixo no bucket:** da legenda.md): a versao nova fica ao lado da que foi ao ar")

    texto_html = html.read_text(encoding="utf-8")
    total = len(SLIDE_RE.findall(texto_html))
    if total == 0:
        die(f"nenhuma <section class=\"slide\"> em {html}")
    wanted = parse_only(a.only, total)
    # as telas protegidas: todas na peca publicada inteira; nos Stories pela API, so as que tem linha na tabela
    protegidas = set(range(1, total + 1)) if publicada is True else set(publicada or ())
    if a.upload and protegidas & set(wanted) and not (a.motivo and a.motivo.strip()):
        die(f"a peca ja foi publicada ({reg.name}" + ("" if publicada is True else f", telas {sorted(protegidas)}")
            + "): o --upload sobe a tela publicada como versao nova em <prefixo>/versoes/versao-N/, sem "
            "sobrescrever a publicada, e pede --motivo \"<o que mudou>\" para o registro")
    if a.motivo and not protegidas & set(wanted):
        print("[--] --motivo so vale para tela ja publicada; ignorado")
    videos = {} if a.sem_video else {n: s for n, s in telas_em_video(texto_html).items() if n in wanted}
    erros_conferidos = [] if a.sem_conferir else conferir(post, a.html, (a.width, a.height),
                                                           True if publicada is True else frozenset(protegidas))
    out_dir = Path(a.out_dir).resolve() if a.out_dir else post / "images"
    out_dir.mkdir(parents=True, exist_ok=True)

    def saida_de(n: int) -> Path:
        return out_dir / f"slide-{n:02d}.{'mp4' if n in videos else a.format}"

    def js_da_tela(n: int) -> str:
        """O JS que prepara a tela n para a foto: o mesmo para o JPEG (shot-scraper) e para o video (tela_em_video)."""
        previa = "document.body.classList.add('previa');\n" if a.previa else ""
        return JS.format(idx=n - 1, previa=previa).strip()

    shots = []
    for n in wanted:
        if n in videos:
            continue
        out = saida_de(n)
        block = [f"- output: {out.as_posix()}", f"  url: {a.html}", f"  selector: \"{a.selector}\"",
                 f"  width: {a.width}", f"  height: {a.height}"]
        if a.format == "jpg":
            block.append(f"  quality: {a.quality}")
        block.append("  javascript: |")
        block += ["    " + line for line in js_da_tela(n).splitlines()]
        shots.append("\n".join(block))
    imagens = [n for n in wanted if n not in videos]
    print(f"[..] {total} slide(s) em {html.name}; exportando {wanted} -> {out_dir}"
          + (f" ({len(imagens)} em {a.format.upper()}, {len(videos)} em vídeo: telas {sorted(videos)})" if videos else
             f" em {a.format.upper()}"))
    if shots:
        config = "\n".join(shots) + "\n"
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False, encoding="utf-8") as f:
            f.write(config)
            cfg = f.name
        try:
            r = subprocess.run(["shot-scraper", "multi", cfg, *BROWSER_ARGS], cwd=post)
            if r.returncode != 0:
                die(f"shot-scraper terminou com codigo {r.returncode}")
        finally:
            os.unlink(cfg)

    if videos:
        tv = carregar_tv()
        for n, seg in sorted(videos.items()):
            if not (tv.MIN_S <= seg <= tv.MAX_S):
                die(f"tela {n}: data-video=\"{seg:g}\" fora de {tv.MIN_S:g} a {tv.MAX_S:g} s (o limite da API)")
            print(f"[..] tela {n} em vídeo: {seg:g} s a {a.fps} qps -> {saida_de(n).name}")
            try:
                g = tv.gravar(post, a.html, n - 1, seg, saida_de(n), js_da_tela(n), (a.width, a.height), a.selector,
                              a.fps, a.som_mudo)
            except Exception as e:  # noqa: BLE001 - falha da gravacao para a exportacao com a mensagem
                die(f"tela {n}: a gravacao do video falhou ({type(e).__name__}: {e})")
            if g.get("faltam"):
                # a fonte que nao carregou: o video de revisao sai na fonte de reserva, como a tela em JPEG, e o ERRO
                # barra o --upload (regra 7); a gravacao nao para o export inteiro por isso
                print(f"[ERRO] tela {n} fonte_nao_carregada: no video, "
                      + "; ".join(f"{f['familia']} ({f['fonte']})" for f in g["faltam"])
                      + " (a rede, para a fonte da web, ou o @font-face); o MP4 saiu na fonte de reserva")
                if "fonte_nao_carregada" not in erros_conferidos:
                    erros_conferidos = sorted(set(erros_conferidos) | {"fonte_nao_carregada"})
            if g["parada"]:
                print(f"[AVISO] tela {n}: todos os quadros saíram iguais; a animação não andou "
                      "(o window.quadro(t, idx) muda a tela?)")
            elif g.get("laco"):
                print(f"[--] tela {n}: em laço (o último quadro igual ao primeiro); o estado parado é o da página sem quadro")
            if not g["parada"] and not g.get("laco"):
                # o tempo parado no fim, que nenhuma conferência media (um quadro final de 0,85 s só se viu na leitura)
                p = tv.fim_parado(saida_de(n))
                if p is None:
                    print(f"[--] tela {n}: o quadro final parado não foi medido (o saltos.py da object-anatomy, o numpy ou o ffmpeg)")
                elif p < tv.FIM_PARADO_S:
                    print(f"[AVISO] tela {n} fim_parado: o quadro final fica parado {p:.2f} s, menos que os "
                          f"{tv.FIM_PARADO_S:g} s da convenção da série; a animação acaba perto do fim do vídeo")

    files = [saida_de(n) for n in wanted]
    missing = [f for f in files if not f.is_file()]
    if missing:
        die(f"saida nao gerada: {[m.name for m in missing]}")
    blocking = False
    for f in files:
        kb = f.stat().st_size // 1024
        if f.suffix.lower() == ".mp4":
            probs, avisos = carregar_tv().conferir(f)
            if not probs:
                print(f"[OK] {f} ({kb} KB, {avisos[0]}; dentro dos limites do Instagram)")
            else:
                blocking = True  # video fora dos limites a API recusaria: barra o --upload
                print(f"[AVISO] {f} ({kb} KB): " + "; ".join(probs))
            for x in avisos[1:]:
                print(f"[AVISO] {f.name}: {x}")
            continue
        probs = validate(f)
        if not probs:
            print(f"[OK] {f} ({kb} KB, dentro dos limites do Instagram)")
        else:
            blocking = blocking or any("acima de 8 MB" in x or "nao e JPEG" in x for x in probs)
            print(f"[AVISO] {f} ({kb} KB): " + "; ".join(probs))
    if "travessao" in erros_conferidos:
        voz = voz_pede_sem_travessao()
        if not voz:
            # a regra do travessao e da voz de quem usa: sem ela escrita, a conferencia nao inventa regra
            erros_conferidos = [e for e in erros_conferidos if e != "travessao"]
            print("[--] travessao no texto: nao barra, porque " + (
                "context/sobre-mim.md nao existe" if voz is None else "context/sobre-mim.md nao pede texto sem travessao")
                + " (a regra e da voz de quem usa)")
    # a copia de trabalho tem um arquivo por tela: so depois de a exportacao passar nas conferencias (sem ERRO das telas
    # e com os arquivos novos dentro dos limites), o arquivo da mesma tela no outro lado da troca imagem/video (a tela
    # que virou video, ou deixou de ser) sai, para o registro na legenda.md e o --upload nao levarem os dois. O
    # --sem-video nao apaga nada (e so revisao); o PNG, que tambem e so revisao, cai no "fora dos limites" e nao apaga
    if not a.sem_video and not blocking and not erros_conferidos:
        for n in wanted:
            for velho in out_dir.glob(f"slide-{n:02d}.*"):
                if velho.suffix.lower() in EXT_ITEM and (velho.suffix.lower() == ".mp4") != (n in videos):
                    velho.unlink()
    if a.upload and blocking:
        die("upload cancelado: ha arquivo fora dos limites de publicacao do Instagram")
    if a.upload and erros_conferidos:
        o_que = []
        if any(e.startswith("sobreposicao") for e in erros_conferidos):
            o_que.append("corrigir a tela (ou, se o desenho cobre o texto de proposito, marcar o elemento com a classe "
                         "'intencional', conferindo antes que ele nao cruza outra palavra)")
        if "hashtags" in erros_conferidos:
            o_que.append("deixar no maximo 5 hashtags na legenda.md")
        # regras da casa: o que fazer em cada uma, o texto da tabela de achados da visual-form (references/conferencias.md)
        CASA = {"contraste": "trocar a cor do texto (4,5:1 no corrido, 3:1 no grande)",
                "contraste_parcial": "tirar o texto de cima do traco ou do desenho (ou trocar a cor)",
                "transbordo": "fazer o texto caber na tela; sinal grafico que sangra de proposito leva data-sangria",
                "corte": "fazer o texto caber na caixa que o corta; sangria de proposito leva data-sangria",
                "alinhamento_titulo": "alinhar o titulo a posicao das telas irmas; acima de 100 px, se for escolha, "
                                      "declarar com data-alinhamento no titulo",
                "cor_anulada": "por a cor na classe ou no style, para o svg sair como declarado",
                # area segura, zona proibida, travessao e a fonte antes da medida
                "area_segura": "trazer o texto para dentro de y 192 a 1802 e x 32 a 1048 (a interface do app cobre o resto)",
                "zona_proibida": "trazer o texto para dentro da area de 1000 por 1270 centrada; sinal que sangra de "
                                 "proposito leva data-sangria",
                "travessao": "tirar o travessao do texto (da tela ou da legenda), como pede a voz em context/sobre-mim.md: "
                             "virgula, dois-pontos ou frase nova",
                "fonte_nao_carregada": "fazer a fonte carregar (a rede, para a fonte da web, ou o @font-face) e "
                                       "exportar de novo: a imagem e as medidas sairiam na fonte de reserva"}
        o_que += [CASA[e] for e in erros_conferidos if e in CASA]
        if "video" in erros_conferidos:
            o_que.append("na tela em video, definir window.quadro(t, idx) na pagina e o data-video de 3 a 60 s")
        if "nao_rodou" in erros_conferidos:
            o_que.append("fazer as conferencias rodarem (o erro esta acima)")
        die("upload cancelado pelas conferencias (" + ", ".join(erros_conferidos) + "): " + "; ".join(o_que)
            + "; depois exportar de novo")

    bucket = prefix = None
    # a tela publicada sobe como versao nova; a ainda sem publicar (nos Stories pela API, sem linha na tabela) sobe no
    # proprio prefixo, com o mesmo nome, como antes de publicar (o criterio em references/projeto.md)
    files_prot = [saida_de(n) for n in wanted if n in protegidas]
    files_livres = [saida_de(n) for n in wanted if n not in protegidas]
    if a.upload and files_prot:
        # depois de publicada, nada se sobrescreve: a versao nova vai para <prefixo>/versoes/versao-N/
        bucket, prefix = a.upload[0], a.upload[1].strip("/")
        n = max([1] + versoes_registradas(reg) + versoes_no_bucket(bucket, prefix)) + 1
        destino = f"{prefix}/versoes/versao-{n}"
        print(f"[..] {'peca ja publicada' if publicada is True else 'telas ja publicadas ' + str(sorted(protegidas & set(wanted)))}: "
              f"versao {n}, em {destino}/")
        subiram, falhou = [], None
        for f in files_prot:
            r = subprocess.run([sys.executable, str(R2), "put", bucket, str(f), f"{destino}/{f.name}"])
            if r.returncode != 0:
                falhou = f
                break
            subiram.append(f)
        r2 = load_r2()
        links = []
        for f in subiram:
            url = r2.public_url(r2.bucket(bucket), f"{destino}/{f.name}")
            links.append(f"[{f.stem}]({url})" if url else f"`{destino}/{f.name}`")
        # o registro so cresce: a versao que subiu pela metade fica registrada, marcada, e a proxima usa outro N
        registrar_versao(reg, n, a.motivo, links,
                         incompleta=f"subiram {len(subiram)} de {len(files_prot)}" if falhou else "")
        if falhou:
            die(f"upload falhou em {falhou.name}; a versao {n} ficou registrada como incompleta")
        if reg.name == "legenda.md":
            print("[--] peca publicada: **Imagens:** e ## Slides ficam como estao (o registro do que foi ao ar)")
        if not files_livres:
            return
    if a.upload:
        bucket, prefix = a.upload
        prefix = prefix.strip("/")
        if files_prot:
            print(f"[..] telas ainda sem publicar {[f.name for f in files_livres]}: no proprio prefixo, {prefix}/")
        for f in files_livres:
            r = subprocess.run([sys.executable, str(R2), "put", bucket, str(f), f"{prefix}/{f.name}"])
            if r.returncode != 0:
                die(f"upload falhou em {f.name}")
        # a tela que virou video (ou deixou de ser) deixa no prefixo o arquivo do outro formato com o mesmo numero; a
        # publicacao recusa o numero repetido, e o velho sai a mao, uma chave por vez e confirmada na conversa
        # (regra 2 da r2-storage)
        r2 = load_r2()
        no_prefixo = []
        for page in r2.client().get_paginator("list_objects_v2").paginate(Bucket=r2.bucket(bucket), Prefix=prefix + "/"):
            no_prefixo += [o["Key"] for o in page.get("Contents", []) if "/" not in o["Key"][len(prefix) + 1:]]
        repetidos = [k for k in mesma_tela_outro_formato(no_prefixo) if Path(k).name not in {f.name for f in files}]
        for k in repetidos:
            print(f"[AVISO] {k} ficou no bucket com o numero de uma tela que agora sai em outro formato: quem publica "
                  f"recusa o numero repetido; remover depois de confirmar na conversa, uma chave por vez: "
                  f"`python {R2.relative_to(ROOT).as_posix()} rm {bucket} {k}`")

    if publicada and reg.name == "legenda.md":
        print("[--] peca ja publicada: **Imagens:** e ## Slides ficam como estao (o registro do que foi ao ar)")
    elif publicada:
        pass  # Stories: o roteiro.md nao tem secao de imagens a reescrever
    elif a.sem_video:
        print("[--] --sem-video e so revisao: **Imagens:** e ## Slides ficam como estao")
    elif out_dir.is_relative_to(post):
        record_in_legenda(post, out_dir, bucket, prefix, {f.name for f in files})
    else:
        print(f"[--] saida fora da pasta do post ({out_dir}); nada registrado na peca")


if __name__ == "__main__":
    main()
