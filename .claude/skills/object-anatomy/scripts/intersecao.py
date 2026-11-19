"""A conferência de interseção do objeto que se move: nada atravessa nada, em repouso e em cada quadro da explosão
(R20 do método, `.claude/skills/object-anatomy/references/metodo.md`). Roda antes de qualquer render: um atravessamento
para a skill.

Lê um `pecas.json` que o script de geometria da peça exporta (R10: a geometria sai de código, nunca a olho) e diz, estado
a estado, que pares de peças se atravessam e quanto. Não desenha nem abre navegador: confere a geometria verdadeira,
não a imagem, porque na imagem a peça da frente cobre a de trás e o atravessamento não aparece.

O modelo: cada peça é um polígono simples num plano (o perfil (x, r) da peça de revolução, a vista de frente do
mecanismo plano, a planta da peça em camadas), com uma faixa opcional de profundidade fora desse plano. Duas peças se
atravessam quando as faixas de profundidade se cruzam (ou alguma não tem faixa) e os polígonos entram um no outro além
da tolerância de encosto. A medida (`fundo`) é o maior entre dois números: o quanto a borda de uma entra na outra (o
maior afastamento, para dentro, de um vértice, exato, ou de um ponto ao longo de um lado, a cada `passo`) e a espessura
da sobreposição (o dobro do afastamento, das duas bordas, do ponto mais fundo de dentro das duas, numa grade), que pega
as peças coincidentes ou quase. É um piso: a verdadeira pode passar dele. Encostar não conta. O polígono tem de ser
simples (área diferente de zero, sem lado cruzando outro); o ponto de fecho repetido sai sozinho.

    {
      "tolerancia": 0.02,                  # o encosto permitido no plano, na unidade da geometria
      "tolerancia_profundidade": 0.02,     # opcional: o mesmo, no eixo da profundidade (padrão: a tolerância)
      "passo": 0.02,                       # opcional: o espaço entre os pontos amostrados nos lados
                                           # (padrão: a tolerância, ou 1/500 da diagonal da cena, o que for maior)
      "pecas": [
        {"nome": "roda dentada", "grupo": "roda", "poligono": [[x, y], ...], "profundidade": [z0, z1]},
        ...
      ],
      "estados": [                         # o repouso e cada quadro da explosão (o modelo de movimento os exporta)
        {"rotulo": "repouso"},
        {"rotulo": "t=0.033", "desloca": {"roda": [dx, dy]}, "gira": {"ponteiro": {"angulo": 12, "centro": [x, y]}}}
      ],
      "cruzamentos_de_projeto": [          # o que atravessa de propósito, sempre com o porquê
        {"pecas": ["eixo do ponteiro", "mostrador"], "porque": "o eixo passa pelo furo do mostrador", "fundo_max": 0.4}
      ]
    }

O `desloca` aceita [dx, dy] ou [dx, dy, dz] (o dz move a faixa de profundidade); o `gira` gira o grupo no plano, em
graus, em volta do centro, antes do deslocamento. Grupo sem entrada no estado fica onde está no repouso. A faixa de
espessura zero é uma camada plana: atravessa a outra camada plana na mesma altura, e a faixa que a contém por dentro;
encostada na face de um bloco, não. O par que não se moveu um em relação ao outro desde um estado já conferido não se
mede de novo (a grade da espessura segue os eixos, então o par que gira junto pode medir um pouco diferente girado; o
número continua um piso). O ponto repetido em seguida sai sozinho. O cruzamento declarado com `fundo_max` volta a ser atravessamento quando entra
além dele; sem `fundo_max`, o par fica livre em todos os estados. A declaração que nunca cruza sai num aviso, para
conferir se ainda vale.

    python -X utf8 .claude/skills/object-anatomy/scripts/intersecao.py <pasta-da-peca>/object/pecas.json [--json] [--max 40]

Saída 0: nenhum atravessamento fora dos declarados; 1: há atravessamento (a lista diz o estado, o par e o fundo);
2: o `pecas.json` é inválido. O zero é necessário, não suficiente: o zoom de 4× nas juntas (`juntas.py`, ao
lado) continua sendo lido. Testes em `teste_intersecao.py`, ao lado.
"""
import argparse
import json
import math
import sys
import traceback

GRADE_GROSSA = 5  # pontos por eixo na grade de dentro que roda em todo par que se toca
GRADE = 16        # na fina, que mede a espessura quando a borda ou a grossa já acusaram


def _num(v, onde):
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise ValueError(f"{onde}: esperava um número, veio {v!r}")
    v = float(v)
    if not math.isfinite(v):
        raise ValueError(f"{onde}: número não finito ({v})")
    return v


