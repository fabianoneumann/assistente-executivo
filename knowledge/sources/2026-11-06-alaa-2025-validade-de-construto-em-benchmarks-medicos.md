---
titulo: "Medical Large Language Model Benchmarks Should Prioritize Construct Validity"
tipo: paper
autor: "Ahmed Alaa, Thomas Hartvigsen, Niloufar Golchini, Shiladitya Dutta, Frances Dean, Inioluwa Deborah Raji, Travis Zack"
url: "https://arxiv.org/abs/2503.10694"
publicado_em: 2025-03-12
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [construct-validity, content-validity, criterion-validity, benchmarks, medical-llm, llm-evaluation, medqa, electronic-health-records, validity-theory, psychometrics]
licenca: "CC BY 4.0, em arxiv.org/abs/2503.10694"
---

# Alaa e outros 2025 (arXiv): benchmarks de LLM médicos deveriam priorizar a validade de construto

Ficha na ordem do artigo. Autores da UC Berkeley, da UCSF e da Universidade da Virgínia (contribuição igual indicada para parte deles); arXiv:2503.10694v1, cs.CL, 12/03/2025. Artigo de posição em avaliação de LLM (large language model, modelo de linguagem de grande porte) médico, com experimentos de prova de conceito em dados clínicos reais. Os números da figura 1 estão impressos nela; os da figura 5 foram lidos do gráfico e levam "cerca de".

## A posição

Afirmações sobre LLM médico, de codificar conhecimento clínico a raciocinar como médico, costumam se apoiar em benchmarks competitivos, herança do aprendizado de máquina. Os autores não contestam a importância dos benchmarks (citam o ImageNet). Defendem que os de medicina sejam desenhados de propósito e avaliados de forma quantitativa quanto à validade de construto, com dados do mundo real, como o prontuário eletrônico (EHR, electronic health record). A visão: cada benchmark associado a afirmações explícitas e avaliado empiricamente por sistemas hospitalares.

**Por que o tema pesa mais na medicina.** O desempenho nesses benchmarks sugere, de modo implícito, habilidade clínica geral, e muitos adotam provas humanas como o USMLE, exame de licenciamento médico dos Estados Unidos: "real-world clinical practice bears little resemblance to these exams". As provas funcionam como proxy de prontidão humana, refinadas por décadas sobre desempenho humano e habilidades cognitivas, e os autores dizem não haver razão forte para supor que sirvam ao mesmo fim em LLM.

**A premissa.** As capacidades do LLM, como os traços psicológicos, são construtos latentes sem definição operacional, e por isso não bastam benchmarks aceitos pela validade de face, que é subjetiva.

**Figura 1, o retrato do campo.** Nos 100 artigos mais citados sobre LLM médico nos últimos cinco anos, 60% avaliam em benchmark construído e 40% em dados reais de hospital, privados ou públicos. A legenda descreve os 60% como benchmarks públicos feitos a partir de provas médicas; o apêndice A define "constructed benchmark" como dados sintéticos ou desenhados por pesquisadores. Entre os benchmarks, o mais usado é o MedQA (16,7%), seguido de PubMedQA (10,4%), MultiMedQA (8,3%) e MedMCQA (6,2%), sem consenso sobre um padrão. Apêndice A: busca no PubMed de artigos de acesso aberto, 361 encontrados, os 100 mais citados revisados à mão, classificados por fonte dos dados e por benchmark usado.

**Por que validar.** Esclarece o que a nota significa e ajuda a entender rankings que mudam de um benchmark para outro (exemplo: GPT-4 e Claude no Open Medical-LLM Leaderboard; Pal e outros, 2024). A discussão de validade é rara na literatura de ML: Raji e outros (2021) analisam qualitativamente ImageNet e GLUE, e Fang e outros (2024) testam empiricamente se o progresso no ImageNet se transfere a dados reais.

## A analogia com o teste psicológico

Teste psicológico tem cinco componentes, e cada um tem seu par em LLM (figura 2):

| Componente | Em psicologia | Em LLM |
|---|---|---|
| Sujeito | a pessoa avaliada | o modelo (GPT-4, PaLM, Claude) |
| Construto latente | traço de personalidade, habilidade cognitiva, condição de saúde mental | a capacidade (raciocínio matemático) |
| Instrumento | itens que provocam respostas | o benchmark (GSM8K, MATH) |
| Nota | medida derivada das respostas | a métrica no benchmark |
| Inferência | interpretação da nota quanto ao construto | a afirmação do pesquisador sobre a capacidade |

