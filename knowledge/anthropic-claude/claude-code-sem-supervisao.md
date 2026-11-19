# Claude Code sem supervisão: o que existe e os três buracos

Mapa do que a documentação oficial oferece para um agente trabalhar sozinho num repositório, com assinatura Pro/Max e sem chave de API, e de onde agendar uma rotina. Fontes: *Documentação do Claude Code: o que existe para operação sem supervisão (verificação de 2026-09-20)*, de Subagente de verificação (Claude Code) sobre as docs oficiais da Anthropic (https://code.claude.com/docs/en/), *Use the Claude Agent SDK with your Claude plan (crédito mensal anunciado e pausado)*, de Anthropic (Claude Help Center) (https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan), *Documentação do Claude Code: tarefas agendadas na nuvem, no Desktop, /loop, ambientes, GitHub Actions e claude -p (verificação de 2026-11-16)*, de Anthropic (documentação do Claude Code) (https://code.claude.com/docs/en/routines), *Schedule recurring tasks in Claude Cowork*, de Anthropic (Claude Help Center) (https://support.claude.com/en/articles/13854387) e *API credits for Max, Ultra, and Team plans (a página da plataforma, o artigo de suporte dos créditos e a nota de 07/10 no artigo do Agent SDK)*, de Anthropic (Claude Platform docs e Claude Help Center) (https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers). As docs mudam rápido, então o detalhe se reverifica antes de virar dependência.

## O que existe, por função no laço

| Função | Peça | Como funciona | Limite que importa |
|---|---|---|---|
| Executar sem ninguém | `claude -p` (headless) | Uma chamada por tarefa; `--permission-mode auto`, `--max-turns`, saída JSON com custo, `--mcp-config`; `--permission-prompts none` para quando ninguém responde | Sem painel: só código de saída e JSON; o `--bare` vai virar o padrão do `-p` (abaixo) |
| Impedir o que não pode | Hooks `PreToolUse` com `deny` | Rodam antes da permissão e valem acima de qualquer modo | Precisam de matcher certo por comando |
| Não parar antes de provar | Hook `Stop` com `block` | Recusa encerrar até a condição valer (testes, build) | Combinar com teto de turnos para não girar em vazio |
| Contexto limpo por etapa | Skills `context: fork`, subagentes | Cada etapa em subagente; revisor adversarial em contexto novo | Skill `disable-model-invocation` não dispara sozinha |
| Isolar código | Worktrees | `--worktree`, `isolation: worktree` em subagente | Paralelismo entre tarefas gera merge; dentro da tarefa, não |
| Repetir enquanto houver trabalho | `/loop` na sessão | Ritmo fixo ou dinâmico, a partir de 1 minuto | Expira em 7 dias e exige sessão aberta |
| Rodar com a máquina desligada | Tarefa agendada na nuvem (antes "routine") | Agenda, endpoint `/fire` ou evento do GitHub; repo clonado a cada execução | No mínimo 1 hora entre execuções; mesma cota da assinatura; sem o Claude in Chrome nem MCP local (o ambiente tem um Chrome sem tela) |
| Rodar na máquina, sem sessão aberta | Tarefa agendada local do Desktop | Agenda no app, sessão nova a cada execução, na pasta ou numa worktree | Máquina ligada e acordada, com o app aberto; recupera só uma execução perdida |
| Rodar no GitHub | GitHub Action | Token da assinatura (`CLAUDE_CODE_OAUTH_TOKEN`), gatilho por label ou `schedule: cron`, abre PR | Sem navegador; minutos do runner |
| Ver a tela | Claude in Chrome | Navegar, clicar, console, screenshot, GIF | Janela do Chrome aberta e login claude.ai |
| Revisar | `/code-review` | Funciona em `-p`, com `--fix` e níveis | `/security-review` e `/simplify` não documentados como comandos |
| Decidir por imagem | Artefatos com comentários | Protótipo publicado; comentário "Send to Claude" | Só acorda sessão aberta |
| Medir gasto | `/usage` e custo no JSON | Barras de 5h e 7 dias; custo por corrida; a linha de status recebe o percentual usado das duas janelas | Fora da sessão interativa, sem cota restante legível (buraco 1) |

## Os três buracos e o que cada um muda

**1. Cota restante não é legível fora da sessão interativa.** Nada na API da assinatura devolve a um script quanto falta das janelas de 5 horas e 7 dias. Consequência: um orçamento do tipo "parar com X% de sobra" vira **orçamento calibrado**: teto de tokens por rodada, somado da saída JSON de cada corrida e calibrado lendo o `/usage` depois da primeira rodada; a parada dura é o erro de limite, tratado como fim de rodada, não como falha. Na sessão interativa, a linha de status recebe o percentual usado das duas janelas e a hora em que renovam (o campo `rate_limits`; num dos planos, a janela de 5 horas vem vazia). Se o `claude -p` ou a tarefa agendada expõem o mesmo dado, nenhuma página lida diz, e a documentação das tarefas também não diz quanto uma execução gasta (*Documentação do Claude Code: tarefas agendadas na nuvem, no Desktop, /loop, ambientes, GitHub Actions e claude -p (verificação de 2026-11-16)*, de Anthropic (documentação do Claude Code), "Lacuna"). Para o laço sem supervisão, o orçamento calibrado segue valendo.

**2. Uso programático não tem cota própria.** A Anthropic anunciou um crédito mensal separado para Agent SDK e `claude -p` (US$ 20 no Pro, 100 no Max 5x, 200 no Max 20x) e, no mesmo texto, avisou que a mudança está pausada: SDK, `claude -p` e apps de terceiros seguem gastando a cota da assinatura (*Use the Claude Agent SDK with your Claude plan (crédito mensal anunciado e pausado)*, de Anthropic (Claude Help Center)). Ou seja, o SDK **autentica** com a assinatura, mas compete pela mesma cota do uso interativo. Consequência: o executor pode ser um script em volta de `claude -p` ou um programa sobre o SDK, e nos dois casos o orçamento é o do buraco 1. Quem chama o modelo por fora do binário do Claude Code cai em outra regra, em [[assinatura-em-ferramentas-de-terceiros]].

Depois disso, os planos Max, Ultra e Team passaram a trazer um **crédito mensal na Claude Platform** (US$ 100 no Max, 200 no Ultra, até 500 no Team), pego ao ligar uma organização do Console ao plano; cobre a API, os Managed Agents e o Agent SDK, vence no fim do ciclo e não muda os limites do plano (*API credits for Max, Ultra, and Team plans (a página da plataforma, o artigo de suporte dos créditos e a nota de 07/10 no artigo do Agent SDK)*, de Anthropic (Claude Platform docs e Claude Help Center)). O artigo de suporte dos créditos fecha a dúvida do `claude -p`: com uma chave de API da organização ligada, ele conta como Agent SDK e sai do crédito; com o login do plano, segue na cota da assinatura; e as execuções da **GitHub Action do Claude Code**, de extensão de IDE e do app de desktop contam como Claude Code e **não** saem do crédito, mesmo com `-p`. Quando a organização só tem esses créditos e manda um pedido que eles não cobrem, como uma sessão do Claude Code, o Claude Code mostra "Credit balance too low". *Leitura:* o buraco 2 ganha uma saída só para o `claude -p` ou o SDK chamados por script com a chave da organização, fora da Action; a tarefa agendada segue na cota do plano, e a Action também, com o token OAuth (com uma chave de API, ela é cobrada como API, fora do crédito). A chave da Platform, se usada, convém ficar numa variável de nome próprio, para não tomar o lugar do login do plano no Claude Code.

**3. Comentário só acorda sessão viva.** A resposta automática a comentário de artefato depende de uma sessão aberta observando. Consequência: com a sessão rodando, o comentário chega na hora; fora disso, os comentários **esperam** e são lidos na abertura da sessão seguinte. Não é bloqueio, é cadência.

## Agendar em horário marcado

Quatro jeitos de o Claude Code rodar sozinho numa hora marcada, todos na documentação (*Documentação do Claude Code: tarefas agendadas na nuvem, no Desktop, /loop, ambientes, GitHub Actions e claude -p (verificação de 2026-11-16)*, de Anthropic (documentação do Claude Code)), salvo o cron local, que nenhuma página da Anthropic trata. Um quinto, fora do Claude Code, é o Managed Agent agendado da própria Anthropic (abaixo).

| | Tarefa na nuvem | Tarefa local do Desktop | GitHub Actions | Cron local |
|---|---|---|---|---|
| Onde roda | nuvem da Anthropic | a máquina, pelo app | runner do GitHub | a máquina, pelo agendador do sistema |
| Máquina ligada | não | sim, acordada e com o app aberto | não | sim |
| Intervalo mínimo | 1 hora | 1 hora nos formulários; 1 minuto quando o Claude agenda | o do cron do GitHub | o do sistema |
| Fuso | UTC, ou `CRON_TZ=` | hora local | UTC (cron do GitHub) | o do sistema |
| Execução perdida | não documentado | uma de recuperação, a mais recente dos últimos 7 dias | não lida nesta verificação | não se aplica |
| Repositório | clone novo; empurra para `claude/` salvo prompt que mande outra | a pasta como está, ou uma worktree | o checkout do workflow | a pasta |
| Rede | "Limited" por padrão, com lista de domínios | a da máquina | a do runner | a da máquina |
| Chrome e MCP local | sem o Claude in Chrome (há um Chrome sem tela); conectores do claude.ai ou `.mcp.json` do repo | sim | não | sim |
| Custo | cota da assinatura, como sessão interativa | cota da assinatura (leitura: é uma sessão local comum) | cota da assinatura com o token OAuth, mais minutos do runner; nunca o crédito de API | a da credencial usada |

- **Limites da nuvem:** 100 execuções agendadas por hora por conta; 30 por hora por tarefa somando "Run now", API e reagendar; nenhum tem excedente pago. Está em prévia de pesquisa, e o histórico mostra só como a sessão terminou, não se o trabalho foi feito: quem lê o resultado é a transcrição.
- **O `claude -p` em cron e o `--bare`:** a documentação avisa que o modo bare vai virar o padrão do `-p`; nele a chamada não usa o login da assinatura (pede chave de API) e não carrega `CLAUDE.md`, hooks, skills nem `.mcp.json`. Um cron com `claude -p` montado sobre a cota do plano e as regras do repositório precisa ser revisto quando o padrão mudar.
- **Num projeto** do Claude Code na nuvem, as tarefas agendadas criadas nele aparecem na vista "Scheduled tasks" do projeto, e a execução pode continuar uma thread em vez de abrir sessão nova, com o modo de permissão dela (*Documentação do Claude Code: tarefas agendadas na nuvem, no Desktop, /loop, ambientes, GitHub Actions e claude -p (verificação de 2026-11-16)*, de Anthropic (documentação do Claude Code); os projetos em [[2026-10-30-claude-code-projects-memoria-na-nuvem]]).
- **O Cowork** tem tarefa agendada própria, que roda remotamente mesmo com o computador dormindo; só a que precisa de arquivos ou apps locais roda no computador (*Schedule recurring tasks in Claude Cowork*, de Anthropic (Claude Help Center)). São dois produtos no mesmo app, e a tarefa local do Claude Code segue existindo.
- **O Managed Agent agendado:** o molde de automação da Anthropic roda como Managed Agent e traz as regras de uma leitura agendada: um marcador por fonte em vez da janela fixa de "últimas 24 horas", a fonte que falhou registrada numa linha em vez de passar por dia calmo, e um teto por rodada que pausa em vez de falhar ([[2026-11-13-anthropic-automacoes-de-agente-agendadas]]). O post não diz como a rodada é cobrada; *leitura:* pelos créditos de API, já que o Managed Agent está entre o que eles cobrem.

### O que isso dá a uma leitura automática agendada

*Leitura*, sobre as fontes acima, para uma rotina que lê dados (métricas, uma caixa, um painel) e grava no repositório:

1. **Commitar na branch principal:** a tarefa na nuvem empurra para uma branch `claude/` salvo prompt que mande outra. A proteção de branch do GitHub só segura a tarefa se o acesso conectado não puder contorná-la; se o acesso é o do dono do repositório, só trava uma regra sem exceção para ele. Sem isso, o prompt decide.
2. **Alcançar um serviço de fora:** a rede padrão é "Limited"; cada domínio que a rotina usa (inclusive o da URL pública de um bucket, que costuma ser diferente do endpoint da API) entra em "Allowed domains" do ambiente.
3. **Custo e limites:** a execução gasta a cota da assinatura sem número fixo; a de uma leitura curta, que sai cedo quando não há o que fazer, é pequena, mas só o `/usage` depois da primeira rodada mede (buraco 1).
4. **Execução perdida:** segue sem documentação na nuvem; o Desktop recupera uma.

**Para duas janelas no dia:** a documentação mostra uma tarefa combinando tipos de gatilho (agenda, API, GitHub), não duas agendas na mesma tarefa; duas janelas cabem numa expressão cron com duas horas, mas com um prompt só para os dois trabalhos, ou em duas tarefas. O prompt pode ler um arquivo de calendário e sair cedo. Mudar a própria agenda só está documentado no Desktop, e só com alguém clicando em "Run now" e aprovando, ou seja, nunca numa execução agendada. As regras do molde da Anthropic (o marcador por fonte e a queda registrada) servem a qualquer leitura, qualquer que seja o lugar. O que tem hora exata, como publicar, fica melhor numa rotina determinística (um workflow disparado por relógio) do que numa sessão de modelo.

## Onde cada peça cabe

- **PC próprio** é o único lugar que reúne o Claude in Chrome com o login, MCPs locais e o repositório: é onde o laço completo roda. A tarefa local do Desktop leva esse lugar para uma agenda, com a máquina acordada e o app aberto.
- **Tarefa na nuvem** serve ao que não precisa do navegador com login: caça a lacunas quando uma issue é aberta, revisão noturna, leitura de métricas que já estão no repositório. Gasta a mesma cota.
- **GitHub Action** é o mesmo caso da tarefa na nuvem, com o repositório já no lugar e sem navegador.
- **Agent teams** ficam fora por ora: experimental e caro em tokens.

## O que reverificar a cada ciclo

Nomes de flags e modos de permissão, a lista de eventos de hook, o comportamento de resposta automática de artefatos, se apareceu leitura programática de cota fora da linha de status, os limites e o estado de prévia das tarefas na nuvem, quando o `--bare` vira o padrão do `-p`, e o que os créditos de API dos planos cobrem. Cada item carrega a URL na fonte.
