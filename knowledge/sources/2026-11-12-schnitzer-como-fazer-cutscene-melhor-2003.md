---
titulo: "How to Build a Better Cutscene"
tipo: artigo
autor: "Adam Schnitzer"   # linha "Author: by Adam Schnitzer" na página; o texto fala na primeira pessoa
url: "https://www.gamedeveloper.com/art/how-to-build-a-better-cutscene"
publicado_em: 2003-03-06   # data na página ("March 6, 2003") e datePublished do JSON-LD; o dateModified é 2023-11-20; publicado na Gamasutra, hoje Game Developer
capturado_em: 2026-11-12
licenca: "protegido (rodapé: 'Copyright © 2026 Informa' e, no topo, 'all copyright resides with them', sobre a Informa PLC; sem licença de conteúdo declarada); ficha de estudo em palavras próprias, sem o integral"
areas: [generative-media]
tags: [cutscene, game-cinematics, pixar, layout, previsualization, animatic, videomatic, animation-pipeline, staging, camera-movement, easing, film-editing, continuity, jump-cut, cutaway, shoeleather, production-cost]
---

# Schnitzer: a cutscene de jogo feita como animação de cinema, em quatro passos

Ficha de estudo: as seções seguem a ordem do artigo (a abertura, os quatro passos, a nota sobre técnica de câmera, o fecho e a bibliografia), com o método em listas e tabelas, os números no contexto em que o autor os dá e as ressalvas dele. Não há integral: o artigo é protegido.

**Proveniência.** Artigo de Adam Schnitzer na Gamasutra, hoje Game Developer, https://www.gamedeveloper.com/art/how-to-build-a-better-cutscene, datado de 06/03/2003 na página (com "34 Min Read" e as marcas "Art" e "Interviews" acima do título), baixado com curl em HTML em 2026-11-12 e lido no texto extraído (a cópia de trabalho `2026-11-12-linguagem-de-camera-virtual`), conferido no HTML para título, data e autor. O texto extraído é o do bloco `<main>`, que traz também o menu e as caixas de outras matérias do site; o sha256 do `protegidas.json`, (hash omitido), é o do texto desse bloco sem tags, script e estilo (refeito nesta ficha, igual). Wayback: `http://web.archive.org/web/20241108060914/https://www.gamedeveloper.com/art/how-to-build-a-better-cutscene`. Título conferido no `og:title` e no `headline` do JSON-LD. Cobertura: o artigo inteiro, do subtítulo à bibliografia; ficam fora o menu, as caixas de notícias e o rodapé. O artigo não tem imagens no corpo (as do HTML são de outras matérias e do site).

