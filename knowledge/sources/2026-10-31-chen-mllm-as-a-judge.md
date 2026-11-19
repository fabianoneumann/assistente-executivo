---
titulo: "MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark"
tipo: paper
autor: "Dongping Chen, Ruoxi Chen, Shilin Zhang, Yaochen Wang, Yinuo Liu, Huichi Zhou, Qihui Zhang, Yao Wan, Pan Zhou, Lichao Sun"
url: "https://arxiv.org/abs/2402.04788"
publicado_em: 2024-02-07
capturado_em: 2026-10-31
licenca: "CC BY 4.0 (indicada na página do arXiv, link para creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [mllm-as-judge, pairwise-comparison, score-rating, batch-ranking, position-bias, egocentric-bias, verbosity-bias, judge-hallucination, judge-consistency, chain-of-thought, vision-description]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 07/02/2024, v2 em 06/06/2024 e v3 em 11/06/2024; lida a v3. Comentário do arXiv: "ICML 2024 (Oral)"; o PDF traz o rodapé dos anais (Proceedings of the 41st International Conference on Machine Learning, Viena, PMLR 235, 2024). Autores da Huazhong University of Science and Technology, da Zhejiang University of Technology e do LAIR Lab da Lehigh University; os sete primeiros com contribuição igual; correspondência com Yao Wan e Pan Zhou. Código e dados em https://mllm-judge.github.io/. A v3 inclui quatro conjuntos e modelos acrescentados na réplica aos revisores (Mind2Web, ScienceQA, AesBench, MM-Vet; LLaVA-1.6 e Qwen-VL), o que explica números de modelos e conjuntos diferentes entre seções. Texto extraído do PDF da v3 com `pdftotext`; as Tabelas 2 e 3 e as Figuras 19 e 20 foram conferidas na página renderizada. Lido para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Atenção:** o que os juízes avaliam aqui são **respostas em texto** de modelos a uma pergunta sobre uma imagem (legenda, matemática, gráfico, leitura de texto, infográfico), não imagens geradas nem designs. Nos pares, as duas respostas são texto sobre a mesma imagem.

## 1. A pergunta

Modelos multimodais (MLLMs) servem de juiz de tarefas visuais, e quão perto ficam da preferência humana? O artigo leva a ideia de LLM-as-a-Judge (Zheng et al. 2023, MT-Bench) para o domínio multimodal e compara três formatos de julgamento: nota de 1 a 5 para uma resposta, comparação em pares (com opção de empate) e ordenação de um lote de respostas (sem empate).

## 2. O método

- **Passo 1, pares de imagem e instrução:** 4.414 instruções sobre 4.114 imagens, 300 de cada conjunto (600 no MathVista, com e sem dica), de 14 conjuntos: MS COCO (cena real), Conceptual Captions, DiffusionDB (imagens de difusão), InfographicVQA (rótulo "Graphics"), MathVista, TextVQA, WIT (texto multilíngue), ChartQA, VisIT-Bench, CC-3M, e na réplica Mind2Web (páginas web), ScienceQA, AesBench (percepção estética) e MM-Vet; mais o Mementos (sequências de imagens) num experimento à parte.
- **Passo 2, respostas:** GPT-4V, Gemini (Pro Vision), LLaVA-1.5-13b, CogVLM e, depois, Qwen-VL-Max e LLaVA-1.6-34b respondem; cerca de 17 mil respostas (17.096 na Tabela 1; 17.656 no apêndice), com as recusas e as curtas demais excluídas. As respostas são divididas em três grupos sem sobreposição, um para cada formato.
- **Passo 3, julgamento e anotação humana:** onze MLLMs julgam (GPT-4V, Gemini-Pro-Vision 1.0 e 1.5, LLaVA-1.5-13b, LLaVA-1.6 de 7, 13 e 34b, Qwen-VL-Plus, Max e Chat, CogVLM). Os capazes fazem "analisar e depois julgar" (CoT de um passo: análise e depois a decisão, em JSON); LLaVA e CogVLM julgam direto. Seis autores anotam de forma independente, instruídos a ignorar tamanho, nome e posição das respostas, com validação cruzada.
- **Configurações extras:** sem a imagem; com a imagem trocada por uma descrição detalhada feita pelo GPT-4V ("especialista de visão"), testando também LLMs só de texto (GPT-4, LLaMA-2-70b, Mixtral-8x7b, GPT-3.5); e CoT de três passos.
- **Métricas:** nota, correlação de Pearson com a nota humana por conjunto; pares, acurácia (mais F1 e revocação) com e sem empate; lote, distância de Levenshtein normalizada entre as ordens (menor é melhor). As três métricas são diferentes, e o artigo compara os formatos por elas. Tudo amostrado três vezes e tirada a média.
- **Concordância humana com o juiz:** humanos dizem sim ou não para cada julgamento do modelo, dão nota de 1 a 5 à análise do juiz e marcam alucinações (com uma árvore de decisão). Cada julgamento revisto três vezes por anotadores diferentes.
- **Hiperparâmetros:** GPT-4V como juiz com temperatura 0,9 e top-p 0,9 (seguindo Chiang e Lee 2023), sem o "JSON mode" (num teste com 50 casos e três anotadores, os humanos preferiram a saída sem ele), reamostrando em erro de formato ou recusa; Gemini com os padrões, e às vezes respondendo em chinês ou japonês a perguntas em inglês.

