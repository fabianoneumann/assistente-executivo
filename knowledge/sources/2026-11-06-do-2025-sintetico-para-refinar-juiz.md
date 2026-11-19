---
titulo: "Generate, Evaluate, Iterate: Synthetic Data for Human-in-the-Loop Refinement of LLM Judges"
tipo: paper
autor: "Hyo Jin Do, Zahra Ashktorab, Jasmina Gajcin, Erik Miehling, Martín Santillán Cooper, Qian Pan, Elizabeth M. Daly, Werner Geyer"
url: "https://arxiv.org/abs/2511.04478"
publicado_em: 2025-11-06
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [synthetic-data, llm-as-judge, criteria-refinement, human-in-the-loop, evalassist, user-study, human-llm-alignment, borderline-cases, criteria-drift]
licenca: "CC BY-NC-ND 4.0, em arxiv.org/abs/2511.04478; pela cláusula NC (decisão de 2026-11-01) entra só a ficha, e o integral está na url"
---

# Do e outros 2025 (arXiv, cs.HC): caso sintético para refinar os critérios de um juiz LLM

Ficha em palavras próprias (licença com NC e ND: o integral não entra; está na url). Manuscrito submetido à ACM, versão 1 no arXiv de 6/11/2025, de pesquisadores da IBM Research (EUA, Irlanda, Argentina). Área: interação humano-computador aplicada a avaliação com LLM como juiz (LLM-as-a-judge, um modelo de linguagem grande que avalia texto). A ferramenta estudada, EvalAssist, é um sistema aberto do mesmo grupo (`ibm.github.io/eval-assist`), construído sobre a biblioteca Unitxt.

## A pergunta

O juiz LLM permite critério definido pelo usuário, e o alinhamento com a pessoa costuma sair de iterar sobre poucas amostras. Falta dado variado, sobretudo perto da fronteira de decisão, e mesmo com dado disponível a amostragem pode não cobrir os pontos cegos de quem define. Já se estudou dado sintético para treinar modelo; aqui o estudo é sobre o uso dele como "a means to help humans critically reflect on and refine their own criteria". Quatro perguntas: preferência (RQ1), o dado gerado (RQ2), carga de trabalho (RQ3) e critérios (RQ4).

## A ferramenta

**Estudo formativo:** entrevistas com 5 profissionais de uma grande empresa de tecnologia. Viam valor no sintético quando o dado real falta ou é desbalanceado (um cita 20 amostras de um cliente, por confidencialidade), e temiam teste circular de modelo que avalia a própria saída, viés que se soma, métricas infladas e texto que não reflete o real ruidoso e informal. Daí os princípios de desenho (o texto diz cinco e lista seis): controle sobre o prompt; cobertura de casos limítrofes; personas e variação de estilo; transparência do prompt e da justificativa; lotes pequenos antes de escalar; interface simples.

**Duas funções:**

- **Geração de instâncias:** o usuário escolhe tarefa (geração de texto, resumo, pergunta e resposta, genérica), domínio, persona, comprimento e quantidade por opção do critério, com uma opção "limítrofe" de caso que não cabe claramente em nenhuma. Se pedir limítrofe, um LLM escreve antes a descrição dessa opção a partir dos critérios atuais.
- **Manipulação direta:** selecionando um trecho, parafraseia, elabora, encurta ou regenera (troca por sentido alternativo ou contrafactual, como "helpful" por "harmful"); o usuário aceita ou rejeita.

**Exemplo do artigo (Jane):** critério de viés com "uma perspectiva" contra "várias perspectivas". O caso limítrofe gerado critica uma política, ela espera "Biased", o juiz diz "Non-biased" porque o texto menciona mais de um ponto de vista. Ela percebe a falha, reescreve para "favorece um lado" contra "imparcial", varia o caso com o botão de elaborar, e o resultado passa a bater.

## O estudo com usuários, passo a passo

