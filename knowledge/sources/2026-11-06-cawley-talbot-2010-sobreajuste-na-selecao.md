---
titulo: "On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation"
tipo: paper
autor: "Gavin C. Cawley, Nicola L. C. Talbot"
url: "https://www.jmlr.org/papers/volume11/cawley10a/cawley10a.pdf"
publicado_em: 2010-07
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [model-selection, overfitting, selection-bias, performance-evaluation, nested-cross-validation, hyperparameters, bias-variance, kernel-methods, benchmarks]
licenca: "JMLR, sem licença aberta conferida: '© 2010 Gavin C. Cawley and Nicola L. C. Talbot' na primeira página do PDF; entra só a ficha, e o integral está na url"
---

# Cawley e Talbot 2010 (JMLR): sobreajustar o critério de seleção e o viés que isso traz à avaliação

Ficha em palavras próprias (o integral não entra; está na `url`). Cawley e Talbot, Universidade de East Anglia. Journal of Machine Learning Research, volume 11, páginas 2079 a 2107, submetido em 10/2009, revisado em 3/2010, publicado em 7/2010; editora Isabelle Guyon. Área: aprendizado de máquina, com classificadores de kernel em benchmarks sintéticos e do repositório UCI.

## A pergunta e a tese

Selecionar modelo costuma ser otimizar numericamente um critério, em geral um estimador do desempenho, como a validação cruzada em k dobras. O erro do estimador tem viés e variância. Costuma-se elogiar a ausência de viés; os autores mostram que variância baixa importa ao menos tanto, porque uma variância não desprezível abre espaço para sobreajuste também na seleção.

Duas afirmações empíricas, que declaram ser a novidade do artigo (os métodos usados não são novos): o sobreajuste nesse segundo nível de inferência pode prejudicar muito o desempenho, e pode criar um viés otimista em protocolos de avaliação comuns. Os efeitos costumam ter "comparable magnitude to differences in performance between learning algorithms". Embora estudem seleção por validação cruzada, os autores estendem os achados a qualquer seleção por otimização de um critério medido em amostra finita, inclusive evidência bayesiana e limites de desempenho.

**Vocabulário.** Parâmetros são ajustados no treino (laço interno). Hiperparâmetros são ajustados pelo critério de seleção (laço externo). Sobreajuste na seleção é continuar minimizando o critério além do ponto em que a generalização deixa de melhorar e passa a piorar.

## Classificador e dados

**KRR (Kernel Ridge Regression, regressão ridge com kernel), também chamado LS-SVM.** Modelo linear num espaço induzido por kernel, com função de perda de mínimos quadrados regularizada. Usa kernel gaussiano RBF, com o parâmetro η, e um parâmetro de regularização λ; o ajuste de parâmetros é um sistema linear. Serve bem por ser simples e permitir validação cruzada deixando um de fora em forma fechada. O critério é a estatística PRESS (soma dos quadrados dos resíduos deixando um de fora), otimizada por Nelder-Mead ou gradiente conjugado.

**Benchmark sintético.** Baseado em Ripley: quatro gaussianas bivariadas esféricas com variância 0,04, duas por classe. Erro de Bayes (o mínimo possível) de cerca de 12,38%. Como o gerador é conhecido, dá para medir o erro verdadeiro e ter dados à vontade. Com 4.096 amostras e hiperparâmetros ajustados no erro verdadeiro, o modelo ARD chega a 12,50%, então a forma do modelo não é o problema.

**Treze benchmarks de Rätsch et al. (2001)** (tabela 1). Cada um com 100 partições predefinidas, 20 em `image` e `splice`:

| Conjunto | Treino | Teste | Atributos |
|---|---|---|---|
| banana | 400 | 4.900 | 2 |
| breast cancer | 200 | 77 | 9 |
| diabetis | 468 | 300 | 8 |
| flare solar | 666 | 400 | 9 |
| german | 700 | 300 | 20 |
| heart | 170 | 100 | 13 |
| image | 1.300 | 1.010 | 18 |
| ringnorm | 400 | 7.000 | 20 |
| splice | 1.000 | 2.175 | 60 |
| thyroid | 140 | 75 | 5 |
| titanic | 150 | 2.051 | 3 |
| twonorm | 400 | 7.000 | 20 |
| waveform | 400 | 4.600 | 21 |

## Sobreajuste na seleção, demonstrado

**Experimento 1 (figura 2).** Mil realizações de 64 amostras do benchmark sintético, kernel ARD (uma escala por atributo), validação cruzada em quatro dobras. O erro de validação cai sempre ao longo das iterações; o erro verdadeiro cai no começo e, depois de cerca de 30 a 40 iterações, volta a subir devagar. É a mesma curva clássica do sobreajuste em treino. Numa realização específica, o estrago foi grande, e parar antes teria ajudado.

**Viés e variância (figura 3).** Deixar um de fora é quase sem viés, e isso costuma ser citado como vantagem. Para selecionar, o que importa é que o mínimo do critério numa amostra indique o mínimo do erro verdadeiro. Um critério sem viés e com variância alta espalha o mínimo conforme a amostra; um critério com viés e variância baixa pode ser melhor. A figura é hipotética, construída para ilustrar.

**Experimento 2 (figuras 4 a 8).** Treino fixo de 256 padrões, KRR com RBF, grade de hiperparâmetros, taxa de erro suavizada com γ = 8.

- Com 100 conjuntos de validação de 64 padrões, a média do erro lembra o erro verdadeiro: o estimador por divisão simples é aproximadamente sem viés.
- Em cada conjunto de validação, a superfície fica irregular e às vezes com mais de um mínimo, e os hiperparâmetros escolhidos dependem da amostra. Seis realizações vão de modelos muito subajustados a muito sobreajustados.
- O erro de validação é fortemente enviesado depois de minimizado, e os autores dizem que não deve servir para estimar desempenho.
- Com 256 padrões de validação em vez de 64, os hiperparâmetros se concentram em torno do ótimo e os erros verdadeiros têm menos valores extremos. Aumentar a validação é a forma direta de reduzir a variância.

**Partição única engana (figura 9).** Em `banana`, com 100 realizações, o KLR (regressão logística com kernel) ganha do GPC (classificador de processo gaussiano) em 36, embora o GPC seja melhor na média (sem diferença significativa) e vença as outras 64; avaliado numa só daquelas 36, o KLR pareceria superior. Duas regras saem disso. Uma é de escala: diferença entre algoritmos menor que a variação trazida pela amostragem dos dados dificilmente importa na prática, mesmo significativa, porque juntar mais dados provavelmente renderia mais que acertar o classificador. A outra é de método: toda avaliação deve usar várias partições.

**Em dados reais (tabelas 2 e 3).** O RBF é caso particular do ARD, então o ARD nunca poderia ser pior no ótimo.

- KRR com PRESS, por Wilcoxon, em negrito na tabela 2: RBF significativamente melhor em 7 conjuntos (breast cancer, diabetis, german, heart, ringnorm, twonorm, waveform), ARD em 1 (image), sem diferença significativa em 5. O ARD tem PRESS significativamente menor em 11 dos 13, e assim um critério melhor com erro de teste pior.

| Conjunto | Erro RBF | Erro ARD | PRESS RBF | PRESS ARD |
|---|---|---|---|---|
| breast cancer | 26,727 ± 0,466 | 28,766 ± 0,391 | 70,632 ± 0,328 | 66,789 ± 0,385 |
| heart | 16,730 ± 0,359 | 22,810 ± 0,411 | 42,576 ± 0,356 | 37,023 ± 0,494 |
| ringnorm | 1,613 ± 0,015 | 2,750 ± 0,042 | 28,324 ± 0,246 | 27,680 ± 0,231 |
| waveform | 9,792 ± 0,045 | 11,836 ± 0,085 | 61,658 ± 0,596 | 56,424 ± 0,637 |
| image | 2,990 ± 0,159 | 2,188 ± 0,134 | 74,056 ± 1,685 | 44,488 ± 1,222 |

