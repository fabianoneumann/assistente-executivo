# As conferências: como ler cada uma e o que conta como passar

As três conferências do objeto (a interseção, as pontas e o zoom de 4×) e a câmera lenta do vídeo, mais a leitura dos recortes. **O zero de um script é necessário, não suficiente:** a leitura a 4× é parte da conferência, e cada recorte lido entra no relatório com o que se viu nele. Os comandos estão em [`projeto.md`](projeto.md); o `intersecao.py`, o `juntas.py` e o `saltos.py` moram nesta skill; a ponta da seta é um AVISO da conferência da forma (`medidas_forma.py`, na `visual-form`), que daqui só se lê.

## 1. A interseção (`scripts/intersecao.py`, R20): antes de qualquer render

**O que lê:** o `object/pecas.json` que o script de geometria exporta, do mesmo modelo que move a página (R10, R14). Cada peça é um polígono simples num plano (o perfil da peça de revolução, a vista de frente do mecanismo plano, a planta da peça em camadas), com uma faixa opcional de profundidade fora do plano; os estados são o repouso e cada quadro da explosão e do movimento, com o deslocamento e o giro de cada grupo. O formato inteiro está no docstring do script.

**Qual plano escolher:** o que mostra o atravessamento verdadeiro. Peça de revolução em volta de um eixo comum: o perfil (x, r), e duas peças se atravessam se, e só se, os perfis se sobrepõem. Mecanismo que corre num plano (alavanca, engrenagem de frente, carro em trilho): a vista desse plano, com a profundidade de cada camada na faixa. Objeto em camadas empilhadas: a planta, com a altura na faixa. Se nenhum plano basta (peças que se cruzam em ângulo), diga no relatório que a prova é parcial, e qual parte do objeto ficou sem ela.

**Os estados:** o repouso, cada quadro do vídeo (a 30 por segundo, todos) e, na vista explodida, pelo menos 100 posições do caminho inteiro de ida e volta. O par que não se move um em relação ao outro não se mede de novo, então os quadros a mais custam pouco.

**Passa quando:** a saída é 0 (nenhum atravessamento fora dos declarados). Cruzamento de propósito (a haste que passa pelo furo) se declara no próprio `pecas.json`, com o porquê e o `fundo_max`; a declaração que nunca cruza sai em AVISO e se confere. Saída 1: a skill corrige a geometria e roda de novo, **antes de renderizar qualquer imagem**; não se desenha por cima de um atravessamento. Saída 2: o `pecas.json` está inválido, e se corrige o exportador.

**O apoio (R8)** não é deste script: o script de geometria lista, no repouso, as peças que não tocam nenhuma outra (até a tolerância), e a lista vai ao `confere.json` como `soltas`, que tem de sair vazia (a peça que fica no ar de propósito, como um ponteiro preso por um eixo desenhado, se declara com o porquê).

## 2. A ponta de linha (R19)

- **A ponta da seta:** o AVISO `ponta_da_seta` do `conferir_telas.py` (a seta do rótulo entra de 20 a 30 px no alvo; o conector encosta). Rode o `conferir_telas.py` na `tela.html` e leia só os achados do desenho (`ponta_da_seta`, a sobreposição de texto com o `svg`); os de texto e de ocupação da tela são da forma, depois do encaixe.
- **Toda ponta de traço do desenho:** cada uma tem de terminar num traço, num ponto, num contorno ou sumir em degradê. O `juntas.py` (abaixo) lê duas pontas por elemento (o começo e o fim do `path`), então serve às setas e aos traços soltos, um por `path`; as arestas que o `iso.js` junta num `path` só não saem nele. No objeto do `iso.js`, e em todo objeto de muitas peças, meça no navegador (1 px até outro traço ou preenchimento pintado depois; marca curta enraizada a 2 px; ponta livre declarada) e grave a contagem no `confere.json` como `pontas` (o total, as em traço, as em face, as livres e as soltas, que têm de ser 0), com um autoteste que planta uma ponta solta e confere que ela sai.

