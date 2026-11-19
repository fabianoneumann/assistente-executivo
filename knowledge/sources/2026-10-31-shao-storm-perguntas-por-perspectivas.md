---
titulo: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
tipo: paper
autor: "Yijia Shao, Yucheng Jiang, Theodore A. Kanell, Peter Xu, Omar Khattab, Monica S. Lam"
url: "https://aclanthology.org/2024.naacl-long.347/"
publicado_em: 2024-06-16
capturado_em: 2026-10-31
licenca: "CC BY 4.0 na versão publicada (rodapé da ACL Anthology: material publicado em 2016 ou depois sob Creative Commons Attribution 4.0); o integral lido vem dessa versão. A cópia no arXiv (2402.14207) tem só a licença não exclusiva do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0)"
areas: [agent-engineering]
tags: [perspective-discovery, multi-perspective-question-asking, simulated-conversation, retrieval-augmented-generation, long-form-generation, outline-generation, coverage-metrics, human-evaluation, llm-as-judge, source-bias, verifiability]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0, versão da ACL Anthology) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Publicado em Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2024, Volume 1: Long Papers), páginas 6252 a 6278, Cidade do México, 16 a 21/06/2024; DOI 10.18653/v1/2024.naacl-long.347. No arXiv, 2402.14207: v1 em 22/02/2024 e v2 em 08/04/2024, com o comentário "27 pages, NAACL 2024 Main Conference"; o texto da v2 do arXiv e o da Anthology foram comparados palavra a palavra e só diferem no carimbo do arXiv e na numeração das páginas dos anais. Lida a versão da Anthology, extraída do PDF oficial com `pdftotext`; as tabelas 2, 3, 6 e 11, a Figura 3 e a Figura 6, que saem embaralhadas no texto, foram conferidas nas páginas renderizadas. Todos os autores são da Stanford University (Omar Khattab é o autor do DSPy, usado na implementação). Código e recursos em https://github.com/stanford-oval/storm. Apoio da Verdant Foundation e créditos do Microsoft Azure AI; a You.com cedeu a API de busca. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01, pelo desenho de descobrir perspectivas antes de perguntar.

**Atenção:** STORM é um sistema de escrita, não um avaliador. A avaliação dele usa um juiz LLM (Prometheus 13B) e editores humanos da Wikipédia, e os dois discordam em pontos que a ficha registra.

## O resumo

Os autores estudam como usar LLMs para escrever do zero artigos longos, fundamentados em fontes e organizados, com a amplitude e a profundidade de uma página da Wikipédia. O problema pouco explorado está na pré-escrita: pesquisar o tema e preparar um esboço antes de escrever. STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking) modela a pré-escrita em três movimentos: descobre perspectivas diversas ao pesquisar o tema; simula conversas em que escritores com perspectivas diferentes fazem perguntas a um especialista fundamentado em fontes confiáveis da internet; e cura a informação coletada num esboço. Para avaliar, montam o FreshWiki (artigos recentes e de alta qualidade da Wikipédia) e medidas de qualidade do esboço, e ouvem editores experientes da Wikipédia. Frente a uma linha de base de RAG guiado por esboço, mais artigos do STORM são julgados organizados (+25 pontos absolutos) e amplos em cobertura (+10). Os editores também apontam desafios novos: a transferência de viés das fontes e a associação excessiva de fatos não relacionados.

## 1. O problema e as duas hipóteses

