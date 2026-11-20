---
titulo: "Manual de Linguagem Simples: como planejar, desenvolver e testar textos que funcionam"
tipo: artigo
autor: "Patricia Roedel (Edições Câmara, Câmara dos Deputados)"
url: "https://www.gov.br/gestao/pt-br/acesso-a-informacao/estrategia-e-governanca/estrutura-de-governanca/arquivos/Manualdelinguagemsimples_comoplanejardesenvolveretestartextosquefuncionam.pdf"
publicado_em: 2024
capturado_em: 2026-11-04
licenca: "direitos reservados pela Lei 9.610/1998, nota na página de créditos (p. 4): sem autorização prévia da Edições Câmara só cabem breves citações com a fonte indicada. Sem licença aberta, entra só a ficha (item 2 de sources/README.md); o integral está na url"
areas: [content-design]
tags: [plain-language, comprehension-testing, usability-testing, cloze-test, readability-formulas, sample-size, audience-definition, information-architecture, typography, data-visualization, social-media, brazil]
---

# Roedel 2024 (Edições Câmara): Manual de Linguagem Simples

Ficha em palavras próprias de um manual de cerca de 17 mil palavras, lido inteiro; o integral não entra. 1ª edição, Brasília, 2024, linha institucional; ISBN 978-85-402-1044-8 (e-book) e 978-85-402-1043-1 (papel). A url é a cópia em PDF no site do Ministério da Gestão; a ficha catalográfica aponta para livraria.camara.leg.br. Texto extraído com `pdftotext`; as páginas 23, 51, 97 e 103 foram lidas também como imagem. Os números de página são os impressos: o PDF tem 108 páginas e a contagem impressa pula 41 e 93, então a página impressa é a do PDF até a 40, a do PDF mais 1 até a 92 e a do PDF mais 2 daí em diante.

**A licença (p. 4):** a frase veda reproduzir a obra, por qualquer meio, sem que a Edições Câmara autorize antes, e abre uma só exceção: "breves citações, desde que indicada a fonte". Lida inteira, ela permite citar pouco e com crédito; copiar o resto depende de autorização. A mesma nota reserva os direitos pela Lei 9.610 e dá à editora a venda exclusiva.

**Autora e encomenda:** jornalista e servidora da Câmara, consultora e instrutora do tema; dirigiu a Agência Câmara de Notícias, o jornalismo da casa e o LabHacker, coordenou a reformulação do site e esteve no grupo que adaptou a norma na ABNT (p. 109). O Conselho de Comunicação Social da Câmara pediu o livro, pensando em assembleias, câmaras municipais, Senado e Câmara; a autora diz que os conceitos servem também a empresas e aos outros Poderes (p. 9, contracapa). Os textos de exemplo da parte de design são de elaboração própria, com informações fictícias (p. 72, nota 9); parte dos outros veio de oficinas dadas com Joseane Corrêa (p. 46, nota 8). A apresentação é da deputada Any Ortiz, presidente do conselho (p. 11).

**Plano do livro:** conceitos (p. 12 a 33), planejar (p. 34 a 40), desenvolver (p. 42 a 92), avaliar (p. 94 a 105).

## Conceitos

