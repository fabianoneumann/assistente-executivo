---
titulo: "Hardware and Software Specifications for Unreal Engine"
tipo: artigo
autor: "Epic Games (documentação oficial do Unreal Engine)"   # as quatro páginas não têm assinatura de pessoa
url: "https://dev.epicgames.com/documentation/unreal-engine/hardware-and-software-specifications-for-unreal-engine"
publicado_em: null   # nenhuma das quatro páginas traz data visível; o título de todas diz "Unreal Engine 5.9 Documentation"; o HTML tem carimbos created_at/updated_at de trechos (de 2025 a 2026-11-09), que datam os blocos, não a página
capturado_em: 2026-11-12
licenca: "protegido (documentação da Epic Games; nenhum aviso de direitos nem licença de conteúdo no HTML baixado, cujo rodapé é montado no navegador; tratada como protegida); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unreal-engine, gpu, hardware, vram, real-time-rendering, offline-rendering, ray-tracing, global-illumination, image-sequence, interested-party]
---

# Unreal Engine 5.9: o que a máquina precisa para o Lumen e o Nanite, e como o Movie Render Pipeline exporta

Nota de fato: tabelas do que quatro páginas da documentação do Unreal Engine 5.9 dizem sobre requisitos de máquina, iluminação (Lumen), geometria (Nanite) e exportação de imagem e vídeo (Movie Render Pipeline), uma seção por página, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: as páginas são protegidas. É documentação técnica, por isso nota de fato, e as quatro são longas, lidas por seções: cada página tem a sua seção na ficha, com as tabelas na ordem das seções dela, mas as linhas de cada tabela foram dispostas fora da ordem da página, para a ficha não andar junto com o texto; o rótulo de cada linha diz o tema.

**Proveniência.** Quatro páginas de dev.epicgames.com, todas baixadas com `curl` em 2026-11-12. O sha256 de cada uma é o do texto do bloco `<main>`/`<article>` extraído pelo `baixa.py`, sem tags, script e estilo; não é o hash do HTML inteiro.

| Página | URL | sha256 (texto do `<main>`) | Wayback |
|---|---|---|---|
| P1, requisitos (a principal) | https://dev.epicgames.com/documentation/unreal-engine/hardware-and-software-specifications-for-unreal-engine | (hash omitido) | http://web.archive.org/web/20261018121524/https://dev.epicgames.com/documentation/unreal-engine/hardware-and-software-specifications-for-unreal-engine |
| P2, Lumen | https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine | (hash omitido) | http://web.archive.org/web/20261015100109/https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine |
| P3, Nanite | https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine | (hash omitido) | http://web.archive.org/web/20261015100109/https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine |
| P4, Movie Render Pipeline | https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine | (hash omitido) | http://web.archive.org/web/20260228081818/https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine |

Títulos conferidos no `<title>` do HTML: "Hardware and Software Specifications for Unreal Engine", "Lumen Technical Details in Unreal Engine", "Nanite Virtualized Geometry in Unreal Engine" e "Movie Render Pipeline in Unreal Engine", todos seguidos de "Unreal Engine 5.9 Documentation". Cobertura de fato:

