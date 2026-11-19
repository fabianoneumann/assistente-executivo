---
titulo: "AI Motion Capture Pricing · Plask"
tipo: artigo
autor: "Plask (Plask USA Inc., nos termos)"   # páginas do site da Plask, sem assinatura de pessoa
url: "https://plask.ai/en-US/pricing"
publicado_em: null   # a página de preços não traz data (só '© 2026 Plask' no rodapé); os termos dizem "Last Updated: April 5, 2023"
capturado_em: 2026-11-12
licenca: "protegido (rodapé da página de preços: '© 2026 Plask'; a dos termos não traz rodapé no HTML lido); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [plask, motion-capture, markerless, pricing, licensing, commercial-use, terms-of-service, user-content, interested-party, fbx, bvh]
---

# Plask: três planos de captura por vídeo, e termos que dão a licença comercial só a um plano "Commercial"

Nota de fato: uma tabela da página de preços e uma tabela por seção dos termos de serviço que trata de licença, uso comercial, conteúdo do usuário e uso de dados, na ordem dos termos, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: as duas páginas são protegidas.

**Proveniência.** Duas páginas da Plask sobre o próprio serviço, as duas baixadas em HTML com `curl` em 2026-11-12 e lidas no texto extraído do bloco principal, conferido no HTML. Os sha256 são os do texto do `<main>`/`<article>` sem tags, script e estilo, não os do HTML inteiro.

| Página | URL | Data no texto | sha256 | Wayback |
|---|---|---|---|---|
| Preços (a principal) | https://plask.ai/en-US/pricing | nenhuma | (hash omitido) | `http://web.archive.org/web/20261022231704/https://plask.ai/en-US/pricing` |
| Terms of Service | https://plask.ai/docs/100002 | "Last Updated: April 5, 2023" | (hash omitido) | `http://web.archive.org/web/20240529023956/https://plask.ai/docs/100002` |

Títulos conferidos no texto: a página de preços abre com "AI Motion Capture Pricing"; a dos termos, com "Terms of Service" e "PLASK USA INC.". Texto de quem vende o serviço.

**Cobertura.** A página de preços inteira (os três planos), com o preço da cobrança mensal tirado dos dados da própria página, onde fica o valor do botão "Monthly billing" (o texto extraído só mostra o preço anual). Os termos foram lidos inteiros, do preâmbulo à seção "Complete Agreement"; ganham tabela, na ordem deles, as seções que tratam de licença, uso comercial, conteúdo do usuário e uso de dados: Summary, Agreement to these TOS, Terms of Sale, Workspaces (com Unpaid Users e Paid Users), Commercial Users, User IP License, Service License, Intellectual Property Rights, Consent to Use of Data, a parte de licença da seção NFTs, User Content, Prohibited Conduct e Changes, Suspension or Termination. Ficam sem tabela, lidas, as de créditos, pagamento, recibo, menores, impostos, a mecânica das NFTs, serviços de terceiros, aviso, senha, garantia, responsabilidade, indenização, suporte, exportação, governo dos EUA, comunicações, lei e foro, e as cláusulas finais; três fatos delas vão na última tabela. Os termos não falam em aprendizado de máquina fora da User IP License. A Privacy Policy, a que os termos remetem, não foi aberta.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2, contra os dois textos extraídos juntos, preços e termos, num arquivo só). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), com 58 unidades medidas (23 de prosa, 35 de célula com texto), 0 coladas e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 58 unidades, segue a fonte a que traduz uma frase ou cláusula dela, junta duas ou funde três ou mais na ordem dela; ficam fora as seis células que só listam fatos (as duas listas de recursos dos planos e as quatro listas de atributos de uma licença) e a frase que junta seções distantes ou as duas páginas. Resultado: 30 de 58 (29 células com texto, cada uma o resumo de uma cláusula dos termos, e a segunda frase da recomendação, que junta Commercial Users e Service License na ordem dos termos); nenhuma das outras 22 frases de prosa (proveniência, esta conferência, "Em uma frase", a primeira frase da recomendação e a lacuna) segue a fonte. A maior sequência de unidades seguidas que seguem a fonte, na ordem dela, é de 28 (as células com texto da Summary à Changes, Suspension or Termination), porque as tabelas seguem as seções dos termos na ordem, como pede o formato de termos lidos por seção; é texto normativo do serviço, não argumentativo, e não há trecho colado no texto que recomenda ou conclui.

## Em uma frase

Texto da Plask sobre o próprio serviço: a página de preços oferece Freemium (15 segundos por dia), Standard e Pro, sem falar em licença, e os termos de 2023 limitam o serviço a uso pessoal não comercial, dão licença comercial só a quem assina um plano "Commercial" e tomam do usuário uma licença ampla sobre o que ele envia, inclusive para aprendizado de máquina.

