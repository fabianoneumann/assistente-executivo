# Log da base

Registro com a entrada nova no fim. As últimas: `grep "^## \[" knowledge/log.md | tail -5`.

Formato: `## [AAAA-MM-DD] <tipo> | <assunto>`, conferido pelo hook do commit e pelo CI. Os tipos: **`setup`** (a estrutura da base), **`decisao`** (um ADR novo ou revisto), **`nota`** (o que se aprendeu numa entrega), **`analise`** (uma investigação em `analysis/`) e **`versao`** (uma versão cortada). Tipo novo entra aqui na mesma operação em que é usado pela primeira vez.

## [{{DATA}}] setup | o projeto nasce, com a base, as travas e o CI

A base em `knowledge/` (a arquitetura, o plano, o processo, os metadados, as travas e a versão), os ADRs 001 e 002, os modelos de issue e de PR, o CI, os hooks do git e o do agente, e o onboarding em `onboarding/`.
