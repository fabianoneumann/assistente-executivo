---
titulo: "MotionPath"   # título da página; o do HTML é "MotionPath | GSAP | Docs & Learning"
tipo: artigo
autor: "GSAP (Webflow)"   # página da documentação, sem assinatura de pessoa
url: "https://gsap.com/docs/v3/Plugins/MotionPathPlugin/"
publicado_em: null   # a página não traz data; as versões citadas no texto vão até a 3.7.0 (fromCurrent)
capturado_em: 2026-11-12
licenca: "protegido (rodapé: '©2026 GSAP - A Webflow Product. All rights reserved.'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [gsap, motion-path, svg, web-animation, camera-path, easing, interested-party]
---

# GSAP MotionPathPlugin: animar ao longo de um caminho, com o tempo remapeado para a velocidade não oscilar

Nota de fato: uma tabela por seção da página, na ordem dela, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Página da documentação do GSAP 3, https://gsap.com/docs/v3/Plugins/MotionPathPlugin/, baixada com curl em 2026-11-12 e lida no texto extraído do HTML, conferido no próprio HTML. A página abre com o título "MotionPath"; o título do HTML é "MotionPath | GSAP | Docs & Learning". sha256 (hash omitido), que mede o texto do bloco `<main>` ou `<article>` sem tags, script e estilo (não o HTML inteiro); Wayback `http://web.archive.org/web/20261106034404/https://gsap.com/docs/v3/Plugins/MotionPathPlugin/`. Cobertura: o texto inteiro da página (o começo rápido, os destaques, o objeto de configuração, a nota sobre o alinhamento, a seção de outras propriedades e a lista de métodos); o código e o CSS das duas demonstrações foram lidos só para ver o que elas fazem, e o vídeo e a coleção de demonstrações no CodePen não foram abertos. Texto de quem faz a ferramenta, que se elogia ("no other tool on the web offers this functionality"). Documentação mais longa que uma fonte curta (umas 2.600 palavras de texto fora o código das demonstrações), lida por seções, por isso nota de fato com uma tabela por seção, na ordem da página.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática, contra o texto extraído: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), com "unidades medidas: 41 (14 de prosa, 27 de célula com texto)" e "coladas: 0 de 41 (0%); trechos de 3 ou mais seguidas: 0". Na leitura lado a lado das mesmas 41 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a célula que só traz um fato fica fora, e as 10 frases da linha do formato, da proveniência e desta conferência, a frase da recomendação (que junta o `resolution`, o `autoRotate` e a nota do alinhamento) e as duas da lacuna não seguem frase nenhuma. Resultado: 27 de 41 (a frase de "Em uma frase" e 26 das 27 células com texto, que vertem cada uma a descrição de uma forma, propriedade ou método; fica fora a célula que descreve o código da primeira demonstração). A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 15 (de "Em uma frase" à célula do `useRadians`), e a segunda de 9 (da célula do alinhamento não responsivo à do `pointsToSegment`), as duas em descrição de forma, propriedade e método, que é dado, numa nota de fato com uma tabela por seção na ordem da página; no texto de recomendação da página (a nota do alinhamento e o conselho do `resolution`), nenhuma sequência leva mais de 1 unidade de recomendação, porque a saída proposta vem antes do "não é responsivo" na tabela e os conselhos do `resolution` estão em células de fato curtas.

## Em uma frase

Página da documentação do GSAP sobre o plugin que move um alvo por um caminho (um `<path>` de SVG, os dados de um path, uma lista de pontos ou até uma sequência de valores de outras propriedades), com alinhamento do alvo ao caminho, rotação na direção dele, trechos de 0 a 1 e uma correção do tempo para a velocidade não variar com o desenho da curva.

## As formas do caminho (começo rápido)

| Forma | Fato |
|---|---|
| Registro | `gsap.registerPlugin(MotionPathPlugin)` |
| Uso mínimo | `motionPath: { path: "#path" }` num `gsap.to` |
| Elemento `<path>` de SVG | por seletor ou referência direta |
| Dados de path em texto | ex.: `"M9,100c0,0,18-41,49-65"` |
| Lista de pontos x, y | a curva passa pelos pontos; a posição atual do alvo entra no começo |
| Lista de pontos com `type: "cubic"` | lida como bézier cúbica: âncora, dois controles, âncora |
| Lista de valores de outras propriedades | ex.: `scale` e `rotation`; suaviza a mudança de velocidade a cada valor |
| Objeto de configuração | o `path` em qualquer das formas, mais `align`, `alignOrigin`, `autoRotate`, `start`, `end` |

## Os destaques da página

| Recurso | Fato |
|---|---|
| Alinhamento | põe o alvo sobre o caminho, ou o caminho sobre o alvo, por mais aninhados e transformados que estejam os contêineres |
| `autoRotate` | o alvo gira na direção do caminho |
| Trecho | começo e fim por progresso de 0 a 1, com volta e marcha a ré |
| Edição no navegador | ferramenta à parte, o MotionPathHelper |
| Sem SVG | basta dar coordenadas; a curvatura se ajusta |
| Métodos auxiliares | converter formas SVG em `<path>`; posição relativa entre dois elementos; path em texto para bézier crua e de volta; conversão entre espaços de coordenadas |

## O objeto de configuração

