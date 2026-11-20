---
titulo: "Rokoko Software Ecosystem Plans & Prices"
tipo: artigo
autor: "Rokoko Electronics ApS"   # a empresa dinamarquesa que vende o Studio, o Create e o Vision, parte dos termos; as páginas não trazem assinatura de pessoa
url: "https://www.rokoko.com/pricing"
publicado_em: null   # a página de preços e a do Vision não trazem data; os termos dizem "Effective date: 16 July 2026 (Version 2.0.1)"
capturado_em: 2026-11-12
licenca: "protegido (rodapé das três páginas: '© Rokoko'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [rokoko, motion-capture, video-to-motion, pricing, licensing, ai-training-restriction, character-animation, retargeting, interested-party]
---

# Rokoko Vision: mocap por vídeo de graça até 30 segundos por mês, planos de US$ 10 a 50 e termos que vetam treinar IA com os assets

Nota de fato: tabelas do que a página de preços, a página do Vision 3.0 e os termos de uso dos serviços da Rokoko dizem sobre planos, limites, o que o mocap por vídeo faz e não faz e o uso do que se cria, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: as três são protegidas. O formato é o da lista (nota de fato), porque são página de venda e termos lidos por seções.

**Proveniência.** Três páginas da Rokoko, que vende o que descreve, baixadas com `curl` em 12/11/2026:

| Fonte | URL | Data no texto | sha256 | Wayback |
|---|---|---|---|---|
| Preços (a principal) | https://www.rokoko.com/pricing | nenhuma | (hash omitido) | `http://web.archive.org/web/20261030055841/https://www.rokoko.com/pricing` |
| Vision 3.0 | https://www.rokoko.com/products/vision | nenhuma | (hash omitido) | `http://web.archive.org/web/20261025150457/https://www.rokoko.com/products/vision` |
| Termos de uso dos serviços | https://www.rokoko.com/studio-term-of-use | "Effective date: 16 July 2026 (Version 2.0.1)" | (hash omitido) | `http://web.archive.org/web/20260114073747/https://www.rokoko.com/studio-term-of-use` |

O que o hash mede: o texto do bloco `<main>` de cada página, sem tags, script e estilo, extraído pelo `baixa.py` da rodada (`leitura/<id>.txt`; conferi que o sha256 de cada um bate). Títulos conferidos no HTML: "Rokoko Software Ecosystem Plans & Prices" (`<title>`) e "Rokoko Pricing Plans" (`<h1>`); "Rokoko Vision: AI motion capture from video, start for free" e "Vision 3.0 AI motion capture from your own video"; "Rokoko Services - Standard Terms of Use" e "Rokoko Terms of Use". O `<h1>` e o parágrafo de abertura da página do Vision ficam fora do `<main>` e foram lidos no HTML. As células de sim e não da tabela de comparação de preços são ícones, lidas pelo desenho do SVG de cada célula (o X e o visto). O link "Studio, Preview and Vision - Terms of Use" da página do Vision leva a `/terms-of-use-update`, que não foi aberto; a cláusula 12.1 dos termos lidos dá como endereço da versão mais nova `https://www.rokoko.com/services-terms-of-use`, outro endereço que o da `url` lida.

Cobertura: a página de preços inteira (o seletor anual e mensal, os cinco cartões nas duas cobranças, a faixa do Enterprise, a tabela de comparação e as quatro perguntas do FAQ); a página do Vision inteira (abertura, os blocos de novidade, os quatro passos, os cartões de preço, a comparação com concorrentes, os depoimentos e as seis perguntas do FAQ); os termos inteiros (cláusulas 1 a 14). As páginas ligadas ("What has changed", "See the full comparison", a política de privacidade) não foram abertas.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), medido contra os três textos juntos num arquivo temporário (preços, Vision e termos, nessa ordem), com 56 unidades medidas (21 de prosa, 35 de célula com texto), 0 coladas e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 56 unidades, segue a fonte a que traduz uma frase ou uma cláusula dela, junta duas ou funde três ou mais na ordem dela; a célula de rótulo e a frase que junta lugares distantes não contam. Resultado: 33 de 56, todas células das tabelas (as listas dos cartões, a faixa do Enterprise, a linha do teste, as do Vision e as 19 cláusulas dos termos); nenhuma frase de prosa segue a fonte. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 20: a célula da oclusão, do FAQ do Vision, e as 19 da tabela dos termos, que segue a ordem das cláusulas, como pede a regra dos termos lidos por seção; é texto de contrato e de dado, não argumentativo. Fora dela, a maior é de 5 (as listas dos quatro cartões e a faixa do Enterprise).

