---
titulo: "Image to video and keyframes — Seedance 2.5 | Runware Docs"
tipo: artigo
autor: "Runware (documentação do agregador)"
url: "https://runware.ai/docs/models/bytedance-seedance-2-5/guides/image-to-video.md"
capturado_em: 2026-11-11
licenca: "protegida: o Markdown da documentação da Runware não declara licença (valem os termos do site); ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [seedance, runware, aggregator, image-to-video, first-last-frame, seamless-loop, keyframes]
---

# Runware: imagem para vídeo, primeiro e último quadro e laço com o Seedance 2.5

Ficha de estudo do guia da Runware sobre animar imagens paradas com o Seedance 2.5. Fonte curta (uma página de guia): organizada pelo que serve a quem vai fazer a chamada (como a imagem entra, as regras, o que pôr no prompt em cada modo, o laço em detalhe, o que a página não diz), e não pela ordem da página.

**Proveniência.** Versão Markdown da página, baixada em 11/11/2026, 258 linhas, . O cabeçalho do arquivo dá como endereço da página https://runware.ai/docs/models/bytedance-seedance-2-5/guides/image-to-video (sem o `.md`). A página não traz data de publicação nem de atualização. Os vídeos de exemplo não foram vistos, só as legendas e os prompts. **Cobertura:** a página inteira (introdução, formato do pedido, os quatro modos e as dicas finais), com os exemplos de código em TypeScript, Python, cURL, CLI e JSON lidos para os parâmetros.

**Quem fala.** A Runware, que revende o acesso ao modelo da ByteDance pela própria API: as regras e os nomes de parâmetro são os da interface dela, e as recomendações de prompt são dela.

## Como a imagem entra

- O modelo se chama `bytedance:seedance@2.5`; a tarefa é `videoInference`, no endpoint `https://api.runware.ai/v1`, com a chave em `Authorization: Bearer`.
- As imagens vão em `inputs.frameImages`, uma lista em que cada item diz a imagem (`image`, por URL) e o lugar dela no vídeo (`frame`: `first` ou `last`).
- O exemplo do pedido usa `resolution: '720p'`, `duration: 5` e `deliveryMethod: 'async'`, além do prompt em `positivePrompt`.

## As regras do `frameImages`

| Pergunta | Resposta da página |
|---|---|
| O que é obrigatório? | um item `first`; com ele só, o vídeo parte da imagem |
| O que é opcional? | um item `last`, o segundo e último possível; com os dois, o modelo preenche o caminho de um ao outro |
| O que a API recusa? | `last` sem `first`; `width` e `height`; misturar `frameImages` com `referenceImages`, `referenceVideos` ou `inputs.video` na mesma chamada |
| O que vem da imagem? | o tamanho e a proporção da saída, tirados do primeiro quadro; da chamada, só a faixa de `resolution`, que a página dá como 480p ou 720p |
| E se as duas imagens tiverem tamanhos diferentes? | o último quadro é esticado para caber; a página pede dimensões iguais |
| E para mais de dois pontos de passagem? | outro caminho: as imagens em `inputs.referenceImages` (até 30) e o prompt mandando lê-las como quadros-chave |

## O que pôr no prompt, modo a modo

| Modo | Entrada | O que o prompt deve dizer | Quando falha, segundo a página |
|---|---|---|---|
| Um quadro só | uma imagem como `first` | só o que se mexe, em que direção, e uma única ação do sujeito; descrever a cena de novo concorre com a imagem | a página não dá caso de falha; recomenda aprovar primeiro a imagem e só depois animar |
| Primeiro e último quadro | duas imagens da mesma cena, mudando uma coisa (no exemplo, a luz da manhã e a da tarde sobre o mesmo frasco) | a passagem de uma à outra como um plano contínuo | duas imagens sem relação deixam o caminho longo demais, e o movimento vira um morph |
| Laço | a mesma imagem como `first` e como `last` | o nome do laço ("end on the exact starting frame") e um movimento que sai e volta | sem câmera e luz fixas, a emenda aparece |
| Quadros-chave | várias imagens em `inputs.referenceImages` | abrir com "Use Images 1 to N in order as keyframes", com as imagens num estilo só | os quadros guiam sem fixar: o modelo se aproxima de cada imagem em vez de travar nela, e num clipe curto cabem poucas antes de cada etapa ficar curta demais |

Para um roteiro mais solto, em que as imagens são um painel de clima e não uma sequência estrita, a página sugere contar a história no prompt e usar uma única imagem de storyboard com poucos quadros e traço simples.

## O laço, em detalhe

**A técnica.** Com a mesma imagem nas duas pontas, o modelo gera um movimento "that departs and returns, so the clip ends exactly where it began and plays as a seam-free loop". Não há parâmetro próprio de laço na página: o laço sai da repetição da imagem e do prompt.

**O movimento que a página recomenda.** O que já é cíclico, como uma rotação completa ou um deslocamento lento de ida e volta, para que a volta pareça movimento e não um vídeo rebobinado.

**O exemplo.** Um relógio de pulso num suporte dá uma volta de 360 graus e termina no mesmo ângulo, posição e enquadramento do início. O prompt pede começo e fim no mesmo quadro, luz, suporte, fundo e enquadramento constantes, uma rotação contínua, e termina em "Silent".

**Para que a página diz servir.** Um giro de produto em laço para um anúncio de loja, ou um fundo ambiente para um site ou uma transmissão.

## O que a página não diz

- Data, preço, duração máxima e mínima, proporções aceitas e taxa de quadros.
- Se há 1080p (a página só fala nas faixas de 480p e 720p) e como se pede áudio: os prompts trazem uma linha "Audio:" (ou "Silent"), mas nenhum parâmetro de áudio aparece no código.
- Se o laço fecha sem emenda em todos os casos, ou com que frequência a emenda aparece: o exemplo é um só.
- O que acontece quando a imagem tem o rosto de uma pessoa real; o único exemplo com pessoa (a mulher no trigal, vista de costas, que vira a cabeça) parte de uma imagem gerada num modelo de imagem, segundo a própria página.
