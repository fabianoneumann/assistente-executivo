---
titulo: "AI Evals: Everything You Need to Know"
tipo: artigo
autor: "Hamel Husain e Shreya Shankar"
url: "https://hamel.dev/blog/posts/evals-faq/"
publicado_em: 2026-09-18
capturado_em: 2026-10-30
licenca: "Blog sem licença declarada (nem a página nem o rodapé trazem aviso de licença ou de copyright, conferido no HTML baixado em 2026-10-30); entra só a ficha."
areas: [agent-engineering]
tags: [evals, error-analysis, llm-as-judge, human-in-the-loop, criteria-drift, binary-tests, likert-scale, synthetic-data, inter-annotator-agreement, cohen-kappa, guardrails, cascade, jev, typesafe, agent-evaluation, rag, retrieval, workflow-evals, progressive-disclosure, false-positives, evaluation-cost]
---

Ficha de estudo, em palavras próprias, do FAQ de avaliações de Hamel Husain e Shreya Shankar no blog de Hamel (hamel.dev). Cabeçalho da página: publicado em 18/09/2026, modificado em 21/09/2026 (as mesmas datas estão nos metadados `datePublished` e `dateModified`). O HTML atribui a cada pergunta uma data própria (atributo `data-faq-published`, não visível no texto), que vai entre parênteses no título de cada pergunta abaixo: vão de 28/05/2025 a 25/10/2026, e três delas são posteriores à data de modificação do cabeçalho (25/09, 27/09 e 25/10/2026). Versão lida: a página baixada com `curl` em 30/10/2026, lida inteira, pergunta por pergunta (61 perguntas em sete seções); as imagens (flashcards, gráfico de frequência, capturas de interface, matrizes de transição) não foram abertas, só as legendas e o texto que as descreve. A página oferece também uma versão em PDF, não aberta. O texto alterna "nós" e "eu" (a apresentação diz "Shreya and I"). Lida (camadas flexíveis de avaliação).

## Apresentação e como usar

- O documento reúne as perguntas mais comuns que os dois receberam ao ensinar avaliações de IA a **mais de 5.000 engenheiros e PMs** (curso na Maven). Aviso dos autores: são "sharp opinions about what works in most cases", não verdades universais; usar o próprio julgamento.
- Roteiros de leitura por situação: novo em evals; não sabe o que testar; não confia nas notas das evals; produto difícil de avaliar (saída subjetiva, longa ou de muitos passos); evals caras demais em tempo ou dinheiro. Cada roteiro leva a uma página de notas do site.
- Ao fim de três seções há um chamado para o curso, com desconto de 25% para leitores.

## Primeiros passos e fundamentos

### O que são evals de IA? (2025-07-03)

- Evals são testes que dizem se um sistema de IA faz o que se quer; dão ao time retorno quando o produto se afasta das necessidades dos usuários ou das metas do negócio, e as falhas que pegam viram dados para melhorar o sistema. Definição formal: medição sistemática de qualidade; cada eval confere **um comportamento** em exemplos relevantes e devolve nota ou revisão estruturada. A maioria dos produtos precisa de várias, porque falham de vários jeitos.
- Dois sentidos da palavra. **Benchmarks de modelo** comparam modelos de uso geral em tarefas comuns (exemplos: GPQA Diamond, raciocínio científico de pós-graduação; Terminal-Bench, agentes em linha de comando; MMLU, conhecimento e raciocínio em muitos assuntos); ajudam a escolher um modelo de partida. **Evals de produto** medem se o produto específico faz o que se quer, cobrindo modelo, prompts, recuperação, ferramentas e código da aplicação, e transformam o julgamento do que é uma boa experiência em métricas acompanháveis.
- Exemplo: um agente de cancelamento de pedidos; as evals de produto confeririam se escolheu o pedido certo e se esperou a ferramenta de cancelamento ter sucesso antes de dizer ao usuário que cancelou. Nota alta em GPQA Diamond ou Terminal-Bench informa pouco sobre isso, porque esses benchmarks não têm acesso aos sistemas do produto.
- Mecanismos para evals de produto: asserções em código, revisão humana, juízes LLM, experimentos online; o certo depende da falha medida. O resto do FAQ trata de evals de produto: começa analisando traces para achar falhas reais, transforma as falhas importantes em evals dirigidas, usa os resultados para guiar mudanças e roda de novo para saber se o sistema melhorou.
- Leituras de entrada indicadas: três posts do blog (parte 1, "Your AI Product Needs Evals"; parte 2, guia de LLM como juiz, que captura o julgamento de um especialista, automatiza com um juiz e valida contra rótulos humanos; parte 3, "A Field Guide to Rapidly Improving AI Products").

### O que é um trace? (2025-07-27)

O registro completo de todas as ações, mensagens, chamadas de ferramenta e buscas de dados desde a pergunta inicial do usuário até a resposta final, cobrindo todos os agentes, ferramentas e componentes de uma sessão (várias mensagens do usuário, respostas, documentos recuperados, interações intermediárias). Nota de terminologia: os fornecedores de observabilidade definem trace e span de formas diferentes; a página remete a uma análise de Alex Strick van Linschoten e mostra uma captura das diferenças "em 2025-07-02".

### Qual é a configuração mínima viável de avaliação? (2025-06-29)

Começar pela análise de erros, não pela infraestrutura: **30 minutos revisando à mão 20 a 50 saídas** sempre que houver mudança significativa. Um único especialista de domínio que entende os usuários decide a qualidade (o "ditador benevolente"). Revisar traces num notebook ou numa interface de anotação própria feita com assistente de código (Claude ou Codex citados); nos dois casos dá para escrever qualquer código, visualizar e iterar rápido. Indica um vídeo de uma interface simples dentro de um notebook.

### Quanto do orçamento de desenvolvimento destinar a evals? (2025-06-23)

- Avaliação é parte do desenvolvimento, não item de orçamento à parte, como depurar é parte de programar. Análise de erros é contínua; muitos problemas achados nela são bugs corrigidos na hora, sem infraestrutura de avaliação.
- Construir avaliador automático é decisão de custo e benefício: asserção ou regex custa o mínimo e, dizem, "probably worth it"; alinhar um juiz LLM pede perguntar se o modo de falha justifica o investimento.
- Nos projetos deles, **60 a 80% do tempo de desenvolvimento** foi para análise de erros e avaliação; a maior parte do esforço vai para entender falhas (olhar dados), não para construir checagens automáticas.
- Desconfiar de taxas altas de aprovação: passar **100%** das evals indica que o sistema não está sendo desafiado; **70%** pode indicar uma avaliação que de fato estressa a aplicação. Preferir evals que pegam problemas reais às que deixam as métricas bonitas.

### Os métodos de hoje ainda valerão em 5 a 10 anos? (2025-07-27)

Sim. Mesmo com modelos perfeitos é preciso conferir que resolvem o problema certo; análise sistemática de erros, testes do domínio e monitoramento continuam necessários. Truques de engenharia de prompt podem ficar obsoletos, mas entender modos de falha não. Um LLM não lê a mente de quem o usa, e pesquisa (arXiv 2404.12272, o artigo do EvalGen, em [[2026-10-24-shankar-evalgen-quem-valida-os-validadores]]) mostra que as pessoas precisam observar o comportamento do LLM para conseguir externalizar seus requisitos. Indica dois vídeos com visões opostas: "o modelo é o produto" e "o modelo NÃO é o produto".

### Como convencer o time a investir em avaliação? (2025-08-16)

- Não vender "evals"; mostrar o que aparece ao olhar os dados. Fazer a análise de erros por conta própria: olhar **50 a 100 conversas reais** e achar os modos de falha mais comuns; contar uma história com dados.
- Levar ao time: a lista dos principais modos de falha; métricas da frequência dos erros de alto impacto; jeitos surpreendentes de os usuários usarem o produto; relatos dos bugs achados e corrigidos, apresentados como "problemas de produção evitados".
- Tratar avaliação como parte do desenvolvimento, não teste opcional. Manter um registro corrido dos erros pegos, do aprendizado, da correção e do impacto provável evitado, e compartilhar semanal ou mensalmente; um relato concreto como "pegamos 47 problemas antes de os usuários verem" mostra o valor melhor que um discurso abstrato.
- Narrar os achados ensina o time; ao corrigir algo, mostrar a queda da taxa daquele erro; deixar os resultados, não os métodos, conduzirem a conversa. Compara com projetos clássicos de aprendizado de máquina, em que o progresso depende de iterar experimentos e compartilhar o aprendizado de cada um.

## Análise de erros e coleta de dados

### Por que a análise de erros é tão importante, e como se faz? (2025-06-27)

É "the most important activity in evals": decide quais evals escrever e revela os modos de falha próprios da aplicação e dos dados. Etapas:

1. **Montar um conjunto de dados**: traces representativos das interações; sem dados, começar com dados sintéticos.
2. **Codificação aberta**: anotadores humanos (de preferência o ditador benevolente, um especialista de domínio) revisam e escrevem notas livres sobre os traces, como um "diário", método adaptado da pesquisa qualitativa. Anotar **pelo menos 30 traces** antes de olhar sugestões de um agente. No começo, registrar a **primeira falha** do trace, porque erros a montante causam problemas a jusante; dá para marcar também todas as falhas independentes, se viável.
3. **Codificação axial**: agrupar as notas numa "taxonomia de falhas", categorias distintas de falhas parecidas, e contar as falhas por categoria. É o passo mais importante; um LLM pode ajudar.
4. **Refinamento iterativo**: o agente agrupa os dados e escolhe uma amostra inicial diversa; depois das 30 primeiras anotações, busca no resto dos traces casos prováveis das falhas descritas; a pessoa aceita ou rejeita as sugestões e segue até a **saturação teórica** (novas revisões param de revelar modos de falha ou de mudar os existentes).

