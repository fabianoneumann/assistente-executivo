---
titulo: "Addressing TikTok's multimodal complexity: a multi-level annotation scheme for the audio-visual design of short video content"
tipo: paper
autor: "Maciej Nikodem Grzenkowicz e Janina Wildfeuer (Faculty of Arts, University of Groningen)"   # nomes completos em "Author contributions" do texto; a afiliação vem do registro do DOI no Crossref
url: "https://academic.oup.com/dsh/article/40/4/1143/8168928"
publicado_em: 2025-06-18   # o texto gravado não traz data, só "© The Author(s) 2025"; a data é a publicação online no Crossref (DOI 10.1093/llc/fqaf047), que dá também o número impresso de 1/12/2025 (vol. 40, n. 4, p. 1143-1166)
capturado_em: 2026-11-12
licenca: "CC BY 4.0 (últimas linhas do texto, depois das referências: '© The Author(s) 2025. Published by Oxford University Press on behalf of EADH.' e 'This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/)'); o integral está na url"
areas: [generative-media, content-design]
tags: [short-form-video, vertical-video, shot-length, montage, camera-shots, camera-movement, editing-transitions, aspect-ratio, multimodal, film-analysis, annotation-scheme, human-agreement]
---

# Grzenkowicz e Wildfeuer: um esquema de anotação para o TikTok e a duração de plano em 20 vídeos sobre Zelensky

Ficha de estudo: as seções seguem a ordem do artigo (resumo, 1 a 5 e as notas), com o método em passos, as categorias do esquema em tabelas, os números com o grupo de vídeos e a estatística que o texto diz, as ressalvas e os limites dos autores. O texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Artigo de *Digital Scholarship in the Humanities* 40(4):1143, https://academic.oup.com/dsh/article/40/4/1143/8168928, lido pelo Chrome em 2026-11-12. O texto da página foi gravado na cópia de trabalho, e é ele que sustenta o integral: sha256 (hash omitido), o hash do próprio texto gravado, igual ao do `protegidas.json` da rodada. Wayback: http://web.archive.org/web/20260425145621/https://academic.oup.com/dsh/article/40/4/1143/8168928. **O texto gravado não traz o título, o cabeçalho dos autores nem a data**: começa pela barra de ferramentas da página ("PDF", "Split View", "Cite") e pelo resumo. Título, revista, volume, páginas e datas conferidos no registro do DOI 10.1093/llc/fqaf047 no Crossref; os nomes dos autores, em "Author contributions". **Licença:** CC BY 4.0, nas duas últimas linhas do texto, depois das referências. **Cobertura:** lido o texto inteiro, do resumo às cinco notas de rodapé; as referências, só percorridas. As 20 figuras são imagem e não estão no texto (só as legendas): ficam sem leitura, entre elas a Figura 15 (os valores de Kappa), a 17 e a 18 (as tabelas de planos e eventualidades). Os dois apêndices suplementares (um zip, com o esquema gráfico completo e a lista dos vídeos) não foram abertos. Sem conferência automática nem lado a lado: a licença permite a cópia, e o integral não vem neste repositório e se lê na url do frontmatter (`README.md` desta pasta, item 1).

## Em uma frase

Dois pesquisadores de Groningen propõem um esquema de anotação em várias camadas para vídeos curtos do TikTok (plano, objeto visual, corte, texto escrito, fala, som, música, filtro e eventualidade), testam a concordância entre os dois (os próprios autores) e o aplicam a 20 vídeos sobre Zelensky, em que os vídeos de fala têm planos de 14,73 s e os de montagem, de 2,02 s, em média.

## Resumo (o que o artigo promete)

- A pergunta: como analisar de modo sistemático o sentido que se produz nos vídeos curtos, que juntam muitos recursos ao mesmo tempo.
- O caminho: descrever o "terreno semiótico" do TikTok, combinar abordagens de análise de audiovisual e de discurso multimodal, e montar um esquema que trate tanto do formal (plano, objeto visual, som, filtro) quanto do conteúdo (eventualidade, participante representado).
- A prova: o esquema testado e avaliado num corpus de vinte vídeos que mostram o presidente ucraniano.

