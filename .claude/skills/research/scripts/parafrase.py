"""Paráfrase colada à fonte: as frases da ficha que espelham frases da fonte, na ordem dela.

Roda antes da revisão, em toda ficha de obra protegida de qualquer ingestão (o Passo 7 da skill `research` e o
material curado pelo ritual de `knowledge/README.md`; `knowledge/sources/README.md`, item 2, e
`references/conferencias.md`, "Conferências automáticas"). A cópia literal se pega por
busca de trecho; aqui se pega a frase da fonte encurtada, com uma palavra trocada aqui e ali.

Como mede: para cada frase da ficha (fora do frontmatter, dos títulos, dos blocos de código e do que está
entre aspas), acha-se a frase da fonte, ou o par de frases vizinhas, com mais palavras de conteúdo em comum,
e mede-se a fração das palavras de conteúdo da frase da ficha que estão nela (`cobertura`). A frase é
"colada" quando a cobertura chega ao limiar; um "trecho colado" é uma sequência de K ou mais frases coladas
seguidas cujas frases da fonte andam para a frente (até `--janela` frases), isto é, a ficha percorrendo a
fonte frase a frase. Quando várias frases da fonte dão a mesma cobertura (a página que repete o mesmo texto
em abas), todas ficam como candidatas e o trecho escolhe a que mantém a ordem; o empate se resolve pela
posição, então o resultado não muda entre execuções. A saída mostra o par medido: a frase da fonte, ou as
duas vizinhas quando a cobertura veio da união delas.

A fonte se corta em blocos antes das frases (a linha em branco, o título, o item de lista, a linha de
tabela; no HTML, as tags de bloco), para o menu, a lista e a tabela não virarem uma frase só; a frase da
fonte com mais de 60 palavras de conteúdo se mede em pedaços de 30, porque uma frase gigante cobriria
qualquer frase da ficha sobre o tema.

O que fica fora da conta:
  - a célula de tabela que só traz um fato (número, nome, comando, licença, valor): fato não é expressão e
    não há outro jeito de escrevê-lo (a régua de `knowledge/sources/README.md`, item 2, "A
    conferência lado a lado"). O script não vê verbo: conta como fato a célula com menos de
    `--palavras-celula` palavras (padrão 8) ou com menos de três palavras funcionais (a lista de nomes e
    versões, por longa que seja), e a primeira linha da tabela (o cabeçalho). A célula com uma lista em
    `<br>` se divide nos itens, e o teste vale para cada um;
  - a frase com menos de 5 palavras de conteúdo, curta demais para medir (contada à parte).

Limites conhecidos: a medida é por palavra, então não pega a troca por sinônimo nem a frase reorganizada com
as mesmas ideias, e não vê tradução (ficha em português de fonte em inglês sai com cobertura baixa mesmo
quando traduz frase a frase; o script avisa quando as línguas diferem). Não substitui a lente de conteúdo
próprio da revisão nem a conferência lado a lado de quem escreve: aponta onde olhar. O limiar e o K se
calibram contra fichas revisadas à mão (0,7 e 3 guiaram a reescrita de fichas de livro, e a re-revisão
ainda achou espelhamento por sinônimos); a calibração está por fazer e pede um gabarito de fichas revisadas à
mão. O teste sem rede, com os casos que têm de reprovar e os que têm de passar com
0,7 e 3: `teste_conferidores.py`, nesta pasta (rodar a cada edição, e de novo quando a calibração mudar os padrões).

  python -X utf8 .claude/skills/research/scripts/parafrase.py --ficha <ficha.md> --fonte <texto.txt>
         [--limiar 0.7] [--k 3] [--janela 12] [--palavras-celula 8] [--saida pasta]

A fonte é texto (`.txt`, `.md`); `.html` tem as tags tiradas; `.pdf` passa pelo `pdftotext` (precisa estar no
PATH; o erro dele aparece). Saída: o resumo e os trechos no stdout; com `--saida`, `<ficha>-parafrase.json` e
`<ficha>-parafrase.md` na pasta. Código de saída: 0 sem trecho colado, 1 com trecho, 2 com erro de entrada (ou
de gravação do `--saida`, ou do próprio script), 3 sem trecho com a ficha em outra língua que a da fonte. A
língua da ficha se mede no corpo dela, fora a seção "Texto integral" (a cópia da fonte com licença que permite,
que está na língua da fonte). Ficha em outra língua: a medida por palavra não vê tradução, então 0 trecho ali
não quer dizer "passou", e por isso o código é 3, não 0; a conferência lado a lado é a conferência. O trecho
que ela achar mesmo assim vale (código 1).

A entrada é uma ficha e uma fonte, sem caminho fixo; as células de fato e as frases curtas saem da conta.
"""
import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

