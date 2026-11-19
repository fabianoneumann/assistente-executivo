---
titulo: "Voyager: An Open-Ended Embodied Agent with Large Language Models"
tipo: paper
autor: "Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar"
url: "https://arxiv.org/abs/2305.16291"
publicado_em: 2023-05-25
capturado_em: 2026-10-29
licenca: "arXiv nonexclusive-distrib 1.0 (licença padrão do arXiv, sem reuso; indicada na página do arXiv). Só ficha."
areas: [agent-engineering]
tags: [skill-library, lifelong-learning, automatic-curriculum, self-verification, agent-memory, code-as-action, iterative-refinement, embodied-agents]
---

Ficha de estudo extensa, em palavras próprias, cobrindo o artigo inteiro na ordem dele. A licença do arXiv não permite guardar o texto integral; a cópia de trabalho (HTML e PDF da v2) ficou no scratchpad da sessão. arXiv: v1 em 25/05/2023, v2 (lida) em 19/10/2023. O artigo 2610.22984 o cita como publicado na Transactions on Machine Learning Research; a página do arXiv não diz o venue. Instituições: NVIDIA, Caltech, UT Austin, Stanford e UW Madison; o trabalho foi feito no estágio do primeiro autor na NVIDIA. Site e código: voyager.minedojo.org. Lido em 2026-10-29, na pesquisa (lições das skills).

## A pergunta

Dá para fazer um agente que aprende ao longo da vida num mundo aberto (Minecraft), explorando, adquirindo habilidades e descobrindo coisas novas sem intervenção humana, usando o GPT-4 só por consultas (caixa preta), sem ajuste fino nem gradiente? Os autores argumentam que um bom aprendiz contínuo precisa, como um jogador humano: (1) propor tarefas adequadas ao seu nível e à situação (no deserto, areia e cacto antes de ferro); (2) refinar habilidades pelo retorno do ambiente e guardar as dominadas para reusar em situações parecidas (lutar com zumbi parece lutar com aranha); (3) explorar e buscar tarefas novas por conta própria.

A escolha de fundo: a ação é **código** (JavaScript sobre a API Mineflayer), não comandos motores de baixo nível, porque programas representam naturalmente ações longas no tempo e compostas.

## Os três componentes (seção 2)

### 1. Currículo automático (seção 2.1, apêndice A.3)

O GPT-4 propõe a próxima tarefa, de baixo para cima, com o objetivo geral de "descobrir o máximo possível de coisas diferentes". Os autores descrevem isso como uma forma de busca por novidade feita em contexto. O prompt tem:

- **Diretrizes e restrições** (prompt 1, completo no apêndice): agir como mentor e guiar para a próxima tarefa conforme o progresso; ser específico sobre o que coletar, fabricar ou matar; formato curto de uma frase só ("Minerar [quantidade] [bloco]", "Fabricar [quantidade] [item]"), uma tarefa por vez; tarefa **não difícil demais** para os recursos e habilidades atuais; tarefa **nova e interessante**, sem repetir a mesma coisa (repetir só se precisar de mais recursos para algo mais difícil); não pedir para construir abrigo; e evitar tarefas cuja verificação exija ver a tela (colocar, construir, plantar, negociar), para que toda tarefa proposta seja **verificável** pelo estado do agente.
- **Estado do agente:** inventário, equipamento, blocos e criaturas num raio de 32 blocos, blocos vistos há pouco, baús conhecidos e seu conteúdo, bioma, hora do dia, vida e fome, posição.
- **Tarefas já concluídas e as que falharam** ("tarefas que falharam por serem difíceis demais"), que marcam a fronteira de capacidade.
- **Contexto extra:** o GPT-3.5 faz a si mesmo de 5 a 10 perguntas sobre o momento (prompt 2, com exemplos bons e ruins: a pergunta tem de ser específica e autocontida, ligada a um conceito do jogo) e responde com a ajuda de uma wiki do Minecraft (prompt 3; responde "desconhecido" quando não sabe). A wiki é opcional, porque o GPT-3.5 já conhece o jogo; o GPT-3.5 é usado aqui por orçamento.
- **Aquecimento** (tabela A.1): a informação entra no prompt aos poucos, conforme o número de tarefas concluídas. Desde o início: inventário básico, equipamento, blocos próximos e posição; criaturas próximas depois de 5 tarefas; inventário completo depois de 7; blocos vistos e bioma depois de 10; vida, fome, hora e contexto extra depois de 15.
- **Raciocínio antes da resposta:** o GPT-4 explica o progresso e só então propõe a tarefa. Temperatura 0,1 no currículo, para variar as tarefas; 0 em todo o resto.

