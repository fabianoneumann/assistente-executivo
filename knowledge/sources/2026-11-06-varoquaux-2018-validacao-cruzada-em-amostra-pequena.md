---
titulo: "Cross-validation failure: small sample sizes lead to large error bars"
tipo: paper
autor: "Gaël Varoquaux"
url: "https://arxiv.org/abs/1706.07581"
publicado_em: 2017-06-23
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [cross-validation, small-samples, error-bars, confidence-intervals, standard-error, reusable-holdout, vibration-effects, overfitting, neuroimaging, publication-bias]
licenca: "licença não exclusiva do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/), indicada na página do resumo; entra só a ficha, e o integral está na url"
---

# Varoquaux (arXiv 2017, preprint para a NeuroImage): validação cruzada com amostra pequena dá barra de erro grande

Ficha em palavras próprias (o integral não entra; está na `url`). Gaël Varoquaux, INRIA Saclay e CEA/Neurospin, França. Lida a versão 1 do arXiv (23/6/2017), que traz "Preprint submitted to NeuroImage June 26, 2017", na seção "Comments and Controversies", 10 páginas, em neuroimagem. Código das simulações em `github.com/GaelVaroquaux/cross_validation_failure`. O texto lido não traz a data de publicação na revista.

## A pergunta

A validação de modelos preditivos em imagens do cérebro depende da validação cruzada: testar em dados independentes dos usados para ajustar. O autor quer chamar a atenção para as barras de erro dessa medida, em geral subestimadas. Afirma que os erros observados são inerentes a poucas amostras, e que isso afeta sobretudo o desenvolvimento de métodos e os estudos de diagnóstico entre sujeitos; os estudos de neurociência cognitiva sofrem menos, por terem muitas tentativas e sujeitos. Para modelos preditivos, as exigências de amostra são maiores que na estatística usual, em parte porque não há grande tamanho de efeito para compensar.

O foco é classificação balanceada de duas classes, com acaso em 50%. Erro de validação cruzada: a diferença entre a acurácia medida e a esperada em dados novos.

## Quatro evidências

As barras são os percentis 5 e 95 da distribuição do erro, escolhidos por corresponderem ao limiar de 0,05. Os números abaixo são rótulos das figuras, para as duas estratégias: LOO (deixar um de fora, ou deixar uma sessão ou um sujeito de fora) e 50 divisões aleatórias com 20% para teste.

**a. Neuroimagem real (figura 1a).** Resultado de Varoquaux et al. (2017), com os dados divididos duas vezes: um conjunto de decodificação, onde corre a validação cruzada, e um de validação, tão grande quanto ele, para comparar. Desvantagem: a acurácia verdadeira não é conhecida, só estimada.

| Dados | LOO | 50 divisões, 20% |
|---|---|---|
| fMRI dentro do sujeito, cerca de 212 amostras | −21%, +18% | −24%, +13% |
| fMRI entre sujeitos, cerca de 241 amostras | −10%, +10% | −10%, +8% |
| MEG, cerca de 199 amostras | −16%, +14% | −13%, +10% |

O autor resume: as barras vão a pelo menos 10% para cada lado, seja qual for a estratégia (a figura traz +8% na linha entre sujeitos, com divisões).

**b. Competição pública (figura 1d).** Kaggle, diagnóstico de esquizofrenia por ressonância: 144 sujeitos, 86 para treino, teste público de 30 e privado de 28. A diferença entre as duas notas vai de −15% a +14%. Como nenhum dos dois é padrão-ouro, o autor supõe erro dividido entre eles, com margem de cada medida menor por um fator de dois.

**c. Simulação simples (figura 1b, apêndice C).** Duas gaussianas, amostras independentes, SVM linear com C = 1, separação ajustada para 75% de acurácia. Compara a validação cruzada com a acurácia em 10.000 amostras novas, 1.000 repetições. Vantagem: mostra o erro verdadeiro.

