# Distribuir um ambiente de assistente com Claude Code a uma equipe

Como levar um conjunto de skills, `CLAUDE.md`, agentes e hooks a uma equipe, num repositório pronto para clonar, e a quem não programa sem terminal. A documentação da Anthropic muda rápido: reler antes de decidir. As páginas de documentação não trazem data; o que depende de versão está dito com a versão.

**As fontes:**
- *Documentação do Claude Code: plugins na organização, carregamento, criação e referência do marketplace (leitura de 2026-11-17)*, de Anthropic (documentação do Claude Code) (https://code.claude.com/docs/en/plugins/org);
- *Documentação do Claude Code: skills, exemplo de settings, kit do campeão e app de desktop (leitura de 2026-11-17)*, de Anthropic (documentação do Claude Code) (https://code.claude.com/docs/en/skills);
- *Documentação do claude.ai: plugins e skills da organização, sincronia de repositório, suporte por superfície e provisionamento (verificação de 2026-11-17)*, de Anthropic (documentação do claude.com e Claude Help Center) (https://claude.com/docs/plugins/org-rollout);
- *Claude Cowork, a experiência que junta chat e Cowork, os conectores do Google e os Projects (central de ajuda e claude.com, leitura de 2026-11-17)*, de Anthropic (Claude Help Center e documentação do claude.com) (https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork);
- *my-skills (README do repositório)*, de Fabio Akita (https://github.com/akitaonrails/my-skills);
- *Falando um pouco sobre minhas Skills de IA*, de Fabio Akita (https://www.akitaonrails.com/2026/09/17/falando-um-pouco-sobre-minhas-skills-de-ia/);
- [[2026-11-17-karpathy-idea-file-e-claude-md-local]].

Em citação, sem ficha: as issues 32606 e 16625 do `anthropics/claude-code`.

**As vizinhas:**
- [`plugins-e-marketplaces.md`](plugins-e-marketplaces.md): o que o plugin empacota, as versões e os caminhos;
- [`complementos-do-claude-code.md`](complementos-do-claude-code.md): o que ligar de terceiro;
- [`aprendizado-entre-sessoes.md`](aprendizado-entre-sessoes.md): os Projects e a memória;
- [`claude-code-sem-supervisao.md`](claude-code-sem-supervisao.md): as tarefas agendadas, do Cowork inclusive.

## As rotas para levar o ambiente

| Rota | O que chega | O que cada pessoa faz | Onde vale |
|---|---|---|---|
| **O clone** (`CLAUDE.md`, `.claude/skills/`, `.claude/agents/`, hooks no `.claude/settings.json`) | tudo o que está commitado | clona e aceita a confiança da pasta | só no Claude Code (terminal, IDE, aba Code do app); não nas threads de nuvem de um projeto |
| **O plugin dentro de `.claude/skills/`** (uma pasta com `.claude-plugin/plugin.json`) | o plugin, como `<nome>@skills-dir`, sem marketplace e sem instalação | só a confiança da própria pasta (não basta a pasta-pai, nem o `-p`). Liga pelo `defaultEnabled` do manifesto, cujo padrão estas páginas não dão, salvo um settings que o fixe | Claude Code, a partir do diretório de trabalho principal. Ficam sem carregar, sem erro: com managed settings que tenham uma allowlist sem `skills-dir`, com `blockedMarketplaces` com `skills-dir`, ou com qualquer tipo travado em `strictPluginOnlyCustomization`. O `SKILL.md` da raiz da pasta segue como skill comum |
| **O marketplace no mesmo repositório** (`.claude-plugin/marketplace.json` com fonte relativa `./plugins/<nome>`, ou `./` na raiz) mais `extraKnownMarketplaces` e `enabledPlugins` no `settings.json` | o catálogo, registrado depois da confiança | `claude plugin install <nome>@<marketplace> --scope project`. Há três exceções. O marketplace local (`directory` ou `file`) com fonte relativa carrega sem nada a rodar, e o caminho se resolve contra o checkout principal, também numa worktree. No marketplace git, o plugin por fonte relativa carrega com `/reload-plugins`, só naquela sessão. O plugin de fonte externa só se busca quando o `true` vem das configurações do usuário, de um `settings.local.json` fora do git, do `--settings` ou das managed settings, e nunca do `settings.json` do projeto sozinho | Claude Code; a sessão na nuvem não adiciona os marketplaces do repositório |
| **A conta no claude.ai** (Customize > Plugins ou Skills; na organização, o Owner) | o plugin ou a skill na conta da pessoa | sobe o ZIP ou adiciona o marketplace do GitHub ou do GitHub Enterprise, até 25 por conta em cada organização. O plugin tem até 5.000 arquivos e 200 MB | chat, Cowork e o Claude Code que entra com a conta (versão 2.1.273 ou mais nova) |

O plugin no repositório passa pela mesma confiança das regras de projeto. Os MCP que ele declara pedem aprovação por servidor, e os monitores em segundo plano não carregam. Marketplace em repositório privado pede, de cada pessoa, acesso de leitura e as credenciais git da máquina. Para quem não tem conta no host git, a documentação oferece o seed (`CLAUDE_CODE_PLUGIN_SEED_DIR`), pensado para contêiner e CI.

Quando dois plugins têm o mesmo nome, a ordem de quem vence é esta:
- o de marketplace instalado vence o de `.claude/skills/`;
- entre dois de `.claude/skills/`, o de `~/.claude/skills/` vence o do projeto;
- o sincronizado da conta perde para todos.

A sincronia da conta não roda com credencial por token (`ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN`, `apiKeyHelper`), no modo bare ou `--safe-mode`, nem com `--setting-sources` sem `user`.

**O que o repositório muda para todos:**
- uma skill de projeto chamada `verify` ou `simplify` faz o Claude rodá-la antes de cada commit (a partir da v2.1.286), e o `/verify` pode gravar a própria receita em `.claude/skills/verify/`;
- o `allowed-tools` de uma skill de projeto vale até num `-p` em pasta nunca confiada, e a documentação manda revisar antes de rodar;
- as variáveis de telemetria do `settings.json` do repositório são ignoradas;
- a aba Code do app tem uma cópia própria do Claude Code, que pode estar em versão diferente da do terminal;
- no Windows sem Git Bash, a skill com `shell: bash` falha, e sem o campo os comandos `!` vão pelo PowerShell.

**Quando a Anthropic manda virar plugin:** "Make a plugin when you want to share the setup with teammates, install it in several projects, or publish versioned releases". Ao virar plugin, as skills ganham o prefixo (`/plugin:skill`) e mudam de pasta. Para a sincronia da organização no claude.ai, o repositório no github.com ou no gitlab.com tem de ser privado ou interno, o plugin privado fica dentro dele por caminho relativo, e um plugin com `bin/` na raiz é recusado. Para quem tem organização (Team ou Enterprise), a página do rollout usa o mesmo repositório-marketplace para as duas rotas que descreve, as configurações da organização no claude.ai e as managed settings, e diz que "One plugin folder can serve both audiences" (chat, Cowork e Claude Code). O projeto e o marketplace no mesmo repositório vêm de outras páginas: a referência do marketplace dá a fonte relativa, e `plugins/org`, a exceção do marketplace local.

## O que cada superfície carrega de um plugin

| Componente | Chat | Cowork | Claude Code |
|---|---|---|---|
| Skills | carrega | carrega | carrega |
| Comandos | vira skill | carrega | carrega |
| Agentes e hooks | ignora | carrega | carrega |
| MCP remoto (URL fixa) | depois de conectado na aba Connectors | idem | carrega |
| MCP local | ignora | quando a sessão roda no computador | carrega |
| `settings`, LSP, temas | ignora | ignora | carrega |
| Executável em `bin/` | recusa o plugin | recusa o plugin | carrega |

Chat e Cowork leem da conta; o Claude Code lê da máquina. O que se instala na conta aparece no Claude Code como plugin sincronizado. O que se instala pela linha de comando fica na máquina e não volta à conta.

## Quem não programa

- **O Cowork** usa a mesma arquitetura do Claude Code, sem terminal. Está nos planos pagos; o app roda no macOS, no Windows e no Linux (beta). Roda na nuvem, e arquivo local, navegador e uso do computador pedem o app do macOS ou do Windows aberto e conectado. As permissões de saída de rede não valem para o web fetch, a busca web e os MCP.
  - Pede permissão antes de apagar arquivo. O Cowork separado tem três modos de aprovação (Manual, Auto, Skip). Na experiência nova, que junta chat e Cowork, o seletor tem dois: o Auto, que vira o padrão no Pro, Max, Ultra e Team, e o Manual, padrão no Enterprise.
  - Tem instruções globais e instruções da pasta selecionada, projetos e tarefas agendadas na nuvem.
  - Chat e Cowork estão virando uma experiência só, em liberação gradual no Pro, Max e Ultra; no Team e no Enterprise, onde ela está ligada.
- **O Cowork não lê o `~/.claude` da máquina:** carrega as skills, os plugins e os conectores da conta. O que ele faz com a `.claude/` de uma pasta clonada não está escrito em nenhuma página lida.
  - *Leitura do assistente:* até o teste, a rota garantida para quem não usa o Claude Code é a conta.
- **A skill que sobe à conta** (o ZIP no Customize, que é também o jeito de levar uma skill pessoal ao Cowork e à nuvem):
  - aceita só seis campos no frontmatter (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`), e outro campo faz o envio falhar com erro;
  - por isso uma skill com `disable-model-invocation`, `context: fork`, `argument-hint` ou `paths` não sobe como está;
  - a injeção `!` não roda no claude.ai nem no Cowork, que a trocam por um aviso;
  - no terminal, a skill sincronizada da conta não roda `!`, não anexa `@` e não substitui `${CLAUDE_PROJECT_DIR}`.
- **Skills no claude.ai:** pedem "Code execution and file creation" ligado. As que alguém compartilha ou sobe não passam por revisão da Anthropic. Os Projects são contexto sempre carregado, e a skill é procedimento carregado quando o pedido casa.
- **Os conectores do Google:**
  - a central de ajuda diz que o Gmail busca, lê, rascunha e envia, responde e encaminha com aprovação por padrão, e que o Calendar cria, muda e apaga evento;
  - as páginas do Gmail e do Calendar no claude.com dizem "reads [...] only". Divergem também no plano: a central diz "all users", e o claude.com diz Pro ou acima;
  - são duas páginas da Anthropic lidas no mesmo dia, sem conciliação na fonte. *Leitura do assistente:* a da central é mais detalhada e fala dos modos de aprovação recentes, o que sugere que a do claude.com ficou atrás. Confirmar num teste.
- **Na organização** (Team ou Enterprise), só o Owner provisiona skill e plugin; o papel "Admin" não abre a página. A organização define a disponibilidade de cada plugin (Not available, Available, Installed by default, Required) e conecta os conectores, que cada membro liga com a própria conta. O membro pode compartilhar a skill dele com pessoas da organização. A skill fica desligada até quem recebe ligar, e grupo existe só no Enterprise. Item sincronizado de repositório não se reverte pela página: corrige-se no repositório e se faz o Re-sync. No Enterprise, uma varredura de segurança passa, avisa ou bloqueia. As fontes descrevem provisionamento, compartilhamento e disponibilidade só no Team e no Enterprise, e não dizem se uma conta Pro ou Max avulsa compartilha com outra. *Leitura do assistente:* com contas avulsas, conte com cada conta subindo o próprio ZIP ou o próprio marketplace.
- **Exige o Claude Code:** os `settings`, LSP e `bin/` de um plugin. A documentação descreve a pasta `.claude/` do repositório só para o Claude Code, e o que o Cowork faz com ela está por testar. A aba Code do app instala plugin sem terminal. Só a sessão em worktree pede o Git; no Windows, desde a versão 1.49585.0 do app, a sessão local comum não pede.

## O onboarding e o `.env.example`

- **O kit do campeão** (adoção na equipe):
  - postar o prompt de verdade, responder em público uma vez e linkar depois;
  - o `/team-onboarding`, que lê as sessões, os comandos e os MCP de quem já usa o projeto e gera um guia que o colega novo cola como primeira mensagem;
  - postar o `SKILL.md` mais útil, porque "colleagues can adopt them immediately".
- **A skill embutida `/run-skill-generator`** grava a receita de setup (instalação, variáveis, comando) como skill do projeto, para commitar.
- **O `.env.example`:** não há página da Anthropic sobre ele.
  - O exemplo de settings da equipe nega `Read(./.env)` e `Read(./.env.*)` e avisa que o deny sozinho não barra um `grep -r` sobre a pasta, brecha que o bloco `sandbox` fecha.
  - *Leitura do assistente:* o padrão `.env.*` esconde do Claude o próprio `.env.example`, e o desenho escolhe entre os dois.

## As três referências

- **Akita:** "não use as skills dos outros", nem as dele. Os motivos, na primária:
  - o contexto: outra stack, outros riscos, e a skill que carrega "someone else's assumptions, paths, and credentials layout";
  - o risco: rodar instruções alheias com as próprias permissões, nos próprios repositórios, com os próprios tokens.
  
  Ele distribui só para si, por links simbólicos de um repositório-mestre para cada harness, e o README não lista plugin próprio. As skills de avaliar a equipe e os parceiros (`assess-team`, `assess-partners`) ficam num remoto privado, porque o repositório é público e a metodologia de avaliação não pode ir a público. O README e o post não trazem método para distribuir skills a uma equipe.
- **Karpathy:** o idea file, para colar no agente de cada um, que monta a própria versão. O esquema (o `CLAUDE.md` ou o `AGENTS.md`) é algo que cada um evolui com o próprio modelo. No nanochat, o `CLAUDE.md` fica no `.gitignore`, sob "Local setup". O gist e o `.gitignore` não falam de distribuir configuração a uma equipe: o gist cita a equipe só como um uso do wiki ("an internal wiki maintained by LLMs"), e o "CLAUDE.md do Karpathy" que circula é comunitário.
- **Anthropic:** o plugin, para compartilhar com colegas e instalar em vários projetos; a conta, para quem usa chat e Cowork; e, na organização, o mesmo repositório-marketplace para as configurações da organização e para as managed settings. O projeto e o marketplace no mesmo repositório, acima, em "Quando a Anthropic manda virar plugin".

**As tensões:**
- **O mesmo repositório ou separado.** Perplexity e Gemini mandavam separar, sem primária, e a Anthropic documenta o mesmo. *Leitura do assistente:* o argumento deles pesa se as skills forem a vários repositórios de produto.
- **Skills prontas contra "skill boa é a sua".** Do lado da Anthropic, o kit do campeão manda postar o `SKILL.md` mais útil, porque "colleagues can adopt them immediately". *Leitura do assistente:* nenhum dos dois motivos do Akita some porque o autor é conhecido. A skill que roda nos repositórios e com os tokens de uma equipe é instrução de fora para ela.

## O desenho deste repositório

Sobre as rotas e as tensões acima, este repositório segue três escolhas:
1. **Contas avulsas:** sem organização no claude.ai, cada pessoa instala. Para quem não programa, a rota é o Cowork no app, com as skills na própria conta.
2. **Um repositório que é projeto e marketplace**, como a Anthropic documenta: quem clona usa as skills como projeto, e quem quer só o plugin o instala pelo marketplace do mesmo repositório.
3. **As skills vão prontas,** com o que é de cada projeto isolado num `references/projeto.md` de cada uma. O README diz o que cada uma faz, o que lê e o que pode rodar, para a equipe revisar antes de ligar e reescrever a sua, que é a advertência do Akita.

Com contas avulsas, as rotas da organização (provisionar, Required, sincronia do repositório pelo Owner) não se aplicam. O que fica: o clone, o plugin em `.claude/skills/` ou o marketplace no repositório para quem usa o Claude Code, e o ZIP ou o marketplace do GitHub na conta de cada um para o Cowork. *Leitura do assistente:* as skills que vão à conta para o Cowork precisam caber nos seis campos de frontmatter do upload, sem a injeção `!`.

## Não verificado

- **A versão das mudanças:** o plugin em `.claude/skills/` teria começado na v2.1.157 (claudeissues.com, item 63770), e o plugin de fonte externa deixaria de se instalar sozinho a partir da 2.1.195 (Horadecodar). Os dois comportamentos conferem com a documentação; as versões não foram conferidas.
- **O Cowork e o `CLAUDE.md` da pasta:** que ele lê o `CLAUDE.md` da pasta selecionada vem de guias de terceiros, e há um relato de que não segue com regularidade a instrução de nível de projeto (claudeissues.com, item 84229).
- **O app no Windows:** a página do app diz que a aba Code roda "its own copy of Claude Code", que o app baixa e atualiza. Que isso dispensa o Node e a CLI vem do resumo de uma busca, e a página não diz. Há também um bug de junho de 2026, dado como resolvido, em que os plugins apareciam sem skills (claudeissues.com, item 64763).
- **A issue 32606:** relato de bug fechado por inatividade em 09/04/2026, sem decisão de produto. A 16625, o envio de skill da organização com "File not found", fechada em 17/03/2026. É só histórico.

## A testar

- O que o Cowork faz com a `.claude/` e o `CLAUDE.md` de uma pasta clonada e selecionada.
- Se o Gmail envia e o Calendar cria evento, ou se só leem.
- O plugin em `.claude/skills/` e o marketplace local com fonte relativa, num clone do zero.

Antes de prometer qualquer um dos três à equipe, o teste vem primeiro.
