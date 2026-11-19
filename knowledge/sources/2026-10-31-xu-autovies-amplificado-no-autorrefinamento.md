---
titulo: "Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement"
tipo: paper
autor: "Wenda Xu, Guanglei Zhu, Xuandong Zhao, Liangming Pan, Lei Li, William Yang Wang"
url: "https://arxiv.org/abs/2402.11436"
publicado_em: 2024-02-18
capturado_em: 2026-10-31
licenca: "CC BY 4.0 (indicada na página do arXiv: http://creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [self-bias, self-preference, iterative-self-refinement, self-rewarding, llm-as-judge, score-inflation, external-feedback, best-of-n, model-scale, machine-translation]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 18/02/2024 e v2 em 18/06/2024, a lida. Publicado nos anais da ACL 2024 (Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, Bangkok, p. 15474–15492, DOI 10.18653/v1/2024.acl-long.826, conferido na ACL Anthology). Autores da University of California, Santa Barbara (Xu, Zhao, Pan, Wang) e da Carnegie Mellon (Zhu, Li); apoio da NSF e de uma doação da Apple. Código e dados em https://github.com/xu1998hz/llm_self_bias. O texto foi extraído do PDF da v2 com `pdftotext`; os rótulos de vários gráficos saíram com a fonte embaralhada, e os gráficos foram lidos nas páginas renderizadas. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01, por medir o mesmo modelo como gerador e avaliador ao longo de iterações de refinamento; é o "Xu et al. (2024)" que os dois artigos de Pan citam como concorrente.

**Atenção:** a "verdade" contra a qual o viés é medido é, na tradução, uma métrica automática (BLEURT, mapeada para a escala humana MQM), conferida por um anotador humano em 50 exemplos; na geração com conceitos e na matemática, é uma regra exata (cobertura por casamento de cadeias, resposta igual à referência).

## O resumo

Estudos recentes mostram LLMs melhorando com o próprio retorno em umas tarefas e piorando em outras; os autores atribuem a contradição a um viés do modelo ao avaliar a própria saída. Definem o **autoviés** (self-bias), a tendência de favorecer a própria geração, por duas estatísticas, e medem seis LLMs (GPT-4, GPT-3.5, Gemini, LLaMA2, Mixtral e DeepSeek) em tradução, geração com restrição e raciocínio matemático. O autoviés aparece em todos, em várias línguas e tarefas. O autorrefinamento melhora fluência e inteligibilidade, mas **amplifica** o autoviés. Modelo maior e retorno externo com avaliação precisa reduzem o viés e trazem melhora real.

## 1. As duas estatísticas (seção 3)

- **Viés:** a média, sobre as amostras, da diferença entre a nota que o modelo dá à própria saída e a qualidade verdadeira; positivo é superestimar a si mesmo.
- **Assimetria de distância (distance skewness, Székely e Móri 2006):** viés zero não garante simetria (uma cauda longa e fina pode compensar outra curta e grossa); a assimetria de distância vai de 0 (distribuição simétrica em torno de zero) a 1 (tudo de um lado só). As duas se complementam.
- **O laço:** o modelo gera; o mesmo modelo dá retorno; o modelo refina; o refinamento só é aceito se a nota do próprio modelo melhorar. Em cada passo, o modelo vê só a geração ou o retorno da iteração anterior, sem o histórico inteiro.

## 2. Método (seção 4.1)

- **Modelos:** GPT-4, GPT-3.5-Turbo, Gemini (gemini-pro), LLaMA2-7B-chat, Mixtral 8x7B Instruct e DeepSeekMoE 16B chat; na análise de escala, LLaMA2 7B, 13B e 70B.
- **Tradução:** Flores-200, quatro pares de línguas de poucos recursos para o inglês (iorubá, javanês, armênio, igbo), 100 exemplos por par; o modelo dá retorno no formato MQM (local, tipo e gravidade do erro, −1 por erro menor e −5 por erro maior, de 0 a −25). A verdade é o BLEURT-20 levado à escala MQM por mapeamento de quantis (aprendido em 28.125 pares BLEURT-humano do WMT22).
- **Geração com restrição:** 100 exemplos do CommonGen Hard (cerca de 30 conceitos por texto); o retorno aponta conceitos faltantes; a verdade é a cobertura total por casamento exato (1 ou 0).
- **Matemática:** 100 problemas do MATH; a verdade é a resposta final igual à referência.

