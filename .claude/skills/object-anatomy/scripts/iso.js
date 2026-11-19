/* iso.js: o gerador de partida da skill object-anatomy, em SVG (método em ../references/metodo.md).
   Com o papel opaco liso como padrão (estiloPapel), a classe da aresta das faces lisas por opção
   (op.aresta), a projeção sem espelho, o texto escapado e o encaixa da placa vista de lado. Nenhum código do kit do Anatomy: só a conta de projeção de cinco
   linhas (R9), escrita de novo, e o que o método diz. Roda no navegador (window.ISO) ou no Node (module.exports).

   Uso de partida (a página da peça carrega este arquivo e o seu modelo):
     const cam = ISO.encaixa(45, 30, ISO.pontosDe(solidos), [x0, y0, x1, y1]);
     svg.innerHTML = solidos.map(s => ISO.pinta(cam, s, {estilo: ISO.estiloPapel(), aresta: 'c'})).join('');
   O tom pela normal (estiloFace) só entra quando quem chama pede a variante com tom (references/projeto.md).
   Testes, sem navegador: node .claude/skills/object-anatomy/scripts/teste_iso.js (rodar a cada edição daqui).

   - camera(az, el, escala, off): projeção isométrica de câmera fixa; x e y no chão, z para cima; P(ponto) dá o px da tela,
     prof(ponto) a profundidade para quem vê (maior = mais perto), D o vetor que aponta para quem vê.
   - Sólidos como listas de faces planas com normal (caixa, extrusão de um perfil, cilindro). A face que não vira para quem vê
     não se pinta; as que viram se pintam da mais funda para a mais rasa (dentro da peça). Entre peças, a ordem é escrita
     por quem monta a cena (R11): a biblioteca não ordena peças.
   - Papel opaco (R12): toda face é preenchida com o papel (o padrão); o tom pela normal contra uma luz fixa só com
     op.tom (contínuo, com três ou quatro tons visíveis numa caixa).
   - Superfície lisa (lado de cilindro): as faces vizinhas não ganham aresta; só se traça a silhueta, isto é, a aresta cuja
     vizinha não aparece ou não é lisa. É o que o lathe.mjs do kit faz com curva monótona; aqui são 48 a 64 facetas.
*/
(function (raiz) {
  'use strict';
  const rad = g => g * Math.PI / 180;
  const clamp01 = x => x < 0 ? 0 : x > 1 ? 1 : x;
  const suave = x => { x = clamp01(x); return x * x * (3 - 2 * x); };
  const suave5 = x => { x = clamp01(x); return x * x * x * (x * (6 * x - 15) + 10); };
  // envelope de ataque e queda (R15): 0 antes de t0, sobe em a s, segura h s, cai em q s
  const envelope = (t, t0, a, h, q) => t < t0 ? 0 : t < t0 + a ? suave((t - t0) / a) : t < t0 + a + h ? 1 : 1 - suave((t - t0 - a - h) / q);
  const inversa = (f, u) => { let lo = 0, hi = 1; for (let k = 0; k < 50; k++) { const md = (lo + hi) / 2; if (f(md) < u) lo = md; else hi = md; } return (lo + hi) / 2; };
  const soma = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]];
  const sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
  const mul = (a, k) => [a[0] * k, a[1] * k, a[2] * k];
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  const cruz = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
  const norm = a => { const l = Math.hypot(a[0], a[1], a[2]) || 1; return [a[0] / l, a[1] / l, a[2] / l]; };
  const f1 = v => (Math.round(v * 10) / 10).toString();

  // ---------------------------------------------------------------- a câmera (R9): cinco linhas de trigonometria
  function camera(az = 45, el = 30, escala = 1, off = [0, 0]) {
    const SA = Math.sin(rad(az)), CA = Math.cos(rad(az)), SE = Math.sin(rad(el)), CE = Math.cos(rad(el));
    // o x da tela é (-SA, CA, 0): com o y da tela para baixo, x da tela vezes o de cima dá D, como numa câmera de verdade
    const P = p => [escala * (p[1] * CA - p[0] * SA) + off[0], escala * ((p[0] * CA + p[1] * SA) * SE - p[2] * CE) + off[1]];
    const D = [CA * CE, SA * CE, SE];
    const prof = p => p[0] * D[0] + p[1] * D[1] + p[2] * D[2];
    // a parte linear (para pôr texto numa face com transform="matrix(...)")
    const L = v => [escala * (v[1] * CA - v[0] * SA), escala * ((v[0] * CA + v[1] * SA) * SE - v[2] * CE)];
    return { az, el, escala, off, P, D, prof, L, SA, CA, SE, CE };
  }

  // ---------------------------------------------------------------- tom pela normal
  const LUZ = norm([-0.35, 0.42, 0.84]);
  function tomDe(n, base = 'face') {
    const k = dot(n, LUZ);                       // 1 = de frente para a luz
    const p = Math.round(8 + 58 * (1 - (k + 1) / 2) ** 1.25);   // % de sombra misturada
    return { p, base };
  }
  function estiloFace(n, base, liso) {
    const { p } = tomDe(n);
    const cor = `color-mix(in srgb, var(--${base}-sombra) ${p}%, var(--${base}))`;
    return liso ? `fill:${cor};stroke:${cor};stroke-width:0.9` : `fill:${cor}`;
  }
  // o padrão: toda face no papel (opaco, as linhas do papel somem dentro do objeto, R12), sem tom; a face plana leva o
  // contorno na tinta, e a lisa só esconde a costura entre as facetas (a silhueta dela vem no path da aresta)
  function estiloPapel(papel = 'var(--papel-b)', tinta = 'var(--tinta)', traco = 4) {   // os tokens do caderno.css da série
    return (n, f) => f.liso ? `fill:${papel};stroke:${papel};stroke-width:0.9`
      : `fill:${papel};stroke:${tinta};stroke-width:${traco};stroke-linejoin:round;stroke-linecap:round`;
  }

  // ---------------------------------------------------------------- sólidos
  // face = {pts: [[x,y,z]...], n: [..], liso: bool, furos: [[pts]...]}; solido = {faces, base, aberto}
  function caixa(x0, x1, y0, y1, z0, z1, op = {}) {
    const v = (x, y, z) => [x, y, z];
    const faces = [
      { pts: [v(x0, y0, z1), v(x1, y0, z1), v(x1, y1, z1), v(x0, y1, z1)], n: [0, 0, 1] },
      { pts: [v(x0, y0, z0), v(x0, y1, z0), v(x1, y1, z0), v(x1, y0, z0)], n: [0, 0, -1] },
      { pts: [v(x0, y1, z1), v(x1, y1, z1), v(x1, y1, z0), v(x0, y1, z0)], n: [0, 1, 0] },
      { pts: [v(x1, y0, z1), v(x0, y0, z1), v(x0, y0, z0), v(x1, y0, z0)], n: [0, -1, 0] },
      { pts: [v(x1, y1, z1), v(x1, y0, z1), v(x1, y0, z0), v(x1, y1, z0)], n: [1, 0, 0] },
      { pts: [v(x0, y0, z1), v(x0, y1, z1), v(x0, y1, z0), v(x0, y0, z0)], n: [-1, 0, 0] },
    ];
    return { faces, base: op.base || 'face', nome: op.nome };
  }
  // extrusão de um perfil 2D (a, b) no plano (origem, u, v), varrido ao longo de w (vetor com o comprimento)
  function extrusao(perfil, origem, u, v, w, op = {}) {
    u = norm(u); v = norm(v);
    let area = 0;
    for (let i = 0; i < perfil.length; i++) { const p = perfil[i], q = perfil[(i + 1) % perfil.length]; area += p[0] * q[1] - q[0] * p[1]; }
    const ccw = area > 0;
    const M = (p, t) => soma(soma(soma(origem, mul(u, p[0])), mul(v, p[1])), mul(w, t));
    const wn = norm(w), uv = norm(cruz(u, v)), mesmo = dot(uv, wn) > 0;
    // w pode ser oblíquo ao plano (u, v): a tampa tem a normal do plano, do lado para onde w anda,
    // e a lateral, a de aresta × w, virada para fora
    const nTampa = mul(uv, mesmo ? 1 : -1), sinal = ccw === mesmo ? 1 : -1;
    const faces = [];
    const baixo = perfil.map(p => M(p, 0)), cima = perfil.map(p => M(p, 1));
    faces.push({ pts: cima.slice(), n: nTampa, tampa: true, furos: op.furosCima });
    faces.push({ pts: baixo.slice().reverse(), n: mul(nTampa, -1), tampa: true });
    for (let i = 0; i < perfil.length; i++) {
      const j = (i + 1) % perfil.length;
      const n = mul(norm(cruz(sub(baixo[j], baixo[i]), w)), sinal);
      faces.push({ pts: [baixo[i], baixo[j], cima[j], cima[i]], n, liso: !!op.liso });
    }
    return { faces, base: op.base || 'face', nome: op.nome, mesmo };
  }
  function circulo(r, n = 48, a0 = 0) { return Array.from({ length: n }, (_, k) => [r * Math.cos(a0 + 2 * Math.PI * k / n), r * Math.sin(a0 + 2 * Math.PI * k / n)]); }
  // a base ortonormal de um eixo (para cilindros e discos)
  function baseDoEixo(eixo) {
    const e = norm(eixo);
    const t = Math.abs(e[2]) < 0.9 ? [0, 0, 1] : [1, 0, 0];
    const u = norm(cruz(t, e)), v = norm(cruz(e, u));
    return { e, u, v };
  }
  function cilindro(c, eixo, r, comp, op = {}) {
    const { e, u, v } = op.uv ? { e: norm(eixo), u: op.uv[0], v: op.uv[1] } : baseDoEixo(eixo);
    return extrusao(circulo(r, op.n || 48, op.a0 || 0), c, u, v, mul(e, comp), { liso: true, base: op.base, nome: op.nome, furosCima: op.furosCima });
  }
  // uma placa de duas faces (lâmina fina sem espessura): a face que aparece é a que vira para quem vê
  function placa(pts, op = {}) {
    const n = norm(cruz(sub(pts[1], pts[0]), sub(pts[2], pts[0])));
    return { faces: [{ pts, n, duas: true, furos: op.furos }], base: op.base || 'face', nome: op.nome };
  }
  function move(sol, d) {
    if (!d || (!d[0] && !d[1] && !d[2])) return sol;
    return Object.assign({}, sol, { faces: sol.faces.map(f => Object.assign({}, f, { pts: f.pts.map(p => soma(p, d)), furos: f.furos && f.furos.map(h => h.map(p => soma(p, d))) })) });
  }
  // gira em torno de um eixo que passa por c (Rodrigues)
  function giraPonto(p, c, eixo, ang) {
    const k = norm(eixo), q = sub(p, c), co = Math.cos(ang), si = Math.sin(ang);
    const r = soma(soma(mul(q, co), mul(cruz(k, q), si)), mul(k, dot(k, q) * (1 - co)));
    return soma(r, c);
  }
  function gira(sol, c, eixo, ang) {
    if (!ang) return sol;
    const gv = n => sub(giraPonto(n, [0, 0, 0], eixo, ang), [0, 0, 0]);
    return Object.assign({}, sol, { faces: sol.faces.map(f => Object.assign({}, f, { pts: f.pts.map(p => giraPonto(p, c, eixo, ang)), n: gv(f.n), furos: f.furos && f.furos.map(h => h.map(p => giraPonto(p, c, eixo, ang))) })) });
  }

  // ---------------------------------------------------------------- desenho de um sólido
  const chaveP = p => `${Math.round(p[0] * 100)},${Math.round(p[1] * 100)},${Math.round(p[2] * 100)}`;
  function pinta(cam, sol, op = {}) {
    const base = op.base || sol.base || 'face';
    const caminho = pts => 'M' + pts.map(p => { const q = cam.P(p); return f1(q[0]) + ' ' + f1(q[1]); }).join('L') + 'Z';
    const vis = sol.faces.map(f => {
      let n = f.n;
      const d = dot(n, cam.D);
      if (f.duas && d < 0) n = mul(n, -1);
      return { f, n, ve: f.duas ? true : d > 1e-6, pr: f.pts.reduce((s, p) => s + cam.prof(p), 0) / f.pts.length };
    });
    // vizinhança das arestas (para a silhueta das faces lisas)
    const viz = new Map();
    vis.forEach((o, i) => o.f.pts.forEach((p, k) => {
      const q = o.f.pts[(k + 1) % o.f.pts.length], a = chaveP(p), b = chaveP(q), ch = a < b ? a + '|' + b : b + '|' + a;
      if (!viz.has(ch)) viz.set(ch, []); viz.get(ch).push(i);
    }));
    const ordem = vis.map((o, i) => i).filter(i => vis[i].ve).sort((a, b) => vis[a].pr - vis[b].pr);
    const cls = op.cls ? ` class="${op.cls}"` : '';
    let s = '', bordas = '';
    for (const i of ordem) {
      const o = vis[i], f = o.f;
      let d = caminho(f.pts);
      if (f.furos) for (const h of f.furos) d += caminho(h);
      // sem estilo, o padrão (papel opaco liso, sem tom); o tom pela normal só com op.tom, na variante com tom
      const est = op.estilo ? op.estilo(o.n, f) : op.tom ? estiloFace(o.n, base, f.liso) : PAPEL(o.n, f);
      s += `<path${cls} d="${d}" style="${est}"${f.furos ? ' fill-rule="evenodd"' : ''}${f.liso ? '' : ' data-a="1"'}/>`;
      if (f.liso) {
        f.pts.forEach((p, k) => {
          const q = f.pts[(k + 1) % f.pts.length], a = chaveP(p), b = chaveP(q), ch = a < b ? a + '|' + b : b + '|' + a;
          const outros = (viz.get(ch) || []).filter(j => j !== i);
          const silh = outros.length === 0 || outros.some(j => !vis[j].ve || !vis[j].f.liso);
          if (silh) { const A = cam.P(p), B = cam.P(q); bordas += `M${f1(A[0])} ${f1(A[1])}L${f1(B[0])} ${f1(B[1])}`; }
        });
      }
    }
    if (bordas) s += `<path class="${op.aresta || 'aresta'}" d="${bordas}"/>`;
    return s;
  }
  // as faces não lisas ganham contorno pelo CSS (path[data-a]); a aresta das lisas vem no path .aresta
  function linha(cam, pts, cls = 'traco', fecha = false) {
    return `<path class="${cls}" d="M${pts.map(p => { const q = cam.P(p); return f1(q[0]) + ' ' + f1(q[1]); }).join('L')}${fecha ? 'Z' : ''}"/>`;
  }
  function poli(cam, pts, est, cls = '') {
    return `<path${cls ? ` class="${cls}"` : ''} d="M${pts.map(p => { const q = cam.P(p); return f1(q[0]) + ' ' + f1(q[1]); }).join('L')}Z" style="${est}"/>`;
  }
  // texto deitado numa face: origem no pé da primeira letra, u para a direita do texto, v para cima do texto
  const escapa = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  function textoFace(cam, str, origem, u, v, tam, cls = 'gravado', extra = '') {
    const a = cam.L(norm(u)), b = cam.L(mul(norm(v), -1)), o = cam.P(origem), k = tam / 100;
    return `<text class="${cls}" transform="matrix(${f1(a[0] * k * 100) / 100} ${f1(a[1] * k * 100) / 100} ${f1(b[0] * k * 100) / 100} ${f1(b[1] * k * 100) / 100} ${f1(o[0])} ${f1(o[1])})" font-size="100"${extra}>${escapa(str)}</text>`;
  }
  // caixa de tela de uma lista de pontos 3D (para encaixar o objeto no cartão)
  function caixaTela(cam, pts) {
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const p of pts) { const q = cam.P(p); x0 = Math.min(x0, q[0]); y0 = Math.min(y0, q[1]); x1 = Math.max(x1, q[0]); y1 = Math.max(y1, q[1]); }
    return [x0, y0, x1, y1];
  }
  const pontosDe = sols => sols.flatMap(s => s.faces.flatMap(f => f.pts));
  // escolhe escala e deslocamento para a caixa 3D caber em [x0, y0, x1, y1] da tela
  function encaixa(az, el, pts, alvo, alinha = [0.5, 0.5]) {
    const c1 = camera(az, el, 1, [0, 0]), b = caixaTela(c1, pts);
    const bw = b[2] - b[0], bh = b[3] - b[1];
    if (!(bw > 0 || bh > 0)) throw new Error('encaixa: os pontos não têm largura nem altura na tela (lista vazia ou um ponto só)');
    const esc = Math.min(bw > 0 ? (alvo[2] - alvo[0]) / bw : Infinity, bh > 0 ? (alvo[3] - alvo[1]) / bh : Infinity);
    const w = (b[2] - b[0]) * esc, h = (b[3] - b[1]) * esc;
    const off = [alvo[0] + (alvo[2] - alvo[0] - w) * alinha[0] - b[0] * esc, alvo[1] + (alvo[3] - alvo[1] - h) * alinha[1] - b[1] * esc];
    return camera(az, el, esc, off);
  }

  const PAPEL = estiloPapel();
  const API = { rad, clamp01, suave, suave5, envelope, inversa, soma, sub, mul, dot, cruz, norm, f1, camera, caixa, extrusao, circulo,
    baseDoEixo, cilindro, placa, move, gira, giraPonto, pinta, linha, poli, textoFace, caixaTela, pontosDe, encaixa, estiloFace, estiloPapel, LUZ };
  if (typeof module !== 'undefined' && module.exports) module.exports = API; else raiz.ISO = API;
})(typeof window !== 'undefined' ? window : globalThis);
