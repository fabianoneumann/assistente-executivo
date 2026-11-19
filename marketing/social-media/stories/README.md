---
area: stories
cadencia: a definir
artefatos: [roteiro.md, stories.html]
---

# Stories

Uma pasta por sequência, `AAAA-MM-DD-<tema>/`, com o `roteiro.md` (objetivo, linha narrativa, os Stories, a avaliação, as imagens usadas e o resultado) e o `stories.html` de onde saem as imagens, com o adesivo de cada tela declarado em `data-adesivo`. A régua de juízo é a `../rubrica-de-stories.md`; a forma das telas é da skill `visual-form`, e a exportação, da `slides-export` (com `--height 1920`).

**Antes de criar:** ler no arquivo de lições das peças (`marketing/licoes.md`) as lições de cada etapa antes de fazê-la, e anotar no roteiro as que aplicou, ou "nenhuma lição registrada".

## O que está nesta pasta

| Arquivo | Para quê |
|---|---|
| `template/stories.html` | o modelo de sequência em flexbox, com três telas (abertura com enquete, tela densa, fecho com caixinha), que passa nas conferências da forma com 0 ERRO. Copie para a pasta da sequência e renomeie para `stories.html`: os caminhos relativos já valem de lá. Ele aponta para o caderno da série de exemplo; troque pelo da série da sequência |
| `adesivos.css` | os adesivos do app simulados por cima do Story, só na prévia (o export com `--previa`) |
| `scripts/espacos.py` | põe os desenhos de enfeite de cada tela nos maiores vazios dela (abaixo, "Os desenhos de enfeite") |
| `scripts/anima_cena.py` | grava em MP4 uma cena guiada por `window.quadro(t)`, para o Story em vídeo |
| `animacoes.md` | o banco de animações dos Stories, com a técnica e o estado de cada uma |
| `references/guias-do-editor.md` | as medidas das guias do editor do app, de onde sai a área segura, e a escala do texto |

**A instalação:** os scripts pedem o que a `visual-form` e a `slides-export` já pedem (Playwright com o Chromium, Pillow, numpy, `imageio-ffmpeg`), mais o `scipy` para o `espacos.py` (`pip install scipy`).

## A forma dos Stories

- **O topo e os adesivos:** a área segura do texto essencial é de y 192 a 1802 e de x 32 a 1048 (`references/guias-do-editor.md`); o `conferir_telas.py` da `visual-form` a confere, e o texto fora dela é ERRO. Os adesivos ficam na posição padrão do app: a enquete de duas opções, centrada, de y 783 a 1137; a caixinha, com a foto, de 744 a 1176; a reação, um círculo de cerca de 290 px centrado em (540, 1036); a barra de emoji, 727 px de largura, centrada em y 654, com a altura crescendo com as linhas de pergunta. Todos estão simulados no `adesivos.css`; quando o adesivo vai para outra posição, a tela declara `--adesivo-top`. O texto fica acima do adesivo.
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
- **Horário sempre com o dia;** o Story que pode ir para um Destaque leva a data, porque fica no perfil sem prazo; nenhuma tela depende de a pessoa ter visto a anterior; e fica de fora a chamada que o app não deixa cumprir ("arrasta pra cima", "link na bio" sem dizer qual, "clica aqui").
- **O aviso do post sem verbo no futuro:** o Story fica no ar antes e depois da hora do post, então "às 18h sai o post" fica errado para quem vê depois. Use um verbo que vale dos dois lados ("o post de sexta, às 18h, traz...") ou só o substantivo com o dia.

## O registro no roteiro

- **As passadas:** a cada etapa de conversa com quem valida (passada ou mesa), a prévia da sequência inteira ganha uma linha na seção "Passadas" do roteiro, com o caminho ou o link da imagem, na mesma entrega.
- **Os artefatos gerados:** a seção "Artefatos gerados" do roteiro leva cada imagem gerada que foi ao banco de imagens, usada ou não, com os Stories em que entrou.

## O Story montado no app e o de resposta

- **Story montado no app** (o compartilhamento de um post, a resposta a uma caixinha): o assistente monta uma simulação no `stories.html` da pasta (o cartão do post ou da resposta na posição combinada, o fundo e o texto com as quebras e o tamanho, em fontes aproximadas das do app), que serve para validar o texto e saber onde posicionar. Validada, a simulação é exportada, e o roteiro ganha a tabela de imagens (simulação e publicado).
- **Story de resposta à caixinha:** para cada resposta escolhida, o assistente gera a imagem de fundo com o comentário já escrito e o espaço livre para o cartão da resposta, que a pessoa encaixa pelo app. O nome de quem respondeu não aparece no cartão compartilhado, e as respostas, que são dado pessoal de terceiro, não se guardam no repositório.
- **O resultado da enquete não se compartilha sobre fundo novo:** compartilhado de novo num Story, ele vem com o fundo do Story original. Para devolver o resultado com a imagem da série, o cartão é recortado de um print do Story de origem e colado na imagem, no lugar da enquete.

## O Story em vídeo

As animações e o estado de cada uma ficam em [`animacoes.md`](animacoes.md); uma por sequência, para a leitura dizer qual segura quem assiste. A cena é uma página com `window.quadro(t)`, gravada pelo `anima_cena.py`:

```
python -X utf8 marketing/social-media/stories/scripts/anima_cena.py <pasta>/<cena>.html <trabalho>/cena.mp4 --segundos 6 --altura 1920
python -X utf8 marketing/social-media/stories/scripts/anima_cena.py <pasta>/stories.html <trabalho>/story-04.mp4 --slide 4 --segundos 12
```

O objeto que funciona, se monta ou se separa vem da skill `object-anatomy`, no mesmo contrato.

## O que esta versão não traz

- **A parte em código da rubrica de Stories com o Jev** (o avaliador que lê a imagem com os adesivos simulados e pega a referência implícita a um dia): vem numa próxima versão. Até lá, o código confere a área segura, a sobreposição, o contraste e o dia relativo (pelo `conferir_telas.py`), e o resto da rubrica é leitura.
- **A publicação dos Stories pela API e a ligação de cada Story ao id publicado:** não vêm. A sequência se publica pelo app; o `conferir_telas.py` já reconhece a tabela "Publicada pela API" no `roteiro.md`, se uma publicação pela API vier a gravá-la.
- **A agenda da semana e a janela de horário:** são escolha de cada conta; decida e escreva aqui, com o porquê, antes da primeira sequência.
