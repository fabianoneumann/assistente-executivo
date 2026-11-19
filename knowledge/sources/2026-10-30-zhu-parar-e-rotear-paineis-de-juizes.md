---
titulo: "Stopping and Routing LLM Judge Panels"
tipo: paper
autor: "Bin Zhu, Yi Xie, Yanghui Rao"
url: "https://arxiv.org/abs/2608.19802"
publicado_em: 2026-08-20
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, judge-panel, routing, stopping-criteria, panel-size, model-selection, ensemble, cascade, correlated-errors, evaluation-cost, calibration]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 20/08/2026, a única versão e a lida. O comentário do arXiv diz "21 pages, 2 figures, 20 tables. Accepted at WISE 2026"; o PDF não menciona o evento. School of Computer Science and Engineering, Sun Yat-sen University (Guangzhou, China). O integral foi extraído do PDF; as tabelas que a extração embaralhou (1, 2, 3, 8, 9, 14, 16 e 17) foram lidas na página renderizada do PDF. Lida (camadas flexíveis de avaliação).

## O resumo

Um pipeline de avaliação costuma ter muitos juízes candidatos: prompts gerais de LLM-juiz, modelos de recompensa, classificadores de segurança, variantes com confiança e verificadores próprios da tarefa. A pergunta de implantação, dizem os autores, não é só qual juiz é o melhor, mas quais chamar, em quais exemplos e quando parar de montar o painel. Eles formulam o desenho do painel como "a role-conditioned allocation problem": a partir de um pequeno conjunto de auditoria rotulado, de fatias declaradas e do custo de cada juiz, o método estima papéis relativos ao alvo. **Cópias** não acrescentam informação condicional, **complementos** melhoram o painel global e **especialistas** ajudam só em fatias. Os papéis induzem uma política: descartar cópias, somar complementos ao painel global, rotear especialistas por condição e parar quando o ganho de validação cai abaixo de um limiar. O método é comparado, em auditorias de raciocínio, código, segurança, preferência, modelo de recompensa, sumarização e matemática, com juízes únicos, painéis planos, heurísticas de diversidade de mesmo tamanho, empilhamento com todas as chamadas, júris de confiabilidade e cascatas frugais. O resultado é um "mapa de regimes": rotear especialistas em fatias implantáveis, parar em regimes de verificador saturado, manter conjuntos amplos quando o benefício em risco vale o custo, ignorar cópias condicionais. A saída é um plano de chamadas reutilizável e auditável para o próximo lote de avaliação.

## 1. Introdução

- Um pipeline realista pode ter um juiz geral, um prompt de rubrica, um modelo de recompensa, um classificador de segurança, uma variante com confiança e um verificador determinístico. A cada lote novo, o pesquisador decide algo concreto: chamar o painel inteiro, chamar um verificador barato e parar, rotear um juiz de segurança só para os casos arriscados, ou descartar um prompt redundante. Um ranking estático de juízes não responde a isso: o valor de um juiz depende do painel atual, da distribuição-alvo e da fatia de exemplos em que será usado.
- Um pequeno conjunto de auditoria rotulado transforma a diversidade de juízes de propriedade descritiva em política de chamada. Os exemplos dos autores: um juiz de segurança pode virar especialista em falhas de jailbreak; um verificador pode tornar vários juízes LLM redundantes; um conjunto completo ainda pode ser o ponto final certo em matemática ampla ou em modelo de recompensa. A meta é identificar esses casos antes de pagar as chamadas do próximo lote.
- A saída do método é uma política de chamada π(x) ⊆ J com um registro de parada baseado em validação. Para cada candidato, o método pergunta se ele reduz o risco de calibração fora da amostra depois de condicionar no painel atual, e se o ganho é global ou de uma fatia.
- Três afirmações: (1) a diversidade de juízes deve ser relativa ao alvo e condicional, não nominal; (2) os papéis cópia, complemento e especialista viram uma política com custos, fatias e condição de parada; (3) o valor empírico do método é um mapa de regimes para implantação: quando rotear especialistas, quando manter um painel barato parado, quando parar depois de um verificador e quando pagar o painel completo.
- Há um artigo companheiro, "A Finite-Calibration Regime Map for LLM Judge Panels", que compartilha parte das matrizes de saída dos juízes e o mesmo conjunto de juízes, mas trata de outra decisão: este escolhe chamadas condicionais e a parada; o companheiro escolhe um prefixo de painel e a família de agregação depois que as saídas já estão disponíveis.

## 2. Alocação condicionada por papel

**Definições.**

- X é o item avaliado e Y ∈ [0, 1] o rótulo de auditoria. Um conjunto finito J de candidatos traz sinais Z_j (correto/incorreto, seguro/inseguro, A/B). Para um painel S ⊆ J, Z_S é o padrão conjunto das saídas. O pesquisador declara fatias F que importam para a distribuição-alvo (subconjuntos do LLMBar, modos de falha de segurança, tipo de gerador, nível de dificuldade). A meta é uma política π(x; J, F) ⊆ J que decide quais juízes chamar em x.
- Preditor oráculo do painel: η_{P,S}(z) = E_P[Y | Z_S = z]. Risco oráculo com perda quadrática: R*_{P,S} = E_P[(Y − η_{P,S}(Z_S))²].
- Valor condicional de acrescentar o juiz j ∉ S: g_P(j | S) = R*_{P,S} − R*_{P,S∪{j}}, "a informação sobre o alvo que está em j e ainda não está em S".
- **Lema 1 (identidade do ganho por projeção):** g_P(j | S) = E_P[(η_{P,S∪{j}} − η_{P,S})²] ≥ 0. A identidade não exige nenhuma hipótese de independência entre os juízes.
- Ganho amplo C_P(j | S) = g_P(j | S); ganho de fatia A_f(j | S) = g_{P_f}(j | S). O perfil de papel é o par (C_P, {A_f}) e é multirrótulo: um juiz pode ser complemento amplo e especialista de fatia ao mesmo tempo, e o papel pode mudar depois que outro juiz entra no painel.
- O perfil é "an action interface rather than a naming scheme". Exemplos dos autores: um modelo de recompensa fraco como juiz de preferência isolado ainda pode ser complemento depois que um prompt de rubrica entra, se separar casos que o prompt junta; um segundo prompt da mesma família de modelos pode virar cópia se o ganho condicional some depois do primeiro.
- Razão de especialização, diagnóstica: ρ_f(j | S) = g_{P_f}(j | S) / (g_P(j | S) + ε₀), com ε₀ > 0 só para evitar divisão por zero. Não torna os papéis mutuamente exclusivos; sinaliza concentração de valor.

**Tabela 1 (papel, padrão do sinal, implicação para a política).** Os papéis são relativos ao alvo, condicionais ao painel atual e podem se sobrepor.

| Papel | Padrão do sinal | Implicação |
|---|---|---|
| Cópia | ganhos amplo e de fatia abaixo do limiar | não chamar por padrão |
| Complemento | ganho amplo C_P(j \| S) acima do limiar | somar ao painel global |
| Especialista | ganho de fatia ajustado pelo custo passa o limiar da fatia | rotear para os exemplos da fatia |
| Complemento + especialista | ganho amplo alto e concentrado em uma ou mais fatias | chamar globalmente; opcionalmente priorizar na fatia |