- **Definição (p. 13):** técnicas de redação e de design da informação cujo teste é prático: o público-alvo acha, entende e usa o que precisa, sem releitura nem especialista ao lado. A meta declarada é a clareza, e por isso o nome engana: "o mote da técnica não é exatamente 'quanto mais simples melhor', mas 'quanto mais claro melhor'". Daí valer até para documento técnico dirigido a especialistas, caso em que trocar vocabulário sai do topo da lista (p. 13 e 14).
- **Alcance (p. 14):** quatro frentes (arquitetura da informação, frases, palavras, design), para que o esforço mental vá ao assunto e não à decodificação. Não é só para quem tem baixo letramento. A autora diz que as diretrizes têm amparo em psicolinguística, neurolinguística e design da informação, sem citar estudo nesse ponto. Norma: ISO 24495-1 (2023), adaptada pela ABNT em 2024 como NBR ISO 24495-1.
- **O que fica de fora (p. 19 e 20):** *Leitura Fácil* é técnica de acessibilidade para quem tem dificuldade de compreensão por deficiência intelectual, neurodivergência ou pouca fluência no idioma; tem outra validação, e quatro regras dela não se transferem (frases em caixa alta, texto em estrofes, evitar subjuntivo, evitar metáfora), sob pena de piorar a leitura de quem não tem deficiência. Linguagem Simples, sozinha, não garante acessibilidade. *Linguagem neutra* ("todes", "elu") não busca clareza e pode até atrapalhar quem não está habituado; *linguagem inclusiva* é outra coisa: usa "pessoas", dobra o gênero ou alterna os plurais. *Coloquial* também não: a norma culta fica. Dois quadros resumem: centrada no cidadão, objetiva, eficiente, clara e empática; nunca simplória, infantil, informal ou errada, na gramática ou na técnica.
- **Histórico (p. 16 e 17):** causa nascida nos anos 1940 (memorando *Brevidade*, de Churchill, 1940), com marcos no livro de John O'Hayre (EUA, 1966), Suécia e Canadá (1976), Carter (1978), Plain English Campaign (1979), selo britânico (1990), Constituição sul-africana (1996), memorando de Clinton (1998) e o Plain Writing Act (2010); hoje em mais de cinquenta países. O Plain Writing Act dá a data do Dia Internacional da Linguagem Simples, 13 de outubro. No Brasil: Constituição de 1988 como semente; LAI (2011), Lei de Inclusão (2015), Lei dos Direitos do Usuário (2017), LGPD (2018) e Lei do Governo Digital (2021), cada uma com sua expressão; programa municipal de São Paulo (2019) como marco, seguido de leis locais. O manual é anterior à Lei 15.263/2025.

## Por que usar: os números e a quem ele os atribui

| Afirmação | Número | Origem dada pelo manual | Página |
|---|---|---|---|
| Brasileiros com acesso à internet | 87,2% | IBGE, 2022 | 21 |
| Acessos à internet feitos por celular | 98,9% | IBGE, 2022 | 22 |
| Acessos ao site da Câmara por celular | 73% | dado da própria Câmara, sem referência | 22, 45 |
| Usuários eventuais do portal da Câmara | 75% | idem; ela estende por analogia às assembleias e câmaras municipais | 24 |
| Atenção em telas: 2min30s (2004), 1min15s (2012), 47s (2020) | | Gloria Mark, 2023 | 22 |
| Parcela do conteúdo lida, em mais de 45 mil visualizações de página | 18% | Nielsen, 2008 | 22 |
| Leitores que leem tudo | 16% | Nielsen Norman Group, 1997 | 22 |
| Prazo para decidir se a página serve | até 10 s | Nielsen, 2011 | 23 |
| Proficientes em leitura, de 15 a 64 anos | 12% | Inaf, 2018 | 25 |
| Analfabetos funcionais, mesma faixa | 30% | Inaf, 2018 | 25 |
| Estudantes do 1º ano do ensino médio com aquela proficiência | 0,2% | Pisa, "do mesmo ano" | 25 |
| Entrevistados que veem o país como burocrático | 84% | Fiesp, 2017 | 26 |

Em volta dos números, o argumento tem cinco partes (p. 21 a 26): a obrigação legal sem o "como"; a tela (atenção curta, leitura que varre em vez de seguir linha a linha, competição com notificações e outras abas); a informação buscada pelo leitor, o que o sociólogo Wolton (1999) chamou de mídias de demanda, opostas às de oferta, como jornal e TV; a baixa proficiência; e o custo (atendimento, retrabalho, intermediários, desistência). Na "leitura em F" a pessoa percorre linhas no começo e no meio do texto e fica, em média, nas duas primeiras palavras de cada linha (p. 22). O celular reforça a varredura, porque rolar é fácil (p. 23). Os 12% do Inaf são os que dão conta de texto complexo e conceito abstrato, separam fato de opinião implícita e fazem inferências (p. 25), e a autora põe em quem produz a obrigação de se fazer entender. Um quadro resume o ganho: mais efetividade, confiança, transparência, controle social, inclusão e democracia; menos tempo de atendimento, ruído, retrabalho, intermediários, corrupção por venda de facilidades e desistência (p. 27). A p. 26 traz uma lista para a Casa conferir o que o cidadão consegue fazer no site e no telefone.

