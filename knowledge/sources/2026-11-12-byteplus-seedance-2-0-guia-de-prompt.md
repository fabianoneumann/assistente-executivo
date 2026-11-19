---
titulo: "Seedance 2.0 series prompt guide (BytePlus ModelArk)"
tipo: artigo
autor: "BytePlus (documentação oficial do ModelArk)"
url: "https://docs.byteplus.com/docs/en/modelark/seedance-2-0-prompt-guide.md"
publicado_em: null   # a página não traz data
capturado_em: 2026-11-12
licenca: "protegida: o Markdown oficial da BytePlus não declara licença (valem os termos do site); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [seedance, byteplus, character-consistency, reference-images, prompt-guide, id-drift, multi-view-reference, video-extension]
---

# Seedance 2.0: como a BytePlus manda montar a referência de personagem e o prompt

Nota de fato: tabelas do que a página registra, uma célula por fato, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida.

**Proveniência.** Guia de prompt da série Seedance 2.0 na documentação do BytePlus ModelArk, baixado na versão Markdown oficial em 12/11/2026 (1.167 linhas, `sha256` (hash omitido)), e lido inteiro no arquivo: as fórmulas básica e avançada, as seis partes da fórmula, os dois casos, as dicas, a configuração de assets, as normas de língua e de símbolo, as onze perguntas do FAQ e o apêndice de exemplos (texto, imagem, vídeo, edição, extensão). Ficaram fora os vídeos e as imagens de exemplo, que o Markdown só traz como link. Formato: nota de fato, por ser documentação técnica (`README.md` desta pasta, item 2), organizada pelo que se pergunta ao montar uma geração (o que mandar, como escrever, o que dá errado), não pela ordem da página.

**Quem fala.** A BytePlus, que vende o acesso ao modelo pelo ModelArk. A nota do topo diz que as imagens, os vídeos e os áudios de exemplo foram gerados pelos próprios modelos Seedance e Seedream.

**Data.** A página não traz data de publicação nem de atualização. O guia é da série 2.0, e não diz se vale para o 2.5.

