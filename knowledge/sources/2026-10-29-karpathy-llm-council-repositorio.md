---
titulo: "karpathy/llm-council: várias LLMs respondem, revisam-se às cegas e um presidente sintetiza"
tipo: artigo
autor: "Andrej Karpathy"
url: "https://github.com/karpathy/llm-council"
publicado_em: 2025-11-22
capturado_em: 2026-10-29
licenca: "nenhuma declarada (campo license nulo na API do GitHub em 2026-10-29, sem arquivo LICENSE no repositório); tratado como protegido"
areas: [agent-engineering]
tags: [llm-council, multi-agent-debate, model-heterogeneity, llm-as-judge, self-preference, karpathy, openrouter]
---

**Proveniência:** lido em 29/10/2026 pela API do GitHub, na apuração (o Reel do Lucas Puerto Faria que adapta este repositório, ficha em `2026-10-29-puerto-faria-reel-conselho-de-ia.md`). Arquivos lidos: `README.md`, `CLAUDE.md`, `backend/config.py`, `backend/council.py`, `backend/openrouter.py`, `backend/main.py`, `backend/storage.py`, `pyproject.toml`, `start.sh`, `frontend/package.json` e os componentes `App.jsx`, `ChatInterface.jsx`, `Stage1.jsx`, `Stage2.jsx` e `Stage3.jsx`. Ficha de estudo em palavras próprias; o código e o README não entram na íntegra porque o repositório não tem licença.

## Ficha

| Campo | Valor (29/10/2026) |
|---|---|
| Criado | 22/11/2025, 23:24 UTC |
| Histórico | 5 commits, todos em 22/11/2025 entre 22:27 e 23:35 UTC ("v0", "Label maker add", "a bit more progressive update and single turn", "add vibe code warning", "readme tweaks"); nenhum depois |
| Estrelas | 26.053 |
| Forks | 4.477 |
| Issues abertas | 145 |
| Descrição | "LLM Council works together to answer your hardest questions" |
| Linguagem | Python (backend) e JavaScript (frontend) |

## A ideia, nas palavras do README

Em vez de fazer a pergunta a um só provedor de LLM, juntar vários num "LLM Council". O app local tem cara de ChatGPT, manda a pergunta a vários modelos pelo OpenRouter, pede que eles revisem e ordenem o trabalho uns dos outros, e um modelo presidente (Chairman) produz a resposta final. O `CLAUDE.md` do repositório chama a revisão anônima da etapa 2 de "key innovation", porque impede os modelos de favorecerem uns aos outros.

## A motivação declarada: o "Vibe Code Alert"

