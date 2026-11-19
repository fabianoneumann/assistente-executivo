# Machinima e motores de jogo: o que cada motor custa e roda, o jogo comercial, e os complementos do Blender

Os motores de jogo como estúdio de vídeo (Unreal, Unity, Godot, iClone com Character Creator, Source Filmmaker), a machinima feita dentro de jogo comercial, os complementos do fluxo do Blender (bibliotecas de assets, animação assistida, captura de movimento por vídeo, storyboard no Grease Pencil) e o que respostas de modelo afirmaram contra a primária. Pesquisa rasa nas três frentes (62 buscas: 12 Perplexity, 12 Gemini e 38 nativas; pior caso de cerca de US$ 1,20), revisada com conferência e re-revisão. A síntese irmã do mundo 3D ([[mundo-3d-com-camera-por-codigo]]) cobre o Three.js, o Blender sem tela com Line Art, os assets CC0 e o Mixamo; o vocabulário de câmera que os motores trazem está em [[linguagem-de-camera-virtual]]; a comparação Unity contra Unreal para vídeo (os servidores oficiais de agente, o render pela linha de comando nos dois, o MetaHuman pela voz, os requisitos da Unity 6.6, a cláusula de "education technology" dos termos do Editor e a leitura de quando usar cada um) está em [[unity-e-unreal-para-video]].

**O que a base já tinha:** a rota do Unreal 5.8 por linha de comando, a montagem dele como "a mais pesada" do artigo e o `--write-movie` do Godot 4.7.2 que precisou de tela, num texto de quem vende um renderizador ([[2026-11-11-voyager-render-3d-headless]]); o Movie Maker do Godot ([[2026-11-12-godot-gravar-filmes]]) e o Recorder do Unity, que grava só no editor ([[2026-11-12-unity-recorder-manual]]). A ferramenta de partida para vídeo por código é o HyperFrames ([[video-como-codigo]]).

**Leitura do assistente:** a machinima no sentido próprio (filmar dentro de um motor de jogo) resolve um problema que uma série desenhada não tem: os motores entregam o 3D fotorrealista ou de jogo, que teria de virar traço, como o Sobel no Three.js e o Line Art no Blender. Um motor que entregasse quadros ou GLB ao HyperFrames ampliaria a comparação com o Blender, não trocaria a ferramenta. O que se traz já é vocabulário de direção (trilho, grua, corte e fusão de câmeras, plano e take), que o código faz.

## Os motores, pelo custo e pelo que roda numa máquina de entrada

A máquina de referência: GTX 1660 Ti de 6 GB, i7-12700, 16 GB de RAM, com o Blender 5.2.4 LTS instalado.

| Motor | Custo | Roda na máquina de referência? | Risco |
|---|---|---|---|
| Unreal 5 (Sequencer e Movie Render Queue) | zero: vídeo renderizado não paga royalty, mesmo monetizado, e o assento fica dispensado abaixo de US$ 1 milhão de receita bruta em 12 meses (contando o grupo e o capital levantado); pede conta na Epic e o aviso nos créditos | **apertado:** a Epic só publica o recomendado (32 GB de RAM, 8 GB ou mais de vídeo, DirectX 12), sem mínimo; o Lumen por software pede "GTX-1070 or higher" (que a 1660 Ti caiba é leitura do assistente, pela geração), e nele o personagem com esqueleto entra limitado; o Nanite pede Shader Model 6.6 atomics, que a 1660 Ti ter vem só de fórum | visual de motor contra o traço desenhado; a montagem mais pesada; conta nova |
| Unity 6 (Timeline, Cinemachine, Recorder) | zero no Personal, abaixo de US$ 200 mil de receita e captação; mas quem usa o Unity para o que não é só jogo ou entretenimento é "Industry Customer", a critério da Unity, e não pode usar o Personal (pela página de planos): aí o Pro, US$ 2.310 por assento por ano; os termos do Editor de 30/06/2026 (seção 4, o texto que obriga) e a FAQ põem "education technology" entre os exemplos ([[2026-11-12-unity-precos-planos-e-termos-do-editor]]); cada usuário avalia o próprio enquadramento, que é a critério exclusivo da Unity ([[unity-e-unreal-para-video]]) | **provável** (leitura do assistente): a 6.6 não dá placa mínima; pede placa com DX10 a DX12 ou Vulkan e 8 GB de RAM como mínimo recomendado ([[2026-11-13-unity-6-6-requisitos-de-sistema]]) | a cláusula Industry; o Recorder só grava no editor, em Play |
| Godot (Movie Maker) | zero (MIT, pelo `LICENSE.txt` do repositório) | provável, não medido | o `--write-movie` precisou de tela na 4.7.2 (texto de fabricante); outro ecossistema; ganho pequeno sobre o Three.js no HyperFrames (leitura do assistente) |
| iClone 8 com Character Creator 5 | o Personal é grátis, mas sem uso comercial: o render é só para uso pessoal e social, e o uso comercial pede a versão perpétua ou a assinatura (os preços carregam por script e não vieram; os US$ 599 e 299 das respostas não foram verificados) | **não:** o mínimo da página do Personal é 8 GB de VRAM e 16 GB de RAM | o Personal limita a 30 exportações 3D de 30 s; o estilo é humano digital |
| Source Filmmaker | a ferramenta pode ter uso comercial; os assets dos jogos da Valve são só para uso pessoal e não comercial | provável, não medido | ferramenta de 2012; o visual dos jogos da Valve |

