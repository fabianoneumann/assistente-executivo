# Modelos de vídeo por API: o que roda por baixo dos agregadores, quanto custa e o que não transfere

Levantamento motivado por uma pergunta específica: **integrar direto com os modelos de vídeo em vez de assinar um agregador como o Higgsfield.** A resposta curta é que dá, é barato, e o que se perde é uma camada bem identificável. A leitura mais recente das páginas vem logo abaixo; a anterior segue depois dela, como histórico, porque preços e versões mudam rápido e a comparação entre as duas mostra o quanto. Como estes modelos serviriam ao ambiente de uma cena feita em código (laço de fundo, rascunho de movimento, blocagem como referência) e os testes propostos estão em [[video-gerado-no-ambiente-da-cena]]. Como cada um recebe a referência de um personagem (o close e o corpo inteiro do Seedance 2.0, o *element* do Kling, o teto do Omni Flash, o Soul ID do Higgsfield) e o que se mediu da consistência entre planos estão em [[personagem-consistente]].

## A leitura mais recente: Kling 4.0, Seedance 2.5 e Veo 3.1 fora da Gemini API

Lida na documentação dos fabricantes e nas páginas dos agregadores; nenhuma geração. Três mudanças em relação à leitura anterior: o **Kling 4.0** chegou à API (completa em 28/10/2026; o 4.0 Flash em 04/11); o **Seedance 2.5** (lançado em 31/07/2026) tem a API aberta na BytePlus ModelArk; e a **Veo 3.1 Preview da Gemini API foi desligada em 22/10/2026**, com a ordem de migrar para o Gemini Omni Flash ou para os modelos GA do Vertex ([[2026-11-11-kling-api-4-0-versoes-e-precos]], [[2026-11-11-seed-seedance-2-5-lancamento]], [[2026-11-11-byteplus-seedance-2-5]], [[2026-11-11-gemini-api-veo-desligado-e-omni-flash]]).

### O que cada um faz de pronto

| | Kling 4.0 | Seedance 2.5 | Veo 3.1 (Vertex) | Gemini Omni 1.2 Flash |
|---|---|---|---|---|
| Duração por geração | 3 a 30 s (Flash: 3 a 20 s) | 4 a 30 s, com extensão | 4, 6 ou 8 s (8 s com imagem de referência) | 3 a 15 s; extensão por turnos até 30 s |
| Resolução | 720p e 1080p (Flash só 720p) | 480p, 720p, 1080p (10 bits) | Standard até 4K; Fast e Lite até 1080p; 24 fps | 720p por padrão (também 360p); 1080p e 4K por upscaling |
| Vertical | 9:16, 21:9, 16:9, 1:1, `adaptive` | sete proporções; com quadro inicial, `adaptive` segue a imagem | 9:16 e 16:9 | 9:16 e 16:9 |
| Quadros | primeiro, do meio e último, até 10 imagens (Flash: só o primeiro) | primeiro, ou primeiro e último | primeiro e último | primeiro e último (3 a 10 s) |
| Referência e movimento | Omni: até 10 imagens, 5 vídeos, 7 "elements"; movimento por `feature_video`; Motion Control dedicado só no 3.0 e no 2.6 | até 50 referências (30 imagens, 10 vídeos, 10 áudios), inclusive "clay render" de blocagem | "asset images" (não no Lite, e a página não diz quantas); vídeo só de saída | até 6 imagens; vídeos de referência de até 3 s |
| Edição de vídeo | por prompt sobre `base_video`; edição de elementos à parte | por prompt sobre um vídeo de 4 a 30 s, por marca de tempo: troca de sujeito, objetos, trecho do quadro e áudio, ou só a câmera | não; estende vídeo ("Extend videos: Supported") | conversacional, sobre vídeo enviado de até 15 s (não em todas as regiões) |
| Áudio e língua | nativo; voz ligada ao element | gerado junto; 11 línguas, inclusive o português | com e sem, a preços diferentes; prompt só em inglês | nativo |
| Particular | 4K na tabela de capacidades e "coming soon" na nota de lançamento, sem preço (contradição da própria doc) | **rascunho** a 480p antes do final, com o ID válido 14 dias, e o final sobre o rascunho só em 1080p; também na fal (fora dos endpoints dos EUA), não no Replicate | GA `veo-3.1-generate-001` e `-fast-` (17/11/2025, retirada "May 4, 2027 or later"); Lite em Preview | GA em 05/11/2026; só no nível pago |