- **Decomposição da tarefa:** dado um tema t, achar um conjunto de referências R e gerar um artigo S em que cada frase cita documentos de R. A tarefa se divide em duas: a pré-escrita, que pesquisa e produz um esboço O (lista de títulos de seção em vários níveis) e R; e a escrita, que usa t, R e O para produzir S. A divisão imita o processo humano de pré-escrita, rascunho e revisão (Rohman, 1965); professores de escrita acadêmica às vezes supervisionam no estágio do esboço, porque um esboço extenso indica compreensão ampla do tema.
- **Por que não basta o conhecimento do modelo nem a busca simples:** gerar direto do conhecimento paramétrico falta detalhe e alucina, sobretudo em temas de cauda longa; o RAG volta ao problema de pesquisar o tema, porque muita informação não aparece numa busca simples pelo tema.
- **Por que não basta pedir perguntas:** um modelo instruído a "fazer 30 perguntas sobre o tema" produz perguntas básicas de "o quê", "quando" e "onde", que só tocam fatos de superfície (Figura 1, exemplo da cerimônia de abertura dos Jogos de Inverno de 2022). Com a perspectiva de um organizador de eventos, as perguntas viram transporte e orçamento da cerimônia.
- **As duas hipóteses do desenho:** (1) perspectivas diversas levam a perguntas variadas; (2) formular perguntas profundas exige pesquisa iterativa. A primeira se apoia na teoria dos stakeholders (Freeman et al., 2010: partes interessadas diferentes priorizam facetas diferentes de uma empresa); a segunda, na teoria das perguntas de Ram (1991: respostas a perguntas existentes geram perguntas novas).

## 2. O FreshWiki e as medidas do esboço

- **Dados:** para evitar vazamento do pré-treino, os 100 artigos mais editados de cada mês de fevereiro de 2022 a setembro de 2023 (pela API de métricas da Wikimedia), filtrados para qualidade B ou acima pelo classificador ORES (só cerca de 3% das páginas da Wikipédia atingem esse padrão), sem artigos de lista nem artigos sem subseções, só o texto (sem tabelas nem imagens). O critério é por edição, não por data de criação, porque a maioria dos artigos nasce como esboço curto. O processo pode ser repetido quando sair um modelo novo.
- **Amostra dos experimentos:** 100 artigos sorteados com até 3.000 palavras. Tabela 7: em média 8,4 seções, 15,8 títulos de todos os níveis, 327,8 palavras por seção, 2.159,1 palavras por artigo e 90,1 referências; as figuras 4 e 5 mostram que o número de referências cresce ao longo de muitas edições.
- **Medidas do esboço, contra os títulos do artigo humano como gabarito:** (a) recall suave dos títulos (heading soft recall), pela definição de Fränti e Mariescu-Istodor (2023): a "contagem suave" de cada item é o inverso da soma das similaridades de cosseno dele com os itens do conjunto (embeddings paraphrase-MiniLM-L6-v2 do Sentence-BERT), a cardinalidade é a soma das contagens, e o recall é card(G ∩ P)/card(G), com a interseção definida pela união; (b) recall de entidades dos títulos (heading entity recall), a fração de entidades nomeadas dos títulos humanos, extraídas pelo NER do FLAIR, que aparecem no esboço. Exigir casamento exato dos títulos foi considerado desnecessário.

## 3. O método (Figura 2, Algoritmo 1)

1. **Levantar temas parecidos:** o LLM sugere páginas da Wikipédia sobre temas próximos; o sistema baixa os sumários (tabelas de conteúdo) dessas páginas pela API da Wikipédia, quando existem.
2. **Identificar perspectivas:** os sumários concatenados viram contexto para o LLM escolher N perspectivas. O prompt pede "um grupo de editores da Wikipédia" que trabalhem juntos, cada um representando uma perspectiva, papel ou afiliação diferente, com a descrição do foco de cada um. Para garantir o básico, entra sempre uma perspectiva p0 fixa: o "escritor de fatos básicos", focado em cobrir amplamente os fatos básicos do tema.
3. **Ler e perguntar:** para cada perspectiva, em paralelo, uma conversa de até M rodadas entre um escritor da Wikipédia (o LLM com aquela perspectiva) e um especialista no tema. A cada rodada o escritor faz uma única pergunta, a partir do tema, da perspectiva e do histórico da conversa; o prompt pede uma pergunta por vez, sem repetir as anteriores, e uma frase de encerramento quando não houver mais o que perguntar.
4. **Dividir em consultas:** o LLM quebra a pergunta em consultas de busca.
5. **Buscar e filtrar:** os resultados passam por um filtro por regras baseado na diretriz de fontes confiáveis da Wikipédia (Reliable sources), que exclui fontes não confiáveis.
6. **Sintetizar:** o LLM, como especialista, responde só com o que as fontes coletadas sustentam ("cada frase apoiada na informação reunida"), e as fontes entram em R.
7. **Rascunho do esboço:** o LLM gera um esboço só a partir do tema, para aproveitar o conhecimento interno (em geral genérico, mas organizado).
8. **Refinar:** o LLM recebe o tema, o rascunho e as N+1 conversas e melhora o esboço.

