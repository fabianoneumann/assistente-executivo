---
titulo: "Heuristic evaluation of user interfaces"
tipo: paper
autor: "Jakob Nielsen e Rolf Molich"
url: "https://www.cs.cmu.edu/~bam/uicourse/20790utc04/cmuonly/p249-nielsen.pdf"
publicado_em: 1990-04-01
capturado_em: 2026-10-29
licenca: "© 1990 ACM (rodapé da primeira página). A nota da ACM permite copiar sem taxa para uso sem vantagem comercial direta, com o aviso de copyright; republicar exige permissão. Não é licença aberta de reuso: entra só a ficha."
areas: [agent-engineering, content-design]
tags: [heuristic-evaluation, usability, evaluator-aggregation, independent-review, inter-rater-variability, checklist, false-positives]
---

Ficha de estudo, em palavras próprias. Artigo dos anais do CHI '90 (Seattle, 1 a 5 de abril de 1990), páginas 249 a 256, DOI 10.1145/97243.97281. Nielsen estava na Universidade Técnica da Dinamarca; Molich, na Baltica A/S. Lido em 2026-10-29 no PDF de 8 páginas (cópia digitalizada com OCR; as tabelas 2, 3 e 4 foram lidas na imagem da página, porque o texto extraído não as trazia). O mesmo arquivo está no espelho da FU Berlin (mesmo tamanho em bytes). Citações literais só curtas.

## A pergunta

Quase toda avaliação de interface feita na prática é heurística (alguém olha a interface e julga pela própria opinião), mas quase nada se sabia sobre ela, porque a pesquisa a tratava como inferior. Os autores perguntam: quão bem pessoas que não são especialistas em usabilidade encontram problemas olhando uma interface com uma lista curta de princípios, e o que acontece quando se juntam os achados de várias pessoas?

## O contexto que os autores dão

- **Quatro jeitos de avaliar uma interface:** formal (técnica de análise), automático (procedimento de computador), empírico (experimento com usuários de teste) e heurístico (olhar e julgar). O formal ainda não servia a projetos reais; o automático só faz checagens primitivas; o empírico é o caminho bom, mas pouca gente faz por falta de tempo, experiência, vontade ou tradição.
- **O dado que motiva:** Milsted e colegas (1989) acharam que só 6% das empresas dinamarquesas que desenvolvem software usavam o método de pensar em voz alta, e nenhuma usava outro método empírico ou formal.
- **A estratégia:** estudar os métodos que têm chance de uso real, em vez dos que ninguém vai adotar.

## As heurísticas originais (Tabela 1)

As coleções de diretrizes da época tinham na ordem de mil regras (Smith e Mosier, 1986) e intimidavam quem desenvolve; na prática as pessoas avaliavam por intuição. Os autores cortam a base de regras em duas ordens de grandeza, para nove princípios (detalhados em Molich e Nielsen, 1990, na Communications of the ACM):

1. Diálogo simples e natural
2. Falar a língua do usuário
3. Minimizar a carga de memória do usuário
4. Ser consistente
5. Dar retorno (feedback)
6. Oferecer saídas claramente marcadas
7. Oferecer atalhos
8. Boas mensagens de erro
9. Prevenir erros

Por que nove: a lista nasceu de anos ensinando e prestando consultoria em engenharia de usabilidade; cabe numa única aula e explica uma proporção muito grande dos problemas observados em interfaces. Os princípios correspondem ao que a comunidade já reconhecia e pareceriam "óbvios", não fosse o resultado do artigo mostrar que são difíceis de aplicar. Os autores notam que usar diretrizes completas e detalhadas como checklist, sobretudo na forma de padrão de interface, já seria quase um método formal.

## Como mediram

- **Quatro experimentos, mesmo método:** cada avaliador ("sujeito") recebia um desenho de interface e escrevia um relatório apontando os problemas de usabilidade com a maior precisão possível. Cada relatório era pontuado pelo casamento com uma lista de problemas montada pelos autores.
- **A lista dos autores mudou depois da primeira leitura dos relatórios**, porque os avaliadores acharam problemas que os autores não tinham identificado. Leitura dos autores: nem especialista em usabilidade é perfeito na avaliação heurística.
- **Pontuação liberal:** contava a menção ao problema mesmo que a descrição estivesse incompleta.
- **Os avaliadores não eram especialistas em usabilidade.**

