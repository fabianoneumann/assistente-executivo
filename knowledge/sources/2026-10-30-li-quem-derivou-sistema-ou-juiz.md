---
titulo: "Who Drifted: the System or the Judge? Anytime-Valid Attribution in LLM Evaluation Pipelines"
tipo: paper
autor: "Yitao Li"
url: "https://arxiv.org/abs/2606.15474"
publicado_em: 2026-06-13
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, judge-drift, anchor-set, human-labels, drift-detection, anytime-valid, e-process, prediction-powered-inference, cascade, evaluation-cost, policy-versioning]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 13/06/2026, a única versão, lida. Autor único (Yitao Li), sem instituição indicada no artigo. O PDF diz "Preprint. Under review." e não nomeia venue; a página do arXiv não traz comentário. Texto extraído do PDF da v1; tabelas de leitura difícil na extração (1 a 5 e 10) foram conferidas na página renderizada. Lida (camadas flexíveis de avaliação).

## A pergunta

Produtos com LLM são avaliados continuamente por outro LLM: um juiz dá nota a cada interação, um painel acompanha a média móvel e a equipe é acionada quando a nota cai. O contrato implícito é que o juiz é uma régua fixa. Mas o juiz forte é um modelo atrás de uma API: uma troca de versão ou uma atualização silenciosa de prompt ou de política muda a forma como ele dá nota, sem aviso e sem nenhuma mudança no produto. Quando o alarme dispara, o painel não responde quem derivou, o sistema ou o juiz. Errar custa nos dois sentidos: reverter um produto saudável, ou lançar uma regressão real porque o alarme foi descartado como "coisa do juiz".

O autor afirma que o problema já existe nas ferramentas em uso. A prática de mercado para vigiar o juiz (refazer, a cada nova observação, um teste z da diferença juiz contra humano numa janela móvel, com α = 0,05) dá alarme falso em 75% de fluxos sem nenhuma mudança, e 16 das 60 "detecções" acontecem antes de existir o ponto de mudança (seção 5). Um teste de α fixo repetido a cada passo não tem garantia de validade num tempo de parada que depende dos dados. Monitoramento contínuo pede ferramentas válidas a qualquer momento (e-valores e supermartingais de teste, que podem ser inspecionados a cada passo sem inflar o alarme falso). Com elas, o detector diz que algo derivou; a atribuição (sistema ou juiz) é a lacuna que o artigo preenche.

## A construção, em resumo

Parte do monitor que uma equipe preocupada com custo já usaria: um juiz barato dá nota a todo item, o juiz forte e caro é amostrado sob orçamento, e um e-processo "prediction-powered" por estrato acumula evidência válida a qualquer momento de deriva do sistema (seção 3). A isso soma um componente: um **conjunto de âncoras** fixo, com rótulos humanos, separado antes de o monitoramento começar e reavaliado pelo juiz atual num intercalamento constante, alimentando um segundo e-processo que vigia a distância do juiz aos rótulos humanos congelados (seção 4). Uma regra de janela de guarda combina os dois tempos de parada num veredito em {none, system, judge}.

A assimetria é deliberada: como as âncoras são congeladas, a deriva do produto nunca chega a elas (melhore ou estrague o sistema, a distância aos rótulos humanos nesses itens fixos não muda); só uma mudança no juiz move essa distância. O autor chama o processo das âncoras de "espelho de mão única": vê a deriva do juiz e nada mais.

Contribuições declaradas: (1) a construção das âncoras e a regra de atribuição com janela de guarda; (2) quatro proposições (validade a qualquer momento, identificação de mão única, a corrida de atribuição e a ortogonalidade dos processos), com a "lei de projeto" de que o processo das âncoras precisa correr mais rápido que o processo principal que ele guarda; (3) duas mudanças reais de juiz, não só deriva sintética, replicadas num segundo domínio sem reajuste; (4) evidência de que as alternativas clássicas falham; (5) a base com custo controlado (monitor estratificado que detecta regressões localizadas a cerca de um terço do custo de avaliar tudo com o juiz forte).

## Trabalhos relacionados

- **Inferência "prediction-powered" (PPI) e testes válidos a qualquer momento:** PPI usa um preditor barato para corrigir o viés de um conjunto pequeno de rótulos caros. O monitor principal herda o e-valor de Csillag et al. (2025b). O autor declara que não traz teoria nova de validade: a combinação de PPI, e-processo e detecção de deriva já existe; a contribuição da seção 3 é a montagem específica (um e-processo por célula rubrica×estrato com Bonferroni e um gatilho de escalonamento pela riqueza acumulada), e o material novo de fato é a construção das âncoras da seção 4.
- **Aquisição ativa e adaptativa:** Sfyraki e Wang (2026) provam que, para estimar média com PPI, amostragem adaptativa guiada por incerteza é assintoticamente igual a um orçamento fixo. O resultado do artigo é consistente com isso: o gatilho por riqueza só empata com um orçamento fixo equivalente na deriva mais fraca, e a afirmação é só sobre custo frente a outros gatilhos adaptativos.
- **Confiabilidade do LLM-juiz:** os trabalhos anteriores corrigem ou qualificam um juiz estático (tratam o erro do juiz como distorção fixa a corrigir). Este trata de um juiz cujo comportamento muda no tempo, e de separar essa mudança da mudança do sistema avaliado. Segundo o autor, nenhum trabalho anterior roda um e-processo ancorado em humanos para detectar e atribuir deriva na identidade do juiz.

