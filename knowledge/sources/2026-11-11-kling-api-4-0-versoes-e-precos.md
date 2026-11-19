---
titulo: "Kling API: Video Capability Map, Video Pricing e API Updates"
tipo: artigo
autor: "Kling AI (documentação da API)"
url: "https://kling.ai/document-api/guides/capability-map/video"
publicado_em: 2026-10-20   # "Updated At" do mapa de capacidades; a tabela de preço não traz data; a entrada mais nova do changelog é de 04/11/2026
capturado_em: 2026-11-11
licenca: "protegida: o Markdown da documentação da API da Kling não declara licença; valem os termos do site. Ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [kling, video-generation, api-pricing, image-to-video, first-last-frame, multi-keyframe, omni-reference, motion-transfer, video-editing, 4k, changelog]
---

# Kling na API: versões, capacidades e preços de vídeo (novembro de 2026)

**Proveniência.** Três páginas da documentação da API da Kling (kling.ai/document-api), baixadas em 11/11/2026 no Markdown que a própria documentação serve para leitura por modelo (cada arquivo abre com "This content is optimized for LLMs"):

1. **Mapa de capacidades de vídeo**, https://kling.ai/document-api/guides/capability-map/video, "Updated At: 2026-10-20": lido inteiro (as cinco tabelas: modelos, capacidades gerais, texto para vídeo, imagem para vídeo e referência Omni).
2. **Tabela de preço de vídeo**, https://kling.ai/document-api/pricing/base/video: a página não traz data; lida inteira (a regra de cobrança do 4.0 e as 29 linhas da tabela).
3. **Changelog da API**, https://kling.ai/document-api/updates/api, aba "API Updates", com entradas de 09/19/2024 a 11/04/2026 (datas no formato mês/dia/ano da página; abaixo, em dia/mês/ano): cobertas inteiras e em ordem, da mais nova para a mais antiga, as entradas sobre modelos e recursos de vídeo, cobrança e retenção; o resto vai numa linha no fim da seção.

**Quem fala.** A Kling, que faz e vende os modelos: capacidades e preços são o que o fabricante declara. Nenhuma das três páginas nomeia a empresa por trás da Kling.

## Modelos de vídeo na API (mapa de capacidades)

| Modelo | Como a página o apresenta | Entrada | Duração | Resolução |
| --- | --- | --- | --- | --- |
| Kling 4.0 | 30 s nativos, movimento dinâmico, referência Omni, controle dos momentos da narrativa | texto, imagem, vídeo | 3 a 30 s | 720p, 1080p, 4K |
| Kling 4.0 Flash | mais rápido e de melhor custo | texto, imagem, vídeo | 3 a 20 s | 720p |
| Kling 3.0 Turbo | resultado constante a custo menor | texto, imagem | 3 a 15 s | 720p, 1080p |
| Kling 3.0 | áudio nativo melhor, elements mais consistentes, várias tomadas | texto, imagem, vídeo | 3 a 15 s | 720p, 1080p, 4K |
| Kling 3.0 Omni | entrada multimodal única, personagem movido por voz, áudio nativo com storyboard | texto, imagem, vídeo | 3 a 15 s | 720p, 1080p, 4K |
| Kling O1 | modelo unificado com instruções multimodais e consistência | texto, imagem, vídeo | 3 a 10 s | 720p, 1080p |
| Kling 2.6 | slogan sobre ver o som e ouvir a imagem | texto, imagem, vídeo | 5 ou 10 s | 720p, 1080p |
| Kling 2.5 Turbo | criatividade a bom custo | texto, imagem | 5 ou 10 s | 720p, 1080p |

**Capacidades gerais**, fora da tabela por modelo: Motion Control "Only available for Kling 3.0 and Kling 2.6 models."; Avatar (vídeo de apresentador a partir de uma foto), Lip Sync (boca do personagem movida por texto ou áudio), Multi-element Video Editing (marcar, trocar, acrescentar ou tirar elementos de um vídeo), Video to Audio (som para vídeo da Kling ou enviado) e Text to Audio valem para todas as versões.

**Texto para vídeo**

| Capacidade | 4.0 | 4.0 Flash | 3.0 Turbo | 3.0 | 3.0 Omni | O1 | 2.6 | 2.5 Turbo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Uma ou várias tomadas | sim | sim | sim | sim | não | não | só uma tomada | só uma tomada |
| Áudio nativo | sim | sim | sim | sim | não | não | não | não |

