---
titulo: "Unreal MCP in Unreal Editor"
tipo: artigo
autor: "Epic Games (documentação oficial do Unreal Engine)"   # a página não tem assinatura de pessoa
url: "https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor"
publicado_em: null   # sem data visível; o título diz "Unreal Engine 5.9 Documentation"; o HTML tem carimbos created_at 2026-11-09 e updated_at 2026-11-10 de um bloco, que datam o bloco, não a página
capturado_em: 2026-11-13
licenca: "protegido (documentação da Epic Games; nenhum aviso de direitos nem licença de conteúdo no HTML baixado, cujo rodapé é montado no navegador; tratada como protegida); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unreal-engine, mcp, claude-code, agentic-workflows, editor-scripting, python, sequencer, security]
---

# Unreal MCP: o servidor MCP oficial dentro do Unreal Editor, experimental

Nota de fato: tabelas do que a página da documentação diz sobre o plugin Unreal MCP, uma seção por parte da página, na ordem dela, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida, e o código e os exemplos de configuração dela não se copiam aqui, só se descrevem. É fonte técnica longa que lista fatos (o que cada ajuste, comando e ferramenta faz), então as seções e as linhas seguem a ordem da página, sem reordenar (o `README.md` desta pasta, item 2, e Passo 7, item 1, da `research`); a medida da cópia é a do `parafrase.py` e a da conta lado a lado, com a maior sequência declarada.

**Proveniência.** Página de dev.epicgames.com, baixada com `curl` em 13/11/2026 e lida no texto do bloco `<article>` (4.645 palavras, do aviso de recurso experimental ao "See Also"), conferido no HTML; sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco, não do arquivo HTML); Wayback http://web.archive.org/web/20261017025042/https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor, anterior à versão lida. Título conferido no `<title>`: "Unreal MCP in Unreal Editor | Unreal Engine 5.9 Documentation". Lida a página inteira; os blocos de código recolhidos ("Expand code") aparecem só nas primeiras linhas no texto extraído, e as páginas ligadas ("Run External AI Agents in the Unreal Assistant Panel", "Using Python with AI Agents", a especificação do MCP) não foram abertas.

