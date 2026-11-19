"""Perguntas do Jev sobre a imagem renderizada de uma tela: só defeitos concretos de ver.

Experimental: a TypeSafe chama imagem de "dreamer-ready" e exige o cabeçalho
`TypeSafe-Danger-Zone-Images: true`. Julgamento estético fica fora (os estudos de modelos de
visão julgando design, como o AesEval-Bench e o DesignSense, mostram que até os melhores falham
nisso): aqui o Jev só responde se o defeito está na tela.

Texto cortado: uma pergunta por borda, e o código junta (cortado se alguma borda corta), adaptando
a receita da documentação da TypeSafe de uma pergunta Noul por borda.

Uso: python -X utf8 scripts/jev/imagens.py <saida.json> <tela1.jpg> [<tela2.jpg> ...]
Pede TYPESAFE_API_KEY (ver .env.example); sem ela, sai com a mensagem de como configurar.
"""
import base64, io, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cliente import chamar as chamar_jev, ErroJev, tem_chave, SemChaveJev

MODELO = "jev-1.14.0"


def noul(instrucao, sim, nao):
    return {"type": "noul", "instructions": instrucao, "criteria": {"true": sim, "false": nao}}


BORDAS = {"cima": "de cima", "baixo": "de baixo", "esquerda": "da esquerda", "direita": "da direita"}
PERGUNTAS = {
    f"cortado_{k}": noul(
        f"Algum texto em `tela` é cortado pela borda {nome} da imagem?",
        f"Uma palavra ou uma linha some na borda {nome} antes de terminar: faltam letras ou a parte de baixo ou de cima delas.",
        f"O texto mais perto da borda {nome} termina inteiro dentro da imagem.",
    )
    for k, nome in BORDAS.items()
}


def texto_cortado(a, sim=0.7, nao=0.3):
    """Cortado se alguma borda corta; não cortado se todas dizem que não; None se alguma fica no meio."""
    v = [a.get(f"cortado_{k}") for k in BORDAS]
    if any(x is not None and x >= sim for x in v):
        return True
    return False if all(x is not None and x <= nao for x in v) else None


LADO_MAX = 1536  # a API recusa 1080x1920 ("Invalid image dimensions"); 864x1536 passa


def ler_imagem(caminho):
    """Bytes da imagem; reduz mantendo a proporção quando um lado passa do que a API aceita (o Story tem 1920 de altura)."""
    from PIL import Image
    im = Image.open(caminho)
    if max(im.size) <= LADO_MAX:
        return open(caminho, "rb").read()
    im.thumbnail((LADO_MAX, LADO_MAX))
    buf = io.BytesIO(); im.convert("RGB").save(buf, "JPEG", quality=92)
    return buf.getvalue()


def chamar(caminho):
    dados = base64.b64encode(ler_imagem(caminho)).decode("ascii")
    ref = "tela-" + os.path.basename(caminho).replace(".", "-")
    corpo = {"model": MODELO, "state": {"tela": ref},
             "assets": {ref: {"type": "image", "format": "jpg", "data_base64": dados}},
             "questions": PERGUNTAS}
    return chamar_jev(corpo, {"TypeSafe-Danger-Zone-Images": "true"}, timeout=180, orcamento=300)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    if not tem_chave():
        raise SemChaveJev()
    saida, telas = sys.argv[1], sys.argv[2:]
    out = {}
    for t in telas:
        try:
            resp, meta = chamar(t)
        except ErroJev as err:
            print(t, "ERRO", err); continue
        a = {k: v.get("noul") for k, v in resp["answers"].items()}
        out[t] = {"respostas": a, "texto_cortado": texto_cortado(a), "uso": resp.get("usage"), "modelo": meta["modelo"], "segundos": meta["segundos"],
                  "request_id": meta["request_id"], "tentativas": meta["tentativas"], "custo_usd": meta["custo_usd"]}
        print(os.path.basename(os.path.dirname(t)), os.path.basename(t), {k: round(v, 2) for k, v in a.items()}, resp.get("usage"))
    json.dump(out, open(saida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
