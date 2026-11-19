---
titulo: "Eustachian tube dysfunction: A diagnostic accuracy study and proposed diagnostic pathway"
tipo: paper
autor: "Matthew E. Smith, Yemisi Takwoingi, Jon Deeks, Cuneyt Alper, Manohar L. Bance, Mahmood F. Bhutta, Neil Donnelly, Dennis Poe, James R. Tysome"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC6224095/"
publicado_em: 2018-11-08
capturado_em: 2026-11-04
licenca: "Creative Commons Attribution (CC BY), escrita na página do PMC: 'open access article distributed under the terms of the Creative Commons Attribution License' (© 2018 Smith et al.); o integral está na url"
areas: [agent-engineering]
tags: [reference-standard, expert-panel, latent-class-analysis, adjudication, diagnostic-accuracy, no-gold-standard, indeterminate, incorporation-bias, medical-annotation]
---

# Smith et al. 2018 (PLOS ONE): como medir testes quando a doença não tem padrão-ouro

Ficha em palavras próprias; o texto integral (CC BY) não vem neste repositório e se lê na url do frontmatter. DOI 10.1371/journal.pone.0206946. Lido no texto bruto da página do PMC em 2026-11-04. Estudo prospectivo de acurácia diagnóstica sobre a disfunção da tuba de Eustáquio (ETD, a tuba que liga o ouvido médio à nasofaringe), numa doença sem método de referência aceito. O ponto metodológico que importa aqui: o estudo constrói o "padrão de referência" de duas maneiras diferentes, um painel de especialistas e um modelo estatístico de classes latentes, e compara o que cada uma dá.

## Desenho

- **Amostra:** 116 pacientes adultos, recrutados de forma não consecutiva num ambulatório de otorrinolaringologia de Cambridge (nov/2016 a mai/2017), com sintomas ou achados sugestivos de ETD (pelo menos dois sintomas, e/ou retração da membrana timpânica, e/ou timpanograma com pressão negativa de -100 daPa ou menos). Excluídos: otite média com efusão, perfuração, colesteatoma, marca-passo, fenda palatina e outras malformações, quem não consentisse ou não lesse inglês. Todos fizeram todos os testes numa única sessão, com um único avaliador; a ordem foi parcialmente aleatória (timpanometria e "nine-step" sempre primeiro).
- **Testes avaliados ("index tests"):** 14 testes de abertura da tuba (nove para a forma obstrutiva, OETD; cinco para a patulosa, PETD), dois questionários de sintomas (PROMs: CETDA e ETDQ-7) e os escores compostos ETS e ETS-7. Registrou-se também o tempo, a dificuldade e o desconforto de cada teste.
- **Duas formas de referência:** (1) painel de especialistas; (2) análise de classes latentes (LCA), um modelo que infere o diagnóstico não observado a partir da combinação dos testes.
- **Painel:** seis especialistas internacionais divididos em dois painéis de três (A e B). Cada paciente foi sorteado para um painel (estratificado pelo diagnóstico da clínica de origem); 20 pacientes foram dados aos dois painéis para medir a concordância entre painéis. O painel via um resumo do caso (história, exame, audiometria, resposta a tratamentos prévios) e não via os resultados dos testes, exceto a timpanometria, para evitar viés de incorporação (o teste avaliado entrar no gabarito que o avalia). Opções: OETD, PETD ou outro diagnóstico.
- **Regra de decisão do painel:** cada membro diagnostica sozinho e sem conversar; se os três concordam, vale; as discordâncias vão a uma teleconferência do painel, que deve buscar consenso; sem consenso, decide a maioria de 2 a 1.
- **Regras fixadas antes para o conflito entre os dois painéis (nos 20 casos comuns):** (1) diagnóstico por concordância individual vale mais que o de discordância inicial; (2) diagnóstico por consenso em discussão vale mais que o de voto 2 a 1; (3) se nenhuma das duas regras resolve (diagnósticos conflitantes obtidos do mesmo modo), o caso é registrado como "indeterminado".
- **LCA:** um teste por aspecto da função da tuba, para respeitar a exigência de independência entre testes; para cada teste, o limiar com maior índice de Youden (J = sensibilidade + especificidade - 1), porque não havia razão para priorizar sensibilidade ou especificidade. Quatro modelos: com todos os testes e o painel como um "teste" a mais; sem o painel; sem os questionários; só os testes de abertura. Variantes sem a timpanometria, por ela ter sido vista pelo painel.
- **Regressão logística penalizada (LASSO):** dois modelos para prever OETD, um "clínico" (só testes de rotina) e um "de pesquisa" (com os de uso raro), validados internamente por bootstrap de 200 amostras.

## Resultados

**O painel.** 57 pacientes (49,1%) tiveram OETD, 12 (10,3%) PETD, 45 (38,8%) outro diagnóstico; em 2 (1,7%) os painéis não chegaram a acordo e o caso ficou "indeterminado" e fora das análises. Nos 20 casos vistos pelos dois painéis houve concordância em 15 (75%), kappa de Cohen 0,55 (IC 95% 0,21 a 0,89), "moderado".

**Sintomas e função não andam juntos.** A análise de componentes principais achou quatro componentes. O primeiro reuniu os testes de abertura da tuba; o segundo, os dois questionários e o diagnóstico do painel, com os testes de abertura pesando pouco ou negativamente nele. A correlação entre questionários e testes de abertura foi não significativa em quase todos os pares. Os autores leem nisso que sintomas e função medida variam de modo independente; o diagnóstico do painel, aproximação do diagnóstico clínico atual, acompanhou os sintomas e não a função medida. Para a forma patulosa o padrão foi outro: o diagnóstico do painel correlacionou-se com os testes de abertura (o que sugere que a história característica reflete melhor a função nesse subtipo). O terceiro componente separou testes de abertura passiva dos de abertura ativa.

