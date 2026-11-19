---
titulo: "Effective Human Oversight of AI-Based Systems: A Signal Detection Perspective on the Detection of Inaccurate and Unfair Outputs"
tipo: paper
autor: "Markus Langer, Kevin Baum, Nadine Schlicker"
url: "https://link.springer.com/article/10.1007/s11023-024-09701-0"
publicado_em: 2024-11-05  # online; Minds and Machines, volume 35, artigo 1 (2025)
capturado_em: 2026-11-04
licenca: "CC BY 4.0 (a página do Springer marca o artigo como 'Open access' e liga a creativecommons.org/licenses/by/4.0/); o integral está na url"
areas: [agent-engineering, psychology]
tags: [human-oversight, signal-detection-theory, error-detection, sensitivity, response-bias, unfairness-detection, eu-ai-act, conceptual-paper]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Lido na página HTML do Springer em 2026-11-04.

## Tipo de texto

Artigo conceitual, sem dado novo: a seção "Future Work" abre dizendo que o trabalho é conceitual e que os próximos passos são testes empíricos. Os autores dizem não conhecer estudo que aplique a teoria de detecção de sinais à detecção de saídas injustas de sistemas de IA, e citam um trabalho (Gentile et al., 2023) que começou a aplicá-la a saídas imprecisas.

## A tese

Supervisão humana eficaz em tempo de uso exige antes detecção confiável de erros, e a teoria de detecção de sinais (SDT) é proposta como o quadro para estudá-la. "Erro" é o termo-guarda-chuva para duas coisas: saída imprecisa (inconsistente com o estado do mundo) e saída injusta (viola um padrão de justiça). A supervisão eficaz seria detecção eficaz somada a intervenção eficaz. Pano de fundo citado: o artigo 14 da lei de IA da UE, e a dúvida da literatura (Green, 2022) sobre se humanos conseguem de fato supervisionar; os autores propõem, em vez de descartar a supervisão, estudar as condições sob as quais ela funciona.

## Por que detectar erro é difícil, segundo o artigo

Quatro processos de manejo de erro em automação imperfeita (McBride et al.): detecção, explicação, correção e integração. Dificuldades listadas, vindas da literatura de automação: capacidades humanas limitadas diante de sistemas em geral melhores que o humano, atenção difícil de manter com sistema quase sempre confiável, expectativa de quase perfeição e perda de habilidade; complacência e viés de automação; aversão a algoritmos (relatar erros que não existem) e apreciação de algoritmos (deixar erros passarem); sobrescrever saída correta; confiar de menos ou demais.

## A SDT aplicada à supervisão

O supervisor transforma as evidências sobre a saída em um valor numa variável de decisão ("evidência de erro"); acima de um critério de resposta, julga a saída errada. Modelo de variância igual, decisões binárias: "sinal" é a saída errada, "ruído" é a saída normal.

- Acerto (hit): dizer que há erro quando há erro. Falha (miss): dizer que está normal quando havia erro. Alarme falso: dizer que há erro numa saída normal. Rejeição correta: dizer que está normal quando está.
- Sensibilidade, d' = z(H) − z(FA) (com citação a Stanislaw e Todorov, 1999): distância entre as distribuições de saídas normais e erradas; quanto maior, mais fácil distinguir.
- Viés de resposta, c = −0,5 × (z(H) + z(FA)): valor mais alto é conservador (exige mais evidência para apontar erro) e mais baixo é liberal.
- Citação central: usar a taxa de acerto sozinha como medida da capacidade de detectar erros ignora que "a higher hit rate is associated with a higher false alarm rate" (uma taxa de acerto maior vem junto com um alarme falso maior). Com d' constante, mover o critério sobe ou desce as duas taxas; só o d' maior melhora a razão entre elas, como mostram as curvas ROC.
- Para a sensibilidade, valor maior é melhor; para o viés, não existe valor "ótimo" em si: critério conservador gera mais falhas e liberal gera mais alarmes falsos, e quando a falha custa mais que o alarme, um viés liberal pode ser melhor.
- Variantes citadas: variâncias desiguais, outras distribuições e tarefas de classificação em escala (por exemplo de 1, "muito confiante de que é normal", a 6, "muito confiante de que é erro"), que dão pontos de uma curva ROC; a nota diz que uma diferença de sensibilidade significativa no modelo de variância igual pode não valer em outro modelo, e indica como estado da arte regressões de nível misto com participantes e estímulos como efeitos aleatórios.

