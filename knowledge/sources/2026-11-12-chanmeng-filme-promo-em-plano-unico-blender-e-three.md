---
titulo: "Making a One-Take 3D Promo Film with three.js, Blender and Real Instrument Samples"
tipo: artigo
autor: "Chan Meng"   # meta author e author do JSON-LD (BlogPosting); o post fala na primeira pessoa, como autor do archlang e do repositório
url: "https://chanmeng.org/blog/archlang-one-take-promo-film"
publicado_em: 2026-10-28   # data na página ("October 28, 2026 (2w ago) · 18 min read") e meta article:published_time; o dateModified do JSON-LD repete 2026-10-28
capturado_em: 2026-11-12
licenca: "protegido (a página lida não traz aviso de copyright nem licença de conteúdo); o post diz que o código do repositório que cita, ChanMeng666/archlang-promo-threejs, é MIT, o que vale para o código, não para o texto do post; ficha de estudo em palavras próprias, sem o integral"
areas: [generative-media]
tags: [threejs, blender, headless-rendering, playwright, chromium, glb, deterministic-rendering, video-as-code, continuous-shot, camera-travel, camera-keyframes, depth-of-field, motion-blur, software-webgl, audio-sync, cc0, ffmpeg, ai-assistant-workflow]
---

# Chan Meng: filme de 32 s em plano único, com o Blender só no modelo e o three.js na câmera

Ficha de estudo: as seções seguem a ordem do post (a abertura, as seções 1 a 11 e os créditos), com o método em listas e tabelas, os números com a condição em que o autor os dá e as ressalvas dele. Não há integral: o post é protegido.

**Proveniência.** Post no blog pessoal de Chan Meng, https://chanmeng.org/blog/archlang-one-take-promo-film, baixado em HTML em 2026-11-12 e lido no texto extraído do HTML, conferido no HTML para título, autor e data. sha256 do texto do bloco `<main>`/`<article>`, sem tags, script e estilo, registrado na rodada: (hash omitido) (conferido de novo no HTML do a cópia de trabalho; o do arquivo inteiro, que muda a cada download, é (hash omitido)). Sem captura na Wayback. Título conferido no `<h1>` e no `og:title`. Cobertura: o texto inteiro do post, da abertura às seções 1 a 11 e aos créditos, com os trechos de código; o rótulo da rodada registrava a leitura das seções 1 a 7, do começo da 8 e da linha do tempo de render da 8, e esta ficha leu também o resto da 8 e as seções 9 a 11 e os créditos. Não foram abertos o vídeo embutido, o repositório, a release, o `CREDITS.md` nem o projeto onetake.

**Quem fala.** O autor do archlang (a linguagem aberta dele para escrever planta baixa como código) e do repositório do filme. Ele conta que não escreveu o código à mão: dirigiu pelo chat um assistente de IA de desktop, o Grok Bot, que instalou, programou, renderizou e publicou num computador Linux na nuvem do próprio assistente.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). O `parafrase.py` contra o texto extraído saiu com o código 3 (ficha em português, fonte em inglês): 110 unidades medidas (66 de prosa, 44 de célula com texto); fora da conta, 178 células de fato, 32 de cabeçalho e 22 frases curtas demais para medir; 1 colada de 110 (1%, uma célula que só lista requisitos); 0 trecho de 3 ou mais seguidas. Pela conta lado a lado, sobre as mesmas unidades medidas pelo script, 92 de 110 seguem uma frase da fonte (traduzem, juntam duas ou fundem três ou mais seguidas); ficam de fora da conta de "segue" a proveniência, a descrição do código da seção 3 (o começo da fonte `.arch`, as constantes, os valores de `K`), a lista de requisitos, um rótulo de tabela e três das quatro frases da lacuna. A maior sequência de unidades seguidas que seguiam a fonte tinha 51 unidades (da digitação na grade, seção 3, ao acompanhamento do render, seção 8): é método e dados na ordem do post, como pede a ficha de estudo, e se declara aqui. Na revisão, os blocos de prosa das seções 5 e 6 (a mola, o "punch" e a flutuação, a profundidade de campo, a abertura da trilha e os dois "Com o assistente") foram reescritos, abrindo pelo porquê ou pelo efeito e trocando a ordem das frases; o `parafrase.py` passou a medir 107 unidades, 1 colada e 0 trecho. Das cerca de 13 unidades reescritas, 2 ainda acompanham de perto uma frase da fonte (a abertura da trilha e o foco que anda), o total fica em cerca de 81 de 107, e a sequência de 51 se quebra na seção 5; antes dela (da seção 3 ao começo da 5) e depois (do HTML autocontido à seção 8, fora a 6) a ficha segue a ordem do post, como antes (revista em 2026-11-19). Numa segunda rodada no mesmo dia, três trechos apontados por uma conferência independente foram refeitos: a ressalva sobre o 2D subiu para o começo da seção 3 e abre pelo uso; os cinco passos do desfoque da seção 8 viraram uma frase que abre pelo resultado do render e uma tabela que vai da regra ao mecanismo, na ordem inversa à do post; e as cinco células de entrega e de cópia da seção 11 viraram quatro, agrupadas por tema e com a ordem interna trocada. Nesses trechos, antes 11 de 11 unidades seguiam a fonte na ordem dela (5 seguidas no desfoque, 5 na entrega); depois, 3 de 11 ainda acompanham de perto uma frase dela (a janela de exposição, a regra das capturas e a composição do quadro), sem três seguidas na ordem do post (a maior é de 2, a janela e a composição); o total fica em cerca de 73 de 107, e a sequência na ordem do post depois da seção 6 se quebra no desfoque (revista em 2026-11-19). No texto argumentativo (o princípio do tempo primeiro, as consequências do f(t), os números fracos publicados, as lições da seção 10 e os conselhos da seção 11) não há três unidades seguidas que andem para a frente na fonte: as lições juntam duas a duas em outra ordem, separadas por uma tabela de fatos, e os conselhos vão em ordem trocada.

