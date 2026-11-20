"""Os AVISOs de forma do conferir_telas.py que pedem olhar, todos provisórios até calibrar com peças rotuladas da série:
nenhum barra o --upload. Cada limiar diz de onde saiu; os de partida se trocam pelos da série no design/papeis.json.

- papel_fora_da_tabela: o corpo, a entrelinha e o peso computados de cada bloco com classe de papel contra a tabela
  "Letra" do design system da série (o design/papeis.json; a nota no corpo da chamada é a chamada), no papel da tela
  (tipo-a ou tipo-b), com 1 px de tolerância; e mais de um tamanho por papel na mesma tela. Só no carrossel da série
  (tipo-a, tipo-b; nos Stories o corpo tem a faixa própria do README). O desvio declarado no refinamentos.md também
  dispara, e deve: o aviso sai com o desvio ao lado, para a leitura.
- corpo_sem_negrito (por peça): a fração das telas com corpo ou item de lista que levam algum negrito abaixo de 25%.
  Por bloco não separa (um corpo longo sem negrito pode estar certo), por isso a conta é da peça; e só a partir de
  quatro telas com corpo, porque com menos a conta não diz nada.
- acento_area: a fração dos pixels perto da cor do acento que a série declara (com um filtro de croma), na tela com as
  fotos e imagens escondidas e as linhas do papel fora. Por peça, a média abaixo do piso avisa (falta a marca à mão);
  por tela, acima do teto (cor quente em área demais). Os pontos de partida, 0,41% e 1,4%, se trocam pelos medidos nas
  publicadas da série ("limiares" no papeis.json). Sem a cor declarada, não roda.
- imagem_ja_publicada: o SHA-256 de cada imagem da tela (img e url() de fundo) contra as das peças publicadas, só as
  que moram na pasta da peça publicada (o kit da série, fora das pastas das peças, não conta): nenhum desenho repetido
  de uma peça publicada sem o motivo dito.
- texto_fora_do_travado: as palavras visíveis de cada tela (fora a moldura e a palavra riscada da correção) contra as
  da tela no texto.md travado; um aviso por tela, com o que entra e o que sai. "Ajuste de forma não troca palavra do
  texto aprovado."
- ponta_da_seta (toda linha termina em algo; a ponta da seta entra no alvo, de 20 a 30 px): a ponta de cada seta livre
  do desenho (path.seta-livre) que não cai nem encosta (12 px) em nenhum alvo (forma do svg que não é seta, foto,
  imagem, folha que espia) nem fica perto de texto (40 px) termina no vazio; a seta de anotação (a que sai de uma nota,
  rótulo ou legenda) que cai num alvo largo e entra menos de 20 px, mal entra. O conector entre dois desenhos só
  precisa encostar. O alvo se mede pela caixa, então a profundidade é aproximada: é aviso, e o zoom das juntas
  (juntas.py, da object-anatomy) mostra a ponta a 4×.
- Na legenda, só na exportação: caractere_invisivel (espaço de largura zero, hífen suave, marca de direção, caractere
  de tag, espaço sem quebra) e primeira_frase_legenda, a primeira frase que passa do corte do feed (cerca de 125
  caracteres, número aproximado e ainda sem fonte que o confirme). Avisa a partir de 110: a margem de 15 é de partida,
  a calibrar. A fonte fala da primeira linha; o código mede a primeira frase (até o primeiro ponto ou a primeira
  quebra), no lugar dela.

- cor_fora_dos_tokens (D3) e itens_por_grupo (D4), só nas telas da série: a cor computada (texto, fundo, borda, traço e
  preenchimento do svg) fora das cores das propriedades --* da página, com a imagem e a foto colada (.foto) fora; e a
  lista (ul, ol) com mais de quatro itens, fora as listas que o design system libera (a lista de pendências,
  .pendentes, e a linha do tempo, .linha-tempo).
- papeis_por_tela, só nas telas da série: mais de 4 papéis tipográficos de conteúdo na tela (PAPEIS_TETO), pela classe
  (CLASSE_PAPEL), com o rótulo (.rot, .leg, a anotação de diagrama), a fonte (.fonte, metadado) e a moldura fora.

Fica de fora, com o motivo: tela_sem_dominante, porque nenhum limiar de altura absoluta separou a tela fraca das boas
(a falta era o traço fino e o tamanho relativo à tela-par, que a I2 lê).
"""
import functools
import hashlib
import json
import re
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[4]

