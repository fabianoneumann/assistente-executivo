"""Teste do calibra_parafrase.py, sem rede nem vault: uma fonte plantada, uma ficha colada e uma em palavras próprias.

    python -X utf8 .claude/skills/research/scripts/teste_calibra_parafrase.py
"""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("calibra_parafrase", AQUI / "calibra_parafrase.py")
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)

FONTE = """A validade de conteúdo mede quanto os itens de um instrumento representam o construto que se quer medir.
Os especialistas julgam cada item quanto à clareza, à pertinência e à relevância para o público da pesquisa.
O índice de validade de conteúdo soma as notas três e quatro e divide pelo número total de especialistas consultados.
Recomenda-se um mínimo de cinco juízes e um máximo de dez para que a concordância tenha algum sentido estatístico.
Quando o índice fica abaixo de oito décimos, o item deve ser revisto ou retirado da versão final do instrumento.
A adaptação cultural exige tradução, retrotradução e um comitê que compare as versões antes do pré-teste com leitores.
"""

FRONT = "---\ntitulo: \"t\"\ntipo: artigo\n---\n\n"

COLADA = FRONT + """Os especialistas julgam cada item quanto à clareza, à pertinência e à relevância para o público da pesquisa.
O índice de validade de conteúdo soma as notas três e quatro e divide pelo número total de especialistas.
Recomenda-se um mínimo de cinco juízes e um máximo de dez para que a concordância tenha sentido estatístico.
Quando o índice fica abaixo de oito décimos, o item deve ser revisto ou retirado da versão final.
"""

PROPRIA = FRONT + """Para saber se um questionário cobre o que promete, um grupo pequeno de juízes dá nota a cada pergunta.
A conta é simples: a fração de juízes que deram nota alta; abaixo de um corte, a pergunta muda ou cai.
Levar o questionário a outra língua pede ida e volta da tradução e uma conversa entre as versões.
"""


class TesteCalibra(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        (d / "fonte.txt").write_text(FONTE, encoding="utf-8")
        (d / "colada.md").write_text(COLADA, encoding="utf-8")
        (d / "propria.md").write_text(PROPRIA, encoding="utf-8")
        self.gab = [
            {"id": "colada", "ficha": str(d / "colada.md"), "fontes": [str(d / "fonte.txt")], "veredito": "colada", "grupo": "g"},
            {"id": "propria", "ficha": str(d / "propria.md"), "fontes": [str(d / "fonte.txt")], "veredito": "ok", "grupo": "g"},
            {"id": "sem-ficha", "ficha": str(d / "nao-existe.md"), "fontes": [str(d / "fonte.txt")], "veredito": "ok", "grupo": "g"},
            {"id": "sem-fonte", "ficha": str(d / "propria.md"), "fontes": [str(d / "nao-existe.txt")], "veredito": "ok", "grupo": "g"},
        ]

    def tearDown(self):
        self.tmp.cleanup()

    def test_padrao_separa_colada_de_propria(self):
        medidos = C.mede(self.gab)
        _, resumo = C.tabela(medidos)
        r = resumo[("g", "0.7/3")]
        self.assertEqual((r["vp"], r["fn"], r["fp"]), (1, 0, 0))

    def test_k_alto_demais_perde_a_colada(self):
        _, resumo = C.tabela(C.mede(self.gab))
        self.assertEqual(resumo[("g", "0.7/4")]["vp"], 1)  # quatro seguidas na ficha colada
        self.assertEqual(resumo[("g", "0.9/4")]["fn"] + resumo[("g", "0.9/4")]["vp"], 1)

    def test_erro_de_entrada_fica_fora_da_conta(self):
        medidos = C.mede(self.gab)
        txt, resumo = C.tabela(medidos)
        self.assertIn("sem-ficha", txt)
        self.assertIn("sem-fonte", txt)
        r = resumo[("g", "0.7/3")]
        self.assertEqual(r["vp"] + r["fn"] + r["fp"] + r["vn"], 2)

    def test_fonte_que_falha_tira_a_ficha_da_conta(self):
        # a colada com uma fonte boa e outra que não existe: fica sem medida, e não vira negativa nem positiva
        g = dict(self.gab[0], id="mista", fontes=[self.gab[0]["fontes"][0], str(Path(self.tmp.name) / "falta.txt")])
        txt, resumo = C.tabela(C.mede([g, self.gab[1]]))
        self.assertIn("mista", txt)
        r = resumo[("g", "0.7/3")]
        self.assertEqual((r["vp"], r["fn"], r["vn"]), (0, 0, 1))

    def test_gabarito_mal_formado_sai_com_2(self):
        d = Path(self.tmp.name)
        for linha in ("[]", '{"id": "x", "ficha": "f.md"}', '{"id": "x", "ficha": "f.md", "fontes": "f.txt", "veredito": "ok"}'):
            (d / "ruim.jsonl").write_text(linha, encoding="utf-8")
            sys.argv = ["x", "--gabarito", str(d / "ruim.jsonl")]
            self.assertEqual(C.principal(), 2, linha)

    def test_ficha_de_revisao_git_lida_do_repositorio(self):
        import subprocess
        repo = Path(self.tmp.name) / "repo"
        repo.mkdir()
        git = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=repo,
                                        check=True, capture_output=True)
        git("init", "-q")
        (repo / "f.md").write_text(COLADA, encoding="utf-8")
        git("add", "f.md")
        git("commit", "-q", "-m", "antes")
        (repo / "f.md").write_text(PROPRIA, encoding="utf-8")  # a versão de agora é outra: o teste lê a antiga
        antigo, C.VAULT = C.VAULT, repo
        try:
            g = dict(self.gab[0], id="git", ficha="git:HEAD:f.md")
            _, resumo = C.tabela(C.mede([g]))
        finally:
            C.VAULT = antigo
        self.assertEqual(resumo[("g", "0.7/3")]["vp"], 1)

    def test_revisao_git_inexistente_vira_erro(self):
        medidos = C.mede([{"id": "git", "ficha": "git:nao-existe-0000:x.md", "fontes": [], "veredito": "ok", "grupo": "g"}])
        self.assertIn("erro", medidos[0])

    def test_saida_json(self):
        d = Path(self.tmp.name)
        (d / "gab.jsonl").write_text("\n".join(json.dumps(g) for g in self.gab[:2]), encoding="utf-8")
        sys.argv = ["x", "--gabarito", str(d / "gab.jsonl"), "--saida", str(d / "out.json")]
        self.assertEqual(C.principal(), 0)
        self.assertEqual(len(json.loads((d / "out.json").read_text(encoding="utf-8"))), 2)


if __name__ == "__main__":
    unittest.main()