| Propriedade | Tipo | Padrão | Fato |
|---|---|---|---|
| `path` | String, Element ou Array | obrigatória | o caminho, em qualquer das formas acima |
| `align` | String ou Element | — | sem ela, as coordenadas do path entram cruas no x e y do alvo; com ela, o alvo vai para cima do caminho; `"self"` move o caminho para o alvo, que assim não salta no começo |
| `alignOrigin` | Array | — | o ponto do alvo que fica sobre o caminho, em progresso de x e y (`[0.5, 0.5]` é o centro); acerta também o `transformOrigin`; desde a 3.2.0 |
| `autoRotate` | Boolean ou Number | — | `true` segue o ângulo do caminho; um número soma graus (90 gira um quarto a mais) |
| `start` | Number | 0 | onde começa no caminho (0,3 é 30%); aceita negativo |
| `end` | Number | 1 | onde termina; menor que `start` anda para trás, 1,5 dá a volta e para no meio |
| `curviness` | Number | 1 | só para lista de pontos: 0 dá retas com quinas, 2 bem mais curva; afasta os controles das âncoras |
| `offsetX`, `offsetY` | Number | 0 | ajuste fino do alinhamento |
| `fromCurrent` | Boolean | ligado | desligado, a posição atual não entra no começo da lista e o alvo salta para o primeiro ponto; desde a 3.7.0 |
| `relative` | Boolean | — | só para lista: cada valor soma ao anterior (x 100 com `[{x:5},{x:10},{x:-2}]` passa por 105, 115 e 113) |
| `type` | String | — | `"cubic"` para ler a lista de x, y como béziers; começa e acaba em âncora |
| `resolution` | Number | 12 | só para lista: quantos pedaços por segmento a correção do tempo usa |
| `useRadians` | Boolean | false | rotação em radianos, útil com bibliotecas que usam radianos, como Pixi.js |

## A velocidade no caminho (`resolution`)

| Ponto | Fato |
|---|---|
| O problema | numa bézier, o alvo parece acelerar e frear conforme o lugar dos controles e o comprimento de cada segmento |
| O que o plugin faz | remapeia o tempo, cortando cada segmento em pedaços, para reduzir ou eliminar a variação |
| Mais pedaços | remapeamento mais exato, com mais processamento |
| Quando subir o valor | se ainda se notar mudança de ritmo no caminho |
| Quando baixar | para dar prioridade à velocidade de cálculo |

## A demonstração e a nota sobre o alinhamento

| Ponto | Fato |
|---|---|
| Demonstração | um retângulo de SVG percorre um path com `align`, `autoRotate` e `alignOrigin: [0.5, 0.5]`, em 5 s, com `ease: "power1.inOut"` e vaivém |
| Quando o alinhamento se calcula | uma vez, no começo da animação |
| Saída proposta | um ouvinte de resize próprio: guardar o progresso, `progress(0).kill()`, criar uma animação nova e saltar ao progresso guardado |
| Responsivo | não: se a tela mudar de tamanho e o caminho mudar, o alinhamento não se refaz |
| Por quê | recalcular a cada tick custaria CPU demais |

## Outras propriedades no lugar de coordenadas

| Ponto | Fato |
|---|---|
| O que se passa | lista de objetos com outras propriedades, como `scale` |
| O que o plugin faz | suaviza a mudança de velocidade ao passar por cada valor |
| Demonstração | três escalas (1,3, 0,2 e 1), em 3 s sem easing, com `curviness` 0 e 2 lado a lado |
| O que ela mostra | com curvatura maior, a mudança de velocidade fica mais suave |

## Os métodos

| Método | Fato |
|---|---|
| `arrayToRawPath` | curva por uma lista de coordenadas, devolvida como RawPath; aceita `type: "cubic"` |
| `convertCoordinates` | leva um ponto do espaço local de um elemento para o de outro, com as transformações aninhadas |
| `convertToPath` | `<circle>`, `<rect>`, `<ellipse>`, `<line>` viram `<path>` |
| `getAlignMatrix` | Matrix2D para alinhar um elemento a outro |
| `getGlobalMatrix` | Matrix2D do espaço local de um elemento para o global |
| `getLength` | comprimento de um path |
| `getPositionOnPath` | x, y (e o ângulo, se pedido) num progresso do RawPath |
| `getRawPath` | o RawPath de um elemento ou de dados de path: um array por segmento contínuo, com x, y alternados de bézier cúbica |
| `getRelativePosition` | a distância x, y entre dois elementos, no sistema do pai do primeiro |
| `pointsToSegment` | segmento de bézier cúbica por uma lista de pontos, com curvatura |
| `rawPathToString` | sem descrição na página |
| `sliceRawPath` | corta o RawPath entre um começo e um fim |
| `stringToRawPath` | sem descrição na página |

## O que a fonte recomenda

Quando o ritmo no caminho importa, a página manda confiar na correção do tempo e só mexer na `resolution` se ainda se notar oscilação; para girar e centrar o alvo no caminho, usar `autoRotate` com `alignOrigin` no meio (ou `transformOrigin` e os percentuais de x e y); e, como o alinhamento se fixa no começo, refazer a animação por conta própria quando a tela mudar de tamanho.

## Citações

- "When you align the motionPath, those calculations are done at the very start of the animation - it is NOT responsive"
- "The greater the number, the more accurate the time remapping. But there is a processing price to pay for greater precision."
- "If true, each successive value is interpreted as relative to the previous one."

## Lacuna

A página só trata de duas dimensões (x e y, SVG e DOM): não fala de caminho em 3D nem de câmera, e não diz se o progresso de 0 a 1 se mede por comprimento de arco depois da correção do tempo. Não dá os padrões de `align`, `autoRotate`, `relative` e `type`, não descreve `rawPathToString` e `stringToRawPath`, não diz a versão atual do GSAP nem as condições de uso do plugin, e o vídeo e o MotionPathHelper ficam só citados.
