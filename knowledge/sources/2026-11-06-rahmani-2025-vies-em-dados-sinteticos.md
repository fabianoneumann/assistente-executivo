---
titulo: "Towards Understanding Bias in Synthetic Data for Evaluation"
tipo: paper
autor: "Hossein A. Rahmani, Varsha Ramineni, Emine Yilmaz, Nick Craswell, Bhaskar Mitra"
url: "https://arxiv.org/abs/2506.10301"
publicado_em: 2025-10-04
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [synthetic-data, test-collections, information-retrieval, relevance-judgments, llm-as-judge, evaluation-bias, kendall-tau, mixed-effects-model, trec]
licenca: "CC BY 4.0, em arxiv.org/abs/2506.10301"
---

# Rahmani e outros 2025 (CIKM '25): o viés de avaliar sistemas de busca com coleção de teste sintética

Ficha em palavras próprias; o integral não vem neste repositório e se lê na url do frontmatter. Artigo curto de 5 páginas nos anais do CIKM '25 (Seul, 10 a 14/11/2025), DOI 10.1145/3746252.3760908, versão 2 no arXiv de 4/10/2025. Autores da University College London, do The Alan Turing Institute e da Microsoft. Área: recuperação de informação (IR). Código e dados em `github.com/rahmanidashti/BiasSyntheticData`.

## A pergunta

Uma coleção de teste de IR tem consultas e julgamentos de relevância feitos por pessoas, o que é caro. Trabalho anterior com parte dos mesmos autores mostrou que coleções sintéticas têm potencial para avaliar sistemas. Aqui se pergunta o que muda quando o LLM (modelo de linguagem grande) gera as consultas, os rótulos ou ambos: que vieses aparecem e que efeito têm na avaliação.

## Dados

TREC DL 2023, tarefa de ranqueamento de passagens, que os autores dizem ser, até onde sabem, a única coleção com consultas humanas e sintéticas e com julgamentos de especialista humano e de LLM. São 82 consultas: 51 humanas, 18 geradas pelo GPT-4 e 13 geradas pelo T5. Julgamentos em escala de 4 pontos: 1.830 perfeitamente relevantes (3), 2.259 muito relevantes (2), 4.372 relacionados (1), 13.866 irrelevantes.

## Consultas humanas contra sintéticas

- **Comprimento:** as reais têm menos palavras (Figura 1a, sem números no texto). Os autores atribuem a pessoa querer digitar menos ou esperar que a busca lide com pergunta incompleta.
- **Palavras frequentes (Tabela 1):**

| Palavra | Reais: contagem, %, posto | Sintéticas: contagem, %, posto |
|---|---|---|
| what | 21, 7,14%, 1 | 10, 3,75%, 2 |
| is | 14, 4,76%, 2 | 6, 2,25%, 7 |
| how | 13, 4,42%, 3 | 3, 1,12%, 12 |
| of | 9, 3,06%, 4 | 7, 2,62%, 4 |
| in | 8, 2,72%, 5 | 7, 2,62%, 3 |
| to | 8, 2,72%, 6 | 3, 1,12%, 13 |
| a | 7, 2,38%, 7 | 6, 2,25%, 8 |
| the | 7, 2,38%, 8 | 15, 5,62%, 1 |
| does | 4, 1,36%, 9 | 6, 2,25%, 6 |
| did | 4, 1,36%, 10 | 0, 0%, sem posto |

- **Leitura deles:** gente real prefere perguntas diretas e factuais, o que o modelo talvez não replique por inteiro; mesmo assim os dois conjuntos têm distribuição equilibrada dos termos comuns, e as sintéticas captam parte do que as reais têm. O texto diz "começar com what" e dá 7,4% contra 3,75%; a tabela dá 7,14% em frequência.

## Rótulos humanos contra rótulos do GPT-4

