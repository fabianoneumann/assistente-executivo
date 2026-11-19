"""Os testes do `montar.py` e do `conferir.py`, e os testes das travas dentro do projeto montado.

  python -X utf8 -m unittest discover -s .claude/skills/project-kit/scripts -p "teste_*.py"

Monta as duas variantes de partida e a `outra` numa pasta temporária, confere com 0 ERRO, roda os testes das travas
que vão junto com o projeto, e planta um erro de cada tipo para ver o `conferir.py` acusá-lo.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import conferir  # noqa: E402
import montar  # noqa: E402

BASE = {
    "arquitetura.md": "# A arquitetura\n\nUm serviço HTTP com um banco.\n",
    "plano.md": "# O plano\n\n## Os arcos\n\n1. O esqueleto.\n",
    "decisions/001-arquitetura-e-stack.md": "# ADR 001: a arquitetura e a stack\n\n**Revê se:** o volume passar de mil por dia.\n",
    "decisions/002-ferramental.md": "# ADR 002: o ferramental\n\n**Revê se:** o CI passar de 3 minutos.\n",
}


class Montar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.raiz = Path(cls.tmp.name)
        cls.base = cls.raiz / "base"
        for rel, texto in BASE.items():
            (cls.base / rel).parent.mkdir(parents=True, exist_ok=True)
            (cls.base / rel).write_text(texto, encoding="utf-8")
        comandos = json.loads((AQUI.parent / "assets/stacks.json").read_text(encoding="utf-8"))["python-fastapi"]
        comandos["STACK_DESCRICAO"] = "Go 1.25"
        comandos["CMD_TESTES"] = "make test # todos, com: dois pontos"
        cls.comandos = cls.raiz / "comandos.json"
        cls.comandos.write_text(json.dumps(comandos), encoding="utf-8")
        cls.projetos = {}
        for stack, conta in (("python-fastapi", "user"), ("node-ts", "org"), ("outra", "user")):
            destino = cls.raiz / f"p-{stack}"
            args = ["--destino", str(destino), "--nome", f"teste-{stack}", "--descricao", 'Um "teste" do kit.',
                    "--stack", stack, "--dono", "alguem", "--base", str(cls.base), "--conta", conta, "--data", "2026-11-17"]
            if stack == "node-ts":
                args += ["--responsavel", "pessoa"]  # o responsável é opcional: só um projeto o recebe
            if stack == "outra":
                args += ["--comandos", str(cls.comandos)]
            assert montar.main(args) == 0, stack
            cls.projetos[stack] = destino

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_responsavel_do_dependabot_e_opcional(self):
        import yaml
        sem = yaml.safe_load((self.projetos["python-fastapi"] / ".github/dependabot.yml").read_text(encoding="utf-8"))
        com = yaml.safe_load((self.projetos["node-ts"] / ".github/dependabot.yml").read_text(encoding="utf-8"))
        self.assertTrue(all("assignees" not in u for u in sem["updates"]))
        self.assertTrue(all(u.get("assignees") == ["pessoa"] for u in com["updates"]))

    def test_conferir_sai_sem_erro_nas_tres(self):
        for stack, pasta in self.projetos.items():
            with self.subTest(stack):
                erros, _ = conferir.conferir(pasta)
                self.assertEqual(erros, [])

    def test_so_o_bloco_da_stack_e_da_conta(self):
        py, node = self.projetos["python-fastapi"], self.projetos["node-ts"]
        ci_py = (py / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        self.assertIn("setup-python", ci_py)
        self.assertNotIn("setup-node", ci_py)
        self.assertIn("setup-node", (node / ".github/workflows/ci.yml").read_text(encoding="utf-8"))
        self.assertIn('labels: ["defeito"]', (py / ".github/ISSUE_TEMPLATE/defeito.md").read_text(encoding="utf-8"))
        self.assertIn("type: Bug", (node / ".github/ISSUE_TEMPLATE/defeito.md").read_text(encoding="utf-8"))
        self.assertIn("prioridade:urgente", (py / "knowledge/metadados.md").read_text(encoding="utf-8"))
        # a regra da tag: escrita no CLAUDE.md na conta pessoal; o ruleset só na organização
        claude_py = (py / "CLAUDE.md").read_text(encoding="utf-8")
        claude_node = (node / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertIn("A tag publicada não se move nem se apaga", claude_py)
        self.assertNotIn("A regra de tag do GitHub impede", claude_py)
        self.assertIn("A regra de tag do GitHub impede", claude_node)
        self.assertNotIn("[kit:", claude_py + claude_node)
        self.assertIn("Priority", (node / "knowledge/metadados.md").read_text(encoding="utf-8"))
        self.assertTrue((py / "pyproject.toml").is_file() and (node / "package.json").is_file())
        self.assertFalse((py / "CLAUDE.md.modelo").exists())
        self.assertEqual(json.loads((node / "package.json").read_text(encoding="utf-8"))["description"], 'Um "teste" do kit.')

    def test_comando_com_cerquilha_sobrevive_no_yaml(self):
        import yaml
        ci = yaml.safe_load((self.projetos["outra"] / ".github/workflows/ci.yml").read_text(encoding="utf-8"))
        runs = [p.get("run") for p in ci["jobs"]["ci"]["steps"]]
        self.assertIn("make test # todos, com: dois pontos", runs)

    def test_git_e_hooks_ligados(self):
        pasta = self.projetos["python-fastapi"]
        r = subprocess.run(["git", "config", "--get", "core.hooksPath"], cwd=pasta, capture_output=True, text=True)
        self.assertEqual(r.stdout.strip(), ".githooks")
        r = subprocess.run(["git", "ls-files", "-s", ".githooks/pre-commit"], cwd=pasta, capture_output=True, text=True)
        self.assertTrue(r.stdout.startswith("100755"), r.stdout)
        self.assertNotIn(b"\r", (pasta / ".githooks/pre-commit").read_bytes())

    def test_os_testes_das_travas_passam_no_projeto(self):
        pasta = self.projetos["python-fastapi"]
        for d in (".claude/hooks", ".githooks"):
            with self.subTest(d):
                r = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", d, "-p", "test_*.py"],
                                   cwd=pasta, capture_output=True, text=True, env={**os.environ, "PYTHONUTF8": "1"})
                self.assertEqual(r.returncode, 0, r.stderr[-2000:])
        r = subprocess.run([sys.executable, ".githooks/hooks.py", "log"], cwd=pasta, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_recusas_do_montar(self):
        casos = [
            ("destino cheio", ["--destino", str(self.projetos["python-fastapi"])], "não está vazio"),
            ("outra sem comandos", ["--stack", "outra"], "--comandos"),
            ("nome ruim", ["--nome", "Meu Projeto"], "não serve"),
            ("base sem ADR", ["--base", str(self.raiz)], "decisions/001"),
        ]
        for nome, troca, trecho in casos:
            with self.subTest(nome):
                args = {"--destino": str(self.raiz / f"novo-{nome.replace(' ', '-')}"), "--nome": "x", "--descricao": "d",
                        "--stack": "python-fastapi", "--dono": "a", "--base": str(self.base)}
                args.update(dict(zip(troca[::2], troca[1::2])))
                ns = montar.argparse.Namespace(**{k[2:].replace("-", "_"): v for k, v in args.items()},
                                               conta="user", responsavel=None, comandos=None, data="2026-11-17", ramo="main", sem_git=True)
                with self.assertRaises(montar.Falta) as ctx:
                    montar.montar(ns)
                self.assertIn(trecho, str(ctx.exception))

    def test_conferir_acusa_cada_erro_plantado(self):
        plantados = [
            ("marcador", "README.md", lambda t: t + "\n{{NOME}}\n", "marcador"),
            ("modelo nao preenchido", "knowledge/arquitetura.md", lambda t: t + "\n<!-- kit: preencher -->\n", "marcador"),
            ("caminho absoluto", "knowledge/plano.md", lambda t: t + "\nVer D:\\projetos\\x\\y.md\n", "caminho absoluto"),
            ("mencao a origem", "knowledge/plano.md", lambda t: t + "\nComo no assistente-executivo.\n", "ambiente de onde"),
            ("acao sem hash", ".github/workflows/ci.yml", lambda t: t.replace("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1", "actions/checkout@v7"), "hash"),
            ("ask no settings", ".claude/settings.json", lambda t: t.replace('"deny"', '"ask": ["Bash(gh *)"], "deny"'), "ask"),
            ("dependabot de versao", ".github/dependabot.yml", lambda t: t.replace("    open-pull-requests-limit: 0", "    open-pull-requests-limit: 5", 1), "open-pull-requests-limit"),
            ("yaml quebrado", ".github/release.yml", lambda t: t + "\n  - : [\n", "YAML"),
            ("sem union", ".gitattributes", lambda t: t.replace("merge=union", ""), "merge=union"),
            ("claude longo", "CLAUDE.md", lambda t: t + "linha\n" * 160, "acima de 150"),
            ("casca em crlf", ".githooks/pre-commit", lambda t: t.replace("\n", "\r\n"), "CRLF"),
        ]
        for nome, rel, mudar, trecho in plantados:
            with self.subTest(nome):
                copia = self.raiz / f"plantado-{nome.replace(' ', '-')}"
                shutil.copytree(self.projetos["python-fastapi"], copia, ignore=shutil.ignore_patterns(".git"))
                arq = copia / rel
                arq.write_bytes(mudar(arq.read_bytes().decode("utf-8")).encode("utf-8"))
                erros, _ = conferir.conferir(copia)
                self.assertTrue(any(trecho in e for e in erros), f"{nome}: {erros}")


if __name__ == "__main__":
    unittest.main()
