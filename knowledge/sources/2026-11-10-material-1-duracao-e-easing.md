---
titulo: "Duration & easing (Material Design 1, Motion)"
tipo: artigo
autor: "Google, Material Design"
url: "https://m1.material.io/motion/duration-easing.html"
publicado_em: null
capturado_em: 2026-11-10
areas: [generative-media, content-design]
tags: [motion-design, easing, duration, animation, design-systems]
licenca: "sem licença de conteúdo declarada no texto lido; ficha em palavras próprias, sem o integral"
---

# Material Design 1: duração e easing

Ficha da página de duração e easing do Material Design 1, lida no HTML baixado em 2026-11-10. A própria página avisa que o Material 1 saiu de manutenção e aponta o Material 3, cuja página equivalente (`m3.material.io/styles/motion/easing-and-duration/applying-easing-and-duration`) não abriu sem JavaScript. Guia de interface, não de vídeo. A ficha junta curva e duração por tipo de elemento, fora da ordem da página.

## Por tipo de elemento, no celular

| O elemento | Curva (`cubic-bezier`) | Tempo de referência |
|---|---|---|
| Entra na tela: chega a toda velocidade e vai freando até parar | desaceleração `(0.0, 0.0, 0.2, 1)` | 225 ms |
| Sai de vez | aceleração `(0.4, 0.0, 1, 1)` | 195 ms, menos que a entrada, porque pede menos atenção |
| Muda de lugar ou de tamanho sem sair | padrão `(0.4, 0.0, 0.2, 1)`, a mais comum | perto de 300 ms; perto de 375 ms se for de tela inteira ou complexo |
| Sai mas pode voltar | sharp `(0.4, 0.0, 0.6, 1)`, simétrica | |

A página dá também os valores das curvas para Android, iOS e After Effects.

## O que move os números

- **O percurso:** distância maior ou mudança grande de área, mais tempo; percurso curto, menos, senão parece lento. Em tela maior o mesmo movimento cobre mais chão e chega a uma velocidade de pico maior, por isso o tablet leva cerca de 30% a mais (300 ms viram 390) e o vestível, cerca de 30% a menos (210 ms).
- **O desktop é a exceção:** de 150 a 200 ms e mais simples, porque ali a transição chama menos atenção e precisa responder na hora; e, na web sem aceleração por GPU, a animação longa perde quadros, o que a curta esconde.
- **O teto:** passar de 400 ms tende a parecer lento.

## O princípio por trás

Duração boa é a que não faz ninguém esperar e ainda deixa a mudança ser entendida, puxada para o curto porque transição se repete muito. E a curva natural muda de velocidade aos poucos, acelerando e freando em ritmos diferentes: a assimetria é o que tira a cara de máquina.