- EP-GPC (classificador de processo gaussiano por propagação de expectativa) com evidência bayesiana, tabela 3: RBF melhor em 8 (banana, breast cancer, diabetis, german, heart, ringnorm, twonorm, waveform), ARD em 3 (flare solar, image, splice), sem diferença em 2. O ARD tem evidência significativamente melhor nos 13. Exemplo: em `ringnorm`, erro de 4,406 contra 8,589 e −log evidência de 121,260 contra 91,356. Os autores concluem que sobreajustar a evidência também é problema prático.

Razão dada: o ARD tem bem mais hiperparâmetros, logo mais graus de liberdade para explorar peculiaridades da amostra. Conclusão: pode ser problema importante na prática, "especially where there are many hyper-parameters or where only a limited supply of data is available".

## Como evitar o sobreajuste na seleção

Seção 4.4, formulada como sugestão ("It seems reasonable to suggest") e sem medida própria. O raciocínio é por analogia com o treino: o risco existe sempre que se otimiza direto um critério medido numa amostra finita e cresce, como no treino, com poucos dados e muitos hiperparâmetros a ajustar; sem como conseguir mais dados, os remédios também seriam os do treino. A lista junta esses aos que fogem da seleção:

- **Os remédios do treino:** regularizar o critério (Cawley e Talbot, 2007), parar cedo (Qi et al., 2004) e tirar a média de modelos ou de hiperparâmetros (Cawley, 2006; Hall e Robinson, 2009).
- **Menos hiperparâmetros:** os autores sugerem reduzir quantos hiperparâmetros há; o exemplo é tratar os do kernel como parâmetros comuns, otimizados no primeiro nível, e deixar um só hiperparâmetro de regularização.
- **Nenhuma seleção, por dois caminhos:** a via totalmente bayesiana, que integra os hiperparâmetros em vez de otimizá-los, preferida dos autores quando a amostra é muito pequena; ou ensembles como Random Forest, que não são panaceia, porque em modelos hierárquicos costuma ser mais fácil embutir conhecimento especializado.

Os autores pedem mais análise teórica, porque a que existe ajuda pouco: os resultados assintóticos não tratam deste caso, Bengio e Grandvalet (2004) mostraram que não há estimador não enviesado da variância da validação cruzada em k dobras, e há só limites por estabilidade.

## O viés na avaliação de desempenho

O princípio: "treat both training and model selection together", como partes do ajuste, sem separá-las em nenhum ponto da avaliação. Rever a seleção a cada nova amostra.

**Protocolo interno, sem viés.** A seleção é refeita em cada realização, dentro de cada dobra. Três classificadores (RBF-KRR com PRESS; RBF-KLR com aproximação de deixar um de fora da log-verossimilhança; EP-GPC isotrópico com verossimilhança marginal). Tabela 4: postos médios de 1,9231 (KRR), 2 (GPC) e 2,0769 (KLR), sem superioridade significativa. Os autores não se surpreendem, porque os modelos têm estrutura parecida e diferem na seleção.

**Protocolo da mediana, com viés (Rätsch et al., 2001, adotado por vários estudos).** Faz seleção só nas 5 primeiras realizações e usa a mediana dos hiperparâmetros em todas. Foi razoável pelo custo da época; os autores dizem que os experimentos deste artigo rodaram numa única estação Linux. Três fontes de viés: parte dos dados de teste foi vista na seleção; a mediana reduz a variância; com hiperparâmetros fixos, some o espaço para sobreajustar à amostragem de cada partição.

Viés da mediana no KRR, em pontos percentuais de erro, como diferença entre interno e mediana (tabela 5):