## A página de preços

| Plano | Preço anual | Preço mensal | Captura | Armazenamento | Além do que todos têm |
|---|---|---|---|---|---|
| Freemium | grátis, sem assinatura | — | 15 segundos por dia | 1 GB | — |
| Standard | US$ 18 por mês, cobrança anual | US$ 40 por mês | 10 minutos por mês | 3 GB | processamento mais rápido |
| Pro | US$ 50 por mês, cobrança anual | US$ 140 por mês | 1 hora por mês | 10 GB | processamento mais rápido; recursos antes do lançamento; benefícios de organização |

| Ponto | Fato |
|---|---|
| O que todos os planos listam | corpo inteiro e mãos; várias pessoas; exportação FBX, GLB e BVH; render de vídeo; compartilhar cena; colaboração em tempo real; câmera e luz automáticas; efeitos ajustáveis |
| Licença ou uso comercial | a página não fala |
| Plano chamado "Commercial" | não aparece |

## Os termos, por seção

### Summary

| Ponto | Fato |
|---|---|
| Valor do resumo | só conveniência; vale o texto inteiro |
| Uso permitido | só pessoal e não comercial |
| Venda ou transferência | vetada, do serviço e de conteúdo ou item digital dele |
| Propriedade da Plask | não copiar nem modificar, salvo o que os termos permitem |
| Conteúdo que o usuário posta | a Plask pode usar para qualquer fim, inclusive publicidade |
| Foro | tribunais de Seul, Coreia |

### Agreement to these TOS and Future Changes

| Ponto | Fato |
|---|---|
| Natureza | o serviço é licenciado, não vendido |
| Mudança dos termos | a critério da Plask, sem consentimento, valendo ao publicar |
| Aceite da mudança | continuar usando o serviço |

### Terms of Sale

| Ponto | Fato |
|---|---|
| O que se faz | vídeo de captura de movimento ("User Video") a partir do vídeo bruto enviado |
| O que o serviço inclui | Plask Tool; Plask API; personagens avatar 3D; captura de movimento |

### Workspaces, Unpaid Users e Paid Users

| Ponto | Fato |
|---|---|
| Conta | um Workspace licenciado, com um dono, para cobrança |
| Dois níveis | Unpaid Users (só o grátis, com compra avulsa) e Paid Users (assinatura mensal) |
| Unpaid, processamento | tempo limitado por dia; exemplo dos termos: 30 segundos |
| Unpaid, mais tempo | pagar uma taxa ou esperar o dia seguinte |
| Paid, mínimo mensal | o texto traz o marcador "[NUMBER OF HOURS]", sem número |
| Paid, recursos avançados com taxa à parte | várias pessoas; Plask API; AI Physics Engine |

### Commercial Users

| Ponto | Fato |
|---|---|
| Quem | Paid Users do plano de assinatura "Commercial" |
| Força | vale mesmo contra o que os termos disserem em contrário |
| Licença recebida | não exclusiva, sem royalties, mundial |
| Sobre o quê | a propriedade da Plask (Plask IP) dentro dos User Videos e na distribuição deles |
| Atos cobertos | usar, copiar, modificar, exibir, executar em público, reproduzir |
| Fins | comerciais e não comerciais, em toda mídia |
| Marcas da Plask | só pelas instruções escritas e pelas diretrizes de marca |

### User IP License

| Ponto | Fato |
|---|---|
| User IP | toda propriedade intelectual que o usuário fornece para criar, produzir ou distribuir User Videos |
| Dono | o usuário, por inteiro |
| Licença à Plask | irrevogável, não exclusiva, já paga, sem royalties, mundial |
| (a) | acessar, usar, copiar, modificar, derivar, reproduzir e analisar, para prestar o serviço |
| (b) | processar por aprendizado de máquina, otimização algorítmica, análise humana e meios parecidos |
| (c) | exibir no User Video e na distribuição e promoção dele, e na publicidade da Plask, em toda mídia |
| Garantias do usuário | ter os direitos; nada ilegal, difamatório ou pornográfico; responder sozinho pela violação |

### Service License

| Ponto | Fato |
|---|---|
| Licença do serviço | limitada, revogável, pessoal, não comercial, intransferível, sem sublicença, não exclusiva |
| Dispositivos | só os do usuário |
| Vetado | alugar, vender, redistribuir; descompilar ou fazer engenharia reversa; derivar o serviço |
| User Videos | contêm Plask IP |
| Licença sobre a Plask IP no vídeo | limitada, revogável, pessoal, não exclusiva, intransferível, mundial, para usar no vídeo e distribuí-lo em toda mídia |
| Uso comercial da Plask IP | vetado sem consentimento escrito, salvo o que os termos preveem |
| Redes sociais pessoais | postar User Videos nelas não conta como fim comercial |

