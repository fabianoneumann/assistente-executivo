---
titulo: "A Typography Benchmark for Co-Creative Graphic-Design Agents"
tipo: paper
autor: "Jaejung Seol, Elad Hirsch, Haonan Zhu, Adrienne Deganutti, Purvanshi Mehta"
url: "https://icml.cc/virtual/2026/68576"
publicado_em: 2026-07-11
capturado_em: 2026-10-31
licenca: "Protegido: o PDF de camera-ready traz 'Copyright 2026 by the author(s)', sem licença aberta; o site do workshop publica os artigos como 'non-archival reports'; a página do OpenReview (onde poderia constar uma licença) recusou o acesso (403 com verificação anti-robô, também na API) e a Wayback Machine respondeu 429. Entra só a ficha."
areas: [agent-engineering, content-design]
tags: [vlm-as-judge, typography, font-recognition, graphic-design, benchmark, text-rendering, text-removal, design-editing, lica-dataset, claude-opus]
---

Ficha de estudo, em palavras próprias; sem texto integral. Artigo curto (8 páginas e apêndices, 13 no total) apresentado como pôster no Workshop on Human-AI Co-Creativity: Advances, Opportunities, and Challenges do ICML 2026 (Seul), sessão de 11/07/2026, "Paper #16" na numeração do workshop; não é artigo da trilha principal do ICML. Autores da Lica World (San Francisco); correspondência com Purvanshi Mehta. Benchmark e código em https://github.com/lica-world/GDB. Lido o PDF de camera-ready baixado do site do workshop (https://genaicreativity.org/icml2026/files/16/16_paper.pdf), extraído com `pdftotext`; as Tabelas 3 e 4 foram conferidas na página renderizada. O PDF que o OpenReview serve (https://openreview.net/pdf/ebe237c13afa71b973aeac3aacca599944ae7b6c.pdf, fórum `KAVgwI5UO5`) não abriu (403), então não foi possível confirmar se é idêntico. Lido para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Relação com o Graphic-Design-Bench (arXiv 2604.04192, ficha `2026-10-31-graphic-design-bench.md`):** o TypoBench é o recorte de tipografia do GDB, dos mesmos cinco autores (em outra ordem) e sobre o mesmo corpus (989 layouts, 2.568 elementos de texto do LICA). Não é cópia: o TypoBench reavaliou os modelos e os números mudaram. GPT-5.4 tem os mesmos números nos dois; Gemini-3.1-Pro e Gemini-3.1-Flash-Lite, que no GDB v2 apareciam quase no zero (fonte 4,7% e 6,5%, cor com ΔE acima de 52, nenhuma curva detectada, porque devolviam respostas vazias ou cor fixa), passam a liderar várias tarefas no TypoBench (Gemini-3.1-Pro com 29,9% em fonte e ΔE 4,81); Claude-Opus-4.6 também muda (fonte de 0,6% para 9,8%, tamanho de 10,84 para 9,55 px). A geração troca GPT-Image-1.5 e Gemini-3.1-Flash-Image por GPT Image 2 e Gemini 3 Pro Image. O artigo não comenta a diferença.

## 1. A pergunta

Quando um designer pede a um colaborador de IA "deixe este título mais confiante" ou "use a mesma fonte da referência", a conversa é tipográfica: família, peso, tamanho, cor, alinhamento, espaçamento, curvatura e ênfases dentro da linha codificam hierarquia, tom e marca. Os benchmarks de texto em imagem medem se o gerador soletra certo; quase nunca perguntam se usou a família pedida, a cor certa, se ficou dentro da região e se preservou o resto. A pergunta: modelos de visão de fronteira leem e reproduzem a camada tipográfica com a fidelidade que o trabalho de design pede?

## 2. O benchmark

- **Corpus:** templates reais em camadas (o LICA, Hirsch et al. 2026, arXiv 2603.16098), em que cada componente de texto traz a especificação completa: família, tamanho em px, peso CSS (100 a 900), cor RGB, alinhamento, espaçamento entre letras (em), altura de linha (px), curvatura (−100 a +100), rotação e faixas de estilo dentro do texto. Isso permite medir contra o valor real, não contra opinião.
- **Doze tarefas em três grupos.** Dez de compreensão sobre 2.568 elementos de 989 layouts sem vídeo (até três elementos por layout, para conter custo): família da fonte (2.556 amostras, 167 famílias em cauda longa puxada por Poppins, Montserrat e Roboto), cor do texto em hex (2.498; 58 sem valor), tamanho, peso, alinhamento (quatro classes), altura de linha, espaçamento entre letras, texto curvo com curvatura, faixas de estilo (intervalos de caracteres com estilo distinto) e rotação. Duas de geração: texto estilizado (inserir texto numa máscara do layout, ou gerar o trecho isolado, a partir de uma especificação) em 100 amostras quadradas com fontes livres do Google; e remoção de texto com reconstrução do fundo em 100 templates (lado maior de pelo menos 1.024 px, proporção abaixo de 2).
- **Modelos:** GPT-5.4, Claude-Opus-4.6, Gemini-3.1-Pro e Gemini-3.1-Flash-Lite na compreensão; GPT Image 2 e Gemini 3 Pro Image na geração. Temperatura 0, um prompt fixo por tarefa (no apêndice B), igual para todos. Os autores dizem que o objetivo não é ranquear modelos, mas mostrar onde o campo inteiro falha.
- **Métricas "nativas de design":** acerto exato para família e alinhamento; erro absoluto médio (MAE) para tamanho, altura de linha e espaçamento; ΔE (CIEDE2000) para cor, com ΔE < 5 como "perceptualmente aceitável", mais distância RGB e acerto de matiz em 8 faixas; IoU de faixas e acerto exato (intervalo e todas as propriedades dentro dele); IoU e F1 da região gerada; LPIPS, SSIM, FID, CLIP e DINO para qualidade; RMSE de preservação fora da máscara; ausência de texto (transcrição pelo GPT-5.4 não contém mais o texto alvo) e ReMOVE (métrica sem referência da naturalidade do apagamento); PSNR e SSIM da reconstrução.
- **Régua de "resolvido":** não resolvida se o melhor modelo fica abaixo de 80% do limiar utilizável; parcialmente entre 80% e 95%; quase resolvida acima de 95%.

