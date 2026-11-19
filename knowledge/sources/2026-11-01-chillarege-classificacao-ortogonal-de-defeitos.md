---
titulo: "Orthogonal Defect Classification: A Concept for In-Process Measurements"
tipo: paper
autor: "Ram Chillarege, Inderpal S. Bhandari, Jarir K. Chaar, Michael J. Halliday, Diane S. Moebus, Bonnie K. Ray, Man-Yuen Wong (IBM Thomas J. Watson Research Center)"
url: "https://chillarege.com/docs/Papers/concept"
publicado_em: 1992-11-01
capturado_em: 2026-11-01
licenca: "Copyright 1992 IEEE (declarado na própria página). Cópia de trabalho lida na versão HTML que o primeiro autor mantém no site dele; entra só a ficha."
areas: [agent-engineering]
tags: [orthogonal-defect-classification, defect-taxonomy, defect-type, defect-trigger, root-cause-by-phase, process-feedback, severity-as-effect, missing-vs-incorrect, verification-effectiveness, in-process-measurement, software-quality]
---

Ficha de estudo, em palavras próprias. Publicado na IEEE Transactions on Software Engineering, vol. 18, n. 11, novembro de 1992, p. 943 a 956, DOI 10.1109/32.177364. Lida a versão em HTML do site do primeiro autor (Chillarege Inc.), que reproduz o texto com a nota de copyright da IEEE; **as figuras não estão no texto da página e não foram lidas** (os números e tabelas que elas trazem, como a tabela de associações entre tipo de defeito e fase, ficam fora desta ficha, exceto onde o texto os descreve). É o artigo que apresenta a classificação ortogonal de defeitos (ODC), com os pilotos feitos em laboratórios da IBM. Lido para a rodada investigativa, porque a camada 1 trouxe a ODC (agente a5) para ligar o tipo do defeito à camada do processo que o causou.

**Atenção à força da evidência:** é um artigo de conceito com resultados de projetos-piloto internos da IBM (gráficos de distribuição em algumas fases), não um experimento controlado. A versão aqui é a de 1992; o esquema evoluiu depois (versões posteriores com mais atributos), e esta ficha não cobre as versões seguintes.

## 1. O problema

Medir um processo de desenvolvimento para dar retorno a quem desenvolve esbarra na falta de relações de causa e efeito validadas. Num extremo, os modelos de confiabilidade tratam todos os defeitos como iguais; no outro, a análise de causa raiz dá retorno qualitativo, defeito a defeito, caro e lento. Faltava o meio: um jeito sistemático e barato de tirar dos defeitos um sinal sobre o processo.

Um estudo anterior dos autores mostrou que, classificando os defeitos pelo **significado da correção**, dava para ligar mudanças na curva de crescimento de confiabilidade a tipos específicos de defeito: grupos com mais defeitos de inicialização tinham curvas com inflexão (erros no começo do caminho do código escondem outros), e muitos defeitos de função apontavam para um problema no desenho.

## 2. O que é a ODC

Classificar cada defeito em classes que, juntas, **apontam a parte do processo que precisa de atenção**, como localizar um ponto em eixos ortogonais pelas coordenadas. Três requisitos para um sistema de medida que permita aprender com a experiência e comparar projetos: **ortogonalidade** (classes distintas e mutuamente exclusivas), **consistência entre as fases** (a mesma classificação vale do desenho ao teste) e **uniformidade entre produtos** (independe do produto e da organização). Poucas classes, porque escolher entre poucas é mais fácil e erra menos.

- **Condição necessária:** existe uma classificação **semântica** dos defeitos tal que as classes se relacionam com o processo e explicam o avanço do produto por ele.
- **Classificar pelo significado da correção, não pela opinião de onde o defeito nasceu.** Perguntar ao programador "em que fase isto entrou?" é a solução degenerada: é uma pesquisa de opinião, propensa a erro, específica de um processo e inútil quando o processo muda. O tipo do defeito é decidido pela correção que acabou de ser feita, por isso é mais exato ("medida de um evento, não opinião sobre o processo"); o preço é uma tabela de associação que liga cada tipo às fases, calibrada para cada processo.
- **Condição suficiente:** os valores de cada atributo formam um **conjunto gerador** do espaço do processo: tudo o que se quer inferir pode ser descrito pelas classes. Não dá para garantir isso de antemão; é método experimental, que se refina com os pilotos. Os tipos começaram com cinco (função, inicialização, checagem, atribuição, documentação) e chegaram a oito; os que já existiam e as dimensões que cobriam ficaram estáveis.

## 3. Três grupos de dados

- **Atributos de causa**, escolhidos ortogonais: o **tipo do defeito** e o **gatilho** (abaixo).
- **Atributos de efeito**: a **gravidade** (na IBM, de 1 a 4), o impacto no cliente (a classificação CUPRIMD: capacidade, usabilidade, desempenho, confiabilidade, instalação, manutenção, documentação) e medidas calculadas (crescimento de confiabilidade, densidade de defeitos). **A gravidade é um eixo à parte do tipo**, não parte dele.
- **Identificadores de subpopulação**: projeto, pessoas, processo, ferramentas, para comparar grupos.

## 4. O tipo do defeito

