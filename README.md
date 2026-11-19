# Assistente executivo

Um modelo de ambiente para trabalhar com o Claude como assistente executivo e pessoal, pronto para usar: um `CLAUDE.md` que diz ao Claude como trabalhar aqui, uma base de conhecimento de método (`knowledge/`), as decisões com o porquê (`decisions/`), treze skills (da captura de uma ideia à peça exportada para o Instagram, mais o kit que faz nascer um projeto de software novo já com o processo) e as pastas da vida pessoal (`finance/`, `health/` e `maps/`), com o método e sem nenhum dado.

É para quem quer um assistente que acumula contexto em arquivos, em vez de redescobrir tudo a cada conversa (o padrão LLM Wiki), e não quer montar tudo do zero. Funciona para uma pessoa só, no trabalho e na vida pessoal.

> **O curso.** O curso *Engenharia de Agentes de IA* ensina a construir o seu próprio ambiente do zero, por prompts, e usa este repositório como gabarito: você monta o seu, compara com este e entende o porquê de cada regra. Quem só quer o ambiente pronto pode usar este modelo direto.

## Comece por aqui: crie o seu repositório, privado

1. No GitHub, clique em **Use this template** > **Create a new repository**.
2. Em **visibility**, escolha **Private**. É o seu repositório que vai guardar a sua voz, as suas ideias e, se você usar a parte pessoal, as suas finanças, a sua saúde e os seus mapas. **Escolha Private antes de pôr qualquer dado pessoal.** Se você já criou como público, mude em Settings > General > Danger Zone > Change repository visibility antes de escrever o primeiro registro: o histórico do git guarda o que foi commitado, mesmo depois de apagado.
3. Siga um dos dois caminhos abaixo: o de quem programa (o Claude Code) ou o de quem não programa (o Cowork, no app do Claude).

Depois, o `scripts/confere_dados.py` ajuda a manter assim: rodado antes do push, com o `gh` instalado e logado, ele para quando há registro pessoal e o remoto do GitHub é público, e diz como deixar o repositório privado. Ele não roda sozinho (não há hook) e nada confere antes do primeiro registro. Sem o `gh`, ou sem o login dele, sai com o código 3 ("não conferiu") e diz o que falta: a visibilidade no momento da criação é com você.

**Trabalho e vida pessoal no mesmo repositório, ou em dois?** O modelo é um só, com as duas partes. Se você vai dividir o repositório com outras pessoas (um sócio, uma equipe), crie dois a partir deste modelo: um de trabalho, compartilhado, e um pessoal, só seu. A visibilidade e os colaboradores valem para o repositório inteiro.

## Antes de ligar: revise as skills

Uma skill é instrução que o Claude segue com as suas permissões, nos seus repositórios e com as suas chaves. O Jev, citado em algumas, é o modelo de decisão da TypeSafe (opcional, pago, com a `TYPESAFE_API_KEY`); sem ele, as skills rodam igual. Leia o `SKILL.md` de cada uma antes de usá-la, e reescreva o que não serve a você; os termos do método que elas usam (mesa, portão, trava do texto, escaleta, I2) estão explicados no [`glossario.md`](./glossario.md). O que é do seu ambiente (caminhos, réguas, comandos, a regra de custo das APIs) está no `references/projeto.md` de cada skill; o método, no `SKILL.md`; e as lições que viraram regra, no `licoes.md`.

