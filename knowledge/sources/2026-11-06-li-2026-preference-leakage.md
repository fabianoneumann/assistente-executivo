---
titulo: "Preference Leakage: A Contamination Problem in LLM-as-a-Judge"
tipo: paper
autor: "Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, Huan Liu"
url: "https://arxiv.org/abs/2502.01534"
publicado_em: 2026-03-04
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [llm-as-judge, preference-leakage, synthetic-data, evaluation-bias, student-models, model-relatedness, calibration, spurious-features, data-contamination]
licenca: "CC BY 4.0, em arxiv.org/abs/2502.01534"
---

# Li e outros 2026 (ICLR 2026): o juiz LLM favorece alunos treinados com dados dele ou de parente

Ficha em palavras próprias; o integral não vem neste repositório e se lê na url do frontmatter. Artigo de conferência na ICLR 2026, versão 3 no arXiv de 4/3/2026, de autores da Arizona State University, University of California Los Angeles, University of Notre Dame e University of Illinois Urbana-Champaign. Área: avaliação de modelos de linguagem grandes (LLM). Código e dados em `github.com/David-Li0406/Preference-Leakage`.

## O conceito

**Vazamento de preferência (preference leakage)** acontece quando "the LLMs used for data generation and evaluation are closely related", e a preferência do juiz passa ao modelo aluno pelo dado sintético, inflando a nota dele. Três papéis: LLM gerador (MG), que produz o conjunto sintético; LLM aluno (MS), treinado nele; LLM juiz (MJ), que dá nota às saídas do aluno. O juiz favoreceria o aluno por traços espúrios (estilo, formato, palavras) herdados do gerador. Os autores comparam com vazamento de dados, a sobreposição entre treino e teste, e dizem que o problema é mais sutil que outros vieses, como comprimento ou o viés egocêntrico de favorecer as próprias saídas, porque a maioria dos LLMs não divulga os dados de treino.

**Três tipos de parentesco entre gerador e juiz:** ser o mesmo modelo; herança, em que um é ajustado a partir do outro ou treinado com as saídas dele, em qualquer direção; mesma família, como versões ou tamanhos diferentes do GPT.

**Três perguntas:** há viés sistemático (RQ1)? Quão grave em cada cenário (RQ2)? Que mecanismo (RQ3)?

## Experimento principal

- **Geradores e juízes:** GPT-4o-2024-11-20, Gemini-1.5-flash, LLaMA-3.3-70B-Instruct-turbo.
- **Alunos:** Mistral-7B-v0.1 e Qwen-2.5-14B, na versão pré-treinada, para evitar vazamento de instruções anteriores.
- **Conjunto de teste:** comparação em pares no Arena-Hard (500 perguntas difíceis em inglês, com 96,7% de correlação de Spearman com os prompts difíceis do LMArena, dizem) e no AlpacaEval 2.0 (805 perguntas).
- **Passos:** 30.000 prompts ao acaso do Ultrafeedback; cada gerador responde, formando três conjuntos sintéticos; cada aluno passa por ajuste supervisionado (SFT) em cada conjunto, com três versões; forma-se cada par de versões; cada um dos três juízes compara o par.
- **Treino:** LLaMA-Factory, sequência de 1.024 tokens, taxa de aprendizado 1,0e-5, 3 épocas, cosseno com aquecimento de 0,1, BF16, 8 GPUs A100.
- **Medida, PLS (preference leakage score):** para o par (i, j), com WR(i, j) sendo a taxa de vitória dada pelo juiz j ao aluno i, faz-se a média AVG(i, j) = [WR(i, i) + WR(i, j)] / 2, e PLS(i, j) = média de [WR(i, i) - AVG(i, j)] / AVG(i, j) e [WR(j, j) - AVG(j, i)] / AVG(j, i). Mede quanto cada juiz favorece o aluno parente em relação ao outro juiz. **Exemplo do artigo (Tabela 8):** Mistral-GPT-4o contra Mistral-Gemini-1.5 no AlpacaEval 2.0: o GPT-4o dá 55,1% e 44,9%; o Gemini-1.5, 36,8% e 63,2%. Médias 45,95% e 54,05%; PLS = 18,4%.
- **O que o PLS deixa de fora:** é preferência entre modelos, sem rótulo de qual resposta é melhor. Os autores separam de propósito o experimento principal, controlado e sem ruído de rótulo humano, das análises com rótulo humano (seções 5.4 e 5.7, dizem; a calibração usa rótulo na 5.8).

