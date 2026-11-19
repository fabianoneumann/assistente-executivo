---
titulo: "Motion (Carbon Design System, Elements: Motion overview)"
tipo: artigo
autor: "IBM, Carbon Design System"
url: "https://carbondesignsystem.com/elements/motion/overview/"
publicado_em: null
capturado_em: 2026-11-10
areas: [generative-media, content-design]
tags: [motion-design, easing, duration, animation, design-systems, accessibility]
licenca: "página sem licença de conteúdo declarada no texto lido; ficha em palavras próprias, sem o integral"
---

# IBM Carbon: o guia de movimento do sistema de design

Ficha do guia de movimento do Carbon, o sistema de design da IBM, lido no HTML baixado em 2026-11-10 (a página não traz data). Guia de interface, não de vídeo. A ficha reagrupa o guia em três perguntas (quando mover, como mover, como conferir), fora da ordem das seções da página.

## Quando mover

Só onde o movimento cumpre uma função: confirmar que uma ação foi feita, revelar informação aos poucos para aliviar a carga, puxar o olho para uma chamada. O trabalho começa antes da animação, nos objetivos do produto, na hierarquia de informação da tela e na jornada; depois se escolhe o registro, se prototipa e se testa. Há dois registros, que o guia liga à dualidade entre pessoa e máquina: o **produtivo**, ágil e quieto, para quem está no meio de uma tarefa; e o **expressivo**, enfático, para os poucos momentos em que o próprio movimento tem algo a dizer (abrir uma página, a ação principal, um alerta), e que também serve de pausa no ritmo do produtivo. Para quem não percebe ou não tolera movimento, ou usa aparelho que não o roda liso, a mensagem tem de funcionar parada, com alternativa às transições e versão simplificada no celular e no tablet.

## Como mover

| Situação | Curva | Produtivo | Expressivo |
|---|---|---|---|
| O elemento continua na tela enquanto muda (cresce, troca de lugar) | padrão | `(0.2, 0, 0.38, 0.9)` | `(0.4, 0.14, 0.3, 1)` |
| O elemento chega | entrada | `(0, 0, 0.38, 0.9)` | `(0, 0, 0.3, 1)` |
| O elemento vai embora de vez (acelera ao sair) | saída | `(0.2, 0, 1, 0.9)` | `(0.4, 0.14, 1, 1)` |
| O elemento sai mas fica à mão, como um painel lateral | padrão, que freia ao sair | | |

O guia rejeita o linear, que considera artificial, e a curva que só enfeita; dá também os valores de velocidade para o After Effects. O texto lido descreve o efeito da curva de saída e da padrão, não o da de entrada.

**Tempo:** o expressivo é mais lento que o produtivo, e o percurso maior pede mais tempo, numa escala de duração que o Carbon chama de não linear, para a percepção ficar consistente em qualquer distância (há um gerador para calcular o caso). Os seis valores prontos vão de 70 ms e 110 ms (botão, chave, esmaecer) e 150 ms (pequena expansão) a 240 ms (expansão, aviso do sistema), 400 ms (expansão grande, notificação importante) e 700 ms (escurecer o fundo).

## Como conferir

Cinco perguntas: o movimento tem um porquê? Responde sem atraso (90 a 120 ms nas microinterações)? Nas transições grandes, há algo que segue de uma tela à outra e conduz o olho? Os movimentos parentes conversam entre si e resistem em telas de todo tamanho, inclusive no celular, onde o sutil se perde? E passaria sem ser notado? Se a pessoa comum repara demais, é sinal para cortar ou reduzir.
