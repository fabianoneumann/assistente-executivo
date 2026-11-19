---
titulo: "Calculation of signal detection theory measures"
tipo: artigo
autor: "Harold Stanislaw (California State University, Stanislaus) e Natasha Todorov (Macquarie University)"
url: "https://link.springer.com/content/pdf/10.3758/bf03207704.pdf"
publicado_em: 1999  # Behavior Research Methods, Instruments, & Computers, 1999, 31(1), 137-149; o PDF traz só o ano
capturado_em: 2026-11-04
areas: [psychology, agent-engineering]
tags: [signal-detection-theory, d-prime, response-bias, hit-rate, false-alarm-rate, extreme-rates, roc, measurement-method]
licenca: "artigo da Psychonomic Society/Springer, com copyright (a primeira página do PDF diz 'Copyright 1999 Psychonomic Society, Inc.'); só ficha em palavras próprias, com passagens curtas literais"
---

# Stanislaw e Todorov (1999): como calcular as medidas da teoria de detecção de sinais

Ficha em palavras próprias, lida no PDF de 13 páginas em 2026-11-04 (o texto extraído tem erros de leitura óptica, sobretudo em fórmulas; as fórmulas abaixo seguem o que o texto descreve em palavras e as equações legíveis). É um artigo de método: explica a teoria e dá fórmulas, o tratamento de casos de borda e comandos para vários programas. Langer et al. (2024) o citam para a fórmula de d'.

## Para que serve a teoria

A teoria de detecção de sinais (SDT) vale onde é preciso discriminar dois tipos de estímulo (sinal e ruído): percepção, memória de reconhecimento (itens velhos e novos), detecção de mentira, seleção de pessoal, júri, diagnóstico médico, inspeção industrial, recuperação de informação. A contribuição central, dizem, é separar viés de resposta (a tendência geral a responder sim ou não, dada pela posição do critério) de sensibilidade (a sobreposição entre as distribuições de sinal e ruído). Taxa de acerto, taxa de alarme falso, acerto "corrigido" pela subtração do alarme falso e proporção de respostas corretas misturam as duas coisas.

Cinco exemplos de por que isso importa: limiares maiores para palavrões podem ser viés (mais embaraçoso errar, e o participante é cauteloso) e não proteção perceptual; a hipnose aumenta lembranças e intrusões (alarmes falsos), e só a separação diz se melhora a memória; dois testes diagnósticos podem diferir no acerto e no alarme falso por critérios distintos, e a SDT mede a sensibilidade de cada um independente do critério; instruções ao júri sobre dúvida razoável mudaram o viés (disposição de condenar), não a capacidade de distinguir culpado de inocente; inspetores que detectam menos itens defeituosos ao longo do turno mostram, em geral, mudança de viés, o que levou a remédios que falhariam se a causa fosse perda de sensibilidade. Exemplo médico: radiologistas classificavam a mesma radiografia de forma diferente em parte por critérios diferentes; passou-se a mandar examinar com critério liberal e reexaminar os positivos com critério conservador.

## Os três tipos de tarefa

- Sim/não: provas de sinal e de ruído, e o participante diz se houve sinal. Se a variável de decisão passa do critério, responde sim. Em prova de sinal, sim é acerto; em prova de ruído, sim é alarme falso. A taxa de acerto e a de alarme falso descrevem o desempenho. Critério liberal (baixo) dá muitos acertos e muitos alarmes falsos; conservador, o contrário. A única forma de subir o acerto sem subir o alarme falso é reduzir a sobreposição das distribuições.
- Escala (rating): graus de confiança de 1 a r dão r − 1 pontos de uma curva ROC (acerto por alarme falso para todos os critérios); a área sob a curva (Az, supondo normalidade) mede sensibilidade e vale 0,5 se o sinal não se distingue do ruído e 1 se a distinção é perfeita; só esse tipo de tarefa permite testar se as dispersões são iguais (inclinação 1 da reta no espaço z).
- Escolha forçada (mAFC): um sinal e m − 1 ruídos por prova, com a proporção de acertos como sensibilidade; sem critério, não mede viés.

## Medidas e fórmulas (sim/não)

