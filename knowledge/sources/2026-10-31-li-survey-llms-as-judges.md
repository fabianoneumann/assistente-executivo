---
titulo: "LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods"
tipo: paper
autor: "Haitao Li, Qian Dong, Junjie Chen, Huixue Su, Yujia Zhou, Qingyao Ai, Ziyi Ye, Yiqun Liu"
url: "https://arxiv.org/abs/2412.05579"
publicado_em: 2024-12-07
capturado_em: 2026-10-31
licenca: "Licença não exclusiva de distribuição do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0, indicada na página do arXiv); o PDF usa o template da ACM com aviso de copyright, sem publicação registrada no OpenAlex. Entra só a ficha."
areas: [agent-engineering]
tags: [llm-as-judge, survey, bias-taxonomy, position-bias, self-enhancement-bias, adversarial-attacks, meta-evaluation, multi-llm-evaluation, human-ai-collaboration, fine-tuned-judges, agreement-metrics]
---

Ficha de estudo, em palavras próprias; sem texto integral. arXiv: v1 em 07/12/2024 e v2 em 10/12/2024; lida a v2 (60 páginas, comentário do arXiv: "comprehensive and continuously updated"). O PDF está no template de revista da ACM, com aviso de copyright de 2024 e DOI de modelo ("nnnnnnn"), sem venue; o OpenAlex só registra o arXiv. Autores do Departamento de Ciência da Computação e do Instituto de Judiciário na Internet da Universidade Tsinghua, e da Escola Gaoling de IA da Universidade Renmin; lista de recursos mantida em https://github.com/CSHaitao/Awesome-LLMs-as-Judges. Texto extraído com `pdftotext -layout`. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Atenção:** é uma survey sem experimento próprio; não traz números de magnitude de viés, só a taxonomia, os métodos e as referências. A ficha aponta os trabalhos citados pelo número de referência do artigo quando útil.

## O resumo

Os LLMs passaram a ser usados como avaliadores com base em respostas em linguagem natural ("LLMs-as-judges"), pela eficácia, pela generalização entre tarefas e pela interpretabilidade. A survey cobre cinco perspectivas: funcionalidade (por que usar juízes LLM), metodologia (como usar), aplicações (onde usar), meta-avaliação (como avaliar o juiz) e limitações (problemas existentes), e termina com direções futuras.

## 1. Definição formal (seção 2)

(Y, E, F) = f(T, C, X, R): a função de avaliação f recebe o tipo de avaliação T, os critérios C, o item avaliado X e referências opcionais R, e produz o resultado Y, a explicação E e o feedback F.

- **Função de avaliação, três configurações:**
  - **Um LLM:** simples e escalável, flexibilidade limitada, pode introduzir viés se mal treinado.
  - **Vários LLMs:** cooperação ou competição, cobertura maior, custo maior, e a forma de chegar a consenso ainda é questão aberta.
  - **Humano com IA:** humanos mitigam vieses e dão julgamento subjetivo, com custo e tempo maiores e menos escala.
- **Tipo de avaliação:**
  - **Pontual:** simples, mas pode não captar diferenças relativas e sofre vieses de avaliar isoladamente.
  - **Em pares:** espelha a decisão humana por preferência relativa e serve quando as diferenças são sutis e difíceis de quantificar.
  - **Em lista:** ranqueia o conjunto, considerando a interação entre candidatos.
  - As conversões entre os três não são confiáveis com juízes LLM: uma resposta pode ter nota 5 e outra 4 e a comparação direta não dar a primeira como melhor; os juízes nem sempre respeitam transitividade (preferir A a B e B a C sem preferir A a C).
- **Critérios:** qualidade linguística (fluência, gramática, coerência, concisão), acurácia de conteúdo, métricas da tarefa (informatividade, completude, diversidade, estrutura); exemplos ajudam.
- **Referências:** avaliação com referência (bem definida, limitada pela qualidade e variedade da referência) ou sem referência (flexível, fraca onde o LLM não tem conhecimento).
- **Saídas:** resultado (nota, ranking, categoria), explicação (raciocínio e justificativa, que segundo os autores aumenta a transparência e também leva a resultados mais alinhados a humanos e mais precisos) e feedback (sugestões acionáveis, que exige mais capacidade do modelo).

## 2. Funcionalidade: por que usar (seção 3)

