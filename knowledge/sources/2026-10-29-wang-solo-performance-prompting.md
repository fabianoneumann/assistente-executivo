---
titulo: "Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration"
tipo: paper
autor: "Zhenhailong Wang, Shaoguang Mao, Wenshan Wu, Tao Ge, Furu Wei, Heng Ji"
url: "https://arxiv.org/abs/2307.05300"
publicado_em: 2023-07-11
capturado_em: 2026-10-29
licenca: "arXiv non-exclusive license to distribute 1.0 (sem permissão de reuso); entra só a ficha de estudo"
areas: [agent-engineering]
tags: [persona-prompting, multi-agent-debate, single-agent, self-refine, hallucination, prompt-engineering]
---

Ficha de estudo extensa, em palavras próprias; a licença do arXiv (distribuição não exclusiva) não autoriza guardar o texto integral. arXiv: v1 em 11/07/2023, v4 (lida, no HTML do arXiv) em 26/03/2024. Comentário do arXiv: "Accepted as a main conference paper at NAACL 2024". Autores da University of Illinois Urbana-Champaign e da Microsoft Research Asia (os agradecimentos citam internos da MSRA). Código, dados e prompts em github.com/MikeWangWZHL/Solo-Performance-Prompting. Lido em 2026-10-29, incluindo os gráficos e as figuras com os prompts completos (os números das figuras vêm dos rótulos dos gráficos).

## A pergunta

Humanos resolvem melhor problemas complexos quando juntam mentes diferentes ("sinergia cognitiva"). Um único modelo de linguagem consegue fazer o mesmo, se dividindo em vários personagens que colaboram entre si, sem ferramenta, sem busca externa, sem ajuste fino e sem várias instâncias do modelo? E isso reduz a alucinação factual, que CoT e autocorreção não resolvem? O método se chama **Solo Performance Prompting (SPP)**.

## O ponto de partida

- Os autores separam dois tipos de dificuldade: tarefas que pedem muito conhecimento (onde o problema é a alucinação factual) e tarefas que pedem raciocínio em vários passos (onde falta o "pensar devagar").
- CoT e Self-Refine melhoram o raciocínio, mas não resolvem a alucinação; busca externa traz conhecimento, mas não melhora o raciocínio. O SPP quer atacar os dois.
- A inspiração declarada é o faz de conta no desenvolvimento infantil e trabalhos que mostram que dar uma persona ao modelo muda o comportamento e pode melhorar a resposta.
- Na comparação com métodos anteriores (Tabela 1 do paper), as limitações apontadas são: personas fixas ou específicas da tarefa (Camel fixa 2, GPT-Bargaining fixa 3), necessidade de ajuste fino (ExpertPrompting) e custo de várias instâncias de modelo. O SPP se apresenta como geral, puramente zero-shot (sem exemplos da tarefa avaliada), com número variável de personas identificadas dinamicamente, com refinamento iterativo e com um só modelo.

## O método, passo a passo

Tudo acontece numa única geração do modelo, a partir de um prompt fixo. Os autores dizem que uma iteração de Self-Refine exige três vezes mais inferências que o SPP.

1. **Identificação de personas.** Dada a tarefa, o modelo lista os participantes necessários, sempre incluindo um líder chamado "AI Assistant (you)". Uma persona pode ser especialista de domínio (fã de cinema, especialista em matemática) ou o público-alvo (uma criança de dez anos). Os autores deixam o modelo escolher as personas, em vez de defini-las à mão.
2. **Brainstorming.** Antes da primeira resposta, cada persona contribui com conhecimento e sugestões de como abordar a tarefa a partir da sua especialidade. Os autores dizem que essa etapa melhora a qualidade da solução inicial.
3. **Colaboração iterativa.** O AI Assistant propõe uma solução inicial, pede retorno a cada participante, que critica e sugere revisões; o ciclo se repete até todos ficarem satisfeitos. A resposta final é lida no formato pedido pelo usuário.

Formalmente, o prompt padrão produz a saída direto da entrada; o CoT gera passos intermediários; o SPP gera, nesta ordem, as personas, as falas de brainstorming e, para cada iteração, a solução do líder seguida do retorno de cada persona.

