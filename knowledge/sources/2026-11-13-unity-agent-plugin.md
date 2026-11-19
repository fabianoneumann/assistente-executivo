---
titulo: "Unity Agent Plugin (README e lista de skills do repositório da Unity)"
tipo: artigo
autor: "Unity Technologies (Unity-Technologies/unity-agent-plugin)"
url: "https://github.com/Unity-Technologies/unity-agent-plugin"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "Unity Companion License para projetos que dependem da Unity (LICENSE.md do repositório); sem o integral, por ser licença própria em dúvida para cópia"
areas: [generative-media]
entrada: pesquisa
tags: [unity, claude-code-plugin, agent-control, official-tooling]
---

# O plugin oficial da Unity para agentes: jogo, interface e o Unity CLI, sem Timeline nem gravação

Nota de fato: o texto integral não entra (licença abaixo); a cópia de trabalho fica fora do repositório.

**Proveniência.** README, árvore de arquivos e a skill `unity-cli` do repositório, listado no marketplace oficial `anthropics/claude-plugins-official`; cópia de trabalho na cópia de trabalho. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 636 estrelas, criado em 2026-08-06, último push em 2026-11-13, 5 issues e PRs abertos, última release nenhuma, licença reconhecida pelo GitHub: NOASSERTION.

**Em uma frase:** a Unity publica um plugin de agente (Claude Code, Codex, Grok, Antigravity, Copilot CLI) com 35 skills de desenvolvimento (contagem do assistente na árvore) de jogo, na versão 0.1.9-beta.

| Ponto | O que a fonte diz |
|---|---|
| Versão | 0.1.9-beta, nos exemplos de verificação do README |
| Instalação no Claude Code | `/plugin marketplace add Unity-Technologies/unity-agent-plugin` e `/plugin install unity@unity-agent-plugin` |
| Skills (pela árvore) | projeto novo, física 2D e 3D, tiles, sprites, interface (UGUI, UI Toolkit, IMGUI), áudio, multiplayer, compras no app, localização, URP e pós-processamento, Shader Graph, `unity-cli`, `unity-pipeline` |
| A skill `unity-cli` | roda C# no Editor aberto por `unity command script eval`; manda montar a cena no Editor ao vivo, não em batch mode |
| Vídeo | nenhuma skill de Timeline, Cinemachine ou Recorder na árvore |

**O que a fonte recomenda:** montar a cena com o Editor aberto e o CLI, e ler a saída em JSON.

**Lacuna:** nada sobre câmera de cinema, gravação de vídeo ou render sem tela.

**Conferência lado a lado:** 2 de 5 unidades seguem frases da fonte (a frase de abertura e a célula da skill `unity-cli`; a célula de vídeo vem da árvore, e a recomendação e a lacuna juntam lugares diferentes). Fonte em inglês, ficha em português: o `parafrase.py` não mede tradução, e a conta é esta.
