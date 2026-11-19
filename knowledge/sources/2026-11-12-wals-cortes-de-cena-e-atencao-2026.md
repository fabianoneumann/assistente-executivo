---
titulo: "The dynamic effects of visual complexity and scene cuts on viewer attention"
tipo: paper
autor: "Sammy Wals, Dhruv Grewal, Ines Wilms, Tim Hilken, Alexia Briassouli, Martin Wetzels (RWTH Aachen, Babson College, Maastricht, Twente, EDHEC, Bath, Tecnológico de Monterrey)"
url: "https://link.springer.com/article/10.1007/s11747-025-01137-x"
publicado_em: 2026-03-26   # "Published: 26 March 2026" e "Version of record: 26 March 2026" na página; fascículo de abril de 2026 (Journal of the Academy of Marketing Science 54, 596–617); recebido em 09/10/2024, aceito em 09/12/2025
capturado_em: 2026-11-12
licenca: "CC BY 4.0 (seção 'Rights and permissions' da página do artigo na Springer: 'licensed under a Creative Commons Attribution 4.0 International License'); o integral está na url"
areas: [generative-media, content-design]
tags: [attention, eye-tracking, attentional-synchrony, scene-cuts, shot-duration, visual-complexity, saliency, film-editing, pacing, camera-shots, video-ads, short-form-video, computer-vision, time-series, neuromarketing]
---

# Wals et al. (2026): cena curta e simples junta o olhar do público, e o corte puxa a atenção dois terços de segundo depois

Ficha de estudo: as seções seguem a ordem do artigo (introdução, revisão e hipóteses, desenho e coleta, método de análise, resultados, discussão, caso, limites, notas), com o método passo a passo e uma tabela de onde sai cada número; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Artigo de acesso aberto no *Journal of the Academy of Marketing Science*, https://link.springer.com/article/10.1007/s11747-025-01137-x (DOI 10.1007/s11747-025-01137-x), baixado em HTML em 2026-11-12. sha256 do arquivo HTML baixado (`fontes/wals-2026-jams-scene-cuts.html` da rodada): (hash omitido); o hash mede o arquivo inteiro, como saiu do download, e não um bloco de texto; sem captura na Wayback registrada no `licencas.json` da rodada. Lido no texto extraído do HTML (a cópia de trabalho), com o título conferido no `<title>` do HTML e na primeira linha do texto, e as datas na seção "About this article". Cobertura: o texto inteiro do artigo, do resumo às notas de rodapé, aos agradecimentos, às declarações de ética e à licença. Não estão no HTML e não foram lidos: o conteúdo das Tabelas 1 a 3 (a página só traz a legenda e o link para uma página à parte de cada tabela), as Figuras 1, 3 e 4 (imagens; da Figura 2 vem só a legenda) e os apêndices web A a H, no material suplementar (DOCX). Os números abaixo saem da prosa do artigo. Licença CC BY 4.0, que permite cópia e obra derivada: o integral não vem neste repositório e se lê na url do frontmatter, e a conferência lado a lado do item 2 do README desta pasta não se aplica.

**Quem fez e com quem.** Seis autores de escolas de negócios e de um grupo de biometria; ética aprovada pelo comitê da Rotterdam School of Management (IRB-E Approval-2020-15); os autores declaram não ter conflito de interesse e nenhum financiamento específico (o acesso aberto foi pago pelo fundo da RWTH Aachen, via Projekt DEAL). A coleta de dados teve o apoio da Alpha.One, empresa que vende o sistema Junbi de avaliação automática de anúncios; o estudo de caso do fim do artigo é de uma campanha que usou o Junbi e foi feito com a mesma empresa.

## Em uma frase

Num laboratório, 30 pessoas viram duas vezes 42 anúncios de utilidade pública de cerca de 27 s enquanto um rastreador seguia o olhar; quanto mais simples o quadro e mais curta a cena, mais os olhares se juntam no mesmo ponto, e esse olhar junto acompanha o gosto pelo anúncio e a lembrança dele dois a três dias depois.

## 1. A pergunta (introdução)

