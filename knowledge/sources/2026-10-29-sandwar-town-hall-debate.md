---
titulo: "Town Hall Debate Prompting: Enhancing Logical Reasoning in LLMs through Multi-Persona Interaction"
tipo: paper
autor: "Vivaan Sandwar, Bhav Jain, Rishan Thangaraj, Ishaan Garg, Michael Lam, Kevin Zhu"
url: "https://arxiv.org/abs/2502.15725"
publicado_em: 2025-01-28
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [multi-agent-debate, persona-prompting, single-agent, majority-vote, reasoning, prompt-engineering]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: versão única (v1), submetida em 28/01/2025. Comentário do arXiv: "Accepted to SoCal NLP Symposium 2024". Paper curto (cerca de 3 mil palavras), autores com e-mails pessoais e sem afiliação declarada. Lido em 2026-10-29.

## A pergunta

Um único modelo, instruído a se dividir em vários personagens que debatem em rodadas e votam, raciocina melhor em quebra-cabeças lógicos do que com cadeia de raciocínio (CoT)? E qual o número de personagens que rende mais? O método se chama THDP (town hall-style debate prompting) e se declara inspirado no Solo Performance Prompting de Wang et al. (`2026-10-29-wang-solo-performance-prompting.md`), com a diferença de pedir pensamento divergente e debate com votação.

## Como funciona

- **Uma chamada só, um modelo só.** Tudo acontece dentro de um prompt único e de uma resposta: o modelo gera os personagens, simula o debate e a votação e devolve o resultado num JSON. O artigo não usa a expressão "uma chamada", mas descreve um prompt único, fala em "single-model THDP", em dispensar "um número correspondente de instâncias de agentes separados", e lista como limite o corte da resposta quando o teto de tokens é baixo.
- **Passo 1, identificar personagens:** o modelo escolhe sozinho N personagens adequados à tarefa (em geral "especialistas", como de matemática, lógica ou probabilidade). O N é um parâmetro fixado na hora da execução pelo usuário.
- **Passo 2, debate em 3 rodadas:** cada personagem expõe sua solução e é encorajado a refutar problemas que note nas dos outros. O prompt de grade pede que cada entidade mostre o raciocínio passo a passo, faça réplicas e contra-argumentos, mantenha coerência com o ponto de vista e a especialidade que assumiu, e ajuste a posição diante de informação nova.
- **Passo 3, votação:** cada personagem vota na resposta que melhor representa a solução final, justificando; vence a maioria.
- **Estrutura do prompt (apêndice A):** princípio de sistema ("identifique as n entidades, faça 3 rodadas de debate estilo town hall, votem na resposta final; cada entidade deve criticar e rebater quando necessário"), 1 ou 2 exemplos escritos à mão (um fácil e um difícil, conforme o subconjunto) e um prefixo que lembra o número de entidades e o formato de saída. Nos exemplos, os personagens têm nome e especialidade de uma linha: "Logical Laura (especialista em raciocínio dedutivo)", "Systematic Sam", "Intuitive Ivy" no de múltipla escolha; Logical Deduction Expert, Data Organizer, Pattern Recognition Specialist, Constraint Satisfaction Solver, Sequence Analyst e Hypothesis Tester no de grade. Nos exemplos, as rodadas finais são de confirmação unânime e a votação é unânime.

## Como mediram

- **Tarefa:** ZebraLogic Bench, quebra-cabeças de casas e atributos a partir de pistas; a dificuldade cresce com o tamanho da grade. Dois subconjuntos: múltipla escolha (MCQ, escolher a letra certa) e grade (preencher a grade inteira, bem mais difícil). Por orçamento, as 200 primeiras linhas de cada subconjunto.
- **Métricas:** no MCQ, acertos, erros e "em branco" (saída que não deu para interpretar). Na grade, acurácia de quebra-cabeça inteiro (Puzzle, também chamada Total), separada em fáceis (Easy) e difíceis (Hard), acurácia por célula (Cell, células certas sobre o total) e taxa em branco (Blank).
- **Modelos:** GPT-4o, GPT-4o-mini (para ver o efeito num modelo menor) e Claude 3.5 Sonnet. OpenAI com decodificação gulosa; Claude com temperatura 0,5, escolhida por funcionar melhor em teste.
- **Controle:** CoT com um exemplo (o prompt padrão do ZebraLogic, que já traz um exemplo de CoT).
- **Número de personagens:** mais de 30 avaliações com 2 a 15 personagens; os testes finais usaram 4, 5 e 6 na grade e 7 no MCQ. Não há repetição com sementes nem barra de erro.

## Resultados