## 3. Resultados

- **Tradução (Figura 3):** todos os modelos têm autoviés no laço; os abertos e o GPT-3.5 têm mais que GPT-4 e Gemini, mas o viés cresce com as iterações em todos, nos quatro pares de línguas.
- **O motivo (Figura 4):** ao longo de dez iterações, a nota que GPT-4 e Gemini dão a si mesmos sobe de cerca de −8 ou −9 para perto de 0, enquanto o BLEURT fica parado (cerca de −7,5 e −9,5 no iorubá). A qualidade real não melhora; o modelo enxerga melhoras que não existem, e a distância cresce a cada iteração.
- **Avaliação humana (Tabela 1 e apêndice E; um pós-graduando anotou 50 exemplos das iterações 0 e 10 no iorubá-inglês, em MQM):** a qualidade humana não muda (GPT-4 de −15,0 para −15,1; GPT-3.5 de −22,2 para −21,9; Gemini de −17,3 para −18,3), enquanto a nota do próprio modelo sobe (GPT-4 de −6,92 para −0,52; GPT-3.5 de −2,61 para −0,03; Gemini de −8,92 para −0,72). Viés e assimetria, iteração 0 para 10: GPT-4 8,06 para 14,6 e 0,452 para 0,692; GPT-3.5 19,6 para 21,9 e 0,803 para 0,885; Gemini 9,62 para 17,6 e 0,455 para 0,766 (a Tabela 7 do apêndice dá 0,355 para a assimetria inicial do Gemini, e a diferença das médias, 8,38, não bate com o viés de 9,62).
- **Exemplo (GPT-4, iorubá):** a referência é "Agora temos camundongos de 4 meses que não são diabéticos e que eram diabéticos". A primeira tradução troca o sentido ("quatro ratos sem diabetes que desenvolveram diabetes"; humano −11, GPT-4 −11). A segunda refinação mantém o erro com outras palavras ("Presently, we have four non-diabetic rats that have developed diabetes"); o humano dá −11, o GPT-4 dá 0, viés 11.
- **Geração com restrição (Figura 5):** a melhora estimada pelo modelo cresce muito mais rápido que a cobertura real; o GPT-4 começa com cerca de 40% de cobertura e o GPT-3.5 com cerca de 2%; quando o GPT-3.5 chega a cerca de 20% de cobertura (iteração 5), viés e assimetria sobem forte, e a melhora real satura depois da quinta iteração nos dois.
- **Matemática (Figura 6 e apêndice D):** viés e assimetria sobem no laço; o mesmo acontece trocando a autoavaliação por autoconsistência (dez caminhos de raciocínio e voto), o que leva a um ensemble enviesado.
- **Formato do retorno (Tabela 2, 1.200 amostras anotadas):** a acurácia de formato é quase perfeita na 1ª e na 5ª iteração (93% a 100%); o Gemini recusa sete frases de tema sensível. O viés não vem de saída malformada.

## 4. O que melhora, e o gosto pelo próprio estilo (seções 4.3 e 4.4)

