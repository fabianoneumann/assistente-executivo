---
titulo: "The FreeMoCap Project (README do repositório freemocap/freemocap)"
tipo: artigo
autor: "FreeMoCap (mantenedores no README: Jon Matthis e Endurance Idehen)"
url: "https://github.com/freemocap/freemocap"
publicado_em: null   # o README não traz data, e o HTML lido não traz a data do último commit
capturado_em: 2026-11-12
licenca: "repositório AGPL-3.0; a licença do texto do README não está declarada à parte; tratado como protegido: ficha sem o integral"
areas: [generative-media]
tags: [freemocap, motion-capture, markerless, open-source, agpl, dual-licensing, python, cuda]
---

# FreeMoCap: captura de movimento livre e de código aberto, em AGPL, com outra licença paga a combinar

Nota de fato: tabelas do que o README do repositório diz sobre o projeto, a instalação e a licença, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a licença do texto do README não está declarada.

**Proveniência.** Página do repositório https://github.com/freemocap/freemocap, baixada em HTML com `curl` em 2026-11-12 e lida no texto extraído do bloco principal, conferido no HTML (o README renderizado, os selos e a barra lateral). O sha256 (hash omitido) é o do texto do `<main>`/`<article>` sem tags, script e estilo, não o do HTML inteiro. Wayback: `http://web.archive.org/web/20261028141746/https://github.com/freemocap/freemocap`. Título conferido: o título do HTML é "GitHub - freemocap/freemocap: Free Motion Capture for Everyone 💀✨ · GitHub", e o README abre o texto padrão com "The FreeMoCap Project". Texto dos próprios mantenedores, sobre o projeto deles.

**Cobertura.** O README inteiro, na ramificação `main` (commit (hash omitido)): as instruções especiais da ramificação `development`, o quickstart, a instalação pelo código, a documentação, a contribuição, os mantenedores e a licença; e a barra lateral da página (descrição, site, licença, números). A seção "Related" está vazia na página lida. O arquivo LICENSE, o CONTRIBUTING.md, a documentação e o vídeo de demonstração não foram abertos. Formato: nota de fato, porque é documentação de software curta (cerca de 650 palavras com a lista de arquivos).

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2, contra o texto extraído `leitura/freemocap-github.txt`). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês), com 30 unidades medidas (21 de prosa, 9 de célula com texto), 0 coladas e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 30 unidades, segue a fonte a que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela; a célula que só traz nomes de arquivo e a frase que junta partes distantes do README não contam. Resultado: 11 de 30 (as duas frases dos passos 1 e 2 do quickstart, oito células com texto e a segunda frase da recomendação, que verte a oferta de outra licença); nenhuma das outras 18 frases de prosa (proveniência, esta conferência, "Em uma frase", a primeira frase da recomendação e a lacuna) segue a fonte. A maior sequência de unidades seguidas que seguem a fonte, na ordem dela, é de 4 (os passos 1 e 2 do quickstart e as duas células da instalação pelo código sobre as dependências e o `uv sync`), em método de instalação, não em texto argumentativo; não há trecho colado no texto que recomenda ou conclui.

## Em uma frase

README dos mantenedores do FreeMoCap: um sistema de captura de movimento gratuito e aberto, que se diz independente de hardware e de software, de custo mínimo e de nível de pesquisa, instalado pelo `pip` com o rastreador para GPU NVIDIA ou só CPU, sob a AGPL, com a oferta de outra licença paga para quem a AGPL não serve.

## O projeto

| Ponto | Fato |
|---|---|
| Descrição no README | sistema e plataforma de captura de movimento livre e aberto, independente de hardware e de software, de custo mínimo, de nível de pesquisa |
| Para quê | pesquisa científica descentralizada, educação e treinamento |
| Descrição na barra lateral | "Free Motion Capture for Everyone" |
| Site | freemocap.org |
| Documentação | freemocap.github.io/documentation, feita com Writerside a partir do repositório freemocap/documentation |
| Mantenedores | Jon Matthis; Endurance Idehen |
| DOI | 10.5281/zenodo.7233714 (Zenodo) |
| Citação | o repositório tem CITATION.cff e references.bib |
| Commits na `main` | 1.437 |
| Estrelas; observadores; forks | 10,8 mil; 128; 1,0 mil |
| Estado declarado | em andamento; "pode quebrar" |

## Instalar pelo pip (quickstart)

1. Criar um ambiente com Python 3.9 a 3.11 (o README recomenda o 3.11).
2. Instalar com o extra obrigatório: `pip install freemocap[cuda]` no Windows ou Linux com GPU NVIDIA, ou `pip install freemocap[cpu]` no macOS e nas máquinas sem GPU compatível; sem o extra, o pacote vem sem o rastreador.
3. Rodar `freemocap` para abrir a interface gráfica.
4. Contar no Discord como foi.

## Instalar pelo código

| Ponto | Fato |
|---|---|
| Gerenciador | uv |
| Por que não conda com `pip install -e .` | as dependências (skellytracker, skellycam e outras) vêm de repositórios git privados pelo uv |
| Passos | clonar; `uv venv`; `uv sync` |
| `uv sync` | escolhe sozinho a versão do rastreador: com GPU NVIDIA em Windows e Linux, só de CPU em macOS |
| Sem GPU compatível | `uv sync --no-default-groups --group cpu` |
| Servidor | `uv run python freemocap/__main__.py`, em http://localhost:8005 |
| Interface | React e Electron, com Node.js: em `freemocap-ui`, `npm install` e `npm run dev` |

## A ramificação `development`

| Ponto | Fato |
|---|---|
| Onde fica no README | no topo, antes do texto padrão |
| Trocar de ramificação | `git switch development` |
| Ativar o ambiente | o README escreve `.venv/bin/activate` para o Windows e `source .venv/bin/activate` para Mac e Linux |
| Servidor | `python freemocap/__main__.py`, em http://localhost:8005 |
| Gerar o aplicativo | `npm run build` em `freemocap-ui`; sai na pasta `releases` |
| Limite da geração | desnecessária para desenvolver; ainda não inclui o servidor Python |

## Licença

| Ponto | Fato |
|---|---|
| Na barra lateral | AGPL-3.0 |
| No selo | AGPLv3 |
| No texto da seção | "APGL License", com remissão ao arquivo LICENSE |
| Outra licença | os mantenedores se dispõem a negociar outro acordo para quem a AGPL não serve |
| Preço da outra licença | não dado; o texto diz que cresce "exponencialmente" quanto mais o uso se afasta "espiritualmente" da AGPL |
| Link no "espiritualmente" | o ensaio da GNU "Open Source Misses the Point" |

## O que a fonte recomenda

Para usar, o caminho é o `pip` num Python 3.11, escolhendo o extra de GPU ou de CPU conforme a máquina; para mexer no código, o uv, porque as dependências privadas não instalam por conda. Quem não pode seguir a AGPL deve procurar os mantenedores para outra licença.

## Citações

- "freemocap requires the cuda or cpu extra to be specified" (Quickstart)
- "If the AGPL does not work for your needs, we are happy to discuss terms to license this software to you with a different" (License)
- "Have fun! It might break! Work in Progress lol" (Quickstart, passo 4)

## Lacuna

O README não diz quantas câmeras são precisas nem de que tipo, como se calibram, que precisão o sistema alcança, em que formatos exporta (BVH, FBX, arquivo do Blender) nem que requisitos de hardware tem além da GPU NVIDIA opcional. Não diz se a AGPL alcança os dados de movimento capturados com o programa, quanto custa a outra licença nem qual é a versão atual e a data dela; a página lida não traz a data do último commit.
