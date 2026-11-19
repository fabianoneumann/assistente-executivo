# Lições da skill `slides-export`

O que o uso e a edição desta skill ensinaram. Antes de usar a skill, leia as abertas e as apontadas; ao terminar, registre a lição nova aqui, na mesma entrega, como **aberta**. Cada lição traz o que devia acontecer, o que aconteceu, por quê, o que mudar e quando vale, com a gravidade (crítica, maior, menor) e as ocorrências; a que vira regra entra no `SKILL.md` (ou no código) e passa para "Viraram regra", em uma ou duas linhas, no imperativo, com o porquê. Formato, estados e quem decide em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md). Lição da peça (mensagem, forma) fica em [`marketing/licoes.md`](../../../marketing/licoes.md); lição que vale para várias skills, em [`../licoes-gerais.md`](../licoes-gerais.md).

## Abertas

Nenhuma.

## Viraram regra

- **Suba toda prévia validada ao bucket, com nome próprio, e aponte no roteiro.** A prévia que fica só local se perde, e a evolução da peça deixa de poder ser conferida.
- **Leia e grave arquivo versionado em binário ou com `newline=""`.** O modo texto troca o fim de linha e infla o diff.
- **Exporte com `--browser-arg --disable-lcd-text`.** Sem a flag, o Chromium do Windows desenha o texto miúdo com franja de cor (subpixel).
- **Meça a franja pela distância de cada pixel de tinta ao segmento entre a cor do papel e a da tinta, não pela diferença entre canais.** No papel colorido, a diferença entre canais já é alta sem franja nenhuma.
- **Na tela em vídeo, grave com as animações permitidas, sem quadros B e sem lista de edição, e confira a paridade da caixa antes de fotografar.** Cada uma dessas falhas passava pelo teste da peça e só aparecia no MP4 ou na API.
- **Ponha a saída em linha a linha (`line_buffering`) no começo do script que chama subprocesso.** Num pipe, a saída em bloco saía fora de ordem e escondia o erro.
- **Ao tirar as linhas do papel para medir contraste, apague só as camadas de gradiente da tela, não todo `background-image`.** Apagar tudo levava junto o degradê do fundo e media contra a cor errada.
- **Deduplique a fonte que falta pela família, estilo e peso, sem o tamanho, e marque como sem resposta só a que não respondeu.** Senão a mesma fonte sai em dois ERRO, ou a que carregou fica acusada.
- **Não conte os apelidos de fonte de outro sistema (`-apple-system`, `BlinkMacSystemFont`) como a família da pilha.** No Windows eles não existem, e a exportação barraria sem defeito.
- **No caso de teste de um formato que outro script grava, leia o formato do fonte dele; não o escreva à mão.** O cabeçalho inventado no teste escondeu que o código reconhecia a tabela errada.
- **Meça as duas coisas que se comparam na tela no mesmo estado (depois das fontes e do `prepararSlide`).** Medidas em estados diferentes deram a ponta da seta fora do lugar.
