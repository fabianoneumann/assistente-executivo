---
name: image-gen
description: >-
  Gera imagem raster por dois geradores, o Nano Banana (Gemini) e o GPT Image pelo Codex,
  escolhidos por uma tabela de quem faz o quê, com o banco de imagens consultado antes,
  o custo e a linhagem de cada geração registrados e uma conferência por máquina depois:
  desenhos a lápis das peças, personagens, ilustrações e heros, texturas e fundos,
  infográficos-imagem e mapas esquemáticos, telas de interface como mock. USE quando a
  pessoa pedir para gerar ou criar uma imagem, ilustração, desenho a lápis, personagem,
  hero, fundo, infográfico como imagem ou um "mapa" visual para post, site ou aula, ou
  quando a forma de uma peça pedir uma imagem que o banco não tem. NÃO use para montar ou ajustar as telas
  (visual-form), layout, UI, deck ou one-pager on-brand (Claude Design, frontend-design),
  o objeto que se move (object-anatomy) nem para ícones de sistema em SVG limpo.
---

# Skill: image-gen

Bloco **single-purpose** de geração de imagem, componível: a forma de uma peça (`visual-form`) pede a imagem, depois de o roteiro (`piece-script`) nomear o que ela mostra, e a exportação (`slides-export`) sai em JPEG. A skill é **brand-agnóstica**: quem chama passa `--refs` e põe os tokens e hex no prompt; nenhum design system fica fixo aqui.

> **Passo 0, as credenciais.** Antes de tudo, rode da raiz do projeto `python -X utf8 scripts/confere_ambiente.py --skill image-gen`. Se ele sair com `[PARE]`, pare aqui: repasse à pessoa a mensagem dele (qual variável falta, onde se pega e como se põe) e não tente rodar a skill sem a chave. Se o script não existir (a skill instalada como plugin noutro projeto), siga: o próprio código da skill para com a mesma mensagem na primeira chamada.

**Lições:** antes de começar, leia as abertas e as apontadas em [`licoes.md`](./licoes.md) desta pasta.

**O que é deste projeto** (o banco de imagens, onde salvar, a identidade de cada série, a regra de custo, o perfil do Codex) está em [`references/projeto.md`](./references/projeto.md). Leia antes de gerar.

## Os dois geradores e quem faz o quê

- **Nano Banana** (Gemini), pelo `scripts/nano_banana.py`: AI Studio (`GEMINI_API_KEY`, com a cobrança da sua conta na regra de custo do `references/projeto.md`) por padrão, com custo por geração (abaixo); a Vertex (`VERTEX_API_KEY`, pós-pago) só por `--provider vertex` e pela regra de custo do projeto.
- **GPT Image pelo Codex**, pelo `scripts/codex_imagem.py`: o gerador integrado do Codex (`gpt-image-2`), no plano pago do ChatGPT de quem usa, sem custo por imagem (gasta a franquia; confira o `/status` depois de um lote grande). O modelo não se escolhe. **É opcional:** pede o Codex CLI instalado e logado e um perfil criado uma vez (o passo está no README); sem ele, o script para com a instrução e o Nano Banana segue.
- **Qual usar:** a tabela de quem faz o quê por tipo de pedido, as regras de quando gerar nos dois e de como uma linha se fixa, e o formato do prompt do Codex estão em [`references/roteamento.md`](./references/roteamento.md). Leia antes de escolher.

## Antes de gerar: o banco

Procure primeiro no banco de imagens já geradas (o caminho está em `references/projeto.md`; o `scripts/indexa_banco.py` o monta dos `prompts.md` das peças, e roda de novo depois de uma peça nova). **Reaproveite** quando uma imagem do banco mostra o que a tela pede, no traço da peça, e ainda não foi usada na mesma semana nem na peça irmã (nada de repetir o desenho da semana); **gere** quando nenhuma serve, ou quando a imagem do banco pede só um ajuste que muda o que ela mostra. O reaproveitamento se anota no `prompts.md` da peça, com o arquivo de origem.

**A roda de referências:** a imagem aprovada de uma peça vira âncora `--refs` das próximas do mesmo traço (`knowledge/content-design/formatos-de-imagem.md`). Na iteração, mude uma ou duas coisas por vez e diga o que fica igual, reanexando a referência; num projeto novo, de 4 a 6 direções com nome e tese antes de refinar uma.