A Figura 1 ilustra os três papéis: cópia (o painel diz "A", "A" e o candidato também "A": sem ganho condicional, descartar por padrão), complemento (o painel diz "Valid", "Valid" e o candidato "Invalid": ganho condicional global, somar ao painel) e especialista (na fatia de risco de segurança, o painel diz "Safe", "Safe" e o candidato "Unsafe": ganho só na fatia, rotear nela).

**Regra de construção.**

- Cada conjunto de auditoria é dividido em três partes: ajuste da construção, validação da construção e teste final. Calibradores de padrão estimam η pela média do rótulo em cada célula de padrão conjunto (canonicalizado) na parte de ajuste; padrão não visto na validação ou no teste cai na média de rótulo da parte de ajuste. A seleção usa só o ganho de validação; os resultados reportados usam só o teste final.
- Entra um juiz global só se max_j [ĝ^val_P(j | S) − λc_j] > τ_P, com c_j o custo do juiz e τ_P o limiar.
- Em cada fatia, entra um especialista roteado só se max_j [ĝ^val_{P_f}(j | S ∪ S_f) − λ_f c_j] > τ_f.
- A política implantada chama π(x) = S ∪ S_{f(x)} para exemplos da fatia f(x) e S nos demais. A função de fatia tem de ser computável antes da chamada roteada: rótulos verdadeiros podem definir estratos de auditoria para análise, mas não são entrada válida de π(x) num exemplo novo; rotas implantáveis usam metadados, saídas de verificador, saídas de classificador ou discordância já observada entre juízes.
- **Regra de parada:** se nenhum candidato restante passa o limiar, a política para e registra um relatório de parada baseado em validação: todo ganho amplo ou de fatia não usado está abaixo do limiar declarado. O relatório é "operational rather than asymptotic": diz que, sob a divisão da auditoria e o modelo de custo, o painel é utilizável sem mais chamadas.
- O algoritmo é guloso: começa de um painel vazio ou com sementes do usuário, ajusta o calibrador, pontua cada candidato não usado pelo ganho de validação ajustado pelo custo, adiciona o melhor só se ele passa τ_P e repete. Quando o painel global para, cada fatia roda a mesma busca com o painel global fixo. A política final é reajustada na construção inteira e avaliada uma única vez no teste final. O relatório de parada é o conjunto das desigualdades que falharam: sob a auditoria finita, as fatias, os limiares e os custos declarados, nenhuma chamada única restante vale ser acrescentada ao plano. Quem quiser buscar complementaridade em pares ou de ordem maior pode rodar o mesmo objetivo com propostas em feixe (beam) ou por subconjunto; o relatório passa a documentar esse espaço ampliado.
- O uso pretendido, nas palavras dos autores, é simples: antes de pagar chamadas futuras, usar um conjunto de auditoria rotulado para decidir se um candidato acrescenta informação condicional ao painel que de fato será chamado.

## 3. Protocolo experimental

**Tabela 2 (cenários).** Cada um entra por exercitar uma decisão diferente: somar complementos, rotear especialistas, parar cedo, descartar cópias ou aceitar a fronteira de chamar todos.

| Cenário | Por que estressa a alocação | Sinal de fatia ou rota | Status de implantação |
|---|---|---|---|
| GSM8K difícil, raciocínio | checar a resposta satura, mas a validade do raciocínio pede julgamentos LLM complementares | tipo de gerador candidato e concordância do verificador | disponível antes do rótulo final |
| MBPP public-overfit | um verificador barato de testes ocultos pode dominar alguns sinais LLM, mas não todos os casos | passou ou falhou nos testes públicos e concordância do verificador | disponível antes do rótulo dos testes ocultos |
| JailbreakBench | juízes de segurança têm valor condicional em regiões inseguras e de discordância do classificador | fatias por proxy de classificador ou discordância; o rótulo humano de segurança é só de auditoria | implantável só nas fatias proxy |
| LLMBar | falhas de preferência diferem entre os subconjuntos natural e adversariais | natural, instrução adversarial, saída adversarial, vizinho | metadados disponíveis antes de rotear |
| RewardBench / Arena100K | comparações amplas de preferência testam se painéis parados devem dar lugar à agregação completa | fonte da preferência e metadados do par | metadados disponíveis |
| SummEval | julgamento escalar de resumo testa se juízes extras melhoram um alvo contínuo | dimensão do resumo e proxy de confiança do juiz | dimensão disponível; a confiança vem do juiz |
| MATH-500 | matemática difícil testa se conjuntos amplos seguem úteis além de painéis baratos parados | nível do problema e família do gerador | metadados |
| HumanEval / GSM8K comum | verificador saturado testa se o método recusa expansão desnecessária | resultado do teste unitário ou do verificador de resposta | saída do verificador disponível antes de rotear |

- Só cenários não saturados (em que um juiz único não é perfeito) entram na avaliação principal; HumanEval e o GSM8K comum servem só como checagem de parada saturada. LLMBar roda sob três âncoras: DeepSeek, Qwen3 e JudgeLM.
- Juízes: Qwen2.5 Instruct 7B, Llama 3.1 Instruct 8B, Mistral v0.3 7B, Prometheus 2 v2.0 7B, Gemma 3 IT 12B, Atla Selene Mini (Llama 3.1, 8B) e o DeepSeek V4 Flash por API (284B de parâmetros no total, 13B ativos), com subconjuntos por tarefa. Custo normalizado: 1,0 por chamada de juiz LLM, 0,1 por verificador determinístico. Chaves de rota contam como já disponíveis (metadados, verificador, classificador ou sinal de juiz já observado); se obter a chave exigir outra chamada a modelo, ela entra no modelo de custo.
- **Linhas de base:** melhor juiz único na validação; painel plano com todos os juízes; painéis de mesmo tamanho K (top-k, diversidade por correlação e qualidade-diversidade); empilhamento ridge/logístico com todas as chamadas (Wolpert, 1992; Caruana et al., 2004); júris de confiabilidade no estilo Dawid–Skene; cascatas de confiança no estilo FrugalGPT/RouteLLM. Tudo é média de 10 divisões aleatórias; o Apêndice E traz desvios e IC de 95%. Salvo nota, τ_P = τ_f = 0,005.
- **Métrica:** risco de calibração quadrático fora da amostra em todas as tarefas (a principal, porque o método escolhe juízes pelo ganho condicional calibrado) e acurácia quando o rótulo é binário; custo médio e número médio de chamadas, porque o objeto do artigo é uma política de implantação.
- Os autores escolheram os datasets para que uma única história não explique todos os resultados: GSM8K difícil e MBPP testam combinar um verificador barato e poucos juízes LLM sem chamar todos; LLMBar testa roteamento condicional implantável; JBB testa se o valor de segurança se concentra em proxies implantáveis e em estratos de rótulo humano (rótulo humano só para avaliação); Arena100K e SummEval testam parada em cenários não saturados em que juízes extras podem piorar a calibração; RewardBench e MATH-500 são casos de fronteira em que a agregação ampla pode seguir atraente; HumanEval e GSM8K comum são checagens de sanidade: depois que um verificador objetivo resolve o alvo, a ação correta é parar.
- Cada linha de base responde a uma pergunta: o painel plano e o empilhamento respondem "e se chamarmos todos?" (pontos finais fortes em risco, a custo alto); os de mesmo tamanho, se a diversidade comum de qualidade ou correlação alcança o mesmo orçamento sem papéis; o júri de confiabilidade, se a confiabilidade global basta; a cascata frugal, se uma ordem única de qualidade com gatilho de incerteza basta. "Role allocation should win only when the missing ingredient is conditional value relative to the current panel or slice."

