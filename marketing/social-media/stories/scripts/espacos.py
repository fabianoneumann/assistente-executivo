"""Põe os desenhos de enfeite de cada Story nos maiores vazios da própria tela, do maior para o menor.

Cada tela tem a sua dispersão: nada de repetir a mesma posição entre os Stories. O primeiro desenho da lista de cada
tela é o dominante e encolhe até caber no maior vazio, sem descer de 180 px; os outros encolhem até 30% para caber.
Folga de 24 px em volta de texto, adesivo e outro desenho.

Uso (da raiz do projeto):
  python -X utf8 marketing/social-media/stories/scripts/espacos.py <pasta da peça> [--html stories.html] [--manter]
      [--ignorar-faixa X0:X1 ...]
  --manter: as posições ficam e só as larguras dos pequenos mudam, com o menor deslize que evite esbarrar.
  --ignorar-faixa: uma faixa vertical do papel que conta como papel e não como ocupada (a margem desenhada de um papel
  pautado, por exemplo 90:112); pode repetir.

A pasta precisa de `desenhos.json`: {"desenhos": {"<tela>": [{"src", "largura", "giro", "vira"?}, ...]}, "alt": {"<src>":
"<o que o desenho mostra>"}}, com os PNG em assets/<src>.png. O script exporta a prévia sem desenhos (a slides-export, com
--previa, que desenha os adesivos simulados), mede os vazios, reescreve os <img class="desenho"> de cada <section> do
HTML e imprime as posições. A cor do papel se acha na própria prévia (a cor mais comum da tela), então serve a qualquer
série. Pede numpy, Pillow e scipy.
"""
import argparse, json, pathlib, re, subprocess, sys, tempfile
import numpy as np
from PIL import Image
from scipy import ndimage

K = 4                                   # a medida roda em 1/4 da tela
FOLGA, TOPO, BASE = 24, 150, 1790       # acima de 150 fica o cabeçalho do app; abaixo de 1790, a barra de mensagem
RAIZ = pathlib.Path(__file__).resolve().parents[4]
EXPORT = RAIZ / ".claude" / "skills" / "slides-export" / "scripts" / "export_slides.py"


