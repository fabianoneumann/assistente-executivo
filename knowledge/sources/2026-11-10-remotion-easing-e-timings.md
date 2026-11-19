---
titulo: "Easing; Timings (Remotion docs)"
tipo: artigo
autor: "Remotion"
url: "https://www.remotion.dev/docs/easing"
publicado_em: null
capturado_em: 2026-11-10
areas: [generative-media]
tags: [remotion, easing, spring, transitions, video-as-code]
licenca: "documentação sem licença de conteúdo declarada no texto lido; ficha em palavras próprias, sem o integral"
---

# Remotion: o módulo Easing e os timings de transição

Ficha de duas páginas da documentação do Remotion, lidas no HTML baixado em 2026-11-10: `docs/easing` e `docs/transitions/timings` (`https://www.remotion.dev/docs/transitions/timings`). Nenhuma traz data.

## Easing (com `interpolate()`)

- O módulo Easing implementa as funções de easing comuns, para usar com `interpolate()`; a página aponta easings.net para ver as curvas.
- **Prontas:** `back` (recua um pouco antes de avançar), `bounce` (quica), `ease` (inércia básica), `elastic` (mola simples) e `spring` (mola com física).
- **Padrão:** `linear`, `quad`, `cubic`; `poly(n)` para potências maiores (quarta, quinta).
- **Matemáticas:** `bezier` (curva de Bézier cúbica), `circle`, `sin`, `exp`.
- **Modificadores:** `in` roda a função para a frente, `out` ao contrário, `inOut` a torna simétrica.
- **Exemplo da página:** a escala de um fundo de 0 a 1 entre os quadros 0 e 100 com `Easing.bezier(0.8, 0.22, 0.96, 0.65)` e extrapolação presa (`clamp`) dos dois lados.
- Cada função tem a fórmula e o link da curva (por exemplo, `linear` é f(t) = t, posição proporcional ao tempo; `ease` lembra um objeto que acelera devagar até a velocidade; `elastic(bounciness)`, uma mola oscilando).

## Timings de transição (`@remotion/transitions`)

- Um timing, junto com uma apresentação, forma uma transição.
- **Prontos:** `springTiming()` (transição com `spring()`) e `linearTiming()` (linear, com easing opcional); dá para escrever um timing próprio.
- A duração de uma transição sai de `getDurationInFrames()`: o exemplo da página, `springTiming({config: {damping: 200}})` a 30 quadros por segundo, dura 23 quadros.
