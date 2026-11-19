# Carrossel todo em vídeo: o que o Instagram faz e o que custa produzir

Nota rasa sobre a ideia de um carrossel em que todas as telas são vídeo, com as linhas da sequência navegando desde a tela 1 e seguindo de uma tela para a outra no swipe, num efeito de navegação contínua. Não decide nada; o que é escolha de quem pede está no fim, como pergunta. Parte do que a base já tinha: a seção "Carrossel animado no Instagram" de [[video-como-codigo]], a referência da API da Meta (*IG User Media (reference): specifications and parameters*, de Meta for Developers, https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media; e *Content Publishing (Instagram Platform guide)*, de Meta for Developers, https://developers.facebook.com/documentation/instagram-platform/content-publishing) e a reentrega pela segunda imagem, que o Mosseri descreve (abaixo).

## O que o Instagram faz

**Reiniciar o vídeo ao deslizar: não verificado.** Os dois buscadores, em inglês e em português, dizem que o vídeo de cada tela começa do zero ao chegar e recomeça ao voltar, mas nenhum cita fonte que diga isso; a busca nativa não achou relato, e nem a Meta nem a Central de Ajuda tratam do assunto nas páginas encontradas. O que a base tem de primária é só que o vídeo do Instagram repete enquanto está na tela (página da Meta lida como citação, em [[video-como-codigo]]). Também não se sabe se, durante o arrasto, a tela seguinte já toca ou mostra o quadro parado.

**Nem todo mundo desliza da tela 1 para a 2.** O Mosseri disse, num Reel de 16/10/2024, que, quando alguém vê o carrossel e não desliza, o Instagram muitas vezes dá uma segunda chance e passa sozinho para a segunda mídia (*Carousels often get more reach than single photo posts for two main reasons*, de Adam Mosseri, Reel no perfil @mosseri, https://www.instagram.com/mosseri/reel/DBOeUmTSmIC/). *Leitura do assistente:* quem recebe essa segunda chance viu a tela 1 parada e chega à 2 sem o deslize em que a emenda acontece; a tela 2 precisa se sustentar sozinha, também em movimento.

**Som: desligado por padrão, mas com fonte velha.** A [TechCrunch](https://techcrunch.com/2017/09/16/%E2%80%AAinstagram-now-autoplays-video-sound-once-turned-on-until-you-close-the-app) relatou em 2017, com confirmação do Instagram, que o vídeo do feed toca sozinho sem som ao abrir o app e que, se a pessoa liga o som de um vídeo, os seguintes tocam com som até ela fechar o app; a página da Meta sobre anúncios em carrossel diz que os cartões tocam com som desligado. Não há fonte de 2026 sobre isso. Sobre música, [Lindsey Gamble](https://www.lindseygamble.com/blog/instagram-now-lets-users-add-music-to-video-carousels), em 19/06/2024, disse que o Instagram passara a permitir música em carrossel com vídeo, silenciando o som dos vídeos; a [RecurPost](https://blog.recurpost.com/instagram-carousel-limits/), de 31/10/2026, cita o artigo da Central de Ajuda "Add music to a post with multiple photos": "Music cannot be added to carousels with videos". A fonte mais nova é a que diz não; a Central de Ajuda não foi aberta aqui. Pela API, o som é o que vem dentro do MP4, e o padrão da `slides-export` é sem áudio.

**Distribuição:** a RecurPost diz que o vídeo dentro de carrossel não é Reel e não ganha a distribuição do Reel; a [Aubrium](https://aubrium.com/blog/instagram-carousels) cita o Instagram (2025): foto e carrossel com áudio "may also appear in the Reels tab", sem número. *Leitura do assistente:* não se contradizem, e nenhuma mede.

**Limite pela API: 20 itens, vídeos inclusive.** A referência da Meta diz que o carrossel aceita até 20 imagens, vídeos ou a mistura, sem limite à parte para vídeo, e não traz especificação do vídeo de carrossel (referência IG User Media, acima). Na publicação pela API, um ensaio com 11 itens (10 JPEG e 1 MP4) fechou em FINISHED em 55 s. Mais de um vídeo no mesmo carrossel não foi ensaiado. Os dois buscadores disseram que pela API o limite segue 10, contra a primária e contra o ensaio. A Central de Ajuda avisa que post com vários vídeos "may take longer to upload" (citada pela RecurPost). O limite de 400 containers em 24 horas não pesa: um carrossel de 10 vídeos usa 22 contando um ensaio e a publicação (conta do assistente).

## O que custa produzir

O que pesa, com as contas marcadas como do assistente:

| Ponto | O que se sabe |
|---|---|
| Peso | uma tela em vídeo de 7 s com desenho por código saiu com cerca de 1,5 MB; dez telas assim, cerca de 15 MB por post (conta do assistente; o desenho mais denso pesa mais) |
| Teto por vídeo | a Meta não dá número para o vídeo de carrossel; o mais seguro é o mais estreito de Story e Reel, 3 a 60 s e até 100 MB |
| Render | dez telas de 7 s a 30 qps são 2.100 quadros fotografados (conta do assistente); o tempo por tela se mede na máquina que grava |
| Publicação | a publicação pela API cria todos os containers e espera cada vídeo por um tempo limite; a Meta processa os vídeos ao mesmo tempo; o tempo com dez vídeos não foi medido |
| Conferências | as conferências por script da `slides-export` medem o quadro final de cada tela em vídeo, o salto entre quadros seguidos, o fim parado e as juntas; o texto sobre o traço no meio da animação e a emenda entre telas nenhum script mede, e abrir à mão uns seis quadros por tela dá uns 60 por passada com dez telas (conta do assistente) |
| Objeto que se move | as conferências por script do objeto são obrigatórias por tela; com dez telas em vídeo, o trabalho se multiplica |
| Portão | o juiz lê a tela pelo quadro final; o movimento vai à leitura de quem pede. Num carrossel todo em vídeo, o efeito que a ideia quer fica inteiro fora do que o juiz lê (`marketing/social-media/portao-de-qualidade.md`) |
| Laço | se a animação é em ciclo, o salto da volta aparece a cada ciclo, e com dez telas em vídeo aparece em toda tela olhada por mais tempo que a animação; se para no quadro final, não; nos anúncios, o vídeo abaixo de 30 s repete por cerca de 90 s (citação em [[video-como-codigo]]), e no orgânico não há número |

**A emenda entre telas** (leitura do assistente): se cada vídeo começa do zero ao chegar, a linha que passa de uma tela à outra depende de dois quadros por emenda: aquele em que a tela N está quando a pessoa desliza, que pode ser qualquer um, e o quadro 0 da N+1. Com a N parada no quadro final e a N+1 começando onde a N termina na borda, a emenda fecha para quem espera o fim da animação; quem desliza no meio vê a linha pular. Fazer as linhas da tela N+1 entrarem no quadro 0 já na posição em que saem da borda da N é a metade da solução.

## O que muda na rubrica

A rubrica de design (`marketing/social-media/rubrica-de-design.md`) não mede movimento por padrão: nenhum critério trata de emenda, laço ou leitura durante o movimento; a de qualidade trata da ponte entre telas no texto. O que um carrossel todo em vídeo pediria medir, como leitura do assistente: a emenda de cada par de telas no quadro 0 e no quadro parado; a tela 2 de pé sozinha, para quem chega a ela sem deslizar; o texto legível em todo instante, não só no final; o salto do laço; a capa da grade (o primeiro item; no vídeo, o `thumb_offset`, padrão 0); e o peso total.

## O que fecha o que ficou aberto

Olhar no app um carrossel publicado com uma tela em vídeo: deslizar da tela anterior para a de vídeo, esperar, ir à seguinte e voltar (reinicia?); deslizar devagar (a tela de vídeo já se move durante o arrasto?); com o som ligado num vídeo de outro post, ver se a tela toca com som.

## As escolhas em aberto

1. **Se o teste no app mostrar que cada vídeo recomeça ao chegar, o carrossel todo em vídeo entra?** Opções: (a) sim, inteiro; (b) primeiro duas ou três telas seguidas em vídeo, para medir o custo e a emenda numa peça real; (c) não agora. Sugestão do assistente: (b).
2. **O laço:** a animação em ciclo ou o quadro final parado; com várias telas em vídeo, a escolha pesa mais.
3. **A rubrica:** o critério de movimento (emenda, laço, leitura em movimento, tela 2 sozinha) entra na rubrica de design (a) só quando o carrossel com várias telas em vídeo for adotado, ou (b) já, para a tela única. Sugestão: (a).
