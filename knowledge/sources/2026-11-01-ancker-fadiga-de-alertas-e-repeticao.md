---
titulo: "Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system"
tipo: paper
autor: "Jessica S. Ancker, Alison Edwards, Sarah Nosal, Diane Hauser, Elizabeth Mauer, Rainu Kaushal, HITEC Investigators"
url: "https://doi.org/10.1186/s12911-017-0430-8"
publicado_em: 2017-04-10
capturado_em: 2026-11-01
licenca: "CC BY 4.0 (declarada no artigo: 'distributed under the terms of the Creative Commons Attribution 4.0 International License', http://creativecommons.org/licenses/by/4.0/)"
areas: [agent-engineering]
tags: [alert-fatigue, alarm-fatigue, clinical-decision-support, override-rate, repeated-alerts, cognitive-overload, desensitization, alert-volume, informativeness, observational-study]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. *BMC Medical Informatics and Decision Making* 17:36, publicado em 10/04/2017 (recebido em 11/02/2016, aceito em 24/03/2017). Weill Cornell Medical College, Health Information Technology Evaluation Collaborative (HITEC), Icahn School of Medicine at Mount Sinai e Institute for Family Health. Há uma correção de 2019 (BMC 19:227) que só retira uma afiliação errada da primeira autora; não muda dados. Texto extraído do PDF oficial com `pdftotext`; as tabelas saem desalinhadas no texto, e os números da ficha vêm do resumo, do texto dos resultados e das notas das tabelas. Estudo observacional retrospectivo, sem revisão manual de quais recusas de alerta eram apropriadas. Lida para a rodada investigativa (tema i4, fadiga de alarme).

## O resumo

"Fadiga de alertas" é a explicação usual para as altas taxas de recusa de alertas em sistemas de apoio à decisão clínica, mas o conceito é mal definido. Os autores testaram dois mecanismos: **sobrecarga cognitiva** (quantidade e complexidade do trabalho, e o esforço de separar alertas informativos dos que não informam nada) e **dessensibilização** (exposição repetida ao mesmo alerta ao longo do tempo). Com dados de prontuário eletrônico de 112 clínicos da atenção primária (2010 a meados de 2013), a aceitação caiu com a complexidade do trabalho e com os alertas repetidos, mas não com a quantidade de trabalho; e alertas novos não mostraram queda de resposta ao longo do tempo. Conclusão: a fadiga parece vir de muitos alertas pouco informativos num trabalho complexo, e reduzir as repetições para o mesmo paciente é o alvo mais promissor.

## 1. O cenário e os dados

- Rede de centros de saúde comunitários em Nova York e arredores (Institute for Family Health), prontuário EpicCare desde 2003.
- **Amostra:** 112 clínicos (93 médicos e 19 enfermeiros de prática avançada), 1.266.325 lembretes de boas práticas (BPAs) e 326.203 alertas de interação medicamentosa e de alergia, em 430.803 consultas de 99.649 pacientes. Cada clínico recebia, em geral, mais de 4.000 lembretes e 1.000 alertas de medicamento por ano.
- **Lembretes (BPAs):** recomendações de cuidado (vacina, rastreamento, exames de doença crônica, conformidade com metas de qualidade), mostrados ao abrir o prontuário; contam como aceitos se o clínico clicou em aceitar ou abriu o conjunto de pedidos sugerido. Mediana de aceitação por clínico em torno de 19%.
- **Alertas de medicamento:** aceitação geral abaixo de 1%, o que cria efeito de piso (a taxa não tem para onde cair).
- **Medidas de sobrecarga** (criadas pelos autores, sem validação prévia): quantidade de trabalho (pacientes únicos, consultas por ano), complexidade (comorbidades do painel de pacientes, alertas por consulta) e baixo valor informativo (proporção de alertas repetidos para o mesmo paciente no mesmo ano).
- **Modelo:** binomial negativo com o log do número de alertas como offset, por clínico; resultados como razão de taxas de incidência (IRR).

