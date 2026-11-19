---
versao: 0.1.0
data: AAAA-MM-DD
status: modelo em branco; os valores de partida (papeis.json, caderno.css) são a identidade neutra do exemplo
---

# Sistema visual da série: <nome da série>

A régua de forma da série, lida pela `marketing/social-media/rubrica-de-design.md` e pela skill `visual-form`. Os valores vivem em [`design/caderno.css`](design/caderno.css), o que a página faz sozinha em [`design/caderno.js`](design/caderno.js) e a tabela de papéis em [`design/papeis.json`](design/papeis.json), que todo `slides.html` da série importa; este documento diz as regras. Mudar uma regra daqui é decisão de série, com data no "Histórico". Cada seção abaixo vem com o roteiro do que decidir (as linhas em itálico): troque o roteiro pela decisão, e apague o que não se aplica.

## Como usar

*O que escrever:* a ordem de leitura para montar ou conferir uma peça (este arquivo; o `caderno.css`, com todos os valores; o `caderno.js`, com o que ele faz sozinho; um `slides.html` publicado do mesmo tipo; a rubrica de design) e as **regras duras**, as que não se quebram sem um "Desvio, avisado".

*Decidir:* quantas famílias de letra, e de que categorias; quantas tintas e o papel de cada uma; se toda entrelinha e toda margem são múltiplos de um passo; o que nunca vai por cima de texto; o que é um foco por tela; o que conta como marca desenhada e o que é forma do CSS; a regra de foto (só real, com direito de uso e crédito; retrato gerado de pessoa real, nunca).

**Desvio, avisado:** regra quebrada de propósito vai no `refinamentos.md` da peça, uma linha por desvio ("Desvio, avisado: <regra>, porque <motivo>"), além da marca no HTML (`data-intencional` ou `data-sangria`).

## A ideia e a assinatura

*Decidir:* o conceito da série numa frase (de que objeto ou lugar a peça parece ser: um caderno, um quadro, uma ficha, um painel) e a **assinatura**, a ousadia num lugar só, que a rubrica de design exige: o elemento que faz a peça ser reconhecida antes de ser lida. A assinatura é estável e o objeto desenhado muda com o tema.

## Papel: um por tipo de post

*Decidir:* se a série tem um papel só ou um por tipo de post (por exemplo, A para personalidade e B para educativo), e, para cada um, a cor, a textura (liso, pauta, grade, pontos) e o passo em px. A tela declara o papel pela classe (`tipo-a`, `tipo-b`), e as conferências leem o papel por ela.

| Tipo | Papel | Passo | Por quê |
|---|---|---|---|
| A | *liso com grade de pontos (partida)* | 24 px | |
| B | *pauta fina a cada 48 px (partida)* | 24 px | |

## O texto assenta nas linhas

*Decidir:* se o texto assenta no passo do papel (o `caderno.js` reparte o espaço livre da `.coluna` em múltiplos do passo), o que vai em flexbox e o que vai em posição fixa (só o que tem lugar fixo: moldura, paginação, anotação em volta de um desenho), e como se mede (o `medir_blocos.py` da `visual-form`). A partida: flexbox por padrão, texto e desenho que se seguem na `.coluna`, os vãos nos `.respiro` com o peso em `--w`.

## Tintas

*Decidir:* cada tinta, o valor e a função; o contraste de cada uma sobre cada papel (nada abaixo de 4,5:1 no texto corrido, 3:1 no grande); o acento em pouca área. A cor do acento vai também em `"acento"` no `papeis.json`, para a conferência da área do acento.

| Tinta | Valor | Função |
|---|---|---|
| Tinta | *`#1F2933` (partida)* | *o texto de conteúdo e o desenho* |
| Acento | *`#0B6B58` (partida)* | *a nota, a marca, a peça acesa do desenho* |
| Apoio | *`#5B6470` (partida)* | *a moldura, a fonte, o que fica em segundo plano* |
| Marca-texto | *`#FFE58A` (partida)* | *a frase para levar, uma por post* |

## Letra

*Decidir:* as famílias e os pesos, e o corpo e a entrelinha de cada papel em cada tipo de post; um tamanho por papel em cada tela. A tabela tem cópia em dados no `design/papeis.json`, que as conferências da forma leem; quem muda uma muda a outra, e o `teste_papeis.py` da `visual-form` confere que dizem o mesmo. Os nomes da primeira coluna são os que o teste lê: não os troque. Fonte da web pede rede na conferência e na exportação; a que não carrega é ERRO.

