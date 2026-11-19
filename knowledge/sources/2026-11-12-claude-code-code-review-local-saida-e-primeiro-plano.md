---
titulo: "Review locally with /code-review: por onde saem os achados, como rodar em primeiro plano e o pedido do nível baixo"
tipo: artigo
autor: "Anthropic"
url: "https://code.claude.com/docs/en/code-review-local.md"
capturado_em: 2026-11-12
licenca: "Documentação: todos os direitos reservados (texto da página Legal and compliance da documentação, registrado em 2026-10-29-claude-code-code-review-documentacao: '© Anthropic PBC. All rights reserved. Use is subject to applicable Anthropic Terms of Service.'); entra só a nota de fato. O pedido do nível baixo é texto embutido no Claude Code (o repositório anthropics/claude-code é 'All rights reserved'); entra só a nota de fato, com uma citação curta."
areas: [agent-engineering, anthropic-claude]
tags: [code-review, effort-levels, findings-output, background-tasks]
---

# /code-review local: por onde saem os achados, primeiro plano e o pedido do nível baixo

Nota de fato: tabelas de fatos, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a documentação e o pedido embutido são protegidos. Complementa [[2026-10-29-claude-code-code-review-documentacao]], que é de 29/10 e não fala do canal de saída nem do primeiro plano.

**Proveniência.** Duas partes, de origens diferentes.

1. **A documentação:** página "Review locally with /code-review", https://code.claude.com/docs/en/code-review-local.md, baixada com curl em 2026-11-12, sem data na página, lida inteira. A página do serviço gerenciado, https://code.claude.com/docs/en/code-review.md, que a skill `review` manda conferir, foi lida inteira no mesmo dia e não fala de `ReportFindings`, de `-p` nem de primeiro plano: o assunto está na página local, para a qual ela remete.
2. O mesmo pedido, com a proibição da ferramenta e o `(none)`, está na primeira mensagem de outros cinco registros da mesma pasta (`agent-a817e4b30d9b570ae` e `agent-a7397443cf3a44342`, 07/11; `agent-ae0c2c6281ca5a57c`, 08/11; `agent-a13465e81d8f57101` e `agent-ad22e5ca4cc59bb0c`, 11/11), e nos cinco a resposta final foi `(none)`; no de 12/11, um achado.