- **Avaliação de desempenho:** de respostas (LLM-Eval para diálogo; pontuação de redações; revisão automática de artigos, que Zhou et al. acham ainda pouco confiável quando exige raciocínio lógico ou base de conhecimento profunda; ARES avalia RAG em relevância de contexto, fidelidade e relevância da resposta) e de modelos (benchmarks estáticos; avaliação dinâmica e interativa como Auto-Arena, LMExam e KIEval, em que LLMs fazem as perguntas e julgam, contra vazamento de dados).
- **Melhoria de modelos:**
  - **Recompensa no treino:** SRLMs, OAIF e RLAIF fazem o modelo ser o próprio modelo de recompensa; RELC dá recompensa densa por passo. Os autores alertam que usar o mesmo LLM para gerar a política e a recompensa pode acumular vieses e ruído nas preferências; CREAM impõe consistência entre iterações e CGPO usa "juízes mistos" por grupo de tarefa.
  - **Verificador na inferência:** Best-of-N, autoconsistência, Tree of Thoughts, Graph of Thoughts, verificação passo a passo, Creative Beam Search com o LLM imitando a seleção criativa humana.
  - **Feedback para refinar:** SELF-REFINE, SELF-DEBUGGING, REFINER, revisão por pares entre agentes. Ressalva: os estudos de autocorreção (Huang et al., "Large language models cannot self-correct reasoning yet"; Tyen et al.) mostram que a autocorreção intrínseca muitas vezes não melhora o raciocínio, e Valmeekam et al. duvidam do LLM como autovalidador sem um validador externo confiável.
- **Construção de dados:** anotação (He et al.: melhor acurácia de trabalhadores do MTurk 81,5% contra 83,6% do GPT-4; Gilardi et al.: em 6.183 tweets e notícias, o ChatGPT supera trabalhadores de crowdsourcing em postura, tópico e enquadramento; Törnberg et al.: o ChatGPT-4 supera classificadores humanos na inclinação política de usuários do Twitter com viés igual ou menor; AnnoLLM "explicar e depois anotar"; LLMAAA com aprendizado ativo) e síntese (SELF-INSTRUCT, Evol-Instruct, STaR, ReST-EM).

## 3. Metodologia: como usar (seção 4)

**Um LLM, por prompt:**
- **Aprendizado em contexto:** GPTScore, LLM-EVAL, TALEC (critérios do usuário), ICE. A escolha dos exemplos pode enviesar; ALLURE incorpora as discrepâncias entre o juiz e as anotações no contexto, iterativamente; Song et al. acham viés de símbolo e propõem prompts com muitos exemplos (com e sem referência).
- **Passo a passo:** CoT, G-EVAL (CoT com preenchimento de formulário), ICE-Score para código, ProtocoLLM, PORTIA (divide as respostas em partes, alinha conteúdo semelhante entre as candidatas e junta num prompt só). Chiang e Lee mostram que combinar nota com explicação (nota e depois explicação, ou explicação e depois nota) dá correlação maior com humanos. FineSurE decompõe resumo em fidelidade, completude e concisão.
- **Definição aumentada:** AUTOCALIBRATE (rascunha, revisa e aplica critérios calibrados a preferências humanas, sem gradiente), SALC (critérios gerados pelo próprio LLM conforme o contexto), juiz personalizado por papéis, BiasAlert (conhecimento externo para detectar viés social). Chen et al. [33] acham que, dentro de pipelines de RAG, juízes LLM não mostram autopreferência significativa.
- **Várias rodadas:** ACTIVE-CRITIC infere critérios dos dados; LLMs como formuladores de perguntas que se adaptam ao avaliado.

**Um LLM, por ajuste fino (Tabela 1, com dados, escala, tipo e técnica de cerca de 30 métodos):**
- **Por nota:** PHUDGE (Phi-3), ECT, AttrScore, SELF-J (sem notas humanas), FENCE (fatualidade por afirmação), ARES (inferência com predição para confiança estatística).
- **Por preferência:** DPO; Meta-Rewarding; Con-J (DPO em julgamentos contrastivos com justificativas em vez de nota escalar); JudgeLM; PandaLM; Self-Taught (só dados sintéticos); FedEval-LLM (vários juízes personalizados federados).
- **Mistos:** FLAMe, AUTO-J, Shepherd, X-EVAL, Themis, CritiqueLLM, Self-Rationalization, CompassJudger-1, HALU-J, Prometheus e Prometheus 2 (rubricas personalizadas, nota direta e ranking em pares), Prometheus-Vision, LLaVA-Critic; Zhou et al. com calibração para modelos fechados e treino contrastivo para abertos.

