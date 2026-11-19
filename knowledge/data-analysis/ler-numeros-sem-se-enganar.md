# Ler números sem se enganar: armadilhas, cautelas e conferência

O que os plugins **data** e **small-business** da Anthropic ensinam sobre ler um número antes de escrever uma frase com ele: as armadilhas que fazem a conta certa dizer a coisa errada, as cautelas ao afirmar, a conferência antes de entregar, o veredito e o molde de definição de métrica. As fontes vêm da cópia local dos plugins, sem pesquisa nova.

**O que esta página é.** Um repertório de ofício organizado: as fontes são instruções escritas para assistentes, sem estudo, autor nem medição por trás. Nenhuma regra aqui foi testada neste projeto, e os números que as fontes trazem estão separados na seção 9. "Leitura nossa" marca o que liga as fontes ou as traz para cá e não está nelas.

**As fichas e os apelidos:** Validar, [[2026-11-10-anthropic-plugin-data-validate-data]]; Estatística, [[2026-11-10-anthropic-plugin-data-statistical-analysis]]; Explorar, [[2026-11-10-anthropic-plugin-data-explore-data]]; Molde, [[2026-11-10-anthropic-plugin-data-context-extractor]] (as quatro do plugin data, Apache 2.0, com o texto integral ou os trechos na ficha); Ausente, [[2026-11-10-anthropic-plugin-small-business-ausente-denominador-e-fuso]]; Relatório, [[2026-11-10-anthropic-plugin-small-business-relatorio-e-leitura]] (as duas do small-business, sem licença declarada, só a ficha).

## 1. A resposta curta

- **O erro de que estas fontes tratam não é de conta, é de leitura** (*leitura nossa*, juntando as fichas): o número está certo no lugar de onde saiu e é lido como se dissesse outra coisa. Um buraco no dado lido como fato e um total de um universo usado em outro (Ausente); um período parcial posto ao lado de um cheio (Validar; Relatório). A ficha Ausente diz que o primeiro é o jeito mais comum de as skills daquele plugin errarem, sem contagem que sustente, e dá o motivo de ninguém conferir: para ela, o buraco se lê como boa notícia.
- **Seis armadilhas** foram escolhidas para esta página (a escolha é desta página, não das fontes; o catálogo de Validar tem sete, com outras só nomeadas): período parcial contra cheio, denominador que muda, média de médias, fuso, segmento definido pelo resultado e ausente tratado como zero (seção 3).
- **Seis cautelas** valem ao afirmar: média e mediana juntas, amostra pequena dita, quantos recortes foram olhados, faixa em vez de ponto, tamanho do efeito e outlier investigado (seção 4).
- **Antes de entregar,** a mesma métrica por dois caminhos, as partes somando o todo, e um veredito em três níveis (seções 5 e 6).
- **Antes de tudo,** a métrica tem definição escrita: nome, definição, fórmula, origem e ressalvas (seção 7).

## 2. Antes da conta: o que o dado é

- **O grão:** uma linha é o quê? Sem isso, não se sabe o que uma soma ou uma média está contando. Junto vão a chave e se ela é única, a data da última atualização e até onde o dado volta (Explorar).
- **A completude:** quanto de cada campo veio preenchido, e por que o resto não veio (Explorar). O vazio se trata de forma declarada: excluído, preenchido ou marcado (Validar).
- **O dado suspeito:** valor de marcador no lugar do dado (0, -1, "N/A"), o mesmo valor com frequência demais, valor impossível (data no futuro, porcentagem acima de 100), número sempre redondo, duplicata, campos que se contradizem, série com buraco (Explorar).
- **A data de referência** de cada fonte vai anotada, e o período da análise leva início, fim e fuso (Validar).

## 3. As seis armadilhas