### 2. Biblioteca de habilidades (seção 2.2, apêndice A.4)

Cada habilidade é um **programa executável** que realiza uma tarefa proposta pelo currículo.

- **Como uma habilidade entra:** só depois que a autoverificação confirma que a tarefa foi cumprida (pseudocódigo do apêndice A.1: se deu certo, adiciona o código à biblioteca e marca a tarefa como concluída; se não, marca como falha e nada entra na biblioteca). Programa que não passou na verificação não vira habilidade.
- **Como é escrita:** o prompt de geração de código (prompt 4) pede uma função assíncrona que recebe só o bot; reuso máximo dos programas úteis já fornecidos (minerar, fabricar, fundir, colocar, matar, explorar até achar algo, pegar e guardar em baú); função **genérica e reutilizável**, porque "será reusada para construir funções mais complexas"; não supor nada sobre o inventário e sempre checar se tem os itens antes de usar; mostrar o progresso com mensagens no chat (o que vira retorno do ambiente); sem laços infinitos nem recursão; nome que deixe inferir a tarefa. Funções do código da rodada anterior não são salvas nem executadas.
- **Como é descrita:** ao entrar, o GPT-3.5 escreve uma descrição da função (prompt 5): uma linha só, até 6 frases, sem citar o nome da função nem as mensagens de chat, descrevendo só a função principal. A chave da habilidade no banco vetorial é o embedding dessa descrição (text-embedding-ada-002); o valor é o próprio código.
- **Como é recuperada:** diante de uma tarefa nova, o GPT-3.5 gera uma sugestão geral de como resolvê-la; essa sugestão, junto com o retorno do ambiente, vira a consulta; voltam as **5 habilidades mais relevantes**, que entram no prompt de geração de código. Precisão medida em 309 amostras (tabela A.4): 80,2% no top-1, 89,3% no top-2, 93,2% no top-3, 95,2% no top-4 e 96,5% no top-5.
- **Composição:** habilidades complexas são escritas chamando as mais simples, o que, segundo os autores, faz a capacidade crescer rápido e alivia o "esquecimento catastrófico" de outros métodos de aprendizado contínuo.
- **Exemplos de habilidades guardadas** (apêndice A.4.3): fabricar tábuas de madeira (detecta qual tronco tem e, se não tiver, minera um), minerar 10 blocos de ardósia abaixo do nível 0, fundir 5 ferros brutos (com uma função auxiliar para achar onde pôr a fornalha), encher balde de água, pescar 5 peixes com segurança (tenta de novo se a pesca for cancelada).
- **Se alguma habilidade sai:** o artigo não descreve nenhum mecanismo de remoção, poda ou fusão. Chama a biblioteca de "ever-growing" (sempre crescente) e fala em "expandir e refinar continuamente". O refinamento descrito acontece dentro da tarefa, nas rodadas de código antes de a habilidade entrar. Um dos exemplos se chama "smeltFiveRawIronV2", o que sugere versões de uma mesma habilidade, mas o artigo não explica o sufixo.

### 3. Iteração com retorno do ambiente e autoverificação (seção 2.3, apêndice A.5)

Três tipos de retorno alimentam a próxima rodada de código:

- **Retorno do ambiente:** o progresso intermediário da execução, vindo das mensagens de chat embutidas nas funções básicas. Exemplo: "não consigo fazer o peitoral de ferro porque preciso de mais 7 lingotes". Em outro exemplo da figura 5, o GPT-4 percebe que precisa de mais 2 tábuas antes de fazer gravetos.
- **Erros de execução** do interpretador: operações inválidas ou erros de sintaxe. Exemplo: o GPT-4 percebe que deve fabricar machado de madeira, porque "machado de acácia" não existe no jogo.
- **Autoverificação:** outro agente GPT-4 faz o papel de crítico. Recebe o estado do agente (sem os blocos vistos há pouco nem as criaturas próximas, inúteis para julgar) e a tarefa, raciocina, devolve em JSON se a tarefa foi cumprida e, se não foi, uma crítica dizendo como completá-la (prompt 6). Exceder o pedido conta como sucesso. Os exemplos do prompt ensinam a julgar pela evidência indireta: carne podre no inventário significa que matou um zumbi; fome em 20 significa que comeu; para minerar e fundir, basta olhar o inventário; para plantar, olhar os blocos próximos. Os autores dizem que isso é mais completo que a autorreflexão do Reflexion, porque checa o sucesso e reflete sobre o erro.

