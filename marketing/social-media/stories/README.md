---
area: stories
cadencia: a definir
artefatos: [roteiro.md, stories.html]
---

# Stories

Uma pasta por sequência, `AAAA-MM-DD-<tema>/`, com o `roteiro.md` (objetivo, linha narrativa, os Stories, a avaliação, as imagens usadas e o resultado) e o `stories.html` de onde saem as imagens, com o adesivo de cada tela declarado em `data-adesivo` (os tipos da lista única `ADESIVOS` do `conferir_telas.py` da `visual-form`: enquete, caixinha, pergunta, quiz, reacao, barra, foto, link, post, resposta, resultado; o tipo fora dela é AVISO). A régua de juízo é a `../rubrica-de-stories.md`; a forma das telas é da skill `visual-form`, e a exportação, da `slides-export` (com `--height 1920`).

**Antes de criar:** ler no arquivo de lições das peças (`marketing/licoes.md`) as lições de cada etapa antes de fazê-la, e anotar no roteiro as que aplicou, ou "nenhuma lição registrada".

## O que está nesta pasta

| Arquivo | Para quê |
|---|---|
| `template/stories.html` | o modelo de sequência em flexbox, com três telas (abertura com enquete, tela densa, fecho com caixinha), que passa nas conferências da forma com 0 ERRO. Copie para a pasta da sequência e renomeie para `stories.html`: os caminhos relativos já valem de lá. Ele aponta para o caderno da série de exemplo; troque pelo da série da sequência |
| `adesivos.css` | os adesivos do app simulados por cima do Story, só na prévia (o export com `--previa`) |
| `scripts/espacos.py` | põe os desenhos de enfeite de cada tela nos maiores vazios dela (abaixo, "Os desenhos de enfeite") |
| `scripts/anima_cena.py` | grava em MP4 uma cena guiada por `window.quadro(t)`, para o Story em vídeo |
| `scripts/video_do_story.py` | confere todo vídeo de Story contra os limites da API, mede o movimento e grava a folha de quadros; com o roteiro, o tempo de leitura frase a frase e a legenda do vídeo com voz (o teste é o `teste_video_do_story.py`) |
| `animacoes.md` | o banco de animações dos Stories, com a técnica e o estado de cada uma |
| `references/guias-do-editor.md` | as medidas das guias do editor do app, de onde sai a área segura, e a escala do texto |

**A instalação:** os scripts pedem o que a `visual-form` e a `slides-export` já pedem (Playwright com o Chromium, Pillow, numpy, `imageio-ffmpeg`), mais o `scipy` para o `espacos.py` (`pip install scipy`).

## O arco e a venda (a testar)

O método por trás destas regras está em `knowledge/content-design/metodos-de-mercado-stories.md` (a arquitetura, os tipos de sequência, a medida) e em `knowledge/content-design/stories-10x-dispositivos.md` (os dispositivos e as 26 perguntas de sim ou não); a régua de cada uma é a rubrica de Stories.

- **A mesa dos arcos:** antes de escrever a sequência, três arcos numa mesa de escolhas, cada um com os Stories em uma linha, os dispositivos marcados pelo nome da síntese de dispositivos, o que a caixinha pergunta, o que a manhã seguinte faz com as respostas e onde fica a passagem do emocional ao técnico, ou por que o arco não a tem: a sequência começa pelo emocional ou pelo comportamento e passa ao técnico, porque o técnico sozinho não traz resposta (pergunta 13 da síntese). A quantidade de Stories é item próprio da mesa, e o volume cresce por medida: a retenção no último Story da sequência nova contra a da anterior decide se a próxima sobe.
- **A abertura por caminho:** duas ou três aberturas para o Story 1, cada uma por um caminho diferente da base, com a fonte ao lado: a curiosidade concreta, o enquadramento de notícia, começar no meio do conflito (nunca "hoje vou contar") e o nome esquisito que faz parar (síntese de dispositivos). Na venda, o mesmo vale para o tema: o problema vizinho atrai, e o produto vem no fim.
- **A sequência profunda** (crônica, história, diário, hot seat), que não depende de interação e fica nos Destaques, declara `profunda: true` e `destaque: true` no frontmatter, e a rubrica aceita nela a abertura sem pedido (S2).
- **A semana de venda:** a venda chega depois de dias de jab, sequências sem pedido de compra, porque sem eles ninguém sabe quem você é no dia do pedido (pergunta 4 da síntese de dispositivos; leitura nossa: a proporção de 80% de jab é entre dias). O dia de colheita, quando houver, é a sequência direta de dois Stories (depoimento e link, `direta` no frontmatter), no fim do ciclo de jab, e o dia exato se decide no planejamento da semana de venda. As regras da sequência de consciência e de venda estão na rubrica, seção própria.
- **O combustível:** campo opcional do roteiro da sequência de consciência e de venda, com o canal de fora que traz gente para ela (a legenda do post do dia, o fim de uma palestra, a lista de e-mail, se houver) e o texto da chamada lá, que segue a regra do dia (abaixo), porque a mensagem de fora também é lida horas depois.

## A forma dos Stories