**Imagem para vídeo**

| Capacidade | 4.0 | 4.0 Flash | 3.0 Turbo | 3.0 | 3.0 Omni | O1 | 2.6 | 2.5 Turbo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Primeiro e último quadro | sim | só o primeiro | só o primeiro | sim | não | não | só vídeo mudo a 1080p | só a 1080p |
| Vários quadros-chave | sim | não | não | não | não | não | não | não |
| Referência de voz | não | não | não | não | não | não | com áudio, só a 1080p | não |
| Uma ou várias tomadas | sim | sim | sim | sim | não | não | só uma tomada | só uma tomada |
| Áudio nativo | sim | sim | sim | sim | não | não | não | não |

**Referência Omni**

| Capacidade | 4.0 | 4.0 Flash | 3.0 Turbo | 3.0 | 3.0 Omni | O1 | 2.6 | 2.5 Turbo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vídeo de referência (referência de característica e edição) | até 5, somando até 30 s | até 5, somando até 20 s | não | não | 1, de 3 a 15,5 s | 1, de 3 a 10 s | não | não |
| Imagem de referência | até 10 | até 10 | não | não | limite varia com as outras entradas | limite varia com as outras entradas | não | não |
| Primeiro e último quadro | sim | só o primeiro | não | não | sim | só o primeiro, com 5 ou 10 s | não | não |
| Vários quadros-chave | sim | não | não | não | não | não | não | não |
| Elements (personagem de vídeo e de várias imagens) | até 7, dos quais até 3 de vídeo | até 7, dos quais até 3 de vídeo | não | não | limite depende do tipo, das imagens e de haver vídeo | só de várias imagens | não | não |
| Referência de voz | voz ligada ao element ou voz criada citada direto | não | não | não | só voz ligada ao element | não | não | não |
| Uma ou várias tomadas | sim | sim | não | não | sim | sim | não | não |
| Áudio nativo | sim | sim | não | não | sim | não | não | não |
| Teto de entradas somadas | 15 (imagens, vídeos, elements e vozes) | 15 (imagens, vídeos e elements) | não | não | remete às regras de combinação | remete às regras de combinação | não | não |

Nas células do 3.0 Omni e do O1 sobre o teto de entradas, o texto da página termina numa vírgula, sem o link ou a frase que viria depois ("For limits on reference materials and their allowed combinations,").

## Preço de vídeo (tabela sem data)

A página se apresenta como "Resource package deduction rules": o preço é em units de um pacote, e cada linha dá também o valor em dólar. **Regra do 4.0 e do 4.0 Flash:** cobra-se a duração total em segundos, e ela depende de haver vídeo de entrada. Se a entrada é mais longa que a saída, paga-se o unit pela soma das duas; se a entrada é igual ou mais curta, "Unit price × Output video duration × 2". Conta como entrada o vídeo de referência (de característica e o vídeo a editar, `feature video` e `base video`) e o vídeo dos elements de personagem.

