"""Testes do intersecao.py, sem rede e sem navegador.

    python -X utf8 .claude/skills/object-anatomy/scripts/teste_intersecao.py
    (ou, de dentro de scripts/: python -X utf8 -m unittest -v teste_intersecao)
"""
import json
import math
import os
import subprocess
import sys
import tempfile
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import intersecao as it  # noqa: E402


def quadrado(x, y, lado=1.0):
    return [[x, y], [x + lado, y], [x + lado, y + lado], [x, y + lado]]


def peca(nome, poligono, grupo="g", **extra):
    d = {"nome": nome, "grupo": grupo, "poligono": poligono}
    d.update(extra)
    return d


def dados(pecas, estados=None, **extra):
    d = {"tolerancia": 0.02, "pecas": pecas, "estados": estados or [{"rotulo": "repouso"}]}
    d.update(extra)
    return d


class Profundidade(unittest.TestCase):
    def test_encostadas_nao_atravessam(self):
        r = it.confere(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(1, 0))]))
        self.assertEqual(r["problemas"], [])

    def test_sobrepostas_atravessam_com_a_profundidade(self):
        r = it.confere(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(0.5, 0))]))
        self.assertEqual(len(r["problemas"]), 1)
        p = r["problemas"][0]
        self.assertEqual({p["a"], p["b"]}, {"a", "b"})
        self.assertAlmostEqual(p["fundo"], 0.5, delta=0.02)

    def test_cruz_sem_vertice_dentro(self):
        # duas barras em cruz: nenhum vértice de uma cai dentro da outra
        h = [[-2, -0.1], [2, -0.1], [2, 0.1], [-2, 0.1]]
        v = [[-0.1, -2], [0.1, -2], [0.1, 2], [-0.1, 2]]
        r = it.confere(dados([peca("h", h), peca("v", v)]))
        self.assertEqual(len(r["problemas"]), 1)
        self.assertGreater(r["problemas"][0]["fundo"], 0.05)

    def test_uma_inteira_dentro_da_outra(self):
        r = it.confere(dados([peca("fora", quadrado(0, 0, 4)), peca("dentro", quadrado(1, 1, 1))]))
        self.assertEqual(len(r["problemas"]), 1)

    def test_poligono_concavo(self):
        L = [[0, 0], [3, 0], [3, 1], [1, 1], [1, 3], [0, 3]]
        no_vao = peca("no_vao", quadrado(1.5, 1.5, 1))      # no vão do L, sem tocar
        no_braco = peca("no_braco", quadrado(2, 0.5, 0.4))  # entra no braço de baixo
        r = it.confere(dados([peca("L", L), no_vao]))
        self.assertEqual(r["problemas"], [])
        r = it.confere(dados([peca("L", L), no_braco]))
        self.assertEqual(len(r["problemas"]), 1)

    def test_tolerancia_de_encosto(self):
        # 0,01 de sobreposição fica dentro da tolerância de 0,02; 0,05 passa dela
        r = it.confere(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(0.99, 0))]))
        self.assertEqual(r["problemas"], [])
        r = it.confere(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(0.95, 0))]))
        self.assertEqual(len(r["problemas"]), 1)