- **Bland-Altman (Figura 1b):** viés anotado de cerca de 0,28, com o LLM em média dando notas um pouco mais altas. Limites de concordância de 95% de cerca de -2,1 a 1,62, faixa que os autores chamam de larga: muitas vezes perto do humano, às vezes bem longe. O texto chama o viés de "small negative" e ao mesmo tempo descreve o LLM como mais leniente; a ficha registra as duas coisas como estão.
- **Distribuição (Figura 2, sem números no texto):** nos três tipos de consulta, as pessoas dão mais rótulo 0; o GPT-4 dá mais rótulo 1, o que os autores leem como tendência a ver alguma relevância em caso limítrofe. O efeito é mais evidente nas consultas do T5. Rótulos 2 e 3 são raros e as diferenças são menores e variadas: GPT-4 um pouco mais em 2, um pouco menos em 3.
- **Divergência de Kullback-Leibler (KL) entre as distribuições do GPT-4 e humana:** 0,0186 em todos os tipos de consulta; 0,0328 nas humanas; 0,0335 nas do GPT-4; 0,0509 nas do T5. Os autores leem como alinhamento próximo, um pouco pior no T5.

## Ordem dos sistemas (Figura 3)

Os sistemas do TREC DL 2023 foram classificados em quatro grupos pelos metadados do SynDL: GPT, T5, GPT + T5, e outros (BM25 ou modelo sem GPT nem T5). O eixo x é sempre consulta real com rótulo humano.

| Configuração no eixo y | Kendall, NDCG@10 | Kendall, MAP |
|---|---|---|
| Consultas sintéticas, rótulos humanos | 0,8487 | 0,8343 |
| Consultas reais, rótulos do GPT-4 | 0,9151 | 0,7267 |
| Consultas do GPT-4, rótulos humanos | 0,8175 | 0,8552 |
| Consultas do T5, rótulos humanos | 0,8723 | 0,7368 |

NDCG é ganho cumulativo descontado normalizado e MAP é precisão média média, duas medidas de qualidade de ranqueamento. Os autores chamam as correlações de moderadas a altas e dizem que arranjos híbridos como GPT + T5 mostram melhor alinhamento com a avaliação humana.

- **Nota mais alta no sintético:** em todos os tipos de sistema, o desempenho tende a ser maior nas consultas sintéticas que nas reais, de modo que coleções sintéticas, do GPT-4 ou do T5, "may be easier and thus overestimate system effectiveness". Com rótulos sintéticos sobre consultas reais (Figuras 3b e 3f), quase todos os tipos sobem, o que chamam de visão otimista demais.
- **Favorecimento do parente:** os sistemas só com GPT costumam ficar acima da diagonal, e sistemas baseados em GPT-4 saem favorecidos em consultas ou rótulos do GPT-4 (Figuras 3c e 3g).
- **Ressalva:** "these findings are based on a single test collection"; pedem mais experimentos, em outros domínios e com outros prompts.

## Modelo linear misto (Tabela 2)

**Método:** um modelo por medida, NDCG e MAP, com 5.740 observações, em que cada observação é uma consulta dentro de uma rodada de sistema. Variáveis: se o juiz é o GPT-4 (referência: juiz humano), tipo de sistema (referência: tradicional), dificuldade da consulta (QDR), comprimento da consulta em palavras (QW), comprimento médio do documento (DL), se a consulta veio do GPT-4 e número de modelos na cadeia do sistema (MN), com a interação do juiz GPT-4 com cada uma, e intercepto aleatório por rodada.

