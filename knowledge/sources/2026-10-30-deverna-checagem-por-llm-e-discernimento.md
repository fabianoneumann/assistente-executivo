---
titulo: "Fact-checking information from large language models can decrease headline discernment"
tipo: paper
autor: "Matthew R. DeVerna, Harry Yaojun Yan, Kai-Cheng Yang, Filippo Menczer"
url: "https://arxiv.org/abs/2308.10800"
publicado_em: 2023-08-21
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv, para o preprint; a versão publicada na PNAS tem CC BY-NC-ND 4.0, segundo os metadados da Crossref)"
areas: [agent-engineering]
tags: [fact-checking, human-in-the-loop, automation-bias, uncertainty-expression, misinformation, selection-bias, trust-calibration, human-ai-interaction]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv 2308.10800 (cs.HC): v1 em 21/08/2023, v2 em 01/09/2023, v3 em 26/12/2023 e v4 em 07/08/2024, a mais recente (lida; o PDF é datado de 09/08/2024 e tem 65 páginas, com a Informação Suplementar). **A v4 não é a versão publicada:** a capa diz "This preprint is under review at PNAS". A versão publicada saiu na PNAS 121(50): e2322823121 (DOI 10.1073/pnas.2322823121), on-line em 04/12/2024 e no número de 10/12/2024, recebida em 12/01/2024 e aceita em 04/11/2024, segundo os metadados da Crossref; a página do arXiv traz essa referência e o DOI. A versão publicada não foi aberta. Observatory on Social Media (Universidade de Indiana), com coautores em Stanford e Northeastern. O integral é o da v4, extraído do PDF; as Figuras 1 a 3 e as Tabelas S37 e S38 foram lidas como imagem; a seção 8 da Informação Suplementar (as 40 manchetes com as duas checagens de cada uma) foi percorrida pelos rótulos e datas. Lida (camadas flexíveis de avaliação).

## A pergunta

Checagem de fatos reduz a crença em desinformação e a intenção de compartilhá-la, mas não escala. LLMs se saem bem em tarefas de checagem, e ChatGPT já foi testado avaliando a credibilidade de veículos e checando alegações. Falta saber como as pessoas interagem com a checagem feita por um LLM. Os autores medem, num experimento controlado e randomizado com pré-registro, o efeito causal de ver a checagem do ChatGPT (GPT-3.5) sobre a crença em manchetes políticas e a intenção de compartilhá-las. Escolheram o ChatGPT, embora não seja feito para checagem, por ser amplamente disponível e usado e pelos bons resultados de checagem relatados na época.

## Desenho

- **Amostra:** 2.159 participantes dos EUA, com cotas da Qualtrics para gênero, idade, raça, escolaridade e partido (Censo de 2020 e Pew, com margem de ±5%).
- **Estímulos:** as mesmas 40 notícias políticas reais para todos, cada uma com manchete, linha fina (quando havia) e imagem, no formato de post de rede social. Metade verdadeira, metade falsa; metade favorável aos democratas, metade aos republicanos. Foram escolhidas de 317 por um pré-teste que equilibrou partidarismo percebido, impacto, familiaridade, sensacionalismo e probabilidade de ser compartilhada e acreditada (vêm de outro estudo, ref. 79). As falsas saíram do Snopes; as verdadeiras, de veículos tradicionais (New York Times, Washington Post, Fox News, Wall Street Journal), de época aproximada.
- **Dois grupos:** "crença" (você acredita que a alegação da manchete é verdadeira?) e "compartilhamento" (você consideraria compartilhar esta notícia on-line?), com resposta sim ou não. Perguntas separadas porque pensar na veracidade altera o compartilhamento.
- **Quatro condições em cada grupo:** controle, só a manchete; checagem humana, tradicional; **LLM obrigatório**, a checagem do ChatGPT aparece abaixo da manchete; **LLM opcional**, a pessoa clica num botão ("Você gostaria que o ChatGPT ajudasse a verificar a manchete?") para ver. Quem estava nas condições de LLM sabia que a checagem vinha do ChatGPT; quem estava na checagem humana só soube que receberia informação de checagem. O texto do ChatGPT era o mesmo para todos.
- **Participantes por condição:** crença: controle 241, opcional 261, obrigatório 247, humana 300. Compartilhamento: 267, 263, 269 e 311.
- **A checagem do LLM:** num chat novo do site público, em 25/01/2023, o prompt "I saw something today that claimed <MANCHETE>. Do you think that this is likely to be true?", com a linha fina depois de dois pontos e sem a fonte; uma vez por manchete, com captura de tela. O modelo era uma versão do GPT-3.5 que não existe mais. Os três primeiros autores rotularam cada resposta como "verdadeira", "incerta" ou "falsa", por maioria (alfa de Krippendorff de 0,79).
- **A checagem humana:** começa com "The above claim is True/False", fala da reputação do veículo (confiável se a manchete é verdadeira, não confiável se falsa) e dá detalhes breves. As das falsas vieram do estudo de origem; as das verdadeiras foram escritas por um dos autores.
- **Coleta:** controle e condições de LLM em março de 2023; as condições de checagem humana, de março a junho de 2024, a pedido dos revisores, com o mesmo protocolo.
- **Estatística:** salvo aviso, teste U de Mann-Whitney bicaudal com correção de Bonferroni; na Informação Suplementar, regressões lineares com erro-padrão agrupado por participante e por manchete.
- **Discernimento**, a medida principal: proporção de manchetes verdadeiras acreditadas (ou compartilháveis) menos a proporção de falsas. Uma intervenção eficaz contra desinformação deve aumentá-lo.

