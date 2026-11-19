---
titulo: "Annotating and Modeling Fine-grained Factuality in Summarization"
tipo: paper
autor: "Tanya Goyal, Greg Durrett"
url: "https://arxiv.org/abs/2104.04302"
publicado_em: 2021-04-09
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [factuality, summarization, synthetic-data, human-annotation, error-taxonomy, hallucination, distribution-mismatch, held-out-vs-real, error-localization, dependency-arc-entailment]
licenca: "Licença não exclusiva do arXiv (arXiv.org perpetual, non-exclusive license), indicada na página do arXiv; entra só a ficha, e o integral está na url"
---

# Goyal e Durrett 2021 (NAACL): erro sintético, erro real e anotação fina em factualidade de resumo

Ficha em palavras próprias. Goyal e Durrett, Departamento de Ciência da Computação, Universidade do Texas em Austin; arXiv 2104.04302v1, 9/4/2021, marcado "NAACL 2021" nos comentários da página do arXiv; processamento de linguagem natural. O integral não entra: está na url. Lido no PDF do arXiv em 2026-11-06, inclusive os apêndices A a E e as figuras 4 e 6. Código e dados em `github.com/tagoyal/factuality-datasets`.

## As perguntas

Modelos de resumo abstrativo (que reescrevem, em vez de copiar frases) produzem resumos infiéis ao texto de origem. Já houve conjuntos anotados e modelos para isso, mas sem um quadro claro de que erros importam e de onde as técnicas acertam e falham. Duas perguntas:

1. A geração de dados sintéticos, feita para factualidade, coincide com os erros reais dos modelos? Eles respondem que não.
2. Qual o melhor jeito de modelar e aprender factualidade em resumo muito abstrativo: anotação humana fina (palavra, trecho) ou por frase?

Três achados do resumo do artigo: os erros diferem muito entre conjuntos, e "commonly-used training sets of simple synthetic errors do not reflect errors made on abstractive datasets like XSum"; anotação humana fina treina melhor do que anotação por frase ou dado sintético; o melhor detector permite treinar resumidores mais factuais.

**Definição.** Um modelo de factualidade recebe documento D e resumo gerado S e diz se toda a informação de S se apoia em D. Na nota 3, os autores chamam factualidade de mal definida: inferência, conhecimento de mundo e implicatura variam conforme os anotadores de cada conjunto, embora, dizem, os modelos atuais só raramente caiam nesses casos difíceis.

## Os dois domínios

- **XSum:** resumo "extremo" de artigos da BBC, em que a primeira frase do artigo é tratada como resumo. Muito abstrativo; o modelo precisa de dependências de longo alcance e pode não recuperar tudo.
- **CNN/DailyMail (CNN/DM):** resumo em várias frases, com abstração bem menor e muita sobreposição com o artigo.

## Os dados de treino comparados

- **Ent-C (entity-centric, sintético centrado em entidade).** Segue Kryscinski et al. 2020: corrompe por regra (troca de entidade, número e pronome, negação, ruído), com paráfrase por retrotradução, a partir do resumo de referência. Trata o resumo de referência como factual. Como a corrupção é por regra, dá para marcar o trecho do erro. 50 mil pares em CNN/DM; tamanho parecido em XSum.
- **Gen-C (generation-centric, sintético centrado em geração).** Segue Goyal e Durrett 2020a: gera paráfrases do resumo de referência e usa a 10ª melhor do feixe, supondo que ela erra mais do que a primeira, e rotula como não factual a informação nova. Os autores dizem que esse método se alinha melhor aos erros de modelos do que a troca de entidades. Rótulo por frase e por arco de dependência (a relação entre duas palavras, factual se o documento a sustenta). 40 mil exemplos em cada domínio.
- **Humano (XSum-Human).** De Maynez et al. 2020: trechos marcados como alucinação ou erro em 4 modelos de resumo sobre XSum, além dos resumos de referência; 2.500 pares (artigo, resumo). Se qualquer palavra está marcada, a frase é não factual.

Anotação disponível (tabela 1): Ent-C e Humano têm frase e palavra diretas e arco derivado (se a palavra-cabeça ou a dependente está marcada, o arco é não factual); Gen-C tem frase e arco diretos, sem palavra.

## Taxonomia dos erros (figura 3)

