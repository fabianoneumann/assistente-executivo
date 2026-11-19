"""O teste negativo da conferência do diagrama: os exemplos do modelo saem limpos, e cada defeito plantado na página
renderizada (o rótulo do laço tirado de dentro dele, a perna do laço puxada para fora da base, o rótulo de avanço
posto sobre um cartão, a ponta de uma seta afastada do alvo) é pego pela chave certa; o dado que não serve (a aresta
para um passo que não existe, o tipo fora da lista, o grupo que não existe, o id repetido) dá a caixa de erro na página
com a causa; e a lista dos passos em texto existe na tela larga (escondida, para o leitor de tela) e substitui a
figura na tela estreita. Desde a rodada 3: o esquema fora do navegador pega cada caso pelo código (ESQ-..., C4-...,
SEQ-..., o aviso de dividir a sequência grande sem contar como erro); a sequência sai limpa e a seta afastada da
linha de vida é pega (seq_ponta); e os links da lista em texto (o padrão do NHS Scotland) levam a um passo que existe.
Uso: python -X utf8 teste_diagrama_conferir.py  -> sai com 1 se algum caso falhar."""
import json, shutil, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import diagrama_render as render  # noqa: E402
import diagrama_esquema as esquema  # noqa: E402
from diagrama_conferir import JS_PADRAO, JS_SEQ  # noqa: E402

PLANTAS = {
    "laco": """() => { const r = document.querySelector('.grafo .rotulo-aresta.laco'); r.style.left = (parseFloat(r.style.left) + 160) + 'px'; }""",
    "laco_perna": """() => { const p = document.querySelector('.grafo path.aresta[data-laco]');
        p.setAttribute('d', p.getAttribute('d').replace(/^M([\\d.]+),([\\d.]+)/, (m, x, y) => `M${x},${+y + 30}`)); }""",
    "rotulo_sobre": """() => { const r = [...document.querySelectorAll('.grafo .rotulo-aresta.avanco')][0];
        const c = document.querySelector('.grafo .no'); r.style.left = c.style.left; r.style.top = (parseFloat(c.style.top) + 20) + 'px'; }""",
    "ponta_fora": """() => { const p = [...document.querySelectorAll('.grafo path.aresta.avanco')][0];
        p.setAttribute('d', p.getAttribute('d').replace(/L([\\d.]+),([\\d.]+)$/, (m, x, y) => `L${x - 12},${y}`)); }""",
}


def ruins(base: dict) -> dict:
    """Os dados que não servem, cada um com o trecho que a mensagem de erro tem de trazer (a causa, não a consequência)."""
    import copy
    out = {}
    d = copy.deepcopy(base); d["arestas"][0]["para"] = "naoexiste"; out["aresta_para_inexistente"] = (d, '"naoexiste" (em para) não existe')
    d = copy.deepcopy(base); d["arestas"][1]["tipo"] = "pulo"; out["tipo_de_aresta"] = (d, '"pulo" não é')
    d = copy.deepcopy(base); d["nos"][2]["grupo"] = "fantasma"; out["grupo_inexistente"] = (d, 'o grupo "fantasma" não existe')
    d = copy.deepcopy(base); d["nos"][3]["id"] = d["nos"][2]["id"]; out["id_repetido"] = (d, "se repete")
    return out