- **P1:** a página tem um seletor de sistema operacional, e o bloco extraído traz só a aba Windows (o seletor abre nela), lida inteira. As abas macOS e Linux estão no JSON que a página embute no HTML; foram lidas ali, por script, nas suas tabelas (requisitos recomendados, mínimos para rodar e para desenvolver, máquina de referência no Linux, requisitos por recurso). A página macOS e a página Linux de requisitos de desenvolvimento, às quais P1 remete, não foram abertas.
- **P2:** o texto extraído inteiro, mais do que o rótulo registra (as seções de traçado por software e por hardware): também a introdução, o Surface Cache, o traçado na tela, mundos grandes, campo distante, limites gerais, plataformas, modos de visualização e solução de problemas. As imagens e o Lumen Performance Guide, citado, não foram abertos.
- **P3:** o texto extraído inteiro, da introdução às configurações de projeto. As páginas a que P3 remete (Working with Nanite-Enabled Content, Nanite Technical Details e outras) não foram abertas.
- **P4:** o texto extraído inteiro (o rótulo registra "por trechos"), do resumo ao Play Render Output. A página Render Settings and Formats, à qual P4 remete para os ajustes e formatos, não foi aberta.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra o texto das quatro páginas juntas num arquivo só (os quatro blocos extraídos e as abas macOS e Linux tiradas do JSON da P1), com 139 unidades medidas (27 de prosa, 112 de célula com texto), 13 coladas e 0 trechos de 3 ou mais seguidas; as coladas são células que colam pelo inglês dos nomes de ajuste, versão, placa ou menu (como "Ray Lighting Mode em Hit Lighting for Reflections"): dez são só fato e ficam fora da conta lado a lado, e três (o material dependente da vista, o Android e o ligar do campo distante) entram nela entre as que seguem a fonte. Na leitura lado a lado, segue a fonte a frase ou célula que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a célula só de valores, nomes e versões não conta, e a célula que o script parte em pedaços conta como uma, o que dá 133 unidades. Resultado: 87 de 133. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 2, em várias tabelas, e nenhuma delas está em texto argumentativo; as frases de "O que a fonte recomenda" juntam páginas e seções diferentes.

## Em uma frase

Documentação da Epic sobre o próprio motor: a P1 dá a máquina recomendada (32 GB de RAM, placa com 8 GB ou mais, DirectX 12) e as placas a partir das quais o Lumen e o Nanite rodam; a P2 e a P3 dizem o que cada um aceita e onde falha; e a P4 explica as três ferramentas que exportam a sequência em sequência de imagens ou vídeo, fora do tempo real.

## P1. Requisitos de máquina e software

**Máquina recomendada, por sistema**

| Item | Windows | macOS | Linux |
|---|---|---|---|
| Sistema | Windows 11 | "Latest macOS Sequoia 14" (assim na página) | Ubuntu 22.04 |
| Processador | quatro núcleos Intel ou AMD, 2,5 GHz ou mais | Apple Silicon M3; mínimo M1 ou M2, conforme os recursos de render | quatro núcleos Intel ou AMD, 2,5 GHz ou mais |
| Memória | 32 GB | 32 GB ou mais; mínimo 16 GB | 32 GB |
| Memória de vídeo | 8 GB ou mais | não diz | 8 GB ou mais |
| Placa | compatível com DirectX 12, driver mais recente | compatível com Metal 1.2 | GeForce 2080 |
| API gráfica | DirectX 12 recomendado; alguns recursos aceitam DirectX 11 | Metal 1.2 | Vulkan: AMD RADV 24.2.8+ (recomendado 25.0.0+); NVIDIA 570+ |

**Mínimo de software**

| Item | Windows | macOS | Linux |
|---|---|---|---|
| Rodar o motor | Windows 10 22H2 de 64 bits, ou Windows 10 Enterprise 21H2 de 64 bits; DirectX End-User Runtimes (junho de 2010) | Sonoma 14.5 | Rocky Linux 8 ou Red Hat 8 ou mais novo; kernel 4.18+; glibc 2.28+ |
| Desenvolver | Visual Studio 2026; o 2022 para Nintendo e AGDE abaixo da v26.1.102; VS Code e Rider também | Xcode 26.1.1 recomendado, 26.0 mínimo, 26.4 incompatível; VS Code e Rider também | Ubuntu 22.04 ou Rocky Linux 8; clang 20.1.8; VS Code ou Rider, opcionais |
| Observação | iTunes 12+ para app de iOS; 32 bits fora desde o UE5 | — | editor lento para abrir: conferir glibc 2.35+, pelo `dlopen` lento das anteriores |

| Ponto | Fato |
|---|---|
| Pré-requisitos (Windows) | instaladores no motor, como o Visual C++ 2015-2022 Redistributable |
| Quem instala | o Epic Games Launcher, sozinho |
| Quando instalar à mão | motor compilado do código, ou máquina preparada para um fim, como Swarm Agent |
| Onde ficam | `Engine/Extras/Redist/en-us` |
| Drivers | a versão estável mais recente de cada fabricante |

