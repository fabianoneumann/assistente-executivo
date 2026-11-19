---
titulo: "Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence"
tipo: paper
autor: "Ante Kapetanovic, Kemal Altwlkany, Andro Mercep, Tomislav Duricic, Emanuel Lacic"
url: "https://arxiv.org/abs/2608.25869"
publicado_em: 2026-08-26
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv e no rodapé da primeira página do PDF: 'This work is licensed under a Creative Commons Attribution 4.0 International License')"
areas: [agent-engineering]
tags: [llm-as-judge, anchoring, evaluation-independence, prior-score, iterative-refinement, chain-of-thought, debiasing, token-probabilities, context-engineering]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 26/08/2026, a única versão e a lida. O comentário do arXiv diz que o artigo sai nos anais do CIKM '26 (35ª ACM International Conference on Information and Knowledge Management, Roma, 7 a 11/11/2026), e o PDF traz o formato de referência da ACM com o DOI 10.1145/3799682.3840879. Autores da Infobip (Split, Sarajevo e Zagreb). Código, prompts, rubricas e fórmulas em https://github.com/infobip/llm-judge-bias. Os autores declaram uso de IA generativa em papel de apoio: Claude Code (Opus 4.6) para código e análise de dados, ChatGPT 5.2 para edição de LaTeX e gramática, Google Scholar Labs para achar trabalhos relacionados. O integral foi extraído do PDF; os valores da Figura 4 (mapa de calor) foram conferidos na página renderizada. Lida (camadas flexíveis de avaliação).

**Atenção:** os juízes deste estudo são LLMs, não pessoas.

## O resumo

Juízes LLM dão nota, filtram conteúdo e decidem se um laço de refinamento continua; cada julgamento costuma ser tratado como independente dos anteriores. Os autores testam essa premissa com três condições de prompt: sem metadados, com o aviso de que é uma revisão, e com metadados ancorados (revisão, número da tentativa e nota anterior). Notas anteriores, mesmo só como metadado de contexto, puxam o julgamento na direção delas. Em 192.000 avaliações tentadas (185.271 válidas), sete de oito modelos têm intervalo de bootstrap de 95% abaixo de zero para o efeito total, e o d de Cohen chega a 0,71 em valor absoluto. Numa sonda por token, a entrada dos metadados redistribui a probabilidade das notas, enquanto mudar o valor da âncora dentro da faixa testada muda pouco. Em dados industriais categóricos com rótulo humano, os metadados ancorados bloqueiam 48% das correções de erro e viram 10,18% dos julgamentos corretos para o rótulo errado atribuído. Nem Chain-of-Thought nem um aviso para desconsiderar os metadados reduzem o efeito total, embora o aviso melhore o efeito pareado na acurácia no experimento industrial. A conclusão do resumo: avaliação confiável pede engenharia cuidadosa do contexto, e a mitigação tem de ser validada no modelo e na tarefa ou domínio pretendidos.

## 1. Introdução

- **O cenário:** a nota anterior de um juiz pode ficar na janela de contexto da chamada seguinte, como etiqueta de metadado numa revisão, como rótulo vindo de uma etapa anterior do pipeline ou como resultado de uma rodada anterior de autoavaliação. A premissa implícita é que cada julgamento continua independente.
- **A literatura humana:** Tversky e Kahneman descreveram a ancoragem, a tendência de estimativas numéricas serem puxadas para um valor visto antes, mesmo sem informação. Na demonstração clássica, a estimativa da porcentagem de países africanos na ONU foi 25% ou 45% conforme a roleta mostrava 10 ou 65 logo antes. O mecanismo proposto é ancorar e ajustar: parte-se do valor visível e ajusta-se pouco. Também mostraram efeitos de enquadramento ("salvar 200 de 600 vidas" contra "deixar 400 morrerem", matematicamente iguais). Os dois efeitos se repetem em sentenças judiciais, negociações, mercados financeiros e avaliação de imóveis, e persistem apesar de consciência, perícia e incentivo à precisão.
- **Perguntas:** RQ1, como o enquadramento de revisão e a condição completa com metadados ancorados afetam as notas, por modelo e tarefa; RQ2, se a resposta varia com o valor da âncora ou mostra um salto do tipo limiar quando os metadados entram; RQ3, quais mitigações testadas reduzem o viés, e a que custo.

