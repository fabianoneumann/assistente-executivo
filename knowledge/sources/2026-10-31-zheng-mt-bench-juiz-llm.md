---
titulo: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
tipo: paper
autor: "Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li et al."
url: "https://arxiv.org/abs/2306.05685"
publicado_em: 2023-06-09
capturado_em: 2026-10-31
licenca: "Licença não exclusiva de distribuição do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0, indicada na página do arXiv); a versão dos anais do NeurIPS 2023 (DOI 10.52202/075280-2020) não traz licença aberta (o OpenAlex registra licença nula). Entra só a ficha."
areas: [agent-engineering]
tags: [llm-as-judge, mt-bench, chatbot-arena, position-bias, verbosity-bias, self-enhancement-bias, position-swap, reference-guided-grading, human-agreement, pairwise-comparison, single-answer-grading, neurips-2023]
---

Ficha de estudo, em palavras próprias; sem texto integral. arXiv: v1 em 09/06/2023, v2 em 12/07/2023, v3 em 15/10/2023 e v4 em 24/12/2023; lida a v4 (PDF do arXiv, 29 páginas com apêndices). O comentário do arXiv e o rodapé do PDF dizem NeurIPS 2023, Track on Datasets and Benchmarks (37ª conferência); o OpenAlex registra a versão dos anais com o DOI 10.52202/075280-2020. Autores da UC Berkeley, UC San Diego, Carnegie Mellon, Stanford e MBZUAI (equipe LMSYS, a mesma do Vicuna); o artigo estende um post de blog anterior do Vicuna. Código, as 80 perguntas do MT-bench, 3 mil votos de especialistas e 30 mil conversas com preferência humana em https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge. Texto extraído com `pdftotext -layout`; as Tabelas 5, 6 e 13 e a Figura 3 foram conferidas nas páginas renderizadas. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Atenção:** os modelos são os de 2023 (GPT-4 `gpt-4-0314`, GPT-3.5, Claude-v1, Vicuna-13B); os autores avisam que os exemplos podem não se reproduzir com versões futuras do GPT-4.

## O resumo

Avaliar assistentes de chat é difícil porque os benchmarks clássicos (MMLU, HELM) medem capacidade em tarefas fechadas e não captam a preferência humana em perguntas abertas. Os autores estudam usar LLMs fortes como juízes ("LLM-as-a-judge"), examinam seus vieses (posição, verbosidade, autoaprimoramento) e a capacidade limitada de raciocínio, propõem soluções para parte deles e verificam a concordância com humanos em dois benchmarks novos: o MT-bench (perguntas de várias rodadas) e o Chatbot Arena (batalhas anônimas com votos de usuários). O GPT-4 como juiz passa de 80% de concordância com humanos, o mesmo nível da concordância entre humanos.

## 1. O problema e os dois benchmarks

- **Motivação:** um LLaMA-13B base e o Vicuna-13B (ajustado nele) empatam em benchmarks clássicos, mas a resposta do base a uma pergunta aberta é claramente pior para humanos (Figura 1). Os benchmarks existentes caem em três tipos (conhecimento central como MMLU e GSM-8K; seguimento de instrução como Flan; conversacionais como CoQA), nenhum medindo bem a preferência em diálogos abertos.
- **MT-bench:** 80 perguntas de duas rodadas, feitas à mão, 10 por categoria em oito categorias: escrita, roleplay, extração, raciocínio, matemática, código, conhecimento I (STEM) e conhecimento II (humanidades e ciências sociais). A segunda rodada pede uma mudança ("reescreva começando cada frase com a letra A"; "explique de novo como se eu tivesse cinco anos").
- **Chatbot Arena:** plataforma de batalhas anônimas; o usuário conversa com dois modelos ao mesmo tempo, vota e só depois vê os nomes. Cerca de 30 mil votos no primeiro mês, sem perguntas predefinidas.

## 2. Três formas de juiz (seção 3.1)

