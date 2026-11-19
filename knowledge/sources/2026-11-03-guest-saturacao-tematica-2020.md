---
titulo: "A simple method to assess and report thematic saturation in qualitative research"
tipo: paper
autor: "Guest, Greg; Namey, Emily; Chen, Mario"
url: "https://doi.org/10.1371/journal.pone.0232076"
publicado_em: 2020-05-05
capturado_em: 2026-11-03
areas: [journalism]
tags: [data-saturation, thematic-saturation, stopping-rule, qualitative-research, sample-size, interviews, bootstrap, reporting]
licenca: "CC BY 4.0 (declarada no XML JATS do artigo no PMC, PMC7200005, no elemento license, com link para http://creativecommons.org/licenses/by/4.0/; o Crossref registra a mesma licença para o DOI)"
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Artigo em *PLOS ONE* 15(5): e0232076, publicado em 5 de maio de 2020; PMCID PMC7200005. Autores: Greg Guest (Q42 Research, Research Triangle Park, Carolina do Norte), Emily Namey e Mario Chen (Global Health, Population, and Nutrition, FHI 360, Durham, Carolina do Norte); editor Andrew Soundy (Universidade de Birmingham). Sem financiamento específico, segundo a declaração de financiamento. Texto lido: o XML JATS de texto completo da Europe PMC (o mesmo arquivo do PMC7200005, conferido byte a byte), sem as três figuras, que no XML só têm a legenda. Os dados dos três conjuntos estão no material suplementar S1 (planilha XLSX), não aberto.

## O problema

A saturação de dados é a régua usada para estimar e avaliar o tamanho de amostra qualitativa. Os estudos empíricos e os modelos estatísticos das duas décadas anteriores ajudam a estimar, na fase de desenho, quantas entrevistas um estudo vai precisar, mas não dão um jeito de verificar a saturação, e com ela a adequação da amostra, durante ou depois da coleta. Os autores retomam a frase de Morse (1995) de que a saturação aparece nos estudos "mainly by declaration" e propõem um método para medir e relatar a saturação que vá além da declaração.

Escopo declarado: técnicas de coleta que produzem narrativa (grupos focais e entrevistas individuais com perguntas abertas e sondagem indutiva), validado só com entrevistas individuais; análise temática indutiva, em que os temas são descobertos nos dados e depois viram códigos.

## O que se sabia (revisão)

- **Origem do termo:** "saturação teórica", de Glaser e Strauss (1967), o ponto em que não aparecem mais dados para desenvolver as propriedades de uma categoria; feita para construir e testar modelos teóricos (o modelo se estabiliza). Com o uso fora da teoria fundamentada, o termo mais amplo "saturação de dados" passou a designar o ponto em que dados novos trazem pouca ou nenhuma informação nova para a pergunta de pesquisa.
- **A pesquisa empírica começou pela estimativa**, porque financiadores e comitês de ética pedem o tamanho de amostra antes do campo. Morgan e colegas: as cinco ou seis primeiras entrevistas deram a maior parte da informação nova; perto de 20 entrevistas pouco se ganhava; em quatro conjuntos, 80% a 92% dos conceitos apareciam nas 10 primeiras. Guest e colegas (2006), 60 entrevistas com trabalhadoras do sexo na África Ocidental: 70% dos 114 temas nas seis primeiras e 92% nas 12 primeiras. Francis e colegas e Namey e colegas acharam resultados parecidos. Hagaman e Wutich: menos de 16 entrevistas bastaram em cada um de quatro locais, mas 20 a 40 foram precisas para os metatemas entre locais.
- **Modelos probabilísticos:** Galvin analisou 54 estudos com lógica binomial: com seis pessoas, a chance de achar um tema é maior que 99% se ele for partilhado por 55% da população. Fugard e Potts fizeram uma ferramenta que usa a prevalência estimada do tema, o número de ocorrências desejado e o poder do estudo; exemplo: 80% de poder para ver duas ocorrências de um tema com 10% de prevalência pede 29 participantes; o modelo supõe amostra aleatória.
- **O limite dessas estimativas:** fazem o papel do cálculo de poder do estudo quantitativo e, como ele, perdem a utilidade quando a coleta começa, porque a realidade pode não seguir as suposições. Daí as duas perguntas novas: como operacionalizar melhor a saturação, e como saber se ela foi atingida.

