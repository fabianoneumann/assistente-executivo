---
titulo: "Dreams (Claude Managed Agents): consolidar a memória de um agente a partir de sessões passadas"
tipo: artigo
autor: "Anthropic"
url: "https://platform.claude.com/docs/en/managed-agents/dreams.md"
capturado_em: 2026-10-30
licenca: "Documentação da plataforma Claude: sem licença aberta; o rodapé de direitos não aparece na cópia em markdown lida, e ela é tratada como protegida, como a documentação do Claude Code (2026-10-29-claude-code-code-review-documentacao); entra só a ficha."
areas: [anthropic-claude, agent-engineering]
tags: [managed-agents, dreaming, memory-consolidation, agent-memory, continual-learning, research-preview]
---

Ficha de estudo, em palavras próprias, da página oficial "Dreams" da documentação da plataforma Claude (Managed Agents), lida em markdown em 2026-10-30. Recurso em **prévia de pesquisa**, com acesso por formulário. O anúncio está em [[2026-10-30-anthropic-managed-agents-dreaming-outcomes-anuncio]]. Lida.

## O problema

Os agentes dos Managed Agents escrevem nos seus **memory stores** enquanto trabalham, mas essas escritas são locais e incrementais: com muitas sessões, o store acumula "duplicates, contradictions, and stale entries".

## O que um dream faz

Lê um memory store existente junto com transcritos de sessões passadas e produz **um store novo, reorganizado**: duplicatas juntas, o que ficou velho ou foi contradito trocado pelo valor mais recente, e insights novos trazidos à tona. **O store de entrada nunca é modificado**, então dá para revisar o resultado e descartá-lo.

## Como funciona

- Tarefa **assíncrona**, criada por chamada de API (`POST /v1/dreams`), com duas entradas: o memory store (que o Claude confere, deduplica e reorganiza) e de 1 a 100 sessões (os transcritos que ele minera atrás de padrões e insights). Só com transcritos, sem store, cria-se antes um store vazio.
- O modelo escolhido roda a esteira do dream (na prévia, entre outros, Opus 5.5, Fable 5.1, Sonnet 5.5 e alguns modelos 4.x).
- **Instruções opcionais** (até 4.096 caracteres) orientam a síntese inteira: em que focar ("preferências de estilo de código"), o que preservar sem mudança, convenções para o store todo. A esteira é uma passada de síntese, não um editor de texto: ordem para mudar uma frase específica em geral não muda nada; edição pontual se faz pela API de memory stores, no store de saída.
- Exige dois cabeçalhos de beta: o dos Managed Agents e um próprio do dreaming.

## Acompanhar

Leva de minutos a algumas horas, conforme o número de transcritos. Estados: `pending` (na fila), `running` (processando; o uso de tokens vai subindo), `completed` (a saída é o store novo), `failed` (o store de saída fica com o que foi escrito até a falha), `canceled`. Durante a execução, o dream aponta para a sessão que roda a esteira, e dá para acompanhar os eventos ao vivo (o que ele lê e escreve); a sessão é arquivada, não apagada, no fim.

## Usar o resultado

Quando completa, o store de saída é um memory store comum: revisa-se pela API ou pelo Console e então **usa-se** (ligado às próximas sessões no lugar do de entrada ou junto) ou **descarta-se** (apagar ou arquivar). O dream nunca apaga nem muda as entradas; apagar uma entrada durante a execução faz o dream falhar.

## Cancelar, arquivar, listar, erros

Cancelar é imediato (o uso pode subir alguns segundos ainda); arquivar só depois de terminado, e não mexe no store de saída; listar devolve os não arquivados, do mais novo ao mais antigo. Erros possíveis: tempo esgotado, falha interna, limite de stores da organização, store de entrada grande demais, entrada apagada no meio.

## Custo e limites

Cobrado nas tarifas normais de token do modelo escolhido, proporcional ao número e ao tamanho das sessões; a doc recomenda começar com um lote pequeno e aumentar quando a qualidade da curadoria convencer. Até 100 sessões por dream. Sem retenção zero de dados: as sessões são recursos com estado, e os transcritos ficam até serem apagados.
