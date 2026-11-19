---
titulo: "Video models | Higgsfield API (com a documentação da API, a página de modelos do Enterprise Help Center, o guia 'Which AI model should I use?', o blog do Genjutsu e o changelog)"
tipo: artigo
autor: "Higgsfield"
url: "https://open.higgsfield.ai/explore/video"
capturado_em: 2026-11-11
licenca: "protegida: as páginas do site higgsfield.ai trazem '© 2026 Higgsfield, Inc. All rights reserved.' no rodapé; o catálogo da Higgsfield API e o Markdown da documentação (docs.higgsfield.ai) não declaram licença e valem os termos do site. Ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [higgsfield, aggregator, video-generation, api-pricing, genjutsu, motion-transfer, video-editing, cinema-studio, soul-id, character-consistency, first-last-frame, kling, seedance, veo, wan, mcp]
---

# Higgsfield em novembro de 2026: o catálogo de vídeo, os recursos próprios e o que as páginas dizem do que roda por baixo

Ficha de sete páginas da Higgsfield, todas protegidas: em palavras próprias, com poucas citações curtas e sem o texto integral. Cada página tem a sua seção e a sua proveniência; a `url` do frontmatter é o catálogo de vídeo da API, a página principal, que não traz data de publicação (por isso o campo `publicado_em` fica fora).

**Proveniência comum.** As sete páginas foram baixadas em 11/11/2026 pelo script da rodada (`curl -fsSL` com user agent de navegador): as páginas do site e o catálogo como HTML, as duas da documentação como o Markdown que a própria documentação serve (a URL com `.md`, documentação hospedada no Mintlify). O texto foi lido na extração do HTML; os dados que a extração descarta (o JSON embutido do catálogo, as datas em JSON-LD) foram lidos no HTML baixado.

**Quem fala.** A Higgsfield, em todas: é a empresa que revende modelos de outros fabricantes (ByteDance, Kling, Google, Alibaba e outros) e que tem recursos próprios (Genjutsu, Cinema Studio, Soul, 3D Jutsu). O que as páginas atribuem a um fabricante ("per Kling", "per ByteDance") é a Higgsfield repassando o que o fabricante diz.

**Cobertura.** (1) O catálogo de vídeo da API: os 24 cartões que o HTML baixado traz, inteiros, com o preço, a data de lançamento e o modo padrão de cada um; a página declara 26 itens, e os dois da segunda página não foram lidos. (2) O índice de vídeo da documentação da API e a página do Genjutsu na documentação, inteiros. (3) A página "Generation Models" do Enterprise Help Center, inteira (o menu e o rodapé, não). (4) O guia "Which AI model should I use?", inteiro. (5) O post do blog sobre o Genjutsu, inteiro (os links para outros posts no fim, não). (6) O changelog: das 174 entradas (24/01 a 09/11/2026), as de vídeo, as de modelo de vídeo e as que tratam do Genjutsu, do Cinema Studio, do Soul ID e dos Elements, do 3D Jutsu, do Draw to Video, do MCP e da API, inteiras e na ordem da página, menos as de modelos de linguagem que entram no MCP e as de apps e jogos montados pelo MCP (GPT-6 Sol e Luna, GPT-6 Astra, Grok Bot, Claude Fable 5, Claude Sonnet 5, Higgsfield Apps, Higgsfield Games), cobertas só no que toca ao MCP; as demais, numa linha no fim da seção.

## 1. O catálogo de vídeo da Higgsfield API

**Proveniência.** https://open.higgsfield.ai/explore/video, a página "Explore / Video" do console da Higgsfield API (o produto para desenvolvedores), baixada como HTML. A página não mostra data; o dado embutido marca a carga às 17:54 UTC de 11/11/2026 (`dataUpdatedAt`) e traz, para cada item, a data de lançamento (`released_on`), o preço exato (`amount`, em `USD`, `unit: "second"`) e se o preço é mínimo (`qualifier: "from"`) ou fixo (`"exact"`). O mesmo dado diz `count: 26` com `page_size=24` e aponta uma segunda página: o HTML traz só os 24 primeiros, e os outros dois ficam sem leitura.

**Como ler o preço.** O cartão mostra dólares por segundo de vídeo; "from" quer dizer o menor preço do modelo. A página não diz em que condição vale o mínimo (resolução, áudio, duração, vídeo de entrada) nem quanto custa a configuração mais cara.

