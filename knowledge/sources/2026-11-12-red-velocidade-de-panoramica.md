---
titulo: "Panning Speed Best Practices"
tipo: artigo
autor: "RED Digital Cinema"   # página da seção RED 101 do site da RED, sem assinatura de pessoa
url: "https://red.com/red-101/camera-panning-speed"
publicado_em: null   # a página não traz data, nem no texto nem nos metadados do HTML baixado
capturado_em: 2026-11-12
licenca: "protegido (rodapé: 'Copyright © 2004-2026 RED Digital Cinema, Inc. All rights reserved.'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [camera-movement, camera-moves, pan, judder, strobing, frame-rate, shutter-angle, motion-blur, interested-party]
---

# RED: uma largura de quadro a cada sete segundos, e o que mexe nessa conta

Nota de fato: tabelas do que a página da RED diz sobre a velocidade da panorâmica, o tremor que ela provoca e os fatores que mudam o limite, organizadas pelo efeito de cada fator e não pela ordem da página, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Tutorial da seção RED 101 do site da RED Digital Cinema, https://red.com/red-101/camera-panning-speed, baixado em HTML em 2026-11-12 e lido no texto extraído do HTML, que bate com a página: abre com o título "Panning Speed Best Practices" (o mesmo do `<title>`) e traz o artigo inteiro entre o menu e o rodapé. sha256 registrado na rodada: (hash omitido), que mede o texto do bloco `<main>`/`<article>`, sem tags, script e estilo, e não o arquivo HTML. Wayback: `http://web.archive.org/web/20260313201929/https://www.red.com/red-101/camera-panning-speed`. Sem data na página. Cobertura: o texto inteiro do artigo (a abertura, as seções da velocidade, da taxa de quadros e do obturador, da ferramenta e das outras considerações; os dois links de tópicos relacionados não foram abertos); os vídeos e diagramas aparecem só pelas legendas, e a calculadora da seção "Panning Speed Tool" não está no HTML baixado (nenhum campo dela no arquivo), então os parâmetros que ela pede não foram vistos.

