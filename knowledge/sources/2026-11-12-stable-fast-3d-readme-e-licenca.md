---
titulo: "SF3D: Stable Fast 3D Mesh Reconstruction with UV-unwrapping and Illumination Disentanglement"
tipo: artigo
autor: "Stability AI"   # README do repositório oficial; a citação do README dá Mark Boss, Zixuan Huang, Aaryaman Vasishta e Varun Jampani como autores do artigo científico
url: "https://github.com/Stability-AI/stable-fast-3d"
publicado_em: null   # o README não traz data; o artigo que ele cita é de 2024 (arXiv 2408.00653), e o LICENSE.md diz "Last Updated: July 5, 2024"
capturado_em: 2026-11-12
licenca: "protegido (README sem licença declarada no texto; o LICENSE.md do repositório é a Stability AI Community License, que cobre os modelos, o software e a documentação, e a página stability.ai/license traz '© Stability AI Ltd, 2026'); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [image-to-3d, open-weights, gated-model, gpu, licensing, commercial-use, revenue-threshold, model-outputs, ai-training-restriction, comfyui, interested-party]
---

# Stable Fast 3D: o que pede para rodar, o que sai, e a licença comunitária com teto de US$ 1 milhão

Nota de fato: tabelas do README do Stable Fast 3D (requisitos, opções, saída) e da licença que o cobre, na versão do repositório e na página da Stability AI, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: os três textos são protegidos.

**Proveniência.** Três fontes da Stability AI, baixadas em 2026-11-12 e lidas no texto bruto:

| Fonte | URL | O que foi lido | Data no texto | sha256 | Wayback |
|---|---|---|---|---|---|
| README (a principal) | https://github.com/Stability-AI/stable-fast-3d | o `README.md` inteiro, em markdown | nenhuma; cita o PyTorch 2.4.0 como o mais novo "as of writing" | (hash omitido) | `http://web.archive.org/web/20261012184255/https://github.com/Stability-AI/stable-fast-3d` |
| LICENSE.md | https://github.com/Stability-AI/stable-fast-3d/blob/main/LICENSE.md | o texto inteiro, seções I a V | "Last Updated: July 5, 2024" | (hash omitido) | sem captura |
| Página da licença | https://stability.ai/license | o HTML, no texto extraído e conferido no HTML: os dois planos e as 11 perguntas | nenhuma; rodapé "© Stability AI Ltd, 2026" | (hash omitido) | `http://web.archive.org/web/20261106055535/https://stability.ai/license` |

Títulos conferidos: o README abre com o título do campo `titulo`; o LICENSE.md, com "STABILITY AI COMMUNITY LICENSE AGREEMENT"; a página tem `<title>` "Stability AI License — Stability AI". A página da licença não traz o texto do contrato: é a escolha entre o plano Community e o Enterprise, com perguntas frequentes; o contrato está num link dela (`/community-license-agreement`) que não foi aberto, como não foram a página de registro (`/community-license`), a lista de modelos (`/core-models`), a política de uso aceitável, o model card no Hugging Face e o artigo no arXiv. O README não fala de licença em nenhum ponto. Quem fala: a Stability AI, que faz o modelo e vende a licença Enterprise.

**Conferência lado a lado** (2026-11-12, pela régua do `README.md` desta pasta, item 2). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra cada um dos três textos (README, LICENSE.md, página), com o mesmo cabeçalho nas três rodadas: 47 unidades medidas (19 de prosa, 28 de célula com texto), 0 coladas e 0 trechos de 3 ou mais. Na leitura lado a lado das mesmas 47 unidades, segue a fonte a que traduz uma frase inteira dela, junta duas ou funde três ou mais na ordem dela; o fragmento que só traz um fato e a frase que junta lugares distantes em outra ordem não contam. Resultado: 25 de 47 (24 das 28 células medidas, que trazem cada uma uma frase do README, do LICENSE.md ou da página, mais a terceira frase da recomendação; ficam fora a lista de qualificações da concessão, as duas células da tabela de divergências que descrevem a página em vez de traduzi-la, a frase de "Em uma frase", as duas primeiras da recomendação, a proveniência, a conferência e a lacuna). A maior sequência de unidades seguidas que seguem a fonte é de 14 (do "Powered by" na tabela da licença até a célula da pesquisa na tabela de divergências; na tabela de divergências, as células da página, lidas só entre si, andam para a frente em três seguidas (receita, pesquisa, saídas), alternadas com as do LICENSE.md, e é tabela de dados), mas a fonte anda para trás dentro dela; na ordem da fonte, a maior é de 2, sem trecho colado de 3 ou mais.