**Exemplo do paper (Figura 2):** escrever a história de fundo de um personagem para o próximo jogo de Zelda mencionando o encantamento do Patrono em Harry Potter, o personagem decapitado no nono episódio de Game of Thrones e a última música do segundo álbum de Jay Chou. O prompt padrão do GPT-4 esquece o encantamento e erra a música. Com SPP, o modelo cria Game Designer, Harry Potter Fan, Game of Thrones Fan e Jay Chou Fan; no brainstorming cada fã entrega o fato ("Expecto Patronum", Eddard Stark, "An Jing"), e na revisão cada um confere se o seu item entrou certo na história.

## O prompt

O mesmo prompt serve para qualquer tarefa, com três partes:

- **Princípio de sistema:** começar identificando os participantes que vão contribuir, depois iniciar uma colaboração em várias rodadas até chegar à solução final, com os participantes dando "critical comments and detailed suggestions whenever necessary".
- **Dois exemplos escritos à mão**, de tarefas que não se sobrepõem às avaliadas:
  - *Jogo do 24* (raciocínio), com só duas personas, AI Assistant e Math Expert. O líder propõe uma conta, o especialista confere passo a passo e aponta o erro; a segunda tentativa usa um número que não estava na entrada e o especialista aponta de novo; a terceira se aproxima e o especialista dá uma dica; só a quarta é aprovada. O exemplo mostra o crítico rejeitando várias vezes, com conferência explícita, antes de concordar.
  - *Poema* (conhecimento e restrições): sete versos cujas iniciais formam "CHATGPT", explicando computação quântica para uma criança de dez anos. Personas: AI Assistant, Poet, Computer Scientist e Ten year old child. O poeta lembra a restrição das iniciais, o cientista dá o conteúdo, a criança pede poucas palavras difíceis; depois do primeiro rascunho, poeta e cientista aprovam, mas a criança diz que não entende uma palavra ("perplex"), e o líder reescreve. O exemplo mostra o valor de dar uma persona ao público.
- **Prefixo da tarefa:** pede para identificar os participantes e resolver a tarefa colaborativamente passo a passo, seguido das instruções de formato e da entrada.

## Tarefas e métricas

- **Trivia Creative Writing** (nova, pede conhecimento): escrever uma história coerente que incorpore as respostas de N perguntas de trivia. Benchmark de 100 instâncias para N = 5 e 100 para N = 10, num total de mil perguntas tiradas do TriviaQA; as perguntas foram escolhidas entre as que um modelo pequeno (fastchat-t5-3b) errava, para desafiar o GPT-4; os temas vieram de uma lista de 100 substantivos de cultura pop gerada pelo GPT-4 e curada por humanos. Como julgar a qualidade da história é difícil até para humanos, a métrica mede alucinação: busca por texto, na saída, de qualquer forma aceita da resposta de cada pergunta; nota = respostas citadas corretamente sobre o número de perguntas.
- **Codenames Collaborative** (nova, conhecimento e raciocínio, inclusive teoria da mente): o mesmo modelo faz, em sequência, o Spymaster (dá uma palavra-dica ligada às palavras-alvo e que evite as distratoras) e o Guesser (adivinha as palavras-alvo a partir da dica e da lista completa). 50 instâncias montadas a partir do Codenames do BigBench. Métrica: sobreposição entre as palavras adivinhadas e as alvo, sem anotação humana.
- **Logic Grid Puzzle** (do BigBench, raciocínio puro): 200 quebra-cabeças de 2 a 5 casas com moradores e características; responder números de casa a partir das pistas. Métrica: acurácia.
- **Comparações:** prompt padrão, CoT (planejar ou listar passos antes da resposta, no estilo do Tree of Thoughts) e Self-Refine (retorno e refinamento conforme Madaan et al.; uma iteração).
- **Configuração:** GPT-4 pela API do Azure (versão 2023-3-15-preview), temperatura 0 e top_p 1. Cada método rodou duas vezes, com e sem a mensagem de sistema padrão ("You are an AI assistant that helps people find information"), e a Tabela 2 mostra a média das duas. Casos raros barrados pelo filtro de conteúdo da API foram excluídos.

## Resultados principais (GPT-4, Tabela 2)

