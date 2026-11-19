---
titulo: "Spectrum bias in algorithms derived by artificial intelligence: a case study in detecting aortic stenosis using electrocardiograms"
tipo: paper
autor: "Andrew S. Tseng, Michal Shelly-Cohen, Itzhak Z. Attia, Peter A. Noseworthy, Paul A. Friedman, Jae K. Oh, Francisco Lopez-Jimenez"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC9707965/"
publicado_em: 2021-07-14
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [spectrum-bias, ai-diagnostics, electrocardiogram, aortic-stenosis, generalizability, overestimation, medical-ai, convolutional-network, decision-threshold]
licenca: "Creative Commons Attribution Non-Commercial 4.0 (CC BY-NC 4.0), escrita na própria página do PMC; pela cláusula NC (decisão de 2026-11-01) entra só a ficha, e o integral está na url (PMC9707965)"
---

# Tseng, Shelly-Cohen e colegas 2021 (Mayo Clinic, European Heart Journal: Digital Health): o viés de espectro medido num modelo de IA

Ficha em palavras próprias. Tseng e Shelly-Cohen (primeira autoria compartilhada) e colegas, Departamento de Medicina Cardiovascular da Mayo Clinic, European Heart Journal: Digital Health, 2021, 2(4):561-567, DOI 10.1093/ehjdh/ztab061, PMID 36713099; cardiologia e aprendizado de máquina. O integral não entra: está na url. Lida no texto do PMC em 2026-11-06, com as figuras 1 e 2 e o resumo gráfico nas imagens da mesma página.

## A pergunta

O viés de espectro aparece quando um teste nasce de populações com espectro de doença diferente do da população-alvo. O artigo pega um algoritmo real, um ECG (eletrocardiograma) lido por IA para detectar estenose aórtica (EA) grave, manipula o espectro da doença e mede o efeito sobre o desempenho. Citação da premissa: "use of an extreme spectrum of patients to derive and validate the test, even though a full spectrum exists".

**Motivação.** Muitos algoritmos de IA comparam doença evidente com controle normal. Exemplo dado: detectar autismo pelo rastreio do olhar, entre crianças normais e crianças com autismo evidente, deu acurácia de 89%, e outros hábitos de comportamento deram AUC (área sob a curva ROC) de 0,89 a 0,93. Esses estudos, pequenos, não avaliaram o espectro, e o teste poderia render menos numa população geral de crianças.

## Método, passo a passo

**Quem entra.** Adultos (18 anos ou mais) na Mayo Clinic (Minnesota, Arizona, Flórida), de janeiro de 1989 a setembro de 2019, com pelo menos um ecocardiograma transtorácico (ETT) com medida de EA (área da valva aórtica, gradiente médio, velocidade de pico ou índice de velocidade Doppler) e um ECG digital de 12 derivações até 180 dias antes dele. Com vários exames, ficou o primeiro ETT e o par com menor intervalo.

**Fluxo (figura 1).** 1.057.497 pares de ECG e ETT de 480.340 pessoas. Saem: cirurgia cardíaca prévia 8.021; medida faltando no laudo 83.219; prótese valvar 6.774; marca-passo 7.528; mais de 180 dias entre exames 90.780; discordância entre laudo clínico e medidas 13.242; traçado de ECG inválido 12.169. Ficam **258.607 pacientes (54%)**. Cirurgia prévia e prótese saem porque podem alterar o efeito da EA no ECG; marca-passo, porque o ritmo estimulado perturba a ativação elétrica normal.

**Rótulo.** EA grave se qualquer um destes: velocidade de pico de 4 m/s ou mais, gradiente médio de 40 mmHg ou mais, índice de velocidade Doppler abaixo de 0,25, área da valva abaixo de 1 cm². As impressões do médico no laudo, codificadas, reforçam o rótulo, e a discordância entre impressão e medida exclui o paciente.

**Graus da tabela 1.**

| Medida | Normal | Leve | Moderada | Grave |
|---|---|---|---|---|
| Área da valva, cm² | 2 ou mais | (1,5 a 2,0) | [1,0 a 1,5] | abaixo de 1,0 |
| Velocidade de pico, m/s | 2,5 ou menos | (2,5 a 3,0) | [3,0 a 4,0) | 4 ou mais |
| Gradiente médio, mmHg | 10 ou menos | (10 a 20) | [20 a 40) | 40 ou mais |
| Índice de velocidade Doppler | 0,5 ou mais | (0,35 a 0,5) | [0,25 a 0,35] | abaixo de 0,25 |

