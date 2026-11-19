---
titulo: "Veo 3.1 | Gemini Enterprise Agent Platform | Google Cloud Documentation"
tipo: artigo
autor: "Google (Google Cloud Documentation)"
url: "https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate"
publicado_em: 2026-11-10   # "Last updated 2026-11-10 UTC", no rodapé da página
capturado_em: 2026-11-11
licenca: "CC BY 4.0 no texto e Apache 2.0 nos exemplos de código, pelo rodapé da página: 'Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License' (HTML baixado em 2026-11-11, l. 10515). Textos: https://creativecommons.org/licenses/by/4.0/ e https://www.apache.org/licenses/LICENSE-2.0"
areas: [generative-media]
tags: [veo, video-generation, vertex-ai, image-to-video, first-last-frame, video-extension, reference-images, provisioned-throughput, model-lifecycle]
---

# Veo 3.1 no Google Cloud: a página do modelo (novembro de 2026)

Ficha em palavras próprias; o texto integral da página (CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Página de documentação do Google Cloud, baixada em HTML com `curl` (user agent de navegador) em 11/11/2026; a `canonical` do arquivo é a própria `url`, e o rodapé dá a última atualização, 2026-11-10 UTC. O produto aparece com o nome novo, Gemini Enterprise Agent Platform (o caminho da página é `gemini-enterprise-agent-platform/models/veo/`).

**Quem fala.** O Google, fabricante do modelo, na documentação de referência.

**Cobertura.** A página inteira: a frase de abertura, as três abas (3.1 Generate, 3.1 Fast Generate, 3.1 Lite Generate), cada uma com a tabela completa do modelo e a nota sobre a data de retirada, o aviso de Preview que acompanha a aba do Lite e a frase final que remete à tabela de preços. A navegação lateral do site ficou fora da ficha e do integral. A página não traz parâmetros de API nem exemplos de código.

## As três versões numa tabela só

A página dá uma tabela por versão, cada uma numa aba; aqui as três ficam lado a lado, com os valores escritos como a página escreve.

| | Veo 3.1 | Veo 3.1 Fast | Veo 3.1 Lite |
|---|---|---|---|
| ID do modelo | `veo-3.1-generate-001` | `veo-3.1-fast-generate-001` | `veo-3.1-lite-generate-001` |
| Estado | GA | GA | Preview |
| Lançamento | November 17, 2025 | November 17, 2025 | April 2, 2026 |
| Retirada | May 4, 2027 or later | May 4, 2027 or later | a página não dá |
| Texto | entrada | entrada | entrada |
| Imagem | entrada | entrada | "Not supported" (ver contradição abaixo) |
| Áudio (modalidade) | "Not supported" | "Not supported" | "Not supported" |
| Vídeo (modalidade) | "Output only" | "Output only" | "Output only" |
| Geração: texto para vídeo, imagem para vídeo, primeiro e último quadro | sim | sim | sim |
| Estender vídeos | sim | sim | sim |
| Imagens de referência ("Asset images") | sim | sim | não |
| Geração de som | sim | sim | sim |
| Content Credentials (C2PA) | sim | sim | sim |
| Duração | 4, 6 ou 8 s; com imagem de referência, só 8 s | 4, 6 ou 8 s | 4, 6 ou 8 s |
| Vídeos por prompt (máximo) | 4 | 4 | 4 |
| Imagem de entrada para imagem para vídeo (máximo) | 20 MB | 20 MB | 20 MB |
| Proporções | 9:16, 16:9 | 9:16, 16:9 | 9:16, 16:9 |
| Resoluções de entrada | 720p, 1080p | 720p, 1080p | 720p, 1080p |
| Resoluções de saída | 720p, 1080p, 4K | 720p, 1080p | 720p, 1080p |
| Quadros por segundo | 24 FPS | 24 FPS | 24 FPS |
| Formato | `video/mp4` | `video/mp4` | `video/mp4` |
| Língua do prompt | English | English | English, marcado "Preview feature" |
| Região | `us-central1` (Estados Unidos) | `us-central1` | `us-central1` |
| Cota | 50 "tokens per minute" | idem | idem |
| Controles de segurança (predição online) | Data residency e AXT sim; CMEK e VPC-SC não | idem | a aba do Lite não tem essa linha |

## O que distingue as versões, pela própria página

- Só o Veo 3.1 padrão sai em 4K; Fast e Lite param em 1080p.
- Só o Veo 3.1 padrão tem a restrição de duração com imagem de referência: "reference image to video only supports 8 seconds". Nas outras duas, a linha de duração não traz ressalva.
- O Lite é o único em Preview, o único sem imagens de referência, o único sem data de retirada e sem a linha de controles de segurança, e o inglês dele vem marcado como recurso em Preview.
- A aba do Lite vem com o aviso de oferta Preview de IA generativa, sob os "Pre-GA Offerings Terms" dos termos específicos do Google Cloud; o aviso diz que o cliente pode usá-la "for production or commercial purposes", nos limites do contrato pelo qual acessa o Google Cloud, e tratar dados pessoais conforme o adendo de processamento de dados.

## Como se consome, segundo esta página

As três versões marcam as mesmas opções de consumo: Provisioned Throughput "Supported", Batch inference "Not supported", Pay-as-you-go "Not supported" e Fixed quota "Supported". Cada nome é um link para outra página da documentação (vazão provisionada, inferência em lote, opções de consumo, cotas), não lida aqui; a página do Veo não explica o que cada opção é nem o que o "Not supported" do pagamento por uso muda numa chamada.

Preço não há na página: o fim dela manda para a seção "Veo" da página de custos da plataforma (https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#veo), e cada aba tem um botão "Pricing" para o mesmo endereço sem a âncora.

A cota vem com o mesmo nome nas três: "Regional online prediction requests per base model per minute per base model", com o valor "50 tokens per minute".

## Datas e ciclo de vida

- Veo 3.1 e Veo 3.1 Fast: GA, lançados em 17/11/2025, com retirada em "May 4, 2027 or later".
- Veo 3.1 Lite: Preview, lançado em 02/04/2026, sem data de retirada.
- A nota que acompanha a data de retirada (repetida nas três abas) diz que ela se refere ao fim do suporte na Gemini Enterprise Agent Platform; os modelos "may remain accessible through the Gemini API after these dates have passed", e a Gemini API não é oferta do Google Cloud e tem termos de serviço próprios.

## Contradição e pontos que a página não concilia

- **Lite e imagem (contradição).** Na linha de modalidades do Lite, a imagem vem como "Not supported" (com o ícone `hide_image`); na linha de capacidades da mesma tabela, a geração de vídeo vem como "Text to video, image to video, from first and last frame" e "Supported". A página não resolve.
- **Áudio.** Nas três versões, a modalidade Audio é "Not supported" e a capacidade "Sound generation" é "Supported"; a página não diz se o som gerado sai no próprio arquivo de vídeo.
- **Vídeo de entrada.** A modalidade Video é "Output only" nas três, e as três marcam "Extend videos" como "Supported" e listam "Supported input resolutions: 720p, 1080p"; a página não diz o que entra na extensão nem a que entrada se referem essas resoluções.
- **Cota.** O nome da cota fala em requisições por minuto e o valor está em "tokens per minute"; a página não explica.

## O que a página não diz

- Preço, unidade de cobrança e diferença de preço com ou sem som (remete à página de preços).
- Quantas imagens de referência cabem num pedido, nem que formatos de imagem entram.
- Quanto uma extensão acrescenta, o limite de duração total de um vídeo estendido, e as durações aceitas com primeiro e último quadro.
- Detalhes do som (fala, música, efeitos, línguas da fala).
- Parâmetros da API (semente, prompt negativo, proporção por parâmetro), latência, e regiões fora de `us-central1`.
- Nada sobre pessoas reais, rostos ou moderação de conteúdo.
- Para o Lite: data de retirada e controles de segurança.
