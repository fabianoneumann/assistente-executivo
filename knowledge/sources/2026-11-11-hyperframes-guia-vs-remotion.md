---
titulo: "HyperFrames vs Remotion (guia oficial)"
tipo: artigo
autor: "HeyGen (heygen-com/hyperframes)"
url: "https://github.com/heygen-com/hyperframes/blob/main/docs/guides/hyperframes-vs-remotion.mdx"
publicado_em: 2026-10-26   # último commit do guia (0390f3f908)
capturado_em: 2026-11-11
licenca: "Apache 2.0 (arquivo LICENSE na raiz do repositório heygen-com/hyperframes: o texto padrão da versão 2.0, de janeiro de 2004, com 'Copyright 2026 HeyGen, Inc.'; a raiz não tem arquivo NOTICE). Texto da licença: http://www.apache.org/licenses/LICENSE-2.0"
areas: [generative-media]
tags: [hyperframes, remotion, video-as-code, claude-code-skills, rendering, migration]
---

# HyperFrames: o guia "vs Remotion" (novembro de 2026)

Ficha de estudo em palavras próprias; o arquivo integral (Apache 2.0) não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Um arquivo da documentação do repositório `heygen-com/hyperframes`, baixado com `gh api` (conteúdo bruto) em 2026-11-11, no commit `668983e1a63e` (o `main` das 10:55 UTC de 11/11, oito commits depois da tag v0.9.33, `e596be16`; o arquivo não mudou entre a tag e esse commit): `docs/guides/hyperframes-vs-remotion.mdx` (último commit `0390f3f908`, 2026-10-26). A página publicada, https://hyperframes.heygen.com/guides/hyperframes-vs-remotion, foi baixada com curl no mesmo dia; o texto dela bate com o `.mdx` nos trechos conferidos (o pedido e a tabela do teste). O FAQ, lido no mesmo commit, tem ficha própria: [[2026-11-11-hyperframes-faq]].

**Quem fala.** O guia é da HeyGen, que faz o HyperFrames, comparando o próprio produto com o concorrente. O teste lado a lado é dela e não vem com material para refazer: os dois vídeos estão em `static.heygen.ai`, mas os projetos, os registros da sessão e a máquina não.

**O que mudou em relação à ficha de setembro.** A [[2026-09-29-hyperframes-readme]] trazia só a tabela comparativa do README (autoria, build, animação por relógio, render distribuído, licença). Este guia é material novo: um teste com o mesmo pedido nos dois motores, o mesmo cartão de título escrito nos dois códigos, uma seção franca sobre o que o Remotion faz melhor e o funcionamento da skill de migração.

## O teste lado a lado

- **Condições:** Claude Code com o Opus 5.5, o mesmo pedido de um parágrafo duas vezes, uma só com as skills oficiais de agente do Remotion instaladas e outra só com as do HyperFrames. Uma rodada de cada, sem repetir e sem editar nada depois.
- **O pedido:** vídeo de lançamento de 15 segundos em 1920×1080 (horizontal) para um app fictício de notas, o Inkwell, com slogan; revelação do logo, três frases curtas de recurso e um cartão final com o slogan; sem voz; o MP4 final em `out.mp4` na pasta. O pedido termina com "Don't ask me questions; make the choices yourself."
- **Remotion:** 12 min 30 s até o MP4 renderizado; 10 arquivos TypeScript, 1.037 linhas; cerca de 950 MB de `node_modules` instalados no projeto; nenhum som.
- **HyperFrames:** 11 min 50 s; 4 arquivos HTML, 822 linhas; nada instalado no projeto; uma trilha de fundo e cinco efeitos sonoros escolhidos pelo agente.
- **A ressalva do próprio guia:** "Both are good videos; a single run decides nothing about quality." O que dura, segundo ele, é o que fica na mão: um projeto React para seguir construindo em código, ou arquivos HTML que se abrem no navegador, se editam com um agente ou no app Studio.
- **Lacunas:** o guia não diz em que máquina e sistema rodou, que versão das skills de cada lado foi usada, nem se o tempo inclui a instalação; o som entrou no lado do HyperFrames sem que o pedido o pedisse.

## O mesmo cartão de título nos dois códigos

Três segundos de um título que aparece, fica e some, escritos dos dois jeitos; o guia diz que nenhuma das versões foi inchada nem aleijada para provar um ponto.

