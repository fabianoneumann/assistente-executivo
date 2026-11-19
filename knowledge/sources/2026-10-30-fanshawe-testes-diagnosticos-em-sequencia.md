---
titulo: "A review of methods for the analysis of diagnostic tests performed in sequence"
tipo: paper
autor: "Thomas R. Fanshawe, Brian D. Nicholson, Rafael Perera, Jason L. Oke"
url: "https://doi.org/10.1186/s41512-024-00175-3"
publicado_em: 2024-09-03
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada no PDF da revista, 'licensed under a Creative Commons Attribution 4.0 International License', e no XML do PMC, PMC11370044)"
areas: [agent-engineering]
tags: [cascade, sequential-testing, conditional-dependence, correlated-errors, decision-rules, sensitivity, specificity, imperfect-reference-standard, diagnostic-accuracy]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Revisão metodológica publicada na Diagnostic and Prognostic Research 8:8 (BMC), em 03/09/2024 (recebida em 21/11/2023, aceita em 26/06/2024); versão única no PMC (PMC11370044.1). Universidade de Oxford (Nuffield Department of Primary Care Health Sciences). O texto lido é o XML de texto completo da Europe PMC; os números foram conferidos também no PDF da revista. O material suplementar (a tabela-guia e a especificação do modelo bayesiano) não foi aberto. Lida (camadas flexíveis de avaliação).

## A pergunta

Muitos caminhos de diagnóstico clínico encadeiam testes: um exame de laboratório que separa quem tem mais risco, depois imagem, depois biópsia. Uma revisão citada pelos autores achou testes múltiplos em 16 de 22 caminhos diagnósticos das avaliações de tecnologia em saúde publicadas entre 2009 e 2015. O desempenho da sequência inteira depende do desempenho de cada teste **e da dependência condicional entre eles, dada a verdadeira condição de doença**. Os autores revisam os métodos estatísticos para estimar o desempenho (sensibilidade, especificidade, valores preditivos) de testes feitos em sequência, para orientar o analista à classe de método que serve ao desenho e ao objetivo da sequência.

Quando o caminho é fixo, conhecido de antemão e pode ser estudado inteiro, os passos da análise podem ser parecidos com os de um teste único. Mas muitas vezes é preciso desenvolver um modelo para decidir onde atribuir diagnósticos positivos e negativos no caminho, e os recursos para estudar o caminho inteiro podem ser proibitivos; com frequência só há informação parcial de cada teste, às vezes de estudos diferentes em cenários diferentes, e montar o caminho exige incorporar a dependência entre os resultados, por suposição adicional ou por estimativa publicada.

## Os desenhos: paralelo, condicional e combinação simultânea

- **Testes simultâneos combinados:** vários testes feitos ao mesmo tempo, combinados numa decisão (por exemplo, um escore de risco a partir de exames de sangue); já há métodos para a combinação ótima (regressão, análise discriminante, maximizar a área sob a curva ROC).
- **Testes em sequência, separados no tempo:** o resultado de um é conhecido antes do seguinte. Exemplos: o teste rápido repetido para SARS-CoV-2; na tuberculose latente, oferecer primeiro o teste cutâneo e fazer o ensaio de interferon gama só em quem teve o cutâneo positivo. A decisão de fazer os testes posteriores depende dos resultados já vistos; em geral, o diagnóstico sai do último teste feito.
- O padrão em que o teste seguinte depende do anterior se chama **"teste condicional"** ou **"teste serial"**, em contraste com o **"teste paralelo"**, em que todos os testes são feitos em todos os participantes, qualquer que seja o resultado.
- **O desenho condicional da Fig. 1:** se o teste 1 dá negativo, o diagnóstico negativo sai direto, sem o teste 2. Isso pode reduzir o ônus para o paciente e o custo. Mas **um falso negativo de um teste 1 de baixa sensibilidade impede que o teste 2 seja usado justamente em quem tem a condição**, e isso prejudica o desempenho da sequência mesmo que o teste 2 tenha alta sensibilidade. O texto da Fig. 1 não dá nome de regra a esse desenho. Esse desenho já foi chamado de desenho "pareado" e se estende a mais testes e regras mais complicadas.

## Método da revisão

