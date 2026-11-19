---
titulo: "Graphic-Design-Bench: A Comprehensive Benchmark for Evaluating AI on Graphic Design Tasks"
tipo: paper
autor: "Adrienne Deganutti, Elad Hirsch, Haonan Zhu, Jaejung Seol, Purvanshi Mehta"
url: "https://arxiv.org/abs/2604.04192"
publicado_em: 2026-04-05
capturado_em: 2026-10-31
licenca: "CC BY 4.0 (indicada na página do arXiv, link para creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering, content-design]
tags: [vlm-as-judge, graphic-design, benchmark, typography, layout-understanding, design-metrics, lica-dataset, claude-opus, pixel-metrics, human-evaluation-gap]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 05/04/2026 e v2 em 07/04/2026; lida a v2 (68 páginas com apêndices). Sem comentário de venue no arXiv: é preprint. Autores da Lica World (e-mails @lica.world), listados em ordem alfabética; correspondência com Purvanshi Mehta. Código no PDF: https://github.com/purvanshi-lica/lica-bench (o artigo-filho aponta https://github.com/lica-world/GDB). Texto extraído do PDF da v2 com `pdftotext`; as Tabelas 5, 30 e 65 foram conferidas nas páginas renderizadas. Lido para a pesquisa de avaliadores do experimento noturno de 2026-11-01. **Relação com o TypoBench:** a seção 4 (tipografia) virou o artigo de workshop "A Typography Benchmark for Co-Creative Graphic-Design Agents" (ICML 2026, ficha `2026-10-31-typobench-tipografia-para-agentes-de-design.md`), que reavaliou os modelos com números diferentes para Gemini e Claude (os do GPT-5.4 são iguais); os números abaixo são os do GDB v2.

## 1. A pergunta

Benchmarks medem qualidade perceptual de imagem natural ou perguntas visuais genéricas; nenhum capta o trabalho de design profissional, estruturado, guiado por intenção e em camadas. Os autores apontam quatro diferenças do design: satisfazer várias restrições ao mesmo tempo (um banner tem de renderizar o texto legível, respeitar hierarquia tipográfica, cair no grid e chamar para a ação); precisar de métricas próprias (legibilidade por OCR, IoU de caixa, distância de cor perceptual), que FID e CLIPScore não captam; padrões que mudam com cultura, plataforma e tempo; e dependência de marca, sem uma solução única certa. O artigo ataca só as duas primeiras; as duas últimas ficam como problemas abertos.

## 2. O benchmark

