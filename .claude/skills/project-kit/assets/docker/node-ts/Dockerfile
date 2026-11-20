# syntax=docker/dockerfile:1

# A imagem do serviço (knowledge/imagem-base.md). A base é a tag flutuante da linha: todo build é com --pull, para
# a base vir a do dia, e a vigilância semanal (.github/workflows/vigiar-imagem.yml) diz quando uma versão nova precisa
# ser cortada para levar a correção dela.

# ---- as dependências de produção ----
FROM node:24-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
# A pasta existe mesmo sem dependência de produção, para o COPY do estágio seguinte não falhar.
RUN npm ci --omit=dev --ignore-scripts --no-audit --no-fund && mkdir -p node_modules

# ---- o runtime ----
FROM node:24-alpine AS runtime
WORKDIR /app
ENV NODE_ENV=production

# A procedência: o build passa a versão (a tag) e o commit, e o /health os devolve. Vazios num build à mão: a rota
# devolve null, e ninguém mente sobre o que roda.
ARG VERSAO=""
ARG COMMIT=""
ENV VERSAO=$VERSAO COMMIT=$COMMIT

COPY --from=deps /app/node_modules ./node_modules
COPY package.json ./
COPY src ./src

# Sem os gerenciadores de pacote que a imagem oficial traz (npm, npx, corepack, yarn): o runtime só executa o
# `node`, e o que ninguém executa aqui só soma falha de segurança na varredura. Os caminhos são os da imagem oficial:
# se ela mudar a disposição, a conferência no fim derruba o build, em vez de o npm voltar calado.
RUN rm -rf /usr/local/lib/node_modules /opt/yarn-v* \
    && rm -f /usr/local/bin/npm /usr/local/bin/npx /usr/local/bin/corepack /usr/local/bin/yarn /usr/local/bin/yarnpkg \
    && for p in npm npx corepack yarn yarnpkg; do \
        if command -v "$p" >/dev/null; then echo "o $p continua na imagem: $(command -v "$p")" >&2; exit 1; fi; \
    done \
    && node --version

# O usuário `node` já existe na imagem oficial; nada aqui precisa de root.
USER node
EXPOSE 3000
CMD ["node", "src/servidor.ts"]
