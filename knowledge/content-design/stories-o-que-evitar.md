# O que evitar em Stories: texto e montagem

Os erros de texto e de montagem que fazem um Story falhar com quem chega nele: a referência de tempo que erra no dia seguinte, a tela que só faz sentido para quem viu a anterior, a chamada que o app não deixa cumprir, o adesivo no lugar errado e o que o leitor de tela não alcança. Para cada item: de onde vem, se a conferência é de código, pergunta de um avaliador tipado (o Jev, opcional) ou julgamento, e o que a base já cobre. O método de mercado (o que fazer) está em [[metodos-de-mercado-stories]] e [[stories-10x-dispositivos]]; a régua é `marketing/social-media/rubrica-de-stories.md`, e as regras de produção, `marketing/social-media/stories/README.md`. A área segura de Stories está em [[carrossel-instagram]].

## 1. Referência presa ao momento, além de hoje, amanhã e ontem

O Story fica no ar 24 horas e atravessa a virada do dia; a sequência sai entre 5h e 9h e é vista até a manhã seguinte. A regra de produção (README de Stories) tira "hoje", "amanhã" e "ontem", e uma conferência de código pode procurar "hoje", "amanhã", "ontem", "esta noite", "hoje à noite" e "agora há pouco". Erram pelo mesmo motivo:

- **"agora", "daqui a pouco", "mais tarde", "acabei de":** dizem a hora em que o texto foi escrito, que não é a hora em que é lido; numa sequência preparada na véspera, nem a de quem escreveu.
- **"esta manhã":** lida à noite, ainda serve; lida na manhã seguinte, aponta para outro dia.
- **"esta semana":** o Story de sábado de manhã é visto no domingo, quando "esta semana" já pode ser a seguinte (depende de onde a semana começa).
- **Horário sem fuso:** "terça, 18h" parece seguro. O público está quase todo no horário de Brasília, mas o Brasil tem quatro fusos e há quem siga de fora.

**Vira:** código para a lista de palavras (a mesma conferência, com as palavras novas) e para achar o horário escrito (um padrão como "18h" ou "18h30"); uma pergunta do Jev para a referência implícita a um momento; e julgamento de quem pede sobre o fuso.

## 2. O Story que vai para os Destaques

No Destaque, o Story deixa de vencer em 24 horas, e até o que a regra permite erra: "terça, 18h" vira uma terça qualquer. A base só fala de Destaque como guarda de sequências profundas num perfil do zero (o Ladeira, em [[metodos-de-mercado-stories]], item 2), sem regra de texto. A Central de Ajuda do Instagram, que descreve os Destaques, não renderizou na pesquisa.

**Vira:** julgamento sobre o que guardar; e código, se o roteiro declarar `destaque: true` no frontmatter: aí a lista vale inteira, mais o dia da semana sem data. A alternativa é a tela de Destaque nascer à parte, sem referência de tempo.

## 3. Depender de ter visto outra tela

Muita gente chega a um Story sem ter passado pelos anteriores: pelo Destaque, por um compartilhamento, pulando telas, ou na manhã seguinte, quando a primeira já venceu. Dentro de uma sequência, uma tela puxar a seguinte é o método (a antecipação); o problema é a tela que **só** se entende com a anterior. O caso mais comum é o resultado de enquete sem a pergunta; e o comentário de um compartilhamento tem de conversar com o que o cartão mostra.

**Vira:** pergunta do Jev nas telas de entrada (a primeira do dia, o resultado, a resposta repostada, o compartilhamento): "dá para entender esta tela sem as anteriores?". Nas telas do meio, julgamento.

## 4. Chamada que a plataforma não deixa cumprir

- **"Arrasta pra cima":** o gesto saiu do app, e o Sobral já registra que não existe mais como chamada ([[metodos-de-mercado-stories]], item 14). O link nos Stories é por adesivo.
- **"Link na bio" sem contexto:** a Universidade do Alabama pede que a chamada diga o destino ([[2026-10-29-ua-acessibilidade-stories-instagram]]).
- **"Clica aqui":** pelo mesmo motivo, o rótulo diz para onde vai ("Link: inscrição na oficina", no exemplo da página); e "clica no link" sem adesivo de link na tela é pedido impossível.

