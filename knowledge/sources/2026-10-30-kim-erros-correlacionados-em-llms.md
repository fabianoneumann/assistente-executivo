---
titulo: "Correlated Errors in Large Language Models"
tipo: paper
autor: "Elliot Kim, Avi Garg, Kenny Peng, Nikhil Garg"
url: "https://arxiv.org/abs/2506.07962"
publicado_em: 2025-06-09
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, correlated-errors, model-heterogeneity, self-preference, algorithmic-monoculture, multi-agent, benchmark]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 09/06/2025, a única versão e a lida. O comentário do arXiv diz "Accepted to ICML 2025", e o PDF traz o rodapé dos Proceedings da 42ª ICML (Vancouver, PMLR 267). Cornell University (Kim, Peng e N. Garg) e pesquisador independente (A. Garg); os três primeiros com contribuição igual. O integral foi extraído do PDF; a Tabela 1 saiu embaralhada na extração e foi lida na versão HTML do arXiv. Lida (camadas flexíveis de avaliação).

## O resumo

Supõe-se que a diversidade de dados de treino, arquitetura e fornecedor reduz a homogeneidade entre LLMs, mas falta evidência empírica de que LLMs diferentes diferem de fato. Os autores avaliam mais de 350 LLMs em dois placares públicos e numa tarefa de triagem de currículos. Acham correlação substancial nos erros: num dos placares, quando os dois modelos de um par erram, eles escolhem a mesma resposta errada 60% das vezes. Arquitetura e fornecedor em comum aumentam a correlação, mas modelos maiores e mais precisos têm erros muito correlacionados mesmo com arquiteturas e fornecedores distintos. Mostram os efeitos em duas tarefas: avaliação com LLM como juiz e contratação, esta conferindo previsões teóricas sobre monocultura algorítmica.

## 1. Introdução: as três perguntas

LLMs entram cada vez mais em sistemas de vários agentes em situações de alto risco, e há muitos modelos de muitos fornecedores (um placar do HuggingFace tem mais de 2.000). A diversidade, em tese, ajuda: em mercados de trabalho, empresas com modelos diferentes reduziriam a exclusão sistêmica; sistemas com vários modelos seriam mais robustos ("sabedoria das multidões"). Falta saber se os modelos diferem de modo relevante. Três bases: respostas de 349 LLMs a 12.032 questões de múltipla escolha num placar do HuggingFace; 71 LLMs a 14.042 questões no placar Helm; 20 LLMs avaliando 1.800 pares currículo–vaga.

1. **Quão correlacionados são os erros?** Nas questões de múltipla escolha, mede-se a taxa de concordância de cada par **condicionada a os dois estarem errados**; nos currículos, a correlação dos resíduos em relação a rótulos humanos. Nas três bases os erros se correlacionam muito: no Helm, os pares concordam em média cerca de 60% das vezes quando ambos erram, contra 1/3 se escolhessem ao acaso entre as respostas erradas.
2. **O que explica a correlação?** Por regressão: mesmo fornecedor (empresa), mesma arquitetura de base e tamanhos parecidos aumentam a correlação; mesmo controlando esses fatores, pares de modelos mais precisos têm erros mais correlacionados. Os autores dizem que modelos novos que diferem na superfície podem estar convergindo nas saídas.
3. **Quais os efeitos a jusante?** No juiz LLM, a correlação afeta muito a avaliação quando outro modelo faz as vezes de gabarito: o juiz infla a acurácia de modelos menos precisos que ele, sobretudo os do mesmo fornecedor ou arquitetura. Na contratação, quantificam como a correlação entre empresas afeta quem é contratado (comparado a rótulos manuais de adequação) e o bem-estar dos candidatos.

## 2. Trabalhos relacionados

