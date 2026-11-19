# Skill `research`: instalação e chaves

Skill de pesquisa profissional: coleta de várias fontes de alta qualidade, o Claude faz a síntese, analítica (a voz de escrita de quem usa, em `context/sobre-mim.md`, só entra quando a pesquisa vira post ou aula), e registra na base `knowledge/` seguindo os rituais do LLM Wiki. Processo e roteamento estão no [`SKILL.md`](./SKILL.md); o que é do projeto, em [`references/projeto.md`](./references/projeto.md).

## Chaves de API

| Variável | Obrigatória? | Fornecedor | Onde se pega |
|---|---|---|---|
| `PERPLEXITY_API_KEY` | sim | Perplexity / Sonar (raso e profundo) | https://www.perplexity.ai/account/api/keys (a API é paga à parte do plano do app) |
| `GEMINI_API_KEY` | sim | Google Gemini pelo AI Studio (raso, padrão, e profundo) | https://aistudio.google.com/apikey |
| `VERTEX_API_KEY` | não | Google Vertex AI, o raso por `--provider vertex` (pós-pago) | https://console.cloud.google.com/vertex-ai (Vertex AI > chave de API do modo expresso, num projeto com faturamento) |
| `TYPESAFE_API_KEY` | não | o Jev, só para sondar perguntas tipadas sobre a triagem (`references/projeto.md`) | https://docs.typesafe.ai |

**Como pôr:** copie o `.env.example` da raiz para `.env` (o `.env` nunca vai ao git) e preencha as linhas; ou ponha as variáveis no bloco `env` do seu `.claude/settings.local.json`, que também fica fora do git. O que já está no ambiente vence o `.env`. Depois, reinicie a sessão do Claude Code. Os scripts leem as chaves pelo `scripts/ambiente.py` desta pasta (cópia idêntica do `scripts/ambiente.py` da raiz) e nunca imprimem o valor; sem a chave, param com a mensagem do que falta, onde se pega e como se põe.

**Para conferir**, da raiz: `python -X utf8 scripts/confere_ambiente.py --skill research`.

**O free tier do Gemini não serve ao raso:** a busca (grounding) tem cota zero nele, embora o texto sem busca funcione.

**A Vertex é pós-paga:** cobra na fatura do projeto do Google Cloud, sem teto natural. Só rode com a estimativa de gasto antes (`references/projeto.md`, "Custo das APIs"). O AI Studio com crédito pré-pago se limita pelo saldo.

## O Codex (opcional)

A quarta frente do raso, `scripts/codex_search.py`, pede o Codex CLI (https://developers.openai.com/codex/cli) e `codex login`. Roda em modo só leitura, numa pasta temporária, e gasta a franquia do plano do ChatGPT, não crédito de API. Com `--perfil <nome>`, usa um perfil do `~/.codex/config.toml` (por exemplo, um sem os conectores da conta). Sem o Codex, a rodada segue com as outras três frentes.

## Dependências

```
python -m pip install -r .claude/skills/research/requirements.txt
```

Os conferidores (`confere_rodada.py`, `parafrase.py`, `confere_lugar.py`) e o `jats2md.py` usam só a biblioteca padrão; o `confere_lugar.py` pede o `git`, e o `parafrase.py` pede o `pdftotext` no PATH só quando a fonte é PDF.

## Smoke test (depois de configurar as chaves)

```
python -X utf8 .claude/skills/research/scripts/smoke_test.py          # 2 pings rasos
python -X utf8 .claude/skills/research/scripts/smoke_test.py --deep   # + acesso pago do Gemini Deep
```

O padrão faz um ping barato em cada fornecedor (não dispara deep research); espera-se `[OK]` nos dois. Com `--deep`, valida também o acesso ao tier pago do Gemini Deep Research (cria e cancela um job na hora, sem rodar a pesquisa). Com `--vertex`, o ping do Gemini vai pela Vertex. É o jeito de pegar problema de chave ou de faturamento cedo.

## O teste dos conferidores (sem rede, sem chave)

```
python -X utf8 .claude/skills/research/scripts/teste_conferidores.py
```

Roda os casos plantados que o `confere_rodada.py`, o `parafrase.py` e o `confere_lugar.py` têm de reprovar, ao lado do caso limpo que tem de passar, numa pasta temporária. Rode a cada edição de um dos três.

## Conversor do texto integral

Para a seção "Texto integral" de uma fonte de licença aberta que vem do PMC ou do Europe PMC (o `fullTextXML` da API), `scripts/jats2md.py` converte o XML JATS em markdown (tabelas, MathML em texto, figuras pela legenda; a seção "Associated Data" do PMC fica de fora): `python -I -X utf8 .claude/skills/research/scripts/jats2md.py entrada.xml saida.md [nivel_base]`, com os títulos de seção a partir do nível dado (padrão 3, `###`). Sem `body` no XML (registro só com resumo), ele para com aviso.

## Modelos usados

| Modo | Fornecedor | Modelo |
|---|---|---|
| Raso | Perplexity | `sonar-pro` |
| Raso | Gemini | `gemini-3.5-flash` + Google Search grounding (pelo AI Studio; Vertex por `--provider vertex`) |
| Raso | Busca web nativa | a ferramenta `WebSearch` da sessão do Claude Code (sem script, sem chave) |
| Raso | Codex (opcional) | o Codex CLI com `--search` |
| Profundo | Perplexity | `sonar-deep-research` |
| Profundo | Gemini | `deep-research-preview-04-2026` (agente via `interactions`, assíncrono) |

Escolha deliberada pelo tier de **melhor valor**, não pelo topo de linha (Gemini Pro, Deep Research Max): o ganho marginal não compensa o custo.

## Limitações conhecidas

- **A busca web nativa devolve links e um resumo em texto**, fora do contrato JSON dos scripts, sem data de publicação e com viés de fontes em inglês e dos Estados Unidos. Serve à triangulação e ao termo exato (repositório, issue, CVE); o resumo dela erra como o de qualquer frente, e a primária continua decidindo.
- **As URLs do Gemini (raso) são de redirect** (`vertexaisearch...`), não a URL canônica. Servem para triangular; a URL real se resolve no registro (Passo 7) antes de a fonte entrar em `knowledge/sources/`.
- **O Gemini Deep Research é preview e assíncrono** (jobs de dezenas de minutos): o script cria em background e faz polling; cancela no timeout para não custar à toa. O relatório vem rico, com marcadores `[cite: N]`, e as citações dos `steps` vêm como URLs de redirect, em geral sem título: o valor está no relatório, e título e URL canônica se resolvem no registro.
- **O Perplexity tem limite de taxa:** levas grandes em paralelo batem no 429; o script tenta de novo até três vezes, e o que voltar com erro roda de novo em sequência.
