# Rótulos da triagem

O registro de como a triagem de cada rodada classificou as fontes e quando parou. Serve à conferência automática (`scripts/confere_rodada.py` lê os rótulos), à revisão e, opcionalmente, de gabarito para sondar o Jev em classificar a fonte e na condição de parada (`projeto.md`, "As partes opcionais"). Vale para toda pesquisa da `research` e toda apuração da `story-angle`. Os rótulos são de quem pesquisou, feitos na hora da triagem (o `destino` tem dono próprio, abaixo); rótulo aplicado depois da rodada diz isso na `nota`. Pesquisa feita por agente: o pedido a ele leva este arquivo, e é ele quem grava.

## Onde e quando

- **Arquivo:** `knowledge/research-rounds/<rodada>/rotulos.json`, um por rodada, versionado, com `<rodada>` = `AAAA-MM-DD-<tema>`. Entra no commit da pesquisa; pesquisa sem commit próprio entra no próximo commit da sessão.
- **Rodada:** um pedido, do primeiro disparo à apresentação dos achados, com as levas dirigidas e as correções da revisão. Leva pedida depois da apresentação é rodada nova, em pasta nova (`AAAA-MM-DD-<tema>-<qual>/`), que diz na `nota` de qual é complemento. A apuração da `story-angle` é uma rodada só, até a mesa.
- **Fecha em dois tempos:** `objetivos`, `registro`, `lido` e `traz_novidade` fecham quando a rodada é apresentada, porque a condição de parada pergunta se parar ali bastava; `destino` segue até o fim do registro (Passo 7 da `research`, com o veto até o commit) e da curadoria da `story-angle`, inclusive quando uma rodada seguinte muda o destino da fonte. **De quem é o `destino`:** a `nota` diz o regime: curadoria de quem pediu (a mesa da `story-angle`) ou registro sob o veto (Passo 6 da `research`). Sob o veto, o `destino` é escolha do assistente, salvo o que a pessoa decidiu; a `nota` lista, pelo id, as fontes que ela vetou, as exceções do Passo 6 e o "para decidir" da revisão que ela decidiu.
- **Pesquisa de dado pontual** (a pergunta pede um dado só): o arquivo leva só `nota`, `buscas`, `consultas`, `objetivos` e `"fontes": []`. Ela fica registrada porque a pesquisa que parou cedo e bastou é o exemplo de parar certo.
- **O texto de cada fonte lida:** para cada linha `lido: texto`, baixe a página com `curl -fL`, pela rota que abriu (`knowledge/sources/README.md`, "Quando a primária não abre"), para `fontes/<id>.<ext>`, um arquivo por fonte, na pasta da rodada no scratchpad (Passo 2); o resumo do WebFetch não é a página. Confira que o título bate: o que não baixar nem se ler pelo Chrome, ou vier como página de bloqueio, fica sem texto. O texto lido pelo Chrome se grava por script, o `innerText` do `<article>` ou do `<main>`, em `originals/fontes/<id>.txt`, e ganha linha em `protegidas.json` com `"rota": "chrome"`. Em `fontes/`, só as páginas e `protegidas.json`: nota de leitura fica fora, e a saída de busca é só o que ela devolveu.
- **A pasta da rodada:** ao fechar a rodada, nos dois tempos, copie a pasta do scratchpad, que se perde, para `knowledge/research-rounds/<rodada>/`; na apuração, uma subpasta por pasta de leva. Rodada sem pasta guardada diz isso na `nota`. Ela se divide pela licença (`knowledge/sources/README.md`, "Conteúdo de terceiros", e `projeto.md`, "Onde fica o que é de terceiro"):
  - **Versionado, na raiz da rodada:** as saídas das buscas, `qN-nativa.md`, `rotulos.json` e o texto com licença que permite cópia, em `fontes/`, mais `licencas.json`, ao lado de `fontes/`, com `id`, `url` e `licenca` (qual é e onde está escrita) de cada um, para o erro de licença não ir ao git sem aviso.
  - **Versionado, em `notas/` e `scripts/`:** as notas nossas (achados, rascunhos, revisões) sem citação longa (mais de umas 25 palavras) nem trecho de fonte protegida além da citação curta, e os scripts sem texto de fonte embutido. Antes de copiar, a nota se confere inteira: nenhuma citação longa, nenhum trecho de mensagem, e-mail ou conversa de terceiro, nenhum dado pessoal de terceiro; na dúvida, fica em `originals/`. As listagens públicas de API (a árvore de um repositório, a lista de vídeos de um canal) também ficam versionadas, numa subpasta da rodada, só com os campos de fato (id, título, data, duração, contagens, caminho e tamanho); a descrição do canal, do vídeo ou do repositório e a legenda ficam no bruto, em `originals/`.
  - **Em `originals/`, fora do git (a linha `originals/` do `.gitignore`) e sem backup:** o texto protegido inteiro, inclusive o que se baixa de novo pela URL e o lido pelo Chrome, o texto de licença em dúvida, a nota com citação longa ou trecho de fonte protegida além da citação curta, inteira, sem cortar a citação para versionar, e o script com texto de fonte embutido. Na pasta versionada fica `fontes/protegidas.json`, com `id`, `url`, `baixado_em`, `sha256`, `sha256_de` (o que o hash mede) e `wayback` (o link que `archive.org/wayback/available?url=<url>` devolver, ou `null`) de cada texto. O `sha256` é do texto do bloco `<article>` ou `<main>`, sem tags, script e estilo (o do arquivo muda a cada download); em PDF, do arquivo. Perdido o arquivo, baixa-se de novo; hash diferente quer dizer que o texto mudou.
  - **Para sondar o Jev, só `fontes/`, `originals/fontes/` e as saídas das buscas, nunca `notas/` nem `scripts/`:** as notas nossas trazem os rótulos que a sonda mede.
  - **Conferir o lugar:** ao copiar a pasta, rodar `python -X utf8 .claude/skills/research/scripts/confere_lugar.py knowledge/research-rounds/<rodada>`, que aponta texto protegido na pasta versionada e texto lido sem cópia em `originals/`, e, no checkout principal, o mesmo script com `--repo`, que aponta o que o git não vê fora de `originals/`; o apontado se resolve antes de pedir a validação. Numa cópia de trabalho, o `--repo` roda nela (o aviso de cópia de trabalho é o único aceito ali) e, depois de o `originals/` ir ao mesmo caminho no checkout principal, roda de novo lá.