- **Comparação em pares:** o juiz recebe a pergunta e duas respostas e escolhe a melhor ou empate.
- **Nota de resposta única:** o juiz dá uma nota direta (escala de 1 a 10 no prompt padrão).
- **Nota guiada por referência:** o juiz recebe uma resposta de referência (usado em matemática).
- **Prós e contras declarados:** pares não escalam (o número de pares cresce quadraticamente com o número de jogadores); a nota única pode não discernir diferenças sutis entre um par específico e é mais instável, porque notas absolutas tendem a flutuar mais que resultados relativos quando o modelo juiz muda.
- **Vantagens do juiz LLM:** escala (menos humano no circuito, iteração rápida) e explicabilidade (o juiz dá a nota e a explicação).

## 3. Os vieses e limites, com os números (seção 3.3)

**Viés de posição** (preferir certa posição). Teste: para cada pergunta de primeira rodada do MT-bench, duas respostas parecidas geradas pelo GPT-3.5 com temperatura 0,7; o juiz julga nas duas ordens. Consistência é a porcentagem de casos com o mesmo veredito após trocar a ordem. Os autores avisam que o teste é difícil, porque as respostas são muito parecidas e às vezes indistinguíveis até para humanos.
- Tabela 2 (consistência; favorece a primeira; favorece a segunda; erro de formato): Claude-v1 padrão 23,8%, 75,0%, 0,0%, 1,2%; Claude-v1 com os assistentes renomeados 56,2%, 11,2%, 28,7%, 3,8%; GPT-3.5 padrão 46,2%, 50,0%, 1,2%, 2,5%; renomeado 51,2%, 38,8%, 6,2%, 3,8%; GPT-4 padrão 65,0%, 30,0%, 5,0%, 0,0%; renomeado 66,2%, 28,7%, 5,0%, 0,0%.
- Todos têm forte viés de posição, a maioria a favor da primeira; o Claude-v1 também tem viés de nome (favorece "Assistant A", como mostra o prompt renomeado). Só o GPT-4 passa de 60% de consistência.
- Tabela 9 (mais dois prompts): "score", em que o juiz dá duas notas absolutas em vez de escolher, sobe a consistência do GPT-3.5 (55,0%) mas derruba a do Claude-v1 (20,0%, 80,0% para a primeira) e a do GPT-4 (51,2%, 46,2% para a primeira); "short", sem as instruções contra viés e sem pedir explicação: Claude-v1 22,5%, GPT-3.5 38,8%, GPT-4 62,5%. Prompts diferentes afetam modelos diferentes de formas diferentes.
- Tabela 10 (GPT-4 por categoria; consistente, primeira, segunda): escrita 42%, 46%, 12%; roleplay 68%, 30%, 2%; raciocínio 76%, 20%, 4%; matemática 86%, 4%, 10%; código 86%, 14%, 0%; extração 78%, 12%, 10%; STEM 44%, 54%, 2%; humanidades 36%, 60%, 4%. O viés é maior nas perguntas abertas; em matemática e código o juiz é mais confiante, embora muitas vezes errado.
- Tabela 11 (GPT-4, por par de modelos): GPT-3.5 contra Claude-v1, 67,5% consistente; contra Vicuna-13B, 73,8%; contra LLaMA-13B, 98,8%. O viés de posição é maior entre modelos de desempenho parecido e quase some quando a diferença é grande.
- Origem suspeita (não estudada): dados de treino ou a arquitetura causal da esquerda para a direita. O viés também existe em decisão humana e em outros domínios de ML.

**Viés de verbosidade** (preferir respostas longas mesmo quando não são mais claras, melhores ou corretas). Ataque "repetitive list": 23 respostas do MT-bench com lista numerada; o GPT-4 reescreve os itens sem informação nova e a lista reescrita é inserida antes da original (5 itens viram 10, os 5 primeiros repetidos com outras palavras). O ataque vence se o juiz prefere a versão inchada.
- Tabela 3, taxa de falha: Claude-v1 91,3%, GPT-3.5 91,3%, GPT-4 8,7%. Calibração: com duas respostas idênticas, todos os juízes sempre dão empate; a falha aparece só no ataque mais sutil. Na Figura 12, GPT-3.5 e Claude-v1 elogiam as "definições reformuladas" como mais completas; o GPT-4 aponta a redundância.

