---
titulo: "Information Foraging in Information Access Environments"
tipo: paper
autor: "Peter Pirolli e Stuart Card (Xerox Palo Alto Research Center)"
url: "https://www.chi1995.chistatic.hosting.acm.org/proceedings/papers/ppp_bdy.htm"
publicado_em: 1995
capturado_em: 2026-11-03
areas: [journalism]
tags: [information-foraging, information-seeking, optimal-foraging-theory, information-patch, information-diet, marginal-value-theorem, scatter-gather, browsing, search-strategy, human-computer-interaction]
licenca: "Protegido: '© ACM' no topo da página, com link para o aviso de copyright da ACM; o OpenAlex marca o DOI 10.1145/223904.223911 como acesso fechado e sem licença. Entra só a ficha; o integral está na url (versão HTML dos anais do CHI '95) e na ACM Digital Library."
---

Ficha de estudo, em palavras próprias. Artigo de Peter Pirolli e Stuart Card, do Xerox PARC, nos anais do CHI '95 (ACM Conference on Human Factors in Computing Systems), p. 51 a 58 segundo o OpenAlex; DOI 10.1145/223904.223911. Texto lido: a versão HTML dos anais no site estático do CHI '95 (a url), inteira, e as imagens que ainda abrem nesse site: a Fig. 2, a Fig. 3, a Tabela 1, as equações 7 a 11 e dois parágrafos que a página traz como imagem. As outras imagens (a Fig. 1, as equações 1 a 6 e 12 a 18, os símbolos soltos no meio do texto e dois dos três trechos da "análise do espaço de estados") devolvem erro 404 no site, e a Wayback Machine estava fora do ar na captura; o que dependia delas fica como lacuna nesta ficha.

## O que o artigo propõe

A teoria do forrageio de informação (*information foraging theory*) analisa as atividades humanas com tecnologias de acesso à informação. Vem da teoria do forrageio ótimo, da biologia e da antropologia, que estuda o valor adaptativo das estratégias de busca de comida. Aplicada à interação humano-computador, ela pesa o valor da informação obtida contra o custo da atividade de obtê-la. Os autores ilustram a teoria com tarefas de busca numa interface chamada Scatter/Gather, que mostra ao usuário uma visão geral navegável, calculada automaticamente, do conteúdo de uma coleção de documentos organizada numa hierarquia de grupos (*clusters*).

**De onde parte.** Num mundo rico em informação, dizem os autores (retomando trabalhos anteriores deles), o problema de design não é coletar mais informação, e sim otimizar o tempo do usuário: aumentar a informação relevante obtida por unidade de tempo gasto. A teoria complementa os modelos de processamento de informação da família GOMS, mas olha para escalas de tempo maiores, para a estrutura de custos do ambiente externo e para a adaptação humana. Pelas faixas de tempo de Newell, as atividades de busca e de construção de sentido (*sensemaking*) vão do meio da faixa cognitiva (cerca de 100 ms a 10 s) à faixa racional (minutos a horas) e talvez à social (dias a meses). Quanto maior a escala, mais o comportamento se explica pelas restrições e possibilidades do ambiente da tarefa do que pelo mecanismo interno; em vez da racionalidade normativa clássica, supõe-se que o comportamento se justifica pelo ajuste adaptativo à sua ecologia. É a postura ecológica: os modelos de processamento dizem *como* a cognição opera; os ecológicos dizem *por que* opera assim, dado o contexto.

## Forrageio de informação como tarefa

Forragear informação é avaliar, buscar e manusear fontes de informação; a busca é adaptativa na medida em que usa bem o que se sabe sobre o valor esperado da informação e o custo esperado de acessá-la e extraí-la. A palavra evoca o animal procurando alimento e liga o trabalho à teoria técnica do forrageio ótimo. Animais se adaptam para, entre outras coisas, aumentar a taxa de ganho de energia, e desenvolvem métodos diferentes: o lobo caça a presa; a aranha tece a teia e deixa a presa vir. A estratégia do lobo lembra a recuperação de informação clássica; a da aranha, a filtragem de informação. Caçadores-coletores humanos caçam em grupo quando a variância de achar comida é alta, aceitando uma média esperada menor para diminuir a chance de passar dias sem comer; de modo parecido, os autores observaram em campo analistas de mercado que tinham a ética de repassar informação uns aos outros, forrageando em grupo para reduzir a chance de perder literatura importante.

