---
titulo: "Three.js docs: AnimationMixer, CatmullRomCurve3, OrthographicCamera e CSS2DRenderer"
tipo: artigo
autor: "Colaboradores do three.js (mrdoob/three.js)"
url: "https://threejs.org/docs/pages/AnimationMixer.html"
publicado_em: null   # as páginas não trazem data nem número de versão
capturado_em: 2026-11-12
licenca: "MIT (arquivo LICENSE do repositório mrdoob/three.js); as páginas da documentação são geradas dos comentários do código-fonte, que cada página aponta na seção 'Source'. Que a licença do código cubra o texto da página é leitura do assistente, registrada na rodada (licencas.json), como na ficha 2026-11-11-threejs-docs-toon-e-contorno"
areas: [generative-media]
tags: [threejs, animation-mixer, camera-path, catmull-rom, orthographic-camera, isometric, css2d-renderer, labels, deterministic-rendering]
---

# Three.js: tocar a animação num tempo exato, a curva da câmera, a câmera ortográfica e a etiqueta em HTML

Ficha, organizada pelo que cada peça faz numa cena avançada pelo tempo; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Quatro páginas da documentação do three.js, baixadas com curl em 2026-11-12, com o texto extraído do HTML: https://threejs.org/docs/pages/AnimationMixer.html (sha256 do HTML (hash omitido)), https://threejs.org/docs/pages/CatmullRomCurve3.html ((hash omitido)), https://threejs.org/docs/pages/OrthographicCamera.html ((hash omitido)) e https://threejs.org/docs/pages/CSS2DRenderer.html ((hash omitido)). Lidas inteiras. As páginas não dizem a versão do three.js. Os HTML estão em a pasta da rodada.

## As quatro peças

| Peça | O que é, pela página | O que importa num quadro calculado pelo tempo |
|---|---|---|
| `AnimationMixer` | tocador das animações de um objeto da cena; um por objeto quando vários se animam em separado | `.setTime(time)` leva o tocador a um tempo exato, em segundos, e atualiza a animação; o valor é escalado pelo `timeScale`. O `.update(deltaTime)` avança pelo intervalo desde o último quadro, que a página diz vir em geral do `Clock` ou do `Timer` no laço de render |
| `CatmullRomCurve3` | curva suave em 3D por uma lista de pontos (spline Catmull-Rom) | `.getPoint(t)`, com `t` de 0 a 1, devolve a posição na curva; a curva pode ser fechada, com tipo `centripetal` (padrão), `chordal` ou `catmullrom` e tensão 0,5 por padrão |
| `OrthographicCamera` | câmera de projeção ortográfica: o tamanho do objeto na imagem não muda com a distância | definida pelos seis planos (esquerda, direita, topo, base, perto, longe); `zoom` 1 por padrão; depois de mudar qualquer propriedade, chamar `.updateProjectionMatrix()`; ao contrário da perspectiva, aceita 0 no plano perto |
| `CSS2DRenderer` | versão simplificada do `CSS3DRenderer` (só translação e rotação 2D) para juntar etiquetas em HTML a objetos 3D | os elementos HTML entram na cena como `CSS2DObject`; com `sortObjects` ligado (padrão), o `z-index` sai primeiro do `renderOrder` e depois da distância à câmera; só funciona com zoom do navegador e da tela em 100%; é addon, importado à parte |

## Outros pontos das páginas

- **`AnimationMixer`:** `clipAction(clip)` devolve a ação do clipe (sempre a mesma para o mesmo clipe e raiz); `timeScale` 0 e de volta a 1 pausa e retoma todas as ações; `stopAllAction()` desativa todas; `uncacheAction`, `uncacheClip` e `uncacheRoot` liberam memória, depois de parar as ações.
- **`CatmullRomCurve3`:** o exemplo da página monta um laço fechado de cinco pontos e o desenha como linha com `getPoints(50)`; a página só documenta o `getPoint` próprio da classe e diz que ele sobrescreve o de `Curve`.
- **`OrthographicCamera`:** o exemplo cria a câmera com metade da largura e da altura de cada lado; `setViewOffset` serve a montagens de várias janelas ou monitores.
- **`CSS2DRenderer`:** `setSize`, `getSize` e `render(scene, camera)`; o `domElement` é onde ele põe os elementos, e o parâmetro `element` do construtor permite passar um contêiner próprio.

## Citações

- "Sets the global mixer to a specific time and updates the animation accordingly."
- "In this projection mode, an object's size in the rendered image stays constant regardless of its distance from the camera."
- "The renderer is very useful if you want to combine HTML based labels with 3D objects."

## Lacuna

As páginas não falam de vista isométrica (nem de que posição dar à câmera ortográfica para ela), de amostrar a curva por comprimento de arco (o `getPointAt` não está na página da `CatmullRomCurve3`), de apontar a câmera ao longo da curva, nem de como o `CSS2DRenderer` se comporta numa captura quadro a quadro.