def _obj(v, onde):
    if not isinstance(v, dict):
        raise ValueError(f"{onde}: esperava um objeto, veio {v!r}")
    return v


def _lista(v, onde):
    if not isinstance(v, list):
        raise ValueError(f"{onde}: esperava uma lista, veio {v!r}")
    return v


def _ponto(v, onde):
    _lista(v, onde)
    if len(v) != 2:
        raise ValueError(f"{onde}: o ponto tem de ser [x, y]")
    return _num(v[0], onde), _num(v[1], onde)


def _valida(d):
    _obj(d, "o pecas.json")
    for campo in ("tolerancia", "pecas", "estados"):
        if campo not in d:
            raise ValueError(f"falta o campo '{campo}'")
    tol = _num(d["tolerancia"], "tolerancia")
    if tol < 0:
        raise ValueError("a tolerância não pode ser negativa")
    tz = d.get("tolerancia_profundidade")
    tolz = tol if tz is None else _num(tz, "tolerancia_profundidade")  # null é o padrão, como no "passo"
    if tolz < 0:
        raise ValueError("a tolerância de profundidade não pode ser negativa")
    if not _lista(d["pecas"], "pecas"):
        raise ValueError("nenhuma peça")
    nomes, grupos, pecas = set(), set(), []
    for i, p in enumerate(d["pecas"]):
        _obj(p, f"a peça {i}")
        nome = p.get("nome")
        if not isinstance(nome, str) or not nome:
            raise ValueError(f"a peça {i} não tem nome")
        if nome in nomes:
            raise ValueError(f"nome repetido: {nome}")
        poli = [_ponto(q, f"'{nome}', polígono") for q in _lista(p.get("poligono") or [], f"'{nome}', polígono")]
        poli = [q for k, q in enumerate(poli) if k == 0 or q != poli[k - 1]]  # o ponto repetido em seguida
        if len(poli) > 3 and poli[0] == poli[-1]:
            poli = poli[:-1]                                   # o ponto de fecho repetido, comum nas exportações
        if len(poli) < 3:
            raise ValueError(f"'{nome}': o polígono precisa de pelo menos 3 pontos")
        _confere_simples(poli, nome)
        prof = p.get("profundidade")
        if prof is not None:
            z0, z1 = _ponto(prof, f"'{nome}', profundidade")
            prof = (min(z0, z1), max(z0, z1))
        grupo = p.get("grupo") or nome
        if not isinstance(grupo, str):
            raise ValueError(f"'{nome}': o grupo tem de ser um nome")
        nomes.add(nome)
        grupos.add(grupo)
        pecas.append({"nome": nome, "grupo": grupo, "poligono": poli, "profundidade": prof})
    if not _lista(d["estados"], "estados"):
        raise ValueError("nenhum estado (pelo menos o repouso)")
    estados = []
    for i, e in enumerate(d["estados"]):
        _obj(e, f"o estado {i}")
        rot = str(e.get("rotulo") or f"estado {i}")
        desl, gira = {}, {}
        for g, v in _obj(e.get("desloca") or {}, f"estado '{rot}', desloca").items():
            if g not in grupos:
                raise ValueError(f"estado '{rot}': grupo inexistente em desloca: {g}")
            _lista(v, f"estado '{rot}', desloca de '{g}'")
            if len(v) not in (2, 3):
                raise ValueError(f"estado '{rot}': o deslocamento de '{g}' tem de ser [dx, dy] ou [dx, dy, dz]")
            desl[g] = tuple(_num(x, f"estado '{rot}', desloca de '{g}'") for x in v) + ((0.0,) if len(v) == 2 else ())
        for g, v in _obj(e.get("gira") or {}, f"estado '{rot}', gira").items():
            if g not in grupos:
                raise ValueError(f"estado '{rot}': grupo inexistente em gira: {g}")
            _obj(v, f"estado '{rot}', gira de '{g}' (esperava {{\"angulo\": graus, \"centro\": [x, y]}})")
            cx, cy = _ponto(v.get("centro", [0, 0]), f"estado '{rot}', centro do giro de '{g}'")
            gira[g] = (math.radians(_num(v.get("angulo", 0), f"estado '{rot}', ângulo de '{g}'")), cx, cy)
        estados.append({"rotulo": rot, "desloca": desl, "gira": gira})
    declarados = {}
    for c in _lista(d.get("cruzamentos_de_projeto") or [], "cruzamentos_de_projeto"):
        _obj(c, "cruzamento de projeto")
        par = c.get("pecas") or []
        if (not isinstance(par, list) or len(par) != 2 or not all(isinstance(n, str) for n in par)
                or par[0] == par[1] or any(n not in nomes for n in par)):
            raise ValueError(f"cruzamento de projeto precisa de duas peças diferentes que existem: {par}")
        if frozenset(par) in declarados:
            raise ValueError(f"cruzamento de projeto declarado duas vezes: {par}")
        porque = c.get("porque")
        if not isinstance(porque, str) or not porque.strip():
            raise ValueError(f"cruzamento de projeto sem o porquê: {par}")
        fmax = c.get("fundo_max")
        declarados[frozenset(par)] = {"pecas": sorted(par), "porque": porque,
                                      "fundo_max": None if fmax is None else _num(fmax, f"fundo_max de {par}")}
    xs = [q[0] for p in pecas for q in p["poligono"]]
    ys = [q[1] for p in pecas for q in p["poligono"]]
    diagonal = math.hypot(max(xs) - min(xs), max(ys) - min(ys))
    if "passo" in d and d["passo"] is not None:
        passo = _num(d["passo"], "passo")
        if passo <= 0:
            raise ValueError("o passo tem de ser positivo")
    else:
        passo = max(tol, diagonal / 500) or 1e-6
    return tol, tolz, passo, pecas, estados, declarados


