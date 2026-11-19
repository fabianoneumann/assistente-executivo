---
titulo: "System requirements for Unity 6.6"
tipo: artigo
autor: "Unity Technologies (manual oficial da Unity 6.6)"   # a página não tem assinatura de pessoa; o rodapé diz 'Copyright © 2026 Unity Technologies'
url: "https://docs.unity.com/en-us/engine/6000.6/manual/get-started/install-and-upgrade/getting-started-installing-unity/system-requirements"
publicado_em: null   # a página diz "Last updated 14 days ago" quando lida em 13/11/2026; o HTML traz lastModifiedDate 2026-10-30T03:58:37+00:00
capturado_em: 2026-11-13
licenca: "protegido (rodapé: 'Copyright © 2026 Unity Technologies'; sem licença de conteúdo declarada no texto lido); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unity, hardware, technical-requirements, gpu, ram, system-requirements]
---

# Unity 6.6: o que o Editor e o Player pedem de máquina e de sistema

Nota de fato: tabelas do que a página de requisitos da Unity 6.6 lista, uma seção por parte da página, na ordem dela, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida. É página técnica que lista fatos (sistema, processador, API gráfica, memória por plataforma), então segue a ordem da fonte (o `README.md` desta pasta, item 2, a exceção da página técnica); a medida da cópia é a do `parafrase.py` e a da conta lado a lado.

**Proveniência.** Página do manual da Unity 6.6 (6000.6), baixada com `curl` em 13/11/2026 e lida no texto do bloco `<article>` (2.047 palavras, do caminho de navegação ao rodapé), conferido no HTML; sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco, não do arquivo HTML); Wayback http://web.archive.org/web/20261107012036/https://docs.unity.com/en-us/engine/6000.6/manual/get-started/install-and-upgrade/getting-started-installing-unity/system-requirements. Título conferido no `<title>`: "System requirements for Unity 6.6", seguido de "Install Unity", "6000.6" e "Unity Editor". Lida a página inteira; as páginas ligadas (consoles, OpenXR, ARCore, as notas do Hub) não foram abertas.

