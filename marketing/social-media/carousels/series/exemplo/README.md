---
status: modelo
nome: Série de exemplo
---

# Série de exemplo (em branco)

Uma **série** é um conjunto de carrosséis com o mesmo conceito e a mesma identidade visual: o mesmo papel, as mesmas tintas, a mesma letra, a mesma grade, o mesmo jeito de anotar e de desenhar. O leitor reconhece a peça antes de ler, e quem faz a peça não decide de novo, a cada post, o que já está decidido. Cada série nasce com conceito próprio; dentro dela, a forma evolui de leve, com data no histórico do design system, sem trocar o conceito.

Esta pasta é o modelo. Para começar uma série, copie a pasta inteira para `marketing/social-media/carousels/series/<nome-da-serie>/` e preencha, nesta ordem:

1. **O `design-system.md`:** as seções vêm em branco, cada uma com o roteiro do que decidir. É a régua que a skill `visual-form` lê para montar as telas e que a rubrica de design usa para julgar.
2. **A identidade em `design/`:** troque os valores de `design/caderno.css` (as tintas, as letras, os papéis, a grade) pelos da série, e o que o `design/caderno.js` faz sozinho (assentar o texto, prender a palavra curta, desenhar as marcas), se a série pedir outro gesto. A identidade que vem aqui é neutra e genérica: serve para o exemplo rodar, não para ir ao ar.
3. **O `design/papeis.json`:** a tabela "Letra" do design system em dados e a cor do acento. As conferências da forma leem este arquivo; quem muda a tabela no `design-system.md` muda aqui também (o `teste_papeis.py` da `visual-form` confere que os dois dizem o mesmo).
4. **O post de exemplo** (`exemplo-de-post/`): um `slides.html` de duas telas, com o `texto.md` travado e a `legenda.md`, que passa nas conferências (`conferir_telas.py`) com 0 ERRO. Na primeira peça da série, é ele o "publicado mais recente do mesmo tipo" que a forma copia. Refaça-o na identidade nova antes da primeira peça, e confira de novo.

## O que fica em cada pasta de peça

Cada peça da série ganha uma pasta datada, `AAAA-MM-DD_<tema>/`, ao lado do `exemplo-de-post/`, com o `texto.md` travado, a `escaleta.md`, o `slides.html`, o `assets/` com as imagens usadas, o `refinamentos.md` (o registro das passadas) e a `legenda.md`. A skill `piece-creation` conduz a peça da ideia à prévia, e cada etapa diz o que grava.

## Conferir o exemplo

Da raiz do repositório:

```
python -X utf8 .claude/skills/visual-form/scripts/conferir_telas.py marketing/social-media/carousels/series/exemplo/exemplo-de-post
python -X utf8 .claude/skills/visual-form/scripts/teste_papeis.py
```

O esperado: 0 ERRO e 2 AVISO na primeira, e "ok" na segunda. Os dois avisos são esperados no exemplo: o `acento_area`, porque o exemplo quase não usa o acento; e o `texto_miudo` da tela 2, porque a nota ("a nota aponta o desenho") sai a 32 px, abaixo do piso de 38 px que a rubrica de design dá à nota manuscrita. Na identidade neutra, a nota usa a mesma letra do corpo, no mesmo tamanho; quando a sua série escolher a letra da nota, ponha-a a 38 px ou mais (no `design/caderno.css`, no `design/papeis.json` e na tabela "Letra" do `design-system.md`) e o aviso some. O piso ainda é provisório, a calibrar nas peças publicadas.
