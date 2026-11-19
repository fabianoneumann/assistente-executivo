---
titulo: "Lessons from Building Static Analysis Tools at Google"
tipo: artigo
autor: "Caitlin Sadowski, Edward Aftandilian, Alex Eagle, Liam Miller-Cushon, Ciera Jaspan"
url: "https://doi.org/10.1145/3188720"
publicado_em: 2018-04-01
capturado_em: 2026-11-01
licenca: "© ACM; cópia aberta hospedada pelo Google Research (storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf): só a ficha"
areas: [agent-engineering]
tags: [static-analysis, effective-false-positive, warning-blindness, developer-trust, workflow-integration, code-review, feedback-loop, actionability, alert-fatigue, practitioner-report]
---

Ficha de estudo, em palavras próprias. *Communications of the ACM* 61(4):58 a 66, abril de 2018 (seção "contributed articles"). Equipe de análise estática e de compiladores do Google. Relato de prática de engenharia, sem experimento controlado; os números vêm da operação interna e de uma pesquisa com desenvolvedores. Lido inteiro no PDF hospedado pelo Google Research, extraído com `pdftotext` (a página da CACM devolveu 403). Lido para a rodada investigativa (tema i4): é o caso mais documentado de um avaliador automático cujos apontamentos uma pessoa lê e decide se acata, num fluxo de revisão.

## O resumo

Para uma ferramenta de análise estática dar certo, os desenvolvedores precisam sentir que ganham com ela. O que o Google aprendeu: integrar ao fluxo de trabalho (no compilador e na revisão de código, nunca num painel à parte), mostrar só o que é acionável, medir o falso positivo **pelo que o desenvolvedor faz** e não pelo que o autor da ferramenta acha, e desligar o analisador que irrita. Desenvolvedores têm "a strong bias to ignore static analysis", e qualquer falso positivo vira justificativa para não agir.

## 1. Por que as ferramentas são ignoradas

Lista do artigo: não integradas ao fluxo (ou lentas); avisos não acionáveis; não confiáveis por falsos positivos; o defeito é possível na teoria e não aparece na prática; caro ou arriscado demais de corrigir; aviso não entendido.

## 2. O falso positivo efetivo

- **Definição:** um apontamento é "falso positivo efetivo" se o desenvolvedor não tomou nenhuma ação positiva depois de vê-lo. Se a ferramenta aponta errado mas a pessoa corrige mesmo assim (por legibilidade), não é falso positivo efetivo; se aponta um defeito real que a pessoa não entendeu e por isso ignorou, é. Frase-chave: "Developers, not tool authors, will determine and act on a tool's perceived false-positive rate."
- **Limiares:** checagem que quebra a compilação não pode ter nenhum falso positivo efetivo; checagem mostrada na revisão de código pode ter até 10%, porque na revisão se espera que o retorno não seja perfeito e que o autor avalie antes de aplicar ("Developers should feel the check is pointing out an actual issue at least 90% of the time"). Nota de rodapé dos autores: o número foi escolhido "somewhat arbitrarily" pela primeira autora, mas parece ser um ponto bom para a satisfação e coincide com o corte de sistemas parecidos de outras empresas.

## 3. A história do FindBugs (três tentativas que falharam)

- **Painel:** rodava toda noite sobre o código inteiro; achou centenas de defeitos, mas o painel ficava fora do fluxo e misturar apontamentos novos e antigos distraía; quase ninguém o visitava.
- **Abrir chamados:** uma equipe triava à mão os apontamentos novos de cada noite e abria chamados para os mais importantes. Numa semana de mutirão em maio de 2009, centenas de engenheiros revisaram 3.954 avisos (42% de 9.473); 44% dos revisados (1.746) viraram chamado, mas só 16% (640) foram corrigidos. Muitos eram defeitos reais, mas uma fração grande não era importante o bastante para corrigir na prática, e a triagem manual não escala.
- **Na revisão de código:** os resultados entravam como comentários na revisão, com supressão de falsos positivos e filtro pela confiança da ferramenta; foi descontinuado em 2011 porque os falsos positivos efetivos fizeram os desenvolvedores perderem a confiança e a personalização por pessoa deixava a visão dos resultados inconsistente.

## 4. O que deu certo

- **Compilador:** checagens novas só entram como erro (não aviso, que os desenvolvedores ignoravam) depois que a equipe da ferramenta corrigiu todas as ocorrências existentes no código inteiro. Critérios: fácil de entender, acionável e fácil de corrigir (de preferência com correção mecânica sugerida), sem falso positivo efetivo, e só correção, não estilo.
- **Mais cedo é melhor:** numa pesquisa, os desenvolvedores consideraram "problemas reais" 74% dos apontamentos feitos na compilação contra 21% dos feitos sobre código já entregue, e "críticos" 6% contra 0% ("efeito de sobrevivente": no código entregue, os defeitos importantes já foram pegos por outro meio).
- **Revisão de código (Tricorder):** apontamentos visíveis ao autor e ao revisor; o revisor pode clicar em "Please fix" e costuma segurar a aprovação até a correção; há correção sugerida aplicável com um clique. Na revisão, as pessoas estão em modo crítico e mais receptivas a detalhes de legibilidade e estilo, que na compilação só irritariam.
- **O laço de retorno:** botão "Not useful" que abre um chamado direto para a equipe dona do analisador; a equipe do Tricorder acompanha a razão entre os cliques de "Not useful" e de "Please fix" e, se passa de 10%, desliga o analisador até ele melhorar (raramente para sempre; algumas vezes enquanto subchecagens ruidosas eram revistas). Exemplo: uma checagem correta recebia um "Not useful" por semana de quem não entendia a regra; reescrever a mensagem para dizer a regra de forma direta acabou com os chamados.
- **Escala (janeiro de 2018):** cerca de 50 mil mudanças analisadas por dia; mais de 5.000 cliques em "Please fix" e cerca de 3.000 correções automáticas aplicadas por dia; cerca de 250 cliques em "Not useful" por dia.
- **Mostrar só onde a pessoa está mexendo:** o Tricorder apresenta o apontamento só quando o desenvolvedor está mudando aquele código, antes de entregar.

## 5. As lições, nas palavras dos autores

- A maioria não vai sair do caminho para usar a ferramenta: integrar ao fluxo e ligar para todos por padrão.
- A satisfação do desenvolvedor é chave: se a ferramenta desperdiça tempo com falsos positivos e questões de baixa prioridade, "developers will lose faith and ignore results".
- Não só achar defeitos, corrigi-los: medir o sucesso por defeitos corrigidos, não por apontamentos mostrados. "in practice we did not find such a list motivates developers to fix the defects."
- Para vencer a "cegueira de aviso", foi preciso reconquistar a confiança: vetar cada checagem contra os critérios antes de ligá-la, para que os desenvolvedores raramente fiquem "inundated, confused, or annoyed".

## Tudo o mais que ensina

- Customização por projeto, não por pessoa (a personalização individual foi uma das causas da falha do FindBugs).
- Pontos de integração adicionais só depois de ganha a confiança: linha de comando para quem limpa código, bloqueio de entrega para checagens específicas sem falso positivo, e navegação de código para ver a escala de um problema.
- Por que análises sofisticadas ainda não entram no fluxo central: custo de escala e taxas de falso positivo altas demais.
