"""Confere a política de novas tentativas de `cliente.chamar` contra um servidor local, sem chamar a API.

Uso: python teste_cliente.py (sai com erro no primeiro caso fora da regra).
Cada caso dá ao servidor uma fila de respostas (status, cabeçalhos) e confere quantas chamadas
chegaram, quanto o cliente esperou e o que voltou.
"""
import json, os, socket, sys, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cliente import chamar, ErroJev

FILA, PEDIDOS = [], []
OK = {"model": "jev-1.14.0", "answers": {"x": {"type": "noul", "noul": 0.9}}, "usage": {"input_tokens": 1000}}


class Servidor(BaseHTTPRequestHandler):
    def do_POST(self):
        corpo = self.rfile.read(int(self.headers["Content-Length"]))
        PEDIDOS.append({"corpo": corpo, "auth": self.headers["Authorization"]})
        status, cabecalhos = FILA.pop(0)
        texto = json.dumps(OK if status == 200 else {"error": "falha de teste"}).encode("utf-8")
        self.send_response(status)
        for k, v in {"x-typesafe-request-id": f"req_{len(PEDIDOS)}", "Content-Type": "application/json", **cabecalhos}.items():
            self.send_header(k, v)
        self.send_header("Content-Length", str(len(texto)))
        self.end_headers()
        self.wfile.write(texto)

    def log_message(self, *a):
        pass


srv = ThreadingHTTPServer(("127.0.0.1", 0), Servidor)
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f"http://127.0.0.1:{srv.server_port}/v1/systemone"
CORPO = {"model": "jev-1.14.0", "state": {"texto": "ação"}, "questions": {}}


def caso(fila, **kw):
    FILA[:], PEDIDOS[:] = list(fila), []
    esperas = []
    kw.setdefault("dormir", esperas.append)
    try:
        return chamar(kw.pop("corpo", CORPO), url=kw.pop("url", URL), chave=" chave-de-teste\n", **kw), esperas
    except ErroJev as err:
        return err, esperas


def confere(nome, cond, detalhe=""):
    assert cond, f"{nome}: {detalhe}"
    print("ok", nome)


# 429 com Retry-After de 1 s, depois 200: espera de verdade e um resultado só
t0 = time.time()
(resp, meta), _ = caso([(429, {"Retry-After": "1"}), (200, {})], dormir=time.sleep)
confere("429 e depois 200: duas chamadas", len(PEDIDOS) == 2, len(PEDIDOS))
confere("429 e depois 200: esperou o Retry-After", time.time() - t0 >= 1.0, time.time() - t0)
confere("429 e depois 200: id e tentativas da que deu certo", (meta["request_id"], meta["tentativas"]) == ("req_2", 2), meta)
confere("custo pelo preço publicado", abs(meta["custo_usd"] - 1000 * 0.042 / 1e6) < 1e-12, meta["custo_usd"])

# retry-after-ms manda sobre o Retry-After
_, esperas = caso([(503, {"retry-after-ms": "200", "Retry-After": "9"}), (200, {})])
confere("retry-after-ms tem precedência", esperas == [0.2], esperas)

# 500 sempre: três chamadas, esperas de 0,5 e 1 s com variação, depois erro com status e id
err, esperas = caso([(500, {})] * 3)
confere("500 sempre: três chamadas", len(PEDIDOS) == 3, len(PEDIDOS))
confere("500 sempre: erro, não resposta", isinstance(err, ErroJev) and (err.status, err.tentativas, err.request_id) == (500, 3, "req_3"), err)
confere("500 sempre: espera dobra", len(esperas) == 2 and 0.375 <= esperas[0] <= 0.625 and 0.75 <= esperas[1] <= 1.25, esperas)

# 400 é erro do pedido: não repete
err, esperas = caso([(400, {})])
confere("400 não repete", len(PEDIDOS) == 1 and isinstance(err, ErroJev) and err.status == 400 and not esperas, (len(PEDIDOS), err))

# espera pedida que estoura o orçamento: desiste sem dormir
err, esperas = caso([(429, {"Retry-After": "40"})], orcamento=30)
confere("orçamento de 30 s barra espera de 40 s", len(PEDIDOS) == 1 and not esperas and err.status == 429, (len(PEDIDOS), esperas))

# NaN não sai daqui
FILA[:], PEDIDOS[:] = [], []
try:
    chamar({**CORPO, "state": {"x": float("nan")}}, url=URL, chave="k"); confere("NaN recusado", False, "passou")
except ValueError:
    confere("NaN recusado antes de enviar", len(PEDIDOS) == 0)

# corpo em UTF-8 sem BOM e chave aparada
caso([(200, {})])
confere("UTF-8 sem BOM", not PEDIDOS[0]["corpo"].startswith(b"\xef\xbb\xbf") and "ação" in PEDIDOS[0]["corpo"].decode("utf-8"))
confere("chave aparada", PEDIDOS[0]["auth"] == "Bearer chave-de-teste", PEDIDOS[0]["auth"])

# servidor fora do ar: três tentativas e erro sem status
s = socket.socket(); s.bind(("127.0.0.1", 0)); porta = s.getsockname()[1]; s.close()
err, esperas = caso([], url=f"http://127.0.0.1:{porta}/v1/systemone", timeout=2)
confere("sem servidor: erro depois de três tentativas", isinstance(err, ErroJev) and err.status is None and err.tentativas == 3 and len(esperas) == 2, err)

srv.shutdown()
print("todos os casos passaram")
