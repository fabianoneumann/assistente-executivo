---
titulo: "Building effective agent automations"
tipo: artigo
autor: "Lance Martin e CJ Avilla (Anthropic, claude.dev)"
url: "https://claude.dev/blog/building-effective-agent-automations/"
publicado_em: 2026-10-08
capturado_em: 2026-11-13
licenca: "Post do blog da Anthropic (claude.dev), sem licença aberta na página; entra só a nota de fato."
areas: [agent-engineering, anthropic-claude]
entrada: pesquisa
tags: [scheduled-agents, managed-agents, bookmarks, ledger, failed-reads, spending-cap]
---

# Automações de agente que rodam sozinhas (claude.dev, 08/10/2026)

Nota de fato, sem integral (post protegido).

**Proveniência.** A página foi baixada por curl em 2026-11-13 e convertida em texto, 16.680 caracteres). O texto foi lido pelo WebFetch e conferido por grep na cópia. A data e os autores vêm do cabeçalho.

**Conferência lado a lado** (2026-11-13, na escrita): 2 de 7 unidades de prosa seguem uma frase da fonte; as células de fato ficaram fora. O `parafrase.py`, no mesmo dia, achou 0 de 19 unidades coladas e nenhum trecho seguido; como a ficha é em português e a fonte em inglês, ele sai com o código 3 e não mede tradução, e a conta acima é a que vale.

## Em uma frase

O post apresenta uma implementação de referência, num Managed Agent agendado, que lê canais do Slack e PRs do GitHub, guarda o que já relatou e posta um resumo curto por dia, com as falhas comuns desse tipo de automação e as regras que as evitam.

## As peças

| Peça | Fato |
|---|---|
| Fontes | canais do Slack e PRs do GitHub, só leitura; credenciais fora do sandbox |
| Agente | configuração versionada (modelo, ferramentas, prompt) em `agent.md`; o exemplo usa `claude-sonnet-5-5` |
| Agenda | cron no `deployment.md`; cada disparo, sessão nova sem memória da anterior |
| Memória `preferences` | do leitor; só leitura para o agente; relida a cada rodada; sem ela, o agente para |
| Memória `state` | do agente: marcadores por fonte, ledger do que relatou, um registro por rodada, propostas de mudança nas preferências, notas sobre cada fonte |
| Teto | `max_list_cost` por rodada (exemplo: 500 centavos) |

## As falhas e as regras

| Falha | Regra |
|---|---|
| Janela fixa ("últimas 24 horas") | marcador por fonte com o carimbo do item mais novo lido |
| Fonte fora do ar lida como dia calmo | marcador parado, resumo das outras fontes, uma linha com o que não se leu |
| Resumo longo | item só se o leitor agiria hoje ou se muda uma decisão próxima; contagem não é item |
| Estado mudado desde a leitura | reconferência da fonte viva antes de postar; link copiado do campo |
| Post registrado que não saiu | só conta com a confirmação do Slack; título do dia conferido antes; dúvida vira "maybe posted" |
| Preferência copiada no prompt | leitura do arquivo a cada rodada |
| Teto baixo | pausa, não falha |

## O que a fonte recomenda

Começar o teto em três a cinco vezes o custo de uma rodada normal e apertar com os números reais. Deixar a mudança de preferência como proposta que o leitor aplica. Separar o que é do leitor, que o agente não escreve, do que é do agente.

## Citações

- "A late run leaves a gap and an early run repeats items."
- "A run that hits its cap pauses instead of failing, so a cap set too low looks like a brief that went quiet."

## Lacuna

O post não diz como a rodada é cobrada (assinatura ou créditos de API), nem como se revisa o que o agente propõe além de o leitor aplicar. Não mede quanto as regras reduzem as falhas.
