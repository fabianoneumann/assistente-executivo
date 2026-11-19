---
titulo: "Do ImageNet Classifiers Generalize to ImageNet?"
tipo: paper
autor: "Benjamin Recht, Rebecca Roelofs, Ludwig Schmidt, Vaishaal Shankar"
url: "https://arxiv.org/abs/1902.10811"
publicado_em: 2019-06-12
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [test-set-reuse, adaptive-overfitting, distribution-shift, reproducibility, imagenet, cifar-10, annotation, selection-frequency, benchmarks]
licenca: "licença não exclusiva do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/), indicada na página do resumo; entra só a ficha, e o integral está na url"
---

# Recht et al. 2019 (arXiv): novos testes para CIFAR-10 e ImageNet

Ficha em palavras próprias (o integral não entra; está na `url`). Recht, Roelofs, Schmidt e Shankar, UC Berkeley. Lida a versão 2 do arXiv (12/6/2019; primeira submissão em 13/2/2019), 76 páginas com apêndices, em visão computacional. Conjuntos e código públicos em `github.com/modestyachts/CIFAR-10.1` e `github.com/modestyachts/ImageNetV2`.

## A pergunta

Dois benchmarks de classificação de imagens vêm sendo reusados há quase uma década, o que levanta o risco de sobreajuste aos testes. Os autores repetem o processo de criação dos conjuntos de teste, da mesma fonte e com o mesmo protocolo de limpeza, e medem até onde os modelos atuais generalizam. O ideal seria a mesma acurácia, a menos do erro de amostragem.

## O enquadramento: três parcelas da queda

Com LS o erro no teste original, LS' no novo, e D e D' as distribuições original e nova:

LS − LS' = (LS − LD) + (LD − LD') + (LD' − LS')