### Tabela 2: resumo dos experimentos

| Experimento | Avaliadores | Problemas conhecidos | Média de problemas achados |
| :- | -: | -: | -: |
| Teledata | 37 | 52 | 51% |
| Mantel | 77 | 30 | 38% |
| Savings | 34 | 48 | 26% |
| Transport | 34 | 34 | 20% |

### Os quatro experimentos

1. **Teledata:** o sistema de videotexto dinamarquês. Os avaliadores receberam dez cópias de tela do sistema de busca geral e do subsistema da SAS (Scandinavian Airlines), sem sistema funcionando; os autores defendem que isso é realista para avaliar na fase de especificação. Avaliadores: 37 estudantes de computação numa disciplina de design de interface, que tinham assistido a uma aula sobre as heurísticas. 52 problemas conhecidos.
2. **Mantel:** um desenho criado para o teste (o nome vem de uma telefônica fictícia, "Manhattan Telephone"), um pequeno sistema em que o cliente da telefônica disca por modem e descobre nome e endereço do assinante a partir de um número. Uma tela e algumas mensagens, especificação de uma página só. O desenho saiu como exercício num concurso da revista Computerworld dinamarquesa e chegaram 77 respostas, na maioria de profissionais de computação da indústria. Objetivo: ter dados de profissionais, não só de estudantes. Esses avaliadores **não** tiveram a aula sobre as heurísticas. 30 problemas conhecidos, listados e explicados em Molich e Nielsen (1990).
3. **Savings:** sistema de resposta por voz de uma grande caixa de poupança (saldo, câmbio etc.), operado pelo teclado de 12 teclas de um telefone de tom. 48 problemas conhecidos.
4. **Transport:** sistema de resposta por voz da empresa municipal de transporte de Copenhague (linhas de ônibus). 34 problemas conhecidos.

Os experimentos 3 e 4 testaram sistemas "vivos", com o mesmo grupo de 34 estudantes de computação, também com a aula sobre as heurísticas, sem sobreposição com o grupo do experimento 1. Quatro problemas eram de inconsistência entre os dois sistemas de voz (mesmo público, mesmo aparelho) e entraram na contagem dos dois. O exemplo: a tecla quadrado (a do jogo da velha) encerra um comando no Savings e, no Transport, que não tem tecla de fim de comando, volta ao menu principal; a mesma tecla tinha até nomes diferentes nos dois sistemas.

## Resultados

### O avaliador sozinho é fraco

- **Médias de 51%, 38%, 26% e 20%** dos problemas conhecidos nos quatro experimentos. Mesmo no melhor caso, metade. Os autores ponderam que achar alguns problemas já é muito melhor que nenhum, e que dá para completar com outros métodos.
- **A distribuição por avaliador (Figura 2)** tem forma parecida com a normal, com o Transport um pouco assimétrico: a maioria fica perto da média, poucos vão muito bem, poucos muito mal.

### Tabela 3: diferenças individuais (porcentagem dos problemas conhecidos)

| | N | Mín. | Máx. | 1º decil | 9º decil | 1º quartil | 3º quartil | Máx./mín. | D9/D1 | Q3/Q1 |
| :- | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: |
| Teledata | 37 | 22,6 | 74,5 | 26,6 | 67,9 | 43,2 | 58,5 | 3,3 | 2,6 | 1,4 |
| Mantel | 77 | 0 [6,7] | 63,3 | 23,3 | 53,3 | 30,0 | 46,7 | infinito [9,4] | 2,3 | 1,6 |
| Savings | 34 | 10,4 | 52,1 | 14,4 | 39,8 | 18,8 | 31,3 | 5,0 | 2,8 | 1,7 |
| Transport | 34 | 6,7 | 46,7 | 8,8 | 35,6 | 11,8 | 26,5 | 7,0 | 4,0 | 2,2 |
| Média | | 13,2 | 59,3 | 18,3 | 49,2 | 26,0 | 40,8 | 5,1 | 2,9 | 1,7 |

