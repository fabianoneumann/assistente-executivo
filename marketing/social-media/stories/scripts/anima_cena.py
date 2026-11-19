"""Grava em MP4 uma cena animada por código: a página define window.quadro(t), com t em segundos, e este script a
chama quadro a quadro, fotografa o seletor e monta o vídeo com o ffmpeg do pacote imageio_ffmpeg. A cena determina tudo
pelo t, então o vídeo sai igual a cada gravação (não depende do relógio do navegador).

  python anima_cena.py <pagina.html> <saida.mp4> [--segundos 6 --fps 30 --seletor "#stage" --largura 1080 --altura 1920] [--slide N]

--slide N grava a tela N de uma sequência (o stories.html da peça), ativando-a como a exportação faz.

A página abre pelo arquivo (file://), com o caderno da série pelo caminho relativo.
Render com --disable-lcd-text (sem a flag, o texto miúdo sai com franja de cor). Os quadros ficam numa pasta ao lado do vídeo, que pode ser apagada depois;
no começo de cada gravação, os quadros dela (q0000.png...) saem, e o resto da pasta fica.
O MP4 sai sem lista de edição (elst), que a Meta pede sem (-bf 0 -use_editlist 0, como o tela_em_video.py da
slides-export), e o script confere depois de gravar, com a mesma função de lá; com elst, o MP4 sai da pasta.
Depois, o video_do_story.py ao lado confere o MP4 inteiro contra os limites do Story na API (3 a 60 s, 23 a 60 qps,
H.264 ou HEVC, o moov no começo, a taxa, a proporção do Story) e, como leitura, mede o movimento (o saltos.py) e grava
a folha de quadros a 0, 30, 60 e 90% na pasta dos quadros (folha.jpg); fora dos limites, o MP4 fica (pode ser um
trecho a emendar) e o script sai com 1. Com o roteiro.md ao lado da página, o video_do_story.py confere também o
tempo de leitura frase a frase da tabela de tempo e a legenda revisada do vídeo com voz, como AVISO.
"""
import argparse, re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))   # o video_do_story.py, ao lado
from playwright.sync_api import sync_playwright

SLIDES_EXPORT = Path(__file__).resolve().parents[4] / ".claude" / "skills" / "slides-export" / "scripts"
QUADRO = re.compile(r"q\d{4,}\.png")  # o nome que o script dá aos quadros (q0000.png...), o mesmo que o FFmpeg lê


def listas_de_edicao(f):
    """Quantos elst o MP4 tem, pela mesma função da tela em vídeo do carrossel (tela_em_video.py da slides-export)."""
    if str(SLIDES_EXPORT) not in sys.path:
        sys.path.insert(0, str(SLIDES_EXPORT))
    from tela_em_video import _listas_de_edicao
    return _listas_de_edicao(Path(f))


def problema_elst(f):
    """O erro do MP4 com lista de edição (elst), ou None quando sai sem."""
    n = listas_de_edicao(f)
    return f"{f}: {n} lista(s) de edição (elst); a Meta pede MP4 sem (gravar com -bf 0 -use_editlist 0)" if n else None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("pagina"); p.add_argument("saida")
    p.add_argument("--segundos", type=float, default=6); p.add_argument("--fps", type=int, default=30)
    p.add_argument("--seletor", default="#stage")
    p.add_argument("--largura", type=int, default=1080); p.add_argument("--altura", type=int, default=1920)
    p.add_argument("--slide", type=int, help="a tela da sequência (1 é a primeira), ativada como na exportação")
    a = p.parse_args()
    saida = Path(a.saida).resolve()
    quadros = saida.with_suffix("").parent / (saida.stem + "-quadros"); quadros.mkdir(parents=True, exist_ok=True)
    # os quadros de uma gravação anterior saem: uma mais curta na mesma saída levaria os velhos ao MP4 (só os do script)
    for q in quadros.glob("q*.png"):
        if QUADRO.fullmatch(q.name):
            q.unlink()
    n = round(a.segundos * a.fps)  # o int truncava: 1.16 * 25 é 28,999..., e saíam 28 quadros em vez de 29
    with sync_playwright() as pw:
        b = pw.chromium.launch(args=["--disable-lcd-text"])
        pg = b.new_page(viewport={"width": a.largura, "height": a.altura}, device_scale_factor=1)
        erros = []
        pg.on("pageerror", lambda e: erros.append(str(e)))
        pg.goto(Path(a.pagina).resolve().as_uri())
        pg.wait_for_function("document.fonts.status === 'loaded' && typeof window.quadro === 'function'")
        pg.wait_for_timeout(600)
        if a.slide:
            pg.evaluate("""async n => { const s = [...document.querySelectorAll('.slide')]; s.forEach((x, i) => x.classList.toggle('active', i === n - 1));
              const st = document.getElementById('stage'); if (st) st.style.transform = 'none';
              if (window.prepararSlide) await window.prepararSlide(n - 1); }""", a.slide)
            pg.wait_for_timeout(300)
        el = pg.query_selector(a.seletor)
        if el is None:
            b.close()
            sys.exit(f"o seletor {a.seletor!r} não está na página (--seletor; o padrão é #stage)")
        for i in range(n):
            pg.evaluate("t => window.quadro(t)", i / a.fps)
            el.screenshot(path=str(quadros / f"q{i:04d}.png"))
        b.close()
    if erros:
        sys.exit("erro na página: " + "; ".join(erros))
    import imageio_ffmpeg
    r = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", str(quadros / "q%04d.png"),
                        "-vf", "format=yuv420p", "-c:v", "libx264", "-crf", "18", "-bf", "0", "-use_editlist", "0", "-movflags", "+faststart", str(saida)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.stderr)
    prob = problema_elst(saida)
    if prob:
        saida.unlink()  # o MP4 com elst não fica onde a publicação o pegaria
        sys.exit(prob)
    print(f"[OK] {n} quadros, {a.segundos:g} s, {saida}")
    import video_do_story as vs
    roteiro = Path(a.pagina).resolve().parent / "roteiro.md"   # o da sequência, ao lado do stories.html
    probs, avisos, leituras = vs.conferir(saida, quadros / "folha.jpg", roteiro if roteiro.is_file() else None)
    vs.imprimir(saida, probs, avisos, leituras)
    if probs:
        sys.exit(1)


if __name__ == "__main__":
    main()