## O que entra

**Candidata** é cada fonte distinta que a triagem olhou: os resultados das buscas, sem repetir a fonte, com as cortadas pelo snippet e as que nunca abriram. A lista segue a ordem em que foram lidas, que é o que dá sentido a `traz_novidade`: fonte lida de novo fica na posição da primeira leitura, e as nunca lidas vão no fim.

**Objetivos** são as perguntas do próprio pedido, como vieram. Pedido que é só um tema: as perguntas das primeiras consultas. Apuração: o tema e o que a primeira fase declarou que falta. Nascem antes da coleta; pergunta que surge no meio da busca não entra, porque a condição de parada se mede contra o que se queria antes da coleta.

**Nada de texto de fonte** além de citação curta (até umas 25 palavras, como na ficha de `knowledge/sources/README.md`), e atribuição que ninguém conferiu vem marcada "não verificada". O arquivo vai para o git.

```json
{
  "nota": "quem rotulou, quando, o que a base já tinha no começo (ou nada registrado), o regime do destino (curadoria de quem pediu ou sob o veto, com o que a pessoa decidiu) e o que fugiu desta regra",
  "buscas": 12,
  "consultas": [{"id": "c1", "frente": "perplexity", "texto": "estudo X 2026", "objetivo": "O1"}],
  "objetivos": {"O1 <a pergunta, como veio>": "alcancado"},
  "fontes": [
    {"id": "autor-tema-2026", "url": "https://exemplo.org/estudo", "origem": "primaria", "registro": "registravel", "destino": "fonte", "conteudo": "dado", "traz_novidade": true, "lido": "texto", "consulta": "c1"}
  ]
}
```

