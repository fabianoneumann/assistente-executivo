# Rodadas de pesquisa

Onde moram as rodadas da skill `research` (e as apurações da `story-angle`, que usam a mesma pesquisa): uma pasta por rodada, `AAAA-MM-DD-<tema>/`, com o que a busca trouxe e o que se anotou ao triar. A síntese e as fichas vão para as áreas e para `sources/`; aqui fica o rastro de como se chegou a elas, para não refazer o mesmo chão e para conferir depois uma triagem.

**Rodada** é um pedido, do primeiro disparo à apresentação dos achados, com as levas dirigidas e as correções da revisão. Leva pedida depois da apresentação é rodada nova, em pasta nova (`AAAA-MM-DD-<tema>-<qual>/`), que diz de qual é complemento.

## O que vai em cada pasta

- **Na raiz da rodada, no git:** as saídas das buscas (`qN-<ferramenta>.json`, `qN-nativa.md`), o arquivo de rótulos da triagem, quando a skill o grava, e `fontes/`, só com o texto de fonte cuja licença permite cópia (o item 1 da régua de [`../sources/README.md`](../sources/README.md)), mais `licencas.json`, com `id`, `url` e `licenca` (qual é e onde está escrita) de cada um, para o erro de licença não ir ao git sem aviso.
- **Em `notas/` e `scripts/`, no git:** as notas da rodada (achados, rascunhos, revisões) sem citação longa (mais de umas 25 palavras) nem trecho de fonte protegida além da citação curta, e os scripts sem texto de fonte embutido. Antes de gravar, a nota se confere inteira: nenhuma citação longa, nenhum trecho de mensagem ou conversa de terceiro, nenhum dado pessoal de terceiro; na dúvida, ela vai para `originals/`.
- **Em `originals/`, fora do git** (regra `**/originals/*` do `.gitignore`) e sem backup: o texto protegido inteiro (o baixado pela URL e o lido pelo navegador), o texto de licença em dúvida, a nota com citação longa e o script com texto de fonte embutido. Na pasta versionada fica `fontes/protegidas.json`, com `id`, `url`, `baixado_em` e `sha256` de cada texto protegido, para que, perdido o arquivo, se baixe de novo e se saiba se o texto mudou.

Por quê: a pasta da rodada se perde com o scratchpad da sessão se não for guardada, e o que é de terceiro só vai ao git quando a licença deixa; a divisão por licença é a mesma da base.