# O que a série declara para as conferências mora no design/papeis.json dela, ao lado do caderno.css que a página
# carrega, e não aqui: a tabela "Letra" do design system (papel -> corpo no A, entrelinha no A, corpo no B, entrelinha
# no B, peso), a cor do acento e os limiares do acento. O nível do travessão vem da voz de quem usa
# (context/sobre-mim.md, nivel_travessao). O teste_papeis.py confere que a tabela do
# JSON e a do design-system.md dizem o mesmo. Sem o arquivo, nada disso roda (ausente não é zero).
def pasta_do_caderno(post, html="slides.html"):
    """A pasta design/ da série, pelo caderno.js ou pelo caderno.css que a própria página carrega; None sem eles."""
    p = Path(post) / html
    if not p.is_file():
        return None
    texto = p.read_text(encoding="utf-8")
    for m in re.finditer(r'(?:src|href)="([^"]*caderno\.(?:js|css))"', texto):
        alvo = (Path(post) / unquote(m.group(1))).resolve()
        if alvo.is_file():
            return alvo.parent
    return None


@functools.lru_cache(maxsize=None)
def _ler_serie(caminho):
    return json.loads(Path(caminho).read_text(encoding="utf-8"))


def carregar_serie(post, html="slides.html"):
    """O design/papeis.json da série que a página carrega, como dicionário; None sem ele."""
    pasta = pasta_do_caderno(post, html)
    if pasta is None or not (pasta / "papeis.json").is_file():
        return None
    return _ler_serie(str(pasta / "papeis.json"))


def papeis_de(serie):
    """{papel: (corpo A, entrelinha A, corpo B, entrelinha B, peso)} da série; None sem a tabela."""
    if not serie or not serie.get("papeis"):
        return None
    return {k: tuple(v) for k, v in serie["papeis"].items()}


def carregar_papeis(post, html="slides.html"):
    """A tabela "Letra" da série que a página carrega (papeis_de); None sem o papeis.json."""
    return papeis_de(carregar_serie(post, html))


def acento_de(serie):
    """(r, g, b) da cor do acento que a série declara ("acento": "#RRGGBB"); None sem ela (o acento_area não roda)."""
    c = (serie or {}).get("acento")
    if not isinstance(c, str) or not re.fullmatch(r"#[0-9A-Fa-f]{6}", c):
        return None
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


def limiares_do_acento(serie):
    """(piso da peça, teto da tela), em % da área da tela: os que a série declara em "limiares", ou os de partida."""
    lim = (serie or {}).get("limiares") or {}
    return (float(lim.get("acento_piso_peca", ACENTO_PISO_PECA)), float(lim.get("acento_teto_tela", ACENTO_TETO_TELA)))


# A voz de quem usa pede texto sem travessão? O mesmo critério do voz_pede_sem_travessao() do export_slides.py da
# slides-export (não se importa de lá, porque a exportação importa esta conferência): "sem travessão", "nada de
# travessão", "evite o travessão", "nunca use travessão", "o travessão é proibido"; o roteiro em branco, que só pergunta
# "se o travessão é proibido", não conta. Quem mudar um muda o outro.
VOZ_SEM_TRAVESSAO = re.compile(r"(sem|nada de|evit\w*|(nunca|n[aã]o)( use| usa| usar| uso)?)\s+(o |os |de )?travess"
                               r"|(?<!se o )travess\w*\s+(é|e|são|sao|fica|ficam)\s+(proibid|fora)", re.I)


def voz_pede_sem_travessao(raiz=ROOT):
    """A voz de quem usa (context/sobre-mim.md) pede texto sem travessão? None sem o arquivo."""
    arq = Path(raiz) / "context" / "sobre-mim.md"
    if not arq.is_file():
        return None
    return bool(VOZ_SEM_TRAVESSAO.search(arq.read_text(encoding="utf-8")))


def nivel_travessao(serie=None, raiz=ROOT):
    """O nível do travessão: ERRO quando a voz de quem usa pede texto sem travessão; senão (sem o arquivo, ou sem a
    regra escrita nele), AVISO: a conferência não inventa regra que a voz não tem. `serie` fica pela assinatura."""
    return "ERRO" if voz_pede_sem_travessao(raiz) else "AVISO"
# classe -> papel, na ordem em que se decide (a .margem e o .rot são a nota à margem e o rótulo, no corpo da nota)
CLASSE_PAPEL = (("citacao", "citacao"), ("titulo", "titulo"), ("destaque", "destaque"), ("nota", "nota"),
                ("margem", "nota"), ("fila", "fila"), ("link", "link"), ("apoio", "apoio"), ("fonte", "fonte"),
                ("corpo", "corpo"))
