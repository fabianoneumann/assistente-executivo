---
titulo: "Dreamina Seedance 2.5 tutorial (BytePlus ModelArk), com a seção de vídeo de Pricing e o guia Create portrait videos with Dreamina Seedance models"
tipo: artigo
autor: "BytePlus (documentação oficial do ModelArk)"
url: "https://ai.byteplus.com/ark/region:ap-southeast-1/docs/seedance-2-5"
capturado_em: 2026-11-11
licenca: "protegida: o Markdown oficial da BytePlus não declara licença (valem os termos do site); ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [seedance, byteplus, video-generation, api-pricing, image-to-video, first-last-frame, video-editing, video-extension, draft-mode, reference-images, multilingual, real-face-restriction]
---

# Seedance 2.5 na API da BytePlus: o tutorial, a tabela de preço de vídeo e a regra do rosto real

Ficha de estudo de três páginas da documentação do BytePlus ModelArk sobre o Seedance 2.5. Não há integral: o texto é protegido.

**Proveniência.** As três páginas foram baixadas na versão Markdown oficial (a própria documentação manda acrescentar `.md` à URL para obtê-la) em 11/11/2026:

- o tutorial, https://ai.byteplus.com/ark/region:ap-southeast-1/docs/seedance-2-5 (3.127 linhas);
- a tabela de preços, https://ai.byteplus.com/ark/region:ap-southeast-1/docs/model-pricing.md (561 linhas);
- o guia de retrato, https://ai.byteplus.com/ark/region:ap-southeast-1/docs/seedance-portrait-asset-guide.md (722 linhas).

**Quem fala.** A BytePlus, que vende o acesso ao modelo pela plataforma ModelArk: é a documentação do fornecedor da API, e os preços são os dele.

**Data.** Nenhuma das três páginas traz data de publicação ou de atualização. Ficam como dados da página, sem servir de data dela: o pacote de exemplo do tutorial se chama `modelark_seedance2.5_quickstart_package_arkruntime-20260909.zip`; o tutorial e a tabela de preço citam datas de vigência (o novo prazo do ID de rascunho vale a partir de 28/10/2026, e o Seedance 1.5 Pro sai do ar em 11/11/2026).

**Cobertura.** Do tutorial, todo o texto corrido, as tabelas e as notas, na ordem da página, e os exemplos em cURL de cada seção, lidos para os parâmetros; os mesmos exemplos em Python, Java e Go não foram lidos linha a linha, salvo o cabeçalho do Python (SDK e URL base). Da tabela de preços, a seção "Video generation models" inteira (preços, regras de cobrança e todos os exemplos) e as duas seções gerais do fim ("Rate limits" e "Billing notes"); o resto ficou fora (abaixo, em "O resto da página de preços"). Do guia de retrato, todo o texto e as tabelas; o código só para ver o modelo usado. As páginas para onde elas apontam (regras de ativação, API de criação de tarefa, guia geral de vídeo, guia de prompt, códigos de erro, biblioteca de personagens, cadastro de pessoa real, tabelas de consumo mínimo e calculadoras de preço) não foram abertas.

## 1. O tutorial, na ordem da página

### Abertura e condição de ativação

O tutorial apresenta o Seedance 2.5 (nome completo Dreamina Seedance 2.5) como o modelo de vídeo de nova geração da casa, com ganhos em narrativa longa, referência "omni" e edição: até 30 s de vídeo num pedido, extensão em várias rodadas, até 50 arquivos de referência por pedido e edição por marca de tempo. O alvo do tutorial é a chamada da API "Create video generation task".

Logo depois vem uma nota sobre a ativação: antes de habilitar o modelo, a conta precisa cumprir uma de três condições, nas palavras da página "one of the following conditions". As três são: saldo da conta BytePlus acima de US$ 30 (marcada "Recommended"), um AI Savings Plan dedicado na faixa de US$ 30 ou acima (também "Recommended"), ou um pacote de recursos ("resource pack") da série Seedance 2.5 com cota disponível. As regras detalhadas ficam numa página à parte, "Activate, use, and cancel Dreamina Seedance 2.5 and 2.0 series models", não aberta.

**Contradição interna do tutorial.** O passo 3 do "Getting started" (mais abaixo) trata o pacote de recursos como obrigatório: manda conferir que se comprou um pacote e conclui "Otherwise, you cannot activate Seedance 2.5." A nota do topo (l. 11 a 14 do markdown baixado) dá o pacote como uma de três alternativas; o passo 3 (l. 132), como condição única. O tutorial não resolve a diferença, e a página que a resolveria (l. 16) não foi aberta.

