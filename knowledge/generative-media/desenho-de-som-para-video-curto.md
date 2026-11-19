# Desenho de som para vídeo curto que ensina

O que a evidência diz sobre trilha e efeitos sonoros num vídeo curto que ensina, para quem gera o som por código e precisa escolher com fonte; a base tinha só o volume e a proporção música e voz de vídeo gravado ([[edicao-de-video-gravado]]). Pesquisa rasa nas três frentes, com uma variação em português. Fontes: [[2026-11-10-moreno-mayer-coerencia-sons-2000]], [[2026-11-10-vasilev-letra-de-musica-e-leitura-2023]] e [[2026-11-10-souza-barbosa-musica-com-letra-2023]].

## O que a evidência diz

- **Música de fundo numa explicação narrada atrapalha:** em dois experimentos com animações narradas (o raio, o freio hidráulico), quem ouviu um loop instrumental de fundo lembrou menos e resolveu menos problemas novos que quem ouviu só a narração; com música e sons juntos, pior ainda ([[2026-11-10-moreno-mayer-coerencia-sons-2000]]). A explicação dos autores: o material auditivo irrelevante disputa a memória de trabalho auditiva com a narração. A regra que sai daí, o princípio da coerência: só entra o estímulo relevante para o conteúdo.
- **Como o efeito sonoro se liga à imagem é hipótese dos autores, não achado:** no mesmo estudo, sete sons de ambiente, cada um tocado uma vez e ligado a um acontecimento da animação do raio (vento, condensação, trovão), **não** atrapalharam; dois sons mecânicos repetidos várias vezes em acontecimentos diferentes da animação do freio atrapalharam. Mas os dois experimentos diferem também na lição, no tipo de som e na duração (180 s tocados uma vez contra uma sequência de 9 s repetida), e os autores atribuem a diferença à coordenação dos sons **e à duração**, pedindo estudos que manipulem a coordenação diretamente. Eles dizem que quanto mais relevante e integrado o som, mais ajuda; mas, nos dois experimentos, nenhum grupo com sons foi melhor que o de só narração: no melhor caso, o som ligado ao acontecimento não atrapalhou.
- **Com texto na tela e sem voz, o que pesa é a letra da música:** numa meta-análise de 36 estudos, a música de fundo tem efeito pequeno de distração na compreensão de leitura (d = -0,19); separando, a música cantada distrai (d = -0,35) e a instrumental, efetivamente nada, segundo o resumo de [[2026-11-10-vasilev-letra-de-musica-e-leitura-2023]]. Nos quatro experimentos desse artigo, a instrumental não mudou ou acelerou um pouco a leitura, e a cantada a deixou mais lenta. Num estudo com estudantes da Universidade do Porto, a música com letra atrapalhou a compreensão de leitura e a memória (d de cerca de -0,3), e a instrumental (hip-hop lo-fi) não atrapalhou nem ajudou de forma confiável; só na compreensão de leitura tendeu, sem confiança estatística, a ajudar, e nas outras tarefas teve a mesma tendência negativa da cantada, menor. A recomendação dos autores: entre as duas, a instrumental; pelo desempenho, nem ela deve ser preferida ao silêncio ([[2026-11-10-souza-barbosa-musica-com-letra-2023]]). Os estudos de Vasilev são de leitura de parágrafos no ritmo de quem lê, não de vídeo animado.
- **Reconciliação (leitura do assistente):** os dois achados não brigam. Moreno e Mayer testaram música por baixo de **narração**, que usa o mesmo canal auditivo; os estudos de leitura testaram música por baixo de **texto**, e lá a instrumental passou. Para o vídeo sem voz, a trilha instrumental discreta não distrai a leitura nos estudos, mas não ganha do silêncio; e Brame, na síntese de roteiro, manda podar a música que não serve ao objetivo ([[roteiro-de-video-curto-e-curta-didatico]]). Se a trilha serve ao objetivo de uma peça (o clima, a marca) é a escolha que as fontes não tomam: manter a trilha instrumental é uma escolha de gosto legítima, desde que se teste sem ela quando for o caso. Quando a voz entra, vale o achado de Moreno e Mayer, porque a música passa a disputar o canal da narração; o nível da trilha sob a voz, o arranjo e o lugar dos efeitos estão em [[mixar-narracao-trilha-e-efeitos]].