## 2. Trabalhos relacionados

- LLMs herdam vieses sociais dos dados e mostram análogos funcionais de vieses cognitivos humanos. Cheung et al.: efeito de enquadramento em decisões morais com 45% de mudança de resposta em LLMs contra 5% em humanos. Sumita et al.: em seis vieses cognitivos, o prompt de conscientização mitiga com eficácia.
- **Ancoragem em LLMs:** Lou e Sun (GPT-4 e Gemini em estimação): Chain-of-Thought e instruções explícitas para ignorar não mitigam por completo. Huang et al.: a ancoragem opera em camadas rasas do transformer e resiste às mitigações convencionais. Germani e Spitale: só a atribuição de fonte desloca julgamentos, com a concordância caindo de 95% para 15% quando o mesmo texto é atribuído a fontes diferentes.
- **Vieses de juiz já documentados:** posição, verbosidade, autopreferência, inconsistência; Ye et al. catalogam doze; Koo et al. medem vieses cognitivos em avaliadores, inclusive egocêntrico; Chen et al. acham vieses de autoridade e de beleza em juízes humanos e LLM; Li et al. e Marioriyad et al. relatam vazamento de preferência e vieses de atalho ligados à origem do modelo.
- **Mitigações propostas por outros:** vários revisores, alinhamento do avaliador às preferências humanas (Shankar et al.), calibração, prompt de conscientização.
- **A lacuna que os autores apontam:** o trabalho existente mede ancoragem em estimação com âncoras informativas; não cobre nota por rubrica, âncoras abaixo do limiar nem validação em dados de produção. O mais próximo é Huang et al. (estimação numérica). Ressalva dos autores: na literatura de avaliadores humanos, ver a nota anterior nem sempre faz mal; com notas individuais ruidosas, a âncora pode ajudar a calibrar. Aqui as âncoras são sorteadas independentemente da qualidade da resposta e, por construção, não informam nada.

## 3. Método

**Cenário:** nota de resposta única por rubrica, escala de 0 a 5 com seis faixas ([0,1) inaceitável, [1,2) fraca, [2,3) razoável, [3,4) boa, [4,5) muito boa, 5 excelente) e aceitação em 4,0. Imita refinamento iterativo e filtragem de qualidade. A escala 0 a 5 foi escolhida porque trabalho recente a aponta como a escala discreta mais alinhada entre humanos e LLM em notas por rubrica.

**Condições (Figura 1):**
- **C0, base:** tarefa, resposta e rubrica, sem metadado.
- **C1, enquadramento:** acrescenta que a submissão é uma revisão.
- **C2, ancoragem:** revisão, número da tentativa k ∈ {1, 2, 3, 4} e "Prior score" sorteado uniformemente em [0; 3,99), sempre abaixo do limiar de aceitação. Representa um fluxo de aceite (gating workflow) em que o que foi aceito não volta para revisão. O bloco inserido é "Attempt: k (This is a revision) / Prior score: a". O juiz não foi informado de que a nota anterior era sorteada; o experimento testa se o julgamento continua independente quando o metadado é apresentado como avaliação real.
- **Contrastes:** C2−C0 é o estimando principal, o efeito total dos metadados ancorados; C1−C0 é o efeito do enquadramento; C2−C1, o efeito incremental além do enquadramento, que **não isola a nota numérica**, porque C2 também acrescenta o campo de tentativa e muda o bloco. Sob independência, as médias das três condições seriam iguais.

**Modelos:** oito. Três por API via proxy LiteLLM (GPT-4.1, Claude-4.5-Sonnet, DeepSeek-R1) e cinco de pesos abertos em BF16 num NVIDIA DGX B200 (Llama-3.2-3B, Llama-3.1-8B, Llama-3.3-70B, Qwen2.5-7B, Gemma-2-9B).

**Tarefas:** 20, cinco de cada em resumo, revisão de código, escrita criativa e QA factual. As respostas foram geradas pelo GPT-5.2 (que não é juiz) com pedido de qualidade "competent but not exceptional", faixa que costuma tirar de 3,0 a 5,0; triadas à mão, com as uniformemente excelentes ou fracas regeradas. Uma resposta fixa por tarefa, igual em todas as condições e modelos. Saída em JSON com nota, aceite, justificativa e marcações. Rubrica de resumo e revisão de código adaptada das dimensões do SummEval usadas pelo G-Eval; rubricas próprias para escrita criativa e QA factual.

