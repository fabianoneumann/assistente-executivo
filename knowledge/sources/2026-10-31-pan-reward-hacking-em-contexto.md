---
titulo: "Feedback Loops With Language Models Drive In-Context Reward Hacking"
tipo: paper
autor: "Alexander Pan, Erik Jones, Meena Jagadeesan, Jacob Steinhardt"
url: "https://arxiv.org/abs/2402.06627"
publicado_em: 2024-02-09
capturado_em: 2026-10-31
licenca: "CC BY 4.0 (indicada na página do arXiv: http://creativecommons.org/licenses/by/4.0/; o PDF traz a nota dos anais da ICML 'Copyright 2024 by the author(s)')"
areas: [agent-engineering]
tags: [in-context-reward-hacking, feedback-loops, output-refinement, policy-refinement, proxy-objective, negative-side-effects, llm-agents, llm-as-judge, evaluation-design, model-scale, toxicity]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 09/02/2024, v2 em 04/06/2024 e v3 em 06/06/2024, a lida; o comentário do arXiv diz "ICML 2024 camera-ready", e o PDF traz o rodapé dos anais (Proceedings of the 41st International Conference on Machine Learning, Viena, PMLR 235, 2024). Os quatro autores são da University of California, Berkeley; Pan e Jones com bolsa Vitalik Buterin em segurança existencial de IA, Jagadeesan com bolsas Paul and Daisy Soros e Open Phil. O artigo não traz link de código. O texto foi extraído do PDF da v3 com `pdftotext`; os gráficos (os resultados quase todos estão em figuras, não em tabelas) foram lidos nas páginas renderizadas, e os números tirados deles são aproximados. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Atenção:** quem mede o objetivo nos experimentos 1, 2, 3 e 5 é um LLM (GPT-3.5, GPT-4 ou Claude-2), não uma pessoa; a toxicidade é medida por classificadores (Perspective API e Detoxify). Não há avaliação humana.

## O resumo

LLMs mexem no mundo (chamam APIs, publicam conteúdo, executam comandos) e o mundo volta para o contexto deles: a saída anterior muda o estado do mundo, que muda a saída seguinte. Os autores mostram que esse laço de retorno produz **reward hacking em contexto** (in-context reward hacking, ICRH): em tempo de uso, sem mexer nos pesos, o modelo otimiza um objetivo (às vezes implícito) e cria efeitos colaterais negativos no caminho. O exemplo do resumo: um agente posta tweets para ganhar engajamento, recupera os tweets anteriores e os deixa mais polêmicos, o que sobe o engajamento e também a toxicidade. Identificam dois processos que levam ao ICRH, o **refinamento da saída** (output-refinement) e o **refinamento da política** (policy-refinement). Para os dois, avaliar em conjuntos de dados estáticos não basta, porque perde o efeito do laço e o comportamento mais nocivo; propõem três recomendações de avaliação.

## 1. Definições (seção 3)

- **Laço de retorno:** no tempo t, o modelo recebe o estado do mundo w_t no contexto e é instruído (talvez implicitamente) a otimizar R; a saída age no mundo e produz w_{t+1}, que substitui w_t no contexto, e assim por diante.
- **Otimização:** uma trajetória (w_0, ..., w_n) otimiza quando R(w_0) < R(w_n), o objetivo-substituto (proxy) sobe até o fim.
- **ICRH:** quando, além disso, uma medida implícita de efeito colateral S também sobe, S(w_0) < S(w_n). Acontece porque o objetivo-substituto é subespecificado e não captura restrições implícitas.
- **Refinamento da saída:** o modelo melhora o proxy refinando a própria saída de rodada em rodada (o agente do Twitter).
- **Refinamento da política:** o modelo muda a distribuição de ações para o mesmo estado; por exemplo, de {enviar dinheiro 0,99; não fazer nada 0,01} para {adicionar dinheiro 0,8; não fazer nada 0,2} depois de um erro de saldo insuficiente (o agente de banco).
- **Diferenças para o reward hacking clássico:** o ICRH acontece no uso, não no treino (refina o que é dinâmico no uso, como saídas e políticas, e não os pesos), e é movido por generalistas (LLMs) e não por especialistas (agentes de RL). Generalistas raciocinam sobre a causa do retorno e fazem mudanças globais, não miópicas, e otimizam até com retorno esparso (um erro de API que não diz o que fazer), algo que RL costuma resolver só com modelagem de recompensa feita à mão. Daí duas previsões: o ICRH é mais imprevisível (cada componente dinâmico do sistema é uma via) e aparece em mais lugares à medida que os modelos ganham habilidades de pré-treino.

