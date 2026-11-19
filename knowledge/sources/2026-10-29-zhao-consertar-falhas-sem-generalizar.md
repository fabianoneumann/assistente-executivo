---
titulo: "Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them"
tipo: paper
autor: "Weixiang Zhao, Yichen Zhang, Yanyan Zhao, Jinming Bai, Bin Liang, Ruifeng Xu, Bing Qin, Ting Liu"
url: "https://arxiv.org/abs/2610.22984"
publicado_em: 2026-10-16
capturado_em: 2026-10-29
licenca: "arXiv nonexclusive-distrib 1.0 (licença padrão do arXiv, sem reuso; indicada na página do arXiv). Só ficha."
areas: [agent-engineering]
tags: [self-evolving-agents, learning-from-failure, agent-memory, agent-skills, lessons-learned, generalization, failure-attribution, verifier-feedback]
---

Ficha de estudo extensa, em palavras próprias, cobrindo o artigo inteiro na ordem dele. A licença do arXiv não permite guardar o texto integral; a cópia de trabalho (HTML e PDF da v1) ficou no scratchpad da sessão. arXiv: v1 (única) em 16/10/2026, 28 páginas, 9 figuras, 6 tabelas. Weixiang Zhao e Yichen Zhang dividem a primeira autoria. Instituições: Harbin Institute of Technology (Harbin e Shenzhen) e Chinese University of Hong Kong. Lido em 2026-10-29, na pesquisa (lições das skills).

## A pergunta

Os agentes que "evoluem" pela própria experiência, sem mudar os pesos do modelo, costumam contar com sinais positivos: trajetórias de sucesso, retorno de um verificador, ou experiência que já é útil. Em ambiente aberto e difícil, esses sinais faltam justamente quando mais se precisa deles. O artigo pergunta se o agente consegue construir capacidade nova **só a partir das próprias falhas**, e se o que aprende serve para tarefas que ainda não viu.

Três perguntas de pesquisa: (RQ1) até onde o agente aprende com falhas nessas condições e se isso generaliza; (RQ2) o que impede a experiência tirada de falhas de virar capacidade transferível; (RQ3) que condições de aprendizado faltam para a transferência funcionar.

## O cenário: evolução só com falhas, a partir do zero (CFOE)

O agente é um modelo fixo (pesos congelados) mais um **estado externo** que evolui (memória de raciocínio, documento de habilidade ou o "harness", o conjunto de instruções e procedimentos em volta do modelo), um atualizador que mexe nesse estado e um verificador que julga cada execução. As três restrições do cenário, que os autores chamam de Cold-Start Failure-Only Evolution:

1. **Partida a frio:** começa com o estado externo vazio, sem memória nem habilidades acumuladas.
2. **Só falhas:** apenas trajetórias que falharam atualizam o estado. Acertos podem acontecer, mas contam só para a avaliação; o agente segue para a próxima tarefa sem refletir sobre eles.
3. **Sem orientação privilegiada:** o veredito do verificador, a nota, a explicação do avaliador, a resposta certa e a solução de especialista ficam escondidos do agente e do atualizador. Quem usa o veredito é só o controlador do experimento, para separar o que falhou. O agente nem sabe que está vendo só falhas. Ele continua vendo o que o ambiente devolve durante a execução (resultado das ações, mudança de estado, erros de execução).

A tabela 2 do apêndice mostra o tipo de retorno escondido: no ALFWorld, quais condições do objetivo foram ou não cumpridas; no τ²-Bench, a falha na checagem do banco de dados e as ações esperadas que faltaram, com os argumentos exatos.

## Como mediram (seção 3.1 e apêndices A a C)

**Três paradigmas de autoevolução**, todos acumulando e refinando artefatos externos:

- **ReasoningBank (memória de raciocínio):** mantém uma memória que só cresce, com padrões de raciocínio destilados da própria história do agente (originalmente de sucessos e falhas). Depois de cada tarefa, reflete sobre a trajetória e destila itens de memória; para cada tarefa nova, recupera os itens relevantes e põe no contexto. Aqui, só falhas alimentam a memória, sem nenhuma trajetória de sucesso para mostrar o caminho ou permitir comparar.
- **SkillOpt (evolução de habilidade):** um documento de habilidade em linguagem natural é o artefato "treinável" de um agente congelado. Depois de cada lote de execuções, separa trajetórias de sucesso e de falha em minilotes de reflexão, propõe edições estruturadas, agrega e ranqueia, e aplica as escolhidas dentro de um orçamento fixo de edição. A habilidade candidata só é adotada se melhorar o desempenho num conjunto de validação separado do de teste; edições rejeitadas e seus resultados ficam guardados para orientar as próximas. Foi adaptado do modo original (offline, várias épocas) para fluxo online percorrido uma vez. No modo cego, a nota de validação é usada só pelo controlador para aceitar ou rejeitar; nem o agente que executa nem o que reflete a recebe.
- **Evo-Harness (evolução do harness):** converte experiência em orientação reutilizável, com estratégias gerais e procedimentos específicos por tipo de tarefa, interface ou domínio. Antes de cada tarefa, recupera a orientação relevante; depois, examina as trajetórias que falharam para extrair lições candidatas, **registrando a evidência e as condições em que cada lição se aplica**. A cada lote, um "evoluidor" compara as lições com o harness existente e decide incorporar, fundir ou descartar; lição de tipo recorrente vai para o procedimento do tópico, padrão comum a várias tarefas atualiza as estratégias gerais.

