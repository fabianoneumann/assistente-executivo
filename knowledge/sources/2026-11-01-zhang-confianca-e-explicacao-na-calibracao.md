---
titulo: "Effect of Confidence and Explanation on Accuracy and Trust Calibration in AI-Assisted Decision Making"
tipo: paper
autor: "Yunfeng Zhang, Q. Vera Liao, Rachel K. E. Bellamy"
url: "https://arxiv.org/abs/2001.02114"
publicado_em: 2020-01-07
capturado_em: 2026-11-01
licenca: "arXiv, licença não exclusiva de distribuição: protegido, só a ficha"
areas: [agent-engineering]
tags: [trust-calibration, confidence-display, local-explanation, shap, ai-assisted-decision, appropriate-reliance, human-ai-team, error-boundaries, user-study]
---

Ficha de estudo, em palavras próprias. Publicado no FAT* 2020 (ACM Conference on Fairness, Accountability, and Transparency, DOI 10.1145/3351095.3372852); lida a versão do arXiv (v1, 07/01/2020, a única). Autores da IBM Research AI. Texto extraído do PDF com `pdftotext`; os gráficos não foram lidos como imagem, e os números vêm do texto. Lida para a rodada investigativa (tema i4, como apresentar a saída do avaliador).

**Atenção à força da evidência:** o Experimento 1 tem 72 participantes do Mechanical Turk; o Experimento 2, segundo o texto, só **9** participantes (a análise dele usa graus de liberdade que sugerem comparação com dados do Experimento 1 na mesma condição). Tarefa artificial (prever renda por dados do censo), leigos, sem responsabilidade real; o próprio texto lista esses limites.

## O resumo

Em decisões apoiadas por IA, o que importa não é aumentar a confiança, é **calibrá-la caso a caso**: confiar quando o modelo tende a acertar e desconfiar quando tende a errar. Os autores testam duas informações sobre cada previsão: a confiança do modelo e uma explicação local (contribuição de cada atributo, pelo método de Shapley). A confiança mostrada calibrou a confiança das pessoas (mais adesão quando o modelo estava seguro), mas não melhorou o acerto da dupla; a explicação local não calibrou nada e, se tanto, puxou o acerto para baixo.

## 1. Desenho

- **Tarefa:** prever se a renda anual de uma pessoa passa de US$ 50 mil, a partir de 14 atributos (Adult Data Set do censo de 1994). Os participantes recebiam uma coluna com as chances condicionadas a cada atributo, como conhecimento do domínio, para chegar perto do modelo.
- **Desempenho:** pessoas sozinhas acertaram 65% (Exp. 1) e 63% (Exp. 2); o modelo, 75% nos itens sorteados (estratificados por confiança).
- **Procedimento:** 20 tentativas de treino com retorno (a resposta certa e a do modelo), depois 40 tentativas: a pessoa decide primeiro, vê a informação do modelo e escolhe a final; retorno de acerto em cada uma; contagem regressiva de 10 segundos antes de poder enviar. Bônus de 5 centavos por acerto e perda de 2 por erro.
- **Fatores do Exp. 1:** mostrar ou não a confiança ("o modelo acerta N de 10 vezes em pessoas parecidas"); mostrar ou não a previsão (sem a previsão, a pessoa pode delegar ao modelo); modelo completo ou parcial (sem o atributo mais importante, estado civil, que a pessoa via).
- **Medidas de confiança comportamentais:** porcentagem de troca (quando discorda, quantas vezes adota o modelo, a medida mais estrita) e de concordância final.

## 2. Resultados

- **Confiança mostrada calibra:** com a confiança à vista, as pessoas trocaram mais para o modelo quando ele estava acima de 80% de confiança e menos quando abaixo de 60%; sem ela, a troca ficou igual em todos os níveis (interação F(4, 256) = 15,8, p < 0,001). Valeu mesmo sem mostrar a previsão: confiança alta levou a delegar sem ver a resposta.
- **Mas não melhorou o acerto:** o acerto da dupla não diferiu entre as condições; a esperança de que a pessoa superasse o modelo nos casos de baixa confiança não se confirmou. Explicação dos autores: os casos difíceis para o modelo eram difíceis também para as pessoas (as fronteiras de erro coincidiam), então sobrava pouco conhecimento complementar.
- **Modelo parcial:** saber que tinha informação que o modelo não tinha não mudou nada.
- **Explicação local (Exp. 2):** não mudou a troca nem a concordância ao longo dos níveis de confiança (hipótese rejeitada) e não melhorou o acerto, com tendência inversa.
- **Releitura de Lai e Tan:** o estudo deles, que achou ganho com explicações, mostra aumento indiscriminado da aceitação, certa ou errada; deu ganho porque lá a IA era muito melhor que as pessoas.

## 3. O que os autores concluem

- A confiança ajuda a formar o mapa de onde o modelo erra, com custos: só funciona se a confiança for bem calibrada; um número pode não ser bem interpretado em tarefa complexa; e o mapa depende de experiência repetida. Sugerem descrever explicitamente as zonas de baixa confiança.
- Calibrar a confiança só melhora o resultado quando pessoa e modelo erram em lugares diferentes; generalizar estudos de decisão apoiada exige caracterizar esse alinhamento, não só o acerto geral.
- A explicabilidade costuma ser vendida para aumentar a confiança; para calibrar, a explicação precisa ser sensível à incerteza da previsão. Citam que explicações que mostram só os poucos atributos que virariam a decisão soam mais alarmantes e calibram melhor um julgamento de justiça (Dodge et al.), e que explicações comparativas ajudam a achar limites do modelo (Cai et al.).

## Tudo o mais que ensina

- A confiança apresentada como frequência ("N de 10") em vez de porcentagem, seguindo a literatura de comunicação de risco.
- Aumentar a confiança num modelo inferior é enganar; a meta declarada é calibrar.
