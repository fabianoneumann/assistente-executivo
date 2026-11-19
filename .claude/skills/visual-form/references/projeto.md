# O que é deste projeto

O arquivo da skill com o que muda de projeto para projeto: as réguas de cada formato, as pastas, os caminhos das outras skills e os comandos. O `SKILL.md`, o `i2.md`, o `criterio.md` e o `conferencias.md` guardam o método; o que é deste repositório (que régua, que comando, que pasta) mora aqui. Para usar a skill noutro projeto, troca-se esta folha. Não é configuração: é a régua de hoje, escrita uma vez. **Quando esta folha e o design system da série discordarem, vale o design system,** e a diferença vai ao relatório da forma, para corrigir aqui.

## A série de exemplo

O repositório traz uma série em branco, `marketing/social-media/carousels/series/exemplo/`, para você copiar e preencher: o `README.md` diz o que é uma série e o que preencher; o `design-system.md` tem as seções a decidir; a pasta `design/` tem uma identidade neutra de partida (o `caderno.css`, o `caderno.js` e o `papeis.json`), que as conferências desta skill leem; e o `exemplo-de-post/slides.html` é um post de duas telas que passa nas conferências com 0 ERRO, para servir de "publicado mais recente" na primeira peça. Série nova: copie a pasta inteira com o nome da série, troque a identidade e preencha o design system antes da primeira peça.

## As réguas, por formato

| Formato | A régua | Para montar |
|---|---|---|
| Carrossel da série | o `design-system.md` da série (as tintas, a letra, a grade, as anotações, as regras da casa, "Como montar um post"), os valores em `design/caderno.css`, o assentamento em `design/caderno.js` e a tabela de papéis em `design/papeis.json`; as regras de desenho (o que é a lápis, o que é a caneta, o objeto que se move) na seção "Imagem e desenho" do design system, ou num `design-system-desenho.md` ao lado, quando a série o tiver | copiar o `slides.html` publicado mais recente do mesmo tipo das pastas datadas da série; na primeira peça, o `exemplo-de-post/slides.html` |
| Carrossel avulso | a identidade escolhida na primeira mesa da peça, com as mesmas conferências; as peças em `marketing/social-media/carousels/standalone/` | o avulso publicado da mesma identidade, se houver |
| Sequência de Stories | `marketing/social-media/stories/README.md`: "O topo e os adesivos" (a área segura do texto essencial de y 192 a 1802 e de x 32 a 1048, e os adesivos na posição padrão do app, simulados no `adesivos.css`), "Os desenhos de enfeite" (o `desenhos.json` da pasta e o `marketing/social-media/stories/scripts/espacos.py`, que põe cada desenho no maior vazio da tela) e "A forma dos Stories"; a régua da série vale no resto | o modelo `marketing/social-media/stories/template/stories.html`, copiado para a pasta e renomeado `stories.html`; o texto fica acima do adesivo |
| Story em vídeo | o banco de animações e o estado de cada uma em `marketing/social-media/stories/animacoes.md`; o Story em vídeo segue o vídeo (um estilo só) | gravado pelo `marketing/social-media/stories/scripts/anima_cena.py`, fora da `slides-export`; todo MP4 de Story passa pelo `video_do_story.py` da mesma pasta (o `anima_cena.py` o chama depois de gravar): os limites do Story na API como ERRO, e o `saltos.py` e a folha de quadros a 0, 30, 60 e 90% como leitura, com os números no `refinamentos.md`; com o `roteiro.md` da sequência, os AVISOs do tempo de leitura frase a frase da tabela de tempo e da legenda revisada do vídeo com voz (`--roteiro` roda antes de gravar); no vídeo de câmera, o estilo e o lugar da legenda vão a quem decide, com um quadro de cada opção |
| Story avulso | só a simulação do `stories.html` que o README manda para o Story montado no app, com as conferências em 0 ERRO; sem alternativas e sem I2 | o avulso anterior da mesma função |

**As réguas de juízo:** `marketing/social-media/rubrica-de-design.md` (carrossel) e `marketing/social-media/rubrica-de-stories.md` (Stories); as lições de forma das peças em `marketing/licoes.md`, na etapa da forma.

**O banco de imagens:** a lista do que já foi gerado ou fotografado, com o que mostra e onde entrou, é a da `image-gen` (o `references/projeto.md` dela diz onde fica). Consulte antes de gerar.

## A base que a forma não pode deixar de ler

O que a etapa confere ou que já deu lição, em `knowledge/content-design/` e `knowledge/agent-engineering/`, se as sínteses estiverem no repositório: o texto que cabe e a legibilidade, a quebra de linha em tela, o layout de peças em HTML, a metáfora visual e a demonstração, os princípios de design visual, o juiz de visão julgando design e os defeitos no lugar da nota. Onde cada uma entra está no `criterio.md`. A síntese que faltar na base não para a forma: o `criterio.md` traz a regra que importa, e a falta vai ao relatório.

## As outras skills