## 4. Resultados

**Tabela 3 (comparação principal no teste final).** Risco / acurácia; para a política de papel, também custo e número de juízes.

| Cenário | Juiz único melhor | Plano (todos) | Papel roteado com parada | Custo | Juízes |
|---|---|---|---|---|---|
| GSM8K difícil | 0,2350 / 0,6253 | 0,2106 / 0,6670 | 0,2137 / 0,6843 | 2,90 | 2,90 |
| MBPP public-overfit | 0,0226 / 0,9767 | 0,0158 / 0,9617 | 0,0097 / 0,9900 | 1,52 | 1,70 |
| JBB-7 | 0,1183 / 0,8349 | 0,1291 / 0,8409 | 0,1094 / 0,8527 | 2,29 | 2,29 |
| LLMBar-7 | 0,2180 / 0,6822 | 0,2118 / 0,6692 | 0,1884 / 0,7334 | 3,46 | 3,46 |
| RewardBench-7 | 0,0308 / 0,9678 | 0,0280 / 0,9615 | 0,0291 / 0,9660 | 1,80 | 1,80 |
| Arena100K-7 | 0,2321 / 0,6257 | 0,2462 / 0,6186 | 0,2321 / 0,6257 | 1,00 | 1,00 |
| SummEval-7 escalar | 0,0450 / – | 0,0601 / – | 0,0450 / – | 1,00 | 1,00 |
| MATH-500-5 | 0,0731 / 0,9167 | 0,0537 / 0,9309 | 0,0678 / 0,9202 | 1,70 | 1,70 |

- Leitura dos autores: em GSM8K difícil, MBPP, segurança e LLMBar, as políticas de papel recuperam acurácia útil com menos chamadas que o painel plano. Arena100K e SummEval pedem outra ação: manter o juiz único forte, porque expandir acrescenta pouco. RewardBench e MATH-500 mostram o ponto final do painel completo, onde sinais amplos extras podem valer o custo quando se quer o menor risco.
- No GSM8K difícil, o alvo é decidir se o raciocínio é válido, não checar a resposta; a política com parada melhora a acurácia sobre o juiz único e o painel plano chamando cerca de três juízes. No MBPP, o verificador de testes ocultos é barato e forte, mas não elimina toda a incerteza da auditoria; a política chega à melhor acurácia reportada a um custo perto de uma chamada e meia, "verifier-first stopping with selective LLM additions".

**Tabela 4 (linhas de base fortes).** Risco e custo.

| Cenário | Melhor com todas as chamadas | Melhor de mesmo tamanho, sem papel | Política de papel |
|---|---|---|---|
| GSM8K difícil | 0,1963 (6,10) | 0,2114 (2,90) | 0,2137 (2,90) |
| MBPP public-overfit | 0,0067 (6,10) | 0,0117 (1,61) | 0,0097 (1,52) |
| JBB-7 DeepSeek | 0,1069 (7,00) | 0,1151 (1,90) | 0,1094 (2,29) |
| LLMBar-7 DeepSeek | 0,1804 (7,00) | 0,1967 (2,50) | 0,1884 (3,46) |
| LLMBar-7 Qwen3 | 0,2034 (7,00) | 0,2190 (2,20) | 0,2033 (3,28) |
| LLMBar-7 JudgeLM | 0,1999 (7,00) | 0,2215 (2,30) | 0,2040 (3,48) |
| RewardBench-7 DeepSeek | 0,0201 (7,00) | 0,0284 (1,50) | 0,0291 (1,80) |
| Arena100K-7 DeepSeek | 0,2286 (7,00) | 0,2321 (1,00) | 0,2321 (1,00) |
| SummEval-7 DeepSeek | 0,0446 (7,00) | 0,0450 (1,00) | 0,0450 (1,00) |
| MATH-500-5 | 0,0536 (5,00) | 0,0668 (1,70) | 0,0678 (1,70) |

- O empilhamento com todas as chamadas é um ponto final forte porque vê todas as saídas antes de prever; a alocação por papel responde à pergunta anterior: quais saídas comprar. Segundo os autores, os papéis acrescentam mais quando a informação é condicional ao painel ou ao sinal de rota (segurança e LLMBar); em GSM8K difícil, RewardBench e MATH-500, painéis de mesmo tamanho ou com todas as chamadas podem ser tão competitivos quanto. No caso de segurança implantável (Tabela 10), rotear pelo campo gpt4_cf, e não pelo rótulo humano, chega a risco 0,1094 com 2,29 chamadas, contra 0,1069 do empilhamento de 7 chamadas.

**Tabela 5 (linhas de base de alocação).** Júri de confiabilidade é agregação de vários anotadores com todas as chamadas; cascata frugal é roteamento orçado disparado por confiança. Risco e custo.

| Cenário | Júri de confiabilidade | Cascata frugal | Política de papel |
|---|---|---|---|
| GSM8K difícil | 0,1957 (6,10) | 0,2182 (2,76) | 0,2137 (2,90) |
| MBPP public-overfit | 0,0059 (6,10) | 0,0225 (1,06) | 0,0097 (1,52) |
| JBB-7 DeepSeek | 0,1382 (7,00) | 0,1213 (1,43) | 0,1094 (2,29) |
| LLMBar-7 DeepSeek | 0,2058 (7,00) | 0,2107 (2,52) | 0,1884 (3,46) |
| LLMBar-7 JudgeLM | 0,2113 (7,00) | 0,2337 (2,60) | 0,2040 (3,48) |
| LLMBar-7 Qwen3 | 0,2232 (7,00) | 0,2333 (1,94) | 0,2033 (3,28) |
| RewardBench-7 DeepSeek | 0,0268 (7,00) | 0,0308 (1,00) | 0,0291 (1,80) |
| MATH-500-5 | 0,0631 (5,00) | 0,0658 (1,67) | 0,0678 (1,70) |

- A comparação de mesmo tamanho K é a checagem de justiça pela contagem de juízes: o top-k usa o mesmo número de juízes, mas o custo realizado pode diferir, e escolhe pela qualidade isolada na validação, não pelo valor condicional; os painéis diversos por correlação ou por qualidade-diversidade gastam orçamento parecido, mas com diversidade nominal ou par a par, não condicional ao alvo. Os ganhos em MBPP, no cenário de segurança e nas três âncoras do LLMBar mostram, segundo os autores, o que o perfil de papel acrescenta: gastar o mesmo orçamento em juízes cuja informação residual serve ao painel e à fatia (Kuncheva e Whitaker, 2003).
- O júri de confiabilidade estima quais juízes são globalmente confiáveis, mas não decide que um juiz deva ser chamado só numa fatia; a cascata frugal decide quando chamar o próximo juiz numa ordem global, pela incerteza, mas não modela especialistas. Daí a Tabela 5: as linhas de base são fortes em regimes de complemento amplo, e o roteamento por papel é a ação natural quando os modos de falha são condicionais.
- Dois modos de operação: em cenários de complemento amplo (GSM8K difícil, MBPP), júris de confiabilidade com todas as chamadas podem ter o menor risco, porque todo sinal contribui para o agregado; em cenários condicionais por fatia (segurança, LLMBar), a informação útil se concentra em modos de falha, e a política de papel é ao mesmo tempo mais barata que o júri e de menor risco que a cascata.

