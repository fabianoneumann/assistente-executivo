---
titulo: "Epic Content License Agreement"
tipo: artigo
autor: "Epic Games"   # contrato e página de licença da própria Epic, sem assinatura de pessoa
url: "https://www.unrealengine.com/eula/content"
publicado_em: 2026-02-23   # metadado do HTML: createdTimestamp e lastModifiedTimestamp do corpo do acordo; a página tem updatedAt 2026-10-12; o texto lido não traz data
capturado_em: 2026-11-12
licenca: "protegido (contrato e página da Epic Games; sem licença de conteúdo declarada nos textos lidos); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [licensing, commercial-use, rendered-video, 3d-assets, unreal-engine, metahuman, megascans, ue-only-content, ai-training-restriction, noai, copyleft-incompatibility]
---

# Epic: o conteúdo da Epic entra livre em vídeo renderizado, e o MetaHuman fica, pelo adendo, só na Unreal

Nota de fato: uma tabela por seção do Epic Content License Agreement, na ordem do documento (as seções 1 a 17 e os quatro adendos), e uma seção à parte para a página de licença do MetaHuman, com prosa só para dizer o que as fontes são, o que recomendam e o que falta. Cada documento vai como diz; os dois não se conciliam aqui. Não há integral: os dois textos são protegidos.

**Proveniência.** Dois textos da Epic Games sobre o conteúdo que ela própria licencia:

| Fonte | URL | Como foi lida | Data | sha256 | O que o hash mede | Wayback |
|---|---|---|---|---|---|---|
| Epic Content License Agreement (a principal) | https://www.unrealengine.com/eula/content | HTML baixado com curl em 2026-11-12 e lido no texto extraído do bloco principal, conferido no HTML | nenhuma no texto; no HTML, o corpo do acordo tem `createdTimestamp` e `lastModifiedTimestamp` 2026-02-23, e a página, `createdAt` 2025-10-10 e `updatedAt` 2026-10-12 | (hash omitido) | o texto do bloco `<main>`/`<article>`, sem tags, script e estilo | `http://web.archive.org/web/20261012094709/https://www.unrealengine.com/eula/content` |
| (o mesmo, arquivo) | — | — | — | (hash omitido) | o arquivo HTML inteiro (calculado nesta ficha) | — |
| Página de licença do MetaHuman | https://www.metahuman.com/license | HTML baixado com curl em 2026-11-12: o parágrafo de abertura e as perguntas, no texto extraído; as doze respostas do FAQ, nos dados estruturados (FAQPage, JSON-LD) do mesmo HTML | nenhuma no texto; no HTML, `createdAt` 2025-05-26 e `updatedAt` 2026-02-02 | (hash omitido) | o texto do bloco `<main>`/`<article>` (a abertura e as perguntas, sem as respostas) | `http://web.archive.org/web/20261104193949/https://www.metahuman.com/license` |
| (o mesmo, arquivo) | — | — | — | (hash omitido) | o arquivo HTML inteiro, onde estão as respostas (calculado nesta ficha) | — |

