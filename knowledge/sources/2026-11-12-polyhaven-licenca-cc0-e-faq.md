---
titulo: "License • Poly Haven"
tipo: artigo
autor: "Poly Haven"   # página do próprio site, sem assinatura; o FAQ do wiki tem nos metadados o autor "Greg" e fala na primeira pessoa num trecho ("my article")
url: "https://polyhaven.com/license"
publicado_em: null   # a página de licença não traz data; o FAQ, nos metadados do wiki, foi criado em 2023-07-07 e atualizado em 2026-02-13
capturado_em: 2026-11-12
licenca: "assets CC0; o texto da página de licença é protegido pelos termos de uso que ela mesma traz (4.1 e 4.2: todo o conteúdo do site fora os assets CC0, 'Text and copy' inclusive). O FAQ vem do wiki em docs.polyhaven.com, cuja configuração diz 'All publically accessible content on docs.polyhaven.com is made available under the CC-BY license' (sem versão); tratado como protegido nesta ficha até conferir. Nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [licensing, commercial-use, cc0, 3d-assets, hdri, pbr, attribution, poly-haven]
---

# Poly Haven: assets CC0 para qualquer uso, com o site e a API sob termos próprios

Nota de fato: tabelas do que a página de licença (com os termos de uso do site, na mesma página) e o FAQ do Poly Haven dizem, com prosa só para dizer o que as fontes são, o que recomendam e o que falta. Não há integral nesta ficha (a licença do FAQ está na proveniência).

**Proveniência.** Duas páginas do Poly Haven sobre o próprio acervo:

| Fonte | URL | Como foi lida | Data no texto | sha256 (o que mede) | Wayback |
|---|---|---|---|---|---|
| Licença e termos de uso (a principal) | https://polyhaven.com/license | HTML baixado por curl em 2026-11-12; lido no texto extraído do bloco principal | nenhuma | (hash omitido) (texto do `<main>`/`<article>`, sem tags, script e estilo) | `http://web.archive.org/web/20261109164019/https://polyhaven.com/license` |
| FAQ | https://polyhaven.com/faq | HTML baixado por curl em 2026-11-12; o HTML é a página do wiki, com `og:url` em `https://docs.polyhaven.com/en/faq`; lido no texto extraído do bloco principal | nenhuma no texto; nos metadados do wiki, criada em 2023-07-07 e atualizada em 2026-02-13, autor "Greg" | (hash omitido) (texto do `<main>`/`<article>`) | `http://web.archive.org/web/20230714170625/https://polyhaven.com/faq` (cópia de 2023, anterior à última atualização; não aberta) |

Títulos conferidos: "License • Poly Haven" (título e `canonical` da página), que abre com "Asset License" e tem a seção "Terms of Service" mais abaixo; "FAQ | Poly Haven Wiki". **Licença do texto:** os termos de uso da página de licença protegem todo o conteúdo de polyhaven.com fora os assets CC0, e citam o texto entre os exemplos (4.1 e 4.2). O FAQ não está em polyhaven.com, mas no wiki em docs.polyhaven.com, e a configuração do wiki, no HTML, traz `"contentLicense":"ccby"` e o texto de rodapé que põe todo o conteúdo público do wiki sob "the CC-BY license", sem dizer a versão; a ficha não traz o integral dele. Cobertura: as duas páginas inteiras (a licença, o "Why CC0?" e os onze itens dos termos; as treze perguntas do FAQ, aqui F1 a F13, na ordem da página). Ficaram fora o menu e o rodapé, os termos da API, a política de privacidade e os relatórios financeiros a que as páginas remetem, que não foram abertos.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), medido contra os dois textos juntos num arquivo só (o texto extraído da página de licença e o do FAQ), com 48 unidades medidas (22 de prosa, 26 de célula com texto), 0 coladas e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 48 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a frase que junta lugares distantes não conta. Resultado: 22 de 48, as 22 células de tabela fora da proveniência (quatro de "Os assets", quatro dos termos e catorze do FAQ técnico); nenhuma unidade de prosa segue a fonte. As tabelas dos termos e do FAQ vão fora da ordem da página, e a maior sequência de unidades seguidas na ordem da fonte é de 2.

## Em uma frase

Texto do Poly Haven sobre o próprio acervo: todos os HDRIs, texturas e modelos 3D são CC0, usáveis para qualquer fim, inclusive comercial, sem crédito obrigatório e até dentro de produto vendido, enquanto o resto do site (logos, renders de exemplo, texto) é protegido, a raspagem do site é vetada sem permissão e a API pública tem termos à parte.

## Os assets

| Ponto | Fato | Onde |
|---|---|---|
| O que o acervo tem | HDRIs, texturas, modelos 3D | Licença |
| Quem fez | a equipe do Poly Haven ou artistas que doaram ou venderam a obra a ele | Licença |
| Licença | CC0, em todos | Licença; F1 |
| Uso | qualquer fim, inclusive comercial | Licença; F1 |
| Crédito | não exigido; apreciado | Licença |
| Redistribuir | permitido, inclusive dentro de produto vendido | Licença; F2 |
| O que não se pode | dizer-se o autor original; relicenciar | F2 |
| Treinar IA | permitido | F3 |
| Pedido a quem vende produto com os assets | dizer ao cliente que são grátis e de domínio público; se der, pôr um link para o Poly Haven | F2 |
| Pedido a quem lucra ou usa muito | doação mensal no Patreon | Licença; F2 |
| Revenda por terceiros | acontece, e a página a chama de antiética | Licença |
| Quem usa, segundo a página | artistas 3D, cientistas de dados, desenvolvedores, engenheiros automotivos, pesquisadores de IA | Licença |
| IA generativa na produção | não usada em nenhum asset | F3; F13 |
| Texturas | na maioria por fotogrametria, parte por estéreo fotométrico; nenhuma procedural | F13 |
| Modelos | fotogrametria em alguns (pedras, natureza), com retopologia e mapas feitos depois | F13 |
| Financiamento | doações; relatórios financeiros públicos | F5 |

