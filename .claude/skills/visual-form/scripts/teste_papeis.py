"""O design/papeis.json de cada série diz o mesmo que a tabela "Letra" do design-system.md dela.

    python -X utf8 .claude/skills/visual-form/scripts/teste_papeis.py

A tabela escrita é a regra; o JSON é ela em dados, para as conferências da forma (medidas_forma.carregar_serie). Quem
muda uma muda a outra, e este teste falha se elas divergirem: o corpo e a entrelinha no papel A e no B, e o peso quando a
tabela o diz. Confere toda série de marketing/social-media/carousels/series/ que tem design/papeis.json.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SERIES = ROOT / "marketing/social-media/carousels/series"
NOMES = {"Título": "titulo", "Destaque": "destaque", "Corpo": "corpo", "Apoio": "apoio", "Citação": "citacao",
         "Nota": "nota", "Chamada": "chamada", "Fila": "fila", "Endereço": "link", "Moldura e fonte": "fonte"}


def tabela_do_design_system(serie):
    texto = (serie / "design-system.md").read_text(encoding="utf-8")
    secao = re.search(r"^## Letra\s*$(.*?)(?=^## |\Z)", texto, re.M | re.S).group(1)
    linhas = {}
    for l in secao.splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) < 4 or c[0] not in NOMES:
            continue
        a = [int(x) for x in re.findall(r"\d+", c[2])[:2]]
        b = a if c[3].startswith("igual") else [int(x) for x in re.findall(r"\d+", c[3])[:2]]
        peso = re.search(r"\b(\d{3})\b", c[1])
        linhas[NOMES[c[0]]] = (a, b, int(peso.group(1)) if peso else None)
    return linhas


def conferir(serie):
    js = json.loads((serie / "design/papeis.json").read_text(encoding="utf-8"))["papeis"]
    ds = tabela_do_design_system(serie)
    falhas = []
    if set(ds) != set(js):
        falhas.append(f"papéis diferentes: só no design system {sorted(set(ds) - set(js))}, só no JSON {sorted(set(js) - set(ds))}")
    for papel in sorted(set(ds) & set(js)):
        a, b, peso = ds[papel]
        v = js[papel]
        if v[0:2] != a or v[2:4] != b:
            falhas.append(f"{papel}: o JSON diz {v[0:4]}, o design system diz A {a} e B {b}")
        if peso is not None and v[4] != peso:
            falhas.append(f"{papel}: peso {v[4]} no JSON, {peso} no design system")
    return falhas


def main():
    series = sorted(p.parents[1] for p in SERIES.glob("*/design/papeis.json"))
    if not series:
        print(f"FALHOU nenhuma série com design/papeis.json em {SERIES}")
        return 1
    total = 0
    for serie in series:
        falhas = conferir(serie)
        total += len(falhas)
        for f in falhas:
            print(f"FALHOU {serie.name}: {f}")
        if not falhas:
            print(f"ok    {serie.name}: o papeis.json e a tabela Letra dizem o mesmo")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