**Conferência lado a lado** (2026-11-12, pela régua do item 2 do `README.md` desta pasta): contam as frases de prosa do corpo e as células com texto corrido; a célula que só traz um fato fica fora. Corpo: 5 frases de prosa e 5 tabelas com 20 células de 8 palavras ou mais (o critério do `parafrase.py`); 13 delas são listas de nomes, valores ou passos e ficam como fato. Resultado: 7 das 12 unidades seguem uma frase da fonte, todas células que dão um motivo ou uma causa como a página os dá (o excesso de assets, o motivo da multi-vista, a seção do apêndice, a consequência do desvio, as duas causas do rosto e a atribuição no prompt); as 5 frases de prosa juntam lugares diferentes da página. Contando as 13 listas, 7 de 25. As três citações estão à parte. O `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), e a conta lado a lado é a conferência.

## Em uma frase

Guia oficial de prompt da série Seedance 2.0, que trata as referências como peças com papel (personagem, cenário, câmera, som) e dedica a maior parte do FAQ aos defeitos de identidade e de continuidade, com os contornos que a BytePlus dá para cada um.

## As referências: quantas e quais

| Item | Fato |
|---|---|
| Função de um asset | ancorar o personagem |
| Função de um asset | fixar cenário e estilo |
| Função de um asset | dar a câmera e o ritmo |
| Função de um asset | dar emoção e timbre (áudio) |
| Total recomendado | 4 a 5 assets |
| Imagens do personagem nesse total | 1 a 2 (close do rosto, corpo inteiro) |
| Imagens de cenário | 1 |
| Vídeo de câmera | 1 |
| Áudio | 1 |
| Usar o limite inteiro de assets | não recomendado |
| Efeito de assets demais, segundo a página | o modelo perde a prioridade entre os traços; estilo em conflito; sujeito mal identificado |
| Referência de personagem que basta | close da cabeça + corpo inteiro |
| Imagem multi-vista do personagem | não recomendada |
| Onde o aviso aparece | FAQ do rosto impreciso; FAQ dos personagens duplicados |
| Motivo dado | ângulos diferentes do mesmo personagem lidos como sujeitos diferentes, piorando o desvio de identidade |
| Preferida na correção dos duplicados | foto independente de uma pessoa só |
| Desaconselhado na mesma correção | asset de três vistas ou multi-vista |
| Seção do apêndice | "Multi-perspective subject reference" |
| O que a seção diz | a série aceita referência do sujeito por várias perspectivas |
| Exemplos da seção | câmeras (Image 1 a 3); garrafa térmica; uma mulher (Image 1 a 3) |
| Imagens mostradas no exemplo da mulher | uma, no Markdown |
| Ordem das imagens | a do envio; no prompt, `Image 1`, `Image 2`... |
| Pessoas de referência, limite estável | 4 |
| Acima disso | número errado de pessoas; duplicados |
| Contorno | imagens por grupos de até 4; o vídeo a partir delas |
| Exemplo da página | 8 pessoas na referência, 9 no vídeo; o "depois": 2 imagens de grupo e imagem para vídeo |
| Vídeos de entrada (completar trilha) | até 3, somando até 15 s |

## O rosto: sintoma, causa e correção (FAQ "rosto impreciso")

| Ponto | Fato |
|---|---|
| Sintoma | aparência diferente da referência |
| Sintoma | troca de rosto no meio do vídeo (*ID drift*) |
| Consequência citada | o personagem lembra uma celebridade e é barrado na revisão |
| Causa | imagem mista: rosto, pose, figurino e detalhe numa imagem só |
| Causa | rosto pequeno na imagem mista, com peso baixo |
| Correção | um close só da cabeça, além do corpo inteiro |
| No close | sem expressão, de preferência |
| No close | sem ombro, pescoço nem fundo |
| Correção | no prompt, o rosto atribuído ao close e o figurino ao corpo inteiro |
| Correção | o asset mais exigente antes no prompt |

## O sujeito no prompt

| Regra | Fato |
|---|---|
| Molde da definição | `Define [traços] in <Image_N> as <Subject_N>` |
| Rótulo | pode ser um nome |
| Traços para definir | 2 a 3, estáticos e estáveis |
| Exemplos de traço | roupa, penteado, aparência, categoria |
| Mesmo sujeito em duas imagens | um rótulo só para as duas |
| Vários sujeitos | rótulo único e estável para cada |
| A cada menção | o mesmo rótulo |
| Sujeito sem definição prévia | `<Sujeito>@<Image_N>` |
| ID do banco de assets | não substitui o `<Image_N>` |
| Descrição | curta, sem traço contraditório |
| Relação espacial | pela imagem, de preferência |
| Contra duplicados | a imagem marcada depois de cada nome |
| Contra duplicados | restrição global no fim do prompt |
| Contra duplicados | nada de roteiro inteiro como prompt |

## O prompt: fórmula e planos

| Item | Fato |
|---|---|
| Fórmula avançada | sujeito + ação + cenário + luz e cor + câmera + estilo + qualidade + restrições |
| Camadas, segundo a página | espacial e temporal |
| Vídeo complexo | storyboard por plano (`Shot 1`, `Shot 2`...) |
| Duração por plano | não impor |
| Tempo cravado (0 a 3 s) | instável |
| Ordem dentro do plano | câmera; ação e expressão; posição; áudio |
| Ação | parte do corpo, amplitude, velocidade, força |
| Ação preferida | lenta, suave, contínua |
| Emoção | por detalhe físico |
| Câmera | termos padrão de cinema |
| Movimentos de câmera por plano | um |
| Restrições comuns | sem legenda; sem logo; sem marca d'água |
| Língua do diálogo | uma só |
| Símbolos | `()` música; `<>` efeito; `{}` diálogo; `[]` legenda |
| Extensão | diálogo num cenário só |
| Planos à parte e montados | ação e virada |
| Edição e extensão | `<Video_N>`, sem "reference" |

## Os outros defeitos do FAQ

| Defeito | Contorno |
|---|---|
| Estilo desvia para live action | palavras de estilo explícitas |
| Estilo desvia para live action | a referência convertida antes ao estilo-alvo |
| Duplicados | não se evita 100% |
| Qualidade cai a cada extensão | "modelo branco" (3D branco, sem cor, textura nem sombra) antes de estender |
| Qualidade cai a cada extensão | imagens em alta definição |
| Qualidade cai a cada extensão | poucas extensões |
| Onde a queda aparece | manchas de cor no rosto |
| Salto na emenda da extensão | −6 quadros no fim do anterior, −1 no começo do seguinte |
| Legenda não pedida | restrição no prompt |
| Legenda não pedida | referência sem texto |
| Legenda não pedida | gerar na horizontal e recortar |
| Legenda não pedida | não se evita 100% |
| Logo ou marca d'água | restrição no prompt |
| Efeito especial fora do esperado | vídeo de referência do efeito |
| Ruído no fim do vídeo narrado | gerar de novo, ou volume em rampa no fim |
| Pronúncia do chinês | homófono comum |
| Voz diferente da referência | a voz descrita no prompt |

Para a qualidade na extensão, o salto na emenda e as pessoas demais, a página diz que a correção de fundo virá em versões futuras do modelo.

## O que a fonte recomenda

Mandar poucas referências, cada uma com uma função, e o personagem em duas imagens separadas, a cabeça fechada e o corpo inteiro, com a mais exigente primeiro no prompt; amarrar cada sujeito a um rótulo fixo; e evitar as zonas que a própria página dá como instáveis, a multidão acima de quatro, as extensões em cadeia e o tempo cravado por segundo.

## Citações

- "For character references, using a headshot + full-body photo is sufficient. **Using multi-view character images is not recommended**." (FAQ, rosto impreciso)
- "the model may easily identify them as multiple different subjects, which instead worsens the ID drift issue" (mesma nota)
- "It is not recommended to use the full asset limit." (configuração de assets)

## Lacuna

A página não diz se a multi-vista que ela desaconselha é a folha numa imagem só ou também os ângulos em arquivos separados, nem como o aviso se concilia com a seção do apêndice que aceita referência por várias perspectivas. Não dá o número máximo de imagens de referência da série (só o de vídeos de entrada), não mede quanto cada medida reduz o desvio, não trata de personagem desenhado além do desvio de estilo e não diz se as regras valem para o Seedance 2.5.
