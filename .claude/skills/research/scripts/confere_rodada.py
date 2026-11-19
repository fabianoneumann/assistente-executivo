"""Conferência automática de uma rodada de pesquisa, antes da revisão do Passo 5 (skill `research`).

Aponta, sem corrigir nada, os desvios das cinco regras de procedimento que mais reincidiam: a regra
ganhou uma conferência de código, que roda antes de chamar a revisão, e o texto dela fica. Não substitui a revisão nem a lista "Itens que de fato se esquecem
aqui": confere só o que dá para ler nos arquivos da rodada.

  python -X utf8 .claude/skills/research/scripts/confere_rodada.py <pasta-da-rodada> <rotulos.json>
         [--achados achados.md] [--produtos "A,B"] [--publico-br [--legado]] [--json [arquivo]]

Entradas: a pasta da rodada e o arquivo de rótulos (`references/rotulos.md`). As saídas das buscas (Passo 2)
se procuram na pasta e nas subpastas de leva (a apuração da `story-angle` tem uma por leva), fora `fontes/`:
`qN-perplexity.json`, `qN-gemini.json` e `qN-nativa.md`, com sufixo antes do hífen (`q1pt-gemini.json`) ou
depois da frente (`q2-perplexity-pt.json`), e os nomes antigos `perplexity-qN.json` e `gemini-qN.json`. A
saída lista os arquivos lidos, por leva, e avisa de todo `.json` que ficou sem ler (fora `licencas.json` e
`rotulos.json`, que moram na pasta da rodada).
Saída: a lista legível no stdout; com `--json`, o mesmo em JSON (no stdout, ou no arquivo dado). Código de
saída: 0 sem desvio, 1 com desvio, 2 com erro de entrada (pasta sem nenhuma saída de busca, rótulos ou
rascunho que não abrem, saída de busca que não abre ou não é um objeto JSON, erro do próprio script).
"Aviso" é o que pede um olhar e não muda o código de saída.

As conferências:
  (a) com --publico-br: cada objetivo dos rótulos sem nenhuma consulta em português (Passo 2.5). A consulta
      diz a que objetivo serve pelo campo `objetivo` (`"O2"` ou `["O1", "O2"]`), obrigatório nas rodadas
      novas (`rotulos.md`): a consulta sem ele é desvio ("consulta sem objetivo"), e o objetivo ligado pelo
      campo sem consulta em português também, salvo quando há consulta em português sem o campo, que pode ser
      a variação que falta (aí é aviso). Para a consulta sem o campo, a heurística sugere na mensagem o
      objetivo provável: o que mais divide termos com ela (radical de 5 letras, sem acento, pesado pelo
      inverso de quantos objetivos têm o termo; todo objetivo que chega à metade da nota do melhor), e a
      consulta em português conta só para o de nota máxima. Com --legado (as rodadas antigas, sem o campo,
      que ficam como estão), a consulta sem o campo não é desvio: a heurística atribui, e o que ela acha é
      aviso, porque a atribuição e a língua (pelas palavras funcionais) são aproximadas; a saída mostra a
      atribuição para quem confere. Objetivo sem consulta nenhuma (o de síntese, em geral) é aviso. A regra
      aceita que o rascunho diga que se escolheu não fazer: com --achados, as linhas que parecem dizer isso
      aparecem.
  (b) com --produtos: cada produto sem consulta que o nomeie (desvio); só em consultas que nomeiam também
      outro produto da lista (aviso: a regra pede uma dirigida a cada um). O nome casa com fronteira e, quando
      termina em número, sem continuar a versão ("Seedance 2" não casa em "Seedance 2.5"; "Veo" casa em
      "veo-3.1-generate-preview"), e o produto que só aparece dentro do trecho de outro ("Kling" dentro de
      "Kling 4.0") não tira dela a condição de dirigida a esse outro.
  (c) as URLs das saídas (results e citations dos JSONs, os links dos `qN-nativa.md`) sem linha nos
      rótulos, comparadas normalizadas (esquema, `www.`, caixa do host, barra final, fragmento, parâmetros
      de rastreio e de conta, como `authuser` e `hl`, `.md` final e `?amp=1`, que já apareceram
      juntados numa linha, a caixa do dono e do repositório no GitHub e no Hugging Face e, no GitHub, o commit
      ou ramo do arquivo; o resto do caminho mantém a caixa); a URL sem linha própria cuja página-mãe tem linha (o arquivo de um
      repositório rotulado) é aviso, porque quem rotula pode tê-los juntado de propósito, e a que a `nota`
      dos rótulos cita, com ou sem esquema e comparada normalizada (a URL quebrada corrigida, por exemplo),
      também; e a mesma URL normalizada ou o mesmo `id` em mais de uma linha (com rótulos diferentes é
      desvio; iguais, aviso). O redirect do Gemini conta à parte (`rotulos.md`, campo `url`): casa com a
      linha de `url: null` cuja `descricao` traz o redirect; o que não casa pode ter sido resolvido para a
      URL de destino, o que este script não confere (não abre a rede), e fica como aviso.
  (d) a fonte `so_citacao` sem as rotas registradas (`knowledge/sources/README.md`, "Quando a primária não
      abre"). Procura nos campos de texto da linha (fora `id`, `url` e `registro`; o `lido` entra, porque a
      rota se registra nele), nas frases da `nota` que citam o `id` e, com --achados, nas linhas do rascunho
      que citam o `id` ou a URL (os dois com fronteira: `kling-api` não casa em `kling-api-pricing`). A página
      que saiu do ar ou mudou (404, 410, "fora do ar") pede a Wayback; o 403 é bloqueio ou acesso fechado, não
      página fora do ar. O artigo fechado passa com "fechado" registrado, porque a Wayback não serve para
      contornar acesso fechado; sem motivo registrado, passa qualquer rota registrada: o resumo oficial no
      PubMed ou no OpenAlex (o `lido: resumo`, sem "da busca", é o resumo da própria fonte), a versão aberta,
      a editora, o Chrome. A palavra com negação logo antes, na mesma oração ("não tentei a Wayback", "nem Chrome"),
      não conta, e a saída diz isso ("sem login, pelo Chrome" conta o Chrome). São aviso a página que abriu e veio vazia (`lido: texto`) e a fonte lida pelo resumo
      oficial com um 404 registrado, porque o 404 pode ser de uma cópia do artigo (o PDF num repositório).
  (e) com --achados: SÓ as respostas sem citação (results e citations vazios). Delas, as afirmações
      específicas (números com casa decimal, moeda, unidade ou proporção; termos em código; nomes próprios)
      que não aparecem no rascunho, contadas por resposta. Número e termo em código fora do rascunho é
      desvio; nome próprio é aviso, porque a extração por maiúscula erra para os dois lados. A afirmação sem
      citação dentro de uma resposta que tem citações fica fora: a lista feita à mão continua para ela.
      Aproximado: a busca é por texto (o nome traduzido ou a conta refeita não casam; o número casa só
      inteiro, sem dígito colado nem outra casa: "2.5" não casa em "2.5.1") e o bloco de código cercado fica
      de fora. A saída diz isso.

Biblioteca padrão, sem rede. No Windows, rodar com `-X utf8` (ou PYTHONUTF8=1).
O teste sem rede, com os casos que cada conferência tem de reprovar: `teste_conferidores.py`, nesta pasta
(rodar a cada edição deste script).
"""
import argparse
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import parse_qsl, unquote, urlencode, urlsplit, urlunsplit

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