**Os três componentes de um modelo de otimização:**

- *Decisões:* quais problemas do agente se analisam (perseguir ou não um tipo de item ao encontrá-lo; quanto tempo dedicar a uma coleção; que movimento fazer na navegação; que estratégia sob incerteza; quanto compartilhar recursos).
- *Moeda:* como as escolhas se avaliam. Um critério de existência tem uma moeda e um princípio de escolha (maximizar, minimizar, estabilizar). Os modelos biológicos usam energia como moeda; a teoria do forrageio de informação usa o valor da informação.
- *Restrições:* o que limita e relaciona decisões e moeda, vindo da estrutura da tarefa, da tecnologia da interface e das capacidades e do conhecimento dos usuários.

**A tarefa de fora.** O forrageio de informação costuma estar dentro de outra tarefa, que define o valor e o custo e muda com o tempo. O valor da informação e a relevância de uma fonte não são propriedades do documento: só se avaliam em relação à tarefa de fora. Em geral essa tarefa é um problema mal estruturado que pede conhecimento a mais para definir objetivos, caminhos e heurísticas (escolher um bom programa de pós-graduação, montar um plano de aposentadoria, uma estratégia de negócio, escrever um artigo científico aceitável), e o valor da informação externa está, muitas vezes, na melhora do resultado dessa tarefa.

**A ressalva sobre otimização.** Usar modelos de otimização não é supor que as pessoas sejam racionais no sentido clássico, com informação perfeita e capacidade de cálculo infinita. A hipótese melhor é a da racionalidade limitada, ou do *satisficing* de Simon, que pode ser descrita como otimização local (subida de encosta) com recursos limitados e informação imperfeita como restrições. Os modelos não dizem que o forrageador chega ao ótimo; descrevem as possibilidades de um nicho, uma adaptação vantajosa se nada a bloquear. Para os autores, eles preenchem o que Anderson chama de teoria no nível racional do acesso à informação.

## Os modelos e os exemplos

Os autores apresentam três análises sobre o Scatter/Gather. As duas primeiras, o modelo de manchas de informação (*information patch*) e o modelo de dieta de informação (*information diet*), vêm quase direto da teoria do forrageio ótimo e da equação do disco de Holling: a taxa de ganho R é o ganho líquido U dividido pelo tempo total gasto buscando (Ts) e explorando (Th). (As equações 1 e 2 estão em imagens que não abriram.) A terceira é um modelo dinâmico, que inclui as duas primeiras como partes e usa programação dinâmica para achar a estratégia ótima.

**A interface.** O Scatter/Gather (a interface foi feita por Marti Hearst no PARC) agrupa a coleção, por exemplo, em B = 10 grupos de documentos parecidos, cada um numa área da tela, com as palavras típicas do grupo e os títulos dos três documentos mais representativos. O usuário junta (*gather*) alguns grupos e pede ao sistema para espalhar (*scatter*) esse subconjunto em outros B grupos. O agrupamento usa similaridade entre os textos e roda em tempo de interação constante.

### Exemplo 1: forragear em manchas de informação

Encontros com informação valiosa costumam ser agrupados no espaço e no tempo: os itens vêm em coleções (bibliotecas, bases, agências de notícias), como a comida vem em manchas de qualidades diferentes, e o forrageador precisa decidir como dividir o tempo entre elas. No Scatter/Gather, cada grupo é uma mancha: forragear nele é abrir a lista de títulos, rolar, e para cada título decidir se é relevante; o relevante é selecionado, recortado e colado numa janela de registro. Relevantes e irrelevantes vêm misturados ao acaso.

Esse ciclo se descreve por uma função de ganho acumulado gi(t), quanto valor se obtém em t numa mancha do tipo i. Nos estudos, as instruções definiam o valor como o número de documentos relevantes coletados, e a proporção de relevantes num grupo é a precisão P dele. Com o tempo de varrer e julgar um título (ts) e o de manusear um relevante (th), e com os relevantes espalhados ao acaso, o ganho cresce em linha reta com o tempo, como a curva gA(t) da Fig. 2.

Os autores mostram então o que mudaria com uma função que a interface ainda não tinha: ordenar os títulos de cada grupo pela similaridade com a consulta. (Uma nota diz que o Scatter/Gather tinha busca por similaridade na coleção toda, mas não restrita aos grupos escolhidos.) Com os títulos ordenados pela probabilidade de relevância, o ganho vira uma curva de retornos decrescentes, gB(t): muitos relevantes no começo da lista e cada vez menos adiante.

