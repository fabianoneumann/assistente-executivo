---
titulo: "The Test Oracle Problem in Synthetic LLM-as-Judge Corpora: Disappearance, Distortion and a Validation Protocol"
tipo: paper
autor: "Serkan Ballı"
url: "https://arxiv.org/abs/2607.13707"
publicado_em: 2026-07-15
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [synthetic-data, llm-as-judge, test-oracle, metamorphic-testing, stimulus-integrity, generation-fault, manual-reading, perturbation-corpus, multilingual-evaluation, validation-protocol]
licenca: "licença não exclusiva do arXiv, em arxiv.org/abs/2607.13707; protegida, então entra só a ficha, e o integral está na url"
---

# Ballı 2026 (arXiv, cs.CL): um efeito fabricado pela geração do corpus e o problema do oráculo

Ficha em palavras próprias (licença não exclusiva do arXiv: o integral não entra; está na url). Preprint de um autor, Serkan Ballı, do Departamento de Engenharia de Software da Mehmet Akif Ersoy University (Turquia), versão 1 de 15/7/2026. Área: avaliação com LLM (modelo de linguagem grande) como juiz, em mais de uma língua. Log de chamadas e scripts no OSF (10.17605/OSF.IO/RS2B8). Relata o caso do próprio pipeline do autor.

## A tese

Estudos de viés de juiz LLM costumam montar um corpus sintético em que cada item tem uma resposta correta e uma alucinada, esta geralmente escrita por outro LLM, e tratam essa geração como infraestrutura. O artigo relata um caso em que a geração falhou em silêncio e fabricou um efeito grande, e argumenta que a falha é estrutural: as checagens usuais olham o comportamento agregado do juiz, a jusante, e nenhuma olha o item. O vocabulário vem de engenharia de software: o **problema do oráculo de teste** (Barr e outros, 2015), a questão de existir ou não um procedimento barato e mecânico para decidir se uma saída está certa, e o **teste metamórfico** (Chen e outros, 1998), que verifica uma relação entre entrada e saída em vez de correção absoluta.

## Método

- **Juízes:** DeepSeek-V4-Flash (API oficial), gemini-3.5-flash (com o rastro de raciocínio desligado) e glm-5.2 (GLM). Três famílias, para evitar confusão por família. DeepSeek e Gemini também produzem itens.
- **Itens em turco:** gerados. De cada contexto do wiki40b em turco (primeiras 80 palavras, mais de 60 caracteres), um LLM produtor escreve uma resposta fiel e uma contraditória. A pergunta padrão é aberta, sobre o texto.
- **Itens em inglês:** HaluEval, divisão qa, sem regenerar.
- **Pipeline corrompido:** geração e julgamento compartilham uma função e um limite de `max_tokens` de 5, que basta para o "A" ou "B" do juiz e trunca a geração. O caminho do Gemini é separado e não tem limite explícito (padrão de cerca de 4.000 tokens). O prompt de geração não proíbe abertura conversacional.
- **Pipeline corrigido:** 300 tokens para gerar e 5 para julgar, prompt que proíbe abertura conversacional, cache separado. Mesmos contextos de origem nos dois, o que é o A/B central do artigo.
- **Quatro medidas por juiz:** **estilo**, fração das vezes em que escolhe a resposta com marcador Markdown (- X) contra a mesma resposta sem ele, sempre com A primeiro; **posição**, diferença na escolha da resposta factual entre as duas ordens; **seleção**, taxa com que duas chamadas, rotuladas A/B e 1/2, concordam; **acurácia factual**, taxa com que escolhe a resposta factual. Concordância entre juízes por κ de Fleiss. Maioria dos três juízes como checagem incidental.
- **Duas análises offline:** auditoria de contaminação, que classifica cada alucinação como cópia da resposta factual, abertura conversacional truncada, fragmento curto de até 3 palavras ou válida; e estratificação do estilo por comprimento da resposta factual.
- **Tudo é reproduzível** a partir de um log de cerca de 17.800 chamadas.

## Como o efeito falso foi ficando convincente

1. **Sinal:** em N=500 itens em turco produzidos pelo DeepSeek, o GLM teve acurácia de seleção de cerca de 0,64 (IC 95% de 0,60 a 0,68), contra 0,96 no HaluEval em inglês: uma diferença de 32 pontos. Gemini 0,99 e DeepSeek 0,85 nos mesmos itens. κ de Fleiss = 0,041.
2. **Replicação:** o padrão já aparecera em N=50 (0,54, IC largo), e N=500 estreitou o intervalo sem mudar a direção.
3. **Mecanismo em três camadas:** tokenização (o GLM fragmenta menos, o que contraria a explicação por tokenizador); relatórios técnicos (o GLM-4 com treino dominado por chinês e inglês; o GLM-5 sem avaliação multilíngue), lidos como pouca exposição; comparação de sobreposição lexical nas chamadas certas e erradas (0,19 e 0,18, sem diferença) e de comprimento (cerca de 2 palavras no DeepSeek contra cerca de 45 no Gemini), relida como item de pouca informação penalizando o juiz de menor margem de competência.
4. **Experimento controlado:** trocar o produtor, em conjunto de N=200: GLM 0,61 com DeepSeek e 1,00 com Gemini. O autor chegou a tratar como interação produtor-juiz, a contribuição central.

