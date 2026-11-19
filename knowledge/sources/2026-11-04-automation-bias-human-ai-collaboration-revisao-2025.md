---
titulo: "Exploring automation bias in human–AI collaboration: a review and implications for explainable AI"
tipo: paper
autor: "Giuseppe Romeo, Daniela Conti"
url: "https://link.springer.com/article/10.1007/s00146-025-02422-7"
publicado_em: 2025-07-03
capturado_em: 2026-11-04
licenca: "Creative Commons Attribution 4.0 International (CC BY 4.0), escrita no PDF e na página do artigo ('This article is licensed under a Creative Commons Attribution 4.0 International License'); o integral está na url"
areas: [agent-engineering]
tags: [automation-bias, overreliance, human-ai-collaboration, trust-calibration, explainable-ai, anchoring, cognitive-forcing-functions, literature-review, reliance-measures]
---

# Romeo e Conti 2025 (AI & Society): viés de automação na colaboração humano-IA, revisão de 35 estudos

Ficha em palavras próprias; o texto integral (CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Revisão publicada online em 3/7/2025, na seção Open Forum da AI & Society, vol. 41, pp. 259–278 (edição de janeiro de 2026; recebida em 13/3/2025, aceita em 2/6/2025; DOI 10.1007/s00146-025-02422-7). Lida na página do artigo e no PDF em 2026-11-04.

## O que é

Revisão de literatura pelo PRISMA 2020, feita na Universidade de Catânia, sobre como o viés de automação aparece em ambientes de trabalho com IA e que mecanismos cognitivos o influenciam. Os autores dizem que as revisões anteriores (Goddard 2012; Lyell e Coiera 2017) tratavam de apoio computacional tradicional, não de IA.

Cinco perguntas: (1) que fatores causam ou medeiam o viés; (2) ele ocorre junto com outros vieses; (3) explicação ou transparência o reduzem; (4) letramento em IA ou modelo mental melhor são necessários para reduzi-lo; (5) há diferenças individuais.

## Como foi feita

- **Bases e data:** Scopus, ScienceDirect, PubMed e Google Scholar, em maio de 2025. No PubMed, 31 resultados, 3 incluídos depois da leitura integral; no Scholar, 17; no Scopus, 1. O artigo traz as consultas de cada base e diz que a do PubMed foi testada contra cinco estudos de referência. Somam-se listas de referências e arquivos pessoais, declarados como "outras fontes".
- **Critérios:** revisados por pares, de janeiro de 2015 a abril de 2025, em inglês, quantitativos e experimentais, sobre viés de automação ou confiança excessiva. Fora: preprints, anais, teses, revisões, qualitativos, estudos de aceitação ou calibração de confiança sem viés de automação, e desenvolvimento técnico de IA ou viés algorítmico sem relação com ele.
- **Seleção:** dois pesquisadores independentes, com κ de Cohen de 0,95; divergências resolvidas em reunião.
- **O conjunto:** 35 estudos em 21 periódicos, 19.774 participantes. Saúde é o domínio mais frequente (n = 11; 31,4%), depois segurança nacional (5), finanças (3), administração pública (3), RH (2) e saúde mental (2). 2023 e 2024 têm 10 estudos cada (28,5%). Medida principal: desempenho objetivo, como acerto diagnóstico ou qualidade da decisão.

## Como o viés é medido

Sobre a medida, a frase é: "agreement with incorrect AI recommendations was the most used operational measure of AB" (exemplo: Buçinca 2021). A revisão não dá a contagem de quantos estudos a usam. Outras duas: quantas vezes a pessoa troca a resposta inteira pela da IA (Horowitz e Kahn 2024) e o peso do conselho, WOA (Küper 2025).

## Definições que a revisão adota

- **Viés de automação:** favorecer a recomendação automatizada contra o próprio julgamento, mesmo com informação contraditória e mais correta à mão (Cummings 2004). Gera dois tipos de erro: de comissão (agir pela sugestão errada sem conferir) e de omissão (não agir porque o sistema não avisou) (Wickens 2021).
- **Complacência de automação:** a literatura diverge se é fenômeno distinto; os autores tratam os termos como intercambiáveis, "for simplicity".
- **Calibração da confiança:** alinhar a confiança à capacidade real do sistema, para evitar o mau uso (confiar além da capacidade) e o desuso (aversão ao algoritmo). A confiança é tomada de Lee e See 2004; confiança apropriada é seguir quando a IA acerta e não seguir quando erra.
- **Três confianças:** como traço (disposição), como estado (situacional) e aprendida (Duan 2024).
- **Revisões anteriores:** experiência e confiança em si protegem; carga, complexidade da verificação e tempo agravam. Alta precisão do sistema pode, paradoxalmente, aumentar a confiança e o viés (Lyell e Coiera 2017).

## O que os estudos acharam

**Experiência protege, sem imunizar.** Com diagnóstico automático incorreto, o acerto caiu de 84,86% para 41,66% entre os 15 fellows de cardiologia e de 86,38% para 27,43% entre os outros 15 médicos (Bond 2018, ECG). Em mamografia, com sugestão errada, de 79,7% para 19,8% (pouca experiência), 81,3% para 24,8% (moderada) e 82,3% para 45,5% (muita); os menos experientes cometeram mais erros de comissão, e os de omissão foram parecidos em todos (Dratsch 2023, 27 radiologistas). Foi mais difícil notar o que a IA deixou passar do que o falso alarme (Matzen 2024). Kim 2025 viu falso positivo da IA afetar radiologistas, com o grupo mais experiente mantendo o melhor desempenho. Küçking 2024 (210 profissionais, feridas) achou proteção em perícia diagnóstica, treino em feridas e sexo feminino, mais suscetibilidade com maior benefício percebido da IA, e idade sem efeito. Dar conhecimento de domínio a não especialistas reduziu a dependência de previsão errada (Dikmen e Burns 2022). Os autores falam em risco de perda de habilidade (Dratsch).

**Rejeitar a IA em palavras não impede de segui-la.** Radiologistas deram nota menor ao conselho da IA e se apoiaram nele mesmo assim (Gaube 2021). Executivos em decisão de P&D ganharam confiança e qualidade de decisão, e superestimaram a confiabilidade da IA (Keding e Meissner 2021, 150 executivos).

**Autoconfiança não protege sozinha.** Ela não mudou entre recomendação certa e errada (Jacobs 2021); previu o acerto e reduziu a confiança excessiva só entre os clínicos experientes (Bond 2018); junto com a experiência, reduziu só o erro de comissão (Dratsch 2023). Cabitza 2024 e Küper 2025 ainda acham correlação positiva com o acerto, e os autores lembram que ela pode vir da experiência (Glick 2022), que dão como o fator mais protetor.

**Confiança é fator central, mas não basta.** Respondeu por até 24,1% da variância do comportamento de confiar, apropriado ou não (Küper 2025). Funciona como limiar: abaixo dele, a pessoa não se apoia na IA, seja qual for a confiabilidade mostrada (Horowitz e Kahn 2024). Diferente de Goddard 2012, Klingbeil 2024 achou a confiança situacional correlacionada positivamente com seguir o conselho e a propensão a confiar, negativamente; Küper 2025 mantém a disposição como antecedente, com a situação como mediadora. A confiança aprendida passa de um sistema de IA a outro, o que raramente acontece entre pessoas (Duan 2024). Em cenário de alto risco e 70% de confiabilidade, a confiança foi maior, sobretudo com carga alta (Sato 2020); os autores concluem que o risco não se qualifica como fator ambiental significativo, porque leigos também confiam demais em tarefa de baixo risco (Banker e Khetani 2019).

**Explicações não resolvem, e às vezes pioram.** Mapas de calor melhoraram o acerto só quando a IA acertava, e levaram a excesso de diagnóstico quando errava (Rezazade Mehrizi 2023, 92 radiologistas). Explicação melhorou a autoconfiança sem reduzir a ancoragem da primeira impressão (Nourani 2022), e aumentou a confiança na IA sem melhorar o acerto (Cabitza 2023). Vered 2023 atribui o problema à confiança indevida que a explicação reforça; Cecil 2024, à carga que a explicação complexa acrescenta; EEG indica carga contribuindo para a confiança excessiva (Zhang 2024). Vários formatos juntos não ajudaram a detectar o erro (Naiseh 2023); explicação simplista foi a que mais piorou (Jacobs 2021); retorno de calibração tampouco ajudou (Tatasciore e Loft 2025). Em sentido contrário, Vasconcelos 2023 acha que explicação reduz a confiança excessiva sob condições, e que há utilidade maior em explicação fácil para tarefa difícil. O artigo trata isso como tensão entre simplicidade e detalhe.

**Forçar o pensamento funciona, e é malquisto.** Funções de forçamento cognitivo reduziram a confiança excessiva quando a IA errava, mais que explicação simples; os participantes preferiram a explicação simples, porque as funções exigem mais, e a nota de confiança subjetiva correlacionou negativamente com o desempenho (Buçinca 2021; desconexão também em Jacobs 2021 e Cao 2023). Quem tem mais necessidade de cognição se beneficiou mais.

**A ordem conta.** IA primeiro melhorou o acerto e aumentou o efeito de pré-ativação quando a IA errava; humano primeiro levou a conservadorismo ou a complacência, conforme a IA concordasse ou não com a avaliação inicial, ambos vistos como ancoragem (Cabitza 2023). Quem via a sugestão antes de formar juízo seguia mais a errada (Agudo 2024). Começar pelos pontos fortes do sistema aumentou confiança e erros; começar pelos fracos reduziu erros e subestimou a capacidade, com novatos mais presos e especialistas mais sensíveis à ordem do erro (Nourani 2022). Tempo curto de decisão aumentou a ancoragem, e tempo longo de observação aumentou a confiança no próprio juízo, variando com a tarefa (Cao 2023); tempo serve para desancorar (Rastogi 2022).

**Verificar mais funciona, e responsabilizar não.** Verificar mais melhorou a decisão, e avisar dos erros possíveis aumentou a verificação, mas enfatizar responsabilidade não mudou nada; dados muito agregados no painel reduziram a verificação sem piorar a decisão (Kupfer 2023, RH). Rezazade Mehrizi 2023 ressalva que esse tipo de aviso pode não funcionar sem familiaridade com a ferramenta.

**Letramento em IA tem curva.** Quem sabe pouco tende à aversão, quem sabe medianamente confia demais (efeito Dunning-Kruger, na leitura dos autores) e quem sabe muito se apoia de forma mais equilibrada (Horowitz e Kahn 2024). A hipótese da revisão é que aversão e confiança excessiva nascem do cruzamento de dois saberes, o do domínio e o de IA.

**Três estudos não acham o viés.** Alon-Barkat e Busuioc 2023 acham adesão seletiva, conforme estereótipos prévios (notas baixas pesaram mais contra professores com nome marroquino); Selten 2023 e Bashkirova e Krpan 2024 põem o viés de confirmação como mecanismo dominante. Os autores respondem que esses estudos não explicam quem segue a IA errada apesar da relutância declarada (Gaube 2021), e que podem caber numa trajetória de calibração da confiança.

**Outros achados.** Os usuários preferem sistema que exija menos, mesmo sem ganho na decisão (Buçinca 2021). A confiança excessiva pode ser estratégia para reduzir a carga, e não só confiança mal colocada (Alami 2025). Desvios-padrão altos na intensidade de verificação levaram Kupfer 2023 a sugerir estudar diferenças individuais. A estrutura MABA-HABA (Klingbeil 2024) explica o apoio pela percepção de quem é melhor na tarefa, máquina ou humano, e os autores dizem que ela não dá conta das decisões financeiras nem dos comportamentos opostos em Cabitza 2023. Especialistas tendem a rejeitar a IA por heurísticas próprias, viés de negatividade, ilusão de validade e perseverança na crença (Bertrand 2022).

## O que respondem às cinco perguntas

1. **Fatores:** confiança e complexidade da tarefa predominam, somados a carga, pressão de tempo e ordem. Moderadores: experiência profissional e de domínio são os mais protetores, mais conhecimento avançado de IA e engajamento na verificação.
2. **Outros vieses:** sim, em especial ancoragem e Dunning-Kruger.
3. **Explicação e transparência:** as explicações podem virar atalho e reforçar a confiança; vários tipos e retorno de calibração não ajudam a reconhecer recomendação errada.
4. **Letramento:** conhecer melhor a IA favorece decisão melhor e confiança apropriada.
5. **Diferenças individuais:** sim: experiência, necessidade de cognição, familiaridade com IA. Mulheres menos suscetíveis, idade neutra (Küçking 2024).

## O que propõem para o design

- **Simplicidade e detalhe (5.1):** explicação rende pouco se a tarefa é difícil e a explicação complexa, ou a tarefa fácil e a explicação simples (Vasconcelos 2023). Explicações por contrafactual e por exemplo favoreceram a confiança baseada em cognição (Naiseh 2023). Casos parecidos do passado estimulam reflexão sem tomar o lugar do juízo (Cabitza 2024). Explicação local reforçou o viés depois de primeira impressão boa, e melhorou o foco (Vered 2023).
- **Engajamento (5.2):** algum esforço cognitivo, mesmo reduzindo a preferência do usuário, aumenta o engajamento crítico. Incentivos podem compensar motivação baixa (Vasconcelos 2023). O design deve considerar carga e tempo.
- **Adaptação (5.3):** não supor que todos vão se engajar; adaptar à experiência e ao modelo mental; apoiar o inexperiente com alta disposição a confiar a reconhecer erro, e levar o experiente a engajar criticamente (Küper 2025).
- **Treino (5.4):** sessões guiadas antes de implantar, com saídas certas e erradas (Nourani 2022), mais prática com a ferramenta.
- **Supervisão (5.5):** a regulação usa "supervisão humana" como solução geral, sem ver que o viés persiste nela (Ruschemeier e Hondrich 2024). Agudo 2024 propõe inverter os papéis: a pessoa decide primeiro, e a IA é segunda opinião que alerta. Cabitza 2024 propõe a "IA com atrito" e o método pro-hoc, que não interpreta o caso e mostra casos análogos, a favor e contra a avaliação inicial.

Na conclusão, o engajamento do usuário é o ponto de intervenção "most feasible and impactful", e compreensibilidade e adaptação, os atributos que o apoiam.

## O que mais a introdução traz

Três desafios da colaboração humano-IA (Steyvers e Kumar 2024): entender e melhorar a complementaridade, entender os modelos mentais que as pessoas têm da IA, e desenhar a interação (momento e informação). GDPR e AI Act enfatizam a supervisão humana sem tratar o viés nas decisões híbridas (Ruschemeier e Hondrich 2024). Norma cultural muda o que se espera da IA: europeus-americanos priorizam controle, participantes chineses valorizam conexão e abertura à autonomia dela, e afro-americanos ficam no meio (Ge 2024); os autores veem aí o risco de deixar certas populações mais vulneráveis ao viés. Parte do viés vem de limite de atenção e memória, parte de decisão, como a tendência a poupar esforço cognitivo ("cognitive miser"); viés de confirmação também contribui (Lu e Yin 2021).

## Figura 2 e tabelas

A Figura 2 é um modelo visual que liga, por setas, conhecimento em IA (mínimo, moderado, avançado), perícia, confiança, estilo cognitivo, visualização de dados e nível de verificação à colaboração humano-IA, com confiança excessiva e aversão como desfechos. As Tabelas 1 a 3 reproduzem quadros de Lai 2023, Hemmer 2021 e Bao 2023; a Tabela 4 lista os 35 estudos, com domínio, população, tarefa e tipo de assistência. Estão no integral.

## Limitações declaradas

Só periódicos revisados por pares de 2015 a 2025, com possível perda de trabalhos anteriores e preprints; só inglês; só experimentais, sem qualitativos ou métodos mistos; fora anais, teses e revisões; fora estudos de aceitação ou calibração sem ligação direta com o viés, e desenvolvimento técnico. A própria busca "lacked sensitivity", por lacunas de indexação e variação de termos, o que apareceu nas fontes adicionais. Queriam tratar fatores culturais e sociodemográficos e não conseguiram, por falta de estudos comparativos; só acharam gênero e idade.

## O que a fonte não diz ou deixa em aberto

Não dá a contagem de estudos por medida de viés, embora chame uma delas de a mais usada. Não agrega os resultados numa estimativa de efeito. Não relata avaliação de qualidade ou risco de viés dos estudos incluídos. Na resposta à pergunta 2, escreve que o efeito Dunning-Kruger atinge quem tem conhecimento "limited" de IA; nos resultados e em 4.1.3, quem tem conhecimento "moderate". Declara que trata viés de automação e complacência como intercambiáveis, então os achados não os separam.
