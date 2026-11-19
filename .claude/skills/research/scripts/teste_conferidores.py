"""Teste negativo dos três conferidores da skill: casos plantados que cada um TEM de reprovar, ao lado de um
caso limpo que tem de passar ("tirar a guarda e ver falhar o teste dono"). Sem rede e sem o projeto: tudo nasce
numa pasta temporária, com material inventado, e o `confere_lugar.py` roda num repositório git de teste, com a
pasta pessoal apontada para ela.

  python -X utf8 .claude/skills/research/scripts/teste_conferidores.py     (de qualquer pasta)

Cada regra tem um caso direto e, onde a regra tem um jeito conhecido de escapar, um disfarçado. Roda todos os
casos, mostra cada um que falhar e sai com 1 se algum falhou; o erro no meio de um bloco (um `git` do teste que
falhou) vira falha com o nome do bloco e do último caso, e os outros blocos seguem. As **lacunas conhecidas** (o que
o script ainda não pega, listadas em `references/conferencias.md`, "Lacunas conhecidas") rodam e se mostram, sem
derrubar o teste; quando uma passar a ser pega, ela derruba o teste até virar caso e sair daquela lista. O `parafrase.py` roda com os
padrões de hoje (limiar 0,7 e K 3); quando uma calibração mudar os padrões, os casos de fronteira se reveem junto.
"""
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
FALHAS, LACUNAS = [], []
ULTIMO = ["(nenhum)"]  # o último caso que rodou, para dizer onde um bloco parou


def roda(script, *args, cwd=None, env_extra=None):
    env = dict(os.environ, PYTHONUTF8="1", **(env_extra or {}))
    r = subprocess.run([sys.executable, "-X", "utf8", str(AQUI / script), *map(str, args)], cwd=cwd,
                       capture_output=True, text=True, encoding="utf-8", env=env)
    return r.returncode, r.stdout + r.stderr


def caso(nome, cond, saida=""):
    ULTIMO[0] = nome
    print(("ok     " if cond else "FALHA  ") + nome)
    if not cond:
        FALHAS.append(nome)
        print("       " + saida.strip().replace("\n", "\n       ")[:1500])


def lacuna(nome, pegou, licao):
    if pegou:  # falha de propósito: a lacuna que fecha só avisando se perde numa rodada que sai com 0
        print(f"FECHOU {nome}: a lacuna passou a ser pega; vire caso e tire da lista ({licao})")
        FALHAS.append(f"lacuna fechou: {nome}")
    else:
        print(f"lacuna {nome} (conhecida: {licao})")
        LACUNAS.append(nome)


def grava(p, conteudo):
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(conteudo, (dict, list)):
        conteudo = json.dumps(conteudo, ensure_ascii=False, indent=1)
    p.write_bytes(conteudo.encode("utf-8"))


# ------------------------------------------------------------------------------------------- confere_rodada

def rotulos_limpos():
    return {
        "nota": "rodada inventada para o teste negativo",
        "consultas": [
            {"id": "c1", "frente": "perplexity", "texto": "AI wage premium 2026 study", "objetivo": "O1"},
            {"id": "c2", "frente": "gemini", "texto": "prêmio salarial de quem usa IA no Brasil em 2026", "objetivo": "O1"},
            {"id": "c3", "frente": "perplexity", "texto": "Seedance 2 preço por segundo de vídeo", "objetivo": "O2"},
            {"id": "c4", "frente": "perplexity", "texto": "Kling 2 preço por segundo de vídeo", "objetivo": "O2"},
        ],
        "objetivos": {"O1 qual é o prêmio salarial de IA": "alcancado",
                      "O2 quanto custam o Seedance e o Kling": "alcancado"},
        "fontes": [
            {"id": "estudo", "url": "https://exemplo.org/estudo", "origem": "primaria", "registro": "registravel",
             "destino": "fonte", "conteudo": "dado", "traz_novidade": True, "lido": "texto", "consulta": "c1"},
            {"id": "relatorio", "url": "https://outro.org/relatorio", "origem": "terceiro", "registro": "registravel",
             "destino": "descartada", "conteudo": "dado", "traz_novidade": False, "lido": "texto", "consulta": "c1"},
            {"id": "artigo", "url": "https://revista.org/artigo", "origem": "primaria", "registro": "so_citacao",
             "destino": "citacao", "conteudo": "dado", "traz_novidade": True, "lido": "resumo", "consulta": "c2"},
        ],
    }


