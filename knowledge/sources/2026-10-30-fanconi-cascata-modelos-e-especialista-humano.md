---
titulo: "Cascaded Language Models for Cost-effective Human-AI Decision-Making"
tipo: paper
autor: "Claudio Fanconi, Mihaela van der Schaar"
url: "https://arxiv.org/abs/2506.11887"
publicado_em: 2025-06-13
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [cascade, human-in-the-loop, escalation, deferral, abstention, selective-prediction, calibration, verification, online-learning, cost]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 13/06/2025, v2 em 16/06/2025 e v3 (lida) em 24/10/2025. O PDF da v3 traz no rodapé da primeira página "39th Conference on Neural Information Processing Systems (NeurIPS 2025)". Universidade de Cambridge; código em github.com/fanconic/cascaded-llms. O integral foi extraído do PDF da v3, que inclui a lista de verificação da NeurIPS. Lida (camadas flexíveis de avaliação).

## A pergunta

Na decisão com apoio de IA, três fatores precisam ser equilibrados: a correção das previsões, o custo (de conhecimento e de complexidade de raciocínio) e a confiança para decidir quando abster-se da resposta automática e escalar para um especialista humano. A dificuldade é alocar recursos computacionais e humanos: quando o modelo automático responde, quando escala para um modelo maior e mais capaz, quando passa a um humano. Estratégias ingênuas falham: confiar sempre no modelo barato aumenta erros e alucinações; confiar sempre no capaz encarece. Políticas de delegação estáticas, limiares fixos e calibrações feitas uma vez não se adaptam a mudanças na distribuição das tarefas nem na competência do modelo.

## Os três requisitos (desiderata)

- **D1, reduzir regenerações desnecessárias:** só regenerar com o modelo mais capaz quando houver evidência suficiente de que a resposta atual não é confiável.
- **D2, abster-se quando incerto:** passar ao especialista humano quando a incerteza passa de limites aceitáveis, evitando automação superconfiante em cenários de alto risco.
- **D3, adaptar-se com o tempo:** refinar continuamente as políticas de delegação e de abstenção conforme chega retorno.

Os autores dizem que esses requisitos valem para qualquer sistema desse tipo, independentemente da implementação.

## A abordagem e as contribuições

Uma cascata em níveis: um **modelo base** leve dá a resposta inicial; um **modelo grande**, mais capaz e mais caro, regenera a resposta quando a confiança é baixa; e, se a incerteza continua alta, o sistema **se abstém** e passa a um **especialista humano**. Duas etapas de decisão: uma **política de delegação** (deferral), baseada na confiança, decide se aceita a resposta do base ou regenera com o grande; uma **política de abstenção**, baseada na incerteza, decide se a resposta da cascata é certa o bastante ou precisa de intervenção humana. Um mecanismo de **aprendizado online** ajusta os limiares das duas políticas com o retorno humano. Contribuições declaradas: o sistema multinível que coordena modelos de capacidades diferentes com especialistas humanos; políticas de delegação e abstenção guiadas por calibração bayesiana; e a otimização online dos limiares.

**Figura 1 (exemplos):** pergunta fácil (de que as plantas fazem comida com luz do sol): o base gera, a verificação barata dá incerteza baixa e a resposta fica. Pergunta média (sobre a doença do tumor facial do diabo-da-tasmânia): o base responde D, a confiança leva à regeneração pelo grande, que responde B com incerteza baixa. Pergunta difícil (caso clínico sobre o antibiótico dado): o base responde A, a incerteza é alta e a decisão vai ao especialista, que responde D; o retorno online ajusta os módulos.

## Trabalhos relacionados

