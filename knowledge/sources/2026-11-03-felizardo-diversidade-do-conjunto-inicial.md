---
titulo: "Assessing diversity in creating seed set for snowballing search for systematic literature review in software engineering"
tipo: paper
autor: "Felizardo, Katia Romero; Souza, Francisco Carlos; Souza, Alinne C. Corrêa; Napoleão, Bianca Minetto; Steinmacher, Igor; Gerosa, Marco"
url: "https://users.ime.usp.br/~gerosa/papers/ESEM___Snowballing.pdf"
publicado_em: 2025-10-02
capturado_em: 2026-11-03
areas: [journalism]
tags: [systematic-review, snowballing, seed-set, start-set, diversity, search-strategy, recall, precision, replication, software-engineering, screening]
licenca: "Sem licença indicada: o PDF não traz aviso de licença nem de copyright; o OpenAlex registra o artigo publicado (DOI 10.1109/ESEM64174.2025.00028) como acesso fechado e sem licença. Tratado como protegido; entra só a ficha. O integral está no PDF da url, na página de Marco Gerosa no IME-USP."
---

Ficha de estudo, em palavras próprias. O PDF (11 páginas, gerado em pdfTeX em 29 de julho de 2025) não traz ano nem veículo. Pelo OpenAlex (busca pelo título), o artigo saiu no ESEM, o ACM/IEEE International Symposium on Empirical Software Engineering and Measurement, edição de 2025, com DOI 10.1109/ESEM64174.2025.00028, páginas 1 a 11, data de publicação 2 de outubro de 2025; é essa a data no frontmatter. Autores da Universidade Tecnológica Federal do Paraná (Felizardo, F. C. Souza, A. C. C. Souza), da Université du Québec à Chicoutimi (Napoleão) e da Northern Arizona University (Steinmacher, Gerosa). Financiamento: bolsa do CNPq de Felizardo (302339/2022-1). Texto lido: o PDF inteiro, extraído com pdftotext, inclusive as cinco tabelas; as Figs. 1 e 2 foram lidas pela imagem das páginas. As marcas de Table I (quais critérios cada candidato cumpre) não saíram na extração e foram lidas só pelo que o texto diz delas. Suplemento em https://zenodo.org/records/15284025, não lido.

## A pergunta

Uma revisão sistemática da literatura (SLR) busca cobrir toda a evidência sobre uma pergunta, e na engenharia de software há duas formas principais de busca: em bases, por string, e a bola de neve (*snowballing*), que parte de um conjunto inicial de artigos (*seed set*) e anda para trás (as referências) e para frente (as citações). A busca por string tem custos conhecidos: refinar a string dá trabalho, o resultado traz muito irrelevante e as bibliotecas digitais têm limites técnicos. Os autores citam que a bola de neve responde por 51% dos estudos incluídos em revisões sistemáticas (Greenhalgh e Peacock, 2005); que comparações para atualizar SLRs (Wohlin et al.; Felizardo et al.) acharam as duas abordagens comparáveis nos artigos encontrados, com a bola de neve reduzindo em mais de cinco vezes o número de estudos a analisar; e que estratégias híbridas (bases e bola de neve combinadas) dão resultados melhores (Wohlin et al., 2022).

O ponto fraco é definir o conjunto inicial. Poucos trabalhos tratam disso; em geral se escolhem os artigos mais citados da área ou o resultado de uma busca por palavras-chave da pergunta e seus sinônimos. Wohlin (2014) recomenda um conjunto heterogêneo, diverso em editoras, anos e autores, mas a composição ideal e o grau de diversidade necessário não tinham sido testados. A pergunta do artigo: como a diversidade do conjunto inicial, em editoras, autores e anos, influencia a eficácia da bola de neve em SLRs. As contribuições declaradas: evidência empírica sobre esse efeito, estendendo as diretrizes de Wohlin, e uma ferramenta automatizada que recomenda conjuntos iniciais diversos.

## Trabalhos relacionados

