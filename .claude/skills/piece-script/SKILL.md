---
name: piece-script
description: >-
  Escreve o roteiro de uma peça por formato (o arco e o texto das telas de um carrossel, a escaleta e o texto de uma sequência de Stories, a fala e os blocos de um Reel, a folha de uma cena com voz) até a trava do texto, e grava a escaleta que a forma lê. USE quando a criação de peças chamar o roteiro, ou quando a pessoa pedir para roteirizar uma peça, refazer o arco, escrever ou reescrever o texto das telas ou dos Stories, ou escrever a fala ou a folha de um vídeo, mesmo que não diga "roteiro". NÃO use para achar o ângulo (`story-angle`), apurar (`research`), o Story avulso de uma tela ou a peça inteira (`piece-creation`), montar o HTML ou gerar imagem (`image-gen`), revisar texto pronto (`review`) nem exportar (`slides-export`).
---

# Skill: piece-script

O roteiro da peça, do arco à trava do texto: a escaleta que diz o que cada unidade faz, o que aparece nela e o texto que a forma vai assentar sem trocar palavra. Recebe uma pauta ou uma moldura já decididas; **não apura, não escolhe o ângulo e não desenha a tela.** Os passos de roteiro são técnica clássica do ofício; esta skill os torna obrigatórios e na ordem, antes do texto.

**Lições:** antes de começar, leia as abertas e as apontadas em [`licoes.md`](./licoes.md) desta pasta. **O que é deste projeto** (as réguas, as pastas, a série, as lições das peças, o script de conferência do texto) está em [`references/projeto.md`](./references/projeto.md); leia antes do passo 1.

## Entrada

Quem chama (a criação de peças, ou a pessoa) passa: o formato e o tipo da peça; a pauta com o ângulo escolhido e os não escolhidos (carrossel) ou a moldura da sequência (Stories: objetivo, pedido único, a peça de origem); o ledger ou as fichas de onde sai cada fato; a pasta da peça; e, na série, a escaleta da irmã da semana, se já existe. Se falta o ângulo ou o lastro de um fato, pare e diga: é trabalho da `story-angle` ou da `research`, não daqui.

Depois, leia o arquivo do formato e só ele: [`references/carrossel.md`](./references/carrossel.md) (a série e o avulso), [`references/stories.md`](./references/stories.md) (narrativos e o ramo da resposta) ou [`references/cena.md`](./references/cena.md) (Reels e cena com voz). Cada um diz os campos do formato, onde os arquivos ficam, as paradas, a lista curta da base daquela etapa e, quando o processo do formato pede, uma ordem própria dos passos.

## O contrato em níveis

O contrato é a escaleta: cabeça, unidades e pé. O nível é do **tipo** da peça, não da peça; subir de nível é livre, descer pede o motivo escrito na cabeça.

| Tipo | Nível | Quem escreve |
|---|---|---|
| Story avulso (uma tela: compartilhamento, aviso) | N0, a moldura | o briefing da criação de peças; **esta skill não roda**: se for chamada para um avulso, diga isso e devolva, salvo quando o avulso pede arco: aí ele sobe a N1, com o motivo na cabeça |
| Stories de resposta | N1, a moldura e as unidades com os campos comuns | esta skill, pelo ramo "resposta" de `references/stories.md` |
| Stories narrativos, carrossel, Reels, cena | N2, o contrato inteiro | esta skill |

**Os campos de cada parte (cabeça, unidade, pé), com o que diz cada um e em que nível entra, e a regra do campo fora do nível, estão em [`references/contrato.md`](./references/contrato.md).** Leia antes do passo 1: os rótulos são os da escaleta, e o `scripts/confere_contrato.py` os confere por eles.

## As cinco invariantes

Valem em qualquer padrão de ordem (o porquê de cada uma vai junto, em cada item), e se conferem na escaleta, unidade a unidade:

| Invariante | N1 | N2 |
|---|---|---|
| A unidade de entrada se entende sozinha: no carrossel, a tela 2 sem a capa; nos Stories, a tela de entrada sem as anteriores | sim | sim |
| A ponte: cada unidade, menos a última, puxa a próxima pelo conteúdo | sim | sim |
| O fecho paga a abertura: responde à pergunta que ela fez | sim | sim |
| No máximo uma chamada, a que o objetivo pede | sim | sim |
| A carga alterna: nenhum bloco do mesmo porte do anterior, e o penúltimo com sinal oposto ao do fecho | não se aplica, porque a resposta não tem arco | sim |

## Os passos, nesta ordem

O arquivo do formato pode mudar a posição da parada (passo 6) e dizer quais passos o N1 roda.

