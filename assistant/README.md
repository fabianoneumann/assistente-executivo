# O espelho do assistente (opcional, desligado)

Cópia, no repositório, do que faz o assistente trabalhar do seu jeito e que só existe no seu computador: as memórias do Claude Code deste projeto e a configuração dele. O porquê e o recorte estão em [`decisions/memoria-e-evolucao.md`](../decisions/memoria-e-evolucao.md).

> **Só ligue se o seu repositório for privado.** As memórias vão ao git com o resto. Num repositório público, as suas preferências e o que você contou ao assistente ficariam abertos.

## Como ligar

1. Confira que o repositório é privado (no GitHub, **Settings** > **General** > **Danger Zone** mostra a visibilidade).
2. Rode uma vez à mão e leia o que foi copiado: `python -X utf8 .claude/hooks/espelhar-assistente.py`. Abra `assistant/memory/` e `assistant/config/` antes do primeiro commit.
3. Para rodar sozinho a cada sessão, acrescente ao `.claude/settings.json` os hooks `SessionStart` e `SessionEnd` com o comando `python -X utf8 .claude/hooks/espelhar-assistente.py --hook`.

## O que entra e o que fica fora

| Entra | Fica fora |
|---|---|
| `memory/`: as memórias do projeto e o índice `MEMORY.md`, byte a byte | o `~/.claude/mcp.json`, que pode trazer token |
| `config/settings.json`, só se não tiver um bloco `"env"` | as credenciais, os caches e o histórico das conversas |
| `config/statusline.js` | as skills que vêm da sua conta |

**Não é aqui que se edita.** As memórias continuam sendo lidas e gravadas em `~/.claude/projects/<repositório>/memory/`. Editar aqui não muda nada, e a próxima cópia desfaz.

## Conferir e restaurar

- **Conferir:** `python -X utf8 .claude/hooks/espelhar-assistente.py --conferir` compara o espelho com a origem por sha256. O que não bate vai para `assistant/.erro.log`, fora do git.
- **Restaurar numa máquina nova:** `python -X utf8 .claude/hooks/espelhar-assistente.py --restaurar <pasta vazia>` copia o espelho e confere; depois, copie `memory/` para `~/.claude/projects/<repositório>/memory/`.