REDIRECT = "vertexaisearch.cloud.google.com/grounding-api-redirect/"
URL_RE = re.compile(r"https?://[^\s\"'<>()\[\]{}|\\^`]+")
# URL sem esquema numa frase (`kling.ai/docs/pricing`): host com ponto e domínio de 2+ letras, caminho opcional
URL_SEM_ESQUEMA_RE = re.compile(r"(?<![\w@/.\-])(?:[a-z0-9\-]+\.)+[a-z]{2,}(?::\d+)?(?:/[^\s\"'<>()\[\]{}|\\^`]*)?",
                                re.I)
RASTREIO = {"amp", "ref", "ref_src", "fbclid", "gclid", "si", "source", "igshid", "mc_cid", "mc_eid",
            "authuser", "hl"}

# Os nomes das saídas de busca: os de hoje (`q3-gemini.json`, `q1-codex.json`, `q1pt-gemini.json`, `q2-perplexity-pt.json`) e
# os antigos (`perplexity-q1.json`, `gemini-q2.json`); a busca nativa, `qN-nativa.md`.
SAIDA_JSON_RE = re.compile(r"^(?:q\d+[a-z0-9]*-(?:perplexity|gemini|codex)(?:-[a-z0-9\-]+)?"
                           r"|(?:perplexity|gemini|codex)-q\d+[a-z0-9\-]*)\.json$", re.I)
SAIDA_NATIVA_RE = re.compile(r"^(?:q\d+[a-z0-9]*-nativa(?:-[a-z0-9\-]+)?|nativa-q\d+[a-z0-9\-]*)\.md$", re.I)
DONO_SEM_CAIXA = {"github.com", "huggingface.co"}
FORA_POR_DESENHO = {"licencas.json", "rotulos.json"}  # e a pasta `fontes/`, com as páginas e o `protegidas.json`

# Palavras funcionais (ficam fora dos termos que ligam consulta a objetivo) e, só para dizer a língua,
# palavras de conteúdo comuns nas consultas em português.
FUNC_PT = set("""de do da dos das em no na nos nas com para pra como que nao uma um uns umas os as ao aos por pelo
pela pelos pelas sao quais qual onde quando mesmo mesma cada sem ser esta estao tem dar da e o se seu sua""".split())
FUNC_EN = set("""the and of for with how to in which what is are on by from using does per when can or into vs
versus their there this that a an as at be it its via""".split())
MARCA_PT = FUNC_PT | set("""fazer gerar animar cena cenario camadas camada fundo desenho mao preco segundo novembro
modelo modelos versoes recursos quadro inicial atual atuais exemplo exemplos renderizar ilustracao movimento
referencia refazer codigo estilo remover separar planos tempo tras""".split())
MARCA_EN = FUNC_EN | set("""price latest current official""".split())
VAZIAS = FUNC_PT | FUNC_EN | set("""2024 2025 2026 2027 novembro november api 2d 3d""".split())


def sem_acento(t):
    t = unicodedata.normalize("NFKD", t or "")
    return "".join(c for c in t if not unicodedata.combining(c)).lower()


def e_portugues(texto):
    """Português pelas palavras funcionais e pelos acentos típicos (aproximado)."""
    bruto = (texto or "").lower()
    toks = re.findall(r"[a-z]+", sem_acento(texto))
    pt = sum(1 for w in toks if w in MARCA_PT) + (2 if re.search(r"[ãõç]", bruto) else 0)
    en = sum(1 for w in toks if w in MARCA_EN)
    return pt >= 2 and pt > en


def radicais(texto):
    out = set()
    for t in re.findall(r"[a-z0-9][a-z0-9.+\-]*", sem_acento(texto)):
        t = t.strip(".-+")
        if not t or t in VAZIAS or len(t) < 3:
            continue
        out.add(t[:5] if t.isalpha() and len(t) >= 5 else t)
    return out


def normaliza_url(u):
    u = (u or "").strip().rstrip(".,;:!?*")
    if not u:
        return u
    if not re.match(r"^[a-z][a-z0-9+.\-]*://", u, re.I):
        u = "https://" + u.lstrip("/")  # a `url` sem esquema nos rótulos (`kling.ai/llms.txt`)
    try:
        p = urlsplit(u)
        host = (p.hostname or "").lower()
        porta = p.port
    except ValueError:  # porta que não é número, colchete solto: fica como veio, igual dos dois lados
        return u
    if host.startswith("www."):
        host = host[4:]
    if porta and porta not in (80, 443):
        host = f"{host}:{porta}"
    path = unquote(p.path or "")  # o caminho mantém a caixa: youtu.be/AbC e youtu.be/abc são vídeos diferentes
    if host in DONO_SEM_CAIXA:  # o dono e o repositório não têm caixa nestes sites
        partes = path.split("/")
        for k in (1, 2):
            if len(partes) > k:
                partes[k] = partes[k].lower()
        path = "/".join(partes)
    if host == "github.com":  # o mesmo arquivo em outro commit ou ramo é a mesma candidata
        path = re.sub(r"^(/[^/]+/[^/]+)/(blob|tree)/[^/]+(?=/|$)", r"\1/blob/_", path)
        path = re.sub(r"/blob/_/?$", "", path)
    if path.endswith("/"):
        path = path.rstrip("/")
    if path.lower().endswith(".md"):
        path = path[:-3]
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
         if not k.lower().startswith("utm_") and k.lower() not in RASTREIO]
    return urlunsplit(("https", host, path, urlencode(sorted(q)), ""))


def le_json(caminho):
    return json.loads(Path(caminho).read_bytes().decode("utf-8"))


def urls_do_json(d):
    out = []
    for r in d.get("results") or []:
        if isinstance(r, dict) and r.get("url"):
            out.append(r["url"])
    for c in d.get("citations") or []:
        if isinstance(c, str):
            out.append(c)
        elif isinstance(c, dict) and c.get("url"):
            out.append(c["url"])
    return out


