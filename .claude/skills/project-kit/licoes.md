# Lições da skill `project-kit`

O que o uso e a edição desta skill ensinaram. Antes de usar a skill, leia as abertas e as apontadas; ao terminar, registre a lição nova aqui, na mesma entrega.

**Formato** (o de [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md)): cada lição diz o que devia acontecer, o que aconteceu, por quê e o que mudar, mais quando vale, a evidência, a gravidade (crítica, maior, menor) e as ocorrências. As seções são **Abertas** (à espera de decisão), **Apontadas** (a lição mora em outro arquivo, como [`../licoes-gerais.md`](../licoes-gerais.md)), **A sair**, **Viraram regra** e **Saíram**; seção vazia pode faltar. A lição nova de quem usa entra em "Abertas", como aberta; quando vira regra, passa a uma linha no imperativo em "Viraram regra", com o porquê em termos gerais e o lugar da skill onde entrou.

## Apontadas

- [`../licoes-gerais.md`](../licoes-gerais.md), "Meça o disparo da descrição de uma skill pelo `scripts/medir_disparo.py`": o disparo desta skill se mede por ele, com as frases de `evals/disparo.json`.
- [`../licoes-gerais.md`](../licoes-gerais.md), "Texto com barra invertida vai ao arquivo pela ferramenta Write ou Edit": os modelos e os scripts com regex ou escape (`fluxo.py`, `hooks.py`, `conferir.py`, os testes) se editam assim, e não por heredoc do shell.

## Abertas

Nenhuma ainda: a skill chegou a este repositório em 18/11/2026, e o primeiro uso real (um projeto de verdade) é o que vai ensinar.

## O que conferir no primeiro uso real

- Se a discussão inicial ficou pronta sem a pessoa ter de corrigir a proposta (o "pronta quando" do `discussao-inicial.md`).
- Se o CI do primeiro push saiu verde sem ajuste à mão no projeto.
- Se a pessoa precisou de alguma pergunta de sim ou não para destravar o agente, o que diria que a fronteira das travas não fechou.
- Se o Type e a Priority da organização casaram com o que o `metadados.md` do projeto diz, sem ajuste à mão.

## Viraram regra

| Data | Lição | Onde entrou | Ocorrências | Reincidiu |
|---|---|---|---|---|
| 2026-11-18 (sem mesa, procedimento) | O ELK.js não aceita o corte manual de fileiras (`wrapping.cutting.cuts` dá erro de tipo não registrado): a página escolhe entre os cortes que o motor oferece, por uma régua escrita; num fluxo com ramos a escolha cai na `MULTI_EDGE`, e a conferência e o teste negativo seguram o que a quebra não garante | `assets/diagramas/LEIA.md` ("A página escolhe entre o que o motor oferece" e "Limites encontrados") e a régua no `fluxo.html` | 1 (o padrão v1, 18/11); o diagrama de arquitetura, que era o "rever", virou o modelo do grafo na rodada 2 | |
| 2026-11-18 (sem mesa, procedimento) | O limite medido numa versão do motor se remede na versão nova antes de reescrever a régua; o teste rápido é o `elk.bundled.js` no Node, sem navegador | `assets/diagramas/LEIA.md` ("Limites encontrados", com a versão de cada medida) | 1 (a troca para a 0.12.1, 18/11) | |
| 2026-11-19 (sem mesa, procedimento) | A regressão visual por redução esconde o rótulo pequeno: a 320 px, o "sim" movido 40 px para baixo e 40 para a esquerda muda só 0,015% dos pixels, abaixo do 0,5% posto primeiro na rodada (sem medida); o limiar sai da medida do defeito que se quer pegar, não de um número redondo | `assets/diagramas/LEIA.md`, "O acabamento"; o limiar padrão do `diagrama_regressao.py` e o caso do teste | 1 | |