1. **A cabeça**, inteira, antes de qualquer unidade.
2. **A escaleta antes do texto.** Uma entrada por unidade, com os campos comuns, sem texto de tela nem fala: o que acontece, a função, e o que **promete** e onde **paga em**. É aqui que aparece a promessa sem pagamento e a unidade que falta; numa linha só de prosa, elas não aparecem.
3. **A tabela de plantas e pagamentos,** no pé da escaleta: cada coisa plantada (a pergunta, o objeto, o número, a promessa da abertura) com a unidade que a paga. Promessa sem pagamento ganha a unidade que falta ou sai; nenhum mistério falso.
4. **A coluna do que aparece**, preenchida linha a linha (seção abaixo).
5. **A unidade de entrada, conferida sozinha, como se fosse a única vista.** Ela já dá motivo para ficar (a promessa concreta está nela, não só na seguinte)? Se entende sem as outras? No carrossel, confira também a tela 2 sem a capa. Se a resposta for não, refaça a abertura antes de seguir.
6. **A parada do formato**, no ponto em que o processo dele já a põe (tabela abaixo e arquivo do formato). **Esta skill não cria mesa nova.**
7. **O texto ou a fala**, só agora, a partir da escaleta aprovada, com as conferências do arquivo do formato. Depois, os passos de conferência de [`references/conferencias.md`](./references/conferencias.md) que a cabeça e a escaleta ainda não cobriram, do 5 (a análise de cena) ao 15 (a lista curta das perguntas), mais o 16 na série de biografias: os que acharem defeito se resolvem na escaleta e descem ao texto, não o contrário.
8. **O cético, antes da conferência:** banque o cético da própria premissa, como quem lê desconfiado; ela não pode ser refutável nem pretensiosa, e a que não resiste volta à cabeça (passo 1). **A conferência do contrato** (os rótulos, pelo `scripts/confere_contrato.py <escaleta>`, em 0 ERRO; o resto, à mão): cada campo do nível preenchido ou com o "não se aplica, porque…" fora dele; as invariantes do nível; cada promessa paga; cada ponto dos não escolhidos com a peça e a unidade de destino, o destino dado por uma decisão de quem decide a peça seguido, e o ponto que outra peça mandou para cá numa unidade daqui; e a frase que o campo **Representação** proíbe fora da unidade que tira lição ou pede ação ao leitor e da chamada. E que cada unidade do N2 tem **Promete** e **Paga em** em rótulos próprios e cada unidade com fato aponta a ficha em `knowledge/sources/`. E, em todo nível, a conferência comum: o lastro de cada fato na fonte que existe, o que aparece em cada unidade contra as vizinhas da semana, o pedido único e as palavras por unidade.
9. **A revisão** (seção abaixo) e **a trava do texto**.

## A coluna do que aparece

O roteiro decide o que se vê; a forma decide como se desenha. Por isso a coluna é do roteiro e não fica para depois.

- **Uma linha por unidade, sem "a definir".** Diga a função da imagem (demonstrar, organizar, explicar por analogia; sem função, é enfeite) e o que ela mostra.
- **Do banco antes de gerar:** procure primeiro nos `assets/` das peças publicadas do formato e da série, nas fotos da marca, nas telas animadas já feitas e no banco de imagens geradas (os caminhos em `references/projeto.md`; o banco é o índice da `image-gen`, com o que cada uma mostra, o traço e onde já foi usada), e **nomeie o arquivo** (o caminho), pelo critério de reaproveitar da `image-gen` (nada de repetir o desenho da semana nem o da peça irmã). Só proponha gerar quando o banco não tiver, dizendo por quê; a geração em si fica com a forma e a `image-gen`.
- **Conferida contra a peça do dia e a sequência anterior do mesmo tipo:** nenhum desenho repetido do que foi ou vai ao ar na semana (o calendário do projeto, quando houver, diz o quê; o post do dia incluído) sem motivo escrito; o reaproveitamento que a pessoa pedir entra com o motivo. **Nos Stories de resposta, sem exceção por motivo escrito,** e conferida também contra a sequência de origem (`references/stories.md`, o passo 4 do ramo da resposta).
- **Nenhuma unidade só com texto** entre vizinhas com desenho, salvo motivo escrito.
- **A frase do movimento e a lista de peças ficam fora da escaleta.** Na unidade cujo objeto é a explicação e se move (funciona, se monta ou se separa diante de quem lê), a coluna nomeia o objeto e a função da imagem, como em qualquer unidade. A frase do que se move e do que o movimento significa, e a lista de peças por grupo, com a função de cada uma, são da skill `object-anatomy`, que a forma chama e que os escreve antes de qualquer traço, no `object/objeto.md` da peça; a escaleta não abre esses campos, nem com o "não se aplica", porque não estão no contrato. Se a frase do movimento não sai, o objeto não mapeia e volta à escaleta. Antes de pôr um objeto em movimento na coluna, a pergunta do filtro (passo 0 da `object-anatomy`): é uma coisa física real, com peças que quem lê ganha ao ver funcionar ou se separar, e com fonte do interior? Aparelho que só existe no desenho, fluxo entre aparelhos ou efeito em quem lê não é objeto em movimento: a coluna pede o diagrama a caneta ou o desenho parado.
- **No vídeo, a coluna é da tela, frase a frase de voz, com o tipo de cada frase** pela tipologia da voz contra a imagem: S (soma o que a tela não mostra), F (fio que liga as telas), A (antecipa o que vem), C (contraponto à imagem) ou R (repete o que a tela já mostra). A pergunta é sobre o que **entra ou muda** na tela durante a frase, contra a frase inteira (dividir a frase em duas linhas não cria soma): o que isso mostra que ela não diz (o objeto que ela não nomeia, o número, a data ou o nome que ela não diz, o tempo que passa, o antes e o depois)? Se a resposta é "o que as palavras dela dizem", a linha é R e sai marcada **REPETE**, e isso vale para a palavra escrita ou realçada **e para o desenho literal do que a frase diz, entrando na palavra que o nomeia** (as pessoas em "amigos", o storyboard em "curta", o "?" em "a ordem"): entrar na palavra amarra a imagem à voz, mas não faz o desenho somar. Troque por imagem que some antes de travar. A exceção é o rótulo curto dentro de uma estrutura (a contagem, o nome, a data, o termo técnico) e o emblema de cada item no fio (F), só quando a voz liga uma série que as imagens sozinhas não ligariam (a lista, o mapa); na linha que traz uma palavra da frase e algo que ela não diz, vale o que mais pesa no que acrescenta, e acréscimo mínimo é R; sob a tela parada, a frase que dá o que a imagem não mostra soma, e a que só a descreve repete.

