---
titulo: "Element Management (Kling API, 4.0)"
tipo: artigo
autor: "Kling AI (documentação oficial da API)"
url: "https://kling.ai/document-api/api/video/4-0/elements.md"
publicado_em: null   # a página não traz data
capturado_em: 2026-11-12
licenca: "protegida: a versão Markdown oficial não declara licença (valem os termos do site da Kling); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [kling, kling-api, elements, character-consistency, reference-images, voice-binding]
---

# Kling API 4.0: o que entra num *element* de personagem

Nota de fato: tabelas do que a página registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** A aba "Element Management" da documentação da API da Kling para o 4.0, baixada na versão Markdown que a própria documentação oferece ("optimized for LLMs", com as abas expandidas) em 12/11/2026 (440 linhas, `sha256` (hash omitido)), e lida inteira: criar, consultar (um e lista), listar os prontos e apagar. A página do 3.0 Omni (`.../3-0-omni/elements.md`), baixada no mesmo dia, é igual linha a linha, fora a URL de origem e a lista de abas irmãs (a do 3.0 tem também Motion Control); por isso não tem ficha própria. Formato: nota de fato, por ser documentação técnica (`README.md` desta pasta, item 2), organizada por tipo de *element* e por campo.

**Quem fala.** A Kling, que vende a API. A página avisa que o serviço de criação foi atualizado e leva a versão antiga por um link encurtado.

**Data.** A página não traz data.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa do corpo e as células com texto corrido; a célula que só traz um fato fica fora. Corpo: 3 frases de prosa e 3 tabelas, todas as células de fato (campo, valor, limite, rota; as três células de 8 palavras ou mais são listas de valores ou de passos). Resultado: 0 das 3 unidades segue uma frase da fonte; as duas citações estão à parte. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: a parte traduzida não se mede), 0 frase colada, e a conta lado a lado é a conferência.

## Em uma frase

Referência da API da Kling para criar e gerir *elements*, o recurso que guarda um personagem, objeto ou cenário para reusar nas gerações; a página dá os campos, os limites dos arquivos e a regra de quem pode ser criado por vídeo.

## Os dois tipos de *element*

| Campo | Por imagens (`image_refer`) | Por vídeo (`video_refer`) |
|---|---|---|
| Nome na página | Multi-Image Elements | Video Character Elements |
| Lista obrigatória | `element_image_list` | `element_video_list` |
| Imagem frontal | obrigatória (`frontal_image`) | — |
| Outras imagens | 1 a 3 (`refer_images`), diferentes da frontal |  — |
| O que as outras mostram | outros ângulos ou close | — |
| Formatos | JPG, JPEG, PNG | MP4, MOV |
| Tamanho máximo | 10 MB por imagem | 200 MB |
| Dimensão mínima | 300 px | — |
| Proporção | de 1:2,5 a 2,5:1 | 16:9 ou 9:16 |
| Duração | — | 3 a 8 s |
| Resolução | — | 1080p |
| Quantidade | 1 frontal + até 3 | 1 vídeo |
| Envio | Base64 ou URL | URL |
| Quem pode | (a página não restringe) | só figura humanoide de estilo realista |
| Modelos | (a página não restringe) | `kling-video-o3` e posteriores |
| Fala no vídeo | — | cria uma voz, põe na biblioteca e liga ao *element* |

## Os outros campos da criação

| Campo | Fato |
|---|---|
| Rota | `POST /v1/general/advanced-custom-elements` |
| `element_name` | obrigatório; até 20 caracteres |
| `element_description` | obrigatório; até 100 caracteres |
| `element_voice_id` | opcional; liga a uma voz da biblioteca |
| Voz em *element* de imagens | só personagem ou humanoide |
| Sem `element_voice_id` | sem voz |
| `tag_list` | opcional; várias etiquetas por *element* |
| `o_101` | Hottest |
| `o_102` | Character |
| `o_103` | Animal |
| `o_104` | Item |
| `o_105` | Costume |
| `o_106` | Scene |
| `o_107` | Effect |
| `o_108` | Others |
| `callback_url` | opcional; aviso de mudança de estado |
| `external_task_id` | opcional; único por conta |
| Estados da tarefa | submitted, processing, succeed, failed |

## Consultar, listar e apagar

| Operação | Rota |
|---|---|
| Consultar um | `GET /v1/general/advanced-custom-elements/{id}` (`task_id` ou `external_task_id`) |
| Listar os próprios | `GET /v1/general/advanced-custom-elements` |
| Listar os prontos da Kling | `GET /v1/general/advanced-presets-elements` |
| Página da lista | `pageNum` 1 a 1.000; `pageSize` 1 a 500, padrão 30 |
| Apagar | `POST /v1/general/delete-advanced-elements` (só os próprios) |
| Resposta da consulta | o *element*, a voz ligada, a dedução em units e em saldo |
| `owned_by` | `kling` para a biblioteca oficial |

## O que a fonte recomenda

A página é de referência e quase não recomenda: o que ela deixa como regra é montar o personagem por uma imagem de frente e até três de outros ângulos ou de close, reservar o vídeo ao humanoide realista nos modelos do O3 em diante, e dar nome e descrição curtos.

## Citações

- "at least one frontal reference image (frontal_image), and 1 to 3 additional reference images (image_url) that differ from the front." (`element_image_list`)
- "Currently, only realistic-style humanoid figures can be customized through video." (`element_video_list`)

## Lacuna

A página não diz quanto custa criar um *element* pela API, quantos cabem numa geração, se o personagem desenhado vale igual ao realista no *element* por imagens, nem como os ângulos ajudam a identidade.