def urls_do_texto(t):
    out = []
    for m in URL_RE.finditer(t or ""):
        u = m.group(0).rstrip(".,;:!?*")
        out.append(u)
    return out


def fronteira(termo):
    """Regex do termo com fronteira: `kling-api` não casa em `kling-api-pricing`."""
    return re.compile(r"(?<![\w\-])" + re.escape(termo) + r"(?![\w\-])", re.I)


# ---------------------------------------------------------------- as saídas da rodada

def _ordem(p, pasta):
    rel = p.relative_to(pasta)
    m = re.search(r"q(\d+)", p.name)
    return (str(rel.parent), int(m.group(1)) if m else 10 ** 6, p.name)


def acha_saidas(pasta):
    """As saídas da rodada, na pasta e nas subpastas de leva, fora `fontes/`; e os `.json` que ficam sem ler."""
    jsons, nativas, sem_ler = [], [], []
    for raiz, dirs, arqs in os.walk(pasta):
        dirs[:] = sorted(d for d in dirs if d.lower() != "fontes" and not d.startswith("."))
        for a in arqs:
            p = Path(raiz) / a
            if SAIDA_JSON_RE.match(a):
                jsons.append(p)
            elif SAIDA_NATIVA_RE.match(a):
                nativas.append(p)
            elif a.lower().endswith(".json") and a.lower() not in FORA_POR_DESENHO:
                sem_ler.append(p)
    k = lambda p: _ordem(p, pasta)
    return sorted(jsons, key=k), sorted(nativas, key=k), sorted(sem_ler, key=k)


def le_saidas(pasta):
    jsons, nativas, sem_ler = acha_saidas(pasta)
    rel = lambda p: p.relative_to(pasta).as_posix()
    dados, erros = {}, []
    for f in jsons:
        try:
            d = le_json(f)
        except (ValueError, OSError) as e:
            erros.append(f"{rel(f)}: {e}")
            continue
        if not isinstance(d, dict):
            erros.append(f"{rel(f)}: não é um objeto JSON")
            continue
        dados[rel(f)] = d
    textos = {}
    for f in nativas:
        try:
            textos[rel(f)] = f.read_bytes().decode("utf-8", "replace")
        except OSError as e:
            erros.append(f"{rel(f)}: {e}")
    levas = defaultdict(list)
    for f in jsons + nativas:
        levas[f.relative_to(pasta).parent.as_posix()].append(f.name)
    return {"jsons": dados, "nativas": textos, "erros": erros,
            "sem_ler": [rel(f) for f in sem_ler], "levas": dict(levas),
            "n_json": len(jsons), "n_nativas": len(nativas)}


# ---------------------------------------------------------------- (a) português por objetivo

def objetivos_do_campo(c, objetivos):
    """Os objetivos que o campo `objetivo` da consulta nomeia, e os valores que não casam com nenhum."""
    v = c.get("objetivo")
    if v is None:
        return None, []
    casados, desconhecidos = [], []
    for x in (v if isinstance(v, list) else [v]):
        x = str(x).strip()
        m = [o for o in objetivos if x and (o == x or o.split()[0] == x or o.startswith(x + " "))]
        (casados.extend(m) if m else desconhecidos.append(x))
    return sorted(set(casados), key=objetivos.index), desconhecidos


def confere_portugues(rot, achados_txt, legado=False):
    """Sem --legado, a consulta sem o campo `objetivo` é desvio (o campo é obrigatório nas rodadas novas,
    `rotulos.md`) e a heurística só sugere o objetivo provável; com --legado (as rodadas antigas, sem o campo),
    a heurística atribui e o resultado dela é aviso."""
    objetivos = list((rot.get("objetivos") or {}).keys())
    consultas = rot.get("consultas") or []
    rad_obj = {o: radicais(re.sub(r"^\s*O\d+\s*", "", o)) for o in objetivos}
    df = defaultdict(int)
    for o in objetivos:
        for r in rad_obj[o]:
            df[r] += 1
    campo = {o: [] for o in objetivos}       # consultas ligadas pelo campo `objetivo`
    campo_pt = {o: [] for o in objetivos}
    heur = {o: [] for o in objetivos}        # consultas atribuídas pela heurística
    heur_pt = {o: [] for o in objetivos}     # em português, só no objetivo de nota máxima
    sem_campo, sem_campo_pt, sem_obj, avisos, desvios = [], [], [], [], []
    for c in consultas:
        cid, txt = c.get("id"), c.get("texto", "")
        pt = e_portugues(txt)
        alvo, desconhecidos = objetivos_do_campo(c, objetivos)
        for x in desconhecidos:
            avisos.append({"objetivo": f"consulta {cid}", "motivo": f"`objetivo` {x!r} não casa com nenhum objetivo"})
        if alvo:
            for o in alvo:
                campo[o].append(cid)
                if pt:
                    campo_pt[o].append(cid)
            continue
        sem_campo.append(cid)
        if pt:
            sem_campo_pt.append(cid)
        rc = radicais(txt)
        notas = {o: sum(1.0 / df[r] for r in rc & rad_obj[o]) for o in objetivos}
        melhor = max(notas.values()) if notas else 0
        # a consulta serve a todo objetivo que chega a metade da nota do melhor (pode servir a duas perguntas),
        # mas a língua dela só conta para o de nota máxima: a metade dava a um objetivo a consulta em
        # português de outro e escondia o desvio (code review, F2)
        h = [o for o, n in notas.items() if n > 0 and n >= 0.5 * melhor]
        if not h:
            sem_obj.append(cid)
        for o in h:
            heur[o].append(cid)
            if pt and notas[o] == melhor:
                heur_pt[o].append(cid)
        if not legado:
            desvios.append({"tipo": "consulta sem objetivo", "consulta": cid, "em_portugues": pt,
                            "objetivo_provavel": [o for o in h if notas[o] == melhor] + [o for o in h if notas[o] < melhor],
                            "valor_que_nao_casa": desconhecidos})
    mapa = []
    for o in objetivos:
        mapa.append({"objetivo": o, "pelo_campo": campo[o], "pelo_campo_em_portugues": campo_pt[o],
                     "pela_heuristica": heur[o], "pela_heuristica_em_portugues": heur_pt[o]})
        if campo_pt[o] or heur_pt[o]:
            continue
        # o objetivo do campo sem consulta em português é desvio, salvo se houver consulta em português sem o
        # campo, que pode ser a variação que falta; a sem campo que não está em português não pode ser
        if campo[o] and not sem_campo_pt:
            desvios.append({"tipo": "objetivo sem consulta em português", "objetivo": o, "consultas": campo[o]})
        elif campo[o] or heur[o]:
            motivo = ("provável desvio, pela heurística: nenhuma consulta em português atribuída"
                      if legado else "provável desvio: nenhuma consulta em português liga a ele, a conferir quando "
                      "as consultas sem objetivo ganharem o campo")
            avisos.append({"objetivo": o, "motivo": motivo, "consultas": campo[o] + heur[o]})
        else:
            avisos.append({"objetivo": o, "motivo": "nenhuma consulta atribuída (objetivo de síntese?)"})
    escolha = []
    if achados_txt:
        for n, l in enumerate(achados_txt.split("\n"), 1):
            s = sem_acento(l)
            if "portugu" in s and re.search(r"escolh|sem variac|nao (fiz|rod|fez)|optou|decid", s):
                escolha.append({"linha": n, "texto": l.strip()[:200]})
    return {"legado": legado, "desvios": desvios, "avisos": avisos, "atribuicao": mapa,
            "consultas_sem_campo_objetivo": sem_campo,
            "consultas_sem_objetivo": sem_obj,
            "consultas_em_portugues": [c.get("id") for c in consultas if e_portugues(c.get("texto", ""))],
            "possivel_registro_da_escolha": escolha}


