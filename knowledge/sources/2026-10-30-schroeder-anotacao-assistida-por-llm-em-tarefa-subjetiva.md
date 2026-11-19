---
titulo: "Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks"
tipo: paper
autor: "Hope Schroeder, Deb Roy, Jad Kabbara"
url: "https://arxiv.org/abs/2507.15821"
publicado_em: 2025-07-21
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [human-in-the-loop, llm-assisted-annotation, anchoring, automation-bias, human-labels, subjective-vs-verifiable, inter-annotator-agreement, evaluation-bias, label-homogenization]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv 2507.15821 (cs.CY), v1 de 21/07/2025, a única versão (lida), 25 páginas com os apêndices. MIT (Massachusetts Institute of Technology). Nem o texto nem a página do arXiv dizem em que conferência ou revista o trabalho saiu. O integral foi extraído do PDF; as Figuras 1 a 3 (gráficos de barras) e a Tabela 1 foram lidas como imagem. Lida (camadas flexíveis de avaliação).

## A pergunta

Em tarefas de anotação subjetivas, com mais de uma resposta plausível, é tentador só pôr pessoas para "revisar" as anotações de um LLM. Os autores lembram que pessoas sofrem de ancoragem (Tversky e Kahneman, 1974): tendem à primeira opção apresentada, sobretudo se ela é plausível. Então podem confirmar anotações plausíveis do LLM e com isso mudar duas coisas: a avaliação da anotação e o uso que se faz dela depois (a fronteira de decisão de um classificador, a distribuição dos rótulos numa análise de texto).

Perguntas do estudo: com diferentes formas de assistência por LLM, anotadores de multidão "produzem mais" (vão mais rápido) numa tarefa subjetiva complexa, e isso vem com "entender menos" (a expressão é de Messeri e Crockett, 2024)? Acham as sugestões precisas e úteis, e com que frequência as aceitam? Se anotações influenciadas pelas sugestões forem usadas para montar o gabarito (ground truth), o que acontece com o desempenho medido desses LLMs na mesma tarefa? Os autores também liberam um conjunto de anotações humanas e assistidas nos dois livros de códigos.

## Trabalhos relacionados retomados

- LLMs são usados em anotação para baratear o rótulo, inclusive em tarefas subjetivas de ciências sociais computacionais. Li et al. (2023) acharam que o desempenho de modelos treinados com dados sintéticos cai quanto mais subjetiva é a tarefa; o desempenho do LLM anotador varia com o prompt e com a ordem das opções.
- Plataformas de rotulagem com sugestão de IA aumentam a concordância e a convergência em códigos qualitativos (Gao et al., 2023b). Pessoas ancoram nas sugestões de IA, o que muda comunicação e até opinião (Jakesch et al., 2019). Choi et al. (2024): analistas que viram a lista de tópicos do LLM chegaram a listas diferentes das de quem não viu, o que aponta risco de homogeneização.
- Produtividade: resultados mistos. Bughin (2024) vê troca entre produtividade e qualidade em código; Overney et al. (2024) viram usuários com apoio de IA na plataforma SenseMate gastarem mais tempo codificando.

## Dados e livros de códigos

Os dados vêm do corpus Fora (Schroeder et al., 2024), conversas em pequenos grupos, levemente anonimizadas.

- **NYC**: em 2022, o Departamento de Saúde de Nova York, o NYC Public Health Corps e a ONG Cortico reuniram mais de 100 comunidades em 28 conversas sobre recursos comunitários e decisões de vacinação na covid-19. Trabalhadores comunitários criaram o livro de códigos: 7 temas de topo (por exemplo, motivações externas, motivações intrínsecas, papel das organizações comunitárias, hesitação vacinal) e 20 subrótulos. Base principal: 200 trechos.
- **RTFC** ("Real Talk for Change"): série de conversas em Boston em 2021, antes da eleição para prefeito, sobre comunidades marginalizadas. 9 temas de topo e 41 subrótulos (por exemplo, segurança: violência de rua; moradia: custo da moradia). Base de réplica parcial: 200 trechos.
- Trechos com média de 592 caracteres. Os autores tiraram informação pessoal identificável antes de mandar o texto aos modelos e aos anotadores, e tiraram os comentários em espanhol, porque o livro de códigos foi feito em inglês. Há inglês americano padrão e inglês afro-americano, cuja proporção não puderam estimar. Os livros de códigos completos, com definições e exemplos, estão nos Apêndices E e F.

## Método

**Gabarito da multidão:** cada trecho anotado por 5 anotadores distintos por condição; um rótulo entra no gabarito se ao menos 3 dos 5 o marcaram (maioria 3/5). Quando mais de 5 anotaram, 5 foram sorteados; trechos com só 4 anotadores saíram das análises de multidão (3 na linha de base, 7 na Condição 2, 2 na Condição 3, 16 na réplica com Llama).

