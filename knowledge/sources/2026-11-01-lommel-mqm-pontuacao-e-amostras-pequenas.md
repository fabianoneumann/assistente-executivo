---
titulo: "The Multi-Range Theory of Translation Quality Measurement: MQM scoring models and Statistical Quality Control"
tipo: paper
autor: "Arle Lommel, Serge Gladkoff, Alan Melby, Sue Ellen Wright, Ingemar Strandvik, Katerina Gasova, Angelika Vaasa, Andy Benzo, Romina Marazzato Sparano, Monica Foresi, Johani Innis, Lifeng Han, Goran Nenadic"
url: "https://arxiv.org/abs/2405.16969"
publicado_em: 2024-05-27
capturado_em: 2026-11-01
licenca: "CC BY-NC-SA 4.0 (indicada na página do arXiv). Permite cópia só sem fim comercial e com a mesma licença; como o repositório serve a um negócio, entra só a ficha."
areas: [agent-engineering]
tags: [mqm, error-typology, scoring-model, severity-weighting, calibration, pass-fail-threshold, statistical-quality-control, sample-size, inter-rater-reliability, ceiling-effect, translation-quality]
---

Ficha de estudo, em palavras próprias. arXiv 2405.16969, v1 em 27/05/2024, lida a v5 (05/08/2024); comentário do arXiv: "Accepted by AMTA2024". Autores do MQM Council (o grupo voluntário que mantém o MQM desde 2016), da indústria de tradução (CSA Research, Logrus Global, Argos), das direções-gerais de tradução da Comissão Europeia e do Parlamento Europeu (em nome próprio) e da Universidade de Manchester. Texto extraído do PDF com `pdftotext`; as fórmulas das Figuras 3 e 4 saem como caracteres soltos e foram lidas pelo texto do apêndice. Complementado pela página oficial da tipologia, https://themqm.org/error-types-2/typology/ (licença CC BY 4.0 no rodapé), conferida nesta captura para os nomes das sete dimensões. Lido para a rodada investigativa.

**Atenção à força da evidência:** é um documento de método e de posição, não um experimento. As afirmações sobre tamanho de amostra vêm de trabalhos anteriores dos próprios autores (Gladkoff e coautores, 2022 e 2023) e de questionários de calibração com gestores de qualidade, sem dados novos aqui. A seção sobre modelos de linguagem é opinião ("GenAI não pensa nem entende"), sem medida, e parte dos autores tem interesse comercial em avaliação humana. Vale como a referência oficial do que é o MQM 2.0 (tipologia e modelo de pontuação) e como argumento sobre amostra pequena, não como prova.

## 1. O que é o MQM, segundo quem o mantém

O MQM (Multidimensional Quality Metrics), proposto em 2014 no projeto europeu QTLaunchPad (Lommel, Burchardt e Uszkoreit), é um arcabouço de avaliação **analítica** de tradução: avalia-se uma amostra marcando cada erro com um tipo e uma gravidade, e a nota sai desses dados. Tem dois pilares:

1. **A tipologia de erros**, hierárquica. O MQM Full é o repositório inteiro; o **MQM Core** reúne as **sete dimensões de topo** e os subtipos mais usados: **Terminologia** (termo fora do padrão do domínio ou da organização), **Precisão** (o alvo distorce, omite ou acrescenta ao sentido da fonte; "precisão" aqui é correspondência com a fonte, não acerto factual em geral), **Convenções linguísticas** (gramática, ortografia, pontuação; era "Fluência" na versão 1), **Estilo** (correto, mas fora do guia de estilo), **Convenções locais** (formatos de data, moeda e afins), **Adequação ao público** (conteúdo inválido ou impróprio para o público ou o local; era "Verity") e **Design e marcação** (problemas de apresentação física, formatação, integração com gráficos, layout). Quem implanta escolhe um subconjunto com a granularidade que precisa; os nomes têm definição rigorosa e não valem pelo sentido comum.
2. **O modelo de pontuação**: pesos por tipo de erro, multiplicadores por gravidade e a fórmula que transforma a contagem numa nota e num veredito de passa ou não passa, segundo a especificação do cliente.

Montar uma métrica MQM: analisar a especificação do projeto contra a necessidade do usuário final; escolher os tipos de erro que importam; integrar a métrica às ferramentas ou a uma planilha de pontuação; definir tamanhos e procedimentos de amostra.

## 2. Gravidade e pesos (apêndice A.3)

- **Quatro níveis padrão, com multiplicadores 0, 1, 5 e 25:** **Neutro** (mudança de preferência ou erro que não é culpa de quem traduziu; registra sem punir), **Menor** (impacto limitado na usabilidade, compreensão ou confiabilidade para o fim pretendido), **Maior** (afeta seriamente a compreensão, a confiabilidade ou a usabilidade, ou atrapalha o uso do produto) e **Crítico** (torna o conteúdo inteiro impróprio para o fim, ou traz risco sério físico, financeiro ou de reputação). **Em muitos sistemas, um único erro crítico reprova sozinho.** Três ou dois níveis também são comuns.
- A diferença entre os multiplicadores deve ser **exponencial**, para refletir o salto de risco entre os níveis.
- **Pesos por tipo de erro** (Error Type Weight): 1 para todos por padrão; podem subir para o que importa mais naquele conteúdo (precisão num texto jurídico; estilo e terminologia num de marca e marketing).