def _confere_simples(poli, nome):
    """O modelo pede polígono simples: área diferente de zero e nenhum lado cruzando outro não vizinho."""
    n = len(poli)
    area = sum(poli[i][0] * poli[(i + 1) % n][1] - poli[(i + 1) % n][0] * poli[i][1] for i in range(n)) / 2
    if abs(area) < 1e-12:
        raise ValueError(f"'{nome}': o polígono tem área zero")
    lados = [(poli[i], poli[(i + 1) % n]) for i in range(n)]
    for i in range(n):
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue                                       # o primeiro e o último lado são vizinhos
            if _segmentos_se_tocam(*lados[i], *lados[j]):
                raise ValueError(f"'{nome}': o polígono cruza a si mesmo (lados {i} e {j})")


def _transforma(poli, gira, desl):
    pts = poli
    if gira:
        a, cx, cy = gira
        c, s = math.cos(a), math.sin(a)
        pts = [(cx + (x - cx) * c - (y - cy) * s, cy + (x - cx) * s + (y - cy) * c) for x, y in pts]
    if desl:
        dx, dy = desl[0], desl[1]
        pts = [(x + dx, y + dy) for x, y in pts]
    return pts


def _caixa(pts):
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def _tocam(a, b, folga):
    return not (a[2] < b[0] - folga or b[2] < a[0] - folga or a[3] < b[1] - folga or b[3] < a[1] - folga)


class _Forma:
    """O polígono posto num estado, com as caixas calculadas uma vez."""

    def __init__(self, nome, pts, prof):
        self.nome, self.pts, self.prof = nome, pts, prof
        self.caixa = _caixa(pts)
        n = len(pts)
        self.lados = [(pts[i], pts[(i + 1) % n]) for i in range(n)]
        self.caixas_lados = [_caixa(l) for l in self.lados]


