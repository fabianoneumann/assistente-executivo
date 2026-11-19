---
titulo: "Experiential Reflective Learning for Self-Improving LLM Agents"
tipo: paper
autor: "Marc-Antoine Allard, Arnaud Teinturier, Victor Xing, Gautier Viaud"
url: "https://arxiv.org/abs/2603.24639"
publicado_em: 2026-03-25
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [agent-memory, lessons-learned, experiential-learning, self-reflection, heuristic-retrieval, llm-reranking, retrieval]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 25/03/2026, v2 (lida) em 31/03/2026; o comentário do arXiv diz "publicado como artigo de conferência no workshop MemAgents da ICLR 2026". Trabalho do laboratório conjunto da ILLUIN Technology com o MICS da CentraleSupélec (agradecimentos). Lido em 2026-10-29, na pesquisa sobre registro de lições.

## A pergunta

Agentes de modelo de linguagem enfrentam cada tarefa do zero, sem aproveitar a experiência acumulada, e se adaptam mal a ambientes com ferramentas e convenções próprias. Ajuste fino resolveria, mas é caro, impossível em modelo fechado e não aprende de forma contínua. O ERL (Experiential Reflective Learning) quer que o agente melhore refletindo sobre cada tarefa que já fez, numa tentativa só, e reaproveitando as lições nas tarefas seguintes.

O ponto de partida é a crítica a dois antecessores (seção 1): o **ExpeL** compara trajetórias de sucesso e falha, usa o Reflexion para repetir cada tarefa até acertar e concatena **todos** os insights em **todo** prompt, sem olhar a relevância, o que escala mal; o **AutoGuide** cria diretrizes por contexto contrastando pares de trajetórias com resultados diferentes, mas identifica o contexto e recupera diretrizes **a cada turno** do agente, com custo alto, e não dá orientação nenhuma quando o estado atual não casa com nenhum contexto guardado. Os dois exigem várias execuções da mesma tarefa para formar pares, o que não existe quando a tarefa real não pode ser repetida.

## Como funciona

**1. Geração de heurísticas (seção 2 e prompt da Fig. 8).** O ambiente informa ao fim de cada tarefa se ela deu certo ou errado. Depois de cada tarefa, o agente reflete sobre a experiência (descrição da tarefa, trajetória com raciocínio, chamadas de ferramenta e saídas, e o resultado) num "post-mortem":

- se falhou, aponta o **ponto de quebra** (onde a lógica falhou ou a ferramenta foi mal usada) e escreve uma **regra de correção** que evite essa classe de erro; o prompt dá o exemplo ruim ("devo tomar mais cuidado com arquivos") e o bom ("quando o caminho do arquivo é desconhecido, usar `ls -R` ou `find` antes de `read_file`");
- se deu certo, identifica a **jogada vencedora** e escreve uma **boa prática** para reforçá-la.

A heurística tem formato fixo: (1) **análise** da causa do sucesso ou da falha; (2) **diretriz aprendida**, curta e no imperativo, com **gatilho** ("quando eu encontrar a situação X") e **ação** ("devo fazer Y explicitamente"). Exemplo do artigo: ao mandar e-mail para participantes de um evento do calendário, resolver antes os nomes em endereços pela ferramenta de Contatos. As heurísticas vão para um repositório persistente, junto com a descrição da tarefa e o resultado. Gerador: gpt-5-mini, o mesmo modelo do agente.

**2. Recuperação com nota de relevância dada por um modelo (seção 2, Apêndice C.2 e prompt da Fig. 9).** Diante de uma tarefa nova:

- Um modelo recebe a descrição da tarefa e **a lista inteira de heurísticas**, cada uma com identificador, descrição da tarefa de origem, resultado (sucesso ou falha) e texto.
- Ele **decompõe a tarefa em subtarefas e passos de ação prováveis** e escolhe as **k heurísticas mais relevantes** segundo três critérios: semelhança entre a tarefa de origem e a atual, **diversidade** de experiências (cobrir vários tipos de lição) e **conteúdo informativo** (preferir as que têm diretriz detalhada e acionável).
- A saída é um JSON com os k identificadores escolhidos; para cada um, **primeiro uma justificativa de uma ou duas frases, depois uma nota de 0 a 100**. A seção 2 descreve isso como dar nota de relevância a cada heurística guardada; o prompt pede a nota e a justificativa para as k escolhidas.
- O modelo de recuperação é o **GPT-5.2**, mais forte que o agente. O prompt considera não só a semelhança de tarefa, mas os padrões de erro e as lições escritas em cada heurística. A versão do prompt foi escolhida por **comparação humana** com variantes de rubrica mais detalhada e outras escalas de nota.
- As k heurísticas (k = 20 por padrão) entram **no prompt de sistema uma vez, antes da execução**, sem mudar o laço ReAct, para o agente receber conselho da tarefa em vez de afogar no repositório inteiro. No exemplo do Apêndice F, o agente cita a diretriz durante a execução e a aplica a uma tarefa estruturalmente parecida (substituir eventos em vez de reagendar).

## Como mediram

- **Gaia2** (na plataforma Agents Research Environments, ARE): ambiente de celular simulado com 12 aplicativos e 101 ferramentas; divisões **Search** (busca de informação) e **Execution** (execução em vários passos). O Gaia2 é organizado em **universos** com as mesmas ferramentas e dados totalmente diferentes (contatos, arquivos, agenda), o que evita contaminação: as heurísticas são acumuladas em 8 universos (112 tarefas de execução e 132 de busca) e o teste é em 2 universos separados (48 e 28 tarefas), cada um rodado 3 vezes.
- Agente base: o ReAct padrão do Gaia2, com gpt-5-mini; o juiz do ARE também é gpt-5-mini.
- Comparações: ReAct puro; few-shot com trajetórias brutas no prompt; ExpeL (reimplementado com Reflexion até 3 tentativas, lotes de 3 sucessos e 3 exemplos por embedding); AutoGuide (Reflexion até 3 tentativas, 3 diretrizes recuperadas depois de cada turno).
- Métricas: taxa de sucesso; **pass@3** (acertou ao menos uma vez em 3 execuções, mede capacidade) e **pass^3** (acertou nas 3, mede confiabilidade).

## Resultados

**Taxa de sucesso no Gaia2 (Fig. 2, %):**

| Método | Execution | Search | Geral |
|---|---|---|---|
| ReAct (base) | 43,1 | 53,6 | 48,3 |
| Few-shot com trajetórias | 41,7 | 51,2 | 46,4 |
| ExpeL | 45,8 | 56,0 | 50,9 |
| AutoGuide | 39,6 | 61,9 | 50,8 |
| **ERL** | 51,4 | 60,7 | **56,1** |
| Ablação: sem recuperação | 44,4 | 63,1 | 53,8 |
| Ablação: recuperação por embeddings | 50,7 | 56,0 | 53,3 |
| Ablação: só heurísticas de falha | 50,0 | 67,9 | 58,9 |
| Ablação: só heurísticas de sucesso | 52,1 | 47,6 | 49,9 |

- **ERL 56,1%:** +7,8 pontos sobre o ReAct e +5,2 sobre o ExpeL, o melhor antecessor; +8,3 em Execution e +7,1 em Search. O AutoGuide é forte em Search (61,9) e fica abaixo da base em Execution (39,6).
- **Confiabilidade:** o ganho maior é no pass^3 (+8,3 em Execution, +10,6 em Search); o pass@3 sobe pouco, ou seja, o ERL torna mais estável o que o agente já conseguia, mais do que resolve tarefas novas.
- **Heurística generaliza melhor que trajetória:** pôr trajetórias brutas no prompt piora (−1,9 contra a base). Com o mesmo número de experiências no contexto, heurísticas ganham +5,5 em Execution com cerca de 20 cenários e +23,8 em Search com 40, onde as trajetórias já degradam pelo contexto longo (Apêndice C.1).

**Recuperação por modelo contra embeddings (conferido: 56,1% contra 53,3%):**

