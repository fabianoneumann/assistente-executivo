---
versao: 1.0
status: em uso; os limiares são chute informado até as peças e as métricas da própria conta dizerem o contrário
---

# Rubrica de qualidade de conteúdo

O que a mensagem de uma peça precisa ter para ser dada como pronta antes de exportar e publicar. Vale para carrossel e, com as variantes marcadas, para tela única e Reels. **A forma (hierarquia, legibilidade, sistema visual, cara de IA) está em `rubrica-de-design.md`**, e as duas fecham juntas no portão (`portao-de-qualidade.md`). Nasce da evidência de plataforma (`knowledge/content-design/o-que-prediz-desempenho-instagram.md`), dos métodos de mercado para carrossel na fala pública de criadores, do público em `context/publico.md`, da voz em `context/sobre-mim.md` e das rubricas de juiz que já existem (`knowledge/agent-engineering/rubricas-existentes-e-o-avaliador.md`). Como vira avaliador automático: `knowledge/agent-engineering/desenho-de-rubrica-e-veredito.md`, "Escalas e checklists para juízes de IA" e "O que isto dá para uma rubrica de portão".

**Como ler.** Cada critério tem três níveis descritos como situação (0, 1 e 2), e abaixo da tabela os **testes de sim ou não** que levam ao nível: como regra geral, o critério é 2 quando todos os testes passam, 1 quando passa o primeiro e falha algum outro, 0 quando falha o primeiro. Quando a tabela descreve o nível por contagem (D, G, O) ou nomeia o caso (K: várias chamadas ou venda colada é 0), vale a tabela, e os testes ajudam a achar o nível. Cada teste aceita "não se aplica" (no Jev, ele sai das variantes da peça, decidido no código, nunca como opção da pergunta). Os limiares são chute informado até as métricas da própria conta dizerem o contrário.

**Quem avalia cada teste** (a etiqueta antes do teste):

- **[código]** medida exata no HTML ou no texto, sem modelo: contagem de palavras, de chamadas, travessão.
- **[jev]** pergunta fechada sobre o HTML e o texto, que um modelo de decisão (o Jev, da TypeSafe) responde bem e barato. **O Jev é opcional:** só roda com a `TYPESAFE_API_KEY` configurada, pelo cliente em `scripts/jev/`. Sem ele, e até duas condições valerem critério a critério, o juiz do portão responde estes testes: a régua do critério decidida por quem decide o conteúdo, numa releitura com os testes à vista, e o Jev concordando com o juiz nesses testes, conferido numa amostra pequena contra o fato. O Jev passa ao juiz quando não está seguro.
- **[modelo]** precisa de leitura: um modelo de fronteira com saída estruturada (raciocínio antes da nota).
- **[pessoa]** voz, valores e leitura própria: fica com quem decide o conteúdo da conta.

## Falhas de integridade

A peça engana, se apropria ou fere um valor. Cada falha tem um de dois destinos, e quem aponta propõe o destino; quem decide o conteúdo confirma:

- **Reprova** (volta para a pauta) quando corrigir muda a tese ou o formato: a peça não se sustenta sem a afirmação, a compilação, a promessa.
- **Corrigir** quando corrigir muda uma frase, um número, uma atribuição ou uma imagem, e a tese fica de pé. A peça não sai enquanto a correção não for conferida.

**O teste do destino:** tire da peça o trecho com a falha. Se a capa ainda promete o que as telas entregam e a tela de salvar continua de pé, o destino é corrigir. Se a capa ou a tela de salvar deixam de se sustentar, porque o trecho era o número, a fonte ou o exemplo em que a peça se apoia, o destino é reprova. Exemplo: uma peça cuja tese é um repositório que nunca é nomeado e um número que muda de tela para tela reprova, porque sem eles a peça não tem tese.

As falhas:

