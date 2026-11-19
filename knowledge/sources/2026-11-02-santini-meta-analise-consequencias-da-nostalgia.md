---
titulo: "A meta-analysis on the psychological and behavioral consequences of nostalgia: The moderating roles of nostalgia activators, culture, and individual characteristics"
tipo: paper
autor: "Santini, Fernando de Oliveira; Lim, Weng Marc; Ladeira, Wagner J.; Costa Pinto, Diego; Herter, Márcia M.; Rasul, Tareq"
url: "https://doi.org/10.1002/mar.21872"
publicado_em: 2023-07-18
capturado_em: 2026-11-02
areas: [content-design, psychology]
tags: [nostalgia, meta-analysis, consumer-behavior, behavioral-intention, visual-priming, cultural-orientation, emotion, advertising]
licenca: "CC BY 4.0 (declarada na página do artigo na Wiley Online Library, https://onlinelibrary.wiley.com/doi/full/10.1002/mar.21872, e registrada no Crossref para o DOI como http://creativecommons.org/licenses/by/4.0/)"
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Artigo em *Psychology & Marketing* 40(10), p. 1899 a 1912 (Wiley), publicado online em 18 de julho de 2023. Seis autores, entre eles Wagner J. Ladeira; o texto lido não traz as afiliações (ficaram fora da captura), e os agradecimentos dizem que o acesso aberto foi viabilizado pelo acordo da Wiley com a Swinburne University of Technology. Texto lido: a página completa do artigo na Wiley, capturada pelo Chrome em 2026-11-02, sem as figuras, os apêndices (A, o fluxo PRISMA; B, a análise post hoc) e as referências.

## A pergunta

Os experimentos de marketing com nostalgia não concordam entre si: a maioria acha ganho para a marca ou o produto, mas há achados nulos e negativos (os exemplos que o artigo dá: Gong et al., 2023, para o ganho; Lasaleta e Loveland, 2019, para o nulo; Wang e Chao, 2020, para o negativo). Os autores juntam os experimentos publicados para responder a duas coisas: (1) qual é o efeito da nostalgia manipulada em laboratório sobre quatro consequências, a sensação de agrado (*pleasantness*), a continuidade do eu (*self-continuity*), as atitudes e as intenções de comportamento; e (2) o que muda o tamanho desse efeito, entre três famílias de moderadores: o modo de ativar a nostalgia, a cultura do país da amostra e características da amostra. Base teórica: a *appraisal theory* da nostalgia de Van Tilburg et al. (2019), em que a nostalgia é emoção de aproximação, com o olhar no futuro.

## As treze hipóteses e o raciocínio de cada uma

Efeitos diretos (H1 a H4): a nostalgia aumenta o agrado (porque a emoção é feita de lembranças afetuosas, com traços positivos como calor e felicidade), a continuidade do eu (porque é uma emoção autorreferente, que regula a autoestima e dá sentido à vida), as atitudes e as intenções de comportamento (porque a maioria dos achados é positiva e o lado doce da emoção pesa mais que o amargo).

Ativadores (H5 a H9), cada um uma escolha de manipulação:

- H5, lembrança por **evento** versus por **objeto**: evento mais forte, por ser mais pessoal.
- H6, intensidade, cenário **realista** (listar cinco comidas que dão saudade) versus **não realista** (personagens de desenho animado): realista mais forte, por ser mais tangível.
- H7, conceito, ativação **com pessoas** (amigos e família num anúncio) versus **sem pessoas** (uma música do Led Zeppelin). O parágrafo que justifica diz que a ativação com pessoas é indireta, projetada num terceiro, e que por isso os autores esperam efeito mais forte **sem** pessoas; a frase formal da hipótese, porém, está escrita ao contrário ("stronger when evoked with people than without them", seção 2.4.1). A ficha registra as duas formas como estão; a seção de resultados trata o efeito mais fraco com pessoas como confirmação de H7.
- H8, priming **visual** (a marca Starbucks) versus **textual** (listar comidas): visual mais forte, por ser mais tangível e evocar mais do que só o sentimento.
- H9, nostalgia **pessoal** (vivida pela própria pessoa) versus **coletiva** (partilhada por um grupo): pessoal mais forte.