**Máquina de referência da Epic** (Lenovo P620, versão padrão)

| Item | Windows | Linux |
|---|---|---|
| Sistema | Windows 11 | Ubuntu 22.04 |
| Fonte | 1400 W | 1000 W |
| Memória | 256 GB DDR5-4800 (RDIMM, ECC) | 128 GB DDR4-3200 |
| Processador | AMD Ryzen Threadripper PRO 7985WX, 3,20 a 5,10 GHz | AMD Ryzen Threadripper Pro 3975WX, 32 núcleos, 64 threads, 3,5 a 4,2 GHz |
| Discos | 2 TB SSD M.2 PCIe Gen4 (sistema); 4 TB SSD M.2 PCIe Gen4 (dados) | 1 TB NVMe (sistema); 4 TB em RAID 0, 2 × 2 TB NVMe (dados) |
| Placa | NVIDIA RTX 4080, 16 GB GDDR6 | NVIDIA RTX 3080, 10 GB |
| Rede | AMD RZ616 | 1 Gbps na placa-mãe e Intel X550-T1 10G |
| Outro | TPM | TPM |

| Ponto | Fato |
|---|---|
| Compilação distribuída | recomenda o Unreal Build Accelerator (UBA), que convive com outras soluções |
| Sem compilação distribuída | base prática local de 12 a 16 núcleos; mais núcleos seguem ajudando |

**Requisitos por recurso de render**

| Recurso | Windows | macOS | Linux |
|---|---|---|---|
| Lumen (iluminação global e reflexos) e MegaLights | Windows 10 build 1909.1350+ com DirectX 12; SM6 ligado no projeto; AMD RX-6000+, Intel Arc série A+ ou NVIDIA RTX-2000+ | traçado por software: Mac com GPU Intel ou AMD, ou Apple Silicon M1+; traçado por hardware e MegaLights: sem suporte | SM6 ligado; NVIDIA RTX-2000+, AMD RX-6000+ ou Intel Arc série A+ |
| Lumen por hardware | exige SM6 no projeto | sem suporte | exige SM6 no projeto |
| Nanite e Virtual Shadow Maps | Windows 10 build 1909.1350+ e Windows 11 com DirectX 12 Agility SDK; 2004 e 20H2 na revisão .789+; DirectX 12 com atômicos do Shader Model 6.6, ou Vulkan com `VK_KHR_shader_atomic_int64`; SM6 ligado (padrão em projeto novo); driver mais recente | Apple Silicon M2+, em beta | GPU com `VK_KHR_shader_atomic_int64`; SM6 ligado (padrão em projeto novo); driver mais recente |
| Temporal Super Resolution | qualquer placa com Shader Model 5; o limite de 8 UAVs por shader pesa no desempenho; tipos de 16 bits no D3D12 com SM6 | Mac com GPU Intel ou AMD, ou Apple Silicon M1+ | não listado |
| Path Tracing | não listado | não listado | SM6 ligado; NVIDIA RTX-2000+ ou AMD RX-6000+ |

## P2. Lumen

**Metas e métodos**

| Ponto | Fato |
|---|---|
| Ordem dos traços | primeiro na tela; se não acha ou o raio passa por trás de uma superfície, um método mais confiável |
| Meta principal | mundos grandes e abertos a 60 FPS nos consoles de nova geração (nível High de escalabilidade) |
| Meta secundária | interiores limpos a 30 FPS nos mesmos consoles |
| Custo no nível Epic | cerca de 8 ms nos consoles para iluminação global e reflexos, a 1080p interno, com Temporal Super Resolution levando a perto de 4K |
| Métodos | por hardware (padrão, mais qualidade, mais caro, placa dedicada) ou por software, com campos de distância |
| Quando cada um | software: a opção que rende com muitas instâncias sobrepostas; hardware: o jeito de ter reflexo de espelho de alta qualidade |

