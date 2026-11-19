---
titulo: "Satori: Enlightened library to convert HTML and CSS to SVG (README, v0.63.2)"
tipo: artigo
autor: "Shu Ding e Vercel (vercel/satori)"
url: "https://github.com/vercel/satori"
publicado_em: 2026-10-20
capturado_em: 2026-10-29
licenca: "MPL-2.0 (arquivo LICENSE do repositório vercel/satori e campo license do package.json da v0.63.2)"
areas: [content-design]
tags: [satori, svg, html-to-image, css-grid, flexbox, layout-engine, html-pieces]
---

Ficha de estudo; o README integral (licença MPL-2.0) fica na url. É o README da versão 0.63.2, publicada no npm e no GitHub em 20/10/2026 (a mais recente em 2026-10-29), baixado do pacote no unpkg. Lido em 2026-10-29, na pesquisa sobre o layout das peças de tela fixa em HTML, para conferir se o Satori aceita grid.

## O que é

Biblioteca da Vercel que converte HTML e CSS (escritos em JSX ou como objetos) em SVG, para gerar imagens como as de Open Graph e cartões de rede social; o PNG sai do SVG pelo Sharp. Roda no navegador, no Node.js (16 ou mais) e em Web Workers, com dependências em WASM. Não usa navegador: tem motor de layout próprio, então não garante resultado idêntico ao do navegador.

## O ponto que importa aqui: grid é aceito

O README diz que o Satori usa o **Taffy** (motor de layout em Rust) para flexbox, **grid** e layout em bloco, e um layout próprio para texto e elementos em linha. Na tabela de propriedades, a seção de grid marca como aceitos: `gridTemplateColumns` e `gridTemplateRows` (menos `subgrid`, que dá erro, e `masonry`), `gridTemplateAreas`, `gridAutoColumns`, `gridAutoRows`, `gridAutoFlow`, `gridRow`, `gridColumn`, `gridArea` e as formas longas, `justifyItems`, `justifySelf`, `placeItems`, `placeContent`, `placeSelf` e os atalhos `grid` e `gridTemplate`. Material que diz que o Satori só aceita flexbox (há guias assim circulando, inclusive de habilidades para agentes) descreve versões antigas, do tempo em que o layout era o Yoga; o README não diz em que versão a troca aconteceu.

## Outras diferenças que tocam as nossas peças

- **`position`:** aceito; um elemento em linha posicionado não serve de referência para os filhos absolutos (vale o bloco posicionado mais próximo). `top`, `right`, `bottom`, `left`, `inset` e `zIndex`: aceitos.
- **`display`:** aceito, menos `table`, `ruby` e a sintaxe de dois valores, que dão erro.
- **`lineHeight`:** arredondado para pixel inteiro.
- **`calc()`, `min()`, `max()`, `clamp()` com porcentagem:** só funcionam em tamanhos, margens, enchimentos, deslocamentos, `gap`, `flexBasis` e translações; fora disso, o valor é ignorado.
- **Propriedades fora da tabela são ignoradas** (exemplos do README: `columns`, `writingMode`, `fontStretch`); `text-box-trim` e `text-fit` não aparecem na tabela.
- **Folhas de estilo:** o CSS de `<style>` vale para a árvore toda, com seletores, especificidade, `@media` (com a largura e a altura da imagem), `@container` de tamanho, `::before` e `::after`; `@font-face`, `@keyframes` e `@import` são ignorados, e `<link>` e `<script>` não carregam. Pseudo-classes de interação nunca casam.
- **Arredondamento à grade de pixels:** `pointScaleFactor` (padrão 1) arredonda os valores de layout para múltiplos de 1/fator px; 0 desliga.
- **Fontes:** passadas como dados na chamada (não há `@font-face`); recursos de OpenType pelo HarfBuzz.
- **Estilo inválido** em estilo em linha derruba a renderização inteira, a não ser que se trate com `onStyleError`.

## Para o nosso uso

As peças da série saem do navegador (shot-scraper), não do Satori; a ficha serve para quando se pensar em gerar imagem sem navegador, e para corrigir a ideia de que o Satori obriga a montar tudo em flexbox.

---

O texto integral está na url do frontmatter.
