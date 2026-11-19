---
titulo: "Sets and Cameras | The Science Behind Pixar"
tipo: artigo
autor: "Museum of Science, Boston, com a Pixar Animation Studios"   # rodapé: "This exhibition was developed by the Museum of Science, Boston in collaboration with Pixar Animation Studios"; a página não tem assinatura de pessoa
url: "https://sciencebehindpixar.org/pipeline/sets-and-cameras"
publicado_em: null   # a página não traz data; o único indício no HTML é o caminho do vídeo do Luca (".../2024-05/luca-sets-web.mp4"), que é a pasta de envio do arquivo, não a data da página
capturado_em: 2026-11-12
licenca: "protegido (rodapé: 'All exhibition photos © Michael Malyszko' e 'All other images © Disney/Pixar'; sem licença de conteúdo declarada para o texto); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [pixar, virtual-camera, cinematography, layout, staging, camera-movement, set-design, procedural-generation, animation-pipeline]
---

# The Science Behind Pixar: a etapa de cenários e câmeras, antes da animação

Nota de fato: tabelas do que a página da exposição diz sobre a etapa "Sets and Cameras", com prosa só para dizer o que a fonte é, o que ela afirma e o que falta. A página explica um processo e não dá recomendação, por isso a seção de síntese é "O que a fonte afirma". Não há integral: a página é protegida.

**Proveniência.** Página da etapa "Sets and Cameras" do site da exposição The Science Behind Pixar, https://sciencebehindpixar.org/pipeline/sets-and-cameras, baixada com curl em HTML em 2026-11-12 e lida no texto extraído (a cópia de trabalho `2026-11-12-linguagem-de-camera-virtual`), conferido no HTML, inclusive os textos alternativos das imagens. O HTML não tem bloco `<main>` nem `<article>` de mais de 3.000 caracteres, então o texto extraído é o da página inteira, com o menu das etapas e o rodapé; o sha256 do `protegidas.json`, (hash omitido), é o desse texto da página inteira sem tags, script e estilo (refeito nesta ficha, igual). Wayback: `http://web.archive.org/web/20260408051509/https://sciencebehindpixar.org/pipeline/sets-and-cameras`. Título conferido no `<title>` ("Sets and Cameras | The Science Behind Pixar") e no `og:title` ("Sets and Cameras"). Cobertura: o texto inteiro da etapa (a frase de abertura, a descrição do vídeo do *Luca*, as quatro perguntas, a legenda da imagem de *A Bug’s Life* (*A Bug’s Life*), as caixas de vídeo, de atividade e do Pixar in a Box, a pergunta do "Ask a Pixar Scientist" e o rodapé). Não foram vistos o vídeo do *Luca*, o "Pixar's Sets Challenge" nem o vídeo de Sylvia Wong; não foram abertas a atividade da grama, as aulas do Pixar in a Box nem as outras perguntas do "Click for More".

**Quem fala.** O Museum of Science de Boston, que desenvolveu a exposição com a Pixar; o texto explicativo não é assinado, e a resposta do "Ask a Pixar Scientist" vem com o nome de quem respondeu.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). O `parafrase.py` contra o texto extraído da página inteira saiu com o código 3 (ficha em português, fonte em inglês): 23 unidades medidas (18 de prosa, 5 de célula com texto); fora da conta, 73 células de fato, 9 de cabeçalho e 12 frases curtas demais para medir; 1 colada de 23 (4%, a célula que lista os nomes das aulas do Pixar in a Box); 0 trecho de 3 ou mais seguidas. Pela conta lado a lado, sobre as mesmas 23 unidades, 7 seguem uma frase da fonte: a frase de "Quem fala" (o rodapé do museu), a de "Em uma frase" (que traduz a abertura da etapa e a frase do diretor de fotografia), e as cinco células com texto (o que se fecha na etapa, a cena do *Luca*, que funde as frases da descrição do vídeo na ordem delas, a legenda da imagem de *A Bug’s Life*, a lista do Pixar in a Box e a resposta de Peter Collingridge). Ficam fora as frases do formato, da proveniência e desta conferência, as duas de "O que a fonte afirma", que juntam lugares diferentes da página em outra ordem, e as três da lacuna. A maior sequência de unidades seguidas que seguem a fonte na ordem dela tem 5 (as cinco células com texto, da etapa à resposta do cientista): são fatos e legendas descritivas, espalhados por tabelas de células de fato, e se declaram aqui; não há texto argumentativo da fonte em sequência.

## Em uma frase

Página educativa de uma exposição feita com a Pixar que descreve a etapa em que o cenário e a câmera ficam prontos, antes da animação, e trata o artista de câmera como diretor de fotografia do mundo virtual.

