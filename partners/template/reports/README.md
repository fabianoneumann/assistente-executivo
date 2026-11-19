# Relatório semanal — {{parceiro}} (A/C {{contato}})

O ritual de acompanhamento de um trabalho em curso com o parceiro. Um relatório por semana, entregue a {{contato}}. Os relatórios ficam nesta pasta, um por semana, a partir do `modelo-relatorio-semanal.html`.

## Cadência e corte

- **{{dia: o dia e o momento da entrega, como segunda de manhã, antes de começar a semana}}.**
- **O corte é o começo do dia.** O que for feito depois de gerar o relatório entra no próximo; não se volta para atualizar o que já foi entregue.
- O período de um relatório vai do corte anterior até o corte atual.

## A varredura (o que conferir antes de escrever)

O material vive em {{onde: os repositórios, o quadro de tarefas e os documentos do trabalho}}. Atualizar tudo e então levantar:

1. **Os commits** desde o corte anterior, em todos os repositórios do trabalho; o que a equipe do parceiro fez entra como entrega dela.
2. **As tarefas:** o que fechou, o que segue aberto, o avanço e o prazo da etapa.
3. **Os comentários das tarefas**, sem pular. É onde vive o que nunca vira commit: as confirmações da equipe, as passagens de mão, os diagnósticos de fechamento e os pedidos. Sem eles, o relatório perde entrega dos outros.
4. **O registro de decisões** do projeto: o porquê que o commit não conta.
5. **O que foi entregue** e o que isso destrava.

## Estrutura do relatório

Quatro seções, na ordem:

1. **Resumo:** a narrativa da semana, em um parágrafo por assunto (o que mudou de fase).
2. **Concluído:** cada item com a tarefa como etiqueta. O que veio da equipe do parceiro leva o crédito explícito.
3. **Em andamento / próximos.**
4. **Em curso com terceiros:** o que saiu das suas mãos e ainda não voltou. Serve de radar do gargalo, com as regras abaixo.

## "Em curso com terceiros" — como escrever

A pergunta que a seção responde é: **o trabalho andou, e alguma data está ameaçada?** Ela não é uma lista de cobranças, porque cobrar ação de quem não a tem é errado, e "aguardando" soa como parada.

- **Cada linha leva a data em que o item saiu das suas mãos.** É a idade que separa o fluxo normal do travamento: entregue na quinta e pendente na segunda teve um dia útil, e a data diz isso sem justificativa. Sem ela, três dias e três semanas se parecem.
- **Separar o que está no prazo natural do que ameaça uma data.** Só o segundo ganha destaque, e vem com o que se propõe fazer: um caminho provisório, um recorte ou um pedido direto.
- **Dizer o que andou sem aquilo.** A garantia mais forte não é afirmar que está sob controle, é mostrar.
- **Nunca nomear pessoa como motivo.** Descrever o passo, não quem deve.

**O gatilho de risco**, que impede a seção de virar maquiagem: ela só sustenta confiança se reportar o caso ruim quando ele existir. Vira **risco explícito, com proposta**, quando a espera é a única coisa entre o trabalho e uma data de etapa, ou quando passa de **uma semana sem sinal**. Se "no fluxo natural" aparecer toda semana, deixa de significar alguma coisa.

## Voz e público

{{publico: quem lê e de onde fala, como um sócio que não é desenvolvedor}}. Linguagem de negócio, sem jargão: o termo técnico se traduz pelo que ele faz ("decisão formal", "esqueleto do projeto", "camada de integração"). O que importa é o que avançou e o que trava, não a implementação.

## Convenção e entrega

- Arquivo: **`AAAA-MM-DD-semana-NN.html`** nesta pasta (a data é a do corte).
- Visual: o do `modelo-relatorio-semanal.html`, com a marca nos tokens do topo; o relatório da semana parte do anterior.
- Entrega: {{entrega: o formato, como o PDF salvo do HTML, e o canal}}.
- Versionar o `.html` depois de validado e enviado.
