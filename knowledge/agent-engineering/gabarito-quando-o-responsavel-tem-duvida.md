# Gabarito quando o responsável tem dúvida: quem decide e o que fazer com o caso indeterminado

Quem decide o gabarito de um avaliador quando o responsável pela régua está em dúvida, e o que fazer com o caso indeterminado. A checagem jornalística tem página própria, [[quem-decide-na-checagem]]; o controle de quem responde, [[controlar-se-o-revisor-concorda-demais]]; a gravidade, [[gravidade-por-regra-ou-por-julgamento]]; os leitores, [[testar-compreensao-com-leitores]].

Convenção: "leitura nossa" liga a fonte a um ambiente de agentes e não está na fonte. "(resumo)" é número lido só no resumo oficial; "só citação" é texto fechado; "sem ficha" é texto aberto e lido, que não virou arquivo na base. "VPP" é a chance de um alarme ser defeito de verdade.

## A resposta curta

- **Nada lido responde ao caso de uma pessoa só em dúvida.** Nada lido compara, em número, "o dono decide" com "o segundo revisor decide". O mais próximo é pessoa e IA julgarem sem se ver, com um segundo humano no desempate ([[2026-11-04-berger-independent-aggregation-2026]]), e não há dono nesse desenho. A ponte com o caso de um dono só é leitura nossa.
- **Os métodos que descrevem o procedimento dizem quem decide e o que fazer na discordância.** A decisão continua com alguém ou com uma regra escrita antes (leitura nossa quanto à extensão). A revisão de painéis acha grande variação e pouco relato, então isso não é um padrão estabelecido.
- **Há uma posição contrária já na base:** um único especialista como "ditador benevolente" ([[2026-10-30-husain-shankar-faq-de-avaliacoes]]). É opinião, sem número, e parte de alguém que sabe a resposta; não diz o que fazer quando esse alguém duvida.
- **Excluir o caso difícil superestima a acurácia** (Kellerhuis). Como usar a incerteza coletada ainda está em desenvolvimento.
- **Adjudicar não prova acerto** (Klompenhouwer, Schaekermann), **e concordar não é acertar** (Beigman, Aroyo e Welty, [[2026-11-04-uscinski-2015-epistemologia-da-checagem-replica-a-amazeen]]).
- **Consequência para quem mede um avaliador:** sem gabarito, o falso alarme em casos não plantados fica sem medida (leitura nossa).

## 1. O que os métodos escrevem antes