| # | Fornecedor / modelo (como a página escreve) | Tipo | Selo | O que o cartão diz que faz (resumo) | Preço no cartão (US$/s) | `amount` no dado | `released_on` | Modo padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | bytedance / Seedance 2.5 | Video | | até 30 s; entra texto, imagem, vídeo ou áudio | from 0.118 | 0.1177 | 2026-07-01 | `bytedance/seedance-2.5/text-to-video` |
| 2 | higgsfield / Genjutsu Light | Video | Higgsfield Exclusive | movimento levado a personagens e cenas de referência; só os primeiros 15 s do vídeo-fonte; áudio da fonte mantido | from 0.050 | 0.05 | 2026-10-20 | `higgsfield/genjutsu-light/motion-transfer/v1.0` |
| 3 | higgsfield / Genjutsu | Video | Higgsfield Exclusive | troca personagem, lugar e estilo de um vídeo sem mexer no movimento | from 0.154 | 0.154 | 2026-09-17 | `higgsfield/genjutsu/motion-transfer/v1.0` |
| 4 | kling / Kling 4.0 | Video | | texto, imagens e vídeos de referência; até 30 s em 1080p; quadros-chave; edição de vídeo pronto | from 0.126 | 0.1257 | 2026-10-23 | `kling-video/v4.0/text-to-video` |
| 5 | kling / Kling 4.0 Flash | Video | | só texto, 720p; de 3 a 20 s; proporção 21:9, 16:9, 9:16 ou 1:1 | 0.094 | 0.094 (exact) | 2026-11-04 | `kling-video/v4.0-flash/text-to-video` |
| 6 | minimax / MiniMax H3 | Video | | 2K, até 15 s; referência de texto, imagem, vídeo e áudio opcional | 0.130 | 0.13 (exact) | 2026-07-01 | `minimax/h3/text-to-video` |
| 7 | alibaba / Wan 3.0 Prime | Video | | texto ou mídia de referência, processamento rápido, até 30 s | from 0.051 | 0.051 | 2026-08-24 | `alibaba/wan-3.0-prime/text-to-video` |
| 8 | bytedance / Seedance 2.0 | Video | | 4K de texto ou mídia de referência; até 15 s; som opcional | from 0.080 | 0.0804 | 2026-02-01 | `bytedance/seedance-2.0/text-to-video` |
| 9 | higgsfield / Cinema Studio 4.0 | Video | Higgsfield Exclusive | vídeo de tom cinematográfico, até 30 s, com direção de cena automática | from 0.123 | 0.1234 | 2026-09-18 | `higgsfield/cinema-studio/4.0` |
| 10 | higgsfield / Genjutsu | Workflow | Higgsfield Exclusive | movimento de um vídeo de referência levado a personagens, produtos ou roupas | from 0.318 | 0.318 | (vazio: `null`) | `higgsfiled/genjutsu/motion-transfer/v1.0` (grafia da página) |
| 11 | alibaba / Wan 3.0 | Video | | texto ou imagem, áudio nativo, duração ajustável até 30 s | from 0.038 | 0.0375 | 2026-08-24 | `alibaba/wan-3.0/text-to-video` |
| 12 | lightricks / LTX 2.5 Fast | Video | | texto ou imagem, áudio nativo, controle de movimento de câmera, 4K | from 0.090 | 0.09 | 2026-08-01 | `lightricks/ltx-2.5/text-to-video/fast` |
| 13 | lightricks / LTX 2.5 Pro | Video | | o mesmo, com saída em 1080p | from 0.120 | 0.12 | 2026-08-01 | `lightricks/ltx-2.5/text-to-video/pro` |
| 14 | xai / Grok Imagine Video 1.5 | Video | | de texto ou de imagem parada, 1080p, até 15 s | from 0.080 | 0.08 | 2026-07-01 | `xai/grok-imagine-video/v1.5/reference-to-video` |
| 15 | alibaba / Wan 2.7 | Video | | texto ou imagem, áudio nativo, personagem consistente entre cenas | from 0.075 | 0.075 | 2026-07-01 | `wan/v2.7/text-to-video` |
| 16 | alibaba / Happy Horse 1.1 | Video | | texto ou imagem de referência, 1080p, até 15 s | from 0.140 | 0.14 | 2026-06-01 | `alibaba/happy-horse/v1.1/text-to-video` |
| 17 | kling / Kling 3.0 | Video | | vários planos de texto ou imagem, áudio nativo, até 15 s | 0.071 | 0.0714 (exact) | 2026-06-01 | `kling-video/v3.0/std/text-to-video` |
| 18 | alibaba / Happy Horse 1.0 | Video | | texto ou imagem de referência, até 15 s, 1080p | from 0.140 | 0.14 | 2026-04-01 | `alibaba/happy-horse/text-to-video` |
| 19 | pixverse / PixVerse 6 | Video | | texto ou imagem, som nativo, controle do primeiro e do último quadro | "15 % OFF" 0.098 (de 0.115) | 0.0978 (exact; `original_amount` 0.115, `discount_percentage` 15, sem data de fim) | 2026-03-01 | `pixverse/v6/text-to-video` |
| 20 | kling / Kling O3 | Video | | gera e edita com imagem ou vídeo de referência, vários planos, som nativo | from 0.068 | 0.0683 | 2026-02-01 | `kling-video/o3/first-last-frame` |
| 21 | kling / Kling 2.6 | Video | | vídeo com som (diálogo, efeitos, ambiente) de texto ou imagem | 0.067 | 0.0666 (exact) | 2025-12-01 | `kling-video/v2.6/pro/text-to-video` |
| 22 | kling / Kling O1 (Omni) | Video | | gera e edita com imagem ou vídeo de referência; controle de quadro inicial e final | from 0.063 | 0.0632 | 2025-12-01 | `kling-video/omni/first-last-frame` |
| 23 | alibaba / Wan 2.6 | Video | | vários planos de texto ou imagem, som nativo, vídeo de referência opcional | from 0.075 | 0.0752 | 2025-12-01 | `wan/v2.6/text-to-video` |
| 24 | minimax / MiniMax Hailuo 2.3 | Video | | clipes curtos, corpo em movimento fluido e expressão facial natural | from 0.047 | 0.0467 | 2025-10-01 | `minimax/hailuo-2.3/standard/text-to-video` |

**O que mais o catálogo mostra.** O selo "Higgsfield Exclusive" (no dado, `is_exclusive`) está em quatro cartões: os dois Genjutsu, o Genjutsu Light e o Cinema Studio 4.0, todos com a empresa `higgsfield`. O Genjutsu aparece duas vezes, como modelo (o cartão 3) e como fluxo (o 10, `catalog_type: "workflow"`), com preço e descrição diferentes. Dos 24 lidos, nenhum é do Google (nada de Veo) nem da OpenAI.

**O Genjutsu Light, nas palavras do catálogo:** "Uses the first 15 seconds of the source video and preserves source audio." O nome que o catálogo usa é "Genjutsu Light" (`genjutsu-light`).

**O que roda por baixo, segundo esta página.** Nos cartões próprios (Genjutsu, Genjutsu Light, Cinema Studio 4.0) a empresa é a Higgsfield e o modo é da Higgsfield (`higgsfield/...`); a página não diz que modelo de base nenhum deles usa. Os demais cartões dão o fabricante no próprio nome.

## 2. A documentação da API: o índice de vídeo e a página do Genjutsu

**Proveniência.** https://docs.higgsfield.ai/docs/models/video-generation (título "Video Generation API") e https://docs.higgsfield.ai/docs/models/genjutsu (título "Genjutsu API"), lidas no Markdown que a documentação serve (`.md`). Nenhuma das duas traz data. As páginas de cada fluxo, para onde as duas apontam (os esquemas de entrada, os campos e os valores aceitos), não foram lidas.

**O índice de vídeo.** Diz ter 22 famílias de modelo e 67 entradas no catálogo, e cada cartão dá o rótulo da família, o número de fluxos e uma frase do que o modelo faz. As somas batem: os 22 cartões listados somam 67 fluxos.

| Rótulo da família | Modelo | Fluxos | Para que serve, pelo cartão |
|---|---|---|---|
| `HiggsfieldVideo` | Genjutsu | 3 | transferir movimento, substituir objeto ou mudar o estilo de um vídeo-fonte |
| `ByteDanceVideo` | Seedance 2.0 | 3 | vídeo de texto, de quadros, ou de referências de imagem, vídeo e áudio |
| `ByteDanceVideo` | Seedance 2.5 | 5 | gerar, editar e estender vídeo com texto e referências multimodais |
| `KlingVideo` | Kling 2.5 Turbo | 3 | variantes Standard e Pro |
| `KlingVideo` | Kling 2.6 | 2 | de texto ou de imagem inicial, som opcional |
| `KlingVideo` | Kling 2.6 Motion Control | 2 | movimento de um vídeo-fonte aplicado a uma imagem, Standard ou Pro |
| `KlingVideo` | Kling 3.0 | 8 | variantes Standard, Pro, 4K e Turbo |
| `KlingVideo` | Kling 3.0 Motion Control | 2 | o mesmo do 2.6 Motion Control |
| `KlingVideo` | Kling O3 | 4 | criar e editar com primeiro e último quadro, imagem e vídeo de referência |
| `KlingVideo` | Kling Omni | 4 | criar e editar com imagem e vídeo de referência |
| `AlibabaVideo` | Happy Horse 1.0 | 3 | de texto, imagem inicial ou imagens de referência |
| `AlibabaVideo` | HappyHorse 1.1 | 3 | o mesmo |
| `AlibabaVideo` | Wan 3.0 | 3 | de texto, de quadros ou de referências multimodais |
| `AlibabaVideo` | Wan 3.0 Prime | 3 | o mesmo, na versão Prime |
| `HiggsfieldVideo` | Cinema Studio 4.0 | 1 | planos com controle de câmera e de estilo e mídia de referência |
| `LightricksVideo` | LTX-2.5 | 4 | de texto ou imagem, variantes Fast e Pro |
| `MiniMaxVideo` | MiniMax H3 | 3 | de texto, de quadros ou de referências multimodais |
| `MiniMaxVideo` | Hailuo 2.3 | 2 | de texto ou imagem, na versão Standard |
| `PixVerseVideo` | PixVerse V6 | 2 | de texto ou imagem, som opcional |
| `AlibabaVideo` | Wan 2.6 | 3 | de texto, imagem ou vídeo de referência |
| `AlibabaVideo` | Wan 2.7 | 3 | de texto, de quadros ou de referências multimodais |
| `xAIVideo` | Grok Imagine Video 1.5 | 1 | de texto, imagem ou referência de áudio |