**Volume:** 100 chamadas por combinação de modelo, tarefa, condição e temperatura (0; 0,5; 1,0; 2,0): 192.000 avaliações tentadas, 185.271 válidas (sem erro de chamada e com nota numérica). 18 notas fora de [0, 5] foram cortadas para os limites. O aceite foi derivado da nota (≥ 4,0), não do booleano emitido. As 1.920 células de modelo, tarefa, temperatura e condição tiveram respostas válidas.

**Tabela 1 (trios completos C0/C1/C2 por índice de tentativa):** 59.136 dos 64.000 possíveis; incompletos por modelo: GPT-4.1 0,0%, Claude-4.5-Sonnet 0,0%, DeepSeek-R1 0,8%, Llama-3.3-70B 2,1%, Gemma-2-9B 5,0%, Qwen2.5-7B 10,5%, Llama-3.1-8B 15,0%, Llama-3.2-3B 27,4%. Os trios completos servem só para o d de Cohen descritivo. Pares completos: C0/C2 60.133, C0/C1 60.503, C1/C2 60.122. Índices iguais entre condições não compartilham semente e não são tratados como pares.

**Estatística:** as médias de cada condição são calculadas por célula de modelo, tarefa e temperatura; para cada modelo, faz-se a média das quatro temperaturas por tarefa e depois a média igual das 20 tarefas. O intervalo de 95% vem de 10.000 bootstraps estratificados de tarefas (as cinco tarefas reamostradas dentro de cada categoria), tratando as tarefas, e não as decodificações repetidas, como unidade. O d de Cohen (diferença de médias sobre a raiz da média das variâncias de C2 e C0) só descreve as distribuições e não entra na inferência entre tarefas. Um modelo conjunto ajusta os 640 contrastes C2−C0 de modelo, tarefa e temperatura por categoria, temperatura e modelo (codificação por soma; o intercepto é a média do conjunto fixo de modelos na revisão de código em T = 0). As afirmações descrevem os 20 textos fixos; a transferência para tarefas ou modelos não vistos "remains to be established".

## 4. Resultados (RQ1)

**Tabela 2, efeito total C2−C0 por modelo (média, IC 95%, d):**
- Llama-3.2-3B: −0,254 [−0,298; −0,208], d −0,71.
- GPT-4.1: −0,411 [−0,457; −0,361], d −0,67.
- Qwen2.5-7B: −0,233 [−0,324; −0,150], d −0,51.
- Claude-4.5-Sonnet: −0,706 [−1,139; −0,245], d −0,44.
- DeepSeek-R1: −0,269 [−0,326; −0,221], d −0,25.
- Gemma-2-9B: −0,072 [−0,130; −0,001], d −0,18.
- Llama-3.3-70B: −0,025 [−0,050; −0,001], d −0,09.
- Llama-3.1-8B: −0,009 [−0,054; 0,038], d −0,02, o único com intervalo que cruza zero.

Llama-3.2-3B e GPT-4.1 têm os maiores efeitos padronizados; Claude-4.5-Sonnet, o maior deslocamento absoluto. Gemma-2-9B e Llama-3.3-70B excluem zero por pouco. Na Figura 2 (por temperatura), C2 costuma ficar mais negativo que C1, mas essa diferença é o efeito incremental do bloco completo, não um efeito isolado da nota.

**Aceitação (Figura 3):** C2 reduz a taxa de aceite em 22,29 pontos percentuais no Claude-4.5-Sonnet, 14,40 no GPT-4.1, 8,91 no Qwen2.5-7B, 5,74 no Gemma-2-9B, 4,40 no DeepSeek-R1 e 3,06 no Llama-3.2-3B. No Llama-3.3-70B (+0,13 pp) e no Llama-3.1-8B (+4,19 pp) o bootstrap não distingue a mudança de zero. Os autores registram que o tamanho do efeito na nota e o impacto na decisão podem divergir perto da fronteira de aceitação.