Características da amostra (H10 a H12): estudantes mais que não estudantes (amostra mais homogênea); maioria feminina mais que masculina (a nostalgia é ambivalente e as mulheres relatam emoções ambivalentes com mais intensidade, citando Leunissen et al., 2021); amostras mais velhas mais que mais novas (mais memória acumulada).

Cultura (H13): usa a dimensão de orientação de longo prazo de Hofstede (2010); culturas de curto prazo dão mais valor a recompensas ligadas ao passado e ao presente, então o efeito da nostalgia deveria ser maior nelas.

## O método

- **Busca:** Scopus, Web of Science e Google Scholar, com termos como "nostalgi*", "experiment", "marketing", "customer", "consumer" e "psychology", mais as referências de revisões e de estudos empíricos; autores contatados quando o texto completo não estava acessível. Primeira varredura: 132 artigos.
- **Inclusão:** para entrar, o estudo tinha de ser um experimento que manipulasse nostalgia; medir intenção de comportamento (o artigo aceita intenção comportamental, intenção de compra e disposição a comprar); informar média e desvio padrão dos dois grupos; estar em inglês; e ter saído até 31 de janeiro de 2023. Seleção pelo protocolo PRISMA (fluxo no apêndice A). Sobraram **22 artigos**, com **36 estudos** e **90 tamanhos de efeito**, somando **9.757 participantes** (a soma das amostras da tabela 1 dá exatamente 9.757, conferência de quem fez a ficha).
- **Codificação:** dois codificadores independentes, 97% de concordância, desacordos resolvidos em conversa. A tabela 2 lista o que foi codificado: identificação do artigo; contexto, país, descrição da manipulação, número do estudo, n, média e desvio padrão dos dois grupos e a variável dependente; os cinco ativadores como variáveis binárias (evento = 1; cenário não realista = 1; com pessoas = 1; visual = 1; coletiva = 1); a orientação cultural como contínuo pelo índice de Hofstede do país da amostra; tipo de amostra (só estudantes = 1), proporção de mulheres e idade média.
- **Estatística:** d de Cohen (nostalgia contra controle, padronizado pelo desvio padrão combinado), modelos de efeitos aleatórios; viés de publicação por teste de Egger e gráfico de funil; moderação por meta-análise linear hierárquica (HiLMA), uma regressão multivariada com todos os moderadores no mesmo modelo, no pacote metafor do R.
- **Egger, por consequência** (t; p): agrado 1,21; 0,270. Continuidade do eu −0,499; 0,628. Atitudes 0,177; 0,861. Intenções 1,51; 0,139. Nenhum significativo, e os autores dão o viés de publicação como ausente.

## Os estudos incluídos (tabela 1, resumida)

- **Quem:** Chang e Feng (2016); Chung (2019); Dimitriadou et al. (2019); Fan et al. (2020); Gong et al. (2023, quatro estudos); Hallegatte et al. (2018); Ju et al. (2016); Kessous et al. (2015); Kim e Magnini (2020); Langaro et al. (2020); Lasaleta et al. (2021, dois) e (2014, dois); Ma et al. (2021); Marchegiani e Phau (2012); Muehling et al. (2014); Muehling e Pascal (2011); Nam et al. (2016); Quach et al. (2022, dois); Wang e Chao (2020, dois); Zhou et al. (2012, cinco) e (2019, quatro); Zou et al. (2019). Revistas de marketing e consumo na maioria (Journal of Consumer Research, Journal of Advertising, Psychology & Marketing, Appetite, entre outras), mais duas de psicologia (Journal of Experimental Psychology: Applied; Personality and Social Psychology Bulletin).
- **Manipulações, contadas na tabela:** tarefa clássica de reflexão sobre um evento (*classic event reflection task*) em 14 estudos; fotos em 11; lembrança de evento passado em 8; músicas, personagens de desenho animado e nomes nostálgicos em 1 cada.
- **Países:** China 13 estudos, Estados Unidos 12, Coreia do Sul 2, Grécia, França, Portugal, Austrália e Reino Unido 1 cada, um estudo em fórum online e 3 sem país informado.
- **Contextos:** comida (sorvete, salada de frutas, comida saudável), doação, marcas (Starbucks, marca retrô, marcas nostálgicas e não nostálgicas), pasta de dente, câmera fotográfica, sandálias, perfume e protetor solar, cerveja, hospitalidade, consumo verde, livro de vendas, encher balões, tarefa de compra, música.
- **Tamanhos:** de 40 (Zhou et al., 2012, estudo 3) a 2.426 (Zhou et al., 2019, estudo 4); a maioria entre 100 e 400. Proporção de mulheres, quando informada, de 17,8% a 73%; idade média de 18,9 a 55,8 anos.

