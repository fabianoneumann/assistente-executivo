---
titulo: "Andrej Karpathy: Software Is Changing (Again)"
tipo: palestra
autor: "Andrej Karpathy (keynote no AI Startup School do Y Combinator, San Francisco)"
url: "https://www.youtube.com/watch?v=LCEmiRjPEtQ"
publicado_em: 2025-06-19
capturado_em: 2026-10-29
licenca: "licença padrão do YouTube (o vídeo não está marcado como Creative Commons, conferido pelo yt-dlp em 2026-10-29); tratado como protegido"
areas: [agent-engineering]
tags: [andrej-karpathy, software-3-0, human-in-the-loop, verification, verification-vs-generation, partial-autonomy, autonomy-slider, jagged-intelligence, agent-memory, prompt-injection, vibe-coding, llms-txt]
---

**Ficha de estudo**, em palavras próprias: a estrutura da fala com as marcas de tempo, as regras ensinadas com a ressalva de quem fala, poucas citações curtas conferidas na transcrição e "Tudo o mais que ensina". A transcrição e o deck ficaram na cópia de trabalho, fora do git.

# Andrej Karpathy: Software Is Changing (Again)

- Canal: Y Combinator (vídeo oficial). Keynote no AI Startup School, em San Francisco, para uma plateia que ele descreve como estudantes de graduação, mestrado e doutorado prestes a entrar na indústria.
- URL: https://www.youtube.com/watch?v=LCEmiRjPEtQ
- Data: a descrição do vídeo diz que a palestra foi em 17/06/2025; o slide de abertura diz "June 16"; o vídeo saiu em 19/06/2025.
- Duração: 39:31.
- Fonte da ficha: a transcrição automática do YouTube em inglês (não há legenda manual; as 19 outras línguas são traduções automáticas), baixada com `youtube_transcript_api`: 1.139 trechos, de 0:01 a 39:25, completa até o "Thank you" final. Conferida contra o deck oficial em Keynote que o próprio Karpathy disponibilizou (link do Google Drive na descrição do vídeo), cujo texto dos slides foi extraído para a cópia de trabalho. A transcrição automática erra nomes: "Andre Carpathy", "bite coding"/"vipcoded" (vibe coding), "guey" (GUI), "partial tunneling" (partial autonomy), "Enthropic", "entrograde amnesia", "Momento and 51st dates" (Memento e Como se fosse a primeira vez), "Menu Genen" (MenuGen), "Whimo" (Waymo), "Alexet" (AlexNet), "Tom Wolf" (Thomas Wolf), "Manon" (Manim), "Versell" (Vercel), "get ingest" (gitingest). Nas citações abaixo, os erros evidentes vão corrigidos entre colchetes.
- A descrição do vídeo traz capítulos e um resumo escrito pelo próprio Karpathy ("Thoughts (From Andrej Karpathy!)"), usados para conferir a estrutura.

## Estrutura da fala

Capítulos oficiais da descrição em negrito; o resto, marcas da transcrição.