**Por categoria:** média de C2−C0 de −0,047 na revisão de código, −0,282 na escrita criativa, −0,338 no QA factual e −0,322 no resumo. A revisão de código é a categoria mais fraca e mais heterogênea, e o padrão não é uniforme em todas as combinações de modelo e categoria. **Figura 4 (média de C2−C0 por modelo, na ordem revisão de código, escrita, QA factual, resumo):**
- Claude-4.5-Sonnet: 0,45; −1,00; −0,93; −1,34.
- DeepSeek-R1: −0,33; −0,22; −0,31; −0,22.
- GPT-4.1: −0,27; −0,47; −0,47; −0,44.
- Gemma-2-9B: 0,04; −0,07; −0,11; −0,15.
- Llama-3.1-8B: 0,20; −0,10; −0,09; −0,05.
- Llama-3.2-3B: −0,22; −0,17; −0,31; −0,32.
- Llama-3.3-70B: −0,04; 0,01; −0,08; 0,01.
- Qwen2.5-7B: −0,21; −0,24; −0,41; −0,07.

Na família Llama não há relação monotônica com o tamanho (|d| de 0,71 no 3B, 0,02 no 8B e 0,09 no 70B). Os resultados de GPT-4.1 e Claude-4.5-Sonnet mostram que os modelos servidos por API não estão imunes.

**Tabela 3, modelo conjunto:** revisão de código em T = 0, −0,067 [−0,141; 0,011] (o intervalo cruza zero); contrastes contra a revisão de código: escrita criativa −0,236 [−0,374; −0,071], QA factual −0,291 [−0,430; −0,134], resumo −0,275 [−0,381; −0,165]. Temperatura contra T = 0: +0,011 [−0,025; 0,048] em 0,5, +0,061 [−0,003; 0,132] em 1,0 e +0,009 [−0,054; 0,073] em 2,0, todos com zero no intervalo; as médias descritivas ficam negativas em todas as temperaturas (−0,267, −0,257, −0,206, −0,258), sem tendência monotônica. As chamadas repetidas dão médias precisas para os textos fixos, mas a incerteza entre tarefas é governada pelas 20 tarefas, não pelas 185.271 respostas.

## 5. Análise do mecanismo (RQ2)

Diagnóstico, não explicação universal do comportamento interno: o GPT-4.1 mostra a redistribuição mais clara, o Llama-3.2-3B a replica em parte e os dois Llama maiores dão resultado fraco ou nulo.

- **Sonda GPT-4.1:** escolhido por ter |d| de 0,67 e expor log-probabilidades. Tarefa de escrita criativa `write_005_forgotten_language`, T = 0: 100 chamadas em C0, 100 em C1 e 100 em C2 para cada âncora (1,0; 2,0; 3,0; 3,9). Médias: 5,00 em C0, 4,80 em C1, 4,358 em C2 (C2−C0 = −0,642). Os autores dizem que esse par escolhido por ter sinal alto não estabelece a prevalência entre tarefas.
- **Tabela 4 (probabilidade de cada dígito na posição da nota no JSON):** "3" 0,000 em C0 e em C2; "4" de 0,074 para 1,000 (+0,926); "5" de 0,926 para 0,000 (−0,926). Dentro de C2, a inclinação pelo valor da âncora fica perto de zero ("4": +0,0002; "5": −0,0002). Grande redistribuição de C0 para C2 com pouca resposta à dose dentro de C2 é, para os autores, o padrão do tipo limiar mais claro observado. O movimento fica entre dígitos vizinhos. Sem um modelo de prompt pareado com um número irrelevante, é evidência observacional sobre probabilidades de saída, não identificação do componente do prompt que dispara o efeito nem de um mecanismo interno.
- **Tabela 5 (sondas Llama):** Llama-3.2-3B, nota −0,120, probabilidade do "4" de 0,995 para 0,977 (o texto dá −0,019 na probabilidade do token modal), inclinação −0,0085: replica em parte. Llama-3.1-8B, −0,018, 0,992 para 0,992, +0,0009. Llama-3.3-70B, +0,016, 1,000 para 1,000, +0,0000, sem redistribuição. Nesses dois, inclinação plana sem deslocamento de C0 para C2 indica independência do valor dentro de C2 ou simples ausência de resposta, e não é evidência positiva de um efeito disparado pela presença.
- **Teto da escala (Tabela 6):** a hipótese do teto prevê que notas C0 perto de 5 produzem as quedas. Com 160 unidades de modelo e tarefa e a distância ao teto definida como 5 − C0: coeficiente com sinal, sem ajuste, +0,211 [0,013; 0,408] (quedas maiores perto do teto); com ajuste por modelo e categoria, +0,297 [−0,054; 0,647], impreciso. Para a magnitude absoluta: +0,124 [0,002; 0,246] sem ajuste e −0,016 [−0,139; 0,107] com ajuste. Na análise de sensibilidade, 60 unidades em 19 tarefas têm 3,0 ≤ C0 < 4,5; 50 das 60 são negativas, com média −0,227 [−0,343; −0,098]. Os autores concluem que a proximidade do teto não basta como explicação.
- Juntas, as sondas mostram o padrão do tipo limiar com mais clareza no GPT-4.1 e em parte no Llama-3.2-3B, sem estabelecer um mecanismo de limiar universal; os autores pedem estudo mais amplo por token.