- **Geração com vários LLMs:** estratégias de custo como as do FrugalGPT (estruturação de prompt, aproximação de modelo, cascatas), roteamento que atribui cada prompt ao modelo mais adequado, um arcabouço caixa-preta formalizado como processo de decisão de Markov parcialmente observável (AutoMix), um multiplexador com classificador BERT entre modelo pequeno e grande, um meta-modelo de seleção, e decodificação especulativa (o modelo leve gera tokens que o grande verifica). A diferença declarada: este trabalho integra a intervenção humana quando a incerteza é alta, e prioriza a correção da resposta completa, não a distribuição token a token. O trabalho mais próximo, simultâneo, é o de Zellinger e colegas sobre modelagem probabilística de cascatas com delegação e abstenção.
- **Verificação e quantificação de incerteza:** autoverificação, uso de conhecimento externo, verificação por várias consultas ao modelo, a probabilidade de token substituto de Kadavath et al. (2022), classificadores sobre estados internos e incerteza semântica. O artigo usa a probabilidade de token substituto como componente central e acrescenta a escalada hierárquica entre modelos e humanos.
- **Predição seletiva:** abster-se em entradas incertas, desde Chow (reconhecimento óptico de caracteres, 1957 e 1970); em PLN, por limiares de confiança.
- **Aprendizado online:** políticas refinadas com dados em fluxo; inspiração na mediação online de decisões de Jarrett et al. (2022), que medeia entre decisões humanas subótimas e um oráculo especialista.

## O sistema em cascata (seção 3)

- Dois níveis, base → grande. Para cada entrada x, cada modelo devolve um escore de confiança Φ(x) em [0, 1] e um escore de incerteza Ξ(x) em [0, ∞). Delegar ou não depende de a confiança do base passar de um limiar de delegação φ_base: só se prevê com o base se ele for confiante o bastante. A abstenção depende da incerteza: se Ξ_i(x) passa do limiar ξ_i, o sistema se abstém e encaminha ao humano.
- **Eq. 1:** responde o base se a confiança dele está acima de φ_base e a incerteza abaixo de ξ_base; responde o grande se a confiança do base ficou abaixo de φ_base e as incertezas ficaram dentro dos limiares; senão, abstém-se. Os autores dizem que o arcabouço se generaliza para cascatas com vários LLMs.
- **Risco do sistema (Eq. 2):** o objetivo combina três dimensões, erro, custo e abstenção (seguindo Zellinger e Thomson, 2024): R = P(erro sem abstenção) + λ_c·E[custo] + λ_a·P(abstenção), com λ_c e λ_a pesando custo e abstenção.
- **Hipóteses:** A1, o base é barato e menos preciso, o grande é mais capaz e caro; A2, gerar respostas custa bem mais que processar a entrada, sobretudo com cadeia de pensamento ou raciocínio no momento do teste; A3, cada resposta é certa ou errada, sem ambiguidade.
- **Custo (Eq. 3):** custo = s·(t_in + ρ·t_out), com s o tamanho do modelo em bilhões de parâmetros, t_in e t_out os tokens de entrada e saída e ρ > 0 a razão de custo entre saída e entrada. Serve para comparar modelos sem depender do preço de infraestrutura; outros componentes podem ser somados.

## Confiança e incerteza calibradas (seção 4.1)

Delegação e abstenção dependem de medir bem a confiança e a incerteza: previsões superconfiantes ou mal calibradas levam a erros; incerteza excessiva leva a escaladas desnecessárias. Quatro métodos estimam a probabilidade de a resposta estar certa:

1. **Autoverificação (SV):** pede-se ao modelo uma nota de 0,0 a 1,0 de quão provável é a resposta estar certa; a saída é uma estimativa não calibrada.
2. **Autoverificação consistente (SV, n = 5):** repete-se a autoverificação n vezes com amostragem estocástica e tira-se a média.
3. **Probabilidade de token substituto (STP):** pergunta-se ao modelo se a resposta está certa e lê-se a probabilidade do próximo token entre SIM e NÃO: P(SIM) / (P(SIM) + P(NÃO)) (Eq. 4).
4. **STP por Monte Carlo (MC-STP, n = 5):** aplica-se dropout de Monte Carlo no teste, faz-se n passagens estocásticas e tira-se a média (Eq. 5).

**Avaliação por um modelo maior:** o verificador pode ser o próprio modelo que gerou a resposta ou o modelo maior da cascata. Autoavaliar é barato; verificar a saída do pequeno com o grande ainda é bem mais barato que gerar uma resposta nova (hipótese A2), e modelos maiores tendem a ser mais bem calibrados, segundo trabalhos citados.

