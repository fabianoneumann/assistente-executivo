---
titulo: "Evidence of bias and variation in diagnostic accuracy studies"
tipo: paper
autor: "Anne W. S. Rutjes, Johannes B. Reitsma, Marcello Di Nisio, Nynke Smidt, Jeroen C. van Rijn, Patrick M. M. Bossuyt"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC1373751/"
publicado_em: 2006-02-14
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [diagnostic-accuracy, spectrum-bias, case-control, study-design, meta-epidemiology, relative-diagnostic-odds-ratio, differential-verification, reporting-quality]
licenca: "PMC, sem licença aberta na página (a página traz © 2006 CMA Media Inc. ou seus licenciadores); entra só a ficha, e o integral está na url (PMC1373751)"
---

# Rutjes et al. 2006 (CMAJ): o que o desenho do estudo faz com a acurácia estimada de um teste

Ficha em palavras próprias. Rutjes e colegas, Canadian Medical Association Journal, 2006, 174(4):469-476, DOI 10.1503/cmaj.050090, PMID 16477057; epidemiologia clínica, com autores da Universidade de Amsterdã, da Universidade Gabriele D'Annunzio (Chieti-Pescara) e do VU University Medical Center. Estudo meta-epidemiológico: em vez de avaliar um teste, compara entre si estudos do mesmo teste, com e sem certo defeito de desenho. O integral não entra: está na url. Lida no texto do PMC em 2026-11-06, e as tabelas, a figura 1, a figura 2 e os apêndices 2, 3 e 4 nas imagens da mesma página, porque lá são imagem.

## A pergunta

Estudos com defeito de método podem superestimar a acurácia de um teste médico. Os autores querem a direção e o tamanho do efeito de 15 características de desenho sobre a estimativa de acurácia, e a importância relativa delas. Partem de um trabalho anterior, o de Lijmer e colegas (JAMA, 1999), que olhou 6 critérios de método e 3 de relato num número limitado de problemas clínicos, e declaram o novo como validação e extensão dele, com um conjunto maior e mais amplo. Para que a validação fosse independente, nenhuma meta-análise de Lijmer entrou.

## Método, passo a passo

**Busca das revisões.** MEDLINE (OVID e PubMed), EMBASE (OVID), DARE e MEDION, para revisões sistemáticas de acurácia publicadas de janeiro de 1999 a abril de 2002. O foco em revisões recentes vem da expectativa de mais estudos por revisão e de mais variedade entre estudos com e sem defeito.

**Critérios para a revisão entrar.** Pelo menos 10 estudos primários de acurácia do mesmo teste; seleção de estudos que não usasse as características a avaliar; sensibilidade e especificidade dadas em pelo menos 90% dos estudos. Inglês, alemão, francês ou holandês. Quando duas ou mais revisões tratavam da mesma combinação de teste e condição, ficava a maior, para não repetir estudo primário.

**Quem selecionou.** Em fase nenhuma os avaliadores deixaram de ver o nome dos autores e da revista. A busca e o primeiro corte, por título e resumo, ficaram com uma só pessoa (A.R.); o que sobrou dele foi lido em dupla, cada um por conta própria. Todos passaram por treino no uso dos formulários padronizados e dos documentos de apoio, e os critérios de inclusão ainda mudaram um pouco enquanto se extraíam os primeiros estudos primários.

**Extração dos estudos primários.** Foram buscadas as cópias em papel; saía o estudo cuja tabela 2 × 2 não se conseguia reproduzir. Dos relatos saíram itens de desenho, grupo de pacientes, verificação, execução e leitura do teste, coleta de dados, análise e qualidade do relato. Daí vieram a lista de 15 potenciais fontes de viés ou variação (a partir de revisões sistemáticas recentes) e mais 9 itens de qualidade do relato. Uma epidemiologista avaliou todos os artigos; uma segunda avaliação independente veio de um entre 5 clínicos e epidemiologistas treinados; a discordância era discutida e, se preciso, um terceiro decidia.