Fontes: [[2026-11-12-unreal-eula-e-pagina-de-licenca]], [[2026-11-12-unreal-docs-requisitos-lumen-nanite-e-movie-render]], [[2026-11-12-unity-precos-planos-e-termos-do-editor]], [[2026-11-12-reallusion-iclone-personal-planos-e-licenca-de-conteudo]], [[2026-11-12-valve-sfm-e-politica-de-video]]; o `LICENSE.txt` do Godot fica como citação (abaixo), porque a ficha do Movie Maker já está na base.

**O que mais pesa no Unreal:**

- **O conteúdo da Epic tem regra própria** ([[2026-11-12-epic-content-license-e-metahuman]]): o conteúdo entra livre em mídia linear renderizada, mas o Megascans depende do plano da conta no momento do download (no plano pessoal e no Indie, como o resto do conteúdo; no plano Unreal Engine, só junto da Unreal; baixado sem plano, só para avaliação interna, e não vai em peça); o MetaHuman, pelo adendo, só se usa junto da Unreal, enquanto a página de licença dele diz que se usa "with any engine or creative software" (contradição entre duas primárias da Epic; nos metadados do HTML, a página do MetaHuman foi atualizada em 02/02/2026, e o acordo de conteúdo tem 23/02/2026 no corpo e 12/10/2026 na página, mas nenhum texto diz qual prevalece).
- **A IA:** o anúncio da Epic de 29/10/2026 diz que tirou do EULA as restrições de treino de IA com a engine e com o MetaHuman, para quem aceitar o EULA novo, aceite que é automático para o usuário novo e opcional para quem já usa ([[2026-11-12-unreal-anuncio-eula-ia-2026-10-29]]); o conteúdo marcado "NoAI" pelo vendedor segue fora da entrada de IA generativa ([[2026-11-12-epic-content-license-e-metahuman]], o acordo de conteúdo, seções 5(c)(viii) e 17). O FAQ da página do MetaHuman, atualizada em 02/02/2026, antes do anúncio, ainda traz o veto de usar os personagens e as curvas para treinar ou testar IA, e a resposta remete o veto ao EULA da Unreal ("as further detailed in the Unreal Engine EULA"), mas o EULA lido não tem cláusula sobre IA ([[2026-11-12-unreal-eula-e-pagina-de-licenca]]); nenhum dos textos diz qual vale.
- **A combinação com licença copyleft:** o EULA e o contrato de conteúdo proíbem combinar a engine e o conteúdo com GPL, LGPL ou CC BY-SA (leitura do assistente: pesaria só se o manual do Blender, CC BY-SA, entrasse num projeto Unreal).
- **O render:** a Movie Render Queue é o render offline de conteúdo linear, e a saída padrão é sequência de imagens (JPG, PNG ou EXR).

## Machinima em jogo comercial: fora, para quem divulga o próprio negócio

