---
titulo: "Claude Code: visão geral dos recursos e quando acrescentar cada um, /insights, avaliar e iterar uma skill, /skill-doctor e /doctor prompt-audit"
tipo: artigo
autor: "Anthropic"
url: "https://code.claude.com/docs/en/features-overview.md"
capturado_em: 2026-10-30
licenca: "Documentação: todos os direitos reservados (texto da página Legal and compliance da documentação, registrado em 2026-10-29-claude-code-code-review-documentacao: '© Anthropic PBC. All rights reserved.'; a cópia em markdown lida não traz rodapé); entra só a ficha."
areas: [anthropic-claude, agent-engineering]
tags: [claude-code, harness, continual-learning, insights, skill-evaluation, skill-creator, prompt-audit, claude-md]
---

Ficha de estudo, em palavras próprias, de trechos de quatro páginas da documentação do Claude Code que respondem à mesma pergunta: **como o ambiente (o harness) muda ao longo do uso**. Lidas em markdown em 2026-10-30 (changelog mais recente: 2.1.314). Lida. A seção 1 cobria de início só a seção "Build your setup over time" da página de visão geral; foi completada no mesmo dia, por pedido da curadoria depois de uma revisão, e agora cobre a página de visão geral inteira, na ordem dela. As seções 2 a 5 seguem sendo trechos das outras páginas.

**De onde vem cada coisa:**
- [visão geral] https://code.claude.com/docs/en/features-overview.md ("Extend Claude Code"), a página inteira
- [custos] https://code.claude.com/docs/en/costs.md, seção "Analyze your usage patterns" (`/insights`)
- [skills] https://code.claude.com/docs/en/skills.md, seções "Find unused skills" e "Evaluate and iterate on a skill"
- [memória] https://code.claude.com/docs/en/memory.md, "Audit your instruction files" (ficha completa da página em [[2026-10-30-claude-code-memoria-claude-md-e-memoria-automatica]])
- [comandos] https://code.claude.com/docs/en/commands.md e [changelog] https://code.claude.com/docs/en/changelog.md, para versões

## 1. Visão geral dos recursos e quando acrescentar cada um [visão geral]

**A camada de extensão.** O Claude Code junta um modelo que raciocina sobre o código com ferramentas embutidas (arquivos, busca, execução, acesso à web), que dão conta da maioria das tarefas de programação. A página trata da camada que a pessoa acrescenta para mudar o que o Claude sabe, ligá-lo a serviços externos e automatizar fluxos (o laço agêntico em si fica em outra página, "How Claude Code works"). Para quem começa: primeiro o CLAUDE.md, com as convenções do projeto, e os outros recursos à medida que aparecem os gatilhos (tabela abaixo).

**Onde cada extensão entra no laço:**
- **CLAUDE.md:** contexto persistente que o Claude vê em toda sessão.
- **Estilos de saída (output styles):** papel, tom e formato de resposta para todas as respostas de uma sessão.
- **Skills:** conhecimento reutilizável e fluxos que se invocam.
- **Inteligência de código:** liga o Claude a um servidor de linguagem (LSP), para navegar por símbolo e ver erros de tipo ao vivo.
- **MCP:** liga o Claude a serviços e ferramentas externos.
- **Subagentes:** rodam o próprio laço em contexto isolado e devolvem resumos.
- **Fluxos dinâmicos (dynamic workflows):** muitos subagentes rodados por um script que o próprio Claude escreve, com um resultado só.
- **Mensagens entre sessões (cross-session messaging):** o Claude leva uma mensagem de uma sessão da pessoa para outra.
- **Hooks:** rodam um script, uma requisição HTTP, uma chamada de ferramenta MCP, um prompt ou um subagente quando o Claude Code chega a um evento do ciclo de vida.
- **Plugins e marketplaces:** empacotam e distribuem os recursos acima.

A página chama as **skills** de extensão mais flexível: um arquivo markdown com conhecimento, fluxos ou instruções, invocado por comando (como `/deploy`) ou carregado pelo Claude quando relevante, e que pode rodar na conversa atual ou em contexto isolado, via subagente.

**Casar o recurso com o objetivo.** Os recursos vão do contexto sempre presente, passando pelas capacidades sob demanda, até a automação em segundo plano disparada por evento:

