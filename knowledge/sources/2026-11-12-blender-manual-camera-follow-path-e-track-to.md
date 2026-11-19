---
titulo: "Blender Manual: Cameras, Follow Path Constraint e Track To Constraint"
tipo: artigo
autor: "Blender Documentation Team (manual do Blender)"
url: "https://docs.blender.org/manual/en/latest/render/cameras.html"
publicado_em: 2026-11-12   # rodapé das três páginas: "Last updated on 2026-11-12"; manual 5.3 (latest)
capturado_em: 2026-11-12
licenca: "CC BY-SA 4.0 (rodapé de cada página: 'This page is licensed under a CC-BY-SA 4.0 Int. License'); o integral está na url"
areas: [generative-media]
tags: [blender, camera, camera-path, camera-rig, field-of-view, focal-length, depth-of-field, safe-area, composition, dolly-zoom, constraints]
---

# Blender: a câmera, o trilho por curva (Follow Path) e a mira num alvo (Track To)

Nota de fato: tabelas do que as três páginas do manual dizem, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Ficha; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Três páginas do manual do Blender 5.3, baixadas com curl em 2026-11-12, com o texto extraído do HTML:

| Página | URL | sha256 do HTML baixado |
|---|---|---|
| "Cameras - Blender 5.3 Manual" | https://docs.blender.org/manual/en/latest/render/cameras.html | (hash omitido) |
| "Follow Path Constraint - Blender 5.3 Manual" | https://docs.blender.org/manual/en/latest/animation/constraints/relationship/follow_path.html | (hash omitido) |
| "Track To Constraint - Blender 5.3 Manual" | https://docs.blender.org/manual/en/latest/animation/constraints/tracking/track_to.html | (hash omitido) |

Títulos conferidos no HTML de cada página. Lidas inteiras; a seção "Example" das duas restrições é só um vídeo embutido (video.blender.org), que não foi visto, e as imagens não foram vistas. As páginas a que elas remetem (navegação da câmera no viewport, câmera panorâmica, Damped Track, Clamp To) não foram abertas. Três páginas curtas de documentação, por isso nota de fato. O texto integral não vem neste repositório e se lê na url do frontmatter.

**Conferência lado a lado:** não se fez na captura, porque a licença permitia guardar o integral; neste repositório ele não vem, e se lê na url do frontmatter.

## Em uma frase

O manual do Blender descreve a câmera (lente, profundidade de campo, sensor, áreas seguras e guias de composição) e as duas restrições que fazem o trilho e a mira de um plano: a Follow Path põe o objeto numa curva, por quadro ou por fração de 0 a 1, e a Track To o mantém apontado para um alvo.

## A câmera: lente

| Ponto | Fato |
|---|---|
| Tipos de lente | Perspective; Orthographic; Panoramic (Cycles e EEVEE, com limites no EEVEE); Custom (só Cycles, por código OSL) |
| Perspective | o distante fica menor e as paralelas convergem, como no mundo real |
| Focal Length / Field of View | lente longa, campo menor (mais zoom); lente curta, campo maior |
| Exemplos de lente das imagens | 35 mm e 210 mm |
| Lens Unit | milímetros ou ângulo do campo de visão |
| Dolly zoom, pela dica da página | baixar a distância focal enquanto a câmera anda para o objeto, ou o contrário |
| Orthographic | tamanho real a qualquer distância; paralelas seguem paralelas |
| Orthographic Scale | o único ajuste da ortográfica: o tamanho aparente dos objetos |
| Shift | move os pontos de fuga; equivale a renderizar com campo maior e recortar fora do centro |
| Shift contra girar a câmera | com shift, as horizontais seguem horizontais; girando o objeto câmera, elas entortam |
| Exemplo de shift das imagens | horizontal de 0,330 |
| Clip Start, End | o intervalo em que o objeto aparece direto; fora dele ainda influi pela luz rebatida |
| Precisão do clip | no viewport, limites curtos garantem precisão de rasterização; no ray tracing, valores extremos são seguros |

## A câmera: foco e corpo

| Ponto | Fato |
|---|---|
| Focus Object | o objeto que define o ponto de foco; desliga a distância |
| Focus Distance | a distância de foco quando não há objeto |
| Conta-gotas | E sobre a Focus Distance, depois clique no viewport |
| F-Stop | valor menor, profundidade de campo mais forte |
| Blades | lâminas do diafragma; o bokeh começa com 3 (triangular) |
| Ratio | 1,0 sem distorção; abaixo, distorção horizontal; acima, vertical (bokeh anamórfico) |
| Presets | corpos de câmeras reais |
| Sensor Fit Auto | sensor quadrado pelo lado maior da resolução |
| Sensor Fit Horizontal | a largura do sensor à mão; a altura sai da proporção |
| Sensor Fit Vertical | a altura do sensor à mão; a largura sai da proporção |
| Size / Width, Height | outro jeito de controlar o campo de visão; serve a casar com câmera e lente reais, como no motion tracking |

