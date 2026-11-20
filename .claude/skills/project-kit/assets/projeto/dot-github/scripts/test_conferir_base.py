"""Os testes do conferir_base.py, sem rede: um repositório mínimo em pasta temporária, e cada deriva plantada."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import conferir_base as cb  # noqa: E402

CLAUDE = """# Projeto

O conhecimento fica em `knowledge/` (entrada: `knowledge/index.md`), e as decisões em `knowledge/decisions/NNN-slug.md`, pelo `000-modelo.md`.

- `docs/`: só a operação do sistema, quando ela existir.
- Sem credencial: ela fica no `.env`.
- `git merge origin/main` antes do PR.

## Stack e comandos

- `npm install`: instala.
- `npm run format:check`: confere o formato.
- `npm run typecheck`: o lint.
- `npm run smoke`: o smoke.
- `npm test`: os testes.
- `npm --silent audit`: as dependências com alerta.
- `python .githooks/hooks.py instalar`: liga os hooks.

## O fluxo

Nada aqui.
"""
CI = """jobs:
  ci:
    steps:
      - name: O formato
        run: "npm run format:check"
      - name: O lint
        run: npm run typecheck  # o lint da stack
      - name: O smoke
        run: "npm run smoke"
      - name: Os testes
        run: "npm test"
