# Mapas

> **Espaço sensível.** Um mapa junta numa página só carreira, relação, finanças e saúde. Antes do primeiro mapa, confira que o repositório é **privado**. O quadro de `board/` é local: abre no seu navegador e não se publica em link (nem GitHub Pages, nem bucket público, nem página compartilhada).

Os frameworks de autoconhecimento e de direção, pessoais e do negócio, preenchidos por você com o assistente. Ficam numa pasta própria, e não dentro de `health/` ou de `context/`, porque um mapa cruza áreas: pendurado numa delas, esconderia as outras.

## Os guias

Cada guia diz o que o mapa é, quando usar e onde preencher. Nenhum mapa vem preenchido: a pasta de cada um nasce no primeiro retrato.

| Mapa | Guia | Família | Tipo |
|---|---|---|---|
| Vision Board | [`guides/vision-board.md`](./guides/vision-board.md) | direção | retrato datado |
| Roda da Vida | [`guides/roda-da-vida.md`](./guides/roda-da-vida.md) | diagnóstico | retrato datado |
| Big Five (IPIP-NEO-120) | [`guides/big-five.md`](./guides/big-five.md) | diagnóstico | retrato datado, refeito a cada ano ou dois |
| SWOT (pessoal ou do negócio) | [`guides/swot.md`](./guides/swot.md) | diagnóstico | retrato datado |
| Ikigai | [`guides/ikigai.md`](./guides/ikigai.md) | diagnóstico | retrato datado |
| Matriz EREC | [`guides/erec.md`](./guides/erec.md) | direção | retrato datado |
| OKR | [`guides/okr.md`](./guides/okr.md) | direção | vivo, por período |

## A ordem sugerida

A ordem segue a dependência, e não a data em que cada mapa foi criado:

1. **Vision Board** primeiro, porque não depende de nenhum outro, e distância e oportunidade só se medem contra um destino dito antes.
2. **Roda da Vida**, que depende só do destino.
3. **Big Five**, que não depende de nenhum e vem antes da SWOT, onde os traços são usados.
4. **SWOT**, com o destino e os traços na mão.
5. **Ikigai**, uma síntese dos anteriores, numa passada só.
6. **Matriz EREC**, que parte do Ikigai: o que eliminar, reduzir, elevar e criar.
7. **OKR**, quando houver um resultado que se mede.

Mapa preenchido fora da ordem vale como primeiro retrato e se refaz depois.

## Os dois tipos

- **Retrato datado:** uma pasta por mapa, com um arquivo por data (`maps/roda-da-vida/AAAA-MM-DD.md`), nunca sobrescrito. O valor está na série: o retrato de hoje se lê contra o do ano passado.
- **Vivo:** um arquivo por período (o OKR do trimestre), atualizado no lugar durante o período, com `revisado_em: AAAA-MM-DD` no frontmatter.

## As três regras

1. **O markdown é a fonte, e a página é derivada.** O quadro em `board/` se desenha a partir do arquivo e muda na mesma entrega. Quem lê a máquina lê o markdown; a página serve à tela e à parede.
2. **O mapa aponta, sem copiar.** A evidência fica onde já mora (o registro de treino, o mês das finanças, uma nota), e o mapa cita o caminho. O que dois mapas têm em comum mora num só: os traços no Big Five, as forças na SWOT, o sentido no Vision Board.
3. **Cada item diz de quem é.** O que você reconheceu é seu; a leitura ou o plano do assistente fica marcado "a testar" ou "proposto" até você assumir. Sem isso, um quadro na parede apresentaria sugestão como convicção.

**O assistente não estima traço de personalidade pela conversa.** O resultado do Big Five vem do instrumento que você respondeu; palpite sobre personalidade num quadro vira rótulo.

**Candidato não ganha arquivo.** Um mapa que você talvez faça um dia fica nesta tabela; a pasta nasce quando ele for preenchido.

## O quadro (`board/`)

Uma página em HTML com SVG, desenhada para este modelo, com os tokens em `board/tokens.css` e os modelos em branco da Roda da Vida e do Ikigai. Abra o `board/index.html` no navegador. Quando um mapa for preenchido, o assistente desenha a página dele a partir do markdown, nos mesmos tokens, num arquivo novo, `board/<mapa>-AAAA-MM-DD.html`; o modelo em branco fica intocado. Porquê de tudo isto em [`decisions/vida-pessoal-e-mapas.md`](../decisions/vida-pessoal-e-mapas.md).