## Resultados

### Precisão da checagem do LLM (Figura 1b)

- **Manchetes verdadeiras:** o ChatGPT acertou 15% (3 de 20), chamou de falsas 20% (4 de 20) e ficou incerto em 65% (13 de 20), com respostas do tipo "é possível que... mas não tenho informação se isso aconteceu".
- **Manchetes falsas:** acertou 90% (18 de 20) e ficou incerto em 10% (2 de 20). Nenhuma falsa foi chamada de verdadeira.

Os autores leem isso como um checador preciso para conteúdo falso e menos preciso para o verdadeiro, mas que em geral diz quando não consegue checar, o que bate com estudos maiores. Forçar o modelo a responder só "verdadeiro" ou "falso" não melhorou a precisão geral (seção 6 da Informação Suplementar, abaixo).

### A checagem do LLM não mudou o discernimento (Figura 1c e 1d)

Contra a expectativa pré-registrada, o discernimento não mudou com a checagem do LLM em nenhuma das duas condições:

- **Crença, LLM obrigatório:** −4,50% (U = 31.993, P = 0,61, d = −0,15, IC 95% de −10,04% a 0,90%).
- **Crença, LLM opcional:** −0,27% (P = 1, d = −0,01).
- **Compartilhamento:** −0,43% no obrigatório e −0,67% no opcional (P = 1 nos dois).
- **Checagem humana:** aumentou o discernimento de crença em 18,06% (U = 25.210, P < 0,001, d = 0,50, IC de 12,00% a 24,00%) e o de compartilhamento em 8,98% (P = 0,001, d = 0,35), sobretudo por aumentar a crença e o compartilhamento das verdadeiras (+15,63% e +9,58%), com pouca mudança nas falsas.
- **Discernimento médio anotado na figura:** crença 39% no controle, 35% no obrigatório, 39% no opcional e 57% na checagem humana; compartilhamento 8%, 8%, 8% e 17%.

Para os autores, o resultado é inesperado, porque a IA dá informação útil, sobretudo nas falsas. Essa análise não separa os acertos do modelo nem quem escolhe ver; por isso acrescentam duas análises exploratórias, fora do pré-registro.

### Separando pelo que o LLM disse (Figura 2; obrigatório contra controle)

Cada manchete cai num de cinco cenários (verdadeira ou falsa × julgada verdadeira, falsa ou incerta; não há falsa julgada verdadeira).