Fontes da tabela: [[2026-11-11-kling-api-4-0-versoes-e-precos]], [[2026-11-11-kling-api-omni-e-motion-control]], [[2026-11-11-byteplus-seedance-2-5]], [[2026-11-11-seed-seedance-2-5-lancamento]], [[2026-11-11-google-cloud-veo-3-1]], [[2026-11-11-gemini-api-veo-desligado-e-omni-flash]].

### Preço por segundo

Direto no fornecedor ([[2026-11-11-kling-api-4-0-versoes-e-precos]], [[2026-11-11-byteplus-seedance-2-5]], [[2026-11-11-vertex-precos-video]]; o Omni pela página de preços da Gemini API, [[2026-11-11-gemini-api-precos-imagem-e-video]]):

| Modelo e via | Preço | Condição |
|---|---|---|
| Kling 4.0, API Kling | US$ 0,157 (720p), 0,235 (1080p) | sem vídeo de entrada |
| Kling 4.0, API Kling | US$ 0,094 (720p), 0,141 (1080p) | com vídeo de entrada: se a entrada é mais longa que a saída, cobra a soma das duas; se não, a saída em dobro |
| Kling 4.0 Flash, API Kling | US$ 0,094 (720p); 0,063 com vídeo | mesma regra |
| Kling 3.0, API Kling | US$ 0,084 / 0,112 / 0,42 (720p / 1080p / 4K) sem áudio; 0,126 / 0,168 / 0,42 com | em units de pacote; o unit vale cerca de US$ 0,14 no 3.0 e 0,157 no 4.0, pela divisão das células |
| Seedance 2.5, BytePlus | US$ 10,70 por milhão de tokens (480p e 720p), 11,70 (1080p); com vídeo de entrada 6,40 e 7,00 | tokens ≈ (duração da entrada + da saída) × largura × altura × fps / 1024; pelo exemplo da página, 5 s em 16:9 saem a 0,103 / 0,231 / 0,569 por segundo (480p / 720p / 1080p) |
| Veo 3.1, Vertex | US$ 0,40 com áudio, 0,20 sem (720p e 1080p); 4K 0,60 e 0,40 | a tabela cobra "por count", sem definir a unidade |
| Veo 3.1 Fast, Vertex | US$ 0,10 / 0,12 / 0,30 com áudio (720p / 1080p / 4K); 0,08 / 0,10 / 0,25 sem | idem |
| Veo 3.1 Lite, Vertex | US$ 0,05 / 0,08 com áudio (720p / 1080p); 0,03 / 0,05 sem | idem |
| Gemini Omni 1.2 Flash, Gemini API | US$ 12 por milhão de tokens de vídeo: cerca de 0,07 (720p), 0,104 (1080p), 0,209 (4K) | 5.792 tokens por segundo a 720p, pela conversão da própria página |

Nos agregadores ([[2026-11-11-replicate-precos-video]], [[2026-11-11-fal-precos-video]]):

| Modelo | fal.ai | Replicate |
|---|---|---|
| Veo 3.1 | 0,20 sem áudio, 0,40 com (720p e 1080p); 4K 0,40 e 0,60; **obsoleto (deprecated) em 17/11/2026** | 0,20 e 0,40 |
| Veo 3.1 Fast | 0,10 e 0,15 (720p e 1080p); 4K 0,30 e 0,35; **removido em 17/11/2026** | não aberto |
| Seedance 2.5 | US$ 0,0214 por mil tokens: cerca de 0,22 (480p), 0,47 (720p), 1,16 (1080p) pela tabela (o exemplo da própria página dá uns 0,46 a 720p); vídeo de entrada multiplica por 0,6 | 0,1028 (480p), 0,2312 (720p); com vídeo de entrada, 0,4304 e 0,9676 por segundo de saída (a página não diz se a entrada conta); sem 1080p |
| Kling 4.0 | o preço da Kling, mas na leitura só no playground, "API access coming soon" | `kwaivgi/kling-v4.0` ao preço da Kling, com a mesma regra do dobro |
| Kling 3.0 | não reaberto (0,112 e 0,168 na leitura anterior, abaixo) | standard 0,168 sem áudio e 0,252 com; pro 0,224 e 0,336 |