def _dentro(p, Q):
    x, y, dentro = p[0], p[1], False
    j = len(Q) - 1
    for i in range(len(Q)):
        (xi, yi), (xj, yj) = Q[i], Q[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            dentro = not dentro
        j = i
    return dentro


def _dist_segmento(p, a, b):
    vx, vy = b[0] - a[0], b[1] - a[1]
    l2 = vx * vx + vy * vy
    t = 0.0 if l2 == 0 else max(0.0, min(1.0, ((p[0] - a[0]) * vx + (p[1] - a[1]) * vy) / l2))
    return math.hypot(p[0] - a[0] - t * vx, p[1] - a[1] - t * vy)


def _dist_borda(p, F):
    return min(_dist_segmento(p, a, b) for a, b in F.lados)


def _orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def _segmentos_se_tocam(a, b, c, d):
    """Cruzam ou se tocam (inclusive colineares sobrepostos): o caso em que o lado muda de dentro para fora."""
    o1, o2, o3, o4 = _orient(a, b, c), _orient(a, b, d), _orient(c, d, a), _orient(c, d, b)
    if ((o1 > 0) != (o2 > 0) or o1 == 0 or o2 == 0) and ((o3 > 0) != (o4 > 0) or o3 == 0 or o4 == 0):
        return (min(a[0], b[0]) <= max(c[0], d[0]) and min(c[0], d[0]) <= max(a[0], b[0]) and
                min(a[1], b[1]) <= max(c[1], d[1]) and min(c[1], d[1]) <= max(a[1], b[1]))
    return False


def _fundo_da_borda(A, B, passo, folga):
    """O quanto a borda de A entra em B. Lado sem cruzamento com a borda de B está todo dentro ou todo fora; o de
    dentro só se amostra quando o limite (a distância à borda muda no máximo o quanto se anda) passa do achado."""
    pts = A.pts
    n = len(pts)
    dentro = [_tocam((p[0], p[1], p[0], p[1]), B.caixa, 0.0) and _dentro(p, B.pts) for p in pts]
    dv = [_dist_borda(p, B) if dentro[i] else 0.0 for i, p in enumerate(pts)]
    fundo = max(dv)
    for i, (a, b) in enumerate(A.lados):
        cl = A.caixas_lados[i]
        if not _tocam(cl, B.caixa, folga):
            continue
        j = (i + 1) % n
        cruza = any(_tocam(cl, B.caixas_lados[k], 0.0) and _segmentos_se_tocam(a, b, c, d)
                    for k, (c, d) in enumerate(B.lados))
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        if not cruza:
            if not (dentro[i] and dentro[j]):
                continue                                   # todo fora
            if (dv[i] + dv[j] + L) / 2 <= fundo:
                continue                                   # nenhum ponto do lado passa do que já se achou
        k = max(1, math.ceil(L / passo))
        for s in range(1, k):
            p = (a[0] + (b[0] - a[0]) * s / k, a[1] + (b[1] - a[1]) * s / k)
            if cruza and not _dentro(p, B.pts):
                continue
            fundo = max(fundo, _dist_borda(p, B))
    return fundo


def _espessura_de_dentro(A, B, n):
    """Uma grade de n × n na interseção das caixas: o dobro do afastamento, das duas bordas, do ponto de dentro das
    duas mais fundo. É a espessura da sobreposição: pega as peças coincidentes ou quase, em que a borda de uma mal
    entra na outra (a borda mede o deslocamento, não o quanto as duas ocupam o mesmo lugar)."""
    x0, y0 = max(A.caixa[0], B.caixa[0]), max(A.caixa[1], B.caixa[1])
    x1, y1 = min(A.caixa[2], B.caixa[2]), min(A.caixa[3], B.caixa[3])
    if x1 <= x0 or y1 <= y0:
        return 0.0
    fundo = 0.0
    for i in range(n):
        for j in range(n):
            p = (x0 + (x1 - x0) * (i + 0.5) / n, y0 + (y1 - y0) * (j + 0.5) / n)
            if _dentro(p, A.pts) and _dentro(p, B.pts):
                fundo = max(fundo, 2 * min(_dist_borda(p, A), _dist_borda(p, B)))
    return fundo


def profundidade(A, B, passo, tol=0.0):
    """O fundo: o maior entre o quanto a borda de uma entra na outra e a espessura da sobreposição (a grade de dentro,
    fina quando a borda já acusou ou a grade grossa achou algo, grossa no resto, que é o caso comum do encosto)."""
    if not _tocam(A.caixa, B.caixa, tol):
        return 0.0
    fundo = max(_fundo_da_borda(A, B, passo, tol), _fundo_da_borda(B, A, passo, tol))
    grosso = _espessura_de_dentro(A, B, GRADE_GROSSA)
    if fundo > tol or grosso > tol:
        grosso = max(grosso, _espessura_de_dentro(A, B, GRADE))
    return max(fundo, grosso)


def _faixas_se_cruzam(fa, fb, tz):
    """As faixas de profundidade se cruzam? A de espessura zero é uma camada plana: cruza a outra camada na mesma
    altura (até tz) e a faixa que a tem por dentro, longe das faces; encostada numa face, não. Faixas com espessura
    se cruzam quando se sobrepõem além de tz."""
    if fa is None or fb is None:
        return True
    plana_a, plana_b = fa[1] - fa[0] <= 1e-12, fb[1] - fb[0] <= 1e-12
    if plana_a and plana_b:
        return abs(fa[0] - fb[0]) <= tz
    if plana_a or plana_b:
        z, (lo, hi) = (fa[0], fb) if plana_a else (fb[0], fa)
        margem = min(tz, (hi - lo) / 4)                        # na faixa fina, a margem não engole o meio dela
        return lo + margem < z < hi - margem
    return min(fa[1], fb[1]) - max(fa[0], fb[0]) > tz


def confere(d):
    """Confere todos os estados. Devolve os atravessamentos, os cruzamentos declarados e as contas."""
    tol, tolz, passo, pecas, estados, declarados = _valida(d)
    problemas, vistos = [], {}
    memo = {}  # o par que não se moveu um em relação ao outro dá o mesmo fundo: as peças do mesmo grupo e os grupos parados
    for e in estados:
        postas, chaves = [], []
        for p in pecas:
            g = p["grupo"]
            desl, gira = e["desloca"].get(g), e["gira"].get(g)
            prof = p["profundidade"]
            if prof is not None and desl:
                prof = (prof[0] + desl[2], prof[1] + desl[2])
            postas.append(_Forma(p["nome"], _transforma(p["poligono"], gira, desl), prof))
            chaves.append((gira, desl))
        for i in range(len(postas)):
            for j in range(i + 1, len(postas)):
                A, B = postas[i], postas[j]
                chave = (i, j) + (("junto",) if chaves[i] == chaves[j] else (chaves[i], chaves[j]))
                if chave not in memo:
                    memo[chave] = (profundidade(A, B, passo, tol)
                                   if _tocam(A.caixa, B.caixa, tol) and _faixas_se_cruzam(A.prof, B.prof, tolz) else 0.0)
                fundo = memo[chave]
                if fundo <= tol:
                    continue
                par = frozenset((A.nome, B.nome))
                dec = declarados.get(par)
                if dec and (dec["fundo_max"] is None or fundo <= dec["fundo_max"]):
                    v = vistos.setdefault(par, dict(dec, estados=0, fundo=0.0))
                    v["estados"] += 1
                    v["fundo"] = round(max(v["fundo"], fundo), 4)
                    continue
                problemas.append({"estado": e["rotulo"], "a": A.nome, "b": B.nome, "fundo": round(fundo, 4),
                                  **({"declarado_ate": dec["fundo_max"]} if dec else {})})
    nunca = [dec for par, dec in declarados.items() if par not in vistos
             and not any(frozenset((p["a"], p["b"])) == par for p in problemas)]
    return {"estados": len(estados), "pecas": len(pecas), "tolerancia": tol, "passo": passo,
            "problemas": problemas, "declarados": list(vistos.values()), "declarados_sem_cruzar": nunca}


def _nao_negativo(v):
    n = int(v)
    if n < 0:
        raise argparse.ArgumentTypeError("tem de ser 0 ou mais")
    return n


def main(argv=None):
    ap = argparse.ArgumentParser(description="Confere que nenhuma peça atravessa outra, em cada estado do pecas.json.")
    ap.add_argument("pecas", help="o pecas.json exportado pelo script de geometria da peça")
    ap.add_argument("--json", action="store_true", help="imprime o resultado inteiro em JSON")
    ap.add_argument("--max", type=_nao_negativo, default=40, help="quantos atravessamentos listar (padrão: 40)")
    a = ap.parse_args(argv)
    try:
        with open(a.pecas, encoding="utf-8") as h:
            d = json.load(h)
        r = confere(d)
    except (OSError, ValueError, TypeError, AttributeError, KeyError) as erro:  # nunca a saída 1 por arquivo malformado
        print(f"ERRO: pecas.json inválido: {erro}", file=sys.stderr)
        return 2
    except Exception as erro:  # o resto (um defeito do script) também não é "há atravessamento"
        traceback.print_exc()
        print(f"ERRO: a conferência não chegou ao fim ({type(erro).__name__}: {erro})", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        com = list(dict.fromkeys(p["estado"] for p in r["problemas"]))  # na ordem dos estados
        print(f"{r['pecas']} peças, {r['estados']} estados, tolerância {r['tolerancia']}, passo {r['passo']:g}")
        print(f"atravessamentos: {len(r['problemas'])}, em {len(com)} de {r['estados']} estados")
        for p in r["problemas"][:a.max]:
            extra = f" (declarado até {p['declarado_ate']})" if "declarado_ate" in p else ""
            print(f"  {p['estado']}: '{p['a']}' x '{p['b']}', entra {p['fundo']}{extra}")
        if len(r["problemas"]) > a.max:
            print(f"  (mais {len(r['problemas']) - a.max}; --json para a lista inteira)")
        for c in r["declarados"]:
            print(f"  declarado: {' x '.join(c['pecas'])} ({c['porque']}), cruza em {c['estados']} estados, até {c['fundo']}")
        for c in r["declarados_sem_cruzar"]:
            print(f"  AVISO: o cruzamento declarado {' x '.join(c['pecas'])} não cruza em nenhum estado: confira se ainda vale")
    return 1 if r["problemas"] else 0


if __name__ == "__main__":
    sys.exit(main())
