---
titulo: "Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs"
tipo: paper
autor: "Andries Smit, Paul Duckworth, Nathan Grinsztajn, Thomas D. Barrett, Arnu Pretorius"
url: "https://arxiv.org/abs/2311.17371"
publicado_em: 2023-11-29
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [multi-agent-debate, persona-prompting, self-consistency, ensemble, agreement-modulation, cost-accuracy]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 29/11/2023, v3 (lida) em 18/07/2024. Publicado nos anais do ICML 2024 (PMLR 235, rodapé do PDF). Autores da InstaDeep; Smit e Duckworth com contribuição igual. Lido em 2026-10-29, na apuração. Números com "≈" foram lidos dos gráficos do PDF renderizado (erro de leitura de uns 0,01); os demais estão no texto ou nas tabelas.

## A pergunta

Debate entre vários agentes (MAD, multi-agent debate) vale o custo extra contra estratégias de um agente só ou de amostragem paralela? Comparam protocolos em perguntas de múltipla escolha, olhando acerto, custo em dólar e tempo.

## Como mediram

- **Modelo:** GPT-3.5-turbo para todos os agentes, escolhido pelo custo; testes preliminares com GPT-4 "sugeriram achados parecidos" num subconjunto pequeno. Depois, MedQA com GPT-4 e Mixtral 8x7B.
- **Protocolos de debate (seção 2):** Society of Minds (SoM: cada agente vê as respostas dos outros a cada rodada, com resumo opcional); Multi-Persona (MP: um agente "anjo" afirma, um "diabo" discorda, um juiz decide e pode encerrar cedo); ChatEval (três modos: um após o outro com o histórico, falas simultâneas, falas simultâneas com resumidor).
- **Comparações sem debate:** agente único (com prompts simples, cadeia de raciocínio, poucos exemplos, ou Solo Performance Prompting, um agente que simula um debate interno); self-consistency (várias amostras independentes e voto da maioria); Ensemble Refinement (amostra vários raciocínios e agrega em rodadas); Medprompt sem a busca de exemplos por vizinhos (só embaralhar alternativas e conjunto de cadeias de raciocínio com poucos exemplos). A Tabela 1 resume quem tem juiz, resumidor, interação em sequência, várias chamadas e agentes assimétricos.
- **Testes:** MedQA (1.273 perguntas do exame médico americano, 4 alternativas), PubMedQA (500), MMLU só temas clínicos (123), CosmosQA (500 sorteadas), CIAR (50 perguntas de aritmética contraintuitiva), GPQA (448 perguntas de especialistas) e Chess (estado de partida de xadrez, versão curta).
- **Variações:** número de agentes, rodadas, passos de raciocínio e agregação, prompts dos agentes, resumo por rodada, parâmetros de amostragem. Tabela 3 do apêndice lista todas as configurações com nota e custo.

## Resultados

**Melhor configuração de cada protocolo (Tabela 2, melhor nota e mediana entre parênteses):**

| Protocolo | MedQA | PubMedQA | MMLU | CosmosQA | CIAR | GPQA | Chess |
|---|---|---|---|---|---|---|---|
| Medprompt | 0,65 (0,63) | 0,77 (0,77) | 0,74 (0,73) | 0,48 (0,47) | 0,54 (0,50) | 0,27 (0,25) | 0,32 (0,30) |
| Society of Mind | 0,64 (0,61) | 0,74 (0,71) | 0,73 (0,70) | 0,44 (0,39) | 0,56 (0,46) | 0,27 (0,25) | 0,26 (0,25) |
| Ensemble Refinement | 0,64 (0,60) | 0,74 (0,72) | 0,76 (0,74) | 0,45 (0,40) | 0,48 (0,46) | 0,32 (0,26) | 0,32 (0,25) |
| ChatEval | 0,60 (0,60) | 0,75 (0,73) | 0,71 (0,69) | 0,45 (0,43) | 0,48 (0,43) | 0,26 (0,25) | 0,32 (0,23) |
| Self-Consistency | 0,60 (0,60) | 0,74 (0,72) | 0,78 (0,75) | 0,46 (0,46) | 0,56 (0,52) | 0,24 (0,29) | 0,27 (0,21) |
| Agente único | 0,60 (0,59) | 0,75 (0,70) | 0,76 (0,72) | 0,45 (0,43) | 0,50 (0,50) | 0,33 (0,28) | 0,27 (0,18) |
| Multi-Persona | 0,58 (0,57) | 0,70 (0,69) | 0,72 (0,69) | 0,46 (0,42) | 0,52 (0,50) | 0,29 (0,29) | 0,33 (0,29) |

