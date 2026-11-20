---
versao: 1.0
status: rascunho a calibrar; versão nova pelos gatilhos da decisão 7 da rubrica de qualidade
---

# Rubrica de design de conteúdo

O que a forma de uma peça precisa ter para sair: hierarquia, legibilidade, coerência com o sistema visual da série e direção de arte própria. É a irmã de `rubrica-de-qualidade.md`, que mede a mensagem. Nasce do método de revisão de tela do Impeccable (`pbakaus/impeccable`, Apache 2.0) e das regras de design da base (`knowledge/content-design/carrossel-instagram.md`, `knowledge/content-design/principios-de-design-visual.md`).

**Por que separada.** A régua é outra (o sistema visual da série, e não o público e a tese), quem avalia é outro (código sobre o HTML e o CSS, e um modelo sobre a imagem renderizada) e a cadência é outra: o sistema visual se avalia uma vez, quando nasce ou muda, e cada peça se confere contra ele.

## A régua: o sistema visual da série

Cada série (e o perfil, para peças avulsas, quando houver uma identidade da marca em `context/brand/`) tem um `design-system.md` na pasta dela, que, com as partes que ele aponta, é a fonte única. A série de exemplo, em branco, é `carousels/series/exemplo/`. O sistema diz:

- **Tokens:** cores com uma função cada (um protagonista, um neutro, um acento), espaços, raios.
- **Papéis tipográficos:** uma tabela de papéis (título, corpo, destaque, rótulo, moldura), cada um com tamanho, peso e família. A peça usa papéis, não tamanhos soltos.
- **Moldura:** nome da série, número da tela, @. Não conta na contagem de papéis nem no corpo mínimo; conta no contraste.
- **Assinatura:** a ousadia num lugar só (uma tipografia, um tratamento de imagem, uma cor), dita por escrito.
- **O que a série escolheu de propósito**, com o porquê. Um padrão da lista de cara de IA (abaixo) só vale se estiver aqui com motivo: a série pode ganhar um padrão, o hábito não.

Sem `design-system.md`, a peça não passa do nível 1 em D3. Na calibração, com peças de terceiros, vale a coerência interna da peça (`portao-de-qualidade.md`, modos).

## Dois olhares

1. **Assinaturas e medidas** [código]: lidas no HTML e no CSS, cada uma com `arquivo:linha`.
2. **Percepção** [modelo]: sobre a imagem renderizada, tela a tela e a sequência inteira. O que só a imagem responde não vira achado de código.

## Critérios

| | Critério | 0 | 1 | 2 |
|---|---|---|---|---|
| D1 | **Hierarquia** | apertando os olhos, não se vê o que é principal | o principal aparece, mas compete com rótulos, moldura ou decoração | principal, secundário e grupos aparecem nessa ordem; o que se usa não está no menor corpo |
| D2 | **Legibilidade e medidas** | texto essencial ilegível no celular | legível, fora de alguma medida | dentro de todas as medidas abaixo |
| D3 | **Coerência com o sistema** | valores soltos, sem papel nem token | segue o sistema com desvios | cada texto num papel, cada cor num token com a função dela, o mesmo tratamento para o mesmo elemento em todas as telas |
| D4 | **Foco e carga por tela** | várias coisas disputando, cinco ou mais itens sem grupo | um foco, com excesso de itens ou de marcas, ou duas ênfases que puxam para lugares diferentes | um foco por tela, que sai da finalidade dela; até quatro itens por grupo, salvo o que o sistema libera; uma marca de ênfase do sistema por bloco, com o negrito das palavras-chave fora da conta, e nenhuma ênfase mais forte que o foco |
| D5 | **Composição e espaço** | espaço morto ou amontoado que quebra a leitura | equilibrada em parte das telas | grid respeitado, respiro entre grupos maior que dentro deles, nenhum branco preso entre elementos, e o vazio grande livre e usado pelo foco |
| D6 | **Direção de arte própria** | três ou mais marcas de cara de IA | uma ou duas, ou molde pronto sem marca | nenhuma marca não justificada no sistema, e a resposta a "autoral ou genérico?" é autoral |
| D7 | **Imagem** | estilos que conflitam ou sem espírito comum, mais de um estilo de desenho no vídeo, retrato gerado de pessoa real (falha de integridade na rubrica de qualidade) ou imagem sem direito | imagem coerente que só decora | imagem que carrega sentido, com crédito e direito de uso; no carrossel, os estilos que o sistema declara convivem, cada desenho num estilo só, com espírito comum sobre base firme e sem conflito; no vídeo, um estilo por peça |

