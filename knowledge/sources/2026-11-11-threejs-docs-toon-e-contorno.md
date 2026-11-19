---
titulo: "Three.js docs: MeshToonMaterial, OutlineEffect, OutlineNode e ToonOutlinePassNode"
tipo: artigo
autor: "Colaboradores do three.js (mrdoob/three.js)"
url: "https://threejs.org/docs/pages/MeshToonMaterial.html"
publicado_em: null   # as páginas não trazem data nem número de versão
capturado_em: 2026-11-11
licenca: "MIT (arquivo LICENSE do repositório mrdoob/three.js); as páginas da documentação são geradas dos comentários do código-fonte, que cada página aponta na seção 'Source'. Que a licença do código cubra o texto da página é leitura do assistente, registrada na rodada (licencas.json)"
areas: [generative-media]
tags: [threejs, toon-shading, outline, post-processing, webgl, webgpu, tsl, npr-rendering]
---

# Three.js: o material toon e os três contornos

Ficha de estudo, organizada pelo que cada peça faz e onde roda; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Quatro páginas da documentação do three.js, baixadas com curl em 2026-11-11, com o texto extraído do HTML: https://threejs.org/docs/pages/MeshToonMaterial.html, https://threejs.org/docs/pages/OutlineEffect.html, https://threejs.org/docs/pages/OutlineNode.html e https://threejs.org/docs/pages/ToonOutlinePassNode.html. Lidas inteiras. As páginas não dizem a versão do three.js a que se referem. Na mesma rodada, a API do GitHub confirmou que os exemplos `webgl_postprocessing_sobel`, `webgl_materials_toon` e `webgl_postprocessing_outline` existem no repositório (o código deles não foi lido).

## As quatro peças

| Peça | O que é, pela página | Onde roda | Como entra |
|---|---|---|---|
| `MeshToonMaterial` | "A material implementing toon shading" | núcleo (`src/materials/MeshToonMaterial.js`) | material comum da malha |
| `OutlineEffect` | "An outline effect for toon shaders" | só com `WebGLRenderer`; para o `WebGPURenderer`, a página manda usar o `ToonOutlinePassNode` | addon (`three/addons/effects/OutlineEffect.js`): chama-se `effect.render(scene, camera)` no lugar do `renderer.render` |
| `ToonOutlinePassNode` | passada de render que contorna em estilo toon; só recebem o contorno objetos com `MeshToonMaterial` ou `MeshToonNodeMaterial` | pipeline de nós (`RenderPipeline`, `toonOutlinePass(scene, camera)`) | `src/nodes/display/ToonOutlinePassNode.js` |
| `OutlineNode` | nó de pós-processamento que desenha o contorno em volta dos objetos selecionados, com "great flexibility" para compor o visual final | pipeline de nós (TSL), renderiza uma vez por quadro (`updateBeforeType` = `'frame'`) | addon (`three/addons/tsl/display/OutlineNode.js`, função `outline`) |

## Os parâmetros que mudam o traço

- **`MeshToonMaterial`:** o `gradientMap` é o mapa de degradê do sombreamento toon, e exige `minFilter` e `magFilter` em `NearestFilter`; é dado não colorido (`NoColorSpace`). O resto são os mapas comuns dos materiais (cor, alfa, oclusão, relevo, normal, deslocamento, emissivo, luz pré-calculada), `fog` ligado por padrão e `wireframe`, cuja ponta, junta e espessura só valem no `SVGRenderer`. O deslocamento é o único mapa que mexe de fato na geometria (projeta sombra e bloqueia outros objetos); o relevo e o normal só mudam a luz.
- **`OutlineEffect`:** quatro opções, com os padrões: espessura `defaultThickness` 0,003, cor `defaultColor` `[0,0,0]`, opacidade `defaultAlpha` 1 e `defaultKeepAlive` falso (guardar ou não os materiais internos em cache). Há `setSize` e um `renderOutline(scene, camera)` para desenhar só o contorno, que a página indica para VR, chamado de dentro do `onAfterRender` da cena.
- **`ToonOutlinePassNode`:** cor, espessura e opacidade do contorno entram como nós (`colorNode`, `thicknessNode`, `alphaNode`); o nome padrão da passada é "Outline Pass".
- **`OutlineNode`:** recebe a cena, a câmera e os objetos selecionados; `edgeThickness` (padrão `float(1)`), `edgeGlow` (padrão `float(0)`, para brilho ou pulsação animados) e `downSampleRatio` (padrão 2, a redução de resolução). Devolve duas máscaras, a borda visível e a escondida (`visibleEdge`, `hiddenEdge`), que o exemplo da página multiplica cada uma por uma cor, soma, multiplica por uma intensidade (`edgeStrength` 3,0) e soma à passada da cena.
