# Modelos de pedido e de entrega

Troque o que está entre `<>`. Redija os pedidos em português, completos: o agente não viu a conversa. O nível rápido usa o modelo de achar, só com as lentes dele.

## Achar (Etapa 1)

```
Você revisa um trabalho que não fez e de cujo contexto não participou.
Raiz do projeto: a pasta em que você está (o diretório de trabalho); os caminhos abaixo partem dela.
Trabalho revisado: <caminho ou texto>. Foi feito a partir de: <fontes, arquivos>.
Régua que vale para ele: <arquivos de regra; sempre inclua os READMEs da área e o CLAUDE.md da raiz>.
<Quando a lente "o pedido" está entre as escolhidas: pedido de origem, para ela: <a issue, com corpo e comentários, já na pasta temporária como arquivo: <caminho>; ou o pedido da pessoa, por escrito>. Sem pedido escrito, apague a linha, tire "o pedido" da lista numerada de lentes abaixo e do campo "lentes" do registro.>

Passe o trabalho por estas lentes, uma de cada vez. Cada lente aponta o que achar; nenhuma é obrigada a discordar (se pelo ângulo dela o trabalho se sustenta, diga):
1. Régua: <pergunta do catálogo>
<2..n: as lentes da etapa, com a pergunta de cada uma>

Para cada achado: lente; trecho do trabalho (linha); o problema; a evidência (arquivo e linha da fonte ou o texto da regra); o tipo (afirmação errada, desvio da régua, lacuna, premissa); a gravidade sugerida (crítica: afirma algo errado ou fere regra que barra a entrega; maior: induz decisão errada ou omite o que muda a conclusão; menor: imprecisão que não muda a conclusão; estilo); e uma sugestão de correção em uma frase; nos de gravidade sugerida crítica ou maior, também o "se pularmos": o que acontece, em uma frase, se a correção não entrar.
Se o problema já existia antes deste trabalho (estava no arquivo ou no projeto antes dele; confira no `git log` ou na versão anterior), marque o achado como pré-existente.
Abra a fonte no trecho antes de afirmar um erro de número ou atribuição. Leia a fonte primária inteira no trecho relevante (a seção ou a página em volta), e não só a linha que o trabalho cita: procure a linha que contradiz. Só leitura: não edite nada.
<Se o trabalho pode mudar enquanto a revisão roda, diga aqui; senão, apague a linha.>
<Sempre: "Pode ler as pastas `originals/` se precisar; não copie de lá para o repositório nem para a sua entrega nenhum trecho de mensagem, e-mail ou conversa de terceiro, e de texto protegido só a citação curta que a régua da fonte permite.">
<O que só uma ferramenta do assistente lê (banco de artifact, MCP, `gh` com corpo e comentários) já está na pasta temporária como arquivo: <caminho>. Senão, apague a linha.>
<No nível rápido: só as lentes do nível, régua e fidelidade (mais efeito nas outras skills, na edição de skill); confira cada crítico e maior no trecho da fonte antes de entregar; os menores de certeza alta vão numa lista à parte, ditos como não conferidos; o resto não entra. Senão, apague a linha.>
<No modo por amostra (ingestão em lote): a amostra é <quais fichas, quantas e por que essas>; o `parafrase.py` já rodou em todas (<resultado>); passe a lente da régua (frontmatter, licença, a régua de `knowledge/sources/README.md`) em todas as fichas do lote, e a fidelidade e o conteúdo próprio só na amostra; não generalize o que a amostra achou para as fichas fora dela. Senão, apague a linha.>
Grave em <pasta temporária>/<pasta-da-revisao>/achados.md <no profundo, um arquivo por agente: achados-<lente>.md> <no padrão e no profundo: "e devolva só a contagem por gravidade sugerida e o caminho do arquivo; se não houver crítico, maior nem menor, devolva o texto inteiro"; no rápido: "e devolva o mesmo texto">.
```

## Re-revisão (Etapa 1, quando o trabalho volta corrigido)

