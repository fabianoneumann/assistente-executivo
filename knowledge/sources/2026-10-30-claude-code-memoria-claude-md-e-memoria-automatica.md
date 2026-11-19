---
titulo: "How Claude remembers your project (Claude Code): CLAUDE.md, regras, AGENTS.md e memória automática"
tipo: artigo
autor: "Anthropic"
url: "https://code.claude.com/docs/en/memory.md"
capturado_em: 2026-10-30
licenca: "Documentação: todos os direitos reservados (texto da página Legal and compliance da documentação, registrado em 2026-10-29-claude-code-code-review-documentacao: '© Anthropic PBC. All rights reserved.'; a cópia em markdown lida não traz rodapé); entra só a ficha."
areas: [anthropic-claude, agent-engineering]
tags: [claude-code, claude-md, auto-memory, memory, rules, agents-md, context-engineering, harness, continual-learning, prompt-audit]
---

Ficha de estudo, em palavras próprias, da página oficial de memória do Claude Code, lida em markdown em 2026-10-30 (versão mais recente no changelog do mesmo dia: 2.1.314). A página não tem licença aberta; citações literais só curtas. Lida (como o ambiente aprende com os refinamentos).

## A ideia central

Cada sessão começa com a janela de contexto vazia. Dois mecanismos levam conhecimento de uma sessão para outra: os arquivos **CLAUDE.md** (ou **AGENTS.md**), que a pessoa escreve, e a **memória automática**, que o Claude escreve a partir das correções e preferências. Os dois entram no início de toda conversa e são tratados como **contexto, não como configuração imposta**: para barrar uma ação independentemente do que o Claude decidir, a doc manda usar um hook (PreToolUse). Quanto mais específica e curta a instrução, mais ela é seguida.

| | CLAUDE.md | Memória automática |
|---|---|---|
| Quem escreve | a pessoa | o Claude |
| O que contém | instruções e regras | aprendizados e padrões |
| Escopo | projeto, usuário ou organização | por repositório, compartilhado entre worktrees |
| Carga | toda sessão | toda sessão (as primeiras 200 linhas ou 25 KB) |
| Para quê | padrões de código, fluxos, arquitetura | preferências, correções, contexto que o código não mostra |

Subagentes podem ter memória automática própria (ficha [[2026-10-30-claude-code-memoria-de-subagente]]).

## CLAUDE.md

**Quando acrescentar** ("o lugar do que você explicaria de novo"): quando o Claude erra a mesma coisa pela segunda vez; quando uma revisão de código pega algo que ele devia saber daquele código; quando a pessoa digita no chat a mesma correção ou esclarecimento da sessão anterior; quando um colega novo precisaria do mesmo contexto. Entra o que vale em toda sessão (comandos de build, convenções, estrutura, regras "sempre faça X"); procedimento de vários passos ou que só vale numa parte do código vai para uma skill ou para uma regra por caminho.

**Onde fica, em ordem de carga** (do mais amplo ao mais específico; o mais específico aparece depois no contexto): política gerenciada da organização (um caminho fixo por sistema operacional, que o desenvolvedor não pode excluir); usuário (`~/.claude/CLAUDE.md`); projeto (`./CLAUDE.md` ou `./.claude/CLAUDE.md`, versionado); local (`./CLAUDE.local.md`, pessoal, fora do git). Os arquivos nos diretórios acima do de trabalho carregam no início; os das subpastas, sob demanda, quando o Claude lê, escreve ou edita um arquivo naquela subpasta (um `cat` ou `head` de um arquivo conta como leitura).

**Montar o do projeto:** comandos de build e teste, padrões, decisões de arquitetura, convenções de nome, fluxos comuns. `/init` gera um ponto de partida analisando o código (e sugere melhorias se já existe um); com `CLAUDE_CODE_NEW_INIT=1`, o `/init` vira um fluxo em fases que pergunta que artefatos montar (CLAUDE.md, skills, hooks), explora com um subagente e apresenta uma proposta revisável antes de escrever. `/context` mostra, em "Memory files", o que carregou.

