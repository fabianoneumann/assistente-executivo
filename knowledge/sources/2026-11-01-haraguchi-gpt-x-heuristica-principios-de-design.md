---
titulo: "Can GPTs Evaluate Graphic Design Based on Design Principles?"
tipo: paper
autor: "Daichi Haraguchi, Naoto Inoue, Wataru Shimoda, Hayato Mitani, Seiichi Uchida, Kota Yamaguchi"
url: "https://arxiv.org/abs/2410.08885"
publicado_em: 2024-10-11
capturado_em: 2026-11-01
licenca: "Licença não exclusiva de distribuição do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/, indicada na página do arXiv); o PDF traz o bloco de permissão da ACM com direitos de publicação licenciados à ACM. Entra só a ficha."
areas: [agent-engineering, content-design]
tags: [vlm-as-judge, layout-metrics, alignment-metric, overlap-metric, white-space, design-principles, human-agreement, perturbation, pairwise-judgment, odonovan-energy]
---

Ficha de estudo, em palavras próprias; sem texto integral. arXiv: v1 em 11/10/2024, a única versão, com o comentário "Accepted to SIGGRAPH Asia 2024 (Technical Communications Track)"; 6 páginas mais apêndices A a D. Autores da CyberAgent (Japão) e da Universidade de Kyushu. Texto extraído do PDF com `pdftotext`; os coeficientes da Figura 3 vêm do texto extraído da figura (ver o cuidado na seção 4). Lido para a rodada investigativa (métricas de layout calculáveis contra pessoas). Dados em https://cyberagentailab.github.io/Graphic-design-evaluation/.

## 1. A pergunta

Estudos de geração de design passaram a usar modelos multimodais (GPT-4 e afins) como avaliadores, supondo que eles julgam bem; não se sabia se isso vale. Os autores escolhem um terreno onde dá para comparar com uma medida calculada: três princípios de design que já têm fórmula heurística na literatura (O'Donovan et al., 2014), alinhamento, sobreposição e espaço em branco, e os princípios como descritos por Graham (2002) e Williams (2014). Comparam três leituras da mesma peça: a heurística calculada nas caixas, o GPT-4o olhando a imagem, e pessoas.

## 2. Os princípios e as heurísticas (apêndice A)

- **Alinhamento:** bordas de elementos vizinhos na mesma linha ou coluna; desalinhamento leve entre elementos que parecem querer se alinhar é penalizado pelo tamanho do erro; grupos alinhados maiores (elementos distantes na mesma linha) são preferidos.
- **Sobreposição:** três tipos (elemento sobre texto, texto sobre gráfico, gráfico sobre gráfico); texto com pouco contraste com o fundo é penalizado (a fórmula mede a mudança de cor da área antes e depois de renderizar o texto); elemento que sai do canvas é penalizado.
- **Espaço em branco:** cinco componentes: proporção do canvas sem elementos (mais é melhor), penalidade para regiões grandes demais vazias (distribuição equilibrada), distância entre elementos, variância do espaçamento vertical entre textos (uniforme é melhor) e margens nas bordas.
- As heurísticas são calculadas nas coordenadas e tamanhos dos elementos, normalizadas de 0 a 1. O prompt do GPT-4o transcreve os mesmos pontos e pede nota de 1 a 10 ("um design medíocre só ganha 7"), em JSON com explicação curta.

## 3. Os dados e as pessoas

- **100 templates** de banners e cartazes do VistaCreate, com coordenadas e tamanhos; cada um perturbado em três intensidades (pequena, média, grande) em dois eixos: a posição x do texto (para alinhamento) e o tamanho da fonte (para sobreposição e espaço em branco). Total de 700 peças (100 originais e 600 perturbadas).
- **60 pessoas** por crowdsourcing, cinco notas de 1 a 10 por peça e por princípio; usa-se a média das cinco. O GPT-4o roda cinco vezes por peça, temperatura 1, e também se usa a média.

## 4. Resultados

- **Correlação com as pessoas (Pearson, Figuras 3 e 4):** a heurística fica em 0,310, 0,476 e 0,233; o GPT-4o em 0,524, 0,771 e 0,651. **Cuidado:** os valores vêm do texto extraído da figura, na ordem em que aparecem, que é a ordem alinhamento, sobreposição e espaço em branco das colunas da Figura 4; a atribuição exata de cada valor a cada princípio não foi conferida na imagem. O que o texto do artigo afirma sem ambiguidade: o GPT-4o correlaciona mais com as pessoas que a heurística nos três princípios e em todos os níveis de perturbação.
- **Sensibilidade (Figura 6):** a correlação do GPT-4o cresce com a intensidade da perturbação; no defeito grande, ele acompanha bem as pessoas.
- **Estabilidade (Figura 7):** o desvio padrão das notas do GPT-4o entre execuções é menor que o das notas entre pessoas.
- **Por que a heurística perde na correlação:** ela foi feita para comparar uma peça antes e depois de otimizar, não duas peças diferentes. Na Figura 5, três designs humanos diferentes recebem da heurística uma ordem que pessoas e GPT-4o não compartilham (ela rebaixa um design profissional bom).
- **Onde a heurística ganha (Figura 9 e apêndice C):** como lê os vetores, ela vê diferenças pequenas que o GPT-4o não vê. Na avaliação em pares (a peça original contra a perturbada, cinco execuções e voto, com "as duas iguais" permitido), o acerto do GPT-4o sobe com a intensidade; no médio e no grande ele empata com a heurística; **no pequeno, perde para a heurística em alinhamento e espaço em branco.**
- **Onde o GPT-4o ganha (Figura 8):** num design com objeto embutido no fundo, a heurística conta o fundo como espaço em branco; o GPT-4o vê.

## 5. Conclusão dos autores

O GPT-4o julga razoavelmente bem a adesão a princípios de design e se parece com a heurística, mas não distingue detalhes pequenos; trabalhos futuros: julgar vários princípios juntos e ir além deles (escolha de fonte).

## 6. Tudo o mais que ensina (e o que fica em aberto)

- **A verdade das pessoas também é grossa:** as notas humanas são sobre a imagem, com cinco notas por peça; um desalinhamento de poucos pixels que o código mede pode não aparecer na nota humana, e a correlação baixa da heurística mistura "a heurística erra" com "a pessoa não viu". O artigo não separa os dois.
- **As perturbações são sintéticas e de um eixo** (posição x, tamanho de fonte); defeitos de composição de verdade (tela meio vazia, desenho fora do lugar) não foram testados.
- **Os princípios vêm do mesmo repertório que a base usa** (Williams): alinhamento e proximidade aparecem como fórmula.
- **Trabalhos citados:** O'Donovan et al. (2014, as fórmulas de energia de layout), COLE (Jia et al., 2023, parte do prompt), Ferret (You et al., 2023, a mesma limitação de detalhe fino), OpenCOLE, Graphist, TextDiffuser-2.
