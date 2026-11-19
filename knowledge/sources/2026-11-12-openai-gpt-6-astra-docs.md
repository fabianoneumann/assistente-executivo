---
titulo: "GPT-6 Astra"
tipo: artigo
autor: "OpenAI (documentação oficial da API)"   # a página não tem assinatura
url: "https://developers.openai.com/api/docs/models/gpt-6-astra.md"
publicado_em: null   # a página não traz data de publicação nem de lançamento do modelo; a única data no texto é a do corte de conhecimento (30/04/2026)
capturado_em: 2026-11-12
licenca: "protegida: a versão Markdown oficial não declara licença nem traz rodapé (valem os termos do site da OpenAI); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [openai, gpt-6-astra, model-ids, api-pricing, image-generation, rate-limits]
---

# GPT-6 Astra: o que a página do modelo diz de entradas, saídas, endpoints e preço

Nota de fato: tabelas do que a página registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Página do modelo na documentação da API da OpenAI, https://developers.openai.com/api/docs/models/gpt-6-astra.md, na versão Markdown (`.md` no fim do endereço), baixada em 12/11/2026; sha256 (hash omitido); Wayback http://web.archive.org/web/20261027120503/https://developers.openai.com/api/docs/models/gpt-6-astra.md. Título conferido no cabeçalho do arquivo. Lida inteira (detalhes, preço, endpoints, recursos, ferramentas, snapshots, nuvens e limites de taxa); nenhum link aberto (o guia do modelo, a página de preços, os guias do Bedrock e do Google Cloud).

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (número, rota, estado, nome de ferramenta) fica fora. Resultado: 1 de 11 unidades segue a fonte, a frase da recomendação, que junta a tabela de endpoints à lista de ferramentas; a maior sequência seguida que segue a fonte tem 1 unidade, e as duas citações estão à parte. O `parafrase.py` saiu com o código 3 contra o Markdown da página, com 11 unidades medidas (11 de prosa, 0 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas.

## Em uma frase

Página de referência da OpenAI para o próprio modelo, com as entradas e saídas, os endpoints que o aceitam, as ferramentas, o preço por token e os limites de taxa; para a base, é a consulta do que o GPT-6 Astra faz e não faz pela API.

## O modelo

| Item | Fato |
|---|---|
| ID | `gpt-6-astra` |
| Snapshot padrão | `gpt-6-astra` (o único listado) |
| Entrada | texto, imagem |
| Saída | texto |
| Janela de contexto | 1.050.000 tokens |
| Entrada máxima | 922.000 tokens |
| Saída máxima | 128.000 tokens |
| Corte de conhecimento | 30/04/2026 |
| Tokens de raciocínio | sim |
| `reasoning.effort` | `low`, `medium`, `high`, `xhigh`, `max` |
| Usos que a página indica | raciocínio complexo, código, uso de computador, pesquisa, criação de documentos |
| Data de lançamento | não informada |

## Preço (texto, por 1 milhão de tokens)

| Métrica | Preço |
|---|---|
| Entrada | US$ 10 |
| Entrada em cache | US$ 1 |
| Escrita em cache | US$ 12,50 (1,25× a entrada sem cache) |
| Saída | US$ 50 |
| Prompt acima de 272 mil tokens de entrada | entrada e cache 2×, saída 1,5×, no pedido inteiro |
| Batch e Flex | 50% do Standard |
| Modo Fast | 2× o preço que se aplica |
| Modelos de ferramenta (busca, uso de computador) | taxa por chamada (página de preços) |

## Endpoints

| Endpoint | Rota | Estado |
|---|---|---|
| Chat Completions | `v1/chat/completions` | suportado |
| Responses | `v1/responses` | suportado |
| Batch | `v1/batch` | suportado |
| Live | `v1/live/sessions` | não suportado |
| Realtime | `v1/realtime` | não suportado |
| Realtime translation | `v1/realtime/translations` | não suportado |
| Realtime transcription | `v1/realtime/transcription_sessions` | não suportado |
| Assistants | `v1/assistants` | não suportado |
| Fine-tuning | `v1/fine-tuning` | não suportado |
| Embeddings | `v1/embeddings` | não suportado |
| Image generation | `v1/images/generations` | não suportado |
| Image edit | `v1/images/edits` | não suportado |
| Videos | `v1/videos` | não suportado |
| Speech generation | `v1/audio/speech` | não suportado |
| Transcription | `v1/audio/transcriptions` | não suportado |
| Translation | `v1/audio/translations` | não suportado |
| Moderation | `v1/moderations` | não suportado |
| Completions (legado) | `v1/completions` | não suportado |

## Recursos e ferramentas

| Recursos suportados | Ferramentas na Responses API |
|---|---|
| `streaming` | `web_search` |
| `structured_outputs` | `file_search` |
| `function_calling` | `image_generation` |
| `file_search` | `code_interpreter` |
| `image_input` | `hosted_shell` |
| `web_search` | `apply_patch` |
| `prompt_caching` | `skills` |
| — | `computer_use` |
| — | `mcp` |
| — | `tool_search` |

## Nuvens e limites de taxa

| Provedor | ID do modelo | Estado |
|---|---|---|
| Amazon Bedrock | `openai.gpt-6-astra` | — |
| Google Cloud | `gpt-6-astra` | prévia privada |

| Nível (Standard) | Pedidos por minuto | Tokens por minuto | Fila do Batch |
|---|---|---|---|
| Build | 5.000 | 1.000.000 | 3.000.000 |
| Launch | 10.000 | 4.000.000 | 200.000.000 |
| Grow | 15.000 | 40.000.000 | 15.000.000.000 |

## O que a fonte recomenda

Pelo que a página documenta, o modelo devolve só texto, em três endpoints (chat, Responses e Batch), e as ferramentas, a de gerar imagem entre elas, valem pela Responses API, não pelos endpoints de imagem e vídeo, marcados como não suportados.

## Citações

- "Tools supported by this model when using the Responses API."
- "Prompts with more than 272K input tokens are priced at 2x input and cache rates and 1.5x output for the full request."

## Lacuna

A página não diz quando o modelo foi lançado, se tem data de descontinuação, nem quanto custa cada chamada da ferramenta `image_generation` ou que modelo de imagem ela usa. Não fala de saída em vídeo, áudio ou 3D além da tabela de endpoints, não dá limites de taxa por dia, e não diz o que muda entre a OpenAI e as duas nuvens além do ID.