**Vira:** código para a lista ("arrasta pra cima", "arrasta para cima", "link na bio", "clica aqui", "clique aqui") e para o texto que fala em link numa tela sem adesivo de link (o `data-adesivo` ganharia o tipo `link`); o Jev para a chamada sem destino claro. **Coberto pelo método:** o pedido por palavra ou levantada de mão, com link só no último Story do dia ([[stories-10x-dispositivos]], perguntas 19 e 20).

## 5. Adesivo perto da borda direita ou da caixa de resposta

Um toque na metade direita da tela avança para o próximo Story, e o pé da tela tem a caixa de resposta e os botões; um adesivo encostado nesses lugares é difícil de tocar. As medidas do orgânico (14% livres em cima, 20% embaixo, ~380 px) estão em [[carrossel-instagram]]; a orientação da Meta sobre a área de toque está nas páginas de ajuda, que não renderizaram (só citação).

**Vira:** código: medidas as posições dos adesivos (numa tela de 1080 por 1920, a enquete ocupa cerca de 783 a 1137 px de altura e a caixinha, de 744 a 1176, centradas) e desenhado o adesivo simulado na prévia, um teste confere a caixa do adesivo e o texto essencial dentro da área segura.

## 6. Stories sem texto alternativo

O Instagram não aceita texto alternativo próprio nos Stories ([[2026-10-29-ua-acessibilidade-stories-instagram]]; a Universidade de Nebraska–Lincoln diz o mesmo, só citação), e o post oficial de 2022 só fala de texto alternativo em fotos ([[2026-10-29-instagram-avancos-em-acessibilidade]]). Telas montadas em HTML e exportadas são imagem do começo ao fim: o texto é desenhado no HTML e vira pixel, e o leitor de tela não o lê. A página do Alabama recomenda pôr o essencial com a ferramenta de texto do app, o que sugere que o texto nativo chega ao leitor de tela (não conferido), e publicar a informação crítica também num post do feed, com texto alternativo: "Use Stories for promotion, not as the only source of information." Nebraska–Lincoln vai além e sugere parar de usar Stories até a Meta dar o recurso.

**Vira:** julgamento sobre o que é crítico (data de evento, prazo, a resposta de uma dúvida), com a regra de o Story nunca ser o único lugar dessa informação. **Coberto em parte:** a publicação pela API pode mandar o texto alternativo dos posts (por exemplo, de uma seção "Texto alternativo" na `legenda.md`).

## 7. Contraste: a plataforma não declara número para Stories

Nem o Instagram nem a página do Alabama dão um número; ela pede "contraste forte", fundo sem estampa atrás do texto e nada que dependa só da cor. A referência geral é a WCAG, critério 1.4.3: 4,5:1 para texto comum e 3:1 para texto grande ([[2026-10-29-w3c-wcag22-contraste-minimo]]). Tintas escuras sobre papel claro costumam passar com folga pela conta de luminância da WCAG (um traço de caneta escuro sobre verde ou amarelo-claro dá perto de 9:1; um cinza de lápis, perto de 5:1); o risco está no texto sobre foto, degradê ou cartão de post, como no Story montado no app.

**Vira:** código para as cores sólidas (a conta sai das variáveis de cor do design system da série); conferência pela imagem (Jev ou modelo com visão) quando o fundo é foto ou degradê. E nada que dependa só da cor: o destaque tem de seguir visível para quem não distingue vermelho de verde.

## 8. Vídeo sem legenda

"Stories with audio must be understandable without sound" (Alabama). O adesivo de legendas existe nos Stories desde maio de 2021, gera o texto do áudio e deixa corrigir palavra por palavra, em 17 línguas com o português ([[2026-10-29-instagram-avancos-em-acessibilidade]]); a legenda automática erra e precisa de revisão, e não pode cobrir botões nem o nome. Quanto se assiste sem som: a pesquisa trouxe "1/3 toca sem som", sem primária aberta; o número que circula atribuído ao próprio Instagram é de 60% dos vídeos de Stories vistos com som (40% sem), de cerca de 2018, também não conferido. Para a regra, basta a direção: uma parte grande vê sem som.

**Vira:** julgamento e processo: o item em vídeo do roteiro leva "legenda: adesivo, revisada". **Não coberto** pela régua de texto: o vídeo pede processo próprio.

## 9. Tempo de tela de uma foto