**Grade, 5 personagens contra CoT** (Tabela 1, THDP / CoT):

| Modelo | Easy | Hard | Cell | Blank | Puzzle (Total) |
|---|---|---|---|---|---|
| GPT-4o-mini | 54,5 / 78,0 | 2,6 / 1,9 | 42,0 / 41,7 | 0,0 / 0,5 | 14 / 18,5 |
| GPT-4o | 68,2 / 75,0 | 10 / 8,2 | 49,0 / 36,0 | 0,8 / 22,3 | 24 / 22,3 |
| Claude 3.5 Sonnet | 86,4 / 84,1 | 15,4 / 10,9 | 54,8 / 53,1 | 0,3 / 0,5 | 37,0 / 28,9 |

**Por número de personagens, na grade** (Figuras 2, 5 e 6; valores rotulados nos gráficos; 4 / 5 / 6 personagens / controle CoT):

| Modelo e métrica | 4 | 5 | 6 | CoT |
|---|---|---|---|---|
| Claude, Puzzle | 30,8 | 37,0 | 31,0 | 28,9 |
| Claude, Hard | 10,9 | 15,4 | 14,1 | 10,9 |
| Claude, Easy | 81,8 | 86,4 | 82,8 | 84,1 |
| Claude, Cell | 54,3 | 54,8 | 51,9 | 53,1 |
| GPT-4o, Puzzle | 23,5 | 24 | 19 | 22,25 |
| GPT-4o, Cell | 47,8 | 49,0 | 48,2 | 36,0 |
| GPT-4o, Blank | 0 | 0,75 | 0,5 | 22,25 |
| GPT-4o, Easy | 70,5 | 68,2 | 64,1 | 75 |
| GPT-4o-mini, Puzzle | 14,5 | 14 | 14 | 18,5 |
| GPT-4o-mini, Easy | 54,6 | 54,6 | 54,6 | 78 |
| GPT-4o-mini, Hard | 3,2 | 2,6 | 2,6 | 1,9 |

- O melhor número na grade foi 5 personagens; 6 piora em quase tudo para Claude e GPT-4o.
- **Claude** com 5: difíceis de 10% para 15% (1,5 vez), quebra-cabeça inteiro de 29% para 37% (8 pontos; o resumo diz 9%). Com 4: fáceis um pouco piores que o controle, célula e quebra-cabeça 1,3 a 2 pontos melhores.
- **GPT-4o:** o maior ganho é na célula (de 36% para 49%, os "13%" do resumo). No controle, 22,25% das respostas saíram em branco; com THDP, praticamente nenhuma. Os fáceis pioram (75% para 68% com 5, 64% com 6) e o quebra-cabeça inteiro sobe pouco (22,25% para 24%).
- **GPT-4o-mini piora:** fáceis caem 23 pontos (78% para 54,5%) em todos os números de personagens e o quebra-cabeça inteiro cai de 18,5% para 14%; só os difíceis sobem, sobre base muito baixa (1,9% para 2,6% a 3,2%).

**Múltipla escolha, 7 personagens** (Figura 3, acertos THDP / CoT): GPT-4o-mini 64,5 / 61 (+3,5); GPT-4o 70 / 66 (+4), com o branco caindo de 8% para 0; Claude 3.5 Sonnet 88 / 80 (+8), branco de 2% para 0.

## O que concluem

- O THDP funciona como amplificador da capacidade do modelo: nos fortes (Claude 3.5 Sonnet, GPT-4o), o debate interno usa o pensamento divergente para resolver casos mais difíceis; no fraco (GPT-4o-mini), o debate se desvia em tangentes e fica preso em ciclos repetitivos de raciocínio errado, com pouca correção de erro.
- Ao juntar vários pontos de vista, surgem contra-argumentos e soluções em vários passos que, na leitura dos autores, levam à melhor solução na rodada final.

## Limites declarados

- Mesmo com personagens adequados, a resposta não é garantidamente correta.
- Não se sabe se algum tipo de personagem rende mais: por exemplo, se um especialista de domínio raciocina melhor que um papel como "advogado do diabo". Pedem experimentos para medir o efeito de ter ou não um certo personagem.
- Gasta mais tokens: mais custo, mais tempo de resposta, e risco de a resposta ser cortada em modelos com teto de saída baixo.

Não declarados, mas visíveis no texto: avaliação de uma corrida só, sem variância; 200 itens por subconjunto; o texto troca numerações de figura (cita Figura 3 para resultados que estão na Figura 6 e "seção 3" para resultados da seção 5) e tem pequenas diferenças de arredondamento entre resumo, texto e gráficos.
