"""Conferências de código das telas de uma peça antes de exportar: o que se mede, sem juízo.

Uso: python conferir_telas.py <pasta-da-peca> [arquivo.html] [--legenda <caminho>] [--json]
O arquivo padrão é slides.html (nos Stories, stories.html); a legenda padrão é a legenda.md da pasta, se existir, e
o --legenda, um caminho a partir do diretório atual, para quando não existe.
Sai com código 1 quando há ERRO, 0 quando só há AVISO ou nada, e 2 com a mensagem de uso quando falta argumento
ou um arquivo pedido não existe.

Cada tela é preparada como na exportação (a tela ativa, o window.prepararSlide do caderno.js) e medida no Chromium
do Playwright, o mesmo motor do shot-scraper. Nada da série está aqui: o caderno.js e o design/papeis.json vêm da
pasta que a própria página carrega (medidas_forma.carregar_serie). A tabela de achados, com o que fazer em cada um,
está em ../references/conferencias.md. Conferências:

- sobreposicao_desenho (ERRO): texto sob ou sobre um traço ou desenho (svg). Filtro pelas caixas do DOM: a faixa
  central de cada linha de texto contra a caixa de cada forma do svg, com a espessura do traço; só onde cruzam, a
  confirmação nas camadas de pixel: o texto (a tela com os desenhos escondidos, com e sem o texto) e o desenho
  (a tela com o texto transparente, com e sem os desenhos), e conta os pixels pintados pelos dois. A caixa de uma
  seta curva é um retângulo que cruza o texto mesmo quando o traço passa longe; o pixel pega o traço real.
  Fica de fora o que é de propósito: elemento (ou ancestral) com a classe `intencional` ou o atributo
  `data-intencional` (a isenção vale para o elemento inteiro: no svg, para todos os traços dele), as marcas que o
  caderno.js desenha sobre o texto (svg.marcas: círculo, riscado, sublinhado) e a correção do caderno (`.corr`: a
  palavra riscada com a certa escrita em cima, texto sobre texto de propósito).
- sobreposicao_texto (ERRO): textos de blocos diferentes que se cruzam (faixa central das linhas, mais de 150 px²).
- area_ocupada (AVISO, só no carrossel): a maior faixa horizontal vazia contínua da tela, entre a moldura de cima e a
  de baixo, em px e em fração da altura útil; foto, imagem e folha colada contam como ocupadas. O detalhe diz se a
  faixa está livre (aberta para a margem de cima ou de baixo) ou presa entre elementos. Nos Stories não roda: o
  adesivo e o post compartilhado entram pelo app, no espaço que o HTML deixa vazio de propósito. O vazio preso é
  defeito e o livre é escolha quando o foco o usa: o código mede, quem decide é a leitura; por isso é aviso, não
  erro. O limiar de 40% é ponto de partida, a calibrar com as telas que a leitura apontar como meio vazias.
- respiro_grupos (AVISO, só no carrossel; "o espaço entre grupos é maior que dentro deles"): o grupo é o .bloco.
  Um .bloco com mais de um parágrafo não pode ter, entre dois deles, um vão igual ou maior que o vão até o bloco
  vizinho da mesma coluna; e a .fonte que é bloco próprio fica mais perto do que ela cita (o bloco de cima) que do
  bloco de baixo. Os vãos se medem entre as caixas das linhas de texto (a Range), não entre as caixas dos elementos.
- area_segura (ERRO, só nos Stories): texto fora de y 192 a 1802 e x 32 a 1048 (as guias do editor do app; a
  moldura também); o adesivo simulado fica de fora.
- zona_proibida (só no carrossel): texto fora da área segura de 1000 por 1270 centrada (rubrica de qualidade, "Texto
  essencial em zona proibida": manchete, ponte ou chamada). ERRO no papel que a regra nomeia: o título (h1, h2,
  .titulo), o destaque, a chamada (.chamada, ou a .nota no corpo da chamada, que o papeis.json da série dá) e a
  .ponte; AVISO no resto (a nota, a marca de margem, o corpo), que a regra não proíbe. A moldura fica de fora, e o
  que leva data-sangria também.
- travessao: o travessão (—, e o – entre espaços) na tela ou, na exportação, na legenda. É regra de voz: ERRO quando a
  voz de quem usa (context/sobre-mim.md) pede texto sem travessão; sem o arquivo ou sem a regra, AVISO.
- margem_lateral (AVISO, só no carrossel de 1080): texto do corpo a menos de 80 px da borda da esquerda ou da
  direita (rubrica de design, "Medidas"). Fica de fora o que mora na margem de propósito: a anotação (.nota, .margem,
  .rot, .leg), o texto do desenho (svg), a marca de margem (.marg) e o rótulo dos Stories (.rotulo); a moldura, o
  data-sangria e o que já passa da tela ou da caixa que corta (é transbordo ou corte). Nos Stories, a lateral é a da
  área segura (x 32 a 1048), que já tem conferência. Provisório, a calibrar.
- texto_miudo (AVISO, numa tela de 1080): o piso do corpo de texto da rubrica de design ("Medidas"), pelo papel mais
  próximo do texto (no svg, só dentro dele): corpo e destaque (.corpo, .destaque, e o li sem papel acima dele) 30 px,
  a nota manuscrita (.nota, .margem) 38, o rótulo (.rot, .leg, e o texto do svg sem classe de papel) 28. O tamanho é
  o da tela, pela escala vertical (o viewBox do svg, o transform dos ancestros). O papel que a rubrica não nomeia
  (título, citação, fonte, apoio, fila, link, chamada) e o texto sem classe de papel ficam de fora, e a moldura
  também. Provisório, a calibrar.
  As duas são a parte 3 do Impeccable (`body-text-viewport-edge` e `tiny-text`), a partir do Impeccable, Apache 2.0.
- fonte_nao_carregada (ERRO): a família, estilo ou peso que não carregou na tela (o fontes.py, pedido antes e depois do
  prepararSlide): as medidas seriam da fonte de reserva, então a conferência não vale, e o --upload não sobe.
- hashtags (ERRO): mais de 5 hashtags na legenda (o limite do Instagram; rubrica de qualidade, "Hashtags demais").
  Vira AVISO quando a legenda.md já marca a peça como publicada (a linha **Publicado:**): as já publicadas ficam
  como estão.
- dia_relativo (AVISO): as palavras de PALAVRAS_DO_DIA, a regra "sem hoje, amanhã nem ontem", na tela ou na legenda.
  É aviso porque a palavra não decide sozinha ("que hoje vê até 20%" é "atualmente").
- Os adesivos e a chamada dos Stories, só nas telas de 1920: adesivo_desconhecido (AVISO), o tipo do data-adesivo fora
  da lista única ADESIVOS (aqui, em "As listas dos Stories"); texto_sob_adesivo (AVISO), linha de texto (fora o que é
  de propósito) dentro da caixa do adesivo simulado, lida do ::after que o adesivos.css desenha com body.previa (a
  mesma da imagem da prévia; o tipo sem medida no app não tem caixa); adesivo_na_borda (AVISO), a caixa fora da área
  segura (a metade direita avança o Story, o pé tem a caixa de resposta); chamada_sem_caminho (AVISO), a lista
  CHAMADAS_SEM_CAMINHO ("arrasta pra cima", "link na bio", "clica aqui"); link_sem_adesivo (AVISO), o texto que fala em
  link numa tela sem data-adesivo="link"; e destaque_sem_data (ERRO; AVISO na tela publicada), com `destaque: true` no
  frontmatter do roteiro.md, a tela que diz o dia da semana ou a hora sem uma data (DIA_DA_SEMANA, HORA e DATA).
- palavra_sozinha (AVISO): bloco de texto (título, destaque, citação, corpo, apoio, nota, item de lista) com duas
  linhas ou mais e uma palavra só na última. Acabamento.
- palavra_curta_no_fim (AVISO): linha de título, destaque ou citação, fora a última do bloco, que termina numa
  palavra da lista CURTAS (a mesma que o caderno.js da série prende à seguinte). Acabamento.
  As linhas saem das caixas de cada palavra (uma Range por palavra), agrupadas pela altura e ordenadas, depois do
  prepararSlide e com as fontes conferidas (fonte_nao_carregada, acima).
- video (ERRO): a tela com data-video sem window.quadro(t, idx), ou com a duração fora de 3 a 60 s.

Os AVISOs de forma estão em medidas_forma.py (papel fora da tabela, imagem já publicada, texto fora do travado, corpo
sem negrito, área do acento, ponta da seta, legenda, cor fora dos tokens, itens por grupo e papéis por tela); a linha de NOTA das isenções usadas na peça fecha o relatório.

As regras da casa (os limites que o código aplica, que o design system de cada série repete):
- alinhamento_titulo (ERRO, só no carrossel): o primeiro título de cada tela (h1, h2 ou .titulo em bloco), fora a
  capa, comparado com a posição que as telas irmãs repetem (a moda do topo e da esquerda, com ao menos três telas com
  título e duas na moda; em empate sai um AVISO "sem moda", sem acusar tela); acusa acima de 2 px (ruído de render).
  Acima de 100 px o desvio pode ser escolha, mas precisa estar declarada: o título com `data-alinhamento` não acusa
  (só acima de 100 px; é um atributo próprio, porque o `data-intencional` tiraria o título das conferências de
  sobreposição). Nos Stories não roda: cada tela é vista sozinha e o título anda com a tela.
- contraste e contraste_parcial (ERRO; no parcial, AVISO a menos de 0,1 do mínimo): o contraste de cada linha de
  texto contra o fundo renderizado atrás dela, sem as linhas do papel e sem as marcas que o caderno.js desenha sobre o
  texto (a tela com o texto transparente, as linhas do papel apagadas (na tela que declara --passo, as camadas de
  gradiente do background-image saem e as url() ficam; na tela sem --passo nada sai) e o svg.marcas escondido), pixel
  a pixel pela fórmula da WCAG, na faixa central da linha. A mediana abaixo do mínimo é `contraste`; a mediana passa e
  os 10% piores pixels (p10) não, é `contraste_parcial`: o texto que cruza um traço, um carimbo ou um desenho. O
  mínimo é 4,5:1 no texto corrido e 3:1 no texto grande (66 px ou mais, ou 52 em negrito). As linhas e as marcas saem
  porque a linha fina do papel sob a nota derrubaria o p10 de toda nota, e o riscado sob a palavra riscada é de
  propósito. A opacidade é a acumulada dos ancestrais. O adesivo simulado fica de fora. Cor computada que não é
  rgb()/rgba() (oklch, color-mix) sai como AVISO cor_nao_lida, porque o contraste não foi medido nela.
- transbordo e corte (ERRO): uma linha de texto que passa da borda da tela (transbordo) ou da caixa de um ancestral
  com overflow que corta em algum eixo (hidden, clip, auto, scroll), em mais de 1 px, sem sangria declarada
  (`data-sangria` no elemento ou num ancestral). Qualquer corte de texto que se lê é defeito, sem tolerância.
- cor_anulada (ERRO): atributo fill ou stroke de um elemento do svg que uma regra de CSS anula (a cor computada não
  é a declarada). O código sai como declarado.
Na tela já publicada (o carrossel inteiro com **Publicado:** na legenda.md; nos Stories pela API, só os que têm linha
na tabela "Publicada pela API" do roteiro.md (tabela_da_api); nos outros Stories, a sequência inteira pelo estagio;
rodado sozinho, este script só lê o roteiro, e a exportação também consulta o bucket), o defeito das regras da casa,
da área segura, da zona proibida e do travessão (PUBLICADA_AVISA) que já foi ao ar vira AVISO e não barra a versão
nova, como as hashtags. A sobreposição de texto com traço ou com texto e a fonte que não carregou continuam ERRO
também na publicada.
"""
import functools, io, json, os, re, sys, unicodedata
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))   # medidas_forma.py, ao lado
sys.path.insert(1, str(Path(__file__).resolve().parents[2] / "slides-export" / "scripts"))   # fontes.py, com quem renderiza
CHAMADA_PADRAO = 46   # px: o corpo da chamada para a peça sem design/papeis.json (a avulsa); a da série vem do JSON
from fontes import CARREGAR_FONTES  # noqa: E402
import medidas_forma as mf  # noqa: E402


