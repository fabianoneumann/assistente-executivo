# Lições e aprendizado contínuo: por que bases de lições morrem e como agentes aprendem com o uso

O que as organizações aprenderam sobre registrar lições e o que a pesquisa com agentes de modelo de linguagem mostra sobre aprender com a própria experiência, sem mudar os pesos do modelo. Parte do que a base já tem em [[termos-dos-lacos-de-avaliacao]] (o Reflexion, memória curta de reflexões entre tentativas), [[refinamento-iterativo-com-criticos]] (o registro das passadas) e [[metodos-de-revisao]] (o pre-mortem), e não repete.

## A pergunta

Por que registros de lições costumam virar arquivo morto? E, nos agentes que aprendem com o uso, o que entra numa lição, como ela chega ao momento de agir, como se poda, e onde a lição tirada da experiência engana?

## A resposta curta

As duas tradições chegam ao mesmo ponto: **a lição vale pelo momento em que chega a quem decide**, não pelo registro. Na NASA, uma base de lições à parte foi pouco usada e pouco alimentada, e a auditoria atribui parte disso à lição ter deixado de ser exigida ao longo do projeto, só no encerramento. Nos agentes, as lições entram no prompt na hora de agir, e o que ajuda é uma lista **curada e curta**, com cada lição dizendo **quando vale**; o histórico completo sem curadoria chegou a piorar o modelo. E aprender com a própria experiência engana de jeitos medidos: o agente registra como acerto o que causou a falha, culpa a causa errada, perde a condição de validade da lição ou cria regra que causa falhas novas; mesmo a lição correta tende a ficar presa ao caso de origem. **Registrar também o que deu certo** transferiu mais que investigar a falha. Nenhuma fonte testa lições escritas por um assistente para as próprias skills: o que vem abaixo é evidência de organizações e de agentes em benchmarks.

## 1. Por que bases de lições morrem: a auditoria da NASA (2012)

- A auditoria do inspetor-geral (IG-12-012) ouviu os gerentes de 28 dos 32 projetos de voo lançados de 2005 a 2011. Só **16 usaram** o sistema de lições (LLIS) durante o projeto, e só 6 desses o acharam útil; **12 contribuíram** com lições; só **10 conheciam** a exigência de contribuir. Uma frase de gerente resume o uso por obrigação: não acharam nada útil, mas puderam dizer que tinham "checked this box" (a frase é sobre consultar o sistema, p. 11). [[2026-10-29-nasa-oig-licoes-aprendidas-llis]]
- **O momento do registro piorou com a norma:** em 2002 o gerente informava em cada marco como aplicou lições e contribuía ao fim de cada fase; em 2005, "ao longo do ciclo"; em 2007, só "no descomissionamento ou encerramento". Para a auditoria, isso reduz a tempestividade, a utilidade e o número de lições, porque o projeto dura anos e troca de gerente. É argumento da auditoria, não medida: as entradas no sistema já tinham caído de 87 em 2005 para cerca de 20 por ano de 2006 a 2009, antes da norma de 2007.
- **As causas que os gerentes deram:** sistema desatualizado, pouco amigável e sem informação relevante; projetos "muito diferentes"; difícil achar o que se aplica; registrar é tarefa de baixa prioridade, sem verba; a norma não diz explicitamente que a lição vai ao sistema.
- **A entrega no momento da decisão nunca saiu do papel:** a equipe de 2002 redesenhou o sistema para entregar a informação "no momento em que estão tomando uma decisão crítica", plano não finalizado; o relatório de 2000 pedia "documentar enquanto se faz", meta não cumprida em 2012.
- **Verba sem relação com resultado:** de 2008 a 2010, o JPL recebeu US$ 70 mil e contribuiu com 35 lições; Glenn recebeu cerca de US$ 470 mil e contribuiu com 5. O JPL era o único Centro com fluxo constante, e seus gerentes usavam o processo interno do próprio JPL.
- **Limite:** as causas são relato dos gerentes; a auditoria não mede se alguma lição teria evitado um problema.
- **Só citação:** a revisão depois da ação do Exército americano (After Action Review: o que devia acontecer, o que aconteceu, por que houve diferença, o que fazer da próxima vez; Morrison e Meliza, 1999, U.S. Army Research Institute) e a meta-análise de debriefings de Tannenbaum e Cerasoli (2013, Human Factors; d = 0,67, pelo resumo), não abertas; o GAO-02-195 (2002), pela busca.