## Entender não é conseguir usar, e quem usa a técnica

- **O exemplo da votação (p. 32 e 33):** a tabela do site mostra que um deputado votou "sim". Todos conhecem a palavra; o que o leitor quer saber é se ele é a favor do projeto, e o "sim" pode ter sido a um substitutivo ou à retirada de um trecho. Daí a pergunta do planejamento: para que serve esta informação, a que perguntas responde? Isso pode exigir acrescentar dados, legendas, passo a passo, significados e links, e o trabalho vai além de traduzir o texto existente.
- **Dupla validação (p. 31):** conforme a complexidade, o texto passa pelo público e pela área técnica em rodadas sucessivas, para seguir correto e utilizável: compreensão e utilidade cabem ao usuário, a correção técnica à equipe especializada. O ponto de partida é o que ele quer e precisa saber, seu interesse, conhecimento e letramento, e o contexto de uso.
- **Quem escreve (p. 30):** qualquer equipe que publique. O quadro inclui, na comunicação, redes sociais, notícias e peças publicitárias; na administração, páginas, editais, e-mails, opções telefônicas; na área legislativa, propostas e relatórios.

## Etapa 1: planejar

**O público (p. 35):** antes de escrever, fixar para aquela comunicação o grau de letramento, a idade, o quanto a pessoa sabe do assunto, para que vai usar a informação, em que situação vai lê-la e, no digital, sua competência digital. Às vezes entram profissão, formação ou região. O "contexto" inclui saber se ela busca algo ou se o conteúdo chega sem ser pedido, "como no caso de redes sociais". Esse perfil orienta arquitetura, redação, design e suporte, e é dele que saem os testadores. Se o alvo hoje não usa o serviço porque não consegue, planeja-se para ele, não para quem já vem.

**"Para todos" (p. 36):** a autora chama de "utopia de qualidade". A comparação é o carro, ajustado para quem mede de 1,60 m a 1,80 m e menos confortável para os demais: uma peça não atende igual o jurista e o analfabeto funcional. Um público genérico não dispensa o recorte: alguém tem de ser o leitor de consumo "ótimo". Quando há mais de um público, vem primeiro o principal; o exemplo é o portal, usado pela equipe interna e feito para o cidadão.

**Como conhecer o público:** quem já chega deixa rastro em estatísticas de acesso, cadastros, perguntas de atendimento e reclamações (p. 37); quem ainda não chega pede pesquisa e teste. A escolha do método pesa o que já se sabe, o porte e o impacto do projeto, o tamanho do desconhecimento e a capacidade da equipe de conduzi-lo corretamente.

| Família | Base do resultado | Métodos | Para quê, e cuidado |
|---|---|---|---|
| Atitudinal (p. 38) | o que as pessoas dizem | questionário online; entrevista semiestruturada; grupo focal; teste de compreensão | Questionário: validar hipótese quando já se conhece razoavelmente o público, com muitos respondentes. Entrevista: achar o que você não saberia perguntar e o contexto de uso. Grupo focal: experiências de quem já usou. Pergunta mal feita e intervenção do pesquisador enviesam. |
| Comportamental (p. 39) | o que as pessoas fazem | teste de usabilidade; pesquisa de campo | Campo: serviço complexo, público específico, pesquisador no ambiente do usuário. Registrar sem intervir. |

**Quando o problema é outro (p. 39):** processo interno redundante, banco de dados desestruturado, falta de transparência deliberada ou jornada mal planejada não se resolvem com redação.

**O conteúdo (p. 40):** definir o suporte (celular, computador, jornal, livreto, folheto, cartaz, tela de elevador), o que o público já sabe, o que precisa saber, que dúvidas tem e o que sobra. O excesso custa três vezes: tempo de atenção, varredura e carga cognitiva. "Saber quais informações cortar é tão importante quanto saber o que deve ser dito e em qual ordem."

