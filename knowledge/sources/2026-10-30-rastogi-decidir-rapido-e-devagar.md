---
titulo: "Deciding Fast and Slow: The Role of Cognitive Biases in AI-assisted Decision-making"
tipo: paper
autor: "Charvi Rastogi, Yunfeng Zhang, Dennis Wei, Kush R. Varshney, Amit Dhurandhar, Richard Tomsett"
url: "https://arxiv.org/abs/2010.07938"
publicado_em: 2020-10-15
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv; o registro do DOI 10.1145/3512930 no Crossref também traz CC BY 4.0 para a versão da ACM)"
areas: [agent-engineering]
tags: [human-in-the-loop, anchoring, automation-bias, overreliance, time-allocation, ai-confidence, cognitive-biases, bayesian-modeling, human-ai-complementarity]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 15/10/2020 e v2 (lida) em 04/04/2022; o comentário do arXiv diz "22 pages, 4 figures". O texto da v2 não menciona a revista; a versão publicada tem o DOI 10.1145/3512930, que o Crossref registra em Proceedings of the ACM on Human-Computer Interaction, vol. 6, CSCW1, com data de 30/03/2022 (a página do arXiv não liga esse DOI). Carnegie Mellon University (Rastogi), Twitter (Zhang), IBM Research (Wei, Varshney, Dhurandhar) e Onfido (Tomsett). O integral foi extraído do PDF da v2; as Figuras 2 e 4 são só gráfico, e os valores lidos delas vêm com "cerca de". Lida (camadas flexíveis de avaliação).

## O resumo

Na decisão assistida por IA, a pessoa consome a previsão do modelo e decide no fim, mas a percepção dela é distorcida por vieses cognitivos (confirmação, ancoragem, disponibilidade). Os autores modelam matematicamente os vieses num arcabouço que mostra a interação entre eles e a acurácia humano e IA, e se concentram na ancoragem. Implementam uma estratégia de desancoragem por tempo e a validam num primeiro experimento; daí desenham uma alocação de tempo para recursos limitados, ótima sob certas hipóteses, e num segundo experimento mostram que essa alocação, junto com a explicação, desancora a pessoa e melhora o desempenho conjunto quando a IA tem baixa confiança e está errada.

## 1. Introdução

- A frase de abertura parodia Jane Austen ("It should be a truth universally acknowledged that a human decision-maker in possession of an AI model must be in want of a collaborative partnership"). Exemplos de uso de modelos como apoio em decisões de alto risco: saúde, empréstimo, justiça criminal, recrutamento, monitoramento de fraude.
- As perguntas sobre quando confiar na IA são tratadas como problema de comunicação entre IA e humano; a parte frequentemente deixada de lado é o próprio humano que recebe a comunicação.
- Vieses cognitivos (Tversky e Kahneman, 1974): padrão sistemático de desvio da racionalidade em que a pessoa cria uma "realidade subjetiva" a partir da percepção da entrada.
- **Figura 1, três espaços:** o espaço percebido (o decisor) interage com o espaço observado (atributos e tudo o que o decisor sabe da tarefa) e com o espaço de previsão (a saída da IA: decisão, explicação etc.). Viés de confirmação, viés de disponibilidade, heurística da representatividade e acessibilidade seletiva ficam no espaço observado; ancoragem e efeito da evidência fraca, no espaço de previsão.
- **Definição de ancoragem usada:** a pessoa forma uma percepção enviesada por causa de uma âncora (a decisão da IA) disponível para ela, o que limita a exploração de hipóteses alternativas; "Anchoring bias manifests through blind reliance on the anchor". Os autores dizem que a confiança mal calibrada na IA já foi estudada pela lente da confiança (trust), e que a ancoragem tem outro mecanismo e, por isso, outras estratégias de mitigação.
- **Ancorar e ajustar:** a pessoa ajusta pouco a partir da âncora; Lieder et al. explicam o ajuste insuficiente como uma troca racional, dados os recursos limitados, entre acurácia e tempo. Daí o teste: dar mais tempo alivia a ancoragem? Os autores dizem que a utilidade do tempo é uma ideia intuitiva já discutida, mas não validada empiricamente até onde sabem.
- **O problema de alocação:** dar mais tempo a todas as decisões não aproveita os casos em que a IA é boa e ignora que o tempo é limitado. Exemplo: sistemas de monitoramento de fraude em compras que analisam dezenas de milhares de faturas por dia e sinalizam uma fração que já sobrecarrega a equipe de especialistas; e juízes que decidem sobre muitos documentos, às vezes em menos de um minuto.
- **Contribuições:** um arcabouço bayesiano enviesado; mostrar com pessoas que mais tempo reduz a ancoragem; formular o problema de alocação de tempo; propor a alocação por confiança e as condições em que é ótima; e avaliá-la num experimento, mostrando que, com a informação de confiança à vista, ajuda a desancorar de previsões erradas e de baixa confiança.

