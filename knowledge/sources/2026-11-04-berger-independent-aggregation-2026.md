---
titulo: "Beyond AI advice -- independent aggregation boosts human-AI accuracy"
tipo: paper
autor: "Julian Berger (Max Planck Institute for Human Development), Pantelis P. Analytis (University of Southern Denmark), Ville Satopää (INSEAD), Ralf H. J. M. Kurvers (Max Planck Institute for Human Development; Technische Universität Berlin)"
url: "https://arxiv.org/abs/2603.29866"
publicado_em: 2026-03-31
capturado_em: 2026-11-04
licenca: "CC BY-SA 4.0 (indicada na página do arXiv, arxiv.org/abs/2603.29866, que liga a creativecommons.org/licenses/by-sa/4.0/); o integral está na url"
areas: [agent-engineering, psychology]
tags: [hybrid-confirmation-tree, ai-as-advisor, independent-judgments, signal-detection, overreliance, underreliance, secondary-analysis, human-ai-complementarity]
---

Ficha em palavras próprias; o texto integral (licença CC BY-SA 4.0) não vem neste repositório e se lê na url do frontmatter. Lido no PDF de 2026-11-04 (preprint, arXiv v1, 31 de março de 2026).

## Tipo de evidência

É uma reanálise de dados já coletados por outros grupos, não um experimento novo. A "árvore de confirmação híbrida" (HCT) não foi executada com participantes: o desempenho dela foi calculado, para cada caso de cada conjunto, combinando por permutação os julgamentos de duas pessoas que haviam decidido sem ajuda de IA com o conselho da IA registrado no estudo original. O desempenho do modo "IA como conselheira" vem das pessoas que, nesses estudos, decidiram vendo o conselho. Código e dados estão num repositório OSF.

## A proposta comparada

Na HCT, um humano e a IA decidem de forma independente; se concordam, vale a decisão; se discordam, um segundo humano desempata. O objetivo é preservar a independência dos julgamentos e tirar do humano o encargo de distinguir conselho certo de errado. O modo comparado, "IA como conselheira", é o de a IA recomendar e o humano aceitar ou rejeitar. Os autores citam, como limitações do segundo, subdependência (rejeitar conselho certo), superdependência (aceitar o errado), uso da sugestão como atalho sob pressão de tempo e possível perda de habilidade.

## Dados usados

10 conjuntos, com 41.809 escolhas binárias de 1.229 pessoas em 3.220 casos: sentimento em resenhas de cerveja e de livros (Bansal et al.), confiabilidade de resenhas de hotel (Lai e Tan), câncer de pele por dermatologistas (Vodrahalli et al.; Chanda et al.), lesões em colonoscopia por especialistas e por não especialistas (Reverberi et al.), deepfakes (Groh et al.), manchetes (DeVerna et al.) e reprisão criminal (Fogliato et al.). Precisão da IA, quando informada: pele (Vodrahalli) 83%, deepfakes 78%, reprisão 67%, detecção de fraude em resenhas de hotel 87% (humanos: 51%), resenhas de cerveja e de livros 84%. Um subconjunto de quatro conjuntos tinha 16 condições em que a IA também explicava a decisão (50.390 decisões, 1.423 pessoas, 516 casos).

## Resultados centrais

