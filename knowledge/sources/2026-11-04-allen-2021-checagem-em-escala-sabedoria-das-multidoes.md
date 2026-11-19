---
titulo: "Scaling up fact-checking using the wisdom of crowds"
tipo: paper
autor: "Jennifer Allen, Antonio A. Arechar, Gordon Pennycook, David G. Rand"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC8442902/"
publicado_em: 2021-09-01
capturado_em: 2026-11-04
licenca: "Creative Commons Attribution 4.0 (CC BY), escrita na página do PMC: 'Distributed under a Creative Commons Attribution License 4.0 (CC BY)'; a mesma linha diz 'exclusive licensee American Association for the Advancement of Science' e traz o ano 2019 no copyright; o integral está na url"
areas: [journalism, agent-engineering]
tags: [fact-checking, wisdom-of-crowds, inter-rater-agreement, fact-checker-disagreement, crowd-ratings, misinformation, ground-truth]
---

# Allen et al. 2021 (Science Advances): checadores profissionais discordam entre si, e uma multidão pequena de leigos chega perto da média deles

Ficha em palavras próprias; o texto integral (CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Science Advances 7(36): eabf4393, DOI 10.1126/sciadv.abf4393; lido na cópia do PMC (PMC8442902) em 2026-11-04. Experimento que compara as notas de três checadores profissionais com as de 1.128 leigos americanos para 207 artigos que o Facebook sinalizou para checagem.

## Desenho

- **Artigos:** o Facebook enviou 796 URLs, amostradas por algoritmo com excesso de conteúdo cívico ou de saúde, com maior probabilidade prevista de ser falso ou enganoso (comentários de descrença, páginas reincidentes) e/ou viral. Quatro assistentes de pesquisa tiraram 299 sem afirmação de fato no título ou na primeira frase (lede) e foram descartadas 34 URLs mortas; dos 463 restantes sortearam-se 207. Classificação do Facebook: 109 políticos, 43 de crime e tragédia, 22 sociais, 17 de saúde. Os autores admitem não ter conseguido auditar a seleção do Facebook.
- **Checadores:** três freelancers contratados no Upwork, de out/2019 a jan/2020, depois de triagem e tarefa-teste, com mais de 2.000 horas somadas de checagem. Primeiro checaram 20 artigos, cada um com até 30 minutos de pesquisa; os pesquisadores deram retorno individual e discutiram onde havia desacordo grande (o que revelou desacordos fundamentados, não mal-entendidos ou desleixo); depois cada um avaliou o restante dos 207 sozinho, sem conversar. Leram o artigo inteiro, pesquisaram a afirmação central e registraram evidências.
- **Leigos:** 1.246 residentes nos EUA recrutados no Amazon Mechanical Turk em fevereiro de 2020; 118 não terminaram; 1.128 na amostra (idade média 35, 54,3% preferem o Partido Democrata). Pagamento fixo de US$ 2,25, sem prêmio por concordar com os checadores. Cada um viu o título e a primeira frase de 20 artigos sorteados dos 207 (cerca de 100 avaliações por artigo; mínimo 79, máximo 137), sem pesquisar (tempo médio 35,7 s por artigo). Metade viu também o domínio do editor ("condição com fonte"). Depois fizeram um teste de reflexão cognitiva e um de conhecimento político.
- **Escalas (iguais para os dois grupos):** uma classificação categórica (verdadeiro, enganoso, falso, não sei) e sete notas de 1 a 7 (descreve evento que aconteceu, é verdadeiro, preciso, confiável, digno de confiança, objetivo, sem viés), tiradas em média (alfa de Cronbach 0,96).
- **Multidão equilibrada politicamente:** para cada tamanho k de 2 a 26, mil repetições sorteando k/2 democratas e k/2 republicanos (com reposição) por artigo, e a média das notas.
- **Duas análises:** (1) correlação, entre artigos, da média da multidão com a média dos checadores; (2) AUC de um classificador que usa a nota média da multidão para prever se o veredito modal dos checadores é "verdadeiro" (1) ou qualquer outra coisa (0: falso, enganoso ou impossível de determinar).

## Resultados

**Os checadores entre si.** Correlação média entre as notas agregadas dos três: r = 0,62 (faixa 0,53 a 0,81). Nas classificações categóricas: os três deram o mesmo veredito em 49,3% dos artigos; dois de três em 42,0%; os três diferentes em 8,7%; kappa de Fleiss 0,38 ("justo"). Os autores apontam que pelo menos dois de três concordaram em mais de 90% dos artigos, e que a correlação está longe de 1. Em política, r = 0,56 (109 URLs); fora de política, 0,69 (98 URLs). Outros dados citados: FactCheck.org contra PolitiFact em escalas ordinais, r = 0,66; outro estudo achou concordância entre agências conhecidas tão baixa quanto 0,47; quatro jornalistas profissionais (de uma bolsa para jornalistas de meio de carreira) com os mesmos artigos tiveram r médio de 0,67 entre si e 0,81 com a média dos checadores do Upwork. Os autores concluem que não se deve depender de um único checador para certificar veracidade, e que a verdade "muitas vezes não é uma classificação simples de preto e branco".

**Multidão contra checadores (correlação).** Com poucos leigos por artigo, a correlação com os checadores já não difere de forma significativa da correlação entre os checadores: a partir de k = 8 na condição com fonte (r = 0,58) e k = 12 sem fonte (r = 0,57). Na condição com fonte, a partir de k = 22 (r = 0,66) a multidão passa a correlacionar com os checadores mais do que eles entre si. Mostrar a fonte aumentou a correlação de 0,03 a 0,06, só significativo para k de 24 ou mais. A multidão concorda com os checadores tanto em política quanto fora, e, como os checadores concordam menos em política, ela se sai especialmente bem contra o parâmetro dos checadores nesse tema.

**Multidão como classificador (AUC).** Com cerca de 26 leigos o AUC estabiliza em 0,86 (com fonte) e 0,83 (sem fonte). Leitura dada pelos autores: com uma multidão de 26, em 86% das vezes o artigo verdadeiro recebe nota maior que o não verdadeiro, sorteando um de cada. Nos 102 artigos em que os três checadores concordaram, o AUC foi de 0,90 a 0,92; nos 105 com desacordo, de 0,74 a 0,78. Os autores tiram que a previsão perfeita da multidão pode ser impossível dado o desacordo dos checadores e a dificuldade da tarefa. Acurácia fora da amostra com limiar único: 74,2% num conjunto só de artigos não unânimes, 82,6% num só de unânimes; o limiar ótimo é conservador (a nota média precisa ficar um pouco acima do ponto médio da escala para chamar de verdadeiro).

**Quem acerta mais.** Democratas concordam mais com os checadores que republicanos (p < 0,001, inclusive em artigos não políticos); maior conhecimento político e maior reflexão cognitiva também aumentam a concordância. Mas restringir a multidão à metade melhor de cada grupo não aumentou significativamente o desempenho de uma multidão grande; reduz, porém, quase à metade o número de pessoas necessário para atingir a correlação média entre os checadores. Para os autores, a presença de baixo desempenho não correlacionado cancela ruído e amplifica o sinal dos melhores.

**Custo.** Cada nota levou em média 35,7 s, com pagamento de US$ 0,15 por minuto (1,2 vez o salário mínimo federal); com multidões de 10 pessoas, cerca de US$ 0,90 por artigo.

## O que os autores recomendam ou ressalvam

- Usar a nota contínua da multidão como sinal de ranqueamento do feed (rebaixar na proporção da nota), em vez de um corte seco entre verdadeiro e falso.
- A multidão não substitui os checadores profissionais; é um componente de um sistema que combina aprendizado de máquina, notas de leigos e julgamento de especialistas. O nível de desacordo entre checadores levanta dúvida sobre sistemas que dão a decisão a um único checador, ou que usam as notas de um só como verdade-terreno em modelos supervisionados.
- Ressalvas: indivíduos isolados erram com frequência, mesmo quando a multidão vai bem; só se leram título e primeira frase; o Facebook pode ter fornecido um conjunto enviesado (replicaram com um conjunto publicado, escolhido por pesquisadores, e a multidão foi melhor ali, o que indica que o conjunto do Facebook era mais difícil); a amostra não é representativa dos EUA; o equilíbrio democratas e republicanos é peculiar ao contexto americano, e é preciso evitar que maiorias certifiquem inverdades sobre minorias; a generalização para outros países e para temas de fatos que mudam rápido (COVID-19) está em aberto. Veem a possibilidade de manipulação por partidários como pouco provável, porque o viés se cancelaria na multidão equilibrada.

## O que a fonte não diz

Não diz se o veredito modal dos três checadores está certo (usa-o como referência, e mostra que ele próprio tem 8,7% de artigos com três vereditos diferentes). Não testa multidões com leitura do artigo inteiro ou pesquisa. Não diz como definiu o veredito modal nos artigos em que os três checadores deram vereditos diferentes.
