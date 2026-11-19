---
titulo: "Agentic AI (curso da DeepLearning.AI)"
tipo: artigo
autor: "DeepLearning.AI (página do curso; instrutor: Andrew Ng)"
url: "https://www.deeplearning.ai/courses/agentic-ai/"
publicado_em: 2025-09-30   # a página visível não traz data de lançamento, só "Updated Oct 30, 2026"; 2025-09-30 é o datePublished do JSON-LD e o releasedAt (2025-09-30T08:00:00Z) dos dados embutidos no HTML; lastEditAt 2026-10-30T00:49:36Z
capturado_em: 2026-11-13
areas: [agent-engineering]
entrada: pesquisa
tags: [andrew-ng, deeplearning-ai, online-course, agentic-workflows, agentic-design-patterns, reflection, tool-use, planning, multi-agent, evals, error-analysis, mcp]
licenca: "sem licença aberta na página; nota de fato em palavras próprias, com citações curtas exatas"
---

# DeepLearning.AI, curso Agentic AI: formato, preço e programa

Nota de fato (`knowledge/sources/README.md`, item 2): página de produto que lista fatos (duração, aulas, preço, programa), por isso tabelas que seguem a ordem do programa, com a prosa só para dizer o que a página é, o que recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Página do curso no site da DeepLearning.AI, https://www.deeplearning.ai/courses/agentic-ai/. HTML baixado em 2026-11-13, com o texto do bloco principal extraído para a cópia de trabalho e lido no texto bruto em 2026-11-13. Datas: a página mostra "Updated Oct 30, 2026" e não diz quando o curso foi lançado; nos dados embutidos no HTML, o curso tem `releasedAt` 2025-09-30T08:00:00+00:00 e `lastEditAt` 2026-10-30T00:49:36+00:00, o JSON-LD do curso tem `datePublished` 2025-09-30, e o vídeo de apresentação tem `uploadDate` no mesmo dia. Cobertura: o texto inteiro da página, do cabeçalho do curso ao rodapé, inclusive o programa completo e as perguntas frequentes; as avaliações de alunos que a página mostra são de outros cursos da DeepLearning.AI ("Learner reviews from other DeepLearning.AI courses") e ficaram fora. Os links (página de planos, fórum, vídeo de apresentação) não foram abertos.

**Conferência lado a lado** (2026-11-13, pela régua do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (número, nome, título de aula, preço, rótulo curto) fica fora, e as três citações literais estão à parte. Os títulos das aulas ficam em inglês, como na página, porque são nomes. Resultado: 5 de 16 unidades seguem uma frase da fonte, numa contagem conservadora (detalhe no fim da ficha); a maior sequência na ordem da fonte é de 3, em células da ficha técnica e da tabela grátis e pago (a página de produto que lista fatos pode seguir a ordem da fonte, pelo item 2 do `README.md`, e a conta fica declarada). O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: o script não mede tradução, e a conferência é esta conta), com 2 de 31 unidades coladas e nenhum trecho: as duas são células com títulos de aula longos ("Optional: Set up your local environment..." e "Ungraded Lab: Adding a component-level eval..."), que são nomes e ficam em inglês de propósito.

## Em uma frase

Curso de nível intermediário da DeepLearning.AI, dado pelo Andrew Ng, que ensina a montar fluxos agênticos em Python pelos quatro padrões (reflexão, ferramentas, planejamento, multiagente) e dedica um módulo inteiro a avaliação e análise de erro; os vídeos são grátis para quem audita, e exercícios avaliados e certificado ficam no plano PRO.

## Ficha técnica

| Item | Valor |
|---|---|
| Instrutor | Andrew Ng ("Founder, DeepLearning.AI; Co-founder, Coursera") |
| Nível | Intermediate |
| Duração total (cabeçalho) | 9h55m |
| Vídeos | 31 |
| Exemplos de código (cabeçalho) | 7 |
| Exercícios avaliados | 8 (5 questionários e 3 exercícios de código) |
| Ritmo | no tempo do aluno |
| Atualização | 30/10/2026 |
| Lançamento | não aparece na página visível; 30/09/2025 nos metadados do HTML |
| Línguas nos metadados (JSON-LD) | en, jp, kr |
| Linguagem dos exercícios | Python |
| Construção dos padrões | do zero, antes de qualquer framework |
| Público | desenvolvedores que querem sistemas autônomos de várias etapas; quem tem Python intermediário; quem já conhece o básico de LLMs e APIs |

