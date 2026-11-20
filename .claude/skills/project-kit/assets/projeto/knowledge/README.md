# A base do projeto: as regras de operação

A base guarda o **porquê** do projeto: o desenho, a arquitetura, o plano, as decisões e o que se aprendeu. Segue o padrão LLM Wiki (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): arquivos markdown que acumulam contexto ao longo do tempo, em vez de redescobrir tudo a cada sessão.

## Como usar

- **Antes de uma tarefa,** ler o `index.md` e abrir só os arquivos cujo "ler quando" casa com ela.
- **Ao aprender algo,** atualizar o arquivo certo, refletir no `index.md` se mudou o critério de leitura, e pôr uma entrada no fim do `log.md`.
- **Decisão de arquitetura ou de ferramental** vira ADR em `decisions/<número>-<tema>.md`, copiado de `decisions/000-modelo.md`. Um número por decisão; a que substitui outra diz qual e o que sobrevive dela.
- **O ADR é vivo.** Quando outro ADR muda parte dele, o de antes ganha no topo a linha "alterado pelo ADR N" (o que mudou, em uma frase), sem reescrever o resto; quando um ponto da implementação é entregue, ganha "feito na #N" ao lado. Quem lê o ADR sabe o que ainda vale e o que já existe sem abrir o histórico.
- **A investigação que alimenta uma decisão** vai em `analysis/`, e a decisão fica no ADR ou no corpo da issue.

## As regras

- **Citar, não inventar.** Toda afirmação sobre o sistema vem do código ou do que está registrado aqui. Sem fonte, é dúvida, e vai ao "A decidir" da issue.
- **O que não mora aqui.** O como-fazer-agora fica junto do artefato: a operação em `docs/`, o roteiro do script ao lado dele. Assim o ADR não vira manual, e o manual não vira fonte de decisão.
- **Sem credencial e sem informação comercial.** A base é técnica e se compartilha com quem entra no projeto.
- **O texto da base passa pela pessoa** antes do commit do agente (`CLAUDE.md`, "A base validada antes do commit").
- **Teto de ~150 linhas por arquivo;** passou, divide-se num arquivo mais específico. Ficam de fora o `log.md` e o `index.md`, que são os dois arquivos especiais do padrão.
- **O log cresce pelo fim,** uma entrada por acontecimento, no formato `## [AAAA-MM-DD] <tipo> | <assunto>`. As últimas se leem com `grep "^## \[" knowledge/log.md | tail -5`. O `.gitattributes` o junta por união no merge, o hook do commit recusa a entrada fora do formato ou que não vai no fim, e o CI, a fora do formato.
- **Markdown sem quebra de linha manual:** o parágrafo é uma linha só, e a quebra é do editor.
