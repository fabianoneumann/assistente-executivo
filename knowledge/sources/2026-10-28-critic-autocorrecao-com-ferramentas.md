---
titulo: "CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing"
tipo: paper
autor: "Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Nan Duan, Weizhu Chen"
url: "https://arxiv.org/abs/2305.11738"
publicado_em: 2023-05-19
capturado_em: 2026-10-28
licenca: "arXiv non-exclusive distribution 1.0 (sem licença aberta)"
areas: [agent-engineering]
tags: [critic, tool-interactive-critique, external-feedback, self-correction, verify-then-correct, stopping-criteria]
---

Ficha de estudo, em palavras próprias. Publicado no **ICLR 2024** (campo de comentários do arXiv). arXiv: v1 em 19/05/2023, v4 (lida) em 21/02/2024. Lido em 2026-10-28, na pesquisa.

## A ideia

Um modelo congelado, sem treino adicional, confere e corrige a própria saída **consultando ferramentas externas**, como uma pessoa que checa um fato num buscador ou depura código no interpretador. Cada ciclo tem três passos: gerar a resposta inicial; **verificar** com a ferramenta, produzindo uma crítica; **corrigir** com base na resposta original e na crítica. Para quando a crítica julga a resposta correta ou quando bate o número máximo de iterações.

## Ferramenta por tarefa

- **Perguntas abertas:** busca no Google; a primeira página é lida e até 400 caracteres entram no contexto. Até 7 interações e 3 correções; para antes se a resposta não muda em duas rodadas seguidas.
- **Matemática em forma de programa:** interpretador Python, com mensagens de erro e resultado da execução. Até 4 correções.
- **Toxicidade:** a Perspective API dá a nota geral e seis atributos; o atributo mais alto vira a crítica. Até 4 iterações; para quando a toxicidade cai abaixo de 10%.

## Resultados (ChatGPT)

| Tarefa | Linha de base | CRITIC | Com gabarito (limite superior) |
|---|---|---|---|
| HotpotQA, F1 | 42,8 | 52,9 | 56,9 |
| AmbigNQ, F1 | 64,3 | 74,9 | 79,9 |
| TabMWP, acerto | 75,0 | 89,0 | 94,0 |
| GSM8K, acerto | 72,5 | 78,2 | 83,9 |
| Toxicidade (menor é melhor) | 0,325 | 0,173 | — |

Em média, +7,7 de F1 nas perguntas, +7,0 pontos em matemática e 79,2% menos probabilidade de toxicidade. Ganha do ReAct e de gerar várias e escolher (*rejection sampling*) nas perguntas. Não é uniforme: com o text-davinci-003, o SVAMP caiu de 84,0 para 80,7.

## A ablação que importa: sem ferramenta

Tirando as ferramentas e deixando o modelo criticar a si mesmo, o ganho nas perguntas fica marginal; em matemática, o text-davinci-003 piora (68,3 contra 70,1 no GSM8K); em toxicidade, fica um pouco pior do que sem correção nenhuma (0,353 contra 0,344). Os autores concluem que a autoverificação sem retorno externo não é confiável, apontando a falta de confiabilidade de todos os modelos testados ao validar os próprios resultados.

## Outros achados

- A coluna "com gabarito" corrige só o que se sabe errado; é o teto, não o desempenho real.
- A maior parte do ganho vem nas **duas ou três primeiras correções**.
- A crítica com ferramenta ganha de simplesmente gerar várias respostas e escolher.

## Limites declarados

Latência cresce linearmente com as iterações; depende de prompts feitos à mão no estilo ReAct; só texto; generalidade para outras tarefas e modelos incerta.
