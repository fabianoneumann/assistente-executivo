---
titulo: "Roblox Terms of Use"
tipo: artigo
autor: "Roblox Corporation"   # termos, diretrizes e post da própria empresa, sem assinatura de pessoa; o post do fórum é da conta "Roblox" e fecha com "Developer Relations"
url: "https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use"
publicado_em: 2026-11-01   # "Effective Date: November 1, 2026" no topo dos termos: é a data de vigência; a página não dá data de publicação
capturado_em: 2026-11-12
licenca: "protegido (termos, diretrizes e post da Roblox Corporation; sem licença de conteúdo declarada no texto lido, e os termos, 3.4, põem o texto da Roblox entre o 'Roblox-Owned Content'); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [licensing, commercial-use, roblox, terms-of-use, trademark, avatar-video, game-assets, ai-training-restriction]
---

# Roblox: o conteúdo da Roblox só dentro da plataforma, com o vídeo de avatar liberado no post de 2022

Nota de fato: uma tabela por seção lida dos termos, na ordem deles, e, para as diretrizes, o PDF do selo e o post de 2022, tabelas por tema, com prosa só para dizer o que as fontes são, o que recomendam e o que falta. Não há integral: as cinco são protegidas. Os termos são longos (cerca de 22 mil palavras) e foram lidos por seções, como pede a régua para termos de uso lidos assim.

**Proveniência.** Cinco documentos da Roblox sobre o próprio serviço e a própria marca:

| Fonte | URL | Como foi lida | Data no texto | sha256 (o que mede) | Wayback |
|---|---|---|---|---|---|
| Termos de uso (a principal) | https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use | HTML baixado por curl em 2026-11-12; lido no texto extraído do bloco principal, que traz antes a lista lateral "Articles in this section" e depois a lista dos PDFs por língua | "Effective Date: November 1, 2026" | (hash omitido) (texto do `<main>`/`<article>`, sem tags, script e estilo) | `http://web.archive.org/web/20261108074157/https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use` |
| PDF dos termos | https://en.help.roblox.com/hc/article_attachments/47741686745236 | PDF baixado por curl em 2026-11-12, texto extraído com `pdftotext`; a página dos termos o lista como "EN-US Roblox Terms of Use 20261101.pdf" | "Effective Date: November 1, 2026"; os metadados dão título "Roblox Terms of Use", gerado pelo Safari no macOS em 2026-11-10 | (hash omitido) (o arquivo) | `http://web.archive.org/web/20261011142943/https://en.help.roblox.com/hc/article_attachments/47741686745236` (cópia de 11/10, anterior à data de criação dos metadados; não aberta) |
| Diretrizes de nome e logo | https://en.help.roblox.com/hc/articles/115001708126 | HTML baixado por curl em 2026-11-12; lido no texto extraído, com a mesma lista lateral antes | nenhuma | (hash omitido) (texto do `<main>`/`<article>`) | nenhuma registrada |
| PDF das diretrizes do selo | https://en.help.roblox.com/hc/article_attachments/16896241155348 | PDF de 15 páginas baixado por curl em 2026-11-12, texto extraído com `pdftotext`; a página das diretrizes o lista como "English Roblox Badge Guidelines.pdf" | "Version 2.0"; os metadados dão o título "Roblox Badge Guidelines 2023", gerado pelo Google | (hash omitido) (o arquivo) | `http://web.archive.org/web/20260203061427/https://en.help.roblox.com/hc/article_attachments/16896241155348` |
| Post do DevForum | https://devforum.roblox.com/t/update-to-roblox-licensing-program-brand-guidelines/1843674 | JSON da API do fórum baixado por curl em 2026-11-12; lido o campo `cooked` do primeiro post, sem as tags | criado em 2022-06-23, editado pela última vez em 2022-07-06 (versão 4 do post) | (hash omitido) (o arquivo JSON inteiro) | `http://web.archive.org/web/20260703121406/https://devforum.roblox.com/t/update-to-roblox-licensing-program-brand-guidelines/1843674` |

