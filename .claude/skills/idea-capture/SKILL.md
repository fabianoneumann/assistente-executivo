---
name: idea-capture
description: >-
  Registro rápido de uma ideia crua na pasta de ideias de conteúdo do projeto, sem pesquisar, sem desenvolver e sem propor ângulos, para a pessoa não perder um insight no meio de outra coisa e voltar em segundos ao que estava fazendo. USE quando a pessoa pedir explicitamente para registrar, anotar ou guardar uma ideia ("quero registrar uma ideia", "registre a seguinte ideia", "tive uma ideia de conteúdo que quero registrar", "anota essa ideia"). NÃO use quando ela apenas mencionar, comentar ou pedir opinião sobre uma ideia sem pedir o registro, nem para desenvolver ou aprofundar uma ideia já registrada (isso é outro trabalho, como a `story-angle`).
---

# Skill: idea-capture

Captura de ideia crua. **Velocidade é a funcionalidade:** a pessoa está no meio de outra coisa (um filme, uma série, um trabalho) e quer só não perder a ideia. O sucesso é ela voltar ao que estava fazendo em segundos, sem ter que dizer nenhuma restrição.

**Lições:** antes de começar, leia as abertas e as apontadas em [`licoes.md`](./licoes.md) desta pasta.

**O que é deste projeto** (a pasta das ideias, o desvio para outro domínio, as decisões que valem aqui) está em [`references/projeto.md`](./references/projeto.md). Leia antes de escrever.

**Por que a pasta funciona assim:** ela aceita a ideia crua sem ângulo nem pesquisa, porque baixar a fricção da captura é o que faz a ideia não se perder; e, quando a ideia vira peça, o arquivo encolhe para hub de tema (a nota de estado, o link para a peça e as derivações), para não duplicar o rascunho e para o tema continuar rendendo peças. A linha de abertura usa `**Nota:**`, e a ideia crua não leva o campo `estagio` no frontmatter (ele só aparece quando a produção começa; ver `decisions/artefatos-e-estagio.md`). Esta skill executa isso; não redefine.

## Nunca

Esta é a parte que carrega a skill. Nada aqui é negociável no momento da captura:

- **Não faça pergunta nenhuma.** Cada pergunta é um turno que a pessoa precisa responder no meio do que estava fazendo. Se algo ficou ambíguo, registre do jeito que veio.
- **Não pesquise.** Não chame a skill `research`, não busque na web, não confira dado. Ideia crua entra crua, inclusive com número não verificado.
- **Não invente ângulo.** Se ela não trouxe enquadramento, o arquivo fica sem enquadramento. Ângulo escrito antes de qualquer apuração ancora a peça futura e é o mecanismo que produz conteúdo raso.
- **Não desenvolva.** Sem estruturar em telas, sem sugerir gancho, sem propor título de post, sem listar próximos passos.
- **Não opine.** Sem "boa ideia", sem "isso conversa com tal teoria".
- **Não commite.**

## Registrar

Só o que existe. Seção sem conteúdo não entra no arquivo.

- **Tema:** o território, amplo, de uma a três linhas. Amplo de propósito: o recorte vem depois, na `story-angle`. Se a pessoa já delimitou, respeite.
- **A ideia:** o que ela disse, preservado. Na dúvida entre resumir e manter as palavras dela, mantenha as palavras dela.
- **Gatilho:** o que ela estava vendo, lendo ou fazendo quando a ideia veio, se mencionou. É o que evapora mais rápido e vale muito na hora de desenvolver.
- **Ângulos-hipótese:** **só os que ela trouxe**, marcados como hipótese.

## Onde escrever

Na pasta de ideias de `references/projeto.md`, num arquivo `<tema-em-kebab-case>.md` (nome do arquivo sem acentos; texto do arquivo em português normal). Desvio só quando for inequivocamente de outro domínio, pela tabela do mesmo arquivo. Na menor dúvida, é a pasta de ideias.

**Arquivo novo ou derivação de hub existente?** Antes de escrever, olhe os nomes dos arquivos da pasta e, nos candidatos plausíveis, a seção `## Tema`.

- **Arquivo novo:** tema novo, sem eixo em comum com o que já existe. É o caso normal, não a exceção.
- **Item em "Derivações / ângulos futuros" de um hub existente:** só quando a ideia é do **mesmo eixo** e a conexão é direta e óbvia.
- **Na dúvida, arquivo novo**, citando na confirmação o hub com que talvez converse. Erro assimétrico: arquivo novo que era derivação custa uma fusão trivial; ideia enterrada como item no hub errado some, porque ninguém vai procurar lá.

## Formato do arquivo novo

```markdown
# <Tema, em uma frase>

**Nota:** ideia crua registrada em AAAA-MM-DD.

## Tema
<o território, amplo>

## A ideia
<o que a pessoa disse>

## Gatilho
<o que ela estava vendo, lendo ou fazendo; só se houver>

## Ângulos-hipótese
<só os que ela trouxe; omitir a seção inteira se não trouxe>
```

## Confirmar

**Uma linha.** O caminho do arquivo, o que foi feito e, se for o caso, o hub possivelmente relacionado. Nada além disso: sem devolver a ideia resumida, sem sugerir o que fazer depois, sem perguntar se ficou bom.

> Registrei em `<pasta de ideias>/ia-e-energia.md` (arquivo novo; pode ter relação com `impacto-ambiental-da-ia.md`).

## Pronto quando

- Nada do que a pessoa disse se perdeu.
- Nenhum ângulo que ela não disse foi inventado.
- Nenhuma pergunta foi feita.
- A resposta coube em uma linha.

**Ao terminar:** se houve falha, contorno ou acerto que vale lembrar, registre em [`licoes.md`](./licoes.md) desta pasta, na mesma entrega (formato e estados em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md)).