ROOT = Path(__file__).resolve().parents[4]
MAX_HASHTAGS = 5
AREA_TEXTO_TEXTO = 150      # px²
PIXELS_MIN = 12             # pixels em comum para confirmar a sobreposição (abaixo disso, é antialias da borda)
DIF = 40                    # diferença (soma dos três canais) para contar o pixel como pintado pela camada
# D2 (rubrica de design): as palavras curtas que não terminam linha de título, destaque ou citação. A lista é
# a do prenderCurtas do caderno.js que a página carrega, lida de lá (curtas()) para não haver duas (o caminho sai
# da página, não do código).
VAZIO_AVISO = 0.40          # maior faixa vazia contínua a partir de 40% da altura útil, só no carrossel. Ponto de
                            # partida, a calibrar com as telas que a leitura apontar como meio vazias
# área segura dos Stories (as guias do editor do app; rubrica de Stories) e zona proibida do carrossel (1000 por 1270
# centrada, rubrica de qualidade)
STORIES_TOPO, STORIES_BASE, STORIES_LADO = 192, 118, 32
ZONA_CARROSSEL = (1000, 1270)
TRAVESSAO = re.compile(r"—|(?<=\s)–|–(?=\s)")   # o travessão; o meio-traço só como travessão (entre espaços), não no intervalo
# Regras da casa (o design system da série, "Regras da casa"; rubrica de design, "Medidas")
TOL_ALINHA = 2              # px: ruído de render
DESVIO_ESCOLHA = 100        # px: acima disso o desvio do título pode ser escolha, se declarado (data-alinhamento no título)
CONTRASTE_CORRIDO = 4.5     # mínimo WCAG do texto corrido
CONTRASTE_GRANDE = 3.0      # mínimo do texto grande
GRANDE_REGULAR = 66         # px: texto grande em peso normal (rubrica de design, "Medidas")
GRANDE_NEGRITO = 52         # px: texto grande em negrito (700 ou mais)
AVISO_CONTRASTE = 0.1       # no contraste parcial, a menos disso do mínimo é AVISO, não ERRO
FORA_MIN = 1.0              # px: transbordo ou corte abaixo disso é arredondamento do navegador
# na peça já publicada, o defeito das regras da casa que já foi ao ar vira AVISO e não barra a versão nova, como as
# hashtags
PUBLICADA_AVISA = {"contraste", "contraste_parcial", "transbordo", "corte", "alinhamento_titulo", "cor_anulada",
                   # e a área segura, a zona proibida e o travessão: na publicada, viram AVISO como as regras da casa
                   "area_segura", "zona_proibida", "travessao",
                   # e a data do Story de Destaque: a tela que já foi ao ar fica como está
                   "destaque_sem_data"}
# zona_proibida: o papel que a rubrica de qualidade nomeia (manchete, ponte, chamada) barra; o resto avisa
ZONA_ESSENCIAL = "h1,h2,.titulo,.destaque,.chamada,.ponte"
# As medidas da rubrica de design ("Medidas (sempre em código)") que ainda não tinham código (a parte 3 do
# Impeccable, `body-text-viewport-edge` e `tiny-text`, a partir do Impeccable, Apache 2.0): AVISO provisório até
# calibrar, como os outros provisórios
MARGEM_LATERAL = 80         # px numa tela de 1080: "Margem lateral numa tela de 1080, pelo menos 80 px"
# o piso do corpo de texto, pelo papel mais próximo do texto (o seletor que casa primeiro, subindo da tag do texto):
# corpo e destaque 30, a nota em letra manuscrita 38, o rótulo 28; o papel que a rubrica não nomeia (título, citação,
# fonte, apoio, fila, link, chamada) não tem piso dela e fica de fora (a fonte da série é 26 px pela tabela "Letra")
PISOS = (("h1,h2,.titulo,.citacao,.fonte,.apoio,.fila,.link,.chamada,.ponte", None, 0),
         (".nota,.margem", "nota manuscrita", 38),
         (".rot,.leg", "rótulo", 28),
         (".corpo,.destaque", "corpo", 30))
PISO_ROTULO, PISO_CORPO = PISOS[2][1:], PISOS[3][1:]   # o texto do svg é rótulo; o li sem papel acima dele, corpo
PISOS_DETALHE = ", ".join(f"{nome} {px} px" for _, nome, px in PISOS if nome)


@functools.lru_cache(maxsize=None)
def _curtas_de(caminho):
    m = re.search(r"const CURTAS = new Set\(\[([^\]]*)\]\)", Path(caminho).read_text(encoding="utf-8"))
    if not m:
        raise RuntimeError(f"CURTAS não encontrada em {caminho}")
    return tuple(re.findall(r"'([^']+)'", m.group(1)))


def curtas(pasta, html):
    """A lista CURTAS do caderno.js que a página carrega (a que o prenderCurtas prende à seguinte); () sem ele."""
    d = mf.pasta_do_caderno(pasta, html)
    return _curtas_de(str(d / "caderno.js")) if d is not None and (d / "caderno.js").is_file() else ()


# A regra "sem hoje, amanhã nem ontem": o Story e o post ficam no ar além do dia em que saem, e a referência relativa
# erra para quem vê depois. As locuções vêm antes das palavras soltas ("hoje à noite" antes de "hoje"), para a
# palavra que já contou numa locução não contar de novo. Se um avaliador dos Stories vier a usar a lista, ele a
# importa daqui, para não haver duas.
PALAVRAS_DO_DIA = ("hoje à noite", "agora há pouco", "daqui a pouco", "mais tarde", "acabei de", "esta noite", "esta manhã",
                   "esta semana", "hoje", "amanhã", "ontem", "agora")


def palavras_do_dia():
    """A lista da regra do dia relativo (PALAVRAS_DO_DIA)."""
    return PALAVRAS_DO_DIA


# As listas dos Stories, uma fonte só: a rubrica de Stories, o README dos Stories e o modelo stories.html apontam para
# cá. Os tipos de adesivo que uma tela pode declarar em data-adesivo (o tipo fora da lista é AVISO); o adesivos.css
# desenha na prévia os que já têm medida no app (enquete, caixinha, reacao, barra). O link é o adesivo de link do app.
ADESIVOS = ("enquete", "caixinha", "pergunta", "quiz", "reacao", "barra", "foto", "link", "post", "resposta", "resultado")
# O dia da semana e a data, para o Story de Destaque, que pede a data, e não só o dia da semana (stories-o-que-evitar.md,
# item 2). Buscam no texto sem acento ("terca", "sabado"); o dia da semana que é ordinal ("segunda parte", "pela
# segunda vez") não conta. Os marcadores __ORDINAL__ e __MESES__ se trocam pelas listas, em padrao_de_stories().
ORDINAL = r"parte|vez|etapa|fase|tela|dica|pergunta|opcao|edicao|aula|temporada|chance|serie|versao|rodada|metade"
MESES = r"janeiro|fevereiro|marco|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro"
DIA_DA_SEMANA = r"\b(?:sabado|domingo)\b|\b(?:segunda|terca|quarta|quinta|sexta)(?:-feira\b|\b(?![ \t]+(?:__ORDINAL__)\b))"
DATA = r"\b\d{1,2}/\d{1,2}\b|\b\d{1,2} de (?:__MESES__)\b|\bdia \d{1,2}\b"
HORA = r"\b\d{1,2}h(?:\d{2})?\b|\b\d{1,2}:\d{2}\b"  # "18h", "18h30", "18:30"
# A chamada que o app não deixa cumprir (stories/README.md, "No mesmo espírito"; stories-o-que-evitar.md, item 4), com
# as variantes do imperativo
CHAMADAS_SEM_CAMINHO = ("arrasta pra cima", "arrasta para cima", "arraste pra cima", "arraste para cima", "link na bio",
                        "clica aqui", "clique aqui")
_STORIES = {"ADESIVOS": ADESIVOS, "ORDINAL": ORDINAL, "MESES": MESES, "DIA_DA_SEMANA": DIA_DA_SEMANA, "DATA": DATA,
            "HORA": HORA, "CHAMADAS_SEM_CAMINHO": CHAMADAS_SEM_CAMINHO, "PALAVRAS_DO_DIA": PALAVRAS_DO_DIA}


def de_stories(nome):
    """Uma das listas dos Stories, pelo nome."""
    return _STORIES[nome]


@functools.lru_cache(maxsize=None)
def padrao_de_stories(nome):
    """DIA_DA_SEMANA, DATA ou HORA, com os marcadores trocados pelas listas ORDINAL e MESES."""
    p = de_stories(nome).replace("__ORDINAL__", de_stories("ORDINAL")).replace("__MESES__", de_stories("MESES"))
    return re.compile(p, re.I)


def sem_acento(texto):
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")


def destaque_do_roteiro(pasta):
    """O roteiro.md declara `destaque: true` no frontmatter: a sequência pode ir para um Destaque (stories/README.md,
    "No mesmo espírito"), e a tela que diz quando leva a data (stories-o-que-evitar.md, item 2)."""
    p = Path(pasta) / "roteiro.md"
    if not p.is_file():
        return False
    fm = re.match(r"---\n(.*?)\n---", p.read_text(encoding="utf-8").replace("\r\n", "\n"), re.S)
    m = re.search(r"""^destaque:[ \t]*["']?(\w+)""", fm.group(1), re.M) if fm else None
    return bool(m and m.group(1).lower() in ("true", "sim", "yes"))


def chamadas_da_tela(texto, tipos):
    """A chamada que o app não deixa cumprir (stories/README.md, "No mesmo espírito"; stories-o-que-evitar.md, item 4):
    as da lista CHAMADAS_SEM_CAMINHO, e o texto que fala em link numa tela sem o adesivo de link. AVISOs: "link na bio"
    pode dizer qual link logo depois, e "o link" pode ser o que vai por mensagem a quem responder."""
    t, out = (texto or "").lower(), []
    for c in de_stories("CHAMADAS_SEM_CAMINHO"):
        rx = rf"(?<![\wà-ú]){re.escape(c)}(?![\wà-ú])"
        if re.search(rx, t):
            out.append({"nivel": "AVISO", "conferencia": "chamada_sem_caminho", "texto": c,
                        "detalhe": "chamada que o app não deixa cumprir: o gesto de arrastar saiu do app, \"link na bio\" "
                                   "diz qual link, e \"clica aqui\" diz para onde vai (stories/README.md)"})
            t = re.sub(rx, " ", t)
    if "link" not in tipos and re.search(r"(?<![\wà-ú])links?(?![\wà-ú])", t):
        out.append({"nivel": "AVISO", "conferencia": "link_sem_adesivo", "texto": "link",
                    "detalhe": "o texto fala em link e a tela não declara data-adesivo=\"link\": no Story, o link vai "
                               "pelo adesivo de link; se é o link mandado por mensagem a quem responder, fica como está"})
    return out