- [0:00] **Intro.** O software mudou pouco em 70 anos e mudou duas vezes, rápido, nos últimos anos: há muito software a escrever e reescrever. Ele já tinha dado essa palestra; o problema é que o software continua mudando.
- [1:25] **Software evolution: From 1.0 to 3.0.** O mapa do GitHub; Software 1.0 (código), 2.0 (pesos de rede neural, Hugging Face como o "GitHub" do 2.0) e 3.0 (prompts que programam o LLM).
- [3:30] O exemplo da classificação de sentimento nos três paradigmas.
- [4:40] **Programming in English: Rise of Software 3.0.** O código no GitHub já mistura inglês; o tweet fixado dele sobre programar em inglês; o Autopilot da Tesla, em que o 2.0 "comeu" o 1.0; o 3.0 comendo a pilha agora; ser fluente nos três.
- [6:10] **LLMs as utilities, fabs, and operating systems.** "IA é a nova eletricidade" (Andrew Ng); LLM como serviço público, como fábrica de chips e, sobretudo, como sistema operacional.
- [11:04] **The new LLM OS and historical computing analogies.** Anos 1960: computação cara, centralizada, por tempo compartilhado; o chat como terminal; a inversão da difusão de tecnologia.
- [14:39] **Psychology of LLMs: People spirits and cognitive quirks.** Superpoderes (memória enciclopédica) e déficits cognitivos (alucinação, inteligência serrilhada, amnésia anterógrada, credulidade).
- [18:22] **Designing LLM apps with partial autonomy.** O Cursor e o Perplexity como exemplos; as quatro propriedades do app de LLM, entre elas a interface própria e o controle deslizante de autonomia.
- [21:30] Como fica todo software num mundo de autonomia parcial.
- [22:00] O laço de gerar e verificar: a IA gera, a pessoa verifica; acelerar a verificação e "manter a IA na coleira".
- [23:40] **The importance of human-AI collaboration loops.** Diffs pequenos, prompt concreto, o exemplo da educação (dois apps e o curso como artefato auditável).
- [26:00] **Lessons from Tesla Autopilot & autonomy sliders.** O painel do Autopilot como interface; a viagem perfeita no Waymo em 2013 e os 12 anos depois; "década dos agentes", não "ano dos agentes".
- [27:52] **The Iron Man analogy: Augmentation vs. agents.** Mais armaduras, menos robôs; produtos de autonomia parcial com o controle deslizante no produto.
- [29:06] **Vibe Coding: Everyone is now a programmer.** O tweet que virou meme; crianças fazendo vibe coding; o app de iOS e o MenuGen; o código foi a parte fácil.
- [33:39] **Building for agents: Future-ready digital infrastructure.** Um consumidor novo de informação digital; llms.txt, documentação em Markdown, trocar "clique" por comando, MCP, gitingest e DeepWiki; encontrar o LLM no meio do caminho.
- [38:14] **Summary: We're in the 1960s of LLMs, time to build.** Recapitulação e o controle deslizante indo da esquerda para a direita na próxima década.

## As três expressões: aparecem na fala, e onde

As três aparecem, ditas por ele e escritas nos slides. A marca é o início do trecho da transcrição em que a frase está (precisão de poucos segundos).

| Expressão | Na fala | No deck |
|---|---|---|
| "generation-verification loop" | [28:43] "this is done so that the generation verification loop of the human is very very fast". Antes, a ideia sem o nome: [22:18] a IA faz a geração e "we as humans are doing the verification", e "it is in our interest to make this loop go as fast as possible" | "Fast Generation - Verification loop" (slide de fecho da parte de autonomia) e "speed up the full generation-verification flow" (slide de recapitulação) |
| "keep (the) AI on the leash" | [22:56] "we have to keep the AI on the leash"; de novo em [23:30], [24:28], [25:09], [25:33] e [25:42] ("keeping the AI on leash") | "Keep AI "on a tight leash" to increase the probability of successful verification"; "Example: keeping agents on the leash" (programação assistida por IA e educação/LLM101n) |
| "autonomy slider" | [20:25] "what I call the autonomy slider"; de novo em [20:46], [21:17], [26:09], [28:15], [28:51], [28:55]; e, sem a palavra "autonomy", [39:12] "take the slider from left to right" | "Autonomy slider: Tab → Cmd+K → Cmd+L → Cmd+I (agent mode)" e "Autonomy slider" nas listas de propriedades |

A forma literal dita é "keep the AI on the leash"; "on a tight leash" está só no slide. "Generation verification loop" é dito uma vez, sem hífen na transcrição (o hífen está no slide de recapitulação).

## Regras ensinadas

