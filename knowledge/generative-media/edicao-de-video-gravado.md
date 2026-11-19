# Edição de vídeo gravado com agente: camadas, manual de números e visão

Reúne o que se sabe sobre editar talking head com agente: as camadas, o manual numérico de corte e áudio, e as peças da camada de visão. O mecanismo (código, navegador headless, ffmpeg), os motores e os custos por token ficam em [[video-como-codigo]]; aqui está o que fazer com um vídeo que já foi gravado, para quem tem em "gravar e editar vídeo" o gargalo de conteúdo.

O ecossistema já é mais sobre editar do que sobre gerar: a maior categoria do índice awesome-claude-video-skills é edição de footage existente, 37 de 183 repositórios (*Awesome Claude Video Skills — open-source skills and toolkits that let coding agents make video (índice)*, de zhuyansen / Agent Skills Hub, https://github.com/zhuyansen/awesome-claude-video-skills).

## As cinco camadas

Cada camada tem entrada e saída próprias e alimenta a seguinte. Nenhuma ferramenta aberta faz todas bem; o agente compõe.

1. **Corte bruto.** O `claude-code-video-editing-skill` roda 100% local (whisper.cpp + ffmpeg, Windows incluído): junta clipes sem recodificar, corta só em silêncio, transcreve ilha por ilha para pegar retakes, mantém o último take e nunca corta palavra; 9 minutos viraram 1:58 em dois minutos de máquina, e sai `edited.srt` (*Claude Code video editing skill — automatic rough cut of your raw footage (README)*, de Vincent Ventalon, https://github.com/vincentventalon/claude-code-video-editing-skill). O `video-use` (27,6 mil estrelas) faz o corte mais cor, legenda queimada e fades de 30 ms, e se autoavalia em cada ponto de corte; transcreve pela API Scribe da ElevenLabs. O princípio dele é "o modelo não assiste, lê": 12 KB de transcrição mais PNGs sob demanda (*video-use — edit videos with Claude Code (README)*, de Browser Use, https://github.com/browser-use/video-use).
2. **Áudio.** Limpeza e nível da voz, música de fundo e efeitos. A regra é a do manual de números abaixo. Música e efeitos entram por API (ElevenLabs Sound Effects e Music, Suno) ou catálogo livre; a mixagem com ducking, EQ, compressor e limiter tinha skill pronta no HyperFrames, `/hyperframes-audio` (*HyperFrames — Write HTML. Render video. Built for agents. (README)*, de HeyGen, https://github.com/heygen-com/hyperframes). Na lista de novembro de 2026, o HyperFrames tinha 9 skills, e `/hyperframes-audio` e `/embedded-captions` não estavam mais nela; o `/media-use` diz cobrir voz, música, efeitos e a mistura do áudio ([[2026-11-11-hyperframes-readme-skills-pro-e-adaptador-three]]; o estado em [[video-como-codigo]]). Um "ASMR de teclado, 6 segundos, em loop" é uma chamada de efeito sonoro, não uma capacidade do modelo.
3. **Legenda.** Tempo por palavra do Whisper, quebra em blocos curtos, queima no vídeo. A `/embedded-captions` do HyperFrames fazia isso sobre talking head sem tocar o footage; ela saiu da lista de novembro de 2026, e o FAQ diz que o agente legenda talking head sem mexer no footage ([[2026-11-11-hyperframes-faq]]); o `video-use` queima em blocos de duas palavras em maiúsculas por padrão.
4. **B-roll.** O `motion-broll` recebe vídeo + SRT, planeja os clipes em tabela, espera aprovação e devolve MP4 para cutaway ou ProRes 4444 com transparência para painel ao lado do apresentador (*motion-graphics / motion-broll — Motion-graphic B-roll for your videos, made by Claude Code (README)*, de Barty-Bart, https://github.com/Barty-Bart/motion-graphics). Na demo do autor: Opus 5.5 em medium, 4 a 5 clipes para 33 segundos, cerca de 15 minutos, aprovado sem re-prompt; o corte e a transição para o terço lateral ele fez à mão, e a transcrição vem de fora (*Claude Opus 5.5 Just Solved Motion Graphics (No More AI Slop) — demo da skill motion-broll pelo autor*, de Bart, canal no YouTube, https://www.youtube.com/watch?v=6Ij9-f2T2Ck). O `edited.srt` da camada 1 é a entrada que ele pede. Para overlays desenhados sobre o mesmo footage há o `/talking-head-recut` do HyperFrames; para footage real, `b-roll-finder`.
5. **Visão.** Recorte da pessoa, mão, objetos e 3D ancorado. Peças abaixo.

## O manual de números

O relato mais útil para o corte e o áudio é o de Wado, que parou de terceirizar a edição (cerca de ¥20.000 por vídeo) e passou a entregar ao Claude Code um texto com parâmetros (*I stopped outsourcing video editing with Opus 5.5 (o manual de números)*, de Wado, note.com/wad0427, https://note.com/wad0427/n/nee76ed7d62f2). Sem software de edição: ffmpeg, Python e Remotion para a abertura.

| Etapa | Parâmetro |
|---|---|
| Silêncio | RMS a cada 10 ms com média móvel de 3; abaixo de -45 dB é silêncio; sai o que passa de 0,20 s, mantendo 0,05 s antes da fala e 0,10 s depois |
| Respiro | Trecho com pico abaixo de -30 dB e menos de 0,6 s sai |
| Emenda | Fade de 4 ms; descarta trecho de som menor que 0,04 s |
| Voz | Corta abaixo de 75 Hz; gate em -38 dB; 250 Hz -2,5 dB, 3,5 kHz +3 dB, 5 kHz +1,5 dB; corta acima de 14 kHz; compressor 3:1 |
| Volume final | -14,5 LUFS, True Peak -2 dB |
| Música | 20 dB abaixo da voz, mais 3 dB de redução durante a fala |
| Legenda | Fonte, 92 px, branco com borda preta, 18 caracteres por linha (japonês) |
| Verificação | Carrega sem erro; -14,5 ± 0,5 LUFS e pico ≤ -1,5 dB; nenhum vão de voz acima de 0,3 s; item não conferido se escreve "unverified" |

Medido num vídeo de 16 minutos: 985 s viraram 808 s, 348 cortes, 107 respiros removidos (9,84 s). Limites que ele declara: não remove "hã" automaticamente, para não apagar nome próprio ou citação junto; não serve para multicâmera nem corte no ritmo de música; eco de sala não se conserta na edição.

A tese dele é a que mais vale para a base: os números são texto e sobrevivem à troca de modelo. O manual também tem a forma do portão em código de [[classificacao-como-portao]]: critério mensurável, e abstenção explícita no que não foi conferido. Os valores são dele, para a voz e a sala dele; o que se transfere é ter o arquivo, não os números. Para a música sob narração, o teste de preferência de Torcoli e colegas (2019) recomenda de 10 a 15 LU durante a fala, abaixo dos 20 dB dele ([[mixar-narracao-trilha-e-efeitos]]).

## Camada de visão: as peças

O reel de Paulo Shimada (*Claude can finally edit like a pro (reel): antes e depois de um talking head editado com Opus 5.5*, de Paulo Shimada, @pauloshimas no Instagram, https://www.instagram.com/reel/Dd4S4nYysi1/) demonstra detecção de objetos, recorte da pessoa como adesivo, lata 3D na palma que acompanha a mão. Não há skill aberta que entregue esse conjunto; há as peças.

| Função | Peça | O que a primária diz | Licença |
|---|---|---|---|
| Recorte de pessoa em vídeo | RobustVideoMatting | Rede recorrente com memória temporal, sem trimap; 104 fps em HD numa GTX 1080 Ti (só tensor; o script de conversão é bem mais lento); `convert_video` devolve o alfa como vídeo | GPL-3.0 |
| Recorte quadro a quadro | rembg | `rembg b` lê quadros do ffmpeg por pipe; `birefnet-portrait` para retrato; sem memória entre quadros | Código MIT; o modelo padrão `bria-rmbg` exige contrato pago para uso comercial |
| Recorte e rastreio por frase | SAM 3 e 3.1 | Detecta, segmenta e rastreia em vídeo a partir de texto; Python 3.12, CUDA 12.6, checkpoints sob pedido; números só em H100 | SAM License |
| Mão | MediaPipe Hand Landmarker | 21 pontos em imagem e em mundo, lateralidade, modo vídeo; 17 ms em CPU de celular | Apache 2.0 |
| Skill já empacotada | clip-skills | Máscara de sujeito com SAM ViT-B para texto atrás da pessoa e rastreio com SAM 2; checkpoints de 375 MB a 2,4 GB | não lida |
| 3D | Three.js | Adaptador no HyperFrames; pacote de 24 skills para Claude Code, cuja skill de animação manda avançar o mixer pelo delta de um relógio; leitura do assistente: vai contra o render por quadro (detalhe em [[video-como-codigo]]) | MIT |

Fontes: *RobustVideoMatting — Robust High-Resolution Video Matting with Temporal Guidance (README)*, de Shanchuan Lin et al., ByteDance, https://github.com/PeterL1n/RobustVideoMatting; *rembg — tool to remove image backgrounds (README)*, de Daniel Gatis, https://github.com/danielgatis/rembg; *SAM 3: Segment Anything with Concepts (README e notas da versão 3.1)*, de Meta AI, https://github.com/facebookresearch/sam3; *MediaPipe Hand Landmarker — hand landmarks detection guide*, de Google AI Edge, https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker; *clip-skills PR nº 4 — Add SAM/SAM 2 subject masking+tracking, --crop-track, and campaign-tracker*, de insanity103, https://github.com/insanity103/clip-skills/pull/4; o pacote de skills do Three.js ([[2026-11-11-threejs-claude-skill-package-readme]]); a combinação MediaPipe mais SAM 2 para segmentar mãos ([thevisiblehand](https://github.com/abhishekk962/thevisiblehand)) fica como citação.

**Numa máquina de entrada** (Windows, GTX 1660 Ti de 6 GB, medido): RobustVideoMatting e MediaPipe cabem; o BiRefNet completo pede 3,45 GB a 1024 por 1024 numa RTX 4090 e seria lento; o SAM 3 não informa memória mínima e é o candidato a não rodar. O recorte gratuito do OpenEdit e a rota do Apple Vision são de Mac.

Para uso próprio, sem redistribuir, a GPL do RobustVideoMatting não pesa; o modelo padrão do rembg pesa para uso comercial, e a troca por `birefnet-portrait` resolve.

## Sistemas que empacotam

- **OpenMontage** (61,9 mil estrelas, AGPLv3): pipelines com portões de aprovação, validação pré-render, autorrevisão por ffprobe e orçamento com teto; caminho gratuito com Piper, arquivos abertos, Remotion e HyperFrames (*OpenMontage — agentic video production system (README)*, de calesthio, https://github.com/calesthio/OpenMontage). O mais completo e o mais pesado.
- **OpenEdit** (VEED): pipeline Apache-2.0 com legenda, cortes, motion graphics e remoção de fundo por rota gratuita; transcrição local por WhisperX; renderizador fechado; só Mac com Apple Silicon (*OpenEdit — open-source, agent-driven editing pipeline (anúncio da VEED e README da CLI)*, de VEED, https://www.veed.io/newsroom/openedit-by-veed).
- **Corte pessoal que cresce**: o autor do `claude-code-video-editing-skill` publica um vídeo por dia com um pipeline de 1.400 linhas de instrução e trinta scripts, que cresceu pedindo uma coisa por vez ao Claude. É o mesmo desenho do manual do Wado.

## Edição presa às palavras e revisão por blocos: o agent-video-editor

O `agent-video-editor` do Rodrigo Tadewald ([[2026-11-12-rtadewald-agent-video-editor]], README de 29/10/2026, sem licença; o autor é sócio de uma escola que vende cursos sobre o tema) põe o Claude Code como editor do bruto ao aprovado, em duas skills, e o criador revisa num app local. Cobre o corte, o áudio, a legenda e os inserts das camadas acima, e traz quatro coisas que elas não têm:

- **O contrato preso aos IDs das palavras, nunca a segundos.** O `video-use` já lê a transcrição com tempo por palavra e corta na fronteira da palavra; aqui corte, bloco e comentário se ancoram na palavra, e o mesmo trecho continua o mesmo de uma versão a outra. Leitura do assistente: é o que deixa a edição sobreviver a um recorte ou a um retake.
- **A revisão por blocos versionados:** blocos de cerca de 30 s (nunca menos de 15 s), cortados nas trocas de plano, cada um com a sua versão e um botão que o trava; os comentários pendentes de qualquer versão entram na seguinte.
- **A calibragem e os aprendizados por categoria de vídeo:** vídeos de referência que o criador fornece, analisados; as regras dele por categoria; e, ao aprovar, as correções que ele confirma viram aprendizado, lido antes de cada etapa dos vídeos seguintes. Leitura do assistente: vai além da memória de sessão do `video-use`, que guarda o projeto em `project.md`.
- **Um corpo, várias saídas:** o mesmo vídeo com finais diferentes por destino, e a voz do CTA gravado à parte casada com a do corpo.

O antecessor, o `harness-video-editor` ([github.com/rtadewald/harness-video-editor](https://github.com/rtadewald/harness-video-editor), outubro de 2026, sem licença; citação), tinha seis etapas numa interface no estilo do Premiere: cortes colados em silêncio real, enquadramento que segue o rosto, LUT, velocidade de 1× a 1,5×, transições com som escolhidas pelo par de tipos de plano, voz a −14 LUFS e legenda; a Calibragem dele pedia os Reels já editados do criador, e ele exigia macOS com Apple Silicon. O README do editor atual não diz o sistema; pede `uv`, `ffmpeg`, o Claude Code e chaves do OpenRouter e da ElevenLabs, sem estimar custo por vídeo.

**Para um editor próprio (leitura do assistente):** três ideias valem mais que o resto, e nenhuma depende de rodar o código: a edição presa às palavras; a revisão por blocos, que deixa quem pede aprovar trecho a trecho; e a calibragem por vídeos de referência com aprendizados por categoria, que é o que o portão das peças faz com as rubricas. Usar como referência os Reels que a própria pessoa já publicou é leitura do assistente (o antecessor pedia os Reels do criador; o README atual fala só em vídeos de referência). Só método: os repositórios não têm licença.

## O que a onda do Opus 5.5 mostra sobre edição

O levantamento de athemeroy sobre 1.401 vídeos separa quatro papéis do modelo: desenhar por código, editar mídia fornecida, dirigir outro modelo, e construir um app que alguém grava. Motion graphics e render 3D somam 60,2% dos rotulados; edição de mídia fornecida é um dos caminhos, e a pergunta que ele manda fazer é "o que a performance, o áudio ou os arquivos fornecidos contribuíram?" (*Awesome Claude Opus 5.5 Videos — source-linked guide to videos people made with Claude Opus 5.5 (README)*, de athemeroy, https://github.com/athemeroy/awesome-opus-5-5-videos). No reel do Shimada a resposta é: muito; o take foi coreografado gesto a gesto, e "edited 100%" descreve a pós-produção.

Custo em cota: um filme narrado de 3 minutos consumiu cerca de 7% da cota semanal de uma criadora (*Claude Opus 5.5 for video*, de Heather Cooper, Visually AI, Substack, https://heatherbcooper.substack.com/p/claude-opus-55-for-video). O "talking head" dela é gerado de selfies e amostra de voz por ferramentas via MCP, não edição de gravação.

## Ordem de retorno

Pela distância entre o que está pronto e o gargalo: corte e áudio por números primeiro (local, sem chave, resultado mensurável), depois legenda, depois b-roll com aprovação da tabela, e visão por último, porque é a camada com mais setup e a que mais depende de como o take foi gravado. Gravar não mudou, e o gosto também não: as ferramentas cortam onde há silêncio e põem gráfico onde há palavra-chave.

## Não verificado

- Quais ferramentas o Shimada usou para recorte, detecção e rastreio; o guia fica atrás do "comente EDIT".
- Memória de GPU mínima do SAM 3 e desempenho real do RobustVideoMatting numa GTX 1660 Ti.
- Custo de uma rodada do OpenEdit com Opus 5.5 (1h51, US$ 23 em tokens, US$ 49 em fal): só em resumo de busca de um artigo no X.
- Do Gemini, sem fonte: "US$ 8,34 por short", laço com agente avaliador e Stop hook aplicado a vídeo, recorte pelo Apple Vision. "HyperFrames lançado no fim de setembro" é falso.
- YOLO26 (detecção sem NMS, janeiro de 2026): citado pelo Gemini, primária não aberta.
- Data do `motion-broll`: fim de setembro, sem dia; "resolveu o AI slop" é título, sem definição nem medida.
- Crítica independente à edição por agente: não achei; os limites vêm dos próprios praticantes.
