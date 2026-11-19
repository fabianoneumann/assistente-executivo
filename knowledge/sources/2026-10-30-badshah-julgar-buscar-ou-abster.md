---
titulo: "Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees"
tipo: paper
autor: "Sher Badshah, Ali Emami, Hassan Sajjad"
url: "https://arxiv.org/abs/2608.17994"
publicado_em: 2026-08-18
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, selective-evaluation, abstention, cascade, conformal-risk-control, false-discovery-rate, uncertainty-quantification, retrieval, fact-checking, human-in-the-loop]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 18/08/2026, a única versão e a lida. O comentário do arXiv diz "Accepted at Conference on Language Modelling 2026", e o PDF traz "Published as a conference paper at COLM 2026". Dalhousie University e New York University Abu Dhabi (Badshah, Sajjad) e Emory University (Emami). O integral foi extraído do PDF; as tabelas do apêndice foram lidas também na versão HTML do arXiv. Lida (camadas flexíveis de avaliação).

## O resumo

Juízes LLM viraram prática padrão para avaliar saídas em escala, sobretudo em tarefas subjetivas e abertas sem resposta de referência. Tarefas objetivas trazem outro problema para o juiz sem referência: ele avalia a correção factual pelo conhecimento paramétrico (eficiente, mas pode alucinar ou não ter evidência) ou com ferramentas (mais evidência, mais custo, e precisa de um mecanismo que decida quando e como usar a evidência). Nenhum dos dois, sozinho, dá controle formal do risco dos vereditos aceitos. A proposta: calibrar limiares de incerteza num conjunto separado para que a **taxa de falsas descobertas** (FDR) entre os vereditos aceitos fique abaixo de um nível α escolhido pelo usuário, com alta probabilidade, usando intervalos de Clopper-Pearson de amostra finita. Quando o modo paramétrico não está confiante, o item vai para um modo com busca na web e é reavaliado sob um segundo limiar calibrado. A garantia de amostra finita vale para esse roteamento de dois limiares sem hipóteses adicionais. Em benchmarks de perguntas e respostas de domínio aberto e juízes de vários tamanhos, o método mantém a taxa de erro alvo com cobertura bem maior que as linhas de base de um modo só.

## 1. Introdução

- O juiz LLM avalia milhares de saídas a uma fração do custo humano, mas a maior parte do uso é subjetiva (utilidade, inocuidade, estilo), onde concordância aproximada basta. Em perguntas factuais de domínio aberto, a resposta é certa ou errada, e o gabarito é caro em escala, exige especialistas e é inviável quando LLMs agem como agentes autônomos sem rótulos prévios.
- Dois problemas do juiz sem referência: (1) limitado pelos dados de treino, pode não conhecer eventos recentes, entidades raras ou domínios especializados e não separar resposta certa de invenção plausível; (2) mesmo sabendo, pode alucinar e dar veredito confiante e errado. Nos dois casos **a falha é silenciosa**: o juiz não indica que o veredito é pouco confiável, e o erro passa para as decisões seguintes.
- A avaliação seletiva deixa o juiz se abster quando incerto. Medidas de incerteza identificam vereditos pouco confiáveis, mas um limiar heurístico sobre elas não dá garantia formal sobre a taxa de erro dos aceitos. Trabalhos recentes de predição seletiva com risco controlado calibram limiares que limitam a FDR com alta probabilidade, mas foram feitos para filtrar respostas de examinandos em QA, não para meta-avaliação, e tratam a abstenção como único recurso, descartando casos em que a incerteza vem de lacuna de conhecimento ou alucinação que evidência adicional resolveria.
- **A proposta em dois modos:** no Modo 1, o juiz avalia só com o conhecimento paramétrico; se confiante, o veredito é aceito. Se incerto, vai ao Modo 2, em que busca evidência na web e reavalia. Se continuar incerto, abstém-se e marca o item para revisão humana. Os dois limiares são calibrados juntos num conjunto separado com gabarito, por limites superiores de Clopper-Pearson. Os autores provam que a garantia de amostra finita para um par fixo de limiares vale no roteamento sem hipóteses distribucionais adicionais.
- Contribuições: formular a avaliação seletiva com risco controlado para juiz LLM em QA factual; o roteamento em dois modos com busca adaptativa antes da abstenção; mostrar que a estrutura de Bernoulli exigida pelo Clopper-Pearson se estende aos dois limiares; experimentos mostrando que a busca adaptativa recupera cobertura sobre as linhas de base de um modo só, controlando a taxa de erro do juiz.

