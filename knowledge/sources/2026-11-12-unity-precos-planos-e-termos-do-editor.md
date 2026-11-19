---
titulo: "Changes to Unity subscription plans and pricing"
tipo: artigo
autor: "Unity Technologies"   # páginas institucionais e termos da empresa, sem assinatura de pessoa
url: "https://unity.com/products/pricing-updates"
publicado_em: 2025-11-10   # a página principal diz "Announced November 10, 2025" sobre as mudanças de 2026; o FAQ dela traz trechos de 2024; os termos do editor dizem "Last updated: June 30, 2026"; a página de planos não tem data
capturado_em: 2026-11-12
licenca: "protegido (rodapé das três páginas: '© 2026 Unity Technologies'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unity, pricing, subscription, revenue-threshold, terms-of-service, licensing, commercial-use, interested-party]
---

# Unity: os preços de 2026, os planos e os limites financeiros dos termos do editor

Nota de fato: tabelas do que três páginas da Unity dizem sobre os planos, os preços e quem pode usar cada um, uma seção por página, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: as páginas são protegidas. As tabelas seguem as partes de cada página, mas as linhas dentro de cada tabela estão fora da ordem do texto, para a ficha não andar junto com ele; o rótulo de cada linha diz o tema.

**Proveniência.** Três páginas da Unity, sobre os próprios planos, todas baixadas com `curl` em 2026-11-12. O sha256 de cada uma é o do texto do bloco `<main>`/`<article>` extraído pelo `baixa.py`, sem tags, script e estilo; não é o hash do HTML inteiro.

| Página | URL | Data no texto | sha256 (texto do `<main>`) | Wayback |
|---|---|---|---|---|
| U1, mudanças de preço (a principal) | https://unity.com/products/pricing-updates | "Announced November 10, 2025" | (hash omitido) | http://web.archive.org/web/20261106060210/https://unity.com/products/pricing-updates |
| U2, planos e preços | https://unity.com/products | nenhuma | (hash omitido) | http://web.archive.org/web/20261112031425/https://unity.com/products |
| U3, termos do editor | https://unity.com/legal/editor-terms-of-service/software | "Last updated: June 30, 2026" | (hash omitido) | http://web.archive.org/web/20261101104603/https://unity.com/legal/editor-terms-of-service/software |

Títulos conferidos: U1 abre com "Changes to Unity subscription plans and pricing" (o `<title>` diz "Unity Pricing Changes | Unity"); U2 abre com "Plans & Pricing" (`<title>`: "Unity Plans & Pricing: Pro, Personal, Enterprise, Industry | Unity"); U3 abre com "Unity Editor Software Terms", que é também o `<title>`. Cobertura de fato:

- **U1:** o texto extraído inteiro: as mudanças de 2026, os três planos com o preço de 2026 e o FAQ (DevOps, Havok, planos, termos do editor e Runtime Fee).
- **U2:** o texto extraído inteiro, que é a aba Games (a que a página abre): os três cartões, a tabela de comparação (que sai duas vezes no texto, igual) e o FAQ. A extração perde as marcas de "incluído" da tabela, então as linhas só de marca ficam fora; nas linhas de valor, quando há quatro valores, eles seguem a ordem das colunas (Personal, Pro, Enterprise, Industry). O cartão da aba Industry e os do Unity AI e do Unity Studio não estão no texto extraído: foram lidos no JSON que a página embute no HTML, e não se conferiu como aparecem na página aberta.
- **U3:** por trechos, como registra o rótulo: o cabeçalho com a data e o "What's changed", a seção 1 inteira (elegibilidade e limites financeiros), a abertura da seção 2 e as subseções 2.1, 2.1.1, 2.2 e 2.2.1, e, na seção 4, as definições de "Industry Customer", "Legal Entity", "Unity Industry", "Unity Personal", "Unity Pro", "Unity Enterprise" e "Unity Student Plan". A 2.11 foi aberta, mas não entra (não trata dos limites nem do cliente de indústria); as subseções 2.3 a 2.10 e 2.12, a seção 3 e as outras definições não foram lidas.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra o texto das três páginas juntas num arquivo só (os três blocos extraídos; os cartões lidos no JSON de U2 não estão nele), com 87 unidades medidas (26 de prosa, 61 de célula com texto), 2 coladas e 0 trechos de 3 ou mais seguidas; as duas coladas são o título da tabela do DevOps, feito de nomes de produto, que não segue frase da fonte, e a célula dos minutos grátis, que cola pelos nomes das faixas (Micro, Standard) e entra na conta lado a lado entre as que seguem a fonte. Na leitura lado a lado das mesmas 87 unidades, segue a fonte a frase ou célula que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a célula só de valores e nomes e a frase que junta lugares distantes em outra ordem não contam. Resultado: 60 de 87, todas células das tabelas (a prosa da proveniência, de "Em uma frase", da recomendação e da lacuna não segue a fonte). A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 2, e nenhuma delas está em texto argumentativo.

