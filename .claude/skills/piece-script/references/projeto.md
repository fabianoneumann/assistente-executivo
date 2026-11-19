# O que é deste projeto

O arquivo da skill com o que é deste repositório: as réguas de cada formato, as pastas, a série e os scripts. O `SKILL.md` e as referências dos formatos guardam o método; o que muda de projeto para projeto mora aqui. Os caminhos partem da raiz do repositório.

## As réguas

| O quê | Onde |
|---|---|
| A rubrica da mensagem (carrossel, tela única, Reels) | `marketing/social-media/rubrica-de-qualidade.md` |
| A rubrica dos Stories (sequência, avulso, em vídeo) | `marketing/social-media/rubrica-de-stories.md` |
| As lições das peças, por etapa (lidas antes de escrever; anotadas na cabeça como **Regras conferidas**) | `marketing/licoes.md`; as que já viraram regra, em `marketing/licoes-que-viraram-regra.md` |
| O público e a voz de quem publica | `context/publico.md` e `context/sobre-mim.md` |
| As mesas (o que vai à pessoa e o que se confere antes) | `decisions/mesas-de-design.md` |
| Os estágios do frontmatter | `decisions/artefatos-e-estagio.md` |

## As pastas

| Formato | A pasta da peça | A régua do formato |
|---|---|---|
| Carrossel de série | `marketing/social-media/carousels/series/<série>/AAAA-MM-DD_<tema>/`; a série de exemplo, em branco, é `carousels/series/exemplo/` | a `estrutura-editorial.md` da série (as receitas por tipo, a regra da fala atribuída) e o `processo-criacao-posts.md`, quando a série os tiver |
| Carrossel avulso | `marketing/social-media/carousels/standalone/AAAA-MM-DD_<tema>/` | as três regras do avulso em `carrossel.md` |
| Stories | `marketing/social-media/stories/AAAA-MM-DD-<tema>/` | `marketing/social-media/stories/README.md` |
| Reels e cena | a pasta do formato que o projeto usar (proposta: `marketing/social-media/reels/AAAA-MM-DD-<tema>/`) | este `cena.md` |

## O banco de imagens (a coluna do que aparece)

Antes de propor gerar, procure em: os `assets/` das peças publicadas do formato e da série; `context/brand/` (as fotos e o material da marca); `marketing/social-media/banco-de-imagens.md` (o índice das imagens geradas, mantido pela `image-gen`).

## O que este projeto precisa ter

- **A estrutura editorial de cada série** (`carousels/series/<série>/estrutura-editorial.md`): as receitas de cada tipo de post (as funções das telas) e a regra da fala atribuída. Sem ela, o carrossel de série roda como o avulso, com a função de cada tela vinda da escaleta, e a cabeça diz isso.
- **Um script de conferência do texto, por série** (proposta: `carousels/series/<série>/scripts/confere_texto.py`): confere o `texto.md` e a `legenda.md` contra as fichas (as aspas com verbatim, o teto de palavras pela tela-par, a lista negra da rubrica e a chamada única) e avisa as palavras que soam como mentira. Até existir, essas conferências se fazem à mão no passo 8, e a cabeça diz que foram à mão.
- **Uma conferência do contrato por script** (proposta: `.claude/skills/piece-script/scripts/confere_contrato.py`), que lê a escaleta pelos rótulos fixos de `contrato.md` e acusa o campo ausente, inclusive o que sumiu fora do nível. Até existir, a conferência é a do passo 8.
- **Um calendário editorial**, se o projeto quiser a conferência de desenho repetido contra o que vai ao ar na semana; sem ele, confira contra as pastas datadas da semana.
