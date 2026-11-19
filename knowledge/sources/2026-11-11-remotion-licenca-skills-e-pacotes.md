---
titulo: "Remotion v4.0.542: licença e preços, a licença do 5.0 (PR #3750), Agent Skills, transições, legendas, @remotion/sfx, @remotion/media-utils, npx remotion still e Studio"
tipo: artigo
autor: "Remotion AG"
url: "https://www.remotion.dev/docs/license/pricing"
publicado_em: 2026-11-09   # lançamento da v4.0.542 e último commit do LICENSE.md; as páginas dizem "Last updated on Nov 11, 2026" e os últimos commits dos .mdx vão de 2026-10-28 a 2026-11-11 (proveniência)
capturado_em: 2026-11-11
licenca: "documentação sem licença de conteúdo declarada no texto lido (rodapé: '© Copyright 2026 Remotion AG.'; a Remotion License, no LICENSE.md, dá permissão para usar o software 'for the purpose of creating videos and images' e não fala da documentação); ficha em palavras próprias e em estrutura própria, sem o integral. Os pacotes @remotion/sfx e @remotion/media-utils são MIT no npm, mas isso vale para o código, não para a página."
areas: [generative-media]
tags: [remotion, license, pricing, commercial-use, claude-code-skills, transitions, captions, sound-effects, audio-visualization, still-render, video-as-code]
---

# Remotion em novembro: quem paga, a licença do 5.0, o que vem pronto e como conferir um quadro

Ficha de estudo em palavras próprias, organizada por pergunta, não pela ordem das páginas. Não há integral: a documentação não declara licença de conteúdo.

**Proveniência.** Oito páginas da documentação, baixadas com curl (HTML) em 2026-11-11, e três materiais do GitHub lidos com `gh api` no mesmo dia. Páginas, com o último commit do `.mdx` de cada uma no `main` do repositório `remotion-dev/remotion` (as páginas publicadas trazem todas "Last updated on Nov 11, 2026", com o mesmo horário em quase todas): licença e preços, https://www.remotion.dev/docs/license/pricing (2026-10-28); Agent Skills, https://www.remotion.dev/docs/ai/skills (2026-10-28); `@remotion/transitions`, https://www.remotion.dev/docs/transitions/ (2026-10-28); Captions, https://www.remotion.dev/docs/captions/ (2026-10-28); `@remotion/sfx`, https://www.remotion.dev/docs/sfx/ (2026-11-11); `@remotion/media-utils`, https://www.remotion.dev/docs/media-utils/ (2026-10-28); `npx remotion still`, https://www.remotion.dev/docs/cli/still (2026-11-09); Studio, https://www.remotion.dev/docs/studio/ (2026-10-28). Do GitHub: o `LICENSE.md` do `main` (último commit `c86fc72b2b`, 2026-11-09, "Migrate public licensing links and branding to remotion.dev"), https://github.com/remotion-dev/remotion/blob/main/LICENSE.md; e o PR #3750, corpo e diff do `LICENSE.md` (`gh api repos/remotion-dev/remotion/pulls/3750` e `.../pulls/3750/files`), https://github.com/remotion-dev/remotion/pull/3750; e a árvore do repositório `remotion-dev/skills` em dois pontos, o último commit de setembro e o de hoje (`gh api repos/remotion-dev/skills/git/trees/a1b09e904a99?recursive=1` e `gh api repos/remotion-dev/skills/contents/skills`, com o `main` em `1fc074b74b`, 2026-11-11), https://github.com/remotion-dev/skills. Versão corrente: v4.0.542, lançada em 2026-11-09 (a última release do GitHub no dia); as páginas de instalação dizem "This assumes you are currently using v4.0.542".