TOL_PAPEL = 1.0
NEGRITO_PISO = 0.25
NEGRITO_MIN_TELAS = 4        # peça com menos telas de corpo não tem conta que diga alguma coisa
ACENTO_RAIO = 60             # distância de cor (soma quadrática dos canais) até a cor do acento da série
ACENTO_PISO_PECA = 0.41      # % da área da tela, média da peça: ponto de partida, a calibrar com as publicadas da série
ACENTO_TETO_TELA = 1.4       # % da área de uma tela: idem
SETA_ENTRA_MIN = 20          # px que a ponta entra no alvo (de 20 a 30)
SETA_TEXTO_PERTO = 40        # px: a ponta perto de uma linha de texto aponta o texto (a sobreposição confere a letra)
SETA_ENCOSTA = 12            # px: a ponta a até isto da caixa de um alvo encosta nele (o conector, a linha fina)
CORTE_LEGENDA = 125          # caracteres antes do "mais" no feed (aproximação do autor; a apurar)
CORTE_MARGEM = 15            # margem de partida (a fonte pede margem sem dar número), a calibrar
INVISIVEIS = re.compile("[​‌‍⁠﻿­‎‏‪-‮⁦-⁩᠎ "
                        "\U000e0000-\U000e007f]")

ESCONDER_FIGURAS = (".slide img,.slide .foto,.slide picture,.slide video,.slide canvas{visibility:hidden!important}"
                    ".slide .folha-a,.slide .folha-b{background-image:none!important}")

MEDIR_FORMA = r"""(idx) => {
  const sl = document.querySelectorAll('.slide')[idx];
  const tipo = sl.classList.contains('tipo-a') ? 'a' : sl.classList.contains('tipo-b') ? 'b' : null;
  const fora = e => !!e.closest('svg,.sim,[data-adesivo-sim]');
  const vis = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
                     return r.width > 1 && r.height > 1 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const PAPEL = """ + "[" + ",".join(f"['{c}','{p}']" for c, p in CLASSE_PAPEL) + "]" + r""";
  const papeis = [];
  if (tipo) for (const el of sl.querySelectorAll(PAPEL.map(x => '.' + x[0]).join(','))) {
    if (fora(el) || !vis(el) || !el.textContent.trim()) continue;
    const par = PAPEL.find(x => el.classList.contains(x[0])); const cs = getComputedStyle(el);
    // a moldura não conta na contagem de papéis (rubrica de design; o mesmo filtro do conta_papeis.py)
    papeis.push({papel: par[1], classe: par[0], moldura: !!el.closest('.moldura,.pagina,.arroba'), tamanho: parseFloat(cs.fontSize), entrelinha: parseFloat(cs.lineHeight) || null,
                 peso: cs.fontWeight === 'bold' ? 700 : parseInt(cs.fontWeight) || 400, texto: el.textContent.replace(/\s+/g, ' ').trim().slice(0, 40)});
  }
  // negrito: cada .corpo sem li dentro e cada li
  const pesoDe = el => { const w = getComputedStyle(el).fontWeight; return w === 'bold' ? 700 : parseInt(w) || 400; };
  const unidades = [];
  const add = el => {
    if (fora(el) || !vis(el)) return;
    let txt = '', negrito = false;
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let m;
    while ((m = w.nextNode())) { txt += m.textContent + ' '; if (m.textContent.trim() && pesoDe(m.parentElement) >= 700) negrito = true; }
    const palavras = (txt.match(/[0-9A-Za-zÀ-ÿ][^\s]*/g) || []).length;
    if (palavras) unidades.push({palavras, negrito});
  };
  if (tipo) {
    for (const el of sl.querySelectorAll('.corpo')) if (!el.querySelector('li')) add(el);
    for (const el of sl.querySelectorAll('li')) if (!el.querySelector('li')) add(el);
  }
  // imagens: img e url() de fundo
  const imagens = new Set();
  for (const e of [sl, ...sl.querySelectorAll('*')]) {
    if (e.tagName === 'IMG' && (e.currentSrc || e.src)) imagens.add(e.currentSrc || e.src);
    const bg = getComputedStyle(e).backgroundImage;
    for (const u of bg.matchAll(/url\("?([^")]+)"?\)/g)) imagens.add(u[1]);
  }
  // o texto da tela para o travado: fora a moldura, o adesivo, as marcas e a palavra riscada da correção
  let texto = '';
  const tw = document.createTreeWalker(sl, NodeFilter.SHOW_TEXT); let n;
  while ((n = tw.nextNode())) {
    const pe = n.parentElement; if (!n.textContent.trim() || pe.closest('style,script,title,desc')) continue;
    if (pe.closest('.moldura,.pagina,.arroba,.pager,.sim,[data-adesivo-sim],svg.marcas')) continue;
    if (pe.closest('.corr') && !pe.closest('.sobre')) continue;
    const cs = getComputedStyle(pe); if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    texto += ' ' + n.textContent;
  }
  return {tipo, papeis, unidades, imagens: [...imagens], texto};
}"""


