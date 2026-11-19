---
titulo: "Art or Artifice? Large Language Models and the False Promise of Creativity"
tipo: paper
autor: "Tuhin Chakrabarty, Philippe Laban, Divyansh Agarwal, Smaranda Muresan, Chien-Sheng Wu"
url: "https://arxiv.org/abs/2309.14556"
publicado_em: 2023-09-25
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, creativity-evaluation, aesthetic-judgment, expert-agreement, binary-tests, cohens-kappa]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 25/09/2023, v3 (lida) em 08/03/2024. Publicado no **ACM CHI 2024** (comentário do próprio arXiv). Lido em 2026-10-29, na pesquisa da calibração por dimensão do portão. O objeto é **escrita criativa** (contos), não design visual: serve aqui como evidência sobre julgamento de gosto e qualidade subjetiva.

## A ideia

Medir criatividade como **produto**, adaptando o Teste de Torrance de Pensamento Criativo (que mede criatividade como processo) com a Técnica de Avaliação Consensual (especialistas do campo julgando). O resultado é o **TTCW**, 14 testes de sim ou não com justificativa aberta, nas quatro dimensões de Torrance: fluência (ritmo, cena contra exposição, recursos literários, final, coerência), flexibilidade (perspectiva e voz, emoção, viradas), originalidade (tema, pensamento sem clichê, forma) e elaboração (mundo, personagens, camadas de sentido). Os testes foram formulados com 8 especialistas num estudo anterior e são **aditivos**: valem como conjunto, nenhum é obrigatório.

## Princípios de desenho

Testes ancorados no artefato (o conto), pergunta de sim ou não com justificativa aberta, e soma dos testes no lugar de uma nota única.

## Como mediram

- 48 contos de cerca de 1.400 palavras: 12 publicados na New Yorker e, para cada um, três gerados (GPT-3.5, GPT-4, Claude 1.3) a partir do enredo em uma frase, expandidos até ficarem com tamanho parecido.
- 10 especialistas novos (professores de escrita criativa, agentes literários, escritores com mestrado em escrita), três avaliações por conto: 2.016 rótulos com justificativa, a cerca de US$ 20 e 30 minutos por conto.
- Depois, os mesmos 14 testes aplicados por GPT-3.5, GPT-4 e Claude, com prompt detalhado e cadeia de raciocínio, comparados com a maioria dos três especialistas pelo kappa de Cohen.

## Resultados

- **Especialistas entre si:** kappa de Fleiss médio de **0,41** por teste (de 0,27 a 0,66), concordância moderada; na soma dos testes, correlação de **0,69**. Os autores recomendam aplicar os 14 testes juntos, pelo mesmo especialista.
- **Contos humanos contra gerados:** os da New Yorker passam em 84,7% dos testes; os do GPT-3.5 em menos de 10%, os do GPT-4 e do Claude perto de 30%. Três a dez vezes menos. Os especialistas preferiram o conto humano 89% das vezes.
- **Modelos como juízes: no acaso.** Kappa médio contra os especialistas de **0,016 (GPT-3.5), 0,035 (GPT-4) e −0,006 (Claude)**. Só o GPT-4 passou de 0,2 em dois dos 14 testes (perspectiva e voz, 0,26; originalidade de pensamento, 0,31). Exemplos no prompt, testados em alguns testes, não trouxeram ganho significativo. As justificativas dos modelos eram procedimentais e mais longas que as dos especialistas.
- O resultado contraria trabalho anterior em que o GPT-4 julgava bem criatividade em textos curtos (menos de 100 palavras): não se estende ao texto longo.

## O que dizem os especialistas sobre texto de IA

Frases de abertura e de fecho de parágrafo previsíveis, construção recorrente "[oração de tempo], [exposição]", linguagem ornamental confundida com boa escrita, tom moralizante, pouco subtexto.

## Limites declarados

- Temperatura padrão; outros parâmetros poderiam gerar contos mais criativos.
- Os testes provavelmente se correlacionam entre si; a sobreposição não foi medida.
- Os prompts influenciam o resultado e os modelos fechados mudam com o tempo.
- Feito para conto curto; outras formas (roteiro, poesia, slogan) pediriam testes próprios.
- Painel de base estreita, com viés da ficção literária ocidental; e, em criatividade, maximizar a concordância não deve ser o único objetivo, porque a divergência subjetiva é parte do fenômeno.

---
