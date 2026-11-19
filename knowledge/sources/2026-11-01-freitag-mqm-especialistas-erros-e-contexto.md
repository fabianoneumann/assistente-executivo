---
titulo: "Experts, Errors, and Context: A Large-Scale Study of Human Evaluation for Machine Translation"
tipo: paper
autor: "Markus Freitag, George Foster, David Grangier, Viresh Ratnakar, Qijun Tan, Wolfgang Macherey (Google Research)"
url: "https://aclanthology.org/2021.tacl-1.87/"
publicado_em: 2021-12-01
capturado_em: 2026-11-01
licenca: "CC BY 4.0 (rodapé da primeira página do PDF da TACL: 'Distributed under a CC-BY 4.0 license'; o rodapé do ACL Anthology diz o mesmo para material de 2016 em diante)"
areas: [agent-engineering]
tags: [mqm, error-annotation, error-typology, severity-weighting, human-evaluation, scalar-rating, ceiling-effect, inter-rater-agreement, expert-vs-crowd, machine-translation, ranking-stability]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Publicado na Transactions of the ACL, vol. 9, p. 1460 a 1474, em dezembro de 2021 (submissão em 5/2021, revisão em 8/2021), DOI 10.1162/tacl_a_00437; o preprint é o arXiv 2104.14478 (v1 em 29/04/2021, licença CC BY-SA 4.0). Lida a versão da TACL, que difere do preprint: a TACL acrescenta a tabela de estabilidade dos pesos (Tabela 3) e a de concordância entre pares de avaliadores (Tabela 9), e tira a seção sobre quantas notas são necessárias, que só o preprint tem (contada abaixo, marcada como do preprint). Seis autores do Google Research. Dados liberados em https://github.com/google/wmt-mqm-human-evaluation. Texto extraído com `pdftotext`; as tabelas saem embaralhadas e os números citados aqui foram lidos nas linhas das tabelas e conferidos contra o texto. É o estudo que levou o MQM a ser a avaliação humana oficial da tarefa de métricas da WMT a partir de 2021. Lido para a rodada investigativa (juiz das peças).

**Atenção ao domínio:** tradução automática de notícias, inglês para alemão e chinês para inglês, avaliada por tradutores profissionais. O que transfere para as nossas peças é o desenho da medida (anotar erros e derivar a nota), não os números.

## 1. A pergunta e a tese

Quando a qualidade das saídas sobe, a avaliação por nota única feita às pressas, frase a frase, por avaliadores sem formação, deixa de separar o bom do ótimo: o sinal se perde no ruído e no viés de quem avalia. A tese central: **toda nota ou ordenação de traduções já se apoia, implicitamente, em identificar erros e imperfeições**; tornar essa identificação explícita, listando os erros, dá um padrão "platina" do qual se derivam várias notas, conforme o peso que cada uso dá a cada categoria de erro. Essa é a base conceitual do MQM, criado nos projetos europeus QTLaunchPad e QT21.

## 2. Três formas de avaliar, comparadas nas mesmas saídas

- **WMT 2020 (a de referência na época):** nota de 0 a 100 por segmento, com contexto do documento, dada por pesquisadores e tradutores (inglês para alemão) ou por trabalhadores de plataforma (chinês para inglês, comparando com uma tradução de referência). Menos de uma nota por segmento sobrevive ao controle de qualidade.
- **SQM (Scalar Quality Metric):** escala de 0 a 6 com descritores (6, sentido e gramática perfeitos; 4, quase todo o sentido e poucos erros de gramática; 2, parte do sentido; 0, sem sentido), aplicada por trabalhadores de plataforma (cSQM) e por tradutores profissionais (pSQM).
- **MQM:** tradutores profissionais marcam cada erro no trecho exato, com categoria e gravidade, com o documento inteiro à vista; a nota sai da soma ponderada.

Seis tradutores para pSQM e outros seis para MQM (grupos separados, para não contaminar), três notas por segmento, documentos e sistemas anônimos e em ordem aleatória. Dez "sistemas" por par de línguas, incluindo as traduções humanas de referência (três em inglês para alemão, uma delas uma paráfrase deliberada; duas em chinês para inglês). Cerca de 1.418 segmentos (130 documentos) e 2.000 segmentos (155 documentos). **O MQM custou cerca de três vezes o SQM**, que custou o mesmo com profissionais e com plataforma.