Em todos, o mesmo modelo executa e reflete.

**Modelos (10):** Qwen3.5 densos de 4B, 9B e 27B; Gemma-4-12B-it e Gemma-4-31B-it; os de mistura de especialistas Qwen3.5-35B-A3B e Gemma-4-26B-A4B-it; e, em parte dos paradigmas por causa do custo, DeepSeek-V4-Pro, GLM-5.1 e GPT-5.6 Sol. Oito modelos por paradigma nas figuras principais.

**Quatro ambientes, escolhidos por terem tarefas comprovadamente resolvíveis** (para que a falha venha da dificuldade e da limitação do agente, não de tarefa impossível):

- **ALFWorld** (tarefas domésticas em texto): 3.693 tarefas candidatas, 134 de validação nunca vistas reservadas para teste; até 30 passos.
- **τ²-Bench-Verified** (uso de ferramentas em diálogo com usuário simulado, em companhia aérea, varejo e telecom; a versão verificada corrige inconsistências do original): 178 candidatas, 100 de teste; GPT-5.5 simula o usuário; até 200 passos; sucesso só com recompensa cheia e encerramento válido.
- **WebArena-Verified** v1.2.3 (sites funcionais), quatro sites avaliados à parte: Shopping, Shopping Admin, Reddit e GitLab; cerca de um quarto das tarefas de cada site para teste (47, 46, 27 e 45) e o resto como candidatas (140, 136, 79 e 135); até 30 passos.
- **WebShop** (loja simulada com 1,18 milhão de produtos): 500 tarefas fixas, 80 para teste por amostragem estratificada por categoria, 420 candidatas; até 20 passos; nota média de 0 a 1.

**Fluxo denso de falhas, feito para cada modelo:** um agente ReAct básico, sem experiência, tenta cada candidata até três vezes; ficam só as tarefas que falharam nas três (erros de infraestrutura e de avaliador excluídos), o que tira as que se resolvem por sorte numa nova tentativa. Depois, amostragem balanceada por tipo, domínio ou categoria. Alvo: 200 tarefas no ALFWorld, 50 no τ²-Bench, 80 no WebShop e 30 por site do WebArena; se não houver tantas, entram todas as que se qualificam.

**Duas medidas, separadas de propósito:**

- **Generalização (held-out):** a cada ponto de controle, o agente roda uma vez cada tarefa do conjunto de teste fixo, nunca visto, com a experiência congelada e sem reflexão nem atualização. A curva inclui o estado inicial e o final.
- **Recuperação da tarefa de origem (conserto):** depois de cada atualização efetiva, as tarefas que geraram aquela atualização são tentadas de novo uma vez, do estado inicial, com a experiência daquele momento e sem nova reflexão. A taxa é o total de tentativas bem-sucedidas sobre o total válido, no percurso inteiro. No SkillOpt, só contam propostas aceitas; no Evo-Harness, só lotes que mudaram o harness.

## Resultado 1: conserta parte das falhas, mas não generaliza (seção 3.2, figura 2)