## O monitor principal com juiz forte sob orçamento (seção 3)

- **Modelo do fluxo:** cada item recebe nota em R rubricas, normalizadas em [0, 1], e tem um rótulo de estrato observável (aqui, o tema), entre K estratos. O juiz barato roda em todo item; o forte só num subconjunto amostrado. Nesta seção o juiz forte é a referência confiável: queda nele é, por hipótese, queda real de qualidade.
- **Um e-processo por célula (rubrica × estrato):** testa a hipótese nula de que a média da célula não caiu abaixo de uma barra saudável menos 0,05. A barra é a média da nota do juiz forte em itens sob controle daquele estrato, estimada uma vez com dados de calibração separados; a folga de 0,05 absorve o ruído da calibração. A nota barata entra como previsão para corrigir o viés e, nos itens amostrados, o rótulo forte corrige a previsão. As apostas são previsíveis (escolhidas só com o passado) e limitadas por um teto que depende da probabilidade de amostragem. O alarme dispara quando a riqueza de qualquer célula passa do limiar de Bonferroni RK/α_sys, e a probabilidade de algum alarme falso, em qualquer tempo de parada, fica abaixo de α_sys.
- **Estratificar é necessário, não refinamento:** uma regressão localizada num estrato e numa rubrica em que o juiz barato é cego se dilui até sumir quando agregada. Sob a deriva leve, um único e-processo PPI global por rubrica nunca detecta em nenhum orçamento (censura de 1,00 com taxas de amostragem forte de 0,1, 0,2 e 0,3); o monitor estratificado detecta nos mesmos orçamentos.
- **Dois modos de gastar o orçamento:** orçamento fixo (o juiz forte é chamado com probabilidade π, distribuída de modo uniforme, por estrato ou por bandit) ou **escalonamento por evidência** (a probabilidade sobe de um piso π0 até 1 conforme a riqueza acumulada do estrato se aproxima do limiar). Como a probabilidade depende só da riqueza passada, a validade se mantém por construção. O gatilho usa a evidência acumulada, e não a nota barata, porque o juiz barato é cego justamente para a deriva que se quer pegar.
- **Custo:** cada chamada custa tokens de entrada × preço de entrada + tokens de saída × preço de saída, com cerca de 600 de entrada e 30 de saída: US$ 0,000195 por chamada barata e US$ 0,00156 por chamada forte. Frente a avaliar todo item com o juiz forte (custo 1,0), a fração de custo é 0,125 + S/L, onde 0,125 é o piso irredutível do juiz barato e S/L a taxa realizada de amostragem forte.
- **O que essa base entrega:** numa deriva localizada semissintética, todas as variantes pegam a regressão com fração de custo de 0,21 a 0,43, cerca de um terço da avaliação completa, com alarme falso medido de 0,000 nos 16 pontos de política. O escalonamento fica no canto barato (0,21 a 0,28, perto do piso 0,125 + π0 quando nada está errado); orçamentos fixos compram confiabilidade (fixo em 0,3 chega a censura de 0,28 com custo 0,43); a avaliação completa dá a menor latência (mediana de 327 passos até detectar) a preço cheio. Na Figura 1 (as duas bases), o escalonamento fica acima e à esquerda da família de orçamento fixo (mais detecção por dólar de juiz forte) e paga em latência, o eixo fraco dele, que a figura omite e a Tabela 6 registra. Usar a nota barata como gatilho desperdiça ou não funciona: um gatilho por proximidade da fronteira só detecta amostrando quase tudo (custo de cerca de 0,87 a 0,89); a regra publicada de crescimento previsto do e-valor lê zero quando o juiz barato superestima; o escalonamento por riqueza detecta a cerca de um terço desse custo. Na deriva mais fraca, empata com um orçamento fixo equivalente.

"Tudo acima depende de confiar no juiz forte", e a seção seguinte larga essa hipótese.

## As âncoras: separar a deriva do juiz (seção 4)

**O problema.** O juiz forte também é um serviço de LLM. Quando ele muda, o alarme principal fica ambíguo e o erro se compõe: o juiz contaminado alimenta o próprio processo que deveria certificar a deriva do sistema, e o detector pode afirmar com confiança uma regressão do sistema que é artefato da referência que se moveu.

