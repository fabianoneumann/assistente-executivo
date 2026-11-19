---
titulo: "Unity Terms of Service Update FAQ"
tipo: artigo
autor: "Unity Technologies"   # páginas institucionais da empresa, sem assinatura de pessoa
url: "https://unity.com/legal/editor-terms-of-service/software/faq"
publicado_em: 2025-08-13   # a FAQ diz "Last Updated: August 13, 2025"; o artigo de suporte, a segunda página, diz "December 10, 2024 15:06" com "Updated" ao lado
capturado_em: 2026-11-13
licenca: "protegido (rodapé das duas páginas: '© 2026 Unity Technologies'; sem licença de conteúdo declarada no texto lido); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unity, terms-of-service, licensing, industry-customer, revenue-threshold, education, commercial-use, interested-party]
---

# Unity: quem é "Industry Customer", pela FAQ dos termos e pelo artigo de suporte

Nota de fato: tabelas do que duas páginas da Unity dizem sobre o cliente de indústria, uma seção por página, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: as páginas são protegidas. As duas são curtas e listam o que uma cláusula abrange, então as tabelas seguem a ordem de cada página (o `README.md` desta pasta, item 2, a exceção da página técnica), e a medida da cópia é a do `parafrase.py` e a da conta lado a lado.

**Proveniência.** Duas páginas da Unity, baixadas com `curl` em 13/11/2026. O sha256 de cada uma é o do texto do bloco extraído (o `protegidas.json` da rodada é a referência), não o do arquivo HTML.

| Página | URL | Data no texto | sha256 (texto do bloco) | Wayback |
|---|---|---|---|---|
| U1, FAQ dos termos (a principal) | https://unity.com/legal/editor-terms-of-service/software/faq | "Last Updated: August 13, 2025" | (hash omitido) (`<main>`) | http://web.archive.org/web/20261023073811/https://unity.com/legal/editor-terms-of-service/software/faq |
| U2, artigo de suporte | https://support.unity.com/hc/en-us/articles/32263121729172-What-is-an-Industry-Customer | "December 10, 2024 15:06", com "Updated" | (hash omitido) (`<article>`) | http://web.archive.org/web/20261021204754/https://support.unity.com/hc/en-us/articles/32263121729172-What-is-an-Industry-Customer |

Títulos conferidos no `<title>`: "Unity Terms of Service Update FAQ" e "What is an "Industry Customer"? – Unity Support Help Center". Cobertura: U1 inteira (800 palavras), com as respostas conferidas também no JSON-LD `FAQPage` da página, que traz o mesmo texto; U2 inteira (276 palavras do artigo), sem os artigos ligados. Os termos do Editor e os termos de indústria, que U1 liga, não foram abertos nesta rodada.

