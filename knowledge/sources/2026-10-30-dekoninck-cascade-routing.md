---
titulo: "A Unified Approach to Routing and Cascading for LLMs"
tipo: paper
autor: "Jasper Dekoninck, Maximilian Baader, Martin Vechev"
url: "https://arxiv.org/abs/2410.10347"
publicado_em: 2024-10-14
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [routing, cascade, model-selection, quality-estimation, ex-ante-vs-post-hoc, cost-quality-tradeoff, cost, benchmark]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 14/10/2024, v2 em 14/02/2025, v3 em 22/05/2025, v4 em 12/10/2026 e v5 (lida) em 26/10/2026. O PDF da v5 diz no rodapé da primeira página que o artigo saiu nos anais da 42ª ICML (Vancouver, PMLR 267, 2025). Departamento de Ciência da Computação da ETH Zurich; código em github.com/eth-sri/cascade-routing. O integral foi extraído do PDF da v5. Em relação à cópia de trabalho da v3 (texto do HTML do arXiv), a v5 traz a variante MAX-DEPTH na análise de tempo de execução (apêndice F.2) e frases que precisam a formulação (as estimativas fixas usadas como substitutas na otimização de cada passo, na seção 3 e no apêndice B; a fusão de opções idênticas, no apêndice A); a condição dos autores para a cascata valer tem o mesmo texto nas duas versões. Lida (camadas flexíveis de avaliação).

## A pergunta

Com muitos modelos de tamanhos e custos diferentes à disposição, escolher o modelo certo para cada consulta melhora a relação custo-desempenho: usa-se um modelo pequeno quando a consulta não pede o grande. Há duas estratégias conhecidas. O **roteamento** escolhe um único modelo por consulta e não volta atrás; é útil quando tarefas diferentes pedem especialistas diferentes. A **cascata** passa a consulta por uma sequência de modelos cada vez maiores e para quando um deles dá uma resposta considerada boa o bastante; é útil quando as consultas variam de dificuldade. Os autores apontam três limites do que existia: falta prova de que as estratégias são ótimas, não se sabe em que condições cada uma funciona melhor, e as duas não se combinam. Também contestam a crença de que é preciso ter modelos de vários tamanhos para a cascata compensar: "we show that this notion is incorrect".

## Contribuições declaradas

1. Derivar estratégias ótimas de roteamento e de cascata, com uma cascata nova comprovadamente melhor que as anteriores.
2. Propor o **roteamento em cascata** (cascade routing), que junta as duas e também é provado ótimo.
3. Avaliar e mostrar que a estimativa de qualidade é o fator crítico para a seleção de modelos funcionar.

## As duas estimativas (definição dos autores)

Na introdução, os autores dizem que o que mais pesa são boas estimativas do desempenho do modelo e da qualidade da resposta, e separam duas:

- **Estimativa de qualidade ex ante** (ex-ante quality estimation): "the ability to predict whether a model will perform well on a given query". É feita antes de rodar o modelo. Para o roteamento, uma estimativa ex ante confiável é essencial.
- **Estimativa de qualidade post hoc** (post-hoc quality estimation): "the ability to evaluate the quality of a model’s response after generation". É feita depois que o modelo respondeu. Para a cascata, uma estimativa post hoc robusta é crítica; sem ela, a eficácia da cascata fica muito limitada mesmo com modelos de vários tamanhos.

## Roteamento como otimização linear (seção 2)

