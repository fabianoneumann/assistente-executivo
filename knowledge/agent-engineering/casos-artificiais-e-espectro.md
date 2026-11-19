# Casos artificiais e espectro: por que superestimam e para que ainda servem

Por que testar um avaliador em casos escritos à mão (extremos, sintéticos, com controles separados) tende a superestimar o acerto, e para que esses casos ainda servem. O corte e o reuso do teste estão em [[ponto-de-corte-reuso-do-teste-e-desvio]]; a validade de conteúdo, em [[validade-de-conteudo-e-rubricas]].

Convenção: "leitura nossa" liga a fonte a um ambiente de agentes e não está na fonte. "Não verificado" é afirmação de resposta de buscador, sem primária aberta.

## A resposta curta

- **Testar em casos extremos, com controles separados, tende a superestimar.** A direção é consistente em poucos estudos, e a estimativa é fraca (leitura nossa).
- **Em texto, a queda aparece, em modelo treinado no próprio sintético:** de 91 a 98 em teste sintético para 50 a 77 em erros reais (Goyal e Durrett). Um juiz que não treina no sintético não tem esse ajuste, e parte da queda pode vir dele (leitura nossa).
- **Maheshwari e Rahmani convergem, em leitura nossa:** o número absoluto não se sustenta, e a ordem entre sistemas se sustenta melhor, sem ser firme. Em entidades, Maheshwari mostra o inverso.
- **Falta a medida do caso mais comum num ambiente de agentes:** juiz zero-shot, com gabarito de um dono, em texto curto. O vizinho mais próximo é Do e outros (IBM).
- **Três usos, em leitura nossa:** começar e refinar serve (opinião de Husain e Shankar; paridade medida em Do, com ressalva); conferir que o caso grave dispara serve (Rohlfs), com os itens lidos (Ballı); estimar acerto, não.

## 1. O número clássico e o mecanismo