## Em uma frase

README e licença de quem faz e licencia o modelo: o Stable Fast 3D gera, de uma imagem, uma malha GLB com textura em cerca de 6 GB de VRAM, tem CUDA no Linux como referência e Mac e Windows como experimentais, e é coberto por uma licença comunitária gratuita até US$ 1 milhão de receita anual, com registro obrigatório para uso comercial e as saídas do lado de quem gera.

## O modelo, pelo README

| Ponto | Fato |
|---|---|
| Base | TripoSR |
| O que acrescenta ao TripoSR | malha sem artefatos; textura com UV desdobrado; cor sem iluminação embutida; parâmetros de material previstos |
| Para quê, pelo README | levar o asset a um jogo com facilidade |
| Velocidade | a do TripoSR, mantida |
| Acesso aos pesos | restrito no Hugging Face: login, pedido de acesso, token de leitura, `huggingface-cli login` |
| O que faz | malha 3D de uma imagem só, numa passada |
| Como o README o chama | modelo de código aberto, estado da arte |
| Artigo | arXiv 2408.00653 (2024) |

## Requisitos

| Ponto | Geral | Windows | Mac (MPS) |
|---|---|---|---|
| Situação | — | experimental | experimental |
| Sem garantia de igualdade com | — | o Linux, em desempenho e qualidade | o backend CUDA, em desempenho e qualidade |
| Python | 3.8 ou mais novo | — | — |
| GPU | CUDA ou MPS, opcional | — | — |
| PyTorch | conforme a plataforma, com a CUDA igual à do sistema | com PyTorch e CUDA adequados | o mais novo (2.4.0 quando o README foi escrito) ou o nightly |
| Ferramenta extra | setuptools 69.5.1 (`pip install -U setuptools==69.5.1`); `pip install wheel` | Visual Studio | runtime OpenMP, para o clang aceitar `-fopenmp` |
| Testado com | — | Visual Studio 2022 | M1 Max de 64 GB, PyTorch nightly |
| Variável de ambiente | — | — | `PYTORCH_ENABLE_MPS_FALLBACK=1` |
| Textura | — | — | kernels Metal próprios no baker |
| Memória | ~6 GB de VRAM por imagem, no padrão | não informada | MPS gasta mais que CUDA |
| Pouca memória | — | — | CPU, abaixo de 32 GB unificados |
| CPU | automática sem GPU; `SF3D_USE_CPU=1` força | — | — |
| Dependências | `requirements.txt`; mais `requirements-demo.txt` para o Gradio | — | — |

## Linha de comando e saída

| Opção | Fato |
|---|---|
| Comando | `python run.py <imagem> --output-dir output/` |
| Várias imagens | caminhos separados por espaço |
| Saída | o modelo 3D em GLB, na pasta de saída |
| `--texture-resolution` | resolução da textura, em pixels |
| `--remesh_option` | None, Triangle ou Quad |
| Remesh `none` | malha como saiu, sem custo de CPU |
| Remesh `quad` | quads com fluxo, partidos em triângulos na exportação GLB (Instant Meshes, Jakob et al.); com custo de CPU |
| Remesh `triangle` | vértices e arestas refeitos em triângulos (Botsch e Kobbelt); com custo de CPU |
| Número-alvo de vértices | aproximado, não é limite; ignorado com `none` |
| Nome da opção do número de vértices | o README não dá |
| Ajuda | `python run.py --help` |
| App local | `python gradio_app.py` |
| ComfyUI | nós próprios e um workflow de exemplo; clonar em `custom_nodes`, instalar o `requirements.txt` e reiniciar |

