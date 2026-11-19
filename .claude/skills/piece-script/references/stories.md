# Stories: os narrativos (N2) e o ramo da resposta (N1)

A unidade é o Story. O roteiro mora no `roteiro.md` da pasta da sequência (a pasta dos Stories, em `references/projeto.md`, com uma subpasta `AAAA-MM-DD-<tema>/` por sequência): esta skill escreve nele o frontmatter que o README dos Stories pede (e `destaque: true` quando a sequência pode ir para um Destaque, que faz o `conferir_telas.py` pedir a data em toda tela que diz quando; `voz: true`, opcional, no Story em vídeo com voz, que faz o `video_do_story.py` pedir a legenda revisada; e, desde a rubrica de Stories v0.3, a testar: `profunda: true` na sequência profunda, com o Destaque; `pedido_forte: compartilhar` quando um Story pede que a pessoa compartilhe com amigos; na sequência de consciência e de venda, `virada` com o número do Story da virada, ou `direta` com o motivo, no dia de colheita), a cabeça e a seção "Os Stories" (a escaleta, com os campos do contrato e, no fim, a tabela de plantas e pagamentos), e não toca nas seções da forma, do publicado e do resultado, nem no bloco "Briefing" logo depois do frontmatter, que é da `piece-creation` quando ela chama: a moldura vem dali, e o **Objetivo** e as **Regras conferidas** da cabeça apontam para o bloco em vez de repeti-lo. A linha da trava vai ao `refinamentos.md` da pasta. O que o README e a rubrica de Stories já fixam (a janela, as palavras proibidas, o aviso do post sem verbo no futuro, a área segura) vale como está e não se repete aqui.

## Narrativos (N2)

**Os campos do formato, por Story:** o dispositivo, pelo nome da síntese de dispositivos; o adesivo, quando houver (o que o `data-adesivo` vai declarar); e, na tela parada, a contagem de palavras.

**O pedido na tabela de plantas** (rubrica de Stories v0.3, a testar): o pedido do último Story entra como linha da tabela de plantas e pagamentos (o passo 3), apontando o Story que plantou a tensão que ele retoma, e o texto do pedido diz por que agora (rubrica de Stories, S6). Quando um Story pede a história da pessoa (o pedido íntimo, S5), o teste a medir é se um Story anterior conta uma história vivida por quem publica, que só ela dá (a de personagem fictício declarado não vale como a real, até medir), e se a tela do pedido diz o que acontece com a resposta (quem lê, se vai ao Story, sem o nome).

**Na sequência de consciência e de venda** (rubrica de Stories, seção própria, a testar): a cabeça lista as sequências de jab dos dias anteriores; o produto só aparece da `virada` em diante; o prazo de venda vai com o fuso por extenso ("horário de Brasília", no Brasil); e o campo opcional **Combustível** diz o canal de fora que traz gente para a sequência (a legenda do post do dia, o fim de uma palestra, a lista de e-mail, se houver) e o texto da chamada lá, que segue a regra do dia do README. As palavras que soam como mentira ("fácil", "rápido", "simples") saem como aviso, e a pergunta "isto parece propaganda?" se faz a cada Story.

**A ordem própria,** porque a mesa dos arcos vem antes da escaleta:
1. **A parte da cabeça que não depende do arco:** o nível, a realidade da peça, o objetivo com o pedido único e a peça de origem, e as regras conferidas.
2. **Os três arcos da mesa,** cada um com os Stories em uma linha, a story line, o fecho numa frase e onde fica a passagem do emocional ao técnico, ou por que o arco não a tem (README dos Stories, "O arco e a venda"); a quantidade de Stories é item da mesa, não decisão do roteiro.
3. **A mesa dos arcos** (o passo 6 da skill, aqui antes da escaleta).
4. **O resto da cabeça, sobre o arco escolhido** (o que está em jogo, o padrão de ordem), e daí os passos 2 a 5 e 7 a 9 da skill.

**A abertura:** duas ou três aberturas para o Story 1, cada uma por um caminho diferente da base, com a fonte ao lado (rubrica de Stories v0.3, a testar): a curiosidade concreta ("você escolhe o carro mais barato ou o melhor?") e o enquadramento de notícia, começar no meio do conflito, nunca "hoje vou contar", e o nome esquisito que faz parar (`knowledge/content-design/stories-10x-dispositivos.md`); cada uma com o "falha quando" (o que faria a pessoa sair ali), e a escolhida com o porquê; cada uma passa pelo passo 5 da skill. Na venda, o mesmo vale para o tema: o problema vizinho atrai, e o produto vem no fim.

**O Story em vídeo** (rubrica de Stories, "Story em vídeo"): a tabela de tempo do roteiro ("| Tempo | Na tela | ... |"), uma linha por trecho ("7–12,6 s"), com as frases da linha separadas por " / " e a que entra depois na linha dela, porque o `stories/scripts/video_do_story.py --roteiro` conta cada frase sozinha contra o trecho (`caracteres ÷ 17` s, piso de 0,3 s por palavra) e avisa a que fica abaixo: a frase se divide, não acelera. Com voz, o roteiro diz "legenda: adesivo, revisada" ou "legenda: queimada, revisada", e o texto da tela não repete a fala.

