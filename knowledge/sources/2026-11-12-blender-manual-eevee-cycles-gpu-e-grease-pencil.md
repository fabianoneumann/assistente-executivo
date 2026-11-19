---
titulo: "Blender Manual: EEVEE, GPU Rendering (Cycles), Grease Pencil (Introduction) e Storyboarding App Template"
tipo: artigo
autor: "Blender Documentation Team (manual do Blender)"
url: "https://docs.blender.org/manual/en/latest/render/eevee/index.html"
publicado_em: 2026-11-12   # rodapé das quatro páginas: "Last updated on 2026-11-12"; manual 5.3 (latest), pelo <title> de cada página
capturado_em: 2026-11-12
licenca: "CC BY-SA 4.0 (rodapé de cada uma das quatro páginas: 'This page is licensed under a CC-BY-SA 4.0 Int. License'); o integral está na url"
areas: [generative-media]
tags: [blender, eevee, cycles, real-time-rendering, rendering, gpu, vram, denoising, grease-pencil, 2d-animation, storyboarding, video-editing]
---

# Blender: os dois motores de render, o render na GPU e o desenho 2D com o storyboard

Ficha, em tabelas, uma por página lida, na ordem do que cada uma ensina; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Quatro páginas do manual do Blender 5.3, baixadas com curl em 2026-11-12, lidas no texto extraído do HTML e conferidas no HTML para título, versão, data e licença. O sha256 é o do arquivo HTML baixado, inteiro (`fontes/` da rodada); sem captura na Wayback registrada no `licencas.json` da rodada.

- "EEVEE", https://docs.blender.org/manual/en/latest/render/eevee/index.html ((hash omitido)). É a página de entrada do capítulo: três parágrafos e o sumário das subpáginas. Lida inteira; nenhuma subpágina (ajustes de render, limitações, nós suportados) foi lida.
- "GPU Rendering" (Cycles), https://docs.blender.org/manual/en/latest/render/cycles/gpu_rendering.html ((hash omitido)). Lida inteira.
- "Introduction" (Grease Pencil), https://docs.blender.org/manual/en/latest/grease_pencil/introduction.html ((hash omitido)). Lida inteira.
- "Storyboarding App Template", https://docs.blender.org/manual/en/latest/video_editing/storyboarding/app_template.html ((hash omitido)). Lida inteira, na versão 5.3; o rótulo da rodada registra que a busca tinha trazido a mesma página na 5.2.

Licença CC BY-SA 4.0, que permite cópia: o integral não vem neste repositório e se lê na url do frontmatter, e a conferência lado a lado do item 2 do README desta pasta não se aplica.

## Em uma frase

O manual descreve o EEVEE como o motor rápido, por rasterização, que usa os mesmos materiais do Cycles; diz como ligar o Cycles na GPU de cada fabricante e o que falha nela (sobretudo memória); e apresenta o Grease Pencil como objeto de desenho 2D no espaço 3D, com um modelo de arquivo pronto para storyboard em que cada plano é uma cena e o editor de vídeo é a linha do tempo mestra.

## EEVEE (página de entrada)

| Ponto | O que a página diz |
|---|---|
| O que é | motor de render em tempo real do Blender, voltado para velocidade e interação, com materiais PBR |
| Onde serve | na janela 3D, de forma interativa, e também no render final de alta qualidade |
| Materiais | os mesmos nós de shader do Cycles, então cenas existentes renderizam nele; para quem usa Cycles, serve de prévia de material em tempo real |
| Como calcula | rasterização: acha que superfície a câmera vê e estima a luz nela por vários algoritmos, sem calcular cada raio |
| Ressalva | segue princípios PBR, mas não é perfeito; o Cycles sempre dá o resultado mais fiel à física, e por isso o EEVEE tem limitações (página própria, não lida) |
| Subpáginas listadas | ajustes de render (amostragem, caminhos de luz, raytracing, volumes, curvas, profundidade de campo, desfoque de movimento, filme, desempenho, Grease Pencil); ajustes de cena, de mundo e de objeto; materiais; luzes; sondas de luz (esfera, plano, volume); limitações; nós suportados |

## Cycles na GPU: como ligar e o que cada fabricante pede

