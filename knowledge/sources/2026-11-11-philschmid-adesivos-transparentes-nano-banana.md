---
titulo: "Transparent PNG Stickers with Nano Banana Pro and Gemini interactions API"
tipo: artigo
autor: "Philipp Schmid"
url: "https://www.philschmid.de/generate-stickers"
publicado_em: 2026-01-19   # "January 19, 2026" na página; datePublished e dateModified 2026-01-19 no JSON-LD
capturado_em: 2026-11-11
licenca: "protegido ('Philipp Schmid © 2026' no rodapé; sem licença de conteúdo declarada no texto lido; o post liga para o notebook no GitHub, philschmid/gemini-samples, e o texto lido não diz a licença dele); ficha em palavras próprias e em estrutura própria, sem o integral"
areas: [generative-media, content-design]
tags: [image-generation, nano-banana, gemini, transparency, chroma-key, hsv, stickers]
---

# Philipp Schmid: adesivo de fundo transparente com Nano Banana Pro e chroma key

**Proveniência.** Post do site de Philipp Schmid, https://www.philschmid.de/generate-stickers, baixado com curl em 2026-11-11, com o texto extraído do HTML (Wayback: http://web.archive.org/web/20260716193705/https://www.philschmid.de/generate-stickers). Autor pelo `meta author`, pelo JSON-LD e pelo rodapé; data na página ("January 19, 2026", "9 minute read") e no JSON-LD. O post liga para o notebook no GitHub (`philschmid/gemini-samples`, `examples/interactions-generate-stickers.ipynb`), que não foi aberto. Lido inteiro o texto, com todo o código mostrado; as imagens dos exemplos (o verde cru e o recorte) não foram vistas.

**Conferência lado a lado** (2026-11-11): unidade é a frase fora de tabela ou a célula preenchida de tabela, contadas só no corpo (fora a proveniência e esta linha), e uma unidade segue a fonte quando traduz uma frase dela, ou duas vizinhas, na ordem delas. Resultado: 7 de 33 unidades da ficha seguem uma frase da fonte (7 de 20 sem contar as células que só trazem um rótulo ou uma lista de valores; contando como "segue" toda unidade que traz uma citação literal: são 2). Uma primeira versão, com uma linha de tabela por requisito do prompt e por parâmetro, dava 25 de 59, porque cada célula traduzia uma linha do prompt ou um comentário do código; as tabelas foram refeitas para cada célula juntar o prompt com as dicas e com a comparação, e cada etapa do recorte com todos os seus parâmetros. O post é um notebook comentado, na ordem do código (dependências, funções auxiliares, geração, montagem, exemplos, dicas); a ficha junta o prompt, as dicas de prompt e a comparação numa tabela só, junta as três funções de recorte e a chamada que as usa noutra, com os valores efetivamente usados ao lado dos padrões, e separa o que ficou desligado e o que o post não mede. A medida acima não contou como "segue" a unidade que funde três ou mais frases seguidas da fonte, na ordem dela, ponto cego apontado na revisão do Passo 7 (11/11/2026); o número pode estar baixo, e esta ficha não foi medida de novo.

## A aposta

O problema que o post ataca é o fundo transparente limpo para uso real (adesivo, sobreposição, impressão sob demanda), e a resposta é não pedir transparência ao modelo nem chamar um segundo modelo para tirar o fundo: gera-se o sujeito sobre verde de chroma key e o verde sai por código, no espaço de cor HSV. Na comparação que o autor faz com a remoção de fundo por modelo, o chroma key ganha em tudo o que ele lista (sem chamada extra, mais rápido, mais barato, mais previsível, e com borda que ele chama de excelente graças ao contorno branco, contra a borda irregular do modelo), e a regra que fecha a comparação é: "When you control generation, prompting for a specific background color beats running another model."

## O pedido ao modelo

O prompt embrulha a descrição do usuário em "Create a sticker illustration of", seguido de requisitos numerados, e a lista de dicas no fim do post repete quase todos.