## 2. Trabalhos relacionados

- Vieses cognitivos em decisão e em sistemas de apoio à decisão; confirmação, ancoragem, viés de automação (Lee e See, 2004) e disponibilidade. Citação de Lee e See: "Poor partnerships between people and automation will become increasingly costly and catastrophic".
- Trabalhos sobre colaboração humano e IA testam técnicas de explicação guiadas por heurística; em Bansal et al. (2021), explicações que sustentam a decisão da IA tendem a aumentar a overreliance. Miller (2019) pede que a comunidade de ML se apoie em como as pessoas selecionam explicações; os autores concordam e se apoiam na psicologia dos vieses. Adotam um processo em duas etapas, em que o segundo experimento é desenhado a partir do primeiro.
- Trabalhos sobre vieses em colaboração humano e IA ainda são raros: Fürnkranz et al. e Kliegr et al. (específicos de modelos baseados em regras), Baudel et al. (viés de complacência ou autoridade em decisões de negócio), Wang et al. (arcabouço conceitual de XAI a partir de vieses). Buçinca et al. (2021), contemporâneo, usa funções de forçamento cognitivo contra a overreliance.
- A ancoragem em decisões assistidas por IA também foi estudada "as a part of automation bias", em que os usuários confiam demais na IA por confiança cega na automação. Estudos anteriores: as pessoas não calibram a confiança pela acurácia da IA (Green e Chen), não detectam erros do algoritmo, são enviesadas por informação irrelevante, confiam em algoritmos descritos como de baixa acurácia e em algoritmos descritos como precisos que dão previsões aleatórias. Os autores dizem ser o primeiro trabalho a estudar, empírica e analiticamente, uma estratégia de desenviesamento por tempo contra a ancoragem em decisões assistidas por IA.
- Park et al. (2019) forçam o decisor a deliberar antes de a previsão da IA aparecer; aqui o cenário é o oposto, com a previsão da IA mostrada antes, o que pode gerar ancoragem, e o tempo é tratado como recurso limitado.

## 3. Problema e modelagem

- **Cenário:** classificação binária; a classe verdadeira é y*, os atributos disponíveis são D, a saída da IA é f(M) (previsão ŷ e, se houver, explicação), e a decisão humana é ỹ.
- **Decisor racional:** bayesiano ótimo, escolhe a classe de maior probabilidade a posteriori combinando a priori e a verossimilhança dos dados; com a IA, supõe-se que, dada a decisão, a pessoa percebe D e f(M) de forma condicionalmente independente (Equação 3).
- **Decisor enviesado (Equação 4):** cada fator recebe um expoente, α nos dados, β na saída da IA e γ na priori, seguindo trabalhos que usam vieses exponenciais (parâmetros de temperatura inversa) na inferência bayesiana. Na razão entre as duas classes (Equação 5):
  - Ancoragem: β > 1, o peso da previsão da IA cresce e o da priori e dos dados cai.
  - Viés de confirmação: γ > 1, o peso da priori cresce.
  - Acessibilidade seletiva: distorce o fator dos dados, com α > 1 ou α < −1 conforme a direção.
  - Efeito da evidência fraca (diante de evidência fraca para uma previsão, escolher a oposta): β < −1.
- Os autores escolhem a ancoragem por ser específica da colaboração humano e IA e ter aparecido como problema em trabalhos anteriores.

## 4. Ancoragem e o Experimento 1

