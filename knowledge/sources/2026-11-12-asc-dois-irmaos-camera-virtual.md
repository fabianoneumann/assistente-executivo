---
titulo: "Onward: Quest for Magic"   # no HTML, o título traz um caractere invisível (U+FEFF) entre "Onward: " e "Quest"; aqui sem ele
tipo: artigo
autor: "Jay Holben (American Cinematographer)"   # linha "By Jay Holben" na página e autor do JSON-LD
url: "https://theasc.com/article/onward-quest-for-magic/"
publicado_em: 2020-03-12   # data na página ("March 12, 2020") e meta article:published_time; o dateModified do JSON-LD é 2026-04-29
capturado_em: 2026-11-12
licenca: "protegido (a página lida não traz aviso de copyright nem licença de conteúdo; o rodapé liga a 'Terms of Use', não aberto; legenda: 'All images courtesy of Disney/Pixar'); ficha de estudo em palavras próprias, sem o integral"
areas: [generative-media]
tags: [pixar, virtual-camera, cinematography, layout, staging, virtual-lens, anamorphic, lens-distortion, depth-of-field, focus, camera-capture, steadicam, camera-shake, lighting, color-grading, presto, renderman, reporting]
---

# American Cinematographer: a fotografia de *Dois Irmãos*, com a câmera e a luz da Pixar

Ficha de estudo de entrevista: as seções seguem a ordem da matéria (a abertura, as perguntas da entrevista e a caixa "Ardent Supporters"), com as falas atribuídas a quem as disse, em palavras próprias, e o método em tabelas. Não há integral: a matéria é protegida.

**Proveniência.** Entrevista de Jay Holben na *American Cinematographer*, revista da American Society of Cinematographers (ASC), https://theasc.com/article/onward-quest-for-magic/, marcada "Interview" e datada de 12/03/2020, baixada com curl em HTML em 2026-11-12 e lida no texto extraído (a cópia de trabalho `2026-11-12-linguagem-de-camera-virtual`), conferido no HTML para título, data e autor. O HTML não tem bloco `<article>` nem `<main>` de mais de 3.000 caracteres, então o texto extraído é o da página inteira, com o menu (repetido quatro vezes) e o rodapé; o sha256 do `protegidas.json`, (hash omitido), é o desse texto da página inteira sem tags, script e estilo (refeito nesta ficha, igual). Sem captura na Wayback (a consulta a `archive.org/wayback/available` voltou vazia). Título conferido no `<title>`, no `og:title` e no `<h1>`. Cobertura: a matéria inteira, do subtítulo e da abertura às perguntas, às legendas das imagens e à caixa "Ardent Supporters", com quatro membros da ASC; ficam fora o menu, a lista "Read More" e o rodapé. Não foram vistas as imagens nem abertos os links (a matéria relacionada sobre *Toy Story 4*, as edições citadas da revista, o podcast).

**Por que ficha de estudo, e não nota de fato.** O pedido sugeria nota de fato de reportagem, mas a matéria tem cerca de 4.000 palavras de conteúdo (umas 3.000 na entrevista e umas 1.000 na caixa), bem acima do limite de fonte curta do `README.md` desta pasta, e é uma entrevista em perguntas e respostas, cuja ordem é a das perguntas; por isso a ficha segue essa ordem, com o ângulo da matéria numa linha e as falas atribuídas, como na reportagem.