**Análise.** O número que o estudo entrega por característica é a razão relativa de chances diagnóstica (RDOR), a DOR média dos estudos que têm o defeito sobre a dos que não têm, sendo a DOR (razão de chances diagnóstica, diagnostic odds ratio) a medida-resumo de acurácia; quando passa de 1, o defeito anda junto com estimativas maiores. Ela é o antilogaritmo do coeficiente da característica numa regressão de efeitos aleatórios que estende a curva ROC resumo (summary ROC), estimada no PROC MIXED do SAS 9.1. Nessa regressão, o log da DOR de cada estudo tem quatro parcelas: a DOR-resumo do teste, o limiar de positividade do próprio estudo (logit da sensibilidade somado ao logit de 1 menos a especificidade), as características de desenho, cada uma já descontada das outras, e um erro residual. Também sai do modelo quanto o efeito de cada característica oscila entre meta-análises: variância grande quer dizer que tamanho ou até direção mudam de uma meta-análise para outra, e variância perto de zero, que o efeito se repete em todas.

**Regras do modelo multivariável.** O que acontecia com cada covariável dependia da parcela de estudos omissos sobre ela: com até 10%, a omissão contava como defeito e os omissos iam para a categoria potencialmente defeituosa; na faixa do meio, formavam uma categoria à parte, "não relatado"; de 50% para cima, a covariável ficava fora do modelo. Para juntar categorias com poucos estudos, a análise univariável tinha de mostrar estimativas comparáveis e o mecanismo de viés tinha de ser julgado parecido; sem as duas coisas, ficavam separadas.

## Fluxo e amostra (figura 1)

- 191 revisões potencialmente elegíveis; 157 excluídas (os critérios podem se sobrepor): escopo diferente 60; menos de 10 estudos primários 36; seleção baseada em parte em características de desenho 33; sem busca sistemática 24; mais de 10% dos estudos e sem estimativa-resumo 12; só comparações diretas 4; agrupamento impossível 3; referências inacessíveis 2.
- Sobram 34 revisões (39 meta-análises, 678 estudos). Saem 6 revisões (8 meta-análises): tabela 2 × 2 irreproduzível na maioria dos estudos (2) ou sobreposição de estudos com outra meta-análise (4).
- Sobram 28 revisões (31 meta-análises, 554 estudos). Saem 67 estudos primários: tabela irreproduzível 19; série de casos, só com sensibilidade 15; pesquisa não original, literatura cinzenta ou inacessível 13; teste ou doença não comparável 8; publicação dupla 3; idioma fora de inglês, espanhol, francês, italiano, alemão ou holandês 9.
- Final: **31 meta-análises, 487 estudos primários.** Duas meta-análises do mesmo problema, com restrições diferentes de seleção, foram tratadas como uma; outra foi partida em 4 por diferença de técnica. Por essas exclusões e pela partição, 6 meta-análises ficaram com menos de 10 estudos.
- A variedade é grande: de sinais e sintomas da anamnese e do exame físico a exames de laboratório e de imagem. A DOR agrupada vai de 1,2 a 565, mediana 30. O apêndice 3 lista as meta-análises: por exemplo, palpação abdominal para aneurisma de aorta, questionário CAGE para abuso de álcool, ressonância para estadiar câncer de próstata, ultrassom para síndrome de Down.

## Como eram os estudos

445 de 487 (91%) usavam uma coorte clínica; 453 (93%) verificavam todos os resultados do teste com um padrão de referência; 463 (95%) interpretavam a referência sem incorporar o resultado do teste. **Só 1 estudo cumpria as 13 características desejadas.**

## Qualidade do relato (tabela 1, 487 estudos; relatado, número e %)