**Escrita do artigo:** seção por seção, porque R inteiro não cabe na janela; para cada seção, recupera de R os documentos mais parecidos (embeddings Sentence-BERT) com o título da seção e os das subseções, e gera o texto com citações. As seções, geradas em paralelo, são concatenadas; o LLM apaga repetições e escreve a seção de abertura (lead) que resume o artigo, como manda o estilo da Wikipédia.

**Implementação:** prompts zero-shot no DSPy (Apêndice B traz o pseudocódigo e os prompts). N = 5 perspectivas e M = 5 rodadas. gpt-3.5-turbo para fazer as perguntas e gpt-3.5-turbo-instruct para o resto; uma variante usa gpt-4 para o rascunho e o refinamento do esboço. O especialista simulado busca pela API da You.com, com o artigo-gabarito da Wikipédia excluído dos resultados. O artigo final só é relatado com gpt-4, porque o gpt-3.5 não é fiel às fontes ao gerar texto com citações (Gao et al., 2023). Temperatura 1,0 e top_p 0,9 em tudo; saída limitada a 4.000 tokens (cerca de 3.000 palavras).

## 4. Linhas de base e medidas do artigo

- **Linhas de base:** Direct Gen (o LLM gera o esboço e depois o artigo); RAG (busca pelo tema e gera esboço ou artigo inteiro com os resultados); oRAG, RAG guiado por esboço (igual ao RAG no esboço, mas busca de novo pelos títulos das seções e escreve seção por seção). Para testar o limite do RAG, uma variante RAG-expand usa os títulos do esboço do RAG como novas consultas, junta as fontes novas e pede um esboço polido.
- **Medidas automáticas do artigo:** ROUGE-1 e ROUGE-L e recall de entidades contra o artigo humano; notas de 1 a 5 do Prometheus (LLM avaliador de 13B) em quatro aspectos tirados dos critérios de "Good article" da Wikipédia (interesse, coerência e organização, relevância e foco, cobertura), com uma rubrica desenvolvida junto com dois editores experientes (Tabela 8). O Prometheus funciona melhor com uma resposta de referência nota 5, mas a referência estourava a janela; os autores a omitem, citando que sem referência ele ainda correlaciona bem com preferência humana, e cortam o artigo para 2.000 palavras tirando conteúdo da seção mais curta, iterativamente. Verificabilidade pela revocação e precisão de citação de Gao et al. (2023), com o Mistral 7B-Instruct julgando se as passagens citadas implicam a frase.

## 5. Resultados automáticos