def destaque_sem_data(texto):
    """No Story de Destaque, o dia da semana ou a hora sem a data (o "terça, 18h" vira uma terça qualquer): a lista do
    que a tela diz de quando, sem data absoluta na mesma tela, ou None."""
    t = sem_acento((texto or "").lower())
    if padrao_de_stories("DATA").search(t):
        return None
    achados = [m.group(0) for nome in ("DIA_DA_SEMANA", "HORA") for m in padrao_de_stories(nome).finditer(t)]
    return achados or None


# A caixa do adesivo simulado da tela, como o adesivos.css a desenha na prévia (o ::after com body.previa): a mesma
# medida que a imagem da prévia mostra, uma fonte só. O tipo sem regra no CSS (pergunta, quiz, link, post, resposta,
# foto) sai sem caixa: o tamanho dele não está medido no app
ADESIVO = r"""(idx) => {
  const sl = document.querySelectorAll('.slide')[idx];
  const tipos = (sl.getAttribute('data-adesivo') || '').split(/\s+/).filter(Boolean);
  const tinha = document.body.classList.contains('previa');
  document.body.classList.add('previa');
  const cs = getComputedStyle(sl, '::after');
  let caixa = null;
  if (cs.content !== 'none' && cs.position === 'absolute') {
    const l = parseFloat(cs.left), t = parseFloat(cs.top), w = parseFloat(cs.width), h = parseFloat(cs.height);
    if ([l, t, w, h].every(Number.isFinite) && w > 1 && h > 1) caixa = [l, t, l + w, t + h].map(v => Math.round(v * 10) / 10);
  }
  if (!tinha) document.body.classList.remove('previa');
  return {tipos, caixa};
}"""


# Prepara a tela idx como a exportação e devolve {faltam, setas}. As fontes se pedem antes do prepararSlide (o
# assentamento do caderno.js já mede) e de novo depois dele (o texto que ele mostra ou põe na tela), pelo fontes.py:
# o document.fonts.ready sozinho resolve antes de a fonte ser pedida, e o fonts.check não acusa a família que nem foi
# declarada (o @import da fonte da web sem rede). As setas livres do desenho
# (path.seta-livre) se leem antes do prepararSlide, porque o caderno.js as troca pelo traço de pena no mesmo lugar, mas
# depois das fontes, e a posição na tela sai depois dele: o ponto fica nas coordenadas do path, e a matriz que o leva à
# tela é a do pai (onde o traço de pena entra) depois do prepararSlide, porque o assentamento mexe no fluxo e os alvos
# se medem depois dele. A ponta e um ponto 12 px antes dela. O prepararSlide tem
# prazo: com uma fonte que não responde, ele esperaria o fonts.ready para sempre, e a fonte já sai na lista.
PREPARAR = """async (idx) => {
  const carregarFontes = """ + CARREGAR_FONTES + """;
  const telas = document.querySelectorAll('.slide'), sl = telas[idx];
  telas.forEach((s,i) => s.classList.toggle('active', i===idx));
  const st = document.getElementById('stage'); if (st) st.style.transform = 'none';
  for (const id of ['prev','next']) { const el = document.getElementById(id); if (el) el.style.display = 'none'; }
  document.querySelectorAll('.pager').forEach(p => p.style.display = 'none');
  const vistas = new Set(), faltam = [];
  const confere = async () => { for (const f of await carregarFontes(sl)) if (!vistas.has(f.chave)) { vistas.add(f.chave); faltam.push(f); } };
  await confere();
  const lidas = [];
  for (const p of sl.querySelectorAll('svg path.seta-livre')) {
    const L = p.getTotalLength ? p.getTotalLength() : 0, m = p.getScreenCTM(), pai = p.parentNode;
    const mp = pai && pai.getScreenCTM ? pai.getScreenCTM() : null; if (!L || !m || !mp) continue;
    lidas.push({p, pai, local: mp.inverse().multiply(m), pts: [L, Math.max(0, L - 12), 0].map(d => p.getPointAtLength(d)),
                classe: p.getAttribute('class'), intencional: !!p.closest('.intencional,[data-intencional]')});
  }
  if (window.prepararSlide) await Promise.race([window.prepararSlide(idx), new Promise(ok => setTimeout(ok, 20000))]);
  await confere();
  const o = sl.getBoundingClientRect(), setas = [];
  for (const s of lidas) {
    const mp = s.pai.isConnected && s.pai.getScreenCTM ? s.pai.getScreenCTM() : null;
    const m = s.p.isConnected ? s.p.getScreenCTM() : (mp ? mp.multiply(s.local) : null);
    if (!m) continue;
    const em = q => [Math.round((m.a * q.x + m.c * q.y + m.e - o.left) * 10) / 10, Math.round((m.b * q.x + m.d * q.y + m.f - o.top) * 10) / 10];
    const [ponta, antes, inicio] = s.pts.map(em);
    setas.push({ponta, antes, inicio, classe: s.classe, intencional: s.intencional});
  }
  return {faltam, setas};
}"""

MEDIR = """(idx) => {
  const sl = document.querySelectorAll('.slide')[idx], o = sl.getBoundingClientRect();
  const rel = r => [r.left - o.left, r.top - o.top, r.right - o.left, r.bottom - o.top].map(v => Math.round(v * 10) / 10);
  const INLINE = new Set(['B','I','STRONG','EM','SPAN','BR','SMALL','U','MARK','A','SUP','SUB','CODE','S']);
  const proposito = e => !!e.closest('.intencional,[data-intencional],svg.marcas,.corr');
  const adesivo = e => !!e.closest('.sim,[data-adesivo-sim]');
  const moldura = e => !!e.closest('.moldura,.pagina,.arroba,.pager');
  const PISOS = __PISOS__;
  // o papel mais próximo do texto, pela classe; no svg, só dentro dele (o svg num .corpo não faz do rótulo um corpo), e o
  // texto do desenho sem classe de papel é rótulo; o li sem classe de papel acima dele é corpo (a classe do contêiner,
  // como a .fila ou a .nota, vale mais que a tag; achado do /code-review)
  const pisoDe = el => { const lim = el.closest('svg');
    for (let e = el; e && e !== sl && e !== lim; e = e.parentElement) for (const [sel, nome, px] of PISOS) if (e.matches(sel)) return nome ? [nome, px] : null;
    if (lim) return [__ROTULO__[0] + ' (texto do desenho)', __ROTULO__[1]];
    return el.closest('li') ? __CORPO__ : null; };
  // o tamanho na tela é o font-size vezes a escala do eixo vertical (a altura da letra): no svg, a da matriz da tela
  // (o viewBox, que no preserveAspectRatio="none" difere da horizontal, achado do Codex, e as transformações); no
  // HTML, a das transformações dos ancestros (o transform:scale de um bloco que se encolheu para caber)
  const escalaDe = el => { const t = el.closest('svg') && (el.closest('text') || el);
    if (t) { const m = t.getScreenCTM ? t.getScreenCTM() : null; return m ? Math.hypot(m.c, m.d) : 1; }
    let s = 1;
    for (let a = el; a && a !== sl; a = a.parentElement) { const tr = getComputedStyle(a).transform;
      if (tr && tr !== 'none') { const m = new DOMMatrix(tr); s *= Math.hypot(m.c, m.d); } }
    return s; };
  const blocos = new Map();
  const blocoDe = el => { let e = el;
    if (e.closest('svg')) e = e.closest('text') || e;
    else while (e !== sl && INLINE.has(e.tagName) && getComputedStyle(e).display.startsWith('inline')) e = e.parentElement;
    if (!blocos.has(e)) blocos.set(e, blocos.size); return blocos.get(e); };
  const linhas = [];
  const tw = document.createTreeWalker(sl, NodeFilter.SHOW_TEXT); let n;
  while ((n = tw.nextNode())) {
    const t = n.textContent.replace(/\\s+/g, ' ').trim(); if (!t) continue;
    const pe = n.parentElement; if (pe.closest('style,script,title,desc')) continue;
    const cs = getComputedStyle(pe); if (cs.visibility === 'hidden') continue;
    // a opacidade que vale é a acumulada dos ancestrais (um bloco esmaecido com o texto num <b> é esmaecido)
    let opacidade = 1;
    for (let a = pe; a && a !== sl; a = a.parentElement) opacidade *= parseFloat(getComputedStyle(a).opacity);
    if (opacidade === 0) continue;
    if (cs.color === 'rgba(0, 0, 0, 0)' && !pe.closest('svg')) continue;  // seta escrita que virou traço
    const r = document.createRange(); r.selectNodeContents(n);
    // regras da casa: a cor e o tamanho para o contraste; a sangria declarada e o recorte por overflow escondido
    // num ancestral (fora a própria tela), em qualquer eixo, para o transbordo e o corte
    let clip = null;
    const CORTA = new Set(['hidden', 'clip', 'auto', 'scroll']);
    for (let a = pe; a && a !== sl; a = a.parentElement) {
      const ca = getComputedStyle(a);
      if (CORTA.has(ca.overflowX) || CORTA.has(ca.overflowY)) { clip = rel(a.getBoundingClientRect()); break; }
    }
    const bruto = n.textContent.replace(/\\s+/g, ' ');
    const extra = {cor: pe.closest('svg') ? cs.fill : cs.color, tamanho: parseFloat(cs.fontSize), peso: cs.fontWeight,
                   opacidade, sangria: !!pe.closest('[data-sangria]'), clip,
                   anotacao: !!pe.closest('.margem,.nota,.rot,.leg'),   // o kit de anotações: a seta que sai dela aponta um alvo
                   // a zona proibida barra só o papel que a rubrica nomeia (manchete, ponte, chamada); a chamada da
                   // série é a .nota no corpo da chamada
                   essencial: !!pe.closest('__ESSENCIAL__') || (!!pe.closest('.nota') &&
                     Math.abs(parseFloat(getComputedStyle(pe.closest('.nota')).fontSize) - __CHAMADA__) <= 1),
                   // o travessão, no texto inteiro do nó, não só nos 60 primeiros caracteres; a regex é a
                   // TRAVESSAO daqui, posta no lugar do marcador (uma só para a tela e a legenda)
                   travessao: /__TRAVESSAO__/.test(bruto) ? bruto.trim().slice(0, 80) : null,
                   // o piso do corpo de texto (rubrica de design, "Medidas"): o papel mais próximo do texto; o texto do
                   // desenho (svg) é rótulo
                   piso: pisoDe(pe), escala: escalaDe(pe), svg: !!pe.closest('svg'),
                   // a margem lateral é do texto do corpo: a marca de margem do kit (.marg) e o rótulo dos Stories
                   // (.rotulo) moram na margem de propósito, como a anotação (acima)
                   marca_margem: !!pe.closest('.marg,.rotulo')};
    for (const q of r.getClientRects()) if (q.width > .5 && q.height > .5)
      linhas.push({bloco: blocoDe(pe), texto: t.slice(0, 60), rect: rel(q), proposito: proposito(pe), adesivo: adesivo(pe), moldura: moldura(pe), ...extra});
  }
  // o primeiro título da tela (h1, h2 ou .titulo em bloco, fora do svg e da moldura), para o alinhamento entre irmãs
  let titulo = null;
  for (const e of sl.querySelectorAll('h1,h2,.titulo')) {
    if (e.closest('svg') || moldura(e) || adesivo(e) || getComputedStyle(e).display.startsWith('inline')) continue;
    const q = e.getBoundingClientRect(); if (q.width < 1 || q.height < 1) continue;
    // o desvio de alinhamento escolhido se declara com data-alinhamento no título (não com data-intencional, que
    // tiraria o título das conferências de texto sobre traço e sobre texto)
    titulo = {rect: rel(q), texto: e.textContent.replace(/\\s+/g, ' ').trim().slice(0, 40), declarado: !!e.closest('[data-alinhamento]')}; break;
  }
  // atributo fill ou stroke do svg que o CSS anula
  const SVGNS = 'http://www.w3.org/2000/svg', corAnulada = [];
  for (const el of sl.querySelectorAll('svg [fill], svg [stroke]')) {
    for (const prop of ['fill', 'stroke']) {
      const v = el.getAttribute(prop);
      if (!v || v === 'none' || v === 'currentColor' || v.startsWith('url(')) continue;
      // a sonda leva o valor como estilo com !important: um atributo nela receberia a mesma regra por tag (svg text{fill})
      // e a cor anulada ficaria invisível
      const probe = document.createElementNS(SVGNS, el.tagName); probe.style.setProperty(prop, v, 'important');
      el.parentNode.appendChild(probe); const quer = getComputedStyle(probe)[prop]; probe.remove();
      const sai = getComputedStyle(el)[prop];
      if (quer !== sai) corAnulada.push({tag: el.tagName.toLowerCase(), classe: String(el.className.baseVal || ''), prop, declarado: v, quer, sai,
                                        texto: (el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 40)});
    }
  }
  const formas = []; let k = 0;
  for (const svg of sl.querySelectorAll('svg')) {
    const r0 = svg.getBoundingClientRect(); if (r0.width < 1 || r0.height < 1) continue;
    const sid = 'cf' + (k++); svg.setAttribute('data-conf', sid);
    const cls = String(svg.className.baseVal || '').trim(), c0 = rel(r0);
    const nome = 'svg' + (cls ? '.' + cls.split(/\\s+/).join('.') : '') +
      ` em x ${Math.round(c0[0])}, y ${Math.round(c0[1])} (${Math.round(c0[2] - c0[0])} × ${Math.round(c0[3] - c0[1])})`;
    for (const f of svg.querySelectorAll('path,line,polyline,polygon,circle,ellipse,rect')) {
      const q = f.getBoundingClientRect(); if (q.width < .5 && q.height < .5) continue;
      const sw = parseFloat(getComputedStyle(f).strokeWidth) || 0;
      formas.push({svg: sid, nome, rect: rel(q), folga: sw / 2 + 2, proposito: proposito(f), classe: cls,
                   fcls: String(f.getAttribute('class') || '')});
    }
  }
  const figuras = [];  // foto, imagem e fundo com imagem: ocupam a tela, mas não entram na sobreposição
  for (const e of sl.querySelectorAll('img,picture,video,canvas,[style*="background-image"],.foto,.foto-canto,.folha-a')) {
    const q = e.getBoundingClientRect(); if (q.width > 1 && q.height > 1 && !moldura(e)) figuras.push(rel(q));
  }
  const folhas = [...sl.querySelectorAll('.folha-b')].map(e => rel(e.getBoundingClientRect()));   // alvo da seta da chamada
  // o respiro entre grupos: cada .bloco, com a caixa da tinta (as linhas de texto, fora o que está posto em absoluto, como a
  // correção escrita em cima) e a de cada parágrafo dele
  const tinta = el => { let u = null;
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let t;
    while ((t = w.nextNode())) {
      if (!t.textContent.trim()) continue;
      let solto = false;
      for (let a = t.parentElement; a && a !== el; a = a.parentElement) { const p = getComputedStyle(a).position; if (p === 'absolute' || p === 'fixed') { solto = true; break; } }
      if (solto || t.parentElement.closest('svg')) continue;
      const r = document.createRange(); r.selectNodeContents(t);
      for (const q of r.getClientRects()) if (q.width > .5 && q.height > .5) { const v = rel(q);
        u = u ? [Math.min(u[0], v[0]), Math.min(u[1], v[1]), Math.max(u[2], v[2]), Math.max(u[3], v[3])] : v; }
    }
    return u; };
  const grupos = [];
  for (const el of sl.querySelectorAll('.bloco')) {
    if (el.closest('svg') || moldura(el) || adesivo(el)) continue;
    const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const ink = tinta(el); if (!ink) continue;
    const partes = [];
    for (const c of el.children) {
      const cc = getComputedStyle(c);
      if (cc.display.startsWith('inline') || cc.position === 'absolute' || cc.position === 'fixed' || c.closest('svg')) continue;
      const pi = tinta(c); if (pi) partes.push({rect: pi, texto: c.textContent.replace(/\\s+/g, ' ').trim().slice(0, 40)});
    }
    grupos.push({rect: ink, partes, fonte: el.classList.contains('fonte'), cls: String(el.className),
                 texto: el.textContent.replace(/\\s+/g, ' ').trim().slice(0, 40)});
  }
  // as isenções usadas (a linha de NOTA)
  const isencoes = {};
  for (const [k, s] of [['intencional', '.intencional'], ['data-intencional', '[data-intencional]'], ['data-sangria', '[data-sangria]'],
                        ['data-alinhamento', '[data-alinhamento]']]) { const q = sl.querySelectorAll(s).length; if (q) isencoes[k] = q; }
  return {w: Math.round(o.width), h: Math.round(o.height), linhas, formas, figuras, folhas, titulo, corAnulada, grupos, isencoes,
          texto: sl.innerText.replace(/\\s+/g, ' ').trim()};
}""".replace("__TRAVESSAO__", TRAVESSAO.pattern).replace("__ESSENCIAL__", ZONA_ESSENCIAL).replace(
    "__PISOS__", json.dumps([list(p) for p in PISOS], ensure_ascii=False)).replace(
    "__ROTULO__", json.dumps(list(PISO_ROTULO), ensure_ascii=False)).replace("__CORPO__", json.dumps(list(PISO_CORPO), ensure_ascii=False))

