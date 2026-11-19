---
titulo: "Video Design and Product-Link Clicking in Short-Video Commerce: Guide-Oriented Content, Shot-Duration Diversity, and Algorithmic User–Content Fit"
tipo: paper
autor: "Ziqi Zhao (Zhejiang University) e Yan Liu (NingboTech University; Ningbo Institute for Future Industry Development and Security; Hong Kong Polytechnic University)"
url: "https://www.mdpi.com/0718-1876/21/10/381/pdf"
publicado_em: 2026-10-20   # primeira página do PDF: "Received: 16 July 2026 Revised: 29 September 2026 Accepted: 13 October 2026 Published: 20 October 2026"
capturado_em: 2026-11-12
licenca: "CC BY 4.0 (nota de copyright da primeira página do PDF: 'Copyright: © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license.', com link para creativecommons.org/licenses/by/4.0/); o integral está na url"
areas: [generative-media, content-design]
tags: [short-form-video, shot-length, pacing, editing-rhythm, explainer, cognitive-load, fluency, complexity, personalization, recommendation-feed, social-commerce, observational-study]
---

# Zhao e Liu: vídeo instrucional, mistura de durações de plano e clique no link do produto

Ficha de estudo: as seções seguem a ordem do artigo (resumo, 1 a 6, declarações e apêndice A), com o método em passos, cada medida com a forma como foi construída, os números nas tabelas de onde saem, e as ressalvas e os limites que os autores declaram. O texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Artigo do *Journal of Theoretical and Applied Electronic Commerce Research* (JTAER) 21(10):381, DOI https://doi.org/10.3390/jtaer21100381, baixado em PDF em 2026-11-12 pelo CDN da MDPI (mdpi-res.com), porque o PDF em mdpi.com deu 403 no curl. O PDF, que sustenta o integral, está em a pasta da rodada desta cópia: sha256 do arquivo (hash omitido) (27 páginas; data de criação nos metadados, 2026-10-20). Lido no texto extraído do PDF, a cópia de trabalho; a extração embaralha as colunas das tabelas, e as linhas das Tabelas 2, 3, 4, 9 e A3 foram conferidas pela posição das palavras no PDF. Sem captura na Wayback (consulta à API de disponibilidade do archive.org em 2026-11-12, para a página e para o PDF). Título conferido na primeira página. **Licença:** CC BY, na nota de copyright da primeira página, com o link para a versão 4.0. **Cobertura:** o texto das 27 páginas, do resumo ao apêndice A (Tabelas A1 a A7); as referências, só percorridas; as Figuras 2, 3 e 4 são imagem e não foram vistas (da Figura 1, só os rótulos que estão no texto). **Quem fala:** dois pesquisadores de universidades chinesas, com dados de uma plataforma de comércio eletrônico chinesa que o artigo não nomeia; os dados são proprietários e não se compartilham. Sem conferência automática nem lado a lado: a licença permite a cópia, e o integral não vem neste repositório e se lê na url do frontmatter (`README.md` desta pasta, item 1).

## Em uma frase

Num feed de recomendação de uma grande plataforma chinesa, em 66.244 exibições de vídeos de produtos para a casa (julho e agosto de 2022), o vídeo instrucional e o vídeo que mistura mais as três faixas de duração de plano se associam a menos cliques no link do produto, mas as duas associações enfraquecem quando se controla por usuário ou por criador, e a de mistura de planos depende dos controles escolhidos.

## Resumo (o que o artigo promete)

- A pergunta: se dois traços de design, o conteúdo de "guia" (instrucional) e a diversidade de duração dos planos, se associam à chance de o usuário clicar no link do produto.
- A lente: processamento de informação e carga cognitiva; as demandas de processamento semântico e visual-temporal entram como explicações possíveis, não medidas.
- A condição de contorno: o "ajuste algorítmico usuário–conteúdo", a nota da plataforma para a correspondência entre o vídeo e as preferências passadas do usuário.
- Os dados e o modelo: primeira exibição de vídeos de produtos para a casa, de 25/07 a 23/08/2022; modelos lineares de probabilidade em 66.244 observações completas, com efeitos fixos de data e erros-padrão agrupados por criador e por usuário.

## 1. Introdução

