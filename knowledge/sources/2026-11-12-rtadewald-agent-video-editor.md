---
titulo: "rtadewald/agent-video-editor: o Claude Code como editor de vídeo, com revisão por blocos num app local (README)"
tipo: artigo
autor: "Rodrigo Tadewald (usuário rtadewald no GitHub; nome no perfil: Rodrigo Soares Tadewald)"
url: "https://github.com/rtadewald/agent-video-editor"
publicado_em: 2026-10-29   # último commit que mudou o README.md (744082024e, 01:31 UTC); o repositório teve push até 09/11/2026
capturado_em: 2026-11-12
licenca: "protegida: repositório público sem arquivo de licença (gh api repos/rtadewald/agent-video-editor: license null em 2026-11-12), logo todos os direitos reservados. Nota de fato do método, sem trechos de código"
areas: [generative-media]
tags: [agent-video-editor, video-editing, claude-code-skills, word-level-transcript, review-by-blocks, creator-calibration, learnings-loop, short-form-video, cta-variants, elevenlabs, openrouter]
---

# agent-video-editor: o Claude Code edita o vídeo bruto e o criador revisa por blocos (Rodrigo Tadewald, README de 29/10/2026)

Nota de fato: tabelas do que o README fixa, os passos numa lista quando a ordem é o método, e prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Sem trechos de código: o repositório não tem licença.

**Proveniência.** O `README.md` do repositório público `rtadewald/agent-video-editor`, baixado em 12/11/2026. Conferido com `gh api` (só leitura) em 12/11/2026: o hash git do arquivo baixado é o do `main` (`62ca640fa8`), e o último commit que mudou o README é o `744082024e`, de 29/10/2026. As skills (`.claude/skills/editor/`, `publicar/`), o `edicao.md`, os scripts, o app e o vídeo de demonstração não foram lidos; aparecem só pelo nome que o README dá.

**Estado do repositório** (gh api, 12/11/2026): criado em 11/10/2026, último push em 09/11/2026, 11 estrelas, sem licença. O antecessor do mesmo autor, `rtadewald/harness-video-editor` (04 a 15/10/2026), não entra nesta ficha.

**Quem fala.** O autor do repositório. O nome vem do perfil do GitHub, que o descreve como sócio fundador da Asimov Academy (parte interessada: a escola vende cursos sobre o tema).

**Licença.** Sem arquivo de licença (`license: null`): todos os direitos reservados. A ficha descreve o método; nomes de pasta, de página, de script e os valores aparecem como estão.

**Cobertura.** O README inteiro.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato fica fora. Corpo: 6 frases de prosa fora da proveniência, uma lista de 9 passos (na ordem do README, porque a ordem é o método, em palavras próprias) e 9 células com texto corrido em 9 tabelas; as demais células são fatos curtos (nome, lista, valor). Resultado: 0 das 6 frases e 3 das 9 células seguem uma frase da fonte (quem decide a edição, onde se faz o pedido e o CTA gravado à parte, fatos que levam as palavras da fonte), as mesmas três que o `parafrase.py` aponta; a primeira versão desta ficha, com as tabelas copiando as descrições do README, dava 26 de 46 unidades coladas no `parafrase.py` e foi reescrita. As três citações estão à parte.

## Em uma frase

Editor de vídeo curto em que o Claude Code faz a edição inteira do bruto, cada decisão presa às palavras da transcrição, o criador revisa num app local por blocos de cerca de 30 segundos, e cada vídeo aprovado deixa aprendizados por categoria que o editor lê no vídeo seguinte.

## Entrada, saída e peças

| Item | Fato |
|---|---|
| Entrada | o bruto, com briefing opcional |
| Saída | o vídeo editado inteiro, em 9:16 |
| Camadas da edição | cortes, look, direção visual, inserts, motions, transições, áudio, legenda |
| Exportação | 4K, depois de aprovado |
| Publicação | Google Drive, Notion, Obsidian, Metricool, ManyChat |
| Skills | `editor` (do bruto ao aprovado) e `publicar` (do aprovado ao ar) |
| Decisão editorial | do Claude, a partir dos exemplos que o criador deu |
| Papel dos scripts | conferir, calcular tempo, renderizar |
| Âncora de toda edição | o ID de cada palavra da transcrição; nunca o segundo |
| Onde está o contrato | `edicao.md`, na skill `editor` |
| Como se pede | no Claude Code, na pasta do projeto, com o caminho do bruto |
| Requisitos | `uv`, `ffmpeg`, Claude Code |
| Chaves | OpenRouter e ElevenLabs, num `.env` fora do git |
| App | `ferramentas/servidor.py`, porta 8719 |

## O caminho de um vídeo