### Antes de usar: tipos de tarefa e as restrições de cada um

A página abre com um aviso de perigo: edição, primeiro/último quadro e extensão têm restrições próprias, e violá-las dá erro. O modelo decide o tipo de tarefa pelos arquivos de entrada e pela intenção do prompt.

| Tipo de tarefa | O que o dispara | Restrição |
|---|---|---|
| Texto para vídeo | só o prompt de texto | nenhuma sobre `ratio` ou `duration` |
| Primeiro quadro ou primeiro e último | `content.role` igual a `first_frame` ou `last_frame` | `ratio` tem de ser `adaptive`; a proporção da saída segue a imagem do `first_frame` |
| Referência "omni": referência para vídeo | ao menos um arquivo com `role` `reference_image`, `reference_video` ou `reference_audio` | nenhuma sobre `ratio` ou `duration` |
| Referência "omni": edição | ao menos um `reference_video` e um prompt com intenção de editar | `ratio` `adaptive` e `duration` `-1`; o vídeo de referência entre 4 e 30 s; o modelo escolhe pelo prompt qual vídeo editar e copia dele proporção e duração |
| Referência "omni": extensão | ao menos um `reference_video` e um prompt com intenção de estender | `ratio` `adaptive`; a proporção vem do vídeo escolhido |

O parâmetro `omni_reference_task_type` serve para declarar o subtipo e antecipar a validação. A página descreve três jeitos de configurar:

- **Sem declarar o subtipo:** `omni_reference_task_type` em `auto`, os papéis de referência no `content`, e a recomendação de `ratio` `adaptive` e `duration` `-1`, com vídeos de 4 a 30 s. Em `auto` o modelo pode classificar o pedido como referência, edição ou extensão, e a configuração recomendada já atende às restrições das duas últimas.
- **Edição** (trocar o sujeito, pôr ou tirar objetos, redesenhar ou reparar parte do quadro, mexer no áudio): valor `edit`, um `reference_video`, `ratio` `adaptive`, `duration` `-1`, vídeo de 4 a 30 s, e o prompt precisa conter uma palavra de edição (editar, adicionar, apagar ou remover, modificar, trocar, mudar). Exemplos dados: pôr bichinhos no @Video 1, trocar o personagem do @Video 1 pelo da @Image 1, tirar a música de fundo do @Video 1.
- **Extensão** (para a frente ou para trás): valor `extend`, um `reference_video`, `ratio` `adaptive`, e uma palavra de extensão no prompt (estender para a frente ou para trás, continuar, continuar a história).
- **Primeiro quadro ou primeiro e último:** uma imagem com `role` `first_frame`, e, para os dois quadros, outra com `last_frame`; `ratio` `adaptive`.

**Erros.** A validação acontece em dois momentos. Com `edit` ou `extend` declarados, a API confere as restrições na hora do envio e recusa de imediato; mesmo assim, se o modelo depois entender o prompt como outro tipo de tarefa, sai um erro assíncrono `InvalidParameter.TaskTypeMismatch`. Com `auto` ou sem o campo, e no caso de primeiro/último quadro, o modelo primeiro descobre o tipo e só então confere, e o erro vem depois que a tarefa começou, com o código `InvalidParameter.TaskTypeConstraint`.

### Começar a usar (Getting started)

Para quem não programa, a página indica o console do ModelArk (com modelos prontos, link com `model=dreamina-seedance-2-5-260628`); para testar chamadas, o API Explorer. O resto da seção é um passo a passo para iniciantes em Python:

1. ter conta BytePlus e entrar;
2. criar e guardar uma chave de API;
3. ativar o modelo, com a exigência do pacote de recursos (a contradição acima);
4. baixar e extrair o pacote de exemplo (`...quickstart_package_arkruntime-20260909.zip`).

No Windows, um `setup_windows.bat` baixa a ferramenta `uv`, um Python 3.12 à parte do sistema, cria o ambiente `.venv` e instala o SDK; depois um `run_demo.bat` roda `python/demo_standard.py`. No macOS, o equivalente é um script de shell e um `run_demo.sh`. O demo confere a variável `ARK_API_KEY`, abre no navegador uma página local com o prompt e os arquivos de entrada, manda a tarefa assíncrona, imprime o estado a cada 30 s e, no fim, a URL do vídeo. Para seguir, troca-se o texto em `user_content` e as URLs de referência, que precisam ser públicas (a página sugere o armazenamento TOS da BytePlus com leitura pública).

