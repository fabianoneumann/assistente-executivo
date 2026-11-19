---
titulo: "Unreal® Engine End User License Agreement"
tipo: artigo
autor: "Epic Games"   # contrato e página de licença da própria Epic, sem assinatura de pessoa
url: "https://www.unrealengine.com/en-US/eula/unreal"
publicado_em: null   # o texto lido do EULA não traz data de versão, e o registro de alterações linkado no topo não foi aberto; a página de licença traz nos dados do HTML createdAt 2025-02-20 e updatedAt 2026-10-02
capturado_em: 2026-11-12
licenca: "protegido (contrato e página da Epic Games; sem licença de conteúdo declarada nos textos lidos); ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [licensing, commercial-use, pricing, royalty-free, unreal-engine, eula, royalties, seat-subscription, attribution, rendered-video, copyleft-incompatibility, metahuman]
---

# Unreal Engine: o vídeo renderizado sai sem royalty, e o assento só se paga acima de US$ 1 milhão

Ficha de estudo: o EULA vai na ordem das seções dele (o preâmbulo, as seções 1 a 18 e o Royalty Addendum), uma tabela por seção, com o que cada uma concede, exige ou proíbe, os números e as exceções; a página de licença vem à parte, no fim. É ficha de estudo porque a fonte é longa (o contrato inteiro, lido de ponta a ponta) e a ordem das seções é a forma de consulta do próprio contrato; a prosa fica para o que a fonte é, a recomendação e a lacuna. Não há integral: os dois textos são protegidos.

**Proveniência.** Textos da Epic Games sobre a própria engine, que ela licencia:

| Fonte | URL | Como foi lida | Data no texto | sha256 | O que o hash mede | Wayback |
|---|---|---|---|---|---|---|
| EULA (a principal) | https://www.unrealengine.com/en-US/eula/unreal | pelo Chrome em 2026-11-12 (o curl e o WebFetch deram 403): o `get_page_text` até 50 mil caracteres e o resto em fatias do `innerText`, gravado em `.txt` | nenhuma | (hash omitido) | o texto gravado pelo Chrome (57.605 caracteres) | `http://web.archive.org/web/20260301073606/https://www.unrealengine.com/en-US/eula/unreal` |
| Página de licença, em português do Brasil | https://www.unrealengine.com/en-US/license | pelo Chrome em 2026-11-12, a página inteira pelo `get_page_text`, gravada em `.txt`; o navegador a mostrou em português, com o preço em reais | nenhuma no texto | (hash omitido) | o texto gravado pelo Chrome | `http://web.archive.org/web/20260323205255/https://www.unrealengine.com/en-US/license` |
| Página de licença, HTML em inglês | a mesma | o HTML `en-US` guardado na rodada, lido nas respostas do FAQ (dados estruturados FAQPage) e nos exemplos dos cartões ("Show example"), que o texto do Chrome não traz abertos | `createdAt` 2025-02-20, `updatedAt` 2026-10-02 (dados da página) | (hash omitido) | o arquivo HTML inteiro (calculado nesta ficha; não é o do `protegidas.json`) | a mesma |

