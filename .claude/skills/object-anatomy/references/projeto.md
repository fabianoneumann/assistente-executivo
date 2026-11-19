# O que é deste projeto

O único arquivo da skill com o que é deste repositório: a série, o traço, as cores, os caminhos. O método ([`metodo.md`](metodo.md)) e as conferências ([`conferencias.md`](conferencias.md)) não dependem disto; para usar a skill noutro projeto, troca-se só esta folha. Não é configuração: é a régua de hoje, escrita uma vez. Onde a régua da série e esta folha divergirem, vale a da série (o `design-system.md` dela, e o `design-system-desenho.md` ao lado, quando a série o tiver), e a divergência vai ao relatório.

## A série e os caminhos

O repositório traz uma série em branco, `marketing/social-media/carousels/series/exemplo/`, com uma identidade neutra de partida. Cada série nova é uma cópia dela, com nome próprio; os caminhos abaixo usam a de exemplo, e quem chama diz qual é a série da peça.

| O quê | Onde |
|---|---|
| A régua do desenho (o objeto, o papel opaco, os rótulos, o apoio, o traço do objeto em movimento, a convenção do vídeo) | a seção "Imagem e desenho" do `design-system.md` da série, ou o `design-system-desenho.md` ao lado, quando a série o tiver; na série de exemplo, as regras de traço desta folha (abaixo) valem até a série decidir as suas |
| As tintas, a letra, a grade, o papel | o `design-system.md` da série, e os valores em `design/caderno.css` da mesma pasta (os tokens em `:root`: `--tinta`, `--acento`, `--apoio`, `--papel-a`, `--papel-b`) |
| O CSS e o JS do caderno | `marketing/social-media/carousels/series/exemplo/design/caderno.css` e `caderno.js`; da pasta `object/` de uma peça da série (`series/<série>/<peça>/object/`), `../../design/caderno.css`; de uma peça de Stories (`marketing/social-media/stories/<data>/object/`), `../../../carousels/series/<série>/design/caderno.css`; de um carrossel avulso (`marketing/social-media/carousels/standalone/<peça>/object/`), `../../../series/<série>/design/caderno.css`; numa página interativa ou artifact, que não lê arquivo local, o CSS do caderno embutido na página |
| Uma tela publicada para copiar a estrutura (cabeça, `#stage`, `section.slide`, o `window.quadro` no pé) | no carrossel, uma tela do `slides.html` mais recente da série (na série nova, o `exemplo-de-post/slides.html`), com o `window.quadro(t, idx)` acrescentado no pé como diz "O vídeo", abaixo; nos Stories, o modelo `marketing/social-media/stories/template/stories.html` (1080 × 1920) |
| O contrato da tela em vídeo do carrossel | o docstring de `.claude/skills/slides-export/scripts/tela_em_video.py` |
| O contrato da cena dos Stories | o docstring de `marketing/social-media/stories/scripts/anima_cena.py` |
| O kit do Anatomy (só como prova, nunca instalado nem rodado por esta skill) | o repositório público dele (o endereço e o commit estão no `metodo.md`), baixado por quem pediu, numa pasta fora do projeto, quando a pessoa der o ok |

## O traço

Os nomes de classe são os do `caderno.css` da série de exemplo; a série que tiver outros nomes os diz no design system.

- **Traço em SVG,** sem tremor nem filtro no objeto: `<svg class="traco">`, contorno com a classe `c` (`--tinta`), detalhe com `f` (mais fino), a peça acesa com `l` (`--acento`). O SVG deixa o `conferir_telas.py` medir o texto contra o desenho; canvas fica fora (a sobreposição não se mede nele).
- **O assunto no acento:** só a peça acesa (o que empurra, o que cai, o que passa) é quente; o resto fica na tinta.
- **Papel opaco liso:** toda face preenchida com o papel da tela (`var(--papel-b)` no tipo B, `var(--papel-a)` no tipo A), sem tom. No `iso.js`, sem estilo o `pinta` já sai assim, no `var(--papel-b)` com o contorno em `var(--tinta)` (os tokens do `caderno.css` da série de exemplo); no tipo A, `ISO.pinta(cam, solido, {estilo: ISO.estiloPapel('var(--papel-a)'), aresta: 'c'})`. A série com outros nomes de token passa os dela no `estiloPapel(papel, tinta, traço)`. O tom pela normal (`{tom: true}`) só entra se quem chama pedir a variante com tom (abaixo).
- **O objeto inventado é ilustração;** quando a peça documenta uma máquina real, ela se desenha pela ficha (R6). Antes, o objeto passa pelo filtro do passo 0 do `SKILL.md`: o aparelho que só existe para representar a ideia não é caso desta skill (a analogia com um objeto real que funciona, sim).
- **A linha de detalhe mais fina** (para o objeto de muitas peças) não é token: se precisar, diga no relatório o peso usado e onde.
- **O sombreado não entra por conta própria.** Só quando quem chama pedir a variante com tom: uma segunda página ao lado (`tela-tom.html`), com dois tons da tinta escritos ali (dois degraus claros, sem degradê), nunca em `caderno.css` (o token nasce depois da prova, se a série o adotar). Nenhum texto sobre o tom.

## A caixa

O objeto que é a explicação pede a **tela inteira**, e o texto vai na tela vizinha: numa coluna estreita, as peças pequenas somem no celular. Sem caixa no pedido, a skill desenha na tela inteira, com a margem da área segura; a faixa menor só quando o texto cabe em volta sem encolher as peças: as nomeadas pelo texto ficam legíveis no tamanho do celular, e o relatório diz quando não ficam.