Títulos conferidos: o texto do acordo abre com "Epic Content License Agreement" (o `og:title` é "Epic Content EULA", e o `<title>` do HTML é o genérico do site, "The most powerful real-time 3D creation tool - Unreal Engine"); a página do MetaHuman tem `<title>` "MetaHuman | Licence - MetaHuman", `og:title` "Licensing MetaHuman" e abre com "Licensing". O texto extraído do acordo tem o tamanho do texto do HTML e termina no adendo de Tools, como o HTML. Cobertura: o acordo inteiro (o preâmbulo, o sumário, as seções 1 a 17 e os adendos de Marketplace, Megascans, MetaHuman e Tools), lido de ponta a ponta para esta ficha; o rótulo da rodada registrava a leitura da 1, da 3(b), da 5(a) e (b), da 17 e dos adendos. A palavra "Fab" não aparece no acordo. Da página do MetaHuman, a abertura e o FAQ inteiro: as respostas não aparecem no texto extraído, que só traz as perguntas, mas estão nos dados estruturados do HTML, e foi de lá que se leram (o rótulo dizia que não vinham). Não foram abertos o registro de alterações do acordo, as traduções de referência, os Termos de Serviço da Epic, o EULA do Fab (a "Standard License" que a página do MetaHuman cita) nem a página da Unreal a que o FAQ remete.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). O `parafrase.py` mediu a ficha contra os textos juntos, num arquivo só na cópia de trabalho (o texto extraído do acordo, o da página do MetaHuman e as perguntas e respostas do FAQ tiradas dos dados estruturados do HTML) e saiu com o código 3 (ficha em português, fonte em inglês): 83 unidades medidas (21 de prosa, 62 de célula com texto); fora da conta, 201 células de fato, 45 de cabeçalho e 16 frases curtas demais para medir; 3 coladas de 83, todas células de nomes (os lugares de onde vem o conteúdo na seção 1, o que é da Epic no adendo do MetaHuman e o MetaHuman for Maya e for Houdini no FAQ); 0 trecho de 3 ou mais seguidas. Pela conta lado a lado, sobre as mesmas unidades, 56 de 83 seguem uma frase da fonte (traduzem condensando, juntam duas ou fundem três ou mais seguidas na ordem dela): todas as células do acordo e da página, cada uma com o que uma cláusula ou uma resposta diz. Ficam fora da conta de "segue" a proveniência, esta linha, a frase de "Em uma frase", o título da tabela do FAQ, as duas frases da recomendação e as três da lacuna. A maior sequência de unidades seguidas que seguem a fonte tem 47 (do preâmbulo do acordo à abertura da página do MetaHuman), e a segunda, 9 (as respostas do FAQ): são termos na ordem do documento, como pede a nota de fato com uma tabela por seção, e se declaram aqui. O acordo e a página não têm texto argumentativo de autor; a recomendação e a lacuna juntam lugares distantes, em outra ordem.

## Em uma frase

Textos de quem licencia o conteúdo: o acordo de conteúdo da Epic deixa distribuir livremente o conteúdo dela quando vai embutido em vídeo ou imagem renderizada, mas o adendo do MetaHuman restringe o MetaHuman a "UE-Only Content", e a página de licença do MetaHuman diz que ele pode ser usado com qualquer engine ou software criativo.

## Preâmbulo

| Ponto | Fato |
|---|---|
| Objeto | o conteúdo digital que a Epic oferece ("Licensed Content") |
| Quando vale | ao baixar ou usar |
| Com quem se contrata | com cada Content Licensor; é a Epic, salvo quando outro aparece como licenciante no acesso |
| Aviso em caixa alta | renúncia a ação coletiva, com prazo para sair (seção 15) |

## 1. O que se licencia

| Ponto | Fato |
|---|---|
| Entra | todo conteúdo oferecido por um Content Licensor sob este acordo |
| Exemplos dados | o Unreal Engine Marketplace; a aba Learn do Epic Games Launcher; a biblioteca Quixel Megascans |

## 2. Como se pode usar

| Ponto | Fato |
|---|---|
| Licença | não exclusiva, intransferível, sem sublicença |
| Verbos | usar, reproduzir, exibir, executar e modificar, em particular |
| Limite | não violar o acordo nem a lei |
| Compartilhar | regido pelas seções 3 e 4 |

## 3. Compartilhar projetos feitos com o conteúdo