**Quem fala.** O autor, na primeira pessoa: diz ter trabalhado no jogo, na LucasArts, e no cinema, na Pixar, onde cita *A Bug's Life*, *Toy Story 2* e *Monsters, Inc.*; usa como exemplos dois projetos de jogo, *RTX Red Rock* e *Bounty Hunter* (este, encenado no prédio da LucasArts), sem dizer o cargo dele neles. O texto se refere a si mesmo como uma palestra ("my talk"), e a página o marca com "event-gdc", sem dizer de que edição.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). O `parafrase.py` contra o texto extraído do bloco `<main>` saiu com o código 3 (ficha em português, fonte em inglês): 100 unidades medidas (54 de prosa, 46 de célula com texto); fora da conta, 100 células de fato, 30 de cabeçalho e 19 frases curtas demais para medir; 0 colada de 100 (0%); 0 trecho de 3 ou mais seguidas. Pela conta lado a lado, sobre as mesmas 100 unidades, 85 seguem uma frase da fonte (traduzem, juntam duas ou fundem três ou mais seguidas): a de "Quem fala" e todas as do corpo, das seções da abertura ao fecho, menos uma; ficam fora as frases do formato, desta conferência e da proveniência, a da palestra, a nota sobre a ordem das funções e as três da lacuna. A maior sequência de unidades seguidas que seguem a fonte na ordem dela tem 17 (do passo 4, na frase sobre quem sabe desenho de cinema, às células da imitação da dolly): são o escopo do passo 4, as estratégias de transição e a técnica de câmera, método na ordem do artigo, como pede a ficha de estudo, e se declaram aqui; há outras de 14 (o layout e o começo do passo 3), 13 (as otimizações de modelo e de animação) e 10 (as técnicas de previs). No texto argumentativo (a tese da abertura, as funções da cutscene, o porquê da previs e da previs em 3D, a recomendação do passo 3, os prós e contras das duas cutscenes, a decisão de comprimir ou esticar, o argumento do passo 4 e o da técnica de câmera) não há três unidades seguidas que andem para a frente na fonte: a abertura põe os defeitos antes da tese; as funções vão em ordem própria; o porquê da previs vem depois dos números; no shoeleather, a decisão vem antes dos exemplos e a definição por último; no passo 4, a conclusão vem antes da premissa; e, na nota de câmera, a ressalva sobre a liberdade vai depois da tabela. Na revisão de 2026-11-19, três trechos foram refeitos: o layout do passo 2, que vertia em nove itens, frase a frase e na ordem, os parágrafos do artigo, virou prosa que abre pelo custo da revisão depois do layout, uma tabela que põe personagens e câmera lado a lado e um parágrafo que trata o ciclo do diretor antes das costuras; a tabela da nota de câmera abre pelo ease da Pixar e só depois dá a câmera pesada de onde ele vem; e a célula da mitologia abre pela cutscene. Nesses trechos, a sequência de 14 do layout deixou de existir: das 12 unidades novas, 7 ainda fundem frases da fonte (as quatro células da tabela do layout, as três da nota de câmera), sem três seguidas na ordem dela (a maior é de 2). Numa segunda rodada no mesmo dia, uma conferência independente apontou outros três trechos, que foram refeitos: os quatro itens de "Modelo e textura" viraram um parágrafo que abre pelo ganho no render e põe a textura antes da geometria; a tabela da animação passou a se organizar pelo que sai de cena, em outra ordem, com o critério da câmera subido para a frase de abertura; e a tabela das estratégias de transição do passo 4 agrupa as cinco em duas famílias, na ordem inversa à do artigo, com os dois sentidos numa frase antes dela. Nesses trechos, antes cerca de 23 de 25 unidades seguiam a fonte na ordem dela; depois, cerca de 7 de 23 ainda acompanham de perto uma frase dela, sem três seguidas na ordem do artigo (a maior é de 2), e as sequências de 17 e de 13 declaradas acima deixam de existir (revista em 2026-11-19).

## Abertura: o problema

Os seis defeitos que o autor diz ver:

1. cortes confusos ou desnecessários;
2. câmera hiperativa;
3. quebra das regras básicas de direção na tela;
4. planos que não contam o ponto da história;
5. descaso com a escolha de lente;
6. descuido com a continuidade.

A tese, como o autor a monta: a cutscene costuma falhar por ser feita sem a gramática da linguagem do filme; é essa gramática que rege plano, encenação, corte e ritmo, que na cutscene estão ali porque alguém os escolheu; e ela passa a valer porque, ao entrar na cutscene, o jogador troca a câmera contínua e decidida na hora pela estrutura de cinema.

| Ponto | Fato |
|---|---|
| Formas de cutscene citadas | animação pixelada dos fliperamas; produção com atores em fundo azul nos jogos de PC; animação 3D dos consoles |
| Crítica dos "puristas" | a cutscene distrai e invade o jogo |
| Excesso | jogos com cutscenes demais ou longas demais |
| Pior caso | cutscene tão confusa que seria melhor não ter |
| Formação do autor | jogo (LucasArts) e cinema (Pixar) |

## Passo 1: saber para que serve a cutscene

As sete funções vão aqui em ordem própria; no artigo, o marketing vem por último, como função secundária.

