# O contrato da escaleta: os campos por parte

Os campos que a escaleta abre em cada parte (cabeça, unidades, pé), com o que cada um diz e em que nível entra (N1, N2). O nível do tipo da peça está no `SKILL.md`, "O contrato em níveis".

**Campo fora do nível não some:** sai escrito "não se aplica, porque…", numa linha, no lugar do valor. Dentro do nível, campo vazio é erro, e "a definir na forma" também. **Os rótulos da tabela abaixo são os da escaleta, em negrito, e não mudam,** porque o `scripts/confere_contrato.py` os lê (passo 8 do `SKILL.md`); os campos do formato vêm no arquivo dele. **O destino dos Não escolhidos** nomeia a unidade ("aqui, tela 6", "→ o A, tela 5", ou a tela da receita pela função quando a outra peça ainda não tem escaleta), ou diz "fica fora, porque…"; a seta é opcional.

| Parte | Campo (rótulo) | O que diz | N1 | N2 |
|---|---|---|---|---|
| Cabeça | **Nível** | N1 ou N2, e o motivo, se desceu ou subiu | sim | sim |
| Cabeça | **Realidade da peça** | fato, reconstituição marcada ou ficção; a narração é autoral, e no formato documentário a neutra pode ser a escolha, caso a caso, dita aqui | sim | sim |
| Cabeça | **Objetivo** | salvar, enviar, comentar, seguir, atravessar a peça; nos Stories, também o pedido único e a peça de origem | sim | sim |
| Cabeça | **Regras conferidas** | as da série ou do README do formato que limitam esta peça, o "o que NÃO fazer" da pauta, quando houver, e as lições aplicadas, ou "nenhuma lição registrada" | sim | sim |
| Cabeça | **Critério de escolha** | quantas respostas entram, em que ordem e o que acontece com as outras, escrito antes de lê-las | sim | nos Stories de véspera, sim; nos outros, não |
| Cabeça | **Story line** | em até cinco linhas: algo acontece, algo deve ser feito, algo se faz; o conflito no nível em que está (interno, com o outro, com o sistema) | não | sim |
| Cabeça | **Fecho** | numa frase de valor e causa, "de x a y, pois z", escrito antes do gancho, com o tipo de final | sim | sim |
| Cabeça | **Em jogo** | o que de pior acontece se não der certo | não | sim |
| Cabeça | **Padrão de ordem** | pelo objetivo da peça, dizendo qual manda quando forem dois | não | sim |
| Unidade | **Função** · **Diz** · **Fonte** · **Aparece** · **Puxa a próxima** | a função na receita ou no arco; o que acontece ou diz; em toda unidade com fato, a ficha em `knowledge/sources/` que o sustenta, com a linha, e a do ledger quando houver (fala entre aspas só com verbatim fichado); o que se vê (seção "A coluna do que aparece" do `SKILL.md`); o que puxa a próxima ("mas" ou "portanto", não "e depois") | sim | sim |
| Unidade | **Valor** | o ponto capital numa frase: o valor que vira na unidade | não | sim |
| Unidade | **Promete** · **Paga em** | dois rótulos próprios: o que a unidade promete, e a unidade que paga; o pagamento vai no **Paga em**, nunca dentro do **Promete** nem da **Função**; no N2, os dois em toda unidade, e a unidade sem promessa leva "Promete: não se aplica, porque…" | só se houver promessa | sim, em toda unidade |
| Pé | **Plantas e pagamentos** | a tabela do passo 3 | só se houver promessa | sim |
| Pé | **Não escolhidos** | ponto a ponto, listado, cada ponto dos ângulos não escolhidos da pauta (na série, a pauta é da semana e vale para o A e para o B) vai à **peça a que ele serve**: esta, com a unidade daqui nomeada, ou outra, nomeada e com a unidade de lá (quando a outra ainda não tem escaleta, a unidade da receita do tipo dela, nomeada pela função); quando uma decisão de quem decide a peça já pôs o ponto numa peça (a pauta, o checkpoint, a ficha da pessoa retratada), o destino é o dela, com a linha citada; o ponto que outra peça já roteirizada mandou para esta (lido no campo dela; na série, a irmã da semana) entra numa unidade daqui, ou volta com o porquê, salvo quando o destino veio dessa decisão, que só quem a tomou muda; o que não serve a peça nenhuma fica fora, com o porquê (a `story-angle` já o guarda na fila de derivações). Destino faltando é erro, e "não se aplica" com a pauta tendo não escolhidos também | não | sim, quando a pauta tem não escolhidos |
| Pé | **Representação** | quando a peça conta a experiência de outra pessoa ou de um grupo: de quem é a experiência, o que vai como fato na voz da pessoa, e que frase dela não pode virar lição ou conselho para o leitor | quando houver | quando houver |
| Pé | **Exemplos** | exemplo, contraexemplo e antiexemplo | não | quando a peça ensina |
| Pé | **Enriquecimento** | o método que a base trouxe, com o arquivo (nota abaixo) | não | sim |
| Pé | **Ironia** · **Para ir além** · **Riscos** | a ironia usada, marcada para quem decide avaliar; as fontes e o próximo passo; os riscos para a mesa | ironia e riscos | sim |

**"Não" na coluna do nível é fora do nível.** O campo condicional ("só se houver promessa", "quando houver", "quando a peça ensina") cuja condição não ocorre também sai com o "não se aplica, porque…" e o motivo (sem promessa, sem pessoa retratada), e não conta no sinal de contrato que não serve, do `references/stories.md`. **A passada de enriquecimento** é a skill `base-enrichment`, uma chamada por camada (arco antes da mesa do arco, imagem nos conceitos, texto antes da trava), e o resultado vai ao campo **Enriquecimento**, com as sugestões aplicadas ou levadas à mesa pelo destino de cada uma.
