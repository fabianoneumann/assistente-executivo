# Calibração por dimensão: cada parte do portão contra a sua referência

Se cada dimensão de um portão de qualidade (forma, conteúdo, integridade) deve ser medida contra a sua própria referência, e contra quem se mede um modelo barato. Fontes: [[2026-10-29-chakrabarty-art-or-artifice-ttcw]], [[2026-10-29-bavaresco-judge-bench-20-tarefas]], [[2026-10-29-mukherjee-consenso-nao-e-alinhamento]], [[2026-10-29-goel-rubricas-co-cientista]], *JudgeBench: A Benchmark for Evaluating LLM-based Judges*, de Sijun Tan, Siyuan Zhuang, Kyle Montgomery, William Y. Tang, Alejandro Cuadron, Chenguang Wang, Raluca Ada Popa, Ion Stoica (https://arxiv.org/abs/2410.12784), [[2026-10-29-szymanski-juiz-contra-especialistas]], [[2026-10-29-sage-calibracao-bidirecional]], [[2026-10-29-jung-trust-or-escalate]]. Complementa [[desenho-de-rubrica-e-veredito]], [[classificacao-como-portao]] e [[composicao-do-painel-de-criticos]].

## A pergunta

Um portão que mede a concordância de tudo contra uma referência só (a leitura da pessoa dona da régua) mistura coisas que se medem de jeitos diferentes. Cada dimensão do portão deveria ser medida contra a sua própria referência? E o modelo barato (um modelo de decisão tipado, como o Jev), contra quem: a pessoa, o juiz ou o fato?

## A resposta curta

Sim, e a literatura separa as dimensões por um corte claro. Em julgamento de gosto e qualidade subjetiva, o juiz LLM fica no acaso contra especialistas e os juízes concordam entre si num eixo que os humanos não pesam; ali a referência só pode ser a pessoa dona da régua. Em correção, o juiz vai bem quando a afirmação é verificável e simples e mal quando pede domínio ou raciocínio; ali a referência não é nenhum avaliador, é o fato conferido na fonte. O modelo barato se calibra contra o modelo forte, mas o critério de sucesso continua sendo a referência humana ou o fato, numa amostra. E o kappa só se lê ao lado do teto (a pessoa contra ela mesma) e, quando a falha é rara, ao lado da sensibilidade e do alarme falso.

## O que a base já sustentava

- **A divisão de trabalho:** a pessoa que julga peças tende a olhar a forma, e o juiz acha falhas de integridade que ela não procura; a leitura de gosto de uma pessoa costuma ser estável quando ela repete a ordem de pares que já julgou.
- **Modelos concordam entre si e não com a pessoa:** juízes de famílias e tamanhos diferentes ficam perto do acaso contra o dono da régua nos critérios de texto e concordam entre si, em geral mais severos que ele.
- **Juízes erram juntos:** nove modelos valem cerca de dois votos independentes ([[composicao-do-painel-de-criticos]]).
- **O kappa e a amostra:** a porcentagem infla 34 a 41 pontos sobre o kappa; abaixo de 30 rótulos o intervalo é largo; 0,4 como piso útil; modelos de visão julgam mal estética de design (AesEval, DesignSense) ([[desenho-de-rubrica-e-veredito]]).
- **A cascata com fila humana e amostra do que passou**, e o acordo da pessoa consigo mesma como teto do juiz ([[classificacao-como-portao]]).

## 1. A concordância depende da dimensão

- **Gosto e criatividade: no acaso.** Em 14 testes de sim ou não sobre contos, especialistas concordam moderadamente entre si (kappa de Fleiss 0,41, de 0,27 a 0,66 por teste; 0,69 de correlação na soma), e GPT-3.5, GPT-4 e Claude contra eles dão kappa médio de 0,016, 0,035 e −0,006. O objeto é escrita criativa, não design visual. [[2026-10-29-chakrabarty-art-or-artifice-ttcw]]
- **O caso visual:** a nota holística de cartazes (0 a 10) contra a média de especialistas dá cosseno de 0,347 a 0,399 nos modelos comerciais (Claude-Sonnet-4.5, 0,384), que os autores chamam de "insensitive automatic raters". [[2026-10-31-feng-posteriq-cartazes]]
- **Em 20 tarefas, a propriedade decide.** Alto em seguir instrução (GPT-4o 0,84), raciocínio matemático (0,79 a 0,83) e consistência factual de resumo (QAGS, 0,72 com teto humano de 0,74); baixo em engajamento e de −0,24 a 0,01 em toxicidade e segurança. Nenhum modelo é o melhor em todas as propriedades. [[2026-10-29-bavaresco-judge-bench-20-tarefas]]
- **Consenso não é alinhamento.** Em rubricas subjetivas, os juízes concordam entre si tanto quanto os humanos entre si e alcançam só 58% a 66% da concordância humana; na única rubrica verificável, chegam a 88%. Somar juízes converge para o eixo deles, não para o humano; treinar abre as notas sem girar o eixo; o que ajudou foi ancorar em exemplos avaliados por humanos. [[2026-10-29-mukherjee-consenso-nao-e-alinhamento]]
- **Mesmo padrão em planos de pesquisa:** entre juízes, kappa de cerca de 0,57 a 0,63 na diretriz objetiva e abaixo de 0,35 nas subjetivas. [[2026-10-29-goel-rubricas-co-cientista]]

Leitura nossa: o kappa perto de zero dos modelos contra a pessoa na forma não é defeito a corrigir trocando de modelo; é o resultado esperado nessa dimensão.

## 2. Especialista, leigo e o dono da régua

- **O juiz se parece mais com o leigo.** Nas notas graduadas, os 11 modelos correlacionam mais com anotadores leigos do que com especialistas. [[2026-10-29-bavaresco-judge-bench-20-tarefas]] Em dietética e saúde mental, o GPT-4 concorda com especialistas em 60% a 68% da preferência geral (especialistas entre si, 72% a 75%) e com leigos em 76% a 80%. [[2026-10-29-szymanski-juiz-contra-especialistas]]
- **Especialistas também divergem** (0,41 nos contos), e em criatividade os autores avisam que maximizar a concordância não é o objetivo. Para uma régua de gosto, a referência útil é a do dono da peça, não um consenso de painel.

Leitura nossa: um juiz que sai **mais duro** que a pessoa, e não mais leve como um leigo, não contradiz esses achados: medem direções diferentes, e Goel acha juízes sistematicamente mais duros que especialistas no cumprimento de rubrica (seção 5).

## 3. Integridade: o juiz aponta, a fonte confirma

- **Fácil quando há referência simples:** consistência factual de resumo contra o documento, 0,72. [[2026-10-29-bavaresco-judge-bench-20-tarefas]]
- **No acaso quando pede raciocínio:** em pares com uma resposta certa e uma errada do mesmo modelo, o GPT-4o acerta 50,86% com prompt simples e 56,57% com o do Arena-Hard; o melhor modelo geral, 64,29%; o o3-mini com raciocínio alto, 80,86%. Conferir é tão difícil quanto resolver. *JudgeBench: A Benchmark for Evaluating LLM-based Judges*, de Sijun Tan, Siyuan Zhuang, Kyle Montgomery, William Y. Tang, Alejandro Cuadron, Chenguang Wang, Raluca Ada Popa, Ion Stoica
- **Deixa passar o que o especialista pega:** imprecisões e recomendações danosas que nutricionistas e psicólogos marcaram passaram sem sinal do juiz. [[2026-10-29-szymanski-juiz-contra-especialistas]]
- **A reconciliação:** "o factual é fácil" vale para afirmação checável contra um texto dado; não vale para afirmação que pede conhecimento de domínio. Por isso a integridade fecha na fonte, e não no veredito de um avaliador.
- **O juiz também audita o gabarito:** no SAGE, quando o juiz discordava do rótulo humano, muitas vezes tinha achado evidência que o anotador não viu; o rótulo era corrigido depois de validação. [[2026-10-29-sage-calibracao-bidirecional]]

## 4. Modelo barato contra o modelo forte

- **Professor e aluno, com o humano por cima.** No SAGE, o juiz forte (o3) foi calibrado contra algumas centenas de exemplos de especialistas do produto (kappa linear ponderado de 0,67 a 0,77, em quatro intervenções), e o aluno de 8B foi treinado nas saídas dele. O critério de sucesso é o **aluno contra os humanos** (0,72 e 0,73), não contra o professor (0,81); o professor contra humanos (0,76 e 0,77) é o teto do aluno, e humano contra humano (0,78 e 0,83) é o teto da tarefa. [[2026-10-29-sage-calibracao-bidirecional]]
- **Escalar pela confiança.** O juiz barato decide quando está confiante e sobe o resto; com o limiar calibrado em 500 itens humanos, a cascata garante 80% de concordância com 68% a 79% de cobertura, onde o GPT-4 sozinho quase nunca chega a 80%. A confiança que o modelo declara ou a probabilidade da resposta superestimam a concordância; a que funcionou foi a concordância entre várias chamadas com exemplos diferentes. Os itens em que o juiz se absteve eram os mais subjetivos também para os humanos. [[2026-10-29-jung-trust-or-escalate]]
- **A ressalva de Mukherjee vale aqui:** a concordância entre o modelo barato e o forte mede imitação, não validade. [[2026-10-29-mukherjee-consenso-nao-e-alinhamento]]

## 5. Kappa: teto, prevalência e sensibilidade

- **Comparar com o teto, não só com o piso.** No SAGE, 0,77 vale porque o teto humano é 0,83; nos contos, 0,41 entre especialistas é o máximo razoável. [[2026-10-29-sage-calibracao-bidirecional]] [[2026-10-29-chakrabarty-art-or-artifice-ttcw]]
- **Comparação justa:** medir o juiz contra a média de vários avaliadores e o humano contra um colega favorece o juiz em vários graus; deixar um avaliador de fora e medir os dois contra os demais. [[2026-10-29-mukherjee-consenso-nao-e-alinhamento]]
- **Falha rara derruba o kappa.** Em "sem problema ético", concordância acima de 90% e kappa abaixo de 0,25, porque quase todo plano é correto. E a assimetria: quando o humano diz que o item foi violado, os juízes concordam de 89% a 98%; quando diz que foi cumprido, de 22% a 49%. Pela porcentagem, o critério objetivo concorda mais que o subjetivo; pelo kappa, empatam (0,326 e 0,325). [[2026-10-29-goel-rubricas-co-cientista]]

## A regra que sai daqui

1. **Forma contra o dono da régua.** A pessoa é a referência do gosto e da forma; nenhum modelo é medido como substituto dela nessa dimensão.
2. **Conteúdo e integridade contra o fato conferido na fonte.** O juiz aponta; a confirmação é na fonte (repositório, documento, base, código), não no aval de quem lê; mede-se o juiz por acerto (falhas confirmadas que ele pega) e alarme falso (apontamentos que a fonte desmente).
3. **O modelo barato contra o juiz, depois da régua decidida**, com uma amostra conferida contra o fato ou contra a pessoa, e escalonamento pela confiança dele: seguro, decide; incerto, sobe para o juiz.
4. **Kappa comparado com o teto**, a pessoa contra ela mesma; na integridade, junto com sensibilidade e alarme falso.

## Não verificado

- **Gemini, sem fonte primária** (só blogs de fornecedores: Confident AI, Evidently, Galileo, Netflix): juízes concordariam de 80% a 85% com humanos em critérios subjetivos. Contradiz o kappa perto de zero de Chakrabarty e os 58% a 66% de Mukherjee. **Origem provável, e por que não contradiz de fato:** o "mais de 80%, igual a humanos entre si" do MT-Bench, que vale só para pares sem empate (85% contra 81%); com empates e inconsistências, 66% contra 63%, e cai a cerca de 70% entre modelos de desempenho parecido [[2026-10-31-zheng-mt-bench-juiz-llm]]. É concordância bruta em pares de respostas de chat, não kappa em critério de gosto; na meta-avaliação da survey de Gu, a concordância com pessoas fica de 50,7% a 61,7% em todos os juízes [[2026-10-31-gu-survey-llm-as-a-judge]].
- **Busca nativa:** "0,83 contra um especialista, 0,51 contra a maioria", atribuído à revisão de saúde arXiv 2605.25273; não aparece no resumo, não aberto.
- **Venues não conferidos nos anais:** KDD '26 do SAGE (pela referência da ACM no artigo); Szymanski sem publicação final encontrada.

## O que falta medir num portão novo

- **O teto:** a pessoa contra ela mesma na forma, relendo peças já julgadas.
- **O juiz na integridade:** acerto e alarme falso contra o fato conferido, numa amostra que inclua as peças que o juiz **aprovou** (o que ele deixa passar não aparece olhando só os apontamentos).
- **A confirmação humana:** quanto a pessoa pega quando confere ativamente, e não só quando lê pela forma.
- **O modelo barato pela confiança:** se a confiança dele separa os casos em que concorda com o juiz dos que não, e qual cobertura sobra num limiar que garanta a concordância pedida.
- **O tamanho da amostra:** com falha rara, quantas peças conferidas bastam para estimar sensibilidade com intervalo útil.
