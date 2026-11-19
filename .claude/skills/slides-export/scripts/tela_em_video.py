#!/usr/bin/env python3
"""Tela em video dentro do carrossel: grava em MP4 a tela com data-video do slides.html e confere o MP4 contra os
limites da API de publicacao do Instagram. Usado pelo export_slides.py; roda sozinho para conferir um MP4:

  python tela_em_video.py conferir <arquivo.mp4> [--story]

Com --story, os limites sao os do video de Story (a mesma pagina da Meta): a proporcao de 0,1:1 a 10:1, com AVISO fora do
9:16 recomendado, a largura ate 1920 e sem o aviso dos 5 a 8 s da tela; o resto (moov, elst, codec, 4:2:0, 23 a 60 qps,
3 a 60 s, 25 Mbps, 100 MB, audio) e o mesmo. Quem chama no caminho dos Stories e o video_do_story.py, em
marketing/social-media/stories/scripts/ (o anima_cena.py depois de gravar, o publicar_stories.py antes de subir).

O contrato da pagina:
- a tela em video leva data-video="<segundos>" na <section class="slide"> (3 a 60 s aceitos; 5 a 8, a duracao recomendada);
- a pagina define window.quadro(t, idx), t em segundos e idx a tela a partir de 0, que poe a tela no estado do instante t;
  pode mexer no estilo, no atributo ou no currentTime de uma animacao pausada, mas nada pode correr sozinho (animacao ou
  transicao em andamento para a gravacao com erro);
- o estado parado da tela, sem chamar quadro, e o quadro final, completo: e o que as conferencias medem. Os quadros vao
  de t = 0 a t = (n - 1) / fps, entao a animacao acaba antes do fim e o fim fica parado;
- a tela em laco (o ultimo quadro igual ao primeiro, para o video emendar no carrossel) e
  a excecao: o estado parado, sem chamar quadro, e o instante que a pagina escolhe (a maquina com a palavra batida), e
  nao o fim, que volta ao comeco. As conferencias e o --sem-video seguem medindo o estado sem quadro, entao nada muda
  nelas; muda so o aviso de "animacao parada", que compara todos os quadros e nao so o primeiro e o ultimo.

A gravacao usa o mesmo Chromium do shot-scraper, a mesma janela, a mesma preparacao da tela (o JS que o export_slides.py
passa, uma fonte so) e a mesma flag (--disable-lcd-text) da exportacao em JPEG, e fotografa o mesmo #stage: o video
sai com o papel, as fontes e a moldura das telas estaticas. Cada quadro sai do t, sem o relogio do navegador, entao o
video sai igual a cada gravacao. A conferencia do MP4 pede o ffprobe no PATH; sem ele, o MP4 nao sobe.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fontes import CARREGAR_FONTES  # noqa: E402

# Limites (referencia IG User Media da Meta; confira antes de mudar): a pagina nao tem secao para o video de carrossel; valem os do
# Story e do Reel no que coincidem (MP4 com moov no comeco, H.264/HEVC, 4:2:0, 23 a 60 qps, AAC ate 48 kHz, ate 25 Mbps),
# o mais estreito dos dois na duracao e no tamanho (3 a 60 s, 100 MB) e, na proporcao e na largura, os das imagens,
# porque o carrossel corta todos os itens pela proporcao do primeiro.
MIN_S, MAX_S = 3.0, 60.0
REC_MIN_S, REC_MAX_S = 5.0, 8.0          # a duracao recomendada da tela em video (fora dela, aviso)
MAX_BYTES = 100 * 1024 * 1024
MIN_W, MAX_W = 320, 1440
MIN_RATIO, MAX_RATIO = 0.8, 1.91
MIN_FPS, MAX_FPS = 23, 60
MAX_BITRATE = 25_000_000
CODECS = ("h264", "hevc")
# O video de Story (a mesma referencia IG User Media, lida em 2026-11-13; knowledge/sources/2026-11-13-meta-ig-user-media-
# reference.md, "Video: as duas especificacoes"): proporcao de 0,1:1 a 10:1, recomendado 9:16, largura ate 1920 px; a
# duracao (3 a 60 s), o tamanho (100 MB), os quadros, o codec, o croma, a taxa e o audio sao os de cima. A proporcao do
# carrossel (4:5 a 1,91:1) nao vale aqui: reprovaria todo 9:16 (passada de enriquecimento dos Stories, 2026-11-19, F3)
STORY_MIN_RATIO, STORY_MAX_RATIO, STORY_MAX_W = 0.1, 10.0, 1920
STORY_RATIO = 9 / 16

QUADRO = """([t, idx]) => { window.quadro(t, idx);
  return document.getAnimations().filter(a => a.playState === 'running').length; }"""


def ffmpeg() -> str:
    """O FFmpeg do PATH (o completo, com o ffprobe); sem ele, o do imageio_ffmpeg."""
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def gravar(post: Path, html: str, idx: int, segundos: float, saida: Path, preparar_js: str, janela=(1280, 1560),
           seletor="#stage", fps: int = 30, som_mudo: bool = False) -> dict:
    """Grava a tela idx (a partir de 0) em MP4. preparar_js e a expressao JS que prepara a tela (a mesma da foto do
    JPEG, vinda do export_slides.py). Devolve {'quadros': n, 'parada': bool, 'faltam': [...]} (parada: o primeiro e o
    ultimo quadro saem iguais e nenhum quadro do meio difere, a animacao nao andou; laco: o primeiro e o ultimo saem
    iguais, mas o meio anda, a tela emenda; faltam: as fontes que nao carregaram, pelo fontes.py, e o video
    saiu na fonte de reserva: quem chama da o ERRO, como na tela em JPEG, e nao sobe)."""
    from playwright.sync_api import sync_playwright
    n = max(1, round(segundos * fps))
    with tempfile.TemporaryDirectory(prefix="tela-video-") as tmp:
        tmp = Path(tmp)
        erros: list[str] = []
        with sync_playwright() as pw:
            br = pw.chromium.launch(args=["--disable-lcd-text"])
            try:
                page = br.new_page(viewport={"width": janela[0], "height": janela[1]}, device_scale_factor=1)
                page.on("pageerror", lambda e: erros.append(str(e)))
                page.goto((post / html).resolve().as_uri())
                page.wait_for_load_state("load")
                page.evaluate(preparar_js)
                # a fonte da tela, conferida pelo fontes.py (o preparar_js do export_slides.py ja a pede): o
                # document.fonts.status passava antes de a fonte ser pedida, e a familia nao declarada (o @import sem
                # rede) nao aparece nele. A que falta volta a quem chama, e a gravacao
                # segue na fonte de reserva: no export de revisao, a tela em video sai com o ERRO, como a tela em JPEG,
                # e o --upload nao sobe
                faltam = page.evaluate("async (idx) => { const carregarFontes = " + CARREGAR_FONTES + ";"
                                       " return await carregarFontes(document.querySelectorAll('.slide')[idx]); }", idx)
                if not page.evaluate("typeof window.quadro === 'function'"):
                    raise RuntimeError(f"a tela {idx + 1} tem data-video, mas a pagina nao define window.quadro(t, idx)")
                el = page.query_selector(seletor)
                if el is None:
                    raise RuntimeError(f"seletor {seletor} nao encontrado")
                # o libx264 em 4:2:0 recusa lado impar, e so depois de fotografar tudo: caixa impar e defeito da pagina
                # (o JPEG sairia impar tambem), entao para antes, sem reamostrar (o scale borraria o traco)
                bb = el.bounding_box() or {}
                lados = (round(bb.get("width", 0)), round(bb.get("height", 0)))
                if any(x % 2 for x in lados):
                    raise RuntimeError(f"a caixa {seletor} tem {lados[0]} x {lados[1]} px: o H.264 em 4:2:0 pede lados pares")
                for i in range(n):
                    correndo = page.evaluate(QUADRO, [i / fps, idx])
                    if correndo:
                        # o relogio do navegador mexeria na foto: o video sairia diferente a cada gravacao
                        raise RuntimeError(f"{correndo} animacao(oes) ou transicao(oes) correndo sozinhas em t = {i / fps:.2f} s: "
                                           "o window.quadro tem de posicionar tudo pelo t (pausar a animacao e usar o currentTime)")
                    # animations="allow": o "disabled" levaria ao fim a animacao pausada que o quadro posicionou
                    el.screenshot(path=str(tmp / f"q{i:04d}.png"), animations="allow")
                    if i % fps == 0:
                        print(f"      tela {idx + 1}: quadro {i + 1}/{n}", flush=True)
            finally:
                br.close()
        if erros:
            raise RuntimeError("erro na pagina durante a gravacao: " + "; ".join(erros))
        # todos os quadros, e nao so o primeiro e o ultimo: na tela em laco eles saem iguais de proposito, e o aviso de
        # "animacao parada" seria falso
        hashes = [hashlib.md5((tmp / f"q{k:04d}.png").read_bytes()).hexdigest() for k in range(n)]
        primeiro, ultimo = hashes[0], hashes[-1]
        parada = len(set(hashes)) == 1
        cmd = [ffmpeg(), "-y", "-loglevel", "error", "-framerate", str(fps), "-i", str(tmp / "q%04d.png")]
        if som_mudo:
            cmd += ["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000"]
        # H.264 high, 4:2:0, GOP fechado de 1 s, moov no comeco (+faststart); teto de taxa abaixo dos 25 Mbps da Meta.
        # Sem lista de edicao, que a Meta pede ("no edit lists"): com quadros B, o libx264 grava um elst (o atraso dos
        # quadros B); -bf 0 -use_editlist 0 tira o elst e o video comeca em 0 (conferido na revisao, 2% maior)
        cmd += ["-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high",
                "-r", str(fps), "-g", str(fps), "-keyint_min", str(fps), "-sc_threshold", "0", "-flags", "+cgop",
                "-bf", "0", "-maxrate", "20M", "-bufsize", "40M", "-use_editlist", "0", "-movflags", "+faststart"]
        cmd += ["-c:a", "aac", "-b:a", "128k", "-shortest"] if som_mudo else ["-an"]
        saida.parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(cmd + [str(saida)], capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode:
            raise RuntimeError(f"ffmpeg terminou com codigo {r.returncode}: {r.stderr.strip()[-400:]}")
    return {"quadros": n, "parada": parada, "laco": primeiro == ultimo and not parada, "faltam": faltam}


def _atomos(f: Path) -> list[str]:
    """Os atomos de primeiro nivel do MP4, na ordem (para conferir o moov antes do mdat)."""
    nomes = []
    with f.open("rb") as h:
        tam_total = f.stat().st_size
        pos = 0
        while pos < tam_total and len(nomes) < 50:
            h.seek(pos)
            cab = h.read(16)
            if len(cab) < 8:
                break
            tam = int.from_bytes(cab[:4], "big")
            nome = cab[4:8].decode("latin-1")
            if tam == 1:
                tam = int.from_bytes(cab[8:16], "big")
            elif tam == 0:
                tam = tam_total - pos
            if tam < 8:
                break
            nomes.append(nome)
            pos += tam
    return nomes


def _listas_de_edicao(f: Path) -> int:
    """Quantos atomos elst ha em moov/trak/edts (a Meta pede MP4 "no edit lists"). Le o arquivo inteiro: o MP4 da
    tela tem poucos MB."""
    b = f.read_bytes()
    achados = 0

    def andar(ini: int, fim: int) -> None:
        nonlocal achados
        pos = ini
        while pos + 8 <= fim:
            tam = int.from_bytes(b[pos:pos + 4], "big")
            nome = b[pos + 4:pos + 8].decode("latin-1")
            cab = 8
            if tam == 1:
                tam, cab = int.from_bytes(b[pos + 8:pos + 16], "big"), 16
            elif tam == 0:
                tam = fim - pos
            if tam < 8:
                return
            if nome == "elst":
                achados += 1
            elif nome in ("moov", "trak", "edts"):
                andar(pos + cab, min(pos + tam, fim))
            pos += tam

    andar(0, len(b))
    return achados


def conferir(f: Path, perfil: str = "carrossel") -> tuple[list[str], list[str]]:
    """Confere o MP4 contra os limites; devolve (problemas que barram o upload, avisos). perfil "carrossel" (a tela em
    video) ou "story" (o video de Story, com a proporcao e a largura dele, sem o aviso dos 5 a 8 s)."""
    if perfil not in ("carrossel", "story"):
        raise ValueError(f"perfil {perfil!r}: carrossel ou story")
    story = perfil == "story"
    probs, avisos = [], []
    size = f.stat().st_size
    if size > MAX_BYTES:
        probs.append(f"{size / 1024 / 1024:.1f} MB, acima de 100 MB")
    atomos = _atomos(f)
    if "moov" not in atomos or ("mdat" in atomos and atomos.index("moov") > atomos.index("mdat")):
        probs.append(f"o moov nao esta antes do mdat (atomos {atomos[:6]}): gravar com -movflags +faststart")
    if "ftyp" not in atomos[:1]:
        probs.append("nao comeca com ftyp: nao e MP4")
    elst = _listas_de_edicao(f)
    if elst:
        probs.append(f"{elst} lista(s) de edicao (elst): a Meta pede MP4 sem; gravar com -bf 0 -use_editlist 0")
    probe = shutil.which("ffprobe")
    if not probe:
        return probs + ["ffprobe ausente: codec, quadros e duracao nao conferidos"], avisos
    r = subprocess.run([probe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(f)],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        return probs + [f"ffprobe nao leu o arquivo: {r.stderr.strip()[-200:]}"], avisos
    info = json.loads(r.stdout)
    vs = [s for s in info.get("streams", []) if s.get("codec_type") == "video"]
    aus = [s for s in info.get("streams", []) if s.get("codec_type") == "audio"]
    if len(vs) != 1:
        return probs + [f"{len(vs)} faixas de video, esperada 1"], avisos
    v = vs[0]
    if v.get("codec_name") not in CODECS:
        probs.append(f"codec {v.get('codec_name')}, esperado H.264 ou HEVC")
    if v.get("pix_fmt") not in ("yuv420p", "yuvj420p"):
        probs.append(f"croma {v.get('pix_fmt')}, esperado 4:2:0 (yuv420p)")
    if v.get("field_order") not in (None, "progressive", "unknown"):
        probs.append(f"varredura {v.get('field_order')}, esperada progressiva")
    w, h = int(v.get("width", 0)), int(v.get("height", 1))
    ratio = w / h if h else 0
    if story:
        if not (0 < w <= STORY_MAX_W):
            probs.append(f"largura {w}px acima de {STORY_MAX_W} (Story)")
        if not (STORY_MIN_RATIO <= ratio <= STORY_MAX_RATIO):
            probs.append(f"proporcao {ratio:.3f} fora de 0,1:1..10:1 (Story)")
        elif abs(ratio - STORY_RATIO) > 0.01:
            avisos.append(f"proporcao {ratio:.3f}, fora do 9:16 recomendado para o Story")
    else:
        if not (MIN_W <= w <= MAX_W):
            probs.append(f"largura {w}px fora de {MIN_W}..{MAX_W}")
        if not (MIN_RATIO - 0.005 <= ratio <= MAX_RATIO + 0.005):
            probs.append(f"proporcao {ratio:.3f} fora de 4:5..1.91:1")
    num, _, den = (v.get("avg_frame_rate") or "0/1").partition("/")
    fps = float(num) / float(den or 1) if float(den or 1) else 0
    if not (MIN_FPS <= fps <= MAX_FPS):
        probs.append(f"{fps:.2f} qps fora de {MIN_FPS}..{MAX_FPS}")
    dur = float(info.get("format", {}).get("duration") or v.get("duration") or 0)
    if not (MIN_S <= dur <= MAX_S):
        probs.append(f"{dur:.2f} s fora de {MIN_S:g}..{MAX_S:g} s")
    elif not story and not (REC_MIN_S <= dur <= REC_MAX_S):
        avisos.append(f"{dur:.2f} s, fora dos 5 a 8 s pedidos para a tela")
    br = int(info.get("format", {}).get("bit_rate") or 0)
    if br > MAX_BITRATE:
        probs.append(f"{br / 1e6:.1f} Mbps, acima de 25 Mbps")
    for a in aus:
        if a.get("codec_name") != "aac" or int(a.get("sample_rate", 0)) > 48000:
            probs.append(f"audio {a.get('codec_name')} {a.get('sample_rate')} Hz, esperado AAC ate 48 kHz")
    resumo = f"{w}x{h}, {v.get('codec_name')}, {fps:g} qps, {dur:.2f} s, {('com audio' if story else 'com audio mudo') if aus else 'sem audio'}"
    avisos.insert(0, resumo)
    return probs, avisos


def main() -> None:
    args = sys.argv[1:]
    story = "--story" in args
    args = [a for a in args if a != "--story"]
    if len(args) != 2 or args[0] != "conferir":
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    f = Path(args[1])
    if not f.is_file():
        print(f"[ERRO] nao encontrei {f}", file=sys.stderr)
        sys.exit(2)
    probs, avisos = conferir(f, "story" if story else "carrossel")
    print(f"[..] {f.name}: {avisos[0] if avisos else ''}")
    for x in avisos[1:]:
        print(f"[AVISO] {x}")
    for x in probs:
        print(f"[ERRO] {x}")
    print("[OK] dentro dos limites da API" if not probs else "[ERRO] fora dos limites da API")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
