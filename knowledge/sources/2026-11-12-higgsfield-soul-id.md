---
titulo: "How do I create and use a Soul ID character?"
tipo: artigo
autor: "Higgsfield (central de ajuda)"
url: "https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-create-and-use-a-soul-id-character"
publicado_em: 2026-08-01   # "Aug 1, 2026 · Updated Nov 11, 2026" na página; datePublished 2026-08-01 e dateModified 2026-11-11 no HTML
capturado_em: 2026-11-12
licenca: "protegida: a página não declara licença (valem os termos do site da Higgsfield); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [higgsfield, soul-id, character-consistency, identity-training, elements, seedance, aggregator]
---

# Higgsfield Soul ID: a identidade treinada, o que ela exige e onde ela vale

Nota de fato: tabelas do que a página registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Artigo da central de ajuda da Higgsfield, baixado em HTML em 12/11/2026 (`sha256` (hash omitido)), e lido no texto extraído do HTML: a definição, a comparação com a imagem de referência, o treino em quatro passos, a tabela de fotos, o uso fora do Soul, os limites, os usos indicados e as quatro perguntas finais; ficaram fora o menu, a avaliação do artigo e os artigos relacionados. Formato: nota de fato, por ser documentação de produto (`README.md` desta pasta, item 2). A ficha de 2026-11-11, `2026-11-11-higgsfield-recursos-e-modelos.md`, cobre outras sete páginas da Higgsfield e não esta.

**Quem fala.** A Higgsfield, que vende o Soul ID dentro dos planos pagos.

**Data.** Publicado em 01/08/2026 e atualizado em 11/11/2026, na página e nos metadados.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa do corpo e as células com texto corrido; a célula que só traz um fato fica fora. Corpo: 3 frases de prosa e 5 tabelas; das 5 células de 8 palavras ou mais, 2 são passos de menu e ficam como fato. Resultado: 3 das 6 unidades seguem uma frase da fonte, as três células da promessa e das ressalvas, que trazem o que a página afirma; a recomendação junta o treino, a tabela de fotos e a pergunta do personagem inventado. As três citações estão à parte. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: a parte traduzida não se mede), 0 frase colada, e a conta lado a lado é a conferência.

## Em uma frase

Página de ajuda do Soul ID, a camada de identidade que a Higgsfield treina sobre fotos de uma pessoa para manter o mesmo rosto em toda geração dos modelos Soul, com o que o treino pede, o que ele promete e onde a identidade pode ser usada.

## O que é e o que exige

| Item | Fato |
|---|---|
| O que é | uma identidade treinada, reusável |
| Modelos | a família Soul, da própria Higgsfield |
| Fotos de treino | 20 ou mais, até 80 |
| Pessoas por foto | uma |
| Pessoas por Soul ID | uma |
| Tempo de treino | alguns minutos |
| Plano | pago, para treinar e para gerar |
| Fim do plano | personagens salvos |
| Ao assinar de novo | usáveis outra vez |
| Quem pode estar nas fotos | a própria pessoa, ou quem autorizou |
| Personagem inventado ou estilizado | retratos gerados antes; treino sobre eles |
| Exportar o Soul ID | não; as imagens e vídeos gerados, sim |
| Caminho no site | Soul → Train new character |

## As fotos que ajudam e as que atrapalham

| Ajuda | Atrapalha |
|---|---|
| ângulos e expressões variados | a mesma pose em todas |
| rosto claro e bem iluminado | sombra pesada ou luz dura |
| fotos recentes (últimos 4 a 5 meses) | fotos antigas, se a aparência mudou |
| ao menos uma de corpo inteiro | só fotos da cabeça |
| nada cobrindo o rosto | óculos escuros, chapéu, cachecol |
| uma pessoa por foto | foto de grupo |

| Item | Fato |
|---|---|
| Conjunto preferido | pequeno, limpo e variado |
| Geração inconsistente depois do treino | treinar de novo com um conjunto melhor |

## Onde a identidade vale

| Item | Fato |
|---|---|
| Fora do Soul | no Seedance da Higgsfield, como *Element* |
| Como aparece lá | sozinho, em "My Elements" |
| Criar o *Element* à mão | imagem do personagem → Assets → "Create Element" |
| Chamar no Seedance | `@ Elements` sob o prompt, ou `@` no texto |
| Dois personagens ou mais | por *Elements*, não por Soul ID |
| Usos indicados | influenciador de IA; UGC; moda; marca pessoal |

## O que a página promete e o que ela ressalva

| Ponto | Fato |
|---|---|
| Promessa | o mesmo rosto; qualquer estilo, pose e luz |
| Imagem de referência, segundo a página | desvia entre gerações |
| Soul ID, segundo a página | não desvia |
| Medida que sustente isso | nenhuma na página |
| Ressalva | a mesma pessoa reconhecível, não o pixel idêntico |
| Ressalva | fotos fracas dão identidade fraca |
| Ressalva | desvio pequeno em estilo extremo ou ângulo incomum |

## O que a fonte recomenda

Treinar uma vez, sobre um conjunto curto e limpo de fotos recentes, variadas e com um corpo inteiro, e esperar a mesma pessoa reconhecível, não a cópia exata; para personagem inventado, criar os retratos antes e treinar sobre eles.

## Citações

- "A reference image anchors a single generation but drifts across many separate ones." (comparação com a imagem de referência)
- "Expect \"clearly the same person\" rather than a pixel-identical face across every generation." (limites)
- "For an invented character, generate those portraits first, then train a Soul ID on them." (perguntas finais)

## Lacuna

A página não mede o desvio que atribui à imagem de referência nem a fidelidade do Soul ID, não diz o preço do plano pago, não diz se o Soul ID passa a outros modelos além do Seedance (cita só esse) e não trata de personagem desenhado além da frase sobre o inventado ou estilizado.
