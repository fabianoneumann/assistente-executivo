---
titulo: "Bias in the Loop: How Humans Evaluate AI-Generated Suggestions"
tipo: paper
autor: "Jacob Beck, Stephanie Eckman, Christoph Kern, Frauke Kreuter (LMU Munich; University of Maryland)"
url: "https://arxiv.org/abs/2509.08514"
publicado_em: 2025-09-10
capturado_em: 2026-11-04
licenca: "CC BY 4.0 (escrita na primeira página do PDF: 'The article is licensed under a Creative Commons Attribution (CC BY 4.0) International license', e na página do arXiv); o integral está na url"
areas: [agent-engineering, psychology]
tags: [pre-annotation, human-ai-collaboration, automation-bias, overcorrection, undercorrection, annotation-quality, wizard-of-oz, crowdsourcing, randomized-experiment]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Lido no PDF de 2026-11-04 (preprint, arXiv v1, 10 de setembro de 2025).

## O estudo em uma frase

Experimento aleatorizado com 2.784 pessoas de uma plataforma de microtarefas (Prolific, residentes nos EUA), que decidiam se um valor sugerido por uma "IA" estava certo; a sugestão, na verdade, era escrita à mão pelos pesquisadores (desenho "Mágico de Oz"), e o experimento variou três fatores de desenho do trabalho e media atitudes diante de IA. Os autores registraram hipóteses e abordagem de forma pré-registrada no OSF.

## A tarefa e o plantio dos erros

Cada participante via 10 tabelas de relatórios de empresas e, em cada uma, uma frase do tipo "as emissões do ESCOPO ANO são VALOR, segundo a IA. Está correto?"; devia corrigir as sugestões erradas e deixar as certas. A verdade de referência veio de uma anotação especializada em dois passos, de outro trabalho da equipe. As tabelas foram escolhidas por estrato (concordância entre dois anotadores leigos, acerto de pelo menos um deles, tipo de rótulo).

Os erros plantados imitam os que os autores tinham visto em saídas de um LLM: ano de relato errado, escopo errado, erro de grafia ou alucinação, e erro segundo as regras de definição dadas no tutorial. As três primeiras tabelas eram as mesmas para todos (em ordem aleatória entre si); as outras sete vinham em ordem aleatória, quatro com erro e três com sugestão correta. Antes, três telas de instrução e dois exemplos, um positivo e um negativo.

## Os três fatores manipulados (2 x 2 x 2)

- Pedir ou não o valor correto quando o participante marca a sugestão como errada.
- As três primeiras sugestões todas corretas ou todas erradas.
- Um bônus por desempenho (0,75 libra, para os 10% de maior acurácia) oferecido a metade dos participantes.

Atitude diante de IA: uma escala de seis itens (Likert de 7 pontos), aplicada uma semana antes (para evitar contaminação) a quem foi convidado depois para a tarefa. Dos 3.187 respondentes do questionário, 1.230 (39%) fizeram a anotação; como a taxa ficou abaixo do esperado, entraram outros participantes sem o questionário, e mais da metade da amostra final não o respondeu. Pagamento: 0,75 libra pelo questionário e 1,95 pela anotação. A amostra pretendida, 2.750, vem de um cálculo de poder (alfa 0,05; poder 0,80; efeito de desenho 1,25).

## As medidas

Matriz 2 x 2 entre a sugestão (correta ou incorreta) e a decisão do anotador. Acurácia: acertos sobre o total de instâncias. Supercorreção: sugestões corretas marcadas como erradas, sobre as corretas. Subcorreção: sugestões incorretas aceitas como corretas, sobre as incorretas. Só as sete últimas instâncias contam, porque as três primeiras eram um tratamento. Análise: regressões logísticas quase-binomiais por anotador, com sexo, etnia, idade, atitude e tempo como controles.

## Resultados, hipótese por hipótese