**Tabela 3, qualidade do esboço (recall suave dos títulos / recall de entidades, %):**
- GPT-3.5: Direct Gen 80,23 / 32,39; RAG/oRAG 73,59 / 33,85; RAG-expand 74,40 / 33,85; STORM 86,26† / 40,52†; sem perspectiva 84,49 / 40,12; sem conversa 77,97 / 31,98.
- GPT-4: Direct Gen 87,66 / 34,78; RAG/oRAG 89,55 / 42,38; RAG-expand 91,36 / 43,53; STORM 92,73† / 45,91; sem perspectiva 92,39 / 42,70; sem conversa 88,75 / 39,30.
- † = diferença significativa (p < 0,05, teste t pareado) entre STORM e as linhas de base. O esboço gerado direto já tem recall suave alto, o que os autores leem como capacidade dos LLMs de captar os aspectos gerais de um tema; o STORM cobre mais aspectos específicos. Com o modelo mais fraco (GPT-3.5), jogar informação desorganizada na janela piora o esboço do RAG frente ao Direct Gen.

**Tabela 2, qualidade do artigo (ROUGE-1, ROUGE-L, recall de entidades; notas do Prometheus para interesse, organização, relevância, cobertura):**
- Direct Gen: 25,62; 12,63; 5,08; 2,87; 4,60; 3,10; 4,16.
- RAG: 28,52; 13,18; 7,57; 3,14; 4,22; 3,05; 4,08.
- oRAG: 44,26; 16,51; 12,57; 3,90; 4,79; 4,09; 4,70.
- STORM: 45,82; 16,70; 14,10†; 3,99†; 4,82; 4,45†; 4,88†.
- STORM sem a etapa de esboço: 26,77; 12,77; 7,39; 3,33; 4,87; 3,35; 4,37.
- † = significativo contra o oRAG (melhor linha de base). Na organização, o STORM (4,82) não se distingue do oRAG (4,79), e a variante sem esboço tem a maior nota de organização (4,87) embora caia em todo o resto. Os autores reconhecem "the possibility of the evaluator LLM overrating machine-generated text" e remetem à avaliação humana.

**Tabela 4, citações (juiz Mistral 7B-Instruct):** revocação de citação 84,83% e precisão 85,18%; cerca de 15% das frases não são sustentadas pelas citações.

**Ablações:** "sem perspectiva" tira a perspectiva do prompt de perguntas; "sem conversa" pede um número fixo de perguntas de uma vez. O total de perguntas é igualado entre variantes. O pipeline completo tem o maior recall, e o "sem conversa" cai muito, o que os autores leem como sinal de que ler a informação relevante é crucial para gerar perguntas eficazes. **Tabela 5, número médio de referências únicas em R:** STORM 99,83; sem perspectiva 54,36; sem conversa 39,56. Tirar a etapa de esboço piora o artigo em todas as medidas, exceto a organização pelo Prometheus.

## 6. Avaliação com editores da Wikipédia

- **Quem:** 10 editores experientes, recrutados por uma página de pesquisa no Meta-Wiki e por contato com editores ativos que tinham aprovado artigos recentemente; todos com pelo menos 500 edições e mais de um ano de experiência (3 com 1 a 5 anos, 4 com 6 a 10, 3 com mais de 15). Aprovação de comitê de ética e consentimento pelo Qualtrics; US$ 50 por participante.
- **Desenho:** 20 temas sorteados; para cada tema, o artigo do STORM e o do oRAG (a melhor linha de base automática), cada par avaliado por 2 editores. Escala de 1 a 7 (mais fina que a do juiz automático) nos mesmos cinco aspectos, com a verificabilidade pelo padrão da Wikipédia, "verificável e sem pesquisa original" (Tabela 10). Um aplicativo web mostrava o artigo e os trechos das citações lado a lado. Os editores também deram comentário livre e preferência pareada e, ao fim, compararam um artigo do STORM com o artigo humano correspondente e responderam a três afirmações de utilidade numa escala Likert de 1 a 5.
- **Tabela 6 (oRAG: média e % de notas ≥ 4; STORM: média e % ≥ 4; valor p do teste t pareado):** interesse 3,63 e 57,5% contra 4,03 e 70,0%, p = 0,077; organização 3,25 e 45,0% contra 4,00 e 70,0%, p = 0,005; relevância 3,93 e 62,5% contra 4,15 e 65,0%, p = 0,347; cobertura 3,58 e 57,5% contra 4,00 e 67,5%, p = 0,084; verificabilidade 3,85 e 67,5% contra 3,80 e 67,5%, p = 0,843. Preferência pareada: 26 para o STORM e 14 para o oRAG (40 julgamentos).
- **O que o resumo arredonda:** os "+25%" de organização e "+10%" de cobertura são diferenças absolutas na fração de notas ≥ 4 (70,0 contra 45,0; 67,5 contra 57,5). Só a organização tem p < 0,05; a cobertura tem p = 0,084. A organização é justamente a dimensão em que o juiz automático não via diferença.
- **Concordância entre os editores (nota 11, alfa de Krippendorff na escala 1 a 7):** interesse 0,349; organização 0,221; relevância 0,256; cobertura 0,346; verificabilidade 0,388. Todos baixos.
- **Utilidade percebida (Figura 3, n = 10):** "pode ajudar especificamente na minha pré-escrita": 70% concordam em parte e 30% totalmente (unânime); "vai me ajudar a editar um artigo sobre tema novo": 20% neutros, 50% concordam em parte, 30% totalmente; "pode ser útil para a comunidade da Wikipédia": 10% discordam em parte, 20% neutros, 60% concordam em parte, 10% totalmente.
- Dois editores elogiaram a profundidade frente ao artigo humano ("a bit more background information"; "the AI articles had more depth").