| Papel | Família e peso | No A | No B | Uso |
|---|---|---|---|---|
| Título | Exemplo Titulo 700 | 64 / 72 px | igual | o título da tela |
| Destaque | Exemplo Titulo 700 | 44 / 48 | igual | o gancho, a frase-chave |
| Corpo | Exemplo Texto 400, negrito 700 | 32 / 48 | igual | o texto que se lê; o negrito marca as palavras-chave |
| Apoio | Exemplo Texto 400, tinta de apoio | 30 / 48 | igual | o texto de apoio |
| Citação | Exemplo Titulo 700 | 52 / 72 | igual | a fala literal, com fonte |
| Nota | Exemplo Texto 400, acento | 32 / 48 | igual | a anotação, a pergunta que puxa a próxima tela |
| Chamada | Exemplo Texto 400, acento | 44 / 72 | igual | o pedido da última tela |
| Fila | Exemplo Texto 400, tinta de apoio | 30 / 48 | igual | o que se deixa de lado, esmaecido |
| Endereço | Exemplo Texto 700 | 30 / 48 | igual | o link que a pessoa vai digitar |
| Moldura e fonte | Exemplo Texto 400 | 24 / 48 | igual | a série, a paginação, a fonte de um número |

*Decidir também:* a quebra de linha (título, destaque e citação com `text-wrap: balance`; corpo e nota com `pretty`), a lista das palavras curtas que não terminam linha de título (a `CURTAS` do `caderno.js`), e a ordem do que cede quando o texto não cabe (começando pelo que não custa espaço; cortar texto é decisão de quem escreve, não da forma).

## Grade e moldura

*Decidir:* as margens (a de partida, 104 px de cada lado), a moldura (o que vai nela, onde, igual em todas as telas), a paginação, o que a capa leva e o que a última tela leva. Lembre que o app cobre o canto de cima à direita na primeira leitura do carrossel, e que a grade do perfil corta a capa dos lados.

## Anotações: o kit

*Decidir:* que anotações a série tem (nota à margem, pergunta que puxa a próxima tela, correção riscada, rótulo com seta, sublinhado, círculo, marca-texto), em que tinta, quantas por tela, e a regra da seta (a ponta entra no alvo, de 20 a 30 px, e nunca cruza letra; o conector entre dois desenhos só encosta). Cada anotação diz alguma coisa e aponta para o que comenta; a que só enfeita é enfeite.

## Imagem e desenho

*Decidir:* a regra de foto; o estilo do desenho (traço em SVG, ilustração gerada, os dois, e qual para quê: o objeto parado, o diagrama, a linha do tempo, o objeto que se move); o peso do traço; o enfeite (o que só decora custa atenção; um dominante por tela; no máximo três tamanhos); a marca da reconstituição, quando um desenho reconstitui um momento documentado. Se as regras de desenho crescerem, elas vão a um `design-system-desenho.md` ao lado, que é parte desta régua.

## Stories

*Decidir:* se a série vai aos Stories e o que muda lá. As regras gerais dos Stories (área segura, adesivos, enfeite, o modelo em flexbox) estão em `marketing/social-media/stories/README.md`; aqui fica só o que é da série.

## Regras da casa: os limites que o código aplica

As conferências da `visual-form` (`conferir_telas.py`) aplicam estes limites antes da exportação; o que passa do limite é defeito que se corrige antes do juiz. A tabela completa, com o nível de cada achado, está em `.claude/skills/visual-form/references/conferencias.md`. *Decidir:* se a série muda algum (e então o código muda junto, com teste). O travessão é regra de voz, não de série: a conferência o trata como ERRO quando `context/sobre-mim.md` pede texto sem travessão, e como AVISO no resto.

| Conferência | Limite |
|---|---|
| Título fora do alinhamento das telas irmãs | acusa acima de 2 px; acima de 100 px pode ser escolha, declarada com `data-alinhamento` |
| Contraste e contraste parcial | 4,5:1 no texto corrido e 3:1 no grande, na mediana e nos 10% piores pixels |
| Texto cortado ou passando da borda | nenhum; sinal gráfico sangra com `data-sangria` |
| Texto sobre texto, texto sobre desenho | nenhum, salvo `data-intencional` |
| Cor declarada anulada pelo CSS | nenhuma |
| Zona proibida do carrossel | título, destaque, chamada e ponte dentro de 1000 por 1270, centrada |

## O que a série escolheu de propósito

*O que escrever:* os padrões da lista de "cara de IA" da rubrica de design que a série usa mesmo assim, e por quê (números em sequência, sombra, degradê, fonte monoespaçada). Sem esta seção, o juiz conta cada um como defeito.

## Como montar um post

*O que escrever:* o passo a passo da série, que a `visual-form` segue. A partida:

1. O texto vem travado da etapa do roteiro (`texto.md`, no formato do `exemplo-de-post/texto.md`).
2. Copiar o `slides.html` de um post publicado do mesmo tipo (na primeira peça, o `exemplo-de-post/`), trocar o texto, refazer os desenhos e as anotações que mudam. O CSS da peça só posiciona; valor novo de cor, letra ou tamanho entra no `design/caderno.css`, no `papeis.json` e aqui, com data. Foto e imagem vão em elemento próprio, nunca como `background-image` da tela.
3. Conferir com a `visual-form` (as conferências em 0 ERRO) e exportar com a `slides-export`; subir ao bucket só quando a peça estiver pronta. Mudança no sistema regera as telas das peças e compara com a versão aprovada; peça publicada sobe como versão nova.

## Histórico

- **0.1.0 (AAAA-MM-DD):** o modelo em branco, com a identidade neutra de partida. *Cada mudança de regra entra aqui, com a data, o que mudou e o porquê.*
