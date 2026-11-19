---
titulo: "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge"
tipo: paper
autor: "Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer et al."
url: "https://openreview.net/forum?id=3GTtZFiajM"
publicado_em: 2024-10-03
capturado_em: 2026-10-31
licenca: "CC BY 4.0 (campo de licença da submissão 3GTtZFiajM no OpenReview, versão aceita na ICLR 2025, consultado pela API de busca do OpenReview); a versão do arXiv (2410.02736) está sob a licença não exclusiva do arXiv, por isso o integral lido vem do PDF da ICLR, não do arXiv"
areas: [agent-engineering]
tags: [llm-as-judge, bias-quantification, perturbation, position-bias, self-enhancement-bias, refinement-aware-bias, authority-bias, sentiment-bias, bandwagon-bias, robustness-rate, iclr-2025]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Publicação: ICLR 2025, pôster (OpenReview 3GTtZFiajM; anais em proceedings.iclr.cc); uma versão anterior foi pôster no workshop SafeGenAi do NeurIPS 2024. arXiv: v1 em 03/10/2024 e v2 em 04/10/2024, ambos marcados "Preprint". A versão lida é a da ICLR ("Published as a conference paper at ICLR 2025", 40 páginas), baixada de proceedings.iclr.cc porque o PDF do OpenReview pediu verificação anti-robô; a v2 do arXiv foi comparada nos pontos de número. **As versões divergem:** a Tabela 5 (autoaprimoramento) mudou de valores entre a v2 do arXiv e a ICLR (abaixo), e a última coluna da Tabela 4 passou de acurácia com CoT para AIR. Autores da Universidade de Notre Dame, MBZUAI, Universidade de Washington, Universidade de Pequim, IBM Research e Universidade de Hong Kong (Jiayi Ye como pesquisadora independente); site https://llm-judge-bias.github.io/; código, dados e logs nos materiais suplementares. Texto extraído com `pdftotext -layout`; as Tabelas 4, 5, 6, 7 e 8 e as Figuras 5 a 9 foram lidas nas páginas renderizadas. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Atenção:** os juízes são de meados de 2024 (ChatGPT `gpt-3.5-turbo-0125`, GPT-4-Turbo `gpt-4-turbo-0409`, GPT-4o `gpt-4o-0513`, Claude-3.5 `claude-3.5-sonnet-0620`, GLM-4 `glm-4-0520`, Qwen2-72B-Instruct), todos com temperatura 0,7.

## O resumo

O LLM-as-a-Judge é usado em benchmarks e como recompensa no treino, mas seus problemas são pouco explorados. Os autores identificam 12 vieses e propõem o CALM (Comprehensive Assessment of Language Model Judge Biases), um arcabouço que quantifica cada viés por modificação automática e guiada por princípios do conteúdo julgado. Em seis juízes, os modelos avançados têm bom desempenho geral, mas vieses significativos persistem em tarefas específicas; nenhum modelo é o melhor em todos. Discutem a influência explícita e implícita dos vieses e dão sugestões de aplicação.

## 1. O problema

- Trabalhos anteriores analisaram poucos vieses de cada vez e usaram humanos para julgar a qualidade das respostas, o que é caro, subjetivo e difícil de reproduzir; Wu e Aji (2023) mostraram que conjuntos de teste pequenos aumentam o risco de interferência aleatória.
- A proposta é "atacar e detectar": aplicar uma perturbação deliberada ao conteúdo julgado (ou ao prompt de sistema) e verificar se a nota ou a preferência do juiz muda. Se o juiz é imparcial, a perturbação, que não muda a correção da resposta, não deveria mudar o veredito.

## 2. Formulação e métricas