Nada disso era real. A leitura manual dos itens do DeepSeek mostrou 81,0% começando com abertura conversacional truncada ("Tabii ki, iş..."), 12,2% com a alucinação igual à resposta factual e 6,8% com outros fragmentos, sem nenhuma alucinação bem formada na amostra. Nos 12,2%, a tarefa era impossível por construção. A causa foi o limite compartilhado de tokens, com o caminho do Gemini ileso.

**Tabela 1, corrompido e corrigido (Turco, produzido pelo DeepSeek):**

| Quantidade | Corrompido | Corrigido |
|---|---|---|
| Validade da geração | 0,0% | 98,8% |
| Comprimento médio da alucinação (palavras) | 2,1 | 20,0 |
| Contaminação, abertura conversacional | 81,0% | sem nova medida |
| Contaminação, repetição literal | 12,2% | sem nova medida |
| Contaminação, fragmento curto | 6,8% | sem nova medida |
| Acurácia de seleção do GLM (N) | 0,61 (N=200) | 1,00 (N=80) |
| Acurácia factual do GLM | 0,845 | 0,99 |
| Acurácia factual do DeepSeek nos próprios itens | 0,88 | 1,00 |
| Acurácia factual da maioria dos três | 0,962 | 1,00 |

Itens do Gemini ficam em 46,9 palavras nas duas versões. Nenhum efeito entre línguas, de produtor ou de si mesmo sobreviveu.

**O rótulo do 0,64:** o método define seleção como concordância entre as chamadas A/B e 1/2, e a seção 4.1 usa "selection accuracy" para o número; a seção 4.2 chama o 0,642 do GLM de acurácia factual, enquanto a Tabela 1 dá 0,845 factual. O artigo não reconcilia esses nomes.

## Dois modos de corrupção

- **Desaparecimento:** a queda de seleção foi fabricada por inteiro e não tem resíduo.
- **Distorção:** a preferência de estilo existe, mas muda com o comprimento do texto em que foi medida.

**Tabela 2, fração que escolhe a versão Markdown, por comprimento da resposta factual:**

| Juiz | Respostas de 1 a 2 palavras | 16 palavras ou mais | Ao alongar |
|---|---|---|---|
| DeepSeek | 0,24 (inglês), 0,43 (turco) | 0,81 (turco) | sobe e cruza 0,5 |
| Gemini | 0,00 (inglês), 0,02 (turco) | 0,00 (turco) | fica perto de 0 |
| GLM | 0,90 (inglês), 0,89 (turco) | 0,65 (turco) | cai, acima de 0,5 |

Testes de duas proporções: DeepSeek z de cerca de 8,7; GLM z de cerca de 7,0. Conjuntos usados: turco corrompido (média 2,1 palavras), turco do Gemini (média 43), HaluEval (média 2,2). Notas gerais no HaluEval: DeepSeek 0,27, Gemini 0,00, GLM 0,88.

Consequências que o autor tira: turco e inglês pareciam iguais em estilo porque os dois conjuntos tinham respostas curtas, e a invariância era de comprimento. E "no measured bias can be safely partitioned into "real" and "spurious" from aggregate metrics alone", porque a partição depende de propriedade do estímulo que a métrica não mostra.

## A assimetria do oráculo

- **Perturbação mecânica:** cada negativo deriva da resposta certa por uma transformação determinística (troca de entidade, número, negação; cita o BabelJudge, 2026). A relação entre certo e negativo se verifica por comparação de texto, a custo O(1) por item, sem juízo semântico. Falha no script aparece quando o negativo fica igual ao certo.
- **Negativo gerado por LLM:** amostrado de uma distribuição, sem relação para inverter. Um item degenerado é igual na superfície a um apenas curto, e distinguir exige ler.

**Controle positivo:** 50 frases em turco com numerais, do mesmo fluxo; a perturbação troca o primeiro numeral; a falha injetada, por sorteio independente de 30% com semente 42, pula a troca sem avisar. Saíram 20 itens sem troca (40%, cerca de 1,5 desvio acima dos 15 esperados, que ele atribui a flutuação). A comparação entre certo e negativo acertou 50 em 50, sem chamada de API e sem leitura humana.

