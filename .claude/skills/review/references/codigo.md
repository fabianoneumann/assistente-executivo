# Código: o `/code-review`, o substituto e o Codex

Os caminhos `scripts/...` e `references/...` partem da pasta da skill; os links com `./` ou `../`, do próprio arquivo; os demais caminhos, da raiz do projeto.

**Código.** O que é código (script, teste, programa) vai ao `/code-review` do Claude Code (ferramenta Skill, `code-review`, com o nível e os caminhos), que é o padrão; `max` e `ultra` só por pedido da pessoa. O nível baixo lê só o diff, numa chamada, sem abrir o arquivo inteiro, pula os trechos de teste e de fixture, entrega poucos achados sem conferência e responde `(none)` quando nada se qualifica. Daí três regras:
- **Script novo, ainda fora do git:** antes do `/code-review`, marcar o arquivo com `git add -N <caminho>`, para ele entrar inteiro no diff, e passar o caminho no alvo (`/code-review low <caminho>`); sem a marca, o arquivo não versionado fica fora do diff. Antes de rodar, conferir com `git diff HEAD --stat -- <caminho>` que o arquivo está no diff. Logo depois do `/code-review`, desmarcar com `git reset <caminho>`, vá ele ou não ao git: com a marca no índice, o `git pull` com autostash e o `git stash` falham, e um `git commit -a` leva o arquivo. Arquivo fora do repositório (a pasta temporária) não aceita a marca e vai ao médio; se o médio devolver `(none)` nesse caso, use o substituto.
- **Código como trabalho principal** (o script é a entrega, não um ajuste dentro de um trabalho de texto), e o teste novo, que o baixo pula: nível médio. O baixo fica para o ajuste, e é o de menos falsos positivos pela documentação.
- **`(none)` no baixo** quer dizer "nada no trecho do diff": conta como revisão do que mudou, não do arquivo inteiro, e a entrega e o registro dizem isso.
O agente `general-purpose` com o modelo "Código, no lugar do `/code-review`" de [`prompts.md`](./prompts.md) entra só se o médio falhar (sem resposta, erro, ou resposta que não é achado nem `(none)`); se o baixo falhar desse jeito, rode o médio antes. O substituto vai dito na entrega e no registro como substituto. Por quê: o baixo responde `(none)` depois de ler só o diff, como manda o pedido dele, e rodar de novo repete o resultado; o substituto, que lê o arquivo inteiro, acha mais, a um custo um pouco maior.

Os achados do `/code-review` também passam pela conferência, porque no médio vêm sem verificação e parte deles cai. Texto, regra, rubrica e instrução de skill ficam com esta skill, e a lente "executor" continua rodando os comandos escritos no markdown. Trabalho misto passa pelos dois, e os achados do `/code-review` entram na Etapa 2 como os do agente que acha, com a mesma conferência. Por quê: cada um pega o que o outro não pega (o `/code-review`, os erros de lógica; esta skill, os problemas de texto e de regra). Detalhe em `decisions/revisao-de-texto-e-de-codigo.md`.

**O Codex como segunda revisão de código (opcional, pede o Codex CLI com login):** ao lado do `/code-review`, sem substituí-lo, o Codex revisa o mesmo código num perfil só leitura, numa pasta isolada que leva só os arquivos revisados e o que eles importam, nunca o projeto inteiro. Os achados dele entram na Etapa 2 com os do `/code-review`, na mesma conferência, e a entrega os diz à parte ("Codex N / confirmados / derrubados"). Por quê: um segundo modelo traz achados que o `/code-review` e a revisão Claude não trazem, sem substituí-los, e custa pouco. Sem o Codex (não instalado, sem login, fora do ar), a revisão segue sem ele e a entrega diz que ele não rodou.

O comando e o perfil:

```
codex exec --skip-git-repo-check --ephemeral -p <perfil> -C <pasta isolada> -o <pasta>/achados-codex.md - < <pasta>/pedido.md
```

O `<perfil>` é um perfil só leitura do Codex, criado uma vez por pessoa em `~/.codex/<nome>.config.toml` (por exemplo, `~/.codex/revisao.config.toml`, usado com `-p revisao`):

```toml
sandbox_mode = "read-only"
approval_policy = "never"

[features]
apps = false
```

O `read-only` impede o Codex de gravar; o `never` faz ele não parar pedindo aprovação no meio do `exec`; e o `apps = false` desliga os conectores da conta, que a revisão não precisa. A `<pasta isolada>` se monta na pasta temporária só com os arquivos revisados e o que eles importam (no código) ou com o trabalho, as fontes e a régua (no texto), nunca o projeto inteiro: o Codex lê só o que a revisão precisa, e nada de `.env`, `settings.local.json` ou `originals/` vai junto.

**O Codex também no texto (opcional):** na revisão de texto de peça e de pesquisa, no padrão e no rápido, o Codex pode ler o mesmo trabalho que o agente que acha, com o mesmo pedido, sem ver os achados dele, numa pasta isolada com o trabalho, as fontes que ele cita e a régua da etapa (só o que o trabalho precisa, nunca o projeto inteiro). Os achados dele vão à mesma conferência da Etapa 2, e o registro os diz à parte. Os dois leem cada um sozinho, sem conversar antes de conferir: o debate entre agentes não supera a leitura independente, e o ganho de misturar modelos vem das perguntas que só um acerta. Ele soma, não substitui: tende a achar atribuição e régua que a revisão Claude perde, e a perder premissa e coerência que ela acha.