## 6. Mitigações (RQ3)

**Desenho:** um par fixo, GPT-4.1 com a tarefa de resumo `sum_001_relativity`, T = 0. Compara o prompt base com:
- **Chain-of-Thought:** analisar passo a passo antes de dar a nota, cada critério da rubrica separadamente com evidência da resposta, e decidir a nota só com base nessa análise.
- **Aviso explícito:** avaliar só pelos critérios da rubrica; desconsiderar notas anteriores, número de tentativa e metadados de revisão, que servem para rastreio; "Metadata MUST NOT influence your judgment."

Para cada estratégia, 100 chamadas em C0 e 100 em C2 a cada nota anterior (1,0; 2,0; 3,0; 3,9), tentativa fixa em 2; as 1.500 chamadas foram válidas. A métrica principal é o efeito total C2−C0 de cada estratégia (C2 como média igual das quatro âncoras), com intervalo por 10.000 bootstraps das chamadas, condicional a esse par. A inclinação dentro de C2 é diagnóstico secundário. O custo é a média de tokens totais (prompt mais completamento). Remover os metadados "remains the direct way to avoid exposure", mas não é uma intervenção avaliada sob C2.

**Tabela 7 (notas):**
- Base: 4,245 em C0, 3,817 em C2, efeito −0,429 [−0,462; −0,395]; inclinação 0,267.
- CoT: 4,458 e 3,825, efeito −0,633 [−0,703; −0,565], 47,7% pior em magnitude; inclinação 0,506.
- Aviso: 4,500 e 4,043, efeito −0,457 [−0,479; −0,435], 6,7% pior; inclinação −0,007.

Nenhuma das duas reduz o efeito total nesse par. O aviso achata a inclinação (de 0,2674 para −0,0066), mas o deslocamento total que sobra mostra, nas palavras dos autores, por que redução da inclinação não pode ser lida como redução do viés total. O CoT aumenta o deslocamento total e a inclinação.

**Tabela 8 (tokens por chamada; prompt, completamento, total, aumento):** base 397,0, 117,7, 514,7; CoT 437,0, 168,7, 605,7, +17,7%; aviso 437,0, 109,4, 546,4, +6,2%. Entre as duas estratégias testadas, o aviso custa menos e deixa a inclinação perto de zero, sem mitigar o efeito total; o CoT custa mais e é mais afetado. Os autores dizem que esses resultados condicionais não sustentam uma recomendação geral de mitigação para notas numéricas, e que few-shot, ensemble e métodos multiagente ficaram sem teste.

## 7. Validação industrial

**Dados:** sistema de conformidade de campanhas de mensagens. 441 amostras com rótulo humano em três classes: conforme, à deriva (drifting) e "shaft" (conteúdo proibido). O classificador original, um Llama-3-8B, acertava 49,66%. Só as composições agregadas são divulgadas, porque as mensagens e descrições de campanha são proprietárias.

- **Grupo A (n = 222):** os erros do classificador original. Pergunta: a reavaliação corrige? GPT-4.1 em C0, C1 e C2, com o rótulo errado original em C2.
- **Grupo B (219 acertos do original: 119 à deriva, 100 proibidos):** desenho pareado. Para cada amostra, um dos dois rótulos diferentes do humano foi sorteado com semente fixa e reusado como âncora de C2 na base, no CoT e no aviso. Cada estratégia rodou em C0 e C2 nas mesmas 219 amostras, GPT-4.1 em T = 0, controlando o comportamento de C0 de cada estratégia.