| Ponto | O que a página diz |
|---|---|
| Por que usar | a GPU pode acelerar o render; em troca, tem menos memória para cenas complexas e trava a interação quando a mesma placa desenha a tela e renderiza |
| Como ligar | escolher o back-end (CUDA, OptiX, HIP, oneAPI ou Metal) nas preferências de dispositivo do Cycles; marcar os dispositivos; em cada cena, pôr o dispositivo em GPU Compute |
| CUDA (NVIDIA) | Windows e Linux; capacidade de cálculo 5.0 ou mais |
| OptiX (NVIDIA) | Windows e Linux; capacidade 5.0 ou mais e driver 575 ou mais; usa a aceleração de raytracing das placas RTX |
| Denoise na GPU (NVIDIA) | OpenImageDenoise acelerado a partir da capacidade 7.0, o que inclui todas as RTX |
| HIP (AMD) | Windows e Linux; arquitetura RDNA1 ou mais nova, placa dedicada ou APU; séries RX 5000, RX 6000 e Pro W6000, RX 7000 e Pro W7000, RX 9000 |
| Drivers AMD mínimos | Windows: Radeon Software 24.9.1 ou Radeon PRO 24.Q4; Linux: Radeon Software 24.30 ou ROCm HIP Runtime 6.3 |
| Extras AMD | raytracing por hardware nas RX 6000 e mais novas, com driver recente, ligado nas preferências; denoise na GPU em placa dedicada RX 6000+ no Linux e RX 7000+ no Windows |
| oneAPI (Intel) | Windows e Linux; Arc de arquitetura Xe HPG (séries A e B); raytracing e denoise por hardware; denoise na GPU em todas as suportadas |
| Drivers Intel mínimos | Windows: Intel Graphics Driver XX.X.101.5518; Linux: intel-level-zero-gpu 1.3.27642 (em geral pelo intel-compute-runtime XX.XX.34666.3) |
| Metal (Apple) | Apple Silicon; macOS 13.0 ou mais para todos os recursos; raytracing e denoise na GPU |
| DLSS (NVIDIA) | Ray Reconstruction só para limpar o ruído da janela 3D, com CUDA ou OptiX: build do Blender com DLSS, capacidade 7.5 ou mais, driver 590 ou mais, e o driver precisa declarar suporte; não vale para o render final |
| Limites | Path Guiding em nenhuma GPU; Open Shading Language só no OptiX, com restrições; cáusticas de sombra não funcionam no HIP sem raytracing por hardware |

## Cycles na GPU: perguntas frequentes e erros

| Situação | O que a página diz |
|---|---|
| Blender trava durante o render | em GPU antiga, a placa ou renderiza ou desenha a interface; em GPU nova, cena pesada ainda pode travar; a solução completa é uma GPU para render e outra para a tela |
| Renderiza na CPU e não na GPU | a causa mais comum é falta de memória na placa, que só usa a dela, em geral bem menor que a do sistema; com CUDA, OptiX, HIP e Metal, se a memória da GPU enche, o Blender tenta usar a do sistema, mais devagar, mas em geral ainda mais rápido que a CPU |
| Várias GPUs | sim, em Preferences ‣ System ‣ Compute Device |
| Memória somada entre GPUs | em geral não; a exceção são placas NVIDIA ligadas por NVLink, com Distributed Memory Across Devices nas preferências, com pequena perda de desempenho |
| O que é mais rápido | depende do hardware e da cena; a página manda ao Blender Open Data |
| Antes de tudo | instalar o driver oficial do fabricante da GPU (ou do gerenciador de pacotes no Linux); o do fabricante do computador pode estar velho ou incompleto |
| Out of memory | a cena não cabe na memória da GPU; textura menor reduz: 8k, 4k, 2k e 1k ocupam 256 MB, 64 MB, 16 MB e 4 MB |
| Driver da NVIDIA perde a conexão com o de vídeo | no Windows, a GPU que também desenha a tela tem limite de tempo de cálculo; diminuir o Tile Size no painel de desempenho pode aliviar; a solução real são placas separadas; aumentar o tempo-limite deixa a interface mais lenta |
| Unsupported GNU version (Linux) | usar um GCC compatível pela variável `CYCLES_CUDA_EXTRA_CFLAGS="-ccbin gcc-x.x"` ao abrir o Blender, ou apagar a linha de checagem em `/usr/local/cuda/include/host_config.h` |
| Kernel compilation failed | placa NVIDIA nova que a versão do Blender e do CUDA não conhece; ver se a versão mais recente do Blender a suporta, ou, para quem compila o Blender, instalar um toolkit CUDA mais novo; normalmente não se instala o toolkit, porque o Blender vem com os kernels prontos |

