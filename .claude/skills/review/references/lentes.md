# Catálogo de lentes

Cada lente é uma pergunta que direciona o que o revisor procura. A lente da régua roda sempre; as outras, a skill que chama escolhe (de 3 a 6). Uma lente nova entra aqui com a pergunta, quando usar, o tipo de achado que costuma gerar e de onde vem. Nenhuma lente é obrigada a discordar.

## Sempre

| Lente | Pergunta | Tipo de achado | De onde |
|---|---|---|---|
| **Régua** | O trabalho fere alguma regra escrita que vale para ele? Cite o texto da regra (rubricas, design system, `decisions/`, READMEs da área, `CLAUDE.md`, e o critério registrado antes de rodar: o registro do experimento, o comentário de critério da issue). | desvio da régua | Code Review (agente de conformidade com o `CLAUDE.md`); lentes que só olham a decisão perdem a regra escrita |

## Fato e evidência

| Lente | Pergunta | Quando usar | Tipo | De onde |
|---|---|---|---|---|
| **Fidelidade** | Cada número, data e atribuição ("X disse", "Y mediu") bate com a fonte, na condição certa? Abra a fonte no trecho. | sínteses, fichas, pautas, peças com dado | afirmação errada | o número certo citado na condição errada é o erro mais comum de síntese |
| **Números** | O número diz o que a frase afirma? Período parcial ao lado de cheio, denominador que muda, média de médias, fuso, segmento definido pelo resultado, ausente lido como zero; as partes somam o todo e a mesma conta por dois caminhos bate; amostra pequena, média sem mediana e quantos recortes foram olhados estão ditos? | relatórios e leituras de métricas, pesquisas e sínteses com conta nossa, a reavaliação desta skill | afirmação errada ou lacuna | `knowledge/data-analysis/ler-numeros-sem-se-enganar.md` (seções 3 a 5) |
| **Além da evidência** | Onde o trabalho conclui mais do que as fontes sustentam: generalização, causa, "o que mais rendeu"? | sínteses, recomendações, leituras de teste | lacuna ou afirmação | revisões de sínteses |
| **O que contraria ou falta** | Há evidência nas fontes ou na base que vai contra a conclusão e ficou de fora? Que lacuna não está marcada como lacuna? | sínteses, pautas, decisões | lacuna | `story-angle` ("o que pode derrubar") |
| **Busca** | A base foi consultada por várias formas da pergunta (sinônimos, inglês, o termo vizinho) antes de dizer "nada registrado"? | o Passo 0b da `research`, a Fase 0 da `story-angle` | lacuna | a busca por um termo só não acha o que a base registra com outro |
| **Conteúdo próprio** | O texto, a composição ou o exemplo nosso ficou perto demais da obra de terceiro de onde saiu (frase traduzida quase literal, mesmo molde, mesmos itens, mesmo produto)? O sentido pode ser o dela; as palavras, o arranjo e o enchimento são nossos. | trabalho derivado de obra protegida: fichas, peças e aulas a partir de livro ou curso | desvio da régua (quando há regra escrita) ou lacuna | a régua de `knowledge/sources/README.md`; nos trabalhos derivados de obra, foi o que mais pesou |
| **Fonte** | Fonte primária ou resumo de terceiro? A licença foi conferida? O número veio de gráfico (marcar com "cerca de")? | lista de fontes, fichas | afirmação | `knowledge/sources/README.md`; o número atribuído a um artigo que não está no artigo |
| **Calibração das ressalvas** | Cada ressalva nomeia a decisão do leitor que ela muda, e cada afirmação sobre o que foi testado, medido ou lido bate com a evidência? A ressalva que não serve a decisão nenhuma sai, se estreita ou muda de lugar. | sínteses, leituras de teste, análises com bloco de ressalvas; o par de "além da evidência", que pega a frase que diz mais | afirmação errada ou lacuna | o agente de estilo do Elephant-Goldfish Model; candidata, a medir |
| **Referências** | Cada afirmação sobre um script, arquivo, função, comando, campo, issue ou caminho bate com o que existe? Abra e confira um por um; o que contradiz o código e a referência ao que não existe são achados, e o arquivo que o trabalho propõe criar, não. | skills, planos, decisões e documentação de projeto que citam código ou caminhos | afirmação errada | o agente de detalhes do código do Elephant-Goldfish Model; candidata, a medir |

