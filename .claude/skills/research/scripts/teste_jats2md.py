"""Teste do jats2md.py, sem rede: um artigo JATS mínimo escrito aqui.

Uso: python -X utf8 .claude/skills/research/scripts/teste_jats2md.py

O jats2md.py converte o XML de artigo aberto (PMC e Europe PMC) na seção "Texto integral" das fichas e não tinha
teste. Este roda o script como a research roda (`python -I -X utf8`, por subprocesso) sobre um XML com título,
autores, resumo, seções aninhadas, a seção "Associated Data" (que fica de fora), lista, tabela com rowspan e
colspan, a barra vertical escapada na célula, fórmula em MathML, figura pela legenda, sub e sup, citação recuada,
notas e referências; e o XML sem corpo, que para com a mensagem. Não muda o script.
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent

XML = """<?xml version="1.0"?>
<article xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">
 <front><article-meta>
  <title-group><article-title>Um estudo <italic>de</italic> teste</article-title></title-group>
  <contrib-group>
   <contrib contrib-type="author"><name><surname>Silva</surname><given-names>Ana</given-names></name></contrib>
   <contrib contrib-type="author"><name><surname>Souza</surname><given-names>Bruno</given-names></name></contrib>
   <contrib contrib-type="editor"><name><surname>Editora</surname><given-names>Carla</given-names></name></contrib>
  </contrib-group>
  <abstract><p>O resumo , com espaço antes da vírgula .</p></abstract>
 </article-meta></front>
 <body>
  <sec><title>Introdução</title>
   <p>Água H<sub>2</sub>O e área m<sup>2</sup>.</p>
   <sec><title>Detalhe</title><p>Um parágrafo aninhado.</p></sec>
  </sec>
  <sec><title>Associated Data</title><p>Não pode aparecer.</p></sec>
  <sec><title>Métodos</title>
   <list><list-item><p>primeiro</p></list-item><list-item><p>segundo</p></list-item></list>
   <table-wrap><label>Tabela 1</label><caption><p>Os grupos</p></caption>
    <table><tr><th rowspan="2">A</th><th colspan="2">B</th></tr><tr><td>b1</td><td>x | y</td></tr></table>
   </table-wrap>
   <disp-formula><label>(1)</label><mml:math><mml:mfrac><mml:mi>a</mml:mi><mml:mi>b</mml:mi></mml:mfrac></mml:math></disp-formula>
   <fig><label>Figura 1</label><caption><p>Uma legenda.</p></caption></fig>
   <disp-quote><p>Uma citação.</p></disp-quote>
  </sec>
 </body>
 <back>
  <fn-group><fn><label>1</label><p>Uma nota.</p></fn></fn-group>
  <ref-list><ref><label>1.</label><mixed-citation>Autor A. Título. 2020.</mixed-citation></ref></ref-list>
 </back>
</article>
"""


class TesteJats(unittest.TestCase):
    def converter(self, xml):
        with tempfile.TemporaryDirectory() as t:
            src, dst = Path(t) / "a.xml", Path(t) / "a.md"
            src.write_text(xml, encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(AQUI / "jats2md.py"), str(src), str(dst)],
                               capture_output=True, text=True, encoding="utf-8")
            return r, (dst.read_text(encoding="utf-8") if dst.exists() else None)

    def test_artigo(self):
        r, md = self.converter(XML)
        self.assertEqual(r.returncode, 0, r.stderr)
        linhas = md.splitlines()
        self.assertEqual(linhas[0], "**Um estudo de teste**")
        self.assertIn("Ana Silva, Bruno Souza", md)
        self.assertNotIn("Carla", md)                         # editor não é autor
        self.assertIn("### Abstract", md)
        self.assertIn("O resumo, com espaço antes da vírgula.", md)
        self.assertIn("### Introdução", md)
        self.assertIn("#### Detalhe", md)                     # a seção aninhada desce um nível
        self.assertIn("H_2O", md)
        self.assertIn("m^2", md)
        self.assertNotIn("Não pode aparecer", md)             # Associated Data fica de fora
        self.assertIn("- primeiro\n- segundo", md)
        self.assertIn("**Tabela 1 Os grupos**", md)
        self.assertIn("| A | B |  |", md)
        self.assertIn("|  | b1 | x \\| y |", md)             # rowspan vira célula vazia; a barra se escapa
        self.assertIn("(a)/(b) (", md)  # a fórmula linearizada e o rótulo; a forma do rótulo está no teste abaixo
        self.assertIn("**[Figura]** Figura 1 Uma legenda.", md)
        self.assertIn("> Uma citação.", md)
        self.assertIn("### Notes", md)
        self.assertIn("1 Uma nota.", md)
        self.assertIn("### References", md)
        self.assertIn("- 1. Autor A. Título. 2020.", md)

    def test_rotulo_da_formula_sem_parentese_dobrado(self):
        # o rótulo que já vem com parênteses saía com dois, "((1))" (achado menor, corrigido em 21/11)
        r, md = self.converter(XML)
        self.assertIn("(a)/(b) (1)\n", md)
        self.assertNotIn("((1))", md)
        # o rótulo sem parênteses ganha os parênteses uma vez só
        r, md = self.converter(XML.replace("<label>(1)</label><mml:math>", "<label>2</label><mml:math>"))
        self.assertIn("(a)/(b) (2)\n", md)

    def test_sem_corpo_para(self):
        r, md = self.converter('<article><front><article-meta><abstract><p>só o resumo</p></abstract></article-meta></front></article>')
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("não traz o texto integral", r.stderr)
        self.assertIsNone(md)


if __name__ == "__main__":
    unittest.main(verbosity=2)