Escolhido por quem corrige, implícito na correção; em cada tipo se distingue **faltando** de **incorreto**. Os oito tipos: **função** (capacidade importante, interfaces com o usuário ou com outros produtos, estruturas globais; pede mudança formal de desenho), **atribuição** (poucas linhas: inicialização, valores), **interface** (interação com outros componentes), **checagem** (lógica que não valida dados antes de usar), **temporização e serialização** (recursos compartilhados e de tempo real), **montagem, empacotamento e integração** (bibliotecas, controle de versão), **documentação** e **algoritmo** (eficiência ou correção que se resolve reimplementando, sem mudar o desenho). Cada tipo se associa a poucas fases: um defeito de **função** aponta para o **desenho de alto nível**, achado no teste de sistema ou no de unidade; um de temporização, para o desenho de baixo nível.

**Usar a distribuição, não o defeito isolado.** Em cada fase, a proporção de cada tipo tem um perfil esperado: função cai ao longo do processo, temporização sobe no teste de sistema, atribuição tem pico no teste de unidade e interface na integração. A mudança da distribuição mede o avanço do produto e mostra quando ele está "logicamente" numa fase anterior à que está "fisicamente" (por exemplo, no teste de sistema com o perfil de teste de unidade). Um desvio do perfil aponta o tipo culpado e, por ele, a fase do processo que falhou. No piloto, a proporção de defeitos de função chegou a quase metade no último período (teste de sistema): o remédio indicado era **revisar o desenho de novo, não testar mais**. Outros pilotos mostraram tendências saudáveis (função e interface caindo, algoritmo subindo do desenho de alto para o de baixo nível; atribuição e checagem subindo na inspeção de código) e uma doente (interface dominando nos testes de função e de sistema, e atribuição ainda subindo tarde).

**Inferência automática:** com a tabela das associações principais (tipo por fase de verificação), monta-se para cada tipo uma árvore binária de "alto" ou "baixo" em cada fase associada; cada caminho da raiz à folha é uma história de desenvolvimento com uma inferência. Exemplo: para função, alto na inspeção de desenho, baixo no teste de função e alto no teste de sistema quer dizer que o desenho está exposto e o teste de função falhou, então é ele que se refaz. Os critérios de alto e baixo vêm da experiência.

## 5. O gatilho do defeito

A **condição que fez o defeito aparecer**. Não fala do processo de desenvolvimento, e sim do **processo de verificação**: a distribuição dos gatilhos dos defeitos de campo deveria parecer a do teste de sistema; uma discrepância mostra buracos no teste. Exemplo: em defeitos de corrupção de memória do MVS, a crença era que a temporização os disparava; os gatilhos mostraram só 12,4% por temporização e as condições de fronteira como causa dominante, o que trocou o investimento de testar em vários equipamentos para **inspecionar o código procurando condições de fronteira**.

**Gatilhos de revisão de documento e inspeção de código:** derivados do que cada revisor faz (procurar detalhes, conferir conformidade com requisitos, compatibilidade para trás e lateral, consistência e seções faltando, situações raras). **Cada gatilho pede uma habilidade**: detalhe pede pouca experiência; compatibilidade lateral pede quem conhece outros produtos; situação rara pede muita experiência. O produto cruzado de tipo e gatilho mede a eficácia da verificação. Num piloto, **a ausência de defeitos de interface achados por compatibilidade lateral, num produto com muita interação com outros, era suspeita: ou o desenvolvimento era excelente, ou a revisão era deficiente**. Olhando a equipe de revisão, faltava quem conhecesse os outros produtos; uma segunda revisão foi feita e medida pelos mesmos gatilhos.

## 6. Custo e implantação

Na ordem de uma dúzia de teclas por defeito, menos de um a quatro minutos conforme o sistema de registro; formação de cerca de três horas com laboratório; um processo definido para analisar e devolver os dados, com donos. A ODC alimenta o processo de prevenção de defeitos (que acha a causa raiz e cria ações para não repetir) apontando os pontos quentes e ordenando os problemas por impacto, sem análise humana de cada defeito e sem o limite de atenção humana.

## 7. Contribuições, nas palavras dos autores resumidas

Classificação baseada no que se sabe do defeito (tipo, gatilho), não em opinião (onde foi injetado); o tipo como medida do avanço pelo processo, com o desvio da distribuição como alarme que aponta a fase; o gatilho como medida da eficácia e da completude da verificação; retorno rápido aos desenvolvedores; e a ODC como conceito geral, que a IBM já explorava em hardware, em produção de informação e em problemas que não são defeitos.

## 8. Tudo o mais que ensina

- **A calibração leva tempo**, mas, até ela, a análise de tendência entre duas fases já orienta.
- **Classes podem se fundir** quando apontam para as mesmas fases e a resolução extra não é desejada; podem crescer quando o processo ganha dimensões novas (concorrência, montagem em larga escala) sem mexer nas que já existiam.
- **Defeitos de um tipo escondem outros** (inicialização no começo do caminho do código), e isso deforma a curva de achados.
- **Produtos mais velhos têm menos defeitos de função** e mais de atribuição e checagem no campo: o perfil muda com a maturidade.
- **Zero achados não é boa notícia por si:** só se lê contra o perfil esperado e contra quem estava procurando.
