---
name: piece-creation
description: >-
  Leva uma peça de conteúdo da ideia crua, da pauta pronta ou do quadro da série até a peça pronta (a prévia, o portão e a exportação): o carrossel da série ou avulso, a sequência de Stories, o Story avulso. USE quando a pessoa pedir para fazer, montar ou produzir um post, a peça da semana, o carrossel de alguém da série, os Stories de um dia ou o compartilhamento de um post, ou quando perguntar se uma ideia rende e pedir para fazer, mesmo que não diga "skill". NÃO use para só registrar uma ideia (`idea-capture`), só apurar ou achar o ângulo (`story-angle`), só escrever ou refazer o roteiro (`piece-script`), revisar um texto (`review`), gerar só uma imagem (`image-gen`) nem para exportar o que já está pronto (`slides-export`).
---

# Skill: piece-creation

A orquestradora da criação de peças: **guarda a ordem, o estado e as paradas, e chama as outras skills pelo nome.** Não tem ofício próprio: o roteiro é da `piece-script`, a apuração da `research` e da `story-angle`, a revisão da `review`, a forma das telas da `visual-form` (que chama a `image-gen` e a `object-anatomy`), a exportação da `slides-export`, o juízo do portão do arquivo do portão (`references/projeto.md`). O que ela faz por si é pouco e é o que costuma faltar: ler o que já existe antes de escrever, escrever o briefing, escolher o formato com o porquê, e não deixar nenhuma etapa ser pulada em silêncio.

**Por que existe:** as regras de olhar as peças anteriores, de parar no arco antes do texto e de declarar a revisão, espalhadas e lembradas de cabeça, falham: a peça sai sem olhar as vizinhas, ou vai do pedido à prévia sem a parada do arco e sem dizer que a pulou. Aqui cada uma vira passo com registro.

**Lições:** antes de começar, leia as abertas e as apontadas em [`licoes.md`](./licoes.md) desta pasta. **O que é deste projeto** (as pastas, as réguas, o portão, o público, as lições das peças) está em [`references/projeto.md`](./references/projeto.md).

**As credenciais:** esta skill não usa chave. As skills que ela chama e que usam (a `research`, a `image-gen` e a `slides-export` com `--upload`) conferem cada uma a própria credencial no passo 0 delas; se uma delas parar por falta de chave, a peça para naquele passo, o estado registra "parado, porque falta a chave <VARIÁVEL>", e a mensagem da skill vai à pessoa como veio.

## A entrada: de onde a peça parte

| Ponto de partida | Como reconhecer | Por onde começa |
|---|---|---|
| **Ideia crua** | um arquivo da pasta de ideias sem `estagio: pauta`, ou uma ideia dita na conversa | [`references/ideia-crua.md`](./references/ideia-crua.md): o "rende?" com o porquê, os formatos candidatos, e a `story-angle` |
| **Pauta pronta** | o arquivo da ideia com `estagio: pauta`, ou o checkpoint da semana com o ângulo escolhido | o briefing (passo 2), direto |
| **Quadro de série** | o pedido nomeia a série, o tema da semana ou o post A/B | o rascunho da semana da série (o briefing é da semana) e o arquivo do formato |

Depois, leia o arquivo do formato e só ele: [`references/carrossel.md`](./references/carrossel.md) (a série e o avulso) ou [`references/stories.md`](./references/stories.md) (narrativos, de resposta e o avulso de uma tela). A forma é da skill `visual-form` (passo 5).

**Formato fora daqui:** Reel e cena em vídeo vão só até a folha da `piece-script` (`references/cena.md` dela); a execução do vídeo ainda não tem skill. Post para outra rede (LinkedIn, Facebook) ainda não tem processo: diga isso e proponha o formato mais próximo, sem inventar régua. **Retomada:** se a pasta da peça (ou, na ideia crua, o arquivo da ideia) já tem a seção "Estado da criação" (abaixo), comece de onde ela parou.

## O estado da peça

A primeira seção do `refinamentos.md` da pasta da peça é desta skill e só dela: **"## Estado da criação"**, uma tabela que nasce no passo 1 e se atualiza ao fim de cada passo. Na ideia crua, enquanto o formato (e por isso a pasta) não está escolhido, a seção nasce no arquivo da ideia, ao lado do "Rende?", e passa ao `refinamentos.md` da pasta quando a primeira mesa escolhe o formato.

| Passo | Quem faz | Estado | Arquivo | Parada com a pessoa |
|---|---|---|---|---|
| (número e nome) | (esta skill ou a skill chamada) | feito · parado · a fazer · pulado, porque… · não se aplica, porque… | (o que saiu) | (o que foi à pessoa, a escolha dela e se coincidiu com a sugestão) |