| Modelo | Condição | Base | 720p | 1080p | 4K |
| --- | --- | --- | --- | --- | --- |
| Kling 4.0 | sem vídeo de entrada | por segundo; total = saída | 1,0 unit (US$ 0,157)/s | 1,5 unit (US$ 0,235)/s | - |
| Kling 4.0 | com vídeo de entrada, entrada ≤ saída | por segundo; total = saída × 2 | 0,6 unit (US$ 0,094)/s | 0,9 unit (US$ 0,141)/s | - |
| Kling 4.0 | com vídeo de entrada, entrada > saída | por segundo; total = entrada + saída | 0,6 unit (US$ 0,094)/s | 0,9 unit (US$ 0,141)/s | - |
| Kling 4.0 Flash | sem vídeo de entrada | por segundo; total = saída | 0,6 unit (US$ 0,094)/s | - | - |
| Kling 4.0 Flash | com vídeo de entrada, entrada ≤ saída | por segundo; total = saída × 2 | 0,4 unit (US$ 0,063)/s | - | - |
| Kling 4.0 Flash | com vídeo de entrada, entrada > saída | por segundo; total = entrada + saída | 0,4 unit (US$ 0,063)/s | - | - |
| Kling 3.0 Turbo | com áudio nativo | por segundo; total = saída | 0,8 unit (US$ 0,112)/s | 1,0 unit (US$ 0,14)/s | - |
| Kling 3.0 | sem áudio nativo | por segundo; total = saída | 0,6 unit (US$ 0,084)/s | 0,8 unit (US$ 0,112)/s | 3,0 units (US$ 0,42)/s |
| Kling 3.0 | com áudio nativo | por segundo; total = saída | 0,9 unit (US$ 0,126)/s | 1,2 unit (US$ 0,168)/s | 3,0 units (US$ 0,42)/s |
| Kling 3.0 | Motion Control | por segundo; total = saída | 0,9 unit (US$ 0,126)/s | 1,2 unit (US$ 0,168)/s | - |
| Kling 3.0 Omni | sem vídeo de referência, sem áudio | por segundo; total = saída | 0,6 unit (US$ 0,084)/s | 0,8 unit (US$ 0,112)/s | 3,0 units (US$ 0,42)/s |
| Kling 3.0 Omni | sem vídeo de referência, com áudio | por segundo; total = saída | 0,8 unit (US$ 0,112)/s | 1,0 unit (US$ 0,14)/s | 3,0 units (US$ 0,42)/s |
| Kling 3.0 Omni | com vídeo de referência, sem áudio | por segundo; total = saída | 0,9 unit (US$ 0,126)/s | 1,2 unit (US$ 0,168)/s | 3,0 units (US$ 0,42)/s |
| Kling O1 | sem vídeo de referência | por segundo; total = saída | 0,6 unit (US$ 0,084)/s | 0,8 unit (US$ 0,112)/s | - |
| Kling O1 | com vídeo de referência | por segundo; total = saída | 0,9 unit (US$ 0,126)/s | 1,2 unit (US$ 0,168)/s | - |
| Kling 2.6 | sem áudio nativo | por segundo; total = saída | 0,3 unit (US$ 0,042)/s | 0,5 unit (US$ 0,07)/s | - |
| Kling 2.6 | com áudio, sem referência de voz | por segundo; total = saída | - | 1,0 unit (US$ 0,14)/s | - |
| Kling 2.6 | com áudio e referência de voz | por segundo; total = saída | - | 1,2 unit (US$ 0,168)/s | - |
| Kling 2.6 | Motion Control | por segundo; total = saída | 0,5 unit (US$ 0,07)/s | 0,8 unit (US$ 0,112)/s | - |
| Kling 2.5 Turbo | sem áudio nativo | por segundo; total = saída | 0,3 unit (US$ 0,042)/s | 0,5 unit (US$ 0,07)/s | - |
| Multi-element Video Editing | - | a cada 5 s; total = saída | 3 units (US$ 0,42)/5 s | 5 units (US$ 0,70)/5 s | - |
| Avatar | vídeo | por segundo; total = saída | 0,4 unit (US$ 0,056)/s | 0,8 unit (US$ 0,112)/s | - |
| Avatar | TTS | por chamada | 0,05 unit (US$ 0,007) | - | - |
| Lip Sync | sincronia labial | a cada 5 s | 0,5 unit (US$ 0,07)/5 s | - | - |
| Lip Sync | reconhecimento de rosto | por chamada | 0,05 unit (US$ 0,007) | - | - |
| Geração de áudio | texto para áudio | por chamada | 0,25 unit (US$ 0,035) | - | - |
| Geração de áudio | vídeo para áudio | por chamada | 0,25 unit (US$ 0,035) | - | - |
| Geração de áudio | voz personalizada | por chamada | 0,05 unit (US$ 0,007) | - | - |
| Reconhecimento de imagem | - | por chamada | 0,1 unit (US$ 0,014) | - | - |

**O valor do unit**, tirado da divisão de cada célula: nas seis linhas do 4.0 e do 4.0 Flash, cerca de US$ 0,157 por unit (1,0 unit = US$ 0,157); nas outras 23, US$ 0,14 por unit. A página não diz por que o unit vale diferente, nem quanto custa um pacote, o tamanho mínimo, a validade ou se há cobrança fora de pacote.

## O changelog, nas entradas de vídeo