**Base:** depois de ancorada, a pessoa ajusta pouco, porque ajustar dá trabalho e para quando chega a uma estimativa plausível; no modelo racional de recursos de Lieder et al., isso é uma troca entre tempo e acurácia, consequência da racionalidade limitada (satisficing: aceitar o bom o bastante). Epley e Gilovich apontam carga cognitiva e pressão de tempo como fatores do ajuste insuficiente. "Desancorar" é o nome que os autores dão ao processo racional de se afastar da âncora.

**Medida de ancoragem:** a probabilidade de a pessoa concordar com a previsão da IA, P(ỹ = ŷ). Pela Equação 6, se a probabilidade do modelo de dar ŷ é maior quando ŷ coincide com a decisão, quanto maior β, maior a chance de a decisão humana ser ŷ; no limite β → ∞, a concordância é 1; com β = 1, os três fatores pesam de forma apropriada e a concordância fica num valor de base natural. Os autores ressalvam que a medida tem de vir de tarefas em que a pessoa tem razão para escolher outra previsão.

**H1:** aumentar o tempo de uma tarefa alivia a ancoragem, com mais chance de ajuste suficiente para longe da decisão da IA quando a pessoa tem o conhecimento para dar outra previsão.

**Participantes:** 47 pessoas do MTurk nos EUA, com aprovação de pelo menos 98% e mínimo de 100 tarefas aprovadas; 10 entre 18 e 29 anos, 26 entre 30 e 39, 6 entre 40 e 49 e 5 acima de 50. Tempo médio de 27 minutos; US$ 4,50 (US$ 3,50 de base e US$ 1 de bônus por acurácia), cerca de US$ 10 por hora.

**Tarefa e IA:** prever se um aluno passa ou reprova, com o Student Performance Dataset do UCI (1.044 instâncias, duas disciplinas, matemática e português, 33 atributos), rótulos binarizados e divisão 70/30 entre treino e teste. A IA é uma regressão logística; ficaram os 10 atributos de maior coeficiente (escolaridade e profissão da mãe e do pai, horas semanais de estudo, interesse em ensino superior, horas semanais saindo com amigos, faltas no ano, reforço escolar e reprovações anteriores na disciplina).

**Procedimento:**
- **Treino:** 15 tentativas iguais para todos, com a resposta certa mostrada depois de cada uma, distribuídas uniformemente nas faixas de probabilidade prevista de 0,5 a 1 (a probabilidade como proxy de dificuldade). Gráficos de barras com a distribuição do resultado por atributo só no treino.
- **Para induzir a ancoragem:** os participantes foram informados no início de que a IA tinha 85% de acurácia (as tentativas de treino foram escolhidas para que ela acertasse 85% delas), enquanto a acurácia real era 70,8% no conjunto de treino e 66,5% no de teste. Os autores justificam a acurácia declarada alta pelo treino curto e dizem que essa diferença é realista se houver mudança de distribuição entre treino e teste, o que tornaria a confiança das pessoas mal colocada. A previsão da IA em cada tentativa de treino era mostrada depois da tentativa.
- **Teste:** 36 tentativas do conjunto de teste, iguais e na mesma ordem para todos; decisão com os dados do aluno e a previsão da IA; a pessoa também declarava a confiança na própria previsão (baixa, média ou alta). O texto não relata resultados dessa confiança.
- **Tentativas-sonda (probe trials):** 8 tentativas de dificuldade média (probabilidade prevista de 0,6 a 0,8) em que a IA acertava, com a previsão mostrada invertida; com a âncora, a pessoa erraria, e com conhecimento poderia se afastar. Poucas, para não destruir a confiança na IA. As demais, não modificadas, sorteadas com distribuição uniforme da probabilidade prevista. A acurácia da IA mostrada no teste foi 58,3%, bem abaixo dos 85% anunciados.
- **Tempo:** um piloto indicou que 10, 15, 20 e 25 segundos cobriam do necessário ao suficiente. O teste foi dividido em quatro blocos de 9 tentativas (2 sondas e 7 não modificadas, em ordem aleatória), cada bloco com um tempo, numa permutação aleatória por participante. Não era possível avançar antes de o tempo acabar. A randomização do tempo, independente do participante, do desempenho e da sequência, permite isolar o efeito do tempo.