- **Nenhum passo some.** O passo que não roda sai escrito "pulado, porque…" ou "não se aplica, porque…", com o motivo, como o campo fora do nível da `piece-script`; o que ainda não chegou sai "a fazer", que não se confunde com o que parou. É o que impede a etapa pulada em silêncio.
- **A parada registra a escolha e a concordância.** Coincidiu com a sugestão do assistente: sim ou não. A taxa por tipo de pergunta é o sinal para, com o tempo, propor à pessoa delegar aquele tipo; a skill não corta parada por conta própria.
- **Na série,** a pasta do post nasce no passo 1 (a do carrossel da semana, pelo modelo de pastas da série) para a tabela ter onde morar; o briefing da semana continua no rascunho da semana.

## As paradas com a pessoa

As paradas são **as que o processo de cada formato já tem**; esta skill não cria mesa nova. Onde o processo do formato fecha cada camada numa mesa, a peça sobe em camadas; onde duas camadas vizinhas têm decisões pequenas, elas dividem uma mesa.

| Formato | As paradas, na ordem | O que não é parada |
|---|---|---|
| Carrossel da série | os ângulos (da semana, na `story-angle`); o arco, os conceitos e as imagens, numa mesa só (na `piece-script`); a forma; a prévia; a volta do portão, se houver | o ok do texto vem na entrega da `review`, sem mesa própria |
| Carrossel avulso | os ângulos; o arco, os conceitos e as imagens; a forma; a prévia; a volta do portão | o mesmo |
| Ideia crua (antes do formato) | a primeira mesa junta o briefing (os formatos candidatos e, sem série, a identidade visual) com a mesa de ângulos da `story-angle` | o "rende?" não para a peça quando o pedido já disse "se render, faz": só para quando a resposta é não |
| Stories narrativos | a semana; a mesa dos arcos (na `piece-script`); a leitura da prévia | a escaleta só vai antes se a pessoa pedir |
| Stories de resposta | a semana; a escolha das respostas (na `piece-script`); a leitura da prévia | sem mesa de arcos |
| Story avulso | a semana; a leitura da prévia | sem mesa nenhuma antes da prévia |

**Como cada parada se faz:** o que é regra (o design system, a rubrica, as lições) se confere antes e sai da mesa; só vai à pessoa o que é gosto e direção de arte ([`decisions/mesas-de-design.md`](../../../decisions/mesas-de-design.md)). A mesa grava cada escolha assim que ela é feita (num artifact do claude.ai com banco de dados, uma página publicada na sua conta que guarda cada escolha e o assistente lê depois, ou no arquivo da peça; ver "Mesa" no [`glossario.md`](../../../glossario.md)), com comentário por item e as opções "nenhuma destas / outra" e "pela régua / não sei", e a sugestão do assistente aparece depois da escolha, para não ancorar; o link ou o lugar da mesa vai no arquivo da peça. As peças da mesa chegam com o lastro já conferido. **Quando quem chama já traz a escolha da pessoa numa parada, siga com ela** e registre na tabela do estado, sem perguntar de novo.

## Os passos, nesta ordem

1. **Abrir o estado.** A pasta da peça e a seção "Estado da criação" (acima), com o ponto de partida, o formato e o tipo; na ideia crua, a seção no arquivo da ideia. Se o formato não veio no pedido nem na pauta, ele é item do briefing (passo 2), não suposição.
2. **O briefing, antes de escrever qualquer coisa.** Primeiro, ler o que já existe (no Story avulso, a lista mais curta de [`references/stories.md`](./references/stories.md) substitui esta): o calendário, quando o projeto tiver, e as peças anteriores do mesmo tipo e da mesma semana (o texto, a prévia da última passada, o `refinamentos.md`); as lições da etapa (as do tipo e as de "todas"); o público; o README da série ou dos Stories (os caminhos em `references/projeto.md`). Depois, escrever, no lugar que o arquivo do formato diz:
   - a função da peça, o público e o objetivo na plataforma (salvar, enviar, comentar), mais uma linha de **objetivo de aprendizagem**: "depois desta peça, a pessoa consegue…";
   - o pedido final, um só;
   - o **efeito**: que sensação a peça passa e que elemento a carrega, herdado do design system quando é de série, decidido aqui quando não é (então vai à mesa, como identidade visual);
   - o que as anteriores já fizeram, com o caminho de cada uma aberta, e o **incremento da semana**, quando a série ou a agenda dos Stories o pedem (um, com a tela e o elemento onde se vê);
   - as lições aplicadas, ou "nenhuma lição registrada";
   - quando o formato está aberto, os **formatos candidatos, cada um com o porquê**: o mesmo conteúdo pode servir a mais de um (carrossel, Story, tela única, vídeo curto), e a escolha é caso a caso, nunca fixa por tipo de conteúdo.

   O Story avulso (N0) termina aqui: o briefing é o roteiro dele ([`references/stories.md`](./references/stories.md)), e a `piece-script` não roda.