| Método | Trivia N=5 | Trivia N=10 | Codenames | Logic Grid |
|---|---|---|---|---|
| Padrão | 74,6 | 77,0 | 75,4 | 57,7 |
| CoT | 67,1 (−10%) | 68,5 (−11,1%) | 72,7 (−3,6%) | 65,8 (+14,1%) |
| Self-Refine, antes de refinar | 73,8 | 76,3 | 75,2 | 58,8 |
| Self-Refine, 1 iteração | 73,9 (−1%) | 76,9 (−0,1%) | 64,6 (−14,6%) | 60,0 (+4%) |
| SPP | 79,9 (+7,1%) | 84,7 (+10%) | 79,0 (+4,8%) | 68,3 (+18,5%) |

As porcentagens são ganho relativo sobre o prompt padrão.

- **Trivia:** CoT fica abaixo do padrão; produz planos razoáveis, mas a história final ainda tem fatos errados. Self-Refine quase não muda. SPP supera todos, e o ganho cresce com mais domínios na mesma tarefa (10% com N = 10 contra 7% com N = 5).
- **Codenames:** CoT de novo não ajuda. Self-Refine piora bastante (de 75,2 para 64,6), porque tende a mudar a resposta inicial mesmo quando ela já estava boa. SPP sobe cerca de 5%.
- **Logic Grid:** aqui CoT ajuda muito (+14,1%), como a literatura já mostrava para raciocínio, e o SPP vai além (+18,5%).
- Os autores afirmam que o SPP é o primeiro método zero-shot de prompt que melhora conhecimento e raciocínio ao mesmo tempo no GPT-4.

**Estabilidade (Tabela 3, Trivia N = 5, três corridas):** padrão 74,4 ± 1,3; CoT 69,7 ± 1,0; SPP 80,2 ± 0,5. Mesmo com temperatura 0 o GPT-4 varia um pouco (cerca de 1%), e o SPP varia menos.

**Com e sem mensagem de sistema (Tabelas 5 a 7):** os padrões divergem por tarefa e método. SPP com e sem: Trivia N = 5 80,0 / 79,8; N = 10 85,2 / 84,2; Codenames 82,5 / 75,5; Logic Grid 66,3 / 70,4.

## Por que só aparece no GPT-4

Mesma tarefa, mesmo prompt, três modelos (Figura 6; GPT-3.5 com a melhor configuração de mensagem de sistema do SPP no GPT-4; Llama2-13b-chat com decodificação gulosa; valores padrão / CoT / SPP):

| Modelo | Trivia (média) | Codenames | Logic Grid |
|---|---|---|---|
| GPT-4 | 76 / 70 / 83 | 74 / 71 / 82 | 59 / 62 / 70 |
| GPT-3.5-turbo | 64 / 48 / 37 | 66 / 54 / 35 | 46 / 50 / 48 |
| Llama2-13b-chat | 46 / 28 / 4 | 0 / 18 / 1 | 4 / 26 / 0 |

(Os valores do GPT-4 nessa figura batem com a melhor das duas configurações de mensagem de sistema, não com a média da Tabela 2.)

- No GPT-3.5 o SPP fica abaixo do prompt padrão nas três tarefas, e muito abaixo nas duas que pedem conhecimento (37 contra 64 em Trivia, 35 contra 66 em Codenames). No Llama2 o SPP praticamente zera.
- A explicação dos autores: a sinergia cognitiva só se solta num modelo com capacidade de seguir instruções no nível do GPT-4. Fazem a analogia com crianças, que só começam a brincar de faz de conta por volta dos 2 a 3 anos (Piaget). Na figura do problema, dizem que forte capacidade de seguir instruções é pré-requisito para o SPP funcionar.
- **Término precoce (early-termination):** no Llama2, o modelo lista os participantes, escreve "Start collaboration!" e para, como se esperasse a fala de um usuário, em vez de seguir os exemplos e simular o diálogo sozinho. Nem instrução extra ("siga o mesmo procedimento dos exemplos, simule o diálogo") resolve.
- O paper não detalha o mecanismo da queda do GPT-3.5 além da diferença de capacidade.

## O que pesa: tipo, detalhe e número de personas

