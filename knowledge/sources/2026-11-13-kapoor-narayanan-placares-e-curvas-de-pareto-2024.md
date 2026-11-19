---
titulo: "AI leaderboards are no longer useful. It's time to switch to Pareto curves."
tipo: artigo
autor: "Sayash Kapoor, Benedikt Stroebl, Arvind Narayanan"   # linha "By" do corpo do post; o cabeçalho da página (bylines do Substack) mostra só Sayash Kapoor e Arvind Narayanan
url: "https://www.normaltech.ai/p/ai-leaderboards-are-no-longer-useful"
publicado_em: 2024-04-30   # a página mostra "Apr 30, 2024"; JSON-LD datePublished e dateModified 2024-04-30T14:03:42+00:00
capturado_em: 2026-11-13
areas: [agent-engineering]
entrada: pesquisa
tags: [agent-evaluation, pareto-frontier, inference-cost, reproducibility, humaneval, ldb, lats, reflexion, baselines, benchmarks]
licenca: "protegido: rodapé da página '© 2026 Sayash Kapoor and Arvind Narayanan', sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
---

# Kapoor, Stroebl e Narayanan: placar de agente sem custo não serve

Nota de fato (`knowledge/sources/README.md`, item 2): post curto de autores de referência, mas o que a base usa dele são medidas, linhas de base e o resultado de uma reprodução, por isso tabelas de fatos e não ficha de prosa. Não há integral: a página é protegida.

**Proveniência.** Post da newsletter AI Snake Oil (o próprio texto convida a assinar "AI Snake Oil"; a publicação hoje se chama "AI as Normal Technology" e vive em normaltech.ai), subtítulo "What spending $2,000 can tell us about evaluating AI agents". HTML baixado em 2026-11-13 da `url` (que é também o `canonical` e o `og:url` da página), com o texto extraído para a cópia de trabalho e lido no texto bruto em 2026-11-13. Cobertura: o texto inteiro do post, do subtítulo aos agradecimentos, e as 19 notas de rodapé. Não abertos: o apêndice do post, o código da análise, os links para o paper do LDB, o placar do Papers With Code e o post do Andrew Ng; os números de acerto e custo de cada agente estão nas figuras, que a extração não traz, e só os que o texto escreve entram aqui.

**Conferência lado a lado** (2026-11-13, pela régua do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido, aqui as que juntam duas afirmações, trazem um juízo dos autores ou têm verbo conjugado; a célula que só traz um fato (número, nome de agente ou modelo, valor, "sim" ou "não", rótulo curto) fica fora, e as três citações literais estão à parte. Resultado: 25 de 31 unidades seguem uma frase da fonte (cada célula de texto condensa uma frase ou duas do post, como é próprio da nota de fato); a maior sequência na ordem da fonte é de 4 unidades seguidas, nas notas 14, 15 e 19 (detalhe no fim da ficha). O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: o script não mede tradução, e a conferência é esta conta), com 0 trecho e 2 células marcadas como coladas fora de trecho: os rótulos de linha "GPT-3.5 sozinho, com os prompts do paper do LDB" e o do GPT-4, que casam com a fonte pelos nomes próprios (GPT-3.5, GPT-4, LDB, prompts, paper) e são rótulos de fato.

## Em uma frase

Os autores reavaliaram no HumanEval três agentes que disputavam o topo do placar (LDB, LATS e Reflexion), mediram também o custo em dólar e compararam com linhas de base simples que nenhum paper testava: as simples empatam ou ganham gastando menos, a reprodução não alcança os números publicados do LDB e do LATS, e por isso o placar de agentes só faz sentido como curva de Pareto de acerto contra custo.

## A medição