**Conferência lado a lado** (2026-11-11, na reescrita pedida pela revisão do Passo 7, N23): unidade é a frase fora de tabela ou a célula preenchida de tabela, e uma unidade segue a fonte quando traduz uma frase dela, ou duas vizinhas, na ordem delas. Resultado: 64 de 137 unidades seguem uma frase da fonte (64 de 90 sem contar as células que só trazem um nome, um rótulo ou um valor). As comparações com setembro e as partes do PR, das legendas, dos efeitos sonoros e do media-utils ficam quase todas fora da conta; o que segue está nas tabelas de preço, de chave de licença, de skills e de flags do still, uma célula por frase da fonte, com as linhas agrupadas por quem paga, pelo que o agente precisa fazer e pelo que se quer conferir.

**O que mudou em relação à ficha de setembro** ([[2026-09-29-remotion-licenca-faq]], que leu o FAQ da licença):

- **O preço não mudou:** Creators a US$ 25 por mês, Automators a US$ 0,01 por render com mínimo de US$ 100 por mês.
- **A descrição do Creators mudou de palavras:** em setembro, o FAQ falava em US$ 25 "per person who writes Remotion code themselves"; a página de preços de agora fala em "per seat", diz que o plano cobre a criação manual de pouco volume e a construção de sistemas de motion design em ambiente local "including using AI agents and Remotion Studio", e manda "Get 1 seat per user". A página não diz que a regra do assento mudou, e esta ficha não afirma isso.
- **Skills:** a página lista 13. A árvore do repositório `remotion-dev/skills` no último commit de 29/09/2026 (`a1b09e904a`) tinha 12 pastas em `skills/`, e a de hoje tem 13; a nova é a `remotion-license`. O "28" que constava da síntese de setembro veio de um terceiro, não da documentação do Remotion.
- **Novo nesta captura:** o plano Enterprise com preço de partida, os créditos da Mux, a chave de licença que registra cada render e a marca de render de desenvolvimento (abaixo), e o PR da licença 5.0, citado no topo do `LICENSE.md`.
- **Um detalhe de redação:** a ficha de setembro cita o FAQ com a elegibilidade "an organization or team of individuals with up to 3 people". O `LICENSE.md` em vigor ainda diz "a for-profit organization with up to 3 employees"; a formulação do FAQ é a que o PR do 5.0 leva para o `LICENSE.md`.

## Quem paga e quanto

| Quem você é | Licença | O que paga |
|---|---|---|
| pessoa física; organização com fins lucrativos de até 3 empregados; organização sem fins lucrativos; quem ainda avalia o Remotion sem uso comercial (a elegibilidade do `LICENSE.md` em vigor; a página de preços resume como pessoas e empresas de até 3 pessoas) | Free License | nada, com todos os recursos e uso comercial ilimitado; "Terms apply", com link para conferir a elegibilidade |
| empresa fora da gratuita que monta ferramenta ou produto de vídeo automatizado: render em lote, editor de vídeo, app de prompt para vídeo, Remotion Player embutido | Company License, modo Remotion for Automators | US$ 0,01 por render, com mínimo de US$ 100 por mês; quem desenvolve o projeto de automação dispensa assento de Creators |
| empresa fora da gratuita que faz os próprios vídeos à mão e em pouco volume, ou monta sistemas de motion design em ambiente local, inclusive com agentes de IA e o Studio | Company License, modo Remotion for Creators | US$ 25 por mês por assento, um assento por usuário |
| empresa com as duas frentes | Company License, os dois modos | a soma, que a calculadora da página faz |
| quem tem necessidades avançadas | Enterprise License | a partir de US$ 500 por mês |

- **O que vem com o que se paga:** toda Company License leva uso comercial, cobrança pelo uso, suporte prioritário e, para cliente novo da Mux, US$ 250 em créditos dela. O Enterprise acrescenta canal privado no Slack, Discord ou Teams, uma consultoria por mês, termos, cobrança e preço sob medida, formulários de conformidade, prioridade nos pedidos de recurso e o Editor Starter.
- **A calculadora no HTML baixado** marcava 10 mil renders a US$ 100, Creators "Not selected" com 3 assentos a US$ 75 e total de US$ 100 por mês, com a frase "At this spend, you are eligible for the Enterprise License". Lacuna: a página não diz a partir de que gasto vale essa frase, e o Enterprise começa em US$ 500.

