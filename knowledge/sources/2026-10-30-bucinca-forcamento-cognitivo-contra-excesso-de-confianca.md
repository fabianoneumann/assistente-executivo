---
titulo: "To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making"
tipo: paper
autor: "Zana Buçinca, Maja Barbara Malaya, Krzysztof Z. Gajos"
url: "https://arxiv.org/abs/2102.09692"
publicado_em: 2021-02-19
capturado_em: 2026-10-30
licenca: "CC BY 4.0 para a versão do arXiv (indicada na página do arXiv); o PDF traz o aviso de permissão da ACM ('© 2021 Copyright held by the owner/author(s). Publication rights licensed to ACM.'), que vale para a versão publicada na ACM"
areas: [agent-engineering]
tags: [human-in-the-loop, overreliance, cognitive-forcing-functions, explainable-ai, anchoring, need-for-cognition, trust-calibration, human-ai-complementarity]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0, a da versão do arXiv) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 19/02/2021, a única versão e a lida; a página do arXiv liga o DOI 10.1145/3449287. O PDF do arXiv traz a formatação e o rodapé da revista: Proceedings of the ACM on Human-Computer Interaction, vol. 5, CSCW1, artigo 188 (abril de 2021), 21 páginas; recebido em outubro de 2020, revisto e aceito em janeiro de 2021. Harvard University (Buçinca e Gajos) e Lodz University of Technology (Malaya). O integral foi extraído do PDF; as Tabelas 1, 2, 4 e 5 e as Figuras 2 e 3 saíram com colunas embaralhadas e foram lidas nas páginas renderizadas. Lida (camadas flexíveis de avaliação).

## O resumo

Quem usa ferramentas de apoio à decisão com IA costuma confiar demais nela (overreliance): aceita a sugestão mesmo errada. Acrescentar explicações não parece reduzir isso, e há estudos em que aumenta. Pela teoria do processo dual, os autores supõem que as pessoas raramente se engajam analiticamente com cada recomendação e explicação, e criam heurísticas gerais sobre quando seguir a IA. Com base em pesquisa sobre decisão médica, desenham três intervenções de forçamento cognitivo e as comparam, num experimento com 199 pessoas, a duas abordagens simples de IA explicável e a uma linha de base sem IA. O forçamento cognitivo reduziu de forma significativa a overreliance frente às abordagens simples, com uma troca: as pessoas deram as piores avaliações subjetivas aos desenhos que mais reduziram a overreliance. Numa auditoria de desigualdade, o benefício foi maior, em média, para quem tem alta necessidade de cognição (Need for Cognition, a motivação para atividades mentais de esforço).

## 1. Introdução

- Equipes humano e IA costumam superar a pessoa sozinha, mas ficam abaixo da IA sozinha; em vez de combinar o próprio juízo com a sugestão, as pessoas seguem a IA mesmo quando ela erra e elas teriam acertado sozinhas.
- A IA explicável (XAI) deveria resolver isso: a explicação mostraria quando o raciocínio da máquina está errado. As evidências dizem que, quando a IA sugere algo errado ou subótimo, as pessoas ainda decidem, em média, pior do que sem ajuda.
- **A lente do processo dual:** as pessoas operam quase sempre no Sistema 1 (heurísticas e atalhos); o Sistema 2 (analítico) é acionado raramente, por ser lento e custoso. O Sistema 1 deixa a pessoa exposta a vieses cognitivos. Os autores dizem que não querem sugerir que o Sistema 1 seja sempre ruim: reconhecer padrões a partir de muita experiência é parte da perícia, mas especialistas também caem em vieses, e é preciso combinar os dois.
- A premissa implícita da XAI é que a pessoa avalia analiticamente cada explicação. Como isso exige esforço, que as pessoas evitam, os autores dizem que a premissa é "likely incorrect": as pessoas parecem formar uma heurística sobre a competência geral da IA, e há estudos em que a explicação é lida como sinal geral de competência e, só por estar presente, aumenta a confiança e a overreliance.
- **A proposta:** além de boas técnicas de explicação, aumentar a motivação para se engajar com elas. Na medicina, as funções de forçamento cognitivo (cognitive forcing functions) são intervenções no momento da decisão que interrompem o raciocínio heurístico: listas de verificação, pausas diagnósticas, pedir que a pessoa descarte explicitamente uma alternativa. Hipótese: intervenções mais rígidas fazem pensar mais, mas são achadas complexas e menos usáveis.
- **Contribuições:** introduzir o forçamento cognitivo como desenho de interação em decisões humano e IA e mostrar que pode reduzir a overreliance, com uma troca entre eficácia e aceitação; e uma autoauditoria que mostra o benefício maior para quem tem NFC alto. Os autores dizem que a eficácia da colaboração depende de fatores humanos como a motivação cognitiva, além da forma e do conteúdo da explicação, e que auditar escolhas de desenho de interação para efeitos desiguais é tão importante quanto auditar algoritmos.