## Em uma frase

Texto de quem vende o Rokoko Vision: o mocap tirado de um vídeo comum de uma pessoa sai de graça até 30 segundos de processamento por mês e em planos de US$ 10 a 50 por mês no anual, exporta FBX ou BVH pelo Studio, e os termos de julho de 2026 deixam o conteúdo com o usuário, mas vetam usar os assets da Rokoko para treinar IA e dão à Rokoko o direito de usar o conteúdo, em forma anônima, para melhorar os serviços e sublicenciar a terceiros.

## Os planos, pelos cartões da página de preços

| Ponto | Starter | Basic | Plus | Pro | Enterprise |
|---|---|---|---|---|---|
| Por mês, cobrança anual | US$ 0 | US$ 10 | US$ 20 | US$ 50 | a partir de US$ 100 |
| Por mês, cobrança mensal | US$ 0 | US$ 12 | US$ 28 | US$ 70 | a partir de US$ 150 |
| Vision AI (processamento de vídeo) | 30 s por mês | 600 s por mês | 3.000 s por mês | 15.000 s por mês | — |
| Vision no período de teste (anual) | — | 30 s | 30 s | 30 s | — |
| Clipes de texto-para-movimento | sem limite | sem limite | sem limite | sem limite | — |
| Clipes de texto-para-movimento levados ao Studio | 5 por mês | 100 por mês | 1.000 por mês | sem limite | — |
| Nuvem | 1 mês | sem limite | sem limite | sem limite | armazenamento local, sem nuvem |
| Exportação | FBX | mais BVH ("BHV" no cartão) e opções avançadas | idem | mais CSV | idem |
| O que o plano acrescenta | gravar e exportar mocap; filtros de limpeza | importar e fazer retarget de personagem próprio; suavização e laço | transmissão ao vivo a outro programa; equipe sem limite; esqueletos próprios; suporte por chat e e-mail | captura de rosto; API de comando avançada; mensagens UDP; gerente de sucesso | dias offline a mais, horário de suporte, onboarding e SLA sob medida |

| Ponto | Fato |
|---|---|
| Seletor da cobrança | anual, marcado "-30% off", ou mensal, para todos os cartões |
| Enterprise, na faixa abaixo dos cartões | preço sob medida, armazenamento local, suporte dedicado e onboarding próprio, para estúdios e equipes maiores |

## A tabela de comparação da mesma página

| Ponto | Starter | Basic | Plus | Pro |
|---|---|---|---|---|
| Preço no topo da tabela | grátis | US$ 20 por mês (anual) | US$ 50 por mês (anual) | "Contact us" |
| Dias offline até logar de novo | 1 | 3 | 7 | 21 |
| Atores simultâneos com traje | 3 | 3 | 3 | 3 |
| Perfis de ator salvos | 3 | 5 | 10 | 50 |
| Personagem próprio | não; só malhas padrão | sim | sim | sim |
| Transmissão ao vivo (Unreal, Unity, Blender, Maya, Cinema 4D, MotionBuilder, iClone, Houdini, VRChat, Cartoon Animator 4) | não | não | sim | sim |
| Biblioteca de movimentos | sim | sim | sim | sim |
| Captura de rosto, mensagens UDP, CSV | não | não | não | sim |
| BVH, opções avançadas de exportação, suavização e laço | não | sim | sim | sim |
| Criadores (admin) e membros (editor) | 1 e 0 | 1 e 0 | sem limite | sem limite |
| Suporte | central de ajuda, chatbot, comunidade | idem | e-mail e chat | e-mail, chat e consulta individual |
| Prazo de resposta | não se aplica | até 4 dias úteis | até 3 dias úteis | até 2 dias úteis |
| Suporte a rigging | não | não | só personagens da Rokoko | só personagens da Rokoko |