- O vídeo curto (de segundos a poucos minutos, feito para consumo rápido no celular) virou vitrine de produto e já não fica só na página do produto: circula em feeds de recomendação, onde o usuário passa ao próximo vídeo com um gesto ou clica no link embutido.
- No feed, ninguém buscou o produto, então o clique depende mais do contexto. Demonstração passo a passo e edição variada podem parecer informativas ou profissionais, mas aumentam o que o usuário tem de processar; com pouca motivação, a resposta ao link pode cair.
- A pesquisa de comércio eletrônico estuda sobretudo quem busca e compara produtos, caso em que a informação detalhada ajuda; no feed, o custo de sair é baixo, e o mesmo traço pode funcionar de outro jeito.
- Contribuições que os autores declaram: levar o estudo do engajamento dentro do feed à passagem do vídeo para a página do produto; aplicar a perspectiva da complexidade ao formato instrucional e à combinação temporal dos planos, separando um do outro; e tratar o ajuste algorítmico como condição de contexto, não como medida da qualidade da recomendação.

## 2. Fundamentação e hipóteses

O raciocínio: a capacidade de atenção é limitada; traços que aumentam as unidades de informação ou a variação da apresentação podem elevar a demanda de processamento, o que cria uma troca entre o valor da informação e o esforço de usá-la. No feed, essa troca pesaria mais. A variável dependente é o clique no link (entrada na página do produto), não a compra nem o engajamento de longo prazo.

| Hipótese | O que prevê | Mecanismo proposto pelos autores |
|---|---|---|
| H1 | o conteúdo de guia se associa a menos cliques | integrar passos, narração, texto na tela e atributos do produto pede memória de trabalho que o usuário do feed pode não dar |
| H2 | a diversidade de duração dos planos se associa a menos cliques | adaptar-se a ritmos diferentes de apresentação reduz a fluência de processamento (a facilidade sentida) |
| H3 | o efeito negativo do guia é mais fraco com ajuste alto | o conteúdo familiar dá pistas semânticas que facilitam entender a instrução |
| RQ1 | como o ajuste modera a diversidade de planos (sem direção prevista) | a familiaridade com o tema não resolve a demanda temporal, e o ajuste alto pode aumentar a sensibilidade a desvios do esperado |

Sobre o ajuste em si, os autores propõem que ele pode se associar a menos cliques sem indicar recomendação ruim: o conteúdo muito parecido com o que o usuário já viu acrescenta menos.

## 3. Método

### 3.1 Cenário e amostra (passo a passo)

1. **Fonte:** o feed de recomendação da página inicial do aplicativo de uma grande plataforma chinesa de comércio eletrônico; vendedores e criadores terceiros sobem vídeos gravados e anexam um ou mais links de produto. A distribuição é pelo algoritmo, não por busca.
2. **Período:** 25/07 a 23/08/2022, com a mesma versão do algoritmo, sem grandes promoções nem feriados.
3. **Posição:** só o primeiro vídeo de cada evento de recomendação amostrado, para reduzir o efeito de posição e de exibições anteriores na mesma sequência.
4. **Categoria:** produtos para a casa, em que a demonstração visual é comum.
5. **Duração:** saem os vídeos com menos de 10 s ou mais de 180 s.
6. **Casos completos:** dos 74.797 registros brutos, ficam 66.244 exibições com todas as variáveis da especificação completa, de 36.542 usuários, 11.045 vídeos e 4.225 criadores; muitos usuários aparecem mais de uma vez, o que permite a análise dentro do usuário.
7. **Unidade:** cada observação é uma exibição usuário–vídeo, com o registro do clique. A exibição não é aleatória (o sistema escolhe pelo histórico do usuário, pelo desempenho anterior e pelo criador); daí os controles, os efeitos fixos de data, as especificações alternativas e os efeitos fixos de usuário e de criador em análises à parte.

### 3.2 Como cada medida foi feita

