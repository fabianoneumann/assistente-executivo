---
titulo: "Efficacy of Synthetic Data as a Benchmark"
tipo: paper
autor: "Gaurav Maheshwari, Dmitry Ivanov, Kevin El Haddad"
url: "https://arxiv.org/abs/2409.11968"
publicado_em: 2024-09-18
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [synthetic-data, benchmark, zero-shot, absolute-vs-relative-performance, mspd, spearman-correlation, bias-factor, intent-detection, named-entity-recognition, text-similarity]
licenca: "CC BY-NC-ND 4.0, em arxiv.org/abs/2409.11968; pela cláusula NC (decisão de 2026-11-01) entra só a ficha, e o integral está na url"
---

# Maheshwari, Ivanov e El Haddad 2024 (arXiv): dado sintético serve de benchmark?

Ficha em palavras próprias (licença com NC e ND: o integral não entra; está na url). Preprint no arXiv, cs.CL, versão 1 de 18/9/2024, de autores da empresa Diabolocom e do ISIA Lab da Universidade de Mons. Área: processamento de linguagem natural com modelos de linguagem grandes (LLM). O código e os prompts estão no repositório do GitHub `Diabolocom-Research/SG4NLP`, citado no artigo.

## A pergunta

Quem não tem dado de teste real, por custo ou privacidade, consegue escolher o melhor LLM para uma tarefa testando em dado gerado por outro LLM? Os trabalhos anteriores, dizem os autores, combinavam sintético e real para melhorar resultado; aqui se mede até onde o sintético prevê o desempenho zero-shot (sem exemplos no prompt) dos LLMs. Duas perguntas: o sintético representa o real, e há viés quando o mesmo LLM gera o dado e resolve a tarefa?

## Método, passo a passo

1. **Tarefas e conjuntos:** seis conjuntos reais em três tarefas. Detecção de intenção: SNIPS (7 intenções) e ATIS (Airline Travel Information System, transcrições sobre voos, 17 intenções). Reconhecimento de entidades nomeadas (NER): duas variantes do Cross-NER, Literature e Politics. Similaridade de texto: SemEval 2012, Headlines (pares de manchetes) e Tweets-News. De cada conjunto, 200 exemplos para teste. O artigo não diz o tamanho de cada conjunto sintético.
2. **Modelos:** seis LLMs de três famílias, que fazem dois papéis, gerar dado e resolver a tarefa: GPT-4o e GPT-4o-mini; Mixtral-8x22B-Instruct-v0.1 e Mixtral-8x7B-Instruct-v0.1; Meta-Llama-3-70B-Instruct e Meta-Llama-3-8B-Instruct. Os "métodos" que se ordenam são esses seis, em zero-shot.
3. **Geração:** o prompt tem quatro partes: descrição da tarefa, com as regras de anotação do conjunto original quando existem; poucos exemplos tirados do conjunto real; orientações sobre o dado (comprimento, tom e outros atributos); formato de saída. Exemplos usados: 1 por intenção, 1 por nota de similaridade, 5 ao acaso em NER (legendas da Tabela I).
4. **Resolução:** prompt zero-shot com descrição da tarefa, formato de saída e o item a prever.
5. **Medidas de desempenho:** intenção, macro F1 médio, mais precisão e revocação; similaridade, correlações de Pearson e de Spearman; NER, F1 de correspondência exata e parcial do trecho da entidade e F1 da previsão do tipo.
6. **Comparação real contra sintético:** a mesma medida calculada para cada um dos seis LLMs no conjunto real e no sintético gerado por cada LLM, e daí as duas medidas abaixo.

## As medidas que o artigo cria ou usa