**Conferência lado a lado** (2026-11-13, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra os textos das páginas juntos num arquivo só (`2026-11-13-unity-faq-dos-termos-e-industry-customer.fonte.txt`, na cópia de trabalho), com 34 unidades medidas (17 de prosa, 17 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas. Na leitura lado a lado, segue a fonte a unidade que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela, e conta como unidade que segue a fonte a célula que o script partiu em pedaços da mesma frase: 18 de 24 unidades do corpo (de "Em uma frase" em diante), 18 de 34 com as 10 do cabeçalho de proveniência, que não tratam do conteúdo. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 15, a tabela de U1 inteira: a página é técnica e lista fatos, e a ficha segue a ordem dela pela exceção do item 2; a justificativa da separação entre os clientes está numa célula só.

## Em uma frase

A FAQ dos termos da Unity define o cliente de indústria como quem usa a Unity em projeto que não é só jogo ou entretenimento, dá os setores de exemplo (entre eles "education technology") e diz que plano esse cliente pode usar por faixa de receita; o artigo de suporte repete a primeira parte da definição, com uma lista menor de setores.

## U1. A FAQ dos termos (13/08/2025)

**O que mudou nesta versão, pela própria página:** as respostas passaram a trazer setores de indústria como exemplos na definição de cliente de indústria, e o Pixyz passou a se chamar Unity Asset Transformer.

| Pergunta | O que a página responde |
|---|---|
| Quem é cliente de indústria | pessoa física ou jurídica que licencia a Unity para projeto de uso industrial (não jogo, não entretenimento), ou para qualquer uso que não seja só jogo ou entretenimento |
| Quem fica fora | quem usa as versões educacionais |
| Setores de exemplo, numa lista que não se esgota | automotivo, aeroespacial, manufatura, governo, arquitetura, engenharia, construção, energia, saúde, "education technology" e varejo |
| O que a página diz que é "education technology" | empresas que usam aplicativos ou aparelhos de tecnologia para ensinar e aprender |
| Por que separar | o Unity Industry é um pacote novo, feito para esse cliente, com termos próprios; esses termos não valem para o cliente de entretenimento |
| Limites dos outros clientes | os limites financeiros dos planos para todos os outros clientes não mudaram |
| O que é o plano Unity Industry | um conjunto com Unity Enterprise, Industry Success, Unity Asset Transformer Toolkit e outros itens; sucede o Unity Industrial Collection, que sai de linha "this year" |
| Quando o cliente de indústria pode usar o Pro ou o Enterprise | com finanças totais abaixo de US$ 1 milhão por ano: Pro, Enterprise ou Industry |
| Acima de US$ 1 milhão por ano | o Unity Industry, obrigatório pelos termos |
| Quem presta serviço a terceiro | conta a receita bruta ou a captação do cliente dele para o limite de US$ 1 milhão (seção 1.1 dos termos) |
| Quem usa para indústria e para jogo ou entretenimento | não pode usar ao mesmo tempo planos com limites financeiros diferentes; o cliente de indústria mantém licenças Unity Industry nos projetos e fala com o vendedor da Unity sobre o caso |
| Assinaturas ativas | os termos de indústria valem só para renovação e licença nova; houve seis meses de transição, de 03/04/2023 a 03/10/2023 |
| Como passar do Pro ao Industry | pelo Unity ID, se o Pro foi comprado online; pela equipe de vendas, se foi por parceiro |
| Clientes de jogo e entretenimento | os planos e os limites financeiros deles não mudam com esta atualização |
| Unity Gaming Services | os termos adicionais passaram a usar os mesmos Termos de Serviço do Editor; os de consultoria se juntaram nos Consulting Services Additional Terms |
| Success Plans | os termos adicionais foram atualizados e renomeados para Success Services Additional Terms |

## U2. O artigo de suporte "What is an Industry Customer?"

| Item | O que a página diz |
|---|---|
| A dúvida que o artigo responde | quem vai comprar uma licença e não sabe se é cliente de indústria; quem usa a Unity fora de jogo, em manufatura |
| Definição | pessoa física ou jurídica que licencia a Unity para projeto de uso industrial (não jogo, não entretenimento) |
| Setores, numa lista que não se esgota | automotivo, aeroespacial, manufatura, governo, arquitetura, engenharia, construção, energia e varejo |
| Prestador de serviço, plataforma, agência, revendedor e afins | pode precisar de outra concessão de direitos ou de autorização por escrito da Unity |
| Dúvida sobre a elegibilidade | falar com a equipe de vendas da Unity |
| Leituras ligadas | "How can I contact Unity?", "Which Unity Editor license should I use/purchase?" e a FAQ dos termos (U1) |

## O que a fonte recomenda

O artigo manda quem tem dúvida sobre a elegibilidade falar com a equipe de vendas da Unity; a FAQ manda falar com o vendedor só quem usa a Unity para indústria e para jogo ou entretenimento. A FAQ põe o corte em "só jogo ou entretenimento" e, para o cliente de indústria, o corte de US$ 1 milhão por ano entre o Pro ou o Enterprise e o Industry; o artigo acrescenta que quem presta serviço ou revende pode precisar de autorização por escrito.

## Citações

- "or for any use that is not solely for games or entertainment purposes."
- "education technology (companies utilizing applications or technology devices for the purposes of teaching and learning)"
- "Customers may not use Unity Software tiers with different financial thresholds at the same time."

## Lacuna

Nenhuma das duas páginas diz se o cliente de indústria pode usar a Unity Personal, nem quem decide o enquadramento; nenhuma trata do criador de conteúdo, do vídeo, do curso ou do ensino feito por uma pessoa. A definição do artigo (U2) não traz a frase "for any use that is not solely for games or entertainment purposes", e a lista dele não traz saúde nem "education technology". A FAQ não diz de que ano é o "this year" da saída do Unity Industrial Collection.