Os exemplos de código usam o endpoint `POST https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks` e, para consultar, `GET .../tasks/<id>`, com a chave no cabeçalho `Authorization: Bearer`; o SDK de Python é o `arkruntime`.

### O que mudou do 2.0 para o 2.5 (Latest capabilities)

- Duração máxima por geração de 15 para 30 s.
- Imagens de referência de 9 para 30; áudios ou vídeos de referência de 3 para 10; a soma da duração dos áudios ou vídeos de referência de 15 para 30 s.
- Proporção e duração automáticas: na edição, a saída mantém a proporção e a duração do vídeo de entrada; na extensão e no primeiro/último quadro, a proporção do vídeo ou da imagem de entrada.
- Saída nova em `mov`: H.264, croma yuv444p e áudio PCM, para fidelidade de cor na edição e na extensão.
- Onze línguas nativas: chinês, inglês, espanhol, indonésio, malaio, tailandês, árabe, português, vietnamita, japonês e coreano.

### A tabela de capacidades (2.5 contra a série 2.0)

| | Seedance 2.5 | Seedance 2.0 | 2.0 fast | 2.0 mini |
|---|---|---|---|---|
| ID do modelo | `dreamina-seedance-2-5-260628` | `dreamina-seedance-2-0-260128` | `dreamina-seedance-2-0-fast-260128` | `dreamina-seedance-2-0-mini-260615` |
| Texto para vídeo, primeiro quadro, primeiro e último quadro | sim | sim | sim | sim |
| Referência por imagem, por vídeo, combinada | sim | sim | sim | sim |
| Referência só por áudio | sim | não (pede imagem ou vídeo) | não | não |
| Editar e estender vídeo; vídeo com áudio | sim | sim | sim | sim |
| Máximo de referências | 50 (30 imagens, 10 vídeos, 10 áudios) | 15 (9, 3, 3) | 15 | 15 |
| Modo rascunho | sim | não | não | não |
| Devolver o último quadro | sim | sim | sim | sim |
| Resolução de saída | 480p e 720p (8 bits), 1080p (10 bits) | 480p, 720p e 1080p (8 bits), 4K (10 bits) | 480p e 720p (8 bits) | 480p e 720p (8 bits) |
| Proporções | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, `adaptive` | as mesmas | as mesmas | as mesmas |
| Duração | 4 a 30 s, ou `-1` (o modelo escolhe) | 4 a 15 s, ou `-1` | 4 a 15 s, ou `-1` | 4 a 15 s, ou `-1` |
| Formato de saída | mp4, mov | mp4 | mp4 | mp4 |
| Inferência offline | não | não | não | não |

### Capacidades em destaque, com os exemplos

**Vídeo coerente de 30 s.** O limite passa de 15 para 30 s, para contar uma história inteira sem emendar trechos. O exemplo junta texto e oito imagens de referência num plano-sequência que atravessa seis salas, com marcas de tempo a cada 5 s no prompt; a chamada usa `generate_audio: true`, `ratio: "16:9"`, `duration: 30` e `watermark: true`, e uma das imagens entra por ID de arquivo (`asset://...`) em vez de URL.

**Até 50 referências.** Num só pedido cabem 30 imagens, 10 vídeos e 10 áudios, combinados à vontade, e o 2.5 aceita gerar só com referência de áudio. O exemplo (um comercial de biscoitos) usa uma imagem e seis vídeos, cada um chamado no prompt como @Video1 a @Video6 para uma função (composição, movimento de câmera, impacto, texto final); a chamada leva `omni_reference_task_type: "reference"`, `output_format: "mov"`, `ratio: "16:9"` e `duration: 15`. O valor `reference` aparece no exemplo, mas não na lista de modos da seção de configuração, que fala de `auto`, `edit` e `extend`.

**Proporção e duração automáticas.** Com `ratio` `adaptive` e `duration` `-1`, o modelo escolhe sozinho, com regras próprias para três tarefas:

- *Edição:* proporção e duração copiadas do vídeo escolhido; os dois parâmetros só aceitam esses valores. A saída pode sair até 0,4 s mais curta que a entrada, pelo processamento dos quadros. Exemplo: um vídeo de 5:4 e 16 s, prompt "Video edit: remove everyone in @Video 1 except the protagonist", saída de 5:4 com cerca de 16 s.
- *Extensão:* a proporção vem do vídeo estendido; a duração aceita de 4 a 30 s ou `-1`. Exemplo: três vídeos de entrada (o primeiro em 7:5, os outros em 16:9), prompt que estende o primeiro e entra nos outros dois, saída em 7:5; a chamada pede `duration: 11` e não declara `omni_reference_task_type`.
- *Primeiro ou primeiro e último quadro:* a proporção vem da imagem do `first_frame`, e a duração aceita de 4 a 30 s ou `-1`. A ilustração da seção usa um primeiro quadro 1:1 e outro último, com saída 1:1 e órbita de câmera de 360 graus. No exemplo em cURL da mesma seção, `first_frame` e `last_frame` apontam para a mesma URL de imagem (`seedance2.5_reference1.png`), com o prompt de um biscoito que dá uma volta completa enquanto a câmera o contorna, `ratio: "adaptive"` e `duration: 5`; a página não comenta essa escolha nem fala em laço.

**Vídeo multilíngue.** O prompt e o áudio gerado aceitam as onze línguas listadas acima. O exemplo é um clipe de hip-hop com letra em oito línguas, a partir de uma imagem de referência, em 16:9 e 20 s, com `generate_audio: true`.

### Outras capacidades e o modo rascunho

A seção "More capabilities" remete o texto para vídeo ao guia geral e anuncia o modo rascunho: um vídeo de 480p para validar antes do vídeo final de alta qualidade.

**O que é o rascunho (Draft mode).** Uma geração em dois passos: primeiro uma prévia em baixa resolução para conferir a estrutura da cena, a sequência dos planos, o movimento do sujeito e se o prompt foi entendido; depois, aprovado o rascunho, o vídeo final é gerado a partir do ID da tarefa de rascunho, reaproveitando modelo, prompt, arquivos, semente, áudio, proporção e duração.

**Validade do ID.** Conta-se do `created_at` da tarefa. IDs de rascunho criados a partir das 10h de 28/10/2026 (UTC+8) valem 14 dias; os criados antes, sete dias. Vencido, o ID não gera mais o final. O aviso se repete três vezes na seção e de novo em "Retention period".

**Passo 1, o rascunho.** Liga-se com `draft=true` na mesma chamada `POST /contents/generations/tasks`. Regras: "Only 480p Draft videos can be generated", e outra resolução dá erro; o rascunho consome tokens e paga a tarifa de um 480p comum. O exemplo manda texto e uma imagem (sem `role` declarado), `duration: 5`, `ratio: "adaptive"`, `resolution: "480p"`, `output_format: "mov"`, `service_tier: "default"` e `draft: true`; o vídeo sai em `content.video_url` quando o estado chega a `succeeded`.

**Passo 2, o final.** Chama-se de novo o mesmo endpoint, com um item `content` de tipo `draft_task` que leva o ID do rascunho. A regra que mais pesa: a partir de um rascunho, o Seedance 2.5 "currently supports only 1080p output", e outra resolução dá erro. Os dois passos são cobrados à parte: o primeiro como 480p; o segundo pela resolução final, com a tarifa decidida por haver ou não vídeo de entrada no passo 1, e a duração de entrada contada pelo vídeo do passo 1, sem contar o rascunho. Os parâmetros do passo 2 se dividem assim:

| Grupo | Parâmetros | Regra |
|---|---|---|
| Fixos | `model`, `draft`, `resolution` | o modelo igual ao do rascunho; `draft` omitido ou `false`; `resolution` obrigatório e só `1080p` |
| Reaproveitados pelo modelo | `content.text`, `content.image_url`, `content.video_url`, `content.audio_url`, `duration`, `ratio`, `seed`, `generate_audio`, `omni_reference_task_type` | não se mandam de novo; repetir dá erro, mesmo com os mesmos valores |
| Que se podem mandar de novo | `return_last_frame`, `output_format`, `watermark`, `service_tier`, `execution_expires_after`, `priority`, `callback_url`, `safety_identifier` | omitidos, valem os padrões do modelo, não os do rascunho |

### Especificações da saída