## 2. Trabalhos relacionados

- **Juiz LLM:** LLMs fortes aproximam preferências humanas em dimensões subjetivas e são usados em modelagem de recompensa. Em tarefas objetivas, o SAFE usa um agente com busca para verificar fatos em respostas longas, e o SAGE (dos mesmos autores) um agente com ferramentas que busca e sintetiza evidência para avaliar QA sem referência; melhoram a acurácia, sem garantia formal.
- **Incerteza na avaliação:** métodos de caixa branca usam as probabilidades dos tokens (o mais comum é a entropia preditiva), frequentemente bem calibradas; métodos de caixa preta consultam o juiz várias vezes e medem a consistência dos vereditos. Os dois se correlacionam com a acurácia, mas são heurísticos: um limiar escolhido à mão ou ajustado em validação não garante a taxa de erro dos aceitos.
- **Roteamento por incerteza e uso de ferramentas:** FrugalGPT e AutoMix usam a confiança para rotear entre modelos, trocando custo por qualidade; o FLARE usa a incerteza por token para decidir quando buscar durante a geração; o SAGE introduziu busca para juízes. Essas abordagens costumam buscar incondicionalmente, com computação desnecessária, e não dão garantia formal.
- **Avaliação seletiva com risco controlado:** a predição conformal dá garantias de cobertura sem hipótese de distribuição e de amostra finita; o controle conformal de risco generaliza para limitar perdas, inclusive a FDR. Em QA, o SConU constrói conjuntos de predição, e o COIN calibra um limiar que limita a FDR das respostas aceitas com Clopper-Pearson. Mais perto deste trabalho, Trust or Escalate (Jung et al., 2025) e SCOPE adaptam isso à avaliação par a par com garantia de concordância humana, mas em tarefas subjetivas de preferência, não de correção factual.

## 3. Método

Os limiares são calibrados num conjunto separado com rótulos humanos para que a probabilidade de um veredito errado entre os itens avaliados fique limitada por α. Uma nota de rodapé diz que a revisão humana não foi implementada: o termo indica que esses itens saem da avaliação automática.

**3.1 Formulação.**
- Um examinando F gera a resposta candidata a uma pergunta; y* é a resposta de gabarito. O juiz J dá um veredito binário v (1 = considera a candidata correta).
- **Função de admissão:** o rótulo de verdade e* (a candidata é mesmo correta?) vem de anotação humana ou de uma função de relevância entre candidata e gabarito com um limiar. O veredito é admissível se v = e*.
- **Avaliação seletiva:** com um escore de incerteza U, o juiz só dá veredito se U ≤ t. A FDR é o erro esperado entre os itens em que o juiz escolhe avaliar.
- **Objetivo:** para um risco α e uma significância δ (por exemplo 0,05), achar t tal que a FDR ≤ α com probabilidade de pelo menos 1 − δ, sobre a aleatoriedade dos dados de calibração.
- **Calibração:** N exemplos separados, com gabarito, i.i.d. da mesma distribuição.

**3.2 Incerteza.** Quanto melhor o escore separa vereditos certos de errados, maior a cobertura (menos abstenções) num dado nível de risco.

