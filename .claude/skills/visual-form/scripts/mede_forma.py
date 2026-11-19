"""As medidas objetivas da forma, por tela, que a trava da I2 lê (`references/i2.md`): negrito no corpo, margem lateral
do texto, a caixa do maior desenho, linhas de texto, marcas e o destaque manuscrito.

    python -X utf8 mede_forma.py <slides.html> [saida.json] [--estatico] [--fora SELETOR ...] [--desenho SELETOR ...]

Por tela sai também `corpo`, o número de blocos `.corpo` com texto, e `modo`. Dois modos:

- **no navegador** (padrão): o Chromium do Playwright, como a `slides-export`, com a tela preparada pelo
  `window.prepararSlide` do `caderno.js` quando existe. Antes de medir, pede as fontes do texto da tela e confere se
  carregaram (`slides-export/scripts/fontes.py`): se faltar alguma, sai sem medida,
  código 3, porque margem e linhas seriam da fonte de reserva.
- **`--estatico`**, sem navegador: só o que se conta pelas classes do HTML (o destaque manuscrito, o negrito no corpo,
  as marcas e o `corpo`). A margem, as linhas, o maior desenho e o `transborda` (que o `caderno.js` marca em tempo de
  execução) saem `null`: ausente, não zero. Serve à versão guardada cujo CSS não resolve (a cópia em `versions/`, que
  linka o `caderno.css` por um caminho relativo que dali não existe) e ao teste.

O maior desenho conta `svg.traco` (fora as `.marcas`), `img.desenho`, `figure.foto` e o que tiver `data-desenho`;
`--desenho` acrescenta seletores (um desenho com `id` próprio) e `--fora` tira os que se repetem em todas as telas (uma
faixa que atravessa a sequência). A tela sem texto medível sai com a margem `null`. Com `saida.json`, grava em UTF-8 com fim de linha LF.
Códigos: 0 medido; 2 entrada ruim (ou a saída que não grava); 3 fonte não carregou; 4 o navegador falhou (sem medida).
"""
import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path

AQUI = Path(__file__).resolve().parent
EXPORT = AQUI.parents[1] / "slides-export" / "scripts"

