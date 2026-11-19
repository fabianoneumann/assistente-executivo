---
titulo: "2025 LLM Year in Review"
tipo: artigo
autor: "Andrej Karpathy"
url: "https://karpathy.bearblog.dev/year-in-review-2025/"
publicado_em: 2025-12-19
capturado_em: 2026-10-29
licenca: "nenhuma declarada (a página do Bear Blog só traz 'Powered by Bear' no rodapé, sem licença aberta, conferido em 2026-10-29); tratado como protegido"
areas: [agent-engineering]
tags: [andrej-karpathy, rlvr, verification, jagged-intelligence, benchmarks, partial-autonomy, autonomy-slider, human-in-the-loop, context-engineering, claude-code, vibe-coding, llm-council]
---

**Proveniência:** lido em 29/10/2026 no HTML do blog, na apuração. Data na página: 19/12/2025 (`datetime="2025-12-19T18:00Z"`). Cerca de 1.800 palavras: uma introdução, seis seções numeradas, um meme com legenda e um "TLDR". Ficha de estudo em palavras próprias, cobrindo o texto inteiro na ordem dele; o integral não entra porque o blog não tem licença aberta. Na página de pessoa: `knowledge/people/andrej-karpathy.md`.

## A pergunta

Quais foram, para ele, as "mudanças de paradigma" dos LLMs em 2025: as coisas que mudaram o cenário e chamaram a atenção dele no plano conceitual, de modo pessoal e "levemente surpreendente"?

## O texto, na ordem

### Introdução

2025 foi um ano forte e movimentado. A lista é pessoal: as mudanças que o marcaram conceitualmente, não um balanço do mercado.

### 1. RLVR (aprendizado por reforço com recompensas verificáveis)

- **A receita do início de 2025** em todos os laboratórios: pré-treino (GPT-2/3, por volta de 2020), ajuste supervisionado (InstructGPT, por volta de 2022) e RLHF (reforço com feedback humano, por volta de 2022). Receita estável e provada por um tempo.
- **O estágio novo:** em 2025 o RLVR virou o novo estágio principal. Treinando os LLMs contra recompensas verificáveis automaticamente em vários ambientes (quebra-cabeças de matemática e código), os modelos desenvolvem sozinhos estratégias que parecem "raciocínio" para nós: quebram o problema em cálculos intermediários e aprendem estratégias de ir e voltar até achar a solução (aponta o paper do DeepSeek R1 como exemplo). Isso seria muito difícil nos paradigmas anteriores, porque não se sabe como é o rastro ótimo de raciocínio para o modelo; ele precisa achar o que funciona para ele, pela otimização contra a recompensa.
- **Por que gastou o compute:** o ajuste supervisionado e o RLHF são estágios finos e curtos (ajustes pequenos em compute). O RLVR treina contra funções de recompensa objetivas, que ele chama de "não manipuláveis" (non-gameable), e isso permite otimizar por muito mais tempo. Deu muita capacidade por dólar e engoliu o compute que ia para o pré-treino. Resultado: o progresso de 2025 veio de os laboratórios consumirem a sobra desse estágio novo; os LLMs ficaram com tamanho parecido, mas com rodadas de RL muito mais longas.
- **O botão novo:** o RLVR trouxe um controle inédito, com lei de escala própria: capacidade em função do compute na hora do teste, gerando rastros de raciocínio mais longos ("tempo de pensar").
- **Marcos:** o o1 da OpenAI (fim de 2024) foi a primeira demonstração de um modelo RLVR; o o3 (início de 2025) foi o ponto de inflexão em que se sentia a diferença intuitivamente.

### 2. Fantasmas e animais / inteligência serrilhada

- **A forma da inteligência:** em 2025 ele (e, acha, a indústria) começou a internalizar de modo intuitivo a "forma" da inteligência do LLM. Não estamos "evoluindo animais", estamos "invocando fantasmas". Tudo na pilha do LLM é diferente (arquitetura, dados, algoritmo de treino e, sobretudo, a pressão de otimização), então não surpreende que saiam entidades muito diferentes, que não se devem pensar pela lente animal.
- **Pressão de otimização comparada:** em bits de supervisão, a rede neural humana foi otimizada para a sobrevivência da tribo na selva; a do LLM, para imitar texto humano, colher recompensa em quebra-cabeças de matemática e ganhar o voto de um humano no LM Arena.
- **Serrilhado:** como os domínios verificáveis permitem RLVR, os LLMs dão "picos" de capacidade perto desses domínios e têm desempenho serrilhado: são ao mesmo tempo um polímata genial e um aluno de primário confuso e com dificuldade cognitiva, a segundos de ser enganado por um jailbreak e vazar seus dados.
- **O meme:** a imagem mostra a inteligência humana em azul e a da IA em vermelho; a legenda diz que ele gosta dessa versão porque lembra que a inteligência humana também é serrilhada, do jeito dela (ele perdeu a referência do post original no X).
- **Perda de confiança em benchmarks:** em 2025 ele ficou apático e perdeu a confiança nos benchmarks. Motivo: benchmark é, quase por construção, um ambiente verificável, e por isso fica imediatamente exposto ao RLVR e a formas mais fracas dele, via dados sintéticos. No "benchmaxxing" típico, as equipes constroem ambientes vizinhos aos bolsões do espaço de embeddings ocupados pelos benchmarks e fazem crescer "pontas" que os cobrem. "Treinar no conjunto de teste" virou arte. A pergunta que ele deixa: como é ganhar todos os benchmarks e ainda assim não ter AGI?
- **Leituras dele sobre o tema:** "Animals vs. Ghosts", "Verifiability" (ficha em `2026-10-29-karpathy-verificabilidade.md`) e "The Space of Minds".

