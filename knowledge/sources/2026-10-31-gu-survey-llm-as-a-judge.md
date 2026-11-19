---
titulo: "A Survey on LLM-as-a-Judge"
tipo: paper
autor: "Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen et al."
url: "https://arxiv.org/abs/2411.15594"
publicado_em: 2024-11-23
capturado_em: 2026-10-31
licenca: "CC0 1.0, dedicação ao domínio público (indicada na página do arXiv, link creativecommons.org/publicdomain/zero/1.0); a versão publicada na revista The Innovation (DOI 10.1016/j.xinn.2025.101253) é CC BY-NC-ND e não foi a usada"
areas: [agent-engineering]
tags: [llm-as-judge, survey, reliability, position-bias, self-enhancement-bias, length-bias, adversarial-robustness, meta-evaluation, majority-voting, evaluation-drift, pairwise-comparison, reasoning-models]
---

Ficha em palavras próprias; o texto integral (licença CC0 1.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: seis versões (v1 em 23/11/2024, v2 em 16/12/2024, v3 em 09/01/2025, v4 em 01/02/2025, v5 em 09/03/2025, v6 em 19/10/2025); lida a v6, 64 páginas. A página do arXiv lista 16 autores; o PDF da v6 lista 18 (acrescenta Zhouchi Lin e Bowen Zhang), da IDEA Research (International Digital Economy Academy), Sun Yat-sen, DataArc, Instituto de Tecnologia da Computação da Academia Chinesa de Ciências, Imperial College London, Renmin, HKUST e Universidade de Pequim; autores correspondentes Yuanzhuo Wang e Jian Guo. Página do projeto e lista de recursos em https://awesome-llm-as-a-judge.github.io/. O OpenAlex registra uma versão publicada na revista The Innovation (Cell Press), com data de 10/01/2026 e licença CC BY-NC-ND, e uma cópia no PubMed Central; essa versão não foi lida. O texto foi extraído com `pdftotext -layout`; as Tabelas 2, 3 e 4 foram lidas na página renderizada (o texto extraído as embaralha). Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Atenção:** é uma survey; a maior parte dos achados é dos trabalhos citados, que a ficha aponta pelo número de referência do artigo quando útil. O único experimento próprio é a meta-avaliação da seção 4.4.

## O resumo

Avaliar com precisão e consistência é difícil por subjetividade, variabilidade e escala. O "LLM-as-a-Judge" usa LLMs como avaliadores de tarefas complexas, unindo a escala das métricas automáticas ao raciocínio contextual do especialista. A survey dá uma definição formal e uma classificação, e se organiza em torno da pergunta "como construir sistemas LLM-as-a-Judge confiáveis?": estratégias para melhorar a consistência, mitigar vieses e adaptar a cenários; métodos para avaliar a confiabilidade do juiz, com um benchmark de meta-avaliação; aplicações, desafios e direções futuras.

## 1. Definições

- **Formal básica:** E ← P_LLM(x ⊕ C). E é a avaliação final (nota, escolha, rótulo ou frase); P_LLM é a função de probabilidade do modelo, autorregressiva; x é o que se avalia (texto, imagem, vídeo); C é o contexto (template de prompt, histórico); ⊕ é a combinação, que pode pôr x no começo, meio ou fim.
- **Formal com confiabilidade:** R ← F_R(P_LLM, x, C), em que F_R é o conjunto de restrições e validações (mitigar vieses, controlar variabilidade, confirmar robustez a entradas adversariais) aplicado sobre o pipeline básico. A confiabilidade é função de três variáveis: o modelo (viés e instabilidade internos), a entrada (ruído ou perturbação) e o contexto (mudanças de redação ou de ordem no prompt mudam o julgamento).
- **Papéis cobertos:** avaliador de nota, avaliador, crítico, verificador, examinador, modelo de recompensa e de ranking.
- Abre com Kant: julgar é pensar o particular como contido no universal, isto é, decidir se algo cai sob uma regra.

## 2. Como usar: o pipeline (seção 2)

**Aprendizado em contexto: quatro formatos de prompt.**
- **Gerar nota:** discreta (1 a 3, 1 a 5, 1 a 10) ou contínua (0 a 1, 0 a 100); com só a faixa e os critérios, ou com critérios detalhados (Likert por dimensão e nota geral, como no Language-Model-as-an-Examiner: quatro dimensões de 1 a 3 e nota geral de 1 a 5).
- **Sim ou não:** comum em etapas intermediárias e laços de autoaperfeiçoamento (Reflexion; frases como "Modification needed." e "No modification needed.").
- **Comparação em pares:** avaliação relativa; modos de duas opções, de três (com empate) e de quatro (empate "ambos bons" e empate "ambos ruins"). Os autores citam que LLM e humanos se alinham mais em pares do que em notas (Liu et al. [95]) e que pares superam outros métodos em consistência de posição.
- **Múltipla escolha:** mais rara.
- **Riscos declarados:** pequenas mudanças de prompt mudam o resultado; notas têm confiabilidade entre avaliadores inconsistente pela aleatoriedade da geração e sensibilidade à redação; sim/não e múltipla escolha têm ambiguidade de interpretação; vieses de posição e tamanho.

**Escolha do modelo.** Modelo geral forte (GPT-4) ou modelo ajustado como juiz (PandaLM, JudgeLM, Auto-J, Prometheus). Ajustar segue três passos: coletar dados (instruções, objetos avaliados, avaliações de GPT-4 ou de humanos), desenhar o prompt e fazer ajuste por instrução. Riscos: caixa-preta e dependência de versão do modelo comercial (reprodutibilidade); juízes ajustados sobreajustam e generalizam mal fora dos dados de treino, e herdam vieses deles; modelos pequenos abertos podem divergir de humanos.

**Pós-processamento.** Extrair tokens por regra (frágil a variações de formato; decodificação restrita por máquina de estados finitos garante sintaxe mas pode distorcer a distribuição e degradar a saída; DOMINO, XGrammar e SGLang reduzem o custo); normalizar logits para obter uma nota contínua (probabilidade do "Yes"); selecionar frases. Riscos: erros silenciosos na extração; normalização sensível ao prompt e à tokenização; seleção por sentença pode propagar viés se o juiz reage a estilo mais que a substância; todo pós-processamento é vulnerável a manipulação que infla a nota sem melhorar o conteúdo.

**Quatro cenários:** juiz de modelos, de dados (anotação, recompensa, filtragem; risco de amplificar vieses no pseudo-rótulo), de agentes (o juiz como agente inteiro ou numa etapa; erros iniciais se acumulam em cascata) e de raciocínio (recompensa no treino, escolha do melhor caminho no teste, como em Best-of-N; risco de avaliações confiantes mas erradas).

**Prática rápida (Figura 8):** pensar (o que avaliar, como humanos avaliam, há exemplos confiáveis?), desenhar o prompt (dimensões de nota, comparação relativa, exemplos), escolher um modelo grande com bom raciocínio e bom seguimento de instrução, padronizar a saída (\boxed{XX}, nota numérica, sim/não) e testar com casos e retestar.

## 3. Como melhorar (seção 3)

**Desenho do prompt.**
- Few-shot (FActScore, SALAD-Bench, GPTScore).
- Decompor os passos da avaliação (G-Eval e DHP com CoT; SocREval com o método socrático) ou os critérios (Branch-Solve-Merge, HD-Eval com decomposição hierárquica alinhada a preferências humanas, Hu e Gao com 11 critérios definidos para o juiz não confundir padrões).
- Contra o viés de posição: trocar a ordem e tirar a média das notas (Wang et al. [155]), embaralhar (Auto-J, JudgeLM) ou marcar empate quando a troca muda o veredito (PandaLM).
- Converter nota em comparação: como a nota absoluta é menos robusta que a comparação relativa [116], Liu et al. [95] propõem o PARIS (comparações locais em pares, ranking global), mais alinhado a humanos; a nota única é mais suscetível a variação de prompt e aleatoriedade.
- Padronizar a saída: preencher formulário "X: Y" (G-Eval, DHP), JSON (LLM-EVAL); pedir nota com explicação (CLAIR, 0 a 100 com razões em JSON; FLEUR pergunta "Why?" depois da nota).

**Capacidade do modelo.** Ajuste fino especializado com dados de meta-avaliação por template (PandaLM, SALAD-Bench) ou por transformação profunda: OffsetBias gera versões fora do tema da entrada para produzir respostas ruins e reduz vieses de tamanho, concretude e conhecimento; JudgeLM com referência presente e removida; CritiqueLLM; Yu et al. com GPT-4o analisando pares sintéticos. Refinamento iterativo por feedback: INSTRUCTSCORE (modos de falha e feedback do GPT-4), JADE (humanos corrigem e os casos mais corrigidos viram exemplos few-shot), Think-J (offline com crítico, online com GRPO e recompensa por regra).

**Saída final.** Integrar várias fontes: várias rodadas com média (Sottana et al.; PsychoBench, média e desvio de dez rodadas), vários juízes com voto (CPAD), revisão por pares descentralizada entre os próprios modelos (Bai et al.), detecção de conflito por limiar de diferença e voto da maioria (EvalMORAAL), avaliação em cascata do modelo fraco ao forte por confiança (Jung et al., Cascaded Selective Evaluation), avaliação comparativa com respostas de "multidão" geradas por vários LLMs. Otimizar a saída direta: suavizar a nota pela probabilidade de cada dígito (FLEUR, G-Eval, DHP; TrustJudge com expectativa contínua e agregação por probabilidades bidirecionais), o que exige acesso às probabilidades; autoverificação (TrueTeacher pergunta ao juiz sobre a certeza e guarda só o que passa).

## 4. Como avaliar o juiz: concordância, viés, robustez (seção 4)

**Concordância com humanos:** porcentagem de concordância, kappa de Cohen, correlação de Spearman, ou precisão e revocação tratando o humano como rótulo. Tabela 1, benchmarks de meta-avaliação (ano; tamanho; formato; tipos de viés cobertos): MTBench (2023; 80; pares; 3), Chatbot Arena (2023; 30 mil; pares; 3), FairEval (80; pares; 1), PandaLM (pares; 0), LLMEval2 (2.553; pares; 0), Shepherd (1.317; nota; 0), EvalBiasBench (80; pares; 6), CALM (2024; 4.356; pares e nota; 12, sem concordância humana), JudgeBench, MLLM-as-a-Judge (30 mil), CodeJudge (1.860), KUDGE (3.324). Os autores apontam falta de meta-avaliação do juiz usado para anotar dados em larga escala.

**Vieses, em duas classes.** A taxonomia separa os vieses do LLM em qualquer tarefa (mais fundamentais, que dependem de avanços no modelo base) dos específicos do julgamento (ligados ao formato da tarefa, tratáveis por desenho específico e que não somem naturalmente com modelos melhores).
- **Independentes da tarefa:**
  - **Diversidade:** contra grupos demográficos (gênero, raça, orientação sexual), por exemplo dar nota maior a respostas que reforçam estereótipos.
  - **Cultural:** expressões de culturas pouco familiares recebem notas piores.
  - **Autoaprimoramento:** o juiz prefere respostas geradas por ele mesmo [CALM, MT-Bench]; também chamado de viés de fonte em recuperação e QA. Recomendação de não usar o mesmo modelo como avaliador, com a ressalva dos autores de que isso "is only a stopgap", porque pode impedir de usar o melhor avaliador ao avaliar os modelos mais avançados.
- **Específicos do julgamento:**
  - **Posição:** com o ChatGPT como juiz, o Vicuna-13B supera o ChatGPT só por ficar na segunda posição [155]. Métricas: consistência de posição e justiça de preferência (Shi et al. [126]); taxa de conflito após a troca [155]. O grau do viés varia com a diferença de qualidade e a posição preferida varia por modelo (o GPT-4 tende à primeira, o ChatGPT à segunda).
  - **Compaixão que esmaece:** efeito do nome do modelo; nota maior ao que vem rotulado "gpt-4"; daí a necessidade de avaliação anônima.
  - **Estilo:** preferir conteúdo visualmente atraente independentemente da validade, como texto com emojis [19]; inclui o viés de sentimento (tons alegre, triste, irritado, de medo).
  - **Tamanho (verbosidade):** medido reescrevendo uma resposta de forma mais longa [CALM, MT-Bench], o que pode mudar perplexidade, fluência ou estilo, ou comparando várias amostras com qualidade difícil de igualar [121].
  - **Concretude:** preferir detalhes específicos (fontes de autoridade, números, termos complexos), também chamado viés de autoridade ou de citação, que ignora a correção dos detalhes e assim incentiva alucinação.

**Robustez adversarial** (amostras feitas de propósito para manipular a nota, diferente do viés em amostras naturais):
- Frases de ataque universais aprendidas num modelo substituto inflam a nota drasticamente sem melhorar o texto (Raina et al. [116]).
- O EMBER mostra viés com marcadores epistêmicos de certeza e incerteza.
- Um "modelo nulo" que devolve sempre a mesma resposta irrelevante obtém taxas de vitória altas em vários juízes (Zheng et al. [216]).
- Símbolos sem palavra (como ":") ou aberturas de raciocínio ("Thought process:") enganam o juiz a avaliar positivamente (Zhao et al. [211], "One Token to Fool LLM-as-a-Judge").
- Opinião da maioria ("90% acham que esta é melhor") e frase irrelevante no prompt de sistema ("Assistant A loves eating pasta").
- Defesas como a perplexidade detectam só alguns tipos de ataque.

## 5. O experimento de meta-avaliação (seção 4.4)

**Montagem.** Uma ferramenta de meta-avaliação (Figura 13) aplicada a dois conjuntos já existentes: o LLMEval2 (2.553 amostras com pergunta, par de respostas e preferência humana) para concordância com humanos, e o EvalBiasBench (80 amostras com a resposta correta sem influência de viés) para seis vieses (tamanho, concretude, referência vazia, continuação de conteúdo, instrução aninhada, conhecimento familiar). O viés de posição é medido trocando a ordem das respostas nas amostras dos dois conjuntos. Métricas: porcentagem de concordância; acurácia nos vieses; consistência de posição (mesma escolha nas duas ordens). Juízes: GPT-4-turbo (2024-04-09), GPT-3.5-turbo (0125), Qwen2.5-7B-Instruct, Llama-3-8B-Instruct, Mistral-7B-Instruct-v0.3, Mixtral-8x7B-Instruct-v0.1 (abertos numa A100 de 40 GB), e os de raciocínio gemini-2.0-thinking, o1-mini, o3-mini e DeepSeek-R1; temperatura 0. Estratégias testadas sobre o GPT-3.5-turbo: explicação junto com a nota, autovalidação, cinco rodadas agregadas por maioria, média ou melhor nota, e voto de três LLMs (conjunto 1: GPT-4-turbo, GPT-3.5-turbo e Llama-3-8B; conjunto 2: troca o Llama pelo Qwen2.5-7B). Os autores chamam isso de benchmark novo no resumo; na prática é um protocolo sobre conjuntos existentes.

**Tabela 2 (porcentagens; concordância com humanos n = 5.106; posição n = 2.633; tamanho 34; concretude 28; referência vazia 26; continuação 24; instrução aninhada 24; conhecimento familiar 24):**
- GPT-4-turbo: 61,54; 80,31; 91,18; 89,29; 65,38; 95,83; 70,83; 100,0.
- GPT-3.5-turbo: 54,72; 68,78; 20,59; 64,29; 23,08; 91,67; 58,33; 54,17.
- Qwen2.5-7B: 56,54; 63,50; 64,71; 71,43; 69,23; 91,67; 45,83; 83,33.
- Llama-3-8B: 50,72; 38,85; 20,59; 57,14; 65,38; 75,00; 45,83; 54,17.
- Mistral-7B: 55,42; 59,78; 26,47; 67,86; 53,85; 66,67; 37,50; 41,67.
- Mixtral-8x7B: 56,29; 59,06; 50,00; 78,57; 42,31; 83,33; 29,17; 83,33.
- gemini-2.0-thinking: 60,75; 76,84; 94,12; 89,29; 50,00; 100,00; 83,33; 100,00.
- o1-mini: 60,16; 76,73; 91,18; 89,29; 53,85; 95,83; 75,00; 95,83.
- o3-mini: 61,66; 74,63; 82,35; 92,86; 73,08; 95,83; 87,50; 91,67.
- DeepSeek-R1: 56,48; 69,17; 94,12; 100,00; 50,00; 100,00; 75,00; 87,50.

Leituras dos autores: o GPT-4-turbo supera os outros com folga e mostra menos vieses; o Qwen2.5-7B é o melhor aberto e supera o GPT-3.5 menos em posição e instrução aninhada; fora concretude e continuação, o desempenho é em geral fraco, sobretudo em tamanho (GPT-3.5 e Llama acertam 20,59%); até o GPT-4-turbo cai em referência vazia e instrução aninhada; os modelos não diferem de forma significativa na concordância com humanos, todos entre 50,72% e 61,66%, com espaço claro para melhorar. Recomendam juízes fortes ou ajustados e uma pequena meta-avaliação antes de escolher o modelo, porque cada modelo tem um perfil de vieses.

**Tabela 3 (LLMEval2 por rótulo humano; acurácia):** quando o humano prefere a resposta 1, o GPT-4-turbo acerta 68,47% (1.418 de 2.071), o gemini-2.0-thinking 65,41%, o o1-mini 69,76%, o o3-mini 72,26%, o DeepSeek-R1 66,10%; quando prefere a 2, 69,47%, 78,31%, 67,65%, 60,18%, 64,80%; quando o humano marca empate, 29,73%, 13,20%, 23,57%, 42,31%, 17,95%. O texto do artigo arredonda alguns desses valores de outro jeito (69,44, 29,67, 78,27). As amostras barradas pela política de conteúdo do Azure OpenAI ficaram de fora, por isso os totais variam. Os modelos de raciocínio são competitivos, mas não trazem a vantagem esperada no alinhamento com humanos.

**Tabela 4 (estratégias sobre o GPT-3.5-turbo; mesmas colunas da Tabela 2):**
- base: 54,72; 68,78; 20,59; 64,29; 23,08; 91,67; 58,33; 54,17.
- com explicação: 52,47; 48,97; 35,29; 60,71; 38,46; 91,67; 41,67; 50,00.
- com autovalidação: 54,86; 69,31; 23,53; 60,71; 23,08; 91,67; 41,67; 50,00.
- maioria de 5: 54,68; 70,11; 26,47; 67,86; 23,08; 95,83; 54,17; 50,00.
- média de 5: 54,72; 69,58; 11,76; 57,14; 26,92; 87,50; 50,00; 50,00.
- melhor de 5: 51,95; 58,72; 5,88; 42,86; 19,23; 87,50; 37,50; 45,83.
- vários LLMs, conjunto 1: 57,66; 32,28; 26,47; 64,28; 46,15; 87,50; 66,67; 62,50.
- vários LLMs, conjunto 2: 58,19; 70,98; 64,71; 71,43; 69,23; 91,67; 45,83; 83,33.

Leituras dos autores: nem toda estratégia ajuda. A explicação dá interpretabilidade, mas em geral piora o desempenho e o viés (a consistência de posição cai de 68,78 para 48,97), talvez por vieses mais profundos introduzidos pela autoexplicação; a autovalidação quase não muda nada, talvez por excesso de confiança do modelo; a maioria de cinco rodadas é descrita como benefício claro em várias dimensões, enquanto média e melhor nota não ajudam ou pioram (a média pode incluir resultados enviesados; a melhor nota pode escolher notas infladas por viés). Na tabela, a maioria de cinco melhora posição, tamanho, concretude e continuação, empata em referência vazia e piora em concordância humana (por 0,04), instrução aninhada e conhecimento familiar. O voto de vários LLMs depende de quem vota: no conjunto 1, o GPT-3.5 e o Llama fracos em tamanho e posição puxam o resultado para baixo (posição 32,28); no conjunto 2 o resultado acompanha o Qwen2.5. A linha do conjunto 2 é idêntica à linha do Qwen2.5-7B sozinho da Tabela 2 em seis das oito colunas (tamanho, concretude, referência vazia, continuação, instrução aninhada, conhecimento familiar); o artigo não comenta.

**Sugestões finais da seção:** integrar resultados de várias fontes depois de escolher bons juízes; a comparação entre maioria de cinco e média de cinco, segundo os autores, mostra que a avaliação em pares dá resultados mais confiáveis que a pontual; gerar avaliação e explicação ao mesmo tempo pode não ser aconselhável. A estratégia empírica que recomendam para comparação em pares é escolher LLMs mais fortes, trocar a posição das respostas e tirar a maioria de várias rodadas; para melhorar o alinhamento com humanos, falta pesquisa.

## 6. Repensar a meta-avaliação (seção 4.5)

- Falta um benchmark unificado que cubra concordância, vários vieses e robustez num só arcabouço; EvalBiasBench e CALM cobrem só partes, e quem usa juiz LLM ainda tem de desenhar o próprio protocolo de meta-avaliação e verificar à mão.
- Estudo controlado é difícil: isolar um viés de outros fatores; alongar uma resposta muda estilo, fluência e coerência e pode introduzir outros vieses; a preferência do GPT-4 pelas próprias respostas sobre as do GPT-3.5 pode ser autoaprimoramento ou preferência legítima por texto melhor.

## 7. Aplicações (seção 5)

- **Aprendizado de máquina:**
  - **Geração de texto:** resumo, diálogo, alucinação, segurança e recusa excessiva, contexto longo, debate entre agentes.
  - **Raciocínio:** escolha de caminho por amostra e por passo (modelos de recompensa de processo, MCTS, verificadores de vantagem).
  - **Recuperação:** ranking de documentos, autoconsistência por permutação contra viés de posição, RAG.
  - **Inteligência social:** SOTOPIA-EVAL; Agent-as-a-Judge com correlação de 0,83 com humanos em tarefas de cognição social, e vieses que crescem com o anonimato do agente.
  - **Avaliação multimodal:** o MLLM-as-a-Judge acha juízes que vão bem em pares mas mal em nota absoluta e ranking em lote; em casos extremos de direção autônoma, juízes de texto correlacionam mais com humanos que os próprios modelos de visão e linguagem.
- **Finanças:** avaliadores com conhecimento de domínio, benchmarks como UCFE, e o QuantAgent com laço de dois LLMs para sinais de trading avaliados por coeficiente de informação e Sharpe; papel ainda auxiliar.
- **Direito:** Eval-RAG para textos jurídicos coreanos, LegalBench, LexEval; problemas de alucinação, viés e distinções sutis.
- **Ciência:** acordo de kappa 0,79 de um avaliador LLaMA-2 ao checar consistência de notas clínicas; Math-Shepherd leva o Mistral-7B a 84,1% no GSM8K; MedHELM mostra modelos comerciais ainda fracos em segurança de medicação.
- **Outros:** resumo de relatos de bug (juiz supera humanos cansados), correção de redações, moderação de conteúdo no Reddit (alta taxa de verdadeiros negativos, dificuldade com regras complexas), preferência por persona (fraca com personas simplificadas, melhor com estimativa verbal de incerteza nos casos de alta certeza).

## 8. Desafios (seção 6)

- **Confiabilidade:** sensibilidade a pequenas mudanças de prompt e à ordem dos exemplos; aleatoriedade da geração; excesso de confiança, sobretudo em modelos treinados com RLHF, ligado ao autoaprimoramento; caixa-preta e dependência de versão; juízes ajustados sobreajustam.
- **Robustez:** ataques sutis (paráfrase de uma frase-chave, frase enganosa mas gramatical); jailbreak e persona com preconceitos; fragilidade do formato de nota (uma entrada pode fazer o juiz devolver texto em vez de número e quebrar o pipeline).
- **Limites do modelo base:** multimodalidade fraca; o juiz pode dar nota alta pela fluência do estilo e não ver uma falha sutil na cadeia lógica ou causal.
- **Interpretabilidade:** o processo é caixa-preta e não mostra que precedentes ou critérios pesaram.
- **Meta-avaliação e consistência no tempo:** raramente se examina o avaliador; o julgamento deriva com atualizações do modelo ("evaluation drift"; um tema controverso aceito por uma versão de março e penalizado por uma de junho após novo ajuste de segurança).
- **Ética e sociedade:** amplificação de vieses (penalizar dialeto ou estilo de grupo marginalizado); falta de responsabilização; impacto na criatividade: se o juiz favorece sempre um estilo, formato ou tom, pode homogeneizar o conteúdo produzido, fenômeno que os autores chamam de "evaluation-driven convergence".

## 9. Direções futuras (seção 7)

- **Julgamento centrado em raciocínio:** julgar e raciocinar se reforçam; laços de raciocínio, julgamento e refinamento no treino e na inferência (o1, DeepSeek-R1, IA constitucional); juízes que se autocalibram e evoluem ("World Model-as-a-Judge", que simula consequências).
- **Fundamentação teórica:** trazer estatística e teoria da medida, adaptar kappa de Cohen e alfa de Krippendorff para medir a confiabilidade entre juízes.
- **Juiz mais confiável:** treino adversarial específico de julgamento, quantificação de incerteza, humano no circuito para decisões críticas.
- **MLLM como juiz** de dados, agentes, recompensa e verificação.
- **Benchmarks:** meta-avaliação do próprio avaliador com prompts de qualidades adversariais conhecidas e acompanhamento da estabilidade entre versões; benchmarks maiores, de domínio e multimodais, com métricas mais finas que uma nota.
- **Juiz para anotar dados, para escalar** (rótulos de preferência para RLHF, anotação inicial verificada por humanos, crítico ou recompensa em tempo real), **para inteligência incorporada** (avaliar sequências de ações de robôs e agentes), **para otimizar LLMs** (ReFT, multiagentes) e **por domínio** (médico, jurídico, educação, revisão por pares).

## 10. Tudo o mais que ensina

- **Conclusão dos autores:** o juiz LLM tende a virar componente central da avaliação, aumentando a perícia humana em vez de substituí-la; a confiabilidade esbarra em saídas probabilísticas, excesso de confiança e vieses herdados; a robustez, em manipulação do prompt e efeitos de enquadramento do contexto; a generalização, em multimodalidade e padrões de domínio.
- **Trabalhos citados com o achado de cada um:** Wang et al. [155] ("Large Language Models are not Fair Evaluators", ACL 2024), viés de posição e calibração por troca e média; Shi et al. [126] ("Judging the Judges", arXiv 2406.07791), métricas de posição; Thakur et al. [144] ("Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges", arXiv 2406.12624), porcentagem de concordância e kappa; Chen et al. [19] ("Humans or LLMs as the judge?", arXiv 2402.10669), vieses de estilo e citação; Koo et al. [66] (CoBBLEr, arXiv 2309.17012), compaixão, manada e distração; Park et al. [110] (OffsetBias, arXiv 2407.06551), dados para reduzir vieses e o EvalBiasBench; Raina et al. [116] (arXiv 2402.14016), ataques universais; Zheng et al. [216] (arXiv 2410.07137), modelo nulo; Zhao et al. [211] (arXiv 2507.08794), um token engana o juiz; Saito et al. [121] (arXiv 2310.10076), verbosidade em rótulos de preferência; Liu et al. [95] (COLM 2024), preferência em pares; Huang et al. [49] (arXiv 2403.02839), juízes ajustados são classificadores específicos de tarefa; Jung et al. [57] ("Trust or Escalate", arXiv 2407.18370), garantias de concordância com humanos; Dong et al. [30] (arXiv 2406.11657), juiz personalizado por persona; Wang et al. [158] (Self-Taught Evaluators, arXiv 2408.02666); Wang et al. [161] (TrustJudge, arXiv 2509.21117); Zhang et al. [207] (LLMEval2, arXiv 2308.01862).
- **Fórmula do avaliador por probabilidade (seção 2.3.2):** a nota de autoconsistência e de autorreflexão vem da probabilidade dos tokens relevantes ("Yes") condicionada ao contexto, e a nota final é o produto das duas.
- **Exemplos de prompt:** templates de Gao et al. para Likert (resumo em quatro dimensões de 1 a 5) e para pares ("Summary 0" ou "Summary 1", sem explicar); template de sim/não ("Is the sentence supported by the article?") e de múltipla escolha com unidades de conteúdo semântico.

---