- **Fluência e inteligibilidade sobem, qualidade não (Figura 7):** medidas pelo UniEval, as duas sobem de forma consistente com as iterações em GPT-4, GPT-3.5 e Gemini, sem ganho de qualidade. O laço melhora qualidades intrínsecas do texto, não a que o prompt pede.
- **Preferência pelo próprio estilo (Figura 8):** 100 traduções do Madlad400-10b, parafraseadas por GPT-4, GPT-3.5 e Gemini sem pedido de melhora; antes da paráfrase, GPT-4 e Gemini têm viés negativo sobre essas traduções; depois, os três aumentam o viés a favor das paráfrases, porque a qualidade cai e eles a enxergam como melhora.
- **Autorrecompensa com melhor de N (Tabela 3, iorubá):** amostrar k candidatos e escolher pela própria nota (como no self-rewarding de Yuan et al. 2024) aumenta viés e assimetria com k: DeepSeekMoE de 14,8 e 0,735 (k = 1) para 18,5 e 0,840 (k = 32); Mixtral de 12,4 e 0,483 para 18,5 e 0,790; LLaMA2-7B de 8,75 e 0,491 para 20,9 e 0,850. Escolher num conjunto maior amplifica o viés, e treinar nessas escolhas o propaga.

## 5. Mitigações (seção 5)

- **Retorno externo com avaliação precisa (Figura 9 e Tabela 4):** o InstructScore (modelo de métrica que vê a referência e devolve local, tipo e gravidade do erro, sem dar a correção) substitui o próprio retorno. O viés fica abaixo do da autoavaliação em todos os modelos, e os três passam a melhorar de verdade pelo BLEURT. O mesmo exemplo do iorubá, com retorno externo: humano −11, −2, −1 até "We now have 4-month-old mice that are non-diabetic that were diabetic". Os autores chamam esse retorno de oráculo, porque vê a referência.
- **Modelo maior (Figura 10):** no LLaMA2, o viés do 70B se estabiliza depois da quinta iteração, enquanto o 7B e o 13B continuam amplificando; modelos maiores avaliariam a própria saída com mais precisão.

## 6. Limitações e perguntas abertas declaradas

O estudo mede o viés de um modelo sobre a própria saída. Ficam abertas: o viés entre modelos diferentes; se um modelo favorece mais modelos com o mesmo pré-treino, dados ou objetivo; se favorece mais os da mesma família; se modelos destilados (Vicuna do GPT-4, Alpaca do ChatGPT) têm mais viés. A anotação humana total levou seis horas, por um anotador pago acima do mínimo local.

## 7. Tudo o mais que ensina

- **Autocorreção:** Self-Refine (Madaan et al.), Self-Debug (Chen et al.), Reflexion (Shinn et al.), autoconsistência (Wang et al. 2023), autoaperfeiçoamento por ajuste no caminho mais confiável (Huang et al. 2023a), autorrecompensa (Yuan et al. 2024) e ReST (Gulcehre et al. 2023). Contra: LLMs não corrigem o próprio raciocínio e até pioram (Huang et al. 2023b, "Large language models cannot self-correct reasoning yet"); não acham erros de raciocínio mas corrigem se apontados (Tyen et al. 2023); o retorno do próprio modelo é limitado ao que ele já sabe (Stechly et al. 2023, "GPT-4 doesn't know it's wrong"; Hong et al. 2023) e pode afastá-lo da resposta certa (Valmeekam et al. 2023).
- **LLMs como avaliadores:** G-Eval com cadeia de raciocínio (Liu et al. 2023a), GPTScore por verossimilhança (Fu et al. 2023), esquemas de erro detalhados como GEMBA-MQM e InstructScore; vieses cognitivos de avaliadores (Koo et al. 2023), verbosidade e autopromoção (Zheng et al. 2023), preferência por texto memorizado (Chang et al. 2023), e métricas sem referência enviesadas para a própria saída (Deutsch et al. 2022; Liu et al. 2023b, "narcissistic evaluators", o BARTScore favorecendo texto do mesmo modelo em resumo).
- **Mapeamento de quantis (apêndice B):** para pôr uma métrica não calibrada na escala humana, ordenam-se as duas distribuições, calculam-se as funções de distribuição acumulada, aprende-se a interpolação entre percentis e aplica-se à métrica, preservando a ordem.
- **Por que línguas de poucos recursos:** em pares de muitos recursos, como chinês-inglês, o GPT-4 já traduz perto do nível humano e sobra pouco para o refinamento melhorar (Kocmi et al. 2023).

---
