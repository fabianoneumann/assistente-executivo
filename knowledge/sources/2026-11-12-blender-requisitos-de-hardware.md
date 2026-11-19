---
titulo: "System Requirements for Blender"
tipo: artigo
autor: "Blender (blender.org)"   # página do site oficial; o texto gravado não traz assinatura de pessoa nem nome de organização
url: "https://www.blender.org/download/requirements/"
publicado_em: null   # o texto gravado não traz data nem número de versão do Blender
capturado_em: 2026-11-12
licenca: "licença não encontrada no texto gravado da página; a licença do manual do Blender não se estende ao site blender.org; tratada como protegida até conferir; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [blender, hardware, technical-requirements, gpu, vram]
---

# Blender: o mínimo é 8 GB de RAM e 2 GB de VRAM, o recomendado, 32 GB e 8 GB

Nota de fato: tabelas do que a página de requisitos do Blender diz sobre o computador para rodá-lo, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a licença do texto não foi encontrada, e a página se trata como protegida.

**Proveniência.** Página do site oficial do Blender, lida pelo Chrome em 12/11/2026, porque o `curl` deu 403; o texto do `<body>` (a página não tem `<main>`) foi gravado na cópia de trabalho. sha256 (hash omitido), do texto gravado (conferi que bate); Wayback `http://web.archive.org/web/20261110161817/https://www.blender.org/download/requirements/`. Título conferido no texto: "System Requirements for Blender". Cobertura: o texto gravado inteiro, que traz só a aba do Windows aberta; as abas de macOS e Linux aparecem só pelo nome, sem o conteúdo, e não foram lidas. A página não diz a que versão do Blender os números se referem. O texto tem pouco mais de 250 palavras.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), medido contra o texto gravado, com 20 unidades medidas (15 de prosa, 5 de célula com texto), 1 colada (a célula do OpenGL, que traz os nomes das extensões) e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 20 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a célula de rótulo e a frase que junta lugares distantes não contam. Resultado: 4 de 20 (as células da NVIDIA, do OpenGL, da mesa digitalizadora e do mouse); nenhuma frase de prosa segue a fonte. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 2 (NVIDIA e OpenGL), sem trecho colado de 3 ou mais.

## Em uma frase

A página oficial do Blender pede, no Windows, no mínimo Windows 8.1 de 64 bits, 4 núcleos com SSE4.2, 8 GB de RAM e 2 GB de VRAM com OpenGL 4.3, e recomenda Windows 11, 8 núcleos, 32 GB de RAM e 8 GB de VRAM.

## Windows

| Item | Mínimo | Recomendado |
|---|---|---|
| Sistema | Windows 8.1, 64 bits | Windows 11 |
| Processador | 4 núcleos com SSE4.2 | 8 núcleos |
| Memória | 8 GB | 32 GB |
| Placa de vídeo | 2 GB de VRAM, OpenGL 4.3, Vulkan 1.3 | 8 GB de VRAM |

## Placas de vídeo aceitas

| Fabricante ou API | O que a página pede |
|---|---|
| NVIDIA | GeForce 900 em diante; Quadro da arquitetura Tesla em diante, inclusive as RTX; driver da NVIDIA |
| AMD | GCN de 4ª geração em diante |
| Intel | arquitetura Kaby Lake em diante |
| OpenGL | 4.3 ou mais, com as extensões GL_ARB_shader_draw_parameters e GL_ARB_clip_control obrigatórias |
| Driver | sempre o mais recente, do site do fabricante |

## O resto

| Item | Fato |
|---|---|
| Compatibilidade | a página remete a uma lista das mudanças que quebram compatibilidade, que não foi aberta |
| Computador antigo | as versões anteriores seguem disponíveis para baixar |
| Mesa digitalizadora | aceita, e recomendada para escultura, pintura e desenho com Grease Pencil |
| Mouse | dá para usar com dois botões ou trackpad; três botões é o recomendado |
| Mais de um monitor | aceito |
| Tela | qualquer tamanho funciona; 1920×1080 é o mínimo recomendado |
| Render na GPU com o Cycles | requisitos próprios, no manual |

## O que a fonte recomenda

Para o uso pleno, a página aponta 8 núcleos, 32 GB de memória e 8 GB de VRAM, uma tela de pelo menos 1920×1080, mouse de três botões e o driver de vídeo mais novo; para render na GPU, manda ler o manual do Cycles, e quem tem máquina velha pode ficar numa versão anterior.

## Citações

- "Your old computer can run Blender forever."
- "a minimum resolution of 1920×1080 is recommended for optimal use"

## Lacuna

O texto gravado não traz os requisitos de macOS e Linux, nem a versão do Blender a que os números valem, nem data. O "see below" ao lado do Vulkan 1.3 não tem continuação no texto gravado, que só detalha o OpenGL. A página não dá números para o Cycles na GPU (manda ao manual) e não diz quanto de VRAM pede uma cena pesada ou um render em 4K.
