---
titulo: "Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory"
tipo: paper
autor: "Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan Jurafsky, James Zou"
url: "https://arxiv.org/abs/2504.07952"
publicado_em: 2025-04-10
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [agent-memory, test-time-learning, memory-curation, lessons-learned, retrieval, tool-use]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 (única) em 10/04/2025. A página do arXiv não diz o venue; o artigo 2610.22984 o cita como publicado nos anais do EACL 2026 (19ª conferência do capítulo europeu da ACL, volume 1, p. 7080 a 7106). Código e dados: github.com/suzgunmirac/dynamic-cheatsheet. Lido em 2026-10-29, na pesquisa (lições das skills).

## A pergunta

Um modelo de linguagem usado como caixa preta, sem mexer nos pesos, consegue melhorar ao longo de uma sequência de perguntas guardando o que aprendeu numa memória externa que ele mesmo mantém? Os autores chamam essa memória de "cola" (cheatsheet): uma biblioteca compacta de estratégias, esboços de solução e trechos de código, que o modelo consulta antes de responder e reescreve depois. Não há rótulo de resposta certa nem retorno humano: o próprio modelo julga o que vale guardar.

## O que a cola guarda

- **Conteúdo:** estratégias de solução, heurísticas gerais, trechos de código reutilizáveis (Python), técnicas de otimização e casos de borda, e conhecimento específico (fórmulas, teoremas). No MMLU-Pro, o Claude guardou "guias de referência" compactos de princípios de engenharia e física (seção 4.2).
- **Formato** (prompt do curador, figuras 14 e 15 do apêndice B.4.3): a cola tem número de versão e seções fixas ("trechos de código e estratégias de solução", "heurísticas gerais", "otimização e casos de borda", "conhecimento especializado e teoremas"). Cada item tem uma descrição (o contexto do problema e o essencial da solução, com a referência às questões de onde veio, como "Q14, Q22"), um exemplo (código comentado, solução trabalhada ou estratégia) e um **contador de uso**. Teto de cerca de 2.000 a 2.500 palavras.
- **Exemplos reais** (figuras 5 e 6): no Game of 24, depois de 100 questões, o GPT-4o tinha um item "estratégia do solucionador do 24" com passos, um exemplo resolvido, dicas e o código Python de força bruta, com contador 99. No AIME 2024, depois de 20 questões, o Claude 3.5 Sonnet tinha itens de meta-raciocínio como um "roteiro de análise sistemática de problemas" (referência Q1 a Q20, contador 20) e uma "estratégia de verificação de solução" (Q5 a Q20).

## Como a cola é curada

O sistema tem dois papéis, o **gerador** (responde usando a cola) e o **curador** (atualiza a cola). Nos experimentos, os dois são o mesmo modelo com prompts diferentes (seção 2.1).

- **O que o curador pesa** (seção 2.1.2): (i) se a resposta nova é útil e generalizável; se for, destila numa forma de consulta; (ii) se algum item existente estava errado ou foi superado por estratégia mais eficiente ou versátil, e então remove ou atualiza; (iii) clareza e compactação da cola inteira, consolidando os itens em referências curtas e de alto impacto.
- **Sem gabarito:** o curador não vê a resposta certa e precisa avaliar sozinho se a solução está correta e eficiente antes de mudar a memória. Os autores dizem que, na prática, esse passo poderia ser uma série de verificações com várias ferramentas e modelos; nos experimentos foi um único modelo.
- **O que entra, pelo prompt do curador:** só estratégias, código, intuições e padrões de alto valor; o que contribui de forma significativa para resolver problemas; meta-estratégias novas tiradas da experiência recente.
- **O que sai:** detalhe redundante, trivial ou muito específico de um problema, que não generaliza; entradas duplicadas. Se aparece abordagem melhor que uma já registrada, "replace the old version" (substitua a versão antiga).
- **Como se reescreve:** a cola inteira é regenerada a cada atualização. O prompt avisa que o que não for copiado explicitamente para a cola nova "will be lost and cannot be retrieved" (se perde e não volta), e pede equilíbrio para que técnicas antigas e eficazes não se percam ao entrar as novas. O contador de uso serve para priorizar o que é mais usado.
- **Falha observada na reescrita** (seção 5): o modelo às vezes, em vez de reescrever, abrevia a memória com algo como "conteúdo anterior [...] preservado", e essa atualização truncada degrada a qualidade da cola com o tempo. A sugestão dos autores é uma base estruturada externa que o modelo consulte sem ter de regenerar grandes blocos de texto.

