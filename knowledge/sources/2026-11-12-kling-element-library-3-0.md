---
titulo: "Kling Element Library User Guide"
tipo: artigo
autor: "Kling AI"
url: "https://kling.ai/quickstart/klingai-element-library-3-user-guide"
publicado_em: 2026-02-05   # "Feb 5, 2026" na página; datePublished e dateModified do HTML iguais
capturado_em: 2026-11-12
licenca: "protegida: a página baixada não traz aviso de licença (valem os termos do site da Kling); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [kling, elements, character-consistency, reference-images, multi-view, voice-binding, start-frame]
---

# Kling Element Library (3.0): o *element* no app, quantos entram por geração e o que custa

Nota de fato: tabelas do que a página registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Guia de uso da biblioteca de *elements* na seção "quickstart" do site da Kling, do lançamento do 3.0 e do 3.0 Omni, baixado em HTML em 12/11/2026 (`sha256` (hash omitido)), e lido no texto extraído do HTML: os cinco destaques, a apresentação, os tipos de *element*, a criação por imagens e por vídeo, os exemplos e as cinco perguntas do FAQ; ficaram fora o menu, o rodapé e os guias relacionados. Os exemplos são em vídeo e imagem, e a página só mostra os prompts. Formato: nota de fato, por ser guia técnico (`README.md` desta pasta, item 2). Trata do app e do site (Omni, Video 3.0, página de assets); a criação pela API está em `2026-11-12-kling-api-4-0-criacao-de-element.md`.

**Quem fala.** A Kling, que vende a ferramenta; a página fecha com links para outros guias e para gerar no produto.

**Data.** "Feb 5, 2026" e "11 min read"; os metadados do HTML dão a mesma data.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa do corpo e as células com texto corrido; a célula que só traz um fato fica fora. Corpo: 3 frases de prosa e 5 tabelas; as 12 células de 8 palavras ou mais são listas de nomes, valores ou limites e ficam como fato. Resultado: 0 das 3 unidades segue uma frase da fonte (a recomendação junta a criação por imagens, a descrição e o FAQ do Video 3.0); as três citações estão à parte. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês: a parte traduzida não se mede), 0 frase colada, e a conta lado a lado é a conferência.

## Em uma frase

Guia de venda e de uso da biblioteca de *elements* da Kling no lançamento do 3.0: como criar um personagem, objeto ou cenário reusável por várias imagens ou por um vídeo, ligar uma voz a ele e prendê-lo ao quadro inicial, com os limites por geração e por plano.

## O *element* por imagens

| Item | Fato |
|---|---|
| Imagens por *element* | no mínimo 2, no máximo 4 |
| Composição | 1 principal + 1 a 3 complementares |
| Imagem principal recomendada | de frente |
| Complementares | outros ângulos ou detalhes |
| Mais imagens, segundo a página | mais consistência entre vistas |
| Vistas que faltam | Kling O1 Image, a partir de uma imagem |
| Descrição | escrita à mão ou gerada por IA |
| O que a descrição deve trazer | traços centrais; detalhes-chave; o que o modelo deve ignorar |
| Nome | único na biblioteca |
| Tipo detectado ao subir | ajustável: personagem, animal, item, figurino, cenário, outros |

| Tipo | Exemplos que a página dá |
|---|---|
| Personagens | realista moderno; histórico ou de fantasia; de anime; em CG |
| Animais | realista; de anime; em CG |
| Objetos | do dia a dia; montáveis; de jogo |
| Figurino e acessórios | roupa; visual; acessório |
| Cenários | interno; externo; virtual; realista |
| Efeitos | atmosfera; partículas; magia |

## O *element* por vídeo e a voz

| Item | Fato |
|---|---|
| Onde | 3.0 Omni |
| Vídeo | 3 a 8 s, de um personagem só |
| Criar gravando | só no app |
| Recomendação ao cortar o vídeo | incluir tomadas do personagem em vários ângulos |
| O que se extrai | aparência e voz nativa |
| Voz | a original ou uma trocada |
| Voz no *element* por imagens | áudio de 5 a 30 s de uma pessoa falando |
| Formatos do áudio | mp3, wav, mp4, m4a, mov e outros |
| Áudio recomendado | fundo limpo; ritmo médio; voz neutra; emoção constante |
| Alternativas | biblioteca de vozes; "sem voz" |

## Quantos entram por geração

| Onde | Limite |
|---|---|
| Video 3.0 Omni ou Video O1, com vídeo na entrada | 4 imagens ou *elements* no total |
| Video 3.0 Omni ou Video O1, sem vídeo | até 7 |
| Video 3.0, com quadro inicial (ou inicial e final) | até 3 *elements* a mais |
| Condição no Video 3.0 | estar nos quadros de referência |
| Image 3.0 Omni ou Image O1 | até 10 imagens ou *elements* |
| Destaque da página | vídeo com até 7 personagens de referência; imagem, até 10 |
| Modelos que usam *elements* | Video 3.0, Video 3.0 Omni, O1 Video e Image |

## Conta, custo e partilha

| Item | Fato |
|---|---|
| *Elements* por conta, sem assinatura | 30 |
| Standard | 50 |
| Pro e Premier | 150 |
| Ultra | 500 |
| Plano que vence ou desce | *elements* existentes usáveis |
| Acima do limite do plano | sem criar nem editar |
| Criar um *element* | grátis |
| Completar vistas por IA, assinante | 3 grátis por dia; depois 5 créditos cada |
| Completar vistas por IA, sem assinatura | 5 créditos cada |
| Partilhar o *element* no Explore | não |
| Partilhar o vídeo feito com ele | sim; recriável por outros com um clique |

## O que a fonte recomenda

Subir uma imagem de frente como principal e até três de outros ângulos ou detalhes, descrever o que fixar e o que ignorar, e, quando a cena parte de um quadro inicial no Video 3.0, prender a ele os *elements* que aparecem nesse quadro.

## Citações

- "Each element must contain at least 2 reference images [...] and can include up to 4 reference images" (tipos de *element*)
- "It is recommended to bind elements that appear in the start frame." (Video 3.0)
- "Features you want the model to ignore during generation" (o que a descrição deve trazer)

## Lacuna

A página não mede a consistência que promete, não diz se o personagem desenhado se comporta como o realista, não dá o preço da geração com *elements* e não trata do Kling 4.0.