| O `LICENSE.md` em vigor deixa | Não deixa |
|---|---|
| usar o software para criar vídeos e imagens, com fim comercial ou não | copiar ou modificar o código para vender, alugar, licenciar ou sublicenciar um derivado próprio do Remotion |
| modificá-lo para o próprio caso, ou para devolver correções e melhorias ao projeto | — |

A Company License vale para os mesmos usos da gratuita, mais o suporte prioritário. Não há garantia de nenhum tipo, e o suporte da gratuita é "best-we-can-do", pelas issues do GitHub e pelo Discord.

**Como cada render é contado** (flag `--license-key`, desde a v4.0.539, que manda um evento de uso pelo `@remotion/licensing`):

| Situação | O que se passa |
|---|---|
| render no servidor: `renderMedia()`, `renderStill()` e a CLI | a chave privada, que começa com `rm_sec_` |
| render no navegador com o `@remotion/web-renderer` | a chave pública, `rm_pub_` |
| quem cabe na licença gratuita | `"free-license"`, no lugar da chave |
| Studio | a licença escolhida em Settings → License, gravada no arquivo de configuração por `Config.setPublicLicenseKey()` |

As duas chaves ficam na página License keys do projeto, no Remotion Dashboard. Render de desenvolvimento vai com `--is-production=false` e não entra como cobrável, o que só tem efeito havendo chave.

## O que muda na 5.0 (PR #3750, aberto e sem merge)

- **O PR:** "`remotion`: Prepare Remotion 5.0", aberto em 2024-04-22, ainda aberto e em rascunho, sem merge, última atualização em 2026-11-04, com 66 arquivos alterados. O topo do `LICENSE.md` em vigor avisa que a licença "will slightly change" no 5.0 e aponta para ele. Lacuna: nenhuma das páginas dá data para o 5.0.
- **As duas mudanças efetivas, segundo o corpo do PR:** os prestadores de serviço passam a contar no tamanho do time ("Contractors also count towards team size"; antes, uma empresa podia trabalhar só com prestadores e nunca precisar da licença de empresa); e a licença de empresa passa a ficar presa a termos e condições próprios, escritos pela Remotion e introduzidos com o 5.0 (o PR diz que os termos anteriores tinham saído de um gerador e "did not make sense").
- **O que o diff do `LICENSE.md` mostra:** a elegibilidade troca "a for-profit organization with up to 3 employees" por "an organization or team of individuals with up to 3 people"; o uso permitido troca "videos and images" por "media assets (e.g. videos and images)"; a introdução passa a falar em "for-profit organizations and groups of individuals of a certain size". Entra uma proibição nova: operar um serviço de render que deixe o usuário final trazer ou subir o próprio código Remotion, sem aprovação prévia, explícita e por escrito, e isso "regardless of whether you are eligible for the Free License". E entra uma seção de termos: quem usa o software precisa aceitar os termos e condições, descritos como juridicamente vinculantes.

## O que vem pronto para som, legenda e transição

