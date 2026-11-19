# O que é deste projeto

O arquivo da skill com o que é deste repositório: as pastas, as réguas, o portão, o público e o que o processo chama. O `SKILL.md` e as referências dos formatos guardam o método; o que muda de projeto para projeto mora aqui. Os caminhos partem da raiz do repositório.

## As réguas e o que se lê antes

| O quê | Onde |
|---|---|
| O portão (o juiz, o ciclo, a saída) | `marketing/social-media/portao-de-qualidade.md` |
| A rubrica da mensagem e a da forma (as duas do portão do carrossel) | `marketing/social-media/rubrica-de-qualidade.md` e `marketing/social-media/rubrica-de-design.md` |
| A rubrica dos Stories (a conferência final, sem juiz) | `marketing/social-media/rubrica-de-stories.md` |
| As lições das peças, por etapa | `marketing/licoes.md`; as que já viraram regra, em `marketing/licoes-que-viraram-regra.md` |
| O público e a voz de quem publica | `context/publico.md` e `context/sobre-mim.md` |
| A identidade da marca (fotos, cores, o que os avulsos herdam) | `context/brand/` |
| As mesas (o que vai à pessoa e o que se confere antes) | `decisions/mesas-de-design.md` |
| A pauta e o estágio da ideia | `decisions/apuracao-e-pauta.md` e `decisions/artefatos-e-estagio.md` |

## As pastas

| O quê | Onde |
|---|---|
| As ideias cruas e as pautas | `marketing/social-media/ideas/` (o formato do arquivo no `README.md` de lá) |
| As séries de carrossel | `marketing/social-media/carousels/series/<série>/`: o `README.md`, o `design-system.md`, a `estrutura-editorial.md`, o `processo-criacao-posts.md` (quando houver), o rascunho de cada semana e uma pasta datada por post. A série de exemplo, em branco, é `carousels/series/exemplo/`, o modelo para a primeira série do projeto |
| Os carrosséis avulsos | `marketing/social-media/carousels/standalone/AAAA-MM-DD_<tema>/` |
| As sequências e os avulsos de Stories | `marketing/social-media/stories/AAAA-MM-DD-<tema>/`, pelas regras do `marketing/social-media/stories/README.md` |
| O banco de imagens geradas | `marketing/social-media/banco-de-imagens.md`, mantido pela `image-gen` |

## O que o processo chama, e o que cada uma pede

| Skill | Passo | Pede |
|---|---|---|
| `story-angle` | 3, e a primeira mesa da ideia crua | nada além do que a `research` pede |
| `research` | 3 | a própria chave, conferida no passo 0 dela |
| `piece-script` | 4 | nada |
| `review` | 4, e a revisão do briefing | nada |
| `visual-form` | 5 | o navegador para as conferências; chama a `image-gen` (a própria chave) e a `object-anatomy` |
| `slides-export` | 8 | a chave e o bucket do armazenamento só com `--upload`, conferidos no passo 0 dela |
| o Jev (opcional) | 7 | `TYPESAFE_API_KEY`; o cliente em `scripts/jev/` |

**A publicação** (pela API do Instagram) não está nesta versão: a peça termina na exportação, e quem publica sobe as imagens pelo app.

## O que este projeto precisa ter

- **Um calendário editorial**, se o projeto quiser que o briefing confira a semana contra o que vai ao ar (proposta: `marketing/social-media/calendar/`, com a semana e as peças de cada dia). Sem ele, o briefing confere contra as pastas datadas da semana.
- **A parte em código da rubrica de Stories** (proposta: `marketing/social-media/stories/scripts/confere_stories.py`), que roda os testes [código] da rubrica e, com o Jev configurado, os [jev]. Até existir, os testes se fazem à mão e o estado diz isso.
- **Uma pasta de Reels**, quando o projeto fizer vídeo (proposta: `marketing/social-media/reels/`); até lá, o vídeo vai só até a folha da `piece-script`.
