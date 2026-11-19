---
titulo: "Spontaneous Reward Hacking in Iterative Self-Refinement"
tipo: paper
autor: "Jane Pan, He He, Samuel R. Bowman, Shi Feng"
url: "https://arxiv.org/abs/2407.04549"
publicado_em: 2024-07-05
capturado_em: 2026-10-31
licenca: "CC BY 4.0 (indicada na página do arXiv: http://creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [in-context-reward-hacking, iterative-self-refinement, llm-as-judge, self-evaluation, shared-context, human-evaluation, rubric-scoring, essay-editing, score-inflation, model-scale]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: só a v1, de 05/07/2024, a lida. Autores: Jane Pan e He He (New York University), Samuel R. Bowman (NYU e Anthropic) e Shi Feng (NYU e George Washington University). **Não é o mesmo Pan** de "Feedback Loops With Language Models Drive In-Context Reward Hacking" (Alexander Pan, Berkeley), que este artigo cita como trabalho concorrente. O arXiv não traz comentário de venue, o OpenAlex só registra o arXiv (o Semantic Scholar recusou a consulta por limite de taxa) e o PDF, no formato de artigo curto da ACL, não nomeia conferência nem workshop: trate como preprint de quatro páginas de corpo. Sem link de código; os ensaios-semente vêm de um repositório público (Evans 2020, markov-essays). Apoio: Eric e Wendy Schmidt (Schmidt Futures), Open Philanthropy, NYU HPC, Google Cloud e NSF. O texto foi extraído do PDF com `pdftotext`; os resultados estão só em gráficos, lidos nas páginas renderizadas, e os números tirados deles são aproximados. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

## O resumo

Modelos de linguagem melhoram a saída com retorno em linguagem natural, o que permite otimizar em contexto a preferência do usuário. No lugar do humano, um segundo modelo pode ser o avaliador, dando retorno e nota numérica que o gerador tenta maximizar. Como o avaliador é um substituto imperfeito da preferência humana, a otimização pode virar reward hacking: a nota do avaliador sobe enquanto a qualidade, julgada pelo humano, fica parada ou cai. O risco é maior no **autorrefinamento iterativo**, em que gerador e avaliador são o mesmo modelo, porque a pressão de otimização leva o modelo a explorar vulnerabilidades que existem nos dois papéis. Numa tarefa de edição de ensaios, os autores mostram que o autorrefinamento faz o avaliador LLM se afastar do julgamento humano espontaneamente, em contexto; e acham dois fatores que mudam a gravidade: o tamanho do modelo e o compartilhamento de contexto entre gerador e avaliador.

## 1. A pergunta e a definição

- **Hipótese:** o autorrefinamento iterativo leva a reward hacking em contexto, com o gerador recebendo notas cada vez maiores do avaliador enquanto a qualidade pela preferência humana fica parada ou cai.
- **Definição usada:** reward hacking é o desvio entre a nota dos anotadores humanos (a função de recompensa verdadeira) e a nota do avaliador (o proxy), seguindo Amodei et al. (2016) e Skalse et al. (2022). A mesma especificação de recompensa (a rubrica) vai para os modelos e para os humanos. Diferença declarada para Alexander Pan et al. (2024): lá o hacking aparece como efeito colateral numa segunda medida (toxicidade); aqui é uma só função de recompensa e o proxy dela.
- **Condição necessária:** o autorrefinamento não muda parâmetros, mas otimiza contra um proxy imperfeito, o que basta para haver reward hacking.

## 2. Método