Uma foto nos Stories fica cerca de 7 segundos na tela, e o Metricool recomenda de 5 a 7 segundos para foto, vídeo curto ou citação. Não há primária da Meta na pesquisa: vale conferir no app, cronometrando um Story publicado. A tela de texto precisa ser lida nesse tempo, ou a pessoa toca para voltar.

**Vira:** código para a contagem de palavras por tela, com o limite calibrado contra a navegação medida (voltar e sair, que uma coleta de métricas pela API traz). Quantas palavras cabem em 7 segundos não tem fonte direta; é hipótese a medir. Pela régua da legenda (até 17 caracteres por segundo em português, Netflix; 0,33 s por palavra na média da BBC, 0,3 no piso), 7 s comportam cerca de 120 caracteres ou de 21 a 23 palavras; a leitura silenciosa, sem a imagem em movimento que a legenda divide, daria até cerca de 28 (média em inglês); um teto de 40 palavras pediria cerca de 13 s na régua da legenda; detalhe e ressalvas em [[tempo-de-leitura-em-video]]. A calibração pela navegação é o que decide, com um limite: se quase nenhuma tela publicada ficou abaixo do corte que se quer testar, o que já foi publicado não testa o corte, e o teste que falta é uma sequência com as telas divididas abaixo dele contra uma densa do mesmo tipo. Leitura do assistente: comparar dentro de cada sequência (voltas e alcance da tela seguinte contra o número de palavras), não entre sequências.

## Resumo

| Item | Vira | Já na base |
|---|---|---|
| 1. Referência ao momento | código (lista, horário), Jev (implícita), julgamento (fuso) | hoje, amanhã e ontem, no README de Stories; o fuso: o prazo de venda leva "horário de Brasília" (rubrica de Stories, "Sequência de consciência e de venda", a testar) |
| 2. Destaque | julgamento; código com `destaque: true` | o ERRO `destaque_sem_data` do `conferir_telas.py` |
| 3. Depender de outra tela | Jev nas telas de entrada; julgamento no meio | resultado sem a pergunta; comentário do compartilhamento |
| 4. Chamada impossível | código (lista, link sem adesivo), Jev (destino) | link só no último Story; "arrasta para cima" em [[metodos-de-mercado-stories]]; a lista e o link sem adesivo como AVISOs do `conferir_telas.py` |
| 5. Adesivo na borda ou no pé | código (área segura) | área segura em [[carrossel-instagram]]; o texto sob o adesivo e a caixa fora da área segura como AVISOs do `conferir_telas.py` |
| 6. Sem texto alternativo | julgamento (o que é crítico) | texto alternativo nos posts (na publicação pela API); na venda, o teste [pessoa] da rubrica de Stories ("Sequência de consciência e de venda") |
| 7. Contraste | código (cores sólidas), imagem (foto e degradê) | WCAG 1.4.3 |
| 8. Vídeo sem legenda | julgamento e processo | o aviso do `video_do_story.py` para o vídeo com voz sem "legenda: ..., revisada" no roteiro |
| 9. Tempo de tela | código (palavras), medida (voltar) | [[tempo-de-leitura-em-video]] |

Tudo o mais que a página do Alabama pede e a base já pratica: frases curtas, o texto no mesmo lugar de uma tela para a outra, espaço para nada ficar cortado, e nada que pisque.

## Fontes

- **Raw:** [[2026-10-29-ua-acessibilidade-stories-instagram]], [[2026-10-29-instagram-avancos-em-acessibilidade]].
- **Só citação:** Metricool (Kalum), "How Long Can (and Should) Instagram Stories Be?", 07/11/2025, atualizado em 19/06/2026, https://metricool.com/instagram-stories-length/ ("each one will show for 7 seconds"; de 5 a 7 segundos para foto); University of Nebraska–Lincoln, "Digital Accessibility Best Practices for Social Media", https://ada.unl.edu/digital-accessibility-best-practices-social-media (Stories sem texto alternativo; post do feed com texto alternativo depois, ou parar de usar Stories); Central de Ajuda do Instagram e Meta Business Help, páginas sobre Stories (Destaques, área de toque, duração), que não renderizaram na pesquisa.
- **Não verificado:** "1/3 dos Stories toca sem som" (sem primária); "60% dos vídeos de Stories são vistos com som", atribuído ao Instagram em matérias de cerca de 2018.
