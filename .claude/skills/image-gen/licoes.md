# Lições da skill `image-gen`

O que o uso e a edição desta skill ensinaram. Antes de usar a skill, leia as abertas e as apontadas; ao terminar, registre a lição nova aqui, na mesma entrega, como **aberta**. Cada lição traz o que devia acontecer, o que aconteceu, por quê, o que mudar e quando vale, com a gravidade (crítica, maior, menor) e as ocorrências; a que vira regra entra no `SKILL.md` (ou no código) e passa para "Viraram regra", em uma ou duas linhas, no imperativo, com o porquê. Formato, estados e quem decide em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md). As lições de imagem das peças moram em [`marketing/licoes.md`](../../../marketing/licoes.md) (seção "Forma"), porque são das duas coisas, da peça e da ferramenta; aqui elas só se apontam e não contam como abertas.

## Abertas

Nenhuma.

## Viraram regra

- **Grave o custo de cada geração pelos tokens da resposta, não pela tabela do fornecedor.** A tabela contava menos tokens por imagem do que as gerações gastam, e o custo saía subestimado.
- **Ache o executável do Codex por `shutil.which("codex")`.** No Windows o npm instala um atalho `codex.cmd`, que o `subprocess` só acha pelo caminho completo.
- **No AI Studio, não peça `output_mime_type`: converta para o formato do `--out` depois.** O AI Studio recusa o parâmetro, que só o Vertex aceita.
