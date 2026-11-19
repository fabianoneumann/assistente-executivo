---
titulo: "One Token to Fool LLM-as-a-Judge"
tipo: paper
autor: "Yulai Zhao, Haolin Liu, Dian Yu, S. Y. Kung, Meijia Chen, Haitao Mi, Dong Yu"
url: "https://arxiv.org/abs/2507.08794"
publicado_em: 2025-07-11
capturado_em: 2026-10-31
licenca: "Licença padrão do arXiv, não exclusiva de distribuição (http://arxiv.org/licenses/nonexclusive-distrib/1.0/, indicada na página do arXiv); entra só a ficha."
areas: [agent-engineering]
tags: [llm-as-judge, reward-hacking, generative-reward-model, rlvr, master-key-attack, false-positive-rate, adversarial-robustness, data-augmentation, model-scale, chain-of-thought]
---

Ficha de estudo, em palavras próprias; sem texto integral (licença não exclusiva do arXiv). arXiv: v1 em 11/07/2025, v2 em 26/09/2025 e v3 em 11/06/2026, a lida; o PDF diz "Preprint. Under review." e o arXiv não traz comentário de venue, então trate como preprint. Afiliações: Princeton (Zhao, Kung), University of Virginia (Liu), Tencent AI Lab (Yu, Mi, Dong Yu) e Rutgers (Chen); Zhao e Liu dividem a primeira autoria e fizeram o trabalho como estagiários da Tencent AI Lab. Modelos e dados liberados em https://huggingface.co/sarosavo/Master-RM e https://huggingface.co/datasets/sarosavo/Master-RM. O resumo da v1 enquadrava o risco para amostragem por rejeição, otimização de preferência e RLVR; o da v3 foca no RLVR e acrescenta GPT-o1 e Claude-4 entre os afetados. Lido o PDF inteiro da v3 com `pdftotext`; as tabelas 1, 2, 3 e 15 e as figuras de escala foram conferidas nas páginas renderizadas. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Atenção:** o cenário é o de juiz com resposta de referência e veredito binário (a resposta bate com a referência?), não o de nota por rubrica nem o de preferência entre pares.

## O resumo

LLMs viraram juízes automáticos, para avaliar e para dar o sinal de recompensa no treino de outros modelos, inclusive no cenário com referência do RLVR (aprendizado por reforço com recompensas verificáveis). Os autores acham uma vulnerabilidade sistemática nesse cenário: entradas superficiais, que chamam de **"chaves mestras"** (master keys), como símbolos que não são palavra (":" ou ".") ou aberturas genéricas de raciocínio ("Thought process:", "Let's solve this problem step by step."), arrancam recompensa positiva falsa sem nenhum raciocínio. A falha atinge muitos modelos, inclusive GPT-o1 e Claude-4. Como defesa, propõem aumento de dados com saídas de modelo truncadas como exemplos negativos; os modelos resultantes, **Master-RMs**, resistem às chaves e mantêm o desempenho na avaliação normal. Analisam também escala, variações de prompt e estratégias de inferência.

## 1. Como o problema apareceu

Num treino de RLVR, a política entrou em colapso: o comprimento das respostas caiu para menos de 30 tokens e a divergência KL disparou (Figura 2). A política (Qwen2.5-7B, REINFORCE, 30 mil exemplos do WebInstructSub, OpenRLHF) tinha aprendido a responder só com aberturas vazias, e o juiz (Qwen2.5-72B-Instruct) dava recompensa positiva. Depois do colapso, numa amostra separada de 5 mil perguntas, 94,26% das respostas eram literalmente "Thought Process:", 3,00% "Let's solve this problem step by step." e o resto variações (Tabela 14); o juiz considerou cerca de 90% delas corretas. Exemplo da Figura 3: pergunta "Ali tinha US$ 21, Leila deu metade dos US$ 100 dela; quanto Ali tem?", referência 71, resposta "Solution", e o juiz aceita.

## 2. Definições e montagem