SAIDA_SEM_CITACAO = {"provider": "gemini", "query": "prêmio salarial de IA", "answer":
                     "O prêmio é de 37,5% para quem usa IA, segundo o barômetro, com o modelo `wage-v2`.",
                     "results": [], "citations": [], "error": None}
ACHADOS = "# Achados\n\nO prêmio salarial medido é de 37,5% (barômetro, 2026), com o modelo `wage-v2`.\n"
PRODUTOS = "Seedance 2,Kling 2"


def monta_rodada(base, rot=None, saidas=None, nativa=None, achados=ACHADOS):
    pasta = base / "2026-11-20-teste"
    if pasta.exists():
        for p in sorted(pasta.rglob("*"), reverse=True):
            p.unlink() if p.is_file() else p.rmdir()
    grava(pasta / "q1-perplexity.json", {"provider": "perplexity", "query": "AI wage premium 2026", "answer": "x",
                                         "results": [{"url": "https://www.exemplo.org/estudo/?utm_source=busca"}],
                                         "citations": ["https://outro.org/relatorio"], "error": None})
    grava(pasta / "q2-gemini.json", SAIDA_SEM_CITACAO)
    grava(pasta / "q2-nativa.md", nativa if nativa is not None else "- https://revista.org/artigo\n")
    for nome, d in (saidas or {}).items():
        grava(pasta / nome, d)
    grava(base / "rotulos.json", rot if rot is not None else rotulos_limpos())
    grava(base / "achados.md", achados)
    return pasta


def conferir(base, pasta, produtos=PRODUTOS):
    return roda("confere_rodada.py", pasta, base / "rotulos.json", "--achados", base / "achados.md",
                "--produtos", produtos, "--publico-br")