| Armadilha | Como aparece | Como se evita | Fonte |
|---|---|---|---|
| **Período parcial contra cheio** | o mês ou a semana em andamento ao lado do período anterior inteiro parece queda | comparar só períodos completos, ou o mesmo número de dias, e escrever "até o dia tal"; e comparar o mesmo ponto do ciclo (semana contra semana no mesmo dia da semana), para não tomar sazonalidade por tendência | Validar; Relatório; Estatística |
| **Denominador que muda** | a taxa muda porque mudou a definição de quem entra na base, não o comportamento; ou o total de um universo vira a base de uma taxa de um universo menor | mesma definição em todos os períodos, mudança anotada; a taxa contra a base que aquilo consegue alcançar, com a parte e o todo ditos | Validar; Ausente |
| **Média de médias** | tirar a média de médias prontas, com grupos de tamanhos diferentes | agregar do dado bruto, ou ponderar pelo tamanho de cada grupo | Validar |
| **Fuso** | carimbo em UTC ao lado de data local; cortes diários em horas diferentes; rótulo de fuso que contradiz o deslocamento gravado | levar tudo a um fuso só e dizer qual; vale o deslocamento do horário, não os dígitos; sinais que discordam se dizem | Validar; Ausente |
| **Segmento definido pelo resultado** | o grupo é formado pelo próprio desfecho que se mede, e a comparação é circular | definir o grupo por algo anterior ao que se mede | Validar |
| **Ausente tratado como zero** | campo vazio, 0 de marcador, busca que não achou ou fatia paginada lidos como fato | perguntar o que faria o número aparecer assim se o dado estivesse quebrado; não dando para separar, dizer | Ausente; Explorar (o 0 entre os marcadores); Relatório |

**Sobre a última.** A regra já existe no projeto e não se repete aqui: "ausente não é zero", com o porquê em [`decisions/dado-de-fora.md`](../../decisions/dado-de-fora.md), e já cobre a fatia paginada, o resumo no lugar da fonte, o vazio que tem a mesma cara da consulta que falhou e as duas contagens que divergem. O que a ficha Ausente traz e a regra não tem: o zero implausível, que se lê como desconhecido; o registro sem data, que é o caso mais preocupante e não o mais recente; e a data posterior a hoje, que é defeito e sobe ao topo de uma ordenação por recência. A ficha Relatório traz o caminho inverso: o grupo que não teve movimento continua na tabela, com zero e uma nota, em vez de sumir.

**Sobre o fuso** (*leitura nossa*). As fontes não dizem a mesma coisa: Validar recomenda levar tudo a UTC antes de analisar; Ausente manda converter para o fuso de quem lê quando a hora sai para alguém. As duas se conciliam separando a conta do texto: um fuso só, declarado, na conta; o fuso do leitor, escrito, na frase.

**Vizinhas das seis, que esta página só nomeia (o desenvolvimento está nas fichas):** contagem dupla (a mesma coisa somada de duas fontes, ou a linha de total contada junto com as linhas de item, em Relatório; a junção que multiplica linhas e o registro duplicado, em Validar), viés de sobrevivência (quem não está no conjunto?), paradoxo de Simpson (a tendência do agregado se inverte nos segmentos quando a mistura muda), correlação dita como causa, e janela de tempo escolhida para favorecer a história (Validar; Estatística).

## 4. As seis cautelas ao afirmar

- **Média e mediana juntas.** Se as duas divergem muito, a distribuição é assimétrica e a média sozinha engana; a distância entre elas é a informação. Percentis contam mais que a média quando poucos valores puxam o total (Estatística).
- **Amostra pequena se diz no texto,** com o que ela não permite concluir. Resultado de amostra pequena é pouco confiável mesmo quando parece nítido (Estatística).
- **Comparações múltiplas.** Olhando muitos recortes, algum sai diferente por acaso. Se vários segmentos foram olhados até aparecer um que destoa, a leitura diz quantos foram (Estatística).
- **Faixa em vez de ponto.** Número com casas decimais sugere uma certeza que não existe; previsão e estimativa saem como faixa, com arredondamento honesto (Estatística).
- **Tamanho do efeito.** Dizer de quanto é a diferença e o que ela vale na prática, não só que existe. Com muitos dados, uma diferença pode ser real e irrelevante (Estatística).
- **Outlier investigado e relatado.** Não se remove de forma automática: primeiro saber se é erro de dado, extremo verdadeiro ou outra população; depois dizer o que foi feito, com quantos casos e por quê (Estatística).

