---
titulo: "PosterIQ: A Design Perspective Benchmark for Poster Understanding and Generation"
tipo: paper
autor: "Yuheng Feng, Wen Zhang, Haodong Duan, Xingxing Zou"
url: "https://arxiv.org/abs/2603.24078"
publicado_em: 2026-03-25
capturado_em: 2026-10-31
licenca: "Licença não exclusiva de distribuição do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/, indicada na página do arXiv); a versão do CVF Open Access diz que o copyright fica com os autores ou outros titulares. Entra só a ficha."
areas: [agent-engineering, content-design]
tags: [vlm-as-judge, poster-design, typography, layout-judgment, holistic-rating, font-perception, benchmark, text-to-image, claude-sonnet, iterative-refinement]
---

Ficha de estudo, em palavras próprias; sem texto integral. arXiv: v1 em 25/03/2026, a única versão e a lida; comentário "CVPR 2026". Publicado nos anais do CVPR 2026, pp. 29295-29304; a versão do CVF Open Access (https://openaccess.thecvf.com/content/CVPR2026/html/Feng_PosterIQ_A_Design_Perspective_Benchmark_for_Poster_Understanding_and_Generation_CVPR_2026_paper.html, PDF de 10 páginas e material suplementar à parte) é idêntica à aceita, e os números conferidos (Tabelas 4, 5 e 7) batem com o arXiv, que junta o suplementar no mesmo PDF. Autores da Hong Kong Polytechnic University (Feng, Zou, autora de correspondência), Snapchat (Zhang) e ByteDance Seed (Duan). Projeto e dados em https://github.com/ArtmeScienceLab/PosterIQ-Benchmark. Texto extraído do PDF do arXiv com `pdftotext`; as Tabelas 2 a 7 foram lidas na página renderizada. Lido para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

## 1. A pergunta

Avaliações de modelos são centradas em texto, e as de geração de imagem priorizam estética, ignorando o caráter restrito e comunicativo do design. O cartaz é o caso extremo: tema, hierarquia da informação, regras tipográficas, acoplamento de texto e imagem, coerência de estilo e público interagem de modo que métrica de uma dimensão só não capta. Para os autores, cartaz é meio de comunicação visual, feito para a mensagem ser percebida, entendida e lembrada com pouca carga cognitiva; "Design without communicative purpose yields only superficial elegance." O PosterIQ quer medir, separadamente, o que um modelo precisa para entender e gerar cartazes: ler texto e julgar legibilidade, perceber fonte, raciocinar sobre layout e hierarquia, reconhecer estilo e decodificar metáforas visuais.

## 2. O benchmark

- **Tamanho:** 7.765 instâncias de compreensão e 822 prompts de geração, 24 tipos de tarefa, com cartazes reais (de fontes livres para pesquisa, limpos à mão de borrões, artefatos e problemas de direitos), layouts profissionais (partindo de arquivos PSD) e casos sintéticos.
- **Compreensão, cinco famílias:**
  - **OCR (3.005 itens):** logotipo, cartaz real, OCR simples (palavras do Oxford 3000 em fundo branco), OCR difícil (letras sem ordem, fontes variadas, leve rotação, cores aleatórias, fundo com textura) e OCR em 14 tamanhos de fonte.
  - **Fonte (2.788):** casar a fonte entre nove candidatas que mostram outro texto (força a olhar o estilo, não as letras); atributos de fonte em pares, com 37 atributos humanos de O'Donovan et al. (2014; 31 relativos, como "boring" ou "angular", e 6 binários, como serifa ou itálico); efeitos tradicionais (nove, como negrito, sombra, contorno, entre quatro opções); efeitos avançados estilizados (identificar a cor dominante e escolher o efeito entre 48, como "composed of lava rocks").
  - **Raciocínio espacial (1.178):** localizar texto (caixas normalizadas), alinhamento e rotação do texto, espaço vazio (grade de 7 por 7 sobre um cartaz incompleto; o modelo escolhe um número pedido de células; a verdade é a interseção do que três anotadores marcaram), **comparação de layout** (um layout profissional contra uma versão que viola princípios de design de propósito; "Which poster image, A or B, has a more visually appealing layout?") e geração de layout (caixas para até cinco elementos a partir de descrição de tamanhos e posições).
  - **Design avançado (575):** estilo entre 17 (minimalista, Memphis, vaporwave, Cinema 4D etc.); composição (descrever as operações usadas: desalinhamento, divisão, aninhamento, recorte, repetição, extensão, foco, espelhamento), com cobertura julgada por LLM contra pontos anotados; intenção e metáfora (explicar cartazes como celulares empilhados que evocam um hambúrguer, soldados de brinquedo que formam uma pomba).
  - **Nota geral (219 cartazes):** o modelo dá uma nota única de qualidade.
- **Geração, cinco tarefas (822 prompts):** densa (114; temas com 10 entidades e ações), fonte (135; cartazes de texto pedindo diversidade tipográfica), estilo (256; os 17 estilos), composição (117; as mesmas técnicas da compreensão) e intenção (200; cartazes com metáfora).
- **Modelos:** compreensão com GPT-5, Claude-Sonnet-4.5, Gemini-2.5-Pro e Grok-4-fast (fechados) e MiniCPM-V-4.5, Gemma-3n-e4b-it, Qwen3-VL-4B e Qwen3-VL-8B (abertos); geração com Seedream-4.0, Gemini-2.5-Flash-Image, GPT-Image-1 e Qwen-Image.

## 3. Métricas e juízes (suplementar B e C)

- OCR de logotipo e cartaz: acerto exato por instância. OCR sintético: revocação de blocos de cinco caracteres; Δ entre simples e difícil (robustez); desvio padrão entre tamanhos (estabilidade).
- Múltipla escolha normalizada para que o chute dê zero: Score = max(0, (k·a − 1)/(k − 1)), com k opções e acerto a. Em pares (k = 2), Score 0,7 equivale a 85% de acerto.
- Layout: IoU das maiores caixas; revocação do número de caixas pedidas; na geração de layout, desvio do centro e razão de área (não há posição única certa).
- **Nota geral contra humanos:** humanos e modelos dão nota de 0 a 10 (o prompt do modelo pede de 1 a 10, ponderando tipografia, composição do layout e metáfora e estética, e só o número); as duas séries são centradas na média e comparadas por similaridade de cosseno. A verdade humana: vários anotadores por cartaz, distribuições padronizadas (média zero, variância normalizada), cartazes com amplitude de notas acima de um limiar descartados, média dos restantes.
- **Juízes de modelo:** GPT-5 confere a cobertura de pontos-chave na compreensão de intenção e composição e na geração densa e de intenção; Gemini-2.5-Pro na geração de composição; GPT-5 classifica o estilo gerado e descreve a tipografia gerada no vocabulário dos 37 atributos (riqueza = cobertura média dos atributos). Uma descrição só conta como acerto se cobrir todos os pontos anotados.
- **Validação humana dos juízes:** num subconjunto, o juiz de LLM concorda com humanos em cerca de 92% nas tarefas de compreensão com julgamento textual; na geração, 30 imagens por tarefa avaliadas por humanos mantêm a ordem relativa dos geradores "largely consistent". Não há números por tarefa nem tamanho do subconjunto.
- **Anotação:** pelo menos três anotadores especialistas por amostra nas tarefas de layout, design avançado e nota; um anotador líder revisa, resolve divergências e descarta casos ambíguos, ficando só amostras de alta concordância (espaço vazio exige mais de 90% de acordo; intenção exige que a explicação externa do cartaz bata com a do anotador).

## 4. Resultados de compreensão

**OCR (Tabela 1):** logotipo e cartaz perto de 0,9 em todos menos o Grok-4-fast (0,440 em logotipo). OCR difícil derruba todos (GPT-5 0,496; Claude 0,579; Gemini 0,472; Qwen3-VL-8B 0,781, o mais robusto, Δ 0,156). Estabilidade por tamanho: Claude (desvio 0,035), Gemini (0,037) e MiniCPM (0,023) os mais estáveis; GPT-5 0,113.

**Fonte (Tabela 2; Score normalizado):**
- Casar fonte: Claude-Sonnet-4.5 0,699, GPT-5 0,668, Gemini 0,362; os demais perto do acaso (−0,012 a 0,083).
- Atributos de fonte (concordância com o julgamento humano): Gemini 0,720, GPT-5 0,664, Claude 0,633; abertos de 0,603 a 0,653.
- Efeito tradicional: GPT-5 0,805, Gemini 0,790, Claude 0,773.
- Efeito avançado: cor de 0,701 a 0,804; efeito de 0,181 a 0,358 (Gemini melhor; Claude 0,204).

**Design avançado (Tabela 3):** estilo acima de 0,8 em GPT-5 (0,851), Gemini (0,830), Claude (0,813) e Qwen3-VL-4B (0,805); composição, Gemini 0,802, GPT-5 0,730, Claude 0,608; intenção, GPT-5 0,824, Gemini 0,788, Claude 0,761. Os fechados mostram mais "letramento em design" que os abertos nas tarefas de composição e intenção.

**Layout (Tabela 4):**
- Localizar texto (IoU médio): Qwen3-VL-8B 0,450, Gemini 0,295, GPT-5 0,171, Claude 0,060.
- Alinhamento (Score): Claude 0,468, GPT-5 0,347, Gemini 0,325; abertos perto de zero ou abaixo. Rotação: Gemini 0,576, Qwen3-VL-8B 0,495, Claude 0,488, GPT-5 0,480.
- Espaço vazio: Gemini IoU 0,491 e acerto do número pedido 0,982; Claude 0,300 e 0,976; GPT-5 0,384 e 0,820.
- **Comparação de layout em pares:** GPT-5 0,719, Gemini 0,680, Claude 0,648, Qwen3-VL-4B 0,633; Grok 0,172, Gemma 0,086. Em acerto, cerca de 86%, 84% e 82% para os três primeiros. O artigo não diz se a posição A ou B do layout bom foi alternada.
- Gerar layout: Gemini melhor (desvio de centro 0,084, razão de área 0,569); GPT-5 0,084 e 0,484; Claude 0,145 e 0,423.

**Nota geral (Tabela 5, cosseno com a nota humana):** GPT-5 0,347, Claude-Sonnet-4.5 0,384, Gemini-2.5-Pro 0,399, Grok-4-fast 0,465, MiniCPM-V-4.5 0,095, Gemma-3n-e4b-it 0,483, Qwen3-VL-4B 0,172, Qwen3-VL-8B 0,237. Os maiores valores são de dois modelos fracos no resto do benchmark. Os autores concluem que a nota única dos modelos tem baixa correlação com humanos e que os comerciais são "insensitive automatic raters", cujas notas não separam bem cartazes fortes de fracos; por isso defendem avaliar dimensões separadas em vez de uma nota global.

**Média geral (Tabela 7; OCR, fonte, layout, compreensão, nota):** Gemini-2.5-Pro 0,647, GPT-5 0,622, Claude-Sonnet-4.5 0,601, Qwen3-VL-8B 0,543, Qwen3-VL-4B 0,538, Gemma 0,486, Grok 0,471, MiniCPM 0,466.

## 5. Resultados de geração (Tabela 6 e Figura 3)

- Média: Gemini-2.5-Flash-Image 0,626, Seedream-4.0 0,609, GPT-Image-1 0,593, Qwen-Image 0,552. Densa: 0,622, 0,618, 0,508, 0,464. Riqueza de fonte (o gargalo): 0,391, 0,342, 0,299, 0,286. Estilo: GPT-Image-1 0,633. Composição: 0,801 a 0,866 (Gemini). Intenção: GPT-Image-1 0,670, Gemini 0,663.
- Padrões: fonte e densidade são eixos parcialmente independentes; quem domina composição e intenção (o global) não domina estilo e fonte (o local), sugerindo treino que favorece planejamento global sobre precisão local.
- Qualitativo: GPT-Image-1 e Qwen-Image preferem fontes conservadoras e retas; Seedream ousa mais, mas quebra traços sob efeitos; todos convergem para estilos seguros e pouco criativos em relação aos cartazes de referência; técnicas avançadas (desalinhamento intencional, espaço em branco, figura e fundo, recortes) falham em geral, e colagens mostram emendas; o Gemini mostra viés ocidental; na intenção, os modelos pegam associações de superfície e raramente transmitem o conceito.

## 6. Entender melhora gerar (Figura 4)

Laço iterativo: um pedido vago gera um cartaz; um modelo de visão (GPT-5 ou Qwen3-VL) recebe o cartaz e o pedido original, diagnostica problemas e devolve um prompt revisado, sem nenhuma dica humana de design; o gerador (GPT-Image-1 ou Qwen-Image) refaz. Na rodada 0, os geradores produzem imagens bonitas que comunicam mal (caveiras e rostos assustadores num cartaz para crianças sobre jogar demais); depois de uma e duas rodadas, o modelo de visão aponta estilo, clima e tipografia, e o resultado melhora, sobretudo no tom emocional ajustado ao objetivo. É demonstração qualitativa, sem métrica. Os autores propõem o fluxo entender, idear, compor e gerar, porque a síntese de ponta a ponta não basta para cartazes muito restritos.

## 7. Limites (implícitos no texto)

O artigo não tem seção de limitações. Do próprio texto: a nota geral usa 219 cartazes e cosseno sobre notas centradas, sem intervalo de confiança; a validação humana dos juízes é resumida em uma porcentagem e uma frase; as tarefas de geração são pontuadas por GPT-5 e Gemini-2.5-Pro, que também estão entre os avaliados na compreensão; não há relato de controle de posição nas tarefas de escolha.

## 8. Tudo o mais que ensina

- **Dimensões do bom cartaz, segundo os autores:** texto legível mesmo em composição densa (glifo, peso, tamanho, contraste), hierarquia explícita (grade, espaço em branco, alinhamento, camadas, figura e fundo), estilo coerente com público e tema sem ruído que esconda a informação, imagem que traduz a mensagem e dirige a atenção para o essencial primeiro, e retórica visual (metáfora, símbolo) decodificável, equilibrando novidade e risco de não ser entendida.
- **Trabalhos citados:** MMBench, Creation-MMBench e Seed-Bench-2-Plus (compreensão multimodal), OCRBench e OCRBench v2, DPG do ELLA e GenEval (aderência ao prompt na geração), CVTG-2K do TextCrafter e LongTextBench do X-Omni (texto renderizado), VGBench, ChartQA e InfographicVQA, LiveIdeaBench, DesignProbe (Lin et al. 2024) e UI-Vision; na geração de cartaz, PosterLLaVA, COLE, OpenCOLE, VASCAR (layout ciente do conteúdo), FontCLIP, ControlText e FontTS (controle tipográfico), PosterCraft e DreamPoster.
- **Diretrizes de anotação** (suplementar D): a instrução de nota geral pede considerar propriedades da fonte, layout, comunicação textual e conceito criativo; a de composição pede listar só as técnicas necessárias em tópicos; a de intenção exige procurar a explicação original do cartaz e descartar a amostra se ela contradiz a leitura do anotador.
- **Os prompts** (suplementar E) pedem resposta seca ("output A or B directly", "Output only a single number"), sem justificativa.
