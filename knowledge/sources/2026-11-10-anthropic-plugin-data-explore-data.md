---
titulo: "explore-data: grão, completude e dado suspeito ao conhecer um conjunto de dados (skill do plugin data da Anthropic, versão 1.1.0; recorte)"
tipo: instrumento
autor: "Anthropic"
publicado_em: 2026-09-29   # data de atualização do plugin no manifest.json da cópia local; a skill não traz data própria
capturado_em: 2026-11-10
licenca: "Apache 2.0 (arquivo LICENSE na raiz da pasta do plugin data: o texto padrão da licença, versão 2.0, de janeiro de 2004; a linha de copyright do apêndice está no modelo, 'Copyright [yyyy] [name of copyright owner]', e a pasta não tem arquivo NOTICE; o autor declarado em .claude-plugin/plugin.json é Anthropic). Texto da licença: http://www.apache.org/licenses/LICENSE-2.0"
areas: [data-analysis]
tags: [data-profiling, data-quality, completeness, grain, placeholder-values]
---

# explore-data: o que olhar num dado antes de calcular qualquer coisa

Ficha de um **recorte** da skill `explore-data` do plugin **data** da Anthropic (versão 1.1.0): só o que serve a ler números sem se enganar (o grão, a completude e o dado suspeito). O resto da skill (acesso a banco, perfil coluna a coluna, consultas de esquema, sugestão de análises) fica de fora. A licença (Apache 2.0) permitiria copiar trechos; esta ficha não copia, e quem quiser o texto da skill o encontra no próprio plugin.

**Proveniência.** Não há url: o plugin veio sincronizado da conta do claude.ai (catálogo `anthropic-plugin-directory`) e foi desligado em 2026-11-10. O arquivo lido é `skills/explore-data/SKILL.md` (325 linhas) numa cópia local feita naquele dia. Os números de linha são os dessa cópia.

**O que a fonte é e o que não é.** Instrução para um assistente traçar o perfil de uma tabela ou arquivo. Não cita estudo nem medição, e ela mesma se apresenta como heurística: no fim, avisa que um sinal de qualidade pede uma olhada rápida, não uma condenação, porque nem todo sinal é defeito (linha 325).

## O grão vem antes da conta (linhas 39 a 48 e 253 a 261)

Antes de analisar, cinco perguntas sobre a tabela: o tamanho (linhas e colunas); o grão, isto é, a que corresponde cada linha; a chave, e se ela se repete; a data da última atualização; e o começo da série. O molde que a skill propõe para documentar uma tabela fixa essas respostas em campos (o grão, a chave, a contagem aproximada com a data em que foi feita, a frequência de atualização) e soma dois: uma frase sobre o que a tabela representa e quem responde por ela.

## Completude: quanto do campo veio preenchido (linhas 174 a 182)

Cada coluna recebe uma nota pela fração preenchida, em quatro faixas que vão de "completa" a "esparsa". No meio, o que muda é o que fazer: na quase completa, olhar os vazios; na incompleta, descobrir a causa e decidir se ela pesa; na esparsa, a coluna talvez só sirva depois de preenchida por estimativa. Os cortes das faixas estão na seção de números, abaixo.

## Dado suspeito (linhas 110 a 120 e 184 a 207)

- **Valor de marcador no lugar do dado:** 0, -1, 999999, "N/A", "TBD", "test", "xxx". O zero está na lista.
- **Valor padrão:** um mesmo valor com frequência alta demais para ser natural.
- **Dado parado:** a data de atualização não mostra mudança recente num sistema que está em uso.
- **Valor impossível:** quantidade negativa onde só cabe positiva, data no futuro em dado histórico, data final antes da inicial, porcentagem acima de 100, idade acima de 150, duração negativa.
- **Viés de número redondo:** valores que terminam sempre em 0 ou 5 indicam que alguém estimou, não mediu.
- **Inconsistência entre colunas:** estado "concluído" com a data de conclusão vazia; chave estrangeira sem registro correspondente.
- **O mesmo conceito escrito de vários jeitos,** número guardado como texto, datas em formatos diferentes, maiúsculas misturadas e espaço sobrando no fim.
- **Duplicata:** ver se existe chave natural e se ela se repete.
- **Cardinalidade que surpreende:** um identificador com poucos valores distintos, ou uma categoria com valores demais.
- **Distribuição muito torta:** pode distorcer a média.
- **Atualidade:** quando foi a última atualização, qual a frequência esperada, se há atraso entre o fato e a carga, e se a série tem buracos.

## Correlação e tabela grande (linhas 239 a 245 e 321 a 325)

Entre colunas numéricas, a skill manda montar a matriz de correlação de todos os pares, marcar as fortes para investigar e procurar também relação que não é reta (quadrática, logarítmica), e manda dizer com todas as letras que correlação não prova causa. Em tabela muito grande, o perfil sai de uma amostra, e quem precisa da contagem exata deve pedir.

## Números da fonte, sem lastro

A fonte não diz de onde vêm; entram aqui como número da fonte, sem medição própria nem referência.

- **Faixas de completude:** acima de 99% preenchido, completa; de 95% a 99%, quase completa; de 80% a 95%, incompleta; abaixo de 80%, esparsa (linhas 178 a 182).
- **Taxa de vazio:** acima de 5%, aviso; acima de 20%, alerta (linha 114).
- **Correlação forte:** acima de 0,7 em módulo (linha 243).
- **Tabela grande, para a amostragem:** a partir de 100 milhões de linhas (linha 323).
