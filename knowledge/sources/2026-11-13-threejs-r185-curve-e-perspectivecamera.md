---
titulo: "three.js r185: Curve.js (getPointAt e getUtoTmapping) e PerspectiveCamera.js (getFilmHeight)"
tipo: artigo
autor: "three.js authors (repositório mrdoob/three.js)"
url: "https://github.com/mrdoob/three.js/blob/r185/src/extras/core/Curve.js"
publicado_em: 2026-07-01   # data do commit 2431a09, para o qual a tag r185 aponta (API do GitHub); os arquivos não trazem data
capturado_em: 2026-11-13
licenca: "MIT (arquivo LICENSE da tag r185, https://github.com/mrdoob/three.js/blob/r185/LICENSE, 'Copyright © 2010-2026 three.js authors'); trechos do código com os comentários, embaixo, sem o texto da licença"
areas: [generative-media]
tags: [threejs, camera-path, catmull-rom, arc-length, perspective-camera, film-gauge, aspect-ratio, source-code]
---

# three.js r185: o getPointAt anda pelo comprimento da curva, e a altura do filme só encolhe em paisagem

Nota de fato: tabelas do que os três métodos fazem e do que os comentários deles dizem, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Ficha; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Dois arquivos do código-fonte do three.js na tag `r185` (o objeto da tag é o `cb3b077`, que aponta para o commit `2431a09`, de 2026-07-01, pela API do GitHub; o `package.json` da tag está na versão 0.185.1, a do pacote `three@0.185.1`): https://github.com/mrdoob/three.js/blob/r185/src/extras/core/Curve.js e https://github.com/mrdoob/three.js/blob/r185/src/cameras/PerspectiveCamera.js, baixados de `raw.githubusercontent.com/mrdoob/three.js/r185/` na revisão do Passo 7 da rodada "linguagem de câmera virtual", para conferir dois fatos que a documentação não dá. sha256 dos arquivos baixados: `Curve.js` (hash omitido), `PerspectiveCamera.js` (hash omitido) e `LICENSE` (hash omitido); duas descargas separadas, a da conferência e a desta ficha, deram os mesmos hashes. Cobertura: a ficha registra só os três métodos que a síntese usa, o `getPointAt` e o `getUtoTmapping` do `Curve.js` e o `getFilmHeight` do `PerspectiveCamera.js`, e os trechos embaixo são eles, com os comentários; o resto dos dois arquivos não entra. Fonte curta, por isso nota de fato.

**Conferência lado a lado:** não se aplica; a licença permite a cópia e os trechos estão no mesmo arquivo.

## Em uma frase

No código do three.js r185, o `getPointAt(u)` da classe base das curvas troca o `u` por um `t` tirado do comprimento de arco antes de chamar o `getPoint(t)`, e o `getFilmHeight()` da câmera de perspectiva divide o `filmGauge` pelo aspecto só quando o quadro é mais largo que alto.

## A curva (`Curve.js`)

| Ponto | Fato |
|---|---|
| `getPointAt(u, optionalTarget)` | chama `getUtoTmapping(u)` e passa o `t` que volta ao `getPoint(t, optionalTarget)` |
| Comentário do `getPointAt` | ao contrário do `getPoint`, o método respeita o comprimento da curva, com amostras equidistantes |
| `getUtoTmapping(u, distance)` | devolve um fator na mesma faixa, de 0 a 1, que serve para amostrar pontos equidistantes da curva |
| O comprimento-alvo | `u` vezes o comprimento total; com `distance`, a própria distância |
| Como acha o `t` | busca binária nas somas acumuladas do `getLengths()` e, entre os dois pontos achados, a fração do segmento somada ao índice |
| Comentário sobre a precisão | daria para ter mais detalhe nos comprimentos ou interpolar entre dois pontos |

## A câmera (`PerspectiveCamera.js`)

| Ponto | Fato |
|---|---|
| `getFilmHeight()` | `this.filmGauge / Math.max( this.aspect, 1 )` |
| Quadro em retrato (`aspect` abaixo de 1) | pela fórmula, a altura é o `filmGauge` inteiro |
| Quadro em paisagem (`aspect` acima de 1) | pela fórmula, o `filmGauge` dividido pelo aspecto; o comentário de dentro diz que, em paisagem, o filme não fica todo coberto |
| Comentário do método | diz que, em paisagem, o resultado é igual ao `filmGauge`, e o `@return` diz "The film width" |

## O que a fonte recomenda

Para andar por uma curva com pontos equidistantes, o caminho é o `getPointAt(u)`, não o `getPoint(t)`, e o `getUtoTmapping` aceita também uma distância sobre a curva no lugar do `u`. Na câmera, a altura do filme só se reduz quando o quadro é mais largo que alto.

## Citações

- "Unlike {@link Curve#getPoint}, this method honors the length"
- "that can be ued to sample equidistant points"
- "film not completely covered in landscape format (aspect > 1)"

## Lacuna

Os três métodos não dizem como aplicar um ease sobre o `u`, nem como fazer duas curvas, a da posição e a do alvo, chegarem juntas a um mesmo ponto de parada; o comentário do `getFilmHeight` não diz o que vale em retrato, e o que ele diz da paisagem não é o que a fórmula dá.