STOP = set("""a o as os um uma uns umas de do da dos das em no na nos nas por pelo pela pelos pelas para pra com sem sob
sobre entre e ou mas nem que se não sim é ser são era foi foram está estão esta este isto esse essa isso aquele aquela
aquilo ele ela eles elas lhe lhes seu sua seus suas meu minha nosso nossa já também muito mais menos como quando onde
porque quem qual quais cada todo toda todos todas outro outra outros outras mesmo mesma há ter tem têm tinha pode podem
deve devem vai vão ao aos à às num numa até depois antes ainda só apenas tão tanto bem
the of and to in is that it for on with as are was were be been by at an or from this these those which who what
when where how not no but if than then so can could would should will may might must do does did has have had its
their there they them we you your our his her he she i me my also into out up about more most such only other some
any all each very just""".split())
PT_FUNC = set("de do da dos das em no na nos nas com para que não uma um os por pelo pela ao se mais como".split())
EN_FUNC = set("the of and to in is that it for on with are was by from this which not".split())


def palavras(t):
    t = unicodedata.normalize("NFC", t.lower())
    return [w for w in re.findall(r"[a-zà-üç]+", t) if w not in STOP and len(w) > 2]


def blocos(t):
    """Os blocos do texto: o parágrafo (linhas seguidas), o título, o item de lista (com a continuação) e a
    linha de tabela. Sem isso, título, lista, célula e menu sem ponto final se fundiam numa frase só (P2)."""
    t = re.sub(r"-[ \t]*\n[ \t]*(?=[a-zà-ü])", "", t)  # palavra hifenizada na quebra de linha
    out, atual = [], []

    def fecha():
        if atual:
            out.append(" ".join(atual))
            atual.clear()
    for l in t.replace("\f", "\n\n").split("\n"):
        s = l.strip()
        if not s:
            fecha()
        elif re.match(r"#{1,6}\s", s) or s.startswith("|"):
            fecha()
            out.append(s)
        elif re.match(r"(?:[-*+•]|\d+[.)])\s", s):
            fecha()
            atual.append(s)
        else:
            atual.append(s)
    fecha()
    return out


def frases(t):
    out = []
    for b in blocos(t):
        b = re.sub(r"\s+", " ", b)
        out += [s.strip() for s in re.split(r"(?<=[.!?;:])\s+(?=[A-ZÀ-Ü\"“(])", b) if len(s.strip()) > 20]
    return out


def pedacos(s, maximo=60, passo=30):
    """A frase da fonte com mais de `maximo` palavras de conteúdo, em pedaços de `passo` (P2)."""
    if len(palavras(s)) <= maximo:
        return [s]
    out, atual, n = [], [], 0
    for w in s.split():
        atual.append(w)
        n += len(palavras(w))
        if n >= passo:
            out.append(" ".join(atual))
            atual, n = [], 0
    if atual:
        out.append(" ".join(atual))
    return out


def lingua(t):
    toks = re.findall(r"[a-zà-üç]+", t.lower())
    pt = sum(1 for w in toks if w in PT_FUNC)
    en = sum(1 for w in toks if w in EN_FUNC)
    return "pt" if pt > en else "en" if en > pt else "?"