**Surface Cache e traçado na tela**

| Ponto | Fato |
|---|---|
| Custo do traçado na tela | limita a direção de arte da luz indireta (Indirect Lighting Scale, Emissive Boost) |
| Surface Cache, o que é | parametrização automática das superfícies próximas, para ler a luz onde o raio bate |
| Cards por malha | 12 por padrão; sobe em Max Lumen Mesh Cards |
| Traçado na tela | serve a qualquer geometria e cobre diferenças entre a cena do Lumen e a de triângulos |
| Área sem cobertura | rosa no modo Surface Cache, não rebate luz e sai preta nos reflexos; corrige-se com mais cards ou partindo a malha em peças menos complexas |
| Interiores | paredes, piso e teto em malhas separadas; um cômodo inteiro com móveis numa malha só não deve funcionar |
| Malha com esqueleto | seis cards em volta da caixa antes do skinning; cobertura limitada, pior em animação que deforma muito |
| Nanite e captura | malha de muitos polígonos precisa de Nanite para captura eficiente; folhagem e Instanced Static Mesh só com Nanite |
| Material dependente da vista | Pixel Depth, Camera Position, Camera Vector podem sair errados, e o nó Ray Tracing Quality Switch dá uma versão para o Lumen |
| Spline mesh | cards da malha original reajustados à malha deformada; perde qualidade com a deformação |

**Traçado por software**

| Ponto | Fato |
|---|---|
| Quando entra | traçado por hardware desligado ou indisponível |
| Exige | Shader Model 6 e Generate Mesh Distance Fields ligado no projeto |
| Streaming | os campos entram e saem conforme a distância da câmera, num atlas único |
| Padrão | só o Global Distance Field, que junta os campos das malhas |
| Mais qualidade | Distance Field Voxel Density (projeto) ou Distance Field Resolution Scale (malha); aumenta o disco do projeto |
| Detail Tracing | campo de cada malha nos dois primeiros metros, global no resto; custo muito alto em cena de kitbashing |
| Global Tracing | só o campo global; o mais rápido e o padrão |

**Limites do traçado por software**

| Ponto | Fato |
|---|---|
| Escala | a resolução do campo vem da escala de importação; malha importada pequena e ampliada na cena fica sem resolução |
| Geometria aceita | Static Mesh, Instanced e Hierarchical Instanced Static Mesh e Landscape |
| Folhagem | só com Affect Distance Field Lighting ligado na ferramenta de folhagem |
| Partes finas e malha de uma face vista por trás | o campo não representa |
| World Position Offset | não suportado |
| Material translúcido | entra como card, recebe iluminação global difusa com Hit Lighting nos reflexos |
| Paredes | 10 cm ou mais, para a luz não vazar |
| Geometria modular | exigida; montanha ou prédio de vários andares numa malha só dá autossombreamento errado |
| Material trocado no componente | o campo segue o material do asset; blend mode ou dupla face diferentes desencontram as representações |

**Traçado por hardware**

| Ponto | Fato |
|---|---|
| Malha Nanite | usa a Fallback Mesh ou, com Generate Ray Tracing Proxies (padrão em projeto novo), um proxy próprio |
| O que ganha | mais tipos de geometria, inclusive malha com esqueleto; bate nos triângulos; pode calcular a luz no ponto do raio |
| Ajustes para hit lighting | Support Hardware Ray Tracing e Use Hardware Ray Tracing when available ligados; Ray Lighting Mode em Hit Lighting for Reflections |
| Desencontro com a Fallback Mesh | traçado na tela cobre; se não basta, subir Fallback Relative Error |
| Custo | o maior custo de montagem em cena grande com muitas malhas sobrepostas |
| Plataformas que rendem | Windows 10+ com DirectX 12 e NVIDIA RTX-2000+ ou AMD RX 6000+; PlayStation 5; Xbox Series S e X; Switch 2 |
| Sem pagar os dois | `r.DistanceFields.SupportEvenIfHardwareRayTracingSupported=0` no DefaultEngine.ini; depois disso não se alterna em tempo de execução |
| Reinício | mudar Support Hardware Ray Tracing pede reiniciar o motor |
| Malha com esqueleto | atualizar a estrutura de aceleração a cada quadro custa na proporção dos triângulos com skinning |

