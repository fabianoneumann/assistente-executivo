"""A conferência de todo vídeo de Story: os
limites da API para o vídeo de Story e, como leitura, o movimento medido e a folha de quadros.

  python -X utf8 video_do_story.py <arquivo.mp4> [--folha <saida.jpg>]

- **Os limites** (ERRO, barram a publicação): a conferência do `tela_em_video.py` da slides-export, no perfil "story"
  (o `moov` no começo, sem lista de edição, H.264 ou HEVC, 4:2:0, 23 a 60 qps, 3 a 60 s, até 25 Mbps e 100 MB, AAC até
  48 kHz, largura até 1920 e proporção de 0,1:1 a 10:1, com AVISO fora do 9:16 recomendado), da referência da Meta para a
  publicação de mídia, lida em 2026-11-13. A proporção do carrossel não vale aqui.
- **O movimento** (leitura, sem nível): o `saltos.py` da object-anatomy, os picos isolados e o fim parado.
- **A folha de quadros** (leitura): os quadros a 0, 30, 60 e 90% da duração, lado a lado, para olhar o vídeo pelos
  quadros-chave (`knowledge/generative-media/reels-de-referencia-feitos-em-codigo.md`, a conferência depois do render).
  Sem --folha, sai ao lado do MP4, como <nome>-folha.jpg.
- **O roteiro** (AVISO, não barra): o `roteiro.md` da sequência (o
  de --roteiro, ou o achado ao lado do MP4 ou uma pasta acima). O tempo: a conta frase a frase da tabela de tempo
  ("| Tempo | Na tela | ... |", uma linha por trecho, "0–7 s"): cada frase fica pelo menos `caracteres ÷ 17` s e
  0,3 s por palavra, contados do começo da linha até o fim dela (o começo da saída), cada frase da célula sozinha
  (as várias frases de uma linha separadas por " / "; a que entra depois vai na linha dela); a frase abaixo da régua
  se divide, não acelera (`knowledge/content-design/tempo-de-leitura-em-video.md`, critérios 1 e 3:
  frase a frase, não a soma). A legenda: o vídeo com voz (`voz: true` no frontmatter, ou a `funcao` de vídeo falando para
  a câmera) declara a legenda revisada numa linha "legenda: ..., revisada" (adesivo ou queimada).

  python -X utf8 video_do_story.py --roteiro <roteiro.md>      (só o roteiro, antes de gravar)

Quem chama: o `anima_cena.py` depois de gravar; rode também antes de publicar qualquer vídeo de Story (todo gerador: anima_cena,
anima_svg, sprite_loop, o HyperFrames, o vídeo de câmera). Pede o ffmpeg e o ffprobe no PATH. Sai com 1 quando há ERRO.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SLIDES_EXPORT = ROOT / ".claude" / "skills" / "slides-export" / "scripts"
OBJECT_ANATOMY = ROOT / ".claude" / "skills" / "object-anatomy" / "scripts"
PONTOS = (0.0, 0.3, 0.6, 0.9)   # as frações da duração da folha (a da visual-form, references/projeto.md)
CARACTERES_POR_S, PISO_POR_PALAVRA = 17, 0.3   # tempo-de-leitura-em-video.md, critério 1 (Netflix em português; BBC)
TRECHO = re.compile(r"^\s*(\d+(?:[.,]\d+)?)\s*[–-]\s*(\d+(?:[.,]\d+)?)\s*s\b")   # "7–12,6 s"
COLUNAS_DE_TEXTO = ("na tela", "legenda", "frase", "texto")


def _importar(pasta: Path, nome: str):
    if str(pasta) not in sys.path:
        sys.path.insert(0, str(pasta))
    return __import__(nome)


def limites(mp4: Path) -> tuple[list[str], list[str]]:
    """(problemas que barram a publicação, avisos), pelo perfil Story do tela_em_video.py."""
    return _importar(SLIDES_EXPORT, "tela_em_video").conferir(Path(mp4), "story")


def movimento(mp4: Path) -> str:
    """A linha do saltos.py (leitura, sem nível), ou o motivo de não ter medido."""
    try:
        r = _importar(OBJECT_ANATOMY, "saltos").medir(str(mp4))
    except Exception as e:  # noqa: BLE001 - a leitura não barra; diz por que não mediu
        return f"movimento não medido ({type(e).__name__}: {e})"
    return (f"{r['quadros']} quadros a {r['fps']} qps; picos isolados: {r['picos'] or 'nenhum'}"
            f"{'; no quadro-chave: ' + str(r['picos_chave']) if r['picos_chave'] else ''}; "
            f"parado no fim: {r['parado_quadros']} quadros ({r.get('parado_s', 0):.2f} s)")


def duracao(mp4: Path) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip() or 0)


def folha(mp4: Path, saida: Path) -> Path:
    """Os quadros a 0, 30, 60 e 90% lado a lado, com a fração escrita em cima; cada quadro a 270 px de largura."""
    from PIL import Image, ImageDraw
    dur = duracao(mp4)
    quadros = []
    with tempfile.TemporaryDirectory(prefix="folha-story-") as tmp:
        for k, f in enumerate(PONTOS):
            q = Path(tmp) / f"q{k}.png"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{f * dur:.3f}", "-i", str(mp4), "-frames:v", "1",
                            str(q)], check=True, capture_output=True)
            im = Image.open(q).convert("RGB")
            quadros.append(im.resize((270, max(1, round(270 * im.height / im.width)))))
    g, topo = 12, 36
    h = max(q.height for q in quadros)
    out = Image.new("RGB", (g + len(quadros) * (270 + g), topo + h + g), "white")
    dr = ImageDraw.Draw(out)
    for k, (f, q) in enumerate(zip(PONTOS, quadros)):
        x = g + k * (270 + g)
        out.paste(q, (x, topo))
        dr.text((x, 10), f"{round(f * 100)}% ({f * dur:.1f} s)", fill="black")
    saida.parent.mkdir(parents=True, exist_ok=True)
    out.save(saida, quality=90)
    return saida


def _limpa(celula: str) -> str:
    """O texto da célula sem a marcação do markdown (==marca-texto==, **negrito**, *itálico*, `código`)."""
    t = re.sub(r"==|\*\*|`", "", celula)
    t = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def tempos_do_roteiro(texto: str) -> list[tuple[float, float, str]]:
    """As frases da tabela de tempo do roteiro: [(início, fim, frase)]. A tabela é a que abre com a coluna "Tempo", e
    o texto vem da coluna "Na tela" (ou "Legenda", "Frase", "Texto"; senão, a segunda). A linha sem trecho em segundos
    ("o vídeo todo", a etiqueta fixa) fica de fora; as frases de uma célula se separam por " / "."""
    out, cols = [], None
    for linha in texto.splitlines():
        if not linha.strip().startswith("|"):
            cols = None
            continue
        cel = [c.strip() for c in linha.strip().strip("|").split("|")]
        if cols is None:
            nomes = [c.lower() for c in cel]
            if nomes and nomes[0].startswith("tempo"):
                cols = next((i for i, c in enumerate(nomes) if any(c.startswith(n) for n in COLUNAS_DE_TEXTO)), 1)
            else:
                cols = -1   # outra tabela: as linhas dela ficam de fora
            continue
        if cols < 0 or set("".join(cel)) <= set("-: "):
            continue
        m = TRECHO.match(cel[0])
        if not m or cols >= len(cel):
            continue
        ini, fim = (float(x.replace(",", ".")) for x in m.groups())
        out += [(ini, fim, f) for f in (_limpa(x) for x in cel[cols].split(" / ")) if f]
    return out


def pede(frase: str) -> float:
    """Os segundos que a frase pede: o maior entre `caracteres ÷ 17` (espaço e pontuação contam) e 0,3 s por palavra."""
    return max(len(frase) / CARACTERES_POR_S, PISO_POR_PALAVRA * len(frase.split()))


def _fmt(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def conferir_roteiro(roteiro: Path) -> list[str]:
    """Os AVISOs do roteiro: a frase abaixo da régua do tempo de leitura e o vídeo com voz sem a legenda
    revisada declarada. Lista vazia quando passa."""
    texto = Path(roteiro).read_text(encoding="utf-8")
    avisos = []
    for ini, fim, frase in tempos_do_roteiro(texto):
        if pede(frase) > fim - ini + 1e-9:
            curta = frase if len(frase) <= 60 else frase[:57] + "..."
            avisos.append(f"tempo de leitura: \"{curta}\" ({_fmt(ini)}–{_fmt(fim)} s) pede {_fmt(round(pede(frase), 1))} s "
                          f"e fica {_fmt(round(fim - ini, 1))} s; divida a frase em vez de acelerar")
    fm = re.match(r"---\r?\n(.*?)\r?\n---", texto, re.S)
    campos = dict(re.findall(r"(?m)^(\w+):[ \t]*(.*)$", fm.group(1))) if fm else {}
    funcao = campos.get("funcao", "").lower()
    voz = (campos.get("voz", "").strip().strip("\"'").lower() in ("true", "sim", "yes")
           or "câmera" in funcao or "camera" in funcao)
    if voz and not re.search(r"(?im)legenda:[^\n]*revisada", texto):
        avisos.append("vídeo com voz sem a legenda revisada declarada: o roteiro diz \"legenda: adesivo, revisada\" "
                      "ou \"legenda: queimada, revisada\" (stories-o-que-evitar.md, item 8)")
    return avisos


def roteiro_ao_lado(mp4: Path) -> Path | None:
    """O roteiro.md da sequência: na pasta do MP4 ou uma acima (o images/ da sequência)."""
    for pasta in (Path(mp4).resolve().parent, Path(mp4).resolve().parent.parent):
        if (pasta / "roteiro.md").is_file():
            return pasta / "roteiro.md"
    return None


def conferir(mp4: Path, saida_folha: Path | None = None,
             roteiro: Path | None = None) -> tuple[list[str], list[str], list[str]]:
    """(problemas que barram, avisos, leituras): os limites do Story e, como leitura, a linha do movimento e o caminho
    da folha de quadros (ou por que não saiu; a leitura nunca barra). Os avisos do roteiro (o dado ou o achado ao lado
    do MP4) vêm depois dos do vídeo; o primeiro aviso segue sendo o resumo do ffprobe."""
    probs, avisos = limites(mp4)
    roteiro = roteiro or roteiro_ao_lado(mp4)
    if roteiro:
        avisos = (avisos or ["(sem o resumo do ffprobe)"]) + conferir_roteiro(roteiro)
    leituras = [f"movimento: {movimento(mp4)}"]
    try:
        f = folha(Path(mp4), saida_folha or Path(mp4).with_name(Path(mp4).stem + "-folha.jpg"))
        leituras.append(f"folha de quadros (0, 30, 60 e 90%): {f}")
    except Exception as e:  # noqa: BLE001 - a folha é leitura
        leituras.append(f"folha de quadros não saiu ({type(e).__name__}: {e})")
    return probs, avisos, leituras


def imprimir(mp4: Path, probs: list[str], avisos: list[str], leituras: list[str]) -> None:
    """O relatório, no formato do tela_em_video.py: o resumo do ffprobe, os AVISOs, as leituras e os ERROs."""
    print(f"[..] {Path(mp4).name}: {avisos[0] if avisos else '(sem o resumo do ffprobe)'}")
    for x in avisos[1:]:
        print(f"[AVISO] {x}")
    for x in leituras:
        print(f"[leitura] {x}")
    for x in probs:
        print(f"[ERRO] {x}")
    print("[OK] dentro dos limites do Story na API" if not probs else "[ERRO] fora dos limites do Story na API: não sobe")


def main(args: list[str]) -> int:
    saida = roteiro = None
    for opcao in ("--folha", "--roteiro"):
        if opcao in args:
            k = args.index(opcao)
            if k + 1 >= len(args) or args[k + 1].startswith("--"):
                print(__doc__, file=sys.stderr)
                return 2
            valor = Path(args[k + 1])
            args = args[:k] + args[k + 2:]
            if opcao == "--folha":
                saida = valor
            else:
                roteiro = valor
    if roteiro is not None and not roteiro.is_file():
        print(f"[ERRO] não encontrei {roteiro}", file=sys.stderr)
        return 2
    if roteiro is not None and not args:
        avisos = conferir_roteiro(roteiro)
        for x in avisos:
            print(f"[AVISO] {x}")
        print(f"[OK] {roteiro}: " + ("nenhum aviso" if not avisos else f"{len(avisos)} aviso(s)"))
        return 0
    if len(args) != 1 or args[0].startswith("--"):
        print(__doc__, file=sys.stderr)
        return 2
    mp4 = Path(args[0])
    if not mp4.is_file():
        print(f"[ERRO] não encontrei {mp4}", file=sys.stderr)
        return 2
    probs, avisos, leituras = conferir(mp4, saida, roteiro)
    imprimir(mp4, probs, avisos, leituras)
    return 1 if probs else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
