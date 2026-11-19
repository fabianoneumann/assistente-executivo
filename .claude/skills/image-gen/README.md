# Skill `image-gen`: setup e chaves

Geração de imagem pelo Nano Banana (Gemini image, `generate_content`) e, opcional, pelo GPT Image do Codex. Processo e modos no [`SKILL.md`](./SKILL.md); o que é deste projeto em [`references/projeto.md`](./references/projeto.md).

## Instalação

```
python -m pip install -r .claude/skills/image-gen/requirements.txt
```

Depois, da raiz do projeto, `python -X utf8 scripts/confere_ambiente.py --skill image-gen` diz o que ainda falta configurar.

## As variáveis

Os valores vão no `.env` da raiz (copie o `.env.example` para `.env` e preencha as linhas; o `.env` nunca vai ao git) ou no bloco `env` do `.claude/settings.local.json`. Os scripts leem pelo `scripts/ambiente.py` desta pasta; **nunca** ponha chave no código. Sem a chave, o script para com a mensagem (a variável, onde se pega, como se põe), sem traceback.

| Variável | Obrigatória | Uso | Onde se pega |
|---|---|---|---|
| `GEMINI_API_KEY` | sim | o padrão (`--provider aistudio`, crédito pré-pago do AI Studio); a mesma da skill `research` | https://aistudio.google.com/apikey |
| `VERTEX_API_KEY` | não | `--provider vertex` (pós-pago no projeto do Google Cloud; só com a estimativa de gasto antes) | https://console.cloud.google.com/vertex-ai (chave de API do modo expresso) |
| `TYPESAFE_API_KEY` | não | o Jev, na conferência de texto inventado (`confere_imagem.py --jev`); sem ela, a conferência pula com aviso | https://docs.typesafe.ai |

## O Codex (opcional)

O `codex_imagem.py` precisa do Codex CLI instalado (https://developers.openai.com/codex/cli), do `codex login` num plano pago do ChatGPT (no gratuito a ferramenta de imagem não existe) e de um perfil criado uma vez em `~/.codex/claude-imagem.config.toml` (ou em `$CODEX_HOME`):

```
# Perfil para o Claude Code gerar imagem pelo Codex (skill image-gen): escrita só na pasta de onde roda (uma pasta
# isolada temporária), sem aprovação, sem os conectores da conta do ChatGPT, com a geração de imagem integrada.
sandbox_mode = "workspace-write"
approval_policy = "never"

[features]
apps = false
image_generation = true
```

Ou rode o script uma vez com `--criar-perfil`, que grava esse arquivo se ele não existir. Sem o Codex ou sem o perfil, o script para com a instrução, e o Nano Banana segue.

## Smoke test (pede rede e chave)

```
python -X utf8 .claude/skills/image-gen/scripts/smoke_test.py            # AI Studio (o padrão)
python -X utf8 .claude/skills/image-gen/scripts/smoke_test.py --vertex   # Vertex (pós-pago)
```

Gera uma imagem pequena (flash @ 1K) e confirma os bytes salvos. É o jeito de pegar cedo problema de chave, faturamento ou modelo.

## Modelos e custo (pela tabela do fornecedor)

| Modelo (`--model`) | ID | 1K/2K | 4K |
|---|---|---|---|
| `pro` (Nano Banana Pro) | `gemini-3-pro-image` | US$ 0,134 | US$ 0,24 |
| `flash` (Nano Banana 2) | `gemini-3.1-flash-image` | US$ 0,067 (1K) / US$ 0,101 (2K) | US$ 0,151 |

A tabela conta 1.120 tokens por imagem; o medido saiu acima (o `SKILL.md` mostra o medido, e cada geração grava o próprio custo). Os dois modelos rodam no AI Studio e no Vertex.

## Saída

- **PNG por padrão** (`--out .png`), melhor para texto e linha de infográficos e mapas; `--out .jpg` gera JPEG.
- Proporções nativas: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9. **8:5 não é nativa** (a estratégia de mapa está no `SKILL.md`).

## Limitações conhecidas

- **Texto pequeno ou denso na imagem sai ilegível** (limite oficial). Rótulos primários curtos saem bem; anotações finas vão como overlay HTML.
- Consistência de personagem e de rosto não é perfeita; retrato de pessoa real vem de foto real, não de geração.
- **A Interactions API não rodava no Vertex** (só no AI Studio); por isso o `generate_content`.
