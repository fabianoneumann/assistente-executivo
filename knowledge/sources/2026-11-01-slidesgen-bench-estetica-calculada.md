---
titulo: "SlidesGen-Bench: Evaluating Slides Generation via Computational and Quantitative Metrics"
tipo: paper
autor: "Yunqiao Yang, Wenbo Li, Houxing Ren, Zimu Lu, Ke Wang, Zhiyuan Huang, Zhuofan Zong, Mingjie Zhan, Hongsheng Li"
url: "https://arxiv.org/abs/2601.09487"
publicado_em: 2026-01-14
capturado_em: 2026-11-01
licenca: "CC BY-NC-SA 4.0 (indicada na página do arXiv, link creativecommons.org/licenses/by-nc-sa/4.0/); só a ficha entra (licença não comercial)"
areas: [agent-engineering, content-design]
tags: [slide-generation, computational-aesthetics, design-metrics, human-alignment, vlm-as-judge, contrast, visual-clutter, deck-rhythm, benchmark, pixel-metrics]
---

Ficha em palavras próprias; o texto integral (licença CC BY-NC-SA 4.0, não comercial) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 14/01/2026; lida a v2 de 21/08/2026 (37 páginas, 34 figuras), com o comentário "EMNLP 2026 Main Conference". Autores do CUHK MMLab, SenseTime Research, CPII e Shanghai AI Laboratory. Texto extraído do PDF da v2 com `pdftotext`; as Tabelas 2 e 5 foram lidas no texto extraído (números conferidos entre o corpo e a tabela). Lido para a rodada investigativa (forma: código e imagem).

## 1. A pergunta

Geradores de slides seguem três paradigmas (preencher modelo, gerar código HTML que renderiza, gerar a imagem inteira), e os protocolos de avaliação ou dependem de uma referência (o slide verdadeiro) ou de um juiz de modelo sem calibração, sujeito a viés de verbosidade e falhas de raciocínio. A proposta é avaliar os três paradigmas na mesma base: projetar tudo na imagem renderizada para conteúdo e estética, e ler a estrutura do arquivo só para a editabilidade. Cada dimensão por um pipeline verificável, e não por um julgamento único de modelo.

## 2. O benchmark

- **Instruções:** cerca de 30 mil decks humanos coletados, filtrados por tamanho (5 a 40 páginas), anotados por tema e propósito com GPT-4o; documentos-fonte montados da Wikipedia; 94 instruções finais em seis cenários de propósito (marca, plano de negócio, apresentação pessoal, lançamento de produto, introdução a tema, relatório).
- **Sistemas avaliados (nov.-dez. de 2025):** Gamma, Quark, Kimi (padrão e "smart"), Zhipu e Skywork (HTML), NotebookLM, Skywork-Banana e Kimi-Banana (imagem), AutoPresent e PPTAgent (acadêmicos, adaptados).
- **Três ramos:** conteúdo (QuizBank), estética (quatro métricas calculadas sobre os pixels) e editabilidade (PEI, escala de cinco níveis lida do arquivo, com regra de nocaute: falhar um nível impede os de cima).

## 3. Conteúdo: o exame de livro aberto

Do documento-fonte saem âncoras quantitativas (4 a 6 números, datas, especificações) e qualitativas (6 a 8 conceitos) com citação literal da página; um segundo passo audita as âncoras contra o texto; um terceiro gera questões de múltipla escolha. Depois, um modelo de visão transcreve cada slide em markdown (texto literal, dados de gráfico, e a "interpretação visual" de ícones e imagens que carregam informação, ignorando decoração), e outra chamada responde às questões só com essa transcrição. Separar extrair de raciocinar isola de onde vem o erro: só 1,2% dos erros vieram da extração. Na auditoria humana dos 2.499 erros (19,1% de 13.023 respostas), 66,3% foram conteúdo ausente no slide.

## 4. Estética: quatro métricas sobre a imagem

Ancoradas, segundo os autores, em teoria da carga cognitiva e ergonomia visual; operam na imagem renderizada e tratam o deck como sequência.

- **Harmonia:** ajuste das cores do slide a modelos de harmonia de matiz em HSV (Cohen-Or et al., 2006); no deck, a média menos a dispersão entre slides (penaliza inconsistência).
- **Engajamento:** a métrica de "colorido" de Hasler e Süsstrunk (2003), em canais oponentes; no deck, um termo de ritmo pela dispersão do colorido entre slides, com um alvo.
- **Usabilidade:** contraste figura-fundo calculado **dentro das regiões de texto** detectadas por um modelo de análise de layout, pela fórmula de luminância do WCAG, normalizado em log (21:1 vale 1,0). O apêndice insiste que o contraste local, na caixa do texto, pega o texto cinza-escuro sobre preto que o contraste global da imagem não pega.
- **Ritmo visual (VisualHRV):** a desordem visual de cada slide pela entropia de sub-bandas (Rosenholtz et al., 2007, "feature congestion", que aproxima o custo da busca visual), e a variação dela entre slides vizinhos (RMSSD). A ideia: deck bom alterna slides densos e leves; deck exigente e plano cansa.
- **Nota estética:** soma das quatro. Os parâmetros saem de três etapas: distribuição em cerca de 3 mil slides humanos, escolha inicial, e otimização bayesiana contra rankings humanos num conjunto de verificação de 1.000 pares, separado do de teste.

