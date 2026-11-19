---
titulo: "explainer-studio (README do repositório)"
tipo: artigo
autor: "reedodev (reedodev/explainer-studio)"
url: "https://github.com/reedodev/explainer-studio"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "MIT (README e API do GitHub); fontes sob SIL OFL 1.1; o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [whiteboard, hand-drawn, explainer, cpu-render, windows]
---

# explainer-studio: explicador desenhado traço a traço, em CPU, medido no Windows

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 21 estrelas, criado em 2026-10-20, último push em 2026-10-22, 0 issues e PRs abertos, última release v1.0.0 2026-10-22T11:00:11Z, licença reconhecida pelo GitHub: MIT.

**Em uma frase:** um storyboard em JSON vira vídeo explicativo narrado e desenhado traço a traço em oito estilos (o quadro branco entre eles), com quadros desenhados num canvas de CPU e passados ao FFmpeg.

| Ponto | O que o texto diz |
|---|---|
| Medida no Windows | 53,3 s de vídeo em 42 s (Node 26.5.0, FFmpeg 8.0.1) |
| Máquina | sem GPU, sem API paga, sem modelo de vídeo; os oito estilos da demo, de 10 a 60 s cada num PC de mesa |
| Agente | plugin do Claude Code e CLI `npm run es --` com `build`, `render`, `styleframes` e `init` |
| Voz | silent, SAPI do Windows, comando próprio ou edge (endpoint não oficial) |
| Limites declarados | só 1920x1080 horizontal; sem rig de personagem, 3D nem gravação de tela; legenda pelo tamanho da frase, não por palavra; passar nas checagens não é assistir |

**Lacuna:** não diz uso de disco nem de memória.
