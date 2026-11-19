"""O teste das duas ferramentas que preparam o material da I2 (`prepara_i2.py` e `folha_de_contato.py`).
Sem rede nem navegador, em segundos.

    python -X utf8 .claude/skills/visual-form/scripts/teste_ferramentas_i2.py
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

AQUI = Path(__file__).resolve().parent


def roda(script, *args):
    return subprocess.run([sys.executable, "-X", "utf8", str(AQUI / script), *map(str, args)],
                          capture_output=True, text=True, encoding="utf-8")


class AsFerramentas(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.telas = self.d / "telas"
        self.telas.mkdir()
        for i, cor in enumerate(["red", "green", "blue"], 1):
            im = Image.new("RGB", (108, 135), "white")
            im.paste(Image.new("RGB", (54, 67), cor), (0, 0))   # o quadrante de cima à esquerda tem a cor
            im.save(self.telas / f"slide-{i:02}.jpg", quality=95)

    def test_zoom_quatro_quadrantes_ampliados(self):
        r = roda("prepara_i2.py", "zoom", self.telas, self.d / "zoom")
        self.assertEqual(r.returncode, 0, r.stderr)
        saidas = sorted((self.d / "zoom").glob("*.jpg"))
        self.assertEqual(len(saidas), 12)
        a = Image.open(self.d / "zoom/slide-01-a-sup-esq.jpg")
        self.assertEqual(a.size, (108, 135), "cada quadrante volta ao tamanho da tela: ampliado 2x")
        r_, g, b = a.convert("RGB").getpixel((54, 67))
        self.assertGreater(r_, 200)
        self.assertLess(g, 80)
        d = Image.open(self.d / "zoom/slide-01-d-inf-dir.jpg").convert("RGB").getpixel((54, 67))
        self.assertTrue(all(c > 200 for c in d), "o quadrante de baixo à direita é só o branco")

    def test_semtexto_apaga_o_texto_e_mantem_os_caminhos(self):
        html = self.d / "peca" / "slides.html"
        html.parent.mkdir()
        html.write_text("<!doctype html><html><head><link rel='stylesheet' href='../design/caderno.css'></head>"
                        "<body><p>texto</p></body></html>", encoding="utf-8")
        r = roda("prepara_i2.py", "semtexto", html, self.d / "sem", "ng")
        self.assertEqual(r.returncode, 0, r.stderr)
        out = (self.d / "sem/ng.html").read_text(encoding="utf-8")
        self.assertIn(f'<base href="{html.parent.resolve().as_uri()}/">', out)
        self.assertIn("color:transparent", out)
        self.assertLess(out.index("<base"), out.index("caderno.css"), "o <base> vem antes do primeiro caminho relativo")
        self.assertLess(out.index('id="teste-sem-texto"'), out.index("</head>"))

    def test_semtexto_sem_head(self):
        html = self.d / "x.html"
        for corpo in ("<p>sem head</p>", "<html><head><title>x</title><body><p>sem fecho do head</p></body></html>"):
            html.write_text(corpo, encoding="utf-8")
            r = roda("prepara_i2.py", "semtexto", html, self.d / "sem", "x")
            self.assertNotEqual(r.returncode, 0, corpo)
            self.assertFalse((self.d / "sem/x.html").exists(), "nada se grava quando falta o head")

    def test_semtexto_head_com_atributo_e_texto_gerado(self):
        html = self.d / "y.html"
        html.write_text("<html><HEAD lang='pt'><style>.p li::before{content:'1.';color:blue}</style></HEAD>"
                        "<body><ol class='p'><li>a</li></ol></body></html>", encoding="utf-8")
        r = roda("prepara_i2.py", "semtexto", html, self.d / "sem", "y")
        self.assertEqual(r.returncode, 0, r.stderr)
        out = (self.d / "sem/y.html").read_text(encoding="utf-8")
        self.assertIn("*::before", out)
        self.assertLess(out.index("<base"), out.index("</HEAD>"))
        self.assertLess(out.index('id="teste-sem-texto"'), out.index("</HEAD>"))

    def test_uso_sem_argumentos(self):
        self.assertNotEqual(roda("prepara_i2.py").returncode, 0)
        self.assertNotEqual(roda("prepara_i2.py", "semtexto", "a.html").returncode, 0)

    def test_folha_de_contato_uma_linha_por_peca(self):
        outra = self.d / "outra"
        outra.mkdir()
        for i in (1, 2):
            Image.new("RGB", (108, 135), "black").save(outra / f"slide-{i:02}.jpg")
        saida = self.d / "folha.jpg"
        r = roda("folha_de_contato.py", saida, f"nova={self.telas}", f"publicada={outra}")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(Image.open(saida).size, (12 + 3 * (240 + 12), 2 * (300 + 40 + 12) + 12))


if __name__ == "__main__":
    unittest.main(verbosity=2)
