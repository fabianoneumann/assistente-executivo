---
titulo: "Headless 3D rendering: Blender, Three.js, Unreal and vork, with the commands"
tipo: artigo
autor: "Ravi Parikh"   # assinatura na página ("Co-founder, Voyager") e meta article:author
url: "https://voyager.so/blog/headless-3d-rendering"
publicado_em: 2026-11-06   # meta article:published_time (2026-11-06T14:26:33-08:00); a página mostra "Updated Nov 7, 2026" (article:modified_time 2026-11-07)
capturado_em: 2026-11-11
licenca: "protegido (rodapé: '© 2026 Voyager'); sem licença de conteúdo declarada no texto lido; ficha em palavras próprias e em estrutura própria, sem o integral"
areas: [generative-media]
tags: [headless-rendering, threejs, blender, unreal-engine, vork, gpu, chromium, playwright, video-as-code]
---

# Voyager: render 3D sem janela, com os comandos e os tempos de uma máquina

Nota de fato: tabelas de números, comandos, requisitos e licenças, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: o artigo é protegido.

**Proveniência.** Artigo de Ravi Parikh, cofundador da Voyager, no blog da empresa, https://voyager.so/blog/headless-3d-rendering, baixado com curl (HTML) em 2026-11-11, com o texto extraído do HTML; sha256 (hash omitido); sem captura na Wayback. Título conferido no HTML: o cabeçalho da página é o do campo `titulo`, e o `og:title` é a forma curta "Headless 3D rendering: Blender, Three.js, Unreal, vork". Publicado em 2026-11-06 (meta `article:published_time`), com a página dizendo "Updated Nov 7, 2026". Lido o texto inteiro do artigo, inclusive as perguntas frequentes e o rodapé, que promove o produto da Voyager (um agente de desktop para trabalho criativo). Nenhum dos links (o README do vork, as documentações, o post da Voyager sobre o Godot) foi aberto.

Condensada em nota de fato em 2026-11-11, depois de três reescritas em prosa que seguiam a fonte.

