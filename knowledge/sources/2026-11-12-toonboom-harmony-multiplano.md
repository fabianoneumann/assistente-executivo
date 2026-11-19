---
titulo: "About Multiplane"
tipo: artigo
autor: "Toon Boom Animation"   # página do manual do Harmony 27 Premium, sem assinatura de pessoa
url: "https://docs.toonboom.com/help/harmony-27/premium/staging/about-multiplane.html"
publicado_em: null   # a página não traz data; é do manual do Harmony 27 Premium (código do tópico T-HFND-008-013)
capturado_em: 2026-11-12
licenca: "protegido (rodapé: '© 1994-2026 Toon Boom Animationc Inc. All rights reserved.', com a grafia da página); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [multiplane, parallax, 2-5d-animation, camera-movement, depth, toon-boom-harmony, interested-party]
---

# Toon Boom Harmony: o multiplano como camadas no eixo Z, com a câmera passando entre elas

Nota de fato: tabelas do que a página do manual do Harmony diz sobre o multiplano, organizadas por ferramenta e por cuidado, e não pela ordem da página, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Tópico "About Multiplane" do manual do Harmony 27 Premium, da Toon Boom, https://docs.toonboom.com/help/harmony-27/premium/staging/about-multiplane.html, baixado em HTML em 2026-11-12 e lido no texto extraído do HTML, que bate com a página: o `<title>` é "Harmony 27 Premium Documentation: About Multiplane" e o `<h1>`, "About Multiplane", seguido do código T-HFND-008-013. sha256 registrado na rodada: (hash omitido), que mede o texto do bloco `<main>`/`<article>`, sem tags, script e estilo, e não o arquivo HTML. Sem captura na Wayback. Sem data na página. Cobertura: o tópico inteiro (a definição, o conselho de planejamento, o exemplo de seis camadas, a nota sobre desenhar as camadas inteiras, o movimento no eixo Z, a hierarquia e os dois procedimentos para abrir a barra e a vista de coordenadas); as imagens do exemplo aparecem só pela descrição do texto, e os tópicos vizinhos do manual não foram abertos.

**Quem fala.** A Toon Boom, que vende o Harmony, no manual do próprio programa.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` contra o texto extraído saiu com o código 3 (ficha em português, fonte em inglês): 22 unidades medidas (14 de prosa, 8 de célula com texto); fora da conta, 41 células de fato, 12 de cabeçalho e 6 frases curtas demais para medir; 0 colada de 22 e 0 trecho de 3 ou mais seguidas. Na leitura lado a lado das mesmas 22 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais seguidas na ordem dela; a frase que junta lugares distantes em outra ordem não conta. Resultado: 8 de 22 (as células da montagem em camadas, do princípio do filme com atores, da perda de conta na hierarquia, da vista da câmera aberta durante o ajuste, das duas da nota sobre desenhar a camada inteira, a do planejamento e a do caminho pelo botão Add View, que é um caminho de menu, contada por cautela). A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 2 (o princípio do filme com atores e a perda de conta na hierarquia; as duas da nota sobre desenhar a camada inteira; o planejamento e o caminho do menu, que estão longe um do outro na página), sem trecho de 3 ou mais; a proveniência, a frase de abertura, a recomendação e a lacuna não seguem a fonte.

## Em uma frase

Página do manual do Harmony, da Toon Boom, que define o multiplano como o cenário repartido em camadas espalhadas no eixo Z, com a câmera atravessando o conjunto para dar perspectiva sem 3D, e mostra onde se mexe na profundidade de cada camada e como ler a profundidade herdada dos pais.

## O que é

| Ponto | Fato |
|---|---|
| Outro nome na página | Z-depth |
| Montagem | cenário em várias camadas, cada uma numa profundidade em relação à câmera |
| Efeito buscado | ilusão de perspectiva com a câmera em movimento |
| Princípio, no filme com atores | o perto anda mais na tela que o longe quando a câmera se move |
| Exigência de 3D | nenhuma |
| Exemplo da página | seis camadas, um objeto por distância |
| Vistas do exemplo | de lado; de um canto; pela câmera |

## Profundidade herdada

| Ponto | Fato |
|---|---|
| Z de um pai | soma no Z aparente de todos os filhos |
| Quem afeta um filho | qualquer pai acima dele |
| Problema apontado | perder a conta de quais camadas já saíram do lugar em Z |
| Onde conferir | vista Coord. and Control Points; barra Coordinate |
| Campo 1 | Z da própria camada, sem os pais |
| Campo 2 | Z acumulado: o da camada somado ao de todos os pais |

## Onde mexer na profundidade

| Onde | Como | Efeito |
|---|---|---|
| Vistas Side ou Top | ferramenta Transform | camada mais perto ou mais longe |
| Camera View | Alt + arrastar para cima ou para baixo | camada mais perto ou mais longe |
| Barra Advanced Animation | ferramenta Maintain Size | muda o Z sem mudar o tamanho aparente |
| Sem o Maintain Size | — | perto fica maior; longe fica menor |
| Durante o ajuste nas vistas Side e Top | manter uma Camera View aberta | ver o quadro final enquanto posiciona |

## Antes de montar

| Cuidado | Fato |
|---|---|
| Desenhar | cada camada inteira, mesmo o trecho coberto pela da frente |
| Por quê | panorâmica ou zoom podem revelar o que estava escondido no enquadramento inicial |
| Planejar | imaginar o cenário em 3D, a câmera andando nele e a velocidade de cada objeto conforme a distância da lente |

## Menus para ver o Z

| Para abrir | Caminho 1 | Caminho 2 |
|---|---|---|
| Barra Coordinate | Windows > Toolbars > Coordinate | clique direito numa barra > Coordinate |
| Vista Coord. and Control Points | Windows > Coord. and Control Points | botão Add View, no canto de cima à direita de uma vista > Coord. and Control Points |

## O que a fonte recomenda

Montar o multiplano começa fora do programa, pensando o cenário como espaço com profundidade e cada camada completa, porque a câmera vai descobrir o que hoje está atrás de outra. Na hora de posicionar, o manual pede a vista da câmera sempre aberta e, quando há hierarquia, a leitura do Z acumulado, já que o pai desloca os filhos sem que isso apareça no Z de cada um.

## Citações

- "In 2D animation, multiplanes can be used to achieve a similar effect without having to use 3D."
- "it is important to draw each layer fully."
- "which is the sum of the Z coordinate of the selected layer with the Z coordinate of all its parents."

## Lacuna

A página não dá números: distâncias em Z do exemplo, unidade do eixo, campo de visão ou lente da câmera, nem quanto cada camada anda na tela para um dado movimento. Não fala de como animar a câmera (chaves, curvas, velocidade), de desfoque por profundidade nem de tamanho de arte para aguentar o zoom, e não diz se o tópico vale igual para as edições do Harmony abaixo da Premium.