| Item | Valor |
|---|---|
| Benchmark | HumanEval, 164 problemas |
| Versão do HumanEval | a dos autores do LDB (testes de exemplo nos 3 problemas sem eles), em todos os experimentos |
| Execuções por agente | 5 |
| Medidas | acerto médio; custo total médio |
| Eixo vertical do gráfico principal | 0,7 a 1 |
| Eixo inteiro, barras de erro, robustez | no apêndice |
| LDB (A, B) | A: gerador; B: depurador |
| LDB (A) | mesmo modelo nos dois papéis |
| Versão dos modelos da OpenAI | abril de 2024 |
| Checagem de robustez | modelos de junho de 2023; resultado substancialmente igual |
| Llama-3 | endpoints da together.ai |
| Preço do Llama-3 8B | US$ 0,20 por milhão de tokens (entrada e saída) |
| Preço do Llama-3 70B | US$ 0,90 por milhão de tokens (entrada e saída) |
| Outros benchmarks rodados | HotPotQA; NovelQA |
| Resultado neles | parecido: custo muito diferente por trás de ganho pequeno de acerto |
| Gasto (subtítulo) | US$ 2.000 |

## As linhas de base

| Linha de base | Modelo | Temperatura | Tentativas | Gatilho da nova tentativa |
|---|---|---|---|---|
| Zero-shot | GPT-3.5; GPT-4 | — | 1 | — |
| Retry | o mesmo a cada vez | 0 | até 5 | falha nos testes do enunciado |
| Warming | o mesmo a cada vez | de 0 a 0,5, subindo a cada tentativa | até 5 | falha nos testes do enunciado |
| Escalation | Llama-3 8B → GPT-3.5 → Llama-3 70B → GPT-4 | — | um degrau por falha | falha num caso de teste |

| Detalhe | Fato |
|---|---|
| Entrada do zero-shot | descrição do problema; testes de exemplo do HumanEval |
| Arquitetura de agente no zero-shot | nenhuma |
| Razão do retry | modelo não determinístico mesmo a temperatura 0 |
| Testes de avaliação no gatilho | nunca (vazamento) |
| Papers que comparam com retry, warming ou escalation | nenhum que os autores conheçam |

## Custo e acerto comparados (só o que o texto escreve)

| Comparação | Fato |
|---|---|
| Agentes contra as linhas de base simples | sem ganho de acerto; custo maior |
| Faixa de custo para acerto parecido | quase duas ordens de grandeza |
| Warming contra o melhor agente | diferença de acerto não significativa |
| Reflexion e LDB contra o warming | mais de 50% mais caros |
| LDB usado nessa conta (nota 10) | LDB (Reflexion, GPT-3.5), o de melhor resultado no paper do LDB |
| LATS contra o warming | mais de 50 vezes mais caro |
| Origem desses custos | GPT-4, toda ou quase toda |
| Estabilidade das razões se o preço mudar | sim, pela origem acima |
| Escalation contra o LDB (GPT-3.5) | acerto estritamente maior; menos da metade do custo, a preços de então |
| Custo concreto nos papers dos agentes | nenhum; só discussão abstrata (nota 9) |
| Primeira vez no HumanEval, para os autores | Retry, Warming, LDB (GPT-4), LDB (GPT-4 + Reflexion) |
| Posição desses quatro | os de maior acerto |
| Pergunta do começo do post | +2% de acerto por 100× o custo compensa? |
| Linhas de base mais baratas, na lista inicial | até 50×, em alguns casos |
| Tempo de execução contra acerto (nota 8) | mesma conclusão; no apêndice |

## A reprodução

| Agente | Publicado | Reproduzido |
|---|---|---|
| LDB (Reflexion, GPT-3.5) | 95,1% | máximo de 91,5% nas 5 execuções |
| LATS | 94,4% | máximo de 91,5% nas 5 execuções |
| GPT-4 sozinho, no paper do LDB | 75,0% | média de 89,6% nas 5 execuções, com o código do paper |
| GPT-3.5 sozinho, no paper do LDB | 73,9% | — |
| GPT-3.5 sozinho, com os prompts do paper do LDB | — | 73,9% |
| GPT-4 sozinho, com os prompts do paper do LDB | — | 89,6% |
| LDB (GPT-3.5 + Reflexion), nota 16 | — | 88,9% |
| LDB (GPT-4 + Reflexion), nota 16 | — | 92,9% |
| LATS, efeito de checar só parte dos testes de cada problema | — | 3 pontos (média das 5 execuções) |