## Etapa 2: desenvolver

Sequência (p. 44): identificar o que dizer, o que tirar, definir a arquitetura, estruturar as frases, rever as palavras, elaborar o design. A autora aproxima as diretrizes de jornalismo, UX writing e visual law (p. 43) e avisa que "dificuldade" é relativa ao documento e ao público; por isso muitos exemplos mantêm o vocabulário, e às vezes basta um glossário. Cada exemplo é reescrito em função da diretriz em pauta.

### Título e abertura

Não há diretriz própria sobre como redigir um título. O que há sobre a abertura está em "Escreva o mais importante primeiro" (p. 44 a 47): o primeiro parágrafo traz o que mais importa *para o público*, e o resto desce em importância. Dois leitores saem atendidos, quem se interessa e segue, e quem percebe que não é aquilo e não perde tempo. A prática a abandonar é o "nariz de cera", introdução sobre o tema que quase só tem função de estilo e que o leitor pula. Exceções: listas vão em ordem alfabética ou da data mais recente para a mais antiga; instruções e processos, em ordem cronológica (p. 45). Nos pares de antes e depois, as aberturas fracas dizem quem faz (e não o que se faz), se elogiam, enumeram integrantes ou explicam o Poder Legislativo em geral. Exemplo de depois: "O Politeia é um projeto que simula atividades legislativas para estudantes universitários atuarem como deputados ou jornalistas" (p. 46).

Sobre título, o restante está espalhado: títulos e intertítulos entram na lista de esquematização (p. 50); hierarquia visual por tipo, tamanho e peso (p. 78); caixa alta só em títulos e intertítulos curtos (p. 80); negrito, itálico ou light reservados a pouco texto, como títulos (p. 77); cor reservada a títulos, intertítulos, avisos e ícones (p. 82). No link, "Confira a Ordem do Dia" vira "Veja as votações previstas" (p. 67).

### Arquitetura da informação

- **Uma ideia por parágrafo (p. 48):** os erros opostos são parágrafo novo a cada frase e ideias diferentes no mesmo bloco; o branco entre blocos é o que deixa varrer. A convocação de mesário vira frase principal mais três rótulos (local, datas, horário de chegada) (p. 49).
- **Esquematizar (p. 50):** escolher entre índice, títulos, menus, links por nível de profundidade, listas, tabelas, gráficos, infográficos, imagens de apoio e vídeos, conforme tamanho, complexidade e suporte. O "principal objetivo" que na verdade são três vira lista de três (p. 50). A tramitação de medida provisória ganha um infográfico de apoio em fluxo (p. 51), e a tabela de andamento de um projeto vira versão gráfica com abas (p. 52 e 53).

### Frases

| Diretriz | Razão dada | Ressalva ou exemplo |
|---|---|---|
| Só o necessário (p. 54) | o supérfluo fica sem leitura e ainda esconde o que importa | 25 palavras por frase como teto de referência, artigos e preposições incluídos; o documento final pode ficar maior que o original, porque explicação e glossário entram |
| Voz ativa (p. 57) | clareza, proximidade do modelo mental, mostra o responsável; a passiva costuma trazer verbo substantivado | a passiva não é condenada: serve para pôr o foco no que se faz; converter pode exigir apurar quem fez |
| Ordem direta (p. 58) | a inversa custa mais processamento | o exemplo põe sujeito, verbo e complemento na ordem (os idosos, antes, precisam se vacinar) |
| Sem intercaladas (p. 59) | interrompem o raciocínio e alongam | o aviso da biblioteca perde um acréscimo no meio e outro no fim |
| Afirmativas (p. 60) | para ler o "não" pensa-se antes no positivo; a dupla negativa pesa mais | ficam só as negações necessárias: o exemplo troca a negação por uma condição afirmativa (o eleitor tira o passaporte quando regularizar a situação) |

### Palavras

