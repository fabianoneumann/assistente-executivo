---
titulo: "Blender Manual: Line Art Modifier e Freestyle (Introduction)"
tipo: artigo
autor: "Blender Documentation Team (manual do Blender)"
url: "https://docs.blender.org/manual/en/latest/grease_pencil/modifiers/generate/line_art.html"
publicado_em: 2026-11-12   # rodapé das duas páginas: "Last updated on 2026-11-12"; manual 5.3 (latest)
capturado_em: 2026-11-12
licenca: "CC BY-SA 4.0 (rodapé de cada página: 'This page is licensed under a CC-BY-SA 4.0 Int. License'); o integral está na url"
areas: [generative-media]
tags: [blender, line-art, grease-pencil, freestyle, npr-rendering, outline, occlusion, bake]
---

# Blender: as duas rotas de linha, o Line Art (Grease Pencil) e o Freestyle

Ficha, organizada pelo que cada rota faz e pelo que custa; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Duas páginas do manual do Blender 5.3, baixadas com curl em 2026-11-12, com o texto extraído do HTML: "Line Art Modifier", https://docs.blender.org/manual/en/latest/grease_pencil/modifiers/generate/line_art.html (sha256 do HTML (hash omitido)), e a introdução do Freestyle, https://docs.blender.org/manual/en/latest/render/freestyle/introduction.html ((hash omitido)). Lidas inteiras; das outras páginas do Freestyle (estilos, conjuntos de linhas, Python), nada foi lido. Os HTML estão em a pasta da rodada.

## Line Art: o que é e o que pede

| Ponto | O que a página diz |
|---|---|
| O que faz | gera traços de Grease Pencil a partir de uma cena, de uma coleção ou de um objeto (malha, texto, curva, superfície) |
| Condição | a cena precisa de câmera ativa; só se gera linha no que essa câmera vê |
| Custo de vários modificadores | não há cache global: cada modificador Line Art refaz o cálculo de oclusão inteiro, então separar partes da cena em vários (para estilos diferentes) demora bem mais; a página chama isso de limitação conhecida |
| Use Cache | o modificador que não é o primeiro da pilha pode reaproveitar os dados do primeiro, perdendo algumas opções |
| Oclusão | mesmo filtrando por coleção, ele carrega a cena visível inteira para a oclusão sair certa, salvo o que se marcar fora pela propriedade de uso do objeto ou da coleção |
| Saída | camada e material de Grease Pencil, raio e opacidade do traço; pode gerar formas preenchidas no lugar do contorno |

## Line Art: que linhas, e como se ajustam

- **Tipos de aresta:** contorno (com silhueta do conjunto ou de cada objeto), vinco abaixo de um ângulo (o limiar por objeto vence o padrão), interseção entre faces, borda entre materiais, marcas de aresta do Freestyle, arestas soltas, contorno de luz e sombra projetada a partir de uma luz de referência; há filtro por região iluminada ou sombreada.
- **Geometria:** câmera própria no lugar da ativa (para assar tomadas de vários ângulos e para efeitos de motion graphics); arestas sobrepostas tratadas como contorno; objetos instanciados (com custo quando são muitos); linha de recorte nos planos perto e longe; tirar as faces de trás acelera, mas muda os níveis de oclusão.
- **Oclusão por nível:** 0 é a linha visível, 1 é a escondida por exatamente uma camada de faces; máscaras de material e de coleção escolhem linhas por quem as esconde.
- **Encadeamento:** juntar interseção com contorno, tratar tudo como contorno, guardar detalhe pequeno ou suavizar, encadear pela distância na geometria ou na imagem, limiar de distância, suavização de cadeia serrilhada e quebra em curva fechada.
- **Composição:** **Overscan** dá uma margem fora do quadro para o traço não acabar seco na borda da imagem; recorte na borda; deslocamento do traço em direção à câmera.
- **Bake:** assa os traços do objeto Grease Pencil ativo no intervalo de quadros da cena (ou de todos os que têm Line Art), e os modificadores assados se desligam sozinhos; limpar o assado apaga também o que se desenhou à mão no mesmo intervalo.

## Freestyle

- **O que é:** motor de render NPR de linha que usa os dados da malha e a profundidade Z para desenhar linhas em tipos de aresta escolhidos, com aparência artística ("hand drawn", "painted") ou técnica.
- **Duas formas de definir o estilo:** parâmetros de um Line Style (tracejado, vários tipos de linha, modificadores) ou scripts em Python, com estilos prontos (pincel japonês, cartoon, blueprint, espessura pela profundidade).
- **Organização:** liga-se em Render; os ajustes ficam na View Layer; uma view layer tem um mapa de vista (detecção de arestas), que tem vários Line Sets, cada um com um Line Style.
- **Limites declarados:** consome muita memória (todas as malhas da view layer carregam de uma vez); só malhas com faces; não detecta arestas nas interseções de faces; o resultado não tem profundidade Z; câmera panorâmica não funciona.

## Citações

- "each Line Art modifier will run the entire occlusion calculation for itself"
- "This optimization however, can result in strokes ending abruptly at the edge of the image."
- "Freestyle rendering results do not have any Z depth information."

## Lacuna

Nenhuma das duas páginas dá tempo de cálculo, fala de estabilidade da linha entre quadros com a câmera andando, ou trata do render em segundo plano (`-b`). A do Freestyle não diz se ele roda na CPU ou na GPU, nem compara com o Line Art.