**Três paradigmas de software**
- Software 1.0 é o código que se escreve para o computador; Software 2.0 são os pesos de uma rede neural, que não se escrevem: ajusta-se o conjunto de dados e roda-se um otimizador; Software 3.0 são os prompts, programas em inglês que programam o LLM. [1:30–3:30]
- O que mudou de fundo: até pouco tempo as redes eram computadores de função fixa (imagem para categoria, como a AlexNet); com os LLMs a rede ficou **programável**, e isso merece uma designação nova. [2:30–3:19]
- Quem entra na indústria deve ser fluente nos três, porque cada um tem prós e contras; cabe decidir, por funcionalidade, se é código explícito, rede treinada ou prompt, e transitar entre eles com fluidez. [5:32–6:00]
- Ressalva dele: ele mesmo diz que já tinha dado essa palestra e que o software "continua mudando".

**Os LLMs como "espíritos de pessoas"**
- O jeito como ele gosta de pensar os LLMs: "people spirits", simulações estocásticas de pessoas, em que o simulador é um transformer autorregressivo que gasta quase o mesmo compute em cada pedaço (token). Como foi ajustado a todo o texto da internet, tem uma "psicologia" emergente parecida com a humana. [14:50–15:30]
- É preciso pensar ao mesmo tempo nos superpoderes e nos déficits: como programar esses modelos contornando os déficits e aproveitando os superpoderes. [18:00]
- Os déficits que ele lista [16:06–17:32]: alucinam e inventam; têm autoconhecimento insuficiente ("melhorou, mas não é perfeito"); inteligência **serrilhada** (sobre-humanos em uns domínios, erros que nenhum humano comete, como achar 9.11 maior que 9.9 ou contar dois "r" em "strawberry"); **amnésia anterógrada** (não consolidam o que aprendem como um colega novo que dorme e volta sabendo mais; a janela de contexto é memória de trabalho e precisa ser programada diretamente); e são **crédulos**, sujeitos a injeção de prompt e a vazar dados.
- No slide, a síntese: "uma simulação com perdas de um savant com problemas cognitivos".

**Apps de autonomia parcial**
- Em vez de ir direto ao "sistema operacional" (copiar e colar código no ChatGPT), use um app dedicado. O Cursor tem a interface tradicional, para fazer tudo à mão, e a integração com o LLM, para ir em pedaços maiores. [18:29–19:31]
- As propriedades comuns aos bons apps de LLM [19:31–20:46]: (1) fazem muito do **gerenciamento de contexto**; (2) **orquestram várias chamadas de LLM** (no Cursor, modelos de embedding para os arquivos, modelos de chat, modelos que aplicam diffs); (3) têm uma **interface gráfica própria da aplicação**, porque texto é difícil de ler e interpretar e certas ações não deveriam ser digitadas (ver o diff em vermelho e verde, aceitar ou rejeitar com um atalho); (4) têm um **controle deslizante de autonomia**.
- A interface existe para a pessoa **auditar** o trabalho de sistemas falíveis e ir mais rápido. [20:15]
- O controle deslizante no Cursor: completar com Tab (você manda), Cmd+K (muda um trecho), Cmd+L (muda o arquivo), Cmd+I (o agente faz o que quiser no repositório). Você ajusta quanta autonomia cede conforme a complexidade da tarefa. [20:25–20:46]
- No Perplexity, o mesmo desenho: empacota informação, orquestra vários LLMs, tem interface para auditar (cita as fontes), e o controle vai da busca rápida à pesquisa e à pesquisa profunda que volta 10 minutos depois. [21:03–21:30]
- Muito software vai ficar parcialmente autônomo. As perguntas para quem mantém um produto: o LLM consegue ver tudo o que a pessoa vê? Agir de todos os jeitos que ela age? A pessoa consegue supervisionar e ficar no laço? Como é um diff no Photoshop? Os botões e chaves feitos para humanos vão ter de mudar. [21:30–22:00]
- Ressalva dele: "porque, de novo, são sistemas falíveis, ainda não perfeitos". [21:30]