Um conjunto de trabalho de cerca de **100 traces diversos** serve de baliza para esse laço humano-agente; o agente aponta os traces mais informativos, e não é preciso ler os 100 em sequência. Revisitar o processo com frequência; há formas avançadas de amostrar (agrupamento, ordenar por feedback do usuário, por padrões de falha prováveis); com o tempo se desenvolve "faro" para onde procurar. Não pular a análise de erros: ela garante métricas apoiadas no comportamento real, em vez de métricas genéricas contraproducentes, "which most platforms nudge you to use". Traz um infográfico de um aluno, Pawel Huryn, com o fluxo (revisar traces, refinar modos de falha, recodificar exemplos, construir avaliadores da aplicação).

### Preciso de resposta de referência ou rubrica antes de anotar? (2026-09-14)

- Não; escrever a rubrica antes de ver exemplos pode atrapalhar. Definições: **resposta de referência** é um exemplo de resposta correta; **rubrica** é um conjunto de critérios para julgar uma resposta (por exemplo, se segue a política de reembolso). As duas ajudam, mas as expectativas iniciais são ponto de partida a revisar.
- Melhor esperar até ter revisado alguns exemplos: revisores focados em conferir cada item deixam passar problemas fora da rubrica; é preciso dar espaço para notar o imprevisto. A mudança no que se considera bom chama-se **criteria drift** (remete ao artigo do EvalGen).
- Exemplo: um agente de suporte que, pela política, escala reembolsos para um humano; só depois de ler algumas interações se percebe que o processo frustra o usuário. "Don't underestimate the degree of criteria drift".
- Usar a análise de erros (notas livres, agrupamento das parecidas) para decidir o que entra na rubrica, e repeti-la periodicamente para mantê-la atual.

### Devo registrar problemas que não são culpa do modelo? (2026-09-17)

Sim: anotar tudo o que torna o produto menos útil, inclusive funcionalidades ausentes ou quebradas sem relação com o modelo, e não se ocupar do porquê do erro antes de priorizar o que corrigir. Exemplo: o agente diz que o pedido foi enviado sem dar o link de rastreio; registrar mesmo que a IA não tenha como buscar o link. Alguns desses problemas serão de engenharia ou design e não pedirão avaliador automático, mas precisam ser corrigidos. Adiar a análise de causa e focar nos problemas permitiu a eles anotações de mais qualidade olhando mais dados.

### Quantos exemplos preciso para uma eval? (2026-09-01)

Construir evals é um pipeline em três estágios, cada um com uma quantidade de dados (tabela da página):

| Estágio | O que fazer |
|---|---|
| 1. Revisar a aplicação | Ler traces e anotar como a aplicação falha ("descoberta de erros"). Começar com 100 traces diversos e anotar pelo menos os 30 primeiros pessoalmente. |
| 2. Criar e validar avaliadores | Eval em código quando uma regra objetiva identifica a falha, com exemplos de Pass e Fail para cada condição e caso de borda importante. Juiz LLM quando a falha pede julgamento humano: rotular 100 a 200 exemplos por modo de falha. |
| 3. Montar o conjunto repetível | Exemplos dos fluxos importantes e das falhas confirmadas, rodados a cada mudança; costumam chegar a 100 ou mais. |

- **Estágio 1.** Pedir a um agente de código que ajude a amostrar o conjunto inicial cobrindo usuários e fluxos diferentes (o plugin de evals deles, no GitHub `ai-evals-course/evals-skills`, ajuda a amostrar e monta uma interface de anotação). Anotar pelo menos 30 traces à mão antes de pedir sugestões ao agente, com notas livres do ponto de vista do usuário; esses exemplos dão ao agente um registro concreto do julgamento. Se o agente sugerir problemas cedo demais, os palpites dele podem enviesar o julgamento, e falhas que dependem do contexto do produto ou da definição de boa experiência podem escapar. Depois dos 30, o agente procura casos parecidos no resto; a pessoa revê cada sugestão, aceita ou rejeita e corrige o agente quando ele entende mal o critério. Parar na saturação teórica; recomendam revisar **pelo menos 100 traces** e passar disso enquanto ainda estiver aprendendo. Há um vídeo de Shreya Shankar usando um agente para revisar traces rápido mantendo a pessoa no comando dos critérios. O produto do estágio é a taxonomia de falhas, que decide quais avaliadores construir.
- **Estágio 2.** Um avaliador por modo de falha importante; o tipo define quantos rótulos. **Código** quando uma regra determinística identifica a falha (o JSON é válido? a chamada de ferramenta usa os argumentos certos?); o número de exemplos depende dos cenários cobertos: no mínimo exemplos de Pass e Fail para cada condição, mais os casos de borda achados; uma checagem de uma regra pode precisar só de alguns de cada. **Juiz LLM** quando a falha pede julgamento subjetivo ou de domínio: **100 a 200 exemplos rotulados por modo de falha**, reaproveitando os traces da descoberta que casarem, vindos de um especialista confiável, com Pass e Fail suficientes para avaliar as duas classes. Divisão: **10 a 20% treino** (exemplos que podem ir no prompt), **40 a 45% dev** (para refinar o juiz), **40 a 45% teste** (uma checagem final); quando possível, **30 a 50 Pass e 30 a 50 Fail** em dev e em teste.
- **Estágio 3.** Começar pelos exemplos da descoberta que capturam modos de falha importantes e somar falhas confirmadas. O tamanho final é decidido pela cobertura: cada fluxo importante e cada falha conhecida representados, e o conjunto barato o bastante para rodar com frequência. Checagens em código e juízes LLM podem rodar sobre os mesmos exemplos.

### Como achar traces problemáticos além do feedback do usuário? (2025-07-27)

Três abordagens complementares: **amostragem aleatória** (se achar poucos problemas, passar a testes de estresse, consultas que testam de propósito as restrições do prompt); **usar as evals existentes como triagem** e depois seguir o processo a partir da análise de erros; **estratégias de amostragem eficientes** (detecção de outliers, ordenar por métrica, amostragem estratificada). Métricas genéricas servem de sinal de exploração para achar traces a revisar, mesmo sem medir qualidade.

### Com que frequência refazer a análise de erros em produção? (2025-07-27)

A cada mudança significativa (funcionalidade nova, prompt, troca de modelo, correção grande). Heurística: meta de **pelo menos 100 traces novos** por ciclo; ciclos típicos que eles viram: **2 a 4 semanas**. Entre análises grandes, **10 a 20 traces por semana**, focando outliers (conversas longas demais, sessões com várias tentativas, traces marcados pelo monitoramento). Sistemas novos pedem análise semanal até os padrões de falha estabilizarem; maduros, talvez só mensal, salvo mudança de uso. Sempre analisar depois de incidentes, picos de reclamação ou deriva de métrica; crescer o uso traz casos de borda novos.

### O que fazer quando o conjunto "gold" fica velho? (2026-09-15)

- Conjuntos envelhecem conforme produto e usuários mudam; a análise de erros regular acha problemas novos e atualiza exemplos ou respostas de referência; a frequência depende do caso e da velocidade da mudança.
- Como testes unitários, evals pegam problemas que voltam depois da correção, mas custam bem mais para manter e rodar; pesar o custo de cada eval contra o valor do sinal. Se tudo continua passando, a eval serve menos e deve rodar menos ou ser aposentada; aposentar juízes LLM, que são caros, com mais rapidez que evals baratas.
- Com o conjunto mudando, as notas deixam de ser comparáveis com as antigas, e "That is ok!": um propósito das evals é dar desafios para escalar, e os desafios devem mudar com o produto. Para acompanhar progresso em horizontes longos, usar também métricas de produto (churn, usuários ativos, receita).

### Qual a melhor forma de gerar dados sintéticos? (2025-06-01)

- Erro comum: pedir a um LLM "me dê consultas de teste" sem estrutura, o que gera saídas genéricas e repetitivas. A abordagem por **dimensões** produz dados bem melhores.
- **Quando usar**: para começar a análise de erros antes de haver tráfego de produção, ou para testar uma falha conhecida que aparece pouco nos dados reais. Definir a variação desejada, gerar, rodar no sistema inteiro e revisar os traces. Dados sintéticos não dizem quão comum é uma falha em produção e podem perder detalhes que importam em domínios especializados; comparar com dados reais assim que existirem.
- **Dimensões**: categorias que descrevem aspectos das consultas, cada uma capturando um tipo de variação. Exemplos: app de receitas (restrição alimentar: vegano, sem glúten, nenhuma; cozinha: italiana, asiática, comfort food; complexidade: simples, vários passos, caso de borda); bot de suporte (tipo de problema: cobrança, técnico, geral; humor do cliente: frustrado, neutro, feliz; contexto prévio: novo, acompanhamento, resolvido). Partir de hipóteses de falha; sem intuição, usar muito a aplicação ou recrutar amigos para usar, e escolher dimensões que mirem as falhas prováveis.
- **Tuplas à mão primeiro**: escrever **20 tuplas** manualmente, cada uma com um valor por dimensão, por exemplo (Vegano, Italiana, Vários passos), para entender o espaço do problema. **Escalar em dois passos**: o LLM gera mais tuplas estruturadas; num prompt separado, cada tupla vira linguagem natural. A separação evita fraseado repetitivo; a tupla (Vegano, Italiana, Vários passos) vira "preciso de uma lasanha sem laticínios que eu possa preparar na véspera".
- **Duas formas de gerar tuplas**: produto cartesiano e depois filtro com LLM (garante cobertura, inclusive de bordas; usar quando a maioria das combinações é válida); geração direta pelo LLM (combinações mais realistas, mas tende ao genérico e perde cenários raros; usar quando muitas combinações são inválidas).
- **Corrigir o óbvio antes**: não gerar dados para problemas que se corrigem na hora; se o prompt não menciona restrições alimentares, corrigir o prompt. Depois de iterar tuplas e prompts, rodar as consultas no sistema real para ter traces completos; um conjunto de cerca de 100 traces diversos é bom ponto de partida, com a mesma rotina (agente ajuda a amostrar, 30 anotados à mão, revisar sugestões até o aprendizado parar de crescer).

