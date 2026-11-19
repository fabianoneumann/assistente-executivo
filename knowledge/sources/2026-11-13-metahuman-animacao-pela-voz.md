---
titulo: "Audio Driven Animation | MetaHuman Documentation"
tipo: artigo
autor: "Epic Games (documentação oficial do MetaHuman)"   # a página não tem assinatura de pessoa
url: "https://dev.epicgames.com/documentation/en-us/metahuman/audio-driven-animation"
publicado_em: null   # sem data visível; o HTML tem carimbos created_at e updated_at de 2025-11-03 de um bloco, que datam o bloco, não a página
capturado_em: 2026-11-13
licenca: "protegido (documentação da Epic Games; nenhum aviso de direitos nem licença de conteúdo no HTML baixado, cujo rodapé é montado no navegador; tratada como protegida); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [metahuman, unreal-engine, facial-animation, lip-sync, audio, sequencer]
---

# MetaHuman Animator: a animação do rosto tirada de um arquivo de áudio, fora do tempo real

Nota de fato: os passos do processo numa lista, porque a ordem é o método, e tabelas dos pré-requisitos e das opções, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida. É fonte técnica curta que lista o que cada opção faz, então segue a ordem da página (o `README.md` desta pasta, item 2, a exceção da página técnica); a medida da cópia é a do `parafrase.py` e a da conta lado a lado.

**Proveniência.** Página da documentação do MetaHuman em dev.epicgames.com, baixada com `curl` em 13/11/2026 e lida no texto do bloco `<article>` (688 palavras, da abertura ao "Next Up"), conferido no HTML; sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco, não do arquivo HTML); Wayback http://web.archive.org/web/20260226151728/https://dev.epicgames.com/documentation/en-us/metahuman/audio-driven-animation. Título conferido no `<title>`: "Audio Driven Animation | MetaHuman Documentation | Epic Developer Community". Lida a página inteira; as imagens (o painel e a tabela numerada) não foram vistas, e as páginas ligadas (as recomendações de captura de áudio, a animação em tempo real por Live Link, o processamento em lote no Content Browser) não foram abertas.