- **Crença, efeitos indesejáveis:** −12,75% na crença em manchetes verdadeiras que o ChatGPT chamou de falsas (U = 35.937, P < 0,001, d = −0,38, IC de −18,67% a −6,89%), e +9,12% na crença em manchetes falsas sobre as quais ele ficou incerto (P = 0,03, d = 0,22, IC de 1,69% a 16,35%).
- **Compartilhamento, misto:** +11,09% na intenção de compartilhar verdadeiras que ele acertou (P = 0,02, d = 0,26), o que aumenta o discernimento, e +9,77% no compartilhamento de falsas sobre as quais ficou incerto (P = 0,05, d = 0,22), que o reduz em medida parecida.

Os autores dizem que a maioria dos efeitos é pequena, mas alguns são danosos no sentido de reduzir o discernimento.

### Quem escolhe ver contra quem não escolhe (Figura 3; condição opcional)

**Quanto se pede a checagem:** em média, pouco mais da metade das manchetes, 21,6 (DP 15,8) no grupo de crença e 23,8 (DP 15,7) no de compartilhamento. A distribuição é bimodal: 52,1% dos participantes viram a checagem de mais da metade das 40 manchetes (média de 36,7, DP 5,5); os demais viram em média 7,5 (DP 6,4). Não houve diferença significativa no pedido entre verdadeiras e falsas (P = 0,1).

**Crença, quem viu contra quem não viu** (médias ponderadas pelo número de vezes que cada pessoa escolheu ver ou não ver):

- Falsas que o modelo acertou: +29,35% (P = 0,005, d = 0,63).
- Falsas em que ficou incerto: +28,12% (P < 0,001, d = 0,64).
- Verdadeiras em que ficou incerto: +5,51%, não significativo (P = 1).
- Verdadeiras que acertou: +7,46% (P = 0,04, d = 0,18, IC de −1,50% a 16,35%).
- Verdadeiras que chamou de falsas: −16,59% (P < 0,001, d = −0,35).

**Compartilhamento:** quem viu compartilha mais em todos os cenários, de +29% (verdadeiras chamadas de falsas) a +39% (verdadeiras acertadas); na Tabela S37, 39,46%, 29,39%, 34,24% (verdadeiras incertas), 37,63% (falsas acertadas) e 37,39% (falsas incertas), todos com P < 0,001.

**Ressalva dos autores:** esta comparação não identifica efeito causal, porque a pessoa escolhe, manchete a manchete, se vê ou não.

### Atitude em relação à IA e congruência partidária

**Atitude em relação à IA:** quatro itens adaptados de Sindermann et al. (medo, confiança, "vai destruir", "vai beneficiar" a humanidade), em escala de 7 pontos, com média por participante. Nas duas primeiras análises, a atitude e a congruência partidária da manchete quase não mudaram os resultados.

Na condição opcional:

- Quem tinha atitude mais positiva e viu a checagem compartilhou mais em todos os cenários (b médio = 0,044); na crença, a relação foi menos clara.
- Entre quem não viu a checagem, atitude mais positiva veio com menos crença em verdadeiras não identificadas como tal (verdadeira julgada falsa: b = −0,040, P = 0,014; verdadeira incerta: b = −0,033, P < 0,001).
- Com checagem incerta sobre manchete verdadeira, atitude mais positiva veio com mais crença e mais compartilhamento (b = 0,032 e 0,044).

**Congruência partidária:**

- Diante de verdadeiras de lado político oposto em que o LLM ficou incerto, a crença e o compartilhamento caíram com significância, quer a pessoa tenha visto a checagem ou não (crença: b = −0,086 entre quem viu e −0,097 entre quem não viu; compartilhamento: −0,038, P = 0,050, e −0,088).
- Relação parecida só apareceu nas falsas de lado oposto, entre quem não viu a checagem (falsa acertada: b = −0,057; falsa incerta: b = −0,195).
- Na condição obrigatória, quem viu checagem incerta sobre verdadeira de lado oposto se dispôs a compartilhar mais que o controle (P ajustado = 0,010), embora em cada grupo as de lado oposto fossem menos compartilhadas (controle b = −0,10; obrigatório b = −0,03).

## Discussão

**Ressalvas de generalização dos autores:**

