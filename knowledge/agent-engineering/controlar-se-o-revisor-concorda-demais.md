# Controlar se quem revisa concorda demais: item plantado, releitura e o que dá para medir com poucos casos

Como medir se a pessoa que confere a saída de um avaliador (ou de um conjunto de modelos) concorda demais com ela: item plantado, releitura às cegas e o que se conclui com poucos casos. Que a pessoa ancora, e o efeito de julgar antes, estão em [[camadas-de-avaliacao-o-que-melhora-cada-arranjo]] (seção 4) e [[quem-le-a-saida-do-avaliador]]; aqui fica o instrumento de medida. Quem decide o gabarito: [[gabarito-quando-o-responsavel-tem-duvida]].

Convenção: "leitura nossa" liga a fonte a um ambiente de agentes ou é conta nossa. "(resumo)" é número lido só no resumo oficial; "só citação" é texto fechado; "sem ficha" é texto aberto e lido, que não virou arquivo na base. Beck, Berger, Hunter e BAT-RM são preprints.

## A resposta curta

- **A medida padrão pede saber o que está errado:** concordância com a recomendação errada. Vale lê-la ao lado da adoção da certa, senão ela premia só a desconfiança (leitura nossa).
- **Plantar é documentado, e para alarme falso em revisor único não está validado.** Nada lido trata de quem revisa sem colegas para comparar, nem compara plantar com as alternativas.
- **Poucos plantados testam "aceita tudo", não medem uma taxa.** Contra uma referência em que quase tudo é aceito, dez bastam para isso, e uma aceitação real de 70% a 80% escapa em 38% a 68% das vezes. Contra uma referência de aceitação mais baixa, dez só pegam aceitação real perto de 30% ou menos (contas nossas).
- **Reler às cegas mede estabilidade, não concordância excessiva.** Soma-se a um controle.
- **Concordar muito nem sempre é ruim:** depende de quem é mais preciso, a pessoa ou a máquina.

## 1. As medidas

- **Concordância com a recomendação errada** = aceitos sobre erros mostrados; "switch fraction" = quantas vezes a pessoa troca a resposta pela da IA ([[2026-11-04-passi-vorvoreanu-aether-overreliance-2022]]). A revisão de 35 estudos da AI & Society (2025) a dá como a mais usada ([[2026-11-04-automation-bias-human-ai-collaboration-revisao-2025]]).
- **Definição mais exigente** (Hunter 2024): seguir o conselho num problema que a pessoa resolveria melhor sozinha, o que pede o contrafactual. [[2026-11-04-hunter-reliance-drills-2024]]
- **Detecção de sinal:** Langer 2024 chama de sinal o erro da saída, e Berger 2026, o conselho certo; os sinais do critério se invertem, então vale dizer qual se usa (leitura nossa, [[2026-11-04-langer-effective-human-oversight-2024]]). Taxas de 0 ou 1 quebram a conta, e são comuns com poucos ensaios; há correções, sem regra de n mínimo ([[2026-11-04-stanislaw-todorov-sdt-measures-1999]]).
- **Tempo na tela não indica:** r < 0,04 com o acerto (Beck 2025, n = 2.784). [[2026-11-04-beck-bias-in-the-loop-2025]]

## 2. Plantar: o que se sabe

