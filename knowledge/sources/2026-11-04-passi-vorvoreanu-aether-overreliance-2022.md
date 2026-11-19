---
titulo: "Overreliance on AI: Literature review"
tipo: artigo
autor: "Samir Passi e Mihaela Vorvoreanu (Microsoft; Aether UX Research & Education)"
url: "https://www.microsoft.com/en-us/research/wp-content/uploads/2022/06/Aether-Overreliance-on-AI-Review-Final-6.21.22.pdf"
publicado_em: 2022-06-21  # o PDF não traz data; vem do nome do arquivo ("Final-6.21.22") e do caminho /2022/06/ no site da Microsoft Research
capturado_em: 2026-11-04
areas: [agent-engineering]
tags: [overreliance, automation-bias, human-ai-teams, reliance-measures, cognitive-forcing-functions, literature-review, appropriate-reliance]
licenca: "sem nota de licença no PDF nem na página de origem; relatório da Microsoft, com todos os direitos reservados presumidos; por isso só ficha em palavras próprias, com poucas passagens curtas literais"
---

# Aether/Microsoft (2022): revisão de literatura sobre dependência excessiva de IA

Ficha em palavras próprias, lida no PDF de 23 páginas em 2026-11-04. O relatório sintetiza cerca de 60 artigos de IHC, fatores humanos, interfaces inteligentes, trabalho cooperativo apoiado por computador, ciência organizacional e justiça/transparência em IA, e se organiza em três partes: o que é dependência excessiva e como medi-la; antecedentes, mecanismos e consequências; técnicas de mitigação. É revisão da literatura de terceiros: as afirmações empíricas abaixo são as que o relatório atribui aos estudos que cita, e não foram conferidas nos originais.

## A definição

O relatório trata a dependência apropriada como um alvo que se move, por dois motivos: é difícil de converter em medida e depende do contexto e do domínio de aplicação. O lado excessivo se nomeia com mais facilidade, como erros de comissão: o usuário acata a recomendação da IA justamente quando ela está errada. Na cadeia que o texto descreve, quem desconhece o que o sistema consegue fazer, com que qualidade e de que jeito funciona fica sem base para decidir se confia nele, ou quanto, e é nessa situação que a dependência excessiva costuma aparecer.

Duas ressalvas do texto: (a) a dependência excessiva nem sempre é visível, porque quando a IA é melhor que o humano e a dupla sai melhor que o humano sozinho a situação parece aceitável, mas a IA erra de modo diferente do humano e pode errar de formas novas depois de atualizações de modelo, o que pede cautela; (b) o pedido de supervisão humana pressupõe cooperação fluida, e os autores dizem que ele pode dar uma falsa sensação de segurança.

## Medidas listadas

- Concordância com recomendações incorretas: quantas vezes o usuário aceita a recomendação incorreta, do total de incorretas mostradas (atribuída a Buçinca et al., 2021).
- Fração de troca (switch fraction): quantas vezes o usuário muda por completo a resposta para igualar a da IA (Lu e Yin, 2021; Kim et al., 2021). Extensão: a porcentagem de mudança em direção à IA.
- Peso do conselho (weight of advice, Logg et al., 2019): a importância dada à recomendação, calculada como a diferença entre a resposta final e a inicial dividida pela diferença entre a recomendação da IA e a resposta inicial; o valor 1 indicaria dependência excessiva.
- Termos associados: concordâncias e discordâncias (a previsão do usuário, feita antes de ver a IA, igual ou diferente da recomendação), erros humanos (o usuário erra quando discorda de uma IA também errada) e delegação (deixar a IA decidir por ele).

## Antecedentes

Diferenças individuais: alfabetização em IA (clínicos com pouca alfabetização teriam sido sete vezes mais propensos a escolher o tratamento alinhado à IA, num estudo citado); especialistas e novatos podem ambos depender demais (novatos aceitam muito, especialistas dizem desprezar a IA e ainda assim dependem dela); familiaridade com a tarefa leva a mais confiança relatada e menos adesão, e mais excesso de confiança em si. Recomendações do relatório: projetar para a variação de confiança, perícia, familiaridade, alfabetização e atitudes; acompanhar usuários de baixa perícia; usar telemetria para ver quais recomendações são aceitas e criar uma tipologia de problemas.