- **`resolution`:** padrão `720p`; valores `480p` e `720p` (8 bits) e `1080p` (10 bits). O 1080p sai em 10 bits com H.265/HEVC, que a página diz servir a produção profissional e HDR e poder não tocar em alguns ambientes (sugere VLC, mpv ou QuickTime Player).
- **`ratio`:** padrão `adaptive`; valores `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `21:9` e `adaptive`. Regra do `adaptive`: na edição e na extensão, a proporção do vídeo escolhido pelo prompt; no primeiro/último quadro, a da imagem do `first_frame`; no texto para vídeo e na referência, o modelo escolhe entre as seis proporções fixas conforme o prompt. Nas três tarefas especiais só `adaptive` é aceito.
- **`duration`:** padrão `-1`; faixa de 4 a 30 s, ou `-1`. Com `-1`, na edição a saída acompanha a duração do vídeo escolhido, pode ter fração de segundo e sair até 0,4 s mais curta; nas outras tarefas o modelo escolhe um número inteiro de segundos entre 4 e 30. Na edição só `-1` vale, e o vídeo a editar precisa ter de 4 a 30 s.
- **`output_format`:** `mp4` (padrão, o mais compatível) ou `mov` (cor de maior precisão, para correção de cor, recorte e composição; recomendado como entrada e saída de edição e extensão). Tocadores de `mov` listados: IINA só no macOS; VLC, mpv e ffplay no macOS e no Windows.
- **`watermark`:** `true` põe no canto inferior direito uma marca de que o vídeo é gerado por IA; o padrão é `false`. Os exemplos da página usam `true`.

Pixels por resolução e proporção:

| Proporção | 480p | 720p | 1080p |
|---|---|---|---|
| 16:9 | 854×480 | 1280×720 | 1920×1080 |
| 4:3 | 752×560 | 1112×834 | 1664×1248 |
| 1:1 | 640×640 | 960×960 | 1440×1440 |
| 3:4 | 560×752 | 834×1112 | 1248×1664 |
| 9:16 | 480×854 | 720×1280 | 1080×1920 |
| 21:9 | 992×432 | 1470×630 | 2206×946 |

### Retrato, prompt e limites de uso

**Retrato.** A seção "Create portrait videos with ease" diz que o 2.5 tem os mesmos recursos de retrato da série 2.0 e lista as três saídas do guia de retrato (seção 3 desta ficha): saídas de modelos da própria conta, personagens digitais prontos e pessoa real autorizada.

**Prompt.** Há uma skill de otimização de prompt, instalada por `npx` com `--skill sd25-pe` e chamada no chat como `/sd25-pe` seguido do prompt. As regras da página: montar o prompt na ordem sujeito, ação, cena, estilo visual, câmera ou cortes, som (partes dispensáveis podem sair); dizer o que cada arquivo referido por `@Image 1`, `@Video 1` ou `@Audio 1` fornece (aparência, ação, timbre) e o que não se deve copiar dele; marcar a música entre `()`, o efeito sonoro entre `<>`, a fala entre `{}` e a legenda entre `【】`, e, em fala que não é em chinês, dizer a língua antes. Um guia de prompt à parte não foi aberto.

**Entrada multimodal.** O aviso que abre a seção: "Seedance 2.5 does not support directly uploading reference images or videos containing real human faces", com remissão ao guia de retrato.

| Entrada | Como entra | Formatos | Dimensões e duração | Tamanho | Quantidade |
|---|---|---|---|---|---|
| Imagem | URL, Base64 ou ID de arquivo | jpeg, png, webp, bmp, tiff, gif, heic, heif | proporção (largura/altura) de 0,4 a 2,5; lados de 300 a 6000 px | menos de 30 MB por imagem; corpo do pedido até 64 MB; Base64 não para arquivo grande | 1 no primeiro quadro; 2 no primeiro e último; 1 a 30 na referência |
| Vídeo | URL ou ID de arquivo | mp4 e mov (H.264 ou H.265; áudio AAC ou MP3, e PCM no mov) | 480p, 720p, 1080p ou 4K; 2 a 30 s cada (4 a 30 s na edição); proporção de 0,4 a 2,5; lados de 300 a 6000 px; total de pixels entre 407.696 e 8.295.044; 24 a 60 fps | até 200 MB por vídeo | até 10, somando no máximo 30 s |
| Áudio | URL, Base64 ou ID de arquivo | wav, mp3 | 2 a 30 s cada | até 15 MB por áudio; corpo até 64 MB | até 10, somando no máximo 30 s |

**Prazo de guarda.** IDs de tarefa de rascunho: as regras acima (14 dias a partir de 28/10/2026, sete antes). Os outros IDs de tarefa de vídeo: sete dias. A URL do vídeo gerado dura 24 horas e aceita até 100 downloads.

**Limites de taxa** (por conta principal e por modelo, qualquer versão; acima do limite, erro `429`): o máximo de tarefas criadas por minuto é 600 para empresa e 180 para pessoa física; o de tarefas simultâneas, 10 e 3 (acima disso, a tarefa entra numa fila). Nas chamadas que não geram, o limite por segundo é 20 para consultar uma tarefa, 1 para listar tarefas e 20 para cancelar ou apagar.

## 2. A tabela de preço de vídeo (página Pricing, seção "Video generation models")

**Como se forma o preço.** O preço é a tarifa por token vezes o consumo de tokens; a página diz que, com o resto igual, resolução mais alta custa mais e ter vídeo de entrada custa mais. Indica duas calculadoras (série 2.0 e série 2.5), não abertas. A unidade da página, dita no topo, é US$ por milhão de tokens.

**Tarifa por milhão de tokens** (inferência online, salvo onde diz offline):

| Modelo | Sem vídeo de entrada: 480p e 720p | 1080p | 4K | Offline | Com vídeo de entrada: 480p e 720p | 1080p | 4K | Offline |
|---|---|---|---|---|---|---|---|---|
| `dreamina-seedance-2-5-260628` | 10,70 | 11,7 | não | não | 6,40 | 7,0 | não | não |
| `dreamina-seedance-2-0-260128` | 7,0 | 7,7 | 4,0 | não | 4,3 | 4,7 | 2,4 | não |
| `dreamina-seedance-2-0-fast-260128` | 5,6 | não | não | não | 3,3 | não | não | não |
| `dreamina-seedance-2-0-mini-260615` | 3,5 | não | não | não | 2,1 | não | não | não |
| `seedance-1-0-pro-250528` | 2,5 (uma célula só para o online) | | | 1,25 | (sem linha) | | | |
| `seedance-1-0-pro-fast-251015` | 1 (uma célula só para o online) | | | 0,5 | (sem linha) | | | |

Em "Retiring models", o `seedance-1-5-pro-251215` sai do ar em 11/11/2026; a tarifa dele depende do áudio: online, 2,4 com áudio e 1,2 sem; offline, 1,2 e 0,6.

**Regras de cobrança.**

- Só se paga vídeo gerado com sucesso; falha, inclusive por moderação de conteúdo, não cobra.
- Preço estimado: `Token unit price × token consumption`.
- Tokens estimados: `(Input video duration + output video duration) × output video width × output video height × output video frame rate / 1024`.
- Rascunho: no Seedance 2.5, sempre a 480p, com o mesmo consumo e a mesma tarifa de um 480p comum; no Seedance 1.5 Pro, o consumo normal vezes um fator de 0,7 (sem áudio) ou 0,6 (com áudio).
- O consumo é estimado; o que vale é o `usage.completion_tokens` da resposta da API.
- **Consumo mínimo:** na série 2.0 e no 2.5, quando a entrada inclui vídeo, há um piso de tokens, que depende da resolução, da proporção e da duração da saída; abaixo dele, cobra-se o piso. Os pisos estão em duas tabelas externas (Lark), não abertas.

**Exemplos de preço do Seedance 2.5** (16:9, 5 s de saída):

| Resolução | Sem vídeo de entrada | Com vídeo de entrada de 2 a 30 s |
|---|---|---|
| 480p | US$ 0,514 por vídeo (0,103 por segundo) | 0,553 a 2,152 |
| 720p | 1,156 (0,231 por segundo) | 1,244 a 4,838 |
| 1080p | 2,843 (0,569 por segundo) | 3,062 a 11,907 |

Na coluna com vídeo, o menor preço é o de 2 a 4 s de entrada, e o maior, o de 30 s.

**Exemplos da série Seedance 2.0** (16:9, 5 s de saída; sem vídeo, por vídeo e por segundo; com vídeo de entrada de 2 a 15 s, faixa por vídeo, do menor, com 2 a 4 s de entrada, ao maior, com 15 s):

| Modelo | 480p | 720p | 1080p | 4K |
|---|---|---|---|---|
| 2.0, sem vídeo | 0,35 (0,07/s) | 0,76 (0,15/s) | 1,87 (0,37/s) | 3,89 (0,78/s) |
| 2.0 Fast, sem vídeo | 0,28 (0,06/s) | 0,60 (0,12/s) | não | não |
| 2.0 Mini, sem vídeo | 0,18 (0,04/s) | 0,38 (0,08/s) | não | não |
| 2.0, com vídeo | 0,39 a 0,86 | 0,84 a 1,86 | 2,06 a 4,57 | 4,20 a 9,33 |
| 2.0 Fast, com vídeo | 0,30 a 0,66 | 0,64 a 1,43 | não | não |
| 2.0 Mini, com vídeo | 0,19 a 0,42 | 0,41 a 0,91 | não | não |

**Exemplos do Seedance 1.0 Pro e do 1.0 Pro Fast** (24 quadros por segundo em todas as linhas; tokens e preço por vídeo, em US$):

| Resolução | Proporção | Pixels | Duração | Tokens | 1.0 Pro | 1.0 Pro Fast |
|---|---|---|---|---|---|---|
| 480p | 16:9 | 864×480 | 5 s | 48.600 | 0,12 | 0,05 |
| 480p | 16:9 | 864×480 | 10 s | 97.000 | 0,24 | 0,10 |
| 480p | 4:3 | 736×544 | 5 s | 46.920 | 0,12 | 0,05 |
| 480p | 4:3 | 736×544 | 10 s | 93.840 | 0,23 | 0,09 |
| 480p | 1:1 | 640×640 | 5 s | 48.000 | 0,12 | 0,05 |
| 480p | 1:1 | 640×640 | 10 s | 96.000 | 0,24 | 0,10 |
| 480p | 21:9 | 960×416 | 5 s | 46.800 | 0,12 | 0,05 |
| 480p | 21:9 | 960×416 | 10 s | 93.600 | 0,23 | 0,09 |
| 720p | 16:9 | 1248×704 | 5 s | 102.960 | 0,26 | 0,10 |
| 720p | 16:9 | 1248×704 | 10 s | 205.920 | 0,51 | 0,21 |
| 720p | 4:3 | 1120×832 | 5 s | 109.200 | 0,27 | 0,11 |
| 720p | 4:3 | 1120×832 | 10 s | 218.400 | 0,55 | 0,22 |
| 720p | 1:1 | 960×960 | 5 s | 108.000 | 0,27 | 0,11 |
| 720p | 1:1 | 960×960 | 10 s | 216.000 | 0,54 | 0,22 |
| 720p | 21:9 | 1504×640 | 5 s | 112.800 | 0,28 | 0,11 |
| 720p | 21:9 | 1504×640 | 10 s | 225.600 | 0,56 | 0,23 |
| 1080p | 16:9 | 1920×1088 | 5 s | 244.800 | 0,61 | 0,24 |
| 1080p | 16:9 | 1920×1088 | 10 s | 489.600 | 1,22 | 0,49 |
| 1080p | 4:3 | 1664×1248 | 5 s | 243.360 | 0,61 | 0,24 |
| 1080p | 4:3 | 1664×1248 | 10 s | 486.720 | 1,22 | 0,49 |
| 1080p | 1:1 | 1440×1440 | 5 s | 243.000 | 0,61 | 0,24 |
| 1080p | 1:1 | 1440×1440 | 10 s | 486.000 | 1,22 | 0,49 |
| 1080p | 21:9 | 2176×928 | 5 s | 236.640 | 0,59 | 0,24 |
| 1080p | 21:9 | 2176×928 | 10 s | 473.280 | 1,18 | 0,47 |

Na linha de 480p, 16:9 e 10 s, a tabela dá 97.000 tokens; nas outras linhas, o valor de 10 s é o dobro exato do de 5 s (aqui seria 97.200).

**As duas notas gerais do fim da página.** Os limites de chamada de cada modelo são por minuto (RPM e TPM) e aparecem na página de ativação do console, onde se pede aumento. Uma conta fica em débito quando o saldo não basta ou fica negativo, e depois de 2 horas em débito os serviços de modelo são suspensos até a recarga.

**O resto da página de preços** (fora desta ficha): grandes modelos de linguagem (com e sem áudio de entrada, regras e exemplos, horários de pico do DeepSeek V4.1 Flash e modelos que saem do ar em 11/11/2026), geração de imagem, geração 3D, embeddings, "Model unit", Managed Agents e Coding Plan.

## 3. O guia de retrato (Create portrait videos with Dreamina Seedance models)

**A regra.** O guia vale para o Seedance 2.5 e a série 2.0: "Seedance 2.5 and Seedance 2.0 series models do not support directly uploading reference images/videos that contain real human faces." O guia existe para oferecer caminhos para quem precisa de rosto.

**As três saídas, pelo que cada uma exige:**

| Saída | O que entra | Condição | Limite que o guia dá |
|---|---|---|---|
| Personagens digitais prontos | um personagem da biblioteca da plataforma, por `asset://<asset ID>` no campo `content.<modality>_url.url` | ativar a biblioteca (página à parte, não aberta) | servem a quem quer rosto de aparência real sem precisar de uma pessoa específica; o guia os chama de grátis, de acordo com as regras e variados |
| Saídas confiáveis de modelos da própria conta | rosto gerado por certos modelos na mesma conta, nos últimos 30 dias | o arquivo original, sem edição, dentro do prazo | ver as regras abaixo |
| Pessoa real autorizada | imagem, vídeo e áudio da pessoa, enviados ao ModelArk e guardados com ID de arquivo | verificação da pessoa real e autorização dela (processo noutra página, não aberta) | o guia não dá outro limite |