**Quem fala.** O entrevistador da revista e os dois diretores de fotografia do filme: Sharon Calahan, ASC, de luz, e Adam Habib, de câmera; na abertura, uma declaração de imprensa do diretor Dan Scanlon; na caixa, Dennis Muren, Steven Poster, Stephen Goldblatt e Daryn Okada, membros da ASC que apoiaram a entrada de Calahan.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). O `parafrase.py` contra o texto extraído da página inteira saiu com o código 3 (ficha em português, fonte em inglês): 71 unidades medidas (31 de prosa, 40 de célula com texto); fora da conta, 131 células de fato, 40 de cabeçalho e 8 frases curtas demais para medir; 1 colada de 71 (1%, a legenda com os nomes de Scanlon e Kelsey Mann); 0 trecho de 3 ou mais seguidas. Pela conta lado a lado, sobre as mesmas 71 unidades, 51 seguiam uma frase da fonte: todas as células com texto e as frases de prosa das seções numeradas e da caixa, que traduzem ou fundem falas da entrevista. Ficam fora as frases do formato, desta conferência, da proveniência, do porquê do formato e de "Quem fala", a de "Em uma frase" e o ângulo, que juntam lugares distantes da matéria, e as três da lacuna. A maior sequência de unidades seguidas que seguiam a fonte na ordem dela tinha 16 (do refletor invisível, na seção 4, ao pedido de abrir o diafragma e à razão para vigiar o foco, na seção 7). Na revisão, as seções 4 a 7 foram reescritas: linhas reagrupadas por outro critério (o que se imita da luz real, para que serve cada experimento, de onde vem cada imperfeição), o parágrafo do estágio aberto pelo porquê e as legendas do pipeline fundidas numa célula. O `parafrase.py` passou a medir 69 unidades (31 de prosa, 38 de célula), 1 colada (a mesma legenda) e 0 trecho; das cerca de 16 unidades dessas seções, 3 ainda acompanham de perto uma frase da fonte (a ferramenta de cor falsa, as imperfeições em camadas, o ator de chroma verde), o total da ficha fica em cerca de 37 de 69, e nenhuma sequência ali anda mais de 2 unidades para a frente na fonte. Depois, a seção 3 (as anamórficas) também foi reescrita: a tabela das lentes vem primeiro, ordenada do visual menos para o mais marcado, e a origem da escolha vem depois, de trás para a frente; das 8 unidades dela, 2 ainda acompanham de perto uma frase da fonte (a pergunta e a observação sobre os filmes dos anos 1980) e nenhuma sequência anda mais de 2 unidades para a frente; fora das seções 3 a 7 a conta não foi refeita (revista em 2026-11-19). No texto argumentativo (as razões da divisão entre layout e luz, a razão da marcação de cor, o porquê da anamórfica e das ferramentas de luz, o fecho dos dois e os argumentos da caixa) não há três unidades seguidas que andem para a frente na fonte: as razões da divisão vão em ordem inversa, depois dos papéis; na marcação de cor, a razão de fundo vem por último; o fecho põe Habib antes de Calahan; e a caixa vai do último ao primeiro membro, com a abertura dela no fim.

## Em uma frase

Entrevista da revista da ASC com os dois diretores de fotografia de *Dois Irmãos* (*Onward*), em que a câmera e a luz da Pixar são descritas como fotografia de cinema, com lentes reais imitadas, imperfeições de operador gravadas e ferramentas de foco próprias.

**Ângulo da matéria:** a fotografia de animação como fotografia de verdade, a ponto de a caixa final reunir os membros da ASC que defenderam a entrada de Calahan na sociedade.

## Abertura: o filme e os dois diretores de fotografia

| Ponto | Fato |
|---|---|
| Filme | *Onward*, da Pixar |
| Premissa | dois irmãos elfos adolescentes, Ian e Barley, tentam rever o pai morto por um feitiço que dá errado e traz só as pernas e os pés dele; têm 24 horas para achar outra gema mágica |
| Origem, pela declaração de Scanlon | a relação dele com o irmão e com o pai, morto quando ele tinha cerca de um ano; uma fita em que o pai diz só "hello" e "goodbye" |
| Cargos | Calahan, "director of photography: lighting"; Habib, "director of photography: camera" |
| Créditos das fotos de bastidor | Deborah Coleman, Adam Habib, Patrick Lin, Gairo Cuevas; imagens cedidas pela Disney/Pixar |

| Pessoa | Trajetória, pela matéria |
|---|---|
| Sharon Calahan | na Pixar desde 1994; supervisora de luz em *Toy Story*; diretora de fotografia em *A Bug's Life*, *Toy Story 2*, *The Good Dinosaur*, *Cars 2*, *Ratatouille* e *Finding Nemo*; formada em design gráfico, ilustração e fotografia; diretora de arte de TV e diretora de luz na Pacific Data Images antes; primeira fotógrafa de animação a entrar na ASC; no ramo de fotografia da Academia |
| Adam Habib | mestrado (M.F.A.) em cinema na University of Southern California; na Pixar desde 2010 como artista de câmera e encenação; artista principal em *Inside Out*; diretor de fotografia de câmera no curta *Lou*; *Onward* é o primeiro longa dele no cargo |