def casos_do_esquema() -> list:
    """(nome, dado, código esperado, nível) — conferidos pelo diagrama_esquema.validar, sem navegador."""
    import copy
    ler = lambda n: json.loads((render.MODELO / n).read_text(encoding="utf-8"))  # noqa: E731
    arq, seq, flu = ler("arquitetura.json"), ler("sequencia.json"), ler("fluxo.json")
    out = []
    d = copy.deepcopy(flu); d["arestas"][0]["para"] = "naoexiste"; out.append(("fluxo, aresta para nó inexistente", d, "ESQ-REF", "erro"))
    d = copy.deepcopy(flu); d["modelo"] = "pizza"; out.append(("modelo desconhecido", d, "ESQ-MODELO", "erro"))
    d = copy.deepcopy(arq); d["arestas"][0]["rotulo"] = "usa"; out.append(("C4, rótulo genérico", d, "C4-GENERICO", "erro"))
    d = copy.deepcopy(arq); d["arestas"][1].pop("rotulo"); out.append(("C4, seta sem rótulo", d, "C4-ROTULO", "erro"))
    d = copy.deepcopy(arq); next(n for n in d["nos"] if n["id"] == "api").pop("tecnologia"); out.append(("C4, contêiner sem tecnologia", d, "C4-TECNOLOGIA", "erro"))
    d = copy.deepcopy(arq); d["titulo"] = "As partes do sistema"; out.append(("C4, título sem tipo e escopo", d, "C4-TITULO", "erro"))
    d = copy.deepcopy(arq); d["legenda"].pop("grupo"); out.append(("C4, legenda sem a fronteira", d, "C4-LEGENDA", "erro"))
    d = copy.deepcopy(flu); d["arestas"][0]["rotulo"] = "  "; out.append(("fluxo, rótulo vazio", d, "ESQ-TEXTO", "erro"))
    d = copy.deepcopy(seq); d["passos"][0]["para"] = "fantasma"; out.append(("sequência, mensagem para quem não participa", d, "SEQ-REF", "erro"))
    d = copy.deepcopy(seq); d["participantes"].append("fantasma"); out.append(("sequência, participante fora da arquitetura", d, "SEQ-PARTICIPANTE", "erro"))
    d = copy.deepcopy(seq); d["passos"][3]["bloco"] = "talvez"; out.append(("sequência, bloco desconhecido", d, "SEQ-BLOCO", "erro"))
    d = copy.deepcopy(seq); d["passos"] += [{"tipo": "mensagem", "de": "dev", "para": "agente", "texto": f"mais {k}"} for k in range(14)]
    out.append(("sequência acima de 20 mensagens", d, "SEQ-DIVIDIR", "aviso"))
    return out