**Mundos grandes, campo distante, limites e plataformas**

| Ponto | Fato |
|---|---|
| Câmera rápida | a cena do Lumen fica para trás e a luz indireta aparece aos saltos |
| Cena do Lumen | em volta da câmera; aceita mundo grande e streaming |
| Alcance por software | 200 m da câmera; até 800 m em Lumen Scene View Distance; além disso, só traçado na tela |
| Nanite | não é exigido, mas a captura fica muito lenta com muitas malhas pesadas sem Nanite e sem bons LODs |
| Luz estática | iluminação global do Lumen não convive com lightmaps; os reflexos convivem |
| Campo distante (Far Field) | só por hardware; até 10 km por padrão, a partir do Max Trace Distance (200 m) |
| Android | com o renderizador de desktop (Vulkan SM5); o Mobile Renderer não |
| Ligar o campo distante | `r.LumenScene.FarField=1` no DefaultEngine.ini; exige HLOD do World Partition, com o HLOD1 construído |
| Raio de descarte | `r.RayTracing.Culling.Radius` deve casar com a distância máxima, ou fica um vão |
| Forward Shading | incompatível |
| Consoles antigos | PlayStation 4 e Xbox One fora |
| Por software, exige | DirectX 12 com Shader Model 6; NVIDIA GeForce GTX-1070 ou melhor |
| Por hardware, exige | Windows 10 com DirectX 12 ou Linux com Vulkan; NVIDIA RTX-2000+ ou AMD RX-6000+ |
| Realidade virtual | sem suporte por ora |

**Visualização e problemas**

| Sintoma ou ferramenta | Fato |
|---|---|
| Por onde começar | o modo Lumen Overview |
| Outros modos | Lumen Scene, Geometry Normals, Reflection View, Surface Cache (rosa: complexo demais; amarelo: descartado), Dedicated Reflection Rays |
| Reflexo de espelho manchado em interior | subir Lumen Scene Lighting Quality |
| Malha pequena preta no reflexo | subir Lumen Scene Detail |
| Reflexo da melhor qualidade | Hit Lighting for Reflections no projeto inteiro, ou no Post Process Volume para um só plano ou ponto de vista |
| Luz vazando em área fechada | subir Lumen Scene Detail e Max Trace Distance |
| Mudança de luz lenta | subir Final Gather Lighting Update Speed; voltar ao padrão depois |
| Emissivo pequeno inconstante | Emissive Light Source na instância |
| Sombra do céu e iluminação global somem a 200 m | subir Lumen Scene View Distance |
| Malha problemática | tirar Affect Distance Field Lighting (software) ou Visible in Ray Tracing (hardware) |

## P3. Nanite

**O que é e como funciona**

| Ponto | Fato |
|---|---|
| Disco | SSD recomendado, porque o streaming lê do disco sob demanda |
| O que é | geometria virtualizada, formato interno de malha que desenha detalhe na escala do pixel e muitos objetos |
| Memória | só o detalhe visível fica na memória; passo de render próprio, sem draw calls tradicionais |
| Trabalho | só no detalhe visível; dados muito comprimidos, streaming fino e LOD automático |
| Como funciona | na importação, a malha vira agrupamentos hierárquicos de triângulos; no render, trocados conforme a câmera, sem rachaduras |
| Malha Nanite | Static Mesh com uma marcação; continua malha de triângulos; aceita várias UVs e cor por vértice |
| Texturas virtuais | não exigidas, muito recomendadas |

**Quando usar, como ligar e recursos**

