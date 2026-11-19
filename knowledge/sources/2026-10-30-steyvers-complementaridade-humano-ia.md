---
titulo: "Bayesian modeling of human–AI complementarity"
tipo: paper
autor: "Mark Steyvers, Heliodoro Tejeda, Gavin Kerrigan, Padhraic Smyth"
url: "https://doi.org/10.1073/pnas.2111547119"
publicado_em: 2022-03-11
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada no XML de texto completo do PMC, PMC8931210: 'This open access article is distributed under Creative Commons Attribution License 4.0 (CC BY)')"
areas: [agent-engineering]
tags: [human-ai-complementarity, human-in-the-loop, correlated-errors, ensemble, confidence-scoring, bayesian-modeling, model-heterogeneity]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. PNAS 119(11): e2111547119, publicado on-line em 11/03/2022 e no número de 15/03/2022 (recebido em 24/06/2021, aceito em 17/01/2022; editado por Terrence Sejnowski; "PNAS Direct Submission"). Universidade da Califórnia em Irvine (Ciências Cognitivas e Ciência da Computação). Versão lida: PMC8931210.1, pelo XML de texto completo da Europe PMC; as Figs. 3 e 4 foram lidas como imagem, do PMC. O SI Appendix (detalhes do modelo, prova do resultado teórico, resultados por ruído e por classificador) não foi aberto. Lida (camadas flexíveis de avaliação).

## A pergunta

Combinar previsões de vários classificadores de máquina diferentes, ou de grupos de pessoas, já se mostrou vantajoso, sobretudo quando os membros são diversos ou pouco correlacionados. Sabe-se menos sobre a combinação **híbrida** de pessoas e máquinas. Os autores constroem um modelo bayesiano que junta as classificações e as confianças de humanos e de máquinas, cada um com o seu jeito de exprimir confiança, para investigar quando há **complementaridade**: a combinação humano-máquina rende mais do que combinar só humanos ou só máquinas. Perguntas: vale mais misturar humano e máquina do que juntar dois humanos ou dois algoritmos? Quanto importa diferenciar os erros de cada um? Como juntar expressões de confiança qualitativamente diferentes?

O pano de fundo do texto: modelos de aprendizado profundo têm fraquezas sistemáticas e pontos cegos e falham de formas surpreendentes; trabalhos anteriores mostraram humano e máquina juntos melhores que cada um sozinho em reconhecimento facial, previsão esportiva, imagem diagnóstica e imagens astronômicas; em classificação de imagens, humanos e redes erram coisas diferentes mesmo com acurácia parecida. Classificação de imagens é escolhida como domínio de teste porque redes convolucionais (CNNs) e a visão humana têm semelhanças de representação, mas erram diferente.

## O modelo de combinação

- Trabalha com **pares** de classificadores ("classificador" é humano ou máquina): humano-máquina (HM), humano-humano (HH) e máquina-máquina (MM). Para cada imagem, as previsões do par viram uma previsão do par.
- O modelo estima a previsão combinada e a **correlação latente entre os classificadores**: a dependência entre as confianças dos dois (se um está confiante numa imagem, o outro tende a estar também). Essa correlação é estimada para cada tipo de par.
- Modelos anteriores supõem independência condicional forte ou saídas do mesmo tipo e não servem quando humano e máquina dão confianças de tipos diferentes. A máquina dá uma distribuição de probabilidade sobre todos os rótulos; ao humano não é prático pedir isso, então o humano dá **uma** confiança ordinal (baixa, média, alta) associada à sua escolha. As duas formas de confiança saem de processos geradores diferentes sobre as mesmas representações latentes.
- **Processo gerador (Eqs. 1 a 4):** N imagens, L rótulos possíveis, os dois classificadores tratados como rotuladores ruidosos em relação à verdade z_i. Para cada rótulo, uma normal bivariada gera os logits latentes do humano e da máquina, com média a quando o rótulo é o verdadeiro e b quando não é, variâncias σ² e correlação ρ_HM entre os dois. A diferença a − b é a capacidade de discriminar rótulos. Os logits viram probabilidades de confiança. Na máquina, essas confianças são observadas (a saída da CNN). No humano, são latentes: a escolha sai de uma softmax com temperatura τ (o ruído da decisão humana), e a confiança declarada sai de um probit ordenado sobre a confiança latente do rótulo escolhido, com limiares c e nitidez δ.
- Para pares MM, o humano das Eqs. 1 e 2 vira outra máquina e as Eqs. 3 e 4 não se usam; para pares HH, a máquina vira outro humano e as Eqs. 3 e 4 se aplicam a cada humano.

