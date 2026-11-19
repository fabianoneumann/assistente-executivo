---
titulo: "Text Autofit: How do I stop text overflowing? (Orshot Studio)"
tipo: artigo
autor: "Orshot (documentação do produto, sem autor individual)"
url: "https://orshot.com/docs/orshot-studio/text-modes"
publicado_em: 2026-06-07
capturado_em: 2026-10-29
licenca: "sem licença indicada (documentação de produto comercial; tratada como protegida)"
areas: [content-design]
tags: [text-fit, autofit, overflow, image-generation-api, templates, typography]
---

Ficha de estudo, em palavras próprias (documentação sem licença aberta). Ferramenta de gerar imagem a partir de modelo com texto variável, por editor e API. A data vem dos metadados da página de ajuda equivalente (https://orshot.com/help/text-sizing-modes), publicada e modificada em 2026-06-07. Lido em 2026-10-29, na pesquisa sobre o que cede quando o texto não cabe.

## Os quatro modos para texto que não cabe na caixa

| Modo | O que faz | Quando a documentação recomenda |
|---|---|---|
| **Overflow** (padrão) | o texto quebra normalmente e pode passar da borda da caixa | caixa grande o bastante, ou vazamento aceitável no desenho |
| **Fit** | reduz o corpo até caber; o campo de corpo vira "corpo máximo", com um "corpo mínimo" de **8 px por padrão** | caixa fixa, corpo pode variar com o tamanho do texto, quer o maior texto que cabe |
| **Truncate** | mostra as linhas inteiras que cabem e põe reticências | caixa fixa e corpo que não pode mudar, deixando claro que houve corte |
| **Flow** | divide o texto em várias páginas, repetindo cabeçalho, rodapé e logo em cada uma; corta por linha, palavra ou caractere e evita viúva e órfã com um mínimo de linhas no começo e no fim | texto de tamanho imprevisível (artigo, relatório, nota fiscal) |

## O que vale reter

- O modo vale por camada de texto e é aplicado sozinho quando a API recebe o texto novo; quem chama a API não decide nada na hora.
- O piso padrão do Fit (8 px) não protege a leitura: num modelo de 1080 px, o texto pode encolher muito abaixo de qualquer faixa legível sem aviso. A documentação não diz o que acontece se nem o mínimo couber.
- Os modos são as quatro respostas possíveis ao excesso: deixar vazar, encolher, cortar com sinal ou levar para outra página. A última é o equivalente automático de "dividir em duas telas".

## Tudo o mais que ensina

- O modo se escolhe no painel de estilos, num menu "Text Autofit"; o Flow tem guia próprio ("Flowing Content") e muda a resposta da API, que passa a devolver várias páginas.