| Ponto | Fato |
|---|---|
| Skeletal Mesh | API própria, um draw call por malha, sombra por Virtual Shadow Maps, LOD de animação e não de geometria, instâncias com bancos de animação |
| Quando usar | sempre que a plataforma aceitar; boa candidata: muitos triângulos ou triângulos minúsculos na tela, muitas instâncias, grande oclusora, sombra por Virtual Shadow Maps |
| Static Mesh | sem LODs; aceita iluminação global e reflexos do Lumen e Virtual Shadow Maps |
| Exceção citada | a esfera do céu; perda pequena mesmo assim |
| Na importação | sem Lightmass, desligar Generate Lightmap UVs, que custa tempo e um canal de UV a mais |
| Como ligar | na importação (Build Nanite), no editor de cada malha ou em lote no Content Browser (Nanite > Enable) |
| Editores com a opção | Static Mesh, Skeletal Mesh e Geometry Collections |
| Projeto grande | Derived Data Cache compartilhado ajuda na conversão |
| Outros recursos | Landscape; folhagem (demo técnica de The Witcher 4); splines; deslocamento estático por tesselador offline; tesselação dinâmica por mapa de deslocamento ou material |

**Limites e suporte**

| Ponto | Fato |
|---|---|
| Materiais | só Opaque e Masked; outro tipo vira material padrão, com aviso no Output Log |
| Teto de instâncias | 16 milhões na cena, contando todas as carregadas, Nanite ou não |
| Outros limites de material | caixa Wireframe não; Vertex Interpolator e Custom UVs avaliados três vezes por pixel; nós de expressão própria (como ParallaxOcclusionMapping) podem dar artefato |
| Tangentes por vértice | não guardadas; derivadas no pixel shader; plano de suportar depois |
| Componentes aceitos | static, skeletal, instanced e hierarchical instanced static, spline mesh, geometry collection, foliage painter, landscape grass |
| Plataformas | consoles atuais e desktop com DirectX 12, Shader Model 6 e driver recente |
| Decal | projetado, sim; Mesh Decal, não |
| Deformação | translação, rotação e escala não uniforme; World Position Offset limitado, com deslocamento a limitar; Morph Targets não |
| Sem suporte no render | filtro por vista (Minimum Screen Radius, descarte por distância); Forward Rendering; estéreo de VR; MSAA; Lighting Channels; alguns modos de visualização |
| Ray tracing na malha Nanite | usa a Fallback Mesh; suporte nativo experimental com `r.RayTracing.Nanite.Mode 1` |
| Ressalva da página | instâncias, triângulos por malha, complexidade de material, resolução de saída e desempenho se medem para cada conteúdo e máquina |
| Vantagens declaradas | ordens de grandeza a mais de geometria; quadro sem teto de polígonos, draw calls e memória de malha; esculturas do ZBrush e fotogrametria importadas direto; detalhe em polígono no lugar de normal map; LOD sem ajuste à mão; perda de qualidade rara |

## P4. Movie Render Pipeline

**As ferramentas e a preparação**

| Ponto | Fato |
|---|---|
| Alpha (desde o UE 5.5) | uma caixa Alpha Output, desligada por padrão, ligada em alguns modelos (cinema, TV, produção virtual); em Rendering > Default Settings |
| O que é | a solução do motor para renderizar fora do tempo real sequências de imagem e filmes |
| Movie Render Graph | define quadros, ajustes e tipos de arquivo; um plano ou vários; grafos salvos como asset reutilizável; aceita os presets antigos da fila |
| Ferramentas | Movie Render Graph (grafo de nós, "Beta" no menu), Movie Render Queue (presets, scripts, fila) e Quick Render (um clique) |
| Holdout no Deferred | exige Support Primitive Alpha Holdout (Deferred); modelos de cinema e TV ligam; jogo pode desligar |
| Abrir o grafo | pela fila: Settings > Unsaved Config > Movie Render Graph (Beta), depois criar o asset |
| Pré-requisitos | plugin Movie Render Queue ligado (Edit > Plugins, seção Rendering, reiniciar); um Level Sequence; o Meerkat Demo serve de exemplo |

**Movie Render Queue**