- **Definição 1:** uma estratégia de roteamento é uma função que leva cada consulta a uma distribuição de probabilidade sobre os k modelos; o modelo é sorteado dessa distribuição. Os trabalhos anteriores usavam só estratégias determinísticas (probabilidade 0 ou 1); os autores usam a versão probabilística, que dá solução melhor e análise mais simples.
- **Qualidade e custo:** q_i(x) é a qualidade da saída do modelo i na consulta x (pode ser acurácia, preferência do usuário ou outro indicador) e c_i(x) é o custo (dinheiro ou latência). Como são desconhecidos, usam-se estimadores. A qualidade pode ser estimada por classificadores pequenos treinados para prever a acurácia do modelo; o custo, tokenizando a consulta, estimando o tamanho médio da saída e aplicando o preço por token da API, ou pelo tempo médio de execução.
- **Definição 2 (roteamento ótimo):** maximizar a qualidade esperada do modelo escolhido sujeito a um orçamento médio de custo B.
- **Solução:** para cada consulta, escolher o modelo que maximiza a troca τ_i(x, λ) = q̂_i(x) − λ·ĉ_i(x), em que λ ≥ 0 regula o peso do custo conforme o orçamento. Quando vários modelos empatam nessa troca, definem-se s_MIN (o mais barato entre os empatados) e s_MAX (o mais caro).
- **Teorema 1:** para um orçamento B existem λ e γ ∈ [0, 1] tais que a estratégia ótima é γ·s_MIN + (1 − γ)·s_MAX; e toda estratégia com custo esperado exatamente B escrita como combinação convexa dessas duas atinge a mesma qualidade ótima. Como γ costuma não ser 0 nem 1, a estratégia ótima não é determinística; os trabalhos que só admitiam roteamento determinístico não conseguem expressá-la e ficam com a quase ótima s_MIN. O Algoritmo 1 dá o pseudocódigo. λ e γ são achados num conjunto de validação; o apêndice A mostra que a busca se reduz a uma busca binária em λ.
- **Exemplo:** dois modelos, custo estimado (0,9; 1) constante; qualidade estimada pela categoria da consulta: matemática (0,8; 0,5), código (0,5; 0,8), genérica (0,8; 0,9). Com λ = 1 e γ = 0,7, o roteador escolhe m1 em matemática, m2 em código e, nas genéricas (empate na troca), m1 com probabilidade 0,7 e m2 com 0,3.
- **Estimativa ex ante no roteamento:** os autores separam a qualidade verdadeira da estimada. O roteamento ótimo só escolhe bem se q_i(x) ≈ q̂_i(x); se as estimativas forem imprecisas, a estratégia falha mesmo quando o roteamento serve à aplicação. A estimativa de custo tem desafios parecidos, mas eles a acharam menos crítica e mais fácil de aproximar.

## Cascata como roteamento em sequência (seção 3)

