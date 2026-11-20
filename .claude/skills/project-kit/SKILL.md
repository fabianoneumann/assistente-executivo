---
name: project-kit
description: >-
  Cria um projeto de software novo já estruturado: a discussão inicial antes de propor, a arquitetura e o plano macro na base `knowledge/` (LLM Wiki), os ADRs da arquitetura e do ferramental, o repositório montado a partir dos modelos (o CLAUDE.md roteador, os modelos de issue e de PR, o CI, o Dependabot só de segurança, as travas que recusam e dizem o que falta, o onboarding em HTML com os diagramas das travas, da prioridade e da sequência, conferidos por esquema no CI) e conferido por script, e o GitHub (a regra da tag, a primeira milestone e as specs). A tecnologia se escolhe a cada projeto; o processo vem pronto. USE quando a pessoa quiser começar, criar, montar ou estruturar um projeto ou sistema novo, um repositório novo com o processo, "um projeto do zero", ou levar o processo do CRM a um projeto que nasce, mesmo sem dizer "kit". NÃO use para trabalhar uma issue ou mexer no CI e no processo de um projeto que já existe, revisar código (`/code-review`), pesquisar uma tecnologia (`research`), uma página (`frontend-design`), nem para mudar o processo deste repositório.
---

# project-kit

Um projeto de software novo, do zero até a primeira milestone com as specs: a arquitetura pensada, o processo de issues e de PR com as travas, a base no padrão LLM Wiki e o onboarding. A tecnologia muda a cada projeto; o processo vem pronto, destilado da prática de um CRM de atendimento (de onde veio cada parte e a decisão: o `references/projeto.md`).

**As regras que não mudam:**
- **O projeto não cita o ambiente de onde veio.** Nenhum caminho de lá, nenhuma regra sobre ele, nenhum "ver em". Do lado de cá fica só um ponteiro de mão única (etapa 7, pelo `projeto.md`). O `conferir.py` recusa a menção.
- **As travas só recusam e dizem o que falta, ou avisam; nunca perguntam.** O projeto não leva `ask`, e nenhuma regra nova volta como pergunta de sim ou não (a fronteira está no `travas.md` da base que o projeto recebe).
- **Nenhuma pergunta de sim ou não à pessoa,** também na conversa: a pergunta é aberta, ou de escolha, com as opções e o que cada uma implica.
- **A base passa pela pessoa antes do commit.** A arquitetura, o plano, os ADRs e as specs são texto que ela lê e aprova na conversa; só então vão ao repositório.

**Antes de começar:** leia as abertas de [`licoes.md`](./licoes.md) e o [`references/projeto.md`](./references/projeto.md), com o que é deste repositório (onde o projeto nasce, o dono no GitHub, o ponteiro).

## Entra

| O quê | De onde |
|---|---|
| A ideia do projeto | o pedido da pessoa, um documento dela, ou um sistema que já existe e vai ganhar um repositório novo |
| A stack | escolhida na discussão inicial: as variantes de partida `python-fastapi` e `node-ts`, ou outra, com os comandos perguntados ([`references/stacks.md`](./references/stacks.md)) |
| O dono no GitHub | o `projeto.md` (a conta pessoal ou a organização) |

## Sai

- O repositório montado e conferido em 0 ERRO, com o primeiro commit no `main`: o `CLAUDE.md` roteador (até 150 linhas), o `AGENTS.md` curto, a base em `knowledge/` (o processo, os metadados, as travas, a versão, a arquitetura, o plano e os ADRs 001 e 002), os modelos de issue e de PR, o CI, o Dependabot, as travas com os testes, e o onboarding em `onboarding/index.html`, com `onboarding/diagramas/` (as páginas das travas, da prioridade e da sequência com o dado embutido, o motor de layout, os tokens e o `esquema.py`, que o CI roda nas páginas).
- No projeto que publica imagem (`--docker`), também o `Dockerfile`, o build no CI, a publicação na tag e o vigia semanal da imagem base.
- O repositório no GitHub, privado, com o CI verde, a regra de tag (ou o aviso de que o plano não a oferece), a primeira milestone e as specs dela.
- O ponteiro de mão única do lado do ambiente, onde o `projeto.md` diz.

## O fluxo

### 1. A discussão inicial: perguntar antes de propor, e nada escrito

**Leia [`references/discussao-inicial.md`](./references/discussao-inicial.md) antes.** Pergunte o que muda o desenho (o resultado, quem usa, onde roda, o dado, as integrações, o relógio, a equipe, a stack, os limites), em blocos de até cinco, cada pergunta aberta ou de escolha. Antes de cada uma, confira o que a conversa, os documentos dele ou o sistema que já existe respondem. Depois, a proposta na própria resposta: a arquitetura (com duas ou três opções quando há mais de uma forma razoável, e a sugestão com o porquê), os arcos, a stack e o ferramental, a primeira milestone e o que fica em aberto. **Nesta etapa não se escreve nenhum arquivo, pasta ou repositório.** Fica pronta quando dá para escrever a arquitetura, o plano e os dois ADRs sem adivinhar.

### 2. A arquitetura e o plano macro

No scratchpad, em `<scratchpad>/<nome>/base/`, a partir dos modelos `assets/projeto/knowledge/arquitetura.md` e `plano.md`: cada seção com o que a conversa decidiu, e os comentários `<!-- kit: -->` apagados. O plano leva os arcos, as grandes entregas e a ordem sugerida, com a data. O que ficou em aberto vai como item do "A decidir" de uma issue da primeira milestone, e não como suposição no texto. Quando a escolha depende de dado de fora (o estado de uma biblioteca, de um serviço), chame a `research` antes de escrever.

