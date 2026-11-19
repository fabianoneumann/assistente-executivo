---
titulo: "Predicting Preferred Dialogue-to-Background Loudness Difference in Dialogue-Separated Audio"
tipo: paper
autor: "Luca Resti, Martin Strauss, Matteo Torcoli, Emanuël Habets e Bernd Edler (Fraunhofer IIS e International Audio Laboratories Erlangen)"
url: "https://arxiv.org/abs/2305.19100"
publicado_em: 2023
capturado_em: 2026-11-11
areas: [generative-media]
tags: [audio-mixing, loudness, dialogue-enhancement, dialogue-intelligibility, background-music]
licenca: "licença não exclusiva de distribuição do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0), que não permite cópia; versão v2 em HTML lida em 2026-11-11; ficha em palavras próprias, sem o integral"
---

# Resti e colegas (2023): a diferença de loudness preferida entre diálogo e fundo

Ficha do artigo da conferência QoMEX 2023 (15th International Conference on Quality of Multimedia Experience), lido na versão HTML do arXiv (2305.19100v2).

## O que se mediu

- A **diferença de loudness preferida (PLD)** entre a fala e o fundo, quando a emissora só tem a mixagem pronta e separa a fala por uma rede neural para remixar.
- 20 ouvintes de língua alemã (23 a 48 anos, mediana de 27; dez treinados e dez leigos), 20 trechos de 9 a 14 s de TV alemã, com homens e mulheres em número igual; a fala normalizada em -23 LUFS e o fundo atenuado de 3 em 3 LU, de 0 a 21 LU; nota de 0 a 100, como se estivessem vendo TV em casa.
- A loudness da fala e do fundo foi medida **só nos trechos com fala** (dialogue gating, antes do BS.1770), porque a diferença só tem sentido quando os dois tocam juntos.
- Quatro classes de trecho: narração de estúdio sobre música, narração sobre ambiente, diálogo gravado no set sobre música e diálogo de set sobre ambiente.

## O que muda a preferência

- **A pessoa** explicou a maior parte da variação (32%), com uma faixa interquartil média de 5,7 LU por pessoa: não há uma mistura que sirva a todos.
- **O trecho** (27%) e **a classe** (24%) vêm depois: com ambiente, a PLD foi cerca de 5 LU maior que com música, como no estudo de 2019 ([[2026-11-11-torcoli-ducking-preferido-2019]]); diálogo de set sobre ambiente pediu 2,3 LU a mais que narração sobre ambiente, e sobre música não houve diferença.
- A experiência pesou pouco (1,7%).

## Como prever

- Pelo índice de inteligibilidade BiDWGP: a regra de 2019 (o ponto de inteligibilidade completa mais 17,7 LU) superestimou a preferência em 80% dos trechos (erro médio de 5 LU); a regra mais antiga (mais 5,5) subestimou (erro de 7,5). Os autores propõem o mesmo ponto mais 13,2 LU (erro de 3,2) ou o ponto 0,1 mais 22,5 LU (erro de 2,5).
- A conclusão: a preferência mediana se prevê por medida objetiva, e dá para oferecer uma remixagem padrão que a respeite, deixando a personalização para quem quiser outra.
