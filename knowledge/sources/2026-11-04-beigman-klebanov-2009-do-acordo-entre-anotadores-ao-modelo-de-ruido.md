---
titulo: "From Annotator Agreement to Noise Models"
tipo: paper
autor: "Beata Beigman Klebanov, Eyal Beigman"
url: "https://aclanthology.org/J09-4005.pdf"
publicado_em: 2009-12-01  # Computational Linguistics 35(4), seção "Squibs"; o PDF registra aceite em 26/1/2009
capturado_em: 2026-11-04
licenca: "© 2009 Association for Computational Linguistics (nota do PDF); sem licença aberta escrita no texto lido; tratado como protegido: só a ficha"
areas: [agent-engineering]
tags: [inter-annotator-agreement, kappa, gold-standard, noise-model, easy-hard-instances, benchmarking, annotator-count]
---

# Beigman Klebanov e Beigman 2009 (Computational Linguistics): do acordo entre anotadores a um gabarito com taxa de ruído

Ficha em palavras próprias; as seções seguem a ordem das do artigo, com a frase reescrita dentro delas (revista em 2026-11-19) (artigo protegido: o integral não entra). Lida no texto bruto do PDF em 2026-11-04. É um "squib" (nota curta, matemática) sobre a passagem de dados anotados para um padrão de referência: um subconjunto suficientemente livre de ruído, com confiança declarada. A tese central: sem reinterpretação, os coeficientes de concordância não dizem a qualidade do conjunto como recurso de avaliação; concordância geral alta não é suficiente nem necessária para extrair dali uma parte muito confiável.

## O problema com a prática corrente

Os autores partem de uma lacuna: entende-se pouco quanto o valor do kappa diz da qualidade dos dados para comparar algoritmos, e ainda assim é desse coeficiente de concordância que a linguística computacional costuma deduzir essa qualidade. A regra prática é de tudo ou nada, com o corte firmado por volta de kappa 0,67: abaixo dele, o conjunto inteiro vai fora; acima, o conjunto inteiro fica, e cada discordância restante ganha um rótulo por arbitragem (de um especialista, de uma discussão ou, com mais de dois anotadores, da maioria) ou, em alguns estudos, sai dos dados de teste. Em nota, os autores observam que muitos trabalhos nem deixam claro que destino deram às discordâncias.

## O modelo

Cada item é de um de dois tipos escondidos: fácil (os anotadores concordam sempre) ou difícil (cada anotador "joga uma moeda", independentemente). A divisão se apoia em relatos de quem faz anotação, de que há casos claros e casos de fronteira. Só os itens fáceis deveriam entrar no padrão de referência. Mas o tipo não é observável: entre os itens com acordo, alguns são difíceis em que a moeda calhou igual. O que se estima, com um nível de confiança dado, é a proporção de itens difíceis entre os itens concordantes, a partir do número de discordâncias observadas; essa proporção é o nível de ruído do padrão formado pelos itens concordantes. A chance de os anotadores concordarem num item difícil (p) depende do número de anotadores e da distribuição das categorias. O modelo aceita que cada anotador tenha uma tendência diferente de usar mais uma categoria.

## Os exemplos numéricos do artigo

- **Dois anotadores, 1.000 itens, 900 de acordo, categorias equiprováveis:** p = 0,5 e kappa = 0,8, que costuma ser lido como sinal de qualidade alta. Com 95% de confiança, até 125 dos 900 acordos podem ser sorte, isto é, ruído de 13,8%. Um caso real citado: o experimento 1 de Poesio e Vieira (1998), com 992 itens, 121 discordâncias e p = 0,47, dá 15% de ruído com 95% de confiança.
- **A pergunta inversa:** para um projeto de dois anotadores e 1.000 itens, só 33 discordâncias seriam toleráveis para a parte concordante ter 95% de ausência de ruído com 95% de confiança, o que corresponde a kappa de 0,93. Em prática, dizem, um projeto desse tamanho com dois anotadores dificilmente produz padrão de alta qualidade, apesar do kappa alto.
- **Cinco anotadores, 1.000 itens, 660 de acordo (todos iguais):** o caso que contraria a leitura usual, porque um kappa tido como baixo convive com um padrão confiável. Os 660 itens unânimes ficam com até 5% de ruído a 95% de confiança, e o que garante isso é a unanimidade aparecer com frequência suficiente, já que com cinco anotadores a chance de acordo num item difícil cai a p = 0,0625. O kappa nem tem valor único aqui: varia com a partilha dos 340 desacordos, de 0,52 se todos fossem 3 a 2 até 0,73 se todos fossem 4 a 1, e o mais provável é 0,637.

