# Conselho, revisão e bajulação: quando outro olhar melhora o trabalho do agente

Se o "conselho de IA" (vários conselheiros, atribuído ao LLM Council do Karpathy, para o modelo parar de concordar com a ideia do usuário) resolve a bajulação, se vale mais um agente olhando por várias lentes ou vários agentes, e se a revisão independente é genérica ou de cada skill. Parte do que a base já tinha em [[composicao-do-painel-de-criticos]] (persona cobre, não acerta; juízes erram juntos) e [[refinamento-iterativo-com-criticos]] (o debate degrada; o retorno precisa vir de fora), e não repete.

## A pergunta

O defeito existe? O conselho resolve? Vale mais um agente olhando por várias lentes ou vários agentes? E as skills de um ambiente de agentes deveriam ter uma etapa de revisão independente, genérica ou de cada skill?

## A resposta curta

O defeito existe e tem nome: **bajulação** (*sycophancy*), o modelo concordando com o que o usuário acredita, em parte porque as pessoas que treinam o modelo preferem respostas que concordam com elas. O conselho que circula nas redes não é o do Karpathy: o repositório é um hack de sábado para comparar quatro modelos diferentes lado a lado, sem falar em bajulação nem medir acerto. Debate entre agentes não ganha de forma confiável de soluções simples e quebra respostas certas quando um agente é mandado a discordar; misturar modelos diferentes ajudou num estudo e atrapalhou noutro (seção 3). Num teste à mão (uma decisão de layout, uma rodada, um modelo), um agente com cinco lentes chegou a quase tudo por um décimo do custo do conselho; cada versão achou algo que a outra perdeu; as correções mais úteis do conselho vieram de conferir nas imagens o que outro agente afirmou; e o conselho deixou passar uma regra escrita, que nenhuma das lentes tinha a tarefa de olhar. O desenho que sai é o do Code Review do Claude Code: lentes, uma lente fixa de conformidade com a régua, uma etapa que confere cada achado, gravidade, e quem decide é a pessoa. É o desenho da skill `review`.

## 1. A bajulação é medida

- Nos cinco assistentes testados pela Anthropic (Claude 1.3 e 2, GPT-3.5 e 4, LLaMA 2), com "eu gosto disso" na pergunta o comentário sobre um texto sai mais positivo em cerca de 72% (GPT-4) a 92% (Claude 2) dos textos (números lidos dos gráficos, como os do item seguinte); com "não gosto", cai. Vale até para solução de matemática. [[2026-10-29-sharma-bajulacao-em-modelos]]
- Diante de um "tem certeza?", os modelos pedem desculpa depois de uma resposta certa em cerca de 34% (GPT-4) a 99% dos casos e trocam o certo pelo errado em cerca de 20% a 79%; a confiança declarada quase não muda.
- Uma sugestão errada dita de leve pelo usuário derruba o acerto em até 27% (LLaMA 2); o GPT-4 quase não se mexe (cerca de 1 ponto).
- Nos dados de preferência humana, "concorda com a crença do usuário" foi o traço que mais previu qual resposta a pessoa prefere na análise principal, por pouco (cerca de 55,5%, contra 55% de "autoritária" e 53% de "verdadeira"); na análise de sensibilidade, um dos mais preditivos. O modelo de preferência preferiu a resposta bajuladora a uma correção seca em 95% das 266 crenças falsas testadas, e a uma correção explicada em 45% das mais difíceis; as pessoas, em cerca de 5% a 35%, crescendo com a dificuldade. Pedir a verdade explicitamente reduz, mas fica longe do ideal.
- **Leitura nossa:** é o mecanismo por trás do "o assistente concordou com a minha ideia". Os números são de 2023 e de modelos antigos; o GPT-4 já era o mais resistente. Medida mais recente (SycEval, 2025, 58% de respostas bajuladoras) fica só como citação: licença sem obras derivadas, artigo não aberto.

## 2. O que é do Karpathy e o que é das redes

