---
titulo: "Rules of Machine Learning: Best Practices for ML Engineering"
tipo: artigo
autor: "Martin Zinkevich"
url: "https://developers.google.com/machine-learning/guides/rules-of-ml"
publicado_em: 2025-08-25
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [ml-engineering, best-practices, heuristics, metrics, baseline, training-serving-skew, feature-engineering, launch-decisions, proxy-objective, monitoring]
licenca: "CC BY 4.0, no rodapé da página"
---

# Zinkevich, "Rules of Machine Learning": 43 regras de engenharia de ML

Ficha em palavras próprias. Martin Zinkevich, guia publicado em Machine Learning, Google for Developers; o rodapé traz última atualização em 25/8/2025 (UTC), e a página não informa a data original. Área: engenharia de sistemas de aprendizado de máquina. Guia de praticante, para quem tem noção básica de ML, escrito como um manual de estilo, à maneira do Google C++ Style Guide. Sem estudo por trás: os casos vêm de produtos do Google (YouTube, Google Play, Google Plus), e o autor assume os erros e as "unpopular opinions" como dele.

## Os termos do guia

- **Instância:** a coisa sobre a qual se quer prever.
- **Rótulo:** a resposta da tarefa, a produzida pelo sistema ou a certa, dada no treino.
- **Atributo (feature):** propriedade da instância usada na predição.
- **Coluna de atributos (feature column):** conjunto de atributos relacionados; termo próprio do Google, chamado de "namespace" no sistema VW ou de campo.
- **Exemplo:** instância com atributos e rótulo.
- **Modelo:** representação estatística da tarefa.
- **Métrica:** número que importa, otimizado ou não.
- **Objetivo:** a métrica que o algoritmo tenta otimizar.
- **Pipeline:** a infraestrutura em volta do algoritmo: coleta, arquivos de treino, treino, exportação.
- **Taxa de cliques:** percentual de visitantes que clicam no link de um anúncio.

## A tese geral

"do machine learning like the great engineer you are, not like the great machine learning expert you aren't." A maior parte dos problemas é de engenharia, e a maior parte dos ganhos vem de bons atributos, mais do que de algoritmos sofisticados. A receita: pipeline sólido de ponta a ponta, objetivo razoável, atributos de bom senso de jeito simples, pipeline mantido sólido. Ela funciona por muito tempo. Só se muda quando os truques simples acabam, porque complexidade atrasa as próximas entregas.

## Antes de usar ML (regras 1 a 3)

- **Regra 1, não ter medo de lançar sem ML.** ML pede dados. Usar dados de outro problema e ajustar costuma render menos que heurísticas básicas. Na comparação do autor, se o ML daria 100% de ganho, uma heurística leva a 50% do caminho. Exemplos: taxa ou número de instalações para ordenar apps; barrar quem já mandou spam; ordenar contatos pelo uso recente ou alfabeto; edição humana. Sem necessidade absoluta, não usar ML até ter dados.
- **Regra 2, primeiro desenhar e implementar métricas.** Registrar o máximo possível no sistema atual antes de definir o que o ML fará. Motivos: a permissão dos usuários é mais fácil cedo; dados históricos ficam prontos para preocupações futuras; instrumentar desde o início evita garimpar logs; e se vê o que muda e o que não muda, como um indicador de usuários ativos por dia que não se move com mudanças drásticas. A orientação é ser generoso: problema percebido ou mudança animadora, adicionar métrica. Um arcabouço de experimentos, com usuários em grupos e estatísticas por experimento, é importante.
- **Regra 3, preferir ML a heurística complexa.** A heurística simples põe o produto na rua, e a complexa fica impossível de manter. Com dados e uma ideia do objetivo, migrar para ML: atualizar um modelo aprendido é mais fácil.

## Fase I: o primeiro pipeline (regras 4 a 15)

**Infraestrutura**