## 1. Como as duas funções se dividem

| Ponto | Fato | Quem diz |
|---|---|---|
| Dois departamentos de fotografia | layout e luz | Calahan |
| O que cabe a Habib | encenação e composição de cada cena; lente, movimento de câmera e escolha de plano | Calahan |
| Com quem Habib trabalha | montagem e story; com a equipe de cenário, na previs, para caber a ação em cada ambiente | Calahan |
| Pré-luz | Calahan acompanha o plano da câmera e já ilumina o grosso para saber onde caem as sombras | Calahan |
| O que cabe a Calahan | o visual de luz do filme inteiro: arte conceitual, colorscript, desenho de luz e marcação de cor final, no Nucoda, da Digital Vision | Calahan |
| Volume por semana, na luz | cerca de 10 cenários e uns 150 planos | Calahan |
| Por que a divisão se mantém | duas equipes grandes trabalhando ao mesmo tempo, cada uma com o seu chefe | Calahan |
| Por que é difícil juntar | luz e layout usam ferramentas feitas sobre plataformas de software diferentes | Calahan |
| De onde vem a divisão | da animação em acetato da Disney, origem de muita gente de *Toy Story* | Calahan |
| Como os dois se entrosaram | muitas reuniões no começo, trocando referências, mais para conhecer o gosto do outro que para fechar uma visão | Habib |

**A marcação de cor numa imagem toda fabricada.** O caso difícil de *Onward*, conta Calahan, foi a pele azul das personagens, que sob luz colorida puxava para o verde, o cinza ou o roxo e foi acertada com máscaras na sessão com o colorista Mark Dinicola, porque o diretor reparava nisso (e até na animação, brinca ela, há luminária da cor errada). Acertar a pele na luz de cada plano não resolveria, diz, com uns 30 artistas iluminando sequências diferentes. A sessão existe pela continuidade: são de 30 a 60 iluminadores, e o filme tem de parecer de uma visão só.

| Legenda | Fato |
|---|---|
| Storyboard de Le Tang | um de cerca de 488 da sequência "Conjuring Dad" |

## 2. Como se definiu o visual com o diretor

| Ponto | Fato | Quem diz |
|---|---|---|
| Material reunido | referências de filme, foto, ilustração e pintura; muita arte conceitual; filmes vistos juntos | Calahan |
| O que sai daí | um plano de câmera e um plano de luz, que mudam ao longo da produção | Calahan |
| Oficina de luz real | rara, por custo e agenda: alguém demonstra luz no mundo físico | Calahan |
| Exemplo | oficina de luz de carro com Bill Bennett, ASC, antes de *Cars 3* | Calahan |

## 3. As lentes anamórficas

O ponto de partida da pergunta é a inspiração do visual nas anamórficas Cooke /i. Na resposta de Habib, a lente muda com o arco dos meninos; a tabela põe as três aparências da menos para a mais marcada, e o parágrafo seguinte conta, de trás para a frente, como a escolha se firmou.

| Aparência imitada | Quanto marca a imagem | Em que trecho do filme |
|---|---|---|
| Arri/Zeiss Ultra Prime | pouco: esférica, imagem mais plana e limpa | a vida comum dos dois irmãos |
| Cooke S4 | meio-termo entre a limpeza da Ultra Prime e o caráter da anamórfica | o terceiro ato |
| anamórfica | muito: distorção com mais caráter, e cada focal do jogo com grau e tipo de distorção definidos na Camera and Staging (a de 50 mm difere da de 35 mm) | da partida na busca em diante, quando a aventura engrena |

