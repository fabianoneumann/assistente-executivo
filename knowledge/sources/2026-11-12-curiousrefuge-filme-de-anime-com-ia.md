---
titulo: "How to Create a Professional Anime Film with AI"
tipo: artigo
autor: "Tyler Smith (Curious Refuge)"
url: "https://curiousrefuge.com/blog/how-to-create-an-anime-film-using-ai"
publicado_em: 2026-06-30   # "Jun 30" na página; datePublished 2026-06-30 no HTML
capturado_em: 2026-11-12
licenca: "protegida: '© 2026. All rights reserved.' no rodapé; a página não declara outra licença; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [anime, character-sheet, style-reference, location-reference, reference-to-video, short-film, upscaling, voice-consistency]
---

# Curious Refuge: o curta em anime em que a folha de personagem vai direto à ferramenta de vídeo

Nota de fato: tabelas do que a página registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Artigo do blog da Curious Refuge, com um vídeo tutorial embutido (não assistido), baixado em HTML em 12/11/2026 (`sha256` (hash omitido)), e lido no texto extraído do HTML: a abertura, os onze passos e o passo bônus, e a chamada final; ficaram fora o menu, o formulário e os links. Formato: nota de fato, por ser tutorial de método (`README.md` desta pasta, item 2), organizada por etapa. A ferramenta de vídeo não tem nome na página.

**Quem fala.** Tyler Smith, contando o próprio projeto, no blog da Curious Refuge, escola de cinema com IA; a página leva ao curso gratuito da escola e à comunidade dela.

**Data.** "Jun 30", sem ano no texto; os metadados do HTML dão 30/06/2026.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa do corpo e as células com texto corrido; a célula que só traz um fato fica fora. Corpo: 3 frases de prosa e 1 tabela; das 3 células de 8 palavras ou mais, 2 são listas e ficam como fato. Resultado: 1 das 4 unidades segue uma frase da fonte (a da voz, que traz o julgamento do autor); a recomendação junta os passos 2, 4, 5, 6, 7, 9 e 10. As três citações estão à parte. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: a parte traduzida não se mede), 0 frase colada, e a conta lado a lado é a conferência.

## Em uma frase

Tutorial de um curta em anime com visual de pintura a óleo (uma perseguição em Positano), em que a referência de estilo, as referências dos personagens e das locações viram folhas e imagens que vão direto à ferramenta de vídeo, sem storyboard.

## O fluxo, por etapa

| Etapa | Item | Fato |
|---|---|---|
| 1. História | Cena | perseguição de ficção científica em Positano |
| 1. História | Origem | uma viagem do autor à Itália |
| 1. História | Personagens | 3: protagonista, protagonista, vilão |
| 2. Estilo | Fonte da referência | página Explore do Midjourney |
| 2. Estilo | Visual | anime ou mangá; pintura a óleo |
| 2. Estilo | Onde a referência entra | personagens; locações; cenas |
| 3. Personagem | Referência de cada um | achada ou gerada |
| 4. Folha | Ferramenta | modelo de imagem (sem nome) |
| 4. Folha | Entradas | referência de estilo; referência do personagem |
| 4. Folha | Vistas | frente; costas; lado |
| 4. Folha | Mais | expressões; close do rosto |
| 4. Folha | Proporção | 1:1 |
| 4. Folha | Tentativas | várias |
| 5. Locações | Quantas | 4 |
| 5. Locações | Quais | restaurante na praia; beco; saguão de hotel; outro ângulo do beco |
| 5. Locações | Entrada | a referência de estilo |
| 5. Locações | Proporção | 16:9 |
| 6. Primeira cena | Ferramenta | "your AI video tool" (sem nome) |
| 6. Primeira cena | Entradas | folha do personagem; locação |
| 6. Primeira cena | Quadro inicial | não mencionado |
| 6. Primeira cena | Storyboard | dispensado |
| 6. Primeira cena | Cortes | vários, gerados pelo modelo |
| 6. Primeira cena | Resolução sugerida (anime, 2D) | 720p |
| 7. Cena seguinte | Entradas | clipe anterior (15 s); duas folhas; locações |
| 7. Cena seguinte | Instrução | cada personagem continua o mesmo |
| 7. Cena seguinte | Iterações | algumas, segundo o autor |
| 8. Áudio | Separar voz e fundo | SAM Audio (Meta) |
| 9. Voz | Consistência com o áudio nativo | difícil, às vezes quase impossível, segundo o autor |
| 9. Voz | Contorno | voz ajustada à parte (tutorial próprio da escola) |
| 10. Upscale | Ferramenta | Topaz Video AI, modelo Proteus |
| 10. Upscale | De e para | 720p → 4K |
| 11. Montagem | O que entra | melhores cortes; ADR; efeitos; música |
| Bônus | Acabamento | cor; grão; FilmConvert; halation |

## O que a fonte recomenda

Fixar primeiro o estilo, numa imagem só que acompanha todo o trabalho, e derivar dele as folhas dos personagens e as imagens das locações; depois entregar essas referências à ferramenta de vídeo e deixar que ela gere os cortes, encadeando cada cena na anterior; e corrigir à parte o que a geração não segura, a voz e a resolução.

## Citações

- "Character sheets help AI video tools understand what your characters look like from multiple angles." (passo 4)
- "Upload your character sheet and environment reference into your AI video tool." (passo 6)
- "Instead of creating traditional storyboards, you can describe the action and let the AI generate multiple shots." (passo 6)

## Lacuna

A página não diz qual ferramenta de vídeo nem qual modelo de imagem usou, não mostra quantas gerações cada cena levou nem as que falharam, não mede se a identidade se manteve e não dá custo.