| Amostras | LOO | 50 divisões, 20% |
|---|---|---|
| 30 | −20%, +18% | −19%, +15% |
| 100 | −10%, +10% | −10%, +8% |
| 200 | −7%, +7% | −7%, +5% |
| 300 | −6%, +6% | −5%, +4% |
| 1.000 | −3%, +3% | −3%, +2% |

Com 100 amostras, reproduz o que se vê nos dados reais.

**d. Lei binomial, o melhor caso (figura 1c).** O modelo mais simples é jogar moeda n vezes com probabilidade p, a acurácia, aqui 75%. Observações independentes, sem variabilidade do treino do classificador.

| Amostras | Limites |
|---|---|
| 30 | −15%, +12% |
| 100 | −7%, +7% |
| 200 | −5%, +5% |
| 300 | −4%, +4% |
| 1.000 | −2%, +2% |

Dados reais têm correlação entre amostras e confundidores, que reduzem os graus de liberdade. Por isso os erros seguem a ordem: neuroimagem acima da simulação, simulação acima da binomial.

**Preditor perfeito (apêndice E).** Para descartar instabilidade do modelo, repete com um classificador independente dos dados: as duas estratégias dão cerca de −10% a −11% e +8% com 100 amostras, −6% e +5% a +6% com 300, e ±3% com 900. O texto diz que o resultado é muito parecido com o do SVM treinado e atribui a variabilidade ao ruído de amostragem do teste; LOO e divisões dão o mesmo erro.

**Tamanho das amostras no campo (figura 2).** Histograma de cinco revisões mais os 100 primeiros resultados no PubMed para "fmri decoding": 642 estudos, com mediana de 89 amostras.

## A regra de bolso

"Confidence bounds" esperados para classificação binária, resumindo experimentos e simulações (tabela 1):

| Amostras | 30 | 100 | 300 | 1.000 |
|---|---|---|---|---|
| Limites | ±15% | ±10% | ±6% | ±3% |

Em situações adversas, como observações correlacionadas ou classificadores muito instáveis, podem ser bem maiores.

Para outras acurácias esperadas, limites de 5% e 95% da binomial, um limite inferior do erro real (tabela A1):

| Acurácia esperada | 30 amostras | 100 amostras | 300 amostras |
|---|---|---|---|
| 10% | 3,3% a 20,0% | 5,0% a 15,0% | 7,3% a 13,0% |
| 25% | 13,3% a 40,0% | 18,0% a 32,0% | 21,0% a 29,0% |
| 50% | 36,7% a 63,3% | 42,0% a 58,0% | 45,3% a 54,7% |
| 75% | 60,0% a 86,7% | 68,0% a 82,0% | 71,0% a 79,0% |
| 90% | 80,0% a 96,7% | 85,0% a 95,0% | 87,0% a 92,7% |

Os limites apertam perto de 0% e de 100%, onde a distribuição fica assimétrica.

## Erro padrão entre dobras subestima

Medir a dispersão da acurácia entre dobras é a saída simples, mas otimista, porque as previsões não são independentes entre dobras (Bengio e Grandvalet, 2004). A variância entre dobras dá "a false sense of security". Na simulação, usando 1,64 vezes o erro padrão da média (SEM) como limite unilateral de 95% (apêndice D, figura A4):

| Estratégia | Amostras | SEM | Empírico |
|---|---|---|---|
| LOO | 30 | ±13,8% | ±18,9% |
| LOO | 100 | ±7,4% | ±10,3% |
| LOO | 300 | ±4,1% | ±5,9% |
| LOO | 1.000 | ±2,2% | ±2,9% |
| 50 divisões, 20% | 30 | ±3,4% | ±15,3% |
| 50 divisões, 20% | 100 | ±2,0% | ±8,1% |
| 50 divisões, 20% | 300 | ±1,1% | ±4,1% |
| 50 divisões, 20% | 1.000 | ±0,6% | ±2,1% |

