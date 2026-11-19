"""Chamada à API do Jev com a política de novas tentativas do SDK oficial, sem depender do pacote.

Copiado do `RetryPolicy` do SDK de Python (docs.typesafe.ai/sdk/python/api/retries): até 2 tentativas
a mais em 408, 429, 5xx, falha de conexão e tempo esgotado; espera de 0,5 s dobrando até 5 s, com
variação de 25% para mais ou para menos; `retry-after-ms` e `Retry-After` mandam na espera quando
vêm na resposta; orçamento total por chamada (primeira tentativa e esperas incluídas), que para antes
de uma nova tentativa cuja espera chegaria ao limite. Erro de pedido (400, 401, 422...) não se repete.

Antes de enviar, `NaN` e infinito viram erro aqui (a API recusa com 400). Cada resposta volta com o
id da requisição (`x-typesafe-request-id`), as tentativas, os segundos e o custo pelo preço publicado.
"""
import email.utils, json, os, random, socket, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ambiente  # noqa: E402  (lê o .env da raiz sem sobrescrever o ambiente; cópia de scripts/ambiente.py)

SEM_CHAVE = ("[jev] TYPESAFE_API_KEY não configurada (o Jev, da TypeSafe, é opcional nas skills deste repositório). "
             "Onde se pega: https://docs.typesafe.ai (o painel da TypeSafe, chaves de API). "
             "Como pôr: copie o `.env.example` para `.env` na raiz do repositório e preencha a linha TYPESAFE_API_KEY, "
             "ou ponha no bloco \"env\" do `.claude/settings.local.json`; depois, reinicie a sessão. "
             "Para conferir: python -X utf8 scripts/confere_ambiente.py")


def tem_chave():
    """True quando há TYPESAFE_API_KEY: quem usa o Jev como opcional pergunta antes e pula com aviso."""
    return bool(ambiente.valor("TYPESAFE_API_KEY"))

URL = "https://api.typesafe.ai/v1/systemone"
PRECO_POR_MILHAO = 0.042  # US$ por milhão de tokens de entrada; a saída não é cobrada (docs.typesafe.ai/models)
REPETE = {408, 429} | set(range(500, 600))


class SemChaveJev(SystemExit):
    """Falta a chave: sai com a mensagem de como configurar, sem traceback, mesmo sem ninguém capturar."""

    def __init__(self):
        super().__init__(SEM_CHAVE)


class ErroJev(Exception):
    """Falha de chamada: nunca deve ser lida como resposta."""

    def __init__(self, mensagem, status=None, request_id=None, tentativas=1):
        super().__init__(f"{mensagem} (status {status}, requisição {request_id}, {tentativas} tentativa(s))")
        self.status, self.request_id, self.tentativas = status, request_id, tentativas


def _espera_pedida(cabecalhos):
    """Segundos que o servidor pediu para esperar, ou None."""
    if cabecalhos is None:
        return None
    ms = cabecalhos.get("retry-after-ms")
    if ms:
        try:
            return max(0.0, float(ms) / 1000)
        except ValueError:
            pass
    ra = cabecalhos.get("Retry-After")
    if ra:
        try:
            return max(0.0, float(ra))
        except ValueError:
            try:
                data = email.utils.parsedate_to_datetime(ra)
            except (TypeError, ValueError):  # data malformada: o servidor não pediu espera que se leia
                return None
            return max(0.0, data.timestamp() - time.time()) if data else None
    return None


def chamar(corpo, cabecalhos=None, timeout=120, orcamento=30.0, tentativas_extras=2, url=None, chave=None, dormir=time.sleep):
    """Envia `corpo` e devolve (resposta, meta). Levanta ErroJev se a chamada falhar de vez.

    Sem TYPESAFE_API_KEY, levanta SemChaveJev (um SystemExit com a mensagem de como configurar), que encerra
    o script com a mensagem e sem traceback; quem trata o Jev como opcional confere antes com `tem_chave()`."""
    dados = json.dumps(corpo, ensure_ascii=False, allow_nan=False).encode("utf-8")  # ValueError com NaN, antes de gastar
    chave = (chave or ambiente.valor("TYPESAFE_API_KEY")).strip()
    if not chave:
        raise SemChaveJev()
    h = {"Authorization": "Bearer " + chave, "Content-Type": "application/json", **(cabecalhos or {})}
    url = url or os.environ.get("TYPESAFE_URL", URL)
    t0, espera = time.time(), 0.5
    for n in range(1, tentativas_extras + 2):
        rid, pedida = None, None
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=dados, method="POST", headers=h), timeout=timeout) as r:
                bruto = r.read().decode("utf-8", "replace")
                try:
                    resp = json.loads(bruto)
                except json.JSONDecodeError:
                    raise ErroJev(f"resposta que não é JSON: {bruto[:200]}", r.status, r.headers.get("x-typesafe-request-id"), n) from None
                rid = r.headers.get("x-typesafe-request-id")
            tokens = (resp.get("usage") or {}).get("input_tokens", 0)
            return resp, {"request_id": rid, "tentativas": n, "segundos": round(time.time() - t0, 2), "modelo": resp.get("model"),
                          "tokens_de_entrada": tokens, "custo_usd": tokens * PRECO_POR_MILHAO / 1e6}
        except urllib.error.HTTPError as err:
            rid, pedida = err.headers.get("x-typesafe-request-id"), _espera_pedida(err.headers)
            falha = ErroJev(err.read().decode("utf-8", "replace")[:300], err.code, rid, n)
            if err.code not in REPETE:
                raise falha from None
        except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError) as err:
            falha = ErroJev(f"sem resposta do servidor: {err}", None, None, n)
        if n > tentativas_extras:
            break
        atraso = pedida if pedida is not None else espera * random.uniform(0.75, 1.25)
        if orcamento is not None and time.time() - t0 + atraso >= orcamento:
            break
        dormir(atraso)
        espera = min(espera * 2, 5.0)
    raise falha