Cada categoria se divide em **extrínseco** (alucina informação que não está no artigo) e **intrínseco** (interpreta mal o que está lá), pela distinção de Maynez et al. 2020.

1. **Entidade:** nomes, quantidades, datas. Entidade nova é extrínseco; juntar duas do artigo é intrínseco ("Paul Telstra", mistura de um advogado com uma operadora, no exemplo).
2. **Evento:** afirmações erradas sobre eventos, como predicado com argumento trocado. Evento novo é extrínseco; atributo ou agente trocado é intrínseco.
3. **Sintagma nominal (NP):** novo modificador é extrínseco; modificador errado vindo do artigo é intrínseco.
4. **Outros:** agramatical, palavra repetida, trecho muito errado; sem a divisão.

Diferente da de Lux et al. 2020, voltada ao efeito no leitor: esta segue o papel gramatical do erro.

**Anotação manual.** XSum: 100 resumos gerados pelo BART. CNN/DM: os 50 resumos de 10 modelos reunidos por Kryscinski et al. Também os erros artificiais de Ent-C e Gen-C. Em 50 resumos anotados pelos dois autores (apêndice A): concordaram sobre o que é erro 74% das vezes e, marcando o mesmo trecho, sobre a categoria 84%.

## Distribuição de erros (figura 4; lida do gráfico, fração de exemplos, um exemplo pode ter vários erros)

| Conjunto | Ext. entidade | Ext. evento | Ext. NP | Int. entidade | Int. evento | Int. NP | Outros |
|---|---|---|---|---|---|---|---|
| XSum, BART real | cerca de 0,23 | cerca de 0,23 | cerca de 0,17 | cerca de 0,05 | cerca de 0,15 | cerca de 0,13 | cerca de 0,04 |
| CNN/DM, real | | cerca de 0,02 | | cerca de 0,22 | cerca de 0,50 | cerca de 0,22 | cerca de 0,04 |
| Ent-C, sintético | cerca de 0,17 | | | | cerca de 0,40 | cerca de 0,26 | cerca de 0,17 |
| Gen-C, sintético | cerca de 0,06 | cerca de 0,05 | cerca de 0,03 | | cerca de 0,24 | cerca de 0,28 | cerca de 0,35 |

- **XSum:** 60% dos erros do BART são extrínsecos e 40% intrínsecos. Razões dadas: o conjunto foi montado automaticamente e os resumos de referência têm ruído (75% deles não factuais, segundo Maynez et al.), e por serem muito abstrativos o modelo aprende a combinar partes distantes do artigo. A barra da figura 4 traz 75% para XSum e 14% para CNN/DM como fração de resumos não factuais no conjunto de teste.
- **CNN/DM:** só 14% dos resumos gerados têm erro, no conjunto de validação de Kryscinski; a maior parte é intrínseca, sobretudo de evento, por compressão ou fusão de frases. Exemplo: dois meninos "em estado crítico nas Ilhas Virgens", quando estavam no hospital depois de uma viagem às ilhas. Extrínseco é raro, e mais raro ainda em sistemas recentes como o PEGASUS.
- **Sintético contra real:** o intrínseco de evento de Ent-C vem quase só de troca de pronome. Como os dois domínios erram tão diferente, sintético inspirado em um não deve servir no outro.

## Os modelos de factualidade

- **Sent-Factuality:** BERT ou ELECTRA recebe D e S concatenados; o token [CLS] passa por uma camada linear e softmax e dá factual ou não factual.
- **DAE (Dependency Arc Entailment):** mesmo encoder, mas decide por arco do parse de dependências do resumo; a representação do arco concatena as das duas palavras. Basta um arco não factual para o resumo ser não factual. Exemplo: em "Seven games involving Nimes were arrested", o arco de "games" com "arrested" é não factual; o de "seven" com "games" se sustenta.
- **DAE-Weak:** para quando só há rótulo por frase. Em exemplo factual, todo arco é factual; em não factual, pelo menos um arco é não factual, e ele não deve estar no documento. Treina maximizando a verossimilhança marginal das rotulagens que respeitam essas restrições.

Todos são ELECTRA (electra-base-discriminator) afinado, com taxa de aprendizado 2e-5, lote 8, 3 épocas (tabela 9). Os modelos tratam resumos de uma frase, para coincidir com o teste humano; os autores dizem que estender a várias frases é direto.

