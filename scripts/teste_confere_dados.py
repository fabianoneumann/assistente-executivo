#!/usr/bin/env python3
"""Casos do confere_dados.py, sem rede: cada padrão acha o que deve e deixa passar o que não é dado.

Uso, da raiz: python -X utf8 scripts/teste_confere_dados.py
Monta um repositório temporário com os arquivos de cada caso, roda o conferidor sobre ele e compara.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

# (nome do caso, conteúdo do arquivo, tipo que deve sair ou None)
CASOS = [
    ("e-mail simples", "escreva para ana.souza" + "@empresa.com.br", "e-mail"),
    ("e-mails em chaves, como nos artigos", "{wang, nlp.li, zef}" + "@gmail.com", "e-mail"),
    ("e-mails em chaves com espaço antes do @", "{luq, jin} " + "@seu.edu.cn", "e-mail"),
    ("e-mail de exemplo passa", "contato@example.com", None),
    ("chave da Perplexity", "PERPLEXITY_API_KEY=pplx-" + "a1b2c3d4e5" * 4, "chave"),
    ("marcador do .env.example passa", "PERPLEXITY_API_KEY=COLE_SUA_CHAVE_AQUI", None),
    ("caminho de usuário do Windows", "abra " + "C:" + "\\Users\\alguem\\x.md", "caminho de usuário"),
    ("telefone", "ligue (45) " + "99876-5432", "telefone"),
    ("hash de URL de artigo passa", "https://proceedings.example.org/paper/" + "ab12" * 8 + "-Paper.pdf", None),
    ("ação do GitHub fixada por hash passa", "- uses: actions/checkout@" + "3d3c42e5" * 5 + " # v7", None),
    ("hash de 40 sem dono/acao segue acusado", "commit=" + "3d3c42e5" * 5, "chave"),
    ("hash de 41 colado em ação segue acusado", "uses: actions/checkout@" + "3d3c42e5" * 5 + "a", "chave"),
    ("endereço de bucket", "https://pub-" + "0f" * 16 + ".r2.dev/x.jpg", "endereço de bucket"),
    ("SHA-256 de arquivo baixado passa", "baixado em 18/11, SHA-256 `" + "b1032b7c" * 8 + "`", None),
    ("hex de 64 sem SHA-256 segue acusado", "segredo " + "b1032b7c" * 8, "chave"),
]


def main() -> int:
    falhas = 0
    for nome, conteudo, esperado in CASOS:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            (repo / "scripts").mkdir(parents=True)
            shutil.copy(RAIZ / "scripts/confere_dados.py", repo / "scripts/confere_dados.py")
            (repo / "nota.md").write_text(conteudo + "\n", encoding="utf-8")
            r = subprocess.run([sys.executable, "-X", "utf8", str(repo / "scripts/confere_dados.py"), "nota.md"],
                               capture_output=True, text=True, encoding="utf-8")
            achou = [l for l in r.stdout.splitlines() if l.startswith("nota.md:")]
            ok = (not achou and r.returncode == 0) if esperado is None else (
                r.returncode == 1 and any(f"[{esperado}]" in l for l in achou))
            print(("ok   " if ok else "FALHA") + f" {nome}" + ("" if ok else f": {achou or r.stdout.strip()[-200:]}"))
            falhas += not ok
    falhas += teste_privacidade()
    falhas += teste_ignorados()
    falhas += teste_vendorizado()
    falhas += teste_excecao_por_arquivo()
    print("TODOS OK" if not falhas else f"{falhas} falha(s)")
    return 1 if falhas else 0


def teste_vendorizado() -> int:
    """Em `*.bundled.js`, a regra genérica de KEY não acusa o código minificado; a chave de prefixo conhecido, sim."""
    falhas = 0
    for nome, conteudo, esperado in [
        ("minificado com key: passa", 'var a={ke' + 'y:"' + "abcdefghij" * 3 + '"};', None),
        ("chave da Anthropic no minificado segue acusada", 'var k="sk-ant-' + "a1b2c3d4e5" * 3 + '";', "chave"),
    ]:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            (repo / "scripts").mkdir(parents=True)
            shutil.copy(RAIZ / "scripts/confere_dados.py", repo / "scripts/confere_dados.py")
            (repo / "lib.bundled.js").write_text(conteudo + "\n", encoding="utf-8")
            r = subprocess.run([sys.executable, "-X", "utf8", str(repo / "scripts/confere_dados.py"), "lib.bundled.js"],
                               capture_output=True, text=True, encoding="utf-8")
            achou = [l for l in r.stdout.splitlines() if l.startswith("lib.bundled.js:")]
            ok = (not achou and r.returncode == 0) if esperado is None else (
                r.returncode == 1 and any(f"[{esperado}]" in l for l in achou))
            print(("ok   " if ok else "FALHA") + f" {nome}" + ("" if ok else f": {achou or r.stdout.strip()[-200:]}"))
            falhas += not ok
    return falhas


def teste_ignorados() -> int:
    """Com o git, o que o .gitignore tira (o laudo em originals/, o .env) não é achado; o originals/ que iria ao git é."""
    falhas = 0
    casos = [
        ("laudo em originals/ ignorado passa", "originals/\n", "health/medical/exams/originals/laudo.txt", None),
        (".env ignorado passa", ".env\n", ".env", None),
        ("originals/ sem .gitignore segue acusado", "", "health/medical/exams/originals/laudo.txt", "terceiro"),
    ]
    for nome, gitignore, rel, esperado in casos:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            (repo / "scripts").mkdir(parents=True)
            shutil.copy(RAIZ / "scripts/confere_dados.py", repo / "scripts/confere_dados.py")
            (repo / rel).parent.mkdir(parents=True, exist_ok=True)
            (repo / rel).write_text("PERPLEXITY_API_KEY=pplx-" + "a1b2c3d4e5" * 4 + "\nfulano" + "@empresa.com.br\n", encoding="utf-8")
            if gitignore:
                (repo / ".gitignore").write_text(gitignore, encoding="utf-8")
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            r = subprocess.run([sys.executable, "-X", "utf8", str(repo / "scripts/confere_dados.py"), Path(rel).parts[0]],
                               capture_output=True, text=True, encoding="utf-8")
            achou = [l for l in r.stdout.splitlines() if l.startswith(rel)]
            ok = (not achou and r.returncode == 0) if esperado is None else (
                r.returncode == 1 and any(f"[{esperado}]" in l for l in achou))
            print(("ok   " if ok else "FALHA") + f" {nome}" + ("" if ok else f": {achou or r.stdout.strip()[-200:]}"))
            falhas += not ok
    return falhas


def teste_excecao_por_arquivo() -> int:
    """`!arquivo::texto` no arquivo de termos libera o texto só naquele arquivo; em outro, segue acusado."""
    falhas = 0
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        (repo / "scripts").mkdir(parents=True)
        shutil.copy(RAIZ / "scripts/confere_dados.py", repo / "scripts/confere_dados.py")
        (repo / "LICENSE").write_text("Copyright (c) 2026 Beltrana Exemplo\n", encoding="utf-8")
        (repo / "nota.md").write_text("escrito por Beltrana Exemplo\n", encoding="utf-8")
        termos = Path(tmp) / "termos.txt"
        termos.write_text("Beltrana\n!LICENSE::Beltrana Exemplo\n", encoding="utf-8")
        r = subprocess.run([sys.executable, "-X", "utf8", str(repo / "scripts/confere_dados.py"), "--termos", str(termos),
                            "LICENSE", "nota.md"], capture_output=True, text=True, encoding="utf-8")
        ok = (r.returncode == 1 and not any(l.startswith("LICENSE:") for l in r.stdout.splitlines())
              and any(l.startswith("nota.md:") and "[termo próprio]" in l for l in r.stdout.splitlines()))
        print(("ok   " if ok else "FALHA") + " exceção só no arquivo dela: o titular no LICENSE passa, o nome em outro arquivo não"
              + ("" if ok else f": {r.stdout.strip()[-300:]}"))
        falhas += not ok
    return falhas


GH = "https://github.com/alguem/meu-assistente.git"
EM_BRANCO = "<p>Modelo em branco.</p>\n"

# cada caso: os arquivos (caminho: conteúdo), os remotos, o que o gh responde por repositório ("sem gh" levanta
# FileNotFoundError; ausente, o gh falha como sem login), o .gitignore, os argumentos, o código esperado,
# se o [PARE] aparece, os repositórios que o gh deve consultar e se um [AVISO] é esperado
CASOS_PRIVACIDADE = [
    dict(nome="só o modelo, remoto público: passa sem consultar o gh",
         arquivos={"finance/README.md": "# x\n", "maps/guides/swot.md": "# x\n", "maps/board/index.html": "x",
                   "maps/board/ikigai.html": EM_BRANCO},
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=0, pare=False, consultas=[]),
    dict(nome="registro pessoal, remoto público: para",
         arquivos={"finance/README.md": "# x\n", "finance/personal/overview.md": "# x\n"},
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=1, pare=True, consultas=["alguem/meu-assistente"]),
    dict(nome="o [PARE] traz o comando com o repositório e não mostra o caminho do registro",
         arquivos={"health/medical/exams/2027-01-01-exame-sensivel.md": "# x\n"},
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=1, pare=True, consultas=["alguem/meu-assistente"],
         contem=["gh repo edit alguem/meu-assistente --visibility private"], nao_contem=["exame-sensivel"]),
    dict(nome="mapa preenchido, remoto público: para",
         arquivos={"maps/roda-da-vida/2027-01-01.md": "# x\n"},
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=1, pare=True, consultas=["alguem/meu-assistente"]),
    dict(nome="página do quadro preenchida no lugar, remoto público: para",
         arquivos={"maps/board/roda-da-vida.html": "<p>as notas de quem usa</p>\n"},
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=1, pare=True, consultas=["alguem/meu-assistente"]),
    dict(nome="README numa pasta nova conta como registro",
         arquivos={"health/training/current/README.md": "# as minhas notas\n"},
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=1, pare=True, consultas=["alguem/meu-assistente"]),
    dict(nome="arquivo novo dentro de maps/guides/ conta como registro",
         arquivos={"maps/guides/consultas/2027.md": "# x\n"},
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=1, pare=True, consultas=["alguem/meu-assistente"]),
    dict(nome="registro fora do git pelo .gitignore, remoto público: passa",
         arquivos={"finance/personal/overview.md": "# x\n"}, gitignore="finance/**/*.md\n!**/README.md\n",
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=0, pare=False, consultas=[]),
    dict(nome="registro pessoal, remoto privado: passa",
         arquivos={"health/training/current/plan.md": "# x\n"},
         gh={"alguem/meu-assistente": "PRIVATE"}, codigo=0, pare=False, consultas=["alguem/meu-assistente"]),
    dict(nome="registro pessoal, sem o gh instalado: sai com 3 (não conferiu) e diz o que falta",
         arquivos={"health/training/current/plan.md": "# x\n"},
         gh="sem gh", codigo=3, pare=False, consultas=["alguem/meu-assistente"], aviso=True,
         contem=["[NÃO CONFERIU]", "gh auth login"]),
    dict(nome="registro pessoal, gh sem login: sai com 3",
         arquivos={"health/training/current/plan.md": "# x\n"},
         gh={}, codigo=3, pare=False, consultas=["alguem/meu-assistente"], aviso=True, contem=["[NÃO CONFERIU]"]),
    dict(nome="sem registro pessoal e sem o gh: nada muda, sai com 0",
         arquivos={"finance/README.md": "# x\n"},
         gh="sem gh", codigo=0, pare=False, consultas=[], nao_contem=["[NÃO CONFERIU]"]),
    dict(nome="um remoto público e outro sem conferir: o achado vence, sai com 1",
         arquivos={"finance/personal/overview.md": "# x\n"},
         remotos=[("origin", GH), ("outro", "https://github.com/alguem/outro-repo.git")],
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=1, pare=True,
         consultas=["alguem/meu-assistente", "alguem/outro-repo"], aviso=True, nao_contem=["[NÃO CONFERIU]"]),
    dict(nome="remoto em SSH e em HTTPS do mesmo repositório: uma consulta, um achado",
         arquivos={"finance/personal/overview.md": "# x\n"},
         remotos=[("origin", GH), ("espelho", "git" + "@github.com:alguem/meu-assistente.git")],
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=1, pare=True, consultas=["alguem/meu-assistente"], achados=1),
    dict(nome="remoto fora do GitHub, com nome parecido: avisa e não consulta",
         arquivos={"finance/personal/overview.md": "# x\n"},
         remotos=[("origin", "https://notgithub.com/alguem/meu-assistente.git")],
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=0, pare=False, consultas=[], aviso=True),
    dict(nome="com pastas na linha de comando, a privacidade também roda",
         arquivos={"finance/personal/overview.md": "# x\n"}, args=["finance"],
         gh={"alguem/meu-assistente": "PUBLIC"}, codigo=1, pare=True, consultas=["alguem/meu-assistente"]),
]


def teste_privacidade() -> int:
    """O [PARE] do repositório público com registro pessoal, com o `gh` simulado no subprocess (sem rede).

    A `visibilidade` real roda: só a chamada ao executável `gh` é trocada pela resposta do caso."""
    import contextlib
    import importlib.util
    import io
    falhas = 0
    for caso in CASOS_PRIVACIDADE:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            (repo / "scripts").mkdir(parents=True)
            shutil.copy(RAIZ / "scripts/confere_dados.py", repo / "scripts/confere_dados.py")
            for rel, conteudo in caso["arquivos"].items():
                (repo / rel).parent.mkdir(parents=True, exist_ok=True)
                (repo / rel).write_text(conteudo, encoding="utf-8")
            if caso.get("gitignore"):
                (repo / ".gitignore").write_text(caso["gitignore"], encoding="utf-8")
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            for nome_remoto, url in caso.get("remotos", [("origin", GH)]):
                subprocess.run(["git", "-C", str(repo), "remote", "add", nome_remoto, url], check=True)
            spec = importlib.util.spec_from_file_location("confere_dados_teste", repo / "scripts/confere_dados.py")
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            consultas, roda_de_verdade = [], mod.subprocess.run

            def run(cmd, *args, _gh=caso["gh"], **kw):
                if cmd[0] != "gh":
                    return roda_de_verdade(cmd, *args, **kw)
                consultas.append(cmd[3])
                if _gh == "sem gh":
                    raise FileNotFoundError("gh")
                v = _gh.get(cmd[3])
                return subprocess.CompletedProcess(cmd, 0 if v else 1, (v.lower() + "\n") if v else "",
                                                   "" if v else "gh auth login")
            mod.subprocess.run = run
            saida = io.StringIO()
            try:
                with contextlib.redirect_stdout(saida):
                    r = mod.main(caso.get("args", []))
            finally:
                mod.subprocess.run = roda_de_verdade
            texto = saida.getvalue()
            ok = (r == caso["codigo"] and ("[PARE]" in texto) == caso["pare"] and consultas == caso["consultas"]
                  and ("[AVISO]" in texto) == caso.get("aviso", False)
                  and all(x in texto for x in caso.get("contem", []))
                  and not any(x in texto for x in caso.get("nao_contem", []))
                  and ("achados" not in caso or texto.count("[repositório público]") == caso["achados"]))
            print(("ok   " if ok else "FALHA") + f" {caso['nome']}"
                  + ("" if ok else f": código {r}, gh {consultas}, {texto.strip()[-300:]}"))
            falhas += not ok
    return falhas


if __name__ == "__main__":
    sys.exit(main())