- **04/11/2026, Kling 4.0 Flash na API.** Vídeo de 3 a 20 s a 720p, por texto, por imagem e por referência Omni, nos caminhos `/text-to-video/kling-4.0-flash`, `/image-to-video/kling-4.0-flash` e `/omni-video/kling-4.0-flash`. Na imagem para vídeo, só o quadro inicial. Duração e proporção vão por parâmetro ou no próprio prompt, "including 21:9 and adaptive aspect ratios". Limites: prompt de até 26.000 caracteres em inglês, até 10 imagens e até 5 vídeos de referência; na referência Omni, imagens, vídeos e elements se combinam, para gerar e para editar, num teto de 15 entradas por tarefa. A cobrança segue a duração total, e a entrada aqui inclui o vídeo de referência, o vídeo a editar e o vídeo dos elements de personagem.
- **28/10/2026, Kling 4.0 "Fully Available".** Saída nativa de até 30 s numa geração; 720p e 1080p, com a ressalva "(10-bit 4K coming soon)"; as proporções 21:9 e adaptive entram como novidade. Mesmos três caminhos, com `kling-4.0` no fim. Até 10 quadros-chave de entrada. O endpoint Omni passa a citar voz direto. Os limites de prompt, imagem e vídeo são os mesmos do Flash; o teto de 15 entradas vem com menos parâmetros e menos exclusões mútuas, o que a Kling apresenta como integração mais barata. A cobrança pela duração total conta, nesta entrada, o vídeo de referência e o dos elements de personagem.
- **15/07/2026, a nova API (a do 3.0 Turbo) para mais modelos:** 3.0, 3.0 Omni, 3.0 Motion Control, 2.6, 2.6 Motion Control e 2.5 Turbo. Estrutura mais simples, menos acoplamento entre parâmetros, consulta em lote por ID e paginação por cursor. "The legacy API will continue to be available with no current plans for deprecation." A documentação passa a exportar Markdown.
- **06/07/2026, extrato de débitos pela API:** débitos de pacote e de saldo, em APIs separadas, filtráveis por período, chave de API, ID e nome do pacote, com paginação por cursor.
- **17/06/2026.** (a) **Kling 3.0 Turbo** lançado: texto e imagem para vídeo a 720p e 1080p, cobrado pela duração gerada, 0,8 unit/s a 720p e 1,0 a 1080p; a nova API só aceita chave de API. (b) **3.0 Omni** com vídeo de referência de 3 a 15 s e com 4K; com vídeo de referência de característica, várias tomadas exigem `multi_shot` verdadeiro, `shot_type` `intelligence` e a descrição das cenas no prompt; o 4K custa 3 units por segundo gerado. (c) Autenticação só por chave de API, ao lado da AK/SK. (d) Dois elements novos na biblioteca oficial, Grace e Armored Youth.
- **07/05/2026:** `kling-v3-omni` e `kling-v3` passam a aceitar várias tomadas junto com primeiro e último quadro (antes se excluíam).
- **23/04/2026, 4K nativo** com `mode` igual a `4k`, cobrado a 3 units por segundo gerado: no Omni (`kling-v3-omni`) em tudo menos vídeo de referência, e no texto e na imagem para vídeo do `kling-v3`.
- **01/04/2026:** só explicação, no 3.0 Omni, de como o vídeo de referência muda os elements e o número de imagens (`image_list`, `element_list`); a lógica não mudou.
- **23/03/2026:** elements de várias imagens também ganham voz, pelo `element_voice_id`, como já tinham os elements de vídeo.
- **11/03/2026:** `shot_type` `intelligence` no 3.0 Omni, para storyboard automático. Regras esclarecidas na mesma entrada: o `kling-video-o1` não aceita element ao gerar com quadro inicial e final; element criado por vídeo só pode ser realista e humanoide; `element_voice_id` é string; várias câmeras não aceitam quadro inicial e final; imagem que não é quadro inicial nem final vai sem o parâmetro `type`; e uma descrição de quais modelos têm controle de tom.
- **04/03/2026, Motion Control 3.0.** O element pode ser ligado para dar consistência, e com ele só se segue a orientação da pessoa no vídeo; o parâmetro `model_name` separa as versões, com `kling-v2-6` como padrão; 0,9 unit/s no modo STD e 1,2 no PRO.
- **25/02/2026:** lançados o 3.0 Omni e o V3, em vídeo e em imagem. Elements reformulados: podem nascer de um vídeo e levar voz, a criação vira serviço assíncrono, e a API nova (`advanced-custom-elements`) tem biblioteca à parte da antiga, sem consulta cruzada.
- **23/01/2026:** a partir da vista frontal de um element, o serviço infere outros ângulos e devolve três conjuntos para escolher, a 0,5 unit por chamada; a consulta da tarefa passa a trazer os units gastos (`final_unit_deduction`); parte das APIs gera também uma versão com marca d'água (`watermark_info`, devolvida em `watermark_url`).
- **22/12/2025, Motion Control lançado** (a entrada não nomeia o modelo). Imagem e vídeo de referência vão juntos; modo standard a 0,5 ponto por segundo e alta qualidade a 0,8, com os segundos arredondados para o inteiro mais próximo; o vídeo de referência vai até 30 s quando a orientação segue o vídeo e só até 10 s quando segue a imagem; ainda sem biblioteca de ações.
- **16/12/2025:** V2.6 com voz escolhida por `voice_list` no prompt, 6 units por 5 s e 12 por 10 s; voz própria ou predefinida.
- **15/12/2025:** V2.6 lançado em texto e imagem para vídeo, com o áudio ligado pelo parâmetro `sound`; lançados também o Omni-Video e o Omni-Image, API nova em que várias funções se pedem só pelo prompt.
- **04/12/2025:** Avatar chega a vídeos de 5 minutos, sem mudar parâmetros.
- **17/11/2025:** 2.5 Turbo PRO com primeiro e último quadro (`image` e `image_tail`), 2,5 units por 5 s e 5 por 10 s.
- **11/11/2025:** 2.5 Turbo em modo STD, texto e imagem para vídeo, 1,5 unit por 5 s e 3 por 10 s.
- **03/11/2025:** Avatar mais rápido, de uma hora para pouco mais de 10 minutos, sem mudar código.
- **20/10/2025:** 2.5 Turbo em texto e imagem para vídeo, modo PRO, 5 s a partir de 2,5 units; API de reconhecimento de elementos numa imagem (sujeitos, rostos, roupas; 4 conjuntos por pedido), para Multi-Image to Video e Multi-Elements.
- **15/10/2025:** Avatar lançado (vídeo de rosto falando a partir de imagem, áudio ou texto); com vários rostos na imagem, ainda não se escolhe qual.
- **29/09/2025, aviso:** imagens e vídeos gerados pela API são apagados depois de 30 dias e devem ser baixados a tempo.
- **15/09/2025:** Lip-Sync com várias pessoas na tela (`face_id`) e com instante de início (`sound_insert_time`), e corte de áudio; TTS online, com `audio_id` reaproveitável nas APIs.
- **05/09/2025:** V2.1 com quadro inicial e final, 5 ou 10 s, só no modo PRO; Video-to-Audio aceita prompt de efeito sonoro e de trilha e um modo ASMR.
- **15/08/2025:** Video-to-Audio aceita vídeo em resolução cheia; Multi-Image to Video com melhora declarada de "102%" (consistência, dinâmica, aderência ao prompt), sem mudar código.
- **12/08/2025:** texto para vídeo V1.6 em modo PRO, 5 e 10 s.
- **01/08/2025:** lançados Text-to-Audio e Video-to-Audio (para vídeo da Kling ou enviado).
- **21/07/2025, Multi-Elements:** acrescentar, trocar e remover elementos de um vídeo existente, que antes precisa ser inicializado e marcado.
- **30/06/2025:** Lip-Sync de até 60 s (eram 10), com geração a partir de 2 minutos.
- **19/06/2025:** imagem para vídeo `kling-v2-1` (STD e PRO) e `kling-v2-1-master` em imagem e texto para vídeo.
- **13/05/2025:** `kling-v2-master` em texto e imagem para vídeo, sem o parâmetro `mode`.
- **31/03/2025:** V1.6 PRO gera a partir do quadro final; V1.5 e V1.6 ganham extensão de 4 a 5 s (para trás, quando o vídeo foi gerado só com o último quadro).
- **12/03/2025:** V1.5 PRO com quadro inicial e final, só final, motion brush e controle de câmera (só o simples); V1.6 PRO com quadro inicial e final; Lip-Sync para qualquer vídeo de até 10 s em 720p ou 1080p, com 8 vozes novas em chinês e inglês.
- **07/01/2025:** V1.6 lançado (texto para vídeo STD, imagem para vídeo STD e PRO), ainda sem quadro final, motion brush e câmera.
- **23/12/2024:** Lip-Sync para vídeos do V1.0 e do V1.5 que cumpram os requisitos de rosto.
- **09/12/2024:** V1.5 STD só em imagem para vídeo, sem quadro final.
- **02/12/2024:** criado o mapa de capacidades, para conferir de relance o que cada versão tem.
- **29/11/2024:** Motion Brush, só no V1.0 com 5 s, STD e PRO.
- **15/11/2024:** V1.5 PRO só em imagem para vídeo, sem quadro final; extensão de 4 a 5 s para vídeos do V1.0; campo `external_task_id`.
- **25/10/2024:** o que se gera é apagado depois de 30 dias.
- **19/09/2024:** `prompt` e `negative_prompt` limitados a 2.500 caracteres.