class Achados_do_code_review(unittest.TestCase):
    """Os casos que uma revisão de código mostrou rodando o script."""

    def test_pecas_coincidentes(self):
        r = it.confere(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(0, 0))]))
        self.assertEqual(len(r["problemas"]), 1)
        self.assertGreater(r["problemas"][0]["fundo"], 0.3)

    def test_circulos_quase_coincidentes_medem_mais_que_o_deslocamento(self):
        circ = lambda cx: [[cx + 5 * math.cos(2 * math.pi * k / 80), 5 * math.sin(2 * math.pi * k / 80)] for k in range(80)]
        r = it.confere(dados([peca("a", circ(0)), peca("b", circ(0.3))]))
        self.assertEqual(len(r["problemas"]), 1)
        self.assertGreater(r["problemas"][0]["fundo"], 5)   # a espessura da sobreposição, perto de 9,7

    def test_quase_coincidentes_nao_saltam_na_tolerancia(self):
        # segunda passada do /code-review: com 0,019 de deslocamento media 4,57, com 0,021 media 0,021
        for dx in (0.019, 0.021):
            r = it.confere(dados([peca("a", quadrado(0, 0, 10)), peca("b", quadrado(dx, 0, 10))]))
            self.assertGreater(r["problemas"][0]["fundo"], 5, dx)

    def test_camadas_planas_na_mesma_altura(self):
        pecas = [peca("a", quadrado(0, 0), profundidade=[0, 0]), peca("b", quadrado(0.5, 0), profundidade=[0, 0])]
        self.assertEqual(len(it.confere(dados(pecas))["problemas"]), 1)
        pecas[1]["profundidade"] = [1, 1]
        self.assertEqual(it.confere(dados(pecas))["problemas"], [])

    def test_camada_plana_encostada_na_face_nao_atravessa(self):
        pecas = [peca("folha", quadrado(0, 0), profundidade=[1, 1]), peca("bloco", quadrado(0.2, 0), profundidade=[0, 1])]
        self.assertEqual(it.confere(dados(pecas))["problemas"], [])
        pecas[0]["profundidade"] = [0.5, 0.5]
        self.assertEqual(len(it.confere(dados(pecas))["problemas"]), 1)

    def test_camada_no_meio_de_faixa_fina(self):
        pecas = [peca("folha", quadrado(0, 0), profundidade=[0.015, 0.015]), peca("chapa", quadrado(0.2, 0), profundidade=[0, 0.03])]
        self.assertEqual(len(it.confere(dados(pecas))["problemas"]), 1)

    def test_faixas_finas_que_so_encostam(self):
        pecas = [peca("a", quadrado(0, 0), profundidade=[0, 0.02]), peca("b", quadrado(0.2, 0), profundidade=[0.02, 0.04])]
        self.assertEqual(it.confere(dados(pecas))["problemas"], [])

    def test_ponto_de_fecho_repetido_aceito(self):
        q = quadrado(0, 0) + [[0, 0]]
        self.assertEqual(it.confere(dados([peca("a", q), peca("b", quadrado(3, 0))]))["problemas"], [])

    def test_mesmo_movimento_nao_se_mede_de_novo(self):
        pecas = [peca("a", quadrado(0, 0), grupo="fixo"), peca("b", quadrado(0.5, 0), grupo="fixo"),
                 peca("c", quadrado(5, 5), grupo="anda")]
        estados = [{"rotulo": f"t{k}", "desloca": {"anda": [k * 0.1, 0]}} for k in range(20)]
        conta = {"n": 0}
        original = it.profundidade

        def contando(*a, **k):
            conta["n"] += 1
            return original(*a, **k)
        it.profundidade = contando
        try:
            r = it.confere(dados(pecas, estados))
        finally:
            it.profundidade = original
        self.assertEqual(len(r["problemas"]), 20)                # a x b, em todo estado
        self.assertLess(conta["n"], 20)                          # mas medido uma vez só

    def test_cruzamento_declarado_com_fundo_max(self):
        pecas = [peca("haste", quadrado(0, 0), grupo="h"), peca("furo", quadrado(0.8, 0), grupo="f")]
        estados = [{"rotulo": "repouso"}, {"rotulo": "escorregou", "desloca": {"h": [0.5, 0]}}]
        dec = [{"pecas": ["haste", "furo"], "porque": "a haste passa pelo furo", "fundo_max": 0.3}]
        r = it.confere(dados(pecas, estados, cruzamentos_de_projeto=dec))
        self.assertEqual([p["estado"] for p in r["problemas"]], ["escorregou"])
        self.assertEqual(r["declarados"][0]["estados"], 1)

    def test_declaracao_que_nunca_cruza_vira_aviso(self):
        dec = [{"pecas": ["a", "b"], "porque": "antigo"}]
        r = it.confere(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(3, 0))], cruzamentos_de_projeto=dec))
        self.assertEqual(r["problemas"], [])
        self.assertEqual(len(r["declarados_sem_cruzar"]), 1)

    def test_entradas_invalidas(self):
        base = [peca("a", quadrado(0, 0)), peca("b", quadrado(3, 0))]
        casos = [
            dados(base, passo=0),
            dados(base, tolerancia=float("nan")),
            dados([peca("a", [[0, 0], [1, float("inf")], [0, 1]])]),
            dados(base, cruzamentos_de_projeto=[{"pecas": ["a", "a"], "porque": "erro de digitação"}]),
            dados(base, [{"rotulo": "x", "gira": {"g": 12}}]),
            dados(["não é peça"]),
            dados(base, ["não é estado"]),
            dados(base, cruzamentos_de_projeto=[{"pecas": [["a"], "b"], "porque": "lista no lugar do nome"}]),
            dados(base, cruzamentos_de_projeto=[{"pecas": ["a", "b"], "porque": "um"}, {"pecas": ["b", "a"], "porque": "dois"}]),
            dados([peca("gravata", [[0, 0], [1, 1], [1, 0], [0, 1]])]),
            dados([peca("reta", [[0, 0], [1, 0], [2, 0]])]),
        ]
        for c in casos:
            with self.assertRaises(ValueError, msg=str(c)[:80]):
                it.confere(c)

    def test_desempenho_de_perfis_de_revolucao(self):
        # sem relógio (que varia com a máquina): conta as distâncias à borda; a primeira versão fazia uma por ponto
        # amostrado, cerca de 15 mil neste caso
        circ = lambda cx: [[cx + 5 * math.cos(2 * math.pi * k / 400), 5 * math.sin(2 * math.pi * k / 400)] for k in range(400)]
        conta = {"n": 0}
        original = it._dist_borda

        def contando(*a):
            conta["n"] += 1
            return original(*a)
        it._dist_borda = contando
        try:
            r = it.confere(dados([peca("a", circ(0)), peca("b", circ(0.3))], tolerancia=0.002))
        finally:
            it._dist_borda = original
        self.assertEqual(len(r["problemas"]), 1)
        self.assertLess(conta["n"], 3000)