def teste_confere_rodada(base):
    cod, out = conferir(base, monta_rodada(base))
    caso("rodada: a rodada limpa passa (código 0)", cod == 0, out)

    def reprova(nome, trecho, rot=None, produtos=PRODUTOS, **kw):
        cod, out = conferir(base, monta_rodada(base, rot=rot, **kw), produtos)
        caso(f"rodada: {nome}", cod == 1 and trecho in out, out)

    r = rotulos_limpos()
    r["consultas"][1]["texto"] = "AI wage premium Brazil 2026"
    reprova("(a) objetivo sem consulta em português", "DESVIO sem consulta em português", r)
    r = rotulos_limpos()
    r["consultas"][1]["objetivo"] = "O2"  # disfarce: há consulta em português, mas ela serve a outro objetivo
    reprova("(a) disfarçado: a consulta em português ligada a outro objetivo", "DESVIO sem consulta em português", r)
    r = rotulos_limpos()
    del r["consultas"][0]["objetivo"]
    reprova("(a) consulta sem o campo objetivo", "DESVIO consulta sem objetivo", r)
    reprova("(b) produto que nenhuma consulta nomeia", "DESVIO nenhuma consulta nomeia Veo 3",
            produtos=PRODUTOS + ",Veo 3")
    r = rotulos_limpos()
    r["consultas"][2]["texto"] = "Seedance 2.5 preço por segundo de vídeo"  # disfarce: outra versão
    reprova("(b) disfarçado: só outra versão do produto (2.5 por 2)", "DESVIO nenhuma consulta nomeia Seedance 2", r)
    reprova("(c) URL das saídas sem linha nos rótulos", "DESVIO sem linha: https://naorotulada.org/x",
            saidas={"q3-perplexity.json": {"query": "q", "answer": "x", "results": [{"url": "https://naorotulada.org/x"}],
                                           "citations": [], "error": None}})
    r = rotulos_limpos()
    r["fontes"].append({"id": "video", "url": "https://youtu.be/abc", "origem": "primaria", "registro": "registravel",
                        "destino": "fonte", "conteudo": "dado", "traz_novidade": True, "lido": "texto"})
    reprova("(c) disfarçado: o mesmo endereço com outra caixa no caminho (outro vídeo)",
            "DESVIO sem linha: https://youtu.be/AbC", r,
            nativa="- https://revista.org/artigo\n- https://youtu.be/AbC\n")
    r = rotulos_limpos()
    r["fontes"].append(dict(r["fontes"][0], id="estudo-2", url="https://www.exemplo.org/estudo?utm_source=y",
                            origem="terceiro"))
    reprova("(c) a mesma URL em duas linhas com rótulos opostos", "DESVIO mesma url em 2 linhas", r)
    r = rotulos_limpos()
    r["fontes"][2]["lido"] = "nao abriu"
    reprova("(d) só citação sem nenhuma rota registrada", "DESVIO artigo", r)
    r = rotulos_limpos()
    r["fontes"][2]["lido"] = "resumo da busca; a página deu 404, fora do ar, e não tentei a Wayback"
    reprova("(d) disfarçado: a Wayback citada com negação (\"não tentei a Wayback\")", "DESVIO artigo", r)
    # o outro lado da (d): a negação de outra coisa, na oração de antes, não apaga a rota registrada depois da vírgula
    r = rotulos_limpos()
    r["fontes"][2]["lido"] = "resumo da busca; o PDF veio bloqueado sem login, pelo Chrome"
    cod, out = conferir(base, monta_rodada(base, rot=r))
    caso("rodada: (d) \"sem login, pelo Chrome\": a rota registrada depois da negação de outra coisa passa", cod == 0, out)
    r["fontes"][2]["lido"] = "resumo da busca; o PDF veio bloqueado sem login pelo Chrome"
    cod, out = conferir(base, monta_rodada(base, rot=r))
    lacuna("rodada: (d) \"sem login pelo Chrome\", sem a vírgula, devia passar", cod == 0,
           "`references/conferencias.md`, \"Lacunas conhecidas\", a janela da negação na (d)")
    r["fontes"][2]["lido"] = "resumo da busca; a página deu 404, fora do ar, e não tentei web.archive.org"
    cod, out = conferir(base, monta_rodada(base, rot=r))
    lacuna("rodada: (d) \"não tentei web.archive.org\" devia reprovar (o \"web\" empurra o \"não\" da janela)",
           cod == 1 and "DESVIO artigo" in out,
           "`references/conferencias.md`, \"Lacunas conhecidas\", a janela da negação na (d)")
    reprova("(e) número da resposta sem citação fora do rascunho", "DESVIO q2-gemini.json",
            achados="# Achados\n\nO prêmio é alto (barômetro, 2026), com o modelo `wage-v2`.\n")
    reprova("(e) termo em código da resposta sem citação fora do rascunho", "DESVIO q2-gemini.json",
            achados="# Achados\n\nO prêmio salarial medido é de 37,5% (barômetro, 2026).\n")
    reprova("(e) disfarçado: o número com outra casa no rascunho (37,55%)", "DESVIO q2-gemini.json",
            achados="# Achados\n\nO prêmio medido é de 37,55% (barômetro), com o modelo `wage-v2`.\n")
    cod, out = conferir(base, monta_rodada(base, achados=ACHADOS.replace("37,5%", "37.5%")))
    caso("rodada: (e) o mesmo número com ponto no lugar da vírgula passa", cod == 0, out)
    cod, out = conferir(base, monta_rodada(base, rot=["não é objeto"]))
    caso("rodada: rótulos que não são um objeto JSON saem com 2", cod == 2, out)


# ------------------------------------------------------------------------------------------------ parafrase

