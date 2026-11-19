# Ponto de corte, reuso do teste e desvio do critério, com poucos casos

Como se fixa um ponto de corte, o que reusar o teste para decidir faz com o resultado, quantos casos bastam e o que fazer quando se desvia do critério combinado, quando há poucos casos. Os casos artificiais estão em [[casos-artificiais-e-espectro]]; o limite inferior e o limiar com garantia, em [[camadas-de-avaliacao-o-que-melhora-cada-arranjo]].

Convenção: "leitura nossa" liga a fonte a um ambiente de agentes e não está na fonte. "Não verificado" é afirmação de resposta de buscador, sem primária aberta.

## A resposta curta

- **Corte é decisão com propósito declarado,** não descoberta, e métodos diferentes dão cortes diferentes.
- **Reusar o teste para decidir tende a sobreajustar:** Husain e Shankar dizem do dev, mesmo sem os exemplos no prompt, e Dwork mostra em dado sintético; Recht não acha o efeito em benchmark grande. A saída que a base dá é separar dev e teste, e pegar teste novo se contaminar.
- **Com poucos casos, as técnicas lidas não resolvem:** o holdout reusável depende de n, e a barra de erro da validação cruzada continua larga (leitura nossa, a partir de Dwork e Varoquaux).
- **Reduzir o que se ajusta** é a parte que se transfere a pergunta, estado e limiar (leitura nossa).
- **Desviar não anula necessariamente o teste.** Antes de ver o resultado, documentar basta; depois, relatar ajuda a avaliar, e o risco de viés sobe mesmo assim.
- **Sem resposta:** como ajustar a redação de uma pergunta com menos de 30 positivos.

## 1. Como se fixa um corte

[[2026-11-06-zieky-perie-livingston-2006-pontos-de-corte]] (ETS, exames educacionais): não há jeito perfeito; o corte expressa a opinião de quem julga, precisa ser validado e mudado se não servir. O primeiro passo é dizer para que ele existe: que decisão usa, como ela é tomada hoje, por que seria melhor com ele. Há métodos centrados no teste (Angoff) e nos casos reais (grupo limítrofe, grupos contrastantes). Grupos contrastantes têm a "strongest theoretical rationale" e são os únicos dos descritos que estimam os dois tipos de erro. A desvantagem é conseguir juízos de juízes bem treinados, e a meta razoável é "at least 100" por nível, "not a strict rule".

