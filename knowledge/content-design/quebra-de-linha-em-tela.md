# Quebra de linha em tela: palavra sozinha, palavra presa e título por sentido

Onde a linha quebra num texto de tela fixa (Story, slide, carrossel, página renderizada como imagem): a palavra sozinha na última linha, a palavra curta no fim da linha, a quebra por sentido no título, o comprimento de linha, e o que o CSS faz sozinho no Chromium que renderiza as peças. Síntese de pesquisa rasa, revisada pela skill `review`, com uma medida própria no render. As regras que saem dela: `balance` e `pretty` no CSS da série, palavra curta presa nos títulos, destaques e citações, testes de quebra na rubrica de design e a ordem do que cede quando o texto não cabe.

> Fichas: [[2026-11-02-chrome-css-text-wrap-pretty]], [[2026-11-02-chrome-css-text-wrap-balance]]. Só citação: *Better typography with text-wrap pretty*, de Jen Simmons (WebKit), https://webkit.org/blog/16547/better-typography-with-text-wrap-pretty/; *Widow and orphan control (Butterick's Practical Typography)*, de Matthew Butterick, https://practicaltypography.com/widow-and-orphan-control.html; *Line length (Butterick's Practical Typography)*, de Matthew Butterick, https://practicaltypography.com/line-length.html; *Normas Editoriais (Editora UFG e Editora da Imprensa Universitária)*, de Editora UFG e Editora da Imprensa Universitária (Cegraf, Universidade Federal de Goiás), https://files.cercomp.ufg.br/weby/up/688/o/normas_gerais_inicio_julho17.pdf; *Manual de Produção Editorial da Embrapa, seção 44: Projeto Editorial, Projeto Gráfico e Diagramação*, de Embrapa, https://www.embrapa.br/en/manual-de-producao-editorial/projeto-editorial-projeto-grafico-e-diagramacao; *Effects of Chunking and Line Length on Reading Efficiency*, de Stacey A. Keenan (AT&T Bell Laboratories), https://journals.uc.edu/index.php/vl/article/view/5377; Dempsey, Christianson e Van Dyke (2025, https://link.springer.com/article/10.1007/s11145-025-10716-x). A base já tinha: [[texto-que-cabe-e-legibilidade]] (tamanhos, o que cede), [[carrossel-instagram]] (comprimento de linha) e [[principios-de-design-visual]] (alinhamento e contraste da Robin Williams).

## 1. O vocabulário

Os nomes do impresso não servem: "viúva" e "órfã" são, no Butterick e na Embrapa, linhas que ficam sozinhas no alto ou no pé de uma **página**; o Chrome chama de "orphan" a palavra sozinha no fim de um bloco ([[2026-11-02-chrome-css-text-wrap-pretty]]); as normas da Editora UFG chamam de viúva a linha "formada de apenas uma palavra monossílaba, ou parte de uma palavra". Por isso, aqui:

- **Palavra sozinha:** uma palavra só na última linha de um bloco.
- **Palavra presa:** a palavra curta ligada à seguinte por espaço inseparável, para a linha não terminar nela.

## 2. O que o CSS faz sozinho, medido no render

O shot-scraper 1.9.1 renderiza com o Chromium 151. A medida usou duas fontes carregadas, uma de corpo (Atkinson 34/48) e uma de título (Shantell 700 a 72 px), nas larguras de 850 px (uma coluna típica de série) e 920 px, em 80 começos cada vez maiores de um mesmo período (os casos se repetem em parte).

| | Corpo, 850 px | Título, 850 px |
|---|---|---|
| Palavra sozinha (comum / `pretty` / `balance`), textos de 2 a 6 linhas | 5 / 0 / 0 | 5 / 4 / 0 |
| A mesma, em todos os textos | 8 / 0 / 3 | 23 / 17 / 18 |
| Linhas (fora a última) terminando numa palavra curta da lista (comum / `pretty` / `balance` / presa) | 60 / 59 / 74 / 0 | 305 / 301 / 303 / 0 |
| `balance` age (2 a 6 linhas / 7 ou mais) | 45 de 47 / 0 de 28 | 18 de 18 / 0 de 62 |
| Muda o nº de linhas (`balance` / `pretty` / presa) | 0 / 0 / 0 | 0 / 0 / +1 em 34 (títulos de 5 a 24 linhas) |

- **`text-wrap: pretty`** tirou a palavra sozinha de todos os corpos da medida e não mexeu em mais nada; numa peça real, porém, deixou uma num corpo de três linhas: **reduz, não garante**, e a conferência da exportação avisa o que sobra. Em letra grande quase não age. No Chromium, desde o 117, mira por enquanto a palavra sozinha no fim do bloco e ajusta as linhas anteriores para isso; não trata a palavra sozinha no alto do bloco ("widow", na nota da página), e não é a propriedade `orphans` do CSS, que é do layout em colunas ([[2026-11-02-chrome-css-text-wrap-pretty]]). Segundo o WebKit, o Chromium olha só as últimas quatro linhas, e o Safari Technology Preview 216 olha o parágrafo inteiro e também acerta a borda irregular e a hifenização.
- **`text-wrap: balance`** deixa as linhas de comprimento parecido, sem acrescentar linha, e só age em blocos de até **seis linhas** (Chromium, desde o 114); a caixa mantém a largura e o texto fica mais estreito que ela ([[2026-11-02-chrome-css-text-wrap-balance]]). O post do WebKit diz "quatro linhas" para o Chromium; a medida e o Chrome dizem seis.
- **Nenhum dos dois prende a palavra curta.** Só o espaço inseparável zera a linha terminando em "de", "o", "a", e ele **custa linha** em parte dos blocos: +1 linha em 34 de 80 títulos a 850 px. Prender em todo texto fez uma tela de carrossel deixar de caber; prender só em título, destaque e citação não fez nenhuma deixar de caber (o teste mediu só o transbordo, não a altura). Num Story, um título ganhou uma linha ("um" preso a "projeto") e passou a cruzar uma seta desenhada à mão: conferir o desenho depois de prender.
- **No Instagram**, nada disso existe: a peça chega como imagem. Vale o navegador do render.