- **Afirmação sem lastro** [código + jev + modelo]: o código confere os números contra a fonte, o Jev escolhe entre sustenta, contradiz e não diz e só reprova: contradiz ou não diz com confiança de pelo menos 0,8 é a falha; sustenta, com qualquer confiança, e o que fica abaixo de 0,8 vão ao juiz (em erros reais, a força de uma afirmação mudada pode sair "sustenta" com confiança alta; o 0,8 é o do cookbook de citações da Anthropic). A falha: número, data ou atribuição que não está numa fonte da base ou na legenda. Fonte da base é o registro original em `knowledge/sources/`; a síntese de uma área ajuda a achar, mas não é lastro sozinha. Número que muda entre telas e legenda conta. Número do próprio negócio do autor vale como fonte quando dito como dele ("na minha empresa").
- **Citação que não é literal** [modelo]: frase entre aspas, com travessão e nome, ou sob rótulo de atribuição ("a resposta dele:") que não é a fala exata, com fonte; recorte literal usado fora do sentido original; frase atribuída à pessoa errada. Paráfrase vai sem aspas e sem rótulo de fala.
- **Método ou ideia de terceiro adaptado sem aviso** [modelo]: a adaptação do autor apresentada como se fosse do original. Separar "o que ele diz" de "como eu aplico"; a parte do autor conta como leitura própria. **Paráfrase de uma obra:** resumir ou recontar o livro, o método ou a fala de alguém não é falha quando o crédito está na peça ("segundo Frankl", "o método dele"); sem crédito, é esta falha, com destino corrigir (dar o crédito). A falta de perspectiva do autor do post pesa em I (conexão), não na integridade; compilação continua sendo lista com o miolo reproduzido.
- **Imagem de pessoa real sem direito de uso** [pessoa]: retrato gerado de uma pessoa real reconhecível, nomeada ou não, com um rosto que não é o dela ou com o rosto dela. Usar foto real com direito de uso, ou ilustração assumida e reconhecível; foto com filtro de ilustração conta como ilustração assumida.
- **Reconstrução fora das regras** [modelo]: na peça de fato sobre pessoas, a cena reconstruída em qualquer um de três casos: fala inventada entre aspas; ação ou momento específico (quem, onde, quando) não documentado, na voz, no texto ou no desenho; desenho de um momento específico reconstituído sem a marca "reconstituição" na tela ou sem a fonte na legenda. A falha são só esses três casos; as outras regras da reconstrução são de produção e não entram aqui: sem fonte, a voz conta em discurso indireto; o genérico da época desenhado (a sala, o objeto, a máquina) não é falha nem leva marca; a leitura do autor se assume na voz. A fala inventada entre aspas é também "citação que não é literal". Curta de ficção é outro caso.
- **Promessa não cumprida** [modelo]: o gancho, a legenda ou a chamada prometem o que o conteúdo não entrega. Com um alerta [jev] que não bloqueia: algum item de uma tela contradiz a promessa da capa? O alerta aponta a tela para o juiz olhar; pega a contradição de um item, não a troca de tese.
- **Erro de conteúdo** [modelo]: o que se ensina não funciona como dito; a peça contradiz a própria tese entre telas ou com a legenda; a ação pedida contradiz a tese; a narrativa só se sustenta omitindo um fato que a base registra.
- **Sem leitura própria** [pessoa]: repost ou compilação de terceiro sem a perspectiva do autor (paráfrase com crédito e sem perspectiva pesa em I, ver a falha de método de terceiro). Compilação reprova mesmo com gancho bom; o gancho vai para `ideas/`. Notícia com a fonte nomeada não é falha: vale I = 1 sem uma linha de leitura própria. **Onde a curadoria deixa de ser compilação:** o teste é **quem escreveu o miolo de cada item**. É curadoria quando o autor escreve o miolo com as palavras dele, numa estrutura que ele impôs à lista (o problema, o que faz, o resultado; uma frase de fecho própria por item), mesmo que os fatos venham da descrição do item; também é curadoria quando ele diz por que escolheu cada item a partir do uso dele, ou quando uma tela própria muda o jeito de usar a lista (a ordem, o critério de escolha, o que evitar). É compilação quando o miolo é reproduzido de terceiro: citações, moldes com lacunas, prints, descrições copiadas. Uma linha genérica por item ("Para quem...", "Serve para...") em volta de um miolo reproduzido não muda isso.
- **Fora dos valores** [pessoa]: escassez ou urgência falsas, exclusividade falsa para empurrar ação, promessa de resultado que depende só da compra, exposição de terceiros para vender.

## Erros de execução (bloqueiam a exportação, não reprovam)

A peça diz a coisa certa com acabamento errado. Leva a retocar: corrige-se o trecho, e a peça não fecha para publicar enquanto não corrigir.

