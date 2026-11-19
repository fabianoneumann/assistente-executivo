# Mesas de decisão de design

## Regra se confere, gosto se pergunta; a variável se decide no passo, a combinação no todo

**Decisão:** numa mesa de escolhas de forma (design system, conceito de série, rodada de design), só entra o que é gosto ou direção de arte. O que já é regra escrita (o `design-system.md` da série, a rubrica de design, as regras de livro que a base registrou) se confere em código ou leitura, e cada opção chega à mesa já conferida, com o conceito e a justificativa de por que cabe. O passo a passo decide variáveis, uma por comparação, sobre a mesma tela e com o mesmo acabamento; a visão do todo valida combinações: cada camada de decisões fecha com um retrato da peça inteira ao lado da versão anterior, e o que destoar reabre uma decisão, não todas.

**Motivo:** perguntar de novo o que a régua já responde desperdiça a leitura de quem decide e mistura técnica com gosto; na prática, quando a mesa leva itens que já eram regra, boa parte deles sai, e quem decide devolve a decisão à régua ("respeitar o conhecimento ingerido"). Uma variável por comparação é o que deixa ver o efeito de cada escolha; e há interações que só a tela inteira mostra (fonte, corpo e entrelinha com o fundo; moldura, paginação e selo), por isso o retrato do todo.

**Como aplicar:** antes de montar a mesa, mapear cada item contra o design system, a rubrica e as regras da base, e registrar o que saiu e onde já é regra; o que fica recebe opções renderizadas, sem rótulo de recomendação antes do clique; o retrato do todo sai numa pasta própria, nunca sobre a peça publicada. A mesa grava cada clique (no banco da página, quando é um artifact), com espaço para comentário por item e a opção de não escolher.

**Grandeza, "pela régua" e a sugestão depois do clique:**
- Decisão com grandeza (um limite numérico) vai pela **escada**: os casos medidos aparecem do menor desvio ao maior, com a medida, e o degrau marcado vira o limite que o código aplica (o método do marcador para nota de corte, `knowledge/agent-engineering/ponto-de-corte-reuso-do-teste-e-desvio.md`).
- Toda mesa tem a opção **"pela régua" ou "não sei"**: sem ela, quem decide escolhe no escuro onde a régua responderia melhor.
- A **sugestão do assistente, com o porquê, aparece depois do clique**, não antes, e a resposta pode ser trocada ao lê-la: a sugestão vista antes ancora a escolha (`knowledge/agent-engineering/quem-le-a-saida-do-avaliador.md`), e vista depois ainda corrige o erro de leitura.
- **Os números da pergunta se conferem contra a régua vigente antes de publicar a mesa:** a pergunta que leva um número já superado produz uma regra errada, que a revisão depois tem de desfazer.
