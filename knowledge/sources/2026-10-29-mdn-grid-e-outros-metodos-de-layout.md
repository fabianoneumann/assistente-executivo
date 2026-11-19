---
titulo: "Relationship of grid layout to other layout methods (MDN)"
tipo: artigo
autor: "MDN contributors (Mozilla)"
url: "https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods"
publicado_em: 2026-04-07
capturado_em: 2026-10-29
licenca: "Texto em CC BY-SA 2.5 e exemplos de código em CC0 (LICENSE.md do repositório mdn/content)"
areas: [content-design]
tags: [css, css-grid, flexbox, absolute-positioning, layout, html-pieces]
---

Ficha de estudo em palavras próprias; o texto integral (licença CC BY-SA 2.5) não vem neste repositório e se lê na url do frontmatter. Guia do MDN; `publicado_em` é a data da última alteração da página (rodapé: "last modified on Apr 7, 2026", igual ao último commit do arquivo no repositório `mdn/content`). Lido em 2026-10-29, na pesquisa sobre o layout das peças de tela fixa em HTML.

## O que é

O guia que situa o CSS grid entre os outros métodos de layout: o flexbox, a posição absoluta e o `display: contents`. Não é referência de propriedade; é o critério de escolha, com exemplos lado a lado.

## Grid e flexbox

- **Uma dimensão contra duas:** o flexbox foi feito para uma linha **ou** uma coluna; o grid, para linhas **e** colunas ao mesmo tempo. A pergunta que o guia propõe: preciso controlar o layout só por linha ou só por coluna (flexbox), ou pelas duas (grid)?
- **Do conteúdo para fora contra do layout para dentro:** no flexbox, o tamanho do conteúdo decide quanto espaço cada item ocupa, e cada linha que quebra reparte o espaço sozinha (os itens da segunda linha não se alinham com os da primeira). No grid, primeiro se cria a grade e depois se põem os itens nela.
- **O sinal de troca:** se, no flexbox, você começa a desligar a flexibilidade (dar largura fixa a um item para alinhar com o de cima), provavelmente o caso é de grid.
- **Alinhamento:** as propriedades de alinhamento nasceram no flexbox e hoje moram no módulo de alinhamento de caixa, usado pelos dois; no grid, o item se alinha dentro da sua área.
- **`fr` e `minmax()`:** com `repeat(auto-fill, 200px)` o grid cria quantas colunas couberem; com `repeat(auto-fit, minmax(200px, 1fr))`, colunas de no mínimo 200 px que repartem o que sobra, um comportamento parecido com o do flexbox, mas mantendo linhas e colunas.

## Grid e posição absoluta

- **O contêiner de grid como bloco de referência:** com `position: relative` no contêiner, um item com `position: absolute` toma o contêiner como referência; se o item também tem posição na grade (linhas de início e fim), a referência é a área da grade onde ele está, e `top` e `left` deslocam dentro dela.
- **Sai do fluxo:** o item absoluto não participa mais do tamanho da grade nem do posicionamento automático; os outros itens ocupam o lugar dele, e a linha que ele pediria não é criada.
- **Sem `position: relative` no contêiner,** a referência vira o que estiver acima com posição (no exemplo, a janela).
- **Área da grade como pai:** um item aninhado dentro de uma área com `position: relative` se posiciona em relação a essa área.

## Grid e `display: contents`

Com `display: contents`, a caixa do elemento some e os filhos sobem um nível, virando itens da grade (ou do flexbox). Serve para tratar como itens da grade os filhos de um item aninhado.

## O fecho do guia

O grid é uma ferramenta entre outras; o guia recomenda misturar os métodos para cada efeito.

---