**O conjunto de âncoras (Definição 1).** Uma coleção fixa de k itens com rótulos humanos congelados h(a) em [0, 1]^R, sorteada antes de o monitoramento começar e excluída de toda calibração do processo principal. A cada ρ posições do fluxo (taxa de intercalamento 1/ρ), uma âncora é sorteada uniformemente do conjunto e reavaliada pelo juiz forte atual. Para cada reavaliação calcula-se a distância reescalada entre nota do juiz e rótulo humano, (nota − rótulo + 1)/2, cortada em [0, 1]. A linha de base é a média dessa distância para o juiz do tempo zero sobre o conjunto inteiro, calculada uma vez antes do monitoramento; como as notas do juiz do tempo zero ficam em cache, ela é a média exata e não tem erro amostral.

**O e-processo das âncoras.** Para cada rubrica e cada direção (abaixo, acima), um e-processo de apostas compara a distância observada com a linha de base, com aposta previsível (no código, média da diferença sobre média do quadrado). O alarme dispara quando a maior riqueza passa de 2R/α_judge (Bonferroni sobre os 2R pares rubrica×direção). As duas direções testam se o juiz ficou mais leniente ou mais severo nas âncoras em relação aos rótulos humanos.

**A regra de atribuição.** Com τ_sys e τ_anc os primeiros alarmes do processo principal e do das âncoras, e uma janela de guarda W: veredito *none* se nenhum dispara; *judge* se as âncoras disparam e o principal não dispara ou dispara no máximo W posições antes delas; *system* se o principal dispara e as âncoras não disparam ou disparam mais de W posições depois. Quando os dois disparam dentro da janela, o veredito é *judge* por projeto: um juiz contaminado invalida o alarme principal, e o método não tenta atribuir as duas coisas ao mesmo tempo.

**Garantias.** O autor diz que as afirmações de validade vêm de resultados conhecidos sobre supermartingais de teste; a contribuição é a construção a que se aplicam.

- **Proposição 1 (validade a qualquer momento):** sem mudança no juiz, a probabilidade de a família das âncoras disparar em falso, em qualquer horizonte escolhido pelos dados, é no máximo α_judge. Só exige que as distâncias sejam limitadas: não precisam ser gaussianas, independentes entre rubricas nem de variância estável, e não há fluxos de calibração nem horizonte fixo, ao contrário dos detectores clássicos.
- **Proposição 2 (identificação):** as observações das âncoras dependem só dos itens fixos, dos rótulos congelados e do juiz atual. Deriva do sistema (mudança na distribuição dos itens novos ou na qualidade real deles) não altera a distância nas âncoras, então só uma mudança do juiz viola a nula das âncoras. Sob deriva pura do sistema, P(veredito = judge) ≤ α_judge para qualquer W; sem deriva nenhuma, P(veredito diferente de none) ≤ α_sys + α_judge. É um teste de mão única da identidade do juiz; pegar a deriva do juiz depressa o bastante é questão de poder, não de validade.
- **Proposição 3 (a corrida de atribuição):** sob deriva do juiz, atribuir ao sistema exige que o processo principal contaminado dispare mais de W posições antes das âncoras. Essa probabilidade não aumenta quando crescem W, a taxa de intercalamento e o tamanho do conjunto de âncoras, e não diminui quando cresce o poder de amostragem do processo principal. A janela de guarda custa latência de atribuição, nunca validade, e não muda o evento total de "deriva detectada"; a regra só decide o rótulo.
- **Proposição 4 (ortogonalidade):** o tempo das âncoras independe da configuração do principal (política, orçamento, π), e o principal independe do intercalamento, porque as reavaliações das âncoras são chamadas fora do fluxo, em itens separados, que nunca entram nas estatísticas principais. O orçamento das âncoras (k, ρ) e W governam a latência de deriva do juiz e a corrida; a configuração principal governa o poder contra o sistema; α_judge e α_sys são orçamentos de Bonferroni separados. O veredito ainda acopla os dois pela corrida.

Duas fronteiras ditas logo ali: a construção não afirma otimalidade (a aposta aproxima a ótima em log, e a regra não minimiza o erro de atribuição a orçamento fixo); e supõe que os rótulos humanos continuem uma referência válida.

## O que o texto supõe sobre as âncoras rotuladas por humanos

Reunido do que o artigo afirma em vários pontos:

- Os itens e os rótulos humanos nunca mudam; por isso, só o juiz pode mover a distância (Definição 1, Proposição 2).
- As âncoras são separadas antes do monitoramento e ficam fora de toda calibração do processo principal; as chamadas a elas não entram nas estatísticas principais (Definição 1, Proposição 4).
- Os rótulos humanos seguem sendo uma referência válida. Se o padrão de qualidade das âncoras derivar conceitualmente (o significado de uma rubrica muda, por exemplo), o processo continua acusando corretamente o desacordo juiz contra âncora, mas a leitura disso como deriva do juiz enfraquece, porque o desacordo pode ser "o mundo andando sob uma régua fixa". Uma renovação periódica das âncoras, rerrotulando contra o padrão atual, restabelece a linha de base (seções 4.5 e 6, apêndice A); políticas de renovação com princípio ficam como trabalho futuro.
- O teste é sobre a mudança da distância em relação ao juiz do tempo zero, não sobre o nível de concordância: os rótulos humanos estão em outra escala (HelpSteer2 de 0 a 4 por atributo, TL;DR em Likert de 7 pontos), reescalada para [0, 1], e a distância de base absorve a diferença constante de escala (seção 5.1).
- As âncoras são sorteadas com reposição, e a linha de base é exata porque as notas do juiz do tempo zero ficam em cache (Observação 6).
- A família das âncoras é agregada sobre rubrica e direção, sem dimensão de tema, porque a deriva do juiz é "plausivelmente global"; o custo é menos poder contra uma deriva do juiz restrita a um tema (seção 6).
- O processo das âncoras dispara pelo componente sistemático da mudança do juiz, não pelo ruído item a item, e por isso precisa de cerca de 200 âncoras para a troca de versão sutil (seção 5.3).
- Em cada base há uma rubrica de baixa resolução (verbosidade no HelpSteer2, coerência no TL;DR) com humanos perto do teto e a pior concordância juiz-humano, que o autor atribui ao desenho da rubrica, não ao monitor (seção 5.6).

## Experimentos (seção 5)

Quatro afirmações testadas: a regra separa deriva do juiz e do sistema; o erro de atribuição é uma corrida ajustável por W, taxa e tamanho das âncoras; os dois processos são ortogonais e precisam ser dimensionados juntos; e o e-processo das âncoras supera as alternativas clássicas. Tudo roda em duas bases sem reajuste entre elas (mesmos juízes, configuração, limiares e orçamentos), e o autor trata a segunda base como teste fora da amostra das proposições.

### Montagem (5.1)

- **HelpSteer2:** 1.498 itens, 5 rubricas (helpfulness, correctness, coherence, complexity, verbosity), 6 estratos de tema. **TL;DR (sumarização):** 1.498 itens, 4 eixos (overall, accuracy, coverage, coherence), 5 estratos por subreddit.
- Juiz barato: gemini-3.1-flash-lite; juiz forte: gemini-3.1-pro-preview. Rótulos das âncoras: as notas humanas de cada base.
- Fluxos de 1.200 posições, ponto de mudança na posição 300, média de 60 sementes, α_sys = α_judge = 0,1.
- **Três derivas do juiz:** *real leniente* (todo item reavaliado pelo gemini-3.5-flash, uma troca silenciosa de versão real, uniformemente mais leniente; deslocamento médio por rubrica de +0,022 a +0,072 no HelpSteer2 e de +0,031 a +0,071 no TL;DR); *real severa* (o mesmo modelo com um prompt mais estrito, "v2-strict", que baixa as notas de −0,043 a −0,152 no HelpSteer2, com a verbosidade como exceção em +0,025, e de −0,097 a −0,230 no TL;DR); *sintética* (deslocamento ajustável de −0,25 mais ruído).
- **Deriva do sistema:** depois da mudança, a célula alvo (creative×helpfulness no HelpSteer2, relationships×overall no TL;DR) passa a vir de um conjunto de itens "regredidos e invisíveis" (nota forte baixa, nota barata alta), o ponto cego que torna o juiz barato insuficiente. Cruzando as duas derivas: quatro condições, {none, system, judge, both}.
- **Configuração de destaque:** processo principal com orçamento fixo de 0,3, 200 âncoras intercaladas a 1/5, guarda W = 300. Custa cerca de 0,64 (HelpSteer2) e 0,63 a 0,65 (TL;DR) da avaliação completa. A alternativa "barata mas surda" (escalonamento com π0 = 0,02 e âncoras a 1/20) custa 0,21 mas perde a maior parte das regressões do sistema.

### Separação e detecção (5.2; Tabelas 1 e 2)