## O que a licença permite, exige e proíbe (LICENSE.md, versão de 5 de julho de 2024)

| Tema | Ponto | Fato | Onde |
|---|---|---|---|
| Uso comercial | Permitido? | sim, grátis, com registro e abaixo do teto | §III |
| Uso comercial | "Commercial Purpose" | finalidade voltada sobretudo a vantagem comercial ou pagamento | §III |
| Uso comercial | Exemplos dados | o próprio produto ou serviço, inclusive hospedado ou por API; a operação interna da empresa | §III |
| Uso não comercial | Permitido? | sim, grátis | §II |
| Uso não comercial | "Research Purpose" | avanço acadêmico ou científico | §II |
| Uso não comercial | "Non-Commercial Purpose" | nem pesquisa nem voltado a lucro | §II |
| Uso não comercial | Exemplos dados | uso pessoal de hobby; avaliação e teste | §II |
| Uso não comercial | Registro | não pedido; o registro só aparece na §III | §II, §III |
| As duas licenças | Tipo de concessão | não exclusiva, mundial, intransferível, sem sublicença, revogável, sem royalties | §II, §III |
| As duas licenças | Direitos | usar, reproduzir, distribuir, criar derivadas, modificar | §II, §III |
| Atribuição | Cópia da licença | a quem recebe | §IV(a) |
| Atribuição | Arquivo "Notice" | com o aviso de copyright dado na licença | §IV(a) |
| Atribuição | "Powered by Stability AI" | em destaque, num site, interface, post, página "sobre" ou documentação | §IV(a) |
| Atribuição | Marca | nenhuma licença além do "Powered by" | §IV(c)(i) |
| Modificação | Derivative Work | inclui fine-tune e LoRA | §V |
| Modificação | Dono da derivada | quem a cria, perante a Stability | §IV(c)(ii) |
| Modificação | "Notice" da derivada | avisos próprios separados dos da Stability, com o que mudou e como | §IV(a) |
| Redistribuição | Gatilho das exigências | distribuir os materiais, uma derivada ou produto que use parte deles | §IV(a) |
| Redistribuição | Quem recebe dentro de produto final | fora da §III | §III |
| Saídas | Dono | o licenciado, perante a Stability, até onde a lei permite | §IV(c)(iii) |
| Saídas | Saída é Derivative Work? | não | §V |
| Saídas | Limites de uso | lei, controle de comércio, documentação e política de uso aceitável | §IV(b) |
| Saídas | Garantia | nenhuma ("AS IS") | §IV(d) |
| Território | — | mundial | §II, §III |
| Teto de receita | Valor | US$ 1.000.000 por ano, ou o equivalente em moeda local | §III; introdução |
| Teto de receita | De quem | do licenciado ou das afiliadas, sozinhos ou somados | §III |
| Teto de receita | Que receita | toda, tenha ou não vindo dos materiais | §III |
| Teto de receita | Afiliada | controle direto ou indireto, ou controle comum, acima de 50% dos votos | §V |
| Teto de receita | Ao passar | fim das licenças na data | §III |
| Teto de receita | Depois | pedir licença em stability.ai/enterprise, a critério da Stability | §III |
| Registro | Quando | uso ou distribuição para fim comercial | §III |
| Registro | Onde | stability.ai/community-license | §III |
| IA | Veto | criar ou melhorar modelo gerativo fundacional | §IV(b) |
| IA | Com o quê | materiais, derivadas e saídas | §IV(b) |
| IA | Exceção | os próprios modelos e as derivadas | §IV(b) |
| Outros | O que a licença cobre | modelos, software e documentação da Stability | §V |
| Outros | Que modelos | os da página Core Models, que pode mudar | §V |
| Outros | Processo de PI contra a Stability | fim das licenças na data | §IV(c)(iv) |
| Outros | Feedback | licença perpétua e irrevogável à Stability | §IV(c)(v) |
| Outros | Responsabilidade da Stability | nenhuma por dano | §IV(e) |
| Outros | Término | por violação; apagar e parar de usar | §IV(f) |
| Outros | Lei | Estados Unidos e Califórnia | §IV(g) |

