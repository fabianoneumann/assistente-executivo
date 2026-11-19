---
titulo: "The spectrum effect in tests for risk prediction, screening, and diagnosis"
tipo: paper
autor: "Juliet A. Usher-Smith, Stephen J. Sharp, Simon J. Griffin"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC4916916/"
publicado_em: 2016-06-22
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [spectrum-effect, spectrum-bias, diagnostic-accuracy, prevalence, sensitivity, specificity, likelihood-ratio, case-control, external-validity, simulation]
licenca: "Creative Commons Attribution (CC BY 3.0), escrita na própria página do PMC; o integral está na url"
---

# Usher-Smith, Sharp e Griffin 2016 (BMJ): por que o desempenho de um teste muda de uma população para outra

Ficha em palavras próprias, em estrutura própria. Usher-Smith (Primary Care Unit, Universidade de Cambridge), Sharp e Griffin (MRC Epidemiology Unit, Cambridge), The BMJ, 2016, 353:i3139, DOI 10.1136/bmj.i3139, PMID 27334281; artigo de análise em medicina e epidemiologia, sem encomenda, com revisão por pares externa. Usa exemplos da literatura e simulações. Lida no texto e nas figuras da página do PMC em 2026-11-06. O apêndice suplementar com o detalhe das simulações (PDF) não foi lido: o PMC, o BMJ e o Europe PMC não o entregaram por download direto.

## Definições

**Efeito de espectro** (spectrum effect): a variação, entre subgrupos e ambientes, do desempenho de testes de predição, rastreamento e diagnóstico. Os autores preferem esse nome a "viés de espectro" (spectrum bias), usado ainda hoje na literatura, por refletir melhor que a variação é da natureza do teste. A origem é Ransohoff e Feinstein, 1978, que observaram que estudos com uma faixa estreita demais de pessoas, com ou sem a doença, podem representar mal o desempenho na prática; eles discutiram o espectro de pacientes sem usar o termo.

**As medidas, no quadro 1:**
- Sensibilidade: chance de teste positivo em quem tem a doença.
- Especificidade: chance de teste negativo em quem não tem.
- Valor preditivo positivo: chance de ter a doença com teste positivo; valor preditivo negativo: chance de não ter com teste negativo.
- Razão de verossimilhança positiva (LR+): sensibilidade / (1 − especificidade). Negativa (LR−): (1 − sensibilidade) / especificidade.
- Área sob a curva ROC (AUROC): chance de o classificador pôr acima uma pessoa doente sorteada em relação a uma não doente sorteada.

A razão de verossimilhança multiplica a chance pré-teste e dá a chance pós-teste, que se converte em probabilidade. Que o valor preditivo varia com a prevalência é sabido; que sensibilidade, especificidade e razão de verossimilhança também variam, dizem os autores, é bem descrito e mesmo assim costuma passar despercebido por médicos e formuladores de política.

## O mecanismo

Sensibilidade, especificidade e razões de verossimilhança só não dependem da prevalência e da distribuição da doença em dois casos: doença de fato dicotômica, ou teste perfeito, e chance igual de erro de classificação em doentes e não doentes. Isso raramente acontece, por duas razões que se somam:

1. **A condição costuma ser um contínuo**, do claramente ausente ao claramente presente, medido ou não.
2. **Todo teste erra**, de três maneiras: erro simples de medida (glicose plasmática no rastreamento de diabetes tipo 2, D-dímero na suspeita de trombose venosa profunda ou embolia pulmonar); erro subjetivo, quando a categoria vem de relato do paciente, sintomas, exame físico, imagem ou lâmina que profissionais leem de modos diferentes (adenoma avançado na colonoscopia, mamografia); e covariáveis não medidas, porque poucos marcadores são exclusivos de uma doença, e o falso positivo vem de condições vizinhas (o peptídeo natriurético tipo B ajuda no diagnóstico de insuficiência cardíaca, mas também sobe na insuficiência renal e na hipertensão pulmonar).

Daí: **quem está perto do ponto de corte erra mais.** O efeito sobre o desempenho geral depende de quantas pessoas estão perto do corte, logo da prevalência e da composição da amostra.