## As paradas com a pessoa

As paradas antes do texto são as que o processo de cada formato já tem, e estão no arquivo do formato (no carrossel e na cena, "As paradas"; nos Stories, a ordem própria de cada ramo). O ok da trava:

| Formato | O ok da trava |
|---|---|
| Carrossel | na entrega da `review`, sem mesa própria |
| Stories narrativos e de resposta | na leitura da prévia (`references/stories.md`, "A trava") |
| Cena e Reels | na mesa da fala; a direção de arte da tela vem depois, fora desta skill |

O que é regra se confere antes e não vai à mesa; só vai à pessoa o que é gosto e direção de arte ([`decisions/mesas-de-design.md`](../../../decisions/mesas-de-design.md)). Quando quem chama já traz a escolha dela numa parada, siga com ela, sem perguntar de novo.

## Revisão (skill `review`)

- **Ponto de pausa:** com o texto ou a fala escritos e o contrato conferido (passo 8), antes de pedir o ok que trava o texto.
- **Nível:** padrão.
- **Lentes:** régua (sempre) + fidelidade, além da evidência, de fora, comparar com o anterior.
- **Conferir contra:** o ledger e as fichas da peça; a rubrica do formato (`references/projeto.md`); a estrutura editorial da série ou o README dos Stories; a peça-par publicada do mesmo tipo e a sequência anterior.
- **Itens que de fato se esquecem aqui:**
  - toda fala entre aspas com ficha própria e o verbatim achado nela; sem isso, discurso indireto com a fonte nomeada;
  - cada promessa com a unidade que a paga, e a abertura que dá motivo para ficar já nela;
  - a coluna do que aparece com o arquivo nomeado em cada unidade, sem repetir a peça do dia nem a sequência anterior sem motivo escrito (nos Stories de resposta, sem exceção por motivo, e nem a sequência de origem: `references/stories.md`);
  - no vídeo, o tipo de cada frase de voz reconferido linha a linha por quem não escreveu a folha (quem escreve tende a contar como soma o desenho que entra na palavra), e nenhuma R fora da exceção de "A coluna do que aparece" (o rótulo curto dentro de uma estrutura, o emblema no fio);
  - cada ponto dos não escolhidos na peça a que serve, com a unidade de lá, e o que outra peça mandou para esta numa unidade daqui;
  - a representação conferida na unidade que tira lição ou pede ação ao leitor e na chamada, e a ironia marcada;
  - o campo fora do nível com o "não se aplica, porque…".

Os achados confirmados voltam à escaleta, e dela ao texto.

## A trava do texto (a saída)

Com o ok da pessoa na parada da tabela, o texto trava, e a linha "Texto travado em AAAA-MM-DD, com o ok de <quem, em que parada>" vai ao `refinamentos.md` da pasta da peça. Nos Stories, o ok vem na prévia, que é da forma; o caminho está em `references/stories.md`, "A trava". Daí em diante a forma assenta o texto sem trocar palavra; o pedido que muda o arco ou o texto volta à escaleta.

**O que esta skill escreve, e só isso:** os arquivos do formato (o arquivo do formato diz quais); no `roteiro.md` dos Stories, o frontmatter, a cabeça e a seção "Os Stories", sem tocar nas seções da forma, do publicado e do resultado; na `legenda.md`, o texto (a legenda, o texto alternativo e as hashtags), porque os embeds são da `slides-export`.

## Nunca

- Escrever o texto antes da escaleta, ou a escaleta sem "promete" e "paga em".
- Deixar a coluna do que aparece para a forma, ou propor gerar imagem sem ter procurado no banco.
- Criar uma mesa que o processo do formato não tem, ou perguntar o que já é regra.
- Pôr fato sem fonte, ou fala entre aspas sem verbatim fichado.

**Ao terminar:** se houve falha, contorno ou acerto que vale lembrar, registre em [`licoes.md`](./licoes.md) desta pasta, na mesma entrega (formato e estados em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md)).