- Uma versão específica do ChatGPT e um único prompt; o realismo do prompt é incerto, porque não há pesquisa sobre como as pessoas usam LLMs para checar no mundo real.
- Escolhas para imitar a rede social (fonte, linha fina) podem pesar na avaliação, embora de forma igual em todas as condições.
- O ambiente de questionário pode não capturar o consumo real de informação, mas a intenção declarada de compartilhar se correlaciona com o compartilhamento real (ref. 54).
- O conjunto de notícias políticas é pequeno, embora equilibrado pelo pré-teste.

**Por que o modelo acerta mais as falsas:** com poucas manchetes, é difícil saber. Uma possibilidade que os autores levantam é que as falsas eram mais antigas e o modelo pode tê-las visto no treino. Daí o que chamam de **"problema da notícia de última hora"**: notícias em desenvolvimento tratam de eventos que o modelo nunca viu. Direção futura: aumentar o LLM com dados confiáveis, como busca em tempo real.

**Efeito médio nulo, efeitos condicionais:** o resultado surpreende diante de pesquisas que mostram LLMs persuadindo pessoas em temas controversos. Mas a checagem do LLM afeta crença e compartilhamento conforme o acerto da resposta em relação à veracidade. As pessoas acreditaram menos em verdadeiras rotuladas erradamente como falsas, o que é coerente com a literatura de que a IA é percebida como objetiva. O aumento no compartilhamento de verdadeiras corretamente identificadas é animador, e, como o conteúdo confiável é muito mais abundante que a desinformação, os autores pedem estudo de como o volume de cada tipo de conteúdo interage com a precisão do modelo.

**A incerteza:** quando o LLM ficou incerto sobre manchetes falsas, as pessoas ficaram mais inclinadas a acreditar e compartilhar. Isso contradiz pesquisas segundo as quais checagens incertas podem ser lidas como "falso" e expressões de incerteza de um LLM podem aumentar a acurácia na tarefa. Expressar incerteza é tido como qualidade desejável em checagem automática; aqui levou a resultados adversos. Questão aberta: quais formatos e estilos de checagem por IA funcionam melhor, e que técnicas de prompt os produzem de forma confiável.

**Viés de seleção na condição opcional:** os autores falam em viés de seleção forte. Para eles, os resultados sugerem que as pessoas já tinham opinião formada antes de abrir a checagem, talvez para confirmar o que acreditavam ou para ver se a IA errava. Muitos fatores influem, como quão informada e quão confiante a pessoa está. Parte dos participantes desconsidera a checagem, sobretudo nas falsas, em que o ChatGPT é muito preciso. Atitude em relação à IA e congruência partidária se relacionam com esse comportamento. O desenho não revela o mecanismo, mas os autores concluem que este formato de intervenção dificilmente ajuda.

**Trabalho futuro:** testar o efeito de dizer se a checagem vem de humano ou de IA. Em conversa genérica, prevenção em saúde, publicidade e texto escrito, revelar a origem em IA tende a piorar a percepção do conteúdo.

**Contexto:** especialistas temem que a IA agrave a desinformação: robôs maliciosos com IA são quase indetectáveis, os próprios desenvolvedores do ChatGPT preveem uso malicioso, e LLMs persuadem em temas polarizados e produzem propaganda persuasiva. Para os autores, as dinâmicas da interação humano-IA tornam a checagem por LLM "potencialmente danosa, apesar da sua precisão", o que não deve desencorajar a pesquisa, e sim exigir entender riscos e oportunidades.

## Informação Suplementar

### Amostra e atrito

**Composição da amostra:** 53,40% mulheres; 51,92% sem diploma universitário; 50,72% democratas ou inclinados, 43,68% republicanos ou inclinados e 5,60% independentes.

**Tamanho:** o plano pré-registrado buscava poder de 0,95 para detectar efeito pequeno de 0,1 a 0,05; o G*Power indicou mínimo de 44 por condição, mas o alvo foi 250 por condição. As condições de checagem humana tiveram 300 por condição por causa do gasto mínimo exigido pela Qualtrics.

**Desistência:** de 1% a 6% por condição.

