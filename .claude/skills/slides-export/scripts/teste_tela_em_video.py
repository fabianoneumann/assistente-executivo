"""Testa a tela em vídeo sem a peça real: páginas mínimas num diretório temporário, sem o bucket nem a API. A gravação
e a leitura (casos 1 a 8), a exportação de uma peça mínima (9 a 11: o --sem-video, a limpeza do formato velho e o PNG
de revisão fora do registro), a fonte que não carregou (12, o fontes.py na gravação, e 15, o export de revisão que
segue com o ERRO) e o saltos.py da object-anatomy (13 e 14: o movimento contínuo sem pico, a troca súbita com pico e o
fim parado; pulados, com aviso, quando a object-anatomy não está no projeto). Sem rede, sem bucket e sem chave.

  python -X utf8 teste_tela_em_video.py          (de qualquer pasta; sai com erro no primeiro caso que falhar)

Precisa do shot-scraper, do Playwright com o Chromium e do FFmpeg com ffprobe; leva cerca de 40 s.
"""
import hashlib
import importlib.util
import pathlib
import subprocess
import tempfile

AQUI = pathlib.Path(__file__).resolve().parent


def carregar(nome, pasta=AQUI):
    spec = importlib.util.spec_from_file_location(nome, pasta / f"{nome}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


tv, ex = carregar("tela_em_video"), carregar("export_slides")

# a tela 2 tem uma bola que anda de x = 100 a x = 900; o jeito de mover muda por variante
PAGINA = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#fff}} #stage{{position:relative;width:{w}px;height:{h}px}}
.slide{{display:none;position:absolute;inset:0}} .slide.active{{display:block}}
.bola{{position:absolute;left:0;top:300px;width:80px;height:80px;border-radius:50%;background:#1b3a8c}}
{css}</style></head><body><div id="stage">
<section class="slide active"><p>1</p></section>
<section class="slide" data-video="3"><div class="bola" id="bola"></div></section>
</div><script>{js}</script></body></html>"""

VARIANTES = {
    # o quadro posiciona pelo estilo
    "estilo": ("", "window.quadro = (t, i) => { if (i === 1) document.getElementById('bola').style.transform = `translateX(${100 + 800 * t / 3}px)`; };"),
    # o quadro posiciona uma animação pausada pelo currentTime (o caso que o animations="disabled" congelava)
    "waapi": ("", "let a; window.quadro = (t, i) => { if (i !== 1) return; if (!a) { a = document.getElementById('bola').animate("
              "[{transform:'translateX(100px)'},{transform:'translateX(900px)'}], {duration:3000, fill:'both'}); a.pause(); } a.currentTime = t * 1000; };"),
    # uma animação CSS correndo sozinha: o relógio do navegador entraria na foto
    "correndo": (".bola{animation:gira 2s linear infinite} @keyframes gira{to{transform:rotate(360deg)}}",
                 "window.quadro = (t, i) => {};"),
    # o texto da tela numa família que nenhuma regra declara (o @import da fonte da web sem rede)
    "fonte": (".bola::after{content:'texto';font-family:'Fonte Que Nao Veio',monospace}",
              "window.quadro = (t, i) => { if (i === 1) document.getElementById('bola').style.transform = `translateX(${100 + 800 * t / 3}px)`; };"),
    # a bola anda devagar, salta 400 px em 1,5 s e para em 2,5 s: o salto e o fim parado que o saltos.py mede
    "salto": ("", "window.quadro = (t, i) => { if (i !== 1) return; const u = Math.min(t, 2.5);"
                  " document.getElementById('bola').style.transform = `translateX(${100 + 120 * u + (t >= 1.5 ? 400 : 0)}px)`; };"),
    # a tela em laço: a bola vai e volta ao lugar de partida antes do fim (o último quadro igual ao primeiro, 18/11)
    "laco": ("", "window.quadro = (t, i) => { if (i !== 1) return; const u = Math.min(t, 2.5);"
                 " document.getElementById('bola').style.transform = `translateX(${100 + 800 * Math.sin(Math.PI * u / 2.5)}px)`; };"),
}


def caso(nome, cond, extra=""):
    print(("ok    " if cond else "FALHA ") + nome)
    if not cond and extra != "":
        print("   ", extra)
    assert cond, nome


def grava(pasta, nome, w=1080, h=1350):
    css, js = VARIANTES.get(nome, VARIANTES["estilo"])
    (pasta / f"{nome}.html").write_text(PAGINA.format(w=w, h=h, css=css, js=js), encoding="utf-8")
    out = pasta / f"{nome}.mp4"
    try:
        g = tv.gravar(pasta, f"{nome}.html", 1, 3.0, out, ex.JS.format(idx=1, previa="").strip(), fps=24)
    except RuntimeError as e:
        return str(e), None
    d = pathlib.Path(tempfile.mkdtemp())
    subprocess.run([tv.ffmpeg(), "-loglevel", "error", "-i", str(out), str(d / "f%03d.png")], check=True)
    hs = [hashlib.md5(p.read_bytes()).hexdigest() for p in sorted(d.glob("*.png"))]
    return g, (hs, tv.conferir(out))


with tempfile.TemporaryDirectory() as tmp:
    pasta = pathlib.Path(tmp)
    g, (hs, (probs, avisos)) = grava(pasta, "estilo")
    caso("1. pelo estilo: 72 quadros, todos diferentes, MP4 dentro dos limites", len(hs) == 72 and len(set(hs)) == 72 and not probs)
    caso("2. o MP4 sai sem lista de edição (elst)", tv._listas_de_edicao(pasta / "estilo.mp4") == 0)
    g, (hs, _) = grava(pasta, "waapi")
    caso("3. animação pausada pelo currentTime anda (não congela no fim)", not g["parada"] and len(set(hs)) > 60)
    erro, _ = grava(pasta, "correndo")
    caso("4. animação correndo sozinha para a gravação", isinstance(erro, str) and "correndo sozinhas" in erro)
    erro, _ = grava(pasta, "impar", w=1081, h=1351)
    caso("5. caixa de lado ímpar para antes de fotografar", isinstance(erro, str) and "lados pares" in erro)
    caso("6. avisa fora de 5 a 8 s (a duração recomendada)", any("fora dos 5 a 8 s" in x for x in avisos))
    g, _ = grava(pasta, "fonte")
    caso("12. a fonte que não carregou volta da gravação (fontes.py), sem matar o vídeo de revisão",
         isinstance(g, dict) and [f["familia"] for f in g.get("faltam", [])] == ["Fonte Que Nao Veio"]
         and (pasta / "fonte.mp4").is_file(), g)
    g, (hs, _) = grava(pasta, "laco")
    caso("16. tela em laço: o primeiro e o último quadro iguais não contam como animação parada",
         isinstance(g, dict) and not g["parada"] and g["laco"] and len(set(hs)) > 30, g)
    pasta_oa = AQUI.parents[1] / "object-anatomy" / "scripts"
    if (pasta_oa / "saltos.py").is_file():
        sl = carregar("saltos", pasta_oa)
        caso("13. saltos.py: o movimento contínuo não tem pico", not sl.medir(str(pasta / "estilo.mp4"))["picos"])
        grava(pasta, "salto")
        r = sl.medir(str(pasta / "salto.mp4"))
        caso("14. saltos.py: a troca súbita sai como pico, e o fim parado se conta",
             any(35 <= q <= 39 for q, _ in r["picos"]) and 8 <= r["parado_quadros"] <= 13)
    else:
        print("pulado 13 e 14: o saltos.py da object-anatomy não está no projeto")

for forma in ('data-video="6"', "data-video='6'", "data-video=6"):
    r = ex.telas_em_video(f"<section class=\"slide\"></section><section class='slide' {forma}></section>")
    caso(f"7. {forma} é lido como tela 2 de 6 s", r == {2: 6.0})
r = ex.telas_em_video('<section class="slide" data-video="6,5"></section>')
caso("8. vírgula decimal", r == {1: 6.5})

# a exportação de uma peça mínima (shot-scraper e gravação de verdade, sem conferências nem bucket)
import sys  # noqa: E402


def exporta(post, *args):
    return subprocess.run([sys.executable, str(AQUI / "export_slides.py"), str(post), "--sem-conferir", *args],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


with tempfile.TemporaryDirectory() as tmp:
    post = pathlib.Path(tmp) / "peca"
    (post / "images").mkdir(parents=True)
    css, js = VARIANTES["estilo"]
    (post / "slides.html").write_text(PAGINA.format(w=1080, h=1350, css=css, js=js), encoding="utf-8")
    leg = post / "legenda.md"
    leg.write_text("# Legenda — teste\n\n**Imagens:** antes\n\n## Legenda (final)\n\nx\n", encoding="utf-8")
    (post / "images" / "slide-02.mp4").write_bytes(b"o video de antes")
    antes = leg.read_bytes()
    r = exporta(post, "--sem-video")
    caso("9. --sem-video: a tela 2 sai em JPEG, e o MP4 de antes e a legenda.md ficam como estavam",
         r.returncode == 0 and (post / "images" / "slide-02.jpg").is_file()
         and (post / "images" / "slide-02.mp4").read_bytes() == b"o video de antes" and leg.read_bytes() == antes)
    (post / "images" / "slide-01.png").write_bytes(b"png de revisao")
    r = exporta(post)
    imagens = sorted(p.name for p in (post / "images").iterdir())
    texto = leg.read_text(encoding="utf-8")
    caso("10. exportação que passa: o JPEG da tela que é vídeo sai, o MP4 novo fica",
         r.returncode == 0 and "slide-02.jpg" not in imagens and (post / "images" / "slide-02.mp4").stat().st_size > 1000)
    caso("11. o PNG de revisão fica na pasta, mas não no registro", "slide-01.png" in imagens
         and "slide-01.png" not in texto and "images/slide-01.jpg" in texto and "images/slide-02.mp4" in texto)

    # a tela em vídeo com a fonte faltando, no export de revisão: sai com o ERRO, como a tela em JPEG, sem matar o export
    sem_fonte = pathlib.Path(tmp) / "sem-fonte"
    (sem_fonte / "images").mkdir(parents=True)
    css, js = VARIANTES["fonte"]
    (sem_fonte / "slides.html").write_text(PAGINA.format(w=1080, h=1350, css=css, js=js), encoding="utf-8")
    r = exporta(sem_fonte)
    caso("15. export de revisão: a tela em vídeo sem a fonte sai com o ERRO fonte_nao_carregada, e o export segue",
         r.returncode == 0 and "[ERRO] tela 2 fonte_nao_carregada" in r.stdout
         and (sem_fonte / "images" / "slide-02.mp4").is_file(), (r.returncode, r.stdout[-600:], r.stderr[-600:]))
print("TODOS OK")
