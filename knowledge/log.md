# Log da base de conhecimento

Registro só de acréscimo: ingestões, consultas arquivadas e passes de lint. O prefixo é fixo para ficar fácil de ler por máquina: `grep "^## \[" log.md | tail`.

Formato: `## [AAAA-MM-DD] <tipo> | <assunto>`, seguido de um parágrafo com o que entrou, de onde veio, a rota que funcionou quando a fonte não abriu de primeira, e o que ficou de fora e por quê. Tipos: **`setup`** (mudança na estrutura da base) · **`ingest`** (fontes novas e síntese) · **`enrich`** (aprofunda uma página existente) · **`top-up`** (atualiza os números de uma síntese) · **`nota`** (síntese de discussão, sem pesquisa de fora) · **`pauta`** (apuração da skill `story-angle` até o ângulo escolhido) · **`query`** (pergunta arquivada) · **`lint`** (passe de varredura). Tipo novo entra nesta lista na mesma operação em que é usado pela primeira vez.

## [2026-11-17] setup | a base nasce da cópia do método, sem as fontes pagas

A base nasce com a estrutura (este log, a porta de entrada, o README com os rituais e a régua de `sources/`) e com as sínteses de método de um ambiente anterior: apuração e checagem (`journalism/`), oferta e venda (`sales-and-offers/`), leitura de números (`data-analysis/`), Claude Code (`anthropic-claude/`) e avaliação, rubrica, revisão e orquestração de agentes (`agent-engineering/`). Vieram as fichas de fonte com licença registrada; as fontes sem licença registrada aparecem nas sínteses como citação simples (título, autor e endereço), e o material de curso pago não entrou. As decisões e os casos daquele ambiente ficaram de fora; das sínteses ficou a regra e o porquê.

## [2026-11-18] setup | a área software-engineering, com o kit de projeto novo

A área nasce com uma página: o desenho da skill `project-kit` (`kit-de-projeto-novo.md`), que diz de onde veio cada parte do processo de um CRM de atendimento em produção. A síntese da prática do CRM e o inventário item a item que originou o kit ficaram fora; a página do kit resume as três classes dele (processo, interação, só do projeto).

## [2026-11-18] setup | a base do modelo público

A base deste modelo público sai da anterior com a régua apertada: as fichas de fonte livre vêm só como citação simples (o título, o autor, o link e a licença), sem a ficha de estudo e sem o integral; as fichas de posts de criadores e de livros protegidos saíram, e as sínteses que se apoiavam nelas citam a fonte pela citação simples; sete fichas tiveram a citação aparada para até umas 25 palavras; três sínteses que reconstruíam o método de um curso pago saíram. A régua do público está em `sources/README.md`.

## [2026-11-19] setup | as fichas livres voltam em palavras próprias

As 180 fichas de fonte livre que tinham entrado só como citação simples voltam com a ficha de estudo em palavras próprias, sem o texto integral e sem seção de trechos copiados: o integral se lê na fonte, pelo link. Cada uma passou antes pelo `parafrase.py` contra o próprio integral: 177 voltaram (174 com a ficha em outra língua que a fonte, que o script não mede, e 3 sem trecho colado), e 3 ficaram como citação simples por trecho colado acima do limiar (a Lei 15.263/2025, a metodologia do Projeto Comprova e os artigos 8 e 46 a 48 da Lei 9.610/1998). Três citações acima de 25 palavras foram aparadas. As duas fichas dos plugins de dados da Anthropic perderam a seção de trechos integrais, e o que só estava nela foi para o corpo em palavras próprias. As fichas que seguiam a fonte frase a frase foram reescritas no trecho apontado pela conferência lado a lado.

## [2026-11-19] lint | as fichas protegidas em até três citações e o tempo de leitura em código

As fichas de obra protegida passaram pelo `conta_citacoes.py` novo da `research`, que conta as citações literais contra o teto de três da régua, e as que passavam ficaram em até três, com o resto em palavras próprias. Nas sínteses de Stories, `content-design/tempo-de-leitura-em-video.md` fecha a conta da tela com várias frases (frase a frase, não a soma, em código no `video_do_story.py`), e `content-design/stories-o-que-evitar.md` aponta as conferências novas: os adesivos, a chamada e a data do Destaque no `conferir_telas.py`, e a legenda do vídeo com voz no `video_do_story.py`.

## [2026-11-19] ingest | o método de Stories na base e a sequência de consciência e de venda

Entram `content-design/metodos-de-mercado-stories.md` e `content-design/stories-10x-dispositivos.md`, do material que o autor do método publica de graça (a página e o vídeo de vendas, podcasts e aulas abertas), em palavras próprias e com a fonte em citação simples, porque as fichas delas passam de três citações; `content-design/stories-o-que-evitar.md` volta inteiro, com as ligações ao método. Três fichas que cabem na régua (até três citações, sem integral) entram e voltam a ser ligação nas sínteses: a matéria sobre o Mosseri e o compartilhamento do próprio post nos Stories, o post de acessibilidade do Instagram e a página de acessibilidade em Stories da Universidade do Alabama. A rubrica de Stories passa à v0.3, com a sequência de consciência e de venda a testar.

## [2026-11-19] lint | o Claude Design dentro do Claude

O estado do Claude Design revisto nas páginas oficiais: dentro das conversas, do Claude Code e da aba Artifacts desde 16/09/2026, fora do beta em todos os planos desde 08/10/2026, e o site separado `claude.ai/design` fecha em 14/12/2026. A mudança está em `content-design/claude-design-vs-nano-banana.md` e na linha dela no índice da área.

## [2026-11-20] lint | mais itens no kit de projeto novo

Entraram nos modelos do `project-kit` a spec com o teste do essencial, o bloqueio, o que não pode acontecer e a alternativa descartada; a premissa e o dado de fora na discussão inicial; o passo de procedimento de `docs/` e a volta escrita antes de instalar; a lente de tela, a consequência do achado e o que se pulou no PR; a passagem entre sessões; e o `conferir_base.py` no CI do projeto. Na skill, a régua do genérico e a lista de automações (`references/automacoes.md`). O que não entrou e o porquê estão em `decisions/kit-de-projeto-novo.md`.

## [2026-11-20] lint | duas páginas reconferidas

Os padrões de esforço por modelo (o Fable 5.2 entra na linha do `medium`), o ultracode e o `effortLevel` reconferidos na documentação do Claude Code, em `anthropic-claude/niveis-de-esforco.md`; e os sinais do Instagram e a originalidade, sem mudar os três sinais, em `content-design/o-que-prediz-desempenho-instagram.md`.

## [2026-11-20] lint | duas fichas que seguiam a fonte frase a frase, reescritas

`sources/2026-11-04-agencia-lupa-politica-de-correcoes.md` e `sources/2026-11-04-aos-fatos-nosso-metodo.md` seguiam a página na ordem dela; foram reescritas em estrutura própria (quadros de casos, critérios e quem decide), com até três citações curtas, conferidas contra a captura de 2026-11-04.

## [2026-11-20] lint | a calibragem do parafrase.py, o teste de disparo das skills e as fichas em até três citações

O `parafrase.py` da `research` foi medido contra 179 fichas com veredito, e o limiar 0,7 com K 3 ficou (o `calibra_parafrase.py` mede de novo); as skills ganharam os casos do teste de disparo (`evals/disparo.json`), e as descrições da `research` e da `review` cobrem mais pedidos; várias fichas de obra protegida desceram a até três citações, em palavras próprias.