## 1. Introdução: por que o vídeo curto pede um esquema próprio

- Os estudos de TikTok cresceram (cultura, política, desinformação), mas a complexidade da produção de sentido raramente é o foco, e faltam esquemas de anotação para análise em grande escala ou automática.
- Filme, série, anúncio e YouTube já foram muito estudados na pesquisa multimodal; o vídeo curto, não.
- Os autores dão o exemplo das contas de checagem de fatos no TikTok (Politifact, Bolivia Verifica, com cerca de 205 mil e 216 mil seguidores em novembro de 2024, pela nota 1): para saber como elas mostram o conteúdo enganoso, é preciso olhar objeto visual, fala e texto, música de fundo e filtro (como a câmera lenta) juntos.
- O recorte é o TikTok: vídeo de no máximo um minuto em média e um algoritmo que favorece engajamento, o que, para os autores, leva a estratégias mais complexas que as de outras redes, com muito reaproveitamento de material; por isso a unidade de análise precisa ser fina (perspectiva, movimento e transição de câmera, música, som, transcrição de fala e texto), como na análise multimodal de filme.

## 2. O estado da arte e a anotação "stand-off"

- O desafio comum aos esquemas de anotação de artefato multimodal é ligar a forma (os elementos do vídeo) à composição narrativa ou argumentativa. No vídeo curto, uma narração pode atravessar vários planos e telas divididas e comentar só alguns acontecimentos; objeto visual, som não diegético e texto aparecem sem sincronia entre si. Daí a necessidade de segmentações separadas para o som, a imagem e os acontecimentos.
- Os estudos de TikTok existentes criam cada um o seu quadro e terminologia, e por isso não se comparam; outros olham muitos dados com poucos traços (brilho, cor, presença de rosto) ou com divisões largas (visual, sonoro, textual), sem detalhe de câmera, de som ou de tipografia. Os autores dizem não conhecer esquema como o deles.
- Na anotação de filme, a AdA Film Ontology tem mais de 500 valores e prioriza a impressão de quem vê, não a técnica de produção; o esquema deste artigo, ao contrário, pesa mais a produção, combinada com a leitura semiótica.
- A anotação "stand-off": o anotador divide o material em segmentos e os descreve em níveis independentes, que podem valer ao mesmo tempo, sem escrever a estrutura dentro do dado. Nasceu para a sobreposição espacial dos quadrinhos e serve, para os autores, ao dado organizado no tempo.
- A base teórica é a Linguística Sistêmico-Funcional: redes de sistema que listam as escolhas disponíveis a quem produz o texto. O esquema se oferece como base a ajustar: quem analisa escolhe as categorias que interessam e detalha as mais salientes.

## 3. O esquema de anotação

### 3.1 As unidades principais

- O ponto de partida é decidir a unidade de análise; um vídeo do TikTok pode ter várias "telas" (canvas), sobretudo nos formatos que reusam outro vídeo (stitch, tela verde, meme de música).
- As unidades nasceram da anotação de uma amostra aleatória de vídeos de subgêneros variados, partindo do plano e do acontecimento principal de um trabalho anterior sobre séries (Drummond e Wildfeuer, 2020) e acrescentando categorias quando a amostra pedia.
- **Plano:** a unidade mais universal do audiovisual; todo vídeo do TikTok tem pelo menos um. **Corte** e **filtro** viram unidades próprias, porque o corte pode ter sentido e o filtro pode cobrir um plano, um som ou vários.
- Objeto visual e texto escrito entram e saem sem seguir os planos nem os acontecimentos; som, música e fala também são unidades independentes (a narração atravessa planos; a música pode durar o vídeo inteiro; o efeito sonoro curto sublinha uma ação).
- **Eventualidade** (termo da semântica do discurso, no lugar de "evento" ou "ação"): a ação, o acontecimento ou o estado de coisas que um segmento significa. Um vídeo de muitos planos pode mostrar um só acontecimento, e um plano pode mostrar vários; nova eventualidade quando surge uma nova relação entre participantes, objetos ou lugares.

