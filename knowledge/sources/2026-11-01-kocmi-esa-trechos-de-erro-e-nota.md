---
titulo: "Error Span Annotation: A Balanced Approach for Human Evaluation of Machine Translation"
tipo: paper
autor: "Tom Kocmi, Vilém Zouhar, Eleftherios Avramidis, Roman Grundkiewicz, Marzena Karpinska, Maja Popović, Mrinmaya Sachan, Mariya Shmatova"
url: "https://arxiv.org/abs/2406.11580"
publicado_em: 2024-06-17
capturado_em: 2026-11-01
licenca: "CC BY 4.0 (indicada na página do arXiv, com link para http://creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [mqm, error-span-annotation, direct-assessment, error-annotation, holistic-score, score-after-errors, ties, ceiling-effect, inter-rater-agreement, intra-rater-agreement, severity-reliability, attention-checks, annotation-cost, machine-translation]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv 2406.11580, v1 em 17/06/2024 e v2 em 18/10/2024; lida a v2. Publicado nos anais da Ninth Conference on Machine Translation (WMT 2024), p. 1440 a 1453, Miami, novembro de 2024 (https://aclanthology.org/2024.wmt-1.131). Autores da Microsoft, da ETH Zurich, do DFKI, da UMass Amherst, da DCU e da Dubformer; os dois primeiros com contribuição igual. Código e dados em https://github.com/wmt-conference/ErrorSpanAnnotation. Texto extraído do PDF da v2 com `pdftotext`; as tabelas saem soltas e foram lidas linha a linha. Lido para a rodada investigativa.

**Atenção:** um par de línguas (inglês para alemão), um subconjunto de 207 segmentos por sistema da WMT23, 13 "sistemas" (12 de tradução automática e uma tradução humana). O MQM de comparação dos autores e o MQM oficial da WMT vêm de grupos e ferramentas diferentes, o que mistura protocolo e equipe nas comparações de concordância.

## 1. A pergunta

O MQM (classificar cada erro numa tipologia, com gravidade) é caro, lento e exige especialistas treinados; a nota direta de 0 a 100 (DA, com os descritores do SQM, "DA+SQM") é barata e qualquer tradutor faz, mas é menos confiável. Dá para ficar no meio?

## 2. O protocolo ESA

1. **Primeiro, marcar todos os trechos com problema** (caracteres, palavras, frases), cada um com uma de **duas gravidades**: menor (estilo, gramática ou escolha de palavra que poderia ser melhor) ou maior (sentido seriamente mudado, difícil de ler, uso prejudicado). Sem categoria de erro. Omissão se marca num marcador "[MISSING]" no fim do texto traduzido.
2. **Depois, dar uma nota de 0 a 100 ao segmento**, com os descritores do SQM (0, nenhum sentido preservado; 33%, parte do sentido; 66%, quase todo o sentido com poucos erros de gramática; 100%, sentido e gramática perfeitos), **vendo os erros que acabou de marcar**. A tese: o anotador que marcou os erros primeiro dá uma nota mais bem informada; a nota é o resultado principal, e os trechos servem de base para ela.

## 3. Por que não somar os erros (a crítica à nota tipo MQM)

- A conta usual (menos 5 por maior, menos 1 por menor, de Freitag e coautores) **não escala com o tamanho do texto**: o mesmo segmento repetido duas vezes vale o dobro de penalidade, o que pesa em avaliação por parágrafo, com segmentos de tamanhos muito diferentes.
- A nota somada pode não corresponder à qualidade do segmento quando **um erro só afeta vários lugares** e é marcado várias vezes (no exemplo do artigo, um verbo errado arrasta o auxiliar).
- **A soma se amontoa perto de zero e não tem piso:** a distribuição da nota tipo MQM fica concentrada em 0 e pode ir a menos infinito quanto maior o segmento; as notas manuais dos anotadores se espalham e ficam sempre entre 0 e 100.
- **Empates:** no MQM oficial da WMT23, **30,8% dos segmentos não têm erro nenhum**; na nota direta, só 5,2% recebem 100. Muitos empates complicam medir concordância.
- O MQM foi feito como **protocolo de diagnóstico** e depois reaproveitado para dar nota a segmentos.

## 4. Resultados