```
Você revisa a nova versão de um trabalho que já passou por uma revisão; não fez o trabalho nem a revisão anterior.
Raiz do projeto: a pasta em que você está (o diretório de trabalho); os caminhos abaixo partem dela. Trabalho: <caminho>. O que mudou desde a revisão anterior: <git diff ... ou a lista de arquivos e trechos>.
Achados da revisão anterior: <pasta temporária>/<pasta-da-revisao-anterior>/achados.md (e conferencia.md, com os vereditos).
O que a pessoa decidiu: aprovou <lista>; recusou <lista>.
Régua: <a mesma da revisão anterior>.
<O que só uma ferramenta do assistente lê já está na pasta temporária como arquivo: <caminho>. Senão, apague a linha.>
<Sempre: "Pode ler as pastas `originals/` se precisar; não copie de lá para o repositório nem para a sua entrega nenhum trecho de mensagem, e-mail ou conversa de terceiro, e de texto protegido só a citação curta que a régua da fonte permite.">

Responda só a três perguntas, sem reler o que não mudou:
1. Cada achado que a pessoa aprovou foi resolvido? Para cada um: resolvido, resolvido em parte (o que falta) ou não resolvido; e se a correção criou outro problema. Os que ele recusou não se reabrem: liste-os como "mantido por decisão da pessoa".
2. O que mudou traz problema novo? Passe só os trechos mudados pelas lentes: <as mesmas da revisão anterior>. O achado novo que só existe por causa de uma correção, e que reverter a correção resolveria, sai marcado "churn", com o número do achado original que a correção atendia.
3. Zoom out: o que as correções acrescentaram sem precisar (a ressalva defensiva, a explicação que só o revisor pedia, a regra repetida)? Olhe só o que elas acrescentaram.
Para cada achado novo, o mesmo formato de sempre (lente, trecho, problema, evidência, tipo, gravidade sugerida, sugestão de correção, e pré-existente se o problema já estava antes do trabalho revisado, não só antes das correções).
Os críticos e maiores que você achar, e os seus vereditos de resolvido deles, vão à conferência de outro agente: não os dê como conferidos.
<Re-revisão conjunta de duas frentes do mesmo passo: responda às três perguntas para cada frente, em seções separadas. Senão, apague a linha.>
Só leitura. Grave em <pasta temporária>/<pasta-da-revisao>/achados.md e devolva só a contagem por gravidade sugerida e o caminho do arquivo; se não houver crítico nem maior, novo ou de resolvido, devolva o texto inteiro.
```

## Conferir (Etapa 2)

```
Você confere achados de uma revisão; não acha problemas novos e não participou do trabalho nem da busca.
Raiz do projeto: a pasta em que você está (o diretório de trabalho); os caminhos abaixo partem dela. Trabalho: <caminho>. Achados: <pasta temporária>/<pasta-da-revisao>/achados.md <no profundo: todos os achados-<lente>.md>. <No trabalho misto: achados de código em <pasta temporária>/<pasta-da-revisao>/codigo.md, ou no texto do `/code-review` gravado ali. Senão, apague.>

Confira cada achado de gravidade crítica, maior ou menor (pule os de estilo), abrindo o trabalho e a fonte no trecho, com a pergunta do tipo dele:
- afirmação errada: primeiro leia o que a fonte diz no trecho, sem olhar o trabalho; depois compare;
- desvio da régua: o trabalho fere a regra, cujo texto exato está citado? Sim ou não;
- lacuna: a lacuna existe, e incluí-la muda a conclusão ou a decisão? Na sobra da lente "o pedido": o pedido, citado na linha, pediu isto?
- premissa: o problema de partida ainda vale, conferido no arquivo ou no estado atual?
- pré-existente (marca, além do tipo): o problema já estava antes deste trabalho? Confira no `git log` ou na versão anterior do arquivo.
- na re-revisão, cada veredito de resolvido dos críticos e maiores anteriores: a correção aprovada está no trabalho e resolve o achado, sem criar outro problema? Confira no trecho mudado.
Em todo achado conferido, julgue também a sugestão de correção do achador: ela resolve sem criar outro problema, e o que ela acrescenta serve ao leitor real do trabalho, não só a um revisor sem contexto? Se não, diga a certa em uma frase.
Veredito: confirma; confirma em parte (diga o que muda na gravidade ou no detalhe); não confirma; ou "a prova está com a pessoa", só quando você nomeia a prova que decidiria o achado e ela está fora do que você pode abrir (uma decisão dita só na conversa, um comentário que não veio no pedido, um artifact): diga qual é a prova. A dúvida pela evidência fraca, com a fonte aberta, é "não confirma". Para os vereditos de resolvido, o confirma vale sobre o veredito do achador ("confirmo que está resolvido" ou "confirmo que não está"); se discordar, diga qual é o certo. Na dúvida, não confirme.

<Só na re-revisão: confira só os críticos e maiores, novos e vereditos de resolvido; os menores resolvidos e os menores novos entram listados, sem conferência. Senão, apague a linha.>
<Os achados de código que vieram com execução e cenário concreto (<quais>) não passam por aqui: confira só os outros. Senão, apague a linha.>
Saída: uma linha por achado (número, veredito, porquê com arquivo e linha, juízo da sugestão, e o "se pularmos" do achador nos críticos e maiores, corrigido se for o caso) e, no fim, os confirmados por gravidade, os de "a prova está com a pessoa" e, copiados sem conferir, os de estilo (e, na re-revisão, os menores) do arquivo de achados e os de código com execução e cenário do `codigo.md`, para a entrega sair só deste arquivo.
Leia a versão atual do trabalho: se ela difere da que o achador leu, diga, e julgue pela atual.
<Sempre: "Pode ler as pastas `originals/` se precisar; não copie de lá para o repositório nem para a sua entrega nenhum trecho de mensagem, e-mail ou conversa de terceiro, e de texto protegido só a citação curta que a régua da fonte permite.">
Só leitura. Grave em <pasta temporária>/<pasta-da-revisao>/conferencia.md e devolva o mesmo texto.
```

