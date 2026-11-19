"""A conferência por máquina do diagrama de fluxo, a 1280 px, no claro e no escuro (emulação real do
prefers-color-scheme), uma vez por arquivo de dados:
  - as do texto no SVG (`diagrama_conferir_svg.py`): texto pequeno, vazando, sobreposto, coberto, contraste;
  - as mesmas para o texto em HTML da figura (cartões, rótulos, cabeçalho, a faixa da versão): menor que 12 px,
    texto sobre texto, contraste abaixo de 4,5:1 contra o fundo efetivo, rolagem horizontal;
  - atravessa_no: aresta que passa por dentro de um cartão que não é origem nem destino
    (e a que entra no interior da própria origem ou destino, longe da borda);
  - ponta_fora: a ponta da seta que não toca a borda do cartão destino (tolerância 2 px), ou chega por dentro;
  - rotulo_sobre: rótulo de aresta sobre um cartão, sobre outro rótulo, ou cortado por uma aresta;
  - sai_do_cartao: texto que sai do cartão (cada linha medida pelo Range, mais o scroll do próprio cartão);
  - aresta_sobre_texto: aresta que passa por cima de qualquer texto da figura;
  - sem_rota: aresta do dado que não foi desenhada;
  - laco: a recusa que volta ao próprio passo e não se lê como laço: as duas pontas fora da base do mesmo cartão,
    as pernas mais juntas que o rótulo, o laço mais raso que o rótulo, ou o rótulo fora do laço.
  - antes do navegador, o esquema do dado (`diagrama_esquema.py`, com as regras do C4 no grafo e os limites da
    sequência); o dado que não serve não abre a página;
  - saida_longe: no grafo, o rótulo da saída de uma decisão (o nó com duas ou mais setas rotuladas saindo, como o
    "sim" e o "não" de uma pergunta) que não fica junto da saída: a mais de 24 px do começo da seta, ou mais perto
    do fim que do começo;
  - na sequência: seq_ponta, a seta que não sai ou não chega na linha de vida do participante (tolerância 2 px).
Cada achado leva um código estável (DG-..., ESQ-..., C4-..., SEQ-...) e uma dica de correção.
Uso: python -X utf8 diagrama_conferir.py [dados.json ...] [--saida <pasta>] [--json]
  -> imprime (ou, com --json, devolve o JSON) e grava <saida>/conferencia.json; sai com 1 se houver achado
     (os avisos do esquema, como dividir a sequência grande, não contam)."""
import argparse, json, shutil, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from diagrama_conferir_svg import JS as JS_SVG  # noqa: E402
import diagrama_esquema as esquema  # noqa: E402
import diagrama_render as render  # noqa: E402  (o mesmo modelo, a mesma pasta servida e a mesma abertura)

