"""O teste do `mede_forma.py`: os dois modos concordam no que contam pelas classes, e o modo sem navegador não confunde
HTML torto com medida.

    python -X utf8 .claude/skills/visual-form/scripts/teste_mede_forma.py [--sem-navegador]

Com navegador (o Chromium do Playwright, uns 15 s): o post de exemplo da série de exemplo medido nos dois modos dá os
mesmos números no que se conta pelas classes, com a margem e o maior desenho medidos; e a fonte que não carrega para a
medida (código 3). Sem navegador: o parser em páginas mínimas feitas aqui.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[3]
EXEMPLO = RAIZ / "marketing/social-media/carousels/series/exemplo/exemplo-de-post/slides.html"
sys.path.insert(0, str(AQUI))
import mede_forma  # noqa: E402

SEM_NAVEGADOR = "--sem-navegador" in sys.argv
if SEM_NAVEGADOR:
    sys.argv.remove("--sem-navegador")


def pagina(corpo, estilo=""):
    d = Path(tempfile.mkdtemp())
    p = d / "slides.html"
    p.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{estilo}</style></head><body>{corpo}"
                 "</body></html>", encoding="utf-8", newline="\n")
    return p


def roda(*args):
    return subprocess.run([sys.executable, "-X", "utf8", str(AQUI / "mede_forma.py"), *args],
                          capture_output=True, text=True, encoding="utf-8")


class OEstatico(unittest.TestCase):
    def test_conta_pelas_classes(self):
        p = pagina("""
<section class="slide s1"><h1 class="titulo">T</h1><div class="bloco destaque"><p>frase</p></div>
  <p class="corpo">um <b>dois</b> <strong>três</strong></p><p class="corpo">   </p>
  <img class="desenho" src="x.png"><br><span class="circulo">c</span><span class="nota margem">n</span></section>
<section class="slide s2 transborda"><div class="citacao">cit</div><p class="destaque citacao">duas classes, conta uma</p>
  <svg class="traco"><path d="M0 0"/><text class="sublinha">s</text></svg><b>fora do corpo</b></section>""")
        a, b = mede_forma.medir_estatico(p)
        self.assertEqual((a["destaque_manuscrito"], a["negrito"], a["corpo"]), (1, 2, 1))
        self.assertEqual(a["marcas"], {"circulo": 1, "sublinha": 0, "marca_texto": 0, "notas_acento": 1})
        self.assertIsNone(a["transborda"], "o caderno.js marca o transborda em tempo de execução: no estático, ausente")
        self.assertEqual((b["destaque_manuscrito"], b["negrito"], b["corpo"], b["transborda"]), (2, 0, 0, None))
        self.assertEqual(b["marcas"]["sublinha"], 1)

    def test_corpo_aninhado_e_vazio(self):
        p = pagina('<div class="slide"><div class="corpo"><p class="corpo">x</p></div><p class="corpo"></p></div>')
        (m,) = mede_forma.medir_estatico(p)
        self.assertEqual(m["corpo"], 2, "como o filtro do navegador: os dois .corpo com texto, o vazio fora")

    def test_classe_parecida_nao_abre_tela(self):
        p = pagina('<section class="slide"><div class="slide-numero destaque">1</div></section>')
        (m,) = mede_forma.medir_estatico(p)
        self.assertEqual(m["destaque_manuscrito"], 1)

    def test_sem_tela(self):
        self.assertEqual(roda(str(pagina("<p>nada</p>")), "--estatico").returncode, 2)
        self.assertEqual(roda(str(Path(tempfile.mkdtemp()) / "nao-existe.html"), "--estatico").returncode, 2)

    def test_grava_json_em_lf(self):
        with tempfile.TemporaryDirectory() as d:
            saida = Path(d) / "m.json"
            r = roda(str(pagina('<section class="slide"><p class="destaque">x</p></section>')), str(saida), "--estatico")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertNotIn(b"\r", saida.read_bytes())
            self.assertEqual(json.loads(saida.read_text(encoding="utf-8"))[0]["destaque_manuscrito"], 1)


@unittest.skipIf(SEM_NAVEGADOR, "sem navegador")
class ONavegador(unittest.TestCase):
    def test_navegador_e_estatico_concordam_no_exemplo(self):
        with tempfile.TemporaryDirectory() as d:
            saida = Path(d) / "m.json"
            r = roda(str(EXEMPLO), str(saida))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            nav = json.loads(saida.read_text(encoding="utf-8"))
            est = mede_forma.medir_estatico(EXEMPLO)
            self.assertEqual(len(nav), len(est))
            for x, y in zip(nav, est):
                for k in ("negrito", "corpo", "marcas", "destaque_manuscrito"):
                    self.assertEqual(x[k], y[k], f"tela {x['tela']}, {k}: navegador e estático discordam")
                self.assertIsNotNone(x["margem_esq_min"], "no navegador, a margem se mede")
            self.assertEqual(nav[1]["maior_desenho"]["quem"], "traco desenho")
            self.assertEqual(nav[1]["negrito"], 1)

    def test_tela_sem_texto_tem_margem_nula(self):
        with tempfile.TemporaryDirectory() as d:
            saida = Path(d) / "m.json"
            p = pagina('<section class="slide"><svg class="traco" width="300" height="200"></svg></section>'
                       '<section class="slide"><svg data-desenho width="200" height="100"></svg><p>x</p></section>')
            r = roda(str(p), str(saida))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            a, b = json.loads(saida.read_text(encoding="utf-8"))
            self.assertIsNone(a["margem_esq_min"])
            self.assertEqual(a["maior_desenho"]["quem"], "traco")
            self.assertIsNotNone(b["margem_esq_min"])
            self.assertEqual(b["maior_desenho"]["quem"], "svg", "o desenho sem id nem classe sai pelo nome da tag")

    def test_fonte_que_nao_carrega(self):
        p = pagina('<section class="slide"><p class="corpo">um texto qualquer para medir</p></section>',
                   "@font-face{font-family:'Falta';src:url('nao-existe.woff2')} .slide{font-family:'Falta',serif}")
        r = roda(str(p))
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)
        self.assertIn("fonte_nao_carregada", r.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