Três etapas: (1) 18 artigos que os autores já conheciam; (2) busca no PubMed restrita a cinco revistas que já publicavam na área (Biometrics, Biostatistics, Journal of Biopharmaceutical Statistics, Statistical Methods in Medical Research, Statistics in Medicine); (3) busca de citações uma geração para a frente e para trás, no Scopus e na Web of Science, sem restrição de revista. Em cada etapa, dois pesquisadores triaram de forma independente (título e resumo, depois texto completo se preciso).

- **Entraram:** métodos estatísticos para a acurácia diagnóstica de dois ou mais testes distintos em sequência ou num caminho; de testes repetidos (o mesmo teste em duas ou mais ocasiões); de sequências dentro de programas de rastreamento; e artigos que juntam a sequência a outro problema, como padrão de referência imperfeito ou parcial.
- **Ficaram de fora:** estudos primários de um teste; revisões sistemáticas de um teste; testes de hipótese sequenciais para outros fins; artigos só de prevalência; métodos para comparar dois testes e escolher o melhor, em vez de juntá-los num caminho.
- A busca **não foi desenhada para ser sistemática**, pela dificuldade de buscar na área; o alvo eram as classes de método mais proeminentes. Os artigos foram agrupados em temas pelo objetivo e pelo tipo de método. O foco é o caso de teste e doença binários, o mais comum na clínica, com menção aos testes contínuos.

Saíram cinco grupos (Tabela 1): (1) combinar resultados de testes em sequência, mais adequado quando todos fazem todos os testes; (2) estimar a dependência condicional e lidar com o teste condicional, quando nem todos fazem todos os testes; (3) sequências para avaliação de risco, com o mesmo teste repetido, em rastreamento ou monitoramento; (4) sequências com padrão de referência imperfeito ou incompleto; (5) metanálise.

## 1. Combinar os resultados de testes em sequência

### As regras do E e do OU (dois testes)

No caso mais simples, **dois testes binários são feitos em todos os participantes** (resultados X1 e X2; T é a condição verdadeira). Duas regras simples:

- **Regra do OU**, também chamada "believe the positive" ou "Any+": diagnóstico positivo se X1 **ou** X2 for positivo.
- **Regra do E**, também chamada "believe the negative" ou "Both+": diagnóstico positivo só se os dois forem positivos.
- Nesses casos, X2 pode ser visto como teste "add-on" a um teste já estabelecido X1, ou X1 como um novo teste de triagem antes de um X2 já estabelecido.
- **Terceira regra, "believe the extreme":** X2 só é feito nos participantes com resultado **indeterminado** em X1, e o diagnóstico é positivo se qualquer dos dois for positivo.

Há expressões algébricas para a sensibilidade e a especificidade da combinação em função da sensibilidade e da especificidade de cada teste **e da dependência condicional entre eles** (no Apêndice). Termos condicionais como P(X2 | X1, T) nessas expressões mostram a influência direta da dependência condicional sobre o desempenho da sequência.

### O efeito da dependência condicional

- Com dados só de estudos que avaliaram cada teste isolado, estimar os termos que envolvem X1 e X2 juntos é problemático. A saída mais simples é supor P(X2=0 | X1=0, T=1) = P(X2=0 | T=1), a **suposição forte de independência condicional** dada a condição de doença.
- De forma geral, a sensibilidade e a especificidade combinadas se reescrevem com o coeficiente phi, as **correlações condicionais ρ+ e ρ−** entre os resultados dos testes entre os doentes e entre os não doentes.
- A faixa possível da covariância condicional é limitada pela sensibilidade e especificidade marginais de cada teste. No extremo de correlação condicional perfeitamente negativa, os testes sempre discordam: a sensibilidade do OU vira 1 e a do E vira 0; a especificidade do OU vira 0 e a do E vira 1.
- **Sob a regra do OU:** a sensibilidade combinada **aumenta quando os testes são condicionalmente correlacionados de forma negativa entre os doentes**; a especificidade combinada **aumenta quando são correlacionados de forma positiva entre os não doentes**. **Sob a regra do E, valem as conclusões opostas.** A relação entre a força das correlações e o desempenho das regras já foi explorada numericamente.
- **Valores preditivos:** na maioria dos cenários realistas, o OU tende a baixar o VPP e subir o VPN, e o E tende a subir o VPP e baixar o VPN; a tendência não é garantida e pode não ocorrer quando os testes são altamente correlacionados, com correlação de força diferente entre doentes e não doentes.