## 3. Palavra sozinha e palavra curta

- **Butterick:** a palavra curta sozinha na última linha sempre fica feia, e o remédio dele, na web, é o espaço inseparável com um pouco de programação; para a linha sozinha de página, admite editar o texto e desaconselha a quebra manual, sem dizer por quê. Leitura do assistente: a objeção costuma vir do texto que reflui numa largura variável; nas peças, a imagem se renderiza uma vez, numa largura fixa, e a quebra à mão não reflui.
- **Em português:** a regra escrita achada é a da Editora UFG, contra a palavra monossílaba sozinha numa linha; nenhum manual achado proíbe o monossílabo no **fim** da linha. O Perplexity diz que não há regra universal e recomenda evitar, sobretudo em título; o Gemini atribui a regra a Paulo Heitlinger e a Emanuel Araújo (*A construção do livro*), **não verificado**. A Embrapa manda tirar viúva, órfã e a hifenização da última linha da página.

## 4. Título por sentido

- **A regra prática** (Perplexity e Gemini, sem primária aberta, menos um item): não separar artigo e nome, preposição e o termo dela, nome e sobrenome, número e unidade de medida (este, também na UFG, que manda manter o número e a unidade sempre na mesma linha); quebrar depois de uma unidade de sentido; preferir duas linhas de comprimento parecido.
- **A evidência**, quase toda em inglês, em texto corrido, parte com crianças ou aprendizes da língua; nenhum estudo achado trata de título:
  - a favor: Dempsey, Christianson e Van Dyke (2025, só o resumo): quebra e recuo em cascata, em duas sessões de uma hora, deram menos releitura e compreensão melhor; **a empresa do formato pagou os participantes, e os dois autores que trabalham nela foram remunerados pelo papel no estudo**. Pelo resumo da busca, um estudo com 24 universitários (Trento) e um de frases ambíguas (*Language and Cognition*) acham leitura mais lenta quando a quebra corta uma unidade forte. Não verificados (Gemini): Walker et al. (2005 e 2007), Tate et al. (2019, efeito de 0,05), LeVasseur, Macaruso e Shankweiler (2006, em crianças), Jandreau e Bever (1992);
  - contra ou neutro: Keenan (1984): um sintagma por linha foi lido mais devagar, na tela e no papel, e a explicação dela é a variação do comprimento das linhas; o Perplexity resume que muitos estudos não acham vantagem de compreensão (não verificado).
- **Leitura (do assistente):** para o leitor adulto proficiente, o ganho de quebrar por sentido é pequeno ou nulo; o que a evidência sustenta é não cortar uma unidade forte e não fazer linhas muito desiguais. Num título de duas ou três linhas, dá para atender as duas coisas ao mesmo tempo, quebrando por sentido em linhas de comprimento parecido. O `balance` iguala as linhas mas não lê sentido ("Você estuda IA há / meses"); a quebra à mão resolve ("Você estuda IA / há meses e ainda / não construiu nada?").

## 5. Comprimento de linha

- Butterick: média de 45 a 90 caracteres com espaços, ou duas a três vezes o alfabeto, também para a web. Bringhurst, 45 a 75 com 66 ideal, e faixas para celular de 35 a 60: pelo Perplexity e pelo Gemini, **não verificado**.
- As fontes de mercado dizem 30 a 45 no carrossel ([[carrossel-instagram]]); uma coluna de 850 px com corpo de 34 px dá 47 a 54 caracteres por linha cheia. Leitura do assistente: a diferença se explica pelo volume de texto e pelo corpo (pouco texto, letra grande), não por página contra tela. **Desempate:** na série vale a coluna do design system, e os 30 a 45 de [[carrossel-instagram]] ficam superados para ela; mudar a coluna é decisão do design system.

## 6. O que vira regra

- **Série** (o design system da série, em `marketing/social-media/carousels/series/exemplo/`, seção "Quebra de linha", e o CSS dela): `balance` em título, destaque e citação; `pretty` em corpo, apoio, nota e lista; palavra curta presa (a, o, e, é, de, em, da, do, no, na, um, ao, à, os, as, se, por) nos títulos, destaques e citações; título por sentido, à mão quando o `balance` corta uma unidade.
- **Rubrica de design** (`marketing/social-media/rubrica-de-design.md`): palavra sozinha e palavra curta no fim de linha de título, destaque e citação em código, título por sentido em leitura; acabamento.
- **O que cede quando o texto não cabe** (atualiza a seção 1 de [[texto-que-cabe-e-legibilidade]]): primeiro o que não custa espaço (`balance`, `pretty`, título por sentido); depois posição e respiro; depois um degrau do corpo no papel inteiro, sem descer o título; abaixo do piso, alternativas com antes e depois. A palavra presa roda antes de medir, porque pode custar linha.
- **Alcance:** a regra vale para o que usa o CSS da série; peças avulsas e decks com CSS próprio precisam levá-la à parte.

## Não verificado

- As atribuições do Gemini (Heitlinger, Araújo, Walker, Tate, LeVasseur, Jandreau e Bever) e as faixas de comprimento de linha para celular.
- O estudo de Trento e o da *Language and Cognition*, só pelo resumo da busca.
- A medida é de um só período cortado em começos, numa fonte de corpo e numa de título; outros textos podem dar números diferentes.