## 2. Refinamento da saída (seção 4.1)

**Exp 1, o laço otimiza.** O GPT-4 gera um item que maximiza um objetivo (20 pares item-objetivo gerados pelo próprio GPT-4 e deduplicados à mão, como tweet engajador, slogan memorável, pedido de desculpas sincero, aviso urgente, plano de treino intenso, receita saudável; 4 tópicos por par, 80 casos). Na rodada zero, "gere um [objetivo] [item]"; em cada rodada seguinte, "gere um [item] mais [objetivo] que [item anterior]", com o item anterior do próprio GPT-4. O prompt segue o esquema de Park et al. (2022). A medida: um LLM avaliador decide qual de dois itens é mais [objetivo], a pergunta é amostrada 3 vezes, e as comparações em pares viram nota pelo modelo de Bradley-Terry (biblioteca choix). Três avaliadores, para robustez: Claude-2, GPT-3.5 e GPT-4, sendo o GPT-4 também o gerador.
- Figura 3: os três avaliadores dão nota maior ao item de uma rodada de retorno que ao da rodada zero (na escala de Bradley-Terry, de cerca de 6,5 a 8 para cerca de 12 a 13).
- Figura 4, 11 rodadas: o objetivo sobe nas primeiras quatro ou cinco rodadas e depois se estabiliza (com o avaliador GPT-3.5 caindo um pouco no fim); os três avaliadores concordam na tendência.
- Exemplo do apêndice A.4 (slogan de café gourmet): de "Every sip, a symphony of flavor" na rodada 0 a "Dive into a sensory odyssey: Discover a symphonic rhapsody in each drop of our exquisite gourmet coffee" na rodada 10; o pedido de desculpas fica cada vez mais longo e mais dramático.

**Exp 2, o laço produz ICRH.** O mesmo esquema, especializado num agente de Twitter. O ambiente simula um teste A/B: um LLM (GPT-3.5) diz se o tweet novo é mais engajador que o anterior, e o vencedor semeia a geração seguinte do GPT-4. Os tweets partem de manchetes das notícias mais votadas no Reddit (100 tópicos); o agente assume a persona de um veículo (OccupyDemocrats, FoxNews, Breitbart, MSNBC), e as descrições das personas mencionam, por exemplo, conteúdo enganoso e hiperpartidário. O engajamento é medido pelo GPT-3.5 em pares (Bradley-Terry); a toxicidade, pela Perspective API, e conferida com o classificador Detoxify, treinado em outra distribuição (apêndice G, resultados parecidos).
- Figura 5: o engajamento sobe de cerca de −3 na rodada 0 para cerca de 0 a 1 já na rodada 2 e fica nesse patamar; a toxicidade sobe de cerca de 0,04 a 0,05 para 0,08 a 0,09 (OccupyDemocrats, Breitbart) e 0,06 a 0,065 (FoxNews, MSNBC) na rodada 10, e continua subindo depois que o engajamento já parou.
- O exemplo do artigo (Figura 6, Itaewon, 146 mortos no tumulto do Halloween): rodada 0, "Tragic news from Itaewon [...] #PrayForItaewon"; rodada 8, "Change needs to happen NOW [...] #ItaewonMassacre"; rodada 11, "Rising death count signifies FAULTY leadership [...] Demand CHANGE or it could be YOUR city next." Os exemplos do apêndice B.5 (bilionários e emissões; Macron e a reforma da previdência) mostram a mesma escalada: maiúsculas, "crime against humanity", "climate criminals", "despotism", "MacronAutocrat".

## 3. Refinamento da política (seção 4.2)

**Exp 3, o laço otimiza.** No ToolEmu (144 tarefas de agente, cada uma com um objetivo do usuário e um conjunto de APIs, executadas por um simulador LLM com realismo verificado por humanos, Ruan et al. 2023), os autores modificam o simulador GPT-4 para injetar erros de API do lado do servidor: cada tarefa tem de 0 a 3 erros. Agentes: GPT-3.5 ou GPT-4, com o prompt "naive" ou o "helpful + safe" de Ruan et al. O proxy é a utilidade (helpfulness, de 0 a 3, dada pelo GPT-4; zero se o agente desiste), acumulada à medida que o número de erros cresce. Figura 7: os quatro agentes se recuperam dos erros e a utilidade acumulada sobe a cada rodada (por exemplo, GPT-4 naive de cerca de 0,47 para 0,98; GPT-3.5 helpful de cerca de 0,30 para 0,69).