- **Verbo substantivado (p. 61 e 62):** esconde o sujeito, alonga e é marca de burocracia. Vários pares corrigem junto outros defeitos, como anunciar processo interno em vez de resultado.
- **Termo impreciso (p. 63 e 64):** obriga a explicação depois. "Desafeta o perímetro" vira a informação concreta, reduzir em 40% a área da floresta; sites "suspensos" são trocados por sites que não serão atualizados, porque a primeira forma não deixava claro se saíam do ar.
- **Palavra comum (p. 65 e 66):** entre sinônimos, a mais usual (pretender em vez de objetivar, pedir em vez de peticionar, eleição em vez de pleito, tribunal em vez de corte, para em vez de "no sentido de"). Os sintomas da Covid perdem anosmia, mialgia e cefaleia.
- **Termo técnico (p. 67 e 68):** trocar ou explicar, e o texto costuma crescer. "A proposta sobresta a pauta" vira que ela tranca a pauta e impede outras votações.
- **Estrangeirismo (p. 68):** só quando mais conhecido que o termo em português (site, e-mail, mouse, airbag); o vocabulário de publicitários, gestores e analistas de TI escapa para o público sem que se perceba (checklist, coffee-break, download, expertise).
- **Sigla (p. 69):** usa-se se for mais conhecida que o nome (IBGE, CPF, CEP, CPI) ou se repetir muito, e aí com o nome na primeira menção. Sigla de setor interno, melhor omitir.

**Linguagem burocrática, as oito marcas da p. 70, agrupadas nesta ficha:** no conteúdo, quatro escolhas do que vai à frente: a introdução que adia o assunto, o órgão no lugar da ação, o fundamento legal e o elogio ao processo interno junto do resultado. Na palavra, jargão ou termo de especialista sem tradução e sigla de setor de dentro da casa. Na forma, fileira de verbos convertidos em substantivo e letra maiúscula em substantivo comum, plurais inclusive.

### Design

Abre com "Design é informação" (p. 72). Revisão técnica de Denise Faria (p. 4); as regras vêm sem citação, uma a uma; a seção indica duas leituras gerais (Nesta; Schriver, 1996, p. 92).

| Tema | Regra | Página |
|---|---|---|
| Suporte | cada um pede algo: o cartaz tem imagens, pouco texto, fonte grande e alto contraste, e se lê a 2 m; no site, pensar primeiro no celular; sem responsividade, uma coluna só e tabelas, gráficos e imagens mais verticais | 72, 73 |
| Alinhamento | à esquerda, jamais justificado, sem separar sílabas entre linhas | 74 |
| Linha | de 55 a 75 caracteres com espaços; curta cansa os olhos, longa faz perder a linha | 74 |
| Entrelinha | ao menos 20% acima do corpo; em média de 1,2 a 1,5 (corpo 10, entre 12 e 14); evitar a "simples" | 75 |
| Fonte em tela | sem serifa (Open Sans, Helvetica, Verdana, Roboto, Lato, Montserrat) | 76 |
| Tamanho | referências a testar, porque variam com a fonte: 16 pt no computador, 14 no celular, 10 em livreto impresso | 77 |
| Peso | regular no corpo; negrito, itálico e light para trechos curtos | 77 |
| Hierarquia e simplicidade | mostrar os níveis visualmente; no máximo dois tipos de fonte | 78, 79 |
| Maiúsculas | nenhuma frase inteira; só título ou intertítulo curto | 80 |
| Contraste | suficiente entre texto e fundo; em tela branca, cinza 90% em vez de preto 100%; no papel, depende do tom | 81, 82 |
| Cor no meio do texto | pode parecer link; deixar para títulos, avisos e ícones; se destacar, cor bem distinta da do link, e link sublinhado | 82 |
| Saturação e sentido | paleta suave e coordenada para não disputar atenção; tons fortes para ícones e avisos; não usar cor de alerta para coisa boa | 83, 84 |
| Ícones | da mesma família, traço simples, legíveis em tela pequena; "não é um enfeite": precisam ter relação direta com o texto | 85, 86 |
| Gráficos | pizza (parte do todo), barras (proporção), linhas (evolução) são os mais fáceis; evitar dispersão e áreas | 87, 88 |
| Eixos e legendas | poucas barras se leem melhor na vertical; em barras horizontais, o mês mais recente fica em cima; legenda na ordem dos dados | 89, 90 |
| Cor em gráfico | dados diferentes, cores bem diferentes; mesmo dado, mesma cor; quantidade, gradiente da mesma cor com contraste mínimo | 91 |

