---
titulo: "Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance"
tipo: paper
autor: "Gagan Bansal, Tongshuang Wu, Joyce Zhou, Raymond Fok, Besmira Nushi, Ece Kamar, Marco Tulio Ribeiro, Daniel S. Weld"
url: "https://arxiv.org/abs/2006.14779"
publicado_em: 2020-06-26
capturado_em: 2026-11-01
licenca: "arXiv, licença não exclusiva de distribuição: protegido, só a ficha"
areas: [agent-engineering]
tags: [explainable-ai, complementary-performance, human-ai-team, over-reliance, appropriate-reliance, confidence-display, adaptive-explanation, expert-explanations, user-study]
---

Ficha de estudo, em palavras próprias. Publicado no CHI 2021 (DOI 10.1145/3411764.3445717); lida a v3 do arXiv (12/01/2021). University of Washington, Microsoft Research e Allen Institute for AI. Dados e exemplos em github.com/uw-hai/Complementary-Performance. Texto extraído do PDF com `pdftotext`; os gráficos não foram lidos como imagem. Lida para a rodada investigativa (tema i4, como apresentar a saída do avaliador).

## O resumo

Os estudos que mostravam ganho com explicações de IA tinham um ponto em comum: a IA sozinha era melhor que a equipe, então tirar a pessoa do laço daria resultado ainda melhor. Os autores igualam o acerto da IA ao das pessoas, para abrir espaço ao **desempenho complementar** (equipe melhor que cada um sozinho), e testam vários tipos de explicação em três tarefas. Houve complementaridade em todas, mas as explicações não a aumentaram em relação a mostrar só a recomendação e a confiança. Em vez disso, as explicações **aumentaram a chance de a pessoa aceitar a recomendação, certa ou errada**.

## 1. Desenho

- **Tarefas:** sentimento de resenhas de cerveja (Beer) e de livros da Amazon (Amzbook), e questões de raciocínio lógico do LSAT. A IA (RoBERTa) foi posta, pela escolha dos itens, num acerto comparável ao das pessoas (no LSAT, 65%).
- **Condições:** só a pessoa; equipe com recomendação e confiança, sem explicação (a linha de base forte, porque os modelos dão confiança e ela é a explicação mais simples); explicar só a classe prevista (Top-1); explicar as duas classes (Top-2, o argumento e o contra-argumento); **adaptativa** (Top-1 quando a IA está segura, Top-2 quando não, com o corte na mediana da confiança: 89,2% e 88,9%); e explicações de especialistas, como teto de qualidade. Explicações automáticas por LIME, destacadas no texto; no LSAT, só de especialista (adaptadas de um livro preparatório).
- **Participantes:** Mechanical Turk, nos EUA, com histórico de aprovação; 566 (Beer), 552 (Amzbook) e 508 (LSAT) recrutados, cerca de 100 por condição; filtro de qualidade e bônus por acerto.

## 2. Resultados

- **Complementaridade em todas as tarefas**, inclusive só com recomendação e confiança.
- **Explicações não acrescentaram** sobre a confiança: nenhuma diferença significativa entre Top-1 e Top-2, nem entre adaptativa e só confiança, nem entre explicação de especialista e automática.
- **O efeito que apareceu:** explicar a classe prevista melhorou o acerto quando a IA estava certa e piorou quando estava errada, já no estudo piloto e de novo no principal; as explicações aumentaram a dependência mesmo quando a recomendação estava errada.
- **Adaptativa:** reduziu a concordância cega quando a IA estava incerta (mais propensa a errar), o que os autores chamam de evidência sugestiva, mas não melhorou o acerto final: nos casos incertos, a pessoa precisava discordar e ainda resolver certo, e o contra-argumento ajudava a suspeitar sem ajudar a acertar.
- **Expertise relativa:** a ajuda da IA rende mais onde ela acerta o que as pessoas erram (Beer e LSAT) do que onde as fronteiras de erro coincidem (Amzbook).
- **Qualitativo:** as pessoas queriam explicações melhores e se confundiam quando a explicação não batia com o comportamento do modelo; sem o contra-argumento destacado, liam a primeira frase destacada e paravam.

## 3. O que os autores concluem

Explicações que aumentam a aceitação indiscriminadamente não servem a equipes em que a pessoa precisa pegar o erro da máquina; o desafio é explicação que produza confiança adequada, sensível a quando a IA pode estar errada. A interface pesa: a posição da recomendação e o destaque do argumento mudam a estratégia da pessoa.

## Tudo o mais que ensina

- Uma tabela de estudos anteriores em que a explicação "melhorou" a equipe, todos com a IA sozinha melhor que a equipe: o ganho vinha de a pessoa obedecer mais a uma IA melhor.
- A recomendação de controlar o acerto relativo da IA e da pessoa ao estudar equipes, e de olhar o resultado separado pelos casos em que a IA erra.
- Relacionado, não aberto: Fok e Weld, "In search of verifiability: Explanations rarely enable complementary performance" (*AI Magazine*, 2024), que defende que a explicação só ajuda quando permite à pessoa **verificar** a resposta.