**Especialistas roteados (Tabela 7, LLMBar; frequência da rota em 10 divisões).** A checagem é de que o roteamento não é um painel global caro disfarçado: um juiz pode não passar o limiar amplo e ainda passar o de uma fatia, o mecanismo que falta aos júris globais e às cascatas de confiança.

| Âncora | Fatia | Juiz roteado | Frequência |
|---|---|---|---|
| DeepSeek | adversarial gptinst | llama3 8b | 6/10 |
| DeepSeek | adversarial neighbor | llama3 8b | 5/10 |
| DeepSeek | natural | gemma3 12b | 6/10 |
| Qwen3 | adversarial gptout | gemma3 12b | 5/10 |
| Qwen3 | adversarial neighbor | mistral 7b | 6/10 |
| Qwen3 | natural | gemma3 12b | 5/10 |
| JudgeLM | adversarial gptout | gemma3 12b | 5/10 |
| JudgeLM | adversarial neighbor | mistral 7b | 6/10 |
| JudgeLM | natural | gemma3 12b | 5/10 |

**Limiares de parada (Tabela 8).** Risco / acurácia / custo / juízes por limiar τ.

| Cenário | τ = 0,001 | τ = 0,005 | τ = 0,020 |
|---|---|---|---|
| GSM8K difícil | 0,2129 / 0,6790 / 3,10 / 3,10 | 0,2137 / 0,6843 / 2,90 / 2,90 | 0,2318 / 0,6373 / 1,30 / 1,30 |
| MBPP public-overfit | 0,0078 / 0,9920 / 1,53 / 1,80 | 0,0097 / 0,9900 / 1,52 / 1,70 | 0,0206 / 0,9787 / 1,01 / 1,10 |
| JBB | 0,1078 / 0,8688 / 3,68 / 3,68 | 0,1094 / 0,8527 / 2,29 / 2,29 | 0,1183 / 0,8349 / 1,00 / 1,00 |
| LLMBar | 0,1954 / 0,7303 / 4,10 / 4,10 | 0,1884 / 0,7334 / 3,46 / 3,46 | 0,1834 / 0,7443 / 2,00 / 2,00 |
| MATH-500 | 0,0617 / 0,9209 / 2,70 / 2,70 | 0,0678 / 0,9202 / 1,70 / 1,70 | 0,0731 / 0,9167 / 1,00 / 1,00 |

Os autores dizem que nenhum limiar é universalmente melhor: τ é "a transparent risk-cost dial". Limiares maiores poupam chamadas em GSM8K difícil, MBPP, JBB e MATH-500; o LLMBar é a exceção, em que um limiar mais conservador também melhora o risco, evitando expansões esparsas ou redundantes.

**Figura 2 (fronteira risco × custo)** em GSM8K difícil, MBPP, JBB-7, LLMBar-7, RewardBench-7 e MATH-500, cada ponto uma média de 10 divisões: empilhamento e júri com todas as chamadas podem ser pontos finais de baixo risco em regimes de conjunto amplo, mas exigem chamar todos os juízes; as políticas de papel ocupam regiões úteis da fronteira quando especialistas ou verificadores baratos importam.

**Tabela 6 (evidência das quatro ações).**

- Rotear especialistas: o LLMBar vai do risco 0,2118 / acurácia 0,6692 do plano para 0,1884 / 0,7334 com 3,46 chamadas; rotas repetidas aparecem nos subconjuntos adversariais e natural sob as três âncoras.
- Parar: aumentar τ reduz as chamadas em GSM8K difícil (de 3,10 para 1,30), MBPP (de 1,80 para 1,10), JBB (de 3,68 para 1,00) e MATH-500 (de 2,70 para 1,00); HumanEval e GSM8K comum param depois do verificador ou do juiz único forte.
- Descartar cópias: quatro cópias exatas no LLMBar e no JBB deixam risco e custo da política iguais (LLMBar 0,1884 / 3,46; JBB 0,1094 / 2,29), enquanto o custo do júri com todas as chamadas sobe para 11 e o risco piora (LLMBar 0,2860; JBB 0,1594).
- Expor fronteiras: em RewardBench e MATH-500, as políticas de papel são mais baratas, mas o empilhamento com todas as chamadas tem risco menor (0,0201 contra 0,0291; 0,0536 contra 0,0678). Os autores chamam o método de "regime detector": quando a informação de conjunto amplo segue valiosa e o custo é aceitável, chamar o painel completo.

**Teste de estresse com cópias (Tabela 9).** Quatro cópias exatas de um juiz DeepSeek já presente, no LLMBar e no JBB. Risco (custo):

| Cenário | Condição | Plano | Júri | Cascata | Papel |
|---|---|---|---|---|---|
| LLMBar | base | 0,2118 (7,00) | 0,2058 (7,00) | 0,2107 (2,52) | 0,1884 (3,46) |
| LLMBar | +4 cópias | 0,2118 (11,00) | 0,2860 (11,00) | 0,2107 (3,80) | 0,1884 (3,46) |
| JBB | base | 0,1291 (7,00) | 0,1382 (7,00) | 0,1213 (1,43) | 0,1094 (2,29) |
| JBB | +4 cópias | 0,1291 (11,00) | 0,1594 (11,00) | 0,1213 (1,65) | 0,1094 (2,29) |

A política de papel não muda porque as cópias têm ganho condicional de validação zero quando o original já está presente; as linhas de base com todas as chamadas pagam pelas cópias, e o júri de confiabilidade piora porque os votos duplicados ficam sobreponderados.

**O fechamento da seção, nas palavras dos autores:** quando um juiz novo traz informação condicional ampla, entra no painel global; quando o valor se concentra numa fatia declarada, é roteado em vez de chamado em toda parte; quando o ganho some depois de condicionar no painel atual, é descartado, mesmo que aumente a diversidade nominal de modelos; quando a agregação com todas as chamadas segue com menor risco e o custo é aceitável, o mapa de regimes marca o painel completo como ponto final.

## 5. Trabalhos relacionados