## A página stability.ai/license

| Ponto | Fato |
|---|---|
| Plano Enterprise, para quem | empresas, provedores de API e negócios com mais de US$ 1M de receita anual |
| Plano Enterprise, o que inclui | uso comercial; suporte de implementação |
| Plano Enterprise, extras | treino de modelo sob medida; consultoria |
| Plano Enterprise, preço | sob consulta |
| Plano Community, para quem | pesquisadores, desenvolvedores, pequenas empresas e criadores com menos de US$ 1M de receita anual |
| Plano Community, o que inclui | Stable Audio 3.0; Stable Diffusion 3.5 Suite; SDXL Turbo; Stable Fast 3D; link para a lista completa |
| Plano Community, preço | grátis |
| Criador individual em casa | não paga |
| Fine-tuner que vende o modelo | não paga abaixo de US$ 1M |
| LoRA treinada com saída de outra LoRA | permitido |
| Modelo fundacional, pela página | arquitetura "nova" derivada de um Core Model; LoRA, hypernetwork, fine-tune, retreino e retreino do zero não são |
| Ao chegar a US$ 1M | contatar a Stability para comprar a Enterprise |
| Revogação | quando os termos são violados |

## Onde o LICENSE.md e a página dizem diferente

| Ponto | LICENSE.md (5/7/2024) | Página stability.ai/license |
|---|---|---|
| Receita que conta | a do licenciado e das afiliadas, sozinhos ou somados, direta ou indiretamente dos materiais ou não | a da pessoa ou organização, qualquer que seja a fonte; afiliadas não aparecem |
| Pesquisa acima do teto | a frase do teto, na §III, encerra qualquer licença dada pela Agreement, sem ressalva escrita para pesquisa | uso só de pesquisa fica na Community e não paga, qualquer que seja a receita |
| Registro | para todo uso comercial | aparece só na resposta ao pesquisador cuja pesquisa vira produto ou serviço |
| Saídas | do licenciado, no limite da lei | do licenciado, para usar à vontade, dentro da lei e da política de uso aceitável |
| Restrição de IA | modelo gerativo fundacional, sem definir o termo | define fundacional como arquitetura nova e lista o que não é |
| Acima do teto | as licenças acabam na data; a Stability concede outra se quiser | contatar para comprar; recusar cliente novo não combina com o objetivo da empresa |

## O que a fonte recomenda

A referência do README é Linux com CUDA, cerca de 6 GB de VRAM e o PyTorch casado com a versão de CUDA do sistema; Mac e Windows funcionam sem garantia de igualdade, e no Mac com pouca memória o README manda para a CPU. Antes do primeiro uso, é preciso pedir acesso aos pesos no Hugging Face, e antes do primeiro uso comercial, registrar na Stability, conferindo a receita do grupo inteiro contra o teto de US$ 1 milhão.

## Citações

- "regardless of whether that revenue is generated directly or indirectly from the Stability AI Materials or Derivative Works" (LICENSE.md, §III)
- "You own any outputs generated from the Models or Derivative Works to the extent permitted by applicable law." (LICENSE.md, §IV(c)(iii))
- "this falls within the Community License and you don’t need to pay, regardless of the amount of revenue generated by your organization" (página, pergunta do pesquisador)

## Lacuna

O README não diz a licença, o tempo de geração, a resolução de textura padrão nem o nome da opção do número de vértices, e não dá VRAM para Windows nem para a CPU. O LICENSE.md não define modelo gerativo fundacional. A página não traz o texto do contrato, só o link para ele, que não foi lido, e não tem data; daqui não se sabe se o contrato em vigor é ainda o de 5 de julho de 2024 do repositório. Nenhum dos três diz o que acontece com saídas geradas antes de a receita passar do teto.
