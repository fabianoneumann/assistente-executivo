# Ideias

A incubadora das peças: um arquivo por tema, da ideia crua à pauta. A ideia entra aqui para não se perder, sem pesquisa e sem ângulo, pela skill `idea-capture`; quando alguém quer desenvolvê-la, a skill `story-angle` apura e escreve a pauta no próprio arquivo; quando ela vira peça, a `piece-creation` parte daqui.

## Os estágios de um arquivo

- **Ideia crua:** o que a pessoa disse, preservado, sem campo `estagio` no frontmatter. A linha de abertura é `**Nota:** ideia crua registrada em AAAA-MM-DD.`
- **Pauta:** o ângulo fechado pela `story-angle`, com `estagio: pauta` no frontmatter e os ângulos não escolhidos na fila de derivações. A síntese da apuração fica em `knowledge/`; a pauta aponta para ela e nunca copia número dela (`decisions/apuracao-e-pauta.md`).
- **Hub de tema:** depois que a ideia vira peça publicada, o arquivo encolhe para o status e o link da peça, sem duplicar o rascunho, e acumula as derivações ("Derivações / ângulos futuros"). Uma derivação ganha arquivo próprio só quando alguém vai trabalhá-la.

## O formato da ideia crua

O nome do arquivo é o tema em kebab-case, sem acentos (`ia-e-energia.md`); o texto é em português normal. Seção sem conteúdo não entra.

```markdown
# <Tema, em uma frase>

**Nota:** ideia crua registrada em AAAA-MM-DD.

## Tema
<o território, amplo, uma a três linhas>

## A ideia
<o que a pessoa disse, nas palavras dela>

## Gatilho
<o que ela estava vendo, lendo ou fazendo quando a ideia veio, só se ela disse>

## Ângulos-hipótese
<só os que ela trouxe, marcados como hipótese; sem eles, a seção não entra>
```

**Arquivo novo ou derivação?** Antes de escrever, olhe os nomes dos arquivos daqui e, nos candidatos plausíveis, a seção `## Tema`. Tema novo é arquivo novo; só vai como item em "Derivações / ângulos futuros" de um hub a ideia do mesmo eixo, com conexão direta e óbvia. Na dúvida, arquivo novo: juntar dois arquivos depois é fácil, e a ideia enterrada no hub errado some.
