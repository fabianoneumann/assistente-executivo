"""O ponto de entrada do serviço. O primeiro endpoint é o de saúde, que o smoke do CI chama."""

import os

from fastapi import FastAPI

app = FastAPI(title={{NOME_JSON}})


@app.get("/health")
def health() -> dict[str, str | None]:
    # A instalação declara o que roda: a versão e o commit chegam do build (VERSAO e COMMIT).
    # Vazios, num build à mão ou fora da imagem, saem null, e ninguém mente sobre a procedência.
    return {
        "status": "ok",
        "versao": os.environ.get("VERSAO") or None,
        "commit": os.environ.get("COMMIT") or None,
    }
