# Layout de peças de tela fixa em HTML

Como montar a tela de uma peça de tamanho fixo (Story de 1080×1920, slide de carrossel de 1080×1350, deck) em HTML e CSS: quando o flexbox, quando o grid, quando a posição absoluta, e o que o CSS novo de tipografia vertical faz por nós. A regra que sai daqui: o que se segue na tela vai em flexbox, o grid entra em dois casos e fica em posição absoluta o que tem lugar fixo. Esta página é a referência técnica por trás dela e mostra onde está o limite. O sistema visual da série fica no design system da série, em `marketing/social-media/carousels/series/exemplo/`; a área segura dos Stories, em [[carrossel-instagram]].

## O critério de escolha

O MDN dá duas perguntas ([[2026-10-29-mdn-grid-e-outros-metodos-de-layout]]):

- **Uma dimensão ou duas?** O flexbox controla uma linha **ou** uma coluna; o grid controla linhas **e** colunas ao mesmo tempo.
- **Do conteúdo para fora ou do layout para dentro?** No flexbox, o tamanho do conteúdo decide o espaço de cada item; no grid, primeiro se desenha a grade e depois se põem os itens nela. O sinal de troca: quando, no flexbox, se começa a desligar a flexibilidade (largura fixa num item para alinhar com o de cima), o caso é de grid.

A tela de uma peça é quase sempre uma coluna: título, texto, desenho, fecho, um embaixo do outro, com o conteúdo decidindo a altura de cada um. É o caso do flexbox: uma `.coluna` com `display:flex; flex-direction:column` e espaçadores (`.respiro`) entre os grupos.

## Flexbox por padrão, inclusive na tela cheia de texto

A tentação é montar a tela cheia de texto com posição fixa e medir os blocos por script. A experiência mostra que o flexbox serve à tela cheia; o que costuma estourar é a conta de assentamento que o design system faz sobre a coluna, quando ele alinha o texto a linhas de um papel quadriculado ou pautado. Um exemplo dessa conta:

1. Com um passo de coluna grosso (por exemplo, uma linha forte a cada 120 px), **cada respiro começa com uma faixa inteira** (`flex: 0 0 120px`), para o encaixe que sobe nunca encostar um bloco no outro.
2. A primeira linha de texto de cada bloco (menos o primeiro, que só desce) vai para a linha grossa **mais próxima**, subindo ou descendo até meio passo; as linhas de dentro do bloco descem para a linha fina seguinte.
3. O espaço que sobra entre o pé do último bloco e o pé da coluna vira faixas inteiras, repartidas entre os respiros na proporção de um peso. Se o que sobra é negativo, a tela transborda.

Numa tela de Story com 16 faixas de 120 px, cinco blocos têm quatro respiros: são 480 px de espaço mínimo antes de qualquer texto, mais o arredondamento de cada começo de bloco. É isso que não cabe na tela cheia. O "respiro de peso 0 que sai igual ao de peso 1" é a mesma conta vista do outro lado: o peso só reparte o que sobra, e a faixa mínima é de todos.

**A saída:** quando a coluna transborda no passo grosso, desfazer o assentamento e refazer a conta no passo fino do papel, que deixa respiros menores; só acusar o transbordo se nem assim couber, e marcar na coluna o passo usado. O preço: nessa tela, o começo dos blocos assenta na linha fina, e não na grossa que o olho lê.

## Quando o grid

Dentro de uma coluna em flexbox, um bloco pode ser um grid, em dois casos:

- **Texto e desenho lado a lado, começando na mesma linha.** São duas dimensões: o desenho numa coluna, o texto na outra, alinhados entre si. Um grid de duas colunas (`grid-template-columns`) alinha os dois sem largura fixa em cada item, que seria o sinal de troca do MDN.
- **Anotação empilhada sobre o desenho.** O par pai `position: relative` e filhos `position: absolute` sobrepõe os elementos, mas tira os filhos do fluxo e deixa o pai sem altura. Com o pai em grid de uma célula e cada filho em `grid-area: 1 / 1` (o mesmo que `grid-row-start: 1; grid-column-start: 1`), os filhos se sobrepõem e continuam no fluxo: o pai fica com a altura do maior, e o conjunto anda com a coluna (*Overlap Elements With CSS Grid Instead Of Position Absolute*, de Rik Schennink (PQINA), https://www.pqina.nl/blog/css-grid-position-absolute-alternative/). A ordem de pintura é a do HTML. Para deslocar a anotação dentro da célula, o MDN mostra o meio-termo: a área da grade com `position: relative` vira a referência de um filho absoluto, e `top` e `left` deslocam dentro dela ([[2026-10-29-mdn-grid-e-outros-metodos-de-layout]]).

Dois cuidados. Se o design system assenta toda linha de texto (`p`, `li`, `h1` a `h3`) que está dentro da coluna, a anotação empilhada precisa de uma marca (como `data-livre`) para não ser empurrada para a linha do papel. E o espaço de uma anotação desenhada à mão se mede pela linha desenhada, que passa uns 40 px fora da caixa do texto. A anotação empilhada **sobre** o desenho vai em grid; as anotações **em volta** de um desenho continuam em posição absoluta.

## Quando a posição absoluta

Fica em posição absoluta o que é **ancorado na tela**, e não no conteúdo: o que deve ficar no mesmo lugar se o texto crescer ou encolher.

- A moldura: a assinatura e a arroba a 40 px do pé, a paginação a 40 px do topo.
- O espaço do cartão de resposta nos Stories (de ~260 a ~700 px) e o lugar dos adesivos, nas posições medidas no app (`marketing/social-media/stories/README.md`).
- O que se sobrepõe de propósito e não acompanha o texto: a folha que espia, a fita, a foto colada.
- As telas de composição (capa, diagrama, tela final), em que cada peça tem lugar próprio.

O teste prático: se o texto da tela mudar, isso deve ficar onde está? Se sim, é absoluto; se deve andar junto, é fluxo.

## O CSS novo de tipografia vertical

| Recurso | O que faz | Suporte (fim de 2026) | Por que não resolve o assentamento em linha de papel |
|---|---|---|---|
| `text-box-trim` com `text-box-edge` | Corta o espaço acima e abaixo do texto na caixa do elemento, por exemplo até o topo das maiúsculas e rente à linha de base (`text-box: trim-both cap alphabetic`) ([[2026-10-29-mdn-text-box-trim]]) | Chrome e Edge 133, Safari 18.2, Firefox 154 | Torna a caixa previsível, mas não põe a linha de base numa linha do papel: a linha do papel está numa posição da página, e onde o bloco cai depende de tudo o que vem antes. O script de assentamento mede a linha de base com uma sonda e continuaria medindo |
| `text-fit` | Muda o tamanho desenhado da fonte para o texto encher a largura da caixa (`grow`) ou caber nela (`shrink`), com limite em porcentagem; não muda o `font-size` calculado nem a altura de linha ([[2026-10-29-mdn-text-fit]], [[2026-10-29-chrome-150-novidades]]) | Chrome e Edge 150; Firefox e Safari, não; experimental | Age na largura, e o estouro típico é na altura. Com várias linhas, a quebra vence o `shrink`. E uma escala de tipos fixa (por exemplo 72, 52, 34 px) não prevê tamanho que muda por tela: seria uma regra nova do design system |
| `rlh` | Unidade igual à altura de linha do elemento raiz; Bernat monta o ritmo vertical do texto com margens e alturas em múltiplos de `1rlh` ([[2026-10-29-bernat-css-ritmo-vertical]]) | Todos os navegadores desde 2023 | O passo do papel já faz esse papel em px. O ritmo do Bernat alinha as caixas de linha; o assentamento alinha a linha de base, e duas fontes diferentes põem a linha de base em alturas diferentes dentro da mesma caixa |
| `block-step` | Arredonda a altura de um bloco para um múltiplo do passo, escolhendo onde pôr o espaço e para que lado arredondar; `line-height-step` faz o mesmo com a altura de cada linha | Rascunho do W3C (CSS Rhythmic Sizing, Working Draft de 17/02/2026); fora dos dados de compatibilidade do MDN; "most browsers don't support it yet" (Bernat, abril de 2026) | Seria o respiro em faixas inteiras feito pelo navegador, mas não existe nos navegadores, e também arredonda altura sem assentar linha de base |

O exportador da skill `slides-export` (shot-scraper sobre o Playwright, com Chromium recente) já entende `text-box-trim` e `text-fit`; a prévia aberta no navegador de quem revisa depende do navegador.

## Correção: o Satori aceita grid

O Satori, da Vercel, gera SVG a partir de HTML e CSS sem navegador. Há material circulando que diz que ele só aceita flexbox; o README da versão 0.63.2 diz que o layout é feito pelo Taffy, para flexbox, **grid** e bloco, e lista como aceitos `gridTemplateColumns`, `gridTemplateRows` (menos `subgrid` e `masonry`), `gridTemplateAreas`, `gridArea` e os demais ([[2026-10-29-satori-readme]]). A informação antiga é do tempo em que o motor era o Yoga. Vale como ressalva: as peças saem do navegador, não do Satori; se um dia a imagem sair sem navegador, ele arredonda a altura de linha para pixel inteiro e ignora o que não está na tabela, como `text-box-trim` e `text-fit`.

## Fontes

- **Fichas:** [[2026-10-29-mdn-grid-e-outros-metodos-de-layout]], [[2026-10-29-mdn-text-box-trim]], [[2026-10-29-mdn-text-fit]], [[2026-10-29-chrome-150-novidades]], [[2026-10-29-satori-readme]], [[2026-10-29-bernat-css-ritmo-vertical]].
- **Só citação:** *Overlap Elements With CSS Grid Instead Of Position Absolute*, de Rik Schennink (PQINA), https://www.pqina.nl/blog/css-grid-position-absolute-alternative/; W3C, CSS Rhythmic Sizing Module Level 1, Working Draft de 17/02/2026 (Koji Ishii e Elika J. Etemad), https://www.w3.org/TR/css-rhythm-1/ (define `block-step-size`, `block-step-insert`, `block-step-align`, `block-step-round`, o atalho `block-step` e `line-height-step`).
- **Suporte dos navegadores:** dados de compatibilidade do MDN (`browser-compat-data`).