### Intellectual Property Rights

| Ponto | Fato |
|---|---|
| Plask IP | todo o conteúdo do serviço (dados, software, texto, imagem, vídeo, áudio, interface), fora a User IP e o conteúdo do usuário |
| Dono da Plask IP | a Plask ou quem a licencia |
| Leis citadas | dos EUA, da Coreia do Sul e internacionais |
| Marcas | não registrar nem usar marca da Plask ou parecida sem consentimento escrito |
| User IP | do usuário; a Plask não responde por ela |

### Consent to Use of Data

| Ponto | Fato |
|---|---|
| O que a Plask coleta | dados técnicos e de uso do aparelho, do sistema e do aplicativo |
| Para quê | atualização, suporte e outros serviços |
| Uso para melhorar produtos | permitido, na forma que não identifica a pessoa |

### NFTs (a licença)

| Ponto | Fato |
|---|---|
| Quando vale | quando o usuário pede à Plask que crie uma NFT com User IP |
| Licença à Plask | não exclusiva, perpétua, irrevogável, transferível, mundial, para a NFT e para a publicidade da Plask |
| O que o usuário recebe | uma porcentagem da venda da NFT |
| Taxa de criação | o texto traz o marcador "[AMOUNT HERE]", sem valor |

### User Content

| Ponto | Fato |
|---|---|
| O que é | o que o usuário cria, envia ou publica no serviço, inclusive User Videos e metadados |
| Sigilo | não é confidencial |
| Devolução | não é devolvido |
| Licença à Plask | mundial, irrevogável, perpétua, não exclusiva, transferível, sem royalties, com direito a sublicenciar |
| Atos cobertos | usar, copiar, adaptar, modificar, distribuir, licenciar, vender, exibir, transmitir e explorar, para qualquer fim |
| Também coberto | nome de usuário, persona e imagem que aparecem no conteúdo |
| Direitos morais | o usuário renuncia ao crédito e aos direitos morais, onde a lei deixa |
| Fora do serviço | salvar e compartilhar em outros apps e sites, salvo aviso da Plask |
| Infração de direito autoral | aviso ao agente DMCA (Gamma Law, San Francisco); conta de infrator reincidente pode ser encerrada |

### Prohibited Conduct

| Ponto | Fato |
|---|---|
| Item (h) | usar o serviço para qualquer fim comercial |
| Outros vetos | burlar limites de uso, usar conta alheia, violar propriedade intelectual de terceiros, entre outros |

### Changes, Suspension or Termination of the Service

| Ponto | Fato |
|---|---|
| Vigência da licença | até o usuário ou a Plask encerrar |
| Violação | encerra os direitos sem aviso; a Plask avisa e pode suspender por 30 dias antes de encerrar |
| Ao encerrar | parar de usar e apagar os apps; a conta e os dados podem se perder, sem reembolso |

### Outros pontos lidos

| Ponto | Fato | Seção |
|---|---|---|
| Lei aplicável | federal dos EUA e da Califórnia | Governing Law |
| Teto de responsabilidade da Plask | US$ 50 | Limitation of Liability |
| Idade mínima | 13 anos nos EUA; 14 em outros países, entre eles a Coreia do Sul; menor de 18 com consentimento do responsável | Minor Users |

## O que a fonte recomenda

Os termos pedem que o usuário os releia antes de cada uso, porque mudam sem aviso, e que só envie o que tem direito de enviar, já que o conteúdo fica com a Plask para qualquer fim. Quem quer uso comercial do resultado precisa do plano "Commercial"; sem ele, vale o uso não comercial, e postar o vídeo nas redes sociais pessoais não conta como comercial.

## Citações

- "You may only utilize the Service for personal non-commercial use." (Terms, Summary)
- "posting User Videos on your personal social media channels will not constitute a commercial purpose under these TOS" (Terms, Service License)
- "process User IP through machine learning, algorithmic optimization, human analysis, and similar approaches" (Terms, User IP License)

## Lacuna

A página de preços não diz qual plano, se algum, é o plano "Commercial" dos termos, nem fala de licença por plano; os termos são de abril de 2023, e a página de preços não tem data, só o "© 2026" do rodapé. Os termos dão 30 segundos por dia como exemplo do limite grátis, e a página de preços, 15. O texto dos termos tem marcadores não preenchidos: as horas mínimas do plano pago, a taxa de criação de NFT e o endereço e o contato da Stripe. Os termos não dizem se o item (b) da User IP License inclui treinar modelos da Plask com o vídeo enviado, nem dão um jeito de recusar. Nenhuma das páginas fala de atribuição ao usar o resultado.
