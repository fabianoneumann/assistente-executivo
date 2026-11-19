---
titulo: "Simulating Hand-Drawn Motion with SVG Filters"
tipo: artigo
autor: "Camillo Visini"
url: "https://camillovisini.com/coding/simulating-hand-drawn-motion-with-svg-filters"
publicado_em: 2025-07-09   # "Published on July 09, 2025" na página (no topo e no bloco do autor)
capturado_em: 2026-11-11
licenca: "protegido ('© 2025 Camillo Visini' no rodapé; sem licença de conteúdo declarada no texto lido, e nenhuma licença para o código mostrado); ficha em palavras próprias e em estrutura própria, sem o integral"
areas: [generative-media]
tags: [line-boil, svg-filters, hand-drawn, feturbulence, fedisplacementmap, web-animation]
---

# Visini: o tremor de traço à mão (line boil) com filtros SVG

Nota de fato: tabelas da receita e dos valores, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: o post é protegido.

**Proveniência.** Post do blog de Camillo Visini (que assina como CEO e fundador da Visini AG), https://camillovisini.com/coding/simulating-hand-drawn-motion-with-svg-filters, subtítulo "A practical guide to implementing the boiling line animation effect using SVG filter primitives and JavaScript", baixado com curl em 2026-11-11, com o texto extraído do HTML (`sha256` (hash omitido); Wayback: http://web.archive.org/web/20261012041930/https://camillovisini.com/coding/simulating-hand-drawn-motion-with-svg-filters). Lido inteiro o texto, com o bloco de código; das demonstrações interativas, que não foram executadas, leram-se as legendas e os valores iniciais que o HTML passa aos componentes (atributo `props`), marcados como tal abaixo. O clipe da ARTE e as imagens não foram vistos.

Condensada em nota de fato em 2026-11-11, depois de três reescritas em prosa que seguiam a fonte.

**Conferência lado a lado** (2026-11-11, na condensação, pela régua de 2026-11-11 do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (número, nome, comando, flag, valor ou rótulo curto) fica fora, como as marcas "—" e "não informado". Corpo: 4 frases de prosa e 117 células de dados em 5 tabelas, 14 delas marcas e 103 de fato; as 3 que trazem verbo são rótulos da primeira coluna. A frase da recomendação junta a decomposição, a nota sobre raster e SVG e a conclusão do post. Resultado: 0 das 4 unidades seguem a fonte; as três citações literais estão à parte. A versão anterior, pela mesma régua, dava 16 de 19 (re-revisão do Passo 7).

## Em uma frase

Post de 2025 que reconstrói na web o contorno trêmulo dos desenhos animados com dois filtros SVG e um temporizador em JavaScript, partindo de um documentário da ARTE; para a base, é a receita com valores da rota do tremor por filtro, uma das que a decisão sobre o tremor no vídeo compara.

## O efeito

| Item | Fato |
|---|---|
| Nomes | line boil; "boiling" |
| Técnica tradicional | o mesmo quadro redesenhado várias vezes seguidas |
| Variação entre as cópias | posição e rotação, leve |
| Para que serve | movimento em cena parada (ex.: personagem imóvel) |
| Demonstração manual do autor | decalques à mão do mesmo objeto |
| Quando a diferença entre decalques aparece | só com as cópias sobrepostas e animadas |
| Ponto de partida do autor | documentário da ARTE sobre a pizza napolitana |
| Estilo das ilustrações da ARTE | formas simples, cores chapadas |
| Conteúdo do trecho | a receita e os ingredientes |
| Autores das ilustrações | não identificados pelo autor |
| Leitura do autor sobre a ARTE | pós-processamento sobre formas "perfeitas" |
| Indício dele | contorno que treme em ciclo |
| Textura de papel na ARTE | sobreposta à cena inteira |
| Movimento da textura | também |
| Textura de papel no post | fora do escopo |

## A receita

| Peça | Fato |
|---|---|
| Ruído | `feTurbulence` (campo de ruído procedural) |
| Deslocamento | `feDisplacementMap`, guiado pelo ruído |
| Animação | JavaScript |
| O que a animação muda | atributos do filtro |
| Ritmo da troca | intervalo regular |
| Origem aceita | imagem raster ou SVG |
| Diferença entre raster e SVG | nenhuma |
| Ilustrações das demonstrações | raster |
| Peça menos intuitiva, para o autor | a distorção |

| Parâmetro | No código de exemplo | Nas demonstrações (props do HTML) | Papel |
|---|---|---|---|
| `feTurbulence type` | `turbulence` | não informado | ruído |
| `baseFrequency` | `0.03`, fixo | base `0.02` | o que oscila |
| Sequência de deslocamentos da frequência | — | `[-0.02, 0.01, -0.01, 0.02]` | um valor por tique |
| `numOctaves` | `2` | `5` | não explicado |
| `seed` | `1` | não informado | não explicado |
| `feDisplacementMap scale` | `20` | `displacementScale` `5` | intensidade |
| `xChannelSelector` | `R` | não informado | eixo x pelo canal vermelho |
| `yChannelSelector` | `G` | não informado | eixo y pelo canal verde |
| `in` | `SourceGraphic` | — | imagem deslocada |
| `in2` | o resultado do ruído | — | mapa de deslocamento |
| Intervalo da troca | — | `100ms` | um tique |
| Intervalo citado na decomposição | 200 ms, como exemplo | — | — |
| Cena completa do post | — | mesmos valores iniciais da demonstração | — |

## A dose

| Escala de animação | Conta no primeiro tique | Resultado |
|---|---|---|
| 0 | — | sem tremor |
| 0,5 | 0,02 + (−0,02 × 0,5) = 0,01 | tremor suave ("gentle") |
| 1 | — | oscilação inteira, ±0,02 entre quadros |

| Controle da dose | Fato |
|---|---|
| Os três botões | turbulência de base; intensidade do deslocamento; escala de animação |
| Mínimo do efeito | tremor sutil |
| Máximo do efeito | ondulação extrema e incômoda |
| No máximo | formas quase irreconhecíveis |

## O que a fonte recomenda

Montar o tremor em duas partes que se desenvolvem separadas, a deformação do contorno por ruído e o relógio que muda o ruído, o que serve tanto a desenho vetorial quanto a imagem raster; depois, dosar pela escala de animação, porque os mesmos controles que dão o tremor discreto, empurrados um pouco, apagam o desenho.

## Citações

- "drawing the same frame multiple times in a row, with slight variations in position and rotation"
- "the contours are wobbling “in a loop”"
- "A little goes a long way here: Don’t let things boil over."

## Lacuna

O post não mede custo de desempenho (quadros por segundo, navegador, tamanho da cena), não explica `numOctaves` nem `seed` além dos valores, não diz por que a sequência tem quatro valores nem por que 100 ms, e não trata de exportar o efeito para vídeo. O código de exemplo (0,03 e 20) e as demonstrações (0,02 e 5) aparecem sem comparação entre si.
