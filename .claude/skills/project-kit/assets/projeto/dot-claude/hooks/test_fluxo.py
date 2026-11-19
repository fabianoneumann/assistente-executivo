"""Os testes do hook do fluxo, em tabela, com o git e o gh trocados por respostas gravadas.

  python -m unittest discover -s .claude/hooks -p "test_*.py"

Cada caso de recusa roda duas vezes: com a trava, recusa; sem ela (`sem={trava}`), deixa de recusar. Assim o teste
prova que é aquela trava que pega o caso, e não outra coisa da linha.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fluxo  # noqa: E402

CABECA, BASE = "a" * 40, "b" * 40
CORPO_BOM = """Closes #12

## O que muda

Uma frase.

## Antes de abrir este PR

- [x] **Discussão inicial** feita
- [x] N/A: sem base mudada

## Validação exploratória

Rodei o fluxo. Um exemplo de caixa em código: `- [ ] isto não conta` e `<!-- nem isto -->`.

## Divergências

Nenhuma.
"""


def falso(respostas: dict[str, tuple[int, str, str]]):
    """O `rodar` dos testes: a resposta da primeira chave que começa a linha; sem chave, sucesso vazio."""
    def rodar(args, cwd):
        linha = " ".join(args)
        for chave, resposta in respostas.items():
            if linha.startswith(chave):
                return resposta
        return 0, "", ""
    return rodar


def remoto(branch: str | None = CABECA, base: str | None = BASE) -> dict:
    linhas = []
    if base:
        linhas.append(f"{base}\trefs/heads/main")
    if branch:
        linhas.append(f"{branch}\trefs/heads/12-tema")
    return {
        "git rev-parse --abbrev-ref HEAD": (0, "12-tema\n", ""),
        "git rev-parse HEAD": (0, CABECA + "\n", ""),
        "git ls-remote": (0, "\n".join(linhas) + "\n", ""),
    }


class Casos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        fora = Path(cls.tmp.name)
        cls.repo = fora / "repo"
        cls.repo.mkdir()
        cls.corpos = {}
        textos = {
            "bom": CORPO_BOM,
            "comentario": CORPO_BOM.replace("Uma frase.", "<!-- Uma frase. -->"),
            "sem_checklist": CORPO_BOM.replace("## Antes de abrir este PR", "## Outra seção"),
            "caixa_vazia": CORPO_BOM.replace("- [x] N/A: sem base mudada", "- [ ] **Base corrigida**"),
            "sem_numero": CORPO_BOM.replace("Closes #12", "Closes #"),
        }
        for nome, texto in textos.items():
            p = fora / f"corpo-{nome}.md"
            p.write_text(texto, encoding="utf-8")
            cls.corpos[nome] = p.as_posix()
        dentro = cls.repo / "corpo.md"
        dentro.write_text(CORPO_BOM, encoding="utf-8")
        cls.corpos["dentro"] = dentro.as_posix()
        os.environ.pop("CLAUDE_PROJECT_DIR", None)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def casos(self):
        c, r = self.corpos, self.repo.as_posix()
        topo = {"git rev-parse --show-toplevel": (0, r + "\n", "")}
        verde = {"gh pr checks": (0, json.dumps([{"name": "ci", "bucket": "pass"}]), "")}
        return [
            # (nome, gatilho, linha, respostas, shell, esperado, trava)
            ("encadeado", "pr-create", f"git push && gh pr create --body-file {c['bom']}", {**topo, **remoto()}, "Bash", "recusa", "encadeado"),
            ("fill", "pr-create", "gh pr create --fill", topo, "Bash", "recusa", "corpo_proibido"),
            ("body", "pr-create", 'gh pr create --title t --body "x"', topo, "Bash", "recusa", "corpo_proibido"),
            ("sem body-file", "pr-create", "gh pr create --title t", topo, "Bash", "recusa", "sem_body_file"),
            ("corpo no repo", "pr-create", f"gh pr create --body-file {c['dentro']}", {**topo, **remoto()}, "Bash", "recusa", "corpo_no_repo"),
            ("comentario", "pr-create", f"gh pr create --body-file {c['comentario']}", {**topo, **remoto()}, "Bash", "recusa", "corpo_comentario"),
            ("sem checklist", "pr-create", f"gh pr create --body-file {c['sem_checklist']}", {**topo, **remoto()}, "Bash", "recusa", "corpo_sem_checklist"),
            ("caixa vazia", "pr-create", f"gh pr create --body-file {c['caixa_vazia']}", {**topo, **remoto()}, "Bash", "recusa", "corpo_caixa_vazia"),
            ("sem numero", "pr-create", f"gh pr create --body-file {c['sem_numero']}", {**topo, **remoto()}, "Bash", "recusa", "corpo_sem_numero"),
            ("nao enviada", "pr-create", f"gh pr create --body-file {c['bom']}", {**topo, **remoto(branch=None)}, "Bash", "recusa", "branch_enviada"),
            ("commit nao enviado", "pr-create", f"gh pr create --body-file {c['bom']}", {**topo, **remoto(branch="c" * 40)}, "Bash", "recusa", "branch_enviada"),
            ("atras da base", "pr-create", f"gh pr create --body-file {c['bom']}", {**topo, **remoto(), "git merge-base": (1, "", "")}, "Bash", "recusa", "branch_atras"),
            ("tudo certo", "pr-create", f"gh pr create --title 'a; b' --body-file {c['bom']}", {**topo, **remoto()}, "Bash", "passa", None),
            ("powershell", "pr-create", f"& gh pr create --body-file '{c['bom']}' 2>&1", {**topo, **remoto()}, "PowerShell", "passa", None),
            ("sem rede", "pr-create", f"gh pr create --body-file {c['bom']}", {**topo, "git ls-remote": (128, "", "fatal")}, "Bash", "aviso", None),
            ("outro repo", "pr-create", "gh pr create -R dono/outro --fill", topo, "Bash", "passa", None),
            ("so cita", "pr-create", "echo 'use gh pr create depois'", topo, "Bash", "passa", None),
            ("merge encadeado", "pr-merge", "gh pr merge 12 --squash; git pull", verde, "Bash", "recusa", "encadeado"),
            ("ci vermelho", "pr-merge", "gh pr merge 12 --squash", {"gh pr checks": (1, json.dumps([{"name": "ci", "bucket": "fail"}]), "")}, "Bash", "recusa", "ci_vermelho"),
            ("ci rodando", "pr-merge", "gh pr merge 12 --squash", {"gh pr checks": (8, json.dumps([{"name": "ci", "bucket": "pending"}]), "")}, "Bash", "recusa", "ci_rodando"),
            ("sem checks", "pr-merge", "gh pr merge 12 --squash", {"gh pr checks": (1, "", "no checks reported on the '12-tema' branch")}, "Bash", "recusa", "ci_sem_checks"),
            ("ci verde", "pr-merge", "gh pr merge 12 --squash", verde, "Bash", "passa", None),
            ("merge sem rede", "pr-merge", "gh pr merge 12 --squash", {"gh pr checks": (1, "", "error connecting to api.github.com")}, "Bash", "aviso", None),
            ("aspa escapada", "pr-create", 'gh pr create --title "fix \\"x\\"" --fill', topo, "Bash", "recusa", "corpo_proibido"),
            ("aspa dobrada no powershell", "pr-create", 'gh pr create --title "a ""b""" --fill', topo, "PowerShell", "recusa", "corpo_proibido"),
            ("aspas sem fechar", "pr-create", 'gh pr create --title "x --fill', topo, "Bash", "aviso", None),
            ("head atras", "pr-create", f"gh pr create --head dono:12-tema --body-file {c['bom']}", {**topo, **remoto(), "git merge-base": (1, "", "")}, "Bash", "recusa", "branch_atras"),
            ("head sem o commit aqui", "pr-create", f"gh pr create --head 12-tema --body-file {c['bom']}", {**topo, **remoto(), "git merge-base": (128, "", "")}, "Bash", "aviso", None),
            ("merge com subject", "pr-merge", 'gh pr merge --squash --subject "feat: x" 12', {"gh pr checks 12 ": (1, json.dumps([{"name": "ci", "bucket": "fail"}]), "")}, "Bash", "recusa", "ci_vermelho"),
            ("checks vazio", "pr-merge", "gh pr merge 12 --squash", {"gh pr checks": (0, "[]", "")}, "Bash", "recusa", "ci_sem_checks"),
            ("commit fora de repo", "commit", "git commit -m x", {"git rev-parse --git-dir": (128, "", "fatal")}, "Bash", "passa", None),
            ("commit com -C", "commit", "git -C ../outro commit -m x", {"git config --get core.hooksPath": (1, "", "")}, "Bash", "aviso", None),
            ("hooks desligados", "commit", "git commit -m x", {"git config --get core.hooksPath": (1, "", "")}, "Bash", "aviso", None),
            ("hooks ligados", "commit", "git add . && git commit -m x", {"git config --get core.hooksPath": (0, ".githooks\n", "")}, "Bash", "passa", None),
        ]

    def test_cada_caso(self):
        for nome, gatilho, linha, respostas, shell, esperado, _ in self.casos():
            with self.subTest(nome):
                decisao, texto = fluxo.Fluxo(falso(respostas), base="main").decidir(gatilho, linha, str(self.repo), shell)
                self.assertEqual(decisao, esperado, texto)
                if esperado != "passa":
                    self.assertTrue(texto.strip(), "recusa e aviso dizem o que falta")

    def test_cada_recusa_falha_sem_a_trava(self):
        for nome, gatilho, linha, respostas, shell, esperado, trava in self.casos():
            if esperado != "recusa":
                continue
            with self.subTest(nome):
                com = fluxo.Fluxo(falso(respostas), base="main").decidir(gatilho, linha, str(self.repo), shell)
                sem = fluxo.Fluxo(falso(respostas), base="main", sem={trava}).decidir(gatilho, linha, str(self.repo), shell)
                self.assertNotEqual(sem, com, f"sem a trava {trava}, o caso recusa pelo mesmo motivo: {com[1]}")

    def test_saida_da_recusa_e_do_aviso(self):
        recusa = json.loads(fluxo.saida("recusa", "falta x"))["hookSpecificOutput"]
        self.assertEqual(recusa["permissionDecision"], "deny")
        self.assertNotIn("permissionDecision", json.loads(fluxo.saida("aviso", "y"))["hookSpecificOutput"])
        self.assertEqual(fluxo.saida("passa", ""), "", "passar é não imprimir nada (nunca um allow)")

    def test_leitor_da_linha(self):
        self.assertEqual(fluxo.separar(fluxo.tokenizar("gh pr create -t 'a && b' 2>&1")), [["gh", "pr", "create", "-t", "a && b", "2>&1"]])
        self.assertEqual(len(fluxo.separar(fluxo.tokenizar("git push\ngh pr create"))), 2)
        self.assertEqual(fluxo.tokenizar(r"gh pr create -F ..\tmp\c.md", powershell=True)[-1], r"..\tmp\c.md")


if __name__ == "__main__":
    unittest.main()
