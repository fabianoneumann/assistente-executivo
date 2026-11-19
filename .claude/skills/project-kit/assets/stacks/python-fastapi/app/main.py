"""O ponto de entrada do serviço. O primeiro endpoint é o de saúde, que o smoke do CI chama."""

from fastapi import FastAPI

app = FastAPI(title={{NOME_JSON}})


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