**Conferência lado a lado** (2026-11-13, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra `epic-unreal-mcp-doc.txt` (o texto do bloco, na cópia de trabalho), com 96 unidades medidas (19 de prosa, 77 de célula com texto), 2 coladas, que são listas de nomes em inglês (os clientes do Client Selection; os transportes), fatos sem outra grafia, e 0 trechos de 3 ou mais seguidas. Na leitura lado a lado, segue a fonte a unidade que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela, e conta como unidade que segue a fonte a célula que o script partiu em pedaços da mesma frase: 81 de 87 unidades do corpo (de "Em uma frase" em diante), 81 de 96 com as 9 do cabeçalho de proveniência, que não tratam do conteúdo. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 81, de "O que é" a "Limites conhecidos": a página é técnica e lista fatos, e a ficha segue a ordem dela pela exceção do item 2; não há texto argumentativo do autor na página.

## Em uma frase

O Unreal MCP é um plugin experimental que põe um servidor MCP dentro do processo do Unreal Editor, ouvindo só na própria máquina (por padrão em `http://127.0.0.1:8000/mcp`) e sem autenticação, para que um agente como o Claude Code controle o Editor pelas ferramentas que o motor expõe, inclusive as de Sequencer, e pelas que se escrevem em Python ou C++.

## O que é

| Item | Fato |
|---|---|
| Estado | experimental: recursos em desenvolvimento, APIs e formatos podem mudar; cuidado ao publicar projeto com ele |
| Onde roda | dentro do processo do Unreal Editor, por conexão HTTP local |
| Agentes citados | Claude Code, Codex, Cursor, Gemini CLI, Visual Studio Code com GitHub Copilot, MCP Inspector |
| O que expõe como ferramentas | criar e editar atores; montar Blueprints e Widget Blueprints; criar materiais, MetaSounds, PCG, Niagara e conteúdo de Sequencer; inspecionar widgets Slate; medir desempenho; rodar testes automáticos |
| Ferramentas próprias | dá para acrescentar |

## O protocolo

| Item | Fato |
|---|---|
| Especificação | aberta, em modelcontextprotocol.io |
| Mensagens | um conjunto pequeno de JSON-RPC (`initialize`, `tools/list`, `tools/call` e afins) |
| Tools | funções com nome e parâmetros e retornos tipados |
| Resources | dados só de leitura, por URI |
| Prompts | modelos de prompt reaproveitáveis |
| O que o Unreal MCP oferece | Tools (dos toolsets do Toolset Registry) e Resources; aceita qualquer cliente MCP |
| O que não oferece | Prompts |

## Preparar

| Item | Fato |
|---|---|
| Dois caminhos | o agente num terminal (o do sistema ou o do plugin Terminal do Editor), ou no painel Unreal Assistant; as ferramentas são as mesmas |
| Terminal, para quem | quem usa cliente que o painel não aceita, prefere a própria IDE ou terminal, ou quer ligar o agente a mais de um Editor |
| Painel, para quem | quem quer o jeito mais rápido sem sair do Editor; dispensa arquivo de configuração; aceita Claude Code, Codex, Cursor, OpenCode e agentes ACP próprios; um Editor por vez |
| Os passos | ligar os plugins; conferir que o servidor roda; abrir o agente; instruções do servidor (opcional); testar |
| Plugins | Unreal MCP (ligado por padrão) e All Toolsets, em Edit > Plugins, com reinício do Editor; os dois dependem do Toolset Registry, que se liga sozinho |
| All Toolsets | carrega todos os toolsets padrão; para expor só alguns, ligar os plugins de cada um |
| Início automático | ligado por padrão: o servidor sobe com o Editor e escuta em `http://127.0.0.1:8000/mcp` |
| Onde conferir | Edit > Editor Preferences > Agentic Workflows > Model Context Protocol > Auto Start Server; ali também a porta (8000) e o caminho (`/mcp`) |
| Subir à mão | `ModelContextProtocol.StartServer`, com a porta opcional, no console do Editor |
| Commandlet | não sobe o servidor sozinho; `-ModelContextProtocolStartServer` o sobe |
| Editor aberto pelo próprio agente | abrir com `-ModelContextProtocolPort=<porta>` para não brigar com o Editor do usuário ou de outro agente |

## O agente pelo terminal

| Item | Fato |
|---|---|
| Arquivo de configuração | o plugin o gera: Editor Preferences > Model Context Protocol > MCP Client > Client Selection (padrão: Claude Code) > Generate Client Config |
| Onde sai o `.mcp.json` | na raiz do projeto, no motor instalado; na raiz do motor, no motor compilado do código (aí, copiar a entrada para o projeto se o agente abre de lá) |
| O que ele contém, no Claude Code | uma entrada `unreal-mcp` do tipo `http` com a URL do servidor |
| Pelo console | `ModelContextProtocol.GenerateClientConfig <Client>`, com `ClaudeCode`, `Cursor`, `VSCode`, `Gemini`, `Codex` ou `All` |
| Gerar de novo | não apaga outras entradas: nos JSON (Claude Code, Cursor, VS Code, Gemini), funde e atualiza a porta; o TOML do Codex só se escreve uma vez, e com o arquivo existente o plugin registra erro e a entrada se edita à mão |
| Ligar | abrir o agente na pasta do arquivo, depois que o Editor e o servidor subiram |
| Se o agente não acha o servidor | abrir da pasta do arquivo, abrir depois do Editor, reconectar |
| Plugin Terminal | painel de terminal dentro do Editor, que roda comandos ao abrir; com ele, o fluxo inteiro fica numa janela |
| Comandos de abertura do Terminal | nesta ordem: o tipo de terminal (`TERM=xterm-256color`), o `cd` para a pasta do `.mcp.json`, e o agente (`claude`) |
| Sem o `TERM` | o agente cai num modo degradado e pode mostrar sequências de escape cruas |
| Por que o `cd` | o Terminal abre em `FPaths::RootDir()`, que é a raiz do código no motor compilado e a pasta do motor no instalado |

## O agente no painel, as instruções e o teste

| Item | Fato |
|---|---|
| Painel Unreal Assistant | roda Claude Code, Codex, Cursor, OpenCode ou agente ACP dentro do Editor e o liga ao servidor deste Editor, sem arquivo de configuração |
| Instruções do servidor | mandadas a todo agente que se liga: convenções do projeto, pastas que não se mexem, mapa de teste preferido |
| Onde ficam | Editor Preferences (só para o usuário) ou Project Settings, guardadas no `DefaultGame.ini` (para todos do projeto) |
| Depois de mudar | o cliente reconecta |
| Testes sugeridos | perguntar que atores estão selecionados, o que o agente faz no Unreal, que toolsets há; pedir uma luz pontual branca quente acima do ator selecionado |
| Ressalva | o resultado varia com o agente |

## Como funciona

| Item | Fato |
|---|---|
| De onde vêm as ferramentas | do Toolset Registry, um subsistema do plugin de mesmo nome |
| Toolset | classe que implementa `IToolsetProvider` e expõe funções como ferramentas; em geral deriva de `UToolsetDefinition` (C++) ou `unreal.ToolsetDefinition` (Python) |
| Sem classe extra | subsistemas do Editor e bibliotecas de Blueprint podem implementar a interface; exemplos: `LevelSequenceEditorSubsystem`, `PCGEditorSubsystem`, `WidgetBlueprintEditorSubsystem` |
| Registro | o C++ ao subir o módulo; o Python pelo `init_unreal.py` do plugin |
| Alcance | cada ferramenta vira ferramenta MCP para todo cliente ligado; outros recursos de IA do motor usam o mesmo registro |
| Nomes | qualificados: `<Plugin>.<Classe>` sem o U no C++ (`GASToolsets.AttributeSetToolset`), o caminho do módulo no Python (`geometry_toolset.geometry_ops.GeometryTools`); sem a busca de ferramentas, listados como `<Toolset>.<Tool>` |

**A busca de ferramentas (tool search),** ligada por padrão (`bEnableToolSearch = true`), faz o `tools/list` devolver quatro meta-ferramentas em vez de todas:

| Meta-ferramenta | O que devolve ou faz |
|---|---|
| `list_toolsets` | os nomes e as descrições dos toolsets |
| `describe_toolsets` | as ferramentas de um ou mais toolsets, com nome, descrição e anotações; os esquemas com `include_schemas: true` |
| `describe_tools` | os esquemas completos de ferramentas dadas como `Toolset.Tool`, com erro para nome desconhecido |
| `call_tool` | chama a ferramenta com os argumentos e devolve o resultado no mesmo turno |

| Item | Fato |
|---|---|
| Por que a busca | mantém pequena a resposta do `tools/list` mesmo com centenas de ferramentas |
| Desligada | lista tudo de saída, e a primeira resposta fica bem maior |
| Aviso | não contar com a lista inteira de saída: a maioria dos agentes recebe as meta-ferramentas |
| Módulos | `ModelContextProtocol` e `ModelContextProtocolEngine` (de execução: servidor, protocolo, ajustes, comandos de console); `ModelContextProtocolEditor` (só de Editor: o início automático); o adaptador do registro e a busca ficam no `ModelContextProtocol` |
| Nome interno | `ModelContextProtocol` no código, nos `.uplugin` e nos comandos; Unreal MCP na janela de plugins e na documentação |

## Como o servidor roda: segurança

| Item | Fato |
|---|---|
| Processo | dentro do Editor |
| Conexões | por padrão, só da mesma máquina; sem autenticação; não feito para uso remoto |
| Cabeçalho Origin | conferido contra uma lista: localhost, 127.0.0.1 e [::1], mais as origens acrescentadas; barra o ataque de DNS rebinding a partir de página web |
| Origem acrescentada | cada uma aumenta a exposição |
| Sem autenticação, quem chama | qualquer processo local, ou qualquer página servida de uma origem permitida |
| Execução | uma chamada de ferramenta por vez, na thread do jogo; o cliente não deve mandar chamadas sobrepostas |

## Estender

| Caminho | Para quê |
|---|---|
| Toolsets | o jeito recomendado, em Python ou C++, registrado no Toolset Registry; serve a quase todo caso |
| Registro direto | ferramenta cujo esquema só se sabe em execução, que aparece e some, ou que depende de dado fora do sistema de tipos: implementar `IModelContextProtocolTool` e registrar com `AddTool()` (e tirar com `RemoveTool()`) |
| Skills de agente | conjuntos de instruções com nome, carregados quando o agente precisa do conhecimento de um fluxo |
| Resources | dados só de leitura por URI |

| Toolset em Python ou C++ | Fato |
|---|---|
| Atalho no Claude Code | a skill `create-toolset` do plugin `unreal-mcp` para Claude Code escreve o esqueleto, nas duas linguagens |
| Quando o C++ | função do motor fora do Python; assinatura com `USTRUCT` ou tipo refletido que a dica de tipo do Python não expressa bem; ferramenta chamada tanto que a travessia entre Python e motor pesa; ferramenta que precisa rodar em build empacotado |
| Boas práticas | cada ferramenta pequena e de uma tarefa; nomes descritivos e retornos estruturados (viram JSON Schema com tipo e descrição por campo), em vez de texto livre |
| Em Python | classe derivada de `unreal.ToolsetDefinition`, ferramentas com `@toolset_registry.tool_call` e `@staticmethod`, registro no `init_unreal.py` do plugin |
| Em C++ | classe derivada de `UToolsetDefinition`, marcada `UCLASS(BlueprintType, Hidden)`, funções `UFUNCTION(meta = (AICallable))`, registro com `UToolsetRegistry::RegisterToolsetClass()` ao subir o módulo; os comentários de documentação entram no esquema |
| Exemplo em C++ | `UAttributeSetToolset`, no plugin experimental GASToolsets (desligado por padrão) |

| Metadado | O que faz |
|---|---|
| `AICallable` | marca a função como ferramenta |
| `AIRuntimeCallable` | ferramenta que também pode rodar em build empacotado; só estas entram no manifesto de execução |
| `AIAccessMode` | `Read`, `Write` ou `Execute`; vai ao cliente como modo de acesso e como `readOnlyHint`, para ele decidir se pede confirmação; o padrão é `Execute`, por isso a página manda pôr em toda ferramenta (no Python, `mode=unreal.ToolAccessMode.<Modo>`) |
| `AIIgnore` | tira a função da lista de ferramentas |
| Ferramenta sobre um objeto | `UsesInstanceDispatch()` (o registro acha um objeto só, como um subsistema) ou `UsesInstanceArgument()` (cada ferramenta recebe o argumento reservado `instance`); uma das duas por classe |
| Atualizar depois de mudar | `ModelContextProtocol.RefreshTools`, e o cliente pode ter de reconectar; no C++, o Live Coding pega mudança no corpo da função, mas `UFUNCTION` nova pede reiniciar o Editor; no Python, recarregar o módulo e rodar o `RefreshTools` |

| Skills de agente | Fato |
|---|---|
| Em Python | classe derivada de `unreal.AgentSkill`, com `@agent_skill` (o exemplo é uma skill de pôr atores no chão) |
| Em C++ | classe derivada de `UAgentSkill`, achada pelo Asset Registry; dá para criar e editar em execução com `CreateSkill` e `UpdateSkill` |
| Em Markdown | uma pasta com `SKILL.md`, com nome e descrição no frontmatter e as instruções depois |
| Onde o registro procura | `<Plugin>/Skills/` de cada plugin ligado, `<Project>/Skills/`, `Engine/Extras/AgentTools/Skills/`, e o que o C++ acrescentar com `AddSearchRoot` |
| Chave da skill | `/Skills/<Plugin>/<pasta>` ou `/Skills/Project/<pasta>`, passada a `AgentSkillToolset.GetSkills`; os links relativos do `SKILL.md` viram absolutos |
| Resources | implementar `IModelContextProtocolResourceProvider` e registrar com `AddResourceProvider()`; o motor não traz nenhum provedor |

**Fora do Editor:** um jogo empacotado, inclusive Shipping, pode hospedar o servidor (por `StartServer()` ao subir ou por `-ModelContextProtocolStartServer`). No Editor, todas as ferramentas `AICallable` valem; no empacotado, só as `AIRuntimeCallable`, do manifesto gerado no build, e a página avisa que o jogo empacotado não é só de leitura. Os toolsets do motor com ferramentas para execução são NavMesh, Scene Capture, Console, Widget Finder, Perf (perfiladores e estatísticas) e Input.

## Depurar

| Ferramenta | Para quê |
|---|---|
| Output Log | o endereço, a porta e o caminho do servidor ao subir; o erro quando não consegue escutar (porta ocupada, plugin faltando) |
| Informação da instância | todo `initialize` traz id da instância, processo, versão do motor, ramo, changelist, nome e pastas do projeto e do motor, para o agente conferir que Editor alcançou; o servidor se chama `unreal-mcp` |
| Categorias de log | `LogModelContextProtocol` (detalhe com `Log LogModelContextProtocol Verbose`) e `LogToolsetRegistry` |
| MCP Inspector | o cliente oficial de depuração: lista as ferramentas com esquema e chama cada uma por formulário, sem agente; abre com `npx @modelcontextprotocol/inspector` e se liga ao servidor por Streamable HTTP |
| Dump Media To Disk | grava as imagens e os áudios que as ferramentas devolvem em `Saved/ModelContextProtocol/` |

## Dicas

| Dica | Fato |
|---|---|
| Mais de um Editor | cada um com o seu servidor, a sua porta e a sua entrada com nome próprio no arquivo do cliente; o `GenerateClientConfig` sempre escreve `unreal-mcp` para o Editor em que roda, e as outras entradas se acrescentam à mão (o exemplo da página liga um Editor na 8000 e outro, chamado `unreal-mcp-5-8`, na 8001) |
| Chamada longa | alguns clientes param de esperar (o Claude Code, depois de cerca de 120 segundos); mandar um `progressToken` em `_meta` para receber sinais de progresso, `notifications/cancelled` para cancelar, e dividir o trabalho longo (Live Coding, script grande, varredura de assets, testes) em chamadas curtas |
| Reiniciar o Editor pelo agente | `ExitEditor` em `EditorToolset.EditorAppToolset`, depois abrir de novo; o cliente reconecta |
| Importar assets | as ferramentas `ImportFile` (som, textura, malha estática e com esqueleto, tabelas) têm `bReplaceExisting` e `bSave`, falsos por padrão; cada uma só substitui asset da própria classe |

## Referência de configuração

| Ajuste (Editor Preferences) | Padrão | O que faz |
|---|---|---|
| Auto Start Server | true | sobe o servidor com o Editor |
| Server Port Number | 8000 | a porta |
| Server URL Path | `/mcp` | o caminho |
| Enable Tool Search | true | o `tools/list` devolve só as quatro meta-ferramentas |
| Additional Allowed Origins | vazio | origens aceitas além de localhost, 127.0.0.1 e [::1]; cada uma aumenta a exposição |
| Dump Media To Disk | false | grava imagem e áudio em `Saved/ModelContextProtocol/` |
| Instructions | vazio | instruções do usuário, mandadas a cada cliente |
| Client Selection | Claude Code | o cliente do botão Generate Client Config: All, Claude Code, Codex, Cursor, Gemini ou VS Code |
| Instructions (Project Settings) | n/a | instruções do projeto, no `DefaultGame.ini` |

| Comando de console | O que faz |
|---|---|
| `ModelContextProtocol.StartServer [porta]` | sobe o servidor |
| `ModelContextProtocol.StopServer` | para o servidor e fecha as sessões |
| `ModelContextProtocol.RefreshTools` | relê os provedores de ferramentas |
| `ModelContextProtocol.GenerateClientConfig <Client\|All>` | gera o arquivo do cliente |

| Argumento de linha de comando | O que faz |
|---|---|
| `-ModelContextProtocolStartServer` | sobe o servidor ao abrir o Editor ou o commandlet, com ou sem o início automático |
| `-ModelContextProtocolPort=N` | troca a porta (1 a 65535); valor inválido volta ao ajuste |

| Variável de console | Tipo e padrão | O que faz |
|---|---|---|
| `ModelContextProtocol.WrapPODToolResultsInObject` | bool, true | embrulha resultado primitivo em `{"result": ...}` |
| `ModelContextProtocol.AudioResultOggFormat` | bool, false | áudio em OGG em vez de WAV |
| `ModelContextProtocol.ProgressIntervalSeconds` | float, 1.0 | intervalo mínimo entre avisos de progresso |
| `ModelContextProtocol.PaginationPageSize` | int32, 0 | itens por página; 0 devolve tudo |
| `ModelContextProtocol.EnableAnalytics` | bool, true | liga ou desliga a telemetria |

## Limites conhecidos

| Limite | Fato |
|---|---|
| Transporte | só Streamable HTTP e SSE; sem stdio nem WebSocket |
| Rede | só a própria máquina por padrão, pelo `DefaultBindAddress` do `[HTTPServer.Listeners]` (127.0.0.1); projeto ou plugin que o ponha em `any` expõe o MCP à rede; sem autenticação, não expor além da máquina |
| Resources e Prompts | nenhum toolset do motor traz Resources; Prompts não existem |
| Build empacotado | só as ferramentas `AIRuntimeCallable` |
| Live Coding | não pega `UFUNCTION` nova; ferramenta nova em C++ pede reiniciar o Editor |

## O que a fonte recomenda

Ligar o Unreal MCP e o All Toolsets, gerar o `.mcp.json` pelo Editor e abrir o agente da pasta dele (ou usar o painel Unreal Assistant), deixar a busca de ferramentas ligada e escrever ferramentas próprias pequenas, com retorno estruturado e o modo de acesso declarado. Como não há autenticação, manter o servidor só na máquina e não acrescentar origens sem necessidade; e, nas chamadas longas, mandar o sinal de progresso ou dividir o trabalho.

## Citações

- "Unreal MCP is Experimental. Many features are still under development and APIs and data formats may change at any time."
- "By default, the server only accepts connections from the same machine, has no authentication layer, and isn't designed for remote use."
- "The MCP server runs tool calls one at a time on the game thread, so clients shouldn't send overlapping tool calls."

## Lacuna

A página não diz em que versão do motor o plugin estreou nem a lista das ferramentas de cada toolset (as de Sequencer e de Movie Render Queue inclusive); não diz se uma ferramenta dispara render nem se o servidor funciona com o Editor sem janela. O exemplo de duas portas nomeia uma entrada `unreal-mcp-5-8`, e o texto não comenta. Não diz quanto o servidor pesa na memória, nem como o agente vê o resultado de uma ação na cena além das imagens que as ferramentas devolvem.
