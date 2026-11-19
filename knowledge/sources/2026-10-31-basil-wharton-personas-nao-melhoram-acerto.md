---
titulo: "Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy"
tipo: paper
autor: "Savir Basil, Ina Shapiro, Dan Shapiro, Ethan Mollick, Lilach Mollick, Lennart Meincke"
url: "https://arxiv.org/abs/2512.05858"
publicado_em: 2025-12-05
capturado_em: 2026-10-31
licenca: "CC BY 4.0 (indicada na página do arXiv: 'Creative Commons Attribution 4.0 International', link creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [persona-prompting, role-prompting, expert-persona, factual-accuracy, gpqa, mmlu-pro, low-knowledge-persona, refusal, repeated-sampling, prompt-sensitivity]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 05/12/2025, a única versão e a lida; 40 páginas, das quais umas 7 de texto e o resto figuras e tabelas suplementares; também depositado no SSRN (abstract 5879722, não aberto aqui). É o quarto de uma série de relatórios curtos do Generative AI Labs (GAIL) da Wharton School (University of Pennsylvania), escrita para líderes de negócio, educação e política; sem revisão por pares declarada. Afiliações: todos no GAIL da Wharton; Dan Shapiro também na Glowforge; Lennart Meincke também na WHU–Otto Beisheim School of Management. A OpenAI forneceu créditos de API; os autores dizem que nenhuma outra parte participou do desenho, execução, análise ou interpretação e que não recebem compensação das empresas estudadas. Sem link de código ou dados. O integral foi extraído do PDF com `pdftotext`; as Figuras 1, S4 e S5 foram lidas nas páginas renderizadas (as médias por modelo citadas abaixo são leitura aproximada das barras, porque o relatório não as tabela). Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Como chegou:** pela matéria do Knowledge at Wharton "Why You Shouldn't Ask Chatbots to Act Like an Expert" (Seb Murray, 28/04/2026, https://knowledge.wharton.upenn.edu/article/why-you-shouldnt-ask-chatbots-to-act-like-an-expert/), lida pelo WebFetch porque o `curl` recebeu 403 do servidor. A matéria resume o relatório com fidelidade e **acrescenta** falas de Lennart Meincke (pesquisador do Mack Institute) que não estão no relatório: que a persona era tida como útil quando os LLMs surgiram, "but it matters less today"; que para pergunta factual o papel não importa (um advogado e um leigo devem receber a mesma resposta para "qual a capital do Reino Unido?"); que a persona continua "immensely useful" para tom e apresentação; e cita o projeto da Meta de uma versão IA de Mark Zuckerberg para falar com funcionários como sinal de que a ideia de "IA como especialista" chega às empresas. **O que simplifica ou distorce:** atribui a Meincke que perguntar a mesma questão difícil 25 ou 30 vezes dá a resposta certa "só algumas vezes", frase que o relatório não sustenta como regra (as médias de acerto ficam entre ~40% e ~73% conforme o modelo); converte a média de 10,56 recusas em 25 tentativas por pergunta (Gemini 2.5 Flash, especialista não relacionado, GPQA) em "mais de 10 de 25 tentativas em alguns casos"; e fala em "nearly 200" e "300" perguntas sem dizer que o segundo conjunto é um recorte de três áreas do MMLU-Pro.

## O resumo do relatório

Pergunta: dar uma persona ao modelo melhora o desempenho em perguntas objetivas difíceis de múltipla escolha? Seis modelos, dois benchmarks (GPQA Diamond e MMLU-Pro), três abordagens: especialista do mesmo domínio da pergunta ("você é especialista em física" para física), sem efeito significativo, com exceção do Gemini 2.0 Flash; especialista de outro domínio, diferenças marginais; e personas de pouco conhecimento (leigo, criança, criança de 4 anos), em geral prejudiciais. Conclusão: personas em geral não melhoram o acerto frente à linha de base sem persona; especialista fora do domínio às vezes piora; persona de pouco conhecimento costuma piorar. Os autores frisam que o resultado é só sobre acerto e que personas podem servir a outros fins, como mudar o tom.

## 1. Por que a pergunta importa

- A documentação oficial dos fabricantes recomenda persona: o guia de prompt do Vertex AI (Google) manda "Assign a role" e dá o modelo "You are a [persona, such as a 'math teacher' or 'automotive expert']"; um exemplo da Anthropic começa com "You are an expert AI tax analyst"; material de desenvolvedor da OpenAI usa "You are a world-class Python developer".
- A lógica implícita dos guias: a persona estaria estatisticamente associada a abordagens que levam à resposta certa, então "aja como professor de física" melhoraria o acerto em física.
- Pesquisa independente sobre ganho por persona é rara e inconsistente: Kong et al. 2024 acham ganho em benchmarks; Zheng et al. 2024 não acham ganho confiável com persona no prompt de sistema em perguntas factuais.

## 2. Método