| Requisito | O que o prompt pede, e o que o post diz a respeito |
|---|---|
| Fundo | verde de chroma key exatamente `#00FF00` (RGB 0, 255, 0), um tom só, sem variação, gradiente, sombra ou efeito de luz; nas dicas, a cor do fundo vem sempre dita explicitamente |
| Contorno branco | de 2 a 3 pixels entre o sujeito e o verde, para a cor não vazar de um para o outro; é a ele que o autor credita a borda excelente na comparação com a remoção por modelo, e é por ele que a remoção agressiva vem com `edge_pixels` em 0 |
| Verde no sujeito | proibido, para não se confundir com o chroma key, e trocado por um tom bem distinto, como verde-floresta escuro ou azul-petróleo, quando o sujeito precisa de verde (folhas); nas dicas, o método funciona melhor com sujeito sem verde |
| Borda | nítida e bem definida, nada suave ou borrado, e nas dicas a expressão a usar é "clear defined edges", para facilitar o recorte |
| Enquadramento | sujeito centralizado e com folga em todos os lados, pedido tanto no prompt quanto nas dicas |
| Estilo | adesivo de cartum ou ilustração, vibrante, limpo, de cores fortes, com "sticker-style" ou "illustration" sempre escrito, segundo as dicas |
| Finalidade | o prompt avisa ao modelo que o verde será removido por programa |

Imagens de referência entram antes do texto, cada uma como bloco de conteúdo (tipo imagem, dados em base64, tipo MIME tirado da extensão e JPEG quando ela é desconhecida); o segundo exemplo do post usa uma foto do autor e o novo logotipo do Google DeepMind para gerar um desenvolvedor parecido com ele, de moletom da DeepMind, e o primeiro, só texto, um gato feliz de olhos grandes. A chamada é `client.interactions.create` da Interactions API do Gemini, com o modelo `gemini-3-pro-image-preview`, que o post chama de "Gemini Pro 3 Image Preview (Nano Banana Pro)", e `generation_config.image_config` com proporção `1:1` e tamanho `2K` por padrão (comentado no código como resolução maior para borda melhor); da resposta se toma a primeira saída do tipo imagem, e sem ela a função levanta erro. Para rodar, o post pede `google-genai`, `pillow` e `scipy` e a variável `GEMINI_API_KEY`.

## O recorte

| Etapa | Valores na montagem final (padrão da função) | Como funciona, segundo o código e os comentários |
|---|---|---|
| Verde por HSV | matiz 120 com faixa de 25, saturação acima de 75 e valor acima de 70 (matiz em graus, saturação e valor de 0 a 100), dilatação 2, erosão 0, todos iguais ao padrão | converte RGB em HSV, mede a distância ao matiz 120 dando a volta no círculo e marca como verde o pixel dentro da faixa e acima dos dois mínimos; os comentários justificam cada valor (o verde puro, a faixa estreita, só verde saturado para preservar o verde de logotipo, só verde claro), a dilatação estende a máscara aos pixels de borda suavizados e a erosão, opcional, tiraria ruído isolado |
| Limpeza de borda | limiar 64 (padrão 128) | alfa abaixo do limiar vira 0 e o resto vira 255, para tirar o halo da borda suavizada |
| Remoção agressiva | desligada (padrões: razão 1,2 e `edge_pixels` 0) | marca o pixel em que o verde domina, com G acima de 1,2 vez o maior entre R e B (somado 1 para não dividir por zero) e G maior que os outros dois, o que pega também verde escuro, verde claro e sombra esverdeada; o `edge_pixels` dilataria a máscara, e o padrão 0 evita comer o contorno branco |

O pixel que cai na máscara recebe alfa 0, e o resultado se grava como PNG em RGBA; há opção de gravar também a imagem crua, com `_raw` no nome, para depurar.

## O que ficou desligado, e o que o post não mede

A docstring da montagem descreve quatro passagens (prompt, verde por HSV, remoção agressiva, limpeza de borda), mas a terceira está comentada no código, com o motivo escrito ao lado: "Skip aggressive removal (disabled - causes speckles in subject)". As vantagens de velocidade, custo e previsibilidade sobre a remoção por modelo vêm afirmadas sem número, sem tempo nem preço por imagem, e a qualidade de borda se mostra só nos pares de imagem cru e recortado dos dois exemplos. Os usos listados para o PNG com canal alfa são programas de design (Figma, Photoshop), apresentações, aplicativos de conversa, impressão sob demanda e aplicativos de celular.
