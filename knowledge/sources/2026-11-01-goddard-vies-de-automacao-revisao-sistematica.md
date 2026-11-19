---
titulo: "Automation bias: a systematic review of frequency, effect mediators, and mitigators"
tipo: paper
autor: "Kate Goddard, Abdul Roudsari, Jeremy C. Wyatt"
url: "https://doi.org/10.1136/amiajnl-2011-000089"
publicado_em: 2011-06-16
capturado_em: 2026-11-01
licenca: "© BMJ Publishing Group (aberto no PMC, PMC3240751, sem licença Creative Commons): só a ficha"
areas: [agent-engineering]
tags: [automation-bias, automation-complacency, clinical-decision-support, systematic-review, negative-consultation, commission-error, omission-error, mitigation, confidence-display, display-prominence, accountability, reliability-threshold]
---

Ficha de estudo, em palavras próprias. *Journal of the American Medical Informatics Association* 19(1):121 a 127, edição de janeiro e fevereiro de 2012 (publicado online em 2011). Kate Goddard e Abdul Roudsari (City University London), Jeremy C. Wyatt (University of Warwick). Revisão sistemática com PRISMA, feita como parte de um doutorado. Lida no PMC (https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/); o apêndice com a tabela dos 74 estudos não foi aberto. Lida para a rodada investigativa (tema i4), como sucessora da revisão de [[2026-11-01-parasuraman-manzey-complacencia-e-vies-de-automacao]], com foco em frequência e mitigação.

## O resumo

Viés de automação (a tendência a confiar demais na automação) foi revisado sistematicamente com foco em saúde, a partir de 13.821 artigos, dos quais 74 entraram. Fatores da pessoa (estilo cognitivo, experiência), atitudes (confiança no sistema e na própria decisão) e o ambiente (carga, complexidade, pressão de tempo) modulam o viés. Mitigam: treino e responsabilização, na implantação; e, no desenho do sistema, a posição da recomendação na tela, níveis de confiança atualizados junto de cada saída, e dar informação em vez de recomendação.

## 1. Método

- Busca entre setembro de 2009 e janeiro de 2010 em MEDLINE/PubMed, CINAHL, PsycInfo, IEEE Xplore e Web of Science, sem limite de data, só em inglês, em qualquer área (aviação, interação humano-computador, militar, saúde).
- Concordância entre dois revisores na extração: 87% bruta, kappa 0,84.
- Perfil: 15 estudos de detecção auxiliada por computador, 16 de outros apoios clínicos, 27 de aviação, 6 de interação humano-computador geral, 3 militares, 7 outros.

## 2. Frequência

- **Meta-análise pequena** (4 estudos de saúde homogêneos, apoio não interruptivo em texto, erros de comissão): o risco de seguir a recomendação errada foi 26% maior com o apoio do que no grupo sem ele (razão de risco 1,26; IC 95% 1,11 a 1,44).
- **Consulta negativa** (a pessoa tinha a resposta certa e troca pela errada depois de ver o apoio), a medida mais limpa: de 6% a 11% dos casos em quatro estudos prospectivos. Friedman et al.: 12% de consultas positivas e 6% de negativas, ganho líquido de 6%. Berner et al.: 21 de 272 (8%).
- **Aviação:** Mosier et al. com 55% de omissão e 0% de comissão num estudo; Skitka et al. com comissão maior que omissão em dois.
- **Detecção auxiliada por computador:** resultados mistos; quatro estudos com queda de sensibilidade e especificidade quando o apoio erra, quatro com sensibilidade maior e especificidade menor, e alguns sem viés, como um em que os falsos positivos do apoio eram diferentes dos que as pessoas marcariam e fáceis de descartar.
- **Confiabilidade:** sistemas muito confiáveis, mas não perfeitos, aumentam a complacência; menos confiáveis (sem serem obviamente ruins) a reduzem. Madhavan e Wiegmann põem o ótimo em 70% de confiabilidade, abaixo do qual o desempenho cai ou o sistema é abandonado (citado, não aberto).

## 3. Mediadores

- **Experiência:** inexperiência na tarefa aumenta o viés, mas os inexperientes também ganham mais com o apoio; a experiência específica com o sistema pode diminuir a monitoração (habituação, Bailey e Scerbo).
- **Confiança na própria decisão contra confiança no sistema:** quem confia mais na própria decisão depende menos do apoio; médicos menos seguros do próprio diagnóstico aceitam mais a recomendação (Dreiseitl e Binder). A confiança mal calibrada é, para os autores, provavelmente o motor mais forte; há um viés de positividade a favor do apoio automático sobre o humano (Dzindolet et al.).
- **Tarefa e ambiente:** tarefas mais complexas, carga maior e pressão de tempo empurram para o uso heurístico do apoio, com um estudo em sentido contrário (dificuldade maior levou a olhar mais de perto).

## 4. Mitigadores

- **Implantação:** mostrar o raciocínio do apoio aumentou a dependência adequada (um estudo); a responsabilização reduz o viés, mas num estudo só a percebida pela pessoa funcionou, não a imposta de fora; cultura de trabalho e normas sociais pesam; o treino pode ajudar a reconhecer o erro do apoio, com evidência contrária citada por Parasuraman e Manzey (o treino reduz mais a complacência que o viés).
- **Desenho do sistema:** recomendação errada em destaque é mais seguida (Berner et al.); detalhe demais na tela torna as pessoas menos conservadoras (Yeh e Wickens); confiança atualizada a cada recomendação, em vez de uma confiabilidade fixa do sistema, melhorou a dependência adequada (McGuirl e Sarter 2006); mostrar o estado (o que está acontecendo) em vez do comando (o que fazer) reduz o viés, porque o comando corta um passo da decisão.
- **Síntese dos autores:** dá para reduzir o viés com menos destaque para a saída do apoio, menos detalhe na tela, confiança atualizada e informação em vez de comandos; a complacência se reduz com alocação adaptativa das tarefas.

## 5. Limites declarados

O viés quase sempre aparece como achado secundário, fora do título e do resumo, o que dificulta a busca; os conceitos seguem mal definidos; a heterogeneidade só permitiu uma meta-análise pequena; ensaios controlados podem não capturar a dependência no mundo real.

## Tudo o mais que ensina

- A maioria dos sistemas de apoio clínico acerta entre 80% e 90%, e o erro ocasional deles é o que puxa a pessoa a reverter uma decisão certa.
- A "consulta negativa" como medida: comparar a decisão antes e depois de ver o apoio separa o viés de quem já errava sozinho.
