"""Smoke test das APIs de pesquisa.

Valida chave + endpoint + faturamento de cada fornecedor com um ping mínimo e
barato. O padrão NÃO dispara deep research (lento e caro).

Uso:
    python -X utf8 .claude/skills/research/scripts/smoke_test.py           # 2 pings rasos (Perplexity + Gemini pelo AI Studio, o padrão da rasa)
    python -X utf8 .claude/skills/research/scripts/smoke_test.py --vertex  # o ping do Gemini raso pela Vertex (pós-pago), em vez do AI Studio
    python -X utf8 .claude/skills/research/scripts/smoke_test.py --deep    # + probe de acesso pago do Gemini Deep Research
                                   #   (cria e cancela um job na hora; não roda a pesquisa)
Saída: [OK] / [FALTA] / [ERRO] por checagem; exit 0 se tudo passa, 1 caso contrário.
Sem a chave, a checagem diz a variável, onde se pega e como se põe, sem chamar a rede.
"""
import argparse
import sys

import lib


def check_perplexity() -> None:
    key = lib.get_key("PERPLEXITY_API_KEY")
    openai = lib.importar_sdk("openai")
    client = openai.OpenAI(api_key=key, base_url="https://api.perplexity.ai", timeout=60)
    resp = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Responda apenas: OK"}],
        max_tokens=16,   # Perplexity exige min. 16
    )
    if not resp.choices:
        raise RuntimeError("resposta sem choices")


def check_gemini(vertex: bool = False) -> None:
    # Espelha a rasa real: AI Studio por padrão; Vertex só com --vertex.
    key = lib.get_key("VERTEX_API_KEY" if vertex else "GEMINI_API_KEY")
    genai = lib.importar_sdk("google.genai")
    types = lib.importar_sdk("google.genai.types")
    client = genai.Client(vertexai=True, api_key=key) if vertex else genai.Client(api_key=key)
    resp = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Responda apenas: OK",
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())],
        ),
    )
    if not (resp.text or "").strip():
        raise RuntimeError("resposta vazia")


def check_gemini_deep_access() -> None:
    """Probe do tier pago do Deep Research: cria um job e o cancela na hora.
    Valida auth + acesso pago sem rodar a pesquisa completa (que é longa/cara).
    Necessário porque o Flash tem free tier e mascararia um billing ausente."""
    key = lib.get_key("GEMINI_API_KEY")
    genai = lib.importar_sdk("google.genai")
    client = genai.Client(api_key=key)
    it = client.interactions.create(
        agent="deep-research-preview-04-2026", input="ping", background=True,
    )
    try:
        client.interactions.cancel(it.id)   # aborta antes de gastar com a pesquisa
    except Exception:
        pass
    if not getattr(it, "id", None):
        raise RuntimeError("create nao retornou id")


def main() -> None:
    ap = argparse.ArgumentParser(description="Smoke test das APIs de pesquisa.")
    ap.add_argument("--deep", action="store_true",
                    help="tambem faz o probe de acesso pago do Gemini Deep Research")
    ap.add_argument("--vertex", action="store_true",
                    help="testa o Gemini raso pela Vertex (pós-pago) em vez do AI Studio")
    args = ap.parse_args()

    ok = True
    checks = [
        ("Perplexity (sonar-pro)", check_perplexity),
        (f"Gemini raso {'Vertex' if args.vertex else 'AI Studio'} (gemini-3.5-flash + grounding)",
         lambda: check_gemini(args.vertex)),
    ]
    if args.deep:
        checks.append(("Gemini Deep Research (acesso pago)", check_gemini_deep_access))
    for name, fn in checks:
        try:
            fn()
            print(f"[OK]   {name}")
        except SystemExit as e:            # chave ausente/placeholder ou SDK faltando: a mensagem completa
            print(f"[FALTA] {name}:\n{e}\n")
            ok = False
        except Exception as e:             # rede/API/billing
            print(f"[ERRO] {name}: {type(e).__name__}: {str(e)[:200]}")
            ok = False
    print("\nResultado:", "tudo certo" if ok else "há falhas")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
