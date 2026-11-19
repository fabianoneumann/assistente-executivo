---
titulo: "data-context-extractor: o molde de definição de métrica e as perguntas que tiram o conhecimento de quem usa o dado (skill do plugin data da Anthropic, versão 1.1.0; recorte)"
tipo: instrumento
autor: "Anthropic"
publicado_em: 2026-09-29   # data de atualização do plugin no manifest.json da cópia local; a skill não traz data própria
capturado_em: 2026-11-10
licenca: "Apache 2.0 (arquivo LICENSE na raiz da pasta do plugin data: o texto padrão da licença, versão 2.0, de janeiro de 2004; a linha de copyright do apêndice está no modelo, 'Copyright [yyyy] [name of copyright owner]', e a pasta não tem arquivo NOTICE; o autor declarado em .claude-plugin/plugin.json é Anthropic). Texto da licença: http://www.apache.org/licenses/LICENSE-2.0"
areas: [data-analysis]
tags: [metric-definition, data-dictionary, glossary, tribal-knowledge]
---

# data-context-extractor: como se escreve a definição de uma métrica

Ficha de um **recorte** da skill `data-context-extractor` do plugin **data** da Anthropic (versão 1.1.0): só o molde de documentação de métrica e as perguntas que o alimentam. O resto (descoberta de esquema em banco de dados, geração e empacotamento de uma skill por empresa) fica de fora. A licença (Apache 2.0) permitiria copiar trechos; esta ficha não copia, e o texto da skill está no próprio plugin.

**Proveniência.** Não há url: o plugin veio sincronizado da conta do claude.ai (catálogo `anthropic-plugin-directory`) e foi desligado em 2026-11-10. O arquivo lido é `skills/data-context-extractor/SKILL.md` (215 linhas) numa cópia local feita naquele dia. Os números de linha são os dessa cópia.

**O que a fonte é e o que não é.** A skill serve para um assistente entrevistar analistas e gerar outra skill com o conhecimento da empresa sobre os próprios dados. Não cita estudo nem medição. O que interessa aqui é a forma que ela dá ao registro de uma métrica.

## O molde da métrica (linhas 188 a 193)

Cinco campos para cada métrica documentada:

| Campo | O que entra |
|---|---|
| Nome | o nome pelo qual as pessoas a chamam |
| Definição | a explicação em linguagem simples |
| Fórmula | a conta exata, com os campos que entram nela |
| Origem | de que tabela ou tabelas o dado vem |
| Ressalvas | casos de borda, exclusões e armadilhas |

A skill usa o mesmo desenho para outras duas coisas. A **tabela** leva o caminho completo, o que ela guarda e quando usá-la, como se identifica uma linha, de quanto em quanto tempo ela se renova, as colunas que importam (nome, tipo, descrição, observação), como ela se liga às outras e duas ou três consultas típicas como exemplo. A **entidade** leva o nome, o que ela é para o negócio, a tabela onde mora, o campo que a identifica, como se relaciona com as outras e os filtros que sempre se aplicam a ela (tirar os internos, os de teste).

## As perguntas que alimentam o molde (linhas 59 a 102)

A skill pede que venham uma a uma, em conversa, depois de olhar o esquema.

- **Sobre a entidade:** o que as pessoas querem dizer quando falam "usuário" ou "cliente", e se há tipos diferentes por trás da palavra. É a única que a fonte marca como crítica. O que se busca na resposta: mais de um tipo sob o mesmo nome (usuário, conta, organização), a cardinalidade entre eles e o campo que os liga.
- **Sobre o identificador:** qual é o principal e se a mesma entidade tem mais de um. Na resposta, separar a chave do banco da chave do negócio, notar se o identificador é UUID ou número inteiro e se sobrou um sistema antigo de identificação.
- **Sobre as métricas:** as duas ou três mais pedidas e a conta de cada uma: a fórmula exata, as tabelas e colunas que a alimentam e a convenção de período (últimos 7 dias, mês do calendário).
- **Sobre a limpeza:** o que se tira sempre antes de contar (dado de teste, interno, fraude, registro apagado). A resposta vira as condições de filtro que toda consulta leva e aponta as colunas que marcam o que sai.
- **Sobre os erros de quem chega:** os enganos que um analista novo costuma cometer com esse dado. A fonte lista o que esperar: nome de coluna que confunde, fuso, o jeito peculiar de tratar o vazio, e tabela de histórico confundida com a do estado atual.