### Outras medidas de desempenho

- O ganho de acrescentar um teste pode ser medido por razões de verossimilhança positiva e negativa, por testes da diferença ou da proporção de diagnósticos corretos adicionais, ou por taxas relativas de verdadeiro e falso positivo e pela curva ROC relativa.
- O mesmo princípio se estende ao custo em termos de economia da saúde, quando se quer minimizar o custo total e os custos relativos de cada acerto e erro são quantificáveis: serve para testar se o ganho diagnóstico dos testes seguintes, pela regra do OU ou do E, justifica o custo adicional.
- Há quem meça o efeito do teste adicional no kappa ponderado de concordância entre testes, medida difícil de interpretar como desempenho clínico.
- Um método alternativo, para manter as taxas de falso positivo e falso negativo dentro de limites, classifica ao acaso uma parte dos resultados discordantes como positivos e o resto como negativos; a desvantagem é que duas pessoas com resultados idênticos podem receber diagnósticos diferentes.
- Para testes contínuos com limiar, há expressões da sensibilidade e especificidade combinadas; os limiares podem ser fixos ou adaptativos (mudam conforme a ordem na sequência). Como a sensibilidade da sequência se escreve como a sensibilidade do primeiro teste e a sensibilidade condicional do segundo dado o primeiro, conhecendo esses parâmetros dá para buscar os limiares que atingem um desempenho-alvo da sequência inteira.

### Mais de dois testes

- O número de combinações e sequências cresce exponencialmente com o número de testes, e a maioria não se escreve como OU ou E simples. Regras com nome: a da **maioria** (positivo se mais da metade dos resultados for positiva) e a da **unanimidade** (generalização do E: positivo só se todos forem positivos).
- Com muitos testes, escolher a combinação ótima vira um problema de otimização parecido com o "problema da mochila"; essa formulação não leva em conta a variabilidade amostral dos testes.
- Com dados para modelar, a combinação se generaliza para tempo contínuo (monitorar se um biomarcador modelado ao longo do tempo passa de um limiar, talvez variável, durante o seguimento).
- Alguns métodos supõem a regra de decisão já definida e o desempenho de cada teste e a correlação condicional já conhecidos; servem, por exemplo, para escolher o número de rastreamentos repetidos ou a ordem dos testes que minimiza o custo controlando as taxas de erro. Um "gráfico de modificação de probabilidade" mostra como a probabilidade condicional de doença muda a cada resultado acrescentado.

### Criar uma regra nova

Quando a regra não está predefinida, usam-se métodos multivariados: regressão logística (para testes binários e contínuos), análise discriminante e métodos "livres de distribuição" que maximizam, por exemplo, o estimador de Mann-Whitney da área sob a curva ROC. Na forma usual, só servem se todos os participantes têm resultado em todos os testes.

## 2. Estimar a dependência condicional e o teste condicional

Quando nem todos fazem todos os testes, porque a decisão de fazer o seguinte depende dos resultados já vistos, estimar a dependência entre os testes, condicional à condição verdadeira, fica mais importante, porque ela afeta o desempenho da sequência inteira.