O índice não tem Kling 4.0 nem Veo, não dá preço e não descreve parâmetro; o roteiro de uso que ele dá é escolher o modelo e o fluxo, mandar o corpo JSON documentado com a credencial e buscar o resultado como o fluxo manda.

**A página do Genjutsu.** Três fluxos, cada um com o seu endpoint:

| Fluxo | Endpoint |
|---|---|
| Motion transfer | `POST /higgsfield/genjutsu/motion-transfer/v1.0` |
| Object swap | `POST /higgsfield/genjutsu/object-swap/v1.0` |
| Restyle | `POST /higgsfield/genjutsu/restyle/v1.0` |

A página não traz o esquema de entrada (ele está nas páginas de cada fluxo, não lidas), nem limite de duração, nem preço, nem menção ao Genjutsu Lite.

**O que roda por baixo, segundo estas páginas.** O Genjutsu e o Cinema Studio 4.0 estão na família `HiggsfieldVideo`; nenhuma das duas páginas diz que modelo de base eles usam.

## 3. Enterprise Help Center: "Generation Models"

**Proveniência.** https://higgsfield.ai/enterprise-help-center/platform/ai-models, baixada como HTML; a página mostra "Last updated Nov 1, 2026" (no JSON-LD, `dateModified` 2026-11-01). É a central de ajuda do plano Enterprise, em Models & Workflows. Fonte curta: organizada aqui pelo tipo de trabalho, e não pela lista de modelos da página.

**Para gerar um vídeo do zero.** O ponto de partida que a página dá é o Seedance 2.5: prompt ou referências, som gerado com a imagem, clipes de até 30 s, bom para cena com personagem, produto animado e planos encadeados. Para câmera de cinema, cena aberta e plano aéreo, o Veo (sem número de versão). Som sincronizado em clipe criativo: Grok Imagine. Imagens de personagem, referência de movimento e áudio num vídeo só, com diálogo e efeitos: MiniMax H3.

**Para conduzir o plano por quadros.** Quando se quer fixar tanto o quadro de abertura quanto o de fechamento, o guia aponta o Wan. Uma sequência guiada por quadros-chave, pelo Kling 4.0.

**Para levar o movimento de um vídeo a outro.** Duas indicações na mesma página: o Motion Transfer do Genjutsu, que aplica o movimento de um vídeo existente a outro personagem ou cena, e o Kling Motion Control: "Kling Motion Control remains the option for transferring movement from a reference video."

**Para editar um vídeo que já existe.** O Kling 4.0 edita um clipe pronto; o Object Swap do Genjutsu troca produto, roupa ou outro elemento. O Genjutsu Lite, nas palavras da página: "Genjutsu Lite is a lower-cost option for short Motion transfer or Objects swap tasks; use standard Genjutsu for Restyle or longer clips." A página não dá o limite de duração em segundos.

**Antes do vídeo final.** O Seedance 2.5 Draft serve para testar a ideia. O 3D Jutsu monta, de um prompt, uma cena 3D editável onde se posicionam objetos, se acerta a luz e se planeja a câmera.

**Para manter o personagem.** O Soul ID guarda uma identidade de rosto reutilizável; os Elements chamam personagens salvos "in supported models", sem dizer quais.

**O resto da página, numa linha cada.** Presets para começar (Viral Presets, foto que vira vídeo curto; Soul Photodump, um conjunto de fotos de um personagem Soul ID). Modelos de imagem: Higgsfield Soul 2.0 (pessoas, moda), GPT Image 2.5 (Flare e Sunburst), Nano Banana (Pro para instrução detalhada e texto), Seedream 5.0 Pro, Recraft V4.1, Ideogram Vector 1.0, Flux. Áudio: Voiceover, Change Voice, Translate, Voice Cloning, Seed Audio, Lipsync Studio e Higgsfield Intone. Antes de gerar: conferir o custo em créditos e as configurações; o que está disponível depende do plano e das permissões do workspace.

**O que roda por baixo, segundo esta página.** Nada sobre o modelo de base do Genjutsu, do Genjutsu Lite ou do 3D Jutsu. O Cinema Studio não aparece no corpo da página (só no menu).

## 4. O guia "Which AI model should I use?"

**Proveniência.** https://higgsfield.ai/creator-hub/help-center/ai-models/which-ai-model-should-i-use, na central de ajuda do Creator Hub, baixada como HTML. A página mostra "Aug 1, 2026"; o JSON-LD dá `datePublished` 2026-08-01 e `dateModified` 2026-11-06. Assinado "Higgsfield". Fonte curta: organizada aqui pelo que é da Higgsfield e pelo tipo de exigência do plano, e não pela tabela do guia.

**O que o guia diz que é da própria Higgsfield.** Três coisas: o Soul (família de imagem nativa, moda e cinema, com o Soul Cinema), o Popcorn (nativo, para storyboard e vários quadros encadeados) e o Higgsfield DOP, que o guia define assim: "Higgsfield DOP is Higgsfield's native cinematography layer" (efeitos visuais e movimento de câmera dirigido, por preset). O Cinema Studio, para o guia, é ferramenta, não modelo; ele aceita várias famílias de vídeo, trocáveis conforme a cena, sem que o guia diga quais.

**Vídeo, pela exigência do plano.** Movimento: o de gente realista (expressão, dinâmica da cena) vai ao Seedance, que é também o começo mais tolerante para iniciante; o fisicamente coerente, e a transferência de movimento de um vídeo para outro, ao Kling; o de câmera, ao DOP. Duração e continuidade: clipe longo e vários planos encadeados, Kling; continuar uma cena ou chegar a um estado inicial ou final definido, Wan, pelo controle do primeiro e do último quadro. Som sincronizado: Grok Imagine. Muita dinâmica, gerada rápido: Minimax Hailuo. Do Veo, a linha do guia só diz que é o modelo do Google.

