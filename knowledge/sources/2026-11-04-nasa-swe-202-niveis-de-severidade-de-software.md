---
titulo: "SWE-202 - Software Severity Levels (NASA Software Engineering Handbook)"
tipo: artigo
autor: "NASA (Software Engineering Handbook, requisito 5.5.2 da NPR 7150.2)"
url: "https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels"
capturado_em: 2026-11-04
areas: [agent-engineering]
tags: [severity-levels, defect-management, non-conformance, nasa, software-assurance, prioritization]
licenca: "a página não declara licença nem nota de direitos; conteúdo de órgão do governo dos EUA, mas sem declaração na página, então só a ficha (licença em dúvida)"
---

# NASA, SWE-202: níveis de severidade de software

Ficha em palavras próprias da página do requisito SWE-202 no Software Engineering Handbook da NASA, lida no HTML em 2026-11-04. A página não mostra data. Segue a ordem das seções da página (requisito, justificativa, orientação, projetos pequenos, lições, garantia de software, evidências), que é longa, de cerca de 7.200 palavras. O integral não entra, porque a página não declara licença.

## O requisito

O item 5.5.2 manda o gerente do projeto definir e implementar níveis de severidade claros para todas as não conformidades de software, incluindo ferramentas, COTS, GOTS, MOTS, OSS, componentes reutilizados e sistemas de solo aplicáveis. Nota do requisito: no mínimo, as classes devem incluir perda de vida ou de veículo, sucesso da missão, visível ao usuário com contorno operacional, e uma classe "outra" para o que não cabe nas anteriores. A página registra que o requisito é do histórico "NEW" na revisão C da norma e sem mudança na D.

## Definição e o que a severidade serve para

Severidade é o grau de impacto que um defeito tem sobre o desenvolvimento ou a operação do software; mais efeito sobre a funcionalidade do sistema significa severidade maior. Funções que a página lista: priorizar a correção; dar uma linguagem comum a equipes multidisciplinares (testadores, desenvolvedores, engenharia de sistemas, garantia de software) e às decisões em comitês de controle de configuração; avaliar de forma consistente todo tipo de software; dar evidência para auditorias e marcos de revisão (PDR, CDR, TRR); formar histórico para manutenção e reuso; distribuir recursos; e triar vulnerabilidades de cibersegurança.

## Como definir os níveis

- **Fatores a considerar:** criticidade do sistema (por exemplo, rotulado para humanos, cargas úteis críticas), riscos a astronautas, funcionários e público, perturbação de cronograma, funcionalidade ou coleta de dados científicos, perda possível de investimento do governo, dependência de componentes de terceiros.
- **Ações:** envolver equipes multidisciplinares, revisar e refinar as definições com regularidade, documentá-las nas diretrizes do projeto e nos planos (gerenciamento de configuração, garantia de software, carta do projeto).
- **Quantidade:** manter um número gerenciável, tipicamente entre 3 e 5; evitar definições granulares demais.
- **Treinar** todos os envolvidos nas definições e alinhar a ordem de gravidade entre software e hardware.
- Usar métricas (por exemplo, taxa de fechamento por severidade) e lições dos projetos para ajustar as definições.

## Quadro exemplo da página (cinco níveis)

| Nível | Definição | Exemplos | Tempo de resposta |
|---|---|---|---|
| Crítico (P1) | ameaça imediata ao sucesso da missão, à segurança ou à integridade do sistema | queda de subsistema crítico; falha que compromete a segurança humana; não conformidade em sistema de solo que interrompe a prontidão de lançamento; vulnerabilidade com violação de dados | menos de 1 semana; escalada à gerência |
| Alto (P2) | afeta os objetivos da missão de forma significativa, sem ameaça imediata | perda de desempenho, confiabilidade ou função; integridade de dados de carga útil; software reutilizado que se comporta de modo imprevisível em certas condições | 1 a 2 semanas |
| Médio (P3) | pode afetar componentes ou produtos de trabalho sem ameaçar a missão de imediato | interrupções leves de fluxo; bugs com contorno; discrepâncias em interfaces ou ferramentas | 3 a 6 semanas |
| Baixo (P4) | impacto mínimo; normalmente cosmético | melhorias de usabilidade; erros de digitação em documentação; falhas gráficas em telas não críticas | mais de 6 semanas, ou quando houver recurso |
| Trivial ou editorial | sem impacto mensurável | estilo de relatórios, comentários, mensagens de log; scripts de teste com formatação | a critério da equipe |

