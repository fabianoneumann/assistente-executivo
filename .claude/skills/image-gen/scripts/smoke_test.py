"""Smoke test da skill `image-gen`.

Valida o caminho **AI Studio + generate_content + imagem** (o padrão, com a conversão de formato pelo Pillow) gerando
1 imagem pequena (flash @ 1K) e confirmando que vieram bytes. Custo de alguns centavos (pede rede e chave).

Uso:
    python -X utf8 smoke_test.py               # provider aistudio (padrão, GEMINI_API_KEY)
    python -X utf8 smoke_test.py --vertex      # Vertex (VERTEX_API_KEY, pós-pago: só com o gasto combinado)
Saída: [OK]/[ERRO] + exit 0/1. Sem a chave, a mensagem de como configurar, sem traceback.
"""
import argparse
import os
import sys
import tempfile

import nano_banana as nb


class _Args:
    pass


def main() -> None:
    ap = argparse.ArgumentParser(description="Smoke test da skill image-gen.")
    ap.add_argument("--vertex", action="store_true", help="usar a Vertex (pós-pago) em vez do AI Studio")
    ap.add_argument("--aistudio", action="store_true", help="o padrão; mantido por compatibilidade")
    parsed = ap.parse_args()

    provider = "vertex" if parsed.vertex else "aistudio"
    out = os.path.join(tempfile.gettempdir(), "imagegen_smoke.png")

    args = _Args()
    args.prompt = "A simple flat minimalist blue circle centered on a plain white background"
    args.out = out
    args.mode = "explore"
    args.model = "flash"
    args.size = "1K"
    args.aspect = "1:1"
    args.refs = None
    args.provider = provider

    label = f"{provider} + generate_content + imagem (flash@1K)"
    try:
        res = nb.run(args)
        if res.get("error"):
            print(f"[ERRO] {label}: {res['error']}")
            sys.exit(1)
        ok = os.path.exists(out) and os.path.getsize(out) > 1000
        print(f"[{'OK' if ok else 'ERRO'}] {label}: {res.get('bytes')} bytes -> {out}")
        sys.exit(0 if ok else 1)
    except SystemExit:
        raise
    except Exception as e:
        print(f"[ERRO] {label}: {type(e).__name__}: {str(e)[:300]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
