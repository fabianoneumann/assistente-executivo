---
titulo: "Expert panel as reference standard procedure in diagnostic accuracy studies: a systematic scoping review and methodological guidance"
tipo: paper
autor: "Bas E. Kellerhuis, Kevin Jenniskens, Mike P. T. Kusters, Ewoud Schuit, Lotty Hooft, Karel G. M. Moons, Johannes B. Reitsma"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12070646/"
publicado_em: 2025-05-13
capturado_em: 2026-11-04
licenca: "Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND), escrita na página do PMC; pela cláusula NC (decisão de 2026-11-01) entra só a ficha, e o integral está na url (PMC12070646)"
areas: [agent-engineering]
tags: [expert-panel, reference-standard, adjudication, consensus, tiebreaker, uncertainty, incorporation-bias, reporting-guidelines, medical-annotation]
---

# Kellerhuis et al. 2025 (Diagnostic and Prognostic Research): como os painéis de especialistas são montados e relatados

Ficha em palavras próprias, em estrutura própria (artigo de acesso aberto com NC e ND: o integral não entra). Lida no texto bruto da página do PMC em 2026-11-04; DOI 10.1186/s41512-025-00195-7, volume 9, artigo 12. Revisão de escopo (PRISMA-ScR, sem protocolo registrado) que atualiza uma revisão anterior (Bertens et al., 2013, PLoS Medicine, que achara 83% dos estudos sem alguma informação crítica sobre o painel). Mapeia o uso do painel de especialistas como padrão de referência em estudos de acurácia diagnóstica, quando não existe teste único que diga se a doença está presente.

## Método da revisão

PubMed, publicações de 1/6/2012 a 1/10/2022 (busca de 6/10/2022), com ajuda de bibliotecário; entram estudos de acurácia de um teste ou modelo em que um painel de especialistas serve de referência, em inglês, holandês ou alemão. 4.078 registros; 3.524 excluídos no título e resumo; 32 sem texto completo; 204 excluídos no texto completo; 318 estudos analisados. Um autor extraiu os dados e outro conferiu os casos duvidosos; um pesquisador júnior conferiu uma amostra de 30 artigos (kappa de 0,87 a 1,0 nos itens). Só o PubMed foi pesquisado.

## Quem são os estudos

Oncologia 20%, cardiologia 16%, doenças infecciosas 14%, neurologia 13%, pneumologia 7,9%. O teste avaliado era um software (IA ou aprendizado de máquina) em 31%. Participantes por estudo: mediana 139 (percentis 25 e 75: 68 e 351); menos de 100 em 32% e mais de 500 em 17%.

## Como os painéis são compostos

- **Tamanho:** de 1 a 20 especialistas por painel (mediana 3); 3 especialistas em 46% dos estudos. O resumo dá dois ou menos em 29%, três ou quatro em 55% e cinco ou mais em 16%; a tabela, que inclui os não relatados (13%), traz 25%, 48%, 11% (cinco a nove) e 2,4% (dez ou mais).
- **Quem julga:** em mais de 75% o mesmo grupo avalia todos os participantes; em 13% sai de um conjunto maior (de 1 a 261 especialistas no estudo, mediana 3); 12% não dizem. Mesma especialidade em 63%, mista em 23%, não relatada em 13%.
- **O que o painel recebe:** história clínica, biomarcadores, imagem, acompanhamento. Em 18% dos estudos o resultado do teste avaliado entra nas informações dadas ao painel, quase sempre em estudos comparativos em que o novo teste substitui um já usado na prática (por exemplo, uma tomografia de melhor qualidade contra a atual). Em 6% não se sabe.
- **Dados já rotulados:** em 4% o painel já tinha julgado os participantes antes do estudo (banco de dados, estudo prévio); nos demais montou-se um painel novo.
- **Verificação diferencial:** pelo menos 8% dos estudos avaliaram parte dos participantes por outro meio (por exemplo, autópsia para quem morreu e painel para quem viveu).

## Os quatro tipos de painel, por como se decide