## Os efeitos diretos (seção 4.1 e figura 2)

Nostalgia contra controle, d de Cohen com intervalo de confiança de 95%:

| Consequência | d | IC 95% | Z | tamanhos de efeito | hipótese |
|---|---|---|---|---|---|
| Agrado (pleasantness) | 0,54 | 0,41 a 0,67 | 8,16 | 8 | H1 apoiada |
| Continuidade do eu | 0,84 | 0,75 a 0,94 | 17,45 | 9 | H2 apoiada |
| Atitudes | 0,47 | 0,41 a 0,54 | 6,96 | 20 | H3 apoiada |
| Intenções de comportamento | 1,31 | 0,94 a 1,68 | 6,96 | 53 | H4 apoiada |

Todos com p < 0,001. A heterogeneidade foi alta, I² de 69% a 99% (o teto na relação com intenções), e é isso que, segundo os autores, pede a análise de moderação.

## Os moderadores (tabela 3)

A moderação foi testada só sobre a relação entre nostalgia e **intenções de comportamento**, a única com mais de 30 tamanhos de efeito (critério de Geyskens et al., 2009). Coeficientes da regressão hierárquica:

| Moderador (código 1 vs. 0) | β | EP | Z | p | leitura dos autores |
|---|---|---|---|---|---|
| Intercepto | −9,50 | −3,60 | −14,66 | 0,000 | |
| Lembrança: evento vs. objeto | 5,29 | 0,60 | 8,73 | 0,000 | evento mais forte (H5 apoiada) |
| Intensidade: não realista vs. realista | −2,91 | 1,00 | −2,90 | 0,003 | realista mais forte (H6 apoiada) |
| Conceito: com pessoas vs. sem | −2,57 | 1,46 | −1,75 | 0,000 | com pessoas mais fraco (H7 apoiada) |
| Priming: visual vs. textual | 7,59 | 1,83 | 4,32 | 0,000 | visual mais forte (H8 apoiada) |
| Tipo: coletiva vs. pessoal | −0,07 | 1,43 | −0,05 | 0,962 | sem diferença (H9 não apoiada) |
| Amostra: estudantes vs. não | 0,09 | 0,29 | 0,34 | 0,729 | sem diferença (H10 não apoiada) |
| Proporção de mulheres | 0,05 | 0,01 | 2,11 | 0,028 | mais mulheres, efeito maior (H11 apoiada) |
| Idade média | −0,06 | 0,23 | −0,26 | 0,792 | sem diferença (H12 não apoiada) |
| Orientação cultural (de curto a longo prazo) | −0,06 | 0,01 | −6,05 | 0,001 | curto prazo mais forte (H13 apoiada) |

Detalhes que o texto e a tabela mostram e a ficha só registra: a seção 4.2.1 dá β = −2,58 e p < 0,001 para o conceito, enquanto a tabela traz −2,57, Z = −1,75 e p = 0,000; o erro padrão do intercepto aparece como −3,60. Saldo: dez hipóteses apoiadas e três não (H9, H10, H12); H7 contou como apoiada pelo efeito mais fraco com pessoas (ver a nota sobre a redação de H7 acima).