## 3. Os três modelos de pontuação

- **Linear bruto:** soma dos pontos de penalidade (contagem × multiplicador de gravidade × peso do tipo), dividida pelo número de palavras da amostra; a nota é 100 menos essa proporção vezes 100, a fração "sem erro". Problemas: a escala não é legível, o limiar de tolerância muda de lugar de um cenário para outro e cai em números fracionários, e as notas não se comparam entre tipos de conteúdo. **No caso de exigência alta, a nota bruta fica espremida perto de 100** (um cliente jurídico pode exigir 99,5; um de suporte técnico aceita 97,2), e notas muito parecidas ficam difíceis de usar.
- **Linear com calibração** (publicado pelo MQM Council em abril de 2024): o cliente define quantos pontos de penalidade aceita por um número de palavras de referência e associa esse limite a um **limiar de aprovação** numa escala calibrada (por exemplo, 90 de 100). A conta estica a janela estreita entre a nota máxima e o limiar bruto para uma faixa larga e legível. Nota igual ou acima do limiar, passa; abaixo, não passa. A calibração também ajusta a fórmula à percepção de quem avalia.
- **Não linear com calibração:** a percepção humana de erro não é proporcional ao tamanho da amostra. Gestores de qualidade toleram um erro maior numa página, mas não sete em sete páginas: reprovariam já com três ou quatro. Questionários de calibração estendidos, que perguntam a tolerância para vários tamanhos sem deixar a pessoa fazer a regra de três, dão sempre uma curva logarítmica: a tolerância por palavra cai quando a amostra cresce. Os autores atribuem isso a "priming": ver erros deixa o leitor mais atento a eles. Um modelo linear calibrado num tamanho (por exemplo, quatro páginas) erra num tamanho muito diferente (dez páginas).

## 4. A tese das três faixas de tamanho de amostra

- **Baixa concordância entre avaliadores em amostra pequena "não é defeito, é característica".** Linguistas treinados concordam em amostras grandes e discordam no segmento: no alcance do erro, na categoria e na gravidade (Lommel, Popović e Burchardt, 2014). A causa é a ambiguidade da língua e a interpretação do leitor, não a falta de qualificação. Segundo os autores, uma nota automática por frase é tão incerta que não faz sentido, qualquer que seja o método.
- **Abaixo de cerca de uma página (15 a 17 frases, 250 palavras), não se mede qualidade por avaliação analítica**, a menos que a amostra seja o texto inteiro: o caso é de **controle estatístico de qualidade** (inspeção por atributos, ISO 2859), cuja saída não é uma nota, mas a probabilidade do risco do produtor e do consumidor. Um trabalho anterior dos autores achou que, para a nota variar pouco, a amostra precisa de mais de 200 frases (3.400 palavras); com menos, o intervalo de confiança "explode". O exemplo mais baixo de métrica confiável que citam é a certificação da ATA: uma página traduzida, mas lida por **dois** revisores e em **duas** amostras de tipos diferentes, para compensar a incerteza.
- **De cerca de 300 a 5.000 palavras**, a avaliação analítica linear funciona; **acima de cerca de 5.000**, entra a não linearidade.

## 5. Sobre modelos de linguagem (opinião dos autores)

Os autores afirmam que modelos generativos erram fatos ao gerar e "não veem" erros ao anotar, que quanto melhor a saída mais variável a avaliação do modelo, e que toda métrica automática dá um número de confiabilidade desconhecida que precisa ser validado por avaliação humana analítica em amostras de tamanho suficiente, com avaliadores treinados e monitorados. Não há experimento que sustente isso no artigo.

## 6. Tudo o mais que ensina

- **Erros não são independentes nem uniformes no texto:** alguns só aparecem porque outro erro fundamental os provocou, e a densidade varia por trecho e por tipo de material. Por isso se avalia por amostras e, quando possível, o texto inteiro.
- **A nota é relativa a uma especificação:** o mesmo texto passa para um cliente e reprova para outro; o limiar vem do uso, não da tipologia.
- **A planilha de pontuação (scorecard)** registra, por tipo e por gravidade, a contagem e os pontos, com a contagem de palavras da amostra, o limiar e o veredito; hoje isso vive dentro das ferramentas de tradução.
- **A norma ISO 5060** (avaliação de tradução) admite contagem por caracteres ou por linhas no lugar de palavras, para línguas com contagens muito diferentes.
- **Calibrar exige uma pergunta bem feita:** quem já domina a fórmula linear responde a tolerância fazendo a regra de três; é preciso perguntar a quem não domina ou pedir explicitamente que não faça a proporção.