**O que afirma e o que não afirma:** a auditabilidade do item é propriedade do desenho. A perturbação tem seus próprios custos, em outro eixo: pode ser pouco natural, cobre só os tipos de perturbação implementados e pode embutir vieses de quem a escreveu. Na conclusão: "mechanical perturbation is not better, its faults are merely findable". A escolha depende da pergunta de pesquisa.

## O protocolo para quem não tem oráculo

Antes de qualquer estatística agregada, para cada condição de geração (produtor, língua, modelo de prompt):

1. **Ler** de 15 a 20 itens gerados crus, inteiros. O número vem de n ≥ ln(1 - C) / ln(1 - p), para ver ao menos um item com falha com confiança C numa taxa de falha p. Com C de 99%: n=7 com 50%, n=13 com 30%, n=21 com 20%, n=44 com 10%. Ele toma 30% como referência, emprestado do controle positivo, para ilustrar um cenário de limite inferior (a falha dele foi de 100%). Quinze já passam em 30%; vinte chegam a cerca de 99,9% em 30% e ficam perto de 99% em 20%.
2. **Medir comprimento:** a média de palavras do campo gerado, por condição. No caso dele, cerca de duas palavras contra de vinte a quarenta e sete.
3. **Medir degeneração:** duas taxas, a fração de itens idênticos à resposta factual e a fração que começa com abertura conversacional ou é fragmento de menos de três palavras (12,2% e 81,0% no caso dele).

**Regra de decisão:** condição com taxa de degeneração acima de um dígito se resolve antes de entrar na estatística, corrigindo o pipeline ou excluindo a condição.

**O peso dos números:** os limiares "are not universal"; são "a worked example, not a calibrated standard". O que ele diz generalizar é a forma do diagnóstico: separação nítida de comprimento e degeneração entre a condição afetada e as outras. Tarefa de resposta naturalmente curta, ou falha de paráfrase sutil, tem outra linha de base, a estabelecer antes de medir.

**O que o protocolo não faz:** não detecta viés de juiz; corpus bem formado ainda pode medir juiz enviesado, e confirmar o item não valida a estimativa do viés. Não substitui um oráculo.

## Limites declarados

- Um único pipeline e uma única falha; o controle positivo testa um tipo de falha em um corpus.
- Assimetria não demonstrada entre tipos de falha, domínios e corpora; varredura fica para trabalho futuro.
- Três juízes de três famílias, uma comparação de produtores em uma língua, uma fonte enciclopédica.
- Classificação binária de fidelidade, certo contra alucinado. Como essa falha se propaga em julgamento de preferência ou qualidade, sem referência correta, é outra questão, e o artigo não trata.
- A referência em inglês, o HaluEval, não foi auditada pelo próprio protocolo: foi aceita pela reputação. A afirmação sobre os dados corrigidos se apoia só no turco.
- Não é censo de corpora afetados: só auditou o próprio pipeline, e cita candidatos sem verificar, como o CalibJudge.
- Não descobre viés novo: o dramático era artefato e o preservado é uma preferência de formato já conhecida.

## Tudo o mais que ensina

- **Por que quatro checagens falharam:** amostra maior, replicação, mecanismo convergente e manipulação controlada olham o agregado. Cada uma aumentou a confiança no efeito, e nenhuma é um oráculo.
- **Maioria pode esconder:** nos dados corrompidos, a maioria dos três juízes teve 0,962 de acurácia factual contra 0,642 do GLM. É compatível com a defesa de júri (Verga e outros, 2024; Zhang e outros, 2026) e com a possibilidade de a maioria esconder uma falha do estímulo (Ma e outros, 2025, sobre amplificação de viés com vários agentes). O autor deixa em aberto.
- **Outra fonte da mesma classe de falha:** o Gemini flash-latest é um modelo com raciocínio, e não desligar esse rastro consome o orçamento de saída em silêncio. A troca silenciosa de versão por trás de um apelido de modelo é da mesma classe; os apelidos dele ficaram estáveis durante a coleta (julho de 2026).
- **Prática sugerida:** relatar, junto de cada número agregado de viés, comprimento dos itens gerados, quantos degenerados e se alguém os leu.
- **Falsa pista com Li e outros 2026:** o autor havia distinguido seu efeito do vazamento de preferência, por DeepSeek e GLM serem de famílias diferentes; o registro fica para documentar o engano, já que a interação era artefato.
- **Levantamentos citados:** Judging the Judges (Soumik, 2026: viés de estilo de 0,76 a 0,92 e de posição de no máximo 0,04, em cinco juízes); Judging the Judges (Shi e outros, 2025, posição); BabelJudge (Shreyas KC, 2026); PoLL (Verga e outros, 2024); UDA (Zhang e outros, 2026); Gu e outros, 2025 (levantamento sobre LLM como juiz).