**3.3 Avaliação seletiva com risco limitado (um modo).** Para cada limiar candidato t, contam-se os itens selecionados (U ≤ t) e os erros entre eles; a FDR empírica é a razão. Ela é estimativa sem viés, mas pode subestimar o risco num conjunto de calibração por variação amostral. Como os itens são i.i.d. e a seleção é função determinística da pergunta e da candidata, os indicadores de falha dos selecionados são Bernoulli i.i.d., e aplica-se o limite superior unilateral exato de Clopper-Pearson (inversa da Beta com erros + 1 e acertos). Escolhe-se o **maior limiar cujo limite superior fica abaixo de α para todos os limiares menores**, maximizando os itens avaliados.

**3.4 Busca adaptativa em dois modos.**
- **Modo 1 (direto):** o juiz usa só o conhecimento interno e produz v1 e U1.
- **Modo 2 (com busca):** consulta-se um buscador web com a própria pergunta, pegam-se os k primeiros resultados (título, trecho, URL), concatenados num bloco de evidência anexado ao prompt; o juiz reavalia e produz v2 e U2.
- **Roteamento no teste:** se U1 ≤ t1, sai v1; se U1 > t1 e U2 ≤ t2, sai v2; senão, abstém-se. A busca só ocorre quando o Modo 1 está incerto, então itens confiantes não têm custo de busca.
- **Calibração conjunta:** os dois modos são pré-computados para todos os N itens de calibração; para cada par (t1, t2), contam-se os aceitos por qualquer dos modos e os erros entre eles, e escolhe-se o par que **maximiza a cobertura sujeito ao limite superior ≤ α**. A busca percorre os valores únicos de incerteza ordenados, com somas acumuladas, em tempo proporcional ao produto dos dois conjuntos de candidatos (Algoritmo 1). Como a busca avalia muitos pares, reportam também uma variante conservadora com correção de Bonferroni (δ dividido pelo número de pares; apêndice D.4).

**3.5 Garantia teórica.** Lema 1: com dados i.i.d. e limiares fixos, os indicadores de falha dos selecionados pelo roteamento são Bernoulli i.i.d. com parâmetro igual à FDR do par. A prova: seleção e correção dos selecionados são funções determinísticas de (pergunta, candidata, gabarito), e condicionar à seleção preserva independência e identidade de distribuição. Com o Clopper-Pearson, vale para qualquer par fixo: a FDR fica abaixo do limite superior com probabilidade de pelo menos 1 − δ; qualquer par fixo cujo limite fique ≤ α controla o erro em α com confiança 1 − δ.

**Custo.** Se p é a fração aceita pelo Modo 1, a busca roda só em 1 − p dos itens. Com α = 0,20 e Qwen3-14B no TriviaQA, p ≈ 0,45: quase metade das avaliações sem custo de busca. Em benchmarks mais difíceis p cai, mas os itens mais confiantes continuam sem busca.

## 4. Experimentos

- **Dados:** quatro benchmarks de QA de domínio aberto (TriviaQA, Natural Questions, HotpotQA, PopQA), 2.000 itens de cada partição separada padrão, semente 42.
- **Candidatos:** Qwen3-8B e LLaMA-3.1-70B (decodificação gulosa; modo de raciocínio do Qwen3 desligado). **Juízes:** Qwen3-4B, Qwen3-8B, Qwen3-14B e LLaMA-3.1-8B-Instruct, com veredito binário (True/False) e uma explicação curta.
- **Funções de admissão** (para saber se a candidata está mesmo certa): correspondência exata, F1 de tokens (≥ 0,5) e um avaliador LLM (Qwen2.5-7B-Instruct) que julga equivalência semântica com a referência.
- **Incerteza:** entropia preditiva binária, calculada das probabilidades dos tokens True e False na posição do veredito, numa única passada. Quando há acesso aos estados ocultos, pode ser trocada por escores supervisionados sem mudar a garantia (apêndice D.2).
- **Busca:** API Serper com a pergunta original, k = 3 por padrão; k em {3, 6, 9} testado num par (candidato LLaMA-70B, juiz Qwen3-8B).
- **Calibração:** 100 divisões aleatórias 50/50 entre calibração e teste, δ = 0,05, α em {0,05; 0,10; 0,15; 0,20; 0,25}.
- **Métricas:** FDR (fração dos aceitos com veredito errado), cobertura (fração aceita em vez de abstida) e distribuição do roteamento (Modo 1, Modo 2, abstenção). Resultados principais com entropia preditiva e avaliador LLM.