class Achados_da_revisao(unittest.TestCase):
    """Os casos de uma revisão de código do script. O primeiro e o
    terceiro falham na versão anterior; o segundo (a ponta que dobra sobre si, que o achado dizia passar) já era
    recusado, e fica para não deixar de ser."""

    def test_ponto_repetido_em_seguida_aceito(self):
        q = [[0, 0], [1, 0], [1, 0], [1, 1], [0, 1]]
        self.assertEqual(it.confere(dados([peca("a", q), peca("b", quadrado(3, 0))]))["problemas"], [])

    def test_ponta_que_dobra_sobre_si_recusada(self):
        with self.assertRaises(ValueError):
            it.confere(dados([peca("espinho", [[0, 0], [2, 0], [1, 0], [1, 1], [0, 1]])]))

    def test_tolerancia_de_profundidade_nula_e_o_padrao(self):
        r = it.confere(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(3, 0))], tolerancia_profundidade=None))
        self.assertEqual(r["problemas"], [])


class Estados(unittest.TestCase):
    def test_explosao_acusa_so_o_quadro_que_atravessa(self):
        pecas = [peca("base", quadrado(0, 0), grupo="base"), peca("tampa", quadrado(0, 1), grupo="tampa")]
        estados = [
            {"rotulo": "repouso"},
            {"rotulo": "t=0.5", "desloca": {"tampa": [0, 1]}},
            {"rotulo": "t=1.0", "desloca": {"tampa": [0, -0.4]}},
        ]
        r = it.confere(dados(pecas, estados))
        self.assertEqual([p["estado"] for p in r["problemas"]], ["t=1.0"])
        self.assertEqual(r["estados"], 3)

    def test_giro_do_grupo(self):
        # uma barra que, girada 90 graus em volta do próprio centro, entra na vizinha
        barra = [[0, -0.1], [2, -0.1], [2, 0.1], [0, 0.1]]
        vizinha = quadrado(0.9, 0.5, 0.5)
        pecas = [peca("barra", barra, grupo="rotor"), peca("vizinha", vizinha, grupo="fixo")]
        estados = [{"rotulo": "repouso"}, {"rotulo": "90", "gira": {"rotor": {"angulo": 90, "centro": [1, 0]}}}]
        r = it.confere(dados(pecas, estados))
        self.assertEqual([p["estado"] for p in r["problemas"]], ["90"])

    def test_camadas_de_profundidade_separadas_nao_atravessam(self):
        pecas = [peca("em_cima", quadrado(0, 0), profundidade=[1, 2]), peca("embaixo", quadrado(0.5, 0), profundidade=[0, 1])]
        r = it.confere(dados(pecas))
        self.assertEqual(r["problemas"], [])
        pecas[1]["profundidade"] = [0, 1.5]
        r = it.confere(dados(pecas))
        self.assertEqual(len(r["problemas"]), 1)

    def test_cruzamento_de_projeto_declarado(self):
        pecas = [peca("haste", quadrado(0, 0)), peca("furo", quadrado(0.5, 0))]
        r = it.confere(dados(pecas, cruzamentos_de_projeto=[{"pecas": ["haste", "furo"], "porque": "a haste passa pelo furo"}]))
        self.assertEqual(r["problemas"], [])
        self.assertEqual(len(r["declarados"]), 1)


