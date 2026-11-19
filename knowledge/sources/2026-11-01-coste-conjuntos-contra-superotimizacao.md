---
titulo: "Reward Model Ensembles Help Mitigate Overoptimization"
tipo: paper
autor: "Thomas Coste, Usman Anwar, Robert Kirk, David Krueger"
url: "https://arxiv.org/abs/2310.02743"
publicado_em: 2023-10-04
capturado_em: 2026-11-01
licenca: "CC BY 4.0 (indicada na página do arXiv, link para http://creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [reward-model, ensembles, overoptimization, goodhart, worst-case-optimization, uncertainty-weighted-optimization, best-of-n, ppo, kl-penalty, label-noise, synthetic-gold-labels]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 04/10/2023, v2 (lida) em 10/03/2024; publicado no ICLR 2024 (comentário do arXiv e cabeçalho do PDF). Universidade de Cambridge (Coste, Anwar, Krueger) e University College London (Kirk). Código em github.com/tlc4418/llm_optimization. O texto foi extraído do PDF da v2 com `pdftotext`; as figuras não foram lidas como imagem, então os números vêm do texto e das tabelas 6 e 7 do apêndice. Lida para a rodada investigativa (o juiz das peças), tema detecção.

**Atenção:** como no Gao ([[2026-10-31-gao-leis-de-escala-superotimizacao]]), o "ouro" aqui é um modelo de recompensa de 7B, não pessoas, e os modelos são pequenos (política Pythia de 1,4B; modelos de recompensa de 7M a 1,3B). Os membros do conjunto diferem **só na semente do ajuste fino** (cabeça escalar e ordem dos dados), sobre o mesmo modelo pré-treinado e os mesmos dados. O contraponto com dados humanos e conjuntos mais diversos está em [[2026-11-01-eisenstein-conjuntos-ajudam-mas-nao-eliminam]].

## O resumo

No RLHF, o modelo de recompensa aprendido é um substituto imperfeito da recompensa verdadeira e pode ser superotimizado (a nota do substituto sobe e a verdadeira cai). Os autores testam se um **conjunto de modelos de recompensa** com objetivos conservadores resolve isso, no arranjo sintético do Gao, acrescentando 25% de rótulos trocados para imitar a discordância entre anotadores humanos. Resultado: com a melhor de N (BoN), o otimizador conservador praticamente elimina a superotimização e melhora o desempenho em até 70%; com PPO, sempre reduz a superotimização e supera o modelo único, e com uma penalidade de KL pequena a elimina sem custo de desempenho.

## As três formas de juntar o conjunto

- **Média:** não é conservadora; se um membro superestima a recompensa, a política explora esse membro mesmo que os outros acertem.
- **Pior caso (WCO), o mínimo do conjunto:** basta um membro não superestimar para a otimização não superotimizar. Não tem hiperparâmetro; pode custar desempenho por ser conservador demais.
- **Ponderada pela incerteza (UWO):** a média menos um peso λ vezes a variância entre os membros; penaliza a política por gerar respostas em que os membros discordam.

## Montagem

- Dados: AlpacaFarm (instruções do Alpaca, 52 mil), com divisões para ajuste supervisionado, preferências e validação. Ouro: o modelo de recompensa de preferência humana de 7B do AlpacaFarm. Política: Pythia 1,4B. Modelos de recompensa substitutos: 7M, 44M e 1,3B. Rótulos gerados pelo ouro; opcionalmente 25% trocados. Os substitutos chegam a 60% a 75% de acerto na validação.
- Conjunto: cinco modelos de recompensa treinados com os mesmos dados e hiperparâmetros e sementes diferentes.
- Otimização: BoN até n = 12.500 (cerca de 8,4 nats de KL; gerar e rotular isso para mil prompts levou cerca de 700 horas de GPU A100) e PPO por 3.000 passos.

## Resultados

- **Qualquer conjunto quase sempre ajuda sobre o modelo único.**
- **BoN:** com WCO e UWO, nenhuma superotimização; com 25% de ruído, a média ainda superotimiza. Ganho final de cerca de 30% sem ruído e cerca de 75% com ruído sobre a média dos modelos únicos (o resumo arredonda para "até 70%").
- **PPO:** WCO e UWO reduzem sem eliminar a superotimização; com penalidade de KL de 0,01 a eliminam sem perder desempenho. Só com a penalidade de KL, sem conjunto, é preciso um peso 20 vezes maior (0,2) para eliminá-la, com perda grande de desempenho. Em todos os pesos de KL, WCO e UWO empatam ou superam o modelo único.
- **Escala:** o ganho do conjunto é ortogonal ao de aumentar o modelo de recompensa ou os dados; mesmo com o modelo de 1,3B, quase do tamanho da política, WCO e UWO ainda ajudam.
- **Tamanho do conjunto:** salto entre 3 e 4 membros; 4 e 5 quase iguais, com retorno decrescente depois.
- **Peso da incerteza no UWO:** a maioria dos valores razoáveis funciona; quase dispensa ajuste.
- **Por que funciona (seção 5.5):** com 25% de ruído, a variância entre os membros sobe cerca de 2,5 vezes durante o treino com a média e só cerca de 20% com o UWO; a média deixa a política explorar o membro que superestima, a penalidade de incerteza não deixa.
- **Taxa de vitória (apêndice F.9):** as políticas finais com conjunto vencem as de modelo único em cerca de 55% a 63% das comparações no modelo de 44M, e até cerca de 72% a 74% com o BoN no de 1,3B.
- Com 35% de ruído e com PPO estendido a 10 mil passos, o ganho e a estabilidade se mantêm (apêndice F.6 e F.7).

## O que os autores dizem que falta

Replicar em outros conjuntos de dados de RLHF e em modelos maiores; e testar o RLHF online, em que o modelo de recompensa é retreinado com dados humanos novos ao longo da otimização.

## Tudo o mais que ensina

- Superotimização é um caso de *reward hacking*; o texto cita a definição formal de Skalse et al. (2022) e o estudo de Zhuang e Hadfield-Menell (2020) sobre proxies que perdem traços relevantes.
- Conjuntos são usados há tempos para estimar incerteza (Lakshminarayanan et al., 2017) e muitas vezes superam métodos bayesianos mais complexos; em RL baseado em modelo, a discordância entre membros também guia a exploração.
- A perda de validação dos modelos de recompensa varia pouco entre sementes e **não prevê** qual membro vai resistir à superotimização (apêndice F.1).
- Nos exemplos qualitativos, o modelo único com BoN produz respostas ruins e até alucinações (aeroporto de Seattle com linhas de trem inventadas); com PPO, respostas longas e repetitivas.
- Reproduzem as tendências do Gao com modelos abertos (apêndice E).
