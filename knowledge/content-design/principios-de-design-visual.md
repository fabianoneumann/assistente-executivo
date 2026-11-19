# Princípios de design visual: os quatro da Robin Williams e o que a NN/g acrescenta

Os nomes para ver e consertar o defeito de uma tela: proximidade, alinhamento, repetição e contraste (Robin Williams), mais escala, hierarquia e equilíbrio (Nielsen Norman Group). Da pesquisa feita para pôr desenhos de enfeite numa sequência de Stories, refeita com o livro inteiro (3ª edição) lido direto, exemplos incluídos. O livro é de impressos e os artigos da NN/g são de interface; nenhuma das três fontes trata de peça de rede social, e a aplicação a ela é leitura nossa, marcada como tal. Medidas (tamanho de texto, área segura) ficam em [[texto-que-cabe-e-legibilidade]] e [[carrossel-instagram]]; como montar a tela em HTML, em [[layout-de-pecas-em-html]]; o sistema visual da série, no design system dela, em `marketing/social-media/carousels/series/exemplo/`.

## Por que nomear

A tese de abertura do livro é a da iúca: ela ganhou um guia de árvores, aprendeu a reconhecer a primeira, e passou a vê-la em quatro das seis casas da própria rua, onde morava havia treze anos. O que não tem nome não se vê; uma página que "parece errada" quase sempre fere pelo menos um dos quatro princípios, e quem os nomeia sabe onde mexer (*Design para quem não é designer (The Non-Designer's Design Book), 3ª edição: o livro inteiro, com os exemplos*, de Robin Williams (https://www.peachpit.com/store/non-designers-design-book-9780321534040)). É o mesmo uso que as rubricas fazem: transformar "não gostei" em um defeito com nome.

## Os quatro princípios

Ordem do livro: proximidade, alinhamento, repetição, contraste. Ela não escreve a sigla: depois da lista, na ordem contraste, repetição, alinhamento, proximidade, vem um "Umm..." e a admissão de que há uma sigla fácil de lembrar, mas imprópria, com um pedido de desculpas; o leitor monta C.R.A.P. A tradução em português mantém a nota (p. 13). Cada capítulo fecha com finalidade, como conseguir e o que evitar (*Design para quem não é designer (The Non-Designer's Design Book), 3ª edição: o livro inteiro, com os exemplos*, de Robin Williams (https://www.peachpit.com/store/non-designers-design-book-9780321534040)).

**Proximidade.** O que se relaciona fica junto e vira uma unidade visual; o que não se relaciona fica longe. A finalidade é **organizar**. Como conferir: apertar os olhos e contar quantas vezes o olho para; mais de três a cinco paradas pede juntar. Evitar: muitos elementos soltos; o mesmo espaço entre todos os elementos; aproximar o que não tem relação; pôr coisa no canto ou no meio só porque o espaço está vazio; deixar o leitor com qualquer dúvida sobre a que pertence um título, uma legenda ou uma imagem. O espaço vazio arrumado é consequência da organização, não enfeite à parte.

A NN/g dá a base perceptiva ([[2026-10-30-nngroup-proximidade-gestalt]]): a proximidade **vence** a semelhança de cor e de forma (uma grade de círculos e triângulos com um espaço maior no meio é lida como dois grupos mistos); o espaço em branco é o instrumento do agrupamento; o item afastado do grupo a que pertence é lido como sem relação e, por quem está focado, nem é visto (o "Pular" num canto, longe dos botões); e quando o layout encolhe ou empilha, o que estava junto se separa.

**Alinhamento.** Nada vai para a página por acaso: todo elemento tem ligação visual com outro, por uma linha invisível. A finalidade é **unificar**. Achar uma linha forte e usá-la: a borda alinhada à esquerda ou à direita é firme, o centralizado tem duas bordas moles e muitas vezes parece fraco. Evitar: mais de um alinhamento de texto na mesma tela; o centralizado por omissão (centralizar pode, se for escolha); o espaço em branco preso entre elementos, sem saída para a margem.

**Repetição.** Repetir algum aspecto (fonte, fio, cor, marcador, forma, relação de espaço) pela peça inteira, empurrando a consistência que já existe até ela virar chave visual. A finalidade é **unificar e dar interesse**. Do capítulo: dá para acrescentar um elemento só para repetir, inclusive um que não tem a ver com o assunto (petróglifos num formulário, pássaros num relatório), em tamanhos e **ângulos** variados, desde que pareça intencional e não aleatório; os itens repetidos não precisam ser idênticos, basta a ligação ser clara; com a estrutura de baixo firme (alinhamentos, formato), os elementos de cima podem ser mais livres; a surpresa só se destaca sobre um fundo consistente. Evitar: repetir até cansar, como o vestido preto com todos os acessórios vermelhos.

**Contraste.** Se dois itens não são iguais, torná-los **muito** diferentes; meio diferente é conflito e parece engano (12 pontos contra 14, fio de meio ponto contra fio de um ponto, marrom-escuro contra preto não são contraste). A analogia dela é o retoque de parede: ou a cor é exatamente a mesma, ou se pinta a parede inteira. A finalidade é **criar interesse e organizar** a ordem de leitura. Começar decidindo o ponto focal, o que se vê primeiro. Contrasta-se por tamanho, peso, cor, forma, direção, espaço. "Don't be a wimp": diferença pequena não é contraste.

## O que a NN/g acrescenta: escala e equilíbrio

Do artigo dos cinco princípios ([[2026-10-30-nngroup-cinco-principios-de-design-visual]]), regras de bolso da autora, sem estudo citado:

- **Escala:** no máximo **três tamanhos**; o mais importante é o maior; ter pequeno, médio e grande.
- **Hierarquia:** escala, valor, cor, espaço e posição dão a ordem de leitura; elementos parecidos demais obrigam a ler tudo.
- **Equilíbrio:** o peso visual conta pela **área** ocupada, não pelo número de elementos. Simétrico é quieto; **assimétrico é dinâmico**; radial puxa para o centro. Escolher pelo que se quer transmitir.
- **Contraste de cor:** baixar o contraste do texto para tirar ênfase prejudica a leitura e a acessibilidade.

## O que o livro inteiro acrescenta

Da leitura direta da 3ª edição, com os exemplos de antes e depois (*Design para quem não é designer (The Non-Designer's Design Book), 3ª edição: o livro inteiro, com os exemplos*, de Robin Williams (https://www.peachpit.com/store/non-designers-design-book-9780321534040)):

- **Revisão (cap. 6): "Don't be a wimp".** Não ter medo de espaço vazio, de assimetria, de tirar do centro, de palavra muito grande ou muito pequena. O capítulo refaz uma capa aplicando os princípios um de cada vez, começando pela proximidade, porque sem o espaçamento certo os outros não adiantam.
- **Limpar antes de compor:** o primeiro passo do Quiz #2 tira rótulos óbvios, caixas, maiúsculas corridas e enfeites que só enchem cantos.
- **Alinhamento com imagem:** a borda da imagem conta como linha de alinhamento; com alinhamentos fortes, romper um de propósito parece escolha, desde que se rompa de vez. Imagem pode crescer e sangrar a borda quando tem propósito.
- **Repetir um pedaço:** um motivo pequeno tirado de uma ilustração, espalhado em tamanhos e direções, amarra várias peças; quando a imagem já é conhecida, uma parte cortada pela borda basta.
- **Cor (cap. 7):** quente em pouca área chama o olho, fria precisa de área maior; contraste de tom pesa mais que de matiz (testar em escala de cinza); a cor de destaque pode vir de uma imagem da própria peça.
- **Tipografia (caps. 9 a 11):** duas fontes se relacionam por concordância, conflito ou contraste, e o conflito (parecidas, mas não iguais) é o que falha; nunca duas fontes da mesma categoria na mesma página; seis caminhos de contraste entre letras: tamanho, peso, estrutura, forma (caixa alta contra baixa, roman contra itálico), direção e cor. Quando duas linhas "não casam", perguntar o que elas têm de **igual**.
- **Caixa-baixa** no título permite corpo e peso maiores no mesmo espaço; maiúsculas corridas pesam e cansam.
- **Dicas por peça (cap. 8):** cartão, papel de carta, folheto, informativo, brochura, cartão-postal, anúncio e site, cada um com o seu ponto focal e as suas armadilhas; o pacote de uma marca se reconhece pela repetição de uma dupla de fontes e de um elemento gráfico.

**Duas regras que a leitura do texto não deixa ver e que aparecem ao refazer os exemplos do livro com conteúdo próprio:** alinhar à esquerda não é encostar tudo numa borda só, e uma segunda borda (título para fora, itens recuados) mostra a hierarquia; e o foco pode romper a margem de propósito, com ousadia, quando o resto está bem alinhado.

## Aplicado a desenhos soltos numa tela de texto (leitura nossa)

Nenhuma fonte trata do caso; o que segue é o que os princípios implicam, e serve de regra para os desenhos de enfeite dos Stories (`marketing/social-media/stories/README.md`, "Os desenhos de enfeite"):

- **Um dominante por tela, os outros bem menores** (contraste e escala): dois desenhos quase do mesmo tamanho brigam; o claramente maior vira ponto focal. No máximo três tamanhos.
- **Folga em volta do texto** (proximidade): desenho colado a um bloco é lido como legenda dele; deixar uns 24 px de folga para texto, adesivo e outro desenho.
- **Ângulos e dispersão variados entre telas** (repetição): o mesmo estilo de traço amarra a sequência; a posição e o giro variam, o que o livro admite para o elemento repetido. Ancorar os desenhos nos mesmos pontos em todas as telas parece repetição cansativa.

**A tensão que fica a testar.** O livro diz para não pôr nada num canto ou no meio só porque o espaço está vazio, e um posicionador automático que põe o maior desenho no maior vazio faz exatamente isso. O que reconcilia, pela leitura nossa, é o capítulo da repetição: o elemento decorativo é legítimo quando parece intencional, e o que o torna intencional é o estilo comum, o tamanho claramente hierárquico e não deixar dúvida de pertencimento (nada no meio do caminho entre dois blocos). Se uma tela tiver vazio sem desenho que caiba com folga, o vazio fica.

## O que não foi conferido

- A paginação: a cópia lida é um e-book convertido, sem a numeração impressa; a ficha cita a página do PDF, e as páginas do exemplar em português estão na ficha anterior.
- As diferenças entre a 3ª edição (lida) e a 4ª (2014): só o capítulo da repetição e o índice da 4ª foram lidos, na amostra oficial.
- Algumas ilustrações da parte de tipografia que se perderam na conversão do e-book (marcadas na ficha).

## Fontes

- **Fichas:** *Design para quem não é designer (The Non-Designer's Design Book), 3ª edição: o livro inteiro, com os exemplos*, de Robin Williams (https://www.peachpit.com/store/non-designers-design-book-9780321534040) (o livro inteiro, lido direto, com os exemplos), *Design para quem não é designer (The Non-Designer's Design Book), caps. 1 a 5: a epifania da iúca e os quatro princípios*, de Robin Williams (https://ptgmedia.pearsoncmg.com/images/9780133966152/samplepages/9780133966152.pdf) (a primeira ficha, dos caps. 1 a 5 por citações de terceiros e pela amostra oficial da 4ª edição), [[2026-10-30-nngroup-proximidade-gestalt]], [[2026-10-30-nngroup-cinco-principios-de-design-visual]].
- **Só citação** (na ficha do livro): destaques de leitores no Goodreads, a resenha de Yevgeniy Brikman (2015), o Coding Horror de Jeff Atwood (2007), o relatório "TNDDB Applied" da Proper Sky (2026) e a página de curso da UNCW.
