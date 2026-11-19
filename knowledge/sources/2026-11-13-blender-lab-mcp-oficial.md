---
titulo: "Blender MCP (README e lista de ferramentas do repositório lab/blender_mcp)"
tipo: artigo
autor: "Blender Lab (projects.blender.org/lab)"
url: "https://projects.blender.org/lab/blender_mcp"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "GPL-3.0 (arquivo LICENSE do repositório e campo licenses da API do Gitea do projects.blender.org); o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [blender, mcp, agent-control, headless-render, official-tooling]
---

# O MCP oficial do Blender (Blender Lab): ferramentas para o Blender aberto e para o Blender em processo de fundo

Só a ficha: o texto integral está na url do frontmatter.

**Proveniência.** readme.md e readme_tools.rst do repositório lab/blender_mcp no projects.blender.org (a página web deu 403; o texto veio pelo caminho raw e os dados pela API do Gitea: criado em 21/02/2026, atualizado em 29/09/2026, 37 estrelas, 40 forks, 27 issues e 5 PRs abertos, 6 releases, a última v1.0.3 de 11/09/2026). Chegou pela lista da Evolink, que aponta o guia oficial. As respostas da API do Gitea ficaram na cópia de trabalho. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado).

**Em uma frase:** o Blender tem um servidor MCP próprio, feito pelo Blender Lab, pequeno de propósito, com um addon que roda dentro do Blender e um servidor que o cliente MCP abre, falando por socket TCP.

| Ponto | O que o texto diz |
|---|---|
| Peças | addon em `addon/blender_mcp_addon/` (porta, host e auto-início nas preferências) e servidor `blender-mcp` em `mcp/blmcp/`, aberto pelo cliente por stdio |
| Blender em processo de fundo | ferramentas com sufixo `_for_cli` rodam o código ou abrem o arquivo num Blender de fundo; o modo de fundo só aceita pedido que termina na hora (sem resposta adiada) |
| Ferramentas de cena | rodar Python no Blender aberto, resumo do arquivo e dos objetos, foco do viewport, troca de aba |
| Imagem | captura de uma área ou da janela inteira em PNG; render de miniatura e render da cena num caminho |
| Documentação embutida | a referência da API Python e trechos do manual vão no pacote, com busca de texto |
| Cliente citado | Llama.cpp, com wiki para LLM local |

**Lacuna:** o texto não fala de animação, de vídeo nem de Grease Pencil, não dá requisito de máquina e não diz se o render da cena serve a uma sequência de quadros.

O texto integral está na url do frontmatter.