- **O topo e os adesivos:** a área segura do texto essencial é de y 192 a 1802 e de x 32 a 1048 (`references/guias-do-editor.md`); o `conferir_telas.py` da `visual-form` a confere, e o texto fora dela é ERRO. Os adesivos ficam na posição padrão do app: a enquete de duas opções, centrada, de y 783 a 1137; a caixinha, com a foto, de 744 a 1176; a reação, um círculo de cerca de 290 px centrado em (540, 1036); a barra de emoji, 727 px de largura, centrada em y 654, com a altura crescendo com as linhas de pergunta. Todos estão simulados no `adesivos.css`; quando o adesivo vai para outra posição, a tela declara `--adesivo-top`. A pergunta, o quiz e o link ainda não têm medida no app e não se desenham na prévia. O texto fica acima do adesivo: o `conferir_telas.py` avisa o texto que cai dentro da caixa do adesivo simulado (`texto_sob_adesivo`) e a caixa fora da área segura (`adesivo_na_borda`: um toque na metade direita avança o Story, e o pé tem a caixa de resposta), medidos na mesma caixa que a prévia desenha.
- **A prévia:** o export com `--previa` desenha os adesivos simulados por cima e a linha branca do topo; é a imagem para quem valida conferir as posições e para a conferência pela imagem. A imagem que vai para o celular sai sem eles.
- **Sequência nova nasce em flexbox,** do modelo `template/stories.html`: a `.coluna` começa em 192 px e termina a 118 px do pé, ou antes do adesivo. Posição fixa só para o que tem lugar fixo (desenho de enfeite, cartão, anotação em volta de um desenho).
- **Corpo de 40 a 46 px,** título de 76 a 80 px; um tamanho por papel em cada tela. **Negrito nas palavras-chave** do texto denso; o **marca-texto só na frase para levar**, no máximo um por tela.
- **Cartão com moldura só com função:** no Story denso de leitura que precisa segurar quem pularia; nunca como padrão.
- **A moldura da sequência** (série, perfil, contador), quando houver, fica dentro da área segura, como o texto essencial.
- **Mudança de fonte, peso ou entrelinha reassenta as anotações posicionadas:** medir (o `medir_blocos.py` da `visual-form`) antes de dar a tela por pronta.
- **Desvio, avisado:** regra quebrada de propósito vai no `refinamentos.md` da sequência, uma linha por desvio, com `data-intencional` ou `data-sangria` no HTML.

## Os desenhos de enfeite

Cada tela tem a sua dispersão, sem repetir a posição de outra; o maior vazio da tela recebe o desenho maior, e assim por diante, com um dominante por tela e no máximo três tamanhos. A lista de cada tela vai em `desenhos.json` na pasta da sequência (o formato no docstring do `espacos.py`), e o script mede os vazios na prévia com os adesivos simulados e escreve as posições no HTML:

```
python -X utf8 marketing/social-media/stories/scripts/espacos.py marketing/social-media/stories/<pasta> --html stories.html
```

O que só decora custa atenção, e custa mais quanto mais: nada de valência negativa, o objeto é típico e reconhecível, e a quantidade se mede nas métricas, não se supõe.

## O texto que atravessa o dia

- **Sem "hoje", "amanhã" nem "ontem":** o Story fica no ar 24 horas e atravessa a virada do dia, então a referência relativa erra para quem vê no dia seguinte. Use o dia da semana ou a data ("terça, 18h"), ou uma referência que não depende do dia ("o post mais recente"). O `conferir_telas.py` avisa as palavras da lista dele (`PALAVRAS_DO_DIA`).
- **Horário sempre com o dia,** e, no prazo de venda, com o fuso por extenso: no Brasil, pelo horário de Brasília ("até domingo, 23h59, horário de Brasília"; rubrica de Stories, "Sequência de consciência e de venda", a testar); nos outros horários, a critério. O Story que pode ir para um Destaque leva a data, porque fica no perfil sem prazo; nenhuma tela depende de a pessoa ter visto a anterior; e fica de fora a chamada que o app não deixa cumprir ("arrasta pra cima", "link na bio" sem dizer qual, "clica aqui"). O `conferir_telas.py` avisa a chamada da lista dele (`CHAMADAS_SEM_CAMINHO`) e o texto que fala em link numa tela sem `data-adesivo="link"`; e, com `destaque: true` no frontmatter do `roteiro.md` (a sequência que pode ir para um Destaque), a tela que diz o dia da semana ou a hora sem a data é ERRO (`destaque_sem_data`).
- **O aviso do post sem verbo no futuro:** o Story fica no ar antes e depois da hora do post, então "às 18h sai o post" fica errado para quem vê depois. Use um verbo que vale dos dois lados ("o post de sexta, às 18h, traz...") ou só o substantivo com o dia.

## O registro no roteiro

- **As passadas:** a cada etapa de conversa com quem valida (passada ou mesa), a prévia da sequência inteira ganha uma linha na seção "Passadas" do roteiro, com o caminho ou o link da imagem, na mesma entrega.
- **Os artefatos gerados:** a seção "Artefatos gerados" do roteiro leva cada imagem gerada que foi ao banco de imagens, usada ou não, com os Stories em que entrou.