**Como a escolha funciona.** Escolhe-se a família, não a versão: a mais nova vira o padrão quando sai, e as gerações antigas não mudam. Os modelos são o motor e as ferramentas (Cinema Studio, Canvas, Marketing Studio, Supercomputer) são onde se usam; na maioria delas se troca de modelo a qualquer momento. O custo em créditos varia com a família, a resolução e a duração, e aparece antes de confirmar; nem todo modelo está em todo plano.

**Imagem e áudio, numa linha cada.** Imagem: além do Soul (cuja força é treinar um personagem uma vez como Soul ID, reaproveitar o rosto e levá-lo a "some other models" salvando-o como Element) e do Popcorn, Nano Banana, GPT Image, Seedream, Recraft, FLUX e a ferramenta Upscale. Áudio: Seed Audio (cena sonora inteira numa passada, clonagem de voz e dublagem; no MCP e nos plugins do Premiere e do DaVinci Resolve), Eleven, MiniMax Speech, Seed Speech e VibeVoice, usados pelo Voiceover, pelo Change Voice e pela tradução.

**O que roda por baixo, segundo este guia.** Nativos da Higgsfield: Soul, Popcorn e Higgsfield DOP. O guia não cita o Genjutsu, o 3D Jutsu nem o Draw to Video no corpo, e não diz que famílias o Cinema Studio usa.

## 5. O blog do Genjutsu

**Proveniência.** https://higgsfield.ai/blog/higgsfield-genjutsu, "Meet Higgsfield Genjutsu: How It Works and What You Get", assinado "Higgsfield", baixado como HTML. A página mostra "Aug 31, 2026 · Updated Nov 2, 2026" (JSON-LD: `datePublished` 2026-08-31, `dateModified` 2026-11-02). Fonte curta: organizada aqui pela comparação entre o Genjutsu padrão e o Lite, pelo preço e pelo que a página não diz, e não pela ordem do post.

**Os modos, segundo o post.** Motion Transfer: o movimento de um vídeo existente comanda um personagem novo ou uma cena refeita. Object Swap: só o elemento apontado (produto, objeto, roupa) muda, e o resto do plano fica. Style, que o post põe dentro do Motion Transfer: cada quadro ganha outro visual, com 20 estilos prontos (entre os exemplos, animação de cel pintada à mão, stop motion de feltro, 3D de videogame antigo) ou um estilo tirado de uma imagem enviada, e movimento, câmera e enquadramento ficam como filmados. O post não usa o nome "Restyle". Serve para filmagem real ou vídeo gerado, e para variar estilo, roupa, anúncio por mercado, acabamento de comercial e quem aparece na tela, sempre mantendo da fonte o movimento, o ritmo ou o enquadramento.

**Genjutsu padrão e Genjutsu Lite, lado a lado** (limites no app, como o post os dá):

| | Genjutsu padrão | Genjutsu Lite (atualização "As of October 20, 2026") |
|---|---|---|
| Vídeo de entrada | 1 clipe, de 4 a 30 s | "It supports clips from 4 to 30 seconds, up to 10 reference images, and output at 720p or 1080p." |
| Imagens de referência | até 30 | até 10 |
| Escolha do modo | Motion Transfer ou Object Swap | nenhuma: o Lite aplica a mudança sozinho |
| Prompt | opcional; mais de 30 presets | o post não diz |
| Resolução de saída | até 1080p | 720p ou 1080p |
| Velocidade e preço | | mais rápido e mais barato |

O nome que o post usa é "Genjutsu Lite".

**Quanto custa no app** (vídeo de 15 s; o post converte créditos em dólar a US$ 49 por 1.000 e avisa que a conta pode mostrar preço menor: "Prices checked on November 2, 2026."):

| Modo | 480p | 720p | 1080p |
|---|---|---|---|
| Motion Transfer | 45 créditos, cerca de US$ 2,21 | 105, cerca de US$ 5,15 | 300, cerca de US$ 14,70 |
| Object Swap | 48, cerca de US$ 2,35 | 112, cerca de US$ 5,49 | 320, cerca de US$ 15,68 |
| Genjutsu Lite | (fora da tabela) | 96, cerca de US$ 4,70 | 192, cerca de US$ 9,41 |

O preço cresce com a duração e a resolução, e o valor exato aparece no botão de gerar. O preço pela API, diz o post, fica à parte, no console da API, e ele não o reproduz.

**Onde roda.** O Genjutsu e o Lite estão no conector MCP (para o Claude ou o ChatGPT) e na API; o Lite também no CLI, nos plugins e no Supercomputer.

**O que o post não diz.** Que modelo de base roda por baixo do Genjutsu ou do Lite; o preço por API; a duração do vídeo de saída.

**Dentro do próprio post.** No FAQ, a pergunta "Does Genjutsu work with AI-generated video?" recebe como resposta onde o Genjutsu está disponível (MCP e API), sem tratar de vídeo gerado; é o corpo do post que diz que ele funciona com vídeo gerado.

## 6. O changelog

**Proveniência.** https://higgsfield.ai/creator-hub/changelog, "What's new", baixado como HTML. A página não tem uma data própria: cada entrada traz a sua, e a mais nova é de 09/11/2026 (no JSON-LD, cada entrada tem também `datePublished` e `dateModified`). São 174 entradas, de 24/01 a 09/11/2026, cada uma com tipo (Announcement, Release, Feature, Improvement, Fix) e categoria (Models, Video Tools, Cinema Studio, MCP & Integrations, Platform e outras). A ordem abaixo é a da página, da mais nova para a mais antiga; entre parênteses, o tipo e a categoria.

**Novembro de 2026**

- **09/11, Ads Studio now creates video ads** (Release, Video Tools): o Ads Studio passa a fazer anúncio em vídeo, inclusive longo, por um agente no chat: ideia ou roteiro, estilo (Micro drama, Cartoon story, Cinematic story, Claymation story e outros), produto e ator; kit de marca a partir do link do site, ou montado à mão; um ator para todos os anúncios.
- **05/11, Gemini Omni Flash 1.2** (Feature, Models): a versão nova do modelo de vídeo do Google, com áudio nativo e extensão de vídeo; de 3 a 15 s por geração em 360p, 720p, 1080p ou 4K; até 6 imagens e 3 vídeos curtos de referência, só para aparência (o áudio do vídeo de referência é ignorado); quadro inicial obrigatório e final opcional; a extensão continua do fim, de 3 a 10 s por passo, até 30 s no total. Na web, no MCP, no Supercomputer e no CLI.
- **04/11, Kling 4.0 Flash** (Feature, Models): versão leve do Kling 4.0 para teste rápido, com os mesmos modos (References, Frames, Edit video), de 3 a 20 s em 720p; só quadro inicial, que também define a proporção, sem último quadro nem quadros-chave; até 10 imagens e 5 vídeos de referência, mais Elements; custa menos por geração; para versão final com quadros-chave e 1080p, o Kling 4.0.
- **03/11, Shorts Studio** (Release, Video Tools): reels verticais 9:16 com um avatar de IA apresentando; o roteiro sai de um tema, um gancho ou tópicos; o movimento vem de um vídeo de referência de 10 a 120 s ou de um formato pronto; duração de 10 s a 2 min, qualidade Basic ou High; também no Claude pelo MCP.
- **02/11, Kling generation failures resolved** (Fix, Models): as gerações de todos os Kling (4.0, 3.0, Motion Control) falharam por um problema do lado do fornecedor; resolvido, créditos devolvidos.

