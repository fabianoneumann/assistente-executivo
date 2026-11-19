# Métodos de revisão: avaliadores independentes, gravidade, checklists e conferência

Os métodos que dizem como revisar bem, para uma skill de revisão nascer com lentes e etapas que vêm de fonte e não de invenção. Parte do que a base já tem em [[conselho-revisao-e-bajulacao]] (o desenho do Code Review, o teste do conselho), [[desenho-de-rubrica-e-veredito]] (perguntas de sim ou não do CheckEval, checklist gerado da instrução do TICK) e [[orquestracao-de-skills-e-agentes]] (checklist vago dá nota inflada), e não repete; a caça a lacunas por um agente em contexto limpo é a mesma ideia aplicada a uma especificação.

## A pergunta

Como se revisa bem um trabalho? Quantos revisores, com que perguntas, como se separa o achado real do falso, como se dá gravidade, e como se pergunta a um modelo sem fazê-lo concordar ou inventar defeito?

## A resposta curta

Quatro tradições chegam a regras parecidas. **Um revisor sozinho acha só parte dos problemas**, e revisores diferentes acham problemas diferentes, então vale ter mais de um, cada um sozinho, juntando só no fim. **Achar e dar gravidade são etapas separadas**, e a gravidade de uma pessoa só é pouco confiável. **O checklist com pausa e confirmação reduziu complicações e mortes em cirurgia**, sem que se saiba qual parte funcionou; as regras de desenho (curto, de itens que se esquecem, "fazer e depois confirmar") vêm do Gawande e não foram medidas. E, na tarefa de fato, **a conferência rendeu mais quando quem confere não vê a resposta original e responde a cada pergunta isolada**; sem verificação de fora, a autocorreção quebrou mais do que consertou. O pre-mortem gera mais hipóteses de falha, sem medida de que sejam melhores. Tudo isso é evidência de pessoas (usabilidade, cirurgia, projetos) ou de modelos em fato e matemática: nenhuma fonte testa revisão por modelo de pesquisa, pauta ou peça. Isso dá à skill de revisão as lentes nomeadas, a separação entre achar, conferir e dar gravidade, o formato da seção de revisão em cada skill e o formato das perguntas da conferência.

## 1. Avaliação heurística: revisores independentes, cada um acha uma parte

- Nos quatro experimentos de Nielsen e Molich (1990), um avaliador sozinho achou em média 51%, 38%, 26% e 20% dos problemas, conforme a interface; individualmente, de 0% a 74,5%. As porcentagens são dos problemas que os autores conheciam, com avaliadores não especialistas e interfaces pequenas. Juntando avaliadores sorteados, com 5 se acha de 55% a 90% (cerca de dois terços), com 10, de 71% a 97%: de 5 para 10 ainda se ganham de 7 a 16 pontos, e os autores veem o retorno cair por volta de 10. [[2026-10-29-nielsen-molich-avaliacao-heuristica]]
- Avaliador fraco acha problema difícil e avaliador bom perde problema fácil, e o bom num sistema não é necessariamente bom no outro (R² = 0,33): por isso juntar ajuda. Os falsos positivos foram poucos, e, pela experiência dos autores (sem análise formal), quase sempre de um avaliador só.
- A recomendação é de 3 a 5 avaliadores, cada um sozinho, comparando só depois do relatório escrito; avaliar junto reduziria a variedade, que é a fonte do ganho (hipótese dos autores, não medida). O resumo de terceiros "um acha 35%, cinco acham 75%" não está nesse artigo; costuma ser atribuído ao modelo de Nielsen e Landauer (1993, DOI 10.1145/169059.169166), que fica só como citação, sem texto primário acessível e sem a atribuição conferida.
- O procedimento atual (NN/g, 2023): escopo estreito; ninguém vê o do outro antes de terminar; uma passada para conhecer e outra para apontar; cada achado ligado à heurística que fere; **ferir uma heurística não obriga a mudar**, o contexto pode justificar; consolidar por afinidade e discutir onde concordam, o que mais prejudica e o que pede mais dados. As 10 heurísticas vêm de uma análise de 249 problemas (1994). [[2026-10-29-nngroup-como-fazer-avaliacao-heuristica]]

