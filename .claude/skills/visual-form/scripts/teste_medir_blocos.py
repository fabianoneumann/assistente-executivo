"""Testa o medir_blocos.py e a conferência de fonte dele (fontes.py) sem rede e sem peça real: páginas mínimas num
diretório temporário, com a fonte de teste servida pelo próprio sistema (`local()`), um arquivo que não existe, uma
família que nenhuma regra declara (o caso do `@import` da fonte da web que não veio) e um servidor local que aceita o
pedido da fonte e nunca responde (a rede travada). O erro que ele impede: a medida que roda na fonte de
reserva sem avisar.

  python -X utf8 teste_medir_blocos.py          (de qualquer pasta; sai com erro se algum caso falhar)

Precisa do shot-scraper com o Chromium e de uma destas fontes instaladas: Arial, Liberation Sans ou DejaVu Sans. Sem
nenhuma delas, o caso 1 acusa a fonte de teste, e o teste diz que a máquina não tem a fonte (não é falha do script).
"""
import http.server
import pathlib
import re
import subprocess
import sys
import tempfile
import threading
import time

AQUI = pathlib.Path(__file__).resolve().parent
LOCAL = 'local("Arial"),local("Liberation Sans"),local("DejaVu Sans")'


def pagina(faces, corpo, css="", script=""):
    """A página mínima: telas .slide (só a ativa aparece) com blocos de 40 px em linhas de 60 px, na família pedida."""
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
{faces}
body{{margin:0}} .slide{{display:none;position:relative;width:1080px;height:1350px}} .slide.active{{display:block}}
.bloco{{position:absolute;left:80px;width:600px;font-family:"Fonte Teste",monospace;font-size:40px;line-height:60px}}
{css}
</style></head><body>
{corpo}
{script}</body></html>"""


FACE = '@font-face{font-family:"Fonte Teste";src:' + LOCAL + '}'
# a tela 2 começa escondida (display:none), como as telas fora da ativa: o caso em que o fonts.ready não espera nada
DUAS_TELAS = ('<section class="slide active"><p class="bloco" data-base="300" style="top:200px">Uma linha de teste</p></section>\n'
              '<section class="slide"><p class="bloco" style="top:400px">Outra tela, escondida no começo</p></section>')
CASOS = [
    # (nome, html, código esperado, trecho esperado na saída)
    ("fonte carregada, tela escondida no começo", pagina(FACE, DUAS_TELAS), 0, "base"),
    ("arquivo da fonte não existe", pagina('@font-face{font-family:"Fonte Teste";src:url("nao-existe.woff2")}', DUAS_TELAS),
     3, "ERRO fonte_nao_carregada S1 Fonte Teste"),
    ("família que nenhuma regra declara (o @import que não veio)",
     pagina(FACE, DUAS_TELAS, css='.slide + .slide .bloco{font-family:"Fonte Da Web Que Nao Veio",monospace}'),
     3, "ERRO fonte_nao_carregada S2 Fonte Da Web Que Nao Veio"),
    # o 400 carrega e o 700 falha: o Chromium não engrossa o 400 no lugar do 700, mede na reserva, e a largura acusa
    ("o peso 700 declarado falhou e o 400 carregou",
     pagina(FACE + '\n@font-face{font-family:"Fonte Teste";font-weight:700;src:url("nao-existe-700.woff2")}',
            '<section class="slide active"><p class="bloco" style="top:200px;font-weight:700">Em negrito</p></section>'),
     3, "ERRO fonte_nao_carregada S1 Fonte Teste"),
    # o texto que o prepararSlide da peça põe na tela, depois da primeira conferência
    ("texto que o prepararSlide insere, numa família que não veio",
     pagina(FACE, '<section class="slide active"><p class="bloco" style="top:200px">Antes</p></section>',
            script='<script>window.prepararSlide = async i => { const p = document.createElement("p"); p.className = "bloco";'
                   ' p.style.cssText = "top:400px;font-family:\'Inserida Que Nao Veio\',monospace"; p.textContent = "Inserida";'
                   ' document.querySelectorAll(".slide")[i].appendChild(p); };</script>\n'),
     3, "ERRO fonte_nao_carregada S1 Inserida Que Nao Veio"),
    ("fonte usada só num ::before",
     pagina(FACE, '<section class="slide active"><ol class="bloco" style="top:200px"><li>Passo</li></ol></section>',
            css='li::before{content:counter(list-item) ".";font-family:"Pseudo Que Nao Veio",monospace}'),
     3, "ERRO fonte_nao_carregada S1 Pseudo Que Nao Veio"),
    ("bloco só com desenho, sem texto",
     pagina(FACE, '<section class="slide active"><div class="bloco" data-base="300" style="top:200px">'
                  '<svg width="10" height="10"></svg></div><p class="bloco" style="top:400px">Texto</p></section>'),
     0, "sem texto"),
    # o prepararSlide põe antes do texto outro na mesma família que não veio, noutro tamanho: um ERRO só, não dois
    ("a mesma fonte faltando antes e depois do prepararSlide",
     pagina(FACE, '<section class="slide active"><p class="bloco" style="top:400px;font-family:\'Dupla Que Nao Veio\',monospace">'
                  'Antes</p></section>',
            script='<script>window.prepararSlide = async i => { const p = document.createElement("p"); p.className = "bloco";'
                   ' p.style.cssText = "top:200px;font-size:60px;font-family:\'Dupla Que Nao Veio\',monospace"; p.textContent = "Posta";'
                   ' document.querySelectorAll(".slide")[i].prepend(p); };</script>\n'),
     3, "ERRO fonte_nao_carregada S1 Dupla Que Nao Veio"),
    # a pilha da fonte do sistema dos Stories ("-apple-system, 'Segoe UI', ..."): o apelido de outro aparelho não acusa,
    # a conta vai para a família seguinte (aqui, a de teste)
    ("pilha do sistema: -apple-system antes da fonte",
     pagina(FACE, '<section class="slide active"><p class="bloco" style="top:200px;font-family:-apple-system,'
                  'BlinkMacSystemFont,\'Fonte Teste\',sans-serif">Pilha</p></section>'),
     0, "base"),
]

# bloco sem data-base antes de um com data-base fora do alvo: o --ajustar mexe no bloco certo
AJUSTAR_CERTO = pagina(FACE, '<section class="slide active"><p class="bloco" style="top:100px">Sem alvo</p>'
                             '<p class="bloco" data-base="300" style="top:500px">Fora do alvo</p></section>')
# o atributo na outra ordem num bloco, e o mesmo data-base no seguinte: o --ajustar não mexe no bloco errado
AJUSTAR_ORDEM = pagina(FACE, '<section class="slide active"><p class="bloco" style="top:100px" data-base="300">Ordem trocada</p>'
                             '<p class="bloco" data-base="300" style="top:500px">Na ordem</p></section>')
# data-base que não é número antes de dois blocos com o mesmo alvo: cada um recebe o próprio ajuste
AJUSTAR_INVALIDO = pagina(FACE, '<section class="slide active"><p class="bloco" data-base="x" style="top:100px">Sem número</p>'
                                '<p class="bloco" data-base="300" style="top:500px">Primeiro</p>'
                                '<p class="bloco" data-base="300" style="top:900px">Segundo</p></section>')


class Mudo(http.server.BaseHTTPRequestHandler):
    """Aceita o pedido da fonte e não responde: a rede travada, não a ausente."""
    def do_GET(self):
        time.sleep(40)

    def log_message(self, *a):
        pass


def rodar(pasta, *extra, timeout=120):
    """Roda o medir_blocos.py; o prazo estourado vira falha do caso (código None), não derruba os outros."""
    try:
        r = subprocess.run([sys.executable, "-X", "utf8", str(AQUI / "medir_blocos.py"), str(pasta), "slides.html", *extra],
                           capture_output=True, text=True, encoding="utf-8", timeout=timeout)
    except subprocess.TimeoutExpired as e:
        return None, f"o medir_blocos.py não terminou em {timeout} s\n{e.stdout or ''}{e.stderr or ''}"
    return r.returncode, r.stdout + r.stderr


def sem_resposta(pasta, timeout=90):
    """Chama o carregarFontes do fontes.py na tela 2 e devolve as fontes que ele marcou como sem resposta."""
    sys.path.insert(0, str(AQUI.parents[1] / "slides-export" / "scripts"))   # fontes.py, da slides-export
    from fontes import CARREGAR_FONTES
    js = ("async () => { const carregarFontes = " + CARREGAR_FONTES + "; const s = document.querySelectorAll('.slide');"
          " s.forEach((x, j) => x.classList.toggle('active', j === 1)); await carregarFontes(s[1]);"
          " return [...(window.__fontesSemResposta || [])]; }")
    try:
        r = subprocess.run(["shot-scraper", "javascript", "slides.html", js], cwd=pasta, capture_output=True, text=True,
                           encoding="utf-8", timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, f"o shot-scraper não terminou em {timeout} s"
    return r.returncode, r.stdout + r.stderr


def caso(tmp, nome, html):
    pasta = pathlib.Path(tmp) / re.sub(r"\W+", "-", nome)[:40]
    pasta.mkdir()
    (pasta / "slides.html").write_bytes(html.encode("utf-8"))
    return pasta


def main():
    falhas = 0

    def conta(ok, n, nome, rc, saida):
        nonlocal falhas
        print(f"{'ok ' if ok else 'FALHOU'} caso {n}: {nome} (código {rc})")
        if not ok:
            print(saida)
            falhas += 1

    with tempfile.TemporaryDirectory() as tmp:
        for i, (nome, html, codigo, trecho) in enumerate(CASOS, 1):
            pasta = caso(tmp, nome, html)
            rc, saida = rodar(pasta)
            erros = [l.split(" (")[0] for l in saida.splitlines() if l.startswith("ERRO")]   # a mesma fonte na mesma tela, uma vez
            conta(rc == codigo and trecho in saida and len(erros) == len(set(erros)), i, nome, rc, saida)
            if i == 1 and rc == 3:
                print("  (nenhuma das fontes locais do teste, Arial, Liberation Sans ou DejaVu Sans, está instalada nesta "
                      "máquina: o caso 1 não vale aqui, e os outros também medem na reserva)")
        n = len(CASOS)

        # o --ajustar não mexe no HTML quando a fonte não carregou (o bloco da tela 1 está fora do alvo de propósito)
        pasta = caso(tmp, "ajustar-sem-fonte", CASOS[1][1])
        antes = (pasta / "slides.html").read_bytes()
        rc, saida = rodar(pasta, "--ajustar")
        conta(rc == 3 and (pasta / "slides.html").read_bytes() == antes and "ajustado" not in saida.replace("nada ajustado", ""),
              n + 1, "--ajustar com a fonte faltando não grava", rc, saida)

        pasta = caso(tmp, "ajustar-certo", AJUSTAR_CERTO)
        rc, saida = rodar(pasta, "--ajustar")
        depois = (pasta / "slides.html").read_text(encoding="utf-8")
        conta(rc == 0 and 'style="top:100px">Sem alvo' in depois and 'style="top:500px">Fora' not in depois,
              n + 2, "--ajustar com um bloco sem data-base antes mexe só no que tem alvo", rc, saida)

        pasta = caso(tmp, "ajustar-ordem", AJUSTAR_ORDEM)
        antes = (pasta / "slides.html").read_bytes()
        rc, saida = rodar(pasta, "--ajustar")
        conta(rc == 0 and (pasta / "slides.html").read_bytes() == antes and "AVISO S1" in saida,
              n + 3, "--ajustar com data-base antes do style não mexe no bloco seguinte de mesmo alvo", rc, saida)

        pasta = caso(tmp, "ajustar-invalido", AJUSTAR_INVALIDO)
        rc, saida = rodar(pasta, "--ajustar")
        rc2, saida2 = rodar(pasta)
        conta(rc == 0 and rc2 == 0 and saida2.count(" ok |") == 2 and 'style="top:100px">Sem número' in
              (pasta / "slides.html").read_text(encoding="utf-8"),
              n + 4, "--ajustar com um data-base que não é número antes acerta os dois blocos de mesmo alvo", rc2, saida + saida2)

        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Mudo)
        srv.daemon_threads = True
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        url = f"http://127.0.0.1:{srv.server_address[1]}/fonte.woff2"
        # a fonte lenta é só da tela 2, escondida no carregamento: a página carrega, e quem a pede é a conferência
        lenta = '@font-face{font-family:"Fonte Lenta";src:url("' + url + '")}'
        pasta = caso(tmp, "rede-travada", pagina(FACE + "\n" + lenta, DUAS_TELAS,
                                                 css='.slide + .slide .bloco{font-family:"Fonte Lenta",monospace}'))
        t0 = time.monotonic()
        rc, saida = rodar(pasta, timeout=90)
        dt = time.monotonic() - t0
        conta(rc == 3 and "ERRO fonte_nao_carregada S2 Fonte Lenta" in saida and dt < 30, n + 5,
              f"a fonte que não responde vira fonte_nao_carregada, sem pendurar ({dt:.0f} s)", rc, saida)

        # a fonte que carregou no mesmo pedido da que não respondeu não entra na lista das sem resposta
        pasta = caso(tmp, "sem-resposta-so-a-lenta", pagina(
            FACE + "\n" + lenta,
            '<section class="slide active"><p class="bloco" style="top:200px">Tela 1</p></section>\n'
            '<section class="slide"><p class="bloco" style="top:200px">Carregou</p>'
            '<p class="bloco" style="top:400px;font-family:\'Fonte Lenta\',monospace">Lenta</p></section>'))
        rc, saida = sem_resposta(pasta)
        conta(rc == 0 and "Fonte Lenta" in saida and "Fonte Teste" not in saida, n + 6,
              "no prazo estourado, só a fonte sem resposta fica marcada", rc, saida)
        srv.shutdown()
    if falhas:
        sys.exit(1)
    print("todos os casos passaram")


if __name__ == "__main__":
    main()
