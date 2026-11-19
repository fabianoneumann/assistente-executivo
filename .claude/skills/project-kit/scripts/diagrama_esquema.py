"""O esquema dos dados dos diagramas, conferido fora do navegador (sem dependência além da biblioteca padrão).

Três modelos, pelo campo "modelo" do dado: "fluxo" (o padrão, quando o campo falta), "grafo" e "sequencia".
Cada achado sai com um código estável, o lugar, a mensagem e a dica de correção. Os de nível "erro" fazem o
script sair com 1; os de nível "aviso" (dividir a sequência grande) só aparecem.

No grafo com "c4" (por exemplo "contêiner"), as regras de notação do C4 também se conferem: o título diz o tipo
e o escopo, a legenda explica o que se usa, todo contêiner diz a tecnologia, toda seta tem rótulo e nenhum rótulo
é genérico ("usa", "chama" sozinhos).

A sequência é uma vista do mesmo dado da arquitetura: "arquitetura" aponta o JSON do grafo (caminho relativo ao
arquivo da sequência), e cada participante é um id de nó dele.

Uso: python -X utf8 diagrama_esquema.py <dados.json | pagina.html> [...] [--json]
  (na página .html, lê a cópia embutida em <script id="dados-embutidos">, como a que vai ao projeto)"""
import argparse, glob, json, re, sys
from pathlib import Path

TIPOS_NO = ("pessoa", "máquina", "neutro")
TIPOS_ARESTA = ("avanço", "recusa", "volta")
TIPOS_BLOCO = ("alt", "loop", "opt")
GENERICOS = {"usa", "chama", "acessa", "conecta", "interage", "envia", "depende", "liga", "fala com", "usa o", "usa a"}
C4_TITULO = re.compile(r"^\s*(Contexto|Contêineres|Componentes|Código)\s*:\s*\S", re.I)
LIMITE_MENSAGENS, LIMITE_PARTICIPANTES, LIMITE_NIVEIS = 20, 7, 3

DICAS = {
    "ESQ-JSON": "corrija o JSON (vírgula, aspas, chave) até ele abrir num validador",
    "ESQ-MODELO": "use \"fluxo\", \"grafo\" ou \"sequencia\" em \"modelo\"",
    "ESQ-TEXTO": "escreva o texto do campo; ele aparece na figura ou na lista em texto",
    "ESQ-LISTA": "o campo é uma lista JSON ([...])",
    "ESQ-LEGENDA": "dê em \"legenda\" uma frase para cada tipo que o diagrama usa",
    "ESQ-ID": "dê a cada nó e grupo um id único, sem repetir",
    "ESQ-TIPO": "use um dos tipos da mensagem",
    "ESQ-GRUPO": "crie o grupo em \"grupos\" ou troque o \"grupo\" do nó",
    "ESQ-REF": "troque pelo id de um nó que existe, ou crie o nó",
    "ESQ-LACO": "o laço que volta ao próprio passo é \"recusa\", não \"avanço\"",
    "ESQ-VERSAO": "aponte \"versao.origem\" para um passo que existe e dê a lista \"versao.portas\"",
    "C4-TITULO": "comece o título pelo tipo e pelo escopo, como \"Contêineres: o sistema X\"",
    "C4-LEGENDA": "explique na legenda cada tipo usado e a fronteira (\"grupo\")",
    "C4-TECNOLOGIA": "diga em \"tecnologia\" com o que o contêiner é feito (\"Python, FastAPI\")",
    "C4-ROTULO": "dê à seta um rótulo que diga o que passa por ela",
    "C4-GENERICO": "troque o verbo genérico pelo que de fato acontece (\"lê e grava por SQL\", \"faz o pedido por HTTPS\")",
    "SEQ-ARQUITETURA": "aponte \"arquitetura\" para o JSON do grafo, com o caminho relativo a este arquivo",
    "SEQ-PARTICIPANTE": "use o id de um nó da arquitetura, para a sequência ser vista do mesmo dado",
    "SEQ-REF": "a mensagem só liga participantes da lista \"participantes\"",
    "SEQ-BLOCO": "o bloco é alt, loop ou opt, com \"rotulo\" e a lista \"passos\"",
    "SEQ-DIVIDIR": "divida a sequência em duas figuras: acima do limite, ela deixa de se ler de uma vez",
}