QUEBRAS = r"""(idx) => {
  const sl = document.querySelectorAll('.slide')[idx];
  const SEL = '.titulo,.destaque,.citacao,.corpo,.apoio,.nota,li';
  const fora = e => !!e.closest('.moldura,.pagina,.arroba,.pager,.sim,[data-adesivo-sim],svg');
  const out = [];
  for (const el of sl.querySelectorAll(SEL)) {
    if (fora(el) || el.querySelector(SEL)) continue;   // a unidade é o bloco mais de dentro
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const palavras = [], caixas = [];
    let anterior = null;   // o nó de texto anterior: palavra partida por uma tag ("o <b>tr</b>em") é uma palavra só
    const tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let n;
    while ((n = tw.nextNode())) {
      // texto posto fora do fluxo (a correção escrita em cima, .corr .sobre) não é linha do bloco
      let solto = false;
      for (let a = n.parentElement; a && a !== el; a = a.parentElement) {
        const p = getComputedStyle(a).position; if (p === 'absolute' || p === 'fixed') { solto = true; break; }
      }
      if (solto) continue;
      // a linha que conta é a da quebra do texto: item em bloco ou flex (a lista de caixinhas dos Stories) é
      // uma unidade própria, e não a última linha do bloco de fora
      let c = n.parentElement;
      while (c !== el && getComputedStyle(c).display.startsWith('inline')) c = c.parentElement;
      if (!caixas.includes(c)) caixas.push(c);
      const ci = caixas.indexOf(c);
      // quebra à mão (<br>): só o último trecho entra na palavra sozinha, porque a linha curta antes de um <br> é escolha
      const seg = [...c.querySelectorAll('br')].filter(b => b.compareDocumentPosition(n) & Node.DOCUMENT_POSITION_FOLLOWING).length;
      const re = /[^\s]+/g; let m;   // \s inclui o espaço inseparável: "de IA" preso conta como duas palavras
      const colado = anterior && /\S$/.test(anterior.data) && /^\S/.test(n.data) && palavras.length &&
        palavras[palavras.length - 1].c === ci;
      anterior = n;
      while ((m = re.exec(n.data))) {
        const r = document.createRange(); r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
        const q = r.getClientRects()[0]; if (!q || q.width < .5) continue;
        const ult = palavras[palavras.length - 1];
        // continuação da palavra do nó anterior: colada a ela na mesma linha (não depois de um <br> nem de um item)
        if (m.index === 0 && colado && Math.abs(q.left - ult.dir) < 2 && Math.abs((q.top + q.bottom) / 2 - ult.y) < ult.h / 2) {
          ult.p += m[0]; ult.dir = q.right; continue;
        }
        if (!/[0-9A-Za-zÀ-ÿ]/.test(m[0])) continue;   // seta, travessão, pontuação solta
        palavras.push({p: m[0], c: ci, seg, x: q.left, dir: q.right, y: (q.top + q.bottom) / 2, h: q.height});
      }
    }
    for (let ci = 0; ci < caixas.length; ci++) {
      const ps = palavras.filter(w => w.c === ci);
      if (!ps.length) continue;
      ps.sort((a, b) => a.y - b.y || a.x - b.x);
      const linhas = [];
      for (const w of ps) {
        const l = linhas[linhas.length - 1];
        if (l && Math.abs(w.y - l.y) < 0.5 * Math.max(w.h, l.h)) l.w.push(w); else linhas.push({y: w.y, h: w.h, w: [w]});
      }
      for (const l of linhas) l.w.sort((a, b) => a.x - b.x);
      const ultimo = Math.max(...ps.map(w => w.seg));
      const doUltimo = linhas.filter(l => l.w.some(w => w.seg === ultimo)).map(l => l.w.filter(w => w.seg === ultimo).map(w => w.p));
      out.push({ultimas: doUltimo, classe: String(el.className || el.tagName.toLowerCase()), forte: el.matches('.titulo,.destaque,.citacao'),
                texto: caixas[ci].textContent.replace(/\s+/g, ' ').trim().slice(0, 50), linhas: linhas.map(l => l.w.map(w => w.p))});
    }
  }
  return out;
}"""