# ---------------------------------------------------------------- (b) produto nomeado

def padrao_produto(nome):
    toks = re.findall(r"[a-z0-9]+", sem_acento(nome))
    # sem continuar a versão: "seedance 2" não casa em "seedance 2.5"; só quando o nome termina em número, porque
    # o nome sem versão casa no id de modelo da API ("seedance" em "seedance-1.0-pro", "veo" em "veo-3.1-...")
    fim = r"(?![a-z0-9]|[.\-]\d)" if toks and toks[-1][-1:].isdigit() else r"(?![a-z0-9])"
    return re.compile(r"(?<![a-z0-9])" + r"[\s.\-_]*".join(map(re.escape, toks)) + fim)


def confere_produtos(rot, produtos):
    consultas = rot.get("consultas") or []
    pads = {p: padrao_produto(p) for p in produtos}
    desvios, avisos, mapa = [], [], []
    for p in produtos:
        nomeiam, dirigidas = [], []
        for c in consultas:
            t = sem_acento(c.get("texto", ""))
            sp = [m.span() for m in pads[p].finditer(t)]
            if not sp:
                continue
            nomeiam.append(c)
            # o outro produto só conta quando aparece fora do trecho deste ("kling" dentro de "kling 4.0" não)
            outros = [q for q in produtos if q != p and any(
                not any(a <= s and e <= b for a, b in sp) for s, e in (m.span() for m in pads[q].finditer(t)))]
            if not outros:
                dirigidas.append(c)
        mapa.append({"produto": p, "consultas": [c.get("id") for c in nomeiam],
                     "dirigidas": [c.get("id") for c in dirigidas]})
        if not nomeiam:
            desvios.append({"produto": p})
        elif not dirigidas and len(produtos) > 1:
            avisos.append({"produto": p, "motivo": "só em consultas que nomeiam também outro produto da lista",
                           "consultas": [c.get("id") for c in nomeiam]})
    return {"desvios": desvios, "avisos": avisos, "mapa": mapa}


# ---------------------------------------------------------------- (c) URLs e rótulos opostos

CAMPOS = ("origem", "registro", "destino", "conteudo", "traz_novidade", "lido", "copia")


def confere_urls(saidas_lidas, rot):
    fontes = rot.get("fontes") or []
    nota = rot.get("nota") or ""
    saidas = defaultdict(set)  # url crua -> arquivos
    for nome, d in saidas_lidas["jsons"].items():
        for u in urls_do_json(d):
            saidas[u].add(nome)
    for nome, t in saidas_lidas["nativas"].items():
        for u in urls_do_texto(t):
            saidas[u].add(nome)

    rot_norm = defaultdict(list)
    descr_redirects = []
    for i, f in enumerate(fontes):
        if f.get("url"):
            rot_norm[normaliza_url(f["url"])].append(i)
        else:
            descr_redirects.extend(u for u in urls_do_texto(f.get("descricao") or "") if REDIRECT in u)

    def mae(n):
        """A linha da página-mãe (o repositório de um arquivo dele, a seção de uma página), se houver."""
        p = urlsplit(n)
        partes = [x for x in p.path.split("/") if x]
        for k in range(len(partes) - 1, 1, -1):
            cand = urlunsplit(("https", p.netloc, "/" + "/".join(partes[:k]), "", ""))
            if cand in rot_norm:
                return fontes[rot_norm[cand][0]].get("id")
        return None

    # as URLs que a `nota` cita, com e sem esquema, normalizadas: a comparação é por igualdade
    urls_nota = {normaliza_url(u) for u in urls_do_texto(nota)}
    urls_nota |= {normaliza_url(m.group(0)) for m in URL_SEM_ESQUEMA_RE.finditer(URL_RE.sub(" ", nota))}

    sem_linha, cru = defaultdict(set), {}
    red_total, red_casados, red_sem = set(), set(), set()
    for u, arqs in saidas.items():
        if REDIRECT in u:
            red_total.add(u)
            if any(u == d or (len(d) >= 80 and u.startswith(d)) or d.startswith(u) for d in descr_redirects):
                red_casados.add(u)
            else:
                red_sem.add(u)
            continue
        n = normaliza_url(u)
        if n not in rot_norm:
            sem_linha[n] |= arqs
            cru.setdefault(n, u)

    def grupos(chave):
        g = defaultdict(list)
        for i, f in enumerate(fontes):
            k = chave(f)
            if k:
                g[k].append(i)
        return {k: v for k, v in g.items() if len(v) > 1}

    repetidas = []
    vistos = set()
    for tipo, g in (("url", grupos(lambda f: normaliza_url(f["url"]) if f.get("url") else None)),
                    ("id", grupos(lambda f: f.get("id")))):
        for k, idx in g.items():
            chave = tuple(sorted(idx))
            if chave in vistos:
                continue
            vistos.add(chave)
            dif = [c for c in CAMPOS if len({json.dumps(fontes[i].get(c), ensure_ascii=False) for i in idx}) > 1]
            repetidas.append({"por": tipo, "chave": k, "ids": [fontes[i].get("id") for i in idx],
                              "linhas": [i + 1 for i in idx], "campos_diferentes": dif})
    desvios_rep = [r for r in repetidas if r["campos_diferentes"]]
    avisos_rep = [r for r in repetidas if not r["campos_diferentes"]]
    return {
        "urls_nas_saidas": len([u for u in saidas if REDIRECT not in u]),
        "urls_normalizadas_nas_saidas": len({normaliza_url(u) for u in saidas if REDIRECT not in u}),
        "sem_linha": [{"url": cru[u], "arquivos": sorted(a)} for u, a in sorted(sem_linha.items())
                      if not mae(u) and u not in urls_nota],
        "sem_linha_com_pagina_mae": [{"url": cru[u], "arquivos": sorted(a), "linha_mae": mae(u)}
                                     for u, a in sorted(sem_linha.items()) if mae(u)],
        "sem_linha_citada_na_nota": [{"url": cru[u], "arquivos": sorted(a)} for u, a in sorted(sem_linha.items())
                                     if not mae(u) and u in urls_nota],
        "rotulos_opostos": desvios_rep,
        "repetidas_com_rotulos_iguais": avisos_rep,
        "redirects": {"nas_saidas": len(red_total), "com_linha_null": len(red_casados),
                      "sem_linha_null": len(red_sem),
                      "linhas_null_nos_rotulos": sum(1 for f in fontes if not f.get("url"))},
    }


