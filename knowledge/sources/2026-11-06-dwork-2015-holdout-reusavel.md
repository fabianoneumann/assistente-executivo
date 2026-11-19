---
titulo: "Generalization in Adaptive Data Analysis and Holdout Reuse"
tipo: paper
autor: "Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, Aaron Roth"
url: "https://arxiv.org/abs/1506.02629"
publicado_em: 2015-09-28
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [holdout-reuse, adaptive-data-analysis, overfitting, generalization, differential-privacy, description-length, max-information, thresholdout, sparsevalidate]
licenca: "licença não exclusiva do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/), indicada na página do resumo; entra só a ficha, e o integral está na url"
---

# Dwork et al. 2015 (arXiv): reusar o conjunto de teste em análise adaptativa sem sobreajustar a ele

Ficha em palavras próprias (o integral não entra; está na `url`). Dwork, Feldman, Hardt, Pitassi, Reingold e Roth, então na Microsoft Research, IBM Almaden, Google Research, Universidade de Toronto, Samsung Research America e Universidade da Pensilvânia. Lida a versão 2 do arXiv (25/9/2015, data de 28/9/2015 na primeira página; primeira submissão em 8/6/2015), 29 páginas, em aprendizado de máquina e teoria. Trabalho sobretudo teórico, com um experimento em dados sintéticos.

## A pergunta

O alvo é duplo: um problema prático, reusar o holdout (a parte dos dados guardada para testar) para validar quando a análise é adaptativa, e um geral, garantir que o resultado final de uma análise adaptativa generalize para a distribuição dos dados. A distância que motiva as duas é entre a teoria, que supõe amostra nova ou holdout novo para cada procedimento, e a prática, interativa, em que os mesmos dados voltam a ser usados e cada hipótese ou parâmetro sai do resultado das análises anteriores.

Esse reuso adaptativo aparece em toda parte, e os autores listam o ajuste de hiperparâmetros, o holdout de competições como a ImageNet, a seleção de atributos, a geração de aprendizes de base em boosting e bagging, a checagem de condição de parada e as decisões com analista no circuito. Em todos esses casos cai a condição que torna válida a estimativa no holdout, a de o preditor não depender dele, porque "in practice the holdout dataset is rarely used only once"; o efeito é sobreajustar ao próprio holdout. Corrigir pelos testes múltiplos só resolve no caso estático, em que a lista de hipóteses testadas é conhecida de antemão e independe do holdout. O estrago tem demonstração clássica no paradoxo de Freedman (1983): selecionar variáveis com t significativo e fazer a regressão só com elas, nos mesmos dados, declara relações que não existem.

## Dois algoritmos de holdout reusável

O analista faz o que quiser no conjunto de treino, mas só chega ao holdout por um algoritmo que controla o que ele vê.

### Thresholdout

Deriva as garantias da privacidade diferencial (critério que limita o quanto a saída de um algoritmo muda quando se troca um único elemento dos dados). Para cada função φ com valores em [0, 1], compara a média de φ no treino com a média no holdout. Em vez de devolver a média do holdout, revela pouco: se φ não sobreajustou ao treino, o analista recebe a média do próprio treino, ou seja, praticamente uma confirmação de um bit; se sobreajustou, recebe um valor com ruído calibrado.

Entradas: treino St, holdout Sh, limiar T, taxa de ruído σ, orçamento B. Passos da figura 1:

1. Sorteia γ de uma Laplace com parâmetro 2σ e faz T̂ = T + γ.
2. Para cada consulta φ: se B < 1, devolve ⊥ (para de responder). Senão, sorteia η de Laplace(4σ).
3. Se |média em Sh − média em St| > T̂ + η: sorteia ξ de Laplace(σ) e um novo γ, reduz B em 1, atualiza T̂ e devolve média em Sh + ξ.
4. Caso contrário, devolve a média em St.

O texto dá 0,01 como exemplo de T. A seção 1.1.1 diz que, no sobreajuste, volta a média no conjunto de treino com ruído; a seção 4.1 e o pseudocódigo devolvem a média no holdout com ruído.

Garantias, para dados independentes e identicamente distribuídos:

- **Privacidade (lema 23):** (2B/(σn), 0)-diferencialmente privado, e também (√(32B ln(2/δ))/(σn), δ) para qualquer δ > 0.
- **Amostra por consulta (lema 24):** erro de generalização menor que τ com probabilidade de pelo menos 1 − β se n ≥ max{2B/(στ), ln(6/β)/τ²} ou se n ≥ 80·√(B ln(1/(τβ)))/(τσ). O primeiro limite cresce linearmente com B, é mais simples e se estende a outras distribuições; o segundo tem dependência quadraticamente melhor em B e um pouco pior em τ.
- **Execução inteira (teorema 25):** com T = 3τ/4 e σ = τ/(96 ln(4m/β)), a probabilidade de existir uma resposta com erro de τ ou mais, enquanto o número de consultas que sobreajustaram ao treino por mais de τ/2 for menor que B, é no máximo β, desde que n seja da ordem de (ln(m/β)/τ²)·min{B, √(B·ln(ln(m/β)/τ))}.

Leitura dos autores desse limite: o termo ln(m/β)/τ² é, a menos de constante, o que m consultas não adaptativas já exigiriam; a tolerância τ escala como 1/√n, a menos do fator logarítmico; e m pode ser exponencial em n desde que B cresça abaixo de n² (B ≤ n^(2−c), com c > 0). "Naturally, the specific guarantees depend on the number of samples n in the holdout set."

A observação 26 traz duas variantes: as estimativas podem vir de outra fonte que não Sh, e há versão de um só lado, que pega apenas o caso em que o treino parece melhor que o real.

### SparseValidate

Parte de outra ideia: se quase sempre os procedimentos do analista não sobreajustam, validá-los revela pouco do holdout, porque a transcrição da interação cabe numa descrição curta. O analista escolhe qualquer função booleana do conjunto de dados (ou algoritmo que devolva um bit) e recebe o valor dela no holdout. Há dois orçamentos: m consultas no total e B consultas que retornaram 1. Esgotado qualquer um, acabam as respostas.

Exemplos de consulta: a acurácia de um preditor no holdout é de pelo menos α; rodar um algoritmo no holdout e ver se a hipótese se parece com a do treino; ver se as variáveis selecionadas no holdout se sobrepõem às do treino; ajustar uma mistura de gaussianas nos dois e comparar os parâmetros. Diferente do Thresholdout, a função não precisa ter faixa limitada.

Garantia (teorema 27): se cada consulta fixa tem probabilidade βi de dar 1, a consulta adaptativa i tem probabilidade de no máximo ℓi·βi, com ℓi = soma de j = 0 a min{i−1, B} das combinações de i tomadas j a j, que é no máximo m^B. Cabe ao analista gastar os orçamentos com economia e escolher consultas que raramente falhem. Com esse cuidado e parâmetros adequados, pode tratar o holdout como amostra nova para validar, e a falha indica sobreajuste. Diferença para o Thresholdout: SparseValidate não corrige o valor quando há sobreajuste. Uma saída é permitir valores em {0, 1, ..., L}, com L = ⌊1/τ⌋ para precisão τ, o que dá limite ℓi·L^min{B, i−1}·βi; os autores dizem que muitas vezes sai mais barato ter um conjunto separado só para obter as estimativas corretas.

## O enquadramento geral: análise como sequência

A análise adaptativa é vista como uma sequência A1 → A2 → ... → Am sobre o mesmo conjunto S, em que cada passo recebe S e as saídas anteriores. Os algoritmos podem representar as escolhas do analista, sem precisar estar especificados. Supõe-se que cada um generalize se executado numa amostra nova. A dependência das saídas anteriores, que dependem de S, é o que invalida essas garantias.

Há três caminhos:

- **Privacidade diferencial.** Compõe-se de forma adaptativa: uma sequência de algoritmos privados é privada, com parâmetros piores (teorema 3 soma ε e δ; teorema 4 dá limite melhor quando ε < 1), e o pós-processamento preserva a garantia (lema 5). Por corolário de trabalho anterior dos autores, qualquer saída de um algoritmo privado sobre dados independentes pode alimentar análises seguintes com risco de sobreajuste controlado (teorema 6, corolário 7; teorema 8, de Nissim e Stemmer, para privacidade aproximada e função com valores em [0, 1]).
- **Comprimento de descrição.** Se as saídas anteriores cabem em k bits, há no máximo 2^k entradas possíveis para o passo seguinte, e pela união dos eventos a falha é no máximo 2^k·β (teorema 9: |Y|·β). Hipóteses mais curtas revelam menos dos dados e por isso ajudam também no cenário adaptativo. O resultado não supõe nada sobre a distribuição dos dados.
- **Max-informação aproximada, a contribuição técnica principal.** Medida nova que unifica os dois: quanto o conhecimento da saída reduz, no pior caso, a incerteza sobre o conjunto de dados, em log. Propriedades: limita a probabilidade de eventos ruins (teorema 13: P[(S, A(S)) ∈ O] ≤ 2^k·P[S × A(S) ∈ O] + β); algoritmos privados têm pouca max-informação para qualquer distribuição (teorema 19: no máximo log e·εn), com limite melhor em dados independentes (teorema 20: log e·(ε²n/2 + ε√(n ln(2/β)/2))); saídas curtas também (teorema 17: log(|Y|/β)); compõe-se de forma adaptativa, somando k e β (lema 14, teorema 15); sobrevive ao pós-processamento (lema 16). Os limites vindos da privacidade valem só para a privacidade pura (δ = 0). Informação mútua não bastaria para garantir que eventos ruins tenham probabilidade ínfima: com informação mútua k, a probabilidade pode chegar a k/(2 log(1/δ)).

Privacidade e comprimento de descrição são incomparáveis entre si: descrição curta não basta para privacidade, que impede revelar até poucos bits sobre um indivíduo, e privacidade não limita o comprimento da saída. Como consequência da composição, dá para misturar passos privados e passos de saída curta na mesma análise, e a privacidade passa a controlar a generalização para além de dados independentes.

## Trabalhos relacionados

- O trabalho anterior (Dwork et al., 2014) iniciou o estudo formal, com consultas estatísticas escolhidas de forma adaptativa, e a ligação entre privacidade e generalização foi reforçada depois (Bassily et al., 2015; Nissim e Stemmer, 2015).
- Há métodos para responder exponencialmente muitas consultas adaptativas, mas não eficientes, e isso tem razão de fundo: Hardt e Ullman (2014) e Steinke e Ullman (2014) provam que, sob hipóteses criptográficas, nenhum algoritmo eficiente responde mais que quadraticamente muitas consultas estatísticas escolhidas por um adversário que conhece a distribuição.
- A abordagem clássica (dimensão VC e medidas de complexidade) dispensa a preocupação com adaptatividade se a amostra garante generalização para toda a classe; os autores querem limites sem supor a classe de funções.
- Noções de estabilidade do algoritmo são necessárias e suficientes para generalizar, mas não se compõem; a max-informação se compõe.
- Inspirados neste trabalho, Blum e Hardt (2015) mostraram como manter um placar confiável em competições, com a técnica de comprimento de descrição (o Ladder).

## O experimento

**Desenho.** Dados sintéticos com d = 10.000 atributos e conjunto S de tamanho 2n, com n = 10.000, dividido ao meio em treino e holdout. O analista calcula a correlação de cada atributo com o rótulo nos dois conjuntos, fica com os que têm o mesmo sinal e módulo de pelo menos 1/√n nos dois, pega os k de maior correlação no treino, e monta um classificador linear que soma os atributos selecionados pelo sinal da correlação. Mede a acurácia no treino e no holdout. Compara-se com um conjunto novo de tamanho n, tirado da mesma distribuição. Média e desvio de 100 execuções independentes.

**Thresholdout do experimento.** Difere do analisado na teoria: T = 0,04 e τ = 0,01, abaixo do que a prova exige, e ruído gaussiano em vez de Laplace. Os autores dizem que os valores da prova não se destinam a aplicação direta e que estes bastam para evitar o sobreajuste neste experimento.

**Sem correlação entre atributos e rótulo.** Atributos N(0, 1), rótulo sorteado por igual, logo nenhum classificador passa de 50% de acurácia real. Com holdout comum, a acurácia relatada passa de 63% em k = 500, no treino e no holdout, com desvio do erro abaixo de 0,5%. Na figura 2, o holdout comum sobe até encostar no treino, cerca de 0,63 em k = 500, e o conjunto novo fica em cerca de 0,50 em todo k. Com Thresholdout, o treino sobe a cerca de 0,69, o holdout relatado fica em cerca de 0,51, e o conjunto novo em cerca de 0,50. O relato pode errar em até 0,04 quando treino e holdout estão a menos de 0,04 um do outro, por causa de T.

