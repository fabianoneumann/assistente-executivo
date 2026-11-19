# Revisão de texto e de código: a skill `review` e o `/code-review`

## Código ao `/code-review`, texto à `review`, os achados dos dois pela mesma conferência

**Decisão:** quem revisa depende do objeto, não da tarefa.

- **Código** (script, teste, programa): o `/code-review` do Claude Code, sobre o diff, em nível baixo por padrão; o médio quando o código é o trabalho principal. `max` e `ultra` só por pedido explícito, porque disparam muitos agentes e o `ultra` é cobrado à parte.
- **Texto, regra, rubrica e instrução de skill:** a skill `review`. A lente "executor" dela roda os comandos escritos no markdown, que o `/code-review` não lê como código.
- **Trabalho misto** (uma skill com script, uma rubrica com o código que a aplica): os dois. A `review` revisa o texto e chama o `/code-review` para o código; os achados dele entram na conferência da `review` como os de qualquer agente que acha, e a entrega é uma só.

**Motivo:** rodados os dois sobre a mesma edição (texto de skill e um script novo), nenhum pegou o que o outro pegou. O `/code-review` achou os erros de lógica do script (um número calculado por contagem que colidia quando faltava um item; um formato que o script não reconhecia), que a revisão de texto tinha dado como resolvidos; a revisão de texto achou os problemas de regra e de registro (uma regra que ficou para trás em dois lugares, um campo que nenhum pedido mandava preencher), que o `/code-review` não olha. E o `/code-review` custou menos da metade.

**Por que os achados do `/code-review` passam pela conferência:** no nível médio ele entrega candidatos sem verificação, e parte deles não se sustenta; um achado derrubado mandava trocar uma chamada que já funcionava por outra mais complicada. Aplicar sem conferir leva a correção que piora o código. O achado de código que vem com execução e cenário concreto dispensa a conferência por outro agente; o de texto, não.

**Alternativas consideradas:**
- *Só a `review`, com uma lente de lógica de código:* ela leu o script e não achou os erros de lógica; o `/code-review` foi feito para isso.
- *Só o `/code-review` no trabalho misto:* ele não lê as réguas do projeto (só conhece o `CLAUDE.md`), nem os comandos escritos no markdown.

## O nível baixo lê só o diff

O nível baixo do `/code-review` lê só o diff numa chamada e responde `(none)` quando não há achado no trecho. Por isso o arquivo novo, fora do git, entra nele marcado com `git add -N <caminho>` (passar só o caminho não o põe no diff); o `(none)` conta como "nada no trecho do diff", não como falha a repetir. Por quê: sem a marca, o script novo não é lido, e o vazio parece revisão. Testado com erros plantados num script novo marcado assim: o baixo achou os dois, também rodando sem interface (`claude -p`), o que abre o uso em automação.

## Re-revisão: o que mudou, uma rodada

**Decisão:** na re-revisão do trabalho corrigido, a conferência fica nos críticos e maiores, e roda uma só, dos trechos mudados; a segunda rodada só por pedido de quem recebe a entrega (a aprovação de uma correção que reescreve trecho conta como esse pedido). Depois do nível rápido, a re-revisão padrão só é obrigatória quando a correção reescreve regra ou decisão. O nível padrão fica para pesquisa, decisão e peça; o rápido, para arrumação e edição pequena.

**Motivo:** na prática, a conferência dos menores quase nunca derruba achado, e as re-revisões chegam a um terço ou mais do custo nas revisões grandes. É a mesma escolha do Code Review da Anthropic, que revê só o que mudou quando o trabalho volta e limita os miúdos. **Risco aceito:** uma segunda rodada às vezes ainda acha um maior, que agora só aparece se ela for pedida.

## Fichas de obra protegida reescritas

Quando a correção reescreve fichas de obra protegida pela lente de conteúdo próprio, os trechos reescritos passam por uma conferência só dessa lente antes da validação, feita por quem aplicou (comparando com a fonte) ou por um agente quando forem muitos trechos. Por quê: sem ela, a reescrita por direito autoral fica sem nenhuma conferência quando a revisão foi no rápido.

## Uma segunda revisão de outra família de modelo

**Decisão:** quando o Codex CLI está instalado, ele revisa todo código ao lado do `/code-review`, sem substituí-lo, num perfil só de leitura e sem conectores, numa pasta isolada que leva só os arquivos revisados; os achados dele entram na conferência da `review`, ditos à parte. Ele pode ler também os textos de peça e de pesquisa, como segunda leitura independente, seguida da mesma conferência única (não como conversa entre os agentes). Sem o Codex, a revisão segue sem ele e diz isso.

**Motivo:** o modelo de outra família acha o que os do mesmo modelo não acham, e não favorece o próprio trabalho (`knowledge/agent-engineering/vieses-do-juiz-llm-e-defesas.md`); dois modelos diferentes juntos acertam mais que a média dos dois, pelas perguntas que só um acerta (`knowledge/agent-engineering/conselho-revisao-e-bajulacao.md`). Não substitui o `/code-review`, que também acha o que ele não acha. A conversa entre revisores fica de fora porque a base mostra que o debate tende a convergir para a opinião mais confiante, não para a certa.
