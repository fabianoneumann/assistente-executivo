"""O smoke: o servidor sobe de verdade e responde. Roda em todo PR (pytest -m smoke)."""

import socket
import subprocess
import sys
import time

import httpx
import pytest


def porta_livre() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@pytest.mark.smoke
def test_o_servidor_sobe_e_responde():
    porta = porta_livre()
    servidor = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--port", str(porta)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        for _ in range(50):
            try:
                resposta = httpx.get(f"http://127.0.0.1:{porta}/health", timeout=1)
                break
            except httpx.TransportError:
                time.sleep(0.2)
        else:
            pytest.fail("o servidor não respondeu em 10 s")
        assert resposta.status_code == 200
    finally:
        servidor.terminate()
        servidor.wait(timeout=10)
