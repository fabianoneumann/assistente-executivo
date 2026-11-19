---
titulo: "Cascadeur end-user agreement"
tipo: artigo
autor: "Nekki Limited"   # a empresa que licencia o Cascadeur (Chipre), parte do EULA; as três páginas não trazem assinatura de pessoa
url: "https://cascadeur.com/help/category/4"
publicado_em: 2025-07   # o EULA diz "VERSION 2025.1" e "JULY 2025", sem dia; a página de planos e o FAQ de licenças de 2024 não trazem data
capturado_em: 2026-11-12
licenca: "protegido (rodapé da página de planos e do FAQ: '© 2018-2026, Nekki Limited. All rights reserved.'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [cascadeur, licensing, commercial-use, pricing, revenue-threshold, perpetual-license, character-animation, interested-party]
---

# Cascadeur: Free sem uso comercial, Indie abaixo de US$ 100 mil por ano e Pro sem limite, com a licença perpétua no plano anual

Nota de fato: tabelas do que a página de planos, o FAQ de licenças de 2024 e o EULA do Cascadeur dizem sobre planos, preços, uso comercial e propriedade do que se cria, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: as três são protegidas. O formato é o da lista (nota de fato, uma tabela por tema), porque são termos de uso e páginas de venda lidos por partes.

**Proveniência.** Três páginas da Nekki, que vende o Cascadeur, sobre o próprio produto, baixadas com `curl` em 12/11/2026:

| Fonte | URL | Data no texto | sha256 | Wayback |
|---|---|---|---|---|
| EULA (a principal) | https://cascadeur.com/help/category/4 | "VERSION 2025.1", "JULY 2025" | (hash omitido) | `http://web.archive.org/web/20200918081156/https://cascadeur.com/help/category/4` |
| Planos e preços | https://cascadeur.com/plans | nenhuma; a faixa de promoção diz "From 16.06 till 24.06", sem ano | (hash omitido) | `http://web.archive.org/web/20261109124954/https://cascadeur.com/plans` |
| FAQ da nova estrutura de licenças | https://cascadeur.com/blog/general/cascadeurs-new-licensing-structure-comprehensive-faq | nenhuma; o texto fala da versão 2024.1 e de prazos de março a maio de 2024 | (hash omitido) | `http://web.archive.org/web/20260417154921/https://cascadeur.com/blog/general/cascadeurs-new-licensing-structure-comprehensive-faq` |

O que o hash mede: o texto extraído de cada página pelo `baixa.py` da rodada (`leitura/<id>.txt`; conferi que o sha256 de cada um bate), não o HTML. As três páginas não têm `<main>` nem `<article>`, e o texto extraído inclui o menu: no EULA, a árvore inteira da ajuda; nos planos, a lista de escolas e o formulário. O Wayback do EULA é de 2020, anterior à versão lida. Títulos conferidos no HTML: "Cascadeur end-user agreement" (o `<title>` e o `<h1>`, e o texto abre com "CASCADEUR END-USER LICENCE AGREEMENT"), "Cascadeur Pricing Plans" e, no FAQ, que não tem `<title>` preenchido, o título do post, "Cascadeur's New Licensing Structure: Comprehensive FAQ". Preços: os cartões da página de planos vieram em reais (R$, com os números no HTML), não em dólar; o FAQ da mesma página dá os preços em dólar. As células de marca da tabela "Compare Plans" (sim e não) são ícones, lidos pela classe do HTML (`--check` e `--cross`).

