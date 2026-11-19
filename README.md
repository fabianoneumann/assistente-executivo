# Assistente executivo

Um modelo de ambiente para trabalhar com o Claude como assistente executivo e pessoal, pronto para usar: um `CLAUDE.md` que diz ao Claude como trabalhar aqui, uma base de conhecimento de método (`knowledge/`), as decisões com o porquê (`decisions/`), treze skills (da captura de uma ideia à peça exportada para o Instagram, mais o kit que faz nascer um projeto de software novo já com o processo) e as pastas da vida pessoal (`finance/`, `health/` e `maps/`), com o método e sem nenhum dado.

É para quem quer um assistente que acumula contexto em arquivos, em vez de redescobrir tudo a cada conversa (o padrão LLM Wiki), e não quer montar tudo do zero. Funciona para uma pessoa só, no trabalho e na vida pessoal.

> **O curso.** O curso *Engenharia de Agentes de IA* ensina a construir o seu próprio ambiente do zero, por prompts, e usa este repositório como gabarito: você monta o seu, compara com este e entende o porquê de cada regra. Quem só quer o ambiente pronto pode usar este modelo direto.

## Comece por aqui: crie o seu repositório, privado

1. No GitHub, clique em **Use this template** > **Create a new repository**.
2. Em **visibility**, escolha **Private**. É o seu repositório que vai guardar a sua voz, as suas ideias e, se você usar a parte pessoal, as suas finanças, a sua saúde e os seus mapas. **Escolha Private antes de pôr qualquer dado pessoal.** Se você já criou como público, mude em Settings > General > Danger Zone > Change repository visibility antes de escrever o primeiro registro: o histórico do git guarda o que foi commitado, mesmo depois de apagado.
3. Siga um dos dois caminhos abaixo: o de quem programa (o Claude Code no terminal) ou o de quem não programa (a aba Code do app do Claude, sem terminal).

Depois, o `scripts/confere_dados.py` ajuda a manter assim: rodado antes do push, com o `gh` instalado e logado, ele para quando há registro pessoal e o remoto do GitHub é público, e diz como deixar o repositório privado. Ele não roda sozinho (não há hook) e nada confere antes do primeiro registro. Sem o `gh`, ou sem o login dele, sai com o código 3 ("não conferiu") e diz o que falta: a visibilidade no momento da criação é com você.

**Trabalho e vida pessoal no mesmo repositório, ou em dois?** O modelo é um só, com as duas partes. Se você vai dividir o repositório com outras pessoas (um sócio, uma equipe), crie dois a partir deste modelo: um de trabalho, compartilhado, e um pessoal, só seu. A visibilidade e os colaboradores valem para o repositório inteiro.

## Antes de ligar: revise as skills

Uma skill é instrução que o Claude segue com as suas permissões, nos seus repositórios e com as suas chaves. O Jev, citado em algumas, é o modelo de decisão da TypeSafe (opcional, pago, com a `TYPESAFE_API_KEY`); sem ele, as skills rodam igual. Leia o `SKILL.md` de cada uma antes de usá-la, e reescreva o que não serve a você; os termos do método que elas usam (mesa, portão, trava do texto, escaleta, I2) estão explicados no [`glossario.md`](./glossario.md). O que é do seu ambiente (caminhos, réguas, comandos, a regra de custo das APIs) está no `references/projeto.md` de cada skill; o método, no `SKILL.md`; e as lições que viraram regra, no `licoes.md`.

