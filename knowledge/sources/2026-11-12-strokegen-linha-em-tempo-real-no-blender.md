---
titulo: "This Real-Time Line Art Renderer for Blender Is Open for Testing"
tipo: artigo
autor: "Gloria Levine"   # assinatura na página ("Head of Content") e author do JSON-LD
url: "https://80.lv/articles/this-real-time-line-art-renderer-for-blender-is-open-for-testing"
publicado_em: 2024-12-03   # "03 December 2024" na página; article:published_time 2024-12-03T12:17:00+00:00, modified 14:46:45 do mesmo dia
capturado_em: 2026-11-12
licenca: "protegido (rodapé: '© 2026. 80 level. All rights reserved'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [blender, npr-rendering, line-art, real-time-rendering, gpu, strokegen]
---

# StrokeGen: um renderizador de linha em tempo real para o Blender, aberto em beta

Nota de fato (reportagem): tabelas do que a notícia registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela afirma e o que falta. Não há integral: o artigo é protegido.

**Proveniência.** Notícia do 80 Level (80.lv), seção News, assinada por Gloria Levine, https://80.lv/articles/this-real-time-line-art-renderer-for-blender-is-open-for-testing, baixada em HTML em 12/11/2026 e lida no texto extraído, conferido no HTML (links do corpo, dados estruturados e metas); sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco principal do HTML, não do arquivo); Wayback http://web.archive.org/web/20250810023257/https://80.lv/articles/this-real-time-line-art-renderer-for-blender-is-open-for-testing. Título conferido no `headline` do JSON-LD; o `og:title` é a forma curta "Real-Time Line Art Renderer for Blender Open for Testing", e o HTML não tem `<title>`. Lido o artigo inteiro (cerca de 300 palavras), até a chamada final para as redes do 80 Level; os vídeos embutidos (posts do criador no X) não foram assistidos, e nenhum link foi aberto, nem o post do criador no fórum de desenvolvimento do Blender, de onde vem a descrição das fases, nem a página de releases.

**Ângulo da matéria.** Notícia de lançamento (a beta aberta), com subtítulo em tom de piada.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato fica fora. Resultado: 1 de 12 unidades segue a fonte, a frase de "O que a fonte afirma", que junta a abertura, a fala do criador e a segunda fase; a maior sequência seguida que segue a fonte tem 1 unidade, e as duas citações estão à parte. O `parafrase.py` saiu com o código 3 contra o texto extraído do artigo (`strokegen-80lv.txt`), com 12 unidades medidas (12 de prosa, 0 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas.

## Em uma frase

Notícia curta do 80 Level, site do setor de jogos e arte digital, sobre o StrokeGen, com a parte técnica tirada das palavras do criador no fórum de desenvolvimento do Blender.

## O que a notícia registra

| Item | Fato |
|---|---|
| Ferramenta | StrokeGen |
| O que é | renderizador de linha (line art) em tempo real |
| Para | Blender |
| Criador | Wangziwei Jiang (no X, `jwtstone`) |
| Estado | beta aberta a testes |
| Versão disponível | StrokeGen Beta 1.0 |
| Onde baixar (link do artigo) | github.com/JiangWZW/strokegen-releases/releases |
| Origem | exploração de técnicas NPR do criador |
| Já noticiado antes | sim, em outro artigo do 80 Level (link) |
| Fonte da descrição das fases | post do criador no devtalk.blender.org (link) |
| Comentários na página | 0 |

## Como funciona, pelo criador

| Item | Fato |
|---|---|
| Entrada | malha |
| Saída | curvas de feição 2D, a partir de curvas 3D |
| Curvas suportadas hoje | só contorno |
| Previstas | borda, interseção, vinco |
| Fase 1, por objeto | lê vértices, faces e arestas de cada malha |
| Fase 1, conversão | representação própria para GPU |
| Fase 1, processamento | kernels paralelos na GPU: remalhar, tesselar, analisar a superfície |
| Fase 1, fim | gera as curvas de feição |
| Fase 2, por curva | junta todas as curvas em lote |
| Fase 2, reamostragem | de 3D para 2D |
| Fase 2, estilo | aplicado às curvas 2D |
| Fase 2, saída | desenhada na tela |
| Modo de desenho 1 | carimbo (stamping), como pincel do Photoshop |
| Modo de desenho 2 | traço (stroking), como curva vetorial do Illustrator |

## O que a fonte afirma

A ferramenta saiu da fase de demonstração e pode ser baixada em beta; pelo que o criador descreve, o traço nasce da malha na GPU, como curva 3D que vira 2D antes de ganhar estilo, e por enquanto só o contorno é traçado.

## Citações

- "Given an input mesh, StrokeGen traces 3D feature curves and then resamples them to 2D curves." (Wangziwei Jiang, citado no artigo)
- "It currently only supports contour curves" (Wangziwei Jiang, citado no artigo)

## Lacuna

O artigo não diz se o StrokeGen é complemento do Blender ou se pede uma versão própria dele, nem com que versão do Blender roda. Não dá números de velocidade nem compara com o Freestyle ou o Line Art, não diz a licença, o preço, o sistema ou a placa exigidos, e não diz se a linha sai no render final (EEVEE, Cycles) ou só na viewport.
