---
titulo: "Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge"
tipo: paper
autor: "Lin Shi, Chiyu Ma, Wenhua Liang, Xingjian Diao, Weicheng Ma, Soroush Vosoughi"
url: "https://arxiv.org/abs/2406.07791"
publicado_em: 2024-06-12
capturado_em: 2026-10-31
licenca: "CC BY-NC-SA 4.0 (indicada na página do arXiv, link creativecommons.org/licenses/by-nc-sa/4.0/); só a ficha entra (licença não comercial)"
areas: [agent-engineering]
tags: [llm-as-judge, position-bias, pairwise-comparison, listwise-comparison, position-consistency, preference-fairness, repetition-stability, answer-quality-gap, judge-agreement, mt-bench, benchmark-design]
---

Ficha em palavras próprias; o texto integral (licença CC BY-NC-SA 4.0, não comercial) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv 2406.07791, com nove versões: v1 em 12/06/2024 e v9 em 11/11/2025, a lida. O comentário do arXiv diz AACL-IJCNLP 2025. O artigo mudou bastante entre versões: até a v6 o título era "Judging the Judges: A Systematic Investigation of Position Bias in Pairwise Comparative Assessments by LLMs"; o resumo da v1 fala em 9 juízes e cerca de 80.000 avaliações, o da v4 e da v7 em 12 juízes e mais de 100.000, e o da v9 em 15 juízes e mais de 150.000 (o corpo da v9 ainda diz "more than 100,000", na seção 3.1). Autores do Dartmouth College. Código num repositório anônimo (anonymous.4open.science, "Position-Bias-Analyzer-Demo"); custo declarado de cerca de US$ 3.000 em API. O integral foi extraído do PDF da v9; a Tabela 2, as Figuras 2, 3 e 4 e os modelos de prompt (páginas 21 a 23, que estão em imagem e não saem no texto) foram lidos nas páginas renderizadas. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Atenção:** os juízes deste estudo são LLMs, não pessoas; a "verdade" sobre qual resposta é melhor não vem de humanos, mas da própria consistência do juiz sob troca de ordem.

## O resumo

O viés de posição é a tendência do juiz LLM de favorecer uma resposta pelo lugar que ela ocupa no prompt, e não pelo conteúdo. Os autores estudam o viés em comparações em pares e em listas, com três métricas: estabilidade na repetição (repetition stability), consistência de posição (position consistency) e justiça de preferência (preference fairness). São 15 juízes, MTBench e DevBench, 22 tarefas, cerca de 40 modelos que geram as respostas candidatas. O viés não é ruído aleatório, varia muito entre juízes e entre tarefas, depende pouco do comprimento dos textos e depende muito da diferença de qualidade entre as respostas: quanto mais parecidas, mais o juiz vira com a ordem. A análise de concordância entre juízes mostra quais instâncias são fáceis ou difíceis de julgar e sugere ajustes no desenho de benchmarks.

## 1. A pergunta

- Estudos anteriores registraram o viés de posição ao lado de outros vieses, de forma preliminar. As mitigações propostas removem o viés só em parte, acrescentam complexidade, introduzem vieses novos, funcionam de forma inconsistente ou exigem acesso aos pesos (inviável em modelo fechado). O cenário de lista (mais de dois candidatos) ficou pouco explorado.
- Objetivo: uma investigação sistemática e exploratória do viés de posição, separando os fatores em três níveis (do juiz, do candidato e da tarefa). O estudo é post hoc: primeiro coletaram os julgamentos, depois identificaram os fatores.
- Achados declarados na introdução: (1) o viés dos juízes capazes não é variação aleatória; (2) a direção da preferência oscila muito, até no mesmo juiz em tarefas diferentes; (3) a diferença de qualidade entre as respostas influencia muito a consistência; (4) o comprimento dos prompts tem correlação muito fraca com o viés.

## 2. O desenho

