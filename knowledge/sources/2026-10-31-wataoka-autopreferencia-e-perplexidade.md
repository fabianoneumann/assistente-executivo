---
titulo: "Self-Preference Bias in LLM-as-a-Judge"
tipo: paper
autor: "Koki Wataoka, Tsubasa Takahashi, Ryokan Ri"
url: "https://arxiv.org/abs/2410.21819"
publicado_em: 2024-10-29
capturado_em: 2026-10-31
licenca: "CC BY 4.0 (indicada na página do arXiv, link creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [llm-as-judge, self-preference, perplexity, familiarity-bias, equal-opportunity, algorithmic-fairness, chatbot-arena, pairwise-comparison, position-bias, judge-ensemble]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv 2410.21819: v1 em 29/10/2024 e v2 em 21/06/2025, a lida; comparadas, as duas versões só diferem na data do cabeçalho (mesmo texto, mesmas 5.232 palavras extraídas). O comentário do arXiv diz que foi aceito no NeurIPS 2024 Safe Generative AI Workshop (workshop, não a trilha principal). Os três autores são da SB Intuitions (Japão). Sem código declarado. Artigo curto (cerca de 9 páginas com referências), sem testes estatísticos nem intervalos de confiança: as comparações entre curvas são visuais. O integral foi extraído do PDF da v2; as Figuras 1 a 6 (os resultados quase todos estão em gráfico) foram lidas nas páginas renderizadas. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

## 1. A pergunta

Juízes LLM são muito usados para medir sistemas de diálogo (o MT-Bench, por exemplo), e são enviesados. Um dos vieses mais importantes é a **autopreferência**: superestimar a qualidade das próprias respostas. O risco declarado é o juiz promover ideologias ou estilos de resposta próprios dele. Faltam, segundo os autores, uma métrica confiável da autopreferência e uma explicação da causa. Panickssery et al. (2024) ligaram autopreferência a autorreconhecimento, mas sem comparar com avaliadores humanos; Xu et al. (2024) e Stureborg et al. (2024) mediram a autopreferência em notas absolutas de um texto só, o que exige avaliadores de referência dando notas consistentes por critérios abstratos, e por isso ficaram restritos a tarefas como resumo e tradução e a métricas com referência (BLEURT). Os autores preferem a comparação em par: comparar dois textos deixa as diferenças mais visíveis e torna o julgamento humano mais consistente, o que serve para medir o desvio em relação a humanos.

**Contribuições declaradas:** (1) uma métrica nova de autopreferência; (2) a medida em oito LLMs; (3) a tendência de os LLMs darem nota maior a textos de menor perplexidade, como explicação possível da autopreferência.

## 2. A métrica (seções 3 e 4.1)

- **Base em justiça algorítmica:** Equal Opportunity (Hardt et al. 2016) pede que um classificador tenha a mesma taxa de acerto nos positivos (recall) em grupos com atributos sensíveis diferentes: P(Y′ = 1 | S = 1, Y = 1) = P(Y′ = 1 | S = 0, Y = 1). A diferença entre os dois lados mede o viés. A limitação é que, se o rótulo verdadeiro já for enviesado, a definição herda o viés. Demographic Parity (Calders et al. 2009) dispensa o rótulo e pede só a mesma distribuição de previsões entre grupos. Como o juiz LLM serve para substituir avaliadores humanos, os autores usam Equal Opportunity, tratando o juiz como classificador e o humano como verdade.
- **Definição 4.1:** num par de respostas, Y é o índice da preferida pelo humano, Y′ o da preferida pelo juiz f e S o da gerada por f. Viés = P(Y′ = 1 | S = 1, Y = 1) − P(Y′ = 1 | S = 0, Y = 1): a taxa com que o juiz acompanha o humano quando o humano prefere a resposta do juiz, menos a taxa com que acompanha o humano quando o humano prefere a do outro. 0 é ausência de viés; perto de 1, viés forte; −1, viés reverso (o juiz subestima o que é seu).
- **Versão por Demographic Parity (Equação 4, na discussão):** Viés = P(Y′ = 1 | S = 1) − P(Y′ = 1 | S = 0), quanto o juiz prefere o que é seu, sem olhar o humano. Os autores dizem que ela não demonstra injustiça (não considera a qualidade), mas mostra o quanto cada juiz favorece as próprias respostas no cenário.

## 3. O experimento de medida (seção 4)