Parêntese exclui o número, colchete inclui.

**Os dois modelos.**

| Modelo | Positivo | Negativo | Treino (50%) | Validação (10%) | Teste (40%) |
|---|---|---|---|---|---|
| Espectro inteiro (whole-spectrum) | EA grave | EA moderada, leve ou nenhuma | 129.788 | 25.893 | 102.926 |
| Espectro extremo (extreme-spectrum) | EA grave | Nenhuma EA | 75.933 | 15.188 | 60.159 |

Para montar o extremo, saem do conjunto quem tem qualquer grau de insuficiência aórtica, insuficiência mitral ou estenose mitral, e quem tem EA leve ou moderada. Nenhum paciente caiu em mais de um grupo.

**Três conferências.**
1. **Análise mista:** o limiar de decisão do modelo extremo aplicado à coorte de espectro inteiro, simulando na população inteira um teste nascido de um espectro extremo.
2. **Tamanho:** como as coortes têm tamanhos diferentes, a inteira foi reduzida por sorteio ao número do extremo e reavaliada.
3. **O caminho inverso:** o modelo inteiro aplicado à coorte extrema. Se a perda aparece só no sentido extremo para inteiro, é provável um viés próprio do espectro, separado do mero uso de conjuntos reservados diferentes.

**O modelo.** Rede neural convolucional em Keras com TensorFlow, derivada de uma DenseNet menor, com 62 camadas convolucionais e 1 de classificação. Cada ECG vira uma matriz 12 × 5000 (12 derivações, 10 segundos, 500 Hz); os amostrados de 250 a 500 Hz são reamostrados com o SciPy. Otimizador Adam, entropia cruzada categórica, taxa de aprendizado 1e-3, lote de 64, afinados na validação interna; ficou o modelo de maior AUC na validação. A arquitetura vem de estudo anterior na mesma coorte, sobre EA moderada a grave. O limiar de positivo sai do índice de Youden na validação, e a nota final, só do teste.

**Estatística.** Qui-quadrado e t de Student para as características; curvas ROC do teste; intervalos de 95% pela aproximação de DeLong com a otimização de Sun e Xu. Comorbidades por códigos CID-9 e CID-10 antes do ECG e até 30 dias depois; um só código bastava.

## A amostra (tabela 2)

Idade média de 63 anos (DP 16,3), 122.790 mulheres (48%). EA grave confirmada em 2,6%. Os três conjuntos ficaram parecidos. No conjunto de teste (n = 102.926): sem EA 90.763 (88,1%); leve 8.330 (8,1%); moderada 1.225 (1,2%); grave 2.608 (2,5%). O texto dos resultados diz que esses 2.608 foram rotulados "AI-ECG-positive"; a tabela os traz como EA grave por medida. Comorbidades no teste: hipertensão 49,1%, doença pulmonar crônica 20,3%, insuficiência cardíaca 18,0%, diabetes 17,7%, doença vascular periférica 15,7%, doença renal 12,0%, doença cerebrovascular 11,5%, infarto 9,6%, doença do tecido conjuntivo 5,0%.

## Resultados (figura 2 e texto)

| Análise | Modelo | Coorte | Limiar | AUC | Sensibilidade | Especificidade |
|---|---|---|---|---|---|---|
| Espectro inteiro | inteiro | inteira | 0,01635 | 0,87 | 80% | 81% |
| Espectro extremo | extremo | extrema | 0,03074 | 0,91 | 84% | 84% |
| Mista | extremo | inteira | 0,03074 | 0,86 | 83% | 73% |

A legenda dos gráficos da figura 2 traz 0,875, 0,915 e 0,868. As AUCs valem nos grupos de validação e de teste, diz o texto.

- **Do espectro inteiro para o extremo:** os autores chamam a diferença de pequena e dizem que clinicamente ela pode não ser significativa.
- **Mista:** a AUC cai de 0,91 para 0,86, com a especificidade de 84% para 73% e a sensibilidade de 84% para 83%.
- **Inverso:** o modelo inteiro na coorte extrema não perdeu: AUC 0,88, contra 0,88 que o texto dá nesse trecho para o modelo inteiro na coorte inteira (em outros trechos, a mesma análise aparece como 0,87).
- **Coorte reduzida:** a mesma AUC de 0,87.