DESTAQUE = {"destaque", "citacao"}
MARCAS = {"circulo": {"circulo"}, "sublinha": {"sublinha"}, "marca_texto": {"marca"}, "notas_acento": {"nota", "margem"}}
VAZIOS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class _Telas(HTMLParser):
    """Conta, por `.slide`, os elementos pelas classes, como o `querySelectorAll` do modo navegador (cada elemento uma vez)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pilha = []      # [tag, classes, é a tela?, o .corpo já contou? (None se não é .corpo)]
        self.telas = []
        self.atual = None

    def _abre(self, tag, attrs, vazio):
        cls = set((dict(attrs).get("class") or "").split())
        tela = self.atual is None and "slide" in cls
        if tela:
            self.telas.append({"destaque": 0, "negrito": 0, "corpo": 0,
                               "marcas": {k: 0 for k in MARCAS}})
            self.atual = len(self.telas) - 1
        elif self.atual is not None:
            t = self.telas[self.atual]
            if cls & DESTAQUE:
                t["destaque"] += 1
            for nome, alvo in MARCAS.items():
                if cls & alvo:
                    t["marcas"][nome] += 1
            if tag in ("b", "strong") and any("corpo" in e[1] for e in self.pilha):
                t["negrito"] += 1
        if not vazio:
            self.pilha.append([tag, cls, tela, False if (self.atual is not None and "corpo" in cls) else None])

    def handle_starttag(self, tag, attrs):
        self._abre(tag, attrs, tag in VAZIOS)

    def handle_startendtag(self, tag, attrs):
        self._abre(tag, attrs, True)

    def handle_endtag(self, tag):
        for k in range(len(self.pilha) - 1, -1, -1):
            if self.pilha[k][0] == tag:
                if any(e[2] for e in self.pilha[k:]):
                    self.atual = None
                del self.pilha[k:]
                return

    def handle_data(self, data):
        if self.atual is None or not data.strip():
            return
        for e in self.pilha:
            if e[3] is False:    # o .corpo aberto que ainda não tinha texto: conta uma vez, como o filtro do navegador
                e[3] = True
                self.telas[self.atual]["corpo"] += 1


def medir_estatico(html):
    """As medidas que não dependem de layout, lidas do HTML. Margem, linhas e maior desenho saem None."""
    p = _Telas()
    p.feed(Path(html).read_text(encoding="utf-8"))
    p.close()
    if not p.telas:
        raise ValueError(f"nenhuma .slide em {html}")
    return [{"tela": i + 1, "modo": "estatico", "negrito": t["negrito"], "corpo": t["corpo"],
             "margem_esq_min": None, "margem_dir_min": None, "linhas_texto": None, "maior_desenho": None,
             "marcas": t["marcas"], "destaque_manuscrito": t["destaque"], "transborda": None}
            for i, t in enumerate(p.telas)]


JS = r"""
async ([i, fora, extra]) => {
  const carregarFontes = %s;
  const telas = document.querySelectorAll('.slide');
  const s = telas[i];
  telas.forEach((x, j) => x.classList.toggle('active', j === i));
  const faltam = await carregarFontes(s);
  if (window.prepararSlide) await window.prepararSlide(i);
  faltam.push(...await carregarFontes(s));
  if (faltam.length) return {tela: i + 1, faltam};
  const o = s.getBoundingClientRect();
  const R = el => { const r = el.getBoundingClientRect(); return {x: Math.round(r.left - o.left), y: Math.round(r.top - o.top), w: Math.round(r.width), h: Math.round(r.height)}; };
  const textos = [...s.querySelectorAll('p, h1, h2, li')].filter(e => !e.closest('svg') && e.textContent.trim()
      && !e.matches('.moldura, .arroba, .pagina') && !e.closest('.folha-b') && !e.querySelector('p, li'));
  let esq = 1080, dir = 1080, linhas = 0;
  for (const e of textos) {
    for (const q of e.getClientRects()) { esq = Math.min(esq, q.left - o.left); dir = Math.min(dir, o.right - q.right); }
    const lh = parseFloat(getComputedStyle(e).lineHeight) || 48;
    linhas += Math.round(e.getBoundingClientRect().height / lh);
  }
  const base = ['svg.traco:not(.marcas)', 'img.desenho', 'figure.foto', '[data-desenho]', ...extra].join(', ');
  const desenhos = [...s.querySelectorAll(base)].filter(e => !fora.some(f => e.matches(f)))
      .map(e => ({quem: e.id || e.getAttribute('class') || e.tagName.toLowerCase(), ...R(e)}));
  desenhos.sort((a, b) => b.w * b.h - a.w * a.h);
  return {
    tela: i + 1, modo: 'navegador',
    negrito: s.querySelectorAll('.corpo b, .corpo strong').length,
    corpo: [...s.querySelectorAll('.corpo')].filter(e => e.textContent.trim()).length,
    margem_esq_min: textos.length ? Math.round(esq) : null, margem_dir_min: textos.length ? Math.round(dir) : null,
    linhas_texto: linhas,
    maior_desenho: desenhos[0] || null,
    marcas: {circulo: s.querySelectorAll('.circulo').length, sublinha: s.querySelectorAll('.sublinha').length,
             marca_texto: s.querySelectorAll('.marca').length,
             notas_acento: s.querySelectorAll('.nota, .margem').length},
    destaque_manuscrito: s.querySelectorAll('.destaque, .citacao').length,
    transborda: s.classList.contains('transborda'),
  };
}
"""


def medir_navegador(html, fora=(), extra=()):
    """As medidas no Chromium. Devolve (medidas, faltam): com fonte faltando, medidas vazia e a lista do que faltou."""
    sys.path.insert(0, str(EXPORT))
    from fontes import CARREGAR_FONTES
    from playwright.sync_api import sync_playwright

    js = JS % CARREGAR_FONTES
    out, faltam = [], []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--disable-lcd-text"])
        try:
            pg = b.new_page(viewport={"width": 1280, "height": 1560})
            pg.goto(Path(html).resolve().as_uri())
            pg.wait_for_load_state("networkidle")
            n = pg.evaluate("document.querySelectorAll('.slide').length")
            if not n:
                raise ValueError(f"nenhuma .slide em {html}")
            for i in range(n):
                m = pg.evaluate(js, [i, list(fora), list(extra)])
                if "faltam" in m:
                    faltam += [{"tela": m["tela"], **f} for f in m["faltam"]]
                else:
                    out.append(m)
        finally:
            b.close()
    return ([] if faltam else out), faltam


def linha(m):
    d = m["maior_desenho"]
    dd = f"{d['quem']} {d['w']}x{d['h']}" if d else ("nenhum" if m["modo"] == "navegador" else "não medido")
    mg = "não medida" if m["margem_esq_min"] is None else f"{m['margem_esq_min']}/{m['margem_dir_min']}"
    ln = "não medidas" if m["linhas_texto"] is None else m["linhas_texto"]
    return (f"tela {m['tela']:2}: negrito {m['negrito']} (corpo {m['corpo']}), margem {mg}, linhas {ln}, "
            f"maior desenho {dd}, marcas {m['marcas']}, destaque {m['destaque_manuscrito']}"
            + (" TRANSBORDA" if m["transborda"] else ""))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("html")
    ap.add_argument("saida", nargs="?")
    ap.add_argument("--estatico", action="store_true", help="sem navegador: só o que se conta pelas classes")
    ap.add_argument("--fora", nargs="*", default=[], metavar="SELETOR", help="desenhos que não contam (o que se repete em todas as telas)")
    ap.add_argument("--desenho", nargs="*", default=[], metavar="SELETOR", help="desenhos a mais (por id ou classe)")
    a = ap.parse_args(argv)
    html = Path(a.html)
    if not html.is_file():
        print(f"ERRO: não existe {html}", file=sys.stderr)
        return 2
    try:
        if a.estatico:
            out = medir_estatico(html)
        else:
            out, faltam = medir_navegador(html, a.fora, a.desenho)
            if faltam:
                for f in faltam:
                    print(f"ERRO fonte_nao_carregada: tela {f['tela']}, {f.get('fonte')} ({f.get('amostra', '')!r})")
                print("Nenhuma medida: margem e linhas seriam da fonte de reserva.")
                return 3
    except ValueError as e:
        print(f"ERRO: {e}", file=sys.stderr)
        return 2
    except Exception as e:   # o Playwright sem navegador, o prazo, um erro no prepararSlide: nenhuma medida
        print(f"ERRO: o navegador não mediu ({type(e).__name__}: {e}); nenhuma medida", file=sys.stderr)
        return 4
    for m in out:
        print(linha(m))
    if a.saida:
        try:
            Path(a.saida).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
        except OSError as e:
            print(f"ERRO: não gravou {a.saida}: {e}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