- **Contexto que o artigo dá:** vídeo curto (menos de 60 s) é a forma dominante de comunicação de marketing nas redes, e o gasto com anúncio em vídeo nos EUA passa de US$ 60 bilhões em 2024 e chega a US$ 72 bilhões em 2025 (números de terceiros que o artigo cita: eMarketer e IAB). Peças premiadas por criatividade nem sempre funcionam, e o teste A/B com cliques ou tempo de vídeo não diz o que, dentro do vídeo, prendeu ou soltou a atenção.
- **O buraco que os autores apontam:** os estudos anteriores medem o efeito depois de assistir, no agregado, ou em imagem parada; sobre complexidade visual os achados se contradizem; ninguém, até onde eles sabem, juntou visão computacional quadro a quadro com rastreio do olhar a 30 quadros por segundo.
- **O que fazem:** medem duas variáveis do vídeo, complexidade visual (quanta informação o quadro tem) e cortes de cena (que fixam quanto dura cada cena), e a sincronia de atenção dos espectadores, em três escalas: o vídeo inteiro, a cena e o quadro. Depois ligam a sincronia à imersão na narrativa, ao gosto pelo anúncio e ao reconhecimento.
- **A recomendação que já anunciam na introdução:** o elemento mais importante no centro, sem distração, cedo, por pelo menos um segundo sem interrupção, no começo do vídeo ou de uma cena nova; cada cena simples, e várias cenas diferentes em sequência para manter a novidade.

## 2. Revisão e hipóteses

- **Imersão e foco:** imersão narrativa é o estado de quem se perde na história e esquece o entorno; ela prevê intenção de compra e boa imagem de marca, e o foco da atenção é condição para ela. O autorrelato mede isso só no fim, de uma vez; o foco varia ao longo do vídeo e fica mais concentrado nos momentos de suspense.
- **Sincronia de atenção:** é o quanto os pontos de olhar de um grupo coincidem num mesmo instante. Os autores a apresentam como medida validada de foco durante o vídeo; ela depende de montagem e enquadramento bem feitos, é maior em filme narrativo do que em vídeo de natureza ou stop-motion, e maior em trecho profissional de Hollywood do que em vídeo amador.
- **H1:** a sincronia de atenção aumenta o gosto pelo anúncio e o reconhecimento.
- **Complexidade visual:** em imagem parada, mais complexidade leva a mais fixações e mais longas, porque o olho explora. No vídeo, o tempo de cada quadro é curto; explorar quadro carregado divide a atenção, já que não se atende a vários objetos ao mesmo tempo. **H2:** menos complexidade visual aumenta a sincronia. O efeito deve vir com atraso de uma fração de segundo, o tempo de o cérebro processar e mover o olho.
- **Cortes:** quase ninguém percebe o corte de forma consciente, mas ele orienta o olhar: a cena nova provoca uma resposta de orientação, e o olho de todos vai para a parte mais saliente. Com o tempo dentro da mesma cena, o ganho de informação por olhar o mesmo lugar cai e o olhar se espalha. **H3:** cortes aumentam a sincronia.

## 3. Método, passo a passo

