---
titulo: "Evaluating Severity Rating Scales for Heuristic Evaluation (Herr, Baumgartner e Gross, CHI 2016, Late-Breaking Work)"
tipo: paper
autor: "Sascha Herr, Nina Baumgartner, Tom Gross (Human-Computer Interaction Group, Universidade de Bamberg)"
url: "https://cml.hci.uni-bamberg.de/~gross/publ/chi16_herr_et_al_severity_rating_scales__proceedings.pdf"
publicado_em: 2016-05-07  # CHI'16 Extended Abstracts, 7 a 12 de maio de 2016, San Jose; DOI 10.1145/2851581.2892454
capturado_em: 2026-11-04
areas: [agent-engineering]
tags: [severity-rating, heuristic-evaluation, rating-scales, evaluator-effect, psychometrics, usability]
licenca: "ACM, copyright dos autores (aviso de permissão para uso pessoal ou em sala de aula, sem fim comercial); sem licença aberta, por isso só a ficha"
---

# Herr, Baumgartner e Gross (CHI 2016): três escalas de gravidade na avaliação heurística

Ficha em palavras próprias de um resumo estendido de 4 páginas (Late-Breaking Work), lido no PDF do site do grupo, em 2026-11-04. O texto integral não entra (protegido). Lacunas da fonte ficam como lacunas.

## O problema que o artigo apresenta

Na avaliação heurística, especialistas inspecionam uma interface e também atribuem gravidade a cada problema achado, para decidir a ordem de correção. Na prática, as notas dos especialistas divergem muito entre si, fenômeno que o artigo chama de efeito do avaliador (cita Hertzum, 2006), e isso levanta dúvida sobre a exatidão das notas. Os autores dizem que não há padrão comum para o processo de nota. Sobre a saída rápida de discutir as notas em grupo ou notar em conjunto, afirmam que ela é falha, porque efeitos sociais como o domínio de alguém (groupthink) prejudicam a exatidão.

## Defeitos que apontam na escala de Nielsen

A escala de Nielsen tem cinco pontos: 0 não é problema; 1 cosmético; 2 menor; 3 maior; 4 catástrofe de usabilidade. Pelo critério da psicometria, o artigo lista cinco limitações:

1. A escala é desbalanceada (só um lado tem opções), o que, dizem, enviesa as respostas para o lado com mais pontos.
2. "Não é problema" não faz parte conceitualmente da gravidade e pode atrapalhar o processamento cognitivo.
3. Há evidência (Preston e Colman, 2000) de que entre cinco e sete pontos garantem confiabilidade, validade e poder de discriminação; para o construto gravidade, a escala de Nielsen entrega quatro.
4. Gravidade é multidimensional (Nielsen manda ponderar frequência, impacto e persistência, e acrescenta o impacto de mercado), mas na prática se dá uma única nota geral.
5. Falta esclarecer quais fatores compõem a gravidade; pode haver mais do que os discutidos.

## As três escalas comparadas

- **Nielsen (N):** 5 pontos, unidimensional.
- **Do praticante (P):** 3 pontos (menor, moderado, maior), unidimensional. Veio de uma pesquisa preliminar: cinco profissionais de usabilidade entrevistados e uma pergunta postada em fóruns da área. Muitos citam a escala de Nielsen, mas muitos usam a sua própria, de três categorias, focada em simplicidade e rapidez. O artigo não informa quantas respostas os fóruns deram.
- **De fatores individuais (IF):** 5 pontos (diferencial semântico de "muito baixo" a "muito alto"), multidimensional, com sete fatores estimados um a um e depois somados (escala somatória): frequência (com que frequência o problema ocorre na população); dificuldade (para um usuário superá-lo); impacto no fluxo de trabalho; persistência (com que insistência o usuário esbarra nele); frustração; impacto de mercado (na popularidade do produto); esforço de correção (para os desenvolvedores). "Não é problema" sai da escala e vira uma escolha à parte.

