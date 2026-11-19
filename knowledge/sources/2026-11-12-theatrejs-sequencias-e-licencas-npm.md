---
titulo: "Working with Sequences – Theatre.js"
tipo: artigo
autor: "Theatre.js Oy"   # a página não tem assinatura; o rodapé diz '© 2026 Theatre.js Oy – Helsinki', e o campo author dos pacotes do npm diz 'TheaterJS Oy'
url: "https://www.theatrejs.com/docs/0.5/manual/sequences"
publicado_em: 2024-02-01   # "Last edited on February 01, 2024", no pé da página; o HTML não tem meta de data
capturado_em: 2026-11-12
licenca: "protegido (rodapé da página: '© 2026 Theatre.js Oy – Helsinki'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral. Os três JSON do npm são metadados (dados), e as licenças que eles declaram (Apache-2.0 e AGPL-3.0-only) são as do código dos pacotes, não a da página"
areas: [generative-media]
tags: [theatrejs, keyframes, timeline, easing, threejs, react-three-fiber, agplv3, licenses, open-source, video-as-code]
---

# Theatre.js: o editor de sequências do manual 0.5 e as licenças dos pacotes 0.7.2

Nota de fato: tabelas do que a página do manual e os metadados do npm registram, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Quatro textos, todos baixados em 12/11/2026:

- A página principal, o guia "Working with Sequences" do manual da versão 0.5 do Theatre.js, https://www.theatrejs.com/docs/0.5/manual/sequences, baixada em HTML e lida no texto extraído; sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco principal do HTML, não do arquivo); Wayback http://web.archive.org/web/20260124121506/https://www.theatrejs.com/docs/0.5/manual/sequences. Título conferido no `<title>` e no `og:title` do HTML. Lido o texto inteiro do guia, da introdução ao "Learn more", e o pé com a data da última edição; as figuras do guia são vídeos (vistos só pelo rótulo, não assistidos), e nenhum link foi aberto, nem a referência da API de `Sequence` nem o guia do Studio.
- Os metadados de `@theatre/studio` no registro do npm, https://registry.npmjs.org/@theatre/studio/latest; sha256 (hash omitido); sem captura na Wayback.
- Os de `@theatre/core`, https://registry.npmjs.org/@theatre/core/latest; sha256 (hash omitido); Wayback http://web.archive.org/web/20261102110648/https://registry.npmjs.org/@theatre/core/latest.
- Os de `@theatre/r3f`, https://registry.npmjs.org/@theatre/r3f/latest; sha256 (hash omitido); sem captura na Wayback.

