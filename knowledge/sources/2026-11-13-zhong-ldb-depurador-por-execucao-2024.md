---
titulo: "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"
tipo: paper
autor: "Li Zhong, Zilong Wang, Jingbo Shang"   # cabeçalho do HTML da v6; os três da University of California, San Diego
url: "https://arxiv.org/abs/2402.16906"
publicado_em: 2024-02-25   # v1 no histórico de envios da página do resumo; a v6, lida, é de 2024-06-06
capturado_em: 2026-11-13
areas: [agent-engineering]
entrada: pesquisa
tags: [ldb, code-debugging, runtime-execution, basic-blocks, self-correction, self-debugging, humaneval, reflexion, code-generation]
licenca: "arXiv.org perpetual non-exclusive license (nonexclusive-distrib 1.0): escrita no cabeçalho do HTML da v6 ('License: arXiv.org perpetual non-exclusive license') e no link de licença da página do resumo (http://arxiv.org/licenses/nonexclusive-distrib/1.0/); não permite cópia, e a ficha não leva o integral"
---

# LDB: o depurador que lê a execução bloco a bloco

Ficha de estudo (`knowledge/sources/README.md`, item 2), em palavras próprias, na ordem do paper. Não há integral: a licença do arXiv escolhida pelos autores não permite cópia.