| Skill | O que faz | O que lê | O que pode rodar | Chave |
|---|---|---|---|---|
| `idea-capture` | registra uma ideia crua em `marketing/social-media/ideas/`, sem perguntar, pesquisar nem propor ângulo | os arquivos de `ideas/` | nada | nenhuma |
| `review` | revisão independente por lentes: um agente acha os problemas, outro confere cada achado, sai a lista dos confirmados, sem alterar o trabalho | o trabalho e as fontes dele, as réguas, a issue ou o PR | `gh` (ler issues e PRs); o Codex e o Jev, opcionais | nenhuma (o `gh` com o seu login); opcional: `TYPESAFE_API_KEY` |
| `story-angle` | apura um tema por movimentos jornalísticos até uma mesa de ângulos; a escolhida vira pauta no arquivo da ideia | `context/publico.md`, `knowledge/`, `ideas/` | as buscas vão pela `research` | nenhuma própria |
| `research` | pesquisa com fontes (Perplexity, Gemini, busca nativa e, opcional, o Codex), reconcilia e registra fichas e sínteses em `knowledge/` | `knowledge/`, `decisions/`, `context/` | a busca web da sessão; com as chaves, as APIs da Perplexity e do Gemini pela rede; scripts locais de conferência | nenhuma no modo só busca nativa; `PERPLEXITY_API_KEY` e `GEMINI_API_KEY` acrescentam índices e o profundo; opcional: `TYPESAFE_API_KEY` |
| `image-gen` | gera imagem pelo Nano Banana (Gemini) e, opcional, pelo GPT Image do Codex, com o banco consultado antes e o custo registrado | o banco de imagens, o design system da série | a API do Gemini; o Codex CLI, opcional; a conferência pelo Jev, opcional | `GEMINI_API_KEY`; opcional: `TYPESAFE_API_KEY` |
| `r2-storage` | sobe, baixa, lista e remove arquivos num bucket R2 da Cloudflare e dá a URL pública ou assinada | as variáveis `R2_*` | a API S3 do R2 pela rede | `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET_CONTEUDO` (a URL pública, `R2_PUBLIC_BASE_CONTEUDO`, opcional aqui e obrigatória no `--upload`) |
| `piece-creation` | leva uma peça (carrossel, Stories) da ideia ou da pauta até a exportação, chamando as outras na ordem, com as paradas para você decidir | as ideias, a série, as rubricas, o portão, `context/publico.md` | nada próprio; cada skill chamada confere a sua chave | nenhuma própria (a partir da ideia crua, a pesquisa roda no modo só busca nativa; as chaves da `research` acrescentam índices) |
| `piece-script` | escreve o roteiro da peça por formato até a trava do texto | a pauta, as fichas, as sínteses de conteúdo, as rubricas | nada | nenhuma |
| `base-enrichment` | num subagente isolado, passa pela base sobre uma camada da peça e devolve até cinco sugestões de método | `knowledge/`, as peças irmãs, `marketing/licoes.md` | só grava o relatório dela | nenhuma |
| `visual-form` | monta o HTML das telas no design system da série, com as conferências em código, até a prévia | o texto travado, a escaleta, o design system da série | Playwright (Chromium) e FFmpeg, locais | nenhuma |
| `object-anatomy` | num subagente, faz o objeto que se move em SVG por código, com as conferências por script | as fichas que quem chama entrega, a série | Playwright e FFmpeg, locais | nenhuma |
| `project-kit` | cria um projeto de software novo já estruturado: a discussão inicial, a arquitetura, o plano e os ADRs na base `knowledge/` do projeto, o repositório montado dos modelos (o processo de issues e de PR, o CI, o Dependabot de segurança, as travas, o onboarding) e conferido, e o GitHub com a primeira milestone e as specs, na sua conta pessoal | a conversa, os modelos da skill, `knowledge/software-engineering/` | `git`, Python (com o PyYAML e o Playwright do `requirements.txt` dela, para a conferência e os diagramas) e o `gh` (criar o repositório, a milestone e as specs) | nenhuma (o `gh` com o seu login) |
| `slides-export` | exporta as telas em JPEG e a tela em vídeo em MP4, confere e, com `--upload`, sobe ao bucket e registra os links | as telas, a `legenda.md`, `context/sobre-mim.md` | shot-scraper, Playwright e FFmpeg; com `--upload`, o R2 | só para `--upload`: as do `r2-storage` |

**O ciclo de melhoria da `review` só liga com a issue de reavaliação aberta:** sem ela, a revisão roda mas não deixa registro, e você não mede se a skill está ajudando. Quando quiser medir, abra a issue e ponha o número no `references/projeto.md` da skill. A issue junta, a cada revisão, um comentário de uma linha com os números daquele uso (o que se revisou, as lentes, os achados confirmados e derrubados, o que se aplicou, o que a revisão deixou passar e os tokens) e, a partir do 15º registro ou na data de vencimento dela, a proposta de reavaliar a skill com esses números (`.claude/skills/review/references/registro.md`). O que você ensina ao assistente sobre como trabalhar fica na memória dele, com cópia opcional no git (`decisions/memoria-e-evolucao.md`).

