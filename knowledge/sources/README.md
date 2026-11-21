# Sources: a camada bruta

Fontes brutas e **imutáveis**. O assistente lê daqui, sintetiza nas páginas de área, mas **nunca reescreve uma fonte**. É a proveniência da base: de onde veio cada dado, quem disse, quando.

## Nomeação

- Um arquivo por fonte: `AAAA-MM-DD-<slug>.md` (a data é a da captura).
- Se a fonte tem imagens ou anexos, vira subpasta com o mesmo nome, e os arquivos ficam dentro.
- `slug` curto, em minúsculas com hífens; nomes próprios em português quando forem o assunto.

## Frontmatter (obrigatório)

```yaml
---
titulo: "Título da fonte"
tipo: artigo          # artigo | video | palestra | filme | livro | roteiro | paper | nota-de-estudo | post-social | instrumento | pratica-propria
autor: "Nome do autor"
url: "https://..."     # quando houver
publicado_em: 2026-02-05   # data da fonte original (quando houver)
capturado_em: 2026-07-11   # quando entrou na base
areas: [agent-engineering, journalism]   # uma fonte pode alimentar várias áreas
entrada: pesquisa      # curadoria | pesquisa | pratica-propria
licenca: "CC BY 4.0 (indicada na página do arXiv)"   # qual é e onde está escrita
tags: [source-evaluation, fact-checking]   # opcional; temas finos para análise cruzada, em inglês
---
```

`entrada` diz quem trouxe a fonte: `curadoria` (quem usa o ambiente passou o link ou o material), `pesquisa` (veio de uma busca do assistente, na `research` ou na `story-angle`) ou `pratica-propria` (o registro de uma prática da equipe, no tipo de mesmo nome). O peso da fonte trazida pela curadoria vale para escolher o tema e o ângulo; o fato se decide na fonte primária, também contra a fonte curada (`decisions/pesquisa-tooling.md`).

`licenca` decide o que se guarda (abaixo). `tags` serve para cruzar assuntos finos entre áreas, independentemente da área.

O corpo é o material bruto: o clipping do artigo, a transcrição, a anotação de estudo, sem edição interpretativa. A interpretação vive nas páginas de síntese, que citam a fonte pelo nome do arquivo. No corpo, só o que aquela fonte diz: o confronto com outras fontes e a contradição entre elas são da síntese; autor e data que não vêm do próprio documento levam a origem deles (a referência de uma enciclopédia, os metadados do PDF). Por quê: ficha que mistura o confronto com outras fontes deixa de ser proveniência, e autor ou data tirados de terceiro, sem dizer de onde, já vieram errados.

**Prática própria** (`pratica-propria`): fonte que registra a prática da equipe num projeto, sem ser referência externa (o processo, o ferramental, as decisões de um repositório). Entra como ficha em palavras próprias, com a proveniência exata (repositório, caminhos, commit e data), e imutável como as demais. Dado de cliente, detalhe comercial e código de produto ficam fora.

## Este repositório é público

Este modelo é público, e a régua abaixo vale com um aperto: **nada de texto integral no repositório**, mesmo de licença livre.

- **A ficha de fonte de licença livre** vem em palavras próprias, como a de fonte protegida, sem o texto integral nem seção de trechos copiados: o integral se lê na fonte, pelo link do frontmatter. Antes de entrar, a ficha passa pelo `parafrase.py` da `research` contra o integral, e a que tem trecho colado fica fora até ser reescrita.
- **A ficha de fonte protegida** vem em palavras próprias, com até três citações curtas, de até umas 25 palavras cada.
- **Não entram:** a ficha de post de rede social de uma pessoa (o Reel, o post, o fórum) e a ficha de livro protegido, mesmo de amostra da editora. A síntese que se apoiava nelas cita a fonte pela citação simples (título, autor, link), sem ficha. A ficha livre que ainda não passou pelo `parafrase.py` também vem só como citação simples.
- **O conteúdo de curso pago não entra** (aula, apostila, material distribuído só a quem comprou). O material que o autor deixa aberto (aula de evento gratuito, vídeo, podcast, página, resumo em PDF de acesso livre) entra como qualquer fonte: em palavras próprias, com a fonte citada.
- **No repositório que você criar a partir deste modelo, privado,** a régua completa abaixo volta a valer, com o integral da fonte livre. Se o seu repositório for público, siga este aperto.

## Conteúdo de terceiros: inteiro ou em ficha, conforme a licença

O que decide é a licença da fonte, porque "público" (aberto a qualquer um) não é "domínio público" (livre para copiar), e o assistente não escreve a cópia integral de conteúdo protegido.

