---
titulo: "Pricing Animate3D"
tipo: artigo
autor: "DeepMotion"   # página do site da DeepMotion, sem assinatura de pessoa
url: "https://www.deepmotion.com/pricing-animate3d"
publicado_em: null   # a página não traz data no texto nem nos metadados do HTML lido
capturado_em: 2026-11-12
licenca: "protegido (rodapé: 'Copyright © DeepMotion'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [deepmotion, motion-capture, markerless, pricing, licensing, commercial-use, interested-party, character-animation, fbx, bvh]
---

# DeepMotion Animate 3D: o plano grátis é só para uso pessoal, e a licença vem do plano pago

Nota de fato: tabelas do que o FAQ da página de preços do Animate 3D diz sobre licença, créditos, planos, o programa de créditos grátis e os arquivos de entrada e saída, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Página https://www.deepmotion.com/pricing-animate3d, baixada em HTML com `curl` em 2026-11-12 e lida no texto extraído do bloco principal, conferido no HTML. O sha256 (hash omitido) é o do texto do `<main>`/`<article>` sem tags, script e estilo, não o do HTML inteiro. Wayback: `http://web.archive.org/web/20261029180538/https://www.deepmotion.com/pricing-animate3d`. Título conferido no texto: a página abre com "Pricing Animate3D" e o título "Animate 3D Plans & Pricing", com o subtítulo "Markerless Full-Body AI Motion Capture". Texto de quem vende o Animate 3D.

**Cobertura.** O FAQ inteiro: 35 perguntas, aqui P1 a P35, na ordem da página. A tabela de planos não está no HTML baixado: no lugar dela há só um contêiner vazio (`react-target-body`) que um script preenche no navegador, e o HTML não traz nenhum preço nem nome de plano fora do FAQ (o único plano nomeado é o Studio, na P24). O formato é nota de fato porque o FAQ é documentação de serviço, e, como as 35 perguntas não têm seções e alternam de assunto, as tabelas juntam os fatos por tema, com o número da pergunta de onde cada um sai.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2, contra o texto extraído `leitura/deepmotion-pricing-animate3d.txt`). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), com 34 unidades medidas (18 de prosa, 16 de célula com texto), 0 coladas e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 34 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a frase que junta perguntas distantes em outra ordem não conta. Resultado: 16 de 34, as 16 células com texto, cada uma a resposta de uma pergunta em palavras próprias; nenhuma das 18 frases de prosa (proveniência, esta conferência, "Em uma frase", recomendação e lacuna) segue a fonte. A maior sequência de unidades seguidas que seguem a fonte é de 16 (as células, de "Cota esgotada" a "O que mandar ao suporte"), mas a fonte anda para trás dentro dela; na ordem da fonte, com a janela de 12 frases do script, a maior é de 2, porque as tabelas vêm por tema, não na ordem das perguntas (sem limite de distância, 3: as células de P4, P5 e P29, em tabelas diferentes); não há trecho colado no texto que recomenda ou conclui.

## Em uma frase

Texto da DeepMotion sobre o próprio serviço de captura de movimento por vídeo: a conta Freemium dá 60 segundos por mês só para uso pessoal e não comercial, a animação licenciada exige um plano premium pago, e um programa devolve créditos a quem descreve e corrige as próprias animações, texto que alimenta o modelo da empresa.

## Licença e privacidade

| Ponto | Fato | Onde |
|---|---|---|
| Conta Freemium | uso pessoal e não comercial | P26 |
| Animação licenciada | exige plano de assinatura premium | P17, P35 |
| O que decide a licença | o tipo de plano | P17, P35 |
| Animação feita com crédito grátis | mesma licença da feita com crédito da assinatura | P17, P35 |
| Para os detalhes | a página manda à tabela de preços | P17, P35 |
| Vídeos enviados | privados; nem o público nem outros usuários acessam | P32 |

## Créditos e planos