| Função | O que ela faz, pelo autor |
|---|---|
| Marketing, função secundária | nos 10 ou 15 segundos de atenção dos formadores de opinião na E3, alguns minutos de cutscene vistosa impressionam mais que gravação de jogo |
| Avançar a trama | casa a escalada do jogo (apostas maiores, envolvimento mais intenso) com a da história até o clímax, e dá outro nível de sentido à ação |
| Recompensar | pausa de puro entretenimento depois de uma tarefa difícil |
| Abrir e fechar a fase | no começo, prepara a ação; no fim, avisa que os objetivos foram cumpridos |
| Definir a mitologia | é na cutscene que a mitologia do jogo se mostra com mais força, e é ela que o jogador compra ou recusa; essa mitologia se faz das personagens, dos ambientes, dos objetos e do visual, mas sobretudo da história |
| Criar o clima | a cutscene pré-renderizada mostra como o mundo "seria" de fato, e o jogador passa a ver o mundo pobre do jogo através dessas imagens |
| Apresentar elementos e pistas | dá ao jogador o que ele precisa saber, como a história de fundo no filme; nos dois casos, "exposition" |

## Passo 2: previsualizar

### O pipeline da Pixar, como o autor o conheceu

Cutscene se faz como qualquer animação, e a ordem é a da Pixar nos três longas em que ele trabalhou:

1. Roteiro, desenho conceitual e storyboard, ao mesmo tempo (no cinema com atores, o roteiro vem antes do storyboard).
2. Animatic: a montagem junta os storyboards num story reel.
3. Modelagem: quando o estúdio decide fazer o filme, a modelagem constrói personagens e cenários do departamento de arte.
4. Voz: elenco e gravação.
5. Set dressing: os objetos montados nos cenários de cada cena.
6. Layout: cada plano do storyboard montado no mundo 3D, com personagens e cenários.
7. Animação.
8. Luz.
9. Render.
10. Efeitos.

| Ponto | Fato |
|---|---|
| O que ganha o diretor | vê o desenho de cinema do conjunto, separado da animação das personagens |
| Perguntas que a previs responde | encenação; posição da câmera; composição; se a sequência conta a história; se dá para encurtar; onde cortar; ritmo |
| Analogia do autor | animação é a apresentação no palco; previsualização é o ensaio |

| Medida, pelo autor | Valor |
|---|---|
| *RTX Red Rock*, num dia bom | 1 s de animação por hora, por animador |
| Por dia | 8 s |
| Por semana | 40 s por animador |
| Média semanal na Pixar | cerca de 12 s por animador |
| No tempo de um plano animado | o artista de layout passa por uma sequência inteira |

**Por que pagar pela previs.** Ela tira tempo e gente de outras frentes, e o autor responde que vale porque a animação é o trecho caro: o certo é ir do jeito mais rápido e barato de representar a história ao mais lento e caro, e descobrir na previs que um plano sobra custa muito menos do que descobrir depois de animado.

### As técnicas

O autor anuncia três técnicas além do storyboard (o animatic e o layout, do pipeline da Pixar, e o videomatic, tirado da ILM), mas as subseções numeradas são animatic, reunião de breakdown e videomatic, e o layout vem depois, sem número.

| Técnica | Como se faz | O que mostra ou resolve |
|---|---|---|
| Storyboard | quadros com as ações de cada cena | o que cada personagem faz e sente e como se relaciona com o entorno; não mostra o ritmo |
| Animatic | cada quadro escaneado, montado num editor digital em sincronia com um diálogo provisório, muitas vezes com música e efeitos | se os planos cortam bem, quanto a cena dura e se diverte naquele ritmo |
| Reunião de breakdown | todos os departamentos veem o animatic e perguntam; em geral depois do animatic, mas pode ser sobre um videomatic | cada um sai sabendo o que se espera dele e de acordo com o plano; ouvir as objeções cedo poupa trabalho e ressentimento |
| Videomatic | filmagem com câmera de vídeo, com a equipe de atores e o escritório de cenário; os planos aparados e montados depois | a duração de cada plano e de cada sequência, que planos funcionam e em que ordem |

