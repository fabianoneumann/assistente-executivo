---
titulo: "Plugin small-business da Anthropic (versão 1.35.1): a definição salva de um relatório, o relatório que parece certo e está errado, e as regras de escrita da leitura"
tipo: instrumento
autor: "Anthropic"
publicado_em: 2026-11-10   # data de atualização do plugin no manifest.json da cópia local
capturado_em: 2026-11-10
licenca: "Sem licença declarada: a pasta do plugin não tem arquivo LICENSE nem NOTICE (raiz conferida em 2026-11-10: README.md, shared/, skills/, .claude-plugin/plugin.json, .mcp.json e .in_use), o README não fala de licença e o plugin.json só diz o autor, Anthropic. Tratado como protegido: entra só a ficha, em palavras próprias, sem o integral."
areas: [data-analysis]
tags: [reporting, report-definition, metric-definition, partial-period, double-counting, writing-with-numbers]
---

# small-business, `report-builder` e `growth-pulse`: o relatório recorrente que não engana

Ficha em palavras próprias, sem texto integral, porque o plugin não declara licença. A organização é nossa: o que a fonte entende por relatório bem definido, o que ela recomenda (arrumado por tipo de engano, juntando os três arquivos) e as ressalvas.

**Proveniência.** Não há url: o plugin veio sincronizado da conta do claude.ai (catálogo `anthropic-plugin-directory`) e foi desligado em 2026-11-10. Lidos numa cópia local feita naquele dia: `skills/report-builder/reference/report_spec.md` (109 linhas), `skills/report-builder/reference/gotchas.md` (155 linhas) e, de `skills/growth-pulse/SKILL.md` (133 linhas), a frase final do passo 2 (linha 40), os passos 3 a 5 e a lista do que não fazer. O integral está lá, e é lá que se confere esta ficha.

**O que ficou de fora.** Do `growth-pulse`: a coleta nos conectores, as cinco visões de uma empresa que vende e os cortes de status delas (em outro arquivo, não lido), a entrega em página, as ofertas de outras skills e dois itens da lista do que não fazer que só valem para o plugin (não pedir licença antes de puxar o dado; não ler despesa do resumo de um sistema contábil específico). Do `gotchas.md`: o item sobre não refazer a entrevista de um relatório já salvo.

## O que a fonte entende por relatório definido

Para o `report-builder`, o relatório existe primeiro como um texto curto, escrito antes de qualquer consulta e guardado para as rodadas seguintes; é a existência desse texto que permite repetir o relatório sem perguntar tudo de novo. Ele responde a oito coisas: como o relatório se chama, de quanto em quanto tempo roda, que janela de tempo cobre, contra o que compara (o período anterior, o mesmo período um ano antes, uma meta, ou nada), por qual dimensão recorta, quais são as métricas, de que sistemas ou arquivos o dado vem, e o que o solicitante esclareceu no caminho.

A linha de cada métrica tem três partes obrigatórias: nome, conta escrita por extenso e origem. A fonte justifica as duas últimas pela reprodução: um nome como "percentual de mão de obra" não permite refazer nem conferir nada; a divisão escrita e o sistema de onde saiu, sim. As notas guardam as escolhas que alguém precisou fazer (no exemplo, qual era o denominador de uma porcentagem), porque passado algum tempo ninguém lembra por que a conta é aquela. E o relatório tem um assunto só: pedido com muitas métricas sem ligação é sinal para propor dois.

## O que ela recomenda, por tipo de engano

**Comparar coisas de tamanhos diferentes.** O mês corrente, ainda aberto, ao lado do anterior fechado produz uma queda que não existe. A comparação honesta corta os dois no mesmo dia e diz isso no texto; no exemplo da fonte, alinhados, os mesmos dados mostram alta. O `growth-pulse` tem a regra vizinha, para a escrita: nenhum número vai sozinho, cada um leva a referência contra a qual foi lido.

**Somar o que é a mesma coisa.** Uma venda registrada na loja, no meio de pagamento e na contabilidade é uma venda, não três. A saída é eleger um sistema como dono daquela grandeza, dizer qual, e usar os demais para o que só eles têm. A mesma duplicação acontece dentro de um sistema só, quando o relatório exportado traz linhas de total misturadas às linhas de item; elas saem antes de qualquer ranking.

**Esconder ou inventar o que não veio.** Juntando os arquivos, são três situações, cada uma com o seu tratamento. O grupo que não teve movimento continua na tabela, com zero e uma nota: linha que desaparece faz o leitor suspeitar do dado. O que não pôde ser obtido aparece como indisponível, com a causa, seja uma métrica ou uma seção inteira. E o que não pôde ser obtido jamais é trocado por um valor verossímil; a fonte considera esse o pior defeito possível num relatório, porque o número inventado circula antes de ser notado. A frase dela: "Never estimate, never round toward a guess, never carry last period's figure forward silently." O mesmo vale para atribuir resultado a uma campanha sem conseguir rastreá-lo, e para apresentar como receita o valor de um negócio ainda em negociação: previsão e fato levam rótulos diferentes.

**Entregar partes que não fecham.** Recorte e total saem do mesmo relatório e têm de bater; a conferência é de quem monta, antes de entregar. Diferença que tem explicação (lançamento sem a dimensão preenchida, no exemplo) vai escrita, com o valor. O argumento da fonte é de confiança: uma soma que o leitor refaz e não fecha contamina os relatórios seguintes.

**Entregar um painel no lugar de uma leitura.** É onde o `growth-pulse` põe o valor do trabalho. A abertura é uma frase que explique o período, obtida ao relacionar as partes (os exemplos da fonte são de vendas: gasto e custo por contato subindo juntos indicam canal esgotado; um único produto sustentando a alta indica alta frágil). As tabelas ficam para depois. No texto, a quantidade aparece antes do adjetivo, o item é chamado pelo nome (qual campanha, qual produto), e o vocabulário é o do leitor. O fecho são exatamente três ações, cada uma com o que fazer de imediato, o dado que a sustenta e uma estimativa do que está em jogo, ordenadas pelo impacto e não pela facilidade.

**Fabricar movimento.** O texto não cria novidade onde não há: a seção parada registra que não houve mudança relevante, o período estável sai descrito como estável, e, quando a conclusão é que nada precisa mudar, essa frase ocupa o lugar das três ações. A fonte argumenta que recomendações produzidas por obrigação, toda semana, acostumam o leitor a não ler.

## Ressalvas

- **Sem medição.** São instruções para um assistente, sem estudo nem teste relatado. O motivo de rigor que os arquivos repetem é o destino do documento: quem recebe decide com ele e o encaminha a banco, conselho e contador.
- **Os valores são de cenário.** As vendas em dólar, a queda de 19% que vira alta de 8%, a receita triplicada pela soma de três sistemas e a mão de obra "em torno de 30%" são ilustração.
- **"Três" é formato.** As três ações são regra da skill, não resultado; o `gotchas.md` também sugere abrir com três números e três achados, sem justificar a conta.
- **O contexto é outro.** Empresa pequena que vende produto ou serviço, com sistema contábil, loja virtual e funil de vendas, valores em dólar. O que se transporta é o raciocínio.
