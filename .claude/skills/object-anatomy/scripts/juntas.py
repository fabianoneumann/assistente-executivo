"""Zoom de 4× nas juntas e nas pontas do desenho de cada tela (R18 do método do Anatomy): "the owner finds faults by
zooming in, so you zoom in first. Read every PNG you make" (o Anatomy, de onde veio o método; `references/metodo.md`).
Fotografa cada tela a 4× (o mesmo Chromium, a mesma janela e a mesma preparação das conferências, com as fontes
conferidas) e recorta em volta de cada ponto que pede o olho: a ponta e a saída de cada seta livre (path.seta-livre,
lida antes de o caderno.js trocá-la pelo traço de pena e posta na tela depois do prepararSlide) e as duas pontas de cada traço aberto do desenho (path, line e
polyline sem Z, fora as marcas do caderno.js e o traço de pena). Grava os recortes e um juntas.md com a lista, na ordem
de leitura; quem lê é quem faz a peça (ou o agente da forma), recorte por recorte. Não julga nada: é o olho a 4×, no
lugar da imagem inteira, onde a ponta solta e a peça afundada não aparecem.

  python -X utf8 juntas.py <pasta-da-peca> [arquivo.html] --saida <pasta> [--telas 3,5] [--raio 60]

A saída vai para fora do projeto (uma pasta temporária), ou para a pasta medida/ da peça quando o recorte vira registro. Até
40 recortes por tela; pontos a menos de meio raio um do outro saem num recorte só. Os pontos além de 40 ficam de fora,
e o juntas.md diz quantos, por tela (para rodar de novo com --raio maior, ou ler a tela inteira a 4×).
"""
import argparse
import io
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "visual-form", "scripts"))   # conferir_telas.py, da visual-form
import conferir_telas as ct  # noqa: E402  o PREPARAR (fontes e setas) e a mesma janela

ESCALA = 4
MAX_POR_TELA = 40

PONTAS = r"""(idx) => {
  const sl = document.querySelectorAll('.slide')[idx], o = sl.getBoundingClientRect(), out = [];
  for (const f of sl.querySelectorAll('svg path, svg line, svg polyline')) {
    if (f.closest('svg.marcas') || /\btinta-[cl]\b/.test(f.getAttribute('class') || '')) continue;
    if (f.tagName === 'path' && /z\s*$/i.test(f.getAttribute('d') || '')) continue;   // fechado: não tem ponta
    const L = f.getTotalLength ? f.getTotalLength() : 0, m = f.getScreenCTM(); if (!L || !m) continue;
    const em = q => [m.a * q.x + m.c * q.y + m.e - o.left, m.b * q.x + m.d * q.y + m.f - o.top];
    const cls = (f.getAttribute('class') || f.tagName).trim();
    out.push({p: em(f.getPointAtLength(0)), o: 'início de ' + cls}, {p: em(f.getPointAtLength(L)), o: 'fim de ' + cls});
  }
  return out;
}"""


def pontos_da_tela(setas, pontas, raio):
    """Os pontos a recortar, na ordem: as setas (ponta e saída), depois as pontas dos traços; os vizinhos se juntam.
    Devolve (pontos, cortados): cortados é quantos pontos novos passaram de MAX_POR_TELA e ficaram sem recorte."""
    cand = [(s["ponta"], "ponta da seta") for s in setas] + [(s["inicio"], "saída da seta") for s in setas]
    cand += [(tuple(q["p"]), q["o"]) for q in pontas]
    out, cortados = [], 0
    for p, o in cand:
        perto = next((x for x in out if abs(x[0][0] - p[0]) < raio / 2 and abs(x[0][1] - p[1]) < raio / 2), None)
        if perto:
            if o not in perto[1]:
                perto[1].append(o)
        elif len(out) < MAX_POR_TELA:
            out.append((p, [o]))
        else:
            cortados += 1
    return out, cortados


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pasta")
    ap.add_argument("html", nargs="?")
    ap.add_argument("--saida", required=True)
    ap.add_argument("--telas")
    ap.add_argument("--raio", type=int, default=60, help="meio lado do recorte, em px da tela (padrão 60: 480 px a 4×)")
    a = ap.parse_args(argv)
    from playwright.sync_api import sync_playwright
    from PIL import Image
    pasta = Path(a.pasta).resolve()
    html = a.html or ("slides.html" if (pasta / "slides.html").is_file() else "stories.html")
    saida = Path(a.saida).resolve()
    saida.mkdir(parents=True, exist_ok=True)
    linhas = [f"# Juntas a {ESCALA}× de {pasta.name}/{html}", "",
              "Cada recorte é lido na ordem: a ponta que para no ar, o cruzamento na ordem errada, a peça afundada ou "
              "solta, a ponta pousada no contorno de outra linha (R18 e R19 do método do Anatomy).", ""]
    feitos = 0
    with sync_playwright() as pw:
        br = pw.chromium.launch(args=["--disable-lcd-text"])
        page = br.new_page(viewport={"width": 1280, "height": 1560}, device_scale_factor=ESCALA)
        page.goto((pasta / html).resolve().as_uri())
        page.wait_for_load_state("load")
        total = page.locator(".slide").count()
        try:
            quais = sorted({int(x) for x in a.telas.split(",")}) if a.telas else range(1, total + 1)
        except ValueError:
            quais = None
        if quais is None or any(not 1 <= n <= total for n in quais):
            br.close()
            ap.error(f"--telas {a.telas}: as telas vão de 1 a {total}, separadas por vírgula")
        for n in quais:
            prep = page.evaluate(ct.PREPARAR, n - 1) or {}
            page.wait_for_timeout(300)
            if prep.get("faltam"):
                linhas.append(f"- Tela {n}: fonte que não carregou ({', '.join(f['familia'] for f in prep['faltam'])}); "
                              "os recortes sairiam na fonte de reserva")
            pts, cortados = pontos_da_tela(prep.get("setas", []), page.evaluate(PONTAS, n - 1), a.raio)
            if cortados:
                linhas.append(f"- Tela {n}: {cortados} ponto(s) além dos {MAX_POR_TELA} recortes ficaram de fora "
                              "(rodar com --raio maior, ou ler a tela inteira a 4×)")
            if not pts:
                continue
            img = Image.open(io.BytesIO(page.locator(".slide").nth(n - 1).screenshot(animations="disabled"))).convert("RGB")
            for k, (p, o) in enumerate(pts, 1):
                x0, y0 = max(0, (p[0] - a.raio) * ESCALA), max(0, (p[1] - a.raio) * ESCALA)
                x1, y1 = min(img.width, (p[0] + a.raio) * ESCALA), min(img.height, (p[1] + a.raio) * ESCALA)
                if x1 <= x0 or y1 <= y0:
                    continue
                nome = f"tela-{n:02d}-{k:02d}.png"
                img.crop((round(x0), round(y0), round(x1), round(y1))).save(saida / nome)
                linhas.append(f"- `{nome}`: tela {n}, x {round(p[0])}, y {round(p[1])}: {', '.join(o)}")
                feitos += 1
        br.close()
    (saida / "juntas.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"{feitos} recorte(s) a {ESCALA}× em {saida} (lista em juntas.md)")
    return feitos


if __name__ == "__main__":
    main()
