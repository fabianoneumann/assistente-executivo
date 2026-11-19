"""Pesquisa via Gemini: raso (Flash + grounding) e profundo (Deep Research).

- Raso: `generate_content` com Google Search grounding. Padrão: **AI Studio**
  (`GEMINI_API_KEY`, crédito pré-pago, que se limita pelo saldo); a Vertex
  (`VERTEX_API_KEY`, pós-pago no projeto do Google Cloud; pool próprio, menos 503)
  fica por `--provider vertex`, e o pós-pago só roda com a estimativa de gasto
  antes (`references/projeto.md`). O free tier do Gemini não serve aqui: a busca
  (grounding) tem cota zero nele (responde 429).
- Profundo: agente Deep Research via `interactions` (assíncrono; cria job em
  background e faz polling até `completed`). Continua no **AI Studio**
  (`GEMINI_API_KEY`), onde o agente é oferecido. Escolhido o modelo padrão, não o
  `-max` (custo/ganho marginal).

Uso:
    python gemini_search.py --mode shallow --query "..."            # AI Studio
    python gemini_search.py --mode shallow --provider vertex --query "..."
    python gemini_search.py --mode deep    --query "..."
"""
import argparse
import random
import sys
import time

import lib

genai = types = None  # o SDK se importa depois de conferir a chave (lib.importar_sdk)

SHALLOW_MODEL = "gemini-3.5-flash"          # estavel, melhor valor
DEEP_AGENT = "deep-research-preview-04-2026"  # agente Deep Research (nao o -max)
RETRIES = 5                                  # 503/UNAVAILABLE do grounding e transitorio (sobrecarga do modelo)
POLL_INTERVAL = 15                           # s entre checagens do job profundo
DEEP_TIMEOUT = 2400                          # teto de 40 min para o job profundo
TERMINAL_FAIL = {"failed", "cancelled", "incomplete", "budget_exceeded"}


# ---------- raso ----------

def _generate_with_retry(client, query):
    """Chama o modelo com retry em erros transitorios (503/UNAVAILABLE/overloaded),
    comuns no grounding sob demanda. Backoff simples."""
    last = None
    for attempt in range(RETRIES):
        try:
            return client.models.generate_content(
                model=SHALLOW_MODEL,
                contents=query,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(google_search=types.GoogleSearch())],
                ),
            )
        except Exception as e:
            transient = any(s in str(e) for s in ("503", "UNAVAILABLE", "overloaded", "429"))
            if transient and attempt < RETRIES - 1:
                last = e
                # backoff exponencial com jitter: 1-2s, 2-3s, 4-5s, 8-9s (teto ~20s)
                time.sleep(min(2 ** attempt, 20) + random.uniform(0, 1))
                continue
            raise
    raise last


def _sdk():
    global genai, types
    if genai is None:
        genai = lib.importar_sdk("google.genai")
        types = lib.importar_sdk("google.genai.types")


def run_shallow(query: str, provider: str = "aistudio") -> dict:
    # AI Studio (padrão): crédito pré-pago. Vertex (opção): endpoint separado, pool
    # de capacidade próprio, menos 503, fatura no projeto GCP; chave Express bound a
    # service account (project/location inferidos da chave).
    if provider == "vertex":
        key = lib.get_key("VERTEX_API_KEY")
        _sdk()
        client = genai.Client(vertexai=True, api_key=key)
    else:
        key = lib.get_key("GEMINI_API_KEY")
        _sdk()
        client = genai.Client(api_key=key)
    resp = _generate_with_retry(client, query)
    answer = resp.text or ""

    results, citations = [], []
    try:
        gm = resp.candidates[0].grounding_metadata
        for chunk in (getattr(gm, "grounding_chunks", None) or []):
            web = getattr(chunk, "web", None)
            uri = getattr(web, "uri", None) if web else None
            if uri:
                # URLs de redirect (vertexaisearch...); URL canonica resolvida na curadoria.
                results.append({
                    "title": getattr(web, "title", None), "url": uri,
                    "snippet": None, "published": None, "source_type": "web",
                })
                citations.append(uri)
    except (AttributeError, IndexError):
        pass

    out = lib.make_result("gemini", "shallow", SHALLOW_MODEL, query, answer, results, citations)
    out["endpoint"] = provider  # aistudio (crédito) ou vertex (pós-pago)
    return out


# ---------- profundo ----------

