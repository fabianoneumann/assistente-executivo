# A arquitetura

<!-- kit: este é o modelo que a skill preenche na etapa 2, a partir da discussão inicial. Cada seção leva só o que a conversa decidiu; o que ficou em aberto vai ao "A decidir" de uma issue da primeira milestone. Apagar estes comentários ao preencher. -->

O desenho do sistema no macro: as partes, as fronteiras e por onde passa o dado. A decisão da forma e da stack está no ADR 001 (`decisions/001-*.md`). **Ler quando:** for mexer na forma do sistema, nas fronteiras entre as partes ou numa integração.

## O que o sistema faz, e para quem

<!-- kit: uma ou duas frases: o resultado para quem usa, e quem usa. -->

## As partes

<!-- kit: as partes (o serviço, o banco, a fila, o cliente), o que cada uma faz e o que ela não faz. O diagrama, quando houver, em onboarding/, em HTML com SVG. -->

## As fronteiras e as integrações

<!-- kit: o que entra e o que sai de cada parte; os sistemas de fora, o contrato com cada um e o que acontece quando ele cai. -->

## O dado

<!-- kit: onde ele mora, de onde se recupera, e o que se perde se a cópia sumir. -->

## Onde roda

<!-- kit: o ambiente de produção, quem instala, e como se instala uma versão. -->

## Como se sabe que parou

<!-- kit: a resposta da pergunta "quando ele parar, quem fica sabendo, por onde e em quanto tempo?" da discussão inicial. Apagar as partes que não valem para este sistema; o resto fica como regra. -->

Um sistema fora do ar não avisa que caiu. O aviso que ele mesmo dá cobre só o que ele percebe estando de pé, e as falhas que importam passam em silêncio:

- **o serviço fora do ar** (o servidor desligado, o banco caído);
- **a rotina que não rodou** (o backup, a importação, o envio agendado que deixou de acontecer, sem erro nenhum);
- **a entrada em silêncio** (nada chegou por horas, num horário em que algo devia chegar).

Para cada uma, alguém de fora precisa observar. O mínimo são duas formas, que se completam:

- **a checagem de fora:** um serviço que não roda no mesmo servidor chama o `/health` a cada poucos minutos. Cobre o serviço fora; a falta de algo, só se o `/health` a informar (quem conhece a regra calcula o número, e o monitor só confere);
- **o heartbeat:** cada rotina, ao terminar bem, chama uma URL; o monitor avisa quando o aviso não chega no prazo. Cobre a rotina que não rodou.

O aviso marca a mudança de estado (atrasado, depois normalizado), e não cada checagem. O teste do aviso é derrubar de verdade e esperar o alerta e a volta.

<!-- kit: só se o projeto tiver uma pilha de observabilidade (métricas, rastros); sem pilha, apagar o parágrafo seguinte. -->

**Se houver pilha de observabilidade:** onde ela roda pesa mais que qual ferramenta (um agente leve em cada instalação e um central pequeno, em vez de uma pilha por instalação); o dado vai por push, sem abrir porta na instalação; e o filtro do que sai fecha por padrão, no próprio app, onde o dado nasce: sai só o que é técnico, e o resto vira identificador genérico. A pilha não substitui a checagem de fora.

## Os riscos que o desenho assume

<!-- kit: o que pode dar errado com este desenho, e o sinal de que deu. -->
