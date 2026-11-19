---
titulo: "PerspectiveCamera - Three.js Docs"
tipo: artigo
autor: "Colaboradores do three.js (mrdoob/three.js)"
url: "https://threejs.org/docs/pages/PerspectiveCamera.html"
publicado_em: null   # a página não traz data nem número de versão
capturado_em: 2026-11-12
licenca: "MIT (arquivo LICENSE do repositório mrdoob/three.js); a página da documentação é gerada dos comentários do código-fonte, que ela aponta na seção 'Source' (src/cameras/PerspectiveCamera.js). Que a licença do código cubra o texto da página é leitura do assistente, registrada na rodada (licencas.json), como na ficha 2026-11-12-threejs-docs-camera-curva-animacao-e-etiquetas; o integral está na url"
areas: [generative-media]
tags: [threejs, perspective-camera, field-of-view, focal-length, film-gauge, camera, aspect-ratio]
---

# Three.js: a câmera de perspectiva, com o campo de visão vertical e a lente pelo filme de 35 mm

Nota de fato: tabelas do que a página diz da `PerspectiveCamera`, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Ficha; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Página da documentação do three.js, https://threejs.org/docs/pages/PerspectiveCamera.html, baixada com curl em 2026-11-12. sha256 do HTML baixado (a pasta da rodada) (hash omitido). O título do HTML é "PerspectiveCamera - Three.js Docs". O texto extraído da rodada começa no construtor e deixa de fora o topo da página (a cadeia de herança, a frase de abertura e o exemplo de código), que foi lido no próprio HTML. Lida inteira. A página não diz a versão do three.js. Fonte curta, por isso nota de fato. O texto integral não vem neste repositório e se lê na url do frontmatter.

**Conferência lado a lado:** não se fez na captura, porque a licença permitia guardar o integral; neste repositório ele não vem, e se lê na url do frontmatter.

## Em uma frase

Página de referência da câmera de perspectiva do three.js, a que imita o olho humano e é a mais usada para renderizar cena 3D: o campo de visão é vertical e em graus, e a lente se pode dar em milímetros contra um filme de 35 mm no eixo maior.

## A câmera

| Ponto | Fato |
|---|---|
| Herança | EventDispatcher → Object3D → Camera → PerspectiveCamera |
| Projeção | perspectiva, feita para imitar o olho humano; o modo mais comum em cena 3D |
| Construtor | `new PerspectiveCamera(fov, aspect, near, far)` |
| Exemplo da página | `new THREE.PerspectiveCamera( 45, width / height, 1, 1000 )` |
| Depois de mudar qualquer propriedade | chamar `updateProjectionMatrix()` |

## As propriedades

| Propriedade | Padrão | Fato |
|---|---|---|
| `fov` | 50 | campo de visão vertical, de baixo a cima, em graus |
| `aspect` | 1 | em geral, a largura do canvas dividida pela altura |
| `near` | 0.1 | maior que 0 e menor que `far`; 0 não vale, ao contrário da `OrthographicCamera` |
| `far` | 2000 | maior que `near` |
| `zoom` | 1 | fator de zoom |
| `filmGauge` | 35 (mm) | tamanho do filme no eixo maior; só muda a matriz de projeção com `filmOffset` diferente de 0 |
| `filmOffset` | 0 | deslocamento horizontal fora do centro, na unidade do `filmGauge` |
| `focus` | 10 | distância do objeto para estéreo e profundidade de campo; só muda a projeção com `StereoCamera` |
| `view` | null | a janela do frustum; não se edita direto, só por `setViewOffset` e `clearViewOffset` |
| `isPerspectiveCamera` | true | só leitura, para testar o tipo |

## Os métodos

| Método | Fato |
|---|---|
| `getEffectiveFOV()` | o campo de visão vertical em graus, já com o `zoom` |
| `getFocalLength()` | a distância focal tirada do `fov` e do `filmGauge` |
| `setFocalLength(focalLength)` | põe o `fov` pela distância focal, no `filmGauge` atual; com o padrão 35, a lente se dá como numa câmera de 35 mm (full frame); lente e filme na mesma unidade |
| `getFilmWidth()` | largura da imagem no filme; em paisagem (`aspect` 1 ou mais), igual ao `filmGauge` |
| `getFilmHeight()` | altura da imagem no filme; a página repete a descrição da largura, inclusive "Returns: The film width" e o "igual ao `filmGauge`" em paisagem |
| `getViewSize(distance, target)` | largura e altura do retângulo visível a uma distância |
| `getViewBounds(distance, minTarget, maxTarget)` | os cantos inferior esquerdo e superior direito desse retângulo |
| `setViewOffset(fullWidth, fullHeight, x, y, width, height)` | uma janela dentro de um frustum maior, para várias janelas, monitores ou máquinas |
| Exemplo do `setViewOffset` | grade de 3 × 2 monitores de 1920 × 1080, uma chamada por monitor; a página diz que os monitores não precisam ser iguais nem estar em grade |
| `clearViewOffset()` | tira esse deslocamento da projeção |
| `updateProjectionMatrix()` | refaz a matriz de projeção; obrigatório depois de mudar propriedades |

## O que a fonte recomenda

O campo de visão se pensa na vertical, e quem prefere falar em lente usa `setFocalLength` em milímetros contra o filme de 35 mm, que cobre o eixo maior do quadro; a janela da câmera se muda só pelos métodos de deslocamento, e qualquer mudança de propriedade pede `updateProjectionMatrix()`.

## Citações

- "This projection mode is designed to mimic the way the human eye sees."
- "The vertical field of view, from bottom to top of view, in degrees."
- "Film size used for the larger axis. Default is 35 (millimeters)."

## Lacuna

A página não diz como o `fov` vertical se comporta num quadro em retrato (9:16) além de chamar o `filmGauge` de "eixo maior", não dá a fórmula entre lente e campo de visão, não fala de animar o `fov` (nem de efeito como o dolly zoom), e a descrição do `getFilmHeight` é cópia da do `getFilmWidth`, sem dizer quanto vale a altura.