- **LLM como juiz.** O uso é amplo (geração aberta, seguir instruções, tradução, preferência, rubrica), assim como os vieses próprios do avaliador, como posição e comprimento. LLMBar (casos adversariais de preferência), AlpacaEval e FairEval (vieses de comprimento e posição) e JailbreakBench (segurança separada de utilidade e preferência) indicam que a utilidade de um juiz pode depender fortemente do modo de falha. "Our contribution is not a new judge benchmark": é uma política para decidir quais sinais de juiz chamar sob um orçamento finito de auditoria.
- **Painéis e avaliadores multiagente** (Verga et al., 2024; ChatEval, Chan et al., 2024) motivam a diversidade de juízes, mas não decidem, sozinhos, se um juiz extra deve ser chamado globalmente, roteado a uma fatia ou descartado como cópia. Auditorias de erro correlacionado mostram que o tamanho nominal do painel pode superestimar muito a informação efetiva (Kohli, 2026, "Nine judges, two effective votes"); resultados de painel completo calibrado mostram que juízes fracos, mas não redundantes, podem seguir úteis quando seus sinais são aprendíveis (Li, 2026, "Calibrate, don't curate"). A política dos autores reconcilia as duas observações na implantação ao reter um sinal só quando o ganho condicional em amostra finita justifica o custo da chamada.
- **Agregação de anotadores e modelos de preferência** (Dawid e Skene, 1979; Raykar et al., 2010; Whitehill et al., 2009; Bradley e Terry, 1952) estimam a confiabilidade global ou por item a partir de rótulos observados. Aqui, o sistema decide quais saídas observar. Um juiz pode ter baixa confiabilidade global e ser útil numa fatia, ou alta confiabilidade e ser redundante depois que um verificador entra no painel.
- **Conjuntos, deferimento, cascatas e calibração.** Empilhamento e seleção de conjuntos combinam saídas já observadas; medidas de diversidade de conjuntos de classificadores e seus limites (Kuncheva e Whitaker, 2003); aprender a deferir treina sistemas para rotear exemplos a um humano ou especialista (Madras et al., 2018; Mozannar e Sontag, 2020); cascatas e roteadores chamam modelos mais fortes só quando preciso (FrugalGPT; RouteLLM); seleção por wrapper, critérios de redundância condicional e cascatas orçadas de classificadores selecionam sinais sob custo de validação ou aquisição (Kohavi e John, 1997; Brown et al., 2012; Chen et al., 2012); aquisição ativa de atributos decide, por exemplo, quais atributos caros observar (Shim et al., 2018); Cascaded Selective Evaluation aplica escalonamento por confiança a juízes LLM com garantia de concordância humana (Jung et al., 2025). A diferença: aqui se seleciona, a partir de dados finitos de auditoria, uma política de painel com complementos globais, especialistas roteados e cópias não chamadas. O cenário de juízes acrescenta três restrições que roteadores comuns não tratam juntas: os sinais de rota têm de estar disponíveis antes da chamada roteada; estratos de rótulo humano podem servir de diagnóstico de auditoria sem ser entrada de rota; prompts ou modelos nominalmente diferentes podem ser cópias condicionais depois que o painel atual já foi observado.

## 6. Discussão

- A diversidade de juízes se torna útil quando muda uma ação de implantação. Uma família de modelos, um modelo de prompt ou uma cabeça de recompensa pode parecer diversa no papel e ser cópia depois de condicionar no painel; um juiz fraco isolado pode ser justamente a chamada que vale numa fatia de falha.
- O fluxo de trabalho é um laço de calibração: coletar um conjunto de auditoria rotulado, rodar o conjunto de candidatos uma vez, declarar as fatias relevantes para a decisão e ajustar a política de papel com parada. A saída é um plano com juízes globais, especialistas roteados e juízes não usados cujo ganho de validação não justificou o custo.
- Leitura operacional do plano: se um verificador determinístico domina, mantê-lo e parar; se os ganhos amplos estabilizam mas os de fatia continuam, rotear especialistas; se aparecem sinais copiados, descartá-los sem mudar o resto da política; se o painel completo segue como ponto final de menor risco e o orçamento permite, pagar por ele.
- Em divisões repetidas da auditoria, a estabilidade de risco e custo e a identidade exata do plano devem ser lidas separadamente: risco estável com rotas variáveis pede checagem de frequência, manter as chamadas recorrentes e coletar mais rótulos antes de confiar em especialistas de baixa frequência. "This frequency audit is a deployment diagnostic, not a statistical guarantee."
- O limiar é o dial de risco e custo: limiares mais baixos mantêm chamadas marginais quando o erro de avaliação é caro; mais altos produzem políticas mais enxutas quando latência ou orçamento dominam. Se pequenas mudanças no limiar alteram o painel escolhido, a auditoria sinaliza instabilidade; se as mesmas decisões de cópia, rota e parada persistem, o plano é mais crível para o próximo lote.

## 7. Extensões de implantação

A mesma interface escala em três eixos: conjuntos maiores de juízes, trocando as médias por célula por calibradores suavizados, com ajuste cruzado ou paramétricos quando as células conjuntas ficam esparsas; descoberta automática de fatias (descobrir regiões de falha candidatas, validar se algum juiz tem valor condicional nelas e rotear só os especialistas que passam o limiar); e custos normalizados trocados por preço real de API, latência, orçamento de revisão de segurança ou orçamento de carbono. A saída continua um plano de chamadas globais, especialistas roteados e candidatos parados, respaldado pela validação.

## 8. Conclusão

A mudança proposta é de descrever a diversidade de juízes para decidir chamadas de juízes: perfis relativos ao alvo identificam cópias, complementos e especialistas; a construção com parada por validação os transforma em políticas globais e roteadas; a avaliação fora da amostra reporta o equilíbrio de risco e custo. O mapa de regimes diz quando descartar, somar, rotear, parar ou pagar o painel completo. "A larger panel is not automatically more reliable, and a smaller panel is not automatically more efficient if it drops conditional information." Os autores pedem que estudos futuros de painéis de juízes reportem não só qual avaliador pontuou melhor, mas também quais juízes extras valeram a chamada, onde valeram o roteamento e por que a construção do painel parou. Financiamento: National Natural Science Foundation of China (62372483).

## Apêndices

**A. Perfil de papel e construção.**

- Interpretação dos papéis nos experimentos: cópia, quando o ganho amplo e todos os ganhos de fatia ficam abaixo do limiar depois de condicionar no painel atual; complemento amplo, quando o ganho amplo de validação ajustado pelo custo passa τ_P (entra no painel global); especialista de fatia, quando o ganho de fatia ajustado pelo custo passa τ_f (chamado só nos exemplos roteados à fatia); complemento mais especialista, quando o ganho amplo é positivo e ao menos um ganho de fatia é concentrado (entra globalmente e pode ser priorizado para interpretação na fatia). A razão de especialização não é usada para tornar complemento e especialista exclusivos.
- Algoritmo completo, em dez passos: (1) coletar um conjunto de auditoria rotulado e rodar todos os candidatos nele; (2) declarar as fatias relevantes para a distribuição de implantação; (3) dividir em ajuste, validação e teste final; (4) começar de um painel vazio ou de uma semente do usuário; (5) ajustar o calibrador de padrão do painel global na parte de ajuste; (6) estimar o ganho amplo de validação de cada candidato restante; (7) adicionar o candidato de maior ganho amplo positivo ajustado pelo custo se ele passa τ_P, senão parar a construção global; (8) em cada fatia, repetir a busca gulosa condicionando no painel global e nos especialistas já atribuídos à fatia; (9) reajustar os calibradores dos caminhos global e roteados na construção inteira; (10) avaliar a política só no teste final.
- Canonicalização das saídas: rótulos binários e de preferência viram símbolos normalizados; sufixos de confiança são retirados da tabela de padrões; notas de rubrica como as de 1 a 5 do SummEval ficam como rótulos ordinais de célula. Notas numéricas são normalizadas em [0, 1] só para o empilhamento escalar e as cascatas. Os experimentos usam linhas completas: linhas com saída faltante ou não interpretável de algum juiz declarado saem antes da divisão. Empates no ganho ajustado são resolvidos pelo ganho bruto e depois pelo identificador do juiz, o que torna a construção determinística para uma divisão fixa.
- O relatório de parada é o conjunto das desigualdades que falharam e está atrelado ao espaço de busca: com a busca gulosa padrão, registra que nenhuma chamada única adicional se justifica sob a auditoria finita, o limiar e o modelo de custo; com propostas em feixe, por pares ou por subconjunto, o mesmo formato certifica os movimentos ampliados.