- **GPQA Diamond (Rein et al. 2024):** 198 questões de múltipla escolha (4 opções) de nível de doutorado em biologia, física e química. Doutores da área acertam 65% (74% descontando erros que eles mesmos reconheceram depois); não especialistas muito qualificados acertam 34% mesmo com mais de 30 minutos e web livre.
- **MMLU-Pro (Wang et al. 2024):** 10 opções por questão, o que reduz o acerto por chute. Recorte de 300 questões: 100 de engenharia, 100 de direito e 100 de química, escolhidas pela diversidade de domínio e porque têm notas um pouco mais baixas, deixando espaço para ganho.
- **Modelos:** GPT-4o, GPT-4o-mini, o3-mini, o4-mini, Gemini 2.0 Flash e Gemini 2.5 Flash (com e sem raciocínio); a Figura S5 acrescenta o GPT-3.5 Turbo. Os autores dizem que o interesse é a variação dentro de cada modelo, não a escolha do modelo.
- **Repetição:** 25 respostas independentes por questão para cada par modelo e prompt (seguindo Meincke et al. 2025b, segundo o qual mais de 25 tentativas, como 100, não melhoram de forma relevante a precisão nem o poder estatístico): 4.950 execuções por par no GPQA e 7.500 no MMLU-Pro. Temperatura 1,0, que imita o padrão de produção dos fabricantes. Zero-shot, de propósito: imita o uso real e isola o efeito da persona do efeito dos exemplos.
- **Prompt:** o mesmo prompt de sistema genérico em todas as condições ("You are a very intelligent assistant, who follows instructions directly.", de Rein et al. 2024); a persona, quando há, vai no começo do prompt do usuário, seguida da pergunta, das opções e da instrução de formato ("The correct answer is (insert answer here)").
- **Personas:** linha de base sem persona; especialistas "world-class" com descrição longa de propósito (física, matemática, economia, biologia, química no GPQA; engenharia, direito, química, física, história no MMLU-Pro), por exemplo "You are a world-class expert in physics, with deep knowledge across all areas of the field including theoretical, experimental, and applied physics. Answer the question given your expert-level understanding of physics."; e três de pouco conhecimento: leigo ("no special training in this subject"), criança ("thinks they understand the world but sometimes mixes things up") e criança de 4 anos ("thinks the moon is made of cheese").
- **Análise por domínio (Tabela S4):** para cada questão, especialista do mesmo domínio, de domínio adjacente e de domínio não relacionado. GPQA: física com matemática (adjacente) e economia (não relacionado); química com física e economia; biologia com química e economia. MMLU-Pro: engenharia com física e direito; química com física e direito; direito com história e engenharia.
- **Métrica principal:** "Average Rating", a fração de acertos média nas 25 execuções. Métricas suplementares com limiar por questão: 100% (25 de 25), 90% (23 de 25) e 51% (13 de 25). Os autores não consideram PASS@N (passa se uma de N acerta) nem CONSENSUS (passa se a resposta modal acerta) úteis para aplicações reais.
- **Estatística:** testes de permutação por bootstrap pareado (5.000 réplicas); as tabelas dão a diferença de risco (RD) com IC de 95% e p sem correção para comparações múltiplas.

## 3. Resultados

**Geral (Figura 1, Tabelas S2 e S3):**
- Na maioria dos pares modelo e benchmark, nenhuma persona difere estatisticamente da linha de base; quando difere, é mais vezes para pior.
- **GPQA:** nenhuma persona, de especialista ou de pouco conhecimento, melhora de forma confiável em nenhum modelo. O único efeito positivo significativo é a "criança" no Gemini 2.5 Flash (RD = +0,098 [0,029; 0,164], p = 0,005), que os autores tratam como peculiaridade do modelo. No o4-mini, as três personas de pouco conhecimento pioram (criança de 4 anos −0,061, criança −0,037, leigo −0,022); no GPT-4o, a criança de 4 anos piora (−0,052 [−0,087; −0,016], p = 0,004).
- **MMLU-Pro:** em cinco dos seis modelos, nenhuma persona de especialista melhora com significância, e há nove diferenças negativas significativas. A exceção é o Gemini 2.0 Flash: os cinco especialistas dão ganhos modestos (por exemplo, engenharia +0,089 [0,033; 0,148], p = 0,002), enquanto criança de 4 anos e leigo pioram.
- **Ordem da ignorância:** em quatro de seis modelos a criança de 4 anos piora o desempenho; no MMLU-Pro, ela é significativamente pior que o leigo em cinco de seis modelos (a exceção é o GPT-4o-mini, sem diferença significativa entre nenhum par), e pior que a criança em quatro de seis (exceto GPT-4o-mini e GPT-4o). Quanto menos conhecimento a persona implica, pior o resultado.
- **Patamares por modelo (leitura aproximada da Figura 1, linha de base):** GPQA, o4-mini ~0,73, o3-mini ~0,64, Gemini 2.0 Flash ~0,57, Gemini 2.5 Flash ~0,46, GPT-4o ~0,46, GPT-4o-mini ~0,40; MMLU-Pro, o3-mini e o4-mini ~0,66, Gemini 2.5 Flash ~0,61, GPT-4o ~0,60, Gemini 2.0 Flash ~0,55, GPT-4o-mini ~0,47. O maior tombo visível é do Gemini 2.5 Flash com o especialista em economia no GPQA (~0,30) e com especialistas de outro domínio no MMLU-Pro.
- **Limiares de acerto (Figuras S1 a S3):** resultados comparáveis, com efeitos mais marcados nos limiares mais altos.
- **Dificuldade (Figura S4):** o GPQA separado em quatro níveis de dificuldade (graduação fácil, 1.000 execuções; graduação difícil, 2.525; pós-graduação difícil, 1.075; pós-graduação, 250) não muda o quadro; os intervalos alargam nos níveis com menos questões.