### 3.2 As camadas, atributos e valores

**Plano** (seis divisões):

| Divisão | Valores que o texto dá |
|---|---|
| Material com perspectiva: ângulo | nível dos olhos; vista de pássaro (câmera acima); vista de sapo (câmera abaixo) |
| Material com perspectiva: enquadramento | plano muito fechado (VCS), fechado (CS), médio (MS), aberto (LS), muito aberto (VLS) |
| Material com perspectiva: movimento | acompanhar, tremer, zoom de aproximação ou afastamento, panorâmica, tilt, dolly, truck |
| Material sem perspectiva (infográfico, gráfico, tabela, captura de tela) | procedência: captura de tela, material informativo, campo de cor, padrão abstrato (categoria aberta); atividade, que imita o uso do celular: deslizar, ampliar, reduzir; contextualização: se aparece a origem (barra de endereço, o leiaute do app, o título ou o autor do infográfico) |
| Dinamicidade | dinâmico (filmagem, animação, gravação de tela) ou estático (foto, infográfico, captura) |
| Função narrativa | original (a linha principal, inclusive material achado com narração nova), citado (de outra fonte, ligado ao tema), de banco (ilustra sem ligação com o contexto) e fundo (sobre ele se sobrepõem outros recursos) |
| Ajuste ao formato (em geral vertical, com casos horizontais e quadrados) | cortado (falta um pedaço, como um logo de TV pela metade); estendido (faixas acrescentadas, até tarjas pretas, ou o espectro de cor desfocado em cima e embaixo); natural (composição vertical sem sinal de corte); cortado e estendido juntos |
| Composição | um material; dois materiais (como o modo Duet), em posição horizontal, vertical ou imagem dentro de imagem; vários materiais, sem posição a registrar |

A divisão entre material com e sem perspectiva é, para os autores, a novidade do esquema, e o "ajuste" é uma categoria nova. Na composição com mais de um material, todo o ramo do plano se anota para cada material.

**As outras camadas:**

| Camada | Divisões e valores |
|---|---|
| Objetos visuais (gráficos fora do mundo representado, sobrepostos) | forma: figura geométrica, desenho, adesivo (ou GIF), emoji, citação de comentário, gráfico pequeno, logo, outra; e o que mostra, em texto livre |
| Cortes | transição: corte seco, dissolvência, fade de ou para cor única, deslize (entra ou sai pela borda), pop-up (surge ampliando no centro ou some encolhendo), outra; sincronia de som e imagem: sincronizado, L-cut (o som do plano anterior continua no seguinte), J-cut (o som do seguinte começa antes), sem relação, e "sublinhado" (a troca coincide com um som, em geral não diegético) |
| Texto escrito | conteúdo transcrito (emoji no texto vira objeto visual); fonte interna do app (classic, typewriter, handwriting, neon, serif) ou externa; moldura: com caixa, com contorno nas letras, sem moldura |
| Fala | transcrição corrida, sem outra classificação (camadas de análise da conversa podem entrar) |
| Som (o que não é música nem fala) | diegético (vem das ações mostradas) ou não diegético |
| Música | gênero, pelas definições do dicionário de Cambridge (ambient, blues, clássica, eletrônica, folk, funk, hip-hop, jazz, new age, pop, reggae, rock, soul, trap) mais três dos autores: cinematográfica (orquestral ilustrativa sem tema marcante), latina, metal |
| Filtros | audiovisuais, por material (visual ou sonoro) e por tipo (distorção, que degrada, como pixelizar; manipulação, que muda outra propriedade, como o brilho ou o grave); temporais: câmera lenta e timelapse |
| Eventualidade (a camada funcional) | descrita em texto livre; participantes representados (até três por eventualidade, pela seção 4.4.1), com modalidade (visual, sonora, escrita, falada, ou combinação), tipo de entidade (humano, objeto, entidade abstrata; boneco de palito conta como humano, animal antropomorfizado como objeto), função (Ator, Meta, Escopo: quem corta a cenoura, a cenoura, a faca) e gesto (ação de apresentação, de representação positiva ou negativa, ação indexical, que só se entende com a fala junto) |

