---
titulo: "statistical-analysis: estatística descritiva, tendência, outlier, teste de hipótese e quando desconfiar (skill do plugin data da Anthropic, versão 1.1.0)"
tipo: instrumento
autor: "Anthropic"
publicado_em: 2026-09-29   # data de atualização do plugin no manifest.json da cópia local; a skill não traz data própria
capturado_em: 2026-11-10
licenca: "Apache 2.0 (arquivo LICENSE na raiz da pasta do plugin data: o texto padrão da licença, versão 2.0, de janeiro de 2004; a linha de copyright do apêndice está no modelo, 'Copyright [yyyy] [name of copyright owner]', e a pasta não tem arquivo NOTICE; o autor declarado em .claude-plugin/plugin.json é Anthropic). Texto da licença: http://www.apache.org/licenses/LICENSE-2.0"
areas: [data-analysis]
tags: [statistics, descriptive-statistics, outliers, hypothesis-testing, sample-size, multiple-comparisons, effect-size, uncertainty]
---

# statistical-analysis: como descrever um número e quando desconfiar da afirmação

Ficha de estudo, em palavras próprias, da skill `statistical-analysis` do plugin **data** da Anthropic (versão 1.1.0), sem o texto integral, que está no próprio plugin.

**Proveniência.** Não há url: o plugin veio sincronizado da conta do claude.ai (catálogo `anthropic-plugin-directory`) e foi desligado em 2026-11-10. Os números de linha citados abaixo são os dessa cópia.

**O que a fonte é e o que não é.** É uma instrução para um assistente que analisa dados de negócio, escrita para analista, não para estatístico: ela mesma manda passar adiante o que for tendência não linear, sazonalidade múltipla ou previsão que decide recurso (linha 107). Não cita estudo nem livro; as regras são o repertório comum de estatística aplicada, e os limiares que traz não têm lastro na própria fonte (seção no fim desta ficha).

## Descrever um número (linhas 11 a 58)

- **Que medida de centro usar:** média quando a distribuição é simétrica e sem outlier; mediana quando é assimétrica; moda para dado categórico; e, na assimetria forte com outlier (receita por pessoa, por exemplo), mediana e média juntas, porque a distância entre as duas mostra a assimetria.
- **A regra que a fonte destaca (linha 24):** em métrica de negócio, dizer sempre média e mediana juntas; se divergem muito, o dado é assimétrico e a média sozinha engana.
- **Espalhamento:** desvio padrão para dado perto da normal; intervalo interquartil (do percentil 25 ao 75) para dado assimétrico, porque resiste a outlier; coeficiente de variação (desvio dividido pela média) para comparar métricas de escalas diferentes; amplitude (máximo menos mínimo) para uma noção rápida, sensível a outlier.
- **Percentis contam mais que a média:** p50 é a pessoa típica, p90 os 10% de cima, p99 o extremo. O exemplo da fonte: mediana de 4,2 minutos por sessão, os 10% de cima acima de 22 minutos, e a média puxada para 7,8.
- **Toda distribuição se descreve por cinco coisas:** forma (normal, assimétrica à direita ou à esquerda, bimodal, uniforme, de cauda pesada), centro (média, mediana e a distância entre elas), espalhamento, outliers (quantos e quão extremos) e limites naturais (piso em zero, teto em 100%).

## Tendência e previsão (linhas 60 a 107)

- **Média móvel para alisar o ruído:** a de 7 dias serve ao dado diário com padrão semanal; a de 28 alisa o semanal e o mensal.
- **Comparar período com período:** semana contra semana no mesmo dia da semana, mês contra mês, ano contra ano (que a fonte chama de padrão-ouro para negócio sazonal).
- **Taxa de crescimento:** a simples (atual menos anterior, dividido pelo anterior), a composta anual, e a logarítmica para série volátil.
- **Sazonalidade:** olhar o gráfico da série bruta primeiro; tirar a média por dia da semana e por mês do ano; e, ao comparar períodos, usar o mesmo período do ciclo, para não confundir tendência com sazonalidade.
- **Previsão simples:** amanhã igual a hoje como linha de base; igual ao mesmo dia da semana ou do ano anterior; reta ajustada só quando a tendência é claramente linear; a média móvel como previsão.
- **Dizer a incerteza:** dar faixa, não ponto. "De 10 a 12 mil inscrições no mês que vem, pela tendência de três meses", e não "exatamente 11.234".

## Outlier e anomalia (linhas 109 a 153)

