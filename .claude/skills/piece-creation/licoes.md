# Lições da skill `piece-creation`

O que o uso e a edição desta skill ensinaram. Antes de usar a skill, leia as abertas e as apontadas; ao terminar, registre a lição nova aqui, na mesma entrega. A lição que vale para várias skills fica em [`../licoes-gerais.md`](../licoes-gerais.md); a lição da peça (mensagem, forma, exportação) fica em `marketing/licoes.md`, e esta skill aponta com uma linha.

**O formato** é o de [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md): cada lição nova entra em **Abertas**, com as quatro perguntas da revisão depois da ação (o que devia acontecer, o que aconteceu, por quê, o que mudar), **quando vale**, a evidência (arquivo e linha), a **gravidade** (crítica, maior, menor) e as **ocorrências**. As seções são Abertas, Apontadas (a lição mora em outro arquivo), A sair, Viraram regra e Saíram; seção vazia pode faltar. A lição de procedimento que já funcionou num caso real vira regra sem mesa; a que toca critério de quem decide, custo ou publicação espera a decisão dessa pessoa. As lições da equipe entram em "Abertas".

## Abertas

(nenhuma)

## Apontadas

- [`../licoes-gerais.md`](../licoes-gerais.md), sobre os testes com erros plantados: ao testar esta skill em cópias limpas do projeto, a pasta `evals/` não vai às cópias, porque traz o gabarito.

## Viraram regra

| Lição | Onde entrou |
|---|---|
| Marque "a fazer" o passo que ainda não chegou, e "parado" só o que parou: escrever "parado: espera o passo X" nos passos seguintes confunde o que parou com o que não começou | `SKILL.md`, a tabela do estado |
| Escolha a identidade de um quadro novo com uma tela renderizada de cada direção, numa mesa de forma própria, na primeira peça do quadro: sem tela, a escolha na primeira mesa da ideia crua saía mal | `references/ideia-crua.md`, seção 3 |
| Na resposta de véspera, junte a escolha das respostas e a prévia numa parada só, escreva o critério da escolha na sequência que prepara a resposta e desça antes da noite a lista dos desenhos não usados da semana: a escolha tarde da noite, com o critério escrito só depois de ver as respostas, não era cega | `references/stories.md`, "Os narrativos e as respostas" |
| Escreva o porquê de uma regra da skill sem contar o caso (a data, a peça, o resultado): a skill testada em cópias limpas que trazia o desfecho dos cenários vazava o gabarito para o agente da rodada | o texto desta skill; vale ao editá-la |