**O que não está lá:** nenhuma métrica de alinhamento, grade, sobreposição, margem, espaço vazio ou equilíbrio. Composição, no sentido de onde as coisas estão na tela, fica fora do ramo calculado; o juiz de modelo da linha de base é que recebe "equilíbrio espacial, alinhamento, nenhuma sobreposição" no prompt.

## 5. Validação contra pessoas (Slides-Align1.5k)

- **Anotação:** 1.435 registros, decks de nove sistemas para o mesmo pedido, mostrados lado a lado; o anotador ordena do melhor ao pior (ordem, não nota, porque nota absoluta deriva). Anotadores: doutorandos de computação, graduandos de artes e funcionários de escritório, treinados juntos nas quatro dimensões com exemplos bons e ruins.
- **Concordância entre pessoas:** Spearman médio de 0,85 (desvio 0,12); ordem idêntica em 45,3% dos casos.
- **Resultado (Tabela 2):** as métricas calculadas chegam a Spearman médio de 0,71 (desvio 0,16) e 32,6% de ordem idêntica; o juiz de modelo dando nota, 0,57 (0,23) e 20,7%; o juiz em pares ("arena"), 0,52 (0,27) e 17,3%; o PPTEval do PPTAgent, 0,53 (0,26) e 17,8%. O juiz de modelo é o gemini-3-flash-preview, com as imagens renderizadas e um prompt espelhando os critérios.
- **Ablação (Tabela 5), Spearman de cada métrica sozinha:** engajamento 0,224; harmonia 0,312; usabilidade (contraste) 0,574; ritmo visual 0,618. Harmonia + engajamento + usabilidade, 0,667; as quatro, 0,710. Os autores leem que legibilidade e clareza são o que mais pesa na preferência por slides.
- **Transferência entre estilos (Apêndice J):** dois terços dos registros são corporativos; tirar qualquer grupo de estilo muda o alinhamento em menos de 0,05; decks escuros não são penalizados. Os erros de ordem são maiores em decks de marketing cheios de imagem e em paletas criativas (a harmonia pune paleta fora do padrão; o ritmo cai em imagens escuras por causa da entropia).

## 6. Limites declarados pelos autores

- As métricas estéticas são "proxies alinhados a pessoas dentro da distribuição de estilos testada", não medidas universais de qualidade visual; trazem premissas culturais e de domínio e podem pedir recalibração fora dela.
- O conjunto é sobretudo em inglês e voltado a comunicação profissional global; o QuizBank depende do modelo de visão escolhido; a editabilidade tem teto por formato (sistema de imagem nunca passa de certo nível).

## 7. Tudo o mais que ensina

- **Os prompts do juiz de linha de base** (Figuras 24 e seguintes) pesam "Advanced_Design: gradientes, sombras, animações, efeitos de profundidade" como qualidade e pedem nota inteira de 0 a 10 por subcritério; o arena pede vencedor, diferença de 1 a 5 e confiança. Leitura nossa: um prompt que premia degradê e sombra mede outra coisa que a régua da casa, que trata isso como marca de cara de IA.
- **A comparação é entre sistemas muito diferentes** (o mesmo pedido, nove geradores) e no nível do deck: é a situação de diferença grossa, em que métricas e juízes costumam ir melhor; não há teste entre duas versões parecidas de um mesmo deck.
- **Editabilidade (PEI):** a maioria dos sistemas comerciais chega ao nível 2 ("vetor visual", parece certo mas sem estrutura semântica), o que os autores chamam de "amnésia estrutural".
- **Conteúdo:** Zhipu lidera o QuizBank (88,29%); temas de negócio são os mais difíceis (61,61%); Skywork-Banana lidera a estética (27,28 contra 26,58 do segundo).
- **Trabalhos citados para estética calculada:** AIM (Oulasvirta et al., 2018), NIMA (Talebi e Milanfar, 2018), harmonia de cor (Cohen-Or et al., 2006), colorido (Hasler e Süsstrunk, 2003), entropia de sub-bandas (Rosenholtz et al., 2007), linha narrativa (Duarte, 2010) e carga cognitiva (Sweller, 1988).

## Onde está o integral
Não entra aqui: a licença não permite uso comercial, e o repositório serve a um negócio (regra em `knowledge/sources/README.md`). O texto integral está em https://arxiv.org/abs/2601.09487 (PDF e HTML na própria página). A ficha acima é o que as sínteses citam.