Títulos conferidos no texto: o EULA abre com "Unreal® Engine End User License Agreement"; o texto do Chrome da página de licença abre com "Licenciamento", e o `<title>` do HTML é "Unreal Engine (UE5) licensing options - Unreal Engine". O topo do EULA, no texto do Chrome, vem em português (o link do registro de alterações e as traduções de referência em japonês, coreano e chinês); o contrato em si está em inglês. Cobertura: o EULA inteiro (o preâmbulo, o sumário, as seções 1 a 18 e o Royalty Addendum, seções 1 a 7), lido de ponta a ponta para esta ficha; o rótulo da rodada registrava releituras do 3, 4(a), 6, 7(a), 8(a) e (b), 9(c) e do adendo. Da página de licença, o texto inteiro do Chrome (só a primeira resposta do FAQ vem aberta; as outras onze são só perguntas) e, do HTML em inglês, as doze respostas e os exemplos dos cartões. O `leitura/unreal-license-page.txt` da rodada é o texto do HTML em inglês (preço em dólar), não o do Chrome. Não foram abertos: o registro de alterações, as traduções de referência, os Termos de Serviço da Epic, as páginas de release e de marca, as licenças de terceiros na pasta da engine nem a página de aceite.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). O `parafrase.py` mediu a ficha contra os três textos juntos, num arquivo só na cópia de trabalho (o EULA do Chrome, a página de licença do Chrome e, do HTML em inglês, as perguntas e respostas do FAQ e os exemplos dos cartões) e saiu com o código 3 (ficha em português, fonte quase toda em inglês): 114 unidades medidas (23 de prosa, 91 de célula com texto); fora da conta, 326 células de fato, 50 de cabeçalho e 23 frases curtas demais para medir; 6 coladas de 114, todas células de nome e de lista (as lojas e o GitHub do 5(a) e do 6(d), os acordos substituídos do 8(b), a exclusão de vendas do 4(b)(v), o que vem incluído no plano grátis e as traduções do EULA no FAQ); 0 trecho de 3 ou mais seguidas. Pela conta lado a lado, sobre as mesmas unidades, 85 de 114 seguem uma frase da fonte (traduzem condensando, juntam duas ou fundem três ou mais seguidas na ordem dela): quase todas as células do contrato e da página, porque cada uma guarda o que uma cláusula concede, exige ou proíbe. Ficam fora da conta de "segue" a proveniência, esta linha, a frase de "Em uma frase", a célula de que o texto não tem cláusula de IA, o rótulo da exclusão de vendas, a célula do preço em dólar com a leitura do campo do HTML, o título da tabela do FAQ, as duas frases da recomendação e as três da lacuna. A maior sequência de unidades seguidas que seguem a fonte tem 36 (do preâmbulo ao 6(e)), e a segunda, 26 (do 7(a) ao 4(b) do adendo): são termos e números na ordem do contrato, como pede a ficha de estudo, e se declaram aqui. O contrato não tem texto argumentativo de autor; a recomendação e a lacuna juntam lugares distantes, em outra ordem.

## Em uma frase

Texto de quem licencia a engine: o EULA da Unreal deixa usar a engine de graça em particular, cobra royalty de 5% só do produto que leva o código dela e passa de US$ 1 milhão de receita, e cobra assento anual só de quem faz outro uso comercial com mais de US$ 1 milhão de receita do grupo em 12 meses; o vídeo renderizado e os assets feitos nela não pagam royalty.

## Preâmbulo

| Ponto | Fato |
|---|---|
| Objeto | a Unreal Engine e as atualizações dela ("Licensed Technology") |
| Usos citados | jogos; produção virtual para cinema e TV; visualização de arquitetura e automotiva; animação para entretenimento e publicidade; educação; simulação |
| Quando vale | no primeiro download ou uso |
| "Você" | a pessoa ou a empresa que age por ela |
| "Epic" | a empresa da Epic da região do licenciado (seção 10) |
| Aviso em caixa alta | renúncia a ação coletiva, com prazo para sair (seção 17); renúncia a júri |

## 1. O que se licencia

| Ponto | Fato |
|---|---|
| Entra | o código da engine (fonte e objeto), os Examples (pastas Samples e Templates) e o Starter Content |
| Entra também | a versão modificada pelo licenciado |
| Fica fora | o "Content" que a Epic oferece por outros caminhos, mesmo que funcione com a engine |
| Exemplo do que fica fora | o asset baixado de loja da Epic, como o Fab |

## 2. Como se pode usar

| Ponto | Fato |
|---|---|
| Licença | não exclusiva, intransferível, sem sublicença |
| Verbos | usar, reproduzir, exibir, executar e modificar, em particular |
| Limite | não violar o contrato (o teto de assentos do 6(a), por exemplo) nem a lei |
| "Products" | o que é feito com a engine ou a combina com outro software ou conteúdo |
| Distribuir | regido pelas seções 4 e 5 |

## 3. O que se paga

| Uso | Cobrança | Onde |
|---|---|---|
| Royalty Product | royalty sobre a receita bruta mundial do produto; sem assento | 3(a), adendo |
| Qualquer outro uso | assento por desenvolvedor, salvo exceção | 3(b), 6(a) |
| Exceções ao assento | amador; indie abaixo de US$ 1.000.000 por ano; não comercial; instituição de ensino | 6(b) |

## 4. Distribuir o que se fez

| Ponto | Fato |
|---|---|
| Regra geral | só como o 4 permite |
| Engine dentro do produto | só em código objeto e inseparável |
| "Distribute" | dar cópia a público ou a terceiro, ou pôr a função na rede |

**4(a), sem royalty, mesmo com o produto monetizado** (o assento do 6 pode valer):

