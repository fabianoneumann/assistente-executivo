---
titulo: "Memory tool (Claude API): memória em arquivos, do lado do cliente, entre conversas"
tipo: artigo
autor: "Anthropic"
url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md"
capturado_em: 2026-10-30
licenca: "Documentação da plataforma Claude: sem licença aberta; o rodapé de direitos não aparece na cópia em markdown lida, e ela é tratada como protegida, como a documentação do Claude Code (2026-10-29-claude-code-code-review-documentacao); entra só a ficha."
areas: [anthropic-claude, agent-engineering]
tags: [claude-api, memory-tool, agent-memory, context-engineering, compaction, long-running-agents]
---

Ficha de estudo, em palavras próprias, da página oficial da ferramenta de memória da API, lida em markdown em 2026-10-30, na ordem dela. Ferramenta de disponibilidade geral (sem cabeçalho de beta), em todos os modelos a partir do Claude 4. Interessa aqui como o equivalente, na API, da memória automática do Claude Code ([[2026-10-30-claude-code-memoria-claude-md-e-memoria-automatica]]). Os exemplos de código por linguagem (cURL, Python, TypeScript, C#, Go, Java, PHP, Ruby) entram descritos, não transcritos.

## O que é

O Claude cria, lê, atualiza e apaga arquivos numa pasta de memória que persiste entre sessões, acumulando conhecimento sem manter tudo na janela de contexto. Serve à recuperação **na hora** (just-in-time): em vez de carregar tudo no começo, o agente registra o que aprende e relê sob demanda. Casos de uso da doc: manter o contexto de um projeto entre sessões; "apply lessons from past interactions, decisions, and feedback to new tasks"; montar uma base de conhecimento com o tempo.

## Como funciona

- **Do lado do cliente:** o Claude só pede as operações; a aplicação as executa no armazenamento que ela controla (pasta por usuário, banco de dados) e devolve o resultado. `/memories` é um prefixo que a aplicação mapeia para o armazenamento real. Uma conversa futura continua da mesma memória se mandar a mesma ferramenta e a aplicação servir o mesmo armazenamento.
- **Com a ferramenta ligada, o Claude confere a pasta de memória antes de começar uma tarefa.** A API acrescenta sozinha ao prompt de sistema um protocolo: olhar a memória antes de tudo, registrar status e progresso enquanto trabalha, e "assumir interrupção" (a janela pode ser zerada a qualquer momento, e o que não estiver na memória se perde). A descrição da ferramenta já pede para manter a pasta organizada; a doc dá um reforço opcional (manter atualizado, coerente e organizado; renomear ou apagar o que não serve; não criar arquivo sem necessidade) e sugere limitar o tema do que se grava.
- **Exemplo da doc:** um pedido de atendimento ao cliente; o Claude abre a pasta `/memories`, vê dois arquivos (diretrizes de atendimento e políticas de reembolso), lê o primeiro e responde com base nele.
- **Começar:** acrescentar a ferramenta ao pedido (a entrada `memory_20250818` com o nome `memory` é toda a configuração) e implementar no cliente um tratador para cada comando, que recuse caminhos fora de `/memories`. Os SDKs de Python, TypeScript, C# e Java trazem auxiliares (e o executor de ferramentas do namespace beta, embora a ferramenta não exija cabeçalho de beta); Python e TypeScript têm uma implementação pronta em sistema de arquivos local; Go, Ruby e PHP rodam o laço de ferramentas à mão, com armazenamento em memória só para demonstração.
- **Comandos e retornos de referência** (o Claude lê qualquer texto que a aplicação devolver, então os textos podem mudar):
  - **ver:** pasta até dois níveis, com tamanhos legíveis, sem itens ocultos nem `node_modules`; ou arquivo com números de linha (6 caracteres, alinhados à direita, começando em 1), com intervalo opcional; erro acima de 999.999 linhas; a primeira visão de um store vazio não é erro. A descrição da ferramenta diz que ela mostra imagens (jpg, png) e corta a visão de texto acima de 16 mil caracteres, então espere pedidos por intervalo.
  - **criar:** erro se o arquivo existe (a descrição diz "cria ou sobrescreve"; sobrescrever também é escolha válida).
  - **substituir texto:** o texto antigo tem de aparecer uma única vez (senão, erro com as linhas das ocorrências); o novo é opcional (sem ele, apaga).
  - **inserir:** depois da linha indicada (0 = no começo); erro com linha fora do intervalo.
  - **apagar:** arquivo ou pasta, recursivo; recusar apagar a própria `/memories`.
  - **renomear:** recusar se o destino existe e se a origem é a própria `/memories`.

## Segurança

A aplicação responde por tudo: o Claude em geral se recusa a gravar informação sensível, mas a doc recomenda validar e tirar dados sensíveis antes de gravar; limitar o tamanho dos arquivos e do que o "ver" devolve; apagar periodicamente arquivos sem acesso há muito tempo; e validar todo caminho contra fuga da pasta (`../`, codificação em URL), resolvendo para a forma canônica.

## Erros

O mesmo padrão da ferramenta de edição de texto: o resultado da ferramenta volta marcado como erro, com a mensagem no conteúdo.

## Com edição de contexto e compactação

A memória combina com a edição de contexto (limpa resultados de ferramenta no cliente) e com a compactação (resume a conversa no servidor perto do limite): a compactação mantém o contexto ativo pequeno, e a memória guarda o que precisa sobreviver ao resumo.

## Padrão para desenvolvimento em várias sessões

1. Uma **sessão inicial** monta os arquivos de memória antes do trabalho: registro de progresso, lista de funcionalidades (o escopo) e a referência ao script de inicialização do projeto.
2. Cada sessão seguinte **abre lendo** esses arquivos, sem reexplorar o código nem refazer decisões.
3. Antes de terminar, a sessão **atualiza o registro** com o que foi feito e o que falta.

Princípio: uma funcionalidade por vez, marcada como pronta só depois de conferida de ponta a ponta, não quando o código foi escrito. A doc aponta um post de engenharia da Anthropic sobre harness para agentes de longa duração.

## Disponibilidade e dados

Disponível em todos os modelos, na API e nas nuvens parceiras (Bedrock, Google Cloud, Foundry, plataforma na AWS); elegível para retenção zero de dados (exceto nos modelos cobertos por exigência própria) e para HIPAA, porque o armazenamento é do cliente e a retenção é dele.