| Ponto | Fato | Onde |
|---|---|---|
| 1 crédito | 1 segundo de animação ou 1 pose 3D | P20 |
| Rastreio de rosto | +0,5 crédito por segundo ou por pose | P20 |
| Rastreio de mãos | +0,5 crédito por segundo ou por pose | P20 |
| Freemium, preço | sem cartão de crédito | P26 |
| Freemium, validade | a conta não expira | P26 |
| Freemium, cota | até 60 segundos de animação por mês | P26 |
| Cota mensal | varia com o plano | P30 |
| Cota esgotada | esperar o mês seguinte do plano ou subir de plano | P30 |
| Sobra de créditos | não passa para o mês seguinte, nos planos mensal e anual | P31 |
| Recarga | a cada mês, no valor do plano | P31 |
| Plano Studio | créditos ilimitados | P24 |
| Plano Studio, prioridade | os primeiros 7.200 créditos do mês na prioridade mais alta; o resto em prioridade baixa | P24 |
| Subir de plano | a qualquer momento; cobra a diferença proporcional; créditos proporcionais na hora | P23 |
| Cancelar | a qualquer momento; sem novas faturas; ativo até o fim do ciclo pago | P28 |
| Reprocessar (rerun) | limite conforme o plano | P11 |
| API e SDK de tempo real | por contato com a empresa | cabeçalho, P31 |

## O programa de créditos grátis (Free Animation Credit Program)

| Ponto | Fato | Onde |
|---|---|---|
| Para onde vai o texto | alimenta o modelo próprio que aprende a descrever movimento | P18 |
| Produtos que o programa melhora | Animate 3D e SayMotion (texto ou vídeo para movimento 3D, gerativo) | P16, P33 |
| Duas formas de ganhar | descrever o movimento do vídeo (Labeling); corrigir a animação no Rotoscope Pose Editor (Correction) | P22 |
| Teto | o total de créditos que o trabalho gastou (exemplo da página: 15 de 15) | P10 |
| Tipos de trabalho | qualquer um: pose, captura de uma pessoa, de várias | P14 |
| Trabalhos antigos da biblioteca | não; só trabalhos novos, por ora | P15 |
| Rerun | a descrição do original vale para o rerun; não se escreve outra | P11 |
| Correção | quadro a quadro, nas juntas mal rastreadas | P6 |
| Nota da correção | Pose Score, pelo comprimento e ângulo dos ossos contra um modelo mecânico do corpo humano | P7 |
| Descrição, tamanho | até 256 caracteres | P4 |
| Descrição, mínimo | dois aspectos do movimento: tipo de ação e estilo | P4 |
| Termos técnicos | permitidos (exemplos: balé, boxe, MMA, basquete, ginástica) | P12 |
| Nota da descrição | dada por um modelo próprio da DeepMotion | P5 |
| Língua da nota | modelo feito para inglês; outra língua pode baixar a nota | P5 |
| Validade do crédito ganho | zera todo mês, sem acumular | P9, P13, P34 |
| Prioridade do crédito ganho | a do plano do usuário | P9, P34 |
| Várias pessoas no celular | a descrição não está disponível | P19 |

## Entrada, saída e personagens

| Ponto | Fato | Onde |
|---|---|---|
| Vídeo de entrada | MP4; MOV; AVI | P27 |
| Exportação | FBX; BVH; MP4; GLB | P27 |
| GLB | só com personagem próprio | P27 |
| Personagens | do usuário ou um conjunto padrão do serviço | P29 |
| Personagem próprio | criado no serviço pela parceria com a Wolf3D, ou enviado em FBX ou GLB | P29 |
| Resultado diferente do esperado | conferir as Capture Guidelines; pedir ajuda no Discord | P25 |
| O que mandar ao suporte | vídeo original; gravação ou MP4 da animação; captura das configurações do trabalho | P25 |
| Login que não carrega | tradutor automático do navegador atrapalha; cookies precisam estar ligados | P2 |

## O que a fonte recomenda

Quem vai usar a animação em trabalho comercial precisa estar num plano premium, porque o Freemium é só pessoal e a licença segue o plano, não a origem do crédito. Para recuperar créditos, a descrição deve gastar o máximo dos 256 caracteres, em inglês e com vocabulário técnico, e a correção deve aproximar a pose do modelo humano; e, antes de pedir ajuda, o vídeo deve seguir as diretrizes de captura.

## Citações

- "Freemium accounts are available for personal, non-commercial use." (P26)
- "In order to have licensed animation, you must have a premium subscription plan." (P17)
- "your text feeds our proprietary model to understand descriptions of motions" (P18)

## Lacuna

A tabela de planos não veio no HTML (carrega por script), então a ficha não tem nomes, preços nem cotas dos planos pagos, nem diz quais deles são "premium". O FAQ não diz o que a licença permite (uso comercial em vídeo, revenda, crédito ao serviço), nem remete a termos de uso com essas regras; os Termos de Serviço do rodapé não foram abertos. Não diz se os vídeos enviados entram no treino de algum modelo (diz só que ficam privados e que o texto das descrições alimenta o modelo próprio), nem qual é o preço da API. A página não tem data.