## O que o kappa informa dentro do modelo

Sob o modelo, o kappa se aproxima da proporção de itens fáceis quando as categorias são distribuídas de modo uniforme (com categorias desbalanceadas, a estimativa se afasta e tende a subestimar a proporção de fáceis, segundo simulações de Aickin 1990 citadas). Assim, kappa de 0,8 significa que cerca de 20% dos dados são difíceis, e usar tudo, sobretudo para teste, é arriscado. Pela estimativa do kappa, 800 dos 900 acordos seriam fáceis, ruído de 11%; com 95% de confiança, 13,8%. No caso dos cinco anotadores, a estimativa pontual é 3,5%, contra os 5% de alta confiança.

## Teste e treino com ruído

- **Comparar dois algoritmos:** nos itens difíceis o padrão é cara ou coroa, então há diferença esperada de desempenho puramente por acaso. No exemplo (900 itens, até 125 ruidosos), uma diferença de até 35 respostas "corretas" (3,9% do padrão) pode ser acaso; os autores propõem relatar a taxa de ruído e exigir que a diferença entre algoritmos supere a escala da diferença casual. A escala de acaso encolhe em conjuntos grandes (mesmo no corpus de 130 mil palavras de teste usado em etiquetagem morfossintática, vale conhecer o ruído estimado).
- **Efeito do tipo de ruído (Reidsma e Carletta 2008):** se o ruído é de uso excessivo de uma categoria por um anotador, as estimativas de acurácia ficam infladas; se é ruído aleatório de classificação, o desempenho aparente tende a ficar abaixo do real. Os autores sugerem testar só na parte menos ruidosa (itens concordantes) e informar o nível de ruído.
- **Treino:** o ruído de anotação difere do ruído aleatório uniforme, que o aprendizado supervisionado tolera; aqui o "cara ou coroa" se concentra nos itens difíceis, que provavelmente formam aglomerados no espaço de atributos (um classificador treinado com um anotador concorda mais com os dados dele que com os de outro). Em artigo à parte (Beigman e Beigman Klebanov 2009, *Learning with annotation noise*), mostram que o modelo de perda 0-1 pode ser vulnerável em conjuntos pequenos, e que o perceptron votado pode sofrer um viés constante com os casos difíceis, qualquer que seja o tamanho do conjunto.

## Sobre os casos difíceis

Que o "cara ou coroa" descreva os casos difíceis lhes parece plausível pela experiência própria: num trabalho deles sobre metáfora, quem tinha feito as marcações retirou algumas ao revisitá-las de quatro a oito semanas depois. O que defendem para esses casos é tirá-los do teste, não da pesquisa. Sem rótulo correto que a teoria atual determine, o caso difícil não permite comparar algoritmos com justiça, embora seja ali que a teoria tem o que aprender; o conjunto com acordo, ao contrário, representa a parte já bem formulada da teoria e pode servir de gabarito. A fronteira se move: se a teoria avançar e alguns desses itens passarem a ter tratamento sem problema, entram no conjunto. Nisso uma teoria linguística em construção difere de uma condição médica, em que se presume haver rótulo verdadeiro até para o caso mais difícil de diagnosticar (um revisor lembrou que algumas condições, como o autismo, também são só parcialmente entendidas).

## Mais anotadores

O ruído nos acordos depende do número de itens concordantes e da chance de concordância casual p; a segunda o pesquisador controla pelo número de anotadores exigidos em acordo. Com dois anotadores e 800 fáceis em 1.000, a detecção tem até 13,8% de ruído; com um terceiro, p = 0,25, esperam-se 850 acordos, com no máximo 7,7% de ruído com 95% de confiança, o que elimina cerca de metade dos acordos casuais.

## Limites do modelo, ditos pelos autores

O valor que os autores reivindicam para o modelo simples está no trajeto que ele desenha, do acordo até um padrão com ruído estimado, e na prova de que acordo geral baixo não exclui um subconjunto confiável. Ao mesmo tempo o chamam de simplificação, e deixam para a área, como agenda de pesquisa, o que ele não cobre. Com muitos anotadores, seria preciso admitir anotadores imperfeitos, que errem ao acaso até nos itens fáceis; e a dificuldade talvez não seja uma só, com graus diferentes que mudem o comportamento de quem anota.

## O que a fonte não diz

Não testa o modelo contra um gabarito conhecido ou dados reais com os dois tipos de item rotulados; os exemplos numéricos são ilustrações do cálculo (a exceção é o experimento de Poesio e Vieira, tomado de outro estudo). Não indica como identificar na prática quais itens concordantes são os difíceis.
