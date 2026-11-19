---
titulo: "A review of Lawshe’s method for calculating content validity in the social sciences"
tipo: paper
autor: "Marcela Romero Jeldres, Elisabet Díaz Costa, Tarik Faouzi Nadim"
url: "https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2023.1271335/full"
publicado_em: 2023-11-20
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [content-validity, content-validity-ratio, content-validity-index, lawshe, expert-panel, critical-values, binomial-test, bayesian-methods, instrument-development, education-assessment]
licenca: "CC BY, na própria página"
---

# Romero Jeldres, Díaz Costa e Faouzi 2023 (Frontiers in Education): revisão do método de Lawshe

Ficha na ordem do artigo. Autores da Universidade Metropolitana de Ciências da Educação e da Universidade de Santiago do Chile; Frontiers in Education, vol. 8, artigo 1271335, seção Assessment, Testing and Applied Measurement, classe "Methods"; DOI 10.3389/feduc.2023.1271335; recebido em 02/08/2023, aceito em 31/10/2023, publicado em 20/11/2023. Área: medida em educação e ciências sociais. As equações, ausentes do texto corrido da página, foram lidas no MathML da própria página.

## Pergunta

Mostrar a utilidade do método de Lawshe (1975) para investigar validade de conteúdo por julgamento de especialistas, revisar seu uso histórico nas ciências sociais, analisar por hipóteses matemáticas as críticas principais, e testar num instrumento sobre as competências pedagógicas de estudantes de formação inicial de professores no Chile.

## Enquadramento

- **Fontes de validade:** conteúdo, processos de resposta, estrutura interna, relação com outras variáveis e consequências da avaliação (Eignor, 2013; Plake e Wise, 2014).
- **Dois caminhos para analisar conteúdo:** métodos por julgamento de especialistas e métodos derivados da aplicação do instrumento (Pedrosa e outros, 2014; Urrutia e outros, 2014). O artigo fica no primeiro.
- **O que se coleta:** evidência sobre a definição do domínio dos itens (representatividade) e a adequação do conteúdo (relevância).
- **Antes de começar** (Urrutia e outros): decidir o que pode ser medido e quantos especialistas, com que características.
- **O número de juízes depende da análise prevista:** deve alcançar o mínimo para o teste estatístico valer (Tristán-López, 2008).
- **O qualitativo não basta** para estabelecer o grau de concordância sobre a adequação do item (Sireci, 1998).

## A proposta de Lawshe

Cada juiz com expertise no construto avalia os itens sozinho, em duas categorias, essencial e não essencial. Lawshe sugere concordância mínima de 50% entre juízes e dois índices.

- **CVR (content validity ratio, razão de validade de conteúdo):** mede a concordância do painel sobre um item. Na forma do artigo, equação (1): CVR = (n_e − n_ne) / N, com n_e os que concordam, n_ne os que discordam e N = n_e + n_ne.
- **CVI (content validity index, índice de validade de conteúdo):** a média dos CVR dos itens que formam o instrumento final. Na forma de Lawshe, CVI_accepted = soma dos CVR_j / m, com m o número de itens cujo CVR passa do crítico.

Lawshe publicou uma tabela de CVR crítico por número de juízes.

## As críticas e as tabelas concorrentes

- **Lawshe (1975).** Usou significância de 0,05 sem dizer qual teste aplicou; para os autores, esta é a crítica mais forte ao trabalho dele. Para Tristán-López, a fórmula não se aplica a menos de cinco juízes.
- **Polit e outros (2007).** Sugerem CVR crítico de 0,78 para três juízes ou mais. Os autores recusam para as ciências sociais: baixo demais para cinco juízes ou menos, perde validade discriminante, e em seis ou mais fica perto demais do valor de três, contra os estudos que mostram o crítico caindo com o tamanho do painel.
- **Tristán-López (2008).** Refaz a tabela e declara o teste: qui-quadrado com α = 0,1 e 1 grau de liberdade. Ganha um cálculo para painéis menores; os autores não veem justificativa para subir o erro admissível a 0,1. Ayre e Scally (2014) consideram o qui-quadrado inadequado, porque os dados têm distribuição binomial.
- **Wilson e outros (2012).** Nova tabela pela aproximação normal da binomial, com o teorema central do limite e juízes independentes. Só vale com painel grande, difícil de reunir.
- **Ayre e Scally (2014).** Teste binomial exato, calculado em STATA. Como há duas categorias, cada juiz segue uma Bernoulli com p = 0,5 e, com juízes independentes, o total segue uma binomial. Hipótese nula: n_e ≤ N/2, com significância de 0,05; n_cr é o mínimo de concordantes para o item contar como essencial. Os autores chamam essa alternativa de apropriada ao modelo de Lawshe. O texto escreve p = 0,5 numa frase e p = 0,05 na seguinte.
- **Baghestani e outros (2019).** Método bayesiano: hipótese H0 p ≤ 0,5 contra H1 p > 0,5, com p realização de uma variável X de distribuição desconhecida. A priori de X é Beta(α, β), com α = β = 1 (modelo de Berger, 2013). Rejeita-se H0 quando a integral de 0 a 0,5 de p^(N_e+α) (1−p)^(N−N_e+β) dp fica abaixo de 0,05, e N_e é o menor valor que rejeita. Ganho: reduzir juízes mantendo crítico aceitável. Essa vantagem, escrevem os autores, só aparece depois de corrigir um erro de cálculo que acharam no trabalho original, ligado ao uso da função `pbinom` do pacote `stats` do R.

