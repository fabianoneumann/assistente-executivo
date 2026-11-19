---
titulo: "GEMBA-MQM: Detecting Translation Quality Error Spans with GPT-4"
tipo: paper
autor: "Tom Kocmi, Christian Federmann (Microsoft)"
url: "https://arxiv.org/abs/2310.13988"
publicado_em: 2023-10-21
capturado_em: 2026-11-01
licenca: "CC BY 4.0 (indicada na página do arXiv, com link para http://creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [mqm, llm-as-judge, error-annotation, error-span-detection, severity-weighting, reference-free-evaluation, few-shot-prompting, system-level-ranking, category-misuse, proprietary-model-caveat, machine-translation]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv 2310.13988, v1 em 21/10/2023, a única versão; comentário do arXiv: "Accepted to WMT 2023" (artigo curto de submissão à tarefa de métricas). Dois autores da Microsoft. Texto extraído do PDF com `pdftotext`; as tabelas saem com as colunas soltas e foram lidas linha a linha. O prompt completo e os três exemplos fixos estão no apêndice do artigo, na url do frontmatter. Lido para a rodada investigativa.

**Atenção à força da evidência:** artigo curto, com resultados que os próprios autores chamam de preliminares; o modelo é proprietário (GPT-4 e GPT-3.5-Turbo de 2023), sem garantia de que o mesmo modelo continue servido, e os dados de teste públicos podem ter entrado no treino dele. Medido sobretudo na **ordenação de sistemas** (qual sistema de tradução é melhor no agregado), não na qualidade de cada lista de erros.

## 1. O que é

Um avaliador que pede ao GPT-4 para **marcar os erros de uma tradução no formato MQM** (trecho, categoria e gravidade), sem tradução de referência, e calcula a nota pelos pesos do MQM. É o sucessor do GEMBA-DA, dos mesmos autores, que pedia só uma nota direta por segmento.

- **Prompt (Figura 1):** sistema: "você anota a qualidade de tradução automática; identifique os erros e avalie a qualidade". Usuário: a fonte e a tradução entre crases triplas, e a instrução de identificar e classificar os erros nas categorias precisão (adição, má tradução, omissão, texto não traduzido), fluência (codificação, gramática, inconsistência, pontuação, registro, ortografia), estilo (construção estranha), terminologia (inadequada ao contexto, uso inconsistente), não tradução, outro, ou "sem erro". Cada erro tem uma de três gravidades: **crítico** (impede a compreensão), **maior** (atrapalha o fluxo, mas o sentido ainda se entende) e **menor** (tecnicamente erro, sem atrapalhar fluxo nem compreensão).
- **Três exemplos fixos** (de inglês para alemão, inglês para tcheco e chinês para inglês), os mesmos para qualquer par de línguas, para não depender de preparar exemplos por língua. A escolha não foi para ganhar desempenho (exemplos específicos do domínio e da língua costumam ajudar), e sim para poder usar o método em qualquer par.
- **Nota:** soma dos erros com os pesos do MQM; o texto cita, para o método vizinho EAPrompt, 25 para crítico, 5 para maior e 1 para menor.

## 2. Resultados

- **No conjunto cego da WMT 2023 (MQM23), primeiro lugar na ordenação de sistemas:** acurácia por pares de sistemas de 96,5%, acima de todas as outras métricas, inclusive as que usam tradução de referência (a seguinte, XCOMET-Ensemble, 95,2%). Na meta-avaliação oficial daquele ano, que mistura ordenação de sistemas, correlação de Pearson e duas medidas por segmento, ficou no **terceiro grupo** (0,802, contra 0,825 do primeiro): bom para ordenar sistemas, menos destacado por segmento.
- **No conjunto MQM22,** todas as variantes GEMBA superam as métricas clássicas na ordenação de sistemas (de 86,5% a 89,8%, contra 70,8% do BLEU e 83,9% do COMET-22).
- **No conjunto interno da Microsoft** (15 línguas, notas humanas por avaliação direta), o GEMBA-MQM com GPT-3.5-Turbo perde por pouco para o COMETKiwi-22 (78,4% contra 79,9%): sinal de limite fora dos dados públicos.

## 3. A categoria que o modelo usou mal

A primeira versão tinha a categoria **convenção local** (formato de moeda, data, nome, telefone, hora). No conjunto interno, o modelo marcou **32% de todos os erros** como convenção local, inclusive em traduções corretas: por exemplo, apontou "euros" num texto tcheco como erro de moeda, talvez porque o euro não circula na República Tcheca. Os autores **tiraram a categoria do prompt** em vez de explicá-la melhor; cerca de metade desses erros migrou para outras categorias e a outra metade deixou de ser marcada. A variante com a categoria era melhor no MQM22 e pior no conjunto interno de 15 línguas, e os autores admitem que isso pede mais investigação. Distribuição final no conjunto interno (Turbo, sem a categoria local): 51% precisão, 33% fluência, 14% terminologia, 2% estilo.

## 4. A crítica dos autores à própria meta-avaliação

Questionam o uso de Pearson na ordenação de sistemas: com poucos sistemas (12 no MQM23), o coeficiente é sensível ao tamanho da amostra e a valores extremos, e mede relação linear com notas MQM que não são lineares (pesos de 0,1, 1, 5 e 25).

## 5. Cautela com modelos "caixa-preta" (limites declarados)

Os autores recomendam cuidado ao usar o método em trabalho acadêmico para provar melhora: não se sabe com que dados o GPT-4 foi treinado (todo conjunto público pode ter sido visto), o modelo pode mudar ou sair do ar, e o desempenho do GPT-4 variou ao longo de 2023. Só línguas com muito recurso foram testadas. Sugerem repetir com modelos de pesos abertos.

## 6. Tudo o mais que ensina

- **A lista de categorias no prompt muda a distribuição dos erros:** uma categoria mal entendida vira um ralo que atrai achados falsos; tirar a categoria redistribuiu metade e apagou metade.
- **O avaliador por erros brilha no agregado:** ordenar sistemas pela média de muitos segmentos tolera erros de anotação que, segmento a segmento, pesam.
- **Exemplos fixos e gerais** trocam um pouco de desempenho por portabilidade.
- **"Sem erro" é uma resposta prevista** no prompt, ao lado das categorias.
