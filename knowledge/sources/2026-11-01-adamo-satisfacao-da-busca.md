---
titulo: "From \"satisfaction of search\" to \"subsequent search misses\": a review of multiple-target search errors across radiology and cognitive science"
tipo: paper
autor: "Stephen H. Adamo, Brian J. Gereke, Sarah Shomstein, Joseph Schmidt"
url: "https://doi.org/10.1186/s41235-021-00318-w"
publicado_em: 2021-08-28
capturado_em: 2026-11-01
licenca: "CC BY 4.0 (indicada no XML do PMC, PMC8403090: 'licensed under a Creative Commons Attribution 4.0 International License')"
areas: [agent-engineering]
tags: [satisfaction-of-search, subsequent-search-misses, multiple-target-search, radiology, visual-search, checklists, computer-aided-detection, attentional-template, human-error]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Revisão narrativa em *Cognitive Research: Principles and Implications* 6:59 (Springer, acesso aberto), agosto de 2021. Universidade da Flórida Central (Adamo e Schmidt), Universidade do Texas em Austin (Gereke) e George Washington University (Shomstein). Texto lido: o XML de texto completo da Europe PMC (PMC8403090), inteiro, inclusive as tabelas 1 e 2. Lida para a rodada investigativa (o juiz das peças), tema detecção.

**Força da evidência:** revisão narrativa, não sistemática, de dois campos (radiologia desde os anos 1960, ciência cognitiva desde cerca de 2010); o primeiro autor é um dos que renomearam o efeito, e a seção final propõe uma teoria dos próprios autores ainda não testada. Serve como mapa do que se sabe e do que não se sabe, com as fontes primárias citadas.

## A pergunta e o nome

Quando há mais de um alvo numa imagem, achar o primeiro baixa a chance de achar o segundo. A radiologia chamou isso de **"satisfação da busca"** (Tuddenham, 1962; Smith, 1967); a ciência cognitiva, de **"erro de busca subsequente"** (*subsequent search miss*, SSM; Adamo et al., 2013). O efeito responde por até um terço de certos erros de leitura em radiologia (Anbari e West, 1997) e aparece em abdome, esqueleto, tórax e politrauma; com leigos, aparece em telas simples (procurar letras T entre letras L), o que indica um limite geral de como as pessoas buscam, não algo próprio de radiologistas.

## As três teorias (todas com algum apoio, nenhuma explica tudo)

- **Satisfação:** achado o primeiro, o leitor se dá por satisfeito com o significado da imagem e encerra a busca cedo. É a origem do nome, mas só foi testada 30 anos depois, e em boa parte **não se sustentou como explicação principal**: radiologistas passaram o mesmo tempo em imagens com uma e com duas anormalidades (Berbaum et al., 1991), e na ciência cognitiva os observadores continuam fixando outros itens depois do primeiro achado (Cain et al., 2013). O apoio vem de diferenças individuais: quem busca menos tempo depois do primeiro achado erra mais o segundo (Adamo et al., 2018), e quem não espera um segundo alvo busca menos (Stothart e Brockmole, 2019).
- **Conjunto perceptivo:** achado um alvo, o leitor fica preparado para achar outros parecidos e perde os diferentes. Fraturas: menos efeito quando as duas eram leves do que quando uma era grave e a outra leve (Berbaum et al., 2001). Bagagem simulada com cerca de 100 tipos de alvo: mais erro quando os dois alvos eram diferentes, menos quando eram idênticos, mas o erro não some nem com alvos idênticos (Biggs et al., 2015; Mitroff et al., 2015).
- **Esgotamento de recursos:** o primeiro alvo consome atenção e memória de trabalho e sobra menos para o segundo. Tirar o primeiro alvo da tela depois de achado reduz o erro (Cain e Mitroff, 2013); repetir a tela mais tarde sem o primeiro alvo também (Cain et al., 2014). Uma "piscada atencional" de cerca de 200 a 500 ms depois de fixar o primeiro alvo explica parte dos erros; desordem visual em volta do segundo alvo e movimento na tela aumentam o efeito.

## Onde o erro acontece (rastreio do olhar)

