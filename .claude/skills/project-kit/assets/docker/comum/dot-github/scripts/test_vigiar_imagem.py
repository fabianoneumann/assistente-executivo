"""Os testes do vigia da imagem base, sem rede, sem docker e sem gh: as duas perguntas e o estado do aviso.

  python3 -m unittest discover -s .github/scripts -p "test_*.py"
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vigiar_imagem as v  # noqa: E402

A = ("CVE-1", "HIGH", "libx", "1.0", "1.1", "usr/lib")
B = ("CVE-2", "CRITICAL", "liby", "2.0", "2.1", "usr/lib")


class Perguntas(unittest.TestCase):
    def test_trivy_um_achado_por_linha_sem_repetir(self):
        dados = {"Results": [
            {"Target": "alpine", "Vulnerabilities": [
                {"VulnerabilityID": "CVE-1", "Severity": "HIGH", "PkgName": "libx", "InstalledVersion": "1.0",
                 "FixedVersion": "1.1"}] * 2},
            {"Target": "node_modules", "Vulnerabilities": None},
        ]}
        self.assertEqual(v.achados_do_trivy(dados), [("CVE-1", "HIGH", "libx", "1.0", "1.1", "alpine")])
        self.assertEqual(v.achados_do_trivy({}), [])

    def test_node_atras_de_um_security_release(self):
        indice = [{"version": "v24.3.0", "security": True}, {"version": "v24.4.0", "security": False},
                  {"version": "v22.9.0", "security": True}]
        self.assertEqual(v.runtime_atrasado_node(indice, "v24.2.0")[0], "node-v24.3.0")
        self.assertIsNone(v.runtime_atrasado_node(indice, "v24.3.0"))
        self.assertIsNone(v.runtime_atrasado_node(indice, "v24.4.0"))
        # a comparação é por número, e não por texto: 24.10 vem depois de 24.9
        self.assertIsNone(v.runtime_atrasado_node([{"version": "v24.9.0", "security": True}], "v24.10.0"))
        with self.assertRaises(v.Falha):
            v.runtime_atrasado_node(indice, "v26.0.0")

    def test_python_atras_da_ultima_da_linha(self):
        listagem = '<a href="3.12.9/">3.12.9/</a> <a href="3.12.10/">3.12.10/</a> <a href="3.13.1/">3.13.1/</a>'
        self.assertEqual(v.runtime_atrasado_python(listagem, "3.12.9")[0], "python-3.12.10")
        self.assertIsNone(v.runtime_atrasado_python(listagem, "3.12.10"))
        with self.assertRaises(v.Falha):
            v.runtime_atrasado_python(listagem, "3.11.2")

    def test_python_a_pasta_so_com_rc_nao_conta(self):
        listagem = '<a href="3.12.9/">3.12.9/</a> <a href="3.12.10/">3.12.10/</a> <a href="3.12.11/">3.12.11/</a>'
        pastas = {"3.12.11": '<a href="Python-3.12.11rc1.tgz">', "3.12.10": '<a href="Python-3.12.10.tgz">'}
        self.assertEqual(v.runtime_atrasado_python(listagem, "3.12.9", pastas.get)[0], "python-3.12.10")
        self.assertIsNone(v.runtime_atrasado_python(listagem, "3.12.10", pastas.get))


class Estado(unittest.TestCase):
    def test_em_aberto_soma_tira_e_zera(self):
        historico = ["<!-- achados: CVE-1 CVE-2 -->", "<!-- resolvidos: CVE-1 -->"]
        self.assertEqual(v.em_aberto(historico), {"CVE-2"})
        self.assertEqual(v.em_aberto(historico + ["<!-- limpa: v1.0.0 -->"]), set())
        self.assertEqual(v.em_aberto(historico + ["<!-- limpa: v1.0.0 -->", "<!-- achados: CVE-1 -->"]), {"CVE-1"})
        self.assertEqual(v.em_aberto(["texto que fala de <!-- achados: CVE-9 --> no meio da linha"]), set())
        self.assertEqual(v.em_aberto(["editado na web\r\n<!-- achados: CVE-1 -->\r\n"]), {"CVE-1"})

    def test_sem_issue_abre_so_com_achado(self):
        self.assertEqual(v.plano(None, set(), [A])["acao"], "abrir")
        self.assertEqual(v.plano(None, set(), [])["acao"], "nada")

    def test_so_comenta_quando_muda(self):
        self.assertEqual(v.plano("OPEN", {"CVE-1"}, [A])["acao"], "nada")
        p = v.plano("OPEN", {"CVE-1"}, [A, B])
        self.assertEqual((p["acao"], p["novos"], p["resolvidos"]), ("comentar", [B], []))
        p = v.plano("OPEN", {"CVE-1", "CVE-2"}, [B])
        self.assertEqual((p["acao"], p["novos"], p["resolvidos"]), ("comentar", [], ["CVE-1"]))
        self.assertEqual(v.plano("OPEN", {"CVE-1"}, [])["resolvidos"], ["CVE-1"])

    def test_fechada_so_reabre_com_achado_novo(self):
        self.assertEqual(v.plano("CLOSED", {"CVE-1"}, [A])["acao"], "nada")
        p = v.plano("CLOSED", {"CVE-1"}, [])  # o que saiu se grava, sem reabrir
        self.assertEqual((p["acao"], p["reabrir"], p["resolvidos"]), ("comentar", False, ["CVE-1"]))
        # e o achado que volta depois de sair é novo outra vez
        historico = ["<!-- achados: CVE-1 -->", "<!-- resolvidos: CVE-1 -->"]
        self.assertEqual(v.plano("CLOSED", v.em_aberto(historico), [A])["reabrir"], True)
        p = v.plano("CLOSED", {"CVE-1"}, [A, B])
        self.assertEqual((p["acao"], p["reabrir"], p["novos"]), ("comentar", True, [B]))

    def test_os_corpos_levam_as_marcas_que_o_estado_le(self):
        ref = "ghcr.io/alguem/projeto:v1.0.0"
        novo = v.corpo_novo(ref, [A, B])
        self.assertEqual(v.em_aberto([novo]), {"CVE-1", "CVE-2"})
        p = v.plano("OPEN", {"CVE-1", "CVE-2"}, [B])
        self.assertEqual(v.em_aberto([novo, v.corpo_comentario(ref, p, [B])]), {"CVE-2"})
        limpa = v.corpo_comentario(ref, v.plano("OPEN", {"CVE-2"}, []), [])
        self.assertEqual(v.em_aberto([novo, limpa]), set())


if __name__ == "__main__":
    unittest.main()