## Onde a página de preços diz coisas diferentes

| Ponto | Cartões | Tabela de comparação | FAQ da página |
|---|---|---|---|
| Preço anual do Basic, Plus e Pro | US$ 10, 20 e 50 | US$ 20, 50 e "Contact us" | — |
| BVH | do Basic para cima | do Basic para cima | Plus e Pro |
| CSV | Pro | Pro | Pro e Enterprise |
| Vision nos planos pagos | 600 a 15.000 s por mês | 600 a 15.000 s por mês | os pagos liberam captura do Vision "unlimited" |
| Transmissão ao vivo | do Plus para cima | do Plus para cima | os planos pagos liberam |
| Retarget de personagem próprio | do Basic para cima | linha: do Basic para cima; dica da linha: malha própria "for 'Plus' plans and above" | — |
| Teste | "30s during trial" nos cartões anuais pagos | — | teste grátis de 7 dias do Plus ou do Pro para toda conta nova |
| Integrações em tempo real | — | dez programas | oito (sem VRChat e Cartoon Animator 4) |

## O Vision 3.0, pela página do produto

| Ponto | Fato |
|---|---|
| O que é | mocap por IA a partir de um único vídeo, sem traje nem marcadores |
| Onde roda | no navegador, dentro do Rokoko Create, junto com o texto-para-movimento |
| O que mudou | o solver monocular foi refeito do zero |
| Passo 1 | gravar com qualquer câmera ou usar qualquer vídeo com o movimento |
| Passo 2 | subir o vídeo no Create |
| Passo 3 | levar ao Studio para ver, editar, fazer laço e aplicar a personagem próprio |
| Passo 4 | exportar FBX ou BVH com esqueleto HIK, Mixamo ou outro |
| Esqueletos citados | UE5 Manny, HIK, Mixamo |
| Programas citados | Blender, Unreal, Unity, Cinema 4D, Maya, Houdini, MotionBuilder, iClone |
| Dedos | não no lançamento; para dedos, as luvas Smartgloves II |
| Webcam ao vivo | retirada; segundo a página, mais de 90% gravavam antes e subiam o arquivo |
| Duas câmeras | encerrada cerca de 30 dias depois do lançamento do 3.0 |
| Pessoas por vídeo | segundo a página, nenhuma ferramenta de mocap por IA capta bem mais de uma; os trajes inerciais captam até 5 |
| Oclusão | membro escondido ou fora do quadro piora o rastreio |
| Tempo real | não; o vídeo precisa de processamento antes |
| Fundo, luz e distância | pesam na qualidade do vídeo e da animação |
| Usos indicados | porta de entrada no mocap; pré-visualização |

| Comparação da página (sem data nem fonte) | Preço por minuto | Processamento incluído |
|---|---|---|
| Rokoko Vision, Basic | US$ 1 | 10 min |
| QuickMagic, Starter | US$ 4 | 2,5 min |
| Uthana, Indie | US$ 3 | 1 a 2,5 min |

## Os termos de uso (versão 2.0.1, de 16/07/2026)