A radiologia separa três tipos de omissão (Nodine e Kundel, 1987): **amostragem** (o alvo nunca é fixado), **reconhecimento perceptivo** (fixado, mas não por tempo bastante) e **decisão** (fixado o bastante, mas rejeitado). Em radiologia, a maior parte dos erros de busca subsequente é de alvo **olhado e não reconhecido**: cerca de 90% dos alvos perdidos foram fixados, com 20% a mais de erros de reconhecimento nas imagens com vários alvos (Samuel et al., 1995). Em telas simples, cerca de metade é de amostragem.

## O que se tentou para reduzir (e quase nada funcionou)

- **Busca sistemática e listas de verificação:** Tuddenham propôs varrer o filme em ordem; radiologistas usando uma lista (Berbaum et al., 2006) ou uma lista falada (Berbaum et al., 2016) não reduziram o erro de busca subsequente. No texto da revisão a frase sai como "they did affect SSM error rates", mas o contexto ("may affect the efficacy of checklists") indica que o sentido é "não afetaram"; as listas ajudam em buscas por um alvo de categoria definida (Nartker et al., 2020).
- **Ferramentas de destaque:** imagens com contraste **aumentaram** o erro (Franken et al., 1994), talvez porque a atenção vai às áreas de alto contraste e deixa as outras sem exame; a detecção assistida por computador não mudou o erro (Berbaum et al., 2007; com uma ressalva de Schartz et al., 2013).
- **O que reduziu no laboratório:** tirar da vista o primeiro alvo assim que é achado, na hora ou repetindo a tela depois.
- **Verbalizar a busca** reduziu o erro num estudo (Berbaum et al., 2000), talvez por tornar a leitura mais deliberada.

## Como se mede (e como a medida infla o efeito)

- Na radiologia, o padrão é comparar a mesma imagem com e sem um alvo acrescentado (um nódulo simulado), por curva ROC, sem olhar a ordem em que os alvos foram achados. Berbaum et al. (2015) separaram o **Tipo I** (cai o acerto sem mudar o falso alarme) do **Tipo II** (cai o acerto e o falso alarme: o leitor fica mais relutante em relatar qualquer coisa); estudos antigos em filme mostraram mais Tipo I, os de radiografia computadorizada, mais Tipo II.
- Na ciência cognitiva, comparar o acerto do "segundo alvo" com o do alvo sozinho **infla o efeito**, porque o segundo achado tende a ser o mais difícil (Adamo et al., 2019). A correção por telas pareadas reduz o efeito; a fórmula de Becker et al. (2020), que estima o esperado só das telas com dois alvos supondo detecções independentes, reduz mais, e o efeito continua significativo (Tabela 2: d de Cohen de 0,93 a 1,63 conforme o método).

## O que os autores propõem e pedem

- **Teoria do molde atencional:** o primeiro alvo achado vira o molde que guia a busca seguinte; prevê menos erro para alvos parecidos, mais erro quanto mais recurso se gasta mantendo o primeiro, e um molde que perde prioridade com o tempo. Ainda não testada.
- **Efeito de mera presença:** um segundo alvo pode atrapalhar mesmo sem ter sido achado primeiro; as medidas atuais não separam isso.
- **Prevalência e frequência:** prevalência baixa de alvos aumenta o erro de busca subsequente (Chen e Rich, 2019); não se sabe se a raridade de um **tipo** de alvo faz o mesmo. Achados incidentais de categoria rara são mais perdidos que os de categoria comum (Wolfe et al., 2017).

## Tudo o mais que ensina

- O efeito aparece fora da radiologia: triagem de bagagem simulada, diagnóstico médico em geral, citologia e simuladores de direção.
- Distinguir erro de percepção de erro de decisão por um único limiar de tempo de fixação é frágil, porque cada anormalidade pede um tempo diferente para ser reconhecida.
- Radiologistas sabem onde a anormalidade costuma aparecer; nas telas de laboratório o alvo cai em qualquer lugar, o que pode explicar a diferença na proporção de erros de amostragem entre os campos.
- A passagem da mamografia 2D para a tomossíntese (fatias em profundidade) acha mais cânceres e reconvoca menos, mas não se sabe se reduz o erro de busca subsequente.
- Fecho dos autores: o erro não vem só de o leitor "se satisfazer" e parar, como se pensava desde 1962, mas do modo como a mente mantém e atende ao que já achou.