- **Definição 3 (supermodelo):** uma sequência de modelos; rodar a consulta no supermodelo é rodá-la em cada um deles. M_{1:j} é o supermodelo (m1, …, mj).
- **A cascata vira uma sequência de roteamentos:** no passo j, já se têm as saídas dos j − 1 primeiros modelos. Para decidir se roda m_j, compara-se, em expectativa, o desempenho de todos os supermodelos M_{1:j−1}, …, M_{1:k}. Se M_{1:j−1} for o melhor, a cascata para e devolve a saída de m_{j−1}; se algum dos maiores for melhor, roda m_j. **Definição 4:** uma estratégia de cascata é uma sequência de roteamentos (s(1), …, s(k)), cada s(j) escolhendo entre esses supermodelos. É preciso olhar todos os supermodelos à frente, e não só o próximo, porque m_j pode ir mal numa consulta em que m_{j+1} vai muito bem.
- **Qualidade e custo do supermodelo:** as estimativas são atualizadas a cada passo com as respostas já obtidas. O custo do supermodelo é a soma dos custos. A qualidade é governada pelo melhor modelo dentro dele: a esperança do máximo das qualidades estimadas, tratando cada estimativa como variável aleatória. Ignorar essa incerteza suporia que o supermodelo sempre vale o seu melhor modelo, quando o melhor pode dar uma resposta ruim e outro uma boa. A incerteza é estimada pela variância, num conjunto de validação, da diferença entre a estimativa no passo j e a estimativa final.
- **Teorema 2 (cascata ótima):** existem λ_1, …, λ_k e um γ tais que a estratégia ótima em cada passo j é a combinação γ·s_MIN + (1 − γ)·s_MAX do Teorema 1, com λ_j próprio. O orçamento vale para a cascata inteira; em cada passo, as estimativas daquele momento servem de substitutas fixas na otimização. Algoritmo 2 dá o pseudocódigo; o apêndice B formula um problema interno (o roteamento ótimo em cada passo, para um orçamento B_j) e um externo (os orçamentos por passo que maximizam a qualidade com custo total até B), resolvido por busca de hiperparâmetros. Só um γ é necessário, porque o orçamento vale para a cascata toda.
- **Exemplo:** custos (0,5; 1) e qualidades (0,5; 0,8), sem incerteza. Roda-se m1. Se a resposta é muito longa e a confiança do próprio modelo é só 30%, as estimativas viram, por exemplo, qualidade (0,3; 0,6) e custo (1; 2). Com λ_2 = 1, a cascata para e devolve m1; com λ_2 = 0,1, roda m2 e devolve a saída dele.
- **Os trabalhos anteriores como limiar:** a cascata anterior continua no passo j se a qualidade estimada do modelo anterior fica abaixo de um limiar τ_j. Segundo os autores, todos os trabalhos existentes que eles conhecem são instâncias desse esquema com estimadores próprios da aplicação. **Corolário 1:** sob pequenas hipóteses técnicas, o limiar equivale à cascata ótima se e somente se o custo estimado não depende da consulta, a qualidade estimada dos modelos ainda não rodados não depende da consulta, e a qualidade do supermodelo é igual à do último modelo rodado.

## A condição para a cascata valer (seção 3, "Post-Hoc Quality Estimation")

Na cascata, o peso passa da estimativa ex ante para a post hoc. A regra dos autores: "Cascading approaches are only advantageous when the post-hoc quality estimate provides significantly better information than the ex-ante estimate." Se a melhora for mínima, é mais eficaz rotear direto para o modelo mais adequado, sem cascata. A estimativa post hoc serve para refinar a decisão, mas a ex ante continua útil para julgar se os modelos seguintes podem fazer melhor; só na cascata por limiar, em que a estimativa ex ante é fixa, ela deixa de importar. A cascata deles usa as duas.

Na abertura da seção 4, os autores contrastam os dois paradigmas: o roteamento é útil quando as estimativas ex ante são precisas, e "cascading is more beneficial when post-hoc estimates are accurate".

## Roteamento em cascata (seção 4)

- **Definição 5:** igual à cascata, com uma diferença: no passo j, o roteamento escolhe entre todos os supermodelos que começam pelos j − 1 modelos já computados, e não só entre M_{1:j−1}, …, M_{1:k}. Pode começar por qualquer modelo e continuar redirecionando para outros até um deles dar resposta de qualidade suficiente. **Teorema 3:** a estratégia ótima tem a mesma forma do Teorema 2. Algoritmo 3 dá o pseudocódigo.
- **Ordem dos modelos:** a qualidade e o custo estimados de um supermodelo não dependem da ordem; então os autores ordenam os modelos do supermodelo escolhido por custo e rodam primeiro o mais barato, como na cascata.
- **Número de supermodelos:** na cascata são no máximo k por passo; no roteamento em cascata chegam a 2^k, o que pode ficar caro, e a seleção precisa custar pouco perto da computação dos modelos. **Lema 1 (ganho marginal negativo):** se um modelo m piora a troca custo-qualidade de um supermodelo M numa consulta, nenhum supermodelo que contenha todos os modelos de M será rodado; esses podem ser podados. Segundo os autores, a contribuição negativa é comum, e a poda reduz bastante o espaço de busca. A prova usa a submodularidade da esperança do máximo (Lema 6, apêndice C).
- **Exemplo:** dois modelos com custos (0,5; 1) e qualidades (0,5; 0,8). Com λ_1 = 0,1, roda-se m2 direto; se a saída de m2 for tão ruim que a estimativa vira (0,5; 0,1), com λ_2 = 0,1 roda-se m1 e devolve-se a saída dele. Com λ_1 = 1, volta-se ao caso clássico, começando por m1.