## 2. Trabalhos relacionados

- **Forçamento cognitivo e estratégias:** na clínica, muitos erros diagnósticos vêm de vieses e síntese falha da informação, não de falta de conhecimento. As intervenções se dividem em estratégias educacionais (desenviesamento metacognitivo por currículo, simulação e treino, para decisões futuras) e funções de forçamento cognitivo (no momento da decisão: listas de verificação, pausas diagnósticas, decisão lenta). Estudos indicam que as segundas aumentam mais a acurácia diagnóstica que as primeiras.
- **Overreliance em decisões assistidas:** equipes ficam abaixo da IA sozinha em tarefas em que a IA é mais precisa que as pessoas (escolha de tratamento médico, detecção de resenhas enganosas, previsão de inadimplência, detecção de nutriente gorduroso, faixa de renda). Explicações não ajudaram a detectar recomendações erradas; melhoraram o desempenho frente ao humano sozinho ou à previsão sem explicação, mas a equipe continuou abaixo da IA. A visão dominante é que as pessoas confiam demais na IA; daí a ênfase em confiança calibrada. Há diretrizes contra a confiança excessiva (em robôs, evitar traços que levem à antropomorfização; em carros autônomos, ferramentas que percebam a desatenção do motorista), mas, até onde os autores sabem, nenhuma intervenção desenhada para reduzir a overreliance em IA e testada empiricamente.
- **Formas de forçamento já usadas ou com análogos em decisões com IA:**
  - Pedir a decisão antes de mostrar a recomendação: estudos anteriores mostraram ancoragem quando a recomendação vem antes, e decisões melhores quando a IA aparece depois de uma decisão sem ajuda.
  - Desacelerar o processo: atrasar a apresentação da recomendação pode melhorar os resultados.
  - Deixar a pessoa escolher se e quando ver a recomendação: conselho não pedido que contradiz a ideia inicial pode provocar reatância (resistência ao conselho).
- **Preferência contra desempenho:** visualizações mais difíceis melhoram compreensão e memória sem serem preferidas; estudantes preferem e acham que aprendem mais com instrução passiva, mas aprendem e rendem mais com a ativa. Por isso os autores esperam uma tensão entre forçamento cognitivo e preferência.

## 3. Experimento

**Hipóteses:**
- H1a: frente à XAI simples, o forçamento cognitivo melhora o desempenho da equipe quando a principal previsão da IA está errada.
- H1b: em consequência, melhora o desempenho da equipe no geral.
- H2: há correlação negativa entre a aceitação autodeclarada da interface e o desempenho da equipe quando a IA erra.

**Tarefa:** nutrição, escolhida porque recrutar especialistas (juízes, clínicos) é caro e difícil. A pessoa vê a foto de um prato e troca o ingrediente mais rico em carboidrato por um pobre em carboidrato e de sabor parecido: primeiro escolhe o ingrediente a retirar (lista de cerca de 10, com todos os ingredientes principais da foto e outros), depois o substituto (outra lista de cerca de 10). Cada prato tinha um ingrediente com muito mais carboidrato que os outros.

**Condições (seis relatadas; Figura 1):**
- **No AI:** só a foto e os dois menus.
- **XAI simples (SXAI):**
  - *Explanation:* lista dos ingredientes reconhecidos pela IA e as quatro melhores substituições para o mais rico em carboidrato, cada uma com redução de carboidrato e semelhança de sabor estimadas, mostradas de imediato. Representa o desenho comum de interface.
  - *Uncertainty:* igual, mais a frase "The AI is X% confident in its suggestion.", mostrada só quando a IA estava incerta.