- **Tabela 1** (deriva sintética de −0,25, principal fixo em 0,3, W = 50, 60 sementes). Com âncoras dimensionadas (k = 200, 1/5): detecção do sistema 41/60 (HelpSteer2) e 56/60 (TL;DR), igual ao poder do principal; deriva do juiz detectada 60/60 nas duas linhas no HelpSteer2 e 55/60 e 59/60 no TL;DR. No HelpSteer2, nenhuma rodada de juiz ou ambos cai em *system* (0/120); no TL;DR sobra um vazamento de 5 + 1 em 120, que a corrida explica e uma janela maior fecha. Vereditos falsos de juiz: 2/60 sem deriva e 2/60 com deriva só do sistema (cerca de 0,03, abaixo de 0,1). Latência mediana do juiz: 120 (HelpSteer2) e 140 (TL;DR).
- **Âncoras subdimensionadas** (k = 50, 1/20): o principal lê o juiz contaminado tão depressa que dispara cerca de 300 itens antes das âncoras; 48 a 50 das 60 rodadas de deriva do juiz no HelpSteer2 e 54 a 58 no TL;DR caem em *system*, e a separação desaba. Latência do juiz: 420 e 440. A lição de dimensionamento conjunto: a latência das âncoras precisa ficar abaixo da latência de disparo contaminado do principal mais W.
- **Tabela 2** (troca de versão real, leniente, deslocamento médio de até +0,072; principal por escalonamento). A detecção depende do orçamento das âncoras: com k = 50 a 1/20, 7% (4/60) nas duas bases; com k = 150 a 1/8, 62% (37/60) no HelpSteer2 e 38% (23/60) no TL;DR; com k = 200 a 1/5, 100% (60/60) no HelpSteer2 e 83% (50/60) no TL;DR, onde a troca é mais sutil por eixo na célula de destaque. As falhas caem com segurança em *none*. Nenhuma rodada de juiz cai em *system* em nenhum orçamento; alarme falso de juiz de 0/60 a 2/60. Latências: 660, 652 e 498 (HelpSteer2); 810, 516 e 555 (TL;DR). Com o principal fixo em 0,3: 60/60 com latência 498 (HelpSteer2) e 50/60 com 555 (TL;DR), sem nenhuma atribuição errada ao sistema.
- **A ressalva unilateral:** a troca leniente dá notas iguais ou maiores em toda rubrica, e o monitor principal só dispara com queda. Um juiz leniente não consegue empurrar o principal para um alarme de sistema, então o zero de atribuição errada da Tabela 2 é em parte estrutural para essa direção, não só mérito das âncoras. A Tabela 2 mostra detecção de uma troca real sutil; o teste de separação sob contaminação é a mudança severa da seção 5.3. Segundo o autor, as duas demonstrações são necessárias e nenhuma sozinha sustenta a afirmação inteira.

### Uma mudança severa real: contaminação e a corrida da guarda (5.3; Tabelas 3 e 4, Figura 2)

O prompt v2-strict manda o mesmo modelo "reservar 4 para trabalho impecável" e, na dúvida, escolher a nota menor. **Tabela 3** (cerca de 1.496 a 1.498 itens avaliados pelos dois juízes; deslocamento médio, correlação e concordância exata por item):

| Rubrica | Leniente: desloc. | corr | concord. | Severa: desloc. | corr | concord. |
|---|---|---|---|---|---|---|
| HelpSteer2 helpfulness | +0,064 | 0,88 | 63,6% | −0,152 | 0,90 | 45,0% |
| correctness | −0,008 | 0,86 | 70,0% | −0,120 | 0,88 | 55,1% |
| coherence | +0,022 | 0,76 | 82,5% | −0,092 | 0,79 | 62,9% |
| complexity | +0,050 | 0,59 | 72,5% | −0,043 | 0,57 | 77,5% |
| verbosity | +0,072 | 0,46 | 62,6% | +0,025 | 0,60 | 71,0% |
| TL;DR overall | +0,048 | 0,89 | 69,7% | −0,230 | 0,84 | 26,2% |
| accuracy | +0,031 | 0,91 | 84,4% | −0,097 | 0,89 | 65,7% |
| coverage | +0,071 | 0,87 | 65,6% | −0,193 | 0,83 | 31,9% |
| coherence | +0,037 | 0,81 | 78,6% | −0,134 | 0,78 | 51,0% |

A troca leniente tem a mesma assinatura de +0,03 a +0,07 nos dois domínios ("propriedade da troca de versão, não da base"); a severa desce mais no TL;DR, onde os resumos oferecem mais falhas a penalizar. A concordância item a item cai muito mais do que as médias sugerem (exata de 26% a 84%), e as rubricas em que os dois juízes fortes menos concordam (verbosity e complexity, correlação de 0,46 a 0,60) espelham os pontos cegos do próprio juiz barato.

**Tabela 4** (mudança severa real, configuração de destaque, 60 sementes, variando W; vazamento = rodadas de deriva do juiz atribuídas ao sistema, em 120):

| W | linha juiz (none/sys/judge) | linha ambos | vazamento | latência | custo |
|---|---|---|---|---|---|
| HelpSteer2 50 | 0/10/50 | 0/19/41 | 29 | 370 | 0,64 |
| 150 | 0/8/52 | 0/10/50 | 18 | 370 | 0,66–0,67 |
| 300 | 0/3/57 | 0/7/53 | 10 | 370 | 0,68–0,71 |
| TL;DR 50 | 0/3/57 | 0/2/58 | 5 | 205 | 0,63–0,65 |
| 150 | 0/1/59 | 0/0/60 | 1 | 205 | 0,63–0,68 |
| 300 | 0/0/60 | 0/0/60 | 0 | 205 | 0,63–0,73 |

A mudança severa contamina de fato o principal, mas as âncoras viram a grande maioria dos disparos contaminados para o veredito correto, e o vazamento cai monotonicamente com W (29 → 18 → 10 no HelpSteer2; 5 → 1 → 0 no TL;DR), como a Proposição 3 prevê. O TL;DR chega a 240/240 nas duas linhas de deriva com W = 300: o deslocamento maior (overall −0,23) deixa as âncoras mais rápidas (latência mediana 205 contra 370). As linhas *none* e *system* são idênticas em todo W nas duas bases (58/0/2 e 17/41/2; 58/0/2 e 2/56/2): alargar a guarda não custa detecção do sistema nem alarme falso de juiz, só latência de atribuição e um pouco de custo de âncora. A guarda é o terceiro botão, depois do tamanho e da taxa das âncoras, e o mais barato: "compra correção com latência em vez de dólares".

