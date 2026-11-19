# A conferência: a sugestão, o veredito e as dispensas

Os caminhos `scripts/...` e `references/...` partem da pasta da skill; os links com `./` ou `../`, do próprio arquivo; os demais caminhos, da raiz do projeto.

**A tabela da conferência, com o porquê de cada pergunta** (o `SKILL.md`, Etapa 2, traz as perguntas):

| Tipo | Pergunta da conferência | Por quê |
|---|---|---|
| Afirmação errada (número, atribuição, fato) | aberta: "o que a fonte diz sobre isto, no trecho?", e só depois comparar com o trabalho | perguntado se um fato é verdadeiro, o modelo tende a concordar com o fato do jeito que veio (CoVe) |
| Desvio da régua | sim ou não, com o texto exato da regra citado: "o trabalho fere esta regra?" | regra só conta se der para citar (Code Review); sim ou não sobre critério aumenta a concordância (CheckEval) |
| Lacuna (o que falta, o que não foi ressalvado) | "a lacuna existe, e incluí-la muda a conclusão ou a decisão?"; na sobra da lente "o pedido" (o feito sem ser pedido), "o pedido, citado na linha, pediu isto?" | a pergunta "o trabalho afirma isso?" derruba toda lacuna, porque lacuna é justamente o que não foi afirmado |
| Premissa | "a pergunta ou o problema de partida ainda vale, conferido no arquivo ou no estado atual?" | uma discussão inteira pode correr sobre um problema que, conferido no estado atual, já não existia |
| Pré-existente (marca, além do tipo) | "o problema já estava antes deste trabalho?", conferido no `git log` ou na versão anterior do arquivo | o problema antigo não conta contra o trabalho, mas não pode sumir (Code Review, Pre-existing) |
| Resolvido (na re-revisão) | "a correção aprovada está no trabalho e resolve o achado, sem criar outro problema?", conferido no trecho mudado | o resolvido que não está resolvido volta à pessoa como pronto |

**A sugestão de correção, em todo achado conferido:** "a sugestão resolve o achado sem criar outro problema, e o que ela acrescenta serve ao leitor real do trabalho? Se não, qual seria a certa, em uma frase?". A correção que só explica o que esse leitor já sabe, para satisfazer um revisor sem contexto, incha o arquivo e a carga de sessão: aí a sugestão certa é outra, ou o achado não vale. Adianta parte da pergunta do resolvido, sem substituir a re-revisão: a correção cria problema novo com frequência, e a conferência troca muitas sugestões que levariam a pessoa a aplicar a correção errada.

**O veredito.** Por achado: **confirma**, **confirma em parte** (o que muda), **não confirma** ou **a prova está com a pessoa**, mais o juízo da sugestão. **Na dúvida, não confirma.**

**O quarto veredito, "a prova está com a pessoa":** quando o conferente nomeia a prova que decidiria o achado e ela está fora do que ele pode abrir (uma decisão dita só na conversa, um comentário de issue que não veio no pedido, um artifact), o achado não cai. O crítico e o maior sobem ao "para decidir" com a prova que falta; o menor vai à tabela "para aprovar em bloco", com a marca e a prova que falta. Quem chamou pode resolvê-lo antes da entrega só citando a prova escrita (arquivo e linha, o comentário, a decisão registrada), e cada um que ele resolver aparece na entrega, com a prova citada e o resultado: caiu, ao lado dos derrubados, ou se confirmou e foi ao bloco da gravidade dele; sem prova escrita, vai à pessoa. Como quem chama costuma ser quem fez o trabalho, a prova citada na entrega é o que deixa a pessoa conferir. A dúvida pela evidência fraca, com a fonte aberta, continua derrubando.

**O papel da conferência** é corrigir gravidades, detalhes errados dentro de achados verdadeiros e sugestões que levariam à correção errada, e derrubar o que não se sustenta. Com o uso, derrubar pesa cada vez menos (os achadores aprendem a régua), e o valor fica na troca de sugestões e na correção de gravidade.

**Números que um script calculou** (o resultado de um teste medido por script) podem ser conferidos por quem fez o trabalho, recalculando cada um por script a partir dos arquivos de dados, em vez de por outro agente; o texto em volta deles continua com a conferência de outro agente. O registro diz "conferência dos números por script, não independente". Por quê: custa metade, e o recálculo por script faz o papel da conferência nos números.

**Achado de código com execução e cenário concreto** (o comando rodado, a entrada e a saída que mostra a falha) dispensa a conferência por outro agente, porque a execução faz o papel dela (o ultrareview do Code Review reproduz cada achado); o achado de texto da mesma revisão continua com a conferência, e o registro diz "código conferido pela execução". Por quê: a dispensa do código não pode levar junto o texto, que a conferência corrige com frequência.
