---
titulo: "Structure Enables Effective Self-Localization of Errors in LLMs"
tipo: paper
autor: "Ankur Samanta, Akshayaa Magesh, Ayush Jain, Kavosh Asadi, Youliang Yu, Daniel R. Jiang, Boris Vidolov, Kaveh Hassani, Paul Sajda, Jalaj Bhandari, Yonathan Efroni"
url: "https://arxiv.org/abs/2602.02416"
publicado_em: 2026-02-02
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [self-correction, error-localization, self-verification, verification, chain-of-verification, self-consistency]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 02/02/2026, v2 (lida) em 30/05/2026; sem comentário de conferência. Autores da Meta AI e Meta Superintelligence Labs, com Columbia (Samanta, Sajda) e Tel Aviv (Efroni); Bhandari e Efroni com contribuição igual. Lido em 2026-10-29 (skill de revisão), pela pergunta de onde a etapa que confere um achado consegue apontar o erro.

## A pergunta

A autocorreção de modelos de linguagem costuma não funcionar: pedir ao modelo que revise a própria resposta várias vezes não converge para o certo, e o ganho que aparece muitas vezes é só sorteio de nova resposta. Os autores separam o problema em três capacidades: **verificar** (a resposta está errada?), **localizar** (em que passo errou?) e **corrigir** (refazer a partir dali). Trabalho anterior (Tyen et al., 2024) mostrou que o modelo corrige quando alguém de fora diz onde está o erro, mas não consegue achar o erro sozinho. A pergunta aqui: o modelo consegue localizar o erro no próprio raciocínio se o raciocínio for gerado em passos discretos?

## O método (seções 3 e 4, apêndice C)

- **Pensamento por pensamento (Thought MDP).** Em vez da cadeia de raciocínio corrida, o modelo gera um passo por chamada: cada passo é "uma observação, um cálculo ou uma dedução", fechado com o marcador `</thought>`. A cada chamada o prompt traz a pergunta, dois exemplos resolvidos no formato e os passos já gerados. O próprio modelo decide onde o passo termina; ninguém recorta o texto depois. Termina quando aparece a resposta final em `\boxed{}` ou com 100 passos.
- **Verificação.** Um portão: só a resposta julgada errada entra no laço de correção. A fonte do julgamento é configurável: um oráculo (a resposta certa conhecida) ou o próprio modelo.
- **Localização.** O modelo recebe o raciocínio numerado ("Step 1: ..., Step 2: ...") e o pedido de verificar passo a passo, procurar falha lógica, erro de conta ou suposição errada, e devolver o número do **primeiro** passo com erro crítico, com a justificativa (ou 0 se estiver tudo certo).
- **Reamostragem.** O sistema corta o raciocínio antes do passo apontado e gera de novo a partir do último passo tido como certo, com o mesmo prompt de geração. É uma busca em profundidade no espaço de pensamentos: gera, volta ao achar erro, tenta outro caminho.
- **Três saídas do laço:** (1) a verificação aprova a resposta; (2) a verificação diz que está errado mas a localização não acha erro (desacordo V/L); (3) acaba o limite de iterações.
- **Controle: Token-ICS.** O mesmo laço sobre cadeia de raciocínio comum; como não há passos numerados, o modelo tem de citar literalmente o trecho errado, e o corte é feito por busca do texto. Quando a citação não bate com o texto (pequenas variações), refaz do zero.
- **Inspiração declarada:** o córtex cingulado anterior monitora erros em pontos de decisão discretos, nem neurônio a neurônio nem na sequência inteira, e o cérebro testa alternativas mudando um ponto de decisão.

## Como mediram (seção 5)

- Oito modelos abertos de 3B a 120B parâmetros: LLaMA 3 (3B, 8B, 70B), Qwen 2.5 (7B, 14B, 32B), GPT-OSS (20B, 120B).
- Seis tarefas com resposta checável por igualdade exata: AMC23 e AIME (competição de matemática), MATH500 nível 5, MathQA, CSQA (senso comum) e GPQA (ciência de pós-graduação). 100 problemas por tarefa (AMC23 tem 40).
- Temperatura 0,5, top-p 0,9; até 10 iterações nos métodos iterativos.
- **Oráculo de localização:** três modelos de fronteira (Sonnet 3.7, GPT-4.1, GPT-5-mini) apontam o primeiro passo errado de cada resposta; quando discordam, vale o mais cedo. Concordância entre eles: 51% unânime, 74% dentro de um passo, 85% dentro de dois. Na cadeia corrida a concordância cai para 58% (tolerância de 10% do tamanho da solução). Os autores avisam que o oráculo é consenso de juízes, não verdade anotada.
- **Prefixo limpo:** a localização acerta quando aponta o primeiro erro (ou antes dele); o que sobra antes do corte não tem erro. Se aponta um passo depois do primeiro erro, o prefixo continua contaminado.

## Resultados

**Com verificação por oráculo (o modelo sabe que errou, não sabe onde; tabela 4, apêndice H):**

- A versão em passos fica de 20 a 40% acima da cadeia comum (o resumo e a figura 2; o ganho somado de gerar em passos e de corrigir) e ganha da versão corrida e do voto de maioria de 10 amostras (MV@10) na maioria das células; as exceções são poucas (LLaMA-3B no AIME, MV@10 28 contra 12; Qwen-32B no GPQA, corrida 68 contra 67). Exemplos: GPT-OSS-20B no AIME vai de 21% para 72% (Token-ICS 22%, MV@10 20%); GPT-OSS-120B no GPQA de 45% para 79% (Token-ICS 56%); LLaMA-3B no GPQA de 20% para 63%.
- Só gerar em passos já sobe o acerto inicial, antes de qualquer correção: +6,5 pontos em média, ganho em 36 de 48 pares modelo-tarefa; nos modelos de 20B para cima, +35 a +41 no AIME e +18 a +30 no AMC23 (tabela 3, apêndice D). Em modelos pequenos às vezes cai (LLaMA-3B no CSQA, de 69 para 59).

