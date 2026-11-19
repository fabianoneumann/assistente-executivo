---
titulo: "Regras compartilhadas do plugin small-business da Anthropic (versão 1.35.1): o buraco no dado lido como fato, o denominador de outro universo e a hora errada"
tipo: instrumento
autor: "Anthropic"
publicado_em: 2026-11-10   # data de atualização do plugin no manifest.json da cópia local
capturado_em: 2026-11-10
licenca: "Sem licença declarada: a pasta do plugin não tem arquivo LICENSE nem NOTICE (raiz conferida em 2026-11-10: README.md, shared/, skills/, .claude-plugin/plugin.json, .mcp.json e .in_use), o README não fala de licença e o plugin.json só diz o autor, Anthropic. Tratado como protegido: entra só a ficha, em palavras próprias, sem o integral."
areas: [data-analysis]
tags: [missing-data, absent-vs-zero, denominator, timezone, connectors, reporting]
---

# small-business, pasta `shared/`: quando o número certo vira resposta errada

Ficha em palavras próprias, sem texto integral, porque o plugin não declara licença. A organização é nossa: o que a fonte defende, o que ela recomenda (arrumado pelo caminho de uma leitura, do que se lê ao que se calcula e ao que se escreve, e não pela lista de regras dela) e as ressalvas.

**Proveniência.** Não há url: o plugin veio sincronizado da conta do claude.ai (catálogo `anthropic-plugin-directory`) e foi desligado em 2026-11-10. Lidos numa cópia local feita naquele dia: `shared/absent-is-not-zero.md` (105 linhas, inteiro) e `shared/chain-seams.md` (152 linhas; a primeira parte, do denominador, a terceira, do fuso, e a seção final "The shared shape", linhas 128 a 137). O integral está lá, e é lá que se confere esta ficha.

**O que ficou de fora.** De `chain-seams.md`: a parte sobre prometer uma rotina que ninguém agendou e a nota sobre a ferramenta de sugestão de horário que dá como livre um dia ocupado. Não são leitura de números; a a pesquisa já registra a primeira.

## O que a fonte defende

Os dois arquivos tratam de um mesmo engano em dois tamanhos. No menor, falta um pedaço do dado e a falta é lida como informação sobre o negócio. No maior, um número correto dentro de uma skill é entregue a outra, que mede um conjunto diferente, e passa a valer para o conjunto errado. O segundo arquivo se apresenta como o primeiro "um nível acima".

O argumento para tratar isso como regra, e não como descuido eventual, é a direção do erro: para a fonte, a falta de dado se lê como boa notícia (menos dívida, nenhuma despesa, cliente recém-atendido), e resultado bom não desperta conferência. Ela diz que essas falhas só apareceram com conectores de verdade, porque o dado de teste nasce completo.

## O que ela recomenda, pelo caminho de uma leitura

**Antes de tudo, um teste.** Supor por um instante que o dado veio com defeito e ver se o valor na tela seria o mesmo. Se seria, ele sozinho não prova nada sobre o negócio, e o texto registra que não dá para saber qual das duas coisas aconteceu.

**Ao ler um zero ou um "nada encontrado".** Três situações produzem a mesma tela: o valor é zero de fato, o provedor não tem o dado, ou a consulta estava errada. A fonte pede um juízo de plausibilidade (na frase dela, "A company with no revenue is rare; a data provider with no figure is common.") e, quando o zero é implausível, que ele seja lido e escrito como desconhecido. Para o resultado vazio, pede uma segunda via de checagem antes de afirmar ausência; no caso que ela conta, a busca por um marcador de e-mail voltava vazia enquanto o próprio marcador acusava mensagens.

**Ao ler datas.** As duas pontas enganam. Registro sem data some dos filtros por período, ou passa por recém-movimentado, quando é justamente o que nunca foi tocado. Registro com data posterior a hoje é defeito, e numa ordenação por recência vai para o primeiro lugar. Os dois saem da fila comum: formam um grupo à parte, com nome próprio, tratado como o mais preocupante.

**Ao ler uma hora.** A agenda usada de exemplo guardava, para cada evento, três indicações de fuso que discordavam entre si: o deslocamento gravado no horário, o rótulo de fuso do evento e o fuso padrão da conta. Imprimir o relógio como veio dava três horas de erro. A hierarquia que a fonte fixa: manda o deslocamento gravado; o padrão da conta não informa onde a pessoa está (informa onde a conta foi aberta), então o fuso de quem lê se pergunta uma vez e fica guardado; a hora sai convertida e com o fuso escrito quando vai para terceiros; e a discordância entre as indicações é relatada.

**Ao totalizar.** O risco é somar um pedaço achando que é tudo. Acontece de dois jeitos: a chamada trouxe só os primeiros itens (limite ou paginação), ou trouxe um resumo pronto junto com as linhas e o resumo não bate com elas, coisa que a fonte diz ter visto em mais de um conector. Total, portanto, só do conjunto inteiro e a partir das linhas; fora disso, o número sai com o aviso de que é parcial.

**Ao dividir.** Um total pode acompanhar o trabalho como pano de fundo, mas não serve de base para uma taxa de algo que só alcança parte dele. O caso da fonte é o retorno de anúncios de uma loja virtual calculado sobre a receita da empresa toda, sendo a loja uma fatia mínima: o retorno aparece dezenas de vezes maior do que é, e é esse número que orienta a verba seguinte. Duas práticas saem daí: escrever a parte e o todo lado a lado, e desconfiar da razão que sai uma ordem de grandeza melhor do que o setor permitiria, começando a conferência pelo denominador.

**Ao ter dois números para a mesma coisa.** Quando duas contagens do mesmo objeto se afastam por uma ordem de grandeza, a explicação provável é que não contam o mesmo objeto. O texto registra qual delas entrou e a razão, em vez de ficar com uma sem aviso.

**Ao redigir.** Basta uma frase que diga de que fonte veio cada número e para que ela serviu; a mecânica do conector não interessa a quem lê. O que ficou sem apurar entra como lacuna, com nome, e nada se põe no lugar. A justificativa, na frase da fonte: "A named gap is useful. A fabricated zero is worse than silence".

## Ressalvas

- **Sem medição.** São regras de quem escreveu o plugin, a partir de falhas que diz ter visto. Não há contagem, método de coleta nem estudo. A fonte afirma que este é o jeito mais comum de as skills dela errarem com segurança e que lista as regras pela frequência; nenhuma das duas afirmações vem com número.
- **A direção do erro não é sempre a mesma.** A fonte afirma que o buraco esconde o problema, mas a tabela de casos dela traz o contrário também (um produto que vende bem lido como encalhado).
- **Os valores são de cenário.** Os totais em dólar, a loja como 2,4% da receita, o retorno de 4,7 vezes relatado como 194 vezes e as três horas de erro pertencem ao exemplo do plugin (uma torrefadora com cafés, atacado e loja virtual) e não se carregam.
- **O contexto é outro.** As skills leem livros contábeis, loja virtual, funil de vendas e agenda de uma empresa pequena, com valores em dólar. O que se transporta é o raciocínio, não os casos.