**Por domínio (Figura 2, Tabelas S5 e S6):**
- Persona ajustada ao domínio não melhora em geral. No GPQA, nenhuma diferença positiva significativa entre a linha de base e as três variações (mesmo domínio, adjacente, não relacionado).
- No MMLU-Pro, duas exceções: o Gemini 2.0 Flash melhora em engenharia e química com as três variações, e o GPT-4o melhora em direito com o especialista do mesmo domínio. Os autores acham que os ganhos do Gemini 2.0 Flash podem ser pontos fora da curva, porque o Gemini 2.5 Flash, da mesma família, não teve nenhuma diferença positiva significativa.

**Modo de falha: recusa por papel estreito:**
- Com especialista de outro domínio, o Gemini 2.5 Flash muitas vezes se recusa a responder. Na condição de especialista não relacionado no GPQA, recusa em média 10,56 das 25 tentativas por questão, dizendo que não tem a especialidade ou que não pode, "in good conscience", escolher uma resposta. O Gemini 2.0 Flash faz o mesmo, menos, em algumas condições de física e química. Na Tabela S5, na física do GPQA, o Gemini 2.5 Flash cai 0,247 com o especialista não relacionado (p < 0,001).
- Regra dos autores: "role instructions that are too narrow can cause models to under-utilize their actual knowledge".

## 4. Conclusões e recomendações dos autores

- Para perguntas factuais difíceis do tipo GPQA Diamond e MMLU-Pro, dar persona de especialista "is not a reliable way to improve accuracy"; quando a persona importa, é mais provável que piore do que melhore.
- Ajustar a persona ao domínio da pergunta não traz benefício consistente; os poucos ganhos parecem específicos do modelo e da pergunta.
- Personas podem servir a outros fins, fora do acerto: mudar em que fatores o modelo foca e como ele raciocina (preocupações regulatórias para um responsável por conformidade, oportunidades de mercado para um desenvolvedor de negócios), como expressa o resultado (especialista confiante contra conselheiro cauteloso) e o tom e a apresentação. Também podem ajudar o usuário: nomear um papel ajuda a formular e enquadrar a pergunta.
- Testar várias variações de prompt num problema específico ainda pode valer, dada a variabilidade por pergunta vista em trabalhos anteriores, mas sem esperar ganho consistente.
- Recomendação final: organizações tendem a ganhar mais iterando nas instruções da tarefa, nos exemplos ou nos fluxos de avaliação do que acrescentando personas de especialista.

## 5. Limitações declaradas

- Só um subconjunto de modelos; benchmarks acadêmicos que podem não refletir todos os usos reais; um conjunto específico de personas num número limitado de domínios.
- Os autores dizem que os nulos consistentes entre modelos e benchmarks sugerem que atribuir persona pode ser ineficaz, mas que práticos devem esperar resultados imprevisíveis.

## Tudo o mais que ensina

- **A série Prompting Science Reports:** relatório 1, "Prompt Engineering is Complicated and Contingent" (Meincke et al. 2025a, SSRN 5165270); relatório 2, "The Decreasing Value of Chain of Thought in Prompting" (2025b, SSRN 5285532), que também fixou o protocolo do GPQA e o número de 25 tentativas; relatório 3, "I'll pay you or I'll kill you — but will you care?" (2025c, SSRN 5375404), sobre gorjeta e ameaça no prompt.
- **Barras de erro em avaliações:** Miller 2024, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations" (arXiv 2411.00640), citado para justificar a repetição por questão.
- **Autoconsistência:** Wang et al. 2023 (arXiv 2203.11171), citado para justificar muitas amostras por questão na busca de uma tendência central confiável.
- **Por que médias por questão e não PASS@N:** a métrica de acerto médio sobre 25 amostras mede o que o usuário recebe numa chamada qualquer; os limiares de 100%, 90% e 51% respondem a perguntas diferentes (tarefa sem margem de erro, erro aceitável parecido com o humano, maioria simples).
- **Persona como ajuda ao usuário:** além do efeito no modelo, nomear um papel pode ajudar quem escreve o prompt a pensar a pergunta, efeito que o estudo não mede.
- **Personas de pouco conhecimento como contraste:** nas palavras dos autores, o grau de falta de conhecimento implicado pela persona afetou o quanto o modelo piorou (criança de 4 anos pior que criança, pior que leigo); o modelo responde ao conteúdo da persona para baixo, mesmo quando a persona de especialista não o move para cima.
- **System card do GPT-5.1 (OpenAI 2025a):** citado como exemplo de que personas certamente moldam tom e apresentação.

---