## 3. Resultados: o juiz contra os humanos (Tabela 2, médias nos 14 conjuntos)

- **Nota (Pearson):** GPT-4V 0,490; Gemini 0,304; LLaVA-1.5-13b 0,225; LLaVA-1.6-34b 0,184; Qwen-VL-Max 0,170.
- **Pares com empate (acurácia):** GPT-4V 0,636; Gemini 0,509; LLaVA-1.6-34b 0,460; Qwen-VL-Max 0,438; LLaVA-1.5-13b 0,384.
- **Pares sem empate:** GPT-4V 0,773; LLaVA-1.6-34b 0,648; Qwen-VL-Max 0,644; Gemini 0,615; LLaVA-1.5-13b 0,504.
- **Lote (Levenshtein, menor é melhor):** GPT-4V 0,361; Gemini 0,432; Qwen-VL-Max 0,486; LLaVA-1.6-34b 0,501; LLaVA-1.5-13b 0,597.

Por conjunto, o GPT-4V passa de 0,8 sem empate em vários (COCO 0,804, Conceptual Captions 0,870, Diffusion 0,922, InfographicVQA 0,807, MathVista 0,801, TextVQA 0,805, ChartQA 0,849); na nota, vai de 0,185 (Mind2Web) a 0,645 (InfographicVQA e ChartQA). **No AesBench (estética):** nota 0,401 no GPT-4V contra 0,414 no LLaVA-1.5-13b e 0,360 no Gemini; pares com empate 0,606 (GPT-4V) e 0,190 (Gemini); sem empate 0,755 (GPT-4V), 0,741 (Qwen-VL-Max) e 0,265 (Gemini). O Gemini foi omitido no conjunto de difusão por não processar imagens geradas por IA.

**A conclusão principal:** os MLLMs se alinham aos humanos nos pares, e divergem bastante na nota e na ordenação. Causas apontadas:
- **Viés de nota alta:** Gemini, LLaVA e CogVLM dão quase sempre perto de 4, raramente 1 ou 2; Qwen-VL dá 80% das notas entre 4 e 5. Os autores comparam ao viés de "sim" e atribuem a desequilíbrio entre instruções positivas e negativas no treino. As notas do GPT-4V são mais distribuídas e mais próximas das humanas (Figura 4).
- **Empate:** Gemini, LLaVA e CogVLM quase sempre declaram um vencedor; o GPT-4V declara empate com frequência parecida com a dos humanos, sugerindo limiar de empate semelhante.
- **Ordenação:** o CogVLM não consegue ordenar (só aponta o primeiro); o LLaVA copia a sequência do exemplo do prompt.

## 4. Consistência e concordância humana