## Em uma frase

Páginas da Unity, que vende as assinaturas que descreve: o Personal é grátis até US$ 200 mil de receita e captação em 12 meses, o Pro custa US$ 2.310 por ano por assento em 2026 (5% a mais desde 12 de janeiro), o Enterprise é obrigatório a partir de US$ 25 milhões, e quem faz aplicação fora de jogos e entretenimento com mais de US$ 1 milhão vai para o Unity Industry.

## U1. Mudanças de preço

**Os planos em 2026**

| Ponto | Enterprise | Pro | Personal |
|---|---|---|---|
| Preço | sob consulta; pode haver assinatura mínima | US$ 2.310 por ano por assento, pago adiantado, ou US$ 210 por mês por assento | grátis |
| Limite | exigido acima de US$ 25 milhões de receita anual | exigido acima de US$ 200 mil de captação ou receita anual | até US$ 200.000 de receita e captação |
| O que traz | suporte técnico premium; acesso ao código-fonte; três anos de LTS estendido | publicar em console e no Apple Vision Pro; atendimento prioritário; suporte premium à parte | tela de abertura opcional no Unity 6; Unity Cloud (Version Control, Asset Manager); Cloud Diagnostics |

| Ponto | Fato |
|---|---|
| Havok, depois do 6.3 | sem direito nem suporte da Unity; a equipe Havok da Microsoft pode oferecer a integração como extensão de terceiro |
| Para quem já assina | o preço novo vale na renovação em 12/01/2026 ou depois; o valor final varia por região, com imposto, câmbio e arredondamento |
| Havok Physics | sai do Pro, do Enterprise e do Industry a partir do Unity 6.3; segue com suporte até o fim do 2022 LTS e do 6.0 LTS |
| Reajuste | 5% no Pro e no Enterprise a partir de 12/01/2026, dentro do compromisso de reajuste anual previsível |
| Unity DevOps | acesso grátis ampliado em todos os planos, mais adiante em 2026 |
| Valores | todos em dólar americano |

**O FAQ dos planos, dos termos e da Runtime Fee**

| Ponto | Fato |
|---|---|
| Runtime Fee | cancelada em 12/09/2024; nunca foi aplicada a nenhum jogo, de nenhuma versão |
| Pro com US$ 25 milhões ou mais | passa ao Enterprise na renovação depois de 01/01/2025, com contato da Unity |
| Orçamento feito para a Runtime Fee | deixa de contar; o reajuste do Pro e do Enterprise de 2025 pode entrar no lugar |
| Enterprise abaixo de US$ 25 milhões | pode ficar no Enterprise |
| Educação e sem fins lucrativos | o reajuste do Pro vale para elas; as elegíveis têm a Education Grant License, grátis |
| Unity Runtime nos termos | citado como produto, a parte do software que se distribui, não como taxa |
| Industry | nenhuma mudança por ora |
| Termos do editor, por que mudaram | para tirar o texto da Runtime Fee e trazer os novos limites dos planos; em vigor desde 10/10/2024 |
| Reajuste e termos antigos | o preço muda também para quem ficou nos termos antigos, só na compra ou renovação |
| Quem os termos alcançam | todo usuário do editor, de todos os planos e versões |
| Limites, desde quando | Personal até US$ 200.000, desde o lançamento do Unity 6 (17/10/2024); Pro de US$ 200.001 a 24.999.999 e Enterprise de US$ 25 milhões em diante, desde 01/01/2025, na compra, renovação ou upgrade |
| Termos antigos | seguem valendo enquanto se usa a mesma versão nomeada do editor (de 2022.1 para 2022.2 é a mesma) |
| Unity 6 | exige aceitar os termos de 10/10/2024 |
| Comprar plano acima do exigido | sempre permitido |

