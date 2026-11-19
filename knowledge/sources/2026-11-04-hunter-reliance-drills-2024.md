---
titulo: "Monitoring Human Dependence On AI Systems With Reliance Drills"
tipo: paper
autor: "Rosco Hunter (University of Warwick), Richard Moulange (University of Cambridge), Jamie Bernardi, Merlin Stein (University of Oxford)"
url: "https://arxiv.org/abs/2409.14055"
publicado_em: 2024-09-21  # v1; a versão lida é a v5, de 2024-11-28
capturado_em: 2026-11-04
licenca: "CC BY 4.0 (indicada na página do arXiv, arxiv.org/abs/2409.14055, que liga a creativecommons.org/licenses/by/4.0/); o integral está na url"
areas: [agent-engineering]
tags: [reliance-drill, over-reliance, human-oversight, automation-bias, seeded-errors, risk-management, phishing-simulation, proposal-paper]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Lido no PDF da v5 (12 páginas), em 2026-11-04.

## Que tipo de texto é

É uma proposta conceitual, sem experimento e sem dado: o artigo define uma prática, discute por que e como adotá-la e dá dois cenários hipotéticos (e-mail médico, operador militar). O único desenho empírico que aparece é um ensaio que os autores sugerem que outros façam (apêndice B). O PDF traz na primeira página "Preprint. Under review." O PDF e a página do arXiv não dizem se o texto foi apresentado em alguma oficina ou conferência.

## O conceito

Os autores partem de uma definição de dependência excessiva que compara com o que a pessoa faria sozinha: o usuário depende demais da IA quando tenta seguir uma orientação dela num problema que resolveria melhor por conta própria. Quem aplica o conceito precisa dizer, para a sua tarefa, qual solução conta como mais eficaz (o exemplo é uma IA mais precisa porém menos robusta que o humano).

O "reliance drill" é o exercício que baixa de propósito a qualidade da ajuda de um sistema real e observa se o usuário a segue. A ajuda é alterada sem aviso para conter um erro deliberado; passa no teste quem reconhece e rejeita o erro, e é sinalizado como possível dependente quem não o faz. Um segundo termo proposto na nota é "simulated AI hallucinations".

Duas formas de produzir o erro: edição manual da resposta, que não escala, ou um prompt de sistema adversário que manda o modelo errar. A tabela 1 mostra o GPT-4o Mini, com esse prompt, trocando a resposta certa de uma questão de cardiologia (alternativa c, comunicação interatrial) pela alternativa a (estenose aórtica), com uma explicação curta e convincente; sem o prompt ele costuma acertar.

## O que os autores dizem sobre as medidas que já existem

Não haveria método universal de medir dependência excessiva. As medidas citadas são contar quantas sugestões incorretas o usuário aceita e a frequência com que ele muda a resposta para igualar a da IA. A crítica é que várias dessas medidas não comparam o desempenho da pessoa com e sem a ajuda, e a definição acima tenta aproximar esse efeito marginal. A nota 5 limita o alcance: o exercício mede só se o usuário identifica erros num texto supostamente gerado por IA, uma parte estreita do fenômeno.

## Por que uma organização faria o exercício

Três incentivos, todos como hipóteses: financeiro (seguradoras dão prêmio menor a quem tem gestão de risco forte, e fornecedores podem ser responsabilizados), reputacional (garantia de que a IA ajuda e não atrapalha) e legal (o artigo 14 da lei de IA da União Europeia pede que sistemas de alto risco sejam projetados atentos à tendência humana de confiar automaticamente na saída). A analogia é a simulação de phishing, em que funcionários recebem golpes falsos: equipes internas em organizações grandes, especialistas externos em pequenas, com relatório de segurança. Os autores a descrevem como um modelo de negócio possível e dizem que o paralelo é imperfeito.

## O processo em cinco passos

