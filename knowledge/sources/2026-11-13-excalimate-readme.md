---
titulo: "Excalimate (README do repositório)"
tipo: artigo
autor: "excalimate (excalimate/excalimate)"
url: "https://github.com/excalimate/excalimate"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "MIT (README e API do GitHub); o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [excalidraw, whiteboard, mcp, camera-2d, hand-drawn]
---

# Excalimate: diagrama do Excalidraw animado por um servidor MCP, com câmera

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 100 estrelas, criado em 2026-03-13, último push em 2026-11-13, 9 issues e PRs abertos, última release v0.5.1 2026-09-13T14:10:05Z, licença reconhecida pelo GitHub: MIT.

**Em uma frase:** um editor web que anima diagramas do Excalidraw por quadros-chave e exporta MP4, WebM, GIF, SVG animado e Lottie, com um servidor MCP de 35 ferramentas que um agente usa.

| Ponto | O que o texto diz |
|---|---|
| MCP | 35 ferramentas, 29 antigas e seis de ação (`auto_animate`, `apply_animation_preset`, `upsert_action_sequence`, `create_camera_move`, entre elas); por HTTP local ou stdio |
| Claude Code | `claude mcp add excalimate http://localhost:3001/mcp`; skills por `npx skills add` |
| Exportação | no navegador, pelo WebCodecs |
| Aviso | boa parte do código foi feita com IA, a limpeza e as correções seguem, usar com cautela |

**Lacuna:** não diz se exporta sem navegador aberto, nem limites de duração e resolução.
