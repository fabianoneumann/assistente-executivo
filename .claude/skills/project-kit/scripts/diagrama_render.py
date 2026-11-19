"""Renderiza o diagrama de fluxo em PNG a 1280 px, no claro e no escuro, uma vez por arquivo de dados.

O modelo mora em `assets/diagramas/` (o `fluxo.html`, o `tokens.css` e o motor de layout, quando embutido). Os dados
são um JSON no formato do `assets/diagramas/fluxo.json` (o `LEIA.md` ao lado diz os campos). A página se abre por
http, numa pasta temporária com o modelo e os dados, e o PNG sai com o `--disable-lcd-text`: sem a flag, o texto miúdo sai com franja de cor.

Uso:
  python -X utf8 diagrama_render.py [dados.json ...] [--saida <pasta>] [--embutir]
    sem dados: os de exemplo do modelo (fluxo.json, fluxo-mais.json)
    --saida: onde gravar <nome>-claro.png e <nome>-escuro.png (padrão: a pasta atual)
    --embutir: copia o primeiro arquivo de dados para dentro da página do modelo dele (o fluxo.html, ou o grafo.html
               quando o dado diz "modelo": "grafo"; a cópia que vale ao abrir o arquivo direto do disco)
"""
import argparse, functools, http.server, json, re, shutil, tempfile, threading
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
MODELO = SKILL / "assets" / "diagramas"
ARQUIVOS_DO_MODELO = ("fluxo.html", "grafo.html", "sequencia.html", "tokens.css", "elk.bundled.js")
PAGINAS = {"fluxo": "fluxo.html", "grafo": "grafo.html", "sequencia": "sequencia.html"}


def com_dados(s: str, dados: Path) -> str:
    """A página do modelo com a cópia embutida trocada pelos dados (a que vale ao abrir o arquivo direto do disco)."""
    obj = json.loads(Path(dados).read_text(encoding="utf-8"))
    if obj.get("modelo") == "sequencia" and obj.get("arquitetura"):
        # a sequência é vista da arquitetura: do disco a página não lê o outro JSON, então os nós vão junto, em "_nos"
        arq = json.loads((Path(dados).parent / obj["arquitetura"]).read_text(encoding="utf-8"))
        obj["_nos"] = {n["id"]: {k: n.get(k) for k in ("id", "titulo", "tipo", "tecnologia") if n.get(k)} for n in arq["nos"]}
    d = json.dumps(obj, ensure_ascii=False, indent=1)
    s2, n = re.subn(r'(<script type="application/json" id="dados-embutidos">\n).*?(\n</script>)',
                    lambda m: m.group(1) + d.replace("</", "<\\/") + m.group(2), s, flags=re.S)
    if n != 1:
        raise SystemExit('a página do modelo não tem a cópia embutida (<script id="dados-embutidos">)')
    return s2


def embutir(dados: Path, html: Path | None = None):
    html = html or MODELO / pagina_de(dados)
    s = html.read_text(encoding="utf-8")
    s2 = com_dados(s, dados)
    if s2 != s:
        html.write_bytes(s2.encode("utf-8"))


def pagina_para_projeto(dados: Path) -> str:
    """A página que o projeto recebe para um diagrama: o modelo certo (fluxo ou grafo) com os dados embutidos, para
    abrir do disco ao lado do tokens.css e do elk.bundled.js (o montar.py a grava em onboarding/diagramas/)."""
    return com_dados((MODELO / pagina_de(dados)).read_text(encoding="utf-8"), dados)


# o nome com que cada dado foi servido na pasta temporária (o caminho resolvido -> o nome), para dois arquivos de mesmo
# nome em pastas diferentes não se sobrescreverem; nome_de() devolve o nome a usar na página e na saída
SERVIDOS: dict = {}


def _livre(tmp: Path, nome: str) -> str:
    """O nome na pasta servida: o próprio, ou com -2, -3… quando já há outro arquivo com ele."""
    p = Path(nome); n = 2
    while (tmp / nome).exists():
        nome = f"{p.stem}-{n}{p.suffix}"; n += 1
    return nome