**DevOps (Version Control e Build Automation)**

| Ponto | Fato |
|---|---|
| Concorrência | de 1 para 2 builds ao mesmo tempo; "Concurrent Machines" vira "Unity Editor Concurrency", a preço mensal fixo |
| Desde quando | 01/03/2026, para quase todos os clientes (quem tem contrato negociado fala com o vendedor) |
| Minutos grátis | 200 Windows (Micro), 100 Mac (Standard) e 100 Linux (Micro) por mês, em toda conta |
| Egress em março e abril de 2026 | sem cobrança (num ponto, a página fala só do primeiro mês) |
| Ultrapassar o grátis sem cartão | acesso bloqueado na hora, com risco de apagar os dados até haver cartão |
| Egress grátis | 100 GB por mês; acima disso, US$ 0,10 por GB; só conta download externo |
| Mac no grátis | o plano grátis passa a compilar para iOS e macOS |
| Assentos | Version Control na nuvem pública sem cobrança por assento; o Personal passa de 3 assentos grátis a ilimitado |
| Armazenamento grátis | 25 GB por organização por mês (antes 5 GB), medido em GB e não em GB-hora, dividido entre Version Control e Build Automation |
| Avisos | em 50%, 75%, 90% e 100% do grátis |
| On-prem | sem mudança de preço |

## U2. Planos e preços

**Os cartões da aba Games**

| Ponto | Enterprise | Pro | Personal |
|---|---|---|---|
| Para quem | times com problemas complexos; exigido acima de US$ 25 milhões de receita anual | times experientes e desenvolvedores solo; exigido acima de US$ 200 mil de captação ou receita anual | amadores e times indie pequenos; só aplicações de jogos e entretenimento |
| Preço | sob consulta, com vendas | US$ 210 por mês; na tabela, "a partir de US$ 2.310 por ano" | grátis, sem cartão |
| Créditos de IA por mês | 3.000, incluídos | 2.000, incluídos | 1.000 (IA grátis por 14 dias, depois paga) |
| O que soma | build na nuvem e on-prem; código-fonte só leitura; um ano a mais de LTS; suporte dedicado; licença para máquina offline | console e Apple Vision Pro; suporte mais rápido; mais nuvem | web, desktop, AR/VR e celular; Unity Cloud; acesso ao MCP da Unity; linha de comando |
| Ressalva | termos especiais para jogo de azar; pode haver compromisso mínimo | — | — |

**Linhas de valor da tabela de comparação** (Personal, Pro, Enterprise, Industry; a coluna Industry diz "Custom pricing")

