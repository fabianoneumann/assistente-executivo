---
titulo: "AudioJudge: Understanding What Works in Large Audio Model Based Speech Evaluation"
tipo: paper
autor: "Potsawee Manakul, Woody Haosheng Gan, Michael J. Ryan, Ali Sartaz Khan, Warit Sirichotedumrong, Kunat Pipatanakul, William Held e Diyi Yang (SCB 10X, University of Southern California e Stanford University)"
url: "https://aclanthology.org/2026.eacl-long.168.pdf"
publicado_em: 2026-03
capturado_em: 2026-11-11
areas: [agent-engineering, generative-media]
tags: [audio-llm-as-judge, speech-evaluation, positional-bias, verbosity-bias, speaking-rate, gpt-4o-audio, gemini]
licenca: "CC BY 4.0, declarada no rodapé das páginas da ACL Anthology (\"Materials published in or after 2016 are licensed on a Creative Commons Attribution 4.0 International License\"); o PDF traz só ©2026 Association for Computational Linguistics, que não contradiz a licença; ficha em cima; o integral está na url"
---

# Manakul e colegas (2026): o que funciona quando um modelo de áudio julga fala

Ficha do artigo dos *Proceedings of the 19th Conference of the European Chapter of the ACL* (EACL 2026), volume 1, páginas 3644-3663, lido no PDF da ACL Anthology em 2026-11-11.

## A pergunta

- A avaliação de fala depende de sistemas especializados para cada característica (UTMOS e DNSMOS para qualidade, STOI e NISQA para inteligibilidade, outros para prosódia e pronúncia), e as medidas automáticas se correlacionam mal com a preferência humana. A proposta: usar um modelo grande de áudio como juiz (AudioJudge), como o LLM juiz faz com texto.
- Dois usos: **detectar uma característica num exemplo** (pronúncia, velocidade da fala, identidade de quem fala, qualidade) e **ordenar sistemas** pela preferência humana.

## Detectar uma característica num exemplo (com o GPT-4o-Audio)

- **As tarefas, todas em pares:** duas pronúncias da mesma palavra combinam? (200 pares, a referência do Wiktionary contra o GPT-4o-Audio); qual fala é mais rápida?; é a mesma pessoa?; qual tem mais qualidade? (SOMOS, em inglês; TMHINT-Q, em mandarim com ruído; ThaiMOS, pronúncia de fala sintetizada em tailandês).
- **O teto humano:** dois anotadores de fora acertaram de 69,5% a 83% conforme a tarefa, o que mostra o quanto ela é subjetiva.
- **Com o pedido simples, o modelo chuta:** pronúncia, 46,0%; velocidade da fala, 46,9%, perto do acaso. Em qualidade, o ponto de partida é bem melhor.
- **Dar a transcrição ajuda pouco:** a pronúncia sobe (46,0% para 63,0%), o resto quase não muda ou piora.
- **Exemplos separados (in-context) ajudam pouco;** **juntar os áudios num arquivo só ajuda muito:** só juntar os dois áudios do teste levou a pronúncia a 66,0% e a velocidade a 54,2%; o melhor arranjo, com quatro exemplos também juntados no mesmo fluxo de áudio, chegou a 66,5% na pronúncia, 55,3% na velocidade e 70,0% na identidade de quem fala, e perto do humano na qualidade.
- **Mesmo assim, a velocidade da fala segue longe do humano:** 55,3% contra 77,8%; a identidade, 70,0% contra 83,0%.

## Contra os modelos especializados (seção 4.3 e Tabela 2)

- Na qualidade da fala, o juiz de áudio (áudios juntados e quatro exemplos) foi comparado com redes treinadas em notas humanas: o UTMOS (cerca de 100 horas de anotação), o MOSANET+ (25 horas) e o SALMONN ajustado (650 horas), contra menos de 0,2 hora de exemplos do juiz.
- **Acertos (SOMOS em inglês / TMHINT-Q em mandarim / ThaiMOS em tailandês):** UTMOS, 77,5 / 71,5 / **53,5**; MOSANET+, 85,0 / 77,5 / 62,5; SALMONN ajustado, 82,0 / 61,0 / 58,5; o juiz de áudio, 71,0 / 74,5 / **64,0**. As redes especializadas ganham no conjunto em que foram treinadas e caem fora dele; o juiz fica mais estável entre línguas, e os autores o indicam para línguas diversas ou com pouco dado anotado.
- **O UTMOS, pelo apêndice C:** um preditor de nota que junta aprendizado de conjunto, redes autossupervisionadas e modelos clássicos, treinado de início em dados de inglês e de chinês, com correlação acima de 0,8 mostrada depois em outras línguas, como o japonês (Seki e colegas, 2023).

## Ordenar sistemas pela preferência humana

- Dois conjuntos: o ChatbotArena-Spoken (conversas do ChatbotArena sintetizadas em voz, para julgar o conteúdo) e o SpeakBench, criado pelos autores (82 instruções que pedem sotaque, emoção, estilo, prosódia, volume, altura, velocidade ou efeito sonoro, com 13 sistemas e 1.066 pares; 508 julgamentos humanos de 4 anotadores).
- **Correlação de Spearman com a preferência humana, no nível do sistema:** sem nada, o GPT-4o-Audio dá 0,902 e 0,731 e o Gemini 2.5 Flash, 0,805 e 0,846; com áudios juntados e quatro exemplos, 0,931 e 0,775, e 0,877 e 0,857.
- **O conjunto de juízes por aspecto** (um para o conteúdo, um para a qualidade da fala, um para os traços paralinguísticos): 0,802 no GPT-4o-Audio e **0,912 no Gemini 2.5 Flash** no SpeakBench; combinar isso com os exemplos juntados melhora o GPT-4o (0,846) e piora o Gemini (0,857).

## A robustez

- **Ruído:** com ruído branco até 1 dB de relação sinal-ruído, o GPT-4o-Audio manteve a maioria das decisões (85%, 93% e 73% sem mudar nas três categorias); os autores leem que o modelo foi feito para extrair conteúdo no ruído.
- **Viés de tamanho:** todos os modelos preferem a resposta falada mais longa quando a qualidade é a mesma (significativo em todos), o que pouco mexe na ordem dos sistemas porque os empates são cerca de 20% dos dados.
- **Viés de posição:** apresentando o mesmo par nas duas ordens, o GPT-4o-Audio e os Gemini 1.5 e 2.5 Flash preferem o primeiro no julgamento de conteúdo; na velocidade da fala, o GPT-4o-Audio prefere o segundo (chamou o segundo áudio de mais rápido em 49,2% dos casos mesmo invertendo a ordem); em várias tarefas, menos de 80% das decisões se mantêm ao inverter. O viés cresce quando a diferença entre os dois é pequena.

## A conclusão e os limites declarados

- Com o pedido simples, o juiz de áudio ainda erra os julgamentos não lexicais quase como o acaso; as técnicas de pedido melhoram, mas não bastam para todos os casos no nível do exemplo. **No nível do sistema, a correlação com o humano passa de 0,9**, mas não em todo conjunto: no ChatbotArena-Spoken, que julga o conteúdo, o GPT-4o-Audio passa de 0,9; no SpeakBench, que julga os traços paralinguísticos, só o Gemini 2.5 Flash com os juízes por aspecto chega lá (0,912), e o GPT-4o fica de 0,731 a 0,846.
- A diferença para o humano nas tarefas paralinguísticas continua grande; os arranjos que funcionam custam caro; o SpeakBench é pequeno e só em inglês. Mitigações propostas para o futuro: normalizar o tamanho, sortear a ordem e conferir com a ordem invertida.