Scanlon só aderiu depois de um teste: ele tinha dúvidas, a equipe trouxe uma Arri Alexa Mini com anamórficas Cooke, e foi a textura que a lente dava ao fundo que o convenceu. A ideia vinha de uma observação sobre o gênero, a de que os filmes de fantasia dos anos 1980 usados como referência (*Labyrinth*, *The Goonies*, *The Dark Crystal*) eram todos anamórficos. Para Habib, o que ganhou todo mundo foi o eco desses filmes antigos e a textura própria da lente, que dá licença para a magia acontecer; tornar esse visual viável dependeu também de Calahan e da equipe dela.

## 4. A luz, comparada à de um set

| Ponto | Fato | Quem diz |
|---|---|---|
| Até onde vai a física | as ferramentas partem dela, mas só a aproximam, e sobra margem para estilizar e "fudging physics"; o resultado puxa mais para a pintura que para o fotorrealismo | Calahan |
| Vantagem sobre o set | a fonte vai onde se quiser, até no meio do quadro, sem precisar esconder; se a grama verde tinge a pele, basta um rebatedor invisível de outra cor | Calahan |
| O que se copia de um refletor de verdade | o efeito (qualidade, intensidade, cor), montado com fontes de forma e tamanho básicos; pedir um 20K pelo nome dá, mas quase não se faz | Calahan |

## 5. Os experimentos da preparação

Os quatro tipos de "weird science experiments", nas palavras de Habib:

| Para quê | Experimento |
|---|---|
| Animar a equipe, sem buscar visual nenhum | alguns servem só para isso |
| Antever o pai que volta só da cintura para baixo | um ator de roupa de chroma verde, com calça e sapato, filmado correndo |
| Saber se a equipe aprova o "visual anamórfico" | mostrá-lo em fotografia, em vez de descrevê-lo |
| Tirar ideias de encenação | filmar um ator fazendo a ação |

| Legendas das imagens | O que dizem |
|---|---|
| O pipeline, etapa por etapa | a Camera and Staging faz dos momentos do storyboard os planos do filme, compostos com os princípios da fotografia; a animação parte desse layout sugerido e do diálogo gravado para criar a atuação das personagens; a luz integra tudo numa imagem só, com fontes virtuais que iluminam personagens e cenário, guiam o olho às áreas-chave e dão o clima |

Para Habib, o artista de computação gráfica ganha muito ao sentir uma câmera de verdade nas mãos. Foi o que ele levou ao estágio em sala de aula que a Pixar criou depois de *Onward* para ensinar o processo de Camera and Staging: com os estagiários, vindos quase todos de escola de arte ou de animação, aproveitou a visita de um representante da Zeiss com lentes novas e uma Sony Venice numa cabeça fluida para que eles olhassem pelo visor, fizessem pan e tilt e sentissem o peso da câmera e a resistência da cabeça.

## 6. As imperfeições de propósito

| Ponto | Fato | Quem diz |
|---|---|---|
| O tremor da estrada | como boa parte do filme é viagem, filmou-se de verdade com a câmera em suportes de carro, e Leo Santos, artista principal, rastreou a vibração no Nuke, da Foundry | Habib |
| O passo de quem carrega a câmera | uma biblioteca de movimentos comuns (caminhada, corrida, andar furtivo) gravada pelo operador de steadicam Nick Schwyter, em sessões de captura que Jan Pfenninger, artista principal, conduziu | Habib |
| A reação do operador | parte das câmeras de *Onward* teve o movimento capturado, para guardar o jeito de quem opera respondendo à atuação | Habib |
| O destino de tudo | tudo isso entra em camadas sobre os planos | Habib |
| O risco de perder | nem toda imperfeição sobrevive: em *Inside Out*, um foco atrasado de propósito passava por erro, era "corrigido" e teve de ser reposto umas 20 vezes no caminho pelo pipeline | Habib |

| Legenda | Fato |
|---|---|
| Scanlon e o supervisor de story Kelsey Mann | trabalhando com equipamento de realidade virtual |

## 7. Profundidade de campo e foco

