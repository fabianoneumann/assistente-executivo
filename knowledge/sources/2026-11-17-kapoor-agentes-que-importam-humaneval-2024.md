---
titulo: "AI Agents That Matter"
tipo: paper
autor: "Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, Arvind Narayanan"   # cabeçalho do HTML da v1; os dois primeiros com contribuição igual, Princeton (o e-mail do cabeçalho)
url: "https://arxiv.org/abs/2407.01502"
publicado_em: 2024-07-01   # "Submitted on 1 Jul 2024" na página do resumo; lida a v1
capturado_em: 2026-11-17
areas: [agent-engineering]
entrada: pesquisa
tags: [agent-evaluation, humaneval, baselines, retry, inference-cost, reproducibility, ldb, lats, reflexion]
licenca: "arXiv.org perpetual non-exclusive license (nonexclusive-distrib 1.0): o link de licença da página do resumo, conferido em 2026-11-17 na v1 e na versão atual; não permite cópia, e a ficha não leva o integral"
---

# Kapoor e colegas, "AI Agents That Matter": a tabela dos agentes de código no HumanEval

Nota de fato (`knowledge/sources/README.md`, item 2), de cobertura parcial: o paper é longo, e esta ficha registra só a parte que a base usa, as linhas de base simples e a tabela A1 de acerto e custo dos agentes no HumanEval, com os detalhes de implementação do apêndice A.1. O resto do paper (os outros benchmarks, a discussão de avaliação para uso e de reprodutibilidade, as recomendações gerais) não foi fichado. Não há integral: a licença do arXiv escolhida pelos autores não permite cópia. É o paper que o post de 30/04/2024 dos mesmos autores anuncia, com a mesma medição em forma completa ([[2026-11-13-kapoor-narayanan-placares-e-curvas-de-pareto-2024]]).

**Proveniência.** arXiv 2407.01502, v1 de 01/07/2024. A licença foi conferida na página do resumo (https://arxiv.org/abs/2407.01502), em 2026-11-17.

**Conferência lado a lado** (2026-11-17, pela régua do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; as células de fato (número, nome, modelo) ficam fora. Resultado: 4 de 10 unidades seguem uma frase da fonte (as três células de "como funciona" das linhas de base, que condensam cada uma a frase que define a estratégia, e a célula do empate); "O que a fonte recomenda" foi reescrita em 17/11 pela re-revisão, porque traduzia duas frases do paper, uma delas a citação 3, e agora diz a recomendação por outra pergunta (o que fazer na tabela e antes de dar crédito), sem seguir frase da fonte; a maior sequência na ordem da fonte é de 3, as três linhas de base, que são método e seguem a ordem da lista do paper. O `parafrase.py` não rodou com resultado útil: ficha em português, fonte em inglês, e a conta é esta.

## Em uma frase

No HumanEval (164 problemas de programação), cada agente rodou cinco vezes com o acerto e o custo medidos, e três linhas de base simples, que só pedem de novo quando o programa falha nos testes do enunciado, ficaram junto dos agentes mais elaborados, gastando menos.

## As linhas de base

| Linha de base | Como funciona | Modelo na tabela A1 |
|---|---|---|
| Retry | chama o mesmo modelo de novo, até cinco vezes, com a temperatura em zero, enquanto o programa falha nos testes do enunciado | GPT-4 |
| Warming | o retry, com a temperatura subindo a cada tentativa, de 0 a 0,5 (0,3 na segunda e na terceira, 0,5 nas duas últimas) | GPT-4 |
| Escalation | começa num modelo barato e sobe para um mais caro a cada falha (Llama-3 8B, GPT-3.5, Llama-3 70B, GPT-4) | a cadeia de modelos |

| Detalhe (A.1) | Fato |
|---|---|
| Versão do GPT-3.5 | gpt-3.5-turbo-0125 |
| Versão do GPT-4 | gpt-4-turbo-2024-04-09 |
| Medição | abril de 2024 |
| Checagem de robustez | as versões de junho de 2023, com resultado substancialmente igual |

## A tabela A1: acerto e custo no HumanEval

Média de cinco execuções; entre parênteses, o mínimo e o máximo. O asterisco do paper marca as combinações que os autores originais não avaliaram.

| Agente | Acerto médio (mín.–máx.) | Custo total médio, US$ |
|---|---|---|
| LDB (GPT-4)* | 93,3 (92,1–94,5) | 6,36 |
| Warming (GPT-4) | 93,2 (92,1–93,9) | 2,45 |
| LDB (Reflexion, GPT-4)* | 92,9 (91,5–95,1) | 7,26 |
| Retry (GPT-4) | 92,0 (91,4–92,7) | 2,51 |
| LDB (GPT-4, GPT-3.5) | 91,0 (89,0–92,1) | 2,19 |
| GPT-4 sozinho | 89,6 (87,8–90,9) | 1,93 |
| LDB (Reflexion, GPT-3.5) | 88,9 (86,6–91,5) | 4,19 |
| LATS (GPT-4) | 88,0 (82,3–91,5) | 134,50 |
| Reflexion (GPT-4) | 87,8 (86,0–90,9) | 3,90 |
| Escalation | 85,0 (84,1–85,4) | 0,27 |
| LATS (GPT-3.5) | 80,4 (78,7–83,5) | 9,49 |
| LDB (GPT-3.5) | 80,2 (78,7–82,9) | 0,63 |
| GPT-3.5 sozinho | 73,9 (72,0–76,2) | 0,05 |

| Comparação do texto | Fato |
|---|---|
| Warming contra o agente de melhor acerto | sem diferença significativa de acerto |
| O agente de melhor acerto (a maior média da tabela A1) | o LDB com o GPT-4 nos dois papéis, escrevendo e depurando, combinação que o paper original do LDB não testou |
| Custo do Reflexion e do LDB contra o warming | mais de 50% maior |
| Custo do LATS contra o warming | mais de 50 vezes maior |
| De onde vêm esses custos | todo ou quase todo das chamadas ao GPT-4 |

## O que a fonte recomenda

Pôr o gasto em dólar na mesma tabela da taxa de acerto, sempre, para que um ganho comprado com mais chamadas ao modelo apareça como o que é; e só dar crédito a um agente novo depois de pô-lo ao lado das três estratégias simples desta ficha, no mesmo teste.

## Citações

- "There is no significant accuracy difference between our warming strategy and the best-performing agent architecture." (a seção dos resultados no HumanEval)
- "Reflexion and LDB cost over 50% more than the warming strategy, and LATS over 50 times more" (a mesma seção)
- "Accuracy alone cannot identify progress because it can be improved by scientifically meaningless methods such as retrying." (o resumo da seção)

## Lacuna

- A ficha não cobre o resto do paper (os outros benchmarks, a avaliação para uso, a reprodutibilidade).
- A tabela A1 é da v1; as versões seguintes não foram abertas.
- O paper não diz em que problemas o warming e o melhor agente diferem.