## A tabela 1 e a divergência no N = 7

CVR crítico por N ("at a confidence level of .05", na legenda). Os autores dizem ter comparado em R os resultados de Lawshe, Tristán-López e Ayre e Scally. O artigo traz de N = 2 a N = 40; aqui, de 4 a 15 e os N maiores com valor na coluna de Lawshe.

| N | Binomial exato (Ayre e Scally) | Qui-quadrado (Tristán-López) | Lawshe | Bayesiano (Baghestani) |
|---|---|---|---|---|
| 4 | sem valor | 1,00 | sem valor | 1,00 |
| 5 | 1,00 | 1,00 | 0,99 | 1,00 |
| 6 | 1,00 | 1,00 | 0,99 | 1,00 |
| 7 | 1,00 | 1,00 | 0,99 | 0,71 |
| 8 | 0,75 | 0,75 | 0,75 | 0,75 |
| 9 | 0,78 | 0,78 | 0,78 | 0,78 |
| 10 | 0,80 | 0,80 | 0,65 | 0,60 |
| 11 | 0,64 | 0,64 | 0,59 | 0,64 |
| 12 | 0,67 | 0,67 | 0,56 | 0,50 |
| 13 | 0,54 | 0,69 | 0,54 | 0,54 |
| 14 | 0,57 | 0,57 | 0,51 | 0,57 |
| 15 | 0,60 | 0,60 | 0,49 | 0,47 |
| 20 | 0,50 | 0,50 | 0,42 | 0,40 |
| 25 | 0,44 | 0,44 | 0,37 | 0,36 |
| 30 | 0,33 | 0,40 | 0,33 | 0,33 |
| 35 | 0,31 | 0,37 | 0,31 | 0,31 |
| 40 | 0,30 | 0,35 | 0,29 | 0,30 |

Para N = 2 e N = 3, nenhuma coluna tem valor. A coluna de Lawshe só tem valor de N = 5 a 15 e em 20, 25, 30, 35 e 40.

**Tabela e prosa divergem no N = 7.** A prosa diz que, para Lawshe, o CVR crítico de um painel de sete é igual ou maior que 0,75. A tabela do mesmo artigo dá, na coluna de Lawshe, 0,99 para N = 7, e 0,75 para N = 8. O artigo não comenta a diferença.

**Duas outras frases a conferir com a tabela.** A prosa diz que os três métodos coincidem com nove juízes ou menos e divergem de dez em diante; na tabela, a coluna de Lawshe traz 0,99 onde as outras duas têm 1,00 em N = 5, 6 e 7. E os resultados dizem que o crítico é função decrescente de N; na coluna do binomial exato, os valores sobem de 0,75 a 0,80 entre N = 8 e N = 10, e de 0,64 a 0,67 entre N = 11 e N = 12.

**O que os autores tiram da comparação.** O binomial é mais preciso que o qui-quadrado, e propor outro índice de CVR não mudaria a decisão sob o binomial exato. Tristán-López serve de alternativa quando o painel tem quatro juízes (tabela 1). O bayesiano reduz o painel e, como o qui-quadrado, permite avaliar com quatro. A figura 1 compara Lawshe, Tristán-López e Ayre e Scally; a figura 2, Ayre e Scally e Baghestani.

## O CVI: qual soma usar, e qual corte

- **Crítica ao critério de Lawshe.** Com a conta de Lawshe, o CVI do instrumento completo, com itens aceitos e recusados, nunca passa do CVI só dos aceitos; os autores chamam o critério de exagero.
- **Sem corte único.** CVI crítico de 0,7 (Tilden e outros, 1990), 0,8 (Davis, 1992) e 0,5 (Tristán-López, 2008).
- **CVR ou CVI.** Gilbert e Prion (2016): depende da orientação do estudo. Aqui o objetivo era a concordância sobre um conjunto de itens, para interpretar a perspectiva teórica e melhorar o instrumento, e os autores ficam com o CVI.
- **Combinação com análise fatorial.** O índice de Lawshe, menos exigente por olhar só os aceitos, foi combinado com a validade de construto por análise fatorial confirmatória (CFA), que verifica confiabilidade dos itens e unidimensionalidade dos fatores com todos os itens: rho de Joreskög, variância extraída, contribuição fatorial e qui-quadrado sobre graus de liberdade. Com isso, dizem, reduziram o viés dos avaliadores.
- **Cultura.** Romero-Jeldres e Faouzi (2018): concordância entre juízes é complexa por elementos culturais. Em competências pedagógicas, os avaliadores chilenos se ajustaram ao marco regulatório do país, e os alemães divergiram nos marcos teóricos.