FONTE = """# O método das três caixas

O método das três caixas organiza o trabalho semanal em tarefas urgentes, tarefas importantes e tarefas adiáveis. Cada caixa recebe um limite fixo de itens, definido no começo da semana pela própria equipe. Quando uma caixa enche, nenhuma tarefa nova entra nela até que outra saia concluída. A equipe revisa as caixas toda sexta-feira e move as tarefas que mudaram de prioridade. Os autores mediram o método em doze equipes de software durante seis meses seguidos. As equipes que seguiram o limite entregaram mais tarefas importantes e menos retrabalho no trimestre. As equipes que ignoraram o limite voltaram ao padrão antigo depois de poucas semanas. O estudo não comparou o método com outras formas de priorização conhecidas no mercado.
"""
CABECA = "---\ntitulo: Ficha de teste\n---\n\n# Ficha\n\n"
COLADA = [  # a frase da fonte encurtada, com uma palavra trocada aqui e ali, na ordem dela
    "O método das três caixas organiza o trabalho semanal em tarefas urgentes, importantes e adiáveis.",
    "Cada caixa recebe um limite fixo de itens, definido no início da semana pela equipe.",
    "Quando uma caixa enche, nenhuma tarefa nova entra até que outra saia concluída.",
    "A equipe revisa as caixas toda sexta-feira e move as tarefas que mudaram de prioridade.",
]
PROPRIA = ("Um jeito de priorizar que põe teto no número de itens de cada grupo. A pesquisa acompanhou times de "
           "programação por meio ano e viu ganho nas entregas que pesam. Quem furou o teto regrediu rápido. Falta "
           "comparar com outras abordagens.\n")


def teste_parafrase(base):
    fonte = base / "fonte.txt"
    grava(fonte, FONTE)

    def mede(nome, corpo, *extra, fonte_=fonte):
        f = base / f"{nome}.md"
        grava(f, CABECA + corpo)
        return roda("parafrase.py", "--ficha", f, "--fonte", fonte_, *extra)

    cod, out = mede("propria", PROPRIA)
    caso("paráfrase: a ficha em palavras próprias passa (código 0)", cod == 0, out)
    cod, out = mede("colada", " ".join(COLADA) + "\n")
    caso("paráfrase: a frase da fonte encurtada, quatro seguidas na ordem, reprova (código 1)",
         cod == 1 and "Trecho colado" in out, out)
    tabela = "| Passo | O que diz |\n|---|---|\n" + "".join(f"| {i} | {s} |\n" for i, s in enumerate(COLADA, 1))
    cod, out = mede("tabela", tabela)
    caso("paráfrase: disfarçada em células de tabela com texto corrido, reprova (código 1)",
         cod == 1 and "Trecho colado" in out, out)
    lista = "".join(f"- {s}\n" for s in COLADA)
    cod, out = mede("lista", lista)
    caso("paráfrase: disfarçada em itens de lista, reprova (código 1)", cod == 1 and "Trecho colado" in out, out)
    misturada = f"{COLADA[0]} {COLADA[1]}\n\n{PROPRIA}\n{COLADA[2]} {COLADA[3]}\n"
    cod, out = mede("duas-e-duas", misturada)
    caso("paráfrase: duas coladas, texto próprio no meio, duas coladas: abaixo do K 3, passa (código 0)",
         cod == 0 and "coladas: 4" in out, out)
    cod, out = mede("duas-e-duas-k2", misturada, "--k", "2")
    caso("paráfrase: as mesmas com --k 2 reprovam (código 1)", cod == 1, out)
    aspas = "\n\n".join(f"“{s}”" for s in COLADA) + "\n"  # um parágrafo por citação: sem tirar as aspas, reprovaria
    cod, out = mede("aspas", aspas)
    caso("paráfrase: a frase entre aspas é citação e fica fora da conta (código 0)", cod == 0, out)
    ingles = ("The three boxes method splits the weekly work into urgent, important and deferrable tasks. Each box "
              "has a fixed limit of items that the team sets at the start of the week. When a box is full, no new task "
              "goes into it until another one is done.\n")
    cod, out = mede("ingles", ingles)
    caso("paráfrase: ficha em outra língua que a fonte sai com 3, não com 0", cod == 3, out)
    cod, out = roda("parafrase.py", "--ficha", base / "nao-existe.md", "--fonte", fonte)
    caso("paráfrase: ficha que não abre sai com 2", cod == 2, out)
    chines = base / "fonte-zh.txt"
    grava(chines, "三个盒子的方法把每周的工作分成紧急任务、重要任务和可以推迟的任务。每个盒子都有固定的上限，由团队在一周开始时确定。"
                  "盒子满了以后，在另一项任务完成之前，不能再放入新的任务。\n")
    cod, out = mede("sobre-chines", " ".join(COLADA[:3]) + "\n", fonte_=chines)
    lacuna("paráfrase: fonte em chinês e ficha em português devia sair com 3", cod == 3,
           "`references/conferencias.md`, \"Lacunas conhecidas\", a língua no `parafrase.py`")