Cobertura: o EULA inteiro foi lido (o preâmbulo e as cláusulas 1 a 14), e a ficha tabela o preâmbulo e as cláusulas 1, 2, 3, 5, 6, 7, 10.2, 10.3 e 14.8; garantia (8), limites de responsabilidade (9), comunicação (11), dados pessoais (12), confidencialidade (13) e o resto da 14 ficam fora das tabelas. O rótulo da rodada registrou só as cláusulas 1.4, 1.6 e os tipos de licença; esta leitura foi além. Da página de planos: os cartões, a tabela de comparação, o texto da licença acadêmica (sem a lista de escolas e o formulário), o FAQ inteiro e as cinco janelas modais que estão no HTML. O FAQ de 2024: as 15 perguntas (0 a 14) e a introdução; os resumos de outros posts no pé ficaram fora.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), medido contra os três textos juntos num arquivo temporário (o EULA, os planos e o FAQ de 2024, nessa ordem), com 76 unidades medidas (25 de prosa, 51 de célula com texto) e 0 trechos de 3 ou mais; colada, 1 (a célula dos requisitos mínimos, uma lista de especificações). Na leitura lado a lado das mesmas 76 unidades, segue a fonte a que traduz uma frase ou uma alínea dela, junta duas ou funde três ou mais na ordem dela; a célula de rótulo e a frase que junta lugares distantes não contam. Resultado: 45 de 76, todas células das tabelas, que traduzem cada uma uma frase, uma alínea ou uma lista da fonte; nenhuma frase de prosa segue a fonte. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 18: as 16 da tabela do resto do EULA, do preâmbulo à 14.8, que segue a ordem das cláusulas, como pede a regra dos termos lidos por seção, e as duas primeiras células das janelas da página de planos, que vem depois do EULA no texto juntado; é texto de contrato e de dado, não argumentativo. Fora dela, a maior é de 4.

## Em uma frase

Texto de quem vende o Cascadeur: o plano Free não permite nenhum uso comercial e só exporta no formato próprio, o Indie permite o uso comercial a quem tem receita ou financiamento abaixo de US$ 100 mil em doze meses, o Pro e o Teams não têm teto, e o EULA de julho de 2025 deixa com o usuário a propriedade dos personagens, animações e cenas que ele cria.

## Os planos, pela página de planos

| Ponto | Free (na tabela, "Basic") | Indie | Pro | Teams |
|---|---|---|---|---|
| Assentos (cartão) | 1 | 1 | 1 | 2 a 6 |
| Mensal (cartão) | R$ 0 | R$ 105 | R$ 270 | R$ 270 por usuário |
| Anual, por mês (cartão) | R$ 0 | R$ 44 | R$ 182 | R$ 182 por usuário |
| Preço no FAQ da página | US$ 0 | US$ 96 por ano ou US$ 19 por mês | US$ 396 por ano ou US$ 49 por mês | US$ 396 por ano ou US$ 49 por mês |
| Uso comercial (tabela) | não comercial | abaixo de US$ 100 mil por ano | sem limite | sem limite |
| Exportação (tabela) | só CASC | CASC, FBX, DAE, USD, GLTF | CASC, FBX, DAE, USD, GLTF | CASC, FBX, DAE, USD, GLTF |
| Exportação (cartão do Free) | só .casc; .fbx e .dae não | — | — | — |
| Teste grátis | — | — | 14 dias | 14 dias |
| Licença perpétua (cartão) | — | no anual | no anual | — |
| Retargeting, interação com o ambiente, scene linking, autopose de quadrúpede (tabela) | não | não | sim | sim |
| Física, unbaking, inbetweening, autopose, autopose de dedos, rigging (tabela) | sim | sim | sim | sim |
| Recursos pagos do app de iOS (tabela) | não | não | sim | sim |
| Chat no Discord da equipe e chamada de 30 min de onboarding (tabela) | não | não | não | sim |

| Ponto | Fato | Onde |
|---|---|---|
| Plano Educational | US$ 49; só para professor, docente e instituição, não para aluno avulso | Planos, FAQ e texto acadêmico |
| Desconto do anual | "Save 32%" no seletor; no FAQ de 2024, o desconto de 32% no Pro anual é permanente | Planos, cartões; FAQ 2024, item 11 |
| Faixa de promoção | 25% de desconto, de 16.06 a 24.06, sem ano | Planos, topo |
| Instalação | até 3 computadores de mesa por assento; a licença só serve a quem a comprou | Planos, FAQ |
| Reembolso | pedido até 14 dias depois da compra inicial | Planos, FAQ |
| Línguas | software, documentação e EULA só em inglês; documentação com tradução automática em coreano, japonês e chinês | Planos, FAQ |
| Pagamento | pela Paddle (compra nova); quem comprou pela Xsolla renova por lá | Planos, FAQ |
| Requisitos mínimos | 64 bits com SSE4.1 (Windows e Linux) ou Apple ARM; 2,4 GHz; 4 GB; NVIDIA GTX 550 Ti ou melhor, com OpenGL 3.3 | Planos, FAQ |
| Sistemas | Windows 10 (1809 ou mais) e 11; Ubuntu 20.04 ou mais; macOS 13.3 ou mais, só em Mac ARM | Planos, FAQ |
| Recursos pagos no celular | exportar em FBX, GLB e CASC (FBX não no Android), vídeo de referência, vídeo sem marca d'água, tween machine | Planos, FAQ |