Como um teste de QI, que mede resolução de problemas e padrões como proxies, o benchmark mede tarefas assumidas como reflexo de "raciocinar" ou "entender". Os autores lembram Gould (*The Mismeasure of Man*) sobre o mau uso de medidas de inteligência, e perguntam se o campo está medindo mal os modelos.

## Teoria da validade

**Visão clássica, tripartite (Cronbach e Meehl, 1955).** Exemplo condutor: o Inventário de Depressão de Beck (BDI, Beck Depression Inventory).

- **Validade de critério.** O quanto o teste prevê ou correlaciona com um desfecho externo observável que representa o construto. Preditiva, quando o teste vem antes do critério; concorrente, quando os dois são medidos em período próximo. BDI: comparar com o diagnóstico psiquiátrico pelo DSM-5 ou com outras medidas (Ambrosini e outros, 1991, adolescentes, K-SADS), ou com episódios futuros (Green e outros, 2015, item de suicídio). LLM: se a nota no MedQA, feito de vinhetas clínicas e múltipla escolha, prevê a acurácia em pacientes reais, cruzando vinhetas com prontuários e códigos ICD. Paralelo nas provas médicas: Swanson e outros (1996), retenção de conhecimento; Norcini e outros (2014), notas do USMLE e sucesso profissional.
- **Validade de conteúdo.** Os itens representam o domínio de conteúdo, em geral por dedução: define-se o domínio e daí se tiram os itens. O critério sozinho pode não bastar: um BDI que preveja bem e enfatize sono e apetite, deixando de lado humor e anedonia, falha como medida. BDI: definir o universo de sintomas por DSM ou ICD e pedir a um painel que avalie; Moran (1982) achou 6 de 9 critérios do DSM-III bem capturados, 2 em parte (sono e alimentação) e 1 ausente (agitação). LLM: a medicina já tem ontologias (SNOMED, LOINC, RxNorm, ICD) e quadros educacionais (taxonomia de Bloom, pirâmide de Miller); a relevância de cada conceito se mede pela prevalência no EHR da população, e dá para ver a cobertura por tipo de paciente.
- **Validade de construto.** Entra quando o atributo não tem definição operacional, e pergunta: "What constructs account for variance in test performance?" Um teste a tem se a variação das notas entre sujeitos vem sobretudo do construto. Divide-se em convergente (correlaciona com outras medidas do mesmo construto) e discriminante (não correlaciona com construtos alheios; Campbell e Fiske, 1959). BDI: Schotte e outros (1997), análise fatorial em pacientes internados com depressão unipolar, duas dimensões, psicológico-cognitiva e somático-vegetativa, correlacionadas com biomarcador de supressão de dexametasona. LLM: o benchmark separa os modelos pela proficiência naquela habilidade; o ranking no MedQA deveria generalizar para casos reais de diagnóstico, sem precisar prever tarefas alheias como resumir texto. Rankings diferentes entre benchmarks da mesma tarefa levantam a questão.

**Visão moderna (figura 3).** Messick (1989) reúne tudo como formas de evidência da validade de construto, com a face, a preditiva, a concorrente, a convergente e a discriminante como fontes. "validation is not about the test itself but about the interpretations and applications of test scores". Cronbach acompanhou em 1989; Kane (2001, 2012) reforça; a ETS, que aplica TOEFL e GRE, adota a visão unificada nos manuais (Dorans, 2013).

## Os experimentos com o MedQA

**Objeto.** MedQA (Jin e outros, 2021), feito de questões licenciadas do USMLE, com vinheta, pergunta e alternativas. O construto que se costuma atribuir a ele: conhecimento médico. Dados reais de um grande centro médico acadêmico, sem nome no artigo. Os autores chamam os procedimentos de prova de conceito, para mostrar que a validação é viável.

### Validade de critério

**Como.** Para cada questão de múltipla escolha das seções Step 1 e Step 2, a resposta certa é classificada como droga (mapeada para RxNorm) ou diagnóstico (SNOMED). Com o código, buscam-se 10 notas de evolução médica (o apêndice diz "approximately 10") em que aquilo aparece na seção "Assessment and Plan". No formato SOAP, retira-se o "Plan" para evitar viés, e o resto da nota vai ao modelo com a pergunta e as alternativas originais.

