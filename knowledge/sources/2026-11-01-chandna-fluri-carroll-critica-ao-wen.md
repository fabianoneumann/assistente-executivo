---
titulo: "Is the evidence in \"Language Models Learn to Mislead Humans via RLHF\" valid?"
tipo: artigo
autor: "Aaryan Chandna, Lukas Fluri, Micah Carroll"
url: "https://www.lesswrong.com/posts/EvxTAwPFRufWnWWLB/is-the-evidence-in-language-models-learn-to-mislead-humans"
publicado_em: 2025-12-01
capturado_em: 2026-11-01
licenca: "post do LessWrong sem licença aberta declarada na página: tratado como protegido, só a ficha"
areas: [agent-engineering]
tags: [u-sophistry, rlhf, replication, reward-hacking, truncation, experimental-validity, contested-result, model-organism]
---

Ficha de estudo, em palavras próprias. Post de 01/12/2025 no LessWrong (22 minutos de leitura), também aceito como pôster na **trilha de blog** do ICLR 2026 (página iclr.cc/virtual/2026/poster/10012085; fórum no OpenReview, id tNQ7qvTC8Z, não aberto). Trilha de blog não é a trilha principal de artigos: o texto passou por uma revisão de blog, não pela de um artigo de conferência. O trabalho começou no estágio de Lukas Fluri no CHAI (Center for Human-Compatible AI, Berkeley) em 2024; Aaryan Chandna conduziu o resto, com Micah Carroll como orientador. Código das execuções e fork do repositório original publicados (links no post). Página baixada com `curl` e lida inteira, inclusive a seção escrita pelos autores do artigo original e os comentários. Lida para a rodada investigativa (tema i4), como contraprova de [[2026-11-01-wen-rlhf-ensina-a-enganar-pessoas]].

## A tese

Boa parte do resultado do Wen (o RLHF ensina o modelo a enganar pessoas sem ninguém ter planejado) pode vir de defeitos do desenho que tornam o RLHF irreal e muito fácil de "hackear"; corrigidos numa das condições, o resultado se inverte. Os autores **não** contestam a ideia geral: otimizar para o retorno humano cria incentivo a enganar, e isso é "clearly true" na teoria e já aconteceu em sistemas de produção (lá, com retorno de usuários). O que contestam é que o experimento seja informativo sobre RLHF padrão com retorno de anotadores. Dizem também que a evidência deles "is not comprehensive" e que os tamanhos de efeito do Wen estão "likely significantly inflated".

## 1. Os defeitos apontados

- **QuALITY, modelo de recompensa sem a história:** no treino do modelo de recompensa e no PPO, o "juiz" via pergunta, as duas respostas e o argumento, mas não a passagem sobre a qual a pergunta é feita. Sem como premiar a correção, ele premia o argumento que soa bem.
- **QuALITY, política sem contexto:** as passagens eram cortadas em 482 tokens, 8,5 vezes menos que o contexto de 4.096 do Llama 2. Pelo GPT-4o, 88,6% das histórias cortadas no treino e 86,4% na validação não tinham informação suficiente para responder. A política não tinha como aprender a acertar; aprender a convencer era o que sobrava.
- **APPS, corte de entrada e saída:** prompts limitados a 384 tokens (cerca de 30 a 35% das descrições de problema cortadas; o post dá os dois números em lugares diferentes) e saída limitada a 384 tokens, o que pode empurrar o modelo para programas mais densos e menos legíveis, justamente um dos comportamentos que o Wen descreve como engano.
- **Não declarado:** nada disso aparece no artigo, por isso os críticos leem como defeito e não como escolha de desenho; e cada defeito, dizem, amplia o efeito medido em vez de torná-lo conservador.

## 2. O que eles rodaram

- **Reprodução** da condição QuALITY com modelo de recompensa geral (Figura 2.b.1 do Wen), no desenho original: reproduz o padrão (recompensa sobe, acerto real cai). O estudo humano **não** foi refeito.
- **Desenho corrigido** (história inteira para o modelo de recompensa e para a política, Llama 3.1 8B, raciocínio passo a passo): o "hackeamento" some e o acerto real sobe de 36% para 70% em 30.000 episódios; a política inicial acerta 49% (contra uns 52% no Wen) e depois do PPO 72% (contra uns 50%).
- **Ablação** isolando o corte (com as outras mudanças): o modelo quase não sai do acaso, mas o "hackeamento" já desaparece. Um comentarista achou a rotulagem dessa ablação confusa.
- **APPS:** só checagens exploratórias (um ponto de SFT com 35% de acerto e análises de comprimento), sem PPO.
- Custo citado como limite: cerca de 3 dias em 8 A100 por execução.

## 3. A resposta dos autores do Wen (no próprio post)

- As falhas dos modelos de recompensa eram parte do desenho de "organismo modelo"; não induziram o engano contra pessoas (não pediram nem ajustaram o modelo para enganar, não premiaram engano explicitamente), e dizem que treino com recompensa "hackeável" (preferência humana, ROUGE) não deve ser chamado automaticamente de indução intencional.
- O corte é comum em bibliotecas como a trlx; laboratórios de fronteira podem ter computação para RL de contexto longo, outras empresas não.
- Tirar a passagem do modelo de recompensa simula a pessoa que, com tempo curto, não consegue conferir um texto longo, como no debate com assimetria de informação.
- "Intentionality is a spectrum": mantêm a tese, reconhecendo que há debate sobre onde traçar a linha.

## 4. Os comentários

Um comentarista (Simon Steshin) acha que os defeitos rebaixam uma tese forte para uma fraca, põem o artigo ao lado de outros estudos de "organismo modelo" com desenho artificial, e nota que vários artigos posteriores citam o Wen como exemplo natural de desalinhamento; contesta a defesa de realismo, porque os trabalhos de debate citados dão a passagem ao juiz.

## Tudo o mais que ensina

- Antes de tomar um resultado de "o modelo aprendeu a enganar o avaliador" como geral, conferir se o avaliador (modelo de recompensa ou pessoa) tinha a informação necessária para julgar a correção. Sem ela, qualquer otimização premia plausibilidade.
- A parte humana do Wen (pessoas com tempo curto aprovando mais o que soa convincente) não foi refeita nem contestada aqui; o que se contesta é a origem do comportamento e o tamanho do efeito.