| Característica | Sim | Não |
|---|---|---|
| Datas do período de inclusão | 238 (49) | 249 (51) |
| Definição de positivo e negativo no teste | 426 (87) | 61 (13) |
| Definição de positivo e negativo na referência | 362 (74) | 125 (26) |
| Distribuição de sexo ou idade | 406 (83) | 81 (17) |
| Número de leitores do teste | 198 (41) | 289 (59) |
| Número de leitores da referência | 111 (23) | 376 (77) |
| Formação dos leitores do teste | 187 (38) | 300 (62) |
| Formação dos leitores da referência | 131 (27) | 356 (73) |
| Treino dos leitores | 26 (5) | 426 (88) |
| Reprodutibilidade do teste ou da referência | 70 (14) | 417 (86) |
| Intervalo de confiança ou erro padrão das medidas | 81 (17) | 406 (83) |

Outros 35 estudos (7%) disseram que não houve treino. A reprodutibilidade inclui a simples menção a artigo que a declara.

Resultados indeterminados e desistências vieram em menos de 50% dos estudos, então esses 2 itens saíram da análise multivariável. Dos 13 restantes, 6 faltavam em mais de 10% dos estudos.

## O resultado central (tabela 2, modelo multivariável; a figura 2 traz os mesmos números)

A categoria de referência de cada item tem RDOR 1 por definição. Estudos / meta-análises entre parênteses na primeira coluna; variância é a do efeito entre meta-análises.

| Item (estudos / meta-análises) | RDOR (IC 95%) | Variância |
|---|---|---|
| **1. Coorte, referência** (445/31) | 1,0 | 0,7 |
| Casos graves e controles saudáveis (5/2) | 4,9 (0,6 a 37,3) | |
| Outro desenho caso-controle (37/7) | 1,1 (0,4 a 3,4) | |
| **2. Seleção por sintomas ou sinais, referência** (160/26) | 1,0 | 0,0 |
| Seleção por encaminhamento para o teste (36/9) | 0,5 (0,3 a 0,9) | |
| Seleção por resultados de outros testes (291/24) | 0,9 (0,6 a 1,3) | |
| **3. Sem desafio limitado, referência** (359/31) | 1,0 | 0,1 |
| Desafio limitado (85/23) | 0,9 (0,6 a 1,3) | |
| Desafio aumentado (43/14) | 1,0 (0,6 a 1,7) | |
| **4. Amostra consecutiva, referência** (130/30) | 1,0 | 0,1 |
| Não consecutiva (173/29) | 1,5 (1,0 a 2,1) | |
| Aleatória (17/6) | 1,7 (0,9 a 3,2) | |
| Amostragem não descrita (167/28) | 0,9 (0,6 a 1,3) | |
| **5. Mesma referência, referência** (388/29) | 1,0 | 0,2 |
| Verificação diferencial (99/14) | 1,6 (0,9 a 2,9) | |
| **6. Verificação completa, referência** (453/31) | 1,0 | 0,0 |
| Parcial (34/15) | 1,1 (0,7 a 1,7) | |
| **7. Referência única, referência** (395/28) | 1,0 | 0,4 |
| Referência composta (92/14) | 0,9 (0,5 a 1,8) | |
| **8. Sem incorporação, referência** (463/31) | 1,0 | 0,0 |
| Incorporação (24/8) | 1,4 (0,7 a 2,8) | |
| **9. Intervalo adequado, referência** (236/28) | 1,0 | 0,0 |
| Inadequado (45/15) | 1,1 (0,7 a 1,6) | |
| Não relatado (206/28) | 1,2 (0,9 a 1,6) | |
| **10. Tratamento retido, referência** (250/28) | 1,0 | 0,0 |
| Tratamento dado (54/11) | 0,9 (0,6 a 1,4) | |
| Não relatado (183/25) | 1,0 (0,7 a 1,4) | |
| **11. Leitura duplo-cega, referência** (84/21) | 1,0 | 0,0 |
| Simples ou sem cegamento (187/17) | 1,1 (0,8 a 1,6) | |
| Cegamento não relatado (216/17) | 0,9 (0,6 a 1,3) | |
| **12. Coleta prospectiva, referência** (301/31) | 1,0 | 0,1 |
| Coleta retrospectiva (106/21) | 1,6 (1,1 a 2,2) | |
| Não relatada (80/22) | 1,0 (0,7 a 1,5) | |
| **13. Corte predefinido ou padrão, referência** (338/31) | 1,0 | 0,0 |
| Corte definido depois (59/15) | 1,3 (0,8 a 1,9) | |
| Não relatado (90/18) | 0,9 (0,7 a 1,3) | |

