---
titulo: "Severity Ratings for Usability Problems"
tipo: artigo
autor: "Jakob Nielsen (Nielsen Norman Group)"
url: "https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/"
publicado_em: 1994-11-01
capturado_em: 2026-10-29
licenca: "Rodapé do site: 'Copyright © 1998-2026 Nielsen Norman Group, All Rights Reserved', com política própria de cópia e reimpressão. Entra só a ficha."
areas: [agent-engineering, content-design]
tags: [severity, usability, heuristic-evaluation, prioritization, inter-rater-reliability, independent-review]
---

Ficha de estudo, em palavras próprias. Artigo curto de Jakob Nielsen, publicado em 01/11/1994 (o metadado da página registra modificação em 31/01/2024), lido no HTML em 2026-10-29. Como o artigo é curto, a ficha cobre todo o conteúdo dele. Citações literais só curtas.

## Para que serve a gravidade

- **Alocar recurso:** pôr o maior esforço de correção nos problemas mais sérios.
- **Estimar se falta trabalho de usabilidade:** se as notas indicam que ainda restam vários problemas desastrosos, lançar provavelmente não é aconselhável; se os problemas que sobram são todos cosméticos, dá para decidir lançar mesmo com vários deles.

## Os fatores

A gravidade de um problema combina três fatores:

1. **Frequência:** o problema é comum ou raro?
2. **Impacto:** quando acontece, é fácil ou difícil para o usuário superar?
3. **Persistência:** acontece uma vez e o usuário supera depois que aprende, ou volta a incomodar repetidamente?

Além deles, pesa o **impacto no mercado**: certos problemas podem derrubar a popularidade de um produto mesmo sendo "objetivamente" fáceis de contornar. Apesar de ter vários componentes, é comum juntar tudo numa **nota única** por problema, como avaliação geral, para facilitar priorizar e decidir.

## A escala, de 0 a 4

| Nota | Significado, em palavras próprias |
| :-: | :- |
| 0 | Quem avalia discorda de que isso seja um problema de usabilidade |
| 1 | Só cosmético: não precisa ser corrigido, a menos que sobre tempo no projeto |
| 2 | Problema menor: corrigir com prioridade baixa |
| 3 | Problema grave: importante corrigir, prioridade alta |
| 4 | Catástrofe de usabilidade: corrigir é obrigatório antes de lançar |

O 0 dá ao avaliador um jeito de recusar o achado, não só de pesá-lo.

## Como coletar as notas numa avaliação heurística

- **Não durante a sessão de busca.** É difícil obter boas estimativas de gravidade enquanto o avaliador está concentrado em achar problemas novos. E cada avaliador acha só uma pequena parte dos problemas, então as notas só dos problemas que ele achou ficam incompletas.
- **Depois, por questionário com a lista completa.** Terminadas as sessões, envia-se a cada avaliador a lista de **todos** os problemas descobertos pelo grupo e pede-se a nota de cada um.
- **Descrever bem cada problema.** Como cada um achou só parte da lista, os problemas precisam vir descritos com profundidade razoável, talvez com capturas de tela. Quem observou a avaliação sintetiza a descrição a partir dos comentários dos avaliadores que acharam aquele problema (ou dos relatórios escritos, quando houver). Assim dá para julgar até o problema que a pessoa não achou.
- **Custo:** tipicamente cerca de **30 minutos** por avaliador para dar as notas.
- **Independência:** cada avaliador dá as suas notas sem ver as dos outros.
- **Acesso ao sistema durante a nota:** em geral o avaliador não tem o sistema à mão e julga pela memória e pela descrição escrita. Revisitar a interface pode trazer percepções novas, mas sem dúvida deixa a nota mais lenta, e às vezes é difícil dar acesso a todos (protótipo que exige equipamento especial, distribuição restrita por sigilo).

## Confiabilidade

Pela experiência do autor, a nota de **um avaliador só é pouco confiável demais para se confiar nela**. Com mais avaliadores julgando, a qualidade da **média** das notas sobe rápido, e a média de **três avaliadores** já é satisfatória para muitos fins práticos. O artigo não dá número para essa confiabilidade (nenhum coeficiente nem curva); a afirmação vem da experiência declarada do autor. Qualquer coeficiente de confiabilidade atribuído a este artigo tem de vir de outro trabalho.

## Limites declarados

A escala junta fatores diferentes num número só por conveniência de decisão, não porque sejam a mesma coisa. A confiabilidade da média de três é afirmada pela experiência, sem medida publicada no artigo. A nota sem acesso ao sistema depende da qualidade da descrição sintetizada.
