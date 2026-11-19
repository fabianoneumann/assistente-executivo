"""Confere a escaleta da piece-script contra a tabela do contrato (references/contrato.md), pelos rótulos em negrito.

Uso: python -X utf8 confere_contrato.py <escaleta.md> [...] [--json]

O que confere (cada achado com código estável):
- CT-NIVEL      o **Nível:** ausente da cabeça ou sem N1/N2 (sem ele, nada mais se confere). A cabeça é o que vem antes
                da primeira unidade; os campos dela só se procuram ali;
- CT-AUSENTE    campo do nível (cabeça, unidade ou pé) que não aparece;
- CT-SUMIU      campo fora do nível, ou condicional sem a condição, que sumiu em vez de sair com "não se aplica, porque…";
- CT-VAZIO      campo do nível vazio, "a definir" ou tabela só com o cabeçalho;
- CT-NSA-MOTIVO "não se aplica" sem o motivo ("porque", "pelo mesmo motivo", ou o motivo depois de vírgula ou ponto e vírgula);
- CT-NSA-DENTRO "não se aplica" num campo obrigatório do nível (não condicional); o **Critério de escolha** é obrigatório
                no N2 dos Stories de véspera ("véspera" no **Nível** ou no **Objetivo**);
- CT-PROMETE    no N2, unidade sem **Promete** ou sem **Paga em** em rótulo próprio (o rótulo combinado não conta), ou
                unidade que promete e deixa o **Paga em** em "não se aplica" (o pagamento noutra peça se nomeia);
- CT-FONTE      **Fonte** sem sigla da lista "Fontes, por sigla" nem caminho em knowledge/sources/ (no N1, a resposta
                pelo número ou pelo tema também vale, references/stories.md);
- CT-ESCOLHIDO  ponto dos **Não escolhidos** sem destino: a unidade de destino (a tela, o Story, a unidade, pelo número ou
                pela função), o ângulo da peça, ou "fica fora"/"não se aplica" com o porquê; a seta é opcional;
- AV-LINHA      (aviso) sigla na **Fonte** sem o número da linha;
- AV-FICHA      (aviso) **Fonte** cujas siglas não apontam nenhuma ficha que exista em knowledge/sources/ (a sigla de
                rascunho, mesa ou síntese não é ficha; o script não abre a ficha para ver o trecho);
- AV-ROTULO     (aviso) rótulo fora da grafia do contrato que o script aceitou (hoje, "Fontes" no lugar de "Fonte").
Sai com 1 se houver ERRO (CT-*), 0 se só avisos ou nada. Sem rede. Lê um arquivo só: o pé dividido em outro arquivo
não é lido.
"""
import json
import re
import sys
from pathlib import Path

CABECA = ["Nível", "Realidade da peça", "Objetivo", "Regras conferidas", "Critério de escolha", "Story line",
          "Fecho", "Em jogo", "Padrão de ordem"]
UNIDADE = ["Função", "Diz", "Fonte", "Aparece", "Puxa a próxima", "Valor", "Promete", "Paga em"]
PE = ["Plantas e pagamentos", "Não escolhidos", "Representação", "Exemplos", "Enriquecimento", "Ironia",
      "Para ir além", "Riscos"]
TODOS = CABECA + UNIDADE + PE

# por nível: "sim" (obrigatório), "fora" (sai com o não se aplica) e "cond" (preenchido ou não se aplica com motivo)
REGRA = {
    "N1": {"Nível": "sim", "Realidade da peça": "sim", "Objetivo": "sim", "Regras conferidas": "sim",
           "Critério de escolha": "sim", "Story line": "fora", "Fecho": "sim", "Em jogo": "fora",
           "Padrão de ordem": "fora", "Função": "sim", "Diz": "sim", "Fonte": "sim", "Aparece": "sim",
           "Puxa a próxima": "sim", "Valor": "fora", "Promete": "cond", "Paga em": "cond",
           "Plantas e pagamentos": "cond", "Não escolhidos": "fora", "Representação": "cond", "Exemplos": "fora",
           "Enriquecimento": "fora", "Ironia": "cond", "Para ir além": "fora", "Riscos": "sim"},
    "N2": {"Nível": "sim", "Realidade da peça": "sim", "Objetivo": "sim", "Regras conferidas": "sim",
           "Critério de escolha": "cond", "Story line": "sim", "Fecho": "sim", "Em jogo": "sim",
           "Padrão de ordem": "sim", "Função": "sim", "Diz": "sim", "Fonte": "sim", "Aparece": "sim",
           "Puxa a próxima": "sim", "Valor": "sim", "Promete": "sim", "Paga em": "sim",
           "Plantas e pagamentos": "sim", "Não escolhidos": "cond", "Representação": "cond", "Exemplos": "cond",
           "Enriquecimento": "sim", "Ironia": "cond", "Para ir além": "sim", "Riscos": "sim"},
}
# variantes de rótulo que as escaletas reais usam para o mesmo campo: aceitas, com o AV-ROTULO
SINONIMOS = {"Fonte": ["Fontes"]}