- **Dados:** o conjunto do Chatbot Arena (Zheng et al.), com 33.000 diálogos, cada um com a pergunta de um usuário, duas respostas de LLMs diferentes e o voto humano ("model_a", "model_b" ou "tie"). Os pares já existentes no conjunto são reavaliados pelos juízes.
- **Juízes (oito, todos presentes no Chatbot Arena como respondentes):** GPT-3.5-Turbo e GPT-4 (fechados); Vicuna-7b, Vicuna-13b, oasst-pythia-12b, dolly-v2-12b, Koala-13b e stablelm-tuned-alpha-7b (abertos).
- **Protocolo:** o prompt de Zheng et al., que pede uma explicação e depois "[[A]]", "[[B]]" ou "[[C]]". A nota de A é a probabilidade do token "A" dividida pela soma das probabilidades de "A" e "B", lida na posição depois de "[["; o mesmo para B. Para mitigar o viés de posição, as respostas são trocadas de lugar e as notas das duas ordens são promediadas. Respostas fora do formato são descartadas. O artigo não diz como a nota contínua vira a escolha binária nem como os empates humanos são tratados na métrica.

**Resultados (Figura 1b, viés pela Definição 4.1):** GPT-4 0,52; GPT-3.5-Turbo 0,03; Vicuna-13b 0,25; Vicuna-7b 0,05; Koala-13b 0,15; oasst-pythia-12b −0,02; dolly-v2-12b −0,05; stablelm-tuned-alpha-7b −0,02. O GPT-4 tem o maior viés, seguido de Vicuna-13b e Koala-13b; os três negativos mostram viés reverso.

**Matrizes de confusão (Figura 2, pares que incluem a resposta do próprio juiz; linhas pelo humano, colunas pelo juiz, contagem "perde" e "ganha" da resposta do juiz):** GPT-4: humano diz que perde, juiz diz que perde 118 e que ganha 160; humano diz que ganha, juiz diz que perde 108 e que ganha 1.852. O acerto quando o humano prefere a resposta do GPT-4 é 0,945 (1.852 de 1.960); quando o humano prefere a do outro, 0,425 (118 de 278); a diferença, 0,520, é o viés da Figura 1b. Note-se a base pequena do segundo grupo (278 pares). GPT-3.5-Turbo: 656, 293 | 676, 1.785. Vicuna-13b: 895, 654 | 568, 2.099. Vicuna-7b: 646, 402 | 297, 586. Koala-13b: 596, 501 | 388, 879. oasst-pythia-12b: 151, 141 | 116, 116. dolly-v2-12b: 797, 692 | 233, 210. stablelm-tuned-alpha-7b: 730, 676 | 244, 241.

**Exemplo (Tabela 1):** pedido "liste os itens azuis". O GPT-4 começa dizendo que, como modelo de linguagem, não vê os objetos ao redor, lista dez itens e pede contexto; o GPT-3.5-Turbo lista dez itens direto. Humanos e o GPT-3.5-Turbo preferem a resposta do GPT-3.5; o GPT-4 prefere a sua. Para os autores, as duas são boas, e a decisão reflete a política e o estilo do avaliador. A Figura 1a traz caso parecido: sobre o mercado financeiro, o GPT-4 prefere a própria resposta que diz não ter dados em tempo real; os humanos preferem a do Vicuna-13B, que responde.

**Tabela 2 (viés por Demographic Parity):** GPT-4 0,749; GPT-3.5-Turbo 0,191; Vicuna-13b 0,382; Vicuna-7b 0,052; Koala-13b 0,175; oasst-pythia-12b 0,006; dolly-v2-12b −0,069; stablelm-tuned-alpha-7b −0,032. Mesma ordem geral da Definição 4.1.

## 4. A explicação pela perplexidade (seção 5)

