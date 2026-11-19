---
titulo: "Depth Anything V2 (README do repositório)"
tipo: artigo
autor: "Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiaogang Xu, Jiashi Feng e Hengshuang Zhao (HKU e TikTok), DepthAnything/Depth-Anything-V2"
url: "https://github.com/DepthAnything/Depth-Anything-V2"
publicado_em: 2024-06-14   # artigo, código e modelos lançados, pela seção "News" do README
capturado_em: 2026-11-11
licenca: "Apache 2.0 (arquivo LICENSE do repositório); o README diz que o modelo Small é Apache 2.0 e que os modelos Base, Large e Giant são CC BY-NC 4.0 (não comercial). Texto do README guardado sob a Apache 2.0 do repositório: http://www.apache.org/licenses/LICENSE-2.0"
areas: [generative-media]
tags: [depth-estimation, monocular-depth, open-weights, licensing, parallax, gpu]
---

# Depth Anything V2: mapa de profundidade de uma imagem

Ficha de estudo em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** `README.md` do repositório https://github.com/DepthAnything/Depth-Anything-V2, baixado em 2026-11-11, lido inteiro. O artigo (arXiv 2406.09414), a página do projeto e as pastas `metric_depth` e `DA-2K.md` não foram lidos.

## O que o modelo faz

Estima a profundidade relativa de cada pixel de uma imagem (o resultado é um mapa altura por largura, em `numpy`), e há versões ajustadas para profundidade métrica. O README diz que o V2 supera muito o V1 em detalhe fino e robustez e que, comparado aos modelos baseados no Stable Diffusion, é mais rápido, tem menos parâmetros e acerta mais a profundidade. Sai um mapa, não camadas separadas da imagem.

## Os quatro modelos e a licença de cada um

| Modelo | Parâmetros | Licença (seção LICENSE do README) |
|---|---|---|
| Depth-Anything-V2-Small | 24,8 M | Apache 2.0 |
| Depth-Anything-V2-Base | 97,5 M | CC BY-NC 4.0 |
| Depth-Anything-V2-Large | 335,3 M | CC BY-NC 4.0 |
| Depth-Anything-V2-Giant | 1,3 B ("Coming soon") | CC BY-NC 4.0 |

## Como se usa

- **Pelo repositório:** clonar, instalar os requisitos, baixar o checkpoint para `checkpoints/` e chamar `model.infer_image(img)`; o código escolhe `cuda`, `mps` ou CPU, o que houver. O script `run.py` processa uma imagem, uma pasta ou uma lista, com tamanho de entrada padrão 518 ("you can increase the size for even more fine-grained results"), e pode salvar só o mapa (`--pred-only`) e em cinza (`--grayscale`); o `run_video.py` faz o mesmo em vídeo, e o README diz que o modelo maior tem melhor consistência no tempo.
- **Pelo Transformers:** `pipeline(task="depth-estimation", model="depth-anything/Depth-Anything-V2-Small-hf")`. O README avisa que as previsões podem diferir um pouco das do repositório, porque o OpenCV (usado por eles) e o Pillow (usado pelo Hugging Face) ampliam a imagem de modo diferente, e recomenda o caminho do repositório.
- **Outros:** demo Gradio local e online; versões da comunidade para Core ML, TensorRT, ONNX, ComfyUI, Android e Transformers.js (profundidade em tempo real no navegador, por WebGPU). Projetos irmãos citados nas notícias: Video Depth Anything (2025-01-22, mapas consistentes para vídeos de mais de 5 minutos) e Prompt Depth Anything (2024-12-22, profundidade métrica em 4K com LiDAR de baixa resolução).

## O que o README não diz

Não dá memória de GPU, tempo por imagem nem resultado em desenho de traço ou ilustração.