# O texto some, o svg fica: o svg e o que está dentro dele saem da regra do color, e a cor de cada svg é fixada antes
# (FIXAR), porque um traço em currentColor herda o color do pai, que a regra deixaria transparente (o K1 da revisão).
SEM_TEXTO = """*:not(svg):not(svg *){color:transparent!important;-webkit-text-fill-color:transparent!important;
text-shadow:none!important;text-decoration-color:transparent!important;caret-color:transparent!important}
svg text,svg tspan{fill:transparent!important;stroke:transparent!important}"""
PAPEL_FORA = r"""(idx) => {
  // as linhas do papel saem do fundo do contraste, o fundo real fica. O papel é a tela que declara --passo
  // (Tipo A e Tipo B do caderno.css, que o caderno.js lê para assentar o texto; a classe vai na própria tela): nela,
  // as camadas de gradiente do background-image são as linhas e saem; as camadas url() ficam. Tela sem --passo não é
  // papel e não perde nada: degradê e foto ficam (apagar todo background-image da tela mediria o texto sobre degradê
  // contra o fundo do body). Cada camada mantida leva junto size, position, repeat, origin,
  // clip e attachment, que no CSS são listas paralelas por camada; o inline anterior volta em PAPEL_VOLTA com a prioridade.
  const PROPS = ['background-image', 'background-size', 'background-position', 'background-repeat', 'background-origin',
                 'background-clip', 'background-attachment'];
  const sl = document.querySelectorAll('.slide')[idx]; const cs = getComputedStyle(sl);
  if (!cs.getPropertyValue('--passo').trim()) return 'sem papel';
  const parte = s => { const out = []; let d = 0, cur = '';   // separa as camadas na vírgula de fora dos parênteses
    for (const ch of s) { if (ch === '(') d++; if (ch === ')') d--; if (ch === ',' && d === 0) { out.push(cur.trim()); cur = ''; } else cur += ch; }
    out.push(cur.trim()); return out; };
  const camadas = parte(cs.backgroundImage);
  if (camadas.length === 1 && camadas[0] === 'none') return 'papel sem linhas';
  const fica = camadas.map((c, k) => c.startsWith('url(') ? k : -1).filter(k => k >= 0);
  if (fica.length === camadas.length) return 'papel sem linhas';
  sl.setAttribute('data-conf-bg', JSON.stringify(PROPS.map(p => [sl.style.getPropertyValue(p), sl.style.getPropertyPriority(p)])));
  const ou = (arr, k) => arr[k % arr.length];
  const listas = PROPS.map(p => parte(cs.getPropertyValue(p)));   // ler tudo antes de mexer: a lista computada encolhe ao trocar a imagem
  if (!fica.length) sl.style.setProperty('background-image', 'none', 'important');   // sem foto, só a imagem sai
  else PROPS.forEach((p, j) => sl.style.setProperty(p, fica.map(k => ou(listas[j], k)).join(', '), 'important'));
  return `linhas do papel fora (${camadas.length - fica.length} de ${camadas.length} camadas)`;
}"""
PAPEL_VOLTA = r"""(idx) => { const sl = document.querySelectorAll('.slide')[idx]; const v = sl.getAttribute('data-conf-bg'); if (v === null) return;
  const PROPS = ['background-image', 'background-size', 'background-position', 'background-repeat', 'background-origin',
                 'background-clip', 'background-attachment'];
  JSON.parse(v).forEach(([val, prio], k) => { sl.style.removeProperty(PROPS[k]); if (val) sl.style.setProperty(PROPS[k], val, prio); });
  sl.removeAttribute('data-conf-bg'); }"""
FIXAR = """(idx) => { for (const s of document.querySelectorAll('.slide')[idx].querySelectorAll('svg')) {
  s.dataset.corAntes = s.style.getPropertyValue('color'); s.dataset.prioAntes = s.style.getPropertyPriority('color');
  s.style.setProperty('color', getComputedStyle(s).color, 'important'); } }"""
SOLTAR = """(idx) => { for (const s of document.querySelectorAll('.slide')[idx].querySelectorAll('svg')) {
  if (s.dataset.corAntes) s.style.setProperty('color', s.dataset.corAntes, s.dataset.prioAntes);
  else s.style.removeProperty('color');
  delete s.dataset.corAntes; delete s.dataset.prioAntes; } }"""


def miolo(r):
    h = r[3] - r[1]
    return [r[0], r[1] + 0.2 * h, r[2], r[3] - 0.2 * h]


def cruza(a, b, folga=0.0):
    w = min(a[2], b[2] + folga) - max(a[0], b[0] - folga)
    h = min(a[3], b[3] + folga) - max(a[1], b[1] - folga)
    return (w, h) if w > 0 and h > 0 else None


def faixa_vazia(linhas, formas, figuras, H):
    """Maior faixa horizontal sem conteúdo entre o topo e o pé da área útil (sem a moldura). O vazio somado não
    serve: conta a entrelinha de cada parágrafo e, nas peças publicadas, foi de 24% a 81%."""
    ocup = sorted((r[1], r[3]) for r in [l["rect"] for l in linhas if not l["moldura"] and not l["adesivo"]] +
                  [f["rect"] for f in formas if "marcas" not in f["classe"].split()] + figuras)
    molduras = [l["rect"] for l in linhas if l["moldura"]]
    topo = max([r[3] for r in molduras if r[3] < H * 0.25], default=0)
    pe = min([r[1] for r in molduras if r[1] > H * 0.75], default=H)
    maior, ini, cursor = 0.0, topo, topo
    for a, b in ocup:
        a, b = max(a, topo), min(b, pe)
        if b <= cursor:
            continue
        if a > cursor and a - cursor > maior:
            maior, ini = a - cursor, cursor
        cursor = max(cursor, b)
    if pe - cursor > maior:
        maior, ini = pe - cursor, cursor
    util = max(pe - topo, 1)
    # livre: a faixa encosta na margem de cima ou de baixo da área útil; presa: entre dois elementos (D5 da rubrica de design)
    aberta = "cima" if ini <= topo + 1 else "baixo" if ini + maior >= pe - 1 else None
    return round(maior), round(ini), round(maior / util, 2), aberta


def mascara(a, b):
    import numpy as np
    return np.abs(np.asarray(a, dtype=np.int16) - np.asarray(b, dtype=np.int16)).sum(axis=2) > DIF


def cor_css(css):
    """(r, g, b), alfa de um 'rgb(...)' ou 'rgba(...)' computado; None se não for cor."""
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", css or "")
    return (tuple(float(x) for x in m.groups()[:3]), float(m.group(4) or 1)) if m else None


def luminancia(a):
    """Luminância relativa (WCAG) de um array de cores 0..255, no último eixo."""
    import numpy as np
    c = a / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def contraste_da_linha(linha, arr):
    """Mediana e p10 do contraste da cor do texto contra os pixels do fundo sob a caixa da linha (arr: a tela com o
    texto transparente, já como array). None sem pixels; "cor" se a cor computada
    não é rgb()/rgba() (a conferência não roda nessa linha, e o chamador avisa)."""
    import numpy as np
    c = cor_css(linha["cor"])
    if c is None:
        return "cor"
    # a faixa central da linha (os 60% do meio), como nas outras conferências: a caixa inteira inclui a folga da fonte
    # e, numa nota girada, a caixa reta pega o traço vizinho
    x0, y0, x1, y1 = (int(round(v)) for v in miolo(linha["rect"]))
    x0, y0, x1, y1 = max(0, x0), max(0, y0), min(arr.shape[1], x1), min(arr.shape[0], y1)
    if x1 <= x0 or y1 <= y0:
        return None
    bg = arr[y0:y1, x0:x1].reshape(-1, 3).astype(float)
    cor, alfa = c
    alfa *= linha.get("opacidade", 1) or 1
    cor = np.array(cor) * alfa + np.median(bg, axis=0) * (1 - alfa)   # a cor com transparência, composta sobre o fundo
    lt, lb = luminancia(cor[None, :])[0], luminancia(bg)
    cr = (np.maximum(lt, lb) + 0.05) / (np.minimum(lt, lb) + 0.05)
    return round(float(np.median(cr)), 2), round(float(np.percentile(cr, 10)), 2)


def minimo_de_contraste(linha):
    """4,5:1 no texto corrido; 3:1 no texto grande da rubrica de design (66 px, ou 52 em negrito)."""
    peso = str(linha.get("peso", "400"))
    negrito = peso in ("bold", "bolder") or (peso.isdigit() and int(peso) >= 700)
    grande = linha["tamanho"] >= GRANDE_REGULAR or (negrito and linha["tamanho"] >= GRANDE_NEGRITO)
    return CONTRASTE_GRANDE if grande else CONTRASTE_CORRIDO


def protegida(publicada, n):
    """A tela n conta como publicada: `publicada` é True (a peça inteira), False, ou o conjunto das telas publicadas
    (os Stories pela API, tela a tela)."""
    if isinstance(publicada, (set, frozenset)):
        return n in publicada
    return bool(publicada)


def respiro(grupos, tela):
    """"O espaço entre grupos é maior que dentro deles": o grupo é o .bloco. Os vizinhos de um bloco
    são os da mesma coluna (cruzam na horizontal em mais da metade do mais estreito), o de cima e o de baixo."""
    def coluna(a, b):
        w = min(a[2], b[2]) - max(a[0], b[0])
        return w > 0.5 * min(a[2] - a[0], b[2] - b[0])

    def vizinhos(g):
        r = g["rect"]
        cima = [o for o in grupos if o is not g and coluna(o["rect"], r) and o["rect"][3] <= r[1] + 1]
        baixo = [o for o in grupos if o is not g and coluna(o["rect"], r) and o["rect"][1] >= r[3] - 1]
        c = max(cima, key=lambda o: o["rect"][3], default=None)
        b = min(baixo, key=lambda o: o["rect"][1], default=None)
        return (c, r[1] - c["rect"][3] if c else None), (b, b["rect"][1] - r[3] if b else None)

    out = []
    for g in grupos:
        (c, vc), (b, vb) = vizinhos(g)
        fora = [v for v in (vc, vb) if v is not None]
        partes = sorted(g["partes"], key=lambda q: q["rect"][1])
        dentro = [(partes[k + 1]["rect"][1] - partes[k]["rect"][3], partes[k + 1]["texto"]) for k in range(len(partes) - 1)]
        if dentro and fora:
            vao, texto = max(dentro)
            if vao >= min(fora) - 1:
                out.append({"nivel": "AVISO", "conferencia": "respiro_grupos", "tela": tela, "texto": g["texto"],
                            "detalhe": f"dentro do bloco, {round(vao)} px antes de \"{texto}\"; até o bloco vizinho, "
                                       f"{round(min(fora))} px: o D5 pede o espaço entre grupos maior que dentro deles, "
                                       "e aqui ele não é"})
        # a fonte que é bloco próprio fica mais perto do que ela cita (o bloco de cima) que do de baixo
        if g["fonte"] and vc is not None and vb is not None and vc >= vb - 1:
            out.append({"nivel": "AVISO", "conferencia": "respiro_grupos", "tela": tela, "texto": g["texto"],
                        "detalhe": f"a fonte fica a {round(vc)} px do que ela cita (\"{c['texto']}\") e a {round(vb)} px do "
                                   f"bloco seguinte (\"{b['texto']}\"): ela vai no mesmo .bloco do que cita, ou mais perto dele (D5)"})
    return out


def fora_da_area(r, W, H, stories):
    """A faixa da interface em que a caixa de linha r entra (topo, base, esquerda, direita), ou None; 1 px de folga.
    Stories: y 192 a 1802 e x 32 a 1048. Carrossel: a área de 1000 por 1270 centrada."""
    if stories:
        x0, y0, x1, y1 = STORIES_LADO, STORIES_TOPO, W - STORIES_LADO, H - STORIES_BASE
    else:
        mx, my = (W - ZONA_CARROSSEL[0]) / 2, (H - ZONA_CARROSSEL[1]) / 2
        x0, y0, x1, y1 = mx, my, W - mx, H - my
    for nome, fora in (("base", r[3] - y1), ("topo", y0 - r[1]), ("esquerda", x0 - r[0]), ("direita", r[2] - x1)):
        if fora > 1:
            return nome, round(fora, 1)
    return None