1. **Licença que permite cópia** (domínio público, Creative Commons sem a cláusula não comercial, inclusive o vídeo marcado assim, documentação e repositório com licença MIT ou Apache, texto oficial liberado): guarda-se o texto integral, com o campo `licenca` dizendo qual é e onde está escrita. Fica no mesmo arquivo da fonte, de qualquer tamanho: a ficha vem em cima (é o que as sínteses citam) e o integral embaixo, na seção "Texto integral", com a atribuição (o autor, a fonte, o nome da licença e o link dela). **Antes de salvar, conferir que o integral é da página da `url` do frontmatter** (o título e o começo do texto batem com ela), porque já veio integral de outra página do mesmo site. O integral sai do arquivo baixado, por `grep` ou por script, nunca do que o terminal mostrou (abaixo, "Citação e cobertura").
   - **Cláusula não comercial (NC):** a licença Creative Commons com NC (BY-NC, BY-NC-SA, BY-NC-ND) entra como o item 2, só a ficha, porque o repositório serve a um negócio; a ficha diz onde está o integral (a `url` e, quando houver, o PDF), e a síntese que a cita registra o mesmo numa linha.
   - **Cláusula sem derivadas (ND):** muda a forma da ficha, não o que se guarda: o BY-ND, que permite cópia, segue com o integral do item 1, e o BY-NC-ND, só com a ficha. Nas duas, a ficha de obra ND não traduz em sequência o texto argumentativo do autor (conclusões, limites, recomendações): nenhum trecho de três ou mais frases seguidas da fonte, na ordem dela, que o `parafrase.py` da `research` aponta. Os fatos, os números e as tabelas de fatos ficam fora dessa medida. Por quê: a licença veta por escrito a obra derivada, e a tradução contínua de um trecho é o que mais se aproxima dela; os fatos não são do autor.
2. **Protegido, mas aberto** (o vídeo comum, inclusive sem legenda para baixar; o artigo; o PDF de aula gratuita; o livro oferecido de graça sem licença aberta): o assistente baixa do link oficial ou lê pelo navegador para a cópia de trabalho (abaixo), faz ali a extração e entra na base a **ficha de estudo**, completa e em palavras próprias; o integral não entra. Markdown que outra pessoa extraiu só vale quando a licença do original permite a cópia, e depois de conferido contra a versão oficial. O conteúdo serve de base para criar com a voz de quem usa, nunca para publicar como está. A fonte curta sai num destes formatos, e quem escreve diz qual na proveniência da ficha:
   - **Ficha de prosa,** para o ensaio ou texto curto de um autor de referência, cujo raciocínio vale comparar com o de outros: em palavras próprias, escrita das notas (ler, anotar as ideias, fechar a fonte e escrever a partir das notas), organizada por outra pergunta (definições, recomendação, ressalvas), não pelas seções da fonte.
   - **Nota de fato,** para a fonte técnica (dado, receita, passo, documentação, guia, comparação de ferramentas): "Em uma frase"; tabelas de fatos, cada célula um fato; "O que a fonte recomenda", em 2 a 4 linhas próprias que juntam lugares diferentes da fonte; até três citações curtas e exatas, na língua da fonte; e "Lacuna", com o que a fonte não diz. Os passos de um método podem ir numa lista numerada, porque a ordem é o método. A página técnica que lista fatos e a documentação técnica longa podem seguir a ordem da fonte, desde que a ficha não cole frases.
   - **Reportagem e notícia:** nota de fato, com "O que a fonte afirma" no lugar de "O que a fonte recomenda", as falas atribuídas como citação curta com quem disse, e uma linha para o ângulo da matéria.
   - **A conferência lado a lado:** quem escreve conta quantas unidades da ficha seguem uma da fonte, sobre o total das unidades da ficha (as frases de prosa e as células com texto corrido), e diz as duas contas ("7 de 19"). Segue a fonte a unidade que traduz uma frase dela, a que junta duas e a que funde três ou mais seguidas, na ordem dela; a célula que só traz um fato (número, nome, comando, valor) fica fora da conta, porque fato não é expressão.
   - **A conferência automática:** em toda ficha de obra protegida roda antes da revisão o `parafrase.py` da skill `research` (`--ficha <ficha.md> --fonte <cópia de trabalho>`), que aponta as frases coladas e os trechos de três ou mais seguidas na ordem da fonte; na ficha em outra língua que a da fonte, o script sai com o código 3, que não é "passou", e a conta lado a lado é a conferência. Quando um agente escreve a ficha, o pedido manda mudar a organização do parágrafo, não só as palavras, porque o script não vê o espelhamento por sinônimos.
   - **Por quê:** seguindo a ordem de uma página curta, a ficha sai quase tradução; a medida que só contava frases soltas deixava passar fichas que fundiam várias frases seguidas; e contar célula de fato como cópia punia a ficha densa de fatos.