| Ponto | Fato | Quem diz |
|---|---|---|
| Ferramenta nova do filme | uma "cor falsa" de foco, no molde da de exposição: verde no que está em foco, amarelo à frente da faixa nítida, vermelho atrás dela | Habib |
| O tom do filme | regras de profundidade de campo, diafragma, obturador, ISO e níveis de luz conforme a hora do dia, discutidos cedo e acertados na prática (uma passada, olhar o resultado) até agradar aos dois e ao diretor | Calahan |
| Por que ela fez falta | Calahan pedia muitas vezes mais um ponto de diafragma aberto, e Habib em geral topava; com a profundidade mais rasa, ficava difícil saber o que estava nítido, e até na animação uma personagem sai fora de foco sem ninguém querer | Habib |

| Legenda | Fato |
|---|---|
| Plano aberto de paisagem | profundidade de campo maior, para parecer real |
| Raios de sol entre nuvens | outro exemplo de profundidade maior |

## 8. Software

| Uso | Programa | Quem diz |
|---|---|---|
| Layout de câmera | Presto, proprietário, o mesmo da animação | Calahan |
| Luz | Katana, da Foundry, muito adaptado | Calahan |
| Render | RenderMan | Calahan |

## 9. O fecho: fotografia sem câmera física

| Quem | O que diz, em resumo |
|---|---|
| Habib | lente e luz são o que liga o virtual ao físico, e por isso tudo é fotografia; o diretor de fotografia de animação e o de filmagem com atores perguntam a mesma coisa: como contar a história com a imagem |
| Calahan | cita como inspiração o cruzamento de Lubezki em *Gravity* e de Caleb Deschanel em *The Lion King*; a animação tem poucas regras e vai da pintura 2D de *Into the Spider-Verse* ao quase-foto de *The Lion King*; e, depois da fala de Habib, "It’s all about making images" |

## A caixa "Ardent Supporters"

| Quem | Como a conheceu | O argumento |
|---|---|---|
| Daryn Okada, ASC | em meados dos anos 2000 | na animação, o crédito de diretor de fotografia nem sempre é de quem faz fotografia, mas ela pesquisa a história, procura locações pela essência, cor e textura e chefia a equipe como numa filmagem; parte da página em branco e pensa a pele e o rosto de cada personagem; ajudou a mostrar o paralelo aos colegas, e ela passou do ramo de animação ao de fotografia da Academia |
| Stephen Goldblatt, ASC, BSC | em sessões de exibição na Pixar | a Pixar achava que ela devia ter crédito de diretora de fotografia, e ele concordou; em *Ratatouille*, ela foi a fotógrafa em tudo; fora da equipe e da fotografia tradicionais, o fotógrafo é um "visualizer" |
| Steven Poster, ASC | numa visita à Pixar | o trabalho dela é tão fotográfico quanto o da filmagem; ela conhece cor e fluxo de trabalho e, na época, desenhava a passagem de cor de linear para log, para a animação parecer película; compara com *Gravity*; chama-a de pintora |
| Dennis Muren, ASC | — | via paralelo com o trabalho dele em miniaturas, stop-motion e efeitos; ela parte de um quadro em preto e branco do visual e o colore pelo próprio gosto, com trapaças impossíveis na fotografia física, buscando o impacto emocional; diz que deixou de prever o futuro, mas põe o trabalho dela nessa categoria |

A caixa abre lembrando que, em 2013, Calahan foi a primeira fotógrafa admitida na ASC por trabalho em animação, e reúne quatro membros que a apoiaram, aqui do último ao primeiro.

## Citações

- "how the unique texture gives permission for magical things to happen." (Adam Habib, sobre as lentes anamórficas)
- "We layered all these imperfections into the shots to create that physical believability." (Adam Habib)
- "When there is a lens and there is light, there is cinematography, even if those lenses and lights are virtual!" (Adam Habib)

## Lacuna

A matéria não dá distâncias focais além dos exemplos de 35 mm e 50 mm, nem o grau de distorção de cada lente, os valores de diafragma ou as regras de profundidade de campo de cada parte do filme. Não diz quantos planos usaram câmera capturada, como a biblioteca de steadicam e a vibração de carro foram aplicadas à câmera virtual (em camadas sobre qual movimento, com que ajuste), nem como a cor falsa de foco funciona no Presto. As imagens, que mostram storyboards, mapas de lente e planos, não foram vistas.
