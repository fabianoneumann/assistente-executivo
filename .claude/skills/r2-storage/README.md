# Skill `r2-storage`: setup e chaves

Bloco de acesso aos buckets R2 (Cloudflare Object Storage) do projeto, via API S3. É um **bloco componível**: a exportação das peças (`slides-export`) e o que mais precisar de uma URL pública chamam este script; ele não sabe nada de post ou anúncio, só sobe, baixa, lista e gera URL. Processo em [`SKILL.md`](./SKILL.md); o que é deste projeto em [`references/projeto.md`](./references/projeto.md).

## Instalação

```
python -m pip install -r .claude/skills/r2-storage/requirements.txt
```

Depois, da raiz do projeto, `python -X utf8 scripts/confere_ambiente.py --skill r2-storage` diz o que ainda falta configurar.

## As variáveis

Os valores vão no `.env` da raiz (copie o `.env.example` para `.env` e preencha as linhas; o `.env` nunca vai ao git) ou no bloco `env` do `.claude/settings.local.json`. O script lê pelo `scripts/ambiente.py` desta pasta: o que já está no ambiente vence, e o que falta se lê do `.env`. **Nunca** ponha chave no código nem num arquivo versionado. Depois de mexer no `settings.local.json`, reinicie a sessão do Claude Code: o bloco `env` é lido na abertura.

| Variável | Obrigatória | O que é | Onde se pega |
|---|---|---|---|
| `R2_ACCOUNT_ID` | sim | o ID da conta Cloudflare | https://dash.cloudflare.com > R2 > Overview (fica na lateral) |
| `R2_ACCESS_KEY_ID` | sim | o Access Key ID do token S3 | R2 > Manage API tokens > Create API token |
| `R2_SECRET_ACCESS_KEY` | sim | o Secret Access Key do mesmo token (aparece uma vez só) | idem |
| `R2_BUCKET_<APELIDO>` | ao menos uma | o nome de cada bucket, por apelido: `R2_BUCKET_CONTEUDO`, `R2_BUCKET_CURSO`, `R2_BUCKET_CAMPANHAS` ou outro qualquer | o nome que você deu em R2 > Create bucket |
| `R2_PUBLIC_BASE_<APELIDO>` | para bucket público | a URL pública do bucket (o endereço r2.dev ou o domínio próprio), para montar os links | R2 > o bucket > Settings > Public access, ou `r2.py public <apelido> --enable` |
| `CLOUDFLARE_API_TOKEN` | não | o **Token value** do token R2 (não é o Access Key); só o comando `public` usa, para ligar ou desligar o r2.dev pela API REST, e pede permissão *Admin Read & Write* | a mesma tela de criação do token; se não foi salvo, crie outro só para isso |

Exemplo no `.env` (valores fictícios):

```
R2_ACCOUNT_ID=COLE_SUA_CHAVE_AQUI
R2_ACCESS_KEY_ID=COLE_SUA_CHAVE_AQUI
R2_SECRET_ACCESS_KEY=COLE_SUA_CHAVE_AQUI
R2_BUCKET_CONTEUDO=nome-do-seu-bucket-de-conteudo
R2_PUBLIC_BASE_CONTEUDO=https://cdn.exemplo.com
```

**O token:** permissão **Object Read & Write** e, em *Specify bucket(s)*, só os buckets do projeto (nada de "all buckets" nem de admin). Prefira *Account API token* a *User API token*, para o acesso não depender do login de uma pessoa. O endpoint S3 é `https://<R2_ACCOUNT_ID>.r2.cloudflarestorage.com`; o script monta sozinho.

**Sem a configuração:** o script sai com código 1 e uma mensagem com cada variável que falta, para que serve, onde se pega e como se põe, sem traceback e sem mostrar valor. Sem a `R2_PUBLIC_BASE_<APELIDO>`, o `url` sai com 1; o `put` sobe e avisa, uma vez, que o link público não se montou. Quem importa o módulo tem `public_url()` (devolve `None` com o aviso no stderr, para testar sem sair), `exigir_public_url()` (sai com a mensagem) e `faltas()` (a lista do que falta, sem sair).

## URL pública

Uma rede social que publica por API recebe **uma URL pública** da imagem, não o arquivo. Por isso o bucket de conteúdo precisa de acesso público: no painel, o bucket > *Settings* > *Public access*, ligando o subdomínio r2.dev (rápido, para validar) ou um domínio próprio (recomendado depois, se o DNS estiver na Cloudflare). Pelo script: `python -X utf8 .claude/skills/r2-storage/scripts/r2.py public conteudo --enable` (pede `CLOUDFLARE_API_TOKEN`); a saída já traz a linha `R2_PUBLIC_BASE_CONTEUDO=...` pronta. O comando `url` monta `base/chave`. O bucket de material privado fica sem base pública e usa `presign` (URL assinada com validade).

## Testes

```
python -X utf8 .claude/skills/r2-storage/scripts/teste_r2.py   # sem rede e sem chave
python -X utf8 .claude/skills/r2-storage/scripts/r2.py smoke   # com as chaves: a conta de verdade
```

O `teste_r2.py` confere os buckets que vêm do ambiente, cada mensagem do que falta e o aviso da URL pública, num ambiente limpo. O `smoke` faz `head_bucket` em cada bucket configurado, escreve, lê e apaga um objeto temporário (`_smoke/<uuid>.txt`) no de conteúdo (ou no primeiro configurado) e diz quais bases públicas estão configuradas. Espera-se `[OK]` em tudo; falha de credencial ou de escopo do token aparece aqui.