## Resultados: treino em sintético

A medida é a acurácia balanceada por classe. A base é o rótulo majoritário, 50.

**CNN/DM, teste humano de Kryscinski (503 pares, de 10 modelos; tabela 2; o texto remete a ela chamando-a de "Table 7").**

| Modelo | Treino Ent-C | Treino Gen-C |
|---|---|---|
| Kryscinski et al. 2020 | 74,1 | sem valor na tabela |
| Sent-Factuality | 72,3 | 64,4 |
| DAE | 76,7 | 72,1 |
| DAE-Weak | 75,2 | 71,1 |

**XSum, 500 exemplos do teste humano de Maynez (tabela 3).**

| Modelo | Treino Ent-C | Treino Gen-C |
|---|---|---|
| Sent-Factuality | 50,9 | 54,2 |
| DAE | 51,2 | 53,0 |
| DAE-Weak | 53,6 | 51,6 |

**Os mesmos modelos em exemplos reservados, feitos do mesmo jeito que o treino (tabela 7, apêndice B).**

| Domínio e modelo | Ent-C | Gen-C |
|---|---|---|
| CNN/DM, Sent-Factuality | 96,4 | 91,2 |
| CNN/DM, DAE | 95,4 | 97,3 |
| CNN/DM, DAE-Weak | 94,8 | 97,8 |
| XSum, Sent-Factuality | 96,1 | 97,9 |
| XSum, DAE | 94,3 | 97,1 |
| XSum, DAE-Weak | 95,3 | 95,9 |

Juntando as três tabelas, os mesmos modelos rendem de 91,2 a 97,9 no sintético reservado, de 64,4 a 76,7 no humano de CNN/DM e de 50,9 a 54,2 no humano de XSum, perto da base. Os autores concluem que os modelos se ajustam bem à distribuição sintética e que ela difere dos erros reais de geração. Citação da regra: "fundamental difference between the errors that are produced by XSum summarization models and those introduced by artificial data corruption mechanisms".

**Figura 6 (CNN/DM, ponto de treino a ponto de treino).** No sintético reservado a acurácia sobe e se estabiliza, cerca de 0,95 em Ent-C e cerca de 0,98 em Gen-C. No conjunto humano de desenvolvimento oscila, de cerca de 0,65 a cerca de 0,79 em Ent-C; em Gen-C fica em cerca de 0,75 (DAE) e cerca de 0,65 (Sent-Factuality). Otimizar para o sintético, dizem, não melhora necessariamente o resultado nos erros reais. Ent-C mostrou mais variância.

## Resultados: treino em dado humano

2.000 exemplos do XSum-Human, os mesmos 500 de teste (tabela 4).

| Modelo | Acurácia balanceada |
|---|---|
| Sent-Factuality | 65,6 |
| DAE | 78,7 |
| DAE-Weak | 70,9 |

Comparação deles: poucos exemplos humanos superam por larga margem os grandes conjuntos gerados, e a anotação fina dá o maior ganho. Sem ela, o DAE-Weak ainda supera o modelo por frase.

**Não transfere entre domínios:** treinado no humano de XSum e testado em CNN/DM, o melhor modelo fica em 55,9, contra 76,7 do DAE com treino em Ent-C.

**Transfere entre modelos do mesmo domínio (apêndice C, tabela 8; 300 pares de teste por modelo).** Treino "All" (2.000 de outros modelos e 200 do mesmo) contra "Others" (2.000 só de outros), com DAE:

| Modelo avaliado | All | Others |
|---|---|---|
| BERTS2S | 79,6 | 82,3 |
| PTGen | 75,8 | 77,0 |
| TConvS2S | 76,7 | 74,1 |
| TranS2S | 84,5 | 85,3 |

Os autores concluem que, nesses modelos, todos treinados no mesmo conjunto, a anotação de um serve para avaliar outro. O texto fala em 5 modelos anotados, e a tabela mostra 4.

## Localizar o erro (tabela 5, XSum)

| Modelo | Precisão | Revocação | F1 |
|---|---|---|---|
| Arco: DAE | 69,7 | 78,2 | 73,7 |
| Arco: DAE-Weak | 54,9 | 76,6 | 63,9 |
| Palavra: DAE | 57,5 | 74,7 | 65,0 |
| Palavra: DAE-Weak | 56,2 | 62,3 | 59,1 |
| Palavra: DAE (best-ckpt) | 62,0 | 83,9 | 71,3 |