**A véspera:** o arco da sequência que prepara uma resposta de véspera já diz o que a manhã seguinte faz com as respostas: o critério da resposta (abaixo) nasce aqui, antes de haver respostas.

**A trava:** depois da `review`, o texto vai à forma "a travar", que é estado do texto e não estágio: o `estagio` do frontmatter segue o vocabulário de [`decisions/artefatos-e-estagio.md`](../../../../decisions/artefatos-e-estagio.md) (`a-validar` enquanto espera a leitura da pessoa). O ok vem na leitura da prévia, e só então esta skill grava a linha da trava, chamada por quem fez a prévia; a mudança de texto pedida ali volta à escaleta, por esta skill.

## O ramo da resposta (N1)

A sequência que devolve as respostas da caixinha e o resultado da enquete. Não tem arco: tem moldura, curadoria e unidades.

**A ordem:**
1. **A cabeça pelo N1** (o passo 1 da skill), com o **Critério de escolha** escrito antes de ler as respostas: quantas entram, em que ordem, e o que acontece com as que não entram. Se a sequência de origem já deixou o critério escrito, use-o e diga de onde veio; se a leitura das respostas pedir para mudá-lo, a mudança vai escrita, com o porquê.
2. **As respostas,** lidas onde a regra de dado de terceiro as deixa (o `originals/` ao lado do `roteiro.md` da sequência de origem, fora do git). No `roteiro.md` vão a contagem, o tema de cada uma e como foi respondida; o texto integral e o @ de quem respondeu ficam no `originals/`, e o nome não aparece no cartão compartilhado.
3. **A escaleta** (o passo 2), uma unidade por resposta escolhida, com os campos comuns: a função; o que o comentário de quem publica diz; a **Fonte** (a resposta pelo número ou pelo tema, sem o @); o que aparece (o cartão no espaço livre e o desenho); e o que puxa a próxima. "Promete" e "paga em" e a tabela de plantas (o passo 3), só onde houver promessa. Unidade a unidade, o comentário trata o caso de quem respondeu, o que o cartão conta, e, como teste a medir (rubrica de Stories v0.3, S5, a testar, sem entrar na nota), não vira mini-aula de dica geral ("ensinar algo geral é palestra, não Stories").
4. **Os passos 4 e 5:** a coluna do que aparece, conferida contra o post do dia, a sequência de origem e a resposta anterior: **nenhum desenho repetido do que foi ao ar no post do dia nem na sequência de origem, sem exceção por motivo escrito** (vale também para o aviso do post da noite, quando vai na sequência); só o reaproveitamento que a pessoa pedir entra. Os desenhos gerados para o post que não foram ao ar podem entrar. E cada resposta repostada conferida sozinha, porque cada uma é tela de entrada.
5. **A escolha com a pessoa** (o passo 6), sem mesa de arcos.
6. **O texto e as conferências** (os passos 7 e 8): dos passos de conferência (`conferencias.md`), rodam os que não pedem arco (a exposição, o 11, e a poda, o 13); os outros vão com o "não se aplica, porque a resposta não tem arco".
7. **As que não entram** ganham o texto sugerido da resposta direta, na tabela de respostas do roteiro de origem, como o README dos Stories manda; depois, a revisão e a trava (o passo 9), como nos narrativos.

**Os campos fora do N1** (a tabela do contrato, `contrato.md`) vão com o "não se aplica, porque…" e o motivo desta sequência. Se mais da metade dos campos comuns das unidades sair "não se aplica" numa sequência, anote em [`../licoes.md`](../licoes.md): é o sinal de que a resposta pede outro contrato.

## A lista curta da base

| Base | O que se confere |
|---|---|
| `knowledge/content-design/stories-10x-dispositivos.md`, "A tabela" e "Perguntas de sim ou não para avaliar uma sequência" | o dispositivo de cada Story; o tema, a virada e o fim escritos; o primeiro Story que pede resposta |
| `knowledge/content-design/stories-o-que-evitar.md`, "3. Depender de ter visto outra tela" | a tela de entrada (a primeira, o resultado, a resposta repostada) que se entende sozinha |
| `knowledge/content-design/tempo-de-leitura-em-video.md`, "A tela parada do Story" | as palavras por tela parada |
| `knowledge/content-design/escrever-em-linguagem-simples.md` | o jargão e o termo interno, trocados ou explicados |
| o README dos Stories (`references/projeto.md`): "O arco e a venda" (a mesa dos arcos, a abertura, a semana de venda, o combustível), a provocação do dia e a resposta à caixinha | a mesa, a provocação com a origem e a fonte, e o caminho das respostas; na consciência e na venda, as palavras que soam como mentira e "isto parece propaganda?" |
| as lições das peças (`references/projeto.md`), "Ideia, pauta e texto" e "Forma" | as linhas de Stories e de "todas" |
