---
titulo: "SpeechJudge: Towards Human-Level Judgment for Speech Naturalness"
tipo: paper
autor: "Xueyao Zhang, Chaoren Wang, Huan Liao, Ziniu Li, Yuancheng Wang, Li Wang, Dongya Jia, Yuanzhe Chen, Xiulin Li, Zhuo Chen e Zhizheng Wu (The Chinese University of Hong Kong, Shenzhen; ByteDance Seed; DataBaker Technology)"
url: "https://arxiv.org/abs/2511.07931"
publicado_em: 2025-11
capturado_em: 2026-11-11
areas: [agent-engineering, generative-media]
tags: [audio-llm-as-judge, speech-naturalness, tts-evaluation, human-preference, reward-model, gemini, gpt-4o-audio, utmos]
licenca: "CC BY-NC-SA 4.0, declarada na página do arXiv; pela cláusula não comercial, só a ficha; o integral fica na url acima (lido na versão HTML v2, https://arxiv.org/html/2511.07931v2)"
---

# Zhang e colegas (2025): quem acerta qual de duas falas sintetizadas soa mais natural

Ficha do artigo do arXiv (2511.07931, versão 2), lido inteiro na versão HTML em 2026-11-11, sem as figuras; os números de concordância entre anotadores da Tabela 5 estavam em fórmulas que a extração não trouxe.

## O que os autores montaram

- **Um conjunto de preferências humanas sobre naturalidade de fala sintetizada:** 99 mil pares de falas geradas por modelos abertos de síntese com voz de referência (CosyVoice2, F5-TTS, MaskGCT e outros), com vozes de referência comuns e expressivas (emoção, sotaque, sussurro, personagens de jogo) e textos em chinês, em inglês e misturando os dois, inclusive com a voz numa língua e o texto em outra.
- **Quem anotou:** 69 anotadores profissionais na China, durante dois meses, cerca de 2,5 anotações por par; nativos de mandarim, e, para o inglês e o texto misturado, com inglês avançado como segunda língua. Cada par recebeu duas tarefas: marcar se o texto foi dito certo (inteligibilidade) e dizer qual das duas falas soa mais natural, numa escala de cinco pontos.
- **A concordância humana:** cerca de 70% dos pares ficaram em concordância total (51,5%) ou fraca (17,2%); a fala expressiva teve concordância menor que a comum, e o chinês, maior que o inglês e o misturado. Quando os dois áudios diferem muito em inteligibilidade, a preferência puxa para o mais compreensível; por isso um subconjunto "de alta qualidade" só guarda pares com diferença de erro de palavra abaixo de 12 pontos.

## O teste dos juízes (SpeechJudge-Eval)

- 1.000 pares tirados do conjunto, só os de concordância total e sem empate, nas três línguas, com o texto e os dois áudios; a pergunta é qual dos dois é mais natural, e a medida é a fração de acertos contra o humano.
- **Os modelos de áudio receberam um pedido simples:** comparar a naturalidade de duas saídas que devem dizer o texto com precisão e naturalidade, dando a cada uma uma nota de 1 a 10 pela prosódia e entonação, pelo ritmo, pela articulação e pela naturalidade geral; a preferência sai da nota maior. Nenhum foi treinado nessa tarefa.
- **A fração de acertos (fala comum / expressiva / total):** Gemini 2.5 Flash, 73,5 / 66,2 / **69,1%**, o melhor; GPT-4o Audio, 71,5 / 64,7 / 67,4%; Gemini 2.5 Pro, 73,0 / 62,2 / 66,5%; Kimi-Audio, 67,0% no total; **GPT-4o mini Audio, 56,3 / 46,7 / 50,5%, o nível do acaso**, como o Gemma-3n (48,2%).
- **As medidas sem modelo de linguagem ficaram perto do acaso:** a taxa de erro de palavra, 57,9%; o UTMOS, 53,7%; o DNSMOS, 57,9%; a semelhança com a voz de referência, 44,5%; os detectores de fala falsa, abaixo de 50%, porque separar fala gerada de fala gravada não é o mesmo que dizer qual gerada soa melhor.

## O juiz treinado (SpeechJudge-GRM)

- Um modelo aberto (Qwen2.5-Omni-7B) ajustado em duas etapas: primeiro com as justificativas em cadeia de raciocínio que o Gemini 2.5 Flash escreveu nos pares em que acertou; depois, por reforço, só nos pares em que o Gemini errou, com a preferência humana como recompensa.
- Chegou a 77,2% (79,4% votando entre 10 respostas), contra 72,7% de um modelo de recompensa clássico treinado com os mesmos dados. Os autores também o usam para escolher a melhor entre várias falas geradas e para treinar um modelo de síntese pequeno, com ganho de naturalidade percebida.

## Limites declarados

- Só fala sintetizada lida, em chinês, inglês e a mistura, julgada por ouvintes chineses: reflete o gosto desse público, não o de falantes nativos de outras línguas, nem a conversa espontânea.
- Os erros que sobram no juiz treinado se concentram em escolhas difíceis: a fala limpa e robótica contra a um pouco ruidosa e viva, a prosódia contra a articulação, e os estilos extremos (emoção muito aguda, sussurro); ali o modelo tende a valorizar demais a limpeza.
- O raciocínio do juiz herda os vieses do Gemini que o ensinou, e as justificativas não foram conferidas por humanos em larga escala.
