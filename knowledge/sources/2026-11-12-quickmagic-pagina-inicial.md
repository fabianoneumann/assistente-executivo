---
titulo: "AI Motion Capture from Video & Text | QuickMagic"
tipo: artigo
autor: "QuickMagic"   # página inicial do site, sem assinatura de pessoa
url: "https://www.quickmagic.ai/"
publicado_em: null   # a página não traz data no texto; os metadados dos três vídeos de demonstração dizem uploadDate 2025-06-30, que é a data dos vídeos, não a da página
capturado_em: 2026-11-12
licenca: "protegido (rodapé: '©2026 QuickMagic.ai'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [quickmagic, motion-capture, markerless, text-to-motion, interested-party, character-animation, fbx, bvh, commercial-use]
---

# QuickMagic: captura de movimento por um vídeo só ou por texto, com o preço e a licença fora da página

Nota de fato: tabelas do que a página inicial da QuickMagic diz sobre o que o serviço captura, para onde exporta, que vídeo funciona melhor e o que o FAQ remete a outras páginas, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Página https://www.quickmagic.ai/, baixada em HTML com `curl` em 2026-11-12 e lida no texto extraído do bloco principal, conferido no HTML (inclusive o FAQ dos dados estruturados, igual ao do texto). O sha256 (hash omitido) é o do texto do `<main>`/`<article>` sem tags, script e estilo, não o do HTML inteiro. Wayback: `http://web.archive.org/web/20261008230802/https://www.quickmagic.ai/`. Título conferido no texto: a página abre com "AI Motion Capture from Video or Text" (o título do HTML diz "& Text"). Texto de quem vende o serviço; os depoimentos são de usuários e parceiros escolhidos pela própria página. No rodapé, o contato é um e-mail no domínio lmdgame.com, e o perfil no X é `QuickMagic_cn`; a página não diz o nome da empresa.

**Cobertura.** A página inteira: a abertura, as quatro seções de recurso (vídeo, robôs, texto, exportação), os depoimentos e as doze perguntas do FAQ. O carrossel de depoimentos vem duas vezes no texto extraído, igual; a ficha conta cada um uma vez. A página de preços, a de formatos de exportação, o User Agreement e a Privacy Policy, a que o FAQ remete, não foram lidos; a de preços deu 403 no `curl`. Formato: nota de fato, porque a página é descrição de produto e FAQ, com cerca de 1.100 palavras sem a repetição.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2, contra o texto extraído `leitura/quickmagic-home.txt`). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), com 40 unidades medidas (21 de prosa, 19 de célula com texto), 0 coladas e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 40 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; ficam fora as duas células que só listam fatos (as entradas e os usos do texto) e a frase que junta partes distantes da página. Resultado: 18 de 40 (17 células com texto, cada uma uma resposta do FAQ, um recurso ou um depoimento em palavras próprias, e a segunda frase da recomendação, que junta as duas frases da resposta sobre uso comercial); nenhuma das outras 20 frases de prosa (proveniência, esta conferência, "Em uma frase", a primeira frase da recomendação e a lacuna) segue a fonte. A maior sequência de unidades seguidas que seguem a fonte é de 17 (as células com texto, da linha "Texto" à de "Dance with Miku", sem contar as duas de fato), mas a fonte anda para trás dentro dela; na ordem da fonte, a maior é de 2, porque as tabelas do FAQ e dos depoimentos vêm por tema, não na ordem da página. Nas duas tabelas do FAQ (revistas em 2026-11-19), as células, que vertiam cada uma uma frase da resposta, foram refeitas: a de plano, uso e prazos separa o que a resposta afirma de para onde ela manda, e a do vídeo abre pela regra geral e segue pelos casos difíceis, com as listas de cada resposta reagrupadas; das 14 células com texto das duas, nenhuma segue mais uma frase da fonte.

## Em uma frase

Texto da QuickMagic sobre o próprio serviço: estima o movimento do corpo, das mãos e do rosto a partir de um vídeo só, sem roupa nem marcadores, ou gera movimento a partir de texto, e exporta para as ferramentas 3D mais comuns, deixando preço, cotas e uso comercial para outras páginas.

## O que o serviço faz

| Recurso | Fato |
|---|---|
| Entrada | um vídeo (celular, webcam ou câmera) ou um texto |
| O que dispensa | roupa de captura; marcadores; sensores; estúdio de várias câmeras |
| Vídeo, o que estima | corpo, mãos e rosto |
| Vídeo, enquadramento | corpo inteiro ou só a parte de cima |
| Vídeo, pessoas | uma ou várias |
| Vídeo, câmera | parada ou em movimento |
| Vídeo, controles | pose, taxa de quadros, limpeza do movimento |
| Texto | rascunho de movimento editável a partir de uma ação, pose ou atuação descrita |
| Texto, usos citados | storyboard e previs; protótipo de jogo e animação; ideação de atuação; MMD, VTuber e humano digital |
| Robôs humanoides | referências de movimento humano para simulação, aprendizado por imitação e protótipos de comportamento |
| Robôs, predefinições | Unitree G1, H1 e H1_2 |