- **Forçamento cognitivo (CFF):**
  - *On demand:* a sugestão não aparece por padrão; a pessoa clica em "See AI's suggestion" para ver sugestão e explicação. Forma leve: a pessoa se engajaria por ter pedido.
  - *Update:* a pessoa decide primeiro sem IA, depois vê sugestão e explicação e pode atualizar. Hipótese: a discordância da IA despertaria curiosidade sobre o porquê.
  - *Wait:* a mensagem "AI is processing the image" por 30 segundos antes da sugestão. Hipótese, apoiada em trabalho anterior em que um algoritmo lento melhorou a acurácia: enquanto espera, a pessoa forma uma hipótese e depois confere se a explicação a sustenta.

**A IA simulada:** 75% de acerto em reconhecer o ingrediente de maior impacto em carboidrato. Não treinaram um modelo real, para controlar o tipo e a frequência dos erros. Uma tabela fixa dava, para cada ingrediente, os dez substitutos de sabor mais parecido, a partir de uma base de moléculas de sabor de 936 ingredientes; a semelhança de sabor é a razão entre moléculas em comum e o total de moléculas dos dois (interseção sobre união). Os substitutos eram ordenados pela média harmônica de semelhança de sabor e redução de carboidrato, para otimizar os dois. As explicações por atributo pretendiam ser comparáveis às geradas por técnicas como SHAP. Os erros foram desenhados como falha de reconhecimento visual: a IA não reconhecia o ingrediente mais rico em carboidrato e sugeria trocar o segundo, que era de baixo carboidrato.

**Procedimento:** no MTurk; 26 questões em dois blocos de 13; cada bloco numa condição sorteada entre nove (as seis acima e três exploratórias não relatadas), diferente em cada bloco. A primeira questão de cada bloco era de prática e foi descartada. Seis questões com a IA errada (três por bloco), em posições fixas, com a ordem das demais sorteada por pessoa. Questionário subjetivo após cada bloco; após o primeiro, quatro itens de Need for Cognition (os de maior carga fatorial da escala original).

**Participantes:** 260 adultos residentes nos EUA, em três lotes; cerca de 15 minutos em média; US$ 2,50 (cerca de US$ 10 por hora) e bônus de US$ 3 ao melhor de cada lote. 49 excluídos por escolherem, em mais de 55% das questões, retirar um ingrediente que não estava no prato (tinham acurácia 0); 12 por terem caído só em condições exploratórias. Ficaram 199; dos 191 que responderam ao questionário demográfico, idade média 37,09 (DP 10,74), 125 (65,44%) homens, 164 (85,86%) com ou cursando graduação, 13 com ensino médio, 13 com ou cursando doutorado, 1 com escolaridade abaixo do ensino médio.

**Medidas (definições dos autores):**
- *Desempenho geral:* porcentagem de trocas ótimas, com o ingrediente certo retirado e o melhor substituto.
- *Detecção da fonte de carboidrato:* porcentagem de acertos do ingrediente a retirar.
- *Redução de carboidrato* e *semelhança de sabor*, em porcentagem frente ao ingrediente retirado.
- *Overreliance:* "Percentage of agreement with the AI when the AI made incorrect predictions".
- *Erro humano* (com a IA errada): decisão errada e diferente da sugestão da IA.
- Subjetivas, Likert de 1 a 5 após cada bloco: preferência ("I would like to use this system frequently."), confiança ("I trust this AI's suggestions for optimal replacement."), demanda mental ("I found this task difficult.") e complexidade ("The system was complex.").

**Análise:** desenho misto entre e dentro de sujeitos (cada pessoa viu duas das nove condições). Análise primeiro por categoria (No AI, SXAI, CFF), depois entre condições dentro de cada categoria. Para o desempenho nas questões em que a IA errava, o grupo No AI entra como comparação nas mesmas questões, sem ter visto previsão. Análise de variância com modelos de efeitos mistos (categoria ou condição fixa, participante aleatório), o que também lida com o desbalanceamento (por isso há graus de liberdade fracionários); comparações post hoc por t de Student com correção de Holm-Bonferroni; médias marginais; d de Cohen calculado considerando o efeito aleatório; correlação de Pearson entre medidas subjetivas e desempenho.

## 4. Resultados

**Acaso:** cerca de 1% na decisão completa e 10% na detecção.

