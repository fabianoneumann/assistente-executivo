---
titulo: "Unity CLI as the replacement for the in-Editor MCP server"
tipo: artigo
autor: "Unity Technologies (documentação oficial do Unity CLI)"   # a página não tem assinatura de pessoa; o rodapé diz 'Copyright © 2026 Unity Technologies'
url: "https://docs.unity.com/en-us/unity-cli/replace-mcp-server-unity-cli"
publicado_em: null   # a página diz "Last updated 6 days ago" quando lida em 13/11/2026; o HTML traz lastModifiedDate 2026-11-06T22:14:43+00:00
capturado_em: 2026-11-13
licenca: "protegido (rodapé: 'Copyright © 2026 Unity Technologies'; sem licença de conteúdo declarada no texto lido); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unity, unity-cli, mcp, claude-code, command-line, deprecation, headless, interested-party]
---

# Unity CLI: o servidor MCP do assistente de IA do Editor foi descontinuado, e o CLI fica no lugar

Nota de fato: tabelas do que a página da documentação do Unity CLI diz sobre a troca do servidor MCP, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida. É fonte técnica curta que lista fatos, então as tabelas seguem as seções da página, na ordem dela (o `README.md` desta pasta, item 2, a exceção da página técnica), e a medida da cópia é a do `parafrase.py` e a da conta lado a lado.

**Proveniência.** Página da documentação do Unity CLI, https://docs.unity.com/en-us/unity-cli/replace-mcp-server-unity-cli, baixada com `curl` em 13/11/2026 e lida no texto do bloco `<article>` (703 palavras, de "Unity CLI" ao rodapé), conferido no HTML; sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco, não do arquivo HTML); Wayback http://web.archive.org/web/20261031005928/https://docs.unity.com/en-us/unity-cli/replace-mcp-server-unity-cli, anterior à atualização de 06/11. Título conferido no `<title>`: "Unity CLI as the replacement for the in-Editor MCP server", seguido de "Unity command-line interface (CLI)". Lida a página inteira; as páginas ligadas (Install Unity CLI e as outras) não foram abertas.

**Conferência lado a lado** (2026-11-13, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra `unity-cli-replace-mcp.txt` (o texto do bloco, na cópia de trabalho), com 23 unidades medidas (15 de prosa, 8 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas. Na leitura lado a lado, segue a fonte a unidade que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela, e conta como unidade que segue a fonte a célula que o script partiu em pedaços da mesma frase: 9 de 15 unidades do corpo (de "Em uma frase" em diante), 9 de 23 com as 8 do cabeçalho de proveniência, que não tratam do conteúdo. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 9, de "A descontinuação" à nota da versão 2.13: a página é técnica e lista fatos, e a ficha segue a ordem dela pela exceção do item 2; não há texto argumentativo do autor na página.

## Em uma frase

A Unity descontinuou o servidor MCP que vinha no pacote do assistente de IA do Editor e pôs no lugar o Unity CLI, que tem o seu próprio modo MCP e, para agente que roda shell, comandos que dirigem o Editor sem MCP no meio; a página diz quem é afetado e como migrar.

## A descontinuação

| Item | Fato |
|---|---|
| O que foi descontinuado | o componente de servidor MCP do pacote `com.unity.ai.assistant` |
| Onde esse servidor roda | dentro do Unity Editor, com o cliente MCP ligado direto nele |
| O substituto | o comando `unity mcp` do Unity CLI |
| Base do MCP do CLI | o pacote Unity Pipeline |
| Protocolo | o mesmo; o cliente se liga do mesmo jeito |
| O modo MCP do CLI | fora da descontinuação, com suporte pleno |
| Para quem o modo MCP existe | agentes que não rodam comando de shell qualquer, e modelos que montam linha de comando sem confiabilidade |

## Os comandos diretos

| Comando | O que faz, pela página |
|---|---|
| `unity command` | dirige o Editor direto, sem MCP |
| `unity eval` | dirige o Editor direto, sem MCP |
| Os dois, contra o MCP | mais rápidos e com menos tokens |
| Quando usar | se o agente roda comandos de shell |

## Quem é afetado

| Configuração | Afetada |
|---|---|
| O pacote do assistente de IA com o servidor MCP ligado a um cliente | sim |
| Pacote MCP de terceiros instalado do GitHub | não |
| `unity mcp` ou `unity command`, do Unity CLI | não |

## A migração, na ordem da página

1. Instalar o Unity CLI.
2. Rodar `unity pipeline install`.
3. Apontar o cliente MCP para o servidor do CLI com `unity mcp configure <cliente>` (os exemplos são `claude`, `cursor`, `vscode` e `windsurf`); o comando reescreve o arquivo de configuração do cliente. `unity mcp configure --list` mostra os clientes aceitos e o estado de cada um.
4. Instalar as skills da Unity para o agente: `unity skill install <agente>`.

## O que o CLI faz, pela página

| Item | Fato |
|---|---|
| Versões do Editor que o CLI gerencia | qualquer uma |
| Versão para dirigir um Editor aberto pelo Pipeline | Unity 6.0 LTS ou mais nova |
| Rede | dirige o Editor local sem internet; o servidor do pipeline só aceita conexão de localhost |
| Licença | grátis e separado do Unity AI; não pede assinatura do Unity AI |
| Agente | serve com o agente que já se usa, ou sem nenhum |
| Uso sem agente | instalar e gerenciar versões do Editor, gerenciar projetos, build sem tela (headless), rodar testes |
| Uso como ferramenta de integração contínua | sim, sozinho |
| Conflito com o pacote do assistente | corrigido a partir da versão 2.13 do pacote; versão anterior pede atualização |

## O que a fonte recomenda

Quem tem agente capaz de rodar shell usa `unity command` e `unity eval`, que a página diz serem mais rápidos e gastarem menos tokens; quem não tem fica no `unity mcp`, que segue com suporte pleno. A migração passa por instalar o CLI e o pipeline, reconfigurar o cliente e instalar as skills, e o pacote do assistente, se continuar no projeto, precisa estar na 2.13 ou depois.

## Citações

- "Unity has deprecated the MCP server included in the in-editor AI assistant package. The Unity CLI replaces this MCP server."
- "The CLI is free and separate from Unity AI."
- "the local pipeline server accepts connections on localhost only."

## Lacuna

A página não dá a data da descontinuação, nem até quando o servidor antigo funciona. Não diz se o Unity CLI está em beta, qual a versão dele, nem que comandos o `unity command` tem; não diz se o `unity eval` tem alguma trava de segurança. Não fala de gravação de vídeo nem do Recorder, e não diz se o CLI roda o Editor sem placa de vídeo.
