# OKR (objetivos e resultados-chave)

**O que é:** um **objetivo** em prosa (aonde se quer chegar no período) e de dois a cinco **resultados-chave** que dizem, em número, se se chegou. O método vem da Intel, com Andy Grove, e se difundiu pelo livro *Avalie o que importa*, de John Doerr (2018).

**Quando usar:** quando há um resultado que se mede, num período definido (um trimestre, um semestre). O que não se consegue medir continua como intenção, no Vision Board, e não vira OKR à força.

**A regra:** **cada resultado-chave tem um alvo e uma fonte de medição.** "Vender 20 unidades por mês, medidas na plataforma de vendas" tem os dois. "Crescer a audiência" não tem nenhum, e só vira resultado-chave quando se quebra por canal, cada um com o número e o lugar de onde ele sai. Use poucos: a forma que dá trabalho demais faz parar de usar.

**Onde preencher:** `maps/okr/AAAA-<periodo>.md` (por exemplo, `2027-T1.md`), um arquivo vivo por período, com `revisado_em` no frontmatter.

```markdown
---
mapa: okr
periodo: AAAA-T1
revisado_em: AAAA-MM-DD
---

# OKR: AAAA-T1

## Objetivo: <em prosa>

| Resultado-chave | Alvo | Fonte de medição | Hoje |
|---|---|---|---|
```