## Exportação

| Ponto | Fato |
|---|---|
| Formatos e predefinições | FBX; BVH; BIP; C4D; VMD; Mixamo; UE4; UE5.5; UE5.6; UE MetaHuman; Character Creator e iClone; Roblox; OnlyFace; UniRobot |
| Programas citados | Blender; Unreal Engine; Unity; Maya; 3ds Max; MotionBuilder; Cascadeur; iClone; MikuMikuDance; Roblox; UEFN (Fortnite); Cartoon Animator |
| Disponibilidade | varia com o plano e o fluxo de trabalho |

## O FAQ: plano, uso e prazos

Quase toda resposta deste bloco manda a outra página; a tabela separa o que a resposta afirma do lugar para onde ela manda.

| Assunto | O que a resposta afirma | Para onde manda |
|---|---|---|
| Uso comercial | não há regra única: contam o plano contratado e quem tem os direitos sobre o que se sobe (vídeo, personagens, áudio e qualquer outro material) | o User Agreement em vigor, a ler antes de usar o resultado em trabalho comercial |
| Plano grátis | existe, para experimentar; os limites dele e o que só os pagos têm a resposta não diz | a página de preços |
| Guarda dos arquivos | quem não paga tem os arquivos guardados por 15 dias; quem paga, sem prazo | a página de preços, que é de onde vem o número |
| Tempo de processamento | varia com o vídeo (duração, resolução), com o que se pediu (os recursos) e com o serviço (a fila, a prioridade do plano) | — |
| Robôs | só que alguns modelos têm fluxo e predefinição | a página de dados de robô, com modelos, juntas, sistemas de coordenadas e limites |

## O FAQ: o vídeo

Primeiro a regra geral, depois os casos em que o resultado fica menos firme:

| Caso | O que a página diz |
|---|---|
| A regra geral | o que ajuda é a pessoa sempre à vista, luz suficiente, pouco borrão, quase nada a encobrindo por muito tempo e, se a captura é do corpo todo, o corpo todo no quadro |
| Movimentos que deixam limpeza para depois | rodopio, pé que toca o chão de modo complicado, duas pessoas muito juntas |
| Mãos e rosto | quanto detalhe se aproveita cai com a imagem ruim, com a mão ou o rosto pouco à vista e com o borrão, e muda conforme o fluxo de saída |
| Mais de uma pessoa | funciona enquanto ninguém sai do quadro nem fica muito tempo atrás de outro; quantas cabem, só a interface informa |
| Câmera que se mexe | aceita em parte dos fluxos, com menos estabilidade quando ela treme, muda de ponto de vista de repente ou perde a pessoa atrás de algo |

## Depoimentos na página

| Quem | Fato |
|---|---|
| Cinemonster | compara com o Move One, que no lançamento saía tremido |
| Cascadeur | captura na QuickMagic, depois retarget, limpeza, poses e física secundária no Cascadeur |
| iClone | captura de corpo inteiro, parte de cima e dedos, integrada ao iClone |
| Defonten | gravou no quarto, baixou FBX e aplicou em personagens Paragon no Unreal |
| Dance with Miku | vídeo de celular aplicado a um MetaHuman no Unreal Engine 5 |
| Just a Simple Caveman | animação para o UEFN em poucos minutos |
| RyanReos | captura na QuickMagic e limpeza no Cascadeur |
| R2 Studio | mistura de animação manual e captura |
| Charlie Driscoll; Oby 1 | elogio sem detalhe de uso |

## O que a fonte recomenda

O vídeo deve mostrar a pessoa inteira, bem iluminada e sem ficar escondida, e o resultado se confere antes de exportar, sobretudo com câmera em movimento ou mais de uma pessoa. Quem pretende usar a animação em trabalho comercial deve ver o plano e o User Agreement, e garantir os direitos sobre o que enviou.

## Citações

- "Commercial-use rights depend on the plan and on the rights you hold to the uploaded footage, characters, audio, and other source materials." (FAQ)
- "Export availability varies by plan and workflow." (abertura e seção de exportação)
- "The current Pricing page lists 15-day asset storage for the Free plan and ongoing account storage for paid plans." (FAQ)

## Lacuna

A página não dá preço, nomes de plano, cotas, duração máxima de vídeo nem quais formatos cabem em cada plano; tudo isso fica na página de preços, que deu 403 e não foi lida. Não diz que planos permitem uso comercial nem o que o User Agreement exige, nem se o vídeo enviado ou o texto entram no treino de modelos. Não dá número de precisão, de taxa de quadros nem de número máximo de pessoas, e não diz quem é a empresa por trás do serviço.