| Caso | Condição | Exemplo do contrato |
|---|---|---|
| (i) Non-Engine Product | sem código da engine, sem precisar dela para rodar, sem Starter Content em formato fonte | arquivos de vídeo renderizado (transmissão, streaming, desenho animado, filme, imagem), mesmo mostrando Starter Content; asset feito com a engine, como modelo de personagem e animação, mesmo usado em outro motor |
| (i), ressalva | certos assets de acordos separados só servem com a Unreal | — |
| (ii) Receita indireta | nenhuma receita ligada ao acesso ao produto, a recurso dele ou a benefício dentro dele | configurador de carro grátis: o carro vendido por ele não paga |
| (iii)(A) Grupo | empresas do mesmo grupo, para uso privado, sem passar adiante | app interno compartilhado com matriz ou subsidiária |
| (iii)(B) Cliente único | encomenda por escrito que dá ao cliente a autoria ou cede o copyright; nenhum dos dois redistribui | app feito sob contrato para um cliente |
| (iii)(C) Local físico | uso só em lugar sob controle do licenciado ou do distribuidor autorizado | brinquedo de parque, fliperama, experiência em local |

**4(b), com royalty:**

| Ponto | Fato |
|---|---|
| Royalty Product | todo produto fora do 4(a) |
| Adiantamento para desenvolver | também entra no adendo |
| Piso | nada a pagar até o produto gerar mais de US$ 1.000.000 de receita bruta direta |
| Port | adaptação para outra plataforma, ou versão com crossplay ou multiplayer de jogabilidade parecida, de um Royalty Product já lançado |
| Exemplo | produto vendido ao público, ou pronto e vendido em particular, direto ou por distribuidor |

**4(c), usuário final e distribuidor:**

| Ponto | Fato |
|---|---|
| O usuário final pode | usar a engine só como parte do produto e no que o uso do produto pedir |
| Condição | EULA próprio que afaste garantias e responsabilidades sobre a engine |
| O usuário final não pode | pôr a engine nos produtos dele |
| Publisher e distribuidor | podem distribuir no lugar do licenciado, no mesmo limite do 4 |

## 5. Distribuir a engine fora de um produto

| Caso | Fato |
|---|---|
| (a)(i) Código da engine | a outro licenciado da mesma versão, em fonte ou objeto |
| (a)(i) Engine Tools em público | só por loja da Epic, como o Fab Marketplace, ou por fork da rede UnrealEngine no GitHub |
| (a)(ii) Trecho em fórum | até 30 linhas, para discutir o trecho ou para patch e plugin, sem servir a quem não tem licença |
| (b) Examples | a qualquer terceiro, em fonte ou objeto |
| (c) Integração de outra linguagem que não C++ | em código fonte, de graça, a todos os licenciados, sob licença que deixe redistribuir de graça |

## 6. Outras restrições

| Ponto | Fato | Onde |
|---|---|---|
| Quem precisa de assento | quem acessa a engine para fazer Royalty-Free Product, salvo o 6(b) | 6(a) |
| Assento | um usuário por assento, em assinatura com renovação automática | 6(a) |
| Vários computadores | um usuário em várias máquinas ocupa um assento | 6(a) |
| Uma máquina, dois usuários | dois assentos | 6(a) |
| Exemplo | quem só faz jogo para o público não compra assento; quem também faz para cliente ou uso interno, sim, para essas pessoas | 6(a) |
| Exceção pessoal e indie | o grupo com menos de US$ 1.000.000 de receita bruta nos últimos 12 meses | 6(b)(i) |
| O que conta na receita | adiantamentos e dinheiro captado | 6(b)(i) |
| Exceção educacional | escola ou biblioteca, só para fim educacional | 6(b)(ii) |
| Exceção não comercial | uso sem benefício comercial direto nem indireto | 6(b)(iii) |
| Empresa comercial | todo uso dela conta como comercial | 6(b)(iii) |
| Licenças incompatíveis | proibido combinar com GPL, LGPL (salvo link dinâmico de biblioteca) ou Creative Commons Attribution-ShareAlike | 6(c) |
| Engine Tools no produto | distribuição só pelo Fab Marketplace ou por fork no GitHub | 6(d) |
| Vetos gerais | violar a lei; alugar; apropriar-se de outro produto da Epic; sustentar alegação de patente contra a engine; dar a engine em garantia; distribuir fora do 4 e do 5 | 6(e) |
| Inteligência artificial | o texto lido não tem cláusula sobre IA (as palavras "artificial", "machine learning" e "generative" não aparecem) | todo o EULA |

## 7. Quem é dono do quê