- **Regra de precedência** (Smith 2018, 116 pacientes, 6 especialistas em 2 painéis de 3): cada um julga sozinho; acordo individual vence consenso, consenso vence voto 2 a 1, e o resto é "indeterminado". Resultado: 2 de 116 (1,7%) indeterminados, excluídos da análise. Nos 20 casos revistos pelos dois painéis, 75% de diagnósticos iguais e κ = 0,55 (IC 95% 0,21 a 0,89). Só esses 20 podiam cair na saída de indeterminado, então a taxa ali é de 2 em 20 (leitura nossa). [[2026-11-04-smith-2018-disfuncao-tuba-eustaquio-padrao-de-referencia]]
- **Adjudicador com limite** (Oliveira 2022, SemClinBr, corpus clínico em português do Brasil, 1.000 documentos, 100% de dupla anotação): o terceiro podia remover o que os dois marcaram, sem criar anotação nova; o preprint de 2020 dizia que não podia remover, e as versões não explicam a diferença. Em vez de excluir os de baixa concordância, o corpus separa "gold" de "silver". [[2026-11-04-oliveira-2022-semclinbr-corpus-clinico-portugues]]
- **O anotador marca a própria dúvida, e só isso sobe** (Hossain 2026, 9.387 relatos de acidentes, um anotador treinado): 852 marcados como incertos (9,1%) foram a uma adjudicação conjunta com alguém mais especialista, com saída "confirmado", "revisado" ou "sem resolução por falta de evidência". Ficaram como estavam 696 (81,7%) e mudaram 156 (18,3%); os autores leem a marca como conservadora, e escrevem que anotar com confiabilidade é possível mesmo com um anotador treinado, com evidência textual e revisão de especialista. Não mediram o anotador contra si mesmo. A incerteza declarada previu desacordo com o código estruturado (razão de chances 8,91). O κ de 0,990 é por construção (leitura nossa), porque o adjudicado só difere nos casos que o próprio anotador marcou. [[2026-11-04-hossain-2026-when-ground-truth-disagrees-crash-narratives]] A dúvida sobe a um especialista, papel que falta quando há um dono só (leitura nossa). A base já nomeia o desenho: "acreditar no extremo", em [[camadas-de-avaliacao-arranjos-e-condicoes]].
- **O que uma revisão do campo achou** (Kellerhuis 2025, 318 estudos com painel como padrão, 2012 a 2022): painéis de 2 ou menos em 29%, de 3 ou 4 em 55%; método de decisão não relatado em 21%; incerteza coletada em cerca de 4% a 5% (o texto traz os dois números); falta orientação sobre o desenho ideal. Recomenda não excluir os casos de discordância e considerar coletar uma medida de incerteza. Forçar o binário "pode enviesar", sem direção conhecida. Licença CC BY-NC-ND: só ficha, integral em https://pmc.ncbi.nlm.nih.gov/articles/PMC12070646/. [[2026-11-04-kellerhuis-2025-painel-de-especialistas-como-padrao-de-referencia]]
- **Viés de incorporação:** a mesma revisão trata do painel que vê o resultado do teste em avaliação. Isso pode fazer o resultado pesar no julgamento; esconder pode piorar a classificação; o efeito dominante é difícil de prever, e a recomendação, por cautela, é não mostrar. 18% dos estudos dão o resultado ao painel. A revisão não testa os dois caminhos. É o problema de uma mesa que mostra à pessoa o ponto em questão, porque sem ele ela não sabe o que está sendo perguntado (leitura nossa).