def main():
    from playwright.sync_api import sync_playwright
    falhou = 0
    for nome, d, codigo, nivel in casos_do_esquema():  # o esquema, fora do navegador
        ach = esquema.validar(d, render.MODELO / "x.json")
        ok = any(x["codigo"] == codigo and x["nivel"] == nivel and x["dica"] for x in ach)
        if nivel == "aviso":  # o aviso não vira erro
            ok = ok and not any(x["nivel"] == "erro" for x in ach)
        falhou += not ok
        print(("ok  " if ok else "FALHA ") + f"esquema {nome} -> {codigo} ({nivel})" + ("" if ok else " " + json.dumps(ach, ensure_ascii=False)[:300]))
    for n in ("fluxo.json", "fluxo-mais.json", "fluxo-ramos.json", "travas.json", "arquitetura.json", "prioridade.json", "sequencia.json"):
        ach = esquema.validar_arquivo(render.MODELO / n)
        ok = not ach
        falhou += not ok
        print(("ok  " if ok else "FALHA ") + f"esquema {n} limpo" + ("" if ok else " " + json.dumps(ach, ensure_ascii=False)[:300]))
    exemplos = [render.MODELO / n for n in ("fluxo.json", "fluxo-mais.json", "fluxo-ramos.json", "travas.json",
                                            "arquitetura.json", "prioridade.json", "sequencia.json")]
    raiz = render.pasta_servida(exemplos); srv = render.servidor(raiz); porta = srv.server_address[1]
    casos_ruins = ruins(json.loads((render.MODELO / "fluxo.json").read_text(encoding="utf-8")))
    for nome, (d, _) in casos_ruins.items():
        (raiz / f"ruim-{nome}.json").write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    # o C4 fica fora da regra da saída de decisão: um contêiner com duas relações rotuladas não é pergunta
    c4 = json.loads((render.MODELO / "arquitetura.json").read_text(encoding="utf-8"))
    outro = next(n["id"] for n in c4["nos"] if n["id"] not in ("api", "banco"))
    c4["arestas"].append({"de": "api", "para": outro, "rotulo": "avisa por HTTPS", "tipo": "avanço"})
    (raiz / "c4-duas-relacoes.json").write_text(json.dumps(c4, ensure_ascii=False), encoding="utf-8")
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch(args=["--disable-lcd-text"])
            pg = nav.new_page(viewport={"width": 1280, "height": 900})
            for d in exemplos:  # os limpos, nos dois modelos (o fluxo em passos e o grafo)
                render.abrir(pg, porta, d.name, render.pagina_de(d))
                pg.evaluate(f"document.body.dataset.arestas = '{len(json.loads(d.read_text(encoding='utf-8')).get('arestas') or [])}'")
                r = pg.evaluate(JS_PADRAO)
                if render.pagina_de(d) == "sequencia.html":
                    r.update(pg.evaluate(JS_SEQ))
                sujos = {k: v for k, v in r.items() if isinstance(v, list) and v}
                ok = not sujos
                falhou += not ok
                print(("ok  " if ok else "FALHA ") + f"{d.stem} limpo" + ("" if ok else " " + json.dumps(sujos, ensure_ascii=False)))
            for chave, js in PLANTAS.items():  # os plantados, no exemplo com ramos (tem laço e rótulo de avanço)
                render.abrir(pg, porta, "fluxo-ramos.json")
                pg.evaluate(js)
                r = pg.evaluate(JS_PADRAO)
                alvo = "laco" if chave.startswith("laco") else chave
                ok = bool(r.get(alvo))
                falhou += not ok
                print(("ok  " if ok else "FALHA ") + f"plantado {chave} -> {alvo}: {len(r.get(alvo) or [])} achado(s)")
            # a saída de decisão: o "sim" levado para perto do destino é pego pelo saida_longe
            render.abrir(pg, porta, "prioridade.json", "grafo.html")
            pg.evaluate("""() => { const r = document.querySelector('.grafo .rotulo-aresta[data-saida]');
                const a = document.querySelector(`.grafo path.aresta[data-indice="${r.dataset.aresta}"]`);
                const fim = a.getPointAtLength(a.getTotalLength()); r.style.left = (fim.x + 6) + 'px'; r.style.top = (fim.y - 40) + 'px'; }""")
            r = pg.evaluate(JS_PADRAO); ok = bool(r.get("saida_longe"))
            falhou += not ok
            print(("ok  " if ok else "FALHA ") + f"plantado sim perto do destino -> saida_longe: {len(r.get('saida_longe') or [])} achado(s)")
            # o C4 com um contêiner de duas relações: nada de saida_longe (a regra é só da árvore de decisão)
            render.abrir(pg, porta, "c4-duas-relacoes.json", "grafo.html")
            r = pg.evaluate(JS_PADRAO); ok = not r.get("saida_longe")
            falhou += not ok
            print(("ok  " if ok else "FALHA ") + f"C4 com duas relações saindo do mesmo contêiner -> saida_longe: {len(r.get('saida_longe') or [])} achado(s)")
            # a sequência: a seta afastada 20 px da linha de vida é pega pelo seq_ponta
            render.abrir(pg, porta, "sequencia.json", "sequencia.html")
            pg.evaluate("() => { const a = document.querySelector('.seq .linha.msg .seta'); a.style.left = (parseFloat(a.style.left) + 20) + 'px'; }")
            r = pg.evaluate(JS_SEQ); ok = bool(r.get("seq_ponta"))
            falhou += not ok
            print(("ok  " if ok else "FALHA ") + f"plantado seta da sequência fora da linha de vida -> seq_ponta: {len(r.get('seq_ponta') or [])} achado(s)")
            # os links da lista em texto levam a um passo que existe (fluxo com volta e grafo)
            for dado in ("fluxo-ramos.json", "arquitetura.json"):
                render.abrir(pg, porta, dado, render.pagina_de(render.MODELO / dado))
                links = pg.evaluate("[...document.querySelectorAll('#passos a')].map(a => !!document.querySelector(a.getAttribute('href')))")
                ok = bool(links) and all(links)
                falhou += not ok
                print(("ok  " if ok else "FALHA ") + f"links da lista em {dado}: {len(links)}, todos com alvo={all(links) if links else False}")
            for nome, (_, trecho) in casos_ruins.items():  # o dado que não serve: a causa à vista
                pg.goto(f"http://127.0.0.1:{porta}/fluxo.html?dados=ruim-{nome}.json")
                pg.wait_for_function("document.body.dataset.pronto", timeout=20000)
                caixa = pg.evaluate("(document.querySelector('.erro-diagrama') || {}).textContent || ''")
                ok = pg.evaluate("document.body.dataset.pronto") == "erro" and trecho in caixa
                falhou += not ok
                print(("ok  " if ok else "FALHA ") + f"dado ruim {nome}: " + (caixa[:120] if caixa else "(sem caixa de erro)"))
            # a lista dos passos: escondida na tela larga, a figura na estreita
            render.abrir(pg, porta, "fluxo.json")
            n_nos = len(json.loads((render.MODELO / "fluxo.json").read_text(encoding="utf-8"))["nos"])
            larga = pg.evaluate("[document.querySelectorAll('#passos li').length, getComputedStyle(document.querySelector('#passos')).clip !== 'auto']")
            ok = larga[0] >= n_nos and larga[1]
            falhou += not ok
            print(("ok  " if ok else "FALHA ") + f"lista na tela larga: {larga[0]} itens, escondida={larga[1]}")
            pe = nav.new_page(viewport={"width": 390, "height": 844})
            render.abrir(pe, porta, "fluxo.json")
            estreita = pe.evaluate("[document.body.dataset.layout, document.querySelectorAll('#passos li').length, getComputedStyle(document.querySelector('.grafo')).display, document.documentElement.scrollWidth <= window.innerWidth]")
            ok = estreita[0] == "lista" and estreita[1] >= n_nos and estreita[2] == "none" and estreita[3]
            falhou += not ok
            print(("ok  " if ok else "FALHA ") + f"tela estreita (390 px): layout={estreita[0]}, {estreita[1]} itens, grafo={estreita[2]}, sem rolagem={estreita[3]}")
            nav.close()
    finally:
        srv.shutdown(); shutil.rmtree(raiz, ignore_errors=True)
    falhou += casos_sem_navegador()
    print("tudo certo" if not falhou else f"{falhou} caso(s) falharam")
    sys.exit(1 if falhou else 0)