| Ponto | Fato | Onde |
|---|---|---|
| "Projects" | o que junta o conteúdo a outro software ou conteúdo, em qualquer proporção | 3 |
| Regra geral | só se distribui como o acordo permite | 3 |
| Em software | só em código objeto e inseparável do projeto | 3(a) |
| Usuário final | usa o conteúdo só dentro do projeto, sob EULA que afaste garantias | 3(a) |
| Publisher e distribuidor | no mesmo limite do licenciado | 3(a) |
| Exemplo | jogo com o conteúdo, vendido ao público, direto ou por publisher | 3(a) |
| Mídia linear | distribuição livre do conteúdo embutido em produto linear renderizado | 3(b) |
| Exemplo | vídeo de transmissão ou streaming, desenho animado, filme, imagem | 3(b) |

## 4. Compartilhar o conteúdo fora de um projeto

| Ponto | Fato |
|---|---|
| Em formato fonte | vetado, salvo o que os termos de serviço específicos disserem |
| Exceção | funcionários, afiliadas e prestadores que fazem o projeto para o licenciado |
| Obrigação deles | não redistribuir e apagar quando acabar o trabalho |
| Quem responde | o licenciado |

## 5. Outras restrições

| Ponto | Fato | Onde |
|---|---|---|
| "UE-Only Content" | conteúdo que a Epic designa como permitido só junto da Unreal Engine e de produtos baseados nela, como o Twinmotion | 5(a) |
| Licenças incompatíveis | proibido combinar com GPL, LGPL (salvo link dinâmico) ou Creative Commons Attribution-ShareAlike | 5(b) |
| Engenharia reversa | vetada | 5(c)(i) |
| Venda avulsa | vetada; o projeto precisa somar valor, e o conteúdo é só um componente | 5(c)(ii) |
| Terceiro criando conteúdo para o público com ele | vetado (editor de níveis, modelagem, conteúdo de usuário), salvo o 4; não vale para UE-Only Content | 5(c)(iii) |
| Lei e direitos de terceiros | não violar | 5(c)(iv)-(v) |
| Avisos e rótulos | não tirar nem alterar | 5(c)(vi) |
| Coleta para dar a outros | vetado juntar ou raspar o conteúdo para publicar, vender ou distribuir | 5(c)(vii) |
| NoAI Content | vetado em dataset, no desenvolvimento ou como entrada de Generative AI Programs | 5(c)(viii), 17 |

## 6. Quem é dono do quê

| Ponto | Fato |
|---|---|
| Projetos | do licenciado, fora o conteúdo e o que os termos específicos disserem |
| Conteúdo | da Epic ou dos licenciantes |
| Natureza | licença, não venda; nada implícito |

## 7. A relação com o Content Licensor

| Ponto | Fato | Onde |
|---|---|---|
| Licenciante padrão | a Epic, salvo outro identificado no primeiro acesso | 7(a) |
| Versão nova | aceite não obrigatório; a aceita continua valendo para o que já se tem | 7(b) |
| Sem aceitar a nova | sem certos serviços e sem baixar conteúdo novo | 7(b) |
| Ao aceitar a nova | ela passa a valer também para o que se baixou antes | 7(b) |
| Termos de serviço específicos | os adendos; prevalecem no conflito, para o conteúdo deles | 7(c) |
| Acordos substituídos | o EULA for Publishing e o EULA for Creators, no que toca ao conteúdo | 7(d) |
| O que sobra deles | só o código e o conteúdo instalados com a engine, até o aceite do EULA da Unreal | 7(d) |
| Licença sob medida | prevalece | 7(d) |
| Aviso | pelos serviços da Epic ou por e-mail | 7(e) |

## 8 a 16. Quem é quem, garantias e o resto