Conclusão deles sobre isso: a perda consistente sugere viés de espectro. Citação: "limiting datasets to clearly positive or negative labels leads to overestimation of test performance".

## Discussão

- **Por que o extremo rende mais.** Normal contra grave, em pacientes de demografia e comorbidades muito diferentes, é um problema binário bem mais fácil. Com as gravidades leve e moderada, a capacidade de distinguir EA grave cai.
- **Tamanho do efeito.** Os autores dizem que o efeito "may be modest in this example" e que o algoritmo segue robusto mesmo na análise mista. Por isso avaliam que talvez se possa usar clinicamente um modelo de espectro enviesado, sabendo que o desempenho será menor do que na validação original.
- **Como ler estudos assim.** O roteiro que os autores deixam para o clínico parte da pergunta de chegada, se o resultado vale para os meus pacientes, e a decompõe em três conferências:
  1. De onde o algoritmo saiu: a idade, o sexo e as comorbidades de cada grupo comparado, e se o artigo relata todas as variáveis que sabidamente mexem no resultado.
  2. Que tipo de variável está em jogo: há condições de sim ou não, como a gravidez, e há as que correm numa escala cortada por um limiar clínico ou arbitrário, caso da própria EA (de normal a grave). O cuidado com a escala vale também para qualquer variável de confusão contínua ou com resultado intermediário, como a fração de ejeção e o fluxo coronário.
  3. Se a condição tem espectro, o que a análise fez com ele.
- **Como reduzir.** Dos vários caminhos (o texto remete a duas referências), o artigo seguiu um comum: todos os graus de EA entram no treino e no teste. A aposta é que o modelo, exposto a uma amostra parecida com a clínica, onde os pacientes chegam misturados e não só nas pontas da gravidade, aprenda mais traços capazes de separar os rótulos e por isso generalize melhor.

## Limites declarados

- **Alcance.** O estudo demonstra um conceito num caso real e não prova o viés de espectro em outras áreas da IA ou outros cenários, o que os autores admitem; os números deste caso podem mudar com outro método de aprendizado de máquina, outro formato de entrada (numérico, gráfico), outra condição ou outra população. Desfechos clínicos, ou seja, a utilidade do teste para o paciente, ficaram fora da medida.
- **Os dois grupos.** No controle há gente com alteração estrutural importante, como fração de ejeção reduzida ou valvopatia relevante fora da aórtica, e um controle mais limpo poderia ter feito o viés medido sair maior. Do lado dos casos, a definição padronizada de EA grave pode ter deixado de fora um punhado de pacientes que não preenchiam os critérios; a resposta foi uma definição inclusiva, reforçada pela impressão final do médico no laudo.

## Tudo o mais que ensina

- **Frase de ineditismo:** dizem ser o primeiro estudo a demonstrar o efeito do viés de espectro num algoritmo de IA para EA grave por ECG.
- **Três ensinamentos que eles listam:** o impacto concreto nas medidas de desempenho; a importância de identificar variáveis de confusão; os primeiros passos para reduzir o efeito ao interpretar estudos.
- **Espectro de quê:** a EA tem heterogeneidade clínica dentro de cada grau, além da escala de normal a grave.
- **Exclusão extra no modelo extremo:** além da EA leve e moderada, o corte tirou as outras valvopatias citadas.
- **Prática de dados:** medidas de ETT em base própria da Mayo; pico e gradiente de todas as janelas de transdutor, para obter os maiores valores; área da valva pela equação de continuidade; ECG em aparelho Marquette (GE Healthcare), guardado no MUSE.
- **Uso anterior da mesma arquitetura:** rastrear disfunção contrátil do ventrículo esquerdo e estimar idade e sexo pelo ECG.
- **Conflito de interesse:** a Mayo licenciou a tecnologia à EKO, fabricante de estetoscópios digitais com eletrodos de ECG, e pode ganhar com isso, salvo no cuidado dos próprios pacientes; Friedman, Lopez-Jimenez e Attia também podem ganhar. Tseng, Shelly-Cohen e Oh sem conflito.
- **Dados:** por pedido razoável ao autor de correspondência.
- **Comitê de ética:** o da Mayo aprovou a dispensa do consentimento informado.

## O que a fonte não diz

O texto e a figura 2 não trazem os intervalos de confiança das medidas, embora o método diga que foram calculados. Não testa o modelo em dados de fora da Mayo. Não dá sensibilidade e especificidade da análise inversa nem da coorte reduzida.
