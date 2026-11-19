---
titulo: "LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks"
tipo: paper
autor: "Anna Bavaresco, Raffaella Bernardi, Leonardo Bertolazzi, Desmond Elliott, Raquel Fernández, Albert Gatt, Esam Ghaleb, Mario Giulianelli, Michael Hanna, Alexander Koller, André F. T. Martins, Philipp Mondorf, Vera Neplenbroek, Sandro Pezzelle, Barbara Plank, David Schlangen, Alessandro Suglia, Aditya K Surikuchi, Ece Takmaz, Alberto Testoni"
url: "https://arxiv.org/abs/2406.18403"
publicado_em: 2024-06-26
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, human-agreement, per-dimension-calibration, expert-vs-lay-annotators, factual-consistency, cohens-kappa]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 26/06/2024, v3 (lida) em 02/06/2025. O comentário do arXiv diz "aceito na conferência principal do ACL 2025". Autores em ordem alfabética. Lido em 2026-10-29, na pesquisa da calibração por dimensão do portão.

## A pergunta

Dá para trocar o julgamento humano por um modelo de linguagem na avaliação de texto? Os autores montam o **Judge-Bench**: 20 conjuntos de dados com anotação humana (mais de 70 mil itens), cobrindo propriedades muito diferentes (gramaticalidade, toxicidade, coerência, consistência factual, fluência, engajamento, verbosidade, raciocínio), com texto escrito por gente e texto gerado por máquina, anotado por especialistas ou por leigos. Testam 11 modelos, abertos e fechados, pedindo a cada um que reproduza as anotações.

## Como mediram

- O prompt é a instrução original dada aos anotadores humanos, quando existe, mais "responda com uma das opções, sem explicar".
- Rótulo categórico: kappa de Cohen contra os humanos. Nota graduada: correlação de Spearman.
- Resposta inválida do modelo (recusa, explicação no lugar da nota) é trocada por um rótulo sorteado da distribuição humana.
- **Teto humano:** quando há vários anotadores por item, a concordância de um anotador sorteado com a agregação dos outros dá o limite superior.
- Cadeia de raciocínio, exemplos no prompt e paráfrases do prompt foram testados no apêndice e não melhoram de forma sistemática.

## Resultados

- **A concordância varia com a propriedade julgada, não só com o modelo.** Kappa médio nas anotações categóricas de 0,28 (GPT-4o e Llama-3.1-70B) a 0,10 (Command R+); Spearman médio nas graduadas de 0,50 (GPT-4o) a 0,30.
- **Alto onde há resposta checável ou instrução clara:** seguir instrução (LLMBar natural, GPT-4o 0,84), raciocínio matemático (ROSCOE-GSM8K, Spearman 0,79 a 0,83), **consistência factual de resumo** (QAGS, GPT-4o 0,72 com teto humano de 0,74).
- **Baixo ou negativo em julgamento subjetivo ou sensível:** engajamento "consistentemente baixo" em todos os modelos; toxicidade e segurança de −0,24 a 0,01 (DICES, Medical-safety), em parte por causa das travas de segurança, com muitos modelos explicando em vez de julgar.
- **Nenhum modelo é o melhor em todas as propriedades.** Os fechados lideram em aceitabilidade e verbosidade; os Mixtral, em coerência e consistência. Os autores questionam a prática de usar um único modelo para julgar todas as dimensões.
- **Especialista contra leigo:** nas notas graduadas, todos os modelos correlacionam mais com anotadores leigos do que com especialistas. A hipótese dos autores, que eles mesmos chamam de especulativa: o leigo lê pela superfície, como o modelo; o especialista aplica critério de domínio mais estrito.
- **Texto humano contra texto de máquina:** todos os modelos concordam mais com os humanos quando julgam texto escrito por gente do que texto gerado, compatível com viés a favor da própria geração.
- Fora poucos conjuntos (QAGS, receitas, NewsRoom), os modelos ficam bem abaixo do teto humano, e a variação não se explica só pela dificuldade da tarefa.

## A recomendação

Validar e calibrar o juiz contra julgamento humano **da própria tarefa** antes de usá-lo como avaliador.

## Limites declarados

- Correlação com humanos pode não ser a melhor validação: humanos e modelo podem concordar por terem os mesmos vieses, e às vezes é preciso validar os anotadores também.
- Usa conjuntos de dados existentes sem reavaliar a qualidade deles, com risco de vazamento para o treino dos modelos.
- Não cobre comparação em pares (cita o JudgeBench para isso).
- Quase só inglês.

---
