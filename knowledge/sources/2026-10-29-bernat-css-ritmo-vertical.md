---
titulo: "CSS & vertical rhythm for text, images, and tables"
tipo: artigo
autor: "Vincent Bernat"
url: "https://vincent.bernat.ch/en/blog/2026-css-vertical-rhythm"
publicado_em: 2026-04-22
capturado_em: 2026-10-29
licenca: "CC BY-SA 4.0 para o texto dos artigos (página de licenças do site, https://vincent.bernat.ch/en/licenses)"
areas: [content-design]
tags: [css, vertical-rhythm, baseline-grid, rlh, block-step, typography, html-pieces]
---

Ficha de estudo, em palavras próprias. A página de licenças do site põe o texto dos artigos do blog em CC BY-SA 4.0, então o texto integral cabia no arquivo; neste repositório ele não vem, e se lê na url do frontmatter. Artigo de blog de cinco minutos, de 22/04/2026, com versão em francês. Lido em 2026-10-29, na pesquisa sobre o layout das peças de tela fixa em HTML.

## A tese

Ritmo vertical é alinhar as linhas a um passo constante descendo a página. Com a unidade `rlh` do CSS, ficou fácil para o texto; ilustrações e tabelas quebram o passo e pedem solução própria. O autor parte de Bringhurst: títulos, citações, ilustrações e legendas são síncopes contra o ritmo do texto, e o texto principal deve voltar "precisely on beat and in phase" depois de cada uma.

## Estrutura

1. Abertura (o conceito e a citação de Bringhurst).
2. Texto.
3. Imagens responsivas.
4. Tabelas.
5. Fecho.

## Texto

- Três fatores governam o ritmo: tamanho da fonte, altura da linha e margem ou enchimento.
- Base de 18 px com altura de linha 1,5 (27 px), e margens e enchimentos zerados nos títulos, parágrafos e listas.
- `rlh` (do módulo CSS Values and Units 4) vale a altura de linha calculada do elemento raiz; segundo ele, todos os navegadores aceitam desde 2023. Com ele: títulos com `margin-top: 2rlh` e `margin-bottom: 1rlh`; o `h1` com `font-size: 2.5rem` e `line-height: 2rlh`; `h2` e `h3` maiores, mas com `line-height: 1rlh`; parágrafo, citação e código com `margin-top: 1rlh`; a nota lateral com fonte menor e `line-height: 1rlh`. A regra de fundo: toda altura de linha e todo espaço vertical é múltiplo inteiro do passo.
- Para navegador antigo, `calc(var(--line-height) * 2rem)` com a variável no `:root` (ele fez um plugin de PostCSS para isso).
- Arredondar a altura de linha de um título para o múltiplo seguinte do passo seria `calc(round(up, calc(2.4rem / 1rlh), 0) * 1rlh)`, mas o Firefox ainda não faz a aritmética com unidades que isso pede, e `round()` só existe nos navegadores desde 2024; ele resolveu também com PostCSS.
- Conferência visual: uma grade sobreposta ao conteúdo, por `body::after` com `linear-gradient` e `background-size: 20px 1rlh`, que ele liga e desliga com Ctrl+Shift+G.
- Um elemento em linha com fonte de métricas mais altas (código, tecla) estica a caixa da linha além do passo; a saída é `line-height: 1` nele: as letras transbordam, mas a linha não cresce.

## Imagens responsivas

A altura da imagem não é conhecida de antemão. O módulo CSS Rhythmic Sizing traz `block-step`, que ajusta a altura de um elemento a um múltiplo do passo, mas "most browsers don't support it yet". A solução dele é JavaScript: medir a altura, calcular o enchimento que leva ao múltiplo seguinte do passo (arredondar para cima e subtrair) e reparti-lo em cima e embaixo; um `ResizeObserver` refaz a conta quando a imagem muda de tamanho.

## Tabelas

Célula com 1 passo de altura fica apertada, com 2 desperdiça espaço. Ele usa entrelinha incremental: uma linha em cada cinco cai na grade (enchimento de 0,2 passo na célula e de 0,4 no cabeçalho). Para o que vem depois da tabela voltar ao passo, soma um enchimento embaixo, escolhido contando as linhas com `:has()` e `nth-child(5n…)` (cinco casos, de 0 a 0,8 passo); a alternativa é o mesmo JavaScript das imagens.

## Fecho

Nada disso é necessário, diz ele, mas depois que se vê, não se desvê; até os navegadores implementarem o Rhythmic Sizing, um pouco de CSS e de JavaScript basta.

## Tudo o mais que cita

O artigo de Paweł Grzybek sobre ritmo vertical com `lh` e `rlh`, o "Scale & Rhythm" de Iain Lamb, o mergulho de Vincent De Oliveira em métricas de fonte e `vertical-align`, a entrelinha incremental de Mark Boulton, os dados de suporte do webstatus.dev e o defeito do Firefox sobre aritmética com unidades. Não menciona `text-box-trim`.

---
