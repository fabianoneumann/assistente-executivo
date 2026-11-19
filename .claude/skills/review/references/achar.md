# Achar: o isolamento, o que volta à sessão e a pasta fora do git

Os caminhos `scripts/...` e `references/...` partem da pasta da skill; os links com `./` ou `../`, do próprio arquivo; os demais caminhos, da raiz do projeto.

Dispare um agente (`general-purpose`) que **não viu a conversa**: ele recebe só o trabalho, as fontes, a régua e as lentes, com o modelo de pedido de [`prompts.md`](./prompts.md). Por quê: o revisor que leu como o trabalho nasceu herda o viés de quem o fez.

**O que chega ao agente filho:** ele não vê nada da conversa de quem o disparou, mas recebe o `CLAUDE.md` do projeto e o índice da memória do projeto (o `MEMORY.md`), quando existem. Isso foi conferido com um marcador posto só no contexto de quem disparou, que o filho não conhecia. Quer dizer que a memória leva ao revisor decisões e preferências de quem usa o ambiente, não a conversa; quando o trabalho depende de uma decisão que só está na conversa, ela vai escrita no pedido.

**O que volta:** no padrão e no profundo, o agente grava os achados na pasta temporária e devolve só a contagem por gravidade sugerida e o caminho do arquivo, que o conferente lê; no rápido, e quando não sobra nada para conferir, devolve o texto inteiro. Por quê: os achados inteiros entravam duas vezes na sessão principal, e devolver só a contagem e o caminho corta a carga em dezenas de vezes sem perda na entrega.

**Agente que falhou não revisou:** o de achar ou o de conferir que não responde, erra ou devolve o que não é achado nem "nada encontrado" roda de novo uma vez; se falhar outra vez, a etapa dele fica como **não rodou** na entrega e no registro, nunca como "nada achado", e os achados que dependiam dela vão como não conferidos. Por quê: ausente não é zero (`decisions/dado-de-fora.md`). O `/code-review` segue [`codigo.md`](./codigo.md).

**Pasta fora do git com dado de terceiro (as pastas `originals/`, pela régua de `knowledge/sources/README.md`):** o agente pode ler a pasta quando precisar; o limite é o git: nenhum trecho de mensagem, e-mail ou conversa de terceiro vai ao repositório nem à entrega, e de texto protegido só a citação curta que a régua da fonte permite; o que é do projeto e não traz conteúdo de terceiro pode ser versionado. O pedido de cada agente leva a linha fixa dos modelos de [`prompts.md`](./prompts.md), porque uma busca recursiva no projeto passa pela pasta mesmo quando o trabalho não a toca. Por quê: proibir abrir e varrer a pasta não se cumpria (a busca recursiva passava por ela sem dano), e o que importa é o que sai para o git.