- **Erro de texto** [código + modelo]: erro de digitação, palavra repetida, caractere solto, texto fantasma de outra versão, texto deformado em imagem gerada. Na tela ou na legenda, hashtags incluídas.
- **Referência relativa de dia** [código + jev]: "hoje", "amanhã", "ontem" e a lista da regra dos Stories (`stories/README.md`) na tela ou na legenda. O post fica no perfil e é lido em qualquer dia, e o Story atravessa a virada do dia em 24 horas: a referência relativa deixa de ser verdade para quem lê depois. Usar o dia da semana, a data ou uma referência que não depende do dia.
- **Hashtags demais** [código, `conferir_telas.py` da `visual-form`, que cancela o `--upload`]: mais de cinco hashtags na legenda. O Instagram passou a limitar a cinco por post (anúncio da conta @creators no Threads em 18/12/2025, com implantação gradual; [Social Media Today](https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/)).
- **Fora da voz** [código + pessoa]: travessão, advérbio de enchimento, termo técnico que o público da peça não conhece sem troca nem explicação no primeiro uso, tradução que muda o sentido de um termo do original. O termo técnico se troca pelo comum ou se explica no próprio texto, mesmo que ele cresça; a analogia é um dos jeitos de explicar, não o único (`knowledge/content-design/escrever-em-linguagem-simples.md`, seção 3). A série pode pedir mais na estrutura editorial dela (a analogia numa tela da receita, por exemplo). O travessão e o resto da voz seguem `context/sobre-mim.md`; se ele não proíbe o travessão, o teste de travessão sai.
- **Texto essencial em zona proibida** [código]: manchete, ponte ou chamada fora da área segura do carrossel, a de 1000 por 1270 centrada, ou no centro da base, onde podem ficar os pontinhos (no feed, nome, botões e legenda ficam abaixo da imagem: `knowledge/content-design/carrossel-instagram.md`).

## Critérios

| | Critério | 0 | 1 | 2 |
|---|---|---|---|---|
| A | **Gancho** (a capa inteira: texto e imagem) | a capa não diz de que o post trata | nomeia o tema, mas a pessoa do público não percebe por que é para ela | alguém do público entende em um segundo do que se trata e por que é para ele, fora da lista negra |
| B | **Segundo bloco** | repete a promessa ou vira bio seca | acrescenta contexto sem abrir loop | nomeia a dor ou traz analogia e abre um loop |
| C | **Contexto** | opinião sem exemplo | exemplo, sem fonte nem verdade reconhecível | dado com fonte, história verificada ou verdade universal que o público reconhece, e antecipa a objeção óbvia com resposta certa |
| D | **Cada tela necessária** | duas ou mais saem sem perda | uma sai sem perda | nenhuma sai sem perda |
| E | **Motivo para salvar** | nenhuma tela serve de referência | lista ou esquema implícito, ou referência que não dá para usar sem buscar fora ou que não serve ao público | uma tela feita para voltar, utilizável como está pelo público da peça |
| F | **Motivo para enviar** | nenhum | genérico | um destinatário reconhecível e um motivo: resolve algo dele, ele se reconhece (humor, identificação) ou é novidade que ele precisa saber |
| G | **Ideia central repetida** | aparece uma vez | duas vezes | no gancho, no meio e no fecho, em formas diferentes |
| H | **Clareza sem repertório** | a primeira tela exige do público da peça algo que ele não tem | entende-se com esforço | entende-se em uma leitura |
| I | **Conexão** | nenhuma voz do autor ou da marca | frase genérica de aproximação, ou notícia com fonte sem leitura | opinião, história ou experiência própria |
| J | **Legenda** | fala de outra coisa ou contradiz a peça | trata da peça, mas só reformula o que as telas dizem, ou é só a chamada | trata da peça e acrescenta o que as telas não dizem: abre com uma frase curta com termo buscável, **ou** amplia a peça (história, crônica, ponto de vista, complemento), com qualquer tamanho |
| K | **Chamada** | várias, ou de venda colada | uma, desalinhada do objetivo | uma, a que a peça pede |
| M | **Emoção** | nenhuma reação | interesse intelectual | identificação ou reação forte, sem exagero |
| O | **Ponte entre telas** | cada tela fecha em si, sem sinal de que há sequência | sequência implícita, ou só o contador de páginas ou a seta | cada tela puxa a próxima pelo conteúdo (pergunta, "próximo:", loop) |
| Q | **Camadas de leitura** | só bloco corrido | destaque sem explicação, ou o contrário | tópico em destaque para quem passa os olhos e explicação curta para quem lê |

As letras L, N (só em Reels, abaixo) e P não estão na tabela: a legibilidade e a cara de IA são da rubrica de design (D2 e D6).

## Testes por critério