**Inferência:** a verdade é observada nas imagens de treino e latente nas de teste; rótulos e confianças humanas e probabilidades da máquina são observados em ambas. Cadeias de Markov Monte Carlo estimam a distribuição a posteriori dos rótulos verdadeiros de teste, da correlação ρ e dos demais parâmetros. Um único conjunto de parâmetros humanos vale para todas as pessoas, porque há poucas observações por pessoa; os autores dizem que o quadro pode ser estendido para diferenças individuais.

## O limite teórico da complementaridade

- Com dois humanos H1, H2 e duas máquinas M1, M2 (cada par permutável), há complementaridade se a acurácia de algum par humano-máquina passar a do par de humanos e a do par de máquinas. Sob "suposições brandas adicionais" (prova no SI Appendix), os autores derivam uma **condição necessária e suficiente** em função das acurácias individuais e das correlações.
- A acurácia do par (Eq. 5) é uma integral que depende de L e de uma variável r do par (Eq. 6): para pares não híbridos, r cresce com |a|/σ e cai com a correlação do par; para o par HM, depende de a_H, a_M e ρ_HM. Não tem solução analítica, mas a ordem das acurácias segue a ordem de r, então **complementaridade equivale a r_HM > máx(r_HH, r_MM)**.
- Pela Eq. 6: aumentar as correlações dos pares não híbridos (ρ_HH, ρ_MM) sempre baixa a acurácia desses pares e facilita a complementaridade. Aumentar a correlação híbrida ρ_HM **baixa** a acurácia HM se e só se mín(a_M/a_H, a_H/a_M) > ρ_HM; os autores leem que essas razões medem o desempenho relativo humano-modelo e que **correlação humano-modelo maior pode ajudar quando os dois têm níveis de desempenho muito diferentes**.

## Dados

- **Imagens:** 1.200 imagens únicas de 16 classes (cadeira, forno, faca, garrafa, teclado, relógio, barco, bicicleta, avião, caminhão, carro, elefante, urso, cachorro, gato, pássaro), um subconjunto da base do ImageNet Large Scale Visual Recognition Challenge 2012, com os rótulos originais como verdade. Para dificultar, ruído de fase em cada frequência espacial, uniforme em [−ω, ω], com quatro níveis (ω = 80, 95, 110, 125): 4.800 imagens.
- **Humanos:** 28.997 classificações de 145 participantes (cada um classificou 200 imagens nas 16 classes, com confiança baixa, média ou alta); pelo menos seis classificações humanas por imagem. O desempenho humano cai com o ruído e a acurácia varia com a confiança declarada.
- **Máquinas:** cinco CNNs pré-treinadas no ImageNet (AlexNet, DenseNet161, GoogleNet, ResNet152, VGG-19), cada uma em quatro variantes ajustadas ao ruído em graus diferentes (0 época, entre 0 e 1 época, 1 época, 10 épocas). Algumas VGG-19 e DenseNet161 ajustadas passam o desempenho humano nos ruídos altos.

## Resultados

**1. Humanos e máquinas erram coisas diferentes, mesmo com desempenho comparável (Fig. 2).** Há imagens difíceis para humanos e fáceis para máquinas (todos os seis humanos com confiança baixa, no máximo um acertou; pelo menos quatro de cinco máquinas acertaram) e o inverso (os seis humanos acertaram com confiança alta; no máximo uma de cinco máquinas acertou).

**2. Pares híbridos têm acurácia alta (Fig. 3, parte de cima).** Acurácia fora da amostra, validação cruzada em quatro partes, ruído baixo (ω = 80) e CNNs ajustadas por uma época. O texto diz que os pares HM rendem alto em relação a dois humanos ou duas máquinas, "especialmente para níveis altos de ruído" (resultados de outros ruídos no SI Appendix). Lido do gráfico, cerca de: um humano 0,90; dois humanos 0,915; máquinas sozinhas entre cerca de 0,77 (AlexNet) e 0,87 (VGG-19); pares HM entre cerca de 0,92 (com AlexNet) e 0,94 (com VGG-19); pares MM entre cerca de 0,82 e 0,88. **Exceção declarada:** o par de AlexNet com um humano nem sempre passa dois humanos; o desempenho de base baixo da AlexNet não produz complementaridade. Dois humanos passam um humano, o que os autores atribuem à confiança humana: quando discordam em confiança, o modelo infere que a escolha mais confiante tende a estar certa.

**3. Pares híbridos têm correlação latente baixa (Fig. 3, parte de baixo).** Média a posteriori de cerca de 0,4 nos pares HM, cerca de 0,7 nos HH e entre 0,65 e 0,75 nos MM: as previsões híbridas são mais independentes. As correlações das máquinas têm pouca incerteza (há confiança em todos os rótulos); as dos humanos, mais, porque há uma confiança só. O padrão de correlação não depende criticamente de como a confiança é representada: usar uma única confiança contínua (a do rótulo escolhido) e discretizar a confiança da máquina em poucas categorias ordinais, como a humana, não muda o padrão qualitativo (SI Appendix).

