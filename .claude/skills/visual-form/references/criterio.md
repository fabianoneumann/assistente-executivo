# O critério da forma: ler, classificar, propor e mover

Os passos 5, 7 e 8 do `SKILL.md` e o vocabulário dos pedidos de quem pede. As partes marcadas "a partir do Impeccable" foram portadas com crédito, **a partir do Impeccable** (`pbakaus/impeccable`, licença Apache 2.0, lido sem instalar nem executar), com as palavras e as regras da casa e sem copiar texto do original. O resto vem da base de design e de avaliação por modelo; as sínteses estão em `knowledge/content-design/` e `knowledge/agent-engineering/`, quando a base do repositório as tiver.

## 1. A leitura crítica antes dos números (a partir do Impeccable, o `critique`)

O número ancora o juízo: quem lê o AVISO antes de olhar a tela passa a ver só o que o AVISO apontou. Por isso, com a peça renderizada e o 0 ERRO, **olhe antes de medir**:

1. Abra a tela-par publicada (a da mesma função na peça anterior do mesmo tipo) e diga o que ela tem e o que ela ousou; só então abra a tela nova.
2. Abra a tela nova inteira (o que se lê sem zoom) e ampliada (cada junção: texto encostando em desenho, a chamada que termina no vazio, a espessura do traço).
3. Escreva a **lista de defeitos**, não uma nota: a tela, o elemento, o que falta ou está errado, a gravidade (crítica, maior, menor) e a correção proposta. A nota direta se espreme no alto e não separa o bom do ruim; a lista de defeitos localizados separa, com um custo: o modelo marca muito mais do que há, sobretudo de estilo, e acerta pouco do que marca (a síntese "defeitos no lugar da nota", em `knowledge/agent-engineering/`). O método para separar o real do alarme é corrigir o defeito e comparar as duas versões.
4. Ao olho se pergunta **onde está o defeito**; a medida fina (posição, largura, contraste) fica com o código (a síntese "juiz de visão julgando design").
5. **A função da imagem:** o desenho feito cumpre a função que a escaleta declarou (literal quando a coisa tem forma; metáfora com a correspondência dita no texto)? A imagem que só enfeita custa atenção (a síntese "metáfora visual e demonstração", em `knowledge/content-design/`).
6. Só então leia os AVISOs do `conferir_telas.py`, o `mede_forma.py` e a ocupação contra a tela-par, e acrescente à lista o que eles acharam e você não.

Esta leitura é sua, no contexto da forma; não substitui a I2, que é de um agente que não fez a forma.

## 2. Refinar preserva, redesenhar substitui (a partir do Impeccable, o `polish`)

- **O ajuste preserva o mundo visual e o texto da peça.** Num pedido de forma, o texto aprovado fica; refazer a tela inteira é outra coisa, e se diz: "isto é redesenho da tela N, não ajuste".
- **Pergunte antes de mudar texto factual.** Um número, um nome, uma data ou uma citação que a forma acha que devia mudar (porque não cabe, porque repete) vai à pessoa como pergunta, com a fonte; a forma não muda.
- **Classifique cada desvio antes de corrigir,** porque cada classe tem um lugar diferente:

| Classe | O que é | Onde se corrige |
|---|---|---|
| **Token que falta** | o design system não tem o valor que a tela pede (uma cor, um tamanho, um peso) | não na peça: é decisão de série, no `design/caderno.css` e no `design-system.md`, com data; até lá, a tela usa o que existe, ou o desvio se avisa |
| **Implementação avulsa** | a peça refez à mão algo que o sistema já tem (uma marca, uma seta, um espaçamento) | troque pelo componente do sistema (`caderno.css`, `caderno.js`) |
| **Conceito** | a tela diz outra coisa que a escaleta, ou a imagem não cumpre a função | volta à escaleta (a `piece-script`), nunca se resolve no HTML |
| **Defeito local** | posição, tamanho, junção, quebra, contraste nesta tela | corrija na tela e confira de novo |

## 3. A forma em passos, e o HTML

- **Os sete passos da Robin Williams** estão no `SKILL.md`, passo 5. Do livro, os que mais pesam na tela: a segunda borda de alinhamento para a hierarquia e um rompimento só; o texto contra a borda reta da imagem; o contraste sem timidez e um foco só. Dos princípios de design visual: a proximidade se confere apertando os olhos, e a cor se testa em cinza.
- **O HTML:** flexbox por padrão; grid só para texto e desenho lado a lado e para a anotação empilhada sobre o desenho; posição absoluta só no que se ancora na tela. A pergunta de cada `position: absolute`: **"se o texto mudar, isso fica onde está?"** (a síntese "layout de peças em HTML").
- **Quando o texto não cabe:** o que cede, na ordem do design system (primeiro o que não custa espaço), com o degrau testado em código (os dois corpos renderizados, as linhas contadas), e o antes e o depois à pessoa se o degrau mexe no papel (as sínteses "texto que cabe e legibilidade" e "quebra de linha em tela"). Cortar texto é alternativa dela, nunca ajuste da forma.

## 4. As alternativas pelo que conduz a tela (a partir do Impeccable, o `visualize`, e da Williams, cap. 12)

As alternativas de forma variam **o que se vê primeiro** (o título, a imagem, o número), como os três redesenhos do cap. 12 da Williams, e não o enfeite nem o detalhe de uma versão só. Duas a três, renderizadas no mesmo acabamento, cada uma com o nome do que conduz e uma frase do que ela ganha e do que custa. Onde a quantidade de texto pesa, uma explica com texto e outra mostra com imagem. As que violam regra não vão: o que é regra se confere antes, e só o gosto sobe (`decisions/mesas-de-design.md`). A avaliação por modelo só se mostrou confiável na comparação em pares com violação clara: entre alternativas boas, a escolha é da pessoa.

## 5. O vocabulário dos pedidos (a partir do Impeccable, os comandos de direção)

Cada pedido é **um movimento num alvo**, que preserva o resto da tela e não inventa cor, fonte nem token: usa o que o sistema já tem.

| A pessoa diz | O movimento | Como se confere |
|---|---|---|
| "mais forte", "com mais força" | sobe a força do foco com o que o sistema tem: o dominante maior, o contraste de tamanho e peso, uma marca de acento no ponto certo, o destaque manuscrito | **o teste do esqueleto:** na versão sem texto (`prepara_i2.py semtexto`), a estrutura ainda diz o que a tela é e onde está o foco? |
| "mais calma", "menos carregada" | baixa a intensidade sem tirar a personalidade: menos marcas, menos pesos, mais respiro, o acento em menos área | a tela ainda tem a assinatura da série (o que o design system chama de assinatura), e o foco continua um só |
| "limpa", "enxuga" | tira o que não ganha o lugar: a anotação que não diz nada, o enfeite, a terceira marca | cada elemento que fica tem função dita; nenhuma palavra do travado sai (cortar texto é outra conversa) |
| "a hierarquia não está clara", "não sei para onde olhar" | ordem de leitura, grupos e ritmo; tipo: tamanho e peso por papel | **o teste de apertar os olhos:** com a vista desfocada, os grupos e a ordem ainda aparecem (a proximidade da Williams) |

Quando o pedido é vago ("melhora a tela 4"), proponha o movimento antes de mexer, numa frase, e siga com o que a pessoa escolher.
