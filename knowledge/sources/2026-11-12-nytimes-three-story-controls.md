---
titulo: "Three Story Controls"
tipo: artigo
autor: "The New York Times, equipe de Research & Development (repositório nytimes/three-story-controls)"   # o README diz que o repositório é mantido por essa equipe; não assina pessoa
url: "https://github.com/nytimes/three-story-controls"   # o README lido; a página https://nytimes.github.io/three-story-controls/, registrada no rótulo e no licencas.json da rodada, é a das demonstrações, segundo o próprio README
publicado_em: null   # o README não traz data; as versões que ele cita são three.js r129 ou mais nova e gsap 3.6.1
capturado_em: 2026-11-12
licenca: "Apache 2.0 (selo 'License-Apache 2.0' no topo do README e o arquivo LICENSE do repositório, lido pela API do GitHub); o integral, com a licença, está na url"
areas: [generative-media]
tags: [threejs, camera-rig, camera-path, camera-movement, scroll-animation, gsap, interactive-narrative, camera-terms]
---

# Three Story Controls: a câmera do three.js com ações de set (pan, tilt, dolly) e esquemas de controle para histórias em 3D

Nota de fato: tabelas do que o README do repositório diz da biblioteca, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Ficha; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório nytimes/three-story-controls, baixado com curl em 2026-11-12, de https://raw.githubusercontent.com/nytimes/three-story-controls/main/README.md (o arquivo em markdown, sem passar pela página do GitHub). sha256 do arquivo baixado (a pasta da rodada) (hash omitido). O README abre com o título "Three Story Controls" e o subtítulo "A three.js camera toolkit for creating interactive 3d stories." Lido inteiro. A documentação da API, os arquivos `docs/*.md` a que cada componente remete, os exemplos e as demonstrações não foram abertos. Fonte curta (umas 1.200 palavras com o código), por isso nota de fato. O texto integral não vem neste repositório e se lê na url do frontmatter.

**Conferência lado a lado:** não se fez na captura, porque a licença permitia guardar o integral; neste repositório ele não vem, e se lê na url do frontmatter.

## Em uma frase

Biblioteca do New York Times para o three.js que envolve a câmera num rig com ações de nome de set (pan, tilt, roll, pedestal, truck, dolly), traz uma ferramenta para gravar posições e exportar o caminho da câmera em JSON e cinco esquemas de controle prontos, entre eles a rolagem da página que corre a câmera por uma animação.

## Instalação

| Ponto | Fato |
|---|---|
| Dependências | three.js r129 ou mais nova; gsap 3.6.1; instaladas à parte |
| Rota 1, módulo ES | `dist/three-story-controls.esm.min.js` com `importmap-shim` (es-module-shims 0.11.1; o exemplo usa three@0.137.0) |
| Rota 2, npm | `npm install -s three gsap three-story-controls` |
| Rota 3, tag de script | `dist/three-story-controls.min.js`, que expõe a global `ThreeStoryControls` |
| Laço de render do exemplo | `controls.update(t)` e `renderer.render(scene, camera)` a cada `requestAnimationFrame` |

## O CameraRig: as ações de câmera

| Ação | Transformação, com o eixo de cima em Y (o padrão) |
|---|---|
| Pan | gira em torno de Y |
| Tilt | gira em torno de X |
| Roll | gira em torno de Z |
| Pedestal | desloca em Y |
| Truck | desloca em X |
| Dolly | desloca em Z |

| Ponto | Fato |
|---|---|
| O que é | o componente central: envolve a câmera do three.js para pedir uma ação sem lidar com a transformação que a câmera já tem |
| Como se pede | `rig.do(CameraAction.Pan, Math.PI / 6)` |
| Trilho | o rig aceita um `AnimationClip` do three.js para andar num caminho definido antes |

## O CameraHelper

| Ponto | Fato |
|---|---|
| O que faz | grava posições de câmera numa cena e monta o caminho da animação, ou pontos de interesse |
| Saída | um arquivo JSON |
| Para quê | alimentar os esquemas de controle |

## Os esquemas de controle

| Esquema | Fato |
|---|---|
| `FreeMovementControls` | primeira pessoa: arrastar gira; WASD, setas e roda do mouse ou trackpad andam |
| `ScrollControls` | a rolagem de um elemento do DOM corre a câmera por um caminho dado por `AnimationClip` |
| `StoryPointControls` | a câmera transita entre pontos escolhidos |
| `PathPointControls` | a câmera vai a quadros escolhidos de um caminho em `AnimationClip` |
| `ThreeDOFControls` | gira a câmera um pouco sem sair do lugar; para usar junto com os outros |
| Demonstrações citadas | movimento livre; rolagem com 3DOF; pontos de história com 3DOF; pontos do caminho; o CameraHelper |

## Os adaptadores de entrada

| Adaptador | Fato |
|---|---|
| Papel geral | alisam e transformam a entrada e emitem eventos com o valor já tratado |
| `PointerAdaptor` | ponteiro, clicar e arrastar, multitoque |
| `KeyboardAdaptor` | teclas escolhidas |
| `ScrollAdaptor` | distância rolada num elemento do DOM |
| `SwipeAdaptor` | gesto de deslizar |
| `WheelAdaptor` | roda do mouse, com limiar de movimento |
| Esquema próprio | adaptadores mais o `CameraRig`, numa classe com `enable`, `disable` e `update(time)` |

## O que a fonte recomenda

A câmera se move por ações com nome de set pedidas ao rig, que cuida da transformação acumulada, e o caminho de uma história se grava antes, com o CameraHelper, para depois ser tocado por um esquema de controle, como a rolagem da página; quem precisa de outro comportamento monta o seu juntando adaptadores de entrada ao rig.

## Citações

- "A three.js camera toolkit for creating interactive 3d stories."
- "makes it easier to specify camera actions such as pan / tilt / dolly etc. without worrying about the existing camera transform."
- "provided as-is for your own use"

## Lacuna

O README não diz como o `ScrollControls` mapeia a rolagem no tempo do clipe (linear ou com easing), não fala de render quadro a quadro nem de exportar vídeo, não dá data nem versão da biblioteca, e não diz se ela segue mantida; as versões citadas (three.js r129 e 0.137.0, gsap 3.6.1) são as do próprio README.