| Campo | Valores | O que diz |
|---|---|---|
| `buscas` | número | as chamadas de busca das frentes do raso, somando as levas; abrir página e repetir por erro não contam |
| `consultas` | lista | cada uma dessas buscas, na ordem em que rodou (na mesma leva, a do disparo), inclusive a que não trouxe nada novo: `id` (`c1`, `c2`...), `frente` (`perplexity`, `gemini`, `codex`, `nativa`), `texto`, como foi escrito, e `objetivo`, obrigatório: o objetivo a que ela serve, pelo número (`"O2"`) ou numa lista (`["O1", "O2"]`). Na conferência da variação em português do `scripts/confere_rodada.py`, a consulta sem o campo é desvio, e o script sugere o objetivo provável |
| `objetivos` | `alcancado`, `em_parte`, `nao_alcancado` | o que a pesquisa conseguiu de cada objetivo |
| `id` | slug | o nome estável da fonte; o mesmo quando ela volta em outra rodada. Antes de criar um, procure a URL nos `rotulos.json` de `knowledge/research-rounds/` |
| `url` | o link, ou `null` | sem link (redirect que não se resolveu): `null`, mais `descricao`, curta, com o domínio. O redirect se resolve ao abrir, se entrar na shortlist; aí `url` muda e `id` fica |
| `origem` | `primaria`, `terceiro` | quem produziu o dado ou quem relata |
| `registro` | `registravel`, `so_citacao`, `descartada` | a classe da fonte no fim da rodada, pelo acesso e pela substância: `registravel` e `so_citacao` como no Passo 5 da `research` (a página vazia é `so_citacao`); `descartada`, cortada sem abrir ou aberta sem dado sobre o pedido. Ler só o resumo da própria fonte (`lido: resumo`) conta como abrir: sem dado sobre o pedido, é `descartada`; com dado e o texto acessível, `registravel`, e o corte, se houver, fica no `destino`; com dado e o texto fechado, `so_citacao` |
| `destino` | `fonte`, `citacao`, `fora`, `a_decidir` | o que aconteceu com ela: virou arquivo em `knowledge/sources/`, foi citada na síntese, não entrou, ainda não se decidiu. Começa em `a_decidir` |
| `conteudo` | `dado`, `opiniao_metodo` | o que ela traz |
| `traz_novidade` | `true`, `false` | por tudo o que se leu dela, traz um dado, método, número, regra ou fala datada que a base, as linhas acima dela no arquivo e o que se leu nas rodadas de que esta é complemento (as que a `nota` diz) não tinham |
| `lido` | `texto`, `resumo`, `resumo da busca`, `nada` | o que se leu dela: o texto; o resumo da própria fonte (abstract); o que o fornecedor ou a busca disse dela; nada. Pode levar um detalhe entre parênteses, como `texto (cap. 9)`; a leitura parcial diz qual parte. Cada rota tentada vai numa oração própria (`references/conferencias.md`, "Lacunas conhecidas") |
| `consulta` | `id` de `consultas` | a primeira da lista que trouxe a fonte. Fonte que não veio de busca: `via <id>` da fonte que a apontou, ou `via pedido`, quando veio no próprio pedido |
| `copia` | `true`, só quando é cópia | o documento é cópia de um original que está em outro lugar (um espelho de um PDF oficial). Vale para o documento, não para a rota: a primária lida pela Wayback não é cópia. Sem o campo, ninguém viu que é cópia |

**`registro` e `destino` são campos diferentes de propósito:** uma fonte pode abrir bem e ficar fora da base, e a mesma fonte pode ser `so_citacao` numa rodada e virar `fonte` depois, porque a seguinte abriu o texto. Descartar na shortlist ou por integridade muda o `destino` para `fora`, não o `registro`: aberta e substantiva, segue `registravel`. Na apuração da `story-angle`, "entra na peça" e "fica na base" são `fonte` ou `citacao`, e a fonte inteira descartada por integridade é `fora`; o número descartado numa fonte que fica não muda o `destino` dela. Quem testa a classificação lê o `registro`; o `destino` é o que aconteceu depois.

## Como uma sonda lê (opcional)

- **Classificar a fonte:** só as linhas com `lido` em `texto` ou `resumo`, tirado o detalhe entre parênteses (`resumo da busca` não entra); quem não leu não tem como rotular o conteúdo. Fonte que tem mais de uma linha dessas, em rodadas diferentes: vale a da última, na ordem que a `nota` dá.
- **Condição de parada:** a lista na ordem, os objetivos, as `consultas` e a `consulta` de cada linha, inclusive os arquivos de dado pontual. Linha com `lido: nada` fica fora da contagem: ninguém leu. Busca de que nada se abriu não conta como busca seca: ninguém olhou o que ela trouxe.
- **Ajuste e calibração se separam pela URL e pelo `id`:** linhas com a mesma URL (`null` não conta) ou o mesmo `id` ficam do mesmo lado, para a mesma fonte não cair nos dois.