## As operacionalizações anteriores (tabela 1, resumida)

A tabela 1 resume dez abordagens e o que os autores veem de limite em cada uma:

- **Guest e outros (2006):** saturação como proporção, temas achados até um ponto divididos pelo total de temas da amostra inteira; relatada como o ponto em que, depois do fato, 80% ou 90% dos temas apareceram; análise em lotes de seis entrevistas. Limite: como o denominador é fixo, todo conjunto chega um dia a 100%.
- **Francis e outros (2010):** amostra inicial de análise e critério de parada (entrevistas seguidas sem tema novo) fixados antes da análise. Limites: exigência rígida, difícil de cumprir em estudo pequeno; feito para estudo baseado em teoria; só uma combinação de amostra inicial e critério foi testada.
- **Coenen e outros (2012):** saturação quando duas entrevistas seguidas não trazem categoria de segundo nível nova. Limites: depende de só duas entrevistas, é vulnerável a casos atípicos, e a definição das categorias de segundo nível não é clara.
- **Galvin:** meta-análise de 54 estudos da literatura de edificações e energia, lógica binomial. Limites: probabilístico, supõe amostra aleatória e conhecimento prévio de quais temas vão surgir e com que frequência; não serve a estudo indutivo.
- **Fugard e Potts:** cálculo com prevalência esperada, número de ocorrências e poder. Limites: os mesmos, mais a exigência de vários parâmetros antes da coleta.
- **Hennink e outros:** separam saturação de código (códigos principais) e de significado (subcódigos com mais nuance), ambas como proporção do total. Limite: o mesmo denominador fixo de Guest 2006.
- **Tran e outros:** simulação de Monte Carlo em perguntas abertas de questionário; saturação quando o custo de mais uma unidade supera o ganho esperado de informação. Limite: respostas de questionário são mais restritas que conversa; não se generaliza para texto livre.
- **Rijnsoever:** simulações comparando três cenários; saturação quando todos os códigos da população foram vistos uma vez na amostra. Limites: os "dados" da população são hipotéticos e o modelo pede muita informação prévia.
- **Hagaman e Wutich:** identificam os três temas mais frequentes, reordenam as entrevistas por bootstrap e registram quantas entrevistas levam até a primeira, segunda e terceira ocorrência deles. Limite: é preciso conhecer antes os temas mais frequentes.
- **Lowe e outros:** modelos estatísticos da taxa de descoberta de temas, quatro modelos com graus diferentes de dependência entre observações, validados em grupos focais e em levantamento de literatura. Limites: probabilístico, supõe amostra aleatória, equações complexas.
- **Weller e outros:** listas livres de 28 conjuntos; saturação quando o número esperado de itens novos por entrevistado é um ou menos. Limite: a medida de saliência não se aplica a entrevista em profundidade com narrativa livre.

## As três limitações que o método quer superar

1. **Métricas sem comparação entre si:** os critérios para declarar saturação variam muito em unidade de análise e rigor, e não há convenção, como os intervalos de confiança do quantitativo, para dizer quanta confiança uma conclusão merece.
2. **Dependência de probabilidade ou de amostra aleatória:** a maior parte da pesquisa qualitativa usa amostra intencional; e mesmo com sorteio, as respostas abertas não formam categorias mutuamente exclusivas (expressar o tema A não exclui o B, e não expressar A não quer dizer "não A"). Além disso, muitos pesquisadores qualitativos não têm o preparo nem o tempo para testes estatísticos; o método proposto usa só aritmética simples e porcentagem.
3. **Avaliação retrospectiva, que exige o conjunto inteiro codificado:** quando o denominador é o total de temas do conjunto completo, a saturação acontece por definição num conjunto fechado. O método troca o denominador por um subconjunto inicial, o que permite avaliar durante a coleta e parar antes do número previsto; em troca, a porcentagem de saturação no sentido daqueles autores deixa de existir.

## O método: três elementos

Definição de trabalho: saturação é o ponto da análise em que entrevistas novas trazem pouca ou nenhuma informação nova útil para os objetivos do estudo. Ela se mede com três elementos.