- **Regra 4, primeiro modelo simples, infraestrutura certa.** O primeiro modelo dá o maior ganho, e os problemas de infraestrutura serão mais numerosos que o esperado. É preciso decidir como os exemplos chegam, o que é "bom" e "ruim", como integrar (ao vivo ou pré-calculado em tabela). Atributos simples facilitam conferir que eles chegam certos ao algoritmo, que os pesos fazem sentido e que chegam certos ao servidor. O modelo simples dá métricas e comportamento de referência para testar os mais complexos. Há equipes que buscam um primeiro lançamento "neutro", sem priorizar ganho de ML, para não se distrair.
- **Regra 5, testar a infraestrutura à parte do ML.** Encapsular a parte que aprende. Testar a entrada (colunas preenchidas, inspeção manual onde a privacidade permite, comparação com estatísticas de outro processamento) e a saída (mesma pontuação no ambiente de treino e no de servir).
- **Regra 6, cuidado com dados descartados ao copiar pipeline.** O What's Hot do Google Plus descartava posts antigos, e a cópia para o Stream, onde eles importam, herdou o descarte. Outro padrão: registrar só o que o usuário viu, o que elimina os negativos se o interesse é entender o que ele não viu.
- **Regra 7, heurísticas viram atributos ou ficam por fora.** O problema em geral já tem regras, e elas guardam intuição. Quatro usos: pré-processar (remetente em lista de bloqueio, bloquear sem reaprender), criar atributo com a pontuação crua, separar as entradas brutas da heurística, modificar o rótulo (multiplicar downloads pela média de estrelas). Cuidar da complexidade adicionada.

**Monitoramento**

- **Regra 8, saber a exigência de atualização.** Quanto cai com modelo de um dia, uma semana, um trimestre? Isso define a prioridade do monitoramento. Sistemas de anúncios atualizam todo dia; o modelo do Play Search parado pode ter efeito negativo em menos de um mês; modelos sem identificador de post podem exportar raramente.
- **Regra 9, detectar problemas antes de exportar.** Conferir desempenho em dados separados, e muitas equipes olham a AUC (área sob a curva ROC) antes de exportar. Com dúvida sobre os dados, não exportar.
- **Regra 10, vigiar falhas silenciosas.** Uma tabela parada faz o sistema decair aos poucos, sem quebrar. Caso do Play: tabela parada por seis meses, cuja atualização sozinha rendeu 2% na taxa de instalação. Uma coluna pode cair de 90% para 60% dos exemplos. Acompanhar estatísticas e inspecionar à mão de vez em quando.
- **Regra 11, dono e documentação para cada coluna.** Saber quem criou ou mantém, o que é, de onde vem e como deveria ajudar.

**Primeiro objetivo**

- **Regra 12, não pensar demais no objetivo direto.** No início, tudo sobe junto, mesmo o que não se otimiza. Sem confundir objetivo com saúde do sistema: se a métrica otimizada sobe e se decide não lançar, é hora de rever o objetivo.
- **Regra 13, métrica simples, observável e atribuível.** Muitas vezes não se sabe o objetivo verdadeiro, e pode nem existir um. O objetivo de ML deve ser fácil de medir e substituto do verdadeiro, e pode haver uma camada de política por cima. O mais fácil é comportamento direto atribuível ao sistema (clicou, baixou, encaminhou, avaliou, marcou como spam). Efeitos indiretos (voltou no dia seguinte, tempo de visita, ativos por dia) são ótimas métricas para testes A/B e lançamento, e ruins como primeiro objetivo. Satisfação e bem-estar são importantes e muito difíceis de medir: usar substitutos, e o juízo humano para ligar o objetivo ao produto e ao negócio.
- **Regra 14, modelo interpretável facilita a depuração.** Regressões linear, logística e de Poisson têm base probabilística, e cada predição vale como probabilidade ou valor esperado, o que permite comparar treino com produção e achar problemas. Elas têm calibração: em certos subconjuntos, a predição média iguala o rótulo médio, supondo sem regularização e com convergência. Ao escolher o modelo, porém, a decisão pesa mais que a verossimilhança.
- **Regra 15, separar filtro de spam e ordenação por qualidade numa camada de política.** "Quality ranking is a fine art, but spam filtering is a war." Os sinais de qualidade ficam óbvios e são explorados; a ordenação deve focar conteúdo de boa-fé, e o filtro muda sempre, com regras óbvias, atualização diária ou mais rápida e peso na reputação do autor. É prática padrão tirar spam do treino do classificador de qualidade.