## Avaliação no RouterBench (seção 5.1)

- **Dados:** RouterBench reúne perguntas de sete benchmarks (entre eles MMLU, GSM8k e MBPP) com respostas de onze modelos, do GPT-4 ao Mistral-7B. 5% dos dados (cerca de 2.000 amostras) servem para ajustar os hiperparâmetros e 95% para avaliar.
- **Estimativas simuladas:** como no trabalho original do RouterBench, soma-se ruído gaussiano de média zero aos valores verdadeiros de qualidade e custo e ajusta-se um modelo sobre esse sinal ruidoso (regressão logística, no apêndice D.1). σ_ante é o ruído antes de rodar o modelo (estimativa ex ante) e σ_post o ruído depois (post hoc). Níveis (Tabela 3, desvios-padrão antes/depois): qualidade baixo 0,6/0,3, médio 1,6/0,8, alto 2,4/1,2; custo baixo 0,0002/0,00005, médio 0,0004/0,0001, alto 100/100 (valores como impressos). Para comparação: a qualidade vai de 0 a 1, e o custo médio vai de 0,000073 (menores modelos) a 0,003281 (maiores).
- **Modelos:** três (Mixtral-8x7B-chat, GPT-3.5-turbo-1106, GPT-4-1106-preview), cinco (mais WizardLM-13B-V1.2 e Claude-v2) e onze (todos).
- **Estratégias comparadas:** roteamento (seção 2), cascata por limiar dos trabalhos anteriores (baseline), cascata ótima deles (Teorema 2), roteamento em cascata, e a interpolação linear de custo e qualidade na fronteira de Pareto dos modelos.
- **Métrica:** para cada método, varia-se o orçamento do modelo mais barato ao mais caro, o que gera uma curva qualidade-custo; a métrica é a área sob a curva (AUC).
- **Resultados, zero-shot (Tabela 1, AUC em %, ruído baixo/médio/alto):**
  - Três modelos: interpolação 69,62; roteamento 79,73/74,97/71,81; cascata baseline 80,86/74,64/72,48; cascata deles 81,09/76,16/72,67; roteamento em cascata 82,36/76,55/73,22.
  - Cinco modelos: interpolação 69,22; roteamento 81,24/74,43/71,33; baseline 82,33/73,03/69,53; cascata deles 83,06/75,17/70,18; roteamento em cascata 84,33/76,31/72,75.
  - Onze modelos: interpolação 70,51; roteamento 83,25/74,63/72,67; baseline 84,48/73,64/69,79; cascata deles 84,47/75,10/70,26; roteamento em cascata 87,24/77,57/74,40.
  - Segundo a legenda, todos os baselines ficam sempre abaixo do intervalo de confiança de 95% do roteamento em cascata. O ganho do roteamento em cascata sobre os baselines vai de 1% a 4%; medido em relação à interpolação linear, de 13% a 80%. A distância aumenta com mais modelos e diminui com mais ruído; os autores concluem que o roteamento em cascata é mais eficaz com conjuntos grandes de modelos e estimativas precisas. A cascata nova supera a por limiar em até 2%.
- **Estimativa de qualidade (Figura 2, cinco modelos, vários níveis de ruído):** o roteamento em cascata fica sempre acima, com ganho de até 8% sobre a cascata e até 12% sobre o roteamento. Para o roteamento, σ_ante é o fator crítico (σ_ante alto reduz muito o desempenho em relação ao roteamento em cascata); para a cascata, pesa mais σ_post (σ_post alto degrada muito o desempenho). O roteamento em cascata aproveita σ_ante baixo e σ_post baixo.