def conferir(pasta, html, legenda=None, janela=(1280, 1560), publicada=False, exportacao=False):
    """Mede as telas com a mesma flag do navegador e a mesma janela da exportação (export_slides.py). `publicada`:
    True ou False para a peça inteira, ou o conjunto das telas (a partir de 1) já publicadas; `exportacao`: a legenda
    passa também pelas conferências que só a exportação roda (o ensaio da publicação chama a conferir_legenda sem elas)."""
    from playwright.sync_api import sync_playwright
    from PIL import Image
    import numpy as np
    achados = []
    titulos = []   # (tela, caixa, declarado, texto) para o alinhamento entre telas irmãs
    da_serie = []  # {tela, unidades, acento} das telas da série, para os AVISOs de peça (medidas_forma.py)
    isencoes = {}  # as isenções usadas, para a linha de NOTA
    travado = mf.telas_travadas(pasta)
    destaque = destaque_do_roteiro(pasta)   # o Story de Destaque leva a data (só nos Stories; o carrossel não tem roteiro.md)
    serie = mf.carregar_serie(pasta, html)     # o design/papeis.json da série, None sem ele
    tabela = mf.papeis_de(serie)               # a tabela "Letra" da série, None sem ela
    nivel_trav = mf.nivel_travessao(serie)     # ERRO se context/sobre-mim.md pede sem travessão, senão AVISO
    cor_acento = mf.acento_de(serie)           # (r, g, b) do acento da série, None sem ele
    _, teto_acento = mf.limiares_do_acento(serie)
    medir = MEDIR.replace("__CHAMADA__", str(tabela["chamada"][0] if tabela else CHAMADA_PADRAO))   # sem papeis.json, a chamada da casa
    with sync_playwright() as pw:
        br = pw.chromium.launch(args=["--disable-lcd-text"])
        page = br.new_page(viewport={"width": janela[0], "height": janela[1]})
        page.goto((pasta / html).resolve().as_uri())
        page.wait_for_load_state("load")
        total = page.locator(".slide").count()
        for i in range(total):
            prep = page.evaluate(PREPARAR, i) or {}
            page.wait_for_timeout(300)
            m = page.evaluate(medir, i)
            n, H, W = i + 1, m["h"], m["w"]
            stories = H >= 1900
            # a fonte que não carregou: a medida da tela seria da fonte de reserva
            for f in prep.get("faltam", []):
                achados.append({"nivel": "ERRO", "conferencia": "fonte_nao_carregada", "tela": n, "texto": f["amostra"],
                                "detalhe": f"{f['familia']} ({f['fonte']}) não carregou: as medidas desta tela seriam da fonte "
                                           "de reserva (a rede, para a fonte da web, ou o @font-face)"})
            # tela em vídeo: a página guia a animação por window.quadro(t, idx), e a duração cabe na API (3 a 60 s);
            # as outras conferências medem o estado parado, que é o quadro final
            v = page.evaluate("i => [document.querySelectorAll('.slide')[i].dataset.video ?? null, typeof window.quadro]", i)
            if v[0] is not None:
                try:
                    seg = float(str(v[0]).replace(",", "."))
                except ValueError:
                    seg = None
                if v[1] != "function":
                    achados.append({"nivel": "ERRO", "conferencia": "video", "tela": n,
                                    "detalhe": "a tela tem data-video, e a página não define window.quadro(t, idx)"})
                if seg is None or not (3 <= seg <= 60):
                    achados.append({"nivel": "ERRO", "conferencia": "video", "tela": n,
                                    "detalhe": f"data-video=\"{v[0]}\": a duração vai de 3 a 60 s (5 a 8 pedidos)"})
            ls = [l for l in m["linhas"] if not l["adesivo"]]
            sec = page.locator(".slide").nth(i)
            foto = lambda: Image.open(io.BytesIO(sec.screenshot(animations="disabled"))).convert("RGB")
            # regras da casa: o fundo renderizado atrás de cada linha, sem as linhas do papel e sem as marcas do
            # caderno.js (a tela com o texto transparente, as linhas do papel apagadas e o svg.marcas escondido).
            # Por quê: a linha fina do papel sob a nota derrubaria o p10 de toda nota, e o riscado sob a palavra
            # riscada é de propósito.
            page.evaluate(FIXAR, i)
            page.evaluate(PAPEL_FORA, i)
            sem_texto = page.add_style_tag(content=SEM_TEXTO + " svg.marcas{visibility:hidden!important}")
            import numpy as np
            fundo = np.asarray(foto())   # uma conversão por tela, não por linha
            page.evaluate("el => el.remove()", sem_texto)
            page.evaluate(PAPEL_VOLTA, i)
            page.evaluate(SOLTAR, i)
            por_bloco = {}   # um achado por bloco e tipo, com a pior linha: um bloco cortado tem várias linhas cortadas
            for l in ls:
                c = contraste_da_linha(l, fundo)
                if c == "cor":
                    por_bloco.setdefault(("cor_nao_lida", l["bloco"]), {"nivel": "AVISO", "conferencia": "cor_nao_lida", "tela": n,
                                         "texto": l["texto"], "detalhe": f"cor computada {l['cor']!r} não é rgb(): o contraste não foi medido"})
                elif c:
                    mediana, p10, minimo = c[0], c[1], minimo_de_contraste(l)
                    if mediana < minimo or p10 < minimo:
                        qual = "contraste" if mediana < minimo else "contraste_parcial"
                        perto = qual == "contraste_parcial" and minimo - p10 < AVISO_CONTRASTE   # a faixa é só do parcial (E2)
                        chave = (qual, l["bloco"])
                        if chave not in por_bloco or min(mediana, p10) < min(por_bloco[chave]["mediana"], por_bloco[chave]["p10"]):
                            por_bloco[chave] = {"nivel": "AVISO" if perto else "ERRO", "conferencia": qual, "tela": n,
                                                "texto": l["texto"], "mediana": mediana, "p10": p10, "minimo": minimo}
                # transbordo pela borda da tela e corte por um ancestral com overflow escondido, sem sangria declarada
                if not l["sangria"]:
                    r, cp = l["rect"], l["clip"]
                    fora = max(-r[0], -r[1], r[2] - W, r[3] - H)
                    qual = "transbordo" if fora > FORA_MIN else None
                    if not qual and cp:
                        fora = max(cp[0] - r[0], cp[1] - r[1], r[2] - cp[2], r[3] - cp[3])
                        qual = "corte" if fora > FORA_MIN else None
                    if qual:
                        chave = (qual, l["bloco"])
                        if chave not in por_bloco or fora > por_bloco[chave]["px_fora"]:
                            por_bloco[chave] = {"nivel": "ERRO", "conferencia": qual, "tela": n, "texto": l["texto"], "px_fora": round(fora, 1)}
            achados.extend(por_bloco.values())
            for c in m["corAnulada"]:
                achados.append({"nivel": "ERRO", "conferencia": "cor_anulada", "tela": n, **c})
            if m["titulo"] and n > 1 and H < 1900:   # só no carrossel: nos Stories cada tela é vista sozinha, e o título anda
                titulos.append((n, m["titulo"]["rect"], m["titulo"]["declarado"], m["titulo"]["texto"]))
            # texto × texto, de blocos diferentes
            vistos = set()
            for a_i, a in enumerate(ls):
                for b in ls[a_i + 1:]:
                    par = tuple(sorted((a["bloco"], b["bloco"])))
                    if a["bloco"] == b["bloco"] or par in vistos or a["proposito"] or b["proposito"]:
                        continue
                    c = cruza(miolo(a["rect"]), miolo(b["rect"]))
                    if c and c[0] * c[1] > AREA_TEXTO_TEXTO:
                        vistos.add(par)
                        achados.append({"nivel": "ERRO", "conferencia": "sobreposicao_texto", "tela": n,
                                        "texto": a["texto"], "elemento": b["texto"], "area_px2": round(c[0] * c[1])})
            # texto × desenho: filtro pelas caixas
            cand = []
            for f in m["formas"]:
                if f["proposito"]:
                    continue
                for l in ls:
                    if l["proposito"]:
                        continue
                    c = cruza(miolo(l["rect"]), f["rect"], f["folga"])
                    if c:
                        r1, r2 = miolo(l["rect"]), f["rect"]
                        cand.append((f["svg"], f["nome"], l, [max(r1[0], r2[0] - f["folga"]), max(r1[1], r2[1] - f["folga"]),
                                                   min(r1[2], r2[2] + f["folga"]), min(r1[3], r2[3] + f["folga"])]))
            if cand:
                ids = sorted({c[0] for c in cand})
                sel = ",".join(f'[data-conf="{s}"]' for s in ids)
                # a isenção é por forma, a camada é por svg: o traço de propósito dentro de um svg candidato some
                # das três fotos, para não somar pixels com o texto
                isentos = page.add_style_tag(content="[data-conf] .intencional,[data-conf] [data-intencional]"
                                                     "{visibility:hidden!important}")
                esconde = page.add_style_tag(content=sel + "{visibility:hidden!important}")
                com_texto_sem_desenho = foto()
                page.evaluate(FIXAR, i)
                sem_texto = page.add_style_tag(content=SEM_TEXTO)
                nada = foto()
                page.evaluate("el => el.remove()", esconde)
                so_desenho = foto()
                page.evaluate("el => el.remove()", sem_texto)
                page.evaluate(SOLTAR, i)
                page.evaluate("el => el.remove()", isentos)
                txt = mascara(com_texto_sem_desenho, nada)
                des = mascara(so_desenho, nada)
                comum = txt & des
                por_par = {}
                for sid, nome, l, r in cand:
                    x0, y0, x1, y1 = (max(0, int(v)) for v in r)
                    px = int(comum[y0:y1 + 1, x0:x1 + 1].sum())
                    chave = (sid, l["bloco"])
                    if px >= PIXELS_MIN:
                        ant = por_par.get(chave)
                        caixa = [x0, y0, x1, y1] if not ant else [min(ant[3][0], x0), min(ant[3][1], y0),
                                                                  max(ant[3][2], x1), max(ant[3][3], y1)]
                        por_par[chave] = (l["texto"], nome, (ant[2] if ant else 0) + px, caixa)
                for texto, nome, px, (x0, y0, x1, y1) in por_par.values():
                    achados.append({"nivel": "ERRO", "conferencia": "sobreposicao_desenho", "tela": n, "texto": texto,
                                    "elemento": nome, "onde": f"x {x0}..{x1}, y {y0}..{y1}", "pixels": px})
            # área ocupada, só no carrossel: nos Stories, o adesivo e o post compartilhado entram pelo app e ocupam
            # um espaço que o HTML deixa vazio de propósito
            maior, ini, frac, aberta = faixa_vazia(m["linhas"], m["formas"], m["figuras"], H)
            if not stories and frac >= VAZIO_AVISO:
                achados.append({"nivel": "AVISO", "conferencia": "area_ocupada", "tela": n,
                                "detalhe": f"faixa vazia de {maior} px a partir de y {ini} ({round(frac * 100)}% da altura útil), "
                                           + (f"livre, aberta para a margem de {aberta}: escolha se o foco a usa, defeito se sobra"
                                              if aberta else "presa entre elementos: o vazio preso é defeito (D5)")})
            # área segura dos Stories e zona proibida do carrossel; o texto que já passa da tela fica só
            # no transbordo (um defeito, não dois), e o que leva data-sangria fica de fora
            por_bloco = {}
            for l in ls:
                if l["sangria"] or (l["moldura"] and not stories) or max(-l["rect"][0], -l["rect"][1], l["rect"][2] - W, l["rect"][3] - H) > FORA_MIN:
                    continue
                f = fora_da_area(l["rect"], W, H, stories)
                if f and (("z", l["bloco"]) not in por_bloco or f[1] > por_bloco[("z", l["bloco"])]["px_fora"]):
                    # no carrossel, a regra escrita nomeia manchete, ponte e chamada: o resto (a nota, a marca de
                    # margem, o corpo) avisa, para a leitura
                    barra = stories or l["essencial"]
                    por_bloco[("z", l["bloco"])] = {
                        "nivel": "ERRO" if barra else "AVISO", "conferencia": "area_segura" if stories else "zona_proibida",
                        "tela": n, "texto": l["texto"], "faixa": f[0], "px_fora": f[1],
                        "detalhe": ("o essencial fica entre y 192 e 1802 e x 32 e 1048 (rubrica de Stories)" if stories else
                                    "manchete, ponte e chamada ficam na área de 1000 por 1270 centrada (rubrica de qualidade)"
                                    if barra else "fora da área de 1000 por 1270 centrada; a rubrica de qualidade proíbe "
                                    "só manchete, ponte e chamada ali, então a nota ou a marca de margem é leitura")}
            # o travessão, um achado por bloco, no nível que a série declara (sem declaração, AVISO)
            for l in ls:
                if nivel_trav and l["travessao"] and ("t", l["bloco"]) not in por_bloco:
                    por_bloco[("t", l["bloco"])] = {"nivel": nivel_trav, "conferencia": "travessao", "tela": n, "texto": l["travessao"],
                                                    "detalhe": "sem travessões (a voz de quem usa, em context/sobre-mim.md)"}
            # as medidas da rubrica de design sem código até aqui: a margem lateral e o piso do corpo, um achado
            # por bloco com a pior linha; a moldura fica de fora nas duas ("moldura fora"). A margem é a do texto do
            # corpo (o `body-text-viewport-edge` do Impeccable): a anotação, o texto do desenho e a marca de margem
            # moram na margem de propósito e ficam de fora (nas publicadas, todos os casos abaixo de 80 px eram deles),
            # como o que leva data-sangria e o que já passa da tela ou da caixa que corta (é transbordo ou corte, um
            # defeito e não dois). A margem só no carrossel: nos Stories, a lateral é a da área segura (x 32 a 1048,
            # rubrica de Stories), que já tem conferência (achado do /code-review)
            for l in ls:
                if l["moldura"] or abs(W - 1080) > 1:   # as duas medidas são numa tela de 1080
                    continue
                r, cp = l["rect"], l["clip"]
                cortada = bool(cp) and max(cp[0] - r[0], cp[1] - r[1], r[2] - cp[2], r[3] - cp[3]) > FORA_MIN
                if (not stories and not l["sangria"] and not l["anotacao"] and not l["svg"] and not l["marca_margem"]
                        and not cortada and max(-r[0], -r[1], r[2] - W, r[3] - H) <= FORA_MIN):
                    perto = round(min(r[0], W - r[2]), 1)
                    k = ("m", l["bloco"])
                    if perto < MARGEM_LATERAL - FORA_MIN and (k not in por_bloco or perto < por_bloco[k]["margem_px"]):
                        por_bloco[k] = {"nivel": "AVISO", "conferencia": "margem_lateral", "tela": n, "texto": l["texto"],
                                        "margem_px": perto, "lado": "esquerda" if r[0] <= W - r[2] else "direita",
                                        "detalhe": f"a margem lateral é de pelo menos {MARGEM_LATERAL} px numa tela de 1080 "
                                                   "(rubrica de design, \"Medidas\"); provisório, a calibrar"}
                tam = round(l["tamanho"] * (l.get("escala") or 1), 1)
                if l["piso"] and tam < l["piso"][1] - 0.5:
                    k = ("p", l["bloco"], l["piso"][0])   # por bloco e papel: a nota dentro do corpo tem o piso dela
                    if k not in por_bloco or tam < por_bloco[k]["tamanho_px"]:
                        por_bloco[k] = {"nivel": "AVISO", "conferencia": "texto_miudo", "tela": n, "texto": l["texto"],
                                        "tamanho_px": tam, "papel": l["piso"][0], "piso_px": l["piso"][1],
                                        "detalhe": f"os pisos: {PISOS_DETALHE} (rubrica de design, \"Medidas\"); "
                                                   "provisório, a calibrar"}
            achados.extend(por_bloco.values())
            if not stories:
                achados.extend(respiro(m["grupos"], n))
            for k, q in m["isencoes"].items():
                isencoes.setdefault(k, []).append(n)
            # os AVISOs de forma (medidas_forma.py): a ponta da seta, o papel, a imagem já publicada, o texto travado,
            # o acento e o negrito. Papel, acento, negrito e imagem só no carrossel da série: os limiares saíram dele, e
            # nos Stories o corpo vai de 40 a 46 px e a imagem do post se repete de propósito
            achados.extend(mf.pontas_das_setas(prep.get("setas", []), m, n))
            fm = page.evaluate(mf.MEDIR_FORMA, i)
            if fm["tipo"] and not stories:
                if tabela:
                    achados.extend(mf.papel_fora(fm["papeis"], fm["tipo"], n, tabela))
                # o teto de papéis por tela (rubrica de design, "Medidas"): até 4, sem rótulo, fonte e moldura
                achados.extend(mf.papeis_por_tela(fm["papeis"], n))
                # a cor fora dos tokens (D3) e os itens por grupo (D4)
                achados.extend(mf.lote5(page.evaluate(mf.MEDIR_LOTE5, i), n))
                page.evaluate(PAPEL_FORA, i)
                sem_fig = page.add_style_tag(content=mf.ESCONDER_FIGURAS)
                pct = mf.acento_pct(np.asarray(foto()), cor_acento) if cor_acento else None
                page.evaluate("el => el.remove()", sem_fig)
                page.evaluate(PAPEL_VOLTA, i)
                da_serie.append({"tela": n, "unidades": fm["unidades"], "acento": pct})
                if pct is not None and pct > teto_acento:
                    achados.append({"nivel": "AVISO", "conferencia": "acento_area", "tela": n,
                                    "detalhe": f"o acento cobre {pct:.2f}% da tela, acima de {teto_acento}%: "
                                               "a cor quente vai em pouca área"})
            for arq, outras in ([] if stories else mf.imagens_ja_publicadas(pasta, fm["imagens"])):
                achados.append({"nivel": "AVISO", "conferencia": "imagem_ja_publicada", "tela": n, "texto": arq,
                                "detalhe": f"a mesma imagem já saiu em {', '.join(outras)}: diga o motivo no refinamentos.md"})
            if n in travado:
                entram, saem = mf.diferenca_do_travado(travado[n], fm["texto"])
                if entram or saem:
                    achados.append({"nivel": "AVISO", "conferencia": "texto_fora_do_travado", "tela": n,
                                    "detalhe": (f"entram {entram[:8]}" if entram else "") + ("; " if entram and saem else "")
                                               + (f"saem {saem[:8]}" if saem else "")
                                               + ": ajuste de forma não troca palavra do texto aprovado (o texto.md; nos Stories, o roteiro.md)"})
            # D2: palavra sozinha na última linha e palavra curta no fim de linha de título, destaque e citação
            for b in page.evaluate(QUEBRAS, i):
                ls_b = b["linhas"]
                ult = b["ultimas"]  # as linhas do trecho depois do último <br> (o bloco inteiro, se não há <br>)
                if len(ult) >= 2 and len(ult[-1]) == 1:
                    achados.append({"nivel": "AVISO", "conferencia": "palavra_sozinha", "tela": n, "texto": b["texto"],
                                    "palavra": ult[-1][0], "linhas": len(ls_b)})
                if b["forte"]:
                    for k, linha in enumerate(ls_b[:-1], 1):
                        fim = re.sub(r"[^\wà-úÀ-Ú]", "", linha[-1].lower())
                        if fim in curtas(pasta, html):
                            achados.append({"nivel": "AVISO", "conferencia": "palavra_curta_no_fim", "tela": n,
                                            "texto": b["texto"], "linha": k, "fim": " ".join(linha[-3:])})
            # os adesivos e a chamada dos Stories: o tipo
            # fora da lista única (ADESIVOS, acima), o texto sob a caixa do adesivo simulado e a caixa fora
            # da área segura (a metade direita avança, o pé tem a caixa de resposta; rubrica de Stories, "Onde vive uma
            # sequência", e stories-o-que-evitar.md, item 5), a chamada que o app não deixa cumprir e, no Story de
            # Destaque, o quando sem a data. Os quatro primeiros são AVISO; o último, ERRO
            if stories:
                ad = page.evaluate(ADESIVO, i)
                fora_da_lista = [t for t in ad["tipos"] if t not in de_stories("ADESIVOS")]
                if fora_da_lista:
                    achados.append({"nivel": "AVISO", "conferencia": "adesivo_desconhecido", "tela": n,
                                    "texto": " ".join(fora_da_lista),
                                    "detalhe": "fora da lista de tipos (ADESIVOS, no conferir_telas.py da visual-form): "
                                               "a prévia não o reconhece"})
                cx = ad["caixa"]
                if cx:
                    sob = {}
                    for l in ls:
                        if l["proposito"] or l["bloco"] in sob:
                            continue
                        c = cruza(miolo(l["rect"]), cx)
                        if c and c[0] * c[1] > AREA_TEXTO_TEXTO:
                            sob[l["bloco"]] = {"nivel": "AVISO", "conferencia": "texto_sob_adesivo", "tela": n, "texto": l["texto"],
                                               "adesivo": " ".join(ad["tipos"]), "caixa": cx,
                                               "detalhe": "o texto se compõe acima do adesivo (rubrica de Stories); se o "
                                                          "adesivo vai em outro lugar no app, declare --adesivo-top na tela"}
                    achados.extend(sob.values())
                    fora = [nome for nome, d in (("esquerda", STORIES_LADO - cx[0]), ("topo", STORIES_TOPO - cx[1]),
                                                 ("direita", cx[2] - (W - STORIES_LADO)), ("base", cx[3] - (H - STORIES_BASE)))
                            if d > FORA_MIN]
                    if fora:
                        achados.append({"nivel": "AVISO", "conferencia": "adesivo_na_borda", "tela": n,
                                        "adesivo": " ".join(ad["tipos"]), "caixa": cx, "faixa": ", ".join(fora),
                                        "detalhe": "a caixa do adesivo sai da área segura (x 32 a 1048, y 192 a 1802): um "
                                                   "toque na metade direita avança o Story, e o pé tem a caixa de resposta"})
                for a in chamadas_da_tela(m["texto"], ad["tipos"]):
                    achados.append(dict(a, tela=n))
                if destaque:
                    quando = destaque_sem_data(m["texto"])
                    if quando:
                        achados.append({"nivel": "ERRO", "conferencia": "destaque_sem_data", "tela": n, "texto": ", ".join(quando),
                                        "detalhe": "o roteiro.md declara destaque: true, e no Destaque o dia da semana e a "
                                                   "hora viram um dia qualquer: a tela que diz quando leva a data "
                                                   "(\"terça, 25/11, 18h\"), ou não diz quando (stories/README.md)"})
            # referência relativa de dia, na tela
            for w in achar_dia(m["texto"]):
                achados.append({"nivel": "AVISO", "conferencia": "dia_relativo", "tela": n, "texto": w})
        br.close()
    achados.extend(mf.avisos_da_peca(da_serie, mf.limiares_do_acento(serie)[0]))
    # alinhamento do título entre telas irmãs (fora a capa): a moda do topo e da esquerda
    if len(titulos) >= 3:
        from collections import Counter
        for eixo, k in (("topo", 1), ("esquerda", 0)):
            comuns = Counter(round(t[1][k]) for t in titulos).most_common()
            moda, quantos = comuns[0]
            if quantos < 2:
                continue
            empate = [str(pos) for pos, q in comuns if q == quantos]
            if len(empate) > 1:   # empate: não há posição que as irmãs repetem
                achados.append({"nivel": "AVISO", "conferencia": "alinhamento_titulo", "tela": "todas", "eixo": eixo,
                                "detalhe": f"sem moda: {quantos} telas em cada uma de {', '.join(empate)}; escolher uma posição"})
                continue
            for n, r, declarado, texto in titulos:
                d = round(r[k]) - moda
                if abs(d) <= TOL_ALINHA or (declarado and abs(d) > DESVIO_ESCOLHA):   # a escolha declarada só vale acima de 100 px
                    continue
                achados.append({"nivel": "ERRO", "conferencia": "alinhamento_titulo", "tela": n,
                                "texto": texto, "eixo": eixo, "valor": round(r[k]), "moda": moda, "desvio_px": d,
                                "detalhe": "acima de 100 px pode ser escolha: declare com data-alinhamento no título"
                                if abs(d) > DESVIO_ESCOLHA else "alinhar à posição das telas irmãs"})
    # tela já publicada: o que já foi ao ar não barra a versão nova (como as hashtags); nos Stories pela API, tela a tela
    for a in achados:
        if a["nivel"] == "ERRO" and a["conferencia"] in PUBLICADA_AVISA and isinstance(a["tela"], int) and protegida(publicada, a["tela"]):
            a["nivel"] = "AVISO"
            a["detalhe"] = (a.get("detalhe", "") + "; " if a.get("detalhe") else "") + (
                "peça já publicada, fica como está" if publicada is True else "tela já publicada, fica como está")
    inteira = publicada is True or (isinstance(publicada, (set, frozenset)) and set(range(1, total + 1)) <= publicada)
    if legenda is not None:
        achados += conferir_legenda(legenda, inteira, exportacao=exportacao, travessao=nivel_trav)
    if isencoes:   # a linha de NOTA: o escape usado fica no registro, sem nível de defeito
        achados.append({"nivel": "NOTA", "conferencia": "isencoes", "tela": "todas",
                        "detalhe": "; ".join(f"{k} nas telas {v}" for k, v in sorted(isencoes.items()))})
    return achados


