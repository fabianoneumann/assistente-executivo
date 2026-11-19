"""Prepara o material do teste I2 com o pacote: HTML sem texto (color: transparent) e recortes ampliados.

Uso:
  python prepara_i2.py semtexto <html_origem> <dir_saida> <nome>   -> <dir_saida>/<nome>.html com <base> e o texto apagado
  python prepara_i2.py zoom <dir_jpegs> <dir_saida>                 -> quatro quadrantes por tela, ampliados 2x

O `semtexto` apaga também o texto gerado pelo CSS (`::before`, `::after`, `::marker`: a numeração dos `.passos`, por
exemplo), e para com erro se a página não tem `<head ...>` e `</head>`. O teste está em `teste_ferramentas_i2.py`, ao lado.
"""
import re
import sys
from pathlib import Path

ESTILO = """<style id="teste-sem-texto">
*, *::before, *::after, *::marker{color:transparent !important;text-shadow:none !important;-webkit-text-stroke:0 !important;caret-color:transparent !important}
svg text, svg tspan, svg textPath{fill:transparent !important;stroke:transparent !important}
</style>"""


def semtexto(origem: str, saida: str, nome: str) -> None:
    src = Path(origem).resolve()
    out = Path(saida)
    txt = src.read_text(encoding="utf-8")
    abre = re.search(r"<head(\s[^>]*)?>", txt, re.I)
    fecha = list(re.finditer(r"</head\s*>", txt, re.I))
    if not abre or not fecha or fecha[-1].start() < abre.end():
        sys.exit("sem <head> e </head>: o estilo e o <base> não têm onde entrar")
    base = f'<base href="{src.parent.as_uri()}/">'
    j = fecha[-1].start()
    txt = txt[:abre.end()] + "\n" + base + "\n" + txt[abre.end():j] + ESTILO + "\n" + txt[j:]
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{nome}.html").write_text(txt, encoding="utf-8")
    print("ok", out / f"{nome}.html")


def zoom(dir_jpegs: str, saida: str) -> None:
    from PIL import Image
    out = Path(saida)
    out.mkdir(parents=True, exist_ok=True)
    for f in sorted(Path(dir_jpegs).glob("slide-*.jpg")):
        im = Image.open(f).convert("RGB")
        w, h = im.size
        nomes = {"a-sup-esq": (0, 0), "b-sup-dir": (1, 0), "c-inf-esq": (0, 1), "d-inf-dir": (1, 1)}
        for nome, (cx, cy) in nomes.items():
            box = (cx * w // 2, cy * h // 2, (cx + 1) * w // 2, (cy + 1) * h // 2)
            q = im.crop(box).resize((w, h), Image.LANCZOS)
            q.save(out / f"{f.stem}-{nome}.jpg", quality=90)
        print("ok", f.name)


if __name__ == "__main__":
    if len(sys.argv) == 5 and sys.argv[1] == "semtexto":
        semtexto(*sys.argv[2:5])
    elif len(sys.argv) == 4 and sys.argv[1] == "zoom":
        zoom(*sys.argv[2:4])
    else:
        sys.exit(__doc__)