| Variável | Como se mede |
|---|---|
| Clique (variável dependente) | 1 se o usuário clicou no link do produto durante a exibição, 0 se não; mede a entrada na página do produto, não a compra |
| Guia | binária, a partir do rótulo de tipo de vídeo que a própria plataforma gera; a classificação combinava reconhecimento de fala (ASR), leitura de legenda e texto na tela (OCR) e informação visual, de estilo e de tema, para achar instrução de uso de um produto ou de combinação de produtos. Os vídeos não podem ser recodificados: os dados são anonimizados e os links antigos expiraram |
| Diversidade de duração dos planos | os cortes se detectam pela mudança do histograma de cor quadro a quadro; os planos se dividem em três faixas nos dados fornecidos pela plataforma: longo (mais de 5 s), curto comum (0,5 a 5 s) e muito curto (menos de 0,5 s); o índice de Gini–Simpson, 1 menos a soma dos quadrados das proporções de planos em cada faixa, vai de 0 a 2/3, e quanto mais alto, mais igual a mistura. Os limites das faixas são os da plataforma; as contagens por faixa vêm separadas do campo de número total de planos |
| Ajuste algorítmico | nota de correspondência que a plataforma gera para cada par usuário–vídeo, a partir das preferências passadas do usuário |
| Controles visuais | complexidade de pixel (pelo tamanho do arquivo comprimido normalizado), proporção de pixels de matiz quente, saturação e brilho médios dos quadros |
| Controles de formato | duração do vídeo em segundos (a duração do conteúdo, não o tempo assistido), proporção altura/largura, se não é apresentação de slides, número de caracteres do título |
| Controles comerciais | preço de tabela (em log) e número de links de produto |
| Desempenho anterior | comentários, compartilhamentos e favoritos dos 14 dias anteriores (em log) |
| Criador | categoria certificada pela plataforma (lojista, influenciador, pessoa física) e seguidores (em log) |
| Usuário | gênero e idade previstos pela plataforma, nível da cidade (1 a 6), consumo dos seis meses anteriores |
| Data | indicadores do dia da exibição em todos os modelos principais; número de planos e cortes por segundo entram à parte, como teste de sensibilidade |

### 3.3 Descritivas (Tabela 2, N = 66.244 exibições)

| Variável | Média | DP | Mín. | Máx. |
|---|---|---|---|---|
| Clique | 0,165 | 0,371 | 0 | 1 |
| Guia | 0,547 | 0,498 | 0 | 1 |
| Diversidade | 0,219 | 0,266 | 0 | 0,667 |
| Ajuste | 12,455 | 10,429 | 0 | 96,741 |
| Não é slides | 0,940 | 0,237 | 0 | 1 |
| Complexidade de pixel | 0,409 | 0,110 | 0,184 | 0,736 |
| Proporção altura/largura | 1,705 | 0,224 | 0,562 | 1,781 |
| Duração do vídeo (s) | 17,782 | 14,662 | 10 | 115 |
| Links de produto | 1,169 | 0,512 | 1 | 4 |
| Idade do usuário | 33,920 | 9,757 | 17 | 62 |

A tabela traz também matiz quente, saturação, brilho, título, preço, comentários, compartilhamentos, favoritos, papel do criador, seguidores, gênero, nível da cidade e consumo, que aqui não se repetem. Em texto, os autores dão:

| Medida | Valor | Nível |
|---|---|---|
| Taxa de clique | 16,52% | exibições |
| Vídeos de guia | 54,67% das exibições; 51,41% contando cada vídeo uma vez | exibições e vídeos |
| Vídeos com todos os planos numa faixa só | 51,66% dos vídeos, 57,39% das exibições | vídeos e exibições |
| Diversidade | mediana 0, média 0,247, percentil 90 de 0,640 | vídeos |
| Planos muito curtos | presentes em 25,69% dos vídeos; em média, 12,84% do total de planos das três faixas dentro de cada vídeo | vídeos |
| Correlação da diversidade | r de Pearson 0,350 com o número de planos; 0,122 com a duração do vídeo | o texto não diz o nível |

Os autores avisam que as proporções descrevem a amostra de produtos para a casa, não o conjunto da plataforma, e que diversidade zero quer dizer uniformidade entre as faixas, não ausência de edição.

### 3.3.2 Dados faltantes (Tabelas 3 e 4)

Saem 8.553 observações (11,43%), concentradas em três variáveis, na ordem de exclusão:

| Variável | Faltantes | Exclusões a mais | Restam |
|---|---|---|---|
| Diversidade | 4.095 | 4.095 | 70.702 |
| Preço (log) | 1.493 | 1.437 | 69.265 |
| Consumo anterior | 3.276 | 3.021 | 66.244 |