**Calibração bayesiana:** para tornar os escores comparáveis entre modelos e coerentes com a correção observada, ajusta-se uma regressão logística bayesiana num conjunto de calibração de **100 amostras** (uma versão bayesiana da escala de Platt, com priori normal). Antes, aplica-se uma transformação não linear ao escore bruto (Eq. 6, seguindo Zellinger e Thomson) para espalhar os aglomerados de probabilidades superconfiantes. A média da distribuição preditiva posterior é a confiança calibrada Φ(x); o desvio-padrão é a incerteza Ξ(x).

## Melhora online (seção 4.2)

- Os limiares de delegação e abstenção são parâmetros otimizados online por descida de gradiente estocástica. Supõe-se que, com o sistema em uso, a resposta verdadeira chega ao fim de cada decisão **em que o sistema se absteve**; o conjunto de dados só cresce nas abstenções.
- O objetivo é o risco do sistema. Os limiares φ_base, ξ_base e ξ_large ficam em (0, 1) por meio de uma sigmoide sobre parâmetros livres. Para tudo ficar diferenciável, cada teste booleano vira um degrau logístico suave σ(k·z), com k regulando a inclinação.
- Máscaras no nível do base: probabilidade de abster-se (Eq. 7), de prever (Eq. 8) e de delegar (Eq. 9); no nível do grande, de abster-se e de prever, condicionadas à delegação (Eqs. 10 e 11). P(abstenção) é a soma das duas formas excludentes de abster-se (Eq. 12). A correção esperada pondera cada máscara de previsão pela confiança calibrada do modelo correspondente (Eq. 13). O custo esperado é c1 (geração e verificação do base, paga em toda consulta) mais a probabilidade de delegar vezes c2 (geração e verificação do grande) (Eq. 14). A perda é R = 1 − E[correto] + λ_c·E[custo] + λ_a·(p_abst1 + p_abst2) (Eq. 15).
- **Risco de um modelo só (apêndice A.1):** 1 − E[(1 − m_abst)·Φ] + λ_c·c + λ_a·E[m_abst], com um único limiar de abstenção.

## Experimentos: configuração

Cascata principal Qwen-2.5-1.5B → Qwen-2.5-7B; no apêndice C, Llama3.2-3B → Llama3.1-8B, Llama3.2-1B → Llama3.1-8B e Qwen-2.5-3B → Qwen-2.5-7B. Escolhidos por serem abertos e caberem numa GPU NVIDIA A100. Cinco conjuntos de múltipla escolha: ARC2-Easy e ARC2-Challenge (ciências do ensino fundamental), MMLU (57 matérias, de STEM a direito internacional, nutrição e religião), MedQA (exame de licenciamento médico dos EUA) e MedMCQA (exame de entrada de medicina da Índia). As respostas são geradas com cadeia de pensamento. A razão de custo saída/entrada é ρ = 5, que os autores dizem estar de acordo com os preços da Anthropic na época. Os prompts estão no apêndice B.2 (geração com papel por conjunto, por exemplo "médico fazendo o exame de licenciamento"; autoverificação pedindo nota de 0,0 a 1,0; STP pedindo um único token sim ou não).

## Custo-benefício dos métodos de verificação (seção 5.1, D1 e D2)

