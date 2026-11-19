"""Monta o índice do banco de imagens geradas a partir dos `prompts.md` das peças.

    python -X utf8 .claude/skills/image-gen/scripts/indexa_banco.py [--saida marketing/social-media/banco-de-imagens.md]

Cada `prompts.md` (a regra da image-gen: o prompt exato de cada geração, na pasta da peça) tem uma seção por imagem,
com o título "## <arquivo> (<onde>)" ou "### <nome>". O índice tira de cada seção: a peça, o arquivo, o que ela mostra
(o começo do prompt), o traço (lápis, caneta ou outro, pelas palavras do prompt), o gerador e o modo, se foi usada
(a linha "Usado:" ou "Virou:") e o link do original no bucket, quando há. A licença é sempre a do projeto: são imagens
geradas para as peças, sem obra de terceiro. O índice é gerado: não se edita à mão; roda de novo depois de uma peça nova.
Lê só os `prompts.md` versionados (`git ls-files`) dentro de `marketing/`; sem nenhum, grava o banco vazio, com o cabeçalho.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

import lib

ROOT = lib.raiz_do_projeto()


def tracos(prompt):
    p = prompt.lower()
    if "pencil" in p or "graphite" in p or "lápis" in p:
        return "lápis"
    if re.search(r"\b(ink|pen|caneta)\b", p):
        return "caneta"
    return "outro"


def campo(bloco, *rotulos):
    for r in rotulos:
        m = re.search(r"\*\*" + r + r"[^*]*:\*\*\s*(.+)", bloco)
        if m:
            return m.group(1).strip()
    return ""


def secoes(texto):
    partes = re.split(r"^(#{2,3} .+)$", texto, flags=re.M)
    for i in range(1, len(partes) - 1, 2):
        yield partes[i].lstrip("#").strip(), partes[i + 1]


def entradas(arq):
    peca = arq.parent.relative_to(ROOT).as_posix()
    texto = arq.read_text(encoding="utf-8")
    for titulo, bloco in secoes(texto):
        prompt = ""
        m = re.search(r"^> (.+)$", bloco, re.M) or re.search(r"```text\n(.+?)\n```", bloco, re.S)
        if m:
            prompt = m.group(1).strip()
        if not prompt:
            continue
        arquivo = titulo.split(" (")[0].strip("` ")
        gerado = campo(bloco, "Arquivo gerado", "Chamada")
        modo = re.search(r"modo `?(\w+)`?|--mode (\w+)", gerado + " " + bloco)
        virou = campo(bloco, "Virou") or (re.search(r"Usado: ([^.;]+)", gerado).group(1) if re.search(r"Usado: ([^.;]+)", gerado) else "")
        url = re.search(r"https://[^\s)]+\.(?:png|jpe?g|webp|mp4)\b", bloco)  # o link do original no bucket público
        texto_ger = gerado + " " + bloco[:600]
        ger = "codex" if re.search(r"codex", texto_ger, re.I) else ("nano-banana" if (modo or re.search(r"AI Studio|Vertex|flash|pro,|nano", texto_ger, re.I)) else "")
        data = re.search(r"20\d\d-\d\d-\d\d", gerado)
        virou = re.split(r"[.;(`]|\*\*", virou)[0].strip()
        yield {"peca": peca, "arquivo": arquivo, "mostra": re.sub(r"\s+", " ", prompt)[:140], "traco": tracos(prompt),
               "modo": (modo.group(1) or modo.group(2)) if modo else "", "usada": virou[:80],
               "gerador": ger + (f", {data.group(0)}" if data else ""), "url": url.group(0) if url else ""}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--saida", default="marketing/social-media/banco-de-imagens.md")
    a = ap.parse_args(argv)
    r = subprocess.run(["git", "-C", str(ROOT), "ls-files", "*prompts.md"], capture_output=True, text=True)
    arquivos = [ROOT / f for f in r.stdout.splitlines() if f.startswith("marketing/") and f.endswith("/prompts.md")]
    linhas = []
    for arq in sorted(arquivos):
        linhas.extend(entradas(arq))
    cab = ["# O banco de imagens geradas", "",
           "Gerado pelo `.claude/skills/image-gen/scripts/indexa_banco.py` a partir dos `prompts.md` das peças; não se edita à mão (rode o script de novo depois de uma peça nova). Antes de gerar, procure aqui pelo que a imagem precisa mostrar e pelo traço: o critério de reaproveitar está no `SKILL.md` da `image-gen`. Todas são do projeto (geradas para as peças); os originais ficam no bucket `conteudo`, em `assets/gerados/<peça>/`.", "",
           f"{len(linhas)} imagens em {len(arquivos)} peças.", "",
           "| Peça | Arquivo | O que mostra (o começo do prompt) | Traço | Gerador | Modo | Usada | Original |",
           "|---|---|---|---|---|---|---|---|"]
    for e in linhas:
        cel = lambda s: s.replace("|", "/")
        orig = f"[bucket]({e['url']})" if e["url"] else ""
        cab.append(f"| `{e['peca'].replace('marketing/social-media/', '')}` | `{cel(e['arquivo'])}` | {cel(e['mostra'])} | {e['traco']} | {e['gerador']} | {e['modo']} | {cel(e['usada'])} | {orig} |")
    saida = ROOT / a.saida
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text("\n".join(cab) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(linhas)} imagens de {len(arquivos)} prompts.md -> {a.saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
