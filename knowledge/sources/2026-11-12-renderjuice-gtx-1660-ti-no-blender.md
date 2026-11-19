---
titulo: "GTX 1660 Ti for Blender: Benchmarks, VRAM & Price"
tipo: artigo
autor: "Renderjuice"   # meta author da página; sem assinatura de pessoa
url: "https://renderjuice.com/gpus/gtx-1660-ti-for-blender"
publicado_em: null   # a página não traz data de publicação; o preço diz "Checked Nov 2, 2026", as fontes de energia "Checked Sep 23, 2026", e os dados embutidos no HTML trazem updatedAt 2026-11-09
capturado_em: 2026-11-12
licenca: "protegido (rodapé: '© Renderjuice 2026 All rights reserved.'); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [blender, cycles, optix, gpu, nvidia, vram, hardware, benchmark, render-time, cloud-rendering]
---

# Renderjuice: a GTX 1660 Ti no Blender, com os tempos de Cycles da Blender Open Data

Nota de fato: tabelas do que a página registra, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Página de catálogo de placas da Renderjuice, https://renderjuice.com/gpus/gtx-1660-ti-for-blender, baixada em HTML em 2026-11-12 e lida no texto extraído do HTML, conferido no HTML; sha256 do texto do bloco `<main>`/`<article>`, sem tags, script e estilo, registrado na rodada: (hash omitido) (conferido de novo no HTML do a cópia de trabalho; o do arquivo inteiro, que muda a cada download, é (hash omitido)). Wayback: http://web.archive.org/web/20260418050554/https://www.renderjuice.com/gpus/gtx-1660-ti-for-blender (captura de abril de 2026, não aberta). Título conferido no `<title>` e no `og:title`. Lido o texto inteiro da página, do comparador ao fim da lista de alternativas, e, no HTML, os dados embutidos do teste da Classroom; as ofertas, o comparador e as fontes citadas (Blender Open Data, NVIDIA, TechPowerUp) não foram abertos.

**Quem fala.** A Renderjuice vende render do Blender em GPU na nuvem, e a página traz ofertas de compra da própria placa e um chamado para o serviço dela.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). O `parafrase.py` contra o texto extraído saiu com o código 3 (ficha em português, fonte em inglês): 18 unidades medidas (14 de prosa, 4 de célula com texto); fora da conta, 130 células de fato, 18 de cabeçalho e 5 frases curtas demais para medir; 1 colada de 18 (6%), a célula "VRAM recomendada do Blender para Windows e Linux"; 0 trecho de 3 ou mais seguidas. Pela conta lado a lado, sobre as mesmas unidades, 7 de 18 seguem a fonte: a frase de quem fala, o "Em uma frase", as quatro células com texto (a origem dos tempos, a ressalva sobre energia, a VRAM recomendada, a dependência de driver e memória) e a frase da recomendação, que junta o destaque, os contras e o conselho de compra da página. A maior sequência de unidades seguidas que seguem a fonte tem 6 (do "Em uma frase" à recomendação); nela, a ordem volta para trás entre a célula dos tempos e a da energia, e o texto argumentativo da página (a avaliação e a recomendação) cabe em duas unidades, sem trecho colado. Ficam fora da conta de "segue" o resto da proveniência, esta linha e a lacuna.

## Em uma frase

Ficha de placa de uma empresa que vende render do Blender na nuvem, com a pontuação e os tempos de Cycles da GTX 1660 Ti tirados da Blender Open Data, as especificações, o preço e a avaliação de que os 6 GB ficam abaixo do recomendado pelo Blender.

## Desempenho no Blender

| Item | Valor |
|---|---|
| Pontuação Blender Cycles | 685 |
| Contra a RTX 4090 | 16,9× mais lenta |
| Origem | Blender Open Data |
| Versão do Blender | 5.2.0 |
| Backend | OptiX |
| Execuções | 31 |
| Suporte de render | OptiX, CUDA |

| Cena de benchmark | Amostras | Tempo estimado de um quadro |
|---|---|---|
| Junkshop | 240 | 68,88 s |
| Monster | 256 | 72,82 s |
| Classroom | 300 | 115,65 s |

