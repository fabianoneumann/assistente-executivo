---
titulo: "Understanding Expert Disagreement in Medical Data Analysis through Structured Adjudication"
tipo: paper
autor: "Mike Schaekermann, Graeme Beaton, Minahz Habib, Andrew Lim, Kate Larson, Edith Law"
url: "https://cs.uwaterloo.ca/~klarson/papers/schaekermann_eeg_adjudication_2019.pdf"
publicado_em: 2019-11-01
capturado_em: 2026-11-04
licenca: "ACM (Proc. ACM Hum.-Comput. Interact. 3, CSCW, art. 76; © 2019 dos autores, direitos de publicação licenciados à ACM); a nota do PDF permite cópia digital ou impressa para uso pessoal ou em sala de aula sem fins lucrativos, e exige permissão para republicar; só a ficha"
areas: [agent-engineering]
tags: [adjudication, expert-disagreement, inter-rater-agreement, guideline-rules, medical-annotation, sleep-staging, delphi, unresolved-cases]
---

# Schaekermann et al. 2019 (CSCW): o que explica o desacordo entre especialistas e por que parte dele sobrevive à adjudicação

Ficha em palavras próprias, em estrutura própria (artigo protegido: o integral não entra). Lida no texto bruto do PDF da cópia da Universidade de Waterloo em 2026-11-04; DOI 10.1145/3359178. Estudo observacional de classificação de estágios do sono em registros de polissonografia: um fluxo de adjudicação estruturada, assíncrono e anônimo, em que os especialistas rejulgam os casos de desacordo em rodadas e justificam cada mudança com regras do manual de classificação. O objetivo declarado é entender as fontes e a dinâmica do desacordo, não tornar a rotulagem mais eficiente ou mais exata.

## O que o artigo tenta explicar

Três perguntas: (Q1) por que especialistas discordam na classificação independente; (Q2) por que alguns desacordos persistem depois da adjudicação coletiva; (Q3) que efeito a adjudicação tem na decisão clínica. Os fatores analisados vêm de três fontes que a literatura já usa para o desacordo (diferenças entre quem rotula, características do dado, clareza das instruções), mais uma que os autores acrescentam: a apresentação do dado, isto é, como cada especialista configura o visualizador.

## A tarefa e os dados

Classificar janelas de 30 segundos de um registro de sono em cinco estágios (vigília, REM e três de sono não REM). O artigo cita, como referência, que a concordância entre dois especialistas independentes fica em torno de 82,6% nessa tarefa. Material: pouco mais de 86 horas de gravação de 12 pacientes (média de 7,19 h cada): 3 saudáveis, 3 com Parkinson, 3 com Alzheimer e 3 com apneia do sono; 10.349 casos (janelas). Participantes: 36 técnicos de sono recrutados em plataformas da área (26 nos Estados Unidos, 7 no Canadá, 2 na União Europeia, 1 de local não informado; 30 com o título RPSGT; 23 com ao menos cinco anos de experiência). Cada grupo de três, sorteado, ficou com um registro, de modo que cada registro foi pontuado e adjudicado pelos mesmos três; cada especialista participou de um único painel. Pagamento de US$ 112,50 por duas passagens, cerca de três horas de trabalho.

## O desenho do fluxo

- **Etapa 1, classificação independente:** cada um classifica todo o registro, pode voltar e mudar decisões antes de marcar a passagem como concluída, e pode ajustar o visualizador (sinais visíveis, escala de amplitude, filtros de frequência); as configurações são gravadas junto de cada decisão.
- **Etapa 2, adjudicação:** em rodadas, um especialista de cada vez revisita todos os casos com desacordo, no seu tempo, em ordem de disponibilidade. Vê os votos de todos (indicadores circulares em vermelho nos casos discordantes), as notas e justificativas das rodadas anteriores (a janela de discussão abre sozinha ao chegar ao caso) e pode reclassificar. Para cada reclassificação é obrigatório citar ao menos uma regra do manual e indicar em que medida os critérios de evidência da regra estão atendidos; o comentário livre é opcional. Os especialistas aparecem por pseudônimos. O caso está resolvido quando os três convergem; o processo termina quando todos resolvem ou depois de três rodadas (uma por membro).
- **Manual como regras:** o guia de classificação foi traduzido em 36 regras do tipo "se a evidência A está presente e a B está presente, classificar como X", apoiadas em 15 características básicas (como atividade de ondas lentas, fusos do sono, complexos K, ritmo alfa, despertar, piscadas); mais uma regra de reserva por classe, para quando nenhuma serve. Disjunções viram regras separadas.
- **Como o desenho evoluiu:** (1) sessão presencial com três técnicos certificados (106 minutos gravados e analisados); (2) sessão de 1 hora por videoconferência com os mesmos três; (3) piloto web com três painéis de três. Do presencial: a discussão girava em torno das regras do manual e da presença de características; a dinâmica interpessoal desviava a conversa e dava vantagem aos mais dominantes ou de maior expertise percebida (daí o anonimato); pediam para ver janelas vizinhas (daí rever o registro inteiro); ajustar o visualizador às vezes resolvia o impasse sem argumento. Da videoconferência: a influência da experiência percebida persistiu e agendar vários especialistas ao mesmo tempo se mostrou inviável em escala (daí texto e rodadas assíncronas); divergências sobre as fronteiras de transição entre tipos de característica levaram a incluir medidas de complexidade do sinal. No piloto, os comentários livres eram curtos, sem conversa pessoal, centrados em regras do manual; poucos traziam argumentos que o manual não cobria (nuances de terminologia ambígua, condição presumida do paciente), e por isso o comentário livre foi mantido.

