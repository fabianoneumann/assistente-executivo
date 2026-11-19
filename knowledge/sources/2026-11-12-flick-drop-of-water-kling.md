---
titulo: "How to Use Kling AI to Make a Short Film in 7 Steps"
tipo: artigo
autor: "Zoey Z. (Flick), sobre o curta Drop of Water, de Karan Archana"
url: "https://flick.art/blog/how-to-use-kling-ai"
publicado_em: 2026-10-26   # "Last updated Oct 26, 2026" na página; datePublished e dateModified 2026-10-26 no HTML
capturado_em: 2026-11-12
licenca: "protegida: '© 2026 FLICKART, Inc.' no rodapé da página; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [kling, character-sheet, turnaround, start-frame, image-to-video, short-film, dialogue, negative-prompt, continuity, interested-party]
---

# Flick: o fluxo do curta *Drop of Water*, da folha de personagem ao take corrigido no Kling

Nota de fato: tabelas do que a página registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Artigo do blog da Flick, baixado em HTML em 12/11/2026 (`sha256` (hash omitido)), e lido no texto extraído do HTML: a resposta curta, os sete passos com os prompts do filme, a tabela das configurações dos 89 clipes, o método da contagem e as oito perguntas do FAQ; ficaram fora o menu, as chamadas de cadastro e os links para outros guias. Os prompts estão na página como o diretor os escreveu; aqui entram descritos, não copiados. Formato: nota de fato, por ser guia de método com números (`README.md` desta pasta, item 2), organizada por etapa do fluxo.

**Quem fala. Parte interessada:** a Flick vende a plataforma em que o filme foi feito (o Kling roda nela a partir do plano Standard), e a página chama para gerar nela. O texto é de Zoey Z., que a página apresenta como cineasta de IA e designer; os prompts e as configurações são do diretor, Karan Archana, lidos no canvas público do filme, que a Flick diz ter lido inteiro em 26/10/2026. O filme é da residência de verão de 2026 da Flick.

**Data.** "Last updated Oct 26, 2026"; os metadados do HTML dão a mesma data.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa do corpo e as células com texto corrido; a célula que só traz um fato fica fora. Corpo: 4 frases de prosa e 5 tabelas; as 13 células de 8 palavras ou mais são listas, valores ou os critérios de contagem citados da página, e ficam como fato. Resultado: 0 das 4 unidades segue uma frase da fonte (a recomendação junta os sete passos e o FAQ). As três citações estão à parte; os prompts do filme não estão copiados. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: a parte traduzida não se mede), 0 frase colada, e a conta lado a lado é a conferência.

## Em uma frase

Guia da Flick que desmonta o curta *Drop of Water* (3:21, drama de seca, 89 clipes do Kling 3.0 4K) em sete passos, com os prompts reais e a contagem das configurações; o fluxo vai da folha de personagem ao quadro inicial composto num modelo de imagem, e só então ao vídeo.

## O filme

| Item | Fato |
|---|---|
| Duração | 3:21 |
| Gênero | drama de seca |
| Diretor | Karan Archana |
| Clipes | 89, todos do Kling 3.0 4K, por imagem para vídeo |
| Estilo | fotorrealista ("photorealistic", "grounded cinematic realism" nos prompts) |
| Kling 4.0 | chegou à Flick em 26/10/2026, depois do filme |

## O fluxo, por etapa