**Comparação em pares (Figura 1a):** o juiz recebe o prompt de sistema, as opções, a pergunta e as duas soluções e escolhe a melhor. Duplo-cego: o juiz não sabe quais modelos geraram as soluções, e os modelos não sabiam que seriam comparados. Depois, o mesmo juiz recebe o prompt com as soluções trocadas de lugar; os dois julgamentos formam um par. Se o juiz escolhe a mesma solução nas duas ordens, é consistente; se muda de vencedor, há viés de posição, na direção de primazia (sempre a primeira) ou de recência (sempre a segunda). Modos de opção: dois (A ou B) ou três (com C para empate).

**Comparação em lista (Figura 1c):** três ou mais candidatos; por eficiência o juiz escolhe só o melhor, com a opção "nenhum claramente superior". A troca vira permutação: com p candidatos, p permutações, cada candidato aparecendo uma vez em cada posição.

**As três métricas:**
- **Repetition Stability (RS):** o mesmo prompt repetido várias vezes; para cada consulta, a fração das tentativas que caiu na escolha mais frequente, média sobre as consultas. Vai de um valor pequeno (decisão aleatória, depende do número de opções) a 1,0 (estabilidade perfeita). É pré-requisito: sem RS alto, o viés medido pode ser só ruído.
- **Position Consistency (PC):** fração das séries de julgamento (original e trocadas) em que o juiz prefere a mesma solução em todas as permutações. É a métrica mais usada antes (Zheng et al.).
- **Preference Fairness (PF):** mede para que lado o juiz pende. Os autores criticam as duas formas anteriores: contar pares com primazia e recência e normalizar pelo total do conjunto (pcn e rcn) fica sensível ao tamanho do conjunto; calcular as taxas só entre os pares inconsistentes (ipr e irr, que somam 1) ignora que julgamento consistente também é justo e pune demais o juiz muito consistente. A proposta combina as duas: PF_raw = (rcn × irr) − (pcn × ipr), reescalada por mínimo e máximo atingíveis para cada juiz e tarefa, para o intervalo de −1 a 1. PF = 1 é recência total com PC = 0; PF = −1 é primazia total com PC = 0; 0 é justo; positivo pende para a segunda posição, negativo para a primeira. Na lista, a extensão é "um contra todos": primazia é preferir o primeiro, e qualquer outra posição conta como recência.

**Fatores (Tabela 1):** do juiz, a "propriedade familiar" (GPT, Claude, Gemini, Llama), usada como substituto de tamanho e treino, que são fechados; do candidato, a diferença de qualidade das respostas; da tarefa e do candidato, os comprimentos da pergunta (entrada), da resposta (saída) e do prompt inteiro.

**Diferença de qualidade (answer quality gap):** a qualidade de uma solução é o quanto ela resolve a pergunta. Os julgamentos são separados em vitórias consistentes (Cw, o mesmo vencedor em todas as permutações), empates consistentes (Ct) e séries inconsistentes (CI). Seguindo Zheng et al., a série inconsistente conta como empate para todos. A taxa de vitória geral é owr = (1/n)[Cw + (1/p)(Ct + CI)], e a diferença de qualidade é δq = |owr − 1/p|, em que 1/p é a linha de base quando tudo é empate. Os autores preferem a owr à taxa de vitória só nas consistentes (Cw sobre o número de séries consistentes, usada por Zheng, Li e Raina) porque ela usa todos os dados e captura os casos de qualidade parecida, justamente os que provocam viés e que a outra taxa ignora.

## 3. Juízes, dados e protocolo