**Figura 2** (uma semente, configuração de destaque, deriva severa real): no HelpSteer2, as âncoras passam do limiar (cerca de 4,61) na posição 735 e o principal contaminado (limiar de cerca de 5,70) só na 1.098; no TL;DR, 370 contra 567. Nos dois casos o disparo principal cai dentro da janela aberta pelo alarme das âncoras, e o veredito é *judge*.

### Dimensionar juntos: poder do principal × taxa das âncoras (5.4; Figura 3)

Cinco configurações do principal contra três taxas de intercalamento (deriva severa real, k = 200, W = 50, 30 sementes), com quatro fatos estruturais:

1. **Ortogonalidade:** a latência do juiz depende só da taxa das âncoras (830, 695 e 430 itens a 1/20, 1/10 e 1/5 no HelpSteer2; 640, 330 e 202 no TL;DR, em todas as configurações do principal), o poder contra o sistema depende só do principal, e o alarme falso de juiz fica plano em cerca de 0,07.
2. **Detectar e atribuir são coisas separadas:** nos pontos com poucas âncoras, detecção do juiz mais vazamento somam cerca de 1; esses pontos não perdem a deriva, rotulam errado.
3. **O vazamento cresce com o poder do principal** a taxa fixa: na coluna 1/5 do HelpSteer2, 0,03 → 0,07 → 0,18 → 0,33 (escalonamento π0 = 0,02, fixo 0,1, 0,2, 0,3). A região viável é uma faixa diagonal, e o orçamento das âncoras tem de crescer junto com o poder do principal, "não ser parafusado depois". No TL;DR, o deslocamento maior deixa as âncoras a 1/5 vencerem até o principal fixo em 0,3 (vazamento de cerca de 0,05), e a faixa fica nas taxas 1/10 a 1/20 (0,42 com fixo 0,3 a 1/10; 0,90 a 1/20).
4. **A guarda é a saída ortogonal:** a varredura da seção 5.3 levou o vazamento do canto do HelpSteer2 de 29 para 10 em 120 com W = 300 (e o do TL;DR de 5 para 0).

### Comparação com detectores clássicos (5.5; Tabela 5, Figura 4)

Mesmo fluxo de âncoras (k = 200, 1/5, 60 sementes):

| Método | Alarme falso | Detecção leniente / severa / sintética | Latência mediana |
|---|---|---|---|
| HelpSteer2 e-processo | 0,03 | 0,97 / 0,97 / 0,97 | 498 / 370 / 120 |
| teste z ingênuo | 0,75 | 0,73 / 0,73 / 0,73 | 130 / 138 / 40 |
| Page-Hinkley calibrado | 0,08 | 0,08 / 0,65 / 1,00 | 555 / 530 / 295 |
| TL;DR e-processo | 0,03 | 0,83 / 1,00 / 1,00 | 555 / 205 / 140 |
| teste z ingênuo | 0,67 | 0,83 / 0,83 / 0,83 | 168 / 72 / 50 |
| Page-Hinkley calibrado | 0,03 | 0,40 / 1,00 / 1,00 | 550 / 248 / 165 |

O teste z ingênuo (janela móvel contra a linha de base, α = 0,05, refeito a cada observação sem correção sequencial, chamado de padrão de mercado) dá alarme falso em 75% e 67% dos fluxos sem deriva, e 16/60 e 10/60 das "detecções" vêm antes da mudança: "a velocidade aparente é a falta de controle de erro". O Page-Hinkley por rubrica e direção, com limiar calibrado em 60 fluxos nulos separados para erro de família de 0,1, é a receita clássica mais forte: segura o alarme falso, mas é quase cego à troca leniente real (8% no HelpSteer2, 40% no TL;DR) e, quando detecta, é mais lento. O e-processo segura o alarme falso em 0,03 sem dados de calibração e com garantia sem horizonte; o 83% na troca leniente do TL;DR é o limite de orçamento das âncoras da Tabela 2, não do método.

### Generalização: todas as células das duas bases (5.6)