**B. Datasets e fatias.**

- GSM8K difícil: checar só a resposta do GSM8K comum é fácil demais para a afirmação principal, porque um verificador de resposta satura o alvo; o cenário pergunta se o raciocínio do candidato é válido, um regime de complemento (o verificador é barato e útil, e juízes LLM ainda trazem informação condicional sobre o raciocínio).
- MBPP public-test overfit: o programa candidato sobreajustou os testes públicos ou generaliza para os ocultos? O verificador de testes ocultos é barato e muitas vezes dominante, mas juízes LLM podem ajudar nos casos residuais.
- JailbreakBench: respostas rotuladas por humanos como seguras ou inseguras. As fatias incluem estratos de rótulo humano, só para análise de auditoria, e regiões proxy definidas pela saída do classificador de segurança ou pela discordância entre juízes, essas implantáveis. A pergunta é se um juiz de segurança deve ser chamado globalmente ou só nas regiões proxy em que o painel atual não é confiável.

**Tabela 10 (JailbreakBench, roteamento por proxy).** Risco com IC de 95%, acurácia, custo.

| Política | Risco | Acurácia | Custo | Leitura dos autores |
|---|---|---|---|---|
| Juiz único melhor | 0,1183 ± 0,0105 | 0,8349 | 1,00 | referência mais barata, uma chamada |
| Plano (todos) | 0,1291 ± 0,0052 | 0,8409 | 7,00 | todos os juízes de segurança em todo item |
| Cascata frugal | 0,1213 ± 0,0115 | 0,8376 | 1,43 | ordem global disparada por incerteza |
| Empilhamento com todas as chamadas | 0,1069 ± 0,0034 | 0,8450 | 7,00 | melhor ponto final com todas as chamadas |
| Papel, global com parada | 0,1199 ± 0,0098 | 0,8258 | 1,90 | painel parado sem rota por proxy |
| Papel, roteado com parada | 0,1094 ± 0,0106 | 0,8527 | 2,29 | especialistas roteados nas fatias proxy de gpt4_cf |

O sinal de rota é o campo gpt4_cf do dataset, a saída de um classificador GPT-4 guardada à parte do rótulo humano majoritário. Em 10 divisões, a política escolheu especialistas extras na fatia proxy "classificador seguro" em 4 divisões e na "classificador inseguro" em 2. O empilhamento segue como o melhor ponto final em risco porque vê as sete saídas, mas o roteamento quase o alcança comprando cerca de um terço das chamadas. Os especialistas escolhidos não são fixos: mistral 7b safety, deepseek v4 flash safety, prometheus 7b safety e selene 8b safety aparecem em fatias proxy diferentes conforme a divisão. Os autores descrevem isso como o comportamento desejado numa auditoria de segurança em operação: usar um proxy barato de classificador para decidir onde o painel precisa de escrutínio extra e manter o painel global parado no resto.

- LLMBar: o principal benchmark de roteamento de especialistas; os subconjuntos natural e adversariais induzem modos de falha diferentes, e a política escolhe juízes diferentes para instrução adversarial, saída adversarial, vizinho adversarial e natural, em vez de expandir o painel por igual.
- RewardBench e Arena100K: testam o comportamento de conjunto amplo; as políticas de papel dão pontos baratos na fronteira, e a agregação com todas as chamadas pode seguir como o ponto final de menor risco.
- SummEval: juízes extras podem piorar ou mal melhorar o equilíbrio de risco e custo; nesse regime, a política parada em um passo é "a meaningful outcome rather than a failed panel". A política de padrão trata cada nota de 1 a 5 como símbolo discreto de célula; as linhas de base escalares usam a nota normalizada.
- MATH-500: a política parada dá o ponto mais barato, e o empilhamento com todas as chamadas pode ter risco menor.
- HumanEval e GSM8K comum: checagens de parada saturada; se um verificador de teste unitário ou de resposta já resolve o alvo, a decisão correta é parar em vez de alegar ganhos artificiais de painel.

**C. Juízes e filtragem.**

- Tabela 11, por cenário (sinais candidatos; chave de rota; verificador barato): GSM8K difícil, juízes de raciocínio DeepSeek, Llama-3.1, Mistral, Prometheus, Qwen2.5 e Selene mais o verificador de resposta do GSM8K (chave: tipo do candidato). MBPP, os mesmos seis como juízes de sobreajuste mais o verificador de testes ocultos (chave: tipo do candidato). JBB-7, juízes de segurança DeepSeek, Gemma-3, Llama-3.1, Mistral, Prometheus, Qwen2.5 e Selene (chave: gpt4_cf; sem verificador). LLMBar-7, a âncora DeepSeek, Qwen3 ou JudgeLM mais Gemma-3, Llama-3, Mistral, Prometheus, Qwen2.5 e Selene (chave: subconjunto). RewardBench, Arena100K e SummEval, DeepSeek, Gemma-3, Llama-3, Mistral, Prometheus, Qwen2.5 e Selene (chave: subconjunto ou nenhuma). MATH-500, Llama-3.1, Mistral, Prometheus, Qwen2.5 e Selene (chave: modelo candidato). HumanEval e GSM8K comum, o verificador da tarefa mais Llama-3.1, Mistral, Prometheus, Qwen2.5, Selene e, onde disponível, DeepSeek e Gemma (chave: modelo ou tipo do candidato). Nomes com sufixos v, s, safety ou de correção da tarefa são saídas de juiz em esquema direto. Famílias de modelos candidatas: DeepSeek, Qwen2.5/Qwen3, Gemma, Llama, Mistral, Prometheus, JudgeLM e Selene.
- Tabela 12 (filtragem por casos completos antes da divisão): LLMBar-7, 838 linhas, 7 juízes, 837 completas (1 descartada, Selene); JBB-7, 300, 7, 298 (2, Prometheus); MBPP, 300, 7, 300; SummEval-7, 1.600, 7, 1.600; correção em Math/GSM8K, 300, 8, 300; variantes de prompt no LLMBar, 838, 10 juízes, 680 completas (158 descartadas, 155 delas do Prometheus com prompt de letra). Por isso a auditoria de variantes de prompt é lida como teste de estresse de casos completos, não como afirmação sobre robustez de interpretação das saídas.