**Métrica.** α = P(acerto no caso real | acerto no MedQA), a acurácia em casos reais parecidos com as vinhetas que o modelo acertou. Com validade de critério perfeita, α tenderia a 1.

**Tabela 1:**

| Modelo | Acurácia no MedQA | Acurácia nos dados reais | α |
|---|---|---|---|
| Llama 3 | 0,54 | 0,48 | 0,56 |
| GPT-4 | 0,71 | 0,28 | 0,29 |
| Chimera Llama | 0,60 | 0,45 | 0,48 |
| Biomerge | 0,57 | 0,36 | 0,49 |
| Orpomed | 0,49 | 0,24 | 0,38 |
| JSL MedLlama | 0,61 | 0,37 | 0,49 |
| PMY MedLLama | 0,75 | 0,36 | 0,45 |

O texto também nomeia OpenBioLLMC como avaliado, e o apêndice, GPT-3.5, e nenhum dos dois tem linha na tabela.

**Leitura dos autores.** Correlação modesta (sem coeficiente no artigo); α pouco acima da acurácia geral em dados reais; acertar a questão não prevê com força o desempenho real em decisões parecidas; a acurácia cai em geral ao passar para os casos reais.

**Efeito do número de alternativas (figura 5, esquerda).** A acurácia cai em todos os modelos quando as alternativas aumentam, de 2 a 7. Cerca de 0,94 a 0,87 no GPT-4o, com leve alta em 3 alternativas; 0,94 a 0,76 no GPT-4; 0,94 a 0,70 no GPT-4o-mini; 0,86 a 0,76 no Llama 3.3; 0,78 a 0,47 no GPT-3.5-Turbo. O apêndice C.1 diz que testaram por modelo, conjunto de dados (MedQA de 4 opções, MedMCQA e subconjuntos do MMLU) e perturbação, sem detalhar o procedimento dela.

**Explicações que os autores levantam.** O formato artificial do MedQA, com alternativas que a prática clínica não dá; vinhetas idealizadas contra notas cheias de ruído; casar paciente pela resposta certa pode não medir similaridade clínica. Propõem que pesquisadores e clínicos definam juntos um padrão de "clinical similarity".

### Validade de conteúdo

**Como.** O domínio de conteúdo é definido por dois eixos. Conceitos: UMLS (Unified Medical Language System, ontologia que integra SNOMED, MeSH, LOINC, RxNorm e ICD), extraídos com cTAKES das 1.273 questões do MedQA e das notas clínicas. Tarefas: cada questão e cada nota é classificada em uma de 15 categorias por um prompt padronizado, usando uma amostra de 100 notas de internação e 100 ambulatoriais, só com a seção "Assessment and Plan".

Categorias: diagnóstico; fato médico; pergunta geral sobre droga; pergunta geral sobre doença; tratamento ou manejo; interação de drogas; efeitos colaterais; pergunta sobre procedimento; pergunta sobre teste ou medida; mecanismo de ação; definição; eficácia de tratamento; segurança de tratamento; uso em populações específicas; ética médica.

**Resultados (figura 5, meio e direita).**

- **Tarefas:** o MedQA cobre várias e pende para o diagnóstico: cerca de 44 questões de diagnóstico contra cerca de 25 de tratamento ou manejo; nas notas reais, cerca de 50 de tratamento ou manejo em cada ambiente, contra cerca de 23 (internação) e 40 (ambulatório) de diagnóstico. Mecanismo de ação, cerca de 11 no MedQA, quase não aparece nas notas. O artigo não dá o tamanho da amostra do MedQA nesse painel.
- **Conceitos:** vinhetas do MedQA com mediana e média perto de cerca de 30 conceitos; prontuário com mediana de cerca de 65 e média de cerca de 95, e cauda até cerca de 580. O texto escreve "USMLE concepts" nessa passagem; a figura e o método falam em UMLS.

**Leitura dos autores.** As vinhetas são enxutas de propósito, e o prontuário traz muito detalhe irrelevante à decisão; o domínio do MedQA é bem mais simples que a prática, e isso poderia explicar a validade preditiva fraca, já que LLMs se distraem (Shi e outros, 2023; Hager e outros, 2024).