O ciclo: o currículo propõe a tarefa; recupera habilidades; o GPT-4 gera código (primeiro explica por que o código anterior falhou, depois planeja passo a passo, depois escreve); executa; coleta retorno e erros; o crítico julga. Repete até o crítico confirmar, e então a habilidade entra na biblioteca e o currículo propõe a próxima. **Depois de 4 rodadas sem sucesso, desiste** e pede outra tarefa; a que falhou vai para a lista de falhas, e o currículo pode tentá-la de novo mais tarde.

## Como mediram (seção 3.1, 3.2, apêndice B)

- **Modelos:** gpt-4-0314 para currículo, código e verificação; gpt-3.5-turbo-0301 para perguntas, respostas, descrições de habilidades e sugestões; text-embedding-ada-002 para embeddings.
- **Ambiente:** MineDojo com a API JavaScript Mineflayer para controle. Muitas mensagens de chat embutidas nas funções e tratamento de exceções para execução contínua. Se o bot morre, renasce perto, com o inventário preservado. O bot recolhe a mesa de trabalho e a fornalha depois de cada programa.
- **Linhas de base,** reinterpretadas para rodar no Minecraft porque nenhuma funcionava pronta: **ReAct** (raciocínio e ação, com o retorno do ambiente e o estado como observação), **Reflexion** (ReAct com autorreflexão, recebendo também os erros de execução e o mesmo módulo de autoverificação do Voyager) e **AutoGPT** (o GPT-4 decompõe o objetivo em submetas; recebe estado, retorno e erros; considera a submeta cumprida se não houver erro, refina até 4 rodadas e, se 3 submetas seguidas não trouxerem item novo, replaneja). ReAct e Reflexion fazem 1 rodada de código do zero e 3 de refinamento, em ciclo. A tarefa de todas é "explorar o mundo e conseguir o máximo de itens possível". O AutoGPT não tem biblioteca de habilidades, autoverificação nem currículo (tabela A.3).
- Não compararam com métodos que leem pixels e emitem comandos de teclado e mouse (VPT e outros), porque o Voyager usa a API de alto nível; a comparação em nível de sistema está na tabela A.2. Três execuções por método.

## Resultados contra as linhas de base (seção 3.3)

- **Exploração (figura 1):** 63 itens únicos em 160 iterações de prompt, 3,3 vezes mais que as outras. Itens por execução, contados das listas do apêndice B.4.1: Voyager 63, 58 e 67; AutoGPT 11, 22 e 25; Reflexion 5, 5 e 5; ReAct 4, 4 e 2. ReAct e Reflexion quase não progridem, porque o objetivo aberto é abstrato demais sem currículo.
- **Árvore tecnológica** (tabela 1; iterações de prompt até desbloquear, média de 3 execuções; entre parênteses, execuções que conseguiram, com limite de 160 iterações):

| Método | Madeira | Pedra | Ferro | Diamante |
|---|---|---|---|---|
| ReAct | não (0/3) | não (0/3) | não (0/3) | não (0/3) |
| Reflexion | não (0/3) | não (0/3) | não (0/3) | não (0/3) |
| AutoGPT | 92 ± 72 (3/3) | 94 ± 72 (3/3) | 135 ± 103 (3/3) | não (0/3) |
| Voyager sem biblioteca | 7 ± 2 (3/3) | 9 ± 4 (3/3) | 29 ± 11 (3/3) | não (0/3) |
| Voyager | 6 ± 2 (3/3) | 11 ± 2 (3/3) | 21 ± 7 (3/3) | 102 (1/3) |