def le_fonte(p):
    suf = p.suffix.lower()
    if suf == ".pdf":
        if not shutil.which("pdftotext"):
            raise RuntimeError("pdftotext não está no PATH: extraia o texto da fonte para .txt antes")
        r = subprocess.run(["pdftotext", "-enc", "UTF-8", str(p), "-"], capture_output=True)
        if r.returncode != 0:
            raise RuntimeError(f"pdftotext saiu com {r.returncode} (PDF protegido ou quebrado?): "
                               f"{r.stderr.decode('utf-8', 'replace').strip()[:300]}")
        return r.stdout.decode("utf-8", "replace")
    t = p.read_bytes().decode("utf-8", "replace")
    if suf in (".html", ".htm"):
        t = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", t)
        t = re.sub(r"(?is)<br\s*/?>", "\n", t)
        t = re.sub(r"(?is)</?(?:p|div|li|ul|ol|h[1-6]|tr|td|th|table|thead|tbody|section|article|nav|header|footer|"
                   r"aside|main|blockquote|pre|dd|dt|dl|figure|figcaption|option|button|summary|details)\b[^>]*>",
                   "\n\n", t)
        t = re.sub(r"(?s)<[^>]+>", " ", t)
        t = html.unescape(t)
    return t


def limpa(l):
    l = re.sub(r"[\"“][^\"”]{0,400}[\"”]", " ", l)          # o que está entre aspas é citação
    l = re.sub(r"`[^`]*`", " ", l)                          # termo em código
    l = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", l)          # link: fica o texto
    l = re.sub(r"https?://\S+", " ", l)
    l = re.sub(r"<[^>]+>", " ", l)                           # tag solta (o <br> da célula já virou divisão)
    return re.sub(r"[*_#>]", " ", l)


def linhas_do_integral(texto_ficha):
    """As linhas da seção "Texto integral" da ficha (do título dela ao próximo título do mesmo nível ou acima)."""
    out, nivel = set(), None
    for n, l in enumerate(texto_ficha.split("\n"), start=1):
        m = re.match(r"(#{1,6})\s+(.*)", l.strip())
        if m:
            if nivel is not None and len(m.group(1)) <= nivel:
                nivel = None
            if nivel is None and re.match(r"texto integral\b", m.group(2).strip(), re.I):
                nivel = len(m.group(1))
        if nivel is not None:
            out.add(n)
    return out


def unidades(texto_ficha, palavras_celula):
    """As unidades da ficha que entram na régua: (linha, frase, tipo) e as contagens do que ficou fora."""
    linhas = texto_ficha.split("\n")
    ini = 0
    if linhas and linhas[0].strip() == "---":
        ini = next((i for i in range(1, len(linhas)) if linhas[i].strip() == "---"), -1) + 1
    itens, fora = [], {"celulas_de_fato": 0, "celulas_de_cabecalho": 0, "titulos": 0}
    em_codigo, em_tabela = False, False
    for n, l in enumerate(linhas[ini:], start=ini + 1):
        st = l.strip()
        if st.startswith("```"):
            em_codigo = not em_codigo
            continue
        if em_codigo or not st or st.startswith("<!--"):
            em_tabela = False if not st else em_tabela
            continue
        if st.startswith("#"):
            fora["titulos"] += 1
            em_tabela = False
            continue
        if st.startswith("|"):
            celulas = [c.strip() for c in st.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in celulas if c):
                continue  # a linha que separa o cabeçalho
            if not em_tabela:  # a primeira linha da tabela é o cabeçalho
                em_tabela = True
                fora["celulas_de_cabecalho"] += len(celulas)
                continue
            for c in celulas:
                # a célula com lista em <br> se divide nos itens, e o teste de fato vale para cada um (P4)
                for item in re.split(r"(?i)<br\s*/?>", c):
                    c2 = limpa(item)
                    toks = re.findall(r"\w+", c2.lower())
                    if len(toks) < palavras_celula or sum(1 for w in toks if w in STOP) < 3:
                        fora["celulas_de_fato"] += 1
                        continue
                    for s in frases(c2) or ([c2.strip()] if len(c2.strip()) > 20 else []):
                        itens.append((n, s, "celula"))
            continue
        em_tabela = False
        l2 = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", limpa(l))
        for s in frases(l2) or ([l2.strip()] if len(l2.strip()) > 20 else []):
            itens.append((n, s, "prosa"))
    return itens, fora


MAX_EMPATES = 50