3. **A apuração e o ângulo, se faltam.** Sem ângulo, a `story-angle` (com a mesa de ângulos dela); sem lastro de um fato, a `research` (que confere a própria chave antes de buscar). Nunca copiar número da síntese para a peça: apontar a fonte.
4. **O roteiro:** a `piece-script`, com o formato, o tipo, a pauta e os não escolhidos, o ledger ou as fichas, a pasta da peça e, na série, a escaleta da irmã da semana. As paradas antes do texto e a revisão do texto são dela; esta skill confere que aconteceram e registra no estado. **A revisão roda pela skill `review`, que despacha agentes que não escreveram o texto;** a revisão feita no próprio contexto de quem escreveu não conta como revisão, e sai no estado como "pulado, porque…".
5. **A forma**, com o texto travado: a skill `visual-form`, chamada pela ferramenta Skill com a pasta da peça e o formato (o HTML das telas, as imagens, o objeto que se move pela `object-anatomy`, as conferências em 0 ERRO, as alternativas para a parada da forma e, no carrossel da série, a I2 com a trava validada por script). A imagem nova sai da `image-gen`, chamada pela forma, que confere a própria chave antes de gerar. A forma não troca palavra do texto aprovado; o pedido que muda o texto volta ao passo 4. Esta skill registra no estado a parada da forma e as telas que a I2 devolveu.
6. **A prévia**, a peça inteira, ao lado da prévia da peça anterior do mesmo tipo, no mesmo acabamento, com a pergunta "superou a anterior?". A **marca de antes** da pessoa (a opção preferida e se a peça está pronta ou precisa de refinamento) se grava aqui, antes de ela ver o veredito do juiz.
7. **O portão:** no carrossel, o arquivo do portão, com o juiz em subagente e as duas rubricas; nos Stories, a conferência final sem juiz, pela rubrica de Stories. **O Jev é opcional:** com a `TYPESAFE_API_KEY` configurada, os testes marcados [jev] das rubricas rodam pelo cliente em `scripts/jev/`; sem ela, o juiz responde esses testes, e o estado diz "Jev não configurado". Crítica do juiz que é de **concepção** (o arco, a escolha da imagem) volta ao passo 4; a de **execução** se corrige na forma. Alarme de fato vira "confira contra esta fonte", não pergunta à pessoa. Depois do portão, a **marca final** da pessoa se grava, e as duas marcas vão ao estado; uma vez por peça ela vê a versão de antes da correção do juiz. Nos Stories, sem juiz, a marca final sai "não se aplica, porque não há juiz".
8. **Fechar, só com a peça pronta:** a `slides-export` com `--upload`, que confere a própria chave e o bucket antes de subir. **A peça termina aqui nesta versão:** a publicação pela API vem na segunda versão do ambiente; até lá, quem publica sobe as imagens pelo app, e o estado registra "publicação: fora desta versão".
9. **O registro:** o `refinamentos.md` (as passadas, as voltas, a linha da trava, a parada de cada camada), as lições novas nas lições das peças e no `licoes.md` da skill que errou, e o calendário atualizado, quando o projeto tiver.

**O que esta skill escreve, e só isso:** a seção "Estado da criação" (no `refinamentos.md`, ou no arquivo da ideia até a primeira mesa); o briefing (no rascunho da semana, no arquivo da ideia, no `refinamentos.md` do carrossel avulso, ou no bloco "Briefing" do `roteiro.md` dos Stories, logo depois do frontmatter, como o arquivo do formato diz); e, no avulso N0, o `roteiro.md`, menos as seções da forma, do publicado e do resultado. O resto tem dono: a escaleta, o texto e o texto da `legenda.md` são da `piece-script`; o HTML e as imagens, da `visual-form`; os embeds da `legenda.md`, da `slides-export`.

## Revisão (skill `review`)

- **Ponto de pausa:** a do texto é da `piece-script` (passo 4). Esta skill declara a sua no fim do briefing, quando a entrada é ideia crua ou o formato está aberto: antes da primeira mesa, sobre o briefing e os formatos candidatos, **num despacho só da `review`** com a revisão da mesa da `story-angle`, somando os itens das duas listas.
- **Nível:** padrão. **Lentes:** régua (sempre) + além da evidência, de fora.
- **Conferir contra:** o README da série ou dos Stories, o público, as peças anteriores do mesmo tipo e as lições da etapa.
- **Itens que de fato se esquecem aqui:** as anteriores do mesmo tipo e da semana abertas e citadas; o objetivo de aprendizagem escrito; o porquê de cada formato candidato; o efeito decidido ou herdado; nenhum fato no briefing sem fonte.

## Nunca

- Escrever o texto ou montar a tela antes do briefing, ou o briefing sem ter aberto as peças anteriores do mesmo tipo e da semana.
- Pular uma parada do formato sem escrever no estado que pulou e por quê, ou criar uma parada que o processo do formato não tem.
- Fazer o ofício de outra skill no lugar dela (o roteiro sem a `piece-script`, a revisão no próprio contexto), salvo o avulso N0, que é desta.
- Exportar com `--upload` sem a peça pronta.

**Ao terminar:** se houve falha, contorno ou acerto que vale lembrar, registre em [`licoes.md`](./licoes.md) desta pasta, na mesma entrega (formato e estados em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md)); a lição da peça vai às lições das peças (`references/projeto.md`).