def palavras(s):
    s = unescape(s or "").lower().replace("’", "'").replace("‑", "-")
    return re.findall(r"[0-9a-zà-öø-ÿ]+(?:['-][0-9a-zà-öø-ÿ]+)*", s)


def caminho_de(url):
    """O arquivo local de uma URL file:// (None para o resto)."""
    u = urlparse(url)
    if u.scheme != "file":
        return None
    p = unquote(u.path)
    if re.match(r"^/[A-Za-z]:", p):
        p = p[1:]
    return Path(p)


@functools.lru_cache(maxsize=None)
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def pecas_publicadas(raiz=ROOT):
    """As pastas dos carrosséis publicados (**Publicado:** na legenda.md), com o HTML de cada um. Só o carrossel: a
    regra é a da I1 ("nenhum desenho repetido da semana anterior sem motivo dito"), e o Story que antecipa ou
    compartilha um post repete a imagem dele de propósito."""
    out = []
    for leg in sorted((raiz / "marketing/social-media/carousels").rglob("legenda.md")):
        md = leg.read_text(encoding="utf-8").replace("\r\n", "\n")
        if re.search(r"^\*\*Publicado:\*\*[ \t]*\S", md, re.M) and (leg.parent / "slides.html").is_file():
            out.append((leg.parent, leg.parent / "slides.html"))
    return out


@functools.lru_cache(maxsize=None)
def indice_publicadas(raiz=ROOT):
    """{sha256: [nome da peça]} das imagens que moram na pasta de uma peça publicada e que o HTML dela usa."""
    idx = {}
    for pasta, html in pecas_publicadas(raiz):
        h = re.sub(r"<script\b.*?</script>", " ", html.read_text(encoding="utf-8"), flags=re.S)
        refs = re.findall(r"""\bsrc\s*=\s*["']([^"']+)["']""", h) + re.findall(r"""url\(\s*["']?([^"')]+)["']?\s*\)""", h)
        for r in refs:
            if r.startswith(("#", "data:", "http")) or not re.search(r"\.(png|jpe?g|webp|gif|svg)$", r, re.I):
                continue
            f = (html.parent / unescape(r)).resolve()
            if f.is_file() and f.is_relative_to(pasta.resolve()):
                idx.setdefault(sha(f), []).append(pasta.name)
    return idx


def imagens_ja_publicadas(pasta, imagens, raiz=ROOT):
    """[(arquivo, [peças])] das imagens desta tela que já saíram noutra peça publicada."""
    out, idx, aqui = [], indice_publicadas(raiz), pasta.resolve().name
    for u in imagens:
        f = caminho_de(u)
        if f is None or not f.is_file():
            continue
        outras = sorted({p for p in idx.get(sha(f), []) if p != aqui})
        if outras:
            out.append((f.name, outras))
    return out


def _limpa(linhas):
    s = " ".join(linhas)
    return re.sub(r"\*\((?:[^()]|\([^()]*\))*\)\*", " ", s).replace("==", " ").replace("**", " ").replace("·", " ")


def stories_travados(pasta):
    """{story: texto} da seção "## Os Stories" do roteiro.md (as linhas "> " de cada "N. **...**", sem as notas de
    produção entre *( )*): o texto dos Stories, que não têm texto.md."""
    p = pasta / "roteiro.md"
    if not p.is_file():
        return {}
    texto = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.search(r"^## Os Stories\s*$(.*?)(?=^## |\Z)", texto, re.M | re.S)
    if not m:
        return {}
    return {int(s.group(1)): _limpa([l[2:] for l in s.group(2).splitlines() if l.startswith("> ")])
            for s in re.finditer(r"^(\d+)\. \*\*[^\n]*\n(.*?)(?=^\d+\. \*\*|\Z)", m.group(1), re.M | re.S)}


