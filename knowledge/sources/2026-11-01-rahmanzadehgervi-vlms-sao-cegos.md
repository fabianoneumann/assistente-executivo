---
titulo: "Vision language models are blind: Failing to translate detailed visual features into words"
tipo: paper
autor: "Pooyan Rahmanzadehgervi, Logan Bolton, Mohammad Reza Taesiri, Anh Totti Nguyen"
url: "https://arxiv.org/abs/2407.06581"
publicado_em: 2024-07-09
capturado_em: 2026-11-01
licenca: "CC BY 4.0 (indicada na página do arXiv, link creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering, content-design]
tags: [vlm-perception, low-level-vision, overlap-detection, geometric-primitives, claude-sonnet, benchmark, spatial-precision, diagram-reading, slow-thinking, linear-probing]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 09/07/2024; lida a v6 de 27/03/2025. A página do arXiv não traz comentário de venue; o artigo usa o formato do LNCS (Springer) e o projeto está em VLMsAreBlind.github.io. Autores da Auburn University e da University of Alberta. Texto extraído do PDF da v6 com `pdftotext`; os números da Tabela 1 foram conferidos contra o texto do artigo (média por tarefa e melhores modelos batem). Lido para a rodada investigativa: é a evidência mais direta de que um juiz de visão não vê bem se uma coisa encosta, cruza ou cobre outra.

## 1. A pergunta

Benchmarks de modelos de visão misturam ver com raciocinar e saber; muitas perguntas se respondem sem a imagem. Os autores querem medir só o ver, como um exame de acuidade do oftalmologista: tarefas com formas geométricas simples, sem conhecimento de mundo, fáceis para qualquer pessoa. A hipótese: os modelos fundem a imagem tarde (extraem a representação visual sem saber a pergunta e passam ao modelo de linguagem), e por isso perdem a posição exata quando as formas se cruzam, se encostam ou estão perto.

## 2. As sete tarefas (BlindTest)

1. Quantas vezes duas linhas (gráficos de dois segmentos) se cruzam (0, 1 ou 2).
2. Se dois círculos se sobrepõem ou se tocam.
3. Qual letra de uma palavra está circulada por uma elipse vermelha.
4. Quantos círculos sobrepostos há (como o logo olímpico), e o mesmo com pentágonos.
5. Quantos quadrados aninhados há.
6. Quantas linhas e colunas tem uma grade, vazia ou com texto nas células.
7. Quantos caminhos de uma só cor ligam duas estações num mapa de metrô simplificado.

Imagens sintéticas, com variação de espessura de linha, tamanho, distância e resolução; dois prompts por tarefa; modelos acessados pela API com configuração padrão.

## 3. Resultados (Tabela 1, acerto médio)

- **Média dos quatro modelos nas sete tarefas: 58,07%**, contra 24% do acaso e 100% esperado de pessoas. Por modelo: GPT-4o 50,23%, Gemini-1.5 Pro 58,48%, Claude 3 Sonnet 45,73%, **Claude 3.5 Sonnet 77,84% (o melhor)**.
- **Por tarefa (média dos quatro):** cruzamento de linhas 56,84%; dois círculos 86,70%; letra circulada 79,36%; círculos sobrepostos 39,44%; pentágonos 30,99%; quadrados aninhados 74,99%; linhas e colunas da grade 47,35%; caminhos do metrô 48,90%.
- **Claude 3.5 Sonnet por tarefa:** 75,36% nos cruzamentos, 90,82% nos círculos, 87,88% na letra circulada, 66,46% e 77,71% nas formas sobrepostas, 92,08% nos quadrados, 74,26% na grade e 58,19% no metrô.
- **Distância decide:** o erro cresce quando as formas estão perto; nos cruzamentos, os modelos se confundem mais quando as duas linhas correm próximas. O GPT-4o erra se dois círculos se tocam mesmo com um raio de distância entre eles. Diante da dúvida, os modelos chutam com cara de certeza (o Sonnet 3.5 tende a responder "não" por cautela).
- **Letra circulada:** quando erram, apontam a letra vizinha; o modelo reconhece o círculo e a palavra separados, mas não a relação entre os dois.
- **Grade:** 34,37% de acerto em contar linhas e colunas de grade vazia, muitas vezes errando por uma ou duas; com uma palavra em cada célula, o acerto quase dobra (o modelo lê tabelas de documentos pelo conteúdo, não célula a célula).
- **Metrô:** com um caminho só, o melhor (Sonnet 3.5) acerta 93,33%; com dois, 58,33%; com três, 22,91%.
- **Pensar mais não resolve (Tabela 4):** os modelos com raciocínio longo ficam no máximo empatados com as versões normais (Gemini 2.0 Flash-Thinking 71,59% contra 72,75% do Flash; QVQ 42,48% contra 54,13% do Qwen2-VL).

## 4. O que faz o acerto subir (seção 5)

- **Mais espaço:** com espaços entre as letras, o acerto da letra circulada sobe (Sonnet 3.5 chega a 95%); afastando as formas sobrepostas, o Sonnet 3 sobe 63 pontos na contagem de círculos; com menos curvas no mapa, sobe também. Com bastante espaço entre as formas, vários modelos chegam perto de 100%.
- **A informação está no codificador de imagem:** sondas lineares sobre o codificador de modelos abertos pequenos resolvem os círculos e os cruzamentos com 99,47%; o gargalo é traduzir o que o codificador vê em palavras.
- **Prompt e exemplos:** na tarefa dos dois círculos, o meta-prompt ("descreva a imagem em detalhe antes, depois responda") e dois exemplos no prompt deixaram o Sonnet 3.5 e o GPT-4o iguais ou piores (Sonnet 3.5: 91,66% na base, 90,53% com o meta-prompt, 77,93% com dois exemplos; apêndice D); os autores leem que o modelo entende a pergunta e o limite é ver; pedir ao Sonnet 3.5 para reconstruir a imagem em SVG, HTML ou Python também não preserva o número de cruzamentos nem se os círculos se tocam (apêndice E).
- **Ajuste fino** de um modelo pequeno com até 100 mil exemplos dos dois círculos não generalizou (de 17,1% a no máximo 36,8%).

## 5. Limites (do artigo e da captura)

- Formas geométricas sintéticas em fundo branco, não design; as versões medidas (GPT-4o, Gemini 1.5, Claude 3 e 3.5 Sonnet) são de 2024 e não são as atuais.
- Os autores não fizeram engenharia de prompt pesada, por escolha; os apêndices mostram que as variações testadas mudam pouco.

## 6. Tudo o mais que ensina

- **Desempenho alto em benchmarks de gráfico e documento não garante ver detalhe:** o GPT-4o, melhor que o Gemini em sete benchmarks complexos, é pior aqui.
- **Interfaces de chat pioram:** os autores acharam o Gemini do site e os modelos via Perplexity piores que as APIs, talvez por ajuste e prompts de sistema próprios.
- **Leitura nossa:** "o texto encosta no traço", "a seta aponta para a palavra certa", "o círculo cobre a palavra" e "o desenho tem três caminhos como o texto diz" são, na geometria, as tarefas em que o modelo mais erra: perto, cruzando, cobrindo, contando o que se sobrepõe. É o caso do Jev que falhou a seta sobre a palavra.