**Método à parte (C.3.1).** Com um médico, identificaram as seções do prontuário que importam; o GPT-4o estruturou cada questão em JSON com "Patient History" e "Objective", e o cTAKES rodou em cada seção, para ver a distribuição dos conceitos por seção.

### Validade de construto

**Como.** Comparar o ranking no benchmark com o ranking na tarefa real. O artigo não calcula correlação de postos.

**Resultado.** Llama 3 lidera nos dados reais (0,48). O texto diz que o GPT-4 lidera no MedQA; na tabela 1, o maior valor é o do PMY MedLLama (0,75), à frente do GPT-4 (0,71). O GPT-4 teve taxa alta de não resposta nas notas reais, sem número no artigo, o que dificulta a interpretação.

**Outros caminhos, propostos e não executados.** Análise fatorial (Kang, 2013), comparando desempenho por categoria do benchmark e da tarefa real. Pedir raciocínio passo a passo e conferir com clínicos: acertar com raciocínio errado pode indicar padrão estatístico em vez de compreensão.

## A proposta: validar o benchmark antes do modelo

Benchmarks passariam a ser testes estruturados, com construto, domínio de conteúdo e critérios de validade definidos, à maneira de um estudo clínico, que avalia uma intervenção (construto) numa população (conteúdo) contra desfechos medidos (critérios).

- **O que falta hoje, segundo eles:** conjuntos ad hoc, métricas soltas e populações sem relevância clara. O MedQA não especifica doença, população ou demografia. Nenhum benchmark da figura 1 foi desenhado com modelo teórico das capacidades. Goodman e outros (2024) mostram que ROUGE não reflete a qualidade de resumo clínico.
- **Por que não só dados reais:** benchmarks com dados reais, como MedHELM, também têm escolhas de desenho a examinar, e hospitais relutam em compartilhar dados por privacidade.
- **O ecossistema:** hospitais validariam localmente benchmarks públicos e reportariam notas de validação, sem compartilhar dados brutos. Haveria leaderboards de benchmarks; os de modelos priorizariam os mais validados, e desenvolvedores escolheriam os endossados pelos sistemas de saúde do seu contexto.

## Visões alternativas que os autores registram

- **Medicina muda** (populações, novas drogas; Finlayson e outros, 2021): benchmark estático perde relevância e pode criar ilusão de progresso.
- **Utilidade clínica** (Hager e outros, 2024; Bossuyt e outros, 2012, em testes diagnósticos): medir o efeito na decisão clínica.
- **Simuladores de conversa** (Mehandru e outros, 2024; Johri e outros, 2025): LLM visto como agente, avaliado de forma dinâmica.

Resposta deles: benchmark deve seguir como o meio de menor atrito para reproduzir e avaliar; utilidade clínica exige modelo embutido num sistema de saúde, inviável para a maioria; avaliação adaptativa e simulação também são testes construídos, e a questão de validade permanece.

## Limites que aparecem no artigo

Posição com experimentos de prova de conceito, num único benchmark e num único centro médico. Os autores admitem que casar por resposta certa pode não medir similaridade clínica. O artigo não relata coeficiente de correlação, intervalo de confiança ou teste de significância para a tabela 1, nem o tamanho da amostra de notas usada, além das 10 por questão. A versão lida é a v1 do arXiv, e o texto não indica revisão por pares.

## Tudo o mais que ensina

- Poucos estudos fazem ensaio clínico randomizado com desfechos reais (Li e outros, 2023; Brodeur e outros, 2024); a maioria fica no benchmark.
- Parte da crítica a benchmarks já é, sem o nome, trabalho sobre validade de construto. Exemplo: Johri e outros (2025), conversas simuladas em vez de vinhetas, porque anamnese e pergunta aberta contam.
- Os autores oferecem a teoria da validade como quadro geral para discutir, avaliar e construir benchmarks, em vez de consertos caso a caso.
- ImageNet tem afirmações de baixa consequência, comparado ao que uma nota médica sugere.
- SAT e bar exam são os outros exemplos de prova como proxy de prontidão humana.
- Exemplos de testes cuja validade já foi estudada: Big Five (Barrick e Mount, 1991), Stanford-Binet (Laurent e outros, 1992), BDI (Richter e outros, 1998).
- Prompt da classificação de tarefas: pede a categoria que melhor caracteriza a tarefa principal do médico na nota, com resposta no formato "[Number: Category]".
