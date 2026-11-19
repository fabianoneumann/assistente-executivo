# Vision Board

**O que é:** um painel com o destino que você quer para os próximos anos, em imagens e frases curtas. É uma prática difundida, sem um autor único. Aqui ele serve de **destino**: os outros mapas medem distância e oportunidade contra o que você disse que quer.

**Quando usar:** antes dos outros mapas, porque não depende de nenhum. Refaça quando o destino mudar, ou uma vez por ano.

**Como montar:** para cada área da vida que importa agora, uma frase no presente ("moro perto do mar", "trabalho quatro dias por semana") e, se quiser, uma imagem que você tem o direito de usar (uma foto sua, uma imagem livre, ou uma gerada pela skill `image-gen`, salva na pasta do Vision Board e nunca no bucket, que costuma ter endereço público). Acrescente o sentido: por que esse destino importa para você.

**Onde preencher:** `maps/vision-board/AAAA-MM-DD.md`, um arquivo por versão, nunca sobrescrito. As imagens ficam na mesma pasta, em `AAAA-MM-DD/`.

```markdown
---
mapa: vision-board
data: AAAA-MM-DD
horizonte: <em quantos anos>
---

# Vision Board: AAAA-MM-DD

**O sentido:** <por que esse destino importa>

| Área | O destino, no presente | Imagem |
|---|---|---|
```
