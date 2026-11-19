---
titulo: "Agent Workflow Memory"
tipo: paper
autor: "Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig"
url: "https://arxiv.org/abs/2409.07429"
publicado_em: 2024-09-11
capturado_em: 2026-10-29
licenca: "CC BY-SA 4.0 (indicada na página do arXiv); share-alike"
areas: [agent-engineering]
tags: [agent-memory, workflow-induction, procedural-memory, web-agents, generalization, lessons-learned]
---

Ficha em palavras próprias; o texto integral (licença CC BY-SA 4.0, share-alike) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 (única, lida) em 11/09/2024. Código em https://github.com/zorazrw/agent-workflow-memory. Lido em 2026-10-29, na pesquisa sobre registro de lições.

## A pergunta

Agentes de navegação na web erram em tarefas longas e cada tarefa é resolvida do zero, sem aprender com sucessos e falhas anteriores. Pessoas resolvem bem tarefas complexas porque abstraem rotinas reaproveitáveis da experiência. O AWM (Agent Workflow Memory) induz essas rotinas, os **workflows**, a partir de trajetórias do agente e as põe na memória dele para guiar as tarefas seguintes.

## O que é um workflow

Um workflow tem duas partes (seção 2.2): uma **descrição** em linguagem natural do objetivo (um resumo da função, tirado das instruções ou escrito pelo modelo) e uma **sequência de passos**, cada um com três elementos: a descrição do estado do ambiente em linguagem natural ("o pedido {id} aparece"), o raciocínio do agente para escolher a ação, e a ação como programa executável (por exemplo, `click`, `fill`, `stop()`).

Duas escolhas de desenho importam (seção 2.3):

- **Granularidade de sub-rotina:** em vez de "comprar ração seca de gato na Amazon e entregar no meu endereço", o modelo é instruído a extrair a parte que se repete em várias tarefas, como "buscar um produto na Amazon".
- **Abstração dos valores:** o que é específico do exemplo vira variável ("ração seca de gato" vira `{product-name}`).

O prompt de indução (Apêndice A.1) pede para achar subconjuntos repetidos de ações entre tarefas, cada um como sub-rotina comum, sem workflows parecidos ou sobrepostos, com pelo menos dois passos e variáveis com nomes descritivos. A saída é cortada em workflows separados nas quebras de linha duplas.

## Como induz e usa

- **Offline:** quando há exemplos de treino de boa qualidade (anotados por pessoas ou sintetizados), todos os exemplos de um site entram concatenados num único prompt, o modelo induz o conjunto de workflows uma vez, e **todos** eles entram na memória do agente para **todas** as tarefas de teste.
- **Online, sem supervisão:** só existem as tarefas de teste, processadas em sequência. A cada tarefa, o agente tenta resolver; um **avaliador baseado em modelo** (de Pan et al., 2024) dá um rótulo binário de sucesso; se o avaliador diz sucesso, o agente induz workflows dessa trajetória e os **acrescenta** à memória, que passa a valer para a tarefa seguinte. A memória só cresce; o artigo não descreve edição nem poda de workflows.
- O AWM roda **por site**: os exemplos são agrupados pelo site e cada grupo tem sua memória, o que mantém a coleção pequena e relevante. A memória não passa por recuperação: todo o conjunto do site vai para o contexto.
- Workflows se compõem: o agente aprende cedo "achar um lugar pelo nome" e depois o usa como primeiro trecho de "obter o CEP de um lugar" (Fig. 6), num efeito de bola de neve.

## Como mediram

- **WebArena:** 812 tarefas em cinco sites (comércio eletrônico, administração de loja, fórum, GitLab, mapas), com avaliação pela execução. Só existe teste, então só o modo online. gpt-4 com temperatura 0. Comparação com BrowserGym (o melhor autônomo publicado, que usa HTML e árvore de acessibilidade; também rodado só com árvore de acessibilidade, a mesma entrada do AWM), AutoEval e SteP (que usa 14 workflows escritos por especialistas para o WebArena).
- **Mind2Web:** tarefas em vários sites e domínios, com testes em três distâncias do treino: mesma tarefa de outros exemplos dos mesmos sites (cross-task), sites novos do mesmo domínio (cross-website) e domínios novos (cross-domain). Métricas por passo (acurácia do elemento, F1 da ação, sucesso do passo) e por tarefa (todos os passos certos). Comparação com MindAct e Synapse, com gpt-3.5-turbo e gpt-4.

## Resultados

**WebArena (Tabela 1, taxa de sucesso %):** AWM 35,5; BrowserGym 23,5 (com HTML) e 15,0 (só árvore de acessibilidade); AutoEval 20,2; WebArena original 14,9; SteP, com workflows humanos, 33,0. São 12,0 pontos e **51,1% de aumento relativo** sobre o BrowserGym, e 7,6% relativo sobre o SteP na seção de resultados (a introdução diz 7,9%). O AWM melhora todos os cinco sites, de 11,8 a 30,7 pontos, e usa menos passos: 5,9 por tarefa contra 7,9 do BrowserGym só com árvore e 46,7 do AutoEval.

