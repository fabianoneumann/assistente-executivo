---
titulo: "rtadewald/neo-stitch: canvas local em árvore para explorar interfaces, da imagem ao vídeo e do vídeo ao HTML"
tipo: artigo
autor: "Rodrigo Tadewald"
url: "https://github.com/rtadewald/neo-stitch"
publicado_em: 2026-10-23
capturado_em: 2026-10-30
licenca: "nenhuma declarada (campo license nulo na API do GitHub em 2026-10-30, sem arquivo LICENSE no repositório; a legenda do Reel diz 'open source'); tratado como protegido"
areas: [generative-media]
tags: [neo-stitch, image-first-design, ui-prototyping, image-to-video, video-to-html, openrouter, react-flow, file-queue, claude-code-skill, lineage, cost-tracking, multi-agent]
---

**Proveniência:** lido em 30/10/2026 pela API do GitHub, a partir do link da legenda do Reel `2026-10-30-tadewald-reel-imagem-antes-do-codigo.md`. Arquivos lidos: `README.md`, `specs.md`, `CLAUDE.md`, `AGENTS.md`, `docs/USO.md`, `docs/AGENTES.md`, `.claude/skills/neo-stitch/SKILL.md` e `modelo.md`, `ferramentas/dados/modelos_video.json`, `ferramentas/ouvir.sh`, o começo de `ferramentas/base.py` e `ferramentas/servidor.py`, uma amostra de `ferramentas/dados/jarvis_prompts.json` e o cabeçalho de `docs/escada/index.html`. Estado: criado em 23/10/2026, último push em 26/10/2026, 33 estrelas, 19 forks, TypeScript e Python. Ficha de estudo em palavras próprias; o README não entra na íntegra porque o repositório não tem licença ("open source" na legenda, mas sem licença o código continua com todos os direitos reservados).

## O que é

Um app **local** (um usuário, sem login, sem deploy) para explorar interfaces (site, app, dashboard) a partir de imagens geradas por IA, organizadas como uma **árvore num canvas infinito**: cada ideia é um nó, cada pedido fica entre a imagem de onde saiu e as que gerou, com o prompt, o modelo, o custo e os comentários guardados. A imagem aprovada ganha **vídeo** (referência de movimento) e depois **HTML vivo**. O lema do README: esboçar com imagens, dar vida com vídeo, entregar em HTML. O app não implementa o produto: termina num pacote HTML/CSS/JS com um documento de passagem.

**Por quê, nas palavras do projeto (resumidas):** ferramentas que geram telas direto em código puxam para o genérico; modelos de imagem inventam interfaces que nenhum template entrega; então primeiro a imagem, depois o movimento, por último o código, e o código só é gasto no que já foi aprovado. O `specs.md` acrescenta o problema prático que motivou o app: o processo anterior (125 imagens soltas em pastas) perdia prompts, linhagem e o vínculo das aprovadas com a origem.

## Como funciona

1. **Pedido no canvas.** O usuário seleciona imagens ou referências, tecla `N`, escreve a intenção e envia. Pode marcar "literal" para o texto ir como prompt sem reescrita.
2. **O Claude Code atende, fora do app.** O app não chama IA nenhuma: grava o pedido em disco e acrescenta uma linha a uma fila (`fila.jsonl`). O Claude Code, numa sessão aberta na pasta, escuta a fila com a ferramenta Monitor (um `tail -F` da fila, mais um arquivo de batimento tocado a cada 20 s que acende no app o ponto verde "Claude ouvindo"); a cada evento, lê o contexto completo do pedido (entradas, os prompts que geraram cada entrada, comentários com posição, o brief), escreve os prompts e roda o gerador. A skill `neo-stitch` ensina esse trabalho ao Claude.
3. **Imagens penduradas na árvore.** Geradas em paralelo pelo OpenRouter (padrão `openai/gpt-image-2`, 3 por pedido, com várias referências por pedido, testado com duas), com custo e prompt gravados no nó.
4. **Vídeo da aprovada.** Um pedido de vídeo (`V`) roda a mesma imagem em vários modelos de image-to-video ao mesmo tempo, um vídeo por modelo, para comparar.
5. **HTML.** Com o movimento aprovado, a tela é reconstruída em HTML/CSS (skills `img-to-html` e `video2html`, que ficam na máquina do autor, fora do repositório) numa pasta de versão imutável `impl/<código>/vN/`.

## As regras que valem estudar