| Variável | Média dos mantidos | Média dos excluídos | SMD |
|---|---|---|---|
| Clique | 0,165 | 0,140 | 0,071 |
| Guia | 0,547 | 0,619 | −0,147 |
| Diversidade | 0,219 | 0,203 (4.458 válidos) | 0,062 |
| Duração do vídeo (s) | 17,782 | 24,188 | −0,320 |
| Compartilhamentos (log) | 3,446 | 2,643 | 0,423 |
| Favoritos (log) | 4,784 | 4,026 | 0,375 |

### 3.4 O modelo

Modelo linear de probabilidade: o clique em função de guia, diversidade, ajuste, guia × ajuste, diversidade × ajuste e os controles, com diversidade e ajuste centrados na média (mantendo a unidade original), efeitos fixos de data e erros-padrão agrupados em duas dimensões, por criador e por usuário (não pelo par). O coeficiente do guia lê-se como a diferença guia/não guia no ajuste médio. Quatro modelos sobre as mesmas 66.244 observações: 1, só as três variáveis focais; 2, mais guia × ajuste; 3, mais diversidade × ajuste; 4, as duas interações. Depois, em sequência: robustez e sensibilidade, heterogeneidade por criador e a interação da complexidade de pixel com o ajuste.

## 4. Resultados

### 4.1 Os quatro modelos principais (Tabela 5)

| Termo | Modelo 1 | Modelo 2 | Modelo 3 | Modelo 4 |
|---|---|---|---|---|
| Guia | −0,02111** (0,00668) | −0,02104** (0,00668) | −0,02116** (0,00668) | −0,02109** (0,00668) |
| Diversidade | −0,03319** (0,01214) | −0,03273** (0,01212) | −0,03325** (0,01212) | −0,03279** (0,01209) |
| Ajuste | −0,00317*** (0,00018) | −0,00369*** (0,00026) | −0,00318*** (0,00018) | −0,00371*** (0,00026) |
| Guia × ajuste | — | 0,00091** (0,00033) | — | 0,00093** (0,00033) |
| Diversidade × ajuste | — | — | −0,00047 (0,00057) | −0,00059 (0,00057) |
| R² | 0,06018 | 0,06034 | 0,06019 | 0,06036 |
| Estatística F | 24,98 | 25,02 | 25,56 | 25,56 |
| Previsões abaixo de 0 | 4,10% | 4,04% | 4,10% | 4,01% |

Erro-padrão entre parênteses; *** p < 0,001, ** p < 0,01. Previsões acima de 1: 0% nos quatro.

- **Guia (H1):** no Modelo 1, o vídeo de guia tem chance de clique 2,11 pontos percentuais menor (p < 0,01), e a associação segue significativa no modelo completo.
- **Diversidade (H2):** subir 0,1 no índice corresponde a cerca de 0,33 ponto percentual a menos de clique (p < 0,01).
- **Guia × ajuste (H3):** positiva e significativa (p < 0,01). A diferença do guia vai de cerca de −3,0 pontos percentuais no ajuste baixo (percentil 10) a −0,9 no alto (percentil 90), onde já não é significativa (p > 0,1); a atenuação é significativa (p < 0,01).
- **Diversidade × ajuste (RQ1):** não significativa (p > 0,1); a associação negativa varia pouco com o ajuste, sem diferença que se distinga.

### 4.2 Robustez e sensibilidade

**Medidas alternativas (Tabela 6).** Cada coluna é o Modelo 4 com uma mudança.

| Termo | + número de planos | + cortes por segundo | Entropia no lugar do Gini–Simpson | Winsorizado | Ajuste médio do usuário |
|---|---|---|---|---|---|
| Guia | −0,02104** | −0,02145** | −0,02117** | −0,02045** | −0,02021** |
| Diversidade | −0,03246** | −0,03581** | −0,02096** | −0,03218** | −0,03231** |
| Ajuste | −0,00371*** | −0,00370*** | −0,00370*** | −0,00369*** | −0,00426*** |
| Guia × ajuste | 0,00094** | 0,00093** | 0,00093** | 0,00094** | 0,00088* |
| Diversidade × ajuste | −0,00059 | −0,00062 | −0,00042 | −0,00058 | −0,00065 |
| R² | 0,06036 | 0,06041 | 0,06037 | 0,06061 | 0,06177 |

