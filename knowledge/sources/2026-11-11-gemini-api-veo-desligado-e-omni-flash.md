---
titulo: "Generate and edit videos with Gemini Omni Flash"
tipo: artigo
autor: "Google AI for Developers"
url: "https://ai.google.dev/gemini-api/docs/omni"
capturado_em: 2026-11-11
licenca: "em dúvida: as três páginas foram lidas na versão .md.txt, que não traz rodapé; o HTML redireciona para aistudio.google.com/docs, app em JavaScript, sem rodapé no que o curl devolve; falta conferir no Chrome se o texto é CC BY 4.0, como a documentação do Google Cloud. Tratada como protegida: ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [gemini-omni, veo, video-generation, video-editing, image-to-video, first-last-frame, video-extension, reference-images, real-face-restriction, model-deprecation]
---

# Gemini API em novembro de 2026: o Veo 3.1 desligado e o Gemini Omni Flash no lugar

**Proveniência.** Três páginas da documentação da Gemini API (Google AI for Developers), baixadas com `curl` em 11/11/2026 na versão markdown oficial, pelo endereço da página com `.md.txt` no fim:

- https://ai.google.dev/gemini-api/docs/omni (principal): o guia "Generate and edit videos with Gemini Omni Flash". Lidos inteiros a prosa, a tabela de resolução, os avisos e as duas respostas JSON da REST; dos exemplos de código (Python, JavaScript, Java, Go, REST e a CLI `gemini-api`), só os nomes de parâmetro, levantados por busca no arquivo.
- https://ai.google.dev/gemini-api/docs/video: o guia "Video generation in the Gemini API", página curta, lida inteira.
- https://ai.google.dev/gemini-api/docs/changelog: as notas de versão ("Release notes"), 150 entradas de 13/12/2023 a 10/11/2026. Lidas inteiras as que tratam de geração de vídeo (Veo e Gemini Omni) e, numa linha, as outras de vídeo; o resto numa linha no fim.