- Nas 28 células tema×rubrica executáveis do HelpSteer2 (duas de coherence perto do teto ficam de fora porque o conjunto de itens regredidos e invisíveis fica vazio): detecção do juiz de 1,00 em 27 de 28 (0,97 em factual_qa:coherence), latência de 98 a 128 itens, atribuição errada ao sistema de 0,00 em 27 de 28 (0,03 na mesma célula), alarme falso de juiz até 0,10. No TL;DR, 19 de 20 células: detecção do juiz de 0,85 a 0,97, latência de 118 a 145, atribuição errada até 0,15 com W = 50, alarme falso até 0,10. As propriedades das âncoras independem da célula por construção; só o poder contra o sistema varia (0,00 a 1,00 no HelpSteer2, 0,40 a 1,00 no TL;DR, mais fraco onde o juiz barato é mais generoso), e regressão perdida cai em *none*, nunca em falso *judge*.
- **Leituras entre as bases:** o que devia se repetir se repetiu (a mesma assinatura da troca de versão; uma rubrica de baixa resolução em cada base, com correlação fraca do juiz barato, humanos perto do teto e a pior concordância juiz-humano). O que devia mudar mudou onde a Proposição 3 prevê: a mudança severa é maior nos resumos, e por isso a latência das âncoras cai (205 contra 370), o vazamento zera com W = 300 e a faixa de dimensionamento vai para taxas mais lentas. O poder contra o sistema, que não se esperava que transferisse, é maior no TL;DR (56/60 contra 41/60) porque os quatro eixos são informativos para o juiz barato, ao contrário de complexity e verbosity no HelpSteer2.

## Discussão e limites declarados (seção 6)

- **Âncoras envelhecidas:** a identificação supõe que os rótulos humanos congelados continuem válidos (ver a seção sobre as âncoras acima); a renovação periódica restabelece a linha de base.
- **Família de âncoras agregada:** sem dimensão de tema, por escolha de poder e orçamento (uma família por tema dividiria as k âncoras entre células e multiplicaria o fator de Bonferroni por K). Custo: menos poder contra deriva do juiz localizada, como um juiz que mudou só em itens com muito código.
- **"Ambos" vira "juiz", por projeto:** uma regressão do sistema simultânea não é atribuída. Nas palavras do autor, uma mudança de juiz confirmada suspende a confiança no veredito principal até o juiz ser reancorado.
- **Sem otimalidade:** valida e identifica, não afirma eficiência; as monotonicidades dizem para que lado cada botão move o vazamento, não que os botões estão no ponto ótimo.
- **Poder contra o sistema depende da célula, e o horizonte é único:** é quase zero nas rubricas em que o juiz barato é cego (complexity, verbosity) e nas células de matemática. Os experimentos usam um só horizonte (1.200 posições, mudança em 300) e um modelo de custo representativo que ignora o custo de atribuir tema; as frações de custo são representativas, não universais.
- **O cardápio de custo:** não há preço único. A configuração barata mas surda custa cerca de 0,21 e perde a maior parte das regressões na célula difícil; a de destaque custa cerca de 0,64 e pega a deriva do sistema sem atribuição errada. Da diferença de 0,43, só 0,20 é das âncoras; o resto compra poder do principal.
- **Receita prática, em ordem:** (1) escolher a configuração principal na fronteira custo/poder, o que fixa o poder contra o sistema e a latência de disparo contaminado que as âncoras precisam vencer; (2) dimensionar as âncoras (k e taxa) para que a latência delas, nas magnitudes de deriva que importam, fique abaixo dessa latência; (3) alargar W para absorver o vazamento residual, o botão mais barato, que nunca fabrica um falso veredito de juiz.

## Conclusão e trabalhos futuros (seção 7)

Um conjunto pequeno e fixo de âncoras com rótulos humanos, reavaliado pelo juiz atual e vigiado por um e-processo a mais, separa a deriva do sistema da do juiz num veredito de três estados, com três botões (tamanho das âncoras, taxa de intercalamento, janela de guarda) e a garantia de que a deriva do juiz nunca é cobrada do sistema além de α_judge. Três direções em aberto: políticas de renovação das âncoras que mantenham os rótulos humanos como referência válida conforme os padrões mudam; famílias de âncoras por estrato, para recuperar poder contra deriva do juiz localizada num tema; e regras ótimas de aposta e de atribuição que minimizem o erro de atribuição a orçamento fixo.

## Apêndices

