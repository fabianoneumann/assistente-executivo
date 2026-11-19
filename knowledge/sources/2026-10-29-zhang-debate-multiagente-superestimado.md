---
titulo: "Stop Overvaluing Multi-Agent Debate -- We Must Rethink Evaluation and Embrace Model Heterogeneity"
tipo: paper
autor: "Hangfan Zhang, Zhiyao Cui, Jianhao Chen, Xinrun Wang, Qiaosheng Zhang, Zhen Wang, Dinghao Wu, Shuyue Hu"
url: "https://arxiv.org/abs/2502.08788"
publicado_em: 2025-02-12
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [multi-agent-debate, model-heterogeneity, self-consistency, chain-of-thought, single-agent, evaluation-methodology]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 12/02/2025, v3 (lida) em 21/06/2025. Artigo de posição; a página do arXiv não indica conferência. Autores conferidos no arXiv e no PDF: Hangfan Zhang (Penn State), Zhiyao Cui (Northwestern Polytechnical) e Jianhao Chen (Nanjing) com contribuição igual, mais Xinrun Wang, Qiaosheng Zhang, Zhen Wang, Dinghao Wu e Shuyue Hu; trabalho feito no Shanghai AI Laboratory. Lido em 2026-10-29, na apuração. Números com "≈" foram lidos dos gráficos do PDF; os demais estão no texto ou nas tabelas. As porcentagens de ganho da Tabela 4 são relativas (ex.: 76,7 contra a média 72,1 dá +6,4%).

## A pergunta

O debate entre vários agentes (MAD) melhora mesmo o modelo, ou a impressão vem de avaliações pobres: poucos testes, sem sobreposição entre artigos, comparação só contra o agente que responde direto, sem medir custo? E, se o debate atual não entrega, o que falta?

## Como mediram

- **5 métodos de debate:** Society of Minds (SoM, 3 agentes, 2 rodadas, voto da maioria), Multi-Persona (MP: anjo, diabo e juiz, até 5 rodadas), Exchange-of-Thoughts (EoT: três personagens de estudante, Kitty, Ben e Peter, que trocam soluções com confiança, até 5 rodadas), ChatEval (três personagens, Público, Crítico e Cientista, um após o outro, 2 rodadas) e AgentVerse (um agente recruta papéis, um resolvedor e três críticos debatem, um avaliador decide; em programação há um executor que roda o código). Tabela 2 compara papéis, agregação, número de agentes e de rodadas.
- **3 referências de agente único:** SA (só a pergunta), CoT ("vamos pensar passo a passo") e SC (self-consistency: várias amostras do CoT e voto da maioria; fica de fora em programação, onde há vários programas certos).
- **9 testes em 3 capacidades:** conhecimento geral (MMLU, MMLU-Pro, CommonsenseQA, ARC-Challenge, AGIEval), raciocínio matemático (GSM8K, MATH) e programação (HumanEval, MBPP), todos sem exemplos.
- **4 modelos:** gpt-4o-mini-2024-07-18, claude-3-5-haiku-2024-1022, Llama 3.1 8B instruct e Llama 3.1 70B instruct, temperatura 1, top-p 1, três repetições com desvio padrão.
- **Orçamento igualado:** rodadas ajustadas para todos os métodos gastarem cerca de 6 chamadas ao modelo, a convenção da área. Implementações oficiais de cada método.
- **Vitória, empate ou derrota:** em cada uma das 36 situações (4 modelos × 9 testes), ANOVA a 0,05 contra o CoT.

## Resultados contra CoT e self-consistency

**Placar contra o CoT nas 36 situações (Figura 2, lido do gráfico):**

| Método | Vence | Empata | Perde |
|---|---|---|---|
| SoM | 13,9% | 44,4% | 41,7% |
| MP | 0% | 22,2% | 77,8% |
| EoT | 5,6% | 36,1% | 58,3% |
| ChatEval | 11,1% | 61,1% | 27,8% |
| AgentVerse | 13,9% | 38,9% | 47,2% |

Nenhum vence o CoT em mais de 20% das situações. Por capacidade, o debate vai pior em programação (só SoM e AgentVerse têm alguma vitória) e melhor em matemática.

**GPT-4o-mini (Tabela 3, acerto em %):** no MMLU, CoT 80,73 e SC 82,13 contra SoM 74,73, MP 75,47, EoT 67,87, ChatEval 79,13 e AgentVerse 80,40. Casos extremos do MP: CommonsenseQA 68,07 contra 82,87 do CoT; MATH 51,87 contra 72,87. O AgentVerse só passa o CoT no HumanEval (85,57 contra 78,05), graças ao executor de código, que os autores consideram fora do escopo de um debate; o ChatEval só no AGIEval (68,87 contra 66,40). Com Claude 3.5 Haiku, no MMLU só o AgentVerse passa o CoT (+0,85%); os outros perdem por pelo menos 3,60%.

**Self-consistency:** onde dá para aplicar, o SC tem o maior acerto na maioria dos casos, à frente do CoT e de todos os debates.

**Replicação:** contra o agente que responde direto (SA), o debate ganha em 34 de 45 condições no GPT-4o-mini, o que bate com a literatura; a diferença é que a literatura raramente compara com CoT. Replicam que o EoT passa o CoT em GSM8K e CommonsenseQA, mas só com Claude 3.5 Haiku. A Tabela 5 mostra que os artigos originais quase não compartilham testes (o MP foi avaliado só em CommonMT e CIAR).

