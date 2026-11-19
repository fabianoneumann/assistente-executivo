---
titulo: "fal: páginas de modelo fal-ai/veo3.1, fal-ai/veo3.1/fast e bytedance/seedance-2.5/reference-to-video, e o artigo Kling 4.0 vs. Seedance 2.5: What's The Difference?"
tipo: artigo
autor: "fal (fal.ai); o artigo é de John Ozuysal, no Learn da fal"
url: "https://fal.ai/models/fal-ai/veo3.1"
publicado_em: 2025-10-08   # campo date do metadado do modelo fal-ai/veo3.1 no payload da página; o texto visível não traz data
capturado_em: 2026-11-11
licenca: "protegida: 'All Rights Reserved.' no rodapé das páginas da fal. Ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [fal, aggregator, api-pricing, veo, seedance, kling, video-generation, image-to-video, first-last-frame, reference-to-video, video-editing, video-extension, motion-transfer, real-face-restriction, deprecation]
---

# fal: o que as páginas de Veo 3.1, Veo 3.1 Fast e Seedance 2.5 aceitam e cobram, e o artigo Kling 4.0 contra Seedance 2.5 (novembro de 2026)

**Proveniência.** Quatro páginas da fal, baixadas como HTML com `curl` em 11/11/2026: https://fal.ai/models/fal-ai/veo3.1 (a principal), https://fal.ai/models/fal-ai/veo3.1/fast, https://fal.ai/models/bytedance/seedance-2.5/reference-to-video e o artigo https://fal.ai/learn/devs/kling-4-0-vs-seedance-2-5. O texto visível foi lido no que se extraiu do HTML; das três páginas de modelo, saíram por script do payload do Next.js embutido no HTML o esquema de entrada (`metadata.openapi.components.schemas`, o objeto que termina em `Input`), o objeto `endpointBilling`, os metadados do modelo (`date`, `pricingInfoOverride`, `deprecated`, `removed`) e os avisos de endpoint (`endpointMessages` e `featureFlagPayloads.endpoint_messages`). Ficaram de fora o playground, os vídeos de exemplo, a navegação e o rodapé do site; do artigo, a lista "Recently Added" (modelos novos de outras famílias), os artigos relacionados e a navegação.

**Quem fala.** A fal, revendedora dos modelos (as três páginas de modelo marcam o endpoint como `partner`). O artigo é assinado por John Ozuysal, apresentado na página como fundador da House of Growth, e escrito em nome da fal ("our playground", "our model page").

**Datas.** As páginas de modelo não mostram data; o metadado `date` do modelo dá 2025-10-08 para `fal-ai/veo3.1` e `fal-ai/veo3.1/fast`, e 2026-07-20 para `bytedance/seedance-2.5/reference-to-video`. O artigo foi publicado em 04/11/2026 ("Published Nov 4, 2026", e `datePublished` e `dateModified` iguais no HTML).

## Veo 3.1 (`fal-ai/veo3.1`)

**Situação do endpoint.** A página traz o aviso "This endpoint will be deprecated on November 17, 2026." O payload repete o aviso em duas regras: uma para `fal-ai/veo3.1` exatamente e outra para tudo o que começa com `fal-ai/veo3.1/`.

**Modos e endpoints, com o preço mínimo ("From") da tabela.**

| Modo | Endpoint | A partir de |
|---|---|---|
| Texto para vídeo | `fal-ai/veo3.1` | US$ 0,20/s |
| Texto para vídeo (Fast) | `fal-ai/veo3.1/fast` | US$ 0,10/s |
| Imagem para vídeo | `fal-ai/veo3.1/image-to-video` | US$ 0,20/s |
| Imagem para vídeo (Fast) | `fal-ai/veo3.1/fast/image-to-video` | US$ 0,10/s |
| Primeiro e último quadro | `fal-ai/veo3.1/first-last-frame-to-video` | US$ 0,20/s |
| Primeiro e último quadro (Fast) | `fal-ai/veo3.1/fast/first-last-frame-to-video` | US$ 0,10/s |
| Referência para vídeo | `fal-ai/veo3.1/reference-to-video` | US$ 0,20/s |
| Extensão de vídeo | `fal-ai/veo3.1/extend-video` | US$ 0,20/s |
| Extensão de vídeo (Fast) | `fal-ai/veo3.1/fast/extend-video` | US$ 0,10/s |