def alinha(itens, fs, ws, inv):
    """Para cada unidade da ficha, a melhor cobertura e todos os pares (a, b) da fonte que a dão: a frase a
    (a == b) ou a união das vizinhas a e b. O empate se resolve pela posição, nunca pela ordem de um set (P1)."""
    al, curtas = [], 0
    n_fs = len(ws)
    for n, s, tipo in itens:
        w = set(palavras(s))
        if len(w) < 5:
            curtas += 1
            continue
        cand = defaultdict(int)
        for x in w:
            for i in inv.get(x, ()):
                cand[i] += 1
        melhor, empates = 0, set()
        for i, _ in sorted(cand.items(), key=lambda kv: (-kv[1], kv[0]))[:40]:
            pares = [(i, i)] + ([(i, i + 1)] if i + 1 < n_fs else []) + ([(i - 1, i)] if i else [])
            for a, b in pares:
                comum = len(w & (ws[a] | ws[b]))  # inteiro: a comparação não depende de arredondamento
                if comum > melhor:
                    melhor, empates = comum, {(a, b)}
                elif comum == melhor and comum:
                    empates.add((a, b))
        # a união que empata com uma das duas frases sozinha não acrescenta nada: fica a frase
        sos = {a for a, b in empates if a == b}
        emp = sorted(p for p in empates if p[0] == p[1] or not ({p[0], p[1]} & sos))[:MAX_EMPATES]
        al.append({"linha": n, "tipo": tipo, "frase": s, "cobertura": round(melhor / len(w), 3),
                   "fontes": [list(p) for p in emp], "fonte": list(emp[0]) if emp else None})
    return al, curtas


def texto_fonte(fs, par):
    a, b = par
    return fs[a] if a == b else f"{fs[a]} / {fs[b]}"


def trechos(al, limiar, k, janela, fs):
    """Sequências de K ou mais coladas seguidas cuja posição na fonte anda para a frente (até `janela`). Entre
    as candidatas empatadas de cada unidade, a que mantém a ordem; recomeça no elemento que quebrou a ordem."""
    col = [x["cobertura"] >= limiar for x in al]
    out, i = [], 0
    while i < len(al):
        if not col[i] or not al[i]["fontes"]:
            i += 1
            continue
        cadeia = None
        for c0 in al[i]["fontes"]:
            c = [tuple(c0)]
            j = i + 1
            while j < len(al) and col[j] and al[j]["fontes"]:
                ant = c[-1][0]
                ok = [tuple(x) for x in al[j]["fontes"] if 0 <= x[0] - ant <= janela]
                if not ok:
                    break
                c.append(min(ok, key=lambda x: (x[0] - ant, x[1] - x[0])))
                j += 1
            if cadeia is None or len(c) > len(cadeia):
                cadeia = c
        j = i + len(cadeia)
        for t, par in zip(range(i, j), cadeia):
            al[t]["fonte"] = list(par)
        if j - i >= k:
            out.append({"linhas": sorted({al[t]["linha"] for t in range(i, j)}),
                        "pares": [{"ficha": al[t]["frase"][:240], "fonte": texto_fonte(fs, al[t]["fonte"])[:480],
                                   "frases_da_fonte": al[t]["fonte"], "cobertura": al[t]["cobertura"]}
                                  for t in range(i, j)]})
        i = j
    return out, col


