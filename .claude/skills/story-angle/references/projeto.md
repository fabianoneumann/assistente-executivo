# O que é deste projeto

O arquivo da skill com o que muda de projeto para projeto. O `SKILL.md` guarda o método (as fases, os gates, a mesa); aqui ficam as pastas, o público e a base deste repositório. Quem instala a skill noutro projeto troca só este arquivo.

## As entradas

| O quê | Onde |
|---|---|
| A pasta de ideias (os hubs e a pauta) | `marketing/social-media/ideas/` |
| O público (a fonte única, inclusive a seção de postura) | `context/publico.md` |
| As peças publicadas (para a Fase 0) | `marketing/social-media/carousels/` e `marketing/social-media/stories/` |

## A base

| O quê | Onde |
|---|---|
| O craft da apuração (movimentos, taxonomias, critérios de conclusão) | `knowledge/journalism/apuracao-investigativa.md` |
| A porta de entrada e os rituais (ingestão, consulta) | `knowledge/index.md` e `knowledge/README.md` ("Query" e "Ingest") |
| O índice de cada área | `knowledge/<área>/index.md` |
| As fichas de fonte | `knowledge/sources/`, pela régua de `knowledge/sources/README.md` |
| O log, com as rodadas e o custo de cada apuração | `knowledge/log.md` |
| As pastas das rodadas de pesquisa | `knowledge/research-rounds/`, pela regra da `research` |

## As decisões que esta skill segue

- `decisions/apuracao-e-pauta.md`: a fronteira com a `research` e a produção (delegação, parada única, a pauta no arquivo da ideia).
- `decisions/artefatos-e-estagio.md`: o campo `estagio: pauta`, que esta skill grava.
- `decisions/licoes-das-skills.md`: o formato e os estados do `licoes.md`.

## As outras skills

| Skill | Para quê |
|---|---|
| `research` | todas as buscas das Fases 1 e 2, o peso das fontes, a pasta de cada rodada, os rótulos da triagem e as conferências automáticas da rodada |
| `review` | a revisão da mesa, antes de apresentá-la (catálogo de lentes em `.claude/skills/review/references/lentes.md`) |
| `idea-capture` | o registro da ideia crua, antes desta skill |
| `piece-creation` | a peça, depois da pauta |

## Chaves

Esta skill não lê chave. As buscas vão pela `research`, que pede as dela no Passo 0.