## As variantes e as linhas de base

- **DC-Cu (cumulativa):** responde com a memória atual e só depois atualiza a memória. Não tem recuperação de exemplos antigos.
- **DC-RS (recuperação e síntese):** antes de responder, recupera as 3 perguntas passadas mais parecidas com a atual (com as respostas que o próprio modelo deu), por semelhança de cosseno de embeddings do text-embedding-3-small da OpenAI; o curador atualiza a cola com esses exemplos e só então o gerador responde. Testaram k de 5 e 7, sem ganho que valesse (notas 1 e 2).
- **BL:** prompt mínimo, sem memória, sem instrução de código.
- **DC-∅:** o mesmo prompt estruturado do gerador (que incentiva escrever e executar Python), com a cola vazia. Isola o efeito da memória do efeito do prompt; os autores a tratam como linha de base forte.
- **FH (histórico completo):** cola todo o histórico de perguntas e respostas no prompt, sem curadoria. Testado só no AIME 2024 e 2025 (30 questões cada).
- **DR (recuperação dinâmica):** recupera as interações passadas mais parecidas e cola literalmente, sem curadoria nem abstração.
- Modelos: GPT-4o, Claude 3.5 Sonnet, GPT-4o-mini, Claude 3.5 Haiku; DeepSeek R1 e o1 em experimentos adicionais. Tarefas: AIME 2024 (30), AIME 2025 (30), AIME 2020 a 2024 (133), GPQA-Diamond (198), Game of 24 (100), Math Equation Balancer (250, montado pelos autores), MMLU-Pro Engenharia e Física (250 de cada). Métrica de acerto flexível ao formato. O texto não informa número de execuções nem variância.

## Resultados, cada número com a condição

Tabela 1 (Claude 3.5 Sonnet e GPT-4o), em % de acerto:

| Tarefa | Sonnet BL | Sonnet DC-∅ | Sonnet DR | Sonnet DC-Cu | Sonnet DC-RS | GPT-4o BL | GPT-4o DC-∅ | GPT-4o DR | GPT-4o DC-Cu | GPT-4o DC-RS |
|---|---|---|---|---|---|---|---|---|---|---|
| AIME 2024 | 23,3 | 36,7 | 43,3 | 50,0 | 46,7 | 20,0 | 36,7 | 26,7 | 36,7 | 40,0 |
| AIME 2025 | 6,7 | 23,3 | 23,3 | 36,7 | 30,0 | 6,7 | 10,0 | 10,0 | 16,7 | 20,0 |
| AIME 2020-24 | 6,7 | 30,1 | 39,1 | 38,4 | 40,6 | 9,8 | 24,1 | 24,1 | 20,3 | 24,8 |
| Game of 24 | 12,0 | 10,0 | 11,0 | 14,0 | 14,0 | 10,0 | 19,0 | 6,0 | 93,0 | 99,0 |
| GPQA-Diamond | 59,6 | 60,1 | 63,6 | 61,1 | 68,7 | 57,1 | 57,1 | 55,1 | 58,1 | 57,1 |
| Equation Balancer | 44,8 | 56,4 | 60,4 | 100 | 97,8 | 50,0 | 88,0 | 100 | 100 | 99,2 |
| MMLU-Pro Eng. | 61,2 | 57,2 | 65,2 | 66,8 | 67,6 | 53,2 | 51,6 | 48,8 | 44,0 | 51,2 |
| MMLU-Pro Física | 74,0 | 75,6 | 80,4 | 77,6 | 82,0 | 75,6 | 70,8 | 75,6 | 70,4 | 75,2 |

