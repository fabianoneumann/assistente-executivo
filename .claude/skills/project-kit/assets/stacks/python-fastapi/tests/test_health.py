from fastapi.testclient import TestClient

from app.main import app


def test_health_responde_ok_sem_procedencia(monkeypatch):
    monkeypatch.delenv("VERSAO", raising=False)
    monkeypatch.delenv("COMMIT", raising=False)
    resposta = TestClient(app).get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok", "versao": None, "commit": None}


def test_health_declara_a_versao_e_o_commit(monkeypatch):
    monkeypatch.setenv("VERSAO", "v1.2.3")
    monkeypatch.setenv("COMMIT", "abc1234")
    assert TestClient(app).get("/health").json() == {
        "status": "ok",
        "versao": "v1.2.3",
        "commit": "abc1234",
    }
