---
titulo: "Recorder package | Recorder | 5.1.8"
tipo: artigo
autor: "Unity Technologies (documentação oficial)"   # a página não tem assinatura; o rodapé diz 'Copyright © 2026 Unity Technologies'
url: "https://docs.unity3d.com/Packages/com.unity.recorder@5.1/manual/index.html"
publicado_em: null   # a página não traz data; a meta generator diz que o HTML foi gerado pelo docfx em "Wednesday, November 11, 2026"
capturado_em: 2026-11-12
licenca: "protegido (rodapé: 'Copyright © 2026 Unity Technologies', com link para 'Trademarks and terms of use'); sem licença de conteúdo declarada no texto lido; nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unity, video-capture, image-sequence, command-line, motion-blur, path-tracing, aov]
---

# Unity Recorder 5.1: o que o pacote grava, e só dentro do Editor

Nota de fato: tabelas do que a página de entrada do manual registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Página de entrada do manual do pacote Recorder da Unity, https://docs.unity3d.com/Packages/com.unity.recorder@5.1/manual/index.html, baixada em HTML em 12/11/2026 e lida no texto extraído, conferido no HTML (título e metas); sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco principal do HTML, não do arquivo); Wayback http://web.archive.org/web/20261002001844/https://docs.unity3d.com/Packages/com.unity.recorder@5.1/manual/index.html. Título conferido no `<title>`: o endereço pede a linha 5.1, e a página servida é a da versão 5.1.8. Lida a página inteira (a nota de instalação, a lista do que o pacote grava, o aviso e a tabela das seções do manual); nenhuma das seções ligadas foi aberta.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (o que se grava, a saída, o resumo curto de cada seção) fica fora. Resultado: 1 de 11 unidades segue a fonte, a frase da recomendação, que junta a nota de instalação, o aviso e três seções vizinhas da tabela; a maior sequência seguida que segue a fonte tem 1 unidade, e as duas citações estão à parte. O `parafrase.py` saiu com o código 3 contra o texto extraído da página (`unity-recorder-manual.txt`), com 11 unidades medidas (11 de prosa, 0 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas.

## Em uma frase

Página de entrada do manual oficial do Recorder, pacote da própria Unity, que lista o que ele grava no modo Play do Editor e aponta as seções do manual; para a base, é o mapa do que existe (vídeo, sequência de imagens, acumulação, AOV, linha de comando) antes de abrir cada seção.

## O pacote

| Item | Fato |
|---|---|
| Pacote | `com.unity.recorder` |
| Versão da página | 5.1.8 |
| Instalação | à parte do Editor da Unity |
| Quando grava | no modo Play |
| Onde funciona | só no Unity Editor, em Play |
| Player avulso ou build | não funciona |

## O que grava

| Captura | Saída |
|---|---|
| Jogo ou cinemática | arquivo de vídeo |
| Jogo ou cinemática | GIF animado |
| Jogo ou cinemática | sequência de imagens separadas |
| Subquadros acumulados | desfoque de movimento nos quadros finais |
| Subquadros acumulados | convergência do path tracing nos quadros finais |
| Passes de render AOV da cena | EXR de várias partes, para composição |
| Movimento de personagem ou câmera | arquivo de animação |
| Áudio do modo Play | arquivo WAV separado |

## As seções do manual, pela tabela da página

| Seção | O que a página diz que ela traz |
|---|---|
| Installation | instalar o pacote |
| Recorder concepts and features | tipos de recorder; API para estender |
| Get started | vários recorders juntos, ou disparo pela Timeline |
| Record videos and image sequences | exemplos: MP4 Full HD; GIF animado; sequência de imagens em sRGB linear |
| Record with Accumulation | gravação com acumulação de subquadros |
| Record AOVs | gravação de AOV para composição |
| Launch recordings from the command line | gravação em lote, por fila |
| Recorder types and properties | todas as propriedades: sessão, entrada, saída |
| Samples | exemplos; entre eles, FFmpeg como codificador |
| Known issues and troubleshooting | problemas e limites conhecidos; ferramentas de depuração |

## O que a fonte recomenda

O pacote se instala à parte e grava dentro do Editor, com o projeto em Play: para vídeo ou imagens, a página manda às seções de exemplos, de acumulação e de AOV, e para gravar muitas tomadas sem a mão de alguém, à seção da linha de comando, que monta uma fila de chamadas.

## Citações

- "The Recorder is designed to work only in the Unity Editor in Play mode. It does not work in standalone Unity Players or builds."
- "Use this setup to enable batch recording via a job queue of many command lines targeting different recordings."

## Lacuna

A página de entrada não diz com que versões da Unity o Recorder 5.1 funciona, qual a licença do pacote, quais formatos e codecs de vídeo existem além do MP4 do exemplo, nem os limites de resolução e de taxa de quadros. Não diz se a gravação pela linha de comando roda sem janela ou sem placa de vídeo, e as seções ligadas, que não foram abertas, ficam fora desta nota.
