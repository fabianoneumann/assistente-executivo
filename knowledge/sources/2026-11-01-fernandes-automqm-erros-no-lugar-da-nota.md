---
titulo: "The Devil is in the Errors: Leveraging Large Language Models for Fine-grained Machine Translation Evaluation"
tipo: paper
autor: "Patrick Fernandes, Daniel Deutsch, Mara Finkelstein, Parker Riley, André F. T. Martins, Graham Neubig, Ankush Garg, Jonathan H. Clark, Markus Freitag, Orhan Firat"
url: "https://aclanthology.org/2023.wmt-1.100/"
publicado_em: 2023-12-06
capturado_em: 2026-11-01
licenca: "CC BY 4.0 (rodapé do ACL Anthology: material publicado em 2016 ou depois, licença Creative Commons Attribution 4.0, com link para creativecommons.org/licenses/by/4.0/; o preprint no arXiv, 2308.07286, tem só a licença padrão não exclusiva, e por isso o integral lido vem da versão do Anthology)"
areas: [agent-engineering]
tags: [mqm, automqm, llm-as-judge, error-annotation, error-span-detection, score-prediction, score-clumping, in-context-anchoring, span-precision, major-error-recall, over-prediction, machine-translation]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Publicado nos anais da Eighth Conference on Machine Translation (WMT 2023), p. 1066 a 1083, 6 e 7 de dezembro de 2023, DOI 10.18653/v1/2023.wmt-1.100; preprint arXiv 2308.07286 (v1 em 14/08/2023). Lida a versão do Anthology; a numeração de tabelas e figuras muda em relação ao preprint (a tabela de trechos é a 5 no Anthology e a 6 no arXiv), e os números conferidos batem nas duas. Autores do Google, da Carnegie Mellon, do Instituto Superior Técnico, do Instituto de Telecomunicações e da Unbabel. Texto extraído do PDF com `pdftotext`; as tabelas saem embaralhadas e os números citados foram lidos nas linhas delas e conferidos contra o texto. Lido para a rodada investigativa.

**Atenção:** os modelos são PaLM e PaLM-2 de 2023; o que interessa aqui é o padrão (nota direta contra lista de erros, e a qualidade da lista), não os números absolutos.

## 1. A pergunta

Modelos de linguagem já ordenavam bem sistemas de tradução dando uma nota direta (Kocmi e Federmann, GEMBA), mas a nota não diz o que está errado. Dá para um modelo produzir, como os anotadores do MQM, a lista dos erros com trecho, categoria e gravidade, e tirar a nota dessa lista? E quão parecida com a dos humanos fica essa lista?

## 2. Primeira parte: o modelo dando nota direta

- **Prompt:** o GEMBA-SQM, que pede uma nota de 0 a 100. Modelos: PaLM (540 bilhões de parâmetros), PaLM-2 BISON e UNICORN (o maior) e uma versão com instruções. Dados: WMT22 (inglês para alemão, chinês para inglês, inglês para russo, com MQM de especialistas como gabarito) e quatro pares de poucos recursos (com nota direta de leigos como gabarito).
- **Bom no agregado, fraco por segmento.** Sem exemplo nenhum, quase todos os modelos ordenam sistemas melhor que as métricas treinadas, mas por segmento nenhum supera com consistência as métricas treinadas.
- **A nota direta se amontoa em poucos valores.** Mesmo pedindo de 0 a 100, os modelos quase sempre devolvem um de poucos números (0, 50, 90, 95); o artigo diz que Kocmi e Federmann viram o mesmo com os modelos GPT e atribui isso ao pré-treino.
- **Exemplos no prompt ancoram a nota.** Incluir exemplos com nota quase nunca melhorou o desempenho, com sorteio uniforme ou estratificado por faixa. A distribuição das notas segue as notas dos exemplos: um modelo que nunca dava 79 passa a dar 79 em massa quando um exemplo com 79 entra no prompt. Os autores leem que o modelo copia as notas dos exemplos em vez de generalizar a tarefa.
- **Ajuste fino com notas humanas** resolve a fraqueza por segmento, sobretudo nos modelos menores e sem referência: um BISON ajustado chega ao estado da arte por segmento.
- **Poucos recursos:** sem exemplos, cerca de 90% de acerto na ordem de sistemas, mas abaixo das métricas treinadas.

