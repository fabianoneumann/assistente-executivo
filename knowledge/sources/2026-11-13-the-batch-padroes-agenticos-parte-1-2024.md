---
titulo: "Agentic Design Patterns Part 1: Four AI agent strategies that improve GPT-4 and GPT-3.5 performance"
tipo: artigo
autor: "Andrew Ng"   # a página não traz o sobrenome: a carta assina "Andrew" e está na seção "Letters" do The Batch (trilha de navegação da página), que o menu do topo chama "Andrew's Letter" e o submenu do The Batch, "Andrew's Letters"; o metadado de autor da página (JSON-LD) traz "Analytics DeepLearning.AI"
url: "https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/"
publicado_em: 2024-03-20   # a página mostra "Published" e "Mar 20, 2024"; meta article:published_time e JSON-LD datePublished 2024-03-20T14:45:48-07:00, sem modificação posterior
capturado_em: 2026-11-13
areas: [agent-engineering]
entrada: pesquisa
tags: [andrew-ng, the-batch, agentic-workflows, agentic-design-patterns, reflection, tool-use, planning, multi-agent, humaneval, code-generation, zero-shot]
licenca: "sem licença aberta na página; nota de fato em palavras próprias, com citações curtas exatas"
---

# The Batch, padrões agênticos, parte 1: as quatro categorias e o gráfico do HumanEval

Nota de fato (`knowledge/sources/README.md`, item 2): carta curta, mas de conteúdo técnico (um conjunto de medidas num gráfico e uma classificação de padrões de projeto), por isso tabelas de fatos e não ficha de prosa. Não há integral: a página é protegida.