def telas_travadas(pasta):
    """{tela: texto} do texto.md travado (os blocos "> " de cada "**Tela N, ...**" da seção "## As telas"); sem
    texto.md, o dos Stories pelo roteiro.md (stories_travados)."""
    p = pasta / "texto.md"
    if not p.is_file():
        return stories_travados(pasta)
    texto = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.search(r"^## As telas\s*$(.*?)(?=^## |\Z)", texto, re.M | re.S)
    corpo = m.group(1) if m else texto
    telas = {}
    for t in re.finditer(r"^\*\*Tela (\d+),[^\n]*\n(.*?)(?=^\*\*Tela |^## |\Z)", corpo, re.M | re.S):
        linhas = [l[2:] for l in t.group(2).splitlines() if l.startswith("> ")]
        s = " ".join(linhas)
        s = re.sub(r"\*\((?:[^()]|\([^()]*\))*\)\*", " ", s).replace("==", " ").replace("**", " ").replace("·", " ")
        telas[int(t.group(1))] = s
    return telas


def diferenca_do_travado(travado, visivel):
    """(entram, saem): as palavras da tela que o texto travado não tem, e as do travado que a tela não mostra. Conta a
    palavra, não as vezes: o ano que o título diz e o rótulo de um desenho repete não é palavra nova."""
    a, b = set(palavras(visivel)), set(palavras(travado))
    return sorted(a - b), sorted(b - a)


def papel_fora(papeis, tipo, tela, tabela):
    """Os AVISOs papel_fora_da_tabela de uma tela da série, contra a tabela do papeis.json dela (carregar_papeis)."""
    out, tamanhos = [], {}
    chamada = tabela["chamada"]
    for p in papeis:
        if p["papel"] == "nota" and abs(p["tamanho"] - chamada[0]) <= TOL_PAPEL:
            p = dict(p, papel="chamada")   # a chamada é a nota no corpo dela (46/72), como "Segue o perfil" nas peças
        alvo = tabela[p["papel"]]
        t, e = (alvo[0], alvo[1]) if tipo == "a" else (alvo[2], alvo[3])
        tamanhos.setdefault(p["papel"], set()).add(round(p["tamanho"]))
        dif = []
        if abs(p["tamanho"] - t) > TOL_PAPEL:
            dif.append(f"corpo {p['tamanho']:g} px (a tabela: {t})")
        if p["entrelinha"] and abs(p["entrelinha"] - e) > TOL_PAPEL:
            dif.append(f"entrelinha {p['entrelinha']:g} (a tabela: {e})")
        if p["peso"] != alvo[4]:
            dif.append(f"peso {p['peso']} (a tabela: {alvo[4]})")
        if dif:
            out.append({"nivel": "AVISO", "conferencia": "papel_fora_da_tabela", "tela": tela, "texto": p["texto"],
                        "detalhe": f"{p['papel']} no papel {tipo.upper()}: " + ", ".join(dif)
                                   + "; se é desvio, ele vai declarado no refinamentos.md"})
    for papel, ts in sorted(tamanhos.items()):
        if len(ts) > 1:
            out.append({"nivel": "AVISO", "conferencia": "papel_fora_da_tabela", "tela": tela,
                        "detalhe": f"{papel} em {len(ts)} tamanhos na mesma tela ({', '.join(map(str, sorted(ts)))} px): "
                                   "um tamanho por papel em cada tela"})
    return out


# ---- dois testes [código] da rubrica de design (D3 e D4), os dois AVISO provisório ----
# a cor fora dos tokens e os itens por grupo
ITENS_TETO = 4               # D4: "até quatro itens por grupo, salvo o que o design-system.md libera (a lista
                             # de pendências e a linha do tempo)"
LISTAS_LIBERADAS = ".pendentes,.linha-tempo"   # as listas que o design system da série deixa passar de quatro itens
CORES_MAX_DETALHE = 5

# "Papéis tipográficos de conteúdo por tela: até 4; rótulo, fonte e moldura fora" (rubrica de design, "Medidas").
# Com "até 3, rótulo incluído", a maior parte das telas de uma série passava do teto (título, corpo, destaque e nota
# são o padrão do design system); o conta_papeis.py mede a distribuição numa série.
PAPEIS_TETO = 4
PAPEIS_FORA_DA_CONTA = ("fonte",)   # o rótulo (.rot, .leg) nem entra na CLASSE_PAPEL; a moldura sai pelo filtro


def papeis_por_tela(papeis, tela):
    """O AVISO papeis_por_tela de uma tela da série, sobre os papéis do MEDIR_FORMA (provisório; não barra o --upload)."""
    conta = sorted({p["papel"] for p in papeis if not p.get("moldura") and p["papel"] not in PAPEIS_FORA_DA_CONTA})
    if len(conta) <= PAPEIS_TETO:
        return []
    return [{"nivel": "AVISO", "conferencia": "papeis_por_tela", "tela": tela, "texto": ", ".join(conta),
             "detalhe": f"{len(conta)} papéis tipográficos de conteúdo na tela, acima de {PAPEIS_TETO} (rubrica de design, "
                        "\"Medidas\"; o rótulo, a fonte e a moldura ficam fora); provisório, a calibrar com o uso"}]