- **Métodos divergem:** Tappan e outros 2025 (citação, https://pmc.ncbi.nlm.nih.gov/articles/PMC12409087/; habilidade clínica): quatro métodos, cortes de 65,9% a 86,1%, aprovação de 60,9% a 98,9% em 92 alunos.
- **Da base:** *Guidelines for Designing and Using Decision Rules (Supplement to the Guidelines for the Use of Tests, AST-NIP 2024)*, de Susan Niessen e outros (Nederlands Instituut van Psychologen) (https://nip.nl/wp-content/uploads/pdfs/NIP_AST_2025_HANDLEIDING_ENG.pdf) traz quatro caminhos (corte existente, estatística direta, captura de política, opinião de especialistas) e não recomenda a estimativa própria.

## 2. Reuso do teste

**Da base:** [[2026-10-30-husain-shankar-faq-de-avaliacoes]]: cada uso do dev para mudar o prompt passa informação ao avaliador, mesmo sem os exemplos no prompt; havendo sobreajuste, repetir o desenvolvimento com teste novo e intocado. *How to Run Statistics over LLM Judges and Trust the Results: Calibrated Inference for Small-Sample AI Evaluation with evalstats*, de Ian Arawjo (https://arxiv.org/abs/2609.35815): ajustar nos itens rotulados "count as cheating, like p-hacking", até informalmente. [[2026-10-30-jev-as-a-judge-cascata]] congela protocolo e limiares antes de chamar.

**O que se mediu:**
- [[2026-11-06-dwork-2015-holdout-reusavel]]: reuso adaptativo leva a sobreajuste ao conjunto, com demonstração em experimento sintético; o Thresholdout limita isso, e a garantia depende de n.
- [[2026-11-06-recht-2019-imagenet-generaliza]] (novos testes de CIFAR-10 e ImageNet, 2.000 e 10.000 imagens): queda de 3% a 15% e de 11% a 14% no resumo, e "the relative order of models is almost exactly preserved". Atribuem a queda a imagens um pouco mais difíceis, sem excluir todas as variantes de sobreajuste. Outra escala, e nenhum dos dois mede o regime de poucos casos (leitura nossa).
- [[2026-11-06-cawley-talbot-2010-sobreajuste-na-selecao]] (JMLR, classificadores em benchmarks): sobreajustar o critério de seleção pode ter o tamanho da diferença entre algoritmos, e os autores estendem, como sugestão, a qualquer otimização num critério medido em amostra finita.
- **Relato fraco, em regime de poucos casos (aproximação nossa),** [[2026-10-31-wahi-juiz-nao-e-oraculo]] (autor único, execução única): calibrado por prompt em 15 diretórios, o juiz chegou a 80% de concordância exata com rótulos humanos; nos 54, que contêm esses 15 e têm 39 com rótulo de modelo, o mesmo prompt deu 51,9%. O autor chama de sobreajuste; o vão também mistura troca de gabarito (leitura nossa).

## 3. Como evitar com poucos casos

- **A regra da base:** separar dev e teste, manter o teste intocado.
- **Cawley e Talbot,** como sugestão sem medida naquela seção, sobre hiperparâmetros: o sobreajuste é pior com amostra pequena e muitos hiperparâmetros; saídas: regularizar, parar cedo, tirar a média ou "minimise the number of hyper-parameters". Avaliar sem viés pede protocolo mais rigoroso, como validação cruzada aninhada.
- **Prática no prompt do agente avaliado, Wahi:** holdout congelado, com subagentes vendo só o treino, e a curva do teste como monitor, não alvo. Abaixo de 20 casos ele pula o holdout, e com 4 a 8 segurados só vê falha grosseira.
- [[2026-11-06-varoquaux-2018-validacao-cruzada-em-amostra-pequena]] (comentário, neuroimagem, simulação e dados; preprint de 2017): com 100 amostras, barra de erro de cerca de ±10%; o erro padrão entre dobras a subestima; 50 divisões aleatórias de 20% dão barras só um pouco menores que deixar um de fora, e não resolvem; o holdout reusável, no artigo da Science de Dwork, não contorna o limite da amostra pequena.

**Quanto testar: não reconciliado.** Husain e Shankar dão meta, não piso: de 100 a 200 exemplos por modo de falha e, quando possível, de 30 a 50 Pass e de 30 a 50 Fail em dev e em teste, sem dizer o que fazer abaixo disso. Nas respostas de buscadores, **não verificadas:** uma prefere manter um teste trancado, mesmo pequeno; outra manda trancar, mas diz que reservar de 20% a 30% com N=40 traz duas vulnerabilidades; outra diz que abaixo de 50 casos pode ser inviável, e reserva 20% no fluxo final; outra diz que as divisões podem ficar pequenas demais, sem dar número.

**O limiar, por resposta de buscador, não verificado:** dentro da validação aninhada; dentro da validação cruzada, considerando a aninhada; sobre as previsões fora da dobra; fixo (numa resposta que o atribui a Cawley e Talbot, cujo artigo não fala de limiar).

**Sem resposta:** falta medida. Há receita em prompt (Wahi; Husain e Shankar), e as demais partem de um modelo que se retreina; num classificador por pergunta, o que se mexe é a pergunta, o estado e o limiar (leitura nossa).

## 4. Quantos casos

[[2026-11-06-negida-2019-tamanho-de-amostra-em-acuracia]] (CC BY-NC, integral na `url` da ficha) dá a fórmula, e a conta parte dos positivos, antes de dividir pela prevalência. Buderer 1996 (citação, https://doi.org/10.1111/j.1553-2712.1996.tb03538.x): depende da precisão pedida, da sensibilidade esperada e da prevalência, e amostra com prevalência diferente da população pode enganar. Negida chama W de largura máxima do intervalo; as contas abaixo o tratam como margem para cada lado, e fecham assim (leitura nossa).

Contas nossas, pela fórmula, com sensibilidade esperada de 0,85: W de 0,15, cerca de 22 positivos; de 0,10, cerca de 49; de 0,05, cerca de 196. Monti 2024 (citação, https://doi.org/10.1186/s41747-024-00474-w) lembra que a aproximação pede mais de cinco acertos e mais de cinco erros: com 22 positivos esperam-se cerca de 3,3 erros, fora da condição; com 49, cerca de 7,4. De 30 a 50 positivos dão cerca de ±0,13 a ±0,10.

| Positivos | Passar em 85% pede | Chance de passar com sensibilidade real de 0,70 | 0,85 | 0,95 |
|---:|---:|---:|---:|---:|
| 11 | 10 | 0,11 | 0,49 | 0,90 |
| 30 | 26 | 0,03 | 0,52 | 0,98 |
| 100 | 85 | 0,00 | 0,57 | 1,00 |

Conta nossa, binomial. Para o limite inferior de Wilson (bilateral de 95%) ficar acima de 0,85: 22 de 22; 43 de 45 (95,6%); 166 de 184 (90,2%).

## 5. Desvio do critério

- [[2026-11-06-nosek-2018-revolucao-do-preregistro]]: desviar é comum e "do not necessarily rule out" testar predições; antes de ver o resultado, documentar basta; depois, reportar ajuda a avaliar, e fica "increased risk of bias [...] even when changes are reported transparently".
- [[2026-11-06-claesen-2021-preregistro-e-desvios]] (Psychological Science, fev/2015 a nov/2017; dos 38 planos com selo, 27 passaram em acesso e detalhe mínimo): 2 sem desvio, 1 com todos declarados, 9 de 25 sem declarar nenhum.
- [[2026-11-06-lakens-2024-quando-e-como-desviar]]: nem todo desvio é problema; pode reduzir ou aumentar a severidade do teste, e o relato deve avaliar isso, em cinco categorias de motivo.
- [[2026-11-06-willroth-atherton-2024-relatar-desvios]] (CC BY-NC, integral na `url` da ficha): tabela com uma linha por desvio, com tipo, motivo, momento, texto original, descrição e efeito para o leitor, mais os passos não registrados. Vem da experiência delas, de modelos não publicados e de uma enquete com 34 editores. Depois de saber o resultado, não se atualiza o registro: relata-se o desvio.

## O que isto dá para quem testa um classificador com poucos casos (leitura nossa)

- **Diga antes que acerto muda a decisão e quantos positivos o teste precisa.** Um corte de acerto (85%, 75%) que não vem de método, sem a amostra necessária dita antes, mede pouco: com 11 positivos, passar ou não em 85% diz quase nada (tabela da seção 4). O primeiro passo do ETS, dizer para que o corte existe, é o primeiro passo de qualquer teste.
- **Grupos contrastantes** seriam a forma natural do caso real, e pedem bem mais casos do que costuma haver.
- **Hipótese medida numa metade já lida não é teste:** Dwork, Husain e Shankar e Arawjo dão o nome; separe dev e teste e registre quando o teste foi visto.
- **O critério escrito antes já é a prática de pré-registro.** Quando se desvia dele, registre o desvio e avalie o efeito no veredito, como Lakens pede, de preferência na forma da tabela de Willroth (uma linha por desvio).

## Ver também

[[casos-artificiais-e-espectro]]; [[desenho-de-rubrica-e-veredito]]; [[classificacao-como-portao]].