Títulos conferidos no texto: "Roblox Terms of Use" (título e `<h1>` da página, e a primeira linha do PDF); "Roblox Name and Logo Guidelines" (título e `<h1>`); "Roblox Badge Guidelines" na capa do PDF do selo; "Update to Roblox Licensing Program & Brand Guidelines" no título do tópico, cujo primeiro post é da conta "Roblox". **O PDF dos termos é o mesmo texto da página:** na comparação palavra a palavra dos dois textos extraídos, as diferenças são a lista lateral e a lista de PDFs da página, as letras e números dos itens de lista (que só o PDF traz), o apóstrofo que o `pdftotext` engoliu ("Roblox s" na página, "Robloxs" no PDF), o "TM" junto de PlayStation e um número de página; nenhuma frase muda. **Cobertura dos termos:** o resumo das mudanças e a introdução dos termos do usuário; o parágrafo de "Your Account" que define "Content"; a seção 3 (Content: a abertura, 3.1 a 3.4.1); a seção 9 (License from Roblox: 9.1 a 9.5); a seção 10 (Roblox Intellectual Property: 10.1 a 10.3); e, nos termos do criador, a 4.1. Mais uma busca por grep, no texto todo, de "video", "film", "YouTube", "stream" e "machinima". O resto (contas, moderação, Robux, IA, pagamentos, disputas, os termos do criador além da 4.1, os anexos por país) não foi lido. **Cobertura do resto:** a página das diretrizes inteira (fora a lista lateral e os artigos relacionados), as 15 páginas do PDF do selo e o primeiro post do tópico inteiro, com o FAQ; as 451 respostas do tópico, não.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), medido contra os cinco textos juntos num arquivo só (o texto extraído da página dos termos, o do PDF dos termos, o da página das diretrizes, o do PDF do selo e o texto do primeiro post, tirado do JSON), com 86 unidades medidas (23 de prosa, 63 de célula com texto), 0 coladas e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 86 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a frase que junta lugares distantes não conta. Resultado: 50 de 86, todas células de tabela fora da proveniência: as 31 das três tabelas dos termos e 19 das 23 das tabelas por tema; nenhuma unidade de prosa segue a fonte. A maior sequência na ordem da fonte é de 31 unidades, as células das tabelas dos termos, que andam na ordem das seções porque a régua manda uma tabela por seção lida, na ordem delas; é texto normativo (o que se permite e o que se veta), não argumentação, e fica declarado aqui. Nas tabelas por tema, a maior sequência na ordem de um mesmo documento é de 2.

## Em uma frase

Textos da Roblox sobre a própria marca: os termos de 01/11/2026 vetam usar fora da plataforma o que a Roblox criou ou possui (avatares clássicos, marca, texto, imagens), inclusive em filme ou obra derivada, salvo autorização expressa e dentro das diretrizes de nome e logo; as diretrizes negam o avatar clássico em conteúdo comercial sem licença; e o post oficial de 2022, no FAQ, diz que vídeo e animação com qualquer avatar seguem permitidos e monetizáveis.

## Termos: o resumo e a introdução

| Ponto | Fato |
|---|---|
| Vigência | 1º de novembro de 2026 |
| O que mudou, pelo resumo | linguagem simplificada; seções reorganizadas; a Roblox como distribuidora principal e "merchant of record" das compras; direito de arrependimento para o usuário do EEA |
| Compra de conteúdo | o usuário obtém o conteúdo da Roblox, não do criador |
| Documentos que entram nos "Roblox Terms" | termos do criador, termos do DevEx, Community Standards, política de privacidade, anexos, diretrizes de nome e logo, termos do DSA da UE |
| Termos por país | prevalecem só no que a lei local exigir e só para quem está lá |
| EUA e Canadá (fora Quebec) | arbitragem individual obrigatória, com renúncia a ação coletiva |
| "Content", na seção das contas | jogos, itens, assets, UGC, imagens, vídeos, áudio, texto, conteúdo gerado por IA, venha de usuário, criador ou da Roblox |

## Termos, seção 3: Content