## Abertura: o filme e o que o post cobre

| Item | Fato |
|---|---|
| Para que é | filme promocional do archlang |
| O que o archlang faz | deixa a IA escrever planta baixa como código |
| Roteiro da tomada | código vira linha de planta; a planta vira casinha 3D; a casa volta a ser planta; fecha no logo |
| Cortes | nenhum |
| mp4 | 12,8 MB, na release v1.0.0 do GitHub |
| Versão interativa | um HTML só, de 2,6 MB, com barra para correr o tempo |
| Assuntos do post | a tabela de batidas comum a imagem, modelo e música; a página que vira mp4 com desfoque de movimento; o trabalho com o assistente |
| Blocos sobre o assistente | marcados "Working with the assistant" e resumidos na seção 11 |

## 1. Os números do filme

| Item | Valor |
|---|---|
| Duração | 32,0 s |
| Imagem | 1920×1080, 30 fps |
| Codificação | H.264 + AAC estéreo, 48 kHz |
| Andamento | 120 BPM, 4/4, 16 compassos |
| Uma batida | 0,5 s, ou 15 quadros exatos |
| Cena | uma só, em three.js, sem corte |
| Câmera, profundidade de campo e animações | função pura do tempo |
| Instrumentos | bateria, piano, violoncelo, contrabaixo, glockenspiel, vibrafone, claves, estalos de dedo |
| Origem do som | amostras gravadas, todas CC0 ou domínio público |
| Volume | −16,2 LUFS integrado; pico −1,5 dBFS |
| Render | 960 quadros, 4.657 capturas |
| Tempo do render | cerca de 36 min por passada completa, 3 workers, WebGL por software |

| Trecho | O que acontece |
|---|---|
| 0–4 s | o código se digita; surgem a grade e a seta do norte |
| 4–12 s | entra a bateria; paredes, cômodos, portas, janelas e móveis se desenham na batida, com o código rolando |
| 12–14 s | respiro: carimbo do título, resultado da compilação e cotas; rufo de tom até o tempo forte |
| 14–24 s | a planta sobe em casa 3D; a câmera entra e sai; o telhado pousa na batida; vista aérea parada |
| 24–32 s | a casa se dobra de volta em planta; o logo se desenha; slogan; fichas finais |

## 2. Arquitetura: uma tabela de batidas, duas saídas

O tempo vem antes de tudo: andamento e lista de eventos se fixam antes de existir imagem ou som, e animação e trilha saem dessa mesma tabela, que é a razão, para o autor, de o som acompanhar a imagem sem alinhamento manual.