**O que entra no endpoint de texto para vídeo** (esquema `Veo31TextToVideoInput`, o único que a página traz): `prompt` obrigatório, até 20.000 caracteres; `aspect_ratio` 16:9 (padrão) ou 9:16; `duration` `4s`, `6s` ou `8s` (padrão `8s`); `resolution` `720p` (padrão), `1080p` ou `4k`; `generate_audio` ligado por padrão; `negative_prompt`; `seed`; `auto_fix` (ligado por padrão: reescreve o prompt que falhar na política de conteúdo ou na validação); `safety_tolerance` de `1` (mais restrito) a `6`, padrão `4`, marcado na interface como fixo. A página diz ainda que o vídeo sai a 24 fps, que cada geração tem até 8 s, e que o som (diálogo com lábios sincronizados, efeitos, música) pode ser ligado ou desligado a cada pedido.

**Preço** (texto do playground, igual ao `pricingInfoOverride`, e tabela "Detailed Pricing"; por segundo de vídeo gerado):

| Camada | Resolução | Sem áudio | Com áudio |
|---|---|---|---|
| Standard | 720p / 1080p | US$ 0,20 | US$ 0,40 |
| Standard | 4K | US$ 0,40 | US$ 0,60 |
| Fast | 720p / 1080p | US$ 0,10 | US$ 0,15 |
| Fast | 4K | US$ 0,30 | US$ 0,35 |

O exemplo da página: 5 s em 1080p com áudio custam US$ 2,00 no Standard e US$ 0,75 no Fast. O `endpointBilling` do endpoint traz `billing_unit: "seconds"` e `price: 0.4`, sem dizer a que condição esse 0,4 corresponde.

**Extensão.** O endpoint de extensão acrescenta até 7 s por passo, até 20 passos, o que a página soma em cerca de 148 s a partir de um clipe.

**Camadas do Veo 3.1, segundo a página.** Standard e Fast, ambas com áudio e até 4K, valem para todos os modos; a camada Light, sem áudio e até 720p, existe só nas plataformas do Google, "not currently on fal.ai".

**O que o modelo recusa.** A resposta do FAQ lista violência gráfica, conteúdo explícito, conteúdo que promova dano e "characters resembling real individuals or celebrities".

