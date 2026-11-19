---
name: r2-storage
description: >-
  Acesso aos buckets R2 (Cloudflare) do projeto via API S3: subir, baixar, listar,
  remover arquivos e obter URL pública ou assinada. USE quando a pessoa pedir para
  subir/enviar/publicar um arquivo ou pasta "no bucket"/"no R2"/"na Cloudflare", listar
  ou baixar o que está lá, ou quando outra skill (a exportação das peças, criativos
  de campanha, material de curso) precisar de uma URL pública para um arquivo local.
  NÃO use para gerar a imagem (image-gen) nem para publicar o post em si numa rede social.
---

# r2-storage

Bloco single-purpose, componível: sobe, baixa, lista e gera URL; não sabe nada de post ou anúncio. Setup, chaves e buckets no [`README.md`](./README.md); o que é deste projeto (os apelidos dos buckets, a convenção de chaves, o que conta como publicado) em [`references/projeto.md`](./references/projeto.md).

> **Passo 0, as credenciais.** Antes de tudo, rode da raiz do projeto `python -X utf8 scripts/confere_ambiente.py --skill r2-storage`. Se ele sair com `[PARE]`, pare aqui: repasse à pessoa a mensagem dele (qual variável falta, onde se pega e como se põe) e não tente rodar a skill sem a chave. Se o script não existir (a skill instalada como plugin noutro projeto), siga: o próprio código da skill para com a mesma mensagem na primeira chamada.

**Lições:** antes de começar, leia as abertas e as apontadas em [`licoes.md`](./licoes.md) desta pasta.

## Comandos

```
python -X utf8 .claude/skills/r2-storage/scripts/r2.py smoke
python -X utf8 .claude/skills/r2-storage/scripts/r2.py ls <bucket> [--prefix p/]
python -X utf8 .claude/skills/r2-storage/scripts/r2.py put <bucket> <arquivo|pasta> [chave|prefixo]
python -X utf8 .claude/skills/r2-storage/scripts/r2.py get <bucket> <chave> [destino]
python -X utf8 .claude/skills/r2-storage/scripts/r2.py rm <bucket> <chave>
python -X utf8 .claude/skills/r2-storage/scripts/r2.py url <bucket> <chave>
python -X utf8 .claude/skills/r2-storage/scripts/r2.py presign <bucket> <chave> [--expires s]
python -X utf8 .claude/skills/r2-storage/scripts/r2.py public <bucket> [--enable|--disable]
python -X utf8 .claude/skills/r2-storage/scripts/teste_r2.py   # o teste sem rede nem chave
```

`<bucket>` é o apelido (`conteudo`, `curso`, `campanhas` ou qualquer outro) que tem uma variável `R2_BUCKET_<APELIDO>` com o nome do bucket, ou o próprio nome que está numa dessas variáveis. Nenhum nome de bucket fica no código.

**Sem configuração, nada roda em silêncio:** sem as credenciais ou sem o bucket, o script sai com código 1 e a mensagem completa (a variável, para que serve, onde se pega e como se põe). Sem a `R2_PUBLIC_BASE_<APELIDO>`, o `url` sai com código 1 e a mesma mensagem; o `put` sobe e avisa, uma vez, que a URL pública não se montou e por quê.

## Regras

1. **A chave no bucket espelha o caminho do projeto**, pela convenção de [`references/projeto.md`](./references/projeto.md). Ao subir, registrar no markdown da peça a chave ou a URL pública, nunca duplicar a imagem em outro lugar do repositório.
2. **Nada de `rm` em lote sem pedido explícito**; remoção é uma chave por vez e confirmada na conversa.
3. **Bucket público só onde precisa** (o de conteúdo, e o de campanhas se for referenciado por URL). O de material privado fica privado e se entrega com `presign`.
4. **Chave de peça publicada não se sobrescreve nem se remove** (`put` ou `rm` direto): o que foi ao ar fica onde está. O que conta como publicada está em [`references/projeto.md`](./references/projeto.md); a versão nova de uma peça publicada sobe pela `slides-export` (`--upload ... --motivo`), em `<prefixo>/versoes/versao-N/`, e é ela que lê o critério em código.
5. Se a Cloudflare recusar com `AccessDenied`, é escopo do token (bucket fora da lista ou só leitura): apontar para o README, não tentar contornar.

**Ao terminar:** se houve falha, contorno ou acerto que vale lembrar, registre em [`licoes.md`](./licoes.md) desta pasta, na mesma entrega (formato e estados em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md)).
