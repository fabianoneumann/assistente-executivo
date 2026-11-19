---
titulo: "Replicate: páginas de modelo bytedance/seedance-2.5, google/veo-3.1, kwaivgi/kling-v4.0 e kwaivgi/kling-v3-video"
tipo: artigo
autor: "Replicate (páginas de modelo oficial, com README)"
url: "https://replicate.com/bytedance/seedance-2.5"
publicado_em: 2026-11-10   # version.created_at da versão atual do bytedance/seedance-2.5, no JSON da página ("Model updated 21 hours ago")
capturado_em: 2026-11-11
licenca: "protegida: a página de modelo do Replicate não declara licença do texto; valem os termos do site. Ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [replicate, aggregator, api-pricing, seedance, veo, kling, video-generation, image-to-video, first-last-frame, reference-to-video, video-editing, motion-transfer]
---

# Replicate: o que as páginas de Seedance 2.5, Veo 3.1, Kling 4.0 e Kling 3.0 aceitam e cobram (novembro de 2026)

**Proveniência.** Quatro páginas de modelo do Replicate, baixadas como HTML com `curl` em 11/11/2026: https://replicate.com/bytedance/seedance-2.5 (a principal), https://replicate.com/google/veo-3.1, https://replicate.com/kwaivgi/kling-v4.0 e https://replicate.com/kwaivgi/kling-v3-video. De cada uma, o README foi lido inteiro no texto extraído do HTML, e dois blocos JSON embutidos no HTML foram tirados por script (`json.JSONDecoder().raw_decode`): a tabela de preço, na chave `billingConfig.current_tiers` (num `<script>` de tipo `application/json` dentro da `<section id="pricing">`), e o esquema de entrada da versão atual, em `version._extras.dereferenced_openapi_schema.components.schemas.Input`. Ficaram de fora os vídeos de exemplo, o playground e a navegação do site.

**Quem fala.** O Replicate, que revende os modelos dos fabricantes; as quatro páginas marcam o modelo como oficial (`is_official: true`) e não dizem quem escreveu o README.

**Datas.** O texto visível só traz datas relativas; a data absoluta é a da versão atual no JSON (`version.created_at`).

| Página | Criado / atualizado (texto da página) | Versão atual | Execuções |
|---|---|---|---|
| `bytedance/seedance-2.5` | 3 months ago / 21 hours ago | 2026-11-10 | 374K |
| `google/veo-3.1` | over 1 year ago / 7 months, 2 weeks ago | 2026-03-25 | 678.5K |
| `kwaivgi/kling-v4.0` | 2 weeks, 5 days ago / 21 hours ago | 2026-11-10 | 17.9K |
| `kwaivgi/kling-v3-video` | 8 months, 3 weeks ago / 21 hours ago | 2026-11-10 | 660.1K |

**Como ler os preços.** Em todas as páginas a unidade da tabela é a mesma, a métrica `video_output_duration_seconds` ("per second of output video"), e cada faixa traz ao lado uma conversão em quantos segundos dá um valor em dólar; o que muda de uma página para outra são os critérios que separam as faixas.

## Seedance 2.5 (`bytedance/seedance-2.5`)

**Modos.** Um modelo só cobre cinco usos: vídeo a partir de texto; a partir de imagem (`image` é o primeiro quadro, e `last_frame_image`, opcional, fixa onde o vídeo termina); composição a partir de referências mistas; edição de um vídeo (troca de objeto, de fundo ou de estilo, mantendo o movimento e a câmera do original); e continuação de um vídeo. O som sai na mesma geração que a imagem.

**Referências.** Imagens até 30 (`reference_images`), vídeos até 10 (`reference_videos`) e áudios até 10 (`reference_audios`); no caso de vídeos e de áudios, a soma das durações de cada grupo não passa de 30 s. No prompt, cada uma é chamada pela posição, como [Image1], [Video1], [Audio1]. Pelo esquema, os vídeos de referência servem a "motion transfer, style reference, editing, and extension"; o áudio de referência só entra com pelo menos uma imagem ou um vídeo de referência; e o par de quadros (primeiro e último) não se mistura com nenhuma referência, sendo que o último quadro exige o primeiro. O prompt é opcional quando há mídia de entrada.

**Duração, resolução e proporção.** `duration` vai de -1 a 30 (padrão 5); -1 deixa o modelo escolher o tamanho, e o modo de edição o exige (o README fala em 4 a 30 s, ou -1). `resolution` aceita só `480p` e `720p` (padrão 720p). `aspect_ratio`: 16:9 (padrão), 4:3, 1:1, 3:4, 9:16, 21:9 ou `adaptive`, que é obrigatório no par de quadros, na edição e na continuação. Saída em mp4 ou mov; marca d'água opcional (`watermark`, desligada por padrão); `seed` sem garantia de repetir o resultado.

