"""O JavaScript que pede as fontes de uma tela e diz quais não carregaram, para todo script que mede texto renderizado
(linhas, larguras, caracteres por linha, posição).

Por que existe (uma lição crítica, em `licoes-gerais.md`): o `document.fonts.ready` resolve na
hora quando nenhuma fonte foi pedida ainda (a página começa sem texto, ou a tela está escondida), e o navegador mede na
fonte de reserva sem avisar. Por isso a fonte se pede de propósito, com o texto que a usa (`document.fonts.load`), e
depois se confere se ela existe mesmo: a família que não carregou (o arquivo falhou, ou o `@import` da fonte da web
não veio, sem rede) mede igual à fonte genérica de reserva.

Uso, dentro do JavaScript de uma página (Playwright ou `shot-scraper javascript`):

    from fontes import CARREGAR_FONTES
    JS = "async () => { const carregarFontes = " + CARREGAR_FONTES + "; const faltam = await carregarFontes(tela); ... }"

`carregarFontes(raiz)` olha o texto visível dentro de `raiz` (ou do `body`), inclusive o dos `::before` e `::after`
(a numeração dos `.passos`, por exemplo), pede cada fonte com esse texto, espera o `document.fonts.ready` e devolve a
lista do que não carregou, cada item com `familia`, `fonte` (a declaração CSS), `chave` (família, estilo e peso, sem o
tamanho: a mesma fonte em dois tamanhos é uma só, e quem chama mais de uma vez deduplica por ela) e `amostra` (o começo
do texto). Lista vazia: as medidas valem para a fonte da peça. Família genérica (`serif`, `cursive`...) não entra na
conta, nem os apelidos da fonte do sistema de outro aparelho (`-apple-system`, `BlinkMacSystemFont`), que a pilha
dos Stories põe antes de "Segoe UI": a conta vai para a família seguinte. A
espera tem prazo (ESPERA, 10 s por chamada): a fonte que não respondeu até lá (a rede travada, não a ausente)
conta como não carregada, em vez de pendurar a medida, e as chamadas seguintes na mesma página não a esperam de novo; a
que respondeu no mesmo pedido continua sendo pedida. Campo de formulário (`input`) não entra: as peças não usam.

A família declarada com um peso que falhou (o 400 carregou e o arquivo do 700 não) não engana a conta: o Chromium não
engrossa o 400 no lugar do 700 que falhou, mede na reserva, e a largura acusa (caso do teste_medir_blocos.py).

Limite conhecido: a conta é por família, numa amostra fixa (AMOSTRA). A fonte da web dividida em subconjuntos por
`unicode-range` (latin, latin-ext) passa se um deles carregou, mesmo que o outro tenha falhado: o caractere do
subconjunto que falhou sai na reserva sem acusar. A medida da largura não separa esse caso do glifo que a fonte não tem
(uma seta, que cai na reserva por desenho). O caminho: depois dos `document.fonts.load`, olhar as `FontFace` da família
com `status === 'error'` cujo `unicodeRange`, peso e estilo cobrem o texto da tela. O texto das peças em português cabe
no subconjunto latin, e por isso o caso não se viu.
"""