**Escrever instruções que funcionam:** concretas o bastante para conferir ("indentação de 2 espaços", não "formate bem"; "rode `npm test` antes de commitar", não "teste suas mudanças"). Tamanho: mirar **menos de 200 linhas por arquivo**, porque arquivo longo consome contexto e reduz a aderência; o que vale só para parte do código vai para regra por caminho. Estrutura: títulos e listas. Consistência: duas instruções contraditórias fazem o Claude escolher uma "arbitrariamente"; revisar periodicamente CLAUDE.md, os aninhados e `.claude/rules/` para tirar o velho e o conflitante.

**Auditar os arquivos de instrução (`/doctor prompt-audit`):** o Claude procura instruções escritas para modelos antigos, referências a arquivos ou comandos que não existem e arquivos que se contradizem, e entrega um relatório com edições propostas; nada muda até a pessoa pedir para aplicar. Por padrão cobre CLAUDE.md, CLAUDE.local.md, AGENTS.md e as regras, skills, comandos, subagentes e estilos de saída em `.claude/` e `~/.claude/`; aceita um caminho para auditar só um arquivo ou pasta. Roda pela skill embutida `/claude-api`; exige a versão 2.1.283 ou posterior (o changelog registra a entrada nessa versão como auditoria de "prompting patterns written for older models"). Não lista os arquivos da memória automática.

**Importar arquivos:** `@caminho` dentro do CLAUDE.md expande o arquivo no contexto (caminho relativo ao arquivo que importa; até quatro saltos de importação recursiva; caminho com espaço pede barra invertida; entre crases não importa). Importar organiza, mas **não reduz** o custo de contexto. Importação que sai do diretório de trabalho pede aprovação na primeira vez (proteção contra arquivos que outros commitam). Comentários HTML de bloco no CLAUDE.md são removidos antes de entrar no contexto (servem de nota para mantenedores).

**Como carrega:** todos os arquivos achados são **concatenados**, não se sobrepõem; da raiz do sistema de arquivos até o diretório de trabalho, então o mais perto de onde a sessão abriu é lido por último; em cada diretório, o `.local` vem depois. `--add-dir` não carrega CLAUDE.md de diretórios extras, a não ser com uma variável de ambiente própria.

## Regras em `.claude/rules/`

Arquivos markdown, um tema por arquivo, descobertos recursivamente. Sem o campo `paths`, carregam no início com a mesma prioridade do `.claude/CLAUDE.md`; com `paths` (padrões glob), só quando o Claude lê ou edita um arquivo que casa. A nota da doc: regra carrega sempre (ou ao abrir o arquivo que casa); instrução que só serve a uma tarefa vai para uma **skill**, que só carrega quando invocada ou julgada relevante. Há regras de usuário (`~/.claude/rules/`, carregadas antes das do projeto; se conflitarem, o Claude pode seguir qualquer uma) e compartilhamento por link simbólico (link para fora do diretório pede a mesma aprovação das importações externas).

## Equipes grandes e AGENTS.md

A organização pode distribuir um CLAUDE.md gerenciado e excluir arquivos por padrão (`claudeMdExcludes`); a regra imposta de verdade vem das configurações gerenciadas, porque o CLAUDE.md "molda" o comportamento sem ser camada de imposição. O AGENTS.md (padrão de outras ferramentas) é lido no lugar do CLAUDE.md quando não há CLAUDE.md no caminho (a partir da versão 2.1.277), ou junto, por configuração; um CLAUDE.md pode importá-lo com `@AGENTS.md`.

## Memória automática

