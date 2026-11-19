---
titulo: "Exporting as Video"
tipo: artigo
autor: "Spline (documentação oficial)"   # a página não tem assinatura
url: "https://docs.spline.design/exporting-your-scene/files/exporting-as-video.md"
publicado_em: null   # nem a página da documentação nem a de preços trazem data
capturado_em: 2026-11-12
licenca: "protegida: o Markdown da documentação e o da página de preços não declaram licença nem trazem rodapé (valem os termos do site da Spline); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [spline, 3d-world, video-export, seamless-loop, watermark, pricing]
---

# Spline: exportar a cena como vídeo, e em que plano isso vem

Nota de fato: tabelas do que as duas páginas registram, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: as páginas são protegidas.

**Proveniência.** Duas páginas, baixadas em 12/11/2026:

- A principal, "Exporting as Video", da documentação da Spline (seção de exportação de arquivos), https://docs.spline.design/exporting-your-scene/files/exporting-as-video.md, na versão Markdown que a documentação serve; sha256 (hash omitido); sem captura na Wayback. Título conferido no cabeçalho do arquivo. Lida inteira (dois parágrafos, os cinco passos, uma imagem e um vídeo, vistos só pelo endereço).
- A de preços, https://spline.design/pricing, lida no Markdown "Spline Pricing" guardado como `spline-pricing.md`; sha256 (hash omitido); Wayback http://web.archive.org/web/20261102011225/https://spline.design/pricing (da página HTML). Lido inteiro, com a tabela de comparação e o FAQ, e conferido contra o texto extraído do HTML da mesma página (cabeçalho "Start for free, scale with your team and agents"): preços, itens dos planos, tabela e FAQ batem. Diferenças: o HTML diz "2 months free" no anual de cada plano, onde o Markdown dá a economia em porcentagem, e lista os créditos extras em degraus com o preço anual de cada um.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (passo, preço, sim ou não) fica fora. Resultado: 3 de 16 unidades seguem a fonte, a célula do render no lugar da gravação de tela, a do cancelamento (junta duas frases do FAQ) e a segunda frase da recomendação, que junta dois itens do plano Pro; a maior sequência seguida que segue a fonte tem 2 unidades, de páginas diferentes, e as três citações estão à parte. O `parafrase.py` saiu com o código 3 contra cada um dos três textos (o Markdown da documentação, o Markdown de preços e o texto extraído do HTML de preços); nas três rodadas, 16 unidades medidas (14 de prosa, 2 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas.

## Em uma frase

Documentação e página de preços da própria Spline, que vende a ferramenta: a primeira dá os cinco passos para gravar uma animação da cena como arquivo de vídeo, a segunda diz em que plano a exportação de vídeo entra; para a base, é a consulta de passos, ajustes e custo dessa rota.

## A exportação de vídeo

| Item | Fato |
|---|---|
| O que é | render das animações definidas, não gravação de tela |
| Promessas da página | tempo de transição constante; reprodução suave |
| Laço | mais fácil fechar laço perfeito, sem emenda |
| Qualidade | mantém a do projeto, inclusive a resolução |
| Passo 1 | botão Export, na barra de ferramentas |
| Passo 2 | categoria Files → "Video" |
| Passo 3 | duração em segundos, FPS e resolução |
| Passo 4 | botão Export |
| Passo 5 | depois do processamento, vai aos downloads ou pede onde salvar |
| Antes de exportar | cena e animação prontas |
| Formato do arquivo | não informado |
| Opções de FPS e de resolução | não informadas |
| Duração máxima | não informada |

## Os planos (preço por assento, em dólar)

| Plano | Mensal | Anual (por mês) | Anual (por ano) | Créditos de IA por assento/mês |
|---|---|---|---|---|
| Free | US$ 0 | US$ 0 | — | nenhum |
| Hobby | US$ 15 | US$ 12 | US$ 144 | 2.000 |
| Pro | US$ 30 | US$ 25 | US$ 300 | 3.000 |
| Max | US$ 70 | US$ 60 | US$ 720 | 10.000 |
| Enterprise | sob consulta | sob consulta, só anual | sob consulta | sob consulta |

| Cobrança | Fato |
|---|---|
| Desconto do anual | até 20% |
| Economia anual por assento | Hobby US$ 36; Pro US$ 60; Max US$ 120 |
| Crédito extra | 1.000 por assento a US$ 5/mês (US$ 48/ano no anual) |
| Teto com extras | 10.000 no Hobby e no Pro; 20.000 no Max |
| Créditos não usados | não acumulam |
| Pagamento | principais cartões de crédito |
| Cancelamento | acesso até o fim do período pago; sem reembolso proporcional |

## Exportação por plano

| Item | Free | Hobby | Pro | Max | Enterprise |
|---|---|---|---|---|---|
| Exportar vídeo (editor 3D e 2D) | não | não | sim | sim | sim |
| Exportação web sem marca-d'água | não | sim | sim | sim | sim |
| Incorporação web sem marca-d'água (editor 2D) | não | não | sim | sim | sim |
| Imagem em resolução maior | — | sim | sim | sim | sim |
| Apple e Android | não | não | sim | sim | sim |
| USDZ e STL | não | não | sim | sim | sim |
| GLTF com cor e textura | não | não | sim | sim | sim |
| Download do código | não | não | sim | sim | sim |
| Exportação auto-hospedada | não | não | não | não | sim |
| Tamanho máximo de vídeo | — | — | — | 100 MB | — |
| Subir vídeo | não | sim | sim | sim | sim |
| Subir áudio | não | não | sim | sim | sim |
| Várias cenas por arquivo | não | não | ilimitadas | ilimitadas | ilimitadas |
| Arquivos | limitados | ilimitados | ilimitados | ilimitados | ilimitados |
| Chamadas de ferramenta MCP por dia | 20 | 100 | 200 | 400 | 400 |
| Geração de mídia | — | — | — | 5× mais por semana | — |

| Plano grátis, pelo FAQ | Fato |
|---|---|
| Arquivos pessoais | limitados |
| Quem vê | visualizadores ilimitados |
| Modelos | acesso aos Spline Templates |
| Publicar cena | com o logo da Spline |

## O que a fonte recomenda

A documentação manda deixar a cena e a animação prontas e então exportar pelo próprio programa, fixando duração, FPS e resolução, em vez de gravar a tela, e diz que assim o laço fecha mais fácil. A página de preços põe essa exportação a partir do Pro, o mesmo plano que tira a marca-d'água das incorporações do editor 2D.

## Citações

- "Instead of relying on recording the screen, it renders defined animations for maximum precision"
- "Set the duration of the animation in seconds, select a desired FPS, and the resolution you want to export."
- "100MB max video size"

## Lacuna

A documentação não diz o formato do arquivo, o codec, se o vídeo leva áudio ou fundo transparente, quais FPS e resoluções existem, nem a duração máxima, e não diz em que plano a exportação funciona. A página de preços não diz se o vídeo exportado leva marca-d'água em algum plano, se os 100 MB do Max valem para o vídeo exportado ou para o que se sobe, nem qual o limite de tamanho no Pro; nenhuma das duas fala de licença de uso comercial, no plano grátis ou nos pagos.