Leitura do assistente: sem vídeo de entrada, o Replicate cobra Seedance 2.5, Veo 3.1 e Kling 4.0 pelo preço do fornecedor (e o Kling 3.0 pelo dobro); a fal cobra o Seedance 2.5 pelo dobro da BytePlus e o Veo 3.1 Fast acima do Vertex. Com vídeo de entrada, o Replicate cobra o Seedance 2.5 a preço fixo por segundo de saída, e a página não diz se os segundos de entrada entram: se não entram, 5 s de entrada e 5 de saída a 480p dão US$ 2,15 no Replicate contra 0,615 na BytePlus, cerca de 3,5 vezes. O que ficou aberto na leitura anterior (a fal 30 a 50% mais barata que o Replicate, de resposta sem fonte, abaixo) não se sustenta nestes modelos: nos lidos, a fal cobra igual ou mais. Nenhuma página lida diz em texto se Replicate e fal são crédito pré-pago ou fatura (os dados embutidos nas páginas trazem campos como `requiresCredit` no Replicate e `paywall-credit-plans` na fal, sem explicação), e é isso que decide se a via precisa de trava de custo antes de um teste longo; ver [[video-gerado-no-ambiente-da-cena]]. Os comparativos de revendedores que as buscas trouxeram (PoYo, Kie, Atlas Cloud e outros) não foram lidos, e os números deles que vieram nas respostas não batem com as primárias.

**Para abrir uma conta:** a Kling debita units de um pacote de recursos (o changelog cita também débito de saldo), e a documentação não dá o preço, o tamanho mínimo nem a validade do pacote; a BytePlus pede, numa nota do tutorial, saldo acima de US$ 30, plano de US$ 30 ou pacote de recursos ("one of the following conditions"), e no passo 3 do mesmo tutorial diz que sem pacote de recursos não se ativa (contradição não resolvida); o Vertex é pós-pago, e a página do Veo marca "Pay-as-you-go" como "Not supported" e "Fixed quota" como "Supported", enquanto a tabela de preços do Vertex cobra o Veo por uso; o impacto disso numa chamada avulsa não foi conferido ([[2026-11-11-google-cloud-veo-3-1]], [[2026-11-11-vertex-precos-video]]). O Omni Flash é do nível pago da Gemini API, pelo AI Studio, que é crédito.

### Rosto real

O Seedance 2.5 e o 2.0 não aceitam imagem nem vídeo de referência com rosto humano real; as saídas da BytePlus são rosto gerado na própria conta, personagem pronto da plataforma ou pessoa real verificada e autorizada ([[2026-11-11-byteplus-seedance-2-5]]). Do Veo, só o FAQ da página da fal diz algo: o modelo recusa personagens parecidos com pessoas reais ou celebridades ([[2026-11-11-fal-precos-video]]); a página do Vertex não trata disso. Do Gemini Omni Flash, a documentação da Gemini API não aceita o envio nem a edição de imagem com "certain recognizable people", sem dizer quais, e restringe imagem de menores no Espaço Econômico Europeu, na Suíça e no Reino Unido ([[2026-11-11-gemini-api-veo-desligado-e-omni-flash]]). A documentação da Kling não traz regra de rosto real, e não se verificou se a moderação do Seedance vale igual pelo Replicate e pela fal. Antes disso vem uma regra de produção: **foto real de pessoa não vai a modelo nenhum** (nunca retrato gerado de pessoa real; foto é documento), e o que se gera é só desenho, cenário sem pessoas ou blocagem em código ([[video-gerado-no-ambiente-da-cena]]).

### O que o Higgsfield monta por cima

Pelo catálogo da Higgsfield API, pela documentação e pelo blog ([[2026-11-11-higgsfield-recursos-e-modelos]]):