Cada arquivo abre com um bloco "AI Agent Context" que aponta para o índice da documentação em `aistudio.google.com/llms.txt`. Nenhuma das três páginas tem data própria; a entrada mais recente do changelog é de 10/11/2026. As páginas remetem aos preços da Gemini API (https://ai.google.dev/gemini-api/docs/pricing), que têm ficha própria na base; os preços não estão nestas três.

**Quem fala.** O Google, fabricante, na documentação da API.

## O guia de vídeo: o Veo saiu da Gemini API

Desde **22 de outubro de 2026** a Gemini API não tem mais Veo: os três IDs de prévia, `veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview` e `veo-3.1-lite-generate-preview`, foram desligados ("The Veo 3.1 Preview in the Gemini API has been shut down."). A página de geração de vídeo indica duas saídas, o Gemini Omni Flash (`gemini-omni-1.2-flash`), que ela passa a apresentar como o modelo de geração e de edição conversacional de vídeo da API, e os modelos GA da Gemini Enterprise Agent Platform, com link para a página do Veo 3.1 no Google Cloud. Fora isso, traz um resumo do Omni Flash (vídeos de 3 a 15 s com áudio nativo, até 6 imagens de referência, edição e extensão em vários turnos pela Interactions API) e manda quem quer analisar vídeo, e não gerar, para o guia de entendimento de vídeo.

## O guia do Gemini Omni Flash, na ordem da página

**O modelo.** Para o guia, o `gemini-omni-1.2-flash` junta três coisas: entrada multimodal (texto, imagem e vídeo) com saída de vídeo e áudio sincronizados de até 15 s; edição e extensão conversacionais pela Interactions API; e personagens e objetos mantidos entre planos com até 6 imagens de referência, somados ao que o modelo entende de física e do mundo. Estado (GA ou Preview) e data de lançamento não aparecem no guia. O 1.1 continua respondendo numa transição de quatro semanas; a partir de **3 de dezembro de 2026**, o que for pedido ao `gemini-omni-1.1-flash` cai no 1.2 sem mudança de código, e a cobrança passa à tabela do 1.2, "lower" segundo a página.

**Texto para vídeo e a resposta.** Só o prompt, em `client.interactions.create`, já devolve vídeo com áudio, e cena, câmera, luz e clima descritos no texto melhoram o resultado. Quem chama a REST direto lê o vídeo no array `steps` (um passo `model_output`, `mime_type` `video/mp4`, dados em base64), porque `interaction.output_video` só existe nos SDKs.

**Proporção, resolução e duração**, os três em `response_format`:

- `aspect_ratio`: `"16:9"` por padrão (paisagem) e `"9:16"` para retrato; os comentários dos exemplos de código dão só esses dois como aceitos.
- `resolution`: `360p`, `720p` (padrão), e `1080p` e `4k` feitos por upscaling.
- `duration`: inteiro de 3 a 15 s (escrito `"15s"`), 10 s se omitido; vale mais que uma duração escrita no prompt; acima de 15 s, erro de argumento inválido. Com primeiro e último quadro, ou num turno de extensão, o teto cai para 10 s, e quantos vídeos de referência cabem depende da duração (em "Limites", abaixo).

**Imagem para vídeo.** A imagem entra ao lado do prompt, e é o texto que decide o papel dela: no exemplo da página, um desenho de peixe saltando vira filmagem realista com "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video". Rende mais com imagem em alta resolução e com câmera, sujeito e ambiente descritos; "make it move" é o contraexemplo.

**Primeiro e último quadro.** O teto é de 10 s (com duas imagens e duração maior, erro de argumento inválido; com uma imagem só, até 15 s): as duas imagens vão na lista `input`, e o prompt descreve a passagem de uma à outra.

**Referência de sujeito.** No máximo seis imagens por pedido, em até 2 personagens com até 3 imagens cada, para segurar semelhança, roupa e objetos de um plano a outro (o exemplo junta um gato e um novelo).

**O parâmetro `task`.** O modo de geração e o papel de cada mídia, o modelo tira do prompt; `task` em `video_config` (nos exemplos de código, dentro de `generation_config`) é a reserva para quando o prompt não basta, com os valores `text_to_video`, `image_to_video`, `reference_to_video`, `edit` e `extend`. A página desaconselha começar por ele, porque impõe amarras (limita as imagens de entrada, trava a combinação das mídias), e declara obsoletas as marcas de controle no prompt (`<FIRST_FRAME>`, `<LAST_FRAME>`, `<IMAGE_REF_0>`, `<VIDEO_REF_0>`), que os modelos futuros não vão aceitar: o papel de cada mídia se diz em palavras.

**Edição com estado.** Encadeados pelo `previous_interaction_id`, os turnos geram cada um um vídeo novo sobre o anterior, e o que o pedido não mencionou fica como estava (mudar a luz e trocar o fundo são os exemplos); vídeos gerados de até 15 s se editam assim sem reenvio.

**Editar um vídeo próprio.** Vale para vídeo de até 15 s, enviado pela Files API (a página a prefere ao base64 por causa do tamanho), e a função não está disponível em todas as regiões.

**Receber por URI.** Para vídeo acima de 4 MB, a página indica receber por endereço: `delivery="uri"` em `response_format` devolve um URI do Google, a consultar até o estado `ACTIVE`. Esse endereço só é garantido na resposta de criação ou no stream SSE; consultado depois por `GET /v1beta/interactions/{id}`, o vídeo volta em base64 no campo `data`.

**Extensão.** O que se estende: o vídeo gerado antes (pelo `previous_interaction_id`) ou um vídeo enviado, inclusive clipes de 15 s, com 3 a 10 s a mais por turno (10 por padrão, ou o `duration`) e no máximo 30 s no total; o pedido diz como a cena continua ("Extend this video"), e imagens de referência no `input` podem trazer personagens ou elementos novos. O que limita: só se acrescenta no fim, nunca no começo nem no meio; o modelo toma como contexto os 10 s finais, então o que só aparecia antes disso precisa voltar no prompt ou como referência; num vídeo enviado em que alguém fala não se acrescenta diálogo (calado, ou sem fala nova no prompt, pode), enquanto o vídeo gerado, estendido por turnos, aceita fala; e no Espaço Econômico Europeu, na Suíça e no Reino Unido não se estende vídeo enviado, só o gerado.

**Boas práticas.** Para geração síncrona mais rápida, `background=false`, `store=false` e `stream=false`, com o porém de que `store=false` tira a chance de editar aquele vídeo nos turnos seguintes; e URI para o que passar de 4 MB.

## Limites, restrições e detalhes técnicos

- **Vídeos e imagens de referência:** de 11 a 15 s, cabe 1 vídeo de referência de até 3 s; de 3 a 10 s, até 3 vídeos de referência de até 3 s cada; imagens de referência, até 6 em qualquer duração. Vídeo de referência "work best for visual likenesses", o áudio dele é ignorado, e só vale para gerar vídeo novo, não para editar nem estender; imagem de referência vale para gerar, editar e estender por prompt. Raciocinar sobre vários vídeos ao mesmo tempo não é suportado e pode degradar o resultado.
- **Duração dos vídeos de entrada:** até 15 s para edição, sejam enviados ou gerados.
- **Pessoas e regiões:** "Uploading and editing images containing certain recognizable people is not supported." Imagens com menores não podem ser enviadas nem editadas no Espaço Econômico Europeu, na Suíça e no Reino Unido; nessas regiões também não se edita nem se estende vídeo enviado (o gerado, sim).
- **O que não existe nesta versão:** edição de voz; envio de áudio como entrada ou referência; vazão provisionada; instrução de sistema, `temperature`, `top_p`, sequências de parada e prompt negativo como parâmetro (o negativo vai no texto do prompt, "Do not do X"); vídeo do YouTube como fonte.
- **Técnico:** todo vídeo gerado leva marca d'água SynthID, invisível e detectável por programa; o tempo de geração varia com duração, resolução e carga da API; há filtros de segurança no prompt e no vídeo, que variam por região; o inglês é plenamente suportado, e as outras línguas "have not been evaluated", podendo funcionar com resultados variáveis.

## O guia de prompt da página

**O que o modelo faz se o prompt não disser:** monta um vídeo com alguns planos e tenta dar a ele uma narrativa, e cria uma trilha de áudio por conta própria. Quem quer uma cena só precisa pedir ("In a single continuous shot", "No scene cuts"); quem quer música precisa descrevê-la.

**O que se escreve no prompt:**

- Negativos simples para tirar o indesejado ("No dialogue", "No extra sound effects").
- Momentos marcados, em linguagem natural ("After 3 seconds, a woman enters the scene") ou em trechos de tempo (`[0-5s]`, `[5-10s]`, `[10-15s]`); um dos exemplos pede troca de cena a cada meio segundo, "12 frames at 24fps".
- Pedidos de qualidade geral, o "meta-prompt": microdetalhe, expressão, figurino, fundo rico.
- Texto na tela, que o modelo escreve legível quando pedido; convém dizer o que deve estar escrito até em placas e letreiros do fundo.

**Na edição e na extensão:** o prompt curto funciona melhor, e o muito descritivo provoca mudanças não pedidas; para mexer numa coisa só, fechar com "Keep everything else the same" (a página mostra dois pares de prompt a evitar e prompt simplificado: um gato que pula no colo, um celular que some da mão). Ao estender, valem as mesmas dicas (dizer como o áudio continua, se há corte de cena, usar imagem de referência), e, na marcação de tempo, 0 s é o começo do trecho novo. A página avisa que a emenda mexe no fim do original: "Some of the final frames in your input video will be edited to make the transition seamless."

## O changelog: as entradas sobre geração de vídeo

| Data | Entrada |
|---|---|
| 05/11/2026 | GA do Gemini Omni 1.2 Flash (`gemini-omni-1.2-flash`): vídeo de até 15 s e edição conversacional; primeiro e último quadro de 3 a 10 s; extensão de 3 a 10 s por turno, até 30 s; consistência de personagem e sujeito com até 6 imagens de referência; saída de vídeo 30% mais barata, a US$ 12,00 por milhão de tokens; limites de uso do nível pago dobrados. Na mesma data, o aviso de que o `gemini-omni-1.1-flash` passa ao 1.2, com o preço do 1.2, a partir de 03/12/2026. |
| 27/08/2026 | GA do `gemini-omni-1.1-flash`, com extensão (tarefa `extend` ou só o prompt), interpolação de primeiro e último quadro (tarefa `image_to_video` com até 2 imagens) e o parâmetro `resolution` em `video_config` (`360p`, `720p` padrão, `1080p` e `4k`, os dois últimos por upscaling). O endpoint `gemini-omni-flash-preview` seria descontinuado em 30/09/2026. |
| 30/06/2026 | Omni Flash em prévia pública (`gemini-omni-flash-preview`): vídeos de 3 a 10 s a 720p, a partir de texto ou de imagem parada, com edição conversacional, pela Interactions API. |
| 15/06/2026 | Aviso de desligamento, em 30/06/2026, de `veo-2.0-generate-001`, `veo-3.0-generate-001` e `veo-3.0-fast-generate-001`; a migração indicada era para os IDs de prévia do Veo 3.1 (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) ou para os modelos 3.1 GA da Gemini Enterprise Agent Platform. |
| 31/03/2026 | Lançamento do Veo 3.1 Lite Preview (`veo-3.1-lite-generate-preview`), descrito como o modelo de geração de vídeo de menor custo, para iteração rápida e alto volume. |
| 13/01/2026 | Saída em 4k para o Veo e mais suporte a vídeo em retrato em todas as resoluções. |
| 11/11/2025 | Aviso de desligamento de `veo-3.0-fast-generate-preview` e `veo-3.0-generate-preview` em 12/11/2025. |
| 15/10/2025 | Veo 3.1 e 3.1 Fast em prévia pública, com extensão de vídeos do Veo, referência a até três imagens e primeiro e último quadro; o Veo 3 ganha durações de 4, 6 e 8 s; e o anúncio do desligamento das prévias do Veo 3.0 em 12/11/2025. |
| 09/09/2025 | GA do Veo 3 e do Veo 3 Fast, com preço mais baixo (a entrada não dá valores) e novas opções de proporção, resolução e semente. |
| 07/08/2025 | A configuração `allow_adult` na geração de imagem para vídeo passa a valer nas regiões restritas. |
| 31/07/2025 | Imagem para vídeo no Veo 3 Preview e lançamento do Veo 3 Fast Preview. |
| 17/07/2025 | Lançamento do `veo-3.0-generate-preview`, que a entrada descreve como a atualização do Veo que introduz a geração de vídeo com áudio. |
| 09/04/2025 | GA do `veo-2.0-generate-001`, de texto e imagem para vídeo. |

O changelog não tem entrada sobre o desligamento do Veo 3.1 Preview. As outras entradas sobre vídeo tratam de vídeo como entrada, não de geração: vídeo aceito nas respostas de função (05/11/2026), entendimento de vídeo agêntico com até 88% menos tokens em conteúdo longo (01/09/2026), geração de imagem a partir de vídeo no `gemini-3.1-flash-image` (28/05/2026), além de suporte a vídeo em versões antigas da API.

**O resto do changelog, fora desta ficha:** lançamentos e descontinuações de modelos de texto (Gemini 4 Carbon e Argon, 3.x, 2.x), de imagem (Nano Banana, Imagen), de voz e música (TTS, Lyria), embeddings, agentes (Deep Research, Computer Use), a CLI `gemini-api`, armazenamento de pedidos e mudanças de API e de arquivos aceitos.

## O que as três páginas não dizem

- Preço do Omni em dinheiro por segundo e quantos tokens conta um segundo de vídeo: o guia do Omni não traz nenhum dos dois e remete à página de preços; o changelog dá só o preço por milhão de tokens.
- Taxa de quadros do vídeo gerado: o único "24fps" do guia está dentro de um exemplo de prompt.
- Tamanho máximo do arquivo enviado e formatos de vídeo e imagem aceitos na entrada.
- Quais regiões, além do Espaço Econômico Europeu, da Suíça e do Reino Unido, ficam sem a edição de vídeo enviado ("not available in all regions").
- Que pessoas reconhecíveis ("certain recognizable people") são barradas, nem se a regra vale para vídeo enviado, além de imagem.
- Estado e data do Omni 1.2 no próprio guia (vêm só no changelog), e o que acontece com chamadas feitas aos IDs do Veo 3.1 Preview depois de 22/10/2026.
