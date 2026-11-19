---
titulo: "Moebius-style post-processing and other stylized shaders"
tipo: artigo
autor: "Maxime Heckel"   # campo author do JSON-LD da página e assinatura ("– Maxime")
url: "https://blog.maximeheckel.com/posts/moebius-style-post-processing"
publicado_em: 2024-03-26   # data na página e article:published_time; "Last Updated Aug 05, 2024" na página (article:modified_time 2024-08-05)
capturado_em: 2026-11-11
licenca: "protegido (rodapé: '© 2026 Maxime Heckel'); sem licença de conteúdo declarada no texto lido; ficha em palavras próprias e em estrutura própria, sem o integral"
areas: [generative-media]
tags: [threejs, react-three-fiber, post-processing, sobel, edge-detection, npr-rendering, hatching, depth-buffer, normal-buffer, glsl]
---

# Maxime Heckel: o estilo Moebius como passe de pós-processamento

Ficha de estudo em palavras próprias, organizada por pergunta (que traço do estilo vira que técnica, o que roda em cada quadro, que número controla o quê, onde a técnica falha e como o autor contornou, onde está o código), não pela ordem do artigo. Não há integral: o artigo é protegido.

**Proveniência.** Artigo de Maxime Heckel no blog dele, https://blog.maximeheckel.com/posts/moebius-style-post-processing, baixado com curl (HTML) em 2026-11-11, com o texto extraído do HTML; Wayback: http://web.archive.org/web/20261027225540/https://blog.maximeheckel.com/posts/moebius-style-post-processing/. Título conferido no HTML (`og:title` e cabeçalho): "Moebius-style post-processing and other stylized shaders". Publicado em 2024-03-26 e atualizado em 2024-08-05, pela página e pelas metas `article:published_time` e `article:modified_time` (o `dateModified` do JSON-LD repete 2024-03-26). Lido o texto inteiro do artigo, com os trechos de código que ele traz; as demos interativas embutidas na página e a cena publicada não foram abertas.

**Conferência lado a lado** (2026-11-11): unidade é a frase fora de tabela ou a célula preenchida de tabela, e uma unidade segue a fonte quando traduz uma frase dela, ou duas vizinhas, na ordem delas. Resultado: 43 de 126 unidades da ficha seguem uma frase da fonte. Quase todas são células que carregam uma afirmação de uma frase dela (um número com o porquê, um sintoma, um contorno) e as citações. A ordem é da ficha, não do artigo: uma tabela junta os quatro traços do estilo com o lugar de cada um no pipeline; a receita segue o que o código roda num quadro; os números estão juntos por função; as falhas e a cena final estão em tabelas de problema e de peça. A medida acima não contou como "segue" a unidade que funde três ou mais frases seguidas da fonte, na ordem dela, ponto cego apontado na revisão do Passo 7 (11/11/2026); o número pode estar baixo, e esta ficha não foi medida de novo.

## Que traço do estilo vira que técnica

O ponto de partida é a decomposição do estilo de Jean Giraud (Moebius) feita em vídeo por @UselessGameDev, que o reconstruiu no Unity; Heckel a refaz no WebGL como um passe único por cima de qualquer cena React Three Fiber, em vez de um material por malha, mantendo luz e sombra físicas por baixo. A motivação dele é sair do PBR, que as ferramentas favorecem, para o render não fotorrealista (NPR), que ele vê voltar nos jogos (cita Zelda BOTW, Hi-Fi Rush, Persona e os independentes Sable e Synergy).

| Traço do Moebius | Técnica | Onde roda |
|---|---|---|
| contorno constante em tudo | Sobel sobre a profundidade (a silhueta do conjunto) e sobre as normais (as quinas de dentro) | no passe |
| contorno que parece feito à mão | deslocamento ondulado e irregular somado a cada leitura do Sobel | no passe |
| sombra hachurada, mais densa quanto mais escura | listras por `mod` em faixas de luminância | no passe |
| reflexo especular branco chapado, com contorno | Blinn-Phong calculado no material de normais, que pinta o brilho de branco | antes do passe, no desenho das normais |

O último é o único que não cabe no passe, e a razão é a regra do artigo: para o Sobel contornar o brilho, "unlike our shadow, we'll have to render those specular upstream from the post-processing shader pass".

## Como o passe entra no React Three Fiber

