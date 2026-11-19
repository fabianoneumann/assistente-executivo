---
titulo: "HyperFrames FAQ"
tipo: artigo
autor: "HeyGen (heygen-com/hyperframes)"
url: "https://github.com/heygen-com/hyperframes/blob/main/docs/faq.mdx"
publicado_em: 2026-11-04   # último commit do FAQ (c3eb052545)
capturado_em: 2026-11-11
licenca: "Apache 2.0 (arquivo LICENSE na raiz do repositório heygen-com/hyperframes: o texto padrão da versão 2.0, de janeiro de 2004, com 'Copyright 2026 HeyGen, Inc.'; a raiz não tem arquivo NOTICE). Texto da licença: http://www.apache.org/licenses/LICENSE-2.0"
areas: [generative-media]
tags: [hyperframes, remotion, video-as-code, claude-code-skills, pricing, telemetry, rendering, audio, captions]
---

# HyperFrames: o FAQ (novembro de 2026)

Ficha de estudo em palavras próprias; o arquivo integral (Apache 2.0) não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Um arquivo da documentação do repositório `heygen-com/hyperframes`, baixado com `gh api` (conteúdo bruto) em 2026-11-11, no commit `668983e1a63e` (o `main` das 10:55 UTC de 11/11, oito commits depois da tag v0.9.33, `e596be16`; o arquivo não mudou entre a tag e esse commit): `docs/faq.mdx` (último commit `c3eb052545`, 2026-11-04, com a mensagem "say HyperFrames is free, and what the Studio app's Pro plan adds"). A página publicada, https://hyperframes.heygen.com/faq, foi baixada com curl no mesmo dia; o texto dela bate com o `.mdx` nos trechos conferidos (o preço, o tempo de render, a telemetria). O guia "HyperFrames vs Remotion", lido no mesmo commit, tem ficha própria: [[2026-11-11-hyperframes-guia-vs-remotion]].

**Quem fala.** O FAQ é da HeyGen, que faz o HyperFrames; os tempos de render dele são números do fabricante.

**O que mudou em relação à ficha de setembro.** O FAQ traz o que a [[2026-09-29-hyperframes-readme]] não tinha: o app Studio com plano grátis e plano Pro pago, o Windows, a telemetria e o que funciona com e sem conta HeyGen.

## As respostas do FAQ

- **É grátis?** Sim: o framework, a CLI e as skills são Apache 2.0, e renderizar no próprio computador é grátis e não pede conta. O plano do agente de IA e os recursos hospedados opcionais da HeyGen (vozes, avatares, render na nuvem) cobram pelas contas de cada um. Há um guia para fazer vídeo com um agente grátis.
- **O app Studio e os planos:** o app é grátis para usar. O plano Free inclui narração por IA, legendas, música e efeitos sonoros, 3 clipes de vídeo por IA e 5 exportações na nuvem por mês. O plano Pro, US$ 25 por mês, acrescenta os melhores modelos de vídeo, imagem, voz e música da HeyGen, fazer um vídeo no estilo de um vídeo enviado pela pessoa e exportação na nuvem ilimitada. Lacuna: o FAQ não usa o nome "HyperFrames Pro" nem diz quais skills o plano libera.
- **Uso comercial:** permitido pela Apache 2.0, nos termos dela; a mídia que se acrescenta (fontes, música, filmagem) mantém a licença própria.
- **Que agente usar:** qualquer agente de código com suporte a skills, entre eles Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, Google Antigravity, IBM Bob e OpenCode; para quem não tem nenhum, começar pelo Claude Code ou pelo Codex.
- **No chat do Claude ou do ChatGPT:** pelo conector hospedado do HyperFrames, que cria e renderiza os vídeos na conta HeyGen da pessoa, sem instalar nada; perde-se a pasta local do projeto e o Studio, e o plano do produto de chat decide se dá para acrescentar um conector próprio.
- **Instalação:** no Claude Code, o plugin (`claude plugin marketplace add heygen-com/hyperframes` e `claude plugin install hyperframes@hyperframes`); nos outros agentes, `npx skills add heygen-com/hyperframes`, escolhendo **Core Skills**, e uma sessão nova do agente.
- **Conta HeyGen ou chave de API:** não para fazer e renderizar na máquina; sim para as vozes e a música da HeyGen, os avatares, o render na nuvem, o conector hospedado e o app Studio. O login é `npx hyperframes auth login`.
- **Windows:** a CLI e as skills rodam no Windows, inclusive o render pelo PowerShell, e o app Studio tem instalador para Windows de 64 bits (Intel e AMD). Para editar no navegador, `npx hyperframes preview`; há dicas para o render lento no WSL2.
- **App Studio e editor do navegador:** o app é um programa de desktop para Mac, Windows e Linux que junta numa janela um chat com o agente, a prévia e um editor, sem terminal; o editor do navegador é o que abre com `npx hyperframes preview` em qualquer projeto. Os dois editam os mesmos arquivos.
- **Diferença do Remotion:** vídeo do Remotion é componente React; do HyperFrames, HTML, CSS e JavaScript cronometrados por atributos de dados e uma timeline pausada. O HyperFrames não usa nem roda o Remotion.
- **Prévia e render:** `npx hyperframes preview` e `npx hyperframes render --output final.mp4`; o render precisa do FFmpeg, e `npx hyperframes doctor` confere a máquina.
- **Quanto demora um render:** depende da duração, da resolução e dos efeitos. No exemplo medido pelo fabricante, uma composição de 300 quadros em 1920×1080 renderizou em 9,8 s, e em 25 s com uma declaração de CSS cara deixada no lugar; `--quality draft` faz um render mais rápido para revisão. Lacunas: a máquina, a taxa de quadros e qual era a declaração de CSS não estão no FAQ (o detalhe fica no guia de desempenho, não lido aqui).
- **Narração, música e efeitos:** basta pedir. Com conta HeyGen, o agente usa as vozes da HeyGen e um catálogo de 10 mil faixas de música; sem conta, a voz é o Kokoro rodando no computador, a música é a que a pessoa põe no projeto (ou geração local, se instalada) e os efeitos vêm de um conjunto incluído.
- **Legendas:** o agente transcreve a fala de um vídeo de rosto falando, cronometra cada palavra e acrescenta as legendas sem alterar a filmagem.
- **Fontes próprias:** o arquivo da fonte vai no projeto, declarado com `@font-face`; uma fonte que o projeto não declara pode cair numa fonte padrão no render, e o `npx hyperframes lint` acusa isso.
- **Render na nuvem ou em servidor próprio:** `hyperframes cloud render` renderiza na nuvem da HeyGen e cobra créditos da conta; também dá para renderizar no próprio AWS Lambda ou Google Cloud Run, ou em Docker.
- **O vídeo vai para a HeyGen?** Não na prévia e no render locais: o projeto fica no computador. O render na nuvem sobe o projeto para a HeyGen, e o conector hospedado o monta na conta HeyGen. A CLI manda dados de uso, como nomes de comando e desempenho de render, que ficam anônimos "until you sign in"; nunca manda nomes de projeto nem conteúdo de vídeo. Desliga-se com `npx hyperframes telemetry disable`. O agente de IA manda os prompts para o provedor dele.
- **Algo falhou:** rodar `npx hyperframes doctor`, `npx hyperframes lint` e `npx hyperframes check` na pasta do projeto e dar ao agente a saída inteira.