**Viés de autoaprimoramento** (self-enhancement, termo emprestado da literatura de cognição social: o juiz favorecer respostas geradas por ele mesmo). Análise só estatística, pela Figura 3(b), taxas de vitória sem empates no MT-bench sob cada juiz contra os humanos: o GPT-4 dá a si mesmo cerca de 10 pontos a mais de taxa de vitória do que os humanos dão (perto de 0,90 contra 0,80); o Claude-v1, cerca de 25 pontos a mais (perto de 0,91 contra 0,65). Mas eles também favorecem outros modelos, e o GPT-3.5 não se favorece. Conclusão dos autores: com poucos dados e diferenças pequenas, o estudo não consegue determinar se há viés de autoaprimoramento; um estudo controlado é difícil porque não dá para reescrever uma resposta no estilo de outro modelo sem mudar a qualidade.

**Capacidade limitada em matemática e raciocínio.** O juiz erra ao julgar até problemas que sabe resolver sozinho, porque é induzido pelas respostas que está julgando. Na Figura 13, o GPT-4 dá como certo um total de US$ 295 que ele mesmo calcula como 280 quando perguntado à parte; na Figura 14, aceita como corretas duas respostas erradas ("false") a um problema que, sozinho, resolve como "true". GPT-3.5 e Claude-v1 mostram a mesma fraqueza.

## 4. As defesas (seção 3.4)

- **Troca de posição:** a abordagem conservadora chama o juiz duas vezes com a ordem trocada e só declara vitória quando a mesma resposta vence nas duas ordens; se o resultado muda, é empate. A abordagem agressiva sorteia a posição, o que funciona em escala com a expectativa correta. Os experimentos seguintes usam a conservadora.
- **Juiz few-shot:** três exemplos de julgamento (A melhor, B melhor, empate), com respostas de GPT-3.5 e Vicuna e julgamentos do GPT-4. Tabela 12: consistência do Claude-v1 de 23,8% para 63,7%; do GPT-3.5 de 46,2% para 55,0% (mas o viés muda da primeira para a segunda posição: 16,2% primeira, 28,7% segunda); do GPT-4 de 65,0% para 77,5% (10,0% e 12,5%). Ressalvas: consistência alta não implica acurácia alta; os exemplos podem introduzir vieses novos; o prompt mais longo deixa a chamada 4 vezes mais cara; a concordância do GPT-4 few-shot com humanos no MT-bench ficou parecida com a do zero-shot. O padrão segue zero-shot.
- **Juiz com chain-of-thought:** o juiz resolve a pergunta sozinho antes de julgar (Figura 7). Mesmo assim, muitas vezes repete exatamente o erro das respostas dadas (Figura 15: copia o raciocínio errado da resposta B e dá 20 inteiros quando o certo é 19).
- **Juiz guiado por referência:** primeiro gera a resposta do juiz de forma independente, depois a mostra como referência no prompt de julgamento. Tabela 4 (10 perguntas de matemática, LLaMA-13B contra Vicuna-13B nas duas ordens, falha = o GPT-4 dizer que uma resposta errada está certa): padrão 14/20, CoT 6/20, referência 3/20 (de 70% para 15%).
- **Ajuste fino de um juiz:** Vicuna-13B treinado com votos do Arena (apêndice F, abaixo).
- **Juiz de várias rodadas (seção 3.5):** quebrar as duas rodadas em dois prompts faz o juiz se perder ao localizar a resposta anterior (Figura 16: atribui ao assistente A o "segundo exemplo" do assistente B). Mostrar as duas conversas completas num prompt só, pedindo foco na segunda pergunta, alivia o problema.

## 5. A concordância com humanos (seção 4)