- **Próprio:** o **Genjutsu** (`higgsfield/genjutsu/motion-transfer/v1.0`: transferência de movimento, troca de objeto e de elenco, restyle com 20 estilos prontos, sobre vídeo de 4 a 30 s, até 1080p; no app, uma transferência de 15 s sai por cerca de US$ 2,21 a 480p e 14,70 a 1080p; na API, "from 0.154 / s" como vídeo e "from 0.318 / s" como fluxo), o Cinema Studio 4.0, o Soul ID (rosto treinado e reutilizável), o 3D Jutsu (cena 3D editável para posicionar objetos, luz e câmera antes do vídeo). Nenhuma das páginas diz em que modelo de base rodam o Genjutsu, o Cinema Studio, o 3D Jutsu ou o Draw to Video (este só aparece pelo nome no changelog); o guia chama de nativos o Soul, o Popcorn e o Higgsfield DOP. A versão barata do Genjutsu tem três descrições: o catálogo chama de "Genjutsu Light" e diz que usa os primeiros 15 s do vídeo; o blog chama de "Genjutsu Lite" e dá clipes de 4 a 30 s; o changelog, no lançamento, fala em vídeo de 4 a 15 s (não resolvido).
- **De terceiros, revendidos:** Seedance 2.5 ("from 0.118 / s"), Kling 4.0 e Flash ("from 0.126 / s" e 0,094), Kling Motion Control para transferir movimento, Wan para primeiro e último quadro; o Veo aparece no guia do app, não no índice da documentação da API nem nos 24 cartões lidos do catálogo (a página declara 26).
- **Acesso:** API e conector MCP (`https://mcp.higgsfield.ai/mcp`, pelo changelog, com o Cursor e o Manus depois, e o agente escolhendo o modelo); o Genjutsu está no MCP e na API.

Leitura do assistente: do que se procurava num agregador, o que não tem equivalente com nome nas três APIs diretas é o Genjutsu como produto (troca de elenco num vídeo inteiro mantendo câmera e áudio); as peças existem direto (Kling 4.0 Omni com `base_video` e `feature_video`, Kling Motion Control 3.0, Seedance 2.5 com edição sobre vídeo de referência). Se a qualidade é a mesma, só um teste diz. A camada de curadoria da leitura anterior (abaixo) continua sendo o que o agregador vende.

## A leitura anterior (histórico)

O estado anterior e o teste do Neo Stitch, como estavam. Preços e versões acima substituem os daqui quando divergem.

### O agregador é uma casca sobre modelos de terceiros, mais os próprios