**Resultados (Figura 2):**
- A discordância com a IA é muito maior nas sondas que nas não modificadas em todos os tempos, o que os autores leem como sinal de que os participantes aprenderam a tarefa. Nas não modificadas, a discordância fica perto de 0,1 em todos os tempos, e os autores concluem que o conhecimento dos participantes era parecido ou menor que o da IA.
- **Sondas:** a discordância média sobe de 48% com 10 s para 67% com 25 s. Regressão linear da discordância média pelo tempo nas sondas, com 5.000 reamostragens bootstrap: coeficiente 0,01, IC 95% [0,001; 0,018], significativamente positivo; como as escalas não foram ajustadas, 0,01 equivale a +0,15 de discordância entre 10 s e 25 s. Consistente com H1. Na Figura 2(a), as sondas aparecem em cerca de 0,49 (10 s), 0,57 (15 s), 0,54 (20 s) e 0,66 (25 s).
- **Adesão ao tempo (Figura 2b):** a distribuição do tempo de resposta acompanha os quatro limites; com 10 s, o pico fica em cerca de 6 s. O tempo medido é o do último clique no botão, e a pessoa pode ter pensado mais. No questionário final, sobre usar o tempo inteiro: frequentemente 15, ocasionalmente 24, raramente 6, nunca 2.

## 5. Alocação ótima de recursos

- **Formulação:** com um orçamento total de tempo T para N decisões, maximizar a acurácia média da equipe. A acurácia de cada tentativa se decompõe (Equação 7) na probabilidade de concordar com a IA quando ela acerta (a ancoragem ajuda) e de discordar quando ela erra (a ancoragem atrapalha); o tempo muda só as probabilidades de concordância, não a correção da IA (Equação 8).
- Como identificar a correção real da IA é difícil, usam a confiança estimada pelo próprio modelo (a probabilidade da classe prevista), C_i, binarizada em baixa (C_L) e alta (C_H), com tempos t_L e t_H (Equação 9).
- **Figura 3, o caso ideal:** confiança separa bem os casos, acurácia da IA perfeitamente correlacionada com a confiança, humano melhor que a IA na baixa confiança e pior na alta. Mais tempo na baixa confiança estimula a pessoa a usar o próprio conhecimento; menos tempo na alta, onde a ancoragem prejudica menos e até ajuda: o "best of both worlds".
- **Hipótese 1 (Equação 10):** com mais tempo, a acurácia esperada não cai na baixa confiança e não sobe na alta. **Proposição 1:** sob essa hipótese, o ótimo é dar o tempo mínimo permitido à alta confiança e o máximo compatível com o orçamento à baixa. Na implementação real, como a confiança da IA é só uma aproximação, os autores recomendam um tempo mínimo acima de zero, para haver supervisão humana caso a confiança esteja mal calibrada.
- **Linhas de base:** tempo constante (T/N para todas) e tempo aleatório (os mesmos t_L e t_H, sorteados na mesma proporção).
- **Apêndice A:** justificativa da Hipótese 1 (no tempo zero, a acurácia condicional é a da IA; pelo Experimento 1, a discordância com a IA errada cresce ou fica igual com o tempo, e a concordância com a IA certa cai ou fica igual; supondo correlação positiva entre baixa confiança e baixa acurácia, na baixa confiança domina o termo da IA errada e a acurácia cresce com o tempo; na alta, domina o da IA certa e ela cai) e o Corolário 1, com prova: sob a Hipótese 1, a alocação por confiança tem acurácia maior ou igual à constante e à aleatória.

## 6. Experimento 2

**Desenho:** t_L = 25 s e t_H = 10 s, a partir do Experimento 1. Conjectura adicional: explicar a razão da alocação (informar a confiança da IA) ajudaria, apoiada em Chambon et al. (2020), em que o cérebro aprende mais rápido com escolhas livres que com forçadas.

**Hipóteses:** H2, a ancoragem prejudica a acurácia conjunta quando a IA erra; H3, com conhecimento complementar, mais tempo ajuda a se afastar da previsão da IA; H4, a alocação por confiança rende mais que o humano sozinho e que a IA sozinha; H5, rende mais que as alocações constante e aleatória; H6, a alocação por confiança com explicação rende mais que as outras condições.

