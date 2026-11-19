---
titulo: "Nano Banana image generation (Gemini API): modelos, referências, resoluções e limites em novembro de 2026"
tipo: artigo
autor: "Google (documentação oficial da Gemini API)"
url: "https://ai.google.dev/gemini-api/docs/image-generation"
publicado_em: null   # a versão .md.txt lida não traz data de atualização
capturado_em: 2026-11-11
licenca: "em dúvida: a versão .md.txt baixada não traz o rodapé de licença do Google Developers; o HTML da página, baixado com curl em 11/11/2026, redireciona para aistudio.google.com/docs/image-generation, app em JavaScript, sem rodapé no que o curl devolve, e a cópia da Wayback, pedida na revisão do mesmo dia, devolveu 620 bytes, uma página de bloqueio por tráfego de robô; falta conferir no Chrome se o texto é CC BY 4.0. Tratada como protegida: ficha em palavras próprias, sem o integral"
areas: [content-design, generative-media]
tags: [nano-banana, image-generation, reference-images, character-consistency, style-reference, aspect-ratio, transparency, multi-turn]
---

# A página de geração de imagem da Gemini API em 11/11/2026

Ficha de estudo da página de geração de imagem (Nano Banana) da Gemini API, organizada por pergunta (qual modelo, quantas referências, que tamanho, o que a página não oferece), não pela ordem da página. Não há integral: a licença do texto lido está em dúvida. A versão de outubro da mesma página está em [[2026-10-23-gemini-api-geracao-de-imagem]].

**Proveniência.** Versão em markdown da página (`https://ai.google.dev/gemini-api/docs/image-generation.md.txt`), baixada com curl em 2026-11-11; cópia na Wayback de 31/10/2026: http://web.archive.org/web/20261031163411/https://ai.google.dev/gemini-api/docs/image-generation. **Cobertura:** lidos a escolha de modelo, o aviso de direitos, a edição em vários turnos, as funções do Nano Banana, a tabela das 14 referências, a busca de imagens, a geração a partir de vídeo, as resoluções, o exemplo de adesivo do guia de prompts, a transferência de estilo, os outros modos, o lote, as boas práticas, as limitações, o formato de saída e as tabelas de proporção e tamanho; os exemplos de código nas várias linguagens e os demais exemplos do guia de prompts não foram lidos um a um.

## Qual modelo

| Nome | Id | Como a página o descreve |
|---|---|---|
| Nano Banana 2.1 | `gemini-nano-banana-2.1` | atualização do Nano Banana 2 e o "cavalo de batalha" de geração e edição por conversa, com a velocidade e o custo da linha Flash e melhor qualidade visual, texto, consistência em vários turnos e busca, a 1K, 2K e 4K |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | o mais rápido e barato; "Not optimized for multiple reference inputs or multi-turn sequential editing" |
| Nano Banana 2 | `gemini-3.1-flash-image` | a geração anterior, otimizada para velocidade, 4K e consistência com várias referências; para projeto novo, a página recomenda o 2.1 |
| Nano Banana Pro | `gemini-3-pro-image` | o premium, que raciocina ("Thinking") para seguir instruções complexas, manter consistência de marca e renderizar texto com fidelidade, voltado à produção profissional |
| Nano Banana | `gemini-2.5-flash-image` | o legado da série; a migração recomendada é para o Lite |

Toda imagem gerada leva a marca d'água SynthID. Quem sobe imagem precisa ter os direitos sobre ela, sob a política de uso proibido do Google. O modo de pensamento gera "imagens de pensamento" intermediárias, que a página diz não serem cobradas, antes da saída final.

## Quantas referências e de que tipo

Até 14 imagens de referência por pedido, divididas assim pela tabela da página, que tem duas colunas:

| Referência | Nano Banana 2.1 e Nano Banana 2 | Nano Banana Pro |
|---|---|---|
| objetos em alta fidelidade | até 10 | até 6 |
| personagens com consistência | até 4 | até 5 |
| estilo | "N/A" | até 3 |

A seção de limitações repete: o 2.5 Flash Image funciona melhor com até 3 imagens de entrada; o Pro, 5 em alta fidelidade e até 14 no total; o 2.1 e o Nano Banana 2, a semelhança de até 4 personagens e a fidelidade de até 10 objetos num mesmo fluxo. A tabela lida não tem coluna do Lite (a ficha de 23/10, sobre a versão de outubro, registrava uma terceira coluna, casada pela ordem numa tabela que veio achatada). Para iterar sobre uma imagem, a página recomenda a conversa em vários turnos, e o exemplo segura o resto com a instrução "Do not change any other elements of the image."

Outras formas de referência: a busca de imagens do Google como contexto visual (só no 2.1 e no Nano Banana 2, e, nesses dois, sem fotos reais de pessoas tiradas da busca); a geração a partir de um vídeo como referência multimodal (só no 2.1, no Nano Banana 2 e no Lite; os exemplos são miniatura, pôster, infográfico); e o modelo de prompt de transferência de estilo, que pede para refazer o conteúdo de uma foto num estilo artístico nomeado, preservando a composição.

## Que tamanho e que proporção

- **Resolução:** os modelos Gemini 3 geram 1K por padrão e também 2K e 4K; o 512 px (0,5K) só no Nano Banana 2 ("not supported on Gemini Nano Banana 2.1"). O valor vai em `image_size`, com o K maiúsculo (o minúsculo é recusado).
- **Proporção:** sem indicação, a saída segue o tamanho da imagem de entrada ou sai quadrada; o 2.1 e o Nano Banana 2 acrescentam 1:4, 4:1, 1:8 e 8:1 às proporções comuns. Para o vertical 9:16, as tabelas dão 768×1376 a 1K, 1536×2752 a 2K e 3072×5504 a 4K, nos três modelos Gemini 3.
- **Tokens por imagem nas tabelas de tamanho:** no 2.1, 1.120 a 1K, 1.680 a 2K e 2.520 a 4K, em todas as proporções; no Nano Banana 2, 747, 1.120, 1.680 e 2.520 (de 0,5K a 4K); no Pro, 1.120 a 1K e a 2K e 2.000 a 4K.
- **Formato de saída:** por padrão o modelo devolve texto e imagem; só a imagem, pedindo o tipo imagem em `response_format`. O texto lido não fala de saída com canal alfa nem de fundo transparente.

## O que a página ensina sobre o prompt

- **O adesivo do guia de prompts** (ilustração estilizada): o prompt de exemplo descreve contorno forte e limpo, cel shading simples e paleta viva, e termina com "The background must be white."
- **Boas práticas:** ser muito específico; dizer o propósito da imagem; iterar por conversa com pedidos pequenos ("mantenha tudo igual, mas..."); dividir a cena complexa em passos (primeiro o fundo, depois o primeiro plano, por fim o objeto); descrever positivamente o que se quer em vez de negar ("rua vazia" em vez de "sem carros"); e controlar a câmera com a linguagem de foto e cinema (grande angular, macro, contra-plongée).
- **Limitações declaradas:** melhor desempenho em 15 idiomas, entre eles o pt-BR; não aceita áudio, e vídeo só no 2.1, no Nano Banana 2 e no Lite; nem sempre segue o número de imagens pedido; para texto na imagem, gerar primeiro o texto e depois pedir a imagem com ele.

## Os outros modos

O Imagen foi desligado e não está mais disponível pela Gemini API ("Use Nano Banana for image generation and editing"); para vídeo, a página remete ao guia do Veo. Tudo o que a página descreve roda também como tarefa em lote, pela Batch API.
