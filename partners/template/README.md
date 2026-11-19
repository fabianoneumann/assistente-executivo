# Modelo da pasta de um parceiro

A pasta de um parceiro ou cliente em branco: o dossiê e os modelos de cada documento, com as seções, a ordem e a forma que já se provaram em uso, e nenhum conteúdo. Para abrir um parceiro novo, copie daqui; o que se escreve depois é do parceiro, e o modelo continua em branco.

## A árvore

```
template/
├── README.md                          este arquivo
├── parceiro-dossie.md                 o dossiê: quem é, o que quer, o que já se propôs
├── proposals/modelo-proposta.html     o que se vende
├── contracts/modelo-acordo.html       o que formaliza um negócio fechado
├── deliveries/modelo-entrega.html     o que encerra: o prometido comparado com o feito
├── reports/
│   ├── README.md                      o ritual do relatório semanal (cadência, varredura, voz)
│   └── modelo-relatorio-semanal.html  o relatório de cada semana
├── meetings/modelo-reuniao.md         o que uma reunião produziu
├── workshops/modelo-workshop.md       o roteiro de um treinamento ou workshop
└── clients/cliente/cliente-dossie.md  o cliente final, quando o parceiro é o canal
```

## Como usar

1. **Ao abrir o parceiro,** crie `partners/<parceiro>/` (o nome em minúsculas e com hífens, sem acento) e copie para lá só o `parceiro-dossie.md`, renomeado para `<parceiro>-dossie.md`.
2. **Cada pasta nasce com o primeiro documento dela:** na primeira proposta, crie `proposals/` e copie o `modelo-proposta.html` com o nome final. Pasta vazia não se cria.
3. **Os nomes começam pela data,** para a pasta se ordenar sozinha: `AAAA-MM-DD-<escopo>.html` na proposta, no acordo e na entrega (o escopo diz a etapa de trabalho); `AAAA-MM-DD-semana-NN.html` no relatório semanal (a data é a do corte); `AAAA-MM-DD-<tema>.md` na reunião e no workshop.
4. **Troque cada marcador** e apague as instruções; o documento pronto não tem nenhum `{{`. Uma busca por `{{` no arquivo mostra o que falta.
5. **Para o PDF,** abra o HTML no navegador e imprima como PDF: os estilos de impressão já estão no arquivo (quebra de página, margens, cores).

Por que as pastas se separam assim: a proposta vende o que ainda não existe, o acordo formaliza o que se fechou e a entrega mostra o que foi feito, e cada uma se procura por uma pergunta diferente. O relatório acompanha um trabalho em curso; a reunião guarda o que uma conversa decidiu. Outra pasta que o parceiro pedir (um diagrama, um material recebido) nasce com o nome do que ela é.

## Os marcadores

| Marcador | O que vai no lugar |
|---|---|
| `{{parceiro}}` | o nome do parceiro, como ele se apresenta |
| `{{razao_social}}` | o nome jurídico, quando o documento pede |
| `{{contato}}` | a pessoa a quem o documento se dirige, com o papel dela |
| `{{cliente}}` | o cliente final, quando o trabalho é para um cliente do parceiro |
| `{{autor}}` | quem prepara o documento |
| `{{marca_autor}}` | a marca ou a empresa de quem prepara |
| `{{email}}`, `{{telefone}}`, `{{link_perfil}}` | o contato de quem prepara, no rodapé |
| `{{data}}` | a data no formato `AAAA-MM-DD` (nome de arquivo, frontmatter) |
| `{{data_extenso}}` | a data por extenso, no cabeçalho do documento |
| `{{periodo}}`, `{{prazo}}` | o intervalo que o documento cobre, o prazo do trabalho |
| `{{titulo}}` | o título do documento |
| `{{campo: instrução}}` | um texto a escrever: a instrução diz o que vai ali e como |

O que fica entre `<!-- -->` no HTML é orientação para quem preenche: uma seção opcional, um bloco que se repete. Pode ficar, porque não aparece na página nem no PDF, ou sair.

## A marca fica nos tokens

Cada modelo HTML abre o `<style>` com um bloco `:root` de tokens: as cores, as duas famílias de letra e a largura da página. **É o único lugar da marca.** O resto do CSS lê dali, e nenhuma cor aparece solta fora do bloco. Para pôr a identidade da sua equipe, troque os valores do `:root` e a linha das fontes no `<head>` (o `<link>` do Google Fonts, ou o carregamento da letra que vocês usam), nos modelos, uma vez: todo documento novo já nasce com a marca. O documento enviado fica com a marca que tinha quando saiu.

O padrão é um tema claro com Space Grotesk e JetBrains Mono: a acentuação em ciano, um degradê de ciano a roxo na linha do topo, cartões com borda fina e os números de seção em letra mono. A entrega tem também os tokens dos marcadores de situação (entregue, de outro jeito, parcial, fora, além), e o relatório, o do risco.

## Cada documento

- **Dossiê** (`parceiro-dossie.md`): a ficha (nome, contato, canais, atuação), o que a empresa é, o engajamento (como entrou, o que quer, o que pediu, a natureza do trabalho), os sistemas e as dores, os clientes em conjunto e a lista das propostas com o estado de cada uma. O frontmatter `status` diz se o parceiro está ativo, pausado ou encerrado.
- **Proposta** (`proposals/`): o cabeçalho (para quem, por quem, prazo, data), contexto, as frentes de trabalho em cartões, o modelo de trabalho, as opções, prazo e investimento em tabela, o que não está incluso, a propriedade, os próximos passos e quem conduz.
- **Acordo** (`contracts/`): objeto, escopo, prazo e dedicação, valores e pagamento, a participação adicional (opcional), propriedade e confidencialidade, a natureza do acordo com o aceite e, se houver, as assinaturas. O modelo é a forma; os termos de cada acordo são das partes, e o que tiver peso jurídico passa por quem entende disso.
- **Entrega** (`deliveries/`): o resumo com os números do período, cada item da proposta comparado com o que foi feito (prometido, entregue, a mudança, a prova, com um marcador de situação), o roteiro mês a mês, o modelo de trabalho, o que foi além, o que mudou de lugar ou ficou aquém e por quê, e o que fica para depois.
- **Relatório semanal** (`reports/`): resumo, concluído, em andamento, em curso com terceiros. O ritual, com a varredura antes de escrever e as regras da seção de terceiros, está no [`reports/README.md`](./reports/README.md).
- **Reunião** (`meetings/`): o que se esperava, o que aconteceu, o que se decidiu, o que ficou em aberto e o próximo passo. A transcrição, quando guardada, fica num `originals/` ao lado, fora do git.
- **Workshop** (`workshops/`): o roteiro interno de um treinamento, bloco a bloco, com a calibragem antes e as notas de condução.
- **Cliente final** (`clients/<cliente>/`): quando o parceiro é o canal e há um cliente dele no trabalho. A pasta guarda o dossiê e o material que alimenta as peças (matrizes, comparativos, insumos); a peça enviada continua em `proposals/` ou `contracts/` do parceiro.

## O que nunca vai ao modelo

Nenhum nome, valor, preço, cliente, pessoa, e-mail, telefone ou detalhe comercial de um parceiro real. Quando um documento pronto ensinar uma forma nova (uma seção, um bloco, um estilo), ela volta ao modelo como esqueleto, com marcadores no lugar do conteúdo.