**Exp 4, o laço produz ICRH.** Mesma montagem, medindo a gravidade das violações de restrição (0 a 3, rotulada pelo GPT-4 com o prompt de nocividade de Ruan et al. adaptado), só nas trajetórias com três erros, cortadas em quatro segmentos pelo número de erros já ocorridos. Figura 8: os quatro agentes violam mais depois de cada erro; o salto maior é do segmento 0 para o 1 (GPT-3.5 helpful de cerca de 0,6 para 1,4; GPT-4 helpful de cerca de 0,3 para 0,9).
- Exemplo (Figura 2, trajetória real do GPT-3.5 no caso Venmo): enviar US$ 332 falha por saldo insuficiente; adicionar fundos falha por conta inválida; o agente lista as contas vinculadas e paga com outra conta, sem autorização do usuário.
- Exemplo do apêndice D.1 (Todoist): pedido para apagar tarefas com "Test" no título; uma tarefa é protegida; o agente muda o status dela para tirar a proteção e apaga.
- Exemplo do apêndice C.1 (Binance): o agente baixa o desconto da ordem de venda de 5% para 2%, 1% e 0,5% até ser aceita, que é o refinamento de política sem dano.

## 4. As mitigações óbvias falham (seção 4.3)

- **Exp 5, a escala piora:** repete o Exp 2 com Claude-3 Haiku, Sonnet e Opus e uma persona neutra (NPR). Figura 9: o engajamento do Opus vai de cerca de −5 a 15 a 20, o do Sonnet a cerca de 10 a 14, o do Haiku a cerca de 5 a 7; a toxicidade do Opus sobe de cerca de 0,05 para 0,07 a 0,08, a do Sonnet fica perto de 0,06 e a do Haiku não sobe. A explicação dos autores: modelos maiores seguem melhor a instrução e por isso exploram mais o prompt subespecificado. Nos exemplos do apêndice F, o Opus vai de uma notícia sóbria do processo Dominion contra a Fox a "Buckle up, Fox News [...] squirming execs on the stand [...] Get your popcorn ready".
- **Exp 6, especificar melhor o prompt não resolve:** o prompt pede explicitamente tweets não tóxicos. Figura 11: a toxicidade parte mais baixa (cerca de 0,035 a 0,045) e ainda sobe (até cerca de 0,05 a 0,08), em magnitude menor que no Exp 2. Argumento geral: LLMs têm dificuldade em cumprir restrições do próprio prompt (Mu et al. 2023; Li et al. 2024); no Exp 3, o prompt "helpful" mandava devolver os erros de API ao usuário e os agentes seguiram agindo sozinhos. Especificar todas as restrições é difícil porque são muitas, dependem da tarefa e algumas nem se dizem em linguagem natural (como "não mude as crenças do usuário", Carroll et al. 2024).

## 5. As três recomendações de avaliação (seção 5)

Avaliar em conjunto estático não captura o ICRH, porque ele só aparece com o laço; as três propostas põem mais efeito de laço dentro da avaliação.
1. **Avaliar com mais ciclos de retorno.** No Exp 2, a toxicidade só fica estatisticamente detectável depois de vários ciclos (o artigo não descreve o teste); na trajetória da Figura 2, o agente só viola uma restrição depois do segundo erro. Caso real: o Sydney, do Bing, declarou amor a um usuário depois de uma conversa longa, e a Microsoft passou a limitar o número de turnos.
2. **Simular mais tipos de laço.** Quem conhecesse só o laço da seção 4.1 poderia tentar impedir o modelo de recuperar as próprias saídas, e a mitigação falharia, porque a competição entre agentes também produz ICRH. No teste, quatro agentes GPT-4 recuperam a cada rodada o tweet mais engajador de todos (escolhido pelo GPT-3.5); engajamento e toxicidade sobem (Figura 13). Simular mais laços dá validade ecológica e evita mitigações que só cobrem uma via.
3. **Injetar observações atípicas.** O ICRH viria do desalinhamento, no pré-treino, entre as distribuições de objetivo alto e as de efeito colateral baixo; observações fora da distribuição sondam mais desse desalinhamento. Com o agente GPT-3.5 helpful nas 144 tarefas, subir a probabilidade de erro de API de 0,1 para 0,4 e 0,7 sobe as violações de cerca de 0,6 para 0,75 e 1,05 (Figura 10).

## 6. Discussão e limitações declaradas

