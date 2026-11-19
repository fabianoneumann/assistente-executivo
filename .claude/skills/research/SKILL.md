---
name: research
description: >-
  Pesquisa profissional de dados, estudos e estatísticas em fontes confiáveis
  (via Perplexity/Sonar, Gemini, a busca web nativa e, opcional, o Codex), com síntese,
  reconciliação de contradições e registro rastreável na base `knowledge/`. USE SEMPRE
  que a pessoa pedir para pesquisar, buscar dados/estatísticas/estudos/fontes, embasar
  uma ideia de conteúdo ou aula, levantar o estado de um tema, ou "ver o que existe"
  sobre um assunto, mesmo que não diga "pesquisa" nem "skill", e mesmo que só mencione
  uma ideia de `marketing/social-media/ideas/` que precise de lastro. NÃO use para
  conversa/opinião sem coleta de dados, nem para perguntas que você já responde bem
  sem buscar fontes externas.
---

# Skill: research

Processo previsível de pesquisa de nível profissional (pensar como jornalista de dados): **coletar de várias fontes de alta qualidade → o Claude sintetiza e reconcilia → registrar na base `knowledge/`**, para que o conhecimento componha ao longo do tempo (padrão LLM Wiki) e sirva a conteúdo e estudo futuros.

**O que é do projeto** (os caminhos da base, onde ficam as rodadas, a regra de lugar do que é de terceiro, a regra de custo, as partes opcionais): [`references/projeto.md`](./references/projeto.md). Os caminhos sem `./` nem `../` (`scripts/...`, `references/...`) partem da pasta da skill; os comandos rodam da raiz do projeto.

**Lições:** antes de começar, leia as abertas e as apontadas em [`licoes.md`](./licoes.md) desta pasta. Chaves e setup: [`README.md`](./README.md).

## Passo 0, as credenciais

Antes de tudo, rode da raiz do projeto `python -X utf8 scripts/confere_ambiente.py --skill research`. Se ele sair com `[PARE]`, pare aqui: repasse à pessoa a mensagem dele (qual variável falta, onde se pega e como se põe) e não tente rodar a skill sem a chave. Se o script não existir (a skill instalada como plugin noutro projeto), siga: o próprio código da skill para com a mesma mensagem na primeira chamada.

As obrigatórias são a `PERPLEXITY_API_KEY` e a `GEMINI_API_KEY`; a `VERTEX_API_KEY` e o Codex são opcionais, e o que faltar deles só desliga a parte deles.

## Duas manoplas

Toda pesquisa combina **fonte** (Perplexity × Gemini × busca web nativa × Codex, as duas últimas só no raso) e **profundidade** (raso × profundo). São decisões independentes.

## Passo 0b, a base primeiro

Antes de buscar fora, consultar a base pelo ritual de consulta de `knowledge/README.md` (Query): a porta de entrada e o índice da área, as sínteses e, se preciso, a busca com a pergunta escrita de várias formas, inclusive os termos do assunto vizinho (o custo, onde roda, quem vê) e as pastas fora de `knowledge/` que decidem sobre ele (`references/projeto.md`, "A base"). Se a base já cobre o tema, a pesquisa é de complemento (raso, o que mudou desde o `capturado_em`); se não cobre, dizer "nada registrado" ao apresentar os achados.

## Passo 1, decidir a profundidade

Padrão é **raso** e você age sozinho. Escale para **profundo** quando o tema for amplo, técnico ou contestado (pede varredura exaustiva e reconciliação de contradições). Antes de rodar um profundo, **confirme com a pessoa**, a não ser que ela tenha pedido "profundo/deep" explicitamente: o profundo custa bem mais (o raso é centavos), então a decisão de gastar é dela (`references/projeto.md`, "Custo das APIs").

**Raso é o certo para:** pergunta delimitada, um dado pontual e, em especial, **atualizar ou complementar uma síntese já existente** com números mais recentes. Nesses complementos, o dado novo entra na síntese e o antigo permanece como **histórico/comparação** (a data vive no `publicado_em` da fonte).

**O profundo não é a porta de entrada obrigatória de temas novos.** Com a iteração do raso (Passo 2.5), muitos temas se resolvem no raso. O profundo é a **escalação** para o amplo, técnico ou contestado que a iteração rasa não fecha.

## Passo 2, raso (as quatro frentes, em paralelo)

Dispare as frentes **na mesma leva** (as chamadas Bash e a ferramenta `WebSearch`, numa só mensagem): é barato e enriquece por triangulação (índices diferentes acham fontes diferentes; quando concordam, sobe a confiança no que procurar na primária, mas não confirma; quando discordam, é sinal a reconciliar, não ruído). A pergunta pede o fato, sem levar a hipótese de quem pediu (Passo 5, "O peso das fontes"):

