---
titulo: "Agent Platform Pricing | Google Cloud"
tipo: artigo
autor: "Google Cloud"
url: "https://cloud.google.com/vertex-ai/generative-ai/pricing"
capturado_em: 2026-11-11
licenca: "protegida: página de produto (canonical cloud.google.com/model-garden/pricing, 'Agent Platform Pricing') sem o rodapé CC da documentação; as únicas licenças no arquivo são as dos scripts embutidos (Apache-2.0, MIT), não do conteúdo. Ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [veo, video-generation, vertex-ai, api-pricing, gemini-omni, video-audio, avatar-video]
---

# Vertex AI (Agent Platform): quanto custa gerar vídeo, pela tabela de preços do Google Cloud

**Proveniência.** Página de preços do Google Cloud, baixada em HTML com `curl` (user agent de navegador) em 11/11/2026, pela `url` acima. O arquivo declara como `canonical` https://cloud.google.com/model-garden/pricing e tem o título "Agent Platform Pricing | Google Cloud"; o cabeçalho da tabela geral é "Cost of building and deploying AI models in Agent Platform". A página não traz data de atualização: os únicos marcos de tempo são os prazos de preços promocionais de outros modelos.

**Quem fala.** O Google Cloud, vendedor do serviço, na tabela pública de preços.

**Cobertura.** Lidos inteiros: a subseção "Veo" (dentro de "Other Google models"), a seção "Gemini Omni" com as duas notas de rodapé, a linha de saída de vídeo de avatar da Gemini 3.8 Live API com a nota de conversão, o parágrafo de abertura de "Other Google models", a seção "Provisioned Throughput" (para ver se nomeia vídeo) e as frases gerais de cobrança do topo e de "Request a custom quote". O resto da página ficou fora, numa linha no fim.

## Veo: preço por versão, som e resolução

A tabela tem as colunas Model, Feature, Description, Input, Output, Output Resolution e "Price (USD)", e cada célula de preço vem escrita como "$0.40 / 1 count". A página não diz o que é um "count" para o Veo (segundo, vídeo ou outra coisa); aqui o preço fica com a unidade que ela escreve.

| Modelo | Saída | Resolução | Preço (USD) |
|---|---|---|---|
| Veo 3.1 | vídeo com áudio | 720p, 1080p | 0.40 / 1 count |
| Veo 3.1 | vídeo com áudio | 4k | 0.60 / 1 count |
| Veo 3.1 | vídeo | 720p, 1080p | 0.20 / 1 count |
| Veo 3.1 | vídeo | 4k | 0.40 / 1 count |
| Veo 3.1 Fast | vídeo com áudio | 720p | 0.10 / 1 count |
| Veo 3.1 Fast | vídeo com áudio | 1080p | 0.12 / 1 count |
| Veo 3.1 Fast | vídeo com áudio | 4k | 0.30 / 1 count |
| Veo 3.1 Fast | vídeo | 720p | 0.08 / 1 count |
| Veo 3.1 Fast | vídeo | 1080p | 0.10 / 1 count |
| Veo 3.1 Fast | vídeo | 4k | 0.25 / 1 count |
| Veo 3.1 Lite | vídeo com áudio | 720p | 0.05 / 1 count |
| Veo 3.1 Lite | vídeo com áudio | 1080p | 0.08 / 1 count |
| Veo 3.1 Lite | vídeo | 720p | 0.03 / 1 count |
| Veo 3.1 Lite | vídeo | 1080p | 0.05 / 1 count |
| Veo 3 | vídeo com áudio | 720p, 1080p | 0.40 / 1 count |
| Veo 3 | vídeo | 720p, 1080p | 0.20 / 1 count |
| Veo 3 Fast | vídeo com áudio | 720p | 0.10 / 1 count |
| Veo 3 Fast | vídeo com áudio | 1080p | 0.12 / 1 count |
| Veo 3 Fast | vídeo | 720p | 0.08 / 1 count |
| Veo 3 Fast | vídeo | 1080p | 0.10 / 1 count |
| Veo 2 | vídeo ("Video generation") | 720p | 0.50 / 1 count |
| Veo 2 | vídeo ("Advanced Controls") | 720p | 0.50 / 1 count |

O que as outras colunas dizem:

- **Entrada:** "Text/Image prompt" em todas as linhas do Veo 3.1, do Veo 3 e da geração simples do Veo 2; só os "Advanced Controls" do Veo 2 aceitam "Text/Image/Video prompt".
- **Descrição:** a linha com áudio fala em vídeo com fala ou efeitos sonoros sincronizados, a partir de um prompt de texto ou de uma imagem de referência; a do Fast acrescenta "faster" e a do Lite, "the fastest". Os "Advanced Controls" do Veo 2 são a interpolação entre quadro inicial e final, a extensão de vídeos gerados e os controles de câmera.
- **4K:** só o Veo 3.1 e o Veo 3.1 Fast têm linha de 4k; o Lite, o Veo 3, o Veo 3 Fast e o Veo 2 não têm.
- Logo antes da tabela fica um botão "Show discount options"; o HTML baixado traz uma tabela só para o Veo, e não mostra o que o botão muda.

## As outras saídas de vídeo da página

**Gemini Omni** (seção própria, preço por milhão de tokens, sem coluna de região):

| Modelo | Entrada (texto, imagem, vídeo, áudio) | Saída de texto | Saída de vídeo |
|---|---|---|---|
| Gemini Omni 1.2 Flash | $1.50 | $9.00 | $12.00 |
| Gemini Omni Flash, Gemini Omni 1.1 Flash | $1.50 | $9.00 | $17.50 |

As notas da tabela dão a conta em tokens, não em dinheiro por segundo:

- Na entrada: 1120 tokens por imagem, 32 por segundo de áudio e "up to 5792 tokens per video second"; o upscaling de vídeo não cobra tokens de entrada.
- Na saída de vídeo, "for video outputs (with audio)": 1931 tokens por segundo a 360p, 5792 a 720p, 8688 a 1080p e 17376 a 4k.
- No upscaling, a saída depende das resoluções de partida e de chegada: 2896 tokens por segundo de 360p para 720p e de 720p para 1080p; 5792 de 360p para 1080p; 11584 de 720p ou de 1080p para 4k.

**Gemini 3.8 Live API:** a tabela tem a linha "Output: video (avatar)", a $1.00 por milhão de tokens em região não global. A nota de cobrança da Live API converte a saída de vídeo de avatar em 6,192 tokens por segundo e diz que ela só é cobrada enquanto o avatar fala, não quando escuta.

## Como a página diz que cobra

- Os preços estão em dólar; quem paga em outra moeda segue o preço na moeda dela nos SKUs da Cloud Platform (a frase aparece no topo e logo depois da tabela do Imagen, antes da do Veo).
- Só se cobra o pedido que volta com código 200; respostas 4xx e 5xx não pagam entrada nem saída.
- A seção "Request a custom quote", no fim, diz: "With Google Cloud's pay-as-you-go pricing, you only pay for the services you use", e convida a falar com vendas para um orçamento. O menu do site, abaixo, repete a ideia ("Pay only for what you use with no lock-in") e fala em economia automática conforme o uso mensal e em desconto para recursos pré-pagos.
- A abertura de "Other Google models", seção onde fica o Veo, trata dos modelos Gemini fora o 2.0 e o 2.5: cobrança por modalidade (caracteres, imagens, segundos de vídeo ou áudio), com "Media input is charged per image or per second (video)". A frase não fala do Veo nem de saída de vídeo.
- A seção "Provisioned Throughput" vende unidades de vazão (GSUs) por compromisso de uma semana a um ano e dá um exemplo de cálculo com `gemini-2.0-flash`; não nomeia o Veo nem vídeo.

## O que a página não diz

- O que é o "count" do Veo, e portanto se o preço é por segundo, por vídeo ou por outra unidade.
- Se o pagamento por uso vale para o Veo, ou se o Veo se compra por outra via; a página fala de pay-as-you-go só em termos gerais.
- Preço do Veo 3.1 Lite em 4K, preço separado para extensão de vídeo ou para imagens de referência no Veo 3.1, e efeito da duração (4, 6 ou 8 s) no preço.
- Desconto ou preço em lote para o Veo; o HTML não mostra o conteúdo do "Show discount options".
- A conversão do Omni de tokens para dólar por segundo, e se os números do Omni valem fora do Vertex.
- A data da tabela.

**O resto da página, fora desta ficha:** os preços dos modelos Gemini 4, 3, 2.5 e 2.0, da Nano Banana, de TTS, Live Translate, Transcribe, Gemini 1.5, Imagen, Lyria, embeddings, Gemini Robotics, agentes (Deep Research), CodeMender, AlphaEvolve, Gemma, embeddings multimodais (com entrada de vídeo, que não é geração), AlphaGenome e AlphaFold 3, completamento de código, tradução, cache de contexto, os créditos promocionais de vazão provisionada, ajuste de modelos e modelos de parceiros.
