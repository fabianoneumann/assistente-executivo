---
titulo: "Sample Size Calculation Guide - Part 4: How to Calculate the Sample Size for a Diagnostic Test Accuracy Study based on Sensitivity, Specificity, and the Area Under the ROC Curve"
tipo: paper
autor: "Ahmed Negida, Nadien Khaled Fahim, Yasmin Negida"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC6683590"
publicado_em: 2019-05-19
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [sample-size, diagnostic-accuracy, sensitivity, specificity, auc, confidence-interval, prevalence, buderer-formula]
licenca: "CC BY-NC 4.0, na própria página. Pela cláusula NC, só a ficha: o integral fica na url"
---

# Negida et al. 2019 (Advances Journal of Emergency Medicine): amostra para estudo de acurácia diagnóstica

Ficha em palavras próprias, em estrutura própria (fonte curta com cláusula NC: o integral não entra e está na `url`, PMC6683590). Artigo educacional, parte 4 de um guia em série sobre cálculo de amostra, em Adv J Emerg Med, vol. 3, n. 3, e33; DOI 10.22114/ajem.v0i0.158; Zagazig University e Bahçeşehir University. Área: medicina de emergência. Sem dados próprios: os dois exemplos são estudos imaginados pelos autores.

## Dois caminhos, conforme a medida do teste

| Medida do teste novo | Como se calcula | O que entra |
|---|---|---|
| Sensibilidade ou especificidade | À mão, pelas fórmulas de Buderer, 1996 (ref. 6), ou no aplicativo Android "statistics and sample size pro" | Valor esperado da medida, largura aceitável do intervalo, prevalência |
| Área sob a curva ROC (AUC) | No programa MedCalc, menu "sampling", opção "area under the ROC curve"; o artigo não traz fórmula | AUC esperada, AUC nula (em geral 50%), razão entre casos negativos e positivos |

O teste novo pode ser aparelho, questionário ou biomarcador. As definições das medidas ficam para editoriais anteriores da equipe (refs. 4 e 5).

## As fórmulas de sensibilidade e especificidade

Siglas: TP são verdadeiros positivos e FN, falsos negativos, cuja soma é o total de pessoas com a condição; TN são verdadeiros negativos e FP, falsos positivos, cuja soma é o total sem ela. P é a prevalência.

| Conta | Para a sensibilidade | Para a especificidade |
|---|---|---|
| Primeiro | TP + FN = Z² × Se × (1 − Se) / W² | TN + FP = Z² × Es × (1 − Es) / W² |
| Depois | N = (TP + FN) / P | N = (TN + FP) / (1 − P) |

Se e Es são os valores esperados, tirados de estudos anteriores. O artigo fixa Z em 1,96, para confiança de 95%, e W em 10%; a W ele chama de "the maximum acceptable width of the 95% confidence interval".

## Os dois exemplos, lado a lado

| | Hipertensão em adolescentes egípcios | Meningite bacteriana ou enteroviral |
|---|---|---|
| Teste novo | Razão entre pressão arterial e altura | Lactato no líquor |
| Referência | Padrão-ouro, aplicado antes do teste novo | Bacterioscopia, aglutinação em látex para antígeno bacteriano e cultura |
| Entradas | Sensibilidade e especificidade de 90%, de estudo anterior parecido; prevalência de 5% (a ref. 7 fecha a frase) | AUC de 94% e razão de 525/662, de estudo anterior; alfa de 5% e beta de 10% |
| Resultado da fonte | TP + FN = 34,5; TN + FP = 34,5; 691 para a sensibilidade; 36 para a especificidade; total de 728 | 11 pacientes: 5 com meningite enteroviral e 6 com bacteriana |

Em ambos se reúnem pessoas com e sem a condição, e cada uma passa pelos dois testes.

## O que conferir nos números da fonte

- As contas escritas usam 34,5, mas os resultados saem do valor sem arredondar. Com 1,96² × 0,9 × 0,1 / 0,1² = 34,57, vêm 691,5 e 36,4, que somam 727,9. Com os números impressos, 34,5 / 0,05 dá 690, e 691 + 36 dá 727.
- A frase que fecha o exemplo chama os 691 de participantes com hipertensão e os 36 de participantes sem hipertensão. No passo da fórmula, os 691 vêm de dividir TP + FN (34,5) pela prevalência.
- O texto do exemplo de AUC atribui o estudo anterior a "Manomaivat et al."; a referência 8, na mesma frase, traz Domingues e outros (2019).

## O que o texto deixa em aberto

- Não há seção de limites nem ressalvas.
- Não trata de intervalos exatos, das condições da aproximação normal nem de amostra com prevalência diferente da população.
- Não diz por que somar os dois N: o exemplo apenas soma.

## Tudo o mais que ensina

- Antes desta parte, a série cobriu amostra para taxa ou proporção única (parte 1), coorte independente (parte 2) e caso-controle independente (parte 3).
- Segundo os autores, um bioestatístico vietnamita programou as equações no aplicativo, que deu estimativas parecidas com as mesmas entradas (Figura 1). As Figuras 2 e 3 mostram o menu e a tabela de resultado do MedCalc.