A bola de neve como Wohlin (2014) a descreve: conjunto inicial, em geral vindo de busca em bases; para trás pelas listas de referências; para frente por índices de citação (Google Scholar, Scopus); cada estudo novo passa pelos critérios de inclusão e exclusão; e as duas direções se repetem nos incluídos até não aparecer nada novo. Badampudi et al. acharam bola de neve e busca em base com eficácia comparável, desde que o conjunto inicial seja adequado. Os autores atribuem a Wohlin a indicação de 5 a 10 estudos iniciais, que levariam à convergência em algumas iterações, e dizem que falta pesquisa sobre o número ideal. Felizardo et al. estudaram a bola de neve para frente para atualizar SLRs; Wohlin recomendou para isso o Google Scholar e os estudos primários da revisão original como conjunto inicial; Mourão et al. estudaram estratégias híbridas. As ferramentas existentes de apoio à bola de neve não cobrem o processo inteiro e não tratam da diversidade do conjunto inicial.

## Desenho do estudo

Cinco passos: (1) definir uma abordagem sistemática para montar um conjunto inicial diverso, com uma ferramenta de apoio; (2) escolher duas SLRs para replicar; (3) gerar os conjuntos iniciais diversos dessas SLRs; (4) rodar a bola de neve com eles; (5) avaliar por revocação relativa, precisão e medida F, e comparar com as originais.

**As métricas.** Como nenhuma SLR garante ter achado todos os estudos relevantes, usa-se a revocação **relativa**, calculada contra a soma dos estudos relevantes e únicos achados pela revisão original. A revocação relativa é o número de estudos incluídos na replicação dividido pela união dos incluídos na replicação e na original; a precisão é o número de incluídos dividido pelo total de estudos identificados pela bola de neve (incluídos e excluídos); a medida F é a média harmônica das duas, 2·P·RC/(P + RC). A equipe declara experiência em conduzir SLRs e em pesquisar o método, inclusive variações da bola de neve.

## A abordagem para o conjunto inicial diverso (seção IV e Fig. 1)

O texto descreve sete estágios; a Fig. 1 numera oito.

1. Tirar as palavras-chave da pergunta de pesquisa e acrescentar sinônimos; sinônimos se ligam por OR e palavras-chave distintas por AND, formando uma string que o pesquisador pode refinar. Filtros como ano podem entrar conforme o objetivo.
2. Buscar candidatos a semente em título, resumo e palavras-chave. Os pesquisadores excluíram à mão o que não cumpria os critérios de seleção da SLR original, inclusive o ano: artigos posteriores ao fim do período de busca da original saíram, para a comparação ser justa.
3. Primeira rotulagem, por três critérios gerais: GC1, o título tem ao menos uma palavra-chave da string; GC2, tem ao menos um sinônimo da string; GC3, está entre os cinco mais citados do resultado. Um artigo pode cumprir mais de um, e aparece mais de uma vez na lista.
4. Remover as duplicatas.
5. Segunda rotulagem, por três critérios de diversidade. DC1, autor: quando vários artigos têm o mesmo conjunto de autores, em qualquer ordem, só um recebe o rótulo, para não repetir a mesma equipe. DC2, ano: recebe o rótulo o artigo de um ano que nenhum outro tem; se vários dividem o ano, só o mais citado deles. DC3, veículo: a mesma lógica do ano; o artigo de veículo único recebe o rótulo e, se vários dividem o veículo, só o mais citado. (Na Fig. 1, os rótulos aparecem trocados: DC1 é "local de publicação" e DC3 é "autor".)
6. Consolidar as duplicatas numa lista só, com os vários rótulos de cada artigo.
7. Gerar o conjunto inicial de forma incremental: entram primeiro todos os artigos com os três rótulos de diversidade; se forem menos de cinco, o mínimo que os autores atribuem a Wohlin, entram os com dois rótulos; se ainda faltar, os com um, até chegar ao mínimo. Na Fig. 1, essa etapa é a de número 8, e o conjunto final é o rótulo "Final seed set (DC1, DC2 and DC3)".