## Benchmarks realistas (seção 5.2)

**Com estimativa de qualidade precisa:**

- **SWE-Bench (estimativa post hoc precisa):** em engenharia de software costuma ser mais fácil gerar testes que reproduzem um problema do que corrigi-lo; os autores supõem que a qualidade de uma resposta é estimada com precisão rodando os testes verdadeiros. Usam a divisão "verified", metade para treino e metade para calibração, e os registros de 10 sistemas do placar oficial (listados no apêndice D.2: SWE-agent com Claude 3 Opus, GPT-4o e Claude 3.5 Sonnet; nFactorial; EPAM AI/Run com GPT-4o, em duas datas; Gru; Navie-2; Agentless-1.5 com Claude 3.5 Sonnet e com GPT-4o). O custo é o tempo em segundos para concluir a tarefa, previsto por regressão linear sobre o tamanho da consulta e, quando disponível, o custo dos outros modelos. A estimativa ex ante é uma regressão logística sobre o tamanho da consulta e o repositório de origem; a post hoc usa as notas verdadeiras da avaliação.
- **Minerva Math + LiveCodeBench com Qwen-2.5 Math e Coder, 1,5B e 7B (estimativa ex ante precisa):** o benchmark de origem entra como variável da estimativa de qualidade. Usa-se só a parte de Álgebra do Minerva Math, para os dois conjuntos terem tamanhos comparáveis, com divisão de 50%. Custo: número de tokens da consulta e da resposta multiplicado pelo tamanho do modelo em bilhões de parâmetros. Ex ante: tamanho da consulta, origem e nível de dificuldade; post hoc acrescenta, por exemplo, se as respostas extraídas de modelos diferentes concordam.
- **Resultados (Tabela 2, AUC):** SWE-Bench com 10 modelos: interpolação 40,51; roteamento 40,47; baseline 38,52; cascata deles 53,20; roteamento em cascata 54,12. Com 5 modelos: 38,64; 39,40; 45,89; 50,94; 51,09. Os métodos deles superam os baselines em até 14%. O roteamento não supera a interpolação trivial, porque a estimativa ex ante é insuficiente ali. A cascata baseline também vai mal apesar da estimativa post hoc perfeita, por causa do retorno binário: o limiar ou admite todos os modelos (τ = 0) ou só os corretos (τ > 0). Math+Code (Qwen): interpolação 45,21; roteamento 58,20; baseline 47,03; cascata deles 52,56; roteamento em cascata 58,20. Com estimativa ex ante precisa, o roteamento supera a cascata baseline em 11%; como a estimativa post hoc é pobre, o roteamento em cascata empata com o roteamento; a cascata deles supera bastante a baseline, o que os autores leem como sinal de que ela aproveita a estimativa ex ante em vez de um limiar fixo.
- O custo no SWE-Bench é por latência e no Math+Code é pelo custo de geração; os autores dizem que o roteamento em cascata se adapta a estimadores de custo diferentes.

**Com estimativa de qualidade pobre:**

- **Tarefas:** classificação (ARC-Challenge, MMLU-Pro, MixEval), em que o modelo escolhe uma opção sem raciocínio intermediário, e raciocínio aberto (MMLU-Pro e GSM8k), em que o modelo raciocina antes de responder. Famílias LLAMA-3.1 (8B, 70B, 405B) e GEMMA (2B, Gemma-2 9B e 27B), com MISTRAL (Mistral-7B, Mixtral-8x7B, Mixtral-8x22B) no apêndice. Não há estimador preciso conhecido para essas tarefas; o estimador segue Gupta et al. (2024), com probabilidades logarítmicas como variáveis.
- **Resultados (Tabela 2, AUC):** classificação LLAMA: interpolação 74,28; roteamento 74,92; baseline 74,81; cascata deles 75,46; roteamento em cascata 75,52. GEMMA: 61,68; 64,44; 54,32; 62,79; 64,84. Raciocínio aberto LLAMA: 79,11; 79,32; 79,23; 79,22; 79,88. GEMMA: 54,10; 58,40; 56,18; 56,18; 59,66. O roteamento em cascata empata ou supera todos os baselines, com margens bem menores, de até 1,2%. Os autores atribuem a margem menor às estimativas muito ruidosas, num quadro parecido com o de ruído muito alto do RouterBench.