Os autores dizem que modalidade, tipo e função são categorias funcionais, úteis para a análise crítica e quantitativa (a quem o vídeo dá mais agência, que ações ele apaga).

## 4. O estudo-piloto

### 4.1 As perguntas

O piloto quer mostrar que o esquema funciona e medir a concordância entre dois anotadores. O tema escolhido é a representação de Zelensky, para levar o estudo do TikTok a uma região pouco coberta. As hipóteses declaradas: pouca diferença entre os dois grupos na frequência de personagens e objetos; uma estrutura parecida de dinamicidade; e que a conta oficial evitaria música popular que destoasse da gravidade do cargo.

- RQ1: que pessoas e objetos representam o Estado ucraniano na comunicação oficial e na popular?
- RQ2: como a duração, a música e a câmera marcam o caráter oficial ou popular?

### 4.2 O corpus (passo a passo)

1. Vinte vídeos postados depois de 24/02/2022, em dois grupos de dez; a lista completa está no apêndice suplementar 2 (não aberto).
2. **Grupo popular:** os dez vídeos mais curtidos com a hashtag #Зеленський no dia da coleta, 30/05/2023. Critério só pelas curtidas, porque, na guerra, comentário e compartilhamento podem vir de robô, e muitos comentários não dizem se a recepção foi boa ou ruim. No máximo um vídeo por criador (fica o mais curtido); um vídeo com a perspectiva russa saiu.
3. **Grupo oficial:** o perfil @ze__president (1,3 milhão de seguidores e 28,6 milhões de curtidas quando o artigo foi escrito). O primeiro vídeo de cada um dos dez meses de agosto de 2022 a maio de 2023; quando o primeiro do mês não tratava do presidente, o seguinte que tratasse.
4. O primeiro anotador fez 2.747 anotações nos vinte vídeos; o artigo relata só uma parte delas.

### 4.3 A anotação e a concordância

1. Ferramenta: ELAN. Cada categoria do esquema vira uma camada (tier), as subcategorias viram subcamadas alinhadas no tempo à de cima (como plano e composição), e parte dos valores entra como vocabulário controlado. O manual de anotação é longo e sai só a pedido (nota 4); os arquivos do ELAN não estão em repositório, e o modelo se compartilha a pedido (nota 5).
2. O grupo oficial foi anotado primeiro; nas discordâncias, o esquema se esclareceu e as anotações se ajustaram. Depois, o grupo popular se anotou de forma independente.
3. Os dois anotadores são os próprios autores, treinados numa amostra aleatória antes; eles chamam a configuração de restrita.
4. Medida: Kappa de Cohen em cinco camadas com vocabulário controlado (música, ajuste, ângulo, enquadramento e movimento de câmera). O texto diz que se usou "o segundo corpus", porque os vídeos do primeiro eram muito parecidos na forma; a legenda da Figura 15 diz "corpus of popular #Zelensky videos". Os grupos de traços se juntam "com generosidade", e as unidades de perspectiva se anotam por plano, então os vídeos de mais planos pesam mais.
5. Leitura dos valores pela régua que o texto usa: acima de 0,81, concordância muito boa ou quase perfeita; acima de 0,61, substancial. Resultado: em geral boa; o Kappa do enquadramento ficou "pouco moderado", apesar da concordância percentual muito boa, o que os autores atribuem ao excesso de planos médios e à falta de planos muito abertos e muito fechados. Os valores estão só na Figura 15, que não foi lida.
6. A concordância veio depois de discutir e ajustar categorias, sobretudo enquadramento e movimento; contou-se como concordância os dois marcarem "sem movimento". A música tinha vocabulário controlado, mas sem definição dos valores, acrescentada depois.