- **O que é:** o Claude acumula conhecimento entre sessões sem a pessoa escrever nada. Grava quatro tipos de nota, com o tipo no frontmatter: `user` (papel, experiência, preferências de trabalho), `feedback` ("corrections you give Claude and approaches you confirm"), `project` (trabalho em curso, prazos, decisões que o código e o histórico do git não mostram), `reference` (onde achar informação fora do projeto).
- **O que não grava:** o que se deriva do código (arquitetura, caminhos, correções de depuração) e o que o CLAUDE.md já diz. Não grava em toda sessão: decide pelo que seria útil numa conversa futura.
- **Ligar e desligar:** ligada por padrão nas sessões locais (desligada por padrão em ambiente auto-hospedado); `/memory` tem o botão (grava `autoMemoryEnabled`); por projeto, a mesma chave nas configurações do projeto; ou a variável `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`.
- **Onde fica:** `~/.claude/projects/<projeto>/memory/`, derivado do repositório git (worktrees e subpastas do mesmo repositório dividem a pasta). É **só da máquina**: os arquivos não são compartilhados entre máquinas nem com ambientes na nuvem; `autoMemoryDirectory` muda o lugar. Um índice `MEMORY.md` e um arquivo por memória (exemplo da doc: `feedback_testing.md`). A faxina dos transcritos de sessão (`cleanupPeriodDays`) não apaga a memória: ela fica até alguém editar ou apagar.
- **Como funciona:** só as **primeiras 200 linhas ou 25 KB** do `MEMORY.md` entram no início; o Claude mantém o índice curto mandando o detalhe para os arquivos de tópico, que lê sob demanda. Depois de cada escrita no índice, o Claude Code mede o arquivo: perto do limite, lembra o Claude de encurtar ("uma linha por entrada", mover o detalhe, "merge or drop stale entries"); acima, a escrita passa mas volta um erro mandando reescrever o índice, porque o que passa do limite some na próxima carga. O limite vale só para o `MEMORY.md` (o CLAUDE.md entra inteiro até 4 MiB).
- **Subagentes e fork:** a memória da conversa principal não carrega nos subagentes; o fork herda a conversa. A memória do subagente é outra pasta.
- **Visível na interface:** mensagens como "Saved 2 memories" e "Recalled 2 memories". Cada arquivo de memória com frontmatter ganha o campo `modified` com a data e hora da escrita, para mostrar quão atual é o fato, à pessoa e ao Claude.
- **Auditar e editar:** é markdown comum; `/memory` abre a pasta.
- **"Lembre-se disso"** vai para a memória automática; "adicione ao CLAUDE.md" vai para o CLAUDE.md.

## Problemas comuns (seção de solução)

- **O Claude não segue o CLAUDE.md:** o conteúdo entra como mensagem de usuário depois do prompt de sistema, sem garantia de obediência estrita, sobretudo com instrução vaga ou conflitante. Conferir com `/context` se carregou; tornar a instrução mais específica; procurar conflitos entre arquivos; conferir se a instrução briga com o que o próprio Claude Code acrescenta (por exemplo regras de commit). O que precisa rodar num ponto fixo (antes de todo commit, depois de cada edição) vira **hook**, que roda "regardless of what Claude decides". Para nível de prompt de sistema, `--append-system-prompt`. O hook `InstructionsLoaded` registra o que carregou e por quê.
- **AGENTS.md que não carrega:** quase sempre há um CLAUDE.md no caminho.
- **Não sei o que a memória gravou:** `/memory`, a pasta.
- **CLAUDE.md grande demais:** acima de 200 linhas consome contexto e pode reduzir a aderência; acima de 4 MiB é pulado; há aviso no início e no `/status`, inclusive quando arquivos dentro do tamanho somam demais. O `/doctor` propõe cortes num CLAUDE.md versionado: tira o que o Claude deriva do código (estrutura de pastas, dependências, visão de arquitetura) e mantém armadilhas, porquês e convenções que fogem do padrão.
- **O fim do CLAUDE.md da subpasta é ignorado:** arquivos que carregam sob demanda têm limite por arquivo (40 mil caracteres com janela de 200 mil tokens; 150 mil a 200 mil caracteres com 1 milhão, conforme o modelo); acima, o Claude recebe só o começo e uma nota para ler o resto.
- **Instrução sumiu depois do `/compact`:** o CLAUDE.md da raiz do projeto é relido do disco e reinjetado; os aninhados e as regras por caminho voltam sob demanda. Se sumiu, foi dada só na conversa: para persistir, ir para o CLAUDE.md.
