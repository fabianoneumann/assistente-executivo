---
titulo: "Create custom subagents (Claude Code): documentação completa"
tipo: artigo
autor: "Anthropic"
url: "https://code.claude.com/docs/en/sub-agents.md"
capturado_em: 2026-10-30
licenca: "Documentação: todos os direitos reservados (texto da página Legal and compliance da documentação, registrado em 2026-10-29-claude-code-code-review-documentacao: '© Anthropic PBC. All rights reserved.'; a cópia em markdown lida não traz rodapé); entra só a ficha."
areas: [anthropic-claude, agent-engineering]
tags: [claude-code, subagents, agent-memory, auto-memory, skills, continual-learning, context-management, delegation, tool-permissions, permission-modes, hooks, mcp, model-selection, effort-levels, fork, worktrees, background-tasks, nested-agents, prompt-injection, auto-compaction, prompt-caching, agent-teams]
---

Ficha de estudo, em palavras próprias, da página oficial "Create custom subagents" do Claude Code, lida em markdown em 2026-10-30. Foi lida e completada por pedido da curadoria depois de uma revisão: a primeira versão cobria só duas seções (memória persistente e skills pré-carregadas). A documentação não tem licença aberta, então não há texto integral; citações literais só curtas, e os blocos de código e de configuração da página vão descritos em palavras. As seções abaixo seguem a ordem da página; as versões mínimas citadas vão de v2.1.63 a v2.1.304.

**Os pontos mais pedidos, onde estão:** memória ligada libera Read, Write e Edit automaticamente (seção "Memória persistente"); o que carrega no início do subagente, e que a memória automática da conversa principal não carrega (seção "O que carrega no início"); o fork e como difere dos outros subagentes (seção "Fork da conversa"); os exemplos de subagentes da página, revisor de código, depurador, cientista de dados e validador de consultas (seção "Exemplos de subagentes").

## O que é um subagente

- **Definição:** assistente especializado que cuida de um tipo de tarefa. Serve quando uma tarefa lateral encheria a conversa principal de resultados de busca, logs ou conteúdo de arquivos que não serão consultados de novo: o subagente faz o trabalho no próprio contexto e devolve só o resumo. Vale definir um personalizado quando se cria o mesmo tipo de trabalhador com as mesmas instruções repetidamente.
- **Como roda:** cada subagente tem janela de contexto própria, prompt de sistema próprio, acesso a ferramentas específico e permissões independentes. Faz as próprias requisições, que contam nos **mesmos limites de uso** da conversa principal. Quando uma tarefa casa com a descrição de um subagente, o Claude delega a ele, que trabalha sozinho e devolve o resultado.
- **Fronteira:** subagentes vivem dentro de uma sessão. Para muitas sessões independentes em paralelo, a página aponta os agentes em segundo plano (agent view); para sessões que trocam mensagens, o cross-session messaging; para um time de sessões coordenado, os agent teams.
- **Para que servem**, segundo a página: preservar o contexto (exploração e implementação fora da conversa principal); impor restrições (limitar ferramentas); reusar configurações entre projetos (subagentes de usuário); especializar o comportamento (prompt focado num domínio); controlar custo (mandar tarefas para modelos mais rápidos e baratos, como o Haiku).
- **A descrição decide a delegação:** o Claude usa o campo de descrição para escolher quando delegar, então ela precisa ser clara. As descrições ocupam contexto: quando a soma das descrições dos subagentes (fora os embutidos) passa de **15.000 tokens**, o Claude Code mostra um aviso na abertura com o total. O remédio é encurtar as descrições e mover o detalhe para o prompt de sistema, que só carrega quando o subagente roda.

## Subagentes embutidos

Todos herdam as regras de permissão da conversa-mãe; a maioria roda com um conjunto restrito de ferramentas. **Explore e Plan começam sem os `CLAUDE.md` e sem o retrato do git status**, para a pesquisa ser rápida e barata; os outros embutidos e os personalizados carregam os dois, a menos que o personalizado use `omitClaudeMd`.

| Embutido | Modelo | Ferramentas | Para quê |
| :- | :- | :- | :- |
| **Explore** | o da conversa principal; se a principal roda Fable, com assinatura Claude, conta do Console ou gateway via `ANTHROPIC_BASE_URL`, roda no Opus para onde o alias `opus` aponta; em Bedrock, Agent Platform do Google Cloud, Microsoft Foundry, Claude Platform on AWS ou Claude apps gateway, fica no modelo da principal | só leitura; Write e Edit negados | achar arquivos, buscar código, explorar a base |
| **Plan** | herda da principal, salvo `CLAUDE_CODE_SUBAGENT_MODEL` forçado em todos | só leitura; Write e Edit negados | pesquisa no modo plano, antes de apresentar o plano |
| **General-purpose** | o de `CLAUDE_CODE_SUBAGENT_MODEL`, se definido e nada mais atribuir modelo; senão o da principal | todas as disponíveis a subagentes | pesquisa complexa, operações de vários passos, alteração de código |

- **Explore:** o Claude delega quando precisa entender ou buscar no código sem mudar nada; ao chamar, escolhe a profundidade: **quick** (busca pontual), **medium** (equilíbrio) ou **very thorough** (análise completa). Um subagente de usuário ou de projeto chamado `Explore` substitui o embutido e mantém o próprio campo `model`; a página sugere definir um com `model: haiku` para explorar num modelo mais barato.
- **Plan:** no modo plano, a pesquisa vai para ele para que a saída da exploração fique em outra janela enquanto a conversa principal segue só leitura.
- **General-purpose:** usado quando a tarefa pede explorar e modificar, raciocínio complexo para interpretar resultados, ou vários passos dependentes.
- **Outros auxiliares**, normalmente chamados sozinhos: `claude` (sem modelo próprio, segue a ordem de escolha de modelo; o curinga com todas as ferramentas para quando nenhum especializado serve, e o agente padrão de uma sessão em segundo plano despachada); `statusline-setup` (Sonnet, ao rodar `/statusline`); `claude-code-guide` (Haiku, para perguntas sobre o próprio Claude Code).
- **Como restringir os embutidos:** negar um tipo específico em `permissions.deny`; negar a ferramenta `Agent` inteira para impedir qualquer delegação; `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` remove só Explore e Plan, e o Claude passa a ler e explorar direto (v2.1.198 ou posterior); no modo não interativo e no Agent SDK, `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1` remove todos os embutidos para usar só os seus.
- Uma chamada da ferramenta Agent sem `subagent_type` falha com "subagent_type is required" quando a sessão não tem um `general-purpose` para cair.

## Primeiro subagente, passo a passo

Subagentes são arquivos Markdown com frontmatter YAML. O passo a passo da página cria um subagente de usuário que revisa código e sugere melhorias:

1. **Pedir ao Claude** que crie, descrevendo o que se quer e onde salvar (no exemplo, um "code-improver" pessoal em `~/.claude/agents/`, que varre arquivos e sugere melhorias de legibilidade, desempenho e boas práticas, explicando cada problema com o código atual e uma versão melhorada, só leitura e em Sonnet). O Claude escreve o arquivo com `name`, `description`, lista de `tools`, `model` e o prompt de sistema.
2. **Revisar o arquivo** gerado e conferir o frontmatter. O exemplo resultante tem nome, uma descrição que diz o que faz e "use depois de escrever ou modificar código", ferramentas Read, Grep e Glob, modelo sonnet, e um corpo de duas linhas definindo o papel. Por estar em `~/.claude/agents/`, vale em todo projeto da máquina; para um projeto só, move-se para o `.claude/agents/` dele.
3. **Testar**, pedindo ao Claude que use o subagente. Na transcrição, a delegação aparece como uma linha com o nome do subagente e uma descrição curta da tarefa entre parênteses.

Se o Claude não acha o subagente novo, reiniciar: isso só acontece quando `~/.claude/agents/` não existia no início da sessão, porque uma sessão em andamento não detecta uma pasta `agents` recém-criada. O comando `/agents` hoje só lembra de pedir ao Claude ou editar as pastas; até a v2.1.197 ele abria um assistente interativo com as abas Running (subagentes vivos) e Library (criar, editar, apagar).

## Configurar: escopo e onde o arquivo mora

O lugar do arquivo define quem tem acesso; o frontmatter define o que ele pode fazer. Com nomes repetidos, vale o de prioridade mais alta:

| Local | Escopo | Prioridade | Como criar |
| :- | :- | :- | :- |
| Configurações gerenciadas | a organização | 1 (mais alta) | distribuído pelas managed settings |
| flag `--agents` | a sessão atual | 2 | JSON ao abrir o Claude Code |
| `.claude/agents/` | o projeto | 3 | pedir ao Claude ou criar à mão |
| `~/.claude/agents/` | todos os seus projetos | 4 | pedir ao Claude ou criar à mão |
| pasta `agents/` de plugin | onde o plugin está ligado | 5 (mais baixa) | instalado com o plugin |

- **Projeto:** ideal para o que é específico de uma base de código; a página recomenda pôr no controle de versão para o time usar e melhorar junto. A busca sobe a partir da pasta de trabalho: todo `.claude/agents/` entre ela e a raiz do repositório é lido, e com nomes repetidos vence o mais próximo da pasta de trabalho. Pasta adicionada com `--add-dir` ou `/add-dir` também tem o seu `.claude/agents/` carregado; para compartilhar entre projetos sem isso, usar `~/.claude/agents/` ou um plugin.
- **Usuário:** `~/.claude/agents/`, pessoais, valem em todos os projetos.
- **Subpastas:** `.claude/agents/` e `~/.claude/agents/` são lidas recursivamente, então dá para organizar em `agents/review/`, `agents/research/` etc.; o caminho não afeta a identidade, que vem só do campo `name`. Nomes precisam ser únicos na árvore inteira: dois arquivos com o mesmo nome no mesmo `.claude/agents/` (subpastas incluídas) fazem o Claude Code carregar só um, pela ordem de leitura do sistema de arquivos, sem precedência documentada. O `/doctor` aponta nomes repetidos na mesma pasta e propõe renomear ou remover.
- **Plugin:** também lido recursivamente, mas aqui a subpasta entra no identificador: `agents/review/security.md` no plugin `my-plugin` vira `my-plugin:review:security`.
- **Pela linha de comando:** `--agents` recebe um JSON com várias definições; existem só naquela sessão, sem ir para o disco, úteis para teste rápido ou automação. A página mostra o mesmo exemplo em bash e em PowerShell: dois agentes, um revisor de código sênior (qualidade, segurança e boas práticas; Read, Grep, Glob e Bash; sonnet) e um depurador (analisar erros, achar a causa raiz, propor correção). No modo não interativo, `--agents` aceita também o caminho de um arquivo JSON com o mesmo objeto (v2.1.281 ou posterior); na sessão interativa o caminho é recusado. Cada chave de topo é o nome do agente (não pode começar com `-`); os campos são `prompt` (o prompt de sistema, equivalente ao corpo do arquivo; pode ser vazio desde a v2.1.281, e um agente de `prompt` vazio e sem `memory` escolhido com `--agent` deixa o prompt da sessão como está) e os campos do frontmatter (`description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `mcpServers`, `hooks`, `maxTurns`, `autoCompactWindow`, `skills`, `initialPrompt`, `memory`, `effort`, `background`, `omitClaudeMd`, `isolation`). `color` e `experimental` são ignorados ali, sem erro.
- **Gerenciados:** o administrador põe arquivos Markdown em `.claude/agents/` dentro da pasta de managed settings, no mesmo formato; têm precedência sobre os de projeto e usuário com o mesmo nome.
- **De plugin:** carregam junto com os seus e aparecem no autocompletar do @ pelo nome com escopo. **Por segurança, ignoram `hooks`, `mcpServers` e `permissionMode`.** Quem precisa deles copia o arquivo para `.claude/agents/` ou `~/.claude/agents/`, ou acrescenta regras em `permissions.allow`, sabendo que valem para a sessão toda; o autor do plugin deve pôr hooks em `hooks/hooks.json` e servidores MCP em `.mcp.json` do plugin, que valem sempre que ele está ligado.
- **Para agent teams:** uma definição de subagente pode ser reaproveitada como colega de time (teammate), nomeando o tipo ao pedir; a página de agent teams diz que partes e escopos valem.

## Escrever o arquivo do subagente

- **Formato:** frontmatter YAML de configuração e, depois, o prompt de sistema em Markdown. O exemplo da página é um `code-reviewer` com Read, Glob e Grep em sonnet, cujo corpo pede retorno específico e acionável sobre qualidade, segurança e boas práticas.
- **O que o subagente recebe:** só esse prompt de sistema mais detalhes básicos do ambiente, como a pasta de trabalho; **não recebe o prompt de sistema do Claude Code**.
- **Recarga automática:** o Claude Code observa `~/.claude/agents/` e `.claude/agents/`; ao criar ou editar um arquivo, a mudança é detectada em segundos e a próxima delegação já usa a versão nova, sem reiniciar. Três casos ainda pedem reinício: a primeira definição numa pasta `agents` que não existia no início da sessão; arquivos em `.claude/agents/` de pastas adicionadas por `--add-dir` (não observadas); e sessões abertas com `--disable-slash-commands`, que não observam nada.
- **Anexar texto a todos os prompts de subagente** (modo não interativo): `--append-subagent-system-prompt` acrescenta texto ao fim do prompt de todos os subagentes, aninhados inclusive, menos o fork, que reusa o prompt da conversa (v2.1.205); para texto longo, `--append-subagent-system-prompt-file` (v2.1.261).
- **Pasta de trabalho:** o subagente começa na pasta atual da conversa principal; `cd` não persiste entre chamadas de Bash ou PowerShell e não muda a pasta da conversa principal. Para uma cópia isolada do repositório, `isolation: worktree`.
- **Conferências de isolamento no worktree:** o subagente com worktree roda os comandos dentro dele; comando cuja pasta resolve para o checkout principal (por exemplo, se o worktree foi apagado no meio) falha. A checagem cobre o repositório inteiro de onde o Claude Code foi aberto e, se a própria sessão roda num worktree ligado, também o checkout principal. No Bash há duas checagens a mais sobre o texto do comando: bloqueia o que redireciona o git para o checkout principal e recusa o comando quando não dá para verificar pelo texto que o git fica no worktree (por exemplo, nome de comando calculado em tempo de execução). PowerShell só tem a checagem da pasta; o Monitor passa pelas mesmas que o Bash. Se a própria conversa principal roda isolada num worktree, as mesmas checagens valem para ela e para todo subagente que ela abrir, mesmo sem `isolation: worktree`.

## Referência do frontmatter

Só `name` e `description` são obrigatórios. Nomes de campo compostos usam camelCase e precisam bater exatamente com a tabela: **campo desconhecido é ignorado sem erro**. Para achar um campo com erro de digitação num subagente que carregou, rodar `claude --debug` e procurar "does not recognize or apply" no log em `~/.claude/debug/<id-da-sessão>.txt`; o log cita até cinco campos de topo não reconhecidos, com o nome provável quando um campo válido é parecido (v2.1.296).

| Campo | O que faz |
| :- | :- |
| `name` (obrigatório) | identificador único, até 256 caracteres; os hooks recebem esse valor como `agent_type`; o nome do arquivo não precisa bater; não pode conter `:`, reservado aos identificadores de plugin |
| `description` (obrigatório) | quando o Claude deve delegar a este subagente |
| `tools` | ferramentas permitidas, em texto separado por vírgula ou lista YAML; se omitido, herda todas as disponíveis a subagentes; se nenhuma entrada vira ferramenta, o subagente em geral não sobe e o erro nomeia as entradas; para pré-carregar skills, usar `skills`, não listar `Skill` aqui |
| `disallowedTools` | ferramentas a negar, tiradas da lista herdada ou dada; mesmo formato; entrada com especificador como `Bash(git push *)` ainda tira a ferramenta inteira |
| `model` | `sonnet`, `opus`, `haiku`, `fable`, um ID completo como `claude-opus-5-5`, ou `inherit`; omitido, segue a ordem de escolha de modelo |
| `permissionMode` | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`, ou `manual` como sinônimo de `default`; ignorado em subagente de plugin |
| `maxTurns` | máximo de turnos agênticos antes de parar; ao bater, a saída volta marcada como parcial e o Claude pode retomar (a marcação de parcial é da v2.1.246) |
| `autoCompactWindow` | baixa a janela de autocompactação deste subagente para um número de tokens entre 100.000 e 1.000.000 (v2.1.296) |
| `skills` | skills pré-carregadas no início; entra o conteúdo inteiro, não só a descrição; o subagente ainda pode invocar as não listadas pela ferramenta Skill |
| `mcpServers` | servidores MCP do subagente: nome de um já configurado ou definição embutida com a configuração completa; ignorado em plugin |
| `hooks` | hooks de ciclo de vida só deste subagente; ignorado em plugin |
| `memory` | escopo da memória persistente: `user`, `project` ou `local`; na tabela: "Enables cross-session learning" |
| `background` | `true` mantém em segundo plano mesmo quando o Claude pede para esperar; por padrão os subagentes que o Claude abre da conversa principal já começam em segundo plano |
| `omitClaudeMd` | `true` sobe sem os `CLAUDE.md` de usuário, projeto e local; os de política gerenciada ainda carregam, exceto em subagente gerenciado; para subagente que tira tudo do prompt de delegação; ignorado quando o agente roda como sessão principal via `--agent` ou `agent` (v2.1.271) |
| `effort` | nível de esforço enquanto o subagente está ativo (`low`, `medium`, `high`, `xhigh`, `max`, conforme o modelo); sobrepõe o da sessão, mas não a variável `CLAUDE_CODE_EFFORT_LEVEL` |
| `isolation` | `worktree` roda num worktree git temporário, por padrão ramificado do branch padrão e não do `HEAD` da sessão-mãe; é limpo sozinho se o subagente não muda nada |
| `color` | cor na lista de tarefas e na transcrição: red, blue, green, yellow, purple, orange, pink ou cyan |
| `initialPrompt` | enviado sozinho como primeiro turno do usuário quando o agente roda como sessão principal (`--agent` ou `agent`); comandos e skills são processados; vai antes do prompt que o usuário der; ignorado em plugin |
| `experimental` | mapa de opções experimentais; a chave `cacheTtl` com `5m` ou `1h` escolhe a vida do cache de prompt das requisições deste subagente; outros valores são ignorados, `1h` é ignorado enquanto a assinatura usa créditos de uso, e o campo só é lido de arquivos de subagente (v2.1.248) |

O `cacheTtl` vai dentro do mapa `experimental`, não no topo do frontmatter (a página mostra um `repo-auditor` com `cacheTtl: 1h`).

### Arquivos que o Claude Code pula

Num `agents` de projeto, usuário, gerenciado ou de pasta adicionada, o arquivo é pulado **sem aviso na sessão** quando: não tem `name` (tratado como documentação ao lado dos agentes); o `---` de abertura não está na primeira linha (lido como sem frontmatter, também documentação); o `name` começa com `-`, contém `:` ou passa de 256 caracteres (erro no log de depuração); tem `name` mas não `description` (motivo no log); o YAML não faz parse (nenhum campo lido, erro de parse no log). O log aparece com `--debug`. Subagente de plugin sem `name` ou com YAML quebrado ainda carrega, com o nome do arquivo. Para conferir antes de abrir a sessão, `claude plugin validate` contra a pasta (`.claude/agents` ou `~/.claude/agents`) acha frontmatter que não faz parse; olha só a pasta indicada e não acusa arquivo sem `name` (v2.1.233).

## Escolher o modelo

- **Valores do campo `model`:** alias (`sonnet`, `opus`, `haiku`, `fable`), ID completo (os mesmos valores da flag `--model`) ou `inherit` (o modelo da conversa principal).
- **Por chamada:** o Claude pode passar um `model` só para aquela chamada da ferramenta Agent, e ali só aceita alias, nem ID completo nem `inherit`.
- **Ordem de resolução:** (1) o parâmetro da chamada; (2) o `model` do frontmatter, com `inherit` dando o da principal; (3) a variável `CLAUDE_CODE_SUBAGENT_MODEL`, quando aponta um alias ou ID; (4) o modelo da conversa principal. Um mod instalado que define modelo no hook `agent.spawn` toma o lugar do parâmetro da chamada. Antes da v2.1.251 a variável vinha primeiro e passava por cima do parâmetro e do frontmatter, `inherit` inclusive.
- **Quando o alias de família vira o modelo da principal:** se a principal é da mesma família, o subagente roda no modelo exato dela, inclusive com o sufixo `[1m]`, ganhando a mesma janela estendida; e, fora da API da Anthropic, quando o Claude Code não consegue saber a família da principal (por exemplo, um ARN de perfil de inferência no Bedrock não resolvido), só para o alias `opus` e só se `ANTHROPIC_DEFAULT_OPUS_MODEL` não estiver definido. Um alias em `CLAUDE_CODE_SUBAGENT_MODEL` sempre resolve para a versão do alias; a variável igual a `inherit` é o mesmo que não definida; e ela sozinha não muda Explore e Plan.
- **Lista de modelos permitidos da organização (`availableModels`):** parâmetro, frontmatter e variável são conferidos contra ela. Alias de família bloqueado roda na versão mais nova da família que a lista permite (antes da v2.1.222, rodava no modelo herdado); qualquer outro valor bloqueado, ou provedor sem essa substituição, ou família sem versão permitida, roda no modelo herdado, tentando antes `CLAUDE_CODE_SUBAGENT_MODEL` se definida. Na sessão interativa aparece um aviso com o modelo pedido e o usado.
- **Conferir:** `/tasks` mostra o modelo na linha do subagente e o esforço definido para ele (v2.1.242). O `model` passado na chamada continua valendo quando o subagente é retomado ou recebe mensagem.
- **Pensamento estendido:** desde a v2.1.198, o subagente herda a configuração da conversa principal (ligado se ela está ligada); não há ajuste por subagente. Antes, os subagentes rodavam sempre sem pensamento estendido.

### Rodar todos os subagentes num modelo só

`CLAUDE_CODE_SUBAGENT_MODEL` é só um padrão; para impor um modelo a todo subagente, colega de time e agente de workflow, definir também `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` (v2.1.257). Com as duas, todos rodam no modelo da primeira; só com a de forçar, rodam no modelo da principal, menos o Explore, que fica no modelo listado para ele. O exemplo da página põe as duas no bloco `env` de um arquivo de settings, com Haiku; confere-se com `/tasks` durante a execução. Com a de forçar ligada, o `model` das definições é ignorado e o Claude não pode passar modelo na chamada; ainda rodam no modelo da principal o fork e a skill que roda num subagente com `model: inherit`.

## Escolher o nível de esforço

O campo `effort` dá ao subagente o próprio nível. Quando se pede ao Claude um esforço específico para um subagente que não é fork, ele pode passar `effort` na chamada, que sobrepõe o campo e continua valendo ao retomar (v2.1.292). A variável `CLAUDE_CODE_EFFORT_LEVEL` vale mais que os dois.

## Controlar o que o subagente pode fazer

### Ferramentas disponíveis

O subagente herda as ferramentas embutidas e as de MCP da conversa principal, com dois filtros; o fork pula os dois e recebe exatamente o conjunto da principal. No macOS, Linux e WSL, o subagente pode ganhar Glob e Grep mesmo quando a principal não os tem.

- **Primeiro filtro, para todo subagente** (mesmo se listadas em `tools`): `Agent` quando o subagente está no limite de profundidade (no fork ela continua listada, mas devolve erro em vez de abrir outro); `AskUserQuestion`; `EndConversation` (só encerra a conversa principal); `EnterPlanMode`; `ExitPlanMode`, salvo com `permissionMode: plan`; `ScheduleWakeup`; `WaitForMcpServers`; `Workflow`.
- **Segundo filtro, para subagente em segundo plano (o padrão):** mantém todas as ferramentas MCP, mas das embutidas só Read, Grep, Glob, LSP, Bash, PowerShell, Edit, Write, NotebookEdit, WebFetch, WebSearch, TodoWrite, Skill, ToolSearch, EnterWorktree, ExitWorktree, Monitor, TaskStop, SendMessage e Artifact, mais SubagentHandback para o subagente que reporta por ela (Agent e ExitPlanMode seguem o primeiro filtro). As demais embutidas saem, herdadas ou listadas, então **a mesma definição pode resolver para ferramentas diferentes na frente e em segundo plano**; a remoção não dá erro, a menos que deixe `tools` vazio. Antes da v2.1.280, o segundo plano não tinha LSP.
- `ListAgents` segue os filtros: o subagente em primeiro plano herda quando o cross-session messaging está ligado; o de segundo plano não.
- Colegas de agent teams mantêm também as ferramentas de tarefa e de cron (TaskCreate, TaskGet, TaskList, TaskUpdate, CronCreate, CronDelete, CronList). Numa sessão sem as ferramentas de Task, os subagentes também não as recebem, mesmo com outro modelo.

### Restringir as ferramentas

- `tools` é lista de permitidas; `disallowedTools`, de negadas. Com as duas, aplica-se primeiro a negação e depois resolve-se `tools` contra o que sobrou; ferramenta nas duas sai.
- Exemplos da página, em palavras: um `safe-researcher` só com Read, Grep, Glob e Bash (não edita, não escreve, sem MCP); um `no-writes` que herda tudo menos Write e Edit (mantém Bash, MCP e o resto).
- Se nada em `tools` vira ferramenta (tudo com erro de grafia ou indisponível a subagentes), o Claude Code em geral se recusa a subir o subagente, e o erro nomeia as entradas.
- **Servidor MCP inteiro:** em `tools`, `mcp__github__*` dá todas as ferramentas de um servidor; em `disallowedTools`, `mcp__github` ou `mcp__github__*` tira um servidor, e `mcp__*` tira todo MCP. O exemplo `local-only` tira o servidor github e mantém o resto.
- **Negar comandos específicos:** entrada com especificador em `disallowedTools` tira a ferramenta inteira; para manter o Bash e bloquear só certos comandos, usar uma regra de negação do Bash em `permissions.deny` nas settings, que vale para a principal e para os subagentes.
- **Servidor com `__` no nome** (como `reports__v2`): em `tools`, escrever `mcp__` mais o nome inteiro mais `__*` (`mcp__reports__v2__*`), porque sem o `__*` final nada casa; em `disallowedTools`, `mcp__reports` ou `mcp__reports__*` negam também todas as ferramentas de `reports__v2`, que começam com o mesmo prefixo, então para negar só o `reports` é preciso listar as ferramentas uma a uma.

### Restringir quais subagentes podem ser abertos

Quando um agente roda como linha principal com `claude --agent`, ele abre subagentes pela ferramenta Agent, e `Agent(tipo1, tipo2)` em `tools` vira lista de permitidos (o exemplo é um `coordinator` que só pode abrir `worker` e `researcher`): pedido de outro tipo falha e o agente vê só os tipos permitidos no prompt. `Agent` sem parênteses libera qualquer um; sem `Agent` na lista, não abre nenhum. Para bloquear alguns e liberar o resto, usar `permissions.deny`. Essa sintaxe só vale para o agente principal; numa definição de subagente, `Agent` em `tools` deixa ele abrir subagentes até o limite de profundidade, e a lista entre parênteses é ignorada. Na v2.1.63 a ferramenta Task virou Agent; referências `Task(...)` continuam valendo como sinônimo.

### Servidores MCP só do subagente

- `mcpServers` dá ao subagente servidores que a conversa principal não tem. Definições embutidas conectam quando o subagente começa (sujeitas à regra de confiança abaixo) e desconectam quando ele termina; referências por nome compartilham a conexão da sessão-mãe.
- Vale nos dois contextos em que um arquivo de agente roda: como subagente (pela ferramenta Agent ou por @) e como sessão principal (`--agent` ou `agent`). Como sessão principal, os embutidos conectam na abertura junto com os do `.mcp.json`; no `/mcp`, um servidor remoto já usado pode aparecer como `cached` e só conectar na primeira chamada.
- O exemplo é um `browser-tester` com um servidor Playwright definido ali mesmo (stdio, via npx) e uma referência ao `github` já configurado, com o corpo pedindo para navegar, capturar tela e interagir com páginas. As definições embutidas seguem o esquema do `.mcp.json` e aceitam os tipos stdio, http, sse e ws.
- **Dica de contexto:** para manter um servidor fora da conversa principal e não gastar contexto com as descrições das ferramentas dele, defini-lo aqui em vez de no `.mcp.json`; o subagente ganha as ferramentas, a principal não.
- As restrições de MCP da sessão principal valem também aqui: `--strict-mcp-config` e `--bare`, a configuração MCP gerenciada da empresa e as políticas `allowedMcpServers` e `deniedMcpServers`. Servidor bloqueado é pulado com aviso. Restrição gerenciada vale para todo subagente; `--strict-mcp-config` não filtra o que se passa embutido via `--agents` ou pela opção `agents` do SDK, por ser entrada explícita de quem chama.

### Confiança exigida para servidor MCP embutido

Servidor embutido num arquivo do `.claude/agents/` do projeto (ou de pasta adicionada) só carrega depois de **confiar na pasta de onde veio o arquivo**; antes da v2.1.238 carregava sem checar. Não contam a confiança de uma pasta-mãe nem a confiança automática que uma sessão `-p` ou do SDK ganha para hooks em settings. Até confiar, todos os servidores embutidos daquele arquivo são pulados, e o log de depuração mostra a chave exata a gravar em `~/.claude.json`. Pasta adicionada de fora do repositório confiável precisa de confiança própria. Carregam sem essa checagem: referência por nome a servidor já configurado, e servidor embutido em arquivo de `~/.claude/agents/`, passado por `--agents` ou pela opção `agents` do SDK, ou vindo das managed settings.

### Modos de permissão

`permissionMode` escolhe o modo do subagente (com os valores de configuração; o modo Manual é `default`). Sem ele, herda o da conversa principal. **O modo da principal decide se o valor é respeitado:**

- principal em `bypassPermissions`, `acceptEdits` ou auto: o subagente roda no mesmo modo e o campo é ignorado. No auto, o classificador avalia as chamadas do subagente com as regras da principal e, quando ele termina, revisa o trabalho e o relatório final antes de entregar;
- principal em `plan`: o subagente fica em modo plano, qualquer que seja o campo, salvo se roda como colega de agent team pelas regras dele; com `dontAsk`, o que o modo plano pediria para aprovar é negado;
- principal em `default` ou `dontAsk`: o subagente roda no modo dado, menos se o valor é `bypassPermissions` (fica no da principal; v2.1.267) ou `auto` sem auto disponível para ele (settings com `disableAutoMode` ou modelo sem suporte).

| Modo | Comportamento |
| :- | :- |
| `default` | Manual: pede permissão |
| `acceptEdits` | aceita sozinho edições e comandos comuns de arquivo na pasta de trabalho ou em `additionalDirectories` |
| `auto` | um classificador em segundo plano revisa comandos e escritas em pastas protegidas |
| `dontAsk` | nega sozinho o que pediria permissão (um mod instalado ainda pode aprovar algumas); ferramentas liberadas explicitamente funcionam; `AskUserQuestion`, ferramentas MCP marcadas `requiresUserInteraction`, leitura de caminhos de rede e conectores que a organização pôs em `ask` são negados mesmo liberados |
| `bypassPermissions` | pula os pedidos de permissão; o subagente só roda assim quando a principal roda |
| `plan` | modo plano, exploração só leitura |

### Skills pré-carregadas

- O campo `skills` injeta o conteúdo **inteiro** de cada skill listada no contexto do subagente ao iniciar (até os 32 primeiros nomes distintos), para ele ter o conhecimento do domínio sem precisar descobrir e carregar a skill durante o trabalho. O exemplo é um `api-developer` com duas skills (convenções de API e padrões de tratamento de erro) e um corpo que manda seguir as skills pré-carregadas.
- O campo controla o que é pré-carregado, não o acesso: sem ele, o subagente ainda pode descobrir e invocar as skills do projeto, do usuário e de plugins pela ferramenta Skill; para impedir, tirar `Skill` das ferramentas ou pô-la em `disallowedTools`.
- Não dá para pré-carregar skill marcada `disable-model-invocation: true`, porque o pré-carregamento sai do mesmo conjunto que o Claude pode invocar; isso inclui a skill embutida `/verify`. Skill ausente ou desligada (por política da organização, por exemplo) é pulada com aviso no log de depuração.
- É o inverso de rodar uma skill num subagente (`context: fork` na skill): com `skills` no subagente, quem manda no prompt de sistema é o subagente, que carrega a skill; com `context: fork` na skill, o conteúdo dela é injetado no agente indicado. Nos dois casos o subagente começa sem o histórico da conversa. Subagentes embutidos não pré-carregam skills.

### Memória persistente

- **O campo `memory`** dá ao subagente uma pasta que sobrevive entre conversas, onde ele acumula conhecimento ao longo do tempo: padrões do código, achados de depuração, decisões de arquitetura. Na tabela do frontmatter: "Enables cross-session learning".
- **Exemplo da página:** um revisor de código com `memory: user` e, no corpo, a instrução de atualizar a memória com padrões, convenções e problemas recorrentes que descobrir ao revisar.
- **Três escopos:**

| Escopo | Pasta | Quando |
| :- | :- | :- |
| `user` | `~/.claude/agent-memory/<nome>/` | o aprendizado vale em todos os projetos |
| `project` | `.claude/agent-memory/<nome>/` | é do projeto e pode ir para o controle de versão |
| `local` | `.claude/agent-memory-local/<nome>/` | é do projeto, mas fora do git |

- **Faz parte da memória automática:** desligar a memória automática (configuração `autoMemoryEnabled` ou a variável `CLAUDE_CODE_DISABLE_AUTO_MEMORY`) anula o campo; o subagente sobe sem as instruções de memória nem o acesso às ferramentas descritos abaixo.
- **Com a memória ligada, três coisas acontecem:**
  1. o prompt de sistema do subagente traz instruções de ler e escrever na pasta de memória;
  2. traz também as primeiras **200 linhas ou 25 KB** do `MEMORY.md` da pasta, o que vier primeiro, com a instrução de curar o `MEMORY.md` se passar do limite;
  3. **Read, Write e Edit são liberados automaticamente**, para o subagente cuidar dos arquivos de memória.
- **Dicas da página:** `project` é o escopo padrão recomendado (o conhecimento vai para o git); pedir ao subagente que **consulte a memória antes** ("check your memory for patterns you've seen before") e que **salve depois** ("save what you learned to your memory"), o que com o tempo monta uma base que o torna mais eficaz; ou pôr a instrução no próprio arquivo do subagente, para ele manter a base por conta própria (a página dá um parágrafo-modelo: registrar caminhos de código, padrões, onde ficam as bibliotecas e as decisões de arquitetura, em notas curtas sobre o que achou e onde, montando conhecimento institucional entre conversas).

### Regras condicionais com hooks

Para controle mais fino do que liberar ou negar a ferramenta, um hook `PreToolUse` valida a operação antes de executar, permitindo umas operações de uma ferramenta e bloqueando outras. O exemplo é um `db-reader` só com Bash e um hook que, antes de cada comando Bash, roda um script de validação. O Claude Code passa a entrada do hook em JSON pela entrada padrão; o script lê o JSON, extrai o comando e, se acha uma palavra de escrita em SQL (INSERT, UPDATE, DELETE, DROP, CREATE, ALTER, TRUNCATE, sem diferenciar maiúsculas), escreve "Blocked: Only SELECT queries are allowed" no erro padrão e sai com **código 2, que bloqueia**; senão sai com 0. No macOS e no Linux o script precisa ser executável, ou o hook falha em vez de bloquear. Para testar, pedir ao subagente um UPDATE: o comando é bloqueado e ele vê a mensagem. No Windows, escrever o script em PowerShell e pôr `shell: powershell` no hook.

### Desligar subagentes específicos

Pôr `Agent(nome)` no `deny` das permissões nas settings (o exemplo nega `Agent(Explore)` e um personalizado), o que vale para embutidos e personalizados; ou usar a flag `--disallowedTools "Agent(Explore)"`.

## Hooks para subagentes

Dois jeitos: no frontmatter do subagente (rodam só enquanto ele está ativo) ou no `settings.json` (valem para a sessão inteira e disparam também dentro dos subagentes: `PreToolUse` e `PostToolUse` disparam nas chamadas do subagente como na principal, e `SubagentStart` e `SubagentStop` quando um subagente começa ou termina). Hooks de settings, de política gerenciada e de plugins valem todos dentro dos subagentes.

### Hooks no frontmatter

- Rodam só enquanto aquele subagente está ativo e são limpos quando ele termina. Disparam quando o agente é aberto como subagente (Agent ou @) e quando roda como sessão principal (`--agent` ou `agent`), neste caso junto com os do `settings.json`.
- **Confiança:** os hooks de frontmatter de um subagente de projeto só rodam depois de aceitar o diálogo de confiança da pasta que contém o arquivo. Os de `~/.claude/agents/` e os passados por `--agents` rodam sem isso; pasta adicionada de fora do repositório confiável precisa de confiança própria. Até confiar, o subagente roda, mas os hooks são pulados com erro explicativo no log. É mais estrito que a regra dos hooks em settings: confiar na pasta-mãe não basta e sessão `-p` não conta como confiável.
- Todos os eventos de hook são aceitos; os mais comuns em subagente são `PreToolUse` (antes de usar uma ferramenta, filtrado pelo nome da ferramenta), `PostToolUse` (depois) e `Stop` (quando o subagente termina, **convertido em `SubagentStop`** ao rodar como subagente). O exemplo é um revisor que valida comandos Bash antes de rodar e roda um linter depois de cada Edit ou Write.

### Hooks de projeto para eventos de subagente

No `settings.json`, `SubagentStart` e `SubagentStop` respondem ao ciclo de vida dos subagentes na sessão principal, com filtro pelo nome do tipo: o `name` do frontmatter nos de projeto e usuário, ou o identificador com escopo nos de plugin (como `my-plugin:db-agent`). Como o identificador com escopo tem dois-pontos, é avaliado como expressão regular sem âncora; para casar só aquele agente, ancorar com `^` e `$`. O exemplo roda um script de preparo da conexão com o banco só quando o `db-agent` começa e um de limpeza quando qualquer subagente termina.

## Trabalhar com subagentes

### Delegação automática

O Claude delega com base na descrição da tarefa no pedido, no campo `description` dos subagentes e no contexto atual. Para incentivar delegação proativa, pôr frases como "use proactively" na descrição. Descrições curtas: passando de 15.000 tokens somadas, há aviso na abertura, mas todos os subagentes ainda carregam. Para subagente distribuído em plugin, `claude plugin eval` mede quão bem o Claude delega a ele em vários pedidos realistas, rodando cada um com e sem o plugin.

### Invocar explicitamente

Três padrões, do mais leve ao que vale para a sessão inteira:

- **Linguagem natural:** nomear o subagente no pedido; o Claude decide se delega (exemplos: usar o test-runner para corrigir os testes que falham; pedir ao code-reviewer que olhe as mudanças recentes).
- **@-menção:** digitar `@` e escolher no autocompletar garante que aquele subagente roda naquela tarefa. A mensagem inteira ainda vai ao Claude, que escreve o prompt da tarefa: a menção controla qual subagente é chamado, não o prompt que ele recebe. Subagentes de plugin aparecem pelo nome com escopo; subagentes nomeados que estão rodando em segundo plano aparecem com o status. Dá para digitar à mão `@agent-<nome>` (ou `@agent-` mais o nome com escopo, para plugin); enquanto se digita, o autocompletar mostra arquivos, mas a menção resolve ao enviar.
- **Sessão inteira como subagente:** `claude --agent <nome>` faz a própria linha principal assumir as restrições de ferramenta e o modelo do subagente. Salvo prompt vazio, o prompt de sistema dele **substitui inteiro** o do Claude Code, como `--system-prompt`; `CLAUDE.md` e memória do projeto ainda carregam pelo fluxo normal, mesmo com `omitClaudeMd`. Rodando com `-p` como agente personalizado com prompt próprio, a sessão também começa sem o retrato do git status. O nome aparece como `@<nome>` no cabeçalho. Funciona com embutidos e personalizados, e a escolha persiste ao retomar a sessão; se o agente não existe mais, a sessão segue com as ferramentas padrão e um aviso. Para agente de plugin basta o nome; com nomes repetidos entre plugins, usar o nome com escopo (incluindo a subpasta, se houver). Para virar padrão de toda sessão no projeto, `agent` em `.claude/settings.json`; a flag vence a configuração.

### Primeiro plano ou segundo plano

- **Primeiro plano:** bloqueia a conversa principal até terminar; pedidos de permissão chegam ao usuário na hora.
- **Segundo plano:** roda em paralelo enquanto se trabalha. Quando precisa de permissão, o pedido aparece na sessão principal com o nome do subagente; aprovar deixa continuar, Esc nega só aquela chamada sem parar o subagente.
- **Quem vai para o segundo plano:** sem configuração, todo subagente que o Claude abre da conversa principal começa em segundo plano. Em `claude -p` e no Agent SDK, o Claude pode esperar, por julgamento próprio ou a pedido; na sessão interativa de terminal, no VS Code e no app desktop local, para o Claude poder esperar é preciso desligar o modo fork, que vem ligado. Skill com `context: fork` segue as regras próprias, com ou sem modo fork.
- **Deixar o Claude esperar:** (1) desligar o modo fork com `CLAUDE_CODE_FORK_SUBAGENT=0`, por exemplo no `env` do `settings.json`; (2) abrir o `claude` de novo ou nova conversa no VS Code; (3) pedir que espere quando o resultado é necessário antes ("rode o revisor e espere o relatório"). Para seguir trabalhando enquanto ele espera, Ctrl+B no terminal ou "Run in background" no VS Code. A alternativa `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` faz o Claude esperar sempre, mas desliga também os comandos em segundo plano e o Ctrl+B.
- **Ferramentas, permissões e resultados em segundo plano:** conjunto menor de ferramentas embutidas, menos para forks e subagentes de primeiro plano retomados. Todo pedido de permissão aparece na sessão principal, e uma resposta que dura além daquela chamada (como liberar para o resto da sessão) **vale para a sessão inteira, conversa principal inclusive**. O subagente pode deixar um comando de Bash ou PowerShell rodando depois do seu turno, e é avisado quando ele acaba. O resultado chega ao Claude como notificação de conclusão num turno posterior; o Claude espera essa notificação antes de relatar e, se perguntado antes, diz que ainda está rodando.
- **Painel e lista de tarefas:** subagente que termina bem some do painel na hora e o rodapé mostra "/tasks to see subagents" por 30 segundos (menos no modo leitor de tela), quando dá para abrir a transcrição pelo `/tasks`; antes da v2.1.232 a linha ficava 30 segundos, como a de um que falhou. Subagente que falha ou é parado fica 30 segundos (`x` limpa antes). No `/tasks`, o concluído fica marcado como feito, abaixo do que roda, pelos mesmos 30 segundos, com a tela de detalhe aberta; os que falham ou são parados saem da lista. Antes da v2.1.208, o concluído saía na hora e o detalhe fechava.

### Nomes de subagente

Com agent teams ligado, o Claude pode dar nome a um subagente na chamada da ferramenta Agent, inclusive sem perguntar; o nome permite mandar mensagem ou retomar depois. Na sessão interativa com agent teams, um subagente aberto da principal com nome sobe como colega de time (teammate), a menos que a chamada seja fork ou passe `isolation` na própria chamada; `isolation` no frontmatter não impede, e o colega roda na pasta da sessão principal.

### Erros de API em subagentes

- Resposta cortada no meio com texto e sem chamada de ferramenta: o Claude Code pede ao subagente que continue, inclusive em sessão interativa; o erro só encerra quando essas continuações acabam.
- Execução que termina em erro de API (limite de uso, erro de servidor repetido) é relatada ao Claude. Em primeiro plano: se já havia texto, a ferramenta Agent devolve a saída parcial com nota de que foi cortada; se não havia nada, ou só chamadas de ferramenta, falha com "Agent terminated early due to an API error" e o detalhe. Em segundo plano: marcado como falho, e a mensagem nomeia o erro e traz a última saída, para o trabalho parcial não se perder.
- Relatório que começa com o aviso de troca de modelo (um ⚠ dizendo que o agente passou para outro modelo porque o anterior não pôde ser usado) significa que terminou num modelo reserva: com uma cadeia de modelos reserva configurada, numa falha coberta por ela o subagente passa para o primeiro modelo da cadeia que aceita e segue trabalhando.
- Passado o erro, pedir ao Claude que tente de novo ou retome o subagente.

### Varredura da saída do subagente

O Claude Code varre o relatório final de cada subagente antes de o Claude lê-lo, porque o subagente pode ter lido arquivos, páginas ou saídas de comando que o usuário nunca viu, com instruções dirigidas à conversa principal. A varredura **nunca remove nem reescreve**; faz duas mudanças visíveis: insere uma barra invertida em texto que imita a saída do próprio Claude Code (uma marca `<system-reminder>`, uma linha começando com "Human:" ou "Assistant:"), para a imitação ser lida como texto comum; e acrescenta no topo uma linha de aviso começando com "[harness: subagent output matched instruction-shaped pattern(s):" quando o relatório imita uma dessas marcas ou menciona configurações de permissão como `bypassPermissions` ou `--dangerously-skip-permissions` (nesse caso o texto fica como está). A varredura não julga se é malicioso nem muda o que uma instrução pode fazer: chamada de ferramenta que o relatório induzir ainda passa pelas checagens de permissão e pelo sandbox, e ela não substitui restringir o que o subagente alcança. O relatório chega também sob um cabeçalho de saída de subagente dizendo que instruções ou alegações de aprovação dentro dele são palavras do subagente, sem autoridade do usuário; o de segundo plano chega numa notificação marcada como evento automático, não como mensagem do usuário.

### Padrões comuns

- **Isolar operações volumosas:** rodar testes, buscar documentação, processar logs; a saída longa fica no contexto do subagente e só o resumo volta (exemplo: rodar a suíte de testes e relatar só os que falham, com as mensagens de erro).
- **Pesquisa em paralelo:** para investigações independentes, vários subagentes ao mesmo tempo (exemplo: pesquisar os módulos de autenticação, banco e API em paralelo), e o Claude sintetiza; funciona melhor quando os caminhos não dependem um do outro. **Aviso da página:** os resultados voltam todos à conversa principal, então muitos subagentes com resultados detalhados gastam muito contexto, e cada um gasta tokens próprios enquanto roda. Para trabalho que precisa seguir em paralelo ou não cabe numa janela, sessões separadas trocando achados.
- **Encadear subagentes:** em fluxos de vários passos, um após o outro; cada um devolve ao Claude, que passa o contexto relevante ao próximo (exemplo: o code-reviewer acha problemas de desempenho e o optimizer corrige).

### Subagente ou conversa principal

- **Conversa principal** quando: há muito vai e vem ou refinamento iterativo; várias fases compartilham muito contexto (planejar, implementar, testar); é uma mudança rápida e pontual; a latência importa, porque um subagente que não é fork começa do zero e pode levar tempo para juntar contexto.
- **Subagente** quando: a tarefa gera saída verbosa que não precisa ficar no contexto principal; se quer impor restrições de ferramenta ou permissão; o trabalho é autocontido e pode devolver um resumo.
- **Skills** em vez disso, quando se quer prompts ou fluxos reutilizáveis que rodem no contexto da conversa principal, e não num contexto isolado.
- **`/btw`** para pergunta sobre algo que já está na conversa: vê o contexto inteiro, não tem ferramentas, e a resposta não entra no histórico.

### Subagentes que abrem subagentes

- Por padrão, um subagente pode abrir os seus, até **três camadas abaixo da conversa principal**. No limite, a ferramenta `Agent` é retirada de todo subagente menos o fork, então o do limite faz o trabalho sozinho e devolve um resumo; o fork no limite mantém `Agent` listada, mas ela devolve erro.
- Serve para tarefa delegada que se divide em subtarefas paralelas, **como um subagente revisor que despacha um verificador por achado**. Por padrão quem abre espera o relatório de cada aninhado: na sessão interativa só o resumo do subagente de topo volta ao usuário, porque o que abre subagentes em segundo plano espera os resultados antes de terminar; em `claude -p` e no SDK, quem abre espera enquanto o modo fork está ligado, e com ele desligado os aninhados começam em segundo plano, sem espera, e reportam à conversa principal se durarem mais que quem os abriu.
- `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` muda o limite (o exemplo põe 2 no `env` do `settings.json`: os subagentes delegam a uma segunda camada, que não delega mais); `1` desliga o aninhamento.
- O aninhado se configura igual e resolve dos mesmos escopos. Para um subagente não abrir outros com o aninhamento ligado (um revisor que deve ficar só leitura, por exemplo), tirar `Agent` de `tools` ou pô-la em `disallowedTools`.
- No terminal, o painel mostra os aninhados em árvore, com um contador `(+N)` de descendentes; abrir uma linha mostra irmãos e filhos diretos, com o caminho de volta até `main`.

### Limite de subagentes simultâneos

Há dois limites, cada um com sua variável: este, que impede abrir mais quando muitos estão rodando, e o de profundidade. Não há limite para o total de subagentes numa sessão. Por padrão, com **20 subagentes rodando**, abrir outro pela ferramenta Agent falha com "Concurrent subagent limit reached", e o erro diz ao Claude para não tentar de novo; volta a funcionar quando a contagem cai. `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` muda o número (qualquer inteiro positivo); sessões com ultracode ativo ficam isentas (v2.1.217). O limite só bloqueia o que o Claude abre pela ferramenta Agent, mas outras execuções ocupam vaga: o fork aberto por `/subtask` ocupa vaga e nunca é bloqueado; retomar um subagente que já terminou ocupa vaga nova sem checar o limite, então retomadas podem passar dele. Agentes de workflow e colegas de agent teams seguem limites próprios.

## Gerenciar o contexto do subagente

### O que carrega no início

Todo subagente começa com uma janela de contexto **nova e isolada**: não vê o histórico da conversa, as skills já invocadas nem os arquivos que o Claude já leu. O Claude escreve uma mensagem de delegação resumindo a tarefa, e o subagente parte dela. A exceção é o fork, que herda a conversa.

O contexto inicial de um subagente que não é fork tem:

| Item | O que é |
| :- | :- |
| **Prompt de sistema** | o prompt do próprio agente mais detalhes de ambiente que o Claude Code acrescenta, **não o prompt de sistema do Claude Code**; os personalizados o definem no corpo do arquivo ou no campo `prompt`; os embutidos têm prompts prontos |
| **Mensagem da tarefa** | o prompt de delegação que o Claude escreve ao passar o trabalho |
| **`CLAUDE.md`** | todos os níveis que a conversa principal carrega: `~/.claude/CLAUDE.md`, regras do projeto, `CLAUDE.local.md`, arquivos de política gerenciada e `AGENTS.md` lidos como instruções de projeto. Explore e Plan pulam; com `omitClaudeMd`, só os de política gerenciada, ou nenhum se a definição vem das managed settings |
| **Git status** | retrato lido do repositório quando o subagente começa; num worktree próprio, mostra o branch, o status e os commits recentes do worktree. Ausente fora de repositório git ou com o retrato desligado (`includeGitInstructions`); Explore e Plan pulam sempre |
| **Skills pré-carregadas** | conteúdo inteiro das skills do campo `skills`; embutidos não pré-carregam |
| **Lista de irmãos** | um lembrete de sistema com `main` e os outros agentes nomeados da sessão, cada um um destino válido para `SendMessage`; só aparece se o subagente tem `SendMessage` e há pelo menos outro agente com nome; é um retrato do início, então os nomeados depois não aparecem |

- Para Explore, Plan e subagentes com `omitClaudeMd`, o `CLAUDE.md` de uma subpasta e as regras com escopo de caminho ainda carregam quando o subagente mexe em arquivos ali.
- A conversa principal ainda tem o `CLAUDE.md` inteiro quando lê os resultados, então a maioria das regras não precisa chegar ao subagente; regra que precisa (como "ignore a pasta `vendor/`") deve ser repetida no pedido de delegação.
- Não dá para escolher quem recebe o git status: só Explore e Plan pulam.
- **O que nunca chega a um subagente que não é fork:** o **estilo de saída** (output style), porque ele roda o próprio prompt de sistema; a **memória automática da conversa principal**, que não carrega (para memória própria, o campo `memory`); e o **tamanho da janela da principal**, porque a janela é a do modelo do subagente, e delegar a um modelo de janela menor dá a ele a janela menor.

### Retomar subagentes

- Cada chamada cria uma instância nova. Para continuar o trabalho de um subagente em vez de recomeçar, pede-se ao Claude que o retome; o retomado mantém o histórico inteiro (chamadas de ferramenta, resultados e raciocínio), inclusive os resultados de subagentes em segundo plano que ele abriu. Antes da v2.1.304, um subagente retomado logo depois de terminar podia esquecer o trabalho mais recente.
- Ao terminar, o Claude recebe o ID do agente. Explore e Plan são de uma vez só e não devolvem ID, então não podem ser retomados; para continuar trabalho, usar `general-purpose` ou um personalizado. Subagente parado no `maxTurns` volta marcado como parcial e pode ser retomado.
- O Claude retoma com a ferramenta `SendMessage`, pondo o ID ou o nome no campo `to`; ela não exige agent teams (só as mensagens estruturadas do protocolo de time, como pedido de desligamento ou aprovação de plano). Com cross-session messaging ligado, a mesma ferramenta fala com outras sessões do Claude Code, na máquina ou fora dela. O exemplo da página: revisar o módulo de autenticação com o code-reviewer e depois pedir que continue a revisão analisando a autorização, e o Claude retoma com o contexto anterior.
- Mensagem a um subagente concluído o retoma em segundo plano sem nova chamada de Agent; o mesmo vale para um que o Claude parou com `TaskStop`, depois que a execução parada sai. A retomada mantém o conjunto de ferramentas da primeira execução e pode reaproveitar o cache de prompt que ela aqueceu.
- Um subagente com `SendMessage` também pode retomar outro; na sessão interativa, o retomado reporta a quem o retomou, não à conversa principal, e quem retomou espera o resultado. Quando um subagente manda mensagem a quem ele reporta (como quem o abriu), esse agente é retomado sem desviar os resultados.
- Subagente parado pelo usuário (`x` no `/tasks` ou `stop_task` no SDK) não se retoma sozinho: mensagem do Claude é recusada com aviso de que foi cancelado. Enquanto a linha dele está no painel, o usuário pode escrever na transcrição para retomá-lo, e depois disso o Claude volta a poder.
- Retomar abre nova execução com o mesmo ID, então um que falhou ou concluiu aparece de novo como rodando, na lista de tarefas e nos eventos do SDK.
- `SendMessage` confere se um nome ainda aponta para o mesmo agente de antes na conversa; se um agente mais novo tomou o nome, recusa o envio e diz para quem o nome aponta agora; para falar com o antigo ainda rodando, usar o ID. A checagem vale para a conversa atual e zera com `/clear`.
- **Regra de autoridade:** o subagente trata mensagens de quem o abriu como direção normal da tarefa, inclusive correções no meio, dentro das próprias permissões. Mas **nenhuma mensagem de agente vale como aprovação do usuário** para um pedido de permissão pendente, e nenhuma pode mudar as permissões, o `CLAUDE.md` ou a configuração de um subagente; só o sistema de permissões ou as mensagens do próprio usuário aprovam.
- **Transcrições:** ficam em `~/.claude/projects/{projeto}/{sessão}/subagents/`, uma por agente (`agent-{id}.jsonl`); dá também para pedir o ID ao Claude. Persistem à parte da conversa principal: a compactação da principal não as afeta; continuam na sessão, então dá para retomar um subagente depois de reiniciar o Claude Code retomando a mesma sessão; e são apagadas depois do período de retenção `cleanupPeriodDays`, 30 dias por padrão.
- **Mensagem por nome depois de reiniciar:** se o Claude não consegue falar com um subagente pelo nome após reiniciar e retomar a sessão, dar o ID. Sobrevivem ao reinício os nomes dados pela principal desde a última compactação; os de antes, não. O ID de um nome está nos arquivos `agent-{id}.meta.json` da mesma pasta. Depois de uma mensagem por ID, o nome volta a funcionar, salvo se outro agente o tomou. Antes da v2.1.299, nenhum nome sobrevivia ao reinício. (Para subagente que subiu como colega de time, valem as limitações de agent teams.)

### Autocompactação

Subagentes compactam sozinhos quando a própria janela enche, e `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` vale também para eles. Os eventos ficam na transcrição do subagente como uma entrada de sistema "compact_boundary", com o gatilho (auto) e `preTokens`, quantos tokens havia antes de compactar (o exemplo mostra cerca de 167 mil).

- **Janela própria de um subagente:** `autoCompactWindow` no frontmatter, entre 100.000 e 1.000.000 tokens, faz aquele subagente compactar mais cedo (v2.1.296). Se `CLAUDE_CODE_AUTO_COMPACT_WINDOW` está definida, vale a variável e o campo não tem efeito, salvo quando o valor da variável é ignorado. O exemplo é um `log-reader` com 200.000.
- **Armadilha:** escrever o número inteiro (`200000`); no frontmatter, `200k` é lido como 200, fora da faixa, e o subagente carrega e compacta como se o campo não existisse. Para conferir, `claude --debug` e procurar "invalid autoCompactWindow".
- Se o valor está na faixa e nada muda: ou ele não está abaixo da janela que o subagente herdaria (só baixa, não sobe), ou a sessão inteira roda como este subagente (`--agent` ou `agent`), caso em que o campo não vale e a janela da sessão se ajusta por outro caminho.

## Fork da conversa

- **O que é:** um subagente que **herda a conversa inteira até ali** em vez de começar do zero. Abre mão do isolamento de entrada que os outros subagentes dão: vê o mesmo prompt de sistema, as mesmas ferramentas, o mesmo modelo e o mesmo histórico da sessão principal, então recebe uma tarefa lateral sem precisar de explicação. As chamadas de ferramenta dele continuam fora da conversa e só o resultado final volta, então a janela principal fica limpa. Serve quando outro subagente precisaria de contexto demais para ser útil, ou para tentar várias abordagens em paralelo do mesmo ponto de partida.
- **Quem abre:** o Claude pode abrir um fork sozinho enquanto o modo fork está ligado (o padrão). O usuário abre com `/subtask` mais a tarefa, com o modo ligado ou não; o Claude Code nomeia o fork pelas primeiras palavras. O exemplo da página bifurca a conversa para rascunhar testes unitários das mudanças no parser enquanto a implementação segue na principal. O fork aparece num painel abaixo do prompt, roda em segundo plano, e o resultado chega como mensagem na conversa principal.
- **`/fork` e `/subtask`:** com o agent view desligado, `/subtask` não existe e `/fork` abre o fork; com ele ligado, `/fork` copia a sessão inteira para uma nova sessão em segundo plano.

### Acompanhar e conduzir forks em execução

O painel tem uma linha para a sessão principal e uma por fork. Fork que termina bem some; o que falhou ou foi parado fica 30 segundos, como qualquer subagente em segundo plano (antes da v2.1.232, todo fork concluído ficava 30 segundos). Teclas: setas para cima e para baixo movem entre linhas; Enter abre a transcrição do fork e permite mandar mensagens; `x` para o fork que roda ou dispensa a linha do que já parou (na linha principal ou na do fork aberto, `x` digita no prompt); Esc volta ao prompt.

Com a transcrição de um fork ou subagente aberta, mensagens e skills vão para aquele agente e comandos embutidos vão para a conversa principal, com proteções: `/compact`, `/clear` e `/rewind` agem na principal e pedem confirmação; `/model` e `/fast` mudariam a principal, então não rodam dali, com um aviso. Para o agente ler a mensagem antes de terminar o que espera, enviar com Ctrl+Enter ou Ctrl+X Ctrl+S: comandos de shell ou subagentes que ele espera e que podem ir para segundo plano vão, e se ele está escrevendo ou esperando algo que não pode ir, lê a mensagem quando aquilo acabar (v2.1.286).

### Como o fork difere dos outros subagentes

| | Fork | Subagente que não é fork |
| :- | :- | :- |
| Contexto | histórico inteiro da conversa | contexto novo com o prompt passado |
| Prompt de sistema e ferramentas | os da sessão principal | os do arquivo de definição, filtrados para execução em segundo plano |
| Modelo | o da sessão principal | o do campo `model` |
| Cache de prompt | compartilhado com a principal | cache separado |

- Como prompt de sistema e ferramentas são idênticos aos da mãe, a primeira requisição do fork **reaproveita o cache de prompt** da principal; por isso, para tarefas que precisam do mesmo contexto, o fork custa menos que um subagente novo.
- Outras diferenças espalhadas pela página: o fork pula os dois filtros de ferramenta; mantém o estilo de saída da principal; não recebe o texto de `--append-subagent-system-prompt`; com `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`, continua no modelo da principal; o parâmetro `effort` na chamada é descrito só para subagente que não é fork.
- Ao abrir um fork pela ferramenta Agent, o Claude pode passar `isolation: "worktree"`, e as edições do fork vão para um worktree separado em vez do checkout. **Fork não abre outro fork.**

### Desligar o modo fork

O modo fork deixa o Claude abrir forks sozinho. Para impedir: só os forks, pondo `"Agent(fork)"` em `permissions.deny`; ou o modo inteiro, com `CLAUDE_CODE_FORK_SUBAGENT=0` (os passos de "deixar o Claude esperar"). Enquanto o modo está ligado, o Claude não consegue esperar um subagente no terminal interativo, no VS Code ou no app desktop local. Ligado por padrão desde a v2.1.302, e na sessão interativa de terminal desde a v2.1.232.

## Exemplos de subagentes

A página dá quatro exemplos como ponto de partida (ou para pedir ao Claude uma versão sob medida), precedidos de **boas práticas**: subagentes focados, cada um excelente numa tarefa; descrições que apontem um único subagente, específicas o bastante para a delegação acertar, dentro do orçamento de 15.000 tokens; limitar as ferramentas ao necessário, por segurança e foco; pôr os subagentes de projeto no controle de versão.

- **Revisor de código (`code-reviewer`):** só leitura, revisa sem modificar; mostra como desenhar um subagente focado, com ferramentas limitadas (Read, Grep, Glob e Bash, sem Edit nem Write), `model: inherit` e prompt detalhado do que procurar e de como formatar. A descrição diz que é especialista em revisão, que revisa proativamente qualidade, segurança e manutenibilidade, e que deve ser usado logo depois de escrever ou modificar código. O prompt: papel de revisor sênior; ao ser chamado, rodar `git diff`, focar nos arquivos modificados e começar já; checklist (código claro e legível, bons nomes de funções e variáveis, sem duplicação, tratamento de erro adequado, sem segredos ou chaves expostos, validação de entrada, boa cobertura de testes, desempenho considerado); retorno por prioridade em três níveis (crítico, deve corrigir; aviso, deveria corrigir; sugestão, considerar), com exemplos concretos de como corrigir.
- **Depurador (`debugger`):** analisa e corrige; ao contrário do revisor, tem Edit (Read, Edit, Bash, Grep, Glob), porque corrigir exige mudar código. Descrição: especialista em erros, falhas de teste e comportamento inesperado, para usar proativamente ao encontrar qualquer problema. Prompt: foco em causa raiz; fluxo de capturar mensagem de erro e stack trace, achar os passos de reprodução, isolar o ponto da falha, implementar a correção mínima e verificar; processo de analisar erros e logs, checar mudanças recentes, formar e testar hipóteses, pôr logs de depuração estratégicos, inspecionar variáveis; para cada problema, explicação da causa raiz, evidência do diagnóstico, correção específica, como testar e como prevenir; corrigir a causa, não o sintoma.
- **Cientista de dados (`data-scientist`):** subagente de domínio fora do código típico; define `model: sonnet` para uma análise mais capaz, com Bash, Read e Write. Descrição: especialista em SQL, BigQuery e insights, para usar proativamente em análise de dados. Prompt: entender o pedido, escrever SQL eficiente, usar a linha de comando do BigQuery quando couber, analisar e resumir, apresentar com clareza; boas práticas (filtros, agregações e joins adequados, comentários na lógica complexa, resultados legíveis, recomendações baseadas em dados); em cada análise, explicar a abordagem, registrar premissas, destacar achados e sugerir próximos passos; consultas sempre eficientes e de custo baixo.
- **Validador de consultas ao banco (`db-reader`):** tem Bash, mas um hook `PreToolUse` só deixa passar SQL de leitura; mostra o uso de hook para controle mais fino que o campo `tools`. Descrição: executar consultas só leitura, para analisar dados ou gerar relatórios. Prompt: analista com acesso só leitura, que responde com SELECT; identificar as tabelas, escrever SELECT eficiente com filtros, apresentar com contexto; se pedirem INSERT, UPDATE, DELETE ou mudança de esquema, explicar que só tem leitura. O script de validação (em qualquer lugar do projeto, com o caminho batendo com o do hook) lê o JSON da entrada padrão, extrai `tool_input.command`, deixa passar se vazio e, se acha uma operação de escrita (a lista do exemplo final soma REPLACE e MERGE às sete da seção de hooks), escreve no erro padrão que só SELECT é permitido e sai com código 2, que bloqueia e devolve a mensagem ao Claude. No macOS e Linux, tornar executável; no Windows, PowerShell com `shell: powershell`. **O hook é rede de segurança:** o prompt já manda recusar escrita, e se o subagente tentar mesmo assim, o comando é bloqueado e ele vê a mensagem.

## Próximos passos (fim da página)

A página fecha apontando três caminhos: distribuir subagentes em plugins, para compartilhar entre times ou projetos; rodar o Claude Code de forma programática com o Agent SDK, para CI/CD e automação; e usar servidores MCP para dar aos subagentes acesso a ferramentas e dados externos.
