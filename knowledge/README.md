---
area: Conhecimento
cadencia: 14d
---

# Knowledge: a base de pesquisa e estudo

A base de conhecimento sobre o mundo de fora (método, pesquisa, dados, temas de estudo), no padrão LLM Wiki: arquivos markdown que acumulam contexto ao longo do tempo, em vez de redescobrir tudo a cada conversa. É o corpus que o assistente pesquisa, acumula e consulta como referência, distinto do resto do repositório, que é sobre o trabalho de quem usa (contexto, decisões, peças, entregáveis).

> Regra divisória: *"isso é pesquisa, fonte ou estudo (vai aqui) ou é um fato operacional de um domínio (vai ao domínio, com link para cá)?"* Um achado de pesquisa que muda uma decisão é refletido por referência no arquivo do domínio (`context/`, `decisions/`); a pesquisa e a fonte ficam aqui.

## As duas camadas

- **`sources/`:** a camada bruta, de fontes **imutáveis** (artigos, transcrições, papers, notas de estudo, posts), cada uma com a proveniência. Ninguém reescreve uma fonte. Convenção de nome, frontmatter e a régua do que é de terceiro em [`sources/README.md`](./sources/README.md).
- **`<área>/`:** as páginas de **síntese** escritas pelos agentes: conceitos, comparações, a tese que evolui. Interligadas com `[[...]]` e citando as fontes pelo nome do arquivo. É o que compõe ao longo do tempo. Cada área tem o seu `index.md`: uma linha por página, com quando ler, os termos-chave (em português e em inglês) e as fontes.

As rodadas da skill `research` (as saídas das buscas, os rótulos e as notas de cada pesquisa) moram em [`research-rounds/`](./research-rounds/README.md).

## Como uma área nasce

**Não se cria pasta de área vazia por antecipação.** Uma área nasce no primeiro ingest de uma fonte daquele tema, com nome em inglês (a taxonomia é em inglês; o conteúdo, em português). A área nasce com o próprio `index.md` e ganha uma linha na porta de entrada ([`index.md`](./index.md)). Por que dois níveis: com uma porta só, a lista de páginas cresce até o agente não achar o que procura; a porta diz a área, e o índice da área diz a página.

Estudos avulsos fora das áreas existentes entram como fonte em `sources/` e ganham área própria só quando acumulam massa.

## Os três rituais

**Ingest.** A entrada em `sources/` depende de quem curou a fonte:

- **Fonte curada por quem usa** (a pessoa passa um link ou documento específico): vai direto para a camada bruta, inteira ou em ficha conforme a licença (regra em [`sources/README.md`](./sources/README.md), "Conteúdo de terceiros"); nunca só o link, porque link apodrece. A URL fica no frontmatter. Na ficha de obra protegida, a cópia de trabalho vai ao fim da ingestão para `sources/originals/<nome da ficha>.<ext>`, fora do git.
- **Pesquisa aberta** (o assistente garimpa, e a busca traz muitos resultados de relevância desigual): **triagem primeiro, registro depois**. Buscar, filtrar por relevância e qualidade da fonte, apresentar uma shortlist ("estes N valem, por quê; descartei estes, por quê"), e só o que passa (e que a pessoa não vetou antes do commit) vira fonte. A camada bruta é curada, não um log de tudo o que a busca devolveu. O `log.md` pode registrar "pesquisei X, shortlist Y" para não refazer o mesmo chão. Na `story-angle`, a curadoria acontece na mesa de ângulos.

Depois de as fontes entrarem: discutir os takeaways, criar ou atualizar as páginas de síntese na área (criando a pasta se for a primeira), atualizar o índice da área e, se a área nasceu ou mudou o que cobre, a porta de entrada, e registrar em [`log.md`](./log.md). Se a fonte gera um achado operacional, refletir por referência no arquivo do domínio. Ingerir uma fonte por vez e conversar os pontos antes de sintetizar; na `research`, a conversa dos takeaways acontece na validação antes do commit, sem pausa no meio do registro.

**Query.** Ler a porta de entrada ([`index.md`](./index.md)), abrir o índice da área (mais de um quando a pergunta cruza áreas, e os temas transversais da porta dizem quais), abrir as páginas relevantes e responder com citação da fonte. Quando o índice não basta e é preciso buscar nos arquivos:

1. escrever a pergunta de várias formas antes de buscar: os termos em português e em inglês, os sinônimos e uma frase de como a resposta estaria escrita, e buscar cada um;
2. o acerto exato vem primeiro (nome próprio, nome de arquivo, número);
3. ir do mais curado ao mais bruto: sínteses, depois fontes, e, quando a busca serve à produção, as ideias e as peças; e olhar também o que o repositório já decidiu fora da base sobre o tema (`decisions/`), que a busca só em `knowledge/` não acha;
4. ler o trecho antes do arquivo (`grep -n -C`) e abrir o arquivo inteiro só quando o trecho confirma;
5. registrar o resultado no que se escreve em seguida (pauta, roteiro, nota): no que se apoia, o que contraria, os termos usados na busca, e "nada registrado" quando a base está vazia, que também é um achado.

Resposta boa (uma comparação, uma tese, uma conexão) vira página nova aqui, e não se perde no chat.

**Lint.** Varrer por contradições entre páginas, fontes órfãs (sem página que as cite), páginas sem link de entrada, conceitos citados sem página própria e lacunas que pedem pesquisa nova.

## Multiagente

Este README é o schema: qualquer agente, na mesma sessão ou em outra, o lê antes de ingerir ou consultar, e escreve seguindo os rituais acima. A porta de entrada e os índices de área são o caminho para achar o que já existe antes de criar página nova. É isso que mantém a base coerente entre agentes.

## Manutenção

Teto de cerca de 150 linhas por página de síntese; se passar, dividir numa mais específica. As fontes em `sources/` ficam fora do teto (uma fonte é um arquivo, de qualquer tamanho, e é imutável), e o `log.md` também, como linha do tempo que só cresce. A cascata vale dentro da base: página nova ou com o critério de leitura mudado atualiza o índice da área; área nova ou com o escopo mudado atualiza a porta de entrada.