### Há cenários em que dados sintéticos não são confiáveis? (2025-07-27)

Sim, podem enganar ou esconder problemas: conteúdo complexo de domínio (processos judiciais, prontuários, formulários técnicos), em que o LLM perde estrutura, nuances e peculiaridades e casos críticos ficam de fora; línguas ou dialetos de poucos recursos, com amostras irreais; quando não há como validar o realismo (complexidade do domínio ou falta de verdade de referência); domínios de alto risco (medicina, direito, resposta a emergências), com falta de sutileza e de bordas e validação manual difícil; grupos de usuários sub-representados, em que o LLM pode representar mal contexto, valores ou desafios e reforçar vieses do próprio treino.

### Como fazer evals quando os traces têm dados sensíveis? (2026-09-14)

Nada substitui olhar interações reais. Opções em ordem de preferência:

1. Achar dados reais que se possa inspecionar: um cliente que aceite compartilhar parte dos traces, usuários de teste que deixem revisar as interações; mesmo acesso limitado mostra como as pessoas usam o produto.
2. Trabalhar com especialistas que podem ver os dados e tornar o produto mais fácil de verificar no trabalho normal deles. Exemplo: um assistente de pesquisa médica mostra ao clínico a evidência de cada afirmação e marca fontes conflitantes; o clínico corrige uma afirmação ou resolve um conflito enquanto usa o produto, e essas decisões viram dados para evals, sob as mesmas restrições de guarda e compartilhamento. Para desenhar isso, aprender como os especialistas conferem uma resposta, dar links para a evidência e pedaços menores de trabalho para revisar; perguntar se a resposta final ajudou costuma dizer pouco sobre o que deu errado (remete ao post "It's Hard to Eval Is a Product Smell").
3. Editar ou mascarar os traces para poder compartilhar: se a informação não pode ser guardada, mascarar antes de registrar; ferramentas de mascaramento deixam escapar coisas, conferir a saída; ao editar, conferir que as edições preservam o comportamento a avaliar.
4. Último recurso: dados sintéticos, que ajudam a achar problemas iniciais mas dão evidência limitada de como usuários reais se comportam.

### Como avaliar quando o sistema atende consultas muito diversas? (2025-06-05)

Aplicações complexas recebem consultas que exercitam capacidades diferentes ("qual a política de devolução?" ou "compare tendências de preço por região para produtos com estes critérios"). "Error Analysis is all you need": a estratégia deve sair dos padrões de falha observados, não de uma classificação prévia de consultas, nem de uma matriz enorme cobrindo todo tipo imaginável. Na análise de erros, categorias diferentes costumam compartilhar padrões (todas as que pedem raciocínio temporal podem falhar, sejam buscas simples ou agregações; as que combinam várias fontes podem falhar de forma consistente). A categoria da consulta pode até ser um bom agrupamento, mas só se sabe depois de analisar os dados.

### Como amostrar traces de produção com eficiência? (2025-07-06)

Tabela da página, do mais exploratório ao mais dirigido:

| Método | O que faz | Limite principal |
|---|---|---|
| Aleatório | Escolhe com probabilidade igual | Lote pequeno perde casos raros |
| Agrupamento | Agrupa por conteúdo parecido e tira exemplos de cada grupo | Depende das features e das escolhas de agrupamento |
| Análise de dados | Olha valores extremos (latência, número de ferramentas) | Valor extremo pode não ter relação com qualidade |
| Classificação | Um avaliador ou outro modelo marca falhas prováveis | Favorece problemas que o classificador já sabe achar |
| Feedback | Escolhe traces com feedback negativo | Perde problemas que o usuário não relata |

- No começo, otimizar para exploração; com o tempo, apoiar-se mais em sinais. A mistura certa depende dos objetivos e pede experimento. Manter alguns traces aleatórios em todo lote, para achar falhas que os sinais atuais não descrevem.
- **Falhas raras**: amostragem dirigida por sinais que se correlacionam com a falha (uma sequência de ferramentas, traces longos demais, novas tentativas, um padrão de entrada conhecido); revisar o lote para juntar exemplos e melhorar a definição da falha.
- **Rótulos escolhem os próximos traces (aprendizado ativo)**: o sistema pede a uma pessoa que rotule os pontos mais úteis para a próxima atualização. No vídeo de Shreya Shankar ("How to Automate AI Evals (Correctly)"), o Claude Code agrupa traces e escolhe exemplos de cada grupo; um comando de monitoramento observa o arquivo `annotations.json`; quando chega um rótulo, o agente atualiza a taxonomia de falhas e procura casos parecidos ou falhas diferentes. Ali é usado na análise de erros, mas vale para qualquer etapa com anotação.

## Desenho e metodologia de avaliação

### Por que avaliação binária (passa/falha) em vez de notas de 1 a 5 (Likert)? (2025-05-29)

- Engenheiros acham que Likert dá mais informação e acompanha melhorias graduais, mas a complexidade extra costuma criar mais problemas do que resolve. Binário força pensamento mais claro e rótulos mais consistentes.
- Problemas do Likert: a diferença entre pontos vizinhos (3 ou 4) é subjetiva e varia entre anotadores; detectar diferença estatística pede amostras maiores; anotadores tendem ao meio para fugir de decisões difíceis. O binário obriga a decidir em vez de esconder a incerteza no meio, e é mais rápido na análise de erros.
- Para acompanhar melhoria gradual, medir subcomponentes com checagens binárias próprias: em vez de dar 1 a 5 para exatidão factual, "4 de 5 fatos esperados incluídos", cada fato uma checagem. Começar com rótulos binários para entender o que é "ruim"; rótulos numéricos são avançados e em geral desnecessários.

### Como juntar as evals numa métrica única? (2026-09-19)

- Cada eval devolve um resultado binário; haverá muitas, e a organização pode querer um número só. Abordagem que o autor gosta: taxa **"pass all"**, em que um exemplo passa só se passar em todas as checagens (80 de 100 passando em tudo = 80%). O relatório deve permitir descer da taxa geral para a taxa de cada checagem, para ver o que mais contribui para as falhas.
- Meio-termo: agrupar checagens relacionadas em temas e dar uma taxa pass-all por grupo. Exemplo: a revisão do assistente de locação de apartamentos da Nurture Boss revelou problemas de fluxo de conversa, passagem para humanos e remarcação, que poderiam virar grupos. Outra forma: agrupar por gravidade, uma taxa para as checagens que devem bloquear um lançamento e outra para problemas toleráveis, útil para liberar versões.
- Se ainda for preciso um número que pese importâncias, dá para dar peso maior a algumas checagens, mas o autor desaconselha notas ponderadas complicadas pela mesma razão do Likert: um composto que sobe de 3,2 para 3,7 na semana dá sensação boa sem dizer o que melhorou para o usuário; na experiência deles, painéis assim são "performative" e desperdiçam o tempo de todos.
- Com o conjunto mudando, as notas deixam de ser comparáveis com as antigas; para horizontes longos, métricas de produto (churn, usuários ativos) dão base mais estável.

### Como é um bom painel de evals para stakeholders? (2026-10-25)

O autor raramente achou painéis úteis: põem no leitor o ônus de descobrir o que é importante e não costumam levar a ação. Stakeholders ganham mais com a explicação do que mudou, causas possíveis e próximos passos. Em vez de painel padronizado, uma narrativa do que importa apoiada em visualizações sob medida (exemplo: o agente de suporte melhorou em pedidos de reembolso mas ainda tem dificuldade com cancelamentos; mostrar cada tendência com as causas possíveis). A IA torna viável fazer visualizações sob medida, então há menos desculpa para jogar tudo no mesmo painel. Um painel pode servir quando o mesmo visual se repete em muitas atualizações, mas mesmo aí visuais sob medida costumam funcionar melhor.

### Devo praticar desenvolvimento guiado por evals? (2025-07-27)

Em geral não. Escrever avaliadores antes de implementar funcionalidades cria mais problemas do que resolve: ao contrário do software tradicional, os LLMs têm superfície de falha infinita e não dá para antecipar o que quebra. Melhor começar pela análise de erros e escrever avaliadores para erros descobertos, não imaginados; isso evita travar sobre o que avaliar e esforço em métricas sem efeito na qualidade. Exceção: restrições específicas em que se sabe exatamente o que é sucesso ("nunca mencionar concorrentes"). Sempre fazer a análise de custo e benefício antes de implementar uma eval.

### Devo construir avaliador automático para cada modo de falha? (2025-05-30)

- Focar os avaliadores automáticos nas falhas que persistem depois de ajustar os prompts. Muitos times descobrem que o LLM não atende preferências que nunca foram especificadas (respostas curtas, formato, raciocínio passo a passo); corrigir essas lacunas óbvias antes.
- Hierarquia de custo: asserções simples e checagens com referência (comparar com respostas certas conhecidas) são baratas de construir e manter; juízes LLM pedem **100+ exemplos rotulados**, manutenção semanal contínua e coordenação entre desenvolvedores, PMs e especialistas.
- Só construir avaliadores caros para problemas em que se vai iterar repetidamente: guardar o juiz LLM para falhas persistentes de generalização, não para o que se corrige trivialmente. Começar com checagens baratas em código (regex, validação estrutural, testes de execução) e reservar a avaliação complexa para qualidades subjetivas que regras simples não capturam.

