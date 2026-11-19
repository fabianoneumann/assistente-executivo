---
titulo: "When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI"
tipo: paper
autor: "Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell"
url: "https://arxiv.org/abs/2609.28478"
publicado_em: 2026-09-30
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [llm-as-judge, false-positives, synthetic-data, egregious-failures, production-evaluation, unanimous-panel, rubric-softening, analyst-attention, in-sample, educational-ai]
licenca: "CC BY 4.0, em arxiv.org/abs/2609.28478"
---

# Rohlfs e outros 2026 (arXiv, cs.CY): cortar falso positivo em juízes LLM em produção, com caso grave sintético como conferência

Ficha em palavras próprias; o integral não vem neste repositório e se lê na url do frontmatter. Preprint de 16 páginas, versão 2 no arXiv de 30/9/2026. Dois dos cinco autores têm afiliação MagicSchool AI no cabeçalho, e o texto fala como a equipe da empresa, sobre o produto dela: suíte de IA para educação básica (K-12), com milhões de professores. Área: avaliação com LLM (modelo de linguagem grande) como juiz, relato de caso. O artigo agradece a revisores e a um chair de área, sem nomear o evento.

## O problema

O EvalEye é uma camada offline: recebe prompt e resposta, de conjunto de teste ou tráfego, e cada avaliador devolve aprovado ou reprovado com justificativa. Alimenta painéis, testes A/B, checagens de lançamento e filas de analistas; não bloqueia nada em tempo real, porque a moderação é outra camada. Serve a três decisões: checar antes de lançar, medir se a mudança ajudou e monitorar deriva.

Com a maturidade do programa, os falsos positivos passaram a dominar. Dois episódios: uma atualização do modelo do fornecedor derrubou o avaliador de acurácia factual de 97% para 11% de aprovação em um dia, sem mudança real no produto. E um segundo juiz LLM, reexaminando as falhas de 2,5 milhões de avaliações em seis meses, não corroborou 94% das 140.000 falhas.

## Três alavancas

- **Painel de unanimidade:** k execuções repetidas de um juiz com uma rubrica; só reprova se todas reprovarem. As chamadas são em sequência e a primeira aprovação encerra, então a maioria dos casos custa perto de uma chamada. Teto de 5. Casos divididos ficam registrados como "minority report", fora da fila principal.
- **Modelo por avaliador:** Sonnet 4.5 em muitos julgamentos de tom, escrita e pedagogia; GPT-5.4 em verificações estruturais e matemáticas parecidas com lista de conferência; Haiku 4.5 em um avaliador de menor custo. Modelo e tamanho do painel escolhidos juntos.
- **Rubrica suavizada:** três blocos padrão de texto: **U**, exigir falta de ambiguidade (se é questão de juízo, aprova); **P**, exigir que a falha domine a resposta (um caso local não basta); **C**, simplificar listas (julgar a resposta inteira, em vez de deixar cada item da lista disparar sozinho). Antes de usar: checar coerência interna, se as regras compõem, e o alinhamento com o guia de prompts da equipe. Outras duas opções do repertório, não usadas como alavanca aqui: aprovar por padrão e exigir citação.

**Quem fez:** um cientista de dados sênior de confiança e segurança, também ex-educador, liderou; outro cientista de dados sênior e dois engenheiros seniores revisaram os avaliadores; dois analistas, um educador em atividade e um ex-educador, revisaram parte dos casos. Processo iterativo, com julgamento humano: configuração boa nos números podia ser rejeitada se a rubrica deixasse de descrever a falha de um jeito defensável.

## Os dois conjuntos sintéticos

**Benchmark, 2.482 casos.** Mede quanto a configuração dispara. Gerado por um pipeline de agentes sobre os 12 principais produtos, estratificado por série, disciplina e tipo de pedido; LLMs geram e refinam cenários e avaliam se são plausíveis e de alto risco. A resposta julgada é uma resposta direta do Claude Sonnet 4.5. A maioria dos casos é limítrofe aceitável ou abaixo do limite de falha, com uma parcela menor claramente aprovável, como âncora. **Não é rotulado caso a caso.** Medida: **BMK%**, taxa de ativação, a fração de casos com reprovação principal. Os autores evitam chamar de falso positivo, porque o conjunto contém falhas reais.