1. O código `.arch` passa pelo `archlang compile` e vira o SVG da planta (a saída real do compilador).
2. O SVG alimenta o Blender sem tela, que monta a casa 3D em `.glb`.
3. SVG, `.glb` e `events.json` (a tabela de batidas) entram num HTML só, em three.js, com câmera, profundidade de campo e movimento como f(t), acessados por `window.__seek(t)`.
4. O `events.json` também alimenta o `score.py`, que gera `soundtrack.wav` de amostras reais.
5. O Playwright captura o HTML quadro a quadro, com desfoque de movimento por subquadros, em PNG.
6. O ffmpeg junta os PNG e o wav em `archlang-promo.mp4`.

| Arquivo do repositório | Papel |
|---|---|
| `src/comp.js` | a composição: tabela de batidas, desenho do editor, da planta e do HUD, câmera, profundidade de campo, eventos, obturador |
| `src/template.html` | casca HTML e player (tocar, correr) |
| `src/entry.js` | entrada do bundle de three.js e pós-processamento (esbuild) |
| `blender/build_house.py` | Blender sem tela até `laneway_house.glb` |
| `audio/samplers.py` | carga das amostras, altura por reamostragem, camadas de velocidade, bateria com vários microfones |
| `audio/score.py` | partitura e mixagem até `dist/soundtrack.wav` |
| `data/events.json` | a tabela de batidas e 115 eventos de animação |
| `scripts/` | `build.py`, `render.py`, `dump_events.py`, `verify_sync.py`, `still.py`, `fetch_samples.sh` e outros |
| Licença do repositório, pelo post | MIT |

**Com o assistente.** O projeto nasceu de uma conversa: o autor descreveu o filme (promo em uma tomada, cara de 3D, instrumentos reais) e apontou o método "one continuous take" do projeto onetake; o assistente pesquisou o Blender e o ferramental, instalou e propôs a arquitetura acima. Do onetake veio só o método, cuja licença é PolyForm Noncommercial; código e assets dele ficaram fora do repositório.

## 3. Do código archlang à planta

- Antes de tomar o filme como demonstração da ferramenta: o volume da casa é licença da promo, e o próprio autor marca a fronteira. O que o archlang entrega é desenho plano, em SVG, DXF, PDF ou PNG; nada no filme vende o 3D como recurso dele.
- Nada na tela é montado à parte: o editor mostra a fonte real do exemplo laneway-house do archlang (sem comentários nem linhas em branco), e a planta é o SVG que o compilador gera dela, com `npx -y @chanmeng666/archlang compile data/laneway-house.arch -o data/laneway-house.svg`.
- O começo da fonte, mostrado no post, declara milímetros, grade de 50, norte para cima, cotas automáticas, rua ao norte e paredes externas com id e espessura de 200.
- O `comp.js` desenha o SVG peça a peça; parede, cômodo, porta, janela e móvel têm um id, e cada id tem uma batida na tabela de tempo `K`.
- Constantes do código: `BPM = 120`, `BEAT = 60 / BPM`, `DUR = 32`, `FPS = 30`, e `B(b)` converte batida em segundos.
- Valores de `K` mostrados: paredes nas batidas 8 a 13; cômodos em 14, 14,5 e 15; portas de 16 a 17,5; `lift` 28, `roofStart` 43, `roofLand` 46, `roofOff` 48, `logo` 56.
- A digitação também cai na grade: cada linha guarda a batida em que pousa o último caractere dela.

## 4. O Blender faz a casa, e só a casa

| Ponto | Fato |
|---|---|
| Comando | `blender -b --factory-startup --python-exit-code 1 -P blender/build_house.py -- blender` |
| De onde vem a geometria | medida no SVG compilado: paredes, vãos, pegada dos móveis |
| Coordenadas | milímetros da planta (SVG, y para baixo) para metros do Blender: X = x/1000, Y = −y/1000, Z para cima |
| Alturas | escritas no script; a planta é um corte horizontal e não as tem |
| Altura das paredes | `WALL_H = 2.7` m |
| Objetos | um por peça, com o nome do que é (`wall_lane`, `door_front`, `furn_sofa`…) |
| Por que um por peça | o three.js faz cada peça crescer na sua batida |
| Exportação | `bpy.ops.export_scene.gltf`, `export_format='GLB'`, `export_yup=True` |
| Extra | duas prévias PNG em Cycles: 24 amostras, com denoise, na CPU |
| Fora do Blender | câmera e animação |
| Onde mora o movimento | no navegador, como função do tempo |
| Determinismo | rodar de novo refaz o `.glb` do repositório byte a byte |

