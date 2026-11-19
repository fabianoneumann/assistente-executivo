---
titulo: "DesignProbe: A Graphic Design Benchmark for Multimodal Large Language Models"
tipo: paper
autor: "Jieru Lin, Danqing Huang, Tiejun Zhao, Dechen Zhan, Chin-Yew Lin"
url: "https://arxiv.org/abs/2404.14801"
publicado_em: 2024-04-23
capturado_em: 2026-10-31
licenca: "Licença não exclusiva de distribuição do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/, indicada na página do arXiv). Entra só a ficha."
areas: [agent-engineering, content-design]
tags: [vlm-as-judge, graphic-design, benchmark, llm-grader, position-bias, answer-permutation, few-shot-images, prompt-rewriting, font-perception, gpt-4v]
---

Ficha de estudo, em palavras próprias; sem texto integral. arXiv: v1 em 23/04/2024, a única versão e a lida; comentário "work in progress", sem venue. Autores do Harbin Institute of Technology (Jieru Lin, Tiejun Zhao, Dechen Zhan) e da Microsoft (Danqing Huang, Chin-Yew Lin); o trabalho foi feito no estágio da primeira autora na Microsoft. O artigo não indica código nem dados públicos. Texto extraído do PDF com `pdftotext`; as Tabelas 1 a 3, a Figura 4 e as tabelas do apêndice foram lidas na página renderizada. Lido para a pesquisa de avaliadores do experimento noturno de 2026-11-01. **Força:** preprint em andamento, 50 exemplos por tarefa (200 perguntas com as permutações), modelos de 2023 (o melhor é o GPT-4V), validação do avaliador em 50 casos de uma só tarefa; promete detalhes num material suplementar que está só em parte no apêndice.

## 1. A pergunta

Um bom design gráfico tem harmonia em dois níveis: nos elementos finos (cor, fonte, layout), que seguem princípios próprios e servem ao conjunto, e no design como um todo. Entender design exige, então, reconhecer os elementos e compreender o conjunto. A pergunta: modelos multimodais de 2023 conseguem? O enquadramento segue o levantamento de Huang et al. (2023, "A survey for graphic design intelligence"), que separa nível do elemento e nível do design geral.

## 2. As oito tarefas (Figura 2)

**Nível do elemento, reconhecimento de atributos:**
- **1, tema de cor:** identificar as cores principais de 50 designs do Crello (cores mais frequentes calculadas e revistas à mão), escolhendo de um conjunto de paletas comuns; nota de 0 a 3 por quantas acerta.
- **2, extração de fonte:** dizer qual é a fonte do texto contornado de vermelho, em escolha única, com exemplos do CTXFont.
- **3, espaço negativo:** dada uma imagem de fundo (do Midjourney), escolher o melhor lugar para o título; posições anotadas por designers profissionais.

**Nível do elemento, compreensão semântica:**
- **4, significado da cor:** que tema ou clima uma paleta transmite (dados PAT; por exemplo, preto quase não aparece em paletas de "casamentos e celebrações"); 50 exemplos sem ambiguidade.
- **5, estilo da fonte:** a que estilo a fonte pertence (Fire_Ice, Initials, Cartoon, Groovy etc.), do conjunto Dafonts.
- **6, importância visual:** onde fica o centro visual do design, com o mapa de saliência do Imp-1k convertido em descrições de posição numa grade de 3 por 3.

**Nível do design geral:**
- **7, estilo geral:** o estilo de um cartaz do conjunto Poster (Zhao et al. 2018), 50 exemplos com estilos em distribuição uniforme, anotados com designers.
- **8, metáfora visual:** explicar a metáfora de imagens do VisMet, em pergunta aberta, nota de 0 a 3.

## 3. O GPT-4 como avaliador (seção 3.2 e Tabela 1)

Mesmo em escolha única, os modelos tendem a responder em texto livre, o que impede a correção por regra. O GPT-4 recebe a pergunta, a resposta certa e a saída do modelo e dá uma de quatro notas: correta, parcialmente correta (estilo certo mas resposta à pergunta errada, ou estilo errado mas com os mesmos elementos do certo), incorreta ou irrelevante (não trata da pergunta). O prompt (apêndice, Figura 1) traz a descrição das notas e exemplos de pergunta, resposta certa, saída e nota.