- **Contagem:** ESA1 (anotadores bilíngues experientes) marca 0,45 trecho por segmento; ESA2 (tradutores, outro fornecedor), 1,00; o MQM dos autores, 0,53; o MQM oficial da WMT, 3,37, sete vezes mais, que os autores atribuem às diferenças entre as equipes. A proporção entre menores e maiores é parecida em todos (cerca de dois terços menores).
- **Ordenação de sistemas, contra o MQM oficial como gabarito:** ESA e o MQM refeito ordenam os 13 sistemas do mesmo jeito (94,9% de acurácia por pares); a nota direta da WMT fica claramente atrás. O ESA usando **só os trechos** convertidos em nota (ESAspans) é pior que o ESA com a nota manual: **"a combinação de trechos e nota parece produzir os melhores resultados"**. A nota direta da WMT pôs a tradução humana no segundo grupo; o MQM, no topo sozinha, talvez porque a nota direta pesa mais estilo e fluência, que são 60% dos erros da tradução humana segundo o MQM.
- **Correlação por segmento com o MQM oficial (Kendall):** todas baixas, de 0,170 a 0,250; as do ESA são as mais altas, e as de só trechos ficam abaixo.
- **Sobreposição dos trechos:** o ESA cobre 29% dos trechos do MQM oficial e o MQM refeito, 32%; o MQM oficial cobre 93% dos trechos do ESA e 85% dos do MQM refeito (mas ele marca sete vezes mais).
- **Concordância (Tabela 4):** intra-anotador (os mesmos anotadores refazendo dois meses depois) e entre anotadores, ESA acima do MQM em todas as medidas. Intra: Kendall tau-c de 0,149 (ESA) contra 0,109 (MQM); Pearson 0,403 contra 0,189. Entre anotadores: tau-c 0,254 contra 0,116; Pearson 0,482 contra 0,281. Revocação de erro (marcar algum erro no mesmo segmento): 69,6% contra 61,9% intra; 66,6% contra 40,1% entre. Os autores levantam a hipótese de que, no MQM, mais trabalhoso, o anotador pula os erros menores para poupar tempo.
- **Concordância nos próprios erros do MQM (Tabela 5):** o mesmo anotador, dois meses depois, marca de novo pelo menos parte do mesmo erro em só **29,3%** dos casos; com a mesma gravidade, 16,9%; com a mesma categoria, 18,9%; com gravidade e categoria, 11,6%; com gravidade e subcategoria, **8,4%**. Entre equipes, 50,2% de sobreposição de algum erro, 23,7% com a mesma gravidade, 10,0% com gravidade e categoria.
- **Controle de atenção:** em documentos sorteados, trocou-se parte da tradução por palavras aleatórias, criando um erro maior conhecido. A versão original teve nota maior que a adulterada em 86% dos casos no ESA e 78% no MQM; o segmento adulterado recebeu mais trechos marcados que o original em 54% (ESA) e 70% (MQM), e o trecho adulterado em si foi marcado em 56% (ESA) e 76% (MQM): o MQM marca mais o trecho, mas no ESA o anotador pode baixar a nota sem marcar.
- **Tempo:** mediana por parágrafo de 38 segundos no MQM e 29 no ESA (menos 23%); pela média das medianas de cada anotador, 49 contra 34 segundos (menos 32%). Pequeno efeito de aprendizado nos dois (cerca de 0,2 segundo a menos por segmento já feito). Especialistas em MQM recebem o dobro da hora de um tradutor; o artigo estima que um segmento MQM pode sair até dez vezes mais caro que uma nota direta.

## 5. Limites declarados

O ESA não dá a quebra por tipo de erro, que ajudaria quem desenvolve o sistema; os autores dizem que o objetivo é avaliar, não diagnosticar, e que os trechos marcados podem ser classificados depois, se for preciso. Um par de línguas só; nota direta não foi refeita para medir a concordância dela.

## 6. Tudo o mais que ensina

- **Descritivo contra prescritivo:** marcar trechos sem tipologia deixa o anotador dizer o que vê (descritivo); classificar numa tipologia fechada pede que ele se alinhe a uma crença única (prescritivo).
- **Erros primeiro, nota depois, com os erros à vista:** a ordem das tarefas é parte do instrumento.
- **Duas gravidades bastam** para o ganho de confiabilidade; a categoria é o que mais custa e o que menos se repete.
- **Itens adulterados de propósito** medem se o anotador presta atenção e servem de controle de qualidade barato.
- **Medir concordância com muitos empates** pede estatística própria (Kendall tau-c), não faixas escolhidas a dedo.
- **Mostrar o documento inteiro** e anotar segmento por segmento mantém o contexto sem perder a granularidade.
