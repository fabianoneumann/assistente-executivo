---
titulo: "text-box-trim CSS property (MDN)"
tipo: artigo
autor: "MDN contributors (Mozilla)"
url: "https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim"
publicado_em: 2026-09-16
capturado_em: 2026-10-29
licenca: "Texto em CC BY-SA 2.5 e exemplos de código em CC0 (LICENSE.md do repositório mdn/content)"
areas: [content-design]
tags: [css, typography, text-box-trim, vertical-rhythm, baseline, html-pieces]
---

Ficha de estudo em palavras próprias; o texto integral (licença CC BY-SA 2.5) não vem neste repositório e se lê na url do frontmatter. Página de referência do MDN; `publicado_em` é a data do último commit do arquivo no repositório `mdn/content`. O suporte dos navegadores vem dos dados de compatibilidade do MDN (`browser-compat-data`, consultados em 2026-10-29), que a página mostra numa tabela. Lido em 2026-10-29, na pesquisa sobre o layout das peças de tela fixa em HTML.

## O que é

Propriedade que corta o espaço acima e abaixo do texto dentro da caixa de um elemento de texto. Cada fonte guarda, na altura da linha, espaço para tudo (maiúsculas, hastes que sobem, que descem), e fontes diferentes no mesmo `font-size` dão caixas de altura diferente; o corte deixa o espaçamento vertical previsível.

## Valores

- `none` (padrão): não corta.
- `trim-start`: corta a borda de cima.
- `trim-end`: corta a borda de baixo.
- `trim-both`: corta as duas.

Quanto se corta é a outra propriedade, `text-box-edge`: por exemplo, `cap alphabetic` corta em cima no topo das maiúsculas e embaixo rente à linha de base. As duas juntas cabem no atalho `text-box` (ex.: `text-box: trim-both cap alphabetic`).

## Exemplos da página

- Dois parágrafos com `text-box-edge: cap alphabetic` e borda em cima e embaixo: com `trim-end`, só a borda de baixo encosta na linha de base; com `trim-both`, as duas encostam no texto.
- Um seletor interativo que troca os valores e mostra a declaração aplicada.

## Suporte (dados de compatibilidade do MDN, 2026-10-29)

Chrome e Edge desde a versão 133 (fevereiro de 2025), Safari desde a 18.2 (dezembro de 2024), Firefox desde a 154 (agosto de 2026). Não está marcada como experimental.

## O que a página não diz

Nada sobre assentar o texto numa grade de linhas fixa (ritmo vertical entre blocos); o corte é da caixa de um elemento, não do passo entre elementos.

---