## Os termos de uso do site (na página de licença)

Os itens vão por tema, não na ordem numerada da página.

| Tema | Fato | Item |
|---|---|---|
| O que fica protegido | tudo em polyhaven.com que não seja asset CC0 | 4.1 |
| Exemplos do protegido | logos; renders de exemplo dos assets; renders e avatares de usuários; texto | 4.2 |
| Usar o protegido | pede permissão prévia por escrito do site ou do titular | 4.1 |
| Aceite e mudanças | usar o site aceita os termos, que mudam a qualquer hora | 1; 2 |
| Por que há termos | o mau uso do site, já que os assets são CC0 e o código é aberto | abertura |
| Raspar ou minerar dados do site | só com permissão expressa | 3.2 |
| Outros vetos | ataque DDoS; invasão de contas ou recursos; código malicioso; assédio | 3.2 |
| Fins do uso | lícitos | 3.1 |
| API pública (api.polyhaven.com) | regida por termos próprios, somados a estes | 5 |
| Lei e foro | África do Sul | 10 |
| Suspensão de acesso | sem aviso, por violação ou outro motivo | 7 |
| Garantia | nenhuma; o site vem "as is" | 8 |
| Responsabilidade por danos | nenhuma, até onde a lei permite | 9 |
| Privacidade | política à parte | 6 |

## O FAQ técnico

As respostas vão misturadas, fora da ordem da página.

| Tema | Fato | Onde |
|---|---|---|
| Mandar um asset | aceito como doação, se atingir o padrão de qualidade | F12 |
| Download que não funciona | extensão de gerenciador de download (erro 404) ou, no Firefox, a opção de apagar cookies ao fechar | F11 |
| Download: por que falha | o zip se monta no navegador por um service worker, que essa opção impede | F11 |
| Encomenda | o site em geral não faz; os artistas talvez; com desconto se o asset puder ser publicado lá | F4 |
| HDRI do site | sem corte; dispensa mexer em gama ou intensidade | F7 |
| HDRI, no sentido geral | qualquer imagem com mais de 8 bits por canal (EXR, HDR); JPG e PNG são de 8 | F6 |
| Textura: o mapa chamado "diffuse" | é um albedo, feito para render físico (PBR), com o mínimo de sombra possível | F10 |
| HDRI: equipamento | varia, com vários fotógrafos; a resposta remete a um artigo sobre fazer HDRI | F9 |
| HDRI: o que olhar ao escolher | se está sem corte; com corte, a luz sai chapada e sem contraste | F8 |
| HDRI: para que serve | luz única para cena realista; casar com a luz de vídeo filmado no mesmo set; reforço de luz; reflexos | F6 |
| Textura para motor antigo ou não fotorrealista | multiplicar a oclusão sobre o albedo num editor de imagem dá o diffuse clássico | F10 |
| HDRI: número de EVs | sem padrão de medida entre sites; o do Poly Haven conta exposições (5 fotos a 3 EVs uma da outra, 12 EVs) | F8 |
| HDRI, no sentido do site | panorama equirretangular de 32 bits, 360×180 graus, para iluminar cena 3D | F6 |
| Textura: de onde vem a sombra | do motor, com deslocamento de geometria e sombreamento por path tracing, ou de um mapa de oclusão à parte | F10 |
| HDRI: tutoriais | vídeos para Blender com Cycles e 3ds Max com Corona | F7 |

## O que a fonte recomenda

O Poly Haven escolheu o CC0 sabendo que alguém vai revender o acervo, e pede em troca só o que a licença não obriga: avisar o cliente de que o asset é grátis, linkar o site e doar quando o uso der dinheiro. Para o uso técnico, o que pesa no HDRI é estar sem corte, mais do que o número de EVs, e o mapa de cor das texturas vem sem sombra porque a sombra é tarefa do motor de render. O site, a API e o texto ficam fora do CC0, e a página veta raspar o site sem permissão.

## Citações

- "You do not need to give credit or attribution when using them (although it is appreciated)." (Licença)
- "The only thing you can't do is claim to be the original author or re-license them." (FAQ, F2)
- "Web scraping or data mining without express permission." (termos de uso, 3.2)

## Lacuna

As páginas não dizem o que os termos da API exigem (crédito, limite de chamadas, uso automatizado) nem se baixar muitos assets um a um pelo site conta como raspagem; não dão data de vigência dos termos. A licença não diz se os renders de exemplo e as miniaturas que acompanham cada asset podem ir junto num vídeo. O wiki não diz a versão da licença CC-BY que declara, e as duas páginas não tratam do caso de um asset doado que traga marca, rosto ou obra de terceiro.
