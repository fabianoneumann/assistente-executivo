# Gravidade por regra ou por julgamento: o que as escalas dizem e o que foi medido

O que as escalas de gravidade de usabilidade, software e redação pedem, e o que se mediu sobre a concordância de quem dá o nível, para decidir entre definir a gravidade por regra ou deixá-la ao julgamento. O procedimento de Nielsen está em [[metodos-de-revisao]]; o MQM e a gravidade no juiz, em [[defeitos-no-lugar-da-nota]].

Convenção: "leitura nossa" liga a fonte a um ambiente de agentes e não está na fonte. "(resumo)" é número lido só no resumo oficial, e os textos desses estudos são pagos; "só citação" é texto fechado; "sem ficha" é texto aberto e lido, que não virou arquivo na base.

## A resposta curta

- **Nada do que se leu mostra que regra, âncora ou árvore de decisão aumente a concordância sobre gravidade.** Há um indício a favor de decompor em fatores, num estudo preliminar. O ganho de κ acima de 0,75 afirmado por um fornecedor de busca não fechou.
- **Pessoas treinadas e modelos divergem no nível exato.**
- **O nível se define pelo que se faz com o problema em Nielsen, e pelo efeito na NASA.** BBC e Lupa usam o efeito no sentido como limiar, sem definir nível; a Folha não define. O nível continua decidido por alguém (leitura nossa).

## 1. O que as escalas pedem

- **Nielsen (1994) não dá fórmula:** frequência, impacto, persistência e impacto de mercado viram uma nota de 0 a 4, e cada nível se define pela ação: 1 não precisa ser corrigido a menos que sobre tempo; 3 é importante corrigir; 4 é obrigatório antes de lançar. A nota de um avaliador só é pouco confiável; a média de três serve para muitos fins, pela experiência dele. [[2026-10-29-nielsen-gravidade-de-problemas]] A fórmula "S = I + F + P − 2" que circula não vem dele (afirmada por um buscador, sem fonte).
- **Software** (NASA SWE-202, página sem data): 3 a 5 níveis, definidos por efeito e adaptados ao projeto, com treino de todos e revisão periódica; o exemplo funde nível e prazo no mesmo rótulo. Sem dado de concordância. [[2026-11-04-nasa-swe-202-niveis-de-severidade-de-software]]
- **Redação (nenhuma traz dado de concordância):**
  - Folha (atualizado em 2024): cabe à Secretaria de Redação classificar "os erros em graves ou menos graves"; há exceções por categoria. [[2026-11-04-folha-manual-da-redacao-erramos]]
  - BBC (sem data na página): no conteúdo sob demanda, a violação séria se corrige e se reconhece, e a não séria recebe correção visível sem alterar o conteúdo; online, corrige-se o erro que altera o sentido editorial. [[2026-11-04-bbc-editorial-guidelines-accuracy-corrigindo-erros]]
  - Lupa: erro gramatical sem nota, salvo se muda o sentido. [[2026-11-04-agencia-lupa-politica-de-correcoes]]

## 2. O que foi medido

- **Humanos (resumo, só citação):**
  - Hertzum, Molich e Jacobsen 2014 (19 profissionais): até 24% (sessão moderada) e 30% (não moderada) dos problemas relatados por mais de um foram "crítico" para um e "menor" para outro.
  - Hertzum e Jacobsen 2001: concordância média entre dois avaliadores de 5% a 65%, em 11 estudos.
  - Tian 2016: cerca de 51% de rótulos inconsistentes em relatos duplicados de bugs.
  - Hertzum 2006: notas de impacto e persistência com correlação fraca com o número de avaliadores que relatou o problema.
- **Modelo (preprint):** Platt 2025, GPT-4o, três sessões, Nielsen de 0 a 4: κ ponderado de 0,63 e concordância exata de 56% na gravidade. O alfa perto de zero que o resumo põe nessa frase é, no corpo, de presença do problema, e os autores o atribuem ao desequilíbrio entre classes. [[2026-11-04-platt-llm-avalia-usabilidade-em-codigo-arxiv-2025]]
- **O único experimento com escalas achado** (Herr 2016, 103 participantes, preliminar): sete fatores ficaram mais perto da nota de dois especialistas (desvio de 23,4) que Nielsen (28,1) e que uma escala de três níveis (39,3), e levaram cerca de 30% mais tempo. Os desvios-padrão menores (2,5, contra 6,7 e 8,8) sugerem menos discordância, dizem os autores, sem medida formal. A distância é de duas pessoas, não concordância entre avaliadores. [[2026-11-04-herr-baumgartner-gross-escalas-de-gravidade-chi-2016]]
- **A nota não acompanha a frequência medida:** Sauro 2013 (blog da empresa dele; um avaliador era o facilitador, viés admitido), 9 estudos, correlação média de 0,056; conclui que não se correlacionam. [[2026-11-04-sauro-problemas-graves-aparecem-primeiro-measuringu-2013]] Hassenzahl 2000 (resumo, só citação): "falta fundamental de correspondência" entre estimativa por dados (tempo de tratamento do problema) e por julgamento. Frequência não é a verdade da gravidade (leitura nossa).

## O que isto dá para um ambiente de agentes (leitura nossa)

- **Separar "é defeito?" de "quão grave?".** A primeira pergunta tem mais chance de concordância; a segunda continua um julgamento, e tirar a pergunta não resolve a falta de definição dos níveis.
- **Definir cada nível pelo efeito no veredito** (o que bloqueia, o que se corrige antes de fechar, o que fica como aviso), como Nielsen faz pela ação, em vez de por uma fórmula.
- **Um teste a experimentar, sem prova:** "altera o sentido, ou leva a fazer errado?". Vem de BBC e Lupa, que não o aplicam a avaliação de conteúdo gerado.
- **Um limite de bloqueio dado pela gravidade de um juiz, sem gabarito, fica sem medida.** Vale registrar isso junto da regra.
- **O sinal da dúvida:** quando a mesma pessoa responde de novo aos mesmos pontos, o "é defeito" tende a se manter e o nível muda com frequência; é um indício de que o nível é o elo fraco.

## Contradições e não verificado

- Menos níveis são mais consistentes (Sauro, por experiência, de 7 para 3, https://measuringu.com/rating-severity/, sem ficha) ou menos precisos (Herr). Sem comparação controlada.
- Sobre se duas classes bastam: a Folha usa duas; nada mede concordância.
- Não verificados, afirmados por fornecedores: κ de 0,20 a 0,45 em bugs, MQM levando κ de 0,18 a mais de 0,70, tipologias de errata.
