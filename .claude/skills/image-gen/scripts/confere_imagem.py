"""As conferências por máquina de uma imagem gerada, antes de ela ir à pessoa (o roteamento da image-gen).

    python -X utf8 .claude/skills/image-gen/scripts/confere_imagem.py <imagem> [--proporcao 1:1] [--sem-texto] [--jev]

- proporção: a razão largura/altura da imagem contra a pedida (avisa acima de 2% de diferença);
- centro visual: a média ponderada do traço escuro contra o meio da imagem (avisa acima de 5%, como o so_traco.py);
- texto inventado (com --jev e --sem-texto), **opcional**: uma pergunta ao Jev (TypeSafe), "a imagem contém letras,
  palavras ou números legíveis?", pelo cliente do projeto em `scripts/jev/` da raiz (`cliente.py` e `imagens.py`).
  É sinal, não trava, até um caso de uso medir o acerto. Sem `TYPESAFE_API_KEY` ou sem o `scripts/jev/`, a conferência
  pula com um aviso de uma linha, e as outras medidas seguem. Quando o pedido tem texto (rótulos que devem aparecer),
  não se roda: o Jev diz se há texto, não se é o certo.
Saída: uma linha JSON com cada medida e os avisos. Código 0 sempre que a medida rodou; 2 sem a imagem.
"""
import argparse
import base64
import io
import json
import os
import sys
from pathlib import Path

import lib


def proporcao_pedida(s):
    s = s.split()[0]
    w, h = s.split(":")
    return float(w) / float(h)


def centro_visual(caminho):
    np = lib.importar("numpy")
    Image = lib.importar("PIL.Image")
    im = np.asarray(Image.open(caminho).convert("L"), dtype=float)
    peso = np.clip(255 - im - 40, 0, None)  # só o traço mais escuro que o papel
    if peso.sum() == 0:
        return None
    ys, xs = np.indices(peso.shape)
    cx, cy = (peso * xs).sum() / peso.sum(), (peso * ys).sum() / peso.sum()
    return cx / im.shape[1] - 0.5, cy / im.shape[0] - 0.5


def carregar_jev():
    """(cliente, imagens) do `scripts/jev/` da raiz do projeto, ou (None, motivo) quando a conferência não pode rodar."""
    pasta = lib.raiz_do_projeto() / "scripts" / "jev"
    if not ((pasta / "cliente.py").is_file() and (pasta / "imagens.py").is_file()):
        return None, f"sem o cliente do Jev em {pasta.as_posix()} (cliente.py e imagens.py)"
    sys.path.insert(0, str(pasta))
    try:
        import cliente
        import imagens
    except Exception as e:  # noqa: BLE001 - o cliente que não carrega vira aviso, não traceback
        return None, f"o cliente do Jev não carregou ({type(e).__name__}: {e})"
    if not cliente.tem_chave():
        return None, ("sem TYPESAFE_API_KEY (opcional; onde se pega: https://docs.typesafe.ai; como pôr: a linha no "
                      "`.env` da raiz, a partir do `.env.example`)")
    return (cliente, imagens), None


def jev_tem_texto(caminho, cliente, imagens):
    Image = lib.importar("PIL.Image")
    im = Image.open(io.BytesIO(imagens.ler_imagem(caminho))).convert("RGB")  # o pedido declara jpg: reencoda sempre
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=92)
    dados = base64.b64encode(buf.getvalue()).decode("ascii")
    corpo = {"model": imagens.MODELO, "state": {"imagem": "img"},
             "assets": {"img": {"type": "image", "format": "jpg", "data_base64": dados}},
             "questions": {"tem_texto": {"type": "noul",
                                         "instructions": "A `imagem` contém letras, palavras ou números legíveis?",
                                         "criteria": {"true": "Há ao menos uma palavra, letra ou número que se lê na imagem, escrito ou impresso, mesmo pequeno ou torto.",
                                                      "false": "Só desenho, formas, rabiscos e marcas sem letra nem número que se leia."}}}}
    resp, meta = cliente.chamar(corpo, {"TypeSafe-Danger-Zone-Images": "true"}, timeout=180, orcamento=300)
    return resp["answers"]["tem_texto"].get("noul"), meta.get("custo_usd")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("imagem")
    ap.add_argument("--proporcao", default=None)
    ap.add_argument("--sem-texto", action="store_true", help="o pedido não tem texto: qualquer texto na imagem é inventado")
    ap.add_argument("--jev", action="store_true", help="a conferência opcional de texto inventado pelo Jev")
    a = ap.parse_args(argv)
    if not os.path.isfile(a.imagem):
        print(json.dumps({"erro": f"imagem não encontrada: {a.imagem}"}, ensure_ascii=False))
        return 2
    Image = lib.importar("PIL.Image")
    try:
        w, h = Image.open(a.imagem).size
    except Exception as e:  # o arquivo que não é imagem: erro no JSON, código 2
        print(json.dumps({"erro": f"não é imagem legível: {a.imagem} ({type(e).__name__})"}, ensure_ascii=False))
        return 2
    out = {"imagem": a.imagem, "tamanho": [w, h], "avisos": []}
    if a.proporcao:
        alvo = proporcao_pedida(a.proporcao)
        dif = abs((w / h) / alvo - 1)
        out["proporcao"] = {"pedida": a.proporcao, "dif": round(dif, 4)}
        if dif > 0.02:
            out["avisos"].append(f"proporção {w}x{h} difere {dif:.1%} da pedida ({a.proporcao})")
    c = centro_visual(a.imagem)
    if c:
        out["centro"] = {"dx": round(c[0], 3), "dy": round(c[1], 3)}
        if max(abs(c[0]), abs(c[1])) > 0.05:
            out["avisos"].append(f"centro visual a {c[0]:+.1%} na largura e {c[1]:+.1%} na altura: centralizar por ele")
    if a.jev and a.sem_texto:
        jev, motivo = carregar_jev()
        if jev is None:
            # opcional: a conferência pula com um aviso de uma linha, e nunca conta como "sem texto"
            out["jev_tem_texto"] = None
            print(f"[image-gen] conferência de texto pelo Jev pulada: {motivo}.", file=sys.stderr)
        else:
            try:
                p, custo = jev_tem_texto(a.imagem, *jev)
                out["jev_tem_texto"] = p
                out["jev_custo_usd"] = custo
                if p is not None and p >= 0.7:
                    out["avisos"].append(f"texto na imagem (Jev {p:.2f}, em teste): o pedido não tinha texto")
            except (Exception, SystemExit) as e:  # sem rede ou erro da API: dizer, nunca contar como "sem texto"
                out["jev_tem_texto"] = None
                out["avisos"].append(f"a conferência de texto pelo Jev não rodou ({type(e).__name__}: {e})")
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