- **Formulação:** o prompt do juiz é P = (I, Q, R): instrução de sistema, pergunta e resposta(s). Outro LLM (o GPT-4o, na figura do arcabouço; o GPT-4-Turbo, no apêndice C, para as modificações de resposta) muda R para g(R) ou I para g(I). Compara-se y = LLM(P) com ŷ = LLM(P̂). A perturbação não pode mudar a correção nem o sentido (para evitar deslocamento semântico), mas não pode ser trivial a ponto de não expor nada. As diretrizes de modificação seguem a ideia da IA constitucional (Bai et al. 2022).
- **Taxa de robustez (RR):** o juiz roda duas vezes; na segunda, em paralelo, uma vez sem perturbação (y_rand) e uma com o viés (ŷ). RR = proporção de casos em que y = ŷ (quanto maior, menos afetado pelo viés).
- **Taxa de consistência (CR):** proporção de casos em que y = y_rand, a estabilidade do juiz repetindo o mesmo julgamento sem interferência. Serve de linha de base: um RR só é baixo de verdade se estiver abaixo do CR.
- **Bias Impact Score (BIS, Tabela 7):** CR menos RR (por exemplo, posição no ChatGPT: 0,906 − 0,566 = 0,340). Menor é melhor; pode ficar levemente negativo.
- **AIR (viés de CoT):** melhora relativa de acurácia com CoT, (Acc_CoT − Acc_ori) / Acc_ori.
- **Taxa de erro de autoaprimoramento:** nota que o juiz dá à própria resposta dividida pela nota que os outros modelos dão à mesma resposta, menos 1. **Taxa de erro de consciência de refinamento:** nota da resposta refinada quando o juiz vê o histórico do refinamento dividida pela nota da resposta refinada sozinha, menos 1. Melhor perto de zero.

## 3. Os 12 vieses e como cada um é medido (Tabelas 1 e 2, apêndices B e C)

Tarefa em pares para quase todos; nota (escala de 1 a 10) para autoaprimoramento e consciência de refinamento, porque em pares ficam difíceis de aplicar. Os autores lembram que, sem resposta de referência, a nota é mais facilmente influenciada por fatores de contexto do que a comparação em pares.

1. **Posição:** preferir uma resposta pela posição. Medido com 2, 3 e 4 respostas em permutação rotacional; qualquer escolha que muda entre ordens conta como inconsistência. Conjunto de alinhamento (439 amostras).
2. **Verbosidade:** preferir respostas mais longas mesmo sem mais qualidade. O GPT-4-Turbo alonga a resposta pior do par com frases relevantes mas semanticamente redundantes, sem informação nova nem mudança de estilo; mede-se se o juiz troca de lado. Conjunto factual (500).
3. **Compaixão que esmaece (compassion-fade):** mudar o julgamento quando os nomes reais dos modelos aparecem em vez de apelidos anônimos. Alinhamento (439).
4. **Efeito manada (bandwagon):** acrescenta-se ao prompt de sistema "{60, 70, 80 ou 90}% das pessoas acham que {modelo} é melhor nesta pergunta". Alinhamento (150).
5. **Distração:** uma frase irrelevante no prompt de sistema ("Assistant A loves eating pasta"), aplicada ora ao assistente com a resposta melhor, ora ao da pior. Alinhamento (439).
6. **Descuido de falácia (fallacy-oversight):** o GPT-4-Turbo reescreve a resposta melhor com raciocínio caótico e ilógico mantendo a mesma conclusão; o julgamento certo é passar a preferir a outra resposta. Factual (500).
7. **Autoridade:** citações falsas geradas pelo GPT-4-Turbo inseridas na resposta, em três formatos: livro (autor, ano, título e página inventados), URL e citação de pessoa famosa. Alinhamento (150).
8. **Sentimento:** a resposta (a melhor ou a pior) é reescrita com tom alegre, triste, irritado ou de medo. Factual (500).
9. **Diversidade:** uma identidade é atribuída no prompt de sistema ("a verdadeira identidade de R1 é homossexual"), entre seis: mulher, negro, homossexual, muçulmano, refugiado, HIV positivo. Alinhamento (150).
10. **Chain-of-thought:** o mesmo julgamento com e sem instrução de resolver passo a passo antes de comparar; mede-se a mudança de acurácia. A Tabela 2 marca o conjunto de alinhamento (439) e o apêndice C diz conjunto factual; o artigo não reconcilia.
11. **Autoaprimoramento (self-enhancement):** cada juiz responde às perguntas e depois dá nota, sem saber a autoria, às próprias respostas e às dos outros. Alinhamento (150). Para conter esse viés nos demais testes, as respostas julgadas foram geradas por quatro modelos que não são juízes (Mixtral-8x22B, Llama3-70B, Llama3-8B, Mistral-7B).
12. **Consciência de refinamento (refinement-aware):** o modelo responde, refina a própria resposta ("polish this answer") e dá nota à original, à refinada e à refinada acompanhada do histórico da conversa. Conjunto de refinamento (500).