- **Sem passe próprio na biblioteca de efeitos:** o `@react-three/postprocessing` não aceita passes próprios, então o passe é uma classe que estende `Pass` (do pacote `postprocessing`), registrada no R3F com `extend()` para virar componente JSX e posta dentro do `<Effects>` do `@react-three/drei`, que simplifica a montagem do `EffectComposer`. O desenho usa o `FullScreenQuad` do `three-stdlib` com um `ShaderMaterial`; o teste de montagem soma 0,2 ao vermelho da cena.
- **Nota de atualização do autor:** quando escreveu, ele não sabia que um efeito próprio (custom post-processing effect) também resolveria, e remete ao artigo dele sobre dithering para esse caminho.
- **Os dados extras:** dois alvos criados com `useFBO`, um com `DepthTexture` e `depthBuffer: true`, outro para as normais; são desenhados no `useFrame` e entram no passe pelos `args`, junto com a câmera.
- **As normais de uma vez:** em vez de pôr um material de normais em cada malha, que ele chama de força bruta, troca-se o material da cena inteira com `scene.overrideMaterial`, usando um material de normais próprio (`CustomNormalMaterial`) porque ele vai ganhar o especular.

## O que roda em cada quadro

1. No `useFrame`, a cena é desenhada no alvo de profundidade.
2. Guarda-se o `overrideMaterial`, marca-se `scene.matrixWorldNeedsUpdate = true`, põe-se o `CustomNormalMaterial` e desenha-se a cena no alvo de normais; depois o material volta e o alvo vira `null`.
3. O `CustomNormalMaterial` sai com a cor da normal, troca por branco onde o especular de Blinn-Phong passa do limiar e guarda a luz difusa no canal alfa.
4. O passe lê a cena (`tDiffuse`), a profundidade (`tDepth`) e as normais (`tNormal`). A profundidade se lê com o `#include <packing>`, passando por `perspectiveDepthToViewZ` e `viewZToOrthographicDepth` (a receita de um exemplo de @mattdesl na documentação do Three.js); o resultado é um cinza em que o perto é escuro e o longe, claro, e o fundo sai branco.
5. Calcula-se o deslocamento do pixel: um par de ondas, seno em y e cosseno em x, cada uma multiplicada por um hash da posição na tela, vezes a amplitude e dividido pela resolução.
6. O Sobel lê a vizinhança 3×3 com passo de `outlineThickness` texels, já deslocada, uma vez na profundidade e outra na luminância das normais; cada gradiente é a raiz da soma dos quadrados do horizontal e do vertical. O contorno é a profundidade com peso 25 mais as normais, e entra por `mix(pixelColor, outlineColor, outline)`.
7. A luminância que decide a sombra é a da cor da cena somada à luz difusa vezes 0,65, e o padrão só se aplica onde a profundidade não passa de 0,99.
8. O brilho especular, que já chegou branco no buffer de normais, contrasta com as cores de normal à volta e ganha contorno no mesmo Sobel.

## Que número controla o quê

| Parâmetro | Valor no artigo | O que faz |
|---|---|---|
| kernels | `Sx = [[-1,0,1],[-2,0,2],[-1,0,1]]`, `Sy = [[-1,-2,-1],[0,0,0],[1,2,1]]` | cada um só vê borda numa direção; a combinação dos dois acha o resto, e zero nos dois é ausência de borda |
| `outlineThickness` | 3,0 | distância, em texels, entre as amostras do kernel |
| cor do contorno | preto, `vec4(0, 0, 0, 1)` | também é a cor das listras |
| pesos de luminância | `(0.2125, 0.7154, 0.0721)` | põem a normal e a cor em cinza |
| peso da profundidade | 25 | compensa quando o gradiente das normais não basta |
| frequência da onda | 0,08 | baixa de propósito, para a linha sair em ondas alongadas |
| amplitude da onda | o texto não dá o valor | ajustável na demo, junto com a frequência |
| hash | `fract` sobre `p.xyx * .1031`, de um Shadertoy de markjarzynski | dá a irregularidade do contorno |
| sombra em tons | luminância ≤ 0,35 vira preto; ≤ 0,45, ≤ 0,6 e ≤ 0,75 multiplicam a cor por 0,25, 0,5 e 0,7 | as condições são independentes, então os escurecimentos se acumulam |
| máscara de fundo | profundidade ≤ 0,99 | impede que um fundo escuro ganhe sombra |
| hachura | período de 8 pixels (`modVal`); diagonal até 0,80, vertical até 0,55, horizontal até 0,35 | quanto mais escuro, mais camadas de listra; na demo interativa, as faixas são 0,65, 0,55 e 0,45 |
| largura da listra | condição `<= 1.0` no resto do `mod` | marca os pixels 0 e 1 de cada 8; o valor é o mesmo da espessura do contorno, e maior dá listra mais grossa |
| especular | brilho (`shininess`) 600, difusa 0,5, limiar 0,25 | acima do limiar, o pixel do buffer de normais vira branco |
| peso da difusa na luminância | 0,65, que o autor chama de número arbitrário | evita hachura demais em área de cor escura mas iluminada |