- **Dados:** o LICA (Hirsch et al. 2026), templates reais de uma plataforma comercial de design, com a estrutura de camadas preservada: tipo de cada componente (texto, imagem, vetor, grupo), caixa, ordem de empilhamento e estilo; texto com família, tamanho, peso, cor, alinhamento, espaçamento, altura de linha, curvatura, rotação e faixas de estilo; metadados globais (proporção, cor de fundo, categoria e subcategoria, descrição da intenção, etiquetas estéticas, paleta); e, no subconjunto animado, tipo de movimento (32 categorias), duração, início e quadros-chave. Templates "irmãos" (mesmo tema, conteúdo ou cor diferentes) permitem tarefas de variante.
- **49 tarefas em cinco domínios, cada um em compreensão e geração (Tabela 2):** layout (8 e 4), tipografia (10 e 2), infográficos e SVG (5 e 5), template e semântica (5 e 2), animação (5 e 3).
- **Tamanhos:** tarefas de layout nos 989 layouts sem vídeo; tarefas por componente com até três por layout (cerca de 2.500 instâncias); geração em 100 amostras na maioria (custo das APIs); 300 SVGs; 50 Lottie; 100 animações; 10 briefings de vídeo; 13 layouts na adaptação de proporção. Os autores afirmam que as diferenças entre modelos são em geral uma ordem de grandeza maiores que a incerteza estatística, sem mostrar intervalos.
- **Modelos:** Gemini-3.1-Pro, Gemini-3.1-Flash-Lite, Gemini-3.1-Flash-Image, GPT-5.4, GPT-Image-1.5, Claude-Opus-4.6, Sora-2 e Veo-3.1, todos fechados, por API, temperatura 0, um prompt fixo por tarefa (apêndice B). Algumas tarefas variam a entrada: só texto (JSON do layout), só imagem (PNG) ou os dois.
- **Régua de solvabilidade, definida com especialistas em design:** quase resolvida acima de 95% do melhor modelo; parcialmente entre 80% e 95% (ou quando uma subcondição é tratável e outra não); não resolvida abaixo de 80% ou com distância estrutural. O corte é alto porque "even small errors (e.g., a few pixels) typically require manual correction".
- **Taxonomia de métricas (seção 2.1):** espaciais (mIoU, F1 de caixa, mAP no protocolo COCO, MAE); perceptuais (LPIPS, SSIM, DreamSim, FID, PSNR); semânticas (CLIPScore, PickScore, BERTScore, cosseno de embeddings); preferência humana aprendida (NIMA, ImageReward, HPSv3); fidelidade de texto (OCR, acerto de família, ΔE CIEDE2000 com limiar 5); validade estrutural (JSON e SVG válidos, taxa de compressão); correlação de ordem (τ de Kendall, ρ de Spearman); agrupamento (ARI, AMI, V-measure, FMI); e um juiz: o **M-Judge** (do AesthetiQ, Patnaik et al., CVPR 2025), taxa de vitória em pares em que um modelo multimodal compara a saída com o layout verdadeiro, dada a intenção, e escolhe o melhor por estética, clareza, usabilidade, criatividade e consistência. O prompt (Tabela 65) pede só o JSON com "image_1" ou "image_2", sem explicação; o artigo não diz qual modelo faz o papel de juiz nem se a ordem das duas imagens é alternada.

## 3. Composição (seção 3)

**Compreensão de layout (Tabela 5 e seguintes; 989 layouts, 15,7 componentes em média, mediana 12):**
- Proporção do canvas (9 classes): GPT-5.4 93,9% (F1 0,679); Gemini-Flash-Lite 23,6%; Gemini-Pro 24,5%; Claude-Opus-4.6 9,3% (F1 0,179).
- Contar elementos: MAE 5,81 (GPT-5.4), 6,46 (Claude), 12,35 e 12,50 (Gemini); erros de cauda pesada nos layouts complexos.
- Tipo do componente (texto, imagem, vetor, grupo; 2.943 amostras): no máximo 46,1% (GPT-5.4); Claude 7,2%. Os modelos reconhecem texto, falham em imagens e vetores.
- Detecção de componentes: mAP@0,5 de no máximo 6,4% (GPT-5.4), ordens de grandeza abaixo de benchmarks de imagem natural.
- Ordem de empilhamento (τ de Kendall, em que 0,5 é aproximadamente aleatório): 0,567 (Flash-Lite), 0,495, 0,492, 0,542 (Claude). Não se correlaciona com as outras tarefas de layout; a Figura 4 mostra o GPT-5.4 enterrando texto e forma atrás do fundo.
- Rotação de imagem: acerto binário de 71,6% a 80,0%, mas erro só nos rotacionados acima de 69° em todos.
- Forma do recorte e moldura: Claude lidera (recorte 76,9%, moldura F1 0,504), apesar de ficar atrás nas outras; os autores chamam isso de capacidade ortogonal.

