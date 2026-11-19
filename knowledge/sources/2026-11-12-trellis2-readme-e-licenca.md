---
titulo: "TRELLIS.2: Native and Compact Structured Latents for 3D Generation (README do Hugging Face, README e LICENSE do GitHub)"
tipo: artigo
autor: "Microsoft (Jianfeng Xiang e outros)"
url: "https://huggingface.co/microsoft/TRELLIS.2-4B/blob/main/README.md"
publicado_em: null   # os arquivos não trazem data; o artigo citado é de 2025 (arXiv 2512.14692)
capturado_em: 2026-11-12
licenca: "MIT (campo 'license: mit' do cartão do modelo e LICENSE do repositório microsoft/TRELLIS.2, 'Copyright (c) Microsoft Corporation.'); o integral dos três arquivos está na url"
areas: [generative-media]
tags: [image-to-3d, 3d-generation, trellis, mesh, pbr, glb, vram, linux, license]
---

# TRELLIS.2: imagem para modelo 3D com material PBR, e o que ele exige da máquina

Ficha em palavras próprias; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Três arquivos baixados em 2026-11-12: o README do cartão do modelo no Hugging Face, https://huggingface.co/microsoft/TRELLIS.2-4B/blob/main/README.md (sha256 (hash omitido)); o README do repositório, https://github.com/microsoft/TRELLIS.2 ((hash omitido)); e o LICENSE do repositório, https://github.com/microsoft/TRELLIS.2/blob/main/LICENSE ((hash omitido)). Lidos inteiros. As licenças das dependências da NVIDIA que o README nomeia (nvdiffrast e nvdiffrec) não fazem parte desta ficha: só o link delas está no README.

## O modelo

| Ponto | Valor, pelos READMEs |
|---|---|
| Nome | TRELLIS.2-4B |
| Entrada | uma imagem |
| Saída | modelo 3D, malha com materiais PBR (cor base, rugosidade, metálico, opacidade), exportado em GLB |
| Tamanho | 4 bilhões de parâmetros, transformer de *flow matching* com VAE 3D esparso |
| Representação | O-Voxel, voxel esparso "sem campo", que aceita superfície aberta, geometria não variedade e estrutura interna fechada |
| Resolução | de 512³ a 1536³ |
| Tempo numa H100 | ~3 s a 512³ (2 + 1, forma e material), ~17 s a 1024³ (10 + 7), ~60 s a 1536³ (35 + 25) |
| Conversões | malha texturizada para O-Voxel em menos de 10 s numa CPU; O-Voxel para malha em menos de 100 ms em CUDA |
| Também gera | textura PBR para uma malha dada, a partir de imagem de referência |
| Código de treino | publicado |

## O que exige

| Requisito | Valor |
|---|---|
| Sistema | testado só no Linux |
| GPU | NVIDIA com pelo menos 24 GB de memória; verificado em A100 e H100 |
| CUDA Toolkit | para compilar pacotes; recomendado 12.4 |
| Ambiente | Conda recomendado; Python 3.8 ou mais; PyTorch 2.6.0 com CUDA 12.4 no ambiente padrão |
| Atenção | `flash-attn` por padrão; em GPU sem suporte (V100, por exemplo), `xformers` com `ATTN_BACKEND` |
| Saída GLB | em modo `OPAQUE` por padrão: o alfa fica na textura, e ligar a transparência é manual no programa 3D |

## Licença

- O modelo e o código saem sob a licença MIT (Microsoft), cujo texto vem embaixo.
- O README do GitHub avisa que algumas dependências têm termos próprios: o nvdiffrast, usado para renderizar os modelos gerados, e o nvdiffrec, que implementa o renderizador *split-sum* dos materiais PBR, cada um com a sua licença, só por link.

## Limites declarados

- A malha crua pode ter furos pequenos ou descontinuidades de topologia; para geometria fechada (impressão 3D, por exemplo), há scripts de pós-processamento, como preenchimento de furos.
- É um modelo de base, sem alinhamento a preferência humana nem ajuste de estética: a saída segue a distribuição dos dados de treino e varia de estilo.

## Citações

- "An NVIDIA GPU with at least 24GB of memory is necessary."
- "Please note that certain dependencies operate under separate license terms"

## Lacuna

Os arquivos não dizem se a limitação de licença das dependências passa para o modelo gerado, não dão tempo nem memória fora da H100, nem dizem se roda no Windows.
