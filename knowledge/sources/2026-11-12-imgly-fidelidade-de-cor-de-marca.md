---
titulo: "Why AI image models miss your brand colors (IMG.LY GenAI Benchmarks)"
tipo: artigo
autor: "IMG.LY"
url: "https://img.ly/ai-benchmarks/findings/brand-color/"
publicado_em: null   # a página não traz data; o rodapé diz "© 2014 – 2026"
capturado_em: 2026-11-12
licenca: "protegida: a página não declara licença (valem os termos do site da IMG.LY); nota de fato em palavras próprias, sem o integral"
areas: [generative-media, content-design]
tags: [brand-color, hex, color-fidelity, ciede2000, image-generation, nano-banana, benchmark, interested-party]
---

# IMG.LY: nenhum modelo de imagem acerta o hex exato da marca

Nota de fato: tabelas do que a página registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela afirma e o que falta. Não há integral: a página é protegida.

**Proveniência.** Página de resultado do benchmark de IA generativa da IMG.LY sobre cor de marca, baixada em HTML em 12/11/2026 (`sha256` (hash omitido)), e lida no texto do `<main>` extraído do HTML (o texto que a rodada extraiu antes, só do `<article>`, trazia apenas os artigos relacionados): o resumo, a tabela dos 26 modelos, a seção do teste mais difícil, a conclusão e as chamadas para o produto. A lista de prompts e as notas por amostra ficam numa janela que o HTML não trazia aberta. Formato: nota de fato, por ser resultado de medição (`README.md` desta pasta, item 2).

**Quem fala. Parte interessada:** a IMG.LY vende o IMG.LY AI Editor, e a página fecha o benchmark dizendo que a lacuna se fecha numa etapa de edição com valores de cor exatos e que essa etapa é trabalho de um editor como o IMG.LY AI Editor, com links para a demonstração e para o produto e um formulário que pede e-mail para mandar um relatório.

**Data.** A página não traz data; a tabela se apresenta como "full 26-model run (pilot-0)".

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa do corpo e as células com texto corrido; a célula que só traz um fato fica fora. Corpo: 3 frases de prosa e 3 tabelas, todas as células de fato (a única de 8 palavras ou mais define a medida). Resultado: 0 das 3 unidades segue uma frase da fonte; "O que a fonte afirma" junta o resumo, a tabela e a conclusão numa frase própria. As três citações estão à parte. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: a parte traduzida não se mede), 0 frase colada, e a conta lado a lado é a conferência.

## Em uma frase

Resultado de um benchmark da IMG.LY que pediu a 26 modelos de imagem cores de marca em hex e mediu a distância de cor no que voltou: nenhum passa limpo, e a página conclui que a paleta se impõe depois de gerar, no editor que ela vende.

## Como mediu

| Item | Fato |
|---|---|
| Modelos | 26 |
| Testes com hex exato no prompt | 3 |
| Amostras por teste | 3 |
| Notas por modelo | 9 |
| Medida | CIEDE2000, entre o hex pedido e a cor dominante mais próxima na imagem |
| Escala | faixas da distância, em nota sobre 5 |
| Teste mais difícil | duotone de duas cores em hex (retrato) |
| Defeitos no duotone | matiz deslocado; degradê; terceira cor |
| Rodada | "full 26-model run (pilot-0)" |

## O que cada modelo tirou

| Posição | Modelo | Nota (de 5) | US$ por imagem |
|---|---|---|---|
| 1 | GPT Image 2 | 4,11 | 0,155 |
| 2 | GPT Image 2.5 Sunburst | 4,00 | 0,036 |
| 3 | GPT Image 2.5 Flare | 3,78 | 0,042 |
| 4 | Seedream 5.0 Pro | 3,78 | 0,135 |
| 5 | Nano Banana Pro | 3,67 | 0,150 |
| 6 | GPT Image 1.5 | 3,44 | 0,140 |
| 7 | Muse Image | 3,44 | 0,010 |
| 8 | Nano Banana 2 | 3,22 | 0,080 |
| 9 | Nano Banana 2.1 | 3,11 | 0,040 |
| 10 | FLUX 3 Image | 3,00 | 0,048 |
| 11 | Grok Imagine Image 2.0 | 2,89 | 0,060 |
| 12 | Nano Banana 2 Lite | 2,89 | 0,042 |
| 13 | Recraft V4.1 | 2,89 | 0,035 |
| 14 | Seedream 4.5 | 2,89 | 0,040 |
| 15 | FLUX.2 | 2,78 | 0,012 |
| 16 | Ideogram 3.0 | 2,78 | 0,060 |
| 17 | FLUX.2 [dev] Turbo | 2,67 | 0,008 |
| 18 | FLUX 3 Image Klein | 2,56 | 0,009 |
| 19 | Qwen Image 3.0 | 2,56 | 0,040 |
| 20 | Seedream 5.0 Lite | 2,56 | 0,035 |
| 21 | FLUX.2 [pro] | 2,33 | 0,030 |
| 22 | Stable Diffusion 1.5 | 2,22 | 0,002 |
| 23 | Luma Photon | 2,11 | 0,021 |
| 24 | Qwen-Image | 2,00 | 0,020 |
| 25 | Recraft V3 | 1,89 | 0,040 |
| 26 | Gemini 2.5 Flash Image | 1,67 | 0,040 |

| Resumo da página | Fato |
|---|---|
| Melhor nota | 4,11 de 5 |
| Abaixo de 3 | 16 de 26 |
| Média do campo | 2,9 |

## O que a fonte afirma

Para a página, a tabela prova que o prompt não basta para a cor exata em nenhum modelo de hoje, e a saída é dupla: o trabalho em que a cor manda vai aos modelos do topo, e a cor se acerta depois, num editor com kit de marca, que é o produto que ela vende.

## Citações

- "Close-enough color is easy; the color in your brand book is not." (resumo)
- "Prompting with hex codes improves the odds but never guarantees the value." (conclusão)
- "Enforce the palette after generation, not in the prompt." (conclusão)

## Lacuna

A página não traz data, não mostra os hex pedidos nem as distâncias de cada amostra no HTML baixado, não diz quantas cores por teste além do duotone, não separa estilo (foto, ilustração, traço) e não trata de personagem; é uma rodada piloto, de nove amostras por modelo.