## 3. O zoom de 4× (`juntas.py`, R18)

**O que faz:** fotografa a tela a 4× e recorta em volta de cada ponta de traço aberto e de cada ponta e saída de seta livre, com um `juntas.md` na ordem de leitura (até 40 recortes por tela; o `juntas.md` diz quantos ficaram de fora). Não julga.

**Como ler, recorte por recorte, nesta ordem:** a linha que entra em algo; o cruzamento na ordem errada (a de trás passando pela frente); a ponta pousada no contorno de outra linha; a peça afundada ou solta; a textura que para no meio. Leia o estado parado (o quadro final) e, no vídeo, os quadros em que cada junta importa (a peça que acabou de assentar), tirados do MP4 com o `ffmpeg`. O `juntas.py` mede o estado parado; os encontros que só existem no meio do movimento, a skill recorta dos quadros.

**Passa quando:** cada recorte lido tem uma linha no relatório (o recorte, o que se viu, e a correção, se houve), e nenhum defeito ficou sem correção ou sem o porquê. Recorte que não prova nada (a junta coberta por outra peça naquele instante) se troca pelo instante em que ela aparece.

## 4. A câmera lenta (`saltos.py`, R21): só no vídeo

**O que faz:** decodifica o MP4 e mede a diferença média entre quadros seguidos; o salto sai como pico isolado, o pulso do quadro-chave do H.264 se marca à parte, e o fim parado se conta em quadros e segundos.

**Junto:** uma folha de 12 a 24 quadros tirados do MP4 (não da página), lida em sequência: sem corte, sem troca súbita de cor, sem peça que some e volta.

**Passa quando:** nenhum pico isolado fora do quadro-chave, ou cada um explicado como mudança de propósito (um contador que começa; nunca uma forma que salta nem uma palavra que troca sem envelope); e o fim parado dentro do contrato (a animação acaba antes do último quadro, e o último quadro é o estado parado da tela, a mesma imagem que as conferências medem; quanto tempo fica parado é escolha da peça, e o número vai ao relatório).

## O `confere.json`

Um arquivo só, na pasta `object/`, com o resultado de cada conferência na versão final, para quem chama ler sem rodar nada:

```json
{
  "pecas": 0, "porGrupo": [["grupo", 0]],
  "intersecao": {"codigo": 0, "estados": 0, "problemas": 0, "declarados": []},
  "soltas": [],
  "pontas": {"pontas": 0, "emTraco": 0, "emFace": 0, "livres": 0, "soltas": 0, "autoteste": "2 de 2"},
  "ponta_da_seta": {"avisos": 0},
  "juntas": {"recortes": 0, "lidos": 0, "defeitos_corrigidos": 0},
  "video": {"segundos": 0, "quadros": 0, "picos": 0, "parado_s": 0}
}
```

Campo que não se aplica (a tela parada não tem `video`; o objeto pequeno pode não medir todas as pontas) sai com `"nao_se_aplica": "<porquê>"` no lugar dos números, nunca omitido nem zerado: ausente não é zero.

## Onde estão o `juntas.py` e o `saltos.py`, e os testes deles

Os dois moram em `scripts/` desta skill. O `juntas.py` (R18) recorta a 4× as pontas e as saídas de seta e as pontas de traço aberto, com um `juntas.md` na ordem de leitura (até 40 recortes por tela), e não julga: é o olho a 4×. O `saltos.py` (R21) mede a diferença entre quadros seguidos do MP4 e o fim parado. O AVISO da ponta da seta é da conferência da forma (`medidas_forma.py`, na `visual-form`), que daqui só se lê. Os testes: o do `juntas.py` está no `teste_conferir_telas.py` da `visual-form`, e o do `saltos.py`, no `teste_tela_em_video.py` da `slides-export`.
