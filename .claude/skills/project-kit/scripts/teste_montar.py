"""Os testes do `montar.py` e do `conferir.py`, e os testes das travas dentro do projeto montado.

  python -X utf8 -m unittest discover -s .claude/skills/project-kit/scripts -p "teste_*.py"

Monta as duas variantes de partida e a `outra` numa pasta temporária, e as duas variantes de novo com a imagem
(`--docker`), confere com 0 ERRO, roda os testes das travas e do vigia da imagem que vão junto com o projeto, e planta
um erro de cada tipo para ver o `conferir.py` acusá-lo.
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
        for chave, stack, conta in (("python-fastapi", "python-fastapi", "user"), ("node-ts", "node-ts", "org"),
                                    ("outra", "outra", "user"), ("docker-python", "python-fastapi", "user"),
                                    ("docker-node", "node-ts", "org")):
            destino = cls.raiz / f"p-{chave}"
            args = ["--destino", str(destino), "--nome", f"teste-{chave}", "--descricao", 'Um "teste" do kit.',
                    "--stack", stack, "--dono", "alguem", "--base", str(cls.base), "--conta", conta, "--data", "2026-11-17"]
            if chave in ("node-ts", "docker-node"):
                args += ["--responsavel", "pessoa"]  # o responsável é opcional: só alguns projetos o recebem
            if stack == "outra":
                args += ["--comandos", str(cls.comandos)]
            if chave.startswith("docker-"):
                args += ["--docker"]
            assert montar.main(args) == 0, chave
            cls.projetos[chave] = destino

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_responsavel_do_dependabot_e_opcional(self):
        import yaml
        sem = yaml.safe_load((self.projetos["python-fastapi"] / ".github/dependabot.yml").read_text(encoding="utf-8"))
        com = yaml.safe_load((self.projetos["node-ts"] / ".github/dependabot.yml").read_text(encoding="utf-8"))
        self.assertTrue(all("assignees" not in u for u in sem["updates"]))
        self.assertTrue(all(u.get("assignees") == ["pessoa"] for u in com["updates"]))

    def test_conferir_sai_sem_erro_nas_cinco(self):
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

    def test_a_imagem_so_nasce_com_o_docker(self):
        import yaml
        for chave in ("python-fastapi", "node-ts", "outra"):
            with self.subTest(chave):
                pasta = self.projetos[chave]
                self.assertEqual([rel for rel in conferir.DOCKER if (pasta / rel).exists()], [])
                ci = yaml.safe_load((pasta / ".github/workflows/ci.yml").read_text(encoding="utf-8"))
                self.assertEqual(list(ci["jobs"]), ["ci"])
                self.assertNotIn("imagem-base.md", (pasta / "knowledge/index.md").read_text(encoding="utf-8"))
                self.assertIn("ganha uma vigilância à parte", (pasta / "knowledge/versao-e-dependencias.md").read_text(encoding="utf-8"))
        for chave, porta, runtime in (("docker-python", "8000", "python"), ("docker-node", "3000", "node")):
            with self.subTest(chave):
                pasta = self.projetos[chave]
                self.assertEqual([rel for rel in conferir.DOCKER if not (pasta / rel).exists()], [])
                ci = yaml.safe_load((pasta / ".github/workflows/ci.yml").read_text(encoding="utf-8"))
                self.assertEqual(list(ci["jobs"]), ["ci", "imagem"])
                passos = " ".join(str(p.get("run", "")) for p in ci["jobs"]["imagem"]["steps"])
                self.assertIn("docker build --pull", passos)
                self.assertIn(f"127.0.0.1:{porta}/health", passos)
                vigia = (pasta / ".github/scripts/vigiar_imagem.py").read_text(encoding="utf-8")
                self.assertIn(f'RUNTIME = "{runtime}"', vigia)
                self.assertEqual(vigia.count("RUNTIME = "), 1)
                self.assertIn("imagem-base.md", (pasta / "knowledge/index.md").read_text(encoding="utf-8"))
                self.assertIn("vigiar-imagem.yml", (pasta / "knowledge/imagem-base.md").read_text(encoding="utf-8"))
        resp = yaml.safe_load((self.projetos["docker-node"] / ".github/workflows/vigiar-imagem.yml").read_text(encoding="utf-8"))
        self.assertEqual(resp["jobs"]["vigiar"]["env"]["RESPONSAVEL"], "pessoa")
        sem = yaml.safe_load((self.projetos["docker-python"] / ".github/workflows/vigiar-imagem.yml").read_text(encoding="utf-8"))
        self.assertEqual(sem["jobs"]["vigiar"]["env"]["RESPONSAVEL"], "")
        ignorar = (self.projetos["docker-python"] / ".dockerignore").read_text(encoding="utf-8")
        self.assertIn(".env", ignorar)
        self.assertNotIn("node_modules", ignorar)

    def test_as_propostas_da_segunda_leitura_nos_modelos(self):
        pasta = self.projetos["python-fastapi"]
        import yaml
        ci = yaml.safe_load((pasta / ".github/workflows/ci.yml").read_text(encoding="utf-8"))
        self.assertEqual(ci["concurrency"]["cancel-in-progress"], "${{ github.event_name == 'pull_request' }}")
        self.assertNotIn("paths", ci[True])  # o PyYAML lê o "on:" como True; filtro por caminho não vai no gatilho
        texto = lambda rel: (pasta / rel).read_text(encoding="utf-8")  # noqa: E731
        self.assertIn("O que ficou sem prova", texto("knowledge/decisions/000-modelo.md"))
        self.assertIn("alterado pelo ADR N", texto("knowledge/README.md"))
        self.assertIn("## O spike", texto("knowledge/processo.md"))
        self.assertIn("## Os testes", texto("knowledge/versao-e-dependencias.md"))
        self.assertIn("rebase", texto("knowledge/versao-e-dependencias.md"))
        self.assertIn('"versao"', texto("app/main.py"))
        self.assertIn("versao:", (self.projetos["node-ts"] / "src/servidor.ts").read_text(encoding="utf-8"))
        self.assertIn("-r requirements.txt", texto("requirements-dev.txt"))

    def test_o_vigia_passa_nos_testes_dentro_do_projeto(self):
        for chave in ("docker-python", "docker-node"):
            with self.subTest(chave):
                r = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", ".github/scripts", "-p", "test_*.py"],
                                   cwd=self.projetos[chave], capture_output=True, text=True, env={**os.environ, "PYTHONUTF8": "1"})
                self.assertEqual(r.returncode, 0, r.stderr[-2000:])

    def test_o_roteador_e_a_base_conferidos_dentro_do_projeto(self):
        # o conferir_base.py e os testes dele vão com todo projeto, com ou sem imagem, e o CI os roda depois do nascimento
        for chave, pasta in self.projetos.items():
            with self.subTest(chave):
                env = {**os.environ, "PYTHONUTF8": "1"}
                r = subprocess.run([sys.executable, ".github/scripts/conferir_base.py"], cwd=pasta, capture_output=True, text=True, env=env)
                self.assertEqual(r.returncode, 0, r.stdout[-2000:])
                self.assertIn("0 ERRO, 0 AVISO", r.stdout)
                r = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", ".github/scripts", "-p", "test_*.py"],
                                   cwd=pasta, capture_output=True, text=True, env=env)
                self.assertEqual(r.returncode, 0, r.stderr[-2000:])
                ci = (pasta / ".github/workflows/ci.yml").read_text(encoding="utf-8")
                self.assertIn("python3 .github/scripts/conferir_base.py", ci)

    def test_os_itens_antigos_da_282_nos_modelos(self):
        pasta = self.projetos["python-fastapi"]
        texto = lambda rel: (pasta / rel).read_text(encoding="utf-8")  # noqa: E731
        spec = texto(".github/ISSUE_TEMPLATE/spec.md")
        for trecho in ("O teste do essencial", "se bloqueia", "o que não pode acontecer", "Dado / Quando / Então", "a descartada", "tira outro daqui"):
            self.assertIn(trecho, spec)
        self.assertIn("O que ficou de fora e o risco", texto(".github/PULL_REQUEST_TEMPLATE.md"))
        self.assertIn("## A passagem entre sessões", texto("knowledge/processo.md"))
        self.assertIn("a interação acessível", texto("knowledge/processo.md"))
        self.assertIn("## A volta, escrita antes de instalar", texto("knowledge/versao-e-dependencias.md"))
        self.assertIn("o comando exato, o resultado esperado", texto("knowledge/README.md"))

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
            ("docker na outra", ["--stack", "outra", "--comandos", str(self.comandos), "--docker", True], "--docker não tem modelo"),
        ]
        for nome, troca, trecho in casos:
            with self.subTest(nome):
                args = {"--destino": str(self.raiz / f"novo-{nome.replace(' ', '-')}"), "--nome": "x", "--descricao": "d",
                        "--stack": "python-fastapi", "--dono": "a", "--base": str(self.base)}
                args.update(dict(zip(troca[::2], troca[1::2])))
                padrao = {"conta": "user", "responsavel": None, "comandos": None, "docker": False, "data": "2026-11-17",
                          "ramo": "main", "sem_git": True}
                padrao.update({k[2:].replace("-", "_"): v for k, v in args.items()})
                ns = montar.argparse.Namespace(**padrao)
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
            ("trivy sem hash", ".github/workflows/vigiar-imagem.yml", lambda t: t.replace("TRIVY_SHA256: c6e6", "TRIVY_SHA256: c6e"), "TRIVY_SHA256"),
            ("publicar sem hash", ".github/workflows/publicar-imagem.yml", lambda t: t.replace("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1", "actions/checkout@v7"), "publicar-imagem.yml: a ação"),
            ("claude cita o que sumiu", "CLAUDE.md", lambda t: t + "\nVer `knowledge/sumiu.md`.\n", "knowledge/sumiu.md`, que não existe"),
            ("ci derivou do claude", ".github/workflows/ci.yml", lambda t: t.replace('run: "python -m pytest -q -m smoke"', 'run: "python -m pytest -q -m fumaca"'), "derivou"),
            ("indice com pagina que nao existe", "knowledge/index.md", lambda t: t + "| `sumiu.md` | nunca |\n", "lista `sumiu.md`"),
            ("ci sem build", ".github/workflows/ci.yml", lambda t: t.replace("docker build --pull", "docker build"), "docker build --pull"),
        ]
        for nome, rel, mudar, trecho in plantados:
            with self.subTest(nome):
                copia = self.raiz / f"plantado-{nome.replace(' ', '-')}"
                shutil.copytree(self.projetos["docker-python"], copia, ignore=shutil.ignore_patterns(".git"))
                arq = copia / rel
                arq.write_bytes(mudar(arq.read_bytes().decode("utf-8")).encode("utf-8"))
                erros, _ = conferir.conferir(copia)
                self.assertTrue(any(trecho in e for e in erros), f"{nome}: {erros}")

    def test_conferir_acusa_a_imagem_pela_metade(self):
        for rel in ("Dockerfile", ".github/workflows/vigiar-imagem.yml"):
            with self.subTest(rel):
                copia = self.raiz / f"metade-{Path(rel).name}"
                shutil.copytree(self.projetos["docker-node"], copia, ignore=shutil.ignore_patterns(".git"))
                (copia / rel).unlink()
                erros, _ = conferir.conferir(copia)
                self.assertTrue(any(f"falta {rel}" in e for e in erros), erros)


if __name__ == "__main__":
    unittest.main()