## Depois de gerar: a conferência por máquina

`python -X utf8 .claude/skills/image-gen/scripts/confere_imagem.py <imagem> --proporcao <pedida> [--sem-texto --jev]`: a proporção contra a pedida, o centro visual e, quando o pedido não tem texto, o texto inventado por uma pergunta ao Jev. **O Jev é opcional** (pede `TYPESAFE_API_KEY` e o cliente em `scripts/jev/` da raiz): sem ele, a conferência de texto pula com um aviso de uma linha, e as outras rodam. A pergunta do Jev está em teste (é sinal, não trava): as telas com texto saem perto de 1,0 e os lápis bem abaixo, com exceções em marcas que parecem letra (máquina de escrever no papel). O defeito objetivo se corrige antes de a imagem chegar à pessoa; o gosto é dela.

## Arquitetura (Nano Banana)

- **AI Studio + `generate_content`** (`GEMINI_API_KEY`) é o padrão; o AI Studio não aceita escolher o formato de saída, então o script converte para o do `--out` (PNG por padrão). A **Vertex** (`VERTEX_API_KEY`, pós-pago no projeto do Google Cloud; devolve PNG direto) fica por `--provider vertex`, e o script lembra no stderr que a geração entra na fatura.
- A Interactions API (mais nova) foi testada e só existia no AI Studio (404 no Vertex). Quando chegar ao Vertex, refatorar só `_generate_with_retry`.

## Modos (presets; override com --model/--size/--aspect)

| modo | model | size | aspect | uso | custo/img (medido) |
|---|---|---|---|---|---|
| `explore` | flash (NB2) | 1K | 4:5 | exploração barata/descartável (0.5K p/ simples) | US$ 0,089 |
| `final` | pro | 2K | 4:5 | entregável (default) | US$ 0,171 |
| `map` | pro | 4K | 3:2 | mestra ampla p/ mapa cortado (2 slides) + zooms no HTML | ~US$ 0,24 (pela tabela, não medido) |

**O custo, medido:** o `nano_banana.py` grava no JSON de saída o uso de tokens que a resposta devolve e o custo pela tarifa da página oficial (`ai.google.dev/gemini-api/docs/pricing`: a saída de imagem do pro a US$ 120 e a do flash a US$ 60 por milhão de tokens). Uma imagem `explore` (flash 1K) gastou cerca de 1.480 tokens de saída, e uma `final` (pro 2K) cerca de 1.430: acima dos 1.120 tokens por imagem que a documentação contava, e por isso a tabela mostra o medido. A tarifa muda: confira a página antes de confiar no número. O custo de cada geração vai ao `prompts.md` da peça. O GPT pelo Codex não tem custo por imagem; pela chave da API da OpenAI, ficaria em uns 3 centavos.

**Lógica:** no Pro, 1K custa igual a 2K, então sempre 2K. Explore no flash@1K (0.5K se muito simples), 2K só se o detalhe importar. `map` em 4K se justifica: uma mestra vira de 4 a 6 slides. Modelo novo do gerador entra na tabela depois de uma comparação às cegas, como o GPT entrou.

## Comandos

```
python -X utf8 .claude/skills/image-gen/scripts/nano_banana.py --mode final --prompt "..." --out img.png
python -X utf8 .claude/skills/image-gen/scripts/nano_banana.py --mode explore --prompt "..." --out draft.png
python -X utf8 .claude/skills/image-gen/scripts/nano_banana.py --mode map --prompt "..." --out master.png
# refs de marca/estilo (0 a 14): --refs marca.png estilo.png paleta.png
# override: --model pro --size 4K --aspect 21:9 ; Vertex (pós-pago, com estimativa antes): --provider vertex
python -X utf8 .claude/skills/image-gen/scripts/codex_imagem.py --prompt "..." --out img.png [--refs a.png --papel-refs "estilo"]
```

Saída (stdout JSON): `{skill, gerador, provider, model, uso, custo_usd, mode, size, aspect, output_mime, out, bytes, error}`; a do `codex_imagem.py` traz a linhagem (`gerador`, `versao`, `modelo`, `data`, `segundos`) e grava um `.json` ao lado da imagem.

