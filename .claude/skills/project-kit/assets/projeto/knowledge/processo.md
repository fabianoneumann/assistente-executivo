# O processo: como as issues se escrevem e se trabalham

O porquê de cada passo do fluxo que o `CLAUDE.md` lista. Princípio: **a issue é uma spec,** e o agente implementa a partir dela. **Ler quando:** for escrever ou trabalhar uma issue, abrir um PR, ou mudar o fluxo.

## Do macro à sessão

Cinco níveis, do maior ao menor. Os dois de cima moram na base; os três de baixo, no GitHub.

1. **O macro:** a arquitetura (`arquitetura.md`) e os arcos do produto (`plano.md`).
2. **As grandes entregas,** em `plano.md`, com a ordem sugerida e a data de cada revisão dela.
3. **A milestone,** de cerca de duas semanas, fechada por critério, e não pela data. Quando dois relógios diferem (a data de alguém de fora e o escopo da equipe), duas milestones andam em paralelo.
4. **A issue,** escrita como spec.
5. **A sessão,** que trabalha uma issue pelos oito passos.

## A issue é uma spec

O modelo está em `.github/ISSUE_TEMPLATE/spec.md`. Os "Requisitos" dizem só o quê; o como fica para o plano da sessão. O "Pronto quando" é o contrato da validação da entrega. O defeito tem modelo próprio, e o primeiro critério dele é um teste que falha antes da correção e passa depois.

- **O corpo carrega o estado, o comentário carrega a conversa.** A spec se edita no lugar. A fala dirigida a alguém não se reescreve. O comentário que afirma como atual algo que já não vale ganha o prefixo "superado, ver a descrição", em vez de ser apagado.
- **Perguntas e ideias vivem na issue,** no campo "A decidir", com quem decide. Antes de pôr uma pergunta, conferir o que o código e os dados respondem. A ideia que ainda não é entrega nasce como issue curta (Objetivo e Pronto quando).
- **Quem preenche é quem fecha.** A parte deixada para depois vira critério da issue que a preenche, apontada pelo número. Nunca um TODO solto no código, nem um "em breve" à vista de quem usa.
- **Knowledge-in-the-loop.** A issue que contraria a base corrige a base na mesma entrega, e a correção entra no "Pronto quando".
- **Buscar antes de criar, atribuir ao pegar.** Antes de abrir, buscar a mesma ideia nas abertas e nas fechadas (`gh issue list --state all --search "<termos>"`); achou, o escopo vai ao corpo dela. Quem pega a issue se atribui a ela.
- **O agente abre a issue por arquivo:** lê o modelo, preenche sem o cabeçalho YAML e sem os comentários, passa o texto pela pessoa e cria com `gh issue create --body-file`. Depois preenche a lateral (`metadados.md`).

## Os oito passos, e por quê

1. **A discussão inicial** confronta a spec com o código e a base de hoje. Fica pronta quando dá para escrever o plano sem adivinhar. O que ela acha tem lugar: a dúvida resolvida vai às "Decisões travadas", com a data; a que não se resolve fica no "A decidir"; a spec que contraria a base põe a correção no "Pronto quando". Sem estado a atingir, um passo é uma intenção.
2. **O plano e o aceite:** a pessoa decide aqui, antes de qualquer código.
3. **Uma branch por issue,** `<issue>-<tema>`, numa worktree. A branch que depende de um PR aberto não se cria: esperar o merge é mais simples que empilhar e refazer a pilha depois do squash.
4. **Implementar.**
5. **O `/code-review`** sobre a branch. As correções de uma rodada de revisão entram num commit só.
6. **A validação da entrega vem antes do PR,** com a exploratória: o "Pronto quando" como roteiro, contra o sistema rodando. O ajuste que ela pede entra na mesma branch, e o PR nasce completo. O achado de ambiente se separa do defeito do sistema.
7. **Sincronizar antes do PR,** porque o CI de um PR só prova contra a base que ele viu: dois PRs que escrevem no mesmo arquivo passam sozinhos e quebram juntos. O PR leva `Closes #N`, ou `Refs #N` quando a entrega é uma etapa, e o checklist do modelo preenchido. O checklist é uma declaração do que se fez, com a evidência; o hook confere que ele está preenchido, e não pergunta nada.
8. **As divergências** (o que saiu diferente da spec) ficam no PR, e as issues relacionadas se ajustam. Se a base andou enquanto o PR esteve aberto, sincroniza-se de novo. O merge é por squash, um commit por issue, assim que validado: o PR aberto "para depois" é a exceção, e não a fila.

## O fechamento vive no commit

- A issue fecha pelo `Closes #N` do corpo do PR, que o squash leva ao commit no `main`. Não se escreve um comentário só para repetir isso; o comentário de fechamento fica para o desvio que o commit não deixa óbvio.
- O PR de uma **etapa** leva `Refs #N` e diz o que ainda falta. É aí que a caixa parcial do corpo da issue ganha função; na entrega de uma tacada, marcar caixa é ruído, e marcar depois pode mentir.
- **O PR que depende do deploy de outro sistema não entra no `main`** enquanto a dependência não estiver no ar: a versão nasce do `main`, e a funcionalidade quebrada iria na próxima. Ou se espera o deploy, ou se esconde a entrada.

## As trilhas à parte

- **O PR do Dependabot** nasce de um alerta, sem issue e sem modelo; a triagem está em `versao-e-dependencias.md`.
- **A base:** o commit que só muda a base pode ir pelo fluxo inteiro ou num PR curto, mas sempre depois de a pessoa validar o texto.

## Os diagramas e o onboarding

- **Os diagramas são HTML com SVG escrito à mão,** no repositório, claro e escuro, com a legenda citando o arquivo da base ou do código de onde saíram. O fonte fica versionado e muda na mesma entrega que a regra que desenha.
- **O onboarding é sempre em páginas HTML,** em `onboarding/`, com a data da última atualização no rodapé, e muda na mesma entrega que o processo.
- **O que pegar agora** é a busca salva do `metadados.md`, que mora no onboarding e na descrição de cada milestone. Não há quadro de projeto.
