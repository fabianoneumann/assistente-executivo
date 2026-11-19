// Testes do iso.js, sem navegador: node .claude/skills/object-anatomy/scripts/teste_iso.js
// Os três primeiros são casos de uma revisão de código, e falhavam na versão anterior.
'use strict';
const assert = require('assert');
const ISO = require('./iso.js');

const casos = [];
const caso = (nome, f) => casos.push([nome, f]);

caso('a câmera não espelha: x da tela vezes o de cima dá a direção de quem vê', () => {
  for (const [az, el] of [[45, 30], [35, 20], [60, 45]]) {
    const cam = ISO.camera(az, el);
    const o = cam.P([0, 0, 0]), ex = cam.P([1, 0, 0]), ey = cam.P([0, 1, 0]), ez = cam.P([0, 0, 1]);
    // as colunas da projeção: o quanto cada eixo do mundo anda na tela (x para a direita, y para baixo)
    const tx = [ex[0] - o[0], ey[0] - o[0], ez[0] - o[0]], ty = [ex[1] - o[1], ey[1] - o[1], ez[1] - o[1]];
    const cima = ty.map(v => -v);
    const d = ISO.cruz(tx, cima);
    for (let k = 0; k < 3; k++) assert(Math.abs(d[k] - cam.D[k]) < 1e-9, `az ${az}, el ${el}: ${d} contra ${cam.D}`);
  }
});

caso('o texto na face de cima, com u e v de mão direita, não sai invertido', () => {
  const cam = ISO.camera(45, 30);
  const a = cam.L([1, 0, 0]), b = cam.L([0, -1, 0]);   // u e o "para baixo do texto" (-v), como o textoFace monta
  assert(a[0] * b[1] - a[1] * b[0] > 0, 'o determinante da matriz do texto devia ser positivo');
});

caso('o textoFace escapa o texto', () => {
  const s = ISO.textoFace(ISO.camera(), 'R&D <5V>', [0, 0, 0], [1, 0, 0], [0, 1, 0], 12);
  assert(s.includes('R&amp;D &lt;5V&gt;'), s);
});

caso('o encaixa aguenta a placa vista de lado e recusa a lista vazia', () => {
  const cam = ISO.encaixa(0, 0, [[0, 0, 0], [0, 0, 10]], [0, 0, 100, 100]);   // só altura na tela
  const p = cam.P([0, 0, 5]);
  assert(Number.isFinite(p[0]) && Number.isFinite(p[1]), String(p));
  assert.throws(() => ISO.encaixa(45, 30, [], [0, 0, 100, 100]));
});

caso('o estiloPapel enche de papel e contorna na tinta, e a face lisa só esconde a costura', () => {
  const est = ISO.estiloPapel('var(--papel-a)');
  assert(est([0, 0, 1], {}).includes('fill:var(--papel-a);stroke:var(--tinta);stroke-width:4'));
  assert(est([0, 0, 1], { liso: true }).startsWith('fill:var(--papel-a);stroke:var(--papel-a)'));
  const svg = ISO.pinta(ISO.camera(), ISO.cilindro([0, 0, 0], [0, 0, 1], 5, 10), { estilo: est, aresta: 'c' });
  assert(svg.includes('class="c"'), 'a silhueta da face lisa sai na classe pedida');
});

caso('sem estilo, o pinta sai no papel liso, sem tom; o tom só com op.tom', () => {
  const s = ISO.caixa(0, 10, 0, 10, 0, 10);
  assert(!ISO.pinta(ISO.camera(), s).includes('color-mix'), 'o padrão não pode ter tom');
  assert(ISO.pinta(ISO.camera(), s, { tom: true }).includes('color-mix'));
});

caso('a extrusão oblíqua tem normais de verdade: perpendiculares à face e para fora', () => {
  const quadrado = [[0, 0], [1, 0], [1, 1], [0, 1]];
  for (const [perfil, w] of [[quadrado, [1, 0, 1]], [quadrado.slice().reverse(), [1, 0, 1]], [quadrado, [0.5, 0.3, -1]], [quadrado, [0, 0, 2]]]) {
    const s = ISO.extrusao(perfil, [0, 0, 0], [1, 0, 0], [0, 1, 0], w);
    const todos = s.faces.flatMap(f => f.pts);
    const c = todos.reduce((a, p) => [a[0] + p[0] / todos.length, a[1] + p[1] / todos.length, a[2] + p[2] / todos.length], [0, 0, 0]);
    for (const f of s.faces) {
      const [a, b, d] = f.pts;
      const e1 = [b[0] - a[0], b[1] - a[1], b[2] - a[2]], e2 = [d[0] - a[0], d[1] - a[1], d[2] - a[2]];
      const dot = (x, y) => x[0] * y[0] + x[1] * y[1] + x[2] * y[2];
      assert(Math.abs(dot(f.n, e1)) < 1e-9 && Math.abs(dot(f.n, e2)) < 1e-9, `normal fora do plano da face, w ${w}`);
      const m = f.pts.reduce((acc, p) => [acc[0] + p[0] / f.pts.length, acc[1] + p[1] / f.pts.length, acc[2] + p[2] / f.pts.length], [0, 0, 0]);
      assert(dot(f.n, [m[0] - c[0], m[1] - c[1], m[2] - c[2]]) > 0, `normal para dentro, w ${w}`);
    }
  }
});

let falhas = 0;
for (const [nome, f] of casos) {
  try { f(); console.log(`ok   ${nome}`); } catch (e) { falhas++; console.log(`FALHA ${nome}: ${e.message}`); }
}
console.log(`${casos.length - falhas} de ${casos.length}`);
process.exit(falhas ? 1 : 0);
