"""Conta as citações literais das fichas de obra protegida em `knowledge/sources/` (régua: até três, de até umas 25
palavras cada; `knowledge/sources/README.md`, "A ficha de estudo" e o item 2 de "Conteúdo de terceiros").

  python -X utf8 .claude/skills/research/scripts/conta_citacoes.py            # fichas com mais de três
  python -X utf8 .claude/skills/research/scripts/conta_citacoes.py --json
  python -X utf8 .claude/skills/research/scripts/conta_citacoes.py --todas   # todas as protegidas, com a conta
  python -X utf8 .claude/skills/research/scripts/conta_citacoes.py --ficha <arquivo.md> [...]  # só estas
  python -X utf8 .claude/skills/research/scripts/conta_citacoes.py --mostra --ficha <arquivo.md>  # os trechos

Ficha protegida: o campo `licenca` do frontmatter não é livre. Livre (o integral pode entrar) é Creative Commons sem
a cláusula NC (BY, BY-SA, BY-ND, CC0), MIT, Apache, BSD, GPL, domínio público e obra do governo dos EUA, e o campo
que diz que o integral está no arquivo. A palavra de quem gravou vem antes do nome da licença: o campo que começa por
"protegido" ou "em dúvida", ou diz "só a ficha" ou "sem o integral", é protegido mesmo citando CC0 de outra coisa (os
assets de um site, o código de um repositório), e a licença negada na mesma frase ("sem licença Creative Commons") não
conta. A ficha sem o campo (o campo existe desde 2026-10-28) conta como protegida e sai marcada `licenca ausente`.
O material pago (item 3 da régua: a ficha cuja licença diz curso pago ou material pago, que segue a regra própria
daquele item, sem o teto de três) fica fora da conta, salvo com `--com-pago` ou `--ficha`.

Citação: trecho entre aspas (retas, curvas ou «») de pelo menos 6 palavras, ou bloco `>` (linhas seguidas, juntas)
de pelo menos 6 palavras. Fica fora:
  - o frontmatter, a seção "Texto integral", as seções de referências ou bibliografia, os títulos (`#`), os blocos e
    trechos de código, o texto de link (`[...]`) e o parágrafo da conferência lado a lado (fala da própria ficha);
  - o título de obra: em itálico (`*"..."*`), logo depois de um ano ("Wang et al. 2023 (", "Berry, 2023, "), logo
    depois de uma palavra que anuncia título ou parte de obra ("título", "artigo", "livro", "capítulo", "seção",
    "anexo", "tabela", "post", "vídeo"...) sem verbo de dizer no meio ("o artigo diz que" é citação), e o trecho igual
    a um título de seção da própria ficha ou aos nomes de seção do padrão ("O que a fonte recomenda");
  - o exemplo e o termo: logo depois de "exemplo", "prompt", "pergunta", "pedido", "comando", "descrição",
    "entrada", "saída" (exemplo de prompt ou de dado) e de "chama de", "chamado de", "nome de" (termo técnico);
  - a tradução entre aspas: o trecho em português numa ficha cuja fonte é de outra língua (a régua pede a citação
    na língua da fonte; o trecho em português ali é tradução, exemplo ou rótulo, e sai à parte, em `traduzidas`).
    A língua da fonte se infere das próprias aspas contadas: estrangeira com duas ou mais em outra língua, ou com
    uma e até duas em português (assim a regra não vira quando a reescrita tira as citações em inglês e sobram as
    traduções).
Onde erra (calibrado à mão em 19/11/2026): `licoes.md` da `research`, a entrada do `conta_citacoes.py`.

Código de saída: 0 sem ficha acima de três, 1 com alguma.
O teste sem rede: `teste_conta_citacoes.py`, nesta pasta.
"""
import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
FONTES = RAIZ / "knowledge" / "sources"
MIN_PALAVRAS = 6
LIMITE = 3

