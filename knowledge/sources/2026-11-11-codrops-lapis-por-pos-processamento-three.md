---
titulo: "Sketchy Pencil Effect with Three.js Post-Processing"
tipo: artigo
autor: "Maya Nedeljković Batić"   # assinatura do artigo na página
url: "https://tympanus.net/codrops/2022/11/29/sketchy-pencil-effect-with-three-js-post-processing/"
publicado_em: 2022-11-29   # data da assinatura na página ("November 29, 2022") e da URL; o HTML não traz meta de data
capturado_em: 2026-11-11
licenca: "protegido (rodapé: '© Codrops 2026', com link para a página de licença do site, que não foi lida); o código do tutorial fica no repositório mayacoda/pencil-lines, dado como MIT pelo resumo do repositório visto na rodada, código não lido; ficha em palavras próprias e em estrutura própria, sem o integral"
areas: [generative-media]
tags: [threejs, post-processing, sobel, edge-detection, npr-rendering, normal-buffer, noise, hand-drawn, glsl]
---

# Codrops: o traço de lápis feito por pós-processamento no Three.js

Ficha de estudo em palavras próprias, organizada por pergunta (do que o efeito é feito, o que roda em cada quadro, que número controla o quê, o que a autora ressalva, onde está o código), não pela ordem do tutorial. Não há integral: o artigo é protegido.

**Proveniência.** Tutorial de Maya Nedeljković Batić no Codrops, https://tympanus.net/codrops/2022/11/29/sketchy-pencil-effect-with-three-js-post-processing/, baixado com curl (HTML) em 2026-11-11, com o texto extraído do HTML; Wayback: http://web.archive.org/web/20260828132247/https://tympanus.net/codrops/2022/11/29/sketchy-pencil-effect-with-three-js-post-processing/. Lido o texto inteiro do artigo, com todos os trechos de código que ele traz. Não foram abertos a demo, as quatro Codesandbox nem o repositório: do repositório só se viu o resumo, na rodada, e o código dele não foi lido.

**Conferência lado a lado** (2026-11-11): unidade é a frase fora de tabela ou a célula preenchida de tabela, e uma unidade segue a fonte quando traduz uma frase dela, ou duas vizinhas, na ordem delas. Resultado: 29 de 110 unidades da ficha seguem uma frase da fonte. As que seguem são de dois tipos: fatos de API que o artigo diz numa frase só (o que o `EffectComposer` faz, o que são os buffers de leitura e escrita, o que o `renderToScreen` faz) e células que carregam uma afirmação de uma frase dela (o que a cor perde, por que a textura não serrilha a linha), mais a citação. A ordem é da ficha, não do tutorial: a receita segue o que o código roda num quadro, e não a ordem em que o tutorial o constrói; os números estão juntos numa tabela por função; as ressalvas e as sugestões do fim estão reagrupadas pelo que cada buffer enxerga e pelo que cada ruído produz. A medida acima não contou como "segue" a unidade que funde três ou mais frases seguidas da fonte, na ordem dela, ponto cego apontado na revisão do Passo 7 (11/11/2026); o número pode estar baixo, e esta ficha não foi medida de novo.

## Do que o efeito é feito

A cena já renderizada vira desenho: linha cor de vinho sobre papel branco, traço que treme e um grão pontilhado nas superfícies curvas. Nada disso troca o material da cena na imagem final; tudo acontece num passe de pós-processamento escrito pela autora (`PencilLinesPass`), que lê a imagem pronta e devolve outra. São quatro ingredientes: o detector de bordas de Sobel sobre a imagem da cena; o mesmo detector sobre um segundo desenho da cena, feito só com as normais; um ruído gerado no shader, que dá o grão; e uma textura de nuvens, que faz a linha tremer.

## Por que um passe próprio, e como ele entra no Three.js

