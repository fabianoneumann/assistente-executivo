---
titulo: "One-take Creation, Flexible Referencing: Introducing Seedance 2.5"
tipo: artigo
autor: "ByteDance Seed (blog oficial da equipe)"
url: "https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5"
publicado_em: 2026-07-31
capturado_em: 2026-11-11
licenca: "protegida: sem licença aberta; o rodapé da página traz 'Copyright© 2026 Bytedance Seed'; ficha em palavras próprias, sem o integral"
areas: [generative-media]
tags: [seedance, bytedance, video-generation, model-launch, video-editing, video-extension, reference-images, clay-render]
---

# Seedance 2.5: o anúncio de lançamento da ByteDance Seed (31/07/2026)

Ficha de estudo do post de lançamento do Seedance 2.5 no blog da equipe Seed. Fonte curta (um post de blog): organizada pelo que serve a quem avalia o modelo (o que foi anunciado e onde, os números, os controles, os limites admitidos, o que falta), e não pela ordem do post.

**Proveniência.** HTML da página baixado com curl em 11/11/2026, e lido no texto extraído dele. A data, 2026-07-31, está no próprio post (campo "Date", categoria "Visual"). Os vídeos de demonstração não foram vistos (o texto extraído só traz o aviso de que o navegador não toca o vídeo, seguido do prompt de cada um). **Cobertura:** o post inteiro, da abertura ao "Summary and looking forward", com os prompts de todos os exemplos; o menu e o rodapé do site, só para a licença.

**Quem fala.** A própria equipe que fez o modelo, num texto de lançamento: as qualidades descritas são as que o fabricante declara, sem medida publicada no post.

## O que foi anunciado, quando e onde

- O Seedance 2.5 saiu em 31/07/2026, descrito como o novo modelo de criação de vídeo da casa. Ele parte da arquitetura do Seedance 2.0, que o post chama de geração conjunta de áudio e vídeo num modelo multimodal unificado.
- No dia do anúncio, o modelo entrava no Jimeng AI, no Doubao Pro e em outras plataformas (em ambos pelo menu de geração de vídeo, escolhendo o Seedance 2.5). A API vinha depois: "API access coming soon via BytePlus ModelArk".
- A página do projeto indicada é https://seed.bytedance.com/seedance2_5.
- O motivo que o post dá para a versão: os usuários deixaram de querer só um trecho gerado e passaram a querer uma obra acabada.

## Os números que o post dá

| O quê | Valor |
|---|---|
| Duração de uma geração | até 30 s (no 2.0 eram 15 s), com áudio e vídeo |
| Extensão | várias rodadas sobre um vídeo já gerado, a ponto de chegar a vídeos de vários minutos |
| Referências num pedido | até 30 imagens, 10 vídeos e 10 áudios |
| O exemplo com mais referências | 18 imagens de referência num concerto de 30 s (sala, pianista, violoncelo, violino, cantor, orquestra, coro, plateia) |

Fora isso, o post não traz número: nem resolução, nem proporção, nem preço, nem medida de qualidade.

## Os controles que o post descreve

**Por referência.** O modelo lê de todos os arquivos a composição, a cena, o estilo, os personagens e os objetos, e os aplica como o prompt manda; o post afirma que mantém a aparência e a voz de vários personagens ao mesmo tempo. Três tipos de referência recebem nome:

- **Clay render:** da maquete 3D sem textura o modelo tira duas coisas, segundo o post, a geometria do plano e a luz. A luz sai fisicamente coerente (direção, temperatura de cor, intensidade, sombra) porque o modelo conhece a disposição espacial da cena; a geometria (o espaço, as poses, a trajetória, os ângulos de câmera) é o usuário quem monta, e o vídeo a segue, para que a composição e a blocagem de planos complexos fiquem como o criador planejou. Os dois prompts de exemplo pedem ao "@Clay Render 1" a câmera, o ritmo, as mudanças de enquadramento, a trajetória e a blocagem, e a uma imagem o desenho dos personagens, os materiais, a luz e a cor; um deles transforma a maquete numa sequência fotorrealista de montagem de carro.
- **Movimento** e **criativa:** citadas pelo nome, sem descrição própria no post.

**Por tempo.** O prompt pode dizer o que acontece em cada intervalo (narrativa, câmera, movimento, ritmo), e, depois de gerado, o vídeo pode ser corrigido num trecho delimitado (personagem, ação, enredo), mantendo o antes e o depois contínuos. Vários exemplos dividem o prompt em faixas de segundos ("0–5s", "6–10s").

**Por edição.** Três modos com nome:

- **Tela verde:** troca o fundo de um vídeo e conta outra história com o mesmo sujeito; o post destaca que o sujeito reage às regras físicas do novo ambiente (roupa, cabelo, passo, luz). O exemplo troca obstáculos, figurino e coadjuvantes de um vídeo de treino de futebol em três faixas de tempo.
- **Perspectiva de câmera:** o exemplo pede para manter personagens, ações e estilo e mudar só o movimento de câmera de um vídeo de 15 s, com um plano por faixa de tempo.
- **Edição por referência:** citada pelo nome.

**Por extensão.** Continua um vídeo gerado com os mesmos personagens, ambiente e ritmo. O exemplo pede outros 30 s a partir do @Video 1, mantendo sujeitos, cena, estilo e efeitos sonoros.

## O que o post diz da qualidade, nas palavras do fabricante

- Nos vídeos longos, transições de câmera mais suaves, sujeito estável entre cortes e som em sincronia com a imagem (o exemplo é uma cena de ópera de Pequim com a câmera girando em torno das mangas do ator).
- Em 30 s, o modelo organiza vários planos em começo, desenvolvimento, virada e desfecho, em vez de esticar um momento (o exemplo é uma cantora que sai do camarim, cruza os bastidores e entra no palco num plano só).
- Contra a aparência artificial, ajustes em textura de objetos, pele e olhos, luz e saturação, e menos legendas e música de fundo aparecendo sem ter sido pedidas.

## Usos fora do audiovisual que o post cita

- **Educação:** do lado do professor, vídeos de demonstração feitos com mais agilidade para princípios científicos, fatos históricos e procedimentos de experimento; do lado da aula, o pano de fundo histórico, os personagens e o enredo postos em imagem. O exemplo vem do "Doubao Classroom", do app Doubao Learning: uma rua de Lin'an na dinastia Song do Sul, com o poeta Xin Qiji tirado de uma imagem de referência.
- **Indústria:** dados sintéticos de vídeo para treinar percepção e manipulação de robôs, simulação industrial, treino de processo, demonstração de equipamento, e cenários raros (tempo extremo, trânsito complexo) para testar direção autônoma.

## O que o próprio fabricante admite que falta

Dois pontos fracos o fabricante admite no fecho: cenas em que vários sujeitos interagem ainda perdem estabilidade, e movimentos complexos nem sempre saem fisicamente plausíveis. Para frente, promete narrativa mais coerente, geração e edição mais intuitivas e um domínio maior da física do mundo real.

## O que o post não diz

- Resolução, proporções, taxa de quadros, formatos de saída e duração mínima.
- Preço, e quando exatamente a API chegaria à BytePlus.
- Línguas do áudio e da fala.
- Primeiro e último quadro, imagem para vídeo e laço: o post não fala de nenhum dos três.
- Regras sobre rosto de pessoa real.
- Comparação medida com outros modelos ou com o 2.0, além dos números de duração e de referências.