**O laço de gerar e verificar**
- Na cooperação com a IA, em geral ela gera e a pessoa verifica; o interesse é fazer esse laço girar o mais rápido possível. Há dois jeitos principais. [22:00–22:30]
- **Primeiro: acelerar muito a verificação.** Interfaces gráficas são essenciais porque usam a "GPU de visão computacional" que temos na cabeça: ler texto cansa e não é divertido, olhar é divertido, uma "estrada" para o cérebro. Interfaces e representações visuais servem para auditar sistemas. [22:30–22:56]
- **Segundo: manter a IA na coleira.** Muita gente está empolgada demais com agentes; um diff de 10 mil linhas no repositório não serve, porque **a pessoa continua sendo o gargalo**: mesmo que as linhas saiam na hora, alguém tem de garantir que não há bug, que faz a coisa certa e que não há problema de segurança. A IA fica "reativa demais". [22:56–23:30]
- O jeito dele de trabalhar: medo de diffs grandes, pedaços pequenos e incrementais, uma coisa concreta de cada vez, para garantir que tudo está bom e girar o laço bem rápido. [23:59–24:04]
- **Prompt concreto aumenta a chance de a verificação passar.** Com prompt vago, a IA pode não fazer o que se queria, a verificação falha, você pede outra coisa e começa a girar em falso. Vale gastar um pouco mais de tempo sendo concreto no prompt. Ele tirou o exemplo de um post de boas práticas que leu (não diz qual). [24:28–25:00]
- O slide desse trecho traz o fluxo de programação assistida: descrever a próxima mudança concreta e incremental; não pedir código, pedir abordagens; escolher uma abordagem e rascunhar o código; revisar e aprender (documentação da API, pedir explicações); voltar atrás e tentar outra abordagem; testar; fazer o commit; pedir sugestões do que implementar a seguir; repetir. Outro slide numera os dois jeitos: "1. Make this EASY, FAST to win" e "2. Keep AI "on a tight leash" to increase the probability of successful verification".
- **Coleira na educação:** pedir "me ensine física" ao chat não funciona, a IA "se perde no mato". Ele separa em dois apps, um para o professor criar cursos e outro que serve os cursos aos alunos; no meio fica um artefato, o curso, que dá para **auditar**, garantir que está bom e consistente, e que mantém a IA presa a um programa e a uma progressão de projetos. Tem chance muito maior de funcionar. [25:00–25:45]
- Ressalva dele sobre a lista de técnicas: os fluxos de programação assistida estão "evoluindo muito rápido" (no slide) e cada um está desenvolvendo os seus jeitos. [24:04]

**O controle deslizante de autonomia, na Tesla e no Homem de Ferro**
- O Autopilot é um produto de autonomia parcial: o painel mostra o que a rede neural vê (a interface) e, ao longo dos cinco anos dele, o controle deslizante foi assumindo mais tarefas (manter a faixa, a distância, pegar bifurcações, parar em semáforo, fazer curvas, conforme o slide). [25:54–26:20]
- A lição da viagem no Waymo: em 2013 ele andou 30 minutos por Palo Alto sem nenhuma intervenção e achou que a direção autônoma era iminente; 12 anos depois ainda há teleoperação e pessoa no laço. Software é difícil como dirigir é difícil. [26:20–27:31]
- Por isso, "2025 é o ano dos agentes" o preocupa: é a **década** dos agentes; precisamos de pessoas no laço e de cuidado. [27:31–27:52] No slide: "Mind the demo-to-product gap"; uma demonstração é um `works.any()`, um produto é um `works.all()`; "2025-2035 is the decade of agents".
- A armadura do Homem de Ferro é ao mesmo tempo **aumento** (Tony Stark pilota) e **agente** (em alguns filmes voa sozinha). O controle deslizante vai de um ao outro; queremos um pouco dos dois, mas, com LLMs falíveis, agora é construir **armaduras, não robôs**: menos demonstrações chamativas de agentes autônomos, mais **produtos de autonomia parcial** com interface própria, para que o laço de gerar e verificar da pessoa seja muito rápido. [27:52–28:43]
- Sem perder de vista que em princípio dá para automatizar: o produto deve ter um controle deslizante de autonomia, e você deve pensar em como deslizá-lo para tornar o produto mais autônomo com o tempo. [28:43–29:01]