def carregar(caminho: Path):
    """O dado de um .json, ou a cópia embutida de uma página .html."""
    texto = caminho.read_text(encoding="utf-8")
    if caminho.suffix.lower() in (".html", ".htm"):
        m = re.search(r'<script[^>]*id="dados-embutidos"[^>]*>(.*?)</script>', texto, re.S)
        if not m:
            raise ValueError("a página não tem a cópia embutida (<script id=\"dados-embutidos\">)")
        texto = m.group(1)
    return json.loads(texto)


class Conferencia:
    def __init__(self):
        self.achados = []

    def add(self, codigo, onde, mensagem, nivel="erro"):
        self.achados.append({"codigo": codigo, "nivel": nivel, "onde": onde, "mensagem": mensagem, "dica": DICAS.get(codigo, "")})

    def texto(self, v, onde):
        if not isinstance(v, str) or not v.strip():
            self.add("ESQ-TEXTO", onde, "falta o texto")
            return False
        return True

    def lista(self, d, k):
        if not isinstance(d.get(k), list):
            self.add("ESQ-LISTA", k, "falta a lista")
            return False
        return True


def _nos_e_grupos(c: Conferencia, d: dict, com_versao: bool):
    c.texto(d.get("titulo"), "titulo"); c.texto(d.get("afirmacao"), "afirmacao")
    ok = all([c.lista(d, "nos"), c.lista(d, "arestas"), c.lista(d, "grupos")])
    leg = d.get("legenda")
    if not isinstance(leg, dict):
        c.add("ESQ-LEGENDA", "legenda", "falta o objeto da legenda"); leg = {}
    if not ok:
        return set()
    if not d["nos"]:
        c.add("ESQ-LISTA", "nos", "a lista está vazia")
    gids, ids = set(), set()
    for k, g in enumerate(d["grupos"]):
        g = g if isinstance(g, dict) else {}
        c.texto(g.get("id"), f"grupos[{k}].id"); c.texto(g.get("rotulo"), f"grupos[{k}].rotulo")
        gids.add(g.get("id"))
    for k, n in enumerate(d["nos"]):
        n = n if isinstance(n, dict) else {}
        onde = f"nos[{k}]" + (f" ({n.get('id')})" if n.get("id") else "")
        c.texto(n.get("id"), onde + ".id"); c.texto(n.get("titulo"), onde + ".titulo")
        # no grafo o grupo também é nó do motor, então o id não pode repetir o de um grupo; no fluxo, pode
        if n.get("id") in ids or (not com_versao and n.get("id") in gids):
            c.add("ESQ-ID", onde, f"o id \"{n.get('id')}\" se repete")
        ids.add(n.get("id"))
        if n.get("tipo") not in TIPOS_NO:
            c.add("ESQ-TIPO", onde + ".tipo", f"\"{n.get('tipo')}\" não é {', '.join(TIPOS_NO)}")
        if n.get("grupo") not in gids:
            c.add("ESQ-GRUPO", onde + ".grupo", f"o grupo \"{n.get('grupo')}\" não existe em grupos")
    usados = {n.get("tipo") for n in d["nos"] if isinstance(n, dict)}
    for k, a in enumerate(d["arestas"]):
        a = a if isinstance(a, dict) else {}
        onde = f"arestas[{k}] ({a.get('de')} → {a.get('para')})"
        for lado in ("de", "para"):
            if a.get(lado) not in ids:
                c.add("ESQ-REF", onde, f"o nó \"{a.get(lado)}\" (em {lado}) não existe em nos")
        if a.get("tipo") not in TIPOS_ARESTA:
            c.add("ESQ-TIPO", onde + ".tipo", f"\"{a.get('tipo')}\" não é {', '.join(TIPOS_ARESTA)}")
        elif a["tipo"] == "avanço" and a.get("de") == a.get("para"):
            c.add("ESQ-LACO", onde, "o avanço não volta ao próprio passo")
        rot = a.get("rotulo")  # sem rótulo é null ou ""; o rótulo só de espaços conta como saída e não aparece
        if rot not in (None, "") and (not isinstance(rot, str) or not rot.strip()):
            c.add("ESQ-TEXTO", onde + ".rotulo", "o rótulo só tem espaços: tire o texto ou escreva o rótulo")
        usados.add(a.get("tipo"))
    for t in ("pessoa", "máquina", "recusa", "volta"):
        if t in usados and not (isinstance(leg.get(t), str) and leg[t].strip()):
            c.add("ESQ-LEGENDA", f"legenda.{t}", f"o diagrama usa \"{t}\" e a legenda não o explica")
    if com_versao and d.get("versao") is not None:
        v = d["versao"] if isinstance(d["versao"], dict) else {}
        if v.get("origem") not in ids or not isinstance(v.get("portas"), list):
            c.add("ESQ-VERSAO", "versao", "a origem não existe em nos ou falta a lista de portas")
    return ids