# --------------------------------------------------------------------------------------------- confere_lugar

GITIGNORE = "originals/\n.env\n__pycache__/\n*.py[cod]\n.claude/settings.local.json\nrascunhos/\n"
# o estado local do Claude Code, que um `.git/info/exclude` pode tirar do git
EXCLUDE = "**/.claude/scheduled_tasks.lock\n**/.claude/scheduled_tasks.json\n**/.claude/routines/.state/\n" \
          "**/.claude/worktrees/\n**/.claude/checkpoints/\n**/.claude/mailbox/\n**/.claude/agent-registry.json\n" \
          "**/.claude/agent-memory-local\n**/.claude/first-run\n**/.claude/assistant-daemon-state.json\n"
# uma linha por regra do exclude, na raiz e numa subpasta (o `**/` vale em qualquer nível)
ESTADO = [f"{nivel}.claude/{p}" for nivel in ("", "personal/projeto/")
          for p in ("scheduled_tasks.lock", "scheduled_tasks.json", "routines/.state/rotina.json", "worktrees/t/x.txt",
                    "checkpoints/a/b.json", "mailbox/m1.json", "agent-registry.json", "agent-memory-local/nota.md",
                    "first-run", "assistant-daemon-state.json")]
RODADA = "knowledge/research-rounds/2026-11-20-teste"


def git(repo, *args):
    """O git do repositório de teste; a falha sobe com o comando e o que o git disse, e o `bloco()` diz o caso."""
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} saiu com {r.returncode}: {r.stderr.strip()[:300]}")
    return r.stdout


def monta_repo(base):
    repo = base / "repo"
    repo.mkdir()
    git(repo, "init", "-q")
    grava(repo / ".gitignore", GITIGNORE)
    exclude = Path(git(repo, "rev-parse", "--git-dir").strip())
    grava((exclude if exclude.is_absolute() else repo / exclude) / "info" / "exclude", EXCLUDE)
    grava(repo / "knowledge/README.md", "# base\n")
    for p in ESTADO:
        grava(repo / p, "{}")
    grava(repo / f"{RODADA}/originals/fontes/artigo.html", "<p>texto protegido</p>")
    grava(repo / f"{RODADA}/fontes/protegidas.json", [{"id": "artigo", "url": "https://revista.org/artigo"}])
    return repo


def lugar(repo, home, *args):
    return roda("confere_lugar.py", *args, cwd=repo, env_extra={"USERPROFILE": str(home), "HOME": str(home)})