**Prompt de imagem de interface (skill, seção 4):** abrir pelo formato ("High-fidelity 16:9 desktop app UI screen, full screen, no browser chrome, no device frame"); conteúdo concreto do brief, com rótulos reais em português e números plausíveis; estilo em termos verificáveis (paleta, família e peso da fonte, materiais, luz, densidade, grade), sem adjetivo vago; ao iterar, dizer primeiro o que manter e depois o que mudar ("mudança demais vira outra direção"); com várias entradas, dizer o papel de cada uma ("a imagem 1 é o layout aprovado, mantenha...; a imagem 2 é a referência de estilo, copie a paleta..."); comentário com posição vira instrução localizada (o x, y vira "canto superior esquerdo"). Os prompts reais do projeto JarvisOS seguem o desenho por regiões: centro, em volta, topo à esquerda, topo à direita, embaixo, e por fim o estilo visual nomeado.

**Exploração divergente antes de gerar:** num projeto novo, o Claude propõe de 4 a 6 direções de estilo bem diferentes (paleta, tipografia, materiais e composição, não só cor), cada uma com nome curto e tese de uma linha; o usuário liga e desliga as direções e só então gera. No caso geral, os N prompts de um pedido variam um eixo de cada vez, para não sair N cópias quase iguais.

**Prompt de vídeo (travas para a interface não derreter):** um prompt só, em inglês; abrir com "animate this exact UI screenshot"; câmera travada, sem zoom nem pan; todo texto, rótulo, número, painel e ícone fica nítido e intacto, nunca reescrito; nomear cada elemento que se mexe e como (respira, pisca, o LED percorre o arco); o que não foi nomeado fica parado; fechar com ritmo calmo, nenhum elemento novo, nenhuma troca de cena; até 1.000 caracteres.

**Do vídeo ao HTML (o contrato para qualquer agente, `docs/AGENTES.md`):** o conteúdo vem da imagem e o movimento vem do vídeo, e o que o vídeo inventa (texto que derrete, rótulo que muda) não entra; tudo o que se mexe é código (CSS, SVG, Canvas, Three.js, shaders, GSAP) e vídeo nunca vira asset; ir além do vídeo, com cada componente reagindo ao cursor e às ações, e o "ocioso" do vídeo virando uma função que a interação também chama; desempenho e acessibilidade ficam para depois. Um caso do README: o HTML do JAR-043 em unidades `cqw` (escala com a janela) ficou com diferença média de 2,8 em 255 contra a imagem.

**Escada do Movimento (`docs/escada/`):** uma página com dez degraus de tecnologia para dar vida a uma interface, do mais simples ao mais caro, cada um com exemplo ao vivo: HTML + CSS; CSS + JS coreografado (GSAP, ScrollTrigger); SVG; Canvas 2D; shader de tela; cena 3D procedural; 3D com shaders próprios; simulação na GPU; modelo 3D (GLB); GLB animado. E os conceitos que atravessam degraus em vez de ser um: GSAP como maestro, cursor, ruído, bloom, física, asset 3D, clipes e morphs.

## Os modelos de vídeo (o teste dele)

O catálogo (`modelos_video.json`) tem 25 modelos de image-to-video do OpenRouter, com durações, resoluções, custo de 6 s, posição em rankings públicos e o veredito de um teste em telas de interface. O critério declarado não é o vídeo mais bonito, e sim o que não mexe na interface. Os da tabela do README (os cinco que o app oferece, mais o Hailuo 3 Max), com custo de 6 s a 720p:

| Modelo | Custo | Veredito no teste |
|---|---|---|
| Hailuo 3 | ~US$ 0,78 | o mais fiel: texto e layout intactos nas telas testadas |
| Hailuo 3 Max | ~US$ 0,48 | estável e barato; às vezes troca números de telemetria (fora do menu do app, mas na tabela do README) |
| Seedance 2.5 | ~US$ 1,39 | sutil e fiel; recusa personagem com direito autoral |
| Wan 3.0 / 3.0 Prime | ~US$ 0,51 / 0,84 | bonitos, mas acendem tudo e trocam rótulos; o Wan 3.0 é o padrão do app |
| Grok Imagine 1.5 Lite | ~US$ 0,19 | rápido e barato, para rascunho; exagera no movimento |

