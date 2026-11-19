---
titulo: "Understanding WCAG 2.2, Success Criterion 1.4.3: Contrast (Minimum)"
tipo: artigo
autor: "W3C, Accessibility Guidelines Working Group (AG WG)"
url: "https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html"
publicado_em: 2026-09-06
capturado_em: 2026-10-29
licenca: "W3C Document License (rodapé: 'Copyright © 2026 World Wide Web Consortium. W3C® liability, trademark and permissive license rules apply'; a página 'Permission to Use WAI Material' diz que as diretrizes estão sob a W3C Document License, que permite copiar e distribuir o documento completo, sem modificar, com URL, copyright e status)"
areas: [content-design]
tags: [accessibility, wcag, contrast, large-text, type-size, legibility, images-of-text]
---

Ficha de estudo, para leitura e citação; o documento integral fica na url. É o texto explicativo do critério 1.4.3 (nível AA), informativo: o critério normativo é a frase da seção "Success Criterion". Página atualizada em 2026-09-06, segundo o rodapé. Lido em 2026-10-29, na pesquisa sobre o tamanho de texto legível numa imagem de 1080 px no celular.

## A regra

- Texto e imagem de texto: contraste de pelo menos **4,5:1** com o fundo.
- **Texto grande** ("large scale"): pelo menos **3:1**. Grande é 18 pt, ou 14 pt em negrito; em CSS, 1 pt = 1,333 px, então **24 px e cerca de 18,5 px**.
- Sem exigência: texto decorativo (palavras que poderiam trocar de lugar sem mudar o sentido), texto de componente inativo, texto incidental numa foto, logotipo.
- Os limites não se arredondam: 4,499:1 não passa.

## O que importa para imagem de texto

- O ponto do editor de imagem não é confiável, porque cada programa supõe uma densidade (72 ou 96 ppi). O que vale é o texto da imagem, **quando exibido**, equivaler a cerca de 1,2 em e 1,5 em do corpo padrão (120% e 150%).
- Tamanho é o da entrega, sem o zoom que a pessoa faça.
- Letra muito fina ou incomum lê pior, sobretudo com pouco contraste; a suavização de borda deixa a letra fina mais clara do que a cor declarada, e o documento recomenda letra de traço mais grosso ou contraste acima do mínimo.
- Imagem de texto pixeliza ao ampliar e não deixa a pessoa trocar cores; a sugestão é usar texto de verdade quando possível, ou imagem de resolução maior.
- Texto que não pode ser lido por causa da identidade visual da marca **não** fica isento; só o logotipo fica.

## Por que 4,5 e 3

3:1 é o mínimo das normas ISO 9241-3 e ANSI/HFES 100-1988 para visão normal. 4,5:1 compensa a perda de sensibilidade ao contraste de quem tem acuidade de 20/40 (fator de cerca de 1,5, a acuidade típica por volta dos 80 anos); 7:1 (nível AAA, critério 1.4.6) cobre 20/80. O 18 pt vem do corpo padrão de impressão ampliada; o 14 pt, do mínimo de impressão ampliada.

## Tudo o mais que ensina

- A fórmula do contraste: (L1 + 0,05) / (L2 + 0,05), com a luminância relativa no sRGB; o 0,05 representa o reflexo típico da tela. Vai de 1:1 a 21:1.
- Borda fina em volta da letra conta como letra; borda larga que preenche o miolo vira halo e conta como fundo.
- Cor sem fundo declarado (ou o inverso) é falha (F24); imagem de fundo sem contraste com o texto também (F83).
- Texto muito estilizado, que funciona como desenho, cai no critério 1.4.11 (contraste de não texto, 3:1).
- Placeholder, texto de passar o mouse e de foco entram na regra; pessoas com algumas deficiências cognitivas precisam de pouco contraste, e oferecer um ajuste de cores que volte ao mínimo não viola o critério.

---

O texto integral está na url do frontmatter.
