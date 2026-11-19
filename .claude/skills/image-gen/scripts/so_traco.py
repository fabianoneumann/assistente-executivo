"""Desenho a lápis gerado (grafite sobre papel branco) -> só o traço, em PNG transparente, para assentar no papel de uma peça.

Uso: python so_traco.py <entrada.png> <saida.png> [--lado 880] [--sem-recorte]

Só quando a imagem vai para cima de outro fundo (o papel da série, por exemplo); imagem usada inteira não passa por aqui.
1. Tira o papel: o traço é o quanto cada pixel é mais escuro que o papel em volta (o tom do papel varia na folha).
2. Recorta pelo traço firme, não por qualquer pixel: as linhas de construção claras vão longe para um lado e, no
   recorte pela caixa inteira, deixam o desenho deslocado na peça. --sem-recorte mantém o quadro.
3. Mede o centro visual (a média ponderada do traço) e avisa quando ele foge mais de 5% do centro da imagem:
   aí, centralizar pelo centro visual ou recortar de novo, em vez de confiar no meio da caixa.
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter, ImageOps

FIRME = 110  # alfa a partir do qual o traço decide o recorte
FOLGA = 12   # px em volta do traço firme

ap = argparse.ArgumentParser(description="Só o traço de um desenho a lápis, em PNG transparente")
ap.add_argument("entrada")
ap.add_argument("saida")
ap.add_argument("--lado", type=int, default=880, help="lado maior da saída, em px")
ap.add_argument("--sem-recorte", action="store_true", help="mantém o quadro inteiro")
a = ap.parse_args()

g = ImageOps.grayscale(Image.open(a.entrada))
fundo = g.filter(ImageFilter.GaussianBlur(60))
traco = np.clip((np.asarray(fundo, float) - np.asarray(g, float)) * 3.2, 0, 255)
traco[traco < 28] = 0  # o que sobra do papel some
out = Image.new("RGBA", g.size, (44, 48, 56, 0))
out.putalpha(Image.fromarray(traco.astype("uint8")))
if not a.sem_recorte:
    ys, xs = np.where(traco > FIRME)
    out = out.crop((max(xs.min() - FOLGA, 0), max(ys.min() - FOLGA, 0),
                    min(xs.max() + FOLGA + 1, out.width), min(ys.max() + FOLGA + 1, out.height)))
out.thumbnail((a.lado, a.lado))
out.save(a.saida, optimize=True)

alfa = np.asarray(out.split()[3], float)
yy, xx = np.indices(alfa.shape)
cx, cy = (alfa * xx).sum() / alfa.sum(), (alfa * yy).sum() / alfa.sum()
dx, dy = cx / out.width - 0.5, cy / out.height - 0.5
aviso = "  [AVISO] centro visual fora do meio: centralizar por ele" if max(abs(dx), abs(dy)) > 0.05 else ""
print(f"{a.saida} {out.size}; centro visual a {dx:+.1%} na largura e {dy:+.1%} na altura{aviso}")
