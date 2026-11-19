---
titulo: "Unreal_mcp, EngineWire (README do repositório)"
tipo: artigo
autor: "ChiR24 (ChiR24/Unreal_mcp)"
url: "https://github.com/ChiR24/Unreal_mcp"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "MIT (README e API do GitHub); o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [unreal, mcp, sequencer, movie-render-queue, security]
---

# Unreal_mcp (EngineWire): o MCP da comunidade que declara Sequencer, Movie Render Queue e Take Recorder

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 1035 estrelas, criado em 2025-09-07, último push em 2026-11-13, 13 issues e PRs abertos, última release v0.6.0 2026-10-27T17:11:57Z, licença reconhecida pelo GitHub: MIT.

**Em uma frase:** um plugin C++ serve MCP dentro do Editor do Unreal 5.0 a 5.8, com uma ferramenta pública que roteia para 23 internas, entre elas a de Level Sequences, Movie Render Queue e Take Recorder.

| Ponto | O que o texto diz |
|---|---|
| Cinema | `manage_sequence`: Level Sequences, câmeras, Movie Render Queue, mídia, Take Recorder, replays |
| Plugins exigidos | Python Editor Script, Movie Render Pipeline, Takes, Level Sequence Editor, entre outros |
| Segurança | escuta só em 127.0.0.1; token por projeto; consentimento por chamada para exclusões e algumas escritas; caminhos de asset limitados |
| Instalação | pela Fab, sem compilar, ou por clone com projeto C++ |
| Versões | 0.6.0 estável; o clone em 0.6.1-beta |

**Lacuna:** não diz os parâmetros do render, se roda sem tela, nem tempos.