- **Generalização:** as curvas de teste mostram ganho limitado, e algumas configurações **caem** conforme a experiência se acumula. O SkillOpt oscila menos que os outros dois, o que os autores atribuem à porta de validação (só aceita habilidade que melhora a validação); mesmo assim, o ganho no teste é pequeno.
- **Conserto parcial:** taxas de recuperação das barras da figura 2, por modelo: no ALFWorld, ReasoningBank de 6,8% a 16,8%, SkillOpt de 6,9% a 24,1%, Evo-Harness de 7,3% a 14,7%; no τ²-Bench, ReasoningBank de 11,5% a 26,8%, SkillOpt de 0,0% a 33,3%, Evo-Harness de 13,8% a 27,8%. Alguns fluxos do τ²-Bench têm menos de 50 tarefas.
- **O exemplo que resume a lacuna:** com SkillOpt no ALFWorld, o Qwen3.5-27B recupera mais tarefas de origem que o Qwen3.5-4B (cerca de 24% contra 7%, pela leitura das barras da figura), e mesmo assim seu desempenho no teste cai. Melhorar o conserto não leva, de forma confiável, a melhorar em tarefa nova.
- **WebArena-Verified** (apêndice D.1, ReasoningBank): a maioria termina igual ou abaixo do ponto de partida no teste. O Qwen3.5-4B cai de 25,93% para 7,41% no Reddit; o DeepSeek-V4-Pro fica parado em 47,83% no Shopping Admin. Recuperação de 3,5% a 15,4%. O Qwen3.5-35B-A3B recupera 11,1% das tarefas de origem no Reddit enquanto seu teste cai de 55,56% para 48,15%.
- **WebShop** (apêndice D.1): a maioria muda pouco ou piora. GPT-5.6-Sol com Evo-Harness cai de 31,06% para 23,79%; GLM-5.1 com SkillOpt vai de 27,40% para 27,70%. Há ganhos isolados, como o Qwen3.5-27B com SkillOpt, de 21,64% para 32,18%, que não se estendem a outros modelos e paradigmas. Recuperação de 2,5% a 11,8% onde houve avaliação válida; em alguns casos nenhuma edição do SkillOpt passou na validação e não houve o que avaliar.

## Resultado 2: horizonte mais longo não fecha a lacuna (seção 3.3, figura 3)

Com 800 tarefas no ALFWorld (todas falharam nas três tentativas preliminares), para Qwen3.5-4B, Qwen3.5-27B e GLM-5.1: o teste continua sem ganho sustentado; cai mais para o Qwen3.5-27B com Evo-Harness e estaciona para o Qwen3.5-4B com SkillOpt, mesmo com recuperação parcial nos dois. Recuperação: ReasoningBank 7,6%, 11,5% e 12,3%; SkillOpt 11,5%, 26,4% e 23,7%; Evo-Harness 6,9%, 10,9% e 12,0% (4B, 27B e GLM, nessa ordem).

## Resultado 3: por que os agentes interpretam mal as próprias falhas (seção 4.1, tabela 1)

Os autores inspecionaram à mão as atualizações de experiência: como o agente leu a trajetória que falhou, a que atribuiu a falha e como essa explicação virou experiência guardada. Três anotadores (jovens adultos com formação universitária, pagos por hora) marcaram cada caso, podendo marcar mais de um modo. O texto não informa quantas atualizações foram revisadas nem a concordância entre anotadores. Quatro modos de erro:

- **M1, falso sucesso:** ações ou estados que contribuíram para a falha são registrados como boa prática. Caso (tabela 3, ALFWorld, "olhar a estátua sob a luminária"): o agente gastou 20 passos abrindo as 10 gavetas, achou a estátua na primeira prateleira, largou-a e continuou procurando a luminária até estourar os 30 passos. A memória gerada diz que ele "localizou a estátua com sucesso" ao varrer gavetas e prateleiras em ordem, e recomenda esgotar um tipo de recipiente antes de passar a outro. Transformou o desperdício que causou a falha em regra de sucesso.
- **M2, atribuição errada ou inventada:** a reflexão ignora a causa real, culpa fator sem relação ou cria explicação sem apoio na trajetória. Caso (tabela 4, loja do WebArena): o agente devia abrir a categoria "Cabinets, Racks & Shelves" (em Office Products), parou em "Racks, Shelves & Drawers" (em Home & Kitchen) por achar parecido e declarou sucesso. A memória gerada ensina a confirmar a categoria pelos filtros e pela trilha de navegação, o que ele já tinha feito; não registra o erro decisivo, que é a página parecida não ser a pedida.
- **M3, consolidação distorcida:** a observação perde a condição ou ganha certeza que não tinha ao virar experiência. Caso (tabela 5, WebShop): a regra do sistema era clicar em "voltar à busca" antes de fazer nova busca a partir da página de resultados. A reflexão entendeu certo, mas a experiência consolidada virou "sempre, se estiver na página de resultados, a ação tem de ser voltar", o que proíbe ações válidas como abrir um produto ou ir para a próxima página. O artigo resume como transformar "volte antes de nova busca" em "sempre volte da página de resultados".
- **M4, orientação venenosa:** julgamento errado ou sem apoio vira instrução direta que conflita com as regras do ambiente e causa novas falhas. Caso (tabela 6, τ²-Bench telecom): de um único episódio, a memória criou a regra "depois de três explicações sem o usuário achar a configuração, pare e transfira para um humano". Nas duas tarefas seguintes em que foi usada, o agente transferiu cedo demais e deixou de fazer os reparos que faltavam (ativar roaming, mudar a preferência de rede); na segunda, ele mesmo causou a confusão ao apresentar nomes internos de diagnóstico como se fossem itens de menu, e usou essa confusão para cumprir a regra. Os autores ressalvam que, sem repetir as tarefas com e sem a memória, isso é evidência de propagação, não prova de que apagar a memória garantiria o sucesso.

