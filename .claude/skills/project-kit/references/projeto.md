# O que é deste repositório

O arquivo da skill com o que é deste ambiente: onde o projeto nasce, quem é o dono no GitHub, o ponteiro que fica do lado de cá e onde está o porquê do kit. O porquê: a decisão em `decisions/kit-de-projeto-novo.md` (as escolhas de gosto e as decididas, com o porquê de cada uma) e o desenho em `knowledge/software-engineering/kit-de-projeto-novo.md`, que diz de onde veio cada parte: o processo de um CRM de atendimento em produção. O `SKILL.md`, os outros arquivos de `references/` e os modelos de `assets/` guardam o método, que vale em qualquer ambiente; ao levar a skill a outro lugar, troca-se este arquivo.

## Onde o projeto nasce

- **Ao lado do assistente:** na mesma pasta onde está o clone deste repositório, em `../<nome>/`. O projeto é um repositório próprio, e não uma subpasta deste: nada do projeto entra aqui, e nada daqui entra lá.
- **O teste e o ensaio** vão em `../projetos-teste/<nome>/`, e se apagam depois.
- **O rascunho da base** (a arquitetura, o plano e os ADRs das etapas 2 e 3) fica na pasta temporária da sessão, em `<scratchpad>/<nome>/base/`, até o `montar.py` levá-lo ao projeto.

## O dono no GitHub

- **A sua conta pessoal** (`--dono <seu usuário> --conta user`). Nela, a natureza da issue vai pelo rótulo `defeito` e a prioridade pelos rótulos `prioridade:*` (a matriz de Eisenhower), porque o Type e o campo Priority nativos só existem em organização: o `montar.py --conta user` escreve o `metadados.md` e o modelo de defeito assim, e o `github.py` cria os rótulos.
- **A regra da tag é escrita, sem ruleset.** No repositório privado de conta pessoal, a regra de tag do GitHub pede o plano Pro (a criação devolve 403). O `montar.py --conta user` escreve no `CLAUDE.md` do projeto que a tag publicada não se move nem se apaga, e o `github.py` não tenta criar a regra. Quem tem o Pro, ou cria o repositório público, pode criá-la à mão (`references/github.md`).
- **O responsável dos PRs do Dependabot é opcional,** e a skill não pergunta por ele: quem cria o projeto já o acompanha (com o watch ligado) e recebe o alerta e o PR por e-mail. O `--responsavel <usuário>` só acrescenta o `assignees` quando quem usa quer outro nome atribuído.
- **Numa organização** (`--conta org`), o Type e a Priority são nativos e quem os cria é o administrador dela; Quem leva a skill a uma organização troca esta seção.
- **O repositório nasce privado.** O público só por pedido de quem usa.

## O ponteiro de mão única

O projeto não cita este repositório: nenhum caminho, nenhuma regra sobre ele, nenhum "ver no assistente" (o `conferir.py` recusa a menção ao `assistente-executivo` e avisa da palavra "vault"). Do lado de cá fica só o ponteiro, na etapa 7, num commit daqui:

- `projects/<nome>.md`, com o frontmatter de entidade (`nome`, `status`), a fase, o lugar (a pasta e o repositório), o tipo e a frase "Rumo, decisões (ADRs), arquitetura e o que está em aberto vivem em `knowledge/` do próprio repositório". O arquivo daqui é ponteiro e não rastreia estado.
- A linha na tabela de `projects/index.md`. A pasta `projects/` nasce com o primeiro projeto: quem a cria acrescenta também a linha dela no `index.md` da raiz.
- A pesquisa do mundo de fora que embasou o desenho vai à base deste repositório (`knowledge/`, pela skill `research`); a do próprio projeto vai à `knowledge/analysis/` dele.

## O que as outras skills daqui fazem

| Etapa | Skill | Para quê |
|---|---|---|
| 1 e 2, quando a escolha depende de dado de fora | `research` | o estado de uma biblioteca, de um serviço ou de uma prática, com as fontes na base deste repositório |
| 2 e 3 | `review` | o texto da arquitetura, do plano e dos ADRs antes de a pessoa ler, quando o projeto é grande |
| 4 | `/code-review` | o código que o kit não trouxe pronto, se a etapa escreveu algum |