1. Material preparado: texto com tempo por palavra, cópia leve, rosto achado, voz tratada.
2. Cortes.
3. Roteiro dirigido, um plano de cada vez.
4. Cinco frentes ao mesmo tempo (inserts, motions, áudio, legenda, transições), com subagentes para o insert e o motion que ainda não existem.
5. Enriquecimento.
6. Render e conferência pelo próprio agente; a primeira versão sai sem pausa.
7. Rodada de revisão: comentário no app, aviso no chat, e o agente aplica tudo o que está pendente, gera a versão e responde a cada um em uma linha.
8. Aprovação e export em 4K.
9. Fechamento: o agente explica a causa de cada correção, o criador confirma quais viram aprendizado, e eles passam a ser lidos antes de cada etapa dos próximos vídeos.

## A revisão por blocos

| Item | Fato |
|---|---|
| Tamanho do bloco | perto de 30 s, mínimo de 15 s |
| Vídeo curto | um bloco só |
| Corte entre blocos | troca de plano |
| Identidade do bloco | presa às palavras, logo estável entre versões |
| O que o painel mostra | só o bloco escolhido, com o histórico de pedidos e respostas dele |
| Botão Finalizar | bloco travado contra novas mudanças do agente |
| Botão Aprovar | o vídeo fechado |
| Indicador no topo | porcentagem concluída |
| Versão | por bloco; sobe só quando ele muda |
| Sinais visuais | estrela no bloco mudado e não visto; carga onde o agente trabalha |
| Pendentes | os de qualquer versão vão para a próxima, mesmo comentados durante outra refação |
| Onde se comenta | no instante do vídeo, com print ou vídeo colado |

## Um corpo, várias saídas

| Item | Fato |
|---|---|
| Projeto | um corpo e várias saídas |
| Saída | corpo mais final, batizada pelo destino (ex.: ManyChat, LP, VSL) |
| Final falado | achado pelo agente no próprio bruto |
| Final gravado à parte | um CTA de outro projeto (há CTAs coringa, que servem a vários vídeos), acrescentado pelo app ou pelo chat |
| Sem final | o corpo puro |
| Comentário no Final | vale só para a saída dele; no CTA, cai no projeto do CTA |
| Áudio com CTA à parte | mixagem única, CTA igualado ao corpo, trilha contínua |
| Arquivo | `final/saidas/<nome> - <destino>.mp4` |

## As páginas do app

| Página | Objeto |
|---|---|
| Projetos e CTAs | os vídeos, em edição ou aprovados |
| Revisão | player, linha do tempo, comentários, provador de look |
| Banco | mídias de insert, com selos |
| Motions | animações HTML e GSAP |
| Referências | os planos da Calibragem |
| Presets e Transições | receitas, original ao lado da recriação |
| Áudio | trilhas e sons |
| Calibragem | vídeos de referência analisados |
| Heurística | regras do criador, por categoria |
| Aprendizados | correções promovidas a regra |
| Lixeira | o apagado, restaurável |

| Categoria (quadro) | Fato |
|---|---|
| Exemplos | Storytelling Projects, Hacks & Tips, Pico, Ad VSL, CTA, VSL |
| Próprio de cada uma | Calibragem, Heurística, aprendizados |
| Efeito | cada vídeo é dirigido pelo que a categoria dele acumulou |

## Pastas e comandos

| Pasta | Conteúdo |
|---|---|
| `.claude/skills/` | `editor/` e `publicar/`; `editor/etapas/` tem um arquivo por etapa |
| `ferramentas/` | scripts PEP 723, um por etapa, e o servidor |
| `render/` | a página de render das camadas gráficas |
| `app/` | o app de revisão, sem build |
| `biblioteca/` | o acervo do criador, fora do git |
| `projetos/` | uma pasta por vídeo, fora do git |

| Script (`ferramentas/`) | Uso |
|---|---|
| `revisao.py` | pendências, leitura, histórico, encerramento |
| `render.py` | versão nova, incremental |
| `render.py --final`, `--saidas` | final 4K; saídas |
| `cortes.py saidas` | as saídas do projeto |
| `servidor.py --limpar-caches 3` | limpeza de cache de aprovados parados (também automática, por hora) |
| `codigo.py` | o que é um código citado no chat |

Para mudar de máquina, a `biblioteca/` é substituída inteira, com o servidor parado, e o que só existia no destino some; uma instalação sem ela começa com uma biblioteca mínima.

## O que a fonte recomenda

Ancorar toda a edição nas palavras e não no relógio, para que corte, bloco e comentário sobrevivam de uma versão à outra, e dar ao criador a revisão em pedaços que se travam um a um. O gosto do criador entra por exemplos e regras por categoria, e cada vídeo aprovado devolve à biblioteca as correções que ele confirmou.

## Citações

- "Tudo fica preso às palavras da transcrição (IDs), nunca a segundos"
- "As decisões editoriais são do Claude, guiadas pelos exemplos do criador"
- "Finalizar trava o bloco (o Claude não mexe mais nele)"

## Lacuna

O README não diz que modelos fazem o corte, a direção e a análise das referências, nem quanto custa ou quanto tempo leva um vídeo; não diz como os motions viram imagem no render, só que uma página os desenha; não mostra o formato do contrato de edição nem o dos aprendizados, que estão no `edicao.md` e na biblioteca, não lidos. O demo de 1 minuto não foi visto.
