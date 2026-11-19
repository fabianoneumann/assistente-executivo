---
titulo: "text-fit CSS property (MDN)"
tipo: artigo
autor: "MDN contributors (Mozilla)"
url: "https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit"
publicado_em: 2026-09-29
capturado_em: 2026-10-29
licenca: "Texto em CC BY-SA 2.5 e exemplos de código em CC0 (LICENSE.md do repositório mdn/content)"
areas: [content-design]
tags: [css, typography, text-fit, fit-text, html-pieces, accessibility]
---

Ficha de estudo em palavras próprias; o texto integral (licença CC BY-SA 2.5) não vem neste repositório e se lê na url do frontmatter. Página de referência do MDN, marcada como experimental; `publicado_em` é a data do último commit do arquivo no repositório `mdn/content`. O suporte dos navegadores vem dos dados de compatibilidade do MDN (`browser-compat-data`, consultados em 2026-10-29). Lido em 2026-10-29, na pesquisa sobre o layout das peças de tela fixa em HTML; a estreia no Chrome 150 está em [[2026-10-29-chrome-150-novidades]].

## O que é

Propriedade que muda o tamanho **desenhado** da fonte para o texto caber exatamente na largura da caixa que o contém, com um limite opcional. Resolve o problema clássico do título que deve encher a largura, antes feito com conta de `font-size` ou JavaScript. Ela age na largura (a direção da linha), não na altura.

## Valores

- Primeiro (obrigatório): `none` (padrão), `grow` (aumenta até caber) ou `shrink` (diminui até caber).
- Segundo (opcional), para texto de várias linhas: `consistent` (padrão: todas as linhas com o mesmo fator, o menor entre elas), `per-line` (cada linha com o seu fator, menos a última e as que terminam em quebra forçada) ou `per-line-all` (cada linha com o seu, inclusive a última).
- Último (opcional), uma porcentagem: o máximo com `grow` (100% ou mais; ex.: `grow 300%`) ou o mínimo com `shrink` (de 0% a 100%; ex.: `shrink 80%`).

## Como funciona

- O fator de cada linha é, mais ou menos, (A + B) / A, em que A é a largura das partes que escalam (o texto, sem o espaço final, e espaçamentos proporcionais à fonte) e B é o espaço que sobra (negativo se o texto transborda). Borda, margem e enchimento em linha não escalam. O método exato pode variar entre navegadores.
- Não muda o tamanho intrínseco do contêiner: num contêiner que se ajusta ao conteúdo (`fit-content`), o texto não tem para onde crescer.
- Não muda o `font-size` calculado: o ajuste vem depois, na hora de desenhar.
- Com `shrink`, a quebra de linha costuma vencer (as palavras descem para a linha seguinte em vez de encolher); para ver o efeito, é preciso `white-space: nowrap`.

## Acessibilidade

A página pede testar em vários tamanhos de tela para o texto não ficar pequeno nem grande demais, e lembra o critério 1.4.4 da WCAG (redimensionar o texto sem perder conteúdo).

## Exemplos da página

Um `h1` com `grow` que enche a largura, um `h2` com `nowrap` e `shrink` que encolhe em vez de transbordar; os mesmos com limites (`grow 300%`, `shrink 80%`) e uma consulta de contêiner que volta a quebrar a linha abaixo de 400 px; três parágrafos comparando `consistent`, `per-line` e `per-line-all`.

## Suporte (dados de compatibilidade do MDN, 2026-10-29)

Chrome, Edge e Chrome para Android desde a versão 150 (junho e julho de 2026). Firefox e Safari, não. Experimental.

---