**Proveniência.** Paper de Li Zhong, Zilong Wang e Jingbo Shang (University of California, San Diego), arXiv 2402.16906, categoria cs.SE. Versões no histórico de envios da página do resumo (https://arxiv.org/abs/2402.16906, baixada com curl em 2026-11-13): v1 em 25/02/2024, v2 em 02/03, v3 em 10/03, v4 em 29/04, v5 em 04/06 e v6 em 06/06/2024; o cabeçalho do HTML da v6 confirma "06 Jun 2024". A página do resumo marca "Comments: Preprint" e não diz em que evento o paper saiu. Lida em 2026-11-13 a v6 em HTML (https://arxiv.org/html/2402.16906v6), baixada para a cópia de trabalho e lida no texto extraído, do resumo ao apêndice J, com as tabelas 1 a 7 e as notas de rodapé; as figuras 1 a 9 só pela legenda e pelo texto que as comenta (a extração não traz os gráficos nem os prompts desenhados). Das versões anteriores, só se abriram a Tabela 2 e a frase sobre os programas do Reflexion, na v1 e na v4 (abaixo, "Versões anteriores").

**Conferência lado a lado** (2026-11-13, pela régua do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (número, nome, modelo, valor) fica fora, e as citações literais estão à parte. Resultado: 63 de 78 unidades seguem a fonte (quase todas condensam, em outra língua e na ordem do paper, uma frase ou um grupo de frases seguidas, como pede a ficha de estudo de fonte longa); a maior sequência na ordem da fonte é de 9 unidades seguidas, nas seções 3.3 a 3.5 (detalhe no fim da ficha). Na revisão de 2026-11-19, a prosa de "Iterações" e a de "Granularidade" foram refeitas: a primeira abre pelo LDB e só depois dá os outros métodos e a leitura dos autores, e a segunda abre pelo resultado e trata a função antes da linha, ao contrário do paper; com isso, a sequência de 9 cai para 8 (termina na primeira frase das iterações) e a de 8 da granularidade ao estudo de caso se parte (a maior que sobra ali é de 5, a dificuldade e o estudo de caso), e nos dois parágrafos não há mais de 2 unidades seguidas na ordem do paper. A granularidade passou de 3 para 4 frases, e o total, de 78 para 79 unidades; pela conta severa, as 7 dos dois parágrafos ainda condensam frases do paper, agora em outra ordem, e o resultado fica em 64 de 79. O detalhe no fim da ficha é o da conferência de 2026-11-13. A ficha continua, no resto, na ordem do paper, como a ficha de estudo permite. O `parafrase.py` saiu com o código 3, com 0 trecho e 0 frase colada (ficha em português, fonte em inglês: o script não mede tradução, e a conferência é esta conta).

## A ideia

Depurar programa gerado por modelo de linguagem do jeito que um programador faz com um depurador: rodar o programa num teste que falhou, parar ao fim de cada trecho e olhar o valor das variáveis. O LDB (Large Language Model Debugger) corta a execução em blocos básicos, mostra ao modelo o estado das variáveis antes e depois de cada bloco e pede um veredito por bloco contra a descrição da tarefa; com os vereditos, o modelo reescreve o programa. Os trabalhos anteriores, segundo os autores, tratam o programa como um todo e só usam o que sai depois da execução (resultado dos testes, mensagem de erro).

## Formulação

Herdada do Self-Debugging (Chen et al., 2023c), a formulação separa os testes visíveis, que o gerador da semente e o depurador veem, dos ocultos, guardados para avaliar o programa final; a descrição da tarefa é um parágrafo quando se gera código a partir de texto e o programa de origem quando se traduz.

## O método: a semente e os passos que se repetem

| Passo | O que faz |
|---|---|
| 0. Semente | o modelo gera o programa; se ele falha num teste visível, começa a depuração |
| 1. Perfil | o programa roda no teste visível que falhou; o grafo de fluxo de controle dá os blocos básicos, e o caminho percorrido é o traço de execução |
| 2. Estado intermediário (parte do perfil da execução, passo 1, na seção 2.2 do paper) | para cada bloco do traço, guardam-se as variáveis em escopo com o valor de entrada e o de saída |
| 3. Depuração | o modelo recebe os estados e dá, para cada bloco, verdadeiro ou falso e uma explicação, comparando com a descrição da tarefa |
| 4. Regeneração | vereditos, explicações e descrição vão num novo pedido, e o modelo reescreve o programa |
| Parada | todos os testes visíveis passam, ou acaba o limite de iterações |

- **Bloco básico** (apêndice B): trecho reto de código, com uma entrada e uma saída; se a primeira instrução roda, todas as outras rodam uma vez, em ordem. O grafo de fluxo de controle tem um bloco por nó e as transições como arestas.
- **Depuração seletiva:** laço e recursão alongam o traço além do limite de tokens; inspirado no programador que pula a parte tediosa, o LDB amostra só alguns blocos. No experimento, com mais de 10 blocos, ficam os 5 primeiros e os 5 últimos (apêndice E).
- **Depuração em lote:** como todos os estados saem de uma única execução da semente, o LDB manda todos os blocos numa só consulta e recebe todos os vereditos juntos. O apêndice F estima o custo: sem lote, os tokens crescem com o quadrado do número de blocos; em lote, crescem na proporção dele.

## Montagem dos experimentos

| Item | Valor |
|---|---|
| Conjuntos | HumanEval e MBPP (texto para código); TransCoder (C++ para Python) |
| Métrica | Pass@1 nos testes ocultos |
| Testes visíveis no HumanEval | os que estão na própria descrição da tarefa |
| Testes visíveis no MBPP | o primeiro de cada problema; o resto fica oculto |
| Testes visíveis no TransCoder | todos (podem ser gerados rodando o programa C++, que o modelo vê) |
| Modelos | GPT-3.5 (turbo-0613); CodeLlama 34B-Instruct; StarCoder, cerca de 15B |
| Parâmetros do GPT-3.5 na tabela | ≥175B, por suposição dos autores (maior que o GPT-3) |
| Sementes | mesmos prompts e parâmetros de geração do Self-Debugging |
| Máximo de iterações | 10 |
| Decodificação na depuração | gulosa, temperatura 0 |
| Limites de amostragem | 10 blocos e 3.097 tokens de entrada |
| Código | https://github.com/FloridSleeves/LLMDebugger (anunciado como "will be released") |

## Linhas de base

- **Sem depurador:** a nota do programa-semente.
- **Self-Debugging (+Expl.):** o modelo explica o programa linha a linha, e a explicação serve de retorno.
- **Self-Debugging (+Trace):** o modelo simula a execução de cabeça (dry run), e a simulação serve de retorno.
- Os dois do Self-Debugging foram reimplementados pelos autores, pelas instruções do paper original, porque o código não estava aberto. Todos os métodos usaram o mesmo modelo, os mesmos testes visíveis, as mesmas sementes e o mesmo formato de prompt. Quando o texto diz só "Self-Debugging", vale a melhor das duas variantes.
- **Amostragem repetida** (só na seção 3.5): gerar de novo até a solução passar no teste visível.

## Tabela 1: resultados principais (Pass@1, %)

| Modelo | Depurador | HumanEval | TransCoder | MBPP |
|---|---|---|---|---|
| GPT-3.5 | sem depurador | 73,8 | 82,3 | 67,6 |
| GPT-3.5 | SD (+Expl.) | 81,1 (+7,3) | 85,9 (+3,6) | 74,4 (+6,8) |
| GPT-3.5 | SD (+Trace) | 80,5 (+6,7) | 86,1 (+3,8) | 72,6 (+5,0) |
| GPT-3.5 | LDB | 82,9 (+9,1) | 87,7 (+5,4) | 76,0 (+8,4) |
| CodeLlama 34B | sem depurador | 49,4 | 69,8 | 51,2 |
| CodeLlama 34B | SD (+Expl.) | 53,0 (+3,6) | 79,4 (+9,6) | 55,6 (+4,4) |
| CodeLlama 34B | SD (+Trace) | 54,3 (+4,9) | 76,4 (+6,6) | 57,2 (+6,0) |
| CodeLlama 34B | LDB | 55,5 (+6,1) | 79,6 (+9,8) | 57,4 (+6,2) |
| StarCoder 15B | sem depurador | 39,0 | 61,8 | 51,6 |
| StarCoder 15B | SD (+Expl.) | 38,4 (−0,6) | 68,9 (+7,1) | 54,4 (+2,8) |
| StarCoder 15B | SD (+Trace) | 39,0 (+0,0) | 65,7 (+3,9) | 54,8 (+3,2) |
| StarCoder 15B | LDB | 39,6 (+0,6) | 69,8 (+8,0) | 55,4 (+3,8) |

Cada bloco da tabela é um modelo, que o texto chama de backbone; a diferença entre parênteses é sobre a linha sem depurador. O ganho máximo, 9,8 pontos, é o do CodeLlama no TransCoder.

## Por que o ganho, segundo os autores

O ponto de partida do argumento é a linha sem depurador: os testes visíveis já iam no pedido da semente e, sozinhos, não bastaram, o que se alinha à suposição dos autores de que é a execução real que ancora o raciocínio do modelo. Daí duas razões para o LDB ganhar do Self-Debugging. A primeira é a granularidade: o veredito bloco a bloco aponta ao modelo onde está o defeito. A segunda é a fonte do dado, que vem de fora do modelo: apoiados em Huang et al. (2023c), os autores dizem que o modelo, ao refletir sobre um programa, erra o valor das variáveis e o caminho em ramos e laços, e um retorno errado desvia o conserto; é com isso que explicam as duas variantes do Self-Debugging não melhorarem o StarCoder no HumanEval.

## Tabela 2 (seção 3.4): sementes de geradores mais fortes, com o GPT-3.5 depurando

| Depurador | Semente do GPT-3.5 | Semente do GPT-4 | Semente do Reflexion |
|---|---|---|---|
| sem depurador | 73,8 | 87,2 | 91,5 |
| SD (GPT-3.5) | 81,1 (+7,3) | 88,4 (+1,2) | 92,1 (+0,6) |
| LDB (GPT-3.5) | 82,9 (+9,1) | 89,6 (+2,4) | 95,1 (+3,6) |

| Condição | Fato |
|---|---|
| Conjunto | só o HumanEval, "como exemplo" |
| Modelo do depurador (SD e LDB) | GPT-3.5 (turbo-0613) |
| Semente do GPT-4 | gerada pelos autores com o GPT-4 (1106-preview), na montagem da seção 3.1 |
| Semente do Reflexion | os programas gerados publicados no repositório oficial do Reflexion, usados como estão |
| Endereço do repositório na nota | https://github.com/noahshinn/reflexion |
| Coluna do GPT-3.5 | entra como referência (é a mesma linha da Tabela 1) |
| Leitura dos autores | o depurador é mais fraco que os dois geradores e ainda assim melhora os dois; o LDB passa o Self-Debugging |
| 95,1% | apresentado como novo estado da arte em geração de código no HumanEval |
| Modelo que gerou os programas do Reflexion | não informado na v6 |

## Iterações (seção 3.5 e apêndice G)

O que a curva das rodadas separa é quem continua tirando proveito delas: o LDB, que no HumanEval com o GPT-3.5 começa subindo mais devagar que os outros, segue melhorando até a décima rodada, termina na frente e, quando o experimento se estende a 20, chega a 84,1%. Os outros três (a amostragem repetida e as duas variantes do Self-Debugging) também melhoram a semente dentro das 10 rodadas, mas o Self-Debugging quase para depois da segunda e, da terceira em diante, já não se distingue da amostragem repetida. Para os autores, é sinal de que a autocorreção tem teto: o modelo que explica ou simula o próprio programa entende melhor a tarefa, sem amarrá-la ao código concreto, e o ganho se esgota em poucas rodadas.

## Granularidade (seção 3.6 e apêndice E)

| Nível | GPT-3.5: acerto | GPT-3.5: tokens por problema | GPT-3.5: rodadas | CodeLlama: acerto | CodeLlama: tokens | CodeLlama: rodadas |
|---|---|---|---|---|---|---|
| sem depurador | 73,8 | — | — | 49,4 | — | — |
| linha | 80,5 (+6,7) | 24K | 6,4 | 53,7 (+4,3) | 72K | 9,1 |
| bloco | 82,9 (+9,1) | 23K | 6,2 | 55,5 (+6,1) | 52K | 7,8 |
| função | 79,9 (+6,1) | 27K | 8,1 | 53,7 (+4,3) | 54K | 9,3 |

| Nível | Amostragem quando o traço é longo |
|---|---|
| linha | acima de 50 linhas, as 25 primeiras e as 25 últimas (cinco vezes o limite de blocos, pelo tamanho médio de bloco em Rotenberg et al., 1996) |
| bloco | acima de 10 blocos, os 5 primeiros e os 5 últimos |
| função | estado só na entrada e na saída da função; com traço longo, 25 linhas do começo e 25 do fim |

O bloco fica com o melhor acerto e o menor custo nos dois modelos, embora os três níveis melhorem a semente, e os autores explicam os dois que perdem por lados opostos. A função perde por ser grossa demais: o modelo recebe o programa quase inteiro, mas o estado só na porta de entrada e na de saída conta pouco da execução, e a depuração se arrasta por mais rodadas, que é de onde vem o gasto de tokens. A linha perde por ser fina demais: a hipótese deles é que uma linha isolada tem sentido incompleto, e o modelo não a entende o bastante para achar o erro. Quanto ao custo da linha, depende do modelo: com o GPT-3.5 ela gasta menos que a função, e com o CodeLlama, mais.

## Dificuldade (seção 3.7)

Nos problemas do TransCoder que o LDB conserta, o GPT-4 (1106-preview) classificou a dificuldade a partir da solução canônica, em fácil, médio e difícil. O acerto do GPT-3.5 cai com a dificuldade, e o ganho do depurador cresce: o maior, 9,1 pontos, é nos difíceis.

## Estudo de caso (seção 3.8)

Uma tarefa do HumanEval pede duas condições: lista em ordem crescente e nenhum número repetido mais de uma vez. A semente testa a primeira certo, mas proíbe qualquer repetição (`lst.count(x) > 1`). O LDB aprova os blocos 0 a 4, acha o erro no bloco 5 e propõe `lst.count(x) > 2`; o programa corrigido passa nos testes visíveis e nos ocultos.

## Apêndices

### A: depuradores melhores (Tabela 3)

| Semente do Reflexion | Acerto no HumanEval |
|---|---|
| sem depurador | 91,5 |
| + LDB (GPT-3.5, turbo-0613) | 95,1 (+3,6) |
| + LDB (GPT-4, 1106-preview) | 96,9 (+5,4) |
| + LDB (GPT-4o, 2024-05-13) | 98,2 (+6,6) |

O texto do apêndice liga o 98,2% à combinação de sementes do Reflexion com o GPT-4o depurando.

### D: tempo (Tabela 4, HumanEval, GPT-3.5)

| Etapa | LDB | Self-Debugging |
|---|---|---|
| Rodar o programa | 0,01 s | 0,01 s |
| Pedir o retorno ao modelo | 0,09 s de perfil + 9,25 s | 9,84 s |
| Pedir o programa novo | 7,83 s | 7,17 s |
| Outros | 0,05 s | 0,01 s |
| Total | 17,23 s | 17,08 s |

O único custo a mais do LDB é o perfil, feito por análise de programa, e os autores o tratam como desprezível diante da variação das outras etapas. Todos os passos são automáticos.

### H: os vereditos estavam certos? (Tabela 7)

| Medida | HumanEval | MBPP | TransCoder |
|---|---|---|---|
| Bloco errado localizado certo | 93,7% | 95,3% | 86,7% |
| Erro de sintaxe entre os consertados | 18,8% | 23,2% | 20,0% |
| Erro semântico entre os consertados | 81,2% | 76,8% | 80,0% |

Quem julgou foi o GPT-4 (1106-preview), sobre os casos que o LDB consertou com o GPT-3.5, vendo a tarefa, a semente, a execução, as respostas do depurador e o programa final; o GPT-4 também classificou o tipo de erro. A hipótese dos autores para o TransCoder ficar abaixo: os programas são mais complicados, e a intenção do C++ original está implícita. Sobre a predominância do erro semântico, dizem que o de sintaxe ficou raro com os modelos atuais e que é no semântico que a informação de execução mais ajuda.

### Outros

- **I, extensão:** o LDB foi feito em Python, mas não usa nada próprio da linguagem; para outra, basta trocar o executor e as ferramentas de análise. Experimentos em várias linguagens (HumanEval-X) ficam para depois.
- **J, prompts:** há um prompt para o modo de chat e outro para o de completar texto (figuras 8 e 9, não lidas).

## Limites declarados

O LDB herda o limite da depuração humana: sem testes corretos, não há o que executar nem com que comparar o fluxo. Fica em aberto se um modelo conseguiria se corrigir só olhando a execução intermediária, sem saber se o resultado está certo (depuração sem caso de teste).

## Versões anteriores (conferência parcial, na própria série do arXiv)

| Versão | Semente do GPT-4, sem depurador | SD sobre a semente do GPT-4 | LDB sobre a semente do GPT-4 | Frase sobre o Reflexion |
|---|---|---|---|---|
| v1 (25/02/2024) | 75,0 | 82,3 (+7,3) | 82,9 (+7,9) | diz ter escolhido a versão do Reflexion baseada no GPT-3.5 |
| v4 (29/04/2024) | 87,2 | 88,4 (+1,2) | 89,6 (+2,4) | sem menção ao modelo do Reflexion |
| v6 (06/06/2024, lida) | 87,2 | 88,4 (+1,2) | 89,6 (+2,4) | sem menção ao modelo do Reflexion |

As colunas do GPT-3.5 e do Reflexion na Tabela 2 são iguais nas três versões. O apêndice com o GPT-4o (98,2%) não aparece na v1 nem na v4 (a busca por "GPT-4o" no HTML delas não acha nada).

## Citações

- "We attribute the advantage of LDB to the fine-grained debugging feedback and the runtime information as external supplements to the LLM self-correction." (seção 3.3)
- "can be up to 98.2% on HumanEval with Reflexion as the seed generators and GPT-4o" (apêndice A)
- "The correct test cases are mandatory in LDB so that LDB can execute the program and compare the execution flow against the task description." (Limitation)

Em palavras próprias, o resto do que a ficha usava como citação: a premissa do ganho, apoiada em Huang et al. (2023c), é que o LLM sozinho corrige mal o próprio raciocínio (seção 3.3); as sementes do Reflexion são os programas gerados que o repositório oficial do método publicou (seção 3.4); e, quando o GPT-3.5 depura, ele é mais fraco que os geradores das sementes, o GPT-4 e o Reflexion (seção 3.4).

## Lacuna e estranhezas do texto

- A v6 não diz com que modelo foram gerados os programas do Reflexion usados como semente, nem qual arquivo do repositório foi usado.
- Na Tabela 1, o texto não diz em frase própria que o modelo de cada bloco também gerou a semente; a Tabela 2 é que trata a coluna do GPT-3.5 como semente do GPT-3.5 com o GPT-3.5 depurando.
- Não há custo em dólar; o custo aparece só em tokens por problema (Tabela 5) e em segundos (Tabela 4). Não há número de execuções por resultado, nem intervalo ou desvio.
- O texto da seção 3.4 manda o leitor à "Table 3" para os resultados que estão na Tabela 2; a Tabela 3 é a do apêndice A.
- O apêndice H dá 95,5% para o MBPP no texto e 95,3% na Tabela 7.
- A seção 3.5 remete ao "Appendix 7" para as 20 rodadas, que estão na Figura 7, no apêndice G.
- A nota do repositório do Reflexion aponta para `github.com/noahshinn/reflexion`.
- O resumo e a introdução dizem que o LDB melhora "up to 9.8%"; na Tabela 1, isso é a diferença em pontos (CodeLlama no TransCoder).

## Detalhe da conferência lado a lado

Conta feita antes de 2026-11-19, quando três das seis citações viraram o parágrafo em palavras próprias depois da lista (três unidades novas, que não entraram na conta abaixo). Total de 78 unidades: 56 frases de prosa (fora títulos e citações, com as notas abaixo das tabelas) e 22 células com texto corrido (6 no método, 5 na montagem, 5 nas condições da Tabela 2, 3 na amostragem da granularidade e 3 nas versões anteriores). Ficam fora as células de fato (números, modelos, nomes de conjunto, endereços, datas, rótulos de linha).

Seguem a fonte 63, contadas pelo lado mais severo (a unidade que condensa um grupo de frases seguidas conta, mesmo resumida): as 3 de "A ideia" (resumo e legenda da Figura 1); a da formulação; as 6 células do método e as 6 frases sobre bloco básico, depuração seletiva e em lote (seção 2 e apêndices B, E e F); as 5 células da montagem (seção 3.1 e a nota da Tabela 1); as 7 das linhas de base (3.2 e 3.5); a primeira nota da Tabela 1 (legenda); 3 das 4 de "Por que o ganho" (3.3); as 5 células de condição da Tabela 2 (3.4); as 3 das iterações (3.5 e apêndice G); as 3 células e as 3 frases da granularidade (3.6 e apêndice E); as 2 da dificuldade (3.7); as 3 do estudo de caso (3.8); a do apêndice A; as 2 do apêndice D; as 3 do apêndice H; as 3 de "Outros" (apêndices I e J); as 2 do limite declarado; e a célula da v1 sobre o Reflexion (que traduz a frase daquela versão). Não seguem 15: a frase do ganho máximo da Tabela 1, a frase que anuncia as duas razões em "Por que o ganho", as 2 células e as 2 frases das versões anteriores que registram a comparação entre versões, e as 9 de "Lacuna e estranhezas", que dizem o que falta ou não bate no texto.

Sequências na ordem da fonte (unidades seguidas da ficha cujas frases da fonte andam para a frente, a até umas doze frases de distância): 9 em "Por que o ganho" (as duas razões), as condições da Tabela 2 e as duas primeiras frases das iterações, que percorrem 3.3, 3.4 e 3.5 em ordem; 8 da granularidade ao estudo de caso (3.6 a 3.8); 7 da formulação às células do método (seção 2 a 2.4); 6 da última célula da montagem às linhas de base (3.1 a 3.2); 6 do apêndice H ao J; e as outras, de 4 ou menos. O que destoa da ordem do paper é a seção "Por que o ganho", que começa pelo último parágrafo de 3.3, e as frases que juntam a seção com o apêndice correspondente.
