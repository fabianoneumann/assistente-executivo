---
titulo: "Rhubarb Lip Sync (README do repositório)"
tipo: artigo
autor: "Daniel Wolf (DanielSWolf/rhubarb-lip-sync)"
url: "https://github.com/DanielSWolf/rhubarb-lip-sync"
publicado_em: null   # README sem data; o estado do repositório vai na proveniência
capturado_em: 2026-11-13
licenca: "MIT (LICENSE.md do repositório: o Rhubarb é MIT, as dependências MIT, BSD ou parecidas, e os dados de lip sync gerados são do usuário; a API do GitHub não reconhece o arquivo, que junta várias licenças); o integral está na url"
areas: [generative-media]
entrada: pesquisa
tags: [lip-sync, 2d-character, cli, audio]
---

# Rhubarb Lip Sync: as bocas 2D tiradas do áudio, pela linha de comando

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório e o LICENSE.md, lido à parte. Baixado em 2026-11-13 pela API do GitHub (ou do servidor indicado). Estado do repositório pela API do GitHub em 2026-11-13: 2766 estrelas, criado em 2015-10-19, último push em 2026-06-16, 26 issues e PRs abertos, última release v1.14.0 2025-04-03T08:58:22Z, licença reconhecida pelo GitHub: NOASSERTION.

**Em uma frase:** a ferramenta lê um áudio de fala e devolve a sequência de formas de boca 2D (A a H e X), pela linha de comando, para animar personagem.

| Ponto | O que o texto diz |
|---|---|
| Comando | `rhubarb -o saida.txt gravacao.wav`, com saída em tsv, xml, json ou dat, e status em JSON |
| Reconhecedor | `pocketSphinx` para inglês; `phonetic` para outras línguas, em geral menos preciso |
| Ajuda pelo texto | `-d` passa o texto da fala para melhorar |
| Integrações | After Effects, Moho, OpenToonz, Spine, Vegas Pro, Visionaire |
| Binários | Windows, macOS e Linux |

**Lacuna:** não mede a qualidade em português nem o tempo de processamento.