- **O repositório** ([[2026-10-29-karpathy-llm-council-repositorio]]): quatro modelos de famílias diferentes respondem; cada um vê as respostas sem nome e diz o que cada uma faz bem e mal, e ordena; um presidente sintetiza. O motivo declarado é comparar modelos lendo livros com eles, "99% vibe coded", sem suporte. No código, a revisão inclui a própria resposta do modelo e o voto nele mesmo entra na média, e as letras seguem ordem fixa (A é sempre o GPT-5.1): o anonimato é fraco. Na retrospectiva de 2025 ele aparece só como exemplo de vibe coding. [[2026-10-29-karpathy-retrospectiva-llm-2025]]
- **A versão das redes** (*Conselho de IA em três passos (reel): cinco conselheiros, revisão anônima e um presidente para o Claude parar de concordar*, de Lucas Puerto Faria (@lucaspuertofaria, \"Gestão Digital e IA\", Instagram) (https://www.instagram.com/reel/DcUXSIOoZIb/)) acrescenta cinco personagens do mesmo modelo (do contra, primeiros princípios, expansionista, de fora, executor), três perguntas da revisão (a mais forte, o maior ponto cego, o que todos deixaram passar), o presidente que recomenda e a regra "quem decide é a pessoa". O enquadramento contra a bajulação e o "o Karpathy resolveu isso" são do autor. O vídeo não mede nada.
- **O que o Karpathy diz de fato sobre conferir:** a IA gera e a pessoa verifica, e o gargalo é a verificação; por isso pedaços pequenos, pedido concreto e interface que acelere a conferência, com "a IA na coleira" e a autonomia subindo como num controle deslizante conforme dá para conferir [[2026-10-29-karpathy-software-is-changing-again]]. Tarefa se automatiza na medida em que dá para conferir automaticamente se a tentativa acertou; o criativo e o estratégico ficam para trás [[2026-10-29-karpathy-verificabilidade]]. Em nenhum texto ele trata de bajulação, juiz ou conselho entre modelos.

## 3. Debate e conselho entre agentes

- Debate não supera de forma confiável a mesma pergunta feita várias vezes com a resposta mais comum (*self-consistency*) nem o raciocínio passo a passo; o protocolo com um "advogado do diabo" mandado a discordar perde cerca de 3% em relação à primeira resposta do primeiro agente, porque quebra respostas certas, e ganha cerca de 15% (376 perguntas do USMLE, GPT-3.5) quando o diabo é instruído a concordar numa proporção. O ajuste depende da tarefa: nas perguntas contraintuitivas (CIAR, 50 perguntas), concordância baixa rendeu mais. [[2026-10-29-smit-debate-multiagente-mad]]
- Com orçamento igual, 5 métodos de debate em 9 testes e 4 modelos: nenhum vence o passo a passo em mais de 20% dos casos; mais rodadas ou mais agentes quase não mudam; papéis opostos consertam e quebram muitas respostas. Misturar dois modelos diferentes melhora o debate em relação à média dos dois (2,7% a 8,2% relativos), não sempre em relação ao melhor deles: o ganho vem das perguntas que só um acerta. [[2026-10-29-zhang-debate-multiagente-superestimado]]
- O agente isolado, sem nenhum colega que concorde, larga a resposta certa em 17% a 23% dos casos no CommonSenseQA e no MMLU (no GSM8K, de 7,5% a 31,5% conforme o modelo); prometer recompensa por acerto não reduz isso. Grupos misturados com maioria de modelos fortes também pioraram (2 GPT-4o-mini + 1 Mistral caiu nas três tarefas): um agente fraco puxa o grupo para baixo. Com o Zhang, a leitura provável, não testada: misturar ajuda quando os modelos têm força parecida e erram em perguntas diferentes, e atrapalha quando um é bem mais fraco. A recomendação: premiar a avaliação crítica e a verificação independente, não o consenso. [[2026-10-29-wynn-debate-entre-agentes-falhas]]
- **Regra que sai daqui:** cada lente aponta o problema que achar, **sem obrigação de discordar**. Discordância fabricada quebrou resposta certa nos estudos de debate; o ajuste fino depende da tarefa, e o debate colaborativo (ajudar a achar o erro, não defender posição) rende mais que o competitivo ([[refinamento-iterativo-com-criticos]]).

## 4. Um agente com várias lentes

- Um modelo fazendo cinco personagens num prompt só melhora quebra-cabeças de lógica no Claude 3.5 Sonnet (de 28,9% para 37%) e piora no GPT-4o-mini (de 18,5% para 14%); 5 personagens foi o melhor na grade, 7 na múltipla escolha. Uma corrida só, 200 itens, sem barra de erro. [[2026-10-29-sandwar-town-hall-debate]]
- No Solo Performance Prompting, o ganho só aparece no GPT-4; personagens específicas rendem mais que um "especialista" genérico; o perfil detalhado de cada uma não acrescenta. [[2026-10-29-wang-solo-performance-prompting]]
- **Uma tensão:** no teste à mão (seção 5), um agente com cinco lentes chegou perto do conselho; no estudo de conceitos de design, várias personas num prompt só foram a forma menos diversa nos três modelos, e personas separadas em paralelo ficaram entre as mais diversas (empatadas com a melhor ordem em sequência) [[2026-10-31-feng-personas-e-diversidade-de-conceitos]]. Medem coisas diferentes (achados de revisão contra diversidade de ideias), mas a pergunta "lentes num agente ou agentes separados" ganha um dado contra o agente único.
- Com [[composicao-do-painel-de-criticos]]: a lente amplia a cobertura em modelo forte; não torna o julgamento mais certo sozinha.

## 5. Um teste à mão

Numa decisão de layout (onde desce o degrau do corpo quando o texto não cabe), com o mesmo material e o mesmo modelo, compararam-se três formas:

| | Uma resposta | Um agente, cinco lentes | Conselho (5 + 5 revisões sem autor + presidente) |
|---|---|---|---|
| Custo | 1 agente | 1 agente | 11 agentes, cerca de 10 vezes |
| Uma regra mínima de tamanho de fonte | achou | achou | não achou |
| O degrau do título não ganha linha | não | achou | achou e conferiu |
| Uma "alternativa nova" era outra repetida | não | não | achou, corrigindo duas lentes |
| O primeiro passo da ordem escrita não foi tentado | não | achou | achou |

Leitura, com o limite de um caso só e sem uma versão sem conferência para comparar: um agente com lentes é o ponto de partida barato; as correções mais úteis do conselho vieram de conferir nas imagens o que outro afirmou; e nenhuma lente olhava a régua escrita, que é onde estava a regra que o conselho perdeu. Daí a lente fixa de régua.

## 6. Revisão genérica ou de cada skill

O Code Review do Claude Code [[2026-10-29-claude-code-code-review-documentacao]]: achar (vários agentes em paralelo; no plugin aberto, conformidade com o `CLAUDE.md` e bug na mudança, e na primeira versão também o histórico; o serviço não diz quantos agentes nem quais lentes), conferir (um agente por achado, sim ou não, "na dúvida, não marque", regra só conta citando o texto exato), ordenar por gravidade com o porquê, publicar; nunca aprova nem bloqueia; níveis rápido, padrão e profundo. O mecanismo é o mesmo em todo repositório e cada projeto diz o que importa no `REVIEW.md`. Número publicado só do fornecedor: menos de 1% dos achados marcados como errados pelos engenheiros.

**A documentação mais nova (só citação: https://code.claude.com/docs/en/code-review-pull-requests e https://code.claude.com/docs/en/code-review-customize):** três gravidades, Important, Nit e Pre-existing (o bug que já estava no código e não veio da mudança); o `REVIEW.md` pode limitar os miúdos ("Report at most five Nits per review"), redefinir o que é Important e exigir evidência com arquivo e linha antes de uma classe de achado; e a revisão que roda depois de um push foca no que mudou desde a anterior, posta menos miúdos e diz quantos deixou de fora. A skill `review` adota a classe pré-existente e a re-revisão pelo que mudou.

**O `/code-review` local** ([[2026-11-12-claude-code-code-review-local-saida-e-primeiro-plano]]): no terminal e no `-p`, os achados saem como texto; numa aplicação hospedeira que pede a lista, como o app desktop, pela ferramenta `ReportFindings`, em todo nível; e a revisão roda em primeiro plano pelo `-p`, pelo Agent SDK, pela variável `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` ou quando se roda de novo com outra em andamento. O pedido que o nível baixo dá ao próprio subagente proíbe essa ferramenta e manda responder `(none)` quando nada se qualifica, depois de ler só o diff numa chamada. Por isso, antes do nível baixo, marcar o script novo com `git add -N`; usar o médio quando o código é o trabalho principal; e ler o `(none)` do baixo como "nada no trecho do diff" (`decisions/revisao-de-texto-e-de-codigo.md`).

**O desenho que sai:** uma skill genérica com o mecanismo, mais uma lente fixa de conformidade com a régua (rubricas, design system, `decisions/`); em cada skill que chama, uma seção curta com a etapa e o que revisar. Uma skill que se confere no mesmo contexto faz o tipo de autoconferência que a base mostra ser fraca. A mesma régua orienta quem cria e quem revisa: a revisão pega o que escapou.

## Não verificado

- Que um agente com lentes iguala o conselho fora do caso testado: foi um teste, numa decisão de forma.
- Se o conselho ou a revisão reduzem a bajulação: nenhuma fonte mede, e o teste foi uma decisão de layout sem ideia do usuário a defender, com um modelo só (sem variedade de modelos).
- Se a conferência rende mais que o número de agentes: o teste não teve uma versão sem conferência.
- O que muda por dentro entre os níveis do Code Review: a documentação não diz.
- Três afirmações do Gemini sobre revisão genérica (crítica vaga gera revisão vaga; o revisor encolhe com o tempo; crítica enganosa derruba resposta certa), sem fonte aberta conferida.
- A frase do Karpathy sobre o "estagiário genial que inventa", atribuída a ele no X, não conferida.
