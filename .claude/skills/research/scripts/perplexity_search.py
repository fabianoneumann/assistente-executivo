"""Pesquisa via Perplexity/Sonar (raso e profundo).

Raso e profundo compartilham a mesma chave e o mesmo endpoint (compatível com a
API da OpenAI); muda só o modelo. Por isso um script cobre os dois modos.

Uso:
    python perplexity_search.py --mode shallow --query "..."
    python perplexity_search.py --mode deep    --query "..."
"""
import argparse
import random
import sys
import time

import lib

BASE_URL = "https://api.perplexity.ai"
MODELS = {
    "shallow": "sonar-pro",           # tier de melhor valor p/ largura de fontes
    "deep": "sonar-deep-research",    # relatorio longo, centenas de fontes
}
# Deep research pode levar minutos; o raso responde em segundos. Teto generoso
# no deep evita timeout prematuro sem penalizar o raso (é só um limite).
TIMEOUTS = {"shallow": 60, "deep": 900}
# Levas disparadas em paralelo batem no limite de taxa (429; já deu 5 erros em 8 consultas simultâneas).
# Até 3 tentativas, com espera crescente entre elas (em segundos, com variação
# aleatória para os processos de uma leva não voltarem juntos, e o Retry-After do
# servidor quando vier maior); o erro só vai ao JSON depois da última. O cliente
# não faz tentativas próprias (max_retries=0): só este laço conta, e o tempo total
# fica dentro do orçamento, para o processo não morrer sem JSON no teto do Bash.
RATE_LIMIT_WAITS = [10, 30]
RETRY_BUDGET = {"shallow": 90, "deep": 300}  # segundos de espera somados, no máximo


def _retry_after(err) -> float:
    try:
        return float(err.response.headers.get("retry-after") or 0)
    except (AttributeError, TypeError, ValueError):
        return 0.0


def _is_quota(err) -> bool:
    # 429 de saldo ou cota esgotada não passa com espera: devolve na hora.
    texto = f"{getattr(err, 'code', '') or ''} {getattr(err, 'body', '') or ''}".lower()
    return "quota" in texto or "credit" in texto or "balance" in texto


def run(mode: str, query: str) -> dict:
    model = MODELS[mode]
    api_key = lib.get_key("PERPLEXITY_API_KEY")  # sem a chave, para aqui com a mensagem completa
    openai = lib.importar_sdk("openai")
    OpenAI, RateLimitError = openai.OpenAI, openai.RateLimitError
    client = OpenAI(
        api_key=api_key,
        base_url=BASE_URL,
        timeout=TIMEOUTS[mode],
        max_retries=0,
    )
    esperado = 0.0
    for wait in RATE_LIMIT_WAITS + [None]:
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": query}],
            )
            break
        except RateLimitError as err:
            if wait is None or _is_quota(err):
                raise
            pausa = max(wait, _retry_after(err)) * random.uniform(0.75, 1.25)
            if esperado + pausa > RETRY_BUDGET[mode]:
                raise
            esperado += pausa
            print(f"[research] Perplexity 429; nova tentativa em {pausa:.0f} s", file=sys.stderr)
            time.sleep(pausa)
    data = resp.model_dump()

    answer = ""
    try:
        answer = data["choices"][0]["message"]["content"] or ""
    except (KeyError, IndexError, TypeError):
        pass

    results = []
    for r in (data.get("search_results") or []):
        results.append({
            "title": r.get("title"),
            "url": r.get("url"),
            "snippet": r.get("snippet"),
            "published": r.get("date") or r.get("last_updated"),
            "source_type": r.get("source") or "web",
        })

    citations = data.get("citations") or [r["url"] for r in results if r.get("url")]
    return lib.make_result("perplexity", mode, model, query, answer, results, citations)


def main() -> None:
    ap = argparse.ArgumentParser(description="Pesquisa Perplexity/Sonar (raso ou profundo).")
    ap.add_argument("--mode", choices=["shallow", "deep"], default="shallow")
    ap.add_argument("--query", required=True)
    args = ap.parse_args()
    try:
        lib.emit(run(args.mode, args.query))
    except SystemExit:
        raise  # chave ausente: mensagem clara já foi emitida por get_key
    except Exception as e:  # falha de rede/API: devolve no contrato e sinaliza erro
        lib.emit(lib.make_result(
            "perplexity", args.mode, MODELS[args.mode], args.query,
            error=f"{type(e).__name__}: {e}",
        ))
        sys.exit(1)


if __name__ == "__main__":
    main()
