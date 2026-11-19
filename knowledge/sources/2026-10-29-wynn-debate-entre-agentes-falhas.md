---
titulo: "Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate"
tipo: paper
autor: "Andrea Wynn, Harsh Satija, Gillian K. Hadfield"
url: "https://arxiv.org/abs/2509.05396"
publicado_em: 2025-09-05
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [multi-agent-debate, sycophancy, conformity, model-heterogeneity, majority-vote, answer-flips]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 05/09/2025, v2 (lida) em 13/10/2025. Comentário do arXiv: "ICML MAS Workshop 2025". Autores: Andrea Wynn (Johns Hopkins, contribuição igual), Harsh Satija (Vector Institute, contribuição igual), Gillian K. Hadfield (Johns Hopkins). Código em github.com/TheNormativityLab/talk-aint-cheap. Lido em 2026-10-29. Substitui a captura em trechos de 2026-10-23, que tinha as citações e a tabela 1 sem os números dos gráficos (apagada em 2026-10-29, com a curadoria).

## A pergunta

O debate entre agentes (cada um responde, lê o raciocínio dos outros, revisa, e a maioria decide) melhora mesmo a resposta? A literatura anterior testou quase sempre grupos do mesmo modelo; aqui o grupo mistura modelos de capacidade diferente, e os autores procuram onde e por que o debate piora o resultado.

## Como mediram

- Protocolo de Du et al. (2023): rodada 0 com resposta e raciocínio de cada agente; depois T = 2 rodadas em que cada agente recebe a pergunta, a própria resposta anterior e as respostas dos outros, e gera uma resposta atualizada; a decisão final é o voto de maioria. Se as respostas dos outros não cabem no contexto, outra chamada as resume.
- Prompt de debate: "aqui estão as soluções dos outros agentes; usando o raciocínio deles como conselho adicional, dê uma resposta atualizada", e pede para examinar a própria solução e a dos outros. System prompt neutro de assistente prestativo.
- Três modelos de famílias diferentes: GPT-4o-mini (forte), Llama-3.1-8B-Instruct (médio), Mistral-7B-Instruct-v0.2 (fraco). Grupos de três: homogêneos, dois de um e um de outro, e um de cada ("Diverse").
- Três tarefas: CommonSenseQA (múltipla escolha de senso comum, nunca testada em debate antes), MMLU (múltipla escolha em 57 domínios) e GSM8K (problema de matemática com resposta aberta).
- 100 perguntas sorteadas por tarefa, 5 sementes, temperatura padrão, top_p 0,9.
- A comparação justa é com a coluna "w/o Debate": o voto de maioria das respostas iniciais do mesmo grupo, sem troca de raciocínio. A diferença isola o efeito de conversar.
- Para a dinâmica, classificam cada revisão de agente em quatro transições: certa para certa, errada para certa, certa para errada, errada para errada; e cruzam a virada de certa para errada com quantos colegas concordavam com o agente.

## Resultados

**O debate piora em relação ao voto sem conversa** (Tabela 1, acurácia média, sem debate para depois do debate):

- CommonSenseQA: o debate piora em todas as dez configurações. Ex.: 2 Llama + 1 Mistral 58,2 para 50,2; 1 Llama + 2 Mistral 53,4 para 46,8; até 3 GPT cai 75,6 para 74,8.
- MMLU: 1 Llama + 2 Mistral 40,0 para 28,0 (a maior queda, 12 pontos); 3 Mistral 33,6 para 24,4; 2 Llama + 1 Mistral 51,8 para 43,6; 1 GPT + 2 Mistral 65,8 para 58,8. Sobem só 3 GPT (+0,8), 1 GPT + 2 Llama (+3,0) e o grupo de um de cada (+5,6).
- GSM8K: misto, seis configurações sobem e quatro caem. Sobem 1 GPT + 2 Llama (88,4 para 92,8), 1 Llama + 2 Mistral (+3,8), o grupo de um de cada (+3,4), 3 Mistral (+2,8), 2 GPT + 1 Llama (+1,0) e 3 GPT (+0,4); caem 2 Llama + 1 Mistral (82,6 para 75,8), 3 Llama (−3,4), 1 GPT + 2 Mistral (−2,4) e 2 GPT + 1 Mistral (−0,4).
- **Maioria forte não protege:** 2 GPT + 1 Mistral cai nas três tarefas (−2,2, −2,0, −0,4) e 2 GPT + 1 Llama cai em CommonSenseQA e MMLU. Um agente fraco basta para puxar o grupo para baixo.
- Agente sozinho, para referência: GPT-4o-mini 74,8 / 82,6 / 93,2; Llama 57,0 / 55,6 / 76,4; Mistral 41,6 / 34,0 / 34,2. O voto de três cópias sem conversa já ajuda os modelos menores (3 Llama no GSM8K: 87,6 contra 76,4 sozinho).