- O projeto foi "99% vibe coded as a fun Saturday hack": escrito quase todo por IA, num sábado, por diversão.
- O objetivo era explorar e avaliar vários LLMs lado a lado no processo de ler livros junto com LLMs (o README liga para um post dele no X sobre isso, https://x.com/karpathy/status/1990577951671509438).
- O que ele achou útil: ver várias respostas lado a lado e também a opinião cruzada de cada modelo sobre a saída dos outros.
- Sem suporte: "I'm not going to support it in any way"; fica como está, para inspirar, e ele não pretende melhorar.
- Fecha com "Code is ephemeral now and libraries are over": quem quiser mudar, que peça à sua LLM.

## As três etapas, como o código faz

Para cada pergunta o backend faz uma chamada por membro na etapa 1, outra por membro na etapa 2 e uma do presidente na etapa 3 (com os quatro modelos padrão, nove chamadas), mais uma ao `google/gemini-2.5-flash` para gerar o título da conversa na primeira mensagem. As chamadas de cada etapa saem em paralelo (`asyncio.gather`), com tempo limite de 120 s cada. A requisição ao OpenRouter leva só o modelo e as mensagens: nenhum prompt de sistema, nenhuma temperatura ou outro parâmetro.

### Etapa 1: primeiras opiniões

- A pergunta do usuário vai sozinha, como única mensagem, a cada modelo do conselho. Não há papel, persona nem instrução extra.
- A conversa é de uma pergunta só: o backend passa ao conselho só a mensagem atual, sem histórico, e a interface esconde a caixa de texto depois da primeira mensagem (o commit "single turn").
- Modelo que falha é descartado em silêncio; o conselho segue com quem respondeu.

### Etapa 2: revisão cruzada anônima

- As respostas recebem os rótulos "Response A", "Response B" e assim por diante, na ordem da lista `COUNCIL_MODELS` em `config.py`. O código não embaralha a ordem: com os padrões, A é sempre o GPT-5.1 (se ele respondeu).
- O backend guarda o mapa de rótulo para modelo (`label_to_model`), usado só para a exibição e a agregação.
- **Todos os membros do conselho avaliam todas as respostas, inclusive a própria.** O README diz que cada modelo recebe as respostas "of the other LLMs"; o código monta um texto único com todas as respostas da etapa 1 e o manda a cada membro. Também um membro que falhou na etapa 1 é chamado a avaliar na etapa 2.
- O prompt diz que são respostas de modelos diferentes, anonimizadas, e pede duas coisas: primeiro avaliar cada resposta em separado, dizendo o que faz bem e o que faz mal; depois, no fim, a ordem final. A ordem tem formato rígido: uma linha "FINAL RANKING:" em maiúsculas e uma lista numerada da melhor para a pior, só com o rótulo em cada linha, sem mais texto. O prompt traz um exemplo completo do formato.
- O README diz que a ordem é por "accuracy and insight"; o prompt não nomeia critério nenhum, só "da melhor para a pior".
- **Extração da ordem:** o código procura o trecho depois de "FINAL RANKING:" e pega as linhas no padrão "número, ponto, Response X". Se não achar, pega qualquer "Response X" no trecho, na ordem em que aparecem; se não houver o cabeçalho, pega qualquer "Response X" no texto inteiro, o que pode capturar menções da parte da avaliação.
- **Agregação:** para cada modelo, a média das posições que recebeu em todas as ordens (inclusive a que ele deu a si mesmo), arredondada em duas casas, com a contagem de votos; menor é melhor. A interface mostra essa tabela com o título "Aggregate Rankings (Street Cred)".

### Etapa 3: o presidente

- O presidente recebe num prompt só: a pergunta original; as respostas da etapa 1, cada uma identificada pelo **nome do modelo** (não pelo rótulo); e o texto completo das avaliações da etapa 2, cada uma identificada pelo nome do modelo avaliador. As avaliações citam os rótulos A, B, C, mas o prompt não diz qual rótulo é qual modelo, e a média agregada não é passada ao presidente.
- O prompt diz que ele é o presidente de um conselho de LLMs cujos membros responderam e se ordenaram, e pede que sintetize tudo numa resposta única, completa e precisa, levando em conta as respostas e suas ideias, as ordens dos pares e o que elas revelam sobre a qualidade, e os padrões de concordância e discordância. Fecha pedindo uma resposta que represente "the council's collective wisdom".
- O presidente padrão (Gemini 3 Pro) é também membro do conselho: responde, avalia e depois sintetiza. O `CLAUDE.md` registra que o presidente pode ser ou não um dos membros e que o Gemini foi escolha de preferência do usuário.
- Se a chamada do presidente falha, a resposta final vira uma mensagem de erro.

## Modelos padrão (`backend/config.py`)

| Papel | Modelo (id no OpenRouter) |
|---|---|
| Membro | `openai/gpt-5.1` |
| Membro | `google/gemini-3-pro-preview` |
| Membro | `anthropic/claude-sonnet-4.5` |
| Membro | `x-ai/grok-4` |
| Presidente | `google/gemini-3-pro-preview` |
| Título da conversa | `google/gemini-2.5-flash` |

O conselho é uma lista de ids de modelo e nada mais: não há campo para dar a cada membro um papel ou prompt próprio. Como as respostas são guardadas num dicionário indexado pelo id, repetir o mesmo modelo duas vezes na lista não gera dois membros.

## A pilha

- **Backend:** FastAPI em Python 3.10 ou mais, httpx assíncrono, chave `OPENROUTER_API_KEY` num `.env`; roda na porta 8001. Duas rotas de mensagem: uma devolve tudo no fim, outra transmite por Server-Sent Events à medida que cada etapa termina.
- **Frontend:** React 19 com Vite 7 e react-markdown, na porta 5173.
- **Armazenamento:** um JSON por conversa em `data/conversations/`, com as três etapas; o mapa de rótulos e a média agregada não são gravados, só voltam na resposta da API.
- **Gestão de pacotes:** uv no Python, npm no JavaScript; `start.sh` sobe os dois.

## A interface

Cada etapa aparece num bloco. A etapa 1 em abas, uma por modelo. A etapa 2 em abas com o texto bruto de cada avaliação, em que o navegador troca "Response A" pelo nome do modelo em negrito só para leitura (com um aviso de que a avaliação original usou rótulos), a ordem extraída logo abaixo para o usuário conferir se a extração acertou, e a tabela agregada. A etapa 3 num bloco verde com o nome do presidente. O `CLAUDE.md` defende essa transparência: tudo inspecionável, para gerar confiança e depurar casos de borda.

## O que o repositório não afirma

- **Não fala em bajulação** (sycophancy) nem em concordar com o usuário. O anonimato serve a outro fim: impedir que um modelo "play favorites" ao julgar as respostas, isto é, favoreça uma resposta pelo nome de quem a escreveu.
- **Não mede se o conselho acerta mais** que um modelo sozinho, nem que o melhor membro. Não há avaliação, conjunto de testes, número de qualidade, custo ou latência. O `CLAUDE.md` cita um `test_openrouter.py` que não existe no repositório.
- **Não trata de personagens** no mesmo modelo: a diversidade vem só de modelos de empresas diferentes respondendo à mesma pergunta sem instrução.
- **Não diz como usar a ordem agregada** além de mostrá-la; ela não entra na síntese do presidente.
- **Não discute os efeitos de o modelo avaliar a própria resposta** nem da ordem fixa dos rótulos.

Entre as ideias futuras do `CLAUDE.md` estão critério de ordenação configurável (não só precisão e insight), análise do desempenho dos modelos ao longo do tempo e escolha do conselho pela interface; nenhuma foi feita.

## Limites declarados

O próprio autor: experimento de um sábado, quase todo escrito por IA, sem suporte e sem plano de evolução, oferecido como inspiração.