**Áudio.** `generate_audio` vem ligado; desligado, sai vídeo mudo. Fala posta entre aspas duplas no prompt vira voz com o movimento dos lábios.

**Recomendações do README.** Para gastar menos enquanto se acerta o estilo, clipes de 5 s, alongados só depois. Para controlar o resultado, o prompt detalha câmera, luz, clima e ação, diz para que serve cada referência citada e, na edição, separa o que muda do que fica.

**Preço** (`billingConfig.current_tiers`, critérios `model variant` e `target resolution`):

| `model variant` | Resolução | Por segundo de vídeo de saída | Conversão ao lado |
|---|---|---|---|
| `non_video_in` | 480p | US$ 0,1028 | cerca de 97 s por US$ 10 |
| `video_in` | 480p | US$ 0,4304 | cerca de 23 s por US$ 10 |
| `non_video_in` | 720p | US$ 0,2312 | cerca de 43 s por US$ 10 |
| `video_in` | 720p | US$ 0,9676 | cerca de 10 s por US$ 10 |

**O que a página não diz.** O que faz um pedido cair em `video_in` (só `reference_videos`, ou também as imagens e os áudios de referência); se os segundos do vídeo de entrada entram na conta (a métrica da tabela é só a saída); quanto se cobra quando a duração é -1; se o áudio muda o preço (a tabela não tem critério de áudio). A palavra "draft" não aparece no HTML da página. Sobre rosto, o README só diz que, com imagens de referência, o modelo mantém rostos, roupa e estilo ao longo do vídeo; nada sobre pessoa real.

## Veo 3.1 (`google/veo-3.1`)

**Entradas.** Prompt obrigatório; `image` para partir de uma imagem (o esquema indica como ideais 16:9 ou 9:16, em 1280x720 ou 720x1280); `last_frame` para uma transição entre a imagem inicial e a final; `reference_images`, de 1 a 3, para manter sujeito, aparência e estilo; `negative_prompt`; `seed`. Com imagens de referência, o esquema impõe 16:9 e 8 s e descarta o último quadro.

**Saída.** 4, 6 ou 8 s (padrão 8); 720p ou 1080p (padrão 1080p); 16:9 ou 9:16; 24 fps, pelo README. O som vem ligado (`generate_audio`). Todo vídeo leva a marca d'água SynthID. O README cita uma variante Fast e a montagem de sequências longas encadeando gerações, mas o esquema não tem parâmetro de extensão.

**Recomendações do README.** O par de quadros funciona melhor quando as duas imagens combinam entre si e o caminho de uma à outra é fisicamente possível. Partindo de uma imagem, o prompt fala do movimento, não do que a imagem já mostra. O som se orienta descrevendo-o no prompt, junto de câmera, luz e clima.

**Preço** (`billingConfig.current_tiers`, critério único `model variant`):

| `model variant` | Por segundo de vídeo de saída | Conversão ao lado |
|---|---|---|
| `with_audio` | US$ 0,40 | 25 s por US$ 10 |
| `without_audio` | US$ 0,20 | 50 s por US$ 10 |

**O que a página não diz.** A tabela não separa 720p de 1080p, e nada no texto diz se a resolução muda o preço. A página não diz nada sobre rosto ou pessoa real.

## Kling 4.0 (`kwaivgi/kling-v4.0`)

**Um modelo para todos os modos.** O README apresenta o 4.0 como a junção, num modelo, dos trabalhos que as versões anteriores dividiam (texto para vídeo, imagem para vídeo, Omni); o modo sai das entradas que se passam.

**Entradas.** Texto; quadros-chave (`start_image`, quantos `middle_images` se quiser, em ordem, e `end_image`), caso em que a proporção vem das imagens; imagens de referência (`reference_images`) para personagem, produto, lugar ou estilo; vídeos de referência (`reference_videos`) para emprestar câmera, movimento ou estilo; e `base_video` para editar um vídeo existente, com a saída do mesmo tamanho e proporção do original (a duração pedida é ignorada). No prompt, imagens são `@image_1`, `@image_2`..., numeradas na ordem `start_image`, `middle_images`, `end_image`, `reference_images`; vídeos são `@video_1`..., com o `base_video` primeiro.

**Limites.**

| Entrada | Quantos | Duração | Arquivo |
|---|---|---|---|
| Imagens (quadros e referências somados) | até 10 | — | até 30 MB, mínimo de 300 px, proporção de 2:5 a 5:2 |
| Vídeos (`base_video` e `reference_videos` somados) | até 5 | 3 a 30 s cada, 30 s no total | .mp4 ou .mov, 700 a 4553 px por lado, até 300 MB, proporção de 2:5 a 5:2 |
| Prompt | — | — | até 26.000 caracteres em inglês, 11.000 em outras línguas |