**Outubro de 2026**

- **30/10, Higgsfield Intone** (Release, Video Tools): personagem falando com sincronia labial e a mesma voz de cena a cena; até 30 s de fala por geração; personagem de imagem enviada (inclusive foto própria) ou do AI Influencer; fala gravada ou gerada, com marcas entre colchetes para a entonação; 720p ou 1080p, cinco proporções.
- **22/10, Content Factory** (Release, Video Tools): de um tema "what if" a um clipe pronto (roteiro, personagens, cenas com narração, edição); de 15 s a 5 min, 1 a 4 episódios por vez; mais de 50 formatos ou um próprio a partir de links de vídeos.
- **21/10, Kling 4.0** (Feature, Models): o modelo novo da Kling, de texto, imagem ou conjunto de referências, e edição de clipe pronto, com desconto de lançamento por tempo limitado; segundo a Kling, comparado ao 3.0: movimento mais estável em cena rápida, até 10 quadros-chave (em vez de só primeiro e último), até 15 referências (até 5 vídeos e Elements), Creative Recreation (reaproveita ritmo, composição e movimento de um vídeo), edição (troca personagem, produto, fundo, ângulo ou estilo); de 3 a 30 s, 720p ou 1080p, de 21:9 a 9:16, som estéreo e narração em 9 línguas.
- **19/10, Genjutsu Lite** (Release, Video Tools): versão leve, para clipe curto e com menos créditos; Motion transfer e Objects swap funcionam como no padrão; para vídeo mais longo, mais referências ou Restyle, o padrão. O limite que a entrada dá: "Inputs: a video from 4 to 15 seconds and up to 10 reference images." Qualidade 720p ou 1080p.
- **19/10, 3D Angles** (Release, MCP & Integrations): no plugin da Higgsfield no ChatGPT, uma foto, um vídeo ou uma descrição viram cena 3D para refilmar de outros ângulos (lentes de 24 a 300 mm, abertura de ƒ1.4 a ƒ16, oito formatos); saída em foto ou vídeo de até 30 s, com vídeo de rascunho para conferir o movimento de câmera.
- **15/10, FLUX 3 Video Upscaler update** (Feature, Models): nova versão do upscaler de vídeo da Black Forest Labs, que substituiu a anterior sozinha: mais detalhe, mais rápida e mais barata; por ora, só na Higgsfield.
- **13/10, Unlimited Wan 3.0 for 7 days and 60% off on the API** (Feature, Models): uma semana de Wan 3.0 e Wan 3.0 Prime sem limite para assinantes do plano Pro para cima, e 60% de desconto no mesmo modelo para todos os usuários da API até 31/10/2026; clipes de até 30 s e até 1080p, em fila compartilhada.
- **08/10, Katana** (Release, MCP & Integrations): uma skill da Higgsfield para o Claude que faz edições de vídeo nos estilos Aura Farming, Motion ou Clipping a partir de uma foto de referência; roda "on Higgsfield models through MCP" (sem dizer quais); até 5 imagens por edição; presets da comunidade levam um vídeo de 3 a 30 s para o movimento e até 40 imagens.
- **06/10, Ad Multiplier** (Release, Video Tools): refaz um anúncio em vídeo com personagens, produtos e lugares próprios, mantendo a estrutura do original; troca produto, elenco, lugar, roteiro, gancho ou chamada; um vídeo de 4 a 30 s e até 20 imagens; 480p, 720p ou 1080p.
- **03/10, Seedance generation failures resolved** (Fix, Models): falhas e lentidão, sobretudo no 2.0, 2.0 Mini, 2.0 Fast e 2.5 Draft Mode, por problema do fornecedor; resolvido, créditos devolvidos.
- **02/10, AI Influencer** (Release, Image Tools): cria um personagem de IA (do zero, de referência ou da própria foto); o botão Use in Genjutsu põe o personagem num vídeo existente por Motion transfer ou Object swap.
- **02/10, Higgsfield API cashback** (Release, Platform): bônus de US$ 15 depois dos primeiros US$ 100 gastos na API e cashback de até 20% em ciclos de 30 dias, pela faixa de gasto (US$ 5 mil, 5%; 10 mil, 8%; 20 mil, 12%; 50 mil, 20%), só sobre uso pago do saldo principal.
- **01/10, Grok Imagine Video 1.5** (Feature, Models): o modelo de vídeo novo da xAI, com som na mesma passada; imagem para vídeo, texto para vídeo, referência para vídeo e extensão a partir do último quadro; até 7 imagens de referência; 480p, 720p ou 1080p, de 1 a 15 s, 24 fps.
- **01/10, Seedance generation failures resolved** (Fix, Models): Seedance 2.0, 2.5 e 2.5 Draft Mode falhando ou lentos, por problema do fornecedor; resolvido.

**Setembro de 2026**

