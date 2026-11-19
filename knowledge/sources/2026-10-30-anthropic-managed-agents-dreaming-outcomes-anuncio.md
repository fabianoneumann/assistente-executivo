---
titulo: "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration"
tipo: artigo
autor: "Anthropic"
url: "https://claude.com/blog/new-in-claude-managed-agents"
publicado_em: 2026-05-19
capturado_em: 2026-10-30
licenca: "Blog: todos os direitos reservados ('© 2026 Anthropic PBC', rodapé da página); entra só a ficha."
areas: [anthropic-claude, agent-engineering]
tags: [managed-agents, dreaming, outcomes, evaluator-optimizer, rubric, llm-as-judge, multi-agent, agent-memory, vendor-claims]
---

Ficha de estudo, em palavras próprias, do anúncio no blog da Anthropic, datado de 19/05/2026 na página (a busca nativa de 2026-10-30 trouxe matérias de terceiros que situam o lançamento no evento Code with Claude, em 06/05/2026: SiliconANGLE, de 06/05, e Gigazine, de 07/05; uma da Let's Data Science fala em 19/05; não abertas). Texto de fornecedor: os números são da Anthropic e dos clientes, sem método publicado. A mecânica do dreaming está em [[2026-10-30-anthropic-dreaming-documentacao]]. Lida.

## O anúncio

Lança o **dreaming** nos Managed Agents como prévia de pesquisa (estende a memória revisando sessões passadas para achar padrões e ajudar os agentes a se aprimorar) e abre a desenvolvedores **outcomes**, **orquestração multiagente** e **webhooks**. A promessa: agentes mais capazes em tarefas complexas com pouca condução.

## Dreaming

- Descrito como "a scheduled process" que revisa sessões e memory stores, extrai padrões e cura memórias para os agentes melhorarem com o tempo. A pessoa escolhe o controle: o dreaming atualiza a memória sozinho, ou ela revisa as mudanças antes de entrarem. (A documentação, em [[2026-10-30-anthropic-dreaming-documentacao]], descreve uma tarefa criada por chamada de API que nunca altera o store de entrada, e não fala em agendamento.)
- Traz à tona o que um agente sozinho não vê: **erros recorrentes**, fluxos em que os agentes convergem e preferências do time. Reestrutura a memória para ela continuar com sinal alto. Útil sobretudo em trabalho longo e com vários agentes.
- **Memória e dreaming juntos:** a memória captura o que cada agente aprende enquanto trabalha; o dreaming refina essa memória entre sessões, juntando o que vários agentes aprenderam e mantendo-a atual.

## Outcomes

- A pessoa escreve uma **rubrica** do que é sucesso, e o agente trabalha em direção a ela. Um **avaliador separado** julga a saída contra os critérios "in its own context window", para não ser influenciado pelo raciocínio do agente; quando algo não está certo, aponta o que mudar, e o agente faz outra passada, até a saída ficar boa o bastante, sem uma pessoa revisando cada tentativa.
- Serve a tarefas que pedem atenção a detalhe e cobertura exaustiva, e também a qualidade subjetiva, como o texto bater com a voz da marca ou o design seguir o guia visual.
- **Números da Anthropic:** em teste, até 10 pontos a mais de sucesso na tarefa sobre um laço de prompt comum, com os maiores ganhos nos problemas mais difíceis; na geração de arquivos, +8,4% de sucesso em docx e +10,1% em pptx, em benchmarks internos. Dá para definir o resultado, deixar o agente rodar e ser avisado por webhook ao terminar.

## Orquestração multiagente

Um agente líder quebra o trabalho e delega cada parte a especialistas com modelo, prompt e ferramentas próprios (exemplo: uma investigação em que os subagentes se espalham pelo histórico de deploy, logs, métricas e chamados). Trabalham em paralelo num sistema de arquivos comum; os eventos são persistentes, então o líder pode voltar a um agente no meio do fluxo, e cada agente lembra o que fez. Cada passo é rastreável no Console.

## Casos citados

- **Harvey** (trabalho jurídico, redação longa e criação de documentos): com o dreaming, os agentes lembram entre sessões contornos de tipo de arquivo e padrões de ferramenta; taxas de conclusão subiram **cerca de 6 vezes nos testes deles** (sem linha de base nem tamanho de amostra).
- **Netflix** (time de plataforma): agente de análise de logs de centenas de builds; a orquestração analisa lotes em paralelo e traz só os padrões que se repetem em muitas aplicações.
- **Spiral, da Every** (agente de escrita por trás da nova API e da linha de comando deles): orquestração e outcomes; o agente líder roda no Haiku, recebe os pedidos e faz perguntas rápidas quando precisa, e passa a redação a subagentes no Opus, que rodam em paralelo quando o usuário pede vários rascunhos; cada rascunho recebe nota contra uma rubrica dos princípios editoriais da Every e da voz do usuário, as duas tiradas da memória, e só voltam os rascunhos que passam.
- **Wisedocs** (agente de checagem de qualidade de documentos): outcomes julgam cada revisão contra as diretrizes internas; as revisões ficaram **50% mais rápidas**, mantendo o alinhamento com o padrão do time.

## Disponibilidade

Dreaming em prévia de pesquisa (acesso por pedido); outcomes, orquestração multiagente e memória em beta pública, dentro dos Managed Agents.
