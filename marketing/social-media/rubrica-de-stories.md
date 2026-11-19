---
versao: 0.1
status: rascunho a testar; muda livremente até a primeira calibração com sequências reais da conta (não está sob a decisão 7 da rubrica de carrossel)
---

# Rubrica de Stories

O que uma **sequência de Stories** precisa ter antes de ir ao ar, e também o **Story avulso** e o **Story em vídeo** (seções próprias, abaixo). A unidade principal é a sequência sobre um tema. Nasce de métodos de mercado em fala pública, sobretudo de quem tem método próprio de Stories em fala pública, com outros criadores como complemento. A prática dos perfis não é medida de fora (Stories somem em 24 horas e não vêm nas APIs públicas de outros perfis), então tudo aqui é fala de referência: **os limiares são chute** até as primeiras sequências da conta serem medidas.

Herda da rubrica de carrossel (`rubrica-de-qualidade.md`) as falhas de integridade, os erros de execução de texto e voz, as etiquetas de quem avalia ([código], [jev], [modelo], [pessoa]) e os quatro vereditos. O público é o de `context/publico.md`, e a voz, a de `context/sobre-mim.md`. Os testes [jev] só rodam com o Jev configurado (`TYPESAFE_API_KEY`, `scripts/jev/`); sem ele, ficam com a leitura de modelo.

## Para que serve

Nas fontes, o Stories é relacionamento e venda para quem já segue, não atração: "o feed é o palco, o Stories é a salinha", a menor parte da audiência, mas a melhor. Por isso, numa conta que começa ou volta de pausa, as primeiras sequências servem para **testar a rubrica e abrir conversa**, não para vender, e a medida é conversa, não view.

## Falhas e erros

- **Falhas de integridade:** as da rubrica de carrossel, sem mudança (afirmação sem lastro, citação que não é literal, promessa não cumprida, fora dos valores e as demais). Em Stories pesa em especial **fora dos valores**: escassez ou urgência falsas e "só hoje" que não é verdade.
- **Falha herdada de lastro:** os fatos de um Story vêm de uma peça que passou pelo portão (post ou Story), sem número novo; se a peça de origem mudar, o Story acompanha. Olhar os posts e os Stories que já passaram ajuda a reforçar o mesmo ponto com outra forma de explicar.
- **Erros de execução:** erro de texto e fora da voz, como no carrossel. **Texto essencial coberto** [código]: no Stories, o topo tem a barra de progresso e o nome, e a base tem a caixa de resposta; o essencial fica na área segura do Stories orgânico, numa tela de 1080 por 1920: o texto começa em 192 px, abaixo da linha que o app mostra a cerca de 140 px, e deixa livres embaixo 118 px (o texto termina antes de y 1802, a guia do editor do app) e 32 px de cada lado (as guias laterais do app), medidos em prints do editor do app num iPhone 11; quem assiste não tem nada sobre a parte de baixo do Story, porque a caixa de mensagem fica abaixo dele, e a guia de 118 px reserva a barra de comentário que o dono vê no próprio Story. Vale remedir no aparelho da equipe. Os 35% embaixo valem só para Story impulsionado, que segue a margem do Reels e dos anúncios.
- **Resultado sem a pergunta** [jev]: quando a pergunta da enquete foi feita no texto da tela, e não no próprio adesivo, o Story que devolve o resultado traz a pergunta antes do resultado, porque quem chega direto nele não viu a tela de origem. A tela declara o resultado como `data-adesivo="resultado"`. O cartão de resposta da caixinha já traz a pergunta e não precisa disso.

## Critérios

| | Critério | 0 | 1 | 2 |
|---|---|---|---|---|
| S1 | **Tema** | Stories soltos, sem fio | um tema, mas fora do que o perfil fala | um tema só, ligado ao que o perfil ensina, com a linha narrativa escrita antes |
| S2 | **Abertura** | abre com saudação ou contexto ("bom dia", "hoje eu quero falar") | vai direto ao ponto, mas não pede interação | vai direto ao ponto e pede interação no primeiro Story (enquete, caixinha, pergunta, mensagem) |
| S3 | **Motivo para ficar** | nada puxa o Story seguinte | promessa vaga de que "vem coisa boa" | antecipação concreta, quebra de expectativa ou dilema real |
| S4 | **Objetivo** | sem objetivo declarado | declarado, mas a sequência não o serve (entretenimento sem virada, venda no meio de uma sequência de engajamento) | declarado (engajamento, consciência ou venda), e cada Story serve a ele |
| S5 | **Comunidade** | nenhum dispositivo | dispositivo sem tensão real ("prefere café ou chá?"), ou um pedido em cada Story | pelo menos um dispositivo com tensão real, sem pedir algo a cada Story |
| S6 | **Pedido** | dois pedidos ou mais, ou link no meio da sequência | um pedido, mas genérico ou com link fora do último Story | um pedido só, no fim, por levantada de mão ou palavra-chave; link, se houver, só no último Story do dia |