| Recurso | O que faz | Quando usar | Exemplo da página (em paráfrase) |
|---|---|---|---|
| CLAUDE.md | contexto persistente, carregado em toda conversa | convenções do projeto, regras "sempre faça X" | usar pnpm e não npm; rodar os testes antes do commit |
| Estilo de saída | instruções de papel, tom e formato para a sessão inteira | voz, tamanho ou formato desejados em toda resposta, ou o Claude num papel que não é o de engenheiro de software | o estilo embutido Concise, para respostas curtas; um estilo próprio que responde tudo com um diagrama primeiro |
| Skill | instruções, conhecimento e fluxos que o Claude pode usar | conteúdo reutilizável, documentação de referência, tarefas repetíveis | `/deploy` roda a lista de verificação de deploy; uma skill com os padrões de endpoint de uma API |
| Subagente | contexto de execução isolado que devolve resultado resumido | isolar contexto, tarefas paralelas, trabalhadores especializados | pesquisa que lê muitos arquivos e devolve só os achados principais |
| Fluxo dinâmico | script escrito pelo Claude que roda muitos subagentes em segundo plano | trabalho que passa de um punhado de subagentes, ou achados que se quer conferidos por outros | auditar uma base de código inteira, com um segundo grupo de agentes verificando cada achado |
| Mensagens entre sessões | o Claude entrega uma mensagem de uma sessão da pessoa a outra | sessões que a própria pessoa roda e que precisam dos achados uma da outra no meio da tarefa | uma sessão avisa outra que uma mudança sua quebra aquilo em que a outra está construindo |
| Inteligência de código | navegação e diagnóstico pelo servidor de linguagem | linguagens tipadas, bases grandes em que o grep é lento ou impreciso | ir à definição de um símbolo em vez de ler o arquivo inteiro |
| MCP | conexão com serviços externos | dados ou ações externos | consultar o banco, postar no Slack, controlar um navegador |
| Hook | script, requisição HTTP, chamada MCP, prompt ou subagente disparado por evento | automação que tem de rodar em todo evento que casa | rodar o ESLint depois de cada edição de arquivo |
| Artifact | publica a saída da sessão como página web privada e interativa | saída que se quer ver ou compartilhar visualmente, não como texto de terminal | uma linha do tempo de incidente que se atualiza enquanto o Claude investiga |

**Plugins são a camada de empacotamento:** juntam skills, hooks, subagentes e servidores MCP numa unidade instalável. As skills de plugin têm nome com o prefixo do plugin (no formato `/plugin:skill`), para vários plugins conviverem. Servem para reaproveitar o mesmo ambiente em vários repositórios ou distribuí-lo a outros por um marketplace.

**Montar o ambiente aos poucos, por gatilho.** Não é preciso configurar tudo de saída: cada recurso tem um gatilho reconhecível, e a maioria das equipes os acrescenta mais ou menos nesta ordem:

| Gatilho | O que acrescentar |
|---|---|
| O Claude erra uma convenção ou um comando duas vezes | CLAUDE.md |
| A pessoa vive pedindo para ser mais curto, explicar mais ou responder no mesmo formato | um estilo de saída (output style) |
| A pessoa vive digitando o mesmo prompt para começar uma tarefa | uma skill que ela invoca |
| A pessoa cola o mesmo roteiro de vários passos pela terceira vez | uma skill |
| A pessoa vive copiando dados de uma aba que o Claude não vê | um servidor MCP |
| O Claude lê muitos arquivos para achar onde um símbolo é definido | um plugin de inteligência de código |
| Uma tarefa paralela enche a conversa de saída que não se usa de novo | um subagente |
| Algo deve acontecer toda vez, sem pedir | um hook |
| Um segundo repositório precisa do mesmo ambiente | um plugin |

Os mesmos gatilhos dizem quando **atualizar** o que já existe: um erro repetido ou um comentário de revisão recorrente é uma edição do CLAUDE.md, "not a one-off correction in chat"; um fluxo que a pessoa vive ajustando à mão é uma skill que pede outra revisão.

**Comparar recursos parecidos.** A página aponta um post do blog ("Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents") para o aprofundamento e faz sete comparações:

- **Skill ou subagente.** A skill é conteúdo reutilizável que se carrega em qualquer contexto; o subagente é um trabalhador isolado, fora da conversa principal. A skill compartilha conteúdo entre contextos e **soma à janela principal**; o subagente isola: o trabalho acontece à parte, numa janela própria com tokens de entrada e saída próprios, e só o resumo volta. Skill serve a material de referência e fluxos invocáveis; subagente, a tarefas que leem muitos arquivos, trabalho paralelo e trabalhadores especializados. As skills podem ser **de referência** (conhecimento usado ao longo da sessão, como o guia de estilo da API) ou **de ação** (mandam fazer algo, como o `/deploy`). Usar subagente quando se precisa isolar contexto ou a janela está enchendo, e quando o trabalho intermediário não precisa ficar visível; subagentes próprios podem ter instruções e pré-carregar skills. Os dois **se combinam**: o subagente pré-carrega skills (campo `skills:`), e a skill roda em contexto isolado com `context: fork`.
- **CLAUDE.md ou skill.** Os dois guardam instruções e os dois importam arquivos com `@caminho`, mas o CLAUDE.md carrega em toda sessão, automaticamente, e não dispara fluxos; a skill carrega sob demanda e dispara fluxo com `/<nome>`. CLAUDE.md para o que o Claude deve sempre saber (convenções, comandos de build, estrutura, regras "nunca faça X"); skill para material de referência que se usa às vezes (documentação de API, guia de estilo) ou fluxo que se dispara pelo nome (deploy, revisão, release). Regra de bolso: **CLAUDE.md abaixo de 200 linhas**; crescendo, mover a referência para skills ou dividir em arquivos de `.claude/rules/`.
- **CLAUDE.md ou estilo de saída.** O CLAUDE.md leva o que o Claude deve saber (fatos e regras do projeto, sempre carregado); o estilo de saída diz como responder (papel, tom, formato; um ativo por vez, trocável a qualquer momento). No CLAUDE.md, o que vale para o projeto em qualquer estilo; no estilo, o que é da própria resposta e que se pode querer desligar (tamanho, formato, quanto explica, outro papel como assistente de escrita). Há estilos embutidos e dá para escrever os próprios. Combinam: o CLAUDE.md fica carregado em qualquer estilo. O Claude segue os dois como instrução, então **nenhum é imposto**; o que tem de acontecer toda vez vai para um hook.
- **CLAUDE.md, regras ou skills.** O CLAUDE.md carrega em toda sessão, vale para o projeto inteiro e serve às convenções centrais e aos comandos de build; as regras de `.claude/rules/` carregam em toda sessão ou quando se abre um arquivo que casa, podem ser recortadas por caminho e servem a diretrizes de uma linguagem ou de um diretório (com `paths` no frontmatter só carregam quando o Claude mexe nos arquivos que casam, economizando contexto, e mantêm o CLAUDE.md focado); as skills carregam sob demanda, quando invocadas ou julgadas relevantes, valem para uma tarefa e servem a material de referência e fluxos repetíveis.
- **Subagente ou fluxo dinâmico.** Os dois trabalham fora da conversa principal; a diferença é quem decide o próximo passo: com subagentes, o Claude decide turno a turno; no fluxo, o script decide. Subagente para um trabalhador rápido e focado (pesquisar uma pergunta, verificar uma afirmação, revisar um arquivo), que devolve resumo; subagentes que o Claude nomeou ao criar podem trocar mensagens entre si. Fluxo dinâmico quando o trabalho passa de um punhado de subagentes ou quando se quer os achados conferidos antes de vê-los (auditoria da base inteira, migração grande, plano rascunhado por vários ângulos); para começar um, pedir um fluxo no prompt. Para passar um achado de uma sessão a outra, pedir ao Claude da primeira que o mande (mensagens entre sessões); a página "Run agents in parallel" compara as outras formas de rodar mais de um Claude, inclusive sessões entregues e conferidas depois.
- **MCP ou skill.** O MCP é o protocolo que liga o Claude a serviços externos e dá ferramentas e acesso a dados (integração com Slack, consultas ao banco, controle de navegador), com a conexão e a autenticação a cargo do servidor; a skill dá o conhecimento de como usar bem essas ferramentas, mais fluxos invocáveis (checklist de revisão, fluxo de deploy, guia de estilo de API; por exemplo, o esquema do banco e os padrões de consulta da equipe, ou um fluxo de postar no Slack com as regras de formatação da equipe). Resolvem problemas diferentes e trabalham bem juntos.
- **Hook ou skill.** O Claude Code **roda** o hook num evento do ciclo de vida; a skill ele **carrega no contexto** para o Claude aplicar. O hook roda comando de shell, requisição HTTP, chamada MCP, prompt de LLM ou subagente, disparado por eventos como `PostToolUse` ou `SessionStart`, sem o Claude decidir, e custa **zero de contexto** a menos que devolva saída; a skill é instrução que o Claude lê e segue, disparada pelo nome ou pela descrição que casa com a tarefa, com resultado que pode variar, e custa a descrição em toda sessão e o conteúdo inteiro quando usada. Hook para o que tem de sair igual toda vez e não pede raciocínio (lint depois de edição, bloquear comando perigoso, log, notificação; formatar ao salvar, recusar um `rm -rf /`, postar no Slack quando a sessão termina); skill quando o Claude deve decidir como aplicar os passos ou o conteúdo é conhecimento e não roteiro (um checklist de release, o guia de estilo da API, um roteiro de depuração). **Barreiras vão em hooks:** uma instrução como "nunca edite o `.env`" no CLAUDE.md ou numa skill "is a request, not a guarantee"; um hook `PreToolUse` que bloqueia a edição é imposição. E a saída do hook entra no contexto: um `PostToolUse` que roda o linter devolve texto que o Claude lê, e uma skill de corrigir lint diz como resolver.