- **30/09, Genjutsu Restyle** (Release, Video Tools): redesenha o vídeo inteiro num estilo visual novo, mantendo movimento, ritmo e câmera; funciona dentro do modo Motion transfer, com vídeo de referência de 4 a 30 s; mais de 20 estilos de animação ou um próprio a partir de imagens; até 30 imagens de referência; 480p, 720p ou 1080p; na web e pelo MCP.
- **30/09, Higgsfield extension for ChatGPT** (Feature, MCP & Integrations): geração de imagem, vídeo, conteúdo de marca e sites dentro do ChatGPT; entre os comandos, `/genjutsu` para o Genjutsu.
- **30/09, Seedance 2.0 generation failures and Seedance 2.5 delays resolved** (Fix, Models): falhas no 2.0 e demora no 2.5, por problema do fornecedor.
- **29/09, OpenAI Dots** (Feature, MCP & Integrations): os agentes sempre ligados do ChatGPT geram vídeo e imagem na Higgsfield pelo plugin; entre as ferramentas, Cinema Studio e Genjutsu.
- **24/09, Higgsfield API cashback** (Release, Platform): campanha de US$ 1 de cashback por dólar gasto na API até 30/09, com teto de US$ 1.000 por conta (US$ 200 mil com e-mail corporativo e cartão); o que se paga com cashback sai a preço cheio, sem desconto de modelo.
- **23/09, Production Skills Bundle** (Feature, MCP & Integrations): 11 fluxos da Higgsfield para o Claude pelo MCP que rodam dentro do Blender, dos apps da Adobe, do TouchDesigner e do DaVinci Resolve Studio (o Claude Desktop e o programa no mesmo computador), devolvendo projeto editável.
- **22/09, Seedance 2.5 Draft Mode** (Feature, Models): duas etapas: um rascunho em 480p e, do escolhido, o render em 1080p com as mesmas configurações (prompt, referências, seed, proporção, duração); o rascunho custa menos créditos; aceita imagem inicial e final, e o modelo preenche o movimento entre elas; som gerado junto; até 30 s; em todas as regiões menos os EUA, onde o fornecedor não oferece o modelo.
- **22/09, GPT-6 Sol and GPT-6 Luna** (Feature, MCP & Integrations): dois modelos de linguagem da OpenAI no Supercomputer e no MCP.
- **16/09, Higgsfield API** (Release, Platform): produto à parte para desenvolvedores, com uma chave para mais de 50 modelos de imagem, vídeo e áudio; cobrança separada dos planos e créditos do higgsfield.ai, por geração, sem assinatura, com preço público por modelo e só a geração bem-sucedida cobrada; três chamadas (enviar, consultar o status, buscar o arquivo); SDK em Python e TypeScript, ou REST.
- **10/09, Seedance 2.0 generation failures resolved** (Fix, Models): falhas acima do normal, problema do fornecedor.
- **06/09, GPT-6 Astra in Higgsfield MCP** (Feature, MCP & Integrations): o GPT-6 Astra cuida da lógica e da orquestração, a Higgsfield gera os assets; o Games 2.0 usa esse par.
- **04/09, 3D Jutsu** (Release, Platform): espaço de trabalho 3D da Higgsfield, ligado ao Supercomputer: um prompt ou uma referência viram cena 3D editável e depois vídeo; a cena (objetos, layout, luz, câmeras, animação) é gerada de um prompt e de um modelo à escolha, "GPT-6 Astra included"; move-se personagem e objeto e muda-se a luz sem refazer a cena; os planos e o vídeo final saem no mesmo espaço.
- **01/09, Genjutsu** (Release, Video Tools): o lançamento: troca objeto, lugar, produto ou personagem num vídeo e deixa o resto; sem prompt obrigatório, com mais de 30 presets; Motion Transfer e Object Swap; um vídeo de até 30 s e até 30 fotos de referência; saída até 1080p.
- **01/09, Seedance 2.5 generation failures resolved** (Fix, Models): falhas acima do normal, problema do fornecedor.

**Agosto de 2026**

- **31/08, MiniMax H3 Max** (Feature, Models): variante do H3 ajustada para aderência ao prompt e estética, limitada a 768p (o H3 base vai a 2K); texto para vídeo, imagem para vídeo e transição entre quadro inicial e final.
- **28/08, Gemini Omni 1.1 Flash** (Feature, Models): o modelo do Google para gerar e editar vídeo, com primeiro e último quadro (gera o meio), modo rascunho em 360p; até 10 s, em 360p, 720p, 1080p ou 4K.
- **27/08, FLUX 3 Video Upscaler** (Feature, Video Tools): upscaler de vídeo da Black Forest Labs para 1080p, 2K ou 4K, em modo Precise (sem detalhe novo) ou Creative (com detalhe novo, por prompt opcional).
- **25/08, Ad Multiplier skill for Claude** (Release, MCP & Integrations): skill para o Claude, pelo MCP, que tira de um anúncio em vídeo muitas variantes com outros personagens, roupas, lugares ou objetos, mantendo o corte, o ritmo e o áudio original (fora das variantes traduzidas).
- **24/08, Wan 3.0 and Wan 3.0 Prime** (Feature, Models): até 30 s em 480p, 720p ou 1080p, rosto e roupa estáveis entre quadros mesmo com vários personagens, som sincronizado; o Prime gera mais rápido e custa mais.
- **22/08, Grok Bot in Higgsfield MCP** (Feature, MCP & Integrations): o Grok Bot da xAI, um agente sempre ligado, gera imagem e vídeo na Higgsfield pelo MCP.
- **21/08, Kling generation failures resolved** (Fix, Models): falhas no Kling 3.0, 3.0 Turbo, 3.0 Motion Control e Kling Edit, problema do fornecedor.
- **21/08, Relight and Color Palette are now standalone products** (Release, Video Tools): as ferramentas de edição de vídeo do Cinema Studio 4.0 passam a funcionar sozinhas: o Relight, com presets de luz e até duas fontes de luz próprias, e o Color Palette, com mais de 50 presets de cor.
- **20/08, Faceless Studio** (Release, Video Tools): vídeos animados sem rosto, de 1 a 5 min, em quatro temas, com 8 estilos e narrador; estilo e voz ficam salvos no canal.
- **19/08, Higgsfield for Enterprise** (Improvement, Platform): acesso dedicado aos modelos Seedance para equipes grandes, em infraestrutura de GPU dedicada nos EUA, com SOC 2 e SSO.
- **12/08, Cinema Studio 4.0** (Release, Cinema Studio): gerações de 30 s; até 50 referências por geração para fixar rosto, produto ou estilo; mais de 30 presets de movimento de câmera, 4 tipos de câmera e um sistema de 5 lentes refeito; Color Palette com mais de 50 presets; Emotion Wheel com mais de 8 emoções para a atuação; seletor de década (grão, cor e lente acompanham); controle do ritmo de corte; extensão para frente e para trás de um clipe.
- **07/08, New Viral Presets** (Improvement, Video Tools): 13 presets novos de tendência de vídeo curto.
- **06/08, Seedance 2.5** (Feature, Models): a versão nova da família Seedance da ByteDance: clipes de até 30 s com ambiente, foley e trilha gerados com a imagem; edição por região (corrigir um objeto ou um rosto sem refazer o clipe, refazer um plano de uma sequência); até 50 referências; resolução de 480p e 720p, com upscale até 4K.

**Julho de 2026**

- **22/07, Kling generation failures resolved** (Fix, Models): falhas em todos os Kling (3.0, Avatar 2.0, 2.6, Motion Control), problema do fornecedor.
- **13/07, Adobe After Effects plugin in Supercomputer and Higgsfield MCP** (Release, Supercomputer e MCP & Integrations): o plugin do After Effects passa a funcionar no Supercomputer e no Claude pelo MCP (no Claude, pelo conector `bridge.higgsfield.ai/mcp`): o agente mexe em composições, camadas, quadros-chave e efeitos, anima a partir de vídeo de referência e importa as imagens e os vídeos gerados.
- **09/07, Kling 3.0 and GPT Image 2 generation failures resolved** (Fix, Models): falhas imediatas, problema do fornecedor.
- **07/07, Higgsfield Apps** (Release, Supercomputer): o Supercomputer monta apps que geram imagem, vídeo e 3D com os modelos da Higgsfield; também no Claude e no Cursor pelo MCP.
- **01/07, Higgsfield Explainer** (Release, Supercomputer e MCP & Integrations): skill do Supercomputer e do MCP para vídeo narrativo animado (sem fotorrealismo): uma narração sobre blocos estilizados de 10 s num mesmo estilo, até 10 min, em 16:9 ou 9:16.
- **01/07, Claude Fable 5 is back in Supercomputer and Higgsfield MCP** (Feature, Supercomputer): o modelo de linguagem da Anthropic volta ao Supercomputer e ao MCP.