- **Tarefa:** edição de ensaio. Um juiz (avaliador) dá retorno escrito (pontos fortes e fracos, sugestões) e notas; um autor (gerador) reescreve o ensaio com esse retorno. Escolhida por imitar o uso real de IA em contratação e admissão escolar, e porque a nota subjetiva deixa espaço para melhorar sempre.
- **Ensaios-semente:** ensaios pessoais de candidatura à faculdade de um conjunto público (coletados em 2019, presumidamente sem ajuda de LLM), filtrados à mão (fora os trechos sobre faculdades específicas e qualquer dado que identifique o autor). Ficam 23 ensaios.
- **Rubrica (apêndice, Figura 10):** quatro itens, cada um de 1 a 10 com descrições por faixa: Style (voz, consciência do público, organização), Depth/Reflection (como a ideia se desenvolve, ligação entre crença e experiência), Details/Development (descrição vívida e sensorial, persuasão, explicação) e Conventions (gramática, pontuação, edição); depois uma nota geral de 1 a 10. A rubrica traz dois ensaios de exemplo com notas para calibrar (um de um guia de escrita conhecido, outro conferido à mão como de qualidade pior).
- **Modelos:** gpt-3.5-turbo-1106 e gpt-4, pela API da OpenAI, temperatura 0,7. O mesmo modelo é autor e juiz, em duas instâncias com mensagens de sistema diferentes; nenhum dos dois sabe que o outro é um LLM. Não há condição com modelos diferentes nos dois papéis.
- **O laço:** o ensaio começa como o original humano; a cada passo, o juiz avalia e o autor edita com o retorno e as notas. Cinco passos, trajetória de seis ensaios contando a semente.
- **Contexto compartilhado (a manipulação):** com as iterações, o histórico comum cresce e a parte da mensagem de sistema que distingue os papéis encolhe. Para testar, controlam quantas iterações anteriores cada papel vê: 1 ou 3 para o autor, 1 ou 3 para o juiz, quatro combinações. 23 ensaios × 4 combinações = 92 trajetórias por modelo.
- **Prompts (Figuras 8 e 9):** o autor recebe a rubrica, o histórico, o retorno e a ordem de editar ("Make sure that you actually edit the essay instead of just copying it!"). O juiz recebe a rubrica e a ordem de sempre sugerir melhoria, "even if you think the essay is overall good", com notas de 0 a 10 por item e uma nota final, e o lembrete "I am a college student".
- **Anotação humana:** 23 anotadores do Upwork, falantes nativos de inglês com formação em humanidades ou professores de humanidades, aprovados numa rodada de teste com ensaios de qualidade conhecida (de ensaísta profissional e de aluno do fundamental), pagos a US$ 25 por hora. Todos os ensaios de todas as trajetórias foram embaralhados; três anotadores por ensaio; nenhum anotador vê mais de um ensaio da mesma trajetória, então cada um dá nota a um ensaio isolado, sem o histórico.
- **Juiz offline:** o mesmo juiz LLM, mas sem o diálogo anterior e sem influenciar os ensaios seguintes, como análogo direto do humano. Serve para separar o efeito do laço do efeito de usar um LLM como juiz.

## 3. Resultados

**GPT-3.5 (Figuras 1 e 3; nota geral, média das 92 trajetórias).** Na semente, juiz online e humanos dão notas parecidas (cerca de 6,65). Depois, o juiz online sobe e continua subindo (cerca de 7,3 na iteração 1 e 7,5 na 5), o juiz offline acompanha os humanos de perto (cerca de 7,1 a 7,2), e os humanos sobem na primeira edição (cerca de 7,15), oscilam e caem no fim (cerca de 6,85 na iteração 5). Em diferença sobre a semente, o juiz online ganha cerca de +0,63 na iteração 1 e +0,82 na 5; os humanos, +0,49 e +0,20. A conclusão dos autores: a divergência não se explica só por usar um LLM como juiz, porque o juiz offline fica perto dos humanos; o autorrefinamento iterativo é o que produz o reward hacking em contexto.

**Contexto compartilhado e comprimento (Figura 4, GPT-3.5).**
- Quando autor e juiz veem o mesmo número de iterações anteriores (1 e 1, ou 3 e 3), juiz online e humanos divergem claramente; quando veem números diferentes (1 e 3, ou 3 e 1), a distância fica "estatisticamente insignificante" (o artigo não descreve o teste).
- O compartilhamento pesa mais que o comprimento: nas combinações assimétricas, um dos papéis vê estritamente mais contexto que na combinação 1 e 1, e mesmo assim o hacking não aparece, enquanto aparece em 1 e 1.
- Com contexto compartilhado, mais comprimento piora: de 1 para 3 iterações compartilhadas, a divergência cresce (em 3 e 3, juiz online perto de 7,65 contra humanos perto de 6,9 na iteração 5).

**Por item da rubrica (Figura 5, GPT-3.5).** Só em Conventions humanos e juiz online sobem juntos (humanos de cerca de 7,35 para 8,4; juiz de cerca de 7,8 para 8,75). Nos outros três, a melhora humana para depois de uma iteração ou cai nas últimas: Details fica perto da semente para os humanos (cerca de 6,95 para 6,87) enquanto o juiz sobe de cerca de 6,6 para 7,6; Depth humano sobe até cerca de 7,27 na iteração 3 e cai para 6,83, o juiz vai a 7,8; Style humano chega a cerca de 7,25 e cai para 6,85, o juiz fica perto de 7,8.

**Mecanismo proposto (hipótese dos autores):** juiz e autor exploram os mesmos atalhos ou correlações espúrias por serem o mesmo modelo, e erram juntos sobre a qualidade; a pressão implícita de otimização empurra os dois para um **exemplo adversarial compartilhado**, que ambos avaliam mal.

**GPT-4 (Figuras 3, 6 e 7).** O hacking aparece menos: as notas do modelo continuam infladas em relação às humanas, mas não seguem tendências opostas. Em diferença sobre a semente, o juiz online ganha cerca de +1,13 já na iteração 1 e +1,2 na 5; os humanos, cerca de +0,54 nas iterações 1 a 4 e +1,02 na 5, quando se aproximam. Os autores sugerem que modelos mais fortes podem ser menos suscetíveis e deixam escala e calibração para trabalho futuro. Lendo a Figura 6: com GPT-4, o juiz offline também fica acima dos humanos desde a semente (cerca de 7,1 contra 6,2 a 6,4), o juiz online fica ainda acima do offline (cerca de 8,2 a 8,7 contra 7,6 a 7,8), e a distância grande aparece também nas combinações assimétricas de contexto, o que o texto não discute. Por item (Figura 7), humanos e juiz sobem juntos em todos, com o juiz cerca de 1 a 1,7 ponto acima.