## 5. O plano único: tudo é função do tempo

A página não guarda estado de animação: `window.__seek(t)` chama `seekScene(t)` e `drawFrame()`, e cada valor da tela sai de `t`. Daí, segundo o autor, qualquer quadro se renderiza em qualquer ordem, em quantos workers paralelos houver, e se refaz depois igual; o aleatório vem de um `rng(seed)` xorshift de semente fixa, nunca de `Math.random()`.

**Mola no lugar do easing de chaves.**

- Por que mola: como a resposta ao degrau de uma mola amortecida tem forma fechada, ela continua calculável em qualquer `t` e ainda dá ao pouso um leve excesso antes de assentar; é o movimento de tudo o que cai numa batida.
- Função: `spring(tau, zeta = .55, om = 22)`, de 0 a 1, nula para `tau <= 0`.
- Portas e paredes: a porta gira numa mola limitada, que passa pouco dos 90° antes de voltar; a parede só começa a subir quando a batida dela já ficou para trás: `rise[w] = t < tt ? 0 : spring(t - tt, .5, 17)`.

**O caminho da câmera.**

| Ponto | Fato |
|---|---|
| Estrutura | lista de chaves `CAMKEYS` |
| Cada chave | tempo, olho, alvo, campo de visão, curva de easing própria |
| Abertura | chaves de cima, de um auxiliar que traduz "mostrar W metros de planta" em altura do olho para lente de 30° |
| Aos 16 s | vista 3/4 |
| De 17 a 20,6 s | altura dos olhos (cerca de 1,5 m), FOV 52–56, deslizando pelos cômodos |
| Saída da casa | sobe com `expoInOut` até a vista aérea |
| Aos 26,2 s | volta à vista de cima, para o cartão final |
| "Punch" | para o espectador sentir o tempo na própria câmera, ela avança um instante rumo ao alvo em cada batida de parede, cômodo, porta e subida, com a mesma mola e um pequeno anel que decai |
| Flutuação de mão | para o quadro parado ficar firme, a oscilação de poucos centímetros no olho e no alvo, feita de somas de senos lentos, se apaga nas pausas |
| Intenção dos dois toques | uma câmera que pareça operada, e não calculada |

**Profundidade de campo como troca de foco.**

- A abertura é um caso à parte: um termo a mais leva o cartão inicial ao foco ao longo do primeiro segundo.
- Foco que anda: depois, no passeio, o foco puxa para o cômodo ou o objeto em cena, porque `FOCKEYS` marca um assunto a cada batida e o ponto de foco pula de um ao seguinte numa mola; a distância nunca fica fixa.
- Como se monta: pós-processamento do three.js, `EffectComposer` com `BokehPass`.

**Um HTML que se basta.**

- `scripts/build.py` embute em `dist/archlang-promo.html` o bundle esbuild do three.js (0.186.1) com os passes de pós-processamento, o `.glb` em base64, o SVG compilado, a marca do archlang, as fontes Archivo e IBM Plex Mono e, quando existe, a trilha em AAC.
- Sem rede, o render se reproduz, e o mesmo arquivo serve de versão interativa na release.

**Com o assistente.** O desenho em f(t) é o que deixava cada ajuste barato, e o log final mostra o efeito: depois da primeira passada completa, só os quadros 618–790 precisaram ser refeitos, duas vezes, para acertar a câmera aérea. O ciclo era curto: diante de um rascunho, o autor pedia em palavras comuns outro enquadramento ou uma câmera mais lenta ou mais firme, e o assistente, antes de partir para o render inteiro, mostrava quadros parados nos segundos em discussão (`scripts/still.py 23.5,31.8`).

## 6. Trilha de instrumentos reais

- Toda a trilha sai de amostras gravadas, que `audio/score.py` encaixa na grade de 120 BPM e mixa com numpy e scipy; instrumento sintetizado, nenhum.
- Os dois "whoosh" que sobem são um prato de ataque de verdade tocado ao contrário, e o impulso do reverb é ruído moldado, que só serve para convoluir os sons gravados: são as únicas peças que vêm de processamento, e não de gravação.