- **15 juízes:** 4 Claude (Claude-3.5-Sonnet 20240620, Claude-3-Opus, Claude-3-Sonnet, Claude-3-Haiku), 3 Gemini (1.5-pro, 1.0-pro, 1.5-flash), 5 OpenAI (GPT-4 0613, GPT-4-Turbo 1106-preview, GPT-4o 2024-05-13, GPT-3.5-Turbo 1106, o1-mini) e 3 Llama de pesos abertos (3.3-70B, 3.1-405B, 3.1-8B). O apêndice F.1 diz "seven GPT, four Claude, and three Gemini", mas lista cinco modelos da OpenAI; a Tabela 2 tem 12 fechados mais 3 Llama. A Tabela 3 do apêndice acrescenta mais sete abertos (GPT-OSS-20B, Gemma-3n-E4B, Llama-4-Scout-17B, Mistral-Small-24B, Qwen2.5-72B, Qwen2.5-Coder-32B, Qwen2.5-7B).
- **MTBench:** 30 modelos candidatos, 8 tarefas (coding, extraction, humanities, math, reasoning, roleplay, stem, writing), 10 perguntas por tarefa; cada candidato é pareado com a resposta de referência do vicuna-13b-v1.3. **DevBench:** 10 candidatos (CodeLlama, DeepSeek-Coder, GPT-3.5 e GPT-4 em várias versões), 14 tarefas (as métricas gerais divididas em detalhadas: classe UML com 4, sequência UML com 5, desenho de arquitetura com 5), 8 perguntas; a referência é a resposta humana. As bases foram escolhidas por terem concordância humano-LLM alta já validada e por serem públicas.
- **Modos de opção:** a seção 3.1 diz dois para o MTBench e três para o DevBench, mas os modelos de prompt do apêndice mostram o contrário (o do MTBench pede "[[A]]", "[[B]]" ou "[[C]]" para empate; o do DevBench só A ou B), e o apêndice C trata o MTBench como o de três opções. Os prompts originais dos benchmarks foram mantidos; todos já pedem ao juiz que evite viés de posição (o do DevBench em maiúsculas: "AVOID ANY POSITION BIASES"), pedem razões (Chain-of-Thought) e um formato de saída fixo. O do MTBench também pede para não deixar o comprimento influenciar e não favorecer nomes.
- **Volumes:** RS com 3 perguntas por tarefa, 4 candidatos e 3 repetições, temperatura 1 para todos os juízes (576 instâncias por juiz no MTBench e 432 no DevBench). PC e PF sobre os conjuntos inteiros: 4.800 instâncias por juiz no MTBench e 2.240 no DevBench (as respostas em ordem original e trocada). Lista: 9 modelos sorteados formando três trios, avaliados por quatro juízes (Claude-3.5-Sonnet, Gemini-1.5-pro, GPT-4o, GPT-3.5-Turbo) no MTBench.
- **Estatística:** regressão stepwise bidirecional (seleção para frente e eliminação para trás) com critério AIC, prevendo PC e PF a partir dos comprimentos médios de entrada, saída e prompt, da diferença de qualidade, do juiz, da identidade do candidato e da categoria da tarefa.

## 4. Resultados

**Tabela 2 (média ± desvio; MTBench em pares RS, PC, PF; DevBench em pares RS, PC, PF; lista no MTBench PC, PF):**
- Claude-3.5-Sonnet: 0,96 ± 0,07; 0,82 ± 0,14; 0,01 | 0,95 ± 0,09; 0,76 ± 0,16; 0,22 | lista 0,67 ± 0,19; 0,17 ± 0,19.
- Claude-3-Opus: 0,95; 0,70; 0,22 | 0,96; 0,69; 0,29.
- Claude-3-Sonnet: 0,93; 0,59; 0,32 | 0,95; 0,71; 0,23.
- Claude-3-Haiku: 0,89; 0,57; 0,18 | 0,90; 0,23; 0,75.
- Gemini-1.5-pro: 0,97; 0,62; 0,23 | 0,87; 0,84; 0,03 (erro 0,13) | lista 0,55; 0,33.
- Gemini-1.0-pro: 0,89; 0,57; 0,30 | 0,85; 0,66; −0,05.
- Gemini-1.5-flash: 1,00; 0,67; 0,07 | 0,04 de RS com 96% de erro no DevBench, inválido.
- GPT-4: 0,97; 0,82; 0,02 | 0,97; 0,83; −0,13.
- GPT-4-Turbo: 0,94; 0,75; 0,02 | 0,97; 0,79; 0,16.
- GPT-4o: 1,00; 0,76; −0,12 | 0,98; 0,80; −0,12 | lista 0,68; 0,18.
- GPT-3.5-Turbo: 0,96; 0,70; 0,06 | 0,99; 0,76; −0,02 | lista 0,34; −0,05 (erro 0,12).
- o1-mini: 0,90; 0,76; −0,04 | 0,93; 0,84; −0,07.
- Llama-3.3-70B: 0,96; 0,80; −0,05 | 0,99; 0,89; −0,03.
- Llama-3.1-405B: 0,93; 0,77; 0,10 (erro 0,02) | 0,94; 0,79; 0,01.
- Llama-3.1-8B: 0,75; 0,69; −0,03 (erro 0,25) | 0,79; 0,47; 0,25.