## Mecanismos

- Viés de automação (favorecer a recomendação automatizada em vez de fontes não automatizadas): usuários dependem do sistema que vai bem e perdem a confiança depois de vê-lo falhar; a confiança cai muito quando a capacidade diminui e sobe pouco quando ela volta. Mais forte em tarefas objetivas e desconhecidas, menor em tarefas subjetivas.
- Viés de confirmação: a dependência cresce quando a recomendação coincide com a previsão do próprio usuário, sobretudo se ele sabe menos do sistema e confia mais em si. Ressalva: o viés também pode aprofundar a desconfiança de quem já subdepende.
- Efeitos de ordem: quem vê a IA ir bem no começo tende à dependência excessiva e a complacência; quem a vê falhar cedo tende à aversão. Novatos dependem demais em ambos os casos; especialistas que veem falha cedo subdependem de forma duradoura, e os que veem sucesso cedo ajustam bem a confiança se ela piorar depois. Ligados ao efeito de ancoragem: a recomendação vista antes de decidir serve de âncora, e a acurácia declarada da IA também (acurácia declarada baixa mantém a desconfiança mesmo com bom desempenho; alta faz perder a confiança quando ela erra, mesmo que supere o usuário).
- Explicações: tornam o usuário mais confiante em todas as recomendações, inclusive as incorretas; explicações detalhadas, ou sem base no funcionamento real, aumentam a confiança; uma explicação não informativa como uma acurácia declarada elevou a confiança mesmo com acurácia de 50%. Ressalva: o descompasso entre a explicação e a expectativa do usuário pode reduzir a confiança.

## Consequências

O desempenho da dupla humano+IA pode ser pior que o do humano ou o da IA sozinhos. Razões citadas: o usuário muda a ação para casar com a IA (num estudo, quase o dobro de pessoas avaliou como precisa uma análise de tom que era aleatória); superestima a acurácia e não percebe que cedeu o controle; recomendações incorretas reduzem a acurácia e deixam o usuário mais lento que quem faz a tarefa do zero; diante de grande desacordo, supõe que errou ele; com dados novos, confia mais na IA. O relatório recomenda comparar o desempenho da dupla com o do humano sozinho, sobretudo diante de recomendações problemáticas, e acompanhá-lo ao longo do tempo.

## Técnicas de mitigação

Na primeira interação: integração com exemplos de recomendações certas e erradas, porque nunca ver a IA errar leva a confiar demais nas capacidades dela; transparência sobre acurácia, objetivo de projeto, limites, casos de borda e usos pretendidos; ajustes personalizados, medindo viés de automação, confiança em si e alfabetização em IA no tutorial; e alterar a sequência de sucessos e falhas iniciais.

No uso regular: funções de forçamento cognitivo (checklists, pausas, explicações sob demanda, pedir que o usuário descarte alternativas), que reduzem a dependência em recomendações incorretas, mas são menos apreciadas pelo esforço extra; retorno em tempo real (acurácia, mas sem apresentar pontuações altas sem crítica; escores de confiança, com o risco de saírem pela culatra; avisar quando o usuário aceita algo problemático, inclusive com modelos separados que detectam recomendações fora do padrão); explicações que informem e não só convençam; mexer na velocidade de resposta (dois estudos com efeitos opostos); recomendações só sob pedido e a opção de decidir antes de ver a IA; e o relatório sugere telemetria para medir aceitação de recomendações problemáticas e peso do conselho. A tabela final lista as técnicas por problema que tratam.

## Citações

> "Overreliance on AI is defined as users accepting incorrect AI recommendations--i.e., making errors of commission."

> "calls for human oversight can provide a false sense of security"

## O que a fonte não traz

Nenhum dado primário nem estudo próprio; nenhuma regra de quantos itens com erro plantado ou de qual taxa de concordância seria excessiva; nenhuma data de publicação no corpo do PDF.