## Código, no lugar do `/code-review`

Só quando o `/code-review` médio falhar: sem resposta, erro, ou resposta que não é achado nem `(none)`; o baixo que falha assim passa antes pelo médio (`codigo.md`).

```
Você revisa código que não escreveu e de cujo contexto não participou.
Raiz do projeto: a pasta em que você está (o diretório de trabalho); os caminhos abaixo partem dela.
Código: <caminhos exatos dos arquivos>. O que ele deve fazer: <uma ou duas frases, ou o SKILL.md que o chama>.
Procure bugs de lógica e casos de borda (entrada vazia ou fora do formato, falha de chamada externa, contagem e índice, encoding e fim de linha no Windows), não estilo.
Para cada achado: arquivo e linha; o problema; um cenário concreto (a entrada e o que sai errado), rodado quando der, com o comando e a saída; a gravidade sugerida (crítica, maior, menor, estilo); e uma sugestão de correção em uma frase. Se não achar nada, diga "nada encontrado".
<Sempre: "Pode ler as pastas `originals/` se precisar; não copie de lá para o repositório nem para a sua entrega nenhum trecho de mensagem, e-mail ou conversa de terceiro, e de texto protegido só a citação curta que a régua da fonte permite.">
Não edite os arquivos; rode só o que não grava fora de <pasta temporária>. Grave em <pasta temporária>/<pasta-da-revisao>/codigo.md e devolva o mesmo texto.
```

## Entrega (Etapa 3)

```
## Revisão (<nível>): <o que foi revisado>

<Uma frase: quantos achados, quantos confirmados, quantos derrubados, quantos pré-existentes.>

### Para decidir

**Crítica**
- <achado> (<lugar>). Por quê: <...>. Evidência: <arquivo:linha>. Se pularmos: <o que acontece, em uma frase>. Sugestão: <o que mudaria, em uma frase>.

**Maior**
- ...

**A prova está com a pessoa** (críticos e maiores; o conferente não pôde abrir a prova que decide o achado; Etapa 2; os menores vão à tabela abaixo, com a marca)
- <achado> (<lugar>). A prova que falta: <qual>.

**Pares do "churn"** (só na re-revisão: o achado novo que reverter a correção resolveria, ao lado do original; só os pares com crítico ou maior; o par só de menores, com delegação, se aplica direto, e sem ela vai à tabela de aprovar em bloco)
- <original> → <correção> → <novo>. Sugestão: <...>.

<Quando a lente "o pedido" estava entre as escolhidas: "O pedido: <N> achados, o pior é <...>." ou "O pedido: ficou de fora, sem pedido escrito.", ao lado da régua.>

**Com delegação, de qualquer gravidade: muda conclusão, regra ou destino, ou reescreve texto que a pessoa aceitou ou decidiu** (Etapa 3; só quando o processo aplica antes da validação)
- ...

### Para aprovar em bloco

| Onde | O quê (no menor com "a prova está com a pessoa", a marca e a prova que falta) | Sugestão |
|---|---|---|
| <arquivo:linha> | <o problema, curto> | <a correção, curta> |

**Menores de certeza alta, não conferidos** (no nível rápido e nos menores novos da re-revisão; no padrão, os menores vão à tabela acima): <lista curta: onde, o quê, sugestão>.

**Estilo** (não conferidos, numa linha): <...>.

**Pré-existentes** (não foram criados por este trabalho): <cada um com o lugar e o destino sugerido: corrigir junto, lição ou issue>.

**Aplicado antes da validação** (só com delegação, Etapa 3; preenche quem aplicou, ao mostrar à pessoa): <o que entrou, e o arquivo dos achados>.

**Derrubados na conferência:** <número e, para cada um, o motivo em poucas palavras>.
**Resolvidos por quem chamou** (a prova estava com a pessoa e veio escrita; Etapa 2): <cada um, com a prova citada (arquivo e linha, o comentário, a decisão registrada) e o resultado: caiu; ou se confirmou e foi ao bloco da gravidade dele>.
**Não conferido:** <o que ficou de fora e por quê>.
**Não rodou:** <a etapa cujo agente falhou duas vezes, ou "nenhuma"; Etapa 1>.
```

Na re-revisão, a entrega começa por uma linha com os achados anteriores resolvidos, em parte, não resolvidos e mantidos por decisão da pessoa, e segue com os novos nos mesmos blocos.