**4. A diferença de acurácia entre os dois limita a complementaridade (Fig. 4).** 320 comparações fora da amostra (quatro níveis de ajuste × quatro níveis de ruído × 20 pares de CNNs). A área prevista pela teoria, com ρ_HM = 0,33, ρ_HH = 0,62 e ρ_MM' = 0,71 (perto das correlações inferidas), é uma **faixa relativamente estreita**: humano e máquina precisam ter desempenho parecido para o par HM superar dois humanos e duas máquinas. O resultado depende fortemente da correlação humano-máquina: num cenário hipotético com ρ_HM = 0 (e as outras correlações iguais), a zona cresce (linha tracejada), mas mesmo esse melhor caso tem limites para a diferença de acurácia.

**5. Diferenciar erros e usar as confianças melhora o par HM (Tabelas 1 e 2).** Três fatores variados sistematicamente: um **modelo de erro por classe** (corrige erros e vieses de humano e máquina em rótulos específicos), a **confiança humana** e a **confiança da máquina**. Acurácia média sobre as cinco máquinas, cada valor com 36.000 observações, nos ruídos ω = 80, 95, 110, 125:

- com os três fatores: 0,933; 0,906; 0,850; 0,748
- sem nenhum: 0,895; 0,858; 0,769; 0,636
- só confiança da máquina: 0,925; 0,895; 0,830; 0,707
- só confiança humana: 0,903; 0,876; 0,815; 0,686
- só modelo de erro: 0,901; 0,872; 0,805; 0,674

Cada fator melhora o desempenho, sobretudo com ruído alto, e os efeitos são independentes. Na regressão logística (Tabela 2, 1.152.000 observações, efeitos em log-odds): intercepto 1,368; modelo de erro 0,101 (IC 0,091 a 0,110); confiança humana 0,104 (0,094 a 0,114); confiança da máquina 0,257 (0,247 a 0,266); todos com P < 0,001. A confiança da máquina pesa mais; segundo os autores, a diferença na forma de dar confiança "likely contributes" para isso: a máquina dá confiança em todos os rótulos ao mesmo tempo, o humano em um só, o da sua escolha. Confiança humana e modelo de erro contribuem quase o mesmo. Daí, segundo os autores, um jeito simples de melhorar o par HM é **pedir a confiança humana**.

## Discussão

- Mesmo quando um humano é melhor que a máquina, juntar a máquina a um humano pode render mais que juntar dois humanos; e o inverso: mesmo com a máquina melhor que humanos, um par HM pode passar a combinação de máquinas que, uma a uma, são melhores que um humano.
- Para algoritmos que ainda não chegam ao nível humano: partindo de um humano, acrescentar previsões algorítmicas menos precisas que ele pode valer mais que acrescentar outro humano. **A régua para avaliar um algoritmo não precisa ser o desempenho humano.** E um algoritmo que já passou o humano não torna o julgamento humano inútil no sistema híbrido.
- **Limites da complementaridade:** trabalhos anteriores mostram que sistemas híbridos nem sempre rendem mais. O fator limitante principal é a **correlação entre as previsões humanas e as da máquina**: correlação alta estreita a diferença de acurácia que ainda permite complementaridade. Para a IA usada como apoio à decisão: "Effective AI advice should not only be accurate but also be as independent as possible from human judgment." A independência pode crescer com mecanismos diferentes de previsão ou mudando a função objetivo do modelo. Os autores notam que reduzir a correlação com o humano vai na direção contrária da modelagem da inteligência natural, que busca imitar o processamento humano.
- **Confiança:** a confiança da máquina já foi usada em sistemas híbridos, a humana muitas vezes não é pedida; aqui ela aumenta o desempenho tanto quanto o modelo de erro por classe. As confianças permitem resolver, imagem a imagem, as habilidades diferentes de humano e máquina.
- Os autores apresentam o quadro como aplicável a muitos problemas de classificação com humanos e algoritmos, com possíveis aplicações de alto risco em medicina e justiça.

## Suposições e extensões que os autores mencionam

O resultado teórico vale sob "suposições brandas adicionais", discutidas no SI Appendix; o modelo usa um único conjunto de parâmetros para todos os humanos, e os autores dizem que ele pode ser estendido para diferenças individuais; o texto não tem seção própria de limitações.

## Financiamento e dados

NSF (prêmios 1900644 e 1927245) e Irvine Initiative in AI, Law, and Society; Kerrigan também pelo HPI Research Center in Machine Learning and Data Science da UC Irvine. Os autores declaram não ter conflitos de interesse. Código e dados no OSF (https://osf.io/2ntrf/).

---