## Grátis e pago

| Recurso | Auditar (grátis) | PRO |
|---|---|---|
| Vídeos | sim | sim |
| Fórum da comunidade | sim | sim |
| Questionários e laboratórios interativos | não | sim |
| Certificado | não | sim, ao concluir as avaliações exigidas |
| Ferramentas de projeto e projetos práticos | não | sim |
| Salvar o progresso | não informado | sim |
| Trilhas do certificado profissional | não informado | sim |
| Preço | grátis | US$ 25 por mês na cobrança anual; US$ 30 por mês na mensal |
| Pagamento | — | Stripe, em dólar, com imposto conforme o local |

## Programa

| Módulo | Aula (título na página) | Tipo | Duração |
|---|---|---|---|
| 1, Introduction to Agentic Workflows | Welcome! | vídeo | 1 min |
| 1 | What is agentic AI? | vídeo | 5 min |
| 1 | Degrees of autonomy | vídeo | 5 min |
| 1 | Benefits of agentic AI | vídeo | 4 min |
| 1 | Agentic AI applications | vídeo | 7 min |
| 1 | Task decomposition: Identifying the steps in a workflow | vídeo | 8 min |
| 1 | Evaluating agentic AI (evals) | vídeo | 5 min |
| 1 | Agentic design patterns | vídeo | 7 min |
| 1 | Optional: Set up your local environment for the ungraded labs | leitura | 10 min |
| 1 | Module 1 quiz | questionário avaliado | 10 min |
| 1 | Try the research agent | exemplo de código | 1 h |
| 1 | convite para o fórum da DeepLearning.AI | leitura | 1 min |
| 2, Reflection Design Pattern | Reflection to improve outputs of a task | vídeo | 3 min |
| 2 | Why not just direct generation? | vídeo | 5 min |
| 2 | Chart generation workflow | vídeo | 3 min |
| 2 | Ungraded Lab: Chart Generation | exemplo de código | 15 min |
| 2 | Evaluating the impact of reflection | vídeo | 8 min |
| 2 | Using external feedback | vídeo | 4 min |
| 2 | Ungraded Lab: Improving SQL Generation with Reflection | exemplo de código | 15 min |
| 2 | Module 2 quiz | questionário avaliado | 10 min |
| 2 | M2 Graded Lab | exercício de código avaliado | 1 h |
| 3, Tool use | What are tools? | vídeo | 6 min |
| 3 | Creating a tool | vídeo | 5 min |
| 3 | Tool syntax | vídeo | 5 min |
| 3 | Ungraded Lab: Turning functions into tools | exemplo de código | 15 min |
| 3 | Ungraded Lab: Email Assistant Workflow | exemplo de código | 15 min |
| 3 | Code execution | vídeo | 5 min |
| 3 | MCP | vídeo | 5 min |
| 3 | Module 3 quiz | questionário avaliado | 10 min |
| 3 | M3 Graded Lab | exercício de código avaliado | 1 h |
| 4, Practical Tips for Building Agentic AI | Evaluations (evals) | vídeo | 15 min |
| 4 | Error analysis and prioritizing next steps | vídeo | 9 min |
| 4 | More error analysis examples | vídeo | 5 min |
| 4 | Component-level evaluations | vídeo | 3 min |
| 4 | Ungraded Lab: Adding a component-level eval to the research workflow | exemplo de código | 15 min |
| 4 | How to address problems you identify | vídeo | 9 min |
| 4 | Latency, cost optimization | vídeo | 4 min |
| 4 | Development process summary | vídeo | 3 min |
| 4 | Module 4 quiz | questionário avaliado | 10 min |
| 5, Patterns for Highly Autonomous Agents | Planning workflows | vídeo | 7 min |
| 5 | Creating and executing LLM plans | vídeo | 2 min |
| 5 | Planning with code execution | vídeo | 7 min |
| 5 | Ungraded Lab: Customer Service Agent | exemplo de código | 15 min |
| 5 | Multi-agentic workflows | vídeo | 9 min |
| 5 | Ungraded Lab: Market Research Team | exemplo de código | 15 min |
| 5 | Communication patterns for multi-agent systems | vídeo | 4 min |
| 5 | Module 5 quiz | questionário avaliado | 10 min |
| 5 | M5 Graded Assignment - Agentic Workflows | exercício de código avaliado | 1 h |
| fecho (sem módulo) | Conclusion | vídeo | 2 min |
| fecho (sem módulo) | Acknowledgments | leitura | 5 min |