- **Uso de vários modelos:** muita literatura supõe, explícita ou implicitamente, que usar LLMs diferentes é melhor que usar o mesmo; por exemplo, para evitar autopreferência, muitos trabalhos usam um LLM separado para avaliar. Raghavan (2024) modela um jogo em que convém ser preciso e diferente dos outros, e acha que aumentar o ruído (temperatura) e escolher um LLM diferente dos concorrentes pode ser preferível a usar o agente individualmente mais preciso. O artigo se apresenta como base empírica para essa literatura.
- **Monocultura algorítmica e exclusão sistêmica:** quando muitos decisores usam o mesmo modelo; na contratação, a monocultura pode prejudicar as empresas correlacionadas, e há a exclusão sistêmica (um trabalhador rejeitado em todas as vagas porque todas usam o mesmo algoritmo). Peng e Garg (2024a) argumentam que a monocultura pode beneficiar os candidatos em média, porque quem recebe ofertas tem mais poder de escolha.
- **Ecossistema:** a hipótese do compartilhamento de componentes (modelos com componentes em comum têm saídas mais correlacionadas); o artigo pode ser lido em parte como teste dela em larga escala.
- **Diversidade gerativa:** Wu et al. (2024) acham monocultura forte dentro de um mesmo LLM, não atenuada por temperatura, top-p ou prompt, e pior com ajuste por RLHF. Este artigo mede a monocultura **entre** LLMs: são mais correlacionados entre si do que com o gabarito, e pior dentro da mesma empresa e entre modelos maiores; "usar vários modelos diferentes não é panaceia".
- **Trabalhos concorrentes:** Wenger e Kenett (2025), em tarefas criativas, acham respostas de LLMs muito mais parecidas entre si do que as de humanos entre si. Goel et al. (2025) criam uma métrica de semelhança que ajusta pela acurácia, conta respostas erradas diferentes como discordância e usa a distribuição de probabilidade das opções; a métrica deste artigo (concordar quando ambos erram) cumpre os dois primeiros critérios, mas não usa probabilidades. Goel et al. também acham que modelos mais capazes erram de modo mais parecido; este artigo acrescenta outros correlatos (desenvolvedor, arquitetura de base, tamanho) e o foco em efeitos a jusante, como a contratação.
- Trabalhos sobre homogeneidade das representações (embeddings traduzíveis entre modelos; ativações consistentes em profundidades parecidas) sugerem, para os autores, uma explicação mecanicista dos resultados.

## 3. Erros correlacionados

### 3.1 Dados e método

- **Múltipla escolha:** placar Open LLM Leaderboard 2 do HuggingFace e Helm (Stanford), ambos com questões do MMLU e respostas corretas rotuladas, com a resposta de cada modelo a cada questão. De cada modelo extraem fornecedor e acurácia; no HuggingFace, também número de parâmetros e arquitetura de base (disponíveis por serem modelos abertos). Esses atributos não estão disponíveis de forma consistente no Helm e nos currículos, onde muitos modelos são fechados.
- **Currículos:** de bases de vagas (Upwork, 53.058 anúncios) e currículos (LiveCareer e um repositório público), escolheram 30 descrições de vaga e 60 currículos por análise de clusters (embeddings SBERT e KMeans com 28 clusters; três pares de clusters vaga–currículo bem parecidos: TI geral, desenvolvimento web, consultoria/finanças), dando 1.800 pares avaliados por 20 LLMs (Meta, Mistral AI, Amazon, Anthropic, OpenAI) com nota de 1 a 10 de adequação, por dois prompts (o principal com critérios explícitos de adequação geral, de área e de habilidades, e uma escala descrita). Rotularam à mão 450 pares (30 currículos e 15 vagas) com os mesmos critérios.
- **Medida do erro correlacionado:** no HuggingFace e no Helm, a **taxa de concordância quando os dois erram**: quando dois modelos erram, com que frequência a resposta errada coincide. Nos currículos, a correlação dos resíduos (nota do modelo menos nota humana), tratando a nota humana como gabarito, com a ressalva de que a adequação é subjetiva. As medidas tentam tirar o efeito da acurácia: dois modelos precisos e independentes concordariam em muitas questões que ambos acertam, e o interesse aqui são os erros. Os apêndices trazem medidas alternativas (concordância geral, concordância quando um dos dois erra).

### 3.2 Resultados

