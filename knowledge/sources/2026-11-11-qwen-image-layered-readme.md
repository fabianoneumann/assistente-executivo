---
titulo: "Qwen-Image-Layered (README do repositório)"
tipo: artigo
autor: "Qwen (Alibaba), QwenLM/Qwen-Image-Layered"
url: "https://github.com/QwenLM/Qwen-Image-Layered"
publicado_em: 2025-12-19   # lançamento do modelo e dos pesos, pela seção "News" do README
capturado_em: 2026-11-11
licenca: "Apache 2.0 (seção 'License Agreement' do README e arquivo LICENSE do repositório). Texto da licença: http://www.apache.org/licenses/LICENSE-2.0"
areas: [generative-media, content-design]
tags: [image-layer-decomposition, rgba-layers, diffusion, open-weights, image-editing, gpu]
---

# Qwen-Image-Layered: separar uma imagem em camadas RGBA

Ficha de estudo em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** `README.md` do repositório https://github.com/QwenLM/Qwen-Image-Layered, baixado em 2026-11-11, lido inteiro. O artigo (arXiv 2512.15603), o blog e o cartão do modelo no Hugging Face não foram lidos para esta ficha.

## O que o modelo faz

Recebe uma imagem e a decompõe em várias camadas RGBA (com transparência), cada uma editável sem mexer no resto. O README apresenta isso como "inherent editability": separar fisicamente os componentes em camadas permite mudar a cor de uma, trocar o conteúdo de outra (no exemplo, uma moça por um rapaz, e o texto por "Qwen-Image", com a camada editada pelo Qwen-Image-Edit), apagar um objeto, redimensioná-lo sem distorção e movê-lo pela tela. O número de camadas é variável (os exemplos mostram 3 e 8), e a decomposição é recursiva: qualquer camada pode ser decomposta de novo.

## Como se usa

- **Requisitos e chamada:** `transformers` 4.51.3 ou mais (por causa do Qwen2.5-VL), a versão mais nova do `diffusers` pelo GitHub, `python-pptx` e `psd-tools`. O exemplo carrega o `QwenImageLayeredPipeline` e o põe em `cuda` com `torch.bfloat16`; os parâmetros do exemplo são 4 camadas, 50 passos de inferência, `true_cfg_scale` 4,0, semente 777 e `resolution` 640, com o comentário de que há dois baldes de resolução (640 e 1024) e que "for this version, 640 is recommended". Cada camada sai como um PNG.
- **O prompt de texto** descreve o conteúdo geral da imagem de entrada, inclusive o que está parcialmente escondido (o texto atrás de um objeto do primeiro plano), e não serve para escolher o conteúdo de cada camada. Os pesos foram ajustados para a tarefa de imagem para camadas; gerar camadas só a partir de texto é suportado, mas "its performance on text-to-multi-RGBA generation is limited".
- **Ferramentas do repositório:** uma interface Gradio (`src/app.py`) que decompõe e exporta as camadas em PPTX, ZIP e PSD; outra para editar imagem com transparência pelo Qwen-Image-Edit (`src/tool/edit_rgba_image.py`); e um script que junta as camadas de novo (`src/tool/combine_layers.py`), carregadas de baixo para cima. O vLLM-Omni também roda o modelo.

## O que o README não diz

Não dá a memória de GPU necessária, o número de parâmetros, o tempo por imagem nem a resolução máxima além dos dois baldes; não fala de desenho de traço ou de ilustração em particular.