## Testes

- **D1** [modelo] o teste de apertar os olhos mostra o principal primeiro? [modelo] o elemento que a peça manda usar (lista, link, passo) tem corpo e contraste de conteúdo, e não de rodapé?
- **D2** [código] as medidas abaixo, por papel. [modelo] o texto sobre imagem ou degradê lê bem na imagem renderizada? [código] nenhuma última linha com uma **palavra sozinha** (o `text-wrap: pretty` reduz no corpo e o `balance` resolve nos blocos de até seis linhas; o que sobra, quem faz a peça quebra à mão)? [código] nenhuma linha de título, destaque ou citação termina numa palavra curta da lista (a, o, e, é, de, em, da, do, no, na, um, ao, à, os, as, se, por), que vai **presa** à seguinte por espaço inseparável? [modelo] o título quebra por sentido, sem separar artigo e nome, preposição e termo, nome e sobrenome? A quebra à mão vale para isso: a imagem se renderiza uma vez, numa largura fixa, e não reflui. Os três são acabamento (P3); medidas e evidência em `knowledge/content-design/quebra-de-linha-em-tela.md`.
- **D3** [código] nenhuma cor fora dos tokens? [código] todo texto num papel do sistema? [modelo] o mesmo elemento (rótulo, número, cartão) tem o mesmo tratamento em todas as telas? Cada desvio se classifica antes de corrigir: **falta um papel ou token** (muda o sistema), **avulso** (o sistema já resolve), **desencontro** (duas telas resolvem igual de jeitos diferentes), **defeito local**. O desvio declarado no `refinamentos.md` da peça ("Desvio, avisado: <regra>, porque <motivo>") conta como escolha justificada, não como desvio.
- **D4** [modelo] um foco por tela, que sai da finalidade dela, do que o leitor procura ali? [modelo] apertando os olhos, o olho para em até três a cinco lugares? [código] até quatro itens por grupo, salvo o que o `design-system.md` libera? [modelo] uma marca de ênfase do sistema por bloco (sem sistema, uma marca gráfica de ênfase por bloco)? [modelo] o negrito das palavras-chave fica fora da conta: é uma camada só, repetida, e marca poucas palavras do bloco? [modelo] a marca e o negrito não caem em trechos diferentes da mesma frase? No mesmo trecho, somam-se e valem como uma ênfase, porque o contraste se faz somando atributos. [modelo] nenhuma ênfase do bloco fica mais forte que o foco da tela? Os princípios são os do livro de design de Robin Williams (contraste, repetição, alinhamento, proximidade; `knowledge/content-design/principios-de-design-visual.md`). Os quatro itens por grupo não vêm de fonte da base e ficam até uma medida.
- **D5** [modelo] o grid se mantém entre as telas? **O vazio:** [modelo] o vazio de cada tela está livre, aberto para a margem, ou preso entre elementos? O preso é defeito (P3). O livre, mesmo grande, é escolha quando o foco o usa; a tela meio vazia, o defeito, é o vazio livre que o foco não usa: sobra porque o conteúdo encolheu (P2). O tamanho não tem número na leitura: "meio vazia" é o vazio grande, e o aviso do código parte de 40%. [código] a medida é a **maior faixa horizontal vazia contínua, em fração da altura útil** (entre a moldura de cima e a de baixo), e avisa a partir de 40%; o aviso pede a leitura acima, não decide. A área vazia total da tela não se mede nem pesa: a quantidade de branco não separa o bom do ruim, a organização sim. **O 40% é provisório:** a calibração que falta é medir a faixa nas telas que quem decide ou o juiz apontarem como meio vazias e pôr o limiar entre as duas populações. [código] o espaço entre grupos é maior que dentro deles? [código] nenhum texto fica sobreposto a traço ou desenho em `svg` (`conferir_telas.py` da `visual-form`; a linha de um papel pautado não conta: é fundo)? [modelo] o mesmo para texto sobre imagem (foto, desenho em PNG), que o código não mede. A sobreposição só passa **de propósito**, em dois casos: o texto que avança sobre uma imagem, na frente dela, legível pelo D2 e cobrindo uma parte que não carrega informação (o título enorme sobre a foto); e o desenho que marca o texto (riscado, círculo, seta que aponta a palavra), com a classe `intencional` ou o atributo `data-intencional`. A acidental continua barrada. [código] **Texto sobre texto:** qualquer sobreposição é defeito, salvo `data-intencional`; o ruído de medida fica no medidor. [código] **Texto cortado ou passando da borda:** qualquer corte de texto que se lê é defeito, sem tolerância; o sinal gráfico que sangra de propósito (aspas enormes, por exemplo) leva `data-sangria`.
- **D6** [modelo] conta as marcas da lista abaixo que o sistema não justifica. [modelo] autoral ou genérico: a composição é desta série ou serviria a qualquer perfil do tema?
- **D7** [modelo] o desenho diz o mesmo que o texto (a seta aponta no sentido que o texto descreve, o ciclo volta para onde o texto manda)? [modelo] no carrossel (a tela em vídeo dele incluída) e no Story parado, a mistura de estilos é a que o sistema declara? [modelo] cada desenho num estilo só, e os estilos com espírito comum sobre base firme e sem conflito? [modelo] no vídeo (Story em vídeo, Reel, cena; não a tela em vídeo do carrossel), um estilo de desenho só na peça, declarado no roteiro? [pessoa] crédito e direito de uso? Pessoa real: foto real ou ilustração assumida (falha de integridade na rubrica de qualidade).