**Imagens:** não há seção sobre foto ou ilustração. Elas aparecem como "imagens de apoio" (p. 50), como item do cartaz (p. 72) e no pedido de formato vertical (p. 73). Infográfico é tratado como apoio ao texto (p. 51), e o exemplo vem da própria Câmara.

## Etapa 3: avaliar

### Quando testar e quando não

- **A experiência reduz a necessidade:** a equipe que já escreve assim para esse público traz o conhecimento acumulado (p. 95).
- **Não há como testar peça a peça** na rotina diária. Os exemplos do manual são "a produção diária de notícias ou de postagens em redes sociais" (p. 95). Daí que avaliar fora seja função de quão madura a equipe está na técnica.
- **Muito importante em quatro casos (p. 95):** o público muda em relação aos testes anteriores, em instrução ou em conhecimento do tema (de interno para externo, no exemplo); o texto vai durar, como página estática; a pessoa depende dele para cumprir um objetivo, como edital, formulário ou propaganda de utilidade pública; a equipe ainda não tem prática e precisa se calibrar.

### Quem e quantos

- **Quem (p. 96):** gente com as características fixadas no planejamento, mais critérios de exclusão para não enviesar. Para textos genéricos do Legislativo, ela sugere excluir servidores do órgão, pessoas próximas a eles (cônjuges, filhos), formados em direito, jornalistas especialistas em política, políticos e quem está fora da idade do voto obrigatório. Exclusão não vale quando a comunicação se dirige justamente a esse grupo.
- **Quantos (p. 96 e 97):** de três a cinco voluntários, um de cada vez, podendo ser remoto. O motivo é a curva de Nielsen e Landauer (1993), atribuída a "estudos de usabilidade": na *interface* de site ou aplicativo, cerca de 85% dos problemas aparecem em cinco participantes, se os itens e o grupo forem os certos; do sexto em diante os problemas se repetem e o custo deixa de compensar. O trabalho se faz em rodadas: corrigir o que se repetiu e voltar a testar com pessoas diferentes.
- **Uma pessoa só é "tiro no pé" (p. 97):** o problema de um único testador pode ser peculiaridade dele, e quem teve o trabalho de testar fica tentado a resolvê-lo, com risco de piorar o texto para a maioria. Entram na correção os repetidos e os que o próprio autor julga graves.
- **Custo (p. 96):** cada teste de 10 a 30 minutos; com anotação e compilação, cabe num dia. Para a autora, testar pede pouca estrutura e dinheiro, e sobretudo a cultura de foco no cidadão. O objetivo é o problema recorrente, sinal de dificuldade para muitos.

### Formas de avaliar

**Usabilidade (p. 96, 98):** para achar informação ou serviço em várias etapas ou telas, ou quando há muita navegação, tabela ou infografia. Vale online, com espelhamento de tela, em 10 a 30 minutos. As tarefas são amplas e sem pista: se o site tem nome próprio para um serviço, o nome não aparece na instrução. Exemplos: achar a transmissão de um evento, assinar o boletim, dizer em que comissão está um projeto.

**Compreensão, para texto com pouca navegação (p. 96, 99 e 100).** Mesmos critérios de seleção, participantes separados.