## Onde salvar a imagem (o uso define o destino)

A imagem nasce onde vai ser usada:
- **Teste ou validação descartável:** scratchpad (temporário), descartar. Só reorganiza se virar keeper.
- **Asset de um post, aula ou site:** na pasta do entregável (o caminho de cada tipo em `references/projeto.md`).
- **Banco de imagens (peça de conteúdo):** toda geração feita para a peça, usada ou não, sobe **original** ao bucket de conteúdo, em `assets/gerados/AAAA-MM-DD_<peça>/` (skill `r2-storage`); o `assets/` da peça guarda só o que foi usado, já limpo. O roteiro da peça aponta tudo em "Artefatos gerados".
- **Prompts da peça:** o prompt exato de cada geração vai para `prompts.md`, na pasta da peça: o arquivo de saída, o gerador e a versão, o modo e a proporção, o custo, as referências (`--refs`), o texto inteiro do prompt e o que virou dele (usado, opção de fora). É dele que o índice do banco se monta, e é ele que deixa reproduzir uma imagem ou tentar uma variação sem reinventar o prompt.
- **Identidade no prompt:** a identidade não fica fixa nesta skill; vem do design system de quem pede a imagem (o da série, o de uma campanha, o de um post avulso), pelo caminho em `references/projeto.md`. As referências pessoais da marca não são material de geração.

## Quando a imagem é recortada ou vai para cima de outro fundo

Imagem usada inteira não passa por isto. Quando ela é **recortada**, ou **assentada sobre outro fundo** (o desenho a lápis sobre o papel da série, por exemplo), usar `scripts/so_traco.py`:
```
python -X utf8 .claude/skills/image-gen/scripts/so_traco.py desenho.png assets/desenho.png [--lado 880] [--sem-recorte]
```
- Tira o papel e deixa só o traço, em PNG transparente.
- **Recorta pelo traço firme, não por qualquer pixel.** As linhas de construção claras vão longe para um lado, e o recorte pela caixa inteira deixa o desenho deslocado na peça.
- **Confere o centro visual:** o script diz quanto o peso do desenho foge do meio, e avisa acima de 5%. Aí, centralizar pelo centro visual (deslocar na peça o quanto ele indicou), não pelo meio da caixa.

## Texto na imagem (decisão por chamada)

- **Rótulos primários curtos** (1 a 2 palavras) saem **nítidos e corretos**: use `pro`.
- **Texto pequeno ou denso sai ilegível ou alucinado** (limite oficial confirmado). Então:
  - **Componente de slide:** o texto fica no **HTML** (mais nítido e na marca), não na imagem.
  - **Infográfico ou mapa:** assar só os **rótulos primários**; anotações finas vão como **overlay HTML** sobre a imagem, ou são evitadas. Palavras exatas entre "aspas" no prompt.

## Consistência

Passar `--refs` (recomendado: 2 a 3 de marca, 2 a 3 de estilo, 1 a 2 de paleta) e os tokens e hex no prompt. **Personagem:** a trava de identidade (3 a 5 traços repetidos em todo prompt) e a medida por juiz ao lado da imagem-mestre, quando houver personagem na fila.

## Mapa panorâmico + zoom (fatiar no HTML, não na skill)

1. Gerar **uma mestra** com `--mode map` (Pro@4K, wide) e salvar no `assets/` do post.
2. No `slides.html`, a **mesma mestra** vira 2 slides seamless (`object-position` metade esquerda e direita) e slides de **zoom** (`background-position` + `scale` recortando regiões). A `slides-export` exporta cada tela.
3. **A API não gera 8:5 nem 16:10** (rejeita com `400 INVALID_ARGUMENT`, e não aceita pixels sob medida). Para **2 slides** seamless, o `map` já sai em **3:2** (o mais próximo de 8:5): o template **corta cerca de 6% de altura** (topo e base) ao 8:5 exato, **preservando os rótulos laterais**; o 16:9 cortaria cerca de 10% de largura e comeria rótulos. Para 3 slides, `--aspect 21:9`. O 4K garante nitidez a 1080 px nos cortes e zooms.

**Ao terminar:** se houve falha, contorno ou acerto que vale lembrar, registre em [`licoes.md`](./licoes.md) desta pasta, na mesma entrega (formato e estados em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md)).