| Item | Ponto | Fato |
|---|---|---|
| Abertura | Propriedade | interagir com conteúdo alheio ou pagar por serviço não dá propriedade sobre ele |
| Abertura | Direitos não concedidos | ficam com a Roblox |
| Abertura | Garantia | nenhuma; conteúdo "as is" |
| Abertura | Disponibilidade | varia por país; a Roblox pode bloquear conteúdo por região, por ordem legal |
| 3.1 | UGC | tudo o que o usuário cria, sobe ou publica, inclusive prompts e saídas das funções de IA |
| 3.1 | Propriedade intelectual de terceiros no UGC | só com permissão do titular ou direito legal |
| 3.1 | Dono do UGC | o usuário, sujeito à licença não exclusiva à Roblox |
| 3.2 | Licença à Roblox | mundial, não exclusiva, sem royalties (com as ressalvas de 4.2 e 6 dos termos do criador), perpétua, irrevogável, sublicenciável, transferível |
| 3.2 | O que a licença cobre | usar, copiar, distribuir, modificar, derivar, exibir, publicar e explorar o UGC para qualquer fim comercial lícito |
| 3.2 | Fins citados | promover os serviços; disponibilizar e monetizar o UGC; desenvolver, melhorar ou treinar modelos de IA e aprendizado de máquina |
| 3.2 | Pagamento pela licença | nenhum, fora o que a seção 6 dos termos do criador prevê |
| 3.2 | UGC apagado | quem já o acessou e a própria Roblox podem continuar usando |
| 3.3 | UGC de outros | para uso dentro dos serviços, pelos recursos deles, não fora deles |
| 3.3 | Aquisição de UGC | só para entretenimento pessoal |
| 3.4 | "Roblox-Owned Content" | texto, imagens, ilustrações, interfaces, gráficos, fotos, clipes de vídeo, ícones, design, fontes, código, marcas, modelos de avatar, roupas, jogos publicados pela Roblox |
| 3.4 | Para que é dado | uso com os serviços, só nos termos |
| 3.4 | Avatar clássico modificado | todos os direitos cedidos à Roblox, de forma irrevogável, inclusive os feitos sob versões anteriores dos termos |
| 3.4 | De volta ao usuário | licença limitada, revogável e intransferível para usar o avatar modificado só nos serviços |
| 3.4 | Fora da cessão | o UGC posto no avatar que não derive do avatar clássico |
| 3.4.1 | Uso fora dos serviços | só com as duas condições: autorização expressa da Roblox e conformidade com as diretrizes de nome e logo |
| 3.4.1 | Uso sem autorização | "strictly prohibited" |

## Termos, seção 9: License from Roblox

| Item | Ponto | Fato |
|---|---|---|
| 9.1 | Licença ao usuário | limitada, não exclusiva, revogável, não sublicenciável, intransferível |
| 9.1 | Para quê | acessar e usar conteúdo e serviços em conexão com a plataforma |
| 9.1 | Quem licencia todo conteúdo | a Roblox, como principal, não o criador |
| 9.1 | Avisos de direito autoral | não se removem |
| 9.2 | Reproduzir, baixar, distribuir, exibir, vender, licenciar ou modificar parte do serviço ou conteúdo | vetado, salvo autorização do próprio serviço ou permissão prévia por escrito da Roblox e, se for o caso, dos titulares |
| 9.2 | Engenharia reversa; burlar o serviço | vetados |
| 9.2 | Robôs, crawlers, scrapers para treinar ou usar IA | vetado |
| 9.2 | Colher conteúdo ou dado | vetado para qualquer fim, IA inclusive |
| 9.2 | Vender anúncio, patrocínio ou promoção no serviço, em volta dele ou no conteúdo | vetado fora dos termos de publicidade da Roblox |
| 9.2 | "Roblox-Owned Content" fora dos serviços | vetado, inclusive ligado a produto, filme, publicação ou outra obra derivada fora deles |
| 9.2 | Alcance dos vetos | também tentar, permitir ou habilitar outros |
| 9.3 | Uso comercial de conteúdo, inclusive treino de IA | a Roblox reserva todos os direitos, por ela e pelos usuários, onde a lei permitir esse uso |
| 9.4 | Serviços de terceiros embutidos | termos próprios; a Roblox não responde por eles |
| 9.5 | Software de código aberto | segue a licença dele |