- **Transições (`@remotion/transitions`, desde a v4.0.53):** o componente `<TransitionSeries>` (uma sequência com transições entre as cenas), dois timings prontos (`springTiming()`, com `spring()`, e `linearTiming()`, linear com easing opcional) e timing próprio. A lista de apresentações tem 20 efeitos e o `none()`, que não faz efeito visual: `fade()`, `pushCut()` (um corte seco com um clarão breve), `slide()`, `wipe()`, `flip()`, `clockWipe()`, `iris()`, `cube()` (as duas cenas giram em perspectiva 3D) e doze marcados "HTML-in-canvas": `zoomBlur()`, `dreamyZoom()`, `filmBurn()`, `linearBlur()`, `bookFlip()`, `zoomInOut()`, `dissolve()`, `ripple()`, `crosswarp()`, `crossZoom()`, `swap()` e `blurSlide()`. Fecha a lista um item à parte, "Audio transitions", para pôr um efeito sonoro numa transição. Dá para escrever uma apresentação própria, e o menu lista `useTransitionProgress()` e `makeHtmlInCanvasPresentation()`. Licença do pacote: Remotion License.
- **Legendas:** a página Captions só aponta para quatro guias, dois de entrada (importar `.srt` ou `.vtt`; gerar as legendas transcrevendo o áudio) e dois de saída (pô-las no vídeo; exportá-las, queimadas ou em `.srt`), e deixa a referência das funções para o pacote `@remotion/captions`. O menu de pacotes da documentação também lista `@remotion/install-whisper-cpp`, `@remotion/openai-whisper`, `@remotion/whisper-webgpu` e `@remotion/elevenlabs`. Lacuna: os quatro guias e esses pacotes não foram lidos.
- **Efeitos sonoros (`@remotion/sfx`, desde a v4.0.429):** URLs de efeitos sonoros para uso geral, pelo pacote ou carregando a URL direto, com volume normalizado para o pico em -3 dB. A página traz 32 efeitos: os de uso neutro (`whip`, `whoosh`, `pageTurn`, `uiSwitch`, `mouseClick`, `shutterModern`, `shutterOld`, `ding`, `recordScratch`) e, na maior parte, sons de meme, de programa ou de marca, pelos nomes e descrições da própria página (`vineBoom`, `windowsXpError`, `spongebobFail`, `wilhelmScream`, `minecraftHurt`, `snapchatNotification`, entre outros). Sobre o uso, a página diz duas coisas: "All files can be used without attribution", no topo, e, na seção de licença, pacote npm MIT e, para os sons, ver a licença na página de cada um. Lacuna: as páginas de cada som não foram lidas.
- **Áudio e vídeo como dado (`@remotion/media-utils`, licença MIT):** para saber o que há num arquivo, `getVideoMetadata()`, `getAudioData()` (e a versão em hook, `useAudioData()`), `useWindowedAudioData()` (busca só o trecho corrente e só lê `.wav`) e `getAudioDurationInSeconds()`; para desenhar a onda, `visualizeAudio()` (música), `visualizeAudioWaveform()` (voz), `getWaveformPortion()` (recorta o dado de áudio numa onda) e `createSmoothSvgPath()` (leva os pontos da onda a um caminho SVG suave); para serializar um buffer de áudio, `audioBufferToDataUrl()`. Só o `useAudioData()` depende do Remotion; as outras rodam fora dele.

## Como o agente trabalha e como se confere um quadro

**As 13 Agent Skills** se instalam com `npx skills add remotion-dev/skills`, com `gh skill install remotion-dev/skills` ou na criação de um projeto com `bun create video`; a página as indica para Claude Code, Codex, Kimi Code e Cursor.

| Etapa | O agente precisa | Skill |
|---|---|---|
| escrever | de um ponto de entrada, sem saber qual skill usar | `/remotion-best-practices`, que reúne todas |
| escrever | abrir projeto ou composição nova | `/remotion-create` |
| escrever | acertar o markup React: composições, animação, layout, tipografia, mídia, efeitos, áudio, fontes, tempo | `/remotion-markup` |
| escrever | fazer mapa: estático, rota e marcador animados, explicação geográfica, Mapbox, MapLibre, MapTiler, GeoJSON, sobrevoo 3D com CesiumJS | `/remotion-maps` |
| escrever | legendar | `/remotion-captions` |
| escrever | tratar mídia no navegador com o Mediabunny, como ler metadados de vídeo e áudio | `/remotion-multimedia` |
| ver e entregar | abrir a prévia no Studio | `/remotion-studio` |
| ver e entregar | renderizar vídeo ou still | `/remotion-render` |
| ver e entregar | deixar o código editável no Studio quando um elemento não se deixa selecionar ou editar | `/remotion-interactivity` |
| produto | desenhar a arquitetura de um app ou de uma integração de produto sobre o Remotion | `/remotion-saas` |
| consultar e manter | conferir API, props e guias antes de implementar, buscando na documentação e trazendo qualquer página em markdown | `/remotion-docs` |
| consultar e manter | saber de licença, FAQ, termos e onde comprar (desde a v4.0.540) | `/remotion-license` |
| consultar e manter | atualizar o Remotion, os pacotes ligados, o Mediabunny compatível e as próprias skills | `/remotion-upgrade` |

