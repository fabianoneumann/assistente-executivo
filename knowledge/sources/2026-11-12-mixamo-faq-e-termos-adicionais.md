---
titulo: "Mixamo | Common questions"
tipo: artigo
autor: "Adobe"   # página de ajuda da Adobe (helpx.adobe.com), sem assinatura de pessoa
url: "https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html"
publicado_em: 2021-09-14   # a página diz "Last updated on Sep 14, 2021"; é a data da última atualização, não a da primeira publicação
capturado_em: 2026-11-12
licenca: "protegido (página de ajuda e termos da Adobe; sem licença de conteúdo declarada no texto lido); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [licensing, commercial-use, royalty-free, mixamo, auto-rigging, humanoid-rig, character-animation, ai-training-restriction]
---

# Mixamo: grátis e sem royalties para personagens e animações, com a IA vetada nos termos adicionais

Nota de fato: tabelas do que o FAQ do Mixamo e os termos adicionais do serviço dizem sobre acesso, uso e restrições, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: as duas são protegidas.

**Proveniência.** Duas fontes da Adobe sobre o próprio serviço:

| Fonte | URL | Como foi lida | Data no texto | sha256 | Wayback |
|---|---|---|---|---|---|
| FAQ (a principal) | https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html | pelo Chrome, com os acordeões abertos, em 2026-11-12 (o curl e o WebFetch deram 403), e o texto da página gravado em `.txt` | "Last updated on Sep 14, 2021" | (hash omitido) (do `.txt`) | `http://web.archive.org/web/20261105220906/https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html` |
| Mixamo Additional Terms | https://wwwimages2.adobe.com/content/dam/cc/en/legal/servicetou/Mixamo-Addl-Terms-en_US-20210623.pdf | PDF baixado em 2026-11-12, uma página, texto extraído com `pdftotext` | em vigor desde 23 de junho de 2021, substituindo as versões anteriores; os metadados do PDF dão criação em 2021-06-18 | (hash omitido) | `http://web.archive.org/web/20240912075430/https://wwwimages2.adobe.com/content/dam/cc/en/legal/servicetou/Mixamo-Addl-Terms-en_US-20210623.pdf` |

Títulos conferidos no texto: o FAQ abre com "Mixamo | Common questions"; o PDF, com "Mixamo Additional Terms", e traz no pé o código "Mixamo Additional Terms_en_US-20210623". Cobertura: o FAQ inteiro (sete perguntas, aqui M1 a M7, na ordem da página) e o PDF inteiro (o preâmbulo e a seção 1, única). No preâmbulo do PDF, a extração perdeu as palavras entre aspas que nomeiam os termos definidos (ficam lacunas no meio das frases); a seção 1 saiu inteira. Os Termos Gerais de Uso da Adobe, a que o PDF remete, e o tutorial do Photoshop citado na M7 não foram abertos.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra cada um dos dois textos, com 32 unidades medidas (17 de prosa, 15 de célula com texto) e 0 trechos de 3 ou mais nas duas rodadas; colada, 1 contra o FAQ (a célula do motivo da China) e 0 contra os termos. Na leitura lado a lado das mesmas 32 unidades, segue a fonte a que traduz uma frase inteira dela, junta duas ou funde três ou mais na ordem dela; o fragmento que só traz um fato e a frase que junta lugares distantes em outra ordem não contam. Resultado: 11 de 32 (a frase de "Em uma frase", a célula do motivo da China, a do vínculo com os Termos Gerais, as cinco células do auto-rig, as duas do serviço e a segunda frase da recomendação; ficam fora as três células da cláusula de IA, que trazem cada uma um pedaço da mesma frase, as células da proveniência, a primeira frase da recomendação e a lacuna). A maior sequência de unidades seguidas que seguem a fonte é de 8 (da célula do vínculo com os Termos Gerais às duas do serviço), mas a fonte anda para trás dentro dela; na ordem da fonte, a maior é de 2, sem trecho colado de 3 ou mais. Na tabela "O serviço" (revista em 2026-11-19), as seis células de M4 e M5 viraram duas, a de M4 aberta pela exclusão e a de M5 aberta pelo conselho, com as frases da fonte em outra ordem (3, 1, 2, 4); nenhuma das duas segue mais uma frase da fonte, e a sequência de 8 acima termina antes delas.

## Em uma frase

Texto da Adobe sobre o próprio serviço: o Mixamo é grátis com um Adobe ID, e os personagens e animações dele entram sem royalties em projeto pessoal, comercial ou sem fins lucrativos, enquanto os termos adicionais de 2021 proíbem usar o serviço ou o que sai dele para criar, treinar, testar ou melhorar IA.

## O que o uso permite, exige e proíbe

