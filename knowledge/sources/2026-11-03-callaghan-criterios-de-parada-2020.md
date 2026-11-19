---
titulo: "Statistical stopping criteria for automated screening in systematic reviews"
tipo: paper
autor: "Callaghan, Max W.; Müller-Hansen, Finn"
url: "https://doi.org/10.1186/s13643-020-01521-4"
publicado_em: 2020-11-28
capturado_em: 2026-11-03
areas: [journalism]
tags: [stopping-rule, screening, systematic-review, active-learning, recall, hypothesis-testing, hypergeometric-distribution, machine-learning]
licenca: "CC BY 4.0 (declarada no XML JATS do artigo na Europe PMC, PMC7700715, no elemento license: 'Creative Commons Attribution 4.0 International License'; os dados do artigo ficam sob CC0, segundo a mesma declaração; o OpenAlex registra cc-by para a versão publicada)"
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Artigo em *Systematic Reviews* 9, artigo 273 (BMC), publicado em 28 de novembro de 2020; PMCID PMC7700715. Autores do Mercator Research Institute on Global Commons and Climate Change (MCC, Berlim) e do Potsdam Institute for Climate Impact Research (PIK); Callaghan também na Universidade de Leeds (Priestley International Centre for Climate). Texto lido: o XML JATS de texto completo da Europe PMC, sem as oito figuras, que no XML só têm a legenda. Código e cadernos de reprodução em https://github.com/mcallaghan/rapid-screening (não abertos).

## O problema

Na triagem de revisão sistemática com aprendizado ativo (*active learning*, AL), as pessoas rotulam documentos, o modelo aprende com esses rótulos e escolhe os próximos a mostrar, em geral os mais prováveis de serem relevantes. Assim, quase sempre se acham todos os relevantes, ou uma proporção deles (a revocação, *recall*: relevantes achados divididos pelo total de relevantes), antes de ver o corpus inteiro; a parte não vista quando se atinge a meta é o trabalho poupado (*work saved*).

Os testes costumam usar revisões já terminadas, em que todos os rótulos são conhecidos e se sabe o momento exato em que a meta de revocação foi atingida. Numa revisão de verdade a revocação só se conhece depois de ver tudo; para poupar trabalho, é preciso parar sem saber a revocação, e revocação baixa aumenta o risco de viés na revisão. A falta de critério de parada já tinha sido apontada como lacuna. O objetivo é um critério que permita declarar, por exemplo: rejeitamos a hipótese nula de ter atingido revocação menor que 95%, com nível de significância de 5%.

## Os critérios existentes e o que falha em cada um

**Critério por amostragem (Shemilt e outros):** uma amostra aleatória no início estima a taxa de inclusão de base (*Baseline Inclusion Rate*, BIR), que dá o número estimado de relevantes; para-se ao achar esse número ou a fração dele que corresponde à meta. Falha: ignora a incerteza amostral. Se a estimativa passar do número real dividido por 0,95, nunca se chega a 95% do estimado e se triam todos os documentos, sem poupar nada; se subestimar por uma unidade que seja, a revocação fica abaixo da meta. O número de relevantes tirados sem reposição segue a distribuição hipergeométrica. Exemplo da figura 1: 20.000 documentos, 500 relevantes (2,5%), amostra de 1.000. Em 48% dos casos a revocação fica abaixo de 95%; em 29% a superestimativa impede qualquer economia; só em 23% há economia com revocação de pelo menos 95%. Mesmo amostras muito grandes mantêm os dois erros frequentes. Na nota 1, os autores fazem a conta para o próprio caso de Shemilt: margem de erro de 0,0025 com proporção observada de 0,0005 dá 400 ± 451 relevantes; para reduzir a margem a ±5% do estimado seria preciso triar 638.323 de 804.919 resultados.

**Critério heurístico:** parar depois de N irrelevantes seguidos. Os autores o leem como estimativa de que a proporção de relevantes no que falta é baixa. Três problemas: ignora a incerteza; não tem descrição formal que ajude a escolher o N; e entende mal o que uma proporção baixa diz sobre a revocação. A figura 2 mostra dois cenários com os mesmos 2% de relevantes no que falta: num o modelo foi bem (74% dos triados eram relevantes), no outro foi mal (26%). Como 2% de um conjunto maior são mais documentos, a revocação depende também do número de documentos não vistos, não só da proporção. Daí duas consequências: quando o modelo vai bem, a mesma proporção baixa indica revocação menor; e num corpus com poucos relevantes a proporção baixa aparece mesmo com revocação baixa. Até um estimador perfeito da proporção não basta; é preciso o número total de relevantes não vistos.

**Critério pragmático:** parar na metade dos documentos (Wallace e outros), que funcionou no experimento deles mas não se sabe generalizar e foi desenhado com os rótulos verdadeiros à mão; ou parar quando acabar o tempo (Jonnalagadda e Petitti), sabendo que se troca revocação por menos trabalho, mas sem informação sobre a revocação provável.