| Ponto | Fato |
|---|---|
| Risco da linha de base fraca, para os autores | ganho inflado atribuído à arquitetura |
| Testes do LATS por problema | só uma parte dos casos do HumanEval |
| Hiperparâmetros do LATS | ausentes do paper e do repositório |
| Problemas do HumanEval sem teste de exemplo | 3 de 164 |
| Reflexion | remove os 3 |
| LATS | remove os 3 e mais 1 (motivo não reportado no paper) |
| O que o paper do LATS afirma | uso dos 164 problemas (incorreto, para o post) |
| LDB | acrescenta testes aos 3 |
| Algum dos três papers relata a mudança | não |
| Motivo do LATS, por correspondência (nota 17) | erro de execução em casos de teste de um problema |

## O LDB, o GPT-3.5 e o post do Ng

| Ponto | Fato |
|---|---|
| Gerador declarado no paper do LDB para o Reflexion, segundo o post | GPT-3.5 (citação abaixo) |
| Gerador do programa usado, segundo o post | GPT-4, no repositório do Reflexion |
| Papel do GPT-3.5 no LDB | depurador |
| Números do post do Ng, como o post os cita | GPT-3.5 zero-shot 48,1%; GPT-4 zero-shot 67,0%; GPT-3.5 em laço de agente até 95,1% |
| Agente por trás do 95,1%, para o post | parece ser o LDB; o post não crava |
| Placar do Papers With Code para o HumanEval | mesma afirmação |
| Origem de 48,1% e 67,0%, para o post | parecem copiados do relatório técnico do GPT-4, de março de 2023 |
| Versões dos modelos desde então | atualizadas muitas vezes |
| Efeito, para o post | ganho do agente muito superestimado |

## Notas de rodapé sobre o LDB e a resposta dos autores

| Nota | Assunto | Fato |
|---|---|---|
| 1 | AgentCoder, primeiro do placar | fora: sem código nem dados para reproduzir |
| 4 | escolha dos agentes | placar do Papers With Code, só com código aberto; Reflexion incluído pelos 91% reportados |
| 5 | versão do HumanEval | a modificada dos autores do LDB, em tudo |
| 14 | de onde vieram as sementes do Reflexion | soluções publicadas no repositório original, sem rodar o Reflexion de novo |
| 14 | causa possível da diferença | o código gerado pelo Reflexion |
| 14 | juízo dos autores do post | reaproveitar é razoável para medir a depuração; o erro é tomar o acerto final como avaliação para uso |
| 15 | GPT-4 a 75,0% no paper do LDB | autores do LDB reconhecem; vão atualizar os resultados |
| 16 | depurador testado no paper do LDB | só o GPT-3.5 |
| 16 | GPT-3.5 contra GPT-4 depurando sementes do Reflexion | 88,9% contra 92,9% |
| 19 | GPT-3.5 como gerador do Reflexion | autores do LDB reconhecem; vão atualizar o paper |
| 18 | "164 problemas" do LATS | autores do LATS reconhecem; vão atualizar o paper |
| Agradecimentos | quem comentou a versão anterior do post | Zilong Wang (LDB), Andy Zhou (LATS), Karthik Narasimhan (Reflexion) |

## Outras ressalvas das notas

| Nota | Assunto | Fato |
|---|---|---|
| 2 | placar de modelos | outros problemas (manipulação); o argumento não vale necessariamente |
| 3 | onde computação sem limite ajuda | verificação fácil: testes de código, teoremas, parte das tarefas na web |
| 12 | versões de modelo dos papers | checagem com junho de 2023 |
| 13 | limites do HumanEval | 164 questões; nenhuma tarefa real; contaminação possível |
| 13 | benchmark mais rigoroso | SWE-bench |

## Avaliar o modelo ou avaliar para uso

O post separa dois propósitos da avaliação: quem desenvolve o modelo quer saber que mudança nos dados ou na arquitetura melhora o acerto, pergunta científica em que vale controlar a computação e deixar o dólar de lado, enquanto quem monta um produto quer escolher o que comprar, e aí o custo em dólar, inclusive a queda dele com o tempo, é o próprio objeto da medida. Nesse segundo uso, trocar o dólar por um substituto engana: no Anyscale, o Mixtral 8x7B custava o dobro do Llama 2 13B, e o gráfico da Mistral, que só contava os parâmetros ativos, mostrava os dois com custo quase igual.

## O que a fonte recomenda