**Sem chave nenhuma, funcionam desde o clone:** `idea-capture`, `review`, `piece-script`, `base-enrichment` e a `research` no modo só busca nativa, e a `project-kit` com o `gh` logado; `visual-form`, `object-anatomy` e a exportação local da `slides-export` pedem só os programas locais. **A pesquisa sem chave:** sem a `PERPLEXITY_API_KEY` e a `GEMINI_API_KEY`, a `research` roda no **modo só busca nativa**: busca pela busca web da sessão do Claude Code, verifica na fonte primária como no modo completo e registra o modo na rodada e na síntese, porque a triangulação é menor (um índice só) e não há o modo profundo. As duas chaves acrescentam índices e o profundo. **Sem chave própria, mas dependem de outra:** a `story-angle` apura pela `research` e a `piece-creation` chama a `research`, a `image-gen` e a `slides-export`, cada uma com a sua. Por isso a apuração e o carrossel feito a partir de uma ideia crua, que passa pela apuração e pela pesquisa antes do roteiro, funcionam desde o clone, no modo só busca nativa; as chaves da `research` acrescentam índices. **As outras com chave não rodam antes de você configurar a sua:** o primeiro passo de cada uma confere, e sem a chave ela para e diz qual variável falta, onde se pega e como se põe. As APIs são cobradas à parte do plano do Claude: antes de usar, preencha a regra de custo das suas contas no `references/projeto.md` da `research` e da `image-gen`.

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
   python -X utf8 scripts/prepara_chaves.py --skill research
   ```
   Ele cria o `.env` a partir do `.env.example`, só se o `.env` ainda não existir (nunca sobrescreve, e não lê nem mostra um que já existe), e diz em que linha fica cada variável da skill que você passou (sem `--skill`, só cria). Abra o `.env` no seu editor e troque o marcador `COLE_...` pelo valor. Cada linha do `.env.example` diz para que serve a chave e onde se pega; linha que fica com o marcador conta como não configurada. O `.env` nunca vai ao git (`.gitignore`). O `.claude/settings.json` nega à ferramenta de leitura do Claude o `.env`, o `.env.local` e o `.claude/settings.local.json`, mas um comando de terminal não é barrado por isso: não peça ao Claude para abrir, mostrar ou procurar dentro desses arquivos, e não cole chave na conversa, nem em nenhum arquivo versionado. Quem lê as chaves são os scripts das skills.

   O `.env` é o caminho recomendado. A alternativa é o bloco `"env"` do `.claude/settings.local.json`, que também fica fora do git e que o Claude Code carrega como variáveis de ambiente da sessão: `python -X utf8 scripts/prepara_chaves.py --settings --skill research` o cria a partir do `.claude/settings.local.example.json`, com as mesmas variáveis e os mesmos marcadores do `.env.example`. Se o `settings.local.json` já existir (o Claude Code o cria ao guardar uma permissão que você aceitou), o script não mexe nele: copie o bloco `"env"` do exemplo para dentro dele, no seu editor. O JSON não aceita comentário, e o exemplo não leva campo de explicação, porque não confirmamos que o Claude Code aceita chave fora do esquema dele: a explicação fica aqui e no `.env.example`. Os dois caminhos funcionam no terminal e no Code do app desktop (testado em 19/11), e o `.claude/settings.json` nega a leitura dos dois ao Claude. Quando a mesma variável está nos dois, vale a do `settings.local.json`.

   Depois, reinicie a sessão e rode o passo 3 de novo.
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
| `python -X utf8 scripts/confere_ambiente.py` | skill por skill, o que já roda e o que falta | código 0, com o quadro: "pronta" nas skills que você configurou e "falta configurar" nas outras, com o que falta (a `research` sem as chaves sai "pronta no modo só busca nativa"); no alto, de onde vieram as chaves (o `.env` ou a variável do sistema) |
| `python -X utf8 scripts/confere_links.py` | os links entre os arquivos e as duas cópias dos agentes | `-- 0 link(s) quebrado(s)` |
| `python -X utf8 scripts/confere_dados.py` | chave, dado pessoal e conteúdo de terceiro no que iria num commit | `-- 0 achado(s)` e código 0; o seu e-mail real nos commits sai como achado (ver "Antes de commitar", acima) |
| `python -X utf8 scripts/teste_confere_dados.py` | os casos do `confere_dados.py` | `TODOS OK` |
| `python -X utf8 scripts/teste_medir_disparo.py` | os casos do `medir_disparo.py` | `TODOS OK` |
| `python -X utf8 scripts/teste_prepara_chaves.py` | os casos do `prepara_chaves.py`, numa pasta temporária | `TODOS OK` |
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

## Caminho 2: quem não programa (o Code, no app do Claude)

O app do Claude no computador tem a aba **Code**, que trabalha numa pasta do seu computador sem você abrir o terminal: é o mesmo Claude Code do caminho 1, numa janela. Para trabalhar com os arquivos de uma pasta, é o caminho que a Anthropic recomenda hoje (o Cowork, que fazia isso antes, foi fundido à conversa do app). Num teste de 19/11, numa cópia deste repositório, o Code do app desktop fez o que o caminho 1 faz: ao escolher a pasta, pediu para confiar nela; leu sozinho o `CLAUDE.md` como instrução; carregou as skills de `.claude/skills/`, que dispararam, e os agentes de `.claude/agents/`; rodou o aviso de início de sessão; recusou sozinho, sem pedir aprovação, a leitura do `.env` e do `.claude/settings.local.json`; leu as chaves dos dois arquivos; rodou o Python e chegou à rede.

1. **O que precisa:** uma conta paga do Claude (Pro, Max ou acima) e o app do Claude no computador (Windows ou macOS), em [claude.ai/download](https://claude.ai/download).
2. **Trazer o seu repositório para o computador.** O jeito mais simples é o [GitHub Desktop](https://desktop.github.com/): entre com a sua conta do GitHub, vá em File > Clone repository, escolha o repositório que você criou pelo **Use this template** e a pasta onde ele vai ficar. Assim, o que você gravar volta ao GitHub pelo próprio GitHub Desktop. Outro jeito: crie uma pasta vazia, escolha-a no passo 3 e peça ao agente "clona aqui o meu repositório", com o link dele; se faltar o Git ou o login do GitHub, ele diz o que falta e ajuda.
3. **Abrir a pasta no Code:** no app, abra a aba **Code**, escolha o ambiente "This computer" e a pasta do repositório (pode estar em outro disco). O app pergunta "Trust this workspace?" e lista o `.claude/settings.json` como o que pode rodar código: confie depois de ter lido as skills (acima). O modo de permissão vem em "Auto".
4. **Pedir ao agente o que faltar:** peça "confere o ambiente com o `scripts/confere_ambiente.py` e instala o que faltar". Se o Python não estiver instalado, o agente o instala antes, e depois os pacotes que o script apontar (o caminho 1 lista quais são, no passo 5).
5. **As chaves:** peça "cria o arquivo de chaves da research com o `scripts/prepara_chaves.py`" (troque `research` pela skill que você vai usar). Ele cria o `.env`, só se ainda não existir, e diz em que linha fica cada variável. Abra o `.env` num editor de texto (o Bloco de Notas serve) e troque o marcador `COLE_...` pelo valor; cada linha do arquivo diz para que serve a chave e onde se pega. Não cole a chave na conversa: o agente não consegue ler esse arquivo, e é assim que deve ser. Quem lê as chaves são os scripts das skills. Depois, comece uma sessão nova. (O bloco `env` do `.claude/settings.local.json` também funciona, ver o passo 4 do caminho 1.)
6. **Preencher o contexto:** `context/sobre-mim.md` e `context/publico.md` vêm em branco, com o roteiro. Peça ao agente para fazer as perguntas do roteiro e preencher com você.
7. **Usar:** peça em linguagem natural ("registra esta ideia", "revisa este texto", "pesquisa o que existe sobre …", "lança o que gastei hoje"). Antes de mandar ao GitHub, peça ao agente para rodar o `scripts/confere_dados.py` (ver "Antes de commitar", no caminho 1).

O que o caminho 1 diz das skills, das chaves e das conferências vale aqui: é o mesmo programa. As conferências da tabela "Para conferir que está tudo certo" o agente roda por você.

**Acompanhar pelo celular:** o app desktop tem o Remote Control, que permite acompanhar pelo celular uma sessão aberta no computador. Ainda não testamos esse uso aqui: conte com ele como possibilidade.

**Aviso para quem usa o assistente no e-mail e na agenda:** o Gmail e a Agenda pelos conectores da conta (Customize > Connectors) foram testados dentro do Code em 19/11: enviaram e-mail, criaram e apagaram evento. No modo de permissão "Auto", que é o padrão, essas ações aconteceram sem pedir confirmação: o agente enviou o e-mail e criou ou apagou o evento sem perguntar antes. Para exigir a confirmação, ligue "Always ask" nas ferramentas do conector (a de enviar, a de criar e a de apagar), ou use um modo de permissão que pergunte antes de agir. Se um plugin instalado trouxer um conector próprio de agenda ou de e-mail que falha, reconectar o conector da conta (Customize > Connectors) resolveu no teste.

**Ainda por testar, antes de contar com isso:**
- o caminho pela conversa do app (o chat), sem pasta, com as skills instaladas na sua conta pelo ZIP do `scripts/empacota_skills.py` (Customize > Skills): fica para depois.

## A vida pessoal

As pastas `finance/`, `health/` e `maps/` vêm com o README do método e o roteiro do que preencher, e nenhum registro: o arquivo de cada coisa (o mês das finanças, o plano de treino, o exame, o retrato de um mapa) nasce quando você contar a primeira informação dele. Os mapas sugeridos, cada um com um guia curto em `maps/guides/`: Vision Board, Roda da Vida, Big Five (pelo IPIP-NEO-120, de domínio público), SWOT, Ikigai, Matriz EREC e OKR. O quadro `maps/board/` abre no seu navegador, com os modelos em branco, e não se publica em link.

O assistente não diagnostica, não estima personalidade pela conversa e sugere o profissional quando o assunto pede. O porquê está em [`decisions/vida-pessoal-e-mapas.md`](./decisions/vida-pessoal-e-mapas.md).

## A base de conhecimento

A `knowledge/` traz 89 sínteses de método, por área (avaliação e revisão por agentes, design de conteúdo, mídia gerada, apuração, dados, psicologia, o Claude Code, vendas, engenharia de software), e 463 fichas de fonte. Num repositório público, nenhuma ficha traz o texto integral da fonte: as de licença livre e as de fonte protegida vêm em palavras próprias, com citações curtas, e o integral se lê na fonte, pelo link. As três fichas livres que ainda têm trecho colado à fonte vêm só como citação simples (o título, o autor, o link e a licença). A régua está em [`knowledge/sources/README.md`](./knowledge/sources/README.md).

## A licença

O código é MIT ([`LICENSE`](./LICENSE)); o texto é CC BY 4.0 ([`LICENSE-texto`](./LICENSE-texto)). O material de terceiro segue a licença dele, e as 17 fichas de fontes em CC BY-SA são exceção declarada, na licença da fonte (a lista está no `LICENSE-texto`).

## Como o repositório se organiza

O mapa do que ler, e quando, está no [`index.md`](./index.md); as regras de manutenção, no [`CLAUDE.md`](./CLAUDE.md); os termos do método, no [`glossario.md`](./glossario.md). Em resumo: `context/` (quem você é e para quem fala), `decisions/` (o porquê das regras), `knowledge/` (a base de método, com as fontes e a régua de conteúdo de terceiro), `marketing/` (ideias, séries, rubricas), `finance/`, `health/` e `maps/` (a vida pessoal), `.claude/skills/` (as skills) e `scripts/` (os conferidores e o empacotador).
