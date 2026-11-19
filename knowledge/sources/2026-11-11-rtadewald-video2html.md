---
titulo: "video2html (rtadewald/skills): SKILL.md e scripts/motion_map.py"
tipo: artigo
autor: "Rodrigo Tadewald (usuário rtadewald no GitHub; nome no perfil: Rodrigo Soares Tadewald)"
url: "https://github.com/rtadewald/skills/tree/main/video2html"
publicado_em: 2026-11-09   # último commit que mudou a pasta video2html (03151b4e2c, 18:22 UTC)
capturado_em: 2026-11-11
licenca: "protegida: repositório público sem arquivo de licença (gh api repos/rtadewald/skills: private false, license null; contents/LICENSE dá 404), logo todos os direitos reservados. Ficha do método em palavras próprias, sem trechos de código"
areas: [generative-media]
tags: [video2html, video-to-code, motion-analysis, image-to-3d, claude-code-skills, ui-animation, three-js, no-2-5d, openrouter, fal]
---

# video2html: refazer em código uma tela animada a partir do vídeo e da imagem (Rodrigo Tadewald, versão de 11/11/2026)

Nota de fato: tabelas do que a skill e o script fixam e os passos do método numa lista, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Sem trechos de código: o repositório não tem licença.

**Proveniência.** Dois arquivos do repositório público `rtadewald/skills` no GitHub, baixados em 11/11/2026: `video2html/SKILL.md` (id `rtadewald-video2html-skill`, https://github.com/rtadewald/skills/tree/main/video2html) e `video2html/scripts/motion_map.py` (id `rtadewald-video2html-motion-map`, https://github.com/rtadewald/skills/blob/main/video2html/scripts/motion_map.py). Conferidos com `gh api` (só leitura): o hash git de cada arquivo baixado é o do `main` em 11/11/2026 (`SKILL.md` `df8338f2a0`, `motion_map.py` `e93d46c758`), cujo último commit é o `03151b4e2c`, de 09/11/2026. O texto lido é, portanto, o de 11/11/2026. Os outros arquivos da pasta (as referências em `references/`, o `templates/character.html`, os demais scripts) não foram lidos; aparecem aqui só pelo nome.

**Quem fala.** O autor da skill, que escreve as instruções para um agente de código. O nome vem do perfil do GitHub e do autor dos commits.

**Licença.** O repositório é público e não tem arquivo de licença: `gh api repos/rtadewald/skills` devolve `license: null`, e `contents/LICENSE` e `/license` dão 404. Por isso a ficha descreve o método e não copia código; nomes de arquivo, de opção e de constante e os valores aparecem como estão.

**Histórico da pasta `video2html`** (`gh api repos/rtadewald/skills/commits?path=video2html`; datas em UTC; o repositório foi criado em 29/08/2026):

| Commit | Data | Mensagem | O que mudou na pasta |
|---|---|---|---|
| `1bb97bd1f2` | 2026-10-24 14:09 | "feat: add video2html skill (imagem + vídeo → HTML vivo)" | cria a pasta: `SKILL.md`, `README.md`, `references/vida.exemplo.md` e scripts com nomes em português (`analisar_video.py`, `caminhos.py`, `comparar_movimento.py`, `comparar_quadro.py`, `gravar.py`, `isolar_camada.py`, `mapa_movimento.py`) |
| `82fe5edfeb` | 2026-10-30 14:27 | "Adicao da img2html" | a primeira versão vai para `video2html-backup/` (os scripts em português são renomeados para lá) e entra a versão atual: `SKILL.md` reescrito, `references/` (`categories.md`, `character-3d.md`, `phase2.md`, `pitfalls.md`, `plan.md`), `templates/character.html`, `agents/openai.yaml` e os scripts em inglês; o `motion_map.py` nasce neste commit |
| `03151b4e2c` | 2026-11-09 18:22 | "Adição da skill draw-wireframe" | muda `SKILL.md`, `references/categories.md` e `references/plan.md` |

**Pastas vizinhas.** Na raiz do repositório existem também `img-to-html/`, `img2html/` e `video2html-backup/`. A ficha não lê o conteúdo delas, só as datas, pelo mesmo comando trocando a pasta (`gh api repos/rtadewald/skills/commits?path=img-to-html` e `?path=img2html`, consultado em 11/11/2026, datas em UTC): o `img-to-html` tem sete commits, do `1ff0376e53` (2026-08-31 01:27, "Tentativa de versao 2.0 (claude) no img-to-html") ao `d9861532a3` (2026-09-17 21:08, "Atualização do img-to-html"); o `img2html` tem dois, o `82fe5edfeb` (2026-10-30 14:27, "Adicao da img2html") e o `03151b4e2c` (2026-11-09 18:22, "Adição da skill draw-wireframe").

**Cobertura.** O `SKILL.md` inteiro e o `motion_map.py` inteiro.

Condensada em nota de fato em 2026-11-11, depois de três reescritas em prosa que seguiam a fonte.

**Conferência lado a lado** (2026-11-11, na condensação, pela régua de 2026-11-11 do `README.md` desta pasta, item 2): contam as frases de prosa e as células com texto corrido; a célula que só traz um fato (número, nome, comando, flag, valor ou rótulo curto) fica fora, como as marcas "—" e "não informado". Corpo: 6 frases de prosa, 20 passos numa lista e 314 células de dados em 12 tabelas, todas de fato; as 25 que trazem verbo foram lidas uma a uma contra o `SKILL.md` e o `motion_map.py`, e cada uma guarda um fato só. As duas frases da recomendação juntam ideias de quatro a cinco lugares do `SKILL.md`. Os passos seguem a ordem do `SKILL.md`, porque a ordem é o método; cada um é rótulo de até uma linha, sem frase da fonte, e nos passos 12 a 19 o rótulo fica perto do rótulo da própria fonte, que já é curto. Resultado: 0 das 6 frases seguem a fonte; dos 20 passos, nenhum traz frase da fonte, e os 8 da fase 2 retomam o rótulo dela; as três citações literais estão à parte. A versão anterior, pela mesma régua, dava 45 a 48 de 51 (re-revisão do Passo 7).

## Em uma frase

Skill de Rodrigo Tadewald que faz a engenharia reversa de uma tela de aplicativo animada por um modelo de vídeo até ela virar página em código, com um script próprio de mapa de movimento; para a base, é a referência de método (só de método, porque o repositório não tem licença) do caminho em que o vídeo gerado serve de rascunho de movimento para uma cena feita em código.

## Entrada e saída

| Item | Fato |
|---|---|
| Entrada | vídeo curto de tela de aplicativo animada |
| Duração típica | 5 a 10 s |
| Origem típica do vídeo | modelo de vídeo |
| Segunda entrada | o quadro parado de onde o vídeo partiu |
| Sem o quadro | primeiro quadro do vídeo |
| Saída | pasta com `index.html` vivo |
| Interação na saída | cursor e clique, além do que o vídeo mostra |
| Partes paradas | HTML, CSS, SVG |
| Partes em movimento | SVG com GSAP; shaders; partículas; Three.js |
| Personagem | modelo 3D por conversão de imagem em 3D |
| Gatilho | menção a video2html; pedido de vídeo de interface em HTML |

| Fonte | Autoridade |
|---|---|
| Quadro parado | conteúdo: disposição, textos, cores, tamanhos |
| Motivo da autoridade do quadro | mais nítido que o vídeo |
| Vídeo | movimento: o que se mexe, como, quando |
| Invenções do modelo de vídeo | artefatos (texto que derrete, rótulo que muda, objeto que pisca) |
| Destino dos artefatos | listados no plano; nunca reproduzidos |
| Comportamento da página | do vídeo e por inferência |
| Exemplo de inferência | nó que acende no vídeo acende também no cursor ou no clique |

## Os passos do método

1. Pasta de saída: a do usuário ou `video2html/<slug>/`; quadro em `reference.png`, vídeo em `analysis/video.mp4`.
2. Quadro em tamanho real, lido por regiões.
3. Folha de contato do `ffmpeg` (grade 4 × 3, 2 quadros/s, 640 px), vista com o primeiro quadro.
4. `motion_map.py` com `--ref-width` igual à largura do quadro.
5. Opcional e pago: texto do `describe_motion.py`, a partir das regiões do mapa.
6. Cada elemento numa das cinco categorias, com a técnica mais leve que fique fiel.
7. Plano no chat, no formato de `references/plan.md`.
8. Parada 1, para o ok do plano.
9. Fase 1: a peça de risco sozinha, numa página, na posição e na escala do quadro.
10. Personagem: imagem limpa, conversão em 3D em vários modelos ao mesmo tempo, o mais parecido, esqueleto no Blender, página Three.js.
11. Parada 2, em `phase1/index.html`.
12. Fase 2, sem consultas: fundo (cores, degradês, textura de base).
13. Blocos e textos reais; família e peso da fonte antes do tamanho.
14. Componentes um a um, ainda parados.
15. Ícones todos juntos, SVG embutido, traço uniforme.
16. Camadas vivas leves (SVG animado, shaders, partículas).
17. Peça da fase 1 encaixada, sem reabrir.
18. Interação e movimento: o do vídeo, mais cursor, clique e laço de repouso.
19. Revisão final: captura inteira contra o quadro; gravação contra o vídeo.
20. Parada 3, com a entrega.

| Regra da sequência da fase 2 | Fato |
|---|---|
| Ordem | fixa, a mesma para todo vídeo |
| Dependência | cada passo se apoia nos anteriores |
| Passo pulado | só o que o plano deixa vazio |
| Detalhe e formato do diário | `references/phase2.md` (não lido) |

| Conferência de cada passo | Fato |
|---|---|
| Captura | `snap.py`, sem janela visível |
| Comparação | `compare.py`, recorte do passo contra o mesmo recorte do quadro |
| Medidas da comparação | posição, tamanho, cor, peso, brilho |
| Teto de rodadas | 3 |
| Diferença que sobra | anotada |
| Trabalho, com diferença anotada | segue |
| Registro | linha no `steps.md`: `ok` ou a diferença |
| Imagem no registro | o lado a lado |

## Paradas e regras

| Ponto | Fato |
|---|---|
| Perguntas ao usuário | 3, no máximo |
| Entre as paradas | nenhuma pergunta |
| O que se mostra na parada | caminho e captura |
| Condição para seguir | ok explícito ("ok", "approved", "go on") |
| Pedido de mudança | não conta como ok |
| Depois da mudança | nova parada |
| Regras do projeto (`AGENTS.md` ou `CLAUDE.md`) | lidas antes do plano |
| Alcance das regras do projeto | todos os passos e paradas, junto com a skill |
| Plano, tamanho | julgável em um minuto |
| Plano, forma | uma linha por elemento: o que é e com que técnica |
| Plano, cobertura | todo elemento visível, inclusive fundo e ícones |
| Plano, conteúdo | peça da fase 1; ordem das camadas; artefatos a ignorar |
| Ordem das camadas | de trás para a frente, decidida no plano |
| Falha de integração mais comum, para o autor | sobreposição errada |
| Categorias | Media, DOM, Particles, Shader, 3D model (`references/categories.md`, não lido) |
| Peça de risco | tecnologia cara ou incerta |
| Exemplos de peça de risco | modelo 3D; shader pesado; simulação na GPU |
| Peças de risco por vídeo | em regra uma |
| Duas peças de risco | uma depois da outra, cada uma com aprovação |
| Sem risco (só DOM e SVG) | fase 1 dispensada |
| Dispensa da fase 1 | registrada no plano |
| Receita de personagem | `references/character-3d.md`, a partir de `templates/character.html` (não lidos) |
| Receita de shader e partículas | `references/categories.md` |
| Régua da fase 1 | pose de repouso do quadro |
| O que deve bater | desenho, ângulo, detalhes que distinguem o sujeito |
| Estilo parecido | não basta |
| Página da fase 1 | peça no lugar sobre o quadro escurecido |
| Tecla na página da fase 1 | alterna o quadro |
| Comportamentos na fase 1 | já rodando (seguir o cursor, falar, respirar) |
| Alcance do ok da fase 1 | modelo, movimento e encaixe |
| Laço de repouso | função que as interações também chamam |
| Entrega final | endereço da página; lado a lado em tela cheia; gravação curta; diferenças do `steps.md` |

| Vetado | Fato |
|---|---|
| Paralaxe entre recortes em camadas | vetada |
| Deslocamento por mapa de profundidade | vetado |
| CSS 3D sobre imagem | vetado |
| Sprite sheet | vetada |
| Alcance do veto | plano, sugestão ao usuário e plano B |
| Objeto com volume (personagem, robô, mascote, produto) | modelo 3D: GLB com esqueleto, animado no Three.js |
| Conversão em 3D falha em todos os modelos | parar e avisar o usuário |
| Framework | vetado |
| Etapa de build | vetada |
| Peça da fase 1 na fase 2 | só encaixada |
| Chaves | nunca impressas |

## Pasta, pilha, chaves e ferramentas

| Caminho na pasta de saída | Conteúdo |
|---|---|
| `reference.png` | o quadro (referência de conteúdo) |
| `index.html` | só marcação |
| `assets/styles.css` | todo o CSS, variáveis em `:root` |
| `assets/app.js` | todo o JS, módulo ES |
| `assets/` | GLB, texturas, áudios de voz |
| `phase1/` | página e arquivos da fase 1 |
| `analysis/` | `video.mp4`, `sheet.jpg`, `motion/`, `motion.md` |
| `review/` | capturas e comparações, uma por passo |
| `steps.md` | diário da fase 2 |

| Ativos gerados | Fato |
|---|---|
| Quais | placas, recortes limpos do sujeito, texturas, modelos 3D |
| Modelos 3D guardados | todos, com o escolhido marcado |
| Com registro de ativos no projeto (biblioteca, canvas de nós, CLI) | cada um registrado ao nascer |
| Anotação no registro | uso e procedência |
| Cadeia de procedência | vídeo → imagem limpa → modelo → página |
| Sem registro | na pasta, com linha no `steps.md` ou em `phase1/notes.md` |

| Pilha | Fato |
|---|---|
| Linguagens | HTML, CSS e JS puros |
| Build | nenhum |
| Framework | nenhum |
| Bibliotecas | CDN, versão travada |
| Exemplo do Three.js | `three@0.170.0`, jsDelivr |
| Exemplo do GSAP | `gsap@3.12.5`, cdnjs |
| Servir | `http://`, com `python3 -m http.server` |
| `file://` | não serve |
| Motivo | WebGL com arquivo local |
| Palco | fixo, do tamanho do quadro, escalado à janela |
| Palco do exemplo | 1536×864 |
| Medidas tiradas do quadro | valem sem conversão |

| Chave ou ferramenta | Uso |
|---|---|
| `OPENROUTER_API_KEY` | geração de imagem; descrição do vídeo |
| `FAL_KEY` | conversão de imagem em 3D |
| Onde as chaves são procuradas | ambiente, `./.env`, `~/.env` |
| Custo citado da descrição do vídeo | centavos |
| `uv` | executor de cada script |
| Dependências dos scripts | declaradas no próprio script |
| `ffmpeg`, `ffprobe` | vídeo |
| Google Chrome | capturas sem janela |
| Blender 4 ou mais novo | esqueleto dos modelos |
| Scripts nomeados no `SKILL.md` | `snap.py`, `compare.py`, `motion_map.py`, `describe_motion.py`, `isolate_subject.py`, `image_to_3d.py`, `render_views.py`, `extract_emissive.py`, `rig_bust.py` |
| Script na pasta e fora do `SKILL.md` | `apply_template.py` |

| Armadilha (`references/pitfalls.md`, não lido, se lê antes da fase 1) | Efeito | Contorno |
|---|---|---|
| Aba escondida | pausa o `requestAnimationFrame` | conferir pelo `snap.py` |
| Bloom | apaga a transparência do canvas | brilho num segundo canvas, com `mix-blend-mode: screen` |
| Canvas WebGL | é uma camada | lugar decidido e `pointer-events: none` |
| Modelo de imagem editando | move e redimensiona o sujeito | realinhar a saída à referência |

## O motion_map.py

| Item | Fato |
|---|---|
| Mede | onde, quanto, quando |
| Não mede | o quê nem como |
| Para o quê e o como | olhar os quadros ou o `describe_motion.py` |
| Requisitos | Python 3.11+; numpy, scipy, pillow |
| Leitura do vídeo | `ffmpeg`, em tons de cinza |
| Taxa de análise | 15 quadros/s, fixa |
| Resolução de análise | 480 × 270 (constantes `W, H`, anotadas como 16:9) |
| Proporção do vídeo de entrada | ignorada no redimensionamento |
| Opção para outra resolução | nenhuma |
| Variação de cada pixel | desvio padrão no tempo |
| Repouso de cada pixel | mediana dos quadros |
| `--threshold` | 0,18 da maior variação da tela |
| Junção de vizinhos | dilatação (ex.: feixe de luz e o nó onde chega) |
| Agrupamento | regiões contíguas |
| `--min-area` | 40 px, na resolução de análise |
| Região grande | acima de 12% da área em movimento |
| Divisão da região grande | pelo instante de pico de cada pixel |
| `--split` | 0,8 s; 0 desliga |
| `--merge` | correlação acima de 0,7 junta pedaços vizinhos |
| Exemplo de junção | anel que brilha inteiro |
| Exemplo de separação | feixes que disparam em tempos diferentes |
| `--ref-width` | 1536, padrão |
| Caixa | na escala da imagem de referência |
| Fator de escala da caixa | `--ref-width` / 480 |
| Área | pixels da região, na resolução de análise |
| Intensidade | variação média da região |
| Pico | quadro mais longe do repouso |
| Janela ativa | atividade acima do meio entre o mínimo e o máximo |
| Período | autocorrelação da curva de atividade |
| Defasagem mínima do período | 0,4 s |
| Pico mínimo da autocorrelação | 0,35 |
| Sem repetição | período vazio |
| Curva de atividade | 5 amostras/s |
| Ordem das regiões | intensidade × área |
| Nomes | `r01`, `r02`… |
| `motion.png` | mapa de calor sobre o primeiro quadro, 960 × 540, caixas numeradas |
| `regions.json` | regiões, duração, taxa de análise, largura de referência |
| `curves.png` | curva de cada região no tempo |
| `frames/` | quadro de pico de cada região; folha 3 × 3 do vídeo |
| Terminal | uma linha por região (caixa, intensidade, pico, período, primeiras janelas) |

## O que a fonte recomenda

Decidir quem manda em quê antes de escrever código (o quadro na aparência, o clipe no movimento, o modelo de vídeo em nada) e fixar cedo a ordem das camadas e a peça mais arriscada, que se resolve sozinha e aprovada. Daí em diante a página cresce do parado para o vivo, cada passo conferido contra o quadro por imagem e por número, e a profundidade fingida nunca entra, nem como plano B.

## Citações

- "No 2.5D, ever."
- "They look cheap as soon as anything moves."
- "It does not know WHAT moves or HOW"

## Lacuna

O `SKILL.md` não diz que modelo de vídeo gera a entrada, que modelos o `describe_motion.py` e a conversão em 3D usam, nem quanto custa a conversão em 3D. Não trata de vídeo vertical: o palco do exemplo é horizontal, e o `motion_map.py` analisa sempre em 480 × 270. As receitas, as armadilhas completas, as categorias e o formato do plano estão em `references/`, que não foi lido, e o repositório não diz desde quando é público.