## Medidas (sempre em código)

| Medida | Valor |
|---|---|
| Contraste do texto corrido, moldura incluída | pelo menos 4,5:1 |
| Contraste de texto grande (52 px ou mais em negrito, ou 66 px ou mais regular, numa tela de 1080: o "texto grande" do WCAG convertido para a escala do celular) | pelo menos 3:1 |
| Margem lateral numa tela de 1080 | pelo menos 80 px |
| Corpo de texto (papéis corpo e destaque) | pelo menos 30 px (o ideal fica em 34 a 42 px; a nota em letra manuscrita, pelo menos 38 px); rótulo pelo menos 28 px; moldura fora (pela conta de 1080 px para a tela de um celular comum, cerca de 2,6 px por ponto; `knowledge/content-design/texto-que-cabe-e-legibilidade.md`) |
| Papéis tipográficos de conteúdo por tela | até 4; o rótulo (anotação de diagrama), a fonte (metadado) e a moldura ficam fora (o AVISO `papeis_por_tela` do `conferir_telas.py`) |
| Cores com função | as do sistema, cada uma com uma só função; a cor computada é igual à declarada (cor anulada pelo CSS é sempre defeito) |
| Alinhamento do título entre telas irmãs | o código acusa acima de 2 px (ruído de render); 12 px já é defeito; acima de 100 px deixa de ser erro e vira escolha, que precisa estar declarada |
| Contraste parcial de texto sobre traço, carimbo ou desenho | p10 (os 10% piores pixels sob o texto) no mínimo do papel do texto (4,5:1 corrido, 3:1 grande); diferença menor que 0,1 é aviso |
| Texto cortado ou sobre outro texto | zero, salvo `data-sangria` e `data-intencional` |
| Onde cada medida roda | nas conferências da forma (`conferir_telas.py` da `visual-form`, que a `slides-export` roda antes de subir): sobreposição de texto com desenho e com texto, contraste inteiro e parcial (contra o fundo sem as linhas do papel e sem as marcas do sistema; degradê e foto de fundo ficam), corte e transbordo (`data-sangria`), alinhamento entre irmãs (só no carrossel; `data-alinhamento`), cor anulada, tela meio vazia, fonte, quebra de linha, dia relativo, hashtags |

