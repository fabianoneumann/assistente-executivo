"""Conta os papéis tipográficos de conteúdo por tela nas peças da série (a medida de uma regra como "até 3 papéis
tipográficos de conteúdo por tela, rótulo incluído; moldura fora"), para quem cuida da série decidir o teto antes de
pôr a regra na rubrica de design. Só mede: não é conferência e não entra na exportação.

O papel de um elemento vem da classe, pela tabela CLASSE_PAPEL do medidas_forma.py (citação, título, destaque, nota e
margem como nota, fila, link, apoio, fonte, corpo), com o mesmo filtro de visibilidade das conferências (fora do svg e do
adesivo simulado, visível, com texto). Opções: --rotulo conta também o rótulo (.rot, .leg) como um papel, como a rubrica
pede ("rótulo incluído"); --sem-fonte tira a .fonte, que o design system trata como metadado.

Uso: python -X utf8 conta_papeis.py [pasta da série] [--rotulo] [--sem-fonte] [--teto N] [--json saida.json]
Sai com a distribuição (quantas telas com 1, 2, 3... papéis) e as telas acima do teto (padrão 3).
"""
import argparse, json, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import medidas_forma as mf  # noqa: E402
from conferir_telas import PREPARAR  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]
SERIE = ROOT / "marketing/social-media/carousels/series/exemplo"

CONTAR = r"""([idx, rotulo, semFonte]) => {
  const sl = document.querySelectorAll('.slide')[idx];
  const tipo = sl.classList.contains('tipo-a') ? 'a' : sl.classList.contains('tipo-b') ? 'b' : null;
  if (!tipo) return null;
  const fora = e => !!e.closest('svg,.sim,[data-adesivo-sim],.moldura,.pagina,.arroba');
  const vis = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
                     return r.width > 1 && r.height > 1 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const PAPEL = """ + "[" + ",".join(f"['{c}','{p}']" for c, p in mf.CLASSE_PAPEL) + "]" + r""".concat(rotulo ? [['rot','rotulo'],['leg','rotulo']] : [])
                 .filter(x => !(semFonte && x[1] === 'fonte'));
  const papeis = new Set();
  for (const el of sl.querySelectorAll(PAPEL.map(x => '.' + x[0]).join(','))) {
    if (fora(el) || !vis(el) || !el.textContent.trim()) continue;
    papeis.add(PAPEL.find(x => el.classList.contains(x[0]))[1]);
  }
  return [...papeis].sort();
}"""


def contar(serie, rotulo, sem_fonte):
    from playwright.sync_api import sync_playwright
    telas = []
    with sync_playwright() as pw:
        br = pw.chromium.launch(args=["--disable-lcd-text"])
        page = br.new_page(viewport={"width": 1280, "height": 1560})
        for peca in sorted(p for p in serie.iterdir() if (p / "slides.html").is_file()):
            page.goto((peca / "slides.html").resolve().as_uri())
            page.wait_for_load_state("load")
            for i in range(page.locator(".slide").count()):
                page.evaluate(PREPARAR, i)
                page.wait_for_timeout(150)
                p = page.evaluate(CONTAR, [i, rotulo, sem_fonte])
                if p is not None:
                    telas.append({"peca": peca.name, "tela": i + 1, "papeis": p})
        br.close()
    return telas


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("serie", nargs="?", default=str(SERIE))
    ap.add_argument("--rotulo", action="store_true", help="conta o rótulo (.rot, .leg) como papel")
    ap.add_argument("--sem-fonte", action="store_true", help="tira a .fonte (metadado no design system)")
    ap.add_argument("--teto", type=int, default=3)
    ap.add_argument("--json")
    a = ap.parse_args()
    telas = contar(Path(a.serie), a.rotulo, a.sem_fonte)
    dist = Counter(len(t["papeis"]) for t in telas)
    acima = [t for t in telas if len(t["papeis"]) > a.teto]
    print(f"{len(telas)} telas; rótulo {'contado' if a.rotulo else 'fora'}; fonte {'fora' if a.sem_fonte else 'contada'}")
    print("distribuição: " + ", ".join(f"{k} papéis: {dist[k]}" for k in sorted(dist)))
    print(f"acima de {a.teto}: {len(acima)}")
    for t in acima:
        print(f"  {t['peca']} tela {t['tela']}: {', '.join(t['papeis'])}")
    if a.json:
        Path(a.json).write_text(json.dumps({"telas": telas, "distribuicao": dict(sorted(dist.items()))}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
