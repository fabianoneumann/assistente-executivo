# A discussão inicial do projeto

A etapa 1 da skill: entender o projeto antes de propor qualquer forma. Nasce do prompt de replicar a base do CRM ("pergunte antes de propor; não escreva nada na primeira passada"), que serve a qualquer projeto. **Leia antes da etapa 1.**

## As três regras

1. **Perguntar antes de propor.** Sem o contexto do projeto, a primeira proposta sai genérica, e a pessoa passa a corrigir a proposta em vez de pensar o projeto.
2. **Nada escrito na primeira passada.** Nem arquivo, nem pasta, nem repositório. A proposta vai na resposta, para a pessoa avaliar; só depois se decide o que criar.
3. **Nenhuma pergunta de sim ou não.** Cada pergunta é aberta ("quem usa, e quantos?") ou de escolha, com as opções e o que cada uma implica. A pergunta de sim ou não esconde a alternativa e convida o "sim" sem pensar; é a mesma razão por que as travas do projeto não perguntam.

Antes de cada pergunta, conferir se a pessoa já respondeu na conversa, num documento que ela deu, ou se o código e os dados de um sistema que já existe respondem. O que eles respondem vira fato, e não pergunta.

## O que perguntar

Em blocos, no máximo cinco perguntas por vez, das que mudam o desenho para as que só o refinam:

| Bloco | A pergunta | O que a resposta decide |
|---|---|---|
| O resultado | O que o sistema faz, para quem, e o que muda para essa pessoa quando ele existe? | os arcos do plano e o que o primeiro marco entrega |
| A premissa | Que premissa, se estiver errada, mata a ideia (alguém quer isto, o dado existe, o sistema de fora deixa), e qual o jeito mais barato de testá-la antes de construir? | o que a primeira milestone testa primeiro: um spike, uma conversa com quem usa, uma consulta ao dado, antes do resto |
| Quem usa | Quantas pessoas, de onde, com que frequência, e quem cuida dele depois? | a escala, o acesso, o onboarding e quem lê as notas da versão |
| Onde roda | Na máquina de quem usa, num servidor do cliente, na nuvem de quem? Quem instala a versão? | o artefato da versão, a implantação, se o projeto publica imagem (o `--docker` do `montar.py`) e o que "chega a quem usa" na triagem de dependência |
| A vigia | Quando ele parar, ou uma rotina dele não rodar, quem fica sabendo, por onde e em quanto tempo? | a checagem de fora, o heartbeat das rotinas, o que o `/health` devolve e, se houver, a pilha de observabilidade (a seção "Como se sabe que parou" da arquitetura) |
| O dado | Que dado ele guarda, de onde ele se recupera se sumir, e o que é pessoal? | o banco, o backup e o que não pode ir ao log nem ao repositório |
| O dado de fora (só quando o sistema lê dado de outro sistema, de uma planilha ou de um banco que já existe) | Qual o perfil do dado, medido antes de confiar: uma linha por quê (o grão), a chave e se é única, quanto de cada campo vem preenchido, o valor de marcador no lugar do dado (0, -1, "N/A", "test"), quando foi atualizado e até onde volta no tempo? Num banco, as cinco perguntas a quem o usa: o que "cliente" (ou a entidade principal) quer dizer ali, e se há tipos; qual o identificador principal, e se há mais de um para a mesma coisa; as duas ou três medidas mais pedidas e como cada uma se calcula; o que sempre se filtra antes de contar (teste, interno, fraude); e que erro quem chega costuma cometer com esse dado | o que o sistema pode prometer com o dado que existe, a limpeza na entrada e os testes com o dado de verdade (anonimizado) |
| As integrações | Que sistemas de fora ele chama ou o chamam, e o que acontece quando um cai? | as fronteiras da arquitetura e os testes de contrato |
| O relógio | Que datas de fora (cliente, lançamento) pesam sobre o projeto, e que escopo a equipe decide sozinha? | a primeira milestone e se há duas em paralelo |
| A equipe | Quem programa, com que agente, e que stack já conhece? | a stack, o ferramental e quanto o onboarding explica |
| A stack | Entre as variantes de partida (python-fastapi, node-ts) ou outra, qual, e por quê? | o ADR 001, o ADR 002 e os comandos do kit (`stacks.md`) |
| Os limites | O que não pode acontecer (custo, prazo, dado fora do país, dependência de um fornecedor)? | as alternativas rejeitadas dos ADRs e os riscos da arquitetura |

## A proposta

Depois das respostas, a proposta na conversa, sem escrever arquivo:

- **A arquitetura em uma passada:** as partes, as fronteiras, onde mora o dado. Quando há mais de uma forma razoável, duas ou três opções, com o que cada uma custa e o que ela deixa fácil, e a sugestão com o porquê.
- **Os arcos e as grandes entregas,** em ordem, com o resultado de cada um para quem usa.
- **A stack e o ferramental** que viram os ADRs 001 e 002, com o viés declarado (o que puxou a escolha) e o custo assumido.
- **A primeira milestone:** cerca de duas semanas, o critério que a fecha e as três a seis issues que a compõem, em uma linha cada.
- **O que fica em aberto,** que vai ao "A decidir" de uma issue, e não a uma suposição no texto.

## Pronta quando

A discussão inicial fica pronta quando dá para escrever a arquitetura, o plano e os dois ADRs sem adivinhar. O que a pessoa escolheu entre as opções vai como decisão, com a data; o que ninguém sabe ainda vai ao "A decidir" de uma issue da primeira milestone. Só então a etapa 2 começa a escrever.
