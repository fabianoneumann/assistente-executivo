---
titulo: "Preferred Levels for Background Ducking to Produce Esthetically Pleasing Audio for TV with Clear Speech"
tipo: paper
autor: "Matteo Torcoli, Alex Freke-Morin, Jouni Paulus, Christian Simon (Fraunhofer IIS) e Ben Shirley (University of Salford)"
url: "https://salford-repository.worktribe.com/output/1360952"
publicado_em: 2019-12
capturado_em: 2026-11-11
areas: [generative-media]
tags: [audio-mixing, ducking, loudness, dialogue-intelligibility, narration, background-music, broadcast]
licenca: "sem licença aberta declarada (Journal of the Audio Engineering Society 67(12), 1003-1011, DOI 10.17743/jaes.2019.0052; o repositório da Salford marca 'Published Open Access', o OpenAlex dá acesso aberto 'bronze', sem licença); lido no Chrome, pelo PDF do repositório; ficha em palavras próprias, sem o integral"
---

# Torcoli e colegas (2019): quanto a trilha deve baixar quando a narração entra

Ficha do artigo do *Journal of the Audio Engineering Society* 67(12), 1003-1011, dezembro de 2019, versão revista de um trabalho do congresso 146 da AES (Dublin, março de 2019, premiado como melhor artigo revisado). PDF de 9 páginas do repositório da University of Salford, lido inteiro no Chrome em 2026-11-11 (o repositório barra o curl).

## O problema e os termos

- Uma das queixas mais comuns às emissoras é não entender a fala porque o fundo (música e efeitos) está alto demais; o fundo mascara a fala pela energia e, quando é outra voz, também pela informação.
- **Ducking**, aqui, é qualquer atenuação do fundo que varia no tempo para a fala ficar clara: automação de volume, compressão ou gate por sidechain.
- **Os parâmetros:** os de tempo (ataque, liberação, o deslocamento que adianta a descida antes de a fala começar e o hold, que segura o fundo baixo nas pausas curtas, contra o "bombeamento") e o de nível, a **diferença de loudness (LD)** entre a fala e o fundo durante o ducking, medida em LU pela loudness integrada do BS.1770-4 (a do EBU R 128); 1 dB a mais é 1 LU a mais.
- Os manuais e as emissoras não davam número: só que a fala tem de ser "compreensível" e "clara".

## O que a literatura tinha (sempre com fundo constante, sem ducking)

- **BBC:** baixar a música, e, com a mixagem pronta, baixar mais 4 dB (um ponto no medidor PPM) e ver se a intenção criativa sofre.
- **Emissoras públicas alemãs (ARD/ZDF):** pelo menos 7 LU, e de 16 a 23 LU para voz sobre voz; num teste, quem tinha mais de 50 anos preferiu pelo menos 7 LU; noutro, de voz sobre voz, um grupo ficou perto dos 14 LU dos técnicos e outro quis cerca de 20.
- **DPP (Reino Unido):** separação mínima de 4 LU entre diálogo e fundo; a Netflix chegou a recomendar o mesmo e tirou a recomendação.
- **NHK:** 12 técnicos escolheram 9 ± 3 LU em documentário (com outra medida de loudness, de comparação incerta); perto de zero ou negativo em música e esporte.
- **Um teste com jovens** (mediana de 23 anos): a maioria entre 0 e 13 LU, média de 7.

## O que os documentários fazem

- 12 documentários do Reino Unido, da Alemanha e da França, com trechos em que o fundo ficava constante durante a fala: voz sobre voz e **narração sobre música, quase sempre entre 10 e 15 LU**; diálogo de locação sobre música, mais alto, de 14 a 17 LU (fala gravada no set é menos clara, e o técnico compensa).

## O teste de preferência

- **Quem:** 11 ouvintes treinados (21 a 43 anos, cinco técnicos de áudio profissionais) e 11 leigos (23 a 59 anos), sem perda auditiva conhecida, falantes nativos de alemão, em salas tratadas com monitores de estúdio, sem vídeo.
- **O material:** 12 trechos de 9 s com narração em alemão no centro: 6 sobre música sem letra (soft rock, ambient, orquestral) e 6 sobre ambiente (água, rua, carro, metrô); nove versões de cada, da sem ducking até 20 a 28 LU, com a fala sempre no mesmo nível; nota de 0 a 100.
- **Os tempos testados:** um conjunto "normal" (ataque, liberação e deslocamento de 500 ms, hold de 1,5 s) e um mais rápido, como o da audiodescrição (200 ms, 200 ms, 200 ms, sem hold). **Os tempos não mudaram de forma significativa a LD preferida**, embora os autores lembrem que, na prática, eles pesam no gosto.
- **Resultados:** o gosto pessoal explicou a maior parte da variação (31,7%); o trecho e o tipo de fundo, juntos, 29,5%; a idade, 7,1%; a experiência, 5,3%. **Os leigos preferiram, em média, 4 LU a mais que os treinados** (o que bate com a regra da BBC); com música, os quartis dos leigos foram de 6,5 a 15,4 LU; com ambiente, de 11 a 20. Uma faixa de mais ou menos 3 LU em torno da preferida ainda foi bem aceita.
- **A previsão por máquina:** a LD em que uma medida objetiva de inteligibilidade (BiDWGP) dá 0,5 (o mínimo de inteligibilidade completa), mais 17,7 LU, acertou a mediana dos leigos por trecho com erro médio de 1,97 LU. Todas as LDs preferidas ficaram acima do ponto de inteligibilidade completa: a preferência pede mais folga que o mínimo para entender.

## A recomendação

- **Narração sobre música: pelo menos 10 LU** durante o ducking; **sobre ambiente, pelo menos 15 LU**; diálogo de locação pede mais.
- **Limite de cima, pela estética:** 15 LU com música e 20 com ambiente (o quartil de cima dos leigos). A faixa de 10 a 15 LU com música é também a que os documentários usam.
- Só a personalização (áudio por objetos, como o MPEG-H) atende a todos; a mixagem padrão tem de servir à maioria, e a experiência do técnico continua insubstituível, lembrando que quem ouve prefere em média 4 LU a mais que quem mixa.

## Limites declarados

- Fundos que não variam muito no tempo; casos diferentes podem pedir outro valor.
- Só ouvintes sem perda auditiva e relativamente jovens; faltam pessoas mais velhas, mais tipos de fundo, outros sistemas de reprodução e o estudo dos tempos do ducking.