A fórmula subestima por um fator de 0,73 no LOO e 0,26 nas 50 divisões (no corpo do texto: 0,7 no melhor caso). Divisões repetidas têm dobras mais correlacionadas, e a fórmula, que ignora isso, erra mais.

**O que ajuda.** Teste de permutação dá bom controle estatístico (Stelzer et al., 2013). Busca do autor no Google Scholar sugere uso em cerca de 30% das publicações de MVPA e 15% dos estudos de decodificação por fMRI. Pelas contagens dele, 15.500 resultados para "fmri decoding" contra 2.380 com "permutation"; 2.360 para "fmri mvpa" contra 728.

**Repetir divisões.** Nota 2: 50 divisões de 20% dão "slightly smaller error bars" que deixar um de fora e podem custar bem menos em conjuntos grandes. O autor recomenda preferir essa estratégia, e diz que ela não resolve o problema da barra grande.

## Efeitos de vibração

Com estatística de alta variância, as escolhas de método mudam muito o resultado, e a chave é a razão entre o efeito e a variação por escolhas analíticas (Ioannidis, 2008).

**Experimento (figura 3).** Dados de Haxby et al. (2001), primeiro sujeito, rosto contra lugar, com rótulos invertidos em uma sessão a cada duas, de modo que a acurácia esperada é 50%. Quase 50 combinações: SVM ou regressão logística, seleção de 100 a 2.000 voxels ou nenhuma, suavização de 2, 4 ou 6 mm.

| Sessões | Amostras | Faixa de acurácia entre os pipelines |
|---|---|---|
| 4 primeiras | cerca de 72 | 25% a 39% |
| 4 últimas | cerca de 72 | 40% a 71% |
| 6 primeiras | cerca de 108 | 38% a 57% |
| 6 últimas | cerca de 108 | 47% a 57% |
| todas as 12 | cerca de 216 | 44% a 52% |

Sem sinal nenhum, alguma escolha chega a 71%. A média também muda entre subconjuntos, o que o autor atribui a não estacionariedade, como flutuação de atenção, ou a ruído de amostragem de observações muito correlacionadas.

## Implicações para o campo, segundo o autor

**Porta aberta a sobreajuste e viés de confirmação.** Quanto maior a variância da medida, mais escolhas arbitrárias melhoram artificialmente o resultado, e isso não se transfere a dados novos. O remédio padrão é um grande teste independente, difícil onde a coleta é cara. Ensaios clínicos usam análise cega, com parte dos rótulos oculta ao estatístico. Publicar só resultados significativos filtra a literatura, infla efeitos e justifica o viés de confirmação.

**Acurácia relatada cai com a amostra (figura 4).** Meta-análise das revisões: a acurácia típica é maior em estudos pequenos. O autor considera que a soma de variância e filtro de publicação poderia explicar isso, e que heterogeneidade não controlada em coortes grandes também poderia. A exceção são os estudos de depressão, sem nenhuma amostra grande.

**Validação cruzada segue crucial.** O autor a chama de "the best tool available", mesmo sem ser solução mágica, por ser o único método não paramétrico de testar generalização. Abordagens bayesianas dependem das hipóteses do modelo e não medem previsão em dados novos. BIC, AIC e MDL dependem de hipóteses e de muito mais observações que parâmetros.

## Recomendações do autor