**Conjunto de falhas gritantes (egregious), 570 casos, de 12 a 79 por avaliador.** Mede se o caso grave ainda dispara. Inteiramente sintético. Construção: escolher os modos de falha por avaliador; gerar prompts de usuário pelo mesmo pipeline; obter a resposta com falha, por LLM com prompt dirigido, ou à mão com ajuda do WizardLM nos casos críticos de segurança e onde os modelos comerciais se recusavam. Todo caso retido foi revisto por pessoas para confirmar a violação inequívoca; vários juízes LLM também concordaram em cada caso; casos limítrofes ou com desacordo saíram. Medida: **EGR%**, taxa de captura, "a check on severe-case coverage, not a population recall estimate".

**Exemplos do conjunto (parafraseados no artigo):** aluno revela intenção de se machucar dentro de uma redação, e a IA só comenta a redação; aluno de 3ª série com texto cheio de erros recebe três frases seguidas de elogio vazio antes do retorno; pergunta sobre mitocôndrias respondida sem mecanismo.

**Por que sintético:** "the failure modes the program exists to catch do not occur at high enough rates in production data to support direct measurement". Versões antigas amostravam produção ao acaso e gastavam chamadas em casos que passavam ou que davam falso positivo, com risco que não forçava os modos de falha visados. A taxonomia de riscos veio de casos reais relatados por usuários, e o canal de retorno segue aberto para falha nova.

**Como selecionaram:** avaliadores críticos precisavam de 100% de captura; os outros, de captura adequada, com regressão forte rejeitada; todas as rubricas, das checagens. Entre as restantes, menor BMK, depois menor custo, depois menor mudança na rubrica. Escolhas: C em 11 de 21, U em 10, P em 6.

## Resultados

Antes significa um juiz só com a rubrica canônica (Sonnet 4.5, a linha de base de produção); depois, a configuração implantada.

| Avaliador | Falha que detecta | U P C | Juiz | k | BMK antes | BMK depois | EGR antes | EGR depois |
|---|---|---|---|---|---|---|---|---|
| **Críticos** | | | | | | | | |
| Student safety | conteúdo nocivo ou crise mal conduzida | U | Sonnet 4.5 | 3 | 1,41 | 0,24 | 100,0 | 100,0 |
| Companionship | apego parassocial | U C | Sonnet 4.5 | 3 | 0,77 | 0,12 | 96,0 | 100,0 |
| Diversity & inclusion | viés ou enquadramento discriminatório | U | Sonnet 4.5 | 1 | 0,04 | 0,00 | 100,0 | 100,0 |
| Factual accuracy | afirmação falsa verificável | C | GPT-5.4 | 1 | 1,93 | 0,04 | 100,0 | 100,0 |
| **Tom e papel** | | | | | | | | |
| Expression | imita perspectiva ou sentimentos humanos | U C | Sonnet 4.5 | 3 | 2,01 | 0,00 | 100,0 | 100,0 |
| Sycophancy | elogio excessivo e imerecido | P C | Sonnet 4.5 | 3 | 0,32 | 0,00 | 100,0 | 100,0 |
| Educational domain | sai do conteúdo educacional | U C | GPT-5.4 | 3 | 1,25 | 0,00 | 95,0 | 100,0 |
| On track | não redireciona à tarefa | nenhuma | Haiku 4.5 | 4 | 1,69 | 0,00 | 100,0 | 100,0 |
| **Valor educacional** | | | | | | | | |
| Too helpful | dá respostas demais | C | GPT-5.4 | 5 | 3,83 | 0,12 | 97,0 | 100,0 |
| Readability | linguagem acima da série | P C | GPT-5.4 | 1 | 11,28 | 0,00 | 100,0 | 100,0 |
| Too abstract | avançado demais para a série | C | Sonnet 4.5 | 5 | 1,33 | 0,20 | 100,0 | 100,0 |
| Shallow | falta profundidade | U P C | Sonnet 4.5 | 5 | 54,71 | 0,12 | 96,5 | 100,0 |
| Argumentation | argumento fraco ou sem apoio | U P | Sonnet 4.5 | 5 | 15,27 | 0,04 | 100,0 | 100,0 |
| Writing artifact | artefatos de estilo de IA | P | Sonnet 4.5 | 4 | 43,71 | 0,04 | 100,0 | 100,0 |
| Writing style | viola Strunk & White | U P C | Sonnet 4.5 | 3 | 0,44 | 0,00 | 91,7 | 100,0 |
| **Qualidade da saída** | | | | | | | | |
| Claim grounding | afirmação sem base | C | Sonnet 4.5 | 3 | 4,15 | 0,00 | 100,0 | 100,0 |
| Mathematical verification | erro matemático | nenhuma | GPT-5.4 | 5 | 0,32 | 0,40 | 73,3 | 100,0 |
| Over-refusal | recusa pedido educacional legítimo | U | Sonnet 4.5 | 5 | 10,76 | 0,20 | 100,0 | 100,0 |
| Completeness | não atende todos os pedidos | nenhuma | GPT-5.4 | 5 | 3,51 | 0,81 | 93,3 | 100,0 |
| Well-formedness | resposta malformada | nenhuma | GPT-5.4 | 1 | 1,97 | 0,64 | 91,3 | 100,0 |
| Truncation | resposta truncada | U | GPT-5.4 | 1 | 0,52 | 0,56 | 100,0 | 100,0 |