| Teste | Procedimento | Como ler o resultado |
|---|---|---|
| 1. Responder perguntas (p. 99) | lista sobre as informações centrais, sem o que se decora ou se confere fácil (nomes, horários); uma leitura, em silêncio, no ritmo natural; perguntas uma a uma, anotando só quem não entendeu | reescrever o que escapou a mais de um |
| 2. Grifar (p. 99) | mesma leitura, grifando termo ou estrutura não entendidos; depois, conversar sobre cada grifo e anotar | reescrever o que apareceu em mais de um; ignorar grifo isolado, porque todo testador tende a cumprir a tarefa e grifar alguma coisa |
| 3. Cloze (p. 100 e 101) | tirar uma palavra a cada cinco, com traço do tamanho dela; a adaptação sugerida é não contar os artigos, sem explicar por quê; a pessoa completa; vale só a palavra exata, sinônimo não conta | duas análises (abaixo) |

**A pergunta proibida (p. 99):** "Você entendeu o texto?" A pessoa sente que a prova é dela e tende a dizer que sim. Sim ou não também esconde o que importa: quem entendeu 95% provavelmente não relata o que faltou.

**Cloze, as duas análises (p. 100):** a primeira é a média de acertos: "inferior a 45%" manda reescrever, e "superior a 60%" é satisfatória. O manual não diz o que fazer entre 45% e 60%. Essa frase não traz citação; o que há é a lista "Para saber mais" do fim da etapa (p. 105), sem indicação de qual obra sustenta os cortes. A segunda olha a palavra: quando dois ou mais participantes erram a mesma lacuna, o manual manda separar a causa, vocabulário raro ou de especialista de um lado e sintaxe pesada de outro, e trocar o termo ou simplificar a frase conforme o caso. O teste se apoia, para a autora, na antecipação que o leitor faz da palavra seguinte a partir do que sabe sobre quais palavras costumam vir juntas, e a leitura flui mais quanto mais familiares forem a frase e o vocabulário. O exemplo (p. 101) é um trecho curto sobre o Orçamento, de elaboração própria, com 13 lacunas. Não há tamanho mínimo de texto nem número específico de testadores para o cloze além dos critérios gerais.

**Fórmulas (p. 102 e 103):** como medem tamanho de frase e de palavra, ignoram a escolha do vocabulário; não bastam sozinhas, mas servem de diagnóstico inicial e para comparar antes e depois. Duas foram adaptadas ao português, sem dizer por quem:

- Flesch: `248,835 - [1.015 x (palavras ÷ frases)] - [84,6 x (sílabas ÷ palavras)]`, assim impresso. Tabela: 90-100 muito fácil; 80-90 fácil; 70-80 razoavelmente fácil; 60-70 "padrão – Linguagem Simples"; 50-60 razoavelmente difícil; 40-50 difícil; 0-30 muito difícil. Ferramenta indicada: Nilc-Metrix (USP).
- Flesch-Kincaid: `[(0,39 x palavras por frase) + (11,8 x sílabas por palavra)] - 15,59`. Tabela: 90-100, 5 anos de escolaridade; 80-90, 6; 70-80, 7; 60-70, 8 a 9; 50-60, 10 a 12, marcado como Linguagem Simples; 40-50, universitários; 0-30, superior completo. Ferramenta indicada: www.legibilidade.com.

As duas tabelas, como impressas, não têm a faixa de 30 a 40, e as duas usam escala de 0 a 100.

**Inspeção (p. 104):** um avaliador percorre o documento com lista de verificação e marca os descumprimentos e sua severidade, como na avaliação heurística da usabilidade; melhor duas pessoas, independentes. O resultado não é ordem de alteração, porque as diretrizes "não são prescritivistas" e descumprir uma delas às vezes soa mais natural e dá ritmo. Ela não traz o olhar do público, então é complementar ao teste; só se torna obrigatória "na absoluta impossibilidade" de testar com ele.

## Redes sociais: tudo o que o manual diz