## 7. As falhas apontadas

- **Mais informação traz problemas além da alucinação factual:** nas 14 preferências pelo oRAG, excluídos 3 casos em que a preferência contradizia as notas do próprio editor, o STORM levou nota menor de verificabilidade em mais da metade. A análise dos artigos e dos comentários atribui isso à falácia do arenque vermelho (red herring) e à sobre-especulação: o artigo cria conexões não verificáveis entre informações de R, ou entre a informação e o tema. Para os autores, isso pede verificação de sentido em nível alto, não só checagem de fato.
- **Os artigos ficam atrás de páginas humanas bem revisadas:** menos informativos que a Wikipédia real.
- **Transferência de viés e tom das fontes:** 7 dos 10 editores disseram que os artigos soam "emocionais" ou "não neutros". A internet não é neutra e tem muito conteúdo promocional; o sistema não tem módulo de pós-processamento.
- **Tabela 11, problemas citados nos comentários livres (número de menções):** linguagem emocional e não neutra, 12 (exemplo: a palavra "significant" 17 vezes num artigo); falácia do arenque vermelho e associação de fontes não relacionadas, 11 (exemplo: "links to climate change shouldn't be made unless explicitly connected by the source"); falta de informação importante, 6; mau tratamento de informação datada, 5 (usar "now" em vez de "as of December 2023"); problemas de organização das seções, 5 (subseções demais).
- **Análise das frases sem sustentação (Apêndice C.3, Figura 6, 10 artigos sorteados, um autor examinou todas):** falta de citação 47%; falso negativo do juiz (a frase estava sustentada pelo julgamento do autor) 15%; ligação inferencial imprópria 14%; divisão errada de frases pelo `sent_tokenize` do NLTK 12%; paráfrase imprecisa 7%; fonte irrelevante 4%; outros 1%. Tabela 9 traz um exemplo de cada um dos três tipos principais (por exemplo, a fonte sobre religião havaiana que não menciona Lahaina; a data de abertura da ponte da Crimeia parafraseada errado; um guia de desempenho do jogo Battlefield 2042 citado num artigo sobre o LK-99). A recomendação dos autores: além de evitar alucinação, impedir saltos inferenciais exagerados a partir da informação fornecida.

## 8. Limitações e ética declaradas