**As condições** (a interface é a ferramenta aberta Potato):

- **Controle (linha de base):** sem sugestão do LLM.
- **Condição 1, sugestão em texto:** depois do trecho aparece "Suggested tags:" seguido da lista de rótulos gerada pelo GPT-4 ou pelo Llama.
- **Condição 2, sugestão em texto com aviso de IA:** igual à 1, mas com "Suggested tags from AI:". Testa se saber a origem muda a percepção da qualidade ou a taxa de aceitação.
- **Condição 3, rótulos pré-destacados:** os mesmos rótulos sugeridos pelo GPT aparecem já destacados em cor na interface, a sugestão mais forte.

Os autores tratam as três condições como uma escala crescente de assistência. O experimento principal roda controle e Condições 1 a 3 no NYC com rótulos do GPT. Réplicas: Condição 1 com rótulos do Llama 3.1 70B no NYC; e controle mais Condição 1 (GPT) no RTFC, para testar outro livro de códigos e outra base.

**Geração das sugestões:** GPT-4 (`gpt-4-1106-preview`) pela API da OpenAI, sem exemplos (zero-shot), e Llama 3.1 70B pelo serviço LlamaAPI, com o mesmo prompt, temperatura 0, uma chamada por trecho, saída em JSON com o livro de códigos e as definições no prompt. As respostas vieram bem formadas. O GPT inventou um rótulo fora do livro ("External Motivations: Government") 3 vezes no NYC, e dois rótulos inventados apareceram uma vez cada no RTFC; os autores notam que eram plausíveis para o conteúdo, mas os retiraram. Um "None of the above" ao lado de rótulo válido foi retirado; uma saída mal formada do GPT no RTFC virou "None of the above".

**Anotadores:** recrutados no Prolific, nos EUA ou no Reino Unido, com inglês como primeira língua, aprovação de 95 a 100% e ao menos parte da faculdade. Pagamento de US$ 12 por hora (1,6 vez o mínimo dos EUA), ajustado para cima quando a estimativa de tempo ficou curta. Cada anotador fez uma só condição: 20 trechos mais 2 perguntas de "compreensão" em ordem aleatória; tempo recomendado de 20 a 30 minutos, média real de 35. Antes, tinham de passar ao menos 3 minutos no documento do livro de códigos. Nas condições assistidas, a instrução dizia que haveria uma lista de rótulos sugeridos "que você pode usar para ajudar". O IRB do MIT classificou o estudo como isento. Ao todo, experimento pré-registrado com 410 anotadores únicos e mais de 7.000 anotações.

**Concordância prévia e perguntas de compreensão:** antes do experimento, 15 anotadores rotularam 19 trechos do NYC e 20 anotadores rotularam 20 do RTFC; o alfa de Krippendorff deu concordância baixa a média, conforme o rótulo (o texto não traz os valores), o que os autores esperavam numa tarefa subjetiva e complexa. Os pares trecho-rótulo de maior concordância viraram perguntas de compreensão mínima: 4 no NYC, com 13 ou 14 de 15 anotadores de acordo, e no RTFC com 15 a 18 de acordo.

**A tarefa:** para cada trecho, uma pergunta por tema de topo (7 no NYC, 9 no RTFC), marcando os subrótulos que se aplicam ou nenhum. Nas condições assistidas, uma pergunta a mais por trecho: as sugestões foram "no geral", "em parte" ou "nada" úteis/precisas.

**Questionário final** (escala de 1 a 5, com o aviso de que a resposta não afetava a avaliação): quão bem entendeu a tarefa; confiança nas respostas; quanto entende das preocupações e prioridades da comunidade; quão bem conseguiria explicá-las. Depois, perguntas demográficas.

## Resultados

### A assistência não reduziu o tempo (5.1)

Contra a hipótese pré-registrada, os anotadores assistidos não foram mais rápidos. Segundos médios por anotação (Tabela 1, só quem completou ao menos 16 trechos): NYC sem assistência 54,3; GPT em texto 78; GPT em texto com aviso de IA 78,8; GPT pré-preenchido 66,2; Llama em texto 91,1. RTFC sem assistência 72,2; GPT em texto 84,4. Os autores ressalvam que parte do aumento pode vir da pergunta extra sobre a qualidade da sugestão. O resultado repete Overney et al. (2024). Anotadores por condição na Figura 2: NYC controle 53, texto 51, texto com aviso 56, pré-preenchido 48, Llama 56; RTFC controle 55, texto 60.

### A assistência aumentou a compreensão relatada (5.2)