O que as primárias dizem, que é o porquê de não usar: GTA, Minecraft, os jogos da Microsoft e a Roblox excluem, por escrito, o vídeo que promove produto ou serviço, que é o caso de um perfil que divulga o próprio negócio (leitura do assistente, forte, não é parecer jurídico); a Valve permite o vídeo monetizado, mas os assets são para uso não comercial.

| Jogo | O que permite | O que exclui | Fonte |
|---|---|---|---|
| GTA (Rockstar) | uso de fã não comercial; "we love seeing machinima" | não comercial é não ganhar dinheiro com a filmagem nem usá-la para promover produto ou serviço; licença caso a caso | [[2026-11-12-rockstar-politica-de-material-protegido]] |
| Minecraft (Mojang) | criar e compartilhar vídeo, com anúncio, se for grátis de ver e tiver conteúdo próprio bastante | promover o que não é Minecraft, inclusive por "individual artists"; as permissões são revogáveis | [[2026-11-12-minecraft-diretrizes-de-uso]] |
| Jogos da Microsoft | licença pessoal, não exclusiva e revogável; anúncio no YouTube e na Twitch | página que vende outros produtos ou serviços; a licença comercial, a Microsoft diz que ainda não deu a ninguém | [[2026-11-12-xbox-regras-de-conteudo-de-jogo]] |
| Roblox | vídeo e animação monetizados com os avatares atuais (post oficial de 2022) | os avatares clássicos em conteúdo comercial; os termos de 01/11/2026 restringem o conteúdo da Roblox em obra derivada fora da plataforma | [[2026-11-12-roblox-termos-diretrizes-e-licenciamento]] |
| Jogos da Valve | o vídeo monetizado pelo programa de parceria do YouTube "and similar programs" | cobrar para ver, vender, licenciar; os assets do SFM são só para uso não comercial | [[2026-11-12-valve-sfm-e-politica-de-video]] |
| YouTube | o conteúdo de jogo pode ser monetizado conforme os direitos que a publicadora dá | o vídeo que só mostra alguém jogando por muito tempo | [[2026-11-12-youtube-ajuda-conteudo-de-videogame]] |

A lei brasileira não abre outra porta: o art. 46 da Lei 9.610/98 permite citar passagens para estudo, crítica ou polêmica, na medida do fim, e reproduzir pequenos trechos quando a reprodução não é o objetivo da obra nova; o inciso VI, que o Gemini cita como uso didático, trata de representação teatral e execução musical no recesso familiar ou na escola ([[2026-11-12-lei-9610-1998-arts-8-e-46-a-48]]). Leitura do assistente, não parecer jurídico.

## Os complementos do fluxo do Blender

