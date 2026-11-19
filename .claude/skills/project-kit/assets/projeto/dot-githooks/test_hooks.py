"""Os testes dos hooks do git, em tabela, com o git e o formatador trocados por respostas gravadas.

  python -m unittest discover -s .githooks -p "test_*.py"

Cada recusa roda também sem a trava (`sem={trava}`) e deixa de recusar: o teste prova que é aquela trava que pega.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hooks  # noqa: E402

CFG = {"base": "main", "log": "knowledge/log.md", "formatador": ["fmt", "{arquivo}"], "extensoes": [".py"], "comando_formatar": "fmt ."}
LOG_BOM = "# Log da base\n\nTexto.\n\n## [2026-11-01] setup | o projeto nasce\n\n## [2026-11-02] nota | outra\n"


LOG_NO_HEAD = {"knowledge/log.md": b"# Log da base\n\nTexto.\n\n## [2026-11-01] setup | o projeto nasce\n"}
LOG_NO_MEIO = "# Log da base\n\nTexto.\n\n## [2026-11-02] nota | outra\n\n## [2026-11-01] setup | o projeto nasce\n"


def git_falso(indice: dict[str, bytes], extra: dict[str, tuple[int, bytes]] | None = None, cabeca: dict[str, bytes] | None = None):
    """O índice (`show :x`), o HEAD (`show HEAD:x`, o log de LOG_NO_HEAD) e respostas soltas; sem MERGE_HEAD."""
    cabeca = LOG_NO_HEAD if cabeca is None else cabeca

    def git(*args, entrada=None):
        if args[:2] == ("diff", "--cached"):
            return 0, "\0".join(indice).encode() + b"\0"
        if args[0] == "show":
            origem, caminho = (cabeca, args[1][5:]) if args[1].startswith("HEAD:") else (indice, args[1][1:])
            return (0, origem[caminho]) if caminho in origem else (128, b"")
        for chave, resposta in (extra or {}).items():
            if " ".join(args).startswith(chave):
                return resposta
        if "MERGE_HEAD" in args:
            return 1, b""
        return 0, b""
    return git


def fmt_que_formata(cmd, conteudo):
    return 0, conteudo.replace(b"x=1", b"x = 1"), b""


class PreCommit(unittest.TestCase):
    casos = [
        # (nome, índice, formatador, código esperado, trava)
        ("fora do formato", {"a.py": b"x=1\n"}, fmt_que_formata, hooks.RECUSA, "formato"),
        ("no formato", {"a.py": b"x = 1\n"}, fmt_que_formata, 0, None),
        ("outra extensao", {"a.md": b"x=1\n"}, fmt_que_formata, 0, None),
        ("sem formatador", {"a.py": b"x=1\n"}, lambda c, b: None, 0, None),
        ("formatador falha", {"a.py": b"x=(\n"}, lambda c, b: (2, b"", b"erro de sintaxe"), 0, None),
        ("log no meio", {"knowledge/log.md": LOG_NO_MEIO.encode()}, fmt_que_formata, hooks.RECUSA, "log"),
        ("data anterior no fim passa", {"knowledge/log.md": LOG_BOM.replace("2026-11-02", "2026-10-30").encode()}, fmt_que_formata, 0, None),
        ("log formato", {"knowledge/log.md": (LOG_BOM + "## 2026-11-03 nota sem colchete\n").encode()}, fmt_que_formata, hooks.RECUSA, "log"),
        ("log cabecalho", {"knowledge/log.md": LOG_BOM.replace("# Log da base", "Log").encode()}, fmt_que_formata, hooks.RECUSA, "log"),
        ("log data que nao existe", {"knowledge/log.md": (LOG_BOM + "## [2026-02-30] nota | x\n").encode()}, fmt_que_formata, hooks.RECUSA, "log"),
        ("log bom", {"knowledge/log.md": LOG_BOM.encode()}, fmt_que_formata, 0, None),
    ]

    def test_cada_caso(self):
        for nome, indice, fmt, esperado, _ in self.casos:
            with self.subTest(nome):
                codigo, msgs = hooks.pre_commit(CFG, git=git_falso(indice), formatar=fmt)
                self.assertEqual(codigo, esperado, msgs)
                if nome in ("sem formatador", "formatador falha"):
                    self.assertTrue(msgs, "o que não foi conferido é dito, nunca passa calado")

    def test_cada_recusa_falha_sem_a_trava(self):
        for nome, indice, fmt, esperado, trava in self.casos:
            if esperado != hooks.RECUSA:
                continue
            with self.subTest(nome):
                codigo, _ = hooks.pre_commit(CFG, git=git_falso(indice), formatar=fmt, sem={trava})
                self.assertEqual(codigo, 0)


    def test_no_merge_a_ordem_e_do_merge(self):
        git = git_falso({"knowledge/log.md": LOG_NO_MEIO.encode()}, {"rev-parse -q --verify MERGE_HEAD": (0, b"abc")})
        self.assertEqual(hooks.pre_commit(CFG, git=git, formatar=fmt_que_formata)[0], 0)


class PrePush(unittest.TestCase):
    REFS = "refs/heads/12-tema " + "a" * 40 + " refs/heads/12-tema " + "0" * 40 + "\n"

    def test_atras_avisa_e_nao_recusa(self):
        git = git_falso({}, {"ls-remote": (0, b"b" * 40 + b"\trefs/heads/main\n"), "merge-base": (1, b"")})
        self.assertIn("atrás", " ".join(hooks.pre_push(CFG, "origin", self.REFS, git=git)))

    def test_em_dia(self):
        git = git_falso({}, {"ls-remote": (0, b"b" * 40 + b"\trefs/heads/main\n"), "merge-base": (0, b"")})
        self.assertEqual(hooks.pre_push(CFG, "origin", self.REFS, git=git), [])

    def test_primeiro_push_cala(self):
        git = git_falso({}, {"ls-remote": (0, b"")})
        self.assertEqual(hooks.pre_push(CFG, "origin", self.REFS, git=git), [])

    def test_sem_rede_diz(self):
        git = git_falso({}, {"ls-remote": (128, b"")})
        self.assertTrue(hooks.pre_push(CFG, "origin", self.REFS, git=git))


class Instalar(unittest.TestCase):
    def test_liga_e_nao_mexe_no_alheio(self):
        import os
        ci = os.environ.pop("CI", None)
        try:
            self.assertIn("ligados neste clone (core", hooks.instalar(git=git_falso({}, {"config --get": (1, b"")}))[1])
            self.assertIn("já estão", hooks.instalar(git=git_falso({}, {"config --get": (0, b".githooks\n")}))[1])
            self.assertIn("não mexi", hooks.instalar(git=git_falso({}, {"config --get": (0, b".husky\n")}))[1])
        finally:
            if ci is not None:
                os.environ["CI"] = ci


if __name__ == "__main__":
    unittest.main()