## Trabalhos relacionados (seção 6)

O roteamento costuma treinar um modelo que prevê se um dado modelo vai acertar a consulta; há variações com dados de preferência quando não existe resposta certa, seleção de API em classificação multirrótulo, encaminhamento de problemas para agentes de software e roteamento token a token. A cascata costuma decidir pela confiança do modelo menor na própria resposta; alternativas: rodar o modelo várias vezes e medir a variância das respostas, saída antecipada por camadas intermediárias em classificação, estudos de medidas de incerteza para cascatas, casos em que a cascata por incerteza falha, votação dinâmica (a cascata para conforme as respostas agregadas) e métricas de qualidade com vários objetivos. Todos podem ser vistos como instâncias do limiar do Corolário 1 com estimadores específicos da aplicação.

## Conclusão e declaração de impacto

Os autores dizem ter dado estratégias teoricamente ótimas para roteamento e cascata, proposto o roteamento em cascata, mostrado que ele supera bastante os baselines, sobretudo com boas estimativas de qualidade e custo, e que a cascata nova supera as anteriores. Na declaração de impacto, apontam a estimativa de qualidade como área crítica de pesquisa futura em seleção de modelos.

## Apêndices: provas (A, B, C)

- **A:** o roteamento é reescrito como programa linear. Supõe-se finito o conjunto dos valores de λ em que dois modelos empatam na troca; os autores chamam a hipótese de muito pequena, porque estimadores implementados em computador têm precisão finita, e modelos com estimativas idênticas são tratados como uma só opção (o que não muda o objetivo). Exige-se também que exista ao menos uma solução viável: o orçamento pode ser tão baixo que nem rodar o modelo mais barato em toda consulta cabe nele.
- **B:** a otimização de cada passo usa as estimativas atuais como substitutas fixas e não modela as atualizações futuras delas. O apêndice prova o Corolário 2 (versão exata do Corolário 1) com uma definição de equivalência entre conjuntos de estratégias.
- **C:** o roteamento em cascata herda a prova da cascata; o Lema 6 prova a submodularidade e dele sai o Lema 1.

## Detalhes experimentais e intervalos (D, E)

- Nas tarefas de estimativa pobre (D.3), metade de cada conjunto é teste; a outra metade se divide entre treinar os estimadores e ajustar hiperparâmetros (no GSM8k usa-se o treino que já existe). Avaliação por completamento, one-shot; na classificação, a probabilidade de cada opção vem direto do modelo; no raciocínio aberto, a resposta é extraída do fim do texto, com várias expressões regulares quando o formato falha. Custo pelos preços por token da API da Together; na classificação a resposta tem um token, e o custo se sabe antes de rodar; no raciocínio aberto, o tamanho da resposta é estimado pelas respostas dos modelos anteriores da cascata ou, sem nenhuma, pela média do treino.
- Variáveis do estimador de qualidade: indicação do conjunto de dados; na classificação, a probabilidade da opção mais provável e a entropia das probabilidades quando o modelo já rodou, e, com vários modelos rodados, se concordam e a divergência de Jensen-Shannon entre as distribuições; no raciocínio aberto, perplexidade, número de tokens e quantis dos logits, e se os modelos concordam. Treina-se uma regressão logística separada para cada combinação de modelo-alvo e histórico de modelos já rodados.
- **E:** a significância é testada por bootstrap sobre as amostras, com o intervalo de 2σ da diferença de AUC entre o roteamento em cascata e cada baseline; se a diferença é positiva e o intervalo não contém zero, o roteamento em cascata é significativamente melhor (Tabelas 4 a 6).

