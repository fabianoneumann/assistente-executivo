---
titulo: "TripoSR (README do repositório)"
tipo: artigo
autor: "Tripo AI e Stability AI (VAST-AI-Research/TripoSR)"
url: "https://github.com/VAST-AI-Research/TripoSR"
publicado_em: null   # o README não traz data; o relatório técnico citado é de 2024 (arXiv 2403.02151)
capturado_em: 2026-11-12
licenca: "MIT (LICENSE do repositório VAST-AI-Research/TripoSR, confirmado pela API do GitHub, e o próprio README: 'The model is released under the MIT license'); o integral está na url"
areas: [generative-media]
tags: [image-to-3d, 3d-reconstruction, triposr, mesh, vram, cuda, license]
---

# TripoSR: um modelo 3D a partir de uma imagem, rápido, em MIT

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** README do repositório VAST-AI-Research/TripoSR, https://github.com/VAST-AI-Research/TripoSR, baixado em 2026-11-12. Lido inteiro. O relatório técnico (arXiv 2403.02151) não foi lido.

| Ponto | Valor, pelo README |
|---|---|
| O que faz | reconstrução 3D a partir de uma imagem só, num passe direto (*feedforward*) |
| Quem fez | Tripo AI e Stability AI |
| Base | os princípios do Large Reconstruction Model (LRM) |
| Velocidade | menos de 0,5 s por modelo numa NVIDIA A100 |
| Licença | MIT, cobrindo o código, os modelos pré-treinados e a demonstração online |
| Requisitos | Python 3.8 ou mais; CUDA se houver; PyTorch com a versão maior do CUDA igual à do CUDA instalado |
| Uso | `python run.py examples/chair.png --output-dir output/`; aceita várias imagens; há um app Gradio (`python gradio_app.py`) |
| Memória | cerca de 6 GB de VRAM por imagem, nas opções padrão |
| Textura | `--bake-texture` troca cor por vértice por textura; `--texture-resolution` dá a resolução da textura em pixels |
| Problema conhecido | o `torchmcubes` compilado sem CUDA ("torchmcubes was not compiled with CUDA support"); a solução é casar a versão do CUDA com a do PyTorch, ter `setuptools` 49.6.0 ou mais e reinstalar o `torchmcubes` a partir do GitHub |

## Citações

- "The default options takes about **6GB VRAM** for a single image input."

## Lacuna

O README não fala do Windows, do formato do arquivo de saída, de quanto tempo leva fora da A100 nem de como o modelo se sai com desenho (ele mostra comparações de qualidade em figuras, sem os números no texto).