**No uso do personagem pronto,** o ID só serve para passar o arquivo; no prompt, o arquivo é chamado pelo tipo e pela ordem entre os do mesmo tipo no pedido ("Image 1"), nunca pelo ID. O exemplo é uma blogueira de beleza (personagem da biblioteca) apresentando um pote de creme (imagem de produto), com fala no prompt; o código usa o `dreamina-seedance-2-0-260128`, `ratio="adaptive"` e `duration=11`.

**O que a plataforma aceita como saída confiável:**

| Saída | Confiável se gerada a partir de | Validade |
|---|---|---|
| Vídeo com rosto gerado pelo Seedance 2.5 ou pela série 2.0 | 11/03/2026 | 30 dias desde a geração |
| Último quadro (imagem) desses vídeos | 16/04/2026 | 30 dias |
| Imagem com rosto do texto para imagem do Seedream 5.0 lite, pro ou flash | 16/04/2026 | 30 dias |

Onde a confiança se perde: arquivo vindo de outra plataforma ou de outra conta; arquivo editado antes de voltar ao modelo; prazo de 30 dias vencido; e, segundo o guia, compressão ou reenvio, que podem invalidar a verificação (daí a recomendação de salvar o original direto no TOS). O que ela não garante: a saída, que ainda passa pela moderação do ModelArk e pode ser barrada. Quando ela nem é necessária: sem rosto na entrada, a moderação de rosto não dispara, e a saída do modelo pode ser reeditada livremente. O exemplo reedita o vídeo da blogueira com o pedido de deixar o creme branco e passar a proporção para 16:9; o código usa de novo o Seedance 2.0, e o guia avisa que a URL do vídeo original dura 24 horas.