Vantagens que os autores atribuem à IF: tornar explícito o julgamento de cada fator deixa o avaliador mais ciente dos próprios critérios (o que, dizem, deve melhorar a exatidão), e os dados extras servem de base para a discussão e para a priorização dos desenvolvedores. Escalas com vários itens, na teoria, são mais confiáveis do que um indicador único (citam Shevlin et al., 1997).

## O estudo

- Questionário online (plataforma Soscisurvey), 103 participantes que concluíram, recrutados sobretudo em comunidades de usabilidade, sem restrição de amostra; 18 a 56 anos (média 31,9); 48% mulheres; experiência média em IHC de 6,9 anos. Por experiência: 36 novatos (um ano ou menos), 34 intermediários, 33 especialistas (dez anos ou mais).
- 32 casos de problema, inventados a partir de projetos de consultoria dos autores, cada um com título, descrição e captura de tela.
- Delineamento entre sujeitos: cada participante foi sorteado para uma só escala; ordem dos casos aleatória.
- Verdade de referência ("ground truth"): dois especialistas (um da academia, um da prática, ambos com mais de 20 anos de IHC) notaram os 32 casos com as três escalas. O artigo não diz como as duas notas foram combinadas.
- As notas foram tratadas como dados intervalares e padronizadas de 0 a 100 pelo método POMP.

## Resultados

- **Nota média por escala:** N 64,0 (DP 9,7; n=39); P 54,9 (DP 12,1; n=34); IF 55,8 (DP 7,8; n=30). ANOVA: F(2,100)=8,99, p<0,001; Tukey: a escala de Nielsen dá notas mais altas que as outras duas (p=0,001 e p=0,004). Refazendo a análise sem as respostas "não é problema", a diferença deixou de ser significativa, o que os autores tomam como confirmação do defeito 2. Eles observam que a média num relatório pode superestimar a gravidade à primeira vista.
- **Desvio em relação à referência (menor é mais exato):** N 28,1 (DP 6,7); P 39,3 (DP 8,8); IF 23,4 (DP 2,5). Kruskal-Wallis H(2)=49,6, p<0,001; todas as comparações par a par significativas (p<0,001). Ordem: IF mais exata, N em segundo, P pior. O desvio-padrão baixo da IF sugere, nas palavras deles, maior precisão e menos discordância entre avaliadores.
- **Tempo médio por caso:** N 35,8 (DP 25,7); P 28,4 (DP 17,0); IF 46,8 (DP 23,5); a unidade não aparece no texto. ANOVA F(2,90)=4,66, p=0,012; só a diferença entre P e IF é significativa (p=0,009). Dez participantes saíram por valores atípicos (pausas). A IF exige sete notas por caso e, ainda assim, só levou 30% mais tempo que N e 64% mais que P.
- **Preferência** (depois de ver a descrição das três): Nielsen 47% (48 pessoas), IF 37% (38), do praticante 16% (17). 42% escolheram a escala que haviam usado. Razões livres: a de Nielsen é estabelecida, comum e fácil; a do praticante é rápida, mas grosseira demais para quem quer julgamento mais fino; a IF é detalhada e informativa, mas demorada e difícil de pegar o ritmo, porque é preciso decorar as dimensões.

## Conclusões dos autores

A escala aplicada influencia as notas, com superestimação na de Nielsen; a IF foi a mais exata, ao custo de cerca de 30% mais tempo, troca que eles acham que pode valer a pena; a mais preferida foi a de Nielsen. Dizem que seria errado complicar demais o método, que é barato, mas que ajustes na escala melhoram exatidão e informação com pouco custo de tempo. Pesquisa futura: seguir investigando a multidimensionalidade da gravidade, montar um arcabouço que guie os avaliadores e investigar se o peso de cada fator muda conforme a área e a finalidade do produto.

## O que a fonte não diz

Não mede concordância entre avaliadores com coeficiente algum (kappa, alfa ou similar); a comparação é com dois especialistas e por desvio médio, e o próprio texto lê o desvio-padrão baixo como "sugestão". Não dá o número de respostas dos fóruns na pesquisa preliminar, nem a unidade do tempo, nem o método de combinar as duas notas de referência. Os casos são cenários criados pelos autores, não problemas observados em sessões de teste com usuários.