**Geração de layout (Tabelas 9 a 12):**
- Da intenção ao layout (100 amostras): GPT-Image-1.5 e Gemini-3.1-Flash-Image empatam em alinhamento e estética (PickScore 20,21 e 19,81; NIMA 5,18 e 5,14), mas o OCR fica em 75,4% e 72,6%: um em cada quatro textos sai errado ou ilegível.
- Completar layout parcial (989): um elemento é tratável, vários não (mIoU 0,2413 contra 0,2007 no melhor, Gemini-3.1-Pro; M-Judge 0,29, 0,26 e 0,31 com um elemento; 0,17, 0,17 e 0,33 com vários, para GPT-5.4, Claude e Gemini).
- Inserir asset na máscara (100): troca entre preservar a identidade do asset e a harmonia do conjunto; condicionar por imagem ou por texto muda pouco.
- Adaptar a outra proporção (13 layouts, com avaliação humana binária): GPT-Image-1.5 preserva o texto (TextAcc 1,0) mas só 23% dos assets; Gemini preserva os assets (1,0) e 92% do texto; M-Judge 0,615 e 0,667. Nenhuma métrica escalar capta o problema.

## 4. Tipografia (seção 4; 2.568 elementos de 989 layouts)

**Tabelas 15 e 16 (família acc; cor ΔE e fração ΔE<5; tamanho MAE px; peso acc; alinhamento acc; altura de linha MAE; espaçamento MAE em):**
- Gemini-3.1-Flash-Lite: 0,065; 52,41 e 0,118; 38,42; 0,390; 0,428; 43,88; 0,045.
- Gemini-3.1-Pro: 0,047; 54,97 e 0,114; 35,53; 0,407; 0,441; 42,16; 0,038.
- GPT-5.4: 0,237; 5,57 e 0,633; 8,97; 0,552; 0,851; 15,66; 0,016.
- Claude-Opus-4.6: 0,006; 14,05 e 0,382 (matiz 69,6%); 10,84; 0,491; 0,861; 17,17; 0,034.

