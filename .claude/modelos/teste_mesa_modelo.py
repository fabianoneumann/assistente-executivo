"""Teste do modelo de mesa (`mesa-modelo.html`), no Chromium do Playwright, com um banco falso em memória.

Faz a conferência que o topo do modelo exige antes de entregar o link de uma mesa:
1. digitar um comentário num item e clicar noutra opção do mesmo item: o texto fica;
2. digitar noutro item e clicar numa opção de um terceiro: os dois textos ficam;
3. recarregar (uma página nova com o mesmo banco): as escolhas e os comentários voltam;
4. o banco tem a escolha e o comentário de cada item.

Uso: python -X utf8 .claude/modelos/teste_mesa_modelo.py [caminho da mesa.html]  (sem argumento, o modelo).
Serve também para conferir uma mesa feita a partir do modelo, desde que ela tenha pelo menos três itens.
Sem rede: as fontes do Google não carregam, e a página segue com a fonte de reserva. Código 0 passou, 1 falhou.
"""
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ALVO = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("mesa-modelo.html")

# o banco falso: a mesma interface que a página usa (claude.use("db") -> collection -> doc.set / onSnapshot)
FALSO = """
window.__store = window.__store || {};
window.claude = { use: async (nome) => {
  if (nome !== "db") return null;
  const ouvintes = [];
  const avisa = () => { const docs = Object.entries(window.__store).map(([id, d]) => ({id, data: () => d}));
                        ouvintes.forEach(f => f({docs})); };
  return { collection: (c) => ({
    doc: (id) => ({ set: async (d) => { window.__store[id] = JSON.parse(JSON.stringify(d)); avisa(); } }),
    onSnapshot: (f) => { ouvintes.push(f); setTimeout(avisa, 0); return () => {}; }
  }) };
}};
"""

HTML_BASE = ('<!doctype html><html><head><meta charset=utf-8></head><body>{corpo}</body></html>')


def pagina(ctx, store):
    pg = ctx.new_page()
    pg.route("**/fonts.googleapis.com/**", lambda r: r.abort())
    falso = f"<script>window.__store = {json.dumps(store)};{FALSO}</script>"
    pg.set_content(HTML_BASE.format(corpo=falso + ALVO.read_text(encoding="utf-8")))
    pg.wait_for_function("document.getElementById('estado').className === 'ok'", timeout=5000)
    return pg


def main():
    falhas = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context()
        pg = pagina(ctx, {})
        ids = pg.eval_on_selector_all(".item", "els => els.map(e => e.id)")
        if len(ids) < 1:
            print("FALHA: a mesa não tem itens"); return 1
        a = ids[0]; b = ids[1] if len(ids) > 1 else ids[0]; c = ids[2] if len(ids) > 2 else ids[0]
        # 1. digitar no item a, sem sair do campo, e clicar noutra opção do mesmo item
        pg.click(f"#{a}-c"); pg.keyboard.type("comentário do primeiro")
        pg.check(f"#{a}-1" if pg.query_selector(f"#{a}-1") else f"#{a}-n")
        if pg.input_value(f"#{a}-c") != "comentário do primeiro":
            falhas.append("1: o comentário do item sumiu ao clicar numa opção dele")
        # 2. digitar no item b e clicar numa opção do item c
        pg.click(f"#{b}-c"); pg.keyboard.type("comentário do segundo")
        pg.check(f"#{c}-0")
        for i, txt in ((a, "comentário do primeiro"), (b, "comentário do segundo")):
            if pg.input_value(f"#{i}-c") != txt:
                falhas.append(f"2: o comentário de {i} sumiu ao clicar noutro item")
        pg.wait_for_timeout(900)  # a espera do autosave é de 600 ms
        store = pg.evaluate("window.__store")
        # 4. o banco tem a escolha e o comentário
        if not (store.get(a, {}).get("comentario") == "comentário do primeiro" and store.get(a, {}).get("escolha")):
            falhas.append(f"4: o banco não tem a escolha e o comentário de {a}: {store.get(a)}")
        if store.get(b, {}).get("comentario") != "comentário do segundo":
            falhas.append(f"4: o banco não tem o comentário de {b} (gravar ao digitar)")
        # 3. recarregar: página nova com o mesmo banco
        pg2 = pagina(ctx, store)
        pg2.wait_for_timeout(200)
        if pg2.input_value(f"#{a}-c") != "comentário do primeiro" or pg2.input_value(f"#{b}-c") != "comentário do segundo":
            falhas.append("3: os comentários não voltaram ao recarregar")
        if not pg2.is_checked(f"#{c}-0"):
            falhas.append("3: a escolha não voltou ao recarregar")
        nav.close()
    for f in falhas:
        print("FALHA", f)
    print("ok" if not falhas else f"{len(falhas)} falha(s)")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