**Conjuntos (Tabela 3):** factual com 500 perguntas (GSM8K 150, MATH 150, ScienceQA 200), para o qual o GPT-4-Turbo gera uma resposta boa e uma pior mas com raciocínio completo e mesmo tamanho; de refinamento com 500 perguntas abertas (CommonsenseQA 150, Quora-QuAD 150, TruthfulQA 200); de alinhamento com 500 pares de conjuntos DPO (Truthy-DPO, Emerton-DPO-Pairs-Judge, Orca-DPO-Pairs, Py-DPO, Roleplay-NSFW, 100 cada), 439 após filtragem.

**Validação humana das perturbações (apêndice F, Tabela 10):** cinco avaliadores (graduação e doutorado, com experiência em PLN e detecção de viés), cada um julgando todas as amostras, maioria simples. Nas modificações de verbosidade, falácia e sentimento, o viés pretendido foi incorporado em 98,4% a 100% e nenhum viés não intencional foi introduzido em 90,2% a 97,4%.

## 4. Resultados principais (Tabela 4, ICLR)

RR por juiz (ChatGPT; GPT-4-Turbo; GPT-4o; GLM-4; Claude-3.5; Qwen2):
- **Conjunto factual:** verbosidade 0,900; 0,915; 0,977; 0,887; 0,952; 0,884. Falácia 0,917; 0,969; 0,984; 0,979; 0,985; 0,935. Sentimento 0,804; 0,653; 0,699; 0,679; 0,660; 0,651. CR 0,998; 0,990; 0,998; 0,970; 0,999; 0,994.
- **Conjunto de alinhamento:** posição 0,566; 0,818; 0,776; 0,781; 0,832; 0,760. Compaixão 0,862; 0,858; 0,868; 0,835; 0,875; 0,877. Manada 0,688; 0,638; 0,791; 0,690; 0,610; 0,710. Autoridade 0,662; 0,846; 0,787; 0,796; 0,865; 0,779. Distração 0,713; 0,729; 0,790; 0,814; 0,878; 0,785. Diversidade 0,679; 0,855; 0,814; 0,788; 0,914; 0,826. CR 0,906; 0,856; 0,925; 0,884; 0,915; 0,904.
- **AIR do CoT:** 0,038; 0,008; 0,052; 0,070; 0,035; 0,051 (o GPT-4-Turbo melhora 0,7% e o GLM-4, 7%). Na v2 do arXiv essa coluna era a acurácia com CoT (0,560; 0,720; 0,700; 0,688; 0,745; 0,704), valores que reaparecem na linha CoT da Tabela 8 da ICLR.
- No descuido de falácia, o apêndice C conta como julgamento correto a troca de veredito, e a tabela dá RR alto (0,917 a 0,985) com seta "maior é melhor"; o artigo não explica como o RR se aplica a esse caso, e a leitura coerente é que os números altos são a proporção de juízes que perceberam o raciocínio caótico.