| Skill | Para quê | Onde ler |
|---|---|---|
| `image-gen` | a imagem que o banco não tem: os geradores pela tabela dela, a conferência da imagem, o banco de imagens e o `prompts.md` da peça | `.claude/skills/image-gen/SKILL.md` e o `licoes.md` dela |
| `object-anatomy` | o objeto que se move; o pedido, a devolução e o contrato do encaixe | `.claude/skills/object-anatomy/SKILL.md` e `references/projeto.md` ("O encaixe na tela da peça") |
| `slides-export` | a exportação local, a tela em vídeo e o `fontes.py`, que as conferências desta skill importam; ela chama as conferências desta skill (`scripts/conferir_telas.py`) antes da foto | `.claude/skills/slides-export/SKILL.md` e o `licoes.md` dela |
| `r2-storage` | baixar do banco uma imagem já gerada; subir o que as regras mandam no caminho (a imagem gerada ao banco, pela `image-gen`; a prévia de cada passada dos Stories, pelo README deles), nunca o `--upload` do fechamento | `.claude/skills/r2-storage/SKILL.md` |
| `base-enrichment` | a passada de método pela base na camada forma (passo 7) | `.claude/skills/base-enrichment/SKILL.md` |

## Os comandos

Da raiz do repositório, com `python -X utf8`. As saídas de trabalho (exportações, quadrantes, folhas) vão a uma pasta fora do repositório (a pasta temporária do sistema serve); os arquivos da medida, a `medida/` da peça.

```
python -X utf8 .claude/skills/visual-form/scripts/conferir_telas.py <pasta>                       # nos Stories: <pasta> stories.html
python -X utf8 .claude/skills/visual-form/scripts/medir_blocos.py <pasta>                         # nos Stories: <pasta> stories.html
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta> --out-dir <trabalho>   # a prévia local, sem --upload
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta> --html stories.html --height 1920 --previa --out-dir <trabalho>
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <pasta> --sem-video --out-dir <trabalho>   # a tela em vídeo como o quadro final
python -X utf8 .claude/skills/object-anatomy/scripts/juntas.py <pasta> --saida <trabalho>            # o zoom de 4x nas junções do objeto encaixado
python -X utf8 .claude/skills/object-anatomy/scripts/saltos.py <arquivo.mp4>                         # o vídeo sem salto nem fim parado fora da regra
python -X utf8 marketing/social-media/stories/scripts/espacos.py <pasta> --html stories.html        # os desenhos de enfeite nos vazios
python -X utf8 marketing/social-media/stories/scripts/video_do_story.py <story.mp4>                # todo vídeo de Story: os limites da API, o saltos.py e a folha de quadros
python -X utf8 marketing/social-media/stories/scripts/video_do_story.py --roteiro <roteiro.md>    # antes de gravar: o tempo de leitura frase a frase e a legenda revisada
ffmpeg -ss <segundos> -i <tela.mp4> -frames:v 1 <trabalho>/quadro-<pct>.jpg                         # um quadro do MP4, a 0, 30, 60 e 90% da duração (a duração: ffprobe)

python -X utf8 .claude/skills/visual-form/scripts/mede_forma.py <pasta>/slides.html <pasta>/medida/medidas.json [--estatico] [--fora <seletor>] [--desenho <seletor>]
python -X utf8 .claude/skills/visual-form/scripts/trava_i2.py <medidas.json> <i2-relatorio.md> [--reconferencia <md> --anterior <trava.json anterior>] [--falha-objetiva N:motivo] --json <trava.json>
python -X utf8 .claude/skills/visual-form/scripts/prepara_i2.py zoom <dir dos JPEG> <dir de saída>
python -X utf8 .claude/skills/visual-form/scripts/prepara_i2.py semtexto <slides.html> <dir de saída> <nome>
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <dir de saída> --html <nome>.html --sem-conferir --sem-video --out-dir <trabalho>/sem-texto   # o esqueleto (sem conferir: o texto transparente acusaria contraste)
python -X utf8 .claude/skills/visual-form/scripts/folha_de_contato.py <saida.jpg> nova=<dir> <publicada>=<dir> ...
```

**A instalação:** `pip install -r .claude/skills/visual-form/requirements.txt` e depois `python -m playwright install chromium` (o navegador das conferências e das medidas). O `ffmpeg` vem pelo pacote da `slides-export` ou do sistema. Nenhuma chave: esta skill não chama API.

**Os testes da skill** (a cada edição dos scripts), na pasta `scripts/`: `teste_trava_i2.py`, `teste_ferramentas_i2.py` e `teste_papeis.py` (sem rede nem navegador, em segundos); `teste_mede_forma.py` (uns 15 s com o Chromium; `--sem-navegador` só a parte do HTML); `teste_medir_blocos.py` e `teste_conferir_telas.py` (com o Chromium, cerca de um minuto; pedem a `slides-export` instalada ao lado, pelo `fontes.py` e pelo `export_slides.py`). O `trava_i2.py` lê o relatório no formato do pedido do `i2.md`; mudar o formato lá pede mudar o leitor e o teste juntos. O caso fixo do teste da trava (uma peça de dez telas e o relatório da I2 sobre ela) está em `scripts/casos/i2/`.

## O que este projeto precisa ter e ainda não tem

- **A parte em código da rubrica de Stories, com o Jev** (o avaliador que confere o dia relativo e a referência implícita a um dia, e lê a imagem com os adesivos simulados): não vem nesta versão. Até lá, o `conferir_telas.py` confere o dia relativo pelas palavras da lista dele (`PALAVRAS_DO_DIA`), e o resto da rubrica de Stories é leitura. Proposta: `scripts/jev/stories.py`, com a lista de palavras lida de um lugar só.
- **Uma ferramenta que compare o texto entre versões de uma peça** (o que mudou de uma versão da forma para a outra): não vem; o AVISO `texto_fora_do_travado` cobre a versão final contra o travado.