**Construir para agentes**
- Há um consumidor novo de informação digital: antes eram pessoas (por interfaces gráficas) e computadores (por APIs); agora, agentes, que são computadores mas parecidos com gente, "espíritos de pessoas" na internet. [33:31–34:02]
- Fale direto com o LLM: um `llms.txt` em Markdown dizendo do que trata o domínio, como o `robots.txt` orienta os robôs de busca; ler o HTML é sujeito a erro. [34:00–34:30]
- Documentação: Markdown é o fácil; o difícil é mudar o conteúdo. Toda instrução "clique" é ruim para o agente; a Vercel troca cada "clique" pelo comando `curl` equivalente. O MCP da Anthropic é outro protocolo para falar com agentes. [34:30–36:31]
- Ressalva dele: os LLMs já conseguem clicar, mas ainda é caro e mais difícil; vale encontrá-los no meio do caminho, e para a cauda longa de software que não vai se adaptar ferramentas de conversão continuam necessárias. Ele é otimista com as duas frentes. [37:30–38:14]

## Citações curtas

- [3:19] "your prompts are now programs that program the LLM"
- [14:50] "they're kind of like people spirits. Um they are [stochastic] simulations of people"
- [20:15] "a [GUI] allows a human to audit the work of these fallible systems and to go faster"
- [22:18] "usually they are doing the generation and we as humans are doing the verification"
- [22:56] "we have to keep the AI on the leash"
- [23:05] "I'm still the bottleneck, right?"
- [23:59] "I always go in small incremental chunks. I want to make sure that everything is good."
- [24:28] "spend a bit more time to be more concrete in your prompts which increases the probability of successful verification"
- [27:31] "this is the decade of agents ... We need humans in the loop. We need to do this carefully."
- [28:25] "it's less Iron Man robots and more Iron Man suits that you want to build"
- [28:43] "this is done so that the generation verification loop of the human is very very fast"
- [28:51] "there should be an autonomy slider in your product"

## O que a fala não trata

Não fala de bajulação, de LLM avaliando LLM, de debate entre modelos nem de conselho de modelos (o LLM Council é de novembro de 2025, cinco meses depois). "Orquestrar várias chamadas" é dividir o trabalho entre modelos com funções diferentes (embedding, chat, aplicar diff), não pôr modelos para revisar uns aos outros. A verificação de que ele fala é sempre a da pessoa.

## Tudo o mais que ensina