MEDIR_LOTE5 = r"""(idx) => {
  const sl = document.querySelectorAll('.slide')[idx];
  const fora = e => !!e.closest('.sim,[data-adesivo-sim],img,picture,video,canvas,defs,mask,clipPath,pattern,filter,marker,symbol');
  const vis = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
                     return r.width > 0.5 && r.height > 0.5 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  // os tokens: toda propriedade --* das folhas da página que é uma cor (o caderno.css e o <style> da peça)
  const probe = document.createElement('span'); probe.style.display = 'none'; sl.appendChild(probe);
  const norm = v => { probe.style.color = ''; probe.style.color = v; return probe.style.color ? getComputedStyle(probe).color : null; };
  const tokens = new Set(['rgba(0, 0, 0, 0)']);
  const varre = regras => { for (const r of regras) {
    if (r.cssRules) varre(r.cssRules);
    if (r.style) for (const p of r.style) if (p.startsWith('--')) { const c = norm(r.style.getPropertyValue(p).trim()); if (c) tokens.add(c); } } };
  for (const s of document.styleSheets) { try { varre(s.cssRules); } catch (e) {} }
  // a folha local (file://) não deixa ler as regras no Chromium: os tokens vêm então do estilo computado, que traz as
  // propriedades --* herdadas pela tela (as do :root e as do papel da tela, .tipo-a e .tipo-b)
  // (as da tela e as dos descendentes: um token definido num seletor de dentro da tela também vale)
  for (const e of [document.documentElement, document.body, sl, ...sl.querySelectorAll('*')]) { const cs = getComputedStyle(e);
    for (const p of cs) if (p.startsWith('--')) { const c = norm(cs.getPropertyValue(p).trim()); if (c) tokens.add(c); } }
  // o elemento com opacidade acumulada zero não aparece: a cor dele não conta
  const apagado = e => { for (let x = e; x && x !== document.documentElement; x = x.parentElement) if (parseFloat(getComputedStyle(x).opacity) === 0) return true; return false; };
  const cores = {};
  const anota = (cor, e, onde) => {
    if (!cor || !cor.startsWith('rgb') || tokens.has(cor)) return;
    const k = cor; if (!cores[k]) cores[k] = {cor, n: 0, exemplo: ''};
    cores[k].n++;
    if (!cores[k].exemplo) cores[k].exemplo = onde + ' em ' + e.tagName.toLowerCase() + (e.getAttribute('class') ? '.' + e.getAttribute('class').trim().split(/\s+/).join('.') : '')
      + ((e.textContent || '').trim() ? ' ("' + e.textContent.replace(/\s+/g, ' ').trim().slice(0, 30) + '")' : '');
  };
  const FORMAS = new Set(['path','rect','circle','ellipse','line','polyline','polygon','text','tspan']);
  for (const e of [sl, ...sl.querySelectorAll('*')]) {
    if (fora(e) || e.closest('.foto')) continue;   // a foto colada com a fita é imagem, não cor do sistema
    const cs = getComputedStyle(e);
    // a linha reta do svg tem caixa de altura (ou largura) zero: basta um dos lados
    const r = e.getBoundingClientRect();
    if (cs.visibility === 'hidden' || cs.display === 'none' || (e instanceof SVGElement ? (r.width <= 0.5 && r.height <= 0.5) : !vis(e)) || apagado(e)) continue;
    // o degradê e a url() do fundo e o traço ou preenchimento em url(#...) (gradiente e padrão do svg) não se conferem: ficam com a leitura
    if (e instanceof SVGElement) {
      const tag = e.tagName.toLowerCase(); if (!FORMAS.has(tag)) continue;
      if (cs.stroke && cs.stroke !== 'none' && parseFloat(cs.strokeWidth) > 0 && parseFloat(cs.strokeOpacity) > 0) anota(cs.stroke, e, 'traço');
      if (tag !== 'line' && cs.fill && cs.fill !== 'none' && parseFloat(cs.fillOpacity) > 0) anota(cs.fill, e, 'preenchimento');
      continue;
    }
    if ([...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim())) anota(cs.color, e, 'texto');
    if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)') anota(cs.backgroundColor, e, 'fundo');
    for (const lado of ['Top','Right','Bottom','Left'])
      if (parseFloat(cs['border' + lado + 'Width']) > 0 && cs['border' + lado + 'Style'] !== 'none') anota(cs['border' + lado + 'Color'], e, 'borda');
  }
  probe.remove();
  // as listas: os itens de cada ul ou ol fora do svg; a lista de pendências (.pendentes) e a linha do tempo
  // (.linha-tempo) o design system libera
  const listas = [];
  for (const l of sl.querySelectorAll('ul,ol')) {
    if (fora(l) || l.closest('svg') || !vis(l) || l.closest('__LIBERADAS__')) continue;
    const itens = [...l.children].filter(c => c.tagName === 'LI' && vis(c)).length;
    listas.push({itens, texto: l.textContent.replace(/\s+/g, ' ').trim().slice(0, 40)});
  }
  return {cores: Object.values(cores), tokens: tokens.size, listas};
}""".replace("__LIBERADAS__", LISTAS_LIBERADAS)