# ---------------------------------------------------------------- (d) só citação sem as rotas

NEGA = {"nao", "sem", "nem", "nunca", "not", "without", "never"}  # "no" fica fora: em português é "em o"
# o artigo e a preposição entre a negação e a rota não contam na janela: "não tentei a Wayback" é negação
# (o teste negativo pegou: com a janela de duas palavras cruas, o "a" a empurrava para fora)
MIUDAS = {"a", "o", "as", "os", "um", "uma", "de", "da", "do", "na", "no", "pela", "pelo", "the", "an", "to", "via"}
# e a janela não passa da vírgula, do ponto e vírgula, dos dois pontos nem do ponto seguido de espaço: em "bloqueado
# sem login, pelo Chrome", o "sem" nega o login, não a rota (a revisão do código pegou: tirar as miúdas
# alcançava mais para trás). O ponto colado não corta, por causa do "web.archive.org". Sem a vírgula ("sem login pelo
# Chrome"), a janela não separa as duas leituras e fica como negação: lacuna em `teste_conferidores.py`
ORACAO = re.compile(r"[,;:]|\.\s")
ROTAS = {
    "Wayback": r"wayback|archive\.org",
    "Chrome": r"chrome",
    "resumo oficial ou versão aberta": r"reposit|openalex|pubmed|e-utilities|\bpmc\b|arxiv|unpaywall|core\.ac|"
                                       r"semantic scholar|versao aberta|acesso aberto|open access|preprint|"
                                       r"biorxiv|psyarxiv|osf\.io|ssrn",  # ResearchGate e Scholar não: cópia de terceiro e busca
    "editora": r"editora|publisher|amostra",
}
# o `lido: resumo` (sem "da busca") é o resumo da própria fonte (`rotulos.md`): a rota do resumo oficial
LIDO_RESUMO = re.compile(r"^\s*(?:resumo|abstract)(?!\s*\(?\s*da\s+busca)\b", re.I)
FECHADO = r"fechad|paywall|(?:acesso|conteudo) (?:restrito|pago)|assinatura|assinante|closed|artigo pago|(?:exige|pede|requer) autentica|autenticar para"
# o 403 fica fora: é bloqueio ou acesso fechado, não página que saiu do ar, e a Wayback não serve para ele
FORA_DO_AR = r"\b404\b|\b410\b|fora do ar|saiu do ar|removid|nao existe mais|mudou|offline|link quebrado|dead link"


def acha(padrao, texto):
    """(achou sem negação, achou só com negação): a negação conta nas duas palavras antes, fora as miúdas, dentro da
    mesma oração."""
    livre = negada = False
    for m in re.finditer(padrao, texto):
        oracao = ORACAO.split(texto[max(0, m.start() - 40):m.start()])[-1]
        antes = [w for w in re.findall(r"[a-z]+", oracao) if w not in MIUDAS][-2:]
        if any(w in NEGA for w in antes):
            negada = True
        else:
            livre = True
    return livre, negada and not livre


def confere_so_citacao(rot, achados_txt):
    nota = rot.get("nota") or ""
    frases_nota = re.split(r"(?<=[.;])\s+|\(\d+\)", nota)
    linhas_ach = (achados_txt or "").split("\n")
    desvios, avisos = [], []
    for f in rot.get("fontes") or []:
        if f.get("registro") != "so_citacao":
            continue
        fid, url = f.get("id") or "", f.get("url") or ""
        # os campos da própria linha, menos os que são rótulo ou chave (um id com "chrome" não é a rota); o `lido`
        # entra, porque é nele que a rodada registra a rota ("resumo (PubMed, pela API E-utilities)")
        textos = [str(v) for k, v in f.items() if k not in ("id", "url", "registro") and isinstance(v, str)]
        rid = fronteira(fid) if fid else None
        rurl = re.compile(re.escape(url) + r"(?![\w/\-])") if url else None
        textos += [s for s in frases_nota if rid and rid.search(s)]
        textos += [l for l in linhas_ach if (rid and rid.search(l)) or (rurl and rurl.search(l))]
        junto = sem_acento(" ".join(textos))
        rotas = {n: acha(p, junto) for n, p in ROTAS.items()}
        if LIDO_RESUMO.search(str(f.get("lido") or "")):
            rotas["resumo oficial ou versão aberta"] = (True, False)
        fechado, fechado_neg = acha(FECHADO, junto)
        fora_ar, _ = acha(FORA_DO_AR, junto)
        tem = {n for n, (livre, _) in rotas.items() if livre}
        so_negada = sorted(n for n, (_, neg) in rotas.items() if neg and n not in tem)
        if fora_ar:
            caso, falta = "saiu do ar ou mudou", ([] if "Wayback" in tem else ["Wayback"])
        elif fechado:
            caso, falta = "fechado", []  # "fechado" registrado basta; a Wayback não se aplica
        else:
            # sem motivo registrado, qualquer rota registrada passa (`conferencias.md`): o resumo oficial no PubMed
            # ou no OpenAlex, a versão aberta, a editora, o Chrome; nenhuma, pede uma delas
            caso = "sem motivo registrado (fechado, fora do ar)"
            falta = [] if tem else ["uma das rotas (resumo oficial no PubMed ou OpenAlex, versão aberta, editora, "
                                    "Chrome)"]
        if not falta:
            continue
        item = {"id": fid, "url": url, "lido": f.get("lido"), "caso": caso, "falta": falta,
                "rotas_registradas": sorted(tem), "so_com_negacao": so_negada + (["fechado"] if fechado_neg else [])}
        if str(f.get("lido", "")).startswith("texto"):
            # a página que abriu e veio vazia é só citação sem as rotas (rotulos.md, `registro`); as rotas são
            # para a que não abre, então aqui é aviso: conferir se o conteúdo não carrega por script
            item["por_que_aviso"] = (f"abriu e veio vazia (lido: {f.get('lido')}); as rotas valem se o conteúdo "
                                     "carrega por script ou saiu do ar")
            avisos.append(item)
        elif fora_ar and "resumo oficial ou versão aberta" in tem:
            # o artigo lido pelo resumo oficial com um 404 registrado: o 404 pode ser de uma cópia (o PDF num
            # repositório), e a Wayback não é rota para a cópia de artigo fechado (`knowledge/sources/README.md`)
            item["por_que_aviso"] = ("lida pelo resumo oficial, com 404 ou \"fora do ar\" registrado: se o que saiu do "
                                     "ar foi a página da fonte, falta a Wayback; se foi uma cópia do artigo fechado, "
                                     "a Wayback não se aplica")
            avisos.append(item)
        else:
            desvios.append(item)
    return {"desvios": desvios, "avisos": avisos}