- A qualidade fica atrás de artigos humanos bem revisados, sobretudo em neutralidade e verificabilidade.
- Mesmo com perspectivas diferentes, a informação coletada pode pender para as fontes dominantes da internet e conter conteúdo promocional; melhorar a recuperação para cobrir pontos de vista diferentes e acrescentar um módulo de triagem de conteúdo seria o próximo passo para neutralidade e equilíbrio.
- A tarefa foi simplificada para texto livre; artigos humanos de qualidade têm dados estruturados e multimodais.
- Só inglês; estender para outras línguas importa porque muitos temas não têm página fora do inglês.
- Nada foi publicado on-line e o sistema não toca páginas vivas da Wikipédia; só informação pública.

## Tudo o mais que ensina

- **Tabela 1, configurações anteriores de geração de Wikipédia:** Balepur et al. (2023), um domínio, um parágrafo, referências dadas; Qian et al. (2023), todos os domínios, um parágrafo, sem referências dadas; Fan e Gardent (2022), um domínio (biografias), artigo inteiro com esboço dado e sem referências dadas; Liu et al. (2018, WikiSum), todos os domínios, um parágrafo com referências dadas, tratado como sumarização de vários documentos; Sauper e Barzilay (2009), dois domínios, artigo inteiro, sem esboço nem referências dados; este trabalho, todos os domínios, artigo inteiro, sem esboço nem referências dados. Gerar um parágrafo não precisa de esboço.
- **Escrita expositiva:** escrita que busca informar o leitor sobre um tema de modo organizado (Weaver e Kintsch, 1991); exige pesquisa e planejamento na pré-escrita e "letramento informacional" avançado (Doyle, 1994) para identificar, avaliar e organizar fontes. Shen et al. (2023): a escrita expositiva pede construção de sentido (sensemaking) sobre as fontes e bom planejamento do esboço. Balepur et al. (2023) propõem imitar, recuperar e parafrasear no nível do parágrafo.
- **Perguntas em PLN:** perguntas de esclarecimento sobre a intenção do usuário (Aliannejadi et al., 2019), decomposição de perguntas grandes para raciocínio composicional (Press et al., 2023); o trabalho mais próximo é Qi et al. (2020), que define informatividade de pergunta pela precisão de unigramas e a aumenta com aprendizado por reforço.
- **RAG:** recuperação como demonstração no contexto ou como informação para ancorar; fontes de domínio, documentação de código ou a internet inteira; recuperar uma vez antes de gerar ou deixar o sistema decidir quando recuperar (Jiang et al., 2023b, e outros). Lewis et al. (2020) mostram que o RAG melhora diversidade e factualidade em tarefas intensivas em conhecimento; Semnani et al. (2023) fazem um chatbot ancorado na Wikipédia em inglês para não alucinar.
- **Os prompts (Listagens 1 e 2):** gerar temas relacionados ("páginas que tragam aspectos interessantes associados ao tema" ou que ajudem a entender o conteúdo e a estrutura típicos); gerar perspectivas (o grupo de editores); gerar pergunta (escritor com foco específico conversando com um especialista); gerar consultas ("o que você digitaria na busca?"); gerar resposta (especialista que usa a informação e sustenta cada frase); gerar esboço direto; refinar esboço com a conversa. Os autores dizem que o STORM é um arcabouço geral que não depende de engenharia de prompt pesada para um domínio.
- **Rubricas:** a Tabela 8 traz as descrições das notas 1 a 5 para o juiz automático e a Tabela 10 as de 1 a 7 para os humanos, nos mesmos aspectos (a de 7 pontos acrescenta degraus intermediários e a verificabilidade).
- **Exemplo completo:** a Tabela 12 traz o artigo gerado pelo STORM sobre o baterista Taylor Hawkins, com seções, subseções e referências numeradas; a Figura 7, a tela do aplicativo de avaliação.
- **Por que o artigo-gabarito importa como referência:** os autores querem artigos humanos de alta qualidade como referência porque os LLMs já geram saídas razoáveis; artigos humanos de qualidade dependem de muitas edições para acumular referências.

---