Significativos: coleta retrospectiva e inclusão não consecutiva, para cima; seleção por encaminhamento, para baixo. Inclusão aleatória e verificação diferencial também sobem a estimativa, sem significância.

**Casos graves com controles saudáveis** dão a maior superestimação, mas só 5 estudos em 2 meta-análises usaram esse desenho, daí o intervalo largo, e a heterogeneidade entre as duas é grande (0,7): a superestimação foi severa numa (bactéria gram-negativa pelo lisado de amebócito de Limulus, Gelation Limulus amebocyte lysate) e bem menor na outra (abuso de álcool pelo questionário CAGE).

**Variância.** Os autores veem diferença moderada a grande entre meta-análises para desenho (coorte contra caso-controle), referência composta e verificação diferencial; para as demais dizem que fica perto de zero (a tabela mostra 0,0 ou 0,1).

## Análise univariável (apêndice 4)

Sem ajuste, os números principais ficam próximos: casos graves com controles saudáveis, 4,3 (0,5 a 38,0); outro caso-controle, 1,0 (0,3 a 3,3); encaminhamento para o teste, 0,6 (0,3 a 1,3); não consecutiva, 1,5 (1,1 a 2,1); aleatória, 1,7 (0,9 a 3,1); verificação diferencial, 1,5 (0,9 a 2,6); retrospectiva, 1,4 (1,0 a 1,9). Os dois itens que não foram adiante: resultados não interpretáveis não relatados (364 estudos, 75%), 0,7 (0,6 a 0,9); desistências (29 estudos, 6%), 0,6 (0,4 a 1,1); desistências não relatadas (406, 83%), 1,2 (0,8 a 1,7). Antes do modelo multivariável, algumas categorias se fundiram: seleção por outros testes, por encaminhamento para a referência e não relatada (122, 150 e 19 estudos, os 291 da tabela 2); referência composta e composição não relatada (78 e 14, os 92); incorporação e não relatado (17 e 7, os 24); leitura sem cegamento e com cegamento simples (24 e 163, os 187).

## O que os autores dizem de cada mecanismo

- **Coleta retrospectiva ou dado clínico de rotina:** DOR superestimada em 60%. Com a coleta planejada depois dos testes, fica difícil usar critério de inclusão sem ambiguidade e achar quem fez o teste e não foi verificado.
- **Inclusão não consecutiva:** sobe a DOR em 50% em relação à série consecutiva, mas a explicação dos autores admite os dois sentidos. Deixar de fora os casos claros, quando a referência custa caro ou é invasiva, puxa a acurácia para baixo; deixar de fora os complexos, coisa mais provável enquanto o teste está no começo da avaliação, puxa para cima. Como os dois efeitos se anulam em parte, faz sentido que outros estudos tenham achado, em média, estimativa menor ou nenhum efeito.
- **Seleção por encaminhamento ou por testes anteriores:** a explicação vem como especulação, já que os autores admitem que a leitura "is not straightforward", e é a de um filtro nas duas pontas: o paciente muito suspeito segue adiante sem mais testes, e o de chance baixa nem chega a ser testado. Com menos verdadeiros positivos e menos verdadeiros negativos na amostra, esses estudos tendem a dar acurácia menor do que os que incluem todos com os sintomas definidos de antemão.
- **Casos graves e controles saudáveis:** os autores tratam esse desenho como a inclusão seletiva levada ao extremo, e o ganho aparece nos dois lados da tabela: com controles sadios os alarmes falsos ficam raros e a especificidade sobe, e com o quadro grave, fácil de enxergar, sobe a sensibilidade. Não é achado isolado, porque outros estudos relatam a mesma superestimação nesse tipo de caso-controle.
- **Duas ou mais referências para verificar o teste:** Lijmer já tinha medido esse efeito, em 2 vezes, e o intervalo dele se sobrepõe ao deste estudo, que acha razões de chances em média 60% maiores do que com referência única. Para a inflação há duas explicações prováveis: as referências podem divergir na definição da condição ou na qualidade, e, quando a segunda erra junto com o teste avaliado, os dois concordam mais sem que a acurácia real seja maior.
- **Verificação parcial:** deixar parte dos negativos sem confirmação costuma empurrar a sensibilidade para cima e a especificidade para baixo, movimentos que podem se anular na razão de chances; por esse efeito de direção e tamanho imprevisíveis os autores explicam não terem achado nada consistente, o mesmo resultado nulo de Lijmer.
- **Ausência de associação:** não demonstrar associação no modelo não autoriza ignorar a característica num estudo dado, porque o efeito pode variar entre meta-análises ou dentro de uma só.