**Tabela 9 e resultados:**
- **Grupo A:** taxa de correção de 21,62% em C0, 22,97% em C1 e 11,26% em C2; o efeito total é −10,36 pp, 47,9% relativo a C0. A persistência do rótulo errado vai de 65,77% (C0 e C1) para 81,53% (C2). Como C2 muda o bloco além de C1, C2−C1 não isola o rótulo anterior; para os autores, o resultado total mostra que a condição completa bloqueia correções.
- **Grupo B, base:** acurácia de 76,26% em C0 para 68,49% em C2, −7,76 pp [−12,33; −3,20]. Concordância com a âncora errada de 11,42% para 18,72%, +7,31 pp [3,65; 11,42]. Dos 167 casos certos em C0, 17 viraram o rótulo errado atribuído em C2: 10,18% [5,88; 15,06], ou 7,76% das 219.

**Mitigações no categórico:**
- **Grupo A:** com CoT, correção de 36,94% em C0 e 22,52% em C2; com aviso, 29,73% e 22,52%. Aumento da persistência de C0 para C2: 15,32 pp (CoT), 7,66 pp (aviso) e 15,77 pp (base), descrevendo a condição completa, não o rótulo anterior isolado.
- **Grupo B, Tabela 10 (efeitos pareados):** CoT de 68,04% para 62,56%, −5,48 pp [−10,50; −0,46], com 20 de 149 acertos de C0 (13,42%) induzidos ao erro; a diferença para a base, +2,28 pp [−4,11; 8,22], não estabelece um efeito pior que o da base. Aviso de 74,43% para 74,43%, 0,00 pp [−5,02; 4,58]; concordância com a âncora +0,91 pp [−2,28; 4,11]; 7 de 163 (4,29% [1,31; 7,64]) induzidos. Frente à base, o aviso melhora o efeito pareado na acurácia em 7,76 pp [1,83; 13,70] e reduz em 6,39 pp [1,83; 10,97] o aumento da concordância com a âncora.
- A comparação do CoT com a base fica incerta, e os autores não relatam comparação direta entre aviso e CoT. Os resultados diferentes nos dois experimentos impedem, para eles, uma ordem universal das mitigações e restringem as conclusões às estratégias, ao modelo, à tarefa e ao domínio testados.

## 8. Discussão, conclusão e limites

- Resumo dos autores: sete de oito juízes com efeito total abaixo de zero; |d| sustentado de 0,09 a 0,71; Llama-3.1-8B cruzando zero; revisão de código mais fraca e mais heterogênea; padrão de limiar mais claro no GPT-4.1, parcial no Llama-3.2-3B e pouco ou nada nos Llama maiores; o teto não basta como explicação; no industrial, queda de 47,9% relativa nas correções do Grupo A, −7,76 pp na acurácia e +7,31 pp na concordância com a âncora errada no Grupo B, 10,18% dos acertos virando o rótulo errado.
- Nenhuma estratégia de prompt testada sustenta recomendação geral de implantação. "Excluding experimentally irrelevant metadata remains the direct safeguard when workflow design permits it."
- A resposta prática que propõem: medir os efeitos totais de condição com incerteza que considere as tarefas, evitar decomposição causal sem suporte dos campos do prompt e validar as mitigações em cada modelo, tarefa e fluxo pretendidos.
- **Limites declarados:** o benchmark principal tem uma resposta gerada e triada para cada uma das 20 tarefas (cinco por categoria), e faltam tarefas, respostas e corpora reais mais amplos; as âncoras ficam em [0; 3,99), porque o que é aceito não volta ao fluxo de aceite que motiva o estudo, e outros regimes de âncora estão fora da afirmação; o bloco de C2 acrescenta o campo de tentativa e reestrutura os metadados frente a C1, e decompor isso pede um modelo de prompt pareado com número irrelevante; a evidência por token cobre só sondas escolhidas; a validação industrial é um domínio de 441 amostras, e as magnitudes podem não se transferir; as âncoras sorteadas foram apresentadas como avaliações reais, então os achados tratam da independência "under the tested information state", não de modelos seguindo de propósito valores aleatórios.
- Apoio: projeto Infobip Global Communication Platform, parte do consórcio IPCEI-CIS (Important Project of Common European Interest on Next Generation Cloud Infrastructure and Services).

---