### 4.4 Os resultados

Os resultados usam a anotação "padrão ouro" que saiu da avaliação.

**Participantes representados (RQ1).** Anotações em texto livre agrupadas (soldado, soldados, esquadrão contam como uma), em proporção do total de eventualidades.

| Participante | Grupo oficial (@ze__president) | Grupo popular (#Зеленський) |
|---|---|---|
| Zelensky | 22 de 33 eventualidades (66,7%) | 27 de 37 (73%) |
| Soldado | 22 de 33 (66,7%), empatado com Zelensky | 2 de 37 (5,4%) |
| Bandeira ucraniana | 7 (21,2%) | 4 (10,8%) |

As eventualidades com soldados são mais curtas e aparecem mais no subgênero de montagem.

**Duração e contagem de planos e eventualidades (RQ2).** A tabela dá cada número como o texto o dá; as Figuras 17 e 18, que trazem os mesmos dados em imagem, não foram lidas. O texto não diz como as durações foram medidas, além de que planos e eventualidades são segmentos da anotação no ELAN, nem se a média é de vídeo a vídeo ou de todos os planos juntos.

| Medida | Grupo oficial | Grupo popular | O que o texto diz da estatística |
|---|---|---|---|
| Duração do vídeo | 29,23 s | 28,67 s | "the similar length of the videos themselves", sem dizer a estatística; a frase vem depois de "on average" |
| Planos por vídeo | 7 | 5,1 | "on average" |
| Duração do plano | 8,25 | 9,15 | "average length of the shots", sem unidade; a ordem segue a da frase ("respectively", oficial antes) |
| Eventualidades por vídeo | 3,3 | 3,6 | "a similar number of eventualities", sem dizer a estatística |
| Duração da eventualidade | 24,48 s | 17,71 s | "average length of eventualities"; é a diferença principal entre os grupos, para os autores |

**Dois formatos.** Comparando contagens, durações e tipos de eventualidade, os autores separam dois formatos: **fala** (uma eventualidade só, longa, em geral anotada como "falando") e **montagem** (pelo menos quatro eventualidades e quatro planos, que reúnem materiais sobre o mesmo participante, Zelensky ou os soldados).

| Medida | Fala | Montagem | O que o texto diz da estatística |
|---|---|---|---|
| Planos por vídeo | 3,8 | 8,625 | "on average"; "quase cinco vezes mais" planos na montagem |
| Eventualidades por vídeo | 1 | 6,875 | "on average"; "quase seis vezes mais" |
| Duração do plano | 14,73 s | 2,02 s | "tend to be significantly shorter", sem teste estatístico relatado |
| Duração da eventualidade | 36,41 s | 2,33 s | idem |
| Vídeos do grupo oficial | 7 de 10 | 3 de 10 | contagem |
| Vídeos do grupo popular | 3 de 10 | 5 de 10 | contagem |

**Música.** Proporção das anotações de cada gênero sobre o total de anotações de música. Grupo oficial: cinematográfica em 6 de 9 anotações, eletrônica em 2, soul em 1. Grupo popular: folk em 8 de 16, quase todas de um vídeo que repete a mesma canção; daí os autores tomarem folk, pop, trap e eletrônica como parecidos em popularidade nesse grupo.

**Enquadramento.**

| Grupo | Planos | Fechado (CS) | Médio (MS) | Aberto (LS) |
|---|---|---|---|---|
| Oficial | 70 | 21 | 37 | 12 |
| Popular | 51 | 4 | 45 | 2 |

Nenhum plano muito fechado nem muito aberto nos dois grupos. Nenhuma composição além de "um material só" apareceu. A legenda da Figura 20 diz "camera angle types", e o parágrafo trata de enquadramento.

### 4.4.3 A leitura dos autores

- O esquema serviu por três razões, pelos autores: é sensível ao material da plataforma (como o gênero da música), separa segmentações que não andam juntas e adapta a eventualidade a planos muito curtos.
- Os autores leem a presença de soldados e da bandeira no perfil oficial como busca de moral e de unidade nacional, ligando o presidente às forças armadas e a todos os cidadãos; e o foco em Zelensky no grupo popular como fascínio dos usuários por ele.
- O perfil oficial prefere a fala, que lembra um pronunciamento de TV, e foge da tendência do TikTok aos vídeos curtos e de corte rápido; a música cinematográfica e a variedade de enquadramentos reforçam, para eles, a imitação da televisão e do cinema, como um "filme de guerra" com final feliz esperado. O grupo popular prefere a montagem, e a música dele seguiria as tendências do TikTok.
- Eles dizem que os achados concordam com estudos anteriores sobre a imagem de Zelensky (a farda no Grammy de 2022; o Instagram dele no começo da guerra, centrado no presidente e de estilo cinematográfico profissional).

## 5. Conclusão, limites e próximos passos (o que os autores declaram)

- O esquema cobre forma e função, e o vídeo curto pede várias categorias de segmentação, porque os modos andam ainda menos sincronizados que em outros audiovisuais.
- Foi pensado também para Instagram e YouTube Shorts, mas a aplicação a outras plataformas ainda não foi testada, e o uso dos modos pode mudar com as possibilidades de cada uma.
- Vinte vídeos não representam as tendências do TikTok nem de outros vídeos curtos; faltam estudos maiores, em contextos locais e pouco estudados, em discursos variados e no tempo. Projetos menores, como o de vídeos de checagem, estão testando o esquema.
- A concordância precisa ser medida com mais anotadores e menos familiarizados com o esquema, e os autores esperam mais variação e mais ajustes.
- Anotar tudo num vídeo complexo leva muito tempo; a maioria dos estudos não precisará de todas as categorias, e os corpora anotados por inteiro podem servir de treino para modelos multimodais que ajudem a anotar.
- A compatibilidade com o ELAN permite quantificar, e o esquema seria o primeiro passo para automatizar a análise, com uso em desinformação, discurso de ódio e propaganda.

## Inconsistências do próprio texto

- A numeração dos grupos muda: nas seções 4.1 e 4.2, o "primeiro corpus" é o popular e o "segundo", o oficial; na 4.4.1, "first corpus" é o do @ze__president, o das 33 eventualidades.
- A seção 4.3 diz que a concordância se calculou no "segundo corpus"; a legenda da Figura 15, no corpus popular.
- O texto remete à seção 3.2.4 para os participantes representados (estão na 3.2.7) e a uma seção 3.2.8, que não existe; a frase do Kappa do enquadramento traz a chamada da nota 2, que é a nota do OntoViz.
- Na 3.2.1, o material sem perspectiva tem as divisões "genre, activity, and contextualization", e o parágrafo descreve a primeira com o nome "Provenance".
- O perfil aparece escrito @ze__president e @ze_president.

## Citações

- "Montage videos contain at least four eventualities and four shots, normally collecting various materials referring to the same represented participant"
- "breaking out of the typical TikTok tendency to produce shorter, dynamically cut videos that attract attention"
- "The corpus of 20 videos analyzed in the pilot study can clearly not be representative of all the general tendencies"

## Lacuna

O texto não diz como a duração do plano foi medida nem como as médias foram agregadas, não dá desvio, mediana nem faixa, nem relata teste para o "significantly shorter"; os valores de Kappa e os números das Figuras 17 e 18 ficam só nas imagens. No grupo popular, dá 3 vídeos de fala e 5 de montagem e não diz o formato dos outros dois. Não liga a duração de plano a retenção, alcance ou outra medida de desempenho, nem compara com o TikTok em geral.
