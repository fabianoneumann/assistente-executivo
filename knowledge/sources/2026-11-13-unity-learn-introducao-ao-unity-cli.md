---
titulo: "Introduction to Unity CLI"
tipo: artigo
autor: "Unity Technologies (tutorial do Unity Learn)"   # a página credita "Unity Technologies"; o exemplo de saída do `unity status` mostra um caminho de usuário "thomaskr", sem nome completo
url: "https://learn.unity.com/tutorial/introduction-to-unity-cli"
publicado_em: 2026-08-10   # o JSON-LD da página traz createdAt 2026-08-10T16:19:05Z e updatedAt 2026-11-12T21:01:10Z; o texto visível não tem data
capturado_em: 2026-11-13
licenca: "protegido (rodapé: 'Copyright © 2026 Unity Technologies'; sem licença de conteúdo declarada no texto lido); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unity, unity-cli, mcp, claude-code, command-line, agentic-workflows, csharp, interested-party]
---

# Unity CLI e o pacote Pipeline: o Editor vira um servidor local de comandos para o terminal e para o agente

Nota de fato: tabelas do que o tutorial do Unity Learn ensina, uma seção por passo do tutorial, na ordem dele, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida. É fonte técnica, e os passos de um tutorial são o método, então a ordem é a dele (`knowledge/sources/README.md`, item 2); a medida da cópia é a do `parafrase.py` e a da conta lado a lado.

**Proveniência.** Tutorial do Unity Learn, https://learn.unity.com/tutorial/introduction-to-unity-cli, nível iniciante, 15 minutos, baixado com `curl` em 13/11/2026 e lido no texto do bloco `<main>` (3.095 palavras, do título ao "Complete this Tutorial"), conferido no HTML; o JSON-LD da página dá a data de criação (10/08/2026), a de atualização (12/11/2026), as versões que ele diz cobrir ("6.4", "6.3", "6.2", "6.1", "6.0") e os seis passos. sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco, não do arquivo HTML); Wayback http://web.archive.org/web/20261101192136/https://learn.unity.com/tutorial/introduction-to-unity-cli, anterior à atualização de 12/11. Título conferido no `<title>`: "Introduction to Unity CLI - Unity Learn". Lidos os seis passos inteiros; as imagens, o vídeo do passo 2 e os artigos ligados ("A Beginner's Guide to Unity CLI and the Pipeline Package" e o "full article" da troca do MCP) não foram abertos.