**Participantes:** 479, recrutados como antes; 83 entre 18 e 29 anos, 209 entre 30 e 39, 117 entre 40 e 49 e 70 acima de 50; 30 minutos em média; US$ 5,125 em média (US$ 4,125 de base e US$ 1 de bônus), cerca de US$ 10,25 por hora.

**Tarefa e IA:** a mesma tarefa. Para simular conhecimento complementar (o que acontece quando o decisor tem perícia que a IA não tem, como em políticas sociais e design), a IA foi treinada com 7 atributos e os participantes viam 3 a mais (horas de estudo, horas saindo com amigos e reforço escolar, o 2º, 3º e 4º mais importantes num modelo completo). Alta confiança: C_i ≥ 0,75. Teste com 40 questões, 20 de baixa e 20 de alta confiança, sorteadas com probabilidade prevista uniforme, conjunto fixo e ordem aleatória por participante. O treino foi igual ao do Experimento 1, de novo com os "85%" anunciados.

**Grupos (sorteio entre cinco):**
- *Human only* (n = 95): sem a previsão da IA, 25 s por tentativa, julgados suficientes pelo Experimento 1.
- *Constant time* (n = 109): com a IA, 17,5 s por tentativa (média de t_L e t_H), anunciados como 18 s.
- *Random time* (n = 95): 10 ou 25 s sorteados por tentativa, com média de 17,5 s.
- *Confidence-based time* (n = 85): 25 s na baixa confiança, 10 s na alta.
- *Confidence-based time with explanation* (n = 96): o mesmo, mais a confiança da IA ("low" ou "high") mostrada em cada tentativa.
- Nos grupos que alternam 10 e 25 s, as tentativas vinham em blocos de 5 com o mesmo tempo (8 blocos), para evitar troca rápida.

**Resultados (texto e Figura 4):**
- **Conhecimento complementar:** IA sozinha e Human only com acurácia geral parecida, de cerca de 60%, e Human only concordando com a IA em só 62,3% das tentativas. Com a IA errada, Human only acertou 61,8% na baixa confiança e 29,8% na alta; os participantes tinham mais conhecimento complementar na baixa confiança.
- **H4:** acurácia de 61% em Confidence-based time e 61,9% com explicação, contra 61,9% de Human only e 60% da IA. Confidence-based time acima da IA sozinha com p = 0,06, t(183) = 1,52; sem evidência suficiente de superar Human only (p = 0,58, t(92) = −0,21). Com explicação, acima da IA sozinha (p = 0,004, t(194) = 2,66) e sem significância contra Human only (p = 0,5, t(189) = −0,02).
- **H2:** a concordância de Human only é muito menor que a dos grupos com IA (p < 0,001, t(184) = 6,73); com a IA errada, a ancoragem reduziu a acurácia frente a Human only (p < 0,001, t(370) = −6,68). Os autores ressalvam que Human only tinha mais tempo em média (25 s); comparando só as tentativas de baixa confiança, em que Human only e Confidence-based time tinham os mesmos 25 s, a diferença se repete na concordância (p < 0,001, t(92) = 4,97) e na acurácia (p < 0,001, t(92) = −4,74). Consistente com H2.
- **H3:** Confidence-based time sozinho não bastou para se afastar da IA errada; com explicação, houve redução significativa da ancoragem nas tentativas de baixa confiança frente às outras condições (p = 0,003, t(383) = 2,70), e acurácia mais alta nessas tentativas: 43,8%, contra 36,2% em Random time, 36,4% em Constant time e 37,5% em Confidence-based time. Os autores dizem que o conjunto de condições não permite separar o efeito da alocação de tempo do efeito da explicação de confiança.
- **H5 e H6:** acurácia geral de 61,9% com explicação, 61% em Confidence-based time, 61,1% em Random time e 61,5% em Constant time. Confidence-based time não difere significativamente dos outros grupos colaborativos (H5); com explicação tem a maior acurácia, sem significância (p = 0,19, t(383) = 0,84) (H6). Os resultados de todos os grupos colaborativos são parecidos, exceto nas tentativas com a IA errada e de baixa confiança, em que o grupo com explicação acerta significativamente mais; daí os autores dizem que, onde há propensão à overreliance, a alocação por confiança com explicação melhora o desempenho da equipe.
- **Por que Confidence-based time não supera os outros no geral:** os autores atribuem à acurácia e à concordância relativamente baixas na alta confiança. Esperavam concordância alta nas tentativas de 10 s; observaram 84% de concordância em C_H, contra 87,9% em Random time e 88,1% em Constant time (estes com 17,5 s em média), o que se traduz em 86% de acurácia quando a IA acerta. O texto não dá teste estatístico para essas três concordâncias.
- **Leituras da Figura 4:** em (a), a acurácia com a IA errada e baixa confiança (triângulos vermelhos) fica em cerca de 0,44 com explicação, 0,34 em Confidence-based time, 0,38 em Random time, 0,36 em Constant time e 0,62 em Human only; na linha AI only, além do losango em cerca de 0,60, há dois marcadores sem legenda, em cerca de 0,50 e 0,70. Em (b), a concordância com a IA errada e baixa confiança fica em cerca de 0,55 com explicação, 0,65 em Confidence-based time, 0,60 em Random time, 0,62 em Constant time e 0,37 em Human only; os dois marcadores de C_H de Confidence-based time aparecem em cerca de 0,88 (o texto dá 84% de concordância em C_H), e os de Human only em C_H em cerca de 0,73 (IA errada) e 0,83 (IA certa).

