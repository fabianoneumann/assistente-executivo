"""Espelha no repositório a memória e a configuração do Claude Code, que só existem no seu computador.

DESLIGADO POR PADRÃO. Só ligue se o seu repositório for PRIVADO: as memórias vão ao git com o resto.
Como ligar e o porquê estão em assistant/README.md e em decisions/memoria-e-evolucao.md.

Uso, à mão ou pelos hooks SessionStart e SessionEnd (quando você os ligar no .claude/settings.json):
    python .claude/hooks/espelhar-assistente.py                    # espelha e confere, mostrando o resultado
    python .claude/hooks/espelhar-assistente.py --hook             # o mesmo, sem imprimir nada (modo dos hooks)
    python .claude/hooks/espelhar-assistente.py --conferir         # só confere a origem contra o espelho
    python .claude/hooks/espelhar-assistente.py --restaurar PASTA  # restaura o espelho numa pasta vazia e confere

Origem e destino:
- ~/.claude/projects/<repositório>/memory/   -> assistant/memory/
- ~/.claude/settings.json e statusline.js    -> assistant/config/ (o settings.json fica de fora se tiver um bloco "env",
  onde costumam morar chaves)
O <repositório> é o checkout principal, achado pelo git: rodando de dentro de uma worktree, o espelho vai para o
principal, porque a memória é uma só para todas as worktrees. Se o git falhar, vale a pasta onde o script está.
Ficam fora de propósito: ~/.claude/mcp.json (pode trazer token), as credenciais, os caches, o histórico das conversas
e ~/.claude/skills/synced/ (vem da conta e se baixa de novo).
Para testar sem tocar na sua memória real: ESPELHO_CASA=<pasta falsa no lugar de ~/.claude> e ESPELHO_DESTINO=<pasta>.

Copia em binário só o que mudou e tira do espelho o que saiu da origem (o histórico fica no git). Depois confere
arquivo a arquivo por sha256, contra a origem relida do disco, e reescreve assistant/espelho.json (sem data, para o
diff só mudar quando o conteúdo muda), só quando a conferência bateu. Diferença ou erro vai para
assistant/.erro.log, fora do git, e o código de saída é 1. No modo --hook não imprime nada: a saída do SessionStart
entraria no contexto da sessão.
"""
import hashlib, json, os, re, shutil, subprocess, sys, traceback


def checkout_principal():
    """A raiz do checkout principal do repositório, mesmo rodando de dentro de uma worktree."""
    aqui = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    try:
        r = subprocess.run(["git", "-C", aqui, "rev-parse", "--path-format=absolute", "--git-common-dir"],
                           capture_output=True, text=True, timeout=15, stdin=subprocess.DEVNULL)
        comum = os.path.normpath(r.stdout.strip()) if r.returncode == 0 else ""
        if comum and os.path.basename(comum) == ".git" and os.path.isdir(comum):
            return os.path.dirname(comum)
    except (OSError, subprocess.SubprocessError):
        pass
    return aqui


REPO = checkout_principal()
CASA = os.environ.get("ESPELHO_CASA") or os.path.join(os.path.expanduser("~"), ".claude")
# O Claude Code nomeia a pasta do projeto trocando por "-" todo caractere que não é letra, número ou "-".
MEMORIA = os.path.join(CASA, "projects", re.sub(r"[^A-Za-z0-9-]", "-", REPO), "memory")
DESTINO = os.environ.get("ESPELHO_DESTINO") or os.path.join(REPO, "assistant")
INDICE = os.path.join(DESTINO, "espelho.json")
ERRO = os.path.join(DESTINO, ".erro.log")
CONFIG = ("settings.json", "statusline.js")


def hash_de(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 16), b""):
            h.update(bloco)
    return h.hexdigest()


def settings_sem_env(caminho):
    """O settings.json só entra se não tiver um bloco "env" (onde costumam morar chaves)."""
    try:
        with open(caminho, encoding="utf-8") as f:
            return "env" not in json.load(f)
    except (OSError, ValueError):
        return False