**Hiperparâmetros (Figura 3):** subir as rodadas de 2 para 4 ou os agentes de 3 para 9 (GSM8K, MMLU, HumanEval) quase não muda o resultado; a exceção é o EoT no GSM8K, que melhora com mais agentes e passa o CoT. Concluem que ajuste de hiperparâmetro não explica a derrota.

**Custo (Figura 6, acerto por tokens gastos):** o SC aproveita o orçamento extra (no MMLU, de ≈81% com ≈300 tokens para ≈85% com ≈4.800); os debates ou não melhoram com mais tokens (SoM no MMLU) ou melhoram e continuam abaixo do SC gastando parecido (EoT). Para eles o debate é, em geral, um jeito menos eficiente de gastar tokens.

**Por que perde (Figura 4):** comparando com o SA pergunta a pergunta, MP, ChatEval e AgentVerse corrigem muitas respostas erradas mas também estragam muitas certas (o MP estraga ≈97 no CommonsenseQA e ≈120 no MATH); SoM e EoT são conservadores, estragam pouco e corrigem pouco. O equilíbrio entre corrigir e estragar é o dilema de projeto que apontam.

## O que medem sobre usar modelos diferentes (seção 4)

- **Heter-MAD:** a cada vez que um agente fala, sorteia de qual modelo vem a resposta, de um conjunto de modelos com probabilidades que somam 1. Mesmo prompt, mesma arquitetura. Testado com GPT-4o-mini e Llama 3.1 70B, 50% cada, em SoM, EoT, ChatEval e AgentVerse; o MP ficou de fora (papéis desequilibrados e 0% de vitória contra o CoT).
- **Média dos 9 testes (Tabela 4):**

| Método | Só GPT | Só Llama | Misturado | vs média dos dois | vs média do CoT (72,5) |
|---|---|---|---|---|---|
| SoM | 74,3 | 69,9 | 76,7 | +6,4% | +5,8% |
| EoT | 73,4 | 66,5 | 75,7 | +8,2% | +4,4% |
| ChatEval | 74,8 | 69,6 | 75,1 | +4,0% | +3,6% |
| AgentVerse | 75,7 | 68,4 | 74,0 | +2,7% | +2,1% |

- Todos os métodos misturados superam a média dos seus dois modelos e a média do CoT; o SoM misturado, o método mais simples, é o melhor de todos. O ganho é menor nos métodos mais complexos (ChatEval, AgentVerse), que eles atribuem a pior compatibilidade com modelos diferentes. Na própria tabela, a referência é a média dos dois modelos: o AgentVerse misturado (74,0) fica abaixo do AgentVerse só com GPT (75,7), e em vários testes o misturado fica abaixo do melhor dos dois (MMLU: SoM só com Llama 84,6 contra 83,5 misturado).
- **De onde vem o ganho (Figura 5):** separando as perguntas em CC (os dois modelos acertam com SoM), WW (os dois erram), CW e WC (só um acerta), o misturado mantém o acerto no CC e ganha principalmente nas perguntas em que só um dos modelos sabe; no WW quase não acerta.
- **Com CoT por cima (Tabela 9, GPT-4o-mini):** pedir CoT a cada agente melhora o debate e o misturado em todos os testes menos MBPP. No MMLU, CoT 80,73, SoM 74,73, SoM com CoT 84,13, SoM com CoT e modelos misturados 87,27. A mistura de modelos ganha do SoM com CoT nos cinco testes de conhecimento geral e empata nos de matemática e programação: os dois ajustes melhoram por caminhos diferentes.

## A recomendação

Parar de superestimar o debate na forma atual: comparar sempre com referências fortes de agente único (CoT, SC), usar conjuntos de testes diversos e representativos e analisar ganho contra custo. Adotar a heterogeneidade de modelos como princípio de projeto, porque agentes do mesmo modelo minam a premissa do debate, que é a diversidade de conhecimento e de raciocínio. Questões abertas que propõem: como aproveitar a mistura de modelos de propósito; como combinar o debate com técnicas fortes de agente único; como fazer os agentes debaterem os passos do raciocínio e não só a resposta final (no estudo de caso do Apêndice B, dois agentes trocam de resposta um para a do outro só por verem que as respostas diferem); e que cenários pedem de fato conhecimentos diversos, já que a maioria das perguntas dos testes exige um só ponto de conhecimento.

## Limites declarados

- É artigo de posição: não propõem um método otimizado para modelos diferentes, só um ajuste simples para validar a ideia.
- Os estudos de caso do Apêndice B são ilustrativos, não estatísticos, e os autores reconhecem que isso enfraquece o argumento.
- Não sabem se técnicas como ReAct ou Reflexion se combinariam com o debate como o CoT se combinou.

Duas divergências internas do próprio artigo, registradas sem interpretação: o texto diz que o SoM perde do CoT nos nove testes com GPT-4o-mini, mas a Tabela 3 marca o SoM acima do CoT em GSM8K (94,93 contra 93,60) e MATH (75,40 contra 72,87); e o texto diz que SoM, EoT, ChatEval e AgentVerse vencem o CoT em cerca de 15% das situações, enquanto a Figura 2 dá 5,6% ao EoT.