- **Sequência com parâmetros conhecidos:** Hershey e colegas, entre os primeiros, derivaram expressões da utilidade clínica (impacto quantificável em desfechos de saúde) de sequências com teste condicional e de mudanças na ordem dos testes. Supõem conhecidos a prevalência, o desempenho, a dependência condicional e a utilidade. Os resultados deles indicam que esses parâmetros juntos ditam a sequência ótima, que isso depende do contexto e que, **para algumas combinações de parâmetros, testar mais pode piorar o desempenho da sequência**.
- Levy e Kass derivaram estimadores de máxima verossimilhança da prevalência e da especificidade, com sensibilidade conhecida, numa sequência condicional de três estágios (só quem deu positivo segue), no rastreamento de bacteriúria.
- **Estimar sem levar em conta o teste condicional dá estimativas em geral enviesadas**, com o tamanho do viés dependendo, entre outros fatores, da prevalência e da dependência condicional; mostrado na teoria e em simulação.
- Por isso há testes da presença de dependência condicional, como um teste de razão de verossimilhança da hipótese ρ+ = 0 (e/ou ρ− = 0). O grau de dependência já foi proposto para decidir a ordem dos testes pelo uso repetido do teorema de Bayes, e isso foi desenvolvido com redes bayesianas.
- Uma forma de modelar é tratar os dados como realização de uma multinomial cujos parâmetros vêm da prevalência π e das sensibilidades e especificidades (verossimilhança no Apêndice); às vezes os termos condicionais se estimam dos dados, e o modelo também serve sem padrão de referência ou com ele incompleto.
- **Escala latente:** o resultado binário pode ser visto como uma medida contínua latente U que passa de um limiar c; a dependência condicional fica governada pela correlação nessa escala. Supor uma forma de distribuição para U, com uma variância de erro de medida, **induz correlação condicional entre os resultados mesmo que os erros de medida sejam independentes**. A ideia se estende a duas variáveis latentes ligadas por uma cópula; na maioria dos cenários esse modelo não é identificável (exige parâmetros fixados ou priors informativas) e não se popularizou.

## 3. Sequências para avaliação de risco

Forma particular de teste condicional ao avaliar risco de doença futura (rastreamento de pressão alta, monitoramento de retinopatia em diabéticos). Difere em pelo menos dois pontos: muitas vezes se quer sensibilidade alta nas fases iniciais; e é comum repetir o mesmo teste, numa sequência condicional ou em consultas periódicas.

- **Rastrear em n ocasiões e declarar positivo com pelo menos k positivos** (Lau, depois de Nissen-Meyer): conhecido o desempenho de um teste, escolher n e k para atingir um critério, como certas taxas de falso positivo e falso negativo (Fig. 2, com n = 4 e k = 3). Desenvolvido primeiro com resultados condicionalmente independentes e depois, por momentos canônicos, com dependência.
- Há métodos para a probabilidade de aparecer um falso positivo em algum ponto da sequência, sem e com teste condicional; sequências em que só quem dá positivo segue se modelam com multinomiais condicionais, com extensão para covariáveis individuais.
- Com teste contínuo, a forma da curva ROC da sequência se modela em função da correlação entre testes e do número de testes por pessoa (que pode depender do resultado); sem levar isso em conta, o desempenho aparente da sequência fica afetado.
- **Métodos de teoria da decisão**, com critério de custo: para interpretar uma sequência de rastreamento com n = 2 num quadro bayesiano e para escolher k; mais adequados ao mesmo teste repetido, mas aplicáveis a testes diferentes se o desempenho de cada um for conhecido.
- A organização de um programa de avaliação de risco (agenda ótima, troca de um teste por outro) fica fora do escopo.

## 4. Padrão de referência imperfeito ou incompleto

Problema comum, sobretudo com teste condicional: o padrão de referência classifica mal. Pode ser **imperfeito** (todos fazem, alguns são diagnosticados errado) ou faltar para alguns ou todos (**verificação parcial**). Não é específico de sequências, e já há revisões desses métodos, mas aparece muito nelas, e o próprio uso do padrão de referência às vezes depende do resultado dos testes (no rastreamento, quem deu positivo tem mais chance de fazer a confirmação; Fig. 3, em que só quem dá positivo em um dos dois testes faz o padrão de referência). Estimativas sem ajuste são enviesadas quando a verificação da doença é incompleta; há estimadores de máxima verossimilhança ajustados.

