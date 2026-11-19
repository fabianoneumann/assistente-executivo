---
titulo: "SAGE: Scalable AI Governance & Evaluation"
tipo: paper
autor: "Benjamin Le, Xueying Lu, Nick Stern, Wenqiong Liu, Igor Lapchuk, Xiang Li, Baofen Zheng, Kevin Rosenberg, Jiewen Huang, Zhe Zhang, Abraham Cabangbang, Satej Milind Wagle, Jianqiang Shen, Raghavan Muthuregunathan, Abhinav Gupta, Mathew Teoh, Andrew Kirk, Thomas Kwan, Jingwei Wu, Wenjing Zhang"
url: "https://arxiv.org/abs/2602.07840"
publicado_em: 2026-02-08
capturado_em: 2026-10-29
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [llm-as-judge, judge-calibration, teacher-student-distillation, human-ceiling, rubric-decomposition, policy-versioning]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv: v1 em 08/02/2026, v4 (lida) em 10/06/2026. Trabalho feito no LinkedIn. A página do arXiv não diz o venue; a referência da ACM no artigo dá o **KDD '26** (Jeju, agosto de 2026, DOI 10.1145/3770855.3818476), segundo a busca, não conferido nos anais. Lido em 2026-10-29, na pesquisa da calibração por dimensão do portão.

## O problema

Avaliar a relevância da busca do LinkedIn (vagas e pessoas) com o julgamento dos donos do produto, numa escala que nem revisão manual nem métrica de clique alcançam. O clique tem viés de popularidade e esconde regressões; a revisão manual não cobre a variedade de consultas.

## A tríade

- **Política:** o critério de relevância escrito em linguagem natural, decomposto em atributos independentes (cargo, senioridade, empresa, local...), cada um com nota própria, combinados por pesos que priorizam o que mais importa ao usuário. Nota graduada de 0 a 4, não comparação em pares, para poder fixar limiares (3 e 4 vão para a vitrine; 0 e 1 são suprimidos).
- **Precedente:** algumas centenas de exemplos representativos anotados por especialistas do próprio time de produto, em vez de muita anotação por leigos. Pequeno de propósito, para ser refeito em horas depois de uma mudança de política.
- **Juiz substituto:** o modelo de ponta (o3) aplicando a política, calibrado contra o precedente.

## A calibração em duas direções

O juiz não só aprende com os humanos: também os critica. Quatro caminhos de retorno:

- **Humano → política:** o anotador marca onde a política manda uma nota que contraria a intuição dele; uma revisão de política periódica decide e escreve a decisão.
- **Humano → humano:** concordância baixa entre anotadores (kappa de Cohen) num tipo de consulta sinaliza política ambígua.
- **Juiz → precedente:** quando o juiz discorda do rótulo humano, lê-se o raciocínio dele; muitas vezes ele achou evidência enterrada em documento longo que o anotador não viu, e o rótulo é corrigido depois de validação por especialista.
- **Juiz → política:** quando o juiz inventa restrição ou aplica lógica inconsistente, costuma ser política mal especificada.

Na busca de pessoas, o kappa linear ponderado juiz-humanos subiu de 0,67 (linha de base no estilo G-Eval) para 0,71, 0,73, 0,75 e **0,77** em quatro intervenções, uma por caminho de retorno.

## A destilação

- O juiz professor (o3) rotula tráfego real; um aluno de 8B é ajustado nessas saídas, com o mesmo prompt e o mesmo esquema de saída, rebalanceando as classes raras (312 mil exemplos). Ajuste completo dos parâmetros funcionou melhor que LoRA.
- **O critério de sucesso é o aluno contra os humanos, no precedente**, não o aluno contra o professor: kappa linear ponderado de pelo menos 0,7, mais F1 para identificar resultados bons (3 e 4) e ruins (0 e 1).
- **Tetos:** humano contra humano, 0,78 (vagas) e 0,83 (pessoas), o limite prático da tarefa; professor contra humanos, 0,76 e 0,77, o limite do aluno; **aluno contra humanos, 0,72 e 0,73**; aluno contra professor, 0,81 (pessoas).
- Custo relativo: aluno 1, professor 92 vezes, humano (piso, preço de Mechanical Turk) 154 vezes.
- Em produção: mais de 10 milhões de anotações por dia e mais de 10 mil consultas por segundo; detectou regressões que a métrica de engajamento não via e contribuiu para +0,25% de usuários ativos diários.

## Lições dos autores

- Curadoria de alta fidelidade vale mais que volume de anotação; o esforço humano mais valioso passa a ser resolver ambiguidade e escrever norma.
- O juiz pode auditar o gabarito: o rótulo humano não é imutável.
- A política precisa ser versionada; senão, mudança de definição aparece como falsa regressão.
- Decompor em atributos torna as falhas depuráveis e dá vocabulário comum ao time.

## Ressalvas

Relato de engenharia de uma empresa sobre o próprio sistema, num domínio (relevância de busca) mais objetivo que gosto estético; o +0,25% de usuários ativos é atribuído pelos autores ao conjunto do que o sistema permitiu fazer, não ao juiz isolado.

---