| Caminho para um efeito próprio | O que é | No tutorial |
|---|---|---|
| `ShaderPass` com um shader escrito | o shader recebe uniforms e attributes | não basta: o efeito precisa de mais dado do que isso (a cena desenhada outra vez com normais) |
| classe que estende `Pass` | métodos `setSize`, `render` e `dispose`; o trabalho fica no `render` | o escolhido |

- **A montagem:** o `EffectComposer` empilha os passes na ordem em que são adicionados, e o `RenderPass` vem primeiro para que a cena chegue aos seguintes; no laço de animação, chama-se `composer.render()` no lugar de `renderer.render(scene, camera)`.
- **Os buffers:** no Three.js, um render target é uma textura onde se desenha, e é por ela que os passes trocam dados; o `render` do passe recebe dois, o de leitura (o que o passe anterior produziu) e o de escrita (o que vai ao próximo). Com `renderToScreen` ligado, o alvo vira `null`, que é o canvas da tela.
- **Para desenhar de fato:** o passe precisa de um `FullScreenQuad` com um `ShaderMaterial`. O teste de montagem usa o `CopyShader` da biblioteca, que só mostra a textura que recebe no uniform `tDiffuse` (o mesmo nome que um `ShaderPass` já passa sozinho); a autora manteve o nome no material próprio.
- **Documentação:** segundo a autora, há pouca sobre passes próprios, e quem quer aprender tem os exemplos que a própria biblioteca traz.

## O que roda em cada quadro

1. O `RenderPass` desenha a cena com os materiais dela; o resultado chega ao passe como buffer de leitura.
2. O passe, que recebeu `scene` e `camera` no construtor, guarda o `scene.overrideMaterial` atual, põe no lugar o `MeshNormalMaterial` único da classe, desenha a cena no `normalBuffer` (um `WebGLRenderTarget` do tamanho do canvas) e devolve o material de antes.
3. O material do passe recebe a textura da cena (`tDiffuse`), a das normais (`uNormals`), a de nuvens (`uTexture`) e o tamanho do canvas (`uResolution`).
4. O vertex shader só repassa a posição e o `uv`; num quad de tela cheia, o `uv` é a posição do fragmento na tela.
5. O fragment shader lê, para cada pixel, a vizinhança 3×3, um texel por vez (o passo é `1 / uResolution`). O valor de cada vizinho é a cor em cinza com peso 0,6 somada às normais em cinza com peso 0,3, e essa parcela das normais vem multiplicada pelo ruído e lida num ponto deslocado pela textura de nuvens.
6. Os dois kernels do Sobel dão o gradiente horizontal e o vertical, e o shader soma os quadrados dos dois, sem tirar a raiz, limitando a 0 a 1. O texto do artigo descreve essa combinação como a média dos dois valores; o código mostrado soma os quadrados.
7. Um `smoothstep(0.01, 0.03)` suaviza o resultado; acima de 0,1, o pixel recebe a cor da linha, e abaixo, branco.
8. O quad desenha no buffer de escrita, ou na tela se o passe for o último.

## Que número controla o quê

| Parâmetro | Valor no artigo | O que faz |
|---|---|---|
| pesos de luminância | `(0.299, 0.587, 0.114)`, tirados do `glsl-luma` | convertem a cor (ou a normal) em cinza antes do Sobel |
| peso da cor | 0,6 | parcela da imagem renderizada no valor de cada vizinho |
| peso das normais | 0,3 | parcela do buffer de normais |
| ruído gerado | `noise(gl_FragCoord.xy)`, levado a −1..1 e multiplicado por 10 | dá força e sinal ao grão |
| textura de nuvens | canal vermelho limitado a 0..50, dividido por 50, menos 0,5/50 | dá o tamanho do deslocamento somado ao `vUv` |
| kernels | `Gx = mat3(-1,-2,-1, 0,0,0, 1,2,1)` e `Gy = mat3(-1,0,1, -2,0,2, -1,0,1)` | em GLSL a matriz se preenche por coluna, como avisa o comentário do código |
| suavização | `smoothstep(0.01, 0.03)` | rampa do valor do Sobel |
| limiar | 0,1 | separa linha de papel |
| cor da linha | `vec4(0.32, 0.12, 0.2, 1.0)` | o resto do pixel sai `vec4(1.0)`, branco |
| `normalBuffer` | `RGBAFormat`, `HalfFloatType`, filtros `NearestFilter`, sem mipmaps, sem stencil | o alvo do segundo desenho |
| `uResolution` | largura e altura do canvas, passadas no construtor | precisa ser atualizado quando o canvas muda de tamanho, o que o tutorial deixa de fora |

