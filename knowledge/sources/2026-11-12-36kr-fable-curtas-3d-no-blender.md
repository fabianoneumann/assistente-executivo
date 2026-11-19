---
titulo: "Fable 5.2生视频也火了，一句话生成3D短片，建模、运镜、渲染全包"   # <title> da página, sem o sufixo "-36氪"
tipo: artigo
autor: "机器之心 (conta de WeChat almosthuman2014), republicado pelo 36Kr com autorização"   # nota no fim do texto; o campo de autor ali diz "关注视频生成的"
url: "https://36kr.com/p/4065250990167170"
publicado_em: null   # o texto lido não traz data: diz só que o Fable 5.2 e o Mythos 5.2 saíram "昨天" (ontem); o rótulo da rodada também não leu data na página
capturado_em: 2026-11-12
licenca: "protegido (republicação autorizada do 机器之心 no 36Kr, '36氪经授权发布'; sem licença de conteúdo no texto lido); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [claude, fable-5-2, opus-5-5, blender, threejs, video-as-code, 3d-world, short-film, cloud-rendering, runpod, elevenlabs, claude-motion, remotion, motion-graphics, news, reporting]
---

# 36Kr (机器之心): o Fable 5.2 e o vídeo feito por código com o Claude

Nota de fato de reportagem: tabelas do que a matéria relata, com prosa só para dizer o que a fonte é, o que ela afirma e o que falta. Não há integral: a matéria é protegida.

**Proveniência.** Matéria do 机器之心 republicada pelo 36Kr, https://36kr.com/p/4065250990167170, lida pelo Chrome em 2026-11-12 (o curl recebeu só a página de verificação de segurança do site, que é o que ficou na cópia de trabalho); a ficha saiu da captura do texto pelo Chrome, em chinês; sha256 da captura (hash omitido); sem captura na Wayback. Título conferido na captura (o `<title>` da página). Lido o texto inteiro da matéria, com os links que ela traz para posts do X e para o índice Claude Video; nenhum desses links foi aberto a partir daqui, nem os vídeos assistidos. **Data:** o texto lido não traz data de publicação; diz que o lançamento do Fable 5.2 e do Mythos 5.2 foi "ontem", sem dizer o dia.

**Quem fala.** Uma reportagem que relata posts de terceiros (criadores no X e no Reddit) e afirmações de pesquisadores da Anthropic em redes sociais, sem medida própria; o que os criadores contam vem atribuído a eles.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). O `parafrase.py` contra a captura do texto em chinês saiu com o código 0, não com o 3 esperado para ficha e fonte em línguas diferentes: o script só lê palavras em alfabeto latino para decidir a língua e classificou a fonte em chinês como português, então o 0 não quer dizer "passou", e a conta lado a lado é a conferência. Cabeçalho da saída: 42 unidades medidas (20 de prosa, 22 de célula com texto); fora da conta, 62 células de fato, 10 de cabeçalho e 10 frases curtas demais para medir; 2 coladas de 42 (5%: as duas listas de nomes de ferramentas, em letras latinas na fonte); 0 trecho de 3 ou mais seguidas. Pela conta lado a lado, sobre as mesmas unidades, 23 de 42 seguem a fonte: o "Em uma frase", o ângulo, as células com texto dos casos (o curta de Riley Brown e os outros) e do método, e a primeira frase do que a fonte afirma, que junta lugares diferentes da matéria. A maior sequência de unidades seguidas que seguem a fonte tem 10 (do "Em uma frase" ao curta do Reddit de 22 de setembro), em relato de fatos na ordem da matéria; no texto argumentativo dela (a diferença para os modelos de vídeo, as vantagens, onde cada um está maduro), as linhas da tabela vão em ordem trocada, sem três unidades seguidas que andem para a frente. Ficam fora da conta de "segue" a proveniência, esta linha, as duas listas de ferramentas, os rótulos das citações, a segunda frase do que a fonte afirma e a lacuna.

## Em uma frase

Reportagem que parte do curta 3D de Riley Brown feito com o Fable 5.2 no Blender e reconstitui a onda de vídeos gerados por código com o Claude desde setembro, explicando como o modelo produz vídeo e onde isso fica atrás dos modelos de vídeo especializados.

**Ângulo da matéria:** o vídeo feito por código com o Claude como fenômeno que cresce do Opus 5.5 ao Fable 5.2, posto ao lado dos modelos de vídeo especializados e fechado com a pergunta se eles terão o próprio "苦涩的教训" (a "lição amarga").

## O curta de Riley Brown, pela matéria

| Item | Fato |
|---|---|
| Lançamento citado | Claude Fable 5.2 e Claude Mythos 5.2, "ontem" |
| Autor do curta | Riley Brown, desenvolvedor, no X |
| Nome do curta | 《The Edge》 |
| Cena | mesa de trabalho; MacBook com a tela acesa; o mascote lagosta do Claude, Clawd |
| Céu na janela | do entardecer à noite, depois o nascer do sol |
| Planos | 13 |
| Duração | cerca de 59 s |
| Instrução | uma só, ao vivo, pelo que Riley disse |
| O que o modelo fez | escreveu o código do Blender; modelou mesa, notebook, luminária e personagem; arranjou os movimentos de câmera; animou os objetos |
| Render | 10 GPUs na RunPod, em 4K, 52 min |
| Custo divulgado por Riley | US$ 5,75 de render na nuvem |
| Acabamento | cor e títulos pelo modelo; trilha e efeitos com a ElevenLabs |

