"""Geração de imagem via Nano Banana (Gemini image) por `generate_content`.

Endpoint padrão: AI Studio (`GEMINI_API_KEY`, crédito pré-pago), que não aceita `output_mime_type`; o formato do
`--out` sai por conversão com o Pillow. A Vertex (`VERTEX_API_KEY`, modo expresso, pós-pago no projeto do Google
Cloud) fica por `--provider vertex`: pós-pago não tem teto natural, então só com a estimativa de gasto antes (a regra
de custo em `references/projeto.md`). Uma API só (`generate_content`) que roda nos dois providers.

Nota de arquitetura: a Interactions API (mais nova) foi testada e só existia no AI Studio (404 no Vertex); por isso
`generate_content`. Quando ela chegar ao Vertex, dá para refatorar só `_generate_with_retry`.

Modos (presets de model+size+aspect; sobrescreva com --model/--size/--aspect):
    explore  -> flash (NB2) @ 1K, 4:5   (exploração barata/descartável)
    final    -> pro          @ 2K, 4:5   (entregável, o padrão)
    map      -> pro          @ 4K, 3:2   (mestra ampla p/ mapa cortado + zooms no HTML)

Uso:
    python nano_banana.py --prompt "..." --out img.png [--mode final] [--refs a.png b.png]

Sem a chave do provider escolhido, sai com a mensagem de como configurar (a variável, onde se pega, como se põe),
antes de importar o SDK e sem traceback.
"""
import argparse
import base64
import os
import random
import sys
import time

import lib

# IDs de modelo (gemini-3-pro-image confirmado no Vertex; flash confirmado no smoke)
MODELS = {"pro": "gemini-3-pro-image", "flash": "gemini-3.1-flash-image"}
# Preço por milhão de tokens, da página oficial (ai.google.dev/gemini-api/docs/pricing, tarifa padrão, não a de lote):
# a saída de imagem do pro a US$ 120 e a do flash a US$ 60; a entrada do flash a US$ 0,50 e a do pro a cerca de US$ 2.
# O custo de cada geração sai dos tokens que a resposta devolve (usage_metadata), não da tabela de modos: há imagens
# que gastam mais tokens que os 1120 da documentação. Confira a página antes de confiar no número: a tarifa muda.
PRECO = {"gemini-3-pro-image": {"entrada": 2.0, "saida": 120.0},
         "gemini-3.1-flash-image": {"entrada": 0.5, "saida": 60.0}}
CHAVE_DO_PROVIDER = {"aistudio": "GEMINI_API_KEY", "vertex": "VERTEX_API_KEY"}


def custo(resp, model_id):
    """(uso, custo em US$) pelos tokens da resposta; (None, None) se a resposta não trouxer o uso."""
    u = getattr(resp, "usage_metadata", None)
    if u is None:
        return None, None
    ent = getattr(u, "prompt_token_count", 0) or 0
    sai = (getattr(u, "candidates_token_count", 0) or 0) + (getattr(u, "thoughts_token_count", 0) or 0)
    pr = PRECO.get(model_id)
    uso = {"entrada": ent, "saida": sai, "total": getattr(u, "total_token_count", None)}
    return uso, (round(ent * pr["entrada"] / 1e6 + sai * pr["saida"] / 1e6, 4) if pr else None)


# preset por modo: (model_key, size, aspect)
MODES = {
    "explore": ("flash", "1K", "4:5"),
    "final":   ("pro",   "2K", "4:5"),
    "map":     ("pro",   "4K", "3:2"),   # 3:2 = mais próximo de 8:5; template corta ~6% de altura ao 8:5
}

# o SDK aceita image_size '512','1K','2K','4K'
SIZE_ALIAS = {"0.5K": "512", "512": "512", "1K": "1K", "2K": "2K", "4K": "4K"}

RETRIES = 5   # 503/UNAVAILABLE do modelo é transitório (sobrecarga)


def _client(provider: str, chave: str):
    genai = lib.importar("google.genai")
    if provider == "aistudio":
        return genai.Client(api_key=chave)
    return genai.Client(vertexai=True, api_key=chave)