NSA = re.compile(r"^\W*n[ãa]o se aplica", re.I)
MOTIVO = re.compile(r"porque|pelo mesmo motivo|[;,:.]\s*\S", re.I)
A_DEFINIR = re.compile(r"^\W*a definir", re.I)
CAB_UNIDADE = re.compile(r"^#{2,4}\s+(Telas?|Story|Stories|Unidade|Bloco|Cena)\b[^\n]*", re.I)
CAB_SECAO = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
ITEM = re.compile(r"^\s*[-*]\s")


def rotulos(rotulo):
    return [rotulo] + SINONIMOS.get(rotulo, [])


def _negrito(nome):
    return re.compile(r"^\s*(?:[-*]\s+)?\*\*" + re.escape(nome) + r"\s*:?\s*\*\*\s*(?:\([^)]*\))?\s*:?\s*(.*)$", re.I)


ROTULO_CONHECIDO = [_negrito(n) for r in TODOS for n in rotulos(r)]


def _e_rotulo(ln):
    return ln.lstrip().startswith("#") or any(p.match(ln) for p in ROTULO_CONHECIDO)


def _junta(linhas, i):
    """O valor que segue um rótulo vazio: as linhas seguintes, com a quebra, até o próximo rótulo conhecido, um
    cabeçalho, ou uma linha em branco que não leva a mais um item de lista."""
    corpo = []
    for j in range(i + 1, len(linhas)):
        x = linhas[j]
        if _e_rotulo(x):
            break
        if not x.strip():
            if not corpo:
                continue
            prox = next((y for y in linhas[j + 1:] if y.strip()), "")
            if ITEM.match(prox) and not _e_rotulo(prox):
                continue
            break
        corpo.append(x)
    return "\n".join(corpo).strip()


def acha(linhas, rotulo, ini=0, fim=None):
    """Valor do campo entre as linhas ini e fim: '**Rótulo:** valor', '**Rótulo** (…): valor', o rótulo vazio com o valor
    nas linhas seguintes, ou a seção '### Rótulo' com o texto até a próxima. Devolve (linha, valor, nome usado)."""
    fim = len(linhas) if fim is None else fim
    for nome in rotulos(rotulo):
        neg = _negrito(nome)
        for i in range(ini, fim):
            m = neg.match(linhas[i])
            if m:
                valor = m.group(1).strip()
                if not valor:
                    valor = _junta(linhas[:fim], i)
                return i + 1, valor, nome
        sec = re.compile(r"^#{2,4}\s+" + re.escape(nome) + r"\b", re.I)
        for i in range(ini, fim):
            if sec.match(linhas[i]):
                corpo = []
                for x in linhas[i + 1:fim]:
                    if re.match(r"^#{1,4}\s", x):
                        break
                    corpo.append(x)
                return i + 1, "\n".join(corpo).strip(), nome
    return None, None, None


def estado(valor):
    v = (valor or "").strip()
    if not v:
        return "vazio"
    if A_DEFINIR.match(v):
        return "vazio"
    linhas = [x.strip() for x in v.splitlines() if x.strip()]
    if linhas and all(x.startswith("|") for x in linhas) and len(linhas) <= 2:
        return "vazio"  # a tabela só com o cabeçalho (e o separador)
    if NSA.match(v):
        resto = NSA.sub("", v, count=1)
        return "nsa" if MOTIVO.search(resto) else "nsa-sem-motivo"
    return "ok"


def unidades(linhas):
    """As unidades: cada cabeçalho '### Tela N…' (ou Story, Unidade) até o próximo cabeçalho de mesmo nível ou menor."""
    out = []
    for i, ln in enumerate(linhas):
        m = CAB_UNIDADE.match(ln)
        if not m:
            continue
        nivel = len(ln) - len(ln.lstrip("#"))
        fim = len(linhas)
        for j in range(i + 1, len(linhas)):
            mm = CAB_SECAO.match(linhas[j])
            if mm and len(mm.group(1)) <= nivel:
                fim = j
                break
        out.append({"linha": i + 1, "indice": i, "titulo": ln.strip("# ").strip(), "corpo": linhas[i + 1:fim]})
    return out