| Biblioteca | Uso no filme | Licença |
|---|---|---|
| Big Rusty Drums (Karoryfer Samplecraft) | a bateria (bumbo, caixa, chimbal, ataque, sino do ride, três tons), os tiques de digitação (aro de tom e baquetas) e os pratos invertidos | CC0 1.0 |
| Splendid Grand Piano (Akai) | acordes Am–F–C–G; acordes do logo e do slogan | domínio público |
| Karoryfer × bigcat Cello | notas longas de fundo; crescendo do logo | CC0 1.0 |
| Karoryfer Meatbass | contrabaixo em pizzicato | CC0 1.0 |
| VCSL (Versilian Community Sample Library) | glockenspiel, vibrafone e claves nos acentos de grade, cômodo, porta, janela, móvel e logo | CC0 1.0 |
| body_percussion | estalos de dedo nas portas | CC0 1.0 |

- As bibliotecas não estão no repositório: `scripts/fetch_samples.sh` baixa só os arquivos usados, em commits fixos, com checkout esparso, raso e sem blobs (`sparse-checkout set`; `fetch -q --depth 1 --filter=blob:none`).

| Peça da mixagem | Como funciona |
|---|---|
| Sampler | `samplers.py` reamostra (`resample_poly`) a partir da nota gravada mais perto, escolhe a camada de velocidade e mistura os microfones da bateria (perto, overheads, embaixo da caixa); o rodízio usa semente fixa |
| Arranjo | groove A em 4–12 s e B em 14–22 s, com bumbo no 1 e no 3, caixa no 2 e no 4 e chimbal em colcheias; viradas de tom na entrada de cada seção; rufo de caixa em colcheias até o tempo forte de 14 s; bumbo nos quatro tempos de 24 a 28 s; prato e bumbo juntos no logo, aos 28 s |
| Sinos da imagem | glockenspiel, vibrafone, claves e estalos nos tempos do `events.json`, uma nota para cada peça que aparece |
| Barramento | baixo, teclas, cordas e sinos abaixam sob o bumbo (sidechain por seguidor de envelope); reverb por convolução, mandado por stem; passa-altas em 28 Hz; fade desde 31 s; normalização a −16 LUFS com pyloudnorm; limitador com antecipação e teto de −1,5 dBFS |
| Determinismo | com `np.random.default_rng(20261023)`, as mesmas amostras dão o mesmo `soundtrack.wav` byte a byte; cada nota vai para `audio/mix_log.json` |

**Com o assistente.** A Terkelsen Marimba chegou a ser avaliada e ficou de fora porque a licença não deixava clara a redistribuição; daí a dica do autor para esta etapa: pedir a licença de cada biblioteca antes de usá-la e um arquivo de créditos com as fontes fixadas. Tudo o que pesava ficou longe do notebook dele, na máquina Linux na nuvem do assistente: as amostras (cerca de 0,6–0,7 GB), o Python com numpy, scipy e pyloudnorm num venv do uv, o Node 20 e o ffmpeg.

## 7. A prova de que imagem e som batem

- A página publica a própria lista de eventos (`window.__events()`), e `scripts/dump_events.py` a grava em `data/events.json`, o mesmo arquivo que a partitura lê.
- `scripts/verify_sync.py` confere essa lista de três maneiras independentes:

| Conferência | Como | Resultado nos 113 eventos com tempo |
|---|---|---|
| Agenda | cada evento tem som no log da partitura no instante exato | 113/113; desvio máximo de 0,0 ms |
| mp4 contra wav | correlação cruzada do áudio | atraso de 0 amostra |
| Áudio | detecção de ataques no wav renderizado (fluxo de energia logarítmica com passa-altas), sem olhar a partitura | 72/113 a até um quadro (33 ms); mediana de 2,5 ms |
| Bateria | evento da grade que coincide com uma batida de bateria no mesmo instante | 86/113 |

- O que fica de fora em cada uma, pelo autor: no áudio, quase só tiques de digitação suaves e sinos baixos sob a bateria, que estão agendados mas escapam a um detector simples; na bateria, quase só eventos em trechos sem bateria (os 4 s iniciais e o respiro dos 12,5 s).
- Os números fracos vão publicados junto, porque mostram quais eventos se veem mais do que se ouvem.

## 8. Render: o navegador como câmera, com obturador

| Ponto | Fato |
|---|---|
| Script | `scripts/render.py` |
| Navegador | Chrome sem tela, pelo Playwright |
| WebGL | por software (SwiftShader); dispensa GPU |
| Flags | `--use-gl=angle`, `--use-angle=swiftshader`, `--ignore-gpu-blocklist`, `--enable-unsafe-swiftshader`, `--no-sandbox` |
| Cada worker | abre o HTML com `?render&w=1920&h=1080` e tira números de quadro de uma fila comum |
| Coordenação entre workers | nenhuma, porque o estado é f(t) |