**D. Linhas de base.** Todas as escolhas das linhas de base usam a mesma divisão de validação da construção que a política de papel, e todos os números reportados vêm só do teste final, porque a agregação com todas as chamadas e as cascatas têm flexibilidade bastante para sobreajustar uma auditoria pequena se a regularização, a ordem ou os limiares forem escolhidos olhando o teste. O juiz único melhor é o de menor risco de validação. O plano chama todos e calibra no padrão conjunto. Os painéis de mesmo tamanho usam o mesmo número médio de chamadas da política de papel sem condicionar em papéis: top-k pela qualidade isolada na validação; diverso por correlação, desencorajando saídas muito correlacionadas; qualidade-diversidade, equilibrando qualidade isolada e diversidade nominal; o orçamento é fixado pelo comportamento na validação. O empilhamento ridge e logístico (com variantes que incluem interações par a par entre saídas) observa todas as saídas antes de prever; a variante usada em cada cenário é escolhida pelo risco de validação. O júri de confiabilidade trata os juízes como anotadores ruidosos e estima o comportamento de erro condicional ao rótulo. A cascata frugal ordena os juízes pela qualidade de validação e chama outros quando a predição calibrada atual é incerta; o limiar de incerteza é escolhido na validação, com o mesmo modelo de custo.

**E. Variação entre divisões (Tabela 13).** Média do risco fora da amostra em 10 divisões, com IC de 95% calculado como média ± t_{0,975;9}·s/√10. Os autores dizem que esses intervalos medem a variação aleatória da divisão, não a incerteza sobre datasets futuros nem sobre modelos de juiz que mudam. A coluna de papel usa a política roteada quando há roteamento e a global parada nos regimes de parada em um passo.

| Cenário | Juiz único melhor | Plano | Política de papel |
|---|---|---|---|
| GSM8K difícil | 0,2350 ± 0,0055 | 0,2106 ± 0,0116 | 0,2137 ± 0,0082 |
| MBPP public-overfit | 0,0226 ± 0,0039 | 0,0158 ± 0,0050 | 0,0097 ± 0,0096 |
| JBB-7 | 0,1183 ± 0,0105 | 0,1291 ± 0,0052 | 0,1094 ± 0,0106 |
| LLMBar-7 | 0,2180 ± 0,0116 | 0,2118 ± 0,0098 | 0,1884 ± 0,0143 |
| RewardBench-7 | 0,0308 ± 0,0015 | 0,0280 ± 0,0019 | 0,0291 ± 0,0019 |
| Arena100K-7 | 0,2321 ± 0,0034 | 0,2462 ± 0,0046 | 0,2321 ± 0,0034 |
| SummEval-7 escalar | 0,0450 ± 0,0008 | 0,0601 ± 0,0022 | 0,0450 ± 0,0008 |
| MATH-500-5 | 0,0731 ± 0,0033 | 0,0537 ± 0,0049 | 0,0678 ± 0,0058 |

**F. Leitura adicional dos resultados.** Regimes de complemento com poucos juízes: no GSM8K difícil, o juiz único chega a 0,6253 de acurácia, o plano a 0,6670 e a política parada a 0,6843 com cerca de 2,9 chamadas; os pontos finais de empilhamento e júri podem ter risco menor, mas a política recupera boa parte do benefício sem pagar todos os juízes. O MBPP é mais fácil, mas não saturado: 0,9900 de acurácia a custo 1,52, acima da acurácia do plano. Regimes de roteamento de especialistas: no LLMBar, rotear especialistas leva a acurácia de 0,6692 (plano) e 0,6822 (único) a 0,7334 com 3,46 chamadas, com o mesmo padrão qualitativo sob as âncoras Qwen3 e JudgeLM; no JBB, a política fica perto do melhor ponto final com todas as chamadas usando cerca de um terço do custo do painel completo; só fatias proxy baseadas em saída de classificador ou discordância entre juízes valem como sinal de rota na implantação. Regimes de parada em um passo: em Arena100K e SummEval, expandir o painel piora ou mal melhora o equilíbrio, e a política mantém um juiz único forte; em HumanEval e GSM8K comum, depois que um verificador resolve o alvo, todos os juízes LLM restantes têm ganho de validação útil zero. Regimes de fronteira de conjunto amplo: em RewardBench e MATH-500, as políticas paradas são mais baratas, mas o empilhamento com todas as chamadas pode ter risco menor; se o alvo ainda ganha com informação ampla e o custo é aceitável, a política diz para manter o painel completo.

**G. Auditorias de robustez para implantação.** Depois de conhecer a fronteira, quem implanta deve rodar três checagens: se as tabelas de padrão escolhidas são esparsas, se o plano é estável com menos rótulos de auditoria e se a mistura de fatias esperada bate com a da auditoria; depois aplica o modelo de custo relevante.

- Tabela 14 (esparsidade, média de 10 divisões; ajuste/validação/teste, chamadas, células globais ocupadas, maior tabela de rota, fração da validação e do teste que caiu na média por padrão não visto): LLMBar-7, 209/209/419, 3,46, 8,3, 23,7, 8,7% e 4,4%; JBB-7, 74/75/149, 2,29, 4,8, 5,0, 4,3% e 2,2%; MBPP, 75/75/150, 1,70, 3,4, 0,0, 0,0% e 0,0%; MATH-500, 200/201/401, 1,70, 3,4, 0,0, 0,2% e 0,1%; SummEval-7, 400/400/800, 1,00, 5,0, 0,0, 0,0% e 0,0%. A pressão de padrões esparsos se concentra nos especialistas roteados de LLMBar e JBB; MBPP, MATH-500 e SummEval param em caminhos curtos e quase não caem na média. Se a queda na média é alta numa fatia-alvo, coletar mais rótulos da fatia ou limitar a profundidade da rota antes de implantá-la.
- Tabela 15 (tamanho da auditoria, com o teste fixo por semente; risco, acurácia, custo e Jaccard do plano contra o plano da auditoria inteira): LLMBar com 50%, 0,1904, 0,7371, 3,07, 0,246; com 100%, 0,1884, 0,7334, 3,46, 1,000. JBB por proxy com 50%, 0,1066, 0,8570, 1,98, 0,238; com 100%, 0,1094, 0,8527, 2,29, 1,000. MBPP com 50%, 0,0306, 0,9680, 0,65, 0,083; com 100%, 0,0097, 0,9900, 1,52, 1,000. As políticas com meia auditoria já recuperam o comportamento de risco e custo de LLMBar e JBB, mas a identidade exata do plano é menos estável. Diagnóstico dos autores: implantar quando risco e custo estão estáveis e coletar mais rótulos quando o conjunto exato de rotas importa.
- Tabela 16 (mudança na mistura de fatias entre construção e implantação; risco/acurácia do único, do plano e da política, e chamadas, média de 10 divisões deslocadas):