- **O mapa do software** [1:00–2:30]: o "Map of GitHub" como retrato de todo o código escrito; o "Model Atlas" como o equivalente para o 2.0, com os parâmetros do Flux no centro: cada ajuste fino sobre o Flux é como um commit que cria outro gerador de imagem.
- **Classificação de sentimento nos três paradigmas** [3:30]: escrever Python, treinar uma rede (no slide, 10 mil exemplos positivos e 10 mil negativos, codificação em bag of words, classificador binário) ou escrever um prompt com poucos exemplos.
- **O 2.0 comeu o 1.0 no Autopilot** [4:31–5:32]: muito C++ no começo; à medida que a rede crescia, o código ia sendo apagado (por exemplo, juntar informação entre câmeras e ao longo do tempo passou para a rede). Ele vê o 3.0 fazendo o mesmo com a pilha agora.
- **LLM como serviço público** [6:30–8:00]: o laboratório gasta capex para treinar (como construir a rede elétrica) e opex para servir por API, com cobrança medida por milhão de tokens; exigimos baixa latência, disponibilidade e qualidade constante; o OpenRouter é a "chave de transferência" entre fontes; como é software, dá para ter seis "fornecedores" sem disputa de espaço físico. Quando os modelos de ponta caem, há um "apagão de inteligência": o planeta fica mais burro, e quanto mais dependência, pior.
- **LLM como fábrica de chips** [8:00–9:00]: capex enorme, árvore tecnológica profunda, segredos de P&D centralizados nos laboratórios. A analogia embaralha porque software é maleável e menos defensável. Correspondências: um nó de 4 nm seria um cluster com certo teto de FLOPS; treinar em GPU da Nvidia é ser "fabless"; o Google com TPUs é como a Intel, dona da fábrica.
- **LLM como sistema operacional** [9:00–10:32]: a analogia mais forte. Não é commodity que sai da torneira, é ecossistema de software cada vez mais complexo; poucos fechados (como Windows e macOS) e uma alternativa aberta (o ecossistema Llama, talvez o "Linux"). O LLM é a CPU, a janela de contexto é a memória, e ele orquestra memória e compute para resolver problemas, com ferramentas e multimodalidade. Um app como o Cursor roda sobre GPT, Claude ou Gemini como o VS Code roda em Windows, Linux ou Mac. No slide: o espaço de prompt de sistema e de usuário lembra o espaço de kernel e de usuário da memória.
- **Anos 1960 da computação** [11:00–12:31]: compute caro força a centralização na nuvem; somos clientes finos, numa fatia do lote, por tempo compartilhado. A computação pessoal ainda não aconteceu; os Mac minis são uma pista, porque inferência com lote de um é limitada por memória. Conversar com o LLM em texto é como falar com o sistema operacional pelo terminal; a interface gráfica geral ainda não foi inventada.
- **A difusão invertida** [12:31–13:30]: eletricidade, criptografia, computação, aviação, internet e GPS começaram por governos e empresas; os LLMs começaram pelo consumidor ("como cozinhar um ovo"), e empresas e governos estão atrasados. O ChatGPT chegou a bilhões de pessoas da noite para o dia. Ele escreveu sobre isso em "Power to the people".
- **Memória de savant** [15:30–16:00]: o filme Rain Man (Dustin Hoffman decorando a lista telefônica) como imagem da memória enciclopédica; o LLM lembra até hashes SHA.
- **Amnésia no cinema** [17:01–17:32]: Amnésia (Memento) e Como se fosse a primeira vez (50 First Dates), protagonistas com "pesos fixos" e contexto apagado toda manhã; ele os recomenda para entender por que o LLM não aprende sozinho no trabalho.
- **Vibe coding** [29:06–31:02]: o inglês faz de todo mundo programador; antes eram 5 a 10 anos de estudo. Ele não sabe prever qual tweet viraliza; o de vibe coding era um "pensamento de chuveiro" e deu nome ao que todos sentiam. O vídeo de crianças fazendo vibe coding (compartilhado por Thomas Wolf, da Hugging Face) seria uma "porta de entrada" para o desenvolvimento de software; ele não é pessimista com a nova geração.
- **O código foi a parte fácil** [31:02–33:31]: fez um app de iOS em Swift sem saber Swift, em um dia. O MenuGen (fotografar o cardápio e gerar as imagens dos pratos) funcionou no laptop em poucas horas e levou uma semana para virar real: autenticação, pagamentos, domínio e deploy na Vercel, tudo clicando no navegador. Dá US$ 5 de crédito a cada cadastro e dá prejuízo. A documentação do Clerk para login com Google era uma lista de "vá a esta URL, clique aqui": um computador dizendo a ele o que fazer, quando o computador é que deveria fazer.
- **Manim pelo LLM** [35:01–35:30]: ele colou a documentação inteira da biblioteca de animação do 3Blue1Brown num LLM, descreveu o que queria e funcionou de primeira; documentação legível para LLM destrava muito uso.
- **Trocar a URL** [36:31–37:30]: gitingest (trocar github por gitingest na URL concatena os arquivos de um repositório num texto só, com a árvore de pastas) e DeepWiki (o Devin analisa o repositório e gera páginas de documentação) como ferramentas que tornam conteúdo acessível ao LLM só mudando o endereço.
- **Recapitulação** [38:14–39:31]: muito código a reescrever, por profissionais e por quem programa em inglês; LLMs como serviço público, fábrica e sobretudo sistema operacional, nos anos 1960; "espíritos de pessoas falíveis" com quem precisamos aprender a trabalhar, ajustando a infraestrutura; e, voltando ao Homem de Ferro, na próxima década o controle deslizante vai da esquerda para a direita.
