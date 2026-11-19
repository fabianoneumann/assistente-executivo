"""O hook do fluxo: as travas do agente no `gh pr create`, no `gh pr merge` e no `git commit`.

A casca `.claude/hooks/fluxo.sh` o chama no PreToolUse do Bash e do PowerShell (`.claude/settings.json`), com o
gatilho no argumento (`pr-create`, `pr-merge`, `commit`) e o evento do Claude Code no stdin. Só a biblioteca padrão.
A trava só recusa e diz o que falta, ou avisa; nunca pergunta. Passar é não imprimir nada (um `allow` pularia o
pedido de permissão de quem trabalha). Sem rede, deixa passar e avisa. O porquê de cada regra: `knowledge/travas.md`.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

PRAZO = 25  # segundos para todas as chamadas juntas, abaixo dos 30 do hook: o hook morto pelo prazo passaria calado
SECAO = "## Antes de abrir este PR"
CONFIG = Path(__file__).resolve().parents[2] / ".githooks" / "config.json"


class Fluxo:
    """Uma decisão do hook. `rodar(args, cwd) -> (código, saída, erro)` chama o git e o gh, e os testes o trocam."""

    def __init__(self, rodar=None, base: str | None = None, sem: set[str] | None = None):
        self.rodar = rodar or rodar_de_verdade(time.monotonic() + PRAZO)
        self.base = base or base_do_config()
        self.sem = sem or set()  # as travas desligadas, para o teste que confere a recusa falhando sem ela
        self.avisos: list[str] = []

    def git(self, cwd: str, *args: str) -> tuple[int, str, str]:
        return self.rodar(["git", *args], cwd)

    # ---- a decisão ----------------------------------------------------------------------------------------------
    def decidir(self, gatilho: str, comando: str, cwd: str, shell: str = "Bash") -> tuple[str, str]:
        """Devolve ("recusa", motivo), ("aviso", texto) ou ("passa", "")."""
        try:
            tokens = tokenizar(comando, powershell=shell == "PowerShell")
        except ValueError:
            if re.search(r"\bgh(\.exe)?\s+pr\s+(create|new|merge)\b", comando):
                return "aviso", ("O hook do fluxo não conseguiu ler esta linha (aspas sem fechar?) e deixou o comando "
                                 "passar sem conferir; rode o `gh pr` sozinho, numa linha simples.")
            return "passa", ""
        segmentos = separar(tokens)
        if gatilho == "commit":
            return self.no_commit(diretorio_do_C(segmentos, cwd))
        sub = "merge" if gatilho == "pr-merge" else None
        achado = achar_gh_pr(segmentos, sub)
        if achado is None:
            return "passa", ""  # a linha só cita o comando (num texto, num laço): o hook dispara, mas não é o comando
        args = achado
        if len(segmentos) > 1 and self.ligada("encadeado"):
            return "recusa", (
                "rode o `gh pr` sozinho, numa chamada própria: na linha encadeada o hook julgaria o estado de antes "
                "dos outros comandos. O push e o corpo vão em chamadas antes."
            )
        if tem(args, "--repo", "-R"):
            return "passa", ""  # outro repositório: as regras são deste
        if not self.mesmo_repo(cwd):
            return "passa", ""
        motivo = self.no_merge(args, cwd) if gatilho == "pr-merge" else self.no_pr(args, cwd)
        if motivo:
            return "recusa", motivo
        if self.avisos:
            return "aviso", " ".join(self.avisos)
        return "passa", ""

    def ligada(self, nome: str) -> bool:
        return nome not in self.sem

    def mesmo_repo(self, cwd: str) -> bool:
        projeto = os.environ.get("CLAUDE_PROJECT_DIR")
        if not projeto:
            return True
        a, b = self.git(cwd, "rev-parse", "--git-common-dir"), self.git(projeto, "rev-parse", "--git-common-dir")
        if a[0] or b[0]:
            return True
        return Path(cwd, a[1].strip()).resolve() == Path(projeto, b[1].strip()).resolve()

    # ---- gh pr create -------------------------------------------------------------------------------------------
    def no_pr(self, args: list[str], cwd: str) -> str | None:
        proibida = next((f for f in ("--fill", "--fill-first", "--fill-verbose", "-f", "--body", "-b") if tem(args, f)), None)
        if proibida and self.ligada("corpo_proibido"):
            return (f"`gh pr create {proibida}`: o corpo do PR é o .github/PULL_REQUEST_TEMPLATE.md preenchido, gravado "
                    "fora do repositório e passado por --body-file (o --fill ignora o modelo; o --body quebra o markdown).")
        corpo = valor(args, "--body-file", "-F")
        if not corpo and self.ligada("sem_body_file"):
            return ("`gh pr create` sem --body-file: o corpo do PR é o .github/PULL_REQUEST_TEMPLATE.md preenchido, "
                    "gravado fora do repositório.")
        topo = self.git(cwd, "rev-parse", "--show-toplevel")
        if corpo:
            motivo = self.conferir_corpo(resolver(corpo, cwd, self.rodar), Path(topo[1].strip()) if not topo[0] else None)
            if motivo:
                return motivo
        head = valor(args, "--head", "-H")
        return self.conferir_sincronia(cwd, valor(args, "--base", "-B") or self.base, head.split(":")[-1] if head else None)

    def conferir_corpo(self, caminho: Path, topo: Path | None) -> str | None:
        if topo and self.ligada("corpo_no_repo") and dentro(caminho, topo):
            return f"o --body-file {caminho} está dentro do repositório: grave-o fora, para ele não ir num commit."
        try:
            texto = caminho.read_text(encoding="utf-8").replace("\r\n", "\n")
        except OSError:
            self.avisos.append(f"O hook não achou o --body-file {caminho} e não conferiu o corpo do PR.")
            return None
        limpo = sem_codigo(texto)
        if "<!--" in limpo and self.ligada("corpo_comentario"):
            return "o corpo ainda tem comentário `<!-- -->` do modelo: as instruções saem antes de abrir o PR."
        if re.search(r"^(Closes|Fixes|Refs) #\s*$", limpo, re.M) and self.ligada("corpo_sem_numero"):
            return "a linha `Closes #` (ou `Refs #`) está sem o número da issue; sem issue própria, apague a linha."
        inicio = limpo.find(SECAO)
        if inicio < 0:
            if self.ligada("corpo_sem_checklist"):
                return f'o corpo não tem a seção "{SECAO[3:]}": ele é o .github/PULL_REQUEST_TEMPLATE.md preenchido.'
            return None
        resto = limpo[inicio + len(SECAO):]
        fim = re.search(r"^## ", resto, re.M)
        vazia = re.search(r"^\s*- \[ \] .*$", resto[: fim.start()] if fim else resto, re.M)
        if vazia and self.ligada("corpo_caixa_vazia"):
            return (f"o checklist tem caixa vazia ({vazia.group(0).strip()!r}). Caixa em branco é \"não feito\": "
                    "marque, ou marque com N/A se não se aplica.")
        return None

    def conferir_sincronia(self, cwd: str, base: str, head: str | None = None) -> str | None:
        """A branch enviada (o HEAD igual ao remoto) e sem atraso em relação à base. Com --head (a branch de outro
        lugar), confere que ela existe no remoto e, se o commit dela está aqui, que contém a base."""
        branch = head or self.git(cwd, "rev-parse", "--abbrev-ref", "HEAD")[1].strip()
        cabeca = None if head else self.git(cwd, "rev-parse", "HEAD")[1].strip()
        codigo, saida, _ = self.git(cwd, "ls-remote", "origin", f"refs/heads/{base}", f"refs/heads/{branch}")
        if codigo:
            self.avisos.append("O hook não alcançou o remoto (sem rede?) e não conferiu se a branch está enviada e sincronizada.")
            return None
        remotas = {linha.split()[1]: linha.split()[0] for linha in saida.splitlines() if len(linha.split()) == 2}
        na_origem = remotas.get(f"refs/heads/{branch}")
        if self.ligada("branch_enviada"):
            if not na_origem:
                return f"a branch {branch} não foi enviada: faça o `git push -u origin {branch}` numa chamada antes."
            if cabeca and na_origem != cabeca:
                return f"a branch {branch} tem commit que não está no remoto: faça o `git push` numa chamada antes."
        ponta_base = remotas.get(f"refs/heads/{base}")
        ponta = na_origem if head else "HEAD"
        if ponta_base and ponta and self.ligada("branch_atras"):
            codigo = self.git(cwd, "merge-base", "--is-ancestor", ponta_base, ponta)[0]
            if codigo == 1 or (codigo and not head):  # sem o commit da base aqui, a branch local não a contém
                return (f"a branch está atrás de origin/{base}: `git fetch` e `git merge origin/{base}`, o push, "
                        "e o PR depois. O CI de um PR só prova contra a base que ele viu.")
            if codigo:
                self.avisos.append(f"O commit da branch {branch} não está neste clone: o hook não conferiu se ela contém a base.")
        return None

    # ---- gh pr merge --------------------------------------------------------------------------------------------
    def no_merge(self, args: list[str], cwd: str) -> str | None:
        if tem(args, "--auto"):
            return None  # o próprio GitHub espera o CI
        alvo = posicionais(args, COM_VALOR_NO_MERGE)[:1]
        codigo, saida, erro = self.rodar(["gh", "pr", "checks", *alvo, "--json", "name,bucket"], cwd)
        try:
            checks = json.loads(saida) if saida.strip() else None
        except ValueError:
            checks = None
        if checks == [] and self.ligada("ci_sem_checks"):
            return "o PR não tem nenhum check: o CI nem começou. Espere o CI rodar (ou confira o workflow) antes do merge."
        if not isinstance(checks, list):
            if "no checks reported" in erro and self.ligada("ci_sem_checks"):
                return "o PR não tem nenhum check: o CI nem começou. Espere o CI rodar (ou confira o workflow) antes do merge."
            self.avisos.append(f"O hook não leu o CI do PR (gh saiu com {codigo}; sem rede?) e não conferiu se está verde.")
            return None
        falhos = [c.get("name", "?") for c in checks if c.get("bucket") in ("fail", "cancel")]
        if falhos and self.ligada("ci_vermelho"):
            return f"o CI do PR está vermelho ({', '.join(falhos)}): corrija na branch antes do merge."
        rodando = [c.get("name", "?") for c in checks if c.get("bucket") == "pending"]
        if rodando and self.ligada("ci_rodando"):
            return f"o CI do PR ainda está rodando ({', '.join(rodando)}): espere terminar antes do merge."
        return None

    # ---- git commit ---------------------------------------------------------------------------------------------
    def no_commit(self, cwd: str) -> tuple[str, str]:
        if self.git(cwd, "rev-parse", "--git-dir")[0]:
            return "passa", ""  # fora de um repositório
        _, saida, _ = self.git(cwd, "config", "--get", "core.hooksPath")
        if saida.strip() != ".githooks" and self.ligada("hooks_desligados"):
            return "aviso", ("Os hooks do git estão desligados neste clone: o commit sai sem o formatador e sem o log "
                             "conferidos. Ligue com `python .githooks/hooks.py instalar`.")
        return "passa", ""


# ---- o leitor da linha ------------------------------------------------------------------------------------------
OPERADORES = ("&&", "||", ";", "|", "&", "\n")


def tokenizar(linha: str, powershell: bool = False) -> list[str]:
    """Separa a linha em palavras e operadores, respeitando as aspas. No Bash a barra invertida escapa; no
    PowerShell é letra (o escape é a crase), por causa dos caminhos do Windows."""
    linha = linha.replace("\\\r\n", " ").replace("\\\n", " ") if not powershell else linha.replace("`\r\n", " ").replace("`\n", " ")
    tokens: list[str] = []
    atual, tem_atual, i = "", False, 0
    while i < len(linha):
        c = linha[i]
        if c in "'\"":
            trecho, i = ler_aspas(linha, i, powershell)
            atual, tem_atual = atual + trecho, True
            continue
        if c == "\\" and not powershell and i + 1 < len(linha):
            atual, tem_atual, i = atual + linha[i + 1], True, i + 2
            continue
        op = next((o for o in OPERADORES if linha.startswith(o, i)), None)
        if op and not (op == "&" and (linha[i - 1:i] in (">", "<") or linha[i + 1:i + 2] == ">")):
            if tem_atual:
                tokens.append(atual)
            tokens.append(op)
            atual, tem_atual, i = "", False, i + len(op)
            continue
        if c.isspace():
            if tem_atual:
                tokens.append(atual)
            atual, tem_atual, i = "", False, i + 1
            continue
        atual, tem_atual, i = atual + c, True, i + 1
    if tem_atual:
        tokens.append(atual)
    return tokens


def ler_aspas(linha: str, i: int, powershell: bool) -> tuple[str, int]:
    """O trecho entre aspas que começa em `i`, e onde ele acaba. No Bash, dentro das duplas, a barra escapa a aspa;
    no PowerShell, a aspa dobrada e a crase escapam. As simples do Bash não escapam nada."""
    aspa, j, trecho = linha[i], i + 1, ""
    while j < len(linha):
        c = linha[j]
        if aspa == '"' and not powershell and c == "\\" and linha[j + 1:j + 2] in ('"', "\\", "$", "`"):
            trecho, j = trecho + linha[j + 1], j + 2
        elif powershell and c == "`" and aspa == '"' and j + 1 < len(linha):
            trecho, j = trecho + linha[j + 1], j + 2
        elif c == aspa and powershell and linha[j + 1:j + 2] == aspa:
            trecho, j = trecho + aspa, j + 2
        elif c == aspa:
            return trecho, j + 1
        else:
            trecho, j = trecho + c, j + 1
    raise ValueError("aspas abertas")


def separar(tokens: list[str]) -> list[list[str]]:
    """Os comandos da linha. O `&` do PowerShell no começo é o operador de chamada, e não um segundo comando."""
    segmentos, atual = [], []
    for i, t in enumerate(tokens):
        if t in OPERADORES and not (t == "&" and i == 0):
            if atual:
                segmentos.append(atual)
            atual = []
        elif t != "&":
            atual.append(t)
    if atual:
        segmentos.append(atual)
    return segmentos


def achar_gh_pr(segmentos: list[list[str]], sub: str | None) -> list[str] | None:
    """Os argumentos depois de `gh pr create` (ou `new`), ou de `gh pr merge`, em qualquer comando da linha."""
    subs = ("merge",) if sub == "merge" else ("create", "new")
    for seg in segmentos:
        for i, t in enumerate(seg):
            nome = re.split(r"[\\/]", t)[-1].lower()
            if nome in ("gh", "gh.exe") and seg[i + 1:i + 2] == ["pr"] and seg[i + 2:i + 3] and seg[i + 2] in subs:
                return seg[i + 3:]
    return None


COM_VALOR_NO_MERGE = {"--subject", "-t", "--body", "-b", "--body-file", "-F", "--match-head-commit",
                      "--author-email", "-A", "--repo", "-R"}


def posicionais(args: list[str], com_valor: set[str]) -> list[str]:
    """Os argumentos que não são flag nem valor de flag (no `gh pr merge`, o número, o link ou a branch do PR)."""
    soltos, pular = [], False
    for a in args:
        if pular:
            pular = False
        elif a in com_valor:
            pular = True
        elif not a.startswith("-"):
            soltos.append(a)
    return soltos


def diretorio_do_C(segmentos: list[list[str]], cwd: str) -> str:
    """O diretório do `git -C <dir> commit`, que o settings.json também manda para cá; sem `-C`, o da sessão."""
    for seg in segmentos:
        for i, t in enumerate(seg[:-2]):
            if re.split(r"[\\/]", t)[-1].lower() in ("git", "git.exe") and seg[i + 1] == "-C" and "commit" in seg[i + 3:]:
                return str(Path(cwd) / seg[i + 2])
    return cwd


def tem(args: list[str], *flags: str) -> bool:
    return any(a == f or (f.startswith("--") and a.startswith(f + "=")) for a in args for f in flags)


def valor(args: list[str], *flags: str) -> str | None:
    for i, a in enumerate(args):
        for f in flags:
            if a == f and i + 1 < len(args):
                return args[i + 1]
            if f.startswith("--") and a.startswith(f + "="):
                return a[len(f) + 1:]
    return None


def sem_codigo(texto: str) -> str:
    """O texto sem os blocos e os trechos de código, onde `<!--` e `- [ ]` são exemplo, e não instrução."""
    texto = re.sub(r"^```.*?^```", "", texto, flags=re.M | re.S)
    return re.sub(r"`[^`\n]*`", "", texto)


def resolver(caminho: str, cwd: str, rodar) -> Path:
    """O caminho do --body-file como o shell o veria: o `~`, as variáveis e, no Windows, o `/c/...` do Git Bash."""
    caminho = re.sub(r"\$env:(\w+)", lambda m: os.environ.get(m.group(1), m.group(0)), caminho)
    caminho = os.path.expandvars(os.path.expanduser(caminho))
    if os.name == "nt" and caminho.startswith("/"):
        m = re.match(r"^/([a-zA-Z])(/.*)?$", caminho)
        if m:
            caminho = f"{m.group(1).upper()}:{m.group(2) or '/'}"
        else:
            codigo, saida, _ = rodar(["cygpath", "-w", caminho], cwd)
            if codigo == 0 and saida.strip():
                caminho = saida.strip()
    p = Path(caminho)
    return p if p.is_absolute() else Path(cwd) / p


def dentro(caminho: Path, pasta: Path) -> bool:
    try:
        caminho.resolve().relative_to(pasta.resolve())
        return True
    except ValueError:
        return False


def base_do_config() -> str:
    try:
        return json.loads(CONFIG.read_text(encoding="utf-8")).get("base", "main")
    except (OSError, ValueError):
        return "main"


def rodar_de_verdade(prazo: float):
    def rodar(args: list[str], cwd: str) -> tuple[int, str, str]:
        resta = prazo - time.monotonic()
        if resta <= 1:
            return 124, "", "o prazo do hook acabou"
        try:
            r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                               timeout=min(resta, 12), env={**os.environ, "GIT_TERMINAL_PROMPT": "0", "GH_PROMPT_DISABLED": "1"})
            return r.returncode, r.stdout, r.stderr
        except (OSError, subprocess.TimeoutExpired) as e:
            return 127, "", str(e)
    return rodar


def saida(decisao: str, texto: str) -> str:
    if decisao == "recusa":
        return json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                  "permissionDecisionReason": f"Trava do fluxo: {texto}"}}, ensure_ascii=False)
    if decisao == "aviso":
        return json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": texto}}, ensure_ascii=False)
    return ""


def main() -> int:
    gatilho = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        evento = json.loads(sys.stdin.read() or "{}")
        comando = (evento.get("tool_input") or {}).get("command", "")
        cwd = evento.get("cwd") or os.getcwd()
        decisao, texto = Fluxo().decidir(gatilho, comando, cwd, evento.get("tool_name", "Bash"))
    except Exception as e:  # nada passa calado: o erro do próprio hook vira aviso
        decisao, texto = "aviso", f"O hook do fluxo falhou ({e!r}) e deixou o comando passar sem conferir (knowledge/travas.md)."
    sys.stdout.write(saida(decisao, texto))
    return 0


if __name__ == "__main__":
    sys.exit(main())
