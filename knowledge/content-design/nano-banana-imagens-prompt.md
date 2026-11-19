# Nano Banana (Gemini Image) — prompt para infográficos, ícones, web e aula

Referência de técnica para **enriquecer visualmente** o conteúdo já produzido (o roteiro/processo é próprio — isto não é um pipeline de produção). Foco: imagens para **sites, ícones, infográficos de aula e esquemas visuais**. Síntese analítica.

> Fontes (oficiais, só citação): *How to create effective image prompts with Nano Banana (Gemini image prompt guide)*, de Google DeepMind, https://deepmind.google/models/gemini-image/prompt-guide/; *Nano Banana Pro image generation in Gemini: Prompt tips*, de Google (blog.google), https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/; *Ultimate prompting guide for Nano Banana (Google Cloud)*, de Google Cloud, https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana. Práticas (só citação): *Nano Banana 2 (Gemini 3.1 Flash Image): o que é, como usar e 20 prompts prontos*, de treinamentosaf.com.br, https://treinamentosaf.com.br/nano-banana-2-gemini-3-1-flash-image-como-usar/; *The Ultimate Nano Banana Pro Prompting Guide (Mastering Gemini 3 Pro Image)*, de atlabs.ai, https://www.atlabs.ai/blog/the-ultimate-nano-banana-pro-prompting-guide-mastering-gemini-3-pro-image. Pesquisa pela skill `research` (Perplexity + Gemini).

## Modelos
- **Nano Banana 2 (Gemini 3.1 Flash Image)** — iterar rápido, consistência por múltiplas referências. **Nano Banana Pro (Gemini 3 Pro Image)** — design final, fidelidade máxima de texto, composições complexas. (A seção "Limites oficiais" abaixo cita também o Nano Banana 2.1 e o 2 Lite; conferir no README da skill `image-gen` quais ela serve.)
- Nome de modelo servido igual no Vertex (ver README da skill `image-gen`).

## Fórmula base (oficial)
`[Subject] + [Action] + [Location/context] + [Composition] + [Style]`. Com referência: `[Imagens de referência] + [Instrução de relação] + [Novo cenário]`. **Framing positivo** (descrever o que quer, não o que não quer). Iterar de forma conversacional — mudar 1–2 aspectos por vez, dizendo o que **permanece igual**.

## Texto legível (o ponto crítico p/ infográfico)
- **Sempre entre aspas** as palavras que devem aparecer: `"Perception"`, `"Núcleo"`.
- **Descrever a fonte:** *"bold, white, sans-serif font"*, *"Century Gothic"*.
- **Hack "texto primeiro":** conversar para definir o texto, depois pedir a imagem com ele.
- **Limitação oficial:** texto pequeno e parágrafo longo distorcem — **máx. ~5–7 palavras** por bloco; descrições longas entram no HTML ou no editor depois.

## Infográficos e diagramas (aula, esquema visual)
- Pedir explicitamente **"timeline, flowchart ou diagrama"** — o modelo organiza a info.
- **Vista 2D plana / flat vector, fundo claro, alto contraste**; rótulos entre aspas.
- **Grounding (Google Search)** ajuda a desenhar conceito **factualmente correto** (ciclo da água, arquitetura de agente) — vantagem real p/ material didático. Dá para pedir "buscar dado real → montar o gráfico" num único prompt (treinamentosaf, Prompt 13).
- Precisão factual **não é garantida** (limitação oficial) — conferir números/rótulos.

## Conjunto de ícones consistente
- **Gerar o lote numa única imagem** (5–12 ícones) força as mesmas regras visuais.
- **Restrições geométricas:** espessura de linha, arredondamento de canto, paleta fixa (1 neutra + 1 destaque), fundo branco isolado.
- Vetorização pós-geração (não-oficial, prático): exportar 2K/4K → **Image Trace** (Illustrator) → SVG.

## Imagens para site
- **Espaço negativo deliberado** de um lado para sobrepor título/CTA em HTML.
- **Fugir do "cara de IA genérica":** *editorial style*, *flat vector*, *minimalist 3D clay*.
- Até **14 imagens de referência** (style guide, logo) para casar com a identidade — "referência rigorosa de estilo".

## Slides de aula
- **16:9**, clareza didática, fundo claro; grounding para precisão do conceito.