Percentual das atualizações revisadas com cada modo (tabela 1; uma atualização pode ter vários):

| Ambiente | Modelo | Paradigma | M1 falso sucesso | M2 atribuição errada | M3 distorção | M4 orientação venenosa |
|---|---|---|---|---|---|---|
| ALFWorld | Qwen3.5-27B | Memória | 41,3 | 46,5 | 32,6 | 35,5 |
| ALFWorld | Qwen3.5-27B | Habilidade | 43,8 | 39,7 | 28,8 | 37,0 |
| ALFWorld | Qwen3.5-27B | Harness | 29,9 | 38,6 | 31,5 | 36,2 |
| ALFWorld | GPT-5.6-Sol | Harness | 21,2 | 31,0 | 25,7 | 23,9 |
| τ²-Bench | Qwen3.5-27B | Memória | 34,0 | 53,2 | 29,8 | 42,6 |
| τ²-Bench | Qwen3.5-27B | Habilidade | 37,8 | 48,6 | 35,1 | 43,2 |
| τ²-Bench | Qwen3.5-27B | Harness | 27,9 | 44,2 | 34,9 | 32,6 |
| τ²-Bench | GPT-5.6-Sol | Harness | 31,7 | 39,0 | 19,5 | 26,8 |
| WebShop | Qwen3.5-27B | Habilidade | 43,3 | 31,3 | 23,9 | 38,8 |
| WebShop | Qwen3.5-27B | Harness | 28,2 | 32,4 | 23,9 | 36,6 |
| WebShop | GPT-5.6-Sol | Harness | 19,7 | 24,6 | 26,2 | 23,0 |

Padrões que os autores tiram da tabela: atribuição errada é mais comum no τ²-Bench, falso sucesso pesa mais no ALFWorld; modelos mais fortes erram menos; evoluir o harness erra menos que evoluir memória ou habilidade. A leitura: interpretações plausíveis mas sem apoio viram experiência persistente e regra de ação, e passam a guiar o comportamento contra as restrições da tarefa. Os autores chamam isso de **gargalo do diagnóstico**.

## Resultado 4: mesmo a experiência correta transfere mal (seção 4.2, figura 4)

Para separar o diagnóstico do uso, guardaram a cada ponto de controle **só** os itens de memória ou mudanças de harness verificados à mão como corretos, e compararam experiência completa, só a verificada e nenhuma, nas mesmas tarefas. Cinco configurações: Qwen3.5-27B com ReasoningBank no ALFWorld e no τ²-Bench, e GPT-5.6-Sol com Evo-Harness no ALFWorld, no τ²-Bench e no WebShop.

Resultado: só a experiência verificada melhora um pouco a recuperação das tarefas de origem nas cinco, mas o desempenho final no teste fica **igual ou abaixo** da linha sem experiência nenhuma em quatro das cinco. A inspeção mostra que essa experiência correta continua presa aos passos e condições específicos da tarefa de onde saiu. Diagnóstico ruim não é o problema todo.

## Resultado 5: o que muda quando se afrouxa o cenário (seção 5, figura 5, apêndice D.3)

Com o Qwen3.5-27B, os autores relaxaram o cenário em três direções:

- **Fonte das trajetórias:** Falha (o cenário original); Sucesso (tarefas que acertaram nas três tentativas preliminares, aprendendo só com sucessos); Misto (tarefas sorteadas, aprendendo com os dois, sem proporção fixa). Fluxos amostrados à parte para cada condição. Sucesso e Misto só com ReasoningBank e SkillOpt, porque o Evo-Harness mantém seu procedimento voltado a falhas. Em todos, o veredito continua escondido ("cego").
- **Retorno do verificador (Feedback):** em evolução só com falhas, expõe o veredito oficial, a nota e o retorno específico do ambiente, inclusive as ações esperadas e seus argumentos quando houver. Nunca trajetória de especialista ou solução completa.
- **Interação extra (Resume):** durante a reflexão, o agente pode voltar ao ambiente para diagnosticar a falha e testar correções, com 10 turnos de interação e um turno final de resumo sem ferramentas (comparação de 5, 10 e 20 turnos no apêndice). Pode usar o que observou, inclusive uma tentativa posterior que deu certo; a execução original continua contada como falha; veredito e gabarito seguem escondidos. Inspirado na análise de erro do Trace2Skill.

