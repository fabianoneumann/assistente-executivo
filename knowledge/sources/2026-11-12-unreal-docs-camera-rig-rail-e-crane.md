---
titulo: "Camera Rigs"   # título da página; o do HTML é "Camera Jibs and Dollies in Unreal Engine | Unreal Engine 5.9 Documentation"
tipo: artigo
autor: "Epic Games (documentação do Unreal Engine)"   # página da documentação, sem assinatura de pessoa
url: "https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine"
publicado_em: 2025-03-25   # não aparece na página; vem do metadado updated_at da revisão, no JSON embutido do HTML ("2025-03-25T07:19:33.531Z"), e é a data da última revisão, não a da primeira publicação
capturado_em: 2026-11-12
licenca: "licença não encontrada na página (nem rodapé de copyright no HTML baixado); tratada como protegida até conferir; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unreal-engine, sequencer, camera-rig, camera-path, spline, camera-movement, camera-animation, crane-shot, tracking-shot]
---

# Unreal: o trilho e a grua virtuais, animados no Sequencer

Nota de fato: tabelas do que a página da documentação diz sobre os dois rigs de câmera do Unreal, o Camera Rig Rail e o Camera Rig Crane, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a licença não aparece na página.

**Proveniência.** Página da documentação do Unreal Engine 5.9, https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine, baixada com curl em 2026-11-12 e lida no texto extraído do HTML, conferido no próprio HTML. A página se intitula "Camera Rigs", com o subtítulo "Film with real-world techniques in Unreal Engine by using Camera Rigs."; o título do HTML é "Camera Jibs and Dollies in Unreal Engine | Unreal Engine 5.9 Documentation | Epic Developer Community". sha256 (hash omitido), que mede o texto do bloco `<main>` ou `<article>` sem tags, script e estilo (não o HTML inteiro); Wayback `http://web.archive.org/web/20260129073957/https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine`. Cobertura: a página inteira (introdução, pré-requisitos, as seções do trilho e da grua, o uso no Sequencer e a combinação dos dois); ficaram fora o menu, o índice lateral e os links do fórum. As imagens da página não foram vistas. Texto de quem faz a ferramenta, sobre a própria ferramenta. Fonte curta (umas 940 palavras), por isso nota de fato.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática, contra o texto extraído: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), com "unidades medidas: 25 (15 de prosa, 10 de célula com texto)" e "coladas: 0 de 25 (0%); trechos de 3 ou mais seguidas: 0". Na leitura lado a lado das mesmas 25 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a célula que só traz um fato fica fora, e as 10 frases da linha do formato, da proveniência e desta conferência, a nota sobre o negrito da citação e as duas frases da lacuna não seguem frase nenhuma. Resultado: 11 de 25 (a frase de "Em uma frase" e as 10 células com texto, que vertem cada uma uma propriedade ou um passo); não segue a frase da recomendação, que junta o trilho, a grua, a rotação e o Sequencer. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 5, na tabela da montagem (dos pré-requisitos à combinação de trilho e grua), que são os passos do método na ordem da página; na tabela de comparação, que alterna trilho e grua, a maior é de 2, e a página não tem texto de recomendação além da frase da combinação, vertida numa célula e citada.

## Em uma frase

Página da documentação da Epic sobre os dois rigs de câmera do Unreal, o trilho (Camera Rig Rail, que imita o dolly e faz o travelling) e a grua (Camera Rig Crane, que imita o braço de grua), aos quais se prende uma Cine Camera e cujas propriedades se animam com keyframes no Sequencer.

## Os dois rigs, lado a lado

| Ponto | Trilho (Camera Rig Rail) | Grua (Camera Rig Crane) |
|---|---|---|
| Aparelho real que imita | dolly sobre trilho | braço de grua (boom, jib) |
| Plano que faz | tracking shot (travelling) | crane shot |
| O que se anima | Current Position on Rail, presa entre 0 (começo do trilho) e 1 (fim) | Crane Pitch (vertical), Crane Yaw (horizontal) e Crane Arm Length |
| Unidade | fração do trilho | o braço em centímetros; "2m" digitado vira 200 cm |
| Forma | uma Blueprint Spline: reta por padrão, com pontos lineares nas pontas | o braço gira nos dois eixos e se estende |
| Mudar a forma | mover os pontos das pontas (comprimento e direção) e as tangentes (curva); "Add Spline Point Here" no botão direito | — |
| Rotação da câmera, por padrão | independente da do carrinho | independente do pitch e do yaw do braço |
| Travar a rotação | Lock Orientation to Rail: a rotação passa a ser relativa à do carrinho | Lock Mount Pitch ou Lock Mount Yaw: relativa ao braço naquele eixo |
| Prévia no viewport | Show Rail Visualization (desligado, fica só a spline); Preview Mesh Scale | — |

## Montagem e animação

| Passo | Fato |
|---|---|
| Antes | saber usar o Cine Camera Actor, com um já no Level, e saber criar animação de câmera no Sequencer |
| Pôr o rig | aba Cinematic do painel Place Actors, arrastando para o viewport |
| Prender a câmera | no World Outliner, arrastar a câmera sobre o rig; depois disso ela ainda se ajusta |
| Animar | no Sequencer: a faixa do rig e a da câmera presa, as propriedades do rig por "+ Track", categoria Properties, e keyframes nas duas |
| Trilho e grua juntos | prender o trilho à grua, pelos mesmos passos usados para prender a câmera; as propriedades dos dois se animam juntas |

## O que a fonte recomenda

O movimento se monta como num set: a câmera se prende ao rig e é o rig que anda, com a posição no trilho de 0 a 1 ou o pitch, o yaw e o braço da grua; a rotação da câmera fica solta a menos que se trave no carrinho ou no braço, e o plano sai de keyframes no Sequencer, tanto no rig quanto na câmera, com o trilho preso à grua quando o plano pede os dois.

## Citações

- "The value range is clamped between 0 and 1, where 0 is the start point of the track, and 1 is the end point." (o HTML marca os números e as pontas em negrito)
- "By default, the camera's orientation is set independently from the orientation of the dolly."
- "Crane and rail properties can be animated together to allow for more freedom and realism in your shot creation."

## Lacuna

A página não diz como a posição de 0 a 1 se distribui pelo trilho (se por comprimento ou pelos pontos da spline), nem como dar aceleração e freio ao movimento (curva de keyframe, interpolação); não fala de apontar a câmera para um alvo enquanto o rig anda, não dá valores padrão nem limites de pitch, yaw e braço, e não trata de render nem de tremor de câmera. As versões do Unreal em que os rigs existem não são ditas além do 5.9 do título.