- **Modelo multinomial de variável latente:** uma parametrização (de Vacek, muito usada desde então) reescreve as probabilidades conjuntas, como a sensibilidade do E, com parâmetros de covariância condicional; como esses parâmetros ficam numa faixa limitada pelo desempenho de cada teste, dá para obter limites superior e inferior da acurácia quando o padrão de referência é imperfeito. O modelo totalmente parametrizado não é identificável: parte dos parâmetros precisa ser fixada ou receber prior informativa. Extensões: covariáveis individuais, diagnóstico em vários estágios, três ou mais testes, e covariância em função do tempo entre testes.
- **Alternativa por efeitos aleatórios individuais**, lidos como uma "intensidade" latente da doença, que induzem correlação entre testes da mesma pessoa sem parâmetros de covariância separados; também costuma exigir priors informativas.
- **Classe latente quando falta o padrão de referência:** a variável latente U é a condição verdadeira; estimação por EM ou bayesiana; na forma básica não considera a ordem nem o tempo dos testes (uma extensão troca U por um processo latente no tempo, como um processo de Markov). Existe com e sem independência condicional. Por identificabilidade, rende mais com muitos resultados de teste, inclusive muitos avaliadores. A **"regra de três"**: na sequência, a identificabilidade é garantida com pelo menos três resultados de teste por participante. Serve também para testes contínuos (modelos de mistura).
- **Verificação parcial:** o desafio comum é a não identificabilidade. Exemplo: se só quem dá positivo em um dos dois testes é verificado, duas das oito células da tabela 2×2×2 ficam sem observação (o "zero estrutural"), e o VPN da regra do OU não se estima direto. Uma saída é impor restrições ao modelo multinomial, como os estimadores de "captura-recaptura" de "dependência homogênea" e de "razão de chances homogênea", estendidos para risco relativo, gama e kappa homogêneos.

## 5. Metanálise

A metanálise de sequências recebeu pouca atenção, exceto quando a sequência pode ser tratada como um teste único e todos os participantes de todos os estudos fizeram todos os testes. Exceção: Novielli e colegas, com D-dímero e escore de Wells em combinação, num modelo que aceita desenhos diferentes (inclusive estudos com teste condicional) e tem parâmetros para a dependência condicional entre os testes e entre sensibilidade e especificidade; mostraram que a análise de custo-efetividade muda com a força da dependência. Esses métodos são pouco usados e podem ser mais fáceis com dados individuais de pacientes do que com dados agregados.

**Modelos de economia da saúde:** dependem da metanálise como entrada, e a correlação condicional (ou a covariância) costuma faltar, seja porque os testes foram avaliados em estudos separados, seja porque nem estudos primários com os dois testes na mesma população a relatam. A recomendação nesses casos é **verificar quanto o desempenho da sequência muda com os valores da covariância, dentro da faixa em que ela pode ficar**, como no exemplo a seguir.

## O exemplo: FIT repetido para câncer colorretal

O FIT (teste imunoquímico fecal) detecta produtos da degradação da hemoglobina humana nas fezes; quem dá positivo vai para colonoscopia. Dados do Oxford FIT study, coorte retrospectiva de amostras consecutivas enviadas da atenção primária ao laboratório do Oxford University Hospitals Trust, de adultos sintomáticos (18 anos ou mais), entre março de 2017 e março de 2020. Positivo é FIT acima de 10 µg Hb/g de fezes. O padrão de referência para câncer colorretal veio de dados hospitalares ligados (laboratório, endoscopia e histopatologia).

**Tabela 2** (1º FIT, 2º FIT, padrão de referência: número de pessoas): + + + : 8; + + − : 63; + − + : 1; + − − : 66; − + + : 0; − + − : 48; − − + : 1; − − − : 1122. São 10 casos de câncer e 1299 pessoas sem câncer.

**A linha de base, o primeiro FIT sozinho:** 9 de 10 casos e 129 de 1299 sem câncer deram positivo; **sensibilidade 0,900 (IC 95% 0,555 a 0,997) e especificidade 0,901 (0,883 a 0,916)**.

**Estimar a sequência só com dados de um teste** (usando só o primeiro FIT, o padrão de referência e as contagens da Tabela 2): a suposição mais simples é a independência condicional; os autores consideram mais plausível supor correlação positiva e, sem dado sobre ela, testar níveis baixo, moderado e alto. **Sob independência (ρ+ = ρ− = 0), dois FITs pela regra do OU dão sensibilidade 0,990 (0,643 a 0,995) e especificidade 0,811 (0,789 a 0,832)**, intervalos pelo método de Wilson. A Tabela 3 mostra o efeito da correlação suposta (sensibilidade; especificidade):

- ρ = 0: 0,990; 0,811
- ρ = 0,25: 0,968; 0,834
- ρ = 0,50: 0,945; 0,856
- ρ = 0,75: 0,922; 0,878

Para a regra do OU, a dependência entre os testes baixa a sensibilidade e sobe a especificidade da sequência em relação à suposição de independência.