**Outros pontos da página.** Todo vídeo leva SynthID, que não se desliga. Uma tabela coloca o Veo 3.1 ao lado de Sora 2, Kling 2.x e Runway Gen-4 (resolução máxima, áudio nativo, fps, duração, acesso por API, marca d'água); casos de uso citados por nome (eToro, Canva, Promise Studios, Razorfish, Volley, OpusClip, Synthesia); uma fórmula de prompt (tipo de plano, sujeito, ação, ambiente, estilo, som) com dicas de câmera, de som descrito por extenso e de falas curtas que caibam em 8 s; o uso comercial é permitido pela API, remetendo aos termos de serviço; e o Veo 3.1 também está no Google AI Studio, no Vertex AI, no app Gemini e no Google Flow.

**Contradições dentro da página.** O exemplo de código em Python passa `"audio": True`, mas o esquema da mesma página chama o parâmetro de `generate_audio`. E o aviso de descontinuação em 17/11/2026 convive, no metadado do modelo, com `deprecated: false` e `removed: false`.

## Veo 3.1 Fast (`fal-ai/veo3.1/fast`)

A página é curta: o playground, o texto de preço e um aviso próprio, mais forte que o da página do Standard: "This model will be removed on November 17, 2026. Move to a supported model before then." O metadado do modelo, como no Standard, diz `deprecated: false` e `removed: false`. O esquema de entrada é o mesmo do texto para vídeo do Standard (`Veo31TextToVideoInput`, com as mesmas opções de duração, resolução, proporção e áudio). Preço por segundo: US$ 0,10 sem áudio e US$ 0,15 com áudio em 720p ou 1080p; em 4K, US$ 0,30 e US$ 0,35; o exemplo dá 5 s em 1080p com áudio por US$ 0,75. O `endpointBilling` traz `price: 0.15` em `seconds`.

## Seedance 2.5, referência para vídeo (`bytedance/seedance-2.5/reference-to-video`)

**O que o endpoint faz.** Gera um vídeo de até 30 s a partir de até 50 referências somadas (imagens, vídeos, áudios), e o mesmo endpoint cobre edição e continuação de um vídeo. Os outros dois endpoints da família na fal são `bytedance/seedance-2.5/text-to-video` e `bytedance/seedance-2.5/image-to-video`.

**Entradas, pelo esquema `Seedance2R2VInput`.** `task`: `reference` (padrão), `editing` (força proporção e duração em `auto`), `extension` (força a proporção em `auto`) ou `auto`, em que o modelo decide pelo prompt e pelas referências. `image_urls`: até 30 imagens, até 30 MB cada. `video_urls`: até 10 vídeos MP4 ou MOV, cada um de 1,8 a 30,2 s e até 200 MB, todos juntos até 30,2 s, de 300 a 6.000 px por lado, proporção de 0,4 a 2,5, de 24 a 60 fps. `audio_urls`: até 10 arquivos MP3 ou WAV, cada um de 1,8 a 30,2 s e até 15 MB, todos juntos até 30,2 s. O total de arquivos, somadas as três listas, não passa de 50. `resolution`: `480p`, `720p` (padrão) ou `1080p`. `draft`: gera uma prévia a 480p, por cima da resolução pedida, e devolve um `draft_id` para completar a prévia em 1080p em até 14 dias. `duration`: `auto` (padrão) ou de `4` a `30`. `aspect_ratio`: `auto` (padrão), 21:9, 16:9, 4:3, 1:1, 3:4, 9:16. `generate_audio`, ligado por padrão, com a nota de que o preço é o mesmo com ou sem áudio. Também `bitrate_mode` (`standard` ou `high`), `codec` (`auto`, `H264`, `H265`), `seed` (o resultado ainda pode variar um pouco) e `end_user_id` (a seção de documentação da página o diz obrigatório para acesso B2B).

**Resoluções em pixels** (tabela da página, só 480p e 720p): em 16:9, 864×496 e 1280×720; em 9:16, 496×864 e 720×1280; também 21:9, 4:3, 1:1 e 3:4.

**Preço.** A cobrança é por token, e neste endpoint a duração do vídeo de entrada é cobrada junto com a da saída. A fórmula que a página dá como a que vale: tokens = altura × largura da saída × (segundos de vídeo de entrada + segundos de saída) × 24 / 1024. O preço é de US$ 0,0214 por mil tokens em 480p e 720p e de cerca de US$ 0,0234 por mil em 1080p (`endpointBilling`: `billing_unit: "1000 tokens"`, `price: 0.0214`); com qualquer vídeo de referência, multiplica-se por 0,6; imagens e áudios de referência não se cobram.

| Resolução | Sem vídeo de referência | Com vídeo de referência (× 0,6, sobre segundos de entrada e de saída) |
|---|---|---|
| 480p | cerca de US$ 0,2205/s | cerca de US$ 0,1323/s |
| 720p | cerca de US$ 0,4730/s | cerca de US$ 0,2838/s |
| 1080p | cerca de US$ 1,164/s (só no texto do playground) | não dado |

A página avisa que os valores por segundo são aproximações para 16:9. Os exemplos dela: 10 s a 720p em 16:9 só com imagens e áudio, 216.000 tokens, cerca de US$ 4,62; 10 s com um vídeo de referência de 8 s, 388.800 tokens, cerca de US$ 4,99 depois do × 0,6; 30 s com um vídeo de 10 s, 864.000 tokens, cerca de US$ 11,09. Daí a recomendação, na mesma seção, de cortar o vídeo de referência, já que todo segundo enviado entra na conta.

**Dicas.** Para gastar menos: cortar o vídeo de referência ao trecho que importa e acertar a composição a 480p, que custa menos da metade, antes de refazer a semente vencedora a 720p. Para controlar: dizer no prompt para que serve cada referência, nomear na edição o que troca e o que fica, e começar pelas duas ou três referências que carregam a ideia, porque cada uma disputa influência com as outras. Para a identidade: imagens limpas, bem iluminadas, com um sujeito só. O endpoint com vídeo de entrada é o mais lento dos três, e a página manda usar a fila em vez da chamada síncrona.

**Contradições dentro da página.** (1) Resolução: a tabela de parâmetros da documentação e a de pixels só têm 480p e 720p, e a seção de preço fala só dessas duas; o esquema aceita `1080p`, e o texto do playground dá o preço de 1080p. (2) Prompt: a tabela de parâmetros o marca como obrigatório; no esquema ele aceita nulo e não está entre os obrigatórios, e o playground o mostra como opcional. (3) Nome das referências no prompt: a documentação usa [Image1], [Video1], [Audio1]; o esquema, @Image1, @Video1, @Audio1. (4) Formatos de imagem aceitos: a tabela de parâmetros lista jpg, jpeg, png, webp, gif e avif; o esquema, JPG, PNG, WebP, BMP, TIFF, GIF, HEIC e HEIF; o playground, jpg, jpeg, png, webp, gif, avif, heic e heif. (5) Preço por segundo e exemplo: pela própria tabela, 10 s a 720p custariam cerca de US$ 4,73 (10 × 0,4730), mas o exemplo de 10 s a 720p dá 216.000 tokens e cerca de US$ 4,62.

**O que a página não diz.** Nada sobre rosto ou pessoa real nas referências. A seção de documentação não cita o `draft`, que só aparece no esquema.

## O artigo "Kling 4.0 vs. Seedance 2.5: What's The Difference?" (04/11/2026)

Coberto inteiro, na ordem do artigo.

**Abertura.** O subtítulo promete o confronto nos quatro tipos de pedido que os dois modelos têm em comum, com as diferenças de esquema e o preço por segundo. O resumo do topo antecipa as conclusões que a tabela detalha depois: no acesso, o Kling 4.0 está no playground e no fal Agent, "with API access coming soon", e o Seedance 2.5 já tem API em três endpoints hospedados nos EUA; no preço, o Kling 4.0 sai mais barato por segundo a 720p e 1080p; e cada um tem o que falta ao outro (do lado do Seedance, referência de áudio, mais imagens de referência, 480p e quadros 4:3 e 3:4; do lado do Kling, `multi_prompt` e elementos com voz). O método anunciado: oito pedidos idênticos aos dois, dois por tipo de tarefa, com os prompts publicados e a conta de tudo a 1080p.

**TL;DR.** O autor ressalva que a API do Kling 4.0 talvez já esteja aberta quando o texto for lido. Os endpoints do Seedance 2.5 nos EUA têm o prefixo `bytedance/seedance-2.5/us`. Na fal, o teto dos dois é 1080p. A edição vai a um endpoint próprio no Kling 4.0 (`kling/v4/video-to-video/edit`) e ao de referência com `task` `"editing"` no Seedance 2.5. As vozes, no Kling 4.0, vão presas a elementos; o Kling 4.0 aceita até 10 imagens de referência. Todos os pares rodaram a 1080p, com o texto do prompt idêntico e o áudio do Seedance no padrão; as imagens de partida vieram do Nano Banana 2.1 e os vídeos de origem do H3 Max, para que nenhum dos dois modelos edite material próprio.

**A tabela de comparação** (os quatro endpoints `kling/v4` contra os três do Seedance 2.5 nos EUA):

| Critério | Kling 4.0 | Seedance 2.5 (EUA) |
|---|---|---|
| Endpoints | `kling/v4/text-to-video`, `kling/v4/image-to-video`, `kling/v4/reference-to-video`, `kling/v4/video-to-video/edit` | `bytedance/seedance-2.5/us/text-to-video`, `.../us/image-to-video`, `.../us/reference-to-video` (edição com `task` "editing") |
| Acesso na fal | playground e fal Agent; API em breve | playground e API |
| Duração | 3 a 30 s | 4 a 30 s, ou `auto` |
| Resolução | 720p ou 1080p (padrão 1080p) | 480p, 720p ou 1080p (padrão 720p) |
| Proporções | 16:9, 9:16, 1:1, 21:9; `auto` só no de referência | auto, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16; no de imagem, fixa em `auto` |
| Áudio | estéreo de dois canais e lábios sincronizados, pela página do modelo; sem campo de áudio no esquema | `generate_audio`, ligado por padrão, mesmo preço ligado ou não |
| Várias tomadas | `multi_prompt`, com a duração igual à soma das tomadas | sem campo; as tomadas vão no texto do prompt |
| Primeiro e último quadro | `start_image_url` e `end_image_url` | `image_url` e `end_image_url` |
| Referências | até 10 imagens; até 5 vídeos, de 3 a 30 s cada e 30 s somados com os vídeos de elementos; voz por `voice_id` em até 3 elementos; até 7 elementos reutilizáveis, feitos de imagens ou de um vídeo; no máximo 15 arquivos por pedido, pela página do modelo | até 30 imagens; até 10 vídeos, de 1,8 a 30,2 s cada e 30,2 s somados; até 10 áudios MP3 ou WAV em `audio_urls`; sem elementos; no máximo 50 arquivos |
| Vídeo a editar | 3 a 30 s, 700 a 4553 px, até 300 MB | 1,8 a 30,2 s, 300 a 6000 px, até 200 MB |
| Semente e codificação | sem `seed`, sem opções de codificação | `seed` no de referência; `bitrate_mode` e `codec` (H.264 ou H.265) |
| Preço sem vídeo de entrada | US$ 0,157/s (720p), 0,235/s (1080p) | cerca de 0,4730/s (720p), 1,164/s (1080p) |
| Preço a 1080p com vídeo de entrada | US$ 0,141 por segundo de entrada mais saída, no mínimo 2× a saída | cerca de 0,698 por segundo de entrada mais saída (1,164 × 0,6) |
| Rascunho mais barato | Kling 4.0 Flash a 720p, até 20 s, em acesso antecipado | 480p a cerca de 0,2205/s |
| Línguas da fala | dez listadas na página do modelo, com sotaques como o inglês britânico e o indiano | fala sincronizada pelo esquema, sem lista de línguas |
| Uso comercial | sim | sim |

Os dois leem referências como @Image1 e @Video1, o que deixou o autor usar o mesmo prompt nos dois.

**Como os testes foram feitos.** Tudo rodou no playground, as 16 gerações, porque a API do Kling 4.0 ainda não estava aberta e o autor quis a mesma interface para os dois. Igualados: 1080p, o texto do prompt palavra por palavra, e duração e proporção onde os dois esquemas têm o campo. Diferenças que o esquema impôs: o Kling não tem chave de áudio e cuida do som sozinho, enquanto o Seedance ficou com `generate_audio` ligado e semente e codificação no padrão; no teste 2, o Kling recebeu o mesmo prompt único, com o `multi_prompt` vazio; nos testes de referência, os dois receberam só `image_urls`, sem elementos no Kling; nas edições, o Kling ficou com a duração em branco e o Seedance com `task` em `"editing"`. Convenção dos prompts: fala entre aspas duplas, texto na tela entre aspas simples. Insumos: a imagem de partida já na proporção final (o Seedance fixa `auto` na imagem para vídeo, e o Kling não tem campo de proporção); os vídeos de origem gerados no H3 Max a 1080p, com a expansão de prompt desligada, altura que passa do mínimo de 700 px do endpoint de edição do Kling.

**Os oito testes.** O artigo dá, para cada um, as configurações, o prompt inteiro e o que o autor olharia no resultado; os vídeos ficam na página, e o texto não diz qual modelo se saiu melhor em nenhum deles.

1. Texto para vídeo, 9:16, 10 s: dois personagens numa loja apresentando um robô aspirador, cada um com uma fala e um sotaque (americano e indiano). O risco que o autor vigia é a fala sair da boca errada; depois, a faixa limpa no chão e uma legenda de preço com a grafia intacta durante todo o clipe.
2. Texto para vídeo, 21:9, 20 s: um comercial de panela em quatro tempos de 5 s, com os tempos escritos no prompt (o Seedance não tem `multi_prompt`). O autor confere se o vermelho da panela bate entre o close e o fim, e se os cortes caem a cada 5 s.
3. Imagem para vídeo, 16:9, 6 s, só com o quadro inicial: uma caixa de som à beira de um lago que toca um grave; as gotas no tampo devem pular no ritmo e a câmera faz um arco de 30 graus.
4. Imagem para vídeo, 1:1, 8 s, com quadro inicial e final (o final feito editando o inicial no Nano Banana 2.1 Edit): uma mesa que sobe da altura sentada à de pé com a câmera parada. O autor reprovaria a tomada se o último quadro pulasse em relação à imagem final ou se as pernas de aço entortassem ou se duplicassem.
5. Referência, 9:16, 12 s, com quatro imagens (a mulher, a bolsa de frente, a bolsa de perfil, o café): a mulher entra no café com a bolsa e fala com sotaque britânico. O autor olha primeiro a marca gravada no couro, que costuma borrar quando a aba se mexe.
6. Referência com vídeo, 16:9, 8 s: um clipe de 5 s do H3 Max com um cubo cinza e uma órbita de 180 graus dá só o caminho e o ritmo da câmera, e uma foto de produto dá o relógio que substitui o cubo; a órbita deve bater com a do clipe em direção e velocidade, e a hora e a marca no mostrador devem continuar legíveis.
7. Edição, 16:9, cerca de 8 s: trocar o fundo de estúdio de um vídeo de aspirador por uma sala escandinava, só com o prompt, mantendo mãos, grãos de café, piso e câmera. O ponto a conferir é a junção do piso com a sala nova.
8. Edição com imagem de referência, 9:16, cerca de 10 s: trocar o capacete preto de uma ciclista por um verde com a marca da foto de referência; o quadro a examinar é o do fecho, em que os dedos passam pela fivela nova.

**Quanto custa na fal.** As taxas vêm das páginas de playground de cada endpoint, e a nota do artigo diz que as taxas ao vivo dessas páginas valem mais que a tabela dele.

| Endpoint e modo | Taxa | O que se cobra |
|---|---|---|
| Kling 4.0, texto, imagem ou referência sem vídeo | US$ 0,157/s (720p), 0,235/s (1080p) | segundos de saída |
| Kling 4.0, referência com vídeo de referência ou elemento de vídeo | US$ 0,094/s (720p), 0,141/s (1080p) | segundos de entrada mais saída, no mínimo 2× a saída |
| Kling 4.0, edição de vídeo | US$ 0,094/s (720p), 0,141/s (1080p) | idem |
| Seedance 2.5, texto, imagem ou referência sem vídeo | cerca de 0,2205/s (480p), 0,4730 (720p), 1,164 (1080p) | tokens a 0,0214 por mil (480p e 720p), cerca de 0,0234 (1080p) |
| Seedance 2.5, referência com vídeo, inclusive edição | as taxas acima × 0,6: cerca de 0,2838/s (720p) e 0,698/s (1080p) | tokens sobre segundos de entrada mais saída |

O exemplo do teste 6: 5 s de referência e 8 s de saída somam 13 s; o piso do Kling eleva a conta a 16 s, US$ 2,256 a 1080p; o Seedance cobra os 13 s a cerca de 0,698, uns US$ 9,08. A tabela dos oito testes a 1080p:

| Teste | Kling 4.0 | Seedance 2.5 (aprox.) |
|---|---|---|
| 1. Robô aspirador, 10 s, texto | US$ 2,35 | US$ 11,64 |
| 2. Panela, 20 s, texto | 4,70 | 23,28 |
| 3. Caixa de som, 6 s, imagem | 1,41 | 6,98 |
| 4. Mesa, 8 s, dois quadros | 1,88 | 9,31 |
| 5. Bolsa, 12 s, quatro imagens | 2,82 | 13,97 |
| 6. Relógio, 5 s de referência e 8 s de saída | 2,256 | 9,08 |
| 7. Fundo do aspirador, 8 s de origem e de saída | 2,256 | 11,17 |
| 8. Capacete, 10 s de origem e de saída | 2,82 | 13,97 |
| Total | 20,492 | 99,41 |

As linhas de edição do Seedance supõem uma saída do tamanho do vídeo de origem, porque a edição põe a duração em `auto`. Para iterar no Seedance, o artigo sugere fechar o prompt a 480p, onde 10 s custam cerca de US$ 2,21; o final a 1080p é uma geração nova, porque "the US input schemas list no draft setting to carry a take over".

**Qual escolher, na visão do autor.** A divisão dele segue dois eixos, o acesso e a taxa. Quem precisa chamar o modelo por API hoje vai ao Seedance 2.5, e quem gera no playground ou no fal Agent pode ficar com o Kling 4.0, mais barato a 1080p, o que pesa em clipes longos. Os recursos desempatam o resto: pedem o Kling as tomadas com prompt e duração próprios (`multi_prompt`), o apresentador recorrente com o mesmo rosto e a mesma voz (elementos com `voice_id`) e um sotaque que a Kling lista; pedem o Seedance o áudio como referência (jingle, locução), mais de 10 imagens ou mais de 5 vídeos de referência, a saída a 480p ou em 4:3 e 3:4, a semente nos pedidos de referência e o H.265. Os dois juntos servem quando lotes automáticos precisam da API do Seedance e peças longas feitas à mão podem ir ao Kling no playground.

**Fim do artigo.** Links para as páginas dos dois modelos, explicadores, um guia de fluxos do Seedance 2.5 com 25 briefings de exemplo e uma comparação Seedance 2.5 contra 2.0. O FAQ retoma números da tabela (preço, quantidade de referências, som, edição) e acrescenta duas coisas: para comércio eletrônico, nenhum dos dois vence sozinho; e os direitos de uso exatos estão nos termos de serviço da fal, embora as páginas dos dois endpoints marquem uso comercial. Fecha com a biografia do autor.

**Contradição dentro do artigo.** As oito linhas da coluna do Seedance somam US$ 99,40; o total impresso é 99,41.

**O que o artigo não diz.** O preço do Kling 4.0 Flash; a data em que a API do Kling 4.0 abre; nada sobre rosto ou pessoa real como referência.

## Como a fal cobra, pelo que as quatro páginas dizem

O texto visível fala em pagar por segundo "with no minimums" (FAQ do Veo 3.1), em servidor que "scales to zero", em pegar a chave de API no painel, e diz que a fal dá acesso ao Veo 3.1 sem conta no Google Cloud. Nenhuma das páginas diz se a cobrança é por crédito comprado antes ou por fatura depois do uso, nem fala em limite de gasto: é lacuna. No payload, sem texto que os explique: o `endpointBilling` de cada endpoint traz `balance_check: false`, `provider_type: "partner"` e `is_partner_api: true`; e as quatro páginas trazem as chaves de configuração `paywall-credit-plans: true` e `credit-checkout-invoice-first: true`.