## 7. Discussão

- **Lições:** Confidence-based time tem concordância baixa na alta confiança, onde o tempo é 10 s e a IA acerta 70%; segundo o texto, menor que a de Human only e de Constant time em C_H, tanto com a IA certa quanto errada. Os autores sugerem que esses participantes podem ter passado a desconfiar da IA, porque discordaram mais em média e gastaram mais tempo nas tentativas em que discordaram (sem número no texto); a desconfiança poderia vir de os tempos longos irem só para a baixa confiança, dando a impressão de uma IA pior do que é. A explicação da alocação reduz esses efeitos. Os autores destacam a importância de considerar o comportamento humano nessas tarefas.
- **Sequencialidade:** o modelo deveria considerar que o decisor continua aprendendo e formando a percepção da IA ao longo da tarefa; propõem estudar modelos cognitivos dinâmicos (como os markovianos já usados em decisão humana) para políticas mais informadas.
- **Limites declarados:** os participantes não são especialistas em avaliação de alunos (mitigado com treino, estatísticas do domínio e atributos extras; a acurácia de Human only parecida com a da IA é, para os autores, sinal de que funcionou); só quatro tempos testados (10, 15, 20 e 25 s), por recursos limitados; especialistas reais seriam caros, e a abordagem se enquadra como "human grounded evaluation" (Doshi-Velez e Kim), com leigos como proxy para padrões gerais de comportamento; tarefa não crítica, sem responsabilidade pelas consequências, mitigada com bônus por resultado; não dá para separar o efeito independente da explicação de confiança; e uma única tarefa de decisão, sendo preciso verificar se os efeitos se generalizam a outros domínios.
- **A afirmação de generalização:** logo depois desse limite, os autores dizem que "prior research provides ample evidence that even experts making critical decisions resort to heuristic thinking, which suggests that our results will generalize broadly". Nesse trecho, o apoio é só essa frase, que não traz referência; na introdução, os autores dizem que o trabalho se aplica também aos outros domínios citados, como processos criminais em que juízes decidem rápido sobre muitos documentos.
- **Conclusões dos autores:** com a estratégia de alocação, o desempenho da equipe fica acima da IA sozinha e acima do humano sozinho nos casos em que a IA acerta; quando a IA erra, a informação dela distrai a pessoa da decisão certa; informar a confiança da IA como explicação da alocação alivia parte disso e aproxima do desempenho ideal da Figura 3.
- **Trabalhos futuros:** estudar outros vieses, como confirmação e efeito da evidência fraca; desenhar estratégias de explicação a partir dos vieses do decisor; usar o arcabouço de alocação de recursos para outros vieses e suas estratégias de desenviesamento.
- Financiamento: NSF CIF 1763734 (Rastogi).

---