## 5. Conferir antes de entregar

- **Dois caminhos.** Calcular a mesma métrica de duas formas e ver se batem. As outras técnicas da mesma família: seguir à mão alguns registros; comparar com uma referência conhecida; fazer a conta inversa (o valor por unidade vezes o número de unidades dá perto do total?); e testar a borda (um dia só, um item só: o resultado miúdo faz sentido?) (Validar).
- **As partes somam o todo.** Somar antes de entregar; se não fecham, dizer o tamanho da diferença e a causa (Validar; Relatório).
- **Sinais que pedem investigação:** mudança grande de um período para o outro sem causa clara; taxa exatamente em 0% ou em 100%; total em número redondo exato; valores idênticos entre períodos ou segmentos; resultado que confirma a hipótese com perfeição (Validar); e razão que sai uma ordem de grandeza melhor que o razoável, que manda olhar o denominador (Ausente).
- **Nunca o número plausível no lugar do que faltou:** não se estima, não se arredonda na direção de um palpite e não se repete o valor do período anterior em silêncio; sai "indisponível", com o motivo (Relatório).

## 6. O veredito em três níveis

Da ficha Validar, para a revisão de uma análise antes de ela chegar a quem decide:

1. **Pronta para compartilhar:** método sólido, contas conferidas, ressalvas ditas.
2. **Compartilhar com ressalvas:** certa no geral, com limites que precisam ir junto; a lista das ressalvas obrigatórias acompanha.
3. **Precisa de revisão:** erro, problema de método ou análise que falta; a lista do que mudar vem em ordem de prioridade.

*Leitura nossa:* o nível do meio é o que mais serve a uma leitura de métricas de conta pequena (dez posts por mês, alcance de poucas centenas a poucos milhares), em que quase tudo vem com amostra curta; ele obriga a escrever a ressalva em vez de calar o número ou soltá-lo sem aviso.

## 7. O molde de definição de métrica

Cinco campos por métrica (Molde): **nome** (como as pessoas a chamam), **definição** (em linguagem simples), **fórmula** (a conta exata, com os campos que entram), **origem** (de onde o dado vem) e **ressalvas** (casos de borda, exclusões, armadilhas). A skill de onde o molde vem tira esse conhecimento de quem usa o dado com perguntas que servem aqui também: quando se diz "usuário" ou "cliente", o que exatamente se quer dizer e se há mais de um tipo (a única que a fonte marca como crítica); como cada métrica é calculada e com que convenção de período; o que sempre se tira antes de contar; e que engano quem chega costuma cometer.

O relatório recorrente tem o seu próprio molde, salvo antes de puxar o dado (Relatório): nome, cadência, período, comparação, agrupamento, as métricas com fórmula e fonte, as fontes e as notas. Quatro regras o mantêm honesto: toda métrica diz a fonte, a fórmula vem por extenso, a ambiguidade resolvida fica anotada com a resposta de quem pediu, e cada relatório tem um propósito só.

## 8. Escrever a leitura

Da ficha Relatório: abrir pela frase que explica o período, não pela tabela; o número antes da palavra; todo número com a sua comparação; nomear o item (qual peça, qual canal); sem vocabulário que quem lê não usa; três ações no fim (a fonte diz exatamente três), cada uma com o número que a justifica; e "sem mudança relevante" ou "nada precisa mudar" como respostas válidas, porque a leitura que fabrica ação toda semana ensina a ignorá-las. Como contar a história com o dado já conferido é outro assunto, em [[storytelling-com-dados]].

## 9. Números das fontes, sem medição daqui

Nenhuma fonte diz de onde estes números vêm. Entram como **número da fonte**: servem de ponto de partida para uma conversa, não de limiar para adotar.