# --- licença -------------------------------------------------------------------------------------------------------
LIVRE = re.compile(
    r"\bCC[\s-]?BY\b|\bCC0\b|creative commons attribution|creative commons atribui|\bMIT\b|\bApache\b|\bBSD\b|"
    r"\bGPL\b|dom[ií]nio p[uú]blico|public domain|governo (?:federal )?dos EUA|U\.S\.C\.|\bobra do governo",
    re.I,
)
NC = re.compile(r"\bNC\b|n[aã]o[- ]?comercial|noncommercial|non-commercial", re.I)
PRIMEIRA_CC = re.compile(r"\bCC[\s-]?(?:BY|IGO)|creative commons", re.I)
INTEGRAL_AQUI = re.compile(
    r"integra(?:l|is) (?:abaixo|embaixo|com atribui|no mesmo arquivo)|integral\b[^;]{0,30}\b(?:embaixo|ao fim)", re.I)
SEM_INTEGRAL = re.compile(r"sem o integral|integral retirad|integral est[aá] na url|integral fica na url", re.I)
PROTEGIDO = re.compile(
    r"s[oó] (?:a )?ficha|sem o integral|tratad[oa] como protegid|protegid|todos os direitos reservados|"
    r"all rights reserved|sem licen[cç]a aberta|n[aã]o declara(?:m)? licen|sem licen[cç]a declarada|em d[uú]vida",
    re.I,
)
PAGO = re.compile(r"curso pago|material pago|sources/archive", re.I)
SEM_DIREITO = re.compile(
    r"sem direito autoral|sem copyright|n[aã]o (?:s[aã]o|é) objeto de prote|n[aã]o protegid[oa] por direito|ato oficial",
    re.I)
NEGA = re.compile(r"\b(?:sem|n[aã]o|nenhuma?)\b[^.;,)]{0,40}$", re.I)


def eh_livre(licenca):
    if not licenca:
        return False
    cc = PRIMEIRA_CC.search(licenca)
    nc = NC.search(licenca[cc.start(): cc.start() + 70]) if cc else NC.search(licenca)
    if nc and not (cc and LIVRE.search(licenca[: cc.start()])):
        return False  # a NC vale para a primeira licença Creative Commons dita, não para a de outra versão
    if re.match(r"\W*(?:protegid|em d[uú]vida)", licenca, re.I):
        return False
    if INTEGRAL_AQUI.search(licenca) and not SEM_INTEGRAL.search(licenca):
        return True
    if SEM_DIREITO.search(licenca):
        return True
    if PROTEGIDO.search(licenca):
        return False
    for m in LIVRE.finditer(licenca):
        if not NEGA.search(licenca[: m.start()][-60:]):
            return True
    return False


# --- citação -------------------------------------------------------------------------------------------------------
ASPAS = re.compile(r'"([^"\n]+)"|“([^”\n]+)”|«([^»\n]+)»')
TITULO_ANTES = re.compile(
    r"\b(?:t[ií]tulos?|artigos?|livros?|cap[ií]tulos?|se[cç](?:[aã]o|[oõ]es)|anexos?|partes?|tabelas?|figuras?|"
    r"posts?|v[ií]deos?|epis[oó]dios?|palestras?|cursos?|aulas?|m[oó]dulos?|s[eé]ries?|intitulad[oa]s?|manchetes?|"
    r"ensaios?|papers?|t[oó]picos?|p[aá]ginas?|obras?|filmes?|romances?|contos?|poemas?|reportagens?|mat[eé]rias?|"
    r"slides?|telas?|lemas?|slogans?|epígrafe|guias?|document[aá]rios?|manuais|subt[ií]tulo|cabe[cç]alho)\b",
    re.I,
)
EXEMPLO_ANTES = re.compile(
    r"(?:\bex\.:?|\b(?:exemplos?|por exemplo|prompts?|perguntas?|pedidos?|pede|comandos?|descri[cç][aã]o|entradas?|"
    r"sa[ií]das?|erros?|avisos? de erro|consultas?|queries|query|tarefas?|instru[cç](?:[aã]o|[oõ]es)|mensagens?|frases? de teste|"
    r"modelos? de frase|template)\b)",
    re.I,
)
TERMO_ANTES = re.compile(
    r"\b(?:chama[mr]?|chamou|chamam|chamad[oa]s?|batiz\w*|denomin\w*|apelid\w*|nome|r[oó]tulo|termo|express[aã]o|"
    r"conceito|categoria|etiqueta|selo|campo)\s*(?:de|como)?\s*[:(]?\s*$",
    re.I,
)
ANO_ANTES = re.compile(r"(?:\[\d+\]|\b(?:1[5-9]|20)\d\d[a-z]?\)?|et al\.)\s*[,:;(]?\s*\(?\s*$", re.I)
DIZER = re.compile(
    r"\b(?:diz|dizem|disse|afirma\w*|escrev\w*|conclu\w*|resum\w*|lembra\w*|explica\w*|defin\w*|cita\w*|"
    r"responde\w*|observa\w*|avisa\w*|admite\w*|garante\w*|defende\w*|argument\w*|prop[oõ]e\w*|sugere\w*|mostra\w*|"
    r"repete\w*|insiste\w*|reconhece\w*|acrescenta\w*|declara\w*|alerta\w*|nota|notam|que|abre|fecha|traz|resume|"
    r"chama|chamam|ensina\w*|recomenda\w*|pergunta|pede)\b",
    re.I,
)
SECOES_PADRAO = {
    "o que a fonte recomenda", "o que a fonte afirma", "tudo o mais que ensina", "em uma frase", "lacuna",
    "o que a fonte não diz", "a estrutura da fala", "as regras ensinadas", "regras ensinadas",
}
SECAO_FORA = re.compile(r"^#{1,6}\s+(?:refer[eê]ncias|bibliografia|leituras|trabalhos relacionados|links)", re.I)
CONFERENCIA = re.compile(r"^\**\s*(?:a\s+)?confer[eê]ncia lado a lado", re.I)
PROVENIENCIA = re.compile(r"^[-*\s]*(?:proveni[eê]ncia|cobertura|fonte e p[aá]ginas|licen[cç]a|t[ií]tulos? conferid[oa]s?)\b", re.I)