**Conferência lado a lado** (2026-11-13, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra `unity-learn-intro-unity-cli.txt` (o texto do bloco, na cópia de trabalho), com 45 unidades medidas (19 de prosa, 26 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas. Na leitura lado a lado, segue a fonte a unidade que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela, e conta como unidade que segue a fonte a célula que o script partiu em pedaços da mesma frase: 29 de 37 unidades do corpo (de "Em uma frase" em diante), 29 de 45 com as 8 do cabeçalho de proveniência, que não tratam do conteúdo. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 26, dos passos 1 a 5: a página é técnica e lista fatos, e a ficha segue a ordem dela pela exceção do item 2; o pouco de texto argumentativo do tutorial (o gargalo da interface no passo 1, a comparação com o MCP) está em células soltas, sem duas seguidas. Na revisão de 2026-11-19, o parágrafo de segurança do passo 3, que vertia na ordem as quatro frases do aviso da página, foi refeito a partir da analogia do assistente, com o `eval` no meio e o uso local por último (as frases da fonte na ordem 4, 1 e 2, 3), e a célula da ressalva do passo 5 abre pelo que não funciona; no parágrafo, a maior sequência de unidades na ordem da fonte é de 2, e a célula da ressalva inverte as duas metades da nota.

## Em uma frase

Tutorial oficial que apresenta o Unity CLI, um programa de linha de comando que gerencia versões, projetos e licenças da Unity, e o pacote Unity Pipeline, que deixa o Editor aberto como servidor HTTP local para o terminal ou um agente de IA mandarem comandos, rodarem C# pelo `eval` e se ligarem por MCP.

## Passo 1. O que é o Unity CLI

| Item | Fato |
|---|---|
| O problema que a página aponta | a interface do Editor vira gargalo em tarefa repetitiva, automação e fluxo com agente; o agente que navega por cliques precisa de uma camada de interpretação visual que erra, é lenta e gasta tokens |
| O que o CLI é | um binário autocontido, sem interface gráfica, que conversa com a Unity pelo terminal |
| Versão na hora em que foi escrito | Unity CLI `1.0.0-beta.17` com `com.unity.pipeline` `0.10.0-exp.1` |
| Aviso | recursos novos entram com frequência; diante de problema, a documentação do CLI |
| O CLI sozinho | prepara o ambiente: instala editores e módulos, gerencia licenças |
| O pacote Pipeline (`com.unity.pipeline`) | transforma o Editor aberto num servidor HTTP local |
| Efeito do Editor aberto | cenas e base de assets ficam carregadas na memória, sem o custo de abrir o motor a frio |
| Recompilação de script | o servidor do pacote trata a compilação de forma assíncrona; a conexão não cai durante o recarregamento do domínio |
| `eval` | compila o trecho de C# na hora e o põe na thread principal da Unity, sem recompilar o projeto nem recarregar o domínio; a resposta volta em milissegundos |
| O MCP oficial | a página diz que o suporte a MCP não sai, e que o CLI e o pacote cobrem os mesmos casos de uso, e mais, com mais velocidade |

## Passo 2. Instalar e conferir

| Item | Fato |
|---|---|
| Instalação pelo Unity Hub | automática nas versões mais recentes |
| Instalação pelo terminal no Windows | `irm https://unity.com/install.ps1 \| iex` (PowerShell) |
| Instalação no macOS e no Linux | `curl -fsSL https://unity.com/install.sh \| bash` |
| Instalar o pacote Pipeline | `unity pipeline install` |
| Conferir | `unity status`: diz se o Editor está pronto, a porta (7800 no exemplo), o caminho do projeto, a versão do Editor (6000.6.0b7 no exemplo) e o identificador do processo |
| Autenticar | `unity auth login`, que abre o navegador para entrar na conta Unity e guarda a credencial no chaveiro do sistema |
| Comandos que usam a credencial | `unity projects`, `unity build`, `unity license`, `unity cloud` |

## Passo 3. Os primeiros comandos

| Item | Fato |
|---|---|
| Ajuda | `unity --help` ou `unity -h`, e `--help` em qualquer nível de subcomando (`unity auth --help`, `unity auth login --help`) |
| Leitura de um comando | o programa (`unity`), os subcomandos como verbos (`auth login`) e as opções como modificadores (`--non-interactive`, que entra pelo terminal sem abrir o navegador) |
| Opção curta e longa | um traço para o atalho, dois para o nome inteiro |
| Versões disponíveis | `unity releases`, com filtros em `unity releases --help` |
| Instalar uma versão | `unity install` (escolha numa lista) ou `unity install 6000.5.9f1` (versão dada) |
| Versão citada como beta na hora | Unity 6.6b7, com a b9 instalada no exemplo |
| Abrir o projeto em outra versão | `unity open --editor-version 6000.6.0b9`, que equivale a escolher outra versão no Hub e atualizar o projeto |
| Listar os comandos do Editor | `unity command` sem argumento lista os grupos; com o grupo (`unity command script`), os comandos e as opções de cada um |
| Exemplos de comandos embutidos | `script eval`, `animation.animator add_layer`, `build run`, `asset find` |
| Quantos são | "hundreds" num trecho e "140+" em outro |
| Exemplo de `eval` | `unity command script eval --code 'Debug.Log("hello from unity cli");'`, que devolve um JSON com `"success": true` e escreve no Console do Editor |

**Segurança, pela página:** entregar o CLI a um agente equivale a abrir o computador a um assistente, que passa a poder tudo o que o usuário pode; o ponto mais sensível é o `eval`, que aceita qualquer C# e por isso fica atrás de uma chave de acesso de cada projeto, e que a página põe na conta da execução remota de código, restrito ao desenvolvimento local. Esse é, aliás, o único uso para o qual o CLI e o pacote foram feitos: jogo publicado fica de fora, e, se ninguém mudar o padrão, nada sai da máquina.

## Passo 4. Ligar o modelo de linguagem

| Item | Fato |
|---|---|
| Agentes citados | Claude, Codex, Copilot, modelos locais |
| Configuração extra | nenhuma, pela página |
| Como ligar | entrar com `cd` na pasta do projeto e abrir o agente ali (`claude`, no exemplo) |
| Teste sugerido | pedir ao agente que rode `unity command` no bash, diga o que ele faz e teste um `eval` |
| O MCP antigo | descontinuado no pacote `com.unity.ai.assistant` e trocado pelo servidor MCP do CLI (`unity mcp`), sobre o pacote Pipeline, com o mesmo protocolo |
| Para quem fica o MCP | agentes que não rodam comando de shell qualquer ou que montam mal a linha de comando |
| Configurar o MCP | `unity mcp configure claude` (ou `cursor`, `vscode`); `unity mcp configure --list` para os clientes aceitos |
| Teste sugerido pelo MCP | pedir um cubo de 2 × 2 × 2 no centro da cena aberta e um script que o gire nos três eixos a 45 graus por segundo; a página mostra a resposta do Claude Code e manda entrar em Play para ver o cubo girando |

## Passo 5. Comandos próprios

| Item | Fato |
|---|---|
| O que já vem | entrar e sair do Play, recompilar, rodar testes de unidade |
| Como criar um comando | um método estático em C# com os atributos `[CliCommand]` e `[CliArg]`, numa classe estática, com o namespace `Unity.Pipeline.Commands` |
| Registro | nenhum: o pacote acha os atributos ao compilar, e `unity command` lista os comandos próprios junto dos embutidos |
| Ressalva | pela nota, comando com parâmetro não recebe opções no estilo do CLI: o método se chama direto, em C#, pelo `unity command script eval`; o atributo `[CliCommand]` serve para o comando aparecer na lista e poder ser chamado |
| Exemplo sem parâmetro | `unity command hello-world` |
| Exemplo com parâmetro | `[CliArg("name", "Who to greet")]` e `unity command hello-world --name "thomas"` |

Na página, a nota do passo 5 diz que parâmetros vão pelo `script eval`, e o exemplo que vem logo depois passa `--name` como opção.

## Passo 6. O plugin de agente da Unity

| Item | Fato |
|---|---|
| O que é | plugin oficial de desenvolvimento de jogos para agentes |
| Agentes, pelo plugin | Claude Code, Codex e Grok, na hora em que foi escrito |
| Agentes, pelo CLI | `unity setup claude` (ou `codex`, `grok`, `copilot`, `antigravity`, `qwen`, `vscode`, `opencode`); `unity setup all` para todos |
| Instalar no Claude Code | `claude plugin marketplace add Unity-Technologies/unity-agent-plugin` (repositório `github.com/Unity-Technologies/unity-agent-plugin`) |
| Dica para projeto novo | rodar `/init` no Claude Code para criar o `CLAUDE.md` com o contexto do projeto (exemplos da página: uGUI ou UI Toolkit, Input System novo ou antigo, service locator ou singleton, MVP na interface) |

## O que a fonte recomenda

Instalar o CLI e o pacote Pipeline, conferir com `unity status`, aprender os comandos pelo `--help` e pelo `unity command`, e ligar o agente abrindo-o na pasta do projeto, com o `unity mcp` só para o agente que não roda shell. O `eval` é o atalho mais rápido e o mais perigoso: fica no desenvolvimento local, atrás da chave do projeto, e o que se dá ao agente é o que ele poderá fazer na máquina.

## Citações

- "This Unity Pipeline package essentially turns your running Editor into a local HTTP server."
- "eval executes arbitrary C# and is gated by a per-project access key."
- "Unity has deprecated the in-Editor MCP server in the com.unity.ai.assistant package."

## Lacuna

O tutorial não diz se o CLI roda sem placa de vídeo, se grava vídeo, nem se o Editor dirigido por ele precisa de janela aberta; não fala do Recorder nem do Timeline. Não dá a lista dos comandos, só exemplos, e as contagens divergem ("hundreds" e "140+"). Não diz o preço nem a licença do CLI, nem em que versão da Unity o pacote Pipeline entra (o JSON-LD diz que o tutorial cobre da 6.0 à 6.4, e o exemplo roda numa 6.6 beta). As imagens e o vídeo, que mostram as respostas, não foram vistos.