## Ablação e tempo de execução (F)

- **F.1 (onze modelos, RouterBench, Tabela 7, AUC % e tempo médio em ms, ruído baixo/médio/alto):** roteamento em cascata 87,29 e 15,26 / 77,61 e 9,53 / 74,41 e 13,68; SLOW (sem a poda do Lema 1) 87,30 e 78,88 / 77,61 e 87,72 / 74,40 e 88,76; GREEDY (só supermodelos de tamanho j + 1 no passo j) 85,93 e 1,39 / 77,17 e 1,17 / 74,35 e 0,89; NO-EXPECT (qualidade do melhor modelo em vez da esperança) 85,98 e 4,78 / 77,11 e 2,49 / 74,35 e 2,08. SLOW é quase uma ordem de grandeza mais lento com desempenho igual; GREEDY e NO-EXPECT são mais rápidos e perdem de 0,5% a 1,3% nos ruídos baixo e médio; no ruído alto a diferença é menor, porque o modelo linear de qualidade prevê um valor quase constante e a esperança importa menos. Recomendação dos autores: usar a versão normal quase sempre, e GREEDY só se o tempo for crítico.
- **F.2 (dados aleatórios, até 80 modelos, 100 pontos por tamanho, Figura 3):** SLOW fica caro demais já abaixo de 20 modelos; a versão normal trata até 40 modelos em menos de 1 segundo; MAX-DEPTH (profundidade máxima de 3 modelos) trata até 80 em menos de 1 segundo, sem perder desempenho quando a profundidade ótima é de até 3; GREEDY continua muito barato com 80 modelos; NO-EXPECT passa do MAX-DEPTH em 80 modelos. Os autores dizem que cascatas de mais de 3 modelos são raras e que o MAX-DEPTH é uma boa escolha.

## Resultados detalhados e adicionais (G, H)

- **Por benchmark (Tabelas 8 e 9, AUC):** na classificação, por exemplo, GEMMA no MMLU: interpolação 39,40, roteamento 40,01, baseline 36,43, cascata deles 37,68, roteamento em cascata 39,93; no raciocínio aberto, GEMMA no GSM8k: 73,86; 75,01; 68,44; 71,10; 75,25. Família MISTRAL (Tabela 11), classificação/aberto: interpolação 63,39/53,86; roteamento 64,89/58,71; baseline 61,20/48,29; cascata deles 63,31/55,51; roteamento em cascata 64,97/58,73. A Figura 4 mostra curvas qualidade-custo (RouterBench com ruído médio e 5 modelos; SWE-Bench com 5 modelos; classificação com LLAMA).
- **Five-shot no RouterBench (Tabela 10, ruído baixo/médio/alto):** onze modelos: interpolação 75,16; roteamento 85,34/77,77/76,44; baseline 87,14/78,60/74,94; cascata deles 86,72/78,67/75,08; roteamento em cascata 88,78/80,90/78,04. As conclusões da seção 5.1 se mantêm, com uma inconsistência declarada: em dois dos três cenários de ruído baixo, a cascata deles fica abaixo da baseline. Com três modelos, a causa é a superfície de otimização dos hiperparâmetros mais difícil (a cascata começa a perder qualidade com o aumento do custo); fixando os hiperparâmetros no ponto de qualidade máxima, ela chega a 83,35% contra 83,17% da baseline. Com onze modelos, a causa é um descompasso: a qualidade do supermodelo é a esperança do máximo, mas o modelo devolvido é o último rodado; permitindo às duas cascatas devolver o modelo de maior qualidade estimada, a deles volta a superar a baseline. O descompasso não afeta o roteamento em cascata, que não tem essa restrição.

---