- [[2026-11-06-lijmer-1999-vies-de-desenho-em-testes-diagnosticos]]: doentes com controle separado superestimaram o desempenho contra população clínica, RDOR (razão entre chances diagnósticas) de 3,0, IC 95% 2,0 a 4,5, em 184 estudos e 218 avaliações, num modelo com 9 características juntas. **Só 5 das 218 usavam caso-controle** (Tabela 2). O mecanismo que dão: os casos leves, difíceis, ficam de fora. Inclusão não consecutiva e coleta retrospectiva não mudaram a estimativa.
- [[2026-11-06-rutjes-2006-vies-e-variacao-em-acuracia]] (487 estudos em 31 meta-análises), com contraste mais estreito: casos graves com controles saudáveis, RDOR 4,9, IC 0,6 a 37,3, com só 5 estudos em 2 meta-análises, severa numa e bem menor na outra. Outro caso-controle, 37 estudos em 7 meta-análises, dá 1,1 (0,4 a 3,4). Rutjes usa efeitos aleatórios onde Lijmer usou fixos, o que explica intervalos mais largos. Aqui, inclusão não consecutiva dá 1,5 (1,0 a 2,1) e coleta retrospectiva, 1,6 (1,1 a 2,2). Caso grave é mais fácil de detectar; controle saudável gera menos falso positivo. Os dois usam RDOR de regressão, com contraste e estudos diferentes, então não se somam, e divergem sobre seleção e coleta (leitura nossa).
- Recognising Bias, Emerg Med J, 2019 (citação, https://pmc.ncbi.nlm.nih.gov/articles/PMC6738935/): largar os indeterminados e amostrar por conveniência têm o mesmo efeito. Na base, Kellerhuis: excluir o caso difícil superestima ([[gabarito-quando-o-responsavel-tem-duvida]]).
- **Não é sempre defeito:** Rutjes 2005 (resumo, só citação, https://doi.org/10.1373/clinchem.2005.048595): o efeito pode ajudar na investigação inicial de um teste novo, e, para a avaliação geral, o desenho "should closely mimic" o transversal. [[2026-11-06-usher-smith-2016-efeito-de-espectro]]: "Ideally", desenvolver e avaliar na população de uso.

## 2. Num modelo de IA

[[2026-11-06-mayo-2021-ecg-e-espectro]] (coorte de 258.607; teste do grupo extremo, 60.159; análise mista, 102.926; CC BY-NC, integral na `url` da ficha): o ECG que separa estenose aórtica grave de nenhuma deu 84% e 84% de sensibilidade e especificidade, AUC de 0,91, no próprio grupo extremo. Com o limiar aplicado ao espectro inteiro, 83% e 73%, AUC de 0,86. Caiu sobretudo a especificidade, e os autores ainda chamam o desempenho de robusto.

## 3. Texto: treinar e testar em sintético

[[2026-11-06-goyal-durrett-2021-erros-de-factualidade]] (NAACL 2021): "commonly-used training sets of simple synthetic errors do not reflect errors made on abstractive datasets like XSum". Os mesmos modelos, treinados em sintético:

| Onde foi testado | Nota |
|---|---|
| Sintético reservado (tabela 7) | 91,2 a 97,9 |
| Humano, CNN/DM (tabela 2) | 64,4 a 76,7 |
| Humano, XSum (tabela 3), com base de 50 | 50,9 a 54,2 |

É a comparação mais direta entre nota em sintético e em real, com modelo treinado no sintético: os modelos conseguem "fit the distribution of the synthetic domain", e um juiz que não treina não tem esse ajuste, então parte da queda pode vir dele (leitura nossa). O sintético que os autores dizem alinhar melhor (Gen-C) cai igual; nesse artigo, com duas gerações, a qualidade do sintético não explica a queda (leitura nossa).

**Na direção contrária:** o MiniCheck, treinado com sintético, empata com o GPT-4 em erros rotulados por pessoas. Richter e Wehrheim 2023 (resumo, só citação, https://conf.researchr.org/details/ase-2023/ase-2023-papers/86/How-to-Train-Your-Neural-Bug-Detector-Artificial-vs-Real-Bugs): detectores de bug treinados em artificiais rendem menos em reais. Goyal e Richter contra MiniCheck, não reconciliado.

## 4. Avaliar em sintético contra real: o que há de mais perto

Nenhum número se transfere (leitura nossa).

- [[2026-11-06-maheshwari-2024-sintetico-como-benchmark]] (empresa e universidade, no arXiv; CC BY-NC-ND, integral na `url` da ficha; 200 exemplos por conjunto; a ordem é entre seis LLMs): "a good predictor of relative performance but not a strong indicator of absolute performance". A diferença absoluta (MSPD) é média de quadrados e não tem sinal, e o artigo não publica os desempenhos de cada lado, então não mostra que o sintético superestima (leitura nossa). SNIPS, com 7 intenções, capta as duas coisas (MSPD 0,00, Spearman 0,94, linha da média), e os autores o tratam como exceção. ATIS, com 17: ordem fica (Spearman de 0,89 a 0,94), diferença não (MSPD de 0,05 a 0,08; de 0,03 a 0,13 por modelo, o que dá de 0,17 a 0,36 de distância típica pela raiz, conta nossa). Entidades, o inverso: MSPD de 0,00 a 0,02, e a ordem cai (até Spearman 0,20). Recomendam gerar com vários LLMs e tirar a média. Dizem que modelos menores favorecem um pouco mais os próprios dados, com exceção na família GPT; a ficha mostra que a Tabela II não fecha em Llama.
- [[2026-11-06-rahmani-2025-vies-em-dados-sinteticos]] (CC BY; recuperação de informação, uma coleção só): a nota sobe nas consultas sintéticas, sugerindo que são mais fáceis. A ordem se mantém em parte (Kendall de 0,82 a 0,92 em NDCG, de 0,73 a 0,86 em MAP), com viés a favor do sistema do mesmo modelo do gerador. Rótulos do GPT-4 no lugar de juízes humanos: notas sistematicamente mais altas (MAP β=0,069; NDCG β=0,207).
- [[2026-11-06-do-2025-sintetico-para-refinar-juiz]] (24 praticantes, autores e ferramenta da IBM; viés e polidez, com 2 e 3 classes; CC BY-NC-ND, integral na `url` da ficha): refinar critérios de um juiz LLM com caso sintético rendeu como o modo manual, em que 13 de 24 usaram 10 exemplos reais à disposição. Concordância com a expectativa, nos casos da tarefa: 0,85 e 0,89. Coincidir com a avaliação do próprio participante, feita antes, em 20 exemplos reais e sintéticos: 0,57 e 0,59. É sobre refinar, não estimar acerto, e o juízo do conjunto veio do próprio participante. Os autores acham efeito comparável; como as estratégias de refino foram em boa parte as mesmas nos dois braços, leem que o dado de teste pesou pouco ("limited downstream impact"), e mais casos não deram necessariamente critério melhor. Sem braço sem caso e sem medida antes do refino, a paridade não mostra que algum dos dois melhorou o juiz (leitura nossa). **É o vizinho mais próximo: juiz LLM com gabarito do dono, em texto curto** (leitura nossa). A distância ocorre nos dois braços, logo não separa artificial de real; fala de dentro do ajuste contra fora dele, com conjuntos e medidas diferentes, e os autores não fazem essa comparação (leitura nossa).
- Chong, Hong e Manning 2022 (citação, https://arxiv.org/abs/2205.12702): ruído de origem humana é mais difícil de detectar que o sintético, e é padrão melhor de avaliação, dizem.
- Rahman e outros 2025 (citação, https://arxiv.org/abs/2510.26130; geração de código, não juiz): 84% a 89% em benchmark sintético, 25% a 34% em classes reais.
- [[2026-11-06-balli-2026-oraculo-em-corpus-sintetico]] (um autor, no arXiv; caso próprio): a geração falhou em silêncio e fabricou um efeito de 32 pontos, que replicou de N=50 a N=500; só ler os itens crus mostrou. Corpus por perturbação determinística traz a própria conferência item a item, ao custo de naturalidade e cobertura. Sugere ler de 15 a 20 itens crus por condição, número calculado para falha em 30% dos itens, a 99% de confiança, "not universal".

## 5. Por que o artificial enganaria

**Há opinião e relato; medida da causa em caso de teste, não** (Rahmani mede a nota mais alta, sem explicar por quê). [[2026-10-30-husain-shankar-faq-de-avaliacoes]], em opinião: dado sintético não diz quão comum é a falha em produção e, em cenários como domínio complexo ou alto risco, pode perder detalhes e enganar ou esconder problemas. Do: o texto gerado não tinha a "messiness" do real, sem gíria, jargão, informalidade nem erro de gramática, e entrevistados do estudo formativo temem teste circular. Rohlfs: os casos podem sub-representar falhas contestadas ou específicas de uma cultura. Em outro uso, Goyal e Chong dão parte. Nas respostas, **não verificado:** "cleaner, more canonical" (Perplexity); gerador e juiz da mesma família dividem preferências, e falta a cauda longa (Gemini).

**Gerador e juiz aparentados, em caso de teste:** Rohlfs relatam que a sobreposição foi irrelevante, em casos inequívocos, com captura de 100% depois da calibração, inclusive em duas fatias escritas à mão, sem filtro por concordância; o artigo também diz que vários juízes concordaram em cada caso retido. Ballı tem produtores entre os juízes e relata que nenhum efeito de produtor ou de si mesmo sobreviveu.

[[2026-11-06-li-2026-preference-leakage]] (ICLR 2026, CC BY) mede um juiz LLM que favorece modelos alunos treinados com dados gerados por ele ou por modelo aparentado: pontuação de vazamento média de -0,1% a 27,9% nos seis pares, perto de zero em dois, maior em perguntas subjetivas e em alunos menores. Numa extensão preliminar, com rótulo humano em pares de respostas, a calibração contextual, com conjunto separado, reduziu o viés de 17,8 para 7,3, e a global subiu para 20,7. Li não testa juiz sobre caso de teste rotulado. Quando um assistente escreve o caso e um modelo de outra família julga, essa relação não foi medida (leitura nossa).

## 6. O caso a favor, como conferência

[[2026-11-06-rohlfs-2026-when-evaluators-cry-wolf]] (CC BY; no arXiv, sobre o produto da MagicSchool, de onde vêm 2 dos 5 autores; 21 avaliadores): conjunto sintético de falhas gritantes, de 12 a 79 casos por avaliador, para conferir que o caso grave ainda dispara. Todo caso retido foi revisto, os limítrofes e com desacordo saíram, e os autores admitem "inherent circularity". Dizem que isso **não** é medida de revocação nem vale para moderado ou limítrofe. Falha real era rara demais para medir direto. O conjunto de benchmark é o mesmo do ajuste, e os números são da amostra. O falso positivo dominou conforme o programa amadureceu, antes do ajuste: precisão por alerta de 0,6% para 49%, com protocolos diferentes antes e depois; depois do ajuste, ainda 51,1% dos alertas.

**Número sem fonte:** "85,3% a 33,8%" vem de um blog secundário que as buscas não identificam e que não nomeia o estudo; é modelo de segurança em benchmark público contra prompts adversários novos, não sintético contra real. **Não verificado.** Os 87% em HumanEval a 25-35% em código real, de geração de código, vêm de um fornecedor que a busca não nomeia, também não verificados.

**Atribuições conferidas que não fecham:** o Gemini disse que Maheshwari achou "significantly overestimated" em tarefas complexas e modelos que favorecem os próprios dados "far more favorably" do que dado real, que o benchmark "falhou completamente", e atribuiu a Li e outros uma concordância de 85%+ que cairia contra anotação humana. Nada disso está nos artigos.

## O que isto dá para um ambiente de agentes (leitura nossa)

- **Variações que pioram um critério de cada vez** servem cedo, para ver se a pergunta dispara, mas o número que sai dali pode superestimar como o desenho de duas portas, por vir de outra população. O 1,1 de Rutjes enfraquece a analogia sem excluí-la. A medida do acerto fica por conta dos casos reais, e a amostra de calibração precisa dizer de onde vem.
- **A forma útil** é a de Rohlfs e Ballı: conferir que o caso grave dispara, com os itens lidos.
- **Usar caso artificial para comparar versões de uma pergunta não tem medida.** As fontes ordenam sistemas e modelos diferentes, não versões do mesmo juiz, de 82 consultas a 200 exemplos ou mais. Com poucos positivos, um caso vale muitos pontos, escolher olhando o mesmo conjunto é reuso, e a falha que o artificial não contém (um campo que chega vazio no dado real, por exemplo) não aparece em ordem nenhuma. No máximo, triagem de diferença grande ou de regressão, a confirmar em caso real.
- **Controles escritos depois do ajuste** que acertam mais que os casos reais não separam acaso, casos fáceis e sobreajuste; estas fontes dão uma hipótese com nome para a diferença.

## Ver também

[[ponto-de-corte-reuso-do-teste-e-desvio]]; [[vieses-do-juiz-llm-e-defesas]]; [[quem-le-a-saida-do-avaliador]].