No Mantel um avaliador não achou nenhum problema; entre colchetes, o segundo pior. O Mantel ficou fora da média dos mínimos e da razão máximo sobre mínimo. (O texto do artigo fala em "cinco experimentos" ao apresentar a tabela; são quatro.)

- **Tamanho da diferença entre avaliadores:** razões Q3/Q1 em torno de 2, como as que Egan (1988) lista para edição de texto, abaixo das razões de 2 a 4 para busca de informação e programação, e próximas do 1,8 do tempo para aprender HyperCard medido com estudantes do mesmo perfil.
- **Quanto mais difícil a interface, maior a diferença entre avaliadores.** Os sistemas de voz foram os mais difíceis: têm persistência baixíssima, a mensagem some assim que é falada, e o avaliador não consegue examinar o detalhe com calma.

### O bom avaliador não é estável

Os mesmos 34 estudantes avaliaram Savings e Transport. Excluindo os quatro problemas compartilhados, a regressão do desempenho de cada um nos dois sistemas dá **R² = 0,33 (p < 0,01)**, correlação fraca (Figura 1). Alguns são melhores que outros, mas a tendência é pequena; os autores não fecham conclusão e levantam a hipótese de que a consistência seria ainda menor entre sistemas mais diferentes (estes dois eram parecidos).

### Os problemas de exemplo, com quanto foram achados

- O Mantel apaga da tela o número digitado, que some quando o nome e o endereço aparecem: 95% acharam.
- O Transport passa da leitura de um submenu para o menu principal sem pausa nem aviso de que mudou de nível: 62%.
- A mensagem de erro "UNKNOWN IP" no Teledata (IP é provedor de informação) poderia ser bem mais legível: 54%.
- Quem não tem o guia impresso nunca descobre que o Savings tem ajuda online: 35%.
- No Transport, a chave para certas informações segue a organização interna dos departamentos da empresa, e não os números de ônibus que o público conhece: 12%.

### O que conta como problema

- **Validade sem teste com usuário:** os autores não fizeram teste empírico. Defendem a lista com dois argumentos: os itens são problemas "óbvios" pelo conhecimento estabelecido da área; e pelo menos 34 pessoas percorreram cada interface, então é improvável que um problema grave não tenha incomodado ninguém o bastante para entrar num relatório.
- **Nunca se sabe se achou todos;** por isso as estatísticas são sobre os problemas "conhecidos".
- **Problema não é um conjunto fixo:** em cada uso real só parte das fraquezas aparece. O critério adotado: um item é problema se seria de esperar que incomodasse algum usuário num uso razoável. Consertar ou não é decisão posterior, pesando quantos usuários afeta e se a correção pioraria outra coisa para outros usuários; mas só se decide sobre o que foi achado.

### Falsos positivos

Houve poucos (avaliador apontando como problema o que os autores não classificariam assim), e por isso não houve análise formal. Na prática o risco é um falso positivo desviar a discussão do grupo; pela experiência deles, um falso positivo costuma ser achado por um avaliador só, e os outros conseguem convencê-lo; se não, um teste empírico arbitra.

### Juntar avaliadores

- **Achar problemas não é uma escala cumulativa (Figura 3).** Se fosse, o bom avaliador acharia todos os fáceis que o ruim acha e mais alguns difíceis. Não é assim: avaliador fraco às vezes acha problema difícil, e avaliador bom às vezes perde problema fácil. Na nota de rodapé: coeficiente de reprodutibilidade de Guttman médio de 0,85 (0,82 a 0,87), mas reprodutibilidade marginal mínima de 0,80 (0,79 a 0,82) e coeficiente de escalabilidade de só 0,06. Prever pelo quanto cada problema é achado em geral já acerta 80%; supor ordem estrita entre avaliadores sobe só para 85%. É esse desvio de 15% que torna a agregação útil: o conjunto sabe mais que o melhor do grupo.
- **Como se agrega:** vários avaliam e se junta a lista de problemas de cada um. Supõe-se uma autoridade que lê os relatórios e reconhece os problemas (um especialista, ou o próprio grupo numa reunião). Não testado; os autores acham razoável porque esses problemas ficam "óbvios" assim que alguém aponta, e pela experiência deles as pessoas costumam aceitar que algo é problema quando outro mostra. A dificuldade está em achar, não em concordar com a lista final.
- **O cálculo:** agregados hipotéticos montados por sorteio entre os avaliadores de cada experimento (não os melhores, porque numa empresa se usa quem está disponível, e o bom de um experimento pode não ser o bom do próximo), por Monte Carlo, entre cinco e nove mil sorteios por tamanho e experimento, de 1 a 30 avaliadores (Figura 4).