| O videomatic de *Bounty Hunter* | Fato |
|---|---|
| Onde | no prédio da LucasArts |
| Elenco | gente da equipe de produção |
| Quem dirigiu | o diretor de animação, que decidiu câmera e marcação |
| Resultado | sequência com cada plano e cada duração cronometrados |

**Por que previsualizar em 3D.** Layout e videomatic atacam as duas perguntas de todo diretor: onde fica a câmera, e como as personagens se movem diante dela. No 3D, ângulo, movimento, tamanho de plano e lente, que mudam o efeito dramático, se testam antes de gastar animação, enquanto o storyboard privilegia atitude e ação, não a composição exata, e a distância entre o desenho 2D e o mundo 3D deixa margem para erro.

### O layout

O layout é o último ponto em que mudar sai barato: dali cada plano segue para a animação, onde qualquer revisão custa muito mais, e por isso o autor quer a estrutura de cinema da sequência inteira, com o tempo e o ritmo, decidida nele, sem quebra depois. Também por isso a etapa não se pula, com ou sem videomatic: além de previs, ela já é o começo da produção de cada plano, e para começar pede roteiro, storyboards, modelos das personagens, a voz e o cenário 3D.

| No layout | Personagens | Câmera |
|---|---|---|
| Acabamento | tosco de propósito: a marcação mais simples que dê conta da história | o oposto, acabada: ângulo, lente, tamanho de plano (close, plano médio, plano aberto) e movimento já pesados com cuidado |
| O que fica fixo para o animador | as marcas cronometradas com precisão que ele vai ter de acertar, como virar a cabeça, começar e parar de andar e os gestos de braço e mão | a câmera e a duração de cada plano, em que ele não toca e às quais se adapta; quando não consegue, pede a mudança, e o plano volta ao layout |

O layout anda em versões: o diretor olha cada montagem da sequência e devolve, e ela se refaz até os planos correrem um no outro e o tempo da cena ficar certo. O que mais se mexe entre uma versão e outra são as costuras, porque o mundo 3D raramente bate com o que o storyboard imaginava: um plano cai, outro entra, dois viram um só por um movimento de câmera, ou a cena inteira se encena de novo.

## Passo 3: otimizar

O terceiro passo é fazer o esforço da equipe aparecer na tela, sem gastar no que não importa; antes dele, a previs, que mostra o tamanho do esforço, serve para perguntar se há hardware, software, talento e tempo, e, se não houver, o autor sugere contratar um estúdio de cutscenes.

### No motor ou pré-renderizada

| | No motor do jogo | Pré-renderizada |
|---|---|---|
| O que é | em tempo real, com personagens e câmera roteirizados, sem gravação prévia | um pequeno filme, quadro a quadro, fora do motor |
| Cenário e detalhe | ditados pelo jogo; detalhe limitado pelo motor | cenário próprio, com maquete antes; o layout diz o que aparece em cada plano |
| A favor | começa na hora, sem carregar; reaproveita personagens, cenários, luz e efeitos do jogo; visual coerente no meio do jogo; mais fácil, sem pós-produção nem render de efeitos | nenhum tempo de programador; processo conhecido, mais controle do artista; visual melhor |
| Contra | o layout espera os níveis estarem prontos, o que aperta o cronograma; exige ferramentas de roteiro complexas, programação e conserto de bugs | — |
| O limite, pelo autor | o motor | o orçamento e o talento da equipe |
| Onde valem as otimizações a seguir | quase todas aqui não | quase todas aqui |

### Modelo e textura

A economia aparece no fim da linha: polígono e textura a menos poupam horas de quem modela e texturiza, mas é no render que o ganho pesa mais. Para chegar lá, o autor não se fia na lista de modelos, que sai do roteiro sem dizer quanto detalhe cada um merece, e sim na previs, que mostra quanto do modelo cabe no quadro e que partes voltam à tela mais vezes. Daí duas medidas. Na textura, nenhum 1024×1024 num objeto ao longe: o tamanho é o que a cena pede. Na geometria, o fundo pode ficar abaixo da resolução do primeiro plano e se apoiar em textura no lugar de modelagem, porque só se modela o que a câmera alcança.