**Localização (seção 5.2, apêndice G):**

- Em passos, 60 a 80% das localizações deixam prefixo limpo; na cadeia corrida, 30 a 45% (41,7% no agregado). Na cadeia corrida o modelo tende a apontar o erro **mais tarde** do que o oráculo (58,3% dos casos), perdendo a causa.
- Modelos maiores localizam com mais precisão: o desvio em relação ao oráculo se concentra em zero; os menores erram mais para depois. Os autores conferem que o ganho não vem de o modelo apontar sempre o primeiro passo (conservadorismo).
- Reamostrar de um prefixo limpo corrige de 2 a 4 vezes mais do que reamostrar de um prefixo contaminado: o erro que fica no prefixo puxa a nova tentativa para o mesmo buraco. O exemplo do apêndice A mostra isso: na primeira volta o modelo aponta o passo 10, refaz e erra igual; na segunda aponta o passo 6, a causa real, e acerta.
- Ressalva de medida: só 27,5% das localizações (5.133 de 18.655) saem no formato pedido e têm oráculo válido; a análise principal usa essas e confere que com todas (fallback de parsing) os números quase não mudam (prefixo limpo 65,1% contra 62,6%).

**Sem oráculo, com autoverificação (seção 6):**

- O modelo verifica com acerto agregado de 60 a 80%, mas isso engana: a cada iteração ele aponta mais erros (recall sobe) e reconhece menos respostas certas (especificidade despenca). A resposta certa fica no laço e acaba quebrada. Ter o conhecimento para resolver não dá a capacidade de verificar a solução.
- Tabela 1 (médias, 9 amostras por iteração nas variantes de voto):

| Verificação | Recall | Especificidade | Quebrou (certas que viraram erradas) | Consertou (erradas que viraram certas) |
|---|---|---|---|---|
| Uma chamada | 68,3% | 66,9% | 10,9% | 6,2% |
| Qualquer amostra diz errado | 94,6% | 30,9% | 21,4% | 8,1% |
| Maioria diz errado | 70,2% | 69,9% | 12,7% | 6,3% |
| Todas dizem errado | 34,7% | 94,6% | 6,0% | 3,5% |

- Leitura dos autores: o voto de autoconsistência só desloca a troca entre recall e especificidade; em todas as regras a autocorreção **quebra mais do que conserta**.
- Por saída do laço (tabela 2): quando a autoverificação aprova, o saldo é positivo (quebrou 2,5%, consertou 6,4%, +3,9); no desacordo V/L, quebrou 51,3% e consertou 2,0% (−49,3); no limite de iterações, quebrou 77,4% e consertou 5,4% (−72,0).
- **A salvaguarda (Thought-ICS-A):** nas duas saídas de baixa confiança (desacordo V/L e limite de iterações), devolver a **resposta inicial** em vez da última tentativa. Com isso o saldo fica positivo em quase toda iteração (figura 8).
- Contra Self-Refine (critica e refaz do zero, até 10 vezes) e CoVe fatorado (2 a 4 perguntas de verificação respondidas sem ver a solução, uma passada só), a Thought-ICS-A ganha em todos os modelos menos o LLaMA-3B (figura 9). Na tabela 7, os ganhos aparecem de 14B para cima (GPT-OSS-120B no AIME: cadeia comum 24, Self-Refine 26, CoVe 36, Thought-ICS-A 67); de 3B a 8B a cadeia comum sem correção muitas vezes é o melhor resultado, e a autocorreção atrapalha (LLaMA-3B no CSQA: 69 sem correção, 56 com Thought-ICS-A).

**Custo e diversidade (apêndices I e J):** com oráculo, a versão em passos gasta 1,21 vez os tokens de correção da corrida (2.610 contra 2.150) com 19,1 pontos a mais de acerto (67,2% contra 48,1%), 13% menos tokens por resposta certa; nos modelos maiores gasta menos tokens em termos absolutos (Qwen-32B −38%, GPT-OSS-120B −46%). Em passos, 77,5% das iterações de correção mudam a resposta (58,9% na corrida); na corrida a mesma resposta se repete entre iterações seguidas em 44,6% dos casos (30,6% em passos).

## A recomendação

A estrutura do raciocínio é o que torna a localização possível: gerar em passos com fronteira decidida pelo modelo, apontar o primeiro passo errado e refazer dali. Em uso autônomo, o gargalo é a verificação; enquanto ela não melhora, só aceite a correção quando a autoverificação aprova, e nas saídas de baixa confiança volte à resposta original.

## Limites declarados

- Modelos de 3B a 120B e tarefas com resposta verificável (matemática, ciência, senso comum); modelos de fronteira e domínios abertos ficam para depois.
- Não está claro se é autocorreção de verdade ou reamostragem estruturada que dá certo.
- O oráculo de localização é consenso de modelos de fronteira, não anotação; as métricas de desvio e prefixo limpo servem para comparar estruturado contra corrido, não como acurácia absoluta.
- A localização pode melhorar com prompt, métodos de confiança ou treino; a autoverificação continua o gargalo e pede treino específico.
