---
titulo: "Blender Manual: Rendering From The Command Line, Rendering Animations e glTF 2.0"
tipo: artigo
autor: "Blender Documentation Team (manual do Blender)"
url: "https://docs.blender.org/manual/en/latest/advanced/command_line/render.html"
publicado_em: 2026-11-12   # rodapé das três páginas: "Last updated on 2026-11-12"; duas são do manual 5.3 (latest), a do glTF é do 5.4 (dev)
capturado_em: 2026-11-12
licenca: "CC BY-SA 4.0 (rodapé de cada página: 'This page is licensed under a CC-BY-SA 4.0 Int. License'); o integral está na url"
areas: [generative-media]
tags: [blender, headless-rendering, command-line, image-sequence, video-encoding, gltf, glb, camera-animation, video-as-code]
---

# Blender: render sem tela, animação em sequência de imagens e exportação glTF

Ficha, organizada pelo que cada página responde; o texto integral não vem neste repositório e se lê na url do frontmatter.

**Proveniência.** Três páginas do manual do Blender, baixadas com curl em 2026-11-12, com o texto extraído do HTML: "Rendering From The Command Line", https://docs.blender.org/manual/en/latest/advanced/command_line/render.html (manual 5.3, sha256 do HTML (hash omitido)); "Rendering Animations", https://docs.blender.org/manual/en/latest/render/output/animation.html (manual 5.3, (hash omitido)); e "glTF 2.0", https://docs.blender.org/manual/nb/dev/addons/scene_gltf2.html (manual 5.4, versão de desenvolvimento, na interface em norueguês, com o texto em inglês e os avisos com rótulos em norueguês, como "Merknad" e "Advarsel"; (hash omitido)). Lidas inteiras. Os HTML estão em a pasta da rodada.

## Render pela linha de comando

| Pergunta | O que a página diz |
|---|---|
| Por que usar | renderizar mais rápido, acessar o Blender de longe ou montar scripts; não precisa de tela (no Linux, nem de servidor X), então roda por shell remoto, como SSH |
| Ordem dos argumentos | eles rodam na ordem dada: saída e extensão vêm antes da ordem de renderizar, e `-f` ou `-a` vão sempre por último |
| Caixa | `-F` e `-f` são argumentos diferentes |
| Um quadro | `blender -b file.blend -f 10` (`-b` é segundo plano, sem interface; `-f -2` é o penúltimo quadro) |
| Saída de um quadro | `-o /project/renders/frame_#####` (cinco dígitos para o número do quadro) e `-F OPEN_EXR` (troca o formato salvo no `.blend`) |
| Animação inteira | `blender -b file.blend -a`, com as configurações salvas no arquivo |
| Motor, intervalo e threads | `-E CYCLES -s 10 -e 500 -t 2 -a`; a lista de motores sai de `blender -E help` |
| O resto | a lista completa de argumentos e as opções próprias do Cycles ficam em outras páginas do manual (não lidas) |

## Animação: direto em vídeo ou em sequência de imagens

- **O padrão:** a animação vai para o disco quadro a quadro, conforme o painel Output, se a opção de salvar a saída estiver ligada; desligada, só um nó File Output do Compositor grava, e sem saída válida o render dá erro.
- **A conta antes de escolher:** renderizar um quadro típico na resolução final e multiplicar pelo número de quadros. O exemplo da página: um minuto a 24 fps são 1.440 quadros; a 30 s por quadro, 720 minutos (12 horas).
- **Direto num arquivo de vídeo (AVI ou MOV):** a página o chama de "highly not recommended" e fora da prática padrão; só cabe em trecho curto, com menos de uma hora de render no total, energia estável e a máquina livre.
- **Sequência de imagens (JPG, PNG ou multicamada):** o caminho estável, um arquivo por quadro, depois montado no Video Sequencer com áudio e codificado (por exemplo, H.264). Indicado com render acima de uma hora, pós-produção (cor, recorte de fundo, composição), vários formatos de saída, tempo preciso (sincronia labial) e quando se quer parar e retomar. O Video Sequencer não aceita EXR multicamada; aí a montagem passa por um nó Image Input no Compositor.
- **Retomar:** com os quadros num formato sem perda (PNG), desligar Overwrite recomeça de onde parou depois de uma queda.
- **Prévia:** Frame Step renderiza um quadro a cada N; depois, com Overwrite desligado e Frame Step em 1, completa os que faltam.

## Exportar para glTF 2.0

- **O formato:** feito para transmitir e carregar modelos 3D na web e em aplicativos; o complemento vem ligado por padrão. Exporta e importa malhas, materiais (Principled BSDF e sem sombreamento), texturas, **câmeras**, luzes pontuais, extensões, propriedades próprias (extras) e animação por chaves, *shape keys* e esqueleto; Gaussian Splatting só na importação.
- **Malhas:** quadriláteros e n-gonos viram triângulos; curvas e o que não é malha precisam virar malha antes; instâncias podem ir pela extensão `EXT_mesh_gpu_instancing`, com limites (só malhas, sem filhos, todas filhas do mesmo objeto).
- **O que a animação leva:** transformação de objeto (posição, rotação, escala), ossos e valores de *shape key*; animação de física, luz ou material fica de fora. Quatro modos de exportar (ações, ações ativas juntas, trilhas NLA, cena), e uma ação só vai se estiver ativa ou guardada numa trilha NLA.
- **Animation Pointer:** exporta como animação algumas propriedades de material, luz ou **câmera**; a página chama o recurso de experimental e diz que nem todas as propriedades são aceitas ainda.
- **Três formas de arquivo:** `.glb` binário único; `.gltf` com `.bin` e texturas à parte; `.gltf` embutido em Base64, o menos eficiente, só quando ligado nas preferências.

## Citações

- "Arguments are executed in the order they are given!"
- "The Direct Approach, which is highly not recommended and not a standard practice"
- "Animation Pointer is a way to export some properties of a material, or a light, or a camera, as an animation." O manual marca o recurso como experimental.

## Lacuna

As páginas não falam de Grease Pencil, Line Art nem do EEVEE em segundo plano, nem de diferença entre sistemas (Windows, Linux) no render sem tela; não dão tempo de render por motor. A do glTF não diz quais propriedades da câmera o Animation Pointer leva nem como a câmera exportada se comporta em outro programa.