## Palavras, rótulos e setas

- **Rótulo só para a peça que o texto da tela nomeia,** até quatro, na margem, na letra das notas da série; a peça que o texto não usa não ganha rótulo.
- **A seta do rótulo** é `path` com a classe `seta-livre` (o `caderno.js` da série desenha a ponta), e a ponta entra de 20 a 30 px no alvo; o conector entre dois desenhos só encosta (até 12 px). O AVISO `ponta_da_seta` do `conferir_telas.py` mede as duas.
- **Texto da tela não é desta skill:** o título, o corpo e a nota vêm travados da escaleta da peça. A página da skill só leva o objeto, os rótulos que o texto nomeia e os números que o modelo gera (R14), e o lugar do texto fica vazio, marcado, para a forma encaixar.

## O encaixe na tela da peça

- **O objeto sai no tamanho da tela final:** num `svg` com o `viewBox` da tela inteira, na caixa que o pedido dá em coordenadas da tela (ou na que a skill escolhe e diz), com o traço já na escala da tela; o `monta` desenha o quadro final. O encaixe não escala o desenho.
- **Um modelo só, carregado, nunca copiado:** o `slides.html` (ou o `stories.html`) carrega `object/iso.js` e `object/geometria.js` por `<script src>`, chama `OBJETO.monta(svg)` no `svg` da tela e, no próprio `window.quadro(t, idx)`, `OBJETO.quadro(t)` quando o `idx` é o da tela do objeto (nos Stories, no `window.quadro(t)` da cena do objeto). Se a peça já tem um `window.quadro` para outra tela, a chamada entra nele.
- **Depois do encaixe, as conferências rodam de novo na peça,** por quem encaixa (`.claude/skills/visual-form/SKILL.md`, passo 4).

## A página interativa

Só no formato "página interativa" (aula, artifact): o mesmo `geometria.js`, com um laço próprio só nessa página (o `requestAnimationFrame` que chama `OBJETO.quadro`), o movimento reduzido (R17: um quadro parado representativo, e a figura ainda responde) e o CSS do caderno embutido. A `tela.html` gravada continua sem laço.

## O vídeo

- **A página segue o contrato da gravação:** `window.quadro(t, idx)` no carrossel (o `tela_em_video.py`, chamado pelo `export_slides.py`) e `window.quadro(t)` nos Stories (o `anima_cena.py`, uma tela por gravação); a `section.slide` da tela em vídeo leva `data-video="<segundos>"`. O estado parado, sem chamar `quadro`, é o quadro final, completo, e é o que as conferências das telas medem.
- **Nada corre sozinho:** nem animação CSS, nem `requestAnimationFrame` próprio, nem `setInterval`. Tudo sai do `t`.
- **Duração:** de 5 a 8 s na tela do carrossel (a gravação aceita de 3 a 60); nos Stories, a duração que quem chama pedir. 30 quadros por segundo.
- **Formato:** 1080 × 1350 no carrossel, 1080 × 1920 nos Stories.

## Os comandos

Da raiz do projeto. Nenhuma chave: esta skill não chama API. Pede o Python com o Playwright e o Chromium (o `requirements.txt` da `visual-form`, com o passo `python -m playwright install chromium`), o Pillow e o numpy, o `node` (para o `geometria.js` exportar o `pecas.json` e para o `teste_iso.js`) e o `ffmpeg` (pelo `imageio-ffmpeg` da `slides-export`, ou do sistema) para o vídeo.

```
python -X utf8 .claude/skills/object-anatomy/scripts/intersecao.py <peça>/object/pecas.json
python -X utf8 .claude/skills/object-anatomy/scripts/juntas.py <peça>/object tela.html --saida <trabalho>/juntas
python -X utf8 .claude/skills/slides-export/scripts/export_slides.py <peça>/object --html tela.html --out-dir <trabalho>/video --sem-conferir
python -X utf8 .claude/skills/object-anatomy/scripts/saltos.py <trabalho>/video/slide-01.mp4
python -X utf8 .claude/skills/visual-form/scripts/conferir_telas.py <peça>/object tela.html --json
python -X utf8 marketing/social-media/stories/scripts/anima_cena.py <peça>/object/tela.html <trabalho>/video/cena.mp4 --segundos 6 --altura 1920
```

O `anima_cena.py` confere, depois de gravar, os limites do vídeo de Story na API (o `video_do_story.py` ao lado dele): a cena de menos de 3 s sai com código 1 e o ERRO, e o MP4 fica, para a leitura; o ERRO só pesa quando o vídeo vai publicado sozinho. O `--out-dir` fora da pasta da peça é o que impede o `export_slides.py` de gravar na `legenda.md` (ela é do roteiro e da exportação final, não desta skill). Nunca `--upload`. A pasta de trabalho (`<trabalho>`) é a que quem chama der; sem ela, uma pasta nova em `tempfile.gettempdir()`, fora do projeto.

**Os testes da skill** (a cada edição dos scripts), na pasta `scripts/`: `python -X utf8 teste_intersecao.py` (sem rede nem navegador) e `node teste_iso.js`. O teste do `juntas.py` está no `teste_conferir_telas.py` da `visual-form`, e o do `saltos.py`, no `teste_tela_em_video.py` da `slides-export`.