- **Três jeitos de achar:** distância da média em desvios padrão (para dado perto da normal); a cerca do intervalo interquartil (resiste a dado não normal); e o corte por percentis extremos (o mais simples).
- **Não remover outlier automaticamente (linhas 135 a 144).** Primeiro investigar o que ele é: erro de dado (corrige-se ou tira-se), extremo verdadeiro (fica, e vale usar estatística robusta, como a mediana) ou outra população (separa-se para análise à parte). E relatar o que foi feito, com quantos registros, que fração e por quê.
- **Em série temporal:** calcular o valor esperado (média móvel ou o mesmo período do ano anterior), medir o desvio em relação a ele, marcar o que passa de um limiar, e separar a anomalia pontual (um valor estranho) da mudança de patamar (deslocamento que se mantém).

## Teste de hipótese (linhas 155 a 200)

- **Para quê:** decidir se uma diferença observada é real ou pode ser acaso (teste A/B, antes e depois, comparação entre segmentos). O roteiro: hipótese nula (não há diferença), hipótese alternativa, nível de significância, estatística e valor-p, interpretação.
- **Que teste em que caso:** duas médias em dado normal, teste t; duas proporções, teste z; medidas pareadas (antes e depois na mesma entidade), t pareado; três ou mais médias, ANOVA; dado não normal em dois grupos, Mann-Whitney; associação entre duas categorias, qui-quadrado.
- **Significância estatística não é importância prática (linhas 184 a 193).** A primeira diz que a diferença dificilmente é acaso; a segunda, que ela é grande o bastante para mudar uma decisão. Com amostra grande, uma diferença pode ser significativa e irrelevante. Dizer sempre o tamanho do efeito (de quanto é a diferença), o intervalo de confiança (a faixa plausível do efeito verdadeiro) e o que isso vale em termos do negócio.
- **Tamanho da amostra (linhas 195 a 200).** Amostra pequena dá resultado pouco confiável mesmo com valor-p significativo; efeito pequeno pede milhares de observações por grupo; e, se a amostra é pequena, isso se diz no texto, com o que ela não permite detectar.

## Quando desconfiar da afirmação (linhas 202 a 245)

- **Correlação não é causa.** Considerar em voz alta a causa inversa, a terceira variável que causa as duas, e a coincidência (com variáveis bastantes, correlação espúria é certa). Pode-se dizer "quem usa X retém 30% mais"; não se pode dizer, sem mais evidência, que X causa a retenção.
- **Comparações múltiplas (linhas 214 a 219).** Testando muitas hipóteses, algumas dão "significativas" por acaso. Se muitos segmentos foram olhados até aparecer um diferente, isso se diz. A saída: dividir o nível de significância pelo número de testes (correção de Bonferroni) ou relatar quantos testes foram feitos.
- **Paradoxo de Simpson.** A tendência do agregado pode se inverter nos segmentos: a conversão geral sobe enquanto cai em todos os segmentos, porque a mistura mudou para o segmento que converte mais. Conferir se a conclusão vale nos segmentos principais.
- **Viés de sobrevivência.** Só se analisa o que sobrou no conjunto; perguntar quem falta e se a presença dele mudaria a conclusão.
- **Falácia ecológica.** O que vale para o grupo não vale necessariamente para o indivíduo.
- **Ancorar em número exato (linhas 240 a 245).** "4,73%" sugere mais certeza do que existe; preferir a faixa ("entre 4% e 6%, pelo histórico") e arredondar com honestidade ("cerca de 5%").

## Números da fonte, sem lastro

A fonte não diz de onde vêm; entram aqui como número da fonte, sem medição própria nem referência.

- **Pelo menos 30 eventos por grupo** para confiabilidade básica em proporções (linha 198), apresentado pela própria fonte como regra de bolso.
- **Nível de significância de 0,05** como o usual (linha 169). O exemplo que a fonte dá para as comparações múltiplas: testar 20 métricas a 0,05 dá cerca de 1 falsamente significativa (linha 217).
- **Limiares de outlier:** mais de 3 desvios padrão; 1,5 vez o intervalo interquartil além dos quartis; abaixo do percentil 1 ou acima do 99; em série temporal, 2 a 3 desvios padrão dos resíduos (linhas 113 a 153). São convenções de uso corrente, sem referência na fonte.
- **Janelas de 7 e de 28 dias** para a média móvel (linhas 64 a 71).
- Os valores dos exemplos (4,2, 22 e 7,8 minutos; 47 registros, 0,3%; 200 observações por grupo; 0,3 ponto percentual) são ilustrativos.