**Post hoc, a pedido dos revisores (apêndice B):** tipo de produto (serviço vs. bem), β = −0,81, p = 0,124; valor do produto (utilitário vs. hedônico), β = −0,05, p = 0,790. Nenhum moderou, e os autores concluem que não importa se o produto é serviço ou bem, utilitário ou hedônico.

## A discussão: as quatro contribuições

1. Fechar a conta dos estudos divergentes (positivos, nulos, negativos) com um efeito principal consolidado para cada uma das quatro consequências.
2. Dar conta de parte da heterogeneidade (até 99% de I²) com os moderadores. O efeito maior quando há mais mulheres na amostra é lido pelos autores como sinal de que gênero ajuda a explicar emoção (mulheres relatariam mais ambivalência), e vira sugestão de covariável para experimentos futuros.
3. Pôr as cinco manipulações lado a lado, coisa que um experimento isolado não faz: evento, cenário realista, sem pessoas e pista visual produziram mais intenção de comportamento, e os autores oferecem isso como guia para quem vai desenhar um experimento.
4. Entrar na lacuna da cultura (apontada por Sedikides e Wildschut, 2022). Os países das amostras caíram nos dois polos da escala de Hofstede: Austrália, Reino Unido e Estados Unidos no curto prazo; China, França e Coreia do Sul no longo. O efeito foi maior no primeiro grupo, e a explicação dada é a tendência dessas culturas a olhar o passado.

## O que os autores dizem que o resultado não cobre

Dois limites declarados. O primeiro é de cobertura: só entraram as variáveis que estudos em número suficiente informavam, e por isso os autores pedem que o resultado seja lido como um retrato do que a área mais mede, não de tudo o que importa; sugerem que novos estudos registrem o contexto em que a nostalgia aparece. O segundo é de profundidade: com os dados que havia, só deu para testar efeito direto e moderação; antecedentes, correlatos e mediadores ficam para pesquisa futura. O fecho é um conselho a pesquisadores e profissionais: o apelo nostálgico tem de ser ajustado ao fenômeno, ao produto e à cultura em que vai ser usado.

## Tudo o mais que ensina

- **Como o artigo define nostalgia, em camadas:** na abertura, uma ligação afetiva com o passado; na seção de agrado, uma saudade sentimental que traz de volta ocasiões boas; na de continuidade do eu, uma emoção sobre si mesmo que idealiza o que foi vivido; e o protótipo de Hepper et al. (2012), lembranças ternas, sobre si e sobre os outros, de tom positivo. O artigo registra ainda, com Merchant et al. (2011), que a lembrança embeleza pessoas, objetos e eventos em relação ao que foram.
- **Tamanho do mercado:** US$ 7,6 trilhões é o valor que a Euromonitor (2017) dá ao mercado de nostalgia nos Estados Unidos, número usado na abertura ao lado do anúncio dos 50 anos da Nike (2022).
- **Gatilhos citados na literatura:** marcas, produtos (comida, principalmente), eventos, lugares, fotos, músicas, cheiros (perfume), conversas com amigos e família; ocasiões especiais como aniversário de filho, reunião de família e feriados.
- **Como as manipulações são descritas:** a tarefa de reflexão sobre evento (Wildschut et al., 2006) pede que a pessoa lembre um evento nostálgico; produtos vintage servem para ativação por objeto (Schibik et al., 2022); listar cinco comidas que dão saudade é o exemplo de cenário realista e de priming textual (Gong et al., 2023; Zhou et al., 2019).
- **Hofstede, orientação de longo prazo:** a dimensão foi escolhida porque amarra passado, presente e futuro; no polo de longo prazo a sociedade espera a recompensa adiante, no de curto prazo a recompensa está no que já foi e no que é.
- **Agradecimentos:** a Constantine Sedikides e Tim Wildschut pela ajuda nas fases iniciais do manuscrito.