def _extract_sources(interaction):
    """Percorre os steps do Deep Research e coleta citações (url_citation).
    Defensivo: a estrutura do preview pode variar.

    Observado: as anotações trazem `url` (redirect vertexaisearch) mas
    o `title` costuma vir vazio — o valor está no `output_text`, que referencia as
    fontes por marcador [cite: N] na ordem desta lista. Títulos/URLs canônicas se
    resolvem na curadoria."""
    results, citations, seen = [], [], set()
    for step in (getattr(interaction, "steps", None) or []):
        for block in (getattr(step, "content", None) or []):
            for ann in (getattr(block, "annotations", None) or []):
                url = getattr(ann, "url", None)
                if url and url not in seen:
                    seen.add(url)
                    results.append({
                        "title": getattr(ann, "title", None), "url": url,
                        "snippet": None, "published": None, "source_type": "web",
                    })
                    citations.append(url)
    return results, citations


def run_deep(query: str) -> dict:
    key = lib.get_key("GEMINI_API_KEY")
    _sdk()
    client = genai.Client(api_key=key)
    interaction = client.interactions.create(
        agent=DEEP_AGENT, input=query, background=True,
    )
    iid = interaction.id
    print(f"interaction_id: {iid}", file=sys.stderr)  # sai antes do fim, para recuperar se algo falhar depois
    deadline = time.time() + DEEP_TIMEOUT

    while True:
        result = client.interactions.get(iid)
        status = str(result.status)
        if status == "completed":
            break
        if status in TERMINAL_FAIL:
            return lib.make_result("gemini", "deep", DEEP_AGENT, query,
                                   error=f"job terminou em status '{status}'")
        if status == "requires_action":
            # Deep Research pediu interacao (ex.: esclarecimento). Um script nao
            # resolve isso; cancela e sinaliza para tratar manualmente.
            try:
                client.interactions.cancel(iid)
            except Exception:
                pass
            return lib.make_result("gemini", "deep", DEEP_AGENT, query,
                                   error="job em 'requires_action' — precisa de interacao; refaca a query mais especifica")
        if time.time() > deadline:
            try:
                client.interactions.cancel(iid)  # nao deixa job rodando/custando
            except Exception:
                pass
            return lib.make_result("gemini", "deep", DEEP_AGENT, query,
                                   error=f"timeout apos {DEEP_TIMEOUT}s (ultimo status '{status}')")
        time.sleep(POLL_INTERVAL)

    answer = _texto_completo(result) or getattr(result, "output_text", None) or ""
    results, citations = _extract_sources(result)
    out = lib.make_result("gemini", "deep", DEEP_AGENT, query, answer, results, citations)
    out["interaction_id"] = iid  # para recuperar o relatório sem rodar de novo
    return out


def _texto_completo(result) -> str:
    """Junta todo o texto do relatório.

    O `output_text` do SDK só traz o último trecho contínuo de texto do último
    passo: um elemento que não é texto no meio do relatório (imagem, gráfico)
    corta tudo o que vem antes: já chegou relatório só com as últimas seções
    por isso.
    """
    def val(o, k):
        return o.get(k) if isinstance(o, dict) else getattr(o, k, None)

    partes = []
    for step in val(result, "steps") or []:
        if val(step, "type") != "model_output":
            continue
        for item in val(step, "content") or []:
            if val(item, "type") == "text" and isinstance(val(item, "text"), str):
                partes.append(val(item, "text"))
    return "".join(partes)


# ---------- cli ----------

def main() -> None:
    ap = argparse.ArgumentParser(description="Pesquisa Gemini (raso: grounding; profundo: Deep Research).")
    ap.add_argument("--mode", choices=["shallow", "deep"], default="shallow")
    ap.add_argument("--query", required=True)
    ap.add_argument("--provider", choices=["aistudio", "vertex"], default="aistudio",
                    help="só no raso: aistudio (padrão, crédito) ou vertex (pós-pago)")
    args = ap.parse_args()

    runner = run_deep if args.mode == "deep" else (lambda q: run_shallow(q, args.provider))
    model = DEEP_AGENT if args.mode == "deep" else SHALLOW_MODEL
    try:
        lib.emit(runner(args.query))
    except SystemExit:
        raise
    except Exception as e:
        lib.emit(lib.make_result("gemini", args.mode, model, args.query,
                                 error=f"{type(e).__name__}: {e}"))
        sys.exit(1)


if __name__ == "__main__":
    main()