CARREGAR_FONTES = r"""async (raiz) => {
  const GENERICAS = new Set(['serif','sans-serif','cursive','fantasy','monospace','system-ui','emoji','math','fangsong',
    'ui-serif','ui-sans-serif','ui-monospace','ui-rounded','inherit','initial','unset']);
  // os apelidos da fonte do sistema de outro aparelho (a pilha "-apple-system, 'Segoe UI', Roboto..." dos Stories):
  // no Windows não existem, e a pilha quer a seguinte, então a conta começa depois deles
  const SISTEMA = new Set(['-apple-system', 'blinkmacsystemfont']);
  const primeira = lista => {   // a primeira família da lista, sem aspas e sem os apelidos do sistema: a que a peça quer
    let resto = lista.trim();
    while (resto) {
      const m = resto.match(/^("([^"]*)"|'([^']*)'|[^,]+)\s*,?\s*/);
      if (!m) return '';
      const f = (m[2] ?? m[3] ?? m[1]).trim();
      if (!SISTEMA.has(f.toLowerCase())) return f;
      resto = resto.slice(m[0].length);
    }
    return '';
  };
  const ESPERA = 10000;   // ms por chamada; a fonte que não respondeu nesse prazo conta como não carregada
  const limite = performance.now() + ESPERA;
  const comPrazo = pr => Promise.race([pr.then(() => true), new Promise(ok => setTimeout(() => ok(false), Math.max(0, limite - performance.now())))]);
  const semResposta = window.__fontesSemResposta || (window.__fontesSemResposta = new Set());   // não se espera duas vezes
  const pedidos = new Map();   // declaração da fonte -> {familia, estilo, peso, texto}
  const anota = (cs, t) => {
    const fonte = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
    const p = pedidos.get(fonte) || {familia: primeira(cs.fontFamily), estilo: cs.fontStyle, peso: cs.fontWeight, texto: ''};
    p.texto += t; pedidos.set(fonte, p);
  };
  const base = raiz || document.body;
  const tw = document.createTreeWalker(base, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = tw.nextNode())) {
    const t = n.textContent.trim(), el = n.parentElement;
    if (!t || !el || !el.getClientRects().length) continue;   // texto escondido não entra na tela medida
    anota(getComputedStyle(el), t);
  }
  for (const el of [base, ...base.querySelectorAll('*')]) {   // o texto dos ::before e ::after não é nó do DOM
    if (!el.getClientRects().length) continue;
    for (const ps of ['::before', '::after']) {
      const cs = getComputedStyle(el, ps), c = cs.content;
      if (!c || c === 'none' || c === 'normal') continue;
      const t = c.replace(/counters?\([^)]*\)/g, '0123456789')
                 .replace(/attr\(([^)]*)\)/g, (_, a) => el.getAttribute(a.trim()) || '').replace(/["']/g, '').trim();
      if (t) anota(cs, t);
    }
  }
  const esperar = [...pedidos].filter(([fonte]) => !semResposta.has(fonte)), responderam = new Set();
  if (!await comPrazo(Promise.allSettled(esperar.map(([fonte, p]) =>
        document.fonts.load(fonte, p.texto).finally(() => responderam.add(fonte))))))
    for (const [fonte] of esperar) if (!responderam.has(fonte)) semResposta.add(fonte);   // só a que não respondeu
  // o fonts.ready espera também a que não respondeu: com uma delas pendente, a conta abaixo decide sem ele
  if (document.fonts && !semResposta.size) await comPrazo(document.fonts.ready);
  const ctx = document.createElement('canvas').getContext('2d');
  const AMOSTRA = 'mmmmmmmmmmlli1WQ@#&ãéç';
  const existe = p => ['monospace', 'serif', 'sans-serif'].some(g => {
    ctx.font = `${p.estilo} ${p.peso} 48px ${g}`; const reserva = ctx.measureText(AMOSTRA).width;
    ctx.font = `${p.estilo} ${p.peso} 48px "${p.familia}", ${g}`; return ctx.measureText(AMOSTRA).width !== reserva;
  });
  const faltam = [], vistas = new Set();
  for (const [fonte, p] of pedidos) {
    const chave = `${p.familia}|${p.estilo}|${p.peso}`;   // o tamanho não conta: a mesma fonte em dois tamanhos é uma
    if (!p.familia || GENERICAS.has(p.familia.toLowerCase()) || vistas.has(chave)) continue;
    vistas.add(chave);
    if (!existe(p)) faltam.push({familia: p.familia, fonte, chave, amostra: p.texto.slice(0, 30)});
  }
  return faltam;
}"""
