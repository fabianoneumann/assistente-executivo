---
titulo: "Spline Dolly"
tipo: artigo
autor: "Unity Technologies (manual do pacote Cinemachine)"   # página do manual, sem assinatura de pessoa
url: "https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachineSplineDolly.html"
publicado_em: null   # a página não traz data; o título do HTML dá a versão do pacote, "Cinemachine | 3.1.7"
capturado_em: 2026-11-12
licenca: "protegido (rodapé: 'Copyright © 2026 Unity Technologies', com link para os termos de uso); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unity, cinemachine, camera-path, spline, camera-movement, camera-animation, damping, interested-party]
---

# Cinemachine: a câmera presa a uma spline, posta por valor ou levada sozinha

Nota de fato: tabelas do que a página do manual diz sobre o comportamento Spline Dolly, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Página do manual do Cinemachine 3.1 (pacote da Unity), https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachineSplineDolly.html, baixada com curl em 2026-11-12 e lida no texto extraído do HTML, conferido no próprio HTML. O título do HTML é "Spline Dolly | Cinemachine | 3.1.7", e a página abre com o título "Spline Dolly". sha256 (hash omitido), que mede o texto do bloco `<main>` ou `<article>` sem tags, script e estilo (não o HTML inteiro); Wayback `http://web.archive.org/web/20261103121825/https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachineSplineDolly.html`. Cobertura: a página inteira (a introdução, a dica sobre o ponto mais próximo e a tabela de propriedades); ficaram fora o menu e o rodapé. Texto de quem faz a ferramenta, sobre a própria ferramenta. Fonte curta (umas 690 palavras), por isso nota de fato.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática, contra o texto extraído: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), com "unidades medidas: 29 (15 de prosa, 14 de célula com texto)" e "coladas: 0 de 29 (0%); trechos de 3 ou mais seguidas: 0". Na leitura lado a lado das mesmas 29 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a célula que só traz um fato fica fora, e as 10 frases da linha do formato, da proveniência e desta conferência não seguem frase nenhuma. Resultado: 16 de 29 (a frase de "Em uma frase", as 14 células com texto, que vertem cada uma a descrição de uma propriedade ou da dica, e a primeira frase da recomendação, que refaz a dica); não seguem a segunda frase da recomendação, que junta o amortecimento e a rotação, e as duas da lacuna. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 5, duas vezes (de "Em uma frase" à célula do amortecimento do modo automático, e da célula de Position às do amortecimento em X e Y), em descrição de propriedade, que é método e dado; no único texto de recomendação da página, a dica da spline em arco, a maior é de 2, sem trecho colado de 3 ou mais.

## Em uma frase

Página do manual da Unity sobre o Spline Dolly, o comportamento de posição do Cinemachine que prende a câmera a uma spline: a posição nela se dá por um valor (que se anima à mão) ou por um modo automático, com velocidade fixa ou buscando o ponto da spline mais perto do alvo.

## O comportamento

| Ponto | Fato |
|---|---|
| Tipo | comportamento de controle de posição da CinemachineCamera |
| O que faz | a câmera só anda sobre uma spline definida antes |
| Onde ela fica | dado pela propriedade Position |
| Duas formas de mover | animar Position à mão; ligar o Automatic Dolly |
| Modos automáticos | velocidade fixa; ponto mais próximo do Tracking Target; um modo próprio escrito pelo usuário |

## Como ela anda sozinha

| Propriedade | Opção | Fato |
|---|---|---|
| Automatic Dolly | — | chave do movimento automático |
| Method | None | sem automação: quem usa põe a posição (a página a chama de PathPosition aqui) |
| Method | Fixed Speed | velocidade constante, escolhida por quem usa |
| Method | Nearest Point To Target | o ponto da spline mais perto do alvo; exige um Tracking Target e aceita deslocamento a partir desse ponto |
| Method | próprio | extensão pela classe `SplineAutoDolly.ISplineAutoDolly` |
| Damping | — | o peso da câmera ao buscar o ponto: número baixo, câmera ágil; alto, câmera pesada e lenta |

## Para onde ela olha

| Propriedade | Opção | Fato |
|---|---|---|
| Camera Rotation | efeito | decide também o enquadramento, porque a mira do Cinemachine respeita o Up |
| Camera Rotation | Default | rotação e Up intocados; o Up global se troca no World Up Override do Cinemachine Brain |
| Camera Rotation | Path | Up e tangente da spline no ponto |
| Camera Rotation | Path No Roll | como Path, sem giro (roll) |
| Camera Rotation | Follow Target | Up e rotação do transform do alvo |
| Camera Rotation | Follow Target No Roll | como Follow Target, sem giro |
| Angular Damping | — | o peso da câmera ao buscar a rotação; só com Camera Rotation fora do Default |

## Onde a câmera fica na spline

| Propriedade | Opção | Fato |
|---|---|---|
| Spline | — | a spline por onde a câmera anda |
| Position | — | o lugar da câmera na spline; anima-se à mão ou fica com o Automatic Dolly |
| Position Units | Knot | conta por nós: 0 é o primeiro nó, 1 o segundo, e o valor fracionário fica entre eles |
| Position Units | Distance | conta em unidades de distância, a partir de 0 no começo |
| Position Units | Normalized | 0 no começo, 1 no fim |

## Fora da linha: deslocamento e amortecimento por eixo

| Eixo, no espaço local da spline | Spline Offset | Damping de posição |
|---|---|---|
| X | perpendicular à spline | alisa defeitos do caminho; pode tirar a câmera da linha |
| Y | o Up da spline | alisa defeitos do caminho; pode tirar a câmera da linha |
| Z | paralelo à spline | não tira a câmera da linha |
| Uso | afastar a câmera da própria linha | — |

## A dica da página

| Ponto | Fato |
|---|---|
| Quando vale | com o modo Nearest Point To Target |
| Forma de risco | spline em arco em volta de um ponto |
| Caso extremo dado | spline circular com o alvo no centro |
| Por que falha | todos os pontos ficam à mesma distância do alvo, e o ponto mais próximo fica instável |
| Efeito | o alvo anda pouco e a câmera salta muito na spline |

## O que a fonte recomenda

A forma da spline se escolhe pensando no modo automático: o que segue o alvo pelo ponto mais próximo pede um trilho que não abrace o alvo em arco. Para alisar um caminho imperfeito, o amortecimento nos eixos de lado e de cima ajuda, mas pode deslocar a câmera da linha, o que o do eixo do trilho não faz; e a rotação, quando não fica no padrão, decide também o enquadramento, porque a mira obedece ao Up que ela define.

## Citações

- "The closest point on the spline is unstable because all points on the circular spline are equally close to the target."
- "Smaller values produce a faster-moving camera, larger values produce a heavier, more slowly-moving camera."
- "Z represents the axis that is parallel to the spline. This won't move the camera off the spline."

## Lacuna

A página não dá valores padrão nem unidades para nenhuma propriedade (o amortecimento não diz se é em segundos, a velocidade fixa não diz em que unidade por tempo), não fala de aceleração ou de curva de velocidade no modo de velocidade fixa, não mostra como criar ou editar a spline e não trata de como animar Position numa Timeline. O texto chama a mesma propriedade de Position na tabela e de PathPosition no modo None, sem dizer se é o nome da API.