## 2. O que entra numa lição, nos agentes

- **ExpeL** (Zhao et al., 2023): a lição ("insight") sai de comparar a falha com o sucesso da mesma tarefa e de lotes de sucessos; insights escritos à mão por quem estudou os erros deram 32% no HotpotQA, contra 39% dos extraídos pelo modelo, e tirar insights sem pares de falha e sucesso deu 35%. [[2026-10-29-expel-agentes-aprendizes-experienciais]]
- **ERL** (Allard et al., 2026): cada heurística tem formato fixo, a análise da causa e uma diretriz curta com **gatilho** ("quando eu encontrar X") e **ação** ("devo fazer Y"); o prompt dá o exemplo ruim ("devo tomar mais cuidado com arquivos") e o bom ("quando o caminho é desconhecido, usar `ls -R` antes de `read_file`"). Heurísticas generalizaram melhor que trajetórias brutas no prompt, que pioraram 1,9 ponto contra a base. [[2026-10-29-erl-aprendizado-reflexivo-experiencial]]
- **Agent Workflow Memory** (Wang et al., 2024): a unidade é a sub-rotina abstrata que se repete ("buscar um produto"), e os valores do dia viram variáveis; o exemplo concreto inteiro enviesa o agente a repetir o caso. [[2026-10-29-agent-workflow-memory]]
- **Dynamic Cheatsheet** (Suzgun et al., 2025): cada item tem descrição, as questões de onde veio, um exemplo e um **contador de uso**; teto de cerca de 2.000 a 2.500 palavras; entra só o que generaliza. [[2026-10-29-suzgun-dynamic-cheatsheet]]
- **Voyager** (Wang et al., 2023): a habilidade (um programa) só entra depois que o crítico confirma o sucesso; sem essa autoverificação, os itens descobertos caem 73%. [[2026-10-29-wang-voyager]]

## 3. Como a lição chega ao momento de agir

- **ExpeL:** a lista inteira de insights entra no enunciado de cada tarefa; só os exemplos de trajetória são escolhidos por semelhança.
- **ERL:** um modelo mais forte que o agente lê a tarefa e as heurísticas e escolhe as 20 mais relevantes, com justificativa e nota de 0 a 100; isso deu 56,1% de sucesso no Gaia2, contra 53,3% da recuperação por embeddings e 53,8% da melhor escolha aleatória. Quantidade demais piora: ao acaso, o ganho sobe até cerca de 40 a 60 heurísticas e cai depois.
- **Voyager:** a habilidade é achada pela descrição curta escrita ao entrar (até 6 frases); 96,5% de acerto entre as 5 primeiras.
- **AWM:** sem recuperação; a memória é separada por site e vai inteira para o contexto.

## 4. Poda: lista editável contra lista que só cresce

- **Editável:** no ExpeL, o modelo aplica operações à lista (acrescentar, editar, votar a favor, votar contra); cada regra nasce com importância 2, ganha com voto a favor ou edição, perde com voto contra e é apagada ao chegar a zero, porque até sucessos podem induzir regra ruim. No Dynamic Cheatsheet, o curador remove o redundante, o trivial e o específico demais, e a versão melhor substitui a antiga.
- **Curadoria contra histórico completo** (Dynamic Cheatsheet, AIME): colar todo o histórico derrubou o GPT-4o abaixo da própria base (de 20,0% para 13,3% no AIME 2024), contra 40,0% com a cola curada. Uma heurística errada que entra se espalha para os casos vizinhos, e por isso a lista pede poda.
- **Só cresce:** Voyager, AWM e ERL não descrevem remoção; o ERL lista entre os limites resolver diretrizes conflitantes num repositório grande.
- **O custo de reescrever:** no Dynamic Cheatsheet, a cola é regenerada a cada passo, e o modelo às vezes a abrevia ("conteúdo anterior preservado"), o que a degrada com o tempo.

