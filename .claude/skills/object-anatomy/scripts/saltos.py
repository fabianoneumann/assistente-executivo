"""Câmera lenta por medida (R21 do método do Anatomy): decodifica o MP4 inteiro e mede a diferença média entre
quadros seguidos. Um salto (troca súbita) aparece como um pico isolado; o fim parado tem que dar ~0 (só ruído do H.264).
É a medida da folha de quadros do vídeo do objeto em movimento (o `conferencias.md`, seção 4).

  python -X utf8 saltos.py <arquivo.mp4> [...]

Pede o ffmpeg e o ffprobe no PATH. O quadro-chave do H.264 (o GOP; na tela em vídeo, um por segundo) mexe uns pixels
mesmo sem movimento: o quadro dele e o seguinte não contam no "fim parado", e o pico que cai nele se marca à parte.
Leitura, sem nível: quem decide se o salto é defeito é quem olha o vídeo.
"""
import subprocess
import sys

import numpy as np


def _probe(mp4: str):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate",
                        "-of", "csv=p=0", mp4], capture_output=True, text=True, check=True)
    w, h, fr = r.stdout.strip().split(",")[:3]
    num, _, den = fr.partition("/")
    return int(w), int(h), round(float(num) / float(den or 1))


def quadros(mp4: str, w: int, h: int):
    p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", mp4, "-f", "rawvideo", "-pix_fmt", "gray", "-"], stdout=subprocess.PIPE)
    while True:
        b = p.stdout.read(w * h)
        if len(b) < w * h:
            break
        yield np.frombuffer(b, np.uint8).astype(np.int16)
    p.wait()


def medir(mp4: str) -> dict:
    """{quadros, fps, mediana, maximo, quadro_max, picos, picos_chave, parado_quadros, parado_s, chave}: picos são os
    quadros (a partir de 1) com um salto isolado fora do quadro-chave; picos_chave, os que caem no quadro-chave."""
    w, h, fps = _probe(mp4)
    ant, d = None, []
    for q in quadros(mp4, w, h):
        if ant is not None:
            d.append(float(np.abs(q - ant).mean()))
        ant = q
    d = np.array(d)
    if not len(d):
        return {"quadros": 1 if ant is not None else 0, "fps": fps, "picos": [], "picos_chave": [], "parado_quadros": 0}
    med = float(np.median(d[d > 0.02])) if (d > 0.02).any() else 0.0
    chave_q = lambda i: (i + 1) % fps in (0, 1)   # d[i] compara o quadro i+1 com o i+2 (a partir de 1)
    todos = [(i + 1, round(float(v), 3)) for i, v in enumerate(d) if v > max(0.15, 4 * med) and (i == 0 or v > 2.5 * d[i - 1])]
    picos = [p for p in todos if not chave_q(p[0] - 1)]
    mexe = [i for i, v in enumerate(d) if v > 0.01 and not chave_q(i)]
    parado = len(d) - 1 - (mexe[-1] if mexe else -1)
    return {"quadros": len(d) + 1, "fps": fps, "mediana": round(med, 3), "maximo": round(float(d.max()), 3),
            "quadro_max": int(d.argmax()) + 1, "picos": picos, "picos_chave": [p for p in todos if chave_q(p[0] - 1)],
            "parado_quadros": parado, "parado_s": round(parado / fps, 2),
            "chave": [round(float(d[i - 1]), 3) for i in range(fps, len(d) + 1, fps)]}


def main(args):
    for mp4 in args:
        r = medir(mp4)
        print(f"{mp4}: {r['quadros']} quadros a {r['fps']} qps; diferença média por quadro: mediana {r.get('mediana', 0):.3f}, "
              f"máx {r.get('maximo', 0):.3f} (quadro {r.get('quadro_max', '-')}); picos isolados: {r['picos'] or 'nenhum'}"
              f"{'; no quadro-chave: ' + str(r['picos_chave']) if r['picos_chave'] else ''}; quadros parados no fim: "
              f"{r['parado_quadros']} ({r.get('parado_s', 0):.2f} s); diferença nos quadros-chave: {r.get('chave', [])}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1:])