1. **Desenho com medidas repetidas, em três etapas.** Etapa 1: cada pessoa viu os 42 vídeos seguidos, em ordem aleatória. Etapa 2: os mesmos vídeos, em outra ordem aleatória, com perguntas a cada bloco de 6. O olhar foi gravado nas etapas 1 e 2. Etapa 3: questionário de reconhecimento enviado 48 h depois e respondido em casa, de 48 a 72 h após o laboratório.
2. **Estímulos.** Anúncios de utilidade pública do Ministério da Saúde, Bem-Estar e Esporte da Holanda (dirigir bêbado, solidão de idosos, pagar impostos, entre outros), de 25 a 30 s, a maioria com 27 s, em cor e com som, num monitor a cerca de 70 cm, pelo programa Presentation 18.0. Tudo em holandês; o artigo traduz para o inglês.
3. **Participantes.** 30 holandeses (18 homens, 12 mulheres), de 18 a 59 anos, média de 31, recrutados com escolaridades e idades variadas para se parecer com a população. Cada um viu cada vídeo duas vezes: 2.520 sessões de visualização, quase 20 h de rastreio e 32.392 quadros de vídeo.
4. **Rastreio do olhar.** Rastreador Tobii Pro Nano preso à tela, a 60 Hz (1.800 amostras num vídeo de 30 s); luz da sala constante; calibração a cada bloco; gravação sem contato.
5. **Medida de sincronia (do grupo).** Para cada quadro, a distância padrão dos pontos de olhar de todos até o centro médio deles, em x e y (biblioteca Python Point Patterns); quanto menor a distância, maior a sincronia.
6. **Medida de sincronia (de cada pessoa).** Para ligar o olhar às respostas individuais, uma correlação entre sujeitos (ISC): a correlação do ponto de olhar de cada pessoa com o centro médio do grupo, quadro a quadro.
7. **Complexidade visual.** Os autores descartam medidas de baixo nível isoladas (densidade de bordas, contraste, tamanho do JPEG) e usam um mapa de saliência, apoiado na teoria da integração de traços: o modelo pré-treinado Deep Gaze II gera, para cada quadro, um mapa de calor do que chama o olho. A complexidade é a distância padrão dos 5% de pontos mais salientes até o centro deles (saliência espalhada é quadro complexo; concentrada, quadro simples), normalizada para 1920 × 1080. O código está no apêndice web A.
8. **Detecção dos cortes.** O Microsoft Azure Video Indexer acha as mudanças bruscas entre quadros (por exemplo, de luminância) e devolve onde estão os cortes e quanto dura cada cena. Daí saem a duração média de cena por vídeo e o tempo desde o último corte em cada ponto. No modelo de série temporal, o corte é uma variável indicadora que vale de 0 a 0,66 s depois dele, porque perceber, disparar e completar um movimento de olho leva em geral até dois terços de segundo.
9. **Duração das cenas.** No conjunto, a maior parte das cenas fica em torno de 2 s: mediana de 2,12 e intervalo interquartil de 1,5 a 3 s (as estatísticas por vídeo estão no apêndice web B, não lido). A análise por cena usa 431 cenas.
10. **Autorrelato.** Na etapa 2, depois de cada bloco de 6, três telas de cada vídeo (2 s cada) e duas frases de um item só, de 1 ("discordo totalmente") a 9 ("concordo totalmente"): imersão ("me senti completamente imerso") e gosto ("gostei de ver este vídeo"). Na etapa 3, pelo Qualtrics, as mesmas três telas por vídeo, em ordem aleatória, e a frase de reconhecimento ("lembro bem do conteúdo deste vídeo").
11. **Análise quadro a quadro.** Modelo autorregressivo de defasagens distribuídas (ARDL) por vídeo: a sincronia de cada quadro explicada pelos valores passados dela, pela complexidade padronizada e pelo indicador de corte, com as defasagens. Dele saem três efeitos: o de curto prazo (no mesmo quadro), o atrasado em cada defasagem (e o acumulado até ela, o "interino") e o de longo prazo (o acumulado total). Ordens escolhidas pelo AIC, de 2 a 5 defasagens; estacionariedade por Dickey-Fuller aumentado (apêndice C); resíduos por Durbin-Watson (apêndice D); pacote ARDL do R, com erro padrão pelo método delta. Os efeitos de curto e longo prazo dos 42 vídeos se juntam numa meta-análise de efeitos aleatórios (pacote metafor), com metarregressão para a heterogeneidade. Os autores chamam o arranjo de quase experimental: o vídeo estava pronto antes, então o olhar não tem como mudar o vídeo.
12. **Análise de autorrelato.** Modelos multinível com intercepto aleatório por pessoa, ligando a ISC de cada pessoa em cada vídeo às três respostas: 30 × 42 = 1.260 observações.

## 4. Resultados