- **Nenhum protocolo domina;** o Medprompt, sem debate, é o melhor no geral e mais barato. No MedQA o melhor debate é o SoM (várias configurações em 61%), e o Multi-Persona fica uns 7% abaixo do Medprompt. Os protocolos de debate não ganham nem nos testes de raciocínio, onde se esperava que brilhassem.
- **Custo:** mais gasto e mais chamadas tendem a acertar mais, mas a relação depende muito de hiperparâmetros; passado um ponto, mais computação não garante resultado. Exemplos da Tabela 3 (MedQA, custo total): agente único US$ 0,43; Multi-Persona US$ 1,47 a 1,57; Medprompt e self-consistency US$ 2,16; SoM com 4 agentes e 3 rodadas US$ 5,18. A Tabela 3 traz notas de MedQA mais altas (0,60 a 0,78) que a Tabela 2 e a Figura 1 (até ≈0,66); o artigo não explica a diferença.
- **Variância:** Ensemble Refinement, self-consistency e agente único têm a maior variação entre configurações; o Medprompt é estável, menos no GPQA. O agente único e o self-consistency "podem ser manipulados via prompt" para variar muito, o que os autores chamam de preocupante em medicina.
- **Sensibilidade a hiperparâmetros (Figura 3):** escolhendo a configuração pelo desempenho nos outros dois testes da mesma categoria (validação cruzada), nos médicos todos superam o agente único menos o Multi-Persona, e self-consistency e Medprompt lideram (≈0,72 e ≈0,71 contra ≈0,67 do agente único); nos não médicos o agente único (≈0,41) supera todos menos Multi-Persona (≈0,42) e self-consistency (≈0,44). Conclusão deles: o melhor ajuste depende do conjunto de dados, e ganhar do agente único num conjunto novo não é garantido.
- **Quanto o debate acrescenta (Figura 4):** comparado à primeira resposta do primeiro agente, o SoM ganha ≈7%, o ChatEval ≈1,4% e o Multi-Persona perde ≈3%. A explicação: o "diabo" é instruído a discordar mesmo quando a primeira resposta está certa.

**O Multi-Persona com o ajuste de concordância (seção 3):**

- O prompt novo diz ao agente "você deve concordar com os outros agentes X% das vezes" (X é a intensidade de concordância), aplicado no prompt de sistema do "diabo".
- O efeito depende do teste (Figura 5): MedQA e PubMedQA melhoram com concordância alta; o CIAR, feito para ser contraintuitivo, segue o padrão inverso e melhora quando o segundo agente discorda forte.
- Em 376 perguntas do USMLE (Figura 6), subir a intensidade de 0 a 100% dá ≈15% de ganho ao Multi-Persona (de ≈0,47 com 10% para ≈0,65 a partir de 60%) e ≈5% ao SoM (de ≈0,675 para ≈0,73 em 80%); o ChatEval quase não muda (≈0,58 a ≈0,63). A concordância pedida no prompt de fato altera a concordância observada na primeira rodada.
- Com 90% de concordância no MedQA completo, o Multi-Persona chega a ≈0,66, que os autores descrevem como novo estado da arte "para o GPT-3" (o motor 3.5-turbo) até onde sabem, saindo de pior para melhor protocolo e passando Medprompt e self-consistency.
- Com GPT-4 no MedQA, usando o mesmo ajuste achado no GPT-3.5, o Multi-Persona é o melhor (≈0,85, contra ≈0,82 do self-consistency e ≈0,80 do Medprompt, Figura 8): o ajuste se transfere. Com Mixtral 8x7B não se transfere, talvez por diferença de arquitetura.

**Comportamento do debate (Figura 7):** o SoM tem a maior área nos gráficos de radar (acerto do consenso, algum agente acertar, mudanças de resposta, diversidade das primeiras respostas). Mudar de resposta só ajuda quando a reavaliação leva a conclusões mais certas; troca arbitrária impede o consenso.

## A recomendação

O debate, na forma original dos protocolos, não supera métodos de conjunto como Medprompt e self-consistency e custa mais chamadas; mas o problema parece ser a sensibilidade a hiperparâmetros, não o debate em si. Ajustar a concordância entre agentes é um hiperparâmetro barato e importante. O código está aberto (github.com/instadeepai/DebateLLM).

## Limites declarados

- Dependência de API de modelo fechado: tempo de resposta variável e atualizações não previstas do modelo; custo e tempo limitam a escala e a replicação. Sugerem modelos abertos em infraestrutura própria.
- O Medprompt foi implementado sem a busca de exemplos por vizinhos, para não dar vantagem por usar dados de treino.
- Os testes com GPT-4 no corpo principal foram informais e num subconjunto; a transferência de hiperparâmetros falhou no Mixtral.
- Na declaração de impacto: sistemas de pergunta e resposta médica podem errar de forma imprevista e com confiança indevida.