- **Compartilhar e juntar dados, mesmo heterogêneos.** OpenfMRI (63 estudos, 2.200 sujeitos) e Neurovault (26.000 mapas). Cerca de 30.000 estudos de fMRI por ano, muitos com dados novos e alguma sobreposição. Exemplo: Wager et al. (2013) separaram dor física de dor social e calor. Heterogeneidade complica, mas biomarcadores muito ligados a um local têm pouco valor clínico. Abraham et al. (2017) e Dansereau et al. (2017): com muitos locais, prever entre locais foi tão bom quanto entre sujeitos do mesmo local.
- **Cuidado com o vazamento.** Com várias sessões por sujeito, não deixar sessões do mesmo sujeito em treino e teste, para que a identidade do sujeito não comande a previsão (Saeb et al., 2017).
- **Paradigmas que facilitem muitos dados.** Localizadores padronizados, estímulos naturalistas, ressonância em repouso, em geral ao custo de menos controle fino da cognição.
- **Em neuroimagem cognitiva, concluir no grupo.** Testar significância no nível do grupo mesmo com validação cruzada por sujeito (Stelzer et al., 2013), ou prever entre sujeitos.
- **Em desenvolvimento de métodos, testar em vários conjuntos** (Demšar, 2006). "I personally believe that this is the only sound way of doing methods development." Ele admite que nem sempre trabalhou assim e que alguns resultados promissores dele não se confirmaram (Michel et al., 2012, não se reproduziu em outros conjuntos, embora a ideia de agrupar voxels tenha se validado depois).
- **Limitar as combinações de análise:** quem desenvolve métodos deve dar recomendações gerais validadas em muitos conjuntos.

Conclusão: o problema "will not be fixed by better classifiers or cross-validation approaches". As soluções estariam em amostras maiores ou análises pré-registradas. Não é problema novo nem exclusivo da área: Braga-Neto e Dougherty (2004) perguntaram se a validação cruzada vale para microarranjos em amostra pequena.

## O holdout reusável

"Improvements on cross-validation such as the reusable holdout (Dwork et al., 2015) cannot circumvent intrinsic limitations of small samples." O apêndice A.1 explica, citando o artigo da revista Science de 2015, "The reusable holdout: Preserving validity in adaptive data analysis": a técnica reusa um holdout com uma perturbação (jitter) na medida do erro quando ela fica abaixo de um limiar, o que evita sobreajustá-lo, sem corrigir a incerteza intrínseca da medição. Embute essa incerteza no procedimento e se recusa a concluir além de um limiar ligado aos intervalos de confiança. Para certo controle de generalização, o limiar deve ser proporcional a √n. O autor chama de melhora bonita, alinhada ao ponto principal dele. Não dá número mínimo de amostras para o método.

## Limites

- Comentário centrado em neuroimagem e em classificação de duas classes; a tabela 1 é uma estimativa de ordem de grandeza.
- Os números de 75% e 50% de acaso são os dos experimentos; para outras acurácias, o apêndice dá só a binomial, como limite inferior.
- O autor sugere causas para a queda de acurácia com amostra (filtro de publicação, heterogeneidade) sem separá-las.
- As contagens de permutação vêm de busca por palavras e são aproximadas.
- O apêndice C descreve as gaussianas em 100 dimensões, e a legenda da figura A3 fala em 300 atributos.
- O artigo não trata de escolha de limiar de decisão.

## Tudo o mais que ensina

- **Vocabulário do campo:** decodificação (prever a condição a partir da imagem), MVPA (análise de padrões multivoxel), searchlight, biomarcador.
- **Relação com "power failure":** o autor liga os efeitos à falta de poder estatístico de Button et al. (2013), mais severa em teste de modelos preditivos.
- **Só acerto ou erro por observação:** o problema vem de o teste discriminante medir só sucesso ou falha por observação.
- **Limiar bilateral:** o texto usa 1,64 SEM para o limite de 95%, e 1,96 SEM se o teste for bilateral (nota 8).
- **Jitter na técnica de Dwork:** conforme a nota 7, ocorre quando erros de treino e teste estão muito próximos, porque preditores bem ajustados têm erros próximos nos dois.
- **Generalizar importa ao diagnóstico e à ciência em geral:** o foco em explicação muito controlada pode limitar a generalidade (Yarkoni e Westfall, 2016).
- **Custos da coleta em neuroimagem:** cansaço e habituação limitam dados por sujeito, e escanear muitos sujeitos pode passar do orçamento típico de um projeto.