- **Validação:** quem tem o olhar mais junto do grupo diz ter ficado mais imerso.
- **H1, aceita:** a ISC mais alta acompanha mais gosto pelo anúncio e melhor reconhecimento depois de 48 a 72 h. Na nota 1, a imersão relatada também acompanha o gosto e o reconhecimento.
- **Por vídeo (H2 e H3, aceitas; Tabela 2):** com a mediana de cada vídeo, vídeo de cenas mais curtas tem mais sincronia, e vídeo mais complexo, menos; as duas variáveis não interagem. Na nota 2, nenhum efeito quadrático passa de 0,05.
- **Por cena (Tabela 3, Figura 3):** o mesmo resultado nas 431 cenas, num modelo multinível com intercepto por vídeo. Na conta dos autores, uma cena 1 desvio padrão mais complexa tem 12% menos sincronia, e cada segundo a mais de cena tira uns 5%. Na nota 3, o termo quadrático da duração sai significativo, mas some quando se tiram uns poucos valores extremos; duração e tipo de plano não interagem.
- **Tipo de plano (exploratório, Tabela 3):** o Video Indexer classificou cada cena pela distância entre câmera e rosto. Plano fechado e plano médio de uma pessoa têm mais sincronia do que cena sem ninguém; o plano médio numa cena complexa tem menos, o que os autores atribuem à disputa entre a pessoa e o fundo.
- **Quadro a quadro:** no mesmo quadro (0,03 s), a complexidade não tem efeito significativo e o corte tem. No longo prazo, os dois têm: +1 desvio padrão de complexidade baixa a sincronia em 26,4%, e um corte a sobe em 40,2%, sobre a mediana. O efeito de longo prazo é cerca de cem vezes o de curto prazo, porque o cérebro demora a responder. Na nota 4, os efeitos resistem a um controle defasado de complexidade do áudio (apêndice E) e a outra forma de medir a sincronia (apêndice F).
- **O tempo do efeito (Figura 4):** nos 20 quadros depois da mudança (dois terços de segundo a 30 quadros por segundo), a complexidade leva a sincronia a um vale perto de dois terços de segundo depois, e daí a curva assenta no efeito de longo prazo; o corte leva a um pico no mesmo intervalo. Os detalhes de cada vídeo estão no apêndice web G.
- **Heterogeneidade (exploratório):** os efeitos de longo prazo variam entre vídeos. O da complexidade não depende da duração mediana das cenas; o de cada corte depende: é mais forte nos vídeos de cenas mais longas, com menos cortes, o que os autores leem como retorno decrescente do corte, talvez por habituação.
- **Idade (exploratório, apêndice H):** divididos pela mediana em 15 mais novos (média de 20 anos) e 15 mais velhos (média de 41), os resultados do ARDL se repetem nos dois grupos, e as curvas de sincronia andam juntas. Os mais novos têm sincronia mais alta e mais oscilante (cerca de 10% de diferença), e a distância entre os grupos cresce nos vídeos mais excitantes, pela escala SAM; a campanha HEY, de saúde mental para 16 a 25 anos (vídeos 30 e 31), sai melhor com os mais novos.

### De onde sai cada número