# ---------------------------------------------------------------- (e) afirmações sem citação

PALAVRA_RE = re.compile(r"[A-Za-zÀ-ÿ][\wÀ-ÿ.+\-]*[\wÀ-ÿ+]|[A-Za-zÀ-ÿ]")
NUM_RE = re.compile(
    r"(?<![\w.,])(?:US\$\s?|\$|€|R\$\s?)?\d+(?:[.,]\d+)*"
    r"(?:\s?(?:%|×|x\b|k\b|K\b|M\b|B\b|ms\b|s\b|fps\b|p\b|px\b|GB\b|MB\b|TB\b|USD\b|dB\b|LUFS\b|"
    r"seconds?\b|segundos?\b|minutes?\b|credits?\b|créditos?\b|tokens?\b))?|\d+:\d+")


def afirmacoes(texto, query):
    """Números, nomes próprios e termos em código de uma resposta (aproximado)."""
    t = re.sub(r"```.*?```", " ", texto or "", flags=re.S)
    codigo = {m.strip() for m in re.findall(r"`([^`\n]{2,60})`", t)}
    t2 = re.sub(r"`[^`\n]*`", " ", t)
    q_norm = sem_acento(query)
    nums = set()
    for m in NUM_RE.finditer(t2):
        s = m.group(0).strip()
        so_dig = re.sub(r"\D", "", s)
        simples = re.fullmatch(r"\d+", s) is not None
        if simples and (int(s) <= 10 or (len(s) == 4 and 1990 <= int(s) <= 2030)):
            continue
        if so_dig and sem_acento(s) in q_norm:
            continue
        nums.add(s)
    minusculas = {w for w in re.findall(r"\b[a-zà-ÿ][\wà-ÿ\-]*", t2)}
    nomes = set()
    for linha in t2.split("\n"):
        linha = re.sub(r"^\s*(?:[#>*\-+|]+|\d+[.)])\s*", "", linha)
        linha = linha.replace("**", " ").replace("__", " ")
        for frase in re.split(r"(?<=[.!?;])\s+|:|\||\(|\)", linha):
            toks = PALAVRA_RE.findall(frase)
            # trecho em Title Case (título, cabeçalho de tabela, rótulo) não dá nome por maiúscula
            longas = [w for w in toks if len(w) > 2 and w[:1].isalpha()]
            titulo = len(longas) >= 2 and sum(w[:1].isupper() for w in longas) >= 0.6 * len(longas)
            atual = []
            for i, w in enumerate(toks):
                w = w.rstrip(".")
                misto = bool(re.search(r"[a-z][A-Z]|[A-Za-z]\d|\d[A-Za-z]", w))
                maiusc = w[:1].isupper() and not titulo
                caps = w.isupper() and len(w) <= 3
                nome = (misto or (maiusc and i > 0 and w.lower() not in minusculas)) and not caps
                if nome and sem_acento(w) not in q_norm:
                    atual.append(w)
                else:
                    if atual:
                        nomes.add(" ".join(atual))
                    atual = []
            if atual:
                nomes.add(" ".join(atual))
    nomes = {n for n in nomes if len(n) > 2}
    return {"numeros": sorted(nums), "nomes": sorted(nomes), "codigo": sorted(codigo)}


def aparece(termo, ach_norm, ach_compacto):
    t = sem_acento(termo).strip()
    if not t:
        return True
    formas = {t, t.replace(",", "."), t.replace(".", ","), t.replace("us$", "$").replace(" ", "")}
    for f in formas:
        # número com fronteira: "1.39" não casa em "11.39", nem "60" em "13:60", nem "2.5" em "2.5.1"; "0.5" casa
        # em "0.50"
        antes = r"(?<![\d.,:])" if f[:1].isdigit() else ""
        depois = (r"0*(?![\d]|[.,]\d)" if re.search(r"[.,]\d+$", f) else r"(?![\d])") if f[-1:].isdigit() else ""
        if re.search(antes + re.escape(f) + depois, ach_norm):
            return True
    if re.search(r"\d", t) and not t[:1].isalpha():
        return False  # o número não passa pela forma compacta, que tira o ponto e junta os dígitos
    comp = re.sub(r"[^a-z0-9]", "", t)
    return len(comp) >= 4 and comp in ach_compacto


def confere_sem_citacao(saidas_lidas, achados_txt):
    ach_norm = sem_acento(achados_txt)
    ach_comp = re.sub(r"[^a-z0-9]", "", ach_norm)
    out, com_citacao, sem_resposta = [], [], []
    for nome, d in saidas_lidas["jsons"].items():
        if d.get("error") or not (d.get("answer") or "").strip():
            sem_resposta.append(nome)
            continue
        if d.get("results") or d.get("citations"):
            com_citacao.append(nome)
            continue
        a = afirmacoes(d.get("answer", ""), d.get("query", ""))
        faltam = {k: [x for x in v if not aparece(x, ach_norm, ach_comp)] for k, v in a.items()}
        total = sum(len(v) for v in a.values())
        n_faltam = sum(len(v) for v in faltam.values())
        out.append({"arquivo": nome, "afirmacoes": total, "fora_do_rascunho": n_faltam, "faltam": faltam,
                    "desvio": bool(faltam["numeros"] or faltam["codigo"])})
    return {"respostas_sem_citacao": out, "respostas_com_citacao_fora_desta_conferencia": com_citacao,
            "sem_resposta": sem_resposta,
            "desvios": [r for r in out if r["desvio"]],
            "avisos": [r for r in out if not r["desvio"] and r["fora_do_rascunho"]]}


