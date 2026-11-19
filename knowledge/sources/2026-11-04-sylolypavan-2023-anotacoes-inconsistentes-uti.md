---
titulo: "The impact of inconsistent human annotations on AI driven clinical decision making"
tipo: paper
autor: "Aneeta Sylolypavan, Derek Sleeman, Honghan Wu, Malcolm Sim"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC9944930/"
publicado_em: 2023-02-21
capturado_em: 2026-11-04
licenca: "Creative Commons Attribution 4.0 International (CC BY 4.0), escrita na página do PMC ('Open Access This article is licensed under a Creative Commons Attribution 4.0 International License'); o integral está na url"
areas: [agent-engineering]
tags: [annotation-inconsistency, majority-vote, consensus, super-expert, learnability, icu, inter-annotator-agreement, external-validation, medical-annotation]
---

# Sylolypavan et al. 2023 (npj Digital Medicine): onze intensivistas rotulam o mesmo conjunto e geram onze modelos diferentes

Ficha em palavras próprias; o texto integral (CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Artigo npj Digital Medicine 6:26, DOI 10.1038/s41746-023-00773-3; a página da Nature veio sem corpo, e o texto foi lido na cópia do PMC (PMC9944930), em 2026-11-04. Pergunta: o que acontece com um sistema de apoio à decisão quando os rótulos de treino vêm de especialistas experientes que discordam entre si, e as práticas comuns de obter um "padrão-ouro" (confiar no mais sênior, votar por maioria) funcionam. Os autores dizem que o foco é o efeito da discordância e o uso dela no desenvolvimento dos modelos, não resolvê-la para formar uma "verdade".

## Desenho

- **Rótulos:** 60 instâncias de pacientes de UTI do Queen Elizabeth University Hospital (Glasgow), sorteadas de 80.291 registros horários, descritas por seis variáveis (adrenalina, noradrenalina, FiO2, SpO2, pressão arterial média, frequência cardíaca). 11 consultores de UTI rotularam cada uma numa escala de gravidade de cinco pontos, A (relativamente estável) a E (instabilidade cardiovascular grave), a ICU-PSS. A tarefa foi escolhida simples de propósito, para reduzir a inconsistência de cada um consigo mesmo e entre eles. Os consultores são anônimos (C1 a C11) e não se sabe quem é mais sênior. Dados de um estudo anterior (Sleeman et al.), em que já se vira que eles discordam.
- **Modelos:** um classificador por consultor (floresta aleatória como principal; árvore de decisão, XGBoost e SVM deram resultados comparáveis; balancear as classes não mudou o desempenho de forma significativa).
- **Validação interna:** validação cruzada de 5 partições contra os próprios rótulos do consultor; o resultado mede a "aprendibilidade" do conjunto rotulado, isto é, quão bem a regra dele pode ser reproduzida a partir dos dados (um proxy de consistência). F1 micro entre 0,50 e 0,77 nos 11 modelos.
- **Validação externa:** base HiRID (hospital de Berna, Suíça), escolhida em vez da MIMIC-III porque a proporção de pacientes em uso de adrenalina/noradrenalina (31,5% na HiRID, 5,9% na MIMIC, 40% nas instâncias de treino) indica população mais compatível. 2.600 instâncias (1.300 de pacientes que receberam alta com vida na hora seguinte, rótulo A; 1.300 que morreram na hora seguinte, rótulo E). A base não tem rótulos A-E; a alta ou a morte funciona como verdade-terreno, e a escala A-E é lida como confiança sobre o desfecho. Num segundo experimento, 1.064 pacientes em série temporal (5 horas antes do desfecho), com regras de corte "extremas" e "neutras" para converter a média ponderada das cinco previsões em classe.
- **Medidas de concordância:** kappa de Cohen (pares) e de Fleiss (vários), e Krippendorff alfa calculados; escala de interpretação do Cohen: 0,0 a 0,20 nenhuma; 0,21 a 0,39 mínima; 0,40 a 0,59 fraca; 0,60 a 0,79 moderada; 0,80 a 0,90 forte; acima de 0,90 quase perfeita.

## Resultados

**Os onze modelos não classificam do mesmo jeito.** Na validação externa, o kappa de Cohen entre pares de modelos vai de -0,01 a 0,48, média 0,255 ("mínima"); Fleiss 0,236 ("justa"). O resumo do artigo também dá Fleiss de 0,383 ("fair") ligado à validação interna; o corpo do texto não repete esse valor. Isso rejeita a hipótese central, de que os onze modelos produziriam classificações consistentes. Mesmo os dois consultores cujos conjuntos eram muito aprendíveis (C2 e C8) tiveram concordância de só 0,27 entre si: o C2 rotulou 10,0% como E e 3,3% como C; o C8, 1,7% como E e 36,7% como C; as previsões seguiram essa diferença. Os autores leem isso como julgamentos diferentes que podem ser válidos e clinicamente úteis, não necessariamente erro.

**Alta contra morte.** Só nos pacientes que receberam alta: Cohen médio 0,21, Fleiss 0,174 ("leve"). Só nos que morreram: Cohen 0,28, Fleiss 0,267 ("justa"). Na série temporal, a concordância na morte sobe (Cohen 0,327 nas regras extremas e 0,587 nas neutras; Fleiss 0,579 "moderada"), a de alta fica em 0,24 a 0,28. Os autores concluem que os especialistas concordam mais ao prever mortalidade que ao decidir altas, com a ressalva de que havia poucos rótulos E nos conjuntos, o que limita comparações. Um consultor (C10) foi o mais "relutante" em dar alta e C2 e C4 os mais inclinados a dar.

**Desempenho.** O desempenho externo ficou bem abaixo do interno, nos extremos (alta e morte). Os autores sugerem que decisões extremas pedem monitoração contínua (por isso o teste com série temporal, onde todos os modelos foram melhor com a regra neutra), e que anotadores evitam as classes A e E numa escala de cinco pontos.

**Não há um "super especialista".** Sem saber a senioridade, os autores usam a correlação entre desempenho interno e externo como indicador: Pearson 0,51 (e 0,64 e -0,51 nas duas versões da série temporal), isto é, não fortemente associados. Concluem que a hipótese de que o mais sênior sempre fornece o padrão-ouro nem sempre vale, e que os modelos com bom desempenho interno (C4, C8) nem sempre são bons fora.

**O voto da maioria é subótimo; filtrar pela aprendibilidade melhora.** Modelo de voto majoritário de todos os 11 (MV): F1 micro externo 0,254. Modelo de voto majoritário só dos consultores com F1 interno acima de 0,7 (TMV): 0,438, melhor que quase todos os consultores individualmente. Na série temporal, o TMV também superou o MV (muito nas regras extremas, pouco nas neutras). Um consenso "difuso" (média das previsões 1 a 5, descartando o 3 como incerto) e sua versão restrita aos aprendíveis (TFC) também foram bem. Em síntese do artigo: avaliar a aprendibilidade de cada especialista antes de formar o consenso, e excluir os julgamentos pouco aprendíveis, deu melhores modelos na maioria dos casos.

**Peso das horas.** Nas regressões logísticas sobre as cinco previsões horárias, a previsão de 5 horas antes foi a mais importante para a maior parte dos modelos, e a de 1 hora antes a menos, o que os autores chamam de contraintuitivo, sem explicação.

## Procedimento que o artigo propõe

Todos os especialistas rotulam o mesmo conjunto; treina-se um classificador por especialista; mede-se a aprendibilidade por validação cruzada contra os rótulos de cada um (checa a consistência da regra dele); excluem-se os modelos abaixo de um limiar definido antes; forma-se o consenso com os restantes.

## Contexto que o artigo traz sobre a discordância

Fontes de inconsistência de rótulo: informação insuficiente (dados de má qualidade, guias pouco claros), pouca expertise, erro humano (deslizes e ruído), subjetividade (julgamento e viés). Aqui os autores atribuem a inconsistência principalmente à variabilidade entre avaliadores. Citam Kahneman et al. (2021, *Noise*) e distinguem julgamento (escolha em um conjunto fixo de alternativas, que é o caso) de opinião. Exemplos de baixa concordância entre especialistas na literatura: patologistas em lesões proliferativas da mama (Fleiss 0,34); psiquiatras em depressão maior (0,28; 4% a 15% de concordância); especialistas em EEG de UTI (Cohen médio 0,38); anotadores clínicos em pneumonia por laudo de radiografia (Cohen 0,085); em 39,4% das internações o paciente foi para uma equipe diferente da primeira indicada. Ruído de rótulo, dizem, reduz a acurácia, aumenta a complexidade do modelo e o número de amostras necessário. Duas abordagens usuais contra ruído (limpar rótulos ou usar algoritmos tolerantes a ruído) podem apagar diferenças sutis e úteis entre anotadores.

## Limitações e próximos passos declarados

Conjunto pequeno e desbalanceado, poucas variáveis, uma só base externa, 11 consultores de um hospital; o desempenho geral dos modelos é ruim e pode ter outras causas (pouco dado, variáveis pouco preditivas, diferenças entre UTIs). Propõem um estudo maior, com várias UTIs e bases externas de outros países; analisar casos fáceis e difíceis; checar a consistência de cada especialista consigo mesmo repetindo itens; pedir um fator de confiança (0 a 1) em cada rótulo e capturar o nível de experiência para ponderar; para sistemas críticos de segurança, filtrar os especialistas por um conjunto de casos com solução predefinida por painel (abordagem citada do sistema Jeopardy da IBM e do KRUST). Dados e código em repositórios indicados na seção de disponibilidade do artigo.

## O que a fonte não diz

Não traz rótulos clínicos de referência na base externa (a verdade lá é o desfecho da internação, alta ou morte, não um rótulo de especialista). Não registra a senioridade dos consultores, que está anonimizada. Não testa o procedimento da aprendibilidade com mais anotadores; o próprio texto pede um estudo maior para confirmá-lo.