def nome_de(d: Path) -> str:
    return SERVIDOS.get(Path(d).resolve(), Path(d).name)


def pasta_servida(dados: list) -> Path:
    """Uma pasta temporária com o modelo e os dados, para a página ler o JSON por fetch. Dados de mesmo nome (de pastas
    diferentes) ganham nomes próprios; a arquitetura de que uma sequência é vista também, e o campo "arquitetura" da
    cópia passa a apontar para ela."""
    tmp = Path(tempfile.mkdtemp(prefix="diagrama-"))
    for nome in ARQUIVOS_DO_MODELO:
        if (MODELO / nome).exists():
            shutil.copy2(MODELO / nome, tmp / nome)
    arquiteturas = {}  # a arquitetura (resolvida) -> o nome já servido, para não copiar a mesma duas vezes
    for d in dados:
        d = Path(d)
        dado = json.loads(d.read_text(encoding="utf-8"))
        arq = dado.get("arquitetura")
        if arq and (d.parent / arq).exists():  # a sequência lê a arquitetura de que é vista
            fonte = (d.parent / arq).resolve()
            if fonte not in arquiteturas:
                arquiteturas[fonte] = _livre(tmp, Path(arq).name)
                shutil.copy2(fonte, tmp / arquiteturas[fonte])
            dado["arquitetura"] = arquiteturas[fonte]
        nome = _livre(tmp, d.name)
        if arq and dado.get("arquitetura") != arq:
            (tmp / nome).write_text(json.dumps(dado, ensure_ascii=False), encoding="utf-8")
        else:
            shutil.copy2(d, tmp / nome)
        SERVIDOS[d.resolve()] = nome
    return tmp


def servidor(raiz: Path):
    class Quieto(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    h = functools.partial(Quieto, directory=str(raiz))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def pagina_de(dados: Path) -> str:
    """O modelo da página pelo campo "modelo": o fluxo em passos (padrão), o grafo (a arquitetura e a árvore) ou a
    sequência (quem fala com quem, vista da arquitetura)."""
    return PAGINAS.get(json.loads(Path(dados).read_text(encoding="utf-8")).get("modelo", "fluxo"), "fluxo.html")


def abrir(pg, porta, nome_dados, pagina="fluxo.html"):
    pg.goto(f"http://127.0.0.1:{porta}/{pagina}?dados={nome_dados}")
    pg.wait_for_function("document.body.dataset.pronto", timeout=20000)
    if pg.evaluate("document.body.dataset.pronto") != "1":
        raise SystemExit(pg.evaluate("document.body.dataset.erro"))


def alvos_de(lista):
    return [Path(a).resolve() for a in lista] or [MODELO / "fluxo.json", MODELO / "fluxo-mais.json"]


def main():
    from playwright.sync_api import sync_playwright
    ap = argparse.ArgumentParser()
    ap.add_argument("dados", nargs="*")
    ap.add_argument("--saida", default=".")
    ap.add_argument("--embutir", action="store_true")
    a = ap.parse_args()
    alvos = alvos_de(a.dados)
    if a.embutir:
        embutir(alvos[0])
    saida = Path(a.saida); saida.mkdir(parents=True, exist_ok=True)
    raiz = pasta_servida(alvos)
    srv = servidor(raiz); porta = srv.server_address[1]
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch(args=["--disable-lcd-text"])
            for d in alvos:
                for tema, nome in (("light", "claro"), ("dark", "escuro")):
                    ctx = nav.new_context(viewport={"width": 1280, "height": 800}, color_scheme=tema)
                    pg = ctx.new_page(); abrir(pg, porta, nome_de(d), pagina_de(d))
                    arq = saida / f"{Path(nome_de(d)).stem}-{nome}.png"
                    pg.screenshot(path=str(arq), full_page=True); ctx.close()
                    print(arq)
            nav.close()
    finally:
        srv.shutdown(); shutil.rmtree(raiz, ignore_errors=True)


if __name__ == "__main__":
    main()
