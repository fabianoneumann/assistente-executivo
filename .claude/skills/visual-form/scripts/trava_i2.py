"""A trava da I2 por script: lê as medidas da forma e a lista da I2 e diz que telas voltam para ajuste, e por quê.

    python -X utf8 trava_i2.py <medidas.json> <i2-relatorio.md> [--falha-objetiva N:motivo ...] [--json saida.json]
    python -X utf8 trava_i2.py <medidas.json> <i2-relatorio.md> --reconferencia <volta.md> --anterior <trava.json> ...

A regra (`references/i2.md`, "A trava"):
- **a antiga** (a toda tela que perde, e não só à pior): a tela que perde nas duas ordens só volta se também falhar um item objetivo da lista ("não"
  em Hi, Ng, Ac, Nº, Tam, Est ou Dest), uma medida (destaque manuscrito zero, corpo sem negrito, texto a menos de 48 px
  da borda, ou a coluna que transborda) ou uma falha objetiva conferida à mão
  (`--falha-objetiva`, para o defeito que nenhum script mede, como o texto sob um elemento que o cobre);
- **a (b)**: volta também a tela que
  tem "não" no Dest da lista **e** zero destaque manuscrito na medida, mesmo sem perder na comparação.

O resto vai à leitura da pessoa como sinal, sem volta: a tela que perde sem falha objetiva, a medida que falha sem o
"não" no mesmo item, o Dest "parcial", e o Can (o traço do desenho no peso da letra), que é item de leitura. O Tam fica fora da
(b) até ter limite medido em todas as telas.

Entrada: as medidas do `mede_forma.py` (no navegador ou `--estatico`) e o relatório da I2 no formato do
`references/i2.md` (um bloco `### Tela N` por tela, com a linha `**Lista:**` com os oito itens e a linha
`**Perde: sim|não**`). **Na volta,** `--reconferencia` lê o relatório do agente que reconferiu só as telas que voltaram,
no mesmo formato, e `--anterior` o `trava.json` da rodada anterior: a reconferência tem de cobrir exatamente as telas
que voltaram; as telas dela trocam as do primeiro relatório; as medidas são as da versão nova; e a regra antiga só vale
nas telas reconferidas (nas outras, a comparação é da versão antiga, e a falha nova de medida vai como sinal).

Para com o motivo (código 2) a tela que falta, o item da lista ou o "Perde" ausente, a medida do destaque ausente
(não é zero), as telas que não batem, a falha objetiva de tela que não existe e a reconferência que não cobre as telas
que voltaram. Códigos: 0 nenhuma tela volta; 1 há tela que volta; 2 entrada que não basta. Com `--json`, grava o
resultado em UTF-8 com fim de linha LF. Só para o carrossel: nos Stories, a comparação (a IS4) é sinal, sem trava.
"""
import argparse
import json
import re
import sys
from pathlib import Path

STATUS = {"sim": "sim", "não": "não", "nao": "não", "parcial": "parcial", "n/a": "n/a"}
ITENS = ("Hi", "Ng", "Ac", "Nº", "Tam", "Can", "Est", "Dest")
OBJETIVOS = ("Hi", "Ng", "Ac", "Nº", "Tam", "Est", "Dest")
MARGEM_MIN = 48


class TravaErro(ValueError):
    """A entrada não basta para decidir: falta tela, item ou medida, ou as duas listas não batem."""


_TELA = re.compile(r"^#{2,3}\s+Tela\s+(\d+)\b", re.M)
_ITEM = re.compile(r"(?<![\wº°])(Hi|Ng|Ac|Nº|N°|Tam|Can|Est|Dest)\s*[:\-–]?\s*\**\s*((?i:sim|não|nao|parcial|n/a))"
                   r"(?![\w/])")
_PERDE = re.compile(r"\*\*Perde:\s*((?i:sim|não|nao))(?!\w)")


