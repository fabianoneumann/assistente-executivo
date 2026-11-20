"""Calibração do `parafrase.py`: o acordo do script com o veredito da revisão à mão, numa grade de limiar e K.

    python -X utf8 .claude/skills/research/scripts/calibra_parafrase.py --gabarito <gabarito.jsonl> [--saida <resultado.json>]

O gabarito tem uma linha JSON por ficha: {"id", "ficha", "fontes": [caminhos], "veredito": "ok" | "perto" | "colada",
"grupo"}. A ficha pode ser um caminho ou "git:<revisão>:<caminho no vault>", para medir a versão de antes de uma
reescrita. Positiva é a ficha "perto" ou "colada"; a ficha marca o trecho quando, contra pelo menos uma das fontes,
o script acha um trecho naquela célula da grade. O alinhamento é o mesmo do `parafrase.py` (as funções dele,
importadas), feito uma vez por par (ficha, fonte); a grade só reaplica o corte de trechos. A saída é a tabela por
grupo (VP, FN, FP, VN e o acerto, com os ids que erraram) e, com `--saida`, o resultado completo em JSON.

A primeira medida, de 2026-11-20, e o gabarito dela estão em
`knowledge/analysis/2026-11-20-calibracao-do-parafrase/`. Rodar de novo quando o gabarito crescer (cada ficha que
a conferência lado a lado julgar à mão, na mesma língua da fonte), e antes de mudar os padrões do `parafrase.py`.
A ficha em outra língua que a da fonte pode entrar num grupo à parte, para medir o que o script não vê.
"""
import argparse
import importlib.util
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
VAULT = AQUI.parents[2]
spec = importlib.util.spec_from_file_location("parafrase", AQUI / "parafrase.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

LIMIARES = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]
KS = [2, 3, 4]
POSITIVOS = {"perto", "colada"}

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass


def le_ficha(ref):
    if ref.startswith("git:"):
        _, rev, cam = ref.split(":", 2)
        r = subprocess.run(["git", "show", f"{rev}:{cam}"], cwd=VAULT, capture_output=True)
        if r.returncode:
            raise RuntimeError(r.stderr.decode("utf-8", "replace").strip())
        return r.stdout.decode("utf-8")
    return Path(ref).read_bytes().decode("utf-8")


def grade_do_par(tf, fonte, janela=12, palavras_celula=8):
    tx = P.le_fonte(Path(fonte))
    fs = []
    for s in P.frases(tx):
        fs.extend(P.pedacos(s))
    ws = [set(P.palavras(s)) for s in fs]
    inv = defaultdict(set)
    for i, w in enumerate(ws):
        for x in w:
            inv[x].add(i)
    itens, _ = P.unidades(tf, palavras_celula)
    al, _ = P.alinha(itens, fs, ws, inv)
    grade = {}
    for lim in LIMIARES:
        for k in KS:
            tr, col = P.trechos([dict(x) for x in al], lim, k, janela, fs)
            grade[f"{lim}/{k}"] = {"trechos": len(tr), "coladas": sum(col)}
    return grade


def mede(gabarito):
    out = []
    for g in gabarito:
        reg = dict(g)
        try:
            tf = le_ficha(g["ficha"])
        except Exception as e:
            reg["erro"] = f"ficha: {e}"
            out.append(reg)
            continue
        reg["resultados"] = []
        for fonte in g["fontes"]:
            try:
                reg["resultados"].append({"fonte": fonte, "grade": grade_do_par(tf, fonte)})
            except Exception as e:
                reg["resultados"].append({"fonte": fonte, "erro": str(e)})
        out.append(reg)
    return out


def marca(reg, celula):
    return any(r.get("grade", {}).get(celula, {}).get("trechos", 0) > 0 for r in reg.get("resultados", []))


def tabela(medidos):
    linhas, resumo = [], {}
    # a ficha só conta com todas as fontes medidas: a fonte que falhou podia ter o trecho, e a ficha viraria negativa
    validos = [x for x in medidos if "erro" not in x and x.get("resultados")
               and all("grade" in r for r in x["resultados"])]
    falhos = [x["id"] for x in medidos if x not in validos]
    if falhos:
        linhas.append(f"sem medida (erro de entrada na ficha ou em alguma fonte): {', '.join(falhos)}")
    for grupo in sorted({x.get("grupo", "") for x in validos}):
        xs = [x for x in validos if x.get("grupo", "") == grupo]
        pos = [x for x in xs if x["veredito"] in POSITIVOS]
        neg = [x for x in xs if x["veredito"] not in POSITIVOS]
        linhas.append(f"\n== {grupo or '(sem grupo)'}: {len(pos)} positivas, {len(neg)} negativas")
        linhas.append("limiar/K  VP FN FP  VN  acerto")
        for lim in LIMIARES:
            for k in KS:
                c = f"{lim}/{k}"
                vp = [x["id"] for x in pos if marca(x, c)]
                fn = [x["id"] for x in pos if not marca(x, c)]
                fp = [x["id"] for x in neg if marca(x, c)]
                ac = (len(vp) + len(neg) - len(fp)) / max(1, len(xs))
                resumo[(grupo, c)] = {"vp": len(vp), "fn": len(fn), "fp": len(fp), "vn": len(neg) - len(fp), "acerto": ac}
                linhas.append(f"{c:8s}  {len(vp):2d} {len(fn):2d} {len(fp):2d} {len(neg) - len(fp):3d}  {ac:.2f}"
                              + (f"  FN: {', '.join(fn)}" if fn else "") + (f"  FP: {', '.join(fp)}" if fp else ""))
    return "\n".join(linhas), resumo


def principal():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--gabarito", required=True)
    ap.add_argument("--saida")
    a = ap.parse_args()
    try:
        gab = [json.loads(l) for l in Path(a.gabarito).read_text(encoding="utf-8").splitlines() if l.strip()]
    except (OSError, ValueError) as e:
        print(f"erro de entrada: {e}", file=sys.stderr)
        return 2
    for n, g in enumerate(gab, 1):
        if not (isinstance(g, dict) and {"id", "ficha", "fontes", "veredito"} <= g.keys()
                and isinstance(g["fontes"], list)):
            print(f"erro de entrada: a linha {n} do gabarito não tem id, ficha, fontes (lista) e veredito", file=sys.stderr)
            return 2
    medidos = mede(gab)
    txt, _ = tabela(medidos)
    print(txt)
    if a.saida:
        Path(a.saida).write_text(json.dumps(medidos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