- H1, esforço de correção: exigir o valor correto reduziu as correções e aumentou a subcorreção, com menos supercorreção; a acurácia geral, descritivamente, foi 68% contra 66% a favor de quem era obrigado a corrigir (p = 0,028), e na regressão ficou inalterada, porque a queda nas correções veio com menos supercorreção. Os autores leem o efeito como tendência de poupar trabalho.
- H2, primeiras impressões: as três primeiras sugestões, boas ou ruins, não influenciaram as sete seguintes (nenhuma métrica com diferença relevante; uma leve alta de supercorreção depois de três erros, que eles chamam de possivelmente espúria). Excluir quem deu o mesmo rótulo às 10 tabelas não mudou o resultado. Os autores apontam duas leituras: crenças fortes prévias, ou reavaliação cuidadosa a cada instância.
- H3, atitudes: quem tinha opinião menos favorável de IA e automação corrigia mais e supercorrigia mais; quem tinha opinião mais favorável subcorrigia mais; os dois quartis inferiores tiveram acurácia maior. Quem não fez o questionário (mais da metade) ficou parecido com os quartis de atitude mais favorável. A regressão manteve o padrão com todos os controles. Os autores o descrevem como o preditor mais forte do desempenho, acima da demografia.
- H4, bônus: sem efeito consistente sobre o desempenho; o texto lista explicações possíveis (a dificuldade da tarefa limita, o bônus pode ter sido pequeno ou parecer inalcançável).
- Tempo: o tempo total e o gasto nas instruções não se relacionam à acurácia (r < 0,04); as três primeiras telas levaram 71 s de média e as demais 48 s; instâncias com sugestão errada e certa levaram 54 e 55 s; quem acertou e quem errou, 55 s. Tempo por tabela, excluídas duas atípicas, teve relação levemente negativa com a acurácia; na regressão, mais tempo se associou a mais acurácia, mais correções e mais supercorreção.
- Demografia, mista: homens com acurácia maior e menos supercorreção; participantes que se identificaram como negros, com acurácia e correções menores e subcorreção maior (referência: asiático-americanos); faixas de 35-54 e 55+ corrigiram mais e subcorrigiram menos que a de 18-34.

## Acurácia por tipo de erro

Erro de grafia (dígitos trocados): corrigido em 82% dos casos. Valor certo presente na tabela, em outra célula (outro ano ou escopo): cerca de 77%. Erro que exigia entender as regras conceituais da anotação: 31%. A tabela da BlackBerry (não incluída na figura) tinha uma sugestão tecnicamente correta cujo reconhecimento exigia saber a diferença entre emissões de Escopo 2 baseadas no mercado e na localização; ali a acurácia caiu a 21%, ou seja, o número de 21% mede acertos numa tabela em que a sugestão estava certa, não é um tipo de erro plantado. A tabela da JetBlue também teve acurácia baixa, atribuída pelos autores à dificuldade ou à ambiguidade do item.

## Discussão dos autores

- Quando exigir a correção afasta o revisor de corrigir, recomendam separar a tarefa: um grupo julga se a sugestão está certa, outro corrige os casos marcados.
- Para quem quiser garantia de seriedade, sugerem critérios de exclusão por padrão de resposta, como quem aceita ou rejeita todas as sugestões, ressalvando que isso pode não mudar o quadro.
- Defendem medir atitudes de antemão e compor um grupo diverso de anotadores; na falta disso, coletar a demografia como substituto. Observam que pesquisadores de IA, de atitude provavelmente mais favorável, podem subcorrigir ao avaliar sistemas automatizados.
- Discordância entre anotadores e acurácia baixa podem ser sinal de dificuldade ou ambiguidade da instância, em vez de ruído.
- Como extensão, propõem instâncias plantadas de propósito ou checagens de atenção ao longo da tarefa, não só no começo, para ver se os anotadores as detectam.
- Dizem que o desempenho não depende só do desempenho do algoritmo, e sim de quem revisa e de como a revisão é estruturada.

## Limitações declaradas

Tarefa curta, talvez insuficiente para mostrar fadiga; a tabela da BlackBerry exigia conhecimento que trabalhadores de microtarefas provavelmente não têm; a ordem das tabelas não foi registrada, então não se analisam efeitos de ordem; não houve condição-base sem pré-anotação; uma única tarefa e uma população de trabalhadores de microtarefas, sem garantia de que valha para pesquisadores, voluntários ou especialistas.

## O que a fonte não traz

Nenhuma condição sem sugestão para comparar; nenhum estudo com revisor único e poucas dezenas de casos; nenhuma análise de quantos itens plantados bastam para medir a subcorreção.
