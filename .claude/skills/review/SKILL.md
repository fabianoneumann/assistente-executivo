---
name: review
description: >-
  Revisão independente de um trabalho do assistente antes de chegar à pessoa: agentes que não o fizeram acham problemas por lentes, outro confere cada achado na fonte, na régua ou no arquivo, e sai a lista dos confirmados por gravidade, sem alterar nada. USE na etapa de revisão que uma skill declara (a `research`, a `story-angle`), na re-revisão do trabalho corrigido e sempre que a pessoa pedir para revisar, conferir, criticar, "achar problemas", "passar um pente fino", "ver o que eu não estou vendo" ou testar uma decisão, num texto, síntese, pauta, plano, issue, skill ou texto de peça em produção, mesmo sem dizer "revisão". NÃO use no lugar do portão de qualidade das peças: antes dele, revisa o texto e a estrutura da peça, sem julgar a forma. Código vai ao `/code-review`; no trabalho misto (skill com script), esta revisa o texto e confere os achados dele. NÃO use para conferências que o código já faz (publicar, exportar, coletar métricas).
---

# Skill: review

Um segundo olhar que não carrega o contexto de quem fez o trabalho. Quem fez tende a confirmar o que acabou de fazer, e o modelo tende a concordar com quem pergunta (bajulação); um revisor em contexto limpo, guiado por lentes e obrigado a conferir cada achado, pega o que escapou. A revisão **nunca aprova, nunca bloqueia e nunca altera o trabalho**: entrega achados conferidos, e quem decide o que aplicar é a pessoa.

**Lições:** antes de começar, leia as abertas e as apontadas em [`licoes.md`](./licoes.md) desta pasta.

**As regras inteiras, com o porquê, estão nas referências**; este arquivo é o roteiro, e cada passo diz qual ler antes de executá-lo. **O que é deste projeto** (as réguas, o portão das peças, a base em que o método se apoia, a issue de reavaliação, os revisores opcionais e os comandos) está em [`references/projeto.md`](./references/projeto.md).

