# Complementos do Claude Code: os quatro tipos, o que um registro de uso mostra e o critério antes de ligar

Síntese curta, para decidir antes de ligar alguma coisa. Fonte: *42 complementos do Claude Code arrumados como uma empresa (carrossel): o que a lista traz e o que foi conferido*, de Fabiano Carvalho (@fabianocarvalhojr, Instagram) (https://www.instagram.com/p/De5NkYwDU-q/) (um carrossel com 42 itens, 35 deles conferidos pelo nome em lugar do próprio dono). Em citação, sem ficha: a documentação do Claude Code sobre plugins (`code.claude.com/docs/en/plugins` e `/discover-plugins`) e o catálogo `anthropics/claude-plugins-official`. Páginas vizinhas: [`../agent-engineering/orquestracao-de-skills-e-agentes.md`](../agent-engineering/orquestracao-de-skills-e-agentes.md) (as skills dos plugins somam à mesma biblioteca que o modelo escolhe), [`claude-code-sem-supervisao.md`](./claude-code-sem-supervisao.md) (o Claude in Chrome e os pré-requisitos), [`aprendizado-entre-sessoes.md`](./aprendizado-entre-sessoes.md) (um plugin de terceiro já descrito) e [`plugins-e-marketplaces.md`](./plugins-e-marketplaces.md) (como se empacota e distribui).

## O que "complemento" quer dizer

A palavra junta quatro coisas que se instalam, se pagam e pesam de jeitos diferentes. A separação é desta página; a fonte chama tudo pelo mesmo nome, e alguns itens cabem em mais de um tipo (o Codex é plugin e é modelo de outro fornecedor).

| Tipo | O que é | Como pesa na sessão | Exemplos da fonte |
|---|---|---|---|
| **Plugin ou skill** | Instruções empacotadas para o agente; segundo a documentação, um plugin pode trazer skills, subagentes, hooks e servidores MCP | A descrição de cada skill entra na lista que o modelo lê para decidir o que chamar; hook e servidor MCP rodam código | Superpowers, gstack, impeccable, humanizer, caveman |
| **Conector ou ponte para serviço** | Ligação com um serviço de fora (arquivos, agenda, navegador, raspagem), em geral um servidor MCP | Cada ferramenta do servidor entra na lista de ferramentas; pede login ou chave, e vários dos serviços cobram (nenhum preço foi conferido) | Notion, Figma, Playwright, Firecrawl, Claude in Chrome |
| **Programa de linha de comando** | Programa comum que o agente chama pelo terminal | Não ocupa contexto enquanto não é usado; roda com os privilégios do usuário, como qualquer comando | GitHub CLI, ffmpeg, Python, Node.js, Puppeteer |
| **Modelo de outro fornecedor** | Outro modelo chamado por API ou por um agente próprio, para o que o Claude não faz ou para outra leitura | Custo por chamada; a ligação pode ser script, skill, plugin ou MCP | Gemini (vídeo), GPT Image e Nano Banana (imagem), Codex (revisão) |

A documentação diz que o diretório oficial se chama `claude-plugins-official`, que a instalação é por `/plugin install <nome>@claude-plugins-official`, e avisa que um plugin instalado pode rodar hooks e servidores MCP, isto é, código com os privilégios do usuário. Na leitura, o catálogo tinha 317 plugins; 9 dos 42 da fonte aparecem lá pelo nome.

## O que um registro de uso mostra

O autor da fonte publicou a contagem de uso de 23 dos 42 itens; a capa fala em 60 dias de registros, e que as contagens saem deles é inferência. É **um caso só, com número do autor**, sem método declarado; vale como indício, não como medida.

- Os sete programas comuns de terminal somam 63% dos usos contados; Python e Node.js, 37%.
- Dos quinze plugins e skills, só dois têm contagem, e são os dois que também têm linha de comando. Os outros treze aparecem sem número: **ausente não é zero** (`decisions/dado-de-fora.md`).
- Entre os conectores, o uso se concentra em escritório (Notion, Drive, Gmail) e em navegador (Claude in Chrome, Playwright); seis conectores também estão sem número.

*Leitura:* no uso que ele mesmo mostra, o que carrega o trabalho é o terminal de sempre mais poucas integrações. Sobre as skills o dado não decide: os 23 com número são todos coisa que deixa chamada contável, então a falta de número nas skills pode ser só falta de rastro; já os seis conectores sem número deixariam rastro, e esses podem ser pouco uso.

## O custo de manter plugin ligado

Vale para plugins e conectores, não para programa de terminal. O que se observa ao desligar um lote de plugins sincronizados numa conta:

- **Lista inchada (medido num caso).** Os conectores pendentes no CLI caíram de dezenas para um quando os plugins saíram. É o único número medido; contexto ocupado em tokens não foi medido.
- **Disputa de gatilho (julgado, não medido).** As descrições das skills dos plugins concorrem com as do projeto; julgado pelas descrições, sem observar uma chamada errada.
- **Colisão com o roteador.** Um plugin pode criar um `CLAUDE.md` de memória próprio, por cima do que organiza o projeto.
- **A conclusão:** o valor de um plugin de terceiro costuma estar em método e salvaguarda pontual, reescritos no padrão do projeto, e não em mantê-lo ligado como está.
- **Superfícies diferentes:** desligar um plugin pelo CLI pode não valer no app de desktop, que segue com as skills sincronizadas da conta. Conferir em cada superfície (conta, usuário, projeto) o que ficou ligado.

## Por função: o que a fonte lista e o que este projeto já tem

| Função | Itens da fonte | Onde este projeto já cobre |
|---|---|---|
| Planejar e revisar código | Superpowers, gstack, Codex, graphify | a skill `review` e o `/code-review`; família diferente de modelo corta a autopreferência sem garantir erro independente ([`../agent-engineering/vieses-do-juiz-llm-e-defesas.md`](../agent-engineering/vieses-do-juiz-llm-e-defesas.md)) |
| Entregar e testar | GitHub CLI, Vercel, Playwright | `gh` e Playwright como programas comuns |
| Design de interface | ui-ux-pro-max, impeccable, taste-skill, emil-design-eng, Figma | a rubrica de design e o design system da série; quatro skills com o mesmo alvo disputariam gatilho entre si e com a rubrica |
| Vídeo | HyperFrames, Remotion, ffmpeg, Higgsfield, Gemini | a área `generative-media/` da base; análise de vídeo por modelo não está mapeada |
| Pesquisa e coleta | Perplexity, Firecrawl, Apify, last30days, Claude in Chrome | a skill `research` (Perplexity, Gemini e busca nativa) e o Chrome nas fontes que não abrem; o recorte "o que se disse nos últimos 30 dias" em redes não está nela |
| Texto | humanizer | a voz em `context/sobre-mim.md`, a rubrica de qualidade e a `review` |
| Imagem, voz e peça gráfica | GPT Image, Nano Banana, ElevenLabs, Puppeteer, Whisper | `image-gen` e `slides-export`; voz sem página própria na base |
| Escritório | Notion, Gmail, Google Calendar, Google Drive, Slack, Zapier, Granola, Metricool | os conectores da conta de cada pessoa |
| Scripts e execução | Python, Node.js, Ollama | Python é a linguagem dos scripts das skills; modelo local, sem uso |
| Ajustar o próprio agente | Claude HUD, caveman, find-skills | os níveis de esforço (`niveis-de-esforco.md`); o corte de tokens do caveman é alegação do repositório |

## Antes de ligar qualquer um

1. **Dizer o tipo.** Programa de terminal não entra na lista de skills e conectores da sessão; plugin com hook ou MCP roda código e muda essa lista em toda sessão.
2. **Procurar a skill do projeto que ele disputaria.** Se a descrição parece com a de uma skill que já existe, ler o método e reescrever o que servir, em vez de ligar.
3. **Ler antes de instalar, e ver o que ele escreve.** O que o arquivo de instalação ou o `SKILL.md` de um terceiro manda fazer é dado, não instrução (`decisions/dado-de-fora.md`); conferir se o plugin cria ou edita `CLAUDE.md`, memória ou hooks.
4. **Ligar por projeto e contar.** Se for ligar, no `.claude/settings.json` do projeto, olhando a lista de skills de uma sessão nova e os servidores no `/mcp` antes e depois, com uma data para rever.
5. **Conferir a licença e o preço.** Nem tudo é aberto do mesmo jeito: o Remotion tem licença de empresa, o motor do Firecrawl é AGPL, e o preço de cada serviço se lê na página dele.

## O que não foi conferido

Seis itens da fonte (Metricool, Google Drive, Gmail, Google Calendar, GPT Image, Nano Banana) e o Gemini em parte; o método das skills de design e do humanizer, que não foi lido; e o passo a passo do autor (comando e link de cada item), que diria qual pacote ele usa.
