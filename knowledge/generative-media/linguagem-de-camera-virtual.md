# Linguagem de câmera virtual: a gramática clássica, a câmera da animação, o vertical e a passagem a código

O vocabulário de plano e de movimento do cinema, o que os estúdios de animação fazem com a câmera virtual, o que muda no 9:16, como cada nome vira parâmetro no Three.js, no Blender e nos motores, e o que disso serve a um teste de câmera e à skill de roteiro (`piece-script`). Pesquisa rasa nas três frentes (62 buscas: 18 Perplexity, 18 Gemini e 26 nativas; pior caso de US$ 1,80), revisada com conferência e re-revisão. O mundo 3D com a câmera viajando por estações está em [[mundo-3d-com-camera-por-codigo]]; o cenário em 2,5D e o catálogo de câmera do HyperFrames, em [[ambiente-da-cena-em-video-por-codigo]]; os princípios de movimento, em [[principios-de-motion-design]].

**O que a base já tinha:** os sete planos, as dez indicações de câmera, o eixo e a câmera que "só se move por um motivo concreto" do livro de Doc Comparato (*Da criação ao roteiro*, 2009, cap. 9 e o glossário do anexo 2; obra protegida, sem ficha no repositório); a área segura do Reels em [[carrossel-instagram]]; e o `motion.md` do HyperFrames, a única fonte com números de câmera: `power2.inOut`, movimento rápido de 0,3 a 0,6 s, órbita de fundo de 3 a 5° por segundo e o empurrão lento no fim da cena entre os padrões que soam gerados, todos padrões que um momento de propósito derruba ([[2026-11-11-hyperframes-catalogo-camera-3d-e-traco-a-mao]]).

## A gramática clássica

| Nome | O que a câmera faz | Fonte |
|---|---|---|
| Pan | gira para a esquerda ou a direita sobre um eixo fixo | LMU, LibreTexts |
| Tilt | gira para cima ou para baixo | LMU, LibreTexts |
| Dolly | anda para dentro ou para fora, num aparelho que se move | LMU, LibreTexts |
| Truck ou track | anda para a direita ou a esquerda | LMU (na LibreTexts, "tracking" é seguir o assunto) |
| Pedestal | sobe ou desce inteira, sem girar, o que a separa do tilt | LibreTexts |
| Arco | anda em volta do assunto, sem precisar fechar o círculo | LibreTexts |
| Jib | uma grua pequena | LMU |
| Dolly zoom | anda e muda a distância focal ao mesmo tempo, mantendo o assunto do mesmo tamanho | Wikipedia |