- **Comparação:** a confiança calibrada do base contra usar só o base (1,5B) e só o grande (7B), em acurácia por custo por amostra (Figura 3). Estratégia sem limiar: delega-se ao grande com probabilidade Φ_base(x). Quatro métodos (SV n = 1, STP n = 1, SV n = 5, MC-STP n = 5), cada um uma vez com o base como verificador e outra com o grande. Ficar acima da reta que liga base e grande indica custo-benefício positivo.
- **Resultado qualitativo:** verificar com o modelo grande dá, em geral, melhor perfil de custo-benefício, sobretudo nos conjuntos mais simples (ARC2-Easy, ARC2-Challenge, MMLU); verificar com o base dá ganho marginal. Nos conjuntos médicos, todos os métodos têm dificuldade. STP (n = 1) é o mais eficaz no ARC2-Easy e no ARC2-Challenge.
- **Métrica ΔIBC:** o benefício incremental por custo (IBC, de Aggarwal et al., 2024) é o ganho de acurácia sobre o base dividido pelo aumento de custo; compara-se o IBC da cascata com o IBC de trocar o base pelo grande, em diferença percentual. Valor maior indica mais custo-efetividade que o baseline.
- **Tabela 1 (calibrado, Qwen 1.5B → 7B, ΔIBC ± erro-padrão; ARC2-Easy / ARC2-Challenge / MMLU / MedQA / MedMCQA):**
  - Verificador base: SV n = 1: −2,4 / −11,6 / −18,7 / −27,3 / −24,8. SV n = 5: 10,2 / −26,2 / −19,4 / −25,4 / −19,5. STP n = 1: −16,9 / −19,3 / −20,4 / −23,9 / −22,9. MC-STP n = 5: −37,4 / −16,0 / −24,6 / −27,3 / −22,2.
  - Verificador grande: SV n = 1: 258,4 ± 39,1 / 70,5 ± 26,0 / −7,8 / −6,1 / −11,6. SV n = 5: 188,5 / 51,0 / −24,1 / −11,9 / −11,0. STP n = 1: 242,7 ± 36,3 / 89,3 ± 26,2 / 2,5 ± 5,2 / 1,7 ± 16,3 / −10,0 ± 10,1. MC-STP n = 5: 171,4 / 39,2 / −22,4 / −16,8 / −19,7.
  - Verificar com o grande dá ΔIBC maiores de forma consistente, sobretudo em ARC2-Easy, ARC2-Challenge e MMLU. Nos médicos, nenhum método supera os outros de forma significativa, e os autores escrevem que ali os ΔIBC com o grande como verificador "are around 0, indicating no cost-benefit".
- **Sem calibração (apêndice, Tabela 2):** segundo os autores, os escores não calibrados parecem dar ΔIBC maiores, mas com erro-padrão bem mais alto, o que eles leem como instabilidade (por exemplo, STP n = 1 com o base como verificador: −100,0 ± 948,0 no ARC2-Easy; com o grande: 284,5 ± 40,4).
- **Tamanho do conjunto de calibração (apêndice C.5, Tabela 7, STP n = 1):** com 50, 100, 200 e 500 amostras, nenhum tamanho é significativamente melhor (Qwen no ARC2-Easy: 239,5; 242,7; 273,5; 254,9). Com conjunto pequeno demais, houve mais cadeias divergentes na amostragem da regressão logística bayesiana.
- **Por matéria do MMLU (apêndice C.6, Tabelas 8 e 9):** diferença grande entre áreas, com erros-padrão grandes. Qwen: média de todas as matérias 2,52 ± 5,23; topo Direito Internacional 58,66 ± 89,93; fundo Virologia −25,63 ± 35,75. Llama (1B → 8B): média −1,16 ± 2,87; topo Religiões do Mundo 35,95 ± 35,25; fundo Fatos Globais −35,32 ± 36,23.
- **Outras cascatas (apêndice C, Tabelas 3 a 6):** Llama 1B → 8B calibrado, STP n = 1 com o grande: 118,3 ± 15,8 no ARC2-Easy, 38,1 ± 13,7 no ARC2-Challenge, −1,2 ± 2,9 no MMLU, 5,6 ± 9,7 no MedQA, −3,7 ± 9,2 no MedMCQA. Nas cascatas Llama 3B → 8B e Qwen 3B → 7B o MMLU foi omitido pelo tamanho e custo; no Llama 3B → 8B, STP n = 1 com o grande como verificador dá, no ARC2-Easy, 331,9 ± 287,7 sem calibração e 77,0 ± 112,2 com calibração.

## Melhora online do sistema (seção 5.2, D3)