Cortes por segundo é (número de planos − 1) dividido pela duração do vídeo; a entropia usa as mesmas faixas com outra agregação; o winsorizado corta preço, contagens sociais e duração nos percentis 1 e 99. Nesta tabela e nas Tabelas 7, 8, A2, A5 e A7, o asterisco simples é p < 0,1 (a nota da Tabela 5 só tem ** e ***).

**Forma funcional (Tabela 7).** Padronizando diversidade e ajuste pelo desvio-padrão da amostra completa, os sinais e a significância de H1 a H3 se mantêm (guia −0,02109**, diversidade −0,00874**, ajuste −0,03866***, guia × ajuste 0,00975**, diversidade × ajuste −0,00164). O termo quadrático da diversidade não é significativo (0,08703, EP 0,08892); o do ajuste é positivo e significativo (0,00003***, p < 0,01), e os coeficientes de H1 a H3 mantêm direção e significância. A curvatura (Figura 4, não vista) quer dizer, para os autores, que a inclinação do ajuste varia com a nota, e que o coeficiente do guia no ajuste médio não vale como relação uniforme na faixa toda; ela não estabelece forma de U nem a forma da moderação.

**Logit (Tabelas A2 e A3).** Em log-odds, guia −0,11309 e diversidade −0,21093 (com * no agrupamento por criador e *** no por usuário); guia × ajuste 0,00335, não significativo em nenhum dos dois agrupamentos. Na escala de probabilidade:

| Contraste (pontos percentuais) | Agrupado por criador | Agrupado por usuário |
|---|---|---|
| Guia no ajuste P10 | −2,206 (p 0,002) | −2,206 (p < 0,001) |
| Guia no ajuste P50 | −1,648 (p 0,013) | −1,648 (p < 0,001) |
| Guia no ajuste P90 | −0,652 (p 0,467) | −0,652 (p 0,166) |
| Guia, P90 − P10 | 1,554 (IC 95% −0,342 a 3,450; p 0,108) | 1,554 (IC 95% 0,146 a 2,961; p 0,031) |
| Diversidade +0,1 no P10 | −0,217 (p 0,107) | −0,217 (p 0,010) |
| Diversidade +0,1 no P50 | −0,256 (p 0,043) | −0,256 (p < 0,001) |
| Diversidade +0,1 no P90 | −0,291 (p 0,081) | −0,291 (p < 0,001) |
| Diversidade, P90 − P10 | −0,074 (p 0,669) | −0,074 (p 0,579) |

A direção concorda com H3, mas o apoio estatístico depende do agrupamento; os autores lembram que o teste do produto e o contraste de probabilidade medem coisas diferentes.

**Agrupamento (Tabela A1).** Sem efeitos fixos de data, agrupar por criador, por usuário ou nas duas dimensões dá os mesmos coeficientes (guia −0,02057, diversidade −0,03285, ajuste −0,00361, guia × ajuste 0,00096, diversidade × ajuste −0,00058, R² 0,05823); o agrupamento só por usuário dá erros-padrão menores (guia 0,00303 contra 0,00665 por criador). Com data e agrupamento por criador, os coeficientes são os do Modelo 4.

**Dados faltantes e conjunto de controles (Tabelas 8, A4 e A5).**

- Tirar só o consumo anterior mantém o padrão nas 66.244 observações (guia −0,02133**, diversidade −0,03332**, guia × ajuste 0,00091**) e na amostra ampliada de 69.265 (−0,02057**, −0,03031*, 0,00085**). Esse teste não recupera as exibições sem diversidade ou sem preço.
- Tirar juntos desempenho anterior, criador e consumo (Tabela A5): a diversidade fica pequena e não significativa (−0,00799 na mesma amostra; −0,00564 na ampliada), e o guia e a interação seguem (−0,02438**, 0,00074*).
- O caminho da diversidade, somando os blocos de controle em ordem (Tabela A4, N = 66.244): só focais 0,00360 (p 0,804); + vídeo −0,00614 (p 0,678); + produto −0,00781 (p 0,585); + desempenho anterior −0,02257 (p 0,073); + criador −0,03295 (p 0,007); + usuário −0,03279 (p 0,007). Os autores avisam que o caminho é descritivo e depende da ordem.

**Efeitos fixos de usuário (Tabela 8).** Sem os usuários que aparecem uma vez só (24.254 exclusões), a amostra pareada tem 41.990 exibições de 12.288 usuários.

