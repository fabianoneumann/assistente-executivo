---
titulo: "3b1b/videos (README do repositório)"
tipo: artigo
autor: "Grant Sanderson, 3Blue1Brown (3b1b/videos)"
url: "https://github.com/3b1b/videos"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "CC BY-NC-SA 4.0 para o conteúdo do repositório (README e LICENSE.txt); o Manim em si é MIT. Só a ficha, pela cláusula NC; o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [manim, diagram-animation, real-production, workflow]
---

# O código dos vídeos do 3Blue1Brown: o Manim usado num canal real

Nota de fato: o texto integral não entra (licença abaixo); a cópia de trabalho fica fora do repositório.

**Proveniência.** README do repositório; cópia de trabalho na cópia de trabalho. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 11489 estrelas, criado em 2020-12-31, último push em 2026-11-10, 48 issues e PRs abertos, última release nenhuma, licença reconhecida pelo GitHub: NOASSERTION.

**Em uma frase:** o repositório guarda o código das cenas dos vídeos explicativos do canal 3Blue1Brown, quase todas feitas no Manim, e o README descreve o fluxo de trabalho do autor.

| Ponto | O que a fonte diz |
|---|---|
| O que é | o código que gera os vídeos de matemática do 3Blue1Brown, quase tudo cenas do Manim (a versão do autor, não a da comunidade) |
| Projetos antigos | podem depender de versões antigas do Manim e não rodar de imediato |
| Fluxo do autor | `manimgl <arquivo> <cena> -se <linha>` abre um modo interativo naquela linha; `checkpoint_paste()` roda o trecho copiado, volta ao estado salvo a cada trecho que começa com o mesmo comentário, e tem os modos `skip` (sem animar) e `record` (grava em arquivo) |
| Editor | atalhos para o Sublime com o Terminus; dá para imitar em outro editor |
| Instalação | o `manimgl` a partir do código-fonte, porque o publicado está desatualizado, e LaTeX |

**Lacuna:** não diz quantos vídeos, nem requisito de máquina.

**Conferência lado a lado:** 6 de 7 unidades seguem frases da fonte na ordem dela (a frase de abertura e as cinco células de texto corrido; a lacuna é nossa). É README técnico, em inglês, com a ficha em português: o `parafrase.py` não mede tradução, e a conta é esta.