- **A (provas):** detalha as quatro proposições. O teto da aposta é 1/(1 − linha de base) na direção "abaixo" e 1/linha de base na direção "acima"; a desigualdade de Ville dá o limite em qualquer tempo de parada. As monotonicidades da Proposição 3 são argumentos de dominância estocástica, sem acoplamento mais fino. A Observação 8 confirma a ortogonalidade: latência do juiz de 830, 695 e 430 constante nas cinco configurações do principal.
- **B (a base de custo em detalhe; Tabelas 6 a 8):** todos os números na célula helpfulness×creative do HelpSteer2, 60 sementes, α_sys = 0,1. **Tabela 6** (latência mediana / censura / fração de custo / custo sob controle): escalonamento π0 = 0,01 nunca detecta (censura 1,00; 0,142 sob controle); π0 = 0,02: 750 / 0,95 / 0,21 / 0,154; π0 = 0,05: 710 / 0,82 / 0,23 / 0,184; π0 = 0,1: 706 / 0,53 / 0,28 / 0,236; fixo uniforme 0,1: 789 / 0,98 / 0,24 / 0,226; fixo 0,2: cerca de 660 / 0,50 / 0,33 / 0,327; fixo 0,3: cerca de 585 / 0,28 / 0,43 / 0,428; avaliação completa: 327 / 0,02 / 1,00 / 1,125; alarme falso 0,000 em todas. O escalonamento com π0 = 0,1 (custo 0,28, censura 0,53) é quase tão confiável quanto o fixo 0,2 (custo 0,33, censura 0,50) e mais barato, e erra o corte de censura até 0,5 por uma repetição. A deriva é difícil (até a avaliação completa censura 2%). **Tabela 7** lista dez métodos em cinco grupos (só barato: o mesmo e-processo, Page-Hinkley e Shiryaev-Roberts sobre a nota barata; só rótulo; PPI global; PPI por estrato com orçamento fixo, gatilho por covariável, a regra do apêndice B.2 de Csillag e o escalonamento do autor; e a avaliação completa), todos com o mesmo teto de aposta. Na grade de 5 níveis do HelpSteer2, as quatro intensidades de deriva colapsam em duas: severa (um só item extremo) e leve (o mesmo conjunto de 21 itens). **Tabela 8:** o gatilho por fronteira detecta sempre, mas com custo de cerca de 0,87 a 0,88; a regra de Csillag fica inerte porque o juiz barato superestima toda barra saudável (helpfulness −0,18, complexity −0,23, verbosity −0,27 na diferença barra menos nota barata) e degenera em orçamento fixo a π0 (fraca na severa, censura de 0,80 com π0 = 0,1; falha na leve, censura de 0,95 ou mais); o orçamento fixo censura 0,12 a 0,2 e 0,05 a 0,3 na severa; o escalonamento detecta na severa com censura de 0,22 a custo 0,28 e, na leve, empata com o fixo 0,2 (0,53 a custo 0,28 contra 0,50 a 0,33). O autor relata o empate como está. Estratificar é decisivo: censura do PPI global contra o estratificado de 0,68 contra 0,12 (severa, 0,2) e 0,58 contra 0,05 (severa, 0,3); na leve, o global censura 1,00 em todos os orçamentos e o estratificado detecta a 0,2 (0,50) e 0,3 (0,27). Os detectores clássicos não transferem: calibrados em sementes nulas separadas, fora dessa amostra o Page-Hinkley tem alarme falso de 0,117 e o Shiryaev-Roberts de 0,267, enquanto os e-processos ficam em até 0,017. Os métodos só com nota barata censuram perto de 1,0 em tudo.
- **C (todas as células; Tabela 9):** configuração de destaque, W = 50, deriva sintética de −0,25, 20 sementes, HelpSteer2. Detecção do sistema de 0,80 a 1,00 nas células de correctness e coherence, de 0,45 a 0,95 em helpfulness, perto de zero em complexity e verbosity e em todas as de matemática. No TL;DR, a detecção do sistema vai de 0,40 a 1,00, mais fraca em coverage.
- **D (calibração do juiz barato; Tabela 10):** correção nota barata → nota forte ajustada nos primeiros 600 itens do HelpSteer2 e medida nos 600 seguintes. Viés (barato menos forte), correlação, inclinação afim e redução do erro quadrático: helpfulness +0,13, 0,81, 0,87, −19% ("informativo, só generoso"); correctness +0,01, 0,81, 0,80, −6% ("já preciso, não corrigir"); coherence −0,02, 0,63, 0,60, −16% ("acompanha"); complexity +0,16, 0,54, 0,40, −54% ("enviesado mas corrigível"); verbosity +0,22, 0,23, 0,28, −49% ("cego"). As correções transferem sem sobreajuste, e um simples deslocamento já tira a maior parte do erro. A conclusão do autor: calibrar tira a generosidade sistemática do juiz barato, mas não cria resolução que ele nunca teve; a verbosidade é a rubrica onde se esconde a deriva localizada do apêndice B e onde aparece a maior diferença entre versões do juiz da Tabela 3.
- **E (prompts):** juiz forte e barato usam o mesmo prompt, mudando só o modelo. A troca de versão real não muda prompt; a mudança severa usa o mesmo modelo com um prompt deliberadamente mais estrito, que acrescenta "cético", "reserve 4 para trabalho impecável", "penalize todo erro, omissão ou afirmação sem suporte" e, entre duas notas vizinhas, "escolha sempre a menor". Três itens do HelpSteer2 e um do TL;DR que o juiz forte não avalia (filtro de conteúdo) voltam à nota sem deriva.
- **F (reprodutibilidade):** uma camada de dados paga, feita uma vez (cache das notas do Gemini), e experimentos só de computação a partir dela. Os artefatos não vão para o repositório; recolher notas de uma versão posterior do juiz daria números diferentes, "o que é exatamente o ponto do artigo". Licenças: HelpSteer2 em CC BY 4.0 (NVIDIA), os dados de feedback de sumarização da OpenAI em MIT modificada, o corpus Webis TLDR em CC BY 4.0; o artefato redistribui só notas derivadas e rótulos humanos, sem o texto bruto.

---