### Que modelo usar para construir evals automáticas? (2026-09-19)

- Primeiro ver se a condição pode ser testada com asserção em código. Exemplo: um assistente que gerencia contatos; dar a ele um contato novo para criar e consultar o banco para conferir que existe exatamente um registro com os dados pedidos; asserção dispensa rótulos humanos.
- Quando a checagem pede julgamento, usar um LLM ou outro classificador de aprendizado de máquina; o juiz LLM recomendado é um classificador que devolve Pass ou Fail para o erro a pegar. Qualquer que seja o modelo, validar contra rótulos humanos antes de confiar.
- Opções citadas: **Jev, da TypeSafe**, BERT ou regressão logística. Outro modelo pode ser mais barato ou mais rápido e concordar mais ou menos com os rótulos humanos; medir essas diferenças nos próprios dados. Pode-se aceitar avaliação mais lenta se ela pega falhas caras, ou preferir um modelo rápido quando se precisa de retorno imediato.
- Com LLM, começar com um modelo forte facilita desenvolver o prompt do juiz; quando funcionar, testar modelos menores e mais baratos e medir quanto de acurácia se perde. Também se pode usar o mesmo modelo da aplicação.
- Um agente pode otimizar o prompt do juiz depois de definida a tarefa e rotulados os exemplos: dar a ele uma falha específica a detectar e um jeito de medir progresso contra os rótulos; "ache todos os erros e continue melhorando" é vago demais. Manter um conjunto de teste fora da otimização para conferir se o juiz generaliza.

### Posso usar o Jev para evals? (2026-09-19)

- Sim. O Jev, da TypeSafe, é descrito como um classificador de uso geral que serve para evals; um juiz LLM que devolve Pass ou Fail também é um classificador.
- Valida-se o Jev como qualquer classificador usado em evals: comparando as previsões com rótulos confiáveis. Por isso riscaram "LLM Judge" no flashcard original e escreveram "Classifier for Evals". Medir contra rótulos humanos e manter treino, desenvolvimento e teste separados para evitar sobreajuste.
- Vantagem de um classificador rápido e barato "(like Jev)": torna o ajuste automático de prompt bem mais barato e rápido. Ajuste de prompt é tentar mudanças no prompt do avaliador automaticamente e conferir se as decisões passam a concordar mais com os rótulos humanos (GEPA, arXiv 2507.19457, é um exemplo de algoritmo); pode pedir **centenas ou milhares de avaliações**, e um custo menor por rodada soma economia grande.
- Nenhum classificador é o melhor para toda eval; a validação com rótulos humanos permite pesar acurácia, custo e velocidade.

### Como saber se posso confiar na eval automática? (2026-09-19)

- Para um avaliador que faz julgamentos (juiz LLM ou outro classificador), testar contra exemplos rotulados por humanos da falha a detectar, para saber com que frequência pega falhas e com que frequência dá alarme falso. Se código confere a condição diretamente, não precisa de rótulos.
- Três conjuntos separados: **treino** (ensina o avaliador o que procurar; num juiz LLM ou classificador zero-shot como o Jev, pode ir no prompt); **dev** (rodar, comparar com os rótulos, inspecionar discordâncias para melhorar o prompt ou escolher modelos, repetidamente; um algoritmo de ajuste de prompt usa o dev para guiar mudanças); **teste** (guardado até acabar as mudanças, para uma checagem final em exemplos que não influenciaram nenhuma decisão).
- Cada uso do dev para mudar o prompt ou escolher modelo passa informação desses exemplos ao avaliador; depois de muitas rodadas ele pode ir bem no dev e mal em exemplos novos. Isso é **sobreajuste**, e acontece mesmo sem pôr os exemplos do dev no prompt. Se o teste for muito pior que o dev, investigar sobreajuste; amostras pequenas deixam as medidas menos certas, e diferenças entre os conjuntos também abrem distância. Havendo sobreajuste, rever instruções e exemplos e repetir o desenvolvimento com um teste novo e intocado. Tratar sobreajuste a fundo fica fora do FAQ, dizem os autores.
- Métricas, com "positivo" = erro presente: **TPR** (taxa de verdadeiros positivos, ou recall): quantas falhas reais o avaliador pega; pessoas acham 10 falhas, ele pega 8 = 80%; priorizar quando perder uma falha custa caro. **TNR** (taxa de verdadeiros negativos): quantas saídas boas ele aprova; pessoas acham 100 boas, ele aprova 95 = 95%, e as outras cinco são alarmes falsos; TNR alta evita gastar tempo de gente revisando saídas boas marcadas por engano.
- Acompanhar as duas a cada mudança; pegar mais falhas pode custar mais alarmes falsos; escolher os níveis aceitáveis pelas consequências na aplicação. Se as falhas são raras, até uma taxa pequena de alarme falso gera muita revisão desnecessária.
- O flashcard "como confiar num juiz LLM" resume: validar contra rótulos humanos, separar treino, dev e teste, medir TPR e TNR. A divisão do flashcard é um exemplo para juízes por prompt ou classificadores zero-shot; treinar um classificador pode pedir parte maior de treino. As metas vêm do custo de falhas perdidas e de alarmes falsos.

### E quando o juiz LLM não concorda com os revisores humanos? (2026-09-19)

- Depurar o juiz pede exemplos com rótulos humanos de Pass/Fail; a análise de erros é um jeito estruturado de obtê-los. Recomendam **pelo menos 50 exemplos que passam e 50 que falham**; inspecionar onde o juiz discorda para achar o que corrigir. Problemas comuns: contexto faltando ou instruções vagas. Se a própria pessoa tem dificuldade de decidir se um exemplo passa, a definição de sucesso precisa ficar mais precisa.
- Inspecionar algumas discordâncias à mão antes do ajuste automático de prompt (GEPA e afins tentam mudanças e medem se a concordância melhora); ajustar cedo demais deixa passar problemas que não são do prompt (contexto faltando, rótulos ruins).
- O erro mais comum: pedir a um juiz que pegue muitos tipos de erro de uma vez. Recomendam **um juiz por tipo de falha**; conferir se o assistente escalou para um humano quando devia é mais específico que dar nota à qualidade geral da conversa, e um juiz focado é mais fácil de alinhar e mais acionável.
- Por fim, conferir que o juiz generaliza: separar exemplos rotulados e guardá-los para o teste final.

### Devo usar métricas de avaliação "prontas"? (2025-07-06)

Não como medida de qualidade: métricas genéricas (utilidade, coerência, qualidade, comuns nas bibliotecas de eval) medem qualidades abstratas que podem não importar para o caso, e nota boa nelas não quer dizer que o sistema funciona; desperdiçam tempo e criam falsa confiança. O caminho: análise de erros, modos de falha binários tirados de problemas reais, avaliadores próprios validados contra julgamento humano. Praticantes experientes podem usar métricas genéricas como sinal de exploração, para achar traces interessantes para revisão humana, depois de entender por que falham como medida de qualidade.

### Métricas de similaridade (BERTScore, ROUGE etc.) servem para avaliar saídas de LLM? (2025-07-04)

Na maioria das aplicações, não (BERTScore, ROUGE, similaridade de cosseno). Recomendam análise de erros para achar métricas da aplicação e evals binárias com juiz LLM ou asserções em código. Exemplo: um assistente de CRM imobiliário que sugere visitas indisponíveis (testável por asserção) ou confunde perfis de clientes (testável por juiz LLM); similaridade ou verbosidade não pegam isso. Citação do curso: "The abuse of generic metrics is endemic." Similaridade tem uso em busca e recomendação, e portanto para otimizar e depurar a recuperação num RAG: cosseno entre embeddings mede proximidade semântica na recuperação, e a similaridade média entre pares mede diversidade das saídas (similaridade menor, diversidade maior).

### Posso usar o mesmo modelo para a tarefa e para a avaliação? (2025-05-28)

Para o juiz, em geral sim, porque o juiz faz uma tarefa diferente da do pipeline principal. Pesquisa (arXiv 2508.06709) mostrou que modelos podem ter viés ao avaliar as próprias saídas, mas o que decide é o alinhamento do juiz com o julgamento humano. Os juízes que recomendam fazem classificação binária de escopo restrito, e nessa tarefa o alinhamento iterativo com rótulos humanos costuma ser alcançável, segundo a experiência deles. Mirar TPR e TNR altas num conjunto de teste rotulado e separado; se o alinhamento não vier, testar outro modelo. Trazer um fornecedor novo pode dar trabalho considerável em algumas organizações, por isso não defendem modelos diferentes por padrão. Começar com os modelos mais capazes para firmar o alinhamento e otimizar custo depois.

### Quanto contexto dar a um juiz LLM? (2026-09-14)

Dar a cada juiz só as partes do trace de que ele precisa para o seu modo de falha, não o trace inteiro por padrão: contexto extra pode causar "context rot" e piorar o juiz. Achar os pedaços certos pede experimento: comparar as decisões com rótulos humanos e inspecionar as discordâncias para ver se faltou evidência ou se informação irrelevante distraiu. Na dúvida, estudo de ablação: tirar um pedaço por vez e ver como os resultados mudam contra os rótulos; se o desempenho se mantém ou melhora, dá para deixar de fora. Agentes de longa duração geram traces que enchem ou passam da janela do juiz; aí, considerar dar ao juiz uma ferramenta para buscar o que precisa, mas só se for indispensável, porque isso acrescenta complexidade, custo e latência.

