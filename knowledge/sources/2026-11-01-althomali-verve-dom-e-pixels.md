---
titulo: "Automated visual classification of DOM-based presentation failure reports for responsive web pages"
tipo: paper
autor: "Ibrahim Althomali, Gregory M. Kapfhammer, Phil McMinn"
url: "https://doi.org/10.1002/stvr.1756"
publicado_em: 2021-06-01
capturado_em: 2026-11-01
licenca: "CC BY (a primeira página do PDF diz 'This is an open access article under the terms of the Creative Commons Attribution License'; a página do White Rose Research Online indica CC BY); o integral lido vem da versão publicada depositada em https://eprints.whiterose.ac.uk/id/eprint/165542/"
areas: [agent-engineering]
tags: [visual-testing, dom-analysis, layout-failures, false-positives, overlap-detection, screenshot-analysis, opacity-layers, web-testing, human-agreement, two-stage-check]
---

Ficha em palavras próprias; o texto integral (licença CC BY) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Artigo de periódico: Software Testing, Verification and Reliability, vol. 31, n. 4, e1756 (2021), número especial; versão estendida do artigo do ICST 2019 que apresentou o VISER (o primeiro autor e o McMinn receberam por ele um prêmio de artigo destacado do IEEE). Recebido em 11/11/2019, aceito em 23/08/2020; `publicado_em` é o ano e o número do periódico, sem o dia exato. Autores da Universidade de Sheffield e do Allegheny College. Texto extraído do PDF publicado (51 páginas) com `pdftotext`; a Tabela III lida na extração com layout. Lido para a rodada investigativa (o que se mede no código e o que só na imagem) e pela ligação direta com a a pesquisa (sobreposição de texto conferida em código).

## 1. A pergunta

Ferramentas que testam o layout de páginas responsivas, como o ReDeCheck, leem o DOM (a árvore de elementos com as caixas calculadas pelo navegador) e apontam falhas de layout em larguras de tela específicas. Como trabalham no DOM, apontam também o que **ninguém vê**: duas caixas que se cruzam com fundo transparente, um elemento que "sai" do contêiner sem nada pintado. Os autores dizem que é limitação fundamental de toda ferramenta baseada no DOM, não só do ReDeCheck. Hoje o desenvolvedor confere à mão cada relato e o classifica como verdadeiro positivo (visível), falso positivo (não existe nem no DOM) ou problema não observável (existe no DOM, não se vê). A proposta: automatizar essa classificação olhando a página renderizada.

## 2. Os cinco tipos de falha que o DOM aponta

- **Colisão de elementos:** com a tela estreitando, dois elementos passam a se sobrepor.
- **Protrusão de elemento:** um elemento sai do seu contêiner.
- **Protrusão da tela:** um elemento sai do corpo da página (estoura a largura).
- **Quebra (wrapping):** um elemento que estava em linha desce para a linha de baixo, fora do alinhamento.
- **Faixa estreita:** um layout diferente que aparece só num intervalo pequeno de larguras (menos de 15).

## 3. O método: filtro no DOM, confirmação nos pixels

- **Filtro no DOM:** confere se as coordenadas realmente se cruzam (colisão) ou se a protrusão tem largura e altura diferentes de zero; se não, é falso positivo e para aí.
- **Área de interesse:** o retângulo da página onde o elemento suspeito pode ter pintado sobre outro ou fora do lugar, definido por tipo de falha e por cenário (os dois elementos aninhados, encostados ou separados).
- **Camadas por opacidade:** o VERVE tira uma foto da área de interesse, zera a opacidade do elemento de cima, tira outra, e assim até o fundo. Se as fotos diferem, a falha é visível (verdadeiro positivo); se não, é não observável. Opacidade e não remoção, porque remover um elemento muda o layout dos outros; com opacidade zero ele continua ocupando o lugar. O método independe do navegador.
- **Quebra:** a mesma manipulação de opacidade, estendida.
- **Faixa estreita:** compara os histogramas de cor da página na largura suspeita com as larguras logo antes e logo depois (seis medidas de distância do OpenCV testadas).

## 4. Resultados

- **Quanto do que o DOM aponta se vê (classificação manual, Tabela III, 25 páginas, 326 relatos):** colisão, 7 visíveis e 24 não observáveis; protrusão de elemento, 3 visíveis e 36 não observáveis; protrusão da tela, 24 visíveis e 23 não observáveis; quebra, 10 visíveis e 4 falsos positivos; faixa estreita, 152 visíveis e 43 falsos positivos. Nas 20 páginas novas (143 relatos), o padrão das colisões se repete: 2 visíveis e 10 não observáveis.
- **Concordância do VERVE com a classificação manual:** nas 25 páginas antigas, 86,3% em colisão e protrusões, 78,6% em quebra e 98,5% em faixa estreita; nas 20 novas, 91,8%, 64,7% e 73,6%. Cerca de 4 segundos por relato, em 469 relatos.
- **Onde discordam, e quem tinha razão:** três protrusões que a pessoa chamou de não observáveis eram falsos positivos (não havia protrusão no DOM; erro de coleta do ReDeCheck); duas diferenças de 2 px que o VERVE chamou de visíveis a pessoa chamou de não observáveis ("tecnicamente verdadeiros positivos, quase imperceptíveis"); duas falhas visíveis o VERVE perdeu porque o ReDeCheck não apontou os elementos mais específicos; um transbordo da tela que obrigava a rolar de lado o VERVE chamou de não observável, porque nada foi pintado por cima, mas a pessoa viu o efeito colateral (rolagem e desalinhamento com o cabeçalho).
- **Ponto de inspeção:** analisar na menor largura da faixa relatada concorda mais com a pessoa; no meio da faixa, algumas falhas deixam de ser visíveis.

## 5. Conclusões dos autores

A classificação pelo VERVE é menos subjetiva e menos sujeita a erro que a manual e serve de companheira das ferramentas de DOM: o DOM aponta o suspeito, a imagem confirma se ele aparece. Trabalho futuro: efeitos visíveis que não são pintura sobreposta (rolagem, desalinhamento com o resto da página).

## 6. Tudo o mais que ensina

- **Três categorias, não duas:** "não observável" é diferente de "falso positivo": o defeito latente existe e pode aparecer em outro contexto, mas não é prioridade. Leitura nossa: para a peça renderizada uma vez num tamanho fixo, o não observável é ruído do portão.
- **Diferença mínima:** o desacordo nos 2 px mostra que "visível" tem limiar; uma régua precisa dizer a partir de quanto conta.
- **A pessoa também erra:** parte do desacordo foi erro da classificação manual, achado pelo método automático; os autores usam isso como argumento de que o processo manual é subjetivo.
- **Trabalhos relacionados citados:** ReDeCheck (Walsh, Kapfhammer e McMinn), VFDetector, X-PERT e ferramentas de comparação entre navegadores, testes de regressão visual.