**Junho de 2026**

- **30/06, Claude Sonnet 5** (Feature, Supercomputer e MCP & Integrations): o modelo de linguagem da Anthropic no MCP e no Supercomputer.
- **29/06, Gemini Omni Flash** (Feature, Models): o modelo de vídeo do Google DeepMind em prévia (beta): 720p, clipes de 4, 6, 8 ou 10 s, 16:9 ou 9:16, áudio nativo; lê texto, imagem e vídeo juntos; segundo o Google, personagem consistente, física crível e edição de um elemento por prompt.
- **26/06, Unlimited Models Marketplace** (Release, Billing & Plans): acesso sem limite a um modelo por 1, 7 ou 14 dias, em vez de créditos por geração; entre os modelos, Seedance 2.0 e Kling 3.0; o que se gera pelo MCP, pelo CLI, pelo Canvas e pelo Supercomputer continua gastando créditos; planos Pro e Plus para cima.
- **25/06, Higgsfield Audio in Higgsfield MCP** (Release, Audio): narração, voz própria, troca de voz e tradução pelo Claude, via MCP.
- **21/06, Seedance 2.0 Mini** (Feature, Models): modelo leve da família Seedance 2.0, "exclusive to Higgsfield with BytePlus", cerca de duas vezes mais rápido que o Enhanced Seedance 2.0 Fast em qualidade comparável; 480p e 720p, de 4 a 15 s, referências de texto, imagem, vídeo ou áudio.
- **21/06, Seedance 2.0 now generates in 4K** (Feature, Models): opção de 4K no Seedance 2.0.
- **19/06, Seedance now has a High bitrate option** (Feature, Models): bitrate Standard ou High no Seedance 2.0 e 2.5; o High dá mais qualidade pelo mesmo custo em créditos, com arquivo maior.
- **16/06, Kling 3.0 Turbo** (Feature, Models): variante rápida do Kling 3.0 para fechar o plano em rascunho antes do render final; texto e imagem para vídeo; na web, no Supercomputer, no MCP e no CLI.
- **15/06, ByteDance Upscale** (Feature, Models): upscale de vídeo da ByteDance com interpolação até 60 fps, em 2K ou 4K; para rosto ou câmera lenta, o motor da Topaz.
- **10/06, Higgsfield Games** (Release, Supercomputer e MCP & Integrations): jogos de navegador a partir de descrição, no Supercomputer ou no Claude pelo MCP.
- **07/06, Higgsfield plugin for DaVinci Resolve** (Feature, MCP & Integrations): as ferramentas da Higgsfield na timeline do DaVinci; na geração, vídeo e imagem, Edit Video e "Draw to Video" por prompt; na edição, Reframe, Remove Background e Upscale; o Color Match faz uma LUT a partir de uma referência. É a única entrada que nomeia o Draw to Video, e ela não diz o que ele é nem em que modelo roda.
- **07/06, Cinema Studio now has its own workspace** (Release, Cinema Studio): o Cinema Studio ganha um espaço próprio, com projetos e subpastas, Elements chamados com @ no prompt e seções de gerações, elementos e favoritos.
- **02/06, Grok Imagine 1.5** (Feature, Models): o modelo de vídeo da xAI anima uma imagem como primeiro quadro, ou parte só de texto; de 1 a 15 s; 16:9, 9:16 e 1:1.

**Maio de 2026**

- **30/05, Higgsfield Reframe** (Release, Video Tools): adapta o vídeo a outra proporção (9:16, 16:9, 4:3, 3:4, 21:9, 1:1) sem cortar: trava nos personagens e regenera o fundo; até 4 imagens de referência.
- **28/05, Video analysis and recreation in Claude through Higgsfield MCP** (Release, MCP & Integrations): o Claude analisa um vídeo de referência (estrutura, planos, ritmo) e gera assets a partir dessa análise no mesmo chat; gasta créditos do plano.
- **27/05, Higgsfield plugins for Adobe Premiere Pro and After Effects** (Release, MCP & Integrations): um painel com cinco ferramentas: Reframe, Remove Background, Upscale até 4K ou 8K, Draw to Edit (desenhar sobre o clipe o que mudar) e Edit Video (edição por prompt); roda nos servidores da Higgsfield com os créditos do plano.
- **22/05, Higgsfield MCP now connects to Cursor** (Release, MCP & Integrations): o mesmo servidor MCP do Claude e do Manus passa a ligar no Cursor.
- **22/05, New formats in Viral Presets** (Improvement, Video Tools): segundo lote de presets que transformam imagem em vídeo.
- **20/05, Higgsfield MCP on Manus AI** (Release, MCP & Integrations): os agentes do Manus geram com os modelos da Higgsfield e publicam (Meta Ads, Instagram, Creator Marketplace).
- **15/05, Higgsfield Viral Presets** (Release, Video Tools): página de formatos de vídeo em alta e presets próprios, de foto ou vídeo, em 16:9, 1:1 ou 9:16; o custo depende do preset.
- **07/05, Ad Reference in Marketing Studio** (Release, Marketing Studio): um vídeo de referência vira anúncio no mesmo estilo com produto e avatar próprios; também pelo MCP no Claude, no Hermes e no OpenClaw.
- **04/05, Higgsfield CLI** (Release, MCP & Integrations): geração de imagem e vídeo pelo terminal e por agentes de código (Claude Code, Cursor, Codex, OpenClaw e mais de 12 outros); as skills entram com `npx skills add higgsfield-ai/skills`.

**Abril de 2026**

- **30/04, Higgsfield Canvas** (Release, Platform): quadro infinito de nós ligados num fluxo (geração de imagem e vídeo, LLM, prompt, upload); entre os modelos de partida, "Simple Seedance 2.0" e "Extend Video".
- **28/04, Higgsfield MCP** (Release, MCP & Integrations): geração de imagem e vídeo dentro do agente que a pessoa já usa, com o resultado no mesmo chat; pede assinatura ativa da Higgsfield e da plataforma conectada e gasta créditos do plano, sem chave de API; mais de 16 modelos de imagem (até 4K) e mais de 17 de vídeo, até 15 s, com controle de duração, gênero e quadro inicial e final; o agente escolhe o modelo para a tarefa ou usa o que a pessoa nomeia; o conector é `https://mcp.higgsfield.ai/mcp`.
- **27/04, HappyHorse** (Feature, Models): o modelo de vídeo da Alibaba, que no lançamento estava em primeiro no Artificial Analysis Video Arena; som na mesma passada, vários planos.
- **23/04, Kling 3.0 and Kling Omni now support 4K** (Feature, Models): 4K nos dois.
- **16/04, Seedance 2.0 now supports 1080p** (Feature, Models): 1080p no Seedance 2.0.
- **15/04, Cinema Studio 3.5** (Release, Cinema Studio): configurações por projeto (gênero, paleta, câmera, lente, luz) e um diretor de IA embutido; esta versão tira o áudio, os presets de movimento de câmera, a rampa de velocidade e a interface de edição; os Elements substituem o modo Image (personagens, lugares e objetos como assets do projeto).
- **06/04, Veo 3.1 Lite, Grok Imagine Image, and Wan 2.7** (Feature, Models): o Veo 3.1 Lite (Google), vídeo rápido em 720p ou 1080p, até 8 s, de texto ou imagem, com áudio nativo; o Wan 2.7 (Alibaba), 1080p até 15 s, com controle de primeiro e último quadro, entrada em grade de 9, áudio nativo, edição por instrução e várias referências (o Grok Imagine Image é de imagem).
- **02/04, Seedance 2.0 and Seedance 2.0 Fast** (Feature, Models): o Seedance 2.0 da ByteDance em versão cheia e em versão leve, mais rápida e mais barata.