**Conferência lado a lado** (2026-11-11, na condensação, pela régua de 2026-11-11 do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (número, nome, comando, flag, valor ou rótulo curto) fica fora, como as marcas "—" e "não informado". Corpo: 6 frases de prosa (uma em "Em uma frase", três em "O que a fonte recomenda", duas na lacuna) e 518 células de dados em 16 tabelas, 39 delas marcas e 479 de fato. As 23 células que trazem verbo foram lidas uma a uma contra a fonte: cada uma guarda um fato só, sem frase inteira da fonte nem junção de duas. As três frases da recomendação juntam ideias de dois a quatro lugares do artigo, em outra ordem e outras palavras. Resultado: 0 das 6 unidades seguem a fonte; as três citações literais estão à parte, em "Citações". A versão anterior, pela mesma régua, dava 38 a 49 de 53 (re-revisão do Passo 7).

## Em uma frase

Texto de fabricante (a Voyager faz o vork, um dos motores comparados) que põe lado a lado as rotas de render 3D por linha de comando, com tempos medidos em três delas; para a base, é a consulta de flags, exigências de GPU, tempos e licenças antes de escolher onde renderizar a parte 3D de um vídeo feito em código.

## O teste

| Item | Valor |
|---|---|
| Máquina | Apple M5 Max |
| Data da medida | 06/11/2026 |
| Executados | Blender 5.2.1 (EEVEE e Cycles), Three.js r187 com Playwright 1.65, vork 0.1.0 |
| Só pela documentação, no mesmo dia | Unreal (página da 5.8), Godot, Babylon.js, Bevy |
| Godot executado antes | 4.7.2, num post anterior da Voyager |
| Resolução | 640×480 |
| Ajustes | padrões de cada motor |
| Exceção | Three.js com luz de preenchimento e tone mapping AgX |
| Aparência igualada entre os motores | não |
| Dentro do tempo medido | inicialização do programa e gravação do arquivo |
| Execuções por faixa de tempo | não informado |
| Ferramenta de cronometragem | não informada |
| Maior tempo aquecido entre as quatro rotas | cerca de 4 s ou menos |
| Rápidas o bastante para laço de agente | as quatro, para o artigo |
| Usos de render sem janela (perguntas frequentes) | servidor; pipeline em lote; agente de IA |

## A cena, por motor (valores do código do artigo)

| Peça | Blender | Three.js | vork |
|---|---|---|---|
| Ponto de partida | configurações de fábrica, vazias | página vazia no Chromium do Playwright | JSON, versão 2 |
| Biblioteca | — | `three` servido de `node_modules` por interceptação de requisições | — |
| Esfera | UV, raio 1, 32 segmentos × 16 anéis | `SphereGeometry`, raio 1, 64 × 32 | `std` sphere, raio 1 |
| Sombreamento da esfera | suave | — | — |
| Cor da esfera | (0.12, 0.35, 0.65) | (0.12, 0.35, 0.65) | (0.12, 0.35, 0.65) |
| Rugosidade da esfera | 0,3 | 0,3 | 0,3 |
| Chão | plano de lado 10 em z = −1 | `PlaneGeometry` 10 × 10 em y = −1 | `grid` 10 × 10 em y = −1 |
| Cor do chão | (0.35, 0.35, 0.35) | (0.35, 0.35, 0.35) | (0.35, 0.35, 0.35) |
| Material | Principled BSDF | `MeshStandardMaterial` | `base_color`, `specular_roughness` |
| Luz principal | área | `DirectionalLight` | `rectangle` |
| Tamanho da luz | 4 | — | 4 |
| Força da luz | energia 700 | intensidade 4 | energia 700 |
| Cor da luz | (1, 0.92, 0.8) | (1, 0.92, 0.8) | (1, 0.92, 0.8) |
| Posição da luz | (−3, −4, 5) | (−3, 5, 4) | (−3, 5, 4) |
| Sombra | do motor | shadow map ligado | do motor |
| Preenchimento | — | `HemisphereLight` 0,5 | — |
| Câmera | (3, −5, 2) | perspectiva de 30,3°, em (3, 2, 5) | (3, 2, 5) |
| Alvo da câmera | origem | origem | origem |
| Tone mapping | padrão | AgX | padrão |
| Opções do render | — | `antialias`, `preserveDrawingBuffer` | — |
| GPU | Cycles: `METAL` (OPTIX ou CUDA na NVIDIA) | `--use-angle=metal --enable-gpu --ignore-gpu-blocklist` | — |
| Dispositivos no Cycles | todos menos CPU | — | — |
| Saída | render com `write_still` | `toDataURL`, PNG gravado pelo Node | `vork render` |
| Fim do programa | — | `browser.close()` | — |
| Animação | — | — | esfera de (0, 0, 0) a (2, 0, 0), linear, chaves 0 e 2 |
| Unidade das chaves | — | — | não informada |

## Tempos (06/11/2026, M5 Max, 640×480)

| Rota | Versão | Amostras | Preparo antes do 1º render | 1º render | Aquecido |
|---|---|---|---|---|---|
| vork `std/final` | 0.1.0 | 8, com denoise | instalador, com 86 s de shaders | 5,2 s | 0,42 a 0,44 s |
| Blender EEVEE | 5.2.1 | 64 | já instalado | 2,0 s | 0,81 a 0,85 s |
| Blender Cycles no Metal | 5.2.1 | adaptativo, com denoise | já instalado | 3,9 s | 2,2 a 4,0 s |
| Three.js no Chromium headless | r187 | — | `npm i three playwright` + download do navegador | 1,9 s | 0,34 a 0,6 s |

| Rota | Sombra | Fundo | Outro |
|---|---|---|---|
| vork | suave | cinza padrão | imagem lisa |
| Blender EEVEE | grão visível na borda | preto (sem mundo definido) | forma correta |
| Blender Cycles | a mais limpa das quatro | — | — |
| Three.js | borda dura, de shadow map de luz direcional | — | `RectAreaLight` sem suporte a sombra |

| Clipe do vork | Valor |
|---|---|
| Quadros | 48 (`--frame-start 0 --frame-end 47`) |
| Primeira vez | 7,2 s |
| Aquecido | 1,8 s |
| Codificação no Mac | VideoToolbox, MP4 direto |
| MP4 no Linux | precisa do ffmpeg para o mux |

| Do README do vork, citado no artigo | Valor |
|---|---|
| Preparo nas máquinas NVIDIA do projeto | 2,5 a 4,5 min |
| Preparo em geral | alguns minutos |
| Primeira cena com programas novos | compila por minutos, sem saída |
| Durante a compilação | não matar o processo |
| Tempo limite | não curto |
| Ganho sobre o EEVEE guardado | 1,15 a 1,90× |
| Onde o ganho foi medido | NVIDIA L4 |
| Casos do ganho | imagens finais padrão em 1080p; resultados completos |
| Amostras na comparação | 8 com denoise (vork) × 64 (EEVEE) |
| Qualidade igual no ganho | não |
| Path tracer do vork contra o Cycles | 2 a 5,8× mais lento |
| Casos dessa medida | dois, nomeados no README |
| Comparação em path tracing favoreceria o vork | não, admite o artigo |
| Custo do Cycles: mais tempo pela melhor imagem | troca usual de path tracer, para o artigo |
| Tomada de vitrine com compute em Slang | um milhão de pássaros |
| Ponto de partida de um agente do zero | algo básico |
| Tomadas de vitrine | muito mais direção |

## Que falta cada rota aguenta

| Rota | Sem janela | Sem servidor de display (Linux sem X11 nem Wayland) | Sem GPU |
|---|---|---|---|
| Blender EEVEE | sim, com `-b` | caminho headless no Linux desde a 3.4 | não: pede contexto de GPU |
| Blender Cycles | sim, com `-b` | não informado | sim, na CPU, devagar |
| Three.js | sim, no Chromium headless | não informado | com render por software (SwiftShader; `swangle`) |
| Unreal 5.8 | a documentação usa `-windowed` | a documentação não diz | a documentação não diz |
| vork 0.1.0 | sim, por projeto | não informado | não |
| Godot `--headless` | — | sim | sim |
| Bevy | sim (exemplo oficial grava imagem) | não informado | não informado |
| Mitsuba 3 | sim | não informado | backend de CPU |

| Requisito de hardware do vork 0.1.0 | Valor |
|---|---|
| NVIDIA | recente, com ray tracing por hardware |
| Sistemas com NVIDIA | Linux, Windows |
| Apple | Apple Silicon com Metal |
| Alvo do Slang empacotado | macOS 26 |
| macOS anteriores | não qualificados |
| AMD | não suportado |
| Intel | não suportado |
| CPU | não suportado |
| Vulkan por software | não suportado (notas de instalação) |
| Qualificação da plataforma pelos tempos do M5 Max | não |

| Modo headless que não dá imagem | Fato |
|---|---|
| Godot `--headless`, documentação | guia de servidor dedicado |
| Máquina-alvo do Godot `--headless` | sem GPU nem display |
| Uso do Godot `--headless` | lógica de jogo |
| `--write-movie` no Godot 4.7.2 | precisou de tela |
| Saída útil com `--headless` | nenhuma |
| Babylon.js `NullEngine` | não renderiza (guia de servidor do Babylon) |
| Uso do `NullEngine` | testes, lógica de servidor, carregadores |

## Comandos

| Rota | Comando que o artigo dá |
|---|---|
| Blender, manual da 5.2 | `blender -b file.blend -f 10` |
| Blender, manual da 5.2 | `blender -b file.blend -E CYCLES -s 10 -e 500 -a` |
| Blender 5.2.1, sem `.blend` | `blender --background --factory-startup --python scene.py -- BLENDER_EEVEE $PWD/eevee.png` |
| Blender 5.2.1, Cycles | o mesmo, com `CYCLES $PWD/cycles.png` |
| Three.js | `npm i three playwright && npx playwright install chromium` |
| Unreal 5.8 | `UnrealEditor-Cmd.exe <projeto .uproject> <mapa> -game -MoviePipelineConfig=<asset da fila> -windowed -resx=<largura> -resy=<altura> -log -notexturestreaming` |
| vork, prévia | `vork render shot.json --profile std/previs --out preview.png` |
| vork, final | `vork render shot.json --profile std/final --out final.png` |
| vork, clipe | `vork render shot.json --profile std/final --frame-start 0 --frame-end 47 --out clip.mp4` |

| Rota | Ponto de atenção | Fato |
|---|---|---|
| Blender | `-b` | sem interface |
| Blender | `-f` / `-a` | renderiza quadro / animação |
| Blender | ordem dos argumentos | vale a sequência dada |
| Blender | posição do arquivo | antes da flag de render |
| Blender | caixa das flags | `-F` ≠ `-f` |
| Blender | automação | script Python no lugar de `.blend` |
| Blender | `bpy.ops` em segundo plano | muitos falham |
| Blender | causa da falha | operador pede contexto de interface |
| Blender | contorno | API de dados |
| Blender | EEVEE no Linux | testar antes |
| Blender | onde testar o EEVEE | no próprio contêiner |
| Blender | prazo do teste | antes de fechar a imagem Docker |
| Blender | referência | relato no rastreador do Blender |
| Three.js | render por linha de comando oficial | não há |
| Three.js | flags de GL do teste | de Mac |
| Three.js | no Linux | outro backend |
| Three.js | `--gl=angle` (guia do Remotion) | desktop |
| Three.js | `--gl=angle-egl` | nuvem com GPU |
| Three.js | `--gl=swangle` | sem GPU |
| Three.js | velocidade do `swangle` | possivelmente lenta |
| Three.js | `angle` | vazamento de memória |
| Three.js | render longo | partir em pedaços |
| Three.js | MP4 | nada no caminho grava |
| Three.js | tempo do vídeo | controlado pelo código |
| Three.js | por quadro | avançar, capturar, codificar |
| Unreal | rota | Movie Render Queue |
| Unreal | formato do vídeo | não informado |
| Unreal | assets | binários |
| Unreal | fila e nível | feitos antes de rodar |
| Unreal | onde fazê-los | editor ou API Python |
| Unreal | extra da 5.8 | servidor MCP próprio, experimental |
| vork | API | muda rápido |
| vork | conferência | `vork help` da versão instalada |
| vork | linguagem | Rust e Slang |
| vork | render | Vulkan e Metal |
| vork | editor | nenhum |
| vork | cena | arquivo JSON |
| vork | geração da cena | SDK em Python ou TypeScript |
| vork | programas de compute | Slang, dentro da cena |
| vork 0.1.0 | neblina | ignorada |
| vork 0.1.0 | volumes participantes | ignorados |
| vork | cena grande | pode falhar |
| vork | transparência densa | pode falhar |
| vork | falhas no Mac | também |
| vork | baixar a resolução | não resolve necessariamente |

## Licenças e indicações

| Ferramenta | Licença | Custo |
|---|---|---|
| Blender | GPL | não informado |
| Cycles | Apache 2.0 | não informado |
| Three.js | MIT | não informado |
| Unreal | não informada | pago acima de um limiar (abaixo) |
| vork | vork Preview License, código-fonte disponível | grátis na prévia de pesquisa, inclusive comercial |

| vork Preview License | Fato |
|---|---|
| Código aberto | não |
| Modificar para uso próprio | pode |
| Redistribuir as mudanças | não, sem permissão |
| Serviço de render hospedado | não, sem permissão |
| Versões futuras | podem ter outros termos |

| Indicação (tabela de escolha do artigo) | Rota |
|---|---|
| `.blend` pronto, render em servidor | Blender com Cycles |
| mesma cena no site e no servidor | Three.js |
| cinemática de projeto Unreal | Unreal Movie Render Queue |
| agente que escreve a tomada do zero | vork |
| shader próprio ou simulação | vork |
| condição do vork | hardware e tomada dentro dos limites |
| neblina, fumaça, volumes | Blender |
| só CPU | Blender Cycles; Three.js com GL por software |
| pesquisa de transporte de luz | Mitsuba 3 |

| Outros motores | Fato |
|---|---|
| Bevy, para quem | já escreve Rust |
| Bevy, render sem janela | exemplo oficial |
| Bevy, aviso do README | faltam recursos importantes |
| Bevy, quebra de API | a cada três meses, mais ou menos |
| Cycles avulso | compila sem o Blender |
| Cycles avulso, cena | XML |
| Mitsuba 3, linguagem | Python primeiro |
| Mitsuba 3, uso | render inverso, transporte de luz |
| Mitsuba 3, fora do uso | entrega com prazo |
| Three.js, visual | de tempo real |
| Unreal, montagem | a mais pesada do artigo |
| Blender, hardware | roda em muito mais máquinas que o vork |
| Unreal, quem paga | empresa que não faz jogo |
| Unreal, limiar | US$ 1 milhão de receita anual |
| Unreal, termos lidos em | 23/10/2026 |

| Imagem do artigo | Assets | Créditos | Vídeo gerativo |
|---|---|---|---|
| Bolo de cenoura, render do vork | CC0 do Poly Haven | foto de Greg Zaal; tratamento de James Ray Cock | — |
| Filmagem com 3D do vork | filmagem de Ron Lach (Pexels), modificada sob a licença da Pexels | — | nenhum |

## O que a fonte recomenda

O ponto de partida é o inventário da máquina (tem tela? tem servidor de display? tem placa?), e os modos de servidor do Godot e do Babylon ficam fora quando o objetivo é imagem. Com cena pequena, o relógio não escolhe: o que escolhe é o ponto de partida (texto escrito por agente, código do site, arquivo do Blender, projeto Unreal) e o que a máquina tem de placa, com o Blender de reserva quando só há CPU ou a tomada pede volume. Para vídeo, nenhuma rota vem pronta do mesmo jeito: o vork grava o MP4 sozinho, mas só nas placas que aceita, e no Three.js cabe ao código avançar e capturar cada quadro, com as flags de GL trocadas conforme o sistema.

## Citações

- "vork is made by Voyager, so read its section with that in mind."
- "The looks were not matched and this is not a benchmark."
- "Times are the whole command, including startup and writing the file."

## Lacuna

O artigo não mede o Unreal, não diz quantas execuções aquecidas entram em cada faixa nem com que ferramenta o tempo foi tomado, e não dá tempo para o Three.js em render por software nem em Linux. Não diz o formato de saída do Movie Render Queue, se o vork ou o Three.js rodam sem servidor de display, nem a unidade das chaves da animação do vork.