**Como os recursos se sobrepõem entre níveis** (usuário, projeto, plugin, política gerenciada; e CLAUDE.md aninhado em subpastas ou skills em pacotes de um monorepo):
- **CLAUDE.md soma:** todos os níveis entram no contexto ao mesmo tempo; os do diretório de trabalho para cima carregam no início, os das subpastas conforme se trabalha nelas; em conflito, o Claude usa o julgamento para conciliar.
- **Skills e subagentes se sobrepõem pelo nome:** com o mesmo nome em vários níveis, vence uma definição pela prioridade (skills: gerenciada > usuário > projeto; subagentes: gerenciada > flag de linha de comando > projeto > usuário > plugin). As skills de plugin têm prefixo para não colidir.
- **Servidores MCP se sobrepõem pelo nome:** local > projeto > usuário.
- **Hooks se juntam:** todos os registrados disparam nos eventos que casam, venham de onde vierem.

**Combinar recursos.** Cada um resolve um problema (CLAUDE.md, o contexto sempre presente; skills, conhecimento e fluxos sob demanda; MCP, conexões externas; subagentes, isolamento; hooks, automação), e os ambientes reais combinam, por exemplo CLAUDE.md para as convenções, uma skill para o deploy, MCP para o banco e um hook para lint depois de cada edição. Quatro padrões: **skill + MCP** (o MCP dá a conexão, a skill ensina a usar bem: o MCP liga ao banco, a skill documenta esquema e padrões de consulta); **skill + subagente** (a skill dispara subagentes em paralelo: uma skill de auditoria abre subagentes de segurança, desempenho e estilo em contexto isolado); **CLAUDE.md + skills** (o CLAUDE.md tem as regras sempre presentes, as skills o material carregado sob demanda: o CLAUDE.md manda seguir as convenções da API, a skill tem o guia completo); **hook + MCP** (o hook dispara ações externas pelo MCP: um hook depois de edição avisa no Slack quando o Claude muda arquivos críticos).

**Custos de contexto.** Todo recurso acrescentado consome contexto. Demais pode encher a janela, e também acrescentar **ruído que deixa o Claude menos eficaz**: skills que não disparam direito, ou o Claude perdendo de vista as convenções. Há uma página interativa ("Explore the context window") que mostra como os recursos se combinam numa sessão rodando.

| Recurso | Quando carrega | O que carrega | Custo de contexto |
|---|---|---|---|
| CLAUDE.md | início da sessão | o conteúdo inteiro de cada arquivo que carrega no início | em toda requisição |
| Estilos de saída | início da sessão, e de novo ao trocar de estilo | as instruções inteiras do estilo ativo; nada no estilo Default | em toda requisição |
| Skills | início da sessão e quando usadas | descrições no início, conteúdo inteiro quando usada | baixo (descrições em toda requisição) |
| Servidores MCP | início da sessão | nomes das ferramentas; esquemas completos sob demanda | baixo até uma ferramenta ser usada |
| Inteligência de código | depois de edições e sob demanda | diagnósticos depois das edições; localização de símbolos na consulta | baixo; reduz leituras de arquivo em outros lugares |
| Subagentes | quando criados | contexto novo com as skills indicadas, ou a conversa do pai num fork | isolado da sessão principal |
| Hooks | no disparo | nada (rodam por fora) | zero, a menos que o hook devolva contexto |

