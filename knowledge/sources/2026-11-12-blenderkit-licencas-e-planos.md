---
titulo: "Blendkit | Licenses"
tipo: artigo
autor: "Blendkit (antes BlenderKit)"   # documentação e página de planos do próprio serviço, sem assinatura
url: "https://www.blenderkit.com/docs/licenses/"
publicado_em: null   # nenhuma das três páginas traz data; o rodapé diz "© 2026"
capturado_em: 2026-11-12
licenca: "protegido (rodapé das três páginas: '© 2026 Blendkit (formerly known as BlenderKit) | All rights reserved'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [licensing, commercial-use, royalty-free, cc0, 3d-assets, blender, pricing, interested-party]
---

# BlenderKit: duas licenças, ambas comerciais, e o plano grátis com parte dos modelos

Nota de fato: tabelas do que a página de licenças, o FAQ de licenciamento e a página de planos do BlenderKit (que agora se chama Blendkit) dizem, com prosa só para dizer o que as fontes são, o que recomendam e o que falta. Não há integral: as três são protegidas.

**Proveniência.** Três páginas do próprio serviço, que vende os planos que descreve:

| Fonte | URL | Como foi lida | sha256 (o que mede) | Wayback |
|---|---|---|---|---|
| Licenças (a principal) | https://www.blenderkit.com/docs/licenses/ | HTML baixado por curl em 2026-11-12; lido no texto extraído do bloco principal | (hash omitido) (texto do `<main>`/`<article>`, sem tags, script e estilo) | `http://web.archive.org/web/20260610082726/https://www.blenderkit.com/docs/licenses/` |
| FAQ de licenciamento | https://www.blenderkit.com/docs/licenses/licensing-faq/ | idem | (hash omitido) (idem) | `http://web.archive.org/web/20260603105050/https://www.blenderkit.com/docs/licenses/licensing-faq/` |
| Planos | https://www.blenderkit.com/plans/pricing/ | idem, e os preços conferidos no HTML (abaixo) | (hash omitido) (idem) | `http://web.archive.org/web/20260610082737/https://www.blenderkit.com/plans/pricing/` |

Títulos conferidos: "Blendkit | Licenses", "Blendkit | Licensing FAQ" e "Blendkit | Subscribe to the Blendkit FREE library of 3D assets"; o `canonical` das três aponta para o domínio blendkit.com, nos mesmos caminhos. Nenhuma página traz data. Cobertura: as três páginas inteiras, fora o menu e o rodapé.

**Os preços.** O texto extraído só mostra a aba ativa de cada plano (a anual), com o preço cheio riscado (classe `strike`) e o preço com desconto ao lado. Os preços das outras abas estão nos atributos de cada aba, no mesmo elemento `<a>` que traz o nome dela ("30 day glimpse", "Monthly", "Yearly"), então a ligação de preço e aba vem do próprio elemento, não só da ordem no HTML. Os nomes dos atributos estão trocados em relação ao que mostram: `data-discount-price-*` guarda o preço que aparece riscado, e `data-price-*`, o preço com desconto; nas abas que não estão ativas, essa leitura sai do nome dos atributos e da aba ativa, porque o script que troca os números não rodou. Os dados de análise da página (`ga4_plan_item`) dão o preço por ano de cada plano anual. Os preços com desconto são 67% dos cheios em todas as abas (conta do assistente), os 33% do banner.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), medido contra os três textos juntos num arquivo só (o texto extraído das licenças, do FAQ e dos planos), com 34 unidades medidas (20 de prosa, 14 de célula com texto), 0 coladas e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 34 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a frase que junta lugares distantes não conta. Resultado: 11 de 34, todas células de tabela: 11 das 12 fora da proveniência (fica fora a que descreve o texto do CC0); nenhuma unidade de prosa segue a fonte. O FAQ vai fora da ordem da página, e a maior sequência de unidades seguidas na ordem da fonte é de 2.

## Em uma frase

Texto de quem vende o serviço: tudo o que se baixa do BlenderKit pode entrar em trabalho comercial, sob a licença Royalty Free ou a CC0 de cada asset, e a diferença é que a Royalty Free veta revender o asset como asset; a biblioteca grátis tem cerca de 24 mil dos 83 mil modelos, e o resto pede um plano pago por assento.

## As licenças

| Licença | Ponto | Fato |
|---|---|---|
| As duas | Quantas | duas: Royalty Free e CC0 |
| As duas | Uso comercial | todo download, pelas duas |
| As duas | Vender obra derivada de nível mais alto | permitido pelas duas |
| Royalty Free | Crédito ao autor | dispensado no uso comercial |
| Royalty Free | Revender o asset na mesma forma | vetado, mesmo modificado |
| Royalty Free | Exemplos do veto | modelo vendido como modelo; parte de pacote de assets; fase de jogo num marketplace |
| CC0 | O que é | renúncia ao direito autoral e de base de dados, o mais perto possível do domínio público |
| CC0 | Uso | qualquer fim, sem restrição de direito autoral |
| CC0 | Texto da página | a descrição da própria Creative Commons, que fala em "our licenses" |