Os três JSON foram lidos inteiros. O endereço `/latest` do npm não traz campo de data; a data de cada pacote na tabela abaixo é a conversão (feita aqui) do carimbo em milissegundos do campo `_npmOperationalInternal.tmp`.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (passo de menu, item da API, campo do npm) fica fora. Resultado: 1 de 13 unidades segue a fonte, a segunda frase da recomendação, que junta o intervalo de foco ao controle por código; a maior sequência seguida que segue a fonte tem 1 unidade, e as três citações estão à parte. O `parafrase.py` saiu com o código 3 contra o texto do guia (`theatrejs-sequences.txt`) e contra os JSON de `@theatre/studio` e de `@theatre/core`, e com o código 0 contra o de `@theatre/r3f`, que não tem campo de descrição e por isso não dá língua ao script; nas quatro rodadas, 13 unidades medidas (13 de prosa, 0 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas.

## Em uma frase

Página do manual oficial do Theatre.js (de quem faz a ferramenta) sobre o editor de sequências do Studio, com uma lista curta da API de `Sequence`, mais os metadados de três pacotes do npm; para a base, é a consulta do que o editor faz com as chaves e de qual licença cobre cada pacote.

## O guia, em resumo de fatos

| Item | Fato |
|---|---|
| Página | "Working with Sequences", seção Manual |
| Versão da documentação | 0.5 (no endereço) |
| Última edição | 01/02/2024 |
| Exemplo de código | luz direcional do THREE.js |
| Objeto do Theatre.js no exemplo | `sheet.object('Directional Light', {...})` |
| Prop do exemplo | `intensity: types.number(...)`, com `range: [0, 30]` |
| Ligação com o objeto do THREE.js | `onValuesChange`, que copia o valor |
| Onde se mexe | Studio: Details Panel e Sequence Editor |

## O que o editor faz

| Ação | Como, pela página |
|---|---|
| Pôr uma prop na sequência | botão direito no nome (Details Panel) → "Sequence" |
| Prop composta, de uma vez | "Sequence all" |
| Tirar da sequência | "Make static" / "Make all static" |
| Efeito de tirar | apaga as chaves daquela prop |
| Inserir chave | na linha do tempo (mostrado em vídeo) |
| Apagar chave | botão direito → "Delete" |
| Editar o valor de uma chave | clique esquerdo → editor em janela |
| Editor em janela vale para | todos os tipos de prop |
| Chave agregada | criada sozinha em props compostas e objetos |
| Mover a agregada | move as chaves filhas |
| Apagar ou copiar a agregada | vale para as filhas |
| Conector | a linha entre duas chaves da mesma trilha |
| Copiar e colar chave | "Copy" → agulha → colar na trilha |
| Seleção | Shift + arrastar um retângulo |
| Chaves selecionadas | movem ou somem juntas |
| Curva entre duas chaves | tween editor, ao clicar no conector |
| Funções do tween editor | por nome ("linear", "quad-in-out") ou Bézier cúbica própria |
| Comparação da página | `transition-timing-function` do CSS |
| Várias trilhas à mão | multi-track curve editor (ícone ao lado da trilha) |
| Cor da curva | a do ícone da trilha |
| Tocar e pausar | barra de espaço, com o Studio em foco |

## Intervalo e laço

| Item | Fato |
|---|---|
| Recurso | Focus Range |
| Como criar | Shift + arrastar na barra superior |
| Reprodução dentro dele | em repetição, por padrão |
| Condição | começar a tocar dentro do intervalo |
| Desligar | temporário, ou apagar |
| Intervalo novo | apaga o anterior |
| Laço pela API | `Sequence.play` "with repeats" (sem nome de parâmetro) |

## A API, como a página lista

| Membro | O que a página diz |
|---|---|
| Acesso | `sheet.sequence`, no código |
| Detalhes | "Sequence API Reference" (não aberta) |
| `Sequence.play` | de uma posição, com repetições, numa direção |
| `Sequence.pause` | pausar |
| `Sequence.position` | ler a posição da agulha |
| `Sequence.pointer` | observar dados extras |
| `Sequence.attachAudio` | ligar áudio à sequência |
| Escrever em `position` para pular a um tempo | não está na página |

## Os pacotes no npm (versão `latest`)

| Campo | `@theatre/core` | `@theatre/studio` | `@theatre/r3f` |
|---|---|---|---|
| Versão | 0.7.2 | 0.7.2 | 0.7.2 |
| Licença | Apache-2.0 | AGPL-3.0-only | Apache-2.0 |
| Carimbo da publicação (UTC) | 19/05/2024 14:29:57 | 19/05/2024 14:30:39 | 19/05/2024 14:30:37 |
| Descrição | "Motion design editor for the web" | "Motion design editor for the web" | — |
| Autor | TheaterJS Oy | TheaterJS Oy | Andrew Prifer; Aria Minaei |
| Dependências | `@theatre/dataverse` 0.7.2 | `@theatre/dataverse` 0.7.2 | nenhuma no campo |
| Dependências de par | — | `@theatre/core` (qualquer) | `@theatre/core` e `@theatre/studio` (qualquer) |
| Outras de par | — | — | `react` e `react-dom` ≥ 17.0.2; `three` ≥ 0.155.0; `@react-three/fiber` ^8.13.6 |
| Tamanho descompactado | 903.189 bytes | 22.283.657 bytes | 21.088.920 bytes |
| Repositório | AriaMinaei/theatre, `theatre/core` | AriaMinaei/theatre, `theatre/studio` | AriaMinaei/theatre, `packages/r3f` |
| Commit (`gitHead`) | `2351a2c0` | `2351a2c0` | `2351a2c0` |

## O que a fonte recomenda

A curva de velocidade, pelo manual, sai do tween editor ou das alças do editor de várias trilhas, e o valor de cada chave se ajusta no próprio Studio, depois de a prop entrar na sequência pelo menu. Para trabalhar um pedaço da sequência, ele indica o intervalo de foco, que toca em repetição; o que passar disso, como tocar, pausar e ler a agulha pelo código, fica para a referência da API.

## Citações

- "By default, the playback will play within the focus range on repeat if you start it from within the focus range"
- "Sequence.play: play at a position, with repeats, in direction, etc"
- "Sequence.position: getting the position of the playhead"

## Lacuna

A página só diz que `Sequence.position` lê a posição da agulha; não diz se escrever nela leva a sequência a um tempo, nem dá os nomes dos parâmetros de `play` (intervalo, número de repetições, direção) ou a unidade da posição. Não fala de exportar vídeo ou quadros, de taxa de quadros, nem de como deixar o Studio fora do site publicado; não diz se o manual 0.5 vale para os pacotes 0.7.2, e não trata de licença, que só aparece nos metadados do npm.
