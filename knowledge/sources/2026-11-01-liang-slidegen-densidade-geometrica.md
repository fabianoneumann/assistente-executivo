---
titulo: "SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation"
tipo: paper
autor: "Xin Liang, Zhilin Zhang, Xiang Zhang, Haoran Su, Yiwei Xu, Siqi Sun, Chenyu You"
url: "https://arxiv.org/abs/2512.04529"
publicado_em: 2025-12-04
capturado_em: 2026-11-01
licenca: "CC BY 4.0 (indicada na página do arXiv, link creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering, content-design]
tags: [slide-generation, layout-metrics, white-space, visual-density, human-alignment, bounding-boxes, multi-agent, vlm-as-judge, calibration, design-metrics]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 04/12/2025; lida a v3 de 22/08/2026, cujo cabeçalho indica os anais do ACM Multimedia 2026 (MM '26, Rio de Janeiro, 10 a 14 de novembro de 2026). Autores de Stony Brook, NYU, UBC, UCLA e Fudan. Texto extraído do PDF da v3 com `pdftotext`. Lido para a rodada investigativa por um motivo só: a métrica de densidade de layout (GAD), calculada nas caixas dos elementos e calibrada contra notas de pessoas. O resto do artigo (o sistema de agentes que faz slides a partir de artigos científicos) vai resumido.

## 1. O sistema, em resumo

Seis agentes de visão e linguagem em estágios: planejar a narrativa (Outliner), casar figuras e equações com as afirmações (Mapper, Formulizer), compor o layout escolhendo entre modelos de slots fixos de uma biblioteca (Arranger), refinar o deck (Refiner: junta slides, extrai a cor tema das figuras, comprime texto que estoura o espaço, com corpo mínimo de 14 pt) e escrever as notas do apresentador (Speaker). A saída é PPTX editável. A biblioteca de modelos com slots fixos "evita sobreposição por construção".

## 2. A métrica de densidade (GAD, seção 4.2 e apêndice A.4)

- **Para que serve:** medir quão bem um slide equilibra espaço ocupado e vazio, o "nem amontoado nem vazio".
- **Dois termos por slide, calculados nas caixas dos elementos lidas do PPTX:**
  - **Ocupação:** a fração do canvas coberta pela união das regiões de conteúdo, penalizada pelo desvio em relação a uma densidade-alvo.
  - **Fragmentação:** uma função em forma de parábola invertida sobre o número efetivo de elementos (ignorando os menores que um limiar), que atinge o máximo num número ótimo de blocos. O porquê, nas palavras dos autores: slide monolítico parece bloco e sem hierarquia; partição demais vira ruído e leitura aos saltos.
- **No deck:** a média dos dois termos ponderados, com pesos que somam um; o peso ótimo da ocupação fica perto de 0,6 e é estável entre 0,5 e 0,7. Os parâmetros finais relatados: 4 e 6,3 para os dois hiperparâmetros da busca em grade (número ótimo de blocos e escala), escolhidos no pico da correlação de Spearman.

## 3. A calibração contra pessoas

- **Dados:** 53 decks, 40 para ajustar e 13 para testar; de cada página, um JSON com tamanho da página e posição, tamanho e texto de cada caixa.
- **Pessoas:** 40 avaliadores dão nota de 1 a 5 (com uma casa decimal) a cada slide, com âncoras explícitas: 1 = extremamente amontoado ou extremamente vazio; 3 = aceitável mas não ideal; 5 = muito limpo, com densidade de informação adequada. As notas são normalizadas por avaliador (escore z), para tirar a diferença de rigor entre pessoas.
- **Ajuste:** os pesos e a escala são ajustados por mínimos quadrados nos decks de treino, com validação cruzada deixando um deck de fora; cada deck de teste fica fora do ajuste.
- **Resultado (Figura 4):** nas páginas dos 13 decks de teste (cerca de 750), Spearman de 0,820, Pearson de 0,811 e erro quadrático médio de 0,580 contra a nota humana.

## 4. As outras avaliações

- **Juiz de modelo:** GPT-4o dá nota de 1 a 5 em conteúdo, design e coerência, com justificativa (critérios do PPTEval). Para afastar o viés de o GPT-4o julgar o que ele mesmo gerou, os autores rejulgaram com Gemini-2.5-Flash: Spearman de 0,90 entre os dois juízes no nível do método; o Gemini dá notas absolutas mais baixas (0,26 em média) e a ordem se mantém.
- **Comunicação:** 100 questões por artigo (50 literais, 50 interpretativas), respondidas por seis modelos leitores só com o deck; cinco doutorandos responderam em 5 artigos e a ordem dos métodos se manteve.
- **Estudo de preferência:** 93,3% dos participantes preferiram os slides do SlideGen.

## 5. Limites (do artigo e da captura)

- A nota humana usada na calibração é **só de densidade** (amontoado contra vazio), com âncoras dadas; a GAD não mede alinhamento, equilíbrio, posição nem hierarquia.
- Slides acadêmicos 16:9 gerados de artigos científicos; a densidade-alvo e o número ótimo de blocos foram ajustados nesse gênero e não valem sem recalibração para outro formato.
- A métrica foi calibrada e testada pelos mesmos autores que a propõem e que a usam para mostrar a vantagem do próprio sistema na tabela principal.

## 6. Tudo o mais que ensina

- **Ablação:** tirar o Arranger (composição explícita) causa a maior queda de densidade; tirar o Outliner, a maior queda nas respostas; tirar o Mapper derruba 8,4 pontos nas questões interpretativas (casar figura e afirmação ajuda a entender).
- **Diagnóstico por blocos (Figura 9):** os métodos anteriores convergem para o mesmo layout vertical; representar cada slide como blocos coloridos mostra a monotonia de composição entre slides.
- **Cor tema (Figura 10):** extraída das figuras do artigo, depois escurecida e saturada até dar contraste com texto branco; os casos de falha (apagada demais, berrante demais) estão desenhados.