## 2. Os resultados

- **Repetição é comum:** pelo resumo, um quarto dos alertas de medicamento e um terço dos lembretes eram repetições para o mesmo paciente no mesmo ano; a discussão diz o contrário (um quarto dos lembretes e um terço dos alertas de medicamento). A fonte se contradiz; não foi possível resolver pelas tabelas extraídas.
- **Cada lembrete a mais por consulta:** a chance de aceitar caiu 30% (IRR 0,70; p < 0,001).
- **Cada 5 pontos percentuais a mais de repetições:** a aceitação de lembretes caiu 10% (IRR 0,90; p < 0,001).
- **Complexidade dos pacientes:** associada a menos aceitação na análise bivariada, perdeu significância no modelo múltiplo (IRR 0,49; p = 0,06).
- **Quantidade de trabalho:** sem associação (número de pacientes e de consultas).
- **Alertas de medicamento:** efeitos de tamanho parecido, sem significância no modelo múltiplo por causa do piso.
- **A primeira decisão se repete:** entre lembretes repetidos, se a primeira ocorrência foi recusada, as seguintes foram recusadas em 87,9% das vezes; se foi aceita, em 51,9%. Nos alertas de medicamento, 99,9% contra 58,4%.
- **Dessensibilização no tempo:** só 6 alertas novos tinham dados suficientes; só um (o lembrete anual de vacina da gripe para maiores de 65) mostrou pico inicial e queda, que os autores atribuem à sazonalidade. Hipótese não sustentada.
- **Achado lateral:** enfermeiros de prática avançada aceitaram alertas de medicamento 4,56 vezes mais que médicos, mesmo controlando a complexidade dos pacientes; lembretes foram mais aceitos por quem recebia mais alertas de medicamento por consulta (IRR 1,91), provavelmente por um confundidor (pacientes polimedicados).

## 3. O que os autores tiram disso

- Os dados combinam com fadiga por **muitos alertas de pouco valor informativo** mais **trabalho complexo** que dificulta separar o relevante do irrelevante; não com dessensibilização nem com carga de trabalho em si.
- Se fosse dessensibilização, o remédio seria aposentar alertas antigos ou mudar a apresentação para parecerem novos; como não é, o remédio é **cortar a repetição** do mesmo alerta para o mesmo clínico e o mesmo paciente.
- Estudos anteriores citados: a recusa de farmacêuticos caiu de 93% para 86% depois que alertas irrelevantes foram retirados; em laboratório, 13% dos alertas (8 de 211) foram tratados errado sob pressão de tempo por ações automáticas, sem atenção consciente; uma revisão sistemática anterior não achou relação entre volume de alertas e taxa de recusa entre estudos; fora da saúde, cada mensagem semanal a mais de saúde pública reduziu em 41% a chance de lembrar o conteúdo (Baseman et al.); a resposta a alertas de recrutamento para ensaios caiu cerca de 2,7% por semana, de 50% para 35% em 36 semanas.

## 4. Limites declarados

Estudo observacional; métricas novas, sem validação; um único prontuário comercial com alertas interruptivos; sem a gravidade das interações; sem revisão manual para separar a recusa apropriada da inapropriada (muitas recusas são certas, por conhecimento clínico fora do prontuário), então não dá para dizer que reduzir a recusa reduziria a recusa errada; sem dados de ruído, interrupções, pressão de tempo ou multitarefa (o que, dizem, puxaria os achados para o nulo); a exposição muito alta pode ter criado efeito de teto.

## Tudo o mais que ensina

- A distinção entre os dois mecanismos e o remédio de cada um é útil fora da clínica: se a pessoa para de ler por excesso de apontamentos de pouco valor, o remédio é cortar e deduplicar; se é por costume com um apontamento antigo, o remédio seria variar a apresentação.
- A aceitação é medida por clínico, não por alerta; quem responde a alertas varia muito entre profissões.