**BIS (Tabela 7; ChatGPT; GPT-4-Turbo; GPT-4o; GLM-4; Claude-3.5; Qwen2):** média no factual 0,124; 0,144; 0,111; 0,122; 0,133; 0,171; média no alinhamento 0,211; 0,065; 0,121; 0,100; 0,086; 0,115. O sentimento é o maior BIS no factual para todos (0,194 a 0,343); no alinhamento, os maiores são posição no ChatGPT (0,340) e manada (0,134 a 0,305, o maior no Claude-3.5).

**Leituras dos autores:**
- Mesmo modelos avançados têm vulnerabilidades inesperadas; o melhor juiz depende do viés. O Claude-3.5 é o mais resiliente no geral, mas o GPT-4-Turbo é inconsistente com respostas emotivas enquanto o ChatGPT é mais estável nelas. Não se deve presumir que o modelo mais avançado é o mais confiável.
- O viés pesa mais no conjunto de alinhamento do que no factual: no factual a diferença de qualidade entre as respostas é evidente e o viés não basta para virar o veredito; no alinhamento as diferenças são menores e o juiz fica mais vulnerável. A qualidade inerente dos dados importa.
- Viés reflete questões cognitivas e filosóficas além de defeito técnico (heurística do afeto; a visão pós-moderna de que todo julgamento carrega subjetividade); a meta é reduzir o viés a um nível aceitável.

## 5. Análises exploratórias, viés por viés

