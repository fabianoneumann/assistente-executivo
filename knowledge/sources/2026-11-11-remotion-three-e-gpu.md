---
titulo: "Remotion: @remotion/three, <ThreeCanvas>, Using the GPU e --gl flag"
tipo: artigo
autor: "Remotion AG"
url: "https://www.remotion.dev/docs/three"
publicado_em: 2026-11-11   # último commit do three.mdx no repositório (2026-11-11); as outras três páginas na proveniência
capturado_em: 2026-11-11
licenca: "documentação sem licença de conteúdo declarada no texto lido (rodapé: '© Copyright 2026 Remotion AG.'; a Remotion License, no LICENSE.md, dá permissão para usar o software 'for the purpose of creating videos and images' e não fala da documentação); ficha em palavras próprias e em estrutura própria, sem o integral"
areas: [generative-media]
tags: [remotion, threejs, react-three-fiber, webgl, webgpu, gpu, deterministic-rendering, video-as-code]
---

# Remotion e o Three.js: a cena presa ao quadro, a GPU e o `--gl`

Ficha de estudo em palavras próprias, organizada por pergunta, não pela ordem das páginas. Não há integral: a documentação não declara licença de conteúdo.

**Proveniência.** Quatro páginas da documentação do Remotion, baixadas com curl (HTML) em 2026-11-11, com o texto extraído do HTML; entre parênteses, o último commit do `.mdx` de cada uma no `main` de `remotion-dev/remotion`: `@remotion/three`, https://www.remotion.dev/docs/three (2026-11-11, uma revisão de redação); `<ThreeCanvas>`, https://www.remotion.dev/docs/three-canvas (2026-11-09, commit `38323ae2de`, "docs: list all inherited Sequence props…"); "Using the GPU", https://www.remotion.dev/docs/gpu (2026-10-28); "--gl flag", https://www.remotion.dev/docs/gl-options (arquivo `open-gl.mdx`, 2026-11-10). As quatro dizem "Last updated on Nov 11, 2026". Versão corrente do Remotion no dia: v4.0.542 (2026-11-09). Não há ficha de setembro sobre estas páginas.

**Conferência lado a lado** (2026-11-11, na reescrita pedida pela revisão do Passo 7, N23): unidade é a frase fora de tabela ou a célula preenchida de tabela, e uma unidade segue a fonte quando traduz uma frase dela, ou duas vizinhas, na ordem delas. Resultado: 35 de 74 unidades seguem uma frase da fonte (35 de 48 sem contar as células que só trazem um nome, um rótulo ou um valor). Quase todas as que seguem são um fato de API, de flag ou de ambiente que a página diz numa frase; as seções e as tabelas se organizam pelas perguntas da ficha (o que pôr na cena, o que fazer e evitar, onde se renderiza), juntando as quatro páginas.

## O que pôr na cena e com quê

`@remotion/three` liga o React Three Fiber (R3F) ao Remotion e se instala com `three`, `@react-three/fiber` e `@types/three` (npm, yarn ou pnpm); fora as peças da tabela, valem as APIs comuns do R3F.

| Quero na cena | Uso | O que saber |
|---|---|---|
| uma cena 3D que siga a timeline | `<ThreeCanvas>`, o `<Canvas>` do R3F preso ao `useCurrentFrame()` | pede `width` e `height` e WebGL; repassa ao R3F os contextos React que um renderizador próprio deixaria de fora, e sem os quais o Remotion quebraria |
| o renderizador WebGPU, com materiais de nós TSL | `<ThreeWebGPUCanvas>` | — |
| um vídeo como textura | `useVideoTexture()`, sobre um `<Html5Video>` | no render, o `useOffthreadVideoTexture()` dá o quadro exato como `ImageTexture`, à maneira do `<OffthreadVideo>` |
| controlar o trecho e a exibição da cena como num `<Sequence>` | as props que o `<ThreeCanvas>` herda dele desde a v4.0.528: `from`, `durationInFrames`, `trimBefore`, `playbackRate`, `freeze`, `hidden`, `name`, `showInTimeline`, `premountFor`, `postmountFor`, `styleWhilePremounted`, `styleWhilePostmounted` | sem indicação, ele fica fora da timeline e se chama `"<ThreeCanvas>"` |
| um ponto de partida | o `remotion-template-three` | repositório-modelo: celular 3D com vídeo trocável dentro e cor, tamanho, espessura e raio dos cantos ajustáveis, como introdução ao `<ThreeCanvas>` e ao `useVideoTexture()` |

- **Compatibilidade:** no markup da página (o `.mdx` embutido no HTML baixado), a `CompatibilityTable` do `<ThreeCanvas>` traz `chrome`, `firefox`, `safari`, `clientSideRendering`, `serverSideRendering`, `player` e `studio` como props verdadeiras; logo abaixo, "Requires WebGL".

## Fazer e evitar ao escrever a cena