Nota da tabela: `disable-model-invocation: true` no frontmatter de uma skill tira a descrição dela do contexto do Claude; para uma skill que a pessoa não escreveu, `skillOverrides` nas configurações faz o mesmo sem editar o arquivo.

**Como cada recurso carrega** (a página tem um diagrama: o CLAUDE.md carrega no início e fica em toda requisição; os nomes das ferramentas MCP carregam no início e os esquemas ficam para o uso; as skills carregam as descrições no início e o conteúdo na invocação; os subagentes ganham contexto isolado; os hooks rodam por fora):
- **CLAUDE.md:** no início da sessão, o conteúdo inteiro de cada arquivo que carrega então (níveis gerenciado, usuário e projeto). O Claude lê do diretório de trabalho até a raiz e descobre os aninhados nas subpastas conforme acessa os arquivos delas; se um aninhado passa do limite de tamanho por arquivo, o Claude recebe só o começo. Dica: manter abaixo de 200 linhas, mover referência para skills, e rodar `/doctor` para receber propostas de corte num CLAUDE.md versionado.
- **Skills:** capacidades extras, de referência ou fluxos invocáveis; há skills embutidas que funcionam sem configuração (a página cita `/code-review`, `/batch` e `/debug`) e dá para criar as próprias. Por padrão, as descrições carregam no início e o conteúdo inteiro quando usada; nas skills só do usuário (`disable-model-invocation: true`), nada carrega até a pessoa invocar. Nas que o modelo pode invocar, o Claude vê nome e descrição em toda requisição, e o conteúdo inteiro entra na conversa quando invocada pelo nome ou carregada sozinha. **Como o Claude escolhe:** casa a tarefa com as descrições; descrição vaga ou sobreposta faz carregar a skill errada ou perder a que ajudaria; para forçar uma, invocar pelo nome. Custo baixo até o uso, zero nas só do usuário até a invocação. **Em subagentes,** o conteúdo inteiro das skills listadas no campo `skills` do subagente carrega no lançamento, não sob demanda, e o subagente ainda pode descobrir e invocar pela ferramenta Skill as skills de projeto, usuário e plugin não listadas. Dica: `disable-model-invocation: true` para skills com efeito colateral, que economiza contexto e garante que só rodam quando chamadas pelo nome.
- **Servidores MCP:** no início da sessão, os nomes das ferramentas e as instruções dos servidores conectados; os esquemas JSON completos ficam adiados até o Claude precisar de uma ferramenta. A busca de ferramentas vem ligada por padrão, então ferramentas MCP paradas consomem contexto mínimo. Dicas: `/mcp` mostra o estado de conexão de cada servidor; `/context all` mostra quantos tokens cada ferramenta MCP carregada usa; o Claude Code reconecta sozinho a servidores remotos que caem, e dá para desconectar os que não se usam.
- **Inteligência de código:** depois das edições (erros e avisos de tipo a cada edição) e sob demanda ao navegar (definição, referências e tipo de um símbolo). Custo baixo, e o uso líquido de contexto pode até cair, porque a consulta de símbolo substitui leituras amplas de arquivo. A ferramenta LSP fica inativa até instalar o plugin de inteligência de código da linguagem.
- **Subagentes:** sob demanda, quando a pessoa ou o Claude cria um para uma tarefa. Carregam contexto novo e isolado com: o prompt de sistema do próprio agente (não o do Claude Code); o conteúdo inteiro das skills do campo `skills:`; o CLAUDE.md e o estado do git (os agentes embutidos Explore e Plan começam sem os dois, e um agente com `omitClaudeMd` na definição começa sem os CLAUDE.md de usuário, projeto e local); e o contexto que o agente principal passa no prompt. Num **fork**, o Claude Code carrega a conversa do pai até ali, o prompt de sistema e as ferramentas. Custo isolado da sessão principal; dica: subagentes para trabalho que não precisa do contexto inteiro da conversa.
- **Hooks:** no disparo, em eventos do ciclo de vida como execução de ferramenta, limites de sessão, envio de prompt, pedido de permissão e compactação. Não carregam nada por padrão, rodam fora da conversa principal, e custam zero a menos que devolvam saída que entra como mensagem na conversa. Dica: ideais para efeitos colaterais (lint, log) que não precisam afetar o contexto do Claude.