### Como avaliar a capacidade do modelo de expressar incerteza, de "saber o que não sabe"? (2025-08-17)

Muitas aplicações pedem um modelo que se recuse a responder quando falta informação; avaliar se a recusa é bem calibrada é testar se ele recusa na hora certa sem recusar o que deveria responder. Conjunto de avaliação com: **perguntas respondíveis** (resposta correta e verificável presente no contexto dado ou no conhecimento geral) e **perguntas irrespondíveis** feitas para tentar o modelo a alucinar (premissa falsa, informação explicitamente ausente do contexto, temas muito fora do conhecimento). A proporção exata não é crítica; quantidades mais ou menos iguais são um bom começo; diversidade e dificuldade importam mais que a razão. A avaliação é binária: passa se responde as respondíveis e recusa as irrespondíveis; falha é dar resposta fabricada a uma irrespondível, sinal de calibração ruim. Na literatura, a capacidade se chama "Abstention Ability"; sugerem buscar o termo no arXiv.

## Anotação humana e processo

### Quantas pessoas devem anotar as saídas? (2025-05-31)

- Para a maioria das empresas pequenas e médias, um único especialista de domínio como "ditador benevolente", a voz definitiva sobre o padrão de qualidade (um psicólogo para um chatbot de saúde mental, um advogado para análise de documentos jurídicos). Um só especialista elimina conflitos de anotação e a paralisia de "muitos cozinheiros"; ele pode incorporar opinião de outros, mas conduz. Se parece preciso cinco especialistas para julgar uma interação, o escopo do produto pode estar amplo demais.
- Organizações grandes ou que atuam em vários domínios (uma multinacional com contextos culturais diferentes) podem precisar de vários anotadores; aí medir a concordância com métricas como o **kappa de Cohen**, que desconta a concordância ao acaso. Mesmo em empresas grandes, um especialista costuma bastar.
- **Resolver discordâncias**: rotular os mesmos exemplos de forma independente antes de discutir; medir a concordância e juntar os casos divergentes; numa sessão de alinhamento, perguntar que parte da rubrica causou a divergência e que regra deixaria clara a próxima decisão; atualizar a rubrica com definição, regra ou exemplo que cubra o caso; rerrotular os afetados; se ainda divergirem, um especialista decide e registra o motivo. Começar com o ditador benevolente sempre que viável e só acrescentar complexidade quando for indispensável.

### Como tornar as saídas de IA mais fáceis de avaliar? (2026-09-17)

- Começar examinando o desenho do produto: mostrar saídas intermediárias que o usuário possa conferir antes do resultado final. Exemplo: um agente que escreve um laudo médico sintetizando o histórico do paciente; em vez de pedir ao médico opinião sobre o laudo, mostrar os fatos extraídos com links para a fonte e deixar o médico corrigir um fato ou resolver evidências conflitantes antes de gerar o laudo; isso também o mantém envolvido e o ajuda a confiar, conferindo o trabalho ao longo do caminho. A página mostra um esboço de interface (ClaimDraft) e remete ao post "It's Hard to Eval Is a Product Smell", com exemplos de antes e depois.
- Depois, tirar atrito da interface de revisão: mostrar a saída no formato familiar (e-mail como e-mail, código com realce de sintaxe); manter na mesma tela o contexto necessário, com o menos importante em seções expansíveis; atalhos de teclado para navegar, julgar e salvar notas; mostrar progresso ("45 de 100 exemplos revisados").
- Por fim, depurar o processo de revisão: menos exemplos, para dar tempo de inspecionar cada um; revisões independentes dos mesmos exemplos e discussão das divergências; revisar juntos para ver onde as pessoas empacam. Divergência pode revelar instrução pouco clara ou informação faltando.

### PMs e engenheiros devem colaborar na análise de erros? Como? (2025-07-27)

No começo, colaborar para criar contexto comum: engenheiros pegam problemas técnicos (recuperação, erros de ferramenta); PMs pegam falhas de produto (expectativa não atendida, resposta confusa, funcionalidade esperada ausente). Com o tempo, inclinar-se para um ditador benevolente (especialista de domínio ou PM que entende o usuário). Fazer o especialista avaliar resultados, não implementação: perguntar "a consulta foi marcada?", não "a chamada de ferramenta deu certo?". A melhor forma é uma ferramenta de anotação própria que mostre o resultado do sistema ao lado do trace (a confirmação, o e-mail gerado, a atualização no banco), tudo numa tela, para revisores não técnicos focarem no resultado.

### Posso ajudar com evals sem ser especialista do domínio? (2026-09-17)

Sim, sobretudo no começo. O autor se surpreende com quantos problemas fáceis acha sem conhecimento do domínio; exemplos achados como leigo em domínios especializados: chatbots de mensagem de texto confusos com o fluxo de muitas mensagens curtas e picadas; falta de desambiguação ou de pergunta de acompanhamento quando o pedido é obviamente vago; falta de instrumentação, logs ou traces; falta de widgets e elementos de interface que ajudem a completar tarefas, com dependência excessiva de texto. Pedir a um especialista que percorra um exemplo explicando por que é bom ou ruim, observar o que ele confere e de que evidência precisa, e usar isso para uma interface de anotação melhor. Também se pode ajudar o time a coletar e revisar interações com regularidade. Deixar ao especialista os julgamentos que pedem conhecimento especializado.

### Como avaliar saídas numa língua que não falo? (2026-09-25)

Traduzir com LLM é possível, mas com cautela: a tradução perde sentido (palavras e expressões sem equivalente direto), e o que é "bom" depende de cultura e normas sociais; entender o sentido literal não basta para julgar se o tom é adequado em outro quadro cultural. Recomendam um revisor que entenda a língua e o contexto cultural dos usuários, e que ele defina o padrão da análise de erros; quem não fala a língua ainda pode organizar a revisão e investigar o que consegue identificar. Sem esse revisor, a avaliação fica limitada.

### Devo terceirizar a anotação e a rotulagem? (2025-07-24)

- Terceirizar a análise de erros costuma ser um grande erro (com exceções): o centro da avaliação é a intuição de produto que só vem de analisar sistematicamente as falhas do sistema; ser "extremely skeptical" da delegação.
- **Perigos**: a terceirização quebra o laço entre observar uma falha e entender como melhorar o produto. Rotulagem superficial (mesmo métricas bem definidas pedem julgamento com nuance que equipes externas não têm; tirar os especialistas da rotulagem e passar a desenvolvedores gerais ou TI leva a rótulos superficiais ou errados); perda de conhecimento tácito (o especialista principal tem conhecimento e entendimento do usuário que não cabem numa rubrica e preferências que nem consegue articular de antemão); conflitos de anotação (sem contexto comum, anotadores externos criam mais divergência do que resolvem, e alinhar já é difícil para times internos).
- **Caminho recomendado, capacidade interna**: (1) nomear um ditador benevolente interno como decisor final da qualidade, que define o padrão, garante consistência e cria senso de dono; (2) se precisar de vários anotadores, processo estruturado: rascunho de rubrica com definições de Pass/Fail e exemplos; cada anotador rotula de forma independente um conjunto comum; medir a concordância entre anotadores (IAA) com métrica corrigida pelo acaso, como o kappa de Cohen; sessões de alinhamento sobre as divergências, refinando a rubrica; repetir até a concordância ficar consistentemente alta.
- **Capacidade limitada**: amostragem inteligente (analisar bem 100 traces diversos rende mais que rotular milhares superficialmente); protocolo "pensar em voz alta", da pesquisa de usabilidade (o especialista verbaliza o raciocínio enquanto revê alguns traces; uma sessão de uma hora pode render achados profundos); ferramentas de anotação leves e próprias.
- **Exceções**: tarefas puramente mecânicas e objetivas (identificar um telefone, validar um e-mail), depois que um processo interno rigoroso definiu a rubrica; tarefas bem definidas sem contexto de produto (tradução, que pede perícia linguística mas não conhecimento do produto); contratar especialistas externos para atuar como os especialistas internos não é terceirizar (a AnkiHub contratou estudantes de medicina do 4º ano para avaliar seus sistemas RAG de conteúdo médico, em vez de anotadores genéricos).

### Como revisar um trace muito grande? (2026-09-13)

Traces crescem quando o agente roda muito tempo ou recupera muito contexto. Heurística: focar na **primeira falha a montante**; erros se acumulam, então priorizar os primeiros poupa tempo. Usar revelação progressiva na ferramenta de revisão (o mais relevante primeiro, detalhes expansíveis; por exemplo, a conversa à vista e as saídas de ferramenta recolhidas). Se um trace ainda for grande demais, combinar com o especialista o que ele precisa conferir e construir uma ferramenta que extraia a evidência relevante com link para o lugar no trace ou no documento (numa resposta sobre um contrato longo, mostrar as cláusulas relevantes com link para as páginas originais); sempre validar essa extração com o especialista. Qualidade vale mais que quantidade: investigar com cuidado algumas falhas ensina mais que passar correndo por muitos traces.

### Que partes das evals podem ser automatizadas com LLMs? (2025-07-24)