**Conferência lado a lado** (2026-11-13, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra `epic-metahuman-audio-driven-animation.txt` (o texto do bloco, na cópia de trabalho), com 32 unidades medidas (19 de prosa, 13 de célula com texto), 2 coladas, que são nomes em inglês (o Realtime Audio Solver; os menus do Content Browser), fatos sem outra grafia, e 0 trechos de 3 ou mais seguidas. Na leitura lado a lado, segue a fonte a unidade que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela, e conta como unidade que segue a fonte a célula que o script partiu em pedaços da mesma frase: 20 de 24 unidades do corpo (de "Em uma frase" em diante), 20 de 32 com as 8 do cabeçalho de proveniência, que não tratam do conteúdo. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 19, de "O recurso" às opções: a página é técnica e lista fatos, e a ficha segue a ordem dela pela exceção do item 2; não há texto argumentativo do autor na página. Na revisão de 2026-11-19, a linha do Downmix Channels e a tabela dos parâmetros adicionais foram refeitas: a tabela deixou a numeração da página e agrupa os parâmetros pelo que controlam, com o Realtime Audio por último e aberto pelo efeito, e as células já não vertem a frase da página; nenhuma das 7 células com texto refeitas segue mais uma frase da fonte, e a sequência de 19 acima termina antes delas, na linha do Generate Blinks.

## Em uma frase

O recurso Audio Driven Animation do MetaHuman Animator transforma um arquivo de áudio de voz em animação facial de um MetaHuman, com movimento de cabeça, piscadas e humor ajustáveis, gerada fora do tempo real em faixas do Sequencer e exportável como Animation Sequence ou Level Sequence, num projeto da 5.6 ou mais nova.

## O recurso

| Item | Fato |
|---|---|
| Onde fica | no MetaHuman Animator |
| O que faz | áudio vira animação facial realista |
| Modos | em tempo real ou fora dele; a página trata do de fora |
| O que o modo de fora acrescenta | parâmetros que mexem no movimento da cabeça, nas piscadas e no humor |
| Formato de áudio | qualquer um que o Unreal aceite como asset SoundWave |
| O Realtime Audio Solver no asset de Performance | ainda é processo fora do tempo real, e não é o mesmo que animar ao vivo por uma fonte Live Link de áudio |
| No UEFN | disponível, menos exportar um Level Sequence a partir de uma performance |

## Pré-requisitos

| Item | Fato |
|---|---|
| Projeto | Unreal Engine 5.6 ou mais novo |
| Plugin | MetaHuman Animator ligado |
| Áudio | um ou mais assets SoundWave, de arquivo existente ou gravados pelo Take Recorder com um dispositivo de áudio |

## Os passos no editor do asset de Performance

1. Criar um asset MetaHuman Performance pelo menu do Content Browser (MetaHuman Animator > MetaHuman Performance).
2. Abrir o asset e, no painel Details, escolher Audio como tipo de entrada.
3. Escolher o SoundWave que vai gerar a animação.
4. Escolher a malha do rosto do MetaHuman em Visualization Mesh.
5. Clicar em Process: o áudio vira as faixas de animação do Facial Rig no Sequencer.
6. Exportar por Export Animation ou Export Level Sequence; no Level Sequence, atribuir o Blueprint do personagem MetaHuman.

## As opções

| Opção | O que faz |
|---|---|
| Downmix Channels | resolve de que canal sai a voz quando o áudio tem vários, o caso comum sendo o estéreo: com ela ligada, todos se misturam num mono antes do processamento; com ela desligada, só se processa o canal cujo número está em Audio Channel Index |
| Generate Blinks | liga ou desliga as piscadas geradas |

**Os parâmetros adicionais** (Additional Solve Parameters; a página abre a seção dizendo que a 5.6 trouxe mais opções, e não diz quais destas são novas):

Agrupados aqui pelo que cada um controla (a página os numera de 1 a 6: Head Movement, Frames to Process, Realtime Audio, Generate Blinks, Process Mask, Solve Overrides):

| Controla | Parâmetro | O que faz |
|---|---|---|
| Que trecho do áudio entra | Frames to Process | delimita, por um quadro inicial e um final, a parte do áudio que vira animação |
| O que sai | Head Movement | a cabeça do MetaHuman passa a se mexer também, recurso que os modos Depth e Real-Time (Video) já tinham |
| O que sai | Generate Blinks | põe as piscadas na animação ou as deixa de fora |
| O que sai | Process Mask | escolhe entre animar o rosto todo e gerar só as curvas da região da boca, estas para trocar ou empilhar outra animação de lábios no lip sync |
| O humor | Solve Overrides | em vez de deixar o humor no Auto Detect, fixa um da lista e regula a intensidade dele, que o Neutral não tem |
| O humor | Humores da lista | Neutral, Happy, Confident, Excited, Playful, Sad, Bored, Fear, Confused, Disgust, Anger, Surprise |
| O resto da tabela | Realtime Audio | ligado, desliga ou esconde as outras opções desta seção, porque troca o solver pelo algoritmo de tempo real, e este não move a cabeça |

## O que a fonte recomenda

Gravar ou importar a voz como SoundWave, seguir as recomendações de captura de áudio da Epic, processar no asset de Performance com a malha do rosto do personagem e exportar a animação; quem quer só a boca usa o Process Mask para sobrepor outra animação de lábios. Para muitos arquivos, a página aponta o processamento em lote no Content Browser.

## Citações

- "process audio into realistic facial animation. This can be done in real time or offline."
- "As of UE 5.6, we now have even more options for tweaking your audio solve."

## Lacuna

A página não diz em que versão o recurso estreou (só que a 5.6 trouxe mais opções e que o projeto precisa ser da 5.6 ou mais nova), quanto tempo leva o processamento, que máquina ou placa ele pede, nem se roda pela linha de comando ou por Python. Não diz se serve a personagem que não é MetaHuman, nem se trata mais de uma voz no mesmo arquivo. Não trata da licença do MetaHuman.
