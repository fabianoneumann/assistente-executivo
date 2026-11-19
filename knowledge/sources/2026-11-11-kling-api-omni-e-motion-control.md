---
titulo: "Kling API: Omni Video Generation (Kling 4.0) e Motion Control 3.0"
tipo: artigo
autor: "Kling AI (documentação da API)"
url: "https://kling.ai/document-api/api/video/4-0/video-omni.md"
capturado_em: 2026-11-11
licenca: "protegida: o Markdown da documentação da API da Kling não declara licença; valem os termos do site. Ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [kling, video-generation, omni-reference, first-last-frame, multi-keyframe, motion-transfer, video-editing, image-to-video, aspect-ratio, api-pricing]
---

# Kling na API: o endpoint Omni do 4.0 e o Motion Control 3.0

**Proveniência.** Duas páginas de referência da documentação da API da Kling, baixadas em 11/11/2026 no Markdown que a documentação serve para leitura por modelo ("This content is optimized for LLMs"); nenhuma das duas traz data de publicação ou de atualização.

1. **Omni Video Generation do Kling 4.0**, https://kling.ai/document-api/api/video/4-0/video-omni.md (o cabeçalho do arquivo declara como fonte a mesma página sem o `.md`): lida inteira, a criação de tarefa (cabeçalhos, corpo, notas de cada campo, exemplo e resposta), os três exemplos de cenário e as duas consultas de tarefa (por ID e por cursor). As abas irmãs da mesma página (Text to Video, Image to Video, Element Management, Voice Management) não estão no arquivo e ficaram fora.
2. **Motion Control 3.0**, registrada na rodada como https://kling.ai/document-api/apiReference/model/motionControl; o cabeçalho do arquivo baixado declara como fonte https://kling.ai/document-api/api/video/motion-control, aba "Motion Control 3.0": lida inteira, com a mesma estrutura. A aba irmã Motion Control 2.6 não está no arquivo e ficou fora.

**Quem fala.** A Kling, que faz e vende o modelo; é a documentação técnica do fabricante.

## Omni do Kling 4.0: a chamada

`POST /omni-video/kling-4.0`, autenticado por `Authorization: Bearer <API_KEY>`, corpo em JSON; os exemplos usam o host `api-singapore.klingai.com`. O corpo tem três blocos:

| Campo | Obrigatório | Padrão | Valores |
| --- | --- | --- | --- |
| `contents` | sim | - | lista de entradas; `type` é `prompt`, `first_frame`, `middle_frame`, `last_frame`, `refer_image`, `feature_video`, `base_video`, `element` ou `voice` |
| `settings.audio` | não | `native` | `native`, `original` |
| `settings.resolution` | não | `1080p` | `720p`, `1080p` |
| `settings.aspect_ratio` | não | `adaptive` | `21:9`, `16:9`, `9:16`, `1:1`, `adaptive` |
| `settings.duration` | não | - | inteiros de `3` a `30` |
| `options.callback_url` | não | - | URL avisada a cada mudança de estado da tarefa |
| `options.external_task_id` | não | - | ID próprio, único na conta, que não substitui o do sistema |
| `options.watermark_info.enabled` | não | `false` | gera também uma versão com marca d'água; marca personalizada não existe ainda |

Cada item de `contents` leva o `type`, o conteúdo (`text`, `url`, `element_id` ou `voice_id`) e um `id`, que é o nome pelo qual o prompt o chama com `@`.

## O que cada tipo de entrada aceita

- **Prompt:** até 26.000 caracteres só em inglês, até 11.000 em outra língua; texto misto tem de caber em E/26000 + N/11000 ≤ 1 (E, caracteres ingleses; N, os outros). A página não tem campo de prompt negativo.
- **Imagens** (`first_frame`, `middle_frame`, `last_frame`, `refer_image`): servem de referência de cena ou de estilo e também de quadro-chave. JPG, JPEG ou PNG, por URL ou base64, até 30 MB, lados de pelo menos 300 px, proporção entre 2:5 e 5:2, no máximo 10 imagens. O `id` é exigido quando há mais de um `middle_frame` ou mais de uma `refer_image`. Com quadro inicial, quadro final e imagens de referência na mesma tarefa, o `first_frame` vem primeiro e o `last_frame` por último na lista, e a página recomenda chamá-las por `@id` no prompt.
- **Vídeos:** `feature_video` é o vídeo de referência de característica; `base_video`, o vídeo a editar. MP4 ou MOV, por URL, até 300 MB. Cada vídeo e a soma de todos ficam entre 3 e 30 s, e a soma inclui os elements de personagem feitos de vídeo. Lados entre 700 e 4.553 px, área de até 8.294.400 pixels, proporção entre 2:5 e 5:2. Entra de 24 a 60 fps; o vídeo gerado sai a 24 fps. Sem element de vídeo, até 5 vídeos de referência; com eles, vídeos e elements de vídeo somam no máximo 5. No máximo um `base_video`.
- **Elements:** há os de personagem, criados a partir de vídeo, e os de várias imagens, cada tipo com seu alcance. Até 7 por tarefa, dos quais até 3 de vídeo, e o `id` é obrigatório. A biblioteca oficial de elements tem guia próprio (só o link).
- **Voz:** até 3 vozes, pelo `voice_id` que a API de voz personalizada devolve ou de uma voz predefinida; `id` obrigatório.
- **Teto comum:** imagens, vídeos, elements e vozes somados não passam de 15.