**Tabela 1, médias marginais (erro padrão) No AI / SXAI / CFF:**
- *Todas as questões:* desempenho geral 0,17 (0,03) / 0,35 (0,02) / 0,33 (0,02), F(2; 141,6) = 15,43, p ≪ 0,0001; detecção 0,42 / 0,56 / 0,57, F(2; 114,4) = 12,41; redução de carboidrato 21,73 / 35,70 / 35,20, F(2; 123) = 20,15; semelhança de sabor 23,57 / 35,26 / 34,63, F(2; 111,8) = 17,86. Nas quatro, No AI abaixo de SXAI e CFF, que não diferem entre si (d de CFF contra SXAI de 0,03, 0,03, 0,01 e 0,01). Também sem diferença dentro das categorias.
- *Questões com a IA errada:* desempenho geral 0,18 (0,02) / 0,03 (0,02) / 0,09 (0,01), F(2; 261,7) = 12,59; detecção 0,49 (0,04) / 0,08 (0,03) / 0,27 (0,03), F(2; 242,6) = 35,59; redução de carboidrato 23,58 / 2,96 / 11,37, F(2; 262,8) = 24,40; semelhança de sabor 24,00 / 3,37 / 11,28, F(2; 262,1) = 27,95; todos com p ≪ 0,0001. Nas quatro, SXAI abaixo de CFF, que fica abaixo de No AI (d de CFF contra SXAI de 0,37, 0,66, 0,53 e 0,53). Sem diferença dentro das categorias.

**Tabela 2, decisões nas questões com a IA errada, SXAI contra CFF:**
- *Decisão completa:* corretas 0,03 contra 0,09, F(1; 207,6) = 8,95, p = 0,003, d = 0,37; overreliance 0,30 contra 0,26, F(1; 180,9) = 1,02, n.s., d = 0,12; erro humano 0,68 contra 0,65, F(1; 95,5) = 0,12, n.s., d = 0,07. As distribuições diferem: χ²(2, N = 663) = 13,30, p = 0,0013. Com CFF, mais acertos e menos overreliance, "but not significantly so".
- *Detecção:* corretas 0,08 contra 0,27, F(1; 197,4) = 24,11, p ≪ 0,0001, d = 0,66; overreliance 0,64 contra 0,48, F(1; 145,8) = 9,24, p = 0,003, d = 0,36; erro humano 0,27 contra 0,26, n.s., d = 0,04 (a tabela repete aqui o F(1; 95,5) = 0,12 da linha do erro humano na decisão completa). χ²(2, N = 663) = 44,35, p ≪ 0,0001.
- Nenhuma diferença significativa entre condições dentro de cada categoria (Explanation contra Uncertainty; On demand, Update e Wait), em nenhuma métrica. O texto não dá os números por condição.

**Tabela 3, subjetivas, No AI / SXAI / CFF:**
- Confiança (não perguntada em No AI): 3,91 contra 3,72, F(1; 146,4) = 2,84, n.s.; mais alta com SXAI, sem significância.
- Preferência: 3,13 / 3,78 / 3,62, F(2; 169,5) = 10,52, p ≪ 0,0001; No AI abaixo das duas com IA.
- Demanda mental: 3,66 / 2,86 / 2,84, F(2; 183,4) = 11,70, p ≪ 0,0001; No AI acima das duas.
- Complexidade: 3,19 / 2,64 / 2,95, F(2; 172,2) = 6,19, p = 0,002; SXAI abaixo de CFF e de No AI.
- Condições dentro das categorias não diferiram em nenhuma medida subjetiva.

**Subjetivo contra objetivo (Figuras 2 e 3, correlação de Pearson):**
- Confiança e desempenho geral: r = 0,005, n.s., com a IA certa; r = −0,24, p = 0,0003, com a IA errada. Confiança e detecção: r = −0,03, n.s. (certa); r = −0,29, p = 0,0008 (errada).
- Preferência e desempenho geral: r = −0,09, n.s. (certa); com a IA errada, a figura traz "r=-16, p=.0002". Preferência e detecção: r = −0,15, p = 0,01 (certa); r = −0,21, p = 0,0005 (errada).
- Demanda mental e desempenho geral: r = −0,24, p < 0,0001 (certa); r = 0,02, n.s. (errada). Demanda mental e detecção: r = −0,24, p < 0,0001 (certa); r = 0,13, p = 0,03 (errada, positiva).
- Complexidade e desempenho geral: r = −0,27, p < 0,0001 (certa); r = 0,01, n.s. (errada). Complexidade e detecção: r = −0,24, p < 0,0001 (certa); r = 0,04, n.s. (errada).
- Confiança e seguir a IA (Figura 3): decisão completa, r = −0,02, n.s. (certa) e r = 0,11, n.s. (errada); detecção, r = −0,05, n.s. (certa) e r = 0,14, p = 0,04 (errada; o texto chama de overreliance seguir a IA quando ela erra).

