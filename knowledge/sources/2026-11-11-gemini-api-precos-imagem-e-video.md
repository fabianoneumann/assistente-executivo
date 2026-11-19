---
titulo: "Gemini Developer API pricing: imagem (Nano Banana 2.1, 2, 2 Lite, Pro e 2.5 Flash Image) e vídeo (Omni 1.2 e 1.1 Flash)"
tipo: artigo
autor: "Google (documentação oficial da Gemini API)"
url: "https://ai.google.dev/gemini-api/docs/pricing"
publicado_em: null   # a versão .md.txt lida não traz data de atualização
capturado_em: 2026-11-11
licenca: "em dúvida: a versão .md.txt baixada não traz o rodapé de licença do Google Developers; o HTML de /pricing, baixado com curl na revisão de 11/11/2026, redireciona para aistudio.google.com/docs/pricing, app em JavaScript, sem rodapé no que o curl devolve, e a página não tem cópia na Wayback; falta conferir no Chrome se o texto é CC BY 4.0. Tratada como protegida: ficha em palavras próprias, sem o integral"
areas: [generative-media, content-design]
tags: [gemini-api, pricing, nano-banana, image-generation, video-generation, gemini-omni, batch-api, google-ai-studio]
---

# Preços da Gemini API em 11/11/2026: imagem e vídeo

Ficha de estudo das seções de imagem e de vídeo da página de preços da Gemini API, organizada por pergunta (quanto custa a imagem, quanto custa o vídeo, o que vale para todos), não pela ordem da página. Não há integral: a licença do texto lido está em dúvida.

**Proveniência.** Versão em markdown da página (`https://ai.google.dev/gemini-api/docs/pricing.md.txt`), baixada com curl em 2026-11-11, sem cópia na Wayback. A mesma página está nas duas rodadas de 11/11 (A, o ambiente das cenas; B, os modelos de vídeo em novembro), e esta ficha serve às duas. **Cobertura:** lidos o cabeçalho dos planos, as seções dos cinco modelos de imagem (Nano Banana 2.1, Nano Banana 2, Nano Banana 2 Lite, Nano Banana Pro e Gemini 2.5 Flash Image; a deste último entrou na revisão de 11/11), as duas do Gemini Omni Flash (1.2 e 1.1), "Pricing for tools", "Pricing for agents" e "Notes"; as seções dos modelos de texto, áudio, TTS, Live, embeddings, Lyria, robótica e Gemma não foram lidas em detalhe e ficam fora desta ficha. Uma busca no arquivo inteiro por "Veo" e por "Imagen" não acha nenhuma ocorrência.

## Quanto custa a imagem

Todos os preços são do nível pago, em US$ por milhão de tokens, e a página converte a saída de imagem em preço por imagem. Nenhum dos cinco tem nível gratuito na API ("Not available" na coluna Free Tier).

| Modelo (id) | Entrada | Saída de texto e pensamento | Saída de imagem | Por imagem (Standard) | Lote (Batch) |
|---|---|---|---|---|---|
| Nano Banana 2.1 (`gemini-nano-banana-2.1`) | 1,50 (texto, imagem, vídeo) | 7,50 | 30 | 0,0336 a 1K; 0,0504 a 2K; 0,113 a 4K | metade: entrada 0,75, texto 3,75, imagem 15 (0,0168, 0,0252 e 0,0567 por imagem) |
| Nano Banana 2 (`gemini-3.1-flash-image`) | 0,50 (texto, imagem) | 3 | 60 | 0,045 a 0,5K; 0,067 a 1K; 0,101 a 2K; 0,151 a 4K | a seção só tem a aba Standard |
| Nano Banana 2 Lite (`gemini-3.1-flash-lite-image`) | 0,25 (texto, imagem, vídeo) | 1,50 | 30 | 0,0336 a 1K (a única resolução da tabela) | entrada 0,125, texto 0,75, imagem 15 (0,0168 a 1K) |
| Nano Banana Pro (`gemini-3-pro-image`) | 2,00 (texto, imagem), ou US$ 0,0011 por imagem de entrada (560 tokens) | 12 | 120 | 0,134 a 1K ou 2K; 0,24 a 4K | a seção só tem a aba Standard |
| Gemini 2.5 Flash Image, o Nano Banana original (`gemini-2.5-flash-image`) | 0,30 (texto, imagem) | como o Gemini 2.5 Flash, diz a seção | 30 | 0,039 até 1024×1024 | entrada 0,15 e 0,0195 por imagem; é o único modelo de imagem com as abas Flex (igual ao lote) e Priority (entrada 0,54, 0,0702 por imagem) |

