---
titulo: "ExpeL: LLM Agents Are Experiential Learners"
tipo: paper
autor: "Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, Gao Huang"
url: "https://arxiv.org/abs/2308.10144"
publicado_em: 2023-08-20
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [agent-memory, lessons-learned, experiential-learning, insight-extraction, self-reflection, retrieval, reflexion]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 20/08/2023, v3 (lida) em 20/12/2024; o comentário do arXiv diz "aceito na AAAI-24". Autores da Universidade Tsinghua. Lido em 2026-10-29, na pesquisa sobre registro de lições. Os números da figura principal (Fig. 5) foram lidos do gráfico e estão transcritos no integral.

## A pergunta

Um agente de modelo de linguagem consegue aprender com a própria experiência entre tarefas, sem mexer nos pesos do modelo (o que serve para modelos fechados acessados por API)? A analogia dos autores é a do estudante que resolve exercícios várias vezes, tira lições e depois faz a prova numa tentativa só, apoiado nessas lições e na lembrança de problemas parecidos. O ExpeL se apresenta como o passo além do Reflexion: o Reflexion melhora dentro da mesma tarefa, tentando de novo; o ExpeL leva o aprendizado de uma tarefa para outras.

## Como funciona

Três etapas (Fig. 1).

1. **Coleta de experiência (treino).** O agente, um ReAct com gpt-3.5-turbo, tenta cada tarefa de treino; se falha, faz uma autorreflexão no estilo do Reflexion e tenta de novo, até 3 novas tentativas. Toda trajetória, de sucesso ou de falha, vai para um banco de experiências. O objetivo é ter mais sucessos para lembrar e também **pares de falha e sucesso da mesma tarefa** para comparar.
2. **Extração de insights.** Um modelo mais forte (gpt-4-0613) mantém uma lista de insights em linguagem natural, que começa vazia, e a atualiza percorrendo dois tipos de entrada: (a) cada falha comparada com o sucesso da mesma tarefa, que mostra a ação errada e a certa; (b) lotes de L sucessos de tarefas diferentes (L = 8 no HotpotQA e no ALFWorld, 4 no WebShop), que revelam boas práticas comuns. A cada lote o modelo aplica operações à lista: **ADD** (regra nova, bem diferente das existentes), **EDIT** (reescrever regra pouco geral), **UPVOTE** (concordar com uma regra relevante) e **DOWNVOTE** (discordar de regra contraditória ou duplicada). Cada regra nasce com contador de importância 2, ganha 1 com UPVOTE ou EDIT, perde 1 com DOWNVOTE e **é apagada ao chegar a zero**. O porquê declarado: até trajetórias de sucesso podem ser subótimas e induzir regras ruins. O prompt (Fig. 2) pede regras gerais e de alto nível, sem mencionar as tentativas, no máximo 4 operações por chamada e no máximo 1 operação por regra. Os autores acharam o gpt-4 melhor que o gpt-3.5 em seguir essas operações e com menos alucinação.
3. **Uso na avaliação.** Cada tarefa nova recebe, no enunciado, **a lista inteira de insights** concatenada, e como exemplos no prompt as **k trajetórias de sucesso mais parecidas com a tarefa**, recuperadas por semelhança de embedding (Faiss, kNN, all-mpnet-base-v2, produto interno). O agente tem uma tentativa só. Os autores dizem que, se a lista crescer, a recuperação seletiva de insights "poderia ser" a saída para caber no contexto.

**Transferência (seção 4.4):** os insights extraídos numa tarefa de origem são "ajustados" para uma tarefa de destino por um prompt ao gpt-4 com poucos exemplos da tarefa de destino, para ancorar as regras e reduzir alucinação.

## Como mediram

HotpotQA (perguntas com busca na Wikipédia, 100 tarefas), ALFWorld (tarefas domésticas em texto, 134), WebShop (compras em site simulado, 100) e FEVER (verificação de fatos, só para transferência). Validação em quatro dobras, treino numa metade e avaliação na outra, com média e erro padrão; taxa de sucesso como métrica. Bases: ReAct e Act (sem raciocínio), e o Reflexion com 1 a 3 novas tentativas como referência; o ExpeL avalia com uma tentativa só. Temperatura 0. Experimentos de julho a agosto de 2023.