Em sequência de engajamento sem pedido, S6 não se aplica.

## Testes por critério

- **S1** [modelo] todos os Stories tratam de um tema só? [pessoa] o tema é do que o perfil ensina? [código] a linha narrativa está escrita no roteiro antes da produção?
- **S2** [jev] o primeiro Story abre sem saudação nem contexto? (no Jev, duas perguntas) [jev] o primeiro Story pede uma interação (enquete, caixinha, pergunta, mensagem)? Que o primeiro Story **do dia** seja estático (foto e texto, ou texto) é hipótese, não teste: o motivo dado nas fontes (o alcance do dia) não tem fonte da plataforma.
- **S3** [jev] algum Story antecipa o que vem no fim, quebra a expectativa ou põe um dilema? (no Jev, uma pergunta por caminho) [modelo] o que se antecipa é concreto (o link, a resposta, o resultado), e é entregue?
- **S4** [código] o roteiro declara o objetivo? [modelo] cada Story serve a esse objetivo? [modelo] se há entretenimento, ele vira um valor ligado ao que o perfil ensina? Separar os objetivos é regra de quem começa; misturar engajamento e consciência é aceito quando declarado.
- **S5** [código + jev] há pelo menos um dispositivo de comunidade (caixinha, enquete com tensão, resposta do público repostada com comentário, pedido de história, análise prometida)? (os adesivos e a resposta repostada, o código; o pedido de história e a análise prometida, o Jev; a tensão, a leitura de modelo) [modelo] a pergunta tem tensão real, alguma coisa que a pessoa queira responder? [código] há pedido de interação em menos da metade dos Stories? Repostar sem comentar não conta.
- **S6** [código] há no máximo um pedido? [código] o pedido está no último Story da sequência? [código + jev] o pedido é por levantada de mão ou palavra-chave ("me manda 'quero'"), e não por link? (uma pergunta do Jev por ação, inclusive o link; a URL escrita, o código confirma) Link é aceito só no último Story do dia.

## Como fecha

Os mesmos quatro vereditos da rubrica de carrossel. **Reprovada:** falha de integridade com destino reprova, ou S1 = 0. **Ajustar:** nota 0 em S2, S4 ou S6, ou soma abaixo do limiar. **Retocar:** falha com destino corrigir, ou erro de execução. **Pronta:** nenhum 0 e soma de pelo menos 9 de 12 (75%; 8 de 10 sem S6). O limiar é chute e muda na primeira calibração.

## Como se mede

A medida é **conversa por pessoa alcançada**: respostas do Story somadas às mensagens que a sequência abre, divididas pelo alcance do primeiro Story. Ao lado, a **saída por Story** (quem sai da sequência ali, sobre quem viu), que mede S3. Os números vêm das métricas da conta (alcance, respostas, envios e navegação de cada Story), coletados enquanto o Story está no ar, porque a plataforma os apaga depois de 24 horas. Nem toda resposta é lead: uma sequência pode ter centenas de curiosos e outra dezenas de interessados, então quem publica marca à mão as conversas que importam.

## Onde vive uma sequência

`marketing/social-media/stories/AAAA-MM-DD-<tema>/roteiro.md`: o objetivo, a linha narrativa numa página e um bloco por Story (o texto, o que aparece, o dispositivo, o pedido). As imagens saem de um `stories.html` no visual da série ou da marca, pela skill `slides-export`, e quem publica sobe pelo celular, pondo os adesivos. O adesivo vai no centro da tela, onde o editor encaixa com as duas linhas guia, e o texto se compõe acima dele. Ajuste de posição não troca palavra; imagem substituída no mesmo endereço do bucket, até a publicação, leva `?v=N` no link do roteiro, por causa do cache (depois de publicada, nada se sobrescreve: a mudança sobe como versão nova); o texto de experiência pessoal vem de quem publica, e o assistente só dá a forma. A avaliação roda no roteiro antes de produzir e nas imagens antes de publicar.

Cada tela do `stories.html` declara o adesivo que vai receber no app (`data-adesivo="enquete"`; vários separados por espaço: enquete, caixinha, pergunta, quiz, reacao, foto). Com isso, a parte em código desta rubrica (quando o projeto a tiver) roda os testes [código] e, com o Jev, os [jev] antes da leitura de quem decide; o que é [modelo] fica com a leitura do assistente, porque nos Stories não há juiz nem ciclo de portão.

## Story avulso

Um Story só, com função própria: antecipar um post, compartilhar um post, responder alguém, avisar. Vale o que é de execução e integridade das seções acima, inclusive a área segura. A pasta é a mesma de uma sequência (`AAAA-MM-DD-<tema>/`, com `roteiro.md` e um `stories.html` de uma tela, próprio, sem imagem emprestada de outra pasta), e o roteiro declara `funcao` no frontmatter: `antecipacao`, `compartilhamento`, `resposta` ou `aviso`. O post compartilhado e o cartão da resposta entram pelo app, então a tela os declara como adesivo (`data-adesivo="post"` ou `"resposta"`), e o texto da tela é o comentário.