- **Lacuna de generalização (LD' − LS'):** só erro de amostragem, porque o novo teste independe do modelo.
- **Lacuna de adaptatividade (LS − LD):** quanto adaptar o modelo ao teste, por exemplo ajustando hiperparâmetros nele, faz o erro de teste subestimar o erro real.
- **Lacuna de distribuição (LD − LD'):** diferença sistemática entre amostrar o teste original e o novo. É difícil argumentar que duas distribuições de alta dimensão sejam a mesma, e coletar dados envolve muitas escolhas de projeto.

Para um único modelo, adaptatividade e distribuição não se separam. Por isso medem muitos modelos: modelos mais novos, resultado de mais ajustes no mesmo teste, deveriam ter mais adaptatividade; no caso extremo, a acurácia real estagnaria enquanto a do teste seguisse subindo.

## Por que esses dois conjuntos

Processo de criação bem documentado, muita competição e dois perfis. CIFAR-10 é pequeno, então mais gente experimentou nele e pode ter havido mais ajuste. ImageNet tem cerca de 24 vezes mais imagens de treino e cerca de 100 vezes mais pixels por imagem, o que sugeriria mais robustez. Nenhuma das duas suposições passou no teste dos autores: o conjunto menor não mostrou sobreajuste adaptativo maior, nem o maior, robustez bem superior.

O ideal seria ter um teste independente escondido por anos, tirado da mesma coleta; eles não conhecem isso para os dois conjuntos. Por isso imitam a curadoria original, o que introduz a dificuldade de separar adaptatividade e distribuição.

## Método: CIFAR-10

CIFAR-10 é subconjunto rotulado de Tiny Images (80 milhões de imagens 32×32, cerca de 75 mil palavras-chave do WordNet, cada uma com cerca de 1.000 a 2.500 imagens, base ruidosa): 10 classes, 6.000 imagens por classe, 50.000 de treino e 10.000 de teste.

1. **Subclasses.** Acharam a palavra-chave de cada imagem do CIFAR-10 (toda imagem tinha duplicata exata em Tiny Images) e ficaram com as 25 mais comuns por classe; as 250 cobrem mais de 95% do conjunto. A distribuição importa: em avião, a palavra mais comum é `stealth_bomber` (0,94% no novo e 0,92% no original, tabela 6).
2. **Coleta em dois papéis.** O autor A faz o papel dos estudantes anotadores: vê as imagens existentes de cada palavra e escolhe novas, seguindo as instruções originais. O autor B faz o papel dos pesquisadores: revê as cerca de 9.000 candidatas e tira as confusas ou fora da regra, com critérios em parte subjetivos. Só uma palavra (`alley_cat`, menos de 0,3% do conjunto) precisou de exame de todas as imagens disponíveis.
3. **Tamanho.** 2.000 imagens, porque para acurácia de 90% o intervalo de Clopper-Pearson de 95% vale [88,6%, 91,3%], cerca de ±1%, e diferença só interessaria se bem maior que 1%; e porque um alvo menor reduz o risco de incluir imagens mais duvidosas.
4. **Montagem.** Amostra que reproduz a distribuição por palavra, remoção de quase duplicatas contra o próprio conjunto e contra treino e teste originais, revisão manual dos 10 vizinhos mais próximos, e nova amostragem até convergir.
5. **Separação.** Nenhum classificador rodou nos dados durante a coleta.

## Método: ImageNet

Base do desafio ILSVRC2012: 1,2 milhão de imagens de treino, 50.000 de validação, 100.000 de teste, 1.000 categorias. Os rótulos do teste nunca foram publicados, para reduzir sobreajuste; não há limite equivalente na validação, e a maioria dos artigos relata acurácia nela. Os autores usam "validação" e "teste" como sinônimos no caso do ImageNet. Replicam a validação porque vem de uma só fonte (quase toda do Flickr), tem rótulos, é a mais citada e é a usada para ajustar modelos.

**Candidatos.** Flickr, com sinônimos do WordNet como busca, imagens enviadas de 11/7/2012 a 11/7/2013, logo após o período original (a liberação final do ILSVRC2012 foi em 10/7/2012). Evitaram a mesma janela porque ela podia estar esgotada de imagens boas. Até 100 imagens por classe, estimando 10% de aproveitamento. Ordenação por data de envio, porque "relevância" e "interessantidade" podem usar modelos treinados no próprio ImageNet. Quando faltava imagem, em ordem: acrescentar palavra da classe mãe; até 200 imagens; ampliar até 11/7/2014; juntar termos compostos; escolher termos alternativos e traduções. Total: 208.145 candidatos.

**Anotação no MTurk (Amazon Mechanical Turk, plataforma de trabalho pago por tarefa).** Interface e instruções próximas das originais: grade de 48 imagens, definição da classe e link para a Wikipedia, aceitar oclusão e texto na cena, excluir desenhos e pinturas. Pelo menos 6 imagens da validação original em cada tarefa, em posições aleatórias, para controle (3 da classe e 3 de classe vizinha). Pelo menos 10 trabalhadores por imagem. O produto é a **frequência de seleção**: a fração de trabalhadores que marcaram a imagem para a classe.

**Quase duplicatas.** Trinta vizinhos mais próximos em três métricas (distância em pixels, em atributos de uma VGG, e SSIM), com revisão manual. O ImageNet original, até onde sabem, usou só a primeira.

**Amostragem.** Os limiares de concordância originais não estão publicados, e a população de trabalhadores de 2010 a 2012 não se repete em 2018. Por isso fizeram três estratégias, todas com 10 imagens por classe:

- **MatchedFrequency:** reproduz, por classe, o histograma de frequência de seleção das imagens originais anotadas, em 5 faixas (de 0 a 0,2 até de 0,8 a 1). É o conjunto principal, com frequência média próxima da original. Faltou imagem numa faixa em 0,8% dos casos, e aí pegaram da faixa de cima, o que facilita o teste.
- **Threshold0.7:** só imagens com frequência de pelo menos 0,7.
- **TopImages:** as 10 de maior frequência.

A classe importa: "African elephant" fica de 0,8 a 1,0; "nail" (o prego) é muito confundida com unha.

**Revisão final.** Os autores viram cada imagem antes de rodar modelos, ao lado de 10 originais da classe, e removeram erros, desenhos, imagens borradas ou muito editadas e desvios visíveis (exemplo: tubarões-brancos que eram maquetes e estátuas). A revisão se repetiu até convergir em 33 iterações, a maioria com poucas mudanças. Aceitaram o risco de desvio, dizendo que um teste só interessa com rótulos corretos.

## Modelos

34 no CIFAR-10 (de `random_features_32k` a `autoaug_pyramid_net_tf`) e 67 no ImageNet (de Fisher vectors a `pnasnet_large_tf`), pré-treinados quando possível. A implementação própria de Fisher vector dá top-5 17% abaixo do publicado e é só uma referência inspirada no método. Top-1 original: de 83% a 98% no CIFAR-10 e de 21% a 83% no ImageNet.

## Resultados no novo teste

Acurácia em %, com intervalo de 95% de Clopper-Pearson (tabela 1; ImageNet é top-1, em MatchedFrequency):

| Conjunto | Modelo | Original | Novo | Queda |
|---|---|---|---|---|
| CIFAR-10 | autoaug_pyramid_net_tf | 98,4 [98,1, 98,6] | 95,5 [94,5, 96,4] | 2,9 |
| CIFAR-10 | shake_shake_64d_cutout | 97,1 [96,8, 97,4] | 93,0 [91,8, 94,1] | 4,1 |
| CIFAR-10 | wide_resnet_28_10 | 95,9 [95,5, 96,3] | 89,7 [88,3, 91,0] | 6,2 |
| CIFAR-10 | resnet_basic_110 | 93,5 [93,0, 93,9] | 85,2 [83,5, 86,7] | 8,3 |
| CIFAR-10 | vgg_15_BN_64 | 93,0 [92,5, 93,5] | 84,9 [83,2, 86,4] | 8,1 |
| CIFAR-10 | cudaconvnet | 88,5 [87,9, 89,2] | 77,5 [75,7, 79,3] | 11,0 |
| CIFAR-10 | random_features_256k_aug | 85,6 [84,9, 86,3] | 73,1 [71,1, 75,1] | 12,5 |
| ImageNet | pnasnet_large_tf | 82,9 [82,5, 83,2] | 72,2 [71,3, 73,1] | 10,7 |
| ImageNet | nasnetalarge | 82,5 [82,2, 82,8] | 72,2 [71,3, 73,1] | 10,3 |
| ImageNet | resnet152 | 78,3 [77,9, 78,7] | 67,0 [66,1, 67,9] | 11,3 |
| ImageNet | inception_v3_tf | 78,0 [77,6, 78,3] | 66,1 [65,1, 67,0] | 11,9 |
| ImageNet | densenet161 | 77,1 [76,8, 77,5] | 65,3 [64,4, 66,2] | 11,8 |
| ImageNet | vgg19_bn | 74,2 [73,8, 74,6] | 61,9 [60,9, 62,8] | 12,3 |
| ImageNet | alexnet | 56,5 [56,1, 57,0] | 44,0 [43,0, 45,0] | 12,5 |
| ImageNet | fv_64k | 35,1 [34,7, 35,5] | 24,1 [23,2, 24,9] | 11,0 |

- **Faixa declarada:** quedas de 3% a 15% no CIFAR-10 e de 11% a 14% no ImageNet. Nas tabelas completas, CIFAR-10 vai de 2,9 a 15,4 (tabela 11, com `random_features_32k` na ponta); ImageNet top-1, de 10,3 a 13,6 nas redes convolucionais e de 6,2 a 11,0 nos Fisher vectors (tabela 14); ImageNet top-5, de 5,6 a 11,9 nas redes convolucionais e de 10,3 a 13,2 nos Fisher vectors (tabela 15).
- **Melhor modelo no ImageNet:** de 83% para 72% em top-1 e de 96% para 90% em top-5. O melhor modelo do ILSVRC 2013 tinha 89% de top-5 e o de 2014, 93%. A queda de 6% em top-5 corresponde, segundo eles, a cerca de cinco anos de progresso.
- **Ordem:** "the relative order of models is almost exactly preserved". O maior deslocamento é de 4 posições no CIFAR-10 (tabela 11) e de 5 no ImageNet top-1 (`bninception`, tabela 14); em top-5 chega a 8 (`resnet152`, tabela 15).
- **Relação linear com inclinação maior que 1:** CIFAR-10, acc_novo = 1,69·acc_orig − 72,7%; intervalo de 95% por 100.000 amostras bootstrap: inclinação [1,63, 1,76], deslocamento [−78,6, −67,5]. ImageNet top-1, acc_novo = 1,11·acc_orig − 20,2%; inclinação [1,07, 1,19], deslocamento [−26,0, −17,8]. Cada ponto ganho no teste original vale mais de um ponto no novo, e modelos melhores caem menos.

## O efeito da limpeza no ImageNet

Mesmo Flickr, imagens corretas, frequência média acima de 0,7, e a acurácia varia 14% (tabela 2; variação média contra a validação original, cuja frequência média é 0,71):

| Estratégia | Frequência média | Top-1 | Top-5 |
|---|---|---|---|
| MatchedFrequency | 0,73 | −11,8% | −8,2% |
| Threshold0.7 | 0,85 | −3,2% | −1,2% |
| TopImages | 0,93 | +2,1% | +1,8% |

Essa variação de cerca de 14% (top-1) e 10% (top-5) entre estratégias é maior que a faixa entre todas as redes depois da AlexNet, excluídas as SqueezeNet, que é de cerca de 14% e 8%.

Por faixa de frequência, segundo as legendas: em MatchedFrequency, imagens de 0,4 a 0,6 dão acurácia média cerca de 20% abaixo do conjunto inteiro e 30% abaixo da validação original (figura 15). Na própria validação original, essa faixa fica cerca de 10 a 15% abaixo do conjunto inteiro (figura 16). Comparando faixa a faixa, o novo teste é sempre pior: cerca de 20% nas faixas do meio e 5 a 10% nas pontas (figura 17).

## Como os autores interpretam a queda

**Adaptatividade.** A forma prototípica seria retorno decrescente no novo teste, e o que se vê é o contrário: "multiple years of competitive test set adaptivity did not lead to diminishing accuracy numbers". Há ressalva expressa: "they do not exclude all variants". Uma queda aproximadamente constante para todos os modelos seria compatível com os dados, e testar isso pede um teste de fato independente da mesma coleta. Exceção que deixam aberta: top-5 em TopImages tem inclinação de 0,88 (intervalo [0,81, 0,91]), e não sabem se é sinal de sobreajuste adaptativo ou efeito de chegar perto de 100%.

Dois mecanismos poderiam ter evitado o sobreajuste, e os experimentos dão pouca evidência para escolher entre eles. Um é o Ladder de Blum e Hardt: interação restrita com o teste permite muitas avaliações, e a comunidade o seguiria implicitamente. O outro é a classe limitada de modelos: importa o número de modelos que de fato chegam ao teste; treinados com variações de SGD num treino fixo e exigindo alta acurácia de treino, podem ser poucos o bastante para a convergência uniforme valer.

**Distribuição.** É a hipótese principal. Mudar a amostragem altera muito a acurácia, mesmo com a mesma fonte e o mesmo resto do processo. A dificuldade principal é provavelmente o caráter subjetivo da anotação humana: população de anotadores, qualificação, lugar e época, formato da tarefa, pagamento, e classes sem definição exata. Os modelos têm dificuldade de generalizar de imagens "fáceis" para "difíceis". Conjectura: a queda vem de pequenas variações na anotação humana.

**Modelo de dificuldade para a relação linear.** Apresentado expressamente como ilustração, sem pretender ser a explicação verdadeira. Numa escala probit (inversa da CDF gaussiana, Φ⁻¹), o ajuste é melhor: Φ⁻¹(α_novo) = u·Φ⁻¹(α_orig) + v, de 21% a 83% de acurácia, cerca de 60 pontos, incluindo os Fisher vectors. Se a imagem tem dificuldade τ com distribuição N(μ, σ²) e o modelo acerta com probabilidade Φ(s − τ), onde s é a habilidade, a acurácia é Φ((s − μ)/√(σ² + 1)), e entre dois testes a relação é linear na escala probit, com u = √(σ₁² + 1)/√(σ₂² + 1) e v = (μ₁ − μ₂)/√(σ₂² + 1).

## Hipóteses alternativas testadas

**CIFAR-10:**

- **Erro estatístico.** Intervalo de 95% de cerca de ±1,2% no novo teste e, no original, de ±0,6% a 90% de acurácia e ±0,3% a 97%. Descartado como explicação principal. Para 10.000 pontos (novo teste do ImageNet), o intervalo é de no máximo ±1% a 95% e ±2% a 99,99%.
- **Quase duplicatas no teste original.** Cerca de 800 imagens (8%), em que os modelos acertam de 99% a 100%. Para um modelo de 93%, a acurácia fora delas seria de cerca de 92,4%, ou seja, 0,6% menos, contra quedas de 8 a 9%. Explica no máximo 1%.
- **Reajuste de hiperparâmetros.** Busca em grade de taxa de aprendizado, dropout e weight decay numa VGG: a maior melhora foi de 85,3% para 85,8%.
- **Inspeção das imagens difíceis.** As que nenhum modelo acerta são válidas e reconhecíveis por humanos (figura 4).
- **Acurácia humana.** Nove estudantes de pós-graduação de Berkeley, ordem aleatória, nos cerca de 5% de imagens mais difíceis para os modelos (500 originais e 115 novas). Quatro foram melhor no original e cinco no novo; diferença média de −0,8%. Os autores chamam de estudo preliminar. Sugere que o novo teste não é bem mais difícil para humanos.
- **Treinar com parte do novo teste.** Cerca de 1.000 imagens somadas ao treino da `vgg16_keras`: 85,1% e 85,4% na metade restante, contra 84,9%.
- **Validação cruzada no CIFAR-10 original (tabela 4).** Cinco divisões, com o teste original somado ao treino e uma das dobras de treino como teste:

| Conjunto | vgg_15_BN_64 | wide_resnet_28_10 | shake_shake_64d_cutout |
|---|---|---|---|
| Teste original | 93,6 | 95,7 | 97,1 |
| Divisões 1 a 5 | 93,5 a 94,0 | 96,0 a 96,5 | 97,2 a 97,4 |
| Novo teste | 84,9 | 89,7 | 93,0 |

- **Discriminador entre os dois testes.** Com 3.200 imagens de treino e 800 de teste, `resnet_32` e `resnet_110`, 160 épocas: 50,1% e 50,3% sem pré-treino, 52,9% e 53,1% com pré-treino, com intervalos que tocam 50%.
- **Classes exatamente balanceadas.** O novo teste tinha 8% de `ship`, contra 10%. Na versão balanceada (tabela 12), modelos fracos ganham cerca de 0,3%, e a queda do melhor não muda.

**ImageNet:**

- **Validação cruzada (tabela 13).** ResNet-50, cinco dobras de 50.000 imagens de treino, com a validação somada ao treino: top-5 de 92,55% a 92,62%, contra 92,5% na validação original e 84,7% em MatchedFrequency. Diferenças dentro dos intervalos de 95%.
- **Efeito da revisão manual.** Do início ao fim, a acurácia subiu cerca de 4%, o que indica que a revisão não causou a queda; a relação linear já aparece na primeira revisão (figura 8). O texto diz `resnet50`; a legenda da figura 7 diz `resnet152`.

## Trabalhos comparados

Sem experimento diretamente comparável, segundo eles. Torralba e Efros (2011) medem generalização entre conjuntos diferentes, com variações maiores e sem dados inéditos. Kornblith et al. (2018) retreinam em outros conjuntos e também acham relação aproximadamente linear. Exemplos adversariais exigem perturbação fina; aqui, variações benignas bastam. Um modelo robusto a ℓ∞ (Madry et al.) cai quase sobre a mesma reta do CIFAR-10. Perturbações explícitas (ruído, rotação, neve) usam intervenção visível, enquanto aqui não se sabe que propriedade das imagens causa a queda.

## Sugestões para os próximos conjuntos

- Publicar também o código de criação.
- Testar os anotadores de forma padronizada e relatar, e construir variantes do teste com anotação diferente.
- Manter um "super hold-out" escondido por anos, para testar sobreajuste adaptativo.
- Escolher tarefas mais simples para humanos (menos classes, fronteiras claras) e variedade maior de pose, luz, oclusão e corrupção.
- Usar especialistas só no teste: viola a hipótese de treino e teste serem da mesma distribuição, mas pode melhorar correção e diversidade.
- Usar mais de um teste por benchmark, porque um só não basta para caracterizar a confiabilidade.

Os autores dizem que isso não é crítica a falhas do CIFAR-10 ou do ImageNet, feitos no fim dos anos 2000 para outro patamar de acurácia.

## Limites declarados e o que fica em aberto

- Separar adaptatividade e distribuição não é possível para um só modelo, e o desenho não tem teste verdadeiramente da mesma coleta.
- A amostragem final do CIFAR-10 foi feita pelos próprios autores, com critérios em parte subjetivos, e parte da revisão do ImageNet também.
- Não se sabe o que torna as imagens mais difíceis; candidatas: tamanho do objeto, filtros (preto e branco, sépia), poses incomuns.
- Falta medir acurácia humana no ImageNet e estudar outros domínios, como processamento de linguagem natural e plataformas de competição.
- Conjuntos de milhares de imagens: 2.000 e 10.000 nos novos testes, com intervalos de cerca de ±1%.

## Tudo o mais que ensina

- **ImageNet tem frequência de seleção como dado de qualidade:** a faixa de 0 a 0,2 reúne as piores imagens e a de 0,8 a 1 as melhores; todas continuam corretas depois da revisão.
- **Alegações de desempenho humano** ganham contexto com essa fragilidade dos classificadores à limpeza dos dados.
- **Treino e validação do ImageNet não vêm da mesma fonte** (vários buscadores contra quase só Flickr), então não são estritamente independentes e identicamente distribuídos. Na validação cruzada, os autores atribuem a pequena alta de acurácia a esse desvio.
- **Classes ambíguas:** projétil e míssil, elefante com presas (`tusker`) e elefante indiano, tela e monitor, por definição do WordNet.
- **Regra de amostra pequena frente ao conjunto:** os novos testes têm cerca de 3% do CIFAR-10 e menos de 1% do ImageNet, para reduzir o viés de sobrarem só imagens difíceis na fonte.
- **Treinamento repetido varia:** a mesma `vgg16_keras` deu 84,9% e 85,3%; os autores atribuem à inicialização aleatória, dentro do intervalo [83,6, 86,8].
