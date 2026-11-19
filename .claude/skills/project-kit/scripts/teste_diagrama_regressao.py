"""O teste da regressão visual (`diagrama_regressao.py`), contra a linha de base guardada, sem mexer nela:
  - a mesma figura renderizada de novo sai igual (0% dos pixels), só no ambiente que gerou a base (o ambiente.json);
    noutro ambiente, o caso sai como AVISO, porque a diferença pode vir do sistema ou do Chromium;
  - um rótulo de saída de decisão movido 40 px para baixo e 40 para a esquerda é pego (REG-PIXELS);
  - o fluxo comparado com a base do fluxo com dois passos a mais é pego pela altura (REG-ALTURA);
  - a figura 1% mais alta, com a diferença só na faixa acrescentada, é pega (REG-PIXELS): a faixa conta inteira;
  - a base com outra largura é recusada (REG-BASE-INVALIDA).
Uso: python -X utf8 teste_diagrama_regressao.py  -> sai com 1 se algum caso falhar."""
import shutil, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import diagrama_render as render  # noqa: E402
import diagrama_regressao as reg  # noqa: E402


def foto(pg, porta, dado: Path, arq: Path, mexe: str | None = None):
    render.abrir(pg, porta, render.nome_de(dado), render.pagina_de(dado))
    if mexe:
        pg.evaluate(mexe)
    pg.screenshot(path=str(arq), full_page=True)


def main():
    from playwright.sync_api import sync_playwright
    falhou = 0
    prioridade, fluxo = render.MODELO / "prioridade.json", render.MODELO / "fluxo.json"
    tmp = Path(tempfile.mkdtemp(prefix="teste-regressao-"))
    raiz = render.pasta_servida([prioridade, fluxo]); srv = render.servidor(raiz); porta = srv.server_address[1]
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch(args=["--disable-lcd-text"])
            ctx = nav.new_context(viewport={"width": 1280, "height": 800}, color_scheme="light"); pg = ctx.new_page()
            foto(pg, porta, prioridade, tmp / "igual.png")
            foto(pg, porta, prioridade, tmp / "mexido.png", """() => { const r = document.querySelector('.grafo .rotulo-aresta[data-saida]');
                r.style.top = (parseFloat(r.style.top) + 40) + 'px'; r.style.left = (parseFloat(r.style.left) - 40) + 'px'; }""")
            foto(pg, porta, fluxo, tmp / "fluxo.png")
            cmp = nav.new_page()
            mesmo_ambiente = reg.ambiente_igual(nav)[0]
            # a figura 1% mais alta, branca na faixa nova; e uma base de 200 px de largura
            alta = tmp / "alta.png"; estreita = tmp / "base-estreita.png"
            png = cmp.evaluate("""async (src) => { const i = new Image(); await new Promise(ok => { i.onload = ok; i.src = src; });
                const c = document.createElement('canvas'); c.width = i.width; c.height = Math.round(i.height * 1.01);
                const x = c.getContext('2d'); x.fillStyle = '#000'; x.fillRect(0, 0, c.width, c.height); x.drawImage(i, 0, 0);
                const e = document.createElement('canvas'); e.width = 200; e.height = 100;
                return [c.toDataURL('image/png'), e.toDataURL('image/png')]; }""", reg.data_url(tmp / "igual.png"))
            import base64
            alta.write_bytes(base64.b64decode(png[0].split(",", 1)[1])); estreita.write_bytes(base64.b64decode(png[1].split(",", 1)[1]))
            casos = [
                ("a mesma figura sai igual", tmp / "igual.png", "prioridade-claro.png",
                 (lambda r: not r["regressao"] and r["fracao"] == 0) if mesmo_ambiente else None),
                ("a figura 1% mais alta, com a diferença só na faixa nova, é pega", alta, "prioridade-claro.png", lambda r: r.get("codigo") == "REG-PIXELS"),
                ("a base de outra largura é recusada", tmp / "igual.png", estreita, lambda r: r.get("codigo") == "REG-BASE-INVALIDA"),
                ("o rótulo movido 40 px é pego", tmp / "mexido.png", "prioridade-claro.png", lambda r: r.get("codigo") == "REG-PIXELS"),
                ("a figura de outra altura é pega", tmp / "fluxo.png", "fluxo-mais-claro.png", lambda r: r.get("codigo") == "REG-ALTURA"),
            ]
            for nome, nova, base, ok_se in casos:
                r = reg.comparar(cmp, nova, base if isinstance(base, Path) else reg.BASE / base, 0.0001); r.pop("diferenca", None)
                if ok_se is None:
                    print(f"AVISO {nome}: outro ambiente que o da base, sem exigir 0% ({r.get('fracao')})"); continue
                ok = ok_se(r); falhou += not ok
                print(("ok  " if ok else "FALHA ") + f"{nome}: {r}")
            nav.close()
    finally:
        srv.shutdown(); shutil.rmtree(raiz, ignore_errors=True); shutil.rmtree(tmp, ignore_errors=True)
    print("tudo certo" if not falhou else f"{falhou} falha(s)")
    sys.exit(1 if falhou else 0)


if __name__ == "__main__":
    main()