## A simulação

Há uma variável contínua X, com valor para cada pessoa; a doença existe se X passa de um limiar. X pode ser um traço (glicose de jejum verdadeira, limiar de 7,0 mmol/L para diabetes; pressão sistólica verdadeira, 150 mm Hg para hipertensão) ou um risco verdadeiro (risco cardiovascular em 10 anos, limiar de 10% na Inglaterra e no País de Gales, recomendado pelo NICE para oferecer estatina). O X verdadeiro é desconhecido; o teste dá uma estimativa Z, por medida ou por modelo. A simulação varia a distribuição de X. Nas figuras, a doença está presente se X ≥ 7.

**Cenário 1: muda a média de uma distribuição normal, com o limiar fixo.** Figura 1, com prevalências de exemplo de 2,3% e 49,6%. Quando a prevalência cai, LR+, LR− e especificidade sobem e a sensibilidade cai, com mudança de 10 vezes nas razões de verossimilhança e variação de 30% em sensibilidade e especificidade. No gráfico, de prevalência perto de zero a perto de 100%, a sensibilidade vai de cerca de 70% a cerca de 100%, e a especificidade faz o caminho inverso. Equivale a aplicar o teste em outro nível de atenção.

**Cenário 2: uma distribuição bimodal de X, em que muda a proporção de gente acima do limiar, de pequena a quase metade.** Figura 2, com prevalências de exemplo de 17,1% e 41,1%. Com mais gente doente, menos doentes ficam perto do limiar e menor é o risco de erro entre eles; nesta distribuição, a sensibilidade sobe (no gráfico, de cerca de 70% a cerca de 98%, conforme a prevalência vai de poucos por cento a 40%), a LR− cai e a especificidade fica quase parada, em cerca de 98%. Como os valores ficam mais espalhados e há menos gente perto do limiar do que no cenário 1, o desempenho é melhor com a mesma prevalência:

| Com 20% de prevalência | Sensibilidade | Especificidade |
|---|---|---|
| Cenário 1 (normal) | 85% | 95% |
| Cenário 2 (bimodal) | 98% | 99% |

O cenário 2 pode aparecer num estudo que tira doentes e não doentes de populações diferentes, como um caso-controle com casos do hospital e controles da comunidade.

## O que o efeito faz na prática

**Regra geral dos pontos-resumo:** teste desenvolvido onde a doença é mais frequente, ou o risco é maior, tende a mostrar sensibilidade menor e especificidade maior ao ir para onde ela é menos frequente.

- **Do hospital ao posto de saúde:** um procedimento criado na atenção secundária, entre suspeitos, tende a perder sensibilidade e ganhar especificidade como rastreamento na atenção primária.
- **O filtro de encaminhamento, no sentido inverso:** teste de diabetes pensado para rastrear pessoas sem sintomas, avaliado na rotina da atenção primária, onde o médico testa primeiro quem tem sintoma ou fator de risco, mostra especificidade menor e sensibilidade maior do que na população em que foi criado. Se o teste foi feito para esse grupo de alto risco, a abordagem é adequada.
- **Estágio e gravidade:** quanto mais avançada a condição nos afetados, maior a separação na medida entre quem tem e quem não tem, e melhor o teste parece. Exemplo hipotético: teste de gravidez avaliado numa clínica de pré-natal, entre grávidas e amigas ou parentes muito provavelmente não grávidas, parece melhor do que na comunidade, onde há gestações muito iniciais.

**Evidência empírica citada.** Uma revisão de 23 meta-análises de acurácia (Leeflang e colegas, CMAJ, 2013) achou associação estatisticamente significativa entre prevalência e sensibilidade ou especificidade em uma de cada três revisões; na análise agrupada, a especificidade caía entre 0,1% e 0,5% a cada ponto percentual de aumento da prevalência. Moons e colegas (1997): teste de esforço para doença coronariana com LR+ de 3,8 em pessoas com pressão sistólica de 141 a 240 mm Hg e de 17,0 naquelas com 100 a 140 mm Hg. Os autores dizem que essas diferenças são comuns e podem ser grandes a ponto de influir na prática clínica, mesmo fora do caso-modelo do limiar contínuo.