## 3. Como o MQM foi montado aqui

- **Diretrizes (Tabela 1):** marcar todos os erros de cada segmento, até cinco; acima de cinco, só os cinco mais graves. Segmento incompreensível demais para separar erros leva um erro especial "não tradução", que cobre o segmento inteiro. Ser o mais granular possível (duas palavras mal traduzidas são dois erros); num mesmo trecho com vários erros, marcar o mais grave; empate de gravidade, a primeira categoria da lista. O contexto do documento decide: o que parece errado isolado mas está certo no documento não é erro, e vice-versa. Erros da fonte se marcam à parte e não contam no limite.
- **Hierarquia (Tabela 2):** as categorias de topo padrão, Precisão (accuracy: adição, omissão, má tradução, texto não traduzido), Fluência (gramática, ortografia, pontuação, registro, inconsistência, codificação de caracteres), Terminologia, Estilo (construção estranha) e Convenções locais (formato de nome, moeda, endereço etc.), mais "não tradução" e "outro".
- **Gravidade, independente da categoria:** Maior (erro de verdade, de tradução ou de gramática), Menor (imperfeição) e Neutra (opinião subjetiva, que não pesa). **A gravidade Crítica foi tirada** de propósito, porque a definição dela depende do contexto e a distinção entre maior e crítico seria muito subjetiva numa avaliação ampla; a distinção entre maior (erro) e menor (imperfeição) seria mais fácil.
- **Pesos, escolhidos por estabilidade:** menor fixo em 1; para o maior, testaram de 1 a 10 (o 10 era a sugestão do padrão MQM), e um peso especial para pontuação menor. Para cada combinação, sortearam 10 mil conjuntos de teste com reposição e contaram em que fração deles a ordenação completa dos sistemas era a mesma do conjunto inteiro (Tabela 3). A combinação **maior 5, menor 1, pontuação menor 0,1** deu a melhor estabilidade combinada e manteve a mesma ordenação do pSQM. Os números de estabilidade são baixos: 39% em inglês para alemão e 28% em chinês para inglês, com essa combinação. Pontuação menor (aspas, espaço) pesa 0,1 porque é fácil de corrigir por algoritmo e não muda o sentido; serve só para desempatar. "Não tradução" vale 25, o mesmo que cinco erros maiores, o máximo permitido, o que dá à nota de um segmento um teto definido (de 0, perfeito, a 25, pior). A nota do segmento é a média entre os avaliadores; a do sistema, a média dos segmentos.

## 4. Resultados