| Skill | O que faz | O que lê | O que pode rodar | Chave |
|---|---|---|---|---|
| `idea-capture` | registra uma ideia crua em `marketing/social-media/ideas/`, sem perguntar, pesquisar nem propor ângulo | os arquivos de `ideas/` | nada | nenhuma |
| `review` | revisão independente por lentes: um agente acha os problemas, outro confere cada achado, sai a lista dos confirmados, sem alterar o trabalho | o trabalho e as fontes dele, as réguas, a issue ou o PR | `gh` (ler issues e PRs); o Codex e o Jev, opcionais | nenhuma (o `gh` com o seu login); opcional: `TYPESAFE_API_KEY` |
| `story-angle` | apura um tema por movimentos jornalísticos até uma mesa de ângulos; a escolhida vira pauta no arquivo da ideia | `context/publico.md`, `knowledge/`, `ideas/` | as buscas vão pela `research` | nenhuma própria |
| `research` | pesquisa com fontes (Perplexity, Gemini, busca nativa e, opcional, o Codex), reconcilia e registra fichas e sínteses em `knowledge/` | `knowledge/`, `decisions/`, `context/` | as APIs da Perplexity e do Gemini pela rede; scripts locais de conferência | `PERPLEXITY_API_KEY`, `GEMINI_API_KEY`; opcional: `TYPESAFE_API_KEY` |
| `image-gen` | gera imagem pelo Nano Banana (Gemini) e, opcional, pelo GPT Image do Codex, com o banco consultado antes e o custo registrado | o banco de imagens, o design system da série | a API do Gemini; o Codex CLI, opcional; a conferência pelo Jev, opcional | `GEMINI_API_KEY`; opcional: `TYPESAFE_API_KEY` |
| `r2-storage` | sobe, baixa, lista e remove arquivos num bucket R2 da Cloudflare e dá a URL pública ou assinada | as variáveis `R2_*` | a API S3 do R2 pela rede | `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET_CONTEUDO` (a URL pública, `R2_PUBLIC_BASE_CONTEUDO`, opcional aqui e obrigatória no `--upload`) |
| `piece-creation` | leva uma peça (carrossel, Stories) da ideia ou da pauta até a exportação, chamando as outras na ordem, com as paradas para você decidir | as ideias, a série, as rubricas, o portão, `context/publico.md` | nada próprio; cada skill chamada confere a sua chave | nenhuma própria (a partir da ideia crua, as da `research`) |
| `piece-script` | escreve o roteiro da peça por formato até a trava do texto | a pauta, as fichas, as sínteses de conteúdo, as rubricas | nada | nenhuma |
| `base-enrichment` | num subagente isolado, passa pela base sobre uma camada da peça e devolve até cinco sugestões de método | `knowledge/`, as peças irmãs, `marketing/licoes.md` | só grava o relatório dela | nenhuma |
| `visual-form` | monta o HTML das telas no design system da série, com as conferências em código, até a prévia | o texto travado, a escaleta, o design system da série | Playwright (Chromium) e FFmpeg, locais | nenhuma |
| `object-anatomy` | num subagente, faz o objeto que se move em SVG por código, com as conferências por script | as fichas que quem chama entrega, a série | Playwright e FFmpeg, locais | nenhuma |
| `project-kit` | cria um projeto de software novo já estruturado: a discussão inicial, a arquitetura, o plano e os ADRs na base `knowledge/` do projeto, o repositório montado dos modelos (o processo de issues e de PR, o CI, o Dependabot de segurança, as travas, o onboarding) e conferido, e o GitHub com a primeira milestone e as specs, na sua conta pessoal | a conversa, os modelos da skill, `knowledge/software-engineering/` | `git`, Python (com o PyYAML e o Playwright do `requirements.txt` dela, para a conferência e os diagramas) e o `gh` (criar o repositório, a milestone e as specs) | nenhuma (o `gh` com o seu login) |
| `slides-export` | exporta as telas em JPEG e a tela em vídeo em MP4, confere e, com `--upload`, sobe ao bucket e registra os links | as telas, a `legenda.md`, `context/sobre-mim.md` | shot-scraper, Playwright e FFmpeg; com `--upload`, o R2 | só para `--upload`: as do `r2-storage` |

