---
titulo: "Training AI Co-Scientists Using Rubric Rewards"
tipo: paper
autor: "Shashwat Goel, Rishi Hazra, Dulhan Jayalath, Timon Willi, Parag Jain, William F. Shen, Ilias Leontiadis, Francesco Barbieri, Yoram Bachrach, Jonas Geiping, Chenxi Whitehouse"
url: "https://arxiv.org/abs/2512.23707"
publicado_em: 2025-12-29
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [rubric-rewards, llm-as-judge, human-agreement, inter-judge-agreement, kappa-prevalence, reward-overoptimization]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 29/12/2025, a única versão (lida). Publicado no **ICML 2026** (a página do arXiv não diz o venue; confirmado em [icml.cc/virtual/2026/poster/62954](https://icml.cc/virtual/2026/poster/62954) e nos anais, [PMLR vol. 306](https://proceedings.mlr.press/v306/goel26b.html)). Lido em 2026-10-29, na pesquisa da calibração por dimensão do portão; o que interessa aqui é sobretudo o apêndice B.6, sobre concordância dos juízes.

## A ideia

Treinar um modelo a escrever **planos de pesquisa** sem executar experimentos. De artigos científicos, um modelo extrai o objetivo de pesquisa e uma **rubrica específica daquele objetivo** (os requisitos que um plano válido precisa cumprir). O modelo é treinado por reforço, e a nota vem de uma cópia congelada do próprio modelo inicial, que vê a rubrica como informação privilegiada: conferir fica mais fácil que gerar.

## Como o avaliador dá a nota

Para cada item da rubrica, o avaliador aponta quais das sete diretrizes gerais o trecho do plano viola (vago, falha não vista, justificativa fraca, custo desnecessário, problema ético, inconsistência, critério não tratado). O item conta como cumprido só se a lista de violações vier vazia; a nota é a fração de itens cumpridos. Nos testes iniciais, apontar violações deu notas mais ancoradas que pedir sim ou não ou uma nota direta; nas ablações, tirar a rubrica específica ou tirar a checagem das diretrizes piora muito.

## Resultados principais

- **Especialistas humanos** (25, de pós-graduandos a profissionais seniores; 100 objetivos de ML, três especialistas por objetivo, 225 horas): preferem o plano do modelo treinado em 70,0% das anotações (p < 0,0001); nota média de 7,89 contra 7,31 em 10. O plano treinado foi julgado melhor em cumprir requisitos, solidez e resultado previsto, mas um pouco menos claro de executar e mais complexo.
- **Qualidade das rubricas extraídas:** 4,3 de 5; 84% dos itens julgados pelo menos necessários.
- **Sobreotimização:** depois de cerca de 120 passos, a nota do próprio avaliador continua subindo, mas a de um avaliador mais forte guardado à parte (Claude-4-Sonnet) se afasta. Os planos passam a ganhar detalhe supérfluo que engana o avaliador fraco; ele também premiava planos mais caros, que o avaliador forte penalizava. Escolheram o ponto do passo 100 por esse avaliador externo.
- Em medicina e em preprints novos, avaliado por um júri de três modelos de ponta: ganho relativo de 12% a 22% sobre o modelo inicial.

## Concordância dos juízes com os humanos (apêndice B.6)

- **Preferência geral, cada juiz contra a maioria humana:** GPT-5-Thinking 75,3% (kappa 0,44); Gemini-2.5-Pro 73,9% (0,27); Claude-4-Sonnet 50,0% (0,08); o júri por maioria, 69,2% (**kappa 0,297**, acima do acaso com p < 0,01). Os autores: no item a item, a nota automática é ruidosa; no agregado, tem sinal.
- **Por critério:** pela porcentagem, o critério mais objetivo concorda mais (cumprir requisitos, 78% a 84%) que o subjetivo (clareza de execução, 50% a 66%); pelo kappa do GPT-5, os dois empatam (0,326 e 0,325). O Claude-4-Sonnet tem kappa negativo em alguns critérios.
- **Item da rubrica cumprido ou não, assimetria:** quando os humanos dizem que o item foi violado, os juízes concordam de 89% a 98%; quando dizem que foi cumprido, só de 22% a 49%. Os juízes são **sistematicamente mais duros** que os especialistas, que marcavam como cumprido o item tratado mesmo de forma imperfeita.

## Concordância entre juízes

- No cumprimento dos itens, kappa de 0,37 a 0,42 entre pares de juízes; mais alto em diretriz objetiva ("trata todos os critérios", cerca de 0,57 a 0,63), mais baixo nas subjetivas (justificativa, falhas não vistas: abaixo de 0,35).
- **O kappa e a prevalência:** em "sem problema ético", a concordância passa de 90% e o kappa fica abaixo de 0,25, porque quase todos os planos são eticamente corretos. O mesmo nas preferências: como o modelo treinado ganha a maioria das comparações, a concordância bruta vai de 40% a 87% e o kappa fica baixo.

## Limites declarados

Estudo humano em um domínio só (ML) e só no fim; os demais resultados dependem do júri de modelos; comparar planos é subjetivo item a item; o avaliador próprio é fraco em custo e esforço, o que deixou os planos mais complicados.

---