## Resultados

**Tamanho do desacordo.** 4.543 dos 10.349 casos (44%) tiveram algum desacordo (exige acordo exato entre três, de modo que os números são menores que os de trabalhos com dois avaliadores). Depois de três rodadas, 1.667 (37% dos casos discordantes) continuavam sem resolução. A concordância entre os avaliadores subiu de 20% a 30% ao longo das três rodadas.

**Q1, por que discordam** (regressão logística sobre os 10.349 casos): diferenças de experiência (mais ou menos de cinco anos) e de localização geográfica dentro do painel predisseram desacordo; diferenças de credencial, não. Diferenças no filtro de frequência e na escala de amplitude estiveram associadas a mais desacordo; já a diferença no número de sinais visíveis apareceu com sinal inverso (menos desacordo). Quanto aos dados, a complexidade espectral do sinal elevou o desacordo, e pacientes com Parkinson (coeficiente 0,73) e Alzheimer (0,27) tiveram mais desacordo que os saudáveis; apneia não diferiu. Os menores acordos antes da adjudicação ocorreram nesses dois grupos.

**Q2, por que persistem** (regressão sobre os 4.543 casos): vários fatores se repetem, com mudanças. Diferença de credencial, que não causava desacordo, aumentou a chance de resolver o caso (-0,93); apneia teve casos mais resolvíveis que os saudáveis; Alzheimer deixou de pesar; a complexidade espectral do sinal acompanhou maior resolução, e a complexidade das transições no tempo, maior chance de caso sem resolução; a escala de amplitude deixou de ter efeito. Sete das 15 características, quando os especialistas divergiam sobre a presença delas, estiveram associadas a casos sem resolução, com os maiores efeitos de todo o modelo: atividade de ondas lentas (5,12), ondas mistas de baixa amplitude (2,16), despertar (1,88), ritmo alfa (1,67), piscadas (1,51), complexo K (1,33) e fuso do sono (1,25). Para movimentos oculares lentos e movimento corporal grande a divergência se associou a consenso. Os autores concluem (hipótese H2d confirmada) que a estrutura do desacordo, no nível das características, é o que mais explica por que ele sobrevive, e tomam essas divergências como lente quantitativa sobre ambiguidades de baixo nível no próprio manual.

**Q3, efeito clínico.** Na pesquisa final, os especialistas disseram que o processo era útil para gerar um hipnograma confiável (p < 0,001) e que o hipnograma adjudicado merece mais confiança que o da primeira passagem (p < 0,001). Entre os parâmetros, a porcentagem de tempo de sono REM caiu de forma significativa (p < 0,05), um marcador relevante para tratamento (o artigo associa o REM reduzido a doenças neurodegenerativas e a apneia, e o diagnóstico do transtorno comportamental do REM depende da classificação correta dele); as variações iam de -7,5% a +1,4%. O gráfico traz também %N1 e %N3, mas o texto só comenta o %REM.

**Comentários dos participantes.** Unanimemente a favor da adjudicação, sobretudo com justificativa por regras do manual; o formato guiado pelo manual pode ajudar tanto quem pontua há anos (e "preso" ao próprio jeito) quanto iniciantes. A ordem sequencial foi vista por alguns como obstáculo. Um especialista apontou que casos "realmente subjetivos" deviam ser reconhecidos como tais, em vez de forçar consenso.

## Posição do artigo diante da regra de agregação

Distingue duas tradições: técnicas como voto majoritário e algoritmos de agregação (usadas com não especialistas) produzem uma resposta tida como "correta", enquanto outras abordagens tratam o desacordo como informação, e resolver nem sempre é possível ou desejável. Cita a deliberação em grupo como preferível ao voto majoritário, que tende a descontar argumentos e dissidências para promover consenso artificial; e a adjudicação em grupo como forma de gerar padrão de referência confiável para avaliar classificadores automáticos (exemplo citado: exames de retina, em que a deliberação superou o voto majoritário em revocação). Também cita a inspiração no método Delphi.

## Limitações e usos que os autores listam

Adjudicação consome recursos e o artigo não faz análise de custo-benefício. Tarefa de séries temporais biomédicas; cuidado para generalizar. O manual precisa existir e ser mapeável em regras; para tarefas sem manual (epilepsia, glaucoma) a opção de comentário livre poderia servir para extrair regras. O piloto usou os mesmos três especialistas no presencial e na videoconferência. Sugerem usos: treinar iniciantes, alimentar sistemas de apoio com dados que registrem a ambiguidade, e priorizar a adjudicação nos casos críticos de desacordo. Deixam em aberto se um fluxo síncrono aumentaria o acordo e quando introduzir adjudicação onde hoje basta uma leitura.

## O que a fonte não diz

Não mede se os casos resolvidos ficaram mais corretos contra um padrão externo (a medida é de concordância e de mudança de parâmetro clínico); não compara com voto majoritário no mesmo conjunto; não traz custo em horas por caso; não diz quanto dos 37% sem resolução eram casos "realmente subjetivos".