## O silêncio e a hierarquia (só citação)

As diretrizes de som do Material Design, do Google, tratam o silêncio como escolha de projeto e pedem que cada som reflita a sua importância na hierarquia, limitando o som decorativo para não cansar; as páginas (`m2.material.io/design/sound/`) não abriram (nem pela Wayback, que só guardou a casca), e o que está aqui vem do resumo da busca, sem conferência.

## Quanto se ouve

Quanto dos Reels e dos Stories se vê com som não tem primária aberta: os números que circulam (60%, 80%, 85%) vêm de blogs que os atribuem à Meta e são de Reels vistos **com** som, ou seja, apontam maioria com som nos Reels; não verificados. Mesmo assim, de 15% a 40% sem som é uma parte grande, e a regra que a base já registra ([[stories-o-que-evitar]], item 8) continua: o vídeo tem de se entender mudo, e o som acrescenta.

## O que isso muda num gerador de som por código (leitura do assistente)

Um gerador de som de cena típico, pelas fontes acima:

| Costume | Pela evidência | O que mudar |
|---|---|---|
| Trilha instrumental suave, sem voz cantada | instrumental por baixo de texto não distrai, mas não ganha do silêncio; cantada distrai | nunca trilha com letra por baixo de texto; a instrumental pode ficar, com um teste sem trilha quando for o caso |
| Um "pop" para cada quadro que entra (vários em 2 s), um "tique" para cada etiqueta | som repetido e ligado a acontecimentos diferentes atrapalhou; som um a um com um acontecimento, não | som só nos acontecimentos de sentido (o ✓, a trava numa data, a lista que muda); a sequência de quadros pode levar um som só, ou nenhum |
| "Escrita" a cada frase | um som que se repete em toda cena é o caso intrusivo | testar sem, ou só na primeira frase, para marcar o gesto |
| Volume final pela referência da base | já é a régua (-14,5 LUFS, pico real de -2 dB) | manter |

## Critérios para produzir e avaliar (leitura do assistente)

1. **Cada efeito tem um acontecimento de sentido e toca uma vez;** sequência repetida em acontecimentos diferentes sai.
2. **Trilha por baixo de texto: instrumental, discreta, sem letra;** o silêncio é pelo menos tão bom para a leitura, e o teste sem trilha é o jeito de saber se ela rende nos vídeos do projeto.
3. **Com voz:** música abaixo da voz e mais baixa durante a fala; a medida de preferência põe a narração sobre música entre 10 e 15 LU durante a fala, e os 20 dB mais 3 de [[edicao-de-video-gravado]] são de um editor, para a voz dele; o nível, o arranjo sob a fala e o lugar dos efeitos estão em [[mixar-narracao-trilha-e-efeitos]].
4. **O vídeo se entende sem som;** o som reforça o que já está na tela.
5. **Na dúvida, menos:** o acréscimo de som "para ficar profissional" foi exatamente o que Moreno e Mayer testaram, e prejudicou.

## Lacunas

Nenhuma fonte desta rodada mede efeito sonoro em vídeo curto de rede social, retenção com e sem trilha num Reel, nem o nível ideal da trilha sem voz em relação aos efeitos. A sincronização de efeito com movimento (o som que dá peso ao gesto) aparece só em cursos e blogs, sem método.

## Ver também

[[principios-de-motion-design]] (o expressivo é raro, vale para o som), [[tempo-de-leitura-em-video]] (o texto que o som não pode atrapalhar), [[edicao-de-video-gravado]] (volume e voz), [[stories-o-que-evitar]] (item 8, vídeo sem som).