- **Participantes:** 24 profissionais que avaliam texto, de uma mesma "large multinational technology company" (o texto não a nomeia), recrutados por mensagem interna, de 7 países, sobretudo EUA (10) e Índia (7). Mais de metade em desenvolvimento de software (13). Experiência em IA: extensa 6, moderada 11, básica 7. Em usar IA para avaliar dados: especialista 3, avançada 6, intermediária 8, iniciante 5, mínima ou nenhuma 2. A maioria (19) não conhecia o EvalAssist.
- **Desenho:** dentro dos participantes, duas condições. **Synthetic:** com a ferramenta, gerar ao menos um caso. **Manual:** ferramenta escondida, criar ao menos um caso à mão. Na Manual, para evitar um rival fraco, os participantes tinham um link com 10 exemplos reais, sorteados de conjuntos públicos anotados com classes balanceadas, de uso opcional: 13 de 24 usaram (subgrupo **Sourced**) e 11 escreveram do zero (**Authored**). O ajuste veio de pilotos (N=6) em que alguns acharam difícil inventar casos.
- **Tarefas:** duas, uma em cada condição, com ordem de condição e tarefa balanceada em quatro sequências. **Viés:** frases de notícias, 2 classes (biased, non-biased). **Polidez:** pedidos, 3 classes (polite, neutral, impolite). Escolhidas por exigirem interpretação subjetiva, serem rápidas de ler e terem conjuntos públicos anotados.
- **Sequência:** questionário prévio, em que cada participante também avalia à mão os dados de validação (20 exemplos de viés e 20 de polidez, parte reais de conjuntos públicos, parte sintéticos do GPT-4.1 Mini; o artigo não dá a proporção). Depois, cerca de 80 minutos por vídeo: tutorial, tarefa de aquecimento, as duas condições pensando em voz alta, com registro das interações, questionário e entrevista após cada uma e entrevista final. Recompensa equivalente a US$ 37,5.
- **Modelo:** Llama 3.3-70B tanto para gerar os casos quanto para julgar, escolhido em testes preliminares por ser razoável e rápido. Modo de avaliação direta, em que o juiz escolhe uma opção da rubrica. Comprimentos: curto 1 a 2 frases, médio 3 a 5, longo 5 a 9. Seis domínios, cinco personas cada, gerados com GPT-4.1 Mini para variar o nível de viés ou polidez.
- **Análise:** temática para o qualitativo (dois pesquisadores, consenso); modelos ordinais mistos (CLMM) com teste de razão de verossimilhança para as escalas Likert, que os autores dizem servirem de apoio ao qualitativo, sem pretensão de generalização; Friedman ou modelo linear misto para o comportamento. Comparação de subgrupos só como exploração quando a principal não dá diferença.

## O que é cada medida e sobre que conjunto

| Medida | O que é | Sobre que conjunto | Synthetic | Manual | Teste |
|---|---|---|---|---|---|
| **Agreement score** (concordância) | acertos entre o resultado que o participante esperava e o que o juiz gerou, divididos pelo total de casos | os casos de teste da própria tarefa daquele participante: gerados pela ferramenta na Synthetic; escritos por ele ou tirados dos 10 reais na Manual. O texto diz "during the task" sem dizer se conta a última rodada ou todas, e as condições pediam só "ao menos um" caso de cada tipo | M = 0,85, DP = 0,23 | M = 0,89, DP = 0,2 | Friedman χ²(1) = 0,6, p = 0,44; W de Kendall = 0,025, IC 95% 0 a 0,27. Subgrupos: χ²(1) = 0,04, p = 0,84; η²H = -0,04, IC -0,05 a 0,18 |
| **Alignment score** (alinhamento) | probabilidade de o resultado do juiz, com os critérios finais do participante, coincidir com a avaliação manual que ele fez antes da sessão | os dados de validação: 20 exemplos por tarefa, reais e sintéticos, fixos e fora da sessão. O artigo não separa o resultado entre reais e sintéticos | M = 0,57, DP = 0,15 | M = 0,59, DP = 0,13 | χ²(1) = 0,46, p = 0,50; f² = 0,14. Subgrupos: χ²(2) = 2,11, p = 0,35; f² = 0,25 |
| Preferência | qual versão prefere | questionário final, 24 participantes | 83% (20) | 2; outros 2 sem preferência | χ²(2) = 27, p < 0,05 |
| Número de casos | casos usados na avaliação | registros | M = 9,08, DP = 4,99 | M = 5,21, DP = 2,04 | χ²(1) = 14,73, p < 0,001; W = 0,61, IC 0,27 a 0,96 |
| Palavras por caso | total de palavras | registros | M = 32,21, DP = 13,23 | M = 16,24, DP = 4,62 | χ²(1) = 13,5, p < 0,001; W = 0,56, IC 0,18 a 1 |
| Termos únicos | contagem por caso | registros | M = 32,21, DP = 13,23 | M = 16,24, DP = 4,62 | χ²(1) = 13,5, p < 0,001; W = 0,56, IC 0,25 a 1 |
| Razão de termos únicos | termos únicos médios sobre total de palavras | registros | M = 0,83, DP = 0,07 | M = 0,88, DP = 0,05 | χ²(1) = 8,17, p < 0,001; W = 0,34, IC 0,06 a 0,84 |
| Tempo da tarefa | duração | registros | sem valores no texto | sem valores no texto | χ²(1) = 0,52, p = 0,47; f² = 0,10 |
| Escalas Likert | percepção de 1 a 5 | questionário após cada condição | Tabela 3 abaixo | Tabela 3 abaixo | Tabela 3 |