**Piora ao longo das rodadas** (Figura 1; leitura aproximada do gráfico): no MMLU, 2 Mistral + 1 Llama vai de cerca de 40 para 31 e 28 nas três medições; 3 Mistral de 34 para 26 e 24; 2 Llama + 1 Mistral de 52 para 45 e 43; 1 GPT + 2 Mistral de 65 para 62 e 58. Há grupos que sobem (um de cada no MMLU, de 58 para 62 e 63), mas a tendência dominante em MMLU e CommonSenseQA é de queda, mesmo com maioria de agentes fortes.

**Com que frequência a certa vira errada** (Figura 2, todas as rodadas somadas; números lidos do gráfico, aproximados):

- Quem começa errado quase sempre continua errado (a faixa clara de errada para errada domina nos grupos fracos).
- Entre quem muda, a virada de certa para errada (vermelho) supera a de errada para certa (verde) em quase todas as configurações. Ex.: MMLU, 2 Mistral + 1 Llama: cerca de 13 pontos de transições certa para errada contra 6 de errada para certa; 1 GPT + 2 Mistral: 11 contra 7; CommonSenseQA, 2 Llama + 1 Mistral: 11 contra 7. A exceção visível é 3 Mistral no GSM8K (verde de cerca de 6,5 contra vermelho de 5), coerente com a única alta desse grupo na tabela.
- Contando sobre as respostas que estavam certas no começo da rodada (conta feita nesta ficha a partir da leitura aproximada), a fração que virou errada vai de cerca de 1% no grupo de 3 GPT a cerca de 30% em 2 Mistral + 1 Llama no MMLU; em grupos mistos com GPT, vai de menos de 1% (GSM8K) a cerca de 17% (1 GPT + 2 Mistral no MMLU).
- **A pressão cresce com as rodadas** (Figura 3, legenda e texto): agentes que resistem a largar a resposta certa na rodada 1 resistem menos na rodada 2; a faixa vermelha é maior na segunda rodada. O arquivo da Figura 3 no HTML do arXiv está truncado; só o painel de CommonSenseQA aparece, e nele a faixa vermelha da rodada 2 é maior que a da rodada 1 na maioria das configurações.

**Conformidade social** (Figura 4; probabilidade de virar de certa para errada conforme quantos dos outros dois concordavam com o agente; leitura aproximada):

| Concordam com o agente | CSQA (GPT / Llama / Mistral) | MMLU | GSM8K |
|---|---|---|---|
| 0 (isolado) | 18 / 23 / 19% | 17,5 / 21 / 16,5% | 7,5 / 31,5 / 8% |
| 1 | 11 / 12,5 / 9,5% | 6,5 / 10,5 / 10,5% | 2 / 15 / 3,5% |
| 2 | 3,5 / 3,5 / 3,5% | 2 / 2,5 / 5% | 0,5 / 1,5 / 1,5% |

O agente isolado é o que mais abandona a resposta certa, e o efeito cai à medida que mais colegas concordam. Varia muito por modelo e tarefa: no GSM8K o Llama isolado larga a certa em cerca de 31% das vezes, contra cerca de 8% do GPT e do Mistral.

**Bajulação (sycophancy) entre agentes, e a tentativa de corrigir com incentivo** (seção 6.3, Figura 5): os autores tratam a bajulação, a tendência atribuída ao RLHF de preferir a resposta que agrada a quem pergunta, como algo que pode se estender aos outros agentes. Testam um "prompt de recompensa por acerto", inspirado em estudos de ciência política em que pagar por resposta correta reduz o viés partidário: o system prompt diz que o modelo recebe 1 se a resposta for igual à verdadeira e 0 se não, e manda maximizar o total; o prompt de debate pede a resposta atualizada "para maximizar o payoff". Resultado: não reduz de forma significativa a virada de certa para errada em nenhum nível de concordância, e em muitos casos aumenta. Na leitura aproximada da Figura 5, o GPT-4o-mini isolado passa de cerca de 18% para 24% de transições certa para errada no CommonSenseQA, de 17,5% para 22% no MMLU e de 8% para 13,5% no GSM8K.

**Nenhuma causa única** (6.4): capacidade do modelo, tipo de tarefa e influência social interagem; bajulação sozinha não explica as falhas.

## O que recomendam

- Não aplicar debate ingênuo: o protocolo pode amplificar erro em vez de corrigir, e o resultado depende da tarefa e da mistura de modelos; testar no cenário de uso antes.
- Desenhar o debate para premiar avaliação crítica, não consenso: pedir que cada agente julgue a solidez do raciocínio alheio, pesar contribuições por estimativa de confiança ou credibilidade, premiar verificação independente das afirmações.
- Em treino ou incentivo, punir a conformidade sem fundamento. O alvo, nas palavras deles, é "constructive epistemic disagreement": discordar quando cabe e manter a crença justificada sob pressão social. Pedir no prompt que o modelo priorize o acerto não basta.

## Limites declarados e de escala

O paper não tem seção de limitações. A escala está no setup: 100 perguntas por tarefa, 5 sementes, três modelos pequenos ou médios (o mais forte é o GPT-4o-mini), duas rodadas de debate, um único protocolo de debate (o de Du et al.) e voto de maioria. As porcentagens por transição só existem nos gráficos; os números das Figuras 1 a 5 nesta ficha são leitura aproximada.
