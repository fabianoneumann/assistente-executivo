---
titulo: "The preregistration revolution"
tipo: paper
autor: "Brian A. Nosek, Charles R. Ebersole, Alexander C. DeHaven, David T. Mellor"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/"
publicado_em: 2018-03-13
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [preregistration, prediction, postdiction, hindsight-bias, forking-paths, deviations, blinding, holdout, selective-reporting, registered-reports]
licenca: "PNAS license, na própria página. Só a ficha: o integral fica na url"
---

# Nosek et al. 2018 (PNAS): predição, pós-dição e o pré-registro como linha entre as duas

Ficha em palavras próprias; o integral não entra e está na `url`. Center for Open Science e University of Virginia; Proceedings of the National Academy of Sciences, vol. 115, n. 11, p. 2600 a 2606; DOI 10.1073/pnas.1708274114. Área: metodologia científica, com exemplos de várias disciplinas. Artigo do Sackler Colloquium "Reproducibility of Research: Issues and Proposed Remedies" (8 a 10 de março de 2017). Revisão argumentativa, sem dados próprios. Conflito declarado: três autores trabalham no Center for Open Science, sem fins lucrativos, cuja missão é ampliar abertura, integridade e reprodutibilidade. A página aponta uma carta de Ledgerwood ("The preregistration revolution needs to distinguish between predictions and analyses", p. E10516) e a réplica ("Predictions without analysis plans are inert", p. E10518), que não foram lidas aqui.

## A tese

A ciência avança gerando hipóteses com observações existentes e testando-as com observações novas. Os autores chamam a primeira atividade de **pós-dição** e a segunda de **predição**, termos gerais que cobrem pares como exploratório e confirmatório, contexto de descoberta e de justificação, análise dependente e independente dos dados. Na predição, os dados chegam para enfrentar a chance de a ideia estar errada; na pós-dição, já são conhecidos e a explicação é feita para eles. Ambas são vitais: a predição dá evidência diagnóstica, a pós-dição descobre o que ninguém havia considerado. O dano aparece quando uma passa pela outra, porque gera confiança excessiva em explicações feitas depois, reduz a incerteza de forma falsa e, no fim, diminui a reprodutibilidade. Pré-registrar é definir perguntas e plano de análise antes de ver os resultados, e a frase que resume o papel dele: "Preregistration does not favor prediction over postdiction; its purpose is to make clear which is which."

## Por que a mente confunde as duas

- **Raciocínio circular:** gerar a hipótese com os dados e avaliá-la nos mesmos dados (hipotetizar depois do resultado, Kerr 1998).
- **Viés de retrospectiva** (Fischhoff): o resultado parece mais previsível depois de visto. Costuma acontecer com predição vaga, em que muitos resultados podem ser racionalizados como apoio. Exemplos do artigo: o biomédico que elege, entre cinco desfechos, o único que melhorou; o cientista político com covariáveis e exclusões que só fazem sentido depois; o químico que dá narrativa à variação ao acaso. Citam Tversky, por meio de Lewis (2016), sobre explicar com confiança o que não se soube prever.
- **Incentivos:** resultados novos, positivos e limpos rendem mais recompensa, e são raros. Isso cria um conflito de interesse potencial entre o que é recompensado e o que é correto.
- **Boa intenção não basta:** memória falha, raciocínio motivado e vieses podem agir fora da consciência. A pessoa pode lembrar errado o propósito original e acreditar sinceramente que previu o resultado. O viés de confirmação procura o que concorda e acha defeito no que não concorda.

## Por que a estatística depende disso

O teste de significância da hipótese nula (NHST, na sigla em inglês) foi feito para predição. O poder diagnóstico de um valor P depende de saber quantos testes foram feitos: P < 0,05 significa coisas diferentes se foi o único teste ou um entre 20, 200 ou 2.000. Quase nunca existe um só jeito de testar, já que é preciso decidir exclusões, transformações, combinações e covariáveis.

Corrigir pelo número de testes feitos é relativamente simples, embora raramente se faça. O problema maior é o **jardim de caminhos que se bifurcam** (Gelman e Loken): se as escolhas ocorrem durante a análise, ver os dados torna alguns caminhos mais prováveis, e no fim talvez nem dê para estimar quais caminhos seriam tomados com dados diferentes. O valor P fica com diagnosticidade desconhecida e não se pode interpretá-lo. Na predição, o caminho é fixado antes, e o P, com a correção pelo número de testes, mantém o sentido. O artigo foca no NHST por ser muito usado e nota que nenhum método estatístico, bayesianos incluídos, elimina por si a flexibilidade em exclusões e criação de variáveis. Notas laterais: valores P perto de 0,05 nem são tão improváveis na prática, e há quem proponha 0,005 como critério (Benjamin e outros, 2017).

