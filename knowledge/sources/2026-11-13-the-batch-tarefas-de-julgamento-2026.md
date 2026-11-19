---
titulo: "Judgement Tasks Is Where Humans Have the Edge: Don’t Overgeneralize from Progress in Math and Code — The Hardest AI Problems Still Require More Work"
tipo: artigo
autor: "Andrew Ng"   # carta assinada "Andrew", seção "Letters"; a página não traz o sobrenome, e o autor no cabeçalho e no JSON-LD é "Analytics DeepLearning.AI"; a atribuição vem da página Writing de andrewng.org, que lista a carta com a data de 16/10/2026
url: "https://charonhub.deeplearning.ai/formal-verification-meets-unverifiable-judgement/"
publicado_em: 2026-10-16   # a página mostra "16 Oct 2026"; meta article:published_time e JSON-LD datePublished 2026-10-16T14:30:41Z; modificada em 2026-11-08 (article:modified_time)
capturado_em: 2026-11-13
areas: [agent-engineering]
entrada: pesquisa
tags: [andrew-ng, the-batch, judgement-tasks, verifiable-tasks, reinforcement-learning, reward-functions, evals, ai-hype, jagged-intelligence, context-advantage]
licenca: "sem licença aberta na página; ficha de prosa em palavras próprias, com citações curtas exatas"
---

# The Batch, tarefas de julgamento: onde o progresso da IA anda mais devagar

Ficha de prosa (`knowledge/sources/README.md`, item 2): é um ensaio curto de opinião de um autor de referência, cujo raciocínio vale comparar com o de outros, e não uma fonte técnica de dados ou receita; por isso vai em prosa, organizada por perguntas próprias (a distinção, as causas, o aviso, a conclusão) e não pelos parágrafos da carta, escrita a partir de notas. Não há integral: a página é protegida.

**Proveniência.** Carta do The Batch, da DeepLearning.AI, seção "Letters", assinada "Andrew" e fechada com "Keep building!", em https://charonhub.deeplearning.ai/formal-verification-meets-unverifiable-judgement/ (a mesma URL no `canonical` e no `og:url`). HTML baixado em 2026-11-13, com o texto do bloco principal extraído para a cópia de trabalho e lido no texto bruto em 2026-11-13. Data conferida no HTML: "16 Oct 2026" no cabeçalho, publicada em 2026-10-16 e modificada em 2026-11-08 pelos metadados; a página não diz o que mudou. A página marca o tempo de leitura em 2 minutos. Título conferido no `<title>` e no `og:title`, iguais ao campo `titulo`; o subtítulo repete a frase de abertura da carta. Cobertura: o texto inteiro da carta, de "Dear friends" à assinatura; o link "written before" (para a carta `three-key-loops-for-building-great-software`) não foi aberto.

**Conferência lado a lado** (2026-11-13, pela régua do `README.md` desta pasta, item 2): contam as frases de prosa; as três citações literais estão à parte. Resultado: 9 de 16 frases seguem a fonte, numa contagem conservadora (detalhe no fim da ficha); a maior sequência na ordem da fonte é de 2 frases seguidas. A carta é curta e quase cada frase dela carrega uma ideia, então a ficha que cobre todas as ideias as reescreve uma a uma; a proteção está na ordem, que é a das perguntas da ficha e não a da carta. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: o script não mede tradução, e a conferência é esta conta), com 0 de 31 unidades coladas e nenhum trecho.

## Em uma frase

Ensaio contra uma generalização: do avanço dos modelos de linguagem em matemática e código não se tira que eles julguem bem, e a distância entre as duas coisas, diz o autor, é maior do que se pensa.

## A distinção

O critério que separa os dois grupos é haver ou não um gabarito que um programa possa conferir. Matemática e código têm esse gabarito; a resposta a uma reclamação de cliente, a escolha de um recurso de produto, a estratégia de um negócio e o plano de coleta de dados de um projeto de IA não têm, e ainda assim nelas há resposta melhor e pior.

## Por que uma anda mais rápido que a outra

