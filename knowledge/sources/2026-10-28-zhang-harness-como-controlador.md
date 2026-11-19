---
titulo: "Stop Comparing LLM Agents Without Disclosing the Harness"
tipo: paper
autor: "Yunbei Zhang, Janet Wang, Yingqiang Ge, Weijie Xu, Jihun Hamm, Chandan K. Reddy"
url: "https://arxiv.org/abs/2605.23950"
publicado_em: 2026-05-07
capturado_em: 2026-10-28
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [harness, control-loop, closed-loop, agent-evaluation, binding-constraint, harness-card, variance-decomposition]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Preprint de posição, arXiv v1 em 07/05/2026, sem venue. Lido em 2026-10-28, na pesquisa.

## A tese

O **harness de execução** é a camada em volta do modelo que monta o contexto, media as ferramentas, orquestra e verifica: decide o que o modelo vê, valida a saída e escolhe quando tentar de novo, escalar ou parar. Em tarefas longas, com modelos de fronteira de capacidade parecida, ele pesa no resultado tanto quanto o modelo ou mais. Os placares medem o par modelo e harness, mas os artigos só reportam o modelo. A **Tese da Restrição Vinculante** (*Binding Constraint Thesis*): a variação de desempenho entre harnesses, com o modelo fixo, costuma ser comparável ou maior do que a variação entre modelos, com o harness fixo; comparações de placar sem o harness são incompletas e podem enganar. A tese cairia num estudo fatorial em tarefas longas em que a variação entre modelos fosse maior.

## O modelo de controle

- O estado do agente é o contexto mais a memória persistente.
- O modelo é uma **política estocástica**: escolhe a ação a partir do contexto que o harness montou.
- O harness é o **controlador**: atualiza o estado com a ação e com a observação do ambiente já filtrada.
- Sozinho, o modelo é um sistema de **laço aberto**: só vê o recorte que o harness mostra e não lembra nada além do que o harness injeta. A autocorreção depende do caminho de retorno que o harness constrói.
- Três propriedades do controlador: **estabilidade** (a distância até estados coerentes com o objetivo não cresce, em média), **deriva do contexto** (quanto o contexto se afasta da tarefa inicial) e **atraso de controle** (passos entre detectar a anomalia e o sinal corretivo chegar ao modelo).
- Em palavras simples: sistemas de laço aberto ficam confiáveis por controle com realimentação, não por atuadores maiores. Um modelo melhor reduz a frequência de anomalias, mas não melhora a forma como o controlador reage a elas.

## A evidência

- **Placares públicos** (observacional): no SWE-bench Pro, seis modelos de fronteira cabem em 4,9 pontos com o mesmo harness, mas trocar só o harness do Claude Opus 4.5 move 9,5 pontos; um subagente de busca inverte a ordem de dois modelos. No HAL, diferenças de 34 a quase 48 pontos entre harnesses para o mesmo modelo. No Terminal-Bench 2, evoluir o harness leva o mesmo modelo de 69,7% a 77,0%.
- **Experimento dos autores:** três modelos × três harnesses (mínimo, melhorado, completo) em 100 tarefas do SWE-bench Verified, duas rodadas por célula. Variação média entre harnesses de 18,48 contra 2,37 entre modelos (7,8 vezes). Trocar o harness moveu um modelo 13 pontos; trocar o modelo com o harness fixo moveu de 2,5 a 5. Seis inversões de ordem em nove comparações.
- **Mecanismo**, pelos registros de trajetória: do harness mínimo ao melhorado, o ganho veio de reduzir ruído de controle (saída malformada, orçamento de passos esgotado), não de conhecimento novo; do melhorado ao completo, de **verificação e de evitar regressão**.

## O que propõem

- **Cartão do harness**, em sete camadas: execução (ambiente, isolamento, orçamentos), ferramentas (lista, esquemas, contrato de erro), contexto (teto, compressão, busca, memória), agendamento (laço, novas tentativas, **escalada**), observabilidade (registros, rastros, pontos de checagem), verificação (validação, autoconferência, detecção de anomalia) e governança (permissões, limites de efeito colateral, **aprovação humana**). É lista de visibilidade, não padrão obrigatório.
- **Protocolo de decomposição da variância:** grade mínima de 2 × 2 modelo por harness, com tudo o mais fixo; reportar as duas variações, a razão, as inversões de ordem e a estatística (com o aviso de que ela infla em grades pequenas).
- **Métricas de trajetória** a reportar: taxa de recuperação, retenção do contexto, atraso de controle.

## Objeções que respondem

Modelos melhores dissolveriam o problema (não: o ecossistema de harness cresceu com os modelos); padronizar basta (em parte: é um dos dois regimes válidos, mas embute escolhas); a interação é pequena (não, pelas inversões); o harness faz parte do agente (concordam para o uso; para comparar modelos, é preciso declarar).

## Limites

A razão de 7,8 vem de 100 tarefas, duas rodadas e grade de 3 × 3; "capacidade parecida" é definida informalmente; a evidência dos placares é observacional; o teste de estresse proposto não foi rodado; uma só distribuição de tarefas.

---
