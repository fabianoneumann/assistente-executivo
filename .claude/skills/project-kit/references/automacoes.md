# O que o kit oferece, pelo sinal do projeto

Uma lista de conferência: para cada sinal que um projeto pode ter, a automação do Claude Code que costuma servir, o que o kit já traz e o que fica para oferecer à pessoa na discussão inicial. **Ler quando:** na etapa 1, depois que a stack e o que o sistema faz estão claros, e ao pensar numa automação nova para o kit.

**De onde vem.** As tabelas "sinal no projeto, automação" da skill `claude-automation-recommender`, do plugin `claude-code-setup` da Anthropic (Apache 2.0; `anthropics/claude-plugins-official`, `plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`, commit `fc49e68` de 28/05/2026, lido em 20/11/2026), em palavras próprias. A skill de lá olha o projeto e recomenda uma ou duas automações por tipo, sem ligar nada; aqui as tabelas servem para conferir o que o kit dá, e nada se liga sem a pessoa pedir.

## As regras do kit que pesam aqui

- **As travas só recusam ou avisam,** e nunca perguntam (`knowledge/travas.md` do projeto): a recomendação de lá de "pedir confirmação" no código sensível não entra.
- **O `settings.json` do projeto não tem `allow`,** e o kit não instala servidor MCP nem plugin: o que a tabela recomenda e o kit não traz vai à proposta da etapa 1, para a pessoa decidir.
- **O formato não se reescreve no commit** (o `pre-commit` confere, sem mudar o arquivo): o "formatar a cada edição" de lá fica como oferta, e não como padrão.

## Os hooks

| Sinal no projeto | A automação | No kit |
|---|---|---|
| Formatador configurado | formatar depois de cada edição | não: o `pre-commit` confere o formato e o CI de novo; o hook de edição se oferece à equipe que quiser |
| Lint configurado | o lint depois de cada edição | não: o lint roda no CI |
| TypeScript | conferir os tipos depois de cada edição | não: o `typecheck` é o lint do CI na `node-ts` |
| Pasta de testes | rodar os testes ligados ao arquivo editado | não: o smoke e os testes rodam no CI |
| Arquivo `.env` | barrar o acesso do agente ao `.env` | sim: o `deny` de leitura do `.env` no `settings.json` |
| Arquivo travado de dependências | barrar a edição à mão do arquivo travado | não: a oferecer no primeiro projeto que sofrer com isso |
| Código sensível | pedir confirmação antes de editar | não, por regra: as travas não perguntam |

## Os servidores MCP

| Sinal no projeto | A automação | No kit |
|---|---|---|
| Bibliotecas conhecidas | a documentação atual da biblioteca (context7) | não: a oferecer quando a equipe consultar documentação com frequência |
| Interface com teste de tela | o navegador automatizado (Playwright) | não: a oferecer no projeto com tela, junto com a lente do passo 5 do `processo.md` |
| Repositório no GitHub | o servidor do GitHub | não: o kit e as travas usam o `gh` |
| Banco de dados | as consultas e o esquema do banco | não: a oferecer no "dado de fora" da discussão inicial, só de leitura |
| Contêineres | o servidor do Docker | não: o build roda no CI (`--docker`) |
| Rastreio de erro, chat da equipe, nuvem | o servidor de cada serviço | não: a oferecer quando o projeto tiver o serviço |

## As skills, os subagentes e os plugins

| Sinal no projeto | A automação | No kit |
|---|---|---|
| O fluxo de PR | uma lista de conferência do PR | sim: o modelo de PR e o hook que recusa o modelo vazio |
| As versões | as notas da versão a partir do git | sim: o `.github/release.yml` e o passo a passo do `versao-e-dependencias.md` |
| A chegada de quem entra | o preparo da máquina | sim: o `onboarding/` e o comando de instalar no `CLAUDE.md` |
| As convenções do projeto | uma skill com as convenções | sim: o `CLAUDE.md` roteador e a base |
| Base de código grande | um revisor de código em paralelo | sim: o `/code-review` no passo 5 |
| Autenticação ou pagamento | um revisor de segurança | não: a oferecer quando o projeto tiver |
| Interface pesada | um revisor de acessibilidade | em parte: a lente de tela do passo 5 do `processo.md`; o subagente se oferece |
| Testes a escrever | um gerador de testes | não |
| Interface | o plugin `frontend-design` | não: a oferecer no projeto com tela |
| Rotas de API | a documentação OpenAPI | não: a oferecer no projeto que publica API |
