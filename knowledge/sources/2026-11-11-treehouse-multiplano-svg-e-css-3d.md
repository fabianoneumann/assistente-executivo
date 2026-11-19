---
titulo: "Multiplane Design with SVGs and CSS 3D Transforms"
tipo: artigo
autor: "Nick Pettit (Treehouse)"   # o byline e o metadado dizem "Treehouse"; Nick Pettit pela primeira pessoa do texto, o tweet incorporado e os comentários (ver proveniência)
url: "https://blog.teamtreehouse.com/multiplane-design-with-svgs-and-css-3d-transforms"
publicado_em: 2013-08-05   # datePublished do JSON-LD e "August 5, 2013" na página; "Last Updated on May 21, 2015 by Josh Long"
capturado_em: 2026-11-11
licenca: "protegido ('©2026 Treehouse Island, Inc.' no rodapé; sem licença de conteúdo declarada no texto lido, e nenhuma licença para o código de exemplo); ficha em palavras próprias e em estrutura própria, sem o integral"
areas: [generative-media]
tags: [multiplane, parallax, css-3d, svg, 2-5d-animation, web-animation]
---

# Treehouse: a câmera multiplano no navegador com SVG e CSS 3D

Nota de fato: tabelas do que o post registra, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: o post é protegido.

**Proveniência.** Post do blog da Treehouse, https://blog.teamtreehouse.com/multiplane-design-with-svgs-and-css-3d-transforms, baixado com curl em 2026-11-11, com o texto extraído do HTML (`sha256` (hash omitido); Wayback: http://web.archive.org/web/20260411014153/https://blog.teamtreehouse.com/multiplane-design-with-svgs-and-css-3d-transforms). Autoria: o byline ("Treehouse writes on August 5, 2013"), o `meta author` e o JSON-LD dizem "Treehouse"; o texto é em primeira pessoa e começa por um tweet do autor ("Recently I tweeted"), incorporado e assinado "Nick Pettit (@nickrp) August 4, 2013", os comentários se dirigem a "Nick" e têm respostas de Nick Pettit, e a demonstração fica em `codepen.io/nickpettit`. Datas: publicação em 2013-08-05 (JSON-LD e página) e "Last Updated on May 21, 2015 by Josh Long" (dateModified 2015-05-21 no JSON-LD). O post liga para a demonstração no CodePen e para um zip do código no S3 da Treehouse ("Download the Code"); nenhum dos dois foi aberto, e o texto lido não dá licença ao código. Lido inteiro o artigo e os 20 comentários; o vídeo de Walt Disney e as imagens do post não foram vistos, só o texto em volta deles.

Condensada em nota de fato em 2026-11-11, depois de três reescritas em prosa que seguiam a fonte.

