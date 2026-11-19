"""O teste da trava da I2, escrito antes do `trava_i2.py` (o teste que falha no código velho antes do conserto).

    python -X utf8 .claude/skills/visual-form/scripts/teste_trava_i2.py

Roda sobre o caso fixo de `casos/i2/`, sem navegador:
- uma peça de dez telas (`slides.html`), medida pelo `mede_forma.py --estatico` (a contagem do destaque manuscrito não
  depende de layout);
- o relatório da I2 sobre ela (`i2-relatorio.md`, no formato do `references/i2.md`): o Dest e o "Perde" de cada tela.

O que ele exige:
- a regra (b), sozinha, devolve as telas 2 e 5 (Dest "não" e nenhum destaque na medida);
- a trava antiga, sozinha, não devolve nem a 2 nem a 5: devolve a 8, que perde e tem Tam "não"; a 10 perde sem falha
  objetiva, e só volta com uma falha objetiva conferida à mão;
- com "Perde: não" em todas as telas (o estado da reconferência), a antiga devolve nada e a (b) continua devolvendo 2 e 5;
- a medida sozinha (destaque manuscrito zero) apontaria 2, 4, 5, 7 e 8;
- não volta tela sem motivo (a 3, a 4, a 7);
- entrada que falta ou não bate para o script, com o motivo, em vez de seguir com zero.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CASO = AQUI / "casos" / "i2"
V2 = CASO / "slides.html"
RELATORIO = CASO / "i2-relatorio.md"
sys.path.insert(0, str(AQUI))

import mede_forma  # noqa: E402
import trava_i2  # noqa: E402


def telas(res, regra=None):
    return {v["tela"] for v in res["voltam"] if regra is None or regra in v["regras"]}


class APremissa(unittest.TestCase):
    """O que o teste lê é o que a I2 julgou: se a premissa muda, o resto não vale."""

    def test_destaque_por_tela_no_caso(self):
        m = mede_forma.medir_estatico(V2)
        self.assertEqual([x["destaque_manuscrito"] for x in m], [1, 0, 1, 0, 0, 1, 0, 0, 2, 1])
        self.assertTrue(all(x["modo"] == "estatico" for x in m))
        self.assertIsNone(m[0]["margem_esq_min"], "sem navegador, a medida de layout fica ausente, não zero")

    def test_lista_da_i2_lida_do_relatorio(self):
        lista = trava_i2.ler_relatorio(RELATORIO)
        self.assertEqual(sorted(lista), list(range(1, 11)))
        dest = [lista[t]["itens"]["Dest"] for t in range(1, 11)]
        self.assertEqual(dest, ["sim", "não", "sim", "sim", "não", "sim", "parcial", "parcial", "sim", "sim"])
        self.assertEqual({t for t in lista if lista[t]["perde"] == "sim"}, {8, 10})
        self.assertEqual(lista[8]["itens"]["Tam"], "não")
        self.assertEqual(lista[2]["itens"]["Can"], "não")


class ATrava(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = mede_forma.medir_estatico(V2)
        cls.lista = trava_i2.ler_relatorio(RELATORIO)

    def test_regra_b_devolve_2_e_5(self):
        self.assertEqual(telas(trava_i2.trava(self.m, self.lista, regras=("b",))), {2, 5})

    def test_trava_antiga_nao_devolve_2_nem_5(self):
        antiga = telas(trava_i2.trava(self.m, self.lista, regras=("antiga",)))
        self.assertEqual(antiga & {2, 5}, set())
        self.assertEqual(antiga, {8}, "a 8 perde e tem Tam 'não'")

    def test_trava_inteira(self):
        res = trava_i2.trava(self.m, self.lista)
        self.assertEqual(telas(res), {2, 5, 8})
        self.assertEqual(telas(res, "b"), {2, 5})
        self.assertEqual(telas(res, "antiga"), {8})

    def test_nao_volta_tela_sem_motivo(self):
        self.assertEqual(telas(trava_i2.trava(self.m, self.lista)) & {1, 3, 4, 6, 7, 9}, set())

    def test_medida_sozinha_apontaria_mais(self):
        self.assertEqual(trava_i2.falham_destaque(self.m), {2, 4, 5, 7, 8})

    def test_perde_nao_em_todas(self):
        lista = {t: {**v, "perde": "não"} for t, v in self.lista.items()}
        self.assertEqual(telas(trava_i2.trava(self.m, lista, regras=("antiga",))), set())
        self.assertEqual(telas(trava_i2.trava(self.m, lista)), {2, 5})

    def test_falha_objetiva_conferida_a_mao(self):
        res = trava_i2.trava(self.m, self.lista, falhas_objetivas={10: "a chamada corre sob a folha que espia"})
        self.assertEqual(telas(res), {2, 5, 8, 10})
        dez = next(v for v in res["voltam"] if v["tela"] == 10)
        self.assertIn("a chamada corre sob a folha que espia", " ".join(dez["motivos"]))

    def test_falha_objetiva_sem_perde_vira_sinal(self):
        res = trava_i2.trava(self.m, self.lista, falhas_objetivas={3: "o círculo encosta no 'na'"})
        self.assertNotIn(3, telas(res))
        self.assertIn(3, {s["tela"] for s in res["sinais"]})

    def test_sinais_levam_o_que_nao_volta(self):
        sinais = {s["tela"] for s in trava_i2.trava(self.m, self.lista)["sinais"]}
        self.assertTrue({4, 7, 10} <= sinais, "medida sem Dest 'não', Dest parcial, e perde sem falha objetiva")
        dez = next(s for s in trava_i2.trava(self.m, self.lista)["sinais"] if s["tela"] == 10)
        self.assertIn("margem e transborda não medidos", " ".join(dez["motivos"]), "o estático não vira 'sem falha'")


class AEntradaQueNaoBate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = mede_forma.medir_estatico(V2)
        cls.texto = RELATORIO.read_text(encoding="utf-8")

    def _relatorio(self, texto):
        d = tempfile.mkdtemp()
        p = Path(d) / "i2.md"
        p.write_text(texto, encoding="utf-8", newline="\n")
        return p

    def test_tela_faltando_no_relatorio(self):
        ini, fim = self.texto.index("### Tela 5"), self.texto.index("### Tela 6")
        lista = trava_i2.ler_relatorio(self._relatorio(self.texto[:ini] + self.texto[fim:]))
        with self.assertRaises(trava_i2.TravaErro):
            trava_i2.trava(self.m, lista)

    def test_dest_ausente(self):
        texto = self.texto.replace(" Dest **não** (o segundo gancho", " (o segundo gancho", 1)
        self.assertNotEqual(texto, self.texto)
        with self.assertRaises(trava_i2.TravaErro):
            trava_i2.ler_relatorio(self._relatorio(texto))

    def test_item_da_lista_ausente(self):
        ini = self.texto.index("### Tela 3")
        trecho = self.texto[ini:self.texto.index("### Tela 4")]
        texto = self.texto.replace(trecho, trecho.replace(" Tam **parcial**", "", 1), 1)
        self.assertNotEqual(texto, self.texto)
        with self.assertRaises(trava_i2.TravaErro):
            trava_i2.ler_relatorio(self._relatorio(texto))

    def test_item_com_dois_pontos(self):
        ini = self.texto.index("### Tela 8")
        trecho = self.texto[ini:self.texto.index("### Tela 9")]
        texto = self.texto.replace(trecho, trecho.replace("Tam **não**", "Tam: **não**", 1), 1)
        self.assertNotEqual(texto, self.texto)
        self.assertEqual(trava_i2.ler_relatorio(self._relatorio(texto))[8]["itens"]["Tam"], "não")

    def test_perde_ausente(self):
        ini = self.texto.index("### Tela 2")
        trecho = self.texto[ini:self.texto.index("### Tela 3")]
        texto = self.texto.replace(trecho, trecho.replace("**Perde: não** (perde só na ordem 2).", ""), 1)
        self.assertNotEqual(texto, self.texto)
        with self.assertRaises(trava_i2.TravaErro):
            trava_i2.ler_relatorio(self._relatorio(texto))

    def test_relatorio_sem_telas(self):
        with self.assertRaises(trava_i2.TravaErro):
            trava_i2.ler_relatorio(self._relatorio("# nada\n\nsem blocos de tela\n"))

    def test_medida_ausente_nao_e_zero(self):
        m = [dict(x) for x in self.m]
        m[1]["destaque_manuscrito"] = None
        with self.assertRaises(trava_i2.TravaErro):
            trava_i2.trava(m, trava_i2.ler_relatorio(RELATORIO))


class APontaDeLinha(unittest.TestCase):
    """O uso pela linha de comando, como a skill manda rodar: código 1 quando há tela que volta, 2 na entrada ruim."""

    def _roda(self, *args):
        return subprocess.run([sys.executable, "-X", "utf8", *args], capture_output=True, text=True, encoding="utf-8")

    def test_mede_e_trava(self):
        with tempfile.TemporaryDirectory() as d:
            med = Path(d) / "medidas.json"
            r = self._roda(str(AQUI / "mede_forma.py"), str(V2), str(med), "--estatico")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertNotIn(b"\r", med.read_bytes())
            saida = Path(d) / "trava.json"
            r = self._roda(str(AQUI / "trava_i2.py"), str(med), str(RELATORIO), "--json", str(saida),
                           "--falha-objetiva", "10:a chamada corre sob a folha")
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            d2 = json.loads(saida.read_text(encoding="utf-8"))
            self.assertEqual({v["tela"] for v in d2["voltam"]}, {2, 5, 8, 10})
            self.assertIn("tela 2", r.stdout)

    def _bloco(self, tela, dest, perde):
        return (f"### Tela {tela}, reconferida\n\n**Lista:** Hi sim. Ng sim. Ac sim. Nº n/a. Tam sim. Can parcial. Est sim. "
                f"Dest {dest}.\n\n**Perde: {perde}.**\n\n")

    def test_reconferencia(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            med, ant, rec, saida = d / "m.json", d / "ant.json", d / "recon.md", d / "t.json"
            self.assertEqual(self._roda(str(AQUI / "mede_forma.py"), str(V2), str(med), "--estatico").returncode, 0)
            r = self._roda(str(AQUI / "trava_i2.py"), str(med), str(RELATORIO), "--json", str(ant))
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            # a volta resolveu as três que voltaram (2, 5, 8); a 10, que perdia sem falha, não foi reconferida
            rec.write_text("# Reconferência\n\n" + self._bloco(2, "sim", "não") + self._bloco(5, "sim", "não")
                           + self._bloco(8, "parcial", "não"), encoding="utf-8", newline="\n")
            falha_10 = ["--falha-objetiva", "10:a margem caiu depois do ajuste da 8"]
            r = self._roda(str(AQUI / "trava_i2.py"), str(med), str(RELATORIO), "--reconferencia", str(rec),
                           "--anterior", str(ant), "--json", str(saida), *falha_10)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            res = json.loads(saida.read_text(encoding="utf-8"))
            self.assertEqual(res["voltam"], [], "a 10 não volta por uma comparação da versão antiga")
            dez = next(s for s in res["sinais"] if s["tela"] == 10)
            self.assertIn("sem reconferência", " ".join(dez["motivos"]))
            # a reconferência que deixa de fora uma tela que voltou, ou traz uma que não voltou, para o script
            for blocos in ((2, 5), (2, 5, 8, 9)):
                rec.write_text("".join(self._bloco(t, "sim", "não") for t in blocos), encoding="utf-8", newline="\n")
                r = self._roda(str(AQUI / "trava_i2.py"), str(med), str(RELATORIO), "--reconferencia", str(rec),
                               "--anterior", str(ant))
                self.assertEqual(r.returncode, 2, f"{blocos}: {r.stdout + r.stderr}")
            r = self._roda(str(AQUI / "trava_i2.py"), str(med), str(RELATORIO), "--reconferencia", str(rec))
            self.assertEqual(r.returncode, 2, "sem o --anterior")

    def test_entrada_ruim(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            med = d / "medidas.json"
            med.write_text("[]", encoding="utf-8", newline="\n")
            self.assertEqual(self._roda(str(AQUI / "trava_i2.py"), str(med), str(RELATORIO)).returncode, 2)
            med.write_text('{"tela": 1}', encoding="utf-8", newline="\n")
            self.assertEqual(self._roda(str(AQUI / "trava_i2.py"), str(med), str(RELATORIO)).returncode, 2)
            self.assertEqual(self._roda(str(AQUI / "mede_forma.py"), str(V2), str(med), "--estatico").returncode, 0)
            for falha in ("dez:sem número", "11:tela que não existe"):
                r = self._roda(str(AQUI / "trava_i2.py"), str(med), str(RELATORIO), "--falha-objetiva", falha)
                self.assertEqual(r.returncode, 2, f"{falha}: {r.stdout + r.stderr}")
            r = self._roda(str(AQUI / "trava_i2.py"), str(med), str(RELATORIO), "--json", str(d / "nao-existe" / "t.json"))
            self.assertEqual(r.returncode, 2, "a pasta do --json que não existe")
            self.assertEqual(self._roda(str(AQUI / "trava_i2.py"), "--help").returncode, 0)

    def test_falha_objetiva_repetida_junta(self):
        m = mede_forma.medir_estatico(V2)
        res = trava_i2.trava(m, trava_i2.ler_relatorio(RELATORIO), falhas_objetivas=trava_i2._falhas(["10:a", "10:b"]))
        dez = next(v for v in res["voltam"] if v["tela"] == 10)
        self.assertIn("a; b (conferido à mão)", dez["motivos"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