| | Critério | 0 | 1 | 2 |
|---|---|---|---|---|
| A1 | **Função** | sem função declarada | | função declarada no roteiro |
| A2 | **Uma ideia** | duas mensagens ou mais disputando a tela | uma ideia, mas longa para ler em poucos segundos | uma ideia só, lida em poucos segundos |
| A3 | **Comentário** (compartilhamento ou resposta) | repost sem comentário | comentário que só aponta ("saiu post", "olha isso") | comentário que acrescenta: o porquê, uma opinião, uma pergunta |
| A4 | **Antecipação** (função antecipação) | não diz o que vem | diz o quê ou quando, não os dois | diz o quê e quando |
| A5 | **Pedido** | dois pedidos ou mais | um pedido genérico ou por link | um pedido só, por palavra ou levantada de mão |

A3 só vale com post ou resposta declarados; A4, só na antecipação; A5, só quando há pedido. **Testes:** A1 [código] o frontmatter tem `funcao`? A2 [modelo] a tela passa uma mensagem só? (hipótese) [código] o texto tem até 40 palavras? A3 [código] há texto além do adesivo? [jev] o texto acrescenta algo ao que é compartilhado, em vez de só apontar para ele? A4 [jev] diz o que vem? [código] diz quando (dia da semana ou data; hora só com o dia)? A5 como o S6. **Fecha** como a sequência: reprovada por falha de integridade com destino; ajustar com um 0; pronta sem 0 e com pelo menos 75% do que se aplica.

**De onde vem:** repostar sem comentar não conta; compartilhar o próprio post não muda o alcance (Mosseri, abril de 2026), então o compartilhamento serve à conversa e ao lembrete, não ao alcance; um pedido só. A base não tem fonte dedicada ao Story avulso: os critérios são a tradução para uma tela do que vale para a sequência, e mudam na primeira calibração. **A2 é hipótese, sem fonte:** nada na base proíbe duas ideias numa tela, e há quem fale em vários dispositivos no mesmo Story; dispositivo não é ideia, mas a regra fica para a calibração confirmar.

## Story em vídeo

Um Story que é um vídeo inteiro (uma cena gravada por código), numa sequência ou avulso. Valem a sequência e o avulso acima, com três mudanças. **Os limiares são chute**, como o resto desta rubrica: vêm de legenda, não de Story, e se calibram pela navegação medida dos Stories em vídeo da conta.

- **S2 no primeiro segundo:** o primeiro segundo do vídeo conta como a capa, o primeiro Story: o que aparece e se lê nele vai direto ao ponto, sem saudação nem contexto [modelo, sobre a folha de quadros]. O pedido de interação segue o S2 do Story parado (o adesivo vai pelo app). O segundo é chute: a base só mede o gancho de vídeo em 3 s, no Reels (`knowledge/content-design/roteiro-em-formato-curto-o-que-e-medido.md`), e nada no Story.
- **A2 pelo tempo de leitura,** no lugar das 40 palavras ([modelo] por ora, a conta à mão de quem lê o roteiro; passa a [código] quando a conta entrar na parte em código): cada frase fica na tela pelo menos `caracteres ÷ 17` segundos, e no mínimo 0,3 s por palavra, contados da primeira palavra até o começo da saída (17 caracteres por segundo da Netflix em português e o piso de 0,3 s por palavra da BBC, `knowledge/content-design/tempo-de-leitura-em-video.md`). A frase longa demais para a cena se divide em duas, em vez de acelerar.
- **Por referência, sem repetir aqui:** a conferência da voz contra a imagem, quando o vídeo tem voz (cada frase classificada de S a R, pela tipologia da `piece-script`, como em "Hipóteses a testar" da `rubrica-de-qualidade.md`, sem entrar na nota); e um estilo de desenho por peça (D7 da `rubrica-de-design.md`).

## Hipóteses a testar (não são critérios)

- O primeiro Story do dia estático rende mais alcance do que vídeo (fala de criadora, sem fonte da plataforma).
- Link nos Stories corta o alcance; repost sem comentário derruba o alcance (fala de criadores, sem fonte da plataforma).
- Pergunta cotidiana, fora do nicho, abre mais conversa que pergunta do tema (relato).
- Volume: até quatro Stories estáticos por dia contra sequências de 5 a 10.
- Mostrar a vida pessoal é escolha: há quem peça o não editado e quem tenha parado de mostrar e visto os cliques subirem.

## Versões

A versão nova registra aqui, numa linha, o que mudou e por quê.

- **0.1:** a primeira versão do repositório.