## 5. Resultados

### 5.1 O controle da FDR vale em todas as configurações

Nas 32 combinações de candidato, juiz e conjunto (Figura 1), a FDR de teste fica igual ou abaixo de α em todos os casos. Três observações dos autores: os quatro juízes dão controle válido qualquer que seja o tamanho, então a garantia não exige um juiz forte; a FDR fica perto de α com faixas estreitas (±0,01 a 0,02) nas 100 divisões; a distância entre FDR e α é menor no TriviaQA e no PopQA, mais fáceis, onde os juízes acertam mais.

### 5.2 A cobertura cresce com a tolerância ao risco e com a capacidade do juiz (Tabela 1)

Cobertura do método de dois modos, média de 100 divisões, com α = 0,05 / 0,10 / 0,15 / 0,20 / 0,25:

| Candidato | Juiz | TriviaQA | NQ-Open | PopQA | HotpotQA |
|---|---|---|---|---|---|
| Qwen-8B | Qwen-4B | .03 / .39 / .66 / .91 / 1.0 | .00 / .03 / .08 / .14 / .28 | .00 / .01 / .91 / 1.0 / 1.0 | .00 / .04 / .09 / .14 / .30 |
| Qwen-8B | Qwen-8B | .12 / .63 / .91 / 1.0 / 1.0 | .00 / .02 / .24 / .82 / 1.0 | .00 / .87 / 1.0 / 1.0 / 1.0 | .00 / .04 / .49 / .74 / .96 |
| Qwen-8B | Qwen-14B | .21 / .78 / .98 / 1.0 / 1.0 | .00 / .05 / .56 / .81 / .99 | .19 / .89 / 1.0 / 1.0 / 1.0 | .02 / .26 / .64 / .86 / 1.0 |
| Qwen-8B | Llama-8B | .13 / .61 / .86 / 1.0 / 1.0 | .00 / .20 / .61 / .83 / 1.0 | .02 / .88 / 1.0 / 1.0 / 1.0 | .01 / .30 / .65 / .85 / 1.0 |
| Llama-70B | Qwen-4B | .05 / .37 / .80 / .98 / 1.0 | .00 / .05 / .18 / .32 / .48 | .00 / .00 / .11 / .35 / .92 | .00 / .09 / .20 / .34 / .55 |
| Llama-70B | Qwen-8B | .17 / .44 / .83 / .99 / 1.0 | .01 / .10 / .25 / .47 / .73 | .00 / .06 / .11 / .48 / .98 | .00 / .11 / .31 / .47 / .65 |
| Llama-70B | Qwen-14B | .12 / .46 / .85 / 1.0 / 1.0 | .00 / .05 / .23 / .51 / .75 | .00 / .04 / .31 / .77 / .99 | .00 / .07 / .31 / .53 / .76 |
| Llama-70B | Llama-8B | .04 / .32 / .67 / .86 / 1.0 | .00 / .02 / .13 / .32 / .59 | .00 / .07 / .23 / .77 / .98 | .00 / .02 / .11 / .27 / .51 |

A cobertura depende da dificuldade do conjunto e da capacidade do juiz. Nos fáceis (TriviaQA, PopQA), até o menor juiz chega perto da cobertura total com α = 0,25; nos que exigem mais conhecimento (NQ-Open, HotpotQA), só os juízes maiores (Qwen-14B, Llama-8B) passam de 80% com α = 0,20 para o candidato Qwen-8B, e o Qwen-4B fica abaixo de 15%. Avaliar o candidato LLaMA-70B, mais forte, é consistentemente mais difícil: o melhor juiz chega a só 53% no HotpotQA com α = 0,20. Os autores atribuem a diferença à diversidade das respostas do modelo de 70B e à maior exigência de conhecimento sobre o juiz.

