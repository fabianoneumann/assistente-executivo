"""Gera uma imagem pelo Codex CLI (o gerador integrado, `image_gen`, que usa o gpt-image-2), no plano do ChatGPT.

    python -X utf8 .claude/skills/image-gen/scripts/codex_imagem.py --prompt "..." --out img.png         [--refs a.png b.png] [--papel-refs "estilo" "identidade"] [--proporcao "1:1 square"] [--fundo-transparente]

Opcional: pede o Codex CLI instalado e logado num plano pago do ChatGPT (no gratuito a ferramenta de imagem não existe).
O gerador integrado não cobra por imagem (gasta a franquia do plano) e não deixa escolher o modelo. Como roda:
- numa pasta isolada nova (tempfile), com só as referências copiadas: o Codex não vê o projeto;
- pelo perfil `claude-imagem` (`$CODEX_HOME/claude-imagem.config.toml`, por padrão `~/.codex/`: escrita só na pasta de
  onde roda, sem aprovação, sem os conectores da conta, com a geração de imagem ligada). O perfil se cria uma vez; sem
  ele, o script para com o passo de criar (o conteúdo está em PERFIL, abaixo, e no README da skill);
- com o prompt no formato rotulado da skill oficial `imagegen` do Codex e cada referência dita pelo papel ("Imagem 1:
  referência de estilo"), sem supor que toda imagem dada é para editar.
Grava a imagem em --out e, ao lado, um .json com a linhagem: gerador, versão do Codex CLI, modelo, data, tempo, prompt e
referências (o roteamento da image-gen, `references/roteamento.md`, pede a linhagem em toda imagem).
"""
import argparse
import datetime
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

MODELO = "gpt-image-2"  # o do gerador integrado do Codex, pela página de geração de imagem do Codex

# o perfil do Codex para gerar imagem: escrita só na pasta de onde roda, sem aprovação e sem os conectores da conta
PERFIL = """# Perfil para o Claude Code gerar imagem pelo Codex (skill image-gen): escrita só na pasta de onde roda (uma pasta
# isolada temporária), sem aprovação, sem os conectores da conta do ChatGPT, com a geração de imagem integrada.
sandbox_mode = "workspace-write"
approval_policy = "never"

[features]
apps = false
image_generation = true
"""


def arquivo_do_perfil(nome):
    return Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / f"{nome}.config.toml"


def sem_perfil(nome):
    """A mensagem de como criar o perfil, uma vez, quando ele não existe."""
    arq = arquivo_do_perfil(nome)
    return (f"[image-gen] o perfil `{nome}` do Codex não existe ({arq}). O gerador pelo Codex é opcional; para usá-lo, "
            f"crie o arquivo uma vez com o conteúdo abaixo (ou rode de novo com --criar-perfil) e repita o pedido:\n\n{PERFIL}")


def codex_bin():
    """O executável do Codex: no Windows, o npm instala um atalho codex.cmd, que o subprocess só acha pelo caminho completo."""
    return shutil.which("codex") or "codex"


def versao_codex():
    try:
        r = subprocess.run([codex_bin(), "--version"], capture_output=True, text=True, timeout=30)
        return (r.stdout or r.stderr).strip()
    except Exception as e:  # sem o Codex instalado, a geração falha adiante com a mensagem dele
        return f"desconhecida ({type(e).__name__})"