**Para saber mais,** a página fecha com um guia por recurso: CLAUDE.md, skills, subagentes, fluxos dinâmicos, mensagens entre sessões, MCP, hooks, plugins e marketplaces.

## 2. Ler as próprias sessões: `/insights` [custos]

Relatório sobre **como** se trabalha, não sobre quantos tokens se gastou. Analisa as sessões recentes daquela máquina e escreve um HTML com: em que se trabalha, pontos de atrito ("misunderstood requests or buggy code") e sugestões para usar melhor o Claude Code. Cada rodada analisa até 200 sessões ainda não vistas e pula as muito curtas (o cabeçalho mostra, por exemplo, "200 sessions (412 total)"). Se o modo automático está disponível e as sessões rodaram quase sem ele, estima quantos pedidos de permissão ele teria resolvido. O relatório mais recente fica em `~/.claude/usage-data/report.html`, com cópias datadas de cada rodada, apagadas no mesmo prazo dos dados de sessão (`cleanupPeriodDays`, 30 dias por padrão). Roda em qualquer plano e provedor; os tokens contam no plano. Não inclui sessões de outras máquinas nem do claude.ai. Não roda em sessões na nuvem.

## 3. Achar skills sem uso: `/skill-doctor` [skills]

Toda skill da listagem soma contexto a cada turno, usada ou não. O `/skill-doctor` mostra o custo de contexto de cada skill e quantas vezes foi usada, marca as nunca invocadas e diz onde desligar; sugere começar pelas de maior custo. Também lista plugins sem uso recente. Não cobre skills embutidas nem corporativas. A página pede a versão 2.1.252 ou posterior; o changelog registra a entrada do comando na 2.1.261. Não é consolidação de conteúdo: é poda por uso e custo.

## 4. Avaliar e iterar uma skill [skills]

- **Ver a skill disparar não prova que ela funciona:** é preciso medir separado se o Claude a invoca nos pedidos certos e se a saída bate com o esperado quando invoca.
- **O teste é a comparação com uma linha de base:** alguns pedidos realistas, cada um rodado numa **sessão nova** com a skill disponível e de novo com ela desligada, e comparar. A sessão nova importa porque o contexto que sobrou de escrever a skill esconde lacunas nas instruções. Skill pessoal ou do projeto se desliga em `skillOverrides`; a de plugin, pelo `claude plugin eval`.
- **Duas ferramentas automatizam:** o `claude plugin eval` (para skill em plugin: cada pedido numa sessão isolada com e sem o plugin, notas por avaliadores que a pessoa define ou que ele escreve, e saída com erro abaixo de um limiar, para travar a integração contínua) e o plugin **skill-creator** (para iterar uma skill dentro da conversa). O skill-creator: guarda os casos de teste em `evals/evals.json` na pasta da skill; roda cada caso num subagente com contexto limpo, anotando tokens e duração; confere cada asserção e grava passou ou falhou com evidência; agrega taxa de acerto, tempo e tokens com e sem a skill; faz comparação **cega A/B entre duas versões**, para confirmar que a edição melhorou antes de commitar; ajusta a descrição medindo pedidos que devem e não devem disparar; e abre um visualizador onde a pessoa registra o retorno qualitativo, que a iteração seguinte lê. Os dois formatos de avaliação não são intercambiáveis.

## 5. Auditar os arquivos de instrução: `/doctor prompt-audit` [memória, changelog]

Procura nos arquivos de instrução o que ficou velho ou contraditório: instruções escritas para modelos antigos, referências a arquivos ou comandos que não existem, arquivos que se contradizem. Entrega relatório com edições propostas e não muda nada sem pedido. Cobre por padrão CLAUDE.md, CLAUDE.local.md, AGENTS.md e as regras, skills, comandos, subagentes e estilos de saída em `.claude/` e `~/.claude/`; aceita um caminho. Exige a versão 2.1.283 (changelog: "audit your CLAUDE.md files, skills, agents and commands for prompting patterns written for older models"). Não inclui a pasta da memória automática no alcance padrão (aceita um caminho como argumento) e não lê transcritos de sessão.
