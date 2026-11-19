# O GitHub do projeto

As etapas 5 e 6 da skill: o repositório, a regra da tag, o Dependabot, a primeira milestone e as specs. **Leia antes da etapa 5.**

## A etapa 5: o `github.py`

Depois do primeiro commit (o `main` com o kit montado e conferido), rode primeiro com `--simular` e leia o que ele faria:

```
python -X utf8 .claude/skills/project-kit/scripts/github.py --pasta <projeto> --repo <dono>/<nome> --criar --simular
python -X utf8 .claude/skills/project-kit/scripts/github.py --pasta <projeto> --repo <dono>/<nome> --criar
```

Ele cria o repositório privado com o push, os rótulos (na conta pessoal, os de prioridade e o `defeito`), liga os alertas e as correções de segurança do Dependabot e cria a regra de tag `tags-imutaveis` (as tags `v*` não se movem nem se apagam; criar segue livre, porque quem corta a versão é o agente). Na conta pessoal com o repositório privado, a regra de tag não se cria, porque pede o GitHub Pro: vale a regra escrita no `CLAUDE.md` do projeto, que o `montar.py --conta user` já põe. Cada passo confere antes de agir: rodar de novo não duplica nada.

**O que conferir depois, no próprio GitHub:**
- o CI do primeiro push rodou e saiu verde (`gh run list --limit 1`): o esqueleto da stack traz o teste e o smoke (`stacks.md`);
- o `dependabot.yml` sem erro: a aba Insights > Dependency graph > Dependabot do repositório lista as entradas sem erro de configuração (a API de alertas responder só prova que os alertas estão ligados, e não o arquivo);
- a regra de tag existe (`gh api repos/<repo>/rulesets`). **Se o plano não a oferece** (o `github.py` avisa com o 403), vale a regra escrita no `versao-e-dependencias.md` da base do projeto, e a entrega diz isso.

**A conta pessoal e a organização:** o Type e a Priority nativos e os campos da issue só existem em organização. Na conta pessoal, a natureza vai pelo rótulo `defeito` e a prioridade pelos rótulos `prioridade:*`; o `montar.py --conta user` já escreve o `metadados.md` e o modelo de defeito assim. Em organização (`--conta org`), o Type e a Priority são da organização, e quem os cria é o administrador dela.

## A etapa 6: a primeira milestone e as specs

1. **A milestone:** o `github.py` com `--milestone "<título>" --prazo AAAA-MM-DD --criterio "<o que fecha>"`. Cerca de duas semanas, fechada pelo critério, e não pela data. A descrição leva o critério e o link da busca "o que pegar agora" filtrada por ela.
2. **As specs:** uma issue por entrega da milestone, pelo `.github/ISSUE_TEMPLATE/spec.md` do projeto. Para cada uma:
   - escreva o corpo num arquivo fora do repositório, sem o cabeçalho YAML e sem os comentários do modelo;
   - mostre os corpos à pessoa, todos juntos, antes de criar (o texto da spec é base, e a base passa pela pessoa);
   - `gh issue create --repo <repo> --title "<frase>" --body-file <arquivo> --milestone "<título>"`, e a prioridade (`--label prioridade:media` na conta pessoal; na organização, pela GraphQL, como diz o `metadados.md` da base do projeto).
3. **Os bloqueios:** o "blocked by" nativo, pela GraphQL (`addBlockedBy`, no `metadados.md` da base do projeto), e a razão da ordem na seção "Dependências" de cada spec.
4. **A primeira issue** troca o esqueleto da stack (o `/health` e o smoke) pelo começo do sistema que a arquitetura pede, com o smoke provando o caminho mínimo de ponta a ponta. O "Pronto quando" dela tem o CI verde no `main`.

## O teste de ponta a ponta do kit

Para provar o kit sem criar um projeto de verdade: um repositório privado descartável, `<dono>/kit-<issue>-teste`, com o push, um PR de teste, o CI verde, a regra de tag e o `dependabot.yml` validado; depois, `gh repo delete <repo> --yes`. O `gh` precisa do escopo `delete_repo` (`gh auth refresh -s delete_repo`, pela pessoa, porque abre o navegador). Sem o escopo, o repositório fica, e a entrega diz o nome dele para a pessoa apagar.
