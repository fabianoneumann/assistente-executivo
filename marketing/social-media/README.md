# Conteúdo para redes sociais

A produção de conteúdo para o Instagram (carrossel, Stories e, quando houver, Reels): o que mora em cada pasta, o fluxo de uma peça e as réguas que ela passa.

## O fluxo de uma peça

```
captura → ideia → apuração → pauta → roteiro → forma → portão → exportação
```

1. **Captura:** a ideia crua, registrada pela skill `idea-capture`, sem pesquisa e sem ângulo, em `ideas/`.
2. **Apuração e pauta:** a skill `story-angle` apura e fecha o ângulo; a síntese vai a `knowledge/`, e a pauta ao próprio arquivo da ideia (`estagio: pauta`). O ângulo se fecha aqui, antes de qualquer tela (`decisions/apuracao-e-pauta.md`).
3. **Produção:** a skill `piece-creation` leva a peça do briefing à prévia, chamando a `piece-script` (o roteiro), a `review` (a revisão), a `visual-form` (as telas) e as que elas chamam.
4. **Portão:** a peça passa pelo [`portao-de-qualidade.md`](./portao-de-qualidade.md), com a [rubrica de qualidade](./rubrica-de-qualidade.md) (a mensagem) e a [de design](./rubrica-de-design.md) (a forma); os Stories, pela [rubrica de Stories](./rubrica-de-stories.md). O veredito é o mais pesado dos quatro (reprovada, ajustar, retocar, pronta).
5. **Exportação:** a skill `slides-export` gera os JPEG e, com `--upload`, sobe ao bucket. A publicação pela API fica para a segunda versão do ambiente; até lá, quem publica sobe as imagens pelo app.

Antes de cada etapa, leia as lições daquela etapa em [`../licoes.md`](../licoes.md) e anote no roteiro, no rascunho ou no briefing as que aplicou, ou "nenhuma lição registrada".

## O que mora em cada pasta

```
marketing/social-media/
├── README.md                  ← este arquivo
├── ideas/                     ← ideias cruas e pautas, um arquivo por tema (formato no README de lá)
├── carousels/
│   ├── series/                ← uma pasta por série, com o design system, a estrutura editorial e uma pasta datada por post
│   │   └── exemplo/           ← a série de exemplo, em branco: o modelo para a primeira série
│   └── standalone/            ← carrosséis fora de série, uma pasta datada por post
├── stories/                   ← sequências e Stories avulsos, uma pasta datada por sequência, e o README com as regras do formato
├── rubrica-de-qualidade.md    ← a régua da mensagem
├── rubrica-de-design.md       ← a régua da forma
├── rubrica-de-stories.md      ← a régua dos Stories
├── portao-de-qualidade.md     ← o juiz, o ciclo e a calibração
└── banco-de-imagens.md        ← o índice das imagens geradas (mantido pela image-gen)
```

**A pasta de uma peça** (de carrossel: `AAAA-MM-DD_<tema>/`; de Stories: `AAAA-MM-DD-<tema>/`) guarda o roteiro (`escaleta.md`, `conceitos-e-imagens.md` e `texto.md` no carrossel; `roteiro.md` nos Stories), o HTML das telas (`slides.html` ou `stories.html`), os `assets/`, o `prompts.md` das imagens geradas, a `legenda.md` e o `refinamentos.md` (o estado da criação, as passadas e as lições da peça). As imagens exportadas são transitórias e ficam fora do git; o que vale guardar vai ao bucket.

Plataforma (Instagram, LinkedIn) não é nível de pasta: as telas são as mesmas, só muda a exportação. Registra-se no cabeçalho do post e vira subpasta só quando existir variante real.

**O que é de terceiro** (as respostas da caixinha com o @, a mensagem de alguém, a imagem protegida) fica numa pasta `originals/` ao lado do que a usa, fora do git.