def origens():
    """{caminho relativo no espelho: caminho de origem}, só arquivos que existem."""
    mapa = {}
    if os.path.isdir(MEMORIA):
        for raiz, _, arquivos in os.walk(MEMORIA):
            for nome in arquivos:
                origem = os.path.join(raiz, nome)
                rel = os.path.relpath(origem, MEMORIA).replace("\\", "/")
                mapa["memory/" + rel] = origem
    for nome in CONFIG:
        origem = os.path.join(CASA, nome)
        if os.path.isfile(origem) and (nome != "settings.json" or settings_sem_env(origem)):
            mapa["config/" + nome] = origem
    return mapa


def no_espelho(base):
    """Os arquivos que o espelho tem em memory/ e config/, relativos a base."""
    achados = set()
    for parte in ("memory", "config"):
        pasta = os.path.join(base, parte)
        for raiz, _, arquivos in os.walk(pasta):
            for nome in arquivos:
                achados.add(os.path.relpath(os.path.join(raiz, nome), base).replace("\\", "/"))
    return achados


def espelhar(mapa):
    for rel, origem in mapa.items():
        alvo = os.path.join(DESTINO, *rel.split("/"))
        if os.path.isfile(alvo) and hash_de(alvo) == hash_de(origem):
            continue
        os.makedirs(os.path.dirname(alvo), exist_ok=True)
        shutil.copyfile(origem, alvo)
    for rel in no_espelho(DESTINO) - set(mapa):
        os.remove(os.path.join(DESTINO, *rel.split("/")))


def conferir(mapa, base):
    """Lista de problemas: arquivo que falta, que sobra ou cujo hash não bate."""
    problemas = []
    tem = no_espelho(base)
    for rel, origem in sorted(mapa.items()):
        alvo = os.path.join(base, *rel.split("/"))
        if rel not in tem:
            problemas.append(f"falta no espelho: {rel}")
        elif hash_de(alvo) != hash_de(origem):
            problemas.append(f"hash diferente: {rel}")
    for rel in sorted(tem - set(mapa)):
        problemas.append(f"sobra no espelho: {rel}")
    return problemas


def gravar_indice(mapa):
    dados = {rel: hash_de(os.path.join(DESTINO, *rel.split("/"))) for rel in sorted(mapa)}
    texto = json.dumps({"arquivos": dados}, ensure_ascii=False, indent=1) + "\n"
    with open(INDICE, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def restaurar(pasta):
    """Copia o espelho para uma pasta vazia e confere contra o espelho.json e contra a origem."""
    if os.path.exists(pasta) and os.listdir(pasta):
        raise SystemExit(f"a pasta {pasta} não está vazia")
    for parte in ("memory", "config"):
        if os.path.isdir(os.path.join(DESTINO, parte)):
            shutil.copytree(os.path.join(DESTINO, parte), os.path.join(pasta, parte))
    with open(INDICE, encoding="utf-8") as f:
        indice = json.load(f)["arquivos"]
    problemas = []
    for rel, h in indice.items():
        alvo = os.path.join(pasta, *rel.split("/"))
        if not os.path.isfile(alvo):
            problemas.append(f"falta na restauração: {rel}")
        elif hash_de(alvo) != h:
            problemas.append(f"hash da restauração não bate com o espelho.json: {rel}")
    problemas += [p.replace("espelho", "restauração", 1) for p in conferir(origens(), pasta)]
    return problemas


def main():
    args = sys.argv[1:]
    calado = "--hook" in args
    try:
        mapa = origens()
        if not any(rel.startswith("memory/") for rel in mapa):
            raise RuntimeError(f"pasta de memória não encontrada ou vazia: {MEMORIA}")
        if "--restaurar" in args:
            problemas = restaurar(args[args.index("--restaurar") + 1])
        elif "--conferir" in args:
            problemas = conferir(mapa, DESTINO)
        else:
            os.makedirs(DESTINO, exist_ok=True)
            espelhar(mapa)
            problemas = conferir(mapa, DESTINO)
            if not problemas:  # o espelho.json só registra a cópia que bateu com a origem
                gravar_indice(mapa)
    except Exception:
        problemas = ["erro:\n" + traceback.format_exc()]
    if problemas:
        os.makedirs(DESTINO, exist_ok=True)
        with open(ERRO, "w", encoding="utf-8") as f:
            f.write("\n".join(problemas) + "\n")
    elif os.path.exists(ERRO) and "--restaurar" not in args:
        os.remove(ERRO)
    if not calado:
        print("\n".join(problemas) if problemas else f"ok: {len(origens())} arquivos conferidos por sha256")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