No desfoque de movimento, que a própria página produz, o trabalho se concentra onde há movimento: no render final, 67 quadros se resolveram com uma captura só, e 17 foram até o teto de 8.

| Peça | Papel |
|---|---|
| Quantas capturas | regra: deslocamento de até 0,6 px fica em uma; acima disso, `ceil(pixels / 5)`, nunca mais de 8 |
| Quem mede o deslocamento | `window.__nSamples`, com dois sinais: pontos da cena levados à tela pela câmera no instante em que o obturador abre e no que fecha, e uma assinatura do resto que se mexe |
| A janela de exposição | 1/60 s, o tempo aberto de um obturador de 180° num filme de 30 fps |
| Quem compõe o quadro | `window.__shutter(t, n, open)`, que reparte `n` instantes pela janela em torno de `t`, desenha cada um e os soma num canvas 2D com `globalAlpha = 1/(k+1)`; a soma é uma média corrida, que sai em PNG por `toDataURL` |

| Ponto | Fato |
|---|---|
| ffmpeg, vídeo | `-framerate 30`, `libx264`, `-preset medium`, `-crf 16`, `-pix_fmt yuv420p`, `-profile:v high`, `-movflags +faststart` |
| ffmpeg, áudio | `-c:a aac`, `-b:a 256k`, `-shortest` |
| Passada completa | cerca de 36 min (2.139 s) |
| Máquina | 3 workers, 8 núcleos, 16 GB |
| Retomada | `--resume --keep` |

**Com o assistente.** O render foi uma tarefa longa em segundo plano na máquina do assistente; a pergunta "como vai?" devolvia a contagem de quadros a qualquer hora, e cada conserto refazia só a faixa de quadros atingida.

## 9. Reproduzir

| Ponto | Fato |
|---|---|
| Requisitos | Python 3.13, Node 20, ffmpeg, git, Google Chrome ou o Chromium do Playwright |
| Blender 5.x | só para refazer o `.glb`; uma cópia pronta está no repositório |
| GPU | dispensada |

0. Clonar o repositório, criar o venv, `pip install -r requirements.txt` (numpy, scipy, soundfile, pyloudnorm, playwright) e `npm install` (three.js, esbuild, fontes); para o Chromium do Playwright, `playwright install chromium` e `ARCHLANG_PROMO_CHANNEL=chromium`.
1. Opcional: refazer as entradas (compilar o `.arch`; rodar o Blender com o comando da seção 4).
2. O HTML ainda sem áudio (`python scripts/build.py --noaudio`) e a tabela de eventos (`python scripts/dump_events.py`).
3. A trilha: `bash scripts/fetch_samples.sh` e `python audio/score.py`.
4. A sincronia: `python scripts/verify_sync.py`.
5. O render: um teste de 5 quadros (`--frames 0:5 --workers 2`), depois o filme (`--workers 3 --audio dist/soundtrack.wav`).
6. `bash scripts/make_release_assets.sh`: o HTML com o áudio embutido e a pasta da release com `SHA256SUMS`.

- Rascunho rápido: `--w 1280 --h 720`.
- Para mudar o tempo: editar `K` em `src/comp.js`, refazer o build, rodar `dump_events.py` e de novo `score.py`; a música acompanha.

## 10. Armadilhas e lições

O autor põe duas regras na base do resto: a tabela de batidas se fecha antes da arte (a 120 BPM e 30 fps, a batida tem 15 quadros exatos e nunca cai entre dois), e a página não guarda estado, porque com tudo em f(t) o render paralelo, a retomada, a faixa refeita e o quadro parado saem sem custo extra.

| Ponto | Fato |
|---|---|
| WebGL por software | lento, mas portátil |
| Entre máquinas | os pixels podem variar um pouco |
| Quadros refeitos do repositório na máquina de build | 4 de 5 iguais bit a bit aos da release |
| O quinto | 117 de 2.073.600 pixels diferentes |
| Sonda de movimento do onetake | não enxerga dentro do canvas WebGL; não registrou movimento |
| Continuidade | conferida a olho, em quadros extraídos |
| Mixagem final em monitores de estúdio | ninguém ouviu |
| De onde vieram os níveis | medidas por stem e medidores de loudness |