**Montagem:** no MT-bench, respostas de seis modelos (GPT-4, GPT-3.5, Claude-v1, Vicuna-13B, Alpaca-13B, LLaMA-13B) às 80 perguntas; juízes LLM julgam todos os pares; 58 rotuladores especialistas (na maioria pós-graduandos de mais de dez universidades, pagos US$ 20 por 20 perguntas, cerca de US$ 35 por hora) julgam cada um pelo menos 20 perguntas aleatórias, cerca de 3 mil votos. No Arena, 3 mil votos de uma rodada sorteados dos 30 mil, com GPT-4, GPT-3.5, Claude, Vicuna-7B/13B, Koala-13B, Alpaca-13B, LLaMA-13B e Dolly-12B, de 2.114 IPs únicos.

**Métrica:** concordância é a probabilidade de dois indivíduos sorteados de cada tipo (não idênticos) concordarem numa pergunta sorteada. Setup S1 inclui vitórias, empates e votos inconsistentes por viés de posição (contados como empate), acaso de 33%; S2 só os votos sem empate, acaso de 50%.

**Tabela 5, MT-bench, primeira rodada (concordância; votos):** GPT-4 em pares contra humanos 66% (1.343) em S1 e 85% (859) em S2; GPT-4 nota única contra humanos 60% (1.280) e 85% (739); humano contra humano 63% (721) e 81% (479); GPT-4 pares contra GPT-4 nota única 70% (1.138) e 97% (662). Segunda rodada: GPT-4 pares contra humanos 66% e 85%; nota única contra humanos 59% e 84%; humano contra humano 67% e 82%; pares contra nota única 70% e 95%.
- A frase do resumo ("mais de 80%, o mesmo nível entre humanos") vale para o setup S2, sem empates: 85% do GPT-4 contra 81% entre humanos na primeira rodada. Com empates e inconsistências (S1), os números caem para 66% e 63%.
- Quando o voto humano divergia do GPT-4, os autores mostravam o julgamento do GPT-4: os humanos o acharam razoável em 75% dos casos e mudaram a própria escolha em 34%.
- Tabela 13 (apêndice D.3) acrescenta Claude, os votos dos autores e a maioria humana ("Human-M"), porque a concordância entre humanos subestima o teto (três humanos votando A, A, B concordam só 1/3; o GPT-4 votando A concorda 2/3). Primeira rodada, S2: GPT-4 pares contra a maioria humana 85%; humano contra a maioria humana 90%; Claude contra humanos 85%; GPT-4 pares contra Claude 94%. S1: GPT-4 pares contra a maioria 67%; humano contra a maioria 81%; Claude contra humanos 54%.

**Tabela 6, Chatbot Arena (S1; S2):** GPT-4 contra humanos 64% e 87% (1.944 votos sem empate); GPT-4 nota única contra humanos 60% e 85%; GPT-3.5 contra humanos 54% e 83%; Claude contra humanos 53% e 84%; GPT-4 contra GPT-4 nota única 72% e 95%. Os outros juízes atingem razão de concordância sem empate parecida, mas o GPT-4 dá muito mais votos sem empate: é mais afirmativo e sofre menos com posição.

**Nota única contra pares:** nos dois benchmarks a nota única do GPT-4 bate bem com os pares do GPT-4 e com humanos, o que os autores leem como "rubrica interna relativamente estável"; às vezes rende um pouco menos que pares e dá mais empates, mas escala melhor.

**Figura 2:** por par de modelos, a concordância GPT-4 e humano sobe com a diferença de taxa de vitória entre os dois modelos, de cerca de 70% (modelos parecidos) a quase 100% (muito diferentes). O GPT-4 se alinha melhor com humanos quando há diferença grande de desempenho.

**Taxas de vitória (Figuras 3 e 4, Tabela 7):** as curvas dos juízes LLM acompanham as dos humanos. Na segunda rodada do MT-bench, humanos preferem mais Claude e GPT-3.5 do que na primeira, o que mostra que várias rodadas diferenciam habilidades. Tabela 7 (taxa de vitória por categoria): GPT-4 de 49,3% (raciocínio) a 76,6% (STEM); LLaMA-13B de 2,1% (código) a 15,1% (escrita e roleplay).