**Quem fala.** A RED, fabricante de câmeras de cinema, numa página de ensino do próprio site, que tem no menu a loja das câmeras e acessórios.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` contra o texto extraído saiu com o código 3 (ficha em português, fonte em inglês): 19 unidades medidas (14 de prosa, 5 de célula com texto); fora da conta, 86 células de fato, 11 de cabeçalho e 8 frases curtas demais para medir; 0 colada de 19 e 0 trecho de 3 ou mais seguidas. Na leitura lado a lado das mesmas 19 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais seguidas na ordem dela; a frase que junta lugares distantes em outra ordem não conta. Resultado: 5 de 19 (as células de "passar do limite", da causa do tremor, da margem do giro, da lente longa com o diagrama e do sujeito que passa rente). A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 2 (a causa do tremor e a margem do giro; a lente longa e o sujeito que passa rente), sem trecho de 3 ou mais; a proveniência, a frase de abertura, a recomendação e a lacuna não seguem a fonte.

## Em uma frase

Página de ensino da RED, que vende câmeras de cinema, dando como regra prática que a panorâmica não deve cruzar mais de uma largura de quadro em sete segundos, sob pena de tremor, e listando o que desloca esse limite: obturador, taxa de quadros, conteúdo da cena, distância do sujeito e o próprio gesto de girar.

## A regra e o alcance dela

| Ponto | Fato |
|---|---|
| Limite | uma largura inteira de imagem a cada 7 s, no máximo |
| Condição de origem | cinema projetado, 24 fps, obturador de 180° |
| Lente, modelo de câmera, sensor | não mudam a regra |
| Passar do limite | piora aos poucos, sem corte brusco para o inassistível |
| Ficar abaixo do limite | não garante imagem livre de artefato |
| Comparação mostrada | travessia em 3 s, com tremor; em 7 s, mais suave |
| Para que tipo de plano | cena parada, câmera em movimento constante |
| Grau de confiança dado | guia aproximado |
| Quem dá a palavra final | o espectador, e o clima da cena |

## O defeito

| Ponto | Fato |
|---|---|
| Nomes | strobing; judder |
| Aspecto | a imagem pula em degraus pela tela |
| Causa | salto na tela grande para o tempo entre quadros |
| Fator decisivo | velocidade de travessia de borda a borda |
| Idade do problema | tão antigo quanto o cinema |

## O gesto de girar

| Ponto | Fato |
|---|---|
| Prioridade | uniformidade do giro, antes dos ajustes da câmera |
| Margem | arrancar antes do ponto inicial, parar depois do final, cortar o excesso |
| Cabo do tripé | mais longo |
| Cabeça do tripé | fluida ou de engrenagem |
| Tensão | ajustada contra trancos e pulos |
| Produção de ponta | panorâmica motorizada |

## O que aperta e o que folga o limite

| Fator | Efeito | Detalhe |
|---|---|---|
| Lente mais longa | aperta | ângulo de visão menor; no diagrama, o mesmo giro cruza o dobro de larguras |
| Sensor menor | aperta | mesmo motivo da lente longa |
| Obturador abaixo de 180° | aperta | imagem mais nítida, movimento mais picotado |
| Obturador acima de 180° | folga | movimento mais liso, imagem mais arrastada |
| Ângulos de exemplo | — | 45° e 270° |
| Cena em clima de sonho, fluida | folga | giro mais rápido com obturador maior |
| Paisagem com muito detalhe | aperta | giro mais lento com obturador menor |
| Reproduzir em taxa alta | folga | tremor menor sem desacelerar o giro |
| Captar em 48 ou 60 fps, mostrar em 24 ou 30 | folga | suaviza os movimentos de alta frequência |
| Contraste alto, cortes bruscos de claro e escuro | aperta | efeito descrito como mais subjetivo |
| Objeto perto da câmera | aperta para ele | cruza o quadro mais rápido que o fundo |
| Exemplo de distância, com a câmera parada | — | gelo do primeiro plano treme, o resto fica liso |
| Fundo desfocado | pesa na escolha | escolhe-se pelo lugar do sujeito |
| Sujeito que passa rente (ciclista) | dispensa | o giro curto e rápido não segue o padrão |
| Chicote (swish pan) | dispensa | o borrão é o objetivo |
| Cena de muita energia | folga | aceita movimento brusco |

## A calculadora da página

| Ponto | Fato |
|---|---|
| Saída | a velocidade em que o tremor passa a incomodar |
| Entrada | a regra dos 7 s e outros fatores, sem lista na página |
| Alternativa a | tabelas dos manuais de fotografia de cinema |
| Uso em desacordo entre pessoas | referência objetiva |
| Campos no HTML baixado | nenhum |

## O que a fonte recomenda

O limite de uma largura por sete segundos é o ponto de onde se parte, e o ajuste vem do resto: o obturador troca tremor por borrão, a taxa de quadros alta folga a velocidade, e o sujeito próximo ou a cena de muito contraste apertam a conta. Antes de tudo isso, o giro precisa ser uniforme, e quem decide no fim é o olho de quem assiste e o clima da cena.

## Citações

- "pan no faster than a full image width every seven seconds, otherwise judder will become too detrimental."
- "it applies regardless of camera lens, model or sensor size."
- "Results should only be taken as a rough guideline for static scenes with constant camera movement."

## Lacuna

A página não diz de onde vem a regra dos sete segundos (estudo, norma, prática de manual) nem como ela muda em números com outro obturador ou outra taxa de quadros; só diz para que lado muda. Não trata de tela pequena, de vídeo vertical, de reprodução no celular nem de câmera virtual, e não mostra o que a calculadora pede nem a fórmula dela.
