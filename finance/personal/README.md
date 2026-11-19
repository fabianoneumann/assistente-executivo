# Finanças pessoais

Dois tipos de arquivo, e nenhum deles existe antes do primeiro registro: o assistente cria cada um quando você relatar a primeira informação que pertence a ele.

| Arquivo | Natureza | O que guarda |
|---|---|---|
| `overview.md` | **vivo** (atualizado no lugar) | o regime (como o dinheiro entra: salário, pró-labore, autônomo), o vocabulário dos tipos de lançamento e os compromissos recorrentes, cada um com o modo de cobrança (na conta ou no cartão) e o dia |
| `debts.md` | **vivo**, com a data da posição | as dívidas (o saldo, as parcelas, quantas faltam), o que você tem a receber e o que vence nos próximos meses |
| `records/AAAA-MM.md` | **registro mensal**, um por mês | os lançamentos do mês, a abertura e o fechamento |

## As três disciplinas do registro mensal

1. **Todos os compromissos, sempre na mesma ordem.** Cada mês lista todos os recorrentes do `overview.md`, na ordem dele, inclusive os que não aconteceram, marcados com `—`. Assim, o que faltou aparece, em vez de sumir.
2. **O vocabulário fechado.** Cada lançamento leva um tipo da lista do `overview.md` (por exemplo: `receita`, `fixo`, `variavel`, `parcela`, `transferencia`). Tipo novo entra na lista na mesma operação em que é usado pela primeira vez.
3. **A abertura e o fechamento fecham.** O saldo de abertura, mais as entradas, menos as saídas, dá o saldo de fechamento. Se não fecha, o mês fica marcado com a diferença até você explicar.

**A conta e o cartão são dois razões.** O que é cobrado no cartão entra na seção do cartão no mês da compra; o pagamento da fatura sai da conta e entra na seção da conta como um lançamento só. Somar os dois contaria a mesma despesa duas vezes.

**A dívida é uma foto datada.** O `debts.md` diz a posição numa data ("posição em AAAA-MM-DD"); quando muda, a foto se atualiza, e o mês em que mudou registra o porquê.

## Como cada lançamento entra

1. Você conta o que entrou ou saiu. Sem data, o lançamento é do dia em que você contou, e o assistente diz a data que usou.
2. O assistente acha o mês (`records/AAAA-MM.md`), o razão (conta ou cartão) e o tipo, e lança.
3. Se o lançamento é um recorrente, ele marca o compromisso do mês; se é novo e vai se repetir, pergunta se entra no `overview.md`.
4. Ao fechar o mês, confere a abertura e o fechamento e diz o que falta.

## O roteiro do que preencher

Para começar, conte ao assistente:
- **as entradas:** de onde vem o dinheiro, quanto e em que dia;
- **os compromissos fixos:** aluguel, contas, assinaturas, escola, plano de saúde, e se cada um é cobrado na conta ou no cartão;
- **as dívidas e as parcelas:** o saldo, a parcela, quantas faltam, a taxa se souber;
- **o cartão:** o dia do fechamento e o do vencimento;
- **o saldo de hoje** da conta, para a abertura do primeiro mês.

Com isso, ele cria o `overview.md` e o `debts.md`; o primeiro `records/AAAA-MM.md` nasce no primeiro lançamento.

## Os modelos

O `records/AAAA-MM.md` segue este esqueleto:

```markdown
# Finanças pessoais: AAAA-MM

**Abertura (conta):** R$ ...   **Fechamento (conta):** R$ ...   **Fecha?** sim | não (diferença de R$ ...)

## Compromissos do mês
| Compromisso | Cobrança | Dia | Valor | Pago em |
|---|---|---|---|---|

## Conta
| Data | Descrição | Tipo | Entrada | Saída |
|---|---|---|---|---|

## Cartão (fatura que vence em AAAA-MM-DD)
| Data | Descrição | Tipo | Valor |
|---|---|---|---|

## Notas do mês
```
