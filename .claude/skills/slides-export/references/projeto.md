# O que é deste projeto na `slides-export`

O método da skill fica no `SKILL.md` e no README; aqui ficam os estados da peça, o critério de publicada e as convenções deste repositório. Outro projeto que instale a skill troca este arquivo.

## Onde ficam as peças

| Formato | Pasta | Registro da peça |
|---|---|---|
| carrossel da série | `marketing/social-media/carousels/series/<série>/<peça>/` (a série de exemplo: `carousels/series/exemplo/`) | `legenda.md` |
| carrossel avulso | `marketing/social-media/carousels/standalone/<peça>/` | `legenda.md` |
| Stories | `marketing/social-media/stories/<data>-<tema>/` | `roteiro.md` |

O HTML é o `slides.html` (carrossel) ou o `stories.html` (Stories, com `--height 1920`). As conferências da forma vêm da `visual-form` (`.claude/skills/visual-form/scripts/conferir_telas.py`); sem ela no projeto, a exportação para revisão segue com aviso e o `--upload` fica bloqueado.

## O bucket

O apelido padrão do `--upload` é `conteudo` (`R2_BUCKET_CONTEUDO` e `R2_PUBLIC_BASE_CONTEUDO`, pela `r2-storage`); outro apelido configurado vale, e o `--bucket-publicado` diz onde a coleta dos Stories guarda o que foi ao ar, quando é outro. A chave no bucket espelha o caminho da peça sem o prefixo de área (a convenção em `../../r2-storage/references/projeto.md`).

## Os estados da peça

A peça anda por estágios, no `**Estágio:**` da `legenda.md` ou no `estagio:` do frontmatter do `roteiro.md`: `rascunho` (em produção), `a-validar` (esperando a leitura de quem decide), `pronto` (fechada, pode publicar), `publicado` (foi ao ar) e `medido` (as métricas já entraram). A exportação lê só o que diz se a peça foi ao ar; os outros estados são do fluxo de produção.

## O que conta como publicada

A regra geral: **o que foi ao ar não se sobrescreve**. Uma mudança no sistema (o CSS ou o script da série) muda a quebra e o desenho de peças que já estão no ar, e o registro precisa guardar o que foi publicado. Por isso, depois de publicada, cada mudança sobe como versão nova (`<prefixo>/versoes/versao-N/`), com o motivo, e entra como linha acrescentada na tabela "## Versões depois de publicada" do registro da peça, sem tirar nada. Antes de publicar, regerar sobrescreve com o mesmo nome: é a mesma peça, ainda em produção, e a evolução fica nas passadas de prévia.

| Caminho | Conta como publicada | O que fica protegido |
|---|---|---|
| **Carrossel** (por API ou pelo app) | a `legenda.md` com `**Publicado:**` preenchido (quem publica por API grava; na postagem pelo app, grava-se à mão depois) | todas as telas, porque o carrossel vai ao ar inteiro |
| **Stories publicados por API** | cada Story com linha na tabela da seção `## Publicado` do `roteiro.md` que abre com "Publicada pela API" (ou com as colunas "tipo" e "link") e traz o id que a publicação devolveu | só os Stories com linha; quando a tabela existe, vale ela, e não o `estagio` |
| **Stories pelo app** | a sequência inteira, quando o `roteiro.md` tem `estagio: publicado` ou `medido`, ou quando há algum objeto em `stories/publicado/<data>/` no bucket, gravado a partir das 5h de Brasília do `data:` do roteiro (onde uma coleta de métricas guarda cada Story como foi ao ar) | a sequência inteira |

Casos de borda: o Story de madrugada (antes das 5h) não marca a sequência do dia; entre a postagem pelo app e a coleta seguinte nada protege, então quem corrige logo depois de postar marca o roteiro à mão antes do `--upload`; sem resposta do bucket, vale só o roteiro, com aviso; Story no ar sem linha na tabela da API leva ao critério do app, a sequência inteira. A peça que vai ser postada à mão sai de `pronto` antes, para nenhuma rotina de publicação a pegar de novo.

## A voz e o travessão

A conferência do travessão (da `visual-form`) só barra o `--upload` quando a voz de quem usa, em `context/sobre-mim.md`, pede texto sem travessão. O arquivo vem em branco, com roteiro: enquanto não disser isso, o achado não barra.

## O que este projeto precisa ter

- **Uma coleta de métricas que guarde os Stories publicados** em `stories/publicado/<data>/` no bucket, se você publicar Stories pelo app e quiser a proteção pelo bucket. Sem ela, a proteção dos Stories vale só pelo `roteiro.md`.
- **Um publicador por API** que grave o `**Publicado:**` da `legenda.md` (carrossel) e a tabela "Publicada pela API" do `roteiro.md` (Stories). Sem ele, grave à mão depois de postar.