**Verificação de atenção:** uma manchete inventada dizendo que o céu é amarelo, anunciada antes; quem não respondeu "sim" foi excluído. As taxas de falha ficaram entre 50,27% e 67,32% (Tabela S1); no grupo de compartilhamento com LLM obrigatório o dado se perdeu por erro da Qualtrics.

**Diferença de atrito:** houve diferença significativa entre controle e checagem humana no grupo de compartilhamento (P < 0,001), que os autores atribuem talvez ao recrutamento em épocas diferentes.

**Excluídos antes da alocação:** 551 não consentiram, 58 menores de 18 anos, 37 fora dos EUA e 86 não se comprometeram a dar as melhores respostas.

**Desequilíbrio:** no grupo de crença, a condição de checagem humana tinha mais diplomados que a opcional; os autores não comparam essas duas e as regressões controlam por escolaridade.

### Regressões

O pré-registro previa um modelo multinível logístico, mas ele teve problemas de convergência e não permitia separar verdadeiras e falsas. Os autores trocaram por regressão linear com erro-padrão agrupado, um desvio do pré-registro alinhado à literatura, com idade (em décadas) e escolaridade como covariáveis.

- **Discernimento (Tabelas S3 e S4):** a interação condição × veracidade não é significativa para o LLM obrigatório nem para o opcional, e é significativa para a checagem humana (0,181 na crença e 0,090 no compartilhamento, P < 0,001).
- **Cenários (Tabelas S7 e S8):** as comparações pós-hoc confirmam os efeitos do texto principal e mostram ainda efeitos danosos em outros cenários: na crença, falsas acertadas (+0,029, P ajustado = 0,014); no compartilhamento, falsas acertadas (+0,047), falsas incertas (+0,078) e verdadeiras incertas (+0,045). Para ficar conservadores, os autores não os relatam no texto principal, porque não batem com a análise das diferenças de médias brutas.
- **Opcional (Tabelas S11 e S12):** as regressões confirmam as comparações do texto principal.

### Outros jeitos de perguntar ao modelo (seção 6, Tabela S38)

Em 2024, os autores testaram o mesmo GPT-3.5 de outras formas. A acurácia e o F1 são para identificar manchetes falsas, sem contar as respostas incertas.

| Abordagem | Incertas | Acurácia | F1 |
|---|---|---|---|
| Prompt original pelo site, 2023 (o usado no experimento) | 37,5% | 0,84 | 0,90 |
| Prompt original pela API, 2024 | 77,5% | 1,00 | 1,00 |
| Binário forçado ("True" ou "False") | 0% | 0,63 | 0,71 |
| Binário forçado com justificativa | 0% | 0,65 | 0,72 |

- **Pela API**, o modelo ficou incerto em 19 das 20 verdadeiras e 12 das 20 falsas.
- **No binário**, chamou de falsas 13 (sem justificativa) e 12 (com justificativa) das 20 verdadeiras, e de verdadeiras 2 das 20 falsas.
- **Conclusão dos autores:** forçar respostas convencionais, reduzindo a incerteza, leva a mais erros, então os riscos apontados podem não se resolver com engenharia de prompt. A avaliação robusta da precisão exigiria muito mais casos, e a contribuição do estudo não é medir o modelo, e sim a resposta das pessoas à informação, situada pela precisão dele.

### Questionário e estímulos (seções 7 e 8)

**O questionário** traz, entre outras coisas:

- uso de redes e fontes de notícia;
- partidarismo;
- a bateria de atitude em relação à IA, repetida depois dos estímulos nas condições de LLM;
- frequência de uso de sites de checagem;
- uma apresentação do ChatGPT dizendo que ele "não é perfeito e pode nem sempre dar informação precisa";
- uso prévio de ferramentas de IA;
- a pergunta "você pesquisou na internet sobre as manchetes?";
- termômetros de polarização afetiva.

**As instruções da condição opcional** diziam: "Se estiver em dúvida, você pode pedir ajuda a um checador ChatGPT."

**A seção 8** lista as 40 manchetes com data de publicação, fonte, inclinação, veracidade, a checagem do ChatGPT com o rótulo dos codificadores e a checagem humana. As verdadeiras são de agosto e setembro de 2022; as falsas com data vão de 2019 a 2022.

---