- d' = z(H) − z(F), onde H é a taxa de acerto, F a de alarme falso e z a função inversa da normal padrão; mede a distância entre as médias em unidades de desvio-padrão; 0 é incapacidade de distinguir, e valores maiores indicam mais capacidade. Pressupostos: distribuições normais e de mesmo desvio-padrão, que não podem ser testados em tarefas sim/não e podem não valer (a igualdade das dispersões é a mais suspeita). Se falham, d' varia com o viés.
- Medida não paramétrica de sensibilidade, A', de 0,5 a 1, com fórmula em dois ramos conforme H ≥ F ou H < F e uma única fórmula com a função sinal; o texto reconhece que é controversa.
- Viés: β, razão de verossimilhanças (1 é neutro, abaixo de 1 tende a sim, acima de 1 a não) e seu logaritmo natural; c = −[z(H) + z(F)]/2, distância do critério ao ponto neutro em unidades de desvio-padrão (valores negativos tendem a sim, positivos a não), que muitos autores passaram a preferir por ser independente de d' e basear-se diretamente na variável de decisão; e B'' de Grier, não paramétrica, de −1 a 1.
- Área sob a ROC estimada a partir de d': Ad' = Φ(d'/√2), que equivale à proporção correta em escolha forçada com duas alternativas se as hipóteses valem.

## Taxas de acerto ou alarme falso iguais a 0 ou 1

Uma taxa de 0 ou 1 leva o z ao infinito (−∞ ou +∞). Três situações deixam isso comum: poucas provas, com erro amostral grande; sinal muito distante do ruído; e um critério extremo, liberal ou conservador, que o participante adota quando, por exemplo, o alarme falso custa caro. O que fazer depende de quantas taxas caem no extremo. Com uma só, d' e Ad' ficam indeterminados. Com as duas, ainda há valor: H = 1 e F = 0 dão d' = +∞ e Ad' = 1; H = 0 e F = 1 dão d' = −∞ e Ad' = 0; e, se as duas forem 0 ou as duas 1, a maioria dos pesquisadores assume d' = 0 e Ad' = 0,5.

Quatro soluções descritas, aqui da mais usada à que troca a medida:
1. Corrigir só as taxas extremas, o remédio mais comum e presente em vários programas (Macmillan e Kaplan, 1985): 0 passa a 0,5/n e 1 passa a (n − 0,5)/n, com n o número de provas de sinal ou de ruído. Enviesa a sensibilidade (Miller, 1996) e pode sair pior que a log-linear; é a convenção do exemplo numérico dos autores.
2. Corrigir todas as contagens, na abordagem log-linear (Hautus, 1995): antes de calcular as taxas, 0,5 entra no número de acertos e no de alarmes falsos, e 1 no total de provas de sinal e no de ruído. Quem a defende a aplica sempre, haja extremo ou não; segundo Hautus, parece funcionar razoavelmente bem.
3. Calcular as taxas sobre os dados somados de vários participantes (Macmillan e Kaplan, 1985), saída restrita a grupos de viés e sensibilidade parecidos e que dificulta o teste estatístico.
4. Trocar a medida por uma não paramétrica (como A'), que dispensa as funções z mas é controversa.

O texto não dá um número mínimo de provas.

## Métodos de cálculo

Tabelas (Elliott, 1964, e outras) têm baixa precisão (arredondamento a dois dígitos muda o segundo dígito de d') e só serviam antes dos computadores; programas específicos para SDT (Brophy, 1986; Macmillan e Creelman; RSCORE4 e ROCFIT para dados em escala, e o RSCORE4 talvez se saia melhor com taxas 0 ou 1); e programas gerais com a função inversa da normal (NORMSINV no Excel e no Quattro Pro, PROBIT no SAS e no SPSS, ZIF no SYSTAT, InvCDF no Minitab, Quantile[NormalDistribution[0,1]] no Mathematica). Exemplos: d' = NORMSINV(H) − NORMSINV(F) e c = −(NORMSINV(H) + NORMSINV(F))/2. Para dados em escala, ajustar a reta no espaço z por mínimos quadrados ordinários dá estimativas enviesadas, porque as duas taxas têm erro amostral; os autores indicam programas específicos ou duas regressões.

O exemplo numérico (tabela 5) usa uma escala de 6 pontos com 50 provas de sinal e 25 de ruído, e mostra as taxas extremas substituídas por 49,5/50 (0,99) e 0,5/25.

## Citação

> "Sensitivity and response bias are confounded by most performance measures"

## O que a fonte não traz

Nenhuma regra de número mínimo de provas por condição; nenhuma discussão de aplicação a revisores de saídas de IA; sua atenção é a quem estuda percepção, memória e diagnóstico.