- **Desempenho absoluto, MSPD (mean squared performance difference, diferença quadrática média de desempenho):** para cada abordagem, a diferença entre a medida no real e no sintético é elevada ao quadrado, e se tira a média entre as abordagens (equação 1). Baixa é melhor. **É média de quadrados:** o artigo a descreve como a diferença média, mas os valores não estão na escala da medida original e não têm sinal. O artigo não publica os desempenhos de cada lado nem a raiz.
- **Desempenho relativo, SRCC (Spearman's rank correlation coefficient):** correlação de postos entre os desempenhos dos seis LLMs no real e no sintético. Alta é melhor. Os autores defendem que, mesmo com MSPD alta, o sintético pode servir se mantiver a ordem, porque a ordem basta para escolher a melhor abordagem.
- **Fator de viés (bias factor), proposta deles:** primeiro normaliza, subtraindo do desempenho de um LLM K no dado gerado por K a média de todos os LLMs nesse mesmo dado (equação 2). Depois compara esse valor com a média do desempenho normalizado de K nos dados gerados pelos outros LLMs (equação 3). A comparação direta não servia, dizem, por causa das grandes diferenças entre dados de LLMs diferentes. Para medida entre 0 e 1, o fator vai de -1 a 1, e positivo indica favorecimento dos próprios dados; medidas acima de 1 devem ser normalizadas antes.

## Tabela I, número por número (célula: MSPD / SRCC)

**(a) Similaridade de texto, 1 exemplo por nota**

| LLM | Headlines, Pearson | Headlines, Spearman | Tweet-News, Pearson | Tweet-News, Spearman |
|---|---|---|---|---|
| GPT-4o | 0,07 / 0,83 | 0,07 / 0,83 | 0,09 / 0,83 | 0,12 / 0,94 |
| GPT-4o-mini | 0,06 / 0,77 | 0,06 / 0,77 | 0,08 / 0,83 | 0,12 / 0,77 |
| Llama-3-70B | 0,05 / 1,0 | 0,05 / 0,77 | 0,03 / 0,94 | 0,04 / 1,0 |
| Llama-3-8B | 0,02 / 0,77 | 0,02 / 0,77 | 0,03 / 0,77 | 0,03 / 0,54 |
| Mixtral-8x22B | 0,05 / 0,83 | 0,04 / 0,83 | 0,06 / 0,94 | 0,09 / 0,77 |
| Mixtral-8x7B | 0,03 / 0,77 | 0,03 / 0,77 | 0,03 / 0,77 | 0,03 / 0,94 |
| Average | 0,04 / 0,83 | 0,04 / 0,83 | 0,03 / 0,83 | 0,05 / 0,94 |

**(b) NER, CrossNER-Literature e CrossNER-Politics, 5 exemplos**

| LLM | Lit., strict F1 | Lit., partial F1 | Lit., entity type | Pol., strict F1 | Pol., partial F1 | Pol., entity type |
|---|---|---|---|---|---|---|
| GPT-4o | 0,02 / 0,77 | 0,01 / 0,60 | 0,01 / 0,77 | 0,01 / 0,71 | 0,01 / 0,49 | 0,01 / 0,83 |
| GPT-4o-mini | 0,01 / 0,83 | 0,01 / 0,60 | 0,01 / 0,83 | 0,01 / 0,60 | 0,01 / 0,09 | 0,02 / 0,66 |
| Llama-3-70B | 0,01 / 0,77 | 0,00 / 0,66 | 0,00 / 0,77 | 0,01 / 0,83 | 0,02 / 0,71 | 0,02 / 0,94 |
| Llama-3-8B | 0,00 / 0,94 | 0,02 / 0,54 | 0,00 / 0,83 | 0,03 / 0,43 | 0,05 / 0,20 | 0,03 / 0,60 |
| Mixtral-8x22B | 0,01 / 0,60 | 0,00 / 0,60 | 0,01 / 0,49 | 0,02 / 0,77 | 0,02 / 0,60 | 0,02 / 1,0 |
| Mixtral-8x7B | 0,00 / 0,83 | 0,01 / 0,43 | 0,00 / 0,66 | 0,02 / 0,89 | 0,02 / 0,14 | 0,02 / 0,94 |
| Average | 0,00 / 0,77 | 0,00 / 0,60 | 0,00 / 0,77 | 0,02 / 0,71 | 0,02 / 0,20 | 0,02 / 0,94 |

**(c) Intenção, SNIPS e ATIS, 1 exemplo por intenção**

| LLM | SNIPS, Precision | SNIPS, Recall | SNIPS, F1 | ATIS, Precision | ATIS, Recall | ATIS, F1 |
|---|---|---|---|---|---|---|
| GPT-4o | 0,00 / 0,94 | 0,00 / 0,94 | 0,00 / 0,94 | 0,11 / 0,89 | 0,09 / 0,89 | 0,11 / 0,94 |
| GPT-4o-mini | 0,00 / 0,84 | 0,00 / 0,90 | 0,00 / 0,90 | 0,13 / 0,89 | 0,09 / 0,89 | 0,12 / 0,94 |
| Llama-3-70B | 0,00 / 0,94 | 0,00 / 0,83 | 0,00 / 0,83 | 0,06 / 0,71 | 0,03 / 0,89 | 0,04 / 0,94 |
| Llama-3-8B | 0,00 / 0,94 | 0,00 / 0,94 | 0,00 / 0,94 | 0,08 / 0,60 | 0,04 / 0,71 | 0,05 / 0,77 |
| Mixtral-8x22B | 0,00 / 0,94 | 0,00 / 0,99 | 0,01 / 0,94 | 0,07 / 0,89 | 0,03 / 0,89 | 0,05 / 0,94 |
| Mixtral-8x7B | 0,00 / 0,89 | 0,00 / 0,94 | 0,00 / 0,94 | 0,1 / 0,60 | 0,05 / 0,89 | 0,07 / 0,94 |
| Average | 0,00 / 0,94 | 0,00 / 0,94 | 0,00 / 0,94 | 0,08 / 0,89 | 0,05 / 0,89 | 0,06 / 0,94 |

**A linha Average:** a legenda a define como a média da medida de desempenho dos LLMs individuais, sem detalhar a conta. Os valores dela não coincidem com a média simples das seis células de cima (conferência aritmética desta ficha): em Politics, partial F1, as seis SRCC dão cerca de 0,37 e a linha traz 0,20; em ATIS, Precision, dão cerca de 0,76 e a linha traz 0,89.

## O que os autores leem na Tabela I

- **Similaridade:** a maioria dos LLMs tem MSPD alta, então o sintético não representa o desempenho absoluto; todos têm SRCC alta, então capta o relativo, com 1,0 do Llama-3-70B em algumas medidas.
- **Intenção:** SRCC alta em todos. No ATIS a diferença absoluta fica; no SNIPS ela some, e os autores tratam o caso como exceção em que o sintético capta as duas coisas, atribuindo isso a ser um conjunto mais simples, com menos intenções (7 contra 17).
- **NER:** a SRCC cai bastante, sobretudo em F1 parcial e tipo de entidade, o que atribuem a ser uma tarefa mais complexa, com previsão de vários trechos. Nas médias, a MSPD fica de 0,00 a 0,02.
- **Síntese deles:** o sintético é "a good predictor of relative performance but not a strong indicator of absolute performance".
- **Nenhum gerador se destaca:** nenhum LLM dá sintético mais representativo que os outros; cada um é forte em alguns conjuntos e medidas. Por isso recomendam "generate data from multiple LLMs and average the benchmarks". O resumo acrescenta preferir modelos maiores sempre que possível.
- **Conclusão por tarefa:** a eficácia depende da tarefa; em tarefas fáceis como intenção o sintético prevê bem, em tarefas complexas como NER a capacidade diminui.

## Tabela II, fator de viés

Medida usada: F1 exato em NER, F1 médio em intenção, Pearson em similaridade. A última coluna é, pela legenda, a média do fator entre as tarefas.

| Modelo | NER Literature | NER Politics | Intent Snips | Intent Atis | Headlines | Tweet-News | Average |
|---|---|---|---|---|---|---|---|
| GPT-4o | +0,045 | +0,062 | -0,02 | +0,113 | +0,007 | -0,009 | +0,033 |
| GPT-4o-mini | -0,014 | -0,055 | -0,014 | +0,137 | -0,005 | +0,07 | +0,019 |
| Llama-3-70B | +0,012 | -0,023 | +0,001 | +0,007 | -0,018 | -0,074 | -0,095 |
| Llama-3-8B | +0,004 | -0,023 | +0,009 | -0,019 | -0,079 | -0,102 | -0,038 |
| Mixtral-8x22B | +0,017 | +0,002 | +0,016 | +0,058 | +0,016 | -0,012 | +0,016 |
| Mixtral-8x7B | +0,041 | +0,04 | +0,004 | +0,017 | +0,047 | +0,223 | +0,061 |

**Conferência aritmética desta ficha:** quatro médias batem com as células, com arredondamento. Duas não: a média simples das seis células do Llama-3-70B dá cerca de -0,016 (-0,095 é a soma delas), e a do Llama-3-8B dá -0,035. Com os valores recalculados, o Llama-3-8B fica abaixo do Llama-3-70B; com os publicados, acima.

**O que os autores dizem:** em Llama e Mixtral, os modelos menores mostram viés mais forte que os maiores; o Mixtral-8x7B tem viés forte a favor dos próprios dados (0,061); na família GPT a tendência se inverte, com GPT-4o acima do GPT-4o-mini. Por tarefa, fatores menores em SNIPS e Headlines e médias maiores em NER, ATIS e Tweet-News. Conclusão deles: LLMs menores em geral têm fator um pouco maior que os maiores, tarefas fáceis mostram menos viés e complexas, mais. O resumo diz que modelos maiores não mostram o viés; a introdução, que não mostram viés significativo. O fator compara o LLM nos próprios dados com o mesmo LLM nos dados de outros LLMs, e não com dado real.

## Limites que os autores declaram

- O mesmo prompt em todos os LLMs, o que pode fazer alguns renderem abaixo do que poderiam.
- Avaliação só em zero-shot; few-shot fica para trabalho futuro.
- Planejam mais tarefas e mais LLMs.

## Tudo o mais que ensina

- **Separar as duas perguntas:** "o número é parecido" e "a ordem é parecida" são medidas separadas, e nas tabelas há conjunto que vai bem nas duas (SNIPS), só na ordem (ATIS) e só no número (Politics, partial F1).
- **O motivo do trabalho:** praticante com pouco ou nenhum dado de teste tem dificuldade de decidir qual LLM serve para uma tarefa, e domínios como saúde e bancos têm restrição de privacidade sobre dado anotado.
- **Custo de obter e anotar** dados grandes é o outro motivo citado para recorrer ao sintético.
- **Fontes da geração por prompt:** a estrutura em partes segue um levantamento sobre geração, curadoria e avaliação de dado sintético por LLM (Long e outros, 2024).