## A licença perpétua, em cada lugar

| Onde | O que diz |
|---|---|
| Planos, texto acima dos cartões | Indie e Pro anuais dão acesso às versões maiores lançadas durante a assinatura, e aos hotfixes delas, para usar depois que ela acaba |
| Planos, FAQ | Indie e Pro anuais viram perpétua depois do prazo mínimo de um ano; o mensal não; o Teams anual não |
| Planos, janela "Version 2019.5b" | a perpétua não vale para o Cascadeur Mobile nem para o Teams |
| EULA, 2.2(b) e (c) | Indie e Pro viram perpétua da última versão lançada na assinatura quando ela acaba; o texto dessas alíneas não fala de plano anual |
| EULA, 2.2(d) | o Teams não vira perpétua |
| FAQ 2024, item 1 | o Indie ganho de graça na transição vira perpétua depois dos dois anos grátis |

## O que é uso comercial e o teto do Indie (EULA, 1.4 e 1.6)

| Ponto | Fato |
|---|---|
| Uso comercial abrange | licenciar, publicar, pôr à disposição, comunicar ao público, explorar ou usar de forma não privada obra que contenha animação feita com o software; usar o software para prestar serviço |
| Condição | visando receita, pagamento ou outro valor, real ou pretendido |
| Fora do uso comercial | instituição de caridade registrada (não o braço comercial); escola, para fins só educativos; obra promocional e limitada, a critério da Nekki, em YouTube ou canal parecido de acesso grátis |
| Teto do Indie | receita bruta ou financiamento somados abaixo de US$ 100.000 nos doze meses até o download e em cada renovação, ou outro valor que o site indique |
| Moeda | converter para dólar pela cotação do Financial Times no dia do download |
| Pessoa física que usa para si | conta o que ganha com o uso do software (vender um jogo feito com ele conta; dar aula de música, não) |
| Empresa | conta tudo o que recebe, de qualquer fonte |
| Caridade ou entidade sem fins lucrativos | conta o orçamento e as doações recebidas |
| Se deixar de caber | avisar na hora e comprar o tipo certo ou parar de usar |
| E-mail de domínio de empresa | o uso conta como da empresa, que precisa caber no teto |
| Free | proíbe qualquer uso comercial e não tem usuários autorizados (2.2(a)) |
| Pro Trial e Educational | proíbem o uso comercial (2.2(e) e (f)) |

## O resto do EULA lido

| Cláusula | Fato |
|---|---|
| Preâmbulo | o licenciante é a Nekki Limited, de Limassol, Chipre; o software se licencia, não se vende |
| Preâmbulo | o direito de desistir acaba ao baixar o software, salvo o que o acordo mantém |
| 1.1 | é preciso registrar no site; a Nekki pode recusar o registro sem dar motivo |
| 1.3 | quem tem Pro e não cabe no Indie não pode pôr usuários no Free ou no Indie; pode ter um Free pessoal, em outro login |
| 1.7 | Educational exige matrícula ou vínculo de ensino e o e-mail da instituição |
| 2.1 | licença não exclusiva, intransferível, sem sublicença, para usar só no país do cadastro |
| 2.2(b) | Indie: até três usuários autorizados |
| 2.2(c) | Pro (individual): uma licença por pessoa |
| 2.2(d) | Teams: vale sozinho quando a mesma pessoa ou empresa compra mais de um Pro |
| 2.4 | instalar em até três unidades, sem usar em mais de uma ao mesmo tempo; uma cópia de segurança |
| 3(g) | não usar o software por rede ou acesso remoto |
| 5.2 | mudança de preço com 30 dias de aviso; no anual, só na renovação |
| 6.3 | o usuário fica com a propriedade intelectual dos personagens, animações, cenas e outros conteúdos que cria ou importa, e responde por eles |
| 7.1 a 7.3 | a IA do software ajuda a posicionar poses e a gerar a interpolação entre quadros-chave, sempre a pedido e sob controle do usuário |
| 7.4 | a saída da IA pode vir errada; sem garantia de acerto |
| 10.2 | o consumidor pode desistir até baixar o software ou até o 14º dia depois do registro, o que vier antes |
| 10.3(c) | a Nekki pode encerrar com 30 dias de aviso se parar de manter o software, devolvendo a parte não usada |
| 14.8 | a Nekki muda o acordo publicando a versão nova no site, com efeito imediato; quem não aceitar pode sair com reembolso proporcional |

