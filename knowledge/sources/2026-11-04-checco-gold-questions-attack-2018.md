---
titulo: "All That Glitters Is Gold -- An Attack Scheme on Gold Questions in Crowdsourcing"
tipo: paper
autor: "Alessandro Checco (University of Sheffield), Jo Bates (University of Sheffield), Gianluca Demartini (University of Queensland)"
url: "https://cdn.aaai.org/ojs/13332/13332-64-16849-1-2-20201228.pdf"
publicado_em: 2018  # Sixth AAAI Conference on Human Computation and Crowdsourcing (HCOMP 2018); o PDF traz só o ano
capturado_em: 2026-11-04
areas: [agent-engineering]
tags: [gold-questions, crowdsourcing, quality-assurance, attack-scheme, collusion, honeypots, hidden-control-items, simhash, worker-surveillance]
licenca: "Copyright 2018, Association for the Advancement of Artificial Intelligence, 'All rights reserved' (primeira página do PDF); só ficha em palavras próprias, com passagens curtas literais"
---

# Checco, Bates e Demartini (HCOMP 2018): um ataque coletivo às perguntas de ouro

Ficha em palavras próprias, lida no PDF do AAAI em 2026-11-04. O mecanismo que o artigo estuda é coletivo, entre trabalhadores de microtarefas: um grupo de trabalhadores que colaboram, e não um revisor individual, descobre quais perguntas de uma tarefa provavelmente são de controle. O texto descreve a ferramenta, um modelo teórico de desempenho, uma simulação sobre dois conjuntos reais de dados, contramedidas e implicações sociais.

## O problema de que parte

O controle de qualidade mais comum em microtarefas pagas é o conjunto de "perguntas de ouro": poucas tarefas cuja resposta o solicitante já conhece, usadas para medir a qualidade do trabalho. Seguindo Oleson et al. (2011), o conjunto deveria ter cinco propriedades: ser pequeno (as respostas certas custam e os trabalhadores precisam ser pagos por responder a algo que não gera informação nova), ter pouca repetição de exposição, ter respostas objetivas e sem ambiguidade, ter distribuição equilibrada entre as respostas possíveis e ser semelhante em forma e conteúdo às demais perguntas. O primeiro item contraria os outros; daí a Suposição 1: o conjunto de ouro é bem menor que o de perguntas sem ouro. Suposição 2: cada pergunta de ouro é sorteada uniformemente do conjunto e mostrada uma vez por trabalhador.

## O ataque

Um plugin de navegador (ou bookmarklet) em cada trabalhador conivente cria uma impressão digital (simhash) de cada tarefa na tela: remove identificadores do trabalhador e etiquetas de sessão, separa a página em tarefas, divide o HTML em trigramas e gera o simhash, de modo que o conteúdo da tarefa não circula e perguntas quase iguais (captchas, aritmética, ouro gerado por programa) agrupam. O par (ID do trabalho, simhashes) vai a um servidor externo, que mantém trios (trabalho, simhash, multiplicidade) e agrupa por distância de Manhattan.

Se as suposições valem, a multiplicidade dos grupos tem distribuição bimodal, e as perguntas de ouro têm multiplicidade média maior. Uma mistura gaussiana de dois componentes dá a probabilidade de cada pergunta ser de ouro. O plugin fica em estado ocioso (qualquer pergunta pode ser de ouro) até haver amostras suficientes (30, cinco vezes o número de parâmetros) e o critério de informação bayesiano preferir o modelo de dois componentes sobre o de um. A ferramenta não revela a resposta, só a probabilidade de ser ouro. O trabalhador escolhe o limiar de confiança, pesando que o falso positivo custa trabalho a mais e perder uma pergunta de ouro pode derrubar seu índice de aprovação; por isso se prioriza recall à precisão. Uma versão sem servidor central (banco de dados distribuído de acréscimo apenas) é descrita. O plano é um alerta tipo semáforo, como o TurkOpticon.

## O modelo teórico

