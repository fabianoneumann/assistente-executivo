---
titulo: "Insights into the Problem of Alarm Fatigue with Physiologic Monitor Devices: A Comprehensive Observational Study of Consecutive Intensive Care Unit Patients"
tipo: paper
autor: "Barbara J. Drew, Patricia Harris, Jessica K. Zègre-Hemsey, Tina Mammone, Daniel Schindler, Rebeca Salas-Boni, Yong Bai, Adelita Tinoco, Quan Ding, Xiao Hu"
url: "https://doi.org/10.1371/journal.pone.0110274"
publicado_em: 2014-10-22
capturado_em: 2026-11-01
licenca: "CC BY (declarada no artigo: 'open-access article distributed under the terms of the Creative Commons Attribution License'; PLOS ONE usa CC BY 4.0)"
areas: [agent-engineering]
tags: [alarm-fatigue, false-alarm-rate, physiologic-monitoring, intensive-care, alarm-burden, actionability, positive-predictive-value, alarm-annotation, observational-study]
---

Ficha em palavras próprias; o texto integral (licença CC BY) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. *PLOS ONE* 9(10): e110274, publicado em 22/10/2014. Grupo de enfermagem e engenharia da University of California, San Francisco (UCSF), com uma autora da University of North Carolina. Financiado pela GE Healthcare, fabricante dos monitores; os autores declaram que o financiador teve papel mínimo no desenho e nenhum na coleta, análise ou publicação, e que a pesquisadora principal é dona dos dados. Texto extraído do PDF oficial com `pdftotext`; as figuras de ECG não foram lidas como imagem. É o estudo observacional de referência sobre a carga e a precisão dos alarmes de monitor em UTI. Lida para a rodada investigativa (tema i4, fadiga de alarme).

## O resumo

Os monitores fisiológicos disparam tantos alarmes que viram ruído de fundo, e um evento grave pode passar. Durante os 31 dias de março de 2013, todos os dados de monitor de 461 adultos em cinco UTIs (77 leitos) foram guardados: 2.558.760 alarmes únicos (1.154.201 de arritmia, 612.927 de parâmetro, 791.632 técnicos), 381.560 deles audíveis, ou **187 alarmes audíveis por leito por dia**. Das 12.671 alarmes de arritmia anotados por enfermeiras pesquisadoras, **88,8% eram falsos positivos**. Dos 168 alarmes verdadeiros de taquicardia ventricular (fora um paciente com tempestade elétrica), 93% não duraram o bastante para pedir tratamento.

## 1. Por que a pergunta importa

- Em 2010, um paciente monitorado morreu num grande centro médico depois de vários alarmes de frequência cardíaca baixa que ninguém na unidade lembrava de ter ouvido; o órgão federal americano (CMS) atribuiu a morte à fadiga de alarme.
- **Definição usada:** fadiga de alarme acontece quando os profissionais ficam dessensibilizados por alarmes numerosos, muitos falsos ou sem relevância clínica, e o som vira ambiente normal; alarmes são silenciados na central sem checar o paciente ou desligados de vez.
- O ECRI listou a fadiga de alarme como o perigo tecnológico número um em saúde para 2014, e a Joint Commission fez da segurança de alarmes uma meta nacional de segurança do paciente em 2014.

## 2. Método

- Infraestrutura especial de coleta (CARESCAPE Gateway e BedMasterEx) que guardou todas as formas de onda (7 derivações de ECG, pressões invasivas, SpO2, respiração), os ajustes de alarme feitos pelas enfermeiras e todos os alarmes, inclusive os só de texto e os técnicos; todos os pacientes consecutivos, com dispensa de consentimento.
- **Anotação:** seis tipos de alarme de arritmia graves (assistolia, fibrilação ventricular, taquicardia ventricular, ritmo ventricular acelerado, pausa, bradicardia ventricular), julgados verdadeiros ou falsos por quatro enfermeiras com doutorado, por um protocolo escrito com critérios de prova para cada tipo. Concordância em 300 alarmes reavaliados: 95%, kappa 0,86. Só 15 alarmes (0,11%) não puderam ser decididos.

## 3. Resultados

- **Taxa de falso positivo por tipo** (Tabela 6): de 32,3% a 96,7% conforme o tipo; 88,8% no total dos seis.
- **Taquicardia ventricular:** 502 alarmes verdadeiros, 334 deles de um único paciente com tempestade elétrica, cujo desfibrilador implantado encerrava cada episódio; dos 168 restantes, 93% não chegaram aos 30 segundos que as diretrizes usam para tratar.
- **Causas dos alarmes em excesso:** ajustes de alarme não adaptados ao paciente; fibrilação atrial persistente alarmando sem parar; artefato imitando taquicardia ou fibrilação ventricular; complexos QRS de baixa amplitude em algumas derivações causando falsas assistolias, pausas e bradicardias (91% das falsas assistolias e 94% das falsas pausas tinham QRS visível em alguma derivação); QRS largo por bloqueio de ramo ou marcapasso disparando alarmes ventriculares; alarmes de ST que não indicam isquemia de fato; e falha de eletrodo.
- **Falsos negativos:** não medidos; os autores dizem que nenhum evento letal passou, porque os 17 códigos azuis do período foram precedidos de vários alarmes.

## 4. O que os autores recomendam (Tabela 9)

Que o monitor sugira ajustes adequados ao paciente ("FC média = 130; quer subir o limite?"); que a fibrilação atrial só alarme no início e no fim; que, diante de alarmes audíveis repetidos, pergunte se o profissional quer continuar ouvindo; que o algoritmo use todas as derivações para achar uma sem artefato e com QRS visível; atrasos configuráveis para taquicardia ventricular segundo os critérios de documentação (10 s) ou tratamento (30 s); e usar a pressão arterial e a SpO2 para confirmar. Também: uma base pública de alarmes anotados ("gold standard") para testar qualquer mudança de algoritmo, porque cada mudança deve ser testada quanto ao efeito nos falsos alarmes e a consequências não previstas.

## 5. Limites

Um mês, um centro, um fabricante; só seis tipos de alarme anotados; falsos negativos não medidos; atrasos de alarme recomendados por outros estudos ainda sem medida de efeito no desfecho do paciente.

## Tudo o mais que ensina

- A diferença entre **falso** (o evento não aconteceu) e **não acionável** (aconteceu, mas não pede ação): a maior parte dos verdadeiros de taquicardia ventricular era não acionável, e isso também gera fadiga.
- O alarme técnico silencioso pode virar perigo: artefato contínuo suspende toda a detecção de arritmia.
- Os autores dizem que, como o computador é mais confiável que a pessoa em monitorar sem parar, há espaço para melhorar o monitor em vez de pedir mais atenção a quem já está saturado.