### Animação

Cada tática abaixo tira alguma coisa de cena para poupar o recurso mais caro da produção, o tempo do animador; o autor quer esse cálculo já no storyboard e, mais ainda, no layout, e o princípio que as reúne é escolher onde pôr a câmera também pelo que ela deixa de mostrar do que é difícil de animar.

| O que sai de cena | Como | Onde o autor põe o limite |
|---|---|---|
| Uma personagem | no diálogo, fica no quadro só quem fala | quem apenas escuta também custa: a reação muda leva tempo de animação |
| Um evento | a batida de carro ou o tombo acontecem fora da tela, e o efeito sonoro com um plano de reação conta o que houve | — |
| Os pés | personagem andando entra enquadrada sem eles | o andar e o correr comuns podem já ter ciclo pronto; o pé num movimento especial fica sempre fora |
| A proximidade extrema | o close extremo se usa com cautela | de perto demais aparece o que o modelo tem de fraco: o low poly se desfaz, pele e cabelo ficam feios na textura, a sincronia labial incomoda |
| Um trecho de tempo | shoeleather: some a cobertura sem necessidade, como o trajeto da personagem de A a B | o difícil é saber o que é dispensável |

**O shoeleather, com os dois exemplos.** Comprimir o tempo ao essencial ou esticá-lo, mostrando a ação inteira, é escolha do diretor e do montador, e o autor guarda o esticar para os momentos dramáticos mais fortes. No exemplo da polícia, um carro freia diante do prédio e o plano seguinte já é a porta da sala arrombada: descer, entrar, atravessar o saguão, subir 12 andares e correr pelo corredor somem, e o público aceita a compressão porque a história anda. No suspense, a heroína que avança pelo corredor escuro até a porta precisa de cada passo, porque é nele que o público imagina o pior. O nome, pelo autor, nasceu para o trajeto de A a B e passou a valer para qualquer cobertura sem necessidade; ele abre o tópico com a frase "Art is life with all the boring parts taken out", sem dizer de quem é.

## Passo 4: aprender desenho de cinema

Para o autor, a cara fraca e amadora de tantas cutscenes vem de não conhecer as regras do desenho de cinema: cortes ruins, câmera ruim, erro de direção na tela e falta de continuidade, os defeitos da abertura, são problemas de concepção, e quanto mais ambiciosa a cutscene, mais ela pede quem saiba. Esse saber, num estúdio de animação, está com o artista de layout e o montador, não com o animador, que ele chama de ator, e é o que falta à empresa de jogo, que tem quase toda a equipe de um filme (conceito, modelagem, textura, animação, efeitos) mas não contrata esses dois, nem fotógrafos de cinema. O tema é grande demais para o artigo, que remete à bibliografia e se detém num caso só: entrar na cutscene e sair dela.

### Sair do jogo e voltar

| Ponto | Fato |
|---|---|
| As duas mudanças na entrada | a câmera passa do jogador ao designer; da ação contínua, sem corte, ao estilo de cinema, com cortes |
| Ferramentas do cinema para atravessar o corte | linha de eixo; direção na tela constante; corte na ação; "eyefix" |
| Meta | o corte que ninguém nota |
| O corte mais difícil | o do jogo para a cutscene |
| Por quê | o designer não sabe onde, nem em que pose, a personagem estará quando a cutscene disparar |
| O defeito | um salto ("pop") da posição no jogo para a da cutscene; no cinema, "jump cut" |

As saídas que o autor empresta do cinema servem igual na entrada da cutscene e na volta ao jogo, e cabem em duas famílias: a câmera que chega à ação por um desvio e o corte para outro ponto de vista.