**O teorema do valor marginal de Charnov.** Os modelos simples de manchas dizem qual é a taxa máxima de ganho e quando parar de forragear numa mancha. Cada tipo de mancha tem a sua função de ganho e uma taxa de encontro (quantas manchas daquele tipo se encontram por tempo de trabalho); o problema é escolher os tempos de permanência que maximizam a taxa total R. O teorema diz que a taxa de longo prazo é máxima quando se deixa cada mancha no momento em que o ganho instantâneo nela cai até a taxa média de longo prazo de todas as manchas. Uma consequência que Charnov mostra: quanto melhor o ganho geral do ambiente, menor o tempo ótimo em cada mancha. (Uma nota esclarece que o modelo supõe que se maximiza o ganho líquido médio de longo prazo, e remete a Hames para outras políticas.)

**A Fig. 2.** O tempo de viagem entre manchas (o inverso da taxa de encontro) vai no eixo horizontal, da origem para a esquerda. A reta que parte desse ponto à esquerda e tangencia a curva de ganho dá, na inclinação, a taxa máxima (RB) e, no ponto de tangência, o tempo ótimo na mancha. Melhorando ainda mais a ordenação dos relevantes, a curva vira gC(t): a taxa sobe para RC e o tempo ótimo em cada grupo cai. Com as funções e quantidades medidas, daria para prever com precisão o efeito de uma mudança de interface; só com o raciocínio gráfico já saem previsões qualitativas.

Os autores dizem suspeitar que, na maioria das tarefas, a taxa de obter informação relevante para a tarefa de fora diminui com o tempo (ou é finita), por exemplo quando há redundância entre documentos relevantes, e que por isso o modelo de manchas teria ampla aplicação.

### Exemplo 2: a dieta de informação

Escolher quais grupos perseguir é como o predador que escolhe que presas perseguir ao encontrá-las: os modelos de seleção de presa, ou de dieta. Os autores destacam três resultados:

- **Ordenar pela lucratividade:** lucratividade é o ganho líquido esperado dividido pelo tempo de manusear o item; no Scatter/Gather, a dos grupos é proporcional à precisão deles. Começando pelos mais lucrativos, um item de nível mais baixo só entra na dieta se a sua lucratividade for maior ou igual à taxa média de ganho de todos os itens acima dele; incluir um item abaixo dessa média só baixa a média. É o **princípio da oportunidade perdida**: manusear o item fraco é perder a chance de ir atrás de um melhor.
- **Regra do zero ou um:** os itens de um mesmo nível de lucratividade entram todos ou nenhum.
- **Independência da taxa de encontro:** entrar ou não na dieta depende só da lucratividade do item, não de com que frequência ele aparece. O exemplo dos autores: se ler mala direta é pouco lucrativo porque há coisa melhor a fazer, a decisão de ignorá-la vale qualquer que seja a quantidade de mala direta que chega.

### Exemplo 3: um modelo dinâmico

Os modelos de manchas e de dieta são estáticos (não levam em conta a mudança de estado ao longo do tempo) e olhavam partes isoladas da interação; o terceiro trata a navegação pela hierarquia de grupos como otimização dinâmica.

**Tarefa e medidas.** O Scatter/Gather rodava sobre o corpus Tipster do NIST, com mais de um milhão de documentos (Wall Street Journal, agência AP, resumos técnicos do Departamento de Energia, Federal Register, artigos de computação da Ziff-Davis), usado pela comunidade de recuperação de informação porque tem consultas com listas de documentos julgados relevantes ou não por especialistas, um padrão comum de comparação, ainda que não uma medida objetiva de sucesso. Quatro pesquisadores do PARC, entre eles os dois autores, com 96, 20, 10 e 2 horas de experiência na interface, tentaram achar o máximo de documentos relevantes para o máximo de consultas do TREC em uma hora. As sessões foram gravadas em vídeo e codificadas ao segundo, e o tempo de resposta do sistema foi medido à parte. Os custos (Tabela 1): tempo médio por consulta T = 720 s; varrer um grupo e julgar a relevância, 3 s; acrescentar um grupo à lista de junção, 5 s; varrer um título e julgar, 1 s; selecionar, recortar e colar um título, 5 s; o sistema espalhar novos grupos, 23 s; mostrar os títulos de um grupo, 20 s.