**Saída.** De 3 a 30 s (padrão 5); 720p ou 1080p (padrão 1080p); 16:9, 9:16, 1:1 ou 21:9, proporção ignorada quando há imagem de quadro ou `base_video`.

**Preço** (`billingConfig.current_tiers`, critérios `model variant` e `target resolution`):

| `model variant` | Resolução | Por segundo de vídeo de saída | Descrição da faixa / conversão |
|---|---|---|---|
| `no-video-input` | 720p | US$ 0,157 | texto ou imagem; cerca de 63 s por US$ 10 |
| `no-video-input` | 1080p | US$ 0,235 | texto ou imagem; cerca de 42 s por US$ 10 |
| `video-input` | 720p | US$ 0,094 | regra de segundos abaixo; "or around 10 seconds for $1" |
| `video-input` | 1080p | US$ 0,141 | regra de segundos abaixo; cerca de 70 s por US$ 10 |

**Regra dos segundos cobrados com vídeo de entrada.** O JSON a dá na descrição das duas faixas com vídeo: "Billed seconds: 2x output if input is shorter than output, otherwise input + output". A seção de preço do README diz o mesmo de outro jeito (a saída mais o maior entre a entrada e a saída) e dá o exemplo: "editing a 5 second video into a 5 second output bills 10 seconds". Qualquer vídeo de entrada aciona essa faixa, seja `base_video`, seja `reference_videos`.

**O que a página não diz.** Nada sobre áudio: o README não o menciona e o esquema não tem parâmetro de som. Nada sobre rosto ou pessoa real. A página aponta, sem resumir, para a política de privacidade, os termos da API e o acordo de nível de serviço da Kling (`app.klingai.com`).

## Kling 3.0 (`kwaivgi/kling-v3-video`)

**Entradas.** Texto (até 2.500 caracteres) ou imagem inicial (`start_image`: .jpg/.jpeg/.png, até 10 MB, no mínimo 300 px, proporção de 1:2.5 a 2.5:1), com imagem final opcional (`end_image`, que exige a inicial); `negative_prompt` até 2.500 caracteres. O modo de várias tomadas (`multi_prompt`) recebe um JSON com até 6 tomadas, cada uma com prompt e duração de pelo menos 1 s, e a soma tem de ser igual à duração do vídeo.

**Saída.** De 3 a 15 s (padrão 5). `mode` decide a resolução: `standard` 720p, `pro` 1080p (o padrão), `4k`. Proporção 16:9, 9:16 ou 1:1, ignorada quando há imagem inicial. Som nativo opcional (`generate_audio`, desligado por padrão), com diálogo sincronizado aos lábios.

**Limites que o README declara.** Duração: 15 s é o teto, e o que for mais longo sai de clipes emendados. Consistência: o mesmo personagem pode mudar de uma geração para outra, e interações físicas complexas podem sair artificiais. Som: rende melhor em inglês e chinês.

**Preço** (`billingConfig.current_tiers`, critérios `with audio` e `model variant`):

| `model variant` | Sem áudio | Com áudio |
|---|---|---|
| `standard` (720p) | US$ 0,168 (cerca de 59 s por US$ 10) | US$ 0,252 (cerca de 39 s) |
| `pro` (1080p) | US$ 0,224 (cerca de 44 s) | US$ 0,336 (cerca de 29 s) |
| `4k` | US$ 0,42 (cerca de 23 s) | US$ 0,42 (cerca de 23 s) |

Todas as faixas são por segundo de vídeo de saída; no 4K, o preço é o mesmo com e sem áudio.

**Contradição dentro da página.** O README lista o `mode` só como "standard (720p) or pro (1080p)" e diz que o modelo gera "at up to 1080p resolution"; o esquema da mesma página aceita `4k` ("'4k' generates 4K") e a tabela de preço tem faixas de 4K.

**O que a página não diz.** Nada sobre rosto ou pessoa real.

## Como o Replicate cobra, pelo que as quatro páginas dizem

O texto visível fala só em pagar por segundo de vídeo de saída (o README do Kling 4.0 abre a seção com "You pay per second of video") e converte cada faixa em segundos por dólar. Nenhuma das quatro páginas diz se a cobrança é por crédito comprado antes ou por fatura depois do uso, nem fala em valor mínimo, limite de gasto ou recarga: é lacuna. No JSON, sem texto que os explique, aparecem: `requiresCredit: true` no componente do playground; `has_special_pricing: true`; um campo `hardware: "CPU"` com `price: "$0.0001 per second"` e um `p50price` (Seedance 2.5 `"$0.017"`, Veo 3.1 `"$0.0095"`, Kling 4.0 `"$0.025"`, Kling 3.0 `"$0.013"`); e a dica de tela "Official models are always on, maintained, and have predictable pricing."
