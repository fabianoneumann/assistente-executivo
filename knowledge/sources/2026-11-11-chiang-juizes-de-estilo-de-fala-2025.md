---
titulo: "Audio-Aware Large Language Models as Judges for Speaking Styles"
tipo: paper
autor: "Cheng-Han Chiang (National Taiwan University e Microsoft), Xiaofei Wang, Chung-Ching Lin, Kevin Lin, Linjie Li, Radu Kopetz, Yao Qian, Zhendong Wang, Zhengyuan Yang (Microsoft), Hung-yi Lee (National Taiwan University) e Lijuan Wang"
url: "https://arxiv.org/abs/2506.05984"
publicado_em: 2025-06
capturado_em: 2026-11-11
areas: [agent-engineering, generative-media]
tags: [audio-llm-as-judge, speaking-style, prosody, gemini, gpt-4o-audio, human-agreement]
licenca: "CC BY 4.0, declarada na página do arXiv (abs/2506.05984); o integral, da versão v1 em HTML, está na url"
---

# Chiang e colegas (2025): modelos de áudio como juízes do jeito de falar

Ficha do artigo do arXiv 2506.05984 (v1, junho de 2025), lido na versão HTML em 2026-11-11.

## Ficha

- **A pergunta:** um modelo de linguagem que ouve áudio consegue julgar o estilo da fala (emoção, volume, ritmo, ênfase em palavra, altura, elementos não verbais como riso e suspiro), que costuma depender de avaliação humana cara e de variância alta?
- **As duas tarefas (StyleSet):** seguir uma instrução de estilo (20 frases, cada uma com o estilo pedido, inclusive mudanças dentro da frase, palavra a enfatizar, emoção, choro, gagueira, pausas e risos) e interpretar um papel (20 contextos do IEMOCAP, com a primeira fala dada). Quatro modelos falantes geraram a fala: GPT-4o-audio, GPT-4o-mini-audio, Qwen-2.5-Omni e Step-Audio.
- **Como se julgou:** escala de 1 a 5; o juiz recebe o texto, o estilo pedido e a fala, com cadeia de raciocínio, cinco respostas por caso juntadas; quatro avaliadores humanos por tarefa com as mesmas instruções.
- **Seguir a instrução, o resultado:** os humanos puseram o GPT-4o-audio em primeiro (média 3,65) e os outros três perto e mal; nenhum modelo consegue mudar o ritmo dentro de uma frase, e dois às vezes leem a palavra "suspiro" em vez de suspirar. Os dois juízes também puseram o GPT-4o-audio em primeiro e se confundiram na ordem dos três piores, que eram parecidos.
- **A concordância (r de Pearson sobre 80 notas):** humano com humano, 0,596; **humano com o Gemini 2.5 Pro, 0,640**; humano com o GPT-4o-audio, 0,355. A correlação do Gemini variou de 0,640 a 0,649 com a temperatura de 1,5, 1,0 e 0,5.
- **Interpretar papel:** os humanos deram 4,03 aos diálogos gravados por pessoas, bem acima de todos os modelos; no estilo, a distância para o GPT-4o-audio foi só 0,64, mas no realismo o humano teve quase o dobro. O Gemini concordou com a ordem dos humanos; o GPT-4o, em linhas gerais. Aqui, humano com humano deu só 0,253, e os dois juízes passaram de 0,30.
- **A conclusão dos autores:** os juízes de áudio podem julgar o estilo nas duas tarefas com concordância comparável à dos humanos entre si.
- **Os limites declarados:** só o estilo foi validado, e o resultado não quer dizer que o juiz serve para avaliar a fala em todos os aspectos; o diálogo foi por turnos, não simultâneo.
