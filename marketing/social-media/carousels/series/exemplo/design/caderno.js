// A série de exemplo: o que o caderno faz sozinho em cada tela, antes da foto. Identidade neutra, para trocar.
// A exportação (skill slides-export) e as conferências (skill visual-form) chamam window.prepararSlide(idx) antes de
// medir ou fotografar; o que ele faz:
//   1. prende a palavra curta à seguinte nos títulos, destaques e citações (a lista CURTAS, que a conferência lê daqui);
//   2. assenta o texto: na .coluna, reparte o espaço livre entre os .respiro (peso em --w) em múltiplos do passo do
//      papel (--passo); se o conteúdo não cabe, a tela ganha a classe "transborda";
//   3. desenha as marcas (.circulo, .sublinha, .riscado) num svg.marcas por cima do texto, e a ponta de cada seta livre
//      (path.seta-livre) do desenho.
(function () {
  const NS = 'http://www.w3.org/2000/svg';

  // 1. a palavra curta presa à seguinte: o espaço depois dela vira inseparável, para nenhuma linha terminar nela
  const CURTAS = new Set(['a', 'o', 'e', 'é', 'de', 'em', 'da', 'do', 'no', 'na', 'um', 'ao', 'à', 'os', 'as', 'se', 'por']);
  function prenderCurtas(slide) {
    if (slide.dataset.presas) return;
    for (const el of slide.querySelectorAll('.titulo, .destaque, .citacao')) {
      const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      const nos = []; while (w.nextNode()) nos.push(w.currentNode);
      for (const n of nos) {
        n.data = n.data.replace(/(?<=^|[\s\u00a0(“"])([A-Za-zÀ-ÿ]+) (?=\S)/g,
          (m, palavra) => CURTAS.has(palavra.toLowerCase()) ? palavra + '\u00a0' : m);
      }
    }
    slide.dataset.presas = '1';
  }

  // 2. o assentamento da coluna
  function assentar(slide) {
    if (slide.dataset.assentado) return;
    const passo = parseFloat(getComputedStyle(slide).getPropertyValue('--passo')) || 24;
    for (const col of slide.querySelectorAll('.coluna')) {
      const respiros = [...col.querySelectorAll(':scope > .respiro')];
      respiros.forEach(r => { r.style.flex = `0 0 ${passo}px`; });
      const ultimo = col.lastElementChild;
      if (!ultimo) continue;
      const livre = col.getBoundingClientRect().bottom - ultimo.getBoundingClientRect().bottom;
      if (livre < -0.5) { slide.classList.add('transborda'); console.warn('caderno.js: a coluna não cabe', Math.round(livre)); continue; }
      const linhas = Math.floor((livre + 0.5) / passo);
      const pesos = respiros.map(r => parseFloat(getComputedStyle(r).getPropertyValue('--w')) || 1);
      const total = pesos.reduce((a, b) => a + b, 0) || 1;
      const parte = pesos.map(p => Math.floor(linhas * p / total));
      let sobra = linhas - parte.reduce((a, b) => a + b, 0);
      for (let i = 0; sobra > 0 && respiros.length; i = (i + 1) % respiros.length, sobra--) parte[i]++;
      respiros.forEach((r, i) => { r.style.flex = `0 0 ${(1 + parte[i]) * passo}px`; });
    }
    slide.dataset.assentado = '1';
  }

  // 3. as marcas e as pontas das setas
  function traco(svg, d, cls) {
    const p = document.createElementNS(NS, 'path');
    p.setAttribute('d', d); if (cls) p.setAttribute('class', cls); svg.appendChild(p); return p;
  }
  function pontas(slide) {
    // a ponta de cada seta livre: dois golpes curtos no fim do traço, na tinta dele; levam a classe seta-livre para
    // não contarem como alvo de outra seta
    for (const p of slide.querySelectorAll('svg path.seta-livre:not(.ponta-seta)')) {
      if (p.dataset.ponta) continue;
      const L = p.getTotalLength(); if (!L) continue;
      const a = p.getPointAtLength(L), b = p.getPointAtLength(Math.max(0, L - 12));
      const ang = Math.atan2(a.y - b.y, a.x - b.x), t = 16;
      const d = [0.5, -0.5].map(k => `M${(a.x - t * Math.cos(ang + k)).toFixed(1)} ${(a.y - t * Math.sin(ang + k)).toFixed(1)} L${a.x.toFixed(1)} ${a.y.toFixed(1)}`).join(' ');
      const h = traco(p.parentNode, d, 'seta-livre ponta-seta' + (p.classList.contains('l') ? ' l' : ''));
      h.setAttribute('stroke', getComputedStyle(p).stroke);
      p.dataset.ponta = '1';
    }
  }
  function marcas(slide) {
    const o = slide.getBoundingClientRect();
    const svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('class', 'traco marcas');
    svg.setAttribute('width', String(Math.round(o.width) || 1080));
    svg.setAttribute('height', String(Math.round(o.height) || 1350));
    svg.style.cssText = 'position:absolute;left:0;top:0;pointer-events:none;z-index:5';
    const R = el => { const r = el.getBoundingClientRect(); return {x: r.left - o.left, y: r.top - o.top, w: r.width, h: r.height}; };
    for (const el of slide.querySelectorAll('.circulo')) {
      const r = R(el), cx = r.x + r.w / 2, cy = r.y + r.h / 2, rx = r.w / 2 + 14, ry = r.h / 2 + 8;
      traco(svg, `M${cx - rx} ${cy} A${rx} ${ry} 0 1 1 ${cx + rx} ${cy} A${rx} ${ry} 0 1 1 ${cx - rx} ${cy}`);
    }
    for (const el of slide.querySelectorAll('.sublinha')) {
      for (const q of el.getClientRects()) {
        const y = q.bottom - o.top - 2;
        traco(svg, `M${q.left - o.left} ${y} L${q.right - o.left} ${y}`);
      }
    }
    for (const el of slide.querySelectorAll('.riscado')) {
      const r = R(el), y = r.y + r.h * 0.55;
      traco(svg, `M${r.x - 4} ${y} L${r.x + r.w + 4} ${y}`);
    }
    slide.appendChild(svg);
  }

  window.prepararSlide = async function (idx) {
    const s = document.querySelectorAll('.slide')[idx];
    if (!s) return;
    try {
      void s.offsetHeight;   // o estilo da tela recém-mostrada, para as fontes dela começarem a carregar
      if (document.fonts) await document.fonts.ready;
      prenderCurtas(s);
      assentar(s);
      if (!s.classList.contains('desenhado')) { pontas(s); marcas(s); s.classList.add('desenhado'); }
    } finally {
      s.classList.add('pronto');   // mesmo com erro, a tela aparece (imperfeita), nunca em branco
    }
  };

  // revisão no navegador: as setas do teclado trocam de tela, e o endereço com #N (a partir de 1) abre na tela N
  const telas = () => [...document.querySelectorAll('.slide')];
  let i = 0;
  const ir = k => {
    i = Math.max(0, Math.min(k, telas().length - 1));
    telas().forEach((x, j) => x.classList.toggle('active', j === i));
    window.prepararSlide(i);
  };
  const doEndereco = () => { const n = parseInt(location.hash.slice(1), 10); return n >= 1 ? n - 1 : null; };
  addEventListener('keydown', e => { if (e.key === 'ArrowRight') ir(i + 1); else if (e.key === 'ArrowLeft') ir(i - 1); });
  addEventListener('hashchange', () => { const k = doEndereco(); if (k !== null) ir(k); });
  addEventListener('load', () => { const k = doEndereco(); if (k === null) window.prepararSlide(0); else ir(k); });
})();