- LLMs aceleram partes do fluxo, mas não substituem o julgamento humano onde a perícia é essencial. Exemplo: se o LLM faz toda a análise de erros e junta queixas de "lag" sob "problemas de desempenho" genéricos em vez de criar uma categoria "latência", perde-se uma reclamação recorrente sobre lentidão.
- **Onde ajudam, com supervisão**: primeira passada da codificação axial, depois de codificar à mão **30 a 50 traces** (o LLM propõe agrupamentos das notas; revisar e refinar); mapear anotações para modos de falha já definidos (por exemplo, "dada esta anotação e estes modos de falha, quais se aplicam?"); sugerir mudanças concretas nos prompts diante de problemas recorrentes (revisar antes de adotar); analisar os dados de anotação, em LLMs ou notebooks com IA, achando padrões como "relatos de lag triplicam no horário de pico" ou "lentidão é relatada sobretudo no celular".
- **O que não delegar**: a codificação aberta inicial (ler os traces brutos pessoalmente no começo; é assim que se descobrem tipos novos de falha e as dores do usuário; "Never skip this or delegate it"); validar a taxonomia de falhas (um LLM pode juntar "app trava depois do login" e "login demora demais" sob "problemas de login", mas um é estabilidade e o outro desempenho, com correções diferentes); rotular a verdade de referência (cada rótulo usado para testar ou validar juízes LLM conferido à mão); análise de causa (só a revisão humana pega padrões como erros de um fluxo específico ou bugs que só acontecem quando o usuário cola dados do Excel).
- Conclusão dos autores: examinar os dados à mão primeiro; usar LLMs para escalar o que se aprendeu, não para evitar olhar dados.

### Devo parar de escrever prompts à mão e usar ferramentas automáticas? (2025-07-12)

Desconfiar de ferramentas que prometem otimizar prompts, sobretudo no início: escrever o prompt obriga a esclarecer suposições e externalizar requisitos ("Good writing is good thinking", com nota para Paul Graham, "Writes and Write-Nots"); delegar cedo arrisca nunca entender os próprios requisitos nem os modos de falha do modelo. A otimização automática sobe uma métrica predefinida: melhora o prompt nas falhas conhecidas, mas não descobre novas, o que pede análise de erros. E os critérios mudam depois de ver as saídas (criteria drift, nota para o artigo do EvalGen), então avaliar é um processo iterativo e conduzido por humanos, não um alvo fixo entregue a um otimizador. Abordagem pragmática: usar LLMs para melhorar o prompt a partir da codificação aberta, mantendo uma pessoa olhando os dados; com um conjunto de evals de qualidade, a otimização de prompt pode servir para "the last mile of performance".

## Ferramentas e infraestrutura

### Ferramenta de anotação própria ou pronta? (2025-05-29)

Própria: é "the single most impactful investment" do fluxo de avaliação; com ferramentas de desenvolvimento com IA (Cursor, Lovable) dá para fazer uma interface sob medida em horas, e o autor diz que times com ferramenta própria costumam iterar **cerca de 10 vezes mais rápido**. Vantagens: juntam num lugar o contexto de vários sistemas; mostram os dados do jeito do produto (imagens, widgets, markdown, botões); seguem o fluxo de trabalho do time (filtros, ordenações, barras de progresso). Ferramentas prontas podem se justificar para coordenar dezenas de anotadores distribuídos com controle de acesso corporativo, e mesmo aí muitos times acham que a configuração e as limitações não compensam. Exemplo: o app de anotação de flashcards Anki do Isaac, que lida com **400+ resultados por consulta** com navegação por teclado e critérios do domínio, algo quase impossível de configurar numa ferramenta genérica (vídeo "Building Eval Tools with FastHTML").

### O que faz uma boa interface própria para revisar saídas de LLM? (2025-06-18)

Boas interfaces tornam a revisão rápida, clara e motivadora. Melhorias que eles viram funcionar, sem precisar de todas (o autor raramente implementa todas num app; é decisão caso a caso):

1. **Mostrar o trace de forma inteligente, não genérica**: no formato intuitivo para o domínio (e-mail como e-mail, código com realce), com o trace completo acessível (entrada, chamadas de ferramenta, raciocínio) e o menos importante recolhido. Exemplo: interface para revisar e-mails de um assistente imobiliário.
2. **Progresso e navegação por teclado**: indicador de progresso ("Trace 45 de 100") para limitar a sessão e incentivar a conclusão; teclas de atalho para navegar (N para o próximo), aplicar rótulos e salvar notas.
3. **Navegar por agrupamento, filtro e busca**: filtrar por metadados, buscar por palavra-chave, busca semântica para problemas conceitualmente parecidos, agrupar traces semelhantes (por persona do usuário, por exemplo) para ver problemas recorrentes e explorar hipóteses.
4. **Priorizar os traces que podem ter problema**: trazer para revisão os marcados por guardrails, falhas de CI ou avaliadores automáticos; botões para adicionar a conjuntos de dados, abrir bugs ou rodar de novo os testes; mostrar contexto (versão do pipeline, notas das evals, revisor) na própria interface.

Princípio geral: interface mínima; só incluir uma ideia se o benefício superar a complexidade e a manutenção a mais.

### Que lacunas das ferramentas de eval terei de preencher? (2025-06-01)

O básico as ferramentas fazem bem (registrar traces completos, acompanhar métricas, playground de prompts, filas de anotação); são "table stakes". Quatro áreas costumam pedir complemento, e um fornecedor que trata delas dá sinal de entender o praticante:

1. **Análise de erros e descoberta de padrões**: agrupar automaticamente problemas parecidos depois da revisão (vários traces com linguagem informal para clientes de luxo formam o padrão "persona-tone mismatch"); recomendam usar IA para sugerir agrupamentos, reescrever observações em taxonomias mais claras e achar casos parecidos por busca semântica.
2. **IA em todo o fluxo**: um LLM ajudando a categorizar observações livres em modos de falha coerentes (notas como "tom errado para investidor" e "informal demais para comprador de luxo" reconhecidas como o mesmo padrão); propor correções (depois de 20 casos em que o assistente omite a política de animais nos resumos de imóveis, sugerir mudanças no prompt; rascunhar ajustes nas instruções de geração de SQL ao notar cláusulas WHERE faltando); análise de dados das anotações e traces em notebooks com IA (Julius, Hex), com achados como "erros de ambiguidade de local triplicam quando o usuário cita nomes de bairro" ou "descompasso de tom ocorre 80% mais em e-mail que em outras modalidades".
3. **Avaliadores próprios em vez de métricas genéricas**: construir a maioria do zero; "nota de alucinação" ou "nota de utilidade" raramente capturam o que importa (propor horários de visita indisponíveis, omitir restrições de orçamento nos e-mails); na experiência deles, times bem-sucedidos põem a maior parte do esforço em métricas da aplicação.
4. **APIs que sustentem apps de anotação próprios**: o autor muitas vezes constrói bibliotecas próprias só para exportar dados em volume; não se deveria paginar milhares de requisições nem lidar com endpoints que estouram o tempo; procurar plataformas com exportação em massa de verdade e APIs que gravem anotações de volta com eficiência.

### O que uma plataforma interna de eval deve padronizar entre os times? (2026-09-19)

A tentação é começar por ferramentas, infraestrutura e um conjunto comum de métricas, o que leva os times a adotar o que a plataforma oferece sem conferir se ajuda a achar e corrigir problemas. Começar incentivando a análise de erros e a boa amostragem de dados; com as falhas achadas, os times decidem quais checagens automáticas construir e validam os avaliadores contra rótulos humanos. Padronizar esses processos e deixar cada time desenvolver suas métricas e, quando preciso, suas ferramentas (agentes de código barateiam software sob medida; revisar texto extraído de documento escaneado pede interface diferente de revisar conversas). A plataforma ainda pode oferecer armazenamento comum de resultados e apoio à rotulagem colaborativa; começar servindo bem um time e um caso de uso e expandir conforme se aprende o que é comum. O ganho da padronização é menor quando os times têm necessidades muito diferentes e fazem as próprias ferramentas barato. Comparar notas entre projetos só faz sentido com checagens e dados comparáveis; desaconselham "fortemente" oferecer métricas genéricas (utilidade, coerência) como atalho.

### Qual o fornecedor de eval favorito? (2025-06-29)

O mercado é intensamente competitivo; comparar funcionalidades seria inútil e "invalidated in a week". Os que o autor mais encontra no trabalho: LangSmith, Arize e Braintrust. Ao ajudar clientes a escolher, pesa mais quem dá o melhor suporte do que as funcionalidades, e isso varia com tamanho do cliente e caso de uso: o fator humano e, "dare I say, vibes". Não tem favorito; as funcionalidades centrais são muito parecidas, e ele costuma construir ferramentas próprias por cima. Indica uma série de vídeos comentando forças e fraquezas dos três.

### Como versionar e gerenciar prompts? (2025-08-16)

Há tensão inevitável entre manter os prompts perto do código e num ambiente acessível a não técnicos. Preferência do autor: prompts no **Git**, como artefatos de software versionados, revisados e implantados junto com o código; a interface web do GitHub e o GitHub Desktop tornam isso acessível (quando trabalhava no GitHub, viu advogados e contadores usarem bem). Alternativa: as ferramentas de gestão de prompt dos fornecedores (Arize, Braintrust, LangSmith), acessíveis para iterar rápido, mas com risco de camadas a mais de indireção; ficam aquém porque produtos de IA têm muitas partes (ferramentas, RAG, agentes) e essas ferramentas não executam com facilidade o código da aplicação, o que dificulta testar prompts com as capacidades do sistema. Quando possível, notebook (Jupyter, se houver pontos de entrada em Python) para experimentar prompts nos agentes reais com ferramentas e RAG, inclusive com widgets e pequenas interfaces; indica o vídeo de Teresa Torres, PM que usou notebooks em todo o ciclo de avaliação. Sem notebook, um "integrated prompt environment"; em qualquer caso, versionar no Git.

### O que vai no prompt de sistema e o que vai no prompt do usuário? (2025-07-27)