1. **Independente (104 estudos, 33%):** cada especialista julga sozinho; os votos se combinam por uma regra prévia (por exemplo, mais de 50% concordam) ou os casos sem unanimidade saem.
2. **Consenso (86, 27%):** os especialistas discutem cada caso juntos e buscam unanimidade; se sobra discordância, usa-se regra prévia (maioria) ou um desempatador.
3. **Em etapas (36, 11%):** julgamento independente; se todos concordam, está decidido; se não, discutem juntos e tentam a unanimidade.
4. **Com desempatador (26, 8%):** julgamento independente; se discordam, um especialista que não participou da primeira rodada decide, e a decisão dele vale como o estado da doença.

Em 20% a 21% dos artigos (a revisão dá os dois números) não foi possível determinar como o painel chegou ao julgamento. Nos painéis independentes, muitas vezes só havia dois especialistas e nenhuma explicação do que acontecia na discordância.

## Incerteza e exclusão

- Em cerca de 5% dos estudos (o texto também diz 4% numa passagem) pediu-se aos membros do painel que registrassem o grau de certeza sobre cada paciente: nota de 1 a 10, percentual, marca num diagrama, ou categorias como "provavelmente presente", "provavelmente ausente", "certamente ausente". Alguns usaram essa medida só para excluir quem tinha muita incerteza.
- Alguns estudos excluíram os participantes em que o painel não concordou. Os autores recomendam fortemente contra, porque excluir os casos difíceis superestima a acurácia do teste.
- Forçar a classificação em presente ou ausente ignora a incerteza que sobra e pode enviesar as estimativas de acurácia (apoiam-se numa simulação de Jenniskens et al., 2019). Há métodos em desenvolvimento para usar a incerteza no cálculo da acurácia.

## O que mais os autores discutem

- **Viés de incorporação.** Dar ao painel o resultado do teste avaliado pode fazer esse resultado pesar indevidamente no julgamento e enviesar a acurácia; reter a informação pode, por outro lado, piorar a classificação do painel. Segundo os autores, é difícil prever qual efeito domina, então a recomendação geral é conservadora: não mostrar ao painel o resultado do teste em avaliação.
- **Relato incompleto.** Faltam informações-chave (número e especialidade dos membros, informação disponível ao painel, se inclui o teste avaliado, regra de decisão), o que impede replicar e avaliar o risco de viés. As diretrizes STARD e TRIPOD pedem o relato da referência, mas não detalham o painel; os autores pedem uma extensão e citam uma diretriz em preparação (LEADING, para estudos de painel de especialistas e diagnóstico de melhor estimativa).
- **IA e multidões.** A possibilidade de um grande grupo de não especialistas substituir um pequeno grupo de especialistas em algumas condições é citada como oportunidade vinda de outros campos (exemplo: avaliação por multidão de habilidades técnicas em laparoscopia).
- **Lacunas de pesquisa que eles apontam:** não há orientação sobre o desenho ideal do painel (custo, tempo dos especialistas, dificuldade do diagnóstico, desempenho como referência); o efeito do número de especialistas sobre a qualidade da classificação segue em aberto; a relação entre painel e modelos de classes latentes, ou o uso dos dois juntos, merece estudo.

## Recomendações da tabela 3

Pedir aos especialistas uma medida de incerteza e usá-la na análise; não excluir participantes em que o painel discorda; descrever com clareza o processo (número de especialistas, expertise, informação disponível, participantes avaliados, procedimento de decisão e o que acontece na discordância); seguir uma diretriz de relato, como STARD ou TRIPOD.

## Limites declarados

Busca só no PubMed; revisão de escopo, não sistemática completa; os resultados não valem necessariamente para pesquisa prognóstica, de intervenção ou para painéis de adjudicação clínica que confirmam desfechos.

## O que a fonte não diz

Não mede a acurácia de nenhum tipo de painel nem compara os quatro tipos entre si; não diz quantos especialistas bastam; não traz as taxas de discordância dos painéis dos estudos incluídos.