def teste_confere_lugar(base):
    home = base / "casa"
    home.mkdir()
    repo = monta_repo(base)
    cod, out = lugar(repo, home, "--repo")
    caso("lugar: o repositório limpo, com o estado do .claude/ que o exclude tira do git, passa (código 0)", cod == 0, out)
    grava(repo / ".env", "PERPLEXITY_API_KEY=COLE_SUA_CHAVE_AQUI\n")
    cod, out = lugar(repo, home, "--repo")
    caso("lugar: o .env fora do git é lugar aceito (código 0)", cod == 0, out)
    cod, out = lugar(repo, home, "--vault")
    caso("lugar: --vault é sinônimo de --repo (código 0)", cod == 0, out)
    cod, out = lugar(repo, home, RODADA)
    caso("lugar: a rodada limpa passa (código 0)", cod == 0, out)

    grava(repo / "rascunhos/copia-da-pagina.html", "<p>x</p>")
    cod, out = lugar(repo, home, "--repo")
    caso("lugar: arquivo ignorado fora dos lugares da tabela reprova", cod == 1 and "rascunhos/copia-da-pagina.html" in out, out)
    (repo / "rascunhos/copia-da-pagina.html").unlink()
    # o exclude não é permissão: ele fica fora do git e da revisão, e uma linha nova nele não cala a conferência
    exclude = Path(git(repo, "rev-parse", "--git-path", "info/exclude").strip())
    exclude = exclude if exclude.is_absolute() else repo / exclude
    grava(exclude, EXCLUDE + "copias-locais/\n")
    grava(repo / "copias-locais/pagina.html", "<p>x</p>")
    cod, out = lugar(repo, home, "--repo")
    caso("lugar: disfarçado: arquivo que só uma linha nova do exclude tira do git reprova",
         cod == 1 and "copias-locais/pagina.html" in out, out)
    (repo / "copias-locais/pagina.html").unlink()
    grava(exclude, EXCLUDE)
    grava(repo / ".claude/checkpoints-velhos/x.json", "{}")
    grava(repo / ".gitignore", GITIGNORE + ".claude/checkpoints-velhos/\n")
    cod, out = lugar(repo, home, "--repo")
    caso("lugar: disfarçado: pasta do .claude/ com nome parecido com o do estado, fora da lista, reprova",
         cod == 1 and ".claude/checkpoints-velhos/x.json" in out, out)
    (repo / ".claude/checkpoints-velhos/x.json").unlink()
    grava(repo / ".gitignore", GITIGNORE)
    grava(repo / ".claude/worktrees/tarefa/knowledge/sources/originals/texto.txt", "x")
    cod, out = lugar(repo, home, "--repo")
    caso("lugar: originals/ dentro de uma cópia de trabalho do Claude Code reprova",
         cod == 1 and "originals/ dentro de uma cópia de trabalho" in out, out)
    (repo / ".claude/worktrees/tarefa/knowledge/sources/originals/texto.txt").unlink()
    grava(repo / "knowledge/sources/2026-11-20-ficha-nova.md", "---\ntitulo: x\nurl: https://nao.org/x\n---\n\n# Ficha\n")
    cod, out = lugar(repo, home, "--repo")
    caso("lugar: ficha nova sem integral e sem original guardado é aviso (código 0, com o aviso)",
         cod == 0 and "ficha de obra protegida sem original guardado" in out, out)
    grava(repo / "knowledge/sources/originals/2026-11-20-ficha-nova.html", "<p>x</p>")
    cod, out = lugar(repo, home, "--repo")
    caso("lugar: a mesma ficha com o original em knowledge/sources/originals/ passa sem o aviso",
         cod == 0 and "sem original guardado" not in out, out)
    (repo / "knowledge/sources/originals/2026-11-20-ficha-nova.html").unlink()
    (repo / "knowledge/sources/2026-11-20-ficha-nova.md").unlink()

    grava(repo / f"{RODADA}/fontes/artigo.html", "<p>texto protegido</p>")
    cod, out = lugar(repo, home, RODADA)
    caso("lugar: texto protegido em fontes/ da pasta versionada reprova",
         cod == 1 and "texto protegido na pasta versionada: fontes/artigo.html" in out, out)
    (repo / f"{RODADA}/fontes/artigo.html").unlink()
    grava(repo / f"{RODADA}/notas/artigo.html", "<p>texto protegido</p>")
    cod, out = lugar(repo, home, RODADA)
    caso("lugar: disfarçado: o texto protegido em notas/, com o id e extensão de página, reprova",
         cod == 1 and "texto protegido na pasta versionada: notas/artigo.html" in out, out)
    (repo / f"{RODADA}/notas/artigo.html").unlink()
    (repo / f"{RODADA}/originals/fontes/artigo.html").unlink()
    cod, out = lugar(repo, home, RODADA)
    caso("lugar: texto com linha em protegidas.json sem cópia em originals/ reprova",
         cod == 1 and "texto lido sem cópia em originals/: artigo" in out, out)
    grava(repo / f"{RODADA}/originals/fontes/artigo.html", "<p>texto protegido</p>")
    git(repo, "add", "-f", f"{RODADA}/originals/fontes/artigo.html")
    cod, out = lugar(repo, home, RODADA)
    caso("lugar: arquivo de originals/ já no git reprova", cod == 1 and "arquivo(s) de originals/ no git" in out, out)
    git(repo, "rm", "-q", "--cached", f"{RODADA}/originals/fontes/artigo.html")
    grava(repo / f"{RODADA}/notas/achados.md", "Ele disse: “" + " ".join(["palavra"] * 30) + "”.\n")
    cod, out = lugar(repo, home, RODADA)
    caso("lugar: citação longa numa nota é aviso, não desvio (código 0, com o aviso)",
         cod == 0 and "possível citação longa" in out, out)