### 5.3 A busca adaptativa recupera muita cobertura

Na distribuição do roteamento (Figura 2), o Modo 2 responde pela maioria dos vereditos não abstidos em várias configurações. Os autores ressalvam que isso não quer dizer que o juiz não saiba avaliar, e sim que a incerteza no Modo 1 não basta para passar o limiar calibrado; são itens em que um método de um modo só se absteria. Juízes com incerteza mais bem calibrada resolvem mais itens no Modo 1: com α = 0,20 no TriviaQA, o Qwen3-14B resolve 45% pelo conhecimento paramétrico e o Qwen3-4B 9%. Em HotpotQA e NQ-Open, todos os juízes dependem sobretudo da evidência buscada. A busca nem sempre aumenta a confiança: em 14% a 29% dos itens ela **aumenta** a incerteza (apêndice E.1), e o segundo limiar manda esses casos para a abstenção.

### 5.4 Um modo contra dois modos (Tabela 2, cobertura com α = 0,20, "só Modo 1" → "conjunto")

| Candidato | Juiz | TriviaQA | NQ-Open | PopQA | HotpotQA |
|---|---|---|---|---|---|
| Qwen-8B | Qwen-4B | .47 → .91 | .01 → .14 | .04 → 1.0 | .00 → .14 |
| Qwen-8B | Qwen-8B | .59 → 1.0 | .07 → .82 | .03 → 1.0 | .05 → .74 |
| Qwen-8B | Qwen-14B | .87 → 1.0 | .14 → .81 | .15 → 1.0 | .35 → .86 |
| Qwen-8B | Llama-8B | .77 → 1.0 | .22 → .83 | .21 → 1.0 | .40 → .85 |
| Llama-70B | Qwen-4B | .67 → .98 | .07 → .32 | .05 → .35 | .09 → .34 |
| Llama-70B | Qwen-8B | .82 → .99 | .22 → .47 | .08 → .48 | .27 → .47 |
| Llama-70B | Qwen-14B | .84 → 1.0 | .12 → .51 | .15 → .77 | .24 → .53 |
| Llama-70B | Llama-8B | .48 → .86 | .02 → .32 | .12 → .77 | .02 → .27 |

No TriviaQA o Modo 1 já cobre muito para juízes fortes (87% no Qwen3-14B) e a busca dá ganho modesto e consistente; o efeito é maior no NQ-Open (Qwen3-8B de 7% para 82%), no HotpotQA (Llama-8B de 40% para 85%) e para o juiz mais fraco no PopQA (Qwen3-4B de 4% para 100%).

### 5.5 Robustez à mudança da web

Os resultados da busca mudam com o tempo, a principal ameaça prática à determinância que a garantia supõe para o Modo 2. Na configuração principal (candidato e juiz Qwen3-8B, avaliador LLM, k = 3), as mesmas 2.000 perguntas do TriviaQA e do HotpotQA foram consultadas de novo cerca de três meses depois. As páginas mudaram muito: sobreposição de Jaccard média por item entre as listas ordenadas dos 3 primeiros URLs de 0,30 (TriviaQA) e 0,24 (HotpotQA); ignorando a ordem, 0,47 e 0,40. Com os limiares calibrados na coleta original e aplicados aos vereditos do Modo 2 refeitos sobre a evidência nova (Modo 1 igual), em 100 divisões, a FDR ficou abaixo de α em todos os cenários e a cobertura ficou quase estável (Tabela 3: no TriviaQA, diferenças de cobertura entre 0 e +0,06; no HotpotQA, entre −0,02 e 0). Os autores concluem que a deriva muda mais quais páginas voltam do que a qualidade geral da evidência e que os limiares seguem válidos após a reimplantação.