def campo_unidade(corpo, rotulo):
    """O valor de '**Rótulo:**' (ou '**Rótulo (nota):**', ou '**Rótulo**:') em qualquer ponto da linha, até o próximo
    rótulo em negrito com dois-pontos na mesma linha. Dois rótulos na mesma linha contam como próprios.
    Devolve (valor, nome usado) ou (None, None)."""
    for nome in rotulos(rotulo):
        pad = re.compile(r"\*\*" + re.escape(nome) + r"(?:\s*\([^)]*\))?\s*(?::\s*\*\*|\*\*\s*:)\s*", re.I)
        for ln in corpo:
            m = pad.search(ln)
            if m:
                resto = ln[m.end():]
                prox = re.search(r"\*\*[^*\n]{1,40}?(?::\s*\*\*|\*\*\s*:)", resto)
                return (resto[:prox.start()] if prox else resto).strip(), nome
    return None, None


def siglas(linhas):
    """As siglas do bloco 'Fontes, por sigla', com o caminho de cada uma quando há: {sigla: caminho ou ''}. O bloco são
    as linhas seguidas ao título (uma linha em branco logo depois dele é tolerada) e fecha na primeira linha em branco
    ou no próximo rótulo do contrato; só conta o negrito curto que não é rótulo (sem dois-pontos)."""
    s = {}
    for k, ln in enumerate(linhas):
        if not re.search(r"Fontes,? por sigla", ln, re.I):
            continue
        j = k + 1
        if j < len(linhas) and not linhas[j].strip():
            j += 1
        while j < len(linhas):
            x = linhas[j]
            if not x.strip() or x.lstrip().startswith("#") or any(p.match(x) for p in ROTULO_CONHECIDO):
                break
            # "Fichas em `knowledge/sources/`: **TB** `2026-…md`" põe a pasta na frente do nome
            base = "knowledge/sources/" if re.search(r"`knowledge/sources/?`", x) else ""
            for seg in re.split(r";", x):
                for m in re.finditer(r"\*\*([A-Z][A-Za-z0-9]{0,7})\*\*(?!\s*:)", seg):
                    cam = re.search(r"`([^`]+)`", seg[m.end():])
                    c = cam.group(1) if cam else ""
                    s[m.group(1)] = (base + c) if (c and base and "/" not in c) else c
            j += 1
        break
    return s


def raiz_do_repo(caminho):
    p = Path(caminho).resolve().parent
    for q in [p] + list(p.parents):
        if (q / ".git").exists():
            return q
    return None


def ficha_existe(raiz, cam):
    if not raiz or not cam:
        return False
    if "knowledge/sources/" in cam:
        rel = cam[cam.index("knowledge/sources/"):]
        if (raiz / rel).is_file():
            return True
        cam = Path(rel).name
    if "/" in cam or not cam.endswith(".md"):
        return False
    # o nome solto (o prefixo de data pode estar no título do bloco): procura em knowledge/sources/
    return any((raiz / "knowledge/sources").glob("*" + cam))


DESTINO = re.compile(r"\b(telas?|story|stories|unidade|cena|bloco|ângulo|angulo|legenda)\b", re.I)
FORA = re.compile(r"\bfica(m)? fora\b|\bfora\b|n[ãa]o se aplica", re.I)


def itens(valor):
    """Os pontos de uma lista: cada item de topo, com as linhas de continuação."""
    out = []
    for x in valor.splitlines():
        if ITEM.match(x) and (len(x) - len(x.lstrip())) < 2:
            out.append(x.strip())
        elif out and x.strip():
            out[-1] += " " + x.strip()
    return out