**Tabela 1, PLS:**

| Aluno | Par gerador e juiz | Arena-Hard | AlpacaEval 2.0 | Média |
|---|---|---|---|---|
| Mistral-7B | GPT-4o e Gemini-1.5 | 28,7% | 18,4% | 23,6% |
| Mistral-7B | GPT-4o e LLaMA-3.3 | -1,5% | 1,4% | -0,1% |
| Mistral-7B | LLaMA-3.3 e Gemini-1.5 | 13,1% | 19,8% | 16,4% |
| Qwen-2.5-14B | GPT-4o e Gemini-1.5 | 37,1% | 18,6% | 27,9% |
| Qwen-2.5-14B | GPT-4o e LLaMA-3.3 | 1,0% | 2,3% | 1,7% |
| Qwen-2.5-14B | LLaMA-3.3 e Gemini-1.5 | 25,4% | 18,4% | 21,9% |

Os autores dizem que há preferência forte em quase todos os pares, com exceção dos dois pares GPT-4o e LLaMA-3.3. **Arena-Hard** costuma dar valores maiores, com duas explicações possíveis, dizem: a dificuldade das perguntas e a distribuição dos tipos.

**Alunos menores, viés maior (Tabela 14, juízes e geradores GPT-4o e Gemini):**

| Aluno | Arena-Hard | AlpacaEval 2.0 | Média |
|---|---|---|---|
| LLaMA-3-1B | 35,4 | 18,2 | 26,8 |
| LLaMA-3-3B | 32,5 | 16,4 | 24,5 |
| LLaMA-3-8B | 30,9 | 15,8 | 23,4 |
| Qwen-2.5-0.5B | 40,9 | 21,2 | 31,1 |
| Qwen-2.5-1.5B | 38,0 | 23,2 | 30,6 |
| Qwen-2.5-3B | 50,7 | 20,1 | 35,4 |
| Qwen-2.5-7B | 32,2 | 22,1 | 27,2 |
| Qwen-2.5-14B | 37,1 | 18,6 | 27,9 |
| Qwen-3-0.6B | 39,8 | 23,8 | 31,8 |
| Qwen-3-1.7B | 40,0 | 20,1 | 30,2 |
| Qwen-3-4B | 30,9 | 17,2 | 24,1 |
| Qwen-3-8B | 33,9 | 17,4 | 25,7 |
| Qwen-3-14B | 31,7 | 19,4 | 25,6 |

O texto diz que os menores são LLaMA-3-1B, Qwen-2.5-3B e Qwen-3-1.7B; a tabela tem Qwen menores que esses, e diz "em geral" dentro de cada família. Suposição dos autores: modelos grandes memorizam, o que piora a contaminação de dados; os pequenos só aprendem traços espúrios repetidos, como formato.

## Análises adicionais (Mistral-GPT-4o contra Mistral-Gemini-1.5, por custo)

- **Mistura de dados (Figura 2b):** 10%, 30%, 50% e 70% do sintético misturados com dado humano ou sintético de múltiplas fontes, mantendo 30.000. O PLS cresce com a proporção de sintético, sem limiar: "no clear threshold separating cases with preference leakage from those without". Os valores estão só no gráfico.
- **Parentesco (Tabela 2, PLS em Arena-Hard, AlpacaEval 2.0, média):**
  - Mesmo modelo: 28,7%, 18,4%, 23,6%.
  - Herança com as mesmas instruções: 17,8%, 20,7%, 19,3%.
  - Herança com outras instruções: 18,3%, 26,3%, 22,3%.
  - Mesma família e série (gerador GPT-4o e Gemini-1.5-flash, juiz GPT-4-turbo e Gemini-1.5-pro): 10,1%, 7,6%, 8,9%.
  - Mesma família, outra série (juiz GPT-3.5-turbo e Gemini-1.0-pro): 3,3%, 2,2%, 2,8%.