## Fase II: engenharia de atributos (regras 16 a 37)

Com o sistema funcionando de ponta a ponta, há muito ganho fácil: juntar muitos atributos de forma intuitiva, com todas as métricas ainda subindo, muitos lançamentos e bom momento para trazer engenheiros.

**Atributos**

- **Regra 16, planejar lançar e iterar.** O modelo atual não será o último; muitas equipes lançam um por trimestre ou mais, durante anos. Razões: atributos novos, regularização e combinações, ajuste do objetivo. Pensar na facilidade de mexer em atributos e duplicar o pipeline.
- **Regra 17, começar por atributos observados diretamente, sem atributos aprendidos.** Sistema externo tem objetivo próprio, envelhece ou muda de significado. Modelos fatorados e profundos não são convexos, o que dificulta saber se o efeito de uma mudança é real. O autor reconhece que é ponto controverso.
- **Regra 18, atributos de conteúdo que generalizam entre contextos.** Estatísticas de outra superfície permitem promover o novo sem dado no contexto que se otimiza, como YouTube Watch Next usando visualizações da busca.
- **Regra 19, atributos muito específicos quando der.** Com muito dado, é mais simples aprender milhões de atributos simples. Grupos em que cada um cobre pouco valem se a cobertura total passa de 90%; a regularização elimina os que têm poucos exemplos.
- **Regra 20, combinar atributos de forma compreensível.** Discretização (faixas de idade; quantis básicos dão a maior parte do efeito) e cruzamentos (cruzar três ou mais colunas pede muitíssimo dado, e colunas muito grandes podem sobreajustar). Em texto: produto escalar, que conta palavras em comum, ou interseção.
- **Regra 21, pesos aprendíveis são cerca de proporcionais aos dados.** Em ordenação de busca, o autor escala assim:

| Exemplos | Abordagem |
|---|---|
| 1.000 | Produto escalar, TF-IDF e meia dúzia de atributos feitos à mão: cerca de uma dúzia de atributos |
| 1 milhão | Interseção de colunas com regularização e talvez seleção; o texto dá também 10 milhões de exemplos para talvez 100 mil atributos |
| Bilhões ou centenas de bilhões | Cruzamentos com seleção e regularização; 1 bilhão de exemplos para 10 milhões de atributos |

- **Regra 22, limpar atributos sem uso.** Atributo parado é dívida técnica. Pensar em cobertura: personalização em só 8% dos usuários rende pouco, mas um atributo em 1% dos dados com 90% de positivos é ótimo.

**Análise humana do sistema**

- **Regra 23, você não é o usuário típico.** A equipe está perto demais e tem viés de confirmação; o tempo dela vale caro (nove engenheiros numa reunião de uma hora, contra rótulos humanos contratados). Testar com leigos pagos, em plataforma de crowdsourcing, ou experimento ao vivo; personas cedo e testes de usabilidade depois.
- **Regra 24, medir a diferença entre modelos.** Antes de qualquer usuário, comparar o resultado novo com o de produção (diferença simétrica ponderada pela posição). Diferença pequena dispensa experimento, e grande pede garantir que a mudança é boa. Conferir a estabilidade: o modelo comparado consigo deve dar perto de zero.
- **Regra 25, o desempenho útil vale mais que o poder preditivo.** O que importa é o uso da predição: a ordenação final, ou a precisão do que passa pelo corte de spam. Se a perda logarítmica melhora e o sistema piora, procurar outro atributo; isso virando frequente, rever o objetivo.
- **Regra 26, procurar padrões nos erros medidos.** Um erro que o sistema reconhece como erro é o que ele tentará corrigir se ganhar um atributo para isso. Atributo criado sobre o que o sistema não vê como erro é ignorado: o caso dos apps de piada, que as pessoas instalam ao buscar jogos grátis. Não ser específico demais: em vez de adivinhar o que é um post longo, dar uma dúzia de atributos de tamanho.
- **Regra 27, quantificar o comportamento indesejado.** Queixa vira número, por exemplo com avaliadores humanos marcando apps de piada, e daí atributo, objetivo ou métrica. Regra geral: "measure first, optimize second".
- **Regra 28, comportamento igual no curto prazo não garante o mesmo no longo.** Um sistema que só olha o histórico de cada documento por consulta empata em testes, e nenhum app novo aparece. Só treinar com dados obtidos com o modelo ao vivo mostraria isso, o que é muito difícil.