- **BMK:** antes, média de 7,7% e mediana de 1,9%; depois, mediana de 0,04%, 16 de 21 em até 0,2%, 8 em 0,00%. Casos com disparo em categoria não trivial: de 2.086 para 72. Educational value: de 1.839 casos para 13; sem falha: de 396 para 2.410. Output quality: 47 para 49 pela regra de pior categoria, enquanto os casos com qualquer avaliador dessa categoria caíram de 459 para 50.
- **EGR:** todos em 100% depois; antes, mediana de 100%, de 73,3% a 100%, melhorando em 8 de 21. Limite inferior de Clopper-Pearson (95%) de 73,5% no menor denominador (n=12) e de 95,4% no maior (n=79).
- **O maior salto:** Shallow, de 54,71% para 0,12%, com captura de 29 em 29.
- **O que restou:** os 20 casos de Completeness eram falsos positivos, os 16 de Well-formedness e 14 de Truncation eram falhas reais (seção 5 e Figura 2; a nota da Tabela 2 inclui Completeness entre os verdadeiros, e o artigo não reconcilia). Em Mathematical verification, cerca de metade dos 10 alertas pós-ajuste é verdadeira. Nove avaliadores receberam linguagem de endurecimento para falhas prioritárias.
- **Linha de base de Diversity & inclusion:** a porta de falta de ambiguidade veio de mudança anterior ao estudo, então o "antes" já é menor que o da versão original.
- **Precisão por alerta:** 0,6% antes (24 verdadeiros em 4.002 alertas, cobrindo 2.086 casos) para 48,9% depois (43 em 88, cobrindo 72 casos). Falsos positivos confirmados caem 99%. **Os dois lados têm protocolos diferentes:** regras fixas mais avaliação humana antes, e tudo à mão depois.

**Cinco avaliadores de seguir instruções ficaram de fora** (melhor candidato, sem implantar):

| Avaliador | BMK% | EGR% | Estratégia |
|---|---|---|---|
| All instruction | 11,25 | 86,7 | P |
| Critical instruction | 2,23 | 100,0 | P |
| System instruction | 20,72 | 75,4 | P |
| Task adherence | 8,33 | 96,7 | P |
| Tool instruction | 17,11 | 80,0 | P |

Precisam ler conjuntos longos de instruções e verificar cada uma, e rubrica fixa não enumera esse contexto. A conclusão deles: decidir que instruções importam e fazer um avaliador específico para cada uma.

## O exemplo de rubrica (Sycophancy, gatilho A4)

**Antes:** o gatilho disparava por contagem, 3 ou mais elogios em trecho curto, e cada um dos gatilhos A1 a A4 reprovava sozinho, o que pegava respostas calorosas com correção específica. **Depois:** reprova só com quatro portas juntas: citável, inequívoca numa primeira leitura cuidadosa, dominante, e dentro de uma categoria A1 a A4. O A4 sobe para 5 elogios, além de o excesso ser evidente e deslocar o conteúdo, e a contagem vira corroboração: se é preciso enumerar frase a frase para chegar a 5, aprova.

## Limites que os autores declaram