| Variável | MAP: coef., erro, p | NDCG: coef., erro, p |
|---|---|---|
| Intercepto | 0,121, 0,016, 0,000 | 0,412, 0,030, 0,000 |
| Julgado pelo GPT-4 | 0,069, 0,016, 0,000 | 0,207, 0,021, 0,000 |
| Sistema GPT | -0,051, 0,019, 0,008 | -0,076, 0,039, 0,054 |
| Sistema T5 | -0,001, 0,023, 0,964 | 0,034, 0,047, 0,466 |
| Sistema T5+GPT | 0,092, 0,018, 0,000 | 0,166, 0,036, 0,000 |
| Dificuldade da consulta | -0,014, 0,002, 0,000 | 0,033, 0,003, 0,000 |
| Comprimento da consulta | 0,001, 0,001, 0,376 | -0,004, 0,002, 0,021 |
| Comprimento do documento | 0,000, 0,000, 0,000 | -0,000, 0,000, 0,482 |
| Consulta do GPT-4 | 0,030, 0,010, 0,002 | 0,059, 0,013, 0,000 |
| MN | 0,016, 0,004, 0,000 | 0,019, 0,008, 0,016 |
| GPT-4 × sistema GPT | 0,032, 0,012, 0,006 | 0,018, 0,016, 0,254 |
| GPT-4 × sistema T5 | -0,001, 0,014, 0,927 | 0,008, 0,019, 0,688 |
| GPT-4 × sistema T5+GPT | -0,027, 0,011, 0,014 | 0,003, 0,015, 0,827 |
| GPT-4 × dificuldade | 0,001, 0,003, 0,653 | -0,009, 0,004, 0,049 |
| GPT-4 × comprimento da consulta | -0,011, 0,002, 0,000 | 0,006, 0,003, 0,027 |
| GPT-4 × comprimento do documento | 0,000, 0,000, 0,000 | -0,000, 0,000, 0,000 |
| GPT-4 × consulta do GPT-4 | 0,026, 0,013, 0,049 | -0,040, 0,018, 0,030 |
| GPT-4 × MN | 0,001, 0,002, 0,732 | 0,000, 0,003, 0,952 |

**O que os autores leem:**

- Os sistemas recebem notas significativamente maiores quando o GPT-4 julga: β = 0,069 em MAP e β = 0,207 em NDCG, ambos p < 0,001. Chamam de viés positivo geral.
- Preferência pequena mas mensurável pelo parecido consigo: MAP maior para sistema baseado em GPT-4 (β = 0,032, p = 0,006), e leve penalidade para os híbridos T5 + GPT (β = -0,027, p = 0,014). Em NDCG essas duas interações não são significativas.
- As interações mudam com a medida: consultas mais longas baixam um pouco o MAP (-0,011, p < 0,001) e sobem um pouco o NDCG (0,006, p = 0,027); consultas do próprio GPT-4 sobem o MAP (0,026, p = 0,049) e baixam o NDCG (-0,040, p = 0,030).

## Conclusão dos autores

- LLMs produzem consultas mais longas e dão notas de relevância mais altas.
- Sistemas baseados em LLM saem superestimados em coleções sintéticas, sobretudo com rótulos sintéticos.
- O efeito do viés pode ser significativo em medida absoluta, enquanto "its effect may not be as significant in comparing relative system performance" (resumo).
- Pedem supervisão humana ao usar LLM para gerar julgamento.

## Tudo o mais que ensina

- **Dois pontos de entrada do sintético:** consulta e rótulo são separáveis, e a tabela de Kendall mostra que a mesma troca rende valores diferentes em NDCG e MAP: rótulos do GPT-4 têm o maior valor em NDCG e o menor em MAP.
- **Gráfico de Bland-Altman:** olha a concordância entre dois avaliadores pela diferença contra a média das notas, com o viés médio e os limites de concordância.
- **As duas medidas de rótulo no mesmo trabalho:** divergência pequena entre as distribuições (KL) e coeficiente significativo a favor de notas maiores com o GPT-4.
- **Motivação de risco:** os autores citam coleções sintéticas usadas para avaliar sistemas que depois vão a aplicações de alto risco ou voltadas ao usuário.
- **Declaração de uso de IA:** o ChatGPT parafraseou um texto inicial dos autores, com edições posteriores deles.
- **Financiamento:** Engineering and Physical Sciences Research Council e programa Enrichment do The Alan Turing Institute.