| Item | Valores |
|---|---|
| Unity AI Credits por mês | Personal só com assinatura mensal; 2.000; 3.000; 3.000 |
| Conexões MCP simultâneas | Personal só com assinatura mensal; 3; 5; 5 |
| Asset Manager incluído | 10 GB por organização; 50 GB por assento; 120 GB por assento; 120 GB por assento |
| Asset Manager além disso | US$ 0,75 por GB nos quatro |
| Standard Storage | 25 GB por mês incluídos; US$ 0,10 por GB de 25 a 100 GB; US$ 0,06 acima de 100 GB |
| Premium Storage | US$ 0,30 por GB |
| Egress | 100 GB por mês incluídos; US$ 0,10 por GB |
| Minuto de build | Micro US$ 0,02 (Linux, Windows); Standard US$ 0,06 a 0,07; Premium US$ 0,11 a 0,12; Ultra US$ 0,18 a 0,20; Turbo US$ 0,37 (Windows) |
| Concorrência | 2 incluídas; US$ 10 por mês cada uma a mais |
| Version Control on-prem | US$ 38 por assento |
| Hospedagem de app do Studio | US$ 0,50 por GB |
| Suporte técnico padrão | "Additional costs; 1-19 seats; 1-9 seats" (três valores, sem dizer a coluna) |

| Ponto | Fato (lido no JSON do HTML, fora do texto extraído) |
|---|---|
| Unity AI para o Personal | US$ 10 por mês ou US$ 120 por ano, por assento; teste de 14 dias com cartão; 1.000 créditos; uma conexão MCP; quatro modelos |
| Unity Studio | US$ 799 por ano por assento |
| Unity Industry | US$ 450 por mês ou US$ 4.950 por ano, por assento; "para times que fazem aplicações industriais" |
| O que o Industry soma ao Enterprise | Unity Studio e Asset Manager; gestão de ativos 3D; mais de 70 formatos de importação 3D; suporte e treino dedicados; implantação própria e plataforma embarcada à parte |

**O FAQ da página**

| Ponto | Fato |
|---|---|
| Cancelar | não há cancelamento nem reembolso; deixar de pagar não tira a obrigação de pagar o período inteiro |
| Personal, para quem presta serviço | cabe se os clientes, somados, tiveram menos de US$ 200 mil de receita ou captação nos 12 meses anteriores |
| Licença flutuante | só no Enterprise |
| Pro, a partir de 01/01/2025 | exigido para empresa com mais de US$ 200 mil de receita ou captação nos últimos 12 meses e para quem trabalha para ela |
| De quem é o conteúdo | de quem o criou |
| Personal, para quem não presta serviço | empresa pequena com receita e captação somadas abaixo de US$ 200 mil; pessoa física com menos de US$ 200 mil gerados pelo uso do Unity |
| Pagamento | cartão de crédito, PayPal, Alipay, UnionPay; fatura só pelo vendedor |
| Unity Industry | exigido para quem faz aplicação fora de jogos e entretenimento e tem finanças acima de US$ 1.000.000 |
| Misturar planos | não; uma empresa escolhe Pro ou Enterprise |
| Cliente de indústria e os outros planos | Pro ou Enterprise só até US$ 1.000.000; Personal nunca |
| Unity Student | estudante de instituição credenciada, com idade para consentir com os dados (13 anos nos EUA, 16 na UE) |
| Rebaixar | não, durante o compromisso; subir pode, sem reduzir assentos |
| Enterprise | exigido acima de US$ 25 milhões de receita ou captação nos últimos 12 meses |

## U3. Termos do editor (trechos)

**Cabeçalho e seção 1, elegibilidade**

| Ponto | Fato |
|---|---|
| Versão | "Last updated: June 30, 2026" |
| Limite do Personal | US$ 200.000 em 12 meses; acima disso, nada de Personal, nem para projeto interno ou protótipo |
| O que mudou nela | "Platform" alinhado entre os termos; volta o termo "Designated User"; "User Modification" esclarecido; compromisso mínimo possível no Enterprise |
| Como se mede | a cada dia de uso, sobre os 12 meses anteriores |
| Limite do Student | US$ 1.000.000; acima disso, só o editor do Pro ou do Enterprise |
| Limite do Pro | de US$ 200.001 a US$ 24.999.999 |
| Total Finances, empresa que presta serviço | a receita bruta e a captação dos clientes, de qualquer origem |
| Ao passar do limite | subir de plano na hora |
| Prova | o usuário declara a elegibilidade, guarda os registros e prova se a Unity pedir |
| Limite do Enterprise | US$ 25.000.000 ou mais; daí em diante, só o Enterprise |
| Total Finances, pessoa física | se presta serviço, a receita e a captação do cliente; se não, o que o uso do software gerou |
| Limite do cliente de indústria | US$ 1.000.000; acima disso, só o Unity Industry |
| Proibido | usar planos de faixas diferentes ao mesmo tempo, entre membros da organização ou juntando projetos de faixas diferentes |
| Total Finances, empresa que não presta serviço | a própria receita bruta e captação somadas |
| Total Finances, governo, sem fins lucrativos, ensino | o orçamento inteiro da instituição |
| Vale fora de plano | os limites valem com ou sem plano da Unity |
| Plano acima do exigido | não precisa de elegibilidade |