PT = {"de", "que", "não", "o", "os", "as", "um", "uma", "é", "para", "com", "se", "do", "da", "dos", "das", "em",
      "no", "na", "nos", "nas", "ao", "à", "mais", "como", "mas", "por", "isso", "ele", "ela", "você", "são", "foi",
      "tem", "sem", "seu", "sua", "também", "já", "muito", "quando", "ou", "então", "pelo", "pela", "eu", "há"}
EN = {"could", "would", "should", "there", "been", "were", "all", "my", "me", "the", "of", "and", "to", "is", "that", "for", "with", "are", "in", "be", "it", "not", "on", "this", "as", "by",
      "an", "or", "we", "you", "can", "they", "what", "from", "at", "was", "have", "has", "will", "your", "our", "if",
      "but", "more", "than", "it's", "i", "their", "which", "about", "how", "when", "do", "does", "into"}
OUTRA = {"el", "la", "los", "las", "del", "y", "es", "una", "le", "les", "des", "et", "est", "du", "une", "pour", "der",
         "die", "das", "und", "ist", "nicht", "mit", "per", "che", "il", "di", "lo", "gli", "con"}


def lingua(trecho):
    ws = re.findall(r"[\wçãõáéíóúâêôàü'’]+", trecho.lower())
    pt = sum(w in PT for w in ws)
    en = sum(w in EN for w in ws)
    ou = sum(w in OUTRA for w in ws)
    if pt >= en and pt >= ou and pt > 0:
        return "pt"
    if en == 0 and ou == 0:
        return "pt"  # sem palavra funcional: trata como da ficha
    return "en" if en >= ou else "outra"


def frontmatter(texto):
    """Devolve (campos simples, índice da primeira linha do corpo)."""
    linhas = texto.split("\n")
    if not linhas or linhas[0].strip() != "---":
        return {}, 0
    campos = {}
    fim_dos_campos = 1
    for i in range(1, len(linhas)):
        if linhas[i].strip() == "---":
            return campos, i + 1
        m = re.match(r"^(\w+):\s*(.*)$", linhas[i])
        if m:
            v = m.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            campos[m.group(1)] = v
            fim_dos_campos = i + 1
    # frontmatter sem o "---" de fechamento: vale o que se leu como campo, e o corpo começa depois do último campo,
    # para o texto dos campos não ser contado como citação
    return campos, fim_dos_campos


def palavras(s):
    """Palavras com letra: "From 16.06 till 24.06" tem duas."""
    return len([w for w in re.findall(r"\w+(?:[-'’]\w+)*", s) if re.search(r"[^\W\d_]", w)])


