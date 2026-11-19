"""Gera o Mermaid de um diagrama a partir do mesmo JSON, para o ADR e o README, que o GitHub desenha sozinho.

O onboarding usa as páginas do kit (com a conferência e a lista em texto); o Mermaid é a cópia para onde só cabe um
bloco de código. O fluxo e o grafo saem como `flowchart` (os grupos como `subgraph`, a recusa e a volta tracejadas), a
sequência como `sequenceDiagram` (mensagem, resposta, nota, alt, loop e opt). Os dois levam `accTitle` e `accDescr`,
que o Mermaid usa como título e descrição para o leitor de tela.

Uso: python -X utf8 diagrama_mermaid.py <dados.json> [--saida <arquivo.mmd>]
  sem --saida, imprime; o dado passa antes pelo diagrama_esquema.py, e o que não serve para com o achado."""
import argparse, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import diagrama_esquema as esquema  # noqa: E402


# os caracteres que fecham ou abrem um trecho da sintaxe (a aspa do rótulo, o '|' do rótulo da seta, o ';' que vale
# por quebra de linha, o '#' das entidades, os sinais de HTML e os colchetes e parênteses das formas) saem como entidade
# do Mermaid (#código;), que ele desenha como o caractere; numa passada só, para a entidade gerada não ser escapada de novo
_ESCAPES = {"#": "#35;", '"': "#quot;", "|": "#124;", ";": "#59;", "<": "#lt;", ">": "#gt;",
            "[": "#91;", "]": "#93;", "(": "#40;", ")": "#41;", "{": "#123;", "}": "#125;"}
_RE_ESCAPE = re.compile("[" + re.escape("".join(_ESCAPES)) + "]")


def _txt(s) -> str:
    """O texto de um rótulo, de um nó ou de uma mensagem: numa linha só, com a sintaxe do Mermaid escapada."""
    t = re.sub(r"\s+", " ", str(s or "")).strip()
    return _RE_ESCAPE.sub(lambda m: _ESCAPES[m.group(0)], t)


def _acc(s) -> str:
    """O accTitle e o accDescr: o leitor de tela lê o texto cru, então só uma linha e sem o ';' que quebraria a linha."""
    return re.sub(r"\s+", " ", str(s or "")).replace(";", ",").strip()


RESERVADAS = {"end", "graph", "subgraph", "flowchart", "class", "classDef", "style", "click", "default"}


def _id(s) -> str:
    i = re.sub(r"[^A-Za-z0-9_]", "_", str(s))
    return "n_" + i if i in RESERVADAS or i[:1].isdigit() else i  # "end" e afins quebram o Mermaid


class Colisao(ValueError):
    pass


def _sem_colisao(ids) -> None:
    """Dois ids diferentes no JSON que viram o mesmo id no Mermaid ("a-b" e "a b" viram "a_b") fundiriam os nós."""
    vistos = {}
    for i in ids:
        vistos.setdefault(_id(i), set()).add(str(i))
    pares = {k: sorted(v) for k, v in vistos.items() if len(v) > 1}
    if pares:
        raise Colisao("ids que viram o mesmo id no Mermaid: " + "; ".join(f"{' e '.join(v)} -> {k}" for k, v in pares.items()))


