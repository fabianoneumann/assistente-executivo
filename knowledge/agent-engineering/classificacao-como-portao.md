# Classificação como portão de conclusão

Quando uma nota ou uma classe dada por modelo pode decidir que um trabalho está pronto, que um conteúdo sobe no ranking ou em que estágio do funil uma pessoa está. Fontes: *LLM-as-a-Judge: can a model grade another? (recomendações práticas)*, de Shivank Agrawal (Scaler Topics) (https://www.scaler.com/topics/llm-as-a-judge/), *Evaluating Small Language Models for Front-Door Routing: A Harmonized Benchmark and Synthetic-Traffic Experiment*, de Warren Johnson (Plexor Labs), Charles Lee (Project Autobots) (https://arxiv.org/html/2604.02367), *Jev vs GPT and Claude: independent benchmark (roteamento de intenção e injeção de prompt)*, de Adel Dahani (AY Automate) (https://www.ayautomate.com/blog/jev-vs-llm-benchmark), *TypeSafe's Jev scores 62.6% asked once and 95% split five ways*, de Rajesh Beri (https://www.beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval), *How to classify, route, and score with Jev and AI SDK (Vercel)*, de Vercel (Knowledge Base) (https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk). O que perguntar antes de automatizar a decisão está em [[antes-de-automatizar-uma-decisao]].

## Princípio

**Nota não substitui teste.** O que é checável por máquina (compila, testes passam, schema válido, segredo não vazou) se checa por máquina, antes de qualquer juiz. A nota entra depois, para o que não se deixa codificar: cobertura do que foi pedido, legibilidade, aderência às convenções, qualidade de um texto. E entra como **uma entrada da política de liberação**, nunca como verdade.

## Arquitetura em camadas

1. **Determinístico primeiro**, rápido e barato: build, testes, lint, validação de schema. Falhou, parou.
2. **Classificador pequeno** para o volume: rotular, rotear, filtrar, rankear candidatos. Barato e rápido; 6 a 8 pontos abaixo do modelo grande em acurácia, segundo o benchmark de roteamento no arXiv.
3. **Modelo de fronteira só para os incertos**: quem ficou abaixo do limiar de confiança sobe de camada. Na medição da AY Automate, a cascata igualou o modelo grande sozinho a um quarto do custo.
4. **Fila humana** para o que nem o modelo grande fecha, e para uma amostra do que passou, que é o que calibra o sistema.

## Como se escreve uma rubrica que funciona

- **Ancorada**: cada nível descreve o que se vê ("3 = compila, mas sem tratamento de erro de borda"), com 3 a 5 exemplos avaliados por humano cobrindo a escala e os casos limítrofes. "Dê nota de 1 a 5" produz notas amontoadas no 4; em juízes de visão, Gemini, LLaVA e CogVLM dão quase sempre perto de 4 [[2026-10-31-chen-mllm-as-a-judge]].
- **Um fator por pergunta**: num teste de phishing, uma pergunta larga deu 62,6% e cinco perguntas atômicas com calibrador deram 95,0%, com um regex de duas linhas em 91,8% e o Haiku também subindo com as mesmas perguntas (*TypeSafe's Jev scores 62.6% asked once and 95% split five ways*, de Rajesh Beri). O julgamento se monta na aplicação, não no prompt.
- **Falha crítica separada da média**: segurança, dado inventado, roteamento errado de dinheiro derrubam sozinhos, por mais alta que seja a média.
- **Raciocínio antes da nota**, JSON estrito com schema, e juiz de outra família de modelo para não se favorecer. A autopreferência tem primária: acompanha a capacidade de o juiz se reconhecer [[2026-10-31-panickssery-autorreconhecimento-e-autopreferencia]] e, no CALM, vai de +5,4% a +9,4% no Claude-3.5, no GPT-4o e no GPT-4-Turbo (no ChatGPT, −16,6%) [[2026-10-31-ye-calm-doze-vieses-do-juiz]]; Gu chama a separação de "only a stopgap", porque impede usar o melhor avaliador nos modelos de ponta [[2026-10-31-gu-survey-llm-as-a-judge]]. O "raciocínio antes da nota" tem evidência mista ([[refinamento-iterativo-com-criticos]], seção 3).

## Como se escolhe o limiar

Não existe "4 de 5 é pronto". O limiar sai de um **conjunto rotulado pela própria pessoa**, 50 a 150 casos estratificados, comparando a decisão do modelo com a dela: kappa de Cohen ≥ 0,6 para portão, Spearman ≥ 0,7 para ranking. Um **conjunto âncora** de 20 a 30 casos com rótulo fixo roda a cada troca de modelo ou rubrica para pegar deriva. O acordo da pessoa consigo mesma na rubrica é o teto: o juiz não o supera. Num portão de conteúdo, a pessoa é a referência na forma e no gosto; a integridade se mede contra o fato, e o modelo barato contra o juiz ([[calibracao-por-dimensao]]). Para ranking, comparação pareada nas duas ordens, vitória só quando as duas concordam; nota absoluta amontoa e sofre viés de tamanho.

## Três casos de uma empresa pequena

**Ranking de conteúdo gerado** (ângulos, posts, derivações de uma ideia). Rubrica derivada do público e da voz, em perguntas atômicas: fala com o segmento certo? tem gancho verificável? contraria uma crença limitante? Cada uma como pergunta de nota ou de sim ou não no modelo pequeno; a soma ponderada ordena; os cinco primeiros vão para a pessoa. Escolher o vencedor sozinho não se sustenta bem: o modelo filtra por testes concretos e a escolha fica com a pessoa. Pareado nas duas ordens quando a decisão for entre dois. O conjunto rotulado nasce das escolhas que a pessoa já faz ao curar.

**Estágio de funil de quem conversa** (lead, contato, qualificado, agendado, fechado). Escolha com lista fechada e, num modelo de decisão tipado, a abstenção como pergunta companheira ("algum estágio se aplica?") em vez de uma opção dentro da lista; as consultas exatas ("já comprou?") no código; evidência comportamental por estágio ("pediu preço", "confirmou data"); e limiar assimétrico: se promover cedo custa caro, otimizar precisão; se perder interessado custa mais, otimizar recall e mandar os incertos para a fila. Estágio inferido de tom ou cargo não conta.

**Nota de código antes do PR.** O juiz aqui é o modelo de fronteira em contexto limpo, depois dos testes, com a issue, os arquivos e o resultado dos testes no contexto, nunca só o diff. O modelo pequeno serve para triar (este diff toca auth, pagamento, migration? então revisão de segurança obrigatória), não para julgar. A política de merge: checagens obrigatórias passam, nenhum achado de severidade alta, nota mínima por critério e não só na média, e divergência entre dois juízes vai para a pessoa.

## Quando a nota não deve decidir

Conteúdo checável (é teste, não juiz); decisão de segurança (o juiz tria, a pessoa decide); domínio que o modelo não tem; e volume em que pontuar tudo dobra o custo de inferência. Nesses casos o portão é determinístico ou humano, e o modelo entra como triagem.