def _guess_mime(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    return {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".webp": "image/webp"}.get(ext, "image/png")


def _out_mime(path: str) -> str:
    """MIME de saída pela extensão do --out (default PNG, melhor p/ texto/linha)."""
    ext = os.path.splitext(path)[1].lower()
    return "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"


def _extract_image_bytes(resp) -> bytes | None:
    for cand in (getattr(resp, "candidates", None) or []):
        content = getattr(cand, "content", None)
        for part in (getattr(content, "parts", None) or []):
            inline = getattr(part, "inline_data", None)
            data = getattr(inline, "data", None) if inline else None
            if data:
                return bytes(data) if isinstance(data, (bytes, bytearray)) else base64.b64decode(data)
    return None


def _generate_with_retry(client, types, model_id, contents, aspect, size, out_mime):
    """generate_content de imagem, com retry em erros transitórios (503/overloaded)."""
    # O AI Studio (Developer API) recusa output_mime_type ("only supported in ... Agent Platform mode"); lá o formato
    # sai do modelo e o run() converte para o do --out.
    img_cfg = {"aspect_ratio": aspect, "image_size": size}
    if out_mime:
        img_cfg["output_mime_type"] = out_mime
    cfg = types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(**img_cfg),
    )
    last = None
    for attempt in range(RETRIES):
        try:
            return client.models.generate_content(model=model_id, contents=contents, config=cfg)
        except Exception as e:
            transient = any(s in str(e) for s in ("503", "UNAVAILABLE", "overloaded", "429"))
            if transient and attempt < RETRIES - 1:
                last = e
                time.sleep(min(2 ** attempt, 20) + random.uniform(0, 1))
                continue
            raise
    raise last


def run(args) -> dict:
    # a chave antes de tudo: sem ela, a mensagem de como configurar, antes de importar o SDK
    chave = lib.get_key(CHAVE_DO_PROVIDER[args.provider])
    if args.provider == "vertex":
        print("[image-gen] a Vertex é pós-pago: a geração entra na fatura do projeto do Google Cloud. Estime o gasto "
              "antes (o custo por imagem está no SKILL.md) e pare perto do valor combinado.", file=sys.stderr)
    dmodel, dsize, daspect = MODES.get(args.mode or "final", MODES["final"])
    model_key = args.model or dmodel
    size = SIZE_ALIAS.get(args.size or dsize, args.size or dsize)
    aspect = args.aspect or daspect
    model_id = MODELS[model_key]
    out_mime = _out_mime(args.out)

    client = _client(args.provider, chave)
    types = lib.importar("google.genai.types")
    contents = [args.prompt]
    for ref in (args.refs or []):
        with open(ref, "rb") as f:
            contents.append(types.Part.from_bytes(data=f.read(), mime_type=_guess_mime(ref)))

    pede_mime = out_mime if args.provider == "vertex" else None
    resp = _generate_with_retry(client, types, model_id, contents, aspect, size, pede_mime)
    img = _extract_image_bytes(resp)
    if not img:
        return {"skill": "image-gen", "out": args.out,
                "error": "resposta sem bytes de imagem (checar modelo/modalidade)"}
    if pede_mime is None:
        # AI Studio: converte para o formato pedido no --out quando o modelo devolveu outro.
        from io import BytesIO
        Image = lib.importar("PIL.Image")
        im = Image.open(BytesIO(img))
        fmt = "JPEG" if out_mime == "image/jpeg" else "PNG"
        if (im.format or "").upper() != fmt:
            buf = BytesIO()
            (im.convert("RGB") if fmt == "JPEG" else im).save(buf, format=fmt, **({"quality": 95} if fmt == "JPEG" else {}))
            img = buf.getvalue()

    os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
    with open(args.out, "wb") as f:
        f.write(img)

    uso, custo_usd = custo(resp, model_id)
    return {
        "skill": "image-gen", "gerador": "nano-banana", "provider": args.provider, "model": model_id,
        "uso": uso, "custo_usd": custo_usd,
        "mode": args.mode, "size": size, "aspect": aspect, "output_mime": out_mime,
        "prompt": args.prompt, "out": args.out, "refs": args.refs or [],
        "bytes": len(img), "error": None,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Gera imagem via Nano Banana (generate_content).")
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True, help="caminho de saída (.png default; .jpg p/ JPEG)")
    ap.add_argument("--mode", choices=["explore", "final", "map"])
    ap.add_argument("--model", choices=["flash", "pro"])
    ap.add_argument("--size", choices=["0.5K", "512", "1K", "2K", "4K"])
    ap.add_argument("--aspect", help="1:1, 3:2, 4:3, 4:5, 16:9, 21:9… (default do modo)")
    ap.add_argument("--refs", nargs="*", help="0–14 imagens de referência (consistência)")
    ap.add_argument("--provider", choices=["vertex", "aistudio"], default="aistudio")
    args = ap.parse_args()

    try:
        lib.emit(run(args))
    except SystemExit:
        raise
    except Exception as e:
        lib.emit({"skill": "image-gen", "out": args.out, "error": f"{type(e).__name__}: {e}"})
        sys.exit(1)


if __name__ == "__main__":
    main()