**Um LLM, por pós-processamento:**
- **Calibração de probabilidade:** Daynauth et al. quantificam por estatística bayesiana e teste t o viés por mais tokens e recalibram; ProbDiff; Product of Experts para comparação eficiente; CRISPR poda neurônios de viés.
- **Reprocessamento de texto:** média de rankings de várias rodadas; dividir e conquistar do AUTO-J; REVISEVAL gera referências adaptadas à resposta; conversão entre perguntas abertas e de múltipla escolha.

**Vários LLMs:**
- **Comunicação:**
  - **Cooperação:** WideDeep; revisão por pares entre agentes; ABSEval. Ressalva: risco de pensamento de grupo, com modelos semelhantes reforçando os vieses uns dos outros em vez de trazer visões diversas.
  - **Competição:** centralizada, como Auto-Arena (debate entre candidatos e comitê de juízes) e as arquiteturas de tribunal MORE e SAMRE; descentralizada, como ChatEval (debate com papéis diversos) e PRD (Peer Rank and Discussion contra autoaprimoramento e posição).
- **Agregação sem comunicação:** voto da maioria (Badshah et al. com veredito guiado por referência; PoLL, painel de modelos menores e diversos com voto ou média, que reduz o viés intramodelo; Language-Model-as-an-Examiner); média ponderada (PiCO, PRE que seleciona revisores por um exame de qualificação e pondera pela concordância com humanos); métodos bayesianos (Bayesian Win Rate Sampling, Dawid-Skene bayesiano) e em grafo (GED, que denoisa grafos de preferência de juízes fracos num DAG); agregação por LLM (Fusion-Eval); cascata do modelo barato ao forte por confiança (Cascaded Selective Evaluation; CascadedEval).

**Humano com IA:**
- **Humanos durante a avaliação:** COEVAL (LLM gera critérios e avaliações, humanos revisam); a calibração de Wang et al. contra viés de posição, com três estratégias (evidência múltipla, posição balanceada e humano no circuito); EvalGen, com feedback humano iterativo para refinar critérios diante de "criteria drift", em que o padrão de avaliação muda à medida que o humano interage com o modelo.
- **Humanos depois:** EvaluLLM; LLM como monitor de curso universitário revisado pela equipe docente.

## 4. Aplicações (seção 5)

- **Geral:** diálogo, resumo, tradução; o Fusion-Eval chega a Kendall-Tau 0,962 com humanos no nível de sistema em resumo e Spearman 0,744 no nível de turno em diálogo.
- **Multimodal.**
- **Medicina:** um avaliador Llama2 checando consistência de notas clínicas concorda com humanos em nível comparável ao de anotadores.
- **Direito:** avaliação de LLMs jurídicos e relevância em busca de casos; o viés tem impacto grave em decisões judiciais.
- **Finanças.**
- **Educação:** correção, redação, matemática e debate; LLMs ainda não substituem revisores humanos em áreas de alta complexidade técnica ou forte inovação.
- **Recuperação de informação.**
- **Software, biologia e ciências sociais:** inclui a "Habermas Machine", que gera declarações de grupo para maximizar aprovação em deliberação.

## 5. Meta-avaliação: como avaliar o juiz (seção 6)

- **40 benchmarks por domínio:**
  - **Código:** HumanEval, SWE-bench, DevAI, CrossCodeEval, CodeUltraFeedback.
  - **Tradução:** MQM, comparações de tradução literária.
  - **Resumo:** SummEval, FRANK, OpinSummEval.
  - **Diálogo:** Topical-Chat, PERSONA-CHAT, DSTC10.
  - **Geração de histórias:** HANNA, 1.056 histórias de 10 sistemas a partir de 96 prompts, com três anotadores e seis critérios (relevância, coerência, ressonância, surpresa, engajamento, complexidade); MANS e OpenMEVA; StoryER, com 100 mil pares de histórias de alto e baixo engajamento (votos positivos de pelo menos 50 ou de no máximo 0) e 46 mil notas por aspecto de 1 a 5 com comentários; PERSER, com rótulos personalizados para lidar com a subjetividade.
  - **Alinhamento de valores:** PKU-SafeRLHF, HHH, CVALUES.
  - **Recomendação:** MovieLens, Yelp.
  - **Busca:** TREC DL, MS MARCO, LeCaRDv2.
  - **Dados abrangentes:** HelpSteer e HelpSteer2; UltraFeedback (cerca de 64 mil prompts); AlpacaEval; Chatbot Arena (mais de 1 milhão de votos, ranking Bradley-Terry); MT-Bench; WildBench (Elo penalizado por tamanho); FLASK (nota por habilidade); RewardBench; RM-Bench (sensibilidade a diferenças sutis e resistência a viés de estilo); JudgerBench; JudgeBench (rótulos de correção objetiva); MLLM-as-a-Judge; MM-Eval (18 línguas, mais um subconjunto de 122, em que juízes tendem a notas neutras nas línguas de poucos recursos).