def limpa_linha(s):
    """Tira o código e o texto de link, que não são citação, mantendo o tamanho da linha."""
    s = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), s)
    s = re.sub(r"!?\[[^\]]*\]\([^)]*\)", lambda m: " " * len(m.group(0)), s)
    s = re.sub(r"\[\[[^\]]*\]\]", lambda m: " " * len(m.group(0)), s)
    return s


def normaliza(s):
    return re.sub(r"[\s*_:.?!]+", " ", s).strip().casefold()


def anunciado(antes):
    """O trecho vem logo depois de algo que diz que ele é título, exemplo ou termo?"""
    janela = antes[-70:]
    if ANO_ANTES.search(janela):
        return "titulo"
    if TERMO_ANTES.search(janela):
        return "termo"
    for rx, classe in ((EXEMPLO_ANTES, "exemplo"), (TITULO_ANTES, "titulo")):
        ultimo = None
        for m in rx.finditer(janela):
            ultimo = m
        if ultimo is None:
            continue
        meio = janela[ultimo.end():]
        if len(meio) <= 45 and not DIZER.search(meio) and not re.search(r"[.;]\s", meio):
            return classe
    return None


def candidatos(texto):
    """Todos os trechos com 6 palavras ou mais, com a classe: cita, ou o motivo de ficar fora."""
    _, ini = frontmatter(texto)
    linhas = texto.split("\n")
    secoes = {normaliza(re.sub(r"^#{1,6}\s+", "", l.strip())) for l in linhas if re.match(r"^#{1,6}\s", l.strip())}
    secoes |= {normaliza(m) for m in re.findall(r"^\*\*([^*]{3,80})\*\*", texto, re.M)}
    secoes |= SECOES_PADRAO
    achados = []
    em_codigo = False
    fora = False
    bloco = None  # [linha inicial, texto]

    def fecha_bloco():
        if bloco is not None and palavras(bloco[1]) >= MIN_PALAVRAS:
            achados.append([bloco[0], palavras(bloco[1]), bloco[1].strip(), "fora" if fora else "cita", "bloco"])

    for n in range(ini, len(linhas)):
        bruta = linhas[n].rstrip("\r")
        tira = bruta.strip()
        if tira.startswith("```") or tira.startswith("~~~"):
            em_codigo = not em_codigo
            continue
        if em_codigo:
            continue
        if re.match(r"^#{1,6}\s", tira):
            fecha_bloco()
            bloco = None
            if re.match(r"^#{1,6}\s+texto integral", tira, re.I):
                break
            fora = bool(SECAO_FORA.match(tira))
            continue
        if tira.startswith(">"):
            conteudo = limpa_linha(tira.lstrip(">").strip())
            if bloco is None:
                bloco = [n + 1, conteudo]
            else:
                bloco[1] += " " + conteudo
            continue
        fecha_bloco()
        bloco = None
        if bruta.startswith("    ") and not tira.startswith(("-", "*", "|", "+")) and not re.match(r"\d+[.)]", tira):
            continue  # bloco de código por recuo
        linha = limpa_linha(bruta)
        conferencia = bool(CONFERENCIA.match(tira))
        proveniencia = bool(PROVENIENCIA.match(tira))
        anterior = None  # (fim, classe) do trecho anterior na linha: o da lista "a"; "b" herda a classe
        for m in ASPAS.finditer(linha):
            trecho = next(g for g in m.groups() if g is not None)
            np = palavras(trecho)
            if np < MIN_PALAVRAS:
                continue
            antes, depois = linha[: m.start()], linha[m.end():]
            if fora or conferencia:
                classe = "fora"
            elif proveniencia:
                classe = "proven"  # o título da página, o aviso de licença, a âncora da cobertura
            elif re.search(r"[*_]\s*$", antes) and re.match(r"^\s*[*_]", depois):
                classe = "titulo"  # em itálico
            elif normaliza(trecho) in secoes:
                classe = "secao"
            elif anterior and anterior[1] != "cita" and re.fullmatch(r"[\s,;/]*(?:e|ou|and|or)?[\s,;/]*",
                                                                         linha[anterior[0]: m.start()]):
                classe = anterior[1]
            else:
                classe = anunciado(antes) or "cita"
            anterior = (m.end(), classe)
            achados.append([n + 1, np, trecho, classe, "aspas"])
    fecha_bloco()
    # a mesma citação repetida na ficha conta uma vez
    # (e o trecho contido noutro: "keep the AI on the leash" dentro de "we have to keep the AI on the leash")
    cita = [a for a in achados if a[3] == "cita"]
    for i, a in enumerate(cita):
        ka = normaliza(a[2])
        for j, b in enumerate(cita):
            if i == j or b[3] != "cita":
                continue
            kb = normaliza(b[2])
            if ka in kb and (ka != kb or j < i):
                a[3] = "repetida"
                break
    # tradução: trecho em português numa ficha de fonte em outra língua
    cita = [a for a in achados if a[3] == "cita"]
    ling = [lingua(a[2]) for a in cita]
    pt = ling.count("pt")
    est = len(ling) - pt
    if est >= 2 or (est == 1 and pt <= 2):
        for a, l in zip(cita, ling):
            if l == "pt":
                a[3] = "traduzida"
    return achados


