---
titulo: "ViStoryBench: Comprehensive Benchmark Suite for Story Visualization (Zhuang et al., arXiv 2505.24862)"
tipo: paper
autor: "Cailin Zhuang, Ailin Huang, Yaoqi Hu, Jingwei Wu, Wei Cheng e outros (StepFun, AIGC Research, Westlake University, ShanghaiTech University)"
url: "https://arxiv.org/html/2505.24862"
publicado_em: 2026-03-29   # versão lida: arXiv:2505.24862v5, 29 de março de 2026, pelo cabeçalho do HTML; a v1 é de maio de 2025, pelo número do arXiv
capturado_em: 2026-11-12
licenca: "CC BY-NC-ND 4.0, indicada na página do arXiv; a cláusula não comercial e a sem derivação não permitem guardar o integral aqui (README desta pasta, item 1, 'Cláusula não comercial'): só a ficha, e o integral fica na url"
areas: [generative-media]
tags: [benchmark, story-visualization, character-consistency, reference-images, cids, copy-paste, user-study, nano-banana]
---

# ViStoryBench: o benchmark de visualização de histórias com referência de personagem

Ficha de estudo em palavras próprias, lida na versão HTML v5 do arXiv em 12/11/2026 (`sha256` do HTML baixado (hash omitido)). **Onde está o integral:** https://arxiv.org/html/2505.24862 (e o PDF na página do arXiv); não entra aqui pela licença CC BY-NC-ND 4.0. Cobertura: lidos o resumo, a definição da tarefa, os dados, as métricas, a configuração dos experimentos, a Tabela 2 (as linhas do ViStoryBench-Lite, célula a célula), o estudo com usuários, as conclusões e limitações, e os apêndices A, B (a análise), C (dados), E (o Lite, pela abertura), G (o estudo com usuários) e I (o CIDS); os outros apêndices, só pelos títulos.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): é ficha de estudo de fonte longa, organizada por pergunta (o que mede, o que se mediu, o estudo com usuários, as conclusões, os limites); contam as frases de prosa e as células com texto corrido. Corpo: 29 unidades (28 frases e 1 célula). Resultado: 9 das 29 condensam um trecho na ordem dele (os quatro passos do CIDS, as duas frases do estudo com usuários que descrevem o método e a correlação, os três itens das conclusões, que juntam a lista de achados dos autores, e a frase dos limites); nenhuma traduz frase a frase. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) e apontou 1 frase colada, a lista de nomes e notas da consistência de ambiente no estudo com usuários, que é fato.

**Reescrita por curadoria** (exceção à regra da fonte imutável, porque o motivo é a licença, não o conteúdo): as seções "O que os autores concluem" e "Limites declarados" seguiam, quase frase a frase e na ordem, a lista de achados e a de limites dos autores, o que a cláusula ND do `README.md` desta pasta passou a vetar no texto argumentativo de obra ND. Foram reescritas por outra pergunta (o que pesa ao escolher modelo e referência; o que fica fora da medida e o que pode distorcê-la), com os fatos da seção 4.2 e do apêndice A (já lido), sem dedução nova; entraram do apêndice o que faltava antes (a falta de medidas de vídeo e de tempo de inferência, o motivo da falta de referência de cenário e a escolha da língua pela documentação de cada modelo); os quatro itens e a frase de limites que a conta acima dava como condensados na ordem saíram. Conta à mão, pela cláusula (a ficha está em outra língua que a fonte): nas duas seções, 13 frases, nenhuma sequência de três ou mais que ande para a frente na fonte, e nenhuma traduz frase a frase.

## O que o benchmark mede