def _c4(c: Conferencia, d: dict):
    if not C4_TITULO.search(d.get("titulo") or ""):
        c.add("C4-TITULO", "titulo", f"\"{d.get('titulo')}\" não diz o tipo e o escopo")
    leg = d.get("legenda") if isinstance(d.get("legenda"), dict) else {}
    if not leg.get("grupo"):
        c.add("C4-LEGENDA", "legenda.grupo", "a legenda não explica a fronteira")
    for k, n in enumerate(d.get("nos") or []):
        if isinstance(n, dict) and n.get("tipo") != "pessoa" and not str(n.get("tecnologia") or "").strip():
            c.add("C4-TECNOLOGIA", f"nos[{k}] ({n.get('id')})", "o contêiner não diz a tecnologia")
    for k, a in enumerate(d.get("arestas") or []):
        if not isinstance(a, dict):
            continue
        onde, r = f"arestas[{k}] ({a.get('de')} → {a.get('para')})", str(a.get("rotulo") or "").strip()
        if not r:
            c.add("C4-ROTULO", onde, "a seta não tem rótulo")
        elif r.lower() in GENERICOS:
            c.add("C4-GENERICO", onde, f"o rótulo \"{r}\" é genérico")


def _sequencia(c: Conferencia, d: dict, caminho: Path | None):
    c.texto(d.get("titulo"), "titulo"); c.texto(d.get("afirmacao"), "afirmacao")
    arq_ids = None
    if isinstance(d.get("_nos"), dict):
        # a cópia embutida na página (o projeto não tem o JSON da arquitetura ao lado): os nós vieram junto, em "_nos"
        arq_ids = set(d["_nos"])
    elif d.get("arquitetura"):
        alvo = (caminho.parent / d["arquitetura"]) if caminho else Path(d["arquitetura"])
        try:
            arq = carregar(alvo); arq_ids = {n.get("id") for n in arq.get("nos", []) if isinstance(n, dict)}
        except (OSError, ValueError) as e:
            c.add("SEQ-ARQUITETURA", "arquitetura", f"não abriu {d['arquitetura']}: {e}")
    if not c.lista(d, "participantes") or not c.lista(d, "passos"):
        return
    pids = []
    for k, p in enumerate(d["participantes"]):
        pid = p if isinstance(p, str) else (p.get("id") if isinstance(p, dict) else None)
        if not pid:
            c.add("ESQ-TEXTO", f"participantes[{k}]", "falta o id"); continue
        if pid in pids:
            c.add("ESQ-ID", f"participantes[{k}]", f"o participante \"{pid}\" se repete")
        if arq_ids is not None and pid not in arq_ids and not (isinstance(p, dict) and p.get("titulo")):
            c.add("SEQ-PARTICIPANTE", f"participantes[{k}]", f"\"{pid}\" não é um nó da arquitetura")
        pids.append(pid)
    conta = {"mensagens": 0, "nivel": 0}

    def passos(lista, onde, nivel):
        conta["nivel"] = max(conta["nivel"], nivel)
        for k, s in enumerate(lista):
            o = f"{onde}[{k}]"
            if not isinstance(s, dict):
                c.add("ESQ-TIPO", o, "o passo não é um objeto"); continue
            t = s.get("tipo")
            if t == "mensagem":
                conta["mensagens"] += 1
                for lado in ("de", "para"):
                    if s.get(lado) not in pids:
                        c.add("SEQ-REF", f"{o}.{lado}", f"\"{s.get(lado)}\" não está em participantes")
                c.texto(s.get("texto"), o + ".texto")
            elif t == "nota":
                sobre = s.get("sobre") if isinstance(s.get("sobre"), list) else [s.get("sobre")]
                for x in sobre:
                    if x not in pids:
                        c.add("SEQ-REF", o + ".sobre", f"\"{x}\" não está em participantes")
                c.texto(s.get("texto"), o + ".texto")
            elif t == "bloco":
                if s.get("bloco") not in TIPOS_BLOCO or not isinstance(s.get("passos"), list):
                    c.add("SEQ-BLOCO", o, f"o bloco \"{s.get('bloco')}\" não é {', '.join(TIPOS_BLOCO)} ou falta a lista passos"); continue
                c.texto(s.get("rotulo"), o + ".rotulo")
                passos(s["passos"], o + ".passos", nivel + 1)
                if s.get("senao") is not None:
                    se = s["senao"] if isinstance(s["senao"], dict) else {}
                    if s["bloco"] != "alt" or not isinstance(se.get("passos"), list):
                        c.add("SEQ-BLOCO", o + ".senao", "o senão só existe no alt, com a lista passos"); continue
                    c.texto(se.get("rotulo"), o + ".senao.rotulo")
                    passos(se["passos"], o + ".senao.passos", nivel + 1)
            else:
                c.add("ESQ-TIPO", o + ".tipo", f"\"{t}\" não é mensagem, nota ou bloco")

    passos(d["passos"], "passos", 0)
    if conta["mensagens"] > LIMITE_MENSAGENS:
        c.add("SEQ-DIVIDIR", "passos", f"{conta['mensagens']} mensagens (o limite é {LIMITE_MENSAGENS})", "aviso")
    if len(pids) > LIMITE_PARTICIPANTES:
        c.add("SEQ-DIVIDIR", "participantes", f"{len(pids)} participantes (o limite é {LIMITE_PARTICIPANTES})", "aviso")
    if conta["nivel"] > LIMITE_NIVEIS:
        c.add("SEQ-DIVIDIR", "passos", f"{conta['nivel']} níveis de bloco (o limite é {LIMITE_NIVEIS})", "aviso")