**Estimar direto da sequência medida:** dos 9 casos com primeiro FIT positivo, 8 deram positivo de novo; o único falso negativo do primeiro FIT também deu negativo no segundo. **Sensibilidade do OU medida: 9/10 = 0,900 (IC 95% 0,596 a 0,982)**, com correlação entre os FITs repetidos nos doentes ρ+ = 0,667. Dos 1299 sem câncer, 1122 deram negativo nos dois: **especificidade do OU medida: 1122/1299 = 0,864 (0,844 a 0,881)**, com ρ− = 0,479, menor que a correlação nos doentes.

**Escolher a estratégia:** envolve trocar sensibilidade por especificidade e pesar a prevalência e as consequências de falsos positivos e falsos negativos. Aqui, o desejo de evitar falso negativo aponta para o OU, porque o E não pode aumentar a sensibilidade em relação a um teste único. Repetir o FIT pelo OU poderia subir a sensibilidade, à custa da especificidade: **na análise empírica, a repetição aumentaria os falsos positivos em 48/1299, cerca de 37 por 1000 (3,7%)**. Pela abordagem de dado único com correlação moderada (ρ+ = 0,5), a sensibilidade subiria, em hipótese, de 0,900 para 0,945, o que equivale a um falso negativo a menos a cada 2250 pacientes testados (com prevalência parecida). **A análise empírica não mostrou mudança na sensibilidade, mas com só 10 casos (n = 10) a incerteza é considerável**; como em outros cenários de baixa prevalência, estimar com precisão a sensibilidade de sequências é difícil empiricamente. Além disso, a abordagem hipotética supõe que nem a condição nem o desempenho do teste mudam com o tempo, o que pode não valer.

**Ajuste para padrão de referência imperfeito:** com verificação completa mas imperfeita, os autores usam um modelo bayesiano de variável latente (a condição verdadeira T). O modelo completo teria prevalência, sensibilidade e especificidade de cada teste e do padrão de referência e duas covariâncias condicionais por par de testes; com só oito combinações possíveis de resultados, não seria identificável. Suposições: os dois usos do FIT têm a mesma sensibilidade e a mesma especificidade (é o mesmo teste); duas covariâncias condicionais (doentes e não doentes) entre os FITs; padrão de referência independente do FIT dada a condição; padrão de referência com especificidade de 100% e sensibilidade alta, abaixo de 100%. Tabela 4 (mediana a posteriori, intervalo de credibilidade 95%): sensibilidade do FIT 0,817 (0,565; 0,959); especificidade do FIT 0,907 (0,893; 0,920); sensibilidade do OU 0,890 (0,658; 0,987); especificidade do OU 0,864 (0,844; 0,882); sensibilidade do padrão de referência 0,955 (0,895; 0,986); ρ+ 0,562 (0,071; 0,925); ρ− 0,477 (0,395; 0,560); prevalência 0,00860 (0,00431; 0,0148). O ajuste tende a reduzir a sensibilidade estimada do teste, com efeito menor na especificidade. Os autores dizem que os resultados são ilustrativos e influenciados pelas priors do padrão de referência.

## Discussão