- **Base (*base size*):** quantas entrevistas iniciais formam o corpo de informação já obtido, cujo número de temas únicos vai no denominador (equivale à amostra inicial de análise de Francis). Usar todas as entrevistas como base produz saturação por definição; e como a informação nova costuma cair depressa nas primeiras entrevistas, numa curva assintótica, os autores testam bases de 4, 5 e 6 entrevistas. Unidade de análise: a entrevista; item contado: código único que representa um tema.
- **Sequência (*run length*):** o conjunto de entrevistas consecutivas em que se procuram temas novos; o número de temas novos na sequência vai no numerador. Hagaman e Wutich e Francis usam sequências de três; Coenen, de duas; o método oferece as duas opções. As sequências se sobrepõem: cada nova sequência anda uma entrevista para frente (figura 1).
- **Limiar de informação nova (*new information threshold*):** quanto de informação nova se aceita como sinal de saturação, escolha que os autores chamam de puramente subjetiva. Em vez de um limiar único, propõem dois: até 5% de informação nova e nenhuma (0%). Servem como o p < 0,05 ou p < 0,01 servem para rejeitar a hipótese nula, mas sem teoria de probabilidade: atingir o limiar não garante saturação; dá um modo transparente de relatar a avaliação. Quanto mais baixo o limiar, menor a chance de sobrar um número importante de temas para as entrevistas seguintes. A figura 2 mostra como a combinação dos três elementos dá mais ou menos confiança.

Vantagens listadas: não pede amostra aleatória nem conhecimento prévio da prevalência dos temas; conta simples, sem estatística; serve durante a coleta (com a possibilidade de fazer menos entrevistas que o previsto) e depois dela (para relatar a adequação da amostra); os parâmetros podem ser fixados antes ou relatados depois; é flexível e dá mais precisão ao uso do termo; e, por ser medida relativa, neutraliza diferenças de granularidade da codificação entre pesquisadores, porque a granularidade afeta numerador e denominador.

## O exemplo passo a passo

Conjunto hipotético (figura 3), base de 4, sequência de 2, limiar de até 5%:

1. As entrevistas 1 a 4 trazem 17, 8, 5 e 7 temas novos: 37 temas na base, que é o denominador.
2. Primeira sequência, entrevistas 5 e 6: 4 + 3 = 7 temas novos.
3. 7 / 37 = 19%: acima do limiar, continua.
4. Próxima sequência, entrevistas 6 e 7 (a 6 se repete): 3 + 1 = 4.
5. 4 / 37 = 11%: ainda acima.
6. Entrevistas 7 e 8: 1 + 0 = 1.
7. 1 / 37 = 3%: abaixo do limiar; para depois da 8ª entrevista.

**Como relatar:** a saturação é atribuída à entrevista 6, porque as duas seguintes só serviram para verificar quanto de novo apareceria; as entrevistas da sequência entram como expoente: "com base 4, o limiar de até 5% foi atingido em 6^+2 entrevistas", que indica oito entrevistas feitas. Para mais rigor, aumenta-se a sequência para 3 ou mais e/ou adota-se o limiar de 0%; no mesmo exemplo, com sequência de 2, o limiar de 0% sairia em 10^+2. O exemplo vai até 20 entrevistas: depois da 12ª ainda apareceram quatro temas, mas todas as sequências ficaram em até 5%.

**As duas perguntas que o exemplo deixa:** (1) como saber que não se perde algo importante parando no ponto indicado? A resposta dos autores: não se sabe, e só se saberia fazendo mais entrevistas; o que ampara a parada é a literatura que mostra a informação nova caindo com o tempo e os temas mais comuns e salientes surgindo cedo, desde que perguntas, perfil da amostra e demais parâmetros fiquem estáveis. (2) A ordem das entrevistas muda o resultado? Pode surgir tema importante tarde, mas os estudos citados mostram os temas mais frequentes aparecendo em cerca de seis entrevistas; para checar, o bootstrap sorteia a ordem.

## A validação

**Três conjuntos reais**, todos de entrevistas individuais com análise temática indutiva, diferentes em população, tema, heterogeneidade, entrevistador e estrutura do roteiro:

- **Conjunto 1:** 40 entrevistas com homens afro-americanos do sudeste dos Estados Unidos sobre busca de cuidados de saúde; roteiro de 13 perguntas com subperguntas; análise de 11 perguntas; 93 códigos únicos; amostra muito homogênea.
- **Conjunto 2:** 48 entrevistas com mães (na maioria brancas) do sudeste dos Estados Unidos sobre risco médico e pesquisa na gravidez; 13 perguntas, análise de 10; 85 códigos; 12 entrevistas em cada modo: presencial, vídeo, e-mail (assíncrono) e chat de texto (síncrono).
- **Conjunto 3:** 60 entrevistas com mulheres de maior risco de HIV, 30 no Quênia e 30 na África do Sul, em continuação a um questionário; 14 perguntas no roteiro, só três analisadas; 55 códigos. As duas amostras diferiam em escolaridade e estado civil (63% das quenianas casadas e morando com o parceiro, contra 3%).

Nos três: gravação, transcrição com protocolo (tradução para o inglês no conjunto 3), NVivo, livro de códigos com definições explícitas. Nos conjuntos 1 e 2, dois analistas codificaram cada transcrição e resolveram as diferenças por consenso; no 3, a checagem entre codificadores cobriu 20% das entrevistas. Aprovação do comitê de ética da FHI 360 (e de comitês locais no Quênia e na África do Sul para o conjunto 3).

**Bootstrap:** 10.000 reamostragens com reposição de cada conjunto, com a ordem das transcrições sorteada em cada uma para neutralizar efeito de ordem. Em cada reamostragem, a proporção de temas novos em sequências de 2 ou 3 relativa a bases de 4, 5 ou 6, e o número de entrevistas até atingir até 5% e 0%. Saem a mediana e os percentis 5 e 95, que formam um intervalo não paramétrico de 90%. Cálculo extra, só para validar (não faz parte do método proposto): no ponto de parada de cada reamostragem, os temas achados até ali divididos pelo total do conjunto, o "grau de saturação" retrospectivo.

## Os resultados (tabelas 2 a 4)

O número de entrevistas não inclui as da sequência (por isso o expoente +2 ou +3). Cada célula: mediana de entrevistas (percentis 5 e 95) e, abaixo, o grau de saturação na mediana (percentis 5 e 95).

**Conjunto 1** (40 entrevistas, 93 códigos):

| Limiar | Sequência | Base 4 | Base 5 | Base 6 |
|---|---|---|---|---|
| até 5% | 2 | 6 (4, 9); 78% (70, 87) | 6 (4, 9); 78% (70, 87) | 6 (4, 9); 78% (70, 86) |
| até 5% | 3 | 7 (4, 12); 83% (73, 89) | 7 (4, 11); 82% (73, 89) | 7 (4, 11); 82% (73, 89) |
| 0% | 2 | 11 (5, 17); 87% (76, 95) | igual | igual |
| 0% | 3 | 14 (7, 23); 90% (82, 97) | igual | igual |

**Conjunto 2** (48 entrevistas, 85 códigos):

| Limiar | Sequência | Base 4 | Base 5 | Base 6 |
|---|---|---|---|---|
| até 5% | 2 | 6 (4, 10); 79% (69, 87) | 6 (4, 10); 79% (68, 87) | 6 (4, 9); 79% (67, 87) |
| até 5% | 3 | 8 (4, 13); 82% (73, 89) | 7 (4, 12); 82% (73, 89) | 7 (4, 12); 82% (72, 89) |
| 0% | 2 | 11 (6, 17); 87% (75, 93) | igual | igual |
| 0% | 3 | 14 (8, 22); 89% (81, 95) | igual | igual |

**Conjunto 3** (60 entrevistas, 55 códigos):

| Limiar | Sequência | Base 4 | Base 5 | Base 6 |
|---|---|---|---|---|
| até 5% | 2 | 9 (4, 16); 64% (45, 78) | 8 (4, 14); 62% (44, 76) | 8 (4, 13); 62% (44, 76) |
| até 5% | 3 | 12 (6, 22); 71% (53, 84) | 11 (6, 19); 69% (53, 82) | 11 (6, 18); 69% (53, 82) |
| 0% | 2 | 12 (6, 19); 69% (49, 83) | igual | igual |
| 0% | 3 | 16 (8, 26); 76% (60, 87) | igual | igual |

Leitura dos autores, por conjunto:

- **Conjunto 1:** com até 5%, a mediana não muda com a base: 6^+2 com sequência de 2 e 7^+3 com sequência de 3; o texto dá grau de saturação de 78% a 82% nesse ponto. Com 0%: 11^+2 e 14^+3, também iguais entre bases; o texto dá 87% a 89%. (Conferência de quem fez a ficha: a tabela 2 traz 83% para base 4 e sequência 3 com até 5%, e 90% para sequência 3 com 0%.)
- **Conjunto 2:** quase igual ao 1: 6^+2 e 7^+3 ou 8^+3 com até 5% (79% a 82%); 11^+2 e 14^+3 com 0% (87% a 89%).
- **Conjunto 3:** com mais variação na amostra, pede um pouco mais de entrevistas e chega a grau de saturação menor: 8 a 9 com sequência de 2 e 11 a 12 com sequência de 3 com até 5% (o número maior com base 4), grau de 62% a 71%; 12^+2 e 16^+3 com 0%, grau de 69% a 76%.

## A discussão

- O método funciona durante ou depois da coleta, e o rigor se escolhe pela sequência e pelo limiar, com mais clareza no relato.
- Os resultados ficam na faixa dos estudos anteriores: com até 5%, em amostra homogênea, 6 a 7 entrevistas costumam captar a maioria dos temas (6 entrevistas para 80% de saturação); no percentil 95 dessa opção, 11 a 12 entrevistas, o que acompanha a literatura que fala em 12 para graus mais altos de saturação.
- **Base quase não muda o resultado:** se isso se mantiver em outros contextos, uma base padrão de 4 basta, e a primeira avaliação se faz depois de 6 entrevistas (4 de base e 2 de sequência); analisando em tempo real, essa primeira avaliação decide se mais entrevistas são necessárias.
- **Sequência muda o resultado:** mais longa, mais entrevistas até a saturação; o efeito é mínimo com o limiar de até 5%. Sequência de 3 ou mais dá uma avaliação mais conservadora.
- **Limiar muda o resultado:** quanto mais baixo, mais entrevistas; escolher 0% dá avaliação mais conservadora.

**Limites declarados:** o método foi feito para análise temática indutiva aplicada, que responde a uma pergunta relativamente estreita sobre um problema concreto, e os três conjuntos vêm desse quadro; não foi testado em pesquisa qualitativa de outra perspectiva epistemológica ou fenomenológica. Foi testado em livro de códigos de um nível só; com códigos em hierarquia (códigos-pai e códigos-filho, ou metatemas como os de Hagaman e Wutich), o pesquisador precisa decidir em que nível conta os temas, decisão subjetiva que depende da granularidade que a análise pede; é possível rodar e relatar a saturação para dois ou mais livros de códigos com granularidades diferentes.

## A conclusão

Os autores concordam com Tran e colegas que achar o ponto de saturação é difícil, porque o pesquisador só tem informação sobre o que já encontrou, e que a parada num estudo indutivo costuma sair do julgamento e da experiência de quem pesquisa. Comparam com o quantitativo: o que conta como efeito grande o bastante ou p pequeno o bastante também é convenção de cada campo, e um p pode ser relatado em valor exato ou em faixas. O pedido é a mesma flexibilidade e transparência para a saturação temática, com base, sequência e limiar escolhidos conforme a confiança desejada, e testes do método em outros tipos de dados, populações e contextos.

## Tudo o mais que ensina

- **Por que estimar antes não basta:** a estimativa é como o cálculo de poder: depende de suposições sobre o estudo e não diz nada sobre os dados que de fato chegaram.
- **A analogia do limiar com o p-valor** é explícita e com ressalva: não há teoria de probabilidade por trás, e atingir o limiar não garante que a saturação ocorreu.
- **Por que a medida é relativa:** com a base como denominador, um codificador mais fino ou mais grosso altera os dois lados da razão, o que reduz a diferença entre equipes.
- **O preço de abandonar o denominador total:** deixa de existir a porcentagem de saturação no sentido de Guest 2006 e Hennink; o grau de saturação entra no artigo só como verificação, porque os autores tinham o total de códigos de cada conjunto.
- **Notação proposta para o relato:** o número de entrevistas até o ponto de saturação, com o tamanho da sequência em expoente (6^+2, 7^+3), sempre acompanhado da base e do limiar usados.
- **Agradecimentos:** a Betsy Tolley, pela leitura de uma versão anterior, e a Alissa Bernholc, pela programação.
