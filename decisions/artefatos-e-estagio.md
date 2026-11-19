# Artefatos e estágio de produção

Dois campos de frontmatter que declaram, para quem lê o repositório de fora (um painel, um script, outro agente), **o que uma área produz e em que ponto está cada peça em preparo**.

## `artefatos`: o que uma área produz

No manifesto da área (o frontmatter do `README.md` ou do arquivo principal dela), ao lado de `area` e `cadencia`:

```yaml
---
area: Conteúdo
artefatos:
  - pasta: "carousels/standalone/*"
    tipo: carrossel
  - pasta: "stories/*"
    tipo: stories
---
```

- `pasta` é glob relativo à área, sempre entre aspas: `*` no início de valor é alias em YAML e quebra o parse.
- **O item é o arquivo ou a pasta com data no nome** (`AAAA-MM-DD-…` ou `AAAA-MM-DD_…`), e a data é a de pronto. O que está na pasta sem data não é item. É assim que material de trabalho convive com a peça sem virar peça.
- `tipo` é vocabulário do repositório. Quem lê mostra ícone para os tipos que conhece e um genérico para o resto.

Coleção que já se declara por item, como `knowledge/sources/`, com `tipo` e `capturado_em` em cada arquivo, não precisa da entrada.

## `estagio`: onde está uma peça em preparo

Nas ideias de `marketing/social-media/ideas/` e nos rascunhos de série:

```yaml
---
estagio: pauta    # planejado | pauta | rascunho | pronto | publicado
---
```

- **Ausência significa incubando.** Ideia crua, hub de tema e lente de avaliação não recebem o campo: estar em `ideas/` já diz que é ideia, e nenhum dos três está em produção. O campo aparece quando a produção começa, em `pauta`, e é a skill `story-angle` que o grava.
- **`planejado`:** ideia com data reservada no calendário e apuração por fazer. Leva `data` junto. Marcar `pauta` mentiria, porque pauta é ângulo fechado pela `story-angle`, que troca o campo para `pauta` ao fechar o ângulo.
- **Outros valores** podem nascer com o processo (por exemplo `a-validar`, esperando a leitura de quem aprova; `medido`, leitura de desempenho registrada; `cancelado`, não será feito, com a nota do porquê). Quem lê o campo trata um valor desconhecido como estágio novo, não como erro.
- Hub não tem *um* estágio: as derivações dele têm, cada uma o seu, quando promovidas a arquivo próprio. Lente nunca vira peça.

## O que não é artefato

Registro de execução, material capturado e conteúdo recebido não entram: o log do que foi postado num dia, a transcrição de um vídeo, um depoimento. Artefato é o que foi **produzido e ficou pronto**.

## O homônimo

Quando o frontmatter leva o valor, a prosa que repetia o valor no corpo (um `**Status:**` com "ideia / rascunho") sai, e a prosa que tem nuance que o campo não expressa fica com outro rótulo (`**Nota:**`). Por quê: dois lugares para o mesmo valor divergem, e quem lê não sabe qual vale.