## O FAQ de licenciamento (sobre a Royalty Free)

As perguntas vão por tema, não na ordem da página.

| Pergunta | Resposta |
|---|---|
| Vender imagem 2D de banco (Shutterstock, Adobe Stock) com material grátis num modelo próprio | sim |
| Vender mockup PSD (GraphicRiver, Creative Market) de modelo grátis personalizado e renderizado | sim |
| Vender render e animação | sim |
| Vender modelo próprio com material do BlenderKit | sim |
| Vender jogo com modelos ou materiais | sim, desde que o jogador não consiga tirar os assets com facilidade do que é distribuído |
| Vender em outro marketplace uma cena 3D montada com modelos do BlenderKit | não |
| Remixar material de outra pessoa | o procedural, com melhora grande; o que tem textura de imagem, não |
| Subir composição com modelos alheios | ainda não dá |
| Subir material montado com texturas baixadas | não, se vierem de serviço comercial; e o BlenderKit tende a recusar o que vem de sites CC0 (Texture Haven, cgbookcase, cc0textures) |
| Por que recusar as CC0 | ligar texturas ao shader dá pouco trabalho, e a renda deveria ir a quem as fez; o próprio FAQ diz que é opinião da casa, não lei |
| A quem o FAQ se aplica | à Royalty Free; a CC0 deixa fazer tudo |
| Pedido para o CC0 | creditar o autor e não revender |

## Os planos

| Ponto | Free | Full | Business |
|---|---|---|---|
| Para quem | não diz; um botão convida a se registrar | empresa com até 5 funcionários e receita anual até US$ 100 mil | empresa com mais de 5 funcionários ou receita anual acima de US$ 100 mil |
| Cobrança | US$ 0 por mês, "Infinitely" | por assento | por assento |
| Anual, preço cheio riscado (por mês) | — | US$ 8,90 | US$ 29 |
| Anual, com desconto (por mês) | — | US$ 5,96 | US$ 19,43 |
| Anual, por ano (dados de análise) | — | US$ 71,52 | US$ 233,16 |
| Mensal, cheio e com desconto | — | US$ 15,90 e 10,65 | US$ 48 e 32,16 |
| "30 day glimpse", cheio e com desconto | — | US$ 17,90 e 11,99, sem renovação | não há |
| Modelos | 23.944 | 82.658 | 82.658 |
| Materiais | 43.285 | 43.285 | 43.285 |
| Cenas | 1.100 | 4.803 | 4.803 |
| HDRIs | 5.085 | 15.370 | 15.370 |
| Pincéis | 1.280 | 7.268 | 7.268 |
| Envio de assets | sim | sim | sim |
| Armazenamento privado | 200 MiB | 2 GiB | 100 GiB |
| Add-ons extras | não listados | sim | sim |
| Desconto de estudante | — | 50% | — |

| Ponto | Fato |
|---|---|
| Promoção do dia da captura | "Happy Black Birthday", 33% de desconto, mantido nas renovações automáticas |
| Para onde vai a assinatura | 70% aos criadores, e parte ao código aberto |
| Como a página se descreve | a maior biblioteca de assets integrada ao Blender |
| Preço sem desconto fora da promoção | a página não mostra outro além do riscado |

## O que a fonte recomenda

Pelas duas licenças, o asset entra em render, animação, jogo e imagem de banco à venda; o que a Royalty Free barra é vender o próprio asset, ou uma cena feita com ele, de novo como asset, e o jogo tem de guardar os arquivos fora do alcance fácil do jogador. Mesmo no CC0, que permite tudo, o BlenderKit pede crédito ao autor e nenhuma revenda, e diz que recusa material que só liga texturas CC0 de outros sites.

## Citações

- "Everything you download is available for commercial use." (Licenças)
- "doesn't allow for re-sale of the asset in the same form" (Licenças, Royalty Free)
- "Yes, if these can't be extracted by the users in an easy way." (FAQ, sobre vender jogo)

## Lacuna

As páginas não dizem como saber a licença de um asset (onde ela aparece, se muda depois do download), se o plano grátis pede conta para baixar, nem se há crédito exigido em alguma situação na Royalty Free. Não dão o preço sem a promoção nem a data em que ela acaba, não explicam o que é um assento quando a mesma pessoa usa vários computadores e não dizem se as contagens da biblioteca são do dia. O FAQ não trata de uso em treino de IA nem de vídeo gerado com ajuda de IA a partir de um render.