## A câmera: o que aparece no quadro

| Ponto | Fato |
|---|---|
| Title Safe (Graphics Safe) | margem para texto e gráfico importantes |
| Action Safe | margem para a ação e os personagens; também afasta elementos da borda |
| Por que existem | overscan das TVs antigas; nas telas digitais não há overscan, mas seguem como boa prática e podem ser exigidas em broadcast |
| Margens padrão | da norma EBU |
| Center-Cut | áreas seguras para outra proporção; padrão: 4:3 dentro de 16:9 |
| Onde se ligam | vistas de câmera e do Sequencer, com os mesmos valores |
| Composition Guides | terços; centro; diagonal; proporção áurea (cerca de 0,618 de cada lado); triângulo áureo A e B; triângulo harmônico A e B |
| Passepartout | escurece o que está fora do campo da câmera; opaco por inteiro, acelera o render dentro da vista |
| Background Images | imagem, sequência, vídeo ou Movie Clip atrás ou na frente da cena, com Stretch, Fit ou Crop |

## Follow Path: o trilho por uma curva

| Ponto | Fato |
|---|---|
| O que faz | põe um objeto ou osso sobre uma curva; pode girá-lo na direção dela |
| Usos dados | câmera em trilho, veículo na estrada, caixa na esteira |
| Posição por quadro | a Evaluation Time da curva, com Offset opcional (positivo leva o dono para trás na curva, negativo para a frente) |
| Posição por fração | Offset Factor, de 0 (começo) a 1 (fim), com Fixed Position ligado |
| Fixed Position | ignora a Evaluation Time; o dono ainda anda se o Offset Factor for animado |
| Animate Path | anima a Evaluation Time para ser sempre igual ao quadro atual da cena; sem ele, a curva fica parada |
| Follow Curve | gira o dono pela Forward Axis (alinhada à tangente) e pela Up Axis (o mais perto possível do Z global) |
| Eixos iguais | a restrição para e o ícone fica vermelho |
| Eixo negativo | o dono aponta para o lado contrário |
| Curve Radius | escala o dono pelos raios dos pontos de controle |
| Deslocamento | a posição e a rotação do dono no mundo viram deslocamento: no espaço local da curva, ou no do ponto da curva com Follow Curve; a escala da curva multiplica |
| Para ficar exato na curva | zerar posição e rotação do dono (Alt-G e Alt-R) |
| Atalho | selecionar o objeto, depois a curva, Ctrl-P, Path Constraint |
| Com mira | combinar com uma restrição de tracking, por exemplo para a câmera andar apontada para um objeto |

## Track To: a mira num alvo

| Ponto | Fato |
|---|---|
| O que faz | aponta um objeto ou osso para um alvo e gira para um eixo local ficar para cima |
| Nome em outros programas | "Look At" ou "Aim" |
| Track Axis | o eixo local que aponta para o alvo; em osso, em geral Y; negativo aponta para longe |
| Up | o eixo local que fica para cima no mundo |
| Eixos iguais | a restrição para e o ícone fica vermelho |
| Target Z | o Up segue o Z do alvo em vez do global |
| Instabilidade | com o dono quase em cima do alvo, o giro em torno do eixo de mira fica instável; a página indica a Damped Track |

## O que a fonte recomenda

Para o plano em trilho, a câmera vai à curva pela Follow Path, com a posição presa ao quadro (Animate Path) ou a uma fração animada de 0 a 1, e a mira vem de uma segunda restrição, a Track To, cujo eixo de cima não pode ser o mesmo da mira e que se troca pela Damped Track quando a câmera passa por cima do alvo. Na câmera, a lente muda o campo de visão (e, junto com o avanço, dá o dolly zoom), o shift endireita a perspectiva sem girar, e as áreas seguras e as guias ajudam a compor.

## Citações

- "Use cases include cameras on rails, vehicles on roads, boxes on conveyor belts, and so on."
- "It’s typically called “Look At” or “Aim” in other 3D software."
- "Using lens shift is equivalent to rendering an image with a larger FOV and cropping it off-center."

## Lacuna

Nenhuma das três páginas fala de velocidade ao longo da curva (se a Evaluation Time e o Offset Factor andam por comprimento ou pelos pontos), de easing no trilho, de tremor de câmera ou de render pela linha de comando. A página da câmera não diz como o Sensor Fit Auto se comporta num quadro em retrato além de "o lado maior da resolução", e as das restrições deixam o exemplo só no vídeo.
