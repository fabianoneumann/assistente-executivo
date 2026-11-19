# Lições que viraram regra

As lições de peças que já viraram regra, cada uma com o lugar onde a regra mora hoje. **Não se lê antes de criar:** quem cria lê a regra no lugar onde ela age (a rubrica, o design system, a skill, o README da pasta). Este arquivo serve para saber de onde a regra veio e para não registrar de novo, em [`licoes.md`](./licoes.md), uma lição que já vale. As etapas e as áreas são as de `licoes.md`.

As linhas abaixo vêm prontas com o ambiente: são lições gerais, aprendidas na produção de carrosséis e Stories antes deste repositório, que já estão escritas nas réguas e nas skills. A lição da equipe que virar regra entra no fim da tabela da etapa, com o destino.

Siglas dos destinos: **RQ** `social-media/rubrica-de-qualidade.md`; **RD** `social-media/rubrica-de-design.md`; **RS** `social-media/rubrica-de-stories.md`; **portão** `social-media/portao-de-qualidade.md`; **DS** o `design-system.md` da série; **S-README** `social-media/stories/README.md`; skills em `.claude/skills/`.

## Ideia, pauta e texto

| Lição | Etapa | Área | Destino |
|---|---|---|---|
| Antes de levar uma tese à mesa, tire da base o que pode derrubá-la | ideia e apuração, pauta | integridade e lastro | `story-angle` (Fase 0) |
| Tese além da evidência dispara rodada dirigida; rebaixar só depois de 2 ou 3 reformulações | pauta | integridade e lastro | `story-angle` |
| Verifique o superlativo na fonte primária | ideia e apuração, pauta | integridade e lastro | `story-angle` |
| Conteúdo sem citação é não verificado, não falso: rode uma leva dirigida | ideia e apuração | integridade e lastro | `research`, `story-angle` |
| Tenha na mesa um ângulo com protagonista diferente do óbvio | pauta | posicionamento | `story-angle` |
| Em série, a capa do post B se sustenta sem o A | pauta, texto | posicionamento | RQ (A) |
| Separe o que o autor diz de como quem publica aplica, e assuma a aplicação | pauta, texto | integridade e lastro | RQ (método de terceiro) |
| A ação pedida é coerente com a tese | pauta, texto | didática | RQ (erro de conteúdo) |
| Aspas e rótulo de fala só com a versão literal e a fonte | texto | integridade e lastro | RQ (citação), `piece-script` |
| Na ponte de série, peça "segue", não "salva"; uma chamada só | texto | posicionamento | RQ (K) |
| Na tela de referência, recursos que sirvam ao público, em corpo de conteúdo | texto, forma | didática, tipografia | RQ (E), RD (D1) |
| A síntese da base não é lastro sozinha: aponte a fonte | texto, avaliação | integridade e lastro | RQ (afirmação sem lastro) |
| Experiência pessoal vem de quem publica: dar a forma, não inventar vivência | texto | texto e voz | RS ("Onde vive uma sequência") |
| Num ajuste de forma, não troque palavra aprovada; corte só como alternativa, com antes e depois | forma, texto | processo | `visual-form`, `piece-creation`, RS |
| Sem "hoje", "amanhã" nem "ontem" na peça | texto | texto e voz | RQ (referência relativa de dia), S-README |
| A pergunta da enquete feita no texto vai antes do resultado | texto | didática | RS (resultado sem a pergunta) |
| Uma ideia por tela no Story avulso | texto | texto e voz | RS (A2, hipótese) |
| Os fatos do Story vêm de peça que passou pelo portão, sem número novo | ideia e apuração, texto | integridade e lastro | RS (falha herdada de lastro) |

## Forma

| Lição | Etapa | Área | Destino |
|---|---|---|---|
| Meça a posição no navegador, não a olho | forma, avaliação | layout | `visual-form` |
| Distribua o respiro entre os blocos | forma | layout | RD (D5) |
| O texto do Story começa em 192 px, abaixo da linha do app | forma | layout | RS (texto essencial coberto) |
| A seta não cruza letra | forma | layout, imagem | RD (D5, texto sobre desenho) |
| Um estilo de desenho por peça no vídeo; no carrossel, os estilos que o sistema declara convivem | forma | imagem | RD (D7) |
| O desenho diz o mesmo que o texto | forma | imagem | RD (D7) |
| Pessoa real: foto real com direito e crédito, nunca retrato gerado | forma | integridade e lastro | RQ, RD (D7) |
| Quando o texto não cabe: primeiro o que não custa espaço (balance, pretty, título por sentido), depois posição e respiro, um degrau do corpo até o piso sem descer o título, e só então alternativas com antes e depois | forma, texto | tipografia | `visual-form`; `knowledge/content-design/texto-que-cabe-e-legibilidade.md` |

## Avaliação, publicação, medição e planejamento

| Lição | Etapa | Área | Destino |
|---|---|---|---|
| Mensagem até o texto travar, depois a forma; reavaliar só o que mudou | avaliação | processo | portão (regra 1) |
| Teto de duas a três passadas, pelo risco de regressão | avaliação | processo | portão (regra 3) |
| Saída com atração de pelo menos 7 por tela e 8 na capa | avaliação | processo | portão (regra 3) |
| O juiz passa antes de quem decide | avaliação | processo | portão (regra 2) |
| Tela aprovada congela; mudança de sistema compara pixel a pixel | avaliação, forma | processo | portão (regra 5) |
| Registre cada passada em `refinamentos.md` | avaliação | processo | portão (regra 6) |
| No Story em vídeo, o S2 vale para o primeiro segundo, e o A2 se mede pelo tempo de leitura, não pelas 40 palavras | avaliação | régua | RS ("Story em vídeo") |
| Toda geração sobe o original ao banco, e o roteiro aponta os artefatos | exportação e publicação | processo | `image-gen` |
| O prompt exato de cada imagem vai em `prompts.md` | exportação e publicação | processo | `image-gen` |
| Imagem trocada no mesmo endereço, até a publicação, leva `?v=N` (depois, versão nova, sem sobrescrever) | exportação e publicação | processo | RS ("Onde vive uma sequência") |
| Cada Story avulso tem o próprio `stories.html` | exportação e publicação | processo | RS ("Story avulso") |
