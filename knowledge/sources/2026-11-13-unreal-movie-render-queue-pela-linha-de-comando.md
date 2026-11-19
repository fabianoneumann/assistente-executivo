---
titulo: "Using Command Line Rendering with Move Render Queue in Unreal Engine"
tipo: artigo
autor: "Epic Games (documentação oficial do Unreal Engine)"   # a página não tem assinatura de pessoa
url: "https://dev.epicgames.com/documentation/en-us/unreal-engine/using-command-line-rendering-with-move-render-queue-in-unreal-engine"
publicado_em: null   # sem data visível; o título diz "Unreal Engine 5.9 Documentation"; o HTML tem carimbos created_at 2025-03-22 e updated_at 2025-03-25 de um bloco, que datam o bloco, não a página
capturado_em: 2026-11-13
licenca: "protegido (documentação da Epic Games; nenhum aviso de direitos nem licença de conteúdo no HTML baixado, cujo rodapé é montado no navegador; tratada como protegida); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unreal-engine, movie-render-queue, sequencer, command-line, offline-rendering, python, headless-rendering]
---

# Unreal Engine 5.9: renderizar pela Movie Render Queue a partir da linha de comando

Nota de fato: tabelas do que a página da documentação diz sobre os três jeitos de disparar a Movie Render Queue (MRQ) pela linha de comando, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida. É fonte técnica curta que lista fatos, então as tabelas seguem as seções da página, na ordem dela (o `README.md` desta pasta, item 2, a exceção da página técnica); a medida da cópia é a do `parafrase.py` e a da conta lado a lado. O título da página escreve "Move Render Queue", e o texto, "Movie Render Queue".

**Proveniência.** Página de dev.epicgames.com, baixada com `curl` em 13/11/2026 e lida no texto do bloco `<article>` (815 palavras, do aviso sobre `MoviePipelineMasterConfig.h` ao executor de exemplo), conferido no HTML; sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco, não do arquivo HTML); Wayback http://web.archive.org/web/20260129074012/https://dev.epicgames.com/documentation/en-us/unreal-engine/using-command-line-rendering-with-move-render-queue-in-unreal-engine. Título conferido no `<title>`: "Using Command Line Rendering with Move Render Queue in Unreal Engine | Unreal Engine 5.9 Documentation". Lida a página inteira; o script de exemplo citado no fim não foi aberto.

**Conferência lado a lado** (2026-11-13, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra `epic-mrq-linha-de-comando.txt` (o texto do bloco, na cópia de trabalho), com 25 unidades medidas (14 de prosa, 11 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas. Na leitura lado a lado, segue a fonte a unidade que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela, e conta como unidade que segue a fonte a célula que o script partiu em pedaços da mesma frase: 11 de 17 unidades do corpo (de "Em uma frase" em diante), 11 de 25 com as 8 do cabeçalho de proveniência, que não tratam do conteúdo. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 11, de "Antes dos modos" ao executor próprio: a página é técnica e lista fatos, e a ficha segue a ordem dela pela exceção do item 2; a vantagem que a página dá ao Python sobre o sistema antigo está numa célula só.

## Em uma frase

A MRQ deixou de lado os muitos argumentos do antigo Render Movie e aceita poucos argumentos básicos na linha de comando, com três modos (uma sequência com um preset, uma fila salva, ou um executor em Python com controle total), e a menor unidade de trabalho que se divide entre máquinas é um corte de câmera.

## Antes dos modos

| Item | Fato |
|---|---|
| Aviso de código C++ | quem referencia `MoviePipelineMasterConfig.h` troca por `MovePipelinePrimaryConfig.h` (grafia da página) |
| Como se monta o render | configuração em asset da MRQ, argumentos de linha de comando e executores em Python |
| Menor unidade distribuível | um corte de câmera, ou um shot de Level Sequence, e não um quadro |
| Por quê | os recursos de tempo real usam dados do quadro anterior, que não se dividem entre máquinas |
| Contra o sistema antigo | a MRQ abandona os argumentos do Render Movie; a lista aceita caiu a uns poucos argumentos básicos |
| O que compensa a lista curta | a personalização em Python, com mais controle do que o sistema antigo |

## Os três modos

| Modo | Argumentos | O que faz |
|---|---|---|
| 1. Uma sequência e um preset | `-LevelSequence` (o asset de Level Sequence) com `-MoviePipelineConfig` (um preset `UMoviePipelinePrimaryConfig`) | o uso mais básico; um trabalho só, num mapa só, com todos os shots da sequência |
| 2. Uma fila | `-MoviePipelineConfig` apontando para um `UMoviePipelineQueue` salvo pela interface da MRQ | roda cada trabalho da fila no mapa e com a configuração gravados nela |
| 3. Executor em Python | `-MoviePipelineLocalExecutorClass=/Script/MovieRenderPipelineCore.MoviePipelinePythonHostExecutor` e `-ExecutorPythonClass=...` | o motor sobe e cria o executor, que lê argumentos, configura ou cria trabalhos, roda a fila e fala com servidores externos |

## Os exemplos da página

| Item | Fato |
|---|---|
| Executável | `UnrealEditor-Cmd.exe` com o `.uproject` e o mapa |
| Argumentos comuns aos três exemplos | `-game -windowed -resx=1280 -resy=720 -log -notexturestreaming` |
| Mapa do exemplo | `subwaySequencer_P` |
| Sequência do exemplo | `/Game/Sequencer/SubwaySequencerMASTER.SubwaySequencerMASTER` |
| Preset do exemplo | `/Game/Cinematics/MoviePipeline/Presets/SmallTestPreset.SmallTestPreset` |
| Fila do exemplo | `/Game/Cinematics/MoviePipeline/Presets/BigTestQueue.BigTestQueue` |
| Executor do exemplo | `/Engine/PythonTypes.MoviePipelineExampleRuntimeExecutor` |

## O executor próprio em Python

| Passo | Fato |
|---|---|
| A classe | uma UClass em Python que herda de `unreal.MoviePipelinePythonHostExecutor` |
| O método a sobrescrever | `execute_delayed` |
| O arquivo de entrada | um `init_unreal.py` em `/Content/Python` que importa o módulo próprio |
| Por que ele é obrigatório | é o que faz o Unreal ler o arquivo Python e reescrevê-lo como UClass que a linha de comando aceita |
| O exemplo pronto | `\Plugins\MovieScene\MovieRenderPipeline\Content\Python\MoviePipelineExampleRuntimeExecutor.py` |
| O que o exemplo mostra | ler a linha de comando, fazer requisição HTTP e tentar conexão de socket local |
| Aviso | o exemplo pede mais argumentos do que os da página; ler o topo do arquivo antes de testar |

## O que a fonte recomenda

Para um render simples, uma sequência com um preset; para vários trabalhos, a fila salva pela interface; e, para controle total, um executor próprio em Python, com o `init_unreal.py` no projeto e o exemplo da Epic como ponto de partida. Quem distribui o render entre máquinas divide por corte de câmera, não por quadro.

## Citações

- "the smallest unit of distributable work in Unreal Engine is a single camera cut, or a Level Sequence Shot."
- "The list of supported command line arguments has been reduced to only a few basic arguments"

## Lacuna

A página não lista os argumentos aceitos além dos usados nos exemplos, não explica `-game`, `-windowed` nem `-notexturestreaming`, e não diz se o render roda sem janela ou sem tela: os três exemplos usam `-windowed`, e a página não traz `-RenderOffscreen` nem `-Unattended`. Não diz em que formato sai a imagem, nem trata do Movie Render Graph. Não diz a versão do motor a que se aplica além do título da documentação (5.9).
