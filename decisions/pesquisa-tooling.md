# Ferramental de pesquisa (skill `research`)

## Contexto

As ideias de conteúdo quase sempre pedem dados recentes de fontes confiáveis, registrados em `knowledge/`. O objetivo é um processo de pesquisa profissional e auditável, no nível de um jornalista de dados, que sirva ao conteúdo, ao estudo e às decisões.

## Decisões (com o porquê)

- **Coletor e sintetizador, não "resposta pronta".** Os provedores fazem a busca; o Claude sintetiza e reconcilia as contradições. A síntese é analítica; a voz de escrita de quem usa (`context/sobre-mim.md`) só entra quando a pesquisa vira post ou aula. Por quê: o conhecimento compõe na base, em vez de morrer no chat, e ver a saída crua de cada fonte é o que permite reconciliar.
- **Duas manoplas independentes:** a fonte (Perplexity, Gemini, a busca nativa, o Codex) e a profundidade (raso ou profundo).
- **Raso: as frentes em paralelo.** Barato, e enriquece por triangulação, porque índices diferentes acham coisas diferentes. **Profundo: rotear um** pela natureza do dado: citável, estatística, estudo, para o Perplexity Deep; técnico-científico ou varredura ampla, para o Gemini Deep Research.
- **A busca web nativa da sessão como frente do raso.** Por quê: os buscadores por API descrevem um produto e deixam de fora o que o índice da busca comum acha na primeira consulta, sobretudo o **termo exato** (repositório, número de issue, identificador de CVE), a custo zero. Limites assumidos: a saída é texto e links, fora do contrato JSON, sem data de publicação e com viés de fontes em inglês. Por isso é triangulação, não substitui os scripts, e a regra de abrir a primária antes de registrar segue.
- **Régua de profundidade:** padrão raso e autônomo; escala para o profundo quando o tema é amplo, técnico ou contestado, **confirmando antes** (custo maior), salvo pedido explícito.
- **Modelos de melhor valor, não topo de linha.** O ganho marginal dos modelos mais caros não compensa o custo na busca rasa.
- **Fronteira de autonomia: na busca e no registro, com veto.** A shortlist entra no registro sem esperar a aprovação, e quem pediu pode vetar uma fonte até o commit, quando também se conversam os takeaways. Esperam a palavra de quem pediu: a fonte que contraria uma decisão registrada ou muda uma regra, a de licença em dúvida e a de parte interessada que sustenta uma recomendação, além do "para decidir" da revisão. Por quê: a aprovação lista a lista acabava sendo sempre "aprovado"; o veto mantém o controle onde ele muda algo. Na `story-angle`, a curadoria continua na mesa de ângulos (`apuracao-e-pauta.md`).
- **Scripts separados por fornecedor,** finos: chamam a API e devolvem JSON no contrato. Sem orquestrador em código: o Claude e o `SKILL.md` orquestram.
- **Chaves** no `.env` da raiz ou no bloco `env` do `.claude/settings.local.json`, ambos fora do git; os scripts leem do ambiente e param com a mensagem do que falta, sem imprimir o valor. Documentadas no README da skill e no `.env.example`.
- **O Gemini Deep Research é um agente**, não um modelo: a chamada é assíncrona (cria em segundo plano, consulta o andamento, cancela no tempo limite).

## O peso das fontes

- **Fontes do mesmo grupo, ou que citam umas às outras, contam como uma voz.**
- **A pergunta ao buscador não leva a hipótese de quem pede.** Por quê: o modelo tende a concordar com quem pergunta.
- **A fonte primária que contesta veta o "confirmado".** Confirmada é a afirmação lida na fonte primária; muitas fontes secundárias sem primária saem como "não verificado".
- **O juízo de valor se decompõe em afirmações medidas** antes de conferir.
- **A fonte trazida pela curadoria pesa na escolha do tema e do ângulo; o fato se decide na primária,** também contra ela. O campo `entrada` (`curadoria`, `pesquisa`, `pratica-propria`) no frontmatter das fichas separa o que foi trazido do que a busca achou (`knowledge/sources/README.md`).

Por quê: onde a pesquisa muda um resultado, quase sempre é um fato pontual tirado da fonte primária; as rodadas largas tendem a só confirmar o que havia, e parte das afirmações dos buscadores não resiste à fonte. E dois buscadores podem errar juntos o ponto que mais pesa, quando ambos se apoiam nos mesmos resumos; só a página do dono do assunto mostra. A concordância entre buscadores não substitui a primária.

## A ficha não encolhe

A ficha de método clássico continua extraindo o máximo da fonte, também no conceito; a ficha de documentação técnica longa pode sair como nota de fato, desde que não cole frases (`knowledge/sources/README.md`, item 2). Por quê: a ficha serve a três coisas, e o "o modelo já sabe isso" mede só uma. As outras duas pesam mais: ser o lastro das regras dos processos (a regra aponta a fonte e o trecho, e isso vale mesmo quando o modelo sabe o conceito) e durar quando o modelo muda. Num teste de perguntas sobre fichas clássicas respondidas por um agente sem a ficha, o modelo sabia só parte do conceito e menos ainda do detalhe exato e do nicho. **Revê se:** o modelo mudar (o teste se repete), ou o custo de ler as fichas passar a pesar na carga das tarefas.

## Elos

- Skill: `research` (o processo).
- Base e rituais: `knowledge/README.md`, `knowledge/sources/README.md`, `knowledge/research-rounds/README.md`.
- Apuração investigativa: `apuracao-e-pauta.md`.