## 5. Onde a lição tirada da experiência engana

- **A lacuna entre consertar e generalizar** (Zhao et al., 2026, aprendendo só com falhas): os agentes recuperaram de 0% a 33,3% das tarefas que tinham errado, conforme modelo, paradigma e ambiente, mas o desempenho em tarefas novas ficou limitado e em algumas configurações caiu. [[2026-10-29-zhao-consertar-falhas-sem-generalizar]]
- **Quatro modos de erro**, em fatias das atualizações revisadas à mão (tabela 1 do artigo; uma atualização pode ter vários): falso sucesso, o que causou a falha registrado como boa prática (19,7% a 43,8%); atribuição errada ou inventada (24,6% a 53,2%); **distorção**, a lição que perde a condição de validade ao ser consolidada, como "volte antes de nova busca" virar "sempre volte da página de resultados" (19,5% a 35,1%); e orientação venenosa, a regra errada que causa falhas novas (23,0% a 43,2%). O artigo não diz quantas atualizações revisou.
- **Mesmo a lição correta transfere mal:** guardando só a experiência verificada à mão como correta, o teste ficou igual ou abaixo de nenhuma experiência em quatro das cinco configurações, porque ela continua presa aos passos do caso de origem.
- **Registrar o que deu certo:** aprender com sucessos deu o maior ganho no teste; o retorno do verificador e mais investigação da falha melhoraram pouco. No ERL o quadro é outro: heurísticas só de falha deram o maior resultado geral (58,9%, contra 56,1% com as duas), puxado pela busca, e as só de sucesso renderam mais em execução; como a mistura real de tarefas é desconhecida, os autores recomendam as duas. Sem o sinal de resultado, o agente julgou o próprio resultado certo em 70% das vezes e o ERL caiu de 56,1% para 51,2%.
- **Quem já acerta ganha mais:** no Dynamic Cheatsheet, o GPT-4o-mini piorou com a memória (de 16,7% para 13,3% no AIME 2024), enquanto o Claude 3.5 Haiku melhorou (de 10,0% para 36,7%); para os autores, modelos que geram poucas soluções corretas não conseguem alimentá-la.

## O que isto dá para um ambiente de agentes

O desenho das lições das skills (`decisions/licoes-das-skills.md`) se apoia nestas fontes, sem que nenhuma o teste: a lição mora na pasta da skill e é lida antes de usá-la (a entrega no momento da decisão, que a NASA planejou e não fez); é registrada na mesma entrega em que aparece (não no encerramento); diz **quando vale** (contra a distorção); registra acertos, não só falhas; e a lista se poda por decisão de quem é dono do ambiente, com um estado intermediário "a sair" antes de a lição sair de vez (saída gradual parecida com a do ExpeL, onde quem decide é o modelo). Um classificador calibrado com perguntas fechadas sobre as lições (por exemplo, um modelo de decisão tipado) segue a avaliar, na linha da escolha por modelo do ERL; nenhuma fonte testa esse papel.

## Não verificado

- O AAR e a meta-análise de debriefings: só pelo resumo da busca.
- Os quatro modos de erro: percentuais de uma revisão à mão de tamanho não informado, em benchmarks de web e de tarefas domésticas.
- O ganho do ERL fora do Gaia2: no τ²-Bench (atendimento com usuário simulado) foi de 36,7% para 38,0%, e caiu em Telecom (de 30,0% para 28,3%).