| Ponto | Fato | Onde |
|---|---|---|
| Produtos | do licenciado, fora a engine | 7 |
| Engine | da Epic | 7 |
| Natureza | licença, não venda; nada implícito | 7 |
| Avisos da Epic | manter os que vêm na engine | 7(a) |
| Créditos | se o produto tiver créditos, dois avisos obrigatórios: "[Product name] uses Unreal® Engine", com a marca registrada, e o copyright da Epic de 1998 ao ano corrente | 7(a) |
| Marcas | nenhum direito sobre as marcas da Epic, inclusive Unreal Engine e MetaHuman | 7(a) |
| Uso maior das marcas | unrealengine.com/branding | 7(a) |
| Software de terceiros | licenças próprias, em `/Engine/Source/ThirdParty/Licenses` e `/Engine/Extras/ThirdPartyNotUE/` | 7(b) |
| Sugestões | a Epic usa livremente, sem crédito nem pagamento | 7(c) |
| Contribuições | licença ampla e irrevogável à Epic (fórum, wiki, GitHub da Epic) | 7(c) |
| Recursos na nuvem | a Epic usa o dado enviado só para atender o pedido e não o guarda | 7(d) |
| Dado com rosto de pessoa | o licenciado precisa dos direitos e dos consentimentos | 7(d) |

## 8 a 12. A relação com a Epic

| Ponto | Fato | Onde |
|---|---|---|
| Versão nova do contrato | aceite não obrigatório; a versão aceita continua valendo para o que já se tem | 8(a) |
| Sem aceitar a nova | sem certos serviços e sem baixar a engine | 8(a) |
| Aviso de mudança | por e-mail ou no próximo login | 8(a) |
| Acordos substituídos | para a engine, os antigos EULA for Publishing e for Creators e o EULA do MetaHuman Creator | 8(b) |
| O que sobra deles | só o que diz respeito a Content, até o aceite do Epic Content License Agreement | 8(b) |
| Licença sob medida | prevalece sobre este contrato nos produtos dela | 8(b) |
| Quem age por outro | obriga a pessoa ou empresa representada | 9(a) |
| Menor de idade | só com responsável que também aceite | 9(b) |
| Inelegível | quem está em lista de sanções dos EUA ou em país sob embargo | 9(b) |
| Conta | conta na Epic para acessar e baixar, sob os Termos de Serviço da Epic | 9(c) |
| "Users" | só pessoas com conta válida; na empresa, os funcionários e agentes | 9(c) |
| Instituição de ensino | pode instalar em todas as máquinas; os alunos não distribuem | 9(d) |
| Parte contratante | Epic Games, Inc. nos EUA; Epic Games Commerce GmbH fora deles | 10 |
| Privacidade | a Epic pode dar ao empregador o e-mail corporativo, a pedido dele, para conferir assentos | 11 |
| Auditoria | no máximo uma por 12 meses, por auditor independente, em horário comercial | 12 |
| Custo da auditoria | da Epic, salvo falta de mais de 5% no pagamento | 12 |

## 13 a 18. Garantias, responsabilidade e o resto

| Ponto | Fato | Onde |
|---|---|---|
| Garantia | nenhuma; engine "como está" | 13 |
| Teto da responsabilidade da Epic | o maior entre US$ 1.000 e o pago à Epic nos 12 meses anteriores | 14 |
| Indenização | o licenciado cobre a Epic em ação de terceiro ligada à violação ou aos produtos dele | 15 |
| Exceção | alegação de que a engine sem modificação infringe patente, marca ou copyright | 15 |
| Lei | Nova York | 16 |
| Foro | Supreme Court do condado de Nova York ou tribunal federal do Distrito Sul de Nova York | 16 |
| Ação coletiva | vetada | 17 |
| Sair da renúncia | carta à Epic em Cary, Carolina do Norte, em até 30 dias do primeiro aceite | 17 |
| Suporte | nenhuma obrigação; nem de manter versões para baixar | 18(a) |
| Cessão | o licenciado não cede; a Epic pode | 18(c) |
| Língua que vale | inglês; tradução só por conveniência | 18(e) |
| Fim do contrato | royalties devidos vencem na hora | 18(g) |

## Royalty Addendum

