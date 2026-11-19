---
titulo: "sketch-to-3d (README do repositório)"
tipo: artigo
autor: "dannystuart (dannystuart/sketch-to-3d)"
url: "https://github.com/dannystuart/sketch-to-3d"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "MIT (README e API do GitHub); o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [threejs, line-drawing, pen-style, claude-code-skill, 3d-object]
---

# sketch-to-3d: o modelo 3D que se desenha a marcador antes do render

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 32 estrelas, criado em 2026-11-05, último push em 2026-11-09, 0 issues e PRs abertos, última release nenhuma, licença reconhecida pelo GitHub: MIT.

**Em uma frase:** uma skill do Claude transforma um modelo 3D (GLB, OBJ, FBX e outros, ou um objeto feito em three.js) num desenho a marcador que se faz sozinho e termina num wipe para o render, em cerca de 7 s, em vídeo ou página web.

| Ponto | O que o texto diz |
|---|---|
| Comando sem agente | `node scripts/render.mjs chair.glb --out chair --size 1080x1080`; `--code lamp.js` para objeto feito em three.js |
| Paletas | papel branco, folha vermelha, lápis, blueprint |
| Tempo | 7 s em 1080p em cerca de 30 s num laptop recente, o dobro com transparência |
| Ambiente | Node 18+, git, ffmpeg; o Chromium do Playwright, cerca de 500 MB, uma vez |
| Limites | scan 3D bruto sai rabiscado; parte deformável com rig e nuvem de pontos não se desenham; vidro claro esconde o que está atrás |
| Saída | mp4, stills por etapa e um relatório de autoconferência |

**Lacuna:** não cita Windows nem GPU.