## O que cada buffer enxerga no Sobel

| Buffer | Acha | Deixa escapar | No tutorial |
|---|---|---|---|
| cor da cena | toda borda, inclusive a das sombras projetadas e das sombras próprias | o contorno do objeto que tem a cor parecida com a do que está atrás | entra com peso 0,6 |
| normais | os contornos que a cor perde, e é onde o ruído vira sombreado | a superfície plana, sem variação de normal: o plano da cena fica sem grão nenhum | entra com peso 0,3, com ruído e distorção |
| profundidade | com as normais, é a receita comum de contorno limpo, que pega a silhueta e deixa de fora as linhas de dentro (ela remete ao tutorial de Omar Shehata, "How to render outlines in WebGL"); sozinha, sem a cor, contornaria os objetos sem contornar as sombras | — | fica de fora: para o lápis, diz a autora, a detecção completa não é necessária; aparece como próximo passo |

## Os dois ruídos e o que cada um produz

| Ruído | Origem | Onde entra | O que produz | Por que esse |
|---|---|---|---|---|
| gradiente de Inigo Quilez | gerado no próprio shader | multiplica a parcela das normais | grão de lápis e pontilhado onde a normal muda | o sombreado sai uniforme |
| textura de nuvens | imagem feita no Photoshop com o filtro Render Clouds, entregue por uniform como os buffers | desloca a coordenada de leitura das normais | o traço que treme | o ruído da textura é suave, e a linha não serrilha |

A regra do tremido cabe numa frase: "we get the squiggled line effect by distorting the image we’re reading from, not by drawing to a different place". Entre gerar o ruído e importá-lo, o que muda, segundo a autora, é o grau de flexibilidade e de controle. O deslocamento também pode variar de buffer para buffer, o que desencontra as linhas e, para ela, deixa o resultado mais perto do desenho à mão. Dois caminhos ficam só sugeridos no fim: variar a espessura da linha com um limiar de borda modulado por textura de ruído, e tirar o ruído da luz da cena em vez das normais.

## Onde está o código

- **Demo:** https://tympanus.net/Tutorials/PencilLines/ (não aberta).
- **Código:** https://github.com/mayacoda/pencil-lines (só o resumo visto, na rodada; código não lido). O código do artigo está em TypeScript e importa `Pass` e `FullScreenQuad` de `three/examples/jsm/postprocessing/Pass`.
- **Uma Codesandbox por etapa** (nenhuma aberta): o passe com o `CopyShader`, https://codesandbox.io/s/brave-napier-izrvkk; o Sobel só na cor, https://codesandbox.io/s/kind-leakey-wojyvw; cor e normais, https://codesandbox.io/s/thirsty-wood-2rbs9l; o efeito final, com ruído e distorção, https://codesandbox.io/s/dreamy-mountain-t2zc71.
- **De onde vêm as peças:** o Sobel é cópia do `SobelOperatorShader` do Three.js, com a mudança de calcular o valor de cada pixel numa função própria (`getValue`) para somar as normais; a luminância vem do `glsl-luma`; o ruído, da implementação de Quilez no Shadertoy (https://www.shadertoy.com/view/XdXGW8).

## Lacuna

O artigo não diz a versão do Three.js usada nem quanto custa, em tempo de quadro, desenhar a cena uma segunda vez para o buffer de normais.
