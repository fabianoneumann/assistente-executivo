---
titulo: "Implement support for off-screen rendering (godot-proposals #5790)"
tipo: artigo
autor: "Hugo Locurcio, Calinou (godotengine/godot-proposals)"
url: "https://github.com/godotengine/godot-proposals/issues/5790"
publicado_em: 2022-11-15
capturado_em: 2026-11-13
licenca: "texto de issue do GitHub, sem licença declarada; nota de fato, sem o integral"
areas: [generative-media]
entrada: pesquisa
tags: [godot, movie-maker, headless-render, offscreen]
---

# Godot: o Movie Maker precisa de janela, e o render fora da tela segue em proposta

Nota de fato: o texto integral não entra (licença abaixo); a cópia de trabalho fica fora do repositório.

**Proveniência.** Corpo da proposta, aberta em 15/11/2022 por Hugo Locurcio, membro da organização do Godot no GitHub e autor do repositório de demonstração do Movie Maker (Calinou/godot-movie-maker-demo), ainda aberta em 13/11/2026 (última atualização em 08/10/2026, 38 comentários, não lidos); cópia de trabalho na cópia de trabalho. Os dados da issue (autor, vínculo com a organização, datas, número de comentários) vêm da resposta da API do GitHub, guardada na cópia de trabalho. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado).

**Em uma frase:** no Godot, o Movie Maker e qualquer captura de cena renderizada precisam abrir uma janela, porque o `--headless` desliga todo o código de render; o modo fora da tela é proposta aberta desde 2022.

| Ponto | O que a fonte diz |
|---|---|
| O limite | o Movie Maker exige uma janela; ela não pode mudar de tamanho durante a gravação |
| `--headless` | não abre janela nem pede GPU, mas desliga o render |
| A proposta | um `--offscreen` que renderiza sem janela visível, incompatível com o `--headless`; ainda exige uma GPU acessível, a menos que um Vulkan por software (Lavapipe, SwiftShader) faça o papel dela |
| No Windows | o sistema é menos exigente com a interface, mas a janela ainda aparece na barra de tarefas durante a gravação |

**Lacuna:** a proposta não diz quando entra, e os comentários não foram lidos.

**Conferência lado a lado:** 5 de 6 unidades seguem frases da fonte na ordem dela (a frase de abertura e as quatro células de texto corrido; a lacuna é nossa). É página técnica que lista fatos, em inglês, com a ficha em português: o `parafrase.py` não mede tradução, e a conta é esta.