- Escolher heurísticas ao acaso dá curva não monotônica: melhora até cerca de 40 a 60 heurísticas e piora com excesso (Fig. 4); a melhor configuração aleatória chega a 53,8%. Na tabela da Fig. 2 a mesma cifra aparece na linha "sem recuperação".
- A recuperação por embeddings (Qwen3-Embedding-0,6B, similaridade de cosseno entre a tarefa nova e as de treino) traz tarefas que usam as mesmas ferramentas (uma tarefa de agenda puxa todas as de agenda), mas não prioriza heurísticas sobre padrões de erro parecidos; o melhor resultado é 53,3% com k = 20.
- A recuperação por modelo vence os embeddings na maioria dos valores de k, sobretudo em Search, e chega a 56,1% com k = 20 (Tabela 3). Conclusão dos autores: a qualidade da recuperação importa mais que a quantidade de heurísticas.

| k | Embeddings: Exec / Search / Geral | Modelo: Exec / Search / Geral |
|---|---|---|
| 1 | 43,1 / 57,1 / 50,1 | 45,1 / 53,6 / 49,4 |
| 3 | 43,8 / 57,1 / 50,5 | 47,2 / 58,3 / 52,8 |
| 5 | 51,4 / 47,6 / 49,5 | 49,3 / 58,3 / 53,8 |
| 10 | 45,8 / 56,0 / 50,9 | 51,4 / 54,8 / 53,1 |
| 20 | 50,7 / 56,0 / 53,3 | 51,4 / 60,7 / 56,1 |

**Falha contra sucesso:** heurísticas só de falha dão o maior geral (58,9), puxado por Search (+14,3 sobre a base), porque funcionam como restrições negativas que cortam estratégias ruins; heurísticas só de sucesso ajudam mais em Execution (+9,0), porque reforçam sequências de ação que funcionaram, e derrubam Search. Como a distribuição real de tarefas é desconhecida, os autores recomendam recuperar das duas fontes.

**Sem o sinal de resultado (Apêndice C.2):** se o ambiente não diz se a tarefa deu certo, o agente julga o próprio resultado e acerta só 70% das vezes; o ERL cai para 51,2% (−4,8), ainda acima da base.

**ERL iterativo (Apêndice E):** recuperar do repositório enquanto ele cresce, em lotes, melhora as tarefas de origem mas piora o teste (50,7%, −5,4 contra o ERL padrão; 54,3% com só falhas). Hipóteses dos autores: com orientação, o agente erra menos e de forma mais estreita, e as heurísticas perdem a variedade de erros ingênuos que tarefas novas provocam; e heurísticas de trajetórias já guiadas transferem pior.

**τ²-bench (Apêndice A, atendimento ao cliente com usuário simulado):** sucesso geral 38,0 contra 36,7; ganha em Airline e Retail, mas cai em Telecom (28,3 contra 30,0, pass^3 vai a zero). Hipóteses: tarefas de Telecom são combinações de subtarefas, o que reduz a chance de uma heurística casar, e o usuário tem ferramentas e persona próprias, o que torna a interação menos previsível.

**Custo (Apêndice D):** as heurísticas recuperadas (cerca de 20 mil tokens) somam-se ao prompt de sistema (cerca de 12 mil) em todo turno; os tokens de entrada na execução sobem 85%, mas com cache o custo da execução sobe 15%; com geração e recuperação, o custo total de API sobe 40%. A latência não foi medida; a chamada extra de recuperação pesa pouco em tarefas de dezenas de turnos e pode pesar em tarefas curtas.

## Limites declarados

- Repositório grande: resolver diretrizes conflitantes e manter a qualidade da recuperação ficam para trabalho futuro; a recuperação por modelo fica ineficiente acima de k = 20, e os autores sugerem duas etapas (embeddings para pré-selecionar, modelo para reordenar).
- Heurísticas ocupam contexto; representações mais compactas ficam para trabalho futuro.
- Depende de um sinal de resultado confiável (ver a queda sem ele).
- Não captura bem estratégias de coordenação com o usuário (Telecom).
- O repositório só cresce: o artigo não descreve edição, voto ou poda de heurísticas.