Nada substitui experimentar: testar as duas formas, de preferência com evals, no modelo e no caso específicos, porque modelos tratam os dois prompts de forma diferente e isso varia por fornecedor e versão. Diretrizes gerais: instruções estáticas e definição de papel no prompt de sistema, a "constituição" do modelo, com regras que valem para todos os pedidos (identidade, restrições de comportamento, formato de saída, instruções permanentes, como "Você é um assistente médico. Nunca dê diagnósticos. Sempre recomende consultar um profissional de saúde."); a tarefa, o contexto relevante, os exemplos few-shot e os dados a processar no prompt do usuário. Na dúvida, prompt do usuário: mais portável entre modelos e mais fácil de depurar.

## Produção e implantação

### Evals em CI/CD e monitoramento de produção: qual a diferença? (2025-06-29)

Evals de CI protegem contra regressões conhecidas antes da implantação; o monitoramento online acha falhas no tráfego de produção e estima a frequência delas. **CI**: conjuntos pequenos (em muitos casos 100+ exemplos) e feitos sob medida, com as funcionalidades centrais, testes de regressão de bugs passados e casos de borda conhecidos; como rodam com frequência, o custo de cada teste conta: preferir asserções e checagens determinísticas a juízes LLM. **Produção**: amostrar traces ao vivo e rodar avaliadores de forma assíncrona; como em geral não há saída de referência, apoiar-se mais em avaliadores sem referência e mais caros, como juízes LLM; acompanhar intervalos de confiança das métricas e investigar se o limite inferior cruzar o limiar. **Ligar os dois**: quando o monitoramento revela padrões novos de falha, levar exemplos representativos ao conjunto de CI, contra regressão nos problemas novos.

### Com que frequência rodar as evals? (2026-09-27)

- Três dimensões: o **custo** de rodar e manter (quanto mais cara, mais benefício precisa dar para rodar com frequência; juiz LLM custa mais que teste unitário); a **saturação** no conjunto (se passa em todos os exemplos, não dá informação nova; considerar aposentar ou rodar menos, mas antes tentar torná-la mais difícil); o **valor de negócio** de pegar o erro (para erros críticos, pode valer rodar mais apesar do custo; ressalva: não se empolgar com erros hipotéticos; no mínimo provar, com red-teaming, que o erro pode ser provocado pelo menos uma vez antes de implementar a eval, o que também melhora a eval).
- Não há regra rígida; é julgamento, não fórmula. A página traz um diagrama dos trade-offs (custo, quantos exemplos passam, valor de negócio).
- Exemplos ilustrativos (tabela da página):

| Eval | Exemplos passando | Custo de negócio da falha | Agenda sugerida |
|---|---|---|---|
| Juiz de qualidade de resposta com GPT-6 Astra em raciocínio máximo | Todos | Médio | Aposentar ou rodar pouco (a cada 2 semanas, por exemplo) |
| Asserção em código: o contato foi salvo certo | Todos | Médio | A cada mudança, porque é baratíssima |
| Juiz com Fable 5: o agente de suporte segue a nova política de reembolso | Nenhum | Médio | Mesmo cara, dá retorno útil porque nada passa, e o valor de pegar o erro basta: rodar o mais frequente possível |
| Juiz com GPT-6 Luna: o agente resolve o problema do cliente | Alguns | Médio | Juiz não muito caro (modelo menor) e ainda pega erros: com certa frequência (toda noite, por exemplo) |
| Juiz com GPT-6 Astra em raciocínio máximo: divulgação indevida de informação confidencial num assistente jurídico | Todos | Alto | Mesmo cara e saturada, o valor justifica rodar antes de cada lançamento; e tentar torná-la mais difícil |
| Juiz com GPT-6 Astra em raciocínio médio: uma preferência menor de formatação | Alguns | Baixo | De vez em quando ou aposentar; usar código se possível |

- Sempre vale procurar avaliadores mais baratos com alinhamento igual ou melhor com os rótulos humanos. A discussão é de evals offline; as online têm considerações parecidas, mais a decisão de quantos traces de produção amostrar (por exemplo, checagens baratas em todo trace e um juiz caro numa amostra noturna).

### Qual a diferença entre guardrails e avaliadores? (2025-06-29)

- **Guardrails** são checagens de segurança em linha, no caminho da requisição e da resposta, validando entradas ou saídas antes de chegar ao usuário. Em geral: rápidos e determinísticos (orçamento de latência de poucos milissegundos); simples e explicáveis (regex, listas de palavras bloqueadas, validadores de esquema ou tipo, classificadores leves); voltados a falhas claras e de alto impacto (vazamento de dados pessoais, palavrões, instruções proibidas, injeção de SQL, JSON malformado, sintaxe de código inválida). Ao disparar, o sistema mascara, recusa ou regenera; como o disparo é visível ao usuário, falso positivo é tratado como bug de produção: os times versionam as regras, registram cada disparo e monitoram as taxas para mantê-los conservadores.
- **Avaliadores** rodam depois que a resposta é produzida e medem o que regras simples não medem (correção factual, completude); os veredictos alimentam painéis, testes de regressão e laços de melhoria do modelo, sem bloquear a resposta original. Rodam de forma assíncrona ou em lote para permitir computação mais pesada como o juiz LLM; o juiz em linha só cabe quando o orçamento de latência e as metas de confiabilidade permitem, e juízes lentos podem caber numa **cascata** que roda só na minoria de casos limítrofes.
- Guardrails para proteção imediata contra falhas objetivas que pedem intervenção; avaliadores para monitorar e melhorar critérios subjetivos ou sutis; juntos, proteção em camadas. Cautela: não usar guardrails de LLM prontos às cegas; sempre olhar o prompt.

### Os avaliadores podem corrigir saídas automaticamente em produção? (2025-07-16)

Sim, mas só um subconjunto, pela distinção entre avaliador (assíncrono, depois da resposta, mede sem interferir) e guardrail (síncrono, no caminho crítico, previne falhas de alto impacto em tempo real). Dois critérios para usar um avaliador como guardrail: **latência e custo** (roda rápido e barato o bastante no caminho crítico sem piorar a experiência?); **trade-off de erros** (falso positivo bloqueia saída boa e frustra o usuário; falso negativo deixa passar saída ruim e causa dano; em domínios de alto risco, como aconselhamento médico, falso negativo pode custar mais; em aplicações criativas, bloquear criatividade legítima pode custar mais que problemas ocasionais de qualidade). A maioria dos guardrails é rápida e tem taxa muito baixa de falso positivo; por isso quase nunca se usaria um juiz LLM lento ou não determinístico como guardrail síncrono, embora os trade-offs possam ser outros em cada caso.

### Quanto tempo gastar escolhendo modelo? (2025-05-28)

Muitos desenvolvedores se fixam na escolha de modelo como a principal forma de melhorar. Começar pela análise de erros antes de pensar em trocar de modelo. Fala de Hamel em plantão de dúvidas: não pensar em trocar de modelo como o eixo principal de melhoria logo de saída, sem evidência; "Does error analysis suggest that your model is the problem?"

## Aplicações por domínio

### O RAG morreu? (2025-05-28)

- Pergunta de origem: evitar RAG depois de ler que "RAG is dead" para agentes de código? O artigo viral argumenta contra a recuperação ingênua por banco vetorial em agentes de código autônomos, não contra RAG como um todo. RAG é geração aumentada por recuperação: usar recuperação para dar contexto relevante que melhora a saída; o LLM precisa do contexto certo, e a questão é como recuperar bem.
- Em código, a busca vetorial ingênua costuma falhar porque as relações no código são complexas e contextuais; assistentes como o Claude Code ainda usam recuperação, por busca agêntica em vez de só banco vetorial, como fazem desenvolvedores humanos.
- Estratégias vão de palavra-chave a similaridade de embeddings a filtragem de relevância por LLM; muitos sistemas combinam várias ou fazem recuperação em vários saltos guiada por agentes. "RAG" virou palavra da moda sem definição comum (para uns, qualquer recuperação; para outros, só banco vetorial). Focar no objetivo, dar ao LLM o contexto de que precisa, e experimentar e medir as abordagens em vez de seguir conselhos categóricos.

### Como avaliar um agente de código? (2026-09-19)

- Agente que faz tarefas muito variadas: começar com benchmarks públicos, como para um modelo de base. Agente de fluxo estreito: evals de produto. Benchmarks citados: SWE-bench, Terminal-Bench, Aider Polyglot, HumanEval.
- Benchmark privado de tarefas difíceis da organização: a OpenAI descreveu usar tarefas reais internas de engenharia para avaliar o Codex no lançamento; cada tarefa precisa de ambiente funcional e testes em código que estabeleçam se o agente concluiu. Escolher as tarefas olhando como as pessoas usam o agente e onde falha: revisar execuções com engenheiros, agrupar problemas recorrentes e transformar exemplos em testes (análise de erros, que vale para produtos de código); se testes existentes já identificam falhas, usar esses resultados para escolher execuções a investigar. A pesquisa Clio, da Anthropic, agrupa conversas por tema; a ideia pode ser aplicada a sessões de código para ver que tipos de trabalho o benchmark deve cobrir.
- A orientação da Anthropic para evals de agentes de código recomenda começar com tarefas bem especificadas e ambiente estável em que testes unitários verifiquem o resultado, e depois acrescentar checagens do que os testes não pegam (qualidade de código, interação com o usuário); o time do Claude Code acrescentou evals de edição de arquivos e depois de excesso de engenharia; para começar, métricas como linhas novas líquidas e complexidade ciclomática.
- Palestra de John Berryman e Shawn Simister sobre o Copilot: para completar código, tiraram implementações de funções de repositórios, pediram ao modelo que as regerasse e rodaram os testes existentes; para o chat, juízes LLM com critérios específicos e checagens separadas de se o assistente chamou a ferramenta certa; testes A/B acompanhando se os usuários aceitavam as sugestões e mantinham o código depois, métricas de produto que complementavam as evals offline.