**Acurácia com o painel como referência.** Pobre: nenhum teste isolado passou de 65% em sensibilidade e especificidade ao mesmo tempo, nem de J = 0,5. Os testes para a forma patulosa foram melhores que os da obstrutiva, com maior especificidade. Poucos casos de PETD (12) impediram LCA e regressão para essa forma.

**Acurácia pelas classes latentes.** Os modelos sem o painel classificaram 31,6% a 32,5% como OETD; os com o painel, 38,5% a 40,2%. (O painel sozinho, 49%.) Incluir o painel como teste adicional reduziu a sensibilidade e a especificidade de todos os outros testes, porque empurrou mais gente para a classe "doente". Incluir qualquer um dos questionários quase não mudou a alocação, e J deles ficou entre -0,09 e 0,10. Em todos os modelos, só timpanometria, sonotubometria e tubomanometria (a 300 daPa) tiveram J acima de 0,5. Os testes de equalização de pressão tiveram especificidade mais alta que os outros. A timpanometria tinha sido tirada dos primeiros modelos pelo temor de viés de incorporação; ao incluí-la, o efeito se parecia com o dos outros testes de abertura, e não com o do painel.

**Questionários.** Sensibilidade boa, mas 71,0% a 81,8% da coorte pontuou positivo, e a especificidade foi muito baixa. Os autores atribuem isso a sintomas inespecíficos (perda auditiva, doença de Ménière, disfunção da articulação temporomandibular também pontuam alto).

**Combinar testes.** Nos modelos de regressão o c-statistic superou a AUC de cada teste isolado; o ajustado por otimismo foi 0,74 para os modelos clínicos e 0,76 a 0,77 para os de pesquisa, sem ganho relevante ao somar os testes de pesquisa. A inclinação de calibração ficou entre 0,79 e 0,83: previsões extremas demais. Os autores não propõem calculadora a partir do modelo, porque a referência em que ele se apoia é duvidosa.

**Viabilidade.** Sem evidência de fadiga entre repetições (ANOVA, p de 0,40 a 0,98). A bateria objetiva toda durou em média 40 min 21 s; os testes foram bem tolerados, com mais desconforto na tubomanometria e na tuboimpedância (pressão súbita na nasofaringe). Um paciente aspirou água, sem sequela.

## O que os autores concluem sobre a referência

- Duas explicações para o painel achar 49% e a LCA 32%: o diagnóstico clínico superestima OETD (sintomas inespecíficos, falsos positivos), ou os testes de abertura subdiagnosticam (a doença é intermitente e o teste pode cair num período normal; ou só aparece em situações como mudança de pressão ambiente; ou é leve demais para falhar nas condições não fisiológicas do teste). Eles apontam as duas como possíveis, sem decidir.
- O fato de especialistas experientes não concordarem em certos casos, somado à correlação fraca com os testes de abertura, sugere que o painel é um padrão imperfeito. Ainda assim, tirar de vez o julgamento clínico perderia um "teste" sofisticado; o modelo LCA sem questionários lhes parece uma forma experimental de combinar clínica e função medida.
- Painel e testes de abertura, se medem a mesma doença, medem aspectos diferentes: são complementares, não alternativos.
- Julgam o resultado das classes latentes mais confiável que o do painel, dada a referência falha deste.

## O percurso diagnóstico proposto

Desenhado para maximizar a especificidade, porque clínicos e pacientes querem certeza antes de uma intervenção. Quatro etapas: (1) avaliação clínica, que serve para selecionar quem testar e qual forma suspeitar (pré-seleção eleva a prevalência e o valor preditivo dos testes); (2) testes de função: na suspeita de OETD com membrana íntegra, timpanometria primeiro (pressão abaixo de -50 daPa diagnostica sem mais testes, salvo história de fungar habitual); se normal, sonotubometria e tubomanometria, ambas positivas para certeza; sem esses aparelhos, a manobra de Valsalva observada é a melhor sem equipamento especial; para PETD, mudança de pressão sincronizada com a respiração (impedância se a membrana é íntegra, TTAG se perfurada), e quem testa negativo na forma suspeitada passa a ser testado para a outra; (3) repetição em outro dia nos testes negativos com suspeita alta (a doença oscila), e provocação por exercício para PETD; (4) incerteza residual: "Possible ETD" para sintomas intermitentes ou situacionais que os testes atuais não pegam, e "ETD Unlikely" quando os sintomas são contínuos e os testes, repetidos, negativos. O grupo "Possible" pode conter outros diagnósticos e os autores não recomendam recrutá-lo para ensaios de intervenção em fase inicial.

## Limitações declaradas

Os especialistas não puderam examinar nem interrogar os pacientes, só ler o resumo; na prática teriam mais exames. Nem o fungar habitual constava dos resumos. A LCA exige independência entre testes, que pode ter sido violada se os testes erram de modo parecido. Amostra pequena, só adultos, com membrana íntegra e ouvido médio aerado; um avaliador. Os limiares valem para o equipamento e o protocolo usados. Dados no repositório da Universidade de Cambridge (doi 10.17863/CAM.26158).

## O que a fonte não diz

Não diz qual das duas referências está certa quanto à prevalência de OETD (49% ou 32%); trata as duas como falhas. Não diz como lidar com o caso "indeterminado" além de excluí-lo das análises. Não testa o percurso proposto em outra coorte.