**Proveniência.** Carta semanal do The Batch, da DeepLearning.AI, seção "Letters", assinada "Andrew", em https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/. HTML baixado em 2026-11-13, com o texto do bloco principal extraído para a cópia de trabalho e lido no texto bruto em 2026-11-13. A página marca o tempo de leitura em 2 minutos. Título conferido no HTML: o cabeçalho é "Agentic Design Patterns Part 1" com o subtítulo do campo `titulo`, e o `alt` da imagem principal junta os dois. Cobertura: o texto inteiro da carta, de "Dear friends" à assinatura, e os títulos dos quatro links do rodapé para as partes 2 a 5 (nenhum aberto, nem o link do Devin, que aponta para a página da Cognition). O gráfico foi lido como imagem, na cópia `batch-part1-humaneval.jpg` (1200×676 pixels; o HTML da carta tem uma só imagem de conteúdo, `content/images/2024/03/unnamed--55--2.jpg`, e a legenda do gráfico está desenhada dentro da imagem, não no texto da página.

**Conferência lado a lado** (2026-11-13, pela régua do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (número, nome, cor, rótulo curto) fica fora, e as três citações literais estão à parte. Resultado: 6 de 19 unidades seguem uma frase da fonte (detalhe no fim da ficha); a maior sequência na ordem da fonte é de 2 unidades seguidas. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: o script não mede tradução, e a conferência é esta conta), com 0 de 33 unidades coladas e nenhum trecho.

## Em uma frase

Primeira de uma série de cinco cartas sobre padrões de projeto de agentes: o autor aposta que os fluxos de agente vão puxar um grande avanço da IA neste ano, talvez maior que o da próxima geração de modelos, mostra num gráfico de HumanEval o salto que o laço de agente dá a um modelo fraco e propõe quatro categorias para organizar a área.

## Os números do texto

| Item | Valor |
|---|---|
| Benchmark | HumanEval, de geração de código |
| Quem juntou os números | a equipe do autor, a partir de resultados de vários grupos de pesquisa |
| GPT-3.5, zero-shot | 48,1% de acerto |
| GPT-4, zero-shot | 67,0% |
| GPT-3.5 dentro de um laço de agente | até 95,1% |
| Comparação que a carta faz | o ganho de trocar o GPT-3.5 pelo GPT-4 é pequeno perto do ganho do laço |
| Contexto citado logo antes dos números | a demonstração do Devin, muito comentada nas redes; a carta não diz que ela motivou a análise |
| Quem já usa as quatro categorias | a AI Fund, equipe do autor, em muitas aplicações |
| Partes da série listadas no rodapé | 2, reflexão; 3, uso de ferramentas; 4, planejamento; 5, colaboração multiagente |

## O gráfico (lido da imagem)

| Elemento | Fato |
|---|---|
| Título | "GPT-3.5 and GPT-4 performance using zero-shot and agent workflows" |
| Eixo | "Human Eval", de 40 a 100, marcas de 5 em 5; GPT-3.5 acima do eixo, GPT-4 abaixo |
| Legenda de cores | verde, zero-shot; vermelho, reflexão; verde-água, uso de ferramentas; laranja, planejamento; azul-escuro, multiagente |
| Marcadores | círculos vazados, com o nome do método ao lado; nenhum valor escrito em número |
| Legenda abaixo do gráfico | desempenho do GPT-3.5 e do GPT-4 em zero-shot no HumanEval, junto de algoritmos com fluxo de agente sobre um dos dois |
| Créditos na legenda | Joaquin Dominguez e John Santerre, pela ajuda na análise |

Posição de cada círculo: o centro medido em pixels contra as marcas do eixo, arredondado; a precisão da leitura é de cerca de um ponto (o zero-shot do GPT-3.5 sai em 48,8 na medida, e o texto dá 48,1).

| Método (rótulo no gráfico) | Modelo | Cor e categoria da legenda | Posição no eixo |
|---|---|---|---|
| zero-shot | GPT-3.5 | verde, zero-shot | cerca de 49 |
| Intervenor | GPT-3.5 | azul-escuro, multiagente | cerca de 75 |
| ANPL | GPT-3.5 | verde-água, uso de ferramentas | cerca de 75 |
| Language Agent Tree Search | GPT-3.5 | laranja, planejamento | cerca de 83 |
| LDB + Reflexion | GPT-3.5 | verde-água, uso de ferramentas | cerca de 95 |
| zero-shot | GPT-4 | verde, zero-shot | cerca de 67 |
| CodeT | GPT-4 | verde-água, uso de ferramentas | cerca de 85 |
| MetaGPT | GPT-4 | azul-escuro, multiagente | cerca de 85 |
| ANPL | GPT-4 | verde-água, uso de ferramentas | cerca de 86 |
| Reflexion | GPT-4 | vermelho, reflexão | cerca de 92 |
| Language Agent Tree Search | GPT-4 | laranja, planejamento | cerca de 95 |
| Agent Coder | GPT-4 | azul-escuro, multiagente | cerca de 97 |

## As quatro categorias

| Categoria | De onde vem a melhora da resposta | Exemplos que a carta dá |
|---|---|---|
| Reflexão | da crítica do modelo à própria saída | — |
| Uso de ferramentas | de funções externas que o modelo chama | busca na web; execução de código; qualquer outra função |
| Planejamento | de um roteiro de etapas traçado e seguido pelo modelo | esboço do ensaio, pesquisa online, rascunho |
| Colaboração multiagente | do debate entre agentes que repartem a tarefa | — |

| Contraste da carta | Fato |
|---|---|
| Modo de uso dominante hoje | zero-shot, saída única sem revisão |
| Exemplo de fluxo de agente para um texto | esboço, decidir se precisa buscar na web, rascunho, leitura crítica do rascunho, revisão |

## O que a fonte recomenda

O pedido da carta a quem trabalha com IA é olhar para os fluxos de agente, com o HumanEval como prova: pôr um modelo mais fraco num processo iterativo rendeu mais que trocar de modelo. Para atravessar a profusão de ferramentas abertas e artigos sobre agentes, as quatro categorias servem de mapa, que as cartas seguintes detalham, cada uma com leituras sugeridas.

## Citações

- "I think AI agent workflows will drive massive AI progress this year — perhaps even more than the next generation of foundation models." (a frase de abertura da carta)
- "Indeed, wrapped in an agent loop, GPT-3.5 achieves up to 95.1%." (o parágrafo dos números do HumanEval)
- "typing straight through with no backspacing allowed" (a analogia do zero-shot, no segundo parágrafo)

## Lacuna

- O texto não liga o 95,1% a um método nem a um grupo de pesquisa, e o gráfico não traz valores em número.
- Nem a carta nem o gráfico nomeiam os artigos de onde vem cada ponto, as versões do GPT-3.5 e do GPT-4, a data das medidas ou a métrica exata do HumanEval (quantas tentativas por problema).
- A carta não diz por que cada método recebeu a sua categoria; LDB + Reflexion aparece com a cor de uso de ferramentas.
- Não diz quais aplicações da AI Fund usam as categorias, nem com que resultado.

## Detalhe da conferência lado a lado

Total de 19 unidades: 1 frase em "Em uma frase", 1 na nota de leitura do gráfico, 2 em "O que a fonte recomenda", 4 na lacuna e 11 células com texto corrido (4 em "Os números do texto", 2 na tabela de elementos do gráfico, 4 na coluna "De onde vem a melhora" e a do exemplo de fluxo). Seguem uma frase da fonte 6: as células de quem juntou os números, da comparação do ganho, do Devin e da AI Fund (cada uma traduz o miolo de uma frase da carta), a célula da legenda abaixo do gráfico (traduz a legenda desenhada na imagem) e a do exemplo de fluxo (funde os cinco passos da lista da carta, na ordem dela). A maior sequência é de 2 (quem juntou e comparação, que andam para a frente na carta; o Devin volta ao começo do parágrafo e quebra a sequência). As quatro células de "De onde vem a melhora" respondem a outra pergunta que a da definição da fonte e não a traduzem; as frases de "Em uma frase" e de "O que a fonte recomenda" juntam lugares diferentes da carta (abertura, números, parágrafo da classificação, anúncio da carta seguinte).
