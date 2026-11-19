# O que é deste projeto na `image-gen`

O método da skill fica no `SKILL.md` e no `roteamento.md`; aqui ficam os caminhos e as regras deste repositório. Outro projeto que instale a skill troca este arquivo.

## O banco de imagens

- **O índice:** `marketing/social-media/banco-de-imagens.md`, gerado pelo `scripts/indexa_banco.py` a partir dos `prompts.md` versionados em `marketing/`. Começa em branco (quem monta a família de produção o escreve com o cabeçalho); não se edita à mão, roda de novo depois de uma peça nova:
  ```
  python -X utf8 .claude/skills/image-gen/scripts/indexa_banco.py
  ```
- **Os originais:** no bucket de apelido `conteudo` (skill `r2-storage`, variável `R2_BUCKET_CONTEUDO`), em `assets/gerados/AAAA-MM-DD_<peça>/`.

## Onde salvar, por tipo de entregável

| Entregável | Pasta |
|---|---|
| carrossel da série | `marketing/social-media/carousels/series/<série>/<peça>/assets/` |
| carrossel avulso | `marketing/social-media/carousels/standalone/<peça>/assets/` |
| Stories | `marketing/social-media/stories/<data>-<tema>/assets/` |
| imagem de um mapa pessoal (o Vision Board) | `maps/vision-board/AAAA-MM-DD/`, ao lado do retrato; nunca sobe ao bucket, porque o quadro é local e não se publica em link (`decisions/vida-pessoal-e-mapas.md`) |
| teste descartável | o scratchpad da sessão |

## A identidade de cada série

A identidade vem do design system de quem pede a imagem: na série de exemplo, `marketing/social-media/carousels/series/exemplo/design-system.md` (em branco até você preencher). A marca do projeto fica em `context/brand/` (em branco, com roteiro). As referências pessoais de quem usa não entram como `--refs` de geração. Técnica de prompt e formatos de imagem na base: `knowledge/content-design/formatos-de-imagem.md` e `knowledge/content-design/claude-design-vs-nano-banana.md`.

## A regra de custo

**Preencha conforme as suas contas** (é você quem sabe como cada uma cobra). O custo por imagem está no `SKILL.md`. Enquanto uma linha estiver como `a preencher`, a skill trata aquela chave como **pós-paga**: estima o gasto antes e pergunta.

| Chave | Como a sua conta cobra | O teto ou a trava que você quer |
|---|---|---|
| `GEMINI_API_KEY` (AI Studio, o Nano Banana) | a preencher | |
| `VERTEX_API_KEY` (opcional) | a preencher | |
| o Codex, para o GPT Image (opcional) | franquia do plano | |

Os três jeitos de cobrar, e o que a skill faz em cada um:
- **Pós-pago** (cobra depois, na fatura, sem teto natural, como costuma ser a Vertex do Google Cloud): não roda por padrão, e **nunca em teste longo** (laço, bancada, rodada com muitos agentes). Fora disso, a tarefa estima o gasto antes, diz a estimativa a você e a usa como trava: perto do valor, para e pergunta se segue. Configure também o limite de gasto no painel do provedor.
- **Crédito pré-pago** (a conta carregada com saldo, que recusa a chamada quando acaba): o saldo é o teto. Pode usar quando a tarefa pedir, no mínimo que responda à pergunta; se acabar no meio, avisa, sem trocar sozinho para uma chave pós-paga.
- **Franquia de plano** (como o Codex, que gasta a franquia do plano do ChatGPT de quem o configurou): sem custo por chamada, mas com limite de uso; a skill diz quando o limite parar a rodada.

- **Antes de gerar, o que já existe:** o banco de imagens, as pastas `assets/` das peças e o bucket de conteúdo. Imagem de terceiro só como referência, nunca como asset.

## O perfil do Codex (opcional)

O `codex_imagem.py` roda o Codex pelo perfil `claude-imagem`, em `$CODEX_HOME/claude-imagem.config.toml` (por padrão `~/.codex/`): escrita só na pasta temporária de onde roda, sem aprovação, sem os conectores da conta, com a geração de imagem ligada. Para criar, uma vez: rode o script com `--criar-perfil`, ou crie o arquivo com o conteúdo que o script imprime (o mesmo do README). Sem o Codex instalado, sem login num plano pago do ChatGPT ou sem o perfil, o script para com a instrução e o Nano Banana segue.

## O Jev (opcional)

A conferência de texto inventado usa o cliente do Jev em `scripts/jev/` da raiz (`cliente.py` e `imagens.py`) e pede `TYPESAFE_API_KEY`. Sem um dos dois, ela pula com um aviso de uma linha.