Fontes: [[2026-11-12-lmu-no-nonsense-filmmaking-movimento-e-direcao-de-tela]] (CC BY-NC-SA, só ficha; o integral em https://lmu.pressbooks.pub/filmmaking/chapter/movement/ e https://lmu.pressbooks.pub/filmmaking/chapter/screen-direction/), [[2026-11-12-libretexts-movimentos-de-camera]] (CC BY-NC, só ficha; o integral na `url` da ficha), [[2026-11-12-wikipedia-regra-dos-30-graus-e-dolly-zoom]]. A LibreTexts manda ensaiar o movimento e ter ponto de partida e de chegada definidos, sem vagar.

- **Os nomes variam entre as fontes:** "tracking" é só lateral na LMU e é seguir o assunto na LibreTexts; no Comparato, o travelling serve a todo trajeto mais ou menos horizontal e também ao de acompanhar a personagem; no Unreal, o trilho imita o dolly que faz os "tracking shots". **Leitura do assistente:** o projeto precisa de um vocabulário fixo e da tradução de cada nome para o parâmetro do motor (abaixo, "Da câmera ao código").
- **O eixo e como cruzá-lo:** a LMU dá três modos de cruzar sem confundir: o personagem cruza a linha e cria outra, a câmera cruza num movimento contínuo, ou a câmera para sobre a linha e a neutraliza. O Comparato dá o preceito sem os modos.
- **A regra dos 30° e a dos 20 mm** (Wikipedia, verbete com aviso de falta de citações desde 2017; a frase dos 20 mm aponta para Hurbis-Cherrier, *Voice & Vision*, não aberto): entre dois planos seguidos do mesmo assunto, a câmera muda pelo menos 30°, senão o corte parece um jump cut; menos de 20 mm de diferença de distância focal no mesmo ângulo dá o mesmo efeito; o corte axial dispensa os 30°, não os 20 mm. Leitura do assistente: 20 mm não pesam igual numa lente de 24 e numa de 100 mm, então a regra é aproximada.
- **O dolly zoom**, pela Wikipedia (que sustenta a autoria num post do Substack de 2025), foi criado por Irmin Roberts, da segunda unidade da Paramount, para *Vertigo*; também se chama Hitchcock shot, Vertigo shot, Jaws effect ou zolly. A conta do `camera-dolly-zoom` do HyperFrames (`d * tan(FOV/2) = const`) e a da Wikipedia são a mesma geometria (leitura do assistente).
- **A velocidade de panorâmica** ([[2026-11-12-red-velocidade-de-panoramica]], texto de fabricante de câmeras): o estrobo depende de quão rápido a cena atravessa a tela; a regra de partida é não passar de uma largura de imagem a cada sete segundos, medida em larguras, então vale para qualquer lente; supõe cena estática, 24 fps e obturador de 180°; obturador maior borra mais, menor picota mais; o pan que segue um assunto perto da câmera e o chicote borrado (swish pan) fogem da regra. A atribuição dos 7 s à ASC, em fóruns, não fecha em primária.
- **Motivado, lógico e ilógico** ([[2026-11-12-schrader-film-comment-movimento-de-camera]], página 1 de 4): o movimento motivado segue a ação; o não motivado é lógico quando a câmera faz o que o espectador quer ou precisa (chegar perto do gesto, da emoção que cresce) e ilógico quando o narrador se impõe e a câmera chama atenção para si; Schrader defende o não motivado. Leitura do assistente: no vídeo didático, em que nada se move na cena e a câmera vai aonde a fala aponta, o movimento é quase sempre o lógico.
- **O enquadramento de gente** (*Cinematography: Theory and Practice for Cinematographers and Directors (amostra da 4.ª edição)*, de Blain Brown (https://api.pageplace.de/preview/DT0400.9781000433692_A41593664/preview-9781000433692_A41593664.pdf), amostra oficial, caps. 1 e 2): o espaço de cabeça e o espaço de olhar contra a tendência de centrar a cabeça, a regra dos terços como ponto de partida, a altura da lente, o dutch tilt e as proporções de tela de 1,33 a 16:9. O capítulo de movimento (motivado e não motivado, contramovimento, revelação) está só no sumário da amostra.
- **Lente e profundidade de campo:** as faixas em milímetros (grande-angular abaixo de cerca de 35, normal perto de 50, teleobjetiva acima de 70 a 85), os diafragmas de foco raso e profundo e a regra de que a perspectiva vem da distância e não da lente ficam **não verificados**: só as respostas os dão.

## A câmera virtual na animação

- **Nenhuma fonte lida dá número da Pixar ou da Disney para a duração de um movimento de câmera,** e a Perplexity diz que não há número universal da Disney ou da Pixar. O que a Pixar publica são regras de aparelho e de lente.
- **A câmera virtual imita o aparelho físico, e o estilo dela conta a história** ([[2026-11-12-studiodaily-divertida-mente-camera-da-pixar]], reportagem de 2015 com o diretor de fotografia Patrick Lin): em *Divertida Mente*, o mundo de dentro usou lentes virtuais que reproduzem as Ultra Prime, de pouca distorção, e câmera de estúdio em trilhos e gruas; o de fora, as Cooke S4, de distorção exagerada, com steadicam e câmera na mão, com movimentos capturados de câmeras reais. No segundo ato, a câmera de dentro parece menor porque anda mais rápido, com aceleração e frenagem mais curtas; quando Alegria entende, a câmera empurra para um plano fechado. Em *Dois Irmãos*, a vibração veio de filmagens reais em suporte de carro, e um operador de steadicam gravou por captura uma biblioteca de movimentos ([[2026-11-12-asc-dois-irmaos-camera-virtual]]).
- **A câmera fica pronta antes da animação:** o "camera artist" escolhe composição, movimento e lente para servir à história na etapa de cenários e câmeras ([[2026-11-12-sciencebehindpixar-cenarios-e-cameras]]); depois do layout, a câmera sai do alcance do animador, que trabalha dentro do plano e da duração já fixados ([[2026-11-12-schnitzer-como-fazer-cutscene-melhor-2003]], de 2003, de um autor que diz ter trabalhado na LucasArts e na Pixar; leitura do assistente: vale como processo, não como regra atual).
- **O multiplano** ([[2026-11-12-toonboom-harmony-multiplano]]): camadas espalhadas no eixo Z, com a câmera passando entre elas; cada camada se desenha inteira, porque o pan ou o zoom revela o que estava escondido; a ferramenta Maintain Size muda a profundidade sem mudar o tamanho aparente. Que o mais longe anda mais devagar já estava na base ([[ambiente-da-cena-em-video-por-codigo]]).
- **O pan na animação clássica:** de *Timing for Animation*, de Whitaker e Halas, só abriu a prévia oficial do começo de cada seção; a de "Strobing" diz que o estrobo aparece no movimento de elementos iguais e espaçados, como degraus e raios de roda, sem número (citação: https://www.oreilly.com/library/view/timing-for-animation/9781000338225/xhtml/74_Chapter64.xhtml). Os limites por quadro e os quadros de aceleração que as respostas atribuem ao livro ficam não verificados.
- **Leitura do assistente:** o ease também é linguagem, não só suavidade: na reportagem da Studio Daily, a aceleração mais curta faz a câmera parecer menor e mais ágil, o que dá a um teste uma variável a medir (o mesmo trajeto com o `power2.inOut` longo e curto).

## O vertical

- **Plano fechado não é regra do 9:16.** Em 1.194 vídeos de TikTok, Reels e Shorts recolhidos em 2023 por alunos, com a escolha pelo algoritmo e pelo gosto de quem coletava, o "abierto" é o mais comum (49,62%, 61,81% e 54,64%) e o "cerrado" vem em segundo (26,20%, 29,65% e 32,58%), em categorias (aberto e fechado) que o texto combina com do panorâmico ao macro e que, por isso, não são tamanhos de plano clássicos (leitura do assistente); a câmera fica à altura dos olhos em 73 a 81% ([[2026-11-12-navarro-guere-video-vertical-2024]], licença não encontrada, só ficha). No piloto de 20 TikToks da OUP, o plano médio predomina nos dois grupos ([[2026-11-12-grzenkowicz-wildfeuer-tiktok-anotacao-multimodal-2025]]). O ensaio da ABCiber, teórico e sem corpus, diz que a verticalidade favorece enquadramentos fechados, a centralidade do corpo e cortes mais rápidos ([[2026-11-12-machado-sanchotene-estetica-acelerada-tiktok]], licença não encontrada, só ficha); os guias dizem o mesmo, sem medida. Por isso o plano fechado se escolhe cena a cena.
- **O movimento lateral pesa mais em 9:16** ([[2026-11-12-sebire-dicas-de-video-vertical]], 2020): a moldura alta e estreita exagera o movimento da esquerda para a direita, sobretudo projetada grande, e o tremor ou o pan de velocidade média podem enjoar. As respostas convergem em preferir o eixo Z (aproximar, afastar), o tilt e o pedestal ao pan lateral, sem medida.
- **A área segura:** a base tem, da zeely, 14% livres em cima, 35% embaixo e 6% de cada lado no Reels, as mesmas margens para Stories e Reels de anúncio ([[carrossel-instagram]]); nenhuma página da Meta, do TikTok ou do Google abriu. Os números de margem do Shorts atribuídos ao Google ficam não verificados.

## O tempo de plano, por formato

O tempo de plano depende do formato, e cada medida vale na condição em que foi feita. Nos vídeos narrados com um mundo, o ritmo vem da câmera e dos elementos que entram, e não há número de corte como regra.

| Formato | Medida | Condição | Fonte |
|---|---|---|---|
| Anúncio de serviço público | cena entre cortes: mediana de 2,12 s, com intervalo interquartil de 1,5 a 3 s; a análise por cena usa 431 cenas, e o texto não diz se a mediana é sobre elas | 42 anúncios holandeses de 25 a 30 s, vistos em monitor de laboratório por 30 pessoas com rastreio do olhar; cortes pelo Azure Video Indexer; se a "cena" é plano ou grupo de planos, não se abriu a documentação do Azure | [[2026-11-12-wals-cortes-de-cena-e-atencao-2026]] |
| Montagem no TikTok | média de 2,02 s | 8 vídeos de montagem de um piloto de 20 sobre Zelensky (2023), numa agregação que o artigo não diz | [[2026-11-12-grzenkowicz-wildfeuer-tiktok-anotacao-multimodal-2025]] |
| Fala no TikTok | média de 14,73 s | 10 vídeos de pronunciamento do mesmo piloto, que os autores dizem fugir do TikTok típico; mesma agregação não dita | idem |
| Shorts virais | mediana das medianas por vídeo: 4,7 s; 2,8 s ou menos no quarto mais rápido; primeiro corte em 1,9 s | 54 Shorts escolhidos pelo desempenho, medidos por quadros; zoom lento e movimento de câmera não contam como corte; texto de quem vende vídeo feito por IA | [[2026-11-12-viibeo-ritmo-de-corte-em-shorts-virais]] |
| Vídeo de IA com uma imagem por frase de narração | mediana de 12 s (11 a 14 s na metade do meio) | as cenas da própria Viibeo antes do estudo | idem |
| Vídeo de produto em comércio por vídeo curto | classes: abaixo de 0,5 s em 25,69% dos vídeos (12,84% dos planos de cada um, em média); de 0,5 a 5 s; acima de 5 s; sem duração média | 11.045 vídeos de uma plataforma chinesa, de julho e agosto de 2022, pelas características da própria plataforma | [[2026-11-12-zhao-liu-design-de-video-e-cliques-2026]] |
| Filme de lançamento | média de 1,8 a 3 s; a demonstração segura 7 a 10 s | medido quadro a quadro pelo próprio fornecedor (HyperFrames) | [[2026-11-11-hyperframes-catalogo-camera-3d-e-traco-a-mao]] |

- **A conta do piloto não fecha:** no artigo da OUP, as médias não saem das contagens (no grupo popular, 5,1 planos de 9,15, valor que o texto dá sem unidade, passam da duração média do vídeo, 28,67 s), então a agregação não é a média simples dos planos, e o artigo não diz como mediu nem como agregou; vale para os quatro números do piloto.
- **O "corte a cada 2 a 4 s" e o "plano de 1,5 a 2,5 s"** das respostas e dos guias não têm medida própria por trás; [[roteiro-em-formato-curto-o-que-e-medido]] aponta para esta tabela.
- **Leitura do assistente:** as cenas de 12 s da Viibeo, uma imagem por frase de narração, são o formato mais perto de um vídeo narrado que ensina; o número que vale para elas é o tempo de leitura da frase ([[tempo-de-leitura-em-video]]), não um ritmo de corte.

## Da câmera ao código

| Conceito | Three.js | Blender | Cinemachine 3.1 | Unreal 5.9 |
|---|---|---|---|---|
| Dolly e truck (a câmera anda num trilho) | a posição numa curva | Follow Path numa curva, por quadro ou por um fator de 0 a 1 | Spline Dolly, a posição em nó, distância ou de 0 a 1 | Camera Rig Rail, posição no trilho de 0 a 1 |
| Pan e tilt (o alvo anda, a câmera não) | `camera.lookAt(alvo)` com o alvo noutra curva | Track To (o "Look At"); Damped Track quando a câmera passa quase por cima do alvo | Look At | — |
| Pedestal e grua | a posição na vertical | idem | idem | Camera Rig Crane (pitch, yaw e braço em cm); o trilho se prende à grua |
| Zoom (a lente muda) | `fov`, `zoom` ou `setFocalLength` | distância focal ou campo de visão | lente | lente |
| Foco | pós-processamento | Focus Object e F-Stop | — | — |

- **Three.js** ([[2026-11-12-threejs-docs-perspectivecamera]], MIT): `fov` é o campo de visão vertical em graus, padrão 50; `filmGauge` é o tamanho do filme no eixo maior, padrão 35 mm; `setFocalLength` acerta o FOV pela distância focal em relação ao filme; `getViewSize(distância)` dá a largura e a altura visíveis a uma distância. No código do three r185 ([[2026-11-13-threejs-r185-curve-e-perspectivecamera]], `three@0.185.1`, MIT), a altura do filme é `filmGauge / Math.max(aspect, 1)`, que a página não diz (a descrição do `getFilmHeight` é cópia da do `getFilmWidth`), e o `getPointAt(u)` da curva respeita o comprimento dela, ao contrário do `getPoint(t)`: o `getUtoTmapping` troca o `u` pelo `t` que dá pontos equidistantes. As páginas da documentação não falam de amostrar por comprimento de arco, e o `getPointAt` não está na da `CatmullRomCurve3` ([[2026-11-12-threejs-docs-camera-curva-animacao-e-etiquetas]]). Leitura do assistente: em 9:16 o eixo maior é a altura, então os 35 mm valem para a altura, e o "sensor width" das respostas não vale para o vertical.
- **Blender** ([[2026-11-12-blender-manual-camera-follow-path-e-track-to]], CC BY-SA): o Follow Path serve a "câmeras em trilhos" e combina com um constraint de mirar; o Sensor Fit em Auto mede o sensor pelo maior lado da resolução (leitura do assistente: em 9:16, a altura, como no three.js); o Focus Object desliga a distância de foco; o F-Stop menor dá foco mais raso. A ordem do Track To e do Follow Path na pilha, que um fórum dá, o manual não trata: a conferir num teste.
- **Cinemachine** ([[2026-11-12-cinemachine-spline-dolly]]): o Automatic Dolly anda a velocidade fixa ou vai ao ponto mais perto do alvo, e fica instável num trilho em arco em volta dele; o amortecimento por eixo deixa a câmera mais pesada e lenta. **Unreal** ([[2026-11-12-unreal-docs-camera-rig-rail-e-crane]]): trilho e grua se animam no Sequencer. **GSAP** ([[2026-11-12-gsap-motionpathplugin]]): o caminho em SVG ou em pontos, com `align`, `autoRotate`, `start`, `end` e `curviness`. **three-story-controls** ([[2026-11-12-nytimes-three-story-controls]], Apache 2.0, do New York Times): um `CameraRig` que dá à câmera ações com nome (pan, tilt, dolly) sem lidar com a transformação.
- **Proposta para o código das estações (leitura do assistente):** a posição e o alvo em duas `CatmullRomCurve3`, com o progresso tirado do comprimento de arco **por trecho, entre duas estações** (um `u` local por trecho, de `getLengths` ou do `getUtoTmapping` dentro do trecho) e o `power2.inOut` aplicado sobre esse `u`, para a posição e o alvo chegarem juntos a cada parada (o `getPoint(t)` faz a velocidade depender do espaçamento dos pontos, e o `getPointAt` nas curvas inteiras põe cada estação num `u` diferente em cada uma); o dolly pela posição, não pelo `fov`; a lente por `setFocalLength`; o `getViewSize(d)` para saber quanto do mundo cabe a cada distância. No Blender, Follow Path com o fator de 0 a 1 animado, Track To, Sensor Fit em Auto, Focus Object num Empty e render em sequência de imagens ([[2026-11-12-blender-manual-render-pela-linha-de-comando-e-gltf]]). Como regra, a câmera do mundo só faz o que um aparelho físico faria (trilho, grua, steadicam), como na Pixar.

## Um conjunto de movimentos de partida (para um vídeo narrado com mundo de estações)

| Situação | Movimento | Parâmetro de partida | De onde vem |
|---|---|---|---|
| Entra | voo entre paradas | de 0,3 a 1,5 s, com borrão de movimento (no `motion.md`, 6 a 12 px em texto e 15 a 20 px em tela cheia, ou o `data-motion-blur`); `power2.inOut` | `motion.md` (0,3 a 0,6 s rápido), os Reels de [[mundo-3d-com-camera-por-codigo]] (0,5 a 1,5 s), RED (acima de uma largura por segundo é chicote, que pede borrão; a conta da largura é do assistente e depende do espaçamento das estações) |
| Entra | parada com deriva lenta | o tempo da régua de leitura, que manda, mais a releitura antes de qualquer movimento grande; sem texto, de 0,2 a 2 s | [[mundo-3d-com-camera-por-codigo]], [[tempo-de-leitura-em-video]], `pan-stations` |
| Entra | aproximação de ênfase, em duas palavras do roteiro, depois que a frase assenta | dolly in (a câmera anda, não o FOV), o equivalente em 3D à escala de 1,08 a 1,18 do `push-in` (conversão do assistente) | Schrader (o lógico), `push-in`, [[principios-de-motion-design]] (critério 2) |
| Entra | deslocamento lateral lento num cenário de fundo detalhado | no máximo uma largura de tela a cada 7 s; sem borrão, o traço fino estroba antes do que a regra prevê (leitura do assistente), então vale medir com e sem `data-motion-blur`, a 30 fps | RED; Sébire para o 9:16 |
| Entra | recuo ao plano geral no fecho | recuo único que desacelera até o mundo inteiro | os Reels de referência; `pull-back-reveal` |
| Entra | câmera parada contra o objeto que se move | câmera fixa; o movimento é do objeto | Comparato (movimento poupado) |
| Variante a comparar | órbita lenta, no lugar da deriva | 3 a 5° por segundo | `motion.md` |
| Variante a comparar | troca de foco | só entre duas profundidades separadas | `rack-focus`, Blender (Focus Object, F-Stop) |
| Fora | dolly zoom e corte seco | — | chamam atenção para a câmera num vídeo que ensina |

**Tensão que fica para o teste:** a deriva depois de chegar fica perto do "slow push late in a scene" que o `motion.md` lista entre os padrões que soam gerados; os guias de vertical recomendam o empurrão lento. A conciliação pelo alvo (empurrão sobre o mundo em camadas, não sobre um título parado) é leitura do assistente ([[principios-de-motion-design]], "Câmera virtual"); a órbita como variante é o jeito de comparar.

## Proposta: campos de câmera por cena no roteiro

Proposta do assistente para a `piece-script`. Cada cena do roteiro diria, além da fala e da tela:

- **O plano**, num vocabulário fixo: geral (o mundo inteiro), conjunto (a estação e a vizinha), médio (a estação), fechado (a parte que a fala nomeia), detalhe (o objeto que vai importar); a indicação de plano é indicação de importância (Comparato). Ponto de partida: o médio na parada.
- **O movimento**, de uma lista fechada (fixo, dolly in, dolly out, truck, pan, tilt, pedestal, grua, arco, dolly zoom, troca de foco, corte), definido como na LMU e na LibreTexts, com o travelling do Comparato traduzido para um deles e o parâmetro de cada um no motor (a tabela acima).
- **A motivação**, numa linha: a palavra da fala que leva a câmera (o lógico de Schrader), com o ponto de partida e o de chegada (LibreTexts).
- **O tempo de parada**, pela régua de leitura, com o movimento começando depois que a frase assenta.
- **A direção de tela**, uma por vídeo (o progresso anda da esquerda para a direita, por exemplo), pela regra do eixo e pelos três modos de cruzá-lo.
- **O orçamento de movimento**, como padrão que um momento de propósito derruba: no máximo um movimento expressivo por vídeo ([[principios-de-motion-design]], critério 7), nenhum empurrão lento sobre título no fim da cena (`motion.md`), e o movimento poupado (Comparato).

## As regras de partida

1. **O tempo de plano se registra por formato,** com a condição de cada medida, e não há número de corte como regra nos vídeos narrados com mundo, em que o ritmo vem da câmera.
2. **O plano fechado se escolhe cena a cena,** e o plano médio da parada é o ponto de partida.
3. **O critério de ritmo da rubrica de qualidade, na variante de Reels, conta como ritmo toda troca de imagem** (corte, voo de câmera, aproximação, elemento que entra), não só o corte, e vale também pela velocidade da câmera e pelo tempo de parada (`marketing/social-media/rubrica-de-qualidade.md`).
4. **Os movimentos de partida** estão na tabela acima: seis entram, a órbita lenta e a troca de foco ficam como variantes, o dolly zoom e o corte seco ficam fora.

## Contradições e não verificado

- **Empurrão lento:** recomendado para o vertical pelos guias, contra o `motion.md`, que o põe entre os padrões que soam gerados como padrão que um momento de propósito derruba (acima).
- **7 s por largura de tela:** a RED dá 7 s para cena estática, 24 fps e 180°; fóruns atribuem 7 ou 8 s à ASC sem documento; o Gemini fala em 3 a 5° por segundo, que mistura a régua do pan com a órbita de fundo do `motion.md`.
- **Render do Blender:** o Gemini grava direto em MP4, contra o manual, que manda sequência de imagens.
- As durações de movimento sem fonte (reenquadramento, push curto, revelação, pausas antes e depois, a fórmula do multiplano, as margens de plataforma) ficam não verificadas.

## Fontes

- **Raw:** as fichas acima. Com o integral (licença que permite cópia): [[2026-11-12-wikipedia-regra-dos-30-graus-e-dolly-zoom]] e [[2026-11-12-blender-manual-camera-follow-path-e-track-to]] (CC BY-SA 4.0), [[2026-11-12-threejs-docs-perspectivecamera]] (MIT), [[2026-11-13-threejs-r185-curve-e-perspectivecamera]] (MIT, os trechos do código usados), [[2026-11-12-nytimes-three-story-controls]] (Apache 2.0), [[2026-11-12-grzenkowicz-wildfeuer-tiktok-anotacao-multimodal-2025]], [[2026-11-12-wals-cortes-de-cena-e-atencao-2026]] e [[2026-11-12-zhao-liu-design-de-video-e-cliques-2026]] (CC BY). Só ficha, pela licença NC: LMU e LibreTexts, com o integral nas URLs das fichas (acima, em "A gramática clássica"); pela licença não encontrada: Navarro-Güere e a ABCiber; de obra protegida: as demais.
- **Citação:** Doc Comparato, *Da criação ao roteiro* (2009); a prévia oficial de *Timing for Animation* na O'Reilly (acima).

## Ver também

[[mundo-3d-com-camera-por-codigo]] (o mundo de estações), [[machinima-e-motores-de-jogo]] (os motores, que trazem o vocabulário de trilho e grua), [[ambiente-da-cena-em-video-por-codigo]] (o 2,5D e o catálogo de câmera), [[principios-de-motion-design]] (o movimento), [[reels-de-referencia-feitos-em-codigo]] (o ritmo pela entrada de elemento), [[tempo-de-leitura-em-video]] (a régua de leitura), [[roteiro-em-formato-curto-o-que-e-medido]], `marketing/social-media/rubrica-de-qualidade.md` (o critério de ritmo).