As outras duas são de conduta: medir a sincronia e publicar também o número fraco, e dizer com todas as letras o que ficou sem verificar, como a audição em estúdio.

## 11. Como o autor tocou o projeto com o assistente

| Frente | O que aconteceu, pelo autor |
|---|---|
| Planejamento | ele descreveu o resultado (promo em uma tomada, cara de 3D, instrumentos reais, tudo reproduzível); o assistente pesquisou o Blender e as ferramentas e propôs o pipeline; o papel dele foi decidir, não digitar comando |
| Onde rodou | no computador Linux na nuvem do assistente, com Blender, Node, Python com uv, ffmpeg e as amostras, e lá também render, codificação e mixagem; o notebook Windows dele ficou livre |
| Tarefas longas | em segundo plano; à pergunta "进度如何了？", progresso concreto: peças ou quadros prontos, hora da última gravação, estimativa |
| O que saiu publicado | repositório público e release v1.0.0 (mp4, HTML, trilha, `SHA256SUMS.txt`), abertos com o git e o gh do próprio autor, a partir dos resultados levados à máquina dele |
| Permissão e git | nada entrou no Windows dele antes de ele liberar o acesso, e o `git push`, como os outros passos arriscados, esperou o ok dele; a configuração de git do autor tinha um erro, que o assistente apontou e contornou informando o autor certo commit a commit, sem tocar nela |
| Tamanho | dos 2,3 GB da pasta de trabalho, o projeto era cerca de 34 MB, e o grosso eram clones inteiros das bibliotecas de amostras e quadros intermediários; a conta veio quando ele perguntou, e a escolha do que copiar ficou com ele |
| A cópia para `D:\` | com teto de cerca de 12 MB por peça, levou horas e fechou conferida por sha256 e pela contagem de 6.230 arquivos dos dois lados, com os temporários apagados; foram 182 peças, uma de cada vez, e cada queda de conexão ou sono do notebook recomeçava da última peça boa |

Os conselhos dele para quem tentar, numa ordem que não é a do post: a aprovação fica com quem dirige nos passos sem volta (push, publicação, mudança na própria máquina). Do assistente se cobra prova (quadro parado num instante exato, relatório de sincronia com números, loudness, checksum do que se copia ou publica) e a lista do que não foi verificado, que aqui incluía a audição em estúdio e o determinismo do render entre máquinas. Na hora de pedir, vale mais descrever resultado e restrições que passos ("um plano contínuo, só instrumentos reais, licenças CC0, reproduzível do repositório" funcionou melhor que prescrever ferramentas), e cada correção vai em fala comum e com escopo: "conserta a aérea" virou os quadros 618–790, não o filme todo.

## Créditos e licenças, como o post os dá

| Item | Licença ou nota |
|---|---|
| Código do projeto | MIT |
| Bibliotecas de amostras | CC0 1.0 ou domínio público; baixadas em commits fixos e não redistribuídas |
| O que se redistribui do som | só a trilha mixada |
| three.js | MIT |
| Blender | GPL; só monta a geometria |
| Fontes | SIL OFL 1.1 |
| archlang | MIT |
| onetake | PolyForm Noncommercial 1.0.0; contribuiu só com o método |
| Detalhe completo | `CREDITS.md` do repositório (não aberto) |

## Citações

- "Every value (camera, focus, the height of each wall, the opacity of each label) is computed from t alone"
- "Blender does nothing else: no camera and no animation."
- "Only the method from onetake was followed. Its licence is PolyForm Noncommercial, so none of its code or assets went into the repository."

## Lacuna

O post não diz que modelo está por trás do Grok Bot, quanto tempo o projeto levou de ponta a ponta nem quanto custou (máquina na nuvem, uso do assistente). Não dá tempo de render com GPU, tempo por quadro com e sem subquadros, nem quantos subquadros tiveram os quadros fora dos 67 e dos 17 citados, e da máquina diz só 8 núcleos e 16 GB. Não diz com que versão do Blender o `.glb` do repositório foi feito (só pede "5.x" para refazê-lo) nem o tamanho dele, e não dá as amplitudes e frequências da flutuação e do "punch" nem a curva de cada chave da câmera. A audição em monitores de estúdio e o determinismo do render entre máquinas ficaram sem verificar, como o próprio autor declara.