**Lastro:** o que a plataforma mede está em `knowledge/content-design/o-que-prediz-desempenho-instagram.md`; a síntese dos métodos de mercado de cada critério não vem neste modelo, e quem usa a refaz pela `research` quando quiser. A regra que mudar depois cita a própria fonte na linha.

- **A** [jev] a capa diz de que o post trata? [jev] alguém do público (`context/publico.md`) entende em um segundo por que é para ele? Vale dizer a quem serve, dizer o que a pessoa ganha, um público implícito no tema, nos termos ou na imagem, ou uma premissa que esse público reconhece (abrir com o que ele já sabe ser verdade); "qualquer pessoa curiosa" não conta como público. (No Jev, cada caminho é uma pergunta e o público implícito no tema fica com o juiz; as frases exatas da lista negra, o código acha.) [jev] fora da lista negra? A lista negra (a validar com peças reais e métricas) tem só fórmulas vazias: "o segredo sobre", "o que ninguém te conta", ordem em tom de vendedor; lista numerada só cai quando a promessa é genérica ("5 dicas que vão mudar sua vida"), e com promessa concreta passa ("30 truques da psicologia que te deixam muito perigoso"). Cair na lista negra limita a nota a 1, não zera. Em série, a capa se sustenta sem o post anterior.
- **B** [jev] acrescenta algo à capa? [jev] nomeia uma dor ou traz analogia? [jev] termina abrindo a tela seguinte?
- **C** [modelo] há exemplo concreto, dado ou história? [modelo] há fonte citada, história verificada ou verdade reconhecível? [modelo] antecipa a objeção óbvia, com resposta correta?
- **D** [modelo] cada tela traz algo que nenhuma outra traz? [modelo] nenhuma ideia se repete em duas telas como item diferente? (as duas pedem ler todas as telas juntas; o código não as manda ao Jev)
- **E** [jev] há tela de referência (lista, comparação, passo a passo, glossário)? [modelo] dá para usar sem buscar fora (nomeia a ferramenta, o repositório, o passo)? [modelo] serve ao público da peça (não pede repertório que ele não tem sem avisar)?
- **F** [jev] a peça tem um destinatário reconhecível? [jev] há um motivo para mandar a ele (resolve, ele se reconhece, ele precisa saber)? (O destinatário perguntado à parte ao Jev tende a ficar no meio da escala: ele segue dentro dos motivos, e F fica com o juiz até a releitura de quem decide.)
- **G** [jev] a ideia central aparece no gancho? no meio? no fecho? (o Jev só responde com a ideia central da pauta no estado; sem ela, o juiz)
- **H** [jev] a primeira tela, lida inteira (texto e imagem, como em A), usa só termos e referências que o público da peça conhece?
- **I** [pessoa] há opinião, história ou experiência do autor ou da marca?
- **J** [jev] a legenda tem relação com a peça e não a contradiz? (no Jev, duas perguntas: o mesmo assunto e a contradição) [jev] ela acrescenta o que as telas não dizem (uma história, uma crônica, um ponto de vista, um complemento), em vez de só reformular as telas? [código] até 30 palavras antes da chamada, com [jev] termo buscável na primeira frase, é o outro caminho para o 2. Só o primeiro teste leva a 0. O tamanho não limita: as 30 palavras são um caminho, não um teto. Texto genérico, com cara de escrito por IA, é "Fora da voz", na execução, não J.
- **K** [jev + código] há exatamente uma chamada ("arrasta" não conta)? (o Jev responde uma pergunta por ação, inclusive o link, e o código conta) [modelo] é a que o objetivo pede? (o objetivo vem da pauta; o código dá só uma pista) [jev] não é venda colada? (no Jev, duas perguntas: vende, e o que vende é do mesmo tema) Chamada para material, curso ou captura de contato **do mesmo assunto** é alinhada; de outro assunto é venda colada. Ponte de série pede "segue", não "salva" (salvar um post não entrega o próximo). Uma chamada de ação na peça e, na legenda, no máximo uma pergunta de conversa contam como uma chamada só. Peça de reflexão ou de emoção sem chamada: K não se aplica. Peça de salvar ou de envio sem chamada: K = 0, que leva a ajustar (falta a chamada que o objetivo pede); de ação ou de venda, K = 0 por falta reprova.
- **M** [modelo] há identificação ou reação nomeável?
- **O** [jev] cada tela, menos a última, termina puxando a próxima? [código] há contador de páginas ou seta (na peça de terceiro, [jev] na imagem da capa)? Contador e seta mostram que há sequência, mas não puxam a próxima: tiram O do 0 e não levam a 2. Na série, o contador pode ficar na moldura do pé e continua contando; o selo "1/8" que o app desenha sobre a capa não conta, porque não é da peça.
- **Q** [código, quando houver; até lá, o juiz] cada item tem título em destaque e uma ou duas linhas de explicação? (o destaque e as linhas saem do DOM, que a transcrição do Jev não guarda)

