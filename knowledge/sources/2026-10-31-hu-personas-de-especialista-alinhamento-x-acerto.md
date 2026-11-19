---
titulo: "Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM"
tipo: paper
autor: "Zizhao Hu, Mohammad Rostami, Jesse Thomason"
url: "https://arxiv.org/abs/2603.18507"
publicado_em: 2026-03-19
capturado_em: 2026-10-31
licenca: "CC BY 4.0 (indicada na página do arXiv: 'Creative Commons Attribution 4.0 International', link creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [persona-prompting, role-prompting, expert-persona, alignment-vs-accuracy, llm-as-judge, verbosity-bias, position-bias, self-distillation, persona-routing, safety-refusal]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 19/03/2026 (cs.AI), a única versão e a lida; 17 páginas, sem comentário de venue no arXiv, portanto preprint sem revisão por pares declarada. Autores da University of Southern California (Los Angeles). Sem link de código ou dados no artigo. O integral foi extraído do PDF com `pdftotext`; a Tabela 1 (embaralhada na extração), a Figura 1, a Figura 2 e a Tabela 15 foram lidas nas páginas renderizadas. Os autores declaram que as descrições de persona usadas nos experimentos foram geradas pelo Claude Opus 4.6 e o modelo few-shot das meta-instruções pelo GPT-4o-mini. Lida para a pesquisa de avaliadores do experimento noturno de 2026-11-01.

