# Antes de automatizar uma decisão: dado na hora do uso, custo do erro, volume e piloto

O que perguntar antes de entregar uma decisão a um modelo (um classificador, um juiz, um modelo de decisão tipado): se o dado chega na hora de decidir, qual o desempenho humano, quanto custa o erro, quantas decisões há e se vale um piloto em sombra. Quando a nota não deve decidir: [[classificacao-como-portao]].

Convenção: "leitura nossa" liga a fonte a um ambiente de agentes e não está na fonte. "Não verificado" é afirmação de resposta de buscador, sem primária aberta.

## A resposta curta

- **A prática pergunta primeiro se o dado existe na hora de decidir,** qual o desempenho humano e quanto custa o erro.
- **Volume e piloto em sombra não têm primária aberta,** embora as respostas dos buscadores recomendem os dois.
- **Um roteiro de caso de uso que não manda medir volume nem a chegada do dado antes de pesquisar** gasta busca em pergunta que a contagem poderia ter encerrado (leitura nossa).

## O que as fontes pedem

- [[2026-11-06-google-2025-viabilidade-de-ml]] (Managing ML Projects, CC BY): cinco fatores, dado disponível, dificuldade do problema, qualidade de previsão pedida, requisitos técnicos e custo. Do dado: quantidade, **se o atributo estará disponível na hora de servir** (equipes gastaram tempo treinando com atributo que só chegava dias depois) e regulação. Da dificuldade: já foi resolvido? Qual é o desempenho humano? Da qualidade: o custo do erro decide o que se exige, e o custo cresce com a qualidade pedida.
- [[2026-11-06-zinkevich-rules-of-ml]] (Google, guia de praticante, CC BY): Regra 1, não ter medo de lançar sem ML; Regra 2, primeiro desenhar e medir; Regra 3, escolher ML no lugar de heurística complexa.
- PAIR, worksheet "User Needs" (citação, https://pair.withgoogle.com/worksheet/user-needs.pdf): reunir evidência do problema antes de discutir IA, e fazer o caso a favor e contra; pesar precisão e revocação pelo que o usuário ganha.
- CRISP-ML(Q), Studer e outros (citação, https://arxiv.org/abs/2003.05155): junta entendimento do negócio e dos dados na primeira fase, porque a disponibilidade do dado muitas vezes define a viabilidade.
- Naser 2026 (citação, https://doi.org/10.1007/s44285-025-00054-3; revisão conceitual, engenharia): critérios de complexidade, dados, recursos, interpretabilidade, valor e risco. Como exemplo, em engenharia, adotar ML só com melhora estatisticamente significativa e relevante na prática sobre os modelos tradicionais. No quadro que propõe, o portão 0 quantifica o dado disponível e compara com o método convencional antes do ML, e o portão 1 verifica se o dado atinge o mínimo viável. Não foi medido.
- **Da base:** [[classificacao-como-portao]] diz quando a nota não deve decidir; um modelo de decisão tipado (como o Jev, da TypeSafe) se encaixa em decisões fechadas e de alto volume.

## O que não fechou

- **Volume:** Perplexity e Gemini dizem que pouca decisão não paga manter um modelo, e o Gemini cita 10 vezes por mês, sem primária. **Não verificado.** Para um modelo de decisão barato o argumento muda: o custo de rodar é pequeno, e o que custa é rotular e revisar (leitura nossa).
- **Piloto em modo sombra:** Perplexity e Gemini recomendam, e a busca dirigida só achou fornecedor e o anúncio de um produto da AWS. **Não verificado como recomendação de primária.** O PinSieve exige validação em sombra antes de trocar o modelo ([[2026-10-30-pinsieve-zona-cinza-e-revisao-humana]]) (ligação nossa).

## O que isto dá para um ambiente de agentes (leitura nossa)

- **Contar antes de pesquisar.** O primeiro passo de um caso de uso pergunta se o código resolve; logo depois, se o dado de entrada chega na hora da decisão e quantas decisões há. Medir isso antes adianta a informação que, medida depois, costuma encerrar o caso só quando as buscas já foram feitas.
- **"Decisão que se repete muitas vezes" é um critério que se mede,** não que se supõe: contar o volume é só aplicá-lo.
- **"Desempenho humano" tem duas leituras.** O do Google é acurácia humana; [[calibracao-por-dimensao]] pede o acordo da pessoa consigo mesma. São medidas diferentes. Quando duas pessoas concordam pouco às cegas, é sinal cedo de que o limite pode estar na tarefa; a medida que decide é o acordo do dono da régua consigo mesmo.

## Ver também

[[ponto-de-corte-reuso-do-teste-e-desvio]]; [[casos-artificiais-e-espectro]].