| Termo | Pareada, sem EF de usuário | Com EF de usuário |
|---|---|---|
| Guia | −0,02206** | −0,00712 (não significativo) |
| Diversidade | −0,03693** | −0,02869** |
| Ajuste | −0,00384*** | −0,00063* |
| Guia × ajuste | 0,00089* | 0,00029 (não significativo) |
| Diversidade × ajuste | −0,00049 | 0,00022 |

Para os autores, diferenças estáveis entre usuários respondem por parte das associações do guia, e a da diversidade aparece dentro do mesmo usuário: apoio mais forte a H2 do que a H1 e H3 nessa análise.

**Efeitos fixos de criador (Tabela A7).** Dos 4.225 criadores, 1.972 têm mais de um vídeo; o guia varia dentro de 1.267 e a diversidade dentro de 1.555. Sem os 1.198 criadores de uma exibição só, ficam 65.046 exibições, 3.027 criadores, 9.847 vídeos e 36.064 usuários.

| Termo | Pareada, sem EF de criador | Com EF de criador |
|---|---|---|
| Guia | −0,020817** | −0,014383* |
| Diversidade | −0,033565** | −0,025245 (não significativo) |
| Ajuste | −0,003661*** | −0,001192*** |
| Guia × ajuste | 0,000894** | 0,000417 (não significativo) |
| Diversidade × ajuste | −0,000549 | −0,000201 |

Os sinais ficam, e a evidência de guia, diversidade e guia × ajuste enfraquece; os autores dizem que isso qualifica o apoio a H1–H3 dos modelos principais.

### 4.3 Heterogeneidade por criador (exploratória; Tabelas 9 e A6)

Criadores divididos por seguidores, papel na plataforma, número de exibições e número de vídeos na amostra; 20 testes de diferença, ajustados pelo método de Holm. Nenhuma diferença de interação é significativa depois do ajuste; a menor, guia × ajuste por seguidores (diferença 0,00149, p 0,031), vai a p 0,622 com Holm.

### 4.4 Complexidade de pixel (exploratória; Tabela 10)

Com as variáveis contínuas padronizadas, acrescentar complexidade de pixel × ajuste ao modelo principal dá −0,00317 (EP 0,00200), não significativo, como a diversidade × ajuste (−0,00236); as duas não diferem entre si (p > 0,1), e a de pixel difere da de guia × ajuste (0,00916**), sem p dado no texto. A moderação aparece só para o guia.

## 5. Discussão

### 5.1 Como os autores leem os resultados

- O guia com menos clique: talvez porque a instrução e a explicação aumentem a demanda semântica antes da decisão de ir à página do produto, e a apresentação rica funcione menos quando sair é fácil.
- A diversidade com menos clique: a variação entre faixas de duração talvez aumente a demanda temporal e tire fluência do acompanhamento visual.
- O ajuste com menos clique: o vídeo muito alinhado ao histórico talvez acrescente pouco, e a relação parece não linear.
- O guia × ajuste: pistas familiares ajudariam a entender a instrução, o que concorda com a explicação pela familiaridade.
- A diversidade e a complexidade de pixel sem moderação: o papel do ajuste dependeria do tipo de traço, mais ligado à informação explicativa do que à variação temporal ou visual.
- A ressalva que eles mesmos repetem: guia e guia × ajuste enfraquecem com efeitos fixos de usuário e de criador; a diversidade segue com efeitos de usuário, varia com os controles e não é significativa com efeitos de criador.

### 5.2 Contribuições declaradas

Mostrar que traços que parecem mais informativos ou variados podem se associar a menos clique quando o vídeo chega por recomendação; separar o formato instrucional da combinação temporal dos planos, em vez de tratar a complexidade como uma coisa só; e tratar o ajuste algorítmico como condição de contorno, que deixa o guia mais útil sem tornar mais valiosa a visita à página do produto.

### 5.3 Implicações práticas que os autores tiram

- **Para criadores:** mais explicação e mais mistura de durações de plano não são caminho seguro para mais clique; o guia serve quando o produto pede demonstração ou instrução, mas vale pensar se ele cabe quando o objetivo imediato é levar à página do produto. A mistura de planos longos, curtos e muito curtos deve seguir o que o vídeo precisa comunicar, não virar estratégia geral; e o clique deve ser avaliado junto com o propósito informativo do vídeo.
- **Para plataformas:** a nota de ajuste alta não é prova de propensão ao clique, porque o conteúdo muito alinhado pode já satisfazer parte da necessidade dentro do feed; guia e diversidade devem ser avaliados em separado ao combinar sinais de design com o ajuste, e o clique, separado de visualização, compartilhamento, compra e uso.

