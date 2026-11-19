# Texto que cabe e legibilidade no celular

O que cede quando o texto não cabe numa tela de tamanho fixo, em que ordem, e qual tamanho de texto ainda se lê numa imagem de 1080 px vista no celular. Refinado para um design system de série em que a entrelinha é múltipla de um passo fixo (uma grade de linha de base, como as linhas de um caderno), que é o caso mais restritivo; o design system da série do projeto fica em `marketing/social-media/carousels/series/exemplo/`. Síntese analítica de duas pesquisas. Os números de piso (30 px no corpo, 28 no rótulo, texto grande a partir de 52 px em negrito ou 66 regular) são os que a `marketing/social-media/rubrica-de-design.md`, a régua de forma, pode adotar; o design system da série muda por decisão de quem o mantém, registrada nele.

> Fontes raw: [[2026-10-29-printwiki-copyfitting]], [[2026-10-29-godfrey-copyfitting-indesign]], [[2026-10-29-orshot-text-autofit]], [[2026-10-29-microsoft-publisher-copyfitting]], [[2026-10-29-contentdrips-tamanho-de-carrossel]], [[2026-10-29-umb-graficos-para-redes-acessiveis]], [[2026-10-29-rocketship-texto-em-video-vertical]], [[2026-10-29-w3c-wcag22-contraste-minimo]], [[2026-10-29-readability-matters-bake-off]]. Só citação: Legge e Bigelow (2011), Atilgan et al. (PNAS, 2020), Bababekova et al. (2011), Apple HIG, CreativePro, Canva e CHILI, com a URL onde aparecem.

## 1. O que cede quando o texto não cabe

### O que o impresso e as ferramentas fazem