```
python -X utf8 .claude/skills/research/scripts/perplexity_search.py --mode shallow --query "<pergunta>"
python -X utf8 .claude/skills/research/scripts/gemini_search.py     --mode shallow --query "<pergunta>"
python -X utf8 .claude/skills/research/scripts/codex_search.py      --query "<pergunta>"     (opcional)
WebSearch(query="<pergunta, mais curta e com os termos exatos>")
```

**A busca web nativa da sessão** (ferramenta `WebSearch`; carregar o schema por `ToolSearch` se estiver adiada) é boa em **termo exato** (nome de repositório, número de issue, identificador de CVE, nome de arquivo) e custa zero em API. Limites: devolve links e um resumo em texto, **fora do contrato JSON**, sem data de publicação e com viés de fontes em inglês e dos Estados Unidos; o resumo dela também erra, então a regra de abrir a primária vale igual. Use a query dela mais curta que a dos scripts, com os termos que identificam a coisa, e rode uma segunda variação quando o tema tiver repositório ou histórico de segurança.

**O Codex com a busca na web** (`codex_search.py`, opcional) costuma trazer achados que as outras frentes não trazem e marca "sem fonte" o que não tem primária, mas também erra atribuição: o que ele traz se confere na primária como o resto. Se não rodar (sem o Codex ou sem o login), a rodada segue com as outras três e diz isso.

Guarde cada saída numa pasta própria da rodada no scratchpad, com o tema e a hora no nome: pesquisas que rodam ao mesmo tempo, em sessões ou agentes paralelos, sobrescrevem arquivos de mesmo nome. Os nomes: `qN-perplexity.json`, `qN-gemini.json`, `qN-codex.json` e, para cada busca nativa (a principal e as levas dirigidas), a saída colada como veio num `qN-nativa.md`, porque ela volta na conversa, não em JSON, e sem o arquivo a revisão não confere a leva. Leia os JSONs (o contrato em [`references/scripts.md`](./references/scripts.md)) e os links da busca nativa. Não grave nada na base ainda.

## Passo 2.5, iterar o raso antes de escalar

**Duas variações rodam sempre, mesmo quando o raso parece completo:** quando o público é brasileiro (`references/projeto.md`), pelo menos uma em português por pergunta, ou o rascunho diz que se escolheu não fazer, porque o que vem do Brasil quase não chega pelas consultas em inglês; e, quando a pergunta nomeia mais de um produto, versão ou superfície, uma dirigida a cada um, antes de dizer que a lista está completa.

Se o raso vier **incompleto ou com fonte fraca** (comum em dados com número e data), **reformule e rode de novo**, em 2 ou 3 variações: sinônimos, termos em inglês, o **ano explícito**, termos de domínio ou de relatório. A query é a maior alavanca de recall.

**Regra de parada:** se 2 ou 3 reformulações seguem batendo em fonte fraca, isso *é* o sinal: ou o dado **não existe publicamente** (registre a lacuna, não force), ou aí sim vale o **profundo** (confirme com a pessoa). Como julgar a fonte e o que se sabe das regras de parada estão na síntese de método da base, [`avaliar-fonte-e-parar-a-busca`](../../../knowledge/journalism/avaliar-fonte-e-parar-a-busca.md).

## Passo 3, profundo (rotear um só)

Escolha o motor pela **natureza do dado**, não pelo rótulo do tema:

- Dado citável, estatística, estudo específico → **Perplexity Deep**: `python -X utf8 .claude/skills/research/scripts/perplexity_search.py --mode deep --query "<pergunta>"`
- Técnico-científico ou varredura ampla → **Gemini Deep**: `python -X utf8 .claude/skills/research/scripts/gemini_search.py --mode deep --query "<pergunta>"`

Os dois profundos são **assíncronos** (levam minutos): **rode em background** e retome ao terminar. Rodar dois profundos é desperdício (caro e redundante): escolha um.

## Passo 4, triagem preliminar

Pré-filtre os resultados por **autoridade da fonte, relevância e snippet**, barato e rápido. É só o corte inicial; a decisão real vem depois de abrir os links. A raw é curada, não um log de tudo que a busca cuspiu. As ações do SIFT e os critérios do CRAAP, para julgar a fonte, estão na mesma síntese de método do Passo 2.5.

## Passo 5, verificar os links e apresentar os achados

**Abra os links da shortlist** (WebFetch) antes de decidir o registro; nunca julgue uma fonte só pelo snippet ou pela autoridade. Isso pega erro de número, página de imprensa sem dado e paywall. O WebFetch devolve o resumo que um modelo pequeno fez da página, e o resumo serve para triar: a primária que vai virar ficha ou sustentar um "a fonte não diz" se lê no texto bruto (curl e extração, ou o Chrome), porque o resumo corta dados. Ao extrair, confira o tamanho e o título do bloco (`<article>`, `<main>`): ele pode ser só a caixa de relacionados ou a barra do leitor, e parte do conteúdo pode estar em dados embutidos da página (JSON-LD, abas). Ao abrir, classifique cada candidata:

- **Raw registrável**: conteúdo acessível e substantivo → pode virar fonte em `knowledge/sources/` (o ritual exige o corpo, não só o link: inteiro se a licença permitir cópia, em ficha se não; ver `knowledge/sources/README.md`). Anote a licença de cada candidata ao abrir o link.
- **Só citação**: paywall, inacessível ou página vazia, depois de tentar as rotas de `knowledge/sources/README.md` ("Quando a primária não abre") → **não** vira fonte; entra como **citação** na síntese, com o dado vindo do relatório do profundo ou de fonte aberta que corrobore.

**Rotule a triagem:** toda pesquisa, de qualquer tamanho, deixa um `rotulos.json` na pasta da rodada, com as candidatas e os objetivos. O formato, o que é rodada e candidata, quando fecha, o texto de cada fonte lida e a cópia da pasta da rodada estão em [`references/rotulos.md`](./references/rotulos.md).

**Conteúdo bom sem citação é *não verificado*, não *falso*.** Quando um fornecedor devolver resposta rica mas **sem grounding** (`results` e `citations` vazios, comum no Gemini), não descarte em silêncio: **extraia as afirmações específicas** (nomes, termos, números, atribuições), a lista inteira antes de escolher o que rodar, e **rode uma leva dirigida a elas**; o que ficou sem leva fica dito no rascunho. O inverso também vale: atribuição que *parece* sólida pode não fechar em primária. Nos dois casos, quem decide é a verificação, não a impressão. O que sobreviver entra normalmente; o que não fechar entra na síntese **marcado como não verificado**, com quem afirma. Nunca suma com o material sem registrar que ele existiu.

Antes de escrever que "a fonte não diz", busque nela sem corte de saída (a contagem primeiro, depois o trecho) e diga o termo buscado; e o número que resume um grupo (mínimo, máximo, mediana) sai de um script sobre o grupo inteiro, não da leitura de uma listagem.

**O peso das fontes:** fontes do mesmo grupo, ou que citam umas às outras, contam como uma voz; a pergunta ao buscador não leva a hipótese de quem pediu; a fonte primária que contesta veta o "confirmado"; muitas fontes secundárias sem primária saem como "não verificado"; e o juízo de valor se decompõe em afirmações medidas antes de conferir. Confirmada é a afirmação lida na fonte primária: os buscadores concordando ainda são secundárias, e já erraram juntos o ponto que mais pesava. **Conferências deste passo** (o peso das fontes, com o porquê; a linha que vira custo de teste ou recomendação, lida na seção inteira da fonte; cada versão do rascunho guardada antes de corrigir; a fonte que entra pela correção tratada como rascunho deste passo): [`references/conferencias.md`](./references/conferencias.md).

Toda leitura do assistente (conciliação entre fontes, hipótese, conta nossa) leva a marca "leitura do assistente" desde o primeiro rascunho, e a marca não sai ao reescrever: sem ela, a leitura nossa vira, na versão seguinte, o motivo atribuído a uma fonte.

Depois, **apresente à pessoa os achados JUNTO com a shortlist**, não só a lista de fontes: os **dados extraídos** organizados por tema (cada número com sua fonte e ano), o que **mantenho e por quê**, o que **descarto e por quê**, e as **contradições** a reconciliar. Assim ela veta ou decide sabendo o que a pesquisa achou. Ainda **não** grave nada na base.

## Revisão (skill `review`)

**A revisão roda duas vezes:** no fim do Passo 5, antes de apresentar os achados e a lista de fontes; e de novo no Passo 7, com a síntese escrita, antes de pedir a validação. Leia [`references/revisao.md`](./references/revisao.md) antes de cada uma: o ponto de pausa, o nível, as lentes, o que conferir e os itens que se esquecem.

## Passo 6, o veto de quem pediu

**A shortlist entra no registro sem esperar aprovação.** Os achados e a lista vão à pessoa no fim do Passo 5, e o Passo 7 começa em seguida; ela pode vetar uma fonte até o commit (`references/registro.md`, item 6). Esperam a palavra dela, além do "para decidir" da revisão, só a fonte que contraria uma decisão já registrada ou muda uma regra, a de licença em dúvida e a de parte interessada que sustenta uma recomendação, que vão à parte na entrega do Passo 5. A conversa dos takeaways também passa para a validação antes do commit. Por quê: aprovar a lista inteira toda vez vira carimbo, e o veto até o commit guarda a decisão onde ela muda alguma coisa. Dentro da `story-angle`, as fontes da apuração seguem a curadoria dela, que já é a parada da mesa.

## Passo 7, registro do que não foi vetado (ritual de Ingest)

Leia [`references/registro.md`](./references/registro.md) antes de executar esta parte: o ritual de Ingest passo a passo (as raw registráveis, o frontmatter, a síntese, o índice, o log e o commit).

## Contrato de saída dos scripts

Leia [`references/scripts.md`](./references/scripts.md) antes de ler as saídas: o formato de cada script.
