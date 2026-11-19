---
titulo: "Are Severe Problems Uncovered Earlier in Usability Tests? (Jeff Sauro, MeasuringU)"
tipo: artigo
autor: "Jeff Sauro (MeasuringU, blog da empresa dele)"
url: "https://measuringu.com/severe-frequent/"
publicado_em: 2013-10-30
capturado_em: 2026-11-04
areas: [agent-engineering]
tags: [severity-rating, problem-frequency, usability-testing, sample-size, inter-rater, rating-bias]
licenca: "sem nota de licença no texto lido; post de blog de empresa, protegido; só a ficha"
---

# Sauro (2013): gravidade e frequência de problemas de usabilidade não se correlacionam

Ficha em palavras próprias de um post de blog da MeasuringU (empresa do autor), lido no HTML em 2026-11-04. Não é artigo revisado por pares. O texto integral não entra. O post admite um viés de método que a ficha registra abaixo.

## A pergunta

Se um teste de usabilidade tem poucos usuários (5 a 10), esses primeiros usuários tendem a revelar os problemas mais graves? Isso só vale se frequência e gravidade do problema forem correlacionadas. Que poucos usuários achem os problemas mais frequentes o autor trata como quase tautologia de probabilidade.

## O que havia antes

- Virzi (estudos de 1990 e 1992): correlação positiva entre gravidade e frequência (r = 0,463); quase todos os problemas de gravidade alta apareciam nos 5 primeiros participantes.
- Lewis (1994): 15 participantes em tarefas de software de produtividade; correlação sem significância (r = 0,06); recomendou tratar gravidade e frequência como independentes.
- Law e Hvannberg (2004): resultado alinhado a Lewis, sem correlação. O autor diz ter achado só esses estudos sobre o tema.

## O estudo do post

- Nove testes de usabilidade em sites e aplicativos móveis (comércio eletrônico, site de material esportivo, app de iPhone e iPad de uma operadora de TV a cabo, e-commerce em tablet), com sessões presenciais e remotas moderadas.
- Entre 2 e 4 avaliadores, de forma independente, deram a gravidade de cada problema numa escala de 3 níveis com definição (1 menor, 2 moderado, 3 crítico). As notas foram tiradas em média por problema (exemplo do post: um problema recebeu 2 de um avaliador e 1 de outro, que não tinha assistido às sessões, e ficou com 1,5) e a média foi correlacionada com a frequência do problema (correlações policóricas, com transformação de Fisher na hora de tirar a média entre estudos).

Tabela do post (usuários, avaliadores, problemas, correlação): estudo 1: 17, 4, 75, 0,09; estudo 2: 12, 3, 37, 0,25; estudo 3: 7, 4, 36, 0,27; estudo 4: 7, 2, 24, -0,12; estudo 5: 5, 2, 25, -0,39; estudo 6: 5, 2, 32, 0,22; estudo 7: 6, 2, 37, -0,38 (significativa); estudo 8: 20, 2, 29, 0,47 (significativa); estudo 9: 20, 2, 36, -0,05. Média: r = 0,056, não diferente de zero. Dos dois estudos significativos, um é negativo: no estudo 7, problemas menos graves ocorreram mais do que os críticos.

## Limites que o próprio post reconhece

- **Quem deu as notas conhecia os dados.** O viés corre a favor de achar correlação positiva. Em cada estudo, quem tinha conduzido as sessões como facilitador estava entre os avaliadores e podia lembrar quais problemas se repetiam; e os outros, todos do laboratório da empresa, também tinham alguma noção dessa frequência, mesmo sem ter facilitado.
- **Teste de mitigação no estudo 8.** Foi o estudo de correlação mais alta (0,47) que o autor submeteu a alguém de fora: com as descrições dos 29 problemas e a escala, as mesmas dadas aos dois avaliadores originais, um avaliador independente, com décadas de experiência, chegou a 0,21, valor ainda positivo, mas sem diferença significativa de zero.
- **Gravidade e frequência se misturam na percepção:** para o autor, o efeito pesa na medida da correlação e provavelmente faz pouco estrago no uso prático: quando muitos usuários tropeçam no mesmo problema, ele passa a parecer crítico, ainda que mexa pouco com a experiência.
- **Notas de gravidade são inconsistentes:** num estudo, os mesmos avaliadores refizeram as notas após dois dias e a correlação entre as duas rodadas (intra-avaliador) foi de cerca de 0,5. O autor lê isso como inconfiabilidade inerente à tarefa e é uma das razões de recomendar tirar a média entre avaliadores.

## Conclusões e recomendações do autor

- **O que muda para o teste com poucos usuários:** os 5 primeiros não têm chance maior de topar com os problemas críticos, consequência de não haver correlação nos nove estudos (a evidência de que o grave aparece menos é tão forte quanto a de que aparece mais). Nem por isso a amostra pequena perde o valor, já que continua pegando os problemas frequentes.
- **O que esperar nos próprios dados:** com os vieses de quem dá a nota e a mistura de frequência e gravidade, uma correlação positiva não deveria espantar ninguém; o que surpreendeu o autor foi a maioria dos estudos não mostrá-la.
- **Quem dá a nota:** a saída do autor contra o viés é juntar ao facilitador pelo menos mais um avaliador e ficar com a média das notas. Tirar o facilitador da tarefa, que seria o teste limpo, não serve na prática: quem não viu as sessões custa a entender até a descrição de problema mais bem escrita.
- **Para depois:** estudos futuros poderiam medir o efeito de métodos de nota mais confiáveis.

## O que a fonte não diz

Não dá o coeficiente de concordância entre os avaliadores de cada estudo (só a correlação intra-avaliador, aproximada, num estudo), não diz em que estudo foi feita a repetição com intervalo de dois dias, não descreve as definições dos três níveis da escala nem quais avaliadores aplicaram a escala em cada estudo.