- **Forma de aprender (Tabela 3):** SFT 28,7%, 18,4%, 23,6%. DPO (direct preference optimization, otimização de preferência em pares): 7,7%, 2,7%, 5,2%. ICL (in-context learning, sem ajuste, com 4 exemplos do sintético na hora da inferência): -4,2%, -1,1%, -2,7%.
- **Mundo real (Tabela 4):** diferença de posição entre LMArena e AlpacaEval 2.0 em 41 modelos presentes nos dois, com GPT-4 Preview como avaliador: 1,00 para o próprio GPT-4 Preview (viés egocêntrico) e 1,33 para Vicuna 7B, 13B e 33B (vazamento de preferência). Caso interpretável, dizem, porque poucos pares aluno e professor são documentados.
- **O juiz reconhece o aluno? (Tabela 5, acurácia):** GPT-4o 41,0% em ponto a ponto e 52,0% em par; Gemini-1.5 53,2% e 44,2%; LLaMA-3.3 41,8% e 29,8%. Os autores leem como perto do acaso, o que tornaria o problema difícil de detectar para o juiz. Já um classificador BERT treinado em 80% das respostas dos três alunos separa de quem é a resposta com 82,4% de acurácia no resto (três classes): os alunos carregam traços identificáveis.
- **Tipo de pergunta (Figura 3a, PLS):** Matemática 7,7, Negócios 16,5, Vida diária 17,2, Ciência 17,3, Escrita 21,0, Outros 23,8, Programação 31,4. O GPT-4o classificou as perguntas.
- **Dimensão do julgamento (Figura 3b, PLS, a partir da justificativa do juiz, classificada pelo GPT-4o):** Completude 27,9, Clareza 28,6, Riqueza 28,8, Satisfação 29,0, Factualidade 29,2, Lógica 30,2, Outros 30,4, Criatividade 30,7, Justiça 32,4.
- **Objetivo e subjetivo:** pergunta com resposta definida mostra menos vazamento que pergunta sem resposta única, e o mesmo vale para as dimensões. Uma frase da seção 5.6 diz o inverso ("more significant in objective questions"), mas o título, os valores e a conclusão apontam para o subjetivo.
- **Traços espúrios (Tabela 6, PLS, juiz Gemini-2.0 no lugar do 1.5, reescrita por Qwen-3-8B):**

| Cenário | GPT e Gemini | GPT e LLaMA | LLaMA e Gemini |
|---|---|---|---|
| Linha de base | 17,5% | 2,3% | 18,8% |
| Sem estilo | 9,0% | 3,3% | 14,6% |
| Sem formato | 9,8% | 1,9% | 14,5% |
| Sem palavras | 11,2% | 2,4% | 18,2% |

Os dois pares com mais vazamento caem, sobretudo tirando estilo e formato; tirar palavras muda menos. Os autores dizem que juízes GPT reagem mais ao estilo e LLaMA ao formato.

- **Mitigação, preliminar (Tabela 7):** corpus com rótulo humano (PPE, MTBench, Human Preference), com GPT-4 como alvo e amostras em que uma resposta vem de um aluno dele, como Vicuna ou Alpaca. Medida nova, **Error Bias** = N(alvo preferido, outro vence) / N(outro vence) - N(outro preferido, alvo vence) / N(alvo vence); perto de 0 indica mitigação. Resultados: base 17,8; prompt que pede imparcialidade 18,3; cadeia de raciocínio 15,6; paráfrase 18,7; autocalibração, que estima um viés global em conjunto separado e desloca a previsão, 20,7; **calibração contextual, que estima o viés em conjunto separado e semelhante a cada cenário, 7,3**.

## Robustez (apêndice D)