| Ponto | Fato | Onde |
|---|---|---|
| Menor de idade | só com responsável que também aceite | 8(b) |
| Inelegível | quem está em lista de sanções dos EUA ou em país sob embargo | 8(b) |
| Conta | conta na Epic para acessar e baixar | 8(c) |
| Instituição de ensino | pode instalar em todas as máquinas; os usuários não distribuem | 8(d) |
| Parte contratante | Epic Games, Inc. nos EUA; Epic Games Commerce GmbH fora deles | 9 |
| Garantia | nenhuma; conteúdo "como está" | 11 |
| Teto da responsabilidade | o maior entre US$ 1.000 e o pago pelo conteúdo nos 12 meses anteriores | 12 |
| Indenização | o licenciado cobre o licenciante em ação de terceiro ligada à violação ou ao projeto | 13 |
| Lei e foro | Carolina do Norte; Superior Court do condado de Wake ou tribunal federal do Distrito Leste da Carolina do Norte | 14 |
| Sair da renúncia à ação coletiva | carta à Epic em até 30 dias do primeiro aceite | 15 |
| Língua que vale | inglês | 16(d) |
| Epic quando não é a licenciante | terceira beneficiária | 16(f) |

## 17. Inteligência artificial

| Ponto | Fato |
|---|---|
| NoAI Content | o conteúdo marcado "NoAI" pela função da plataforma |
| Generative AI Programs | IA, aprendizado de máquina ou profundo, redes neurais e afins feitos para gerar ou ajudar a criar conteúdo novo (áudio, imagem, texto) |
| Vetado com NoAI Content | juntar, raspar ou usar em dataset desses programas, no desenvolvimento deles ou como entrada deles |
| Compromisso da Epic | não usar nem licenciar a terceiros, para esses programas, conteúdo que não seja dela, com ou sem a marca |

## Adendo do Marketplace

| Ponto | Fato |
|---|---|
| Objeto | código, arte e conteúdo do Unreal Engine Marketplace |
| Plugins | o código da engine dentro deles segue o EULA da Unreal, aceito ao baixar ou usar |
| Royalty | nunca antes de US$ 1.000.000 de receita bruta direta do produto; vídeo renderizado nunca paga |
| Plugin por usuário | só o número de usuários comprado |
| Plugin em fonte | pode ir a funcionários, afiliadas e prestadores, dentro desse número |
| Projeto com plugin | só se distribui como Engine Tools, pelo EULA da Unreal |

## Adendo do Megascans

| Plano | Quem se qualifica | O que se pode |
|---|---|---|
| Regra geral | — | depende do plano da conta e da qualificação no momento do acesso |
| Pessoal | pessoa física, uso só pessoal ou receita bruta anual abaixo de US$ 100.000 (adiantamentos e captação contam) | como qualquer conteúdo licenciado, sem passar o arquivo-fonte a ninguém |
| Pessoal, permanência | quem começou nele só perde o plano com mais de US$ 100.000 por dois anos seguidos | — |
| Indie | o grupo com menos de US$ 2.000.000 de receita bruta anual e sem ligação nem financiamento de estúdio de publisher | usar e compartilhar como qualquer conteúdo licenciado |
| Unreal Engine | quem tem EULA da Unreal ativo e válido | só como UE-Only Content |
| Educacional | instituição aprovada pela Epic | só uso não comercial e educacional, em laboratório, sala ou rede local ou VPN; nada comercial com ele |
| Sem plano | — | só avaliação interna; não vai a ninguém, nem dentro de projeto |

## Adendo do MetaHuman

| Ponto | Fato | Onde |
|---|---|---|
| Objeto | personagens humanos digitais baixados do MetaHuman Creator | preâmbulo |
| MetaHuman Creator | o software da Epic que cria e anima personagens (malhas e texturas de rosto, corpo e roupa, cabelo, rigs) | preâmbulo |
| O que é MetaHuman Content | os personagens feitos pelo usuário e os feitos pela Epic | preâmbulo |
| Uso | só como UE-Only Content | 1 |
| Do usuário | os direitos sobre os scans e assets que ele sobe, inclusive dentro do MetaHuman Content; o copyright da imagem renderizada do MetaHuman nos projetos | 2 |
| Da Epic | o MetaHuman Creator e o Rig Logic, inclusive dentro do MetaHuman Content | 2 |
| Rig Logic | a tecnologia de animação facial da Epic embutida no MetaHuman Content | 2 |

