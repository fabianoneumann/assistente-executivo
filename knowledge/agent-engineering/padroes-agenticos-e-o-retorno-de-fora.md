# Os padrões agênticos do Andrew Ng e o retorno de fora

O que Andrew Ng ensina sobre fluxos de agente, de onde vem o número que ele usa, o que a reprodução de fora achou e como isso cruza com o que a base já sabia sobre autocorreção e multiagente.

Fontes: [[2026-11-13-the-batch-padroes-agenticos-parte-1-2024]], [[2026-11-13-the-batch-padroes-agenticos-parte-2-reflexao-2024]], [[2026-11-13-zhong-ldb-depurador-por-execucao-2024]], [[2026-11-13-kapoor-narayanan-placares-e-curvas-de-pareto-2024]], [[2026-11-13-the-batch-tarefas-de-julgamento-2026]], [[2026-11-13-deeplearning-ai-curso-agentic-ai]]; da base, [[2026-10-28-reflexion]], [[2026-10-28-kamoi-quando-llms-se-autocorrigem]], *Building effective agents*, de Erik Schluntz e Barry Zhang (Anthropic) (https://www.anthropic.com/engineering/building-effective-agents). O paper "AI Agents That Matter" (Kapoor e outros, arXiv 2407.01502) tem ficha na parte das linhas de base e da tabela A1: [[2026-11-17-kapoor-agentes-que-importam-humaneval-2024]].

## A resposta curta

Ng ensina quatro padrões (reflexão, uso de ferramentas, planejamento, colaboração multiagente) e, em março de 2024, disse que os fluxos de agente iam puxar muito progresso naquele ano, "perhaps" mais que a próxima geração de modelos, com um gráfico do HumanEval em que o GPT-3.5 "num laço de agente" chega a 95,1%. O ponto de 95,1% do gráfico é um depurador que **roda o código** (na cor de uso de ferramentas do gráfico), aplicado a programas gerados pelo Reflexion com o GPT-4; um grupo de Princeton não reproduziu o número (máximo de 91,5% em cinco execuções), chamou de incorreta a frase do Ng, escreveu que os 48,1% e 67,0% sem exemplos parecem vir do relatório técnico do GPT-4 de março de 2023 (com os prompts do paper, os modelos sozinhos dão 73,9% e 89,6%) e que linhas de base simples e mais baratas, que refazem quando o teste falha, chegam a acerto parecido ao dos agentes. Leitura do assistente: o que a evidência sustenta é o laço com **retorno de fora** (teste, execução, medida), não a autocrítica do modelo sozinha, e isso bate com o que o próprio Ng escreve na carta da reflexão, ensina no curso (avaliar o impacto da reflexão) e disse em outubro de 2026 sobre tarefas verificáveis.

## Os quatro padrões, como Ng os define (2024)

| Padrão | O que é, pela carta de 20/03/2024 |
|---|---|
| Reflexão | o modelo examina o próprio trabalho para achar como melhorar |
| Uso de ferramentas | o modelo recebe ferramentas (busca na web, execução de código, outras funções) para colher informação, agir ou processar dados |
| Planejamento | o modelo monta e executa um plano de vários passos |
| Colaboração multiagente | mais de um agente divide a tarefa e debate ideias |

A abertura da carta compara o uso sem exemplos (*zero-shot*) a escrever um texto do começo ao fim sem poder apagar, e o fluxo de agente a esboçar, pesquisar, rascunhar, reler e revisar. Ng diz que a equipe dele no AI Fund usa os padrões em muitas aplicações. Na carta da reflexão, ele diz que a reflexão vai além quando o modelo recebe ferramentas para avaliar a saída (rodar testes, buscar na web) e quando dois agentes se dividem entre gerar e criticar, e recomenda o Self-Refine, o Reflexion e o CRITIC. O curso "Agentic AI" (DeepLearning.AI; lançado em 30/09/2025 pelos metadados da página, atualizado em 30/10/2026) ensina os quatro padrões em Python intermediário, com módulos de avaliação ("evals"), análise de erro e "avaliar o impacto da reflexão"; dá para assistir de graça, e o certificado é do plano pago.

## O número do HumanEval, em camadas

| Camada | O que diz | Fonte |
|---|---|---|
| A frase de Ng | GPT-3.5 sem exemplos 48,1%; GPT-4 67,0%; "wrapped in an agent loop, GPT-3.5 achieves up to 95.1%"; resultados de vários grupos de pesquisa, compilados pela equipe dele | carta de 20/03/2024 |
| O gráfico da carta | o ponto de 95,1% sob GPT-3.5 é "LDB + Reflexion", na cor de uso de ferramentas; o Reflexion sozinho (que também roda testes que ele mesmo escreve, [[2026-10-28-reflexion]]) aparece só sob GPT-4, perto de 91 | imagem da carta (leitura do gráfico, "cerca de") |
| O paper do LDB | o GPT-3.5 como depurador, que roda o programa e confere os valores bloco a bloco, sobre programas do Reflexion tirados do repositório oficial: 91,5% → 95,1%; sobre programas do próprio GPT-3.5: 73,8% → 82,9%; do GPT-4: 87,2% → 89,6% | Zhong e outros, Tabela 2 |
| O Reflexion | 91,0% no HumanEval, sobre o GPT-4 | [[2026-10-28-reflexion]] |
| As versões do LDB | a v1 (25/02/2024) dizia ter escolhido a versão do Reflexion "based on GPT-3.5"; a v6 (06/06/2024) tirou a frase e manteve o 95,1% | ficha do LDB; Princeton cita a frase da v1 |
| A reprodução | Princeton não reproduziu: máximo de 91,5% em cinco execuções do LDB (Reflexion, GPT-3.5); os programas do repositório do Reflexion usados pelo LDB dependem do GPT-4, e no LDB o GPT-3.5 "is only used to find bugs"; os autores do LDB reconheceram e disseram que iam atualizar | Kapoor, Stroebl e Narayanan, 30/04/2024 |
| A linha de base | os 48,1% e 67,0% do post parecem copiados do relatório técnico do GPT-4 (março de 2023); com os prompts do paper do LDB, o GPT-3.5 sozinho dá 73,9% e o GPT-4 sozinho, 89,6%; para Princeton, o post superestima o ganho atribuído aos agentes | idem |

Com os mesmos prompts, a comparação que sustentava a tese se inverte no HumanEval: o GPT-4 sozinho (89,6%, Princeton) passa o GPT-3.5 com o depurador sobre os próprios programas (82,9% no paper; 80,2% na reprodução, pelo apêndice de "AI Agents That Matter"). Leitura do assistente: o que o HumanEval sustenta não é "o fluxo vale mais que o modelo", e sim que o depurador que roda o código melhora qualquer semente, em poucos pontos (de +2,4 a +9,1 na Tabela 2).

## O que a reprodução de fora mostrou (abril de 2024)

Kapoor, Stroebl e Narayanan rodaram os agentes de código do HumanEval cinco vezes cada, com o custo em dólar: três linhas de base simples, todas refazendo quando falham os testes do enunciado: tentar de novo com o GPT-4 (92,0% na tabela A1 do paper deles), subir a temperatura a cada tentativa (93,2%, sem diferença significativa de acerto para o melhor agente, 93,3%) e escalar de modelo em modelo (85,0%, mais barata que o LDB com GPT-3.5, que reproduziu em 80,2% sobre os próprios programas); o Reflexion e o LDB custaram mais de 50% acima da estratégia de subir a temperatura. Leitura do assistente: as linhas de base também usam retorno de fora (o teste do enunciado), e foi isso que se reproduziu. A recomendação deles: medir acerto e custo juntos, numa curva, e testar no próprio domínio, porque o HumanEval é um indicador grosseiro.

## Onde isso cruza com a base

- **Autocorreção:** a revisão de Kamoi (TACL 2024) não acha autocorreção intrínseca bem-sucedida em tarefa geral; funciona onde conferir é mais fácil que gerar, ou com retorno externo ([[termos-dos-lacos-de-avaliacao]]). O próprio paper do LDB atribui o ganho à informação de execução, como suplemento externo à autocorreção, e cita Huang sobre a autocorreção limitada.
- **Tarefas verificáveis:** em 16/10/2026, Ng escreveu que a distância entre o desempenho em tarefas verificáveis (código, matemática, com resposta conferível automaticamente) e em tarefas de julgamento é maior do que se pensa, e que o progresso nas primeiras leva a generalizar demais. Leitura do assistente: é a mesma fronteira, dita por ele dois anos e meio depois da carta dos padrões.
- **Multiagente:** com o mesmo orçamento, um agente só empata ou ganha de desenhos multiagente em raciocínio de vários passos ([[orquestracao-de-skills-e-agentes]], Tran e Kiela 2026); a Anthropic manda começar pelo mais simples e só acrescentar complexidade que melhore comprovadamente (*Building effective agents*, de Erik Schluntz e Barry Zhang (Anthropic)).
- **Num ambiente de agentes:** o código e um classificador calibrado (como um modelo de decisão tipado) são o retorno extrínseco dos laços de avaliação, e o juiz da mesma família do modelo que gerou fica perto do intrínseco ([[termos-dos-lacos-de-avaliacao]]).

## O que falta saber

- Se os números do HumanEval valem para tarefas fora de código; nenhuma fonte desta página mede isso.
- A versão atualizada do LDB depois da reprodução (os autores disseram que iam atualizar; a v6 lida ainda traz o 95,1%).
- O que as partes 3 a 5 das cartas de 2024 (ferramentas, planejamento, multiagente) dizem: não lidas nesta rodada.