## Como escrever o prompt, segundo a página

No 4.0 e no 4.0 Flash, as várias referências e a edição de vídeo passam todas pelo prompt, que precisa dar conta do papel de cada referência, da cena, da sequência de eventos e do som. Arrumado pelo que entra no texto:

| O que o prompt traz | Como a página pede |
| --- | --- |
| Quem é cada material | pelo `id` dado a ele em `contents`, sem repetição na tarefa, chamado com `@` (uma `refer_image` com `"id": "image_1"` vira `@image_1`) |
| O que tirar de cada referência | a função e o limite de cada uma, como manter rosto, cabelo e roupa de uma imagem, ou pegar de um vídeo só o ritmo: "Follow the movement rhythm in `@video_1` without using its background."; referência sem função declarada fica a critério do modelo ("the model will infer how to use it"), com risco de sair outra coisa |
| A cena e o andamento | o ambiente geral e a ordem dos eventos, com cena, estilo, câmera e ação conforme o caso |
| O som | fala, som ambiente, música e efeitos |
| Numa edição | o que se altera e o que se preserva, dito com todas as letras |

O detalhe fica no guia do 4.0 e do 4.0 Flash, que esta ficha não cobre.

## Áudio, proporção e duração: quem decide

- **Áudio.** `native` gera som junto com a imagem. `original` mantém o som de um vídeo de entrada: não se combina com referência de voz, exige pelo menos um `base_video` ou `feature_video`, e usa o som do `base_video` se houver; se não, o do primeiro `feature_video` da lista.
- **Proporção.** Um valor explícito diferente de `adaptive` vale mais que o prompt. Em `adaptive` ou sem o campo, a ordem é: a proporção dita no prompt (o exemplo é pedir um vídeo vertical 9:16); depois o `base_video`; depois as imagens de quadro-chave, com o quadro inicial à frente e, sem ele, o primeiro quadro-chave; depois o `feature_video`, cuja proporção vale se for um só, e 16:9 se forem vários. Sem nenhuma dessas fontes, 16:9.
- **Duração.** O parâmetro vale mais que o prompt. Sem ele, vale a duração pedida no prompt; sem as duas, a do `base_video` arredondada para o inteiro, e sem `base_video`, 10 s.

## O que a página diz da cobrança

A duração-alvo final é a que se cobra da saída: "The final target duration is used to bill the output video." Ela volta na consulta como `usage.output_duration` e, no extrato, como `output_duration`; junto com a duração de entrada cobrada (`input_duration`, quando há vídeo de entrada) e as regras da página de preço (só o link), dá o custo. O campo `usage` só aparece em tarefas do 4.0 e do 4.0 Flash e depois que a tarefa termina; `input_duration` vem com duas casas decimais, medida depois de uma normalização do sistema, e pode diferir um pouco da duração dos arquivos originais. O campo `duration` de cada vídeo devolvido é a duração real do arquivo, que a página separa da duração cobrada. Cada tarefa traz ainda a lista `billing`: `charge_type` `cash` (saldo) ou `unit` (pacote); no saldo, `cash_type` `balance`, `test_balance` ou `reward_balance`, `currency` CNY ou USD e `list_price`; no pacote, `package_type` `video`, `image` ou `audio`; e `amount`, o valor debitado.

## Os exemplos oficiais

| Cenário | Entradas | Prompt (trecho) | Ajustes |
| --- | --- | --- | --- |
| Pedido de exemplo | um `feature_video` e duas `refer_image` | "Reference the camera path and pacing of @Video1. Replace the subject with the car in @Image1 and the background with @Image2." | 1080p, `adaptive` |
| Vídeo de referência de característica | um `feature_video` (luta) e duas `refer_image` (dois lutadores) | "Reference the fighting movements and attack rhythm from @video_1, and use @image_1 and @image_2 for the character designs." | 15 s, 1080p, `adaptive` |
| Edição de vídeo | um `base_video` | "Edit @Video1. Remove the foreground person from the video. Keep everything else unchanged." | 1080p, `adaptive` |
| Referência de voz | uma `refer_image` e uma `voice` (`id` "1") | uma moça num trem que se levanta e diz "Excuse me." em inglês com a voz `@1`, com câmera que recua e pedido de sincronia labial | 5 s, 1080p, 9:16, sem marca d'água |

## Consultar a tarefa