## Adendo de Tools

| Ponto | Fato |
|---|---|
| Ferramentas | Bridge (acesso e gestão de Megascans e MetaHumans); Mixer (texturas para Megascans) |
| Uso | só em particular, para ajudar a fazer projetos |
| Vetado | pôr parte delas no projeto; modificar; distribuir, salvo o 4 |
| Beta | marcadas como Beta; teto de responsabilidade de US$ 500 no lugar do da seção 12 |

## A página de licença do MetaHuman

| Ponto | Fato |
|---|---|
| Licença | parte da licença padrão da Unreal Engine |
| Preço | grátis abaixo de US$ 1 milhão de receita; acima, os termos padrão da Unreal |
| Outras ferramentas | uso liberado em qualquer engine ou software criativo (a citação está abaixo), com remissão ao FAQ |

**O FAQ** (as respostas, dos dados estruturados do HTML):

| Pergunta | Resposta |
|---|---|
| Quanto custa | o mesmo da abertura; as ferramentas do MetaHuman dentro da engine são Licensed Technology do EULA da Unreal |
| Licença à parte para quem já tem a da Unreal | não; desde a Unreal Engine 5.6, o MetaHuman entra na licença existente |
| Uso fora da Unreal | sim; a página diz que o EULA da Unreal prevê o uso em todas as engines e softwares criativos, "subject to applicable terms" |
| Royalty fora da Unreal | nenhum: personagens e animação contam como Non-Engine Products, tanto em mídia linear quanto em jogo de outra engine |
| Assento fora da Unreal | quem tem mais de US$ 1 milhão de receita bruta anual e renderiza fora da Unreal precisa de assento; abaixo disso, grátis |
| Mais sobre a licença da Unreal | o FAQ da Unreal |
| MetaHuman for Maya e for Houdini | download grátis pelo Fab Marketplace, sob a Standard License do Fab |
| Vender assets feitos com as ferramentas na Unreal | sim, empacotados na Unreal, no Fab e em lojas de terceiros |
| UEFN | grátis como personagem não jogável |
| IA | pode entrar em fluxo de trabalho com IA; vetado usar personagens ou curvas de animação para montar ou melhorar banco de dados ou para treinar ou testar IA e afins, com remissão ao EULA da Unreal; o veto alcança o render feito para reproduzir a função do MetaHuman |
| Licença sob medida | falar com a Epic |

## O que a fonte recomenda

Pelo acordo, o conteúdo da Epic vai livre num filme ou numa imagem renderizada, mas nunca solto em formato fonte, e o que a conta pode fazer com um asset do Megascans se decide pelo plano em que ela estava no dia do download; o personagem baixado do MetaHuman Creator, pelo adendo, só se usa como UE-Only Content. Pela página do MetaHuman, personagem e animação vão a outra engine sem royalty, o assento só se cobra de quem passa de US$ 1 milhão por ano, e nada disso pode servir de treino de IA.

## Citações

- "You may freely Distribute Licensed Content incorporated into rendered linear media products." (acordo, 3(b))
- "MetaHuman Content that you acquire may only be used and shared as UE-Only Content." (acordo, adendo do MetaHuman, 1)
- "MetaHumans can be used with any engine or creative software." (página do MetaHuman, abertura)

## Lacuna

O acordo não diz como a Epic marca o conteúdo como UE-Only nem onde o usuário vê essa marca, e não diz se o vídeo renderizado na Unreal com UE-Only Content entra sem condição na liberdade da mídia linear do 3(b). Não nomeia o Fab, embora cite o Marketplace, e não diz que plano do Megascans vale para quem baixa hoje. A página do MetaHuman não traz data no texto, não diz a que versão do EULA da Unreal se refere quando remete a ele, e as respostas do FAQ não aparecem no texto da página, só nos dados estruturados do HTML.