def pedido(prompt, refs, papeis, proporcao, transparente, nome_saida):
    linhas = ["Generate exactly one image with your built-in image generation tool (image_gen). Do not use any app, "
              "connector or MCP tool, and run no other commands except copying the final image."]
    if refs:
        linhas.append("Input images (references only, never edit targets; copy what the role says, never their objects "
                      "or composition unless the role says so):")
        for i, (r, papel) in enumerate(zip(refs, papeis), 1):
            linhas.append(f"- Image {i} ({Path(r).name}): {papel}.")
    linhas.append(f"Aspect ratio / framing: {proporcao}.")
    if transparente:
        linhas.append("Background: genuinely transparent, preserve the alpha channel.")
    linhas.append("")
    linhas.append("Image prompt:")
    linhas.append(prompt)
    linhas.append("")
    linhas.append(f"After generating, copy the generated image into the current working directory as {nome_saida}. "
                  "Reply only with the absolute path of that copy.")
    return "\n".join(linhas)


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
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--refs", nargs="*", default=[])
    ap.add_argument("--papel-refs", nargs="*", default=[], help="o papel de cada referência, na mesma ordem")
    ap.add_argument("--proporcao", default="1:1 square")
    ap.add_argument("--fundo-transparente", action="store_true")
    ap.add_argument("--perfil", default="claude-imagem")
    ap.add_argument("--limite", type=int, default=600, help="segundos")
    ap.add_argument("--criar-perfil", action="store_true", help="cria o perfil do Codex, se não existir, e segue")
    a = ap.parse_args(argv)
    if not shutil.which("codex"):
        print(json.dumps({"skill": "image-gen", "gerador": "codex", "out": a.out,
                          "error": "o Codex CLI não está instalado (opcional). Como instalar: "
                                   "https://developers.openai.com/codex/cli, depois `codex login` com um plano pago do "
                                   "ChatGPT. Sem ele, gere pelo nano_banana.py."}, ensure_ascii=False))
        return 1
    perfil = arquivo_do_perfil(a.perfil)
    if not perfil.is_file():
        if not a.criar_perfil:
            print(sem_perfil(a.perfil), file=sys.stderr)
            print(json.dumps({"skill": "image-gen", "gerador": "codex", "out": a.out,
                              "error": f"perfil do Codex ausente: {perfil.name}"}, ensure_ascii=False))
            return 1
        perfil.parent.mkdir(parents=True, exist_ok=True)
        perfil.write_text(PERFIL, encoding="utf-8", newline="\n")
        print(f"[image-gen] perfil do Codex criado: {perfil}", file=sys.stderr)
    papeis = a.papel_refs + ["style reference: copy the drawing technique and line quality"] * (len(a.refs) - len(a.papel_refs))

    pasta = Path(tempfile.mkdtemp(prefix="codex-imagem-"))
    nomes = [f"ref{i}-{Path(r).name}" for i, r in enumerate(a.refs, 1)]  # o índice evita que duas refs de mesmo nome se sobrescrevam
    for r, n in zip(a.refs, nomes):
        shutil.copy2(r, pasta / n)
    nome = "saida" + (Path(a.out).suffix or ".png")
    texto = pedido(a.prompt, nomes, papeis, a.proporcao, a.fundo_transparente, nome)
    cmd = [codex_bin(), "exec", "--skip-git-repo-check", "--ephemeral", "-p", a.perfil, "-C", str(pasta)]
    for n in nomes:
        cmd += ["-i", n]
    cmd += ["-"]
    t0 = time.time()
    try:
        codigo, sout, serr = rodar_com_prazo(cmd, texto, pasta, a.limite)
    except (OSError, subprocess.TimeoutExpired) as e:  # o CLI que não existe ou o prazo estourado: erro no JSON, não traceback
        shutil.rmtree(pasta, ignore_errors=True)
        print(json.dumps({"skill": "image-gen", "gerador": "codex", "out": a.out,
                          "error": f"o Codex não rodou ({type(e).__name__}: {e})"}, ensure_ascii=False))
        return 1
    seg = round(time.time() - t0, 1)
    gerada = pasta / nome
    meta = {"skill": "image-gen", "gerador": "codex", "versao": versao_codex(), "modelo": MODELO,
            "data": datetime.datetime.now().isoformat(timespec="seconds"), "segundos": seg, "custo_usd": None,
            "custo": "franquia do plano do ChatGPT (sem custo por imagem)", "prompt": a.prompt,
            "refs": [str(x) for x in a.refs], "papel_refs": papeis[:len(a.refs)], "out": a.out, "error": None}
    if not gerada.is_file():
        cauda = (sout or "")[-600:] + (serr or "")[-400:]
        meta["error"] = ("o Codex não devolveu a imagem (no plano gratuito a ferramenta não existe; confira o login e o "
                         f"/status; se o erro for o limite de tamanho do comando no Windows, repita uma vez): {cauda.strip()}")
        shutil.rmtree(pasta, ignore_errors=True)
        print(json.dumps(meta, ensure_ascii=False))
        return 1
    os.makedirs(Path(a.out).resolve().parent, exist_ok=True)
    shutil.copy2(gerada, a.out)
    with open(Path(a.out).with_suffix(".json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    shutil.rmtree(pasta, ignore_errors=True)
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
