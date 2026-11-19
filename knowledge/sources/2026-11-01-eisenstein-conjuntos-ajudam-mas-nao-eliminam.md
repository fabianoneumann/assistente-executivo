---
titulo: "Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking"
tipo: paper
autor: "Jacob Eisenstein, Chirag Nagpal, Alekh Agarwal, Ahmad Beirami, Alex D'Amour, DJ Dvijotham, Adam Fisch, Katherine Heller, Stephen Pfohl, Deepak Ramachandran, Peter Shaw, Jonathan Berant"
url: "https://arxiv.org/abs/2312.09244"
publicado_em: 2023-12-14
capturado_em: 2026-11-01
licenca: "Licença não exclusiva de distribuição do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/, indicada na página do arXiv); sem licença aberta; entra só a ficha."
areas: [agent-engineering]
tags: [reward-model, ensembles, reward-hacking, overoptimization, underspecification, correlated-errors, pretraining-diversity, distribution-shift, best-of-n, rlhf, goodhart]
---

Ficha de estudo, em palavras próprias; sem texto integral. arXiv: v1 em 14/12/2023, v2 em 21/12/2023 e v3 (lida) em 16/08/2024; publicado na Conference on Language Modeling (COLM) de 2024. Google DeepMind e Google Research. Os 15 checkpoints pré-treinados estão em github.com/google-deepmind/reward-ensembles. O texto foi extraído do PDF da v3 com `pdftotext`, com as seções 1 a 6; as figuras não foram lidas como imagem e os apêndices numéricos (tabelas A e B) não foram conferidos um a um. Lida para a rodada investigativa (o juiz das peças), tema detecção.

**Por que importa ao lado do Coste:** o Coste ([[2026-11-01-coste-conjuntos-contra-superotimizacao]]) usa rótulos sintéticos e conjuntos que só diferem na semente do ajuste fino, e conclui que o conjunto praticamente elimina a superotimização; este usa preferências **humanas**, compara conjuntos que diferem já no **pré-treino**, e conclui que o conjunto atenua, mas não elimina, porque há erros que todos os membros compartilham. Os próprios autores se posicionam assim em relação ao Coste.

## O resumo

Modelos de recompensa criam incentivo para o modelo de linguagem explorar os erros deles (*reward hacking*). Um remédio natural é um conjunto de modelos de recompensa, agregando as notas. Os autores testam conjuntos no treino (RLHF) e na inferência (reordenar a melhor de N) e mostram: (1) modelos de recompensa são **subespecificados**: os que acertam igual dentro da distribuição de treino dão notas muito diferentes fora dela, que é onde o alinhamento leva as saídas; (2) isso gera superotimização: alinhar a um modelo não melhora a nota dada por outro treinado nos mesmos dados; (3) conjuntos atenuam o problema, e os que variam a semente do pré-treino generalizam melhor que os que variam só a do ajuste fino, ambos melhores que um modelo só; (4) mesmo os conjuntos de pré-treino não eliminam o *reward hacking*, porque em vários casos **todos os membros erram do mesmo jeito**.

## Montagem

- Três tarefas: utilidade em diálogo (HELPFULNESS, preferências de Bai et al., 2022), qualidade de resumo (TL;DR, Stiennon et al., 2020) e resumo fiel ao texto (XSUM/NLI, Roit et al., 2023).
- Modelos de recompensa: cinco T5 pré-treinados do zero com sementes diferentes (que mudam a inicialização e a amostra de dados vista no pré-treino), em três escalas (base 220M, large 770M, XL 3B), cada um ajustado com sementes diferentes: 25 modelos por escala e tarefa.
- Conjuntos de cinco membros: **de pré-treino** (cada membro de um pré-treino) e **de ajuste fino** (mesmo pré-treino, sementes de ajuste diferentes). Agregações: média, mediana, média menos desvio-padrão, e mínimo (pior que as outras no geral).
- Avaliação: um T5-XXL treinado nos mesmos dados (que pode ter erros correlacionados com os menores) e, por isso, também o PaLM-2-Large com instrução, que não viu os dados de preferência, julgando nas duas ordens com oito amostras cada e maioria.