- **Métricas (Tabela 4):** acurácia (sensível; não capta avaliações contínuas), Pearson (relação linear de notas, sensível a extremos), Spearman (ordem, robusto), Kendall tau (ordem, lida com empates), kappa de Cohen (dois avaliadores, desconta o acaso), ICC (vários avaliadores, consistência de grupo).

## 6. Limitações: vieses (seção 7.1, Tabela 5)

A taxonomia divide os vieses em quatro grupos pela causa e manifestação, cada um com definição, impacto e soluções propostas.

**Ligados à apresentação:**
- **Posição:** favorecer respostas pela ordem; também ocorre em decisão humana e em modelos de ML treinados com dados ordenados.
  - **Métricas:** estabilidade de repetição, consistência de posição e justiça de preferência ([151], Shi et al.).
  - **Mitigações:**
    - Trocar a ordem e descartar o julgamento inconsistente.
    - Variante por nota: média das notas nas ordens trocadas.
    - Variante por comparação: empate quando a troca muda o veredito. Quanto maior a diferença de qualidade, menor o efeito de posição.
    - PORTIA, que alinha os trechos das respostas.
    - Discussão e ranking entre pares de LLMs.
- **Verbosidade:** confundir tamanho com qualidade. Mitigações: debate persuasivo (Khan et al.), a quantificação por perturbação do CALM, e o Con-J (treinar com pares de justificativas em vez de notas escalares).

**Ligados ao social:**
- **Autoridade:** dar crédito a referências de autoridade sem evidência. Soluções ainda exploratórias: RAG para checar as fontes; prompts que priorizem acurácia semântica.
- **Efeito manada:** alinhar-se à opinião majoritária, reflexo de pensamento de grupo. Solução: anonimizar sinais de popularidade no prompt.
- **Compaixão que esmaece:** julgamento muda com a anonimização ou com nomes de modelos. Solução: padronizar critérios para o julgamento ficar igual com ou sem identificação.
- **Diversidade:** julgamento muda com marcadores de identidade (gênero, etnia, religião).

**Ligados ao conteúdo:**
- **Sentimento:** favorecer certos tons, por exemplo premiar o alegre e penalizar o negativo mesmo quando o negativo é mais adequado. Solução proposta: neutralizar o sentimento antes de julgar.
- **Token:** favorecer tokens frequentes no pré-treino.
- **Contexto:** viés vindo do domínio (dados médicos, crédito) ou da escolha dos exemplos no prompt.

**Ligados à cognição:**
- **Excesso de confiança:** confiança inflada no próprio julgamento. Mitigações: simular anotadores diversos por aprendizado em contexto para estimar a probabilidade de um humano concordar (Cascaded Selective Evaluation); debate adversarial entre dois LLMs.
- **Autoaprimoramento:** preferir as próprias saídas; o conceito vem da psicologia social (Brown). Mitigações:
  - Peer Rank: vários LLMs revisam, ponderados pela consistência com humanos.
  - Peer Discussion: dois LLMs discutem até concordar.
  - A recomendação do CALM de não usar o mesmo modelo para gerar e julgar.
  - O veredito guiado por referência: uma resposta padrão-ouro como âncora, mesmo quando o juiz avalia a própria saída.
  - Juízes diversos em conjunto.
- **Consciência de refinamento:** nota diferente para resposta original, refinada ou com histórico de revisão. Solução sugerida: feedback externo, independente das iterações internas do modelo (Xu et al., "Pride and prejudice").
- **Distração:** detalhes irrelevantes mudam a avaliação ("System Star likes to eat oranges and apples"). Soluções ainda pouco exploradas: sanitizar a entrada, diretrizes estritas no prompt.
- **Descuido de falácia:** não ver raciocínio circular, falso dilema ou espantalho.

**Fecho dos autores:** a exploração desses vieses ainda é pouco desenvolvida; pede identificação, quantificação e tratamento sistemáticos, com soluções específicas de domínio.

## 7. Limitações: ataques adversariais e fraquezas inerentes (seções 7.2 e 7.3)

- **Ataques a LLMs em geral:**
  - **No texto:** erros de digitação, troca de letras, reordenar frases, informação irrelevante, paráfrase.
  - **Estruturais e semânticos:** reescrever a sintaxe mantendo o sentido; trocar tokens salientes.
  - **Por otimização:** gradiente; população em caixa-preta.