| Condição dos tempos | Fato |
|---|---|
| O que estimam | um quadro de cada cena de benchmark |
| De onde vêm | as mesmas execuções, versão e backend da pontuação |
| Margem somada | 19% de "estimation buffer" |
| Projeto real | tempo varia |
| Versões diferentes do Blender | resultados talvez não comparáveis diretamente |
| Leitura | menor é mais rápido |

| Dado embutido no HTML, fora do texto exibido | Valor |
|---|---|
| Pontuação com casas | 685,33 |
| Método da pontuação | mediana das submissões completas |
| Classroom no teste | 1920×1080, quadro 1, 300 amostras |
| Amostragem adaptativa, denoise, tiling automático | desligados |
| Atualização dos dados | 2026-11-09 |

## A placa

| Item | Valor |
|---|---|
| VRAM | 6 GB GDDR6 |
| Lançamento | 2019 |
| Arquitetura | Turing |
| Chip | TU116 |
| Núcleos CUDA | 1.536 |
| Banda de memória | 288 GB/s |
| Barramento | 192 bits |
| Clock base / boost | 1500 / 1770 MHz |
| Processo | 12 nm |
| TDP | 120 W (NVIDIA, referência; TechPowerUp como fonte secundária) |
| Fonte do sistema, mínimo do fabricante | 450 W |
| Fonte sugerida por terceiro | 300 W (TechPowerUp; não é o mínimo do fabricante) |
| Conferência das fontes de energia | 23/09/2026 |
| Ressalva da página sobre energia | potência da placa e fonte do sistema medem coisas diferentes; conferir a placa exata |
| Menor preço | US$ 199,99, conferido em 02/11/2026, com atualização atrasada |
| Ofertas | 11 |

## A avaliação da página

| Ponto | Fato |
|---|---|
| VRAM mínima do Blender | 2 GB: a placa atende |
| VRAM recomendada do Blender para Windows e Linux | 8 GB: a placa fica abaixo |
| Do que depende o uso | compatibilidade de GPU e driver; memória que a cena pede |
| Contras listados | pouca VRAM para projeto pesado; geração antiga |
| Destaques listados | arquitetura Turing; processo de 12 nm |
| Espera de render | mais longa; para quando o tempo de render pesa menos |
| Antes de comprar | conferir memória da cena e compatibilidade |

| Alternativa | Grupo | Pontuação | Ano | VRAM |
|---|---|---|---|---|
| GTX 1660 SUPER | mesma geração | 676 | 2019 | 6 GB |
| GTX 1660 | mesma geração | 612 | 2019 | 6 GB |
| GTX 1650 | mesma geração | 360 | 2019 | 4 GB |
| GTX 1660 Ti Max-Q | mesma faixa | — | 2019 | 6 GB |
| GTX 1660 Ti Mobile | mesma faixa | — | 2019 | 6 GB |
| GTX 660 Ti | mesma faixa | — | 2012 | 2 GB |
| GTX 1080 Ti | desempenho vizinho | 695 | 2017 | 11 GB |
| RTX 2050 Mobile | desempenho vizinho | 696 | 2021 | 4 GB |
| RX 5600 XT | desempenho vizinho | 696 | 2020 | 6 GB |

## O que a fonte recomenda

A página põe a placa como opção de quem aceita esperar mais pelo render e pede que, antes da compra, se confira se a memória da cena cabe nos 6 GB e se placa e driver são compatíveis; os tempos que dá são estimativas com margem, de cenas de benchmark numa versão do Blender, e o chamado da página é para tirar o render do computador e mandá-lo à nuvem dela.

## Citações

- "The calculation uses 240 samples for Junkshop, 256 for Monster and 300 for Classroom, plus a 19% estimation buffer."
- "Results from different Blender versions may not be directly comparable."
- "Meets Blender’s 2 GB VRAM minimum but falls below its 8 GB recommendation for Windows/Linux."

## Lacuna

O texto exibido não dá a resolução das cenas (só os dados embutidos trazem a da Classroom) nem o que é a margem de 19% (sobre que valor, por quê), e não traz número de EEVEE, de Grease Pencil ou de render de animação, só de um quadro em Cycles. Não diz qual sistema operacional e driver as 31 execuções usaram, nem a dispersão entre elas, nem dá link para o requisito de VRAM do Blender que cita; e não traz data de publicação da página.