| Cláusula | Fato |
|---|---|
| 1.1 | a empresa é a Rokoko Electronics ApS, da Dinamarca; os termos cobrem o Studio, o Studio Preview e o Create |
| 1.5 | seguir usando depois de uma mudança vale como aceitar a mudança |
| 2.2 | cada login é de uma pessoa só; vetado dividir |
| 2.3 | a Rokoko pode mudar, encerrar ou repreçar os planos quando quiser |
| 2.4 | a mensalidade ou anuidade se conta por usuário registrado |
| 2.6 | preços em dólar, sem IVA, impostos e tarifas |
| 3.1 | conteúdo do usuário inclui animações, modelos 3D, imagens e áudio; a Rokoko não reivindica a propriedade dele |
| 3.3 | a Rokoko não tem dever de guardar cópia do conteúdo apagado ou da conta fechada |
| 3.4 | a Rokoko pode coletar e usar o conteúdo, os dados de uso e os técnicos para prestar e melhorar os serviços, melhorar outros produtos dela e sublicenciar a terceiros, de forma anônima, para que melhorem os produtos deles |
| 4.1 | licença limitada, revogável, não exclusiva, sem sublicença e intransferível, enquanto houver conta válida |
| 4.3 | instalar em quantos computadores próprios quiser |
| 4.4 | vetado acessar os serviços por meio automático, como script ou robô, sem acordo à parte |
| 5.1 | os assets da Rokoko incluem amostras da empresa e os da biblioteca de movimentos, que são de terceiros; a licença de cada um dura enquanto houver conta |
| 5.3 | pode baixar e copiar os assets para fins legítimos; a cópia que entra numa produção de mídia digital é reconhecida; redistribuir, sublicenciar ou alugar, não, salvo licença própria do asset |
| 5.4 | vetado usar os assets para desenvolver, treinar ou melhorar modelo de IA, comercial ou não, sem consentimento por escrito |
| 6.3 | o usuário fica com os direitos do conteúdo e dá à Rokoko um direito perpétuo, mundial, grátis e sublicenciável de usar, copiar e modificar, só para prestar os serviços e o que os termos preveem; o conteúdo se anonimiza e nenhum subcontratado ou licenciado o distribui na forma original |
| 8.1 | a assinatura se renova sozinha; o preço da renovação é o vigente |
| 8.4 | ao fim da licença, a Rokoko pode apagar a conta e o conteúdo |
| 9.1 | cada parte consente que a outra use o nome dela em marketing |
| 11.1 | responsabilidade limitada ao que o usuário pagou nos últimos seis meses |
| 12.1 | mudança dos termos com um mês de aviso |
| 14.1 | lei da Dinamarca; arbitragem simplificada no Danish Institute of Arbitration |

## O que a fonte recomenda

A página põe o Vision como entrada barata no mocap: gravar antes, com o corpo inteiro no quadro e uma pessoa por vez, subir o arquivo e limpar no Studio, deixando dedos, tempo real e vários atores para os trajes. Os termos pedem respeito à licença de cada asset, que dura enquanto a conta existir, vetam treinar IA com eles e lembram que a assinatura se renova sozinha pelo preço do dia.

## Citações

- "You may not use any assets obtained or provided under this agreement for the purpose of developing, training, or enhancing machine learning and/or AI models or algorithms" (termos, 5.4)
- A Rokoko pode sublicenciar isso a terceiros de forma anonimizada, sem redistribuir nunca na forma original (termos, 3.4).
- Exportar e usar em qualquer projeto, inclusive comercial (preços, dica da biblioteca de movimentos).

## Lacuna

Nenhuma das três páginas diz em palavras que a animação tirada de um vídeo pelo Vision, ou gerada por texto, pode ir a obra comercial em cada plano, inclusive no Starter; os termos só dizem que a Rokoko não reivindica a propriedade. Os termos não dizem o que acontece com a obra já publicada que contém um asset da biblioteca quando a conta acaba. A página do Vision não dá duração máxima, resolução ou taxa de quadros do vídeo de entrada nem a taxa de quadros da animação exportada, e a comparação com QuickMagic e Uthana não tem data nem diz de onde vieram os números. Não há data em nenhuma das páginas de venda.