Lidos na tabela: os quatro juízes Claude têm PF positivo (pendem para a segunda posição, a recência) nos dois benchmarks; os maiores PC em pares são do Llama-3.3-70B no DevBench (0,89), de Gemini-1.5-pro e o1-mini no DevBench (0,84) e de GPT-4 e Claude-3.5-Sonnet no MTBench (0,82). Mesmo os melhores juízes mudam de vencedor com a troca de ordem em cerca de 11% a 18% dos pares.

**Tabela 3 (abertos, apêndice; PC, PF, RS no MTBench | no DevBench):** GPT-OSS-20B 0,79, −0,04, 0,89 | 0,84, −0,04, 0,81; Gemma-3n-E4B 0,68, −0,07, 0,90 | 0,41, 0,40, 0,93; Llama-4-Scout-17B 0,79, 0,05, 0,95 | 0,12, 0,88, 0,98; Mistral-Small-24B 0,72, −0,02, 0,87 | 0,57, 0,27, 0,82; Qwen2.5-72B 0,77, −0,01, 0,94 | 0,81, 0,11, 0,93; Qwen2.5-Coder-32B 0,74, 0,01, 0,91 | 0,81, 0,09, 0,92; Qwen2.5-7B 0,55, −0,21, 0,87 | 0,54, −0,45, 0,93. O Llama-4-Scout é o caso extremo: estável na repetição (0,98) e quase sempre com a segunda posição no DevBench (PC 0,12, PF 0,88), o que ilustra que estabilidade não é justiça.

**Achado 1, o viés não é acaso:** os juízes capazes, com erro de formato mínimo, têm RS acima de 0,85 em geral; Claude-3.5-Sonnet, GPT-4 e Llama-3.3-70B passam de 0,95 nos dois benchmarks. Para os autores, isso dá confiança de que um julgamento único desses juízes já reflete a capacidade deles, e de que o viés medido é sistemático.

**Achado 2, varia por juiz e por tarefa:** o GPT-4o é mais consistente que o GPT-4 em código, menos nas outras tarefas; o Gemini-1.5-pro supera os outros Gemini na maioria das tarefas, mas empata em extração. A direção também muda: o GPT-4 e o GPT-3.5-Turbo pendem para a recência no MTBench e para a primazia no DevBench; o Claude-3.5-Sonnet é quase justo no MTBench (PF 0,01) e pende forte para a recência no DevBench (0,22). PC mais alto costuma vir com PF mais justo (a curva de regressão da Figura 2c), mas não garante: há juízes com PC alto e direção marcada, que muda de tarefa para tarefa. Na lista, os capazes (GPT-4o, Claude-3.5-Sonnet) mantêm consistência alta; o GPT-3.5-Turbo despenca (de 0,70 em pares para 0,34 na lista). No DevBench (Figura 6), GPT-4-Turbo, GPT-4o e Gemini-1.5-pro superam o GPT-4 no desenho de arquitetura, e o GPT-4 segue o melhor na sequência UML. A regressão confirma juiz e categoria de tarefa como preditores significativos de PC e PF.

**Achado 3, a diferença de qualidade comanda a consistência:** nas Figuras 2(e) (pares) e 2(f) (lista), a PC em função da taxa de vitória geral tem forma de parábola: alta perto de 0 e de 1 (uma resposta claramente melhor) e mínima perto da linha de base (no gráfico de pares a curva de regressão desce a cerca de 0,6 perto de owr = 0,5, leitura da figura). Respostas de qualidade parecida são difíceis de julgar e aumentam a chance de o viés decidir. A mesma relação aparece para cada juiz e nos dois benchmarks (Figura 5a). A PF também melhora com a diferença de qualidade, mas menos e não para todos: a PF dos GPT fica perto de 0 qualquer que seja a diferença (curva quase reta), enquanto Claude-3-Opus, Claude-3-Sonnet e os Gemini-pro mostram a parábola nítida no MTBench (Figura 5b). As exceções são comuns nos pontos individuais, então outros fatores também pesam.