### 3. Cursor / uma camada nova de apps de LLM

- **O que o Cursor revelou:** além da ascensão rápida, o Cursor mostrou de forma convincente uma camada nova de "app de LLM"; as pessoas passaram a falar em "Cursor para X".
- **As quatro propriedades**, que ele diz ter destacado na palestra do Y Combinator (linka uma transcrição em donnamagi.com e o vídeo no YouTube; ficha em `2026-10-29-karpathy-software-is-changing-again.md`). Apps como o Cursor empacotam e orquestram chamadas de LLM para verticais específicas:
  1. fazem a "engenharia de contexto";
  2. **orquestram várias chamadas de LLM por baixo, encadeadas em grafos acíclicos (DAGs) cada vez mais complexos, equilibrando com cuidado desempenho e custo;**
  3. **dão uma interface gráfica própria da aplicação para a pessoa no laço** ("human in the loop");
  4. **oferecem um "controle deslizante de autonomia"** ("autonomy slider").
- **O debate do ano:** quão "grossa" é essa camada? Os laboratórios vão capturar todas as aplicações ou há espaço para os apps? A aposta pessoal dele: os laboratórios tendem a formar o "universitário geralmente capaz", e os apps vão organizar, ajustar e de fato animar equipes desses universitários como profissionais em verticais específicas, fornecendo dados privados, sensores, atuadores e laços de feedback.

### 4. Claude Code / IA que mora no seu computador

- **Primeira demonstração convincente de um agente:** o Claude Code foi, para ele, a primeira demonstração convincente do que é um agente de LLM: algo que, em laço, encadeia uso de ferramentas e raciocínio para resolver problemas longos.
- **Roda no seu computador**, com seu ambiente, dados e contexto privados. Ele acha que a OpenAI errou ao focar os primeiros esforços de Codex e agentes em contêineres na nuvem, orquestrados pelo ChatGPT, em vez de simplesmente o localhost. Enxames de agentes na nuvem parecem o "fim de jogo da AGI", mas vivemos num mundo intermediário, de decolagem lenta e capacidades serrilhadas, em que faz mais sentido rodar o agente direto no computador do desenvolvedor.
- **O que importa não é onde roda a "operação de IA"** (nuvem ou local), e sim todo o resto: o computador já existente e ligado, a instalação, o contexto, os dados, os segredos, a configuração e a interação de baixa latência. A Anthropic acertou essa ordem de prioridade e empacotou o Claude Code numa CLI mínima e agradável, que mudou o que é a IA: não um site que se visita, como o Google, mas um pequeno "espírito/fantasma" que "mora" no seu computador. Um paradigma novo de interação.

### 5. Vibe coding

- **O limiar:** 2025 foi o ano em que a IA passou do limiar de capacidade para construir programas impressionantes só em inglês, esquecendo que o código existe. Ele cunhou "vibe coding" num tweet "de chuveiro", sem imaginar o alcance.
- **Programação para todos:** com vibe coding, programar não é mais reservado a profissionais treinados. É mais um exemplo do que ele escreveu em "Power to the people: How LLMs flip the script on technology diffusion": ao contrário de toda tecnologia anterior, pessoas comuns ganham muito mais com LLMs do que profissionais, empresas e governos.
- **E para profissionais:** também deixa o profissional escrever muito mais software que nunca seria escrito. No nanochat, ele fez por vibe coding um tokenizador BPE próprio e eficiente em Rust, em vez de adotar biblioteca pronta ou aprender Rust naquele nível.
- **Onde o LLM Council aparece:** só aqui, como exemplo. Ele diz que fez por vibe coding vários projetos em 2025 como demonstrações rápidas de algo que queria que existisse, e lista menugen, **llm-council**, reader3 e HN time capsule (com link para cada repositório). Não há outra menção ao council no texto: nem método, nem resultado, nem recomendação de uso.
- **Código descartável:** ele fez apps efêmeros inteiros só para achar um bug, porque o código ficou de repente grátis, efêmero, maleável, descartável depois de um uso. O vibe coding vai "terraformar" o software e mudar descrições de cargo.

