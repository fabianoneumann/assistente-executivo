"""Folha de contato: uma linha por peca, telas em miniatura. Uso: python folha_de_contato.py <saida.jpg> <rotulo>=<dir> ..."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
W, H, G, L = 240, 300, 12, 40
linhas = [a.split("=", 1) for a in sys.argv[2:]]
n = max(len(list(Path(d).glob("slide-*.jpg"))) for _, d in linhas)
img = Image.new("RGB", (G + n * (W + G), len(linhas) * (H + L + G) + G), "white")
dr = ImageDraw.Draw(img)
try:
    f = ImageFont.truetype("arial.ttf", 24)
except OSError:
    f = ImageFont.load_default()
y = G
for rot, d in linhas:
    dr.text((G, y), rot, fill="black", font=f)
    for i, p in enumerate(sorted(Path(d).glob("slide-*.jpg"))):
        t = Image.open(p).convert("RGB").resize((W, H), Image.LANCZOS)
        x = G + i * (W + G)
        img.paste(t, (x, y + L))
        dr.text((x + 4, y + L + 4), str(i + 1), fill="black", font=f)
    y += H + L + G
img.save(sys.argv[1], quality=90)
print("ok", sys.argv[1], img.size)