def teste_do_proprio_teste(base):
    """As duas guardas do próprio teste: a lacuna que fecha derruba o teste, e o erro no meio de um bloco vira
    falha com o nome do bloco e do último caso, sem parar os outros blocos."""
    antes = list(FALHAS)
    with contextlib.redirect_stdout(io.StringIO()):
        lacuna("plantada", True, "nenhuma")
        fechou = FALHAS[len(antes):]
        del FALHAS[len(antes):]
        bloco("plantado", lambda b: (caso("antes do erro", True), git(b, "rev-parse", "--verify", "nao-existe")), base)
        parou = FALHAS[len(antes):]
        del FALHAS[len(antes):]
    caso("próprio teste: a lacuna que passou a ser pega conta como falha", len(fechou) == 1, repr(fechou))
    caso("próprio teste: o erro do git no meio do bloco vira falha com o bloco, o caso e o comando",
         len(parou) == 1 and "plantado" in parou[0] and "antes do erro" in parou[0] and "rev-parse" in parou[0],
         repr(parou))


def bloco(nome, f, base):
    """Roda um bloco; o erro no meio dele (um `git` do teste que falhou, um arquivo que não abre) vira falha com o
    nome do bloco e do último caso que passou por `caso()`, e os outros blocos seguem."""
    (base / nome).mkdir()
    ULTIMO[0] = "(nenhum)"
    try:
        f(base / nome)
    except Exception as e:  # noqa: BLE001 — qualquer erro do bloco vira falha dele, com o motivo
        caso(f"{nome}: o bloco parou com erro depois do caso \"{ULTIMO[0]}\": {type(e).__name__}: {e}", False)


def teste_nomes_codex(base):
    """A saída do Codex entra pelo mesmo nome das outras frentes."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("confere_rodada", Path(__file__).with_name("confere_rodada.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    caso("a saída do Codex (q1-codex.json, codex-q2.json) é lida como as outras",
         bool(m.SAIDA_JSON_RE.match("q1-codex.json")) and bool(m.SAIDA_JSON_RE.match("codex-q2.json"))
         and bool(m.SAIDA_JSON_RE.match("q3-gemini.json")) and not m.SAIDA_JSON_RE.match("q1-chatgpt.json"))


def principal():
    with tempfile.TemporaryDirectory(prefix="teste-conferidores-") as t:
        base = Path(t)
        for nome, f in (("proprio", teste_do_proprio_teste), ("rodada", teste_confere_rodada),
                        ("parafrase", teste_parafrase), ("lugar", teste_confere_lugar), ("codex", teste_nomes_codex)):
            bloco(nome, f, base)
    print(f"\n{len(FALHAS)} falha(s); {len(LACUNAS)} lacuna(s) conhecida(s), que não derrubam o teste")
    return 1 if FALHAS else 0


if __name__ == "__main__":
    sys.exit(principal())