**Como chegou:** pela matéria do The Register "Telling an AI model that it's an expert programmer makes it a worse programmer" (Thomas Claburn, 24/03/2026, https://www.theregister.com/2026/03/24/ai_models_persona_prompting/). A matéria resume bem a divisão do artigo (persona ajuda em alinhamento, atrapalha em tarefas que dependem do pré-treino) e repete os números do MMLU (68,0% contra 71,6%) e do JailbreakBench (53,2% para 70,9%, que ela chama corretamente de pontos percentuais, enquanto o artigo escreve "+17.7%"). **O que acrescenta:** falas de Zizhao Hu por e-mail, que não estão no artigo: pedir à IA que seja "programador especialista" não melhora qualidade nem utilidade do código; preferências de interface, arquitetura do projeto e ferramenta pesam mais para o lado do alinhamento e se beneficiam de uma persona detalhada; o "você é um desenvolvedor full-stack especialista" genérico é dispensável, mas o requisito granular do projeto pode ajudar; e a regra prática dele: quando importa alinhamento (segurança, regras, seguir estrutura), ser específico no requisito; quando importa acerto e fato, "do not add anything, just send the query". **O que distorce:** o título generaliza para "torna pior", quando o artigo diz que o efeito depende da tarefa; o "pior programador" vem de uma célula (Coding no MT-Bench, −0,65 com persona longa num modelo de 7B) e não de um teste de programação; a matéria diz que "nenhum fato é acrescentado aos dados de treino", frase sem sentido para um prompt (o artigo diz que a persona não acrescenta conhecimento); e não menciona que tudo foi medido em modelos de 7 a 8B, nem que as notas de alinhamento vêm de juízes LLM. Ela registra, sem destacar, um ponto que interessa: a persona ajuda a gerar respostas "that satisfy the LLM-based judge".

## O resumo

Persona no prompt muda tom e padrão de saída, o que serve a sistemas multiagente e a tarefas centradas em gente; a literatura dá resultados mistos (ganho em alguns domínios e na diversidade de dados sintéticos, efeito nulo ou negativo em utilidade geral). Os autores estudam como otimização do modelo, tipo de tarefa, tamanho e posição do prompt mudam o efeito de personas de especialista em modelos ajustados por instrução e de raciocínio, e propõem o PRISM (Persona Routing via Intent-based Self-Modeling), que destila a persona condicionada à intenção num adaptador LoRA com porta (gate), por autoinicialização (bootstrapping), sem dados, modelos ou conhecimento externos. O PRISM melhora preferência humana e alinhamento de segurança em tarefas generativas e mantém o acerto em tarefas discriminativas, com pouco custo de memória e computação.

## 1. A tese central

- **Persona de especialista atrapalha o que vem do pré-treino e ajuda o que vem do ajuste por instrução.** Em tarefas que dependem de recuperar conhecimento do pré-treino (MMLU, matemática, código), a persona piora o resultado de forma consistente; em tarefas que dependem de alinhamento (seguir formato, tom, intenção, segurança, preferência), ajuda. Os autores dizem que essa distinção explica os achados contraditórios da literatura.
- Regra dos autores: para tarefas que dependem de recuperação de conhecimento pré-treinado, "persona prompts should be avoided entirely".
- Explicação proposta, sem teste causal: o prefixo de persona ativa o "modo de seguir instruções" do modelo, que de outro modo estaria dedicado à recordação factual.
- A capacidade de se dirigir por persona é aprendida no ajuste por instrução (RLHF ou SFT), junto com adaptação de estilo, controle de tom, aderência a formato e recusa; por isso a persona amplifica justamente esses comportamentos.

## 2. Método da investigação (seção 3 e apêndices A a D)

- **Modelos (Tabela 2):** seis. Ajustados por instrução: Qwen2.5-7B-Instruct (prompt de sistema padrão "You are Qwen... a helpful assistant"), Llama-3.1-8B-Instruct (prompt de sistema padrão voltado à segurança), Mistral-7B-Instruct-v0.3 (sem prompt de sistema padrão no template). Mistura de especialistas: Mixtral-8x7B-Instruct-v0.1 (só na investigação; a Figura 1d mostra um "Qwen1.5-MoE" no lugar). Destilados de raciocínio: R1-Distill-Qwen-7B e R1-Distill-Llama-8B (alinhamento de segurança apagado na destilação, conjunto pesado em raciocínio, código e STEM).
- **Personas:** 12, geradas pelo método ExpertPrompting (Xu et al. 2023): oito de especialista ligadas às categorias do MT-Bench (escrita, roleplay, raciocínio, matemática, código, extração, STEM, humanidades) e quatro de comportamento (crítico, monitor de segurança, prestativo, complacente). Três granularidades: completa (~150 tokens), curta (~75) e mínima (~5 tokens, um rótulo como "You are a mathematician."). Os textos completos estão nas Tabelas 3 a 14. A persona "prestativa" faz as vezes de especialista para Ciências Sociais e "Outros" do MMLU.
- **Três eixos de avaliação:** qualidade generativa no MT-Bench (80 perguntas, 8 categorias, duas rodadas; nota de 1 a 10 dada pelo Qwen3-32B-Instruct como juiz, média das duas rodadas; a persona vai no prompt de sistema da geração, e o juiz usa o prompt de sistema padrão); acerto discriminativo no MMLU (14.042 questões, 5-shot, pontuação por log-verossimilhança das letras A a D, com a persona como mensagem de sistema antes dos exemplos; sem intervalo de confiança, erro padrão < 0,5%); segurança em HarmBench (400 prompts), JailbreakBench (79) e PKU-SafeRLHF (400 no texto, 500 na Tabela 15), medida como taxa de recusa julgada por LLM ("Does the Assistant Response refuse...? Yes/No"), com o juiz sendo o próprio modelo avaliado salvo indicação, decodificação gulosa e até 256 tokens; intervalos por 1.000 bootstraps.
- **Posição:** a persona no prompt de sistema contra no prompt do usuário (Figura 1d).

## 3. Resultados da investigação

**3.1 Persona prejudica tarefas do pré-treino:**
- **MMLU (Figura 1b; o modelo não é nomeado na legenda, a linha de base de 71,6% casa com o Qwen2.5-7B):** todas as variantes de persona de especialista ficam abaixo da linha de base nas quatro áreas; no geral, 68,0% com a persona mínima e 66,3% com a longa, contra 71,6%. Nas palavras dos autores, "shorter personas can mitigate this effect, but do not eliminate it".
- **Generativo (Figura 1a):** no MT-Bench, as categorias que dependem de conhecimento memorizado ou cadeia lógica estrita pioram com a persona: Humanidades −0,20, Matemática −0,10, Código −0,65. Exemplo: no Mistral-7B, a questão de dados ("soma pelo menos 3") é acertada sem persona (nota 9/10, P = 35/36) e errada com a persona de matemático (1,5/10, conta 9 resultados abaixo de 3).
- **Persona mais longa prejudica mais** no conhecimento (mínima 68,0% contra longa 66,3% no MMLU); hipótese: prompt curto provoca menos comportamento de seguir instrução.

**3.2 Persona ajuda tarefas de alinhamento:**
- **MT-Bench:** a persona longa melhora 5 de 8 categorias: Escrita, Roleplay, Raciocínio (+0,40), Extração (+0,65) e STEM (+0,60). Os autores dizem que a persona STEM não acrescenta conhecimento, só leva a um formato estruturado "that better matches LLM-judge's expectations". Exemplo na escrita (Qwen, questão 82): o e-mail pedindo retorno ao chefe passa de 7/10 para 9/10 com assunto, saudação e lista numerada.
- **Segurança (Figura 1c):** a persona "Monitor de Segurança" sobe a taxa de recusa nos três benchmarks; maior ganho no JailbreakBench, de 53,2% para 70,9% (+17,7 pontos), contra +8,9 com a versão mínima. Exemplo: com o jailbreak "ChadGPT", o modelo sem persona entra no papel e com a persona recusa.
- **Persona mais longa ajuda mais** no alinhamento: mais descrição dá mais informação de alinhamento.

**3.3 Sensibilidade à otimização do modelo:**
- Modelos mais otimizados para prompt de sistema (ordem: Mistral sem prompt padrão, Qwen, Llama) perdem mais no MMLU com persona e ganham mais em segurança: a sensibilidade à persona cresce com o grau de otimização para seguir instruções. No MT-Bench geral não há direção clara, porque ganhos e perdas por categoria se cancelam.
- **Posição:** quanto mais o modelo é otimizado para prompt de sistema (Llama), maior o benefício e menor o dano da persona posta no sistema; em modelo fraco (Qwen) ou não otimizado para sistema (Mixtral), a posição quase não importa.
- **Modelos destilados de raciocínio (Figura 2d):** qualquer persona, de qualquer domínio, melhora Raciocínio, Código e STEM, as categorias que dominam o conjunto de destilação do R1; o modelo aprendeu que qualquer contexto longo e estruturado ativa as rotas de raciocínio, e a identidade da persona fica quase irrelevante. Escrita, Roleplay e Humanidades pioram. A taxa de recusa fica em 0% com qualquer persona, porque a destilação apagou o ajuste de segurança. Princípio dos autores: a persona "can only amplify behaviors that survived the training".

**3.4 Persona de especialista contra persona aleatória (Figura 2, Qwen2.5-7B nos painéis a a c; média dos dois R1 nos d a f):**
- **Especialista sobre a base, efeito no MT-Bench inteiro:** no Qwen, todas as oito personas ficam abaixo de zero (Escrita −0,23, Roleplay −0,08, Raciocínio −0,16, Matemática −0,18, Código −0,18, Extração −0,06, STEM −0,04, Humanidades −0,18). Nos R1, todas acima (+0,06 a +0,38).
- **Especialista sobre a média das aleatórias, no próprio domínio:** no Qwen, em geral o especialista ganha (STEM +1,12, Extração +0,44, Roleplay +0,31, Código +0,31, Raciocínio +0,21), mas perde em Humanidades (−0,97), Escrita (−0,24) e Matemática (−0,21). Nos R1, as barras ficam perto de zero ou negativas (STEM −0,42, Escrita −0,35): o ganho vem do comprimento do contexto, não da especialidade.
- **Diagonal da Figura 2a (persona no seu próprio domínio, Qwen):** Escrita +0,1, Roleplay +0,1, Raciocínio +0,4, Matemática −0,2, Código −0,7, Extração +0,2, STEM +0,6, Humanidades −0,9. Nesse mapa, as linhas são as personas e as colunas as categorias (é o que a leitura dos autores das "faixas verticais" do painel d implica): a coluna de Código fica negativa com todas as personas (de −0,5 a −1,2), a de STEM com todas menos a própria, e a de Escrita fica positiva ou nula com todas (de 0,0 a +0,6).

## 4. O PRISM (seção 4)

Prova de conceito para absorver o lado bom da persona sem o ruim, contra duas alternativas: roteamento por prompt na inferência (Abordagem 1, caro e sem garantia de melhora) e SFT com dados de especialista (Abordagem 2, prejudica a base e pede dados externos). Usa só o modelo base, nomes de domínio e o modelo de persona. Cinco etapas:
1. **Geração de perguntas:** para cada uma das K = 12 personas (granularidade completa), o próprio modelo gera perguntas que se beneficiariam daquela especialidade.
2. **Resposta com e sem persona:** duas respostas do modelo base para cada pergunta.
3. **Autoverificação:** o modelo base, como autojuiz, compara as duas respostas lado a lado, **duas vezes com a ordem trocada**, "to eliminate position bias and verbosity bias"; a persona só vence se for escolhida nas duas ordens (critério conservador, rótulos de alta precisão). Empates ou resultados mistos vão para o conjunto de retenção, para a porta errar a favor do modelo base.
4. **Treino da porta:** um classificador binário leve (MLP de 3 camadas, h → 128 → 64 → 1, GELU) sobre o estado oculto do último token depois da camada 0, com entropia cruzada binária; o desbalanço de classes é corrigido gerando mais perguntas até equilibrar.
5. **Autodestilação por LoRA:** um único adaptador LoRA (rank 16, alfa 32, nas sete projeções de atenção e MLP, ~21M parâmetros) aprende por divergência KL a reproduzir, sem o prompt de persona, a distribuição do modelo com a persona vencedora; a LoRA não mexe na camada 0, para a porta ver sempre a mesma representação. Na inferência, a LoRA liga quando a porta dá ≥ 0,5.

Detalhes de treino (apêndice F, Qwen2.5-7B): 600 amostras (282 para destilar, 318 para reter), perda de retenção com peso 0,5, ~45 minutos numa A100, acurácia final da porta de 68,8%.

## 5. Resultados do PRISM (Tabela 1, conferida na página renderizada)

Cinco modelos (o MoE ficou de fora por ajuste instável). Seis estratégias: Base (prompt de sistema padrão), No-Sys (prompt de sistema vazio), Random (média das 12 personas), Expert (especialista casado com a categoria, Abordagem 1), SFT (LoRA sem porta) e PRISM. "Overall" é a média macro das 15 subcategorias (8 do MT-Bench ×10, 4 do MMLU, 3 de segurança) numa escala de 0 a 100.

- **Qwen2.5-7B:** MT-Bench médio 7,56 (base) contra 7,53 (expert) e 7,76 (PRISM); MMLU 71,7 contra 69,0 e 71,7; segurança média 60,3 contra 67,3 (expert, a maior) e 63,7; Overall 71,8 contra 72,2 e 73,5. A persona casada dá ganho de segurança e perde conhecimento; no total fica empatada com a base.
- **Mistral-7B:** MT-Bench 8,74 (base) contra 7,16 (expert), 7,36 (random) e 8,99 (PRISM); MMLU 59,8 (base e PRISM) contra 58,4 (expert); segurança 85,5 contra 87,4 (expert) e 87,0; Overall 79,9 contra 71,4 (expert) e 81,5 (PRISM). Aqui a persona casada derruba a utilidade.
- **Llama-3.1-8B:** MT-Bench 7,23 contra 7,46 (expert) e 7,76 (PRISM); MMLU 68,4 contra 46,3 (expert; a célula de Ciências Sociais cai para 21,8) e 68,4; segurança 52,9 contra 62,0 (expert, JailbreakBench 29,1 contra 19,0) e 52,9; Overall 67,5 contra 64,6 e 70,3.
- **Destilados de raciocínio:** recusa perto de 0% em todas as estratégias; PRISM fica em 50,0 (R1-Llama, base 49,1) e 50,6 (R1-Qwen, base 50,5) no Overall. A porta manda 97,6% (R1-Llama) e 99,4% (R1-Qwen) das perguntas para o modelo base, porque o conjunto selecionado puxa para matemática e código, onde o ganho é limitado pelo conhecimento pré-treinado.
- **Achado 3 (Figura 4, Qwen):** a fração roteada para a LoRA por subcategoria correlaciona com o efeito da persona naquela subcategoria (Pearson r = 0,65; Spearman ρ = 0,75): MMLU ~6% roteado, segurança 73% a 78%, MT-Bench de 10% a 100%, sem supervisão do tipo de tarefa.

## 6. O autojuiz e o viés de verbosidade (apêndice E)

- A primeira versão da etapa 3 usava **nota pontual** (cada resposta de 1 a 10, vence a maior). O autojuiz preferia sistematicamente as respostas mais longas e elaboradas, "even when they are factually incorrect".
- Evidência: no Mistral-7B, a persona de matemática teve 68% de taxa de destilação (o juiz achou a resposta com persona melhor em 68 de 100 comparações), enquanto no MT-Bench julgado pelo Qwen3-32B a mesma persona derruba a nota de matemática de 9,05 para 6,10 (−2,95). Para os autores, o autojuiz premiava a formatação passo a passo e verbosa da persona, não a correção matemática; como a persona produz respostas mais longas em todas as categorias, a taxa de destilação inflava em todas, e a porta herdava o viés.
- Solução: **comparação pareada com troca de posição** (A = base, B = especialista; depois o inverso; vence só quem ganha nas duas). Três benefícios declarados: as duas respostas no mesmo contexto permitem comparação direta em vez de nota absoluta; a troca cancela a preferência sistemática pela primeira ou pela segunda; exigir concordância nas duas ordens filtra decisões movidas por traços superficiais (comprimento, formatação).

## 7. Limitações declaradas e ética

- Só modelos de 7 a 8B; os autores acham que os achados de sensibilidade e dependência de tarefa devem generalizar, mas a magnitude do PRISM em 70B+ não foi testada.
- A porta é acoplada ao adaptador, o que impede técnicas padrão de fusão de LoRA (média de pesos, aritmética de tarefas).
- MoE é difícil de ajustar por LoRA; modelos já muito especializados deixam menos espaço para ganho por roteamento de persona.
- Ética: as personas podem, em tese, ser usadas para contornar filtros de segurança (risco inerente ao prompt de sistema), e o PRISM reforça a segurança em vez de enfraquecê-la.

## 8. Inconsistências do próprio texto

- O resumo e a introdução falam em seis LLMs; os experimentos do PRISM usam cinco.
- PKU-SafeRLHF tem 400 prompts no texto e 500 na Tabela 15.
- A legenda da Figura 1 não diz qual modelo está nos painéis a a c, e a linha de base do MMLU ali (71,6%) difere da Tabela 1 (71,7% no Qwen); a persona "Expert" da Tabela 1 dá 69,0% no Qwen, valor que não bate com nenhuma das granularidades citadas no texto (68,0% e 66,3%).
- As seções 3.1c ("Longer persona prompts damage more") e 3.2c ("Longer expert persona prompts help more") tratam de eixos diferentes (conhecimento contra alinhamento), não se contradizem.
- O artigo escreve "+17.7%" para o que é uma diferença de 17,7 pontos percentuais.
- A segurança é julgada pelo próprio modelo avaliado, e o MT-Bench por outro LLM (Qwen3-32B); não há avaliação humana.

## Tudo o mais que ensina

- **Trabalhos relacionados citados, com o achado de cada um:** a favor da persona: raciocínio zero-shot por role-play (Kong et al. 2024, arXiv 2308.07702) e ExpertPrompting (Xu et al. 2023, arXiv 2305.14688); divergência de comportamento em sistemas multiagente (Chen et al. 2026, "Multi-persona thinking for bias mitigation", arXiv 2601.15488); conversas de apoio emocional (Wu et al. 2025); dados sintéticos com um bilhão de personas (Chan et al. 2024, arXiv 2406.20094); justiça na detecção de discurso de ódio (Gajewska et al. 2025); tarefas de visão e linguagem por "in-context impersonation" (Salewski et al. 2023, NeurIPS). Contra ou misto: nenhum benefício confiável em 162 papéis (Zheng et al. 2024, Findings EMNLP); persona como "faca de dois gumes" no raciocínio zero-shot (Kim et al. 2025, IJCNLP-AACL); quedas de acerto pelo estilo do prompt (Truong et al. 2025, arXiv 2507.22168); falha em simular personas contrafactuais de desempenho invertido (Kumar et al. 2025, arXiv 2504.06460); efeitos imprevisíveis na teoria da mente (Tan et al. 2025, PHAnToM); vieses implícitos de raciocínio em LLMs com persona (Gupta et al. 2024, arXiv 2311.04892).
- **Roteamento por intenção:** usar um modelo roteador para detectar a intenção da pergunta e mandá-la para a persona mais adequada na inferência (FrugalGPT, Chen et al. 2023; RouteLLM, Ong et al. 2024). Pressupõe que toda persona de especialista ajuda, premissa que, para os autores, a evidência não sustenta.
- **Destilação de contexto (Askell et al. 2021; Snell et al. 2022):** internaliza no peso o comportamento de um contexto, como um prompt de sistema, sem custo na inferência, mas com deriva permanente de comportamento. Compressão de prompt (Chevalier et al. 2023; LLMLingua-2, Pan et al. 2024) reduz custo mas precisa de componentes extras para ser seletiva.
- **Autoaperfeiçoamento sem supervisão externa:** Self-Instruct (Wang et al. 2023), Self-Refine (Madaan et al. 2023), recompensa autogerada (Yuan et al. 2024), filtragem de soluções sintéticas (Singh et al. 2024), autocrítica constitucional (Bai et al. 2022).
- **Protocolo MT-Bench (Zheng et al. 2023):** recomenda um modelo forte como juiz para comparação consistente entre modelos; o GPT-4 teve mais de 80% de concordância com juízes humanos. O MT-Bench e o Chatbot Arena recomendam comparação pareada em vez de nota pontual.
- **Prompt de sistema vazio contra padrão:** os autores separam "Base" (mantém o prompt padrão embutido, como o do Qwen) de "No-Sys" (sobrescreve com mensagem vazia) para isolar o efeito do próprio prompt padrão. No Qwen, No-Sys fica em 71,5 contra 71,8 de Overall; no Llama, 66,0 contra 67,5.
- **Jailbreak e prompt de sistema:** os autores atribuem a força da persona de segurança ao fato de o ajuste de prompt de sistema priorizar as instruções do prefixo, o que por si já protege contra jailbreak.
- **Exemplos completos de persona (Tabelas 3 a 14):** a persona "Crítico" (Tabela 11) é descrita como analista crítico com experiência em revisão por pares, que separa raciocínio forte de plausibilidade superficial e dá crítica específica e acionável "rather than subjective preference"; as de matemática, código e raciocínio pedem explicitamente correção acima de tudo e mesmo assim, no caso da matemática, derrubam o acerto.
- **Custo computacional:** etapas 1 a 3 e 5 rodam numa GPU (A100 80 GB ou RTX A6000 48 GB); os logits do professor são pré-computados em disco (um arquivo por amostra) para não manter duas cópias do modelo na memória.

---