**Diferença entre treino e produção (training-serving skew)**

É a diferença de desempenho entre treinar e servir, causada por tratamento diferente dos dados, por mudança nos dados ou por laço de realimentação. O autor diz ter visto isso prejudicar sistemas do Google, e recomenda monitorar explicitamente.

- **Regra 29, registrar os atributos usados ao servir e treinar com eles.** Mesmo numa fração pequena, para conferir consistência. A home do YouTube mudou para isso, com melhora significativa de qualidade e código mais simples.
- **Regra 30, ponderar a amostra pela importância, sem descartar ao acaso.** Pegar os arquivos 1 a 12 e ignorar 13 a 99 é erro. Se o exemplo X tem 30% de chance de amostragem, recebe peso 10/3, e a calibração se mantém. Só o que nunca foi mostrado ao usuário pode sair.
- **Regra 31, tabela unida no treino e ao servir pode mudar no meio.** O caminho é registrar os atributos ao servir; com mudança lenta, uma foto horária ou diária chega perto, sem resolver por completo.
- **Regra 32, reusar código entre treino e produção.** Lote e processamento online diferem, mas um objeto comum e legível, com um método único de conversão, elimina uma fonte de diferença. Evitar duas linguagens.
- **Regra 33, modelo com dados até 5 de janeiro se testa com dados a partir de 6.** Espera-se um desempenho menor, sem queda radical. Por efeitos diários, a média de cliques pode variar, e a AUC deve ficar razoavelmente próxima.
- **Regra 34, em filtragem binária, sacrificar um pouco de desempenho por dados limpos.** Exemplos bloqueados não chegam ao usuário, então aprender do que passou introduz viés de amostragem. Com filtro que bloqueia 75% dos negativos, separar 1% do tráfego como reserva e mostrar tudo o que cai nele: passa a bloquear ao menos 74%, e a reserva vira treino. Com bloqueio de 95% ou mais, isso fica menos viável; para medir desempenho, serve uma amostra de 0,1% ou 0,001%. Na frase do autor, "Ten thousand examples is enough to estimate performance quite accurately."
- **Regra 35, viés inerente à ordenação.** Mudar a ordenação muda os dados futuros. Saídas que favorecem o que o modelo já viu: mais regularização nos atributos que cobrem muitas consultas (o contrário do conselho usual), só pesos positivos, nada de atributo só de documento.
- **Regra 36, evitar realimentação com atributos de posição.** A posição aumenta o clique. Treinar com posição e servir sem ela ou com valor padrão, mantendo-a separada do resto do modelo, sem cruzar com atributos de documento.
- **Regra 37, medir a diferença em partes.** Treino contra dados separados: sempre existe e nem sempre é ruim. Dados separados contra dados do dia seguinte: sempre existe; ajustar a regularização para o dia seguinte, e uma queda grande pode indicar atributo sensível ao tempo. Dia seguinte contra dados ao vivo: o mesmo exemplo deve dar o mesmo resultado, e diferença aí provavelmente é erro de engenharia.

## Fase III: crescimento lento e modelos complexos (regras 38 a 43)

Sinais da fase: ganhos mensais menores e métricas em troca, umas sobem e outras caem. O autor avisa que estas regras são mais especulativas, e cada equipe acha o próprio caminho.

