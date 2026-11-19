---
titulo: "O papel do Product Owner em 15 minutos (versão em português de \"Agile Product Ownership in a Nutshell\"): a folha desenhada enquanto a voz explica, os cortes e o zoom out final"
tipo: video
autor: "Henrik Kniberg (vídeo original); versão em português de Eduardo Borges (canal Eduardo Borges, @epborges, YouTube)"
url: "https://youtu.be/7lhnYbmovb4"
publicado_em: 2013-08-02
capturado_em: 2026-11-13
licenca: "todos os direitos reservados (vídeo comum do YouTube; os metadados não trazem licença aberta)"
areas: [generative-media]
tags: [whiteboard-animation, hand-drawn, drawing-while-talking, explainer, big-canvas, camera-moves, hard-cut, zoom-out, speech-drawing-sync, stroke-reveal, pen-cursor, pacing, dubbing, digital-drawing]
---

**Proveniência:** vídeo trazido por curadoria em 13/11/2026, "para estudar o desenho que vai acontecendo, os cortes e o zoom out final que mostra o mapa inteiro", com vistas ao formato da folha desenhada enquanto se fala. A descrição do vídeo diz que é a versão em português do vídeo de Henrik Kniberg, traduzida por Eduardo Borges com autorização do autor, e aponta o original (https://www.youtube.com/watch?v=502ILHjX9EE). Que o original é de 2012 vem do blog do autor, não do vídeo: o post "Agile Product Ownership in a nutshell", de 25/10/2012 (https://blog.crisp.se/2012/10/25/henrikkniberg/agile-product-ownership-in-a-nutshell). Coleta e medidas de 13/11/2026: metadados pelo yt-dlp; vídeo em 360p (640 por 360, 30 quadros por segundo; o YouTube não oferece 480p deste vídeo, só 144p, 360p e 720p); transcrição local com faster-whisper `small`, sem revisão, com o tempo de cada palavra (erra nomes próprios e alguns termos; os tempos por palavra têm erro de alguns décimos de segundo); mudança de cena pelo ffmpeg em todos os quadros, conferida olhando o quadro antes e depois de cada mudança; quantidade de tinta na imagem medida a 10 quadros por segundo (as regras das duas contas estão abaixo, em "O método das contas"); quadros lidos a cada 0,5 s nos trechos de sincronia, a cada 1/30 s no zoom final, e um a cada 25 s no vídeo inteiro. A transcrição tem uma voz só. Ficha de estudo em palavras próprias, centrada na forma (desenho, fala, cortes, mapa final, material); o assunto do vídeo entra só para situar; o integral não entra porque o vídeo não tem licença aberta.

**A condição de todas as medidas:** a voz é a da dublagem, posta sobre a imagem do original. A sincronia medida aqui é entre o desenho do original e a voz em português.

**O método das contas:** **Os reenquadramentos** saem do `reenquadramentos.py`, de 12 a 951,6 s: a nota de cena do ffmpeg em todos os quadros; um bloco é uma sequência de quadros acima de 0,012, com até 3 quadros calmos no meio, e conta se o pico passa de 0,03; o bloco que começa a menos de 0,5 s do fim de um reenquadramento é o resto dele (a imagem assentando) e não conta; com 8 quadros ou mais é movimento de câmera, com menos é corte seco. Só com o limiar de 0,02 e a mesma tolerância saem 47 blocos: a diferença para os 33 são a abertura, o fecho e restos como 8:33,07, 9:18,60, 11:25,70, 12:42,67, 14:37,50, 15:02,03, 15:11,03, 15:11,23 e 15:23,87. **O ritmo** sai do `ritmo_do_desenho.py`, de 12 a 951 s, com o vídeo em cinza a 320 por 180 e 10 quadros por segundo: a imagem mexe quando a diferença média para o quadro anterior passa de 0,08; os quadros a menos de 0,8 s de um reenquadramento saem da conta; pausa é um trecho de 2 s ou mais sem mexer. Sai também do "mexendo" o pico isolado (um quadro acima de 0,08 entre dois abaixo) que cai num quadro-chave do arquivo (um a cada 5,833 s, mais os que o codificador põe nos cortes; a lista sai do próprio vídeo, pelo `ffmpeg -skip_frame nokey`): nesse quadro a imagem inteira muda um pouco sem traço novo (diferença mediana de 0,47, com a tinta mudando 6 px), e, contado como mexendo, ele parte as pausas longas em pedaços de uns 5,8 s; foram 65 picos tirados. A fala conta cada trecho da transcrição inteiro, do começo ao fim, com as pausas de dentro, e por isso sai um pouco maior que a fala de fato.

## Ficha

| Campo | Valor (coleta de 13/11/2026) |
|---|---|
| Formato | vídeo horizontal (16:9), 16:02 (962 s) |
| Publicado | 02/08/2013, no canal Eduardo Borges |
| Números | 162.887 visualizações, 7.099 curtidas, 134 comentários |
| Categoria e etiquetas | Ciência e tecnologia; Scrum, Agile, Product Owner, Product Management, XP, Kanban |
| Assunto | o papel do dono do produto num time de desenvolvimento ágil, explicado por um mapa que se desenha |
| Fala | 3.131 palavras entre 0:05,1 e 15:55,6, cerca de 3,3 por segundo (perto de 198 por minuto), pela transcrição sem revisão |

## A estrutura do vídeo

| Tempo | O que acontece na tela |
|---|---|
| 0:00 a 0:00,27 | preto |
| 0:00,27 a 0:11,5 | cartão de título, também escrito à mão; a fala começa em 0:05,1 |
| 0:11,5 | corte para a folha em branco |
| 0:11,5 a cerca de 8:00 | o ciclo central se monta, com planos longos (de 0:56,7 a 3:40,5, 164 s sem a câmera mexer) |
| cerca de 8:00 a 15:51,7 | os assuntos seguintes ocupam papel vazio ao lado do ciclo, com a câmera indo e voltando entre as regiões |
| 15:51,7 a 15:52,2 | zoom out até a folha inteira |
| 15:52,2 a 15:57,9 | a folha inteira parada |
| 15:57,9 | escurece para o preto; créditos em letra de computador até o fim |

## Desenho e fala

**O padrão observado:** a frase apresenta o elemento com um "esse aqui" e o desenho da figura começa junto com ela; a palavra escrita que rotula a figura chega depois de a palavra ser dita, de meio segundo a pouco mais de três segundos; em seguida a caneta para, e a voz segue desenvolvendo a ideia sem traço novo. O que se desenha é a frase que abre cada bloco, não a explicação que vem depois.

Casos medidos (o tempo da palavra pela transcrição; o do desenho pelos quadros a cada 0,5 s):

| Elemento | Fala | Desenho | Distância |
|---|---|---|---|
| A personagem (boneco) | a frase que a apresenta começa em 11,8 s | corte para a folha em branco em 11,53 s; boneco de 12,0 a 13,0 s | corte 0,27 s antes da frase; boneco durante ela |
| Rótulo "PO" | "Owner" em 13,5 s | escrito de 13,5 a 14,0 s | de 0 a 0,5 s depois |
| Balão "Vision" | "visão" em 14,8 s | brilho verde de 15,0 a 15,5 s; balão de 16,0 a 16,5 s; a palavra de 17,0 a 18,5 s | de 2 a 3,5 s depois |
| Pausa | a voz desenvolve a ideia de 16,3 a 24,5 s | a caneta para ao lado do desenho de 18,4 a 24,6 s | 6,2 s sem traço |
| Interessados (três bonecos) | "stakeholders" em 26,3 s | reenquadramento seco em 25,30 s; bonecos de 25,5 a 27,5 s; a palavra escrita de 28,0 a 29,7 s | corte 0,4 s antes da frase; palavra escrita de 1,7 a 3,4 s depois da dita |
| Cartões ao longo do arco | a frase sobre entregas frequentes, de 66,4 a 67,6 s | cartõezinhos um a um, de 66,5 a 70 s, de 0,5 a 1 s cada | junto |
| "4-6" | "4 a 6" em 68,8 s | escrito por volta de 73,5 a 74,5 s, depois de a caneta terminar a saída do time | cerca de 5 s depois |
| Chave sobre o funil e "6 months!" | "6 meses" dito duas vezes: em 210,7 s, no tamanho da lista de pedidos, e em 217,0 s | chave azul sobre o funil de cerca de 210,2 a 212,5 s; "6 months" escrito de cerca de 213,3 a 217,5 s | chave durante a primeira menção; o rótulo começa uns 2,6 s depois dela e termina perto da segunda |
| Lixeira | a recusa, de 223,4 a 223,6 s | logo depois de um corte para perto (220,53 s), lixeira de 222,5 a 224,5 s | junto |
| Gráfico novo | a frase que o introduz começa em 512,3 s | a câmera viaja para papel em branco de 511,57 a 512,03 s; o eixo começa em 512,4 s | a câmera chega 0,25 s antes da frase |

**O vocabulário desenhado:** bonecos de palito com uma auréola suave de cor atrás (verde nas pessoas); balões de fala; palavras soltas como rótulo, uma ou duas, em inglês; números curtos ("4-6", "10", "WIP Limit = 5"); setas grossas fechando um ciclo; cartões retangulares preenchidos de azul claro; um funil; uma lixeira; uma maçã; uma estrada em perspectiva, sombreada de cinza; gráficos com eixos; um diagrama de três círculos. Quase não há frase escrita: o texto da folha é rótulo.

**O ritmo, medido a 10 quadros por segundo de 0:12 a 15:51, sem o pulso do quadro-chave (método acima):** a imagem muda (traço novo ou caneta andando) em 44,2% do tempo; a voz fala em 87,0%; em 47,7% do tempo a voz fala com a caneta parada. São 68 pausas de traço de 2 s ou mais, somando 361,4 s; a mais longa tem 22,3 s (de 11:45,5 a 12:07,8), seguida de 17,7 s (de 1:23,1 a 1:40,8) e 14,0 s (de 8:49,4 a 9:03,4; esta começa com uns 2 s de traço fino abaixo do limiar de "mexendo", e a pausa de fato, de perto de 8:51,3, dura uns 12 s); só 6 ficam entre 5,7 e 6,2 s, sem aglomeração nessa faixa. Contando o pulso, as pausas longas se partem em pedaços de uns 5,8 s, o ritmo dos quadros-chave, e a conta dá 79 pausas, a maior de 11,6 s, com uma dúzia entre 5,7 e 6,2 s: é efeito da compressão do vídeo, não do desenho. A folha alterna rajadas de desenho, de 1 a 2 s por figura, com o quadro parado enquanto a voz explica.

**A velocidade do traço:** um boneco sai em cerca de 1 s; "Vision", 6 letras, em 1,5 s; "Stakeholders", 12 letras, em 1,7 s (cerca de 7 letras por segundo). Não há medida de tempo real de desenho para comparar. No zoom final, os quadros vêm repetidos aos pares, num arquivo de 30 quadros por segundo.

## Cortes

**O método e o limite:** a folha é quase toda branca, e um reenquadramento sobre papel vazio muda pouco a imagem (o de 0:25 deu nota 0,039), por isso o limiar baixo. Um reenquadramento seco sobre papel quase vazio pode ter ficado abaixo dele; no trecho de 0:12 a 1:22, olhado a cada 2 s, os dois reenquadramentos visíveis eram os dois detectados, e o resto não foi conferido quadro a quadro.

- **Abertura:** do preto ao cartão de título (0:00,27) e do título à folha em branco (0:11,53).
- **Dentro do desenho, de 0:11,5 a 15:51,7, 33 reenquadramentos:**
  - **18 cortes secos,** de um quadro para o outro: 0:25,3; 0:56,7; 3:40,5; 4:06,4; 4:13,0; 7:57,6; 8:19,4; 9:07,6; 9:21,3; 9:25,9; 9:42,7; 11:25,2; 11:43,4; 12:42,3; 14:37,0; 15:01,7; 15:10,8; 15:23,4.
  - **15 movimentos de câmera** de 0,3 a 0,5 s (10 a 16 quadros), com passos pequenos no começo e no fim e grandes no meio, às vezes juntando deslize e zoom: 5:32,9; 5:47,3; 8:31,6; 9:11,0; 9:18,4; 10:37,6; 10:52,0; 12:08,3; 12:11,8; 12:20,4; 12:29,1; 13:22,8; 13:34,6; 14:17,3; 14:20,1.
- **Fecho:** o zoom out (15:51,7), o escurecimento (15:57,9) e os créditos.

**O que os cortes fazem:** nenhum pula tempo do desenho. Nos pares de quadros antes e depois de cada um, o conteúdo da folha é o mesmo, e a medida de tinta não mostra traço surgindo de uma vez, fora das retas (abaixo, em "Material"). Os cortes mudam só o enquadramento: aproximam da parte que vai ser desenhada ou comentada (o funil, em 3:40), recuam para pôr o detalhe de volta no todo (em 9:07, o gráfico recém-desenhado vira um canto da folha) ou levam a câmera a papel em branco, onde o assunto seguinte começa (8:31, 9:25).

**Entre um reenquadramento e outro, a câmera fica parada:** não há deriva nem acompanhamento lento do traço; o movimento existe só nas transições de meio segundo. Até cerca de 8:00, a média passa de 50 s por plano. Na segunda metade, com vários assuntos em regiões separadas, cai para uns 19 s, com rajadas de 3 a 9 s (de 12:08 a 12:29, quatro movimentos em 21 s, entre o ciclo e os gráficos).

**Quando cortam:** nos três casos medidos, o reenquadramento vem de cerca de 0,25 a 0,4 s antes da frase que apresenta o elemento novo: a abertura (11,53 s contra 11,8 s), 0:25,3 (25,30 s contra 25,7 s) e a chegada da câmera em 8:31,6 (511,57 a 512,03 s contra 512,3 s). Não é o padrão dos 33. Cruzando o começo de cada um com os trechos da transcrição: 2 começam de 0,3 a 0,5 s antes de uma frase (0:25,3 e o movimento de 14:17,3); 2 caem numa pausa da fala, mas fora dessa faixa (11:43,4, 1,95 s antes da frase seguinte, e 8:31,6, que começa 0,71 s antes da frase e chega 0,25 s antes dela); e 29 começam dentro de um trecho de fala, 4 deles nos primeiros 0,3 s do trecho, junto com o começo da frase, dentro do erro da transcrição. O corte de 3:40,5 (220,53 s) vem 0,4 s depois do começo da frase da recusa (220,12 s). Nem a troca de assunto segue a faixa: 9:25,9 e 15:01,7 vêm 1,3 s depois da frase que abre o assunto novo.

## O mapa final

**A organização da folha, que cabe inteira no quadro 16:9:**
- **Centro-esquerda, nos dois terços de cima:** o ciclo central, o primeiro a ser desenhado: a personagem à esquerda, os interessados no alto, o funil de cartões embaixo à esquerda, o time embaixo ao centro, um grande arco azul de setas fechando o ciclo e uma nuvem verde no meio, com setas para todos os lados; uma legenda pequena em coluna na borda esquerda.
- **Coluna da direita:** quatro gráficos empilhados, desenhados um a um na segunda metade, ligados ao ciclo por setinhas com rótulo.
- **Faixa de baixo:** a lixeira, a estrada em perspectiva, o diagrama de três círculos e, por último, a versão com vários times, o último desenho antes do zoom out.

**O caminho do desenho:** de dentro para fora. O miolo vem primeiro; cada assunto novo ocupa papel vazio ao lado; a câmera volta ao miolo várias vezes, para acrescentar um detalhe (em 11:25 ela entra no funil para colorir alguns cartões) ou para mostrar onde o assunto novo se encaixa. As ligações entre regiões são poucas e leves (as setinhas do ciclo aos gráficos); a unidade vem da cor e da posição.

**O zoom out:** começa 0,1 s depois de a última frase de conteúdo acabar (a fala termina em 15:51,6; a câmera sai em 15:51,7) e dura cerca de 0,5 s (de 15:51,73 a 15:52,20), com a mesma curva dos outros movimentos: lento no começo, um salto grande no meio, assentando no fim. O plano final mostra uma área cerca de três vezes mais larga que a do plano anterior. A folha inteira fica parada por 5,7 s: a fala de fecho, com o título falado, ocupa os primeiros 3,4 s (de 15:52,5 a 15:55,6), com uma pausa no meio; vêm uns 2,3 s de silêncio sobre o mapa, e então o escurecimento. Não há passeio pela folha pronta.

## Material

- **Sem mão à vista:** a imagem de uma caneta (um estilete cinza de ponta escura) segue a ponta do traço e, nas pausas, fica parada ao lado do desenho.
- **Desenho digital,** não papel filmado: fundo branco levemente creme, sem pauta nem textura visível em 360p, sem a interface do programa no quadro.
- **Pincel com pressão:** a espessura muda ao longo do traço. Contorno preto nas figuras e nas letras; azul no fluxo, nos cartões e nas setas; verde nas pessoas e na comunicação; vermelho e verde nos gráficos. O preenchimento suave (a auréola verde, o amarelo da nuvem central, o cinza esfumado da estrada, o azul claro dos cartões) entra depois do contorno.
- **Retas por ferramenta:** os eixos e as linhas dos gráficos aparecem primeiro como uma linha fina e cinza e, no quadro seguinte, viram o traço grosso definitivo (de 8:32,7 a 8:33,1; de 12:45,2 a 12:45,4).
- **Letra:** toda escrita à mão, inclusive o título de abertura; rótulos curtos, em caixa alta e baixa, pequenos e regulares. Não há texto de computador dentro da folha; só os créditos.
- **Resolução:** em 360p, as letras menores do mapa final não se leem.

## O que a fonte e a medida não dizem

- Se o desenho foi acelerado, e quanto, e se a voz do original foi gravada junto com o desenho: o vídeo não diz. O FAQ do autor, que saiu do ar e foi lido numa captura de 22/09/2021 da Wayback Machine (https://web.archive.org/web/20210922224945/https://www.crisp.se/konsulter/henrik-kniberg/faq), diz que ele grava a tela inteira ao vivo enquanto desenha e fala, e edita depois no ScreenFlow. A pergunta ("How did you make your animated videos?") cita este vídeo pelo nome, entre três; mas a frase da gravação ao vivo vem no presente, logo depois de ele contar que trocou de mesa digitalizadora (por uma Wacom Cintiq), e não fica claro se descreve a gravação de 2012; e, como ele edita depois, a página não diz o que a edição muda nem se o desenho foi acelerado.
- A sincronia do original em inglês: a medida é a da dublagem.
- O nome da personagem e alguns termos: a transcrição sem revisão os troca.
- Os reenquadramentos sobre papel quase vazio que tenham ficado abaixo do limiar, fora do trecho de 0:12 a 1:22.