Outros vereditos curtos do catálogo: Seedance 2.0 Mini, HappyHorse 1.0 e Seedance 1.5 Pro "reescreveram a tela"; Runway Gen-4.5 "mudou os gráficos"; Kling 3.0 Pro "deformou texto"; Veo 3.1 Lite "mexeu na marca"; Grok Imagine "virou silhueta"; Veo 3.1 e Flux 3 Video, estáveis.

## Arquitetura e dados

- **Servidor:** Python só com biblioteca padrão, rodado com `uv`, só em `127.0.0.1`, servindo a API, os arquivos (com Range, para vídeo) e o app compilado.
- **App:** Vite, React 19 e React Flow 12, tema claro e minimalista ("ícones com title, sem texto onde o componente se explica").
- **Dados:** um JSON por nó em `projects/<slug>/nodes/`, imagens, vídeos, modelos 3D, miniaturas, referências, `brief.md`, `diario.md` (decisões, mantido pelo Claude) e `lixeira/`; fora do git. Escrita atômica (temporário e rename) sob uma trava por projeto, porque app e scripts escrevem ao mesmo tempo; a interface consulta a cada ~4 s e o servidor mescla para não sobrescrever o que o Claude escreveu.
- **Tipos de nó:** brief, tela, pedido, imagem, referência, vídeo, modelo 3D. Código curto e estável por nó (`JAR-042`), nunca reaproveitado, que se copia com um clique para citar no chat. Estados da imagem: neutra, favorita, aprovada, descartada (descartar é marcar; nada se apaga, vai para a lixeira e o desfazer traz de volta).
- **Quem escreve o quê:** o app só mexe em posição, título, estado e no rascunho do pedido; o Claude escreve status, prompts, imagens, custos e os próprios comentários.
- **Custos sob teto:** até 6 imagens por pedido, US$ 20 por dia e US$ 2 por pedido de vídeo rodam direto; acima disso o gerador sai com código 3 e o Claude pergunta no chat antes de rodar com confirmação. Custo por imagem medido a 1K: ~US$ 0,055 (o `specs.md`); o nó do Reel mostra US$ 0,14 a 1536×864.
- **Página "em desenvolvimento" (fogo):** a imagem que ganhou vídeo ou HTML recebe selo e página própria, em canvas: imagem → vídeos → imagens tiradas do vídeo (placa de fundo, personagem limpo) → modelos 3D (o Tripo H3.1 aparece no exemplo, ~US$ 0,40) → versões de HTML rodando dentro do cartão.
- **Vários agentes no mesmo vídeo:** qualquer agente de código (Claude Code, Codex, OpenCode, Gemini CLI) reserva a próxima versão com `impl.py iniciar`, reporta etapa e progresso de 0 a 1 pelo menos a cada 10 min (sem atualizar por 15 min, o app mostra "parado?") e termina com `pronto`; o app só lê o `impl.json`. Alteração pedida nunca edita uma versão: cria a evolução `v1.1`, e quem aprova é o usuário, no cartão.

## O que não está no repositório

As skills que fazem o HTML (`img-to-html`, `video2html`, `animate`) e o gerador de imagens original (`openrouter-img`) são globais na máquina do autor; o repositório traz a skill que opera o canvas e o contrato para outros agentes. Requisitos declarados: macOS (miniaturas pelo `sips`), `uv` com Python 3.11+, Node 20+, Claude Code, chave do OpenRouter e `ffmpeg`.

## Tudo o mais que ensina

- **A fila como contrato entre interface e agente.** Em vez de embutir um agente no app, o app escreve um pedido e o agente que já está aberto no terminal o atende; o estado "trabalhando" e o batimento do ouvinte aparecem na interface. Resolve o "botão que dispara o agente" sem dar ao app credencial de modelo nem chat próprio.
- **Linhagem como dado de primeira classe.** "Veio de" e "Saiu daqui" em cada nó, o pedido sempre visível entre pai e filhos (guarda o porquê), recombinação ligando várias entradas, e um modo que recolhe tudo menos o caminho até as aprovadas.
- **Prompts recuperados da transcrição.** Na importação das 85 imagens antigas, os prompts originais foram reconstruídos a partir do registro da sessão do Claude que as gerou, em vez de ficarem como "sem prompt".
- **O diário de decisões por projeto**, escrito pelo agente ("JAR-042 aprovada porque..."), visível num painel do app.
- **Um teste de modelos pelo critério do uso.** O ranking público serve de contexto; o que decide é se o modelo preserva texto e layout numa tela de interface.

