---
titulo: "When Ground Truth Disagrees: A Human-in-the-Loop Audit of Annotation Errors in High-Stakes Crash Narratives"
tipo: paper
autor: "Md Sajjad Hossain, Lin Li, Judy A. Perkins, John Clary, Joel Meyer"
url: "https://aclanthology.org/2026.law-main.18.pdf"
publicado_em: 2026-07-03
capturado_em: 2026-11-04
licenca: "PDF dos anais do 20th Linguistic Annotation Workshop (LAW XX, ACL, 2026, páginas 241 a 256) sem licença escrita no texto lido; tratado como protegido: só a ficha"
areas: [agent-engineering]
tags: [annotation-quality, structured-labels, adjudication, uncertainty-marking, human-label-variation, crash-narratives, single-annotator, ground-truth]
---

# Hossain et al. 2026 (LAW XX): o código estruturado do policial contra o rótulo lido na narrativa

Ficha em palavras próprias, em estrutura própria (artigo protegido: o integral não entra). Lida no texto bruto do PDF em 2026-11-04. Auditoria de quanto os códigos estruturados de fatores contribuintes, preenchidos por policiais em boletins de acidente de trânsito, batem com o que um anotador lê nas narrativas escritas dos mesmos boletins, e de como a incerteza marcada pelo anotador serve de filtro para a adjudicação por um especialista. Os dados são da Secretaria de Transportes e Obras Públicas de Austin (TPW), sob acordo de compartilhamento; dois dos coautores são dessa secretaria.

## O problema que o artigo enfrenta

Em domínios sensíveis (aqui, segurança viária) a anotação é limitada por confidencialidade dos dados, pouco acesso a especialistas e falta de pipelines com muitos anotadores. O trabalho anterior sobre narrativas de acidentes trata os códigos estruturados da polícia como gabarito; os autores dizem que nenhum estudo auditou a qualidade desses códigos contra rótulos independentes derivados da narrativa. As duas perguntas: como as discrepâncias entre código estruturado, anotação da narrativa e correção adjudicada revelam erro sistemático e ambiguidade linguística; que papel a marcação explícita de incerteza e a adjudicação têm para resolver a ambiguidade.

## Dados e desenho

- **Dados:** 9.387 registros, cada um com um campo estruturado (até cinco códigos escolhidos entre 72 opções) e uma narrativa livre. Os 72 códigos foram reduzidos, com os especialistas, a oito categorias: excesso de velocidade, direção sob efeito de álcool ou drogas, direção distraída, falha em dar preferência, avanço de sinal vermelho, acidentes ligados a acesso, obstrução visual e outros. Os dois lados foram convertidos para as mesmas oito classes antes da comparação.
- **Três camadas:** (1) códigos estruturados do policial; (2) anotação feita só pela narrativa, com os códigos escondidos para não vazar rótulo, multirrótulo, com uma marca explícita de "incerto" para narrativa ambígua ou insuficiente; (3) rótulo adjudicado.
- **Anotação:** um único anotador treinado, cerca de 14 meses, com reuniões regulares de revisão com os especialistas da TPW (os coautores), nas quais decisões eram auditadas e as diretrizes refinadas.
- **Adjudicação guiada pela incerteza:** só as narrativas marcadas como incertas vão a uma revisão conjunta entre o anotador e um especialista, que veem a narrativa e os códigos estruturados; os rótulos podem sair confirmados, revisados ou deixados sem resolução por falta de evidência. As não marcadas seguem sem mudança, por desenho.

## Resultados

**Código estruturado contra narrativa.** 50,6% dos registros concordam por inteiro; 49,4% (4.640, ou 4.633 em outra passagem do texto) têm pelo menos uma discrepância. Omissão (fator na narrativa, ausente dos códigos) em 33,3% dos registros; rótulo sem suporte (código sem evidência na narrativa) em 45,4%. Kappa de Cohen macro: 0,446 ("moderado"). Por classe: avanço de sinal vermelho 0,696, falha em dar preferência 0,677, velocidade 0,624, obstrução visual 0,578, outros e álcool/drogas em torno de 0,38 a 0,45, direção distraída 0,167, acidentes ligados a acesso 0,000. Direção distraída: 87% (86,8% no resumo) dos códigos sem suporte na narrativa, 2.871 vezes nos códigos contra 437 nas narrativas; direção sob álcool ou drogas: 69%. Acidentes ligados a acesso: 100% de omissão, 236 casos na narrativa e nenhum no código. A matriz de confusão mostra substituição sistemática (certos códigos tomam o lugar de outros fatores), não ruído ao acaso.