3. **Material pago** (curso, apostila, livro comprado, o que um curso pago distribuiu): não entra nesta base. Quando o conhecimento de um material pago precisar orientar o trabalho, quem o comprou escreve a regra com as próprias palavras, em `decisions/` ou na skill, sem copiar o material.

**Ficha que sustenta peça em produção não se reescreve antes da publicação** (2026-11-21): a ficha citada no roteiro, na escaleta, nos conceitos ou na legenda de uma peça com data de hoje em diante fica como está até a peça sair, mesmo acima do teto de três citações, porque reescrever muda a fonte contra a qual a peça está sendo conferida; a reescrita entra na passada seguinte. O `conta_citacoes.py` avisa quando a ficha listada sustenta uma peça futura (a pasta de `marketing/` com um arquivo da produção, como a `legenda.md`, o `roteiro.md` ou a `escaleta.md`, e a data no nome).

**A ficha de estudo** extrai o máximo de conhecimento da fonte em palavras próprias, não um resumo curto: cabeçalho (autor, url, data, duração), a estrutura da fala com as marcas de tempo, as regras ensinadas com a ressalva de quem fala, poucas citações curtas (até umas 25 palavras, só onde a frase carrega a regra) e a seção "Tudo o mais que ensina", com os outros temas em palavras próprias, para nenhuma ideia que valha aprender se perder. Quando um tema pedir mais, o link e a marca de tempo levam de volta ao trecho.

**Citação e cobertura:** a citação e o integral saem do arquivo da fonte, por `grep` ou por script, nunca do que uma saída filtrada mostrou, e a frase de cobertura da ficha lista as páginas de fato lidas. Por quê: o terminal corta a saída longa, e o fim cortado acaba completado de cabeça.

**Transcrição sem marca de falante** (a automática): a ficha diz no cabeçalho que a transcrição não marca quem fala e marca cada atribuição inferida ("pela sequência dos turnos"); a marca de tempo citada é a do parágrafo em que a resposta começa. Por quê: sem a marca, a atribuição inferida passa por fato.

**A cópia de trabalho:** a transcrição ou o texto integral que o assistente usa para fazer a ficha nasce no scratchpad da sessão e, ao fim da ingestão, se guarda no repositório, fora do git, numa pasta `originals/`: a de uma rodada de pesquisa, no `originals/` da rodada (`knowledge/research-rounds/<rodada>/originals/`), e a de material curado fora de uma rodada, em `knowledge/sources/originals/`, com o nome da ficha e a extensão do original. O de licença que permite cópia vai ao git (item 1); o protegido nunca vai a um bucket público. Por quê: sem a cópia guardada, a ficha não se confere depois contra a fonte, e a cópia do scratchpad se perde com a sessão.

**Quando a primária não abre** (PDF grande, página que bloqueia robô, cookie, captcha), tentar as rotas antes de rebaixar a fonte a "só citação": baixar com `curl -L` e um user agent de navegador; extrair o PDF com `pdftotext` e, se for escaneado ou tiver tabela em imagem, renderizar as páginas como imagem e ler (no PDF longo, o `extrai_pdf.py` da `research` tira o texto por página e renderiza só as páginas que pedem olho, com a saída no `originals/` e a ficha citando "PDF p. N": o método em [`.claude/skills/research/references/scripts.md`](../../.claude/skills/research/references/scripts.md), "A extração barata de PDF longo"); artigo científico pelo resumo oficial (API do PubMed ou OpenAlex) e o texto pela versão aberta (arXiv, PMC); página que saiu do ar, pela Wayback Machine, que não serve para contornar acesso fechado (a cópia de terceiro de artigo fechado não é rota, e a fonte que segue fechada fica como só citação); livro protegido pela amostra oficial da editora; e o navegador por último. Registrar no `log.md` a rota que funcionou.

**A conferência da ficha** (opcional, para fonte longa ou importante): o código confere o que é regra (o frontmatter completo e no formato, os links); um agente sem o contexto da conversa lê a cópia de trabalho e lista os tópicos que valem registro, e o assistente compara com a ficha e a síntese; um modelo de decisão tipado (o Jev, quando configurado) pode servir de sonda de cobertura, com uma pergunta de sim ou não por tag já em uso. Um assunto que a fonte trata e a ficha não registra volta a ficha ao passo da escrita. Quem usa cura, como em toda ingestão.
