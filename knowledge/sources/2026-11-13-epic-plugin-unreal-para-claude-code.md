---
titulo: "Unreal Engine Skills for Claude Code (README do plugin da Epic)"
tipo: artigo
autor: "Epic Games (EpicGames/unreal-engine-skills-for-claude-code-plugin)"
url: "https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "MIT (LICENSE do repositório, Copyright (c) 2026 Epic Games, Inc., confirmado pela API do GitHub); o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [unreal, mcp, claude-code-plugin, sequencer, official-tooling]
---

# O plugin oficial da Epic para o Claude Code: o Unreal pelo MCP do próprio Editor

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório, listado no marketplace oficial `anthropics/claude-plugins-official` (o `marketplace.json` lido na mesma rodada). A skill `unreal-mcp` foi lida à parte: o servidor anuncia só três meta-ferramentas (`list_toolsets`, `describe_toolset`, `call_tool`), e nomes como `SequencerTools.create_level_sequence` se chamam por elas. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 1964 estrelas, criado em 2026-06-08, último push em 2026-10-27, 14 issues e PRs abertos, última release nenhuma, licença reconhecida pelo GitHub: MIT.

**Em uma frase:** a Epic publica no marketplace oficial do Claude Code um plugin que liga o agente ao Editor do Unreal pelo servidor MCP do próprio motor, com centenas de ferramentas em mais de 30 conjuntos, o Sequencer entre eles.

| Ponto | O que o texto diz |
|---|---|
| O que traz | a skill `unreal-mcp`, a skill `create-toolset` e um hook de início de sessão |
| Pré-requisitos | o Editor com os plugins ModelContextProtocol e AllToolsets ligados; o Editor aberto para rodar ferramentas, com o servidor iniciado pelo console |
| Conjuntos citados | atores, Blueprints, materiais, Niagara, Control Rigs, Sequencer, State Trees, widgets, Gameplay Ability System, testes |
| Windows | pelo Git Bash ou WSL; sem bash, o hook não roda, mas as ferramentas funcionam |
| Porta | 8000, caminho `/mcp`; o `.mcp.json` se gera no console do Editor |
| Proxy opcional | mantém a sessão do cliente quando o Editor cai; ferramentas em cache não provam que a chamada ao vivo funciona |

**Lacuna:** o texto não fala de render de vídeo, da Movie Render Queue nem de versão mínima do Unreal.
