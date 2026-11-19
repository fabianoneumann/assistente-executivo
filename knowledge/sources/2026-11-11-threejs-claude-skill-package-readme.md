---
titulo: "Three.js Claude Skill Package (README) e a skill threejs-impl-animation"
tipo: artigo
autor: "OpenAEC Foundation (repositório Impertio-Studio/Three.js-Claude-Skill-Package)"
url: "https://github.com/Impertio-Studio/Three.js-Claude-Skill-Package"
publicado_em: 2026-03-20   # último commit do README.md; o último commit do ramo master (e da skill de animação) é de 2026-03-30
capturado_em: 2026-11-11
licenca: "MIT (arquivo LICENSE do repositório, 'Copyright (c) 2026 OpenAEC Foundation'; a SKILL.md de animação declara 'license: MIT' no cabeçalho)"
areas: [generative-media]
tags: [threejs, claude-code-skills, react-three-fiber, webgpu, animation, open-source]
---

# Three.js Claude Skill Package: 24 skills de Three.js, e a de animação

Ficha de estudo em palavras próprias; o README integral (licença MIT) não vem neste repositório e se lê na url do frontmatter. Da skill de animação, só as regras citadas na ficha.

**Proveniência.** Dois arquivos lidos com `gh api` (conteúdo bruto) em 2026-11-11, no commit (hash omitido) (o topo do ramo `master`, de 2026-03-30): `README.md` (último commit em 2026-03-20) e `skills/source/threejs-impl/threejs-impl-animation/SKILL.md` (último commit em 2026-03-30). Na data, o repositório tinha 29 estrelas e o último push registrado era de 2026-07-08. O README manda clonar de `OpenAEC-Foundation/Three.js-Claude-Skill-Package`; pela API do GitHub, esse nome e `Impertio-Studio/Three.js-Claude-Skill-Package` levam ao mesmo repositório (mesmo id, mesmas estrelas, mesmo README). A árvore do commit tem 24 arquivos `SKILL.md`, 11 deles em `skills/source/threejs-impl/`. Não há ficha de setembro desta fonte.

## O que é

Um pacote de 24 skills para o Claude Code escrever código de Three.js r160 ou mais novo, React Three Fiber, Drei, WebGPU e motores de física. O README chama as skills de "deterministic" no sentido da linguagem: cada uma usa ALWAYS e NEVER, sem palavras de hesitação, para a geração de código sair consistente. Instala-se clonando o repositório ou pondo-o como submódulo git em `.claude/skills/threejs`, e depois apontando a pasta de skills na configuração do Claude Code.

## As skills

- **Núcleo (4):** grafo de cena (hierarquia de `Object3D`, percurso, camadas, neblina, conversão de coordenadas); renderizador (`WebGLRenderer`, tone mapping, gestão de cor, render targets); matemática (vetores, matrizes, quatérnios, ângulos de Euler, cor); raycaster (clique e hover com o mouse, inclusive em `InstancedMesh`).
- **Sintaxe (5):** geometrias (`BufferGeometry`, 21 geometrias prontas, `InstancedMesh`); materiais (15 ou mais tipos, PBR, texturas, regras de espaço de cor); shaders (`ShaderMaterial`, GLSL, uniforms, `ShaderChunk`, `onBeforeCompile`); loaders (GLTF, Draco, KTX2, textura); controles (órbita, mapa, voo, transformação).
- **Implementação:** a tabela diz 10 e lista 11 nomes: luz (7 tipos de luz, IBL, `PMREMGenerator`, mapas de ambiente HDR), sombras (mapas de sombra, ajuste de bias, diagnóstico de artefatos), animação (`AnimationMixer`, crossfade, animação de esqueleto vinda do GLTF), pós-processamento (`EffectComposer`, pmndrs/postprocessing, bloom, SSAO), física (cannon-es e Rapier, com padrões de sincronização), React Three Fiber (Canvas, hooks, JSX, eventos), Drei (mais de 150 componentes auxiliares), WebGPU (`WebGPURenderer`, TSL, materiais de nós, compute shaders), visualizador IFC/BIM (web-ifc e @thatopen/components), áudio espacial 3D e WebXR (VR e AR, controles, rastreamento de mãos, hit testing). Só com 11 a conta fecha nos 24 (4 + 5 + 11 + 2 + 2), e a árvore do commit tem 11; a estrutura de pastas do README também diz "(10 skills)" para `threejs-impl/`.
- **Erros (2):** desempenho (vazamentos de memória, padrões de `dispose`, otimização de draw calls) e renderização (tela preta, cores erradas, z-fighting, artefatos de sombra).
- **Agentes (2):** montador de cena (árvores de decisão para compor uma cena inteira) e otimizador de modelo (pipeline de GLTF com Draco, KTX2 e LOD).

## Como o pacote diz que foi feito

- **Requisitos de qualidade:** menos de 500 linhas por `SKILL.md` (média de 338); só ALWAYS e NEVER; só inglês ("Claude reads English, responds in any language"); cada skill com `methods.md`, `examples.md` e `anti-patterns.md`; imports em módulo ES; versões explícitas (Three.js r160+, React Three Fiber 8.x); cada skill funciona sozinha.
- **Método:** o README fala num método "7-phase research-first" e numera seis fases: plano bruto do panorama, pesquisa (27.627 palavras em 7 documentos), refinamento do plano de 19 para 24 skills pelo princípio da skill atômica, criação em 8 lotes paralelos de 3 skills, validação (24 de 24 passaram em todos os portões) e publicação.
- **Pacotes irmãos do mesmo autor:** ERPNext (28 skills), Blender-Bonsai (73), Tauri 2 (27) e um pacote de integração entre tecnologias de AEC (15), com três skills que ligam IFC, BIM e Three.js.

## A skill de animação (`threejs-impl-animation`)

- **A arquitetura que ela ensina:** `AnimationClip` (os dados, trilhas de keyframes) → `AnimationAction` (o controle de reprodução: tocar, pausar, fade, crossfade) → `AnimationMixer` (o agendador, um por objeto raiz animado) → `Clock` (dá o delta de tempo para o mixer).
- **As regras de tempo:** chamar `mixer.update(delta)` a cada quadro, dentro do laço de render ("animations will NOT play without it"); nunca calcular o delta à mão com `new Date()` ou `performance.now()`, sempre usar `THREE.Clock` ou `renderer.setAnimationLoop`, "which provides stable frame timing". O exemplo mínimo lê `clock.getDelta()` a cada volta de `renderer.setAnimationLoop(animate)`.
- **As outras regras:** um só `AnimationMixer` por objeto raiz animado; nunca criar `AnimationAction` direto, sempre `mixer.clipAction(clip)`; guardar a ação numa variável em vez de chamar `clipAction` no laço; chamar `.play()` uma vez só; `.reset()` antes de `.play()` ao recomeçar uma ação parada ou terminada; `clampWhenFinished = true` com `LoopOnce`, senão a ação volta ao primeiro quadro ao terminar; `.reset()` na ação que entra antes de um crossfade.
- **`.setTime(seconds)`:** aparece só na tabela de métodos do mixer ("Sets global time, updates all actions"), ao lado da propriedade `.time` (tempo global do mixer, em segundos); nenhuma regra nem exemplo da skill o usa.
- **O que a fonte não trata:** nem o README nem a skill de animação falam de vídeo, de render quadro a quadro para arquivo, de levar a cena a um instante dado nem de tempo determinístico; a descrição da skill cita "tween" e "GSAP" entre as palavras-chave, mas o corpo não trata deles.
