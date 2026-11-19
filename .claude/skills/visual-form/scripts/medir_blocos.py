"""Confere a posição do texto de uma peça antes de exportar: depois do assentamento do caderno.js, mede em cada
tela a primeira linha de base e o número de linhas de cada .bloco, no navegador (shot-scraper), não a olho.

Uso: python medir_blocos.py <pasta-da-peca> [arquivo.html] [--ajustar]
O arquivo padrão é slides.html. Um bloco com data-base="Y" diz onde a primeira linha de base deve cair (em px,
na linha do papel; o caderno.js encosta a base 2 px acima dela) e sai marcado ok ou FORA. Com --ajustar, o top
de cada bloco FORA muda para a base cair no alvo, só na tela em que a página e o HTML contam os mesmos blocos com
data-base em número (senão, AVISO e a tela fica para a mão); rodar de novo para conferir. Serve ao papel com linhas
fortes, em que a posição feita a olho deixa linha cortando palavra.

Antes de medir cada tela, pede as fontes do texto dela e confere se carregaram (fontes.py), antes do prepararSlide
(o assentamento já mede) e de novo depois dele (o texto que ele mostra ou põe na tela). Se alguma não carregou, as
medidas seriam da fonte de reserva: sai ERRO fonte_nao_carregada, nenhuma medida, nada ajustado, código 3 (a medida
na fonte de reserva, sem avisar, é o erro que isto impede). O bloco sem texto (só desenho) sai "sem texto", sem linha de base.
"""
import json, re, subprocess, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "slides-export", "scripts"))   # fontes.py, da slides-export
from fontes import CARREGAR_FONTES
args = [a for a in sys.argv[1:] if not a.startswith("--")]
pasta, html, ajustar = args[0], (args[1] if len(args) > 1 else "slides.html"), "--ajustar" in sys.argv
JS = r"""
async () => {
  const carregarFontes = """ + CARREGAR_FONTES + r""";
  const out = [], faltam = []; const slides = [...document.querySelectorAll('.slide')];
  for (let i = 0; i < slides.length; i++) {
    slides.forEach((s, j) => s.classList.toggle('active', j === i));
    const vistas = new Set();
    const confere = async () => { for (const f of await carregarFontes(slides[i])) {   // a chave do fontes.py, sem o tamanho
      if (!vistas.has(f.chave)) { vistas.add(f.chave); faltam.push({slide: i + 1, ...f}); } } };
    await confere();   // antes do assentamento, que já mede
    if (window.prepararSlide) await window.prepararSlide(i);
    await confere();   // o texto que o prepararSlide mostrou ou pôs na tela
    const s = slides[i], top = s.getBoundingClientRect().top;
    let k = 0;
    for (const el of s.querySelectorAll('.bloco')) {
      const r = el.getBoundingClientRect(), lh = parseFloat(getComputedStyle(el).lineHeight);
      const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let t = null;
      while (w.nextNode()) if (w.currentNode.textContent.trim()) { t = w.currentNode; break; }
      const sonda = document.createElement('span'); sonda.style.cssText = 'display:inline-block;width:0;height:0;vertical-align:baseline';
      let base = null;   // o bloco só com desenho (svg, img) não tem linha de base
      if (t) { t.parentNode.insertBefore(sonda, t); base = Math.round((sonda.getBoundingClientRect().top - top) * 10) / 10; sonda.remove(); }
      // k conta só os blocos com data-base em número (o 0 também), os mesmos que o --ajustar acha no HTML
      const db = el.getAttribute('data-base'), valido = db !== null && /^\d+$/.test(db);
      out.push({slide: i + 1, k: valido ? k++ : null, cls: el.className, alvo: valido ? +db : null, base,
                invalido: db !== null && !valido ? db : null,
                linhas: Math.round(r.height / lh), topo: Math.round(r.top - top), pe: Math.round(r.bottom - top), texto: el.textContent.slice(0, 40)});
    }
  }
  return {blocos: out, faltam};
}
"""
r = subprocess.run(["shot-scraper", "javascript", html, JS], cwd=pasta, capture_output=True, text=True, encoding="utf-8")
if r.returncode:
    if "Timeout" in r.stderr:
        print("A página não terminou de carregar no prazo do shot-scraper: um recurso não respondeu (a fonte da web ou o "
              "@import com a rede travada?). Nenhuma medida.")
    print(r.stderr); sys.exit(1)
res = json.loads(r.stdout)
if res["faltam"]:
    for f in res["faltam"]:
        print(f"ERRO fonte_nao_carregada S{f['slide']} {f['familia']} ({f['fonte']}) | {f['amostra']}")
    print("As medidas sairiam na fonte de reserva: nenhuma medida e nada ajustado. Conferir a rede (a fonte da web) "
          "ou o @font-face, e rodar de novo.")
    sys.exit(3)
dados = res["blocos"]
for d in dados:
    if d["base"] is None:
        print(f"S{d['slide']} {d['cls']:22s} sem texto (sem linha de base) topo {d['topo']:5d} pe {d['pe']:5d}")
        continue
    ok = "" if d["alvo"] is None else ("ok" if abs(d["base"] - (d["alvo"] - 2)) < 1 else f"FORA (alvo {d['alvo']})")
    if d["invalido"] is not None:
        ok = f"AVISO data-base=\"{d['invalido']}\" não é número: sem alvo"
    print(f"S{d['slide']} {d['cls']:22s} base {d['base']:7.1f} linhas {d['linhas']} topo {d['topo']:5d} pe {d['pe']:5d} {ok} | {d['texto']}")
if ajustar:
    p = os.path.join(pasta, html); s = open(p, encoding="utf-8", newline="").read()  # newline="": preserva o fim de linha do arquivo
    secs = s.split('<section class="slide')
    for d in dados:
        if d["alvo"] is None or d["base"] is None: continue
        delta = (d["alvo"] - 2) - d["base"]
        if abs(delta) < 1: continue
        sec = secs[d["slide"]]
        blocos = list(re.finditer(r'data-base="(\d+)" style="top:(-?\d+)px', sec))
        # o k do DOM só casa com a ordem do HTML se os dois contam os mesmos blocos: todo data-base em número da tela
        # seguido de style="top", e nenhum posto pelo script da peça. Senão, a tela inteira fica para a mão.
        no_dom = sum(1 for e in dados if e["slide"] == d["slide"] and e["k"] is not None)
        no_html = len(re.findall(r'data-base="\d+"', sec))
        m = blocos[d["k"]] if len(blocos) == no_html == no_dom and d["k"] < len(blocos) else None
        if m is None or int(m.group(1)) != d["alvo"]:
            print(f"AVISO S{d['slide']} não ajustei: a tela tem {no_dom} bloco(s) com data-base na página e {no_html} no HTML, "
                  f"{len(blocos)} na ordem data-base=\"N\" style=\"top:...px\" (o atributo em outra ordem, ou o bloco posto "
                  f"pelo script da peça); ajustar à mão | {d['texto']}")
            continue
        novo = int(m.group(2)) + round(delta)
        sec = sec[:m.start(2)] + str(novo) + sec[m.end(2):]
        secs[d["slide"]] = sec
    open(p, "w", encoding="utf-8", newline="").write('<section class="slide'.join(secs))
    print("ajustado")
