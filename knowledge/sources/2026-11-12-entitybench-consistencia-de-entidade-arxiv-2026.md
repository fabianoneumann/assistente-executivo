---
titulo: "EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation (He, Wei, Yang e Ordonez, arXiv 2605.15199)"
tipo: paper
autor: "Ruozhen He, Meng Wei, Ziyan Yang, Vicente Ordonez (ByteDance, ByteDance Seed, Rice University)"
url: "https://arxiv.org/html/2605.15199"
publicado_em: 2026-05-14   # arXiv:2605.15199v1 [cs.CV], "Submitted on 14 May 2026", pela página do resumo; texto lido na versão HTML v1; preprint
capturado_em: 2026-11-12
licenca: "CC BY-SA 4.0, indicada na página HTML do arXiv ('License: CC BY-SA 4.0') e na do resumo; ficha em palavras próprias em cima; o integral está na url"
areas: [generative-media]
tags: [benchmark, multi-shot-video, character-consistency, entity-memory, reference-images, llm-as-judge, embedding-similarity, preprint]
---

# EntityBench (2026): a consistência de personagem entre planos de vídeo, medida por distância

Ficha em palavras próprias, lida na versão HTML v1 do arXiv em 12/11/2026 (`sha256` do HTML baixado (hash omitido); o resumo em https://arxiv.org/abs/2605.15199). Preprint, sem revisão por pares declarada. Cobertura: lidos o resumo, as seções 1 a 6 e os apêndices C (o EntityMem), F.4 (trocas e limites), F.5 (a queda por distância, com as Tabelas 19 a 21) e o começo do F.6 (por nível de dificuldade); os apêndices A, B, D, E, G e H, pelos títulos e pelo que as seções lidas citam. O integral não vem neste repositório e se lê na url do frontmatter (licença CC BY-SA 4.0, conferida na página).

## O que o estudo faz

- **A pergunta:** como medir se personagens, objetos e lugares continuam os mesmos ao longo de muitos planos de um vídeo, e se um banco de referências por entidade ajuda.
- **Os dados:** 140 episódios, 2.491 planos e 1.146 cenas, em três níveis (fácil, até 14 planos, ou de 8 a 12 na seção 3; médio, de 14 a 30; difícil, 50; 80, 40 e 20 episódios), com até 13 personagens, 8 lugares e 22 objetos que voltam entre planos e intervalos de até 48 planos entre aparições. Cada plano traz a lista das entidades que devem aparecer. Os roteiros saem de mídia narrativa existente ("derived from real narrative media"), filtrada por clareza visual, estética e movimento, e depois reescrita e enriquecida por LLM; o artigo não diz quais obras. Partiram de 100 mil clipes de produção: 46% passaram pelo filtro de qualidade, 27% dos episódios saíram por legenda demais ou cara de documentário, e uma janela deslizante escolheu os trechos com mais retorno de entidades, cerca de 5% dos planos. No nível difícil, 62% dos planos só trazem entidades que já apareceram.
- **A avaliação, em três pilares e 51 métricas:** (1) qualidade de cada plano (seis dimensões do VBench); (2) se o plano segue o prompt: presença de cada entidade, fidelidade de cada uma à descrição (rosto, cabelo, roupa e corpo para personagem), julgada por um modelo multimodal (gemini-2.5-pro), e a ação; (3) consistência entre planos, por dois sinais: a similaridade de embedding (DINOv2) e o julgamento de um LLM que compara cada aparição com uma âncora. Só entram no pilar 3 as aparições que passaram na fidelidade do pilar 2, para não premiar o método que repete a mesma figura errada em todo plano; a aparição barrada conta como zero na média.
- **O sistema dos autores (EntityMem):** monta antes de gerar qualquer vídeo um banco com uma referência por entidade. Para cada personagem, um agente escreve o prompt de um retrato, um modelo de texto para imagem (FLUX) gera candidatos em fundo de *chroma key*, um modelo de segmentação (SAM 2) recorta, o agente escolhe o melhor e outro agente confere; se falhar, tenta de novo com outra cor de fundo (magenta, azul, laranja). O retrato leva o nome do personagem escrito embaixo, para o vídeo ligar nome e rosto. O estilo da história (anime, fotorrealista) é inferido do resumo dela. Lugares ganham um panorama cortado em três ângulos. A cada plano, o modelo de vídeo recebe os retratos rotulados, uma composição de quadro-chave com as posições e o texto; o último quadro do plano anterior entra só como quadro inicial, fora do banco, para não substituir as referências. O EntityMem estende o StoryMem sem treino novo.
- **Os comparados:** HoloCine e CineTrans (geram todos os planos numa passada) e StoryMem (quadro-chave e depois animação, com memória de quadros), todos abertos; nenhum modelo comercial.

## Resultados

- **No agregado:** o EntityMem tem a maior fidelidade de personagem (`face_fidelity` 0,740 contra 0,452 do StoryMem; d de Cohen +1,71 na categoria e +2,33 no destaque do resumo), a maior presença do personagem (96,7% dos planos contra 84,9% do StoryMem) e o melhor julgamento de identidade entre planos (`llm_face_accuracy` 0,406 contra 0,226). Perde em objetos (fidelidade 0,601 contra 0,618 do StoryMem), o que os autores atribuem à aparência de adesivo do objeto colado na composição, e na similaridade DINOv2 (rosto 0,737 contra 0,792 do StoryMem).
- **As métricas discordam:** a similaridade de embedding alta não quer dizer o personagem certo. No exemplo da Figura 24, EntityMem e StoryMem têm quase a mesma similaridade DINOv2 de rosto (0,883 e 0,875), e o LLM reconhece como o mesmo personagem 71% dos pares do EntityMem e nenhum do StoryMem. Para os autores, onde as duas discordam, o LLM é o sinal mais próximo do que uma pessoa notaria.
- **Qualidade visual não é consistência:** o CineTrans ganha as dimensões de qualidade do VBench e tem a pior presença de personagem (0,80) e a pior identidade julgada pelo LLM (0,09).
- **A queda por distância (apêndice F.5, Tabela 19):** pares de aparições seguidas do mesmo personagem, agrupados pelo número de planos entre elas, com a similaridade de identidade julgada pelo LLM e o número de pares entre parênteses:

| Método | 1 a 2 | 3 a 5 | 6 a 10 | 11 a 20 | 21 a 50 |
|---|---|---|---|---|---|
| EntityMem | 0,744 (250) | 0,698 (126) | 0,646 (76) | 0,669 (36) | 0,657 (14) |
| HoloCine | 0,765 (82) | 0,517 (36) | 0,614 (22) | 0,420 (15) | — |
| CineTrans | 0,371 (51) | 0,408 (25) | 0,333 (6) | 0,600 (10) | 0,457 (7) |

  O EntityMem cai 0,075 da primeira faixa à de 11 a 20 planos e fica quase plano depois (0,66 a 0,67); o HoloCine cai 0,345 no mesmo trecho e fica abaixo do EntityMem em toda faixa depois da primeira. O StoryMem fica fora desta tabela: o filtro de fidelidade dele deixa passar cerca de 1,3 par por episódio (180 no total, contra 502 do EntityMem), só os casos fáceis; os números dele estão na Tabela 21, que os autores mandam não comparar por faixa. Na Tabela 20, com a similaridade DINOv2 do rosto, os valores variam pouco com a distância em todos os métodos (de 0,708 a 0,799), o que os autores leem como a métrica de embedding premiando a semelhança visual e não a identidade; no apêndice F.4, uma frase diz que essa métrica cai com a distância nos quatro métodos, em ritmos diferentes.
- **Por nível:** a vantagem do EntityMem em personagem e ação se mantém nos três níveis e, em algumas métricas, cresce no difícil (Tabela 22, lida só no começo).

## O que os autores concluem e ressalvam

- A consistência entre planos cai com a distância entre as aparições nos métodos que existem, e o banco por entidade, gerado e conferido antes do vídeo, melhora a fidelidade e a consistência do personagem em 29 dimensões.
- As referências geradas antes evitam o erro que se acumula quando a referência é tirada do próprio vídeo gerado.
- Limites ditos: objetos e similaridade de embedding pioram com o banco; a avaliação depende de detectores e de um juiz LLM; os riscos de uso (vídeo falso de pessoa real, difamação, desinformação) vêm com a capacidade, e o sistema herda a segurança dos modelos de base.

## O que a fonte não diz

O artigo não diz quais obras deram os roteiros nem a proporção de histórias desenhadas e fotorrealistas (o exemplo qualitativo da seção 5.4 tem um Pokémon recorrente), não nomeia nesta leitura o modelo de vídeo de base do StoryMem e do EntityMem, e não mede nenhum modelo comercial (Kling, Seedance, Veo, Omni).
