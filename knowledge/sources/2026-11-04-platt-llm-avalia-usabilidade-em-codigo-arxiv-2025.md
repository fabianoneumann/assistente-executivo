---
titulo: "Catching UX Flaws in Code: Leveraging LLMs to Identify Usability Flaws at the Development Stage (Platt, Luchs e Nizamani, 2025)"
tipo: paper
autor: "Nolan Platt, Ethan Luchs, Sehrish Nizamani (Virginia Tech)"
url: "https://arxiv.org/abs/2512.04262"
publicado_em: 2025-12-03  # arXiv:2512.04262v1 [cs.SE], 3 de dezembro de 2025; texto lido na versão HTML v1
capturado_em: 2026-11-04
areas: [agent-engineering]
tags: [llm-as-judge, severity-rating, inter-rater-reliability, heuristic-evaluation, krippendorff-alpha, cohens-kappa, self-consistency]
licenca: "CC BY 4.0, indicada na página HTML do arXiv (arxiv.org/html/2512.04262v1, 'License: CC BY 4.0'); o integral está na url"
---

# Platt, Luchs e Nizamani (2025): consistência do GPT-4o ao avaliar usabilidade em código

Ficha em palavras próprias, lida na versão HTML v1 do arXiv em 2026-11-04. O integral não vem neste repositório e se lê na url do frontmatter (licença CC BY 4.0, conferida na página). **Atenção ao resumo do artigo:** a frase do resumo que fala do alfa de Krippendorff está na frase da gravidade ("Severity judgments showed more variability: weighted Cohen's Kappa averaged 0.63, but exact agreement was just 56%, and Krippendorff's Alpha was near zero"), mas no corpo o alfa (Tabela III) foi calculado sobre a presença do problema, não sobre a nota de gravidade. Não há alfa de gravidade no corpo.

## O que o estudo faz

- Pergunta: um LLM consegue dar avaliações heurísticas consistentes na fase de desenvolvimento, lendo só o código-fonte de um site?
- Modelo: GPT-4o, numa versão personalizada do ChatGPT (um "GPT" com instruções fixas), sem ajuste fino. O prompt manda o modelo agir como especialista em usabilidade por análise de código, avaliar as 10 heurísticas de Nielsen e devolver, só em JSON, para cada uma: nota de gravidade de 0 a 4, se achou problema (verdadeiro/falso), descrição, referência e trecho de código, respostas de avaliação e recomendação. Sem problema, a nota tem de ser 0. O texto do prompt está no Apêndice A.
- Material: 30 repositórios públicos do GitHub, com licença permissiva, aplicações de front-end em fase inicial (HTML, CSS e JavaScript apenas). Cada site foi avaliado 3 vezes, em sessões novas e independentes (o arquivo ZIP do código é enviado em cada sessão), e cada sessão é tratada como um avaliador. Total esperado: 900 avaliações heurísticas (30 sites x 10 heurísticas x 3 sessões); 15 foram descartadas por nota ausente ou mal formada, ficando 885 notas de gravidade.
- Metodologia inicial que falhou: com um prompt igual e solto, o GPT-4o preenchia mal o modelo, repetia a mesma heurística dezenas de vezes e comportava-se de modo inconsistente para perguntas semanticamente idênticas em sessões diferentes (nas palavras dos autores); isso levou ao GPT personalizado com saída JSON.
- Dados e código: repositório no GitHub (nolanplatt/LLMUsabilityEvaluations) e arquivo no Figshare.

## Resultados

**Detecção.** A grande maioria das avaliações marcou pelo menos uma falha (o texto não dá o percentual), o que os autores ligam à natureza do conjunto (projetos iniciais ou de demonstração) e leem como tendência a sinalizar algo quase sempre.

**Distribuição das 885 notas de gravidade (Tabela I):** 0 sem problema: 164; 1 cosmético: 251; 2 menor: 306; 3 maior: 155; 4 catástrofe: 9.

**Concordância sobre a presença do problema (Tabela II, kappa de Cohen sem peso, 300 pares por comparação):** sessões 1-2: 0,471 (247/300, 82,3%); 1-3: 0,530 (255/300, 85,0%); 2-3: 0,502 (254/300, 84,7%). Os autores leem a faixa de 0,47 a 0,53 como confiabilidade moderada.

**Medidas de vários avaliadores (Tabela III, sobre a presença do problema):** alfa de Krippendorff = -0,000234; kappa de Fleiss = 0,500. Os autores dizem que o alfa levemente negativo não é erro de cálculo e explicam que a métrica é conservadora diante de desbalanceamento de classes e de pequenas diferenças entre as sessões (explicação deles; o artigo não a testa).

**Concordância sobre a gravidade (Tabela IV, kappa ponderado):** 1-2: 0,625 (169/300 iguais, 56,3%); 1-3: 0,668 (171/300, 57%); 2-3: 0,597 (167/300, 55,6%). Na comparação 1-2, a maioria dos sites teve kappa de 0,6 ou mais, com alguns baixos ou negativos (a figura 2 mostra a distribuição por site), o que o texto atribui a taxas de detecção desbalanceadas entre as duas sessões.

**Por heurística (presença do problema, Apêndice D):** maior concordância em Prevenção de erros (kappa 0,42 a 0,55, média 0,47) e em Compatibilidade entre o sistema e o mundo real (0,27 a 0,57, média 0,40); menor em Ajuda e documentação (-0,07 a 0,19, média 0,08) e em Consistência e padrões (-0,03 a 0,30, média 0,08).

## O que os autores concluem

- O modelo é consistente consigo mesmo, sobretudo em dizer se há problema; a gravidade varia mais, o que eles consideram esperado por ser ordinal.
- Eles apontam que isso é consistência interna e "não implica correção"; as notas deveriam guiar, não substituir, o julgamento de especialistas, e sugerem comparar a saída do modelo com a de especialistas em trabalhos futuros. Dizem que a variação entre humanos em gravidade também é conhecida (citam Rubin e Chisnell) e que a consistência observada sugere abordagem comparável, mas o estudo não mede avaliadores humanos.
- Trabalho futuro: comparar com avaliações humanas, melhorar a robustez do prompt, ajuste fino por domínio.

## O que a fonte não diz

Não compara com especialistas humanos nem verifica se as falhas apontadas existem de fato no código; só mede concordância entre três sessões do mesmo modelo. Não calcula alfa de Krippendorff para a gravidade. Não informa a versão exata do GPT-4o nem parâmetros como temperatura. Não dá o percentual de avaliações que marcaram problema.

---