**Com correlação em parte dos atributos.** 20 atributos vêm de N(y·0,06, 1), onde y é o rótulo; os demais de N(0, 1). Na figura 3, o conjunto novo tem pico em cerca de 0,60, perto de 20 variáveis, e cai a cerca de 0,52 em k = 500, nos dois casos. Com holdout comum, treino e holdout terminam em cerca de 0,65. Com Thresholdout, o treino vai a cerca de 0,70 e o holdout relatado fica um pouco acima do conjunto novo, em cerca de 0,535 em k = 500. Segundo os autores, o método evita o sobreajuste e ainda acha padrões verdadeiros.

**Acurácia real no holdout com Thresholdout (figura 4).** O número que o Thresholdout relata tem a vantagem de poder alimentar novas decisões com menos risco, e a figura 4 confere se ele engana: medida de fato, a acurácia do classificador no holdout fica em cerca de 0,51 no caso sem correlação e em cerca de 0,535 em k = 500 no caso com correlação, o que os autores leem como praticamente nenhum sobreajuste ao holdout.

**Por que acontece, nas palavras deles.** Antes do holdout reusável, dizem, "the only known safe approach was to collect a fresh holdout set each time a function depends on the outcomes of previous validations"; o método proposto abre outro caminho, que vale além deste experimento. Mesmo no cenário simples dele, o Thresholdout evita o sobreajuste sem precisar do procedimento especializado que a literatura tem para procedimentos fixos de dois passos. Validação cruzada e bootstrap, por sua vez, não seriam saída, pois o classificador final continuaria treinado e validado nos mesmos dados. A origem do problema no holdout comum está no reuso: o analista volta a ele depois de já tê-lo usado para medir a correlação de cada atributo.

## Limites e o que fica em aberto, segundo os autores

- As garantias valem para dados independentes e identicamente distribuídos no caso do Thresholdout, e dependem de n, B, m, τ e β.
- Os valores do experimento ficam abaixo dos exigidos pela prova.
- É preciso mais trabalho empírico para saber quando e como aplicar a teoria em cada cenário.
- Pergunta teórica aberta: mesmo só para reusar um holdout no cálculo de predicados booleanos, é possível garantia melhor que a já alcançada por privacidade diferencial?
- O único experimento relatado usa n = 10.000 em dados sintéticos.

## Tudo o mais que ensina

- **Definição de sobreajuste na análise adaptativa:** a variável aleatória S entregue ao passo i deixa de ser amostra independente, porque as saídas anteriores dependem dela.
- **McDiarmid (lema 1):** função de sensibilidade c tem P[f − μ ≥ α] ≤ exp(−2α²/(n·c²)). A média de φ com faixa de comprimento α tem sensibilidade α/n.
- **Aplicações da max-informação à concentração (corolários 21 e 22):** um algoritmo τ/(cn)-privado que produz função c-sensível tem P[f(S) − média ≥ τ] ≤ exp(−3τ²/(4c²n)), quando τ²/(c²n) passa de uma constante.
- **Comprimento de descrição aleatorizado (apêndice A):** é o comprimento k que vale para cada fixação dos bits aleatórios do algoritmo. Também implica generalização (teoremas 29 e 30). Baixa max-informação permite construir outro algoritmo, estatisticamente próximo, com descrição curta (lema 31, teoremas 32 e 33), mas isso não é a recíproca do teorema 30: define um algoritmo novo e exige conhecer a distribuição marginal da saída.
- **Responder consultas por comprimento de descrição (apêndice B):** uma versão sem ruído do Median Mechanism de Roth e Roughgarden mantém os conjuntos pequenos consistentes com as respostas, responde pela mediana deles e só usa os dados quando a mediana erra por mais de 2α; cada rodada dessas corta os candidatos pela metade, o que limita o número delas e a descrição total. Com τ = 3α, erra menos de τ com probabilidade 1 − β se n ≥ 81·log|X|·log m·ln(3m/τ)/(2τ⁴) + 9 ln(2m/β)/(2τ²). A dependência em m é polilogarítmica, ganho exponencial sobre avaliar as consultas diretamente; o algoritmo não é eficiente e os limites são comparáveis aos da privacidade pura.
- **Exemplo de causas sutis de sobreajuste:** os autores remetem a "Clever methods of overfitting", de Langford (2005).