| Ponto | Fato |
|---|---|
| Render (Remote) | processo separado; precisa salvar; base para uma fazenda de render; o comando vai para o Output Log |
| Movie Render Queue | fila de lotes; subamostragem temporal para motion blur radial; pixels translúcidos; HDR de 16 bits linear; configurações salvas como asset |
| Prévia | pode sair abaixo do final; com Tiling, só o ladrilho de baixo à direita; progresso, tempo decorrido e estimado, por corte de câmera |
| Abrir a fila | Window > Cinematics > Movie Render Queue, ou pelo Sequencer, ao lado de Render Movie |
| Interface | barra (somar, tirar, salvar a fila como Queue Preset), trabalhos, detalhes (nome, sequência, mapa, autor, comentário) e disparo |
| Saída padrão | sequência .jpg de 8 bits; troca-se por .png de 8 bits, entre outros |
| Render (Local) | no mesmo processo, numa sessão Play in Editor; não precisa salvar |
| Blueprints | a fila também renderiza em build de runtime, gravando no computador do usuário |
| Output | nome do arquivo, pasta e resolução |
| Deferred Rendering | a entrada tem de existir para a imagem sair; dá a imagem da viewport |
| Mapa | o trabalho abre sozinho o nível indicado; com Spawnables, a mesma cena em níveis diferentes |

**Quick Render e a saída**

| Ponto | Fato |
|---|---|
| Ajustes do Quick Render | um por modo; valem mais que o grafo padrão; o grafo padrão muda nas Project Settings de Movie Pipeline |
| Quick Render | render em tempo real para revisar; indicado para animação e visualização de arquitetura |
| Modos do Quick Render | sequência atual; viewport atual (imagem); câmeras escolhidas (imagem); sequência vista pela câmera da viewport |
| Apply Viewport Look | leva OCIO, Show Flags, View Mode e o que está visível no editor |
| Show Editor-Only Actors | billboards, câmeras, gruas, trilhos e frustums |
| Depois do render | tocar a saída, abrir a pasta ou nada |
| Tocar a saída | o motor não tem visor de imagem; usa o do sistema ou um visor indicado, com notação de quadro para RV, xStudio, DJV, HieroPlayer, mPlay, mrViewer e Cinesync |
| Faixa de quadros | a do Playback, a da seleção ou uma própria, por variáveis do grafo |
| Limite do visor do sistema | só o primeiro quadro, o primeiro trabalho e a primeira camada |
| Ganhos declarados | mais qualidade que o tempo real; ajustes para iluminação global e reflexos por ray tracing; motion blur melhor; menos artefato de anti-aliasing |

## O que a fonte recomenda

Para tirar o máximo do Lumen e do Nanite, a máquina precisa de DirectX 12 com SM6 ligado e uma placa a partir da RTX-2000, da RX-6000 ou da Arc A, e o Nanite convém em quase toda malha, com SSD para o streaming. A cena que o Lumen ilumina bem é modular, com paredes de 10 cm ou mais e cômodos em peças, e a câmera que corre demais deixa a luz indireta atrasada. Para tirar o filme do motor, a fila de render, com o plugin ligado e um Level Sequence, exporta em sequência de imagens; o Quick Render serve à revisão.

## Citações

- "Fast camera movement will cause Lumen Scene updating to fall behind [...], causing indirect lighting to pop in as it catches up." (P2, Large Worlds)
- "Importing an entire room, which includes furniture, in a single mesh is not expected to work with Lumen." (P2, Surface Cache)
- "By default, Movie Render Queue will render out to a sequence of .jpg images." (P4, Output Settings)

## Lacuna

Nenhuma das páginas dá a memória de vídeo mínima por recurso nem um mínimo de máquina para o Windows (P1 só traz o recomendado), e nenhuma dá tempo de render, por quadro ou por segundo de filme, em alguma placa. A P1 lista as placas do Lumen sem separar o traçado por software, que a P2 põe a partir da GTX-1070, e nenhuma explica a diferença. A P4 não diz que máquina o render fora do tempo real pede, nem traz os formatos de vídeo e os ajustes, que deixa para outra página. Nenhuma das quatro tem data visível; só a versão do motor (5.9).
