# A memória e a evolução do ambiente

## O recorte: o que é seu fica na sua memória; o que vale para o repositório vira decisão versionada

**Decisão:** o ambiente melhora por três caminhos, cada um com o seu lugar:

- **O seu feedback sobre como trabalhar** ("prefiro a resposta curta", "confira a data antes de datar") vai à memória do Claude Code: a pasta local `~/.claude/projects/<repositório>/memory/`, uma memória por fato, com o porquê e como aplicar. Ela fica no seu computador e não vai ao git.
- **O que vale para o repositório inteiro** (uma regra de trabalho, uma convenção que qualquer sessão deve seguir) vai a `decisions/`, com o porquê, e ao `CLAUDE.md` quando muda o roteiro.
- **O que é sobre uma skill** segue a regra de `licoes-das-skills.md`: a regra que você dá entra no `SKILL.md`; a falha que você aponta sem dar a regra vai ao `licoes.md` da skill, como aberta; a skill de revisão só mede a si mesma com a issue de reavaliação aberta (o número no `references/projeto.md` dela).

**Motivo:** a memória guarda o jeito de trabalhar que o Claude não acha nos arquivos, e se perde se o disco falhar ou se você trocar de computador. O que é regra do repositório precisa estar versionado e com o porquê, para que nenhuma sessão o redescubra e para que a regra se reveja quando o porquê deixar de valer.

## O espelho da memória, opcional e desligado

**Decisão:** o repositório traz o `.claude/hooks/espelhar-assistente.py`, que copia a memória, o `~/.claude/settings.json` e a `statusline.js` para `assistant/` e confere cada arquivo por sha256. Ele vem **desligado**: nada roda até você ligá-lo (como ligar em [`assistant/README.md`](../assistant/README.md)).

**O recorte:** entram as memórias, o `settings.json` (só se não tiver um bloco `"env"`, onde costumam morar chaves) e a `statusline.js`. Ficam fora o `~/.claude/mcp.json`, que pode trazer token, as credenciais, os caches, o histórico das conversas e as skills que vêm da conta.

**Motivo:** sem cópia, a memória existe só no seu computador. Com o espelho, ela entra no histórico do git com o resto do repositório, e se restaura numa máquina nova.

**O risco aceito, e por que vem desligado:** a memória vai ao git. **Só ligue se o seu repositório for privado**: num repositório público, as suas preferências e o que você contou ao assistente ficariam abertos. O `scripts/confere_dados.py` ajuda a conferir antes do push.

**Revê se:** o Claude Code passar a guardar a memória dentro do próprio repositório, ou a oferecer cópia da memória por conta própria.
