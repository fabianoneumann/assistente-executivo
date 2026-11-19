---
titulo: "CSS text-wrap: balance"
tipo: artigo
autor: "Adam Argyle (Chrome for Developers)"
url: "https://developer.chrome.com/docs/css-ui/css-text-wrap-balance"
publicado_em: 2023-12-19
capturado_em: 2026-11-02
licenca: "CC BY 4.0 para o conteúdo e Apache 2.0 para os exemplos de código, exceto onde a página diz o contrário (rodapé: Except as otherwise noted)"
areas: [content-design]
tags: [typography, line-breaking, text-wrap, headlines, css, chromium, web-standards]
---

Ficha de estudo em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Página da documentação do Chrome for Developers (seção CSS and UI); a data é a da última atualização ("Last updated 2023-12-19"), que não traz outra data de publicação. Lido em 2026-11-02.

## O que a página ensina

- **O que é:** o valor `balance` de `text-wrap`, da especificação CSS Text Level 4. Suporte listado na página: Chrome 114, Edge 114, Firefox 121, Safari 17.5.
- **O problema:** sem ele, quem escreve para a web tinha poucas ferramentas para equilibrar as linhas (as melhores eram `<wbr>` e `&shy;`), porque não sabe de antemão o tamanho final, o corpo nem a língua do título; o navegador sabe. O exemplo da página é um título com largura máxima de `50ch` que ocupa a largura toda e deixa duas palavras penduradas na segunda linha.
- **O que faz:** pede ao navegador a solução de quebra mais equilibrada para o texto. No exemplo, o título passa a quebrar antes do fim da linha e vira um bloco equilibrado. O autor afirma que o bloco equilibrado agrada mais ao olho, chama mais a atenção e é mais fácil de ler.
- **Contexto histórico:** equilibrar títulos era trabalho manual, ou ótico (o designer quer agradar ao olho, não à conta: o tema do alinhamento métrico contra o ótico); para publicações grandes como o New York Times, o equilíbrio de títulos é um detalhe importante de experiência. A prática vem dos tipógrafos que compunham à mão.
- **Uso principal: títulos.** A página recomenda aplicar a `h1` a `h6`, e lembra que o texto precisa de um comprimento máximo de linha vindo de algum lugar; os exemplos usam `max-inline-size`, que funciona como `max-width` para qualquer língua. Uma nota da página registra que o texto corrido do artigo raramente se equilibra, porque não precisa se destacar nem chamar o olho.
- **Limite:** equilibrar custa processamento, porque o navegador faz várias tentativas; por isso **só funciona em blocos de até seis linhas quebradas**.
- **Desempenho:** não aplicar a tudo (`* { text-wrap: balance }`), por causa do limite de seis linhas e do custo no render; a sugestão é `h1` a `h6` e `blockquote`. Vantagem sobre as soluções em JavaScript: não é preciso esperar o carregamento das fontes.
- **Conflito com `white-space`:** um pede para não quebrar, o outro para quebrar equilibrado; desfazer o `white-space` (`white-space: unset`) deixa o equilíbrio agir.
- **A caixa não encolhe:** o `balance` muda só a quebra, não a largura do elemento; sobra espaço vazio no fim da caixa. Por isso, na opinião do autor, ele não fica tão bem em títulos dentro de cartões ou de caixas com borda ou sombra, onde o equilíbrio do texto desequilibra o contêiner.
- **Como o navegador faz:** uma busca binária pela menor largura que não acrescenta linhas, parando na precisão de um pixel de CSS (não de tela); para economizar passos, começa em 80% da largura média das linhas.