**Critérios automáticos novos:** Di Nunzio, baseado em BM25, com revocação "often between 0.92 and 0.94" e sempre acima de 0,7. Yu e Menzies, também BM25, permitem fixar a revocação-alvo mas não o nível de confiança, e em dois de quatro conjuntos a mediana da revocação com meta de 95% ficou abaixo de 95%. Howard e outros estimam a revocação pelo número de irrelevantes desde o δ-ésimo relevante anterior, com binomial negativa: não quantificam incerteza (o caráter conservador é achado de simulação, não garantia), não dão código nem a equação do estimador, pedem um parâmetro δ difícil de ajustar, e como triar é amostrar sem reposição, a hipergeométrica negativa seria a distribuição certa. Em todos, a confiabilidade depende do desempenho do modelo.

## O critério proposto: teste de hipótese com a hipergeométrica

Notação: N_tot documentos; ρ_tot relevantes (desconhecido); ρ_seen relevantes já vistos; revocação τ = ρ_seen / ρ_tot. Fixam-se a revocação-alvo τ_tar e o nível de confiança α (no artigo, ambos 95%). O fluxo (figura 3): aprendizado ativo até certo ponto, depois amostragem aleatória do que falta, testando a cada documento.

1. No início da amostragem, N_AL documentos foram vistos no AL, com ρ_AL relevantes; restam N = N_tot − N_AL documentos, com K = ρ_tot − ρ_AL relevantes (desconhecido).
2. Tiram-se n documentos ao acaso do que resta; k deles são relevantes; ρ_seen = ρ_AL + k.
3. Hipótese nula: τ < τ_tar; alternativa: τ ≥ τ_tar.
4. Como a amostragem é sem reposição, k segue a hipergeométrica (N, K, n).
5. Calcula-se K_tar, o menor número de relevantes restantes compatível com a hipótese nula: K_tar = ⌊ρ_seen / τ_tar − ρ_AL + 1⌋. A nula passa a ser K ≥ K_tar.
6. p = probabilidade de ver k ou menos relevantes com a hipergeométrica (N, K_tar, n), pela função de massa acumulada. Como essa probabilidade cai quando K cresce, p é o máximo entre todos os K compatíveis com a nula.
7. Rejeita-se a nula e para-se a triagem quando p fica abaixo de 1 − α (a nota 2 aponta um caderno no repositório com o passo a passo).

**Teste do teste:** 1 milhão de amostras aleatórias em 6 cenários, variando ρ_AL para simular o início da amostragem com revocações diferentes. Desde que a revocação no início da amostragem esteja abaixo da meta, o critério dispara cedo demais em 5% dos casos, com diferença de até dois décimos de ponto percentual, e o percentil 5 da revocação atingida fica a até dois décimos de ponto de 95% (figura 4).

## A quase-amostragem ranqueada

Variante que trata blocos de documentos já triados como se fossem amostra aleatória. Para cada i, toma-se o conjunto dos documentos vistos depois do i-ésimo: N_AL vira i, n vira N_seen − i, ρ_AL vira o número de relevantes até i e k os relevantes depois; calcula-se p para todo i de N_seen − 1 a 1 e fica-se com o menor, p_min. Com a implementação vetorizada do código do artigo, o cálculo leva menos que o tempo de uma pessoa codificar o documento seguinte.

Dois usos: (1) heurística para decidir quando trocar o AL pela amostragem aleatória, com limiar mais folgado, p_min < 1 − α/2; (2) critério de parada independente, seguindo com AL até p_min < 1 − α. Ressalva dos autores: documentos ranqueados pelo modelo não são amostra aleatória, então o teste não é exato; supondo que a proporção de relevantes nesses blocos seja pelo menos tão alta quanto no que falta, o estimador fica conservador. Comparam com Howard e outros: lógica parecida, mas usa mais informação e dá teste de hipótese em vez de estimativa pontual.

## A avaliação

- **Critérios comparados:** amostragem aleatória (o proposto), quase-amostragem ranqueada, BIR de Shemilt, heurística com 50, 100 e 200 irrelevantes seguidos.
- **Medidas, em 100 rodadas por conjunto:** revocação real no momento da parada; trabalho poupado na parada (WS-SC); e carga adicional (*additional burden*), o trabalho poupado na parada menos o trabalho poupado no momento em que a meta foi de fato atingida (negativo: parou cedo demais; positivo: tarde).
- **Modelo:** SVM simples com n-gramas de 1 e 2 palavras dos resumos; amostra aleatória inicial de 200 documentos (sem o método de Shemilt para o tamanho "ótimo"); lotes dos 20 documentos de maior relevância prevista, com novo treino a cada lote. Lote menor poderia atingir a meta antes, em troca de mais tempo de computação; a escolha afeta o trabalho poupado, não a revocação. Cada critério é avaliado a cada documento. Meta de revocação e nível de confiança: 95%.
- **Dados (tabela 1):** 21 conjuntos: 15 das revisões de Cohen e colegas (2006), Proton Beam e COPD, e 4 de ciência da computação usados no FASTREAD. Vão de 284 documentos (UrinaryIncontinence, 68 relevantes, 24%) a 8.911 (Hall, 104 relevantes, 1%); a proporção de relevantes vai de 1% (Radjenovic, Wahono, Hall) a 35% (Triptans, 205 de 594). Os autores escolheram dados variados de propósito, para não ajustar o modelo a conjuntos específicos; por isso a economia, até a máxima, fica abaixo do estado da arte de cada conjunto, e mostra-se o comportamento dos critérios mesmo com modelo fraco.