## 2. Gravidade: depois da busca, por mais de um

- Combina frequência, impacto e persistência (e o efeito no negócio), numa escala de 0 a 4, em que 0 é "não concordo que seja problema" (funciona como recusa do achado) e 4 é "não sai sem consertar". [[2026-10-29-nielsen-gravidade-de-problemas]]
- A nota se dá **depois** da busca, sobre a lista completa, cada avaliador sem ver as notas dos outros; a de um só é pouco confiável, a média de três serve para muitos fins (experiência declarada, sem número).
- Cada nível se define pelo que se faz com o problema (1, corrigir só se sobrar tempo; 3, importante corrigir; 4, antes de lançar), sem fórmula. O que foi medido depois, inclusive a discordância entre avaliadores treinados e a falta de prova de que regra a reduza: [[gravidade-por-regra-ou-por-julgamento]].

## 3. Checklist: pausa, poucos itens, confirmação

- O checklist cirúrgico da OMS tem três pausas com confirmação em voz alta (antes da anestesia, antes da incisão, antes de sair da sala). Em oito hospitais, antes e depois, sem sorteio: complicações de 11,0% para 7,0% e mortes de 1,5% para 0,8%. Mesmo com ele, cumprir as seis medidas juntas só passou de 34,2% para 56,7%, e os autores não sabem dizer qual parte funcionou (a pausa, a cultura de confirmar, o efeito de ser observado). [[2026-10-29-haynes-checklist-de-cirurgia-segura]]
- As regras de desenho, não medidas (Gawande, a partir do Boorman, piloto e engenheiro de checklists da Boeing; só citação, por resumo; o próprio checklist da OMS tem 19 itens em três pausas): para quem já sabe fazer, "fazer e depois confirmar" num ponto de pausa definido; só os itens que mais custam se esquecidos e que de fato se esquecem; de 5 a 9; cada um verificável; testado no uso.

## 4. Pre-mortem: mais hipóteses de falha, menos confiança no plano

- O roteiro do Klein: anunciar que o plano falhou, cada um escreve sozinho por quê, depois uma razão por pessoa em rodadas. O "30% melhor" que ele cita mede **quantas** razões se geram, não se estão certas (Mitchell, Russo e Pennington, 1989). Imaginar a falha reduziu a confiança no plano cerca de duas vezes mais que listar prós e contras (Veinott, 2010; o desfecho é a confiança, não a qualidade do plano), e equipes de pre-mortem acharam, segundo um painel, mais riscos de qualidade e mais imprevistos de um caso histórico do que equipes de brainstorming (Gallop e Bischoff, 2016). A literatura é rala. [[2026-10-29-collins-pre-mortem]]

## 5. Conferência: perguntas abertas, sem ver o original

- No Chain-of-Verification, o modelo responde, cria perguntas para conferir a resposta, responde cada uma e reescreve. A versão que funciona é a **fatorada**: cada pergunta respondida isolada, sem ver a resposta inicial, que assim não contamina a conferência; com uma revisão final que marca cada fato como consistente, inconsistente ou em parte. Biografias, com o Llama 65B sem busca: de 55,9 para 71,4 no FactScore (medida da fração de fatos certos), perdendo alguns fatos por resposta (de 16,6 para 12,3); numa tarefa de listas, cerca de 17% das entidades da resposta inicial estavam certas contra cerca de 70% quando perguntadas uma a uma. [[2026-10-29-dhuliawala-chain-of-verification]]
- **Pergunta aberta rendeu mais que sim ou não** na variante fatorada de uma tarefa (0,22 contra 0,19; na conjunta, empate): perguntado se um fato é verdadeiro, o modelo tende a concordar com o fato como ele foi enunciado. Pedir "pense passo a passo" não reduziu a invenção. Cobre só erro de fato, e o teto é o que o modelo sabe.
- Raciocínio em passos discretos deixa o modelo achar o **primeiro** passo errado com mais precisão, e refazer a partir do último passo certo corrige de 2 a 4 vezes mais do que refazer a partir de um trecho já contaminado. Vale para modelos abertos de 3 a 120 bilhões de parâmetros, em respostas que se conferem por igualdade exata, e é o modelo corrigindo a si mesmo, não um revisor separado. Mas, **sem verificação de fora, a autocorreção quebra mais do que conserta** (quebrou 10,9% das respostas certas e consertou 6,2%); a salvaguarda que funcionou foi devolver a resposta inicial quando a confiança é baixa; nos modelos de 3 a 8 bilhões, não corrigir foi muitas vezes o melhor. [[2026-10-29-samanta-autolocalizacao-de-erros]]
- Tensão com o CheckEval ([[desenho-de-rubrica-e-veredito]]), em que perguntas de sim ou não aumentam a concordância entre juízes: lá a pergunta é sobre um critério da régua; aqui, sobre um fato enunciado pelo próprio trabalho. A leitura proposta: régua em sim ou não, fato em pergunta aberta.