| Etapa | Ferramenta | Item | Fato |
|---|---|---|---|
| 1. Folha de giro | GPT Image 2 | Quando | antes de qualquer vídeo |
| 1. Folha de giro | GPT Image 2 | Quantas | uma por personagem (Ken, Evelyn) |
| 1. Folha de giro | GPT Image 2 | Painéis da do Ken | 6 |
| 1. Folha de giro | GPT Image 2 | Vistas | frente; perfil esquerdo; perfil direito; costas |
| 1. Folha de giro | GPT Image 2 | Closes do rosto | 2 (lado direito, lado esquerdo) |
| 1. Folha de giro | GPT Image 2 | Fundo | branco liso |
| 1. Folha de giro | GPT Image 2 | Pose | A-pose |
| 1. Folha de giro | GPT Image 2 | Luz e enquadramento | chapada; ortográfico |
| 1. Folha de giro | GPT Image 2 | Base da do Ken | 3 retratos anteriores dele |
| 1. Folha de giro | — | Folha de expressões | uma por personagem |
| 2. Quadro inicial | Nano Banana Pro | Entradas | imagem 1, a cena; imagens 2 e 3, as folhas do Ken |
| 2. Quadro inicial | Nano Banana Pro | Exemplo | plano a dois → close só do Ken |
| 2. Quadro inicial | — | Clipes que partiram de um quadro assim | 89 de 89 |
| 3. Câmera | Kling 3.0 4K | Movimentos por plano | 1 |
| 3. Câmera | Kling 3.0 4K | O que o prompt fixa | ponto de partida; velocidade; ponto de chegada |
| 3. Câmera | Kling 3.0 4K | Exemplo | panorâmica pela cerca, a um terço do percurso normal em 5 s |
| 3. Câmera | Kling 3.0 4K | Durações | 3, 5, 10 ou 15 s |
| 4. O que evitar | Kling 3.0 4K | Partes do prompt | cena; movimentos permitidos; AVOID |
| 4. O que evitar | Kling 3.0 4K | Movimentos permitidos no exemplo | 5 linhas |
| 4. O que evitar | — | AVOID do exemplo, atuação | drama; choro; grito; gesto largo |
| 4. O que evitar | — | AVOID do exemplo, câmera | tremida; câmera na mão; panorâmica; zoom |
| 5. Fala | Kling 3.0 4K | Texto | exato, entre aspas |
| 5. Fala | Kling 3.0 4K | Entrega | descrita (calma, baixa) |
| 5. Fala | Kling 3.0 4K | Silêncio depois | escrito no prompt |
| 5. Fala | Kling 3.0 4K | Áudio | gerado com a imagem ("Generate Audio", ligado por padrão) |
| 6. Resposta | Kling 3.0 4K | Clipes por fala | 1 |
| 6. Resposta | Kling 3.0 4K | Quadro de cada fala | novo, por sobre o ombro |
| 6. Resposta | — | Voz | instrução de manter a voz já ouvida, a cada fala |
| 7. Correção | Kling O3 Pro (edição) | Objeto | o saquinho de água, que mudou entre planos |
| 7. Correção | Kling O3 Pro (edição) | Resto do plano | intocado, com a lista do que preservar |
| 7. Correção | Kling O3 Pro (edição) | Som | o da tomada original |
| 7. Correção | Kling O3 Pro (edição) | Cobrança | por segundo do clipe editado |
| 7. Correção | — | Sugestão do diretor | 2 imagens: último quadro do plano anterior; primeiro do atual |

## As configurações dos 89 clipes

Contagem da Flick no canvas público, em 26/10/2026; um prompt pode contar em mais de uma linha.

| O que o clipe pede | Clipes |
|---|---|
| 5 s | 57 |
| 10 s | 28 |
| 15 s | 4 |
| Áudio gerado | 89 |
| Lista do que evitar | 59 |
| Câmera travada ou parada | 51 |
| Continua do plano anterior | 50 |
| Fala entre aspas | 29 |
| Quadro final além do inicial | 1 |
| Mediana do prompt | 176 palavras |

| Como contaram | Critério |
|---|---|
| Lista do que evitar | a palavra "avoid" no prompt |
| Câmera travada | "locked", "no camera movement" ou "the camera remains completely still" |
| Continua | "previous shot", "last frame", "final frame" ou "continue" |
| Fala | um par de aspas duplas |
| Fora da conta | uploads e tomadas apagadas |

## Preço na Flick

| Item | Fato |
|---|---|
| Kling em vídeo | plano Standard ou acima, a partir de US$ 20 por mês |
| Kling Image V3 | no plano gratuito |
| Créditos de cadastro | 100 |
| Clipe Kling 3.0 4K | 330 créditos na duração padrão; 990 na mais longa |

## O que a fonte recomenda

Fixar o personagem antes do vídeo, numa folha de giro e numa de expressões, compor cada quadro inicial num modelo de imagem com as folhas anexadas, e deixar ao modelo de vídeo só o movimento: uma câmera por plano, a fala exata, a lista do que não fazer, e, quando um objeto falha numa tomada boa, editar o objeto em vez de gerar tudo de novo.

## Citações

- "The start frame carries the face, so the video model never has to guess it." (FAQ)
- "59 of the 89 Kling prompts in the film end with a list like this." (passo 4)
- "Kling video models in Flick run on the Standard plan and up." (abertura)

## Lacuna

A página não mostra nenhum clipe que tenha falhado nem diz quantas tentativas cada plano levou, não compara o fluxo com o de mandar a folha direto ao modelo de vídeo, não mede a consistência do rosto e trata só de um filme fotorrealista com personagens de pessoas; o custo total do filme não é dado.