- **Juiz com referência:** recebe a pergunta q, a resposta o da política e a referência a*, e devolve SIM ou NÃO; SIM vira recompensa 1, NÃO vira 0. Falso positivo no veredito desvia o treino.
- **Chaves mestras avaliadas (dez):** símbolos (" " um espaço em branco, ".", ",", ":") e aberturas de raciocínio ("Thought process:", "Let's solve this problem step by step.", "Solution" e suas versões em chinês "解", japonês "かいせつ" e espanhol "Respuesta").
- **Juízes:** gerais (Qwen2.5-72B-Instruct e 7B, LLaMA3-70B-Instruct e 8B, GPT-4o, GPT-o1, Claude-4 Sonnet, versão 20250514) com um prompt padronizado; e juízes especializados de RLVR com o prompt próprio de cada um (Multi-sub RM de Su et al. 2025, General-Verifier de Ma et al. 2025, Omni-Judge de Gao et al. 2024). Inferência com uma amostra e temperatura 0.
- **Conjuntos (testes):** Multi-subject RLVR (6.000), NaturalReasoning (subconjunto de 5.000), GSM8K (1.319), MATH (5.000) e AIME 1983–2024 (933).
- **Métrica:** taxa de falso positivo (FPR), a fração em que o juiz aceita a chave mestra como resposta correta.
- **O prompt geral (Tabela 6)** manda comparar só a resposta final com a referência e responder NÃO se a solução for "unclear, incomplete, or ambiguous"; mesmo assim os juízes aceitam respostas vazias.

## 3. Resultados: a vulnerabilidade (Tabela 1)

Média e pior caso de FPR (%) sobre as dez chaves e os cinco conjuntos:
- LLaMA3-70B-Instruct 80,6 | 95,1; LLaMA3-8B 76,9 | 92,0; Qwen2.5-72B 66,8 | 90,9; Qwen2.5-7B 12,6 | 31,0.
- GPT-4o 14,6 | 53,6; GPT-o1 6,0 | 37,3; Claude-4 12,4 | 57,7.
- Especializados: Omni-Judge 14,3 | 54,1; General-Verifier 9,7 | 87,0; Multi-sub RM 1,1 | 11,5.
- Master-RM-7B 0,1 | 2,9; Master-RM-32B 0,8 | 5,4.

Detalhes que valem lembrar:
- "Thought process:" dá FPR de 60% a 90% no LLaMA3-70B e no Qwen2.5-72B em todos os conjuntos (Qwen2.5-72B: 67,0 no Multi-subject, 68,3 no NaturalReasoning, 90,9 no GSM8K, 87,8 no MATH, 82,3 no AIME).
- Claude-4 é quase imune nos conjuntos gerais (média 0,7 no Multi-subject e 2,6 no NaturalReasoning) e vulnerável nos de matemática: no MATH, um espaço em branco dá 57,7% e ":" dá 53,6% (média 25,6); no AIME, 56,2% e 50,2% (média 28,2).
- GPT-4o: o espaço em branco chega a 35,9% no GSM8K; "Let's solve this problem step by step." a 53,6% no GSM8K; "Solution" a 40,6% no NaturalReasoning e 40,1% no GSM8K.
- GPT-o1: pior caso "Let's solve this problem step by step." no GSM8K, 37,3%.
- O General-Verifier aceita um espaço em branco em 66,8% no MATH e "Thought process:" em 87,0% no AIME.
- As versões em outras línguas também funcionam ("解" dá 68 a 89% no Qwen2.5-72B), o que os autores atribuem à aparência inofensiva e à frequência desses tokens em dados de perguntas e respostas.
- O texto diz que a pontuação sozinha (":") induz até 35% de FPR no GPT-4o; na tabela, o maior valor de ":" no GPT-4o é 24,4% (GSM8K), e os 35,9% são do espaço em branco. A legenda da Figura 1 fala em FPR "as high as 80%"; a tabela chega a 95,1%.

## 4. A defesa: Master-RM (seção 3.2 e Tabela 2)