- A HCT superou o modo conselheira em todos os 10 conjuntos, com ganhos de 0,2 a 6,6 pontos percentuais; no conjunto de todos, 4,45 pontos (intervalo de maior densidade 95%: 3,73 a 5,27), dentro de uma região de equivalência prática de mais ou menos 1 ponto. Só as resenhas de cerveja não passaram o limiar prático.
- Com explicação da IA: a HCT foi melhor em 11 das 16 comparações, parecida em 2 e pior em 3, as três nas resenhas de hotel, onde os humanos sozinhos acertavam 51,1%, quase o acaso. Para dermatologistas (Chanda), a explicação não melhorou o modo conselheira e a HCT ganhou 3 pontos.
- Por nível de desempenho (terços de acurácia sem IA, nos 5 conjuntos em que a mesma pessoa decidiu com e sem IA): a HCT superou o modo conselheira em 8 pontos para os de baixo (intervalo 6,9 a 9,2), 3,2 para os do meio e 1,9 para os de cima (intervalo 0,6 a 3,2; 92% de significância prática). Pareado com um desempatador de nível médio ou alto, todos ganharam; com um de nível baixo, perderam. Como só uma minoria dos casos precisa de desempate, os autores sugerem pôr o profissional mais caro nessa segunda posição.
- Custo: o desempate é chamado em 22% (resenhas de livros) a 49% (fraude em hotel) dos casos na seção de resultados, e a discussão fala em 20 a 49%.
- Quando a IA acertava (77% dos casos, em média), a HCT acertou 10,4 pontos a mais que o modo conselheira; quando a IA errava, a HCT acertou 11,89 pontos a menos.
- Por que: houve discordância inicial em cerca de 33% dos casos. No modo conselheira, quando a IA discordava e estava certa (21% de todos os casos), o humano adotou a IA em 34%; quando discordava e estava errada (13%), o humano manteve a própria resposta certa em 80%. Na HCT, o desempatador concordou com a IA certa em 71% e rejeitou a IA errada em 47% das vezes. Dos casos, 56,5% tinham humano e IA certos e 9,2%, ambos errados.

## O modelo de detecção de sinais

Os autores seguem a formulação de Langer et al. (2024) e tratam seguir o conselho como um problema de detecção de sinais. Acerto (hit) é seguir o conselho certo; alarme falso é seguir o conselho errado; ambas as taxas são condicionais à discordância entre a resposta inicial do humano e a IA. Sensibilidade d' = z(HR) − z(FAR); viés c = −(z(HR) + z(FAR))/2, com c < 0 indicando tendência a aceitar e c > 0, a rejeitar, e variância igual nos dois lados. As suposições da HCT: erros do humano e da IA independentes, humanos com a mesma acurácia média; no modo conselheira, que o humano não muda de ideia quando já concorda com a IA.

Nos estudos em que a mesma pessoa decidiu antes e depois do conselho, a taxa de acerto e a de alarme falso foram observadas por pessoa; nos estudos com grupos diferentes (Bansal, Lai, DeVerna), foram inferidas pela mudança média entre grupo sem IA e grupo com IA, dividida pela mudança potencial (a parcela do grupo-controle que discordava da IA), com zero quando o grupo-controle concordava com a IA ou a mudança ia no sentido contrário. As previsões do modelo acertaram em 37 de 41 comparações quanto a qual estratégia vencia (duas das 4 falhas em diferenças sem relevância prática e duas com evidência fraca de relevância).

Resultados do modelo: acurácias parecidas de humano e IA, com viés neutro, deixam o modo conselheira mais perto da HCT mesmo com d' baixo; com humano e IA muito precisos, o conselheiro só alcança a HCT com d' alto; com IA mais precisa que o humano, um viés liberal (aceitar mais) pode superar a HCT mesmo com d' baixo, porque o ganho de seguir a IA supera o custo dos erros ocasionais; com humano mais preciso que a IA, o conselheiro só vence com d' alto e viés conservador. Nos dados: no conjunto de fraude em hotel (IA 87%, humano 51%) os humanos tinham d' baixo e pouco apoio na IA, e aceitar mais teria igualado ou superado a HCT; nas resenhas de livros (humano 88%, IA 84%, viés quase neutro) seria preciso um grande salto de d'. Com explicações, não houve padrão claro de d' maior ou viés menor; entre quem decide melhor ou pior sem IA, também não houve diferença sistemática no uso do conselho.

## Discussão dos autores

O custo do segundo humano precisa ser pesado contra o ganho (exemplo da mamografia); a HCT não exige dados de treino nem ajuste de parâmetros e se parece com estratégias rápidas e frugais; a independência protegeria contra perda de habilidade e homogeneização de ideias, de que o texto cita evidências de outros estudos como indício, sem teste na HCT. Os autores dizem que os efeitos de longo prazo da delegação a IA permanecem incertos.

## O que a fonte não traz

Nenhuma execução real da HCT com participantes; nenhum teste com revisor único que seja o próprio segundo humano; nenhuma discussão de limitações em seção separada.
