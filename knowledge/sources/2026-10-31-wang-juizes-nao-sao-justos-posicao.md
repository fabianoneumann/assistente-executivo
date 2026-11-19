---
titulo: "Large Language Models are not Fair Evaluators"
tipo: paper
autor: "Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Lingpeng Kong, Qi Liu, Tianyu Liu, Zhifang Sui"
url: "https://aclanthology.org/2024.acl-long.511/"
publicado_em: 2023-05-29
capturado_em: 2026-10-31
licenca: "CC BY 4.0 na versão publicada (a página do artigo na ACL Anthology traz o selo CC BY 4.0 e o rodapé do site diz que o material publicado a partir de 2016 está sob CC BY 4.0; o PDF traz '©2024 Association for Computational Linguistics'). A versão do arXiv (2305.17926) está sob a licença não exclusiva do arXiv; o integral lido vem do PDF da ACL Anthology"
areas: [agent-engineering]
tags: [llm-as-judge, position-bias, pairwise-comparison, conflict-rate, score-gap, calibration, multiple-evidence-calibration, balanced-position-calibration, human-in-the-loop, vicuna-benchmark, evaluation-cost]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0, da versão publicada na ACL Anthology) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Preprint no arXiv (2305.17926): v1 em 29/05/2023 e v2 em 30/08/2023, com dez autores e licença não exclusiva do arXiv. Publicado nos anais do ACL 2024 (62nd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, Bangkok, agosto de 2024, páginas 9440 a 9450, DOI 10.18653/v1/2024.acl-long.511), com um autor a mais (Lingpeng Kong). Como a ACL Anthology publica sob CC BY 4.0, o integral é o da versão dos anais e a `url` aponta para ela; a v2 do arXiv também foi lida para comparar. Diferenças: a numeração das seções (no arXiv, calibração é a seção 3, experimentos a 4 e análise a 5; nos anais, 2.3, 3 e 4) e dois números: ChatGPT com MEC + BPC tem 58,7% de acurácia no arXiv e 58,8% nos anais (o texto dos anais mantém "+14,3%", que bate com 44,4% + 14,3 = 58,7%), e o modelo de comparação com MEC + BPC tem 60,3% no arXiv e 60,0% nos anais. Afiliações: Peking University (State Key Laboratory of Multimedia Information Processing), The University of Hong Kong e Tencent Cloud AI. Código e anotações humanas no kit FairEval (https://github.com/i-Eval/FairEval). Integral extraído do PDF da ACL Anthology; a Tabela 2 e as Figuras 2 e 5 foram lidas nas páginas renderizadas. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

## 1. A pergunta

Usar GPT-4 e ChatGPT como árbitros para pontuar e comparar respostas de modelos candidatos virou prática comum (o pipeline do Vicuna, que pede ao GPT-4 nota e explicação, ganhou uso amplo pela simplicidade). Mas LLMs são sensíveis a instruções e entradas. Os autores perguntam se esse paradigma resiste a perturbações como a ordem dos candidatos, e mostram que não: trocar a ordem basta para "hackear" o ranking. O exemplo do resumo do artigo: com o ChatGPT como avaliador e o Vicuna-13B na segunda posição, o Vicuna-13B vence o ChatGPT em 66 das 80 perguntas testadas.

## 2. O viés revelado

- **O modelo de avaliação (Tabela 1, do Vicuna/Zheng et al.):** pergunta, resposta do Assistente 1, resposta do Assistente 2 e o pedido: avaliar utilidade, relevância, precisão e nível de detalhe, dar uma nota de 1 a 10 a cada um, primeiro uma linha com as duas notas e depois a explicação, "evitando qualquer viés e garantindo que a ordem em que as respostas foram apresentadas não afete" o julgamento. O viés aparece apesar dessa instrução (Figura 1: a mesma dupla recebe 9 e 7 numa ordem e 7 e 9 na outra).
- **Taxa de conflito (Equação 1):** para cada exemplo, consulta-se o LLM duas vezes, com as respostas em ordem original e trocada; a taxa é a fração dos exemplos em que os dois resultados divergem.
- **Tabela 2 (taxa de vitória do Vicuna-13B como Assistente 1 e como Assistente 2; taxa de conflito):** GPT-4 julgando Vicuna-13B contra ChatGPT: 51,3% e 23,8%; conflito em 37 de 80 (46,3%). GPT-4, Vicuna-13B contra Alpaca-13B: 92,5% e 92,5%; 4 de 80 (5,0%). ChatGPT, Vicuna-13B contra ChatGPT: 2,5% e 82,5%; 66 de 80 (82,5%). ChatGPT, Vicuna-13B contra Alpaca-13B: 37,5% e 90,0%; 42 de 80 (52,5%).
- **Achados:** (1) os LLMs são sensíveis à posição, e o modelo mais forte é menos afetado; (2) cada um pende para um lado: o GPT-4 favorece a primeira posição, o ChatGPT a segunda; (3) o viés depende da diferença de qualidade: o conflito no confronto Vicuna contra Alpaca, em que a qualidade é bem diferente, é muito menor do que no confronto Vicuna contra ChatGPT, de qualidade parecida.
- **Figura 2 (GPT-4; total de exemplos e conflitos por faixa de diferença de nota entre as duas respostas; valores lidos no gráfico):** diferença de 0 a 1, cerca de 35 exemplos e 25 conflitos; de 1 a 2, cerca de 41 e 13; de 2 a 3, cerca de 42 e 2; de 3 a 4, cerca de 24 e 1; 5 ou mais, cerca de 15 e nenhum. A soma dos conflitos (cerca de 41) bate com os 37 + 4 da Tabela 2, o que sugere que a figura junta os dois confrontos julgados pelo GPT-4. Conclusão dos autores: com diferença de nota pequena (até 1), o resultado do GPT-4 depende muito da posição; com diferença grande (3 ou mais), fica estável.

## 3. A calibração proposta (três estratégias)

- **Multiple Evidence Calibration (MEC):** o modelo do Vicuna dá a conclusão antes da explicação, e num modelo autorregressivo a nota não se apoia na explicação que vem depois. O modelo com calibração por evidência (EC, Tabela 3) pede primeiro a "evidência de avaliação" (a explicação) e só depois as notas. Para estabilizar, amostram-se k explicações e notas (temperatura 1) e faz-se a média: um conjunto (ensemble) de julgamentos.
- **Balanced Position Calibration (BPC):** cada par é avaliado também com as respostas trocadas; com MEC, isso dá 2k notas para cada resposta (k em cada posição), e a nota calibrada é a média delas (Equação 2). Vence a resposta de maior média.
- **Human-in-the-Loop Calibration (HITLC):** decide *quando* chamar o humano. Os 2k resultados (vitória, empate ou derrota, de cada amostra em cada posição) entram numa entropia, a Balanced Position Diversity Entropy (BPDE, Equações 3 a 5): quanto mais os resultados divergem entre amostras e posições, maior a entropia e maior a chance de o julgamento estar enviesado. Os top-β% com maior BPDE vão para anotação humana, resolvida por maioria.

## 4. Experimentos

- **Anotação humana:** três dos autores, pesquisadores familiarizados com IA, anotaram independentemente vitória, empate ou derrota entre as respostas do ChatGPT e do Vicuna-13B nas 80 perguntas do Vicuna Benchmark (9 categorias), pelos mesmos quatro critérios do modelo, com as respostas em ordem aleatória; cerca de 3 minutos por exemplo; o rótulo final é a maioria dos três.
- **Configuração:** API da OpenAI ("gpt-3.5-turbo" como ChatGPT, "gpt-4" como GPT-4); temperatura 0 nos métodos sem amostragem; MEC com temperatura 1 e k = 3. Métricas: acurácia e kappa contra o rótulo de maioria humana. Nos métodos sem BPC, a ordem das respostas é sorteada e o resultado é a média de 100 rodadas.
- **Tabela 4 (acurácia; kappa; custo):** humanos individuais 68,8%, 76,3% e 70,0% (kappa 0,50, 0,62 e 0,50; US$ 30 cada), média humana 71,7% e 0,54. GPT-4: VANILLA 52,7%, 0,24, US$ 2,00; EC (k = 1) 56,5%, 0,29, US$ 2,00; MEC (k = 3) 58,7%, 0,30, US$ 3,19; MEC (k = 6) 60,9%, 0,33, US$ 4,98; MEC (k = 3) + BPC (k = 3) 62,5%, 0,37, US$ 6,38; com HITLC (β = 20%) 73,8%, 0,56, US$ 23,1. ChatGPT: VANILLA 44,4%, 0,06, US$ 0,10; EC 52,6%, 0,23, US$ 0,10; MEC (k = 3) 53,2%, 0,24, US$ 0,17; MEC (k = 6) 55,6%, 0,27, US$ 0,28; MEC + BPC 58,8%, 0,31, US$ 0,34; com HITLC (β = 20%) 71,3%, 0,52, US$ 18,3.
- **Leitura dos autores:** cada anotador humano tem boa correlação com a maioria; o GPT-4 se alinha mais aos humanos que o ChatGPT; as calibrações automáticas melhoram os dois (GPT-4 +9,8 pontos de acurácia, de 52,7% para 62,5%; ChatGPT +14,3, com kappa de 0,06 para 0,31); MEC (k = 3) + BPC (k = 3) supera MEC (k = 6) com o mesmo número de amostras, o que mostra que o ganho vem de equilibrar a posição, e não só de amostrar mais; com 20% de ajuda humana, o ChatGPT chega à acurácia média de um humano a US$ 18,3 em vez de US$ 30 (39% mais barato), e o GPT-4 a supera (73,8%).

## 5. Análises

- **Número de evidências e temperatura (Figura 4, ChatGPT):** o desempenho sobe com k e depois fica estável ou cai um pouco; k = 3 é o melhor custo-benefício. Temperatura baixa (0,2) tira a diversidade de que o MEC precisa, e alta (1,4) piora as gerações; 0,6 ou 1,0 funcionaram.
- **BPDE contra alternativas (Figura 5, ChatGPT; valores lidos no gráfico):** escolher para o humano pelos exemplos de maior BPDE supera a escolha aleatória e a entropia "vanilla" (calculada com seis resultados todos na mesma ordem, sem troca). Com 20% para humanos, cerca de 0,71 com BPDE, 0,675 com a entropia vanilla e 0,65 aleatório; com 50%, cerca de 0,87, 0,775 e 0,725. Para os autores, isso mostra de novo a sensibilidade à troca de posição e que os resultados do BPC melhoram a escolha do que vai ao humano.
- **Modelo de comparação direta (Tabela 5, ChatGPT; acurácia, kappa, taxa de conflito):** além do modelo de notas (SCORING), testaram um modelo que só pede "Assistente 1", "Assistente 2" ou "Igual" (COMPARING). Notas: VANILLA 44,4%, 0,06, conflito 82,5%; MEC 53,2%, 0,24, 35,0%; MEC + BPC 58,8%, 0,31. Comparação: VANILLA 50,2%, 0,18, conflito 50,0%; MEC 54,8%, 0,27, 42,5%; MEC + BPC 60,0%, 0,35. Os métodos funcionam nos dois modelos; a diferença de quase 6 pontos entre os VANILLA dos dois modelos, junto com o conflito alto, mostra a instabilidade, que a calibração reduz. A taxa de conflito não se aplica ao BPC, que já usa as duas ordens.
- **Por categoria (Figura 6):** o GPT-4 é bem melhor que o ChatGPT nas categorias complexas (senso comum, código, matemática); o MEC + BPC melhora os dois em quase todas as categorias, com ganho maior no ChatGPT nessas categorias complexas.

## 6. Limites e conclusão dos autores

- O viés de posição compromete seriamente a confiabilidade da avaliação; o arcabouço de três estratégias o reduz e aproxima o juiz dos humanos, a custo baixo.
- **Limite declarado:** não investigaram as causas do viés de posição nos LLMs.
- **Limites visíveis no desenho:** 80 perguntas, um par de modelos com rótulo humano (ChatGPT contra Vicuna-13B), anotadores que são os próprios autores, dois juízes da OpenAI de 2023; os números da Figura 2 e da Tabela 2 vêm de 80 pares por confronto.

## 7. Tudo o mais que ensina

- **Avaliação por item contra em par (seção de trabalhos relacionados):** a avaliação por item é mais conveniente e escala melhor; a em par dá resultados mais precisos (Zheng et al.), porque dar uma nota exata pede um padrão de pontuação detalhado e difícil de estabelecer, enquanto comparar é mais fácil e estável.
- **Métricas tradicionais:** BLEU, ROUGE, BERTScore e BARTScore não medem bem o alinhamento da resposta com a intenção humana (He et al. 2023).
- **Viés em redes neurais:** os autores situam o viés de posição na linha dos atalhos aprendidos dos dados (inferência textual, perguntas e respostas, ROC Story Cloze, inferência lexical, VQA, extração de informação); LLMs pré-treinados na web provavelmente aprendem vieses desses dados.
- **Custo da anotação humana:** US$ 30 por anotador para as 80 perguntas (salário mínimo americano perto de US$ 7,5 por hora, 3 minutos por exemplo).
- **Explicação antes da nota:** a justificativa para o EC é que, num modelo autorregressivo, só o que vem antes condiciona o que vem depois; nota dada antes da explicação não é sustentada por ela.

---
