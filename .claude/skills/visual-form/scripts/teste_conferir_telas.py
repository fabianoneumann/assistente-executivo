"""O teste negativo do conferir_telas.py: para cada ERRO, um caso plantado que tem de reprovar, e uma peça limpa que
não pode ganhar ERRO; mais os AVISOs de forma com o positivo de cada um, a proteção tela a tela dos Stories pela API,
o nível do travessão pela voz de quem usa e as conferências da legenda. Sem rede e sem peça real: páginas mínimas num
diretório temporário, com a fonte de teste do próprio sistema (`local()`), e o post de exemplo da série de exemplo
para a tabela de papéis. Rodar a cada edição do conferir_telas.py ou do medidas_forma.py.

  python -X utf8 teste_conferir_telas.py          (de qualquer pasta; sai com erro se algum caso falhar)

Precisa do Playwright com o Chromium e de uma destas fontes instaladas: Arial, Liberation Sans ou DejaVu Sans. Leva
cerca de um minuto.
"""
import datetime
import importlib.util
import os
import pathlib
import sys
import tempfile

AQUI = pathlib.Path(__file__).resolve().parent


def carregar(nome, pasta=AQUI):
    spec = importlib.util.spec_from_file_location(nome, pasta / f"{nome}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


ct, ex = carregar("conferir_telas"), carregar("export_slides", AQUI.parents[1] / "slides-export" / "scripts")
mf = ct.mf
FALHAS = []
VOZ = mf.voz_pede_sem_travessao   # a original; o teste a troca para fixar o nível do travessão


def caso(nome, cond, extra=""):
    print(("ok    " if cond else "FALHOU ") + nome)
    if not cond:
        FALHAS.append(nome)
        if extra:
            print("   ", extra)


FACE = '@font-face{font-family:"Fonte Teste";src:local("Arial"),local("Liberation Sans"),local("DejaVu Sans")}'


def pagina(telas, w=1080, h=1350, css="", script=""):
    """Telas .slide num #stage, só a ativa aparece; papel branco e texto em caneta, na fonte de teste."""
    secoes = "\n".join(f'<section class="slide{" active" if k == 0 else ""}"{attr}>{corpo}</section>'
                       for k, (attr, corpo) in enumerate(telas))
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
{FACE}
body{{margin:0;background:#d9d9d9}} #stage{{position:relative;width:{w}px;height:{h}px}}
.slide{{display:none;position:absolute;inset:0;background:#fff;overflow:hidden;font-family:"Fonte Teste",monospace;color:#1B3A8C}}
.slide.active{{display:block}}
p,h2{{margin:0;position:absolute;left:126px;font-size:34px;line-height:48px;font-weight:400}}
h2{{font-size:72px;line-height:72px}}
{css}</style></head><body><div id="stage">
{secoes}
</div>{script}</body></html>"""


def conferir(tmp, nome, html, **kw):
    pasta = pathlib.Path(tmp) / nome
    pasta.mkdir()
    (pasta / "slides.html").write_bytes(html.encode("utf-8"))
    return ct.conferir(pasta, "slides.html", **kw)


def tem(achados, conf, tela, nivel="ERRO"):
    return any(a["conferencia"] == conf and a["tela"] == tela and a["nivel"] == nivel for a in achados)


# ---- a peça com um defeito plantado por tela (carrossel) ----
LINHA = '<svg style="position:absolute;left:0;top:0" width="1080" height="1350"><line x1="100" y1="324" x2="900" y2="324" stroke="#1B3A8C" stroke-width="6"/></svg>'
TELAS = [
    ("", '<p style="top:200px">Capa limpa, sem nada de errado.</p>'),                                          # 1
    ("", '<p style="top:300px">Texto cruzado por um traço do desenho</p>' + LINHA),                          # 2
    ("", '<p style="top:300px">Primeiro bloco de texto aqui</p><p style="top:310px">Segundo bloco por cima</p>'),  # 3
    ("", '<p style="top:300px;color:#eeeeee">Texto quase da cor do papel</p>'),                              # 4
    ("", '<div style="position:absolute;left:560px;top:290px;width:200px;height:70px;background:#000"></div>'
         '<p style="top:300px">Texto que passa sobre uma faixa preta no fim</p>'),                             # 5
    ("", '<p style="top:300px;left:700px;white-space:nowrap">Este texto passa da borda direita da tela</p>'),   # 6
    ("", '<div style="position:absolute;left:126px;top:300px;width:500px;height:40px;overflow:hidden">'
         '<p style="position:static">Três linhas de texto numa caixa baixa que corta o que passa dela</p></div>'),  # 7
    ("", '<p style="top:200px">Um desenho com a cor trocada</p><svg style="position:absolute;left:300px;top:600px" '
         'width="100" height="100"><rect class="anula" x="10" y="10" width="80" height="80" fill="#ff0000"/></svg>'),  # 8
    ("", '<p class="destaque" style="top:600px;left:10px">Destaque na zona proibida</p>'),                  # 9
    ("", '<p style="top:600px">Uma frase — com travessão no meio</p>'),                                       # 10
    (' data-video="5"', '<p style="top:600px">Tela em vídeo sem window.quadro</p>'),                         # 11
    ("", '<h2 class="titulo" style="top:100px">Título</h2>'),                                                 # 12
    ("", '<h2 class="titulo" style="top:100px">Título</h2>'),                                                 # 13
    ("", '<h2 class="titulo" style="top:100px">Título</h2>'),                                                 # 14
    ("", '<h2 class="titulo" style="top:130px">Título</h2>'),                                                 # 15
    ("", '<p class="bloco citacao" style="top:200px">Uma fala curta entre aspas.</p>'                        # 16
         '<p class="bloco fonte" style="top:420px">Fulano, 2014.</p><p class="bloco" style="top:500px">O corpo seguinte.</p>'),
    ("", '<p class="bloco margem" style="top:200px">uma nota</p><svg style="position:absolute;left:0;top:0" '
         'width="1080" height="1350"><path class="seta-livre" d="M 300 230 C 400 300 500 400 600 700" fill="none" '
         'stroke="#1B3A8C" stroke-width="4"/></svg>'),                                                           # 17
    # a zona proibida pela regra escrita (rubrica de qualidade): a nota e a marca de margem fora dela avisam; a chamada
    # (a nota no corpo da chamada, 46 px, como na última tela da série) barra
    ("", '<p class="nota" style="top:600px;left:10px">uma nota na margem</p>'),                              # 18
    ("", '<p class="nota" style="top:600px;left:10px;font-size:46px;line-height:72px">Segue o perfil.</p>'),  # 19
    # as medidas da rubrica de design: a margem lateral do corpo e o piso do corpo de texto
    ("", '<p class="corpo" style="top:600px;left:50px">Corpo colado na borda</p>'),                          # 20
    ("", '<p class="corpo" style="top:600px;font-size:24px">Corpo miúdo demais</p>'),                        # 21
    # o rótulo do desenho num viewBox de 2160: 40 na unidade do svg são 20 px na tela; a fonte da série (26 px) não tem piso
    ("", '<p class="fonte" style="top:900px;font-size:26px">Fulano, 2014.</p><svg viewBox="0 0 2160 2700" width="1080" '
         'height="1350" style="position:absolute;left:0;top:0"><text x="400" y="600" font-size="40">rótulo</text></svg>'),  # 22
    ("", '<p class="corpo" data-sangria style="top:600px;left:20px">Corpo que sangra de propósito</p>'),     # 23
    # a escala não uniforme (preserveAspectRatio="none"): a letra de 40 achatada à metade na vertical tem 20 px de altura;
    # e a nota dentro do corpo leva o piso da nota (38), o papel mais próximo do texto
    ("", '<svg viewBox="0 0 1080 2700" preserveAspectRatio="none" width="1080" height="1350" style="position:absolute;'
         'left:0;top:0"><text x="400" y="1200" font-size="40">achatado</text></svg>'
         '<p class="corpo" style="top:900px">Corpo com <span class="nota">nota de 34</span> dentro</p>'),        # 24
    ("", '<p class="corpo" style="top:600px;left:auto;right:40px">Corpo colado à direita</p>'),             # 25
    # o li leva o papel do contêiner: na .fila não tem piso; na .nota, o da nota (38)
    ("", '<ul class="fila" style="position:absolute;top:300px;left:126px;margin:0"><li style="font-size:26px">item da '
         'fila</li></ul><ul class="nota" style="position:absolute;top:600px;left:126px;margin:0"><li style="font-size:32px">'
         'item da nota</li></ul>'),                                                                           # 26
    # o corpo de 34 encolhido por um transform:scale(.75) tem 25,5 px na tela
    ("", '<div style="position:absolute;top:600px;left:126px;transform:scale(.75);transform-origin:0 0">'
         '<p class="corpo" style="position:static">Corpo encolhido</p></div>'),                              # 27
    # o corpo cortado pela caixa e colado na borda é corte (ERRO), não também margem
    ("", '<div style="position:absolute;left:30px;top:600px;width:300px;height:30px;overflow:hidden">'
         '<p class="corpo" style="position:static">Corpo cortado pela caixa baixa</p></div>'),               # 28
]
ESPERADOS = [("sobreposicao_desenho", 2), ("sobreposicao_texto", 3), ("contraste", 4), ("contraste_parcial", 5),
             ("transbordo", 6), ("corte", 7), ("cor_anulada", 8), ("zona_proibida", 9), ("travessao", 10),
             ("video", 11), ("alinhamento_titulo", 15), ("zona_proibida", 19), ("corte", 28)]
AVISOS = [("respiro_grupos", 16), ("ponta_da_seta", 17), ("zona_proibida", 18), ("margem_lateral", 20),
          ("texto_miudo", 21), ("texto_miudo", 22), ("margem_lateral", 25), ("texto_miudo", 27)]

with tempfile.TemporaryDirectory() as tmp:
    mf.voz_pede_sem_travessao = lambda raiz=None: True   # a voz pede texto sem travessão: o travessão é ERRO
    a = conferir(tmp, "defeitos", pagina(TELAS, css=".anula{fill:#00ff00}"))
    for conf, tela in ESPERADOS:
        caso(f"ERRO {conf} na tela {tela}", tem(a, conf, tela), [x for x in a if x["tela"] == tela])
    for conf, tela in AVISOS:
        caso(f"AVISO {conf} na tela {tela}", tem(a, conf, tela, "AVISO"), [x for x in a if x["tela"] == tela])
    caso("a nota na margem fora da zona não é ERRO", not tem(a, "zona_proibida", 18), [x for x in a if x["tela"] == 18])
    caso("margem_lateral: a nota e a chamada na margem não avisam, o corpo com data-sangria também não",
         not any(x["conferencia"] == "margem_lateral" and x["tela"] in (18, 19, 23) for x in a),
         [x for x in a if x["conferencia"] == "margem_lateral"])
    caso("texto_miudo: o rótulo do svg sai na escala da tela, e a fonte de 26 px não tem piso",
         [x["tamanho_px"] for x in a if x["conferencia"] == "texto_miudo" and x["tela"] == 22] == [20.0],
         [x for x in a if x["tela"] == 22])
    caso("texto_miudo: a escala vertical do svg achatado (20 px) e a nota dentro do corpo (piso 38)",
         sorted((x["papel"], x["tamanho_px"]) for x in a if x["conferencia"] == "texto_miudo" and x["tela"] == 24)
         == [("nota manuscrita", 34.0), ("rótulo (texto do desenho)", 20.0)], [x for x in a if x["tela"] == 24])
    miudo = lambda t: sorted((x["papel"], x["tamanho_px"]) for x in a if x["conferencia"] == "texto_miudo" and x["tela"] == t)
    caso("margem_lateral: o lado direito", [x["lado"] for x in a if x["conferencia"] == "margem_lateral" and x["tela"] == 25]
         == ["direita"], [x for x in a if x["tela"] == 25])
    caso("texto_miudo: a nota de 34 px fica abaixo do piso dela (38)", miudo(18) == [("nota manuscrita", 34.0)], miudo(18))
    caso("texto_miudo: o li na .fila sem piso, o li na .nota com o piso da nota", miudo(26) == [("nota manuscrita", 32.0)], miudo(26))
    caso("texto_miudo: o corpo encolhido pelo transform:scale sai no tamanho da tela", miudo(27) == [("corpo", 25.5)], miudo(27))
    caso("margem_lateral: o corpo cortado pela caixa é só corte", not tem(a, "margem_lateral", 28, "AVISO"),
         [x for x in a if x["tela"] == 28])
    caso("a capa limpa não ganha margem_lateral nem texto_miudo",
         not any(x["tela"] == 1 and x["conferencia"] in ("margem_lateral", "texto_miudo") for x in a))
    caso("a capa limpa não tem ERRO", not any(x["tela"] == 1 and x["nivel"] == "ERRO" for x in a), [x for x in a if x["tela"] == 1])
    caso("nenhuma fonte_nao_carregada com a fonte local", not any(x["conferencia"] == "fonte_nao_carregada" for x in a))

    # a voz que não pede (ou o arquivo que não existe): o travessão é AVISO
    mf.voz_pede_sem_travessao = lambda raiz=None: False
    a = conferir(tmp, "travessao-sem-voz", pagina([("", '<p style="top:600px">Uma frase — com travessão no meio</p>')]))
    caso("sem a regra na voz, o travessão da tela é AVISO, não ERRO", tem(a, "travessao", 1, "AVISO") and not tem(a, "travessao", 1), a)
    mf.voz_pede_sem_travessao = lambda raiz=None: True

    # a peça publicada inteira: as regras da casa, a área segura, a zona proibida e o travessão viram AVISO; a
    # sobreposição continua ERRO
    a = conferir(tmp, "publicada", pagina(TELAS, css=".anula{fill:#00ff00}"), publicada=True)
    for conf, tela in ESPERADOS:
        nivel = "ERRO" if conf in ("sobreposicao_desenho", "sobreposicao_texto", "video") else "AVISO"
        caso(f"publicada: {conf} na tela {tela} sai {nivel}", tem(a, conf, tela, nivel))

    # a fonte que não carregou: a família que nenhuma regra declara (o @import da fonte da web sem rede)
    a = conferir(tmp, "fonte", pagina([("", '<p style="top:300px;font-family:\'Fonte Que Nao Veio\',monospace">Sem a fonte</p>')]))
    caso("ERRO fonte_nao_carregada na família não declarada", tem(a, "fonte_nao_carregada", 1), a)
    a = conferir(tmp, "fonte-pub", pagina([("", '<p style="top:300px;font-family:\'Fonte Que Nao Veio\',monospace">Sem a fonte</p>')]),
                 publicada=True)
    caso("fonte_nao_carregada continua ERRO na publicada", tem(a, "fonte_nao_carregada", 1))
    a = conferir(tmp, "fonte-arquivo", pagina([("", '<p style="top:300px;font-family:\'Arquivo Falho\',monospace">Arquivo</p>')],
                                              css='@font-face{font-family:"Arquivo Falho";src:url("nao-existe.woff2")}'))
    caso("ERRO fonte_nao_carregada no arquivo que falhou", tem(a, "fonte_nao_carregada", 1), a)
    a = conferir(tmp, "fonte-sistema", pagina([("", '<p style="top:300px;font-family:-apple-system,BlinkMacSystemFont,\'Fonte Teste\',sans-serif">Pilha do sistema</p>')]))
    caso("a pilha do sistema (-apple-system antes da fonte) não acusa", not any(x["conferencia"] == "fonte_nao_carregada" for x in a), a)

    # Stories: a área segura, e a proteção tela a tela (a tabela da API)
    ST = [("", '<p style="top:100px">Texto no topo, sob o nome do app</p>'),
          ("", '<p style="top:1850px">Texto na base, sob a caixa de resposta</p>'),
          ("", '<p style="top:900px">Story limpo, no meio da tela</p>'),
          ("", '<p class="corpo" style="top:900px;left:48px;font-size:24px">Corpo a 48 px da borda</p>')]
    html = pagina(ST, h=1920)
    a = conferir(tmp, "stories", html)
    caso("Stories: ERRO area_segura no topo e na base", tem(a, "area_segura", 1) and tem(a, "area_segura", 2), a)
    caso("Stories: a margem é a da área segura (sem margem_lateral a 48 px), e o texto miúdo avisa",
         not any(x["conferencia"] == "margem_lateral" for x in a) and tem(a, "texto_miudo", 4, "AVISO"),
         [x for x in a if x["tela"] == 4])
    caso("Stories: a tela limpa sem ERRO", not any(x["tela"] == 3 and x["nivel"] == "ERRO" for x in a))
    a = conferir(tmp, "stories-api", html, publicada=frozenset({1}))
    caso("Stories pela API: a tela com linha na tabela sai AVISO, a sem linha continua ERRO",
         tem(a, "area_segura", 1, "AVISO") and tem(a, "area_segura", 2, "ERRO"), a)

    # a peça limpa: nenhum ERRO e nenhum dos AVISOs novos
    LIMPA = [("", '<h2 class="titulo" style="top:100px">Um título</h2><p class="bloco corpo" style="top:300px">Um parágrafo de corpo.</p>')] * 4
    a = conferir(tmp, "limpa", pagina(LIMPA))
    caso("a peça limpa não ganha ERRO", not any(x["nivel"] == "ERRO" for x in a), a)
    caso("a peça limpa não ganha margem_lateral nem texto_miudo",
         not any(x["conferencia"] in ("margem_lateral", "texto_miudo") for x in a), a)

    # a ponta da seta medida no mesmo lugar que o alvo: o prepararSlide desce o desenho 400 px (o assentamento do
    # caderno.js mexe no fluxo) e, na tela 2, troca o path.seta-livre por um <g>, como o traço de pena
    DESENHO = ('<div class="desce" style="position:absolute;left:0;top:0;width:1080px;height:600px">'
               '<svg width="1080" height="600" style="position:absolute;left:0;top:0"><rect x="600" y="100" width="200" '
               'height="200" fill="none" stroke="#1B3A8C" stroke-width="4"/><path class="seta-livre" '
               'd="M 200 400 C 300 400 500 300 650 200" fill="none" stroke="#1B3A8C" stroke-width="4"/></svg></div>')
    DESCE = ("<script>window.prepararSlide = async i => { const s = document.querySelectorAll('.slide')[i];"
             " s.querySelector('.desce').style.top = '400px';"
             " if (i === 1) for (const p of s.querySelectorAll('path.seta-livre')) p.replaceWith(document.createElementNS('http://www.w3.org/2000/svg', 'g')); };</script>")
    a = conferir(tmp, "seta-desce", pagina([("", DESENHO), ("", DESENHO)], script=DESCE))
    caso("ponta_da_seta: o desenho que o prepararSlide desce não vira seta no vazio (a ponta lida depois dele)",
         not any(x["conferencia"] == "ponta_da_seta" for x in a), [x for x in a if x["conferencia"] == "ponta_da_seta"])

    # o zoom das juntas (juntas.py): a ponta e a saída da seta e as pontas do traço aberto, recortadas a 4×
    jt = carregar("juntas", AQUI.parents[1] / "object-anatomy" / "scripts")
    pasta = pathlib.Path(tmp) / "defeitos"
    n = jt.main([str(pasta), "slides.html", "--saida", str(pathlib.Path(tmp) / "juntas"), "--telas", "17"])
    from PIL import Image
    recortes = sorted((pathlib.Path(tmp) / "juntas").glob("tela-17-*.png"))
    caso("juntas: a seta da tela 17 sai em recortes de 480 px (4× de 120)", n == len(recortes) >= 2
         and all(Image.open(r).size == (480, 480) for r in recortes), [r.name for r in recortes])
    try:
        jt.main([str(pasta), "slides.html", "--saida", str(pathlib.Path(tmp) / "juntas-fora"), "--telas", "99"])
        fora = "sem erro"
    except SystemExit as e:
        fora = e.code
    except Exception as e:  # noqa: BLE001 - o que o teste quer ver é que não cai aqui
        fora = f"{type(e).__name__}: {e}"
    caso("juntas: --telas fora de 1 a N sai com a mensagem de uso (código 2), sem erro do navegador", fora == 2, fora)

muitos = [{"ponta": (k * 100.0, 50.0), "inicio": (k * 100.0, 900.0)} for k in range(1, 26)]
pts, cortados = carregar("juntas", AQUI.parents[1] / "object-anatomy" / "scripts").pontos_da_tela(muitos, [], 60)
caso("juntas: além de 40 pontos por tela, o corte se conta (para o juntas.md dizer)", len(pts) == 40 and cortados == 10,
     (len(pts), cortados))

# ---- funções puras: legenda, roteiro, ids do bucket, medidas de forma ----
L = ct.conferir_legenda
mf.voz_pede_sem_travessao = VOZ
caso("legenda: travessão é ERRO na exportação quando a voz pede", any(x["conferencia"] == "travessao" and x["nivel"] == "ERRO"
                                                                    for x in L("Uma — frase.", exportacao=True, travessao="ERRO")))
caso("legenda: travessão é AVISO sem a regra na voz", any(x["conferencia"] == "travessao" and x["nivel"] == "AVISO"
                                                       for x in L("Uma — frase.", exportacao=True)))
caso("legenda: travessão fica fora do ensaio da publicação", not any(x["conferencia"] == "travessao" for x in L("Uma — frase.")))
caso("legenda: travessão na publicada é AVISO", any(x["conferencia"] == "travessao" and x["nivel"] == "AVISO"
                                                    for x in L("Uma — frase.", True, exportacao=True, travessao="ERRO")))
with tempfile.TemporaryDirectory() as tmp_voz:
    raiz = pathlib.Path(tmp_voz)
    caso("voz: sem context/sobre-mim.md, nada a pedir (None) e o nível é AVISO",
         mf.voz_pede_sem_travessao(raiz) is None and mf.nivel_travessao(None, raiz) == "AVISO")
    (raiz / "context").mkdir()
    (raiz / "context" / "sobre-mim.md").write_text("Pergunte se o travessão é proibido na sua voz.\n", encoding="utf-8")
    caso("voz: o roteiro em branco, que só pergunta, não pede", mf.nivel_travessao(None, raiz) == "AVISO")
    (raiz / "context" / "sobre-mim.md").write_text("Escrevo sem travessão.\n", encoding="utf-8")
    caso("voz: \"sem travessão\" pede, e o nível é ERRO", mf.nivel_travessao(None, raiz) == "ERRO")
caso("legenda: o meio-traço do intervalo não é travessão", not any(x["conferencia"] == "travessao" for x in L("De 2012–2014.", exportacao=True)))
caso("legenda: 6 hashtags é ERRO", any(x["conferencia"] == "hashtags" and x["nivel"] == "ERRO" for x in L("#a #b #c #d #e #f")))
caso("legenda: caractere invisível avisa", any(x["conferencia"] == "caractere_invisivel" for x in L("Olá​mundo.", exportacao=True)))
caso("legenda: primeira frase longa avisa, curta não",
     any(x["conferencia"] == "primeira_frase_legenda" for x in L("a" * 130 + ".", exportacao=True))
     and not any(x["conferencia"] == "primeira_frase_legenda" for x in L("Curta. " + "b" * 200, exportacao=True)))

ROT = "---\ndata: 2026-11-10\nestagio: {e}\n---\n\n# Roteiro\n\n{pub}"
TAB = ("## Publicado\n\nPublicada pela API, na ordem; os ids vêm da publicação.\n\n"
       "| Story | id na API | publicado | tipo | link |\n|---|---|---|---|---|\n"
       "| 1 | 900000000000000001 | 10:00 | imagem | x |\n| 2 | 900000000000000002 | 10:01 | imagem | x |\n")
caso("roteiro sem tabela, estagio pronto: não publicada", ct.publicada_do_roteiro(ROT.format(e="pronto", pub="")) is False)
caso("roteiro sem tabela, estagio publicado: a sequência inteira", ct.publicada_do_roteiro(ROT.format(e="publicado", pub="")) is True)
caso("roteiro com a tabela da API: os Stories com linha", ct.publicada_do_roteiro(ROT.format(e="pronto", pub=TAB)) == frozenset({1, 2}))
caso("rodada interrompida com o estagio marcado pela coleta: vale a tabela",
     ct.publicada_do_roteiro(ROT.format(e="publicado", pub=TAB)) == frozenset({1, 2}))
# a ligação pela imagem e a ligação à mão gravam a tabela sem as colunas "tipo" e "link": a coluna "id na API"
# sozinha não protege tela a tela
LIGADO = ("## Publicado\n\nLigado pela imagem: diferença de 1.0 a 2.0 na tela escolhida.\n\n"
          "| Story | id na API | publicado |\n|---|---|---|\n| 1 | 900000000000000001 | 10:00 |\n")
caso("a tabela da ligação pela imagem não protege tela a tela", ct.publicada_do_roteiro(ROT.format(e="publicado", pub=LIGADO)) is True,
     ct.publicada_do_roteiro(ROT.format(e="publicado", pub=LIGADO)))
caso("a ligação pela imagem não é a tabela da API", ct.tabela_da_api(ROT.format(e="publicado", pub=LIGADO)) is None)
GRAVADA = "## Publicado\n\n" + ct.INTRO_DA_API + ct.CABECALHO_DA_API + "| 1 | 900000000000000001 | 10:00 | imagem | x |\n"
caso("a tabela no formato da publicação pela API protege tela a tela",
     ct.publicada_do_roteiro(ROT.format(e="publicado", pub=GRAVADA)) == frozenset({1}))
caso("o travessão da tela e o da legenda são a mesma regex", ct.TRAVESSAO.pattern in ct.MEDIR)
if hasattr(ex, "carregar_ct"):
    caso("export: o conferir_telas.py carrega uma vez só", ex.carregar_ct() is ex.carregar_ct())
caso("id do objeto sem o sufixo -miniatura", ct.id_do_objeto("stories/publicado/2026-11-10/900000000000000001-miniatura.jpg") == "900000000000000001"
     and ct.id_do_objeto("stories/publicado/2026-11-10/900000000000000002.mp4") == "900000000000000002")
caso("protegida: o conjunto, True e False", ct.protegida(frozenset({1}), 1) and not ct.protegida(frozenset({1}), 2)
     and ct.protegida(True, 9) and not ct.protegida(False, 1))

# a decisão de publicada da exportação (o export_slides.py da slides-export), que usa a tabela daqui
tabela = ct.tabela_da_api(ROT.format(e="pronto", pub=TAB))
if hasattr(ex, "decidir_stories"):
    p, _ = ex.decidir_stories(frozenset({1, 2}), tabela, {"900000000000000001", "900000000000000002"})
    caso("export: Story com linha protegido, sem linha livre", p == frozenset({1, 2}))
    p, _ = ex.decidir_stories(frozenset({1, 2}), tabela, {"900000000000000001", "900000000000000003"})
    caso("export: o id no bucket fora da tabela protege a sequência inteira", p is True)
    p, msg = ex.decidir_stories(frozenset({1, 2}), tabela, None)
    caso("export: sem resposta do bucket, vale a tabela, com aviso", p == frozenset({1, 2}) and "AVISO" in msg)
    p, _ = ex.decidir_stories(False, None, {"900000000000000001"})
    caso("export: sem tabela, o bucket com Story do dia protege a sequência", p is True)
    p, _ = ex.decidir_stories(False, None, set())
    caso("export: sem tabela e sem nada no bucket, não publicada", p is False)
else:
    print("--    a decisão de publicada da exportação: o export_slides.py não tem decidir_stories (pulado)")

with tempfile.TemporaryDirectory() as tmp:
    raiz = pathlib.Path(tmp)
    pub = raiz / "marketing/social-media/carousels/series/x/2026-11-10_a"
    (pub / "assets").mkdir(parents=True)
    (pub / "assets" / "desenho.png").write_bytes(b"o mesmo desenho")
    (pub / "legenda.md").write_text("# L\n\n**Publicado:** 2026-11-10 18:02\n", encoding="utf-8")
    (pub / "slides.html").write_text('<img src="assets/desenho.png">', encoding="utf-8")
    nova = raiz / "marketing/social-media/carousels/series/x/2026-11-13_b"
    nova.mkdir(parents=True)
    (nova / "copia.png").write_bytes(b"o mesmo desenho")
    (nova / "outro.png").write_bytes(b"outro desenho")
    r = mf.imagens_ja_publicadas(nova, [(nova / "copia.png").as_uri(), (nova / "outro.png").as_uri()], raiz=raiz)
    caso("imagem_ja_publicada: a cópia do desenho publicado avisa, o desenho novo não", r == [("copia.png", ["2026-11-10_a"])], r)
    (nova / "texto.md").write_text("## As telas\n\n**Tela 1, gancho**\n> *(nota)* Uma frase aprovada.\n\n## Lastro\n", encoding="utf-8")
    t = mf.telas_travadas(nova)
    caso("texto_fora_do_travado: a palavra trocada entra e sai", mf.diferenca_do_travado(t[1], "Uma frase mudada.") == (["mudada"], ["aprovada"]))

caso("corpo_sem_negrito: 1 de 5 telas com negrito avisa",
     any(x["conferencia"] == "corpo_sem_negrito" for x in mf.avisos_da_peca(
         [{"tela": k, "unidades": [{"palavras": 20, "negrito": k == 1}], "acento": 0.6} for k in range(1, 6)])))
caso("acento_area: a média abaixo do piso avisa, a das publicadas não",
     any(x["conferencia"] == "acento_area" for x in mf.avisos_da_peca([{"tela": 1, "unidades": [], "acento": 0.3}]))
     and not mf.avisos_da_peca([{"tela": 1, "unidades": [], "acento": 0.5}]))
EXEMPLO = AQUI.parents[3] / "marketing/social-media/carousels/series/exemplo/exemplo-de-post"
caso("papel_fora_da_tabela: o título fora da tabela e dois tamanhos de corpo",
     len(mf.papel_fora([{"papel": "titulo", "tamanho": 80, "entrelinha": 72, "peso": 700, "texto": "t"},
                        {"papel": "corpo", "tamanho": 32, "entrelinha": 48, "peso": 400, "texto": "a"},
                        {"papel": "corpo", "tamanho": 28, "entrelinha": 48, "peso": 400, "texto": "b"}], "a", 2,
                       mf.carregar_papeis(EXEMPLO))) == 3)
with tempfile.TemporaryDirectory() as tmp_st:
    st = pathlib.Path(tmp_st)
    (st / "roteiro.md").write_text("# Roteiro\n\n## Os Stories\n\n1. **A pergunta** (nota de produção)\n> Tem uma ==ferramenta== nova?\n> *(nota)* a calculista →\n\n2. **A situação**\n> Túnel de vento, **1940**.\n\n## Publicado\n\n> fora da seção\n", encoding="utf-8")
    sts = mf.telas_travadas(st)
    caso("texto travado dos Stories: sem texto.md, as linhas > do roteiro.md, sem as notas *( )*",
         set(sts) == {1, 2} and "ferramenta" in sts[1] and "nota" not in sts[1] and "a calculista" in sts[1]
         and "1940" in sts[2] and "fora da seção" not in " ".join(sts.values()), sts)
caso("a série sai da página: a tabela, o acento e o caderno.js pelo caderno que o slides.html carrega; nada sem ele",
     mf.carregar_papeis(EXEMPLO)["chamada"][0] == 44 and ct.curtas(EXEMPLO, "slides.html")
     and mf.acento_de(mf.carregar_serie(EXEMPLO)) == (11, 107, 88)
     and mf.carregar_papeis(AQUI) is None and ct.curtas(AQUI, "slides.html") == ())
a = ct.conferir(EXEMPLO, "slides.html")
caso("o post de exemplo da série de exemplo passa com 0 ERRO", not any(x["nivel"] == "ERRO" for x in a),
     [x for x in a if x["nivel"] == "ERRO"])

if FALHAS:
    print(f"{len(FALHAS)} caso(s) falharam")
    sys.exit(1)
print("todos os casos passaram")