No NYC, todas as condições assistidas tiveram médias maiores que a linha de base nas quatro autoavaliações (teste t bicaudal, p < 0,01, alfa de Bonferroni de 0,013), com tamanho de efeito (d de Cohen) pequeno a médio. Na Figura 3 (que inclui a réplica com Llama), lida no gráfico: compreensão da tarefa cerca de 3,3 no controle contra cerca de 3,55 a 4,05 nas assistidas; confiança cerca de 3,2 contra 3,6 a 3,9; capacidade de explicar cerca de 3,2 contra 3,65 a 3,9; compreensão da comunidade cerca de 3,4 contra 3,7 a 4,05; o valor mais alto, nas quatro, é o da sugestão em texto do GPT ou o do Llama. Na réplica RTFC, a condição assistida teve médias maiores com significância (p < 0,01) em "task confidence", compreensão da comunidade e capacidade de explicar, "mas não na confiança na tarefa em si" (a frase do texto nomeia as duas).

Como a compreensão relatada pode subir enquanto a compreensão "real" cai, os autores olharam as perguntas de compreensão no NYC: a taxa de erro foi de 11,6% no total, sem mudança significativa entre condições. Para eles, isso dá ao menos uma garantia básica de que a assistência não levou a tanta dependência que a tarefa básica deixasse de ser entendida.

### Os anotadores gostaram das sugestões e as aceitaram (5.3)

**Utilidade percebida:** convertendo as respostas em 2 (no geral útil), 1 (em parte) e 0 (nada), a média foi 1,24, entre "em parte" e "muito" útil. Sem diferenças notáveis entre GPT-4 e Llama, entre os formatos (texto, texto com aviso de IA, pré-preenchido) ou entre NYC e RTFC.

**Medida de sobreposição** (Apêndice A): para cada trecho, a fração dos rótulos sugeridos pelo LLM que também entraram na decisão da multidão, numa condição c e num limiar de aprovação de 3, 4 ou 5 anotadores; depois, a média sobre os trechos.

**Números (NYC, Figura 1):**

- Linha de base sem assistência (tomada como gabarito): só 40% de sobreposição entre a decisão da multidão e as sugestões do GPT-4 no limiar de 3; 24% no limiar de 4; 8% com consenso dos 5.
- Com as sugestões do GPT (Condições 1 a 3): 81 a 87% no limiar de 3, 56 a 65% no de 4 e 28 a 38% no de 5, conforme o formato. Lido no gráfico: texto cerca de 0,87, 0,66 e 0,32; texto com aviso de IA cerca de 0,84, 0,56 e 0,28; pré-destacado cerca de 0,81, 0,65 e 0,38. No limiar usual de 3, a sobreposição subiu 40 pontos ou mais, aumento significativo (teste t bicaudal, p = 0,05).
- Com as sugestões do Llama em texto: resultado parecido, com sobreposição menor (0,65 no limiar de 3, 0,53 no de 4, 0,30 no de 5).
- Consenso total: a sobreposição com os 5 anotadores de acordo foi de 8% sem assistência para 38% com os rótulos pré-destacados, aumento significativo (p = 0,001, com correção de Bonferroni). Os autores dizem que a interface pode alterar a força com que a sugestão é aceita.

### Usar rótulos assistidos como gabarito infla o desempenho medido (5.4)

**Linha de base:** com o gabarito 3/5 da condição sem assistência, o F1 ponderado médio sobre os 20 rótulos do NYC é baixo e parecido nos dois modelos: 0,47 (desvio-padrão 0,18) para o GPT-4 e 0,44 (0,18) para o Llama. Tomando os rótulos do GPT-4 como gabarito e avaliando o Llama, o F1 médio sobe para 0,62 (0,10), "significativamente" acima do F1 contra a multidão (Tabela 3).

**Com gabarito assistido:** os autores refizeram o gabarito 3/5 com os anotadores que viram as sugestões em texto do GPT-4 ("GPT-assisted") ou do Llama ("Llama-assisted") e avaliaram cada modelo contra o gabarito montado com as sugestões dele mesmo:

- GPT-4 contra o gabarito assistido pelo GPT: F1 ponderado médio de 0,79 (0,14), aumento médio de +0,32.
- Llama contra o gabarito assistido pelo Llama: 0,79 (0,16), aumento médio de +0,35.
- Por rótulo (Tabela 2), alguns sobem bem mais que a média: "Papel das organizações comunitárias: confiança, vínculo e relações" de 0,28 para 0,82 (+0,54) no GPT-4; "Educação e apoio em saúde" de 0,20 para 0,76 (+0,56), o maior aumento da Tabela 2. No Llama, "Mídia social e jornal" de 0,42 para 0,96 e "Redução de barreiras" de 0,36 para 0,90. Um rótulo não mudou no GPT-4: "Discussão do futuro pós-pandemia", 0,81 nos dois gabaritos.

