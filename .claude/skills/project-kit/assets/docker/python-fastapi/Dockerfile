# syntax=docker/dockerfile:1

# A imagem do serviço (knowledge/imagem-base.md). A base é a tag flutuante da linha: todo build é com --pull, para
# a base vir a do dia, e a vigilância semanal (.github/workflows/vigiar-imagem.yml) diz quando uma versão nova precisa
# ser cortada para levar a correção dela.
FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

# Só as dependências de produção. Depois de instalar, o pip sai: o runtime só executa o uvicorn, e o que ninguém
# executa aqui só soma falha de segurança na varredura da imagem. A conferência no fim derruba o build se ele voltar.
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip uninstall -y pip \
    && if python -c "import pip" 2>/dev/null; then echo "o pip continua na imagem" >&2; exit 1; fi \
    && python --version

COPY app ./app

# A procedência: o build passa a versão (a tag) e o commit, e o /health os devolve. Vazios num build à mão: a rota
# devolve null, e ninguém mente sobre o que roda.
ARG VERSAO=""
ARG COMMIT=""
ENV VERSAO=$VERSAO COMMIT=$COMMIT

# Nada aqui precisa de root.
RUN useradd --system --uid 1000 --no-create-home app
USER app
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