## Os outros casos citados

| Data | Quem | O que | Números e detalhes |
|---|---|---|---|
| — | Peter Yang, desenvolvedor | anúncio de viagem de outono ao Fushimi Inari, em Quioto, com o Fable 5.2 | 20 s; feito por código, com música |
| 14 de setembro | Kevin Ngo, desenvolvedor | animação desenhada quadro a quadro em JavaScript pelo Claude Opus 5 | — |
| depois | um desenvolvedor, com o Claude Code | réplica do estilo Risograph | cerca de 3.500 linhas de Canvas 2D; um HTML só; 26 cenas ilustradas; música sintetizada com WebAudio |
| 22 de setembro | Anthropic | lançamento do Opus 5.5 | — |
| 22 de setembro | AzorAhai1TK, no Reddit | curta de terror surreal sobre um dia comum de trabalho, imagem e som programados, ferramentas à escolha do modelo | cerca de 1 min; 45 min no modo de raciocínio Extra-High, render incluído, pelo autor; NumPy, SciPy, Cairo, Piper TTS, FFmpeg |
| 24 de setembro | um usuário do Reddit | batalha em estilo de jogo de SNES, com o Opus 5.5 coordenando vários agentes (personagem, cenário, música, animação da luta) | sem material pronto, pelo autor; duas ou três rodadas de ajuste, confirmadas por ele nos comentários |
| mesmo período | @IterIntellectus, no X | história da civilização ocidental em linhas preto e ouro e gráficos animados (Grécia, Roma, Renascimento, Revolução Industrial) | 2 min 16 s; 5,8 milhões de visualizações em cerca de 24 h; mais de 15 milhões depois; uma instrução só, pelo autor |

| Índice Claude Video (claudevideo.org, terceiro) | Valor |
|---|---|
| Vídeos feitos com o Opus 5.5 | 1.276 |
| Autores | 1.007 |
| Com a instrução pública | 457 |
| Visualizações somadas no X, pela conta do site | cerca de 78,9 milhões |

## Como o Claude faz vídeo, pela matéria

| Ponto | Fato |
|---|---|
| Linguagens e ferramentas | HTML, CSS, JavaScript, SVG, Canvas; Three.js para cena 3D; Blender para modelar e renderizar |
| Exemplo dado | propaganda de produto de 15 s |
| Ordem do exemplo | planejar planos e linha do tempo; escrever o código que controla texto, gráficos, câmera e transições |
| Como sai cada quadro | calculado pelo programa a partir do tempo |
| Exportação para MP4 | gravação do navegador, motor de render ou FFmpeg |
| Cena 3D complexa | script Python do Blender que cria modelos, materiais, luzes e câmera e renderiza na GPU |
| Capacidades em jogo | programação, raciocínio espacial, planejamento de tarefas, uso de ferramentas |
| Remotion | plugin para o Claude Code, para criar e editar projetos de vídeo em linguagem natural |
| Claude Motion | beta lançado pela Anthropic em 8 de outubro; anima texto, gráficos e figuras e exporta MP4; para os planos Team e Enterprise |
| Onde o vídeo por código está mais maduro | motion graphics, visualização de informação, demonstração de produto, divulgação técnica, animação 3D estilizada |
| Vantagens listadas | posição exata de texto, número e gráfico; cena e linha do tempo editáveis de novo; interface de produto, diagrama técnico e gráfico animado por código estruturado |
| Onde os modelos de vídeo seguem com vantagem | pessoa muito realista, movimento natural complexo, plano contínuo de cinema |
| Diferença para Veo e Runway | a imagem vem de cálculo e render de programa, não da geração dos modelos de vídeo |
| Robótica | pesquisadores da Anthropic, em redes sociais, sobre a manipulação de robôs do Fable 5.2 |

## O que a fonte afirma

A matéria trata o curta de Riley Brown como o ponto mais recente de uma sequência que começou em setembro com o Opus 5 e o Opus 5.5, mede o alcance dela por visualizações e por um índice de terceiro, e separa o vídeo por código, em que cada quadro é calculado e renderizado por programa, da geração dos modelos de vídeo, dando a cada um o seu terreno. Os números de tempo, custo e tentativas vêm do que cada criador disse, sem medida da própria matéria.

## Citações

- Riley Brown, pela matéria: "Riley 表示，他在直播中只给 Fable 5.2 提供了一条提示词。"
- O autor do vídeo de SNES, no Reddit, pela matéria: "作者称没有提供现成素材，但在评论中确认，制作过程中进行了两三轮修改。"
- Pesquisadores da Anthropic, em redes sociais, pela matéria: "机器人领域的「苦涩的教训」或许已经到来"

## Lacuna

O texto lido não traz a data de publicação nem o dia do lançamento do Fable 5.2. Não diz como a duração de cerca de 59 s foi obtida, nem a versão do Blender, o motor de render, o modelo das GPUs ou a taxa de quadros do curta de Riley Brown, nem se os US$ 5,75 incluem algo além do render. Não nomeia o desenvolvedor da réplica Risograph nem o usuário do vídeo de SNES, não dá a data do anúncio de Peter Yang nem a do plugin do Remotion, e não diz como o índice Claude Video conta vídeos e visualizações; os pesquisadores da Anthropic citados não são nomeados.