# ---------------------------------------------------------------- saída

def corta(lista, n=40):
    return lista[:n], max(0, len(lista) - n)


def texto(res, args):
    L = [f"Conferência da rodada {res['pasta']}", f"Rótulos: {res['rotulos']}"]
    s = res["saidas"]
    L.append(f"Arquivos lidos: {s['n_json']} saídas JSON e {s['n_nativas']} `qN-nativa.md`, por pasta de leva:")
    for leva, nomes in s["levas"].items():
        L.append(f"    {leva}: {', '.join(nomes)}")
    for f in s["sem_ler"]:
        L.append(f"  aviso: arquivo .json fora do padrão de nome das saídas, sem ler: {f} "
                 "(se for saída de busca, renomear para qN-<frente>.json)")
    for e in s["erros"]:
        L.append(f"  ERRO de leitura (sai com 2; nada desta saída foi conferido): {e}")
    L.append("")
    if "portugues" in res:
        r = res["portugues"]
        if r["legado"]:
            L.append(f"(a) Português por objetivo, com --legado (rodada sem o campo `objetivo`): {len(r['desvios'])} "
                     f"desvio(s). Conta como desvio só o que o campo `objetivo` das consultas liga; sem o campo, a "
                     f"atribuição é por termos e a língua pelas palavras funcionais, e o resultado é aviso")
        else:
            L.append(f"(a) Português por objetivo: {len(r['desvios'])} desvio(s). O campo `objetivo` é obrigatório "
                     f"(`rotulos.md`): a consulta sem ele é desvio, com o objetivo provável pela heurística; rodada "
                     f"antiga, sem o campo, roda com --legado")
        if r["consultas_sem_campo_objetivo"] and r["legado"]:
            L.append(f"  aviso: {len(r['consultas_sem_campo_objetivo'])} consulta(s) sem o campo `objetivo`, "
                     f"atribuídas pela heurística (a em português, só ao objetivo de nota máxima): "
                     f"{', '.join(map(str, r['consultas_sem_campo_objetivo']))}")
        for m in r["atribuicao"]:
            partes = []
            if m["pelo_campo"]:
                partes.append(f"pelo campo {', '.join(m['pelo_campo'])} (em português "
                              f"{', '.join(m['pelo_campo_em_portugues']) or 'nenhuma'})")
            if m["pela_heuristica"]:
                partes.append(f"pela heurística {', '.join(m['pela_heuristica'])} (em português, nota máxima: "
                              f"{', '.join(m['pela_heuristica_em_portugues']) or 'nenhuma'})")
            L.append(f"    {m['objetivo'][:90]}: {'; '.join(partes) or 'nenhuma consulta'}")
        for d in r["desvios"]:
            if d["tipo"] == "consulta sem objetivo":
                prov = "; ".join(o[:60] for o in d["objetivo_provavel"][:3]) or "nenhum (termos sem casar)"
                extra = (f"; o valor {', '.join(map(repr, d['valor_que_nao_casa']))} não casa"
                         if d["valor_que_nao_casa"] else "")
                L.append(f"  DESVIO consulta sem objetivo: {d['consulta']}{' (em português)' if d['em_portugues'] else ''}"
                         f"{extra}; provável, pela heurística: {prov}")
            else:
                L.append(f"  DESVIO sem consulta em português: {d['objetivo'][:110]}")
        for a in r["avisos"]:
            L.append(f"  aviso: {a['objetivo'][:110]}: {a['motivo']}")
        if r["consultas_sem_objetivo"]:
            L.append(f"  aviso: consultas sem objetivo atribuído: {', '.join(map(str, r['consultas_sem_objetivo']))}")
        for e in r["possivel_registro_da_escolha"]:
            L.append(f"  no rascunho, linha {e['linha']} (registro da escolha de não fazer?): {e['texto']}")
        L.append("")
    if "produtos" in res:
        r = res["produtos"]
        L.append(f"(b) Uma consulta por produto nomeado: {len(r['desvios'])} desvio(s)")
        for m in r["mapa"]:
            L.append(f"    {m['produto']}: nomeado em {', '.join(m['consultas']) or 'nenhuma'}; "
                     f"dirigidas {', '.join(m['dirigidas']) or 'nenhuma'}")
        for d in r["desvios"]:
            L.append(f"  DESVIO nenhuma consulta nomeia {d['produto']}")
        for a in r["avisos"]:
            L.append(f"  aviso: {a['produto']}: {a['motivo']} ({', '.join(a['consultas'])})")
        L.append("")
    r = res["urls"]
    L.append(f"(c) URLs das saídas com linha nos rótulos: {r['urls_normalizadas_nas_saidas']} URLs normalizadas "
             f"nas saídas (fora os redirects), {len(r['sem_linha'])} sem linha, "
             f"{len(r['sem_linha_com_pagina_mae'])} só com a linha da página-mãe")
    mostra, resto = corta(r["sem_linha"])
    for s in mostra:
        L.append(f"  DESVIO sem linha: {s['url']}  ({', '.join(s['arquivos'])})")
    if resto:
        L.append(f"  ... e mais {resto} (lista inteira no --json)")
    for s in r["sem_linha_citada_na_nota"]:
        L.append(f"  aviso: sem linha, mas a `nota` dos rótulos cita a URL (correção registrada?): {s['url']}  "
                 f"({', '.join(s['arquivos'])})")
    for s in r["sem_linha_com_pagina_mae"]:
        L.append(f"  aviso: sem linha própria, mas a página-mãe tem ({s['linha_mae']}): {s['url']}  "
                 f"({', '.join(s['arquivos'])})")
    for d in r["rotulos_opostos"]:
        L.append(f"  DESVIO mesma {d['por']} em {len(d['ids'])} linhas ({', '.join(map(str, d['linhas']))}) "
                 f"com rótulos diferentes em {', '.join(d['campos_diferentes'])}: {d['chave']}")
    for d in r["repetidas_com_rotulos_iguais"]:
        L.append(f"  aviso: mesma {d['por']} em {len(d['ids'])} linhas, rótulos iguais: {d['chave']}")
    rd = r["redirects"]
    L.append(f"  à parte, redirects do Gemini: {rd['nas_saidas']} nas saídas, {rd['com_linha_null']} com linha "
             f"`url: null` que os traz na descrição, {rd['sem_linha_null']} sem ela; "
             f"{rd['linhas_null_nos_rotulos']} linhas `url: null` nos rótulos")
    if rd["sem_linha_null"]:
        L.append("  aviso: redirect sem linha `null` pode ter sido resolvido para a URL de destino (a `nota` diz?); "
                 "este script não abre a rede para conferir")
    L.append("")
    r = res["so_citacao"]
    L.append(f"(d) Só citação com as rotas registradas (a Wayback só para a página que saiu do ar ou mudou, 404 ou 410; "
             f"o artigo fechado passa com \"fechado\" registrado, e sem motivo registrado passa qualquer rota): "
             f"{len(r['desvios'])} desvio(s)")

    def linha_d(d):
        extra = f"; rotas registradas: {', '.join(d['rotas_registradas'])}" if d["rotas_registradas"] else ""
        if d["so_com_negacao"]:
            extra += f"; só com negação perto, não contam: {', '.join(d['so_com_negacao'])}"
        return f"{d['id']} ({d['url']}), {d['caso']}: sem registro de {' nem '.join(d['falta'])}{extra}"
    for d in r["desvios"]:
        L.append(f"  DESVIO {linha_d(d)}")
    for d in r["avisos"]:
        L.append(f"  aviso: {linha_d(d)}; {d['por_que_aviso']}")
    if not args.achados:
        L.append("  (sem --achados: procurou só nos rótulos)")
    L.append("")
    if "sem_citacao" in res:
        r = res["sem_citacao"]
        L.append(f"(e) SÓ as respostas sem citação (results e citations vazios): as afirmações delas que não aparecem "
                 f"no rascunho; número e termo em código fora é desvio, nome próprio é aviso. {len(r['respostas_sem_citacao'])} "
                 f"resposta(s) sem citação, {len(r['desvios'])} com desvio")
        L.append(f"    fora desta conferência: {len(r['respostas_com_citacao_fora_desta_conferencia'])} resposta(s) com "
                 f"citação, cujas afirmações sem citação ficam com a lista feita à mão (Passo 5)")
        L.append("    APROXIMADO: extração por padrão e busca por texto; nome traduzido, conta refeita e bloco de "
                 "código não casam")
        for d in r["respostas_sem_citacao"]:
            marca = "DESVIO" if d["desvio"] else ("aviso:" if d["fora_do_rascunho"] else "ok")
            L.append(f"  {marca} {d['arquivo']}: {d['fora_do_rascunho']} de {d['afirmacoes']} afirmações fora do "
                     f"rascunho")
            for k, v in d["faltam"].items():
                if v:
                    m, resto = corta(v, 25)
                    L.append(f"      {k}: {'; '.join(m)}" + (f" ... e mais {resto}" if resto else ""))
        L.append("")
    if res["erros_de_entrada"]:
        L.append(f"Total: {res['total_desvios']} desvio(s), e {len(res['erros_de_entrada'])} erro(s) de leitura: "
                 "a conferência não está completa (sai com 2).")
    else:
        L.append(f"Total: {res['total_desvios']} desvio(s). "
                 + ("Sem desvio." if not res["total_desvios"] else "Corrigir no rascunho ou nos rótulos antes da revisão."))
    return "\n".join(L)