## Variantes

- **Tela única:** B, D, G e O não se aplicam (G pede gancho, meio e fecho); a soma usa só os critérios aplicáveis.
- **Quadrinho, diálogo e meme:** O e Q não se aplicam.
- **Notícia:** em A, o 2 é nomear o fato e por que ele importa para esse público.
- **Reels:** A vale para os três primeiros segundos, com texto, imagem, som e efeitos visuais; D por plano ou por estação: cada plano, ou cada estação quando o vídeo é um plano só com a câmera viajando, é necessário; Q não se aplica; e entra **N, ritmo**, em que conta como ritmo toda troca de imagem (corte, voo de câmera, aproximação, elemento que entra), não só o corte: 0 imagem parada ou trocas frenéticas sem motivo; 1 trocas regulares; 2 acelera o óbvio e desacelera o que pede reflexão, também pela velocidade da câmera e pelo tempo de parada. As áreas seguras do carrossel, que definem a zona proibida, estão em `knowledge/content-design/carrossel-instagram.md`.

## Como o portão fecha

O veredito é o mais pesado que se aplica, contando esta rubrica e a de design, na ordem da tabela (reprovada pesa mais que ajustar, que pesa mais que retocar). Quando ajustar e retocar se aplicam juntos, vale ajustar, e a passada seguinte confere a integridade. São quatro vereditos, definidos pelo que acontece depois, como na revisão por pares (aceitar, revisão menor, revisão maior, rejeitar):

| Veredito | Quando | O que acontece |
|---|---|---|
| **Reprovada** | falha de integridade com destino "reprova", ou nota 0 em A, C ou H; K = 0 por **falta** de chamada quando o objetivo é uma ação. K = 0 por várias chamadas ou por venda colada é "retocar": tira-se a chamada a mais, e na soma e no "nota 0" de ajustar o K entra com a nota que terá depois do retoque, declarada por quem avalia | volta para a pauta |
| **Ajustar** | nota 0 em algum critério, soma abaixo do limiar, ou E e F abaixo de 2; na de design, nota 0 em algum critério ou apontamento P1. E e F são alternativas: E = 0 não leva a ajustar quando F = 2, nem F = 0 quando E = 2 | reescreve as telas apontadas e passa de novo pela etapa do portão que elas tocam; a peça é boa e pede ajustes de conteúdo ou de forma, não recomeço. É a "revisão maior" da revisão por pares |
| **Retocar** | falha de integridade com destino "corrigir", erro de execução ou apontamento de design P2 | corrige o trecho apontado e exporta: quem orquestra confere só o trecho (a integridade, contra a fonte), sem nova passada completa. É a "revisão menor" da revisão por pares |
| **Pronta** | nenhum dos casos acima: nenhum 0 (fora a exceção de E e F), soma de pelo menos 78% do máximo aplicável (22 de 28 no carrossel), nota 2 em E ou F para qualquer tipo de peça, e a de design sem P1 nem P2. Apontamento P3 sozinho não muda o veredito: corrige-se antes de exportar, sem nova avaliação | exporta |

## As decisões da régua