## Para projetos pequenos

A página recomenda 3 ou 4 níveis: Crítico (P1), Maior (P2), Menor (P3) e, opcional, Trivial/Editorial. Tabela da seção: crítico, resolver em até 1 semana e avisar a gerência na hora; maior, com contorno disponível, 2 a 3 semanas; menor, quando houver recurso; trivial, por esforço discricionário. Perguntas sugeridas para avaliar a severidade: impacta os objetivos da missão? Faz o sistema falhar ou produzir resultados inválidos? Há risco à segurança? Deixar sem resolver põe em risco prazo ou custo? Há contorno disponível sem grande investimento? Ferramentas leves aceitas: planilha com ID, severidade, descrição, estado e responsável; Trello, Jira, GitHub Issues, Bugzilla (a severidade vira etiqueta, como "P1"); caderno em equipes muito pequenas; uma pessoa mantém o registro e a severidade é atribuída na rotina da equipe (reuniões diárias, discussão dos resultados de teste). Defeitos menores vão a uma lista de pendências. Métricas mínimas: abertos por severidade, tempo de resolução de críticos e maiores, problemas de terceiros sem solução, tendência de descoberta.

## Software de terceiros

Procurar defeitos conhecidos em listas do fornecedor ou públicas, avaliar se afetam o contexto do projeto, atribuir severidade própria, acompanhar atualizações e integrar os dados à avaliação de risco. A seção de garantia de software acrescenta que a severidade do fornecedor pode não coincidir com a da NASA (por exemplo, um problema de usabilidade "baixo" para o fornecedor pode ser mais grave se interrompe automação ou operação de solo).

## Lições aprendidas listadas na página

Sete lições, com identificadores LLIS, que a página resume (a ficha as registra como a página as lista; não foram conferidas no banco de lições): falta de definições padronizadas leva a priorização ineficaz (LLIS-0934); rastreamento inconsistente entre subcontratados deixou não conformidades críticas sem tratamento (LLIS-2504); dependência de componentes de terceiros sem revisar defeitos conhecidos (LLIS-2215); acúmulo de problemas menores adiados levou a falha grave em sistema de solo (LLIS-1669); em sistemas críticos para a segurança, faltou prioridade clara para problemas graves (LLIS-3092); definições genéricas não refletiam riscos da missão (LLIS-1850); excesso de complexidade sobrecarregou um projeto pequeno (LLIS-1543). Recomendações derivadas: criar as definições com equipe transversal, documentar de forma breve e acessível, estender o esquema ao software de terceiros, reavaliar periodicamente inclusive o que foi adiado e integrar as severidades aos fluxos de trabalho e revisões.

## Garantia de software (NASA-STD-8739.8B) e evidências

Tarefas citadas: confirmar que os níveis estão definidos (e antes de qualquer teste); avaliar a aplicação e a exatidão deles nas não conformidades; confirmar que se atribui severidade também a ferramentas, COTS, GOTS, MOTS, OSS e reutilizados; manter ou acessar a contagem por nível para cada item de configuração. A exatidão se verifica contra as definições do projeto e uma escala-padrão de exemplo (1 = crítico, 4 ou 5 = baixa prioridade), testemunhando sessões de teste ou revisando relatórios, e perguntando se a severidade atribuída refletiu a criticidade real e se problemas de segurança foram escalados. Métricas exigidas: total de não conformidades ao longo do tempo (abertas, fechadas, dias em aberto, severidade das abertas); tendência de abertas contra fechadas; contagem por período; não conformidades de componentes de terceiros abertas contra fechadas; contagem por severidade e item de configuração. Opcionais: em código-fonte; idade das abertas. Evidências que a página lista como prova de conformidade: documento de definições, ferramenta de defeitos configurada com os níveis, relatórios de defeitos e de teste com justificativa da severidade, registros de revisão da garantia de software, relatórios de métricas, atas do comitê de controle, descrições de versão (VDD) com pendências justificadas.

## O que a fonte não diz

Não mede a concordância entre pessoas ao atribuir severidade, não dá método para separar um nível do outro além das definições e exemplos, e não indica como resolver discordância entre quem classifica. Os tempos de resposta dos quadros são exemplos da página, não requisito da norma. A página não dá data.