As linhas de palavras e de termos únicos trazem as mesmas médias e o mesmo teste no texto, com IC diferente; a ficha copia como está. Os autores não comparam as duas medidas principais entre si; elas diferem em conjunto e em cálculo.

## Tabela 3, escalas (mediana e intervalo interquartil; razão de chances com a Synthetic como referência)

| Item | Synthetic | Manual | OR [IC 95%] | χ² (p) | Authored | Sourced | χ² (p), subgrupos |
|---|---|---|---|---|---|---|---|
| Diversidade de tópicos | 4 (4-5) | 4 (3-4,25) | 0,42 [0,14; 1,28] | 2,44 (0,19) | 4 (3-4) | 4 (4-5) | 3,24 (0,19) |
| Diversidade lexical | 4 (3,75-5) | 4 (3-5) | 0,56 [0,18; 1,73] | 1,04 (0,31) | 3 (2-4,5) | 4 (4-5) | 3,07 (0,22) |
| Diversidade sintática | 4 (4-5) | 4 (3,75-5) | 0,56 [0,16; 1,91] | 0,89 (0,35) | 3 (2,5-4) | 4 (4-5) | 7,92 (< 0,05) |
| Diversidade de opções | 4,5 (4-5) | 4 (4-5) | 1,09 [0,73; 1,62] | 0,03 (0,87) | 4 (4-5) | 5 (4-5) | 0,84 (0,66) |
| Utilidade | 5 (4-5) | 5 (4-5) | 1,73 [0,44; 6,70] | 0,64 (0,43) | 4 (4-5) | 5 (5-5) | 5,30 (0,07) |
| Satisfação com o dado | 4,5 (4-5) | 5 (4-5) | 0,90 [0,29; 2,76] | 0,04 (0,85) | 4 (3,5-5) | 5 (4-5) | 0,63 (0,73) |
| Qualidade | 4 (3-4) | 4 (4-5) | 1,84 [0,60; 5,62] | 1,17 (0,28) | 4 (4-4) | 4 (4-5) | 2,61 (0,27) |
| Relevância | 5 (4-5) | 5 (4-5) | 0,80 [0,21; 3,02] | 0,11 (0,74) | 5 (4-5) | 5 (4-5) | 0,12 (0,94) |
| Demanda mental | 3 (3-3) | 3 (2,75-3) | 0,31 [0,08; 1,24] | 3,04 (0,08) | 3 (2,5-3) | 3 (3-3) | 3,23 (0,20) |
| Desempenho | 4 (3-4) | 4 (3-4) | 0,99 [0,32; 3,13] | 0,00 (0,99) | 4 (3-4) | 4 (4-4) | 0,45 (0,80) |
| Esforço | 3 (2-3) | 3 (2-3) | 0,18 [0,12; 0,26] | 1,53 (0,22) | 3 (2,5-3) | 3 (2-3) | 3,57 (0,17) |
| Satisfação com o critério | 4 (4-5) | 5 (4-5) | 2,01 [0,59; 6,83] | 1,30 (0,25) | 5 (4-5) | 5 (4-5) | 1,44 (0,49) |

Só a diversidade sintática difere, entre subgrupos: post-hoc, Synthetic e Sourced acima de Authored (p < 0,05), sem diferença entre Synthetic e Sourced (p = 0,51). Na linha de esforço, o IC da razão de chances não cruza 1 e o p é 0,22; copiado como está.

## Resultados por pergunta