- **Os profissionais separam humano de máquina; a plataforma não.** No pSQM e no MQM, todas as traduções humanas ficam à frente de todos os sistemas, e no MQM com folga grande. A paráfrase humana, que a plataforma pôs perto do fim (avaliadores leigos preferem traduções literais, fáceis de conferir), os profissionais puseram acima de qualquer máquina. No MQM, quem avalia precisa justificar a nota marcando o trecho do erro, o que evita punir a tradução não literal.
- **A nota única dos leigos se espreme no alto.** Em inglês para alemão, a nota de plataforma (cSQM, de 0 a 6) dos dez sistemas vai só de 4,85 a 5,31; a de profissionais (pSQM) vai de 3,32 a 5,16; o MQM vai de 0,75 a 2,99 pontos de erro por segmento, quatro vezes entre o melhor e o pior. Em chinês para inglês, o cSQM vai de 4,83 a 5,11. A ordenação da WMT tem correlação baixa com a do MQM em inglês para alemão e **negativa** em chinês para inglês, e a correlação segmento a segmento é muito baixa nas duas.
- **pSQM e MQM concordam na ordem dos sistemas, mas não segmento a segmento** (Kendall perto de 0,5 no segmento). Quando dois sistemas ficam próximos, a nota de profissionais quase não os separa (diferença de 0,04 entre dois sistemas no pSQM, contra 0,19 no MQM). A conclusão dos autores: quando as saídas se aproximam, uma avaliação mais fina como o MQM é necessária; para uma campanha que só ordena sistemas distantes, o pSQM basta.
- **O que move a nota são os erros maiores e os de precisão.** A ordem só pelos erros maiores, ou só pelos de precisão, é quase a mesma da nota inteira; a maioria dos erros maiores é de precisão (má tradução, sobretudo), e a maioria dos de fluência é menor.
- **A distribuição por categoria diagnostica.** Os sistemas têm cerca de quatro vezes mais pontos de má tradução que os humanos e 28 vezes mais segmentos de "não tradução"; os humanos só perdem em adição (acrescentam palavras por fluência). Sistemas do topo têm perfis diferentes: um é médio em fluência e excelente em precisão, outro o contrário. A lista de erros mostra isso; a nota única esconde.
- **Os erros dos sistemas dependem do documento.** A qualidade humana é estável entre documentos (cerca de um erro menor por segmento em inglês para alemão); a das máquinas varia, e todos os sistemas tropeçam no mesmo subconjunto de documentos: a dificuldade é da entrada, não só do sistema.
- **Concordância entre avaliadores (Tabela 9).** Como uma anotação MQM é uma lista de tamanho variável de pares (categoria, gravidade), os autores agruparam as notas em sete faixas (limites 0, 5, 10, 15, 20, 24,99 e 25) e mediram a concordância entre pares de avaliadores nas faixas. MQM: média de 0,584 em inglês para alemão (de 0,536 a 0,663) e 0,412 em chinês para inglês (0,356 a 0,488). pSQM: 0,304 (0,221 a 0,447) e 0,169 (0,008 a 0,517). Concordância significativamente maior com MQM nos dois pares: basear a nota em erros explícitos dá um ganho mensurável de confiabilidade. O texto chama a medida de "agreement" sem dizer se é concordância simples ou corrigida pelo acaso.
- **Avaliadores diferem em severidade e em hábito.** Em inglês para alemão, todos ficam a até 20% da média (um mais severo, um mais leniente); um quase não usa a categoria de estilo, outro usa muito. Em chinês para inglês, a até 30%, talvez pela ambiguidade maior da tarefa.
- **Métricas automáticas contra MQM.** Com o MQM como gabarito, a ordem das métricas muda por completo; quase todas correlacionam mais com o MQM do que a avaliação humana da própria WMT, e as baseadas em representações pré-treinadas superam os avaliadores de plataforma.

## 5. Só no preprint (arXiv v1): quantas notas bastam

Simulando projetos novos por reamostragem dos dados MQM, a ordem dos sistemas se aproxima da do conjunto inteiro quando há mais notas, e, para um orçamento fixo de notas, é melhor espalhar poucos segmentos seguidos (três) por muitos documentos do que muitos segmentos por poucos documentos. Alinhar os mesmos documentos e segmentos (e, se possível, os mesmos avaliadores) entre os sistemas comparados deixa a comparação mais precisa.

## 6. Conclusão e limites dos autores

Propõem um esquema de pontuação MQM para tradução de alta qualidade e liberam o maior corpus MQM até então. A avaliação de plataforma correlaciona pouco com o MQM e põe em dúvida conclusões tiradas dela, sobretudo para tradução de alta qualidade (a "paridade humana" anunciada antes não se sustenta). Limites que se leem no texto: dois pares de línguas, um domínio (notícias), seis avaliadores por método, pesos escolhidos pela estabilidade da ordem e não por validade externa, e a concordância medida sobre faixas de nota, não sobre os erros um a um.

## 7. Tudo o mais que ensina

- **Lista de erros como dado primário, nota como derivada.** A mesma anotação gera notas diferentes para usos diferentes (só erros maiores, só precisão, peso alto para terminologia), sem anotar de novo.
- **O teto por segmento é uma escolha de desenho.** Limitar a cinco erros e dar à "não tradução" o peso de cinco maiores fecha a escala; sem isso, a soma cresce sem limite com o tamanho do segmento.
- **O peso que separa erro de imperfeição foi calibrado pela estabilidade da ordem**, não pelo dano ao leitor; é uma escolha estatística declarada.
- **Corte de categoria "barata de consertar por algoritmo":** pontuação e espaço com peso quase nulo, porque um passo automático corrige; a função dela é desempatar.
- **A gravidade "neutra"** registra preferência subjetiva sem punir, o que deixa o avaliador dizer o que pensa sem inflar a contagem.
- **A justificativa obrigatória protege o não literal:** exigir o trecho do erro impede punir a solução diferente que está certa.
- **A dificuldade vem da entrada:** todos os sistemas erram nos mesmos documentos, o que aconselha olhar o erro por tipo de entrada, e não só por sistema.