- **Ordem de leitura de postagem (p. 23):** um quadro mostra o padrão comum nas postagens, com o texto maior lido primeiro, o médio em seguida, o menor depois, e uma linha pequena em versalete no alto lida por último: "este você deixou por último". É demonstração visual, sem estudo citado.
- **Mídia de demanda (p. 24):** redes sociais entram, ao lado de sites e streaming, entre as novas mídias em que o usuário escolhe o que acessa, em que ordem e até onde.
- **Sem demanda (p. 35):** entre as características de público, o conteúdo que chega sem ter sido pedido aparece exemplificado pelas redes sociais. As duas passagens estão assim no texto, sem conciliação.
- **Quem produz (p. 30):** redes sociais constam entre os documentos da equipe de comunicação.
- **Exemplo de reescrita (p. 62):** num contexto marcado "postagem em rede social", uma frase passiva sobre projeto apresentado, com "admissão" e "manutenção do vínculo empregatício", vira uma frase ativa e curta, com o projeto de lei como sujeito, dizendo que ele proíbe o empregador de exigir do trabalhador a vacina contra a Covid-19. É o único exemplo com esse rótulo.
- **Teste (p. 95):** a passagem já registrada sobre a falta de tempo hábil na produção diária.
- **Conteúdo de exemplo (p. 64):** um aviso eleitoral menciona redes sociais do governo, sem tratar delas como formato.

Não há orientação específica sobre carrossel, Stories, legenda, gancho ou tamanho de postagem.

## De onde vêm as referências (como o manual as dá, sem conferência nesta ficha)

- **Atenção, leitura e tempo:** Mark, *Attention Span* (Toronto: Harlequin, 2023); Nielsen, "How little do users read" (2008), "How long do users stay on web pages" (2011), "How users read on the web" (1997); Nielsen et al., *How people read online: the eyetracking evidence* (2013), todos em nngroup.com.
- **Dados brasileiros:** IBGE, Pnad Contínua, acesso à internet 2022 (publicado em 2023); Inaf, Instituto Paulo Montenegro (2018); OECD, Pisa 2018; Fiesp, *Pulso Brasil: burocracia* (2017). Os 73% e os 75% da Câmara não têm referência.
- **Mídia de oferta e demanda:** Wolton, *Internet et après* (1999).
- **Teste e tamanho de amostra:** Nielsen e Landauer, *"A mathematical model of the finding of usability problems"* (1993, ACM); Henriques et al., *UX Research com sotaque brasileiro* (2022).
- **Cloze e apreensibilidade (p. 105):** Cunha e Santos, *"Validade por processo de resposta no teste de Cloze"* (*Fractal*, 2009; a referência saiu impressa com a marca editorial "[PLdC1]"); Santos et al., "O teste de Cloze na avaliação da compreensão em leitura" (*Psicologia: Reflexão e Crítica*, 2002); Martins e Filgueiras, *"Métodos de avaliação de apreensibilidade das informações textuais"* (2007). As fórmulas não têm referência própria.
- **Efeito da técnica, em "Para saber mais" (p. 28 e 29):** Cuesta et al. sobre o programa colombiano (BID, 2019); Roseth et al. (BID, 2018); Fischer (2017 e 2021, PUC-Rio, com o caso de um benefício do INSS); textos da própria autora (p. 18 e 29).
- **Guias e normas (p. 18, 92):** ABNT NBR ISO 24495-1; ISO 24495-1:2023; Center for Plain Language; Clarity; International Plain Language Federation; Plain Language Association International; Rede Linguagem Simples Brasil; Abep-TIC (2022); Fiocruz/Icict (2023); plainlanguage.gov; apostila da Prefeitura de São Paulo (2020); Nesta; Schriver (1996).
- **Exemplos da Câmara (p. 107):** PL 1366/2022, a página de votação nominal e "Entenda o processo legislativo".

## O que a fonte não diz

Não traz experimento próprio sobre nenhuma diretriz; os limites de 25 palavras, o tamanho de linha, a entrelinha e os corpos de fonte aparecem sem citação. Os três testes de compreensão vêm sem dados de validade comparada. O corte de 45% e 60% não tem fonte identificada no trecho. Os três a cinco participantes são dados para qualquer teste (p. 96 e 97), a partir de estudo de interface, e nenhum dado de compreensão os sustenta. Não menciona teste de paráfrase com esse nome. Não tem diretriz para redigir título, nem seção sobre foto ou ilustração, nem orientação sobre formatos de rede social. Não cita estudo que mostre o efeito de excluir ou não pessoas próximas do teste.