## Termos, seção 10: Roblox Intellectual Property

| Item | Ponto | Fato |
|---|---|---|
| 10.1 | "Roblox", "Blox" e nomes parecidos | vetados em título de jogo, nome de usuário, nome de exibição e nome de grupo ou comunidade |
| 10.1.1 | Licença de marca | pessoal, limitada, revogável, só dentro do UGC nos serviços |
| 10.1.1 | Marca fora dos serviços | só como dizem as diretrizes de nome e logo |
| 10.1.1 | O "goodwill" do uso | todo da Roblox |
| 10.1.2 | Jogo publicado antes de 22/06/2022 com o nome | mantém o título e os nomes de usuário ou grupo ligados a ele |
| 10.2 | Pedido válido de retirada do titular | o UGC sai; reincidente pode perder a conta |
| 10.3 | Sugestão sobre o serviço | licença perpétua e gratuita à Roblox, para qualquer fim |
| Termos do criador, 4.1 | Licenças do criador | as da seção 3.2 e da 9 dos termos do usuário |
| Texto todo (grep) | Vídeo de jogo, YouTube, transmissão, machinima | nenhuma menção; "film" só no veto da 9.2 |

## Diretrizes, PDF do selo e post de 2022, por tema

Os três documentos são curtos e vão juntos, por pergunta, fora da ordem deles, como pede a régua da nota de fato para fonte curta. Na coluna "Onde": D é a página das diretrizes de nome e logo, S o PDF do selo, P o post do DevForum (A para o anúncio, F para o FAQ dele).

| Vídeo e transmissão | Fato | Onde |
|---|---|---|
| Vídeo, animação ou transmissão com avatar R6 ou R15 | fora do alcance das diretrizes, pelo FAQ | P, F |
| Ganhar dinheiro com esse vídeo | permitido; exemplo dado: anúncio no YouTube | P, F |
| Filme ou série de TV com avatar clássico | pede contato com a Roblox | P, F |
| Filme e TV ligados à marca ou ao avatar clássico | na lista do que exige acordo de licenciamento | D |
| Avatares em miniatura, trailer, rede social e anúncio | todos os tipos liberados, dentro das diretrizes | P, F |
| Canal ou site de fã com "Roblox" ou "Blox" no nome | declarar que não tem ligação com a Roblox | P, F |
| Programa de criadores de vídeo (Roblox Video Stars) | segue | P, F |
| Regra própria para vídeo no PDF do selo | nenhuma | S |

| Avatar clássico e uso comercial | Fato | Onde |
|---|---|---|
| O que é | os modelos R6 (6 partes) e R15 (15 partes) e o que a Roblox julgar derivado deles | D |
| Corpos de base listados | Roblox Boy, Roblox Girl (opções 1 e 2), Roblox Man, Roblox Woman | D |
| De quem é | da Roblox, toda a propriedade intelectual; uso só na plataforma | D |
| Uso em produto físico ou "commercial content" | só com acordo de licenciamento, como o nome, o selo, o logo e as demais marcas | D; P, A |
| Usos citados que pedem o acordo | produto, embalagem, vitrine, serviço, NFT, filme, TV, livro, espetáculo, parque | D |
| Pedido de uso comercial que a Roblox não buscou | negado de saída | D |
| R15 personalizado a ponto de não lembrar o clássico | usável; o grau fica a critério da Roblox | P, A |
| Rthro, criaturas, bichos, prédios, veículos e cenários | liberados em produto comercial próprio, com o nome da experiência | P, A |
| Avatar na peça de promoção | opcional | S |
| Quando usar avatar na promoção | dois ou mais humanos; estilos, gêneros, corpos e tons de pele variados; tamanhos proporcionais | S |
| Sugestões de avatar | cinco corpos de base (Jordan, Robin, Harper, Andi, Billie) e uma lista de avatares de ficção científica, clássicos ou não | S |
| Mercadoria do criador | permitida, sem logo, sem o selo e sem R6 ou R15 | S |
| Aprovação para usar o corpo clássico no comercial | por escrito, pedida no formulário da página das diretrizes | S |
| Programa de licenciamento de produtos (Developer Stars) | fim anunciado em 2022 | P, A |