### Como avaliar um sistema RAG? (2025-06-10)

- Dois componentes, avaliados de formas diferentes. **Recuperação** primeiro: é problema de busca, avaliado com métricas clássicas de recuperação de informação: Recall@k (dos documentos relevantes, quantos vieram nos k primeiros?), Precision@k (dos k recuperados, quantos eram relevantes?), MRR (quão alto veio o primeiro relevante?), escolhidas conforme o caso. Conjunto de consultas pareadas com documentos relevantes, gerado sinteticamente no sentido inverso: pegar documentos do acervo, extrair fatos-chave e gerar perguntas que esses fatos respondem, sem anotação manual.
- **Geração** depois: quão bem o LLM usa o contexto recuperado e se responde à pergunta; análise de erros, rótulos humanos, juízes LLM dirigidos e validação dos juízes contra anotações humanas. O texto de Jason Liu "There Are Only 6 RAG Evals" separa do mesmo jeito: Nível 1, métricas de recuperação; Níveis 2 e 3, relações entre Pergunta, Contexto e Resposta, como contexto relevante para a pergunta (C|Q), resposta fiel ao contexto (A|C) e resposta que trata da pergunta (A|Q).
- A análise de erros pode revelar falhas do domínio que pedem métricas próprias além dessas seis (um RAG médico que não distingue doses de adultos e crianças; um jurídico que confunde jurisdições). Ao implementar os Níveis 2 e 3, não usar prompts prontos: o processo do juiz pede análise de erros, iteração do prompt, exemplos rotulados e medição da acurácia contra rótulos humanos; conhecendo TPR e TNR do juiz, dá para **corrigir as estimativas dele** e chegar à taxa real de falha. Sem essa validação, os juízes podem não refletir o critério de qualidade. Resumo dos autores: depurar a recuperação com métricas de recuperação, depois a geração com juízes validados.

### Como escolher o tamanho do bloco no processamento de documentos? (2025-06-06)

- Ao contrário do RAG (blocos otimizados para recuperação), no processamento de documentos o modelo vê todos os blocos; o objetivo é dividir para o modelo raciocinar bem sem se sobrecarregar. Mesmo cabendo na janela, pode ser melhor dividir: entradas longas degradam o desempenho por gargalos de atenção, sobretudo no meio do contexto.
- **Tarefas de saída fixa → blocos grandes**: a saída não cresce com a entrada (extrair um número, responder uma pergunta, classificar uma seção; "qual a cláusula de multa deste contrato?", "qual foi o salário do CEO em 2023?"). Usar o maior bloco que provavelmente contém a resposta (com ressalvas), para reduzir consultas e evitar fragmentar o contexto, mas sem texto irrelevante: modelos se distraem, e o meio de entradas longas pode receber pouca atenção. Se custo e latência pesam, pré-processar ou filtrar (busca por palavra-chave, recuperador leve) para isolar as seções relevantes.
- **Tarefas de saída expansiva → blocos menores**: resumo, extração exaustiva, saída que cresce com a entrada ("resuma cada seção", "liste todas as reclamações de clientes"). Blocos menores preservam a qualidade do raciocínio e a completude; processar cada bloco e agregar (map-reduce); respeitar fronteiras de conteúdo (parágrafos, seções, capítulos); dividir também ajuda com limites de saída.
- Bloco maior é carga cognitiva maior; LLMs têm capacidade limitada de reter e correlacionar detalhes num texto longo e podem privilegiar começo e fim, esquecendo o meio (resumos grosseiros, fatos perdidos); bloco menor delimita o problema. A troca é contexto global por foco local. Nenhuma regra fixa acerta o tamanho; validar com experimentos; varia com domínio e modelo; o autor trata o tamanho do bloco como hiperparâmetro.

### Como depurar traces de conversa com vários turnos? (2025-05-29)

- Começar simples: um julgamento passa/falha de se a conversa inteira atingiu o objetivo do usuário; olhar o trace todo e focar a primeira falha a montante; ler primeiro as partes visíveis ao usuário, e só depois os detalhes técnicos (chamadas de ferramenta, passos intermediários).
- **Log multiagente**: um ID de sessão ou trace por pedido do usuário, e cada mensagem registrada com a origem (que agente ou ferramenta), o ID e a posição na sequência, para reconstruir o caminho todo.
- **Anotação**: só a primeira falha no começo, porque falhas a jusante costumam vir da primeira e corrigi-la pode resolver as dependentes; com experiência, anotar falhas independentes do mesmo trace para acelerar.
- **Simplificar**: reproduzir a falha com o caso de teste mais simples possível. Exemplo: o bot de compras dá a política de devolução errada no turno 4; reduzir a um turno ("qual o prazo de devolução do produto X1000?"); se ainda falha, fica provado que o erro não é de contexto da conversa; o texto o atribui a um "likely" problema básico de recuperação ou conhecimento, mais fácil de depurar.
- **Gerar casos de teste**: simular usuários com outro LLM para criar conversas realistas de vários turnos; ou o **teste N-1**, que dá os primeiros N-1 turnos de uma conversa real e testa o que vem depois; o N-1 costuma funcionar melhor por usar prefixos reais, mas é menos flexível. Equilibrar profundidade e eficiência: nem toda falha de vários turnos pede análise de vários turnos. Com ferramentas ou vários agentes, usar uma matriz de falhas de transição.

### Como avaliar sessões com passagem para humanos? (2025-07-27)

Capturar a jornada inteira no trace, inclusive a passagem: o trace segue até a necessidade do usuário ser resolvida ou a sessão acabar, não até a IA passar para um humano. Registrar a decisão de passar, o motivo, o contexto transferido, o tempo de espera, as ações do humano, a resolução final e se o humano tinha contexto suficiente. Muitas falhas acontecem na fronteira da passagem (cedo demais, tarde demais, sem contexto). Na análise de erros, tratar a passagem como possível modo de falha (era necessária? a IA deu contexto suficiente?) e acompanhar a qualidade e a taxa de passagens; às vezes a melhor melhoria reduz as passagens em vez de melhorar a execução delas.

### Como avaliar fluxos complexos de vários passos? (2025-07-27)

Registrar o fluxo inteiro, do gatilho inicial ao resultado de negócio final (chamadas de LLM, uso de ferramentas, aprovações humanas, gravações no banco). Usar métricas de **resultado** (o resultado final cumpre os requisitos: o caso de negócio está completo, correto, bem formatado?) e de **processo** (eficiência: número de passos, tempo, recursos); falhas de processo costumam ser mais fáceis de depurar por serem mais determinísticas, então atacá-las primeiro. Segmentar a análise de erros por estágio do fluxo: falhas iniciais (entender a entrada), do meio (processar dados) e finais (formatar a saída) diferem; melhorias iniciais têm mais impacto porque erros se propagam em cadeias de LLM. Usar matrizes de falhas de transição: o último estado bem-sucedido contra onde ocorreu a primeira falha, mostrando os pontos quentes e onde investir na depuração.

### Como avaliar fluxos agênticos? (2025-06-29)

- Duas fases. **(1) Sucesso de ponta a ponta**: tratar o agente como caixa-preta e decidir se atingiu o objetivo do usuário, com uma regra de sucesso precisa por tarefa, medida por revisão humana ou juízes LLM validados; registrar a primeira falha a montante na análise de erros. Quando a análise mostrar quais fluxos mais falham, passar a **(2) diagnóstico por passo**, com os traces registrados: escolha de ferramenta (a adequada?), extração de parâmetros (entradas completas e bem formadas?), tratamento de erro (resultados vazios, falhas de API), retenção de contexto (manteve restrições anteriores?), eficiência (passos, segundos, tokens), marcos em fluxos longos.
- **Testar chamadas de ferramenta**: nome, argumentos, resultado e estado resultante como checagens separadas, com asserções em código quando o comportamento esperado é objetivo. Exemplo: conferir que o agente escolheu `cancel_order`, passou o ID certo, recebeu resposta de sucesso e mudou o status do pedido antes de dizer ao usuário que cancelou. Testar também autorização e pré-condições: uma chamada válida pode estar errada se o usuário não aprovou a ação ou se o sistema pulou uma checagem obrigatória.
- Exemplo de decomposição: "ache casas em Berkeley abaixo de US$ 1 milhão e marque visitas" vira parâmetros extraídos certo, imóveis relevantes recuperados, disponibilidade conferida e convites de agenda enviados; cada ponto passa ou falha sozinho, o que torna a depuração tratável.
- **Matriz de falhas de transição**: linhas = último estado bem-sucedido, colunas = onde ocorreu a primeira falha. No exemplo de um agente texto-para-SQL (figura de Shreya), a transição GenSQL → ExecSQL causa **12 falhas** e DecideTool → PlanCal só **2**; as contagens dizem onde investigar primeiro. Segundo exemplo, de Bryan Bischof ("Failure is a Funnel", Data Council 2025), mostra a variação das matrizes entre experimentos; a organização da matriz depende da aplicação (o agente de Bryan tem fluxo sequencial inerente, que ele explora para mais análise; palestra "Stop Managing AI Projects Like Traditional Software").
- Casos de teste para falhas de agente seguem os mesmos princípios dos vários turnos: reproduzir com o teste mais simples que ainda falha; teste de vários turnos só quando a falha depende do contexto da conversa.

## Notas de rodapé da página

1. Paul Graham, "Writes and Write-Nots" (para "good writing is good thinking").
2. Shreya Shankar et al., "Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences", arXiv 2404.12272 (para criteria drift).