## Consistência (transversal)
- **Nomear** personagens/objetos ao subir referências.
- **Reanexar a referência** a cada 2–3 gerações e instruir "manter idêntico à foto".
- **Limites oficiais:** Nano Banana 2 e 2.1, até **4 personagens e 10 objetos**; Nano Banana Pro, até **5 personagens, 6 objetos e 3 referências de estilo**; Nano Banana 2 Lite, até 14 objetos e sem consistência de personagem; no máximo 14 referências por chamada (*Gemini API: geração de imagem (Nano Banana), referências e consistência de personagem*, de Google (documentação oficial da Gemini API), https://ai.google.dev/gemini-api/docs/image-generation). Versões antigas de guias de terceiros davam 5 personagens e 14 objetos ao Nano Banana 2.

## Ficha de personagem

A partir de uma ficha de continuidade publicada por um criador (@ai.withphil) e da documentação dos fabricantes: *Gemini API: geração de imagem (Nano Banana), referências e consistência de personagem*, de Google (documentação oficial da Gemini API), https://ai.google.dev/gemini-api/docs/image-generation; *OpenAI: guia de prompt para imagem (consistência de personagem e imagens de referência)*, de OpenAI (documentação oficial para desenvolvedores), https://developers.openai.com/api/docs/guides/image-prompting. O conteúdo da ficha vem de guias de praticante, sem documento oficial.

**Para que serve:** manter o mesmo personagem em todas as peças. Os dois fabricantes ensinam o mesmo método: usar a imagem do personagem como referência em cada cena nova e **repetir as restrições de aparência em todo prompt** ("mesmas feições, proporções e paleta", "não redesenhe o personagem"), iterando por conversa e dizendo o que não muda. Edições repetidas desviam; quando um trecho precisa ficar idêntico, compor por cima em vez de confiar no prompt (OpenAI).

**O que a ficha contém:**

- **Trava de identidade:** de três a cinco traços que não mudam (rosto, cabelo, marca, acessório fixo), escritos numa frase que se repete igual em todo prompt.
- **Giro de corpo inteiro:** frente, três quartos, lado, costas, em pose neutra, luz igual e fundo liso.
- **Expressões:** mudam a emoção, não a anatomia.
- **Poses e gestos** característicos.
- **Figurino em duas partes:** o que é fixo e o que varia por tema ("identidade fixa, figurino por tema").
- **Paleta com código hexadecimal** e uma nota de estilo de traço.

**Cuidados:** texto, logo e joia pequena são as âncoras menos confiáveis; não fazer delas a identidade. Com o limite de 4 personagens no Nano Banana 2, um elenco fixo pequeno (dois, como no quadrinho de diálogo de [[formatos-de-imagem]]) é o que mais se mantém. A ficha gerada vira referência fixa da skill `image-gen` (`--refs`), na mesma lógica da roda de referências de [[formatos-de-imagem]].

**A ficha diante do vídeo:** a ficha segue como documento (o *model sheet* da animação, [[2026-11-12-wikipedia-model-sheet]]) e como entrada do Nano Banana para compor quadros, mas não vai como uma imagem só ao modelo de vídeo: o guia do Seedance 2.0 desaconselha a imagem mista e a multi-vista, e o Kling e o Omni Flash recebem as vistas em arquivos separados. Por isso a folha de personagem sai em duas camadas, a folha-documento e o pacote de vistas soltas. A paleta em hex vale como guia, porque nenhum de 26 modelos medidos acerta sempre (o melhor tira 4,11 de 5 e o Nano Banana Pro 3,67, em 9 amostras cada, na rodada que a página chama de pilot-0, numa medição de parte interessada, [[2026-11-12-imgly-fidelidade-de-cor-de-marca]]), e a seed não guarda personagem. Detalhe, fontes e o que se mediu em [[personagem-consistente]].

## Specs úteis
- Resoluções **1K/2K/4K** (especificar p/ nitidez de fonte/linha fina).
- Aspect ratios: 1:1, 3:4, 4:3, **16:9** (slide/site), 9:16 (stories), 21:9, +.
- Imagens carregam SynthID + C2PA; uso comercial permitido.

## Não-verificado (registrar como tal)
- `thinkingLevel: high` para planejar layout de texto — citado só pelo Gemini, **não achado nas fontes oficiais**. Tratar como sugestão.

## Elos
- Aplicação em carrossel-esquema: [[carrossel-instagram]] (áreas seguras/design). O Nano Banana gera o **visual de apoio** ("uma ideia, um visual"); o design de slide segue aquelas regras.
- Contraponto a pesar (público técnico): imagem "cara de IA" pode custar autenticidade com audiência profissional — usar como base/enriquecimento, manter elementos autorais.