| Número | Onde | O que é |
|---|---|---|
| pelo menos 30 eventos por grupo, em proporções | Estatística | regra de bolso, dita assim pela fonte |
| mudança acima de 50% de um período para o outro | Validar | sinal de alerta |
| nível de significância de 0,05 | Estatística | convenção |
| 3 desvios padrão; 1,5 vez o intervalo interquartil; percentis 1 e 99 | Estatística | convenções para marcar outlier |
| média móvel de 7 e de 28 dias | Estatística | janelas sugeridas |
| vazio acima de 5% (aviso) e de 20% (alerta); faixas de completude em 99%, 95% e 80% | Explorar | cortes sugeridos |
| exatamente três ações por leitura | Relatório | regra de formato |

Os valores dos exemplos das fontes (dólares, porcentagens de cenário) são ilustração e não se carregam.

## 10. Onde isso se usa

*Leitura nossa,* a seção inteira: as fontes não falam destes usos. Tudo por referência; cada ponto se confere no caso antes de adotar.

- **Métricas de redes sociais:** as leituras de 24 horas e de 7 dias de Stories e posts e o relatório semanal são onde as seções 3 a 8 cabem. Um exemplo genérico: um post com alcance de 1.200 contra a mediana de 800 dos últimos dez posts parece um salto de 50%; antes de dizer isso, conferir se os dez tiveram o mesmo tempo de vida (período parcial), se o alcance de todos veio da mesma métrica (denominador), se a mediana e a média contam a mesma história (um post viral puxa a média) e se dez casos permitem dizer "acima do normal" ou só "acima dos últimos dez". O que a base sabe sobre o que prediz desempenho, com o tamanho da amostra de cada benchmark, está em [[o-que-prediz-desempenho-instagram]].
- **Números de pesquisa:** ao levar um número de fonte externa para uma síntese ou pauta, cabem as seções 4 e 5; avaliar a fonte em si é de [[avaliar-fonte-e-parar-a-busca]], e os problemas dos próprios dados como história, de [[apuracao-investigativa]] (os tipos de Bradshaw).
- **Medidas de avaliador (modelo de decisão, juiz, portão):** amostra pequena, limiar e reuso do teste têm tratamento próprio e com fonte primária em [[ponto-de-corte-reuso-do-teste-e-desvio]] e [[desenho-de-rubrica-e-veredito]]; esta página não os substitui.
- **As armadilhas mais prováveis numa conta pequena:** o período parcial (a peça com menos dias de vida ao lado de uma mais velha, a semana em curso contra a anterior, peças publicadas em dias diferentes da semana); o denominador (alcance, contas alcançadas e impressões se confundem, e a taxa muda com a base escolhida: 30 salvamentos sobre 1.200 contas alcançadas não é a mesma taxa que 30 sobre 2.000 impressões); o fuso (a plataforma grava em UTC, e a contagem diária pode ser alinhada à meia-noite local; o que cada leitura faz com a hora se confere nela); e o campo que a API não devolve lido como zero.

## 11. Limites e o que falta

- **Sem fonte primária.** Tudo vem de dois plugins de um mesmo autor, escritos para assistentes; nenhuma regra traz estudo. As regras de estatística são repertório comum e têm literatura própria, que a base ainda não tem. É lacuna para uma pesquisa futura, não coisa a buscar por esta página.
- **O contexto das fontes é outro:** empresa com banco de dados, livros contábeis e loja virtual, valores em dólar. Teste de hipótese formal, junção de tabelas e previsão ficaram nas fichas e fora desta página; se servem a métricas de redes sociais é pergunta para o dado de cada projeto.
- **Duas skills do mesmo recorte não entraram:** os mesmos plugins trazem também `marketing-monday`, do small-business (número de plataforma é alegação da plataforma e não se soma ao de outra fonte), e `performance-report`, do plugin marketing (regras de teste e de tendência). Não entraram nesta ingestão; a primeira regra é do assunto, porque as métricas de uma rede social vêm todas da plataforma.
- **O plugin small-business não declara licença:** as duas fichas são em palavras próprias, e o original só existe na cópia local do plugin. Se a cópia se perder, não há como reconferir.
- **Nada foi medido aqui.** A seção 10 diz onde as regras caberiam; se cabem, e com que limiares, é decisão a tomar com o dado de cada projeto.