Para quem escolhe agente para um produto, a medida que importa é o custo em dólar ao lado do acerto, numa curva de Pareto, com a contagem de tokens de entrada e saída publicada para refazer a conta com o preço do dia; proxy como número de parâmetros engana, e o exemplo é o gráfico do Mixtral. Antes de creditar planejamento, reflexão ou depuração, compare com retry, warming e escalation. E nenhum benchmark substitui um conjunto de dados do próprio domínio ou um teste A/B em produção.

## Citações

- "In particular, across all 5 runs for LDB (Reflexion, GPT-3.5), the maximum accuracy was 91.5%, much lower than the 95.1% reported in the paper." (seção da reprodução, com a nota 14)
- "For Reflexion, we select the version based on GPT-3.5 and utilize the corresponding generated programs published in the official Github repository." (frase do paper do LDB, como o post a cita)
- "However, as we discussed above, for LDB, GPT-3.5 is only used to find bugs." (parágrafo sobre o post do Ng)

## Lacuna

- O texto não traz o acerto nem o custo de cada agente em número (estão nas figuras e no apêndice, não lidos); dos agentes reproduzidos, só escreve o máximo do LDB e do LATS e os valores das notas.
- Não diz qual versão do paper do LDB foi lida nem a data da citação; dos autores do LDB, os agradecimentos registram o retorno de Zilong Wang sobre um rascunho anterior do post, mas o post não data esse retorno nem a promessa de atualizar o paper (notas 15 e 19).
- Não diz em dólar quanto custou cada agente nem como os US$ 2.000 do subtítulo se repartem.
- A nota 16 dá 88,9% e 92,9% sem dizer se são médias ou máximos.

## Detalhe da conferência lado a lado

Total de 31 unidades: 10 frases de prosa (1 em "Em uma frase", 2 em "Avaliar o modelo ou avaliar para uso", 3 em "O que a fonte recomenda", 4 na lacuna) e 21 células com texto corrido. Na medição, 3: a da versão do HumanEval, a da checagem de robustez e a do resultado nos outros benchmarks. Na tabela de custo, 5: agentes contra linhas de base, o LDB usado na conta, a escalation, o custo nos papers e a pergunta do começo do post. Na reprodução, 2: a do risco da linha de base fraca e a do LATS que remove um problema a mais. Na seção do Ng, 3: a do agente por trás do 95,1% e a da origem de 48,1% e 67,0%, que levam o "parece" do post, e a do efeito. Nas notas, 8: a da nota 1, a da nota 4, as duas de texto da nota 14 (de onde vieram as sementes e o juízo), as das notas 15, 19 e 18 e a da nota 2. Ficam fora, como fato, as demais células, entre elas a razão do retry, o motivo do LATS, as versões dos modelos, a causa possível da nota 14 e a da nota 3, que trazem uma afirmação só.

Seguem uma frase da fonte 25: as 21 células de texto, que condensam cada uma a frase (ou as duas frases seguidas) de onde vêm; as 2 frases de "Avaliar o modelo ou avaliar para uso" (a primeira funde as frases da distinção entre os dois propósitos, na ordem do post; a segunda, as do exemplo do Anyscale); e 2 frases de "O que a fonte recomenda" (a das linhas de base simples, que traduz a frase sobre os papers que não as testam, e a do conjunto de dados próprio, que traduz a frase do fecho). Não seguem 6: a frase de "Em uma frase" e a primeira de "O que a fonte recomenda", que juntam lugares diferentes do post (a lista inicial, a seção de custo, a de proxies, a de reprodução), e as quatro da lacuna, que dizem o que falta.

Sequências na ordem da fonte (unidades seguidas da ficha cujas frases andam para a frente, a até umas doze frases de distância): a maior é de 4, as células da nota 14 (sementes e juízo), da 15 e da 19; há uma de 3, as três células de texto da seção do Ng (o agente do 95,1%, a origem dos números e o efeito, que andam para a frente no parágrafo sobre o post dele); há pares (as duas frases de "Avaliar o modelo ou avaliar para uso"; versão do HumanEval e checagem de robustez, nas notas 5 e 12; risco da linha de base fraca e LATS, na reprodução; notas 1 e 4), e as demais unidades voltam no post em relação à anterior, porque a ficha agrupa por tema (medição, linhas de base, custo, reprodução, notas) e não segue a ordem do texto.