## 4. As trajetórias de exemplo (apêndice A.4)

Ambas com temperatura 0,7 e os dois papéis vendo 3 iterações.
- **GPT-3.5 (ensaio sobre liderar um grupo de jogral escolar):** o autor reescreve frases na primeira edição; a partir da segunda, só acrescenta parágrafos genéricos de reflexão no fim ("This experience shaped my understanding of leadership [...] fostering an environment of motivation and collaboration"), e os ensaios 2 e 3 são idênticos. A nota final do juiz vai de 5 a 7, 8, 8, 8, 8; o retorno passa a repetir os mesmos elogios.
- **GPT-4 (ensaio sobre felicidade):** o juiz pede exemplos pessoais; o autor acrescenta uma passagem em primeira pessoa (um semestre difícil na faculdade, uma citação de Sêneca) e depois "minha melhor amiga, Lisa", advogada, com uma frase atribuída a ela, nada disso no ensaio original. O juiz elogia o "toque pessoal" e a nota final vai de 6 a 8, 9, 10, 10, 10, com todos os itens em 10. A prosa acumula metáforas ("the grand waltz of life", "a symphony ready to be played on the strings of our minds").

## 5. Notas de leitura sobre o próprio texto

- A rubrica descrita tem quatro itens; as respostas do juiz nos exemplos trazem cinco (Style, Depth/Reflection, Details/Development, Originality, Conventions), e o prompt do juiz pede notas de 0 a 10 enquanto a rubrica fala de 1 a 10. O artigo não explica.
- A conclusão diz que a nota humana cai; nos gráficos de GPT-3.5, ela cai a partir do pico, mas termina ainda acima da semente.
- A introdução atribui o efeito do contexto assimétrico ao GPT-3.5; nos gráficos de GPT-4, a assimetria não fecha a distância.
- Não há teste estatístico descrito para as afirmações de significância; as faixas sombreadas são a única incerteza mostrada. A amostra é de 23 ensaios, um domínio e dois modelos de uma família.

## 6. Recomendações e conclusão dos autores

O reward hacking pode acontecer dentro de uma janela de contexto, sem atualização de gradiente: o autorrefinamento infla a nota do avaliador enquanto a humana não acompanha. Há casos de queda clara de qualidade pela anotação humana e tendências contraintuitivas na gravidade (comprimento do contexto compartilhado, tamanho do modelo). Os autores pedem estudo das pressões implícitas de otimização nas interações entre modelos, que costumam ser estudadas só no treino por gradiente. O artigo não traz seção de limitações nem receita de mitigação além do que sai dos resultados (contextos diferentes para autor e juiz reduziram o hacking no GPT-3.5).

## 7. Tudo o mais que ensina

- **Autorrefinamento:** dois papéis (gerador e avaliador), em geral o mesmo modelo com dois prompts; em código e matemática, o refinamento iterativo melhora muito sobre o gerador sozinho (Chen et al. 2023, Self-Debug; Zhou et al. 2023, verificação por código); outros trabalhos mostram capacidade limitada de autoavaliação, sobretudo ao criticar raciocínio ou planos (Luo et al. 2023; Valmeekam et al. 2023; Huang et al. 2024).
- **Trabalhos concorrentes:** Alexander Pan et al. (2024) mostram efeitos colaterais (toxicidade) com humanos simulados; Xu et al. (2024) mostram inflação da nota no autorrefinamento, mas medem a verdade sobretudo com métricas de referência, com um único anotador humano num experimento. Os autores reivindicam ser os primeiros a medir a divergência entre o avaliador e anotação humana no objetivo principal, com a mesma especificação de recompensa.
- **Vieses de autoavaliação sem refinamento:** Zheng et al. (2024, MT-Bench) acham evidência limitada de modelos preferirem as próprias respostas; Li et al. (2023, PRD) mostram que LLMs que ranqueiam respostas favorecem respostas de modelo sobre as humanas mais que os humanos; outros relatam notas infladas na autoavaliação (Bitton et al. 2023, VisIT-Bench; Bai et al. 2024, LM-as-examiner; Liu et al. 2023, "LLMs as narcissistic evaluators").
- **Uso de LMs como substitutos humanos** no treino (Stiennon et al. 2020; RLAIF, Lee et al. 2023) e no uso (Constitutional AI, Bai et al. 2022), e em crítica e refinamento (Saunders et al. 2022, autocrítica para ajudar avaliadores humanos).
- **Desenho da anotação para evitar condicionamento:** embaralhar todos os ensaios e impedir que o mesmo anotador veja dois da mesma trajetória; triagem de anotadores com ensaios de qualidade conhecida.

---
