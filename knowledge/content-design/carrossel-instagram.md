# Carrossel de Instagram — áreas seguras e boas práticas de design

Referência de design para carrosséis (4:5). Base para os templates da série de exemplo e para qualquer peça futura. Síntese analítica (a voz de conteúdo só entra quando vira post).

> Fontes (só citação, sem ficha no repositório): *Instagram Carousel Size & Aspect Ratio Guide 2026 (Carousel Maker)*, de carouselmaker.co, https://carouselmaker.co/en/blog/instagram-carousel-size-aspect-ratio-guide; *Instagram Safe Zone Sizes Guide 2026 (CampaignSwift)*, de campaignswift.com, https://campaignswift.com/blog/instagram-safe-zone-sizes. Corroboração (só citação): buffer.com, admakeai.com, postworthy.app, stan.store, zeely.ai (pesquisa pela skill `research`).

## Formato
- **4:5 = 1080×1350px** é o recomendado (preenche quase a tela no mobile, mais real estate vertical no feed). Alternativas: 1:1 (1080×1080), 3:4 (1080×1440, novo, mas não pode ser impulsionado como anúncio).
- **A proporção do 1º slide trava o carrossel inteiro.** Todos os slides na mesma dimensão, senão o IG corta.

## Área segura (4:5, 1080×1350)
As fontes variam; a faixa e a recomendação consolidada:
- **Laterais:** 40–80px (usar **~80px** para respiro).
- **Topo:** 80–130px (username/menu ficam na faixa superior).
- **Base:** no **feed**, a interface não fica sobre a imagem: nome, botões e legenda ficam abaixo dela (*Instagram safe zones in 2026: dimensions for Reels, Stories, feed posts, and ads*, de Zeely (blog), https://zeely.ai/blog/master-instagram-safe-zones/; o Gemini, numa pesquisa rasa, diz o mesmo e atribui ao Meta Ads Guide, não conferido). A faixa de 180 a 240 px que se via em versões antigas desta referência vem de Stories e Reels, com números diferentes para cada um (a mesma fonte): no **Reels**, 14% livres em cima, 35% embaixo (~670 px) e 6% de cada lado; no **Stories orgânico**, 14% em cima e 20% embaixo (~380 px), com área segura de ~950 × 1270 px; em **Stories e Reels de anúncio**, as margens do Reels. Ponto em aberto: o Perplexity diz que os pontinhos do carrossel ficam sobre a parte de baixo da imagem; a medida que desempata é um print do próprio feed. Enquanto isso, vale a área segura de 1000×1270 centrada, com o essencial longe do centro da base, onde os pontinhos ficariam se estiverem por cima.
- Regra simples: manter o essencial na **faixa central ~70–80%** ("title-safe"), mínimo 60px de qualquer borda. Área segura citada: **1000×1270 centrada**.
- **Corte no grid do perfil:** desde janeiro de 2025 a grade mostra miniaturas em 3:4. Um post 4:5 (1080×1350) perde as laterais na miniatura, cerca de 34 px de cada lado (a conta da fonte, que fala em topo e base, não fecha), então o gancho e o rosto da capa ficam longe das bordas laterais; as margens de 80 px já cobrem isso. O feed aceita 3:4 nativo (1080×1440) desde meados de 2025, que aparece inteiro no feed e na grade (mesma fonte); é uma opção de formato, não testada.

## Tipografia (mobile-first)
- **Gancho de capa:** grande e curto (fontes divergem: 36–48px conservador; até 72–96px para poucas palavras). Poucas palavras.
- **Subtítulos/títulos de slide:** 40–64px.
- **Corpo:** 34 a 42 px com piso de 30, em [[texto-que-cabe-e-legibilidade]] e na rubrica de design (`marketing/social-media/rubrica-de-design.md`). Os números de mercado mais antigos (24 a 32 px, mínimo de 22) ficaram superados. Abaixo do piso não se encolhe: cortar, dividir ou mover para a legenda, com antes e depois.
- **Labels/handle/paginação:** rótulo com piso de 28 px.
- **Line-height:** corpo ~1.3; títulos 1.1–1.2.
- **Comprimento de linha:** as fontes de mercado dizem 30–45 caracteres, com blocos de ~600–720px de largura. A coluna de uma série é decisão do design system dela (por exemplo, uma coluna de 850 px, com 47 a 54 caracteres por linha cheia); o desempate e o porquê estão em [[quebra-de-linha-em-tela]], seção 5.
- **Máx. de linhas de corpo:** o limite é o que cabe na tela sem passar do piso (ver [[texto-que-cabe-e-legibilidade]]), que tem também a ordem do que cede quando o texto não cabe.

## Composição
- **Negative space:** as fontes de mercado falam em dedicar **35–45%** do slide a espaço vazio. O número vem só de citação de blogs, sem ficha, e o livro da Robin Williams diz que a quantidade de branco não separa o bom do ruim, a organização sim; por isso a área vazia total não pesa no portão: o que se mede é o vazio livre ou preso, pela leitura, e a maior faixa vazia em fração da altura útil, pelo código (ver [[principios-de-design-visual]]). Fica aqui como referência de mercado.
- **Uma ideia por slide.** Se precisa encolher a fonte pra caber, tem texto demais.
- **Alinhamento:** corpo à esquerda (mais fácil de ler); centralizado só em ganchos/citações curtas.
- **Ênfase:** destacar palavra-chave por **cor/negrito** de forma seletiva; evitar CAPS em linhas longas.
- **Contraste:** ≥4.5:1 texto/fundo; usar overlay escuro sob texto em cima de foto.
- **Export:** sRGB, JPEG (a API de publicação não aceita PNG; PNG só para revisão, como na skill `slides-export`), abaixo de 8 MB por slide.

## Aplicação prática (um exemplo de ajuste)
Numa capa de carrossel com foto, o ajuste que funcionou foi: laterais 80px, topo ~130px, base ~184px; títulos maiores, destaque de palavra-chave em cor, conteúdo centralizado com respiro, foto com overlay escuro na base. O diagnóstico que levou ao ajuste: base apertada (120px) e texto pequeno e uniforme davam ar de "documento/PDF" em vez de peça social.

> **Manutenção:** refletir estes números nos templates de prompt da série (em `marketing/social-media/carousels/series/exemplo/`) quando eles existirem.

## Elos
- Série: o design system da série, em `marketing/social-media/carousels/series/exemplo/`.
- Exemplos: para vídeo curto, [[reels-formatos-e-volume]] e [[roteiro-em-formato-curto-o-que-e-medido]].