| Ferramenta | Licença, pela primária | O grátis | Situação |
|---|---|---|---|
| Poly Haven (HDRIs, texturas, modelos) | CC0 em todos os assets, inclusive em produto vendido; não pode se dizer autor nem relicenciar; os termos do site proíbem raspagem sem permissão, e a API tem termos à parte, não abertos | tudo | serve já, baixado à mão ([[2026-11-12-polyhaven-licenca-cc0-e-faq]]) |
| BlenderKit | duas licenças por asset, Royalty Free e CC0; tudo o que se baixa serve a uso comercial, e a Royalty Free proíbe revender o asset | uma parte da biblioteca (23.944 de 82.658 modelos; todos os materiais), com o add-on | serve com a licença de cada asset anotada ([[2026-11-12-blenderkit-licencas-e-planos]]) |
| Cascadeur | o Free proíbe uso comercial e só exporta `.casc`; o Indie exporta FBX e glTF, abaixo de US$ 100 mil de receita ou captação em 12 meses | o Free, sem prazo | o Free não vale em peça publicada ([[2026-11-12-cascadeur-planos-e-eula]]) |
| Rokoko Vision | o usuário fica com os direitos do que gera; a Rokoko pode usar o conteúdo dele para melhorar os serviços e sublicenciá-lo anonimizado; os assets da Rokoko não podem servir a desenvolver ou treinar IA | 30 s por mês de vídeo para animação, em FBX | a cláusula de IA se confere antes de usar, se a peça passar por um avaliador de IA ([[2026-11-12-rokoko-vision-precos-e-termos]]) |
| DeepMotion Animate 3D | a licença depende do plano | 60 s por mês, só para uso pessoal e não comercial | só teste ([[2026-11-12-deepmotion-animate-3d-precos-e-faq]]) |
| Plask | o serviço é para uso pessoal e não comercial; licença comercial no plano "Commercial"; a Plask pode processar o conteúdo do usuário por aprendizado de máquina | 15 s por dia, FBX, GLB e BVH | o grátis não vale em peça publicada ([[2026-11-12-plask-precos-e-termos]]) |
| QuickMagic | não lida (a página de preços deu 403) | — | não verificado ([[2026-11-12-quickmagic-pagina-inicial]]) |
| Move.ai (Move One) | não lida (a documentação e o EULA saíram do ar) | 30 créditos, pela busca | só citação (https://docs.move.ai/knowledge/move-ai-pricing-plans-credits, https://www.move.ai/move-one-eula) |
| FreeMoCap | AGPL-3.0 no programa, com oferta de outra licença paga; se o movimento capturado fica livre, o README não diz | grátis, local, com webcams | provável que rode numa máquina de entrada ([[2026-11-12-freemocap-readme]]) |

**Leitura do assistente:** quando o personagem da série é desenho, não 3D com esqueleto, a captura de movimento só entra se um personagem 3D CC0 (como os da Quaternius, em [[mundo-3d-com-camera-por-codigo]]) entrar.

## O Blender: o que o Gemini disse e o que a primária diz

| Afirmação do Gemini | A primária | Veredito |
|---|---|---|
| O EEVEE é tempo real, para prévia e vídeo estilizado; o Cycles dá a luz realista | o manual chama o EEVEE de motor de render em tempo real, por rasterização, que não é path tracer, e diz que o Cycles sempre dá render mais exato fisicamente | confirmado |
| O Blender tem Grease Pencil e rigging | o Grease Pencil serve a animação 2D, recorte, motion graphics "or use it as a storyboard tool"; o rigging não foi aberto | em parte |
| O BlenderKit e o Poly Haven são grátis | o Poly Haven inteiro; o BlenderKit em parte (acima) | em parte |
| Para renderizar sem travar, RTX ou AMD recente e 16 GB de RAM | mínimo oficial no Windows: 8 GB de RAM, 2 GB de vídeo com OpenGL 4.3, GeForce 900 ou mais nova; recomendado: 32 GB e 8 GB; o RTX só acelera o traçado de raios do Cycles (OptiX) | não é requisito |

Fontes: [[2026-11-12-blender-manual-eevee-cycles-gpu-e-grease-pencil]] (CC BY-SA 4.0, com o integral) e [[2026-11-12-blender-requisitos-de-hardware]]. **Na máquina de referência (leitura do assistente):** os 16 GB ficam entre o mínimo e o recomendado, e os 6 GB da placa abaixo dos 8 recomendados; para um caminho leve (EEVEE ou Workbench com Line Art, ou só a fábrica de GLB), o que limita é a VRAM em cena grande.

**O storyboard no Grease Pencil:** o template Storyboarding parte do 2D Animation e acrescenta o editor de sequência com Sync Scene, uma cena Edit de 10 s como linha do tempo mestre e cada plano como cena própria (Shot.000 como modelo, planos de 2 s). Que o add-on Storypencil quebrou com o Grease Pencil 3 vem de uma avaliação de usuário pela busca: não verificado.

## As regras que saem daqui

1. **A comparação com motor de jogo vem depois** de esgotar o Three.js e o Blender, porque o motor traz visual de jogo e montagem pesada.
2. **Jogo comercial fica fora** para conteúdo que divulga negócio: as licenças excluem a promoção por escrito.
3. **Os planos grátis da Plask e do Cascadeur e o material da Valve não valem em peça publicada,** porque proíbem uso comercial.
4. **As cláusulas que dependem de enquadramento** (a de IA da Rokoko, a Industry Customer da Unity) se conferem antes de usar a ferramenta, não antes; quem decide o enquadramento é quem responde pelo uso.
5. **O Blender sem tela e o animatic no Grease Pencil se testam juntos:** montar por script as estações em blocos e o animatic da cena (blocos, setas e texto do roteiro em Grease Pencil, com os tempos na cena Edit do template Storyboarding), e medir se o Grease Pencil sai em segundo plano no Windows e o tempo por quadro ([[mundo-3d-com-camera-por-codigo]]).

## Os testes que sobram (nada rodado; sem custo de API)

1. **O teste do Blender sem tela com o animatic** (regra 5).
2. **Poly Haven no mesmo teste** (proposta do assistente): uma textura de papel ou um HDRI CC0, baixado à mão, no cenário de blocos com Line Art, para ver se a luz ajuda a ler a profundidade sem fugir do traço da série.
3. **Unreal e Unity numa GPU de entrada:** o que o teste mede e o que falta saber sem testar estão em [[unity-e-unreal-para-video]].
4. **FreeMoCap com a webcam num personagem 3D CC0:** só se o personagem 3D entrar.

## Contradições e não verificado

- **MetaHuman fora da Unreal:** a página de licença e o adendo do contrato de conteúdo, as duas da Epic, dizem o contrário (acima).
- **Nanite na GTX 1660 Ti:** o Gemini diz que roda bem; a Perplexity, que não é alvo sensato de produção; a Epic pede os atomics de SM 6.6 sem listar placas.
- **VRAM do iClone:** 8 GB e GTX 10 na página do Personal (a mais nova lida); 4 GB e GTX 900 no manual e na página do trial, pela busca, não verificados; RTX 2060 no Gemini.
- **Páginas que se contradizem:** as janelas da página de planos do Cascadeur falam de uma "versão grátis" para quem fica abaixo de US$ 100 mil, com 300 quadros por cena, enquanto os cartões e o EULA dizem que o Free não tem uso comercial; na página de preços da Rokoko, o BVH, o CSV, o limite do Vision e o teste grátis mudam entre os cartões, a tabela e o FAQ; na Plask, os termos dão 30 s por dia de exemplo no grátis, e a página de preços, 15 s. Cada ficha registra os dois lados com o lugar.
- **Respostas contra a primária:** o Gemini dizia que a Take-Two deixa monetizar machinima, que o Poly Haven pede para não revender, que o BlenderKit grátis é cerca de metade da biblioteca, que o grátis da Plask permite uso comercial, que o FreeMoCap é "fully permissive" e que o mínimo do Blender é 16 GB com GTX 1660; em todos, vale a primária (acima).
- **MetaHuman e IA:** o anúncio de 29/10/2026 diz que a restrição de IA do MetaHuman saiu, para quem aceitar o EULA novo; o FAQ da página do MetaHuman, de 02/02/2026, ainda a traz (acima).
- **O assento do Unreal:** a página de licença em português dá R$ 6.682,00 por ano; a mesma página em inglês dá US$ 1.850 por usuário por ano no FAQ, e o cartão, preenchido pela localização, traz o valor em dólar fixo só para Belarus, China e Rússia ([[2026-11-12-unreal-eula-e-pagina-de-licenca]]).
- **Preços não verificados:** o iClone e o Character Creator perpétuos, os planos da QuickMagic e da Move.ai.

## Fontes

- **Raw:** as fichas acima. Com o integral: [[2026-11-12-blender-manual-eevee-cycles-gpu-e-grease-pencil]] (CC BY-SA 4.0) e [[2026-11-12-lei-9610-1998-arts-8-e-46-a-48]] (texto de lei). Só ficha: as demais, de obra protegida, e o README do FreeMoCap, cuja licença do texto não está declarada. Da base: [[2026-11-11-voyager-render-3d-headless]], [[2026-11-12-godot-gravar-filmes]], [[2026-11-12-unity-recorder-manual]], [[2026-11-13-unity-6-6-requisitos-de-sistema]].
- **Citação:** o `LICENSE.txt` do Godot (https://raw.githubusercontent.com/godotengine/godot/master/LICENSE.txt); a documentação de preços e o EULA da Move.ai (acima).

## Ver também

[[unity-e-unreal-para-video]] (os servidores oficiais de agente, o render pela linha de comando, a licença da Unity e quando usar cada motor), [[mundo-3d-com-camera-por-codigo]] (o Three.js, o Blender sem tela, os assets e os testes), [[linguagem-de-camera-virtual]] (o trilho, a grua e a câmera em cada motor), [[video-como-codigo]] (o HyperFrames).
