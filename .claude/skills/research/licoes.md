# Lições da skill `research`

O que o uso e a edição desta skill ensinaram. Antes de usar a skill, leia as abertas e as apontadas; ao terminar, registre a lição nova aqui, na mesma entrega, em "Abertas", com as quatro perguntas da revisão depois da ação (o que devia acontecer, o que aconteceu, por quê, o que mudar), quando vale, a evidência (arquivo e linha), a gravidade (crítica, maior, menor) e as ocorrências. A lição de procedimento vira regra sem mesa quando a correção já funcionou num caso real; a que toca critério de quem decide, custo ou publicação espera a decisão dessa pessoa. A regra de procedimento que reincide ganha antes uma conferência automática. Formato, estados (aberta, apontada, a sair, virou regra, reincidiu, saiu) e porquê em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md). Lição que vale para várias skills fica em [`../licoes-gerais.md`](../licoes-gerais.md).

As regras abaixo vieram do uso desta skill noutro ambiente e já estão no `SKILL.md` ou nas referências; ficam aqui com o porquê, para quem usa saber de onde vêm e reconhecer a reincidência. As limitações conhecidas dos conferidores estão em [`references/conferencias.md`](./references/conferencias.md), "Lacunas conhecidas".

## Abertas

Nenhuma.

## Viraram regra

| Regra | Por quê | Onde está |
|---|---|---|
| Consulte a base antes de buscar fora, com a pergunta escrita de várias formas e os termos do assunto vizinho, inclusive fora de `knowledge/` | é a regra que mais reincide: a busca pelas palavras do pedido deixa de fora a decisão ou a síntese que já respondia | Passo 0b; ritual Query de `knowledge/README.md` |
| Abra a primária antes de usar um número; o resumo do fornecedor ou do WebFetch não basta | os resumos cortam e trocam dados, e o número errado chega à síntese | Passo 5 |
| Resposta sem citações: extraia a lista inteira das afirmações e rode uma leva dirigida a elas | a lista parcial deixa sair a afirmação que mais pesava | Passo 5; `confere_rodada.py` (e) |
| Público brasileiro: pelo menos uma variação em português por objetivo | o que vem do Brasil quase não chega pelas consultas em inglês | Passo 2.5; `confere_rodada.py` (a) |
| Pergunta que nomeia mais de um produto ou versão: uma consulta dirigida a cada um | as frentes respondem sobre o produto mais conhecido e calam o outro | Passo 2.5; `confere_rodada.py` (b) |
| Rotule todas as candidatas da triagem, não só as que entraram | sem a lista inteira, a condição de parada não se mede e a mesma fonte ganha rótulos opostos | Passo 5; `references/rotulos.md`; `confere_rodada.py` (c) |
| Esgote as rotas para a primária que não abre antes de dar "só citação" | as rotas (Wayback para a página fora do ar, editora, resumo oficial, Chrome) costumam abrir | `knowledge/sources/README.md`, "Quando a primária não abre"; `confere_rodada.py` (d) |
| Cole a saída de cada busca nativa num `qN-nativa.md`, como veio | ela volta na conversa, e sem o arquivo a revisão não confere a leva | Passo 2 |
| Marque a leitura do assistente desde o primeiro rascunho, e não a tire ao reescrever | sem a marca, a leitura nossa vira motivo atribuído a uma fonte | Passo 5 |
| Passe a lista "Itens que de fato se esquecem aqui" antes de chamar a revisão | as regras reincidem juntas, e só a revisão as pegava | `references/revisao.md` |
| Revise no fim do Passo 5 e no Passo 7, por agentes que não fizeram o trabalho | quem fez confia no próprio rascunho | seção "Revisão" |
| Commit só depois da validação, em bloco pelos caminhos, com a conferência própria antes | commit a cada passo cria ruído em conteúdo ainda a curar | Passo 7, item 6 |
| A ficha extrai o máximo da fonte, em palavras próprias e sem interpretação; o `parafrase.py` roda em toda ficha de obra protegida | ficha curta perde o conhecimento, e a ficha que segue a fonte frase a frase vira cópia | Passo 7, item 1; `references/conferencias.md` |
| Copie a conta do `parafrase.py` do cabeçalho da última saída, medida depois da última edição, contra todos os textos da fonte | a conta escrita de memória ou de uma medida anterior não bate com a ficha final | `references/conferencias.md` |
| A linha que vira custo de teste ou recomendação, e a fonte que contesta a tese, se leem inteiras | o trecho que responde à pergunta não traz o aviso que muda a recomendação | `references/conferencias.md`, Passo 5 |
| Os buscadores concordando são secundárias: confirmado é o lido na primária | já erraram juntos o ponto que mais pesava | Passo 5, "O peso das fontes" |
| Confira o bloco extraído (tamanho, título) e os dados embutidos da página antes de ler | o `<article>` ou o `<main>` pode ser outra coisa, e o conteúdo pode estar no JSON da página | Passo 5 |
| Antes de "a fonte não diz", busque sem corte de saída e diga o termo e a contagem; o resumo de um grupo sai de script sobre o grupo inteiro | a saída cortada do terminal foi lida como ausência e como faixa de números | Passo 5 |
| Guarde cada versão do rascunho antes de corrigir, e trate a fonte que entra pela correção como rascunho do Passo 5 | sem a v1 a re-revisão não compara, e a fonte nova não passou por revisão | `references/conferencias.md` |
| Em fila ou loop, chame a skill pela ferramenta Skill em cada item e diga o nível da revisão | o loop repete de memória, e o que depende de outro agente cai primeiro | `references/conferencias.md` |
| Conte o fim de linha de cada arquivo novo em Python, e grave em binário no script que registra | no Windows, o shell e o `write_text` gravam CRLF, e o `git status` não mostra | `references/conferencias.md`, Passo 7 |
| Confirme o profundo com quem pede, salvo pedido explícito | custa bem mais que o raso, e a decisão de gastar é dela | Passo 1 |
| No 429 do Perplexity, tente de novo com espera crescente antes de devolver o erro | levas em paralelo batem no limite de taxa | `scripts/perplexity_search.py` |
| Vários agentes na mesma rodada: faixa de ids e subpasta de trabalho para cada um | os ids colidem e um agente desatualiza o trabalho do outro | `references/conferencias.md` |