**Validação:** um conjunto de teste de 50 perguntas anotadas por vários anotadores humanos, da tarefa de estilo (as notas falam de estilo), com 22 corretas, 7 parciais, 20 incorretas e 1 irrelevante pela régua humana. Acerto do GPT-4: 100% nas corretas, 100% nas parciais, 75% nas incorretas, 100% na irrelevante, 90% no total. GPT-3.5-turbo: 95,5%, 100%, 10%, 0%, 60% no total. Os autores concluem que o GPT-4 avalia de modo "quite comparable to that of a human evaluator", mais estável e barato. Os erros do GPT-4 ficam todos nas respostas que os humanos deram como incorretas: 5 das 20 receberam outra nota. O GPT-3.5 erra 18 das 20.

## 4. Resultados (Tabela 2; tudo normalizado a 1, média das quatro posições da resposta)

**Controle de posição:** cada pergunta foi repetida quatro vezes, com a resposta certa em cada uma das quatro posições, dando 200 perguntas por tarefa; a Tabela 2 é a média por posição.

**Por modelo (cor reconhecida, fonte reconhecida, layout reconhecido, cor entendida, fonte entendida, layout entendido, estilo, metáfora, média):**
- aleatório: 20,0; 25,0; 25,0; 25,0; 25,0; 25,0; 25,0; 0,0; 21,3.
- InstructBLIP: 8,7; 22,0; 20,5; 14,0; 31,5; 25,0; 78,5; 6,0; 25,8.
- MiniGPT-4: 34,0; 30,0; 23,0; 26,5; 26,0; 31,0; 34,5; 10,7; 27,0.
- Otter: 60,7; 25,0; 22,0; 34,0; 32,5; 28,0; 47,5; 12,7; 32,8.
- LLaMA-Adapter v2: 49,3; 34,0; 31,0; 30,0; 23,0; 35,5; 46,5; 21,3; 33,8.
- BLIP-2: 52,7; 35,0; 30,0; 45,5; 32,0; 32,0; 82,5; 4,0; 39,2.
- mPLUG-Owl2: 49,3; 40,5; 35,5; 54,5; 33,0; 28,5; 66,5; 18,7; 40,8.
- LLaVA v1.5: 64,0; 38,5; 28,0; 45,5; 43,0; 31,5; 82,0; 26,0; 44,8.
- Gemini Pro Vision: 65,3; 39,5; 50,5; 71,5; 63,0; 26,0; 70,0; 33,3; 52,4.
- GPT-4 Vision: 72,0; 43,5; 55,5; 78,0; 48,5; 45,0; 87,5; 45,3; 59,4.

**Leitura dos autores:**
- As tarefas são difíceis: o melhor, GPT-4V, fica em 59,4%, abaixo do limiar de aprovação de 60% que os autores adotam.
- Cor vai melhor que fonte e layout: GPT-4V 72,0% em cor reconhecida contra 43,5% em fonte. A dificuldade com fonte viria da falta de dados de fonte no treino; com layout, da dificuldade com relações espaciais.
- BLIP-2 supera o InstructBLIP (o mesmo modelo com ajuste por instruções) nas tarefas de cor, o que os autores leem como possível troca entre alinhar a preferências humanas e otimizar a capacidade.
- Metáfora: a falha vem de reconhecer o objeto de design, não de raciocinar. Na análise de erros, nenhum caso de "legenda certa, raciocínio errado", mas 8% de "raciocínio certo, legenda errada". Exemplos da Figura 5: o LLaVA não reconhece o uso criativo de um disco de vinil e erra o estilo; o GPT-4V não vê as poltronas de teatro dentro de um carro e erra a metáfora.

## 5. Viés de posição (seção 4.4 e apêndice, Tabelas 1 a 4)

Os modelos variam muito com a posição da resposta certa. Extração de fonte por posição (0, 1, 2, 3): InstructBLIP 52, 18, 12, 6; MiniGPT-4 74, 18, 18, 10; LLaMA-Adapter v2 58, 22, 28, 28; LLaVA v1.5 54, 52, 32, 16; GPT-4V 50, 36, 42, 46; Gemini 46, 30, 38, 44. Estilo geral: MiniGPT-4 76, 28, 20, 14; GPT-4V 86, 86, 88, 90 (a média no apêndice aparece como 27,5, erro de digitação; a Tabela 2 dá 87,5). Importância visual: BLIP-2 20, 24, 32, 52; GPT-4V 38, 46, 54, 42. Os modelos fracos preferem a primeira opção; o GPT-4V é mais equilibrado, mas não neutro.