São quatro razões, e todas favorecem a tarefa conferível. A mais visível está na avaliação: montar conjunto de teste para ela é fácil, e por isso o progresso medido parece maior do que é. A mais formal vem da teoria do aprendizado, que mostra o algoritmo aprendendo mais rápido quando o erro zero é alcançável (o caso que a literatura chama de realizável) do que quando o melhor erro possível, o erro de Bayes, fica acima de zero. As outras duas estão no treino: no supervisionado, o rótulo da tarefa conferível não se discute, venha de máquina ou de anotador, e no julgamento até defini-lo é trabalho; no reforço, apontado pelo autor como grande motor do avanço recente dos modelos de linguagem, um ambiente simulado deixa o modelo ensaiar abordagens, uma função de recompensa diz quais deram certo, e os pesos passam a favorecê-las.

## O aviso

Para o autor, o avanço nas tarefas conferíveis, somado ao entusiasmo em torno de AGI e de RSI (siglas que a carta não explica), está levando as pessoas a supor que a IA também julga bem. Não seria a primeira vez: Deep Blue no xadrez, Watson no Jeopardy e AlphaGo no Go despertaram, cada um, expectativas de uso imediato em outras áreas que se mostraram exageradas, e a tendência de generalizar a partir de um recorte estreito é antiga.

## O que a carta conclui

A posição final é otimista, com prazo: a IA deve chegar a fazer bem também o julgamento, mas há muito trabalho pela frente, e o caminho já se conhece (dados de um domínio, ajuste fino supervisionado, funções de recompensa escritas com cuidado para traduzir o objetivo). Esse caminho é mais lento e mais trabalhoso que o das tarefas conferíveis, e as empresas vão pagá-lo nas aplicações em que ele valer a pena. Enquanto isso, quem constrói sistemas de IA deve contar com o julgamento humano continuando a pesar à medida que o conferível se automatiza: decidir pede garimpar contexto numa massa enorme de dados brutos e achar as poucas peças que mudam a decisão, e nessa vantagem de contexto, que o autor diz já ter defendido antes, as pessoas seguem à frente dos modelos em muitas tarefas, por muito tempo.

## Citações

- "The gulf between LLM performance on verifiable tasks vs. unverifiable tasks that require judgement is larger than most people realize." (a frase de abertura, repetida no subtítulo)
- "Intelligence is jagged, and we do have a recipe for improving AI’s capability for judgement tasks" (o parágrafo do ajuste fino supervisionado)
- "I expect people to continue to have a context advantage over LLMs on many tasks for a long time." (o último parágrafo)

## Lacuna

A carta não traz medida nenhuma da distância que anuncia: nem benchmark, nem número, nem exemplo de modelo que falhou num julgamento. Não define AGI nem RSI. Não diz o que seria um bom conjunto de teste para tarefa de julgamento nem como escrever as funções de recompensa que recomenda. O título escreve "Judgement Tasks Is", e o texto alterna as grafias "judgement" e "judgment"; o endereço da página (`formal-verification-meets-unverifiable-judgement`) não corresponde ao título.

## Detalhe da conferência lado a lado

Total de 16 frases: 1 em "Em uma frase", 2 em "A distinção", 4 em "Por que uma anda mais rápido", 2 em "O aviso", 3 em "O que a carta conclui" e 4 na lacuna (as notas de formato, proveniência e conferência ficam fora). Contagem conservadora: entra como "segue" toda frase que traduz o miolo de uma frase da carta, mesmo reorganizada, e toda que junta frases da carta na ordem dela. Seguem 9: a de "Em uma frase" (o título e a abertura, na ordem); a segunda de "A distinção" (funde as três frases seguintes do primeiro parágrafo, reagrupando os exemplos); três de "Por que" (a da avaliação, que segue a última frase do parágrafo da história; a da teoria do aprendizado; e a do treino, que junta o parágrafo do supervisionado e o do reforço em ordem inversa); as duas de "O aviso" (a do entusiasmo com AGI e RSI segue uma frase do penúltimo parágrafo; a dos três marcos funde as três frases do parágrafo da história, com a ideia geral no fim); e duas de "O que a carta conclui" (a do caminho mais lento junta duas frases do parágrafo do ajuste fino; a da vantagem de contexto junta as duas frases do último parágrafo). A maior sequência na ordem da carta é de 2 (as duas últimas frases da conclusão); "Por que" e "O aviso" andam para trás na carta, de frase a frase. Não seguem 7: a do critério da distinção, a abertura de "Por que", a primeira da conclusão (junta o otimismo do penúltimo parágrafo com a receita do quinto, fora de ordem) e as quatro da lacuna.
