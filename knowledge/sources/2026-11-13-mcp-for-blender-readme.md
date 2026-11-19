---
titulo: "mcp-for-blender, antigo blender-mcp (README do repositório)"
tipo: artigo
autor: "ahujasid (ahujasid/mcp-for-blender)"
url: "https://github.com/ahujasid/mcp-for-blender"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "MIT (README e API do GitHub); termos de telemetria em arquivo à parte; o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [blender, mcp, agent-control, telemetry, security]
---

# mcp-for-blender: o MCP da comunidade para o Blender aberto, com Python arbitrário

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 34316 estrelas, criado em 2025-03-07, último push em 2026-11-13, 58 issues e PRs abertos, última release nenhuma, licença reconhecida pelo GitHub: MIT.

**Em uma frase:** o servidor MCP mais estrelado para o Blender liga o agente ao Blender aberto por um addon e um socket, com nove ferramentas, a principal rodando Python arbitrário.

| Ponto | O que o texto diz |
|---|---|
| Claude Code | `claude mcp add blender uvx mcp-for-blender` |
| Ferramentas | rodar código, olhar o viewport e renders, resumo da cena, gerar 3D por serviços pagos (Tripo, Hunyuan3D, Rodin, Meshy), mundo gaussiano (World Labs), busca e importação de assets (Poly Haven, Sketchfab, Poly Pizza) |
| Aviso do autor | `execute_blender_code` roda Python arbitrário no Blender; salvar sempre o trabalho |
| Rede | o acesso por LAN não tem autenticação nem criptografia |
| Telemetria | anônima e ligada por padrão; desliga por variável; o conteúdo só com opt-in |
| Ambiente | Blender 3.0+, Python 3.10+, uv; Windows citado |

**Lacuna:** o texto não descreve modo de fundo (`blender -b`) nem render de vídeo.