def cor_do_papel(im):
    """A cor mais comum da tela, quantizada em passos de 8: o papel, que ocupa a maior parte de um Story."""
    q = (im // 8).astype(np.int32)
    chave = q[..., 0] * 1024 + q[..., 1] * 32 + q[..., 2]
    moda = np.bincount(chave.ravel()).argmax()
    return np.array([(moda // 1024) * 8 + 4, ((moda // 32) % 32) * 8 + 4, (moda % 32) * 8 + 4], dtype=float)


def ocupado(jpg, faixas=()):
    im = np.asarray(Image.open(jpg).convert("RGB"), dtype=float)
    m = np.linalg.norm(im - cor_do_papel(im), axis=2) > 20   # 20: o cinza claro do adesivo simulado sobre papel branco conta
    for x0, x1 in faixas:
        m[:, x0:x1] = False                                     # a faixa declarada é papel
    m = ndimage.binary_opening(m, structure=np.ones((5, 1)))    # tira as linhas finas do papel (1 a 2 px de altura)
    o = m.reshape(1920 // K, K, 1080 // K, K).any(axis=(1, 3))
    o[:TOPO // K, :] = True; o[BASE // K:, :] = True; o[:, :2] = True; o[:, -2:] = True
    return ndimage.binary_dilation(o, iterations=FOLGA // K)


def posicionar(occ, itens, assets):
    res = []
    for i, it in enumerate(itens):
        w = it["largura"]; a = Image.open(assets / f"{it['src']}.png")
        minimo = 180 if i == 0 else int(w * 0.7)
        ii = np.pad(occ.astype(int), ((1, 0), (1, 0))).cumsum(0).cumsum(1)
        while True:
            h = w * a.size[1] / a.size[0]
            bw, bh = int(np.ceil(w * 1.08 / K)), int(np.ceil(h * 1.08 / K))   # folga para o giro
            soma = ii[bh:, bw:] - ii[:-bh, bw:] - ii[bh:, :-bw] + ii[:-bh, :-bw]
            livre = soma == 0
            if livre.any() or w <= minimo:
                break
            w = int(w * 0.92)
        if not livre.any():
            print(f"  sem lugar: {it['src']}", file=sys.stderr); continue
        dist = ndimage.distance_transform_edt(~occ)
        ys, xs = np.nonzero(livre)
        j = int(np.argmax(dist[ys + bh // 2, xs + bw // 2]))   # o centro mais longe de tudo: o maior vazio
        y0, x0 = ys[j], xs[j]
        f = FOLGA // K
        occ[max(0, y0 - f):y0 + bh + f, max(0, x0 - f):x0 + bw + f] = True
        res.append({**it, "largura": w, "left": int((x0 + bw / 2) * K), "top": int(y0 * K + (bh * K - h) / 2)})
    return res


def manter(occ, itens, atuais, assets):
    """Troca só as larguras dos pequenos, com o centro de cada desenho onde está; se o tamanho novo esbarra em
    texto, adesivo ou outro desenho, desliza o mínimo (até 64 px) para o lugar livre mais perto."""
    res = []
    ordem = sorted(range(len(itens)), key=lambda i: -atuais[itens[i]["src"]]["largura"])
    for i in ordem:
        it = itens[i]; at = atuais[it["src"]]; a = Image.open(assets / f"{it['src']}.png")
        w = at["largura"] if i == 0 else it["largura"]          # o dominante fica como está
        h0 = at["largura"] * a.size[1] / a.size[0]; h = w * a.size[1] / a.size[0]
        cx, cy = at["left"] / K, (at["top"] + h0 / 2) / K
        bw, bh = int(np.ceil(w * 1.08 / K)), int(np.ceil(h * 1.08 / K))
        ii = np.pad(occ.astype(int), ((1, 0), (1, 0))).cumsum(0).cumsum(1)
        H, W = occ.shape; achou = None
        for r in range(0, 17):
            cand = [(dy, dx) for dy in range(-r, r + 1) for dx in range(-r, r + 1) if max(abs(dy), abs(dx)) == r]
            for dy, dx in sorted(cand, key=lambda t: t[0] ** 2 + t[1] ** 2):
                y0, x0 = int(round(cy - bh / 2)) + dy, int(round(cx - bw / 2)) + dx
                if y0 < 0 or x0 < 0 or y0 + bh > H or x0 + bw > W:
                    continue
                if ii[y0 + bh, x0 + bw] - ii[y0, x0 + bw] - ii[y0 + bh, x0] + ii[y0, x0] == 0:
                    achou = (y0, x0); break
            if achou:
                break
        if not achou:                       # não coube sem esbarrar: fica como estava
            print(f"  mantido: {it['src']}", file=sys.stderr); w, h = at["largura"], h0
            bw, bh = int(np.ceil(w * 1.08 / K)), int(np.ceil(h * 1.08 / K))
            y0, x0 = int(round(cy - bh / 2)), int(round(cx - bw / 2))
        else:
            y0, x0 = achou
        f = FOLGA // K
        occ[max(0, y0 - f):y0 + bh + f, max(0, x0 - f):x0 + bw + f] = True
        res.append({**it, "largura": w, "left": int((x0 + bw / 2) * K), "top": int(y0 * K + (bh * K - h) / 2)})
    return [r for _, r in sorted(zip(ordem, res))]


def faixa(s):
    try:
        a, b = (int(x) for x in s.split(":"))
    except ValueError:
        raise argparse.ArgumentTypeError(f"{s!r}: a faixa é X0:X1, em px da tela de 1080")
    return a, b


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("peca"); ap.add_argument("--html", default="stories.html")
    ap.add_argument("--manter", action="store_true", help="mantém as posições e troca só as larguras dos pequenos")
    ap.add_argument("--ignorar-faixa", type=faixa, action="append", default=[], metavar="X0:X1",
                    help="faixa vertical do papel que conta como papel (a margem desenhada, por exemplo)")
    a = ap.parse_args(); peca = pathlib.Path(a.peca); html = peca / a.html
    if not (peca / "desenhos.json").is_file() or not html.is_file():
        sys.exit(f"faltam {peca / 'desenhos.json'} ou {html}")
    if not EXPORT.is_file():
        sys.exit(f"a exportação não está em {EXPORT}: este script usa a skill slides-export para a prévia")
    cfg = json.loads((peca / "desenhos.json").read_text(encoding="utf-8"))
    s = html.read_text(encoding="utf-8")
    atuais = {}
    for n, sec in enumerate(re.findall(r"<section\b.*?</section>", s, re.S), 1):
        atuais[n] = {m[0]: {"left": int(m[1]), "top": int(m[2]), "largura": int(m[3])} for m in re.findall(
            r'<img class="desenho" src="assets/([^.]+)\.png"[^>]*left:(\d+)px;top:(\d+)px;width:(\d+)px', sec)}
    limpo = re.sub(r'\n  <img class="desenho"[^>]*>', "", s)
    tmp = peca / "_sem-desenhos.html"; tmp.write_text(limpo, encoding="utf-8", newline="\n")
    with tempfile.TemporaryDirectory() as d:
        try:
            subprocess.run([sys.executable, str(EXPORT), str(peca), "--html", tmp.name, "--height", "1920", "--previa",
                            "--out-dir", d], check=True, capture_output=True)
        finally:
            tmp.unlink()
        secs = list(re.finditer(r"<section\b.*?</section>", limpo, re.S))
        for n in range(len(secs), 0, -1):
            itens = cfg["desenhos"].get(str(n))
            if not itens:
                continue
            occ = ocupado(pathlib.Path(d) / f"slide-{n:02d}.jpg", a.ignorar_faixa)
            pos = (manter(occ, itens, atuais[n], peca / "assets") if a.manter
                   else posicionar(occ, itens, peca / "assets"))
            print(n, [(p["src"], p["left"], p["top"], p["largura"]) for p in pos])
            imgs = "".join(
                f'  <img class="desenho" src="assets/{p["src"]}.png" alt="desenho: {cfg["alt"][p["src"]]}" '
                f'style="left:{p["left"]}px;top:{p["top"]}px;width:{p["largura"]}px;--giro:{p["giro"]}deg'
                + (f';--vira:{p["vira"]}' if "vira" in p else "") + '">\n' for p in pos)
            m = secs[n - 1]
            limpo = limpo[:m.start()] + m.group(0).replace("</section>", imgs + "</section>") + limpo[m.end():]
    html.write_text(limpo, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
