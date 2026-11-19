---
titulo: "Reflexion: Language Agents with Verbal Reinforcement Learning"
tipo: paper
autor: "Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao"
url: "https://arxiv.org/abs/2303.11366"
publicado_em: 2023-03-20
capturado_em: 2026-10-28
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [reflexion, verbal-reinforcement, episodic-memory, self-reflection, iterative-refinement, coding-agents]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 20/03/2023, v4 (lida) em 10/10/2023. Publicado no **NeurIPS 2023** (pôster; a página do arXiv não diz o venue, confirmado em [neurips.cc/virtual/2023/poster/70114](https://neurips.cc/virtual/2023/poster/70114) e no repositório oficial). A página do NeurIPS lista os autores sem Edward Berman; o arXiv e o repositório o incluem. Lido em 2026-10-28, na pesquisa.

## A ideia

Ensinar um agente por tentativa e erro sem mexer nos pesos do modelo. Depois de cada tentativa, o agente escreve em linguagem natural uma reflexão sobre o retorno que recebeu, guarda essa reflexão numa **memória episódica** e a usa como contexto nas tentativas seguintes. Os autores chamam isso de **reforço verbal**: o "gradiente" é um texto.

## As três peças

- **Ator:** o modelo que gera texto e ações (com cadeia de raciocínio ou ReAct), condicionado à memória de curto prazo (a trajetória da tentativa) e à de longo prazo (as reflexões guardadas).
- **Avaliador:** dá a nota da trajetória. Comparação exata com a resposta nos testes de raciocínio, heurísticas na tomada de decisão, testes unitários (escritos pelo próprio modelo) na programação.
- **Autorreflexão:** um modelo que transforma o retorno esparso (como "deu certo" ou "não deu") mais a trajetória em orientação verbal para a próxima tentativa.

## O laço e a memória

Gerar a trajetória → avaliar → refletir → acrescentar a reflexão à memória → repetir até o avaliador aprovar ou acabar o número de tentativas. A memória de longo prazo é **limitada**: em geral de uma a três experiências (três no ALFWorld e no HotPotQA, uma em programação), numa janela deslizante.

## Tipos de retorno

Sinal binário do ambiente; heurísticas (repetir a mesma ação e resposta por mais de três ciclos, passar de 30 ações); autoavaliação do modelo; até seis testes unitários gerados por problema, filtrados por árvore sintática válida.

## Resultados

- **ALFWorld** (134 tarefas): ReAct com Reflexion completa 130; ganho absoluto de 22% em 12 tentativas. O ReAct sozinho estaciona entre a sexta e a sétima tentativa.
- **HotPotQA** (100 perguntas): ganho de 20%.
- **HumanEval Python:** 91,0% de acerto na primeira tentativa, contra 80,1% do GPT-4. **Rust:** 68,0% contra 60,0%.
- **MBPP Python:** 77,1%, abaixo dos 80,1% do GPT-4 (o único em que perde). **MBPP Rust:** 75,4% contra 70,9%.
- **LeetcodeHardGym** (40 problemas posteriores ao corte do GPT-4): 15,0% contra 7,5%.

## Ablações

- Sem a autorreflexão (os 50 problemas mais difíceis do HumanEval em Rust): fica em 0,60, igual à linha de base; completo, 0,68.
- Sem gerar testes: cai para 0,52, abaixo da linha de base. O retorno ruim piora o resultado.
- No HotPotQA, a reflexão soma cerca de 8 pontos percentuais sobre só guardar a trajetória anterior: o que ajuda é a lição escrita, não o histórico bruto.
- O ganho depende de modelo forte: com um modelo menor (starchat-beta), linha de base e Reflexion empatam em 0,26.

## Limites declarados

- Otimizar em linguagem natural pode parar num mínimo local ruim.
- A memória é uma janela deslizante; os autores sugerem bancos vetoriais ou SQL como trabalho futuro.
- Testes gerados falham com funções não determinísticas, impuras, dependentes de hardware ou concorrentes; no MBPP Python, 16,3% de falsos positivos nos testes (1,4% no HumanEval).
- No WebShop não ganha do ReAct: a tarefa pede exploração, não lição.
- Depende da autoavaliação do modelo e não tem garantia formal de sucesso.

## Impacto

Reflexões em texto tornam o agente mais interpretável: dá para ler o que ele concluiu antes de ele usar uma ferramenta. Os autores recomendam rodar código gerado só em ambiente isolado.

## Nota de leitura (de outra fonte)

A revisão de Kamoi et al. ([[2026-10-28-kamoi-quando-llms-se-autocorrigem]]) classifica o experimento do HotPotQA como irrealista (o retorno é a comparação com o gabarito) e os de jogo e código como justos (o retorno vem do ambiente ou do interpretador).

---