**Programação dinâmica.** Define-se uma variável de estado X e uma função de avaliação do estado no prazo final T, que nessa tarefa é o número de documentos relevantes coletados até o fim. Cada operador muda o estado e tem um custo de tempo; o valor final de um estado (quantos documentos se espera ter no fim, partindo dele) se calcula de trás para a frente: supondo que, a partir de t + 1, se seguem as escolhas ótimas (a política ótima), faz-se a escolha ótima em t.

**O modelo do Scatter/Gather.** O estado tem seis componentes: o número de documentos no grupo atual, o de relevantes nele, os já forrageados nele, os subgrupos forrageados, os documentos coletados até ali e o histórico de agrupamento (o caminho de junções e espalhamentos). O estado inicial médio: um milhão de documentos, mil relevantes, nada forrageado nem coletado. Ao mostrar os títulos de um grupo, o número de relevantes coletados é todos eles, se houver tempo para varrer o grupo inteiro, ou quantos couberem no tempo restante; depois, se o custo não estourar o prazo, a interação volta ao grupo de cima e o estado se atualiza. A cada nó há 10 subgrupos; das 2⁹ − 2 junções possíveis, a análise de dieta indica que basta considerar nove: ordenar os grupos pela lucratividade (proporcional à precisão) e juntar os 1, 2, ... 9 melhores. Por razões práticas, só se consideraram os três melhores. (As equações 12 a 18, com os detalhes de cada operador e dos custos, estão em imagens que não abriram; o texto diz que, juntando i de B subgrupos, o número de documentos e o de relevantes do novo grupo se calculam para o caso médio.)

**A análise do espaço de estados (Fig. 3).** Dos três trechos que a página traz como imagem, só o do meio abriu. Ele explica os painéis: (a) o número de documentos que se espera ainda ganhar até o prazo, de forma ótima, em cada estado, com cada estado desenhado como uma caixa mais ou menos preenchida conforme a precisão; esse número cai à medida que o tempo disponível e a precisão diminuem; (b) os documentos já coletados em cada estado ao longo do tempo, e leva cerca de metade do tempo da tarefa para começar a coletar; (c) a soma dos dois, que é o valor final de cada estado; o painel (d) mostra a precisão por tempo. A conclusão do texto: espalhar e juntar grupos é o ótimo no começo, quando sobra tempo e a precisão é baixa; mostrar títulos e selecionar é o ótimo depois, ou com precisão alta; o número ótimo de grupos escolhidos tende a crescer com a precisão do estado, e a precisão cresce com o tempo.

## Conclusão dos autores

Os autores citam o prefácio de *Foraging Theory*, de Stephens e Krebs: o livro estuda o comportamento alimentar como um engenheiro estuda uma máquina nova, perguntando para que ela serve, com a diferença de que, para o biólogo, o desenho é produto da seleção natural. O artigo diz tentar inverter a analogia: usar a teoria da ecologia comportamental para analisar as ecologias de informação e o design de sistemas interativos, na esperança de dar novas ferramentas a esse design.

## Tudo o mais que ensina

- **Lobo e aranha:** recuperação de informação (ir atrás) e filtragem (deixar vir) são as duas estratégias que os autores associam ao forrageio animal.
- **Forragear em grupo contra a variância:** a observação dos analistas de mercado que se repassam informação para não perder literatura importante é o paralelo humano da caça em grupo quando achar comida é incerto.
- **Relevância situacional:** o valor e a relevância dependem da tarefa de fora e mudam com o tempo; os autores apoiam isso em Repo (valor da informação) e em Schamber, Eisenberg e Nilan (relevância dinâmica e situacional), e citam Bates (1989, berrypicking) entre as referências dessa ideia.
- **Ordenar dentro da mancha muda o tempo ótimo nela:** pela Fig. 2, ordenar por relevância aumenta a taxa geral e reduz o tempo que vale passar em cada grupo, e a previsão sai só do raciocínio gráfico.
- **Mala direta e o princípio da oportunidade perdida:** a regra para ignorar uma fonte fraca não depende do volume em que ela chega.
- **Medidas da interface (Tabela 1):** os custos em segundos de cada operação do Scatter/Gather, que alimentam o modelo dinâmico.