A referência técnica do CLI da Higgsfield (*Higgsfield CLI — Video Models (referência técnica dos IDs de modelo)*, de DeepWiki, https://deepwiki.com/higgsfield-ai/cli/3.2-video-models) lista os IDs reais e separa as duas coisas:

**De terceiros:** `veo_3`, `veo_3_1`, `veo_3_1_lite` (Google), `kling_2_6`, `kling_3_0`, `wan_2_6`, `wan_2_7`, `minimax_hailuo`, `grok_video`.

**Proprietários:** `cinematic_studio_video`, `cinematic_studio_video_v2`, `cinematic_studio_3_0`, `soul_cast`, `marketing_studio_video`.

O case study da NVIDIA (*NVIDIA case study — Higgsfield Scales Video Production With NVIDIA AI*, de NVIDIA, https://www.nvidia.com/en-us/case-studies/higgsfield/) confirma pelo lado da empresa (SOUL e SOUL 2 são modelos próprios, text-to-image) e declara a estratégia sem rodeios: *"By utilizing proprietary models alongside industry leaders like Veo and Kling, Higgsfield ensures that no creative detail is lost."* A mesma fonte dá a dimensão do que é construído por cima: **1.296 lentes de câmera e parâmetros cinematográficos**, servindo 22 milhões de usuários e 6+ milhões de peças por dia.

**Consequência para quem quer ir direto:** os modelos de vídeo são commodity acessível. O que pertence ao agregador é a camada de curadoria: presets de câmera, consistência de personagem (Soul Cast), templates de marketing. Integrar direto entrega a capacidade bruta e devolve a você a tarefa de construir essa camada. Se construir a camada **é** o objetivo, o agregador vira redundante; se não for, ele está vendendo justamente o que falta.

### Preços, e uma unidade de conta que muda a percepção

Da fal.ai, agregador de API (não de UI), verificado em duas páginas oficiais (*fal.ai — Pricing: tabela de modelos de vídeo e modelo de cobrança*, de fal.ai, https://fal.ai/pricing; e *fal.ai — Image to Video APIs: modelos, preços e controle de frame*, de fal.ai, https://fal.ai/explore/image-to-video-apis):

| Modelo | Preço | Notas |
|---|---|---|
| Wan 2.5 | $0,05/s | mais barato; 20s por dólar |
| Kling 2.5 Turbo Pro | $0,35 por 5s, depois $0,07/s | |
| Kling 3.0 Pro | $0,112/s sem áudio · $0,168/s com áudio · $0,196/s com voice control | |
| Seedance 2.0 Fast | $0,2419/s a 720p, áudio incluso | |
| Seedance 2.0 | $0,3024/s a 720p, áudio incluso | |
| Veo 3.1 | $0,20/s sem áudio · $0,40/s com áudio | |
| Veo 3 | $0,40/s | 3s por dólar |
| Ovi | $0,20 por vídeo | |

Cobrança **por output**, não por tempo de GPU, e geração que falha não é cobrada.

Traduzindo para peça: um b-roll de 5 segundos custa **$0,25 em Wan 2.5** ou **$0,35 em Kling 2.5 Turbo**. Um vídeo curto de 30 segundos montado com seis clipes de 5s sai por **$1,50 a $2,25**. Ordem de grandeza: poucos reais por peça, o que coloca a geração de vídeo abaixo do custo de quase qualquer alternativa de produção.

### Controle de frame: o achado que conecta imagem e vídeo

Três dos modelos aceitam **imagem inicial e imagem final**, não só a inicial:

- **Kling 3.0 Pro**: `end_image_url`
- **Seedance 2.0**: `image_url` **e** `end_image_url`, para transições início→fim
- **Veo 3.1**: endpoints dedicados de first-last-frame

Isso transforma "efeito e transição a partir de imagens" de um recurso de plataforma num par de chamadas de API: gera-se o frame de entrada e o de saída com um modelo de imagem, e o modelo de vídeo interpola o movimento entre os dois. É a ponte natural entre uma skill de geração de imagem e uma de vídeo.

### Trocar de modelo é barato por design

Da própria fal: *"once you've integrated one, switching between Seedance 2.0, Kling 3.0 Pro, or Veo 3.1 is a one-line endpoint change."* O padrão de API é consistente entre modelos, o que favorece uma arquitetura de provider fina em vez de integrações separadas por fornecedor, e permite rodar o mesmo prompt em vários modelos para comparar saída.

### Sora 2 saiu do ar em 24/09/2026

Confirmado na primária (*OpenAI — Deprecations: Videos API e Sora 2 removidos em 24/09/2026*, de OpenAI, https://developers.openai.com/api/docs/deprecations): a OpenAI notificou desenvolvedores em 24/03/2026 e remove em **24 de setembro de 2026** a Videos API, `sora-2`, `sora-2-pro` e os snapshots datados. **Nenhum substituto foi designado.** O app e a web do Sora já haviam encerrado em 26/04/2026.

Duas implicações: não construir nada novo em cima do Sora, e notar que agregadores que anunciam Sora 2 no catálogo perderam essa perna em setembro.

### Image-to-video em tela de interface: o teste do Neo Stitch

Quando a imagem é uma tela de interface, o critério muda: não é o vídeo mais bonito, é o que não mexe em texto e layout. O catálogo do Neo Stitch testa 25 modelos do OpenRouter por esse critério ([[2026-10-30-neo-stitch-readme]]); custo de 6 s a 720p:

| Modelo | Custo | Veredito |
|---|---|---|
| Hailuo 3 | ~US$ 0,78 | o mais fiel, texto e layout intactos |
| Hailuo 3 Max | ~US$ 0,48 | estável e barato; às vezes troca números |
| Seedance 2.5 | ~US$ 1,39 | sutil e fiel |
| Wan 3.0 / 3.0 Prime | ~US$ 0,51 / 0,84 | bonitos, mas acendem tudo e trocam rótulos |
| Grok Imagine 1.5 Lite | ~US$ 0,19 | rascunho; exagera no movimento |

Reescreveram a tela, mudaram gráficos ou deformaram texto: Seedance 2.0 Mini e 1.5 Pro, Runway Gen-4.5, **Kling 3.0 Pro**, Veo 3.1 Lite; Veo 3.1 ficou estável. É o teste de um autor, em poucas telas (quatro, pelo README), e os preços são do OpenRouter, não da fal acima. As travas de prompt que seguram a tela são as do próprio README: câmera fixa, texto intacto, só se mexe o que for nomeado.

### Aberto e não verificado

**Runway e Luma no Higgsfield.** O CLI, a fonte técnica mais forte, **não lista** nenhum dos dois. Um post do blog da própria Higgsfield menciona "Runway Gen-4.5", mas em contexto de guia comparativo, o que não é catálogo. Fica: ausentes do CLI, presença na web app não confirmada.

**fal × Replicate.** A afirmação de que a fal é 30 a 50% mais barata e de que o Replicate cobra por GPU-segundo com "cold start tax" veio de resposta **sem grounding** e não fechou em fonte. Não usar para decidir sem verificar.