def principal():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pasta", help="pasta da rodada, com as saídas qN-*.json e qN-nativa.md (ou as subpastas de leva)")
    ap.add_argument("rotulos", help="arquivo de rótulos da rodada (knowledge/research-rounds/<rodada>/rotulos.json)")
    ap.add_argument("--achados", help="o rascunho dos achados (achados.md)")
    ap.add_argument("--produtos", help='produtos, versões ou superfícies que a pergunta nomeia, separados por vírgula')
    ap.add_argument("--publico-br", action="store_true", help="o público é brasileiro: confere a variação em português")
    ap.add_argument("--legado", action="store_true",
                    help="rodada gravada sem o campo `objetivo` nas consultas (importada de outro lugar): na (a), a consulta sem o campo é "
                         "atribuída por termos e dá aviso, não desvio")
    ap.add_argument("--json", nargs="?", const="-", help="saída em JSON, no stdout ou no arquivo dado")
    args = ap.parse_args()

    pasta = Path(args.pasta)
    if args.legado and not args.publico_br:
        print("aviso: --legado só vale com --publico-br; ignorado", file=sys.stderr)
    if not pasta.is_dir():
        print(f"pasta não encontrada: {pasta}", file=sys.stderr)
        return 2
    try:
        rot = le_json(args.rotulos)
    except (OSError, ValueError) as e:
        print(f"não li os rótulos: {e}", file=sys.stderr)
        return 2
    if not isinstance(rot, dict):
        print("os rótulos não são um objeto JSON", file=sys.stderr)
        return 2
    achados_txt = ""
    if args.achados:
        try:
            achados_txt = Path(args.achados).read_bytes().decode("utf-8", "replace")
        except OSError as e:
            print(f"não li o rascunho: {e}", file=sys.stderr)
            return 2
    saidas = le_saidas(pasta)
    if not saidas["n_json"] and not saidas["n_nativas"]:
        print(f"nenhuma saída de busca (qN-<frente>.json, <frente>-qN.json, qN-nativa.md) em {pasta} nem nas "
              "subpastas de leva: é a pasta da rodada?", file=sys.stderr)
        for f in saidas["sem_ler"]:
            print(f"  .json fora do padrão de nome, sem ler: {f}", file=sys.stderr)
        return 2

    res = {"pasta": str(pasta), "rotulos": str(args.rotulos),
           "saidas": {k: saidas[k] for k in ("n_json", "n_nativas", "levas", "sem_ler", "erros")}}
    total = 0
    if args.publico_br:
        res["portugues"] = confere_portugues(rot, achados_txt, legado=args.legado)
        total += len(res["portugues"]["desvios"])
    if args.produtos:
        prods = [p.strip() for p in args.produtos.split(",") if p.strip()]
        res["produtos"] = confere_produtos(rot, prods)
        total += len(res["produtos"]["desvios"])
    res["urls"] = confere_urls(saidas, rot)
    total += len(res["urls"]["sem_linha"]) + len(res["urls"]["rotulos_opostos"])
    res["so_citacao"] = confere_so_citacao(rot, achados_txt)
    total += len(res["so_citacao"]["desvios"])
    if args.achados:
        res["sem_citacao"] = confere_sem_citacao(saidas, achados_txt)
        total += len(res["sem_citacao"]["desvios"])
    res["total_desvios"] = total
    res["erros_de_entrada"] = saidas["erros"]

    if args.json:
        js = json.dumps(res, ensure_ascii=False, indent=1) + "\n"
        if args.json == "-":
            sys.stdout.write(js)
        else:
            Path(args.json).write_bytes(js.encode("utf-8"))
            print(texto(res, args))
    else:
        print(texto(res, args))
    if saidas["erros"]:
        return 2
    return 1 if total else 0


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except Exception as e:  # erro do script não sai com o código de desvio (1)
        print(f"erro do script: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(2)
