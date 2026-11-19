# Lições da skill `review`

O que o uso e a edição desta skill ensinaram. Antes de usar a skill, leia as abertas e as apontadas; ao terminar, registre a lição nova aqui, na mesma entrega.

**Formato** (o de [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md)): cada lição diz o que devia acontecer, o que aconteceu, por quê e o que mudar, mais quando vale, a evidência, a gravidade (crítica, maior, menor) e as ocorrências. As seções são **Abertas** (à espera de decisão), **Apontadas** (a lição mora em outro arquivo, como [`../licoes-gerais.md`](../licoes-gerais.md)), **A sair**, **Viraram regra** e **Saíram**; seção vazia pode faltar. A lição nova da equipe entra em "Abertas", como aberta; quando vira regra, passa a uma linha no imperativo em "Viraram regra", com o porquê em termos gerais e o lugar da skill onde entrou. Quando há issue de reavaliação ([`references/projeto.md`](./references/projeto.md)), as observações de cada uso ficam no registro dela, e o que dali virar lição de como operar a skill entra aqui.

## Abertas

Nenhuma.

## Apontadas

- **Ao reaproveitar um modelo de pedido a agentes, troque as referências da tarefa antes de disparar.** Em [`../licoes-gerais.md`](../licoes-gerais.md).

## Viraram regra

**A entrega**
- **Separe os críticos e maiores, para decidir um a um, dos menores, numa tabela para aprovar em bloco.** Por quê: misturados, dezenas de menores ocupam a mesma atenção que o achado que muda a decisão. (Etapa 3, `references/entrega.md`)
- **Ponha os pré-existentes numa lista à parte, cada um com destino (corrigir junto, lição, issue ou mantido); "lint" e "alerta" não são destino.** Por quê: o problema que o trabalho não criou não conta contra ele, mas sem dono ele fica. (Etapa 3, `references/registro.md`)
- **Com delegação, aplique antes da validação só as correções de fato, de régua e de código; o que muda conclusão, regra ou destino, ou reescreve texto que a pessoa aceitou, vai ao "para decidir".** Por quê: sem esse limite, as correções mudaram regras do próprio trabalho sem que a pessoa visse. (Etapa 3)
- **Antes de postar na issue o resumo ou o registro, confira que não vai nele trecho de terceiro.** Por quê: a entrega chega ao GitHub. (`references/entrega.md`)

**Achar e conferir**
- **Dê a cada achado uma sugestão de correção, e faça a conferência julgá-la.** Por quê: a correção cria problema novo com frequência, e a sugestão errada leva à correção errada. (Etapas 1 e 2)
- **Inclua na régua o critério registrado antes de rodar (o registro do experimento, o comentário de critério).** Por quê: é a régua que pega os problemas de uma proposta de método. (catálogo, lente da régua)
- **Use a lente "comparar com o anterior" e, no trabalho derivado de obra protegida, a lente "conteúdo próprio".** Por quê: nenhuma outra lente nota o que falta em relação ao que já se fazia, nem a distância da obra de origem. (catálogo)
- **Grave na pasta temporária, como arquivo, a fonte que só uma ferramenta do assistente alcança (issue pelo `gh`, banco de artifact, MCP), antes de disparar o agente.** Por quê: o agente filho não tem as ferramentas nem a conversa. (`references/prompts.md`)
- **Diga no pedido quando o trabalho pode mudar durante a revisão, e faça o conferente julgar pela versão atual.** Por quê: o revisor já leu uma versão que mudou no meio. (`references/prompts.md`)
- **Diga ao agente que pode ler as pastas `originals/` e que o limite é o git: nada de terceiro sai para o repositório nem para a entrega.** Por quê: a proibição de abrir a pasta não se cumpria (a busca recursiva passava por ela), e o que importa é o que sai. (`references/achar.md`)
- **Dentro de um subagente com a ferramenta `Agent`, dispare o achador e o conferente como filhos.** Por quê: o subagente dispara outros, e a passada única tirava a conferência independente. (`references/agente.md`)
- **Dispense a conferência por outro agente só no achado de código com execução e cenário; o de texto da mesma revisão continua conferido.** Por quê: a dispensa do código levava junto o texto, que a conferência corrige com frequência. (Etapa 2)

**Níveis e re-revisão**
- **No rápido, liste os menores de certeza alta num bloco à parte, ditos como não conferidos.** Por quê: o rápido trazia menores úteis, e a regra passou a descrever a prática. (Níveis)
- **Use o padrão em pesquisa, decisão e peça; o rápido em arrumação e edição pequena de skill, esta com três lentes (régua, fidelidade, efeito nas outras skills).** Por quê: "padrão sempre" gastava igual em arrumação e em decisão, e sem a terceira lente a edição nunca passaria pela lente que a regra pede. (`references/niveis.md`)
- **Na ingestão em lote por amostra, passe a régua em todas as fichas e declare a amostra antes de rodar.** Por quê: a amostra sem régua deixou passar paráfrases próximas demais da fonte. (`references/niveis.md`)
- **Re-revise quando a correção reescreve trechos, uma rodada só, dos trechos mudados; a segunda, por pedido da pessoa.** Por quê: a correção cria problema novo, e as rodadas automáticas em série custavam mais da metade da revisão. (`references/re-revisao.md`)
- **Na re-revisão, confira só os críticos e maiores, por outro agente que não aplicou a correção nem achou; liste os menores sem conferência.** Por quê: os menores não voltavam, e a conferência por quem aplicou não é independente. (`references/re-revisao.md`)

**Código**
- **Mande o código ao `/code-review`, o texto a esta skill, e os achados dele pela conferência da Etapa 2.** Por quê: cada um pega o que o outro não olha, e parte dos achados do médio cai na conferência. (`references/codigo.md`)
- **No script novo fora do git, `git add -N` e o caminho no alvo antes do `/code-review`, e `git reset` logo depois; use o médio quando o código é a entrega.** Por quê: sem a marca, o arquivo fica fora do diff e o baixo responde `(none)`. (`references/codigo.md`)
- **Leia o `(none)` do baixo como "nada no trecho do diff"; se o médio falhar, use o agente substituto e diga isso.** Por quê: rodar o baixo de novo repete o resultado. (`references/codigo.md`)

**O registro**
- **Conte o número do registro pelo `scripts/registro.py`, na hora, e não por comando de shell.** Por quê: o gatilho que depende de lembrar falha, e o jq com escape e aspas quebra entre Bash e PowerShell. (`references/registro.md`)
- **Registre as lentes, quantos achados mudaram a decisão (com a lente), os aplicados (por quem e quando) e o que veio depois; não só quantos foram aplicados.** Por quê: "aplicados" é quase sempre "todos" e não diz que lente rende. (`references/registro.md`)
- **Dê prazo ao "a ver" (o fim da issue do trabalho) e deixe o resultado da re-revisão na observação, não no "o que veio depois".** Por quê: sem prazo, o "a ver" nunca ganhava complemento, e o campo misturado tirava o registro do acompanhamento. (`references/registro.md`, `scripts/registro.py`)