### 6. Nano banana / a interface gráfica do LLM

- **O modelo do ano em mudança de paradigma:** o Gemini Nano Banana, do Google, é para ele um dos modelos mais incríveis de 2025.
- **A analogia com a computação:** se LLMs são o próximo grande paradigma de computação, como os computadores dos anos 1970 e 80, virão inovações equivalentes pelas mesmas razões: computação pessoal, microcontroladores ("núcleo cognitivo"), internet (de agentes) e assim por diante.
- **Conversar é usar o console:** "conversar" com um LLM é como dar comandos num console dos anos 1980. Texto é o formato preferido do computador (e do LLM), não o das pessoas, sobretudo na entrada. As pessoas não gostam de ler texto: é lento e cansativo. Gostam de consumir informação visual e espacialmente, e por isso se inventou a interface gráfica. Do mesmo jeito, os LLMs deveriam falar conosco no nosso formato: imagens, infográficos, slides, quadros brancos, animações e vídeos, apps web. As versões iniciais são o emoji e o Markdown, jeitos de "vestir" o texto visualmente (títulos, negrito, itálico, listas, tabelas).
- **Quem vai construir a interface gráfica do LLM?** O Nano Banana é a primeira pista. O que importa nele não é só gerar imagem, e sim a capacidade conjunta de geração de texto, geração de imagem e conhecimento de mundo, emaranhados nos mesmos pesos.

### TLDR

2025 foi empolgante e levemente surpreendente. Os LLMs aparecem como um tipo novo de inteligência, ao mesmo tempo muito mais esperta e muito mais burra do que ele esperava. São extremamente úteis, e ele acha que a indústria não realizou nem 10% do potencial deles, mesmo na capacidade atual. Há muitas ideias para testar e o campo parece aberto. Repete o que disse no podcast do Dwarkesh: acredita ao mesmo tempo (paradoxo só na superfície) em progresso rápido e contínuo e em muito trabalho ainda por fazer.

## Regras e afirmações, com a ressalva dele

- **Verificável avança, o resto fica serrilhado:** a capacidade "dá picos" perto dos domínios com recompensa verificável; a ressalva é que a inteligência humana também é serrilhada, de outro jeito.
- **Benchmark não mede o que parece:** por ser verificável, o benchmark é alvo de otimização direta; desconfie de quem ganha todos.
- **Recompensa verificável é "não manipulável":** é a palavra dele para justificar por que o RLVR aguenta otimização longa; no mesmo texto, ele diz que os benchmarks, também verificáveis, são cercados por ambientes vizinhos ("training on the test set").
- **App de LLM = contexto + orquestração de várias chamadas + interface para a pessoa no laço + controle de autonomia.** A orquestração é descrita como DAG de chamadas, com troca entre desempenho e custo; não fala de chamadas que debatem ou se julgam.
- **Agente local antes de agente na nuvem**, enquanto as capacidades forem serrilhadas e a decolagem lenta (opinião dele, datada de 2025).
- **Texto é ruim para as pessoas lerem:** a saída do LLM deveria ser visual e espacial.

## Citações curtas

- "We're not "evolving/growing animals", we are "summoning ghosts"."
- "they are at the same time a genius polymath and a confused and cognitively challenged grade schooler"
- "Training on the test set is a new art form."
- "They provide an application-specific GUI for the human in the loop"
- "code is suddenly free, ephemeral, malleable, discardable after single use."
- "People actually dislike reading text - it is slow and effortful."

## O que o texto não trata

Não fala de bajulação, de LLM como juiz, de debate entre modelos, nem do desenho do LLM Council (que aparece só como nome numa lista de projetos de vibe coding). O "controle deslizante de autonomia" e a "pessoa no laço" aparecem só como propriedades listadas do app de LLM, sem o desenvolvimento que têm na palestra de junho.

## Tudo o mais que ensina

- **Cronologia da receita de treino:** pré-treino (2020), ajuste supervisionado e RLHF (2022), RLVR (2025); útil para explicar por que "raciocínio" virou produto em 2025.
- **Escala no teste:** pensar mais tempo virou um eixo de capacidade separado do tamanho do modelo.
- **"Cursor para X":** o formato de negócio que ele vê crescer é o app vertical que dá ao modelo dados privados, sensores, atuadores e laços de feedback.
- **Onde roda importa menos do que o contexto:** o valor do agente local está na máquina já configurada, com dados, segredos e baixa latência.
- **Vibe coding como ferramenta de profissional:** além de abrir a programação a leigos, serve para o profissional fazer o que nunca faria (o tokenizador em Rust) e para criar programas descartáveis, de uso único.
- **Sinal do próximo passo da interface:** emoji e Markdown são o começo; a interface gráfica do LLM ainda está por ser construída, e o modelo que gera texto e imagem com conhecimento de mundo é a primeira pista.
- **Posição no debate de progresso:** progresso rápido e muito trabalho por fazer não se contradizem, para ele.