**Seções 2 e 4, uso e cliente de indústria**

| Ponto | Fato |
|---|---|
| Cliente de indústria, definição | quem licencia para projeto de uso industrial, ou para qualquer uso que não seja só jogo ou entretenimento |
| Cliente de indústria, quem decide | a Unity, a seu exclusivo critério |
| Setores citados | automotivo, arquitetura, engenharia, construção, aeroespacial, manufatura, petróleo e gás, saúde, tecnologia educacional, varejo |
| Unity Industry | o plano feito para o cliente de indústria |
| Prestador de serviço, agência, revenda, plataforma | pode precisar de outra concessão; as licenças de 2.1 e 2.2 são para quem cria conteúdo próprio |
| Unity Runtime (2.2) | distribuído embutido no projeto, sem royalty, divisão de receita nem taxa de runtime nos projetos do Unity 6 ou anteriores, pagando a assinatura |
| Editor como serviço | proibido oferecer o editor ou processar dados com ele para terceiros, em nuvem ou SaaS, sem outra concessão |
| Runtime para cliente de indústria (2.2.1) | depende das taxas e de autorização expressa da Unity |
| Plano Student, uso comercial (2.1.1) | permitido no limite do plano, se o projeto é só do estudante, sem colaboração e sem distribuição comercial a terceiro |
| Student, quem | 16 anos ou mais, matriculado em instituição credenciada e verificado; até 10 anos somados |
| Região | a Unity pode restringir o editor às versões de unity.cn, conforme o lugar |
| Legal Entity | inclui governo e instituição sem fins lucrativos, de ensino ou acadêmica |
| Direito de uso (2.1) | instalar e rodar o editor só para uso interno, pelo número de usuários do plano, não exclusivo e intransferível |

## O que a fonte recomenda

Quem vai usar o Unity confere primeiro a soma de receita e captação dos últimos 12 meses, contando a dos clientes quando presta serviço, porque ela decide o plano a cada dia de uso e o Personal some acima de US$ 200 mil. A Unity diz quem é cliente de indústria, e quem faz algo que não é só jogo ou entretenimento passa ao Industry acima de US$ 1 milhão. A assinatura não se cancela nem se rebaixa no meio do compromisso, e o preço muda na renovação.

## Citações

- "If your Total Finances exceed $200,000 USD you may not use Unity Personal at all, even for internal projects or prototyping." (U3, 1.1)
- "Qualification of a Customer as an Industry Customer is determined in Unity’s sole discretion." (U3, seção 4)
- "Unity Industry plan is required if you create applications outside of games or entertainment and your company’s total finances exceed $1,000,000 USD." (U2, FAQ)

## Lacuna

Nenhuma das páginas diz se filme, animação ou vídeo feito no Unity, para si ou para cliente, conta como entretenimento ou como uso de indústria, nem dá um exemplo de conteúdo linear. U2 mostra o Industry como "Custom pricing" na tabela e só o JSON da página traz o preço por assento; U1 dá dois prazos para a isenção de egress (março e abril, e só o primeiro mês) e diz num ponto que o Havok sai dos planos no 6.0 LTS e noutro que sai a partir do 6.3. Os termos foram lidos por trechos; as regras de uso das subseções 2.3 a 2.10 e as demais definições ficaram fora.
