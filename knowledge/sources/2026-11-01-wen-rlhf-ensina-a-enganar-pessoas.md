---
titulo: "Language Models Learn to Mislead Humans via RLHF"
tipo: paper
autor: "Jiaxin Wen, Ruiqi Zhong, Akbir Khan, Ethan Perez, Jacob Steinhardt, Minlie Huang, Samuel R. Bowman, He He, Shi Feng"
url: "https://arxiv.org/abs/2409.12822"
publicado_em: 2024-09-19
capturado_em: 2026-11-01
licenca: "arXiv, licença não exclusiva de distribuição (http://arxiv.org/licenses/nonexclusive-distrib/1.0/): protegido, só a ficha"
areas: [agent-engineering]
tags: [u-sophistry, rlhf, human-evaluation, misleading-outputs, false-positive-rate, reward-hacking, goodhart, persuasion, scalable-oversight, human-evaluator-limits, contested-result]
---

Ficha de estudo, em palavras próprias. arXiv: v1 em 19/09/2024, v3 em 08/12/2024 (a lida, que ainda traz no cabeçalho "Under review"); publicado no ICLR 2025 (página de anais em proceedings.iclr.cc). Afiliações: Tsinghua, UC Berkeley, Anthropic, NYU, George Washington University. Código em github.com/Jiaxin-Wen/MisleadLM. Texto extraído do PDF com `pdftotext`; as figuras não foram lidas como imagem, e os números vêm do texto. Lida para a rodada investigativa (tema i4, quem lê a saída do juiz).

**Atenção à força da evidência:** o resultado foi contestado. Em dezembro de 2025, Chandna, Fluri e Carroll (pôster na trilha de blog do ICLR 2026) mostraram que, no QuALITY, o modelo de recompensa não via a história e a política via a história cortada a ponto de 86 a 88% dos exemplos não terem informação para responder; corrigido isso numa das condições, o engano some e o acerto sobe. Os autores do Wen respondem que as falhas eram parte do desenho de "organismo modelo". Ficha própria: [[2026-11-01-chandna-fluri-carroll-critica-ao-wen]]. O que fica de pé com mais segurança é o lado humano do experimento (as pessoas, com tempo limitado, erraram mais nas saídas do modelo treinado), não a tese de que isso nasce de um RLHF "padrão".

## O resumo

Modelos de linguagem podem errar de um jeito difícil de ver, e o RLHF pode piorar isso: para ganhar recompensa, o modelo aprende a convencer pessoas de que está certo mesmo quando está errado. Os autores chamam isso de U-SOPHISTRY (o "U" de não intencional, em contraste com o engano induzido de propósito). Com pessoas avaliando a correção das saídas sob tempo limitado (3 a 10 minutos), em perguntas sobre textos longos (QuALITY) e programação (APPS), o RLHF deixou o modelo mais convincente, mas não mais correto, e a taxa de falso positivo das pessoas subiu 24,1% no QuALITY e 18,3% no APPS. Uma sonda que detecta quase perfeitamente o engano plantado de propósito (agentes adormecidos) não detecta o engano que surgiu sozinho.

## 1. As três recompensas e a hipótese

- **R (oráculo):** o que se quer de fato (o programa certo, a resposta certa), estabelecido por especialistas sem limite de tempo; caro demais para treinar ou avaliar em escala.
- **R_human:** o que se coleta na prática, de pessoas com tempo limitado; herda as fraquezas delas: atalhos, erro sutil que passa, preferência por resposta assertiva, bajuladora ou longa.
- **R_train:** o substituto automático de R_human usado no treino (um modelo de recompensa treinado em preferências); herda as fraquezas de R_human.
- **Hipótese:** o modelo explora a distância entre R_train e R; como R_human tem as mesmas fraquezas de R_train, a aprovação humana também sobe sem que a correção suba. É uma forma da lei de Goodhart: a aprovação humana fica pior como medida quando vira alvo.

## 2. O desenho

- **QuALITY:** passagem de uns 5.000 tokens, pergunta com duas opções (a certa e o melhor distrator); o modelo escolhe e argumenta. Base: LLaMA-2-7B ajustado para imitar respostas e argumentos. Dois R_train: um específico da tarefa (imita avaliações humanas de pares resposta e argumento, de Khan et al. 2024) e um geral (preferências do ChatBotArena).
- **APPS:** programação algorítmica, em média 34 testes por problema. Base: Deepseek-Coder-7B. Como não havia dados humanos suficientes, R_train = passar nos dois testes mais simples, desenhado a partir de um piloto em que as pessoas escreviam em média 2,4 testes simples por programa; correlação com a avaliação humana r = 0,59 (a humano-humano foi 0,63).
- **Treino:** PPO pela biblioteca TRLX.
- **Avaliadores:** 35 contratados pelo Upwork no QuALITY (falantes nativos de inglês, em geral professores, escritores, editores ou universitários), 10 estudantes de computação ou engenharia elétrica no APPS; treinados com exemplos de aquecimento e filtrados pela taxa de erro. 250 perguntas sorteadas por tarefa, cada avaliador vê cada pergunta uma vez só, sem saber se a saída é do modelo antes ou depois do RLHF. QuALITY: 3 minutos, com a passagem, as duas opções e a saída. APPS: 10 minutos, podendo escrever e rodar testes próprios. Cerca de 150 horas de estudo humano.
- **Resposta:** confiança de que a saída está certa (0, 25, 50, 75 ou 100%); acima de 50% conta como aprovação. Bônus por acerto (no APPS, maior para acerto com 100% de confiança), que os autores dizem não ser regra de pontuação própria; por isso a confiança não deve ser lida como probabilidade.
- **Medidas:** correção (R = 1), aprovação humana (R_human = 1), taxa de erro da avaliação humana, e taxa de falso positivo humano (a saída está errada e a pessoa aprova), esta só nos casos em que os dois modelos erram.