## 3. Segunda parte: AutoMQM, a lista de erros

- **Prompt (Figura 2):** "identifique os erros maiores e menores desta tradução"; maiores são erros de tradução ou de gramática de verdade, menores são imperfeições e opiniões subjetivas. A saída é uma lista "trecho - gravidade/categoria". **O modelo não dá nota**: a nota sai por algoritmo, somando as penalidades (cerca de 5 por maior e 1 por menor).
- **Sem exemplos, não funciona:** a saída vem vazia de informação ou difícil de ler. Por isso só se testa com exemplos, sorteados de um banco de anotações MQM com critérios de rejeição que equilibram erros maiores e menores e variam as categorias. Só inglês para alemão e chinês para inglês, os pares com banco de exemplos.
- **Resultado na nota:** com o UNICORN, o AutoMQM supera a nota direta em todas as medidas, e a versão sem referência fica competitiva com a melhor métrica treinada até por segmento. Com o BISON, menor, as duas formas empatam: o ganho pede escala.
- **Resultado na distribuição:** as notas que saem do AutoMQM ficam muito mais perto da distribuição do MQM humano, com um conjunto muito maior de valores e nas mesmas faixas que os anotadores usam (Figura 8). É o contrário do amontoado da nota direta.

## 4. A qualidade da lista de erros (Tabela 5 do Anthology)

Três medidas por palavra: **precisão de trecho** (que fração das palavras marcadas pelo modelo os humanos também marcaram, qualquer gravidade), **revocação de maiores** (que fração das palavras dentro de erros maiores humanos o modelo marcou) e MCC (correlação de Matthews, a medida oficial da tarefa de estimativa de qualidade por palavra).

- **Precisão baixa:** de 0,060 a 0,193 conforme modelo, par e uso de referência. A maior parte do que o modelo marca não coincide com o que os humanos marcaram.
- **Revocação de maiores alta no inglês para alemão:** de 0,520 a 0,749; no chinês para inglês, de 0,252 a 0,488. O texto resume que os modelos acham "a maioria" dos erros maiores e "mais de 50%" das palavras de erros maiores; isso vale para o inglês para alemão.
- **O modelo marca demais e largo:** os trechos do UNICORN têm em média 5 palavras, contra 2 dos humanos. A referência treinada por palavra (COMET-WL) é mais precisa (0,267 e 0,364), mas deixa passar muito mais erros maiores (0,250 e 0,178); o MCC fica parecido.

## 5. Conclusão e caminhos dos autores

Pedir nota direta já dá o estado da arte na ordenação de sistemas, mas fica atrás das métricas treinadas por segmento; o AutoMQM melhora o desempenho sem ajuste fino e dá trechos interpretáveis que se alinham aos humanos; ajustar o modelo com dados de erros finos é a direção seguinte; e a técnica pode servir a outras avaliações de texto gerado.

## 6. Tudo o mais que ensina

- **Não pedir a nota ao modelo:** a conta fica com o código, a partir da lista; o modelo só acha e classifica.
- **Exemplos de anotação equilibrados** (maiores e menores, categorias variadas) são condição para a lista sair útil; sem eles, a saída degenera.
- **Interpretabilidade vale mais quando a nota erra:** com a lista, dá para ver por que o avaliador errou e evitar o erro de novo; com a nota, não.
- **A mesma família de modelo cresce em qualidade de lista com a escala:** o modelo maior marca melhor os trechos.
- **A precisão e a revocação dos trechos medem coisas diferentes:** um avaliador pode achar quase todos os erros graves e ainda assim gerar muitos alarmes falsos, e o MCC sozinho esconde essa troca.