| Tema | Ponto | Fato | Onde |
|---|---|---|---|
| Uso comercial | Permitido? | sim | M3 |
| Uso comercial | Royalties | nenhum, para personagens e animações | M3 |
| Uso comercial | Outros usos cobertos | pessoal; sem fins lucrativos | M3 |
| Uso comercial | Exemplos dados | ilustração e arte gráfica; impressão 3D; filme; videogame | M3 |
| Uso comercial | Preço | grátis, sem compra nem assinatura extra | M1, M2 |
| Atribuição | — | o FAQ não fala | — |
| Modificação | — | o FAQ não fala | — |
| Redistribuição | Arquivos de personagem ou animação como estão | o FAQ não fala | — |
| Saídas | Obra feita com personagem ou animação | dentro dos usos cobertos acima | M3 |
| Território | País vetado | usuário com código de país da China | M1 |
| Território | Motivo dado | a Creative Cloud da China sem os serviços web | M1 |
| Teto de receita | — | o FAQ não fala | — |
| Registro | Conta | Adobe ID, sem assinatura da Creative Cloud | M1 |
| Registro | Contas vetadas | Enterprise ID; Federated ID | M1 |
| IA | Veto | criar, treinar, testar ou melhorar de outro modo | Termos, §1 |
| IA | Alvo do veto | algoritmos de aprendizado de máquina; sistemas de IA, com arquiteturas, modelos e pesos | Termos, §1 |
| IA | Com o quê | o serviço, o software e o que sai ou deriva deles (conteúdo, dado, saída, informação) | Termos, §1 |
| IA | Modo | direto ou indireto | Termos, §1 |
| IA | Terceiros | também vetado instruir ou permitir | Termos, §1 |
| Termos | Vínculo | parte dos Termos Gerais de Uso da Adobe (adobe.com/go/terms) | Termos, preâmbulo |
| Termos | Versões anteriores | substituídas pela de 23/06/2021 | Termos, preâmbulo |

## Quando o auto-rig falha (M6)

| Grupo | O que conferir | O que a página diz do contrário |
|---|---|---|
| Lugar e pose | na origem (0,0,0); pose padrão ou neutra | deslocamento na animação por diferença de unidade; assimetria ou pose prévia podem impedir |
| Arquivo | só o personagem: sem auxiliares, câmeras ou objetos de cena | o auto-rig não funciona |
| Malha | limpa, sem erro, sem vão entre as peças | cabeça solta não funciona; malha limpa dá rig mais confiável e animação melhor |
| Forma | humanoide com cabeça, corpo, braços e pernas distintos; sem membros extras, asas, caudas, cabelo ou roupa grandes | proporção muito deformada e apêndice grande podem impedir |

## O serviço

| Ponto | Fato | Onde |
|---|---|---|
| Corpos aceitos | bicho, veículo e objeto ficam de fora: tanto o auto-rig quanto as bibliotecas de animação atendem só a humanoide bípede | M4 |
| Como não perder o rig | a página aconselha baixar cada personagem assim que ele ganha o rig, porque o site guarda um só, o último usado; quando entra outro, o anterior e as animações dele se perdem, sem histórico, e trocar a animação depois pede reenviar ao Mixamo o arquivo que já tem o rig | M5 |
| Suporte a programa de terceiros | a Adobe não dá | M7 |
| Tutorial indicado | animar personagem 3D com o Mixamo no Photoshop | M7 |

## O que a fonte recomenda

Antes de subir, o personagem precisa ser um humanoide bípede sozinho no arquivo, inteiro, na origem e em pose neutra, e depois do rig ele deve ser baixado na hora, porque o site só lembra do último. O uso em obra (filme, jogo, impressão, ilustração) é livre e sem royalties, mas nada que passe pelo Mixamo pode alimentar o desenvolvimento de um modelo de IA, nem por terceiros.

## Citações

- "You can use both characters and animations royalty free for personal, commercial, and non-profit projects" (FAQ, M3)
- "Mixamo is not available for users who have a country code from China." (FAQ, M1)
- "create, train, test, or otherwise improve any machine learning algorithms or artificial intelligence systems" (Additional Terms, §1)

## Lacuna

O FAQ não diz se é preciso dar crédito, se os arquivos de personagem e de animação podem ser redistribuídos ou revendidos como estão (num pacote de assets, por exemplo) nem se o uso vale para personagem próprio e para os da biblioteca do mesmo jeito. Não diz se usar uma animação do Mixamo dentro de um vídeo gerado com ajuda de IA cai na proibição dos termos adicionais, que, no texto lido, não definem "output" nem tratam de obra final. As duas fontes têm datas de 2021, e nenhuma diz se há versão mais nova dos termos.