**Achado 4, o comprimento pesa pouco:** só o comprimento médio da resposta do candidato entra como preditor significativo, e só para a PF, com mudança mínima de AIC (Tabela 5, os dois benchmarks juntos: AIC −16.103 no modelo completo e −16.088 sem o comprimento). Para os autores não surpreende: resposta mais longa costuma ser vista como melhor.

**Tabelas da regressão (apêndice E; quanto mais o AIC sobe ao tirar a variável, mais ela importa):** PC nos dois benchmarks (Tabela 4): completo −18.370; sem tarefa −18.319; sem candidato −18.303; sem diferença de qualidade −17.703; sem juiz −16.846. PF nos dois (Tabela 5): completo −16.103; sem comprimento da saída −16.088; sem diferença de qualidade −15.873; sem tarefa −15.817; sem juiz −14.641. No MTBench isolado, a PC perde mais sem juiz e sem diferença de qualidade (Tabela 6: −12.594 e −12.559 contra −13.312), e a PF perde mais sem juiz (Tabela 7: −9.672,5 contra −10.909,2). No DevBench (Tabelas 8 e 9), o juiz domina a PC (−5.146,6 contra −6.940,2) e a PF (−5.108,9 contra −6.753,9), com a diferença de qualidade em segundo na PC (−6.525,3).

## 5. Concordância entre juízes (seção 4 e apêndice C)

- **Concordância mútua (Figura 4, mapas de calor):** dois juízes concordam numa instância quando dão a mesma escolha. Mesmo com PC e PF médios parecidos, os juízes divergem muito instância a instância. Há "padrões de família": GPT-4, GPT-4-Turbo e GPT-4o concordam mais de 70% com empates e mais de 85% sem empates no MTBench; o GPT-3.5-Turbo discorda dos GPT-4 e do o1-mini em cerca de 40% das instâncias. Claude-3-Opus concorda muito com Claude-3.5-Sonnet (capacidade parecida) e com Claude-3-Sonnet (mesma série), mas Claude-3.5-Sonnet e Claude-3-Sonnet não concordam tanto entre si, sinal de que a passagem da série 3 para a 3.5 mudou o modo de julgar. Os Gemini concordam pouco entre si, e o 1.5-pro se alinha mais com os GPT-4 e com o Claude-3-Opus. Os Llama grandes concordam entre si e com os GPT; o 8B não. Conclusão dos autores: os juízes se agrupam primeiro por capacidade e, com capacidade comparável, os da mesma família concordam mais entre si do que com os de outras famílias.
- **Discordância:** número de julgamentos diferentes da moda numa instância. No MTBench (Figura 3), 19,1% das instâncias têm discordância zero, 54,8% até 3 (mais de 80% dos 15 juízes de acordo), 85,3% até 6, 94,7% até 7 e 98,4% até 8. O texto diz que menos de 2% são as instâncias "especialmente difíceis" com discordância 8 ou mais, mas pela figura a fração com 8 ou mais é de 5,3% (o que fica abaixo de 2% é a de 9 ou mais); o apêndice fala em menos de 5% de instâncias mais difíceis nos dois benchmarks. No DevBench (Figura 4d, 14 juízes, porque o Gemini-1.5-flash saiu por erro), 10,1% com zero, 60,8% até 3 e 95,2% até 6, de um máximo de 7.
- **Leitura dos autores:** as instâncias de consenso são as fáceis, e nelas o voto da maioria de juízes capazes é confiável; segundo eles, o voto da maioria serviria em mais de 95% das instâncias dos dois benchmarks. As mais difíceis têm três marcas: muita discordância entre juízes, taxas de vitória próximas (diferença de qualidade mínima) e viés de posição na maioria dos juízes. Usos práticos: controlar a dificuldade de um benchmark dosando instâncias fáceis e difíceis; filtrar instâncias em que o voto de vários juízes dispensa o rótulo humano; e estudar as instâncias de discordância para mitigar o viés.

## 6. Regras, recomendações e limites declarados