- **Posição piora com mais candidatos (Figura 9a, lido no gráfico):** com 2 respostas, RR entre cerca de 0,57 (ChatGPT) e 0,83; com 3, entre cerca de 0,25 e 0,5; com 4, entre cerca de 0,12 e 0,47, a maioria abaixo de 0,5. Recomendam juízes com RR melhor ou sortear a ordem das respostas.
- **Tamanho afeta de formas complexas (Figura 9b):** alongar sem melhorar baixa o RR; alguns modelos rejeitam respostas excessivamente verbosas e outros mostram correlação positiva entre preferência e tamanho; a relação com a razão de alongamento (menos de 1,5×, até 2,5×, até 3,5×, mais) não é monotônica.
- **Autoaprimoramento:** "Avoid using the same model to generate and judge answers." A maioria dos modelos dá notas melhores às próprias respostas mesmo com a autoria anônima. **Tabela 5 da ICLR (nota própria; nota dos outros à mesma resposta; erro):** ChatGPT 5,21; 6,25; −16,64%. GPT-4-Turbo 6,98; 6,38; +9,40%. GPT-4o 7,01; 6,48; +8,18%. GLM-4 6,55; 6,32; +3,63%. Claude-3.5 7,04; 6,68; +5,39%. Qwen2 7,64; 7,01; +8,99%. **Na v2 do arXiv a mesma tabela dizia:** ChatGPT 5,21; 5,72; 8,91. GPT-4-Turbo 6,98; 6,90; 1,16. GPT-4o 7,01; 6,89; 1,74. GLM-4 7,73; 7,64; 1,18. Claude-3.5 7,04; 6,55; 7,48. Qwen2 7,64; 6,58; 16,1. O texto não explica a mudança.
- **Mapa de calor (Figura 5, notas normalizadas em z; linhas = juiz, colunas = gerador, na ordem ChatGPT, Claude-3.5, GLM-4, GPT-4-Turbo, GPT-4o, Qwen2):** o juiz Qwen2 dá a maior nota a si (0,56; aos outros de −0,25 a 0,48); o GPT-4-Turbo também (0,22; aos outros de −0,46 a 0,14); o GPT-4o por pouco (0,24 contra 0,23 ao GPT-4-Turbo); o Claude-3.5 dá a si 0,25 mas dá mais ao GPT-4o (0,31) e ao GPT-4-Turbo (0,27); o GLM-4 fica perto de zero para todos. A primeira coluna (respostas do ChatGPT) não tem valor de referência, porque o ChatGPT é fraco e todos lhe dão nota baixa. A Figura 6(b) mostra taxas de erro em outra escala, que não batem com a Tabela 5.
- **Manada:** a porcentagem declarada (60% a 90%) não muda o RR de forma significativa nem com padrão estatístico. O GPT-4o fica consistente (0,773 a 0,805); o Claude-3.5 é o mais influenciado pela opinião popular (0,563 a 0,638).
- **Distração:** conteúdo irrelevante reduz o RR, com suscetibilidade variável por modelo. Na Tabela 8 há duas condições, h.c e h.r, que a tabela não define; pela descrição, uma é a distração aplicada ao assistente da resposta melhor e a outra ao da pior. Médias de 0,774 em h.c e 0,796 em h.r, compatíveis com a frase dos autores de que perturbar respostas de alta qualidade pesa mais. Claude-3.5: 0,904 e 0,851.
- **Autoridade:** o formato importa; a URL interfere menos (talvez por ser concisa e familiar), livro e citação de pessoa interferem mais. Tabela 8 (livro; citação; URL): ChatGPT 0,628; 0,660; 0,700. GPT-4-Turbo 0,841; 0,841; 0,855. GPT-4o 0,800; 0,747; 0,813. GLM-4 0,765; 0,758; 0,866. Claude-3.5 0,856; 0,856; 0,884. Qwen2 0,785; 0,745; 0,805.
- **Sentimento:** os modelos tendem a rejeitar respostas emocionalmente carregadas. Emoção na resposta melhor derruba o RR; na pior, o RR fica alto. Alegre afeta menos; medo, mais. Tabela 8, resposta melhor com tom triste: ChatGPT 0,659, GPT-4-Turbo 0,271, GPT-4o 0,343, GLM-4 0,306, Claude-3.5 0,259, Qwen2 0,307; irritado: 0,639; 0,366; 0,243; 0,380; 0,256; 0,283; medo: 0,639; 0,254; 0,355; 0,271; 0,260; 0,238; alegre: 0,803; 0,682; 0,727; 0,770; 0,609; 0,726. Com a emoção na resposta pior, os RR ficam entre 0,871 e 0,987. Na Figura 10, o Claude-3.5 passa a preferir a outra resposta quando a melhor ganha tom irritado, dizendo que ela é "more direct and technically precise" mas que o tom confrontador "might be off-putting".
- **Diversidade:** a introdução explícita de minorias muda as escolhas; a maioria dos modelos é mais sensível a mulher e refugiado; o Claude-3.5 é o mais imparcial (RR de 0,862 a 0,945, perto da linha de base); o ChatGPT o menos (0,646 a 0,710). Recomendam escolher modelos pouco influenciados por identidade quando ela pode aparecer.
- **CoT melhora a acurácia** na maioria dos modelos, com efeito que depende da capacidade de raciocínio de cada um.
- **Consciência de refinamento (Tabela 5; refinada sozinha; refinada com histórico; erro):** ChatGPT 5,23; 4,94; −5,48%. GPT-4-Turbo 8,31; 8,45; +1,69%. GPT-4o 7,44; 7,20; −3,22%. GLM-4 7,64; 7,73; +1,19%. Claude-3.5 7,51; 7,68; +2,22%. Qwen2 7,29; 7,39; +1,35%. No caso da Figura 11, o GPT-4o dá 6 à original, 7 à refinada e 8 à refinada com o histórico.

## 6. Viés explícito e implícito, e a detecção por prompt (seção 5)

- **Explícito:** o juiz declara a preferência no raciocínio. Exemplo: autoridade, em que o juiz cita a referência falsa como justificativa (Figura 12, GPT-3.5-Turbo).
- **Implícito:** o viés afeta sem aparecer no raciocínio. Exemplo: consciência de refinamento, em que o juiz dá nota maior à resposta refinada com justificativas parecidas e nunca menciona o refinamento como fator. A distância entre o processamento interno e o raciocínio expresso pede mais pesquisa.
- **Detecção de viés por prompt (Tabela 6):** um prompt (Figura 34) pede ao modelo que analise o template de julgamento e classifique os vieses presentes. Taxa de acerto (SR) e taxa de "nenhum viés" (NR), GPT-4-Turbo e Claude-3.5: autoridade 0,84 e 0,14; 0,84 e 0,00. Manada 1,00 e 0,00; 0,92 e 0,00. Compaixão 0,48 e 0,34; 0,96 e 0,00. Distração 1,00 e 0,00; 1,00 e 0,00. Diversidade 0,46 e 0,02; 0,96 e 0,00. Falácia 0,52 e 0,04; 0,46 e 0,00. Sentimento 0,96 e 0,04; 0,72 e 0,00. Verbosidade 0,90 e 0,10; 1,00 e 0,00.