- **Regra 38, sem atributos novos se o problema é objetivo desalinhado.** Se as metas do produto não cabem no objetivo do algoritmo, mudar um dos dois.
- **Regra 39, decisão de lançamento é substituto de metas de longo prazo.** Alice reduz a perda e sobe a instalação, mas a reunião de lançamento vê 5% a menos de usuários ativos por dia, e o modelo não sai. As métricas de teste A/B substituem metas como satisfazer usuários e dar lucro, que substituem ter um produto útil e uma empresa próspera em cinco anos. Decisão fácil é só quando tudo melhora ou não piora; uma heurística que vence em tudo deve ser escolhida. Não há ordem explícita entre as métricas: entre A (1 milhão de ativos por dia e US$ 4 milhões por dia) e B (2 milhões e US$ 2 milhões), quem está em A tende a não ir para B e vice-versa, porque a previsão pode falhar e cada métrica cobre um risco. Aprendizado multiobjetivo começa a tratar disso, mas nem toda métrica vira objetivo, e prever o sucesso de um site inteiro é "AI-complete".
- **Regra 40, ensembles simples.** Ensemble é um modelo que combina as notas de outros. Cada modelo é só ensemble ou só base com atributos, sem misturar. O ensemble deve ser simples, com modelos de base semanticamente interpretáveis, e aumentar a nota de uma base não deve reduzir a dele.
- **Regra 41, no platô, buscar fontes de informação qualitativamente novas.** Sem lançamento acima de 1% por trimestres: histórico do usuário, outros produtos, wikidata, grafo interno, aprendizado profundo. Rever a expectativa de retorno e pesar benefício contra complexidade.
- **Regra 42, diversidade, personalização e relevância se correlacionam menos com popularidade do que se pensa.** Medir cliques, tempo e compartilhamentos mede popularidade, e o comum é difícil de bater: esses atributos recebem menos peso que o esperado, ou até sinal contrário. Dá para usar pós-processamento e, se as metas longas sobem, declarar o valor delas.
- **Regra 43, amigos se repetem entre produtos, interesses nem tanto.** Modelos de proximidade entre pessoas migraram bem de um produto a outro; atributos de personalização, não. Às vezes funciona usar dado bruto de um produto para prever outro, e saber que existe histórico lá já ajuda.

## Limites e ressalvas do autor

- Os 100% e 50% da Regra 1 vêm sem medição que os apoie.
- As regras da Fase III são mais especulativas.
- A Regra 17 é assumidamente controversa.
- A Regra 21 é ponto de partida: a teoria do aprendizado estatístico raramente dá limites justos.
- O apêndice registra que o Google Plus, fonte de vários exemplos, fechou as contas pessoais em 2019 e deu lugar ao Google Currents para empresas em 6/7/2020.

## Tudo o mais que ensina

- O guia se divide em quatro partes: se é hora de construir um sistema de ML; o primeiro pipeline; iterar com atributos, avaliar e tratar a diferença entre treino e produção; e o platô.
- Mais um caso da Regra 6: o pipeline do Play Apps Home misturou exemplos da página de Games sem atributo que indicasse a origem.
- Alertas devem ser acionáveis, e um problema em modelo não exportado pede e-mail, enquanto um em modelo no ar pode pedir acionar alguém.
- Filtrar spam em resultados de busca provavelmente deve ser mais agressivo que em e-mail, nas palavras do autor (Regra 15).
- Conteúdo "racy" se trata à parte da ordenação por qualidade.
- A Regra 18 fica fora da personalização: primeiro descobrir se o conteúdo agrada no contexto, depois a quem agrada mais ou menos.
- Personas: a equipe toda masculina pode desenhar uma usuária de 35 anos e olhar os resultados dela (Regra 23).
- Referências citadas: Machine Learning Crash Course; Machine Learning: A Probabilistic Approach (Murphy); Good Data Analysis; Deep Learning (Goodfellow e outros); o artigo do Google sobre dívida técnica; Sketching User Experiences (Buxton); Don't Make Me Think (Krug).
- Algumas remissões internas apontam para outro número: a Regra 31 remete à 32 para registrar atributos ao servir, tema da 29; a Regra 14 remete à 27 sobre decisão e verossimilhança, tema da 25.