1. Decidir como prejudicar a IA. O erro não pode ser óbvio demais nem pequeno demais para revelar a dependência. Dois exemplos de prioridade: tarefa de respostas perfeitas, em que um erro mínimo já basta; tarefa com tempo crítico, em que o gestor fixa de forma subjetiva o ponto a partir do qual a imprecisão supera o ganho de velocidade. Sem um limiar prévio, o investigador pode aplicar erros de intensidades variadas: os leves dão sinal fraco e os evidentes, sinal forte.
2. Avaliar o risco, ponderando realismo e segurança. O máximo de realismo interrompe a rotina sem aviso; o mínimo de risco usa um ambiente de teste. A escolha depende da confiança em poder encerrar o exercício antes de causar dano; essa confiança cai com pressão de tempo, decisões abertas ou irreversíveis e poucos dispositivos de segurança. Medidas citadas: o gestor decide em segredo o momento para não coincidir com uma emergência, ou o profissional pode suspender os exercícios. Comando e controle nuclear é o exemplo em que o risco é sempre alto demais e só se treina em ambiente dedicado.
3. Conduzir o exercício (aparece só no diagrama da figura 2, sem texto).
4. Monitorar danos colaterais: conferir que o usuário rejeitou o conselho falho e, se não, corrigir o dano; vigiar saúde mental e moral (ansiedade de poder ser enganado a qualquer momento); evitar a lição errada (reação exagerada que vira subdependência) e a fuga para IAs externas sem monitoramento. Medida citada: reunião de esclarecimento depois de cada exercício.
5. Corrigir a dependência de forma gradual: primeiro um aviso, depois um "Reliance Safety Course" com estratégias de vigilância (listas de verificação, reflexão guiada); se o problema for geral, mudanças institucionais, como mais salvaguardas ou explicações do raciocínio da IA, ou até retirar a IA.

## Exemplos aplicados

Médicos que usam uma IA para redigir respostas por e-mail a pacientes: a precisão tem prioridade; em casos raros (o exemplo é um em mil e-mails) o modelo é instruído a inserir uma pequena informação médica incorreta; o envio ficaria bloqueado durante o exercício, e o médico poderia suspendê-lo diante de urgência; quem tenta enviar o e-mail com erro é sinalizado. O esclarecimento deve dizer que a IA nem deve ser descartada nem aceita às cegas.

Operadores militares de comando e controle: exercícios só em ambiente de treino, com erros de gravidade variada, de leves a potencialmente letais, e longos para simular vigilância prolongada; no esclarecimento, lista de serviços de saúde mental; na correção, uma lista de verificação.

## Apêndice B: o ensaio sugerido (não realizado)

Ensaio controlado aleatório com 150 estudantes de medicina ou mais, cada um respondendo 50 a 100 questões difíceis de múltipla escolha em uma hora. Três grupos: controle sem IA; IA com ajuda pré-gerada que às vezes carece de informação que o estudante tem; IA com a mesma ajuda mais o exercício, em que, em uma ou duas questões sem nota, a orientação é alterada para errada e o participante recebe retorno antes de seguir. Uma nota admite um quarto grupo com as mesmas questões erradas e sem retorno. Duas comparações propostas: quantas questões o grupo sem IA acerta a mais que cada grupo com IA (nível de dependência, com teste estatístico, na análise por intenção de tratar, que poderia ser complementada por autorrelato de quanto cada um usou a IA) e o desempenho geral entre os grupos 2 e 3, para ver se alguém passou a desconfiar demais (se o grupo 3 for pior, sinal de subdependência).

## Apêndice C: a dependência além do excesso

Subdependência é não aproveitar o desempenho superior da IA (rejeitar um diagnóstico certo dela, por exemplo). A figura 3 cruza três situações do conselho (melhor, parecido ou pior que a resposta que o humano daria) com a reação do humano; os autores indicam que se poderia randomizar por colunas ou por linhas desse quadro e citam uma única métrica, de outros autores, que mediria as duas dependências, dizendo que falta pesquisa para aplicá-la.

## Apêndice A: termos vizinhos

O apêndice relaciona, sem aprofundar: viés de automação (confiança excessiva nas decisões automatizadas, mais forte em situações complexas ou com limite de tempo), design centrado no humano (computadores que estimulem a pausa e a reflexão), IA explicável e supervisão humana obrigatória em decisões críticas. Dizem que nenhum virou um teste padronizado que a organização use para monitorar a dependência.

## O que a fonte não traz

Nenhum dado de campo ou de laboratório; nenhuma regra para a frequência dos exercícios além do exemplo de um em mil e-mails; nenhuma indicação de quantos erros plantar, de quão sutis, nem de que proporção de acertos ou alarmes falsos seria sinal de dependência.