A ferramenta, de código aberto e online (https://seed-set-recommendation.onrender.com/), faz cinco coisas: extrai palavras-chave, gera a string com sinônimos, mostra a string, busca artigos no Scopus e recomenda o conjunto inicial pelos critérios de diversidade.

## As duas revisões replicadas (seção V)

Critérios para escolher a SLR: seguiu diretrizes rigorosas (C1); a busca principal foi bola de neve nas duas direções (C2); o processo de definir o conjunto inicial foi descrito (C3); palavras-chave e sinônimos estão explícitos no protocolo, porque a abordagem começa por uma string (C4); o processo de bola de neve foi relatado com transparência (C5); a lista completa de incluídos é pública (C6). A escolha dos temas seguiu a experiência dos autores.

- **SLR1, teste de software.** A busca no Scopus por revisões sistemáticas com bola de neve em teste de software trouxe seis artigos, e só um cumpria os seis critérios: Wnuk e Garrepalli (2018), sobre gestão do conhecimento em teste de software. Na original, o conjunto inicial veio de busca em base, num funil de 2.774 artigos, 63 depois de título e resumo, 32 depois de introdução e conclusão, 16 depois do texto completo, e 13 sementes, escolhidas entre os artigos muito citados e bem referenciados. Foram cinco iterações, com o Google Scholar para as citações; 1.457 candidatos analisados (843 referências e 614 citações) e 35 estudos revisados por pares incluídos, contando as 13 sementes; 12 vieram das referências e 10 das citações.
- **SLR2, colaboração entre indústria e academia.** A busca no Scopus trouxe dois artigos, e só um cumpria os seis critérios: Wohlin et al. (2022), que avaliou estratégias híbridas e é ele mesmo uma replicação da SLR de Garousi et al. (2016). O conjunto inicial veio da busca "industry AND academia AND collaboration AND software AND engineering" no Scopus, de 2010 a 2014: 40 artigos, 15 para texto completo, 9 sementes. No total, 1.942 artigos (40 do Scopus, 839 para trás e 1.063 para frente, cinco rodadas cada), 78 em texto completo e 43 incluídos (9 sementes, 18 para trás, 16 para frente).

## A replicação (seção VI)

**Conjuntos iniciais.** Na SLR1 (Tabela II), sete sementes coincidem com as da original (S1, S3, S4, S6, S7, S9, S11). Os motivos de exclusão que o texto registra: S16 e S17, do mesmo ano (2009) que S9, já escolhido; S18, indisponível; S19, fora dos cinco mais citados (GC3); S20 e S21, sem palavra-chave ou sinônimo no título; S15 e S23, mesmos autores de S6 (e S15 também do mesmo ano, 2015); S24, mesmo veículo (TSE) de S11. Seis sementes ficaram só na original (S2, S5, S8, S10, S12, S13): cinco porque não estão no Scopus, e S2, que está no Scopus, porque a estratégia não a recomendou. S14 é semente só da replicação. O conjunto final tem oito artigos. Na SLR2 (Tabela III), a original tinha nove sementes (S1 a S9) e só S1 coincide; quatro candidatos (S11, S13, S15, S18) saíram pelo critério de inclusão IC1; a replicação ficou com seis sementes, entre elas S12, que na original tinha entrado na primeira rodada para trás. (O texto diz "six unique studies" e lista cinco: S10, S12, S14, S16 e S17.)

**Iterações na SLR1.** Cinco iterações, com citações do Google Scholar numa planilha, filtradas por dois autores com experiência no tema, com os mesmos critérios da original, e comparação com a original só depois de terminar. Iteração 1: 421 artigos, 11 incluídos (9 para trás, 2 para frente). Iteração 2: 548 artigos, 11 incluídos, todos já presentes na original. Iteração 3: 470 artigos, 4 incluídos no texto (a Tabela IV dá 5), um deles novo em relação à original. Iteração 4: 489 no texto (450 na Tabela IV), 1 incluído. Iteração 5: 7 referências e 9 citações, nada incluído; fim. Total: 37 estudos (28 da bola de neve e 9 das sementes), 34 deles também na original; três novos (a semente S14, S19 e BW-N1); um da original (S13) não foi recuperado. A Tabela IV dá 1.944 estudos analisados (900 referências e 1.044 citações).

**Iterações na SLR2.** Seis iterações, com referências e citações extraídas por uma ferramenta de Napoleão et al. (2024), conferidas à mão e checadas no Google Scholar. Iteração 1: 499 artigos, 8 incluídos no texto (9 na Tabela IV), todos vindos de um único estudo. Iteração 2: 368, 13 incluídos; sete das oito sementes usadas levaram a pelo menos um incluído. Iteração 3: 1.145, 12 incluídos; um só estudo respondeu por nove das dez inclusões para frente. Iteração 4: 433, 7 incluídos, todos vindos de três dos dez estudos usados. Iteração 5: 261, 1 incluído. Iteração 6: 23 artigos, nenhum; fim. Os 43 estudos da original foram todos recuperados (42 pela bola de neve e um que era semente das duas), e mais quatro novos. Tabela IV: 2.729 analisados (1.139 referências e 1.590 citações) e 42 incluídos.

## Os números (Tabela V)

| | SLR1 original | SLR1 replicação | SLR2 original | SLR2 replicação |
|---|---|---|---|---|
| Como se montou o conjunto inicial | string (Engineering Village) | processo de diversidade | string (Scopus) | processo de diversidade |
| Artigos analisados para montar o conjunto inicial | 4.832 | 18 | 40 | 10 |
| Sementes | 13 | 8 | 9 | 6 |
| Citações para frente via | Google Scholar | Google Scholar | Google Scholar | Semantic Scholar, ResearchGate e Google Scholar |
| Iterações | 5 | 5 | 5 | 6 |
| Referências analisadas / incluídas | 843 / 12 | 900 / 23 | 899 / 18 | 1.139 / 12 |
| Citações analisadas / incluídas | 614 / 13 | 1.044 / 5 | 1.352 / 16 | 1.590 / 29 |
| Artigos analisados na bola de neve | 6.289 | 1.962 | 2.251 | 2.729 |
| Estudos incluídos | 35 | 37 | 43 | 47 |
| Precisão | 0,006 | 0,019 | 0,018 | 0,016 |
| Revocação relativa | 0,921 | 0,974 | 0,953 | 1 |
| Medida F (relativa) | 0,0119 | 0,0372 | 0,0353 | 0,0315 |

O período limitado é 2003 a 2015 na SLR1 e até 2015 na SLR2. A resposta dos autores à pergunta: a diversidade do conjunto inicial reduz o esforço da bola de neve com baixo risco de perder estudos relevantes, com menos artigos a filtrar e cobertura igual ou maior. Na SLR2, a precisão caiu um pouco (0,016 contra 0,018), o que os autores atribuem à cobertura maior, e a medida F ficou em 0,0315 contra 0,0353.

**Números que divergem dentro do texto, registrados como estão.** O resumo dá revocação relativa de 0,97 e a seção VI-C e a Tabela V dão 0,974. Os artigos analisados na SLR1 aparecem como 1.962 (seção VI-C e Tabela V) e 1.944 (Tabela IV e seção VII). Os 13 de citações incluídas na SLR1 original da Tabela V diferem dos 10 da descrição da seção V-A. Na SLR2, o texto fala em quatro estudos novos na seção VI-B e em "eight new candidate studies, five of which were deemed relevant" na seção VII. O número de sementes da SLR2 aparece como seis (seção VI-A e Tabela V) e como sete ("we used seven seeds instead of the nine") na seção VII.

## Discussão (seção VII)

- **Palavras-chave e iniciantes.** Doutorandos conduzem mais da metade das SLRs (Mendes et al.), e iniciantes sem supervisão tropeçam, entre outras coisas, em montar strings. Os autores propõem a estratégia também para o iniciante: ele insere a pergunta e a ferramenta sugere palavras-chave; na SLR1 bastariam "knowledge management" e "software testing", complementadas por especialistas com OR.
- **Esforço para montar o conjunto inicial.** Na SLR1 original, 4.832 artigos do Engineering Village deram 13 sementes; na replicação, 18 artigos deram 8, mais de 99% a menos de artigos a examinar, com menos trabalho manual e menos risco de erro humano. A ressalva dos autores: esforço não basta como medida, e revocação e precisão também contam.
- **Sementes que não entraram (Fig. 2).** Na SLR1, das seis sementes só da original, cinco não vieram do Scopus; S2, S8 e S10 foram recuperadas na primeira iteração, S5 e S12 na segunda, e só S13 não voltou. Na SLR2, só S1 era comum; S12 foi alcançada na primeira rodada para trás, e todas as outras sementes originais voltaram ao longo das seis iterações, com um conjunto inicial montado a partir de só 10 artigos.
- **Usar uma SLR como semente.** Wohlin et al. dizem que usar uma SLR e seus estudos primários como conjunto inicial é o jeito mais custo-efetivo de buscar evidência nova ao atualizar revisões. Na replicação, isso nem sempre funcionou: o mapeamento sistemático BW3 não levou a nenhum estudo novo relevante.
- **Estudos novos.** Os três estudos da SLR1 que a original não tinha tratam de terceirização de teste e gestão do conhecimento (S14), de geração automática de casos de teste a partir de uma ontologia de requisitos com regras de inferência e algoritmos genéticos (BW-N1) e de representação e mapas de conhecimento em teste de software (S19). Os autores dizem que isso indica que a revisão original pode ter deixado passar evidência importante.
- **Número de sementes.** Na SLR1, uma das oito sementes (S4) não levou a nenhum estudo relevante; na SLR2, só uma semente trouxe estudos na primeira iteração. Os autores dizem que nem toda semente contribui igual e que a eficácia pode depender mais da qualidade que da quantidade, e pedem mais replicações para saber o que pesa (número de citações, cobertura do tema, critérios de diversidade).
- **Diversidade de autores.** A SLR1 começou com 22 autores e a SLR2 com 14. Dos 58 autores da SLR1 original, 50 não estavam no conjunto inicial. A semente S6 levou a BW3 (mesmo grupo de autores) e a BW6 (mesma revista); BW9, FW3 e FW5 dividem pelo menos um autor com a semente de onde vieram, o que os autores chamam de padrão de continuidade de autoria. Na SLR2, dos 123 autores únicos da original, só dois (Petersen e Runeson) estavam nos conjuntos iniciais das duas.
- **Diversidade de anos.** O conjunto inicial da SLR1 cobria 2007, 2009, 2011, 2013 e 2015; os incluídos foram de 2003 a 2015 (SLR1) e de 1999 a 2014 (SLR2). Estudos recentes refletem tendências e servem para evidência atual ou emergente (como na atualização de SLRs); referências antigas ajudam a achar trabalhos anteriores e do mesmo contexto histórico.
- **Diversidade de veículos.** A SLR1 começou com oito veículos e terminou com 29; a SLR2 começou com sete e terminou com 25.
- **Quando parar.** Na SLR1, os novos incluídos caíram a cada iteração (11, 11, 5, 1); mesmo com só um na quarta, os autores rodaram uma quinta para confirmar que não havia mais nada, e esse foi o critério de parada; o mesmo raciocínio valeu para a SLR2. Os autores chamam isso de abordagem conservadora, alinhada à orientação de iterar até não haver estudos novos.

**Lições que os autores tiram:** de seis a oito sementes foram adequadas, com convergência em cinco ou seis iterações; a diversidade das sementes em autores, anos e veículos apareceu também no conjunto final; a estratégia "simplificou seis vezes" a definição das sementes; o Google Scholar serve à bola de neve para frente, mas não deixa baixar as citações automaticamente, e a ferramenta de Napoleão et al. ajudou na SLR2, com conferência manual, porque usa as APIs do ResearchGate e do Semantic Scholar em vez do Google Scholar, por limites impostos pelo Google.

## Ameaças à validade e conclusão

- A escolha das SLRs poderia favorecer a estratégia, mas seguiu critérios sobre o conteúdo das revisões. O tema não era central, porque o objetivo era avaliar a bola de neve, mas os pesquisadores precisavam dominar o tema para incluir e excluir bem. Para o viés individual de seleção, dois pesquisadores avaliaram todos os artigos de forma independente.
- Validade interna: as citações vieram do Google Scholar (o rastreamento de citações dele), e as diretrizes de Wohlin foram seguidas à risca. A bola de neve supõe que os outros estudos relevantes estão indexados como as sementes, o que se confirmou na replicação; mas estudos relevantes podem estar fora das bases acadêmicas ou na literatura cinzenta, e o Google Scholar foi usado para mitigar isso, com a citação de Felizardo et al. de que uma base genérica basta para achar a maioria dos estudos.
- Limitação declarada: a estratégia se baseia só no Scopus, então estudos fora dele não entraram nos candidatos; o trabalho futuro sugerido é incorporar Web of Science, IEEE Xplore e ACM Digital Library.
- Conclusão: a contribuição é explorar a estratégia de diversidade para montar conjuntos iniciais, com uma replicação detalhada para transparência. Os autores dizem que os resultados não são definitivos e pedem novos estudos, inclusive experimentos formais, que os confirmem ou os contestem.
