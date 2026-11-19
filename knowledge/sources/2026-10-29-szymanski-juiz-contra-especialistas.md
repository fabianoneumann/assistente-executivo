---
titulo: "Limitations of the LLM-as-a-Judge Approach for Evaluating LLM Outputs in Expert Knowledge Tasks"
tipo: paper
autor: "Annalisa Szymanski, Noah Ziems, Heather A. Eicher-Miller, Toby Jia-Jun Li, Meng Jiang, Ronald A. Metoyer"
url: "https://arxiv.org/abs/2410.20266"
publicado_em: 2024-10-26
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, subject-matter-experts, expert-vs-lay-annotators, per-dimension-calibration, accuracy-evaluation, personas]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 26/10/2024, a única versão (lida). A página do arXiv não diz o venue e o texto traz uma referência da ACM com DOI provisório; não encontrei a publicação final, então fica como preprint. Lido em 2026-10-29, na pesquisa da calibração por dimensão do portão.

## A pergunta

O juiz LLM, que concorda bem com humanos em tarefas gerais de seguir instrução, também concorda com **especialistas** quando a tarefa pede conhecimento de domínio? Dois domínios: dietética (10 nutricionistas registradas, 9,6 anos de experiência em média) e saúde mental (10 psicólogos clínicos, 15,2 anos). 25 instruções do domínio, cada uma respondida pelo GPT-4o e pelo GPT-3.5; o juiz é o GPT-4, pelo AlpacaEval, comparando as duas respostas em pares.

## Como mediram

- Uma pergunta de preferência geral ("qual é melhor no todo?") e perguntas por aspecto, agrupadas em clareza, precisão, padrões profissionais, contexto educativo e personalização.
- Duas versões do juiz: o modelo geral e o modelo com persona de especialista no prompt.
- Especialistas e juiz explicam a escolha; as explicações passaram por análise qualitativa.
- Estudo de seguimento com 10 leigos por domínio (Prolific), só na preferência geral.

## Resultados

- **Preferência geral, juiz contra especialistas:** 64% (dietética) e 60% (saúde mental) com o modelo geral; 68% e 64% com persona de especialista (os números do resumo). **Especialistas entre si:** 75% e 72% (73% no total).
- **Por aspecto, a concordância oscila muito.** Dietética, modelo geral: clareza 55%, precisão 56%, padrões profissionais 80%, contexto educativo 55%, personalização 56%. Saúde mental: precisão 80%, clareza 70% (cai para 40% com persona de especialista). A persona ajuda em alguns aspectos e piora em outros.
- **Leigos concordam mais com o juiz:** 80% nos dois domínios com o modelo geral, 76% com a persona (diferença significativa contra os especialistas, p < 0,0001). Hipótese dos autores: os modelos são ajustados com preferência de leigos.
- **O que o juiz deixou passar:** os especialistas marcaram respostas imprecisas e potencialmente danosas (conceitos de dieta desatualizados, alergênicos tratados errado, diagnóstico sugerido a partir de sintomas vagos, terapia sem evidência). O juiz **não sinalizou essas imprecisões**; tendia a repetir detalhes da resposta e a premiar quem seguia a instrução. Também lia "clareza" como mais detalhe, enquanto os especialistas queriam linguagem simples e menos informação.
- As explicações dos especialistas trazem conhecimento novo; as do juiz repetem a instrução e a resposta.

## O que recomendam

- Especialista no processo para tarefas de domínio; o juiz LLM serve para triagem em escala (eliminar os piores candidatos cedo) e o especialista avalia o que sobra.
- Avaliação por domínio e por aspecto, para saber onde o especialista é mais necessário.
- Persona ajustada ao domínio, sabendo que ela não ajuda em todos os aspectos.

## Limites declarados

- Dois domínios só, pelo custo de anotação especializada; 25 instruções.
- O juiz não foi ajustado com as escolhas dos especialistas.
- Não investiga a relação com os dados de treino.

---
