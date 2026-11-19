"""A quarta frente do raso: o Codex com a busca na web ligada, no contrato de saída dos outros scripts.

    python -X utf8 .claude/skills/research/scripts/codex_search.py --query "<pergunta>" [--limite 600] [--perfil <perfil>]

Opcional: pede o Codex CLI instalado e com login (`codex login`). Roda `codex --search exec` numa pasta isolada nova
(o Codex não vê o projeto), em modo só leitura, e pede cada achado com a URL exata ao lado e "sem fonte" no que não
achar fonte. Com `--perfil`, usa um perfil do `~/.codex/config.toml` (por exemplo, um sem os conectores da conta).
Imprime o JSON do contrato (`references/scripts.md`): `answer` é a resposta dele, `citations` são as URLs que ele
citou, `results` fica vazio (ele não devolve a lista crua de resultados). Gasta a franquia do plano do ChatGPT, não
crédito de API. Sem o Codex, o JSON sai com `error` dizendo como instalar, e a rodada segue com as outras frentes.
O que ele traz se confere na primária como o resto: no teste que o trouxe para a skill, achou o que as outras frentes
não acharam e marcou "sem fonte" o que não tinha primária, mas também errou uma atribuição.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

COMO_INSTALAR = ("o Codex CLI é opcional nesta skill; para ligar esta frente, instale por "
                 "https://developers.openai.com/codex/cli e rode `codex login`. Sem ele, a rodada segue com as "
                 "outras frentes e diz isso")


def rodar_com_prazo(cmd, entrada, cwd, prazo):
    """Roda o Codex e, no prazo estourado, mata a árvore inteira: no Windows o codex do npm é um .cmd que abre o node,
    e o subprocess.run mataria só o cmd.exe e esperaria o node para sempre. Devolve (código, stdout, stderr)."""
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                         encoding="utf-8", cwd=cwd)
    try:
        out, err = p.communicate(entrada, timeout=prazo)
        return p.returncode, out, err
    except subprocess.TimeoutExpired:
        if os.name == "nt":
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(p.pid)], capture_output=True)
        else:
            p.kill()
        try:
            p.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            pass
        raise


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--query", required=True)
    ap.add_argument("--limite", type=int, default=600)
    ap.add_argument("--perfil", default=None, help="perfil do ~/.codex/config.toml (opcional)")
    a = ap.parse_args(argv)
    out = {"contract_version": "1", "provider": "codex", "mode": "shallow", "model": "codex (web_search)",
           "query": a.query, "answer": None, "results": [], "citations": [], "error": None}
    bin_ = shutil.which("codex")
    if not bin_:
        out["error"] = COMO_INSTALAR
        print(json.dumps(out, ensure_ascii=False, indent=2))
        print(f"[research] {COMO_INSTALAR}.", file=sys.stderr)
        return 1
    pasta = tempfile.mkdtemp(prefix="codex-search-")
    pedido = (a.query + "\n\nSearch the web. Answer in the language of the question. List each finding as a bullet with "
              "the exact source URL next to it; mark as \"sem fonte\" anything you cannot source. Do not edit files.\n")
    cmd = [bin_, "--search", "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only"]
    if a.perfil:
        cmd += ["-p", a.perfil]
    cmd += ["-o", f"{pasta}/resposta.md", "-"]
    try:
        codigo, sout, serr = rodar_com_prazo(cmd, pedido, pasta, a.limite)
        try:
            texto = open(f"{pasta}/resposta.md", encoding="utf-8").read().strip()
        except OSError:
            texto = ""
        if not texto:
            out["error"] = ("o Codex não devolveu resposta (confira o `codex login`): "
                            + ((serr or "") + (sout or ""))[-500:].strip())
        else:
            out["answer"] = texto
            urls = [u.rstrip(".,;:") for u in re.findall(r"https?://[^\s)\]>\"']+", texto)]
            out["citations"] = list(dict.fromkeys(urls))
            if codigo != 0:  # resposta parcial: vai, mas avisada
                out["error"] = f"o Codex saiu com o código {codigo}; a resposta pode estar incompleta"
    except (OSError, subprocess.TimeoutExpired) as e:
        out["error"] = f"o Codex não rodou ({type(e).__name__}: {e})"
    finally:
        shutil.rmtree(pasta, ignore_errors=True)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if not out["error"] else 1


if __name__ == "__main__":
    sys.exit(main())