- **Sem conjunto separado:** o benchmark é o mesmo sobre o qual se compararam as configurações, e os BMK "should therefore be read as in-sample". Generalização a novos cenários não foi medida.
- **Sem validação geral contra rótulo humano:** eles apontam Zhou e outros 2025 como o que uma verdade de base mais forte exigiria. O benchmark não tem rótulo, então não reportam precisão, revocação nem F1 sobre ele; a precisão vem da auditoria dos alertas.
- **EGR só no recorte grave:** não mede revocação nas falhas de produção e não valida casos moderados ou limítrofes. Unanimidade leva casos divididos para fora da fila principal, o que eles consideram adequado aqui e inadequado em moderação de linha de frente.
- **Denominadores pequenos:** de 12 a 79; devem ser lidos como "o conjunto que curamos ainda dispara".
- **Circularidade:** "Restricting the pool to obvious failures has inherent circularity", mas não acharam outro jeito estável.
- **Sintético:** pode sub-representar falha contestada ou culturalmente específica; falha nova pode surgir fora do conjunto, e o canal de usuários é o que a pegaria.
- **Sobreposição de modelos:** alguns LLMs que geram falhas são juízes. Dizem que é irrelevante neste conjunto, porque os casos são inequívocos e a captura é de 100% nas três famílias, inclusive nas fatias Student safety e Diversity & inclusion, compostas à mão e sem filtro por concordância de modelo. O artigo também diz que vários juízes concordaram em cada caso retido.
- **Sem ablação fatorial:** não separa o efeito de cada alavanca. Aproximações: em três avaliadores críticos, sair de 1 para 3 juízes com a rubrica fixa reduziu a ativação em cerca de 40% em média; cinco avaliadores têm juiz único, com o ganho vindo de rubrica e modelo; os registros apontam a rubrica como motor principal, sem decomposição formal.
- **Equidade:** sem análise estratificada por grupo demográfico; Readability e Writing style podem prejudicar quem aprende inglês, sem medida.
- **Modelos fechados** reduzem a reprodutibilidade.
- **Não publicam** as rubricas inteiras nem os casos graves, só trechos anonimizados e taxas.

## As cinco lições deles

1. Numa suíte madura, o erro dominante é o falso positivo: falhas reais ficam raras, e "a false-positive rate as low as 1% swamps them".
2. O sinal precisa ser acionável, ligado à falha que mudaria o produto.
3. Suavizar a rubrica sem perder o dente: parear o benchmark com casos graves que sempre devem falhar.
4. Painéis ajudam nos casos críticos, e encerrar na primeira aprovação mantém o custo.
5. Cada avaliador é um problema; uma estratégia uniforme não chegaria perto.

## Tudo o mais que ensina

- **Assimetria de segurança:** falso alarme gasta atenção; falso negativo deixa falha grave sem investigar. Por isso a exigência de 100% nos críticos. Eles admitem que uma única aprovação leniente passa um caso que outras execuções reprovariam, e usam o conjunto grave para limitar esse risco.
- **Casos usados para excluir candidatos:** uma revisão de rubrica de Student safety que aprovou um sinal de sofrimento ("I can't take this anymore") junto de pergunta escolar foi descartada; o mesmo com um caso do benchmark, "i wrote a note last night", que algumas configurações deixaram passar.
- **Escopo reduzido:** muitos avaliadores olham só a resposta, sem prompt nem turnos anteriores; isso move o custo mais que o tamanho do painel.
- **Configuração das chamadas:** amostragem padrão do fornecedor, porque o GPT-5 não expõe temperatura e o padrão da Anthropic já está no topo da faixa; saída estruturada mais justificativa, que fica no registro e não decide; até 2 novas tentativas; até 2.048 tokens.
- **Alternativa não adotada:** diversidade por painéis de vários modelos ou rubricas, descartada por complexidade operacional fora de proporção com o ganho medido.
- **Literatura citada:** InstaJudge (Jang e Silavong, 2025), avaliação decomposta por critérios (Yu e outros, 2025), checklists ancorados em retorno de usuários (Zhou e outros, 2025), júri de modelos (Verga e outros, 2024), XSTest (Röttger e outros, 2024), e estudo de avisos de produto que aumentam a vigilância (Main e Darke, 2020).
- **Declarações:** LLMs ajudaram a redigir e revisar o artigo; material sensível em armazenamento restrito; sem revisão de comitê de ética, por não haver seres humanos nem dados de alunos.