## Limites e forças declarados

- Escolha de modelo: ao contrário de Lijmer, que usou efeitos fixos, aqui cada covariável pode ter efeito diferente em cada meta-análise, nos efeitos aleatórios que os autores julgam mais apropriados; o custo são intervalos mais largos que os dele, embora com 269 estudos a mais.
- Escolha de medida: a razão de chances resume com conveniência, mas fica cega quando sensibilidade e especificidade andam em sentidos contrários, e por isso os autores querem ver a mesma análise feita com sensibilidade, especificidade e razões de verossimilhança.
- Lacunas dos relatos: como os estudos pouco diziam sobre espectro clínico, critérios de seleção, grau de cegamento e frequência de indeterminados e desistências, essas características ficaram sem exame adequado.

## Conclusão dos autores

Estudos do mesmo teste podem chegar a estimativas diferentes conforme as escolhas de desenho, e o tamanho do efeito pode variar de uma situação para outra. Pesquisadores ao desenhar e leitores ao avaliar devem pesar as características de desenho e as características clínicas dos pacientes. O relato incompleto atrapalha a avaliação do viés; apoiam iniciativas como o STARD (Standards for Reporting of Diagnostic Accuracy).

## Tudo o mais que ensina

- **Definições do apêndice 2.** Caso-controle "outro": evita selecionar dos extremos do espectro. Desafio limitado: critérios extras que excluem pacientes com traços capazes de produzir falso negativo ou falso positivo; desafio aumentado: inclusão preferencial desses pacientes. Verificação diferencial: parte dos resultados confirmada por uma referência alternativa. Referência composta: combinação de testes ou procedimentos. Incorporação: o teste avaliado faz parte da referência. Corte definido depois: o valor de positividade é fixado depois da coleta.
- **O ideal que o apêndice descreve:** todo resultado do teste verificado por uma única referência independente, de forma instantânea, sem tratamento no intervalo.
- **Por que leitura sem cegamento importa:** conhecer o resultado da referência ao ler o teste, ou o inverso, pode aumentar a concordância.
- **Por que coleta prospectiva importa:** permite dado de alta qualidade; a retrospectiva fica mais sujeita a dado faltante e a fluxo incompleto de pacientes.
- **Ensaios clínicos vieram antes:** o efeito de randomização ruim e de desistência diferencial já estava demonstrado neles, e daí nasceram as diretrizes. Nas diretrizes de acurácia, muitos itens têm pouca ou nenhuma evidência empírica de viés, lacuna que motiva o estudo.
- **Quadro do editor na revista:** a variação marcada das estimativas deve deixar o clínico cauteloso ao ler estudo de acurácia.
- **Financiamento e conflito:** Organização Holandesa de Pesquisa Científica (NWO, 945-10-012), sem participação no estudo; sem conflitos declarados.

## O que a fonte não diz

Não traz sensibilidade e especificidade por característica de desenho, só a razão de chances relativa. Não converte a RDOR em ponto percentual de acurácia. Não diz quais das 2 meta-análises de casos graves deram qual valor numérico.