- **Terminologia:** a área não tem vocabulário comum, o que dificultou a busca e tornou inviável uma busca totalmente sistemática. Até "sequential testing" se confunde com os testes de hipótese estatísticos repetidos dos ensaios clínicos adaptativos. Ao longo da revisão, os autores marcam os termos usados como sinônimos (no começo, "conditional testing" ou "serial testing", e o desenho condicional também chamado de "paired"; nas regras, "believe the positive" e "Any+" para o OU, "believe the negative" e "Both+" para o E) e **propõem "sequential diagnostic testing" como o descritor mais apropriado**.
- As exigências de análise atravessam áreas metodológicas: um estudo de rastreamento pode precisar avaliar acurácia, número e ordem de vários testes e, ao mesmo tempo, um padrão de referência parcial e imperfeito; os autores dizem que isso pode explicar por que tantos artigos de sequência também tratam do padrão de referência. Como muitos métodos foram feitos para uma aplicação específica, os cinco grupos não devem ser lidos isolados, e sim em conjunto.
- Muitos métodos atacam um problema de dados faltantes (teste condicional, verificação parcial, padrão de referência imperfeito). **Não há "almoço grátis":** em estudos diagnósticos, o número de parâmetros que se estimam sem suposições simplificadoras costuma ser baixo, por mais complexo que o método pareça; por isso, os autores esperam que métodos que juntam informação de vários estudos tenham valor em pesquisas futuras.
- O estudo de caso mostra a importância de considerar a dependência condicional entre testes usados em sequência, sobretudo em caminhos com pouco dado sobre os parâmetros de dependência. Os autores pedem que os analistas saibam que as saídas dos modelos precisam trazer essa informação, ou que os dados venham de forma que permita calculá-la; nos casos simples, basta apresentar tabelas de contingência multidimensionais que cruzem os resultados dos testes e do padrão de referência. Para eles, a exigência tende a ganhar importância com o avanço da metanálise.
- **Limites declarados:** a revisão não é totalmente sistemática e pode ter perdido artigos relevantes; a sobreposição de conceitos impediu oferecer uma ferramenta, como um fluxograma, que aponte o método preferido para cada desenho (a tabela suplementar serve de guia); a escolha do método depende muito do contexto; fora o estudo de caso, a revisão não detalha rotinas de cálculo nem software.
- **Trabalho futuro:** poucos dos métodos têm software fácil de usar, e os autores sugerem que oferecer software seja prioridade; métodos de síntese de vários estudos.

## Conclusão

Os cinco temas ligam os métodos conforme o objetivo, e os autores sugerem usá-los para guiar o desenvolvimento metodológico da área.

## Apêndice: notação e fórmulas

- Prevalência π; T = 1 doente, T = 0 não doente; X1 e X2 os resultados dos testes. X1 ∧ X2 (regra do E) é positivo se e só se os dois forem positivos; X1 ∨ X2 (regra do OU) é positivo se pelo menos um for. ρ+ = Corr(X1, X2 | T = 1) e ρ− = Corr(X1, X2 | T = 0).
- Sensibilidade do OU = 1 − P(X2=0 | X1=0, T=1)·(1 − Se(X1)); especificidade do OU = P(X2=0 | X1=0, T=0)·Sp(X1).
- Sensibilidade do E = P(X2=1 | X1=1, T=1)·Se(X1); especificidade do E = 1 − P(X2=1 | X1=1, T=0)·(1 − Sp(X1)).
- Limites: Se(OU) ≥ máx{Se(X1), Se(X2)}; Sp(OU) ≤ mín{Sp(X1), Sp(X2)}; Se(E) ≤ mín{Se(X1), Se(X2)}; Sp(E) ≥ máx{Sp(X1), Sp(X2)}.
- **Fórmula (1), com o coeficiente phi:** Se(OU) = Se(X1) + (1 − Se(X1))·Se(X2) − τ+, com τ+ = ρ+·[Se(X1)Se(X2)(1 − Se(X1))(1 − Se(X2))]^0,5; Sp(OU) = Sp(X1)·Sp(X2) + τ−. Na expressão de τ− impressa no apêndice (no XML e no PDF), o coeficiente que multiplica [Sp(X1)Sp(X2)(1 − Sp(X1))(1 − Sp(X2))]^0,5 aparece como ρ+.
- A verossimilhança multinomial para dois testes binários, com prevalência π, multiplica, para cada combinação de resultados (i, j), o termo π·P(X1=i, X2=j | T=1) + (1 − π)·P(X1=i, X2=j | T=0), elevado ao número de pessoas com aquela combinação.
- A reparametrização usada no grupo 4 escreve P(X1=1, X2=1 | T=1) = P(X1=1 | T=1)·P(X2=1 | T=1) + c1, com c1 = Cov(X1, X2 | T=1), e as demais probabilidades conjuntas em termos de c1 ou de c0 = Cov(X1, X2 | T=0).

## Financiamento e dados

Financiado pelo NIHR (Community Healthcare MedTech and In Vitro Diagnostics Co-operative, Oxford Health NHS Foundation Trust); Fanshawe também pelo NIHR ARC Oxford and Thames Valley; Nicholson por uma NIHR Academic Clinical Lectureship e pelo CRUK. Os financiadores não tiveram papel no desenho, na interpretação nem na decisão de publicar. Os autores declaram não ter conflitos de interesse. Todos os dados para recriar os resultados estão no corpo do artigo.

---