| Número | O que mede | Onde no artigo |
|---|---|---|
| 42 vídeos; 25 a 30 s, a maioria 27 s | estímulos | Study design, "Videos" |
| 30 pessoas; 18 homens e 12 mulheres; 18 a 59 anos, média 31 | amostra | "Participants" |
| 2.520 visualizações; quase 20 h; 32.392 quadros | volume de dados | "Participants" |
| 60 Hz; 1.800 amostras em 30 s | rastreio | "Eye-tracking data" |
| 5% mais salientes; 1920 × 1080 | complexidade | "Visual complexity" |
| indicador de 0 a 0,66 s após o corte | corte no modelo | "Scene cuts" |
| mediana 2,12; IQR 1,5 a 3 s | duração das cenas | "Scene cuts" |
| 2 a 5 defasagens, pelo AIC | ordem do ARDL | Methodology and analysis |
| 1.260 observações | modelos de autorrelato | "Relating attentional synchrony to self-reported measures" |
| inclinação 2,05; IC 95% [1,302; 2,803] | ISC → imersão | Results, "Validating…" |
| 0,82; IC [0,029; 1,609] | ISC → gosto | Results, "Relating… to ad effectiveness" |
| 0,88; IC [0,246; 1,524] | ISC → reconhecimento após 48 a 72 h | idem |
| 0,643; IC [0,598; 0,688] | imersão → gosto | nota 1 |
| 0,359; IC [0,315; 0,403] | imersão → reconhecimento | nota 1 |
| −4,34; IC [−7,37; −1,31]; p = 0,006 | duração média de cena → sincronia, por vídeo | "Aggregate effects per video", Tabela 2 |
| −12,21; IC [−21,80; −2,62]; p = 0,014 | complexidade → sincronia, por vídeo | idem |
| p = 0,90 | interação duração × complexidade, por vídeo | idem |
| p = 0,356 (duração); p = 0,055 (complexidade) | termos quadráticos, por vídeo | nota 2 |
| 431 cenas | unidades da análise por cena | "Aggregate effects per scene" |
| −4,44; IC [−6,29; −2,59]; p < 0,001 | duração → sincronia, por cena | idem, Tabela 3 |
| −11,76; IC [−19,62; −3,90]; p = 0,003 | complexidade → sincronia, por cena | idem |
| −0,60; IC [−3,12; 1,92]; p = 0,639 | interação, por cena | idem |
| −12% por 1 DP de complexidade; cerca de −5% por segundo de cena | leitura dos autores sobre a linha de base | idem |
| p = 0,367 (complexidade); p = 0,024 (duração, some sem os extremos) | termos quadráticos, por cena | nota 3 |
| aberto 110; médio 143; fechado 55; muito fechado 9 (somado ao fechado); sem pessoa 114 | cenas por tipo de plano | "Exploratory moderation of shot type" |
| 18,6; IC [6,14; 31,11]; p = 0,004 | plano fechado vs. sem pessoa | idem, Tabela 3 |
| 9,77; IC [0,36; 19,18]; p = 0,042 | plano médio vs. sem pessoa | idem |
| −17,84; IC [−28,17; −7,51]; p = 0,001 | complexidade × plano médio | idem |
| −1,62 × 10⁻⁵; IC [−3,90 × 10⁻⁵; 0,67 × 10⁻⁵]; p = 0,163 | complexidade, curto prazo (meta-análise) | "Dynamic effects per frame" |
| 4,07 × 10⁻⁵; IC [1,01 × 10⁻⁵; 7,13 × 10⁻⁵]; p = 0,009 | corte, curto prazo | idem |
| −1,22 × 10⁻³; IC [−1,38 × 10⁻³; −1,05 × 10⁻³]; p < 0,001 | complexidade, longo prazo | idem |
| 1,85 × 10⁻³; IC [1,42 × 10⁻³; 2,28 × 10⁻³]; p < 0,001 | corte, longo prazo | idem |
| −26,4%; IC [22,8%; 30,1%] | complexidade +1 DP, longo prazo, sobre a mediana | idem |
| +40,2%; IC [30,9%; 49,6%] | corte, longo prazo, sobre a mediana | idem |
| 20 quadros, cerca de dois terços de segundo | janela do efeito interino; vale e pico | "Aggregated interim multipliers", Figura 4 |
| Q(41) = 72,96, p = 0,002 (complexidade); Q(41) = 87,60, p < 0,001 (corte) | heterogeneidade entre vídeos | "Exploratory moderation analysis…" |
| QM(1) = 0,61, p = 0,44 | duração de cena modera a complexidade? não | idem |
| QM(1) = 8,02, p = 0,005, R² = 33,69% | duração de cena modera o corte? sim, positivo | idem |
| 15 e 15; médias de 20 e 41 anos | subgrupos de idade | "Exploratory analysis of age subgroups" |
| r = 0,52, p < 0,001 | curvas dos dois grupos | idem |
| diferença de 0,0005, t(41) = 4,63, p < 0,001; cerca de 10% | sincronia, mais novos acima | idem |
| diferença de 0,0003 no MAD, t(41) = 2,08, p = 0,04 | oscilação, mais novos acima | idem |
| R = 0,42, t(40) = 2,89, p = 0,006 | excitação (SAM) × diferença entre grupos | idem |

## 5. Discussão

