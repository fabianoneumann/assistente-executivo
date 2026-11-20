---
titulo: "Verifiability"
tipo: artigo
autor: "Andrej Karpathy"
url: "https://karpathy.bearblog.dev/verifiability/"
publicado_em: 2025-11-17
capturado_em: 2026-10-29
licenca: "nenhuma declarada (a página do Bear Blog só traz 'Powered by Bear' no rodapé, sem licença aberta, conferido em 2026-10-29); tratado como protegido"
areas: [agent-engineering]
tags: [andrej-karpathy, verification, verifiability, subjective-vs-verifiable, jagged-intelligence, rlvr, software-2-0, labor-market]
---

**Proveniência:** lido em 29/10/2026 no HTML do blog, na apuração. A página marca 17/11/2025 (`datetime="2025-11-17T17:00Z"`); a data de 16/11 que circula não aparece na página e pode ser a do post no X que deu origem ao texto (não conferido). O texto é curto: umas 400 palavras, três parágrafos, duas listas e um link para o post "Software 2.0" (Medium, 2017). Ficha de estudo em palavras próprias, cobrindo o texto inteiro na ordem dele; o integral não entra porque o blog não tem licença aberta. Na página de pessoa: `knowledge/people/andrej-karpathy.md`.

## A pergunta

Qual é o traço de uma tarefa (ou de um emprego) que melhor prevê se a IA vai automatizá-la?

## O argumento, na ordem do texto

1. **A analogia que ele escolhe.** Entre as comparações históricas da IA (eletricidade, revolução industrial), a mais forte para ele é a de um **novo paradigma de computação**, porque as duas coisas tratam, no fundo, de automatizar o processamento de informação digital.
2. **O critério dos anos 1980: especificabilidade.** Quem quisesse prever o efeito da computação sobre o emprego nos anos 1980 olharia para isto: a tarefa é transformar informação mecanicamente, seguindo um algoritmo de rotina fácil de especificar? Exemplos dele: digitação, escrituração contábil, os "calculadores humanos". Era a classe de programa que a computação da época deixava escrever, à mão. Programa escrito à mão é o que ele chama de **Software 1.0**.
3. **O que muda com a IA.** Agora dá para escrever programas que nunca se escreveriam à mão: em vez do código, especifica-se um **objetivo** (acurácia de classificação, função de recompensa) e busca-se no espaço de programas, por descida de gradiente, uma rede neural que funcione bem contra esse objetivo. É o paradigma do post "Software 2.0".
4. **O critério novo: verificabilidade.** Nesse paradigma, o traço mais preditivo passa a ser a **verificabilidade**. Se uma tarefa é verificável, ela é otimizável, diretamente ou por aprendizado por reforço, e uma rede pode ser treinada para ficar extremamente boa nela. A pergunta, nas palavras dele, é até que ponto a IA consegue "praticar" aquilo. Para isso o ambiente precisa ter três propriedades:
   - **reiniciável:** dá para começar uma tentativa nova;
   - **eficiente:** dá para fazer muitas tentativas;
   - **recompensável:** existe um processo automático que dá recompensa a cada tentativa feita.
5. **A gradação.** Quanto mais verificável a tarefa, mais ela se presta à automação no paradigma novo. A tarefa não verificável fica dependendo da "mágica" de generalização da rede ("dedos cruzados", diz ele) ou de meios mais fracos, como a imitação.
6. **A fronteira serrilhada.** É isso que produz a fronteira "jagged" (serrilhada, irregular) do progresso dos LLMs. As tarefas verificáveis avançam depressa, possivelmente além dos melhores especialistas: matemática, código, tempo gasto assistindo vídeos, qualquer coisa que pareça quebra-cabeça com resposta certa. Muitas outras ficam para trás em comparação: as criativas, as estratégicas, as que combinam conhecimento do mundo real, estado, contexto e senso comum.
7. **O fecho, em dois versos.** O Software 1.0 automatiza com facilidade o que se pode especificar; o Software 2.0 automatiza com facilidade o que se pode verificar.

## Regras e definições, com a ressalva dele

- **Verificável = treinável por recompensa automática.** "Verificável" aqui é a propriedade de um ambiente de treino (reiniciável, eficiente, recompensável), não a revisão humana do resultado. O texto não fala de quem confere a saída do modelo depois.
- **Previsão por tipo de tarefa:** a automação chega primeiro e mais longe onde há resposta certa conferível por máquina; tarefas criativas, estratégicas e de senso comum ficam para trás "em comparação" (é uma diferença de ritmo, não um "nunca").
- **O enquadramento é de Software 2.0.** O aprendizado por reforço dos LLMs entra aqui sob o rótulo "Software 2.0" (objetivo mais otimização); o texto não usa o termo "Software 3.0" da palestra de junho de 2025.
- **Ressalva dele:** o caminho para o não verificável não é zero, é mais fraco e mais incerto: generalização ("fingers crossed") ou imitação.

## Citações curtas

- "It's about to what extent an AI can "practice" something."
- "Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify."
- Lista das tarefas que ficam para trás: "creative, strategic, tasks that combine real-world knowledge, state, context and common sense".

## O que o texto não trata

Não trata de LLM como juiz, de revisão humana do trabalho do modelo, de várias LLMs se conferindo, nem de bajulação. Não dá número nem estudo: é um ensaio de opinião, com exemplos.

## Tudo o mais que ensina

- **Analogia de mercado de trabalho:** a pergunta implícita é de economia do trabalho. O critério de 1980 explicava quais funções (digitador, guarda-livros, calculador humano) a computação engoliria; o de hoje explicaria quais funções a IA engole primeiro.
- **"Praticar" como chave:** a imagem é a do aprendiz que melhora repetindo com retorno. Sem retorno automático e barato, não há prática em escala, e o modelo depende do que já sabe generalizar.
- **Tempo assistindo vídeo como exemplo de verificável:** ele lista uma métrica de engajamento (o tempo gasto vendo vídeos) ao lado de matemática e código, ou seja, verificável inclui qualquer métrica que uma máquina mede sozinha, não só correção lógica.
- **Ligação com a série dele:** o texto é um dos três que ele aponta depois, na retrospectiva de 2025, como aprofundamento da seção "Ghosts vs. Animals / Jagged Intelligence" (os outros: "Animals vs. Ghosts" e "The Space of Minds"; ficha em `2026-10-29-karpathy-retrospectiva-llm-2025.md`).
