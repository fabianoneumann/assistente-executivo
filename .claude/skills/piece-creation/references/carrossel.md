# Carrossel: a série e o avulso

O que a criação de peças acrescenta aos passos do `SKILL.md` no carrossel. Quando a série tem um processo de criação próprio (o `processo-criacao-posts.md` da pasta dela, `projeto.md`), é ele que roda, e ele manda quando discordar daqui; este arquivo não repete as etapas dele: diz onde cada uma cai nos passos desta skill, quem a faz e onde fica o registro. Sem processo próprio, a série roda pelos passos do `SKILL.md`, na ordem da tabela abaixo.

## Os passos da skill, no processo da série

| Passo da skill | A etapa da série | Quem faz | Onde fica |
|---|---|---|---|
| 2. Briefing | o briefing da semana | esta skill | o rascunho da semana (`rascunho-semana-NN-<tema>.md`, na pasta da série), uma vez para o A e o B; a seção "Estado da criação" no `refinamentos.md` de cada post |
| 3. Apuração e ângulo | a apuração, com o ledger, e a mesa de ângulos (o checkpoint da semana) | `research` e `story-angle` | as sínteses e as fichas em `knowledge/`, o checkpoint no rascunho da semana |
| 4. Roteiro | o arco, os conceitos e as imagens, o texto, a revisão e a trava | `piece-script` (`references/carrossel.md` dela) | `escaleta.md`, `conceitos-e-imagens.md`, `texto.md` e o texto da `legenda.md`, na pasta do post |
| 5. Forma | a forma | a `visual-form` (com a I2 e a trava, antes da prévia) | `slides.html`, `assets/`, `prompts.md`, `medida/` |
| 6. Prévia | a leitura da pessoa | esta skill leva; a pessoa decide | a passada no `refinamentos.md` |
| 7. Portão | o portão | o juiz em subagente, pelo arquivo do portão | o veredito no `refinamentos.md` |
| 8 e 9. Fechar e registrar | a exportação e o registro | `slides-export`; esta skill registra | os JPEG no bucket, os embeds na `legenda.md`; a publicação fica fora desta versão |

**Na semana da série,** a apuração e a mesa de ângulos valem para os dois posts; a partir do roteiro, cada post é uma peça, com o próprio estado. O post roteirizado depois lê a escaleta do primeiro (os não escolhidos que vieram para ele, a ponte do A para o B). No Tipo B, a mesa de ângulos pode ser mais leve, quando o processo da série disser.

**Quando a pauta já está pronta** (o checkpoint da semana feito, o ângulo do post escolhido), o passo 3 sai no estado como "não se aplica, porque o ângulo foi escolhido em <data>, <arquivo e linha>", e a peça segue para o roteiro com a pauta e os não escolhidos da semana. **A mesa do arco, dos conceitos e das imagens não se pula por isso:** ela é do post, não da semana.

## O briefing do carrossel

No rascunho da semana (série) ou no `refinamentos.md` do post (avulso), antes do texto, com os campos do passo 2 do `SKILL.md` e, no carrossel:

- **as peças abertas antes de escrever:** o post publicado do mesmo tipo (o par A com A, B com B), a irmã da semana e os Stories da semana que tocam o post, cada um com o caminho;
- **as regras da vez:** a versão do design system e as pendências abertas dele, a receita do tipo na `estrutura-editorial.md` da série;
- **o incremento da semana**, com a tela e o elemento, quando a série evolui por incrementos;
- **as dimensões que mudam em bloco:** a abertura (pergunta ou afirmação), o par de fontes, a paleta e o formato tendem a se repetir em todas as peças de uma vez; diga qual muda nesta peça, ou que fica igual de propósito.

## O carrossel avulso

Pasta em `marketing/social-media/carousels/standalone/AAAA-MM-DD_<tema>/` (`projeto.md`), com as três regras do avulso: o gancho escrito por último, cerca de 3 linhas por tela, a chamada que puxa comentário genuíno. Sem série, **a identidade visual é item da primeira mesa** (gosto e direção de arte), com o porquê de cada direção; as regras disso estão em `references/ideia-crua.md`, seção 3, que vale também quando o avulso parte de uma pauta pronta. Quando o avulso nasce de ideia crua, a primeira mesa é a de lá.

## O que se confere antes da prévia

- O estado com os passos 1 a 5 preenchidos, nenhum vazio: a mesa do arco, dos conceitos e das imagens aconteceu (ou a escolha da pessoa veio de quem chamou, com a fonte), e o ok do texto veio na entrega da `review`.
- A `review` rodou por agentes que não escreveram o texto (o `refinamentos.md` diz quantos agentes e quantos achados).
- As conferências da forma em 0 ERRO, e o texto da tela igual ao `texto.md` travado (o AVISO `texto_fora_do_travado` do `conferir_telas.py` da `visual-form`).