- **Os modelos concordam muito mesmo errando.** Com respostas ao acaso entre as erradas, a concordância seria 1/3 no Helm (quatro opções) e 0,127 no HuggingFace (entre 3 e 10 opções; mais de 80% das questões com 10). Quase todos os pares ficam acima dessas linhas de base: 100% no HuggingFace e 97,5% no Helm. A concordância média entre pares é 0,423 no HuggingFace e 0,6 no Helm, cerca do dobro ou mais das linhas de base (Figura 1, em que os modelos estão ordenados por acurácia e os mais precisos aparecem mais correlacionados).
- **Alguns pares concordam muito mais.** No Helm, llama-3.2-90b-vision-instruct-turbo e llama-3.1-70b-instruct-turbo concordam em 0,97 quando ambos erram, o que bate com o modelo de visão ser baseado no modelo só de linguagem. Outros são inesperados: google/text-unicorn@001 e writer/palmyra-x-v3 concordam em 0,9987 das questões em que ambos erram (cerca de 22% de todas as questões), e os autores não conhecem relação pública direta entre os dois.
- **Fontes da correlação (Tabela 1,** regressão da concordância nos erros de cada par sobre atributos dos modelos, atributos numéricos padronizados):

| Variável | HuggingFace | Helm | Currículos |
|---|---|---|---|
| Intercepto | 0,398 | 0,602 | 0,653 |
| Mesma empresa | 0,066 | 0,022 | 0,021 (não significativo, p = 0,092 no apêndice) |
| Mesma arquitetura | 0,076 | não disponível | não disponível |
| Acurácia do modelo 1 | 0,014 | 0,055 | 0,015 |
| Acurácia do modelo 2 | 0,013 | 0,054 | 0,028 |
| Interação das acurácias | 0,023 | 0,026 | 0,043 |
| Modelos / respostas por modelo | 349 / 12.032 | 71 / 14.042 | 20 / 1.800 |
| R² | 0,340 | 0,613 | 0,415 |

Os coeficientes marcados são significativos a p < 0,001. Nos currículos, a variável dependente é a correlação dos resíduos, e a "acurácia" é a correlação de cada modelo com a nota humana. Mesmo desenvolvedor, mesma arquitetura de base e tamanhos parecidos se associam a concordância maior; modelos mais precisos, e sobretudo pares em que os dois são precisos, são mais correlacionados. Os atributos explicam entre 34% e 62% da variação. Conclusão dos autores: (a) há erro correlacionado substancial em LLMs; (b) ele é mais forte entre modelos mais precisos e com atributos em comum.

## 4. Estudo de caso: LLM como juiz

Um modelo julga as respostas dos outros, e a acurácia de cada modelo é calculada pelas respostas do juiz como se fossem o gabarito. Juízes escolhidos como o modelo mais preciso dentro de um fornecedor (Helm) ou arquitetura (HuggingFace). A Figura 2 (Helm) põe a acurácia real no eixo x e a **inflação** (acurácia julgada menos real) no eixo y; modelos do mesmo fornecedor ou arquitetura em vermelho.

- Cada juiz **infla sistematicamente a acurácia de modelos menos precisos que ele**, por causa dos erros correlacionados: marca como certa uma resposta errada quando os dois concordam nela.
- Cada juiz **subestima a acurácia de modelos mais precisos que ele**: não consegue premiar um acerto numa questão que ele próprio erra.
- Há casos de inflação forte de modelos do mesmo fornecedor, ligados à autopreferência, o que para os autores sugere que a autopreferência relativa pode ocorrer entre modelos diferentes da mesma família.
- A conclusão que tiram: ao comparar modelos ou estabelecer taxas de erro com LLM como juiz, é importante calibrar as métricas de erro para cada par modelo–juiz com dados de gabarito. O apêndice B.1 (Figura 8) mostra o mesmo padrão no HuggingFace.

## 5. Estudo de caso: LLMs no mercado de trabalho

Contratação é apontada como cenário em que a homogeneidade (monocultura algorítmica) pode ter efeitos negativos, além das preocupações com vieses. Os autores testam previsões teóricas com currículos e vagas reais e LLMs, em vez de modelos tabulares clássicos. Cinco cenários de como as empresas ordenam os candidatos, da monocultura total à policultura total:

1. **Mesmo LLM** para todas as empresas (um modelo domina, por exemplo por um prestador comum).
2. **LLM da mesma empresa:** cada firma sorteia um LLM de um mesmo fornecedor (um fornecedor monopoliza).
3. **LLM mais recente:** cada firma usa um dos modelos mais recentes de cada fornecedor (Llama 3.3 70B, Mistral Large 24.07, Nova Pro, Claude Sonnet de 22/10/2024, GPT-4o mini).
4. **LLMs aleatórios:** cada firma sorteia um LLM do conjunto.
5. **Uniformemente aleatório:** preferências das firmas ao acaso, sem relação com a adequação (decisões não correlacionadas).

### 5.1 Exclusão sistêmica

Um candidato é sistemicamente excluído se não recebe entrevista de nenhuma firma; cada firma entrevista o quartil superior (p = 0,25) e todas usam a mesma descrição de vaga. A taxa é a fração de candidatos que nenhuma firma entrevista.
- Com preferências ao acaso, a taxa tende a zero com o número de firmas (seria 0,75 elevado ao número de firmas). Com cada firma usando um LLM aleatório, **mesmo com 20 firmas cerca de 20% dos candidatos continuam excluídos** (Figura 3a), consequência da correlação geral entre LLMs. Os autores notam que algum nível de exclusão pode ser aceitável se alguns currículos não servem mesmo para a vaga.
- Entre os cinco cenários (Figura 3b, média de 1.500 mercados), firmas que adotam modelos da mesma empresa ou os mais recentes têm exclusão um pouco maior que com LLMs aleatórios, diferenças pequenas perto do cenário em que todas usam o mesmo LLM; a exclusão cai da monocultura para a policultura.
- A taxa não considera a adequação real, a capacidade (cada candidato só trabalha numa firma) nem as preferências dos candidatos; daí a análise seguinte.

### 5.2 Efeitos de mercado com emparelhamento estável

Mercados com 60 candidatos e 30 firmas (ou o subconjunto com rótulos manuais), cada firma contrata no máximo um e cada candidato aceita no máximo uma oferta; preferências dos candidatos pelas firmas ao acaso (o apêndice B.2 repete com preferências dadas pelo Llama 3.1 405B). Três previsões de Peng e Garg (2024a):

- **Resultado das firmas** (Figura 4, subconjunto de 30 candidatos e 15 firmas com adequação avaliada por humanos): usar o mesmo LLM dá o pior resultado para as firmas, com menor probabilidade de emparelhar os candidatos de nota real mais alta. Usar os LLMs mais recentes, que são individualmente os mais precisos e também mais correlacionados que LLMs aleatórios, **maximiza** o resultado das firmas. Os autores leem dois efeitos concorrentes, como em Raghavan (2024): acurácia individual e diversidade; a diversidade de LLMs pode não produzir uma sabedoria das multidões que supere escolher os melhores modelos.
- **Resultado dos candidatos** (Figura 5a, posição média da firma conseguida na lista de preferência do candidato): o mercado com um só LLM dá a melhor posição média, e o bem-estar dos candidatos piora na direção da policultura. É a tendência oposta à da exclusão sistêmica, como previsto: os mercados com mais exclusão dão os emparelhamentos de maior qualidade para os candidatos, um dilema entre exclusão (sem efeitos de mercado) e bem-estar dos candidatos (com eles). Os cenários de modelos correlacionados ficam entre o mesmo LLM e o LLM aleatório.
- **Acesso desigual às candidaturas** (Figura 5b): cada candidato se candidata a um número sorteado de firmas, de 1 a 30. A probabilidade relativa de emparelhar cresce com o número de candidaturas, em ritmos diferentes: com preferências ao acaso, quem manda 30 candidaturas tem cerca de 7 vezes mais chance que quem manda 1; com o mesmo LLM, cerca de 2 vezes. Bate com a hipótese de que a monocultura total é mais robusta ao acesso desigual, porque mais candidaturas dão menos "bilhetes de loteria" independentes.
- No apêndice B.2, com preferências dos candidatos dadas pelo Llama 3.1 405B, a posição média piora em geral (as preferências ficam mais correlacionadas) e adotar vários LLMs não parece melhorar significativamente a posição em relação às preferências ao acaso; os padrões relativos se mantêm.

## 6. Conclusão, limites e trabalhos futuros

