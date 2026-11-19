# Princípios de motion design para vídeo curto feito em código

O ofício do movimento para vídeo curto feito em código. A pergunta nasce de um caso comum: as correções de um primeiro Story em vídeo saem de ofício (o que se move, quando e como), não de ferramenta, e a base só tinha as ferramentas ([[video-como-codigo]]). Pesquisa rasa, nas três frentes, com uma variação em português. Fontes: [[2026-11-10-ibm-carbon-motion]], [[2026-11-10-material-1-duracao-e-easing]], [[2026-11-10-thompson-graphic-content-ahead]], [[2026-11-10-wikipedia-doze-principios-da-animacao]], [[2026-11-10-figma-principios-em-movimento]] e [[2026-11-10-remotion-easing-e-timings]].

**Um aviso sobre a origem dos números:** as durações com fonte primária são de sistemas de design de **interface** (Material, Carbon), feitas para transições que a pessoa vê muitas vezes por dia. Valem como referência de proporção (entrada contra saída, distância contra duração), não como o tempo de uma cena de vídeo, que precisa também do tempo de leitura ([[tempo-de-leitura-em-video]]). Nenhuma fonte aberta nesta pesquisa dá números próprios para vídeo explicativo vertical.

## Tempo e duração

- **Duração dinâmica, não fixa:** a duração cresce com a distância percorrida e com a mudança de tamanho; o que sai da tela pode ser mais curto, porque pede menos atenção ([[2026-11-10-material-1-duracao-e-easing]]; o Carbon usa uma escala não linear, para a percepção ficar igual em qualquer distância, [[2026-11-10-ibm-carbon-motion]]).
- **Os números de interface:** no celular, Material 1 dá cerca de 300 ms por transição, 375 ms para as de tela inteira, 225 ms para entrar e 195 ms para sair, e diz que acima de 400 ms pode parecer lento; o Carbon tem valores fixos de 70, 110, 150, 240, 400 e 700 ms, do microgesto ao escurecer de fundo.
- **Leitura do assistente:** a 30 quadros por segundo, 225 ms são cerca de 7 quadros e 400 ms, 12. Palavras que entram a 0,11 s cada (3,3 quadros) e caixas que se desenham em 0,35 s ficam dentro dessa ordem de grandeza. O que nenhuma fonte dá é quanto a cena fica parada depois.
- **Timing é sentido:** o número de quadros de uma ação vira a velocidade na tela e dá peso (um objeto leve reage mais rápido que um pesado), humor e reação ([[2026-11-10-wikipedia-doze-principios-da-animacao]], princípio 9); "ajustar poucos quadros muda a sensação" é também o primeiro dos oito princípios que Jake Bartlett ensina para motion design (citação: a página do curso dele, https://www.jakeinmotion.com/animation-principles-for-motion-designers).

## Aceleração e desaceleração (easing)

- **Linear parece mecânico** (Carbon; o glossário da equipe de motion da Figma chama de "linear demais", [[2026-11-10-figma-principios-em-movimento]]); o movimento natural acelera e freia, e por isso a animação clássica desenha mais quadros no começo e no fim da ação ("slow in and slow out", princípio 6).
- **As curvas de entrada, saída e padrão** (Carbon e Material): **entrada** desacelera (no Material, entra a toda velocidade e desacelera até parar; o Carbon dá a curva sem descrever o efeito); **saída** acelera (sai de vez); **padrão**, acelerar e frear, para o que está na tela do começo ao fim. O Material tem uma quarta, a **sharp**, simétrica, para o que sai mas pode voltar; o Carbon, para o mesmo caso, usa a curva padrão, como se o elemento descansasse logo fora da vista. As duas bibliotecas divergem nesse ponto.
- **Assimetria:** o movimento parece mais natural quando acelera e freia de forma assimétrica (Material). As curvas de referência em `cubic-bezier`: do Material, padrão `(0.4, 0, 0.2, 1)`, desaceleração `(0, 0, 0.2, 1)`, aceleração `(0.4, 0, 1, 1)` e sharp `(0.4, 0, 0.6, 1)`; do Carbon, entrada `(0, 0, 0.38, 0.9)` e saída `(0.2, 0, 1, 0.9)` no estilo produtivo, mais largas no expressivo.
- **Em código:** o Remotion tem `Easing.bezier(...)`, `in`, `out` e `inOut`, e `spring()` para movimento com física; uma transição de cena com `springTiming({damping: 200})` dura 23 quadros a 30 fps ([[2026-11-10-remotion-easing-e-timings]]). Um gravador que usa uma única curva suave (`u*u*(3-2u)`, simétrica) para tudo tem aí, pela leitura do assistente, o ponto mais barato a melhorar.

## Hierarquia, encenação e o movimento que não compete

- **Encenação (staging):** apresentar a ideia de forma completa e inequivocamente clara, mantendo o foco no relevante e evitando o detalhe desnecessário (Johnston e Thomas, princípio 3). Hill, da Figma, no mesmo sentido: ofício, intenção e **contenção**; Colby: movimento que não diz nada é um filtro por cima do design.
- **A ação secundária reforça, nunca compete:** se tirar a atenção da principal, sai (princípio 8). Exemplo típico: um objeto girando ao lado enquanto a frase principal entra.
- **Dois registros de movimento:** o produtivo, discreto, para quando a pessoa precisa entender, e o expressivo, muito visível, reservado para momentos ocasionais e importantes, como pausa rítmica (Carbon). Leitura do assistente: num vídeo explicativo, o expressivo é o momento da virada (o ✓, a resposta), e ele perde força se tudo for expressivo.
- **Primeiro isto, depois aquilo:** dividir a história em quadros, em vez de condensá-la numa imagem (Desmadrille, da Figma). A ordem em que as coisas se animam é a hierarquia (o passo "estabelecer a hierarquia de informação" do Carbon).
- **Não verificado:** o escalonamento por função (o principal primeiro, o rótulo depois, o detalhe por último, com 50 a 100 ms entre eles) e a atribuição dele a Ben Marriott e a Jake Bartlett vêm da resposta do Perplexity; a página de Bartlett só diz que a sobreposição escalona ações entre elementos.

## Continuidade e transições entre cenas

- **O vocabulário certo** ([[2026-11-10-thompson-graphic-content-ahead]]): "match" é só um elemento que passa de um plano ao outro; **continuidade** é espaço e tempo coerentes através do corte, para a história não se perder; os matches básicos da continuidade são de aparência, posição, ação (cortar no meio do mesmo movimento) e olhar. **Graphic match** (forma, cor ou posição repetidas entre planos diferentes) chama a atenção para si: pode sacudir (o osso e a nave de *2001*) ou ser prazer visual, mas não é a base da continuidade.
- **O match cut no ponto mais rápido:** acelerar, cortar seco no pico da velocidade e frear do outro lado parece uma transição sem emenda (Desmadrille, da Figma); as transições ligam os pontos da história e fazem vários casos parecerem uma experiência só.
- **Elementos contínuos guiam as transições grandes** (lista de avaliação do Carbon). Leitura do assistente: um objeto que encolhe para dentro de uma palavra e volta na cena seguinte é isso, e funciona; o que costuma falhar não é a continuidade, é o **sentido** do objeto (um ✓ que cai no que ainda não terminou).
- **Lacuna:** nenhuma fonte aberta trata de quando cortar seco e quando fazer transição num vídeo explicativo; o "corte para ideia nova, deslize para ideia ligada" veio da resposta do Perplexity, sem fonte aberta, e fica não verificado.

## Câmera virtual

Com fonte nesta pesquisa, só dois princípios gerais: a encenação inclui o ângulo e a posição da câmera (princípio 3), e o que percorre distância maior pede mais tempo (Material, Carbon). O que a pesquisa própria achou de câmera, paralaxe e profundidade está em [[ambiente-da-cena-em-video-por-codigo]], e a gramática da câmera ganhou síntese própria, [[linguagem-de-camera-virtual]] (os movimentos com nome, o eixo, as regras dos 30° e dos 20 mm, a câmera virtual da Pixar, o vertical, o tempo de plano por formato e a tradução de cada nome para o Three.js, o Blender, o Cinemachine e o Unreal).

Para o ofício, o que entra com fonte vem das referências da skill do HyperFrames, medidas nos filmes de lançamento dele e dadas como padrão que uma referência da pessoa derruba ([[2026-11-11-hyperframes-catalogo-camera-3d-e-traco-a-mao]]): movimento de câmera e de cor suaviza nos dois sentidos (`power2.inOut`); entre os movimentos contínuos que funcionam está "a slow orbit of a background stage (3–5° a second)"; e entre os padrões que soam gerados está "a slow creeping scale on a title or a slow push late in a scene". **Tensão com o item 12 abaixo:** a aproximação lenta de 100% a 105% ou 108% em 3 s, do Gemini sem fonte, é o empurrão que o `motion.md` diz soar gerado quando cai num título ou no fim de uma cena; o `film.md` do mesmo pacote, por outro lado, recomenda "one slow push from 1.0 to 1.08" sobre o vídeo num trecho calmo da música. Leitura do assistente: as duas frases se conciliam pelo alvo (o empurrão sobre imagem que se move ou sobre um cenário em camadas é outra coisa que a escala lenta sobre um título parado), mas isso não está escrito em nenhuma fonte, e o item 12 segue sem fonte.

## Som e tempo

O timing do movimento é parente do da música, e som e imagem juntos fazem mais que a soma (Colby e Hill, da Figma); a equipe deles vende a ideia de um movimento com efeito sonoro. O som está em [[desenho-de-som-para-video-curto]].

## Não verificado (sem fonte aberta)

A resposta do Gemini veio sem nenhuma citação. As afirmações, e o destino de cada uma:

1. O gancho visual nos primeiros 0,5 s (quadros 0 a 15) e uma "batida" visual a cada 1,5 a 2,5 s: uma leva dirigida à cadência de troca visual achou só blogs de ferramentas e criadores (2 a 3 s, 2 a 4 s, 8 a 12 s), sem método publicado: hipótese, não regra.
2. 30 quadros por segundo como padrão do vídeo vertical, 60 para simular interface: sem leva; convenção de mercado.
3. As durações por tipo de ação (microinteração de 100 a 200 ms, transição de elemento de 250 a 400 ms, de cena de 400 a 650 ms, a tela parada de no máximo 1,5 a 2,5 s): sem leva; as faixas de elemento batem em ordem de grandeza com as do Carbon e do Material, que são de interface, e o limite da tela parada contraria a régua de leitura de [[tempo-de-leitura-em-video]].
4. Os valores de influência do After Effects para cada curva: sem leva.
5. As curvas `cubic-bezier` de desaceleração `(0, 0, 0.2, 1)`, aceleração `(0.4, 0, 1, 1)` e padrão `(0.4, 0, 0.2, 1)`: **conferem** com o Material; as exponenciais e as de antecipação e ultrapassagem, sem leva.
6. O "pop" de escala (pico de 108% a 112% no quadro 8, assentando em 100% no 12): sem leva.
7. A área segura de 1080 por 1920 (de 100 a 980 px na horizontal, de 250 a 1300 px na vertical; 620 px de baixo livres): sem leva aqui; a base tem a área segura medida em [[carrossel-instagram]] (no Story orgânico, 20% livres embaixo, perto de 380 px; no Reels, 35%, perto de 670 px), e os 620 px do Gemini ficam perto do valor do Reels, não do Story.
8. O escalonamento de 2 a 4 quadros (60 a 120 ms) entre elementos e o atraso de 2 a 3 quadros do movimento secundário: sem leva; o Perplexity deu 50 a 100 ms (acima, também não verificado).
9. As transições verticais (empurrar para cima de 350 a 500 ms; o whip zoom de 200 a 300 ms com obturador de 180 a 270°; o morph de 400 a 600 ms): sem leva.
10. "Evitar corte seco sempre que possível" e manter um objeto âncora entre as cenas: sem leva; contraria o "corte para ideia nova" do Perplexity, também sem fonte.
11. As regras do match cut (centro dentro de um raio de 50 px; escala casada a 120%; morph de 250 a 350 ms): sem leva.
12. A aproximação lenta da câmera, de 100% a 105% ou 108% em 3 s: sem leva; em tensão com o `motion.md` do HyperFrames (acima, em "Câmera virtual").
13. Três planos de profundidade para o paralaxe, com os valores de Z e o desfoque do fundo de 10 a 25 px: sem leva.
14. O tremor de câmera com `wiggle(1.5, 5)`: sem leva.
15. O punch-in de 15% a 20% em 3 a 5 quadros na palavra de ênfase, parado 500 ms: sem leva.
16. A atribuição das recomendações à School of Motion, a Ben Marriott, à Motion Design School, ao Material 3 e ao Apple HIG: sem leva; a página de Bartlett e a do Material lidas não trazem esses números.

Das pesquisas de câmera ([[ambiente-da-cena-em-video-por-codigo]], [[linguagem-de-camera-virtual]]), dos números 12 a 15 só o 108% apareceu como alvo do empurrão lento (no `film.md`, "one slow push from 1.0 to 1.08", e no `push-in`, que vai a 1,08 no modo sutil), sem os 3 s do item 12 e sem nada dos itens 13 a 15. O que a base tem de medido sobre o começo do vídeo está em [[roteiro-em-formato-curto-o-que-e-medido]].

## Critérios para produzir e avaliar (leitura do assistente)

Para o roteiro, o gravador e a avaliação dos vídeos, a partir das fontes acima:

1. **Uma ideia em foco por cena;** o resto apoia ou sai (encenação; ação secundária).
2. **O movimento começa depois que a frase assenta,** salvo o que a própria frase descreve (ação secundária não compete).
3. **Entrada desacelera, saída acelera, nada linear** (exceto o que é mecânico de propósito, como uma engrenagem).
4. **Duração pela distância e pela importância;** saída mais curta que entrada.
5. **Ideia que continua leva um elemento através do corte** (o objeto que volta, o match no movimento). Que a ideia nova pode cortar seco é hipótese: veio do Perplexity sem fonte, e o Gemini, também sem fonte, diz o contrário.
6. **O símbolo cai no que ele significa:** o ✓ no que terminou, a seta para o que de fato causa.
7. **O expressivo é raro:** um momento de virada por vídeo.
8. **A mensagem se entende sem o movimento e sem o som** (alternativa estática do Carbon; o Story que se vê no mudo).

## Ver também

[[video-como-codigo]] (as ferramentas), [[roteiro-em-formato-curto-o-que-e-medido]] (o que é medido em formato curto), [[texto-que-cabe-e-legibilidade]] (texto em tela), `marketing/licoes.md` (as lições das peças).
