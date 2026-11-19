# Fábrica de criativos de anúncio a partir de uma URL

O fluxo de um agente "fábrica de criativos", que parte da URL de um produto e devolve variações de anúncio, estudado para construir em vez de usar pronto. Fonte: *We tested Meta's Advantage+ Creative in 50 campaigns: here's what actually moved the needle*, de Drew Madore (Synergist Digital Media), DEV Community, https://dev.to/synergistdigitalmedia/we-tested-metas-advantage-creative-in-50-campaigns-heres-what-actually-moved-the-needle-4mle; o resto é citação. Sínteses que já cobrem parte do fluxo: [[modelos-de-video-api]] (vídeo por API) e [[nano-banana-imagens-prompt]] (imagem).

## O fluxo que as fontes repetem

1. **A URL vira um resumo estruturado do produto** (nome, benefícios, provas, objeções, público, alegações permitidas e as que precisam de prova, imagens), guardado como dado e não como texto solto.
2. **Uma matriz de variações:** ganchos por formato (problema e solução, depoimento, demonstração, antes e depois, comparação), em vez de um roteiro só.
3. **Geração de imagem e vídeo** para cada célula da matriz.
4. **Checagem e aprovação humana:** alegações, marca, linguagem regulada.
5. **Lançamento** e **métricas** que alimentam a próxima leva.

É consenso entre fornecedores (Creatify, Higgsfield, Arcads, Topview, Zeely), que comparam os próprios produtos; nenhum publica estudo.

## O que se mediu

O relato mais concreto é de um praticante, com 50 campanhas e cerca de 2,1 milhões de dólares: o criativo automático do Meta reduziu o custo por conversão em 23% em média, com 4 campanhas piorando. Ajudou com **muitos conceitos diferentes** (uma loja foi de 11% de ganho com 5 imagens para 47% com 15 conceitos), com gancho visual em vídeo e com texto livre dentro de regras de marca. Atrapalhou quando mexeu em foto de marca de luxo, quando simplificou termo técnico em B2B, e quando havia só três imagens de entrada.

Do próprio Meta, só por matérias (a página oficial não abriu): num beta, quem gerou a maior parte dos anúncios em vídeo com IA teve em média 10% mais cliques e 8% mais conversão; a geração de vídeo a partir de imagem estática no Advantage+ ficou disponível para todos em 06/10/2026. Números de agência ("67% melhor retorno", "73% dos criativos vencedores") não têm método publicado.

## Regras que saem daqui

- **Variedade de conceito vale mais que variação de detalhe:** a matriz precisa de ângulos diferentes, não de dez versões do mesmo.
- **Travar o que é da marca** (logo, alegações, linguagem regulada) e deixar o resto livre; revisar as variações em lote, toda semana.
- **A aprovação humana fica**, porque o que a máquina não confere (alegação sem prova, linguagem regulada, tom da marca) é o que mais custa errar num anúncio.

## O que um projeto precisa para montar a fábrica

Imagem já existe no projeto (skill `image-gen`), e a coleta de métricas pode vir da API do Instagram; publicação e campanha de anúncio pedem uma ferramenta própria (o MCP de anúncios da Meta, por exemplo); vídeo por API está pesquisado em [[modelos-de-video-api]]. Faltam o primeiro passo (URL para resumo estruturado) e a matriz de variações, que são o trecho a construir.

## Não verificado

Os números do Meta (matérias, não a fonte); as capacidades dos fornecedores (páginas de marketing deles); o relato das 50 campanhas é de um único praticante, sem dados abertos.