## 6. Mexer no prompt (seção 4.3)

**Reescrever a pergunta com outro LLM (tarefa 7, estilo; Tabela 3; original, reescrita por LLaMA2, Vicuna, GPT-4, Gemini; desvio padrão):**
- Otter (base MPT): 47,5; 38,0; 52,0; 33,0; 48,0; 7,9.
- mPLUG-Owl2 (base LLaMA2): 66,5; 77,0; 76,5; 70,0; 74,0; 4,5.
- LLaVA (base Vicuna v1.5): 82,0; 79,5; 83,5; 80,0; 81,5; 1,6.
- GPT-4V: 87,5; 89,5; 90,0; 88,0; 90,0; 1,2.
- Gemini Pro Vision: 70,0; 67,5; 75,0; 69,5; 72,0; 2,8.

Achados declarados: quanto melhor o modelo na tarefa, mais robusto às variações de prompt (desvio de 7,9 no Otter contra 1,2 no GPT-4V); reescrever com o próprio LLM de base do modelo sempre melhora sobre o original; e o Vicuna, que só reescreve sem acrescentar texto, rende mais que o GPT-4, que acrescenta passos de solução. Tirando esses passos acrescentados, o LLaVA chega a 85%.

**Acrescentar conhecimento da tarefa (tarefa 5, estilo de fonte; Figuras 3 e 4):** duas formas de informação equivalente: texto (descrição de cada estilo, gerada pelo GPT-4V a partir das imagens de exemplo e ajustada à mão) ou imagens de exemplo de cada estilo.
- GPT-4V: original 48,5; com texto 51,0 (+2,5); com as imagens juntadas numa só 56,5; com várias imagens 59,0 (+10,5).
- LLaVA v1.5: original 43,0; com texto 46,0 (+3,0); com imagem composta 38,5 (piora; o LLaVA só aceita uma imagem).
- Conclusão dos autores: os dois tipos ajudam, mas exemplos em imagem dão ganho muito maior que a descrição em texto. Juntar exemplos numa imagem composta pode servir a modelos de imagem única, mas prejudicou o LLaVA, que talvez não distinga os exemplos dentro de uma imagem, coerente com o desempenho fraco dele em layout.

## 7. Limites

Declarados ou visíveis no texto: trabalho em andamento; 50 instâncias por tarefa; a validação do avaliador cobre uma tarefa e 50 casos; o material suplementar prometido aparece só como as tabelas por posição; os experimentos de prompt rodam em uma tarefa cada. A conclusão do artigo afirma que o benchmark "sets a new standard".

## 8. Tudo o mais que ensina

- **Taxonomia de dois níveis** (elemento e design geral; visual e semântico em cada elemento), herdada de Huang et al. 2023, e a ideia de que os elementos devem obedecer aos próprios princípios e servir ao conjunto (cores com contraste e cooperação alinhadas ao clima e ao estilo).
- **Por que modelos tropeçam em design:** dados de design quase ausentes no pré-treino; elementos de design abstratos e diferentes de objetos do mundo real; falta de conhecimento de design (contraste e harmonia de cor, clareza e simbolismo das fontes, intenção do layout).
- **Trabalhos relacionados citados:** DesignBench (Lin et al. 2023, benchmark de design para texto-para-imagem com o DALL-E 3, cujas tarefas de cor, fonte, layout e estilo foram incorporadas aqui); geração de layout (LayoutTransformer, LayoutDM); sugestão de paleta (Bahng et al. 2018, PAT); predição de fonte em contexto (Zhao et al. 2018); importância visual em design gráfico (Fosco et al. 2020, Imp-1k); personalidade de designs (Zhao et al. 2018, Poster); prompt visual por inpainting (Bar et al. 2022), que inspirou a imagem composta.
- **Modelos avaliados e versões:** LLaVA v1.5 (Vicuna 13B), Otter (MPT-7B), LLaMA-Adapter v2 (LLaMA 7B), MiniGPT (v2, LLaMA2 7B; a tabela diz MiniGPT-4), InstructBLIP (Vicuna 13B), mPLUG-Owl2 (LLaMA2 7B), BLIP-2 (FLAN-T5-XXL, 12B), Gemini Pro Vision e GPT-4 Vision por API.