| Contagem a partir do programa | Valor |
|---|---|
| Aulas de vídeo | 31, 2h50 no total |
| Itens marcados como exemplo de código | 8, 2h45 no total |
| Questionários avaliados | 5, 50 min |
| Exercícios de código avaliados | 3, 3 h |
| Leituras | 3, 16 min |
| Soma das durações listadas | 9h41 |
| Aulas que tratam de avaliação | 6 vídeos (evals no módulo 1; impacto da reflexão no módulo 2; evals, duas de análise de erro e avaliação por componente no módulo 4) e 1 exemplo de código (avaliação por componente no fluxo de pesquisa) |

## O que a fonte recomenda

A página vende o curso a quem já programa em Python e quer passar de respostas isoladas a processos de várias etapas, aprendendo a quebrar um processo de negócio em fluxo agêntico. Avaliação aparece desde o primeiro módulo, com testes, análise sistemática de erros e ajustes para produção espalhados pelo curso, e o módulo 4 reúne evals, análise de erro, latência e custo como dicas práticas de construção.

## Citações

- "building each pattern from first principles before exploring frameworks" (o texto de apresentação, "Why Enroll?")
- "Professionals with intermediate-level Python programming skills to be able to follow along with the implementations." (a lista "Who this course is for")
- "but you won’t have access to assessments, certificates, or project tools." (a pergunta frequente sobre o PRO, na frase sobre auditar grátis)

## Lacuna

- A página visível não diz quando o curso foi lançado; a data de 30/09/2025 só está nos metadados do HTML.
- O cabeçalho diz 7 exemplos de código, e o programa lista 8 itens com esse rótulo; a soma das durações do programa dá 9h41, e o cabeçalho diz 9h55m. A página não explica nenhuma das duas diferenças.
- O JSON-LD do curso registra carga de trabalho de uma hora (`PT1H`) e oferta na categoria "Free", sem relação com as 9h55m nem com o PRO da página visível.
- O texto de apresentação diz que o aluno ganha certificado ao concluir, sem a condição do PRO, que só aparece nas perguntas frequentes.
- Não diz que frameworks o curso usa depois de construir os padrões do zero, nem quais modelos ou APIs os exercícios chamam.

## Detalhe da conferência lado a lado

Total de 16 unidades: 1 frase em "Em uma frase", 2 em "O que a fonte recomenda", 5 na lacuna e 8 células com texto corrido (na ficha técnica, ritmo, lançamento, construção dos padrões e público; na tabela grátis e pago, a condição do certificado no PRO e a do pagamento; na contagem, a das aulas de avaliação; e a do preço, que tem valores mas também texto). Contagem conservadora: entra como "segue" toda unidade que traduz o miolo de uma frase da página, mesmo junto de outra coisa. Seguem 5: a célula da construção dos padrões (o miolo da frase citada em "Citações"), a do público (funde as três linhas de "Who this course is for", na ordem), a da condição do certificado (segue a resposta da pergunta sobre certificado), a do pagamento (funde os três itens de "Important details", na ordem) e a segunda frase de "O que a fonte recomenda" (traduz a frase sobre avaliação espalhada pelo curso e a junta com o módulo 4 do programa). A célula do preço só repete os dois valores e conta como não seguindo. A maior sequência na ordem da página é de 3: construção dos padrões, público e condição do certificado, seguidas na ficha e na página (as células de fato entre elas ficam fora da conta); o pagamento volta para antes do certificado na página e quebra a sequência. A primeira frase de "O que a fonte recomenda" e a de "Em uma frase" juntam o cabeçalho, a apresentação, o programa e as perguntas frequentes, fora da ordem; as da lacuna são da leitura, e não da página.