| Ponto | Fato | Onde |
|---|---|---|
| Quando vale | ao distribuir Royalty Product, ou ao gerar receita ou adiantamento antes disso | preâmbulo |
| Fora do adendo | Non-Engine Product; produto sem receita direta; grupo; cliente da encomenda; local físico | 1 |
| Aviso de lançamento | formulário em unrealengine.com/release antes de distribuir ou de começar a gerar receita | 2 |
| Taxa padrão | 5% da Royalty Revenue | 3(a) |
| Taxa reduzida | 3,5% para "Launch Everywhere with Epic Release", a partir da data em que o produto se qualifica | 3(b) |
| Perda da redução | volta a 5% da data em que deixa de se qualificar | 3(b) |
| Launch Everywhere, requisitos | a partir de 1º/01/2025; lançado em ao menos uma plataforma com a Epic Games Store; na loja da Epic antes ou junto das outras; paridade de conteúdo, recursos e marketing | 3(b) |
| iOS | requisito suspenso, por causa dos termos da Apple; a Epic avisa com 4 meses de antecedência antes de voltar | 3(b) |
| Base | receita bruta mundial do produto, quem quer que a receba | 4(a) |
| Entram | vendas; compras no app, DLC, assinatura, moeda virtual; financiamento coletivo ligado ao acesso; anúncios e afiliados; adiantamento; serviços como Apple Arcade e Game Pass; o mais atribuível ao produto | 4(a)(i)-(viii) |
| Exclusão trimestral | trimestre com receita bruta do produto abaixo de US$ 10.000 | 4(b)(i) |
| Exclusão vitalícia | o primeiro US$ 1.000.000 por produto | 4(b)(ii) |
| Exclusão vitalícia, Oculus Store | os primeiros US$ 5.000.000 por produto | 4(b)(iii) |
| Royalty já pago sobre adiantamento | vira crédito contra royalties futuros | 4(b)(iv) |
| Vendas no Fab Marketplace e na Epic Games Store | excluídas, e também as compras feitas depois dentro do produto se a Epic processar o pagamento | 4(b)(v) |
| Outras exclusões | venda só a licenciados da Unreal; produto que não é software (quadrinhos, trilha, roupa); prêmio em dinheiro; doação sem benefício; imposto cobrado do cliente; Epic MegaGrants | 4(b)(vi)-(xi) |
| Taxa da loja | não se desconta: a base é o preço cheio | 5 |
| Prazo | relatório por produto e pagamento até 45 dias depois de cada trimestre | 6 |
| Atraso | juros pela SOFR média de 30 dias ou o teto legal, o menor, compostos ao mês | 6 |
| Reembolso | nenhum, salvo a lei | 6 |
| Impostos | do licenciado; retenção na fonte com documento | 7(a) |
| Moeda | conversão para dólar por banco internacional ou site de câmbio reconhecido | 7(b) |

**Os exemplos de cálculo do adendo** (todos a 5%):

| Situação | Resultado | Onde |
|---|---|---|
| US$ 9.000 em cada um de dois trimestres | nada | 4(b) |
| US$ 9.000 e depois US$ 10.100 | nada no primeiro; US$ 505 no segundo, salvo outra exclusão | 4(b) |
| 90.000 cópias a US$ 10 | nada sobre os US$ 900.000 | 4(b) |
| Adiantamento de US$ 100.000 | nada | 4(b) |
| Adiantamento recuperável de US$ 1.100.000, depois US$ 500.000 em vendas | US$ 5.000 sobre o adiantamento; US$ 20.000 sobre as vendas, já com o crédito | 4(b) |
| 90.000 cópias a US$ 20 na Epic Games Store | nada sobre os US$ 1.800.000 | 4(b) |
| US$ 10 na App Store, com 30% da Apple | royalty de US$ 0,50 | 5 |
| US$ 1 milhão e depois US$ 9.000 | nada | 5 |
| US$ 1 milhão e depois US$ 10.100 | US$ 505 no segundo trimestre | 5 |

## A página de licença

