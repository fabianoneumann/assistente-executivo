---
titulo: "Code Review do Claude Code: documentação oficial (serviço, /code-review local, ultrareview), post de lançamento e plugin code-review"
tipo: artigo
autor: "Anthropic"
url: "https://code.claude.com/docs/en/code-review.md"
capturado_em: 2026-10-29
licenca: "Documentação e blog: todos os direitos reservados (rodapé da página Legal and compliance da documentação: '© Anthropic PBC. All rights reserved. Use is subject to applicable Anthropic Terms of Service.'; blog: '© 2026 Anthropic PBC'); entra só a ficha. O repositório anthropics/claude-code também é 'All rights reserved' (LICENSE.md). O plugin code-review atual, em anthropics/claude-plugins-official, é Apache 2.0 (arquivo LICENSE na pasta plugins/code-review); também ele entra só em palavras próprias, e o texto original está em plugins/code-review/commands/code-review.md naquele repositório."
areas: [agent-engineering, anthropic-claude]
tags: [code-review, multi-agent-review, verification, false-positives, severity, confidence-scoring, review-instructions, effort-levels, llm-as-judge, sycophancy]
---

Ficha de estudo, em palavras próprias, das páginas oficiais sobre revisão de código no Claude Code, lidas em markdown em 2026-10-29 (changelog mais recente na página: v2.1.312, 27/10/2026). A documentação não tem licença aberta; citações literais só curtas. O comando do plugin `code-review` tem licença Apache 2.0, mas também entra aqui em palavras próprias: o texto original está em `plugins/code-review/commands/code-review.md`, no repositório `anthropics/claude-plugins-official` (https://github.com/anthropics/claude-plugins-official).

**De onde vem cada coisa** (as marcas entre colchetes nas seções abaixo apontam para estas fontes):

- [visão geral] https://code.claude.com/docs/en/code-review.md
- [setup] https://code.claude.com/docs/en/code-review-setup.md (níveis de revisão, quando roda)
- [customizar] https://code.claude.com/docs/en/code-review-customize.md (`REVIEW.md` e `CLAUDE.md`)
- [no PR] https://code.claude.com/docs/en/code-review-pull-requests.md (gravidade, comandos, re-revisão)
- [custos] https://code.claude.com/docs/en/code-review-costs.md
- [problemas] https://code.claude.com/docs/en/code-review-troubleshooting.md
- [local] https://code.claude.com/docs/en/code-review-local.md (o comando `/code-review`)
- [ultra] https://code.claude.com/docs/en/ultrareview.md
- [comandos] https://code.claude.com/docs/en/commands.md (linhas de `/code-review`, `/review`, `/simplify`, `/ultrareview`)
- [desktop] https://code.claude.com/docs/en/desktop.md, seção "Review your code"
- [changelog] https://code.claude.com/docs/en/changelog.md, com a versão de cada entrada
- [blog] *"Bringing Code Review to Claude Code"*, https://claude.com/blog/code-review, 09/03/2026
- [plugin v1] comando `plugins/code-review/commands/code-review.md` no repositório `anthropics/claude-code`, versão de 12/11/2025 (commit b85cc44), sem licença aberta
- [plugin] o mesmo comando, versão atual em `anthropics/claude-plugins-official` (commit c905cd8, 26/10/2026, "bring in the newer command from anthropics/claude-code"), Apache 2.0, e o README da pasta

## O mapa: cinco coisas com nome parecido

A documentação separa ferramentas que têm "review" no nome e não são a mesma coisa. Confundir uma com a outra é o erro mais fácil ao ler sobre o assunto.

| Ferramenta | O que é | Onde roda | Quem usa | Lê `REVIEW.md`? |
| :- | :- | :- | :- | :- |
| **Code Review** (o serviço) | revisão gerenciada de todo PR no GitHub, comentários inline | infraestrutura da Anthropic | planos Team e Enterprise, ligado por um Owner | sim, e `CLAUDE.md` |
| **`/code-review`** (alias `/review`) | skill embutida no Claude Code que revisa o diff da sessão | a sua sessão, como subagente em segundo plano | qualquer plano | não, só `CLAUDE.md` |
| **`/code-review ultra`** (alias `/ultrareview`) | frota de agentes numa sandbox na nuvem, cada achado reproduzido | sandbox na nuvem | conta claude.ai; 3 execuções grátis em Pro e Max, depois créditos | não documentado |
| **plugin `code-review`** | comando aberto (Apache 2.0) com agentes nomeados e filtro de confiança | a sua sessão | quem instalar | não, só `CLAUDE.md` |
| **`/simplify`** | revisão só de limpeza, que aplica as correções; não caça bug | a sua sessão | qualquer plano | não |

Fontes: [visão geral] tabela "Compare ways to get a review"; [customizar] nota sobre os dois arquivos; [local]; [ultra]; [comandos]; [plugin]. A tabela da visão geral lista ainda o Claude no seu CI (GitHub Actions, GitLab) e "o seu próprio revisor" como subagente ou skill.

Vizinhos com outra função: `/security-review` (vulnerabilidades no diff), o plugin security-guidance (o Claude revisa o próprio código por vulnerabilidade na mesma sessão) e o plugin Claude Security (varredura do código inteiro) [comandos; índice llms.txt].

## O mecanismo do serviço: quatro estágios

[visão geral] Por padrão o serviço olha **correção**: bug que quebraria produção, e não formatação nem falta de teste. Uma revisão roda em quatro estágios:

1. **Encontrar:** vários agentes examinam o diff e o código em volta, em paralelo.
2. **Conferir:** uma etapa de verificação checa cada achado candidato contra o código e descarta os falsos positivos.
3. **Ordenar:** o que sobra é deduplicado e ordenado por gravidade.
4. **Publicar:** comentários inline nas linhas, um resumo no corpo da revisão e um check run chamado "Claude Code Review".

O diagrama da página resume o mesmo: o PR vai para vários agentes que buscam em paralelo, a verificação derruba falsos positivos, o restante é deduplicado e ranqueado, e o resultado volta ao GitHub.

O que a revisão acessa: lê o diff e o código em volta, **sem compilar nem executar** o código; dentro da revisão o acesso ao repositório é só leitura, ela não faz commit; no PR, posta comentários e o check run, resolve os próprios fios antigos e pode reagir com 👀. O serviço escolhe os modelos e não oferece escolha de modelo; para mudar a profundidade, muda-se o nível [visão geral].

Quem controla: em repositório automático, abrir ou dar push dispara a revisão, menos em rascunho e em PR de fork; o comando por comentário só vale vindo de quem tem escrita no repositório; e as instruções vêm do `REVIEW.md` do branch base ou do padrão, **nunca das mudanças do próprio PR** [visão geral; customizar].

[blog] O post de lançamento descreve o mesmo fluxo: um time de agentes procura bugs em paralelo, verifica para filtrar falso positivo e ranqueia por gravidade; o resultado chega como um comentário geral "de alto sinal" e comentários inline. Acrescenta que **a revisão escala com o PR**: mudança grande ou complexa ganha mais agentes e leitura mais funda; mudança trivial ganha uma passada leve. Tempo médio nos testes deles: cerca de 20 minutos.

**Quantos agentes e com que lentes, no serviço: a documentação não diz.** Fala em "vários agentes" (several agents), "agentes que encontram" e "agentes que verificam" (estes recebem o `REVIEW.md`, ver abaixo), e "a etapa que escreve a revisão final", que consulta o `REVIEW.md` antes de fixar a gravidade e escrever o resumo [customizar]. O changelog confirma que a verificação é feita por agentes, um por achado ou por grupo: na v2.1.268 (10/09/2026) corrigiram revisões que terminavam incompletas "quando um dos agentes que verificam um achado falhava no meio"; agora o agente é substituído e a revisão chega a um veredito. O detalhe de agentes e lentes só aparece aberto no plugin (próxima seção).

## Agentes e lentes no plugin aberto

O plugin `code-review` é o único lugar com o roteiro escrito. Teve duas formas, e a mudança entre elas é o achado mais útil para quem vai desenhar uma revisão.

### Versão 1 (novembro de 2025): cinco lentes e nota de confiança

[plugin v1] Passos, em palavras próprias:

1. Um agente Haiku checa se vale revisar: PR fechado, rascunho, trivial ou automático "obviamente ok", ou já revisado antes. Se sim, para.
2. Outro Haiku lista **os caminhos** (não o conteúdo) dos `CLAUDE.md` relevantes: o da raiz e os das pastas dos arquivos mudados.
3. Um Haiku lê o PR e devolve um resumo da mudança.
4. **Cinco agentes Sonnet em paralelo**, cada um com uma lente, devolvem uma lista de problemas com o motivo de cada um:
   - **#1 conformidade com o `CLAUDE.md`**, com a ressalva de que o `CLAUDE.md` é orientação para quem escreve código e nem toda instrução vale na revisão;
   - **#2 bug óbvio, varredura rasa**: só as mudanças, sem ler contexto extra, foco em bug grande, ignorar miudeza e provável falso positivo;
   - **#3 histórico**: `git blame` e histórico do código mudado, procurando bug à luz desse contexto;
   - **#4 PRs anteriores**: comentários feitos em PRs antigos que mexeram nos mesmos arquivos e que também valeriam para este;
   - **#5 comentários do código**: se a mudança respeita as orientações escritas nos comentários dos arquivos mudados.
5. **Para cada problema, um agente Haiku em paralelo dá uma nota de 0 a 100** de confiança de que é real e não falso positivo, recebendo o PR, a descrição do problema e a lista de `CLAUDE.md`. Se o problema veio do `CLAUDE.md`, o agente confere que o arquivo fala daquilo especificamente. A régua, que o comando manda passar ao agente "verbatim":
   - **0:** nada confiante; falso positivo que não resiste a um exame leve, ou problema que já existia.
   - **25:** algo confiante; pode ser real ou não, o agente não conseguiu verificar; se é de estilo, o `CLAUDE.md` não pede.
   - **50:** moderado; verificou que é real, mas é miudeza ou raro na prática, pouco importante perto do resto do PR.
   - **75:** alto; conferiu duas vezes, muito provavelmente real e vai acontecer; afeta o funcionamento, ou está citado diretamente no `CLAUDE.md`.
   - **100:** certeza; conferiu e confirmou, vai acontecer com frequência, a evidência confirma diretamente.
6. **Descarta tudo abaixo de 80.** Se não sobra nada, para.
7. Um Haiku repete a checagem do passo 1 (o PR ainda está elegível?).
8. Comenta no PR: curto, sem emoji, citando e linkando o código (link com o SHA completo e uma linha de contexto antes e depois).

### Versão atual (dezembro de 2025 em diante): quatro agentes e validação sim ou não

[plugin] A reescrita de 06/12/2025 (commit 9babb8d, "Update the code review prompt") trocou a nota por validação, e é a versão que hoje está em `claude-plugins-official` (o texto original está no repositório, no caminho citado no topo). Passos:

1. Haiku: elegibilidade (fechado, rascunho, trivial, já comentado pelo Claude). Nota: revisar também PR gerado pelo Claude.
2. Haiku: caminhos dos `CLAUDE.md` relevantes.
3. **Sonnet** resume o PR.
4. **Quatro agentes em paralelo**, cada um recebendo também o título e a descrição do PR (para entender a intenção do autor):
   - **#1 e #2: conformidade com o `CLAUDE.md`**, em Sonnet, **dois agentes na mesma lente por redundância** (o README chama de "redundancy for guideline checks"); só vale o `CLAUDE.md` que está no caminho do arquivo ou acima.
   - **#3: bug óbvio, só no diff**, em **Opus**: sem ler contexto extra; não marcar o que não dá para validar sem olhar fora do diff.
   - **#4: problema no código introduzido**, em **Opus**: segurança, lógica errada, sempre dentro do código mudado.
   - Critério para os quatro, em caixa alta no comando: só **alto sinal**. Entra: código que não compila ou não faz parse; código que dá resultado errado qualquer que seja a entrada; violação clara do `CLAUDE.md` em que dá para **citar a regra exata**. Não entra: estilo, problema que depende de entrada ou estado específico, sugestão subjetiva. "If you are not certain an issue is real, do not flag it. False positives erode trust and waste reviewer time."
5. **Para cada problema, subagentes em paralelo validam**: recebem título, descrição do PR e o problema, e confirmam com alta confiança que ele existe (exemplo do comando: se acusaram "variável não definida", conferir no código que ela não está definida; se é regra do `CLAUDE.md`, conferir que a regra vale para aquele arquivo e foi de fato violada). **Opus para bug e lógica, Sonnet para `CLAUDE.md`.** O texto diz "problemas achados pelos agentes 3 e 4", mas os exemplos incluem regra de `CLAUDE.md`; a ambiguidade é do original.
6. **Descarta o que não foi validado.** O que sobra é a lista de alto sinal.
7. Resumo no terminal; se não achou nada, "No issues found. Checked for bugs and CLAUDE.md compliance." Sem `--comment`, para aqui.
8. Com `--comment`: monta para si a lista de comentários antes de postar (não publica a lista).
9. Posta um comentário inline por problema: descrição curta; sugestão "commitável" só para correção pequena e completa (a de 6 linhas ou mais, estrutural ou espalhada, vira descrição); **um comentário por problema único, sem duplicar**.

**Lista de falsos positivos** que vale nas duas versões, para a busca e para a conferência: problema que já existia; algo que parece bug e não é; miudeza que um engenheiro sênior não apontaria; o que linter, typechecker ou compilador pega (sem rodar essas ferramentas: o CI roda); qualidade geral (falta de teste, segurança genérica, documentação) a menos que o `CLAUDE.md` exija; regra do `CLAUDE.md` silenciada no próprio código (comentário de ignore). A v1 tinha mais dois: mudança de comportamento provavelmente intencional ou ligada à mudança maior, e problema real em linha que o autor não mexeu.

**Descompasso no próprio plugin:** o README atual ainda descreve a v1 (nota 0 a 100, limiar 80, "Nx confidence scorers", agente de histórico com `git blame`), enquanto o comando atual valida por sim ou não e não tem agente de histórico. Quem for citar o plugin deve citar o comando, não o README.

Regras de trabalho do comando atual: os agentes partem do princípio de que as ferramentas funcionam e não fazem chamada exploratória; o comando de postar inline exige `confirmed: true`, para que um subagente que herde a ferramenta e "teste" a chamada não publique no PR de verdade (commit db8834b, 12/03/2026). O comando também restringe as ferramentas, no frontmatter, aos comandos `gh` de ler PR e issue, de buscar e de comentar, mais a ferramenta de comentário inline; manda usar o `gh` em vez de buscar páginas na web, começar por uma lista de tarefas e, nos links para o código, usar o SHA completo do commit, com o intervalo de linhas `L<início>-L<fim>` e ao menos uma linha de contexto antes e depois; sem achados e com `--comment`, posta um comentário curto "Code review" que diz que não achou nada.

## Lentes no `/simplify` e no ultrareview

- [comandos] `/simplify`: **quatro agentes em paralelo**, com as lentes **reuso** de helpers que já existem, **simplificação**, **eficiência** e **altitude** (se a mudança está no nível certo de abstração). Não procura bug; aplica as correções.
- [changelog v2.1.196, 29/06/2026] o fluxo do `/code-review` juntou **cinco buscadores de limpeza em um**, cortando cerca de 25% dos tokens.
- [ultra] ultrareview: "uma frota maior" de agentes revisores explora a mudança em paralelo; **cada achado relatado é reproduzido e verificado de forma independente**, por isso o resultado foca em bug real e não em sugestão de estilo. A página não diz quantos agentes nem quais lentes. O resultado chega como "achados verificados", cada um com o local no arquivo e a explicação.

## Gravidade, deduplicação e o que sai na revisão

[no PR] Cada achado leva um de três marcadores:

| Marca | Gravidade | Sentido |
| :- | :- | :- |
| 🔴 | Important | bug que deveria ser corrigido antes do merge |
| 🟡 | Nit | problema menor, vale corrigir mas não bloqueia |
| 🟣 | Pre-existing | bug que já existia no código e não foi introduzido por este PR |

Quando a revisão guardou o raciocínio, o achado tem uma seção recolhida "Why this was flagged", que diz por que foi marcado e **como foi verificado**. O check run lista todos os achados numa tabela ordenada por gravidade (gravidade, arquivo:linha, problema), inclusive os que o GitHub não aceitou como inline; achado sem linha ou fora do diff vai para "Additional findings" no corpo [no PR; problemas]. A última linha do texto do check run é um comentário HTML com as contagens em JSON, por exemplo `{"nit":1,"normal":2,"pre_existing":0}`, em que `normal` é a contagem de Important; a ausência dessa linha deve ser lida como "sem veredito", não como zero achados [no PR].

Deduplicação: o serviço deduplica no estágio de ordenação [visão geral]; o plugin manda "um comentário por problema único" [plugin]. Teto: no `/code-review` local, quando os achados saem pela ferramenta de achados, o limite é 32; `--max-findings` muda (v2.1.288) [local]. O exemplo de `REVIEW.md` também limita nits (abaixo).

**Re-revisão** [no PR]: a revisão disparada por push foca no que mudou desde a anterior e posta menos nits e pré-existentes; o corpo conta o que deixou de fora ("outside the scope of this re-review and not posted"; "found and not posted"). Ela lê as respostas do autor aos achados anteriores e pode resolver o fio ou postar uma réplica; resolve sozinha o fio quando julga o problema corrigido. Se o push não muda as linhas e nenhum Important foi resolvido, o serviço mantém o resultado anterior em vez de revisar de novo ("Code review skipped — no new changes" ou "not repeated — earlier findings still open"). Uma revisão pedida por `@claude review` cobre o PR inteiro de novo. Desde a v2.1.305 (20/10/2026), a re-revisão não abre com "LGTM" enquanto achados bloqueantes anteriores seguem abertos.

## Níveis de profundidade e o que muda entre eles

**No serviço** [visão geral; setup; changelog v2.1.304, 19/10/2026]: três níveis, escolhidos por um Owner para a organização e, se quiser, por repositório (por exemplo, Quick num código rotineiro e Deep num crítico).

| Nível | O que troca |
| :- | :- |
| Quick | passada mais leve; o mais rápido e o mais barato |
| Standard | equilíbrio entre profundidade, velocidade e custo; o padrão |
| Deep | a passada mais completa; a mais demorada e a mais cara |

A documentação não diz o que muda por dentro (número de agentes, lentes, rodadas de verificação); diz só que o custo de cada revisão cresce com o nível, o tamanho da mudança, a complexidade do código em volta e **quantos achados candidatos precisam de verificação** [custos]. A frequência é outro eixo: uma vez ao abrir o PR, a cada push (o padrão de repositório novo, que multiplica o custo pelo número de pushes) ou só por pedido [setup; custos].

**No `/code-review` local** [local; comandos]: o nível de esforço (`low`, `medium`, `high`, `xhigh`, `max`) troca **cobertura por confiança**. Em `low`, a revisão relata só os achados de que tem mais certeza, com menos falsos positivos; de `medium` a `max`, alarga a cobertura. Conforme o modelo e o esforço, cobre também limpeza (reuso, simplificação, eficiência). A descrição da skill embutida, como aparece na lista de skills da sessão, resume a mesma escala como "de poucos achados de alta confiança a muitos, alguns incertos", e pede que `max` e `ultra` só sejam usados quando o usuário ou uma instrução pedir, por serem os mais caros e abrirem muitos subagentes revisores. Detalhes:

- sem nível digitado, reusa o último nível digitado, mesmo de outra sessão; antes da v2.1.223 usava o esforço atual da sessão [local];
- em `medium`, nos modelos sem ajuste próprio de revisão (Opus 5.5 e Sonnet 5.5 inclusive), passou a relatar também achados de limpeza e de convenções do `CLAUDE.md` (v2.1.290, 05/10/2026) [changelog];
- `ultra` escala para a revisão na nuvem; a página compara: `/code-review` leva de segundos a poucos minutos e serve para retorno rápido enquanto se trabalha; o ultra leva de 5 a 15 minutos e serve para "confiança antes do merge" em mudança substancial [ultra];
- a revisão roda como subagente em segundo plano, com contexto próprio, para não encher a conversa; `--fix` aplica os achados no working tree (passando pelo modo de permissão) e `--comment` posta no PR [local];
- no app desktop, os achados chegam num cartão agrupado por arquivo, com "Walk through in diff", "Fix this one" e "Apply fixes"; quando o Claude corrige depois, cada achado é marcado como corrigido, pulado ou sem mudança necessária [desktop; local].

## Como `CLAUDE.md` e `REVIEW.md` personalizam a revisão

[customizar] Dois arquivos, duas funções:

- **`CLAUDE.md`**: as instruções de projeto que o Claude Code lê em toda tarefa. A revisão lê como contexto e **marca como achado a mudança que viola uma regra dele**, na gravidade que couber. Lê o da raiz e os das pastas acima de cada arquivo mudado; o de uma subpasta só entra se o PR mexe em algo ali. Vale para o serviço e para o `/code-review` local.
- **`REVIEW.md`**: instruções só para revisão, lidas só pelo serviço. **Os agentes que encontram e os que verificam recebem o conteúdo** como instruções de revisão do repositório, ao lado da orientação padrão do serviço; a etapa que escreve a revisão final o consulta antes de fixar a gravidade e escrever o resumo. Pode haver um na raiz e outros em subpastas, que **somam** checagens para mudanças naquela pasta.
- Regra de divisão: o que deve valer nos dois lugares vai no `CLAUDE.md`; o `REVIEW.md` fica para o que muda o comportamento da revisão de PR.

**O que escrever no `REVIEW.md`**, organizado pelo sintoma (Markdown livre; muda o que a revisão acha e relata, não o formato):

| Sintoma | Instrução |
| :- | :- |
| O que é marcado como Important não é o que importa | redefinir o que é Important no repositório (a calibração padrão mira código de produção; repositório de docs, de configuração ou protótipo pode querer algo bem mais estreito), dizendo que classes são Important e quais são no máximo Nit; também dá para subir, por exemplo tratar qualquer violação do `CLAUDE.md` como Important |
| Nit demais | limitar quantos nits uma revisão posta, por exemplo no máximo cinco |
| Comentário em arquivo gerado ou no que o CI já checa | listar caminhos e categorias a pular (código gerado, lockfiles, dependências vendorizadas, lint, ortografia); para caminho que merece alguma revisão mas não a completa, subir a barra: "in `scripts/`, only report if near-certain and severe" |
| Uma regra do time não é checada | escrever a regra que deve ser marcada em todo PR, por exemplo "toda rota nova de API tem teste de integração" |
| Achado que se revela errado | **exigir evidência antes de postar uma classe de achado**; o exemplo da doc: afirmação sobre comportamento precisa citar `arquivo:linha` na fonte, não inferir pelo nome, o que corta o falso positivo que custaria uma ida e volta ao autor |

**O exemplo de `REVIEW.md` da documentação** (para um serviço de backend) tem quatro seções: "o que Important quer dizer aqui" (reservado para o que quebra comportamento, vaza dado ou impede rollback: lógica errada, consulta ao banco sem escopo, dado pessoal em log ou mensagem de erro, migração que não é compatível com a versão anterior; estilo, nomes e refatoração são no máximo Nit); "limitar os nits" (no máximo cinco por revisão); "não relatar" (o que o CI já garante, como lint, formatação e erro de tipo; arquivos gerados em `src/gen/` e todo `*.lock`; código de teste que viola regra de produção de propósito); e "sempre checar" (rota nova de API com teste de integração; log sem e-mail, id de usuário ou corpo de requisição; consulta escopada ao tenant de quem chama).

**Inclusões:** uma linha só com `@arquivo.md` no `REVIEW.md` da raiz põe o conteúdo daquele arquivo no lugar. Regras: arquivo na raiz, nome exato sem espaço, um nível só (inclusão dentro de inclusão fica como texto), no máximo oito arquivos, até 150.000 bytes somando tudo (o arquivo que estouraria é pulado inteiro, não cortado), até 64 links Markdown no conjunto (passou disso, o `REVIEW.md` da raiz inteiro é ignorado). O serviço também troca alguns caracteres do texto da skill (colchetes, sinal de menor, barra vertical, arroba), então a regra que depende deles deve ser dita também em palavras.

**De onde o `REVIEW.md` é lido, e por quê:** do branch base ou do padrão, **nunca das mudanças do PR**; para mudar a revisão, é preciso fazer merge do `REVIEW.md` antes. Com o branch padrão protegido, a revisão honra as instruções que **afrouxam** a revisão: baixar a gravidade de um achado, excluir caminhos, arquivos ou classes de problema, e limitar nits. Sem proteção, lê só o arquivo da raiz; se não consegue confirmar a proteção, não lê nenhum. A doc não escreve o motivo, mas o desenho impede que um PR reescreva as regras da sua própria revisão. Da mesma forma, desde a v2.1.292 (06/10/2026), quando o PR edita um `CLAUDE.md` a revisão usa a versão do branch base [changelog].

[plugin] No plugin, a personalização é editar o próprio comando: trocar o 80 do limiar (na v1) ou acrescentar agentes de segurança, desempenho, acessibilidade ou documentação; e o README recomenda `CLAUDE.md` específicos e atualizar o `CLAUDE.md` com os padrões que se repetem nas revisões.

[local] O `/code-review` é skill embutida, sem `SKILL.md` em disco para editar: as regras do projeto entram pelo `CLAUDE.md`; uma skill de projeto ou pessoal chamada `code-review` substitui a embutida (o alias `/review` continua chamando a embutida); ou escreve-se o próprio revisor como subagente ou skill.

## O que a revisão nunca faz

- **Não aprova e não bloqueia o PR**; a decisão de merge fica com o time [visão geral; no PR]. O check run termina como neutro (ou pulado), **nunca como falha**, então uma revisão terminada não derruba um check obrigatório. Quem quer travar o merge lê as contagens e decide no próprio CI [no PR].
- Não executa nem compila o código; não faz commit; dentro da revisão, só lê [visão geral].
- Não responde na hora à réplica do autor; a próxima revisão lê as réplicas [no PR].
- O post de lançamento diz o mesmo: "It won't approve PRs — that's still a human call" [blog].
- O ultrareview que posta no PR posta um comentário simples da conta do usuário, que "não é uma revisão nem uma aprovação", e só quando o usuário escolhe naquela execução [ultra].
- O Claude não inicia um ultrareview sozinho [ultra]; o `/code-review` comum pode ser iniciado pelo Claude quando pedido em linguagem natural, e isso se desliga com `skillOverrides` [local].
- Nenhum achado não quer dizer código correto: "A review with no findings doesn't mean your code is error-free or secure" [visão geral].

## Números, com a fonte

Todos do post de lançamento [blog], medidos pela própria Anthropic em uso interno, sem método descrito:

- Antes do Code Review, **16%** dos PRs internos recebiam comentários de revisão substantivos; com ele, **54%**.
- PRs grandes (mais de 1.000 linhas mudadas): **84%** recebem achados, **7,5** problemas em média. PRs pequenos (menos de 50 linhas): **31%**, **0,5** problema em média.
- **Menos de 1%** dos achados são marcados como incorretos pelos engenheiros. É a única medida de falso positivo publicada, e mede o que o engenheiro marcou como errado, não uma conferência independente.
- Produção de código por engenheiro da Anthropic cresceu **200%** em um ano (o motivo do produto: a revisão virou gargalo).
- Custo médio por revisão: **US$ 15 a 25**, crescendo com tamanho e complexidade; revisão média de cerca de **20 minutos**.
- Dois casos: uma mudança de uma linha num serviço de produção, que normalmente passaria com aprovação rápida, foi marcada como crítica porque quebraria a autenticação; num refactor de criptografia ZFS do TrueNAS (código aberto), a revisão achou um bug **pré-existente** no código vizinho, um tipo errado que apagava o cache de chaves a cada sincronização.

Da documentação: ultrareview custa tipicamente **US$ 5 a 25** em créditos depois das 3 execuções grátis (Pro e Max, uma vez por conta) e leva **5 a 15 minutos**; aceita até **500 arquivos e 8.000 linhas** mudadas por padrão [ultra]. O serviço não tem preço fixo por revisão; a recomendação é um piloto com teto de gasto, medindo o custo médio por repositório [custos].

## O que mudou entre versões

- **09/03/2026**: serviço lançado em research preview para Team e Enterprise [blog].
- **Plugin**: v1 em 11/2025 (5 Sonnet com lentes, nota 0 a 100 por Haiku, limiar 80); reescrita em 06/12/2025 (4 agentes, Opus nos bugs, validação sim ou não, Opus ou Sonnet conforme o tipo); comentários inline com sugestão em 12/2025; `confirmed: true` em 03/2026; migrado para `claude-plugins-official` em 26/10/2026 [plugin v1; plugin; histórico do GitHub].
- **Ultrareview**: research preview em 20 a 24/04/2026 [whats-new semana 17]; passou a ser `/code-review ultra`, com `/ultrareview` como alias [ultra].
- **v2.1.147 (21/05/2026)**: o antigo `/simplify` virou `/code-review`, que relata bugs de correção num nível de esforço escolhido, com `--comment` [changelog; whats-new semana 21]. v2.1.152: `--fix`. v2.1.154 (28/05): `/simplify` volta como revisão só de limpeza, que aplica as correções.
- **Junho e julho de 2026**: `/review <pr>` passou a usar o mesmo motor do `/code-review medium` (v2.1.186), voltou a ser passada única e rápida (v2.1.202) e, na v2.1.223, virou alias do `/code-review` [changelog; local]. Cinco buscadores de limpeza viram um, 25% menos tokens (v2.1.196). Por um tempo o Claude deixou de rodar o `/code-review` sozinho (v2.1.215); desde a v2.1.246 pode, salvo `skillOverrides` [local].
- **Setembro e outubro de 2026, no serviço**: agente de verificação que falha é substituído (v2.1.268); `--max-findings` (v2.1.288); limpeza e convenções do `CLAUDE.md` em `medium` (v2.1.290); `CLAUDE.md` lido do branch base (v2.1.292); **níveis Quick, Standard e Deep (v2.1.304)**; sem "LGTM" com bloqueante aberto (v2.1.305); `@claude review stop` (v2.1.307); antes de julho de 2026, `@claude review` inscrevia o PR nos pushes seguintes, e agora isso é `@claude review always` [no PR; changelog].

## Limites declarados

- A revisão usa IA e pode deixar passar bug, vulnerabilidade e outros problemas [visão geral].
- O serviço não está disponível com retenção zero de dados, configuração HIPAA ou chave de criptografia do cliente, nem fora do GitHub [visão geral].
- O ultrareview é research preview: recurso, preço e disponibilidade podem mudar [ultra].
- Os números do blog são internos da Anthropic, sem descrição de método nem grupo de comparação.
- A documentação descreve o comportamento e não o desenho interno do serviço: número de agentes, lentes e o que cada nível muda por dentro ficam sem resposta; o plugin aberto é a única versão escrita, e é outro produto.