- **RQ1, preferência:** motivos com contagem: geração rápida (8), diversidade (7), personalização (6), menos carga (5), opções variadas (4), escala (3), inspiração (3), texto de qualidade (2), facilidade (2). Função mais citada: geração de instâncias (17), com domínio (10), persona (7), quantidade (6), limítrofes (4); depois a barra de manipulação (8), com o botão de elaborar (3). Quem preferiu o manual viu valor em exemplo real ou próprio; os dois sem preferência veem os modos como complementares.
- **RQ2, dado:** mais casos e mais longos, sem diferença de tempo. Os participantes usaram poucos parâmetros: 1,50 domínios (DP 0,88), 1,75 personas (DP 0,99), 1,21 comprimentos (DP 0,51), muitas vezes escolhendo um caso desafiador. Exploraram mais as opções: 3,25 (DP 1,02) de 4 em polidez e 2,92 (DP 0,29) de 3 em viés. Os autores não acham diferença em diversidade de opções, e atribuem a isso os 10 exemplos reais terem sido balanceados e as tarefas terem poucas opções.
- **RQ3, carga:** notas moderadas e sem diferença, embora o motivo citado para preferir fosse menos carga. Hipótese dos autores: menos esforço por caso compensado por mais casos e mais longos.
- **RQ4, critérios:** satisfação alta e sem diferença. Estratégias de refino, com número de participantes (Synthetic e Manual): definir conceitos 14 e 15; tom e linguagem 9 e 8; ancorar em dado ou domínio específico 1 e 6; regra objetiva, como limite de comprimento, 2 e 6; casos nuançados 3 e 2; palavras-chave 5 e 6; usar as explicações 2 e 0; sem mudança 5 e 4. As duas estratégias mais frequentes na Manual podem dar critério específico demais, dizem. No geral, "the test data had a limited downstream impact on the criteria refinement process".

## Conclusão e leitura dos autores

Sintético e feito à mão ou real tiveram efeito comparável no refino e no alinhamento, e os participantes preferiram a ferramenta. Mais casos não levaram a critério melhor: pela teoria de sensemaking, a ferramenta ajuda a buscar informação, mas não a achar padrões de desalinhamento nem a transformá-los em mudança de critério. Sugerem que o sistema ajude nisso, como faz o EvalGen. A satisfação alta pode refletir o efeito IKEA, de valorizar mais o que se fez.

## Limites declarados

- Participantes de uma só empresa.
- Uma tarefa de geração de texto, com critérios subjetivos, só texto, só EvalAssist.
- Amostra pequena: as estatísticas de questionário não valem como afirmação isolada.
- Subgrupos Authored e Sourced por autosseleção, então diferenças podem vir de características prévias.
- O desenho das tarefas, com 2 ou 3 opções, limita o que se vê em diversidade de opções.
- Saídas repetitivas sob a mesma configuração, mesmo com temperatura alta.
- "the generated text lacked the "messiness" of real-world data": falta gíria, jargão, informalidade e erro de gramática.

## Tudo o mais que ensina

- **Deriva de critério (criteria drift):** citando o EvalGen de Shankar e outros, conforme as pessoas julgam mais dados, reinterpretam o critério; daí a defesa de iterar com casos suficientes antes de fechar.
- **Limite da amostragem de um conjunto grande:** estratégias baseadas em conjunto, como o EvalLM, supõem dado não rotulado farto; o real é ruidoso e pode não ter o caso raro que revela a falha. Sem casos difíceis, há risco de ajustar o critério aos exemplos vistos.
- **Diversificar a geração:** o LLM dá uma resposta por prompt, então a variedade pede prompts variados: a partir de instâncias semente ou de listas de conceitos e personas.
- **Teoria da variação:** o botão de variar trecho se apoia na ideia de que se aprende variando aspectos críticos.
- **Arquitetura de escolha:** a opção listada com padrão de 1 por categoria foi explorada; domínio e persona em lista de escolha única, não. Os autores sugerem multisseleção.
- **Comprimento e riqueza:** mais termos únicos no total e razão menor; os autores dizem que a diversidade relativa cai com o texto mais longo.
- **Trabalhos relacionados citados:** AMPLIO (Yeh e outros), MOCHA (Gebreegziabher e outros), Self-Taught (Wang e outros), EvalLM (Kim e outros).
