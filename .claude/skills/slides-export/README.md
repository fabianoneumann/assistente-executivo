# Skill `slides-export`: setup

Exporta `slides.html` (ou `stories.html`) em imagens com o `shot-scraper` (Python + Playwright). A configuração do `shot-scraper` é gerada a cada execução, a partir do HTML, e descartada. Processo no [`SKILL.md`](./SKILL.md); o que é deste projeto em [`references/projeto.md`](./references/projeto.md).

## Instalação

```
python -m pip install shot-scraper Pillow playwright
shot-scraper install          # baixa o navegador headless; repetir se o Playwright atualizar
```

A tela em vídeo pede também o FFmpeg com o `ffprobe` no PATH (https://ffmpeg.org/download.html; no Windows, `winget install Gyan.FFmpeg`). As conferências da forma vêm da skill `visual-form`, com os requisitos dela.

## As variáveis (só para o `--upload`)

A exportação local não pede chave. O `--upload` pede as da skill `r2-storage` (ver o README dela): `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET_<APELIDO>` (o apelido padrão é `conteudo`) e `R2_PUBLIC_BASE_<APELIDO>` (para os embeds na `legenda.md`). Elas vão no `.env` da raiz (a partir do `.env.example`) ou no bloco `env` do `.claude/settings.local.json`. Para conferir: `python -X utf8 scripts/confere_ambiente.py --skill slides-export --upload`.

- **Com `--upload` e sem a configuração:** o script para antes de exportar, com código 1 e a mensagem de cada variável que falta (para que serve, onde se pega, como se põe).
- **Sem `--upload` e sem as chaves:** a exportação segue e avisa uma vez que a proteção do publicado pelo bucket ficou desligada: o que já foi ao ar se reconhece só pelo registro da peça, e nada sobe.

## Como funciona

1. Lê `<pasta>/slides.html` e conta as `<section class="slide">` (ignora `.slide-num` e afins).
2. Gera no diretório temporário um YAML do `shot-scraper multi` com um bloco por tela pedida: ativa a tela `i`, zera o `transform` do `#stage`, esconde `#prev`, `#next` e `.pager`, pede as fontes, roda o `window.prepararSlide` da página (se houver) e captura o `#stage` numa janela de 1280 por 1560 (para a função `fit()` dos templates não encolher a captura).
3. Antes, roda as conferências do `conferir_telas.py` da `visual-form`; depois, o `shot-scraper` com a pasta do post como diretório de trabalho e com `--browser-arg --disable-lcd-text` (antialiasing em tons de cinza: sem a flag, o Chromium do Windows desenha a borda das letras com franja azul e laranja; a medida que separa os dois é a distância de cada pixel de tinta ao segmento entre a cor do papel e a da tinta; o `-webkit-font-smoothing` só age no macOS), e confere se cada arquivo saiu.
4. Com `--upload <apelido> <prefixo>`, chama a `r2-storage` para cada arquivo gerado.
5. Antes de publicar, registra na `legenda.md` o rótulo `**Imagens:**` e a seção `## Slides` com um embed por imagem: caminho relativo quando elas são só locais, URL pública depois do upload. Saída fora da pasta do post não registra nada.

## Antes e depois de publicar

**Antes de publicar**, o `--upload` sobrescreve no bucket os mesmos nomes (`<prefixo>/slide-NN.jpg`) e reescreve `**Imagens:**` e `## Slides` na `legenda.md`: é a mesma peça, ainda em produção.

**Depois de publicada, nada se sobrescreve e o registro só cresce.** O critério de publicada está em `references/projeto.md`. O que o código faz com ele:
- **carrossel:** o `ja_publicada()` do `export_slides.py` lê o `**Publicado:**` da `legenda.md` (pelo `publicada()` do `conferir_telas.py`; sem a `visual-form`, pela mesma leitura local, com aviso), e a peça inteira fica protegida;
- **Stories por API:** o `publicada_do_roteiro()` do `conferir_telas.py` lê a tabela "Publicada pela API" da seção `## Publicado` do `roteiro.md` e devolve só os Stories com linha. Com `--upload`, o `ids_no_bucket()` lê os ids de `stories/publicado/<data>/` no bucket (o do `--upload`, ou o do `--bucket-publicado`; só os objetos gravados a partir das 5h de Brasília do `data:` do roteiro; o id sai do nome sem a extensão e sem o sufixo `-miniatura`, o Story com música), e o `decidir_stories()` compara: id no bucket fora da tabela leva à sequência inteira;
- **Stories pelo app:** sem a tabela, a sequência inteira, pelo `estagio: publicado` ou `medido`, ou, com `--upload`, por algum Story do dia no bucket;
- **sem resposta do bucket** (sem rede): vale o roteiro, com aviso;
- **Stories com o `estagio` atrasado:** data já passada, sem a tabela, `estagio` que não é publicado nem medido e nada do dia no bucket: o `--upload` recusa (código 2), porque a sequência pode ter ido ao ar pelo celular sem o roteiro saber. Se foi ao ar, acerte `estagio: publicado` e rode de novo; se não, acerte a data.

Na tela publicada, o `--upload`:
- sobe para `<prefixo>/versoes/versao-N/slide-NN.jpg`. A versão 1 é a publicada, que fica onde está; N é o próximo número depois do maior que aparece no registro ou no bucket. No carrossel, o prefixo é o `**Prefixo no bucket:**` da `legenda.md`, que o script confere (recusa se for outro);
- com `--only`, a versão leva só as telas regeradas; as outras seguem da versão anterior;
- exige `--motivo "<o que mudou>"`, e sem ele termina com código 2, antes de exportar;
- não reescreve `**Imagens:**` nem `## Slides`;
- acrescenta uma linha `| N | AAAA-MM-DD | motivo | links das imagens |` na seção "## Versões depois de publicada" (criada no fim do arquivo na primeira vez) da `legenda.md` ou do `roteiro.md`. Se o upload falhar no meio, a linha entra marcada "(incompleta: subiram K de M)", e o script sai com erro; a próxima tentativa é a versão seguinte;
- passa pelas mesmas conferências: ERRO barra a versão nova também; na tela publicada, as hashtags, as regras da casa e as de área segura, zona proibida e travessão seguem como AVISO, e a sobreposição e a fonte que não carregou continuam ERRO.

A tela ainda sem publicar, numa sequência de Stories em que só parte saiu por API, sobe no próprio prefixo, com o mesmo nome; o `--motivo` só é pedido quando o `--upload` leva alguma tela publicada. Exportar uma peça publicada sem `--upload`, para revisão, deixa `**Imagens:**` e `## Slides` como estão, mas sobrescreve `images/`, a cópia de trabalho. A gravação na `legenda.md` e no `roteiro.md` preserva o fim de linha do arquivo.

## Saída

`images/slide-NN.mp4` na tela em vídeo; nas outras, `images/slide-NN.jpg` (qualidade 95, ajustável com `--quality`) em 1080 por 1350, ou `.png` com `--format png`. `--out-dir` muda a pasta, útil para testar sem tocar a pasta do post. Cada arquivo é conferido contra os limites da API do Instagram: só JPEG, até 8 MB, largura entre 320 e 1440 px, proporção entre 4:5 e 1.91:1 (confira na documentação da Meta, que muda). Fora do limite sai `[AVISO]`; arquivo que a API recusaria bloqueia o `--upload`.

## Tela em vídeo (`tela_em_video.py`)

A tela com `data-video="<segundos>"` na `<section class="slide">` sai em `images/slide-NN.mp4`; as outras seguem em JPEG. O atributo vale com aspas duplas, simples ou sem aspas. **Só no carrossel:** num `stories.html`, a proporção 9:16 fica fora da conferência do MP4 e barra o `--upload`.

**O quadro final parado (AVISO `fim_parado`):** na tela em vídeo que não é laço, a exportação mede quanto o fim fica parado, pela medida do `saltos.py` da `object-anatomy` (`tela_em_video.fim_parado`), e avisa abaixo de 3 s, a convenção da série. É AVISO, não barra o `--upload`. Quando não mede, a exportação diz por quê na linha `[--]` e segue: sem o `saltos.py`, sem o ffprobe no PATH (o ffmpeg pode ser o do `imageio_ffmpeg`, o mesmo da gravação, mas o ffprobe tem de estar no PATH), a medida que falhou (com o tipo do erro) ou o MP4 com menos de dois quadros decodificados, que não vira "parado 0,00 s". A dependência no `medir` do `saltos.py` está escrita na docstring dele.

- **O contrato da página:** `window.quadro(t, idx)` põe a tela `idx` (a partir de 0) no instante `t` (em segundos), sem depender do relógio do navegador: pode mexer no estilo, no atributo ou no `currentTime` de uma animação pausada (`element.animate(...)` com `pause()`), mas nada pode correr sozinho; animação ou transição em andamento para a gravação com erro. O estado parado da tela, sem chamar `quadro`, é o quadro final, completo. **A tela em laço** (o último quadro igual ao primeiro, para o vídeo emendar no carrossel) é a exceção: o estado parado, sem chamar `quadro`, é o instante que a página escolhe desenhar ao carregar, e não o fim, que volta ao começo; as conferências e o `--sem-video` seguem medindo o estado sem `quadro`. A gravação compara todos os quadros: o aviso "a animação não andou" sai só quando todos saem iguais, e a tela em laço sai com a linha `[--] em laço` (teste 16 do `teste_tela_em_video.py`). Os quadros vão de `t = 0` a `t = (n − 1) / fps`, então a animação acaba antes do fim e o fim fica parado.
- **A gravação:** o Chromium do Playwright, a mesma janela, o mesmo JS de preparação do JPEG e a mesma flag; para cada quadro, `quadro(i / fps, idx)` e a foto do `#stage`. A caixa do `#stage` precisa ter lados pares (o H.264 em 4:2:0 não aceita ímpar): a gravação confere antes de fotografar. O FFmpeg do PATH (ou o do `imageio_ffmpeg`) monta em H.264 high, `yuv420p`, 30 qps (`--fps`), GOP fechado de 1 s, sem quadros B e sem lista de edição (`-bf 0 -use_editlist 0`), teto de 20 Mbps e `+faststart`, sem áudio; `--som-mudo` põe uma faixa AAC muda de 48 kHz. Duas gravações dão os mesmos quadros.
- **A conferência do MP4** (`tela_em_video.py conferir`, e a cada exportação): MP4 com o `moov` antes do `mdat` e sem lista de edição (`elst`), H.264 ou HEVC, 4:2:0, progressivo, 23 a 60 qps, 3 a 60 s, até 100 MB e 25 Mbps, largura de 320 a 1440 px, proporção de 4:5 a 1,91:1, áudio ausente ou AAC até 48 kHz. Fora disso, o `--upload` não sobe; fora de 5 a 8 s, aviso; primeiro e último quadro iguais, aviso (a animação não andou). **Pede o `ffprobe` no PATH:** sem ele, a conferência não roda e o MP4 não sobe. **O perfil Story** (`tela_em_video.py conferir <arquivo.mp4> --story`): os mesmos limites, menos a largura e a proporção do carrossel, que dão lugar às do vídeo de Story (largura até 1920, proporção de 0,1:1 a 10:1, com aviso fora do 9:16) e sem o aviso dos 5 a 8 s; quem o usa é o `video_do_story.py` dos Stories (`marketing/social-media/stories/scripts/`), fora desta skill.
- **Nas conferências das telas**, a tela em vídeo é medida no estado parado, o quadro final; os quadros do meio não são medidos.
- **`--sem-video`** exporta a tela em vídeo como imagem, no quadro final: não apaga nada da `images/`, não grava na `legenda.md` e não vale com `--upload`.
- **Registro e bucket:** o `**Imagens:**` diz quantas telas são vídeo, e a `## Slides` traz o embed do MP4. Só depois de a exportação passar nas conferências, a `images/` perde o arquivo da mesma tela no outro formato (o JPEG da tela que virou vídeo, ou o MP4 da que deixou de ser). No bucket, o arquivo velho fica: a exportação avisa e dá o comando de remoção, que roda depois de confirmado na conversa, uma chave por vez.

## A fonte antes da medida (`fontes.py`)

Antes de medir cada tela, e de novo depois do `prepararSlide`, o script pede as fontes do texto dela (`document.fonts.load`, com o texto que as usa, também o dos `::before` e `::after`) e confere se a família existe mesmo, comparando a largura com a das fontes genéricas de reserva. A que não carregou sai `ERRO fonte_nao_carregada`, uma vez por tela para cada família, estilo e peso. Na tela em vídeo, a fonte que falta volta ao `export_slides.py`, que dá o mesmo ERRO: o MP4 de revisão sai na fonte de reserva e o `--upload` não sobe. Os apelidos da fonte do sistema de outro aparelho (`-apple-system`, `BlinkMacSystemFont`) não contam: a conta vai para a família seguinte. A regra vale para todo script que mede texto renderizado: o JavaScript está em `scripts/fontes.py` (`CARREGAR_FONTES`), para importar. Por quê: o `document.fonts.ready` resolve na hora quando nenhuma fonte foi pedida ainda, e a medida sai na fonte padrão do navegador sem avisar. Limite conhecido: a conta é por família, e a fonte da web dividida em subconjuntos (`unicode-range`) passa se um deles carregou.

## Testes

```
python -X utf8 .claude/skills/slides-export/scripts/teste_tela_em_video.py
```

Sem rede, sem bucket e sem chave: páginas mínimas num diretório temporário (o quadro pelo estilo e pelo `currentTime`, a animação solta, a caixa ímpar, o `elst`, as aspas do `data-video`, a fonte que não carregou) e uma peça mínima exportada (o `--sem-video`, a limpeza do formato velho, o PNG de revisão fora do registro). Os casos 13 e 14 usam o `saltos.py` da `object-anatomy` e pulam, com aviso, sem ela. Pede o `shot-scraper`, o Playwright com o Chromium e o FFmpeg com `ffprobe`; leva cerca de 40 s.

## Compatibilidade com os templates

Funciona com todo template que use `#stage`, `<section class="slide">`, `#prev`, `#next` e `.pager` (o da série de exemplo e o dos avulsos). Um template novo precisa manter esses ganchos ou passar `--selector`.