- **O verbete clássico** põe o corte do texto antes de tudo: só "se cortar não for possível" mudam o corpo, a entrelinha ou a letra; na composição automática, também a redução do espaço entre letras ([[2026-10-29-printwiki-copyfitting]]).
- **O designer de impresso** vai do menos ao mais visível: espaço entre letras até -20, quebra manual, hifenização, pedir corte ao redator, escala horizontal de 97% a 103%, largura da coluna, corpo, alinhamento e, por último, a letra. Toda mudança vale para o conjunto (o parágrafo, todas as colunas, todo o texto corrido), para nenhuma parte destoar ([[2026-10-29-godfrey-copyfitting-indesign]]).
- **O CHILI** (composição automática de peças) faz nesta ordem: compacta (reduz entrelinha e espaçamento), depois escala a letra, depois volta a abrir entrelinha e espaçamento; tem corpo mínimo e máximo em porcentagem, limite de linhas e uma opção em que as caixas do mesmo estilo se comportam como grupo, todas com a redução da que mais precisou (https://chilipublishdocs.atlassian.net/wiki/spaces/CPDOC/pages/1412115/CopyFitting).
- **A CreativePro** relata um caso em que o espaço entre letras sozinho deixou o texto ilegível e a solução combinou corpo, entrelinha, espaço entre palavras de 100% para 90% e a escala de glifo (https://creativepro.com/?p=14582, só pelo resumo da busca; a página recusou o acesso).
- **O ajuste automático** das ferramentas de modelo encolhe o corpo sem piso que proteja a leitura: o Publisher reduz até caber ([[2026-10-29-microsoft-publisher-copyfitting]]); o Orshot desce até 8 px por padrão, e as alternativas dele são cortar com reticências ou levar o resto para outra página ([[2026-10-29-orshot-text-autofit]]). No Canva, arrastar a lateral da caixa muda a largura e mantém o corpo; o canto escala os dois (https://www.canva.com/help/wrap-text/, só pelo resumo da busca).
- **No carrossel**, a recomendação de mercado é cortar o texto, não o tamanho, ou dividir em dois slides ([[2026-10-29-contentdrips-tamanho-de-carrossel]]).

### Por que a ordem do impresso não serve como está

- **A entrelinha não cede.** Num sistema em que toda entrelinha é múltiplo do passo do papel (por exemplo, 48 px no corpo) e o texto assenta nas linhas, compactar a entrelinha, o primeiro passo do CHILI, tira o texto da grade.
- **Reduzir o corpo só ganha altura se o bloco perder uma linha.** Com a entrelinha presa em 48, um parágrafo de quatro linhas a 34 px ocupa o mesmo que a 30 px, se continuar em quatro linhas. O degrau de corpo só serve quando faz algum bloco cair uma linha inteira (48 px a menos por linha perdida). Consequência do sistema, conta do assistente.
- **Apertar letra e distorcer ficam fora.** Uma letra como a Atkinson Hyperlegible se escolhe por distinguir bem as letras, e no teste de relance as letras de forma aberta venceram as de espaçamento apertado e forma fechada ([[2026-10-29-readability-matters-bake-off]]); apertar espaço ou escalar a letra vai no sentido contrário. Inferência do assistente, sem teste próprio.
- **Prefira o sinal ao encolhimento:** o código da série marca a tela que transborda em vez de reduzir sozinho, o oposto do ajuste automático do Publisher e do Orshot.

### A ordem proposta para a série

1. **O que não custa espaço.** `text-wrap: balance` nos blocos curtos e `pretty` no corpo (no CSS da série), e o título quebrado por sentido, à mão quando o `balance` corta uma unidade. Nenhum dos dois muda o número de linhas ([[quebra-de-linha-em-tela]]). A palavra curta presa, que pode custar linha, roda antes de medir, e a contagem de linhas confere depois.
2. **Posição e respiro entre blocos.** Sem trocar palavra nem tamanho: mover blocos (medidos por script) e reduzir o respiro entre blocos até o mínimo de um passo. O respiro de dentro do bloco (a entrelinha) não entra.
3. **Um degrau do corpo, no papel inteiro da tela, até o piso, e só se algum bloco perder uma quebra de linha; o título não desce** (o degrau do título não costuma ganhar linha). O papel inteiro desce junto (todo texto de corpo daquela tela), para manter "um tamanho por papel em cada tela"; o degrau é de 34 para 32 ou 30, nunca abaixo do piso (seção 2). Testável em código: renderizar nos dois corpos e contar as linhas de cada bloco; se nenhum bloco perde linha, o degrau não ajuda e não entra.
4. **Abaixo do piso, não se encolhe: mostram-se alternativas com antes e depois**, para quem pede escolher: cortar palavra (o texto aprovado só muda com quem o aprovou), dividir em duas telas (o equivalente do modo Flow) ou mover o trecho para a legenda (o mesmo movimento que a UMB usa quando o contraste não tem conserto, [[2026-10-29-umb-graficos-para-redes-acessiveis]]).

## 2. Legibilidade no celular

### Da imagem de 1080 para a tela

- O feed e o Stories mostram a imagem na largura do celular. Num iPhone de 6,1 polegadas (393 pt de largura) são **2,75 px da imagem por ponto**; num de 6,7 (430 pt), **2,51**. Em celulares mais estreitos (360 a 375 pt) chega perto de 3, o "um terço" do Contentdrips ([[2026-10-29-contentdrips-tamanho-de-carrossel]]). Faixa de trabalho: **cerca de 2,5 a 2,8 px por ponto**. Conta do assistente, pelas larguras de tela; o ponto do iOS equivale ao px do CSS, a unidade do WCAG.
- O vídeo vertical de 1080 × 1920 tem a mesma largura, então os números de vídeo valem na mesma escala: gancho de 60 a 72 px, apoio de 40 a 48, legenda falada de 32 a 36 e nada importante menor ([[2026-10-29-rocketship-texto-em-video-vertical]]).

### O limite da visão

- **Tamanho crítico de impressão:** abaixo de cerca de **0,2° de altura-x** a velocidade de leitura cai rápido; acima, fica no máximo até uns 2°. O valor varia de 0,15° a 0,3° conforme a pessoa e a letra (Legge e Bigelow, 2011, https://pmc.ncbi.nlm.nih.gov/articles/PMC3428264/).
- **Caracteres por linha:** a leitura plena também pede umas 13 letras por linha, o que limita telas pequenas com letra grande (Atilgan et al., 2020, https://www.pnas.org/doi/10.1073/pnas.2007514117); as linhas de 30 a 45 caracteres da base estão longe desse limite.
- **Distância:** as pessoas seguram o celular a cerca de 36 cm para mensagem e 32 cm para internet, mais perto que os 40 cm do papel (Bababekova et al., 2011, https://pubmed.ncbi.nlm.nih.gov/21499163/).
- **Referência de sistema:** no iOS, o corpo padrão é 17 pt e o mínimo 11 pt (Apple HIG, https://developer.apple.com/design/human-interface-guidelines/typography), ou cerca de 43 a 48 px e 28 a 31 px numa imagem de 1080.

### A conta, papel a papel

Para uma letra como a Atkinson Hyperlegible ou a Shantell Sans, a altura-x é cerca de metade do corpo (0,49 a 0,51, lido nas métricas dos arquivos da Google Fonts). Com isso, a 32 a 36 cm:

| Na imagem | Na tela | Altura-x em graus | Leitura |
|---|---|---|---|
| 26 px | 9,5 a 10,4 pt | 0,12 a 0,15° | abaixo do mínimo do iOS |
| 30 px | 11 a 12 pt | 0,14 a 0,18° | na beira de baixo do tamanho crítico |
| 34 px | 12,4 a 13,5 pt | 0,16 a 0,20° | perto do tamanho crítico |
| 40 px | 14,6 a 16 pt | 0,19 a 0,23° | no tamanho crítico ou acima |
| 42 px | 15,3 a 16,7 pt | 0,20 a 0,24° | acima dele |

**Faixas propostas, conta do assistente a conferir com print num celular real:**

- **Corpo:** de **34 a 42 px** o ideal, **piso de 30** (cerca de 11 pt, o mínimo do iOS). O mercado dá corpo de 28 a 36 com piso de 28 ([[2026-10-29-contentdrips-tamanho-de-carrossel]]).
- **Nota manuscrita** (letra manuscrita de peso regular): **38 a 40 px**. Letra manuscrita ou fina pede tamanho maior: a UMB manda somar de 8 a 12 pontos do editor ([[2026-10-29-umb-graficos-para-redes-acessiveis]]); levar isso para esta escala é leitura do assistente.
- **Rótulo** (moldura, fonte de número, paginação, @): **28 a 30 px**, no mínimo do iOS. O mercado aceita de 20 a 26 ([[2026-10-29-contentdrips-tamanho-de-carrossel]]); a UMB põe o secundário em 24 a 28 pontos do Canva, sem dizer em que tamanho de arte.
- **Texto grande do WCAG, o que aceita 3:1:** 18 pt (24 px do CSS) ou 14 pt em negrito (cerca de 18,5 px), medidos na entrega, sem zoom ([[2026-10-29-w3c-wcag22-contraste-minimo]]). Nesta escala começa em **cerca de 52 px em negrito ou 66 regular** (47 a 52 e 60 a 66, conforme o celular; vale o lado alto). Abaixo disso, 4,5:1. Exemplo: um título de 72 px em negrito é grande; um destaque de 52 px num peso abaixo do negrito pleno fica no limite e vai a 4,5:1; uma chamada de 46 px também. A UMB nem usa a exceção nas redes.

**Como conferir:** print do feed num celular de 393 pt e num de 430 pt, medir a altura-x em pixels da tela e olhar com o braço esticado; se precisar apertar os olhos, está pequeno ([[2026-10-29-umb-graficos-para-redes-acessiveis]], [[2026-10-29-rocketship-texto-em-video-vertical]]).

## 3. Contradições

1. **Piso de 22 contra 28 a 30.** A síntese de áreas seguras ([[carrossel-instagram]]) dá corpo de 24 a 32 com mínimo de 22 e rótulo de 16 a 22. A base nova sustenta piso de 30 no corpo e 28 no rótulo (o mercado em 28, o mínimo do iOS em cerca de 28 a 31 px, e a conta do tamanho crítico).
2. **Reduzir numa tela contra o mesmo tratamento em todas.** "Um tamanho por papel em cada tela" admite tamanhos diferentes entre telas; "o mesmo tratamento para o mesmo elemento em todas as telas" não. A regra antiga diz que, se precisa encolher, há texto demais ("corte palavra, não fonte"), mas ajuste de forma não troca palavra aprovada sem quem a aprovou. As fontes apontam para o conjunto: o designer reduz todo o texto corrido ([[2026-10-29-godfrey-copyfitting-indesign]]), o CHILI aplica a maior redução ao grupo, e o "melhor ajuste" do Publisher, caixa a caixa, é o que gera a inconsistência. Três saídas: o degrau só na tela, assumido como acabamento; o degrau na peça inteira; ou nunca reduzir, só as alternativas da etapa 4. A ordem proposta acima escolhe a primeira, com o degrau descendo o papel inteiro naquela tela.
3. **Contraste de título.** Aceitar 3:1 em título de 40 px numa tela de 1080 é frouxo: nesta escala, o texto grande do WCAG começa em cerca de 52 px em negrito ou 66 regular, e 40 px pede 4,5:1.
4. **Margem.** O Contentdrips põe o essencial a 150 a 200 px das bordas; é comum usar de 80 a 130 px nas laterais. Sem medida que desempate; registrado, não resolvido.

## Elos

- Medidas de carrossel e área segura: [[carrossel-instagram]]. Quebra de linha: [[quebra-de-linha-em-tela]]. Régua de forma: `marketing/social-media/rubrica-de-design.md`. Sistema da série: o design system em `marketing/social-media/carousels/series/exemplo/` (papéis, grade, coluna).

## Não verificado

- **As faixas por papel e a conversão** são conta do assistente: larguras de tela da Apple, métricas de altura-x dos arquivos de letra e as distâncias de 2011 (celulares menores que os de hoje); falta o print num celular real. Android (360 a 412 de largura) dá de 2,6 a 3 px por ponto, não medido.
- **O tamanho crítico** foi medido em papel e em laboratório; aplicar ao feed, rolando, é extrapolação.
- **CreativePro e Canva** recusaram o acesso (403); o que está aqui vem do resumo da busca. A ordem do CHILI foi conferida na página.
- **Os pontos do Canva** da UMB não dizem o tamanho da arte; não se convertem em pixel daqui.
- **O peso 600** como negrito para o WCAG: o documento fala só em "bold"; tratado como abaixo do negrito, por cautela.
- **Que apertar a letra pese mais na Atkinson** é inferência a partir de um resumo secundário sobre outra situação (leitura de relance ao dirigir).