## 6. Benchmark de preferência e benchmark padronizado (seção 5)

Tabela 8, variantes do LLaMA (MMLU 5-shot; TruthfulQA; nota MT-bench pelo GPT-4 em nota única, média de 160 notas = 80 perguntas × 2 rodadas, escala de 10): LLaMA-7B 35,2, 0,22, 2,74; LLaMA-13B 47,0, 0,26, 2,61; Alpaca-13B 48,1, 0,30, 4,53; Vicuna-7B "selected" (4,8 milhões de tokens, 3 mil conversas) 37,3, 0,32, 5,95; Vicuna-7B "all" (370 milhões) 47,1, 0,32, 6,00; Vicuna-13B "all" 52,1, 0,35, 6,39; GPT-3.5 70,0, 7,94; GPT-4 86,4, 8,99. Ajuste fino em diálogos de qualidade melhora o MMLU em proporção ao volume; um conjunto pequeno de alta qualidade ensina depressa o estilo preferido pelo GPT-4 (ou, aproximadamente, por humanos) sem melhorar o MMLU. Nenhum benchmark sozinho determina a qualidade; recomendam avaliação híbrida (capacidade e preferência).

## 7. Limitações declaradas e direções

- O estudo enfatiza utilidade (helpfulness) e quase ignora segurança, honestidade e inocuidade.
- Dentro da utilidade, várias dimensões (acurácia, relevância, criatividade) foram combinadas numa métrica só.
- As soluções para os vieses são preliminares.
- Direções futuras: benchmarks maiores, juiz aberto alinhado à preferência humana, melhorar matemática e raciocínio dos modelos abertos.

## 8. Tudo o mais que ensina

- **Os prompts (apêndice A):** o prompt padrão de pares pede para considerar utilidade, relevância, acurácia, profundidade, criatividade e nível de detalhe; manda comparar e explicar antes; diz para evitar viés de posição, não deixar o tamanho influenciar, não favorecer nomes, e dar o veredito no formato "[[A]]", "[[B]]" ou "[[C]]" (empate). O de nota única pede explicação curta e nota de 1 a 10 no formato "[[rating]]". Há versões com CoT (resolver antes), com referência e para várias rodadas.
- **Casos (apêndice B):** a Figura 11 mostra o GPT-4 trocando de lado quando a ordem de duas respostas sobre etiqueta de negócios no Japão é invertida, com justificativas espelhadas ("mais detalhada e organizada").
- **Coleta de dados (apêndice C):** humanos podiam pular até 5 perguntas sem confiança e viam solução de referência em matemática e raciocínio; o Arena é gratuito, sem cadastro, e o usuário aceita termos que permitem liberar as conversas; os dados liberados têm PII limpa e conversas tóxicas marcadas pela API de moderação da OpenAI.
- **Vicuna como juiz (apêndice F, Tabela 15):** zero-shot, o Vicuna-13B tem consistência de 11,2% a 16,2% e erro de formato de 22,5% a 78,8%. Ajustado com 20 mil votos do Arena (2 mil de validação) como classificação de três classes (A, B, empate), sobe a 65,0% de consistência, 0% de erro, e 56,8% de concordância com três rótulos e 85,5% sem empates, contra 66% e 87% do GPT-4. Os autores o veem como substituto barato promissor.
- **Treino do Vicuna (apêndice E):** 125 mil conversas do ShareGPT após limpeza; "selected" é um conjunto de 3 mil sequências com pelo menos 3 rodadas geradas pelo GPT-4, escolhidas como centróides de 3 mil clusters.
- **Trabalhos relacionados citados:** Blunch 1984 (viés de posição em questões de múltipla escolha); Brown 1986 (vieses de autoaprimoramento em julgamento social); Chiang e Lee 2023 (LLMs como alternativa à avaliação humana); Wang et al. 2023 ("Large language models are not fair evaluators", arXiv 2305.17926, viés de posição); DynaBench (dados dinâmicos com humano no circuito contra saturação e sobreajuste de benchmarks estáticos).