## O que o pré-registro faz e o que se sabe do efeito

Comprometer-se com os passos de análise sem conhecer o resultado, em geral postando o plano num registro independente, como clinicaltrials.gov ou osf.io, que preserva o documento e o torna localizável, às vezes após um embargo. Tudo o que não está no plano informa a pós-dição.

**A evidência é declarada como parcial:** o argumento teórico é forte e a evidência correlacional ajuda, mas falta evidência experimental suficiente de superioridade para a reprodutibilidade. Por isso os autores escrevem "em princípio". Números e estudos citados:

| Fonte citada | O que achou | Condição |
|---|---|---|
| Swaen e outros (ref. 11) | Hipotetizar antes se relaciona a maior replicabilidade | Correlacional |
| Kaplan e Irvin | Queda "dramática" na taxa de resultados positivos | Depois da exigência de registrar desfechos primários, em amostra de ensaios clínicos; o artigo não dá o número |
| Franco e outros | 40% dos artigos publicados não relataram uma ou mais manipulações; 70% não relataram uma ou mais variáveis de desfecho | Amostra de estudos pré-registrados |
| Franco e outros | 96% dos achados consistentemente significativos entraram nos artigos publicados; 65% dos efeitos nulos ficaram de fora | Mesma amostra, viés de seleção no que se relata |

Os benefícios se perdem se o plano não for seguido, mas o registro permite detectar e às vezes corrigir vieses de seleção e relato (exemplo citado: compare-trials.org).

## O caso ideal e os nove desafios

No ideal: observar, formular a pergunta, criar desenho e plano, coletar, analisar conforme o plano; depois explorar à vontade; e transformar as pós-dições mais interessantes em predições do estudo seguinte. Com isso, registrar custa muito pouco. Como a pesquisa real é mais complicada, o artigo trata de nove desafios, cada um com um personagem:

1. **Mudança de procedimento durante o estudo (Jolene: 60 bebês em vez de 100, e bebês que dormem).** O desvio é frequente, e testar predições continua possível. O momento decide: com o resultado ainda desconhecido, o registro da mudança basta para manter o valor diagnóstico; com ele já conhecido, o registro ainda rende bem: a maior parte do plano segue de pé, e dá bem mais confiança do que não ter registrado nada. Ressalva: "There is certainly increased risk of bias with deviations from analysis plans after observing the data, even when changes are reported transparently". Usar o resultado observado para decidir se continua coletando pode elevar a chance de resultado enganoso.
2. **Premissa violada descoberta na análise (Courtney: efeito teto e não normalidade).** Quatro saídas, cada uma com seu custo:
   - **Registro por etapas:** registrar primeiro a avaliação das distribuições e exclusões, depois o modelo. Difícil em muitas áreas, e se a etapa anterior revela algo do resultado, o registro fica comprometido.
   - **Cegar os dados:** embaralhar observações mantendo as distribuições, para tratar valores extremos e premissas sem ver o resultado. Mais robusta, mas pode ser difícil de aplicar.
   - **Árvore de decisão registrada:** a sequência de testes e a regra de cada etapa (normalidade decide paramétrico ou não). Serve quando as análises possíveis são fáceis de descrever. Também pode embutir viés, como testar regras de exclusão até dar P < 0,05: isso invalida a inferência, embora fique bem visível.
   - **Procedimentos operacionais padrão (SOPs):** regras gerais para tratar dados, compartilháveis entre estudos, boas para áreas com muitas decisões comuns; podem virar norma da comunidade (padrões de autofagia, análise do Teste de Associação Implícita). Têm o mesmo risco de viés, detectável e evitável, e pedem esforço para formar consenso.