- **Simulação:** 1.000 perguntas inéditas em ordem aleatória, como tráfego de produção. Antes da primeira, as probabilidades de delegação vêm da calibração nas 100 amostras. Depois, as perguntas marcadas para abstenção e respondidas por um especialista oráculo vão para um buffer de repetição, usado em atualizações do otimizador Adam sobre o risco diferenciável (taxa de aprendizado 0,05, lote de 10) nos limiares θ = {φ_base, ξ_base, ξ_large}. A previsão é feita na pergunta inédita e o arrependimento é calculado nela; ao entrar no buffer, a amostra vira treino e não é avaliada de novo. Compara-se a cascata com só o base e só o grande, cada um com um único limiar de abstenção.
- **Métrica, arrependimento acumulado:** a soma corrente do risco por pergunta. Como erro, computação e passagem ao humano já estão na mesma unidade, somá-los no tempo dá, nas palavras dos autores, a "conta" exata que o sistema pagou; curva mais baixa é melhor, e ela mostra quão rápido a política aprende e se os erros iniciais são compensados.
- **Parâmetros:** limiares iniciais {0,5; 0,05; 0,05} (ξ = 0,05 corresponde a desvio-padrão de 5% de confiança); verificação por STP (n = 1), o mais competitivo na seção anterior; λ_c = 10⁻⁵ e λ_a = 0,1, para evitar soluções triviais (como escolher sempre um modelo), em linha com Zellinger et al. (2025).
- **Resultado (Figura 4):** a cascata tem arrependimento acumulado menor que cada modelo sozinho em ARC2-Easy, ARC2-Challenge, MMLU e MedMCQA. No MedQA o ganho é menos claro, o que os autores atribuem, com "likely", à estimativa de confiança ruim já vista na seção anterior. Tendências parecidas nas outras cascatas (Figuras 9, 12 e 15).
- **Gradiente contra busca em grade (apêndice C.7, ARC2-Easy, Qwen 1.5B → 7B):** a busca em grade testa cada parâmetro numa lista de dez valores (impressa como 0.5, 0.15, 0.25, …, 0.95); a complexidade é cúbica e cresce com o buffer, ficando muito cara em relação ao gradiente. A abordagem por gradiente teve arrependimento acumulado menor, tanto nos modelos sozinhos quanto na cascata (Figura 16).

## Especialista imperfeito (seção 5.3)

Na perda, as anotações humanas erradas afetam a correção esperada, pelas confianças calibradas Φ_base e Φ_large: quanto mais ruidoso o retorno, mais descalibradas elas ficam e menos confiável a otimização. No experimento, inverte-se de 0% a 100% (0, 20, 50 e 100%) dos rótulos durante a calibração, no ARC-Easy com Qwen 1.5B → 7B. Quanto maior a corrupção dos rótulos, maior o arrependimento acumulado em uso (Figura 5).

## Limites declarados (seção 6)

- Sensibilidade a variações de custo e de abstenção pode levar a soluções triviais (só o modelo mais barato ou só o de menor erro).
- Diferenças de desempenho ou de custo relativo entre os modelos podem levar a dependência excessiva de um modelo e reduzir a adaptabilidade.
- A inicialização dos parâmetros afeta a convergência da política de delegação.
- O arcabouço depende de retorno humano, que pode atrapalhar a adaptação se for escasso ou ruidoso no mundo real.
- Ajustar uma regressão logística bayesiana costuma ser mais complexo que uma comum, conforme a aproximação da posterior ou a estratégia de amostragem.

## Conclusão e trabalhos futuros

A cascata supera os modelos únicos reduzindo escaladas desnecessárias e melhorando a correção em ARC2-Easy, ARC2-Challenge, MMLU e MedMCQA; no MedQA, não superou o modelo único, possivelmente pela complexidade do conjunto, segundo os autores. Trabalhos futuros declarados: investigar outros métodos de quantificação de incerteza para melhorar a abstenção, e examinar se há garantias teóricas que justifiquem cascatas de LLMs.

## Lista de verificação da NeurIPS (no fim do PDF)

Os autores declaram que o artigo é puramente empírico, sem resultados teóricos; que as tabelas e figuras trazem erro-padrão e intervalos de confiança de 95%; que todos os modelos e conjuntos usados são abertos; e que não há pesquisa com participantes humanos nem coleta por multidão.

---