## O Story montado no app e o de resposta

- **Story montado no app** (o compartilhamento de um post, a resposta a uma caixinha): o assistente monta uma simulação no `stories.html` da pasta (o cartão do post ou da resposta na posição combinada, o fundo e o texto com as quebras e o tamanho, em fontes aproximadas das do app), que serve para validar o texto e saber onde posicionar. Validada, a simulação é exportada, e o roteiro ganha a tabela de imagens (simulação e publicado).
- **Story de resposta à caixinha:** para cada resposta escolhida, o assistente gera a imagem de fundo com o comentário já escrito e o espaço livre para o cartão da resposta, que a pessoa encaixa pelo app. O nome de quem respondeu não aparece no cartão compartilhado, e as respostas, que são dado pessoal de terceiro, não se guardam no repositório.
- **A resposta no direct:** a resposta que não entra na sequência ganha o texto sugerido pelo assistente, que quem publica manda pelo direct, colando ou lendo em voz ou em vídeo, e a tabela de respostas do roteiro diz como cada uma foi respondida. **Na sequência de venda** (rubrica de Stories, a testar; `knowledge/sales-and-offers/vendas-no-direct.md`): o texto sugerido abre com uma pergunta sobre o caso da pessoa, e não com a oferta, que vem só depois que ela se abre; e, a quem recebeu o link, uma segunda mensagem sugerida no dia seguinte ("comprou, ou ficou alguma dúvida?"), com a linha na tabela de respostas.
- **O resultado da enquete não se compartilha sobre fundo novo:** compartilhado de novo num Story, ele vem com o fundo do Story original. Para devolver o resultado com a imagem da série, o cartão é recortado de um print do Story de origem e colado na imagem, no lugar da enquete.

## O Story em vídeo

As animações e o estado de cada uma ficam em [`animacoes.md`](animacoes.md); uma por sequência, para a leitura dizer qual segura quem assiste. A cena é uma página com `window.quadro(t)`, gravada pelo `anima_cena.py`:

```
python -X utf8 marketing/social-media/stories/scripts/anima_cena.py <pasta>/<cena>.html <trabalho>/cena.mp4 --segundos 6 --altura 1920
python -X utf8 marketing/social-media/stories/scripts/anima_cena.py <pasta>/stories.html <trabalho>/story-04.mp4 --slide 4 --segundos 12
```

**Todo vídeo de Story passa pelo `scripts/video_do_story.py`:** os limites do Story na API (de 3 a 60 s, de 23 a 60 qps, H.264 ou HEVC, 4:2:0, o `moov` no começo e sem lista de edição, até 25 Mbps e 100 MB, a proporção do Story com AVISO fora do 9:16), como ERRO, e, como leitura, o movimento medido pelo `saltos.py` da `object-anatomy` e a folha de quadros a 0, 30, 60 e 90% da duração. O `anima_cena.py` o chama depois de gravar; o vídeo que vai pelo app (o de câmera, o de outra ferramenta) passa por ele à mão, e os limites ali são aviso de que a API não o aceitaria. **O roteiro do vídeo:** com o `roteiro.md` ao lado (o da página no `anima_cena.py`, o achado junto do MP4, ou `--roteiro`, que roda sozinho antes de gravar), o `video_do_story.py` avisa a frase da tabela de tempo abaixo da régua do tempo de leitura, contada frase a frase, e o vídeo com voz sem a legenda revisada declarada ("legenda: queimada, revisada"; o vídeo com voz se reconhece por `voz: true`, campo opcional do frontmatter do `roteiro.md`, ou por "câmera" na `funcao`); no vídeo de câmera, o roteiro declara também a forma da legenda (palavras por bloco, lugar, tamanho, cor e o tempo de cada bloco), e o estilo e o lugar dela vão a quem decide, com um quadro de cada opção (rubrica, "Story em vídeo").

```
python -X utf8 marketing/social-media/stories/scripts/video_do_story.py <trabalho>/story-04.mp4
python -X utf8 marketing/social-media/stories/scripts/video_do_story.py --roteiro <pasta>/roteiro.md
```

O objeto que funciona, se monta ou se separa vem da skill `object-anatomy`, no mesmo contrato.

## O que esta versão não traz

- **A parte em código da rubrica de Stories com o Jev** (o avaliador que lê a imagem com os adesivos simulados e pega a referência implícita a um dia): vem numa próxima versão. Até lá, o código confere a área segura, a sobreposição, o contraste, o dia relativo, os adesivos, a chamada e a data do Destaque (pelo `conferir_telas.py`) e o vídeo (pelo `video_do_story.py`), e o resto da rubrica é leitura.
- **A publicação dos Stories pela API e a ligação de cada Story ao id publicado:** não vêm. A sequência se publica pelo app; o `conferir_telas.py` já reconhece a tabela "Publicada pela API" no `roteiro.md`, se uma publicação pela API vier a gravá-la.
- **A agenda da semana e a janela de horário:** são escolha de cada conta; decida e escreva aqui, com o porquê, antes da primeira sequência.