- **O que os autores concluem para a teoria:** em vídeo, a complexidade age ao contrário do que age na imagem parada. Na pintura, o interesse aparece como exploração; no vídeo, como olhar junto, seguindo a narrativa que o diretor monta. A riqueza do vídeo está na troca de cenas ao longo do tempo, e não em mostrar tudo num quadro: cada quadro simples, a soma rica.
- **O corte e a indústria:** o resultado conversa com a onda de vídeo curto, de conteúdo agitado, de planos cada vez mais curtos e com o *jump cut* dos criadores do YouTube, que os autores descrevem como prática de tentativa e erro. Ressalvas que eles mesmos põem: não acharam efeito não linear forte, mas o retorno de cada corte cai; há um teto, porque processar leva tempo, e a amostra não tem cena com menos de um segundo; e o visual simples ainda precisa ser vivo o bastante para se destacar.
- **Para quem faz o vídeo:** o princípio "curto e simples"; preferir o plano fechado de pessoa e evitar o plano médio em cena já carregada; não mostrar muita coisa ao mesmo tempo, porque a mensagem ou a marca pode passar sem ser vista. O efeito do corte chega ao pico uns 0,66 s depois dele, então o conteúdo importante rende mais no começo da cena nova do que no fim, onde muita peça o põe; espaçar os elementos-chave e os efeitos, por causa do atraso da resposta; o principal no centro, sem distração, por pelo menos um segundo inteiro.
- **Para medir:** a sincronia serve para achar que trecho do anúncio rende pouco, em pré-teste, antes de gastar mídia; a medida de complexidade por visão computacional dá retorno rápido e automático e pode guiar a criação por IA; os autores dizem que a resposta biológica de gente ainda informa mais do que os traços do vídeo sozinhos, e sugerem combinar autorrelato, biometria e visão computacional.

## 6. O caso (Tempo Team, com a Alpha.One)

- Agência holandesa de trabalho temporário, campanha no YouTube para jovens adultos sobre satisfação no trabalho, avaliada antes no Junbi, o sistema da Alpha.One que dá, quadro a quadro, notas de facilidade de processamento, de destaque frente ao entorno e de atenção à marca.
- A equipe pôs a marca no centro e cortou elementos visuais irrelevantes.
- Pelo Brand Lift do YouTube: 42% de aumento relativo de marca; preferência +3% e consideração +2%, o dobro da média da categoria; 66% de visualização completa num vídeo de 32 s; custo por visualização de € 0,018; prêmio YouTube Grand Prix. Os autores tiram dali também uma condição: o anúncio tem de ser vivo o bastante para se destacar do entorno, e o teste rápido coube no fluxo de criação melhor do que grupo focal ou estudo de neuromarketing.

## 7. Limites declarados

- Só anúncios de utilidade pública de até 30 s: podem não cobrir toda a faixa de complexidade e de duração de cena; faltam anúncio longo, vídeo narrativo e conteúdo muito estilizado ou de montagem muito rápida.
- A complexidade foi medida pela distribuição espacial da saliência; outras medidas (cor, movimento, detecção de objetos, modelos treinados com notas humanas) ficam para depois.
- O arranjo quase experimental pode não controlar traços do vídeo não medidos que andem junto com complexidade e atenção.
- O áudio (fala, música) e a interação entre som e imagem ficaram fora da análise principal.
- Só traços de baixo para cima (enquadramento, corte); os de cima para baixo (objetivo e interesse de quem vê, a narrativa, a estrutura do enredo) não foram estudados.
- Foco é necessário para a imersão, mas não suficiente (empatia, compreensão da história contam); excitação emocional por pele, batimento ou pupila não foi medida.
- Disponibilidade de dados: "Not Applicable".

## Citações

Copiadas do texto extraído; os espaços finos e não separáveis do original estão como espaço comum.

- "Overall, most scene durations cluster around 2 s (median = 2.12, IQR = 1.5 to 3 s)."
- "the effect of scene cuts on attentional focus peaks approximately 0.66 s after the cut"
- "Scenes of less than one second are not used in our sample of videos"

## Lacuna

O texto lido não traz o conteúdo das Tabelas 1 a 3 nem os apêndices (estatística de duração de cena por vídeo, código, resultados por vídeo), então os coeficientes por tipo de plano e as médias e desvios das variáveis ficam só no que a prosa repete. A mediana de 2,12 vem sem unidade explícita e sem dizer se é sobre as 431 cenas. O artigo não diz quantos cortes tem cada vídeo, nem se os cortes achados pelo Video Indexer foram conferidos à mão ou quanto ele erra; não testa movimento de câmera (dolly, pan, zoom) dentro da cena, só corte e tipo de plano; e não estuda vídeo vertical nem a tela de celular, só monitor a 70 cm, com público holandês.