## O que as três páginas não dizem

- A data de publicação ou de atualização de cada página.
- Como se resolve a condição de ativação (as três alternativas da nota ou o pacote obrigatório do passo 3), quanto custa o pacote de recursos ou o AI Savings Plan, e se o saldo de US$ 30 é consumido ou só exigido.
- A taxa de quadros da saída do Seedance 2.5, que a fórmula de tokens usa; só as tabelas do Seedance 1.0 Pro e do 1.0 Pro Fast dão os quadros por segundo (24). A entrada aceita de 24 a 60 fps.
- O padrão de `generate_audio` e se o áudio muda o preço do 2.5 (a seção de vídeo só fala de áudio na linha do 1.5 Pro).
- Os valores do consumo mínimo com vídeo de entrada, que estão em tabelas externas não abertas.
- Com que tipos de tarefa o rascunho funciona (o único exemplo leva texto e uma imagem sem `role`) e por que o final a partir do rascunho só sai em 1080p.
- Nada sobre laço: o tutorial não usa a palavra nem diz o que acontece quando o primeiro e o último quadro são a mesma imagem, embora o exemplo em cURL faça isso.
- O que conta como "rosto humano real" para a moderação (desenho, ilustração, rosto parcial) e o que acontece com pessoa que não pode dar a autorização.
- Nada sobre o uso do modelo fora do ModelArk (o guia de retrato só diz que a saída confiável não vale entre plataformas).