- **Consistência em seis repetições (Tabela 4; média ponderada e critério de maioria, MCC = mais da metade das seis respostas iguais):** GPT-4V nota 0,796 e 0,611, pares 0,836 e 0,675, lote 0,679 e 0,418; Gemini nota 0,531 e 0,054, pares 0,781 e 0,547, lote 0,629 e 0,338. Os pares são o formato mais estável; a nota do Gemini quase nunca se repete por maioria. O GPT-4V roda com temperatura mais alta e ainda assim é mais consistente.
- **Concordância humana (Tabela 3, 10 conjuntos):** GPT-4V em torno de 70% nas três configurações, com o pico nos pares (79,3% na média da tabela, contra 72,4% do Gemini; 92,6% em Conceptual Captions; o mesmo parágrafo do texto fala também em 78% e 72%, sem explicar a diferença); na nota, 70% em média e 79,9% no COCO, contra 67,7% do Gemini. Na ordenação, os dois caem, sobretudo em matemática e infográficos. O desvio absoluto médio das notas que os humanos dão à análise do juiz é menor no GPT-4V (Figura 18).
- **Variação entre anotadores (dez anotadores, 50 julgamentos em pares):** pouca divergência ao decidir se o julgamento do modelo está certo, mais divergência ao dar nota à análise; quase unanimidade ao marcar alucinação, graças à árvore de decisão bem definida.

## 5. CoT de mais passos não ajuda (Tabela 5)

CoT de três passos (imagem e instrução, imagem, instrução) num subconjunto: GPT-4V nota de 0,557 para 0,299, pares com empate de 0,683 para 0,563, sem empate de 0,806 para 0,728, lote de 0,325 para 0,419 (pior); Gemini cai mais (nota 0,299 para 0,144; sem empate 0,723 para 0,377). Mais passos reduzem a alucinação, mas não aproximam dos humanos e muitas vezes pioram, porque a leitura da figura e a própria resposta do juiz à pergunta contaminam a decisão quando há alucinação no começo da cadeia.

## 6. Ver ajuda, mas descrição detalhada ajuda mais (Tabela 6)

Juízes sem imagem ou com descrição detalhada do GPT-4V (nota; pares com e sem empate; lote):
- GPT-4V com descrição: 0,435; 0,544; 0,878; 0,400. Sem visão: 0,299; 0,491; 0,868; 0,394.
- Gemini com descrição: 0,120; 0,438; 0,785; 0,472. Sem visão: 0,108; 0,433; 0,758; 0,470.
- GPT-3.5: 0,154; 0,453; 0,591; 0,473 com descrição; 0,223; 0,459; 0,644; 0,504 sem.
- LLaMA2-70b e Mixtral-8x7b ficam abaixo de 0,16 na nota em qualquer caso.

A descrição melhora a nota do GPT-4V (0,435 contra 0,299 sem visão), e nos pares sem empate a versão com descrição (0,878) supera o desempenho padrão com imagem (0,773). Os autores leem que MLLMs podem não ter certas capacidades de julgamento humanas e que LLMs podem julgar tarefas multimodais quando recebem descrições completas. Essas configurações rodaram numa amostra de 10% (Tabela 1).

## 7. Vieses e alucinação (seção 4.6)