## Resultados

- **Subespecificação:** os 25 modelos têm acerto quase igual dentro da distribuição (desvio-padrão baixo), mas, na melhor de N, os modelos que **não** compartilham o pré-treino com o que escolheu dão notas bem piores à escolhida, e os que compartilham a superestimam; a diferença não some com a escala. Dois modelos de pré-treinos diferentes escolhem uma melhor de 16 diferente em mais da metade dos casos. Durante o RLHF, a correlação de postos entre os modelos cai, sobretudo com pouca regularização e entre pré-treinos diferentes.
- **Conjuntos:** os de pré-treino melhoram consistentemente sobre o modelo único na melhor de N e no RLHF; os de ajuste fino ajudam em alguns casos e empatam em outros. Exemplo (TL;DR, escala XL, média): vitória sobre a política de partida de 90% com o conjunto de pré-treino, 87,3% com o de ajuste fino e 85,3% na média dos modelos únicos. As diferenças entre agregadores são pequenas, com a média quase sempre no topo ou perto.
- **Hacking explícito no RLHF:** a nota do avaliador grande cai enquanto o objetivo do RLHF sobe, mais nos modelos únicos, muitas vezes nos conjuntos de ajuste fino e raramente nos de pré-treino. Com o PaLM-2 como juiz, aparece **mais** hacking no RLHF do que com o T5-XXL: um avaliador ajustado nos mesmos dados de preferência superestima o desempenho.
- **XSUM/NLI:** os conjuntos quase não ajudam; a conjectura é que, otimizando fidelidade, todos os modelos acham a mesma estratégia simples de nota alta (resumos curtos).

## Onde o conjunto falha (seção 5)

Cinco mudanças qualitativas que o alinhamento produz, que o conjunto não impede porque **todos os membros concordam** que elas melhoram a saída:

- **HELPFULNESS:** respostas em formato de lista sobem para cerca de 50% das saídas, em três membros e no conjunto; nos dados de preferência, cerca de 8% (preferidas e rejeitadas).
- **TL;DR:** resumos com o dobro do tamanho e mais cópia do texto original (a maior subsequência comum dobra), longe do que os dados de preferência premiavam.
- **XSUM/NLI:** resumos mais curtos e menos específicos, com menos números.
- Explicação dos autores: conjuntos estimam bem a incerteza perto da fronteira de decisão e a subestimam longe da distribuição de treino; a política leva as saídas justamente para regiões em que todos os modelos extrapolam do mesmo jeito. O mesmo valeria para outras estimativas de incerteza que não medem distância (Monte Carlo Dropout, redes neurais epistêmicas).

## O que os autores concluem

A diversidade do conjunto é crucial, e os de pré-treino são mais diversos que os de ajuste fino; mas mesmo eles não são diversos o bastante: em muitos hacks todos os membros concordam, e o conjunto fica tão vulnerável quanto cada um. Conjuntos atenuam, não eliminam. Pedem métodos de incerteza que representem explicitamente o afastamento das saídas em relação aos dados de preferência.

## Tudo o mais que ensina

- Bai et al. (2022) já tinham treinado dois modelos de recompensa em metades disjuntas dos dados, um para guiar e outro para medir; como os dois partiam do mesmo pré-treino, isso pode ter subestimado o hacking.
- Gleave e Irving (2022) relataram resultado negativo com conjuntos e atribuíram ao pré-treino compartilhado; este trabalho confirma a hipótese.
- Trabalhos posteriores que tornam conjuntos baratos (adaptação de baixo posto, média de pesos como o WARM) só fazem conjuntos de ajuste fino, o tipo menos diverso.
- Na melhor de N, aumentar N sobe a nota e o afastamento da política de partida; no RLHF, o compromisso entre KL e recompensa se obtém treinando várias vezes com pesos de KL diferentes até convergir, e não lendo a curva de um treino só como fez o Coste (um ponto da curva pode estar suboptimizado).
- O juiz por modelo com instrução (PaLM-2) é usado nas duas ordens e com maioria de oito amostras por ordem para controlar o viés de posição.