**O Studio** serve à prévia e, com um servidor conectado, também ao render; lá dentro se navegam e usam os Elements, os da Remotion e bibliotecas de terceiros, e se escolhe a licença (tabela da chave, acima).

| Como abrir | O que fazer |
|---|---|
| por um agente de código (Claude Code, Codex, Cursor) | instalar o plugin do Remotion e chamar `/remotion-studio`; o agente abre o Studio no navegador, ou no navegador interno se tiver |
| pelo terminal | com a `@remotion/cli` (a maioria dos templates já traz), `npm start`, ou `npm run remotion` nos templates de Next.js e React Router 7, ambos atalhos de `npx remotion studio`; o servidor sobe na porta 3000 ou na primeira livre acima |

**Um quadro como imagem** (`npx remotion still`, desde a v2.3, grava um quadro da composição em arquivo):

| Para conferir | Como |
|---|---|
| um quadro | `--frame`: 0 por padrão; desde a v3.2.27, negativo conta do fim, e -1 é o último |
| vários quadros | `remotion render` com `--frames`, por exemplo `--frames=0,30,90 --image-format=png` (desde a v4.0.502) |
| noutro formato | `--image-format`: `png` (padrão), `jpeg`, `pdf` ou `webp` |
| com mais detalhe | `--scale`, acima de 0 e até 16; vetores e texto ganham detalhe |
| com dados próprios | `--props`, JSON ou caminho de arquivo; no Windows, só arquivo, porque os shells comem as aspas do JSON |
| dando mais tempo ao carregamento | `--timeout`: quanto um quadro espera as chamadas de `delayRender()`, em ms, 30 s por padrão |
| vendo o render acontecer | `--disable-headless`, que abre uma janela do Chrome (pede o Chrome for Testing ou um executável próprio) |
| com a GPU no Linux | `--chrome-mode=chrome-for-testing`, no lugar do `headless-shell` padrão |
| no tema escuro | `--dark-mode` |
| com os efeitos num backend escolhido | `--preferred-effect-backend` (desde a v4.0.540): `webgpu`, `webgl2` ou `2d`, e o `auto` tenta nessa ordem; no Lambda, só WebGL2 ou 2D; vale também na prévia do Studio |
| com outras flags do Chrome | `--chromium-flags`, `--chromium-features` e `--chromium-blink-features`, marcadas v4.0.543, uma versão acima da última lançada no dia; a página avisa que as flags padrão do Chrome podem mudar entre versões de correção |

- **O `--gl` nesta página:** aceita `angle`, `egl`, `swiftshader`, `swangle`, `vulkan` (desde a v4.0.41) e `angle-egl` (desde a v4.0.51 aqui; a página do `--gl` diz v4.0.52), com padrão `null`, o Chrome decide, menos no Lambda, onde é `swangle`. Pelo histórico da seção, o `angle` foi padrão de v2.4.3 a v2.6.6 e saiu por um pequeno vazamento de memória que podia derrubar renders longos; no Lambda, o padrão foi `swiftshader` de v2.6.7 a v3.0.7 e é `swangle` desde a v3.0.8, quando o Chrome 101 passou a suportá-lo. GPU e `--gl` por ambiente na ficha [[2026-11-11-remotion-three-e-gpu]].
- **No 5.0** sai a `--enable-multiprocess-on-linux`.