- **Proposta sem dado:** o "reliance drill" de Hunter planta o erro às escondidas e mede se a pessoa o recusa; não pode ser óbvio demais, e a própria proposta lista riscos: ansiedade, excesso de correção, burlar o exercício.
- **O tipo muda tudo** (Beck): correção de 31% a 82% conforme o tipo de erro; 21% num caso em que a sugestão estava certa e parecia errada. Os três primeiros itens não mudaram os seguintes.
- **A TIP, em aeroportos, é a analogia mais forte, com limite.** Projeta ameaças em imagens de raios X. Previu testes encobertos (1.184 testes de 474 operadores), "medida válida" segundo o estudo; cerca de 100 eventos por pessoa dão confiabilidade de 0,7 quando a taxa média de acerto fica abaixo de 0,9 (728 operadores, 1,2 milhão de eventos, resumo, só citação, Transportation Research Part A 200: 104640, com errata não lida). Mas 34% das imagens têm artefato ou cenário irreal, e operadores reconhecem algumas; os autores concluem que ela "ainda serve ao propósito" ([[2026-11-04-riz-porta-tip-realism-2022]]). Ela planta ameaça verdadeira, e os 100 eventos são para distinguir operadores numa população (leitura nossa). Hofer e Schwaninger 2005 (sem ficha, https://doi.org/10.2495/SAFE050411) usaram bagagens inofensivas projetadas para estimar a taxa de alarme falso de cada operador. A confiabilidade da taxa de acerto foi baixa com acerto muito alto (0,19 em um mês, 0,33 em sete) e alta com acerto menor (0,70 em um mês, 0,94 em dezesseis); a da taxa de alarme falso não foi calculada.
- **Taxa de plantio sem regra:** de 0,1% (Hunter, exemplo) a 57% (Beck, desenho), nenhuma validada.
- **Reconhecer o item de controle:** Checco 2018 mostra um ataque coletivo, entre trabalhadores que compartilham páginas; com um revisor só, esse mecanismo não existe, e o risco que sobra é o da forma repetida (leitura nossa). [[2026-11-04-checco-gold-questions-attack-2018]]
- **Plantar pode mudar quem responde:** a base liga alarme falso à perda de confiança ([[quem-le-a-saida-do-avaliador]]). Nada lido isola esse efeito em dose baixa.

## 3. O que dá para concluir com poucos (contas nossas, binomial exata, IC 95%)

| Plantados aceitos, de 10 | Intervalo |
|---|---|
| 0 | 0% a 31% |
| 1 | 0,25% a 44,5% |
| 5 | 18,7% a 81,3% |
| 9 | 55,5% a 99,75% |

Exemplo com duas referências possíveis de aceitação de base: a resposta final de quem revisa, depois de ver as leituras dos modelos (no exemplo, cerca de 95% aceitos), e a primeira resposta, antes delas (cerca de 60%).

| Referência | Corte em 10 plantados | Chance de pegar, com aceitação real de |
|---|---|---|
| Resposta final, cerca de 95% aceitos | 7 ou menos (0,86%; com 8 ou menos, 7,15%) | 50%: 94,5%; 70%: 61,7%; 80%: 32,2% |
| Primeira resposta, cerca de 60% aceitos | 3 ou menos (4,99%) | 10%: 98,7%; 30%: 65%; 50%: 17,2% |

- **A referência decide:** a final é a resposta dada depois de ver as leituras, e o valor real fica entre as duas.
- **Supõe itens trocáveis,** e Beck mostra que o tipo importa. Outra forma de ler: 8 plantados bastam para dizer "abaixo de 50%" quando o real é 10% (poder de 81%).

## 4. Sem plantar

- **Gravar o juízo antes do apontamento:** uma mesa que mostra o ponto em questão antes da primeira resposta é cega às leituras dos modelos, mas não ao apontamento. É o viés de incorporação de Kellerhuis: a recomendação externa, por cautela, é não mostrar, e esconder também pode piorar ([[gabarito-quando-o-responsavel-tem-duvida]]). Gravar antes pede outra tarefa, ler a peça sem o ponto.
- **Concordância alta sem controle não decide nada:** quando a resposta final de quem revisa coincide quase sempre com a de um modelo, isso é compatível tanto com ancoragem quanto com o modelo acertar (leitura nossa). E uma quebra de cegueira (a leitura de um modelo aparecer antes, por outro canal) contamina o caso.
- **Julgar sem se ver:** quando pessoa e IA julgam separadas e um segundo humano desempata, o resultado supera a IA como conselheira nos 10 conjuntos (de 0,2 a 6,6 pontos; 4,45 no agregado; 1.229 pessoas, mais de 41 mil julgamentos), sem ganho prático num deles. Foi calculado por permutação de julgamentos já coletados, não rodado, e depende do desempatador. [[2026-11-04-berger-independent-aggregation-2026]] Esse desenho exige o juízo independente e o segundo humano que um revisor único não tem (leitura nossa).
- **Reler às cegas depois de um intervalo:** BAT-RM usou 4 semanas, escolhidas por piloto de 3 leitores, e admite que recordação parcial não se exclui; é estudo de traçado automático de tumor em radioterapia, de que só se aproveita o intervalo. [[2026-11-04-bat-rm-auto-contorno-estudo-de-leitores-2026]] Mede repetição, e quem concorda demais pode concordar de novo (leitura nossa). Dados de repetição: o mesmo anotador, dois meses depois, reencontra o erro em 29,3% e repete a gravidade em 16,9% ([[defeitos-no-lugar-da-nota]]); mesmos avaliadores, dois dias depois, r perto de 0,5 ([[2026-11-04-sauro-problemas-graves-aparecem-primeiro-measuringu-2013]]).
- **Rótulo de origem também ancora:** avaliadores preferiram o texto rotulado "humano" por mais de 30%, inclusive com rótulos trocados (Zhu 2025, ACL Findings, sem ficha, https://aclanthology.org/2025.findings-acl.1329/). Por isso, esconder a origem não prova que a pessoa concorda demais (leitura nossa).

## 5. Quando concordar muito não é o problema

Berger: as pessoas discriminam mal o conselho certo do errado, e, se a IA é mais precisa que a pessoa, um viés para aceitar pode render mais; com outras combinações de acurácia, a situação se inverte. Sem saber quem é mais preciso no caso, a concordância alta não é diagnóstico (leitura nossa).

## Contradições e não verificado

- Primeiro erro: Beck não acha efeito; Kim 2023 (ACM TOCHI 30(1), só resumo da busca, não verificado) acha, em outra medida.
- Faixas de plantio afirmadas sem fonte, não verificadas: Gemini (5% a 10%), Perplexity (20%), Koji (25% a 30%, blog de fornecedor).
- Mills 1972 (defect seeding) não abriu; o estimador está em McConnell 1997 (IEEE Software, sem ficha), e Knight e Ammann 1985 (NASA, resumo, só citação) dá apoio misto à ideia de que o semeado é tão achável quanto o real.
