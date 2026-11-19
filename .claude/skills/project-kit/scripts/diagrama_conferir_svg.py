"""As conferências do texto no SVG das figuras (o módulo que o `diagrama_conferir.py` importa):
texto menor que 12 px no tamanho desenhado, texto que vaza do SVG ou da forma que o contém, texto sobre texto,
texto coberto por uma forma pintada depois, e contraste do texto contra o fundo abaixo de 4,5:1."""

JS = r"""
() => {
  const out = {pequeno: [], vaza_svg: [], vaza_forma: [], sobreposto: [], contraste: []};
  const parse = c => { const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(',').map(Number); return {r:p[0], g:p[1], b:p[2], a: p.length > 3 ? p[3] : 1}; };
  const lum = c => { const f = v => { v /= 255; return v <= 0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4); };
    return 0.2126*f(c.r) + 0.7152*f(c.g) + 0.0722*f(c.b); };
  const razao = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05); };
  const fundoPag = parse(getComputedStyle(document.body).backgroundColor);
  const nome = t => (t.textContent || '').trim().slice(0, 40);
  for (const svg of document.querySelectorAll('svg')) {
    const sr = svg.getBoundingClientRect();
    const vb = svg.viewBox.baseVal; const esc = vb && vb.width ? sr.width / vb.width : 1;
    const todos = [...svg.querySelectorAll('*')];
    const formas = todos.filter(e => ['rect','circle','ellipse','polygon','path'].includes(e.tagName) && !e.closest('defs,marker'))
      .map(e => ({e, i: todos.indexOf(e), r: e.getBoundingClientRect(), cs: getComputedStyle(e)}))
      .filter(f => { const c = parse(f.cs.fill); return f.cs.fill !== 'none' && c && c.a > 0 && f.cs.fillOpacity !== '0' && f.cs.opacity !== '0'
        && f.r.width > 4 && f.r.height > 4; });
    const textos = [...svg.querySelectorAll('text')].filter(t => nome(t));
    const caixas = [];
    for (const t of textos) {
      const r = t.getBoundingClientRect(); const cs = getComputedStyle(t);
      const px = parseFloat(cs.fontSize) * esc;
      if (px < 11.95) out.pequeno.push({texto: nome(t), px: +px.toFixed(1)});
      if (r.left < sr.left - 1 || r.right > sr.right + 1 || r.top < sr.top - 1 || r.bottom > sr.bottom + 1)
        out.vaza_svg.push({texto: nome(t)});
      const cx = (r.left + r.right)/2, cy = (r.top + r.bottom)/2, it = todos.indexOf(t);
      const conts = formas.filter(f => f.i < it && f.r.left <= cx && cx <= f.r.right && f.r.top <= cy && cy <= f.r.bottom)
        .sort((a, b) => b.i - a.i);  // a pintada por último, por cima
      const c = conts[0];
      // a forma de fundo: só conta como recipiente se o texto cabe nela pela altura (não é uma faixa fina sob o texto)
      if (c && c.r.height >= r.height * 0.9) {
        const tol = 1;
        if (r.left < c.r.left - tol || r.right > c.r.right + tol || r.top < c.r.top - tol || r.bottom > c.r.bottom + tol)
          out.vaza_forma.push({texto: nome(t), forma: c.e.tagName + (c.e.getAttribute('class') ? '.' + c.e.getAttribute('class') : ''),
            excesso_px: +Math.max(c.r.left - r.left, r.right - c.r.right, c.r.top - r.top, r.bottom - c.r.bottom).toFixed(1)});
      }
      // contraste: a cor do texto contra a primeira forma opaca atrás dele, senão o fundo da página
      let fundo = null;
      for (const f of conts) { const fc = parse(f.cs.fill); const op = parseFloat(f.cs.fillOpacity) * parseFloat(f.cs.opacity);
        if (fc && fc.a * op >= 0.99) { fundo = fc; break; } }
      fundo = fundo || fundoPag;
      const cor = parse(cs.fill);
      if (cor && fundo) { const k = razao(cor, fundo); if (k < 4.5) out.contraste.push({texto: nome(t), razao: +k.toFixed(2), cor: cs.fill}); }
      // coberto: uma forma opaca pintada depois do texto, por cima de parte dele
      for (const f of formas) {
        if (f.i <= it) continue;
        const fc = parse(f.cs.fill); if (!fc || fc.a * parseFloat(f.cs.fillOpacity) * parseFloat(f.cs.opacity) < 0.6) continue;
        const w = Math.min(r.right, f.r.right) - Math.max(r.left, f.r.left), h = Math.min(r.bottom, f.r.bottom) - Math.max(r.top, f.r.top);
        if (w > 2 && h > 3) { out.coberto = out.coberto || []; out.coberto.push({texto: nome(t), por: f.e.tagName + (f.e.getAttribute('class') ? '.' + f.e.getAttribute('class') : '')}); break; }
      }
      caixas.push({t: nome(t), r});
    }
    for (let i = 0; i < caixas.length; i++) for (let j = i + 1; j < caixas.length; j++) {
      const a = caixas[i].r, b = caixas[j].r;
      const w = Math.min(a.right, b.right) - Math.max(a.left, b.left), h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
      if (w > 1 && h > 3) out.sobreposto.push([caixas[i].t, caixas[j].t]);
    }
    out.textos = (out.textos || 0) + textos.length;
    out.escala = +esc.toFixed(3);
  }
  out.rolagem_horizontal = document.documentElement.scrollWidth > window.innerWidth;
  return out;
}
"""
