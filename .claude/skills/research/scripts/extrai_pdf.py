"""Extração barata de PDF longo: o texto por script, e a leitura em imagem só nas páginas que pedem.

O método: em vez de transcrever página a página, extrai-se o texto
de cada página por script, com a marca da página, e levanta-se, por página, o que precisa de olho:

  - `sem_texto`: a camada de texto tem menos de `--min-chars` caracteres (página escaneada, só figura);
  - `imagem`: as imagens cobrem pelo menos `--min-area-imagem` da página (figura, foto, tabela em imagem).
    Na página escaneada com OCR (uma imagem cobre a página inteira e há camada de texto), a imagem é o
    próprio papel, e a marca vem do texto: os blocos de texto cobrem menos de `--min-cobertura-texto` da
    página, o que sobra é figura, tabela ou foto (na BYTE de 1977, a página da tabela da esfera tinha 0,27,
    e a mediana das páginas, 0,45);
  - `tabela`: o PyMuPDF acha uma tabela, a página tem uma grade desenhada (pelo menos três traços retos em
    cada direção, ou `--min-tracos` no total; a caixa cheia de fundo não conta), ou, sem a grade
    (a tabela escaneada), pelo menos `--max-numeros` das palavras são números ou fragmentos de até dois
    caracteres;
  - `estranho`: caractere de substituição, de controle ou de uso privado acima do limiar (fonte sem mapa
    para Unicode), menos de `--min-palavras` das palavras com cara de palavra (OCR ruim), ou muitas palavras
    partidas por hífen no fim da linha;
  - `colunas`: muitas linhas curtíssimas seguidas, sinal de colunas lidas fora de ordem;
  - `citada`: a página que uma ficha cita (`--citadas 3,15` ou `--fichas <arquivos>`, que procura "PDF p. N"
    e "p. N" nas fichas; com `--fichas`, o nome do PDF precisa aparecer na ficha).

Só as páginas levantadas (menos as que só têm `citada`, a menos que `--render-citadas`) viram imagem, a
`--dpi` (padrão 200; a tabela da BYTE de 1977 pediu 400), numa pasta de trabalho. Quem confere lê essas
imagens e as compara com o texto daquela página; o resto fica com o texto do script.

Sai, em `--saida`:
  - `<nome>.md`: o texto, com `<!-- página N -->` antes de cada página; com `--numerar`, cada linha leva o
    número dela dentro da página (`L12| ...`), para achar o trecho no `.md`: a "l. L" é da extração (muda com o
    motor e a ordenação) e não se acha no original, então a ficha cita a página do PDF, "PDF p. N";
  - `<nome>.pontos.json`: por página, as marcas e as medidas, e o resumo de custo (páginas, caracteres,
    tempo de extração e de render, páginas marcadas, imagens geradas);
  - `<nome>.pontos.md`: a mesma lista para ler, só as páginas marcadas;
  - `paginas/<nome>-pNNNN.png`: as páginas renderizadas.

O texto de obra protegida é cópia de trabalho, fora do git (`knowledge/sources/README.md`, "A cópia de
trabalho"): a saída vai ao `originals/` ao lado do que a usa. Na rodada, `knowledge/research-rounds/<rodada>/originals/`;
no material curado fora de rodada, `knowledge/sources/originals/`.

Motor: PyMuPDF (`pymupdf`). O material baixado se lê com `python -I -X utf8` (CLAUDE.md), e o `-I` ignora o
site do usuário, onde o PyMuPDF costuma estar: rode pelo python de uma venv que o tenha (no Windows,
`<venv>/Scripts/python.exe -I -X utf8 extrai_pdf.py ...`; no macOS e no Linux, `<venv>/bin/python`; a venv é vista com `-I`). Com
`--motor auto` e sem o PyMuPDF, o script para (código 2) em vez de cair calado no `pdftotext`; só com
`--aceitar-pdftotext` (ou `--motor pdftotext`) ele segue, e então o `.pontos.md` diz no topo que a lista não
vale como conferência: o `pdftotext` dá o texto e as marcas que saem dele (`sem_texto`, a tabela pelos
números, `estranho`, `colunas`), sem as que pedem o PDF (`imagem`, a tabela achada pelo PyMuPDF, a grade
desenhada) nem render.

Uso:
  python -X utf8 extrai_pdf.py <arquivo.pdf> --saida <pasta> [--numerar] [--dpi 200] [--sem-render]
         [--citadas 3,15] [--fichas knowledge/sources/*.md] [--paginas 1-40]
Código de saída: 0 sem página marcada; 1 com página marcada (o caso normal: há o que conferir, não é falha);
2 erro (entrada, leitura, ou o motor sem o PyMuPDF sem `--aceitar-pdftotext`).
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
import unicodedata
from pathlib import Path

try:
    import pymupdf  # PyMuPDF
except Exception:  # pragma: no cover - o caminho sem PyMuPDF se testa com --motor pdftotext
    pymupdf = None

MARCAS = ("sem_texto", "imagem", "tabela", "estranho", "colunas", "citada")


def faixa(txt: str | None, total: int) -> list[int]:
    """'1-3,7' -> [1, 2, 3, 7], dentro de 1..total."""
    if not txt:
        return list(range(1, total + 1))
    out: set[int] = set()
    for parte in txt.split(","):
        parte = parte.strip()
        if not parte:
            continue
        if "-" in parte:
            a, b = parte.split("-", 1)
            out.update(_intervalo(int(a), int(b), total))
        else:
            out.add(int(parte))
    return sorted(p for p in out if 1 <= p <= total)


def _intervalo(a: int, b: int, total: int) -> range:
    """O intervalo a..b limitado a 1..total antes de expandir (um '1-1000000000' não estoura a memória)."""
    return range(max(a, 1), min(b, total) + 1)


def citadas_nas_fichas(padroes: list[str], nome_pdf: str, total: int) -> set[int]:
    """As páginas que as fichas citam como 'PDF p. N' (ou 'p. N' na ficha que nomeia o PDF)."""
    pags: set[int] = set()
    base = Path(nome_pdf).stem.lower()
    for padrao in padroes:
        for arq in glob.glob(padrao, recursive=True):
            try:
                txt = Path(arq).read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for m in re.finditer(r"PDF\s+p\.\s*(\d+)(?:\s*[-–]\s*(\d+))?", txt):
                a = int(m.group(1)); b = int(m.group(2) or a)
                pags.update(_intervalo(a, b, total))
            if base and base in txt.lower():
                for m in re.finditer(r"(?<![\w.])p\.\s*(\d+)(?:\s*[-–]\s*(\d+))?", txt):
                    a = int(m.group(1)); b = int(m.group(2) or a)
                    pags.update(_intervalo(a, b, total))
    return pags


def medidas_texto(txt: str) -> dict:
    """Os sinais de extração ruim no texto de uma página."""
    chars = len(txt.strip())
    ruins = 0
    for c in txt:
        if c in "\n\r\t ":
            continue
        cat = unicodedata.category(c)
        if c == "�" or cat in ("Cc", "Co", "Cs", "Cn"):
            ruins += 1
    linhas = [ln for ln in txt.splitlines() if ln.strip()]
    toks = re.findall(r"\S+", txt)
    palavra = sum(1 for t in toks if re.fullmatch(r"[(\"“‘']?[^\W\d_]+(?:['’-][^\W\d_]+)*[.,;:!?)\"”’]*", t))
    numero = sum(1 for t in toks if re.fullmatch(r"[\d.,%$()+\-/:]+", t) or len(t) <= 2)
    hifen = sum(1 for ln in linhas if re.search(r"\w-$", ln.rstrip()))
    curtas = sum(1 for ln in linhas if len(ln.strip()) <= 3)
    return {
        "chars": chars,
        "linhas": len(linhas),
        "ruins": ruins,
        "frac_ruins": round(ruins / chars, 4) if chars else 0.0,
        "hifen_fim": hifen,
        "frac_curtas": round(curtas / len(linhas), 3) if linhas else 0.0,
        "palavras": len(toks),
        "frac_palavras": round(palavra / len(toks), 3) if toks else 0.0,
        "frac_numeros": round(numero / len(toks), 3) if toks else 0.0,
    }


def marcar(m: dict, args) -> list[str]:
    out = []
    if m["chars"] < args.min_chars:
        out.append("sem_texto")
    if m.get("escaneada"):
        if m.get("cobertura_texto", 1) < args.min_cobertura_texto:
            out.append("imagem")
    elif m.get("area_imagem", 0) >= args.min_area_imagem:
        out.append("imagem")
    texto_tabela = m["palavras"] >= 40 and m["frac_numeros"] >= args.max_numeros
    if m.get("tabelas", 0) > 0 or m.get("grade") or m.get("tracos", 0) >= args.min_tracos or texto_tabela:
        out.append("tabela")
    ocr_ruim = m["palavras"] >= 40 and m["frac_palavras"] < args.min_palavras
    hifen = m["linhas"] and m["hifen_fim"] / m["linhas"] >= 0.25 and m["hifen_fim"] >= 5
    if m["chars"] and (m["frac_ruins"] >= args.max_ruins or ocr_ruim or hifen):
        out.append("estranho")
    if m["linhas"] >= 10 and m["frac_curtas"] >= args.max_curtas:
        out.append("colunas")
    return out


def extrair_pymupdf(pdf: Path, paginas: list[int], args) -> tuple[dict[int, str], dict[int, dict]]:
    doc = pymupdf.open(str(pdf))
    textos: dict[int, str] = {}
    meds: dict[int, dict] = {}
    for n in paginas:
        pg = doc[n - 1]
        txt = pg.get_text("text", sort=True)
        m = medidas_texto(txt)
        area_pg = abs(pg.rect) or 1.0
        # na página girada, as caixas e o pg.rect podem estar em sistemas diferentes: a área não depende da
        # rotação, então ali se soma a área sem cortar pela página (o min(..., 1.0) segura o excesso)
        def corta(rr):
            return rr if pg.rotation else rr & pg.rect
        infos = pg.get_image_info()
        area_img = sum(abs(corta(pymupdf.Rect(i.get("bbox", (0, 0, 0, 0))))) for i in infos)
        m["area_imagem"] = round(min(area_img / area_pg, 1.0), 3)
        maior = max((abs(corta(pymupdf.Rect(i.get("bbox", (0, 0, 0, 0))))) for i in infos), default=0.0)
        # o papel escaneado com OCR: uma imagem cobre a página e há camada de texto; sem texto, é só imagem
        m["escaneada"] = maior / area_pg >= 0.9 and m["chars"] >= args.min_chars
        cob = sum(abs(corta(pymupdf.Rect(b[:4]))) for b in pg.get_text("blocks") if b[6] == 0)
        m["cobertura_texto"] = round(min(cob / area_pg, 1.0), 3)
        tabelas = 0
        if not args.sem_tabela and not m["escaneada"]:  # no papel escaneado não há tabela vetorial a achar
            try:
                tabelas = len(pg.find_tables().tables)
            except Exception:
                tabelas = 0
        m["tabelas"] = tabelas
        # a grade: segmentos retos horizontais e verticais de pelo menos 20 pt, e o retângulo fino (a linha
        # desenhada como caixa de 1 pt); a caixa cheia (fundo, realce) não é grade: num livro digital, 29 caixas de
        # fundo por página marcavam todo o livro como tabela
        hor = ver = 0
        for d in pg.get_drawings():
            for it in d.get("items", []):
                if it[0] == "l":
                    p1, p2 = it[1], it[2]
                    if abs(p1.y - p2.y) < 0.5 and abs(p1.x - p2.x) >= 20:
                        hor += 1
                    elif abs(p1.x - p2.x) < 0.5 and abs(p1.y - p2.y) >= 20:
                        ver += 1
                elif it[0] == "re":
                    r = it[1]
                    if r.height < 2 and r.width >= 20:
                        hor += 1
                    elif r.width < 2 and r.height >= 20:
                        ver += 1
        m["tracos"] = hor + ver
        m["grade"] = hor >= 3 and ver >= 3
        textos[n] = txt
        meds[n] = m
    doc.close()
    return textos, meds


def extrair_pdftotext(pdf: Path, paginas: list[int]) -> tuple[dict[int, str], dict[int, dict]]:
    exe = shutil.which("pdftotext")
    if not exe:
        raise RuntimeError("nem o PyMuPDF nem o pdftotext estão disponíveis")
    textos, meds = {}, {}
    for n in paginas:
        r = subprocess.run([exe, "-enc", "UTF-8", "-layout", "-f", str(n), "-l", str(n), str(pdf), "-"],
                           capture_output=True)
        if r.returncode != 0:  # PDF cifrado ou corrompido: erro, e não página vazia
            erro = r.stderr.decode("utf-8", errors="replace").strip()[-300:]
            raise RuntimeError(f"pdftotext falhou na página {n} (código {r.returncode}): {erro}")
        txt = r.stdout.decode("utf-8", errors="replace")
        textos[n] = txt
        meds[n] = medidas_texto(txt)
    return textos, meds


def total_paginas(pdf: Path, motor: str) -> int:
    # para contar, qualquer leitor serve (o PyMuPDF, se estiver aqui, mesmo com o motor pdftotext; o pypdf; o pdfinfo)
    if pymupdf is not None:
        with pymupdf.open(str(pdf)) as d:
            return d.page_count
    try:
        from pypdf import PdfReader
        return len(PdfReader(str(pdf)).pages)
    except Exception:
        exe = shutil.which("pdfinfo")
        if not exe:
            # o último recurso: o pdftotext separa as páginas por quebra de página (\f)
            txt_exe = shutil.which("pdftotext")
            if not txt_exe:
                raise RuntimeError("não deu para contar as páginas: sem o PyMuPDF, o pypdf, o pdfinfo ou o pdftotext")
            r = subprocess.run([txt_exe, "-enc", "UTF-8", str(pdf), "-"], capture_output=True)
            if r.returncode != 0:
                raise RuntimeError("o pdftotext não leu o PDF: " + r.stderr.decode("utf-8", errors="replace").strip()[-300:])
            return max(1, r.stdout.count(b"\f"))
        r = subprocess.run([exe, str(pdf)], capture_output=True, text=True)
        m = re.search(r"Pages:\s+(\d+)", r.stdout or "")
        if not m:
            raise RuntimeError("não deu para contar as páginas")
        return int(m.group(1))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pdf")
    ap.add_argument("--saida", required=True, help="pasta de trabalho (fora do git para obra protegida)")
    ap.add_argument("--paginas", help="faixa, como 1-40,52 (padrão: todas)")
    ap.add_argument("--numerar", action="store_true", help="numera as linhas dentro de cada página")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--sem-render", action="store_true")
    ap.add_argument("--render-citadas", action="store_true", help="renderiza também as páginas só citadas")
    ap.add_argument("--sem-tabela", action="store_true", help="pula a busca de tabela (a parte mais lenta)")
    ap.add_argument("--citadas", help="páginas citadas por fichas, como 3,15-17")
    ap.add_argument("--fichas", nargs="*", default=[], help="fichas para achar 'PDF p. N' (aceita glob)")
    ap.add_argument("--motor", choices=["auto", "pymupdf", "pdftotext"], default="auto")
    ap.add_argument("--aceitar-pdftotext", action="store_true",
                    help="com --motor auto e sem o PyMuPDF, seguir pelo pdftotext (a lista não vale como conferência)")
    ap.add_argument("--min-chars", type=int, default=200)
    ap.add_argument("--min-area-imagem", type=float, default=0.25)
    ap.add_argument("--min-tracos", type=int, default=40)
    ap.add_argument("--max-ruins", type=float, default=0.02)
    ap.add_argument("--max-curtas", type=float, default=0.35)
    ap.add_argument("--min-cobertura-texto", type=float, default=0.30)
    ap.add_argument("--max-numeros", type=float, default=0.45)
    ap.add_argument("--min-palavras", type=float, default=0.70)
    args = ap.parse_args(argv)

    pdf = Path(args.pdf)
    if not pdf.is_file():
        print(f"ERRO: {pdf} não existe", file=sys.stderr)
        return 2
    motor = args.motor
    if motor == "auto":
        if pymupdf is None and not args.aceitar_pdftotext:
            print("ERRO: o PyMuPDF não está disponível neste python (com -I, ele precisa estar numa venv que o -I "
                  "veja, como a criada por python -m venv <pasta>). Sem ele, as marcas imagem, tabela e o render somem e a lista de "
                  "pontos não vale como conferência; para seguir assim mesmo, passe --aceitar-pdftotext",
                  file=sys.stderr)
            return 2
        motor = "pymupdf" if pymupdf is not None else "pdftotext"
    if motor == "pymupdf" and pymupdf is None:
        print("ERRO: --motor pymupdf pedido, mas o PyMuPDF não está instalado", file=sys.stderr)
        return 2
    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)

    t0 = time.perf_counter()
    try:
        total = total_paginas(pdf, motor)
        paginas = faixa(args.paginas, total)
        if motor == "pymupdf":
            textos, meds = extrair_pymupdf(pdf, paginas, args)
        else:
            textos, meds = extrair_pdftotext(pdf, paginas)
    except Exception as e:
        print(f"ERRO ao ler {pdf}: {e}", file=sys.stderr)
        return 2
    t_ext = time.perf_counter() - t0

    citadas: set[int] = set(faixa(args.citadas, total)) if args.citadas else set()
    if args.fichas:
        citadas |= citadas_nas_fichas(args.fichas, pdf.name, total)

    nome = pdf.stem
    # dois PDFs de mesmo nome em pastas diferentes não se sobrescrevem: se a saída já é de outro caminho, o
    # nome ganha um pedaço do hash do caminho
    anterior = saida / f"{nome}.pontos.json"
    if anterior.is_file():
        try:
            caminho_ant = json.loads(anterior.read_text(encoding="utf-8"))["resumo"].get("caminho")
        except Exception:
            caminho_ant = None
        if caminho_ant and caminho_ant != str(pdf.resolve()):
            nome = f"{nome}-{hashlib.sha1(str(pdf.resolve()).encode('utf-8')).hexdigest()[:6]}"
    por_pagina = {}
    for n in paginas:
        marcas = marcar(meds[n], args)
        if n in citadas:
            marcas.append("citada")
        por_pagina[n] = {"marcas": marcas, **meds[n]}

    # o texto, com a marca de cada página
    partes = []
    for n in paginas:
        partes.append(f"<!-- página {n} -->")
        linhas = textos[n].rstrip("\n").splitlines()
        if args.numerar:
            partes.extend(f"L{i}| {ln}" for i, ln in enumerate(linhas, 1))
        else:
            partes.extend(linhas)
        partes.append("")
    (saida / f"{nome}.md").write_text("\n".join(partes) + "\n", encoding="utf-8", newline="\n")

    # o render só do que pede olho
    t1 = time.perf_counter()
    geradas = []
    if not args.sem_render and motor == "pymupdf":
        alvo = [n for n in paginas if any(m != "citada" for m in por_pagina[n]["marcas"])
                or (args.render_citadas and "citada" in por_pagina[n]["marcas"])]
        pasta_pg = saida / "paginas"
        if pasta_pg.is_dir():
            for velho in pasta_pg.glob(f"{nome}-p*.png"):
                velho.unlink()  # as imagens de uma rodada anterior com outras marcas não se confundem com estas
        if alvo:
            pasta_pg.mkdir(exist_ok=True)
            with pymupdf.open(str(pdf)) as d:
                for n in alvo:
                    arq = saida / "paginas" / f"{nome}-p{n:04d}.png"
                    d[n - 1].get_pixmap(dpi=args.dpi).save(str(arq))
                    geradas.append(arq.name)
    t_ren = time.perf_counter() - t1

    marcadas = [n for n in paginas if por_pagina[n]["marcas"]]
    contagem = {m: sum(1 for n in paginas if m in por_pagina[n]["marcas"]) for m in MARCAS}
    resumo = {
        "pdf": pdf.name,
        "caminho": str(pdf.resolve()),
        "motor": motor,
        "paginas_no_pdf": total,
        "paginas_lidas": len(paginas),
        "chars": sum(meds[n]["chars"] for n in paginas),
        "paginas_escaneadas": sum(1 for n in paginas if meds[n].get("escaneada")),
        "paginas_marcadas": len(marcadas),
        "por_marca": contagem,
        "imagens_geradas": len(geradas),
        "dpi": args.dpi,
        "segundos_extracao": round(t_ext, 2),
        "segundos_render": round(t_ren, 2),
        "aviso": None if motor == "pymupdf" else (
            "pdftotext: a lista não vale como conferência; há o texto e as marcas que saem dele (sem_texto, a "
            "tabela pelos números, estranho, colunas), sem imagem, a tabela do PyMuPDF, a grade nem render"),
    }
    (saida / f"{nome}.pontos.json").write_text(
        json.dumps({"resumo": resumo, "paginas": {str(n): por_pagina[n] for n in paginas}}, ensure_ascii=False, indent=1),
        encoding="utf-8", newline="\n")

    md = [f"# Pontos a conferir: {pdf.name}", ""]
    if resumo["aviso"]:
        md += [f"> **Atenção:** {resumo['aviso']}.", ""]
    md += [
          f"{len(marcadas)} de {len(paginas)} páginas marcadas; {len(geradas)} renderizadas a {args.dpi} dpi; "
          f"extração em {resumo['segundos_extracao']} s, render em {resumo['segundos_render']} s (motor: {motor}).", "",
          "| Página | Marcas | Caracteres | Imagem (área) | Texto (cobertura) | Palavras | Números | Tabelas |",
          "|---|---|---|---|---|---|---|---|"]
    for n in marcadas:
        p = por_pagina[n]
        md.append(f"| {n} | {', '.join(p['marcas'])} | {p['chars']} | {p.get('area_imagem', '-')} | "
                  f"{p.get('cobertura_texto', '-')} | {p.get('frac_palavras', '-')} | {p.get('frac_numeros', '-')} | "
                  f"{p.get('tabelas', '-')} |")
    (saida / f"{nome}.pontos.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")

    print(json.dumps(resumo, ensure_ascii=False))
    return 1 if marcadas else 0


if __name__ == "__main__":
    sys.exit(main())