def lote5(l5, tela):
    """Os AVISOs de cor e de lista numa tela da série: cor_fora_dos_tokens (D3) e itens_por_grupo (D4). Provisórios,
    a calibrar com o uso; nenhum barra o --upload."""
    out = []
    if l5["cores"]:
        cs = sorted(l5["cores"], key=lambda c: -c["n"])
        out.append({"nivel": "AVISO", "conferencia": "cor_fora_dos_tokens", "tela": tela,
                    "texto": "; ".join(f"{c['cor']} ({c['exemplo']})" for c in cs[:CORES_MAX_DETALHE]),
                    "detalhe": f"{len(cs)} cor(es) computada(s) fora das {l5['tokens']} cores dos tokens da página "
                               "(D3: \"nenhuma cor fora dos tokens?\", rubrica de design); a imagem e a foto ficam de fora; "
                               "provisório, a calibrar com o uso"})
    for li in l5["listas"]:
        if li["itens"] > ITENS_TETO:
            out.append({"nivel": "AVISO", "conferencia": "itens_por_grupo", "tela": tela, "texto": li["texto"],
                        "detalhe": f"lista com {li['itens']} itens, acima de {ITENS_TETO} por grupo (D4, rubrica de design; "
                                   "as listas que o design system libera, .pendentes e .linha-tempo, ficam de fora); provisório, a calibrar com o uso"})
    return out


def acento_pct(arr, cor):
    """% dos pixels a menos de ACENTO_RAIO da cor do acento (r, g, b), com um filtro de croma: o pixel tem de ser
    pelo menos tão saturado quanto 60% do acento, para o cinza e o papel perto dele não contarem."""
    import numpy as np
    a = arr.astype(float)
    alvo = np.array(cor, float)
    d = np.sqrt(((a - alvo) ** 2).sum(axis=2))
    croma = a.max(axis=2) - a.min(axis=2)
    piso = 0.6 * (alvo.max() - alvo.min())
    return round(float(((d < ACENTO_RAIO) & (croma >= piso)).sum()) / d.size * 100, 3)


def dentro(p, r):
    return r[0] <= p[0] <= r[2] and r[1] <= p[1] <= r[3]


def distancia(p, r):
    dx = max(r[0] - p[0], 0, p[0] - r[2])
    dy = max(r[1] - p[1], 0, p[1] - r[3])
    return (dx * dx + dy * dy) ** 0.5