## Os resultados

- **Os dois critérios propostos** atingem 95% de revocação em mais de 95% dos casos; o excesso se deve às vezes em que a amostragem começa depois de a meta já ter sido atingida, quando a hipótese nula é impossível de antemão. A quase-amostragem ranqueada ganha da aleatória nas duas frentes: poupa em média 17% do trabalho, contra 15%, e erra a meta em 0,95% dos casos, contra 3,29%. Explicação dos autores: a revocação maior vem da suposição conservadora se mostrar razoável; a economia maior, de o critério poder escolher a amostra e disparar mais cedo, sem esperar a amostra aleatória.
- **BIR:** erra a meta em 39,67% dos casos, e a economia mais frequente é 0%.
- **Heurística:** com 50 irrelevantes seguidos (IH50), poupa em média 41%, mas erra a meta em 39% dos casos; com 200, também instável.
- **Carga adicional (figura 6):** nos critérios propostos, quase sempre uma carga pequena, o custo de rejeitar a hipótese nula; nos outros, muitos casos negativos, ou seja, parada cedo e meta perdida.
- **Por conjunto (figura 7):** a economia tende a crescer com o tamanho do conjunto; com proporção baixa de relevantes, é preciso triar muito para ter confiança de que restam poucos, e a economia cai.
- **Casos (figura 8):** no Radjenovic (47 relevantes em 5.999), a meta de 95% sai cedo, mas a nula só cai bem depois: com 45 de 47 vistos e 5.029 documentos restantes, a nula é de que 3 ou mais desses 5.029 sejam relevantes, o que pede muita evidência para derrubar. No Proton Beam, ao atingir 95%, a nula era de pelo menos 13 relevantes em 3.369 restantes, ônus menor. No Statins e no Triptans o modelo foi mal e a meta saiu com quase 20% dos documentos restantes; com poucos documentos restantes, poucas decisões bastam para afastar a nula.

## A discussão e os limites declarados

- O preço da revocação confiável é poupar menos que o máximo possível; em conjuntos grandes com proporção relevante significativa, o esforço extra é pequeno perto do que se poupa, o que torna o método adequado a temas amplos com muita literatura: onde o aprendizado de máquina mais ajuda, o custo extra é menor.
- Metas de revocação e tolerâncias de incerteza diferentes cabem no mesmo critério, e a declaração de confiança comunica o uso de aprendizado de máquina a leitores e revisores que não são especialistas.
- O critério independe do modelo: modelo ruim só reduz a economia; nos outros critérios, modelo ruim pode baixar a revocação. Revocação baixa enviesa a revisão; economia baixa não custa nada em relação a não usar aprendizado de máquina.
- **Limite declarado:** o problema dos testes múltiplos (testar a cada documento) não foi tratado formalmente, por ser matematicamente difícil e fora do escopo; o desempenho observado indica, segundo os autores, preocupação prática limitada, e a formalização fica para pesquisa futura.
- Os padrões de revisão sistemática ainda não preveem triagem com aprendizado de máquina; os autores esperam que a confiabilidade e a clareza do relato permitam incluir o critério neles.

## Tudo o mais que ensina

- **Vocabulário:** revocação é a fração dos relevantes achada; trabalho poupado é a fração do corpus não triada; a "carga adicional" mede o atraso ou o adiantamento da parada em relação ao momento ideal, que numa revisão real nunca se conhece.
- **Por que hipergeométrica e não binomial:** triar é tirar documentos sem reposição de um conjunto finito; a binomial (ou a binomial negativa) é aproximação aceitável só com muitos documentos.
- **Por que o pior caso:** testar com K_tar, o menor K compatível com a hipótese nula, dá a maior probabilidade possível de ver tão poucos relevantes se a meta não tivesse sido atingida; é isso que permite falar em nível de confiança.
- **Ligação com intervalos de confiança:** os autores lembram que argumentos parecidos servem para intervalos de confiança do parâmetro K da hipergeométrica, e que um critério equivalente poderia usar o limite superior desse intervalo.
- **Financiamento:** bolsa de doutorado da Fundação Heinrich Böll (Callaghan) e o projeto START do Ministério Federal de Pesquisa e Educação da Alemanha (Müller-Hansen). Sem conflitos de interesse declarados.