def citacoes(texto):
    """Lista de (linha, palavras, trecho) das citações do corpo da ficha."""
    return [(a[0], a[1], a[2][:120]) for a in candidatos(texto) if a[3] == "cita"]


def mede(caminho, todos=False):
    texto = Path(caminho).read_text(encoding="utf-8", errors="replace")
    campos, _ = frontmatter(texto)
    lic = campos.get("licenca") or None  # o campo vazio conta como ausente
    if eh_livre(lic):
        return None
    cand = candidatos(texto)
    cits = [a for a in cand if a[3] == "cita"]
    r = {
        "ficha": Path(caminho).as_posix(),
        "licenca": lic if lic is not None else "ausente",
        "pago": bool(lic and PAGO.search(lic)),
        "citacoes": len(cits),
        "longas": sum(1 for c in cits if c[1] > 25),
        "traduzidas": sum(1 for a in cand if a[3] == "traduzida"),
        "linhas": [{"linha": c[0], "palavras": c[1], "trecho": c[2][:120]} for c in cits],
    }
    if todos:
        r["fora"] = [{"linha": a[0], "classe": a[3], "trecho": a[2][:120]} for a in cand if a[3] != "cita"]
    return r


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--todas", action="store_true", help="lista todas as protegidas, não só as acima de três")
    ap.add_argument("--mostra", action="store_true", help="mostra os trechos, os contados e os que ficaram fora")
    ap.add_argument("--ficha", nargs="+", help="só estas fichas")
    ap.add_argument("--com-pago", action="store_true",
                    help="conta também o material pago (item 3 da régua)")
    a = ap.parse_args(argv)
    arquivos = [Path(f) for f in a.ficha] if a.ficha else sorted(FONTES.glob("*.md"))
    arquivos = [f for f in arquivos if f.name != "README.md"]
    medidas = [m for m in (mede(f, a.mostra) for f in arquivos) if m is not None]
    if not (a.com_pago or a.ficha):
        medidas = [m for m in medidas if not m["pago"]]
    acima = [m for m in medidas if m["citacoes"] > LIMITE]
    saida = medidas if (a.todas or a.ficha) else acima
    if a.json:
        print(json.dumps({"protegidas": len(medidas), "acima": len(acima), "fichas": saida}, ensure_ascii=False,
                         indent=1))
    else:
        for m in saida:
            nome = m["ficha"].rsplit("/", 1)[-1]
            marca = " (licenca ausente)" if m["licenca"] == "ausente" else ""
            longas = f", {m['longas']} longas" if m["longas"] else ""
            print(f"{m['citacoes']:3d}{longas}  {nome}{marca}  linhas {', '.join(str(c['linha']) for c in m['linhas'])}")
            if a.mostra:
                for c in m["linhas"]:
                    print(f"      cita  {c['linha']:4d} ({c['palavras']}) {c['trecho']}")
                for c in m["fora"]:
                    print(f"      {c['classe']:<5} {c['linha']:4d} {c['trecho']}")
        sem = sum(1 for m in acima if m["licenca"] == "ausente")
        print(f"\n{len(medidas)} fichas protegidas; {len(acima)} com mais de {LIMITE} citações"
              f" ({sem} sem o campo licenca).")
    return 1 if acima else 0


if __name__ == "__main__":
    sys.exit(main())