## Resultados

**Taxa de sucesso principal (Fig. 5, %):**

| Ambiente | Act | ReAct | Só insights | Só recuperação | ExpeL | Reflexion R3 |
|---|---|---|---|---|---|---|
| HotpotQA | 29 | 28 | 36 | 31 | 39 | 40 |
| ALFWorld | 28 | 40 | 50 | 55 | 59 | 54 |
| WebShop | 34 | 35 | 37 | 38 | 41 | 48 |

- **Insights e exemplos se complementam, com peso diferente por ambiente.** No HotpotQA os insights pesam mais (36 contra 31), porque a tarefa depende de analisar resultados e pede diretrizes gerais; no ALFWorld pesa mais lembrar trajetórias (55 contra 50), porque a tarefa depende de sequências de ações específicas; no WebShop fica quase empatado (37 e 38; recompensa 0,675 e 0,67). Os dois juntos ganham dos dois sozinhos.
- **Contra o Reflexion:** sem tentar de novo, o ExpeL empata no HotpotQA (39 contra 40 do Reflexion na terceira tentativa) e supera no ALFWorld (59 contra 54); no WebShop fica abaixo até da primeira nova tentativa do Reflexion (41 contra 43), o que os autores reconhecem como espaço de melhora.
- **Transferência HotpotQA para FEVER (Tabela 1):** Act 58, ReAct 63, insights transferidos sem exemplos da tarefa de destino 65, com exemplos 70.
- **Com novas tentativas na avaliação (Tabela 2, ALFWorld):** ExpeL mais Reflexion sobe de 59,0% para 64,2% em três rodadas; ReAct mais Reflexion vai de 40,3% para 54,4%.

**Ablações:**

- **Quantidade e variedade de experiência (Fig. 6, HotpotQA):** insights tirados só dos exemplos iniciais, 27 (nenhuma vantagem sobre o ReAct, 28); experiência coletada só com ReAct, sem novas tentativas e portanto sem pares de falha e sucesso, 35; coleta com Reflexion, 39.
- **Forma de extrair insights (Tabela 3, HotpotQA):** insights escritos à mão por quem estudou os erros, 32; insights com as reflexões do Reflexion misturadas aos pares e listas, 29 (pior, talvez porque as reflexões às vezes alucinam); insights extraídos pelo gpt-3.5, 32; ExpeL, 39.
- **Critério para escolher os exemplos (Tabela 3, ALFWorld):** semelhança de tarefa 59,0; semelhança com o último passo de raciocínio 48,5 (os exemplos mudam no meio da trajetória e desestabilizam); sorteio 42,5; ReAct 40,0.

**Comportamentos observados nas trajetórias (seção 5.3):** depois dos insights, o agente passa a propor a resposta mais provável com o que já observou em vez de responder "desconhecido" (insight "a resposta pode já estar nas observações"); muda a crença sobre onde fica uma panela, do armário para o fogão (insight "considere a natureza e o uso típico do item"); e corrige um erro, devolvendo um objeto pegado por engano (insight "reavalie e considere alternativas se a tentativa não progride").

**Custo:** a trajetória do ExpeL usa bem mais tokens que a do ReAct, por causa dos insights e dos exemplos no prompt; no HotpotQA, cerca de 4.310 contra 1.320 por trajetória (Tabela 6).

## Pontos fortes declarados

Insights e trajetórias ficam em linguagem natural, então o usuário pode inspecionar, editar ou remover o que for nocivo e acrescentar insights de especialista; pede poucos dados e pouca computação; não depende de novas tentativas na hora do uso; melhora junto com o modelo de base (o gpt-4 extrai insights melhores que o gpt-3.5).

## Limites declarados

- Só observações em texto; imagem fica para trabalho futuro.
- Só modelos fechados por API; modelos abertos ficam para trabalho futuro.
- Os insights ainda cabem no contexto; um agente de aprendizado contínuo "de verdade" pode precisar de recuperação de insights para manter o contexto administrável.
- Técnicas de prompt não têm a base teórica do aprendizado por reforço.