**O ciclo de melhoria da `review` só liga com a issue de reavaliação aberta:** sem ela, a revisão roda mas não deixa registro, e você não mede se a skill está ajudando. Quando quiser medir, abra a issue e ponha o número no `references/projeto.md` da skill. A issue junta, a cada revisão, um comentário de uma linha com os números daquele uso (o que se revisou, as lentes, os achados confirmados e derrubados, o que se aplicou, o que a revisão deixou passar e os tokens) e, a partir do 15º registro ou na data de vencimento dela, a proposta de reavaliar a skill com esses números (`.claude/skills/review/references/registro.md`). O que você ensina ao assistente sobre como trabalhar fica na memória dele, com cópia opcional no git (`decisions/memoria-e-evolucao.md`).

**Sem chave nenhuma, funcionam desde o clone:** `idea-capture`, `review`, `piece-script` e `base-enrichment`, e a `project-kit` com o `gh` logado; `visual-form`, `object-anatomy` e a exportação local da `slides-export` pedem só os programas locais. **Sem chave própria, mas dependem de outra:** a `story-angle` apura pela `research` (sem as chaves dela, a apuração para) e a `piece-creation` chama a `research`, a `image-gen` e a `slides-export`, cada uma com a sua. Por isso o carrossel feito a partir de uma ideia crua, que passa pela apuração e pela pesquisa antes do roteiro, pede as chaves da `research` (`PERPLEXITY_API_KEY` e `GEMINI_API_KEY`). **As com chave não rodam antes de você configurar a sua:** o primeiro passo de cada uma confere, e sem a chave ela para e diz qual variável falta, onde se pega e como se põe. As APIs são cobradas à parte do plano do Claude: antes de usar, preencha a regra de custo das suas contas no `references/projeto.md` da `research` e da `image-gen`.

**A vida pessoal não pede skill nem chave:** é o `CLAUDE.md` que diz ao assistente onde lançar uma despesa, um treino, um exame ou um mapa, e os READMEs de `finance/`, `health/` e `maps/` trazem o método e o roteiro do que contar a ele para começar.

Não vêm nesta versão: a publicação no Instagram e as métricas (dependem de uma conta da Meta e de rotinas agendadas). A sua série de posts nasce da série de exemplo em branco (`marketing/social-media/carousels/series/exemplo/`).

## Caminho 1: quem programa (Claude Code)