O desenho vem de três lugares (as fichas e as sínteses, em `references/projeto.md`):
- o **Code Review do Claude Code** (achar por lentes, conferir cada achado, gravidade, nunca aprovar). **Confira a documentação dele de tempos em tempos** (https://code.claude.com/docs/en/code-review e o plugin `code-review` em `anthropics/claude-plugins-official`): quando ele mudar de forma que melhore o mecanismo, traga a mudança para cá;
- os métodos de revisão (heurística, gravidade, pre-mortem, verificação fatorada);
- o teste do conselho e a bajulação.

## Entrada

Quem chama passa:
1. **O trabalho:** o caminho do arquivo ou o texto, e as fontes ou arquivos contra os quais ele foi feito; e **o pedido de origem**, quando há um escrito (a issue, com o "pronto quando", o corpo e os comentários, já na pasta temporária como arquivo, lida pelo `gh`; ou o pedido da pessoa), quando a lente "o pedido" está entre as escolhidas: ela é escolhida como as outras, pela seção da skill que chama ou, no pedido direto, pelo tipo de trabalho, e não roda no rápido. Sem pedido escrito, a lente fica de fora, e a linha do pedido na entrega diz isso.
2. **A etapa e a seção de revisão da skill que chama** (ver "Como uma skill chama a revisão"), com as lentes daquela etapa e contra o que conferir. Pedido direto, sem skill por trás: escolha as lentes pelo tipo de trabalho, no catálogo.
3. **O nível** (abaixo). Sem indicação, pela tabela; na dúvida, padrão.
4. **A revisão anterior, se o trabalho já foi revisado e volta corrigido:** o arquivo de achados dela, o que a pessoa aprovou e o que recusou, e o que mudou desde então (o `git diff` ou a lista de arquivos). Aí a revisão é uma re-revisão (abaixo).

## Níveis

| Nível | Quando | Como |
|---|---|---|
| Rápido | etapa intermediária, trabalho pequeno, arrumação, edição pequena que não muda conclusão nem regra (a de skill, como em [`references/niveis.md`](./references/niveis.md)), ou a pessoa pede "uma olhada rápida" | um agente acha só com a lente da régua e a de fidelidade, e entrega o de certeza alta: crítico e maior, já conferidos por ele no trecho da fonte, e os menores de certeza alta num bloco à parte, ditos como não conferidos |
| Padrão | pesquisa, decisão e peça: sempre que uma etapa entrega uma delas para a pessoa julgar; e a edição de skill, salvo a pequena | um agente acha com todas as lentes da etapa; outro agente confere cada achado; gravidade e entrega |
| Profundo | **só por pedido** da pessoa; decisão grande, difícil de desfazer | um agente por lente (ou de 3 a 5 revisores independentes), cada um sozinho; conferência; gravidade dada por dois agentes sem ver as notas um do outro |

**Leia [`references/niveis.md`](./references/niveis.md) antes de usar** o profundo, o modo **por amostra** (ingestão em lote: a régua em todas as fichas, a fidelidade e o conteúdo próprio na amostra, escrita antes de rodar) ou a **edição de skill** (padrão com a lente "efeito nas outras skills"; a pequena vai no rápido com três lentes).

**Re-revisão:** o trabalho que volta corrigido não se revisa inteiro de novo. O agente que acha recebe o que mudou e os achados anteriores e responde a três perguntas: o aprovado foi resolvido sem criar problema? O que mudou traz problema novo? O que as correções acrescentaram sem precisar? É obrigatória quando a correção reescreve trechos (depois do rápido, só quando reescreve regra ou decisão), tem uma rodada só (a segunda, por pedido da pessoa) e confere só os críticos e maiores. **Leia [`references/re-revisao.md`](./references/re-revisao.md) antes de cada uma**: o "churn" em par, a re-revisão conjunta, as exceções depois do rápido e quem confere.

**Código** (script, teste, programa) vai ao `/code-review` e, quando instalado, ao Codex, ao lado dele; texto, regra, rubrica e instrução de skill ficam com esta skill, e o trabalho misto passa pelos dois, com os achados do código na Etapa 2. **Leia [`references/codigo.md`](./references/codigo.md) antes de chamar:** o nível (baixo no ajuste, médio no código que é a entrega), o `git add -N` no script novo, o `(none)` do baixo, o substituto e o Codex, no código e no texto.

## Etapa 1: achar

Dispare um agente (`general-purpose`) que **não viu a conversa**: ele recebe só o trabalho, as fontes, a régua e as lentes, com o modelo de pedido de [`references/prompts.md`](./references/prompts.md). No padrão e no profundo, ele grava os achados na pasta temporária e devolve só a contagem por gravidade sugerida e o caminho do arquivo, que o conferente lê; no rápido, e quando não sobra nada para conferir, devolve o texto inteiro. **Agente que falhou não revisou:** o de achar ou o de conferir que não responde, erra ou devolve o que não é achado nem "nada encontrado" roda de novo uma vez; se falhar outra vez, a etapa dele fica como **não rodou** na entrega e no registro, nunca como "nada achado", e os achados que dependiam dela vão como não conferidos. **Leia [`references/achar.md`](./references/achar.md) antes de disparar:** o porquê do isolamento (o que chega ao filho e o que não chega), do que volta, e a regra da pasta fora do git com dado de terceiro, que vale para o pedido de cada agente.

- As lentes vêm da seção de revisão da skill que chama, mais a **lente fixa da régua** (conformidade com as regras escritas que valem para o trabalho: rubricas, design system, `decisions/`, os READMEs da área, e o critério registrado antes de rodar), que sempre roda. Ela existe porque lentes que só olham a decisão perdem a regra escrita: um piso de tamanho de letra passou por cinco lentes sem que nenhuma lesse a régua.
- Catálogo, com a pergunta de cada lente, quando usar e de onde vem: [`references/lentes.md`](./references/lentes.md).
- **Nenhuma lente é obrigada a discordar.** Se pelo seu ângulo o trabalho se sustenta, ela diz isso. Discordância fabricada quebra o que estava certo.
- Cada achado sai com: a lente; o trecho do trabalho (linha); o problema; a evidência (arquivo e linha da fonte ou da regra); o **tipo** (afirmação errada, desvio da régua, lacuna, premissa), que decide a pergunta da conferência; e uma **sugestão de correção** em uma frase, que a conferência também julga; no de gravidade sugerida crítica ou maior, também o **se pularmos**: o que acontece, em uma frase, se a pessoa não aplicar (no menor, a resposta já é "a conclusão não muda", pela definição). A gravidade aqui é só sugestão. Se o problema já existia antes deste trabalho (estava no arquivo ou no projeto antes dele), o achado sai marcado **pré-existente**.
- Ferir uma regra não obriga a mudar: o contexto pode justificar. O achado diz qual regra e por que importa ali.

## Etapa 2: conferir

Dispare outro agente, que **não fez o trabalho nem a busca**, para conferir um por um os achados de gravidade sugerida crítica, maior ou menor (os de estilo vão direto para a entrega, marcados como não conferidos) e, na re-revisão, só os críticos e maiores, novos, e os vereditos de resolvido dos críticos e maiores anteriores. Uma pergunta por achado, conforme o tipo, mais a da sugestão de correção (o porquê de cada pergunta, em [`references/conferencia.md`](./references/conferencia.md)):

| Tipo | Pergunta da conferência |
|---|---|
| Afirmação errada (número, atribuição, fato) | aberta: "o que a fonte diz sobre isto, no trecho?", e só depois comparar com o trabalho |
| Desvio da régua | sim ou não, com o texto exato da regra citado: "o trabalho fere esta regra?" |
| Lacuna (o que falta, o que não foi ressalvado) | "a lacuna existe, e incluí-la muda a conclusão ou a decisão?"; na sobra da lente "o pedido" (o feito sem ser pedido), "o pedido, citado na linha, pediu isto?" |
| Premissa | "a pergunta ou o problema de partida ainda vale, conferido no arquivo ou no estado atual?" |
| Pré-existente (marca, além do tipo) | "o problema já estava antes deste trabalho?", conferido no `git log` ou na versão anterior do arquivo |
| Resolvido (na re-revisão) | "a correção aprovada está no trabalho e resolve o achado, sem criar outro problema?", conferido no trecho mudado |

**A sugestão de correção, em todo achado conferido:** "a sugestão resolve o achado sem criar outro problema, e o que ela acrescenta serve ao leitor real do trabalho? Se não, qual seria a certa, em uma frase?".

Veredito por achado: **confirma**, **confirma em parte** (o que muda), **não confirma** ou **a prova está com a pessoa**, mais o juízo da sugestão. **Na dúvida, não confirma.** **Leia [`references/conferencia.md`](./references/conferencia.md) antes de conferir:** o quarto veredito (quando a prova está fora do alcance do conferente, e quem chamou pode resolvê-lo citando a prova escrita), a pergunta da sugestão por inteiro e as duas dispensas da conferência por outro agente (números que um script calculou; achado de código com execução e cenário).

## Etapa 3: gravidade e entrega

Junte os achados confirmados, tire os repetidos e dê a gravidade **depois** da conferência, sobre a lista inteira; quem sobe um achado a crítico ou maior escreve o se pularmos dele:

- **Crítica:** afirma algo errado (número, fato, atribuição) ou fere uma regra que barra a entrega.
- **Maior:** induz a uma decisão errada ou omite o que muda a conclusão.
- **Menor:** imprecisão que não muda a conclusão.
- **Estilo:** clareza, termo sem definição, ordem.
- **Pré-existente** (à parte, sem gravidade do trabalho): o problema que o trabalho não criou. Não conta nos números da revisão; vai numa lista própria, com o destino sugerido (corrigir junto, virar lição ou issue). Vem do Code Review, que separa o bug que já estava no código do que a mudança trouxe.

Entregue em dois blocos, no formato de [`references/prompts.md`](./references/prompts.md) ("Entrega"): **para decidir** (os críticos e os maiores, um a um, com o se pularmos e a sugestão; os de prova com a pessoa; os pares do "churn" com crítico ou maior) e **para aprovar em bloco** (os menores numa tabela curta, o estilo numa linha, os pré-existentes na lista deles). No fim, o que a conferência derrubou e o que não foi conferido. **A revisão não aplica nada.** Com delegação, quem fez o trabalho aplica antes da validação só as correções de fato, de régua e de código, e o que muda conclusão, regra ou destino, ou reescreve texto que a pessoa aceitou ou decidiu, vai ao "para decidir" mesmo assim. **Leia [`references/entrega.md`](./references/entrega.md) antes de entregar:** a linha da lente "o pedido", a delegação por inteiro, o resumo que sai do projeto, onde guardar e a conferência de trecho de terceiro antes de postar.

## Registro de cada uso e reavaliação

Quando o projeto mantém uma issue de reavaliação da `review` (o número em `references/projeto.md`), toda revisão deixa uma linha nela, depois que a pessoa decidir o que aplicar e **antes do merge do trabalho revisado**, com o número dado por `python -X utf8 .claude/skills/review/scripts/registro.py <issue>`. A partir do 15º registro, ou na data da issue, proponha a reavaliação. Sem issue de reavaliação, não há registro. **Leia [`references/registro.md`](./references/registro.md) antes de escrever a linha:** o formato, o que vai em cada campo, os complementos dos "a ver" e o que fazer quando a reavaliação acontece.

## Como uma skill chama a revisão

A skill que chama declara uma seção curta, no ponto em que a etapa entrega algo para a pessoa julgar. É um checklist do tipo "fazer e depois confirmar": quem fez o trabalho segue a própria skill e, nesse ponto de pausa, a revisão confere poucos itens, os que de fato se esquecem.

```markdown
## Revisão (skill `review`)

- **Ponto de pausa:** <a etapa, antes de entregar o quê à pessoa>
- **Nível:** padrão
- **Lentes:** régua (sempre) + <de 3 a 6 lentes do catálogo, as que mais pegam erro nesta etapa>
- **Conferir contra:** <as fontes, arquivos ou regras desta etapa>
- **Itens que de fato se esquecem aqui:** <de 3 a 7 itens conferíveis, um por linha>
```

## Quando a revisão roda dentro de um agente

Se o subagente tem a ferramenta `Agent`, siga as etapas como na conversa principal, com o achador e o conferente como agentes filhos. Sem ela (ou com erro), faça as etapas em sequência, uma passada para cada, e diga na entrega que a conferência não foi independente. **Leia [`references/agente.md`](./references/agente.md) antes**, para o detalhe e o porquê.

## Nunca

- Aprovar, bloquear ou aplicar correções.
- Deixar o código de um trabalho só com as lentes desta skill: ele passa pelo `/code-review`.
- Passar ao revisor a conversa ou o raciocínio de quem fez o trabalho.
- Obrigar uma lente a discordar.
- Entregar achado de afirmação ou de régua sem a evidência (arquivo e linha).
- Dar como revisado o que o agente que falhou não revisou (Etapa 1).

**Ao terminar:** se houve falha, contorno ou acerto que vale lembrar, registre em [`licoes.md`](./licoes.md) desta pasta, na mesma entrega (formato e estados em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md)).