`GET /tasks` aceita `task_ids` ou `external_task_ids`, nunca os dois, e vários IDs separados por vírgula; a página diz que a consulta só vale para tarefas assíncronas. `POST /tasks` consulta por cursor: `start_time` e `end_time` em milissegundos (padrão, os últimos 30 dias até agora; ignorados quando há cursor), `limit` de 100 por padrão e até 500, e filtros por `status` (`submitted`, `processing`, `succeeded`, `failed`) e `product_type` (`video`, `image`, `try_on`); a resposta traz `next_cursor` e `has_more`. Os resultados (`video`, `image`, `audio`, `voice`, `element`) vêm em URLs com proteção contra hotlink e ficam guardados 30 dias. Na falha, o campo `message` dá o motivo, e o exemplo de motivo é acionar o controle de risco de conteúdo da plataforma.

## Motion Control 3.0: a chamada

`POST /motion-control/kling-3.0`, mesma autenticação. Em `contents`, os tipos são `prompt`, `image` (a aparência), `video` (o movimento) e `element`.

| Campo | Obrigatório | Padrão | Valores |
| --- | --- | --- | --- |
| `settings.character_orientation` | sim | - | `image` (orientação do personagem da imagem; vídeo de referência de até 10 s) ou `video` (a do vídeo; até 30 s) |
| `settings.audio` | não | `original` | `original` (mantém o som do vídeo de referência) ou `off` (sem som) |
| `settings.resolution` | não | `720p` | `720p`, `1080p` |
| `options` | não | - | `callback_url`, `external_task_id`, `watermark_info`, como no Omni |

O prompt aceita descrições positivas e negativas, até 2.500 caracteres, e pode acrescentar elementos à cena e efeitos de movimento (com remissão ao guia do Motion Control, não lido).

## Motion Control 3.0: o que a imagem e o vídeo precisam ter

**A imagem do personagem.** A proporção do corpo tem de casar com a do vídeo: "Avoid driving a half-body character with full-body motion." Meio corpo ou corpo inteiro, com a cabeça, à vista e sem nada na frente; nada de orientação extrema (de cabeça para baixo, deitado) nem de personagem pequeno no quadro. Serve personagem realista ou estilizado: gente, animal humanoide, alguns animais e figuras de proporção humana. JPG, JPEG ou PNG, por URL ou base64, até 50 MB, lados de pelo menos 300 px, proporção entre 1:2,5 e 2,5:1.

**O vídeo do movimento.** Quem está no quadro: de preferência uma pessoa real e só uma, de meio corpo ou corpo inteiro, com cabeça e membros sempre à vista e sem nada na frente; figura estilizada ou humanoide pode servir se os membros tiverem proporção aceitável, e, havendo mais gente, "the motion of the character occupying the largest proportion of the frame will be used". Como é a tomada: uma só, contínua, sem corte e sem câmera em movimento, com o personagem o tempo todo no quadro, ou o vídeo pode ser aparado; gesto liso e estável rende mais que o muito rápido. Formato: de 3 s até 30 s (orientação `video`) ou 10 s (orientação `image`), MP4 ou MOV, até 100 MB, lados entre 340 e 3.850 px. O sistema valida o conteúdo e devolve código de erro quando algo não serve.

**Saída mais curta.** Com movimento difícil ou rápido, o vídeo gerado pode sair mais curto que o enviado, porque o modelo usa só o trecho de movimento aproveitável, e gera desde que haja pelo menos 3 s seguidos; "Deduction is calculated based on the output video duration."

**Element.** No máximo um; com ele, o vídeo gerado segue sempre a orientação do personagem do vídeo de referência.

**O exemplo oficial:** prompt "The girl is wearing a loose gray T-shirt and denim shorts", uma imagem, um vídeo de dança de 10 s (`dance_10s.mp4`), orientação `video`, 1080p e som original.

A consulta de tarefa é igual à do Omni, sem o bloco `usage`; ali o `duration` do vídeo é descrito só como a duração do vídeo gerado.

## Desencontros dentro das páginas

- No Motion Control 3.0, a descrição de `settings` fala em parâmetros "such as facial orientation, clarity, duration", mas a tabela não tem campo de duração.
- No Omni, o comentário do JSON marca o `id` do vídeo como opcional; o dos elements e das vozes, como obrigatório; e o das imagens, como obrigatório só quando há mais de um `middle_frame` ou de uma `refer_image`.

## O que estas páginas não dizem

- **Omni:** onde, no tempo, cai cada `middle_frame` (não há campo de posição ou de instante); se o mesmo arquivo pode ser `first_frame` e `last_frame`; se `settings.resolution` aceita 4K (o enum para em `1080p`); qualquer campo de prompt negativo, semente, intensidade de movimento ou controle de câmera; se o áudio nativo muda o preço; regra sobre rosto de pessoa real na imagem ou no vídeo de entrada (a única menção a moderação é o exemplo de motivo de falha).
- **Motion Control 3.0:** o preço (só a regra de que se cobra a saída), um parâmetro de duração da saída, a duração máxima da saída fora do limite do vídeo de entrada, e o que muda com o element além da orientação.