| Fazer | Em vez de | Por quê, segundo as páginas |
|---|---|---|
| tirar rotação, cor, escala e o resto do `useCurrentFrame()`, no próprio markup (o exemplo da página é um cubo que gira, troca de cor e pulsa assim) | animar num `useFrame()` do R3F | é o que permite arrastar a timeline nos dois sentidos e pausar; a página diz "can (and must)" |
| dar `width` e `height` ao `<ThreeCanvas>` | deixar o tamanho por conta do layout | o Studio escala o canvas, e um bug de navegador desmontaria o layout |
| pôr `layout="none"` em todo `<Sequence>` dentro do canvas | o `<Sequence>` como vem | sem isso ele devolve um `<div>`, que ali dentro dá erro |
| depois de trocar uma textura fora do ciclo (no `onVideoFrame` de um `<Video>`, por exemplo), chamar `advance(performance.now())` | `invalidate()` | no render, o `frameloop` fica preso em `'never'`, passe-se o que for, e só o `advance()` redesenha a cena, na hora, antes da captura do quadro |
| renderizar com o `angle` (onde pôr, na tabela "Por onde se escolhe") | o renderizador OpenGL padrão | é a nota da página sobre o render do lado do servidor: com o padrão, o Three.js não renderiza |

## A GPU: por que ligar e que `--gl` escolher

- **Por que ligar:** no render sem janela (headless), o Chromium desliga a GPU e o render perde muito tempo ("significant slowdown in rendering time"), enquanto no Studio e no Player ela já vem ligada quando a máquina tem uma. O que ela acelera: WebGL (Three.js, Skia, P5.js, Mapbox e outros), decodificação de vídeo, `box-shadow`, `text-shadow`, `linear-gradient()` e `radial-gradient()` em `background-image`, `filter: blur()` e `filter: drop-shadow()`, `transform` e muitas operações de canvas 2D.

O `--gl` no Remotion 4.0, por lugar de render, juntando a página do `--gl` e a da GPU:

| Onde se renderiza | GPU lá | Cena com WebGL, WebGPU ou Three.js | Cena sem nada disso |
|---|---|---|---|
| desktop | as páginas não dizem | `angle` | o padrão |
| instância de nuvem com GPU | sim | `angle-egl` | o padrão |
| máquina sem GPU | não | `swangle`, e o render pode sair lento | o padrão |
| AWS Lambda | não | `swangle`, que já é o padrão lá | `swangle` |
| Google Cloud Run | as páginas não dizem | as páginas não dizem | `swangle` |
| GitHub Actions | não, nos runners | o `angle` faz o render falhar; outro valor não é indicado | as páginas não dizem |

O padrão é `null` no render local e `swangle` no Lambda e no Cloud Run, e a página o dá como a melhor escolha para quem não usa WebGL, WebGPU nem Three.js. Fora da tabela, a mesma página diz que, quando a GPU ajuda, costuma valer o `angle`, ou o `angle-egl` no Linux, e deixa o quando e o como para um artigo à parte.

- **O preço do `angle`:** vazamento de memória, problema conhecido segundo a página do `--gl`; um render longo às vezes cai por isso, e a página recomenda partir vídeo grande em vários renders.
- **No 5.0:** o padrão vira `angle`, com a GPU compatível quando há e queda automática do Chromium para o SwiftShader quando não há; WebGL e WebGPU funcionam sem opção nenhuma, e Lambda e Cloud Run ficam no `swangle`.
- **Os valores aceitos:** `null` (padrão do 4.0: o Chrome decide), `angle` (padrão do 5.0), `egl`, `swiftshader`, `vulkan` (desde a v4.0.41), `angle-egl` (desde a v4.0.52) e `swangle` (SwiftShader sobre o ANGLE).

| Por onde se escolhe | Como | Vale em |
|---|---|---|
| APIs do Node | `chromiumOptions.gl` | pela página do `--gl`, `getCompositions()`, `renderStill()`, `renderMedia()`, `renderFrames()`, `getCompositionsOnLambda()`, `renderStillOnLambda()` e `renderMediaOnLambda()`; a do `@remotion/three`, ao pedir o `angle`, cita também `renderMediaOnVercel()` |
| arquivo de configuração | `Config.setChromiumOpenGlRenderer()`, que os projetos novos já trazem com `'angle'`; antes da v3.3.39, `Config.Puppeteer.setChromiumOpenGlRenderer()` | só os comandos da CLI, não o render pelo Node |
| linha de comando | `--gl=` | `remotion render`, `remotion compositions`, `remotion still` e os três equivalentes `remotion lambda render`, `lambda still` e `lambda compositions` |

## Lacuna

Nenhuma das quatro páginas mede o tempo de render: a lentidão sem GPU fica em palavras ("significant slowdown", "might be slow"), sem comparação entre `angle`, `angle-egl` e `swangle` nem custo por quadro de uma cena Three.js; a página da GPU pede relatos de quem usa para documentar mais. Não foram lidos o exemplo de GPU no render do lado do servidor nem o artigo sobre quando usar o `angle`, para os quais as páginas apontam.