## 5. Considerações éticas: diferenças de motivação cognitiva

- **Desigualdade gerada pela intervenção:** quando o benefício de uma intervenção vai desproporcionalmente para um grupo já privilegiado, a distância entre grupos cresce mesmo que todos ganhem algo. Os autores fazem uma auditoria interna limitada e escolhem como variável a Need for Cognition (NFC), traço estável de quanto a pessoa gosta de atividade mental exigente, em vez de raça e gênero. A literatura anterior diz que quem tem NFC alto busca mais informação e a processa mais a fundo, e quem tem NFC baixo recorre mais a pistas de superfície (autoridade ou fama da fonte, estética da apresentação); no software, NFC alto adota mais recursos novos e escolhe o método que poupa esforço manual à custa de esforço mental; há também evidência de que NFC alto ganha menos confiança com explicações em sistemas de recomendação, com limites de generalização. Por isso tratam NFC alto como o grupo já privilegiado.
- Os participantes foram divididos na mediana de NFC. NFC alto teve desempenho geral de 0,44 contra 0,23 (F(1; 172,5) = 29,13, p ≪ 0,0001) e detecção de 0,67 contra 0,44 (F(1; 172,2) = 32,11, p ≪ 0,0001).

**Tabela 4, desempenho por NFC, SXAI contra CFF:**
- *NFC alto:* todas as questões, geral 0,44 contra 0,43 (n.s., d = 0,01) e detecção 0,66 contra 0,68 (n.s., d = 0,09); IA errada, geral 0,02 contra 0,11 (F(1; 100,6) = 10,55, p = 0,002, d = 0,57) e detecção 0,08 contra 0,29 (F(1; 90,51) = 14,75, p = 0,0002, d = 0,69).
- *NFC baixo:* todas as questões, geral 0,25 contra 0,21 (n.s., d = 0,16) e detecção 0,45 contra 0,44 (n.s., d = 0,16); IA errada, geral 0,03 contra 0,06 (F(1; 99,37) = 0,94, n.s., d = 0,15) e detecção 0,09 contra 0,26 (F(1; 99,15) = 9,39, p = 0,003, d = 0,57).

**Tabela 5, decisões com a IA errada por NFC, SXAI contra CFF:**
- *NFC alto, decisão completa:* corretas 0,02 contra 0,11 (p = 0,002, d = 0,57); overreliance 0,39 contra 0,32 (F(1; 82,55) = 1,13, n.s., d = 0,18); erro humano 0,60 contra 0,57 (n.s., d = 0,09). χ²(2, N = 357) = 13,12, p = 0,001.
- *NFC alto, detecção:* corretas 0,08 contra 0,29 (p = 0,0002, d = 0,69); overreliance 0,77 contra 0,57 (F(1; 71,22) = 8,80, p = 0,004, d = 0,50); erro humano 0,16 contra 0,15 (n.s., d = 0,04). χ²(2, N = 357) = 29,03, p ≪ 0,0001.
- *NFC baixo, decisão completa:* corretas 0,03 contra 0,07 (F(1; 99,37) = 0,94, n.s., d = 0,15); overreliance 0,22 contra 0,19 (n.s., d = 0,09); erro humano 0,75 contra 0,77 (n.s., d = 0,05). χ²(2, N = 306) = 2,01, n.s.
- *NFC baixo, detecção:* corretas 0,09 contra 0,26 (p = 0,003, d = 0,57); overreliance 0,50 contra 0,37 (F(1; 82,53) = 2,45, n.s., d = 0,27); erro humano 0,38 contra 0,39 (n.s., d = 0,02). χ²(2, N = 306) = 16,30, p = 0,0003.
- **Divergência na própria fonte:** a mesma comparação (NFC baixo, decisão completa, acertos com a IA errada, com o mesmo F(1; 99,37) = 0,94 e d = 0,15) aparece como 0,03 contra 0,06 na Tabela 4 e 0,03 contra 0,07 na Tabela 5, conferido nas páginas renderizadas do PDF.

