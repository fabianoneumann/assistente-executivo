# O que é deste projeto na `r2-storage`

O método da skill fica no `SKILL.md`; aqui ficam os nomes e as convenções deste repositório. Outro projeto que instale a skill troca este arquivo.

## Os buckets, por apelido

| Apelido | Variável do nome | Para quê | Público |
|---|---|---|---|
| `conteudo` | `R2_BUCKET_CONTEUDO` | as imagens e vídeos das peças (as telas exportadas dos carrosséis e dos Stories, os originais gerados pela `image-gen` em `assets/gerados/`), o que a rede social vai puxar por URL | sim, com `R2_PUBLIC_BASE_CONTEUDO` |
| `curso` | `R2_BUCKET_CURSO` | material de curso ou de cliente que não é público | não: entregar com `presign` |
| `campanhas` | `R2_BUCKET_CAMPANHAS` | criativos de anúncio | só se forem referenciados por URL |

Qualquer outro apelido vale: basta a variável `R2_BUCKET_<APELIDO>` (e a `R2_PUBLIC_BASE_<APELIDO>`, se for público). Os três acima são os que o `.env.example` da raiz traz.

## A convenção de chaves

A chave no bucket espelha o caminho no repositório, sem o prefixo de área, para o markdown apontar sem ambiguidade: um carrossel em `marketing/social-media/carousels/standalone/AAAA-MM-DD_tema/images/slide-01.jpg` vira `carousels/standalone/AAAA-MM-DD_tema/slide-01.jpg` no bucket `conteudo`. As prévias validadas de uma peça ficam em `<prefixo da peça>/previas/passada-N.jpg`, e as versões de uma peça já publicada, em `<prefixo da peça>/versoes/versao-N/` (pela `slides-export`).

## O que conta como publicada

A regra geral: **depois de publicada, nada se sobrescreve nem se remove no bucket**, e a mudança sobe como versão nova, com o motivo, acrescentada ao registro da peça. O critério de "publicada" e o código que o lê estão na `slides-export` ([`../../slides-export/references/projeto.md`](../../slides-export/references/projeto.md)): no carrossel, a `legenda.md` com `**Publicado:**` preenchido.
