# O que é deste projeto

Tudo o que a skill `research` usa e que muda de um projeto para outro fica aqui: os caminhos da base, onde moram as rodadas, a regra de lugar do que é de terceiro, a regra de custo e as partes opcionais. O método fica no [`SKILL.md`](../SKILL.md) e nas outras referências. Para levar a skill a outro projeto, troque este arquivo.

Os caminhos abaixo partem da raiz do projeto.

## A base

- **Rituais da base** (Ingest, Query, Lint): `knowledge/README.md`.
- **Porta de entrada e índice:** `knowledge/index.md`, e o `index.md` de cada área (`knowledge/<área>/index.md`).
- **Registro das mudanças:** `knowledge/log.md`.
- **Fontes (camada raw):** `knowledge/sources/`, com a régua em `knowledge/sources/README.md` (o frontmatter, a régua de licença em "Conteúdo de terceiros", a ficha de obra protegida no item 2, "Quando a primária não abre", "Citação e cobertura", "Transcrição sem marca de falante").
- **A síntese de método que a skill usa:** `knowledge/journalism/avaliar-fonte-e-parar-a-busca.md` (julgar a fonte e as regras de parada).
- **Onde a base olha fora de `knowledge/`** no Passo 0b: `decisions/` (o que o projeto já decidiu sobre o tema) e as pastas de conteúdo (`marketing/`).
- **A voz de escrita de quem usa:** `context/sobre-mim.md`. Só entra quando a pesquisa vira post ou aula; a síntese é analítica.
- **O público:** `context/publico.md`. Quando o público é brasileiro, a variação em português é obrigatória (Passo 2.5) e o `confere_rodada.py` roda com `--publico-br`.

## As rodadas de pesquisa

- **Pasta de trabalho de cada rodada:** no scratchpad da sessão, uma pasta própria com o tema e a hora no nome (`<tema>-<hhmm>/`).
- **Onde a rodada fica guardada:** `knowledge/research-rounds/<rodada>/`, com `<rodada>` = `AAAA-MM-DD-<tema>`. Dentro dela:
  - `rotulos.json`, os rótulos da triagem (`references/rotulos.md`);
  - as saídas das buscas (`qN-<frente>.json`, `qN-nativa.md`), versionadas;
  - `fontes/`, com o texto de licença aberta, `fontes/protegidas.json` e, na raiz da rodada, `licencas.json`;
  - `notas/` e `scripts/`, as notas e os scripts nossos, sem citação longa;
  - `originals/`, fora do git, com o texto protegido, a nota com citação longa e o script com texto de fonte embutido.

## Onde fica o que é de terceiro

Tudo vai ao git, menos o que não pode ir por direito autoral ou privacidade: o texto, a imagem, o áudio ou o vídeo protegido inteiro, a nota com citação longa (mais de umas 25 palavras), a mensagem ou o dado pessoal de terceiro. O que disso se guarda fica numa pasta `originals/` ao lado do que o usa (o `originals/` da rodada, ou `knowledge/sources/originals/` para o original de uma ficha), fora do git pela linha `originals/` do `.gitignore`, e nunca fora do projeto (nem no scratchpad, nem só numa cópia de trabalho). Mensagem e dado pessoal de terceiro, em geral, não se guardam. O `.env` também fica fora do git, pela linha `.env` do mesmo `.gitignore`.

A conferência é o `scripts/confere_lugar.py` da skill: sobre a pasta versionada da rodada, e com `--repo` da raiz do checkout principal. Numa cópia de trabalho (worktree), o `--repo` avisa; leve o `originals/` dela ao mesmo caminho no checkout principal e rode lá antes de remover a cópia.

## Custo das APIs

**Preencha conforme as suas contas** (é você quem sabe como cada uma cobra). Enquanto uma linha estiver como `a preencher`, a skill trata aquela chave como **pós-paga**: estima o gasto antes e pergunta.

| Chave | Como a sua conta cobra | O teto ou a trava que você quer |
|---|---|---|
| `PERPLEXITY_API_KEY` | a preencher | |
| `GEMINI_API_KEY` (AI Studio) | a preencher | |
| `VERTEX_API_KEY` (opcional) | a preencher | |
| o Codex (opcional) | franquia do plano | |

Os três jeitos de cobrar, e o que a skill faz em cada um:
- **Pós-pago** (cobra depois, na fatura, sem teto natural, como costuma ser a Vertex do Google Cloud): não roda por padrão, e **nunca em teste longo** (laço, bancada, rodada com muitos agentes). Fora disso, a tarefa estima o gasto antes, diz a estimativa a você e a usa como trava: perto do valor, para e pergunta se segue. Configure também o limite de gasto no painel do provedor.
- **Crédito pré-pago** (a conta carregada com saldo, que recusa a chamada quando acaba): o saldo é o teto. Pode usar quando a tarefa pedir, no mínimo que responda à pergunta; se acabar no meio, avisa, sem trocar sozinho para uma chave pós-paga.
- **Franquia de plano** (como o Codex, que gasta a franquia do plano do ChatGPT de quem o configurou): sem custo por chamada, mas com limite de uso; a skill diz quando o limite parar a rodada.
- **O profundo custa bem mais que o raso:** a decisão de gastar é de quem pede (Passo 1).

## As partes opcionais

- **O Codex** (`codex_search.py`, a quarta frente do raso): pede o Codex CLI instalado e com `codex login`. Sem ele, a rodada segue com as outras três e diz isso.
- **A Vertex** (`VERTEX_API_KEY`): só para quem preferir o pool próprio do Google Cloud no raso; segue a linha dela na tabela acima.
- **O Jev, como sonda** (`scripts/jev/cliente.py` da raiz, com a `TYPESAFE_API_KEY`): os rótulos de cada rodada servem de gabarito para testar perguntas tipadas sobre a triagem (esta fonte é a origem da afirmação ou a repete? parar aqui bastava?). É opcional: sem a chave, a skill roda igual, e nenhum passo depende dele.

## O que este projeto precisa ter

- `knowledge/research-rounds/` (a pasta das rodadas), com um `README.md` curto que diga o que vai em cada subpasta (o resumo da seção "As rodadas de pesquisa", acima).
- `knowledge/sources/originals/` só existe no disco de quem ingeriu: fica fora do git pela linha `originals/` do `.gitignore`.
- O `.gitignore` da raiz com as linhas `originals/` e `.env`.