- **Repetição (Tabela 9, Mistral-7B, média e variância de 3 rodadas):** Arena-Hard: 28,67 e 0,063; 0,50 e 0,910; 12,93 e 0,583. AlpacaEval 2.0: 19,20 e 0,490; 0,20 e 1,240; 19,87 e 0,013. Na ordem GPT-4o e Gemini, GPT-4o e LLaMA, LLaMA e Gemini.
- **Prompt do juiz (Tabela 10, prompt 1 e 2):** GPT-4o e Gemini-1.5: 18,4% e 16,5% no AlpacaEval, 28,7% e 38,7% no ArenaHard. GPT-4o e LLaMA-3.3: 1,4% e -1,2%; -1,5% e 4,5%. LLaMA-3.3 e Gemini-1.5: 19,8% e 17,9%; 13,1% e 15,8%.
- **Significância (Tabela 11, bootstrap com 10.000 reamostragens sobre 500 prompts do ArenaHard):** Mistral-7B: 28,5 (p < 0,001), -1,1 (não significativo), 7,4 (p < 0,01). Qwen-2.5-14B: 37,9 (p < 0,001), 1,2 (não significativo), 26,3 (p < 0,001). Na mesma ordem de pares. Os valores diferem dos da Tabela 1, sem explicação no texto.
- **Língua (Tabela 12, aluno Qwen-3-8B, juízes GPT-4o e Gemini-1.5):** inglês 17,4%, 33,9%, 25,7%; chinês 12,3%, 51,8%, 32,1% (AlpacaEval, ArenaHard, média).
- **Outros pares com Claude-3.5-Sonnet (Tabela 13, média):** Mistral-7B: GPT-4o e Claude 10,4%; Gemini e Claude 11,8%; LLaMA-3.3 e Claude -3,5%. Qwen-2.5-14B: 11,7%; 14,8%; 0,9%.
- **Anotação humana (apêndice C.3):** 100 perguntas do AlpacaEval 2.0, três anotadores e voto de maioria, concordância média de 78,6. Na ordem Humano, Gemini-1.5, LLaMA-3.3, GPT-4o (vitórias do primeiro modelo): GPT-4o contra Gemini: 53,0, 40,2, 49,4, 58,4. GPT-4o contra LLaMA: 62,0, 76,2, 72,1, 67,8. LLaMA contra Gemini: 36,0, 17,1, 39,0, 46,0. Os autores leem viés maior no Gemini-1.5, depois GPT-4o, e menor no LLaMA-3.3.

## Conclusão dos autores

Há viés claro de cada juiz para o aluno parente, mais forte em certos tipos de pergunta e em alunos menores, em vários cenários, e difícil de detectar, sobretudo em perguntas e dimensões subjetivas. Esperam métodos de avaliação mais confiáveis, fontes de treino diversas e benchmarks resistentes à contaminação. Sugerem um detector externo de parentesco como sinal auxiliar para calibrar o julgamento.

## Limites e lacunas que o texto deixa

- Por custo, as análises da seção 5 usam um par de alunos.
- Reavaliar todo o quadro de líderes com outros juízes seria proibitivo, e poucos pares aluno e professor são públicos.
- A mitigação é preliminar, com um alvo (GPT-4).
- O PLS mede juiz escolhendo entre respostas de modelos alunos. Só a Error Bias e a anotação do apêndice C.3 usam rótulo humano, sempre em pares de respostas. O artigo não testa juiz sobre caso de teste rotulado, escrito por um gerador parente.
- O apêndice C.3 abre dizendo que pares com desempenho parecido ou alunos mais fortes mostram mais vazamento, o que difere da seção 4.2, sobre alunos menores.
- A Tabela 9 grafa "Gemini-3.3" em um dos pares.

## Tudo o mais que ensina

- **Onde o problema aparece:** no estudo preliminar (apêndice B), AlpacaEval 2.0, Arena-Hard e MTBench usam GPT-4 como juiz, e modelos destilados de GPT, como Vicuna e Alpaca, aparecem nos três; os autores citam também estudos que usam o mesmo modelo para gerar e avaliar.
- **Vazamento de dados e os métodos para detectá-lo:** recuperação de sobreposição, instrução guiada e o método CDD; contaminação entre línguas e por tarefa.
- **Diferença para o viés egocêntrico:** favorecer a própria geração é um caso direto; o vazamento vem por vários tipos de parentesco e pelo fluxo de dado sintético entre modelos.
- **Prompts publicados no apêndice:** julgamento em pares, reconhecimento do aluno, categorias de pergunta e dimensões do julgamento, com definição de cada dimensão.
- **Uso de LLMs na escrita:** Gemini 2.5 Pro e GPT-5 só para polimento de linguagem, dizem.
- **Agent-as-a-Judge e Prometheus:** citados como variações do paradigma do juiz.
- **Financiamento:** Departamento de Defesa dos EUA, Army Research Office, W911NF-24-2-0175.
