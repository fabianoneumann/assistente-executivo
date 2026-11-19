# Os metadados da issue: uma dimensão, um lugar

Cada coisa que se quer saber de uma issue mora num lugar só: o campo nativo do GitHub onde ele tem um, e o rótulo só para o que ele não tem. **Ler quando:** for abrir uma issue e preencher a lateral, ou buscar o que pegar agora.

| Dimensão | Onde |
|---|---|
| Natureza | [kit:conta=org]o **Type** (Bug, Feature, Task)[kit:fim][kit:conta=user]o rótulo `defeito`, que o modelo de defeito já põe; o resto não leva rótulo (o Type nativo só existe em organização)[kit:fim] |
| Prioridade | [kit:conta=org]o campo **Priority** da organização (Urgent, High, Medium, Low)[kit:fim][kit:conta=user]os rótulos `prioridade:urgente`, `prioridade:alta`, `prioridade:media` e `prioridade:baixa` (o campo nativo só existe em organização)[kit:fim], pela matriz de Eisenhower |
| Bloqueio | o **"blocked by"** nativo do GitHub, que é da issue inteira e é o que a busca enxerga |
| Prazo | a **milestone** |
| Dono | o **assignee**, que quem pega a issue põe antes de começar |
| Decisão em aberto | o campo "A decidir" do corpo |
| Notas da versão | o rótulo `dependencies`, de PR, que o `.github/release.yml` lê |

Sem rótulos de forma (código, doc, estudo): a natureza já tem lugar, e o que se faz está no título. Sem quadro de projeto: a busca abaixo responde o que pegar.

## A prioridade pela matriz de Eisenhower

Estar numa milestone aberta é o que torna a issue **importante**; a **urgência** vem do prazo externo e do bloqueio.

- **Urgente:** data externa próxima, ou defeito numa versão instalada, com ou sem milestone.
- **Alta:** é o último bloqueio aberto de outra issue, e fechá-la deixa a outra livre. O bloqueio de uma issue que ainda espera outras não sobe a prioridade.
- **Média:** numa milestone aberta, sem urgência. **Baixa:** sem milestone.
- O urgente e não importante, resolve quem é responsável pela issue. Nem um nem outro, fecha como "not planned", com o motivo.

Quem abre a issue preenche os campos. A prioridade se revê no fechamento de cada milestone e quando uma issue fecha ou destrava outra.

A mesma régua em árvore de decisão, as três perguntas na ordem em que se fazem: `onboarding/diagramas/prioridade.html`.

## O que pegar agora

A busca `is:issue is:open no:assignee -is:blocked`, que mostra o rótulo (ou o campo) de prioridade de cada uma, para quem escolhe começar pela mais alta (a busca do GitHub não ordena por rótulo), com o link no onboarding e na descrição de cada milestone aberta (filtrada por `milestone:"<nome>"`): https://github.com/{{REPO}}/issues?q=is%3Aissue+is%3Aopen+no%3Aassignee+-is%3Ablocked

## Para o agente

- **Buscar** com `gh issue list --search "<busca>"`, que usa a busca avançada (`is:blocked`, as exclusões). A REST `search/issues` pelo `gh api` ignora o `is:blocked` e devolve um subconjunto errado com cara de certo.
- **O bloqueio** pela GraphQL: `gh api graphql -f query='mutation { addBlockedBy(input: {issueId: "<id>", blockingIssueId: "<id>"}) { issue { number } } }'`, com os ids de `gh issue view N --json id`.
[kit:conta=org]- **O Type e a Priority** também só pela GraphQL, porque o `gh` não os grava: `updateIssueIssueType(issueId, issueTypeId)`, com os ids em `organization.issueTypes`, e `setIssueFieldValue`, com o cabeçalho `GraphQL-Features: issue_fields` e os ids em `organization.issueFields`.
[kit:fim][kit:conta=user]- **A prioridade e o defeito** pelo `gh issue edit N --add-label prioridade:media`.
[kit:fim]- **O índice da busca atrasa** depois de gravar: conferir pela própria issue (`gh issue view`), e não pela busca.