def principal():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ficha", required=True, help="a ficha (knowledge/sources/AAAA-MM-DD-<slug>.md)")
    ap.add_argument("--fonte", required=True, help="o texto da fonte (.txt, .md, .html ou .pdf)")
    ap.add_argument("--limiar", type=float, default=0.7, help="cobertura a partir da qual a frase é colada")
    ap.add_argument("--k", type=int, default=3, help="coladas seguidas que fazem um trecho")
    ap.add_argument("--janela", type=int, default=12, help="quanto a fonte pode andar entre duas coladas")
    ap.add_argument("--palavras-celula", type=int, default=8, help="abaixo disso, a célula conta como fato")
    ap.add_argument("--saida", help="pasta para o JSON e o markdown do resultado")
    a = ap.parse_args()

    ficha, fonte = Path(a.ficha), Path(a.fonte)
    try:
        tf = ficha.read_bytes().decode("utf-8")
        tx = le_fonte(fonte)
    except (OSError, UnicodeDecodeError, RuntimeError) as e:
        print(f"erro de entrada: {e}", file=sys.stderr)
        return 2
    fs, longas = [], 0
    for s in frases(tx):
        p = pedacos(s)
        longas += len(p) > 1
        fs.extend(p)
    if not fs:
        print("a fonte não tem frases para comparar (texto vazio?)", file=sys.stderr)
        return 2
    ws = [set(palavras(s)) for s in fs]
    inv = defaultdict(set)
    for i, w in enumerate(ws):
        for x in w:
            inv[x].add(i)

    itens, fora = unidades(tf, a.palavras_celula)
    al, curtas = alinha(itens, fs, ws, inv)
    tr, col = trechos(al, a.limiar, a.k, a.janela, fs)
    integral = linhas_do_integral(tf)
    lf = lingua(" ".join(s for n, s, _ in itens if n not in integral))  # a língua do corpo, fora o integral
    lx = lingua(tx[:20000])
    outra_lingua = lf != lx and "?" not in (lf, lx)
    res = {
        "ficha": str(ficha), "fonte": str(fonte), "limiar": a.limiar, "k": a.k, "janela": a.janela,
        "frases_da_fonte": len(fs), "frases_da_fonte_longas_em_pedacos": longas, "unidades_medidas": len(al),
        "prosa": sum(1 for x in al if x["tipo"] == "prosa"), "celulas_com_texto": sum(1 for x in al if x["tipo"] == "celula"),
        "curtas_fora_da_conta": curtas, **fora,
        "coladas": sum(col), "frac_coladas": round(sum(col) / max(1, len(al)), 3),
        "lingua_ficha": lf, "lingua_fonte": lx, "linhas_do_texto_integral_fora_da_lingua": len(integral),
        "trechos": tr,
        "linhas_coladas": sorted({x["linha"] for x, c in zip(al, col) if c}),
        "unidades": al,
    }

    L = [f"Paráfrase colada: {ficha.name} contra {fonte.name}",
         f"limiar {a.limiar}, K {a.k}, janela {a.janela}; fonte com {len(fs)} frases"
         + (f" ({longas} frase(s) com mais de 60 palavras de conteúdo, medidas em pedaços de 30)" if longas else ""),
         f"unidades medidas: {len(al)} ({res['prosa']} de prosa, {res['celulas_com_texto']} de célula com texto); "
         f"fora da conta: {fora['celulas_de_fato']} células (ou itens de célula em <br>) de fato, "
         f"{fora['celulas_de_cabecalho']} de cabeçalho, "
         f"{curtas} frases curtas demais para medir",
         f"coladas: {sum(col)} de {len(al)} ({res['frac_coladas'] * 100:.0f}%); trechos de {a.k} ou mais seguidas: {len(tr)}"]
    if outra_lingua:
        L.append(f"AVISO: ficha em '{lf}' (medida no corpo, fora o \"Texto integral\") e fonte em '{lx}': a medida "
                 "por palavra não vê tradução, então a parte traduzida não foi medida. "
                 + ("Os trechos abaixo valem; o resto, só a conferência lado a lado." if tr else
                    "0 trecho aqui não é \"passou\": o script sai com o código 3, não 0, e a conferência lado a lado "
                    "de quem escreve é a conferência."))
    L.append("Limite: não pega troca por sinônimo nem tradução; a lente de conteúdo próprio da revisão continua.")
    for t in tr:
        L.append("")
        L.append(f"Trecho colado, linhas {', '.join(map(str, t['linhas']))}:")
        for p in t["pares"]:
            L.append(f"  [{p['cobertura']:.2f}] ficha: {p['ficha']}")
            L.append(f"         fonte: {p['fonte']}")
    soltas = [x for x, c in zip(al, col) if c and x["linha"] not in {l for t in tr for l in t["linhas"]}]
    if soltas:
        L.append("")
        L.append(f"Coladas fora de trecho ({len(soltas)}): linhas {', '.join(str(x['linha']) for x in soltas)}")
    saida = "\n".join(L)
    print(saida)

    if a.saida:
        try:
            out = Path(a.saida)
            out.mkdir(parents=True, exist_ok=True)
            (out / f"{ficha.stem}-parafrase.json").write_bytes(
                (json.dumps(res, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))
            (out / f"{ficha.stem}-parafrase.md").write_bytes((saida + "\n").encode("utf-8"))
        except OSError as e:
            print(f"erro ao gravar em --saida: {e}", file=sys.stderr)
            return 2
    return 1 if tr else (3 if outra_lingua else 0)


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except Exception as e:  # erro do script não sai com o código de trecho (1)
        print(f"erro do script: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(2)