- **Egocêntrico (autopreferência):** o GPT-4V mostra "a slight degree of Egocentricity"; o Gemini distribui notas de modo uniforme entre as fontes. O exemplo dado é de alinhamento a valores do próprio treino: o GPT-4V valoriza privacidade e dá notas mais altas a respostas que a preservam. Nas Figuras 19 e 20, a distribuição de notas e de escolhas do GPT-4V sobre as próprias respostas fica próxima da humana (nas escolhas sem empate, cerca de 43% para as respostas do GPT-4V contra cerca de 44% dos humanos).
- **Posição:** LLaVA e CogVLM preferem consistentemente uma posição nos pares (o LLaVA costuma dar "A"); no lote, o LLaVA copia a sequência "ABCD" do exemplo do prompt em 88,2% das respostas. Os autores atribuem isso à dificuldade de seguir instruções complexas e dizem que mais exemplos no prompt reduzem o efeito. O Qwen-VL-Max mostra menos viés de posição que os LLaVA. O artigo não relata troca sistemática de ordem nos pares nem mede o viés de posição do GPT-4V; o prompt só pede para evitá-lo.
- **Tamanho (verbosidade):** GPT-4V e Gemini dão notas maiores a respostas mais longas (Figura 6). Num experimento, o GPT-4 sem visão alongou respostas sem mudar o sentido, e as notas subiram em média 0,6 ponto (GPT-4V) e 0,75 (Gemini) na escala de 1 a 5 (Figura 7).
- **Alucinação:** mais frequente na ordenação em lote (textos mais longos), com leitura errada da imagem e erros de recuperação. No subconjunto difícil, acrescentar passos de raciocínio antes de "analisar e julgar" reduz as alucinações em todos os formatos (Tabela 7, redução por passo acrescentado, imagem e instrução, só imagem, só instrução): nota 46,15%, 48,72%, 33,33%; pares 28,21%, 35,90%, 33,33%; lote 43,59%, 35,90%, 35,90%. Os maiores ganhos vêm dos passos sobre a imagem.
- **Escala:** nas séries LLaVA-1.6 e Qwen, modelos maiores julgam melhor ("scaling law"), mais claramente na ordenação.

## 8. Conjuntos liberados e direções

- **MLLM-AS-A-JUDGE-HQ:** respostas com alta concordância com o julgamento humano. **MLLM-AS-A-JUDGE-HARD:** respostas com inconsistência e alucinação, para testes difíceis.
- **Direções:** usar as anotações humanas (notas e preferências em pares) para treinar modelos de recompensa e DPO multimodal; debate entre agentes como juiz; atacar o viés de posição e a tendência a notas altas; humano no laço, por exemplo chamar uma pessoa quando mais da metade das repetições discorda ou quando a saída foge do formato.
- **A recomendação geral:** os MLLMs, mesmo o GPT-4V, precisam melhorar antes de serem tratados como avaliadores totalmente confiáveis; o artigo pede mais trabalho na área.

## 9. Tudo o mais que ensina

- **Sequências de imagens (Mementos, Tabela 10):** GPT-4V nota 0,361, pares 0,721 e 0,836, lote 0,411; o Video-LLM ChatUnivi gera boas respostas mas não sabe julgar (nota −0,094, pares 0,158 e 0,168).
- **Os prompts (apêndice F)** seguem Chiang e Lee (2023) e Li et al. (2024): papel ("assistente proficiente em problemas de raciocínio visual"), instrução de juiz imparcial, critérios (relevância, acurácia, abrangência, criatividade, granularidade), avisos ("Do not allow the length of the responses to influence your evaluation. Do not favor certain names or positions") e formato. A rubrica de nota descreve cada nível de 1 (Poor) a 5 (Excellent). Nos pares, "[[A]]", "[[B]]" ou "[[C]]" para empate, com a chave de análise antes.
- **Estudos de caso (apêndice G):** um juiz dá 5 a uma resposta que dá o propósito errado do trem (brinquedo para crianças) com elogios genéricos; noutro, o GPT-4V prefere a resposta com um dado a mais (o segundo colocado) quando as duas estão certas, e o Gemini declara empate; no lote, o GPT-4V nota que uma resposta citou errado a data da revista ("1 Giugno" em vez de "10 Giugno") e a põe em último, enquanto o Gemini ordena pela quantidade de detalhe.
- **Trabalhos relacionados:** JudgeLM (LLM ajustado para julgar), AUTO-J (pares e nota única), LLM-as-a-Judge e MT-Bench (Zheng et al. 2023), viés de posição (Zheng et al. 2023; Wang et al. 2024), autopreferência (Li et al. 2024), verbosidade (Saito et al. 2023), alucinação multimodal (Liu et al. 2023; Cui et al. 2023), viés de posição em múltipla escolha humana (Blunch 1984) e o "centro de desatenção" (Raghubir e Valenzuela 2006).

---