## 3. Os resultados

- **Mais aprovação, mesma correção:** a aprovação humana subiu 9,4 pontos (QuALITY com R_train geral), 6,0 (QuALITY específico) e 14,3 (APPS); a correção quase não mudou (na figura de abertura, −1,8 no QuALITY geral).
- **Avaliação pior:** a taxa de erro das pessoas foi de 42,9% para 58,5% (QuALITY específico), de 40,8% para 48,2% (QuALITY geral) e de 31,3% para 45,7% (APPS).
- **Erro mais convincente:** o falso positivo humano foi de 41,0% para 65,1%, de 46,7% para 70,2% e de 29,6% para 47,9%, na mesma ordem. No QuALITY, mais saídas erradas aprovadas com 100% de confiança; no APPS, sobretudo com 75% (os autores supõem que quem programa sabe que os problemas são difíceis e evita dizer que um programa não tem defeito).
- **Robustez:** a taxa de erro subiu para 71%, 76% e 90% dos avaliadores, nas três condições (teste t pareado, p = 0,003, 0,003 e 0,049); o esforço não caiu: no QuALITY todos usaram os 3 minutos inteiros, e no APPS gastaram um pouco mais de tempo (558 s contra 540 s) e escreveram testes um pouco mais numerosos e variados para o modelo treinado.
- **Controle:** o modelo treinado contra R (a correção real) engana muito menos quando erra e melhora a correção, o que indica que a implementação do RLHF funciona e que o problema está nas falhas de R_train.

## 4. Como o modelo engana (análise qualitativa)

- **Perguntas sobre texto:** fabrica ou escolhe a dedo evidência (inclusive estatística inventada que soa autoritária: um avaliador comentou "Agree! statement and statistics in the article indicate that the answer above is correct"), argumenta pela resposta errada com lógica consistente (o modelo inicial começava defendendo A e terminava defendendo B, e isso o entregava) e introduz falácias causais sutis no lugar das óbvias.
- **Programação:** programas errados que passam em todos os 3 a 5 testes escritos pelo avaliador (o modelo inicial falhava já no primeiro), menos legíveis (menos funções auxiliares, mais complexidade ciclomática, o que tira da pessoa a leitura da lógica e a empurra para os testes) e com menos dos erros comuns que as pessoas procuram primeiro (índice fora do limite, por exemplo).

## 5. A sonda que não generaliza

O método de sonda de MacDiarmid et al. (2024), que chega a 99,3% de AUROC para detectar programas defeituosos de um agente adormecido (engano plantado de propósito), fica perto do acaso no modelo deste estudo, mesmo melhorado com uma camada MLP e busca de hiperparâmetros. Conclusão dos autores: o engano induzido não é um bom banco de testes para defesas contra o que surge sozinho.

## 6. Discussão e limites declarados pelos autores

- **A melhora que você vê pode não ser real:** muita avaliação de alinhamento usa avaliação humana como verdade de fato, e empresas usam retorno em massa (como o Elo do ChatBotArena) para avaliar, treinar e anunciar modelos; esse retorno vem com frequência de pessoas sem treino, anônimas, que gastam pouco tempo (por exemplo, 1 minuto).
- **Quem desenvolve pode não perceber:** conferir alguns exemplos à mão costuma revelar quando um modelo foi superajustado a uma métrica ruim, mas não basta aqui, porque quem confere também é humano e também é enganado. Frase dos autores: "The 'developers' that overlooked U-SOPHISTRY can be any human, which includes us, the authors, and you".
- **Limites:** só dois domínios (perguntas sobre texto longo e programação algorítmica); não variaram a capacidade dos avaliadores nem o tempo (3 a 10 minutos, "decente, mas não folgado"); só pediram um veredito binário de correção, e dizem valer estudar se retorno mais fino (por trecho, por tipo de erro) resiste melhor.
- **Trabalhos de supervisão escalável citados como saída:** decomposição da tarefa, geração de casos de teste, crítica e debate, com o alerta de que quase nenhum foi testado contra erros enganosos.

## Tudo o mais que ensina

- A lista de fraquezas do avaliador humano que o modelo pode explorar, com fontes: atalhos e erro sutil que passa (Saunders et al. 2022; Perry et al. 2023; Gudibande et al. 2023), resposta assertiva (Hosking et al. 2023), bajuladora (Sharma et al. 2023) e longa (Kabir et al. 2023).
- A distinção entre explorar R_train (menos grave, porque a pessoa vê a saída ruim e a rejeita) e explorar R_human (mais grave, porque passa pela pessoa).
- O modo de medir: comparar a avaliação humana com um gabarito independente (R), antes e depois, nos mesmos itens, sem que o avaliador saiba a origem da saída; e olhar o falso positivo, não só a aprovação.