## As janelas da página de planos e a transição de 2024

| Ponto | Fato | Onde |
|---|---|---|
| Limite de exportação "da versão grátis" | 300 quadros e 120 articulações por cena | Planos, janela "Animation Export limit" |
| Quem pode usar "a versão grátis" | quem tem receita ou financiamento abaixo de US$ 100 mil nos doze meses até o download, com a conversão pelo Financial Times e os casos da cláusula 1.6, mais um: a pessoa física ou empresa de serviço pessoal, em que conta o que recebem os clientes que a contratam | Planos, janela "Revenue/funding requirements" |
| Crédito | a Nekki pede esforço razoável para dizer que a animação foi feita no Cascadeur ao mostrar, vender ou licenciar a obra | Planos, janela "Mention the use of Cascadeur in the credits" |
| Crédito no EULA | não há cláusula de crédito no texto lido | EULA |
| Antes de 2024.1 | os planos eram Basic e Pro | FAQ 2024, introdução |
| Indie de graça por dois anos, usuário do Free | conta registrada antes de 1º/3/2024, pedido no menu Help da 2024.1 | Planos, janela "Announcement" |
| Indie de graça por dois anos, usuário do Pro | conta registrada antes de 19/3/2024, uma vez, até 20/5/2024, pelo suporte; quem teve Pro ativo entre 19/3 e 19/5/2024 pode pedir a qualquer tempo | FAQ 2024, item 3 |
| Prazo da oferta | 19 de maio (item 2); 20 de maio de 2024 (item 3) | FAQ 2024 |
| Indie diante do antigo Basic | ganha autopose de dedos e layout personalizável, antes só do Pro, e perde o limite de 300 quadros e o de articulações | FAQ 2024, itens 5 e 10 |
| Assinante antigo | renova pelo preço original enquanto a assinatura seguir ativa | FAQ 2024, item 4 |
| Versões antigas | seguem disponíveis; o EULA novo vale para todas | FAQ 2024, itens 6 e 7 |
| Versão anterior à 2024.1 | serve para exportar, com o teto de US$ 100 mil por ano para projeto comercial | FAQ 2024, item 13 |

## O que a fonte recomenda

Quem vai publicar ou vender obra com animação do Cascadeur precisa de um plano pago: o Free e o Educational vetam o uso comercial, e só a peça promocional e limitada num canal grátis como o YouTube escapa da definição. No Indie, a conta da receita se refaz a cada renovação e se informa quando a Nekki pedir; a perpétua só vem com o pagamento anual, e o crédito ao Cascadeur aparece como pedido na página de planos, não como regra do acordo.

## Citações

- "by posting promotional and reasonably limited (in our discretion) works to Youtube or similar channels which can be accessed free of charge" (EULA, 1.4(c))
- "you retain ownership of the intellectual property rights in the characters, animations, scenes or other content you create or import when using the Software" (EULA, 6.3)
- "aggregate gross revenue or funding (from any source of financing) must be less than $100,000 per year" (Planos, FAQ)

## Lacuna

Nenhuma das três páginas diz quanto vale o "reasonably limited" da exceção do YouTube, nem se um canal com anúncio ou um post patrocinado ainda conta como acesso grátis. A página de planos não explica a base do "Save 32%", não converte os preços em reais para o dólar do próprio FAQ, nem diz de que ano é a promoção de junho. As janelas modais ("versão grátis" com teto de receita e limite de 300 quadros) não dizem a que plano ou época se referem, e o FAQ de 2024 não tem data nem diz se foi atualizado. O EULA não trata de crédito, de vídeo gerado com ajuda de outra IA a partir da animação, nem de uso da animação para treinar modelo.