As listras da hachura usam o mesmo deslocamento e a mesma espessura do contorno, para parecerem da mesma mão. Além dos tons e da hachura, o artigo implementa o padrão **raster**, uma grade de círculos que crescem conforme a luminância cai, tirado de um Shadertoy de cdyk; os três padrões se ligam e desligam na demo.

## Onde a técnica falha e o que o autor fez

| Problema | Como aparece | O que o autor fez | O que ficou de lado |
|---|---|---|---|
| a luminância decide o que é área escura | é um critério frágil, que ele aceita como "good enough" | somar a luz difusa (×0,65) à luminância, para cor escura bem iluminada não ganhar listra | — |
| o padrão de sombra vale para a tela toda | um fundo de cor escura sairia hachurado | só aplicar onde a profundidade não passa de 0,99 | — |
| o gradiente das normais às vezes não basta | com a câmera olhando para baixo, o topo do cubo se confunde com o chão e o contorno some | peso 25 na profundidade | — |
| o chão da cena final é deslocado no vertex shader | luz e sombra seguem as dunas, mas o buffer de normais não: "our scene's Normal data (used to draw outlines) does not contain this displacement information"; para o Sobel, o chão é plano | percorrer a cena com `traverse`, guardar o material de cada malha, dar à malha `ground` um `GroundNormalMaterial` que repete o deslocamento (com `uTime` e a posição da luz) e às demais o `CustomNormalMaterial`, desenhar e devolver os materiais na ordem guardada; ele não se orgulha, mas funciona | as sugestões de @Cody_J_Bennett, tirar as normais da profundidade ou usar um gbuffer, que lhe pareceram pesadas demais naquele ponto |

O autor chama o problema do chão de armadilha da implementação e conta que só o notou ao montar a cena final.

## Como a cena final foi montada

| Peça | Como | Para quê |
|---|---|---|
| tema | nave cruzando dunas, com planetas ao longe; mostrada no Twitter no começo de março de 2024 | homenagem à ficção científica e aos desertos de Giraud |
| nave | modelo do Sketchfab, de Sousinho, comprimido com `gltf-transform` de 30 MB para cerca de 1,6 MB; uma variante do passe a desenha como planta técnica (blueprint) | — |
| movimento | só a flutuação da nave é real, 80% do movimento é falso, nas contas dele; o chão tem ruído de Perlin correndo no sentido contrário | parecer veloz e rodar sem fim, sem um plano gigante de deserto |
| chão | `MeshStandardMaterial` com código injetado pelo `onBeforeCompile` depois de `#include <clipping_planes_vertex>`: deslocamento por Perlin e normais recalculadas como no artigo dele sobre cáusticas | manter o modelo de luz e sombra, e por isso a sombra da nave acompanha as dunas |

## Onde estão o código, as demos e as referências

- **Cena publicada:** https://r3f.maximeheckel.com/moebius (não aberta). As demos de cada etapa estão embutidas na página e não foram lidas; o código registrado aqui é o dos trechos do texto.
- **Fontes que o próprio artigo lista:** "How Persona Combines 2D and 3D Art" (@Acerola_t), "Unlocking The Power Of Unity's Scriptable Render Pipeline" (Game Dev Guide), "Moebius-style 3D Rendering" (@UselessGameDev), "Sketchy Pencil Effect with Three.js Post-Processing" (@maya_ndljk, no Codrops) e txstc55, que explorou o mesmo efeito no ano anterior.
- **Sobre o artigo do Codrops, nas palavras dele:** propõe tirar o deslocamento do contorno de uma textura em vez de um hash e traz uma técnica de sombra de lápis; ele recomenda a leitura.
- **Outras referências do texto:** o exemplo de textura de profundidade do Three.js (https://threejs.org/examples/?q=depth#webgl_depth_texture); um vídeo do Computerphile sobre filtros de convolução (que servem também a desfoque, nitidez e redução de ruído); o hash de markjarzynski (https://www.shadertoy.com/view/XlGcRh); o raster de cdyk (https://www.shadertoy.com/view/ttXSzl); e uma resposta do Stack Overflow sobre Blinn-Phong, ao lado de artigos anteriores do autor (render targets, cáusticas, refração e dispersão, dithering).

## Lacuna

O artigo não dá as versões de Three.js, React Three Fiber e `postprocessing`, nem o valor da amplitude da onda, nem medida de desempenho do passe ou dos dois desenhos extras por quadro.