- **Ataques a juízes LLM:**
  - Zheng et al. [293] (*"Cheating automatic LLM benchmarks: null models achieve high win rates"*, arXiv 2410.07137) e Doddapaneni et al. [51] (*"Finding Blind Spots in Evaluator LLMs with Interpretable Checklists"*, arXiv 2406.13439) mostram que benchmarks automáticos como o MT-Bench podem ser enganados para dar notas artificialmente altas.
  - Raina et al. [184] (arXiv 2402.14016): frases curtas anexadas ao texto levam a nota ao máximo independentemente da qualidade, e frases otimizadas num modelo substituto pequeno (FlanT5-xl) transferem para GPT-3.5 e Llama2.
  - JudgeDeceiver [196] (arXiv 2403.17710): injeção de prompt otimizada que leva o juiz a escolher a resposta errada entre as candidatas.
  - O campo é pouco explorado e precisa de defesas.
- **Fraquezas inerentes:** conhecimento desatualizado (um juiz não atualizado pode preferir a resposta com a diretriz antiga da OMS sobre COVID-19; soluções: RAG, ajuste periódico, aprendizado contínuo, checagem de fatos); alucinação (precedentes ou fontes inventadas no julgamento; checagem cruzada com bases confiáveis); lacunas de conhecimento de domínio (grafos de conhecimento, RAG).

## 8. Direções futuras (seção 8)

- **Mais eficientes:**
  - Construir critérios e tarefas automaticamente, por tipo de tarefa, público e domínio, e tarefas dinâmicas contra contaminação.
  - Sistemas modulares escaláveis.
  - Acelerar, com algoritmos de seleção de candidatos (pares exigem muitas rodadas) e comunicação enxuta entre vários LLMs.
- **Mais eficazes:**
  - Integrar raciocínio e julgamento.
  - Mecanismo de julgamento coletivo, com vários LLMs e ensemble dinâmico.
  - Conhecimento de domínio com atualização dinâmica.
  - Transferência entre domínios e línguas.
  - Avaliação multimodal integrada.
- **Mais confiáveis:**
  - Interpretabilidade e transparência, com explicações claras e modelos de validação baseados em lógica.
  - Mitigar viés com algoritmos de desenviesamento, restrições de justiça e treino adversarial.
  - Robustez a ruído e ambiguidade, com aumento de dados.

## 9. Tudo o mais que ensina

- **Introdução:** a avaliação de IA passou de métricas programáveis (acurácia, precisão, revocação) para avaliadores flexíveis; o Teste de Turing como referência; BLEU e ROUGE não captam fluência, coerência e criatividade; anotação humana é o "padrão-ouro" mas cara.
- **Vantagens declaradas do juiz LLM:** critérios ajustáveis ao contexto da tarefa, avaliações interpretativas, alternativa escalável e reprodutível à avaliação humana.
- **Desafios declarados na introdução:** sensibilidade ao template do prompt, vieses implícitos herdados do corpus de treino, dificuldade de adaptar critérios a cada domínio.
- **Referências-chave citadas, com o achado:**
  - Wang et al. [230] (*"Large language models are not fair evaluators"*, arXiv 2305.17926): calibração de posição.
  - Koo et al. [112] (CoBBLEr, arXiv 2309.17012): vieses cognitivos, incluindo distração, manada e compaixão.
  - Chen et al. [25] (arXiv 2402.10669): vieses de autoridade, falácia e diversidade em juízes humanos e LLM.
  - Panickssery et al. [172] (*"LLM evaluators recognize and favor their own generations"*, arXiv 2404.13076): autopreferência.
  - Li et al. [132] (PRD, arXiv 2307.02762): ranking e discussão entre pares.
  - Badshah e Sajjad [8] (arXiv 2408.09235): veredito guiado por referência.
  - Verga et al. [225] (PoLL): júri de modelos.
  - Li et al. [127] (CalibraEval, arXiv 2410.15393): calibrar a distribuição de predição contra viés de seleção.
  - Li et al. [134] (PORTIA, arXiv 2310.01432): dividir e juntar.
  - Ye et al. [270] (Con-J, arXiv 2410.03742): juiz gerativo aprendido de dados de preferência.
  - Chiang e Lee [36] (arXiv 2310.05657): nota com explicação.
  - Chen et al. [33] (arXiv 2410.20833): juízes enviesados, mas não para RAG.
  - Xu et al. [259] (ACL 2024): o LLM amplifica o autoviés no autorrefinamento.
