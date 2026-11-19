---
name: slides-export
description: >-
  Exporta as telas de um carrossel (slides.html) ou de uma sequência de Stories (stories.html, com --height 1920) como
  imagens finais pelo shot-scraper, em JPEG 1080×1350 por padrão, regera só as telas pedidas, grava a tela em vídeo do
  carrossel em MP4 a partir do próprio HTML e sobe ao bucket R2 registrando os embeds na legenda.md; antes de subir, roda
  as conferências da forma (as da visual-form) e barra o upload com ERRO. USE quando a pessoa pedir para exportar, gerar ou
  renderizar as imagens de um post ou de Stories, fechar um carrossel para publicar, regerar telas depois de um ajuste, ou
  gravar e conferir a tela em vídeo (MP4), mesmo que diga só "a tela animada". NÃO use para montar ou ajustar as telas e
  rodar as conferências da forma sozinhas (visual-form), o objeto que se move (object-anatomy), gerar ilustração (image-gen)
  nem para publicar a peça numa rede social.
---

# slides-export

Bloco single-purpose, componível: recebe a pasta do post e devolve os arquivos em `images/`. Setup e detalhes no [`README.md`](./README.md); o que é deste projeto (os estados da peça, o que conta como publicada, o bucket, a voz) em [`references/projeto.md`](./references/projeto.md).

> **Passo 0, as credenciais.** Antes de tudo, rode da raiz do projeto `python -X utf8 scripts/confere_ambiente.py --skill slides-export` (acrescente `--upload` quando o pedido for subir ao bucket). Se ele sair com `[PARE]`, pare aqui: repasse à pessoa a mensagem dele (qual variável falta, onde se pega e como se põe) e não tente rodar a skill sem a chave. Se o script não existir (a skill instalada como plugin noutro projeto), siga: o próprio código da skill para com a mesma mensagem na primeira chamada.

Só o `--upload` pede chave (as do R2, pela `r2-storage`). Sem elas, o `--upload` para antes de exportar, com a mensagem; a exportação local roda sem chave e avisa, uma vez, que a proteção do publicado pelo bucket ficou desligada.

**Lições:** antes de começar, leia as abertas e as apontadas em [`licoes.md`](./licoes.md) desta pasta.

```
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta-do-post>
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta> --only 3,5
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta> --format png
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta> --upload conteudo <prefixo>
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta> --upload conteudo <prefixo> --motivo "<o que mudou>"   # peça já publicada: versão nova
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta-dos-stories> --html stories.html --height 1920 --previa --out-dir <dir>   # prévia com os adesivos do app simulados, só para conferir
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta> --sem-video --out-dir <scratchpad>   # a tela em vídeo em imagem (o quadro final), para a revisão e o portão
python -X utf8 .claude/skills/slides-export/scripts/tela_em_video.py conferir <arquivo.mp4>   # um MP4 contra os limites da API (--story: o perfil do vídeo de Story)
python -X utf8 .claude/skills/slides-export/scripts/teste_tela_em_video.py   # o teste da tela em vídeo, sem peça real nem bucket
```

`conteudo` é o apelido do bucket (`R2_BUCKET_CONTEUDO`, pela `r2-storage`); qualquer outro apelido configurado vale. Nos Stories, `--bucket-publicado <apelido>` diz onde a coleta guarda o que foi ao ar, quando não é o mesmo do `--upload`.

**As conferências da forma são da `visual-form`:** o `conferir_telas.py`, o `medidas_forma.py` e o `medir_blocos.py` moram em `.claude/skills/visual-form/scripts/`, com a tabela de achados em `.claude/skills/visual-form/references/conferencias.md`; o `juntas.py` e o `saltos.py`, na `object-anatomy`. A exportação chama o `conferir_telas.py` de lá antes da foto, e o `--upload` barra o que ele achar como ERRO (regra 7). Aqui ficam a exportação, a tela em vídeo (`tela_em_video.py`) e o `fontes.py`, que as conferências importam.

## Regras