### 3. Os ADRs 001 e 002

Na mesma pasta, em `decisions/`, a partir de `assets/projeto/knowledge/decisions/000-modelo.md`: o `001-arquitetura-e-stack.md` e o `002-ferramental.md` (**leia o `stacks.md`, "O que vai no ADR 002", antes**). Cada um com as cinco seções e o "Revê se", o viés declarado, o custo assumido e as alternativas rejeitadas. **Mostre a arquitetura, o plano e os dois ADRs juntos à pessoa,** com uma pergunta aberta (o que ela mudaria, o que falta), e aplique o que ela pedir; quando ela diz que está bom, a etapa 4 pode commitar a base.

### 4. Montar e conferir

```
python -X utf8 .claude/skills/project-kit/scripts/montar.py --destino <pasta> --nome <nome> --descricao "<frase>" \
       --stack <stack> --dono <dono> --conta user|org [--responsavel <usuário>] --base <scratchpad>/<nome>/base [--comandos <json>] [--docker]
python -X utf8 .claude/skills/project-kit/scripts/conferir.py <pasta>
```

O `montar.py` copia os modelos, põe a stack e a base por cima, troca os marcadores, mantém só os blocos da stack, da conta e da imagem, faz o `git init` com o `core.hooksPath` ligado e prepara os arquivos. O `--docker` vai quando o sistema se instala como imagem (o que a imagem traz: o `stacks.md`, "A imagem"). O lugar da pasta está no `projeto.md`. Depois:
1. O `conferir.py` em 0 ERRO, com os AVISOs lidos. ERRO se corrige no kit ou na base, e não à mão no projeto, para o kit seguinte nascer certo; o que for do kit vai ao `licoes.md`.
2. O `CMD_INSTALAR` da stack, os testes, o smoke, os testes das travas (`python -m unittest discover -s .claude/hooks -p "test_*.py"`, e o mesmo em `.githooks`) e o esquema dos diagramas (`python onboarding/diagramas/esquema.py "onboarding/diagramas/*.html"`, o mesmo passo do CI), todos em código 0. Mudar um diagrama do projeto é mudar o bloco JSON dentro da página; o modelo e a conferência da figura ficam no kit (`assets/diagramas/LEIA.md`).
3. O primeiro commit, no `main`: `git add -A`, `git commit -m "O projeto nasce do kit: a base, as travas e o CI"`. O `pre-commit` do projeto já roda nele.

### 5. O GitHub

**Leia [`references/github.md`](./references/github.md) antes.** O `github.py`, primeiro com `--simular` e depois de verdade, com `--criar`: o repositório privado e o push, os rótulos (na conta pessoal, os de prioridade e o `defeito`), o Dependabot de segurança e a regra de tag. Confira no GitHub o CI do primeiro push verde, o `dependabot.yml` sem erro e a regra de tag; se o plano não oferece a regra, a entrega diz isso, e vale a regra escrita.

### 6. A primeira milestone e as specs

Pelo `github.md`, "A etapa 6": a milestone de cerca de duas semanas, com o critério que a fecha; uma spec por entrega, pelo modelo do projeto, com a prioridade de Eisenhower, a milestone e o "blocked by". **Mostre os corpos das specs à pessoa, todos juntos, antes de criar.** A primeira issue troca o esqueleto da stack pelo começo do sistema. Daqui em diante, cada issue segue o fluxo do `CLAUDE.md` do projeto, na sessão de lá.

### 7. O ponteiro de mão única

Pelo `projeto.md`, "O ponteiro de mão única": o registro do projeto do lado do ambiente, num commit de lá. O projeto não ganha nada que aponte para o ambiente.

## As conferências

- O `conferir.py` em 0 ERRO antes do primeiro commit (etapa 4) e depois de cada mudança nos modelos do kit.
- Os testes do kit: `python -X utf8 -m unittest discover -s .claude/skills/project-kit/scripts -p "teste_*.py"` (as três stacks montadas e conferidas, os testes das travas dentro do projeto, e cada erro plantado acusado). Rodam a cada mudança no kit. Os dos diagramas rodam cada um por si (`python -X utf8 .claude/skills/project-kit/scripts/teste_diagrama_conferir.py` e `teste_diagrama_regressao.py`). Os testes e as conferências pedem o PyYAML e o Playwright com o Chromium, do `requirements.txt` da skill (`python -m pip install -r .claude/skills/project-kit/requirements.txt`, depois `python -m playwright install chromium`).
- Os testes das travas vão junto com o projeto e rodam no CI dele.
- Ao mexer no esqueleto de uma stack, ou num modelo que cai no formato ou no lint dela (um script em `.github/`, um YAML), o `scripts/ci_local.py` num projeto montado de cada stack, com as dependências instaladas: os testes do kit não rodam o formato, o lint nem os testes da stack (lição de 19/11).

## Ao terminar

Diga à pessoa: a pasta e o repositório, o resultado do `conferir.py` e do CI, se a regra de tag existe ou ficou na regra escrita, a milestone e as specs criadas (com os links), e o que ficou em aberto. Registre no `licoes.md` desta skill o que o uso ensinou.
