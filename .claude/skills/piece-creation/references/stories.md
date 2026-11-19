# Stories: narrativos, de resposta e o avulso de uma tela

O que a criação de peças acrescenta aos passos do `SKILL.md` nos Stories. As regras do formato estão no README dos Stories (a agenda, a janela, a provocação, a mesa dos arcos, a resposta à caixinha, a forma, os desenhos) e na rubrica de Stories (os caminhos em `projeto.md`); valem como estão e não se repetem aqui. A pasta de cada sequência é `marketing/social-media/stories/AAAA-MM-DD-<tema>/`, com `roteiro.md`, `stories.html` e `refinamentos.md` (a seção "Estado da criação" desta skill no topo dele).

## O tipo decide o caminho

| Tipo | Quando | Nível do contrato | Quem escreve o roteiro | As paradas |
|---|---|---|---|---|
| **Narrativo** (N) | quatro telas ou mais, que prepara ou antecipa um post, ou é livre | N2 | a `piece-script` | a semana; a mesa dos arcos; a leitura da prévia |
| **Resposta** (R) | a produção de véspera com as respostas da caixinha e o resultado da enquete | N1 | a `piece-script`, pelo ramo da resposta | a semana; a escolha das respostas; a leitura da prévia |
| **Avulso** (A) | uma tela só: o compartilhamento de um post, um aviso | N0 | **esta skill, no briefing; a `piece-script` não roda** | a semana; a leitura da prévia |

O nível é do tipo, não da peça: o avulso que pede arco sobe a N1, com o motivo escrito no roteiro, e vai à `piece-script`.

## O briefing dos Stories (passo 2)

O briefing vai num bloco **"## Briefing"** do `roteiro.md`, logo depois do frontmatter (que fica na primeira linha, porque as conferências e o calendário, quando houver, o leem dali) e acima da cabeça da `piece-script`; é desta skill: a moldura, o objetivo de aprendizagem, o efeito, o incremento da semana, as **Lições lidas** e as **Peças abertas antes de escrever**. Se o `roteiro.md` ainda não existe, esta skill o cria com o frontmatter que o README dos Stories pede, e a `piece-script` o completa. A `piece-script` lê a moldura dali: o **Objetivo** e as **Regras conferidas** da cabeça dela apontam para o bloco em vez de repeti-lo. Antes de escrever, abra e cite no bloco: a agenda da semana no README (e no calendário, quando houver); a sequência anterior do mesmo tipo (a quinta com a quinta, a resposta com a resposta), com a prévia da última passada dela; as vizinhas da semana e o post do dia; o banco de desenhos (os `assets/` das peças de Stories e da série, o material da marca, o banco de imagens geradas; `projeto.md`). É daí que sai a riqueza visual: **nenhuma tela só com texto entre vizinhas com desenho sem o motivo escrito**.

Para a moldura (objetivo, pedido único, a provocação com a origem e a fonte, os fatos com a peça de origem), o README dos Stories manda; na resposta, a moldura se decide **antes de ler as respostas**.

**Na sequência de consciência e de venda** (rubrica de Stories, seção própria, desde a v0.3, a testar): o briefing cita as sequências de jab dos dias anteriores (a venda chega depois delas, README dos Stories, "O arco e a venda") e diz onde a informação crítica (o prazo, o preço, a data da turma ou da entrega, o caminho de compra) está também fora do Story, num post ou numa legenda com texto alternativo, para quem decide conferir [pessoa].

## O avulso de uma tela (N0), inteiro aqui

O avulso é a peça mais curta da semana e não deve carregar o processo da sequência. Por isso:

1. **Quando o pedido junta o avulso e uma sequência** ("faz os Stories de sexta e o compartilhamento de sábado"), faça o avulso **primeiro**, com só as leituras dele, antes de carregar o contexto da sequência; ou, se a sequência já está carregada, num agente próprio, com só essas leituras. As leituras do avulso: a peça de origem (a `legenda.md` e a capa do post compartilhado), o avulso anterior da mesma função e as lições de Stories.
2. **O roteiro do avulso**, no `roteiro.md` da pasta dele: o frontmatter (`estagio`, `data`, `janela`, `funcao`: antecipação, compartilhamento, resposta ou aviso; e `depende_de`, a peça de origem); o objetivo e o pedido único; o fato com a peça de origem; o que aparece (o cartão do post, o desenho, com o arquivo); e o texto, de uma ideia só, em até 40 palavras, com o comentário que acrescenta (o porquê, uma opinião, uma pergunta) e sem dia relativo.
3. **A régua** é a do Story avulso (a rubrica de Stories, "Story avulso"): os testes [código] dela rodam; a leitura [modelo] é a sua, dita no roteiro.
4. **A forma,** pela `visual-form` no formato do Story avulso: o que o README dos Stories manda para o Story montado no app (a simulação no `stories.html`, para a pessoa validar o texto e saber onde posicionar), com as conferências da forma em 0 ERRO. Nada além disso: sem mesa, sem revisão por agentes, sem passada de enriquecimento.
5. **O estado** com os passos 3 e 4 como "não se aplica, porque o avulso é N0: o roteiro é o briefing".

## Os narrativos e as respostas

- **O passo 4 é da `piece-script`** (`references/stories.md` dela), com a moldura, a peça de origem e, na resposta, o caminho das respostas no `originals/` da sequência de origem (fora do git; o texto e o @ de quem respondeu não saem de lá).
- **A forma** (passo 5) é da `visual-form`, que segue o README dos Stories (a área segura, o texto acima do adesivo, os desenhos de enfeite) e a `slides-export` com `--html stories.html --height 1920`; a comparação com a sequência anterior do mesmo tipo vai à leitura da pessoa só como sinal, sem trava. A parte em código da rubrica de Stories roda antes da prévia, quando o projeto a tiver (`projeto.md`); os testes [jev] dela só rodam com o Jev configurado, e sem ele ficam com a leitura do assistente. Na resposta, nenhum desenho repetido do post do dia nem da sequência de origem, sem exceção por motivo.
- **Na véspera da resposta, uma parada só:** quando as respostas chegam à noite e a sequência sai na manhã seguinte, a escolha das respostas e a prévia das telas vão à pessoa juntas, numa parada; o critério da escolha fica escrito na sequência que preparou a resposta, e a lista dos desenhos não usados da semana desce para a pasta antes da noite da véspera. Sem esse aperto, a escolha das respostas e a prévia seguem em duas paradas.
- **A prévia** (passo 6) vai à pessoa na hora que o README fixa para a produção de véspera, ao lado da prévia da sequência anterior do mesmo tipo; o ok da trava do texto vem nessa leitura, e a `piece-script` grava a linha da trava.
- **No Story em vídeo falando para a câmera,** o estilo e o lugar da legenda queimada são uma parada da forma: vão à pessoa com um quadro de cada opção, antes de queimar (rubrica de Stories, "Story em vídeo"); o tempo de cada bloco e a área segura são regra e não vão à parada.
- **A publicação** é da pessoa, pelo app (os adesivos só se põem lá); a publicação pela API fica para a segunda versão do ambiente.