def confere(caminho):
    texto = Path(caminho).read_text(encoding="utf-8")
    linhas = texto.splitlines()
    achados = []
    raiz = raiz_do_repo(caminho)

    def add(cod, onde, msg, dica, nivel="ERRO"):
        achados.append({"nivel": nivel, "codigo": cod, "onde": onde, "msg": msg, "dica": dica})

    us = unidades(linhas)
    fim_cabeca = us[0]["indice"] if us else len(linhas)
    if not us:  # sem unidade, a cabeça acaba no primeiro campo do pé
        for i, ln in enumerate(linhas):
            if any(_negrito(n).match(ln) or re.match(r"^#{2,4}\s+" + re.escape(n) + r"\b", ln, re.I)
                   for r in PE for n in rotulos(r)):
                fim_cabeca = i
                break
    ini_pe = us[0]["indice"] if us else fim_cabeca

    n, v, _ = acha(linhas, "Nível", 0, fim_cabeca)
    m = re.search(r"\bN([12])\b", v or "")
    if not m:
        add("CT-NIVEL", f"linha {n}" if n else "cabeça", "o **Nível:** não está na cabeça ou não diz N1 nem N2",
            "escreva '**Nível:** N1' ou 'N2' antes da primeira unidade, com o motivo se desceu ou subiu")
        return achados
    nivel = "N" + m.group(1)
    regra = dict(REGRA[nivel])
    # Stories de véspera: dito no Nível ou no Objetivo (o "não é véspera" do Critério não conta)
    vespera = " ".join(filter(None, [v, acha(linhas, "Objetivo", 0, fim_cabeca)[1]]))
    if nivel == "N2" and re.search(r"v[ée]spera", vespera, re.I) and not re.search(r"n[ãa]o\s+[ée]\b[^.]*v[ée]spera", vespera, re.I):
        regra["Critério de escolha"] = "sim"  # contrato.md: nos Stories de véspera, sim
    sinonimo_usado = set()

    def julga(rotulo, onde_padrao, achado):
        lin, valor, nome = achado
        if nome and nome != rotulo:
            sinonimo_usado.add((nome, rotulo))
        tipo = regra[rotulo]
        onde = f"linha {lin}" if lin else onde_padrao
        if lin is None:
            if tipo == "sim":
                add("CT-AUSENTE", onde, f"**{rotulo}** do {nivel} não aparece",
                    f"abra o campo **{rotulo}:** (references/contrato.md)")
            else:
                add("CT-SUMIU", onde, f"**{rotulo}** sumiu",
                    f"escreva '**{rotulo}:** não se aplica, porque…' (campo fora do nível não some)")
            return
        e = estado(valor)
        if e == "vazio" and tipo == "sim":
            add("CT-VAZIO", onde, f"**{rotulo}** vazio, 'a definir' ou tabela sem linha",
                "preencha o campo agora, antes da forma")
        elif e == "vazio":
            add("CT-SUMIU", onde, f"**{rotulo}** vazio", f"escreva o valor ou '**{rotulo}:** não se aplica, porque…'")
        elif e == "nsa-sem-motivo":
            add("CT-NSA-MOTIVO", onde, f"**{rotulo}**: 'não se aplica' sem o motivo", "acrescente 'porque…'")
        elif e == "nsa" and tipo == "sim" and rotulo not in ("Puxa a próxima",):
            add("CT-NSA-DENTRO", onde, f"**{rotulo}** é do {nivel} e saiu 'não se aplica'",
                "preencha: dentro do nível o campo não fica de fora")

    for r in CABECA:
        julga(r, "cabeça", acha(linhas, r, 0, fim_cabeca))

    sig = siglas(linhas)
    if not us:
        add("CT-AUSENTE", "unidades", "nenhuma unidade achada ('### Tela N', '### Story N')",
            "abra uma seção por unidade, com os rótulos dos campos")
    for u in us:
        onde = f"linha {u['linha']} ({u['titulo'][:40]})"
        corpo = u["corpo"]
        valores = {}
        for r in UNIDADE:
            valor, nome = campo_unidade(corpo, r)
            if nome and nome != r:
                sinonimo_usado.add((nome, r))
            valores[r] = valor
            tipo = regra[r]
            if valor is None:
                if r in ("Promete", "Paga em") and nivel == "N2":
                    combinado = any(re.search(r"\*\*[^*\n]*Promete[^*\n]*Paga em", x) for x in corpo)
                    add("CT-PROMETE", onde, f"sem **{r}** em rótulo próprio" + (" (está num rótulo combinado)" if combinado else ""),
                        "escreva '**Promete:**' e '**Paga em:**' em linhas próprias; na unidade sem promessa, "
                        "'**Promete:** não se aplica, porque…'")
                elif tipo == "sim":
                    add("CT-AUSENTE", onde, f"**{r}** não aparece na unidade", f"abra '**{r}:**'")
                elif tipo == "fora":
                    add("CT-SUMIU", onde, f"**{r}** sumiu (fora do {nivel})", f"'**{r}:** não se aplica, porque…'")
                continue
            e = estado(valor)
            if e == "vazio" and tipo == "sim":
                add("CT-VAZIO", onde, f"**{r}** vazio ou 'a definir'", "preencha o campo")
            elif e == "nsa-sem-motivo":
                add("CT-NSA-MOTIVO", onde, f"**{r}**: 'não se aplica' sem o motivo", "acrescente 'porque…'")
            elif e == "nsa" and tipo == "sim" and r not in ("Puxa a próxima", "Fonte", "Promete", "Paga em"):
                add("CT-NSA-DENTRO", onde, f"**{r}** é do {nivel} e saiu 'não se aplica'", "preencha o campo")
            if r == "Fonte" and e == "ok":
                usadas = [s for s in sig if re.search(r"(?<![A-Za-z0-9])" + re.escape(s) + r"(?![A-Za-z0-9])", valor)]
                resposta = nivel == "N1" and re.search(r"\bresposta\b", valor, re.I)
                if not usadas and "knowledge/sources/" not in valor and not resposta:
                    add("CT-FONTE", onde, "**Fonte** sem sigla da lista nem caminho em knowledge/sources/",
                        "aponte a ficha pela sigla e a linha (ex.: 'WZ:35'); no N1, a resposta pelo número ou pelo tema")
                elif usadas and "knowledge/sources/" not in valor and not any(ficha_existe(raiz, sig[s]) for s in usadas):
                    add("AV-FICHA", onde, f"as siglas da **Fonte** ({', '.join(sorted(usadas))}) não apontam ficha que "
                        "exista em knowledge/sources/", "acrescente a sigla da ficha do fato, ou escreva a ficha antes",
                        nivel="AVISO")
                # a sigla sem lugar: no trecho dela (até o ';'), nenhum número (linha, página ou seção)
                for trecho in re.split(r";", valor):
                    tem = [s for s in usadas if re.search(r"(?<![A-Za-z0-9])" + re.escape(s) + r"(?![A-Za-z0-9])", trecho)]
                    if tem and not re.search(r"\d", trecho):
                        add("AV-LINHA", onde, f"a sigla {tem[0]} na **Fonte** sem a linha, a página ou a seção",
                            "acrescente ':linha' (ou a página, ou a seção) da ficha", nivel="AVISO")
                        break
        if nivel == "N2" and estado(valores.get("Promete")) == "ok" and estado(valores.get("Paga em")) in ("nsa", "nsa-sem-motivo"):
            add("CT-PROMETE", onde, "promete e o **Paga em** saiu 'não se aplica'",
                "escreva onde paga: a unidade, ou a outra peça e a unidade de lá")

    for r in PE:
        julga(r, "pé", acha(linhas, r, ini_pe))

    lin, valor, _ = acha(linhas, "Não escolhidos", ini_pe)
    if lin and estado(valor) == "ok":
        for x in itens(valor):
            resto = re.sub(r"^[-*]\s+\*\*[^*]+\*\*", "", x)  # o destino se lê depois do nome do ponto
            if DESTINO.search(resto):
                continue
            fora = FORA.search(x)
            if fora and not re.search(r"porque|:|,|\(", x[fora.start():]):
                add("CT-ESCOLHIDO", f"linha {lin}", f"ponto fora sem o porquê: {x[:70]}", "diga por quê")
            elif not fora:
                add("CT-ESCOLHIDO", f"linha {lin}", f"ponto sem a unidade de destino: {x[:70]}",
                    "escreva a peça e a unidade ('aqui, tela N', '→ <outra peça>, tela N' ou a tela pela função) "
                    "ou 'fica fora, porque…'")

    for nome, r in sorted(sinonimo_usado):
        add("AV-ROTULO", "escaleta", f"o rótulo '**{nome}:**' no lugar de '**{r}:**'",
            f"use '**{r}:**', a grafia do contrato (references/contrato.md)", nivel="AVISO")
    return achados


def main(argv):
    como_json = "--json" in argv
    arqs = [a for a in argv if a != "--json"]
    if not arqs:
        print(__doc__)
        return 2
    tudo = {a: confere(a) for a in arqs}
    if como_json:
        print(json.dumps(tudo, ensure_ascii=False, indent=1))
    else:
        for a, ach in tudo.items():
            erros = sum(1 for x in ach if x["nivel"] == "ERRO")
            print(f"{a}: {erros} ERRO, {len(ach) - erros} AVISO")
            for x in ach:
                print(f"  [{x['nivel']}] {x['codigo']} {x['onde']}: {x['msg']} (dica: {x['dica']})")
    return 1 if any(x["nivel"] == "ERRO" for ach in tudo.values() for x in ach) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