Outras fontes guardam a dúvida por outro caminho: distribuição de leituras (Aroyo e Welty), rótulos suaves (AmbiFC, Glockner et al., TACL 2023, α de 0,488 por passagem, sem ficha, https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00629/119057/) e probabilidade em vez de classe (Kellerhuis et al. 2025, simulação, sem ficha, https://link.springer.com/article/10.1186/s12874-025-02557-7).

## 2. O que contraria

- **Adjudicar pode custar sensibilidade** (Klompenhouwer 2015, Eur Radiol, 84.927 mamografias, resumo, análise retrospectiva, só citação, PMID 25894007): na leitura dupla cega, a arbitragem por terceiro leitor derrubaria a convocação de 3,4% para 2,2% e a sensibilidade de 83,2% para 76,0%, subiria o VPP de 22,3% para 31,2% e não mudaria significativamente a detecção. Na leitura não cega, a queda de sensibilidade não foi significativa. Dinnes 2001 (Breast, resumo, só citação) acha ganho com arbitragem ou consenso, com ressalva sobre a mistura de métodos.
- **Adjudicar não resolve tudo** (Schaekermann 2019, estadiamento do sono, 36 especialistas, 10.349 janelas): 44% com alguma discordância; a adjudicação estruturada subiu o acordo em 20% a 30%, e 37% dos discordantes seguiram sem resolução depois de três rodadas. [[2026-11-04-schaekermann-2019-desacordo-de-especialistas-adjudicacao-estruturada]]
- **O especialista que desempata pode não existir** (Sylolypavan 2023, 11 consultores de UTI): κ de Fleiss de 0,383. Modelos treinados com o voto de todos ficaram em F1 (medida de acerto de 0 a 1) de cerca de 0,254 na validação externa; com o voto dos anotadores mais consistentes, 0,438. Os autores não testaram o "super especialista" diretamente, por anonimato: usam uma correlação de 0,51 como indicador e concluem que a ideia "nem sempre" vale. [[2026-11-04-sylolypavan-2023-anotacoes-inconsistentes-uti]]
- **Checadores divergem** (Allen 2021, 207 artigos, 3 checadores freelancers): veredito igual em 49,3%, 2 de 3 em 42,0%, os 3 diferentes em 8,7%; κ de 0,38, r de 0,62. Os autores leem o mesmo dado dos dois lados, como "concordância considerável" e κ só razoável. Uma multidão de cerca de 26 leigos chega a AUC (capacidade de separar verdadeiro de falso, de 0,5 a 1) de 0,86 com a fonte à vista e 0,83 sem ela, contra o veredito modal, e o gabarito é ele mesmo incerto em metade dos casos (leitura nossa). [[2026-11-04-allen-2021-checagem-em-escala-sabedoria-das-multidoes]]
- **κ alto não basta** (Beigman Klebanov e Beigman 2009, modelo matemático que supõe casos fáceis e difíceis): com 1.000 itens, dois anotadores e κ = 0,8, até cerca de 13,8% das concordâncias podem ser sorte. [[2026-11-04-beigman-klebanov-2009-do-acordo-entre-anotadores-ao-modelo-de-ruido]]
- **O guia pode esconder a dúvida** (Aroyo e Welty 2015, artigo de posição, com números só do próprio grupo): para eles, guia mais detalhado acaba com a discordância sem melhorar o rótulo. [[2026-11-04-aroyo-welty-2015-truth-is-a-lie-crowd-truth]]

## 3. Custo

Oliveira 2022: 14 meses e 13 pessoas para 1.000 documentos. Carrell 2016 (Methods Inf Med, sem ficha, https://pmc.ncbi.nlm.nih.gov/articles/PMC5194214/): o custo por instância achada a mais vai de US$ 2,76 com um anotador a US$ 376,99 com o quarto, em dólares de 2014 (o resumo do artigo dá de US$ 0,71 a US$ 377, em mediana); mede achar o que faltou, não desempatar. LDC (Medero 2006, sem ficha, https://www.ldc.upenn.edu/sites/default/files/lrec2006-efficient-approach-decision-points.pdf): adjudicação cara a ponto de ir a 10% a 15% do treino. Nada lido dá custo por caso para uma pessoa só.

## O que isso implica para quem monta um gabarito (leitura nossa)

Nada aqui é conclusão de fonte; a tabela é proposta, a testar.

| Família de defeito | Quem decide, a testar | De onde veio a ideia | Onde é mais fraco |
|---|---|---|---|
| Fato | A fonte ligada à afirmação; sem ela, "insustentável" | AFP, Lupa, Aos Fatos | A conferência automática do lastro não está provada |
| Coerência | Código quando é literal; nos demais, regra escrita | Smith, Oliveira | As fontes usam segundo humano; modelo no lugar é extrapolação. Quando a resposta final da pessoa segue quase sempre a de um modelo, não se sabe se ele acertou ou se ela ancorou |
| Clareza | Leitores, em amostra | CDC, Digital.gov, Scott | Acha problema, não prova ausência; depende do público declarado. Sem regra escrita, quem a escreveria é o próprio dono da régua |
| Gravidade | Para a conta, não importa; para as rubricas, falta definir | BBC, Lupa | Nada do que li mostra que regra aumenta a concordância |
| Gosto | O dono da régua | a mesa só pergunta o que é gosto | |

- **"Não sei" não é um só:** mistura dúvida de regra, de fato e de contexto. Se marcar "não sei" também abre as leituras dos modelos, a resposta seguinte já não é cega. Tratar esses casos como indeterminados muda o VPP, a taxa de peça limpa e o gabarito de qualquer nova rodada.
- **Aceitar a falta de gabarito é uma saída legítima:** fechar a bancada sem candidato aprovado e deixar o avaliador rodando em sombra, com alarmes registrados e não mostrados, até haver como medir.

## Contradições, cuidados e não verificado

- Adjudicar sobe o acordo (Schaekermann) e pode baixar a sensibilidade (Klompenhouwer): depende da medida.
- O guia ajuda (Passonneau 2012, afirmado pelo Gemini, κ de menos de 0,40 para mais de 0,75; texto não obtido, não verificado) ou esconde (Aroyo e Welty, sem número).
- Smith guarda o indeterminado e exclui da análise; Kellerhuis recomenda não excluir.
- Números do Gemini que não fecharam, descartados: Felson 1995, Amazeen com mais de 80%, Dinnes com 5% a 15%.