## 6. Conclusão e trabalhos futuros

O método dá garantias de amostra finita sobre a confiabilidade dos vereditos aceitos, roteia os itens incertos para um segundo modo e obtém cobertura maior que a abstenção de um modo só; a garantia de Clopper-Pearson continua válida na política conjunta de dois limiares sem hipóteses distribucionais adicionais; em todas as configurações testadas a FDR observada ficou igual ou abaixo do alvo. Trabalhos futuros: avaliação graduada e subjetiva, e juízes de caixa preta sem acesso às probabilidades (logits).

## Apêndices: o que acrescentam

**A. Provas e limites declarados.** A.1 prova a validade do limite de Clopper-Pearson (contagem de erros binomial; a função de distribuição é monotônica decrescente no risco verdadeiro; propriedade de super-uniformidade para distribuições discretas). A.2 prova o Lema 1; os dois termos de seleção são mutuamente exclusivos. **Escopo e limites:** a garantia está presa ao retrato da busca usado na calibração; como o índice da web muda, uma consulta pode trazer outra evidência na implantação. A deriva só afeta a garantia se mudar a taxa de erro condicional dos vereditos do Modo 2; se a qualidade da evidência mudar muito, recalibrar restaura a garantia. Qualquer mudança na tarefa, no modelo candidato ou no juiz viola a hipótese de permutabilidade e exige recalibração.

**B. Detalhes.** Prompts do juiz: no Modo 1, juiz imparcial que decide pelo próprio conhecimento se a resposta candidata está correta, com um exemplo de formato (Decision e Explanation); no Modo 2, decide usando os resultados da busca ("se os resultados apoiam, True; se contradizem, False; se inconclusivos, use seu melhor julgamento"). O avaliador LLM de admissão considera a candidata correta se ela transmite o mesmo sentido de qualquer resposta de referência, mesmo mais longa, com sinônimos, abreviações ou nomes alternativos. Na calibração, a busca em grade maximiza os itens aceitos corretamente sujeito ao limite.

**C. Mais resultados.** Acurácia bruta dos vereditos antes da calibração (Tabela 5): a busca melhora a acurácia em todas as configurações, com os maiores ganhos no PopQA (até 44 pontos; Qwen3-8B como juiz do candidato Qwen-8B vai de 44% para 88%). Com o candidato LLaMA-70B, os ganhos são menores (por exemplo, TriviaQA de 78% para 81–82% nos juízes Qwen-8B e Qwen-14B). A Tabela 6 dá FDR e cobertura para α até 0,60.