1. **O que instalar:** o [Claude Code](https://code.claude.com/docs) (ou o app do Claude, aba Code), o Git e o Python 3.11 ou mais novo. Para as skills de forma e exportação, também o FFmpeg e o Chromium do Playwright (abaixo). O `gh` (GitHub CLI) serve à `review`, à `project-kit` e à conferência de privacidade do `confere_dados.py`.
2. **Clonar o seu repositório e abrir:**
   ```
   git clone <endereço do seu repositório> assistente-executivo
   cd assistente-executivo
   claude
   ```
   Na primeira vez, o Claude Code pergunta se você confia na pasta: aceite, depois de ter lido as skills. O `CLAUDE.md` e as skills de `.claude/skills/` carregam sozinhos.
3. **Ver o que falta:** `python -X utf8 scripts/confere_ambiente.py`. Ele mostra, skill por skill, o que já funciona e o que falta, sem nunca mostrar o valor de uma chave.
4. **Pôr as suas chaves** (só as das skills que você vai usar):
   ```
   cp .env.example .env
   ```
   Abra o `.env` no seu editor e preencha as linhas. Cada linha do `.env.example` diz para que serve a chave e onde se pega. O `.env` nunca vai ao git (`.gitignore`). O `.claude/settings.json` nega à ferramenta de leitura do Claude o `.env`, o `.env.local` e o `.claude/settings.local.json`, mas um comando de terminal não é barrado por isso: não peça ao Claude para abrir, mostrar ou procurar dentro desses arquivos, e não cole chave na conversa, nem em nenhum arquivo versionado. Quem lê as chaves são os scripts das skills. (As mesmas variáveis também funcionam no bloco `"env"` do `.claude/settings.local.json`, que fica fora do git; o `.env` é o recomendado.) Depois, reinicie a sessão e rode o passo 3 de novo.
5. **Instalar os pacotes Python** das skills que você vai usar (o `confere_ambiente.py` diz quais faltam):
   ```
   python -m pip install -r .claude/skills/research/requirements.txt
   python -m pip install -r .claude/skills/image-gen/requirements.txt
   python -m pip install -r .claude/skills/r2-storage/requirements.txt
   python -m pip install -r .claude/skills/visual-form/requirements.txt
   python -m pip install -r .claude/skills/project-kit/requirements.txt
   python -m playwright install chromium
   shot-scraper install
   ```
   O FFmpeg (vídeo das telas e quadros) se instala à parte: no Windows, `winget install Gyan.FFmpeg`; no macOS, `brew install ffmpeg`; ou pelo site [ffmpeg.org](https://ffmpeg.org/download.html).
6. **Preencher o contexto:** `context/sobre-mim.md` (quem você é e a sua voz ao escrever conteúdo) e `context/publico.md` (para quem você fala) vêm em branco, com o roteiro. Sem eles, o assistente pergunta em vez de inventar.
7. **Primeiro uso:** peça em linguagem natural, como "registra uma ideia: …", "pesquisa o que existe sobre …", "lança uma despesa de …" ou "vamos fazer a minha Roda da Vida". O Claude escolhe a skill pela descrição dela, e o lugar de cada registro pelo `CLAUDE.md`.

**Antes de commitar** material que veio de fora, e sempre antes do push: `python -X utf8 scripts/confere_dados.py` procura chave, e-mail, telefone, caminho de usuário, id de conta e conteúdo de terceiro fora da régua no que iria num commit (o que o `.gitignore` tira, como o `.env` e as pastas `originals/`, fica fora), confere a privacidade do repositório e, rodado sem pastas, o autor de cada commit do histórico: o seu e-mail real sai como achado; no repositório privado, você pode deixá-lo, ou usar o e-mail `noreply` do GitHub (Settings > Emails). Com `--termos <arquivo fora do repositório>`, procura também os nomes e ids que você quer barrar (de clientes, de familiares), sem que a lista entre no git.

### Para conferir que está tudo certo

Da raiz do repositório, no começo e depois de instalar os pacotes. Nenhum destes comandos pede rede nem chave, e nenhum mostra o valor de uma chave.

| Comando | O que confere | O esperado |
|---|---|---|
| `python -X utf8 scripts/confere_ambiente.py` | skill por skill, o que já roda e o que falta | código 0, com o quadro: "pronta" nas skills que você configurou e "falta configurar" nas outras, com o que falta; no alto, de onde vieram as chaves (o `.env` ou a variável do sistema) |
| `python -X utf8 scripts/confere_links.py` | os links entre os arquivos e as duas cópias dos agentes | `-- 0 link(s) quebrado(s)` |
| `python -X utf8 scripts/confere_dados.py` | chave, dado pessoal e conteúdo de terceiro no que iria num commit | `-- 0 achado(s)` e código 0; o seu e-mail real nos commits sai como achado (ver "Antes de commitar", acima) |
| `python -X utf8 scripts/teste_confere_dados.py` | os casos do `confere_dados.py` | `TODOS OK` |
| `python -X utf8 scripts/teste_medir_disparo.py` | os casos do `medir_disparo.py` | `TODOS OK` |
| `python -X utf8 .claude/skills/research/scripts/teste_conferidores.py` | as conferências das rodadas de pesquisa, sem chamar as APIs | `0 falha(s)`, com as lacunas conhecidas listadas, que não derrubam o teste |
| `python -X utf8 .claude/skills/review/scripts/teste_registro.py` | a contagem do registro da `review`, sem o `gh` | `0 falha(s)` |
| `python -X utf8 -m unittest discover -s .claude/skills/project-kit/scripts -p "teste_*.py"` | a montagem e a conferência de um projeto novo, nas três stacks (pede o `requirements.txt` da `project-kit`) | `Ran 8 tests` e `OK` (as linhas "Montado em ...", que podem vir antes ou depois, são da montagem) |
| `python -X utf8 .claude/skills/project-kit/scripts/teste_diagrama_conferir.py`, e o mesmo com `teste_diagrama_regressao.py` no lugar | os diagramas do onboarding (pedem o Playwright com o Chromium) | `tudo certo` em cada um |

Se um deles falhar, a saída diz o que falta ou o que quebrou; o mais comum, no começo, é um pacote não instalado (o `confere_ambiente.py` diz qual e o `requirements.txt` de onde ele vem).

### O Codex, opcional

Quem usa também o Codex CLI (da OpenAI) acha as instruções do projeto pelo [`AGENTS.md`](./AGENTS.md), que só manda ler o `CLAUDE.md`, a fonte única. Na `review`, o Codex entra como **segunda revisão de código**, ao lado do `/code-review` do Claude Code e sem substituí-lo:
1. instale o [Codex CLI](https://developers.openai.com/codex/cli) e entre com `codex login`;
2. crie uma vez o perfil só leitura em `~/.codex/revisao.config.toml`, com `sandbox_mode = "read-only"`, `approval_policy = "never"` e, numa seção `[features]`, `apps = false`;
3. a `review` monta uma pasta isolada, na pasta temporária, só com os arquivos revisados, e roda `codex exec --skip-git-repo-check --ephemeral -p revisao -C <pasta isolada> -o <achados.md> - < <pedido>`.

Os achados do Codex entram na mesma conferência que os do `/code-review`. Sem o Codex, a revisão segue e diz que ele não rodou. O detalhe está em `.claude/skills/review/references/codigo.md`.

### As skills noutro projeto (o plugin)

O repositório é também um marketplace com o plugin `assistente-executivo`, que leva as treze skills e os dois agentes. Os agentes ficam em dois lugares: `.claude/agents/`, que o Claude Code lê no clone, e `agents/`, na raiz, que o plugin leva, porque declarados a partir da `.claude/` eles não carregam. As duas cópias são iguais, e o `scripts/confere_links.py` acusa quando divergem: quem muda um agente muda os dois. Noutro projeto:
```
claude plugin marketplace add <caminho do clone, ou dono/repositório no GitHub>
claude plugin install assistente-executivo@assistente-executivo
```
No plugin, as skills ganham o prefixo (`/assistente-executivo:research`). Elas esperam a estrutura deste repositório (`knowledge/`, `marketing/`, `context/`, `scripts/confere_ambiente.py`); num projeto sem ela, o método vale, os caminhos não, e a conferência de chave fica a cargo do próprio código de cada skill, que para com a mesma mensagem. Não instale o plugin dentro deste repositório: as skills já carregam de `.claude/skills/`, e ficariam em dobro.

## Caminho 2: quem não programa (Cowork, no app do Claude)

O Cowork faz no app do Claude, sem terminal, o mesmo tipo de trabalho do Claude Code. As skills que ele carrega com certeza são as da **sua conta**; o que ele faz com as skills e o `CLAUDE.md` de uma pasta escolhida ainda está por testar (abaixo). Por isso, nesta versão, as skills se instalam uma vez na sua conta.

1. **O que precisa:** uma conta paga do Claude (Pro, Max ou acima) e o app do Claude no computador (Windows ou macOS), em [claude.ai/download](https://claude.ai/download).
2. **Ligar a execução de código:** em Settings > Capabilities, ligue "Code execution and file creation". Sem isso, as skills não carregam.
3. **Baixar o seu repositório:** no GitHub, no repositório que você criou (privado), clique em **Code** > **Download ZIP** e descompacte numa pasta do seu computador. (Quem tiver o GitHub Desktop pode clonar por ele, e aí o que você gravar volta ao GitHub.)
4. **Instalar as skills na sua conta.** Cada skill precisa virar um ZIP para o app. Peça ao Cowork, com a pasta escolhida: "empacota as skills idea-capture e review com o `scripts/empacota_skills.py`" (ou, num terminal com Python, `python -X utf8 scripts/empacota_skills.py idea-capture review`). Os ZIPs saem em `dist/`. No app, vá em Customize > Skills, envie o ZIP e ligue a skill. O empacotador já tira o que a conta não aceita e avisa o que muda.
5. **Conectar o Gmail e a Agenda:** em Customize > Connectors, conecte o Gmail e o Google Calendar com a sua própria conta do Google.
6. **A pasta de trabalho:** no Cowork, escolha a pasta do passo 3. É nela que as skills procuram as ideias (`marketing/social-media/ideas/`), o público e a base, e onde ficam as suas finanças, a sua saúde e os seus mapas. Comece pelo `context/sobre-mim.md` e pelo `context/publico.md`: peça ao Cowork para fazer as perguntas do roteiro e preencher com você.
7. **Usar:** peça em linguagem natural ("registra esta ideia", "revisa este texto", "o que tenho na agenda amanhã?", "lança o que gastei hoje"). O Cowork pede a sua aprovação antes de apagar arquivo e, conforme o modo escolhido, antes de outras ações.

**Para quem não programa, a primeira versão recomenda as duas skills que não dependem de chave nenhuma:** `idea-capture` e `review`, e a parte pessoal, que não pede skill. A `story-angle` apura pela `research`, e as skills com chave dependem de como o Cowork trata as chaves e os scripts, que ainda está por testar.

**Ainda por testar, antes de contar com isso:**
- se o Gmail envia e responde, e se a Agenda cria evento, ou se só leem;
- o que o Cowork faz com a pasta `.claude/` e com o `CLAUDE.md` de uma pasta escolhida;
- se as skills com chave rodam no Cowork, e de onde ele leria a chave.

## A vida pessoal

As pastas `finance/`, `health/` e `maps/` vêm com o README do método e o roteiro do que preencher, e nenhum registro: o arquivo de cada coisa (o mês das finanças, o plano de treino, o exame, o retrato de um mapa) nasce quando você contar a primeira informação dele. Os mapas sugeridos, cada um com um guia curto em `maps/guides/`: Vision Board, Roda da Vida, Big Five (pelo IPIP-NEO-120, de domínio público), SWOT, Ikigai, Matriz EREC e OKR. O quadro `maps/board/` abre no seu navegador, com os modelos em branco, e não se publica em link.

O assistente não diagnostica, não estima personalidade pela conversa e sugere o profissional quando o assunto pede. O porquê está em [`decisions/vida-pessoal-e-mapas.md`](./decisions/vida-pessoal-e-mapas.md).

## A base de conhecimento

A `knowledge/` traz 89 sínteses de método, por área (avaliação e revisão por agentes, design de conteúdo, mídia gerada, apuração, dados, psicologia, o Claude Code, vendas, engenharia de software), e 463 fichas de fonte. Num repositório público, nenhuma ficha traz o texto integral da fonte: as de licença livre e as de fonte protegida vêm em palavras próprias, com citações curtas, e o integral se lê na fonte, pelo link. As três fichas livres que ainda têm trecho colado à fonte vêm só como citação simples (o título, o autor, o link e a licença). A régua está em [`knowledge/sources/README.md`](./knowledge/sources/README.md).

## A licença

O código é MIT ([`LICENSE`](./LICENSE)); o texto é CC BY 4.0 ([`LICENSE-texto`](./LICENSE-texto)). O material de terceiro segue a licença dele, e as 17 fichas de fontes em CC BY-SA são exceção declarada, na licença da fonte (a lista está no `LICENSE-texto`).

## Como o repositório se organiza

O mapa do que ler, e quando, está no [`index.md`](./index.md); as regras de manutenção, no [`CLAUDE.md`](./CLAUDE.md); os termos do método, no [`glossario.md`](./glossario.md). Em resumo: `context/` (quem você é e para quem fala), `decisions/` (o porquê das regras), `knowledge/` (a base de método, com as fontes e a régua de conteúdo de terceiro), `marketing/` (ideias, séries, rubricas), `finance/`, `health/` e `maps/` (a vida pessoal), `.claude/skills/` (as skills) e `scripts/` (os conferidores e o empacotador).