JS_PADRAO = r"""
() => {
  const out = {pequeno_html: [], sobreposto_html: [], contraste_html: [], atravessa_no: [], ponta_fora: [],
               rotulo_sobre: [], sai_do_cartao: [], aresta_sobre_texto: [], sem_rota: [], laco: [], saida_longe: []};
  const fig = document.querySelector('#figura');
  const R = e => e.getBoundingClientRect();
  const inter = (a, b, tol = 0) => Math.min(a.right, b.right) - Math.max(a.left, b.left) > tol && Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > tol;
  const dentro = (p, r, enc = 0) => p.x > r.left + enc && p.x < r.right - enc && p.y > r.top + enc && p.y < r.bottom - enc;
  const nome = e => (e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 40);

  // As linhas de texto em HTML (cada nó de texto, cada linha pelo Range).
  const linhas = [];
  const tw = document.createTreeWalker(fig, NodeFilter.SHOW_TEXT);
  for (let n = tw.nextNode(); n; n = tw.nextNode()) {
    if (!n.textContent.trim()) continue;
    const pai = n.parentElement; if (pai.closest('svg, script, .medida, .so-leitor')) continue;
    const cs = getComputedStyle(pai); if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    const rg = document.createRange(); rg.selectNodeContents(n);
    for (const r of rg.getClientRects()) if (r.width > 0.5 && r.height > 0.5) linhas.push({el: pai, txt: n.textContent.trim().slice(0, 40), r});
  }
  // texto pequeno
  const vistos = new Set();
  for (const l of linhas) { if (vistos.has(l.el)) continue; vistos.add(l.el);
    const px = parseFloat(getComputedStyle(l.el).fontSize); if (px < 11.95) out.pequeno_html.push({texto: l.txt, px}); }
  // texto sobre texto (linhas de elementos diferentes)
  for (let i = 0; i < linhas.length; i++) for (let j = i + 1; j < linhas.length; j++) {
    const a = linhas[i], b = linhas[j]; if (a.el === b.el || a.el.contains(b.el) || b.el.contains(a.el)) continue;
    const w = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left), h = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
    if (w > 1 && h > 3) out.sobreposto_html.push([a.txt, b.txt]);
  }
  // contraste: a cor do texto contra o primeiro fundo opaco dos ancestrais
  const parse = c => { const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(',').map(Number); return {r:p[0], g:p[1], b:p[2], a: p.length > 3 ? p[3] : 1}; };
  const lum = c => { const f = v => { v /= 255; return v <= 0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4); }; return 0.2126*f(c.r) + 0.7152*f(c.g) + 0.0722*f(c.b); };
  const razao = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05); };
  vistos.clear();
  for (const l of linhas) { if (vistos.has(l.el)) continue; vistos.add(l.el);
    let fundo = null; for (let e = l.el; e; e = e.parentElement) { const c = parse(getComputedStyle(e).backgroundColor); if (c && c.a >= 0.99) { fundo = c; break; } }
    fundo = fundo || parse(getComputedStyle(document.body).backgroundColor);
    const cor = parse(getComputedStyle(l.el).color);
    if (cor && fundo) { const k = razao(cor, fundo); if (k < 4.5) out.contraste_html.push({texto: l.txt, razao: +k.toFixed(2)}); }
  }

  // Cartões, rótulos, arestas.
  const cartoes = Object.fromEntries([...document.querySelectorAll('.grafo .no')].map(c => [c.dataset.id, c]));
  const rotulos = [...document.querySelectorAll('.grafo .rotulo-aresta')];
  const arestas = [...document.querySelectorAll('.grafo path.aresta')];
  const amostra = p => { const t = p.getTotalLength(), m = p.getScreenCTM(), pts = [];
    for (let s = 0; s <= t; s += 1.5) { const q = p.getPointAtLength(s); pts.push({x: m.a*q.x + m.c*q.y + m.e, y: m.b*q.x + m.d*q.y + m.f, s}); }
    const q = p.getPointAtLength(t); pts.push({x: m.a*q.x + m.c*q.y + m.e, y: m.b*q.x + m.d*q.y + m.f, s: t}); return pts; };
  const dBorda = (p, r) => { // distância do ponto à borda do retângulo
    const dx = Math.max(r.left - p.x, 0, p.x - r.right), dy = Math.max(r.top - p.y, 0, p.y - r.bottom);
    if (dx || dy) return Math.hypot(dx, dy);
    return Math.min(p.x - r.left, r.right - p.x, p.y - r.top, r.bottom - p.y); };
  const total = D => D.length;
  const esperadas = JSON.parse(document.body.dataset.arestas || '0');
  if (esperadas && arestas.length !== esperadas) out.sem_rota.push({desenhadas: arestas.length, no_dado: esperadas});
  for (const a of arestas) {
    const de = a.dataset.de, para = a.dataset.para, rot = `${de} -> ${para} (${a.dataset.tipo})`;
    const pts = amostra(a);
    if (pts.length < 2) { out.sem_rota.push(rot); continue; }
    // atravessa um cartão alheio; ou entra fundo na própria origem/destino
    for (const [id, c] of Object.entries(cartoes)) {
      const r = R(c), proprio = id === de || id === para;
      const hit = pts.find(p => dentro(p, r, proprio ? 3 : 1));
      if (hit) { out.atravessa_no.push({aresta: rot, cartao: id, proprio}); }
    }
    // a ponta toca a borda do destino e chega de fora
    const fim = pts[pts.length - 1], rd = R(cartoes[para]);
    const d = dBorda(fim, rd);
    const antes = pts.filter(p => p.s <= fim.s - 6).pop();
    const chegaDeFora = antes && !dentro(antes, rd, 0);
    if (d > 2 || !chegaDeFora || !a.getAttribute('marker-end')) out.ponta_fora.push({aresta: rot, distancia_px: +d.toFixed(1), chega_de_fora: !!chegaDeFora});
    // aresta por cima de texto (qualquer linha de texto da figura, menos o rótulo dela mesma)
    for (const l of linhas) {
      if (l.el.closest('.rotulo-aresta')?.dataset.aresta === a.dataset.indice) continue;
      if (pts.some(p => dentro(p, l.r, 0.5))) { out.aresta_sobre_texto.push({aresta: rot, texto: l.txt}); }
    }
    a._pts = pts;
  }
  // os traços da faixa da versão (a linha do main e as hastes) também não passam por cima de texto
  for (const t of document.querySelectorAll('.trilho > svg line')) {
    const m = t.getScreenCTM(), x1 = +t.getAttribute('x1'), y1 = +t.getAttribute('y1'), x2 = +t.getAttribute('x2'), y2 = +t.getAttribute('y2');
    const L = Math.hypot(x2 - x1, y2 - y1);
    for (let s = 0; s <= L; s += 1.5) { const q = {x: x1 + (x2 - x1) * s / L, y: y1 + (y2 - y1) * s / L};
      const p = {x: m.a*q.x + m.c*q.y + m.e, y: m.b*q.x + m.d*q.y + m.f};
      const l = linhas.find(l => dentro(p, l.r, 0.5)); if (l) { out.aresta_sobre_texto.push({aresta: 'traço da versão', texto: l.txt}); break; } }
  }
  // rótulos: sobre cartão, sobre outro rótulo, cortado por aresta (inclusive a sua)
  const outrosRotulos = [...document.querySelectorAll('.rotulo-grupo, .grafo .rotulo-aresta')];
  for (const r of rotulos) {
    const rr = R(r);
    for (const [id, c] of Object.entries(cartoes)) if (inter(rr, R(c), 0.5)) out.rotulo_sobre.push({rotulo: nome(r), sobre: 'cartão ' + id});
    for (const o of outrosRotulos) if (o !== r && inter(rr, R(o), 0.5)) out.rotulo_sobre.push({rotulo: nome(r), sobre: 'rótulo ' + nome(o)});
    for (const a of arestas) if ((a._pts || []).some(p => dentro(p, rr, 0.5))) out.rotulo_sobre.push({rotulo: nome(r), sobre: `aresta ${a.dataset.de} -> ${a.dataset.para}`});
  }
  // texto que sai do cartão
  for (const [id, c] of Object.entries(cartoes)) {
    const rc = R(c);
    for (const l of linhas) if (c.contains(l.el)) {
      const r = l.r; if (r.left < rc.left - 1 || r.right > rc.right + 1 || r.top < rc.top - 1 || r.bottom > rc.bottom + 1)
        out.sai_do_cartao.push({cartao: id, texto: l.txt});
    }
    if (c.scrollHeight > c.clientHeight + 1 || c.scrollWidth > c.clientWidth + 1) out.sai_do_cartao.push({cartao: id, texto: '(o conteúdo passa da caixa)'});
    // e o que transborda de um filho do cartão (o selo, por exemplo)
    for (const f of c.querySelectorAll('*')) if (f.scrollWidth > f.clientWidth + 1 && getComputedStyle(f).overflow !== 'visible') out.sai_do_cartao.push({cartao: id, texto: nome(f)});
  }
  // o laço da recusa: sai e entra pela base do próprio cartão, abre o bastante para o rótulo, e o rótulo fica dentro
  for (const a of arestas.filter(a => a.dataset.laco)) {
    const rot = `${a.dataset.de} (laço)`, pts = a._pts || [], c = cartoes[a.dataset.de];
    if (!c || pts.length < 2) { out.laco.push({laco: rot, motivo: 'sem cartão ou sem rota'}); continue; }
    const rc = R(c), ini = pts[0], fim = pts[pts.length - 1];
    if (Math.abs(ini.y - rc.bottom) > 2 || Math.abs(fim.y - rc.bottom) > 2 || ini.x < rc.left || ini.x > rc.right || fim.x < rc.left || fim.x > rc.right)
      out.laco.push({laco: rot, motivo: 'as pontas não estão na base do cartão'});
    const fundo = Math.max(...pts.map(p => p.y)), x0 = Math.min(ini.x, fim.x), x1 = Math.max(ini.x, fim.x);
    const r = document.querySelector(`.grafo .rotulo-aresta[data-aresta="${a.dataset.indice}"]`);
    if (!r) { out.laco.push({laco: rot, motivo: 'sem rótulo'}); continue; }
    const rr = R(r);
    if (x1 - x0 < rr.width + 8) out.laco.push({laco: rot, motivo: 'as pernas mais juntas que o rótulo', vao_px: +(x1 - x0).toFixed(1), rotulo_px: +rr.width.toFixed(1)});
    if (fundo - rc.bottom < rr.height + 6) out.laco.push({laco: rot, motivo: 'o laço mais raso que o rótulo', fundo_px: +(fundo - rc.bottom).toFixed(1)});
    if (rr.left < x0 || rr.right > x1 || rr.top < rc.bottom || rr.bottom > fundo) out.laco.push({laco: rot, motivo: 'o rótulo fora do laço'});
  }
  // a saída de decisão: o rótulo junto do começo da seta (da pergunta), e não do destino
  const dRet = (p, r) => Math.hypot(Math.max(r.left - p.x, 0, p.x - r.right), Math.max(r.top - p.y, 0, p.y - r.bottom));
  // a saída de decisão sai do próprio desenho (não da marca da página): a origem com dois ou mais rótulos saindo;
  // só no grafo (no fluxo, o rótulo da recusa e da volta tem o lugar dele, conferido pelo laço)
  const doRotulo = r => arestas.find(a => a.dataset.indice === r.dataset.aresta);
  const porOrigem = {}; for (const r of rotulos) { const a = doRotulo(r); if (a) porOrigem[a.dataset.de] = (porOrigem[a.dataset.de] || 0) + 1; }
  // fora do C4 (toda seta lá tem rótulo, e o contêiner com duas relações não é pergunta)
  const ehGrafo = (!!document.querySelector('.caixa-grupo') || document.body.dataset.modelo === 'grafo') && !document.body.dataset.c4;
  for (const r of rotulos.filter(r => ehGrafo && porOrigem[(doRotulo(r) || {dataset: {}}).dataset.de] >= 2)) {
    const a = doRotulo(r), pts = (a && a._pts) || [];
    if (pts.length < 2) { out.saida_longe.push({rotulo: nome(r), motivo: 'sem a seta'}); continue; }
    const rr = R(r), dIni = dRet(pts[0], rr), dFim = dRet(pts[pts.length - 1], rr);
    if (dIni > 24 || dIni >= dFim) out.saida_longe.push({rotulo: nome(r), aresta: `${a.dataset.de} -> ${a.dataset.para}`,
      do_comeco_px: +dIni.toFixed(1), do_fim_px: +dFim.toFixed(1)});
  }
  out.rolagem_horizontal = document.documentElement.scrollWidth > window.innerWidth;
  out.linhas_de_texto = linhas.length; out.cartoes = Object.keys(cartoes).length; out.arestas = arestas.length;
  out.layout = document.body.dataset.layout;
  return out;
}
"""