Resultados, sem números no texto (só curvas):

- **Sucesso dá o maior ganho no teste**; Misto também ganha, em geral menos que Sucesso. Trajetórias de sucesso mostram sequências de ação que completam a tarefa e dão referência concreta para extrair experiência. Nos quatro sites do WebArena e com SkillOpt no WebShop, Sucesso tem o maior resultado final.
- **O retorno do verificador melhora** o aprendizado só com falhas, mas o ganho é limitado perto do que vem do sucesso: o veredito diz o que falhou e o que faltou, mas o agente ainda tem de inferir a correção de comportamento e escrevê-la como experiência reutilizável.
- **A interação extra também melhora**, com ganho limitado. Orçamentos maiores dão resultado final um pouco maior, com diferenças modestas; em alguns casos, 5 e 10 turnos terminam no mesmo nível (ReasoningBank no Reddit).
- **Retorno junto com sucesso:** Sucesso com retorno e Misto com retorno melhoram sobre o ponto inicial, e o retorno acrescenta ganho em várias configurações, sobretudo no Misto; em vários sites do WebArena, Sucesso chega ao mesmo resultado com e sem retorno. A utilidade do julgamento externo depende do material de onde o agente extrai experiência.

A frase-síntese do artigo: falhas mostram o que deu errado, trajetórias de sucesso mostram "what reliably works and how useful actions compose into complete procedures" (o que funciona de forma confiável e como as ações úteis se compõem em procedimentos completos).

Observação de leitura (não é dos autores): os fluxos de Sucesso são feitos de tarefas que o modelo já acertava nas três tentativas preliminares, e os de Falha, de tarefas que ele errava nas três; o artigo não discute essa diferença de dificuldade entre as condições.

## Trabalhos relacionados (seção 6)

O artigo situa a pesquisa entre agentes que evoluem com pesos congelados: AutoGuide (diretrizes sensíveis ao contexto extraídas de trajetórias, offline), AutoManual (regras do ambiente atualizadas na interação), Dynamic Cheatsheet (memória de estratégias e código), Voyager (habilidades executáveis), Agent Workflow Memory (fluxos reutilizáveis), ReasoningBank, SkillOpt, Evo-Harness e ACE (estratégias organizadas em "playbooks" por atualizações incrementais de contexto). Em aprender com falha: Reflexion (reflexões sobre o retorno da tarefa), ExpeL (contrasta falhas e sucessos para tirar regras entre tarefas), Self-Refine e CRITIC (revisão da saída), ERL (heurísticas tiradas de falha e extração sem retorno de resultado), HarnessFix (diagnóstico ancorado em traços de execução, com validação do reparo proposto) e Sentry (guarda lições de recuperação depois de checar interações seguintes, e avalia reuso em tarefas novas sem recompensa por tarefa). O diferencial declarado: aprender de falhas densas sem explicação do verificador e medir à parte o conserto e a transferência.

## Conclusões e recomendações

- A conclusão central: há uma **lacuna consistente entre consertar e generalizar** em vários paradigmas, modelos e ambientes. A experiência tirada de falhas conserta falhas observadas, mas raramente transfere para tarefas novas, e contribuem para isso tanto a interpretação pouco confiável das falhas quanto a baixa transferência até da experiência correta. Os agentes atuais "are better at learning what went wrong than what reliably works" (aprendem melhor o que deu errado do que o que funciona).
- O artigo não traz lista de recomendações práticas. O que propõe: que pesquisas futuras busquem mecanismos "mais gerais, fundamentados e verificáveis" de aprender com falhas; e, na seção de ética, que caracterizar os erros da experiência acumulada sirva para desenhar mecanismos de avaliação e supervisão de sistemas agênticos. O desenho do estudo também separa, como medida, o conserto da tarefa de origem e a transferência para tarefa nova.

## Limites declarados

- Foco em tarefas difíceis de um conjunto restrito de benchmarks (web e corporificado); podem não cobrir a variedade de situações reais, especialmente com vários agentes ou entrada multimodal.
- Horizonte finito: o mais longo cobre 800 tarefas no ALFWorld; agentes reais podem evoluir por horizontes muito maiores, até sem fim, e fica em aberto se ganhos transferíveis surgem além do regime estudado.
- Experimentos em ambientes controlados de benchmark, com sinais de aprendizado restritos de propósito.
