---
titulo: "Godot Engine documentation: Creating movies"
tipo: artigo
autor: "Juan Linietsky, Ariel Manzur e a comunidade Godot (documentação do Godot)"
url: "https://docs.godotengine.org/en/stable/tutorials/animation/creating_movies.html"
publicado_em: null   # a página (versão stable) não traz data
capturado_em: 2026-11-12
licenca: "CC BY 3.0 (rodapé: '© Copyright 2014-present Juan Linietsky, Ariel Manzur and the Godot community (CC BY 3.0).'); o integral está na url"
areas: [generative-media]
tags: [godot, offline-rendering, movie-maker, command-line, image-sequence, ffmpeg, motion-blur, video-as-code]
---

# Godot: o Movie Maker, gravação fora do tempo real de qualquer projeto 2D ou 3D

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Página "Creating movies" da documentação do Godot (ramo stable, em inglês; a busca da rodada a trouxe em outras línguas), https://docs.godotengine.org/en/stable/tutorials/animation/creating_movies.html, baixada com curl em 2026-11-12. Lida inteira, menos as notas de usuários do fim da página. A licença do motor (MIT, segundo as respostas da rodada) não está nesta página e não foi lida.

## O que é

- **Gravação fora do tempo real:** o Godot grava vídeo e áudio de qualquer projeto 2D ou 3D sem tempo real; a página lista trailer, cena pré-gravada, animação procedural ou motion design (com interação e áudio durante a gravação, sem ouvir o som) e comparação de ajustes gráficos.
- **Vantagens que a página dá:** qualquer ajuste gráfico, sem depender da máquina, com ritmo de quadros perfeito; resolução acima da tela; taxa de quadros acima da final, para gerar desfoque de movimento depois.
- **Contra o Blender, pela página:** quem já usa o Godot pode ser mais produtivo nele do que no Blender para render de vídeo, mas motores feitos para render fora do tempo real, como Cycles e Eevee, podem dar visual melhor, com render mais longo.
- **O que não é:** não serve para capturar partida jogada em tempo real; para isso, a página manda usar OBS Studio ou SimpleScreenRecorder.

## Como se liga e como se roda

| Ponto | O que a página diz |
|---|---|
| No editor | o botão de rolo de filme no canto superior direito; o estado não persiste ao fechar o editor; trocar com o projeto rodando só vale ao reiniciar |
| Caminho da saída | nas configurações do projeto, ou por cena, com um metadado `movie_file` no nó raiz |
| Linha de comando | `godot --path /path/to/your_project --write-movie output.avi`; caminho relativo é relativo à pasta do projeto |
| Resolução | sai do tamanho da janela (nos modos de esticar `disabled` e `canvas_items`); `--resolution 1280x720` muda na partida, limitada à resolução da tela; com o modo `viewport`, manda a resolução do viewport, que pode passar da tela |
| Quadros por segundo | `--fixed-fps 30` |
| Projeto exportado | `--write-movie` e `--fixed-fps` funcionam também nele |
| Parar | pelo X da janela, por `get_tree().quit()`, por `--quit-after N` quadros, ou pela opção do AnimationPlayer que fecha o Godot quando a animação principal acaba; interromper com F8 ou Ctrl+C deixa o AVI e o WAV sem a duração |

## Formatos de saída

| Formato | Vídeo e áudio | Notas da página |
|---|---|---|
| OGV (recomendado) | Theora e Vorbis | equilíbrio de tamanho e velocidade, imagem melhor que o MJPEG; não abre em navegador; sem transparência; só se grava em build de editor |
| AVI | MJPEG e áudio sem compressão | arquivo médio, codificação rápida; precisa ser convertido para a web; sem transparência; até 4 GB |
| PNG | sequência de PNG e um WAV | sem perda, arquivos grandes e lentos; aceita transparência (com o fundo transparente ligado no projeto); oito dígitos no nome de cada quadro |
| Próprio | estendendo a classe `MovieWriter` | em geral por GDExtension |

## Configuração, qualidade e pós-produção

- **Ajustes do Movie Writer:** taxa de mistura do áudio (divisível pelo FPS gravado, para não perder a sincronia), modo de alto-falantes, qualidade do vídeo (0,01 a 1; recomendado 0,75 a 0,9), FPS (as plataformas em geral não passam de 60), qualidade e velocidade do OGV e intervalo de quadros-chave.
- **Ajustes só na gravação:** a etiqueta de recurso `movie` sobrescreve configurações do projeto e pode ser consultada em script, para ligar qualidade que não roda em tempo real (o exemplo melhora o SDFGI). Para 3D, a escala de render acima de 1 dá antisserrilhado por supersampling sem aumentar o arquivo.
- **Com o FFmpeg:** AVI ou OGV para MP4 com CRF 15; PNG e WAV para MP4 com `-r` igual ao FPS gravado, ou para WebM VP9 se houver transparência; cortar, redimensionar, reduzir quadros; e desfoque de movimento por acúmulo, gravando num múltiplo do FPS e misturando os quadros (exemplo: 240 fps, `tmix=frames=4`, saída a 60 fps), já que o Godot não tem desfoque de movimento próprio.

## Citações

- "Godot can record non-real-time video and audio from any 2D or 3D project."
- "This feature is not designed for capturing real-time footage during gameplay."

## Lacuna

A página não dá tempos de gravação, não diz se o Movie Maker roda sem tela (sem janela) nem como se comporta no Windows sem monitor; não fala de licença.