JS_SEQ = r"""
() => {
  const out = {seq_ponta: []};
  const vida = Object.fromEntries([...document.querySelectorAll('.seq .vida')].map(v => [v.dataset.id, v.getBoundingClientRect().left]));
  for (const ln of document.querySelectorAll('.seq .linha.msg')) {
    const de = ln.dataset.de, para = ln.dataset.para, rot = `${ln.dataset.n}. ${de} -> ${para}`;
    if (de === para) { const a = ln.querySelector('.auto'); const r = a && a.getBoundingClientRect();
      if (!r || Math.abs(r.left - vida[de]) > 2) out.seq_ponta.push({mensagem: rot, motivo: 'o laço não sai da linha de vida'}); continue; }
    const a = ln.querySelector('.seta'); if (!a) { out.seq_ponta.push({mensagem: rot, motivo: 'sem seta'}); continue; }
    const r = a.getBoundingClientRect(), x1 = vida[de], x2 = vida[para];
    if (x1 == null || x2 == null) { out.seq_ponta.push({mensagem: rot, motivo: 'participante sem linha de vida'}); continue; }
    const desvio = Math.max(Math.abs(r.left - Math.min(x1, x2)), Math.abs(r.right - Math.max(x1, x2)));
    if (desvio > 2) out.seq_ponta.push({mensagem: rot, motivo: 'a seta não vai de uma linha de vida à outra', desvio_px: +desvio.toFixed(1)});
  }
  return out;
}
"""

