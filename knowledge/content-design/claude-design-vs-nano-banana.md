# Claude Design × Nano Banana — divisão de trabalho

Mapa de decisão: dado um ativo, gerar no **Claude Design** (artefato em código/layout on-brand) ou no **Nano Banana** (imagem raster)? No fluxo deste ambiente, **o Claude Code gera o prompt** (primeiro do design system, depois de cada artefato) e o Nano Banana entra como **complemento de imagem**. Síntese analítica, ancorada em docs oficiais.

> Fontes (oficiais, só citação): *Introducing Claude Design by Anthropic Labs*, de Anthropic, https://www.anthropic.com/news/claude-design-anthropic-labs; *Claude Design now stays on brand for daily work*, de Anthropic (claude.com/blog), https://claude.com/blog/claude-design-stays-on-brand-for-daily-work; *Nano Banana Pro: Gemini 3 Pro Image model from Google DeepMind*, de Google (blog.google), https://blog.google/innovation-and-ai/products/nano-banana-pro/; *Gemini 3 Pro Image (Nano Banana Pro) — model page*, de Google DeepMind, https://deepmind.google/models/gemini-image/pro/. Técnica de prompt de imagem em [[nano-banana-imagens-prompt]].

## A distinção de fundo
São **camadas diferentes**, não concorrentes:
- **Claude Design** (Opus 4.7, research preview) = camada de **layout/interface/documento em código** (HTML/SVG/interativo), **on-brand via design system**: lê codebase/repo/arquivos de design, **constrói com seus componentes e valida a saída contra o design system antes do preview**. Exporta PPTX/PDF/HTML/Canva. **Não gera imagem raster.**
- **Nano Banana Pro** (Gemini 3 Pro Image) = camada de **imagem raster rica** (1K–4K), consistência por até 14 referências, e — oficialmente posicionado para — **infográfico/diagrama/mapa com fatos corretos** (grounding) + **melhor renderização de texto na imagem**.

Quase não se sobrepõem — **exceto no infográfico**.

## Mapa
| Ativo | Ferramenta | Porquê |
|---|---|---|
| Landing/site, one-pager, deck | **Claude Design** | código on-brand via design system; export PPTX/HTML/Canva |
| UI, mockup, protótipo interativo (voz/vídeo/3D/shaders) | **Claude Design** | artefato interativo em código |
| Ícones de sistema (SVG 16–24px) | **Claude Design** / próprio | precisão vetorial; Nano Banana falha em "small faces/fine details" |
| Gráfico de dado que muda | **Claude Design** | código dinâmico, tokenizado, acessível |
| Hero/fundo, textura, ilustração rica | **Nano Banana** | raster fotográfico/ilustrado — Claude Design não "pinta" isso |
| Foto de produto/lifestyle, mascote/personagem | **Nano Banana** | alta fidelidade; consistência por referência |
| Infográfico-imagem (poster, social, slide de aula) | **Nano Banana** | infográfico com fatos (grounding) + texto legível na imagem |

## O overlap do infográfico
Ambos fazem — decidir pela **natureza do ativo**:
- **Claude Design (HTML/SVG)** quando precisa ser **on-brand via tokens, editável/versionável como código, acessível (texto real), dinâmico ou embutido** numa página/deck. Visual mais "geométrico/limpo".
- **Nano Banana (imagem)** quando quer **look ilustrado/poster**, **asset standalone** (carrossel, social, handout de aula), ou **diagrama factual do conhecimento de mundo** (mapa, técnico/histórico) com **ilustração+texto no mesmo bitmap**. Aceitar os limites oficiais: **texto pequeno/ortografia**, fatos **"not infallible" → conferir**.

## Onde o Nano Banana complementa
Ele preenche a **lacuna de imagem raster** que o Claude Design não cobre: **heros/ilustrações/texturas de site, fotos, mascotes e infográficos-imagem** (inclui o carrossel-esquema). Para tudo **estrutural/UI/deck/layout on-brand**, o Claude Design já resolve e o Nano Banana atrapalharia (sem tokens, não editável, fidelidade de texto limitada). O **Claude Code gera o prompt dos dois**: para o Claude Design é o *spec de build*; para o Nano Banana é o *prompt de imagem com hex/tokens + set de referências* (2–3 marca + 2–3 estilo + 1–2 paleta) — ver [[nano-banana-imagens-prompt]].

## Não-verificado
Relatos (não-oficiais) de que o Claude Design integraria **Nano Banana/Higgsfield** internamente para gerar imagens/animações no próprio prompt **não foram confirmados** nas docs oficiais nem na ferramenta `DesignSync` (que sincroniza **componentes**, não gera imagem). Tratar como boato até fonte oficial.

## Elos
- [[nano-banana-imagens-prompt]] — técnica de prompt para as imagens do Nano Banana.
- Aplicação em carrossel: [[carrossel-instagram]].