class Validacao(unittest.TestCase):
    def test_grupo_inexistente_no_estado(self):
        with self.assertRaises(ValueError):
            it.confere(dados([peca("a", quadrado(0, 0))], [{"rotulo": "x", "desloca": {"nao_existe": [1, 0]}}]))

    def test_peca_inexistente_no_cruzamento(self):
        with self.assertRaises(ValueError):
            it.confere(dados([peca("a", quadrado(0, 0))], cruzamentos_de_projeto=[{"pecas": ["a", "b"], "porque": "x"}]))

    def test_cruzamento_sem_porque(self):
        with self.assertRaises(ValueError):
            it.confere(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(2, 0))], cruzamentos_de_projeto=[{"pecas": ["a", "b"]}]))

    def test_poligono_curto(self):
        with self.assertRaises(ValueError):
            it.confere(dados([peca("a", [[0, 0], [1, 0]])]))

    def test_nome_repetido(self):
        with self.assertRaises(ValueError):
            it.confere(dados([peca("a", quadrado(0, 0)), peca("a", quadrado(3, 0))]))


class Linha(unittest.TestCase):
    def roda(self, d, *extra):
        with tempfile.TemporaryDirectory() as tmp:
            p = os.path.join(tmp, "pecas.json")
            with open(p, "w", encoding="utf-8") as h:
                json.dump(d, h)
            env = dict(os.environ, PYTHONUTF8="1")
            return subprocess.run([sys.executable, os.path.join(AQUI, "intersecao.py"), p, *(extra or ("--json",))],
                                  capture_output=True, text=True, encoding="utf-8", env=env)

    def test_formato_errado_sai_com_2_e_nao_com_1(self):
        r = self.roda(dados([peca("a", quadrado(0, 0))], [{"rotulo": "x", "gira": {"g": 12}}]))
        self.assertEqual(r.returncode, 2)
        self.assertIn("inválido", r.stderr)

    def test_max_negativo_recusado(self):
        r = self.roda(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(0.5, 0))]), "--max", "-1")
        self.assertEqual(r.returncode, 2)

    def test_relatorio_em_texto(self):
        r = self.roda(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(0.5, 0))]), "--max", "0")
        self.assertEqual(r.returncode, 1)
        self.assertIn("atravessamentos: 1", r.stdout)
        self.assertIn("(mais 1;", r.stdout)

    def test_codigos_de_saida(self):
        limpo = self.roda(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(1, 0))]))
        self.assertEqual(limpo.returncode, 0, limpo.stderr)
        self.assertEqual(json.loads(limpo.stdout)["problemas"], [])
        ruim = self.roda(dados([peca("a", quadrado(0, 0)), peca("b", quadrado(0.5, 0))]))
        self.assertEqual(ruim.returncode, 1, ruim.stderr)
        invalido = self.roda({"pecas": []})
        self.assertEqual(invalido.returncode, 2)


if __name__ == "__main__":
    unittest.main()