Decorativo (número gigante de fundo, textura) fica fora do contraste, desde que não carregue informação. Valores iniciais; a calibração diz se separam o que quem decide aprova do que recusa.

## Marcas de cara de IA

São o padrão da categoria, não proibições: o `design-system.md` da série pode justificar uma por escrito. Fonte: o `craft-floor` do Impeccable e o que juízes de design costumam apontar.

- **Estrutura:** rótulo pequeno em caixa alta acima de todo título; números de seção (01, 02, 03) que não carregam informação; cartões iguais de ícone, título e texto como estrutura da tela; cartão dentro de cartão; o molde do número gigante com rótulo pequeno.
- **Superfície:** texto em degradê; degradê azul e roxo; brilho, halo ou neon; vidro e desfoque como enfeite; borda colorida grossa num lado do cartão; sombra suave em todo cartão; partículas, pontos ou cérebro de luz; microtexto decorativo.
- **Tipografia:** monoespaçada como fantasia de "técnico", fora de código, dado ou medida; quatro ou mais tamanhos sem papel.
- **Cor e tema:** escuro escolhido pela categoria ("tech é escuro"), e não pela cena de uso; mais cores de acento do que funções.
- **Imagem:** foto realista gerada; caricatura gerada sem estilo próprio; mistura de estilos de ilustração que o sistema não declara (sem sistema, a que conflita ou não tem espírito comum; no vídeo, mais de um estilo; D7); emoji no lugar de ícone.

## Severidade e portão

- **P1:** texto essencial ilegível ou abaixo do contraste mínimo, inclusive o p10 de texto essencial sobre traço; texto que se lê cortado pela borda; a tela que justifica salvar está ilegível. Leva a ajustar: refaz-se a tela, que passa de novo pela etapa da forma.
- **P2:** desvio que muda papel, cor ou marca do sistema (a cor anulada pelo CSS entra aqui), marca de cara de IA não justificada, tela meio vazia (o vazio livre que o foco não usa, D5), desenho que contradiz o texto, texto sobre texto sem `data-intencional`, contraste parcial em texto não essencial, título fora do alinhamento das irmãs em mais de 100 px sem declaração, moldura dos Stories fora da área segura (a área segura vive na `rubrica-de-stories.md`). Leva a retocar: corrige-se o trecho e confere-se só ele.
- **P3:** acabamento (alinhamento, inclusive o título fora das irmãs até 100 px; respiro; branco preso entre elementos, D5; marca de ênfase e negrito em trechos diferentes da mesma frase, D4; quebra de linha; um tamanho ou uma posição avulsos dentro do papel certo). Corrige-se antes de exportar, sem nova avaliação. O ERRO e o AVISO do código não são estas prioridades: ERRO é a regra escrita (da casa, dura do sistema ou do Instagram) medida sem erro, que barra o upload; AVISO pede olhar.

O veredito da forma entra no portão da rubrica de qualidade (seção "Como o portão fecha"): P1 ou nota 0 em qualquer critério de design leva a "ajustar" (refazer a tela); P2 leva a "retocar"; P3 não muda o veredito. Forma e mensagem pesam igual, e o veredito é o mais pesado dos dois: quando juízes discordam entre forma e mensagem, o que se ajusta é esta tabela de P1 a P3, não o fecho do portão.

## Quando roda

- **Sistema visual novo ou redesenho:** crítica completa sobre um carrossel-modelo renderizado, com D1 a D7, as marcas de cara de IA e a pergunta "autoral ou genérico?". É aqui que se decide se um padrão entra no sistema.
- **Cada peça:** as medidas em código (o `conferir_telas.py` da `visual-form`; os testes [código] que ainda não têm código ficam com o juiz), e D1, D2, D4, D5 e D7 sobre a imagem renderizada, pelo juiz único na etapa da forma, com D1 a D7 (`portao-de-qualidade.md`).

## Versões

A versão nova registra aqui, numa linha, o que mudou e por quê.

- **1.0:** a primeira versão do repositório.