- **No Remotion,** o componente é uma função do número do quadro corrente, e a conta do tempo é feita em quadros: um `interpolate()` leva a opacidade de 0 a 1 nos quadros 0 a 15, segura até o 75 e volta a 0 no 90, com a extrapolação presa dos dois lados. Um `<Composition>` em outro arquivo registra a peça como 90 quadros a 30 fps, em 1280×720.
- **No HyperFrames,** o markup declara quando cada coisa está na tela e uma timeline do GSAP declara como ela se move, os dois no mesmo arquivo e com o tempo em segundos. Três regras fazem a peça renderizar: todo espaço visível leva `class="clip"` com `id`, `data-start`, `data-duration` e `data-track-index`; a timeline nasce pausada; e ela é registrada em `window.__timelines` com o mesmo id do elemento raiz. Sem o registro, sai um quadro parado, sem movimento.
- **O juízo do guia:** nenhum dos dois é obviamente melhor. O do Remotion é uma função pura que se acompanha de cabeça; o do HyperFrames é uma página que se abre no navegador e se inspeciona no devtools.

## Onde os dois diferem

- **O que se escreve:** HTML, CSS e JavaScript no HyperFrames; React e TypeScript no Remotion.
- **Como o movimento é cronometrado:** o HyperFrames pausa a animação e a leva ao instante exato (o *seek*) antes de capturar cada quadro; no Remotion, o código lê o número do quadro e devolve os valores daquele quadro. Por o motor conduzir a animação em vez de olhar um relógio, GSAP, Web Animations, Lottie e outros runtimes do navegador saem determinísticos, o mesmo quadro igual a cada vez.
- **Material web que já existe:** HTML, CSS e uma animação GSAP ou Lottie costumam entrar quase como estão no HyperFrames; no Remotion, são reescritos como componentes React.
- **Licença:** Apache 2.0 no HyperFrames; no Remotion, licença própria, grátis para pessoas e empresas de até três pessoas e paga acima disso, com o aviso de conferir os termos atuais.
- **Editor visual:** os dois têm um e os dois gravam as mudanças no código-fonte. O editor do HyperFrames no navegador edita o mesmo DOM que o motor captura; o Remotion Studio edita composições React. Não são intercambiáveis, e nenhum substitui editar a fonte numa mudança de estrutura.
- **Onde renderiza:** os dois em AWS Lambda; o HyperFrames também na máquina local, na nuvem hospedada da HeyGen e no Google Cloud Run.

## O que cada um faz melhor, segundo o guia

- **Remotion:** é mais antigo e muito mais estabelecido, com mais templates, tutoriais, perguntas respondidas e histórico de produção; o Remotion Lambda é um sistema de render maduro e muito documentado, e o guia diz que o do HyperFrames é mais novo. Para um time que já escreve React, vêm de graça os componentes, o design system, as bibliotecas de gráfico e as entradas de composição tipadas e validadas. E o modelo é mais simples de guardar na cabeça: uma função pura do número do quadro, sem timeline para registrar nem contrato para errar por pouco.
- **O lado fraco do HyperFrames que o guia admite:** ele pede que se sigam regras (timeline pausada, nada de relógio de parede, nada de aleatório sem semente) e "breaks quietly if you don't".
- **HyperFrames:** não precisa de React, de build nem de reescrever componentes; um site, um protótipo em HTML, um design exportado ou uma animação de navegador já estão perto de uma composição. É feito para um agente de IA escrever: as skills carregam as regras do framework, o agente escreve composições válidas em vez de adivinhar, e uma pessoa edita depois o mesmo arquivo no editor do navegador. A Apache 2.0 dispensa contagem de assentos e revisão de licença.

## A skill de migração do Remotion

- **Instalação:** `npx skills add heygen-com/hyperframes --skill remotion-to-hyperframes`; depois, pedir ao agente que porte a composição.
- **O que ela traduz:** `useCurrentFrame` e `interpolate` viram tweens de timeline, `Sequence` vira clip, e os quadros viram segundos.
- **O que ela recusa:** o que não cabe no modelo, como máquinas de estado React feitas com `useState` ou `useEffect`, metadados assíncronos e bibliotecas de interface React de terceiros. Esses casos são apontados em vez de traduzidos errado em silêncio.
- **Como ela se confere:** renderiza as duas versões e as compara quadro a quadro, e escreve o que deixou de fora.
- **O conselho do guia:** migrar porque o material de origem ou o time se encaixa melhor do outro lado, não porque um framework parece mais novo.
