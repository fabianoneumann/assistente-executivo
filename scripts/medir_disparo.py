"""Mede o disparo da descrição de uma skill do projeto: para cada pedido, roda `claude -p` algumas vezes e anota qual
skill o modelo chamou primeiro (pela ferramenta Skill), sem deixar a sessão trabalhar.

É o laço de medida da `skill-creator` ("Description Optimization", o `run_eval.py`), adaptado a um projeto com várias skills e ao Windows:
- o `run_eval.py` usa `select` em pipe, que no Windows não funciona; aqui a leitura vai numa thread;
- ele mede uma descrição solta, como comando novo em `.claude/commands/`, ao lado da skill real (que pode tomar o
  disparo); aqui mede a skill como está, contra as vizinhas de verdade, e registra qual foi chamada;
- a sessão roda numa cópia mínima do projeto (o `CLAUDE.md`, o `index.md`, as skills e o `settings.json` sem os
  hooks), numa pasta temporária: os hooks do projeto não rodam dezenas de vezes, e nada se grava no projeto. Sem MCP
  (`--strict-mcp-config`) e sem as ferramentas que escrevem ou saem para a rede. O que é do usuário (o
  `~/.claude/settings.json`, os plugins e as skills dele) carrega de propósito: é a lista de skills que a sessão real
  vê; se o settings do usuário tiver hooks, eles rodam a cada rodada.

Cada rodada se grava em disco ao acabar, com andamento na tela; rodar de novo pula as rodadas que responderam e
refaz as que não (timeout, erro do CLI). A chave de cada rodada leva o pedido, o modelo e o hash dos SKILL.md do projeto:
mudou uma descrição, as rodadas antigas não servem e tudo roda de novo. Usa o
login do Claude Code (o `ANTHROPIC_API_KEY` sai do ambiente do subprocesso, para não tomar o lugar do login).

Uso:
  python -X utf8 scripts/medir_disparo.py --skill idea-capture --casos casos.json --saida <pasta>
         [--rodadas 3] [--modelo claude-opus-5-5] [--paralelo 4] [--timeout 150]

casos.json: lista de {"query": "...", "should_trigger": true|false, "esperada": "<skill certa, opcional>"}.
Saída: <pasta>/rodadas/*.json (uma por rodada), <pasta>/resumo.json e o resumo na tela. Código 0 sempre que mediu
tudo; 2 se alguma rodada não chegou a uma resposta (timeout ou erro do CLI), que fica fora da taxa e é contada à parte.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import queue
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]  # scripts/ fica na raiz do projeto
# o que a sessão de teste não pode usar: escrever, rodar comando, sair para a rede, lançar agente
SEM = ["Bash", "PowerShell", "Edit", "Write", "NotebookEdit", "Agent", "WebFetch", "WebSearch", "Monitor"]
MAX_FERRAMENTAS = 8  # sem chamar skill depois de tantas ferramentas, a rodada conta como "nenhuma"
IGNORA = shutil.ignore_patterns(".venv", "originals", "evals", "__pycache__", "*-workspace", "node_modules")


def montar_projeto(raiz: Path, destino: Path) -> None:
    """A cópia mínima do projeto: o roteador, o índice, as skills e o settings.json sem os hooks."""
    for nome in ("CLAUDE.md", "index.md"):
        if (raiz / nome).is_file():
            shutil.copy2(raiz / nome, destino / nome)
    (destino / ".claude").mkdir(parents=True, exist_ok=True)
    shutil.copytree(raiz / ".claude/skills", destino / ".claude/skills", ignore=IGNORA)
    cfg = raiz / ".claude/settings.json"
    if cfg.is_file():
        d = json.loads(cfg.read_text(encoding="utf-8"))
        d.pop("hooks", None)
        (destino / ".claude/settings.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def eventos(proc: subprocess.Popen, fila: queue.Queue) -> None:
    for linha in proc.stdout:
        fila.put(linha)
    fila.put(None)


def uma_rodada(query: str, projeto: Path, modelo: str | None, timeout: int, claude: str) -> dict:
    """Roda o pedido e devolve a primeira skill chamada (ou None), as ferramentas antes dela e como terminou."""
    cmd = [claude, "-p", query, "--output-format", "stream-json", "--verbose", "--strict-mcp-config",
           "--disallowedTools", *SEM, "--max-turns", "6"]
    if modelo:
        cmd += ["--model", modelo]
    env = {k: v for k, v in os.environ.items() if k not in ("CLAUDECODE", "ANTHROPIC_API_KEY")}
    t0 = time.time()
    proc = subprocess.Popen(cmd, cwd=projeto, env=env, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                            stdin=subprocess.DEVNULL, text=True, encoding="utf-8", errors="replace")
    fila: queue.Queue = queue.Queue()
    threading.Thread(target=eventos, args=(proc, fila), daemon=True).start()
    ferramentas, skill, fim = [], None, "timeout"
    try:
        while time.time() - t0 < timeout:
            try:
                linha = fila.get(timeout=1)
            except queue.Empty:
                continue
            if linha is None:  # o CLI fechou a saída sem o evento "result": não é resposta
                fim = f"CLI saiu sem resultado (código {proc.wait()})"
                break
            try:
                ev = json.loads(linha)
            except json.JSONDecodeError:
                continue
            if ev.get("type") == "assistant":
                for c in ev.get("message", {}).get("content", []):
                    if c.get("type") != "tool_use":
                        continue
                    if c.get("name") == "Skill":
                        skill = str(c.get("input", {}).get("skill", "")).strip().lstrip("/")
                        break
                    ferramentas.append(c.get("name"))
                if skill:
                    fim = "chamou skill"
                    break
                if len(ferramentas) >= MAX_FERRAMENTAS:
                    fim = f"{MAX_FERRAMENTAS} ferramentas sem skill"
                    break
            elif ev.get("type") == "result":
                sub = ev.get("subtype", "")
                if sub == "success" and not ev.get("is_error"):
                    fim = "terminou sem skill"
                elif sub == "error_max_turns":  # usou os turnos todos sem chamar skill: o modelo decidiu
                    fim = "limite de turnos sem skill"
                else:  # erro de login, sobrecarga, erro da API: não é resposta, vai para sem_resposta
                    fim = f"erro do CLI: {sub or 'sem subtipo'}"
                break
    finally:
        if proc.poll() is None:
            proc.kill()
            proc.wait()
    # "respondeu" = o modelo decidiu (chamou skill ou terminou sem); timeout e erro do CLI ficam fora da taxa
    return {"skill": skill, "antes": ferramentas, "fim": fim, "segundos": round(time.time() - t0, 1),
            "respondeu": fim == "chamou skill" or fim.endswith("sem skill")}


def versao(raiz: Path, modelo: str | None) -> str:
    """O que a medida depende além do pedido: as descrições (todos os SKILL.md do projeto) e o modelo."""
    h = hashlib.sha1((modelo or "padrão").encode("utf-8"))
    for f in sorted((raiz / ".claude/skills").glob("*/SKILL.md")):
        h.update(f.relative_to(raiz).as_posix().encode("utf-8") + b"\0" + f.read_bytes())
    return h.hexdigest()[:8]


def chave(query: str, n: int, ver: str = "") -> str:
    return (f"{ver}-" if ver else "") + hashlib.sha1(query.encode("utf-8")).hexdigest()[:10] + f"-{n}"


def resumir(casos: list[dict], rodadas: dict[str, dict], skill: str, rodadas_por: int, ver: str = "") -> dict:
    linhas, ok, validos, sem_resposta = [], 0, 0, 0
    for c in casos:
        rs = [rodadas[chave(c["query"], n, ver)] for n in range(rodadas_por) if chave(c["query"], n, ver) in rodadas]
        validas = [r for r in rs if r["respondeu"]]
        sem_resposta += len(rs) - len(validas)
        disparou = sum(1 for r in validas if r["skill"] and r["skill"].split(":")[-1] == skill)
        taxa = disparou / len(validas) if validas else None
        passou = None if taxa is None else (taxa >= 0.5 if c["should_trigger"] else taxa < 0.5)
        if passou is not None:
            validos += 1
            ok += passou
        linhas.append({"query": c["query"], "should_trigger": c["should_trigger"], "esperada": c.get("esperada"),
                       "taxa": taxa, "rodadas": len(validas), "passou": passou,
                       "chamadas": [r["skill"] or "-" for r in validas]})
    deve = [l for l in linhas if l["should_trigger"] and l["passou"] is not None]
    nao = [l for l in linhas if not l["should_trigger"] and l["passou"] is not None]
    return {"skill": skill, "casos": linhas, "acertos": ok, "medidos": validos, "sem_resposta": sem_resposta,
            "deve_disparar": f"{sum(l['passou'] for l in deve)}/{len(deve)}",
            "nao_deve": f"{sum(l['passou'] for l in nao)}/{len(nao)}"}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--skill", required=True, help="o nome da skill medida, como no frontmatter")
    p.add_argument("--casos", required=True, help="JSON com a lista de {query, should_trigger, esperada}")
    p.add_argument("--saida", required=True, help="pasta das rodadas e do resumo (fora do projeto)")
    p.add_argument("--rodadas", type=int, default=3)
    p.add_argument("--modelo", default=None)
    p.add_argument("--paralelo", type=int, default=4)
    p.add_argument("--timeout", type=int, default=150, help="segundos por rodada")
    p.add_argument("--raiz", default=str(RAIZ), help="a raiz do projeto de onde sai a cópia (padrão: este repositório)")
    a = p.parse_args()
    casos = json.loads(Path(a.casos).read_text(encoding="utf-8"))
    if not isinstance(casos, list) or not all(isinstance(c, dict) and "query" in c and "should_trigger" in c
                                              for c in casos):
        sys.exit("--casos: uma lista de {query, should_trigger}")
    if len({c["query"] for c in casos}) != len(casos):
        sys.exit("--casos: há pedido repetido (a chave da rodada é o pedido)")
    raiz = Path(a.raiz).resolve()
    if not (raiz / ".claude/skills" / a.skill / "SKILL.md").is_file():
        sys.exit(f"skill {a.skill} não existe em {raiz / '.claude/skills'}")
    claude = shutil.which("claude")
    if not claude:
        sys.exit("o CLI `claude` não está no PATH")
    if Path(claude).suffix.lower() in (".cmd", ".bat"):
        # pelo cmd.exe, o pedido com & | " % ^ ou quebra de linha chega mudado, e o kill no timeout mata só o cmd.exe
        sys.exit(f"o `claude` do PATH é um atalho {Path(claude).suffix} ({claude}); aponte o executável de verdade")
    saida = Path(a.saida).resolve()
    if saida.is_relative_to(raiz):
        sys.exit("--saida dentro do projeto: use uma pasta fora dele (uma pasta temporária)")
    (saida / "rodadas").mkdir(parents=True, exist_ok=True)
    ver = versao(raiz, a.modelo)
    rodadas = {}
    for f in (saida / "rodadas").glob(f"{ver}-*.json"):
        r = json.loads(f.read_text(encoding="utf-8"))
        if r.get("respondeu"):  # a que não respondeu (timeout, erro do CLI) roda de novo
            rodadas[f.stem] = r
    faltam = [(c, n) for c in casos for n in range(a.rodadas) if chave(c["query"], n, ver) not in rodadas]
    total = len(casos) * a.rodadas
    print(f"[..] versão {ver} (descrições e modelo); {len(casos)} pedidos x {a.rodadas} rodadas = {total}; "
          f"já respondidas {total - len(faltam)}; "
          f"faltam {len(faltam)}")
    if faltam:
        with tempfile.TemporaryDirectory(prefix="disparo-") as tmp:
            projeto = Path(tmp)
            montar_projeto(raiz, projeto)
            feitas = total - len(faltam)
            with ThreadPoolExecutor(max_workers=a.paralelo) as ex:
                fut = {ex.submit(uma_rodada, c["query"], projeto, a.modelo, a.timeout, claude): (c, n)
                       for c, n in faltam}
                for f in as_completed(fut):
                    c, n = fut[f]
                    try:
                        r = f.result()
                    except Exception as e:  # noqa: BLE001 - a rodada que quebra fica registrada, sem derrubar as outras
                        r = {"skill": None, "antes": [], "fim": f"erro: {type(e).__name__}: {e}", "segundos": 0,
                             "respondeu": False}
                    r["query"], r["rodada"] = c["query"], n
                    k = chave(c["query"], n, ver)
                    (saida / "rodadas" / f"{k}.json").write_text(json.dumps(r, ensure_ascii=False, indent=1),
                                                                 encoding="utf-8")
                    rodadas[k] = r
                    feitas += 1
                    print(f"[{feitas}/{total}] {r['skill'] or '-':<22} {r['fim']:<22} {r['segundos']:>5}s  "
                          f"{c['query'][:60]}")
    res = resumir(casos, rodadas, a.skill, a.rodadas, ver)
    res["versao"] = ver
    (saida / "resumo.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n{a.skill}: {res['acertos']}/{res['medidos']} pedidos certos (deve disparar {res['deve_disparar']}, "
          f"não deve {res['nao_deve']}); rodadas sem resposta: {res['sem_resposta']}")
    for l in res["casos"]:
        if l["passou"] is False:
            print(f"  ERRO  {'deve' if l['should_trigger'] else 'não deve'}  taxa {l['taxa']:.2f}  "
                  f"{l['chamadas']}  {l['query'][:70]}")
    sys.exit(2 if res["sem_resposta"] else 0)


if __name__ == "__main__":
    main()