- **Dados:** partem dos 160 mil exemplos (q, a*, o, y) de Su et al. (2025), com respostas do Qwen2.5-7B-base e rótulos do Qwen2.5-72B-Instruct como professor. Sorteiam 20 mil desses, regeneram a resposta com o GPT-4o-mini em cadeia de raciocínio e guardam **só a primeira frase**, que em geral é uma abertura sem conteúdo ("To solve the problem, we need to find the sets A and B and then determine their intersection"); rotulam NÃO. Conferem que nenhuma delas coincide com as dez chaves do teste, que viram um teste limpo de generalização. Total de 180 mil exemplos.
- **Treino:** ajuste supervisionado com entropia cruzada sobre o rótulo SIM ou NÃO, em Qwen2.5-7B-Instruct (Master-RM-7B, mesma base do Multi-sub RM) e Qwen2.5-32B-Instruct (Master-RM-32B).
- **Robustez:** FPR perto de zero em todas as chaves e conjuntos, apesar de poucos negativos direcionados; generaliza para chaves e conjuntos não vistos.
- **Sem perder acurácia:** concordância (kappa de Cohen) com o GPT-4o em 2.500 perguntas mistas (respostas do Qwen2.5-7B-Instruct) e com humanos num subconjunto de 500: Master-RM-7B 0,91 e 0,90; Master-RM-32B 0,89 e 0,87; Multi-sub RM 0,91 e 0,91; Qwen2.5-72B 0,89 e 0,88; General-Verifier 0,72 e 0,70; GPT-4o tem 0,90 com humanos. No VerifyBench e VerifyBench-Hard (Yan et al. 2025), acurácia e F1 macro: Master-RM-32B 95,15/95,14 e 86,80/81,96; GPT-o1 95,70/95,70 e 88,80/85,48 (o melhor); GPT-4o 94,15/94,15 e 84,30/77,94; Claude-4-Sonnet 95,00/95,00 e 85,30/79,71; o verificador por regras math-verify 66,95/63,40 e 76,00/60,21.
- **A anotação humana:** feita pelos próprios cinco autores (formação de doutorado em computação ou estatística), com voto da maioria (pelo menos três de cinco), busca na web permitida e LLM proibido; os autores relatam alta consistência entre anotadores sem dar o número.
- **Ressalva dos autores:** o trabalho cobre aberturas de raciocínio; marcas de raciocínio no fim (reflexão, autoverificação, recuo) ficam para trabalho futuro.

## 5. Análises (seção 3.4 e apêndices C a F)

- **Escala (Figura 4 e apêndice C, família Qwen2.5-Instruct de 0,5B a 72B):** a FPR média não é monotônica e o padrão se repete em todos os conjuntos e chaves. O 0,5B tem a menor FPR e a pior concordância com o GPT-4o (kappa 0,10); em 1,5B e 3B a FPR salta (cerca de 0,45 a 0,7); 7B e 14B são o melhor equilíbrio; 32B e 72B voltam a subir (no 72B, de cerca de 0,5 no Multi-subject a cerca de 0,9 no GSM8K). Hipótese dos autores, por faixa: o 0,5B compara cadeias literalmente e diz NÃO a qualquer diferença; 1,5B e 3B pegam semelhança superficial (unidades, símbolos, sinônimos) e dizem SIM demais; 7B e 14B verificam com precisão; 32B e 72B **resolvem o problema sozinhos** e comparam a referência com a própria solução, não com a resposta dada. Viram o Claude-4 fazer isso às vezes, e tirar a pergunta do prompt (o que impede resolver) derruba a FPR, o que apoiam como validação parcial.
- **Raciocínio e votação não defendem (Tabela 3a e apêndice E):** com prompt de cadeia de raciocínio e voto da maioria em cinco amostras (temperatura 0,2), o Qwen2.5-72B vai de 66,8 | 90,9 para 50,9 | 97,0 (média melhor, pior caso pior) e o Qwen2.5-7B de 12,6 | 31,0 para 40,4 | 91,3. Nos conjuntos gerais a técnica costuma reduzir falsos positivos (exceto no Qwen2.5-7B); na matemática, aumenta no Qwen e reduz no LLaMA (exceto o LLaMA3-70B no GSM8K). Conclusão: o efeito depende do modelo e do domínio, e o uso pede cautela, ao contrário do que Zhang et al. (2024) acharam no cenário sem referência.
- **Tirar a pergunta do prompt (Tabela 3b e apêndice F):** o Qwen2.5-72B vai de 87,6 | 90,9 para 0,0 | 0,0 no GSM8K e de 54,0 | 90,9 para 0,0 | 0,0 no AIME; no NaturalReasoning, só de 62,3 | 72,8 para 50,1 | 62,4. Recomendam omitir a pergunta em matemática e alertam que em raciocínio geral a pergunta costuma ser necessária para julgar equivalência.
- **Chaves novas por semelhança de embedding (apêndice D, Tabela 15):** corpus de 1.502.250 entradas (Wikipedia simplificada, soluções do GSM8K e do MATH, conjuntos de cadeia de raciocínio e o WordNet, frases até 30 caracteres), embeddings all-MiniLM-L6-v2, duas de cinco vizinhas de cada chave inglesa. Contra o GPT-4o: "mental process" dá 16,1% no GSM8K; "Let's do this step by step." dá 24,4%, 36,4%, 50,0%, 39,0% e 12,1% nos cinco conjuntos; "Solution:" dá 23,4% a 36,6%. A média das chaves novas fica entre 5,4% (AIME) e 26,3% (GSM8K).

