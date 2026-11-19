---
titulo: "claude-codes-influencers (README do repositório)"
tipo: artigo
autor: "kevinbadi (kevinbadi/claude-codes-influencers)"
url: "https://github.com/kevinbadi/claude-codes-influencers"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "MIT (README e API do GitHub); o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [2d-character, lip-sync, rhubarb, vertical-video, claude-code-skill]
---

# claude-codes-influencers: mascote 2D falante com Rhubarb, feito pelo Claude Code

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 40 estrelas, criado em 2026-10-14, último push em 2026-10-14, 0 issues e PRs abertos, última release nenhuma, licença reconhecida pelo GitHub: MIT.

**Em uma frase:** um mascote 2D transforma um roteiro em vídeo vertical 1080x1920 com voz, lip sync pelo Rhubarb, poses por palavra-chave, piscadas e legenda, com skills do Claude Code.

| Ponto | O que o texto diz |
|---|---|
| CLI | `python make.py` com `video`, `create`, `new`, `check`, `draw`, `voice` e `sheet` |
| Skills | `mascot-video` e `draw-mascot`, em `.claude/skills/` |
| Lip sync | o Rhubarb, cerca de 20 MB; o Whisper dá o tempo das palavras |
| Voz | `say` do macOS, ElevenLabs, Voicebox local ou um arquivo de áudio próprio (no Windows, passar o áudio) |
| Criar mascote a partir de imagem | quatro chamadas à API da Anthropic, abaixo de US$ 1 |
| Exemplos | três mascotes, com folhas de modelo e quadros |

**Lacuna:** não diz tempo de render nem teste completo no Windows.