CHAVES_SVG = ("pequeno", "vaza_svg", "vaza_forma", "coberto", "sobreposto", "contraste")
# O código estável e a dica de cada chave da conferência no navegador (os do esquema vêm do diagrama_esquema.py).
CODIGOS = {
    "pequeno_html": ("DG-TEXTO-PEQUENO", "suba a fonte para pelo menos 12 px, no token do papel"),
    "sobreposto_html": ("DG-TEXTO-SOBRE-TEXTO", "afaste os dois textos: mais espaço entre camadas ou rótulo mais curto"),
    "contraste_html": ("DG-CONTRASTE", "troque a cor pelo token de tinta ou de suave, que passam 4,5:1 no claro e no escuro"),
    "atravessa_no": ("DG-SETA-ATRAVESSA", "aumente o espaço entre aresta e nó (--esp-aresta-no) ou mude a ordem dos nós no dado"),
    "ponta_fora": ("DG-PONTA-FORA", "a seta tem de terminar na borda do cartão de destino; confira as portas do nó"),
    "rotulo_sobre": ("DG-ROTULO-SOBRE", "encurte o rótulo ou dê mais espaço entre camadas (--esp-camada)"),
    "sai_do_cartao": ("DG-TEXTO-SAI", "encurte o texto ou aumente a largura máxima do cartão"),
    "aresta_sobre_texto": ("DG-SETA-SOBRE-TEXTO", "mude a ordem dos nós ou o espaço, para a seta contornar o texto"),
    "sem_rota": ("DG-SEM-ROTA", "toda aresta do dado precisa sair desenhada; confira se o motor achou rota"),
    "laco": ("DG-LACO", "o laço da recusa sai e volta pela base do próprio cartão, com o rótulo dentro"),
    "rolagem_horizontal": ("DG-ROLAGEM", "a figura não cabe na largura; reduza colunas ou deixe a lista assumir"),
    "saida_longe": ("DG-SAIDA-LONGE", "o rótulo da saída de uma decisão (sim, não) vai junto da pergunta; confira o TAIL do rótulo no grafo.html"),
    "seq_ponta": ("SEQ-PONTA", "a seta da sequência vai de uma linha de vida à outra; confira os participantes da mensagem"),
}
CODIGOS.update({"svg_" + c: ("DG-SVG-" + c.upper().replace("_", "-"), "o texto do SVG tem de caber, não se sobrepor e ter contraste")
                for c in CHAVES_SVG})