Configuração de referência: 2.000 tarefas e mais 5% (100) de perguntas de ouro; página de 10 tarefas com 9 pedidas e 1 de ouro, mais uma página inicial de teste com 10 perguntas de ouro (padrão da CrowdFlower); o trabalhador só é considerado confiável se responder no mínimo quatro perguntas de ouro e atingir 70% de acerto; cada tarefa sem ouro vai a 3 trabalhadores; no máximo 9 páginas por trabalhador, 100 perguntas de ouro únicas. No caso mais conservador (cada trabalhador faz só 10 tarefas), depois de 50 trabalhadores a probabilidade de reconhecer uma pergunta de ouro supera 99,9%. Com mais de 16% de ouro e média de 30 questões por trabalhador, a probabilidade fica abaixo de 20% mesmo com 25% do trabalho concluído. As próprias autoras avisam que são suposições simplificadas, e que o engajamento real segue uma lei de potência.

## Os dados reais e a simulação

Duas rodadas reais do repositório CSTA (Benoit et al., 2016), na CrowdFlower: (1) 29.594 julgamentos de 336 trabalhadores, 2.700 perguntas únicas, 12,4% de ouro, página de teste com 10 perguntas (8 de ouro) e depois páginas de 10 com 1 de ouro, cada pergunta sem ouro com 10 julgamentos e média de 8,7 páginas por trabalhador, escolhida por ser difícil para o ataque; as perguntas de ouro eram indistinguíveis das demais em forma, e todos os simhashes da mesma pergunta ficavam a menos de 2 bits de distância; (2) 76.183 julgamentos de 230 trabalhadores, 13.371 perguntas, 4,3% de ouro, 5 julgamentos por pergunta. Para não interferir em trabalho real, rodaram o plugin sobre o HTML reconstruído dos logs, subamostrando a fração de ouro (0% a 12,4%) e o número de julgamentos (4 e 10).

Premissas do trabalhador na simulação (pior caso): só gasta tempo nas perguntas sinalizadas (g vezes o tempo da página); responde ao acaso a uma pergunta de ouro que o plugin não sinalizou; responde às sinalizadas como nos logs; considera de ouro o que tiver probabilidade de pelo menos 50%.

Resultados: nos conjuntos com 4,4% ou 12,4% de ouro, a acurácia média dos trabalhadores ficou sempre acima de 70%, o limite de rejeição; com poucas perguntas de ouro ou poucos julgamentos, depois da fase de transição, o trabalhador faria a tarefa em um quinto do tempo (cerca de 2 perguntas por página) sem perda relevante de acurácia; o número de julgamentos por pergunta sem ouro não mostrou tendência na acurácia. Na segunda rodada, a acurácia caiu 4% e o tempo, cerca de 50%. O texto conclui que o sistema "can completely disrupt the gold set paradigm for quality control" (pode desmontar por completo o paradigma de ouro para controle de qualidade). Se só M de N trabalhadores colaboram, o efeito equivale ao de todos colaborarem em M/N do lote.

## Contramedidas discutidas

- Aumentar o conjunto de ouro: passar de 4,4% para 12,4% custaria 54% a mais do custo de coleta, tomando salário mínimo como referência.
- Aumentar julgamentos por pergunta: efeito limitado, custo adicional.
- Reter trabalhadores prolíficos: reduz a força do ataque (menos avaliações iniciais e menos repetição de ouro) e pode melhorar a qualidade por efeitos de aprendizado.
- Seleção não uniforme do conjunto de ouro, que levaria em conta a sequência já mostrada.
- Ouro gerado por programa, sempre diferente e com simhashes distantes, o que eleva o custo de projeto.
- Controles adicionais, como punir quem responde rápido demais, que podem multiplicar as "presas de ouro": trabalhadores corretos reprovados por serem mais rápidos que a média.

## Implicações sociais e econômicas

Os autores comparam o regime de perguntas de ouro ao efeito panóptico do local de trabalho: o trabalhador sabe que pode estar sendo observado a qualquer momento e se autogoverna; a vigilância eletrônica desse tipo se associa a menos confiança na gestão e pior relação de trabalho. Descrevem o plugin como "sousveillance" (vigilância de baixo para cima) e um reequilíbrio parcial de poder, e pedem à comunidade mais transparência, portabilidade de dados e mecanismos coletivos de resolução de disputas, que dispensariam técnicas de controle tão granulares. Trabalhos futuros: otimizar limiares, estudar a robustez com menos trabalhadores colaborando e esquemas de compartilhamento da resposta correta.

## O que a fonte não traz

Nenhum estudo com revisores individuais nem com tarefas de revisão de saídas de IA; nenhuma medida de reconhecimento de itens de controle por quem trabalha sozinho; os resultados vêm de simulação sobre registros de duas rodadas, não de um ataque executado em plataforma real.