3. **Dados já existentes (Ian).** Tudo depende de as decisões serem cegas aos dados. O registro "puro" segue possível se ninguém viu os dados (fósseis não descobertos, dados oficiais não divulgados). As perguntas a fazer: quem viu e o que foi comunicado a quem. Até conhecer outro resultado do mesmo conjunto pode influenciar: a cientista política que analisa religiosidade e voluntariado, tendo visto ideologia e doações, perde parte da cegueira por causa das correlações entre as variáveis. Perdida a cegueira, o melhor é registrar o plano e dizer o que se sabia e o que não se sabia. Esse relato permite ao menos avaliar a credibilidade de forma subjetiva.
4. **Estudos longitudinais e grandes bases (Lily, 20 anos de observações).** Valem as soluções anteriores, e cada onda nova traz variáveis ainda não observadas, que dão alguma cegueira. Isso enfraquece se a variável futura se correlaciona com a já vista, e depende da proporção dos dados relevantes já observada. Cegueira parcial protege mais do que nenhuma.
5. **Muitos experimentos (Natalie).** Com um paradigma comum, um modelo define parâmetros e cada registro diz o que muda. Quando coletar é fácil demais para documentar, tudo começa como exploratório, e o que interessar vira predição numa replicação em que o desenho e o script originais são o registro.
6. **Programa de pesquisa (Brandon, um positivo a cada 20 tentativas).** Registrar tudo não basta: o positivo isolado pode ser acaso. É essencial relatar todos os resultados do plano. Dizer "1 em 20" ajuda a identificar o provável falso positivo, e a replicação traz confiança. Registros e resultados precisam ficar preservados e acessíveis para revisão.
7. **Poucas expectativas (Matt, ciência de descoberta).** Se os dados geram hipóteses sem alegar evidência, o artigo pode assumir a explicação depois do fato. Valor P só deve aparecer ao testar predição, porque em exploração tem diagnosticidade desconhecida. Saídas: primeiro estudo registrado com plano simples e depois explorado, para alimentar o registro do segundo; ou validação cruzada num único estudo grande, dividindo os dados, explorando uma parte e lacrando a outra até registrar o que a exploração gerou. Com poucos dados para dividir, não há saída mágica: "The rules of statistical inference have no empathy for how hard it is to acquire the data." O progresso fica mais lento.
8. **Predições concorrentes (Rusty e Melanie).** Não chega a ser desafio: concordando no desenho e no plano, duas predições opostas favorecem inferência forte entre teorias (Platt, 1964).
9. **Narrativa e conclusões (Alexandra).** Dá para seguir todo o ideal e ainda explorar o acaso na interpretação: dez análises, com foco narrativo em duas, equivalem a não corrigir comparações múltiplas. Dá para corrigir com alfa, como Bonferroni, mas a atenção seletiva é difícil de tratar por estatística. Tirar a narrativa dos artigos seria má solução. Só a transparência permite detectar e tratar essa influência.

## Como tornar a prática norma

Os autores organizam a mudança em meios, motivo e oportunidade.

- **Meios:** a barreira é o treino insuficiente em estatística e método. Há cursos, guias, critérios de selo e modelos. Muito do pré-registro já existe em pedidos de financiamento, revisões de ética e propostas de tese, a poucos passos de um plano completo.
- **Motivo:** o registro é exigido por lei nos EUA para ensaios clínicos e necessário em revistas que seguem a política do ICMJE, embora o padrão peça desfechos primários e secundários sem exigir o plano completo de análise. Milhares de revistas e vários financiadores assinam as diretrizes TOP. Selos para dados abertos se associaram a aumento de mais de dez vezes no compartilhamento num teste inicial. O Preregistration Challenge oferece mil prêmios de US$ 1.000.
- **Registered Reports:** revisão por pares da pergunta e do método antes do resultado; aceito em princípio; no segundo estágio, avalia-se a execução e a aderência, sem julgar a importância do resultado. Dezenas de revistas oferecem o formato.
- **Oportunidade:** registros por área (clinicaltrials.gov, o maior; AEA RCT Registry; RIDIE; EGAP) e o geral OSF, com mais de 8.000 pré-registros na data do artigo. O aspredicted.org oferece um formulário simples, mas o texto observa que ele não é um registro em si, porque o usuário pode manter o formulário privado para sempre.

## Limites declarados

- Não há evidência experimental suficiente de que o pré-registro melhore a reprodutibilidade.
- O pré-registro não elimina comparações múltiplas nem relato seletivo entre estudos; torna possível corrigir, se houver relato completo.
- Não impede más práticas estatísticas, apenas as torna detectáveis.
- Não impede a licença narrativa de autores e leitores.
- A distância até o uso generalizado é grande, e pede ação coordenada num sistema descentralizado.

## Tudo o mais que ensina

- O aforismo de Box, de que nenhum modelo está certo e alguns ainda assim servem: modelos são aproximações, melhoradas pela redução do erro de predição.
- O avanço científico costuma vir de descoberta inesperada: um padrão inexplicável muda o rumo da investigação.
- Mesmo sem nenhuma relação real, muitos testes dão positivos por acaso, e relatar mais os positivos eleva a chance de falso positivo.
- Numa base muito examinada, ainda dá para testar predição se a pessoa nova estiver totalmente cega ao que outros viram e relataram, mas há muitas formas diretas e indiretas de influência, como ler um resumo ou receber conselho de quem já analisou.
- Quando o uso for pervasivo, segundo os autores, descobrir e testar serão ambos valorizados e claramente rotulados, e a exploração será entendida como identificar o possível, com estudos seguintes testando o provável.
- Interpretações diferentes da mesma evidência são um traço da ciência como atividade descentralizada de observadores independentes.
- Fontes de ajuda citadas: cursos no Coursera (statistics; statistical-inferences), critérios de selo em osf.io/6q7nm, modelos em osf.io/zab38/wiki/home.
