---
titulo: "Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement"
tipo: paper
autor: "Jaehun Jung, Faeze Brahman, Yejin Choi"
url: "https://arxiv.org/abs/2407.18370"
publicado_em: 2024-07-25
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, selective-evaluation, cascade, confidence-calibration, abstention, human-agreement]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 25/07/2024, a única versão (lida). Publicado no **ICLR 2025**, com apresentação oral (a página do arXiv não diz o venue; confirmado nos anais, [proceedings.iclr.cc](https://proceedings.iclr.cc/paper_files/paper/2025/hash/08dabd5345b37fffcbe335bd578b15a0-Abstract-Conference.html), e em [iclr.cc/virtual/2025/oral/31838](https://iclr.cc/virtual/2025/oral/31838)). Lido em 2026-10-29, na pesquisa da calibração por dimensão do portão.

## A ideia

Em vez de confiar sempre no veredito do juiz, o juiz só decide quando está confiante o bastante; quando não está, **se abstém** e o item sobe para um juiz mais forte ou para gente. Os autores chamam isso de **avaliação seletiva**. Com um limiar de confiança escolhido num conjunto de calibração pequeno, rotulado por humanos, eles dão uma garantia formal: entre os itens que o juiz decide, a concordância com os humanos fica acima de um nível escolhido pelo usuário (por exemplo, 90%), com alta probabilidade.

## As peças

- **O limiar:** testa limiares do mais alto ao mais baixo no conjunto de calibração e para no último em que o limite superior do erro (pela binomial exata) ainda fica abaixo do risco aceito. Teste em sequência fixa, menos conservador que a correção de Bonferroni. Conjunto de calibração de 500 itens nos experimentos principais (392 no Auto-J).
- **A confiança:** a probabilidade que o modelo dá ao próprio veredito e a confiança que ele declara em texto **superestimam** a concordância com humanos, até no GPT-4. Os autores propõem os **Anotadores Simulados**: o mesmo juiz é chamado N vezes, cada vez com K exemplos de um anotador humano diferente no prompt, e a confiança é o quanto essas simulações concordam entre si. Com N = K = 5, o erro de calibração cai cerca de 50% e a AUROC sobe 13% no GPT-4; os modelos fracos ganham ainda mais. Com exemplos da maioria humana em vez de anotadores individuais (quando só há um rótulo por item), funciona um pouco pior, mas ainda melhor que as linhas de base.
- **A cascata:** começa no juiz barato (Mistral-7B), sobe para o GPT-3.5 e só depois para o GPT-4, cada um com seu limiar calibrado. A garantia vale para a cascata inteira.

## Resultados

- **TL;DR (resumos), alvo de 90%:** a cascata cumpre a garantia em 90,8% das 1000 divisões aleatórias, com 55,7% de cobertura; o GPT-4 sem seleção não cumpre nunca; calibrar o limiar só pela estimativa pontual, sem o teste, cumpre em 47,5% a 79,0%.
- **ChatArena, alvo de 85%:** garantia cumprida em 91,0%, cobertura de 63,2%, com o GPT-4 decidindo só 17,5% dos itens.
- **Destaque do resumo:** num subconjunto do Chatbot Arena em que o GPT-4 quase nunca chega a 80% de concordância, a cascata garante mais de 80% com quase 80% de cobertura (79,1%, dos quais 88,1% decididos pelo Mistral-7B ou pelo GPT-3.5).
- **Sem o GPT-4:** uma cascata só com modelos fracos (Mistral-7B, Mixtral-8x7B, GPT-3.5) garante 80% de concordância com 68,3% de cobertura a 12,6% do custo do GPT-4. O modelo fraco não perde precisão; perde cobertura.
- **A abstenção segue a dificuldade humana:** os itens em que o juiz se absteve têm concordância entre anotadores de 0,815, contra 0,902 nos que ele decidiu (p < 1e-8); tamanho da resposta e sobreposição de palavras não explicam a diferença.
- **Mudança de distribuição:** calibrando com respostas de um grupo de modelos e testando em outro, a garantia se mantém em mais de 90% das execuções, com pequena perda de cobertura.

## Limites declarados e ressalvas

- A garantia supõe que o conjunto de calibração vem da mesma distribuição dos itens avaliados; o teste com mudança de distribuição é empírico.
- É avaliação em pares (qual das duas respostas é melhor), não nota por critério.
- O preço da garantia é cobertura: o que o juiz não decide precisa ir para alguém.

---