Contra o AutoGPT: madeira 15,3 vezes mais rápido, pedra 8,5, ferro 6,4; só o Voyager chega ao diamante, e em 1 de 3 execuções. Sem a biblioteca, o Voyager é até mais rápido na pedra (9 contra 11), mais lento no ferro e não chega ao diamante.
- **Mapa (figura 7):** percorre distâncias 2,3 vezes maiores, atravessando terrenos variados; as linhas de base ficam presas em áreas locais. Biomas por execução no apêndice B.4.2 (Voyager passou por 8, 5 e 12 tipos de terreno).
- **Generalização para tarefas novas num mundo novo** (tabela 2): inventário zerado, mundo novo, quatro tarefas nunca vistas, limite de 50 iterações; o GPT-4 decompõe cada tarefa em submetas para Voyager e AutoGPT.

| Método | Picareta de diamante | Espada de ouro | Balde de lava | Bússola |
|---|---|---|---|---|
| ReAct, Reflexion, AutoGPT | não (0/3) | não (0/3) | não (0/3) | não (0/3) |
| AutoGPT com a biblioteca do Voyager | 39 (1/3) | 30 (1/3) | não (0/3) | 30 (2/3) |
| Voyager sem biblioteca | 36 (2/3) | 30 ± 9 (3/3) | 27 ± 9 (3/3) | 26 ± 3 (3/3) |
| Voyager | 19 ± 3 (3/3) | 18 ± 7 (3/3) | 21 ± 5 (3/3) | 18 ± 2 (3/3) |

O Voyager resolve todas, em menos iterações. A biblioteca aprendida também ajuda o AutoGPT, que sem ela não resolve nada; os autores a chamam de recurso "plugável" que outros métodos podem usar.

## Ablações (seção 3.4, figura 9, apêndice B.3)

Seis escolhas testadas, medindo itens descobertos:

- **Currículo:** trocar por um aleatório (sorteio entre 101 itens que o Voyager já obteve) derruba os itens descobertos em **93%**, porque algumas tarefas fora de ordem são difíceis demais. Um currículo manual (a sequência clássica até minerar diamante, em 10 passos) exige conhecimento do jogo, não considera a situação do agente e fica abaixo do automático.
- **Biblioteca:** sem ela, o agente tende a estacionar nas fases finais; a biblioteca permite construir habilidades novas sobre as antigas.
- **Autoverificação** é o retorno mais importante: sem ela (3 rodadas de refinamento por tarefa, sem crítico), os itens caem **73%**. Ela decide quando passar para a próxima tarefa e quando tentar de novo uma que falhou.
- **Retorno do ambiente e erros de execução:** retirar cada um também piora (só na figura, sem número no texto).
- **GPT-4 contra GPT-3.5 na geração de código** (mantendo GPT-4 no currículo e na verificação): o GPT-4 obtém **5,7 vezes** mais itens únicos.
- **Robustez à versão do modelo** (apêndice B.4.5): repetido com gpt-4-0613, o desempenho fica praticamente igual.

## Retorno humano multimodal (seção 3.5)

O GPT-4 da época não via imagem. Com retorno humano, o Voyager constrói estruturas 3D (portal do Nether, casa) de dois jeitos: o humano como **crítico** (aponta erros espaciais que o agente não percebe, no lugar da autoverificação) ou como **currículo** (quebra a construção em passos menores, no lugar do currículo automático).

## Limites declarados (seção 4)

- **Custo:** o GPT-4 custa 15 vezes o GPT-3.5, e o Voyager depende do salto de qualidade de código do GPT-4, que o GPT-3.5 e os modelos abertos da época não davam.
- **Imprecisões:** mesmo com a iteração, o agente às vezes empaca e não gera a habilidade certa (o currículo pode retomar a tarefa depois); a autoverificação às vezes erra, por exemplo não reconhecer que ter teia de aranha significa ter derrotado a aranha.
- **Alucinações:** o currículo às vezes propõe tarefas impossíveis (espada ou peitoral de cobre, que não existem); na geração de código, o GPT-4 usa pedregulho como combustível (inválido no jogo) e chama funções que não estão na API fornecida.
- Fora dos limites declarados: o artigo diz que o Voyager é ortogonal a métodos de gradiente como o VPT e pode ser combinado com eles se o controlador oferecer uma API de código. Na seção de impactos, lembra que levar para robôs físicos exigiria restrições de segurança humanas.