**D. Ablações e robustez** (em todos os casos a FDR fica controlada; escolhas conservadoras reduzem a cobertura em vez de comprometer o controle):
- **Função de admissão** (candidato Qwen3-8B, juiz Qwen3-14B): o avaliador LLM dá a maior cobertura, com a maior diferença nos conjuntos que exigem conhecimento: no NQ-Open com α = 0,15, 56% contra 0% da correspondência exata e do F1. Os autores explicam que critérios de correspondência de texto penalizam respostas semanticamente certas e de forma diferente, inflando a taxa de erro aparente do juiz.
- **Profundidade da busca** (k = 3, 6, 9): cobertura e FDR estáveis, diferenças de 1 a 2 pontos, salvo o PopQA, em que a cobertura cai de 0,48 para 0,41 e 0,36; k = 3 já basta.
- **Nível de confiança:** apertar δ de 0,05 para 0,01 troca cobertura por confiança, com o custo concentrado em α baixo e no conjunto difícil (HotpotQA com α = 0,15: de 0,49 para 0,37).
- **Tamanho da calibração:** no TriviaQA a cobertura é estável; no HotpotQA cai aos poucos quando o conjunto de calibração encolhe (com α = 0,20: 0,77 com 75% dos itens, 0,74 com 50%, 0,70 com 25%, 0,55 com 10%).
- **Outros escores de incerteza:** a garantia depende só do indicador binário de correção, então o escore afeta a cobertura, não o controle. Dois escores supervisionados sobre o estado oculto da última camada na posição do veredito (uma pequena MLP e um adaptador LoRA com prompt, treinados por validação cruzada de 5 partes no conjunto de calibração): o LoRA dá a maior cobertura, sobretudo onde a entropia informa pouco (HotpotQA com α = 0,10: de 0,04 para 0,44; PopQA com α = 0,05: de 0,00 para 0,71); a MLP melhora em níveis de risco moderados nos conjuntos difíceis (NQ-Open com α = 0,15: de 0,24 para 0,42) e piora nos níveis mais baixos.
- **Linhas de base** (mesma calibração, muda a base do veredito aceito): "direto" (só Modo 1), "autoavaliação" (segunda passada em que o juiz julga o próprio veredito, sem evidência nova) e "vazio" (prompt do Modo 2 sem evidência). O método conjunto domina as três em quase todos os pontos, com a maior diferença no HotpotQA (com α = 0,20, o texto diz 0,74 contra no máximo 0,07 dos controles sem busca; a Tabela 12 traz 0,05 para o direto, 0,07 para a autoavaliação e 0,57 para o vazio). A segunda passada sem evidência quase não ajuda, o que para os autores confirma que o ganho vem da evidência buscada e não de consultar o juiz de novo.
- **Calibração conjunta conservadora:** como o par de limiares é escolhido pelos dados, certificar o par escolhido exige contar a busca; a variante com Bonferroni sobre todos os pares (ou sobre N², limite que não depende dos dados) faz a garantia valer simultaneamente para todos os pares. Nos experimentos principais usaram a seleção sem correção, porque ela já deu controle efetivo do risco, e tratam a conservadora como alternativa teoricamente válida. A correção quase não custa nos conjuntos fáceis e custa muita cobertura nos difíceis (NQ-Open com α = 0,20: de 0,82 para 0,05; HotpotQA: de 0,74 para 0,30). Os autores dizem que Bonferroni é um limite de pior caso muito frouxo, porque limiares vizinhos selecionam quase os mesmos itens, e que a cobertura conjuntamente válida de fato fica entre as duas, mais perto da sem correção.

**E. Análise.**
- **Efeito da busca na incerteza** (candidato e juiz Qwen3-8B): a busca aumenta a incerteza em 20,1% dos itens no TriviaQA, 27,9% no NQ-Open, 14,3% no PopQA e 29,1% no HotpotQA, e a reduz em 68,0%, 68,8%, 84,6% e 69,7%. Os aumentos se concentram no HotpotQA (várias etapas) e no NQ-Open, onde os trechos são só parcialmente relevantes ou as fontes discordam.
- **Exemplos em que a busca corrige o juiz** (candidato Qwen3-8B, juiz Qwen3-14B): quem dubla Jack Kahuna Laguna em Bob Esponja (candidata "Steve Carell", certo "Johnny Depp"); qual país do norte da África tem a bandeira só verde (candidata "Chade", certo "Líbia"); "The Great American Chocolate Bar" (candidata "Milky Way", certo "Hershey"). Nos três, o Modo 1 aceitou a resposta errada com segurança, e no Modo 2 o primeiro resultado da busca continha a resposta certa.
- **Modos de falha** quando a busca não corrige: (i) busca fora do assunto, por pergunta ambígua; (ii) evidência insuficiente, trechos só parcialmente relevantes; (iii) erro de raciocínio do juiz mesmo com a evidência presente (por exemplo, responder False por falta de correspondência literal); (iv) discordância da função de admissão, quando a candidata é semanticamente próxima do gabarito mas pontuada como diferente. A política de dois limiares manda muitos desses casos para a abstenção, e por isso, nos conjuntos mais difíceis, é a cobertura, e não a FDR, que absorve a dificuldade.

---