def flowchart(d: dict) -> str:
    direcao = {"DOWN": "TD", "RIGHT": "LR"}.get(d.get("direcao"), "LR")
    _sem_colisao([n["id"] for n in d["nos"]] + ["g_" + g["id"] for g in d["grupos"]])
    out = [f"flowchart {direcao}", f"  accTitle: {_acc(d['titulo'])}", f"  accDescr: {_acc(d['afirmacao'])}"]
    for g in d["grupos"]:
        out.append(f'  subgraph {_id("g_" + g["id"])}["{_txt(g["rotulo"])}"]')
        for n in [n for n in d["nos"] if n.get("grupo") == g["id"]]:
            num = f"{n['numero']}. " if n.get("numero") is not None else ""
            tec = f"<br/>[{_txt(n['tecnologia'])}]" if n.get("tecnologia") else ""
            # no grafo (a arquitetura), a pessoa é ator do C4 e ganha a forma arredondada; no fluxo, é o passo em que a pessoa decide
            forma = ('(["', '"])') if n.get("tipo") == "pessoa" and d.get("modelo") == "grafo" else ('["', '"]')
            out.append(f"    {_id(n['id'])}{forma[0]}{_txt(num + n['titulo'])}{tec}{forma[1]}")
        out.append("  end")
    for a in d["arestas"]:
        r = _txt(a.get("rotulo") or (d.get("legenda", {}).get(a["tipo"]) if a["tipo"] != "avanço" else ""))
        seta = "-->" if a["tipo"] == "avanço" else "-.->"
        out.append(f"  {_id(a['de'])} {seta}{'|' + r + '|' if r else ''} {_id(a['para'])}")
    out += ["  classDef pessoa fill:#e3f0e8,stroke:#2f6f4e", "  classDef maquina fill:#f7ecdc,stroke:#9a5b13"]
    for tipo, cls in (("pessoa", "pessoa"), ("máquina", "maquina")):
        ids = [_id(n["id"]) for n in d["nos"] if n.get("tipo") == tipo]
        if ids:
            out.append(f"  class {','.join(ids)} {cls}")
    return "\n".join(out) + "\n"


def sequencia(d: dict, base: Path) -> str:
    nos = {}
    if d.get("arquitetura"):
        nos = {n["id"]: n for n in esquema.carregar(base / d["arquitetura"]).get("nos", [])}
    _sem_colisao([p if isinstance(p, str) else p["id"] for p in d["participantes"]])
    out = ["sequenceDiagram", f"  accTitle: {_acc(d['titulo'])}", f"  accDescr: {_acc(d['afirmacao'])}", "  autonumber"]
    for p in d["participantes"]:
        pid = p if isinstance(p, str) else p["id"]
        titulo = (p.get("titulo") if isinstance(p, dict) else None) or nos.get(pid, {}).get("titulo") or pid
        tipo = (p.get("tipo") if isinstance(p, dict) else None) or nos.get(pid, {}).get("tipo")
        out.append(f"  {'actor' if tipo == 'pessoa' else 'participant'} {_id(pid)} as {_txt(titulo)}")

    def passos(lista, recuo):
        for s in lista:
            if s["tipo"] == "mensagem":
                out.append(f"{recuo}{_id(s['de'])}{'-->>' if s.get('retorno') else '->>'}{_id(s['para'])}: {_txt(s['texto'])}")
            elif s["tipo"] == "nota":
                sobre = ",".join(_id(x) for x in ([s["sobre"]] if isinstance(s["sobre"], str) else s["sobre"]))
                out.append(f"{recuo}Note over {sobre}: {_txt(s['texto'])}")
            else:
                out.append(f"{recuo}{s['bloco']} {_txt(s['rotulo'])}")
                passos(s["passos"], recuo + "  ")
                if s.get("senao"):
                    out.append(f"{recuo}else {_txt(s['senao']['rotulo'])}")
                    passos(s["senao"]["passos"], recuo + "  ")
                out.append(f"{recuo}end")
    passos(d["passos"], "  ")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dados")
    ap.add_argument("--saida")
    a = ap.parse_args()
    p = Path(a.dados)
    erros = [x for x in esquema.validar_arquivo(p) if x["nivel"] == "erro"]
    if erros:
        for x in erros:
            print(f"[ERRO] {x['codigo']} {x['onde']}: {x['mensagem']} (dica: {x['dica']})", file=sys.stderr)
        sys.exit(1)
    d = esquema.carregar(p)
    try:
        texto = sequencia(d, p.parent) if d.get("modelo") == "sequencia" else flowchart(d)
    except Colisao as e:
        print(f"[ERRO] MMD-ID {p.name}: {e} (dica: dê ids que não colidam ao trocar o que não é letra, número ou _ por _)", file=sys.stderr)
        sys.exit(1)
    if a.saida:
        Path(a.saida).write_text(texto, encoding="utf-8")
    else:
        print(texto, end="")


if __name__ == "__main__":
    main()