| Nome e logo | Fato | Onde |
|---|---|---|
| "Roblox", "Blox" e parecidos no título de jogo | vetados para jogo de 22/06/2022 em diante; a Roblox decide o que é parecido | D; P, A |
| Jogo antigo com o nome | fica com o título e pode lançar continuação com ele, não título novo | P, F |
| Os mesmos em nome de criador, de exibição ou de grupo | vetados, fora os ligados a jogo anterior à data | D |
| Logo e "Roblox Tilt" | fora do uso geral; reservados a parceiros escolhidos e ao programa Roblox Stars Influencer | D |
| Insinuar parceria ou endosso | vetado | D |
| Comunicado de imprensa que cita a Roblox | pede aprovação, por formulário | D |
| Palavra "Roblox" no texto | mesma fonte e estilo do texto em volta, sem destaque, sem trocar pelo logo | S |
| Preposição | "on Roblox"; nunca "from", "at" ou "in" | S |
| Livro sobre programar na Roblox | nome no título, mas não na frente; capa com UNOFFICIAL; sem logo | D |
| Exceção de educação e pesquisa | publicação aprovada, para escola, faculdade, universidade ou biblioteca sem fins lucrativos | D |

| Selo "Now on Roblox" | Fato | Onde |
|---|---|---|
| Função | anunciar fora da plataforma que a experiência ou o item está na Roblox; toma o lugar do logo | D; S; P, A |
| Promoção digital (redes sociais inclusive) | sem aprovação, seguindo as regras | D; P, A |
| Outdoor, placa, TV, impresso | aprovação prévia, por formulário | D |
| Obrigatório? | não | P, F |
| Versões | a preta, com a borda cinza que faz parte dela, é a preferida; a branca, só quando a preta pesar | S |
| Tamanho | x-height de no máximo 10% da peça | S |
| Lugar | no quarto de baixo, num canto ou no centro; subordinado à arte principal, com distância do logo da experiência | S |
| Vetado | separar, editar, recriar, girar, pôr sombra, juntar ao nome da experiência | S |
| Arquivos na página | vetor do selo (`RBLX_Badge_Logos.ai`, 300 KB) e o PDF do selo (3 MB) | D |
| Tópico do fórum | 452 posts; fechado | P |

## O que a fonte recomenda

Para promover uma experiência fora da plataforma, a Roblox quer o selo "On Roblox" no lugar do logo, pequeno e no rodapé da peça, com o nome escrito sempre como "on Roblox". O que ela criou ou possui, avatar clássico inclusive, fica dentro da plataforma, e qualquer uso comercial dele, de produto físico a filme, passa por licença ou aprovação por escrito; o vídeo e a transmissão com avatares, monetizados, ficam de fora dessa exigência no FAQ de 2022, e a série ou o filme com avatar clássico pede contato antes.

## Citações

- "use Roblox-Owned Content outside the Services or in connection with any off-Services merchandise, film, publication, or other derivative work." (termos, 9.2)
- "Please note that we do not grant unsolicited requests for commercial use." (diretrizes de nome e logo)
- "you may continue monetizing that content (such as through YouTube ad revenue)" (post do DevForum, FAQ)

## Lacuna

Os termos de 2026 não falam de vídeo de jogo, transmissão, YouTube nem machinima, e não dizem se o FAQ do post de 2022, que libera o vídeo monetizado com avatares, segue valendo diante do veto da 9.2 a filme e obra derivada fora dos serviços; o post não está entre os documentos que os termos incorporam pelo nome. Nenhuma das fontes define "commercial content" nem diz se o vídeo de uma marca ou de quem vende curso ou serviço entra nele, nem trata de vídeo com avatar não clássico ou com jogo de terceiro feito na plataforma. As diretrizes não têm data visível, e o PDF do selo não diz quando a versão 2.0 entrou em vigor.