**Março de 2026**

- **31/03, Cinema Studio 3.0** (Release, Cinema Studio): versão para uso comercial e de estúdio: luta, perseguição e explosão com peso; rosto, corpo e roupa consistentes; efeitos, fala e música gerados com o vídeo; um "Cinematic Reasoning Engine" com até 9 referências mais o prompt; sete gêneros e sete rampas de velocidade; personagens e lugares do 2.5 reaproveitáveis. A entrada não diz que modelo de vídeo roda por baixo.
- **18/03, Cinema Studio 2.5** (Release, Cinema Studio): até 3 atores de IA num quadro-chave e correção de cor dentro do estúdio.
- **10/03, Higgsfield AI Cast** (Release, Cinema Studio): estúdio de elenco de atores de IA (gênero do filme, época, orçamento, 12 arquétipos, aparência e detalhes), no modo Image do Cinema Studio.

**Fevereiro de 2026**

- **27/02, Soul Photodump** (Release, Image Tools): um conjunto de 15 imagens do mesmo personagem em poses, roupas e lugares diferentes, todas a partir de um Soul ID.
- **26/02, Moodboards in Soul 2.0** (Release, Image Tools): estilos visuais treinados em imagens próprias (pelo menos 10) ou mais de 20 prontos; funciona com Soul ID, Soul Reference e Soul Hex.
- **25/02, Elements** (Release, Platform): biblioteca pessoal de personagens, lugares, roupas e objetos, salvos uma vez e chamados com @ no prompt; um elemento de vídeo pode manter, tirar ou trocar o áudio; os modelos listados como compatíveis são Kling 3.0, Seedream 4.5 e 5.0 Lite, Cinema Studio (imagem e vídeo), Nano Banana Pro "and more".
- **19/02, Soul 2.0** (Release, Models): a segunda versão do modelo de imagem fotorrealista próprio da Higgsfield ("Higgsfield's own"), retreinado para moda e estéticas de internet.
- **04/02, Kling 3.0, Omni 3.0, and Omni 3.0 Edit** (Feature, Models): o Kling 3.0 (de prompt ou imagem, de 3 a 15 s, 720p ou 1080p), o Kling Omni (texto, imagem, vídeo e áudio num modelo só, com diálogo e sincronia labial e personagens de referência) e o Kling Omni Edit (muda uma parte de um clipe sem refazer o vídeo).

**Janeiro de 2026**

- **30/01, Grok Imagine** (Feature, Models): o modelo de vídeo da xAI para clipes curtos com história, voz e movimento.
- **24/01, Veo 3.1 now supports 4K** (Feature, Models): opção de qualidade 4K no Veo 3.1 do Google.

**O resto do changelog, numa linha.** Ficaram fora as entradas de modelos de imagem (Seedream 5.5, 5.0 Flash, 5.0 Pro e 5.0 Lite; GPT Image 2.6, 2.5 e 2.0; Ideogram 4.5, Precise Edit e Vector 1.0; Nano Banana 2.1, 2 e 2 Lite; FLUX 3 Image; Recraft V4 e v4.1), de ferramentas de imagem (Mangaka, Layers, Ads Studio de imagem, Soul Hex, Angles), de modelos de linguagem só no Supercomputer (Fable 5.2, Inkling 2 Small, GPT-6.1 Terra e Sol, Kimi K3.1 Pro, Claude Sonnet 5.5 e Opus 5.5, Grok 4.7, GPT-6 Astra, Claude Fable 5.1, GLM-5.3 Flash, GPT-5.6 e Grok 4.5), do Supercomputer como produto (lançamento, projetos, Auto Mode, armazenamento, App Builder, AI Employees 2.0, conectores, servidores MCP de terceiros dentro dele, concurso de apps), de áudio (Eleven v4, Seed Audio 1.0, Seed Speech, o Audio novo com Qwen), de plugins sem vídeo (Photoshop, Figma e FigJam, Blender, After Effects pelo ChatGPT, Effects 2.0 no ChatGPT, AI Motion Designer), de cobrança e conta (reinício de créditos, Unlimited nos planos Team e Scale, Usage History), de plataforma (línguas chinesa, coreana, japonesa e espanhola, Playable, Community, Academy, Originals, Contests, afiliados, cancelamento de geração na fila, redesenho do celular, que põe o Genjutsu e o MCP na barra lateral, Marketing Studio) e de concursos e festival (o festival de cinema, o Weekly Challenge e o concurso dos 200 mil do Discord pedem o filme feito num projeto do Cinema Studio); das que ficaram fora, a Playable e o Seedream 5.0 Pro só citam o MCP como canal de acesso.

**Dentro do próprio changelog, dois pontos que a página não concilia.** (a) O Seedance 2.5 sai em 06/08 com resolução de 480p e 720p, e upscale até 4K; a entrada do Draft Mode, de 22/09, dá o render final do mesmo modelo em 1080p. (b) Há duas entradas de lançamento de um "1.5" de vídeo da xAI: "Grok Imagine 1.5", em 02/06, e "Grok Imagine Video 1.5", em 01/10, esta chamada de modelo novo.

**O que roda por baixo, segundo o changelog.** Nenhuma entrada do Genjutsu (lançamento, Restyle, Lite) nem do Cinema Studio (2.5, 3.0, 3.5, 4.0) diz que modelo de vídeo usa. O 3D Jutsu gera a cena com um modelo à escolha, entre eles o GPT-6 Astra, sem dizer qual modelo faz o vídeo final. O Soul 2.0 é dito modelo próprio. O Katana roda em "Higgsfield models", sem nomes. O Draw to Video só aparece como nome de ferramenta no plugin do DaVinci Resolve.

## O que nenhuma das sete páginas diz

- Que modelo de base roda por baixo do Genjutsu, do Genjutsu Lite (ou Light), do Cinema Studio, do 3D Jutsu (no vídeo final) e do Draw to Video.
- Que modelos são os "supported models" dos Elements hoje (a lista do changelog, de fevereiro, termina em "and more").
- O preço do Genjutsu por API na condição de cada resolução; o catálogo só dá o mínimo ("from").
- O que é o Draw to Video.