**Conferência lado a lado** (2026-11-13, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra `unity-66-requisitos.txt` (o texto do bloco, na cópia de trabalho), com 40 unidades medidas (15 de prosa, 25 de célula com texto), 5 coladas, que são nomes de API gráfica, de driver e de sistema em inglês, fatos sem outra grafia, e 0 trechos de 3 ou mais seguidas. Na leitura lado a lado, segue a fonte a unidade que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela, e conta como unidade que segue a fonte a célula que o script partiu em pedaços da mesma frase: 28 de 32 unidades do corpo (de "Em uma frase" em diante), 28 de 40 com as 8 do cabeçalho de proveniência, que não tratam do conteúdo. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 27, do Editor aos sistemas embarcados: a página é técnica e lista fatos, e a ficha segue a ordem dela pela exceção do item 2; não há texto argumentativo do autor na página.

## Em uma frase

A Unity 6.6 não dá placa de vídeo mínima nem tamanho de instalação: para o Editor no Windows, pede Windows 10 21H1 ou mais novo, processador x64 com SSE2 (ou Arm64), placa que rode DirectX 10, 11, 12 ou Vulkan com driver oficial e, como mínimo recomendado, 8 GB de RAM, mais para projeto grande.

## O Editor

| Item | Fato |
|---|---|
| Ressalva geral | o desempenho e a qualidade do render variam com a complexidade do projeto |
| Máquina | estação de trabalho ou notebook, sem emulação, contêiner ou camada de compatibilidade |

| Sistema | Versão | Processador | API gráfica | Outros requisitos |
|---|---|---|---|---|
| Windows | 10 versão 21H1 (build 19043) ou mais novo (x64); 11 21H2 (build 22000) ou mais novo (Arm64) | x64 com SSE2, ou Arm64 | placas com DX10, DX11, DX12 ou Vulkan | driver oficial do fabricante |
| macOS | Ventura 13 ou mais novo | Intel x64 com SSE2 (em descontinuação); Apple M1 ou superior | placas Intel e AMD com Metal | driver oficial da Apple (Intel) |
| Linux | Ubuntu 22.04 e 24.04 | x64 com SSE2 | OpenGL 3.2 ou mais, ou Vulkan; placas Nvidia e AMD | Gnome sobre X11 ou Wayland; driver proprietário da Nvidia ou Mesa da AMD |

| Item | Fato |
|---|---|
| Apple silicon | o lightmapper Progressive CPU (em descontinuação) e o Realtime Global Illumination pedem o Rosetta 2; sem ele, o Unity Compute Light Baker no lugar do Progressive CPU |
| Wayland no Ubuntu 22.04 | com placa AMD |
| Wayland no Ubuntu 24.04 | com AMD, ou com Nvidia no driver proprietário 550 ou mais novo |
| RAM | mínimo recomendado de 8 GB no Windows, no macOS e no Linux |
| RAM por projeto | depende do tamanho e da complexidade; projeto maior pede mais |
| Disco | ao gerar um build, o Editor lê e grava muitos arquivos pequenos; a página recomenda disco com IOPS alto |

## Limites do Editor por plataforma

| Plataforma | Limite |
|---|---|
| Windows on Arm | baixar e instalar o Editor pelo Hub só a partir da versão v3.7.0 Beta 1 do Hub (canal Beta nas preferências) |
| Windows on Arm, plataformas e pacotes | sem suporte às plataformas sem SDK nativo Arm64 nem aos pacotes com binário de terceiro sem suporte a Arm; podem funcionar com emulação x86 |
| Windows on Arm, Vulkan | sem suporte |
| macOS | janelas secundárias do Editor só maximizam, sem tela cheia |
| Linux, vídeo | importação só em VP8 |
| Linux, arquivos | sistema de arquivos diferencia maiúsculas |
| Linux, erro `Pipe error !` | subir o limite de arquivos abertos (`ulimit -n 4096`) antes de abrir o Editor |
| Linux, Wayland | experimental; o Player usa Wayland nativo com `-force-wayland` |

## O Player (o que se publica)

| Plataforma | Sistema | Processador | API gráfica | Outros |
|---|---|---|---|---|
| Android | 8.0 (API 26) ou mais novo; versão personalizada com as APIs padrão do Google | ARMv7 com Neon (32 bits) ou ARM64 | OpenGL ES 3.1 ou mais, Vulkan | 1 GB de RAM ou mais; aparelho de mão, televisão ou tablet pela definição de compatibilidade do Android 9.0; sem contêiner nem emulador; para desenvolver, Android SDK 16 (API 36), NDK r27c e OpenJDK 17, que o Hub instala |
| iOS e iPadOS | 15 ou mais novo | A8 ou superior | Metal | Xcode 16 ou mais novo |
| tvOS | 15 ou mais novo | A8 ou superior | Metal | Xcode 16 ou mais novo; Apple TV HD ou mais nova |
| Windows | 10 versão 21H1 (build 19043) ou mais novo | x86 ou x64 com SSE2, Arm64 | DX10, DX11, DX12 ou Vulkan | driver oficial; o backend IL2CPP pede Visual Studio 2019 com C++ e Windows SDK 10.0.19041.0 ou mais novo |
| Universal Windows Platform | Windows 10 21H1 ou mais novo, Xbox One, Xbox Series X e S | x86 ou x64 com SSE2, Arm64 | DX10, DX11 ou DX12 | driver oficial; Visual Studio 2019 com C++ e Windows SDK 10.0.19041.0 |
| macOS | Monterey 12 ou mais novo | Apple silicon; x64 com SSE2 (em descontinuação) | Metal, placas Intel e AMD | driver oficial da Apple; o IL2CPP pede Xcode |
| Linux | Ubuntu 22.04 e 24.04 | x64 com SSE2 (só 64 bits) | OpenGL 3.2 ou mais, Vulkan | Gnome sobre X11 ou Wayland; Nvidia com driver proprietário ou AMD com Mesa |
| Servidor (Windows, macOS, Linux) | as mesmas versões, em estação de trabalho ou rack, sem emulação | x86, x64, Arm64 (Apple silicon no macOS) | sem suporte explícito a placa de vídeo | driver oficial |
| Web | Chrome, Firefox, Safari ou Edge (Chromium) com WebGL 2.0, HTML 5, 64 bits e WebAssembly, no Windows, no macOS e no Linux | — | — | no Android e no iOS: Safari do iOS 15 ou mais novo, Chrome 58 ou mais novo; Safari 18.2 ou mais novo para mais memória |

**Consoles:** PlayStation 4 e 5 (com os PS VR), Xbox One, Xbox Series X e S, Nintendo Switch e Switch 2 têm requisitos na página de desenvolvimento para consoles; o build para console só sai da Unity no Windows (Windows 10 Pro 64 bits em inglês ou japonês para os dois Switch; Windows 10 64 bits, versão 1709 ou mais nova, para os Xbox; Windows 10 Pro 64 bits 22H2 para os PlayStation).

## XR e sistemas embarcados

| Plataforma | Fato |
|---|---|
| Meta Quest 1 | software da Quest versão 50 ou anterior |
| Meta Quest 2, Pro, 3 | software da Quest 39, 46 e 59 ou mais novo |
| Meta Rift e Rift S | Windows 10 ou mais novo, DX11; processador e placa pelas especificações recomendadas da Oculus |
| OpenXR | a lista de runtimes na documentação do plugin OpenXR |
| Google ARCore | aparelhos da lista do ARCore; ARM 32 e 64 bits; OpenGL ES 3.1 ou mais; SDK até o ARCore 1.24 |
| Apple visionOS | visionOS 2.0; Metal ou RealityKit; Xcode 16 Beta 6; Editor do macOS para Apple silicon (o de Intel não desenvolve para visionOS); realidade virtual, mista e híbrida pedem o Unity PolySpatial; o projeto do Xcode sai também do Editor no Windows, mas o Xcode roda só num Mac com Apple silicon |
| Embarcados (Embedded Linux, QNX) | sob pedido, para muitos chipsets, como parte do Unity Industry; Embedded Linux e QNX com 1 GB de RAM ou mais, x64 ou ARM64 de dois núcleos, OpenGL ES 3 ou Vulkan 1.1 |
| Android Automotive | os mesmos requisitos do Android |

## O que a fonte recomenda

Conferir o sistema, o processador e a API gráfica da tabela do Editor, contar 8 GB de RAM como piso recomendado e mais para projeto grande, e usar disco com IOPS alto para o build. Para quem desenvolve em Windows on Arm, o Hub beta e a emulação x86 nos pacotes sem suporte nativo.

## Citações

- "To run the Unity Editor on Windows, macOS, or Linux, a minimum of 8 GB RAM is recommended."
- "Actual performance and rendering quality might vary depending on the complexity of your project."

## Lacuna

A página não dá placa de vídeo mínima nem memória de vídeo, não dá o espaço em disco da instalação do Editor nem dos módulos, e não diz que caminho de render (URP, HDRP) roda em que placa. Não trata de gravar vídeo, do Recorder nem do Editor sem tela.