| Família | Estratégia | Por que o salto passa | Exemplo do autor |
|---|---|---|---|
| Chegar por um desvio | Hand-off | a câmera acompanha um elemento qualquer e o troca pela personagem principal quando ela entra no quadro, ficando com ela daí em diante | o herói aparece depois de um menino de bicicleta cruzar a tela da esquerda para a direita |
| Chegar por um desvio | Lead-in | a cena não abre na ação, e sim numa vista neutra que leva até ela | a parede do prédio de onde a câmera de *NYPD Blue* desce até a rua |
| Outro ponto de vista | Cut-in | a personagem pode ter trocado de lugar enquanto ocupa a tela o close num detalhe já visto, num ponto que o designer conhece | — |
| Outro ponto de vista | Cutaway | um plano de fora da ação principal faz a ponte entre dois que não colariam direto | à mesa, para usar a primeira metade de uma tomada e a segunda de outra, o montador intercala o relógio, o gato na perna da cadeira ou as gotas no copo |
| Outro ponto de vista | Ângulo contrastante | o que entrega o salto é um primeiro plano de cutscene parecido com a câmera do jogo, e um ângulo bem diferente o disfarça | contraplano, close ou plano alto e aberto |

## Uma nota sobre técnica de câmera

A Pixar, diz o autor, imita o aparelho real para o público se sentir em casa, porque depois de milhares de horas de filme todo mundo sabe como uma câmera deve se mover.

| Ponto | Fato |
|---|---|
| O que a Pixar faz na câmera 3D | põe ease-in e ease-out de sobra na translação, para ela ter peso |
| De onde vem esse peso | da câmera grande e pesada do cinema real, que maquinistas empurram num carrinho (dolly) sobre trilhos: ela demora um instante a pegar velocidade e outro a parar |
| A mesma lógica, em outros movimentos | dolly, grua, pan, tilt e câmera na mão, todos copiados da sensação que têm no cinema com atores |

A liberdade da câmera de computação gráfica, sem as amarras do mundo físico, é para ele bênção e maldição: nada dá mais cara de "3D barato" que uma câmera voando a toda velocidade por toda parte, mas seria tolice não usar uma câmera sem volume e sem gravidade, desde que com o repertório do cinema, porque sem ele a câmera desorienta o público.

## Fecho e bibliografia

O artigo fecha repetindo os quatro passos, com a previs como o que permite o terceiro e o conhecimento de cinema também como o que resolve a passagem do jogo para a história.

| Autor | Título | Editora e edição | ISBN |
|---|---|---|---|
| Daniel Arijon | *The Grammar of the Film Language* | Silman-James Press, reimpressão, 1991 | 187950507X |
| Steven Katz | *Film Directing Shot by Shot: Visualizing from Concept to Screen* | Focal Press, 1991 | 0941188108 |
| Steven Katz | *Film Directing, Cinematic Motion: A Workshop for Staging Scenes* | Michael Wiese Productions, 1998 | 0941188140 |
| Joseph V. Mascelli | *The Five C's of Cinematography* | Silman-James Press, 1965 | 187950541X |
| Karel Reisz e Gavin Millar | *Technique of Film Editing* | Focal Press, 2ª edição, 1995 | 0240514378 |

## Citações

- "After Layout, when the shot goes to Animation, the camera is off limits to the animator."
- "Pixar's philosophy is to make the audience feel at home by mimicking the way that real world cameras move and operate."
- "Animators are actors, not cinematographers."

## Lacuna

O artigo não dá número de movimento de câmera (quanto dura o ease, que velocidade é demais), nem distâncias focais ou regras de lente, embora aponte o descaso com a lente como defeito. Não diz com que programas se fazia layout e previs, nem o custo ou o tempo de um animatic ou de um videomatic, e não explica o que a técnica da ILM tinha de diferente. É de 2003 e descreve a Pixar de *A Bug's Life* a *Monsters, Inc.*; não diz de que palestra saiu o texto, nem o papel do autor em *RTX Red Rock* e *Bounty Hunter*.