## A etapa no processo

| Ponto | Fato |
|---|---|
| Nome da etapa | Sets and Cameras |
| Ordem no menu do site | Story & Art, Surfaces, Simulation, Modeling, Sets & Cameras, Lighting, Rigging, Animation, Rendering |
| O que se fecha nela | os ângulos de câmera e o movimento básico das personagens |
| O que fica para depois | a ação das personagens, na etapa de animação |
| Título da seção de vídeo | "Virtual cameras view virtual 3D worlds" |

## O exemplo do *Luca*, pelo texto do vídeo

| Ponto | Fato |
|---|---|
| Cena | Guilia (grafia da página) entra de bicicleta na piazza, desce, tira um peixe da carroça presa à bicicleta, agita o peixe diante de quem a provoca, discute e vai embora |
| Câmera | já no lugar |
| Peças do cenário | já no lugar |
| Personagens | quase paradas |
| Boca nas falas | imóvel |
| Deslocamento | deslizam de um ponto a outro |

## Cenário e câmera, pelas quatro perguntas

| Papel | Ponto | Fato |
|---|---|---|
| Cenário (set) | O que é | o ambiente virtual onde a história se passa |
| Cenário (set) | O que o ambiente da cena transmite | contexto, história, emoção |
| Cenógrafo (set designer) | Comparado a | arquiteto |
| Cenógrafo (set designer) | Trabalho | ambiente virtual construído do zero |
| Cenógrafo (set designer) | Exemplos de peça | seixo, árvore, prédio |
| Cenógrafo (set designer) | Ponto de partida | os storyboards |
| Cenógrafo (set designer) | Modo 1 | peça modelada uma a uma, como as personagens |
| Cenógrafo (set designer) | Modo 2 | cenário gerado por programa (procedural) |
| Câmera | Função | a nossa janela para o mundo 3D virtual |
| Câmera | O que cada enquadramento diz | para onde olhar; o que sentir |
| Artista de câmera (camera artist) | Comparado a | diretor de fotografia do mundo virtual |
| Artista de câmera (camera artist) | Escolhas | composição; movimento de câmera; tipo de lente |
| Artista de câmera (camera artist) | Critério | servir à história |
| Imagem de *A Bug’s Life*, em cima | O que mostra | o lugar da câmera, um círculo azul, que decide o que o público vê |
| Imagem de *A Bug’s Life*, embaixo | O que mostra | a vista da câmera virtual |

## O resto da página

| Caixa | Fato |
|---|---|
| Vídeo | "Pixar's Sets Challenge" |
| Vídeo | "Programming natural sets", com Sylvia Wong, Layout Technical Director |
| Atividade | "Programming Natural Variety": um campo de grama |
| Parâmetros da atividade, por folha | cor; aglomeração ("clumpiness"); altura; direção da dobra |
| Seletor da atividade | aleatoriedade: folhas quase iguais ou quase diferentes |
| Pixar in a Box | aulas da Pixar com a Khan Academy: Environmental Modeling, Sets and Staging, Virtual Cameras |
| Ask a Pixar Scientist, pergunta | de "Daisy": por que usar matemática em vez de só desenhar |
| Ask a Pixar Scientist, resposta | de Peter Collingridge: milhões de folhas de grama que se mexem com o vento ou com cavalos passando dão menos trabalho assim |
| Apoio | Google; Institute of Museum and Library Services; National Science Foundation (Grant No. 1339244); Science Museum Exhibit Collaborative |

## O que a fonte afirma

Pela página, o ponto de vista se resolve antes da atuação: quando a cena chega à animação, câmera e cenário já estão fixos e a personagem só desliza pelas marcas, sem mexer a boca. Quem decide esse ponto de vista é tratado como diretor de fotografia, e lente, composição e movimento respondem à história; parte do mundo filmado sai de regras de programa, que a resposta do cientista justifica pela economia de trabalho.

## Citações

- "In this stage of the process, the camera angles and the basic motions of the characters are finalized."
- "Camera artists are cinematographers of the virtual world."
- "Camera artists choose the composition, camera movement, and lens type to support the story."

## Lacuna

A página não tem data e não diz com que programa a câmera é posta nem movida, que lentes ou distâncias focais se usam, nem regra alguma de movimento (duração, velocidade, aceleração). Não diz se a etapa é o que outras fontes chamam de layout, embora o cargo de Sylvia Wong tenha esse nome, nem se câmera e cenário voltam a mudar depois que a animação começa. Os vídeos, que mostram a etapa em imagem, não foram vistos.