def conferir_legenda(legenda, publicada=False, exportacao=False, travessao="AVISO"):
    """Hashtags e dia relativo na legenda; a mesma função serve à exportação e ao ensaio da publicação. Com
    `exportacao` (só a slides-export), também o travessão (no nível `travessao`, o de mf.nivel_travessao: ERRO quando a
    voz de quem usa pede texto sem travessão; None o desliga; AVISO na publicada), o caractere
    invisível e a primeira frase depois do corte do feed (AVISOs):
    o ensaio da publicação segue sem eles, sem barrar nem gravar aviso novo na legenda.md."""
    achados = []
    if exportacao:
        trav = TRAVESSAO.findall(legenda) if travessao else []
        if trav:
            achados.append({"nivel": "AVISO" if publicada else travessao, "conferencia": "travessao", "tela": "legenda",
                            "detalhe": f"{len(trav)} travessão(ões) na legenda: sem travessões (a voz de quem usa, em context/sobre-mim.md)"
                                       + ("; peça já publicada, fica como está" if publicada else "")})
        achados += mf.conferir_legenda_exportacao(legenda)
    hs = re.findall(r"(?<![\w&/])#(?=\w*[^\W\d_])\w+", legenda)  # ao menos uma letra: "#1" não conta
    if len(hs) > MAX_HASHTAGS:
        achados.append({"nivel": "AVISO" if publicada else "ERRO", "conferencia": "hashtags", "tela": "legenda",
                        "detalhe": f"{len(hs)} hashtags, limite {MAX_HASHTAGS}"
                                   + ("; peça já publicada, fica como está" if publicada else "")})
    # a lista de palavras só serve a um aviso: se ela não for lida, a conta de hashtags, que barra, continua valendo
    try:
        dias = achar_dia(legenda)
    except Exception as e:
        return achados + [{"nivel": "AVISO", "conferencia": "dia_relativo", "tela": "legenda",
                           "detalhe": f"lista de palavras não lida ({type(e).__name__}: {e})"}]
    for w in dias:
        achados.append({"nivel": "AVISO", "conferencia": "dia_relativo", "tela": "legenda", "texto": w})
    return achados


