# Orquestração de skills e agentes: quando dividir o trabalho

Quando vale dividir o trabalho entre agentes, como fica uma skill que cria uma peça de conteúdo de ponta a ponta usando outras skills e agentes, e o que as pessoas usam como time de agentes. Fontes: *Towards a Science of Scaling Agent Systems*, de Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Yun Liu, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu (https://arxiv.org/abs/2512.08296), *Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets*, de Dat Tran, Douwe Kiela (https://arxiv.org/abs/2604.02460), *When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail*, de Xiaoxiao Li (https://arxiv.org/abs/2601.04748), *Judging with Many Minds: Do More Perspectives Mean Less Prejudice? On Bias Amplification and Resistance in Multi-Agent Based LLM-as-Judge*, de Chiyu Ma, Enpei Zhang, Yilun Zhao, Wenjun Liu, Yaning Jia, Peijun Qing, Lin Shi, Arman Cohan, Yujun Yan, Soroush Vosoughi (https://aclanthology.org/2025.findings-emnlp.941/), *Building agents with Skills: Equipping agents for specialized work*, de Anthropic (https://claude.com/resources/articles/building-agents-with-skills-equipping-agents-for-specialized-work), *I Built a 3-Agent Content Team in Claude Code (Research → Write → Review in One Run)*, de Dheeraj Sharma (https://genaiunplugged.substack.com/p/claude-code-agents-ai-research-team), *Building agents: When to fold subagents into your main agent loop*, de Diane Sarkis (Claude Platform, Anthropic) (https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop). Complementa [[composicao-do-painel-de-criticos]] (quem julga) e [[refinamento-iterativo-com-criticos]] (como o ciclo de passadas degrada); o caso da Anthropic com subagentes de pesquisa está em *How we built our multi-agent research system*, de Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox e Daniel Ford (Anthropic) (https://www.anthropic.com/engineering/multi-agent-research-system).

## A resposta curta

Dividir o trabalho entre agentes só compensa quando o trabalho se divide de verdade: frentes independentes, que rodam em paralelo e se juntam depois. Tarefa sequencial e acoplada piora quando é dividida, e um agente único com o mesmo orçamento empata ou ganha na maior parte dos casos. A Anthropic parou de construir agentes especializados e passou a construir skills para um agente geral. Para uma peça de conteúdo: uma skill orquestradora no contexto principal chamando as skills que existem, a produção num contexto só, e subagentes só para pesquisa e avaliação.

## 1. Quando o multiagente ganha e quando perde

**Kim et al.** (Google Research, Google DeepMind e MIT; v3 de abril de 2026), 260 configurações em seis benchmarks e cinco arquiteturas:

- **Ganha em tarefa decomponível:** coordenação central melhora 80,8% em análise financeira que se divide em partes (0,631 contra 0,349 de um agente só).
- **Perde em tarefa sequencial:** em planejamento, todas as variantes multiagente pioram, de −39% (híbrida) a −70% (independente).
- **Satura com a capacidade:** quando um agente só já acerta mais de cerca de 45%, acrescentar agentes passa a dar retorno negativo. É o único efeito que se sustenta com inferência robusta.
- **Ferramenta pesa:** tarefas com muitas ferramentas pagam sobrecarga de coordenação, de 58% a 515%, com eficiência de 2 a 6 vezes menor; o efeito é direcional.
- **Amplificação de erro é descritiva:** por execução, o erro se amplifica 17,2 vezes com agentes independentes e 4,4 vezes com coordenador central, mas na regressão o efeito não é significativo, e as diferenças são mais bem explicadas por eficiência e sobrecarga. Fica como indício.
- O post do Google descreve uma versão anterior do estudo (180 configurações, quatro benchmarks, +80,9%); vale o artigo. *Towards a Science of Scaling Agent Systems*, de Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Yun Liu, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu

**Tran e Kiela** (Stanford, 2026): com o mesmo orçamento de raciocínio (de 100 a 10 mil tokens), um agente só empata ou ganha de cinco desenhos multiagente em raciocínio de vários passos. O multiagente só passa à frente quando o contexto do agente único está muito corrompido, ou com orçamento muito pequeno. Parte dos ganhos relatados de multiagente vem de mais computação não contabilizada; no Gemini 2.5, o controle de orçamento pela API infla a contagem em 4,7 vezes. *Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets*, de Dat Tran, Douwe Kiela

## 2. Um agente com skills no lugar de vários agentes

- **A Anthropic mudou de rumo:** "por que paramos de construir agentes especializados e passamos a construir skills". O desenho tem quatro camadas: o laço raciocina, o ambiente executa, o MCP conecta e as skills guiam. A skill carrega em etapas (cerca de 50 tokens da descrição, 500 do corpo, 2 mil ou mais dos anexos), o que deixa muitas skills disponíveis sem lotar o contexto. *Building agents with Skills: Equipping agents for specialized work*, de Anthropic
- **Li** (UBC e Vector Institute, 2026): um sistema multiagente pode ser "compilado" num agente com skills, trocando comunicação entre agentes por escolha de skill. Isso economiza cerca de 54% dos tokens e 50% do tempo, com acerto igual (+0,7% em média). **O limite é a biblioteca:** a escolha da skill certa fica acima de 90% até cerca de 20 skills, cai depois de 30 e chega a cerca de 20% com 200. Uma única skill parecida com outra derruba o acerto de 7% a 30%; duas, de 17% a 63%. Agrupar as skills em níveis (roteamento hierárquico) recupera de 9 a 40 pontos. *When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail*, de Xiaoxiao Li

Leitura para um projeto: as skills do projeto podem ser poucas e distintas, mas as dos plugins somam à mesma biblioteca que o modelo escolhe. Por isso a descrição de cada skill diz quando usar e quando não usar.

**Quando trazer subagentes de volta** (Sarkis, Anthropic, 22/10/2026): subagentes servem para contexto inchado, trabalho paralelo com contexto limpo, verificação e permissões separadas. Em implantações de clientes, um agente único com skills muitas vezes venceu tanto o prompt único quanto o desenho com subagentes, "muitas vezes com custo e latência menores por tarefa" (num caso, cerca de 2 vezes mais rápido; noutro, uma dúzia de especialistas difícil de manter coerente com a marca). Dividir por especialidade cria "telefone sem fio" a cada passagem, e equipes tendem a copiar o organograma nos agentes; o certo é dividir por contexto, com subagentes chamados como ferramenta antes de qualquer passagem completa. Procedimento e julgamento moram em skills; ação, dado ao vivo e limite duro (validação, portão de aprovação) moram em ferramentas, e a escolha de ferramenta piora depois de 30 a 50 definições. Para migrar: um conjunto pequeno de ponta a ponta (dez exemplos bons já bastam), trazer um subagente de cada vez, comparar tarefa a tarefa e rodar cada tarefa mais de uma vez, porque uma quebra apareceu em só uma de duas rodadas; manter como subagente só se a versão incorporada pontuar pior. *Building agents: When to fold subagents into your main agent loop*, de Diane Sarkis (Claude Platform, Anthropic)

Medir antes de manter o desenho dividido vale também para quem julga: num conjunto âncora, um painel de quatro especialistas empatou com um juiz único, e o juiz único ficou, por ser mais simples.

## 3. Juízes não devem debater

**Ma et al.** (Findings of EMNLP 2025): em sistemas de juiz com vários agentes, o debate **amplifica** os vieses de posição, prolixidade, cadeia de raciocínio e efeito manada, e o salto acontece já da rodada 0 para a 1 (na consistência de posição do DeepSeek-V3, de 0,82 para 0,71). Um meta-juiz, que lê os pareceres independentes e decide, resiste melhor, com uma queda pequena mas significativa. Acrescentar ao debate um agente sem viés ajuda pouco. *Judging with Many Minds: Do More Perspectives Mean Less Prejudice? On Bias Amplification and Resistance in Multi-Agent Based LLM-as-Judge*, de Chiyu Ma, Enpei Zhang, Yilun Zhao, Wenjun Liu, Yaning Jia, Peijun Qing, Lin Shi, Arman Cohan, Yujun Yan, Soroush Vosoughi As primárias de cada viés que o Ma mede no debate estão em [[vieses-do-juiz-llm-e-defesas]].

Daí o desenho: cada avaliador julga sozinho e quem orquestra integra, sem debate; com um juiz único, a regra é a mesma.

## 4. O que um praticante montou

**Sharma** (GenAI Unplugged, abril de 2026) montou um time de conteúdo no Claude Code com três subagentes em arquivos de `.claude/agents/`:

- **Os agentes:** pesquisador (só web, sem escrita); escritor (o único com escrita, carrega a voz e as regras da marca); e revisor só de leitura, que devolve nota e problemas em crítico, maior e menor.
- **Revisor só lê, de propósito:** "o revisor não edita arquivos, então mostra todo problema". Quando podia editar, trocava a palavra proibida e escondia o padrão.
- **Checklist vago, nota inflada:** com instrução vaga, o revisor dava 9/10 para todo rascunho. Só com checklist explícito passou a apontar problemas concretos.
- **Tempo:** a pesquisa em paralelo cai de cerca de 12 para cerca de 5 minutos; o fluxo inteiro leva cerca de 15 minutos.
- **Modelo:** o Sonnet com boas instruções deu cerca de 90% da qualidade do Opus a 20% do custo, na avaliação dele.

*I Built a 3-Agent Content Team in Claude Code (Research → Write → Review in One Run)*, de Dheeraj Sharma

## O que isso dá para uma skill de produção de conteúdo

1. A skill orquestradora roda no contexto principal e chama as skills que existem (pesquisa, apuração, roteiro, forma, exportação).
2. Texto e HTML das telas nascem no mesmo agente: é trabalho sequencial e acoplado, o caso em que dividir piora.
3. Subagentes só para o paralelo e isolável: as frentes de pesquisa e os avaliadores. Gravam em arquivo e devolvem a referência.
4. Avaliadores só leem, não debatem, e julgam contra rubrica explícita; quem orquestra integra.
5. Portões humanos na pauta, na peça renderizada e na publicação, que só acontece por pedido explícito.