- **Game of 24, GPT-4o de 10% a 99% (DC-RS; 93% em DC-Cu).** A condição: no começo da sequência o modelo descobriu um resolvedor de força bruta em Python, percebeu que os problemas tinham a mesma estrutura, guardou o código e passou a recuperar e aplicar quase o mesmo programa nas questões seguintes (seção 4.1). O prompt sozinho (DC-∅) dá 19%; recuperar exemplos sem curadoria (DR) dá 6%. Os autores atribuem o salto ao uso da memória. **O Claude 3.5 Sonnet, na mesma tarefa, foi só de 12% a 14%**: não internalizou o método geral e continuou fazendo aritmética à mão.
- **Equation Balancer, de 45% a 50% para 98% a 100%**, pelo mesmo mecanismo (rotina de código guardada e reaproveitada). Condição que a tabela mostra: no GPT-4o o prompt com incentivo a código já leva a 88% (DC-∅) e a recuperação sem curadoria (DR) já chega a 100%.
- **AIME:** Sonnet de 23,3% a 50,0% no AIME 2024 e de 6,7% a 36,7% no AIME 2025 (DC-Cu), e de 6,7% a 40,6% no AIME 2020 a 2024 (DC-RS). Parte do ganho já vem do prompt: DC-∅ dá 36,7%, 23,3% e 30,1%. GPT-4o de 20,0% a 40,0% (2024) e de 6,7% a 20,0% (2025) com DC-RS.
- **GPQA-Diamond, "9%" do resumo:** é o Claude 3.5 Sonnet, de 59,6% a 68,7% com DC-RS, 9,1 pontos. A recuperação sozinha (DR) já dá 63,6%; a curadoria acrescenta o resto. **No GPT-4o não houve ganho:** a tabela dá 57,1% em BL e em DC-RS, 58,1% em DC-Cu e 55,1% em DR (abaixo da base). O texto da seção 4.2 diz "de 57,1% a 58,1% com DC-RS", o que não bate com a tabela (58,1 é o DC-Cu). Os autores dizem que a recuperação às vezes confunde o modelo quando traz exemplos ruins, e na seção 5 que o desempenho do GPT-4o "ocasionalmente caiu" no GPQA-Diamond por escolhas ruins da recuperação.
- **MMLU-Pro, "8%" do resumo:** é o Claude, em Física de 74% a 82% (DC-RS); em Engenharia, de 61,2% a 67,6%. **O GPT-4o piorou nas duas:** Engenharia de 53,2% para 44,0% (DC-Cu) e 51,2% (DC-RS); Física de 75,6% para 70,4% (DC-Cu). Leitura dos autores: lacunas de conhecimento de base e complexidade do domínio atenuam o benefício quando a memória curada é menos confiável.
- **Curadoria contra histórico completo** (tabela 2, AIME): Sonnet com FH fica em 26,7% (2024) e 6,7% (2025), contra 50,0% e 36,7% com DC-Cu. GPT-4o com FH cai abaixo da própria base: de 20,0% para 13,3% (2024) e de 6,7% para 3,3% (2025), contra 40,0% e 20,0% com DC-RS. Pares de pergunta e resposta sem curadoria enchem o contexto, diluem o que importa e encarecem a inferência.
- **Votação por maioria não ajuda** (tabela 4): 3 gerações e a resposta mais comum dão 23,3% no AIME 2024 e 6,7% no 2025, igual à base; com o prompt estruturado, 33,3% contra 36,7% sem votação. DC-Cu chega a 50,0% e 36,7%.
- **Modelos menores** (tabela 3): Claude 3.5 Haiku vai de 10,0% a 36,7% no AIME 2024 (DC-Cu; o prompt sozinho dá 26,7%), fica em 13,3% no 2025 e vai de 43,4% a 49,0% no GPQA-Diamond (DC-RS). **O GPT-4o-mini piora com memória:** AIME 2024 de 16,7% para 13,3% (DC-Cu e DC-RS, enquanto DC-∅ dá 20,0%); GPQA-Diamond de 34,3% para 33,8% (DC-Cu) e 32,3% (DC-RS). DeepSeek R1 e o1 tiveram ganho mínimo ou inconsistente, com soluções longas e prolixas demais.
- **Custo em tokens** (nota 13): no AIME 2024, o Sonnet usou em média 370 tokens por resposta na base, 494 com DC-∅, 1.035 com DC-RS e 1.831 com DC-Cu. O texto afirma que a manutenção da memória vira ganho líquido com o tempo, porque evita redescobrir a mesma solução, mas reconhece que o custo inicial de descobrir e curar uma abordagem não é trivial.
- **Estabilidade da memória** (figura 11, Game of 24, GPT-4o): medida pela semelhança entre estados consecutivos da cola, as duas variantes se estabilizam depois das primeiras iterações; DC-Cu oscila um pouco mais na segunda metade.