**Conferência lado a lado** (2026-11-11, na condensação, pela régua de 2026-11-11 do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (número, nome, comando, flag, valor ou rótulo curto) fica fora, como as marcas "—" e "não informado". Corpo: 5 frases de prosa e 168 células de dados em 4 tabelas, 1 delas marca e 167 de fato. As 5 células que trazem verbo foram lidas uma a uma contra a fonte: cada uma guarda um fato só. As duas frases da recomendação juntam ideias de quatro lugares do post, em outra ordem. Resultado: 0 das 5 unidades seguem a fonte; as três citações literais estão à parte. A versão anterior, pela mesma régua, dava 8 a 10 de 14 (re-revisão do Passo 7).

## Em uma frase

Relato de 2013, de quem fez o experimento, sobre levar ao navegador a profundidade da câmera multiplano da Disney com quatro planos vetoriais e as transformações 3D do CSS; para a base, é o registro mais antigo da técnica de planos espaçados em Z que o caminho do 2,5D em camadas usa, com as escolhas e os limites da época.

## De onde veio

| Item | Fato |
|---|---|
| Inspiração | câmera multiplano da Disney |
| Onde o autor a viu | Walt Disney Family Museum, São Francisco |
| Mecanismo da câmera | camadas de vidro pintado em movimento |
| Efeito da câmera | paralaxe, profundidade em imagens planas |
| Estreia da câmera | *The Old Mill*, curta de 1937 premiado com o Oscar |
| Uso depois | muitos longas de animação da Disney |
| Busca por versão em navegador | nada decente no Google |
| Ideia de partida | imagens transparentes em camadas |
| Código de partida | site Beercamp SXSW 2011 |
| O que ele fez com o código | desmontou e enxugou |
| SVG no Beercamp | nenhum |
| Estrutura do Beercamp | camadas num ambiente 3D |
| Navegação do Beercamp | rolagem |
| Arte | ilustração de Griffin Moore, do acervo da Treehouse, nunca usada |
| Tweet do experimento | 04/08/2013 |
| Demonstração | CodePen (`codepen.io/nickpettit`) |
| Código para baixar | zip no S3 da Treehouse |

## A técnica

| Escolha | Fato |
|---|---|
| Planos e ambiente | transformações 3D do CSS |
| Plano B, não usado | elementos 2D escalados, paralaxe falsa |
| Formato da arte | SVG |
| Motivo do vetor | planos ampliados a tamanho enorme e vistos de perto |
| Bitmap | descartado |
| Número de planos | 4 |
| Planos, do fundo para a frente | nuvens; montanha nevada; morros; grama |
| Tamanho dos quatro SVGs | idêntico |
| Prancheta do Illustrator | aparada na maior camada |
| Prática usual, não seguida | prancheta do tamanho de cada SVG |
| Alternativa melhor ao corte, para ele | provavelmente existe |
| Morro novo | verde-escuro, na frente |
| Montanha do fundo | maior, com neve |
| Resto da ilustração | rearranjado |
| Tamanho aparente dos objetos | desenhado no Illustrator, pela distância |
| Exemplo | árvores da frente muito maiores que as do fundo |
| Expectativa inicial | o 3D do navegador cuidaria disso |
| Na demonstração | não cuida |
| Espaçamento dos planos | translação no eixo Z |
| Escala dos planos | até encher a janela |
| Margem | sobra nas bordas |
| Como a escala foi acertada | no olho, por tentativa |
| Matemática da escala | não entendida |
| Leitura sobre a matemática | começada e adiada |
| Explicação da matemática | pedida nos comentários |
| Câmera 3D no CSS | ausente |
| Simulação da câmera | ambiente inteiro movido em Z |
| Movimento simulado | dolly para a frente |
| Rolagem | remapeada para o deslocamento em Z do ambiente |
| Origem desse truque | Beercamp |
| Plano original, não feito | rolagem ligada ao movimento relativo de cada plano |
| Fidelidade do plano original | maior, à câmera da Disney |
| Por que não o fez | o do Beercamp é bem mais fácil |
| Sensação de cena multiplano no Beercamp, para o autor | não |

## Limites e comentários

| Ponto | Estado | Quem diz |
|---|---|---|
| Chrome e Safari de computador | funcionam bem (2013) | o autor |
| Outros navegadores | resultado variado | o autor |
| Celular | problema em aberto | o autor |
| Problemas técnicos em geral | solucionáveis, para ele | o autor |
| Firefox, SVG em fundo CSS escalado por transform | pixeliza | o autor |
| Contorno para o Firefox | imagem no HTML, não no fundo CSS | o autor |
| Firefox Nightly 26a | SVG um pouco borrado | gomeboy |
| Firefox Nightly 26a, render | funciona | gomeboy |
| IE11 | tela em branco | gomeboy |
| Toque | pedido | Logan Call |
| Zoom de pinça | pedido | Mike |
| Peso do SVG em celular e dados móveis | depende do escopo do projeto | Mathew Porter |
| Pane3D | plugin jQuery de navegação 3D parecida | Spiros Martzoukos |
| wagerfield.github.io/parallax | link deixado numa resposta | Nick Pettit |
| winningontheroad.com | apontado como mesma técnica | "Totally Not a CDW Employee" |
| Hobo Lobo | paralaxes elogiadas | Dave Doolin |
| Faria diferente hoje? | pergunta de 2015, sem resposta | Kris Bulman |
| Comentários na página | 20 | — |

| Uso prático (o post deixa em aberto) | Fato |
|---|---|
| Interesse maior do autor | aplicações práticas |
| Destino sugerido | levar a pessoa a um lugar |
| Exemplos de lugar | cenário de filme ou de jogo; site de parque da Disney |
| Momento | design plano em moda |
| Relação com o design plano | evolução possível do estilo |
| Pergunta aos leitores | como usariam na prática |

## O que a fonte recomenda

Pelo relato, três decisões fazem a técnica: a arte vetorial, para o plano aguentar ampliação; a profundidade marcada duas vezes, na distância em Z e no tamanho que cada objeto já ganha no desenho; e a câmera feita movendo a cena toda, que é o atalho, em vez de cada plano por conta própria, que é o mais fiel. Nada disso pede conta, e o alcance de 2013 ficava em dois navegadores de computador.

## Citações

- "planes that are closer will whiz by quickly, while planes that are far away will appear to move very slowly"
- "I just guessed the values until it looked good"
- "A site like this cannot avoid being classified as experiential"

## Lacuna

O post não dá os valores usados (perspectiva, distâncias em Z, escalas), não mede desempenho nem peso dos arquivos, e não diz sob que licença está o código da demonstração. A demonstração e o zip não foram abertos, então o código não foi conferido.