- **A tarefa:** dado um roteiro com a descrição e as imagens de referência de cada personagem e uma lista de planos (cenário, trecho da história, personagens em cena, descrição estática do quadro, enquadramento), gerar uma sequência de imagens que siga os planos e mantenha os personagens. É imagem em sequência, não vídeo: os métodos de vídeo entram pelo quadro-chave de cada plano.
- **Os dados:** 80 trechos de histórias escolhidos à mão (cinema e TV, literatura, folclore, romances, livros ilustrados), resumidos e roteirizados com ajuda de LLM e revistos por pessoas; 1.317 planos, de 4 a 30 por história (16,5 em média); 344 personagens (190 pessoas reais, 135 humanos virtuais, como de animação ou jogo, e 19 não humanos) e 509 imagens de referência, de 1 a 10 por personagem, a maioria tirada de filmes, animações e séries, algumas de cenas parecidas e outras geradas no SDXL (sete histórias). Dez estilos visuais, classificados pela referência dos personagens; 39 histórias realistas e 41 não realistas (animação, arte estilizada, fantasia), divisão que, segundo os autores, permite avaliar por tipo de história.
- **O subconjunto Lite:** 20 histórias (um quarto), com 36 personagens animados, 41 realistas e 43 não humanos, montado para espelhar a base inteira; os produtos comerciais e o estudo com usuários rodam só nele.
- **As métricas:** semelhança de estilo (CSD) e de personagem (CIDS), cada uma "cruzada" (gerada contra a referência) e "própria" (entre as imagens geradas); alinhamento ao prompt em quatro partes (cenário, enquadramento, interação, ação individual), julgado de 0 a 4 por um modelo multimodal (Gemini 3 Pro nas tabelas, Qwen3-VL para reprodutibilidade); contagem certa de personagens em cena (OCCM); Inception Score e nota estética; e a taxa de cópia (*copy-paste*), que mede se o modelo colou a referência em vez de gerar.
- **Como o CIDS se calcula:** o Grounding DINO recorta os personagens, um extrator tira o vetor de cada recorte e um pareamento húngaro liga referência e gerado; a nota é a média do cosseno dos pares. Para personagem realista, um conjunto de três modelos de rosto (ArcFace, AdaFace, FaceNet); para personagem estilizado, o CLIP ViT-L/14. Personagem que o detector não acha fica fora do pareamento.

## O que se mediu (Tabela 2, linhas do Lite)

A tabela tem treze colunas por linha: CSD cruzado e próprio, CIDS cruzado e próprio, as quatro partes do alinhamento e a média, OCCM, Inception, estética e cópia. As linhas dos modelos multimodais e do Sora 2 estão abaixo da faixa "The following results are obtained on ViStoryBench-Lite".

| Linha | CSD cruz. | CSD própr. | CIDS cruz. | CIDS própr. | Alinh. médio | OCCM | Estética | Cópia |
|---|---|---|---|---|---|---|---|---|
| Cópia direta da referência (Lite) | 0,911 | 0,994 | 0,550 | 0,735 | 0,91 | 92,76 | 4,39 | — |
| Gemini 3.0 Pro (a referência [21] do artigo é o Nano Banana Pro) | 0,385 | 0,622 | 0,581 | 0,653 | 3,37 | 59,97 | 5,54 | 0,244 |
| GPT-4o | 0,481 | 0,680 | 0,420 | 0,522 | 3,34 | 69,33 | — | — |
| Sora 2, com imagem de referência | 0,515 | 0,713 | 0,766 | 0,839 | — | — | — | — |
| Sora 2, só texto | 0,365 | 0,685 | 0,364 | 0,561 | — | — | — | — |

As células com "—" não foram lidas nesta captura. A legenda explica os ícones de condição (com imagem de referência; só texto; modo autorregressivo), mas as linhas do GPT-4o e das Gemini não têm ícone, e o asterisco ao lado do nome delas não tem explicação na legenda.

**O texto da análise diverge da tabela:** o apêndice B dá ao GPT-4o CIDS de 0,571 (cruzado) e 0,679 (próprio), e ao Sora 2, 0,738 e 0,813; nas linhas do Lite, o GPT-4o tem 0,420 e 0,522, e o Sora 2, 0,766 e 0,839 ou 0,364 e 0,561. O artigo não explica a diferença, e ela é só do CIDS: os valores de CSD do mesmo parágrafo batem com a tabela (GPT-4o 0,481 e 0,680; Sora 2 0,515 e 0,713, na linha com referência).