**Subjetivas por NFC:** juntando as categorias, NFC baixo achou a tarefa mais exigente (3,10 contra 2,62; F(1; 165) = 7,07, p = 0,009) e o sistema mais complexo (3,04 contra 2,65; F(1; 162,4) = 5,86, p = 0,02); relatou mais confiança (3,92 contra 3,70) e mais preferência (3,80 contra 3,56), ambas n.s. **Tabela 6, SXAI contra CFF:** NFC alto, confiança 3,89 contra 3,56 (F(1; 64,22) = 5,90, p = 0,02), preferência 3,75 contra 3,44 (F(1; 62,04) = 4,63, p = 0,03), demanda mental 2,50 contra 2,70 (n.s.), complexidade 2,64 contra 2,95 (F(1; 57,53) = 6,26, p = 0,01). NFC baixo, confiança 3,93 contra 3,93, preferência 3,73 contra 3,86, demanda mental 3,27 contra 2,96, complexidade 2,96 contra 3,11, todas n.s.

## 6. Discussão

- Como em trabalhos anteriores, quem usou XAI simples rendeu mais que quem não teve IA, e as equipes ficaram abaixo da IA sozinha (75%). Os autores atribuem parte disso à overreliance: com a IA errada, quem tinha XAI simples rendeu menos que quem não tinha IA.
- **H1a sustentada:** com a IA errada, as condições de forçamento cognitivo levaram a mais escolhas ótimas que a XAI simples. Mas as equipes continuaram abaixo da IA sozinha: o forçamento reduziu a overreliance, "but not yet eliminated".
- **H1b sem suporte:** sem diferença significativa no desempenho total entre XAI simples e forçamento cognitivo.
- **H2 sustentada:** com a IA errada, as pessoas renderam melhor nas condições que menos preferiram, em que menos confiaram e que acharam mais difíceis; há uma troca entre aceitação do desenho e desempenho da equipe.
- Os autores concluem que a motivação cognitiva modera a eficácia da XAI, e que pesquisadores de XAI devem garantir que as pessoas se esforcem para ler as explicações, além de ajustar atributos da explicação.
- **Tarefas substitutas (proxy tasks):** os resultados apoiam o achado anterior de que avaliar XAI com tarefas substitutas (prever a saída do algoritmo a partir da explicação) dá resultados diferentes de tarefas reais de decisão. Se a tarefa substituta for vista como uma forma forte de forçamento cognitivo, avaliações com ela tendem a dar resultados mais otimistas que as feitas com decisões reais e XAI simples.
- **Desigualdade:** os ganhos do forçamento, desagregados, valeram sobretudo para NFC alto; esse grupo confiou e preferiu menos o forçamento, enquanto não houve efeito negativo no NFC baixo. Os autores dizem que o forçamento pode ampliar a diferença de desempenho por NFC, e que intervenções futuras poderiam se ajustar à motivação cognitiva: intervenções mais rígidas poderiam beneficiar mais e ainda ser aceitas por quem tem motivação mais baixa.
- **Limites e generalização:** a principal limitação é uma única tarefa, não crítica; é preciso verificar se os efeitos se generalizam a outros domínios. Como a pesquisa anterior dá ampla evidência de que mesmo especialistas em decisões críticas recorrem ao pensamento heurístico e caem em vieses (com quatro referências citadas), os autores dizem ter "some confidence that our results will generalize broadly".
- Outra limitação: o forçamento melhorou o desempenho à custa da usabilidade percebida, e sistemas com ele podem ser menos adotados. Os autores propõem estratégias adaptativas: usar o forçamento mais eficaz só na pequena fração de casos em que se prevê que melhora muito a decisão final, o que pede modelos que prevejam o desempenho da equipe por caso e por intervenção, considerando a incerteza da IA naquele caso e as diferenças individuais de motivação cognitiva.

## 7. Conclusão e trabalhos futuros

Três achados: o forçamento cognitivo reduziu a overreliance frente às explicações simples; há uma troca entre confiança e preferência subjetivas e desempenho (as pessoas preferiram e confiaram mais nos sistemas menos exigentes, com os quais renderam pior); e auditorias devem procurar desigualdades emergentes, porque o forçamento beneficiou desproporcionalmente quem tem NFC alto. Para os autores, a pesquisa em XAI não deve supor que as pessoas se engajam com as explicações por padrão; pedem intervenções que provoquem pensamento analítico quando necessário e pesquisa sobre a quantidade e o momento certos de forçamento cognitivo, considerando as diferenças individuais.

---