**Narrativa contra adjudicado.** 852 registros (9,1%) foram marcados como incertos; 8.535 (90,9%) não. Dos incertos, 696 foram confirmados (7,4% do total) e 156 corrigidos (1,7% do total; 18,3% dos incertos). Concordância entre narrativa e adjudicado: 98,3%; kappa macro 0,990 (todas as classes com 0,966 ou mais; obstrução visual 1,000, outros 0,966). A maior correção líquida foi em "falha em dar preferência" (+42); a transição mais frequente foi de "outros" para "falha em dar preferência" (17 casos; o inverso, 7). Os autores leem a marcação de incerteza como conservadora e a divergência como vinda dos códigos estruturados, não de inconsistência na leitura da narrativa. Ressalva do próprio texto: a adjudicação só olhou os marcados, de modo que o desacordo total pode estar subestimado.

**Taxonomia de discrepâncias** (categorias não excludentes, entre os códigos estruturados e o adjudicado): sem discrepância 4.754 (50,6%); erro, isto é, código sem suporte, 4.225 (45,0% de todos, 91,2% das discrepâncias); omissão 2.911 (31,0%; 62,8%); ambiguidade (o adjudicado inclui "outros" e há discrepância) 799 (8,5%; 17,2%); compressão (informação da narrativa que o sistema estruturado não consegue representar) 238 (2,5%; 5,1%). Direção distraída: 2.484 erros e 50 omissões; acesso: só omissão; "outros": 680 omissões e 669 erros. Aviso do texto: "sem suporte" não significa que o policial errou; significa que o código não pôde ser verificado na narrativa pelas diretrizes do estudo; os códigos podem refletir convenção da agência ou informação que o policial tinha e não escreveu.

**Fontes linguísticas de ambiguidade** (cinco): hedging ("possivelmente", "pode ter"), causalidade implícita, subespecificação (a narrativa não diz por que o carro saiu da pista), compressão de vários eventos (duas colisões em sequência, um só código) e marcadores de perspectiva (o que os motoristas disseram, não o que o policial verificou). Os exemplos foram parafraseados e anonimizados, por contrato.

**Incerteza como sinal.** Registros marcados como incertos discordam do código estruturado em 88,1%, contra 45,5% dos não marcados; qui-quadrado 562,37; razão de chances 8,91 (p < 10^-124). A taxa de incerteza mais alta foi na classe "outros" (30,6%), depois falha em dar preferência (10,0%) e obstrução visual (9,9%); a mais baixa em direção distraída (1,8%) e álcool/drogas (4,5%), apesar das altas taxas de código sem suporte nelas: os autores leem que esses fatores aparecem de forma explícita nas narrativas mas são sub-representados nos códigos.

## Limitações declaradas

Um único anotador, o que pode introduzir viés dele; ele reanotou um subconjunto aleatório depois de um intervalo e o resultado foi revisado, sem estatística formal de concordância intra-anotador (ficou para trabalho futuro). Dados confidenciais, sem compartilhamento integral. A redução de 72 códigos para oito apaga distinções finas. Adjudicação só nos incertos. Planos: apoio semiautomático com modelos que prevêem incerteza, treino consciente de erro, e liberação de um subconjunto e da ferramenta de anotação se o acordo de dados permitir.

## Trabalhos relacionados que o artigo cita

Northcutt et al. (2021): média de 3,4% de erros de rótulo em 10 conjuntos de teste populares. Klie et al. (2023): 18 métodos de detecção de erro de anotação em 9 conjuntos, sem método que funcione em todas as tarefas. Weber-Genzel et al. (2024), VariErr NLI: protocolo de duas rodadas para separar erro de anotação de variação legítima de rótulo humano. Swayamdipta et al. (2020): Dataset Cartography. Plank (2022) e o perspectivismo de dados (Basile et al., 2021): a divergência entre anotadores carrega sinal, e a suposição de uma verdade única costuma ser inadequada; a tarefa LeWiDi do SemEval-2023.

## O que a fonte não diz

Não compara o anotador único com um segundo anotador independente, nem mede o acordo intra-anotador. Não diz quantos dos 696 confirmados estavam certos de fato além da concordância com o próprio especialista que adjudicou. Não testa a estrutura fora do domínio de acidentes.