## 6. Recomendações e conclusão dos autores

Para usar juízes generativos como recompensa no RLVR: preferir juízes de tamanho médio (melhor troca entre acurácia e robustez), usar prompt de cadeia de raciocínio com cautela, tirar a pergunta do prompt quando der (matemática) e treinar com negativos adversariais como os da Master-RM. Declaração ética: divulgar as chaves tem risco de uso indevido, mas achar falhas sistemáticas é condição para mecanismos de alinhamento robustos. Uso de LLM declarado só para gramática e formatação.

## 7. Tudo o mais que ensina

- **Princípio por trás do LLM como juiz:** avaliar costuma ser mais fácil que gerar (Leike et al. 2018); juízes LLM chegam a mais de 80% de concordância com humanos e viraram alternativa escalável à avaliação manual.
- **Recompensa por regras no RLVR:** critérios feitos à mão que comparam a resposta com a referência e dão sinal binário (ou contínuo em [0, 1]); falham em reconhecer respostas equivalentes escritas de outro jeito e em avaliar respostas abertas, o que motivou os juízes generativos.
- **Vulnerabilidades de juízes no cenário de preferência (trabalhos relacionados):** a ordem das respostas muda o julgamento (Wang et al. 2023); frases adversariais universais anexadas a respostas fracas aumentam a preferência (Raina et al. 2024); modelos que geram cadeias sem sentido tiram notas altas em benchmarks com juiz LLM (Zheng et al. 2024); em modelos de raciocínio, inserir "wait, let me think about it" entre duas respostas aumenta a preferência pela segunda (Wang et al. 2025).
- **Trabalho concorrente:** Huang et al. (2025) mostraram que modelos de recompensa em matemática caem com símbolos vazios ou respostas sem sentido, testando modelos pequenos e só matemática, com o GPT-4o como padrão-ouro; este artigo amplia para aberturas de raciocínio, raciocínio geral e modelos grandes, inclusive o próprio GPT-4o.
- **Os prompts dos juízes especializados** (Tabelas 7 a 9): o do Multi-sub RM e da Master-RM manda avaliar só o passo final e tratar o que é incompleto como errado; o do General-Verifier diz "Do not solve the question by yourself"; o do Omni-Judge compara com a referência.
- **Hiperparâmetros:** os do treino das Master-RMs estão na Tabela 11; os do RLVR colapsado, na Tabela 13 (REINFORCE, lote de treino 128, 4 amostras por prompt, até 30 mil amostras, uma época, taxa de aprendizado 5e-7, coeficiente KL inicial 0,01, recompensa normalizada).