## Por que funciona e quando não funciona, segundo os autores

- **O modelo precisa acertar o bastante para alimentar a memória.** Modelos menores geram poucas soluções corretas, a cola se enche de tentativas erradas ou parciais e o refinamento empaca. Também têm dificuldade com contexto longo e com recuperação: não acham a solução passada relevante ou a aplicam mal. "DC can amplify the strengths of models that can already produce high-quality outputs, but not fix foundational gaps in reasoning" (seção 1).
- **Funciona melhor quando as questões têm estrutura parecida.** No Game of 24 e no Equation Balancer, uma vez achada a solução eficiente, ela se reaplica; no AIME, uma estratégia de geometria ou combinatória transfere para questões análogas. A ordem importa: apresentar cedo os problemas típicos pode acelerar o aprendizado, como num currículo (seção 4.6).
- **Erros e acertos se agrupam** no espaço de embeddings (figura 10, GPQA-Diamond). Uma boa heurística ajuda os vizinhos, mas uma heurística errada que entra na memória se espalha do mesmo jeito; manter a memória "limpa" exige curadoria cuidadosa e, se preciso, poda.
- **Transferir a cola de um modelo grande para um pequeno** deu resultado misto: a memória ajuda, mas não compensa capacidade de base insuficiente.
- **Recuperação ruim atrapalha:** com perguntas muito diversas ou pouco relacionadas, a recuperação mal filtrada introduz confusão (o caso do GPT-4o no GPQA-Diamond). Pedem recuperação mais robusta.
- **Uso de ferramenta:** sob DC, os modelos passam a reconhecer quando código é mais confiável que cálculo verbal e a guardar e refinar o programa. Só testaram o interpretador Python.

## O que propõem

Memória externa curada, sem treino, como alternativa a ajuste fino e a recuperação estática; e, como direções: memórias separadas por domínio ou hierárquicas (combinatória, física), cada uma com seu curador, para reduzir a carga e isolar erros; ordenação adaptativa dos exemplos; recuperação mais sofisticada; e um curador em vários passos, com ferramentas e modelos que verifiquem a solução antes de guardá-la.

## Limites declarados

- Ganho depende do tamanho e da capacidade do modelo; modelos pequenos e os de raciocínio (R1, o1) quase não ganham.
- A estrutura é sequencial: atrapalha tarefas em paralelo ou em lote, que precisam de inferência independente.
- Reescrever a memória inteira a cada passo pede geração longa e precisa, e o modelo às vezes trunca.
- Recuperação mal filtrada pode piorar o resultado.
- O efeito depende da semelhança entre as tarefas e da ordem em que chegam.