def validar(d, caminho: Path | None = None) -> list:
    """Os achados do dado (vazio quando serve)."""
    c = Conferencia()
    if not isinstance(d, dict):
        c.add("ESQ-JSON", "(raiz)", "o dado não é um objeto JSON"); return c.achados
    modelo = d.get("modelo", "fluxo")
    if modelo == "fluxo":
        _nos_e_grupos(c, d, com_versao=True)
    elif modelo == "grafo":
        _nos_e_grupos(c, d, com_versao=False)
        if d.get("c4"):
            _c4(c, d)
    elif modelo == "sequencia":
        _sequencia(c, d, caminho)
    else:
        c.add("ESQ-MODELO", "modelo", f"\"{modelo}\" não é fluxo, grafo ou sequencia")
    return c.achados


def validar_arquivo(caminho: Path) -> list:
    try:
        return validar(carregar(caminho), caminho)
    except (OSError, ValueError) as e:
        return [{"codigo": "ESQ-JSON", "nivel": "erro", "onde": str(caminho.name), "mensagem": str(e), "dica": DICAS["ESQ-JSON"]}]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("arquivos", nargs="+")
    ap.add_argument("--json", action="store_true", help="a saída em JSON, um objeto por arquivo")
    a = ap.parse_args()
    res, erros = {}, 0
    nomes = []
    for nome in a.arquivos:  # o padrão (*.html) se expande aqui também, porque o shell do Windows não o expande
        nomes += sorted(glob.glob(nome)) if any(c in nome for c in "*?[") else [nome]
    for nome in nomes:
        p = Path(nome); ach = validar_arquivo(p); res[str(p)] = ach
        erros += sum(1 for x in ach if x["nivel"] == "erro")
        if not a.json:
            if not ach:
                print(f"[OK] {p.name}")
            for x in ach:
                print(f"[{x['nivel'].upper()}] {p.name} {x['codigo']} {x['onde']}: {x['mensagem']} (dica: {x['dica']})")
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