A decisão por palavra sai de forma aproximada do arco: palavra em algum arco não factual é não factual. O "best-ckpt" é o ponto de treino escolhido nos próprios dados de teste, para buscar revocação, e é ele que segue para a aplicação abaixo.

## Aplicação: treinar um resumidor melhor

Treinar sobre uma palavra não factual ensina o modelo a alucinar. Eles alteram a função objetivo para maximizar a verossimilhança só das palavras que o DAE considera factuais (a máscara M vale 1 ou 0), e comparam com o BART sem máscara e com a truncagem de perda de Kang e Hashimoto 2020. 50 mil exemplos de treino, inicialização em BART-XSum-Large; 11 mil de teste, sem os exemplos usados para treinar o detector (tabela 6).

| Modelo | Erro por palavra (menor é melhor) | Erro por frase (menor é melhor) | Humano (maior é melhor) |
|---|---|---|---|
| Base | 32,2 | 74,0 | 37,4 |
| Truncagem de perda | 31,1 | 70,9 | 39,1 |
| Com o DAE | 23,7 | 61,4 | 46,5 |

Os erros por palavra e por frase são medidos pelo próprio DAE. A nota humana vem de 50 artigos sorteados e 7 anotadores no Amazon Mechanical Turk, que marcam cada resumo como factual (1) ou não (0) e destacam o trecho errado; a nota é a média de 7.

## Limites e posições declarados

- Factualidade é noção difusa e não cabe num conjunto de regras discretas; técnicas de restrição de decodificação, correção posterior e modificação do modelo têm dificuldade de cobrir toda a gama de erros.
- Consertar por inteiro um resumo é um problema muito difícil, e por isso trabalhos anteriores cuidaram só de parte dos erros.
- Anotar por modelo é proibitivamente caro, o que motiva o apêndice C.

Conclusão do artigo: "existing synthetic datasets are not well-suited to factuality evaluation of recent summarization models", citando BART e XSum, e esperam modelagem e criação de dados melhores.

## Tudo o mais que ensina

- **Linha do tempo do tema:** resumo antigo avaliava seleção de conteúdo e gramática, com pouca atenção à factualidade; Pyramid poderia servir, mas foi usado para conteúdo. Depois vieram modelos de entailment (Falke et al. 2019), perguntas e respostas (Durmus et al. 2020; Wang et al. 2020) e dado sintético.
- **Verificação de fatos é vizinha, mas outra:** ali a afirmação é em geral escrita por pessoa e direta; num resumo gerado, ela pode vir escondida em modificador nominal ("two-time winner").
- **Regra do DAE-Weak:** a nota 5 aproxima a técnica de regularização posterior (posterior regularization), com a restrição dura por exemplo, e de aprendizado guiado por restrições (constraint-driven learning).
- **Relação com outros usos do sintético:** Ent-C também serve a restrição na decodificação (Zhao et al. 2020) e à correção posterior (Cao et al. 2020); o artigo diz que essas abordagens supõem que a corrupção produz resumos não factuais úteis e que os de referência são factuais.
- **Conjuntos humanos usados em teste:** 503 pares em CNN/DM, 500 em XSum, com a validação de Kryscinski usada para escolher o ponto de treino.
- **Recomendação de dados:** o artigo diz que, em XSum, é preciso dado mais parecido com os erros de geração para treinar nesse cenário, e que coleta e modelagem devem considerar a diferença entre domínios.
- **Tarefa no Mechanical Turk (apêndice E):** o anotador vê um artigo e 3 resumos, marca cada um e destaca o trecho errado.
- **Hiperparâmetros (tabelas 9 e 10):** Adam, sem decaimento de peso e sem aquecimento, entrada máxima de 512; o resumidor BART treina 10 épocas; para a decodificação dele, 6 feixes, penalidade de tamanho 2, sem repetir trigramas, de 10 a 60 tokens. Para o Sent-Factuality da seção 5.2, de alta variância, média de 3 execuções.

## O que a fonte não diz

Não testa um modelo treinado em dado humano contra um conjunto sintético. Usa só dois domínios de resumo, em inglês. Não dá os valores numéricos da figura 4 nem intervalos de confiança ou testes de significância para as tabelas.
