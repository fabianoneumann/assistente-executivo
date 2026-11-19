---
titulo: "Agentic Design Patterns Part 2, Reflection"
tipo: artigo
autor: "Andrew Ng"   # a página não traz o sobrenome: a carta assina "Andrew" e está na seção "Letters" do The Batch (trilha de navegação da página), que o menu do topo chama "Andrew's Letter" e o submenu do The Batch, "Andrew's Letters"; o metadado de autor da página (JSON-LD) traz "Analytics DeepLearning.AI"
url: "https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection"
publicado_em: 2024-03-27   # a página mostra "Published" e "Mar 27, 2024"; meta article:published_time e JSON-LD datePublished 2024-03-27T13:39:08-07:00, sem modificação posterior
capturado_em: 2026-11-13
areas: [agent-engineering]
entrada: pesquisa
tags: [andrew-ng, the-batch, agentic-workflows, agentic-design-patterns, reflection, self-critique, tool-use, multi-agent, code-generation, prompting]
licenca: "sem licença aberta na página; nota de fato em palavras próprias, com citações curtas exatas"
---

# The Batch, padrões agênticos, parte 2: reflexão

Nota de fato (`knowledge/sources/README.md`, item 2): carta curta que ensina um método (uma receita de prompts em etapas, com variações), por isso passos numerados e tabelas, e não ficha de prosa. Não há integral: a página é protegida.

**Proveniência.** Carta semanal do The Batch, da DeepLearning.AI, seção "Letters", assinada "Andrew", em https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection. HTML baixado em 2026-11-13, com o texto do bloco principal extraído para a cópia de trabalho e lido no texto bruto em 2026-11-13. A página marca o tempo de leitura em 2 minutos. Título conferido no HTML: o cabeçalho é "Agentic Design Patterns Part 2, Reflection", com vírgula, e o subtítulo diz que os modelos de linguagem viram agentes mais eficazes ao refletir sobre o próprio comportamento; no rodapé da parte 1, o link para esta carta escreve "Part 2: Reflection", com dois-pontos. Data conferida no HTML: "Published" e "Mar 27, 2024" e os metadados da linha do `publicado_em`. Cobertura: o texto inteiro da carta, de "Dear friends" à assinatura, os três links da lista de leitura (endereços conferidos no HTML, artigos não abertos) e os títulos dos links do rodapé para as partes 1, 3, 4 e 5 (não abertos). A imagem do topo (`AGENTS-REFLECTION-2.jpg`) não foi aberta; o `alt` dela repete título e subtítulo.

**Conferência lado a lado** (2026-11-13, pela régua do `README.md` desta pasta, item 2): contam as frases de prosa, os passos da lista e as células com texto corrido; a célula que só traz um fato (nome, autor, ano, link) fica fora, e as três citações literais estão à parte. Resultado: 5 de 17 unidades seguem uma frase da fonte (detalhe no fim da ficha); a maior sequência na ordem da fonte é de 4 unidades seguidas, os quatro passos do método, que a régua permite em lista porque a ordem é o método; fora da lista, nenhuma sequência. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: o script não mede tradução, e a conferência é esta conta), com 0 de 28 unidades coladas e nenhum trecho.

## Em uma frase

Segunda carta da série sobre padrões de agente: explica a reflexão, em que o modelo critica a própria saída e a refaz, com um roteiro de prompts para código, duas variações (com ferramentas de verificação e com dois agentes) e três artigos para ler.

## O método (o exemplo da carta é código)

1. Pedir ao modelo, direto, o código de uma tarefa.
2. Num segundo prompt, devolver o código gerado e pedir uma revisão crítica dele: correção, estilo, eficiência e o que mudar (o texto do prompt está em "Citações").
3. Num terceiro prompt, dar o código anterior junto da crítica e pedir a reescrita a partir dela.
4. Repetir a dupla crítica e reescrita, se compensar.

## Variações e alcance

| Variação | Quem faz a crítica | Sobre o quê |
|---|---|---|
| Autocrítica | o mesmo modelo, em outro prompt | a própria saída |
| Com ferramentas | o mesmo modelo | os erros que testes unitários ou uma busca na web apontaram |
| Dois agentes | um segundo agente, instruído só para criticar | a saída do primeiro, numa conversa entre os dois |

| Item | Fato |
|---|---|
| Origem da ideia | a crítica que o usuário já faz à mão num chat (ChatGPT, Claude, Gemini), agora automatizada |
| Onde a autocrítica serve | código, texto, respostas a perguntas |
| Facilidade, para o autor | rápida de implementar |
| Lugar entre os fluxos agênticos | um dos tipos mais básicos |
| Resultado relatado | ganhos de desempenho que surpreenderam o autor, em alguns casos das aplicações dele |
| Os quatro padrões, lembrados na abertura | reflexão, uso de ferramentas, planejamento, colaboração multiagente |

## Leituras recomendadas

| Artigo (título como a carta dá) | Autores e ano (como a carta dá) | Link no HTML |
|---|---|---|
| Self-Refine: Iterative Refinement with Self-Feedback | Madaan et al. (2023) | https://arxiv.org/abs/2303.17651 |
| Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. (2023) | https://arxiv.org/abs/2303.11366 |
| CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing | Gou et al. (2024) | https://arxiv.org/abs/2305.11738 |

Os três links do HTML levam parâmetros de rastreio de e-mail (`utm_*`, `_hsenc`), tirados acima.

## O que a fonte recomenda

Começar pela reflexão, que custa pouco a montar e, nas aplicações do autor, já mudou o resultado algumas vezes. Separar quem gera de quem critica em dois agentes é uma montagem que ele achou prática; sem ela, a autocrítica em prompts encadeados já serve, e onde houver como verificar (testes, busca) a crítica parte do que a ferramenta achou.

## Citações

- "Check the code carefully for correctness, style, and efficiency, and give constructive criticism for how to improve it." (o prompt de crítica do exemplo, no terceiro parágrafo)
- "What if you automate the step of delivering critical feedback, so the model automatically criticizes its own output and improves its response?" (o segundo parágrafo, logo antes de "This is the crux of Reflection.")
- "For a design pattern that’s relatively quick to implement, I've seen it lead to surprising performance gains." (o fim do primeiro parágrafo)

## Lacuna

- A carta não traz número nenhum: nem o tamanho dos ganhos, nem em quais aplicações, nem contra que linha de base.
- Não diz quantas voltas de crítica e reescrita fazer nem quando parar.
- Só dá prompt de exemplo para código; para texto e respostas a perguntas, não há roteiro.
- Não resume o que cada artigo recomendado mostra.

## Detalhe da conferência lado a lado

Total de 17 unidades: 1 frase em "Em uma frase", 4 passos do método, 1 frase da nota sobre os links, 2 em "O que a fonte recomenda", 4 na lacuna e 5 células com texto corrido (três na tabela das variações: os erros apontados, o segundo agente, a conversa entre os dois; e as de origem da ideia e resultado relatado). Seguem uma frase da fonte 5: os quatro passos do método (cada um condensa uma frase da carta, na ordem dela, e por isso formam a sequência de 4, permitida na lista de método porque a ordem é o método) e a célula da origem da ideia (condensa as duas frases do segundo parágrafo, na ordem). As células da tabela das variações respondem a perguntas que a carta não faz (quem critica, sobre o quê) e não traduzem frase; a do resultado relatado junta o fim do primeiro parágrafo com o penúltimo; as frases de "Em uma frase" e de "O que a fonte recomenda" juntam lugares distantes da carta, fora da ordem dela.