## Recomendações

**Para quem desenvolve e avalia.**
- O ideal, como nos modelos prognósticos, é usar duas coortes, uma para desenvolver e outra para avaliar, com ampla variedade de estados de doença e características da população. Isso permite explorar o efeito e evita superestimar o desempenho com uma amostra que não representa a população mais ampla.
- Não sendo possível, e usando caso-controle, a amostra deve ser o mais parecida possível com a população em que o teste será usado.

**Para quem relata, em qualquer caso.** Dados suficientes para avaliar o efeito: o STARD pede descrever os participantes, inclusive a distribuição de gravidade; relatar a variabilidade da acurácia entre leitores, centros ou subgrupos e a reprodutibilidade do teste.

**Como examinar subgrupos.**
- Estratificar pela característica e aplicar um teste χ² simples de associação.
- Construir curvas ROC por subgrupo e compará-las pela razão crítica (a diferença das áreas dividida pelo desvio padrão da diferença, comparada a uma distribuição normal).
- Usar modelagem logística, como lembram Mulherin e Miller, que estima desempenho em grupos pequenos, aceita características multicategóricas ou contínuas e modela à parte o que afeta sensibilidade e especificidade.

**Para quem compara e decide.**
- Cuidado ao comparar testes desenvolvidos em populações diferentes, por métodos diferentes. Exemplo de comparação imprópria: sensibilidade e especificidade de um teste novo, validado em caso-controle na atenção secundária, contra as de um programa nacional de rastreamento.
- Médicos e gestores devem conferir o quanto a amostra do estudo se parece com a sua população.
- Citação da regra: "Ideally new tests should be developed and evaluated using data from the population(s) in which they are intended to be used".
- Se não for possível, calcular o valor preditivo só corrige em parte a diferença de prevalência, e o ganho de saúde esperado com o teste deve ser lido com cautela.

## O exemplo do quadro 2 (hipotético)

O Dr B, na atenção primária, avalia um teste novo para infecção bacteriana em quem tem sintomas respiratórios altos. A prevalência assumida na atenção primária é de cerca de 10%. O quadro liga os valores do primeiro relato à figura 2B e os do segundo à figura 1B. Com os dois relatos publicados:

| Relato | Desenho | Sensibilidade | Especificidade | Com teste positivo, chance de infecção bacteriana |
|---|---|---|---|---|
| Primeiro | Caso-controle: 40 pacientes com infecção de um ambulatório de otorrino e 60 controles do ambulatório de ortopedia do mesmo hospital | 97% | 97% | 78% |
| Segundo | Transversal, na população geral, com prevalência de 10% | 72% | 92% | 50% |

## Tudo o mais que ensina

- **Em que o valor preditivo se apoia:** como é a razão de verossimilhança que leva da chance pré-teste à pós-teste, e ela varia com o espectro, ajustar pela prevalência não resolve tudo.
- **Situações de corte:** o limiar pode vir de uma decisão clínica (o de 10% de risco cardiovascular decide estatina), e X pode ser risco em vez de traço, então o raciocínio vale para escores de predição.
- **O gráfico do cenário 1, em escala logarítmica:** com prevalência perto de 100%, 1/LR− passa de 100 e a LR+ cai a cerca de 3; com prevalência perto de zero, a LR+ fica em cerca de 20.
- **O gráfico do cenário 2:** a LR+ fica estável, entre cerca de 20 e 30, em prevalências de 2% a 40%, e o inverso da LR− sobe de cerca de 3 para mais de 30.
- **Financiamento e conflitos:** Usher-Smith com bolsa do National Institute of Health Research, Sharp pelo Medical Research Council; independentes dos financiadores; sem conflitos declarados. Os autores agradecem a discussão com Gary Abel.

## O que a fonte não diz

Não traz estudo próprio com pacientes: os números de sensibilidade e especificidade são de simulação ou de exemplo hipotético, e os empíricos são citados de outros. Não diz quanto cada população precisaria se parecer com a do uso para o efeito ficar pequeno.