"""


class ConferirBase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = Path(self.tmp.name)
        self.escrever("CLAUDE.md", CLAUDE)
        self.escrever("AGENTS.md", "Leia o `CLAUDE.md` e o `knowledge/index.md`.\n")
        self.escrever(".github/workflows/ci.yml", CI)
        self.escrever(".githooks/hooks.py", "")
        self.escrever("package.json", json.dumps({"scripts": {"format:check": "x", "typecheck": "t", "smoke": "s", "test": "y"}}))
        self.escrever("knowledge/index.md", "| Página | Ler quando |\n|---|---|\n| `processo.md` | sempre |\n| `decisions/` | ao decidir |\n")
        self.escrever("knowledge/processo.md", "O spike mora em `spike/<tema>/`; o servidor em `src/servidor.ts`.\n")
        self.escrever("knowledge/decisions/000-modelo.md", "# ADR\n")
        self.escrever("src/servidor.ts", "")

    def tearDown(self):
        self.tmp.cleanup()

    def escrever(self, rel: str, conteudo: str) -> None:
        arq = self.raiz / rel
        arq.parent.mkdir(parents=True, exist_ok=True)
        arq.write_text(conteudo, encoding="utf-8")

    def rodar(self):
        return cb.conferir(self.raiz)

    def test_limpo(self):
        erros, avisos = self.rodar()
        self.assertEqual(erros, [])
        self.assertEqual(avisos, [])

    def test_caminho_que_sumiu_no_claude(self):
        (self.raiz / "knowledge/index.md").unlink()
        erros, _ = self.rodar()
        self.assertTrue(any("CLAUDE.md" in e and "knowledge/index.md" in e for e in erros), erros)
        self.assertTrue(any("AGENTS.md" in e for e in erros), erros)

    def test_comando_sem_script(self):
        self.escrever("package.json", json.dumps({"scripts": {"typecheck": "t", "smoke": "s", "test": "y"}}))
        erros, _ = self.rodar()
        self.assertTrue(any("format:check" in e and "não roda" in e for e in erros), erros)

    def test_arquivo_do_python_que_sumiu(self):
        (self.raiz / ".githooks/hooks.py").unlink()
        erros, _ = self.rodar()
        self.assertTrue(any("hooks.py" in e and "não existe" in e for e in erros), erros)

    def test_ci_derivou_do_claude(self):
        self.escrever(".github/workflows/ci.yml", CI.replace('"npm test"', '"npm run test:all"'))
        erros, _ = self.rodar()
        self.assertTrue(any("Os testes" in e and "derivou" in e for e in erros), erros)

    def test_passo_com_configuracao_antes_do_run_tambem_se_confere(self):
        ci = CI.replace('      - name: Os testes\n        run: "npm test"\n',
                        '      - name: Os testes\n        if: always()\n        env:\n          CI: "1"\n        shell: bash\n        run: "npm run test:all"\n')
        self.escrever(".github/workflows/ci.yml", ci)
        erros, _ = self.rodar()
        self.assertTrue(any("Os testes" in e and "derivou" in e for e in erros), erros)

    def test_aspas_simples_e_bloco_valem_como_o_comando(self):
        ci = CI.replace('run: "npm test"', "run: 'npm test'").replace(
            '        run: "npm run format:check"\n', '        run: |\n          npm run format:check\n')
        self.escrever(".github/workflows/ci.yml", ci)
        erros, _ = self.rodar()
        self.assertEqual(erros, [])

    def test_py_com_opcao_ainda_confere_o_arquivo(self):
        self.escrever("CLAUDE.md", CLAUDE.replace("`python .githooks/hooks.py instalar`", "`py -3 .githooks/sumiu.py instalar`"))
        erros, _ = self.rodar()
        self.assertTrue(any("sumiu.py" in e for e in erros), erros)

    def test_pagina_do_indice_que_nao_existe(self):
        (self.raiz / "knowledge/processo.md").unlink()
        erros, _ = self.rodar()
        self.assertTrue(any("index.md lista `processo.md`" in e for e in erros), erros)

    def test_pagina_orfa_e_aviso(self):
        self.escrever("knowledge/plano.md", "# Plano\n")
        erros, avisos = self.rodar()
        self.assertEqual(erros, [])
        self.assertTrue(any("plano.md" in a and "órfã" in a for a in avisos), avisos)

    def test_base_cita_codigo_que_saiu_e_aviso(self):
        (self.raiz / "src/servidor.ts").unlink()
        erros, avisos = self.rodar()
        self.assertEqual(erros, [])
        self.assertTrue(any("src/servidor.ts" in a for a in avisos), avisos)

    def test_so_o_que_esta_perto_do_caminho_o_isenta(self):
        # "para criar" não é "a criar": o caminho que sumiu na mesma frase continua cobrado
        self.escrever("AGENTS.md", "Leia o `CLAUDE.md`; use `knowledge/sumiu.md` para criar a issue.\n")
        erros, _ = self.rodar()
        self.assertTrue(any("knowledge/sumiu.md" in e for e in erros), erros)
        # e o "quando ela existir" isenta só o caminho perto dele
        self.escrever("AGENTS.md", "O `docs/novo.md`, quando ela existir.\n")
        erros, _ = self.rodar()
        self.assertEqual(erros, [])

    def test_passo_que_sumiu_do_ci(self):
        self.escrever(".github/workflows/ci.yml", CI.replace("- name: O lint", "- name: O lint (rápido)"))
        erros, _ = self.rodar()
        self.assertTrue(any("falta o passo 'O lint'" in e for e in erros), erros)

    def test_package_json_que_nao_e_objeto(self):
        self.escrever("package.json", "[]")
        erros, _ = self.rodar()
        self.assertTrue(any("objeto scripts" in e for e in erros), erros)

    def test_indice_que_falta_e_linha_com_link(self):
        self.escrever("knowledge/index.md", "| Página | Ler quando |\n|---|---|\n| [processo.md](processo.md) e o resto | sempre |\n| `sumiu.md` (e o diagrama) | nunca |\n")
        erros, _ = self.rodar()
        self.assertTrue(any("lista `sumiu.md`" in e for e in erros), erros)
        self.assertFalse(any("processo.md" in e for e in erros), erros)
        (self.raiz / "knowledge/index.md").unlink()
        erros, _ = self.rodar()
        self.assertTrue(any("falta o knowledge/index.md" in e for e in erros), erros)

    def test_o_log_nao_conta(self):
        self.escrever("knowledge/log.md", "## [2026-01-01] x | o `src/antigo.ts` saiu\n")
        self.escrever("knowledge/index.md", (self.raiz / "knowledge/index.md").read_text(encoding="utf-8") + "| `log.md` | o que aconteceu |\n")
        erros, avisos = self.rodar()
        self.assertEqual((erros, avisos), ([], []))


if __name__ == "__main__":
    unittest.main()
