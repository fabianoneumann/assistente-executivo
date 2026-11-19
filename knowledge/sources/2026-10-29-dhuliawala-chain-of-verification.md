---
titulo: "Chain-of-Verification Reduces Hallucination in Large Language Models"
tipo: paper
autor: "Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu, Roberta Raileanu, Xian Li, Asli Celikyilmaz, Jason Weston"
url: "https://aclanthology.org/2024.findings-acl.212/"
publicado_em: 2024-08-11
capturado_em: 2026-10-29
licenca: "CC BY 4.0 na versão publicada (rodapé da ACL Anthology: material publicado em 2016 ou depois sob Creative Commons Attribution 4.0); o integral lido vem dessa versão. A cópia no arXiv (2309.11495) tem só a licença não exclusiva do arXiv"
areas: [agent-engineering]
tags: [chain-of-verification, hallucination, verification, self-correction, factored-verification, verification-questions]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0, versão da ACL Anthology) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Versões: arXiv v1 em 20/09/2023 e v2 em 25/09/2023 (https://arxiv.org/abs/2309.11495); publicado em Findings of the Association for Computational Linguistics: ACL 2024, páginas 3563 a 3578 (11 a 16/08/2024), versão lida em PDF da ACL Anthology, conferida contra o HTML da v2 do arXiv. A versão da ACL acrescenta ao arXiv a comparação com SelfCheckGPT e ChatProtect, a contagem de chamadas por método (seção 7) e os limiares do SelfCheckGPT (seção 8). Autores da Meta AI; Dhuliawala também da ETH Zürich. Lido em 2026-10-29 (skill de revisão), pela etapa que confere cada achado.

## A pergunta

Modelos de linguagem inventam fatos plausíveis (alucinação), sobretudo os fatos raros, que aparecem pouco no treino, e mais ainda em texto longo, onde um erro puxa o seguinte. O modelo consegue deliberar sobre a própria resposta e corrigir os erros, só com ele mesmo, sem busca nem ferramenta? A aposta é que o modelo acerta mais quando pergunta um fato isolado do que quando o escreve no meio de um texto longo.

## O método: quatro etapas (seção 3)

Todas as etapas usam o mesmo modelo, com prompts diferentes, com poucos exemplos no prompt (few-shot).

1. **Resposta inicial.** O modelo responde à pergunta do jeito normal. Ela é também a linha de base que o método tenta melhorar.
2. **Planejar as verificações.** Com a pergunta e a resposta inicial à vista, o modelo escreve uma lista de perguntas de verificação, uma para cada afirmação factual. Exemplo do artigo: se a resposta diz que a guerra entre México e Estados Unidos foi de 1846 a 1848, uma pergunta possível é quando ela começou e terminou. As perguntas são livres, não seguem molde, e não precisam repetir a redação original.
3. **Executar as verificações.** O modelo responde a cada pergunta e compara com a resposta inicial em busca de inconsistência. Sem busca na web: o modelo confere o próprio trabalho.
4. **Resposta final verificada.** Um último prompt recebe a resposta inicial e os pares de pergunta e resposta e reescreve, corrigindo o que a verificação contradisse. No prompt de biografias, as respostas de verificação entram como vindas "de outra fonte", e o modelo deve sintetizar só o que é consistente entre as duas.

## As variantes da etapa 3

- **Conjunta.** Planejar e responder num só prompt: os exemplos mostram as perguntas seguidas das respostas. Problema: como as perguntas são escritas com a resposta inicial no contexto, as respostas também a enxergam, e o modelo tende a repetir o que já disse, inclusive a alucinação. A verificação herda o erro que devia pegar.
- **Em duas etapas.** Um prompt planeja as perguntas (vendo a resposta inicial); outro responde a elas vendo **só as perguntas**, sem a resposta inicial, e por isso não pode copiá-la.
- **Fatorada.** Cada pergunta é respondida num prompt separado, sem a resposta inicial e sem as outras perguntas. Tira a interferência da resposta inicial e também a de uma resposta sobre a outra, e cabe mais perguntas, porque nenhuma disputa o mesmo contexto. Custa mais chamadas, mas elas rodam em paralelo. Exige separar a lista de perguntas, fácil porque os exemplos pedem lista separada por vírgula. O nome vem do trabalho de Radhakrishnan et al. (2023) sobre decomposição fatorada.
- **Fatorada com revisão (factor+revise).** Depois de responder, um prompt a mais por pergunta faz o **cruzamento explícito**: olhando o fato original e a resposta da verificação, classifica como consistente, inconsistente ou parcialmente consistente. Exemplo do artigo: a resposta diz que a guerra veio depois da anexação do Texas em 1845; a pergunta "quando o Texas se separou do México?" volta com 1836, e o cruzamento deve marcar a inconsistência. A resposta final é montada só com os fatos consistentes.

## Como mediram (seção 4)

- **Modelo base:** Llama 65B (sem ajuste por instrução), decodificação gulosa, few-shot com 3 exemplos por tarefa. Comparações: Llama 2 70B Chat sem exemplos e com "vamos pensar passo a passo"; nas biografias, resultados publicados de InstructGPT, ChatGPT e PerplexityAI (que busca na web); na versão da ACL, também SelfCheckGPT (variantes NLI e LLM) e ChatProtect, aplicados sobre GPT-3.
- **Wikidata (mais fácil):** 56 perguntas geradas do tipo "quem são alguns [profissão] nascidos em [cidade]?", cada uma com cerca de 600 respostas certas na base; mede precisão (micro) e a média de entidades certas (positivas) e alucinadas (negativas) por resposta.
- **Lista de categorias da Wikipédia (mais difícil):** 55 perguntas do conjunto QUEST, do tipo "cite alguns filmes mexicanos de terror animados", cerca de 8 respostas cada; mesmas métricas.
- **MultiSpanQA de livro fechado:** 418 perguntas factuais com várias respostas curtas (até 3 tokens cada), sem o documento; mede F1, precisão e recall.
- **Biografias longas:** "fale sobre a vida de <pessoa>", medido com o FactScore (Min et al., 2023), que confere cada fato com um modelo apoiado em busca e correlaciona bem com julgamento humano.

## Resultados com os números

**Tabela 1, listas (precisão; positivas e negativas por resposta):**

| Modelo e método | Wikidata: precisão | positivas | negativas | Categorias: precisão | positivas | negativas |
|---|---|---|---|---|---|---|
| Llama 2 70B Chat, sem exemplos | 0,12 | 0,55 | 3,93 | 0,05 | 0,35 | 6,85 |
| Llama 2 70B Chat, passo a passo | 0,08 | 0,75 | 8,92 | 0,03 | 0,30 | 11,1 |
| Llama 65B, few-shot (linha de base) | 0,17 | 0,59 | 2,95 | 0,12 | 0,55 | 4,05 |
| CoVe conjunta | 0,29 | 0,41 | 0,98 | 0,15 | 0,30 | 1,69 |
| CoVe em duas etapas | 0,36 | 0,38 | 0,68 | 0,21 | 0,50 | 0,52 |
| CoVe fatorada | 0,32 | 0,38 | 0,79 | 0,22 | 0,52 | 1,52 |

- A precisão no Wikidata mais que dobra (0,17 para 0,36). O ganho vem de cortar alucinação (negativas de 2,95 para 0,68), com perda pequena de acertos (positivas de 0,59 para 0,38).

**Tabela 2, MultiSpanQA (F1, precisão, recall):** Llama 2 Chat sem exemplos 0,20 / 0,13 / 0,40; com passo a passo 0,17 / 0,11 / 0,37; linha de base few-shot 0,39 / 0,40 / 0,38; CoVe conjunta 0,46 / 0,50 / 0,42; CoVe fatorada 0,48 / 0,50 / 0,46. F1 sobe 23%, com ganho em precisão e recall.

**Tabela 3, biografias (FactScore; média de fatos por biografia):**

| Modelo e método | FactScore | fatos |
|---|---|---|
| InstructGPT (publicado) | 41,1 | 26,3 |
| ChatGPT (publicado) | 58,7 | 34,7 |
| PerplexityAI, com busca (publicado) | 61,6 | 40,8 |
| Llama 2 70B Chat, sem exemplos | 41,3 | 64,9 |
| Llama 2 70B Chat, passo a passo | 41,1 | 49,0 |
| Llama 65B few-shot (linha de base) | 55,9 | 16,6 |
| CoVe conjunta | 60,8 | 12,8 |
| CoVe fatorada | 63,7 | 11,7 |
| CoVe fatorada com revisão | 71,4 | 12,3 |
| GPT-3 few-shot | 45,3 | 15,6 |
| GPT-3 + ChatGPT, ChatProtect | 48,5 | 14,6 |
| GPT-3 + InstructGPT, SelfCheckGPT LLM | 60,6 | 6,0 |
| GPT-3 + DeBERTa, SelfCheckGPT NLI | 61,7 | 6,3 |
| GPT-3 + InstructGPT, CoVe fatorada com revisão | 68,6 | 9,0 |

- FactScore sobe 28% (55,9 para 71,4) com pouca perda de fatos (16,6 para 12,3). O ganho vale para fatos raros e frequentes (figura 2), mas o PerplexityAI, que busca, ainda ganha nos fatos muito raros; o CoVe ganha nos frequentes.
- Recortar a saída do Llama 2 Chat para 10 frases quase não muda o FactScore (41,3 para 42,7): a métrica é normalizada e as respostas com menos fatos são comparáveis.
- Na versão da ACL, o CoVe ganha das três mitigações publicadas. Para o SelfCheckGPT, os autores escolheram o limiar que dá FactScore alto sem cortar muitos fatos; no limiar mais alto, a variante NLI chega a 76,5 com só 3 fatos por biografia (tabela 6).

**Os outros achados da seção 4.3:**

- **Ajuste por instrução e passo a passo não reduzem alucinação.** O Llama base com exemplos ganha do Llama 2 Chat em todas as tarefas, e pedir para pensar passo a passo não ajuda (no Wikidata, até piora: negativas de 3,93 para 8,92).
- **Fatorada e em duas etapas ganham da conjunta em todas as tarefas** (FactScore 60,8 para 63,7; nas listas, duas etapas é a melhor no Wikidata e fatorada na de categorias). Para os autores, isso sustenta a hipótese de que a pergunta de verificação não deve enxergar a resposta inicial, porque o modelo tende a repeti-la.
- **O cruzamento explícito ajuda mais** (fatorada 63,7 para fatorada com revisão 71,4).
- **Pergunta curta é respondida melhor do que o texto longo.** No Wikidata, só cerca de 17% das entidades da resposta inicial estão certas; perguntando cada entidade em separado, cerca de 70% das respostas de verificação acertam. O modelo muitas vezes sabe que errou quando a pergunta vem isolada.
- **Perguntas geradas pelo modelo ganham das de molde, e as abertas ganham das de sim ou não** (tabela 4, lista de categorias, precisão conjunta / fatorada): perguntas de molde "X responde à pergunta?" 0,13 / 0,16; perguntas de sim ou não geradas pelo modelo 0,15 / 0,19; perguntas abertas geradas 0,15 / 0,22. Nos exemplos com ChatGPT (seção 10 da ACL), o modelo tende a concordar com o fato do jeito que a pergunta de sim ou não o enuncia, certo ou errado.
- **Custo (seção 7 da ACL):** no pior caso, a fatorada com revisão faz 1 + s + 2×f chamadas (s frases, f fatos): uma para a resposta, uma por frase para planejar, uma por fato para verificar e uma por fato para cruzar. ChatProtect faz 1 + s×k×3 (k = 3 repetições) e SelfCheckGPT LLM n + 1 + s×n (n = 4 amostras). Os autores julgam o custo comparável ao das outras mitigações.

## A recomendação

Quebrar a verificação em perguntas simples e respondê-las **sem deixar o modelo ver a resposta que está sendo verificada**; perguntas abertas, escritas pelo modelo conforme a tarefa, em vez de sim ou não ou de molde; e, no texto longo, um passo explícito que marca cada fato como consistente ou não antes de reescrever. Extensão óbvia apontada: usar busca na etapa de execução.

## Limites declarados

- Reduz, não elimina a alucinação; a resposta final ainda pode trazer erro.
- Só trata erro factual dito diretamente; não cobre erro em passo de raciocínio nem em opinião.
- Custa mais tokens, como a cadeia de raciocínio; em troca, as verificações mostradas ao usuário tornam a decisão mais interpretável.
- O teto do ganho é o que o próprio modelo sabe e sabe que sabe; ferramentas externas são o caminho complementar, não explorado aqui.