## Discussão

- Se pessoas revisam sugestões individuais do LLM, o tempo de anotação não cai. A compreensão relatada sobe; a compreensão medida pelas perguntas de teste fica igual. Trabalho futuro: ver se as sugestões aumentaram o tempo por haver mais informação a processar; se ensinam anotadores novos a fazer uma tarefa complexa e por isso aumentam a confiança; e se anotadores com outro incentivo de pagamento aprovariam as sugestões mais depressa.
- **Aviso sobre gabarito:** pessoas costumam aceitar as sugestões do LLM mesmo quando revisam cada rótulo que entra no gabarito. Por isso, usar anotações do LLM, ou rótulos assistidos como os deste estudo, para montar o gabarito pode inflar o desempenho medido do LLM em tarefas subjetivas.
- **Homogeneização:** ao aceitar as sugestões, os anotadores aproximam o "gabarito" do que o LLM produziria. Exemplo: na linha de base, "Basear decisões em dados" era a motivação intrínseca menos frequente (4 ocorrências); com a Condição 1 (sugestões do GPT em texto) ficou quase cinco vezes mais comum (19), empatada com "Voltar ao normal" como a segunda mais citada. Um analista que usasse as anotações assistidas chegaria a outra conclusão sobre a importância relativa dessa motivação.
- **O conceito do LLM:** a homogeneização em direção ao LLM não seria, por si, um problema, mas o desempenho baixo dos dois modelos contra a multidão tem explicações a considerar. Conforme a subjetividade ou a polarização do construto, os humanos podem ser mais ruidosos. Mas, onde humanos concordam muito e o LLM anota de forma sistematicamente diferente, o LLM pode estar usando outro "conceito de fundo" (Jacobs e Wallach, 2021). Exemplo: com F1 inicial de só 0,2 em "Educação e apoio em saúde", o GPT-4 pode operacionalizar o rótulo de outro jeito; com a assistência, o rótulo anotado passa a se parecer com a concepção do LLM.
- **Concordância entre anotadores:** dar a mesma sugestão a vários anotadores aumenta, por construção, as medidas de concordância, que costumam ser lidas como sinal de confiabilidade quando pessoas anotam conceitos sociais. Para continuar lendo assim, o pesquisador precisaria ter confiança de que as sugestões do LLM, e o jeito como ele operacionaliza o conceito, estão mais certas que o julgamento humano. Em tarefa subjetiva isso é difícil de verificar; análise de erro dos rótulos ambíguos pode ajudar.
- **Valor da divergência:** em muitas tarefas de PLN a variação entre anotadores tem valor, para um gabarito robusto (crowd truth, Aroyo e Welty, 2013) ou para representar perspectivas diversas sobre um construto social como discurso de ódio (Sap et al., 2022); algumas tradições qualitativas buscam a divergência de propósito. Para os autores, usar ou oferecer assistência por LLM a anotadores "provavelmente" reduz a variação, nos dois casos (gabarito para PLN e anotação qualitativa).
- **Recomendação:** seguir com anotação assistida só com a cautela que a tarefa e o objetivo pedem, sabendo que o gabarito assistido infla a percepção de desempenho do modelo mesmo com revisão humana e agregação da multidão. Trabalho futuro: tarefa igualmente complexa, tarefa menos complexa, anotadores especialistas. A homogeneização talvez diminua se a interface mostrar a confiança do modelo ou ideias alternativas, em vez de um único conjunto de sugestões.

## Conclusão

Os autores reconhecem que avaliar um modelo com rótulos influenciados por ele "não é padrão nem aconselhável" no paradigma clássico de avaliação, mas dizem que isso tende a acontecer cada vez mais nos sistemas que "só põem um humano no circuito" para aprovar a saída do LLM. Mensagem final: especialmente em tarefas subjetivas, só revisar as sugestões do LLM puxa a distribuição dos rótulos para a do LLM, mesmo quando as pessoas têm a chance de revisar.

## Limites declarados

Anotadores de multidão podem ser particularmente suscetíveis a essa influência; os autores justificam o uso porque eles seguem sendo o padrão de anotação, numa tarefa ambígua de propósito. Anotadores especializados no domínio podem chegar a resultados diferentes, e anotadores com relação com os dados ou com a comunidade podem aderir ou rejeitar a interpretação da IA de outro jeito. Trabalho futuro: ver se especialistas ancoram menos e se afastam da sugestão com segurança quando preciso.

## Outros registros do texto

- O código e os prompts estão em github.com/schropes/ai_sensemaking.
- Os autores declaram ter usado Elicit e ScholarQA para achar trabalhos relacionados (com as citações conferidas) e GitHub Copilot e Cursor para o código (revisado).

---
