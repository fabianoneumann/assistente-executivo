# Formatos de imagem — receituário (Nano Banana × HTML)

Síntese de **quais formatos de imagem** funcionam para conteúdo e de **quanto assar na imagem × quanto compor no HTML**. É **método, não prompts** — os esqueletos de prompt e as referências de estilo nascem das primeiras peças reais (a roda de referências, abaixo). Base: testes da skill `image-gen` + análise de infográficos externos como exemplos de possibilidade. Técnica de prompt em [[nano-banana-imagens-prompt]]; fronteira com o Claude Design em [[claude-design-vs-nano-banana]].

## O dial central: assar na imagem × compor no HTML
Não é regra fixa — é um **dial a calibrar por formato**:
- O Nano Banana carrega **estrutura, ilustração, cena e rótulos curtos/grandes** com folga.
- **Texto denso/pequeno embaralha** (limite oficial, visto nos testes e até em infográficos alheios prontos — ex.: `"Españos"`, `"striph"`, CJK torto).
- **"Mais assado" é direção válida para riqueza visual** — os melhores exemplos são *all-in-image* (texto e tudo) e ficam mais ricos que um esquema com metade em HTML. O custo é a fidelidade do texto. Os primeiros testes ficaram **menos ricos** de propósito (conservadores); dá para subir o "assado".
- **Restrição dura:** **números/dados exatos → HTML** (precisão), ou, se assados, **conferir palavra a palavra**.
- Ponto de partida: assar estrutura + rótulos curtos, dados no HTML; **subir o assado por formato** conforme as primeiras peças mostrarem onde o erro começa.

## Formatos (quando usar · o que assar · o que HTML)
| Formato | Bom para | Assar (Nano Banana) | HTML |
|---|---|---|---|
| **Tirinha / quadrinhos** | storytelling, narrativa, "como surgiu" | painéis ilustrados, cena | balões longos / legenda |
| **Quadrinho de diálogo** (uma tela por quadro) | explicar um conceito técnico por perguntas de quem lê | dois personagens fixos (quem pergunta, quem explica) e um objeto por quadro | os balões |
| **Cena-infográfico** (ciclo da água) | explicar processo/tópico | ambiente ilustrado + rótulos curtos | descrições longas |
| **Sketchnote** (mão-livre) | educação, passo-a-passo, marketing | nós, setas, ícones, headers curtos | dados, notas finas |
| **Comparação** (métodos de café) | diferenciar opções | objetos ilustrados por coluna | **estrutura + números** (tende ao Claude Design) |
| **Hub / mapa esquemático** | apresentar tópico/eixos | nós + rótulos curtos | números por nó |
| **Hero / ilustração / fundo** | enriquecer slide/site | a imagem inteira (sem texto) | o texto por cima |
| **Aforismo com metáfora ilustrada** | reflexão, comportamento, verdade reconhecível; uma frase por tela | a cena que literaliza a metáfora (sem texto) | a frase, no terço de cima |

## Linhas de conteúdo → formato sugerido
- **Passo a passo** → sketchnote / fluxo.
- **Comparação** → comparação ilustrada (números no HTML) ou Claude Design.
- **Explicação de tópico** → cena-infográfico ou hub ilustrado.
- **Apresentação de tópicos** → sketchnote ou mapa.
- **Reflexão ou opinião em frase curta** → aforismo com metáfora ilustrada.

## Aforismo com metáfora ilustrada

Registrado a partir de uma referência de carrossel de terceiros (uma compilação de @sobrepessoasintensas no Instagram, [instagram.com/p/DdoMsRDkduB](https://www.instagram.com/p/DdoMsRDkduB/)). Cada tela traz uma frase e uma cena que **literaliza a metáfora**: a imagem diz a mesma coisa que o texto sem precisar dele. Recursos de cena que funcionaram ali:

- **Antes e depois** em duas cenas na mesma tela (o fracasso é o arco largado, não a flecha errada).
- **Três quadros** dentro da tela, como tirinha (tentar, ajustar, se acomodar).
- **Fila de variações** como escala (da tentação ao controle, pessoa a pessoa).
- **Espelho** para identidade (o reflexo mostra quem a pessoa pode ser).
- **O abstrato vira personagem** (o conflito como uma bola de pelos raivosa).
- **Multidão contra indivíduo** e **comparação lado a lado**.

Animais para temas sensíveis criam distância: a pessoa se reconhece sem se sentir acusada. Composição: frase no terço de cima, cena que se desfaz nas bordas, um ponto focal. **O estilo acompanha o registro do conteúdo:** aquarela quente para reflexão; traço preto com uma cor para método e tutorial (referência do @okaashish). Risco: o estilo aquarelado de motivação está muito difundido; vale buscar assinatura própria.

## Quadrinho de diálogo

Registrado a partir de uma referência de terceiros ([instagram.com/p/DdlpXTLDwdG](https://www.instagram.com/p/DdlpXTLDwdG/), do @okaashish). Variante da tirinha que reduz o custo: **dois personagens fixos** (quem pergunta, no lugar de quem lê; quem explica, sem rosto), **sem cenário**, um objeto desenhado por quadro que concretiza a ideia, e a explicação nos balões. **A pergunta de quem lê move a história** ("diferente como?", "me dá um exemplo", "pra que eu uso?") e vira o gancho de cada tela. Um personagem sem rosto não varia entre quadros, o que resolve o maior risco do formato. Os balões ficam no HTML, como manda o orçamento de texto abaixo.

## Orçamento de texto na imagem (o teto)
Curto + grande + poucos rótulos = confiável. Frase/anotação densa/miúda = quebra. O gatilho de erro é sair de "poucos rótulos curtos" para "texto corrido". Sempre **inspecionar o texto assado** antes de usar — até peça polida de terceiros vaza erro.

## Sketchnote no design system
É estilo de prompt (hand-drawn, marker, doodle). O clássico é papel claro/tinta preta; existe a variante **dark/neon** (fundo escuro, traço neon, "giz em quadro-negro"). Qual entra é decisão do design system da série.

## Roda de referências (o método que faz isso escalar)
1. Fazer a **1ª de cada formato** → ajustar → aprovar.
2. O **prompt concreto fica com o post** (ex.: `prompts.md` na pasta do post — proveniência com o artefato, não numa lista central que apodrece).
3. A peça aprovada vira **âncora `--refs`** para as próximas → a consistência cresce.
4. Quando houver peças aprovadas, montar um **set durável de refs** por formato.

## Elos
- [[nano-banana-imagens-prompt]] · [[claude-design-vs-nano-banana]] · [[carrossel-instagram]]
- Ferramenta: skill `image-gen`.