## Premissa e decisão

| Lente | Pergunta | Quando usar | Tipo | De onde |
|---|---|---|---|---|
| **Premissa** | O problema de partida ainda vale, conferido no arquivo ou no estado atual? | decisões, pautas, issues, planos | premissa | a discussão inteira sobre um problema que já não existia |
| **O pedido** | O trabalho cumpre o que o pedido escrito disse (a issue, com o "pronto quando", o corpo e os comentários, ou o pedido da pessoa)? O que falta ou ficou pela metade, o que foi feito sem ser pedido, o que parece feito e está errado? Cite a linha do pedido. | trabalho que responde a uma issue ou a um pedido escrito: plano, lote, edição de skill, análise pedida; opcional: escolhida pela skill que chama ou pelo tipo de trabalho, quando há pedido escrito, e fora do rápido; sem pedido escrito, não roda (Entrada, item 1) | lacuna (a falta e a sobra; a pergunta da conferência para a sobra está na Etapa 2), afirmação errada (o feito errado) | o eixo da especificação do `code-review` de `mattpocock/skills` (MIT): a régua pergunta se o trabalho fere o critério, não se falta ou sobra algo do pedido |
| **Do contra (pre-mortem)** | Imagine que isto já foi feito e deu errado: por quê? Cada razão, sozinha. | decisões, planos, pautas, desenho de skill | lacuna | Klein; Collins (gera mais hipóteses, não necessariamente melhores) |
| **De fora** | Como quem não conhece o sistema nem o assunto veria isto (o seguidor no celular, o leitor da base)? | peças, textos para o público, páginas | lacuna | a lente que viu a densidade de uma tela que as outras não viram |
| **Executor** | O que se faz na segunda de manhã: custo, o que vira regra, onde se registra, o que se repete? | planos, decisões, issues | lacuna | a decisão que ninguém sabe como executar |
| **Comparar com o anterior** | O trabalho fica abaixo dos anteriores do mesmo tipo (a sequência da semana, a síntese vizinha, a skill irmã)? Quando é peça, abra as telas renderizadas, não só o texto, e olhe a estrutura (quanto texto, se há os elementos visuais que as anteriores tinham), sem julgar a forma, que é do portão. | peças, sínteses, skills, qualquer trabalho que tem antecessor | lacuna | telas só com texto passaram por todas as lentes sem que nenhuma as comparasse com as sequências anteriores |

## Forma e clareza

| Lente | Pergunta | Quando usar | Tipo | De onde |
|---|---|---|---|---|
| **Clareza para a pessoa** | Termo sem definição, frase ambígua, seção que não serve à pergunta? | tudo que a pessoa vai ler | estilo | revisões de sínteses |
| **Paráfrase** | Antes dos achados, resuma em 2 a 5 frases o que o trabalho propõe e como funciona segundo ele. A seção que você não consegue parafrasear é achado, e a paráfrase que o próprio trabalho desmente também. | issues, planos, decisões, skills, sínteses longas; o teste concreto da "de fora", que pega as partes que não se ligam mesmo com todo termo definido | lacuna | o agente de compreensão do Elephant-Goldfish Model; candidata, a medir |
| **Zoom out depois das correções** | O que as correções acrescentaram sem precisar: a ressalva defensiva, a explicação que só o revisor pedia, a regra repetida? Olhe só o que elas acrescentaram. | re-revisão, como terceira pergunta ([`re-revisao.md`](./re-revisao.md)) | lacuna, ou desvio da régua quando passa do teto de linhas ou repete regra | o estágio final da revisão do Elephant-Goldfish Model |
| **Heurísticas de interface** | O trabalho fere alguma das 10 heurísticas de Nielsen (visibilidade do estado, linguagem do usuário, controle, consistência, prevenção de erro, reconhecer em vez de lembrar, flexibilidade, estética e minimalismo, recuperação de erro, ajuda)? | páginas, artifacts, interfaces; na criação de peças, as que se aplicam a cada camada | desvio da régua | a avaliação heurística do Nielsen Norman Group |

## Skills e processos

| Lente | Pergunta | Quando usar | Tipo | De onde |
|---|---|---|---|---|
| **Efeito nas outras skills** | Esta mudança numa skill pede ajuste em outra? Há regra repetida, contradição, lição que vale para as outras? | criar ou editar uma skill | lacuna | a regra mudada numa skill que continua velha na outra |