def casos_sem_navegador() -> int:
    """O Mermaid gerado com a sintaxe escapada e a colisão de ids, e dois dados de mesmo nome na pasta servida (os
    achados da revisão do código)."""
    import copy, tempfile
    import diagrama_mermaid as mmd
    falhou = 0
    base = json.loads((render.MODELO / "fluxo.json").read_text(encoding="utf-8"))
    d = copy.deepcopy(base); d["arestas"][0]["rotulo"] = 'a|b; "c" #d [e]'
    linha = [x for x in mmd.flowchart(d).splitlines() if "-->|" in x][0]
    ok = linha.count("|") == 2 and "#124;" in linha and "#59;" in linha and "#35;d" in linha and "#35#59;" not in linha
    falhou += not ok; print(("ok  " if ok else "FALHA ") + f"mermaid: o rótulo com | ; # \" [ sai escapado numa passada ({linha.strip()[:60]}...)")
    d = copy.deepcopy(base); extra = copy.deepcopy(d["nos"][1]); extra["id"] = "disc ussao"; d["nos"][1]["id"] = "disc-ussao"; d["nos"].append(extra)
    try:
        mmd.flowchart(d); ok = False
    except mmd.Colisao as e:
        ok = "disc ussao" in str(e) and "disc-ussao" in str(e)
    falhou += not ok; print(("ok  " if ok else "FALHA ") + "mermaid: dois ids que viram o mesmo id dão erro com os dois nomes")
    pasta = Path(tempfile.mkdtemp(prefix="dup-"))
    try:
        (pasta / "fluxo.json").write_text((render.MODELO / "fluxo-mais.json").read_text(encoding="utf-8"), encoding="utf-8")
        a, b = render.MODELO / "fluxo.json", pasta / "fluxo.json"
        raiz = render.pasta_servida([a, b])
        na, nb = render.nome_de(a), render.nome_de(b)
        ok = na != nb and (raiz / na).read_text(encoding="utf-8") == a.read_text(encoding="utf-8") and (raiz / nb).read_text(encoding="utf-8") == b.read_text(encoding="utf-8")
        shutil.rmtree(raiz, ignore_errors=True)
    finally:
        shutil.rmtree(pasta, ignore_errors=True)
    falhou += not ok; print(("ok  " if ok else "FALHA ") + f"render: dois dados de mesmo nome servidos sem se sobrescrever ({na}, {nb})")
    return falhou


if __name__ == "__main__":
    main()