**Fora desta ficha** (as demais entradas do mesmo changelog): os lançamentos e as retiradas de efeitos de vídeo prontos, por nome (a maior parte das entradas de 2025 e 2026); Virtual Try-On (19/09/2024, 30/12/2024, 15/09/2026); geração de imagem e Multi-Image to Image (modelos V1.5, V2, V2.1, Omni-Image, o `series_amount` em `auto`, a troca de `model` por `model_name`); os produtos prontos Video Commerce (07/09/2026), Goods Studio (21/08/2026) e AI Apparel Replicator (18/08/2026); assinatura de webhook (07/08/2026); TTS de 1.000 caracteres (26/09/2025); consulta de pacotes (30/10/2024); e o exemplo de código em Java (15/10/2024).

## Contradições e desencontros dentro da documentação

- **4K do Kling 4.0.** O mapa de capacidades (atualizado em 20/10/2026) dá ao 4.0 "720P, 1080P, 4K". A entrada de 28/10/2026 do changelog diz "Supports 720P and 1080P (10-bit 4K coming soon)". A tabela de preço tem a coluna 4K vazia ("-") nas três linhas do 4.0. As três páginas são da mesma documentação e não se reconciliam.
- **Duração do vídeo de referência do 3.0 Omni:** o mapa diz "3–15.5 seconds"; a entrada de 17/06/2026, "3–15 seconds".
- **Data do mapa:** "Updated At: 2026-10-20", e o mapa já traz o 4.0 Flash, cuja entrada no changelog é de 04/11/2026.
- **O que conta como vídeo de entrada no 4.0:** a entrada de 28/10 cita o vídeo de referência e o dos elements de personagem; a de 04/11 (Flash) e a tabela de preço incluem também o vídeo a editar.
- **Motion Control por modo ou por resolução:** o changelog dá o preço por modo (3.0: STD 0,9 e PRO 1,2; o lançamento de 22/12/2025: standard 0,5 e alta qualidade 0,8); a tabela de preço põe os mesmos números nas colunas de 720p e 1080p do 3.0 e do 2.6.
- **4K do 3.0 Omni com vídeo de referência:** a entrada de 23/04/2026 exclui o vídeo de referência do 4K; a de 17/06/2026 anuncia vídeo de referência de até 15 s e 4K no 3.0 Omni; a tabela de preço tem 4K a 3,0 units na linha "With Reference Video Input x No Native Audio".

## O que estas páginas não dizem

- O preço e o tamanho de um pacote de units, a compra mínima, a validade dos units, e se há cobrança por saldo fora do pacote.
- Preço do 4K no 4.0, nem o que quer dizer "10-bit" ali.
- Se o áudio nativo muda o preço do 4.0 e do 4.0 Flash (a tabela não separa com e sem áudio nesses modelos).
- Preço do 3.0 Omni com vídeo de referência e com áudio nativo, e do 3.0 Turbo sem áudio (não há linha).
- Como se arredonda o segundo cobrado no 4.0 (o arredondamento só aparece na entrada de 22/12/2025, para o Motion Control).
- Qualquer regra sobre rosto de pessoa real ou moderação de entrada.
- Se a mesma imagem pode ser primeiro e último quadro.
