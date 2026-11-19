# Banco de animações dos Stories

As ideias de tela em vídeo para os Stories: o desenho que se move, a técnica e o que ele conta. Uma animação por sequência, para cada sequência testar uma e a leitura das métricas dizer o que segura quem assiste. Cada ideia usada ganha o link da sequência e a linha do que a leitura mostrou; o banco cresce semana a semana. Começa vazio neste repositório.

**As técnicas:**
- **Por código** (`scripts/anima_cena.py`, para qualquer cena guiada por `window.quadro(t)`): o desenho em SVG, no traço da série, movido no navegador e fotografado quadro a quadro; o `ffmpeg` monta o MP4. Consistência total e custo zero; serve ao que se desenha em traço. O objeto que funciona, se monta ou se separa vem da skill `object-anatomy`, com o mesmo contrato do `window.quadro(t)`.
- **Quadros gerados** (a skill `image-gen`): o modelo de imagem gera os quadros de um laço curto, alinhados pelo corpo do desenho. Serve ao que só a ilustração resolve (chama, fumaça, gesto); custa uma geração por tentativa. Não há script para isso nesta versão: alinhe os quadros e monte o MP4 com o `ffmpeg`, e diga na linha da animação como foi feito.

**Estados:** a fazer; protótipo; usada (com a sequência e a leitura); descartada (com o porquê); cancelada (não será feita como estava sugerida, com o porquê).

**Antes de usar:** o Story em vídeo leva o fim parado (a animação acaba antes do último quadro, e o último quadro segura sozinho), e o texto da tela continua na área segura do README.

## Testadas

| Animação | Técnica | O que se move | Estado |
|---|---|---|---|

## Ideias

| # | Animação | O que se move | O que conta | Estado |
|---|---|---|---|---|
