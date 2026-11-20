# As travas: as regras do fluxo que viraram código

As regras do `CLAUDE.md` que dependiam de alguém lembrar viram código versionado no repositório, e valem em qualquer computador. **Ler quando:** uma trava recusar um comando, ou for mudar o fluxo, o CI ou um hook.

## A regra das camadas

O lembrete que se repete vira código, **na camada mais baixa que resolve:**

| Camada | Vale para | Chega como |
|---|---|---|
| O CI (`.github/workflows/ci.yml`) | todos, no PR e no push ao `{{BASE}}` | já está no repositório |
| Os hooks do git (`.githooks/`) | pessoas e agentes | `python .githooks/hooks.py instalar`, uma vez por clone |
| As permissões e o hook do agente (`.claude/settings.json`) | o agente no Claude Code | com o clone |

Não há plugin nem linha de estado sob o prompt: bastam o hook e o CI.

## A fronteira: a trava recusa e diz o que falta, e nunca pergunta

Toda trava daqui recusa o comando do agente com o motivo, ou avisa, e ele corrige e roda de novo. **Nenhuma pede à pessoa um sim ou não, ou um 1 ou 2, para liberar um comando.** Por isso o `.claude/settings.json` não tem `ask`, e nenhum hook pergunta. A pergunta de liberar ensina a pessoa a dizer sim sem ler, e trava o agente que trabalha sozinho.

Fica, do lado de cá da fronteira:
- **a recusa que diz o que falta** (o corpo do PR sem o modelo, a branch atrás, o CI vermelho, o arquivo fora do formato);
- **o checklist do PR,** que é a declaração do agente, com a evidência, e que o hook só confere se está preenchido;
- **a regra de conteúdo,** escrita e sem trava: a base validada pela pessoa na conversa antes do commit do agente (`CLAUDE.md`);
- **o aviso** de que uma trava não conferiu (sem rede, sem Python, com os hooks do git desligados).

Uma regra nova que pareça pedir uma pergunta vira recusa com o motivo, regra escrita, ou fica fora. Não volta como pergunta.

O pedido de permissão do próprio Claude Code (o comando que a pessoa não liberou nas configurações dela) não é trava do projeto: é de quem trabalha, e o projeto não acrescenta nenhum.

## O que cada trava cobra

| Trava | Onde | O caso que ela pega |
|---|---|---|
| O corpo do PR é o modelo preenchido | o hook, no `gh pr create` | o `--fill` e o `--body`; a falta do `--body-file`; o corpo dentro do repositório; o comentário `<!--` que ficou; o `Closes #` sem número; a falta da seção "Antes de abrir este PR"; a caixa vazia no checklist |
| Enviado e sincronizado antes do PR | o hook, no `gh pr create` | a branch que não foi enviada, o commit que não está no remoto, e a branch atrás da base do remoto |
| O CI verde antes do squash | o hook, no `gh pr merge` | o check vermelho, o que ainda roda, e o PR sem check nenhum, lidos do `gh pr checks --json` (o código de saída sozinho confunde a falha do CI com a da rede). O `--auto` passa: o GitHub espera o CI |
| Uma chamada própria | o hook, no `gh pr create` e no `gh pr merge` | a linha encadeada (`git push && gh pr create`), em que o hook julgaria o estado de antes do push |
| Os hooks do git ligados | o hook, no `git commit` | só avisa: o commit sairia sem o formato e o log conferidos |
| O formato | o `pre-commit` | o arquivo fora do padrão, na versão do índice, que é a que vai no commit. Não reescreve nada, porque quem preparou só parte de um arquivo perderia o resto |
| O log em ordem | o `pre-commit` e o CI | o cabeçalho partido, a entrada fora do formato e a data que não existe; no `pre-commit`, também a entrada que não vai no fim (as que já estavam no `HEAD` continuam no começo, na mesma ordem). A ordem das datas não se confere: com o `merge=union`, duas branches que escrevem no fim juntam as entradas na ordem do merge, e o commit de merge fica de fora |
| O roteador e a base sem deriva | o CI (`.github/scripts/conferir_base.py`) | o caminho ou o comando do `CLAUDE.md` que não existe, o passo do CI que o `CLAUDE.md` não lista, a página do `index.md` que não existe; só avisa a página órfã e o código que a base cita e saiu |
| A base atrás | o `pre-push` | só avisa, e o push segue; quem recusa o PR atrasado é o hook do agente e o CI |
| Nunca ler credencial | o `deny` do `.claude/settings.json` | o `.env`, o `.env.local` e o `.env.production` pela ferramenta Read e pelos comandos de leitura que o Claude Code reconhece; o `.env.example` segue legível. Um `.env.*` no `deny` negaria também o `.env.example`, porque o `deny` vence qualquer `allow`: outra variante entra pelo nome |
| Não pular os hooks | o `deny` | o `--no-verify`, o `git commit -n` no começo das flags, o `git config --unset core.hooksPath` e o `git -c core.hooksPath` |

## Como o hook é feito

- **Uma casca fina sobre lógica testada:** o `.claude/hooks/fluxo.sh` acha o Python e chama o `fluxo.py`, que só usa a biblioteca padrão; os testes, em tabela, estão em `test_fluxo.py` e rodam no CI. Cada recusa é testada também sem a trava, para provar que é ela que pega.
- **Passar é não imprimir nada.** O `allow` de um hook pularia o pedido de permissão de quem trabalha. A recusa é o `permissionDecision: "deny"`, com o motivo; o aviso, o `additionalContext`.
- **Sem rede, deixa passar e avisa.** A trava existe para lembrar, e não para prender o trabalho fora da rede. Uma conferência que falha não impede as outras. As chamadas cabem em 25 s, abaixo dos 30 s do hook, porque o hook morto pelo prazo passaria calado.
- **O Bash e o PowerShell têm as mesmas entradas,** porque no Windows o PowerShell pode ser o shell do agente.
- **Fora deste repositório** (outro clone, um `-R`), o hook passa: as regras são deste projeto.

## Os limites assumidos

- **O `deny` lê o comando como texto.** As formas que ele não prevê escapam (as flags curtas juntas depois de outra, como `git commit -m x -n`, ou um `alias`). A trava protege do engano, e não de quem a contorna de propósito; o CI confere de novo o formato e o log.
- **Sem Python 3.9 ou mais novo no PATH,** o hook e os hooks do git avisam e deixam passar. A trava real fica no CI.
- **As travas do `.claude/` valem para o agente no Claude Code.** As pessoas e os outros agentes têm os hooks do git e o CI.
- **Sem os hooks do git ligados,** o formato e o log só se conferem no CI. O hook do agente avisa a cada commit.
- **A regra de tag do GitHub** pode pedir um plano pago em repositório privado; sem ela, a tag fica protegida só pela regra escrita (`versao-e-dependencias.md`).

## Quem não quiser

- **Os hooks do agente:** `"disableAllHooks": true` no próprio `.claude/settings.local.json`, que não vai ao git. Ele desliga todos os hooks, os do projeto e os seus.
- **O `deny`** não se desliga por arquivo local: ele vale contra qualquer `allow`.
- **Os hooks do git:** `git config --unset core.hooksPath` desliga neste clone (pela pessoa, num terminal).