1. **A falta de chamada não reprova por si.** Quando o objetivo declarado é uma ação, a chamada é obrigatória e K = 0 reprova; peça de reflexão ou de emoção pode fechar sem chamada, mesmo sem a legenda convidar, e aí K não se aplica.
2. **Encaixe com o público fica fora da nota.** "Não sou o público" não é "é ruim": o encaixe é um campo à parte na calibração.
3. **Compilação de terceiro reprova, mesmo com gancho bom.**
4. **Chamada do mesmo assunto é alinhada:** material, curso ou captura de contato sobre o tema da peça; de outro assunto é venda colada.
5. **E ou F = 2 vale para todo tipo de peça; F conta humor, identificação e novidade como motivo de envio.** Porque salvar e enviar são os sinais que a plataforma mais pesa (`knowledge/content-design/o-que-prediz-desempenho-instagram.md`), e as peças que os têm tendem a render muito acima da mediana do perfil.
6. **Quatro vereditos, e a forma em rubrica própria.** Há casos que só pedem um refino ou uma correção pontual, sem voltar ao começo; e uma rubrica só da mensagem deixa passar o problema de forma.
7. **A rubrica fica congelada em uso.** Versão nova só abre quando uma falha de integridade escapa do portão numa peça da conta, quando as métricas de uns 10 posts mostram que a soma não acompanha envios e salvamentos (contados depois dos primeiros posts de uma conta que volta de pausa, que servem de linha de base, porque o mesmo post rende diferente numa conta aquecida), quando uma ambiguidade muda o veredito de uma peça real, quando uma releitura de quem decide com os testes à vista mostra que a régua escrita não descreve a leitura dela, ou quando quem decide muda a régua. Revisão de execução, que muda quem confere o quê sem mudar nota nem veredito, não espera esses gatilhos. Quando houver um conjunto âncora (peças julgadas por quem decide, guardadas para comparar), ele não é alvo de ajuste: é teste de regressão, rodado a cada versão do modelo ou da rubrica.
8. **A gravidade da mesa nas regras novas.** A regra nova que vem das marcas de quem decide numa mesa entra com a gravidade da mesa traduzida na severidade do portão: bloqueia = crítica, corrige = maior, aviso = menor (`portao-de-qualidade.md`, "Severidade das correções"; `knowledge/agent-engineering/gravidade-por-regra-ou-por-julgamento.md`). Onde cada uma entra (erro de execução, critério, falha de conteúdo) se decide ao escrevê-la, com a fonte.

## Onde entra no fluxo

Depois da revisão de rascunho e antes da skill `slides-export`. A divisão de trabalho esperada: **o modelo é bom em achar falha de integridade e erro de execução, e quem decide o conteúdo é o melhor preditor da nota de qualidade.** O juiz do portão (`portao-de-qualidade.md`) aponta; quem decide dá a nota e o veredito. Os testes [código] rodam num script (os que ainda não têm código ficam com o juiz); os [jev] ficam com o juiz até as duas condições de "Quem avalia", ou de vez quando o Jev não está configurado; os [modelo] vão ao juiz, e os [pessoa] ficam com quem decide.

## Hipóteses a testar (não são critérios)

Entram como variável de teste, uma por vez, medidas em envios e salvamentos por alcance, salvo onde a linha diz outro teste:

- Peso maior para E, F, M e O, que tendem a acompanhar o desempenho; A, C, D, G, H e Q, menos.
- Clímax no penúltimo slide, chamada no último; fechar com reflexão em vez de chamada rende mais comentário.
- Pausa de um segundo depois de uma afirmação que pede reflexão; som marcando a afirmação central (Reels).
- Número de slides, tamanho da manchete da capa, tamanho da legenda, horário; "posts com 4 ou 5 telas repassam mais".
- Texto denso funciona quando a voz é forte e a estrutura de cada tela é fixa.
- Tela 2 que se entende sem a capa: o Instagram "often" reapresenta o carrossel ignorado abrindo na segunda mídia (*Carousels often get more reach than single photo posts for two main reasons*, de Adam Mosseri, Reel de 16/10/2024, https://www.instagram.com/mosseri/reel/DBOeUmTSmIC/). Vale na produção, sem entrar na nota de B até as métricas dizerem se rende.
- Reels: a virada, há pelo menos uma, por ação ou revelação, que muda a direção; o fecho que paga o gancho; a voz que soma à tela, sem anunciar nem repetir o que está escrito.
- **A conferência da voz contra a imagem** (em toda peça narrada: Reel, Story em vídeo, cena; a tipologia S, F, A, C, R da `piece-script`, na coluna da tela do vídeo): [modelo] cada frase da voz se classifica pelo que faz com a imagem que está na tela enquanto ela soa (S soma, F fio, A antecipa, C contraponto, R repete; as definições estão na síntese) e responde "o que a tela mostra que esta frase não diz?". O sinal de falha é R fora de rótulo curto dentro de uma estrutura (contagem, nome, data), ou cena sem nenhum S. Até as métricas dizerem se rende, o sinal vai como apontamento a quem decide, sem entrar na nota nem no veredito; virar critério segue os gatilhos da decisão 7. A classificação da síntese é de um leitor só: o teste mede a direção, não a contagem exata.

## Versões

A versão nova registra aqui, numa linha, o que mudou e por quê.

- **1.0:** a primeira versão do repositório.