## Método do experimento

- **Itens:** vêm de pesquisa anterior (Romero-Jeldres e Faouzi, 2018; operacionalização no apêndice A do material suplementar). O instrumento tem 71 itens.
- **Condições de Guion (1977), parcialmente asseguradas, dizem os autores:** conteúdo do domínio ancorado em comportamento de significado aceito; relevante para os objetivos; bem amostrado; avaliadores qualificados concordando com a amostragem; respostas observadas e avaliadas de forma confiável.
- **Julgamento de especialistas:** opinião informada de pessoas com experiência e reconhecidas como qualificadas (Cabero e outros, 2013). O problema de pesquisa define o perfil; requisitos: formação, experiência, disposição com o tema e abertura para rever o juízo inicial.
- **Painel:** Akins e outros (2005) sugerem ao menos sete para painel pequeno. Os autores identificaram 14 avaliadores nas regiões da amostra, contataram pessoalmente e por e-mail, e recrutaram até oito confirmarem. **O artigo tem três números aqui:** 14 identificados, oito confirmados, e sete na tabela 2 e na frase sobre o exemplo ("seven judges who participated").
- **Quem são os sete (tabela 2):** quatro mulheres e três homens, de 34 a 65 anos, professores de formação, com mestrado, a maioria com doutorado (um sem, um em andamento), de Santiago, Concepción, Antofagasta e um de alcance nacional.
- **Cálculo:** CVR de cada item pelo método bayesiano; CVI pelo modelo de Lawshe, comparado ao corte de Tilden. Sobre a escolha do corte, escrevem: "This criterion was chosen for the convenience of maintaining all the items." A equação dessa etapa é CVI = (1/n) soma de CVR_j, com n o total de itens.

## Resultados

- **Itens:** 56 de 71 passaram de 0,71, o crítico bayesiano da tabela 1 para N = 7.
- **CVI com todos os itens:** 0,77, aceito pelo corte de 0,7 de Tilden, e todos os itens foram mantidos por dimensão.
- **O caso CVR = 0.** Pedrosa e outros veem problema quando metade do painel marca relevante e metade irrelevante. Os autores respondem com um limite: pela aproximação normal, CVR_cr = (1 + z√N)/N = 1/N + z/√N, com z normal padrão; com n_e = N/2 + ε, ε inteiro fixo maior que zero, o CVR tende a zero quando N cresce. Daí: "an item with a CVR value close to 0 would be acceptable if there are many panelists."

## Discussão e conclusões dos autores

- Lawshe tem vantagens sobre as alternativas (Divayana e outros, 2020) e, na expressão do artigo, precisa de mais valores críticos para o cálculo do CVR e para aceitar o CVI; quem usa acaba tendo de escolher entre as propostas.
- Ficam com Baghestani e outros, por ser adequado a variáveis de distribuição desconhecida.
- **A recomendação central:** reconsiderar a soma de todos os CVR no cálculo do CVI, em vez de só os acima do crítico, porque essa conta discrimina mais. O resumo escreve "critical Content Validity Index (CVI)" nesse ponto, e a discussão, "critical CVR".
- **Métodos mistos:** abrir espaço na matriz de avaliação para contribuições dos especialistas (Urrutia e outros), para colher mais que pertinência e relevância e entender o quadro de referência de quem responde.
- **Sobre o CVR = 0:** o piso de 50% de Lawshe resolve a objeção de Pedrosa; e o crítico tende a zero com N muito grande.
- **Complementos:** há tendência a somar outras estratégias aos índices para contornar os limites. Pedrosa e outros sugerem aplicar os itens relevantes a participantes e usar a Teoria da Generalização nas respostas, para medir as fontes de erro.

## Limites que aparecem no artigo

Experimento com um instrumento e um painel de sete; condições de Guion só em parte; corte de CVI escolhido por conveniência. O artigo não traz uma seção de limitações.

## Tudo o mais que ensina

- Conteúdo como base da validade de construto ou como algo próprio de um tipo de teste: Pedrosa e outros (2014) revisam as concepções, e a essência, dizem os autores, ficou estável.
- O trabalho de avaliador é laborioso e pouco reconhecido na academia, e isso dificulta recrutar.
- Figura 1: crítico por N em Lawshe, Tristán-López e Ayre e Scally; figura 2: binomial exato contra bayesiano.
- Declaração de financiamento: nenhum; os agradecimentos citam financiamento da DIUMCE (projeto PMI-EXA-PNNI 01-17).
- Referências para o crítico: Lawshe (1975); Wilson, Pan e Schumsky (2012); Ayre e Scally (2014); Baghestani, Ahmadi e Meshkat (2019); Tristán-López (2008).