- LLMs têm erros correlacionados, muito mais entre modelos individualmente precisos e entre os do mesmo desenvolvedor ou mesma arquitetura de base. Para os autores, os achados sugerem que, com o desempenho subindo, os modelos convergem nos erros, com implicações para o LLM como juiz, para a contratação e para sistemas de vários agentes em geral.
- **Medida de correlação:** como a de Goel et al. (2025), a concordância quando ambos erram corrige pela acurácia; a de Goel et al. também usa as concordâncias nos acertos e as probabilidades de saída, e pode ser preferível quando elas existem. Os apêndices repetem com concordância geral e concordância quando um dos dois erra, com resultados parecidos (R² de 0,451 e 0,300 no HuggingFace; 0,865 e 0,406 no Helm). Limite declarado das métricas atuais, inclusive a deles: tratam todas as respostas erradas como iguais, quando algumas podem estar "mais perto" do certo e ser preferidas por modelos mais precisos, e algumas questões são mais difíceis; trabalho futuro deveria desenvolver uma métrica robusta a isso.
- **Medição de desempenho de vários agentes:** avaliar saída de LLM é questão contestada, sobretudo em sistemas de vários agentes. As medidas usadas (placares de múltipla escolha, notas numéricas de currículos, offline) dão uma visão limitada das capacidades, mas a padronização permite cobrir mais de 350 modelos e mais de 20.000 questões com gabarito. Avaliar geração aberta e raciocínio complexo fica como direção futura. O trabalho não mede as correlações induzidas por LLMs ajudando a escrever vagas ou currículos.
- **Monitoramento do ecossistema:** análises de correlação entre modelos são raras, embora possam ser feitas com os mesmos dados da avaliação individual, já que os benchmarks repetem as questões entre modelos. Os autores recomendam que os responsáveis por placares acompanhem continuamente a correlação entre modelos, que revela padrões inesperados entre pares e indica quais modelos podem funcionar melhor juntos. Leis como a Local Law 144 de Nova York exigem auditoria de algoritmos de contratação, mas análises empíricas de correlação entre modelos ou de várias empresas compartilhando algoritmos são pouco exploradas.
- **Declaração de impacto:** a análise se limita a um subconjunto de tarefas em que a homogeneidade preocupa e serve de base para avaliação e monitoramento do ecossistema.

## Apêndices: o que acrescentam

- **A. Construção dos dados.** No HuggingFace, dos 2.041 modelos originais, partiram dos 500 mais precisos, acharam 451 com dados do MMLU bem estruturados pela API e ficaram com todos os modelos de grandes desenvolvedores e até cinco por pessoa que ajusta modelos de outros (os mais precisos), dando 349; a análise par a par escala com o número de questões vezes n(n−1)/2. O Helm tinha 71 modelos de 15 empresas (entre elas OpenAI, Anthropic, Google, DeepSeek, Qwen), com perguntas de quatro opções e o modelo instruído a escolher uma; o MMLU do HuggingFace tem 12.032 questões de 91 conjuntos e 14 categorias, a maioria com 10 opções, e a resposta é a opção mais bem ranqueada pelo modelo. Os currículos passaram por remoção de duplicatas e dos textos muito curtos antes do clustering.
- **B. Mais análises.** No HuggingFace, o juiz infla do mesmo modo (Figura 8). Nos currículos, as notas e os resíduos de modelos maiores da mesma empresa são fortemente correlacionados (Figura 9); a correlação entre os dois prompts foi forte e os mapas usam só o prompt principal.
- **C. Regressões completas.** No HuggingFace entram também ser de mistura de especialistas (não significativo), log do número de parâmetros e geração (positivos e pequenos) e diferença de tamanho (−0,0215: tamanhos mais distantes, menos concordância nos erros), com 60.726 pares. No Helm, 2.485 pares. Nos currículos, 190 pares; mesma empresa não é significativa na correlação dos resíduos (0,021, p = 0,092), mas é na concordância das notas (0,034, p < 0,001; R² 0,896); ser o modelo mais recente não é significativo.
- **D. Lista de modelos** de cada base, com a correlação de cada modelo de currículos com a nota humana (por exemplo, Nova Pro 0,73, Nova Micro 0,64).

---