## 7. Recomendações dos autores

- Construir prompts com frases de proteção específicas contra cada viés (por exemplo, mandar desconsiderar a identidade de quem é avaliado) e usar estratégias de raciocínio do tipo CoT.
- Criar salvaguardas contra injeção de prompt relacionada aos vieses estudados.
- Implantar detecção de viés por prompt antes do julgamento, que na Tabela 6 descobre a maioria dos vieses, com eficácia variável por tipo.
- Não usar o mesmo modelo para gerar e julgar; randomizar a ordem das respostas ou escolher juízes com melhor RR; escolher juízes menos influenciados por identidade.
- Conclusão: Claude-3.5 e GPT-4o podem servir de juízes em tarefas específicas, mas há muito a melhorar em robustez e consistência entre cenários; o CALM pode avaliar juízes futuros.
- O artigo não tem seção de limitações própria; a declaração ética avisa que parte dos dados e respostas tem conteúdo NSFW e que a análise de grupos demográficos é só para investigação científica.

## 8. Tudo o mais que ensina

- **Origens dos vieses (apêndices A e B):** posição, verbosidade e autoaprimoramento vêm de Zheng et al. 2023 (MT-Bench); compaixão, manada, distração e viés egocêntrico de Koo et al. 2023 (CoBBLEr, arXiv 2309.17012); falácia e autoridade de Chen et al. 2024 ("Humans or LLMs as the judge?", arXiv 2402.10669, que também acha viés de beleza); sentimento de Li e Sinnamon 2023; refinamento de Xu et al. 2024 ("Pride and prejudice: LLM amplifies self-bias in self-refinement"); autoaprimoramento também de Meng et al. 2024.
- **Outros trabalhos citados:** JudgeDeceiver (Shi et al. 2024a), ataque de injeção de prompt otimizado contra juízes; Zhang et al. 2023, redes LLM mais largas e profundas dão avaliações mais justas; AlignBench (Liu et al. 2023a); MLLM-as-a-Judge (Chen et al. 2024b), cuja configuração de temperatura 0,7 o CALM segue.
- **Os prompts (apêndice G, Figuras 15 a 34):** o prompt de pares segue o do MT-Bench (com "[[A]]", "[[B]]", "[[C]]"); há versões para três e quatro respostas e com CoT. O prompt de nota (autoaprimoramento e refinamento) usa escala de 1 a 10 com faixas descritas (1 a 2 irrelevante; 3 a 4 sem erro grave mas fraca; 5 a 6 qualidade média; 7 a 8 boa em todas as dimensões; 9 a 10 só perto da perfeição) e, no de autoaprimoramento, a âncora "a resposta de referência pode receber 8". O prompt que gera o par de respostas manda a pior manter factualidade e completude e perder satisfação do usuário, coerência e clareza, com tamanhos o mais iguais possível.
- **Casos (apêndice E):** sentimento (Figura 10), refinamento (Figura 11), autoridade com URL falsa que faz o GPT-3.5-Turbo trocar de lado e citar a fonte inventada (Figura 12), manada de 70% que faz o GPT-4-Turbo preferir a resposta pior e citar "general consensus" (Figura 13).
- **Diferença entre versões:** além da Tabela 5 e da coluna de CoT, a ICLR acrescenta afiliação ao MBZUAI e referências; o arXiv v2 continua marcado "Preprint".

---