## 3. Resultados de compreensão (Tabelas 3 a 5)

**Tabela 3 (por modelo: família acc e F1; cor ΔE, RGB ℓ2, fração ΔE<5, matiz; tamanho MAE px; peso acc; alinhamento acc; altura de linha MAE px; espaçamento MAE em):**
- Gemini-3.1-Flash-Lite: 0,165 e 0,040; 8,94, 28,2, 0,487, 0,803; 10,70; 0,562; 0,857; 17,05; 0,026.
- Gemini-3.1-Pro: 0,299 e 0,110; 4,81, 15,8, 0,687, 0,895; 10,46; 0,649; 0,879; 16,67; 0,012.
- GPT-5.4: 0,237 e 0,055; 5,57, 20,0, 0,633, 0,881; 8,97; 0,552; 0,851; 15,66; 0,016.
- Claude-Opus-4.6: 0,098 e 0,025; 14,52, 49,7, 0,375, 0,675; 9,55; 0,467; 0,869; 15,62; 0,034.

**Os cinco padrões que os autores tiram:**
- **Reconhecer a fonte é a tarefa mais longe de resolvida:** no máximo 29,9% de acerto em 167 famílias, com F1 macro muito menor. Os acertos se concentram nas fontes frequentes ou muito marcadas; as dez famílias mais comuns cobrem cerca de 60% dos elementos, as outras 157 aparecem menos de 100 vezes cada, e três quartos das famílias têm F1 zero em todos os modelos. Exemplo da Figura 1: a verdade é Lora; GPT-5.4 diz Cormorant Garamond (acerta o estilo serifado, erra a família), Gemini-Lite diz Montserrat, Gemini-Pro diz Bebas Neue (categorias inteiras erradas).
- **Cor é tratável, mas desigual entre fornecedores:** Gemini-3.1-Pro chega a ΔE 4,81 com 68,7% abaixo de 5; Claude fica em 14,52. Qualitativamente, os modelos às vezes devolvem a cor oposta (branco em vez de preto: a verdade rgb(1,1,1), GPT-5.4 responde #FFFFFF).
- **Propriedades tipográficas, parcialmente:** alinhamento e espaçamento entre letras vão bem; tamanho e altura de linha são os maiores erros contínuos. O erro de tamanho fica numa faixa estreita (cerca de 9 a 11 px) em todos, o que os autores leem como limite geral de medir tipografia a partir de pixels, não de um fornecedor.
- **Atributos geométricos raros são detectáveis, mas frágeis (Tabela 4):** só 26 elementos curvos (1%), então a acurácia geral (0,975 a 0,999) é dominada pela maioria reta; nos curvos, detecção de 0,846 (Flash-Lite), 0,962 (Pro), 0,885 (GPT-5.4) e 0,923 (Claude), com erro de curvatura alto (41,77; 75,08; 43,77; 79,92). Rotação: acerto binário 0,972 a 0,987; erro só nos rotacionados de 12,59° (Pro) a 30,79° (Claude). A Figura 1 mostra um texto claramente em arco (curvatura 55) dado como reto.
- **Localizar as faixas de estilo é possível, recuperar a especificação delas não (Tabela 5):** IoU das faixas de 0,972 a 0,982 (Claude 0,982), mas acerto exato 0% em todos os modelos e estratos (1 faixa, n = 2.530; 2 ou mais, n = 26, com IoU de 0,752 a 0,824). O modelo vê onde está a ênfase, mas não diz o que a torna diferente (família, peso, tamanho, cor), o que, para os autores, impede reaplicar a ênfase em outro lugar.

## 4. Resultados de geração (Tabelas 6 e 7)

- **Inserir texto estilizado na máscara (Tabela 6, layout):** GPT Image 2 com IoU 0,648, F1 0,766, fonte 0,420, alinhamento 0,680, tamanho MAE 47,27 px, cor 9,02, LPIPS 0,070, SSIM 0,907, RMSE de preservação 16,77; Gemini 3 Pro Image com IoU 0,542, F1 0,674, fonte 0,430, alinhamento 0,710, tamanho 31,70, cor 10,76, LPIPS 0,077, SSIM 0,921, preservação 13,67. O texto gerado transborda a região ou mexe nos pixels vizinhos; o gargalo, dizem os autores, não é desenhar texto, é confinar a edição à máscara preservando o resto.
- **Trecho isolado (element):** fonte 0,300 e 0,350, alinhamento 0,710 e 0,780, tamanho MAE acima de 100 px (107,10 e 187,97), cor 13,49 e 22,72. O contexto do layout ajuda a calibrar a escala (Gemini de 187,97 para 31,70 px), mas não resolve.
- **Remover texto (Tabela 7):** GPT Image 2 apaga mais (ausência de texto 1,000 contra 0,929; ReMOVE 0,954 contra 0,939), mas o Gemini 3 Pro Image reconstrói e preserva melhor (FID 39,97 contra 49,08; LPIPS 0,064 contra 0,082; PSNR 27,96 contra 27,10; SSIM 0,918 contra 0,911; RMSE de preservação 17,32 contra 22,72). Passar no teste de apagamento não é o mesmo que entregar uma edição reaproveitável.

## 5. Como o artigo mede com modelos (apêndices E e F)

- Para achar a caixa do texto gerado, usam um detector baseado em LLM, porque fontes artísticas, espaçamento extremo, curvas e efeitos derrubam o OCR comum. Escolhido em 100 amostras com caixa real (Tabela 8): GPT-5.4 com mIoU 0,863, precisão 0,946, revocação 0,905, F1 0,919; Gemini-3.1-Pro 0,731, 0,865, 0,797, 0,829; Claude Opus 4.6 0,812, 0,863, 0,922, 0,882 (maior revocação). Todos devolveram caixa em 100% dos casos.
- Para a "ausência de texto", a transcrição é do GPT-5.4, escolhido em 100 amostras com texto conhecido (Tabela 9): recupera o texto alvo em 100%, contra 90% do Tesseract e 73% do PaddleOCR.
- Para medir a tipografia de uma imagem gerada, treinam um preditor leve (Text-Params-Predictor) em renderizações sintéticas de fontes do Google, que extrai família, tamanho, alinhamento e cor do trecho renderizado.

## 6. Conclusões, recomendações e limites declarados

- Os modelos de fronteira já têm percepção tipográfica grosseira, não a confiabilidade de design. Dois sinais: 0% de acerto exato nas faixas de estilo apesar de IoU 0,982 (localizar não basta para editar); e as falhas de geração são de controle da edição, não de realismo. Nenhuma métrica sozinha captura isso; a avaliação deve combinar sinais complementares (ausência de texto, ReMOVE, sobreposição espacial, RMSE de preservação).
- Por que importa, nas palavras dos autores: quem não identifica fontes não audita conformidade de marca; quem alucina cores não harmoniza paleta; quem erra tamanho ou altura de linha não refaz o layout em outra escala; quem vaza a edição para fora da região põe o designer no papel de corretor manual.
- **Limites e próximos passos:** ampliar o conjunto de modelos (abertos, especializados em design, ajustados); estender a outras plataformas, culturas e escritas não latinas (inclusive da direita para a esquerda); e parear as métricas com um estudo com designers profissionais, "a subjective signal that no automatic metric can fully replace". Não há avaliação humana no artigo.

## 7. Tudo o mais que ensina

- **Trabalhos de geração de design citados:** COLE e OpenCOLE (cartaz a partir de briefing), Graphist, LaDeCo e IGD (geração em camadas ou por instrução), CreatiPoster e Accordion (geração editável em várias camadas), e o LICA (o corpus usado). Em todos, a tipografia aparece como subproduto da composição, não como variável controlada.
- **Benchmarks vizinhos:** SVGenius (entender e editar SVG), SlidesGen-Bench (geração de slides) e Graphic-Bench (Ki et al. 2025, planejamento de fluxos de design por agentes); nenhum isola a tipografia.
- **Texto em imagem natural:** apagar texto de cena (Scene Text Eraser, PSSTRNet) e medir legibilidade de texto gerado por OCR; os dois tratam o texto como legibilidade em tela não estruturada, enquanto aqui o canvas é composto de propósito e a fidelidade é à especificação.
- **Definições úteis:** ΔE CIEDE2000 como distância de cor perceptual, com 5 como limiar de aceitável em avaliação profissional de cor; curvatura de −100 a +100, em que ±10 é curva quase imperceptível, ±50 arco moderado e ±100 quase meio círculo (raio de cerca de 2,5 vezes o tamanho da fonte em 100 e 25 vezes em 10).
- **Os prompts** (apêndice B) pedem só o valor, sem explicação ("Respond with ONLY..."), em persona de "typography expert" ou "color expert in design", com um exemplo de saída em JSON.
- **Declaração de impacto:** o benchmark é medição, não capacidade nova; competência tipográfica confiável é pré-requisito para usos sensíveis à acessibilidade (legibilidade, contraste, cobertura de escrita).