- Ao avaliar ou escolher um juiz, medir as duas coisas, consistência e justiça, e considerar a variação por tarefa; a escolha depende da tarefa e do equilíbrio entre consistência, justiça e custo (a v1 destacava que modelos mais baratos às vezes igualam ou superam o GPT-4 em tarefas específicas).
- Em estudos de juízes, controlar a diferença de qualidade entre as respostas, porque ela confunde a medida do viés.
- Se o julgamento único de um juiz não basta, usar vários juízes capazes com voto da maioria.
- O trabalho mede o viés com a troca de posição e conta a inconsistência como empate (o que os autores chamam de "inconsistency-as-a-tie"), mas não propõe nem testa mitigação; deixa explícito que o caso mais difícil, manter consistência e justiça quando a diferença de qualidade é mínima, fica para pesquisa futura.
- **Limites:** 12 juízes fechados em pares e 4 em lista, e listas só de três candidatos; poucos abertos (só três Llama 3.1 ou mais novos, porque os menores não tinham janela de contexto suficiente); só os prompts originais dos benchmarks; os fatores do juiz (arquitetura, tamanho) aproximados pela família; análise post hoc, sem estimar ou controlar os fatores antes de julgar; foco em medir, não em mitigar; sem análise multivariada das interações entre comprimento, complexidade e diferença de qualidade.

## 7. Tudo o mais que ensina

- **Mitigações citadas e seus problemas (apêndice B.2):** descartar os julgamentos inconsistentes não resolve e gera escassez de dados quando o viés é frequente; contar a inconsistência como empate para os dois candidatos (Zheng et al.; Li et al., PRD) é útil na prática mas não reduz o viés; bootstrapping (Hou et al.), split-and-merge (Li et al., 2023 e EMNLP 2024), discussão multiagente (Li et al., PRD; Khan et al., debate com modelos mais persuasivos) funcionam em parte, mas são caros, lentos ou insuficientes; abordagens mecanísticas que mexem em embeddings de posição e na atenção causal (Wang et al., ICLR 2025; Yu et al., 2025) eliminam o viés, mas exigem acesso ao modelo e não servem para modelos fechados. Outras citadas na introdução: mitigação incompleta (Guo et al.), complexidade (Chua et al., treino de consistência aumentado por viés), viés novo introduzido (Ohi et al., mitigação por verossimilhança), efetividade inconsistente (Gallegos et al.).
- **Fator de qualidade em trabalho anterior:** Wang et al. (2023, "Large Language Models are not Fair Evaluators") acharam que a taxa de conflito sob troca cai quando a diferença de nota entre as respostas cresce, no cenário de notas; este artigo leva a ideia para a comparação direta.
- **Repetição e moda:** usar várias repetições e a moda do julgamento (Chen et al., 2024, MLLM-as-a-Judge) é robusto, mas caro; a RS alta é o argumento dos autores para dispensar isso nos juízes capazes.
- **Paradigmas de juiz (B.1):** por item (pointwise), em pares e em lista; por nota ou por relação (comparação, ranking); arranjos multiagente (ChatEval, PRD) e meta-juízes (meta-rewarding, Li et al. 2025). A comparação em pares é tida como o cenário em que os juízes funcionam melhor; ranking de lista completa cresce em custo e perde desempenho, e "escolher o melhor de n" é uma necessidade mais simples e comum.
- **Definições úteis:** primazia (preferir a primeira posição) e recência (preferir a segunda ou posterior), termos que os autores propõem no lugar de "viés para o primeiro ou segundo candidato".
- **Trabalho irmão do mesmo grupo:** Ma et al. 2025, "Judging with many minds: Do more perspectives mean less prejudice?" (arXiv 2505.19477), sobre vieses em juízes multiagente.
- **AIC:** AIC = 2k − 2 log(L); com erros normais, o termo de ajuste vira a soma dos resíduos ao quadrado; a seleção stepwise para quando nem tirar nem pôr variável baixa o AIC.

---

## Onde está o integral
Não entra aqui: a licença não permite uso comercial, e o repositório serve a um negócio (regra em `knowledge/sources/README.md`). O texto integral está em https://arxiv.org/abs/2406.07791 (PDF e HTML na própria página). A ficha acima é o que as sínteses citam.
