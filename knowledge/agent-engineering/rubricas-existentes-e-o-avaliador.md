# Rubricas que já existem: o que ensinam para uma rubrica de conteúdo e para o avaliador

O que as rubricas de interface e de juiz com IA, onde há estudo com concordância medida, ensinam para escrever uma rubrica de qualidade de peças de rede social e para montar o avaliador. Duas premissas guiam a leitura: as peças nascem como HTML, e o código pode servir de estado para um classificador (como um modelo de decisão tipado, o Jev, da TypeSafe) avaliar até a parte visual. Fontes: *WebDevJudge: avaliando (M)LLMs como críticos da qualidade de desenvolvimento web*, de Chunyang Li, Yilun Zheng, Xinting Huang, Tianqing Fang, Jiahao Xu, Yangqiu Song, Lihui Chen, Han Hu (Tencent AI Lab, HKUST, NTU) (https://arxiv.org/abs/2510.18560), *MLLM as a UI Judge: modelos multimodais prevendo a percepção humana de interfaces*, de Reuben A. Luera (UC Berkeley), Ryan Rossi, Franck Dernoncourt, Branislav Kveton e outros (Adobe Research), Cindy Xiong Bearfield (Georgia Tech) (https://arxiv.org/abs/2510.08783), *Vision-Guided Iterative Refinement for Frontend Code Generation (crítica visual no ciclo de geração de frontend)*, de Hannah Sansford, Derek H. C. Law, Wei Liu, Abhishek Tripathi, Niresh Agarwal, Gerrit J. J. van den Burg (Amazon AGI; University of Bristol) (https://arxiv.org/abs/2604.05839), *TypeSafe: mapa de casos de uso do Jev (documentação)*, de TypeSafe AI (documentação oficial) (https://docs.typesafe.ai/concepts/use-case-map), *jev-lint: lint semântico de código com o Jev (repositório)*, de mizchi (projeto aberto no GitHub) (https://github.com/mizchi/jev-lint). O método do portão está em [[classificacao-como-portao]]; a segunda via com modelo generativo, em [[saida-estruturada-e-raciocinio]].

## O ponto de partida

**Não existe rubrica validada para carrossel ou post de Instagram.** As três frentes de pesquisa concordam: para conteúdo social só há guias de praticante. Uma rubrica própria, montada com evidência de plataforma e com o método de quem produz, é o que dá para ter de mais estruturado para esse fim. O que se aprende vem de rubricas de interface e de juiz com IA, onde há estudo com concordância medida.

## O que os estudos mostram

| Achado | Número | Fonte |
|---|---|---|
| Rubrica escrita melhora a concordância **entre humanos** | de 65% para 92% | WebDevJudge |
| Melhor modelo contra a preferência humana em páginas web | 66% (humanos entre si, 85%) | WebDevJudge |
| Tirar o **código** prejudica o juiz mais que tirar a captura de tela | qualitativo | WebDevJudge |
| Juiz de quatro dimensões contra juiz de nota única | 69,5% contra 48,5% de concordância; empates de 28,5% para 8,5% | Amazon |
| Renderizar, criticar a imagem e corrigir o código | +11% a +18% na melhor versão | Amazon |
| Modelo multimodal julgando interfaces | bom em hierarquia visual, clareza e confiança; ruim em facilidade de uso e interesse | Adobe |
| Escolher entre duas interfaces | perto do acaso quando são parecidas; até 90% quando são claramente diferentes | Adobe |

## Lições para uma rubrica de conteúdo

1. **Folhas binárias e atômicas, agregadas em árvore.** Cada critério pode virar um pequeno grupo de testes de sim ou não; a nota do critério é a soma deles. Níveis 0, 1 e 2 servem como resumo legível.
2. **Escalas curtas** (de 0 a 2, por exemplo); em nota individual, o teste binário supera a escala Likert.
3. **Várias dimensões, não uma nota geral.** O ganho medido (69,5% contra 48,5%) pede critérios separados também no avaliador.
4. **"Não dá para avaliar" como opção** em cada critério.
5. **Comparação entre duas versões** é mais confiável que nota absoluta para diferenças sutis; serve para escolher entre variações da mesma peça. Duas ressalvas: o viés de posição é máximo justamente quando as duas versões são parecidas, e a defesa é julgar nas duas ordens e só contar a vitória que resiste à troca [[2026-10-31-zheng-mt-bench-juiz-llm]] [[2026-10-31-shi-vies-de-posicao-judging-the-judges]] [[2026-10-31-wang-juizes-nao-sao-justos-posicao]].
6. **A rubrica calibra também a pessoa:** os humanos passaram de 65% para 92% de concordância só por ter rubrica. Um conjunto âncora mede as duas coisas.
7. **Instruir o juiz a aceitar soluções equivalentes** com forma diferente; juízes tendem a reprovar o que não se parece com o esperado.

## As três camadas de avaliação de uma peça

| Camada | O que avalia | Exemplo | Base |
|---|---|---|---|
| **Medida exata em código** | o que é número | contraste das cores do texto, margem mínima, quantos tamanhos de letra por tela, palavras por tela, número de cores | sem modelo; mais barato e exato |
| **Classificador tipado sobre o HTML e o texto** | julgamento fechado | há uma chamada só? o gancho diz a quem serve? (ponto focal e grade tendem a ficar com o modelo multimodal) | o código é a entrada mais informativa (WebDevJudge); **ninguém publicou um classificador tipado julgando qualidade visual: é experimento** |
| **Modelo multimodal sobre a imagem** | o que só existe depois de renderizar | ilustração gerada, texto sobre foto, "cara de IA" da arte | bom em diferenças claras, fraco em pares parecidos (Adobe); erra fonte (no máximo 29,9%, Claude 9,8%), cor (ΔE até 14,5) e tamanho (9 a 11 px), que vão para a camada de código, e fica com o grosso e com localizar onde está o defeito ([[2026-10-31-typobench-tipografia-para-agentes-de-design]], [[2026-10-31-graphic-design-bench]], [[juiz-de-visao-julgando-design]]) |

O ciclo da Amazon mostra que vale fechar o laço: renderizar, criticar a imagem, voltar ao HTML.

## O que o Jev (TypeSafe) já faz com código

- **A documentação lista lint semântico de código e verificação de saídas de IA**, não avaliação de qualidade visual; interface só aparece como "IA embutida numa UI".
- **jev-lint**, projeto aberto: localiza um trecho, faz **uma pergunta de uma frase** sobre ele e usa **um limiar ajustado por regra** com exemplos próprios. O próprio autor mede cerca de 1 achado errado em cada 5 e trata cada achado como candidato para uma pessoa. É o desenho que o avaliador de conteúdo pode copiar: pergunta curta por elemento, limiar por critério, cache das respostas.
- Uma única matéria (The New Stack, sem acesso ao texto) diz que a Workday usa o Jev para **escolher** componentes do design system ao montar interfaces; é seleção, não julgamento de qualidade.

## Calibração

O relatório de boas práticas de rubrica (repositório `delip/autorubric`, sem autor nem data, só citação) sugere um conjunto de 50 a 100 itens rotulados por humano e revisar a rubrica se o kappa ficar abaixo de 0,7. Uma régua prática, mais exigente com o pequeno número de casos: o limite de baixo do intervalo do kappa acima de 0,4 para contar como calibrado, e acima de 0,6 para o avaliador decidir sozinho.

## Não verificado

- Um classificador tipado julgando hierarquia a partir do HTML: hipótese, a testar com um conjunto âncora.
- O caso da Workday: fonte única, texto não aberto.
- Os estudos de interface medem telas de aplicativo e páginas web, não peças de rede social; a transferência é inferência.

*Texto integral fora da base (licença não comercial):* [[2026-10-31-shi-vies-de-posicao-judging-the-judges]] em https://arxiv.org/abs/2406.07791.