**As personas que o modelo escolhe acompanham a natureza da tarefa** (Figura 7a, nuvens de palavras): mesmo sem a expressão "quebra-cabeça lógico" na entrada, o modelo cria com frequência um "Logic Puzzle Expert". Em tarefas de conhecimento as personas são mais diversas e específicas (Film Expert, Movie Expert, Music Expert, Historian, Story Writer, Sports Expert, Harry Potter Fan, Tolkien Expert); em Codenames aparecem Psychologist, Language Expert, Linguist, Word Expert, Riddle Expert e até General Public; no Logic Grid são mais homogêneas (Logic Expert, Detective, Logic Puzzle Enthusiast, Neighbor).

**Personas dinâmicas e específicas contra personas fixas e genéricas** (Figura 7b, média das duas configurações; SPP / SPP-Profile / SPP-Fixed-Persona):

| Tarefa | SPP | SPP-Profile | SPP-Fixed-Persona |
|---|---|---|---|
| Trivia N=5 | 80 | 79 | 73 |
| Trivia N=10 | 85 | 83 | 76 |
| Codenames | 79 | 77 | 38 |
| Logic Grid | 68 | 65 | 64 |

- **SPP-Fixed-Persona** força só duas personas, "AI Assistant" e "Expert", com os mesmos exemplos reescritos para essas duas (o Expert acumula as falas do poeta, do cientista e da criança). Perde em todas as tarefas. Nos exemplos qualitativos, personas como "Film Expert" e "Sports Enthusiast" acertam a pergunta que o "Expert" genérico erra. Conclusão dos autores: personas dinâmicas e de grão fino rendem mais que personas fixas e gerais.
- A versão fixa também sofre de término precoce no GPT-4: começa a colaboração e para antes da resposta final. Tabela 4, casos de término precoce com e sem mensagem de sistema: Trivia N = 5 18/100 e 0/100; N = 10 16/100 e 1/100; Codenames 37/50 e 4/50; Logic Grid 11/200 e 15/200. Tirar a mensagem de sistema reduz muito o problema, mas não elimina; por isso a versão fixa marca 10,1 com mensagem de sistema e 66,0 sem, em Codenames. Com SPP, SPP-Profile, padrão e CoT no GPT-4 não houve término precoce.
- **SPP-Profile** gera, na identificação, um perfil detalhado de cada persona (como propõe o ExpertPrompting). Não supera o SPP: o nome de uma persona de grão fino, sem descrição, já parece bastar para trazer o conhecimento do domínio.

**Número de personas nos exemplos do prompt** (Figura 9): tirando o segundo exemplo (o do poema, com mais de duas personas) e deixando só o do jogo do 24 (duas personas), o desempenho cai pouco: Trivia N = 5 de 80 para 78, Codenames de 82 para 79, Logic Grid de 70 para 66. Os autores leem duas coisas: o exemplo com várias personas ajuda nas três tarefas, e o SPP é razoavelmente robusto a mudanças no prompt. O paper não varia diretamente quantas personas o modelo cria; esse número é decidido pelo modelo a cada tarefa.

**Número de perguntas na Trivia** (Figura 10): com uma pergunta só (N = 1), todos os métodos ficam parecidos, perto de 75 a 77; a partir de N = 5 o SPP se descola (cerca de 80 com N = 5 e 85 com N = 10, enquanto padrão e Self-Refine ficam perto de 75 a 78 e o CoT perto de 69 a 72). Embaralhar a ordem das perguntas quase não muda o resultado.

## Limites declarados

- Mesmo com persona de grão fino, a resposta pode sair errada; não está claro quanto uma persona realmente acrescenta de conhecimento num domínio. Pedem experimentos de diagnóstico e trabalho teórico para medir o efeito de ter ou não uma persona.
- O prompt é o mesmo, com os mesmos dois exemplos, para qualquer tarefa; escolher exemplos conforme a entrada poderia melhorar.
- Com orçamento suficiente, uma variante natural é passar para vários agentes de verdade: um líder identifica especialistas e forma um "gabinete" de agentes separados, com mais computação, mais memória local e interação mais flexível com humanos, o que eles julgam talvez essencial para aplicações reais.
- Implícitos no desenho: avaliação só em GPT-4 para a maior parte dos resultados, tarefas criadas pelos próprios autores em duas das três, métricas automáticas por busca de texto e sobreposição de palavras, e a coerência da história não avaliada.
