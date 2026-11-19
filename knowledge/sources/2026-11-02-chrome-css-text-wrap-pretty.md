---
titulo: "CSS text-wrap: pretty"
tipo: artigo
autor: "Adam Argyle (Chrome for Developers)"
url: "https://developer.chrome.com/blog/css-text-wrap-pretty"
publicado_em: 2023-10-23
capturado_em: 2026-11-02
licenca: "CC BY 4.0 para o conteúdo e Apache 2.0 para os exemplos de código, exceto onde a página diz o contrário (rodapé: Except as otherwise noted)"
areas: [content-design]
tags: [typography, line-breaking, text-wrap, orphans, css, chromium, web-standards]
---

Ficha de estudo em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Post do blog do Chrome for Developers; a data é a da última atualização da página ("Last updated 2023-10-23"), que não traz outra data de publicação. Lido em 2026-11-02.

## O que a página ensina

- **O que é:** um valor novo de quebra de linha, `text-wrap: pretty`, da especificação CSS Text Level 4, disponível no Chrome a partir da versão 117. Aplica-se com uma linha (`p { text-wrap: pretty; }`).
- **O problema que ataca:** palavras que ficam sozinhas no começo ou no fim de um bloco de texto. Pela definição da página, "widows" são as palavras sozinhas no alto de um bloco e "orphans", as sozinhas no fim; elas interrompem o jeito como o olho percorre o texto, e há designers que fazem de tudo para evitá-las.
- **O que faz no Chrome:** evita a palavra sozinha no fim do parágrafo ("orphan"). Faz um pouco mais que isso: ajusta a hifenização quando há linhas hifenizadas seguidas no fim do parágrafo, mexe nas linhas anteriores para abrir espaço e leva em conta o texto justificado. A página o descreve como uma quebra de linha melhor em geral, "currently focused on orphans", e diz que ele pode trazer outras melhorias no futuro.
- **O que não faz:** não trata a palavra sozinha no alto do bloco ("widow"); quem diz isso é a nota da página ("pretty only handles orphans, not widows"). A mesma nota avisa que o valor é outra coisa que a propriedade CSS `orphans`, que serve ao layout em várias colunas.
- **Comparação com `balance`:** o `text-wrap: balance` não evita a palavra sozinha; ele faz o texto quebrar de modo a formar um bloco harmônico. O autor diz que usa `balance` nos títulos e `pretty` nos parágrafos.
- **Detalhes do algoritmo e desempenho:** a página não os dá; aponta para o documento de desenho escrito pelo engenheiro da funcionalidade, Koji Ishii, e pede que sugestões de quebra de linha sejam enviadas ao rastreador de bugs do Chromium, com exemplos de quebras boas e ruins.
- **Imagens:** duas comparações de parágrafo com e sem palavras sozinhas, tiradas do Google Fonts (glossário "Widows & Orphans") e do site uxmovement.com.