CHAVES = ("pequeno_html", "sobreposto_html", "contraste_html", "atravessa_no", "ponta_fora", "rotulo_sobre",
          "sai_do_cartao", "aresta_sobre_texto", "sem_rota", "laco", "saida_longe")


def main():
    from playwright.sync_api import sync_playwright
    ap = argparse.ArgumentParser()
    ap.add_argument("dados", nargs="*")
    ap.add_argument("--saida", default=".")
    ap.add_argument("--json", action="store_true", help="devolve o resultado em JSON em vez das linhas de texto")
    a = ap.parse_args()
    alvos = render.alvos_de(a.dados)
    # o esquema antes do navegador: o dado que não serve não abre a página, e o achado já diz a causa
    res, n_achados, para_o_navegador = {}, 0, []
    for d in alvos:
        ach = esquema.validar_arquivo(d)
        erros = [x for x in ach if x["nivel"] == "erro"]
        if ach:
            res.setdefault(d.stem, {})["esquema"] = ach
        n_achados += len(erros)
        if not a.json:
            for x in ach:
                print(f"{d.stem} [esquema] {x['nivel'].upper()} {x['codigo']} {x['onde']}: {x['mensagem']} (dica: {x['dica']})")
        if not erros:
            para_o_navegador.append(d)
    alvos = para_o_navegador
    if not alvos:
        return _fim(a, res, n_achados)
    raiz = render.pasta_servida(alvos)
    srv = render.servidor(raiz); porta = srv.server_address[1]
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch(args=["--disable-lcd-text"])
            for tema, nome in (("light", "claro"), ("dark", "escuro")):
                ctx = nav.new_context(viewport={"width": 1280, "height": 900}, color_scheme=tema)
                pg = ctx.new_page()
                for d in alvos:
                    render.abrir(pg, porta, render.nome_de(d), render.pagina_de(d))
                    n_dado = len(json.loads(d.read_text(encoding="utf-8")).get("arestas") or [])
                    pg.evaluate(f"document.body.dataset.arestas = '{n_dado}'")
                    r = pg.evaluate(JS_PADRAO)
                    rs = pg.evaluate(JS_SVG)
                    probs = {c: r[c] for c in CHAVES if r.get(c)}
                    if render.pagina_de(d) == "sequencia.html":
                        probs.update({k: v for k, v in pg.evaluate(JS_SEQ).items() if v})
                    probs.update({"svg_" + c: rs[c] for c in CHAVES_SVG if rs.get(c)})
                    if r["rolagem_horizontal"]:
                        probs["rolagem_horizontal"] = True
                    n = sum(len(v) if isinstance(v, list) else 1 for v in probs.values())
                    n_achados += n
                    codigos = [{"chave": k, "codigo": CODIGOS.get(k, ("DG-" + k.upper(), ""))[0],
                                "dica": CODIGOS.get(k, ("", ""))[1], "detalhe": v} for k, v in probs.items()]
                    res.setdefault(Path(render.nome_de(d)).stem, {})[nome] = {"achados": n, "problemas": probs, "codigos": codigos, "medidas": {
                        k: r[k] for k in ("linhas_de_texto", "cartoes", "arestas", "layout")}}
                    if a.json:
                        continue
                    print(f"{Path(render.nome_de(d)).stem} [{nome}] cartões={r['cartoes']} arestas={r['arestas']} linhas={r['linhas_de_texto']}"
                          f" layout={r['layout']} ->", "0 achados" if not n else f"{n} achados " + json.dumps(probs, ensure_ascii=False))
                ctx.close()
            nav.close()
    finally:
        srv.shutdown(); shutil.rmtree(raiz, ignore_errors=True)
    return _fim(a, res, n_achados)


def _fim(a, res, n_achados):
    saida = Path(a.saida); saida.mkdir(parents=True, exist_ok=True)
    (saida / "conferencia.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    if a.json:
        print(json.dumps({"total": n_achados, "resultado": res}, ensure_ascii=False, indent=1))
    else:
        print(f"total: {n_achados} achados")
    sys.exit(1 if n_achados else 0)


if __name__ == "__main__":
    main()