def pontas_das_setas(setas, m, tela):
    """Os AVISOs ponta_da_seta de uma tela: as setas lidas antes de o caderno.js trocá-las e postas na tela depois do
    prepararSlide (PREPARAR), no mesmo estado em que os alvos se medem.

    Toda seta: a ponta cai num alvo (forma do svg que não é traço de seta, foto, imagem, folha que espia), encosta
    nele (até SETA_ENCOSTA px da caixa), ou aponta texto (até 40 px de uma linha); senão, termina no vazio. A seta de
    anotação (a que sai de uma nota, rótulo ou legenda do kit) que cai dentro de um alvo largo (lado menor de 40 px
    ou mais) entra nele de 20 a 30 px pelo design system; menos de 20 avisa. O conector do diagrama (a seta entre dois
    desenhos) só precisa encostar: ele aponta de um desenho para o outro, e a regra dos 20 a 30 px é do rótulo."""
    out = []
    alvos = ([("forma", f["rect"]) for f in m["formas"] if not re.search(r"\b(tinta-[cl]|seta-livre)\b", f.get("fcls", ""))]
             + [("figura", r) for r in m["figuras"]] + [("folha", r) for r in m.get("folhas", [])])
    linhas = [l for l in m["linhas"] if not l["moldura"] and not l["adesivo"]]
    for s in setas:
        if s.get("intencional"):
            continue
        p = s["ponta"]
        onde = f"ponta em x {round(p[0])}, y {round(p[1])}"
        anotacao = any(l.get("anotacao") and distancia(s["inicio"], l["rect"]) <= SETA_TEXTO_PERTO for l in linhas)
        caixas = [(t, r) for t, r in alvos if dentro(p, r) and (r[2] - r[0]) * (r[3] - r[1]) > 4]
        if caixas:
            tipo, r = min(caixas, key=lambda c: (c[1][2] - c[1][0]) * (c[1][3] - c[1][1]))
            prof = min(p[0] - r[0], r[2] - p[0], p[1] - r[1], r[3] - p[1])
            if anotacao and min(r[2] - r[0], r[3] - r[1]) >= 2 * SETA_ENTRA_MIN and prof < SETA_ENTRA_MIN:
                out.append({"nivel": "AVISO", "conferencia": "ponta_da_seta", "tela": tela,
                            "detalhe": f"{onde}: a seta da anotação entra {round(prof)} px na caixa do alvo ({tipo}), menos "
                                       "que os 20 a 30 px; a caixa é aproximada, conferir no zoom (juntas.py)"})
            continue
        if any(distancia(p, r) <= SETA_ENCOSTA for _, r in alvos):
            continue
        if any(distancia(p, l["rect"]) <= SETA_TEXTO_PERTO for l in linhas):
            continue   # aponta texto: a sobreposição confere se cruza letra
        out.append({"nivel": "AVISO", "conferencia": "ponta_da_seta", "tela": tela,
                    "detalhe": f"{onde}: termina no vazio, sem entrar nem encostar em desenho, foto ou folha nem apontar "
                               "texto (toda linha termina em algo)"})
    return out


def avisos_da_peca(telas, piso_acento=ACENTO_PISO_PECA):
    """Os AVISOs de peça: corpo sem negrito e o piso do acento. `telas`: [{tela, unidades, acento}] das telas da série
    (o acento None quando a série não declara a cor); `piso_acento`, o da série (limiares_do_acento)."""
    out = []
    com_corpo = [t for t in telas if t["unidades"]]
    if len(com_corpo) >= NEGRITO_MIN_TELAS:
        com_negrito = sum(any(u["negrito"] for u in t["unidades"]) for t in com_corpo)
        fr = com_negrito / len(com_corpo)
        if fr < NEGRITO_PISO:
            sem = [t["tela"] for t in com_corpo if not any(u["negrito"] for u in t["unidades"])]
            out.append({"nivel": "AVISO", "conferencia": "corpo_sem_negrito", "tela": "todas",
                        "detalhe": f"{com_negrito} de {len(com_corpo)} telas com corpo ou lista levam negrito ({round(fr * 100)}%; "
                                   f"o piso é {round(NEGRITO_PISO * 100)}%): o negrito marca as palavras-chave para quem passa os olhos; "
                                   f"sem negrito: telas {sem}"})
    medidas = [t["acento"] for t in telas if t.get("acento") is not None]
    if medidas:
        media = sum(medidas) / len(medidas)
        if media < piso_acento:
            out.append({"nivel": "AVISO", "conferencia": "acento_area", "tela": "todas",
                        "detalhe": f"o acento cobre {media:.2f}% da tela na média da peça, abaixo de {piso_acento}%: "
                                   "faltam as marcas no acento?"})
    return out


def conferir_legenda_exportacao(legenda):
    """Os AVISOs da legenda que só a exportação roda: caractere invisível e a primeira frase depois do corte do feed."""
    out = []
    inv = sorted({f"U+{ord(c):04X}" for c in INVISIVEIS.findall(legenda)})
    if inv:
        out.append({"nivel": "AVISO", "conferencia": "caractere_invisivel", "tela": "legenda",
                    "detalhe": f"{', '.join(inv)} na legenda: caractere que não se vê (colado de outro lugar?)"})
    primeira = re.split(r"(?<=[.!?…])\s|\n", legenda.strip(), maxsplit=1)[0]
    if len(primeira) > CORTE_LEGENDA - CORTE_MARGEM:
        out.append({"nivel": "AVISO", "conferencia": "primeira_frase_legenda", "tela": "legenda",
                    "detalhe": f"a primeira frase tem {len(primeira)} caracteres; o feed corta a legenda perto de "
                               f"{CORTE_LEGENDA} (aproximação), e antes do \"mais\" aparece: \"{legenda.strip()[:CORTE_LEGENDA]}\""})
    return out