## 6. O que isso dá a uma skill de revisão

| Etapa da skill | Regra | De onde |
|---|---|---|
| Achar | lentes nomeadas, cada achado ligado à lente e à regra que fere; ferir não obriga a mudar | Nielsen; NN/g |
| Achar, no nível profundo | mais de um revisor, cada um sozinho, juntando só no fim | Nielsen e Molich |
| Juntar os achados | separar o acordo, o conflito (com quem disse o quê) e o ponto que só um achou; depois do acordo, o que mais pesou foi preservar o ponto isolado; não copiar a resolução do conflito por maioria nem deixar quem junta escolher a própria síntese (escolheu a agregada em 92% a 100%) | Multi-expert [[2026-10-31-long-multi-expert-prompting]] |
| Conferir | um agente que não fez o trabalho, uma pergunta por achado; em achado de fato, pergunta aberta ("o que a fonte diz sobre X?"), e em achado de régua, sim ou não com o texto da regra; na dúvida, não confirma | pergunta isolada e aberta: CoVe; sim ou não e "na dúvida": Code Review |
| Gravidade | separada da busca, sobre a lista completa; 0 recusa o achado | Nielsen 1994 |
| Seção de revisão em cada skill | um ponto de pausa definido, com confirmação; poucos itens, os que de fato se esquecem, cada um conferível (regras não medidas) | pausa: checklist da OMS; desenho: Gawande |
| Lente do contra em decisões | pre-mortem: "o plano falhou; por quê?", cada um sozinho | Klein; Collins |
| Depois da revisão | nunca altera sozinha | Code Review |
| Na dúvida sobre uma correção | fica o original | Thought-ICS |

**O que o uso mostrou:** a conferência derrubou uma parte dos achados (menos que nas revisões feitas à mão), mas também rebaixou gravidades e corrigiu detalhes errados dentro de achados verdadeiros; a régua pegou contradições entre regras que nenhuma outra lente pegou; e quem pediu aplicou quase todos os confirmados. Daí vieram a entrega em dois blocos (maiores para decidir, menores numa tabela aprovada em bloco), a classe pré-existente e a re-revisão pelo que mudou (as duas do Code Review, seção 6 de [[conselho-revisao-e-bajulacao]]), e a lente "comparar com o anterior".

## Não verificado

- O modelo de Nielsen e Landauer (1993) e os números "35% e 75%": texto primário inacessível.
- As regras de desenho do Boorman, só por resumo do livro do Gawande.
- Que perguntas abertas rendem mais que sim ou não fora das tarefas de fato do CoVe.
- **A maior lacuna:** nenhuma fonte testa revisão por modelo de pesquisa, pauta ou peça. A transposição das regras de pessoas (vários avaliadores que divergem) para agentes do mesmo modelo é a mais frágil: a base já mostra que juízes do mesmo modelo erram juntos e que um agente com lentes chegou perto do conselho por um décimo do custo ([[composicao-do-painel-de-criticos]], [[conselho-revisao-e-bajulacao]]). Na prática, a conferência derrubou mais de um terço dos achados conferidos numa revisão de síntese: um primeiro número para calibrar.