- **Aprende com pouco (Fig. 5):** no subconjunto de mapas, a curva sobe rápido nos primeiros cerca de 40 exemplos e depois estabiliza; a distância para o agente sem memória chega a 22,5 pontos depois de algumas dezenas de exemplos (Fig. 1).
- **Entre modelos de tarefa diferentes (Tabela 2):** como o WebArena gera várias tarefas de um mesmo modelo, os autores montaram um subconjunto com uma tarefa por modelo; o AWM ainda lidera, 33,2 contra 20,5 do BrowserGym só com árvore, 23,2 do AutoEval e 32,1 do SteP.

**Mind2Web offline, cross-task (Tabela 3):** com gpt-4, sucesso do passo 45,1 contra 36,2 do MindAct (**24,6% relativo**) e sucesso da tarefa 4,8 contra 2,0; com gpt-3.5, 34,6 contra 30,6 do Synapse, que recupera exemplos inteiros. O ganho vem sobretudo da escolha do elemento certo (5,0 a 9,0 pontos de acurácia). Para os autores, o exemplo concreto e inteiro enviesa o agente a escolher elementos parecidos com os do exemplo, e o workflow abstrato não. O F1 da ação fica um pouco **abaixo** do MindAct (57,3 contra 60,6): o workflow às vezes empurra ações que não cabem no estado da página, e o agente tem dificuldade em saber onde se desviar dele.

**O ganho conforme a distância entre treino e teste (Tabela 4, gpt-4, sucesso do passo):**

| | Cross-task | Cross-website | Cross-domain |
|---|---|---|---|
| MindAct | 36,2 | 30,1 | 18,6 |
| AWM offline | 45,1 | 33,7 | 32,6 |
| AWM online | 43,6 | 33,9 | 35,5 |

- O ganho sobre o MindAct é de 7,4 a 8,9 pontos no cross-task, 3,6 a 3,8 no cross-website e 14,0 a 16,9 no cross-domain; o resumo do artigo condensa isso como "de 8,9 a 14,0 pontos absolutos à medida que a distância cresce".
- O que cresce de forma regular com a distância é a vantagem do **online sobre o offline**: −1,5 no cross-task, +0,2 no cross-website e +2,9 no cross-domain. O online induz só das tarefas de teste, então não sofre com treino de outro domínio; o offline ganha quando há exemplos de treino de boa qualidade e da mesma distribuição.
- No cross-task os dois empatam por razões opostas: o online induz de trajetórias que o avaliador julgou certas mas nem sempre são, e workflows errados pioram o agente; o offline sofre quando treino e teste do mesmo site pedem coisas diferentes (comprar na Amazon no treino, candidatar-se a vaga na Amazon no teste).
- O sucesso por tarefa continua baixo em todos: no cross-domain, 1,0 do MindAct, 0,7 do offline e 1,7 do online.

**Representação do workflow (seção 4):**

- **Indução por regra contra por modelo:** a por regra deduplica experiências pela sequência de ações e remove passos inválidos, sem abstrair contexto nem cortar em sub-rotinas. No WebArena empata (35,6 contra 35,5), com o modelo usando menos passos (5,9 contra 6,3); no Mind2Web, o modelo ganha 1,7 ponto no sucesso do passo (45,1 contra 43,4) e a tarefa sobe de 2,0 para 4,8 (Tabelas 5 e 6).
- **Texto contra código:** verbalizar as ações ("clique no botão de envio") dá resultado parecido (passo 45,4 contra 45,1; tarefa 3,6 contra 4,8) (Tabela 7).
- **Descrever o estado em linguagem natural é melhor que colar HTML:** 34,6 só com descrição, 33,8 só com HTML filtrado, 32,9 com os dois; o HTML filtrado perde o elemento certo 47% das vezes e alonga o contexto (Tabela 8, gpt-3.5).

**Workflow como ação (seção 5):** transformar cada workflow numa função que o agente chama (como um atalho) melhora o passo em 1,3 ponto (46,4), mas o agente chama essas ações em só 18,5% das tarefas, e a ação fixa quebra quando a página muda no meio (por exemplo, a lista de aeroportos que aparece ao digitar a cidade). O texto diz que o sucesso da tarefa fica igual, "3,2", mas a Tabela 9 mostra 3,6 contra 4,8.

**Offline mais online juntos (Apêndice C, Tabela 11):** fica entre os dois; os workflows offline parecem atrapalhar a qualidade e o uso dos online, sem efeito aditivo.

**Qualidade dos workflows induzidos (Apêndice A.3, Tabela 10):** cerca de 7,3 a 7,4 workflows por site; no WebArena, usados por 94% das tarefas de teste, com sobreposição de função de 0,08; no Mind2Web, uso de 91%, sobreposição de 0,20 e cobertura de só 40% dos passos de teste.

## Limites declarados

O artigo não tem seção de limites; as ressalvas aparecem ao longo do texto: o modo online induz de trajetórias julgadas certas por um avaliador automático, que podem estar erradas e gerar workflows errados; o agente tem dificuldade em se desviar do workflow quando ele não se aplica ao estado da página; a variante de workflow como ação é rígida diante de páginas dinâmicas e os agentes resistem a usar ações novas; misturar workflows offline e online não soma.