**De onde sai o preço por imagem** (notas de rodapé de cada seção): é o número de tokens que a imagem de saída consome vezes a tarifa. No 2.1, 1.120 tokens a 1K (1024×1024), 1.680 a 2K (2048×2048) e 3.780 a 4K (4096×4096); no Nano Banana 2, 747 a 0,5K (512 px), 1.120 a 1K, 1.680 a 2K e 2.520 a 4K; no Lite, 1.120 a 1K; no Pro, 1.120 para qualquer saída de 1K até 2K e 2.000 até 4K; no 2.5 Flash Image, 1.290 até 1024×1024. O Pro cobra texto de entrada e de saída como o Gemini 3.1 Pro, diz a própria seção.

**Como cada modelo se apresenta na página:** o 2.1 é "uma atualização do Nano Banana 2", feita para gerar e editar por conversa com qualidade visual melhor, consistência de personagem em vários turnos, texto legível e geração apoiada em busca, a 1K, 2K e 4K; o Nano Banana 2, para resposta rápida e muito volume; o Lite, o "especialista em eficiência" da família, de latência ultrabaixa; o Pro, o modelo nativo de imagem "otimizado para velocidade, flexibilidade e compreensão de contexto", a mesma frase que apresenta o 2.5 Flash Image. Este vem com um aviso: está descontinuado, sai do ar em 15/03/2027, e a página manda migrar para o Gemini 3.1 Flash Lite Image (o Nano Banana 2 Lite).

**Busca como apoio (grounding):** no 2.1 e no Nano Banana 2, a busca na web e de imagens do Google; no Pro, a busca do Google. Nos três, 5.000 buscas grátis por mês, divididas entre todos os modelos Gemini 3 em diante, e depois US$ 14 por mil, com teto padrão de 1.500 por dia por projeto; cada consulta de busca que o pedido gerar é cobrada, e o contexto que a busca traz não conta como token de entrada. A busca no Pro, sem nível gratuito na API, "pode ser testada no Google AI Studio".

## Quanto custa o vídeo

A página de preços tem dois modelos de geração de vídeo, os dois do nível pago e sem nível gratuito:

- **Gemini Omni 1.2 Flash** (`gemini-omni-1.2-flash`): descrito como o modelo de "nova geração" para gerar e editar vídeo de até 15 segundos com áudio nativo, "generally available" no nível pago. Entrada a US$ 1,50 por milhão (texto, imagem, vídeo); saída a US$ 9 (texto, incluindo o pensamento) e **US$ 12 por milhão de tokens de vídeo**. A cobrança é pelo total de tokens de saída, a 5.792 tokens por segundo de vídeo em 720p, o que a página converte em cerca de US$ 0,07 por segundo (cerca de US$ 0,70 por clipe de 10 s e US$ 1,04 por clipe de 15 s); em 360p, 1.931 tokens por segundo (US$ 0,023/s); em 1080p com upsampling, 8.688 (US$ 0,104/s); em 4K com upsampling, 17.376 (US$ 0,209/s). A seção só tem a aba Standard.
- **Gemini Omni 1.1 Flash** (`gemini-omni-1.1-flash`), a geração anterior: mesma entrada, saída de vídeo a US$ 17,50 por milhão, à mesma taxa de 5.792 tokens por segundo em 720p, cerca de US$ 0,10 por segundo. A partir de 3 de dezembro de 2026, todo pedido a ele vai sozinho para o 1.2 e é cobrado pela tarifa do 1.2.

**O que a tabela não tem:** nenhum modelo Veo e nenhum Imagen aparecem na página de preços lida.

## O que vale para todos

- **Os três planos do cabeçalho:** Free (acesso limitado a certos modelos, tokens grátis, o AI Studio, e o conteúdo usado para melhorar os produtos do Google); Paid (limites maiores, cache de contexto, "Batch API (50% cost reduction)", os modelos mais avançados, e o conteúdo **não** usado para melhorar os produtos); Enterprise, pela Gemini Enterprise Agent Platform, com suporte, segurança, capacidade reservada e desconto por volume. A abertura fala em preço pré-pago e por uso ("prepaid and pay-as-you-go").
- **Ferramentas** ("Pricing for tools"): cada uma pelo próprio preço, aplicado ao modelo que a usa. A execução de código é grátis no nível gratuito e, no pago, cobrada pela tarifa de tokens do modelo, sem cobrança pelo tempo de sessão (o código gerado e o resultado contam como saída quando criados e como entrada quando o modelo os relê); o contexto de URL conta como entrada; a busca de arquivos cobra as embeddings e os trechos recuperados.
- **Agentes** ("Pricing for agents"): o Deep Research, os agentes gerenciados e o Antigravity cobram a inferência pela tarifa de lista, inclusive os tokens intermediários dos laços; o processamento do ambiente dos agentes gerenciados não é cobrado durante a prévia.
- **Notas:** o uso do Google AI Studio é grátis em todas as regiões disponíveis; os preços podem diferir dos da Gemini Enterprise Agent Platform; tokens de documento (PDF) são cobrados pela tarifa de imagem; o teto padrão de 1.500 buscas por dia vale para todos os níveis pagos na Gemini Developer API, e quem precisa de mais é remetido à Vertex AI.