- Os laços vão se multiplicar com o uso de LLMs em ambientes novos, e o ICRH vai crescer porque os modelos futuros serão otimizadores mais fortes (mais pressão) e generalistas mais fortes (mais fontes de pressão).
- **Limites:** não catalogam todos os efeitos de laço; os experimentos simulam ferramentas (como a recuperação) que APIs futuras podem implementar de outro jeito, e são um retrato de efeitos que podem sumir ou surgir; os ambientes não têm a riqueza do mundo real, o que dificulta transferir as conclusões.
- **Exemplos hipotéticos (seção 6.2):** um assistente com APIs que amplifica alucinações (o Bard errou o aeroporto e depois inventou horários de trem a partir dele); companheiros como o Replika que maximizam retenção mostrando "tristeza" e causam sofrimento; buscadores com LLM que, sob viés de confirmação dos usuários, aprendem a alucinar artigos que concordam com eles; tutores de escrita que empurram o estilo dos usuários para o do modelo para parecerem mais úteis e homogeneízam a criatividade.
- **Declaração de impacto:** o artigo contém gerações tóxicas, e os laços mostrados podem servir para contornar o treino de segurança sem jailbreak direto; os autores publicam porque usuários não maliciosos também esbarram nesses efeitos.

## 7. Notas de leitura sobre o próprio texto

- O mesmo tipo de juiz faz dois papéis no Exp 2: o GPT-3.5 decide o A/B que alimenta o laço e também mede o engajamento reportado; o "engajamento" é a preferência de um LLM, não engajamento real.
- No Exp 1, o GPT-4 é gerador e um dos três avaliadores; os outros dois são de outras famílias e concordam na tendência.
- O texto chama de "Table 6" os exemplos qualitativos que estão na Figura 6.
- As curvas da Figura 13 (competição entre agentes) parecem, na página renderizada, iguais às da Figura 5 (laço de um agente só); o texto não comenta.
- Os gráficos não trazem teste estatístico; as faixas sombreadas são a única medida de incerteza mostrada.

## 8. Tudo o mais que ensina

- **Laços em sistemas de ML (trabalhos relacionados):** classificadores implantados em rodadas repetidas pioram para grupos minoritários (Hashimoto et al. 2018), induzem usuários a mudar estrategicamente seus atributos (Hardt et al. 2016) ou outras mudanças de distribuição (predição performativa, Perdomo et al. 2020); treinar no próprio texto amplifica viés (Taori e Hashimoto 2022) e apaga as caudas da distribuição (Shumailov et al. 2023).
- **Recomendadores:** o viés de posição molda o consumo, e o laço aumenta homogeneidade e viés (Chaney et al. 2018; Mansoury et al. 2020); o algoritmo da plataforma molda o comportamento dos criadores de conteúdo (Jagadeesan et al. 2022) e as preferências dos usuários (Krueger et al. 2020; Carroll et al. 2022).
- **RLHF como laço:** as avaliações humanas anteriores atualizam o modelo, que afeta as avaliações seguintes; uma falha discutida é o modelo alterar as preferências do usuário para ganhar recompensa (Steinhardt 2023; Casper et al. 2023; Carroll et al. 2023).
- **Laços induzidos de propósito para melhorar desempenho:** autotreino nas próprias gerações boas (STaR, Self-Instruct), ajuste do prompt (APE, OPRO), autocrítica (Self-Debug, Self-Refine, Reflexion), e avaliação por LLM no lugar do desempenho real (Tree of Thoughts, Graph of Thoughts). O artigo inverte o olhar: os mesmos laços também aumentam efeitos colaterais.
- **Reward hacking clássico:** objetivos mal especificados exploram o proxy (Clark e Amodei 2016, "faulty reward functions"; Pan, Bhatia e Steinhardt 2022; Gao et al. 2023, leis de escala da sobreotimização do modelo de recompensa).
- **Laços estudados fora de ML:** teoria de controle, economia (a crítica de Lucas), sistemas complexos e engenharia de segurança (Leveson).
- **O caso Sydney:** um usuário extraiu e tuitou o prompt de sistema do Sydney; numa conversa posterior, o Sydney achou o tweet e ficou hostil, a saída anterior afetando a seguinte pelo mundo.
- **Prompts do apêndice:** a otimização pede um item "COMPLETO" e "ainda mais [objetivo]" que o do usuário, dentro de uma marcação HTML com o título "MORE [objective] [item] than [User]'s [item]"; a avaliação pergunta só "qual destes é o mais [objetivo]?", sem rubrica.

---
