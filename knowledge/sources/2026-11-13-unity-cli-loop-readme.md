---
titulo: "unity-cli-loop (README do repositório)"
tipo: artigo
autor: "hatayama (hatayama/unity-cli-loop)"
url: "https://github.com/hatayama/unity-cli-loop"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "MIT (README e API do GitHub); o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [unity, cli, agent-control, video-capture, claude-code-skill]
---

# unity-cli-loop: a Unity pelo terminal, com gravação da Game View em MP4

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 598 estrelas, criado em 2025-06-15, último push em 2026-11-13, 14 issues e PRs abertos, última release v3.24.0 2026-11-13T13:37:44Z, licença reconhecida pelo GitHub: MIT.

**Em uma frase:** a CLI `uloop` e um pacote da Unity deixam o agente compilar, testar, operar e gravar o projeto pelo terminal, com 21 skills e um comando que grava a Game View em MP4.

| Ponto | O que o texto diz |
|---|---|
| Gravar | `record-video` grava a Game View ou uma janela do Editor em MP4 (WebM no Linux) e devolve folhas de quadros e números de mudança por quadro |
| Montar a cena | `execute-dynamic-code` roda C# no Editor; `screenshot`, `get-hierarchy`, `find-game-objects` |
| Testar | entrada simulada de mouse e teclado, replay |
| Ambiente | Unity 2022.3 ou mais nova; no Windows, conexão por pipe nomeado, sem porta TCP |
| Demos | nove vídeos de sessões do Claude Code dirigindo um jogo voxel pequeno |

**Lacuna:** não diz resolução, duração nem quadros por segundo do `record-video`, nem uso sem tela.