def ler_relatorio(caminho):
    """{tela: {"perde": "sim"|"não", "itens": {item: status}}}, ou TravaErro se o relatório não traz o que a trava lê."""
    texto = Path(caminho).read_text(encoding="utf-8")
    marcos = list(_TELA.finditer(texto))
    if not marcos:
        raise TravaErro(f"nenhum bloco '### Tela N' em {caminho}")
    lista = {}
    for k, m in enumerate(marcos):
        tela = int(m.group(1))
        bloco = texto[m.end():marcos[k + 1].start() if k + 1 < len(marcos) else len(texto)]
        bloco = re.split(r"^##\s", bloco, maxsplit=1, flags=re.M)[0]
        if tela in lista:
            raise TravaErro(f"a tela {tela} aparece duas vezes no relatório")
        lin = next((ln for ln in bloco.splitlines() if ln.lstrip().startswith("**Lista:**")), None)
        if lin is None:
            raise TravaErro(f"tela {tela}: sem a linha '**Lista:**'")
        itens = {}
        for nome, st in _ITEM.findall(lin):
            itens.setdefault("Nº" if nome == "N°" else nome, STATUS[st.lower()])
        faltam = [i for i in ITENS if i not in itens]
        if faltam:
            raise TravaErro(f"tela {tela}: a lista não traz {', '.join(faltam)} (no formato 'Tam não.')")
        p = _PERDE.search(bloco)
        if not p:
            raise TravaErro(f"tela {tela}: sem a linha '**Perde: sim|não**'")
        lista[tela] = {"perde": STATUS[p.group(1).lower()], "itens": itens}
    return lista


def falhas_de_medida(m):
    f = []
    if m.get("destaque_manuscrito") == 0:
        f.append("destaque manuscrito: nenhum além do título (medida)")
    if m.get("corpo") and m.get("negrito") == 0:
        f.append("negrito: nenhum no corpo (medida)")
    for lado in ("margem_esq_min", "margem_dir_min"):
        v = m.get(lado)
        if v is not None and v < MARGEM_MIN:
            f.append(f"{lado.replace('_min', '').replace('_', ' ')}: {v} px, abaixo de {MARGEM_MIN} (medida)")
    if m.get("transborda"):
        f.append("a coluna passa do pé (medida)")
    return f


def falham_destaque(medidas):
    return {m["tela"] for m in medidas if m.get("destaque_manuscrito") == 0}


def _confere(medidas, lista, falhas_objetivas, reconferidas):
    if not isinstance(medidas, list) or not medidas:
        raise TravaErro("as medidas não são uma lista de telas (o JSON do mede_forma.py)")
    if not all(isinstance(m, dict) and isinstance(m.get("tela"), int) for m in medidas):
        raise TravaErro("toda medida precisa ser um objeto com o número da tela em 'tela'")
    tm = [m["tela"] for m in medidas]
    if len(tm) != len(set(tm)):
        raise TravaErro("tela repetida nas medidas")
    if set(tm) != set(lista):
        raise TravaErro(f"as telas não batem: medidas {sorted(tm)}, lista da I2 {sorted(lista)}")
    for m in medidas:
        if m.get("destaque_manuscrito") is None:
            raise TravaErro(f"tela {m['tela']}: sem a medida do destaque manuscrito (ausente não é zero)")
    fora = sorted(set(falhas_objetivas) - set(tm))
    if fora:
        raise TravaErro(f"falha objetiva em tela que não existe: {fora}")
    if reconferidas is not None and not set(reconferidas) <= set(tm):
        raise TravaErro(f"reconferência de tela que não existe: {sorted(set(reconferidas) - set(tm))}")