1. **Contar antes de exportar.** O script conta as `<section class="slide">` do HTML; diga à pessoa quantas telas encontrou. Se o número não bater com o que ela espera, pare e olhe o HTML.
2. **JPEG é o formato de publicação** das telas estáticas (a tela em vídeo sai em MP4, regra 10); PNG é só para revisão visual, quando pedido. Nunca suba PNG para publicar.
3. **Ajuste pontual regera só a tela ajustada** (`--only`), para não trocar arquivos já aprovados.
4. **Antes de publicar, upload só quando a peça está fechada**, com o prefixo espelhando o caminho no projeto (a convenção em `references/projeto.md` da `r2-storage`). Regerar uma tela já subida implica subir de novo o mesmo arquivo, com o mesmo nome. **Exceção, a prévia:** toda prévia validada numa passada (`--previa` ou a renderização para a leitura da pessoa) sobe ao bucket pela skill `r2-storage`, nunca pelo `--upload` deste script (que grava o prefixo na `legenda.md` e usaria os mesmos nomes da imagem final), com nome próprio, `<prefixo da peça>/previas/passada-N.jpg`, e fica apontada no roteiro. No carrossel, em que a prévia é igual à imagem final, a passada que foi publicada pode apontar para as imagens finais em vez de subir uma cópia; nos Stories, a prévia leva os adesivos simulados e continua subindo. Depois de publicada, regra 9.
5. **Exportar registra na peça** (antes de publicar; depois, regra 9). O script escreve na `legenda.md` o rótulo `**Imagens:**` e a seção `## Slides` com os embeds: caminho relativo quando as imagens são só locais, URL pública depois do `--upload`. Não edite essa seção à mão. As imagens locais ficam fora do git.
6. Se o `shot-scraper` reclamar de navegador ausente, rode `shot-scraper install` uma vez.
7. **Conferência com ERRO volta a peça para ajuste, não para o juiz.** ERRO não impede exportar para revisão, mas cancela o `--upload` (código 2), e a mensagem diz o que fazer; conferência que não rodou também cancela. A conferência olha a peça inteira mesmo com `--only`, porque a peça vai ao ar inteira; `--sem-conferir` só para regerar para revisão o que já foi conferido, e com `--upload` o script recusa. Cada achado, o nível e o que fazer: a tabela em `.claude/skills/visual-form/references/conferencias.md`. **O travessão só barra quando a voz de quem usa o pede:** se `context/sobre-mim.md` não existe ou não diz que o texto vai sem travessão, o achado não barra o `--upload` (a conferência não inventa regra que a voz não tem).
8. **Posição se confere medindo, não a olho:** é da `visual-form` (o `medir_blocos.py`). Aqui, o `export_slides.py` e o `tela_em_video.py` pedem as fontes antes da foto e do vídeo, e na tela em vídeo a fonte que falta sai como ERRO, como na tela em JPEG, sem parar o export de revisão. Script novo que mede texto renderizado pede as fontes antes, pelo `scripts/fontes.py` (README, "A fonte antes da medida").
9. **Depois de publicada, nada se sobrescreve e o registro só cresce** (o detalhe no README, "Antes e depois de publicar"). O que conta como publicada está em `references/projeto.md`; aqui fica o que o código faz com isso. O carrossel conta inteiro, pelo `**Publicado:**` da `legenda.md`. Nos Stories publicados por API, a proteção é tela a tela, pela tabela "Publicada pela API" do `roteiro.md`; nos Stories pelo app, a sequência inteira, pelo `estagio` ou pelo bucket. O bucket só se consulta com `--upload`; sem resposta (sem rede), vale o roteiro, com aviso. Se uma rotina commita no roteiro do dia, traga o remoto antes de mexer nele (`git pull`, ou `git fetch` e `git merge` numa worktree). Na tela publicada, o `--upload` exige `--motivo "<o que mudou>"`, sobe em `<prefixo das imagens que foram ao ar>/versoes/versao-N/` (a versão 1 é a publicada, que fica onde está) e acrescenta uma linha em "## Versões depois de publicada", sem reescrever `**Imagens:**` nem `## Slides`; a tela ainda sem linha na tabela sobe no próprio prefixo, com o mesmo nome. Stories com a data já passada, sem tabela, com o `estagio` atrasado e nada no bucket: o `--upload` recusa até o `estagio` ser acertado. A pasta `images/` é sobrescrita em toda exportação; o que foi ao ar se lê no bucket. Na tela publicada, as regras da casa (e as de área segura, zona proibida e travessão) saem como AVISO e não barram a versão nova, porque o que já foi ao ar não muda; a sobreposição, a fonte que não carregou e os arquivos fora dos limites continuam barrando.
10. **Tela em vídeo, só no carrossel, é opção.** O código aceita mais de uma tela em vídeo, de 3 a 60 s; a duração recomendada é de 5 a 8 s, e fora dela sai aviso. A tela leva `data-video="<segundos>"` na `<section class="slide">`, e a página define `window.quadro(t, idx)`, que põe a tela no instante `t` sem nada correr sozinho; o estado parado é o quadro final, que as conferências medem, e a animação acaba antes do fim; na tela em laço (o último quadro igual ao primeiro), o estado parado é o instante que a página desenha sem `quadro`, e a exportação diz "em laço" em vez de avisar que a animação não andou (README, "Tela em vídeo"). A exportação grava `images/slide-NN.mp4` do próprio `slides.html` (o mesmo papel, as mesmas fontes e a mesma moldura), sem som (`--som-mudo` põe uma faixa muda), e confere o MP4 contra os limites da API; fora deles, ou sem `window.quadro`, o `--upload` não sobe. Para o juiz do portão e a leitura da forma, `--sem-video --out-dir <scratchpad>` dá o quadro final em imagem, sem apagar nada nem gravar na `legenda.md`; o movimento se lê no MP4. A tela que muda de formato deixa no bucket o arquivo velho com o mesmo número: o script avisa, e ele sai pela `r2-storage`, uma chave por vez e confirmada na conversa. Os Stories não usam esta tela. O detalhe no README, "Tela em vídeo".

**Ao terminar:** se houve falha, contorno ou acerto que vale lembrar, registre em [`licoes.md`](./licoes.md) desta pasta, na mesma entrega (formato e estados em [`decisions/licoes-das-skills.md`](../../../decisions/licoes-das-skills.md)).