**Leitura dos autores:** fonte fraca em todos (23,7% no melhor, 3,6 vezes o segundo, F1 macro uma ordem de grandeza menor); cor muito variável (os Gemini devolvem cores sem relação com a verdade; a Figura 9 diz que o Gemini-Pro devolve texto vazio em várias perguntas de cor e o Flash-Lite responde #000000 sempre); tamanho e altura de linha com diferenças de até 4 vezes entre modelos; espaçamento o mais fácil; alinhamento o mais estável (86,1% no Claude). Texto curvo (26 elementos): GPT-5.4 88,5%, Claude 92,3%, os dois Gemini 0% (tudo "reto"). Rotação: erro nos rotacionados de 18,67° (GPT-5.4) a mais de 54°. Faixas de estilo: IoU 0,982 (Claude) e 0,975 (GPT-5.4) contra cerca de 0,376 nos Gemini, e acerto exato 0% em todos. A Figura 10 mostra o efeito prático: tamanho e posição previstos errados pelo Gemini-3.1-Pro, re-renderizados, geram desalinhamentos e sobreposições.

**Geração (Tabelas 19 e 20):** inserir texto na máscara com IoU de no máximo 0,580 (Gemini-3.1-Flash-Image; GPT-Image-1.5 0,523), com transbordamento e alteração do entorno; no trecho isolado, fonte 0,353 e 0,100, tamanho MAE 188,7 e 104,2 px. Remover texto: as duas apagam mais de 94%, mas a reconstrução diverge (PSNR 30,22 contra 16,64; SSIM 0,944 contra 0,743; LPIPS 0,088 contra 0,331; FID 54,05 contra 115,75), e quem apaga um pouco mais (GPT-Image-1.5, 95,3% contra 94,5%) reconstrói muito pior, sinal de que inventa conteúdo na área mascarada.

**Detector de caixas (apêndice C, Tabela 66):** para medir a posição do texto gerado, um LLM acha a caixa, porque fontes artísticas derrubam o OCR; em 100 amostras, GPT-5.4 mIoU 0,863 e F1 0,919, Claude Opus 4.6 0,812 e 0,882, Gemini-3.1-Pro 0,731 e 0,829.

## 5. Infográficos e SVG (seção 5)

- Só código, sem imagem renderizada, em 300 SVGs; as perguntas de compreensão (quatro opções) foram geradas por um agente Claude Code (Opus 4.6) a partir da imagem renderizada, com resposta verificada. Perguntas perceptuais (87,0% no melhor) são mais difíceis que as semânticas (93,7%). Corrigir bugs (similaridade 0,932), otimizar código (referência SVGO, compressão de 62,6%) e editar estilo mostram forças complementares entre modelos; transformações geométricas compostas (rotação mais escala) falham em todos.
- Gerar SVG depende da entrada: com imagem, SSIM 0,918; só com texto, 0,733. GPT-5.4 e Claude quase sempre produzem SVG válido; o Gemini cai para 81% a 84% de validade com imagem, por truncar saídas longas. Lottie (animação vetorial) é viável mas longe de resolvido (FrameSSIM 0,598 no melhor; o Gemini cai de 100% para 66% de validade com imagem).

## 6. Template e semântica (seção 6)

- **Categoria do template (Tabela 30, 989 pais e 858 subcategorias):** com vocabulário aberto, os modelos dão rótulos razoáveis mas lexicalmente diferentes ("social media graphic" em vez de "Instagram post") e erram: Gemini-3.1 45,50%, GPT-5.4 11,42%, Opus-4.6 17,08%. Dando a lista fechada, sobem 30 a 62 pontos: Opus-4.6 78,66% (top-5 94,13%), Gemini 76,23%, GPT-5.4 55,81% (top-5 91,00%). Subcategoria (estética ou tema): no máximo 10,13% em top-1. Na matriz de confusão do Opus com lista fechada, planner e calendário (0,98) e currículo (0,94) quase perfeitos; educação (0,31) e redes sociais (0,40) se confundem.
- **Intenção do usuário em uma frase:** todos ficam a 1 ponto um do outro (BERTScore 88,5 a 89,6; cosseno 91,4 a 92,7). Os autores advertem que essas métricas premiam proximidade de tema, não o objetivo exato, e que uma imagem admite várias intenções; o Gemini-3.1-Pro ficou de fora porque o raciocínio longo inflava a saída e derrubava as métricas.
- **Reconhecer variantes do mesmo template (Tabela 32):** a linha de base trivial de Jaccard das fontes iguala ou supera os LLMs nas três subtarefas (97,7% em pares, MRR 96,3%, ARI 92,8%): os modelos não usam a consistência tipográfica como pista de agrupamento. Ordenar e decidir em pares se dissociam: o GPT-5.4 tem MRR de 99,35% ao ordenar, mas 62,60% de acerto ao decidir "mesmo ou diferente", porque responde "diferente" em 874 de 1.000 pares (precisão 1,0, revocação 0,25). Os erros: confundir linguagem de design compartilhada com conteúdo parecido (paleta quente igual vira "mesmo template"), ordenar por aparência de superfície, juntar grupos de paleta parecida ou violar o número pedido de grupos.
- **Gerar variante (completar estilo e recolorir):** a validade do JSON é o que separa os modelos (GPT-5.4 pelo menos 94%; Gemini-3.1-Pro no máximo 83%, 55% numa tarefa); recolorir preserva posição e área (cerca de 100%) mas cobre só 77,6% da paleta. A Figura 22 mostra métricas de pixel punindo saídas coerentes de estilo que trocaram o papel das cores (SSIM 0,367 e 0,322), enquanto saídas inconsistentes de estilo pontuam mais.

## 7. Animação (seção 7)

Gemini recebe o vídeo; GPT e Claude, quadros-chave amostrados. Ordenar quatro quadros-chave: acerto exato de 14% a 16%, acerto em pares só cerca de 10 pontos acima do acaso, embora o primeiro quadro seja achado em 67% a 80%. Classificar o tipo de movimento (32 primitivos de interface, como tumble, pop, stomp): abaixo de 13% em todos, quase zero em cenas de um só componente; dar a lista de rótulos melhora pouco o Claude e piora o Gemini. Duração do vídeo com MAE acima de 6 s; decompor a cena é o gargalo. Gerar animação a partir de layout estático e parâmetros: os modelos aplicam um movimento global, animam o componente errado ou alucinam movimento; métricas de quadro (FID, LPIPS) não dizem se a animação certa foi aplicada ao componente certo. No vídeo curto de marketing a partir de um briefing (avaliação humana em 10 amostras), o Sora-2 renderiza texto certo em 79% e o Veo-3.1 em 69%.

## 8. Discussão e limites declarados

- **Mapa de solvabilidade (Tabela 47):** 2 tarefas quase resolvidas (casar e ordenar templates, em que linhas de base não neurais empatam), 25 parcialmente, 22 não resolvidas (a Tabela 47 diz 23; o texto da seção 8.2 e a conclusão dizem 22, que é o número que fecha 49 com 2 e 25). Entre as não resolvidas, em tipografia: família, cor, tamanho, peso e altura de linha. O fio comum: qualquer coisa que exija saída estruturada precisa ou discriminação fina bate num teto.
- **Por que importa, segundo os autores:** no fluxo real, uma sugestão quase certa costuma ser pior que nenhuma, porque o designer tem de parar, achar o erro, corrigir e reavaliar; para auditar marca (fonte certa, cor dentro do guia), as taxas de erro medidas são "complete breakdowns", não margens aceitáveis.
- **Lacunas de avaliação que os próprios autores apontam:** métricas de pixel não distinguem uma transformação correta de uma alucinada quando as duas se afastam igualmente da fonte, e o design precisa de métricas sobre primitivas extraídas (caixas, propriedades de fonte, tokens de cor); a avaliação humana quase não existe (fora pequenos julgamentos de preferência na geração), e um designer julga na hora se um layout é usável ou uma fonte está na marca, sinal que nenhuma métrica automática capta; só modelos fechados; a avaliação quebra perto de desempenho zero; contextos culturais, de plataforma, de acessibilidade e de domínio (editorial, embalagem) não cobertos.
- **Próximos passos anunciados:** modelos abertos, estudo sistemático de prompts, referência de desempenho humano com designers ("currently underway"), outros conjuntos de dados e ablações entre tarefas (se quem vai bem em tipografia também vai bem em gerar texto estilizado).

## 9. Tudo o mais que ensina

- **As métricas de preferência aprendidas** (NIMA, ImageReward, HPSv3, PickScore) foram treinadas em foto ou texto-para-imagem; os autores as usam como sinal de estética, mas a própria discussão diz que não capturam requisitos de design.
- **Rótulo aberto contra fechado** muda a ordem dos modelos (o Gemini lidera aberto, o Claude lidera fechado): o vocabulário de design interno de cada modelo é diferente, e o mesmo template pode ser rotulado de modo diferente em cada ferramenta.
- **Viés de decisão binária:** um modelo que ordena bem pode decidir mal em pares quando adota um limiar conservador; a calibração da ordem relativa não garante a decisão absoluta.
- **Linhas de base simples** (Jaccard de fontes, CLIP, DINOv2, LPIPS, distância de paleta, atributos estruturais) devem acompanhar qualquer comparação com LLM, porque às vezes empatam ou vencem.
- **Trabalhos citados:** COLE e OpenCOLE (cartaz a partir de briefing), Graphist, LaDeCo, IGD, CreatiPoster, Accordion, SVGenius (estratificação de complexidade de SVG), AesthetiQ (origem do M-Judge), DreamSim, HPSv3, ImageReward, Pick-a-Pic, WCAG 2.0.
- **Apêndices:** definições formais das métricas (A), todos os prompts por tarefa (B) e a escolha do detector de caixas (C).

---