def trava(medidas, lista, regras=("antiga", "b"), falhas_objetivas=None, reconferidas=None):
    """{"voltam": [{tela, regras, motivos}], "sinais": [{tela, motivos}]}. Com `reconferidas` (a volta), a regra antiga
    só vale nessas telas."""
    falhas_objetivas = falhas_objetivas or {}
    _confere(medidas, lista, falhas_objetivas, reconferidas)
    voltam, sinais = [], []
    for m in sorted(medidas, key=lambda x: x["tela"]):
        t = m["tela"]
        li = lista[t]
        med = falhas_de_medida(m)
        itens_nao = [f"{k}: não (lista da I2)" for k in OBJETIVOS if li["itens"].get(k) == "não"]
        mao = [f"{falhas_objetivas[t]} (conferido à mão)"] if t in falhas_objetivas else []
        comparada = reconferidas is None or t in reconferidas
        motivos, regra = [], []
        if "antiga" in regras and comparada and li["perde"] == "sim" and (med or itens_nao or mao):
            regra.append("antiga")
            motivos += ["perde nas duas ordens"] + itens_nao + med + mao
        if "b" in regras and li["itens"]["Dest"] == "não" and m["destaque_manuscrito"] == 0:
            regra.append("b")
            motivos += ["Dest: não (lista da I2)", "destaque manuscrito: nenhum além do título (medida)"]
        sinal = []
        if regra:
            voltam.append({"tela": t, "regras": regra, "motivos": list(dict.fromkeys(motivos))})
        else:
            if li["perde"] == "sim":
                sinal.append("perde nas duas ordens, sem falha objetiva" if comparada
                             else "perdia na comparação da versão anterior, sem reconferência nesta volta")
            sinal += med + itens_nao + mao
        nao_medidas = [n for n, c in (("margem", "margem_esq_min"), ("transborda", "transborda")) if m.get(c) is None]
        if nao_medidas and "antiga" in regras and comparada and li["perde"] == "sim":
            sinal.append(f"{' e '.join(nao_medidas)} não medidos (medidas sem navegador): a regra antiga não os viu")
        if li["itens"].get("Can") in ("não", "parcial"):
            sinal.append(f"Can: {li['itens']['Can']} (item de leitura)")
        if sinal:
            sinais.append({"tela": t, "motivos": sinal})
    return {"voltam": voltam, "sinais": sinais}


def _falhas(textos):
    falhas = {}
    for texto in textos:
        n, sep, motivo = texto.partition(":")
        if not sep or not n.strip().isdigit() or not motivo.strip():
            raise TravaErro(f"--falha-objetiva: esperado N:motivo, veio {texto!r}")
        n = int(n)
        falhas[n] = f"{falhas[n]}; {motivo.strip()}" if n in falhas else motivo.strip()
    return falhas


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("medidas")
    ap.add_argument("relatorio")
    ap.add_argument("--reconferencia", help="o relatório da reconferência de uma volta: as telas dele trocam as do primeiro")
    ap.add_argument("--anterior", help="o trava.json da rodada anterior (obrigatório com --reconferencia)")
    ap.add_argument("--falha-objetiva", action="append", default=[], metavar="N:motivo")
    ap.add_argument("--json")
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 2
    try:
        falhas = _falhas(a.falha_objetiva)
        medidas = json.loads(Path(a.medidas).read_text(encoding="utf-8"))
        lista = ler_relatorio(a.relatorio)
        reconferidas = None
        if bool(a.reconferencia) != bool(a.anterior):
            raise TravaErro("--reconferencia e --anterior vão juntos")
        if a.reconferencia:
            nova = ler_relatorio(a.reconferencia)
            ant = json.loads(Path(a.anterior).read_text(encoding="utf-8"))
            voltaram = {v["tela"] for v in ant.get("voltam", [])} if isinstance(ant, dict) else None
            if voltaram is None:
                raise TravaErro(f"o --anterior não é um trava.json: {a.anterior}")
            if set(nova) != voltaram:
                raise TravaErro(f"a reconferência traz as telas {sorted(nova)}, e voltaram {sorted(voltaram)}")
            lista.update(nova)
            reconferidas = set(nova)
        res = trava(medidas, lista, falhas_objetivas=falhas, reconferidas=reconferidas)
        if a.json:
            Path(a.json).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    except (TravaErro, OSError, json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"ERRO: {e}", file=sys.stderr)
        return 2
    for v in res["voltam"]:
        print(f"VOLTA tela {v['tela']} ({', '.join(v['regras'])}): {'; '.join(v['motivos'])}")
    for s in res["sinais"]:
        print(f"sinal tela {s['tela']}: {'; '.join(s['motivos'])}")
    if not res["voltam"]:
        print("Nenhuma tela volta.")
    return 1 if res["voltam"] else 0


if __name__ == "__main__":
    sys.exit(main())
