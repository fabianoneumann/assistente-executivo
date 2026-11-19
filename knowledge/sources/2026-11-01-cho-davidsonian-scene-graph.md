---
titulo: "Davidsonian Scene Graph: Improving Reliability in Fine-grained Evaluation for Text-to-Image Generation"
tipo: paper
autor: "Jaemin Cho, Yushi Hu, Roopal Garg, Peter Anderson, Ranjay Krishna, Jason Baldridge, Mohit Bansal, Jordi Pont-Tuset, Su Wang"
url: "https://arxiv.org/abs/2310.18235"
publicado_em: 2023-10-27
capturado_em: 2026-11-01
licenca: "Licença não exclusiva de distribuição do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/, indicada na página do arXiv). Entra só a ficha."
areas: [agent-engineering, content-design]
tags: [text-image-alignment, question-decomposition, vqa-evaluation, atomic-questions, human-agreement, text-to-image, fine-grained-evaluation, spatial-relations, text-rendering, dependency-graph]
---

Ficha de estudo, em palavras próprias; sem texto integral. arXiv: v1 em 27/10/2023; lida a v4 de 13/03/2024, com o comentário "ICLR 2024". Autores da UNC Chapel Hill, University of Washington e Google Research. Projeto em https://google.github.io/dsg. Texto extraído do PDF da v4 com `pdftotext`; as Tabelas 3 e 5 lidas na extração com layout, que desalinha colunas (ver os cuidados). Lido para a rodada investigativa, pelo D7 (o desenho diz o texto?): é a referência mais citada para conferir, por perguntas atômicas, se uma imagem diz o que um texto diz.

## 1. A pergunta

Medir se uma imagem gerada é fiel ao texto que a pediu. As notas únicas de similaridade (CLIPScore e afins) não têm calibração (0,3 é baixo para foto e alto para pixel art) e escondem onde está a falha. A alternativa que vinha crescendo, chamada QG/A, gera perguntas a partir do texto ("há uma moto?", "a moto é azul?") e pede a um modelo de perguntas sobre imagem (VQA) que as responda olhando a imagem; a nota é a fração de respostas que batem com o esperado. Os autores apontam problemas de confiabilidade nessas perguntas e propõem um jeito de gerá-las melhor.

## 2. Os problemas das perguntas geradas

- **Não atômicas:** "há uma moto azul?" mistura existência e cor; a resposta fica ambígua.
- **Duplicadas:** "há uma moto?" e "que tipo de veículo é este?" perguntam a mesma coisa e pesam em dobro.
- **Alucinadas ou omissas:** perguntam o que o texto não diz, ou deixam de perguntar o que ele diz.
- **Respostas incoerentes:** o modelo diz que não há moto e, na pergunta seguinte, que a moto é azul.

## 3. O método (DSG)

- Inspirado na semântica de Davidson: o significado do texto vira um grafo dirigido sem ciclos cujos nós são **proposições atômicas** (verificáveis contra a imagem e não decomponíveis) e cujas arestas são **dependências** (a cor da moto só se pergunta se há moto).
- Quatro tipos de proposição: entidade (inteira ou parte), atributo (cor, tipo, material, contagem, textura, texto renderizado, forma, tamanho, estado, estilo), relação (espacial, ação) e global (iluminação etc.).
- Três passos automáticos com um modelo de linguagem e exemplos anotados: texto para tuplas, tuplas para perguntas de sim ou não, tuplas para dependências. Na avaliação, se a resposta à pergunta-mãe é não, as filhas não contam (variante "drop").

## 4. Validação

- **As perguntas:** em 30 textos com três especialistas, o DSG tem precisão e revocação altas, atomicidade e unicidade maiores que os métodos anteriores (um deles chega a 3,9% de perguntas atômicas), e 100% das dependências válidas (99% no automático, nos 160 textos).
- **Nota por item contra pessoas (Tabela 3):** com o modelo PaLI respondendo às perguntas do DSG, correlação de Spearman de 0,563 e Kendall de 0,458 com a nota humana de 1 a 5 de fidelidade (o texto diz 0,563; a tabela extraída mostra 0,571; a diferença não foi resolvida). O TIFA, método anterior, tinha relatado Kendall de 47,2 contra 23,1 do CLIPScore.
- **Pergunta a pergunta (Tabelas 4 e 5):** o PaLI concorda com a resposta humana em 73,8% das perguntas; por categoria, entidades e cor ficam por volta de 80% ou mais, **relações espaciais entre 72% e 78%** conforme o modelo, contagem perto de 67% e **texto renderizado perto de 25%**, abaixo do acaso das perguntas de múltipla escolha. A leitura das colunas da Tabela 5 na extração é aproximada; os números do corpo do texto (contagem errada em cerca de 40% dos casos com o PaLI; texto renderizado "bem abaixo de 40%") batem com ela.
- **No nível do gerador:** o PaLI ordena os geradores como as pessoas (Imagen e MUSE acima do SD 2.1), mas é otimista: cerca de 80% de acerto pelo PaLI contra cerca de 60% pelas pessoas; acompanha bem nas categorias concretas e erra mais em contagem, texto e prompts de usuários reais.

## 5. O que os autores concluem

Para comparar geradores em categorias concretas, os modelos de VQA atuais sustentam a abordagem; para o detalhe semântico de uma peça (contagem, texto, o subjetivo), ainda não. Subjetividade ("a cidade é muito detalhada?", "a arte é elegante?") gera discordância entre modelo e pessoa e entre pessoas; conhecimento de domínio ("a imagem é 8k?") nem a pessoa julga. Módulos dedicados (OCR para texto) ajudam (apêndice F).

## 6. Tudo o mais que ensina

- **DSG-1k:** 1.060 textos de 10 fontes (TIFA160, parágrafos, relações sintéticas, contagem, usuários reais, poses, contrassenso, texto), com as perguntas liberadas.
- **Modelo julgando perguntas:** o GPT-3.5 concorda em geral com as pessoas sobre duplicatas, mas se distrai com palavras em comum (marca como duplicadas perguntas diferentes com vocabulário parecido).
- **Os modelos de VQA testados são de 2023** (PaLI, mPLUG-large, Instruct-BLIP); o método, e não os números, é o que serve hoje.
- **Leitura nossa:** "o desenho diz o texto" é, na estrutura, o mesmo problema: decompor a frase da tela em proposições atômicas (há uma seta; a seta vai de A para B; o ciclo volta ao começo; há três caixas) e perguntar uma a uma, com dependência, em vez de pedir uma nota de coerência. As categorias em que o VQA mais erra (relação espacial, contagem, texto) são justamente as de um diagrama.