**Conferência lado a lado** (2026-11-12, na escrita, pela régua do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato fica fora. Corpo: 9 frases de prosa (uma em "Em uma frase", três em "O que a fonte recomenda", cinco na lacuna); as células das tabelas são fatos em lista, separados por ponto e vírgula e sem verbo conjugado, e ficam fora da conta (a primeira versão das tabelas trazia 17 células em frase, quase todas traduzindo uma frase da página ou do pedido, e foi refeita assim). As frases de "O que a fonte recomenda" juntam lugares diferentes da página (a saída, o primeiro plano, os níveis) ou do pedido (o topo e as regras de saída), em outra ordem; a lacuna diz o que falta. Resultado: 0 das 9 unidades seguem a fonte. As três citações estão à parte. O `parafrase.py` rodou contra a cópia de trabalho da página e saiu com o código 3 (ficha em português, fonte em inglês, tradução fora da medida): a conta acima é a conferência.

## Em uma frase

A página diz que o `/code-review` entrega os achados como texto no terminal e no `-p`, e pela ferramenta `ReportFindings` quando uma aplicação hospedeira pede a lista; o pedido que o nível baixo dá ao subagente lê só o diff numa chamada, proíbe essa ferramenta e manda responder `(none)` quando nada se qualifica.

## Por onde saem os achados (documentação)

| Onde a revisão roda | Como os achados saem |
|---|---|
| sessão de terminal (subagente bifurcado) | texto na resposta |
| `-p` com saída em texto ou JSON | texto na resposta |
| aplicação hospedeira que pede a lista (exemplo da página: o app desktop) | ferramenta `ReportFindings`, como lista de achados |

| Lista de achados do host | Fato |
|---|---|
| Campos de cada entrada | lugar no arquivo; resumo de uma frase; etiqueta de categoria (como `correctness`), quando houver |
| Níveis em que o pedido do host vale | todos |
| Correção feita depois, na mesma sessão | novo relato; marca por achado: corrigido, pulado ou sem mudança necessária |
| Limite de achados quando a saída é pela ferramenta (dito junto do `--max-findings`) | 32 |
| `--max-findings` passado num `-p` | fora da memória das próximas revisões |

## Primeiro e segundo plano (documentação)

| Situação | Fato |
|---|---|
| Padrão no terminal | segundo plano; subagente com contexto próprio; achados na conversa ao fim |
| `-p` ou Agent SDK | primeiro plano; achados na resposta; exceção: `ultra`, sem espera pela nuvem |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` | primeiro plano; outros recursos de segundo plano também desligados |
| `/code-review` de novo com uma revisão anterior ainda em andamento | a nova em primeiro plano |
| `--fix` em segundo plano | edições fora dos checkpoints da sessão; `/rewind` sem efeito nelas; desfazer pelo git |
| `--fix` em primeiro plano | edições no turno da pessoa; `/rewind` com efeito |

## Níveis e instruções (documentação)

| Item | Fato |
|---|---|
| `low` | só os achados de maior confiança; menos falsos positivos |
| `medium` a `max` | cobertura mais larga |
| Sem nível digitado | o último de `low` a `max` digitado, mesmo de sessão anterior, com aviso |
| Nível passado num `-p` | nível lembrado intacto |
| `ultra` | fora do nível lembrado (nem lido nem gravado) |
| Nunca digitado | o esforço atual da sessão |
| Instruções seguidas | `CLAUDE.md`, inclusive no `-p` |
| `REVIEW.md` | não lido (é do serviço gerenciado) |

## O pedido do nível baixo (registro da sessão)

| Item | Fato |
|---|---|
| Resumo no topo do pedido | esforço baixo; uma passada pelo diff; sem verificação; até 4 achados |
| Leitura | 1 chamada de ferramenta: o diff unificado (contra o upstream e o `HEAD`, ou o do alvo passado) |
| Fora da leitura | subagentes; leitura de arquivo inteiro; trechos de teste e de fixture |
| O que marca | bug de execução visível só no trecho do diff; helper duplicado visível no diff; código morto deixado pelo diff |
| O que não marca | estilo; nome; desempenho; teste faltando; tudo fora do trecho |
| Forma de cada achado | 1 linha: `caminho:linha`, problema, falha concreta; do mais grave ao menos |
| Nada se qualifica | `(none)`, exato |
| `ReportFindings` | proibido, mesmo disponível |
| Respostas nos seis registros lidos | `(none)` em cinco (07, 08 e 11/11); um achado em 12/11 |

## O que a fonte recomenda

Para quem automatiza, o `-p` resolve duas coisas de uma vez: põe os achados no texto da resposta e espera a revisão acabar, enquanto no terminal eles chegam depois, de um subagente em segundo plano. O nível escolhido troca cobertura por confiança, mas não troca o canal: quem decide o canal é o pedido do host. O pedido do baixo mostra como a troca se faz no nível de menos cobertura: uma leitura do diff, nenhuma conferência, no máximo quatro achados e `(none)` quando nada passa.

## Citações

- Documentação: "A host request applies at every effort level."
- Pedido do baixo: "If nothing qualifies, output exactly `(none)`."
- Pedido do baixo: "Do not call the ReportFindings tool even if it is available."

## Lacuna

A página não fala de resposta vazia nem de rodar de novo depois de uma; o único "rodar de novo" dela é o que põe a nova revisão em primeiro plano enquanto a anterior roda. Não diz como o pedido de cada nível trata a ferramenta quando o host pede a lista. Não diz qual é o limite usual de achados fora da ferramenta. Não mostra o pedido dos outros níveis. O pedido do baixo foi lido em seis execuções de um só projeto, todas como subagente em segundo plano.