### Tabela 4: média de problemas achados por agregados de avaliadores

| Avaliadores no agregado | 1 | 2 | 3 | 5 | 10 |
| :- | -: | -: | -: | -: | -: |
| Teledata | 51% | 71% | 81% | 90% | 97% |
| Mantel | 38% | 52% | 60% | 70% | 83% |
| Savings | 26% | 41% | 50% | 63% | 78% |
| Transport | 20% | 33% | 42% | 55% | 71% |

- **As quatro curvas têm forma muito parecida:** sobem muito de 1 a cerca de 5 avaliadores, achatam entre 5 e 10, e o retorno decrescente chega por volta de 10. Mesmo no Transport, o mais difícil, 5 avaliadores passam da metade. A expectativa geral dos autores para 5 avaliadores é cerca de dois terços dos problemas.
- **Independência:** para o agregado render mais que os indivíduos, cada avaliador deve fazer a sua avaliação sozinho e só comparar depois de escrever o relatório. Avaliar junto tende a puxar todos para o mesmo jeito de abordar a análise e reduz a variedade, que é justamente a fonte do ganho. É hipótese dos autores, não medida.

## A recomendação

Não confiar no resultado de uma pessoa só olhando a interface. Fazer a avaliação heurística com **três a cinco avaliadores, de forma independente**, e gastar o recurso adicional em outros métodos de avaliação. Não depender só da avaliação heurística: completar com métodos como pensar em voz alta.

**Vantagens declaradas:** é barata; é intuitiva e fácil de motivar as pessoas a fazer; não exige planejamento prévio; pode ser usada cedo no desenvolvimento.

**Desvantagens declaradas:** às vezes aponta o problema sem sugerir como resolver; é enviesada pela mentalidade atual dos avaliadores e normalmente não produz avanços de desenho. Nas palavras deles, o método "normally does not generate breakthroughs in the evaluated design".

## Limites declarados

- Avaliadores com um nível só de experiência (não especialistas). Os autores acreditam, sem evidência formal, que especialistas em usabilidade seriam melhores, e que o que ajuda é ter observado usuários reais ao longo dos anos, mais do que saber conduzir teste.
- Só problemas individuais, na fase de polir um desenho já completo. Avaliação holística (escolher entre dois produtos ou entre duas abordagens de desenho) provavelmente pede outras técnicas.
- Só interfaces pequenas; não se sabe o que acontece com interfaces muito maiores.
- Só desenhos completos (protótipo em papel ou sistema funcionando); o "laço interno" do desenho, em que o designer avalia alternativas rapidamente, não foi estudado, embora provavelmente seja heurístico e parte dos resultados possa valer.
- A validade dos problemas não foi conferida com usuários; a autoridade que consolida o agregado é suposta, não testada; os agregados são simulados, não formados num projeto real.
- Falsos positivos sem análise formal.

## Divergência com resumos de terceiros

O resumo do artigo diz que cada avaliador achou "entre 20 e 51%" dos problemas; isso é a faixa das **médias por experimento**. Por avaliador, a faixa vai de 0% (um avaliador do Mantel) a 74,5% (o melhor do Teledata), Tabela 3. Resumos de terceiros costumam atribuir ao método números como "um avaliador acha 35%, cinco acham 75%"; esses números não estão neste artigo (pelo que se costuma citar, vêm de trabalhos posteriores do próprio Nielsen com outros projetos; não conferido nesta captura). Aqui, cinco avaliadores dão de 55% a 90% conforme a interface, cerca de dois terços em média.