### 5.4 Limites declarados

1. **As medidas são traços observáveis, não processos mentais.** O guia é um rótulo da plataforma e não mede a complexidade semântica nem a dificuldade sentida; a diversidade mede a distribuição pelas faixas, não a ordem dos planos, o padrão das transições, a coerência narrativa nem a qualidade da edição. A precisão do rótulo e outros limites de faixa de duração não podem ser avaliados com os dados guardados. A suficiência da informação explica também o efeito do guia (a demonstração responde à dúvida dentro do feed), e faltam tempo assistido, conclusão ou compreensão por exibição para separar as duas explicações.
2. **Desenho observacional:** a exibição não é aleatória, e as relações podem refletir a recomendação e a escolha do usuário; o estilo do criador pode moldar junto o formato, a edição e o clique, e as análises por subgrupo de criador não substituem a comparação dentro do criador. O ajuste só é observado nas exibições que aconteceram, e controlar por ele pode trazer viés de condicionamento.
3. **Seleção por casos completos:** os excluídos têm mais guia (61,9% contra 54,7%), menos clique (14,0% contra 16,5%), vídeos mais longos e menos compartilhamentos; o sentido do viés no coeficiente do guia não se determina por essas diferenças. O teste do consumo anterior não resolve a falta de diversidade e de preço.
4. **Alcance:** uma categoria, uma plataforma, um período curto e só a primeira posição do feed; os autores sugerem outras categorias, plataformas, posições e períodos mais longos, e acompanhar a mudança de algoritmos, edição e hábitos.

Como próximos passos, propõem juntar os dados da plataforma com codificação manual e estudos com usuários, experimentos de campo ou naturais, e a manipulação direta do formato instrucional e da apresentação temporal.

## 6. Conclusões

No feed de recomendação, design mais elaborado não se associa necessariamente a uma resposta comercial imediata maior. Na especificação completa, guia e diversidade se associam a menos clique; a associação do guia enfraquece com ajuste alto, embora o ajuste sozinho se associe a menos clique; o guia e a interação enfraquecem com efeitos de usuário e de criador, e a diversidade depende dos controles; não há moderação estável da diversidade pelo ajuste. A recomendação final é separar riqueza de informação, variação temporal, correspondência usuário–conteúdo e o valor de visitar a página do produto.

## Declarações

- **Financiamento:** Fundação de Ciências Naturais da Província de Zhejiang (LQ24G020010), projetos de cooperação do planejamento de filosofia e ciências sociais de Zhejiang (24SSHZ058YB) e o programa de talentos Yongjiang de Ningbo (2023B-345-G).
- **Dados:** proprietários da plataforma, com restrições de contrato e privacidade, não compartilháveis; código e construção das variáveis a pedido, se o acordo de uso permitir.
- **Conflitos de interesse:** nenhum declarado. Comitê de ética e consentimento: "não se aplica".
- **Ferramenta:** as Figuras 3 e 4 foram geradas no Stata (MP 18.0, na Figura 3).

## Citações

- "Long shots last more than 5 s, ordinary short shots last from 0.5 to 5 s, and very short shots last less than 0.5 s."
- "A zero Diversity value therefore describes uniformity across the supplied duration categories and does not imply an absence of editing."
- "Shot-duration diversity captures the distribution of shots across duration categories but does not capture shot sequence, transition patterns, narrative coherence, or editing quality."

## Lacuna

O artigo não dá a duração média, a mediana nem a distribuição da duração dos planos, nem o número médio de planos por vídeo, só o índice de diversidade e as faixas (a seção 3.2.3 diz que o campo de número total de planos é usado na Tabela 2, e a Tabela 2 não traz essa linha); não nomeia a plataforma nem mostra como o rótulo de guia e a nota de ajuste são calculados; não tem tempo assistido nem compra; e não diz se os vídeos são verticais, além da proporção altura/largura média de 1,705. Os vídeos não podem ser revistos, e os limites de 0,5 s e 5 s são da plataforma, sem teste de outros limites.
