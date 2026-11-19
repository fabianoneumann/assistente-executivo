---
titulo: "BAT-RM: A Boundary-Aware Transformer with Region-Aware Multi-Directional Mamba for Clinically Deployed Cervical Cancer Radiotherapy Auto-Contouring"
tipo: paper
autor: "Istiak Ahmed, Kazi Shahriar Sanjid, Galib Ahmed e outros 16 autores (North South University, Dhaka, e instituições parceiras); autor para correspondência: Istiak Ahmed"
url: "https://arxiv.org/abs/2607.11949"
publicado_em: 2026-07-11
capturado_em: 2026-11-04
licenca: "CC BY 4.0 (indicada na página do arXiv, arxiv.org/abs/2607.11949, que liga a creativecommons.org/licenses/by/4.0/); o integral está na url"
areas: [agent-engineering]
tags: [reader-study, washout, auto-contouring, radiotherapy, human-ai-assistance, recall-bias, pilot-study, medical-imaging]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Lido no PDF de 48 páginas em 2026-11-04 (preprint "submitted to Elsevier", arXiv v1, 11 de julho de 2026).

## Sobre o que é o artigo

Não é um estudo de revisão de saídas de IA nem de dependência: é a apresentação de um sistema de contorno automático de volumes em radioterapia de câncer do colo do útero (o modelo BAT-RM, uma rede híbrida com atenção guiada por bordas e módulo Mamba multidirecional), com banco de dados, comparação com quatro modelos de referência, estudo de leitores e implantação em hospital. Interessa a esta base pela parte do estudo de leitores (seção 5), que usa um intervalo de lavagem (washout) entre sessões com e sem a IA para o mesmo leitor ver os mesmos casos duas vezes.

## O desenho do estudo de leitores (seção 5.1)

- Protocolo pré-registrado, conduzido ao longo de oito meses (janeiro a agosto de 2025), com 13 radio-oncologistas titulados de três instituições de Bangladesh: quatro experts (o texto extraído mostra "20 years" para essa faixa, com o símbolo de comparação perdido), quatro seniors (10 a 19 anos) e cinco juniors (menos de 10 anos).
- Os mesmos 100 casos de pacientes (40, 30 e 30 de cada centro), separados dos dados de treino e validação, travados antes do treino do modelo. O texto reconhece que isso é uma avaliação dentro da distribuição.
- Cada leitor contornou os 100 casos em duas condições, que o texto chama de "randomizadas": sem auxílio (manual) e com a IA (BAT-RM com correção manual), separadas por quatro semanas de washout. O texto não detalha o que foi randomizado nem o procedimento de sorteio.
- Justificativa do washout: um piloto com 3 leitores e 20 casos não mostrou recordação significativa de casos específicos depois de 14 dias, e os autores somaram duas semanas de margem. Além disso, os leitores processavam de 2 a 3 casos por semana durante os oito meses, o que tornaria improvável a lembrança detalhada de um lado a outro do intervalo. Leitores cegos para os próprios contornos anteriores e para a verdade de referência.
- Desfechos primários: acurácia da segmentação (IoU) e tempo de contorno; secundários: taxa de consulta, confiança autorrelatada (0 a 1), esforço de revisão (fatias editadas por caso) e classificação das edições (grandes, pequenas, nenhuma). Comparações pareadas de Wilcoxon com correção de Bonferroni. O tempo foi registrado automaticamente (no modo com IA inclui 18 s de inferência mais a correção); sessões com ociosidade acima de 5 minutos foram excluídas e repetidas.

## Ressalva dos autores sobre a lembrança parcial

Na seção de limitações: o estudo ocorreu só em Bangladesh e não estabelece generalização a cenários com mais recursos; e, embora o washout de quatro semanas tenha sido mantido, "partial recall of challenging cases cannot be completely excluded" (a lembrança parcial de casos desafiadores não pode ser totalmente excluída). Pedem um estudo de leitores multinacional, prospectivo e pré-registrado.

## Resultados do estudo de leitores

IoU sem auxílio e com a IA: juniors de 0,8987 para 0,9648 (+0,0661; acima do modelo sozinho, 0,9465), seniors de 0,9379 para 0,9766, experts de 0,9798 para 0,9857 (ganho pequeno, atribuído a efeito teto). Tempo médio dos juniors de 152 para 29 minutos (80,7% a menos); seniors economizaram 74 a 78 minutos por caso e experts 34 a 39. Taxa de consulta: juniors de 52,1% para 14,3%, seniors de 19,0% para 4,2%, experts de 3,9% para 1,4%. Confiança: juniors de 0,590 para 0,828, seniors de 0,760 para 0,871, experts de 0,950 para 0,961. Concordância de Jaccard entre juniors e experts: de 0,824 sem IA para 0,934 com IA. A estrutura mais editada foi o GTV (42%), depois o CTV (31%) e o reto (15%), por limite no plano, e não por descontinuidade entre fatias.

## O sistema, o banco de dados e a implantação (resumo)

Banco com 1.011 pacientes de três centros, sete classes de órgãos e volumes-alvo, com concordância entre 7 anotadores (Jaccard 0,961 ± 0,024); validação externa em 230 pacientes de uma coorte independente; BAT-RM supera quatro modelos de referência (nnUNet, SegMamba, TransUNet, UNETR) em todas as sete classes, segundo os autores, com teste de Wilcoxon e correção de Holm-Bonferroni em 168 comparações; o sistema tem interface web com exportação DICOM RTSTRUCT e foi implantado na Bangladesh Medical University. Nos oito meses depois da implantação, o tempo de espera para simulação caiu de 1 a 3 dias para 2 a 3 horas; o texto qualifica isso como achado observacional, sem braço de controle, com outros fatores operacionais mudando ao mesmo tempo. Limitações adicionais: pacientes de uma única região metropolitana (Dhaka), só tomografia, sem integração com sistemas hospitalares.

## O que a fonte não traz

Nenhum teste de reconhecimento ou recordação dos casos ao fim do washout além do piloto de 3 leitores; nenhum dado do piloto no texto (só o desfecho); nenhuma regra geral para a duração do washout; nenhum item plantado nem medição de aceitação de saídas erradas da IA.