def achar_dia(texto):
    t, out = (texto or "").lower(), []
    for w in palavras_do_dia():
        if re.search(rf"(?<![\wà-ú]){re.escape(w)}(?![\wà-ú])", t):
            out.append(w)
            t = re.sub(rf"(?<![\wà-ú]){re.escape(w)}(?![\wà-ú])", " ", t)  # "hoje à noite" não conta de novo como "hoje"
    return out


def texto_da_legenda(md):
    """O texto que vai ao ar: as seções "Legenda (final)" e "Hashtags" da legenda.md. Se a publicação vier a ler a
    legenda com outros títulos, mudar aqui também."""
    s = md.replace("\r\n", "\n")

    def secao(titulo):
        m = re.search(r"^## " + re.escape(titulo) + r"\s*\n(.*?)(?=^## |\Z)", s, re.S | re.M)
        return m.group(1).replace("\n---\n", "\n").strip() if m else None

    partes = [x for x in (secao("Legenda (final)"), secao("Hashtags")) if x]
    return "\n\n".join(partes) if partes else None


def publicada(md):
    """A legenda.md marca a peça como publicada: rótulo **Publicado:** com conteúdo, gravado pela publicação ou à
    mão, para a peça publicada pelo app."""
    # [ \t]* e não \s*: o \s engoliria a quebra de linha e leria a linha seguinte como o conteúdo (a legenda com
    # "**Publicado:**" vazio sairia como publicada)
    m = re.search(r"^\*\*Publicado:\*\*[ \t]*(.*)$", md.replace("\r\n", "\n"), re.M)
    return bool(m and m.group(1).strip())


# a tabela que a publicação dos Stories pela API grava na seção "## Publicado" do roteiro.md: a frase "Publicada pela
# API" e o cabeçalho com as colunas "tipo" e "link", que só ela grava; o número do Story e o id que a publicação
# devolveu. A ligação pela imagem e a ligação à mão gravam "| Story | id na API | publicado |", sem as duas colunas:
# a coluna "id na API" sozinha não separa uma da outra. Quem publicar os Stories pela API grava neste formato.
SECAO_PUBLICADO = re.compile(r"(?m)^## Publicado[ \t]*$")
LINHA_DA_API = re.compile(r"^\|\s*(\d+)[^|]*\|\s*(\d{15,})\s*\|", re.M)
CABECALHO_DA_API = "| Story | id na API | publicado | tipo | link |\n|---|---|---|---|---|\n"
INTRO_DA_API = "Publicada pela API, na ordem; os ids vêm da publicação.\n\n"
ESTAGIOS_PUBLICADOS = ("publicado", "medido")


def tabela_da_api(roteiro):
    """{Story: id} da tabela "Publicada pela API" do roteiro.md, ou None quando o roteiro não tem essa tabela (a
    sequência que saiu pelo app, ou a que ainda não saiu). Reconhece-se pela frase "Publicada pela API" ou pelo
    cabeçalho com "tipo" e "link", que só a publicação pela API grava. A tabela da ligação pela imagem e a ligada à
    mão, que também têm a coluna "id na API", não contam: não protegem tela a tela."""
    s = (roteiro or "").replace("\r\n", "\n")
    m = SECAO_PUBLICADO.search(s)
    if not m:
        return None
    j = s.find("\n## ", m.end())
    secao = s[m.end():j if j >= 0 else len(s)]
    if "Publicada pela API" not in secao and CABECALHO_DA_API.split("\n", 1)[0] not in secao:
        return None
    return {int(n): i for n, i in LINHA_DA_API.findall(secao)} or None


def publicada_do_roteiro(roteiro):
    """O que o roteiro.md diz que já foi ao ar: o conjunto dos Stories com linha na tabela da API, quando ela existe (vale a tabela, não o estagio: a coleta marca
    publicado também a rodada que parou no meio); senão, True com estagio publicado ou medido, e False no resto."""
    t = tabela_da_api(roteiro)
    if t is not None:
        return frozenset(t)
    fm = re.match(r"---\n(.*?)\n---", (roteiro or "").replace("\r\n", "\n"), re.S)
    est = re.search(r"""^estagio:\s*["']?([A-Za-z-]+)""", fm.group(1), re.M) if fm else None
    return bool(est and est.group(1).lower() in ESTAGIOS_PUBLICADOS)


def id_do_objeto(chave):
    """O id do Story pelo nome do objeto em stories/publicado/<dia>/: <id>.jpg, <id>.mp4 ou <id>-miniatura.jpg (o Story
    com música guarda só a miniatura), sem a extensão e sem o sufixo, senão todo Story com música parece fora da tabela."""
    nome = chave.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    return nome[:-len("-miniatura")] if nome.endswith("-miniatura") else nome


def relatorio(achados):
    """As linhas do relatório, uma por achado, e o resumo; usadas aqui e no export_slides.py. A NOTA (as isenções
    usadas) sai por último e não conta como aviso."""
    linhas = []
    for a in sorted(achados, key=lambda x: x["nivel"] == "NOTA"):
        resto = " | ".join(f"{k} {v}" for k, v in a.items() if k not in ("nivel", "conferencia", "tela"))
        linhas.append(f"[{a['nivel']}] tela {a['tela']} {a['conferencia']}: {resto}")
    erros = sum(a["nivel"] == "ERRO" for a in achados)
    avisos = sum(a["nivel"] == "AVISO" for a in achados)
    return linhas, f"{erros} erro(s), {avisos} aviso(s)"


def uso(msg="uso: python conferir_telas.py <pasta> [arquivo.html] [--legenda <caminho>] [--json]"):
    """Erro de uso ou arquivo que não existe: código 2, para não se confundir com o 1 do ERRO."""
    print(msg, file=sys.stderr)
    sys.exit(2)


def main():
    pos = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = [a for a in sys.argv[1:] if a.startswith("--")]
    leg_arg = None
    if "--legenda" in sys.argv:
        k = sys.argv.index("--legenda")
        if k + 1 >= len(sys.argv) or sys.argv[k + 1].startswith("--"):
            uso()
        leg_arg = sys.argv[k + 1]
        pos.remove(leg_arg)
    if not 1 <= len(pos) <= 2 or set(opts) - {"--legenda", "--json"}:
        uso()
    sys.stdout.reconfigure(encoding="utf-8")
    pasta = Path(pos[0]).resolve()
    html = pos[1] if len(pos) > 1 else ("slides.html" if (pasta / "slides.html").is_file() else "stories.html")
    if not (pasta / html).is_file():
        uso(f"não encontrei {pasta / html}")
    if leg_arg and not Path(leg_arg).is_file():
        uso(f"não encontrei a legenda {Path(leg_arg).resolve()} (o --legenda é lido a partir do diretório atual; "
                 "sem ele, vale a legenda.md da pasta da peça)")
    leg_path = Path(leg_arg) if leg_arg else pasta / "legenda.md"
    md = leg_path.read_text(encoding="utf-8") if leg_path.is_file() else ""
    legenda = texto_da_legenda(md) if md else None
    # o que já foi ao ar: o carrossel inteiro pela legenda.md; os Stories pela tabela da API, tela a tela, ou pelo
    # estagio. Rodado sozinho, não consulta o bucket
    rot = pasta / "roteiro.md"
    pub = publicada(md) or (publicada_do_roteiro(rot.read_text(encoding="utf-8")) if rot.is_file() else False)
    achados = conferir(pasta, html, legenda, publicada=pub, exportacao=True)
    if "--json" in opts:
        print(json.dumps(achados, ensure_ascii=False, indent=1))
    else:
        linhas, resumo = relatorio(achados)
        print("\n".join(linhas + [f"{html}: {resumo}" + ("" if legenda is not None else "; sem legenda")]))
    sys.exit(1 if any(a["nivel"] == "ERRO" for a in achados) else 0)


if __name__ == "__main__":
    main()
