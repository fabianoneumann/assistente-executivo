---
titulo: "AesthetiQ: Enhancing Graphic Layout Design via Aesthetic-Aware Preference Alignment of Multi-modal Large Language Models"
tipo: paper
autor: "Sohan Patnaik, Rishabh Jain, Balaji Krishnamurthy, Mausoom Sarkar"
url: "https://arxiv.org/abs/2503.00591"
publicado_em: 2025-03-01
capturado_em: 2026-11-01
licenca: "CC BY-NC-ND 4.0 (indicada na página do arXiv, link creativecommons.org/licenses/by-nc-nd/4.0/); só a ficha entra (licença não comercial)"
areas: [agent-engineering, content-design]
tags: [vlm-as-judge, pairwise-judgment, layout-generation, preference-alignment, dpo, alignment-metric, overlap-metric, human-agreement, adobe, crello]
---

Ficha em palavras próprias; o texto integral (licença CC BY-NC-ND 4.0, não comercial) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 01/03/2025, a única versão, com o comentário "Accepted for publication in CVPR 2025". Autores da MDSR, Adobe (Patnaik e Jain com contribuição igual). Texto extraído do PDF com `pdftotext`; as Tabelas 1 e 4 conferidas na extração com layout. Lido para a rodada investigativa; é a origem do juiz de pares (M-Judge) que o Graphic-Design-Bench usa (`2026-10-31-graphic-design-bench.md`) e do gerador sobre o qual o DesignSense montou os pares (`2026-10-24-designsense-preferencia-de-layout.md`).

## 1. A pergunta

Geradores de layout tratam o design como prever coordenadas (x, y, largura, altura) e otimizam a distância ao layout verdadeiro. Quando vários layouts são bons, essa perda castiga as alternativas boas, e reduzir os elementos a números joga fora hierarquia, atributos e contexto. A proposta: treinar um modelo multimodal para gerar layouts e alinhá-lo à preferência estética de outro modelo multimodal que olha o layout **renderizado**, por preferência direta (DPO), em vez de só imitar coordenadas.

## 2. O método (AAPA)

- **Gerador:** InternVL (1B a 8B), recebe o canvas e a lista de elementos (texto, imagem, categoria) e devolve as caixas; pré-treino em 80 mil templates de uma plataforma de design.
- **Juiz (M-judge):** um modelo multimodal recebe **duas** imagens renderizadas e devolve só qual é melhor (`{"better layout": "image 1"}` ou `"image 2"`), sem justificativa e sem empate. O prompt lista cinco critérios: estética, clareza, usabilidade, criatividade e consistência com princípios de design. Na publicação, o juiz é o VILA-7B (aberto, licença amigável); no suplementar, também GPT-4o.
- **Por que pares e não nota:** os autores relatam que dar nota a layouts isolados foi difícil, porque os modelos dão notas parecidas a layouts diferentes ("limited exposure to the design space"); por isso o juiz só compara e escolhe o melhor e o pior entre candidatos, que viram os pares de preferência do DPO.
- **Filtro por métricas de qualidade antes do juiz:** só entram no treino os layouts cuja média de duas medidas calculadas nas caixas fica acima de "média menos um desvio" do conjunto:
  - **Alinhamento (Q_align):** para cada elemento, a menor distância de cada uma das três referências horizontais (esquerda, centro, direita) e verticais (topo, centro, base) à do vizinho mais próximo, passada por uma função exponencial; quanto mais referências coincidem, maior.
  - **Sobreposição (Q_overlap):** um menos a área de interseção de cada par de elementos sobre a área do elemento, em média.
  - Sem o filtro, o modelo de 4B perde 4,97 pontos de IoU e 2,56 de taxa de vitória.

## 3. Avaliação

- **Dados:** Crello (23.302 templates vetoriais de redes sociais, banners etc.; 1.971 de teste) e WebUI (70 mil páginas; como só tem categorias e caixas, a "renderização" do juiz é de caixas sobre fundo).
- **Métricas:** IoU médio contra o layout verdadeiro, em três modos, e **taxa de vitória contra o layout humano verdadeiro** segundo o juiz.
- **Crello (Tabela 1):** AesthetiQ-8B com IoU de 42,83% e vitória de 17,19% contra o layout humano; LayoutNUWA 25,74% e 5,58%; LACE 23,18% e 3,51%; FlexDM 0,93%; o 1B fica em 2,43%. WebUI: o 8B chega a 48,29% de IoU e 24,48% de vitória.
- **Com GPT-4o no lugar do VILA (Tabela 4, só o 8B):** treinar com GPT-4o como juiz sobe o IoU (44,79%); avaliado pelo VILA, 19,41% de vitória, e pelo GPT-4o, 15,74%. Os dois juízes dão taxas diferentes ao mesmo gerador.

## 4. O juiz contra pessoas (suplementar, seção 7)

- **22 voluntários**, "diversos" em idade, gênero, ocupação e religião, 30 perguntas cada, em dois estudos.
- **Estudo 1:** escolher o melhor entre os layouts de quatro métodos, por estética, alinhamento, sobreposição de texto e imagem e se o texto faz sentido: AesthetiQ 78,41%, LayoutNUWA 19,37%, LACE 2,22%, FlexDM 0%.
- **Estudo 2:** pares de layouts gerados; a escolha das pessoas bate com a do VILA em **78,8%**; o GPT-4o chega a **88,6%** (os autores chamam de "correlação", mas o número é de concordância).
- **O que o artigo não diz:** quantos pares havia no estudo 2, se a posição (imagem 1 ou 2) foi alternada, a concordância entre as próprias pessoas, nem quão diferentes eram os layouts de cada par. No estudo 1, a distância entre os métodos é enorme (FlexDM nunca escolhido), o que sugere pares com diferença grossa.

## 5. Limites (leitura da captura)

- A validação do juiz é pequena e sem os controles que a base já sabe que pesam no juiz de pares (troca de ordem, empate, pares parecidos; `knowledge/agent-engineering/vieses-do-juiz-llm-e-defesas.md`).
- A medida principal ("vence o layout humano") é dada pelo mesmo tipo de juiz usado no treino; treinar e medir com o mesmo juiz é o laço que a base trata como superotimização.
- O filtro por alinhamento e sobreposição é heurística de curadoria, não foi validado contra pessoas no artigo.

## 6. Tudo o mais que ensina

- **Escala ajuda:** do 1B ao 8B, a vitória vai de 2,43% a 17,19% no Crello; o 1B quase não ganha com o AAPA porque não gera candidatos bons o bastante para a preferência ter o que escolher.
- **Pré-treino** em 80 mil templates sobe o IoU do 8B de 37,64% para 40,81% e, segundo os autores, ensina "minimizar sobreposição, alinhar, pôr o importante em regiões salientes".
- **Crítica às métricas de coordenada:** IoU e deslocamento de borda (BDE) não captam considerações estéticas sutis; é o argumento para pôr um juiz de imagem na avaliação.
- **Trabalhos relacionados citados:** LayoutGAN++, LayoutDM, LACE (que otimiza alinhamento e sobreposição), PosterLLaVa, LayoutNUWA, LayoutPrompter, FlexDM, Desigen, SmartText+.

## Onde está o integral
Não entra aqui: a licença não permite uso comercial, e o repositório serve a um negócio (regra em `knowledge/sources/README.md`). O texto integral está em https://arxiv.org/abs/2503.00591 (PDF e HTML na própria página). A ficha acima é o que as sínteses citam.