| Ponto | Fato | Versão |
|---|---|---|
| Grátis abaixo de US$ 1 milhão | jogo (royalty depois de US$ 1 milhão de receita do produto); pessoa física e pequena empresa (menos de US$ 1 milhão de receita anual); educador e escola (sem teto) | Chrome, pt-BR |
| Incluído | código fonte; todas as plataformas e recursos; fóruns e documentação | Chrome, pt-BR |
| Modelo por royalty | para produto que carrega a engine em execução (jogo, app) e vai a terceiros: royalty no lugar do assento | Chrome, pt-BR |
| Exemplos do modelo por royalty | qualquer jogo; VR e experiência interativa para vender a consumidor ou a empresa | HTML, en |
| Custo por royalty | 5% sobre o que passar de US$ 1 milhão na vida do produto; o que se vende na loja da Epic não paga | Chrome, pt-BR |
| Depois de lançar | formulário de aviso de lançamento e relatório trimestral | Chrome, pt-BR |
| Modelo por assento | para os demais usos comerciais, quando a receita de 12 meses passa de US$ 1 milhão | Chrome, pt-BR |
| Exemplos do modelo por assento | conteúdo linear (cinema, TV, visualização de arquitetura, gráficos de transmissão e de evento ao vivo); configurador de produto; brinquedo de parque e passeio interativo | HTML, en |
| Preço do assento | R$ 6.682,00 por ano | Chrome, pt-BR |
| Preço do assento | US$ 1.850 por ano (no HTML, o cartão traz um campo a preencher pela localização, e o valor em dólar aparece fixo para Belarus, China e Rússia, que recebem "Contact us" no lugar da compra) | HTML, en |
| Moeda, pelo FAQ | preço ajustado em certos lugares; o valor final aparece antes de pagar | HTML, en |
| Teste | avaliação grátis de 30 dias | os dois |
| Epic Pro Support | compra à parte, para quem tem 10 assentos ou mais | os dois |
| Mais de 25 assentos ou licença sob medida | falar com a Epic | os dois |
| UEFN | pagamento por engajamento e transações nas ilhas do Fortnite | os dois |

**O FAQ** (as respostas, do HTML em inglês; no texto do Chrome, só a primeira vem aberta, em português):

| Pergunta | Resposta |
|---|---|
| O que é o EULA | o contrato que rege a engine; só o inglês é oficial, e o japonês, o coreano e o chinês servem de referência |
| Suporte | material grátis e fóruns; o Epic Pro Support para empresas com 10 assentos ou mais ou com termos sob medida |
| Quanto custa | grátis para estudante, educador, amador e a maior parte das empresas que não fazem jogo, abaixo de US$ 1 milhão de receita anual; royalty de 5% (com descontos possíveis) acima do primeiro milhão do produto; assento de US$ 1.850 por usuário por ano para as outras empresas acima de US$ 1 milhão |
| Lançar produto com royalty | aviso pelo Developer Portal antes; 5% acima do primeiro milhão; 3,5% desde 1º/01/2025 para quem lança na Epic Games Store antes ou junto; pagamento e relatório 45 dias depois do trimestre |
| Gerir assentos | pelo Developer Portal, na compra e depois |
| Assento para prestador de fora | permitido |
| O MetaHuman faz parte da engine | o MetaHuman Creator, o Animator e o Mesh to MetaHuman fazem parte; desde a 5.6, o uso entra na licença da Unreal |
| Não renovar | as ferramentas e os projetos ficam; para seguir usando, renovar, salvo receita abaixo de US$ 1 milhão |
| Quem faz plugin | não paga; na loja, fica com 88% da receita |
| Governo | grátis para uso não comercial; uso comercial por empresa terceira, nas regras dela |
| Os dois tetos de US$ 1 milhão | o royalty olha a receita vitalícia do produto; o assento, a receita anual da empresa nos últimos 12 meses ou no ano fiscal |
| Teto em dólar | sim, com conversão razoável |

## O que a fonte recomenda

Pelo contrato, o licenciado se pergunta primeiro se o que distribui leva o código da engine: o vídeo, a imagem e o asset exportado não levam e ficam fora do royalty, e aí a única conta que sobra é a do assento, que olha a receita do grupo nos últimos 12 meses. Quem tem créditos na obra põe os dois avisos da Epic, não mistura a engine com conteúdo copyleft e guarda registros que mostrem que está dentro das regras de assento e de royalty.

## Citações

- "rendered video files (e.g., broadcast or streamed video files, cartoons, movies, or images) created using the Engine Code" (EULA, 4(a)(i))
- "have generated less than $1,000,000 USD in gross revenue over the last 12 months, the Seat subscription requirement will not apply to your Users" (EULA, 6(b)(i))
- "you are not required to accept the amended Agreement, and this Agreement will continue to govern your use" (EULA, 8(a))

## Lacuna

O texto lido do EULA não traz data nem número de versão; o que mudou entre versões fica no registro de alterações, que não foi aberto. O contrato não diz como a pessoa física que também tem empresa soma a receita para o teto de US$ 1 milhão do assento, nem se essa receita conta antes ou depois de imposto. A página de licença não diz como chegou ao preço em reais nem se ele inclui imposto, e nenhuma das duas fontes diz quando o preço de US$ 1.850 passou a valer.