| Conjunto | Interno | Mediana | Viés |
|---|---|---|---|
| banana | 10,610 ± 0,051 | 10,384 ± 0,042 | 0,226 ± 0,034 |
| breast cancer | 26,727 ± 0,466 | 26,377 ± 0,441 | 0,351 ± 0,195 |
| diabetis | 23,293 ± 0,169 | 23,150 ± 0,157 | 0,143 ± 0,074 |
| flare solar | 34,140 ± 0,175 | 34,013 ± 0,166 | 0,128 ± 0,082 |
| german | 23,540 ± 0,214 | 23,380 ± 0,220 | 0,160 ± 0,067 |
| heart | 16,730 ± 0,359 | 15,720 ± 0,306 | 1,010 ± 0,186 |
| image | 2,990 ± 0,159 | 2,802 ± 0,129 | 0,188 ± 0,095 |
| ringnorm | 1,613 ± 0,015 | 1,573 ± 0,010 | 0,040 ± 0,010 |
| splice | 10,777 ± 0,144 | 10,763 ± 0,137 | 0,014 ± 0,055 |
| thyroid | 4,747 ± 0,235 | 4,560 ± 0,200 | 0,187 ± 0,100 |
| titanic | 22,483 ± 0,085 | 22,407 ± 0,102 | 0,076 ± 0,077 |
| twonorm | 2,846 ± 0,021 | 2,868 ± 0,017 | −0,022 ± 0,014 |
| waveform | 9,792 ± 0,045 | 9,821 ± 0,039 | −0,029 ± 0,020 |

Em `breast cancer`, `german`, `heart` e `thyroid`, o viés supera a diferença típica entre classificadores no protocolo sem viés. Comparando EP-GPC e RBF-KLR no interno com RBF-KRR na mediana, o Wilcoxon a 95% dá KRR como superior, com postos 1,2308, 2,3846 e 2,3846. Os autores chamam essa diferença de "entirely spurious". Interno e mediana não são comparáveis entre estudos.

**O viés não vem só do reuso de amostras (figura 11).** Cem replicações no sintético, cada uma com 100 treinos de 64 padrões e teste de 4.096, todos disjuntos. Mesmo sem reuso, o viés otimista da mediana é altamente significativo (Wilcoxon, p < 0,001). Sobra a redução de variância como causa.

**Nem é coerente por dentro.** Só com a mediana (tabela 6), os postos são 1,5385 (KRR), 2,2308 e 2,2308, sem diferença significativa por Friedman, mas o viés favorece muito o KRR. Na comparação direta do viés entre RBF-KRR e RBF-EP-GPC (tabela 7), o Wilcoxon fica abaixo de 0,05 em 5 dos 13 conjuntos (banana, diabetis, heart, ringnorm, twonorm). Os autores sugerem que o protocolo talvez devesse ser abandonado.

**Favorece o pior critério (figura 14).** KRR com divisão repetida 9:1, variando o número de dobras para controlar a variância. No protocolo interno, com cinco dobras ou menos, o KRR vai mal por sobreajuste; com mais dobras, os três se igualam. Na mediana, a redução de variância esconde o mau desempenho com poucas dobras.

**Protocolo externo, outro viés.** Seleção feita uma vez em todos os dados, às vezes como "estudo preliminar", e depois avaliação em repartições com hiperparâmetros fixos. Parece inofensivo, mas os hiperparâmetros guardam "memória" dos dados que viraram teste. Tabela 8, validação cruzada de 10 dobras, KRR com RBF:

| Conjunto | Externo | Interno | Viés |
|---|---|---|---|
| banana | 10,355 ± 0,146 | 10,495 ± 0,158 | 0,140 ± 0,035 |
| breast cancer | 26,280 ± 0,232 | 27,470 ± 0,250 | 1,190 ± 0,135 |
| diabetis | 22,891 ± 0,127 | 23,056 ± 0,134 | 0,165 ± 0,050 |
| flare solar | 34,518 ± 0,172 | 34,707 ± 0,179 | 0,189 ± 0,051 |
| german | 23,999 ± 0,117 | 24,217 ± 0,125 | 0,219 ± 0,045 |
| heart | 16,335 ± 0,214 | 16,571 ± 0,220 | 0,235 ± 0,073 |
| image | 3,081 ± 0,102 | 3,173 ± 0,112 | 0,092 ± 0,035 |
| ringnorm | 1,567 ± 0,058 | 1,607 ± 0,057 | 0,040 ± 0,014 |
| splice | 10,930 ± 0,219 | 11,170 ± 0,280 | 0,240 ± 0,152 |
| thyroid | 3,743 ± 0,137 | 4,279 ± 0,152 | 0,536 ± 0,073 |
| titanic | 22,167 ± 0,434 | 22,487 ± 0,442 | 0,320 ± 0,077 |
| twonorm | 2,480 ± 0,067 | 2,502 ± 0,070 | 0,022 ± 0,021 |
| waveform | 9,613 ± 0,168 | 9,815 ± 0,183 | 0,203 ± 0,064 |

Viés otimista nos 13 e significativo (maior que duas vezes o erro padrão) em todos, exceto `splice` e `twonorm`, mesmo com só dois hiperparâmetros. Conclusão dos autores: não deve ser usado na prática.

**O que usar.** Avaliação sem viés provavelmente pede protocolo mais rigoroso e caro, como validação cruzada aninhada, ou "double cross" (Stone, 1974). Em vez de avaliar algoritmos isolados, comparar combinações de algoritmo e procedimento de seleção. Também pede várias bases, muitas partições aleatórias e seleção em cada tentativa; é automatizável, e o processamento paralelo o torna mais viável.

## Conclusões dos autores

Alta variância leva a sobreajuste na seleção mesmo com poucos hiperparâmetros. Protocolos adotados em estudos publicados podem introduzir viés sério. O sobreajuste na seleção parece superável pelos métodos já eficazes no treino. A seleção deve ser parte integrante do ajuste e rodar de forma independente em cada tentativa, o que também reflete a boa prática em uso real.

## Limites e lacunas

- A demonstração é com classificadores de kernel e, em parte, com benchmark sintético.
- As saídas da seção 4.4 são sugestões, sem medida naquela seção; os autores não comparam as saídas entre si.
- A extensão a qualquer critério em amostra finita é afirmação geral, com evidência própria só em validação cruzada, divisão simples e evidência bayesiana.
- Inconsistências do texto: a legenda da figura 12 fala em RBF-KLR na mediana, enquanto o diagrama e o texto falam em RBF-KRR; a legenda da tabela 5 fala em três classificadores, e ela traz só o KRR.
- O artigo não trata de escolha de limiar de decisão.

## Tudo o mais que ensina

- **"Robusto" aqui** significa insensível a fatores experimentais irrelevantes, como a amostragem e a partição dos dados, e em geral se obtém por reamostragem cara.
- **Validação cruzada em k dobras** dá estimativa com leve viés pessimista do desempenho do modelo treinado na amostra inteira.
- **Analogia com seleção de atributos:** o viés é análogo ao de Ambroise e McLachlan (2002) em microarranjos, quando se selecionam genes antes de avaliar, e tem solução parecida.
- **Ajuste do GPC:** EP-GPC parte de hipóteses estatísticas mais fortes, então brilha quando elas valem e vai mal com modelo mal especificado (`ringnorm`); os critérios por validação cruzada são mais pragmáticos, com precisão mais constante.
- **Software:** toolbox GKM, em MATLAB, de domínio público, citado pelos autores.
- **Diagrama de diferença crítica** (Demšar, 2006): mostra o posto médio dos classificadores em várias bases e liga por barra os estatisticamente parecidos. Demšar recomenda o Wilcoxon de postos sinalizados para comparar dois classificadores em várias bases.