## Grease Pencil (introdução)

| Ponto | O que a página diz |
|---|---|
| O que é | um objeto do Blender que recebe o desenho do mouse ou da caneta com pressão e o põe no espaço 3D como pontos, que formam um traço |
| Para que serve | animação 2D tradicional, animação de recorte (*cut-out*), motion graphics, storyboard, entre outros |
| Fluxo | o traço nasce no Draw Mode, que exige um quadro-chave novo na linha do tempo; depois se ajusta no Edit Mode e no Sculpt Mode; por fim recebe materiais, modificadores, luz e efeitos |
| Começo rápido | Object Mode ‣ Add ‣ Grease Pencil ‣ Blank; criar quadro-chave ou ligar o Auto Key; passar ao Draw Mode; clicar e arrastar na janela |
| Modelo 2D Animation | File ‣ New ‣ 2D Animation: espaço de trabalho 2D Animation ativo; fundo do mundo branco; vista de gerenciamento de cor Standard; plano de desenho Front (X-Z); camadas Line e Fill com materiais de traço prontos; a linha do tempo cria quadro-chave sozinha ao desenhar em quadro vazio |
| Caneta | o Grease Pencil lê a pressão da mesa digitalizadora ou da caneta |

## Modelo de storyboard (Storyboarding App Template)

| Ponto | O que a página diz |
|---|---|
| O que é | um arquivo-modelo pronto para storyboard, que junta desenho 2D e gestão de cenas num espaço de trabalho |
| Base | o modelo 2D Animation, mais o Video Sequence Editor (VSE) configurado com Sync Scene |
| Plano como cena | cada plano é uma cena própria, com desenho de Grease Pencil, ajustes de câmera e tempo independentes; o Sequencer é a linha do tempo mestra |
| Sync Scene | ao selecionar uma faixa no Sequencer, a cena correspondente aparece, para saltar entre planos durante a edição |
| Cenas prontas | Edit (a mestra, onde se montam os planos); Shot.000, um Scene Asset que serve de molde para planos novos; Shot.001 e Shot.002, exemplos feitos do molde |
| Durações padrão | a cena Edit tem 10 s; cada plano tem 2 s, para ver o ritmo no Sequencer; os intervalos de quadros são mais curtos que o padrão comum (por exemplo, 250 quadros), para navegar melhor na linha do tempo |
| Uso | File → New → Storyboarding; organizar os planos no Sequencer da cena Edit; duplicar o Shot.000 no Sequencer para criar planos; desenhar no espaço 2D de cada plano; mudar tempo e ordem no Sequencer |

## O que a fonte recomenda

Para render, o manual põe o EEVEE como o motor de velocidade e de prévia e deixa ao Cycles a fidelidade física; quem vai ao Cycles na GPU precisa checar back-end, geração da placa e versão do driver, e o limite que mais aparece é a memória da placa, que se contorna com textura menor e, no Windows, separando a placa da tela da placa do render. Para o desenho, o caminho é o Grease Pencil a partir do modelo 2D Animation, e para o storyboard, o modelo próprio, em que cada plano é uma cena de 2 s montada no Sequencer.

## Citações

- "EEVEE is based on rasterization and is not a path tracer."
- "Typically, no, each GPU can only access its own memory."
- "Each shot scene is set to 2 seconds by default"

## Lacuna

Nenhuma das quatro páginas dá tempo de render, compara EEVEE e Cycles em velocidade, nem diz quanto de memória de vídeo cada um pede; a do EEVEE não diz se ele roda sem janela (`-b`) nem quais são as limitações, que ficam numa subpágina não lida. A do Cycles não traz tabela de desempenho por placa (manda ao Blender Open Data) e não diz se o oneAPI também usa a memória do sistema quando a da GPU enche. As do Grease Pencil e do storyboard não falam de exportar o storyboard como vídeo ou imagens, nem de desenhar por script.