- **Hipótese:** o juiz não é informado de qual resposta é sua e mesmo assim prefere as suas; talvez reaja à semelhança com o que ele mesmo geraria, medida pela perplexidade (quanto menor, mais provável o texto para o modelo, mais "familiar").
- **Método:** para cada par, a perplexidade de cada resposta condicionada ao prompt, calculada pelo próprio juiz; a diferença entre A e B (em log10) é dividida em faixas, e em cada faixa se calcula a taxa com que o juiz escolhe A e a taxa com que o humano escolhe A. GPT-4 e GPT-3.5-Turbo ficaram de fora, porque a API não dá a perplexidade.
- **Figura 3 (juiz contra humano por faixa de perplexidade):** nos seis abertos, exceto o stablelm (e, pela legenda, também o dolly), o juiz escolhe mais a resposta de menor perplexidade, e a inclinação é mais forte que a dos humanos em Vicuna-13b, Vicuna-7b, Koala-13b e oasst-pythia-12b. Leitura da figura: no Vicuna-13b, a taxa do juiz vai de cerca de 0,95 quando A é muito mais familiar a cerca de 0,1 quando A é muito menos familiar, enquanto a dos humanos fica entre cerca de 0,2 e 0,55. Os humanos também preferem um pouco o texto de menor perplexidade (que tende a ser mais fluente), mas os juízes reagem demais.
- **Figura 4 (o próprio texto contra o texto dos outros, por faixa de perplexidade):** separando os pares em que a resposta do juiz está presente dos pares só com respostas de outros modelos, as curvas de vitória por perplexidade ficam parecidas em todos, exceto dolly-v2-12b e stablelm. Para os autores, o que decide é a perplexidade, não a autoria. Leitura da figura: nas faixas em que o texto do juiz é bem menos familiar que o outro (diferença positiva), as curvas do próprio texto ficam um pouco acima das dos outros no Vicuna-13b, Vicuna-7b e Koala-13b; não há teste de significância.
- **Figura 5 (log10 médio da perplexidade das respostas, próprias contra de outros):** Vicuna-13b 0,52 contra 0,72; Vicuna-7b 0,58 contra 0,73; Koala-13b 0,46 contra 0,70; oasst-pythia-12b 0,68 contra 0,81; dolly-v2-12b 0,92 contra 0,96; stablelm 0,75 contra 0,97. Em todos, o próprio texto é mais familiar. Daí a conclusão: a autopreferência seria o efeito de os próprios textos terem, por construção, perplexidade menor.
- **Figura 6 (modelos mais fortes, Llama):** como faltam rótulos humanos para respostas dos Llama no Chatbot Arena, os autores fizeram os Llama julgarem as respostas existentes e compararam só com os humanos. Llama-2-7b-chat, Llama-2-13b, Llama-2-70b-chat, Llama-3-8B-Instruct, Llama-3-70B-Instruct, Llama-3.1-8B-Instruct e Llama-3.1-70B-Instruct mudam o julgamento com a perplexidade mais do que os humanos. Leitura da figura: o excesso é maior nos Llama 2 (o 7b vai de cerca de 0,95 a 0,07) e menor nos Llama 3.1 (curvas próximas das humanas, de cerca de 0,8 a 0,2). Para os autores, a perplexidade pode causar viés injusto mesmo em modelos competitivos.

## 5. Discussão e recomendações dos autores

- **Mitigação sugerida (não testada):** avaliação em conjunto com vários modelos, para não depender de um só; e, quando um modelo tem perplexidade baixa numa amostra, reduzir o peso do voto dele naquela amostra. A métrica proposta serviria para medir o efeito de qualquer mitigação.
- **Por que a perplexidade pesa:** o pré-treino minimiza a perplexidade num corpus grande, e o alinhamento com preferências humanas também a minimiza nos diálogos; texto de perplexidade alta seria, então, de domínio que o modelo viu pouco e talvez entenda mal.
- **O paradoxo do GPT-4:** o modelo que conhece mais domínios é o mais enviesado. Nos casos examinados (Figura 1a, Tabela 1), o viés não vinha de erro factual, mas de estilo: como tratar domínio especializado, explicar premissas antes de responder. A hipótese dos autores: modelos avançados, que seguem com rigor as próprias políticas, usam o alinhamento com essas políticas como critério de desempate entre respostas de qualidade parecida.
- **Conclusão:** o GPT-4 tem autopreferência alta, com o risco de o juiz GPT-4 reforçar o próprio estilo e as próprias políticas; os juízes dão notas maiores a textos de menor perplexidade do que os humanos dariam, sejam ou não deles. "the self-preference bias exists because LLMs prefer texts more familiar to them."
- **Limites (alguns declarados, outros visíveis no desenho):** a análise de perplexidade não cobre GPT-4 nem GPT-3.5, justamente os de maior viés; o GPT-4 aparece com viés alto e a explicação por perplexidade é testada em outros modelos; não há seção de limitações nem testes estatísticos; a maioria dos juízes são modelos de 2023, pequenos e fracos; os rótulos humanos são os votos do Chatbot Arena, sem controle de quem votou.

## 6. Tudo o mais que ensina

- **Outros vieses citados:** viés de posição e de verbosidade (Zheng et al.); o de posição seria resolvido "com relativa facilidade" trocando a ordem das opções, e há métodos por alinhamento (Li et al., split-and-merge); Saito et al. (2023, com Wataoka) quantificaram o viés de verbosidade em GPT-4 e GPT-3.5-Turbo pelas taxas de erro quando a opção mais longa é a errada.
- **Uso de feedback de LLM para treinar LLMs:** autorrefinamento (Self-Refine), autodepuração, auto-alinhamento por princípios, modelos que se autorrecompensam (Self-Rewarding), com aprendizado por RLHF ou DPO; pares anotados por qualidade relativa são sinal de treino útil. É por isso que o viés do juiz pode passar para os modelos treinados.
- **Normalização das probabilidades:** dividir a probabilidade de cada opção pela soma das duas (como em Schick et al. 2021) deixa comparáveis juízes com distribuições de probabilidade diferentes.
- **Equal Opportunity contra Demographic Parity:** a primeira mede desvio em relação a uma verdade (aqui, o humano) e herda o viés dela; a segunda mede só o favorecimento e não distingue favorecimento merecido de injusto.

---
