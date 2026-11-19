# Lições gerais das skills

As lições que valem para mais de uma skill. **Leia ao criar, editar ou testar uma skill.** A que vale a cada uso de qualquer skill vira regra no `CLAUDE.md` do projeto. A lição aberta daqui que vale ao usar certas skills fica apontada no `licoes.md` de cada uma delas, para chegar à hora do uso. Cada skill tem as suas em `<skill>/licoes.md`.

**Formato** (o de [`decisions/licoes-das-skills.md`](../../decisions/licoes-das-skills.md)): cada lição diz o que devia acontecer, o que aconteceu, por quê e o que mudar, mais quando vale, a evidência, a gravidade (crítica, maior, menor) e as ocorrências. A lição nova da equipe entra em "Abertas", como aberta; quando vira regra, passa a uma linha no imperativo, com o porquê em termos gerais e o lugar onde entrou.

## Valem ao criar, editar ou testar uma skill

- **No teste com erros plantados, tire o original do alcance do agente.** Por quê: o agente que procura problemas acha o original, compara os dois e esvazia o teste. O material do teste fica numa pasta temporária, sem o original no projeto nem em lugar que o agente leia.
- **Ao dividir um `SKILL.md` em referências, compare cada resumo que fica no roteiro com a referência que ele aponta.** Por quê: o resumo tende a dizer menos que a regra inteira, e quem lê só o roteiro segue a versão mais fraca. Cada ponteiro diz "Leia ... antes de" o passo em que a referência vale.
- **Meça o disparo da descrição de uma skill pelo `scripts/medir_disparo.py`, não pelo medidor da `skill-creator`.** Por quê: o medidor dela não roda no Windows (lê o pipe com `select`) e mede a descrição como um comando novo ao lado da skill real, que pode tomar o disparo e contar como erro; o `medir_disparo.py` mede a skill como está, contra as vizinhas, numa cópia mínima do projeto sem hooks.

## Viraram regra

- **Chame a skill pela ferramenta Skill, nunca siga os passos de memória.** Por quê: seguida de memória, a skill perde os passos que não se lembram, e ninguém vê que ela não rodou.
- **Criar ou editar uma skill passa pela `review` (com a lente "efeito nas outras skills") e, quando a mudança é de estrutura (passo novo, divisão, mudança de entrada ou saída), pela `skill-creator`; o código da skill passa também pelo `/code-review`.** Por quê: cada revisão pega o que a outra não olha.
- **Script improvisado que vai servir de novo sai da pasta temporária na mesma entrega**, para a pasta `scripts/` da skill que o usa ou para `scripts/` na raiz. Por quê: o script deixado na pasta temporária se perde, e a medida que ele fazia não se repete igual.
- **No Windows, rode Python com saída em UTF-8 (`python -X utf8` ou `PYTHONUTF8=1`) e, ao editar arquivo versionado, preserve o fim de linha que ele tem** (ler e gravar em binário ou com `newline=""`; conferir com `git diff --ignore-cr-at-eol --stat`). Por quê: o modo texto troca o fim de linha e infla o diff, e a saída fora de UTF-8 quebra os acentos.
- **Script que percorre muitos itens por uma API roda em etapas gravadas em disco, com retomada e andamento visível, mesmo sendo de uso único; estime o término pelo pior caso medido** (itens × chamadas possíveis × tempo por chamada). Por quê: guardar tudo na memória até o fim perde a rodada inteira numa falha da API ou por falta de memória, e sem andamento ninguém sabe onde ela está.
- **Script que mede texto renderizado confere antes que a fonte da web carregou** (pedir cada fonte com o texto dela e comparar a largura com a das genéricas de reserva), e para com erro quando não carregou. Por quê: o `document.fonts.ready` resolve antes de a fonte ser pedida, o `document.fonts.check` não acusa a família que nem foi declarada, e a medida sai na fonte padrão do navegador sem aviso.

## Abertas

- **Ao reaproveitar um modelo de pedido a agentes, troque as referências da tarefa (issue, pasta, fontes) antes de disparar**, ou mantenha os modelos com marcadores `<>` obrigatórios. Por quê: o pedido copiado leva as referências da tarefa anterior, e o agente adivinha a certa. Vale nas skills que despacham agentes com modelo de pedido (`research`, `review`, `story-angle`).
- **Arquivo que outro script vai ler se grava pelo próprio script, em binário ou com `newline="\n"`, e não por redirecionamento do shell** (ou quem lê faz `.strip()` em cada linha). Por quê: no Windows, o redirecionamento grava em CRLF, e o `\r` entra no que se lê.
- **Confira o fim de linha em binário (`python -c "print(open(p,'rb').read().count(b'\r'))"`) ou com `git diff --ignore-cr-at-eol --stat`, nunca com `grep -c $'\r'` no Git Bash.** Por quê: no Git Bash do Windows, esse grep devolve o total de linhas tanto em LF quanto em CRLF, e leva a converter à toa.
- **Script com argumentos posicionais seguidos de opções `--` separa as opções dos posicionais e para com o uso certo quando falta um.** Por quê: lido por posição, o nome da opção vira o caminho de saída, e o script grava um arquivo chamado `--opção` na raiz.
- **Texto com barra invertida (escape, regex, caminho do Windows) vai ao arquivo pela ferramenta Write ou Edit, não por heredoc do shell;** depois de gravar por heredoc, confira os caracteres de controle em binário. Por quê: o heredoc do Git Bash colapsa a barra invertida dupla, mesmo com o delimitador entre aspas, e um `\\n` vira quebra de linha de verdade no meio da string. O pedido a agente que vai gravar arquivo diz isso.