| Cenário | Construção | Implantação | Único | Plano | Papel | Chamadas |
|---|---|---|---|---|---|---|
| LLMBar-7 | natural-pesada | adversarial-pesada | 0,220 / 0,699 | 0,237 / 0,646 | 0,233 / 0,681 | 3,21 |
| LLMBar-7 | adversarial-pesada | natural-pesada | 0,175 / 0,782 | 0,215 / 0,686 | 0,175 / 0,782 | 2,91 |
| JBB-7 | proxy-segura-pesada | proxy-insegura-pesada | 0,147 / 0,823 | 0,154 / 0,803 | 0,147 / 0,809 | 1,90 |
| JBB-7 | proxy-insegura-pesada | proxy-segura-pesada | 0,125 / 0,828 | 0,147 / 0,724 | 0,109 / 0,855 | 2,20 |

  Leitura dos autores: as políticas de rota seguem úteis quando a auditoria de construção tem exemplos bastantes da fatia de implantação. No LLMBar, uma construção adversarial-pesada transfere bem para um lote natural-pesado, e uma construção natural-pesada não é a auditoria certa para um lote adversarial-pesado. No JBB, a construção proxy-insegura transfere para um lote proxy-seguro e escolhe um plano roteado útil.
- Tabela 17 (chamadas que aparecem em pelo menos 5 de 10 divisões; "fatia:juiz" para rotas, o resto é global): LLMBar com 50% da auditoria, global DeepSeek 8/10 e Prometheus 7/10, rota natural Gemma 5/10; com 100%, global DeepSeek 10/10 e Prometheus 10/10, rotas GPT-inst Llama 6/10, natural Gemma 6/10 e neighbor Llama 5/10. JBB por proxy com 50%, global Selene 6/10 e nenhuma rota chega a 5/10; com 100%, global Selene 8/10 e nenhuma rota proxy chega a 5/10. MBPP com 50%, global verificador de testes ocultos 5/10; com 100%, global Prometheus 7/10 e DeepSeek 7/10. Em vez de implantar toda rota específica de uma divisão, pode-se manter as chamadas que aparecem em ao menos metade das divisões. No JBB, há um juiz global estável e nenhum especialista roteado acima da frequência, então a ação conservadora é implantar a chamada global e coletar mais rótulos de fatias proxy antes de somar rotas. Rotas de baixa frequência "are not deployment failures"; pedem mais rótulos antes de confiar no especialista. A tabela não é uma garantia estatística.
- Tabela 18 (custo de produção, varrendo λ; no LLMBar e no JBB, a âncora DeepSeek por API custa 5 e os juízes locais 1; no MBPP, juízes locais 3, DeepSeek 5 e o verificador 0,05; risco, acurácia, custo, chamadas): LLMBar com λ 0, 0,1884, 0,7334, 7,46, 3,46; com 0,002, 0,1857, 0,7468, 7,08, 3,08; com 0,005, 0,1871, 0,7302, 5,05, 2,62. JBB com λ 0, 0,1094, 0,8527, 3,09, 2,29; com 0,002, 0,1146, 0,8389, 1,82, 1,82; com 0,005, 0,1169, 0,8326, 1,52, 1,52. MBPP com λ 0, 0,0097, 0,9900, 5,91, 1,70; com 0,002, 0,0141, 0,9853, 3,93, 1,60; com 0,005, 0,0224, 0,9767, 3,33, 1,40. Aumentar λ pede uma política mais enxuta sob o mesmo objetivo; os planos mantêm a mesma forma (chamadas globais, especialistas roteados, candidatos parados) e se movem pela fronteira de risco e custo.

**H. Quase-duplicatas e espaço de busca.**

- Tabela 19 (LLMBar com dez chamadas: saídas em esquema JSON e com prompt de letra de cinco famílias locais; 680 linhas completas; risco com IC de 95%, acurácia, custo): juiz único melhor 0,2350 ± 0,0035, 0,6126, 1,00; plano com todas as variantes 0,2633 ± 0,0076, 0,5668, 10,00; top-k de mesmo tamanho 0,2320 ± 0,0055, 0,6335, 2,10; cascata de confiança frugal 0,2351 ± 0,0086, 0,6300, 1,92; empilhamento logístico com todas as chamadas 0,2028 ± 0,0042, 0,6862, 10,00; papel roteado com parada 0,2122 ± 0,0080, 0,7143, 3,64. "Calling every variant is not diversity": a agregação plana de todas as variantes eleva o risco a 0,2633 com dez chamadas. Ainda assim, uma variante de prompt pode virar especialista de fatia: a política roteada chega a 0,7143 de acurácia com 3,64 chamadas, acima dos 0,6862 do empilhamento. A regra operacional dos autores: nem apagar todas as quase-duplicatas nem comprar todas as variantes; rotear variantes só onde o ganho condicional de validação passa o limiar.
- Tabela 20 (pares depois da parada gulosa; um "movimento só de par" é um par cujo ganho passa τ = 0,005 quando nenhuma adição única passa; divisões, movimentos só de par, ganho único médio, maior ganho de par): LLMBar com sete juízes, 10, 0, 0,0008, 0,0039; MBPP, 10, 0, −0,0008, 0,0008; JBB segurança, 10, 3, 0,0011, 0,0116; variantes de prompt do LLMBar, 10, 2, 0,0011, 0,0112. Em JBB e nas variantes de prompt, quem quiser buscar além de adições únicas pode ampliar o relatório de parada para movimentos em feixe ou por subconjunto.

**I. Relatórios de parada.** No HumanEval, o primeiro passo global adiciona o verificador de testes unitários e leva o risco de validação da construção a zero; todos os juízes LLM restantes ficam com ganho zero e o painel para; se o verificador está disponível e bate com o alvo, a chamada padrão é só o verificador. No LLMBar, o painel global adiciona um pequeno conjunto de complementos amplos e para quando o próximo ganho amplo cai abaixo do limiar; a construção por fatia então roteia especialistas diferentes para os subconjuntos adversariais e natural: um juiz pode não valer a chamada global e valer a condicional. No teste com cópias, o relatório diz que as cópias injetadas não têm ganho condicional de validação depois do juiz original, e por isso o risco e o custo da política não mudam quando o conjunto passa de sete para onze juízes.

## Ressalvas que os autores declaram

- O relatório de parada é operacional, não assintótico, e vale para a divisão da auditoria, as fatias, os limiares, os custos e o espaço de busca usados; com a busca gulosa, certifica só que nenhuma adição única se justifica, e a Tabela 20 mostra pares que passariam o limiar em JBB e nas variantes de prompt.
- Os intervalos de confiança medem a variação aleatória de divisão, não a incerteza sobre datasets futuros nem sobre modelos de juiz que mudam; a auditoria de frequência é diagnóstico de implantação, não garantia estatística.
- A identidade exata do plano é menos estável que o risco e o custo quando a auditoria encolhe (Jaccard de 0,083 a 0,246 com metade da auditoria); rotas de baixa frequência pedem mais rótulos.
- O calibrador é uma tabela finita de padrões: células esparsas caem na média, sobretudo nos especialistas roteados de LLMBar e JBB.
- Estratos de rótulo humano servem só de diagnóstico de auditoria; só sinais disponíveis antes da chamada (metadados, verificador, classificador, discordância já observada) valem como rota, e uma chamada extra para obter a chave de rota tem de entrar no custo.
- As políticas de rota seguem úteis quando a auditoria de construção tem exemplos bastantes da fatia de implantação (Tabela 16).
- A auditoria de variantes de prompt é de casos completos, com 158 linhas descartadas, e não é uma afirmação sobre robustez de interpretação das saídas.

---
