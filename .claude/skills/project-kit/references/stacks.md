# As stacks

O kit traz o processo pronto e deixa a tecnologia à escolha de cada projeto. As variantes de partida trazem os comandos e os arquivos de configuração; para outra stack, a skill pergunta os mesmos campos. **Leia antes da etapa 3** (o ADR 002 nasce daqui) **e antes da etapa 4.**

## As variantes de partida

| | `python-fastapi` | `node-ts` |
|---|---|---|
| A linguagem | Python 3.12 | Node 24, com o TypeScript rodado direto pelo Node |
| O formato | `ruff format` | Prettier |
| O lint | `ruff check` | `tsc --noEmit` (o typecheck) |
| Os testes | `pytest`, com o marcador `smoke` | `node --test`, com "smoke" no nome do teste |
| O Dependabot | `pip` | `npm` |
| O que o kit põe na raiz | `pyproject.toml` (o ruff e os marcadores do pytest), `requirements.txt` (produção) e `requirements-dev.txt` (por cima dele) fixados, `app/main.py` com o `/health` e, em `tests/`, um teste dele e o smoke, que sobe o servidor de verdade | `package.json` (os scripts), `tsconfig.json`, `.prettierrc.json`, `.prettierignore`, `src/servidor.ts` com o `/health` e, em `test/`, um teste dele e o smoke |

Os comandos exatos estão em `assets/stacks.json`, e é de lá que o `montar.py` os lê. O esqueleto (o `/health`, o teste e o smoke) existe para o CI nascer verde e o smoke ter o que provar; o sistema de verdade começa na primeira issue da primeira milestone, que troca o esqueleto pelo que a arquitetura pede.

**Antes do primeiro commit, rode o `CMD_INSTALAR` uma vez** e os testes: na `node-ts`, ele gera o `package-lock.json`, que o `npm ci` do CI e o cache do `setup-node` pedem, e o lock vai no primeiro commit.

## Outra stack

Pergunte cada campo abaixo (pergunta aberta, com o exemplo das variantes ao lado), grave as respostas num JSON no scratchpad e passe ao `montar.py` por `--stack outra --comandos <arquivo>`:

| Campo | O que é | Exemplo (python-fastapi) |
|---|---|---|
| `STACK_DESCRICAO` | a stack em uma linha, para o `CLAUDE.md` | Python 3.12, FastAPI, pytest e ruff |
| `CMD_INSTALAR` | instalar as dependências na máquina de quem desenvolve | `python -m pip install -r requirements-dev.txt` |
| `CMD_CI_INSTALAR` | instalar no CI, a partir do arquivo travado | o mesmo |
| `CMD_FORMATAR`, `CMD_FORMATAR_CHECK` | formatar, e só conferir | `python -m ruff format .`, `... --check .` |
| `CMD_LINT` | o lint ou o typecheck | `python -m ruff check .` |
| `CMD_TESTES`, `CMD_SMOKE`, `CMD_E2E` | os testes sem o smoke, só o smoke, e a bateria inteira | `pytest -m "not smoke"`, `-m smoke`, tudo |
| `FORMATADOR` | o formatador que lê do stdin e escreve a versão formatada no stdout, com `{arquivo}` no lugar do caminho | `["python", "-m", "ruff", "format", "--stdin-filename", "{arquivo}", "-"]` |
| `EXTENSOES` | as extensões que o `pre-commit` confere | `[".py"]` |
| `ECOSSISTEMA` | o `package-ecosystem` do Dependabot | `pip` |

Sem um formatador que leia do stdin, o `pre-commit` não confere o formato (ponha `["true"]` e diga no ADR 002); o CI confere pelo `CMD_FORMATAR_CHECK`. O passo de instalar a linguagem no CI (o `setup-*`) não vem pronto na `outra`: escreva-o no `ci.yml` depois de montar, com a ação fixada pelo hash do commit (o `conferir.py` recusa a ação sem hash).

## A imagem (`--docker`)

Quando a discussão inicial diz que o sistema se instala como imagem de contêiner, o `montar.py` recebe `--docker`, e o projeto ganha, nas duas variantes de partida: o `Dockerfile` (a base na tag flutuante da linha, com `--pull` em todo build, o runtime sem o gerenciador de pacote, a versão e o commit que o `/health` devolve, sem root), o `.dockerignore`, o job `imagem` no CI (o build, o contêiner de pé e o `/health` conferido), a publicação no ghcr.io no push da tag (imutável), o vigia semanal da imagem base (o runtime atrás de versão nova da linha e o Trivy fixado pelo hash, uma issue por imagem, que só comenta quando algo muda) e a página `knowledge/imagem-base.md`. Sem `--docker`, nada disso nasce, e o `versao-e-dependencias.md` só diz que o projeto que publica imagem ganha a vigilância à parte. Na `outra`, o `--docker` recusa: o `Dockerfile` se escreve à mão a partir dos modelos de `assets/docker/`, e o `conferir.py` cobra as demais peças juntas.

## O que vai no ADR 002

O ferramental: o formatador, o lint, o executor de testes, a divisão entre o smoke e a bateria inteira, o gerenciador de dependências e o arquivo travado, e o que o CI roda, com o teto de 3 minutos. Cada escolha com o viés declarado e a alternativa rejeitada.