## O estudo com usuários

Participantes deram notas de 0 a 4 em três dimensões (consistência do ambiente, consistência de identificação do personagem, estética subjetiva), sobre versões comerciais disponíveis até meados de maio de 2025, no Lite. Pelo apêndice G, foram 20 avaliadores com experiência em avaliar conteúdo visual (alunos de pós-graduação e trabalhadores de plataforma treinados na rubrica), cada um com uma parte do conjunto (em geral de 6 a 8 histórias), e cada par de modelo e história teve ao menos 10 notas independentes por dimensão; a nota é a média entre avaliadores. Os quatro primeiros em identificação do personagem: Doubao 3,70 (92,6%), AIbrm 3,54 (88,4%), UNO 3,36 (84,0%), GPT-4o 3,26 (81,6%). Em ambiente: UNO 3,28, GPT-4o 3,25, Doubao 3,22, Story-Adapter 3,18. Em estética: GPT-4o 3,42, Doubao 3,40, AIbrm 3,32, UNO 3,21. Os autores ligam cada dimensão humana a uma métrica automática (identificação ao CIDS, ambiente ao CSD, estética à nota estética) e dizem que as correlações (Kendall, Spearman, Pearson) mostram que as métricas refletem a preferência humana; o StoryGen ficou fora da correlação por ser ponto fora da curva.

## O que os autores concluem, pelo que pesa ao escolher modelo e referência de personagem

**Manter o personagem tem preço.** Na leitura dos autores, quem mais segura o personagem copia mais a referência e varia menos entre os quadros: é uma troca entre consistência e diversidade, e não uma qualidade a maximizar sozinha. O caso-limite, colar a referência no quadro, pontua bem em várias métricas e mal no alinhamento ao texto, e por isso nenhuma métrica isolada serve de juiz. Os métodos feitos para imagens de história são os que mais mantêm o personagem, mas generalizam pouco para outros cenários.

**No vídeo, a referência pesa menos.** Os modelos de vários planos repetem bem o próprio personagem de um plano a outro, o que os autores atribuem ao treino com filmes, mas ficam mais longe da imagem que receberam como referência. Os métodos de vídeo de história perdem qualidade em cada quadro quando passam a modelar o movimento.

**Narrativa e imagem não andam juntas.** O GPT-4o e os outros modelos multimodais grandes acertam mais a história do que a qualidade visual, e as ferramentas comerciais fazem o inverso: estética e estilo fortes, pouco controle fino do que o roteiro pede. Ninguém junta bem as duas coisas, nenhum método fica à frente em todas as métricas, e a recomendação dos autores é escolher o modelo pela tarefa.

## Limites declarados

**O que fica fora da medida.** O quadrinho com vários painéis numa imagem não se avalia, por falta de um jeito confiável de separar os painéis, e o tempo de inferência também não. O benchmark julga imagens em sequência e a coerência entre elas; a narrativa com imagem e som sincronizados é o objetivo de longo prazo, e para vídeo ainda faltam medidas de coerência no tempo e de qualidade por quadro. Não há imagem de referência de cenário, porque os métodos abertos quase não a aceitam, e a consistência do ambiente só entra pelo alinhamento ao texto.

**O que pode distorcer a medida.** Cada modelo recebeu o prompt em chinês ou em inglês, conforme a documentação dele, sem controle do quanto a língua muda o resultado. Entre os juízes, os modelos especialistas erram em cena complexa e os multimodais alucinam. E parte das referências vem de filmes, séries e animações conhecidos, o que traz risco de direito autoral e pode fazer as métricas se ajustarem a esses estilos e personagens.

## O que a fonte não diz

O artigo não separa os resultados por estilo (realista contra não realista) em nenhuma tabela lida, não diz em que condição o Gemini 3.0 Pro e o GPT-4o foram rodados (com ou sem imagem de referência) e não mede vídeo do Kling, do Seedance nem do Gemini Omni.