## Detecção de injustiça: o padrão como verdade de referência

Para o cálculo de acertos e alarmes falsos é preciso uma verdade de referência; para imprecisão ela é direta (a lesão é maligna ou benigna), para injustiça é preciso escolher um padrão. Julgamento pode ser agregado (um processo de decisão inteiro, como 57 processos de contratação com número de candidatos e selecionados por gênero, num estudo de Alexander) ou individual (uma decisão sobre um candidato). Padrões discutidos: a regra dos 80% do adverse impact (taxa de seleção do grupo minoritário abaixo de 80% da do grupo mais selecionado: 0,30 contra 0,40 dá razão 0,75; 3 contratadas contra 4 contratados entre 10 e 10 candidatos fere a regra, mas se os supervisores a veriam assim já é outra questão); igualdade de oportunidade, probabilidades equalizadas, justiça contrafactual, justiça por desconhecimento, regras de justiça procedimental, informacional e distributiva (Colquitt) e a teoria do consenso cultural, que estima uma "verdade de consenso" a partir de julgamentos binários e depende da amostra. Os padrões podem ser incompatíveis entre si (Chouldechova); a escolha deve ser deliberada e transparente, e a discussão sobre qual é apropriado é social.

## Fatores que podem afetar sensibilidade e viés (hipóteses, tabela 2)

Sensibilidade, em tarefa: padrão simples ou explícito ajuda; pressão de tempo reduz (Buçinca et al. mostraram que forçar mais tempo de reflexão melhora a detecção de recomendação falha); responsabilização percebida pode melhorar, mas estresse pode prejudicar. Em sistema: confiabilidade alta, ou seja, base baixa de erros, tende a reduzir a vigilância e a sensibilidade (a "ironia da automação" de Bainbridge: sistemas muito bem-sucedidos podem exigir o maior investimento em treino do operador); os autores aventam, como opção controversa, usar de propósito um sistema menos sofisticado para manter o supervisor alerta; nível de automação alto reduz a consciência da situação; transparência e explicações podem ajudar, mas há pouca evidência de que ajudem a detectar injustiça; ferramentas de apoio à supervisão podem ampliar o sinal e trazem os problemas dos auxiliares automáticos (viés de automação, perda de habilidade). Em pessoa: carga de trabalho alta reduz; treino com saídas incorretas ajuda para aqueles erros mas pode não valer para erros não treinados (Bahner et al.); conhecimento do sistema pode ajudar ou, se errado, atrapalhar; capacidade cognitiva maior ajudou num estudo (Alexander).

Viés, em tarefa: o custo relativo de falha e alarme falso empurra o critério; a responsabilização torna salientes as consequências. Em sistema: base alta ou baixa de erros (real ou esperada) move o critério; um auxiliar de supervisão que alerta pouco pode tornar o supervisor mais conservador, e um que alerta muito e é pouco sensível pode fazer o supervisor ignorar os alertas (efeito "cry wolf"; o texto cita Wickens et al. 2009, que não o encontraram em alarmes de controle de tráfego aéreo). Em pessoa: carga alta pode tornar o critério mais conservador, porque apontar erro gera mais trabalho; justiça percebida alta se associa a menos sobrescritas; gênero, valores (sexismo hostil mais conservador, benevolente mais liberal, em estudo de Alexander), orientação política e propensão a confiar em automação (que tornaria o viés mais conservador).

## Trabalhos futuros apontados

Testar os fatores da tabela 2; estender a SDT além do modelo de variância igual binário; estudar outros atores (pessoas afetadas pelas decisões); usar a SDT como quadro integrador de aversão a algoritmos (viés mais liberal depois de ver o sistema errar), apreciação (mais conservador em certos contextos) e viés de automação (mais conservador por expectativas altas); e aplicá-la a auditoria e certificação de supervisão humana.

## O que a fonte não traz

Nenhum dado, nenhum experimento, nenhuma estimativa de quantos ensaios bastam para medir sensibilidade ou viés, nenhuma regra de número mínimo de itens com erro plantado.
