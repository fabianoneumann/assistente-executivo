---
titulo: "The Geometry of LLM-as-Judge: Why Inter-LLM Consensus Is Not Human Alignment"
tipo: paper
autor: "Sourabrata Mukherjee, Hamna Hamna, Kalika Bali, Sunayana Sitaram"
url: "https://arxiv.org/abs/2606.03043"
publicado_em: 2026-06-02
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, inter-judge-agreement, human-agreement, subjective-vs-verifiable, judge-ensembles, human-ceiling]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 02/06/2026, v2 (lida) em 02/09/2026. O comentário do arXiv diz "aceito no EMNLP 2026". Microsoft Research. O arXiv não tem versão HTML deste artigo; o integral foi extraído do PDF. Lido em 2026-10-29, na pesquisa da calibração por dimensão do portão.

## A pergunta

Juízes LLM concordam muito entre si e pouco com pessoas, um padrão que se repete nas meta-avaliações. A concordância entre juízes costuma ser lida como licença para confiar neles. Mas ela tem duas leituras que produzem os mesmos números: os juízes concordam porque captam a qualidade, ou porque **compartilham o mesmo ponto cego**. No segundo caso, juntar mais juízes amplia o erro justamente onde o julgamento humano é mais escasso. Os autores propõem um teste que separa as duas leituras.

## O teste

Tratar as notas de cada juiz como um vetor e medir a forma da discordância, não só o tamanho: dispersão das notas, número efetivo de direções, e o **ângulo** entre o vetor do juiz e o dos humanos. Sempre com três medidas juntas: juiz contra juiz, juiz contra humano e humano contra humano.

**Comparação justa:** um juiz comparado com a média de vários anotadores tem um alvo mais fácil que um anotador comparado com um colega; a diferença vale vários graus. Por isso, toda comparação deixa um anotador de fora e mede ele e o juiz contra a média dos outros dois. Sem isso, numa das rubricas, a correlação do juiz subia de 0,418 para 0,519 e o punha acima do piso humano.

## Dados

170.890 chamadas de juiz, 42 juízes (15 modelos base e 27 variantes ajustadas, com exemplos ou calibradas), dois conjuntos indianos construídos por comunidades: perguntas de saúde em hindi, canarês e malaiala, e perguntas do dia a dia (saúde, finanças, cotidiano) em oito línguas indianas com três anotadores independentes por item.

## Resultados

- **Nas rubricas subjetivas, consenso sem alinhamento.** Na pergunta do dia a dia, os juízes concordam entre si tanto quanto os humanos entre si (aceitabilidade linguística: 0,356 contra 0,357; alucinação: 0,349 contra 0,364) e concordam com os humanos bem menos (0,207 e 0,239): **58% e 66% do nível entre humanos**. Na saúde, juiz contra juiz dá kappa de 0,445 nas comparações e juiz contra humano, 0,128, 3,5 vezes menos.
- **Na rubrica verificável, a distância quase fecha.** Na qualidade da tarefa (restrições checáveis), com os mesmos itens, juízes e humanos, a concordância juiz-humano chega a 0,418, **88%** do nível entre humanos (0,474). O melhor juiz sozinho fica dentro do piso humano; nas subjetivas, nem o melhor chega.
- **Juntar juízes não resolve:** o conjunto converge para o eixo comum dos juízes, não para o humano; mesmo um conjunto ilimitado dos juízes testados fica fora do piso humano nas subjetivas.
- **A dispersão das notas humanas indica o regime antes de rodar qualquer juiz:** uma medida calculada só dos três anotadores separa as rubricas objetivas das subjetivas.
- **Treinar aumenta a dispersão das notas, mas não gira o eixo:** ajuste fino e otimização de preferência abrem as notas, e o ângulo para os humanos quase não se move. O que mais ajudou foi ancorar o juiz em **exemplos avaliados por humanos no momento do julgamento**; reescalar as notas depois, sobre âncoras humanas, não reproduz o ganho (e, com menos de cerca de 40 âncoras, o intervalo desse reescalonamento cruza o zero). Os estágios com exemplos rodaram só num modelo (sarvam-m).
- Preferência pela própria família de modelo não explica o efeito.

## O protocolo que propõem (antes de confiar)

1. Testar dispersão, número de direções e ângulo contra o acaso, reportando as três concordâncias juntas.
2. Deixar cada anotador de fora para montar o piso que o juiz precisa alcançar.
3. Confiar num conjunto de juízes só se o eixo comum passar no teste.
4. Se falhar, ancorar em exemplos avaliados por humanos, não somar mais juízes.

"O consenso mostra que os juízes compartilham um eixo; a geometria mostra se é o humano."

## Limites declarados

Diagnóstico sobre as notas, não afirmação sobre o que acontece dentro do modelo; o regime objetivo se apoia numa única rubrica verificável; no conjunto de saúde não há identificação por anotador, então não há piso humano ali; o tamanho do efeito variou muito por língua e quase sumiu no télugo; juízes fechados mudam sem aviso.

---
