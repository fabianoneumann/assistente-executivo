# O modelo no design e na leitura de imagem: o que a documentação da Anthropic diz

O que as notas de modelo da documentação oficial dizem sobre ler imagem e fazer frontend, e o que isso pede de quem monta a forma de uma peça. As notas mudam a cada modelo novo e se reconferem na documentação antes de virar dependência: o Fable comparado aqui era o 5.1.

## O que a documentação diz

- **O Opus 5.5 lê imagem com mais precisão:** gráficos, diagramas e capturas de tela, inclusive o que depende de posição, como que caixas uma seta liga ou o que mudou entre duas versões de um diagrama. Mesmo no esforço baixo, leu gráficos melhor que o Opus 5 no esforço máximo.
- **O Opus 5.5 faz frontend sem direção em estilos padrão:** fundo creme, uma palavra em itálico no título, rótulos "01/02/03".
  - Pedir "evite cara de IA" só troca um padrão por outro.
  - Ele responde bem quando se **nomeiam os padrões a evitar**, iterando a partir do que saiu.
- **As notas do Fable** (5.1 na época) listam ganhos em código de sessão longa, documento e deck do zero, pesquisa, imagem densa e contexto longo. Não há nota de design de frontend nem de estilo visual.
- **A documentação não compara os modelos em design.**

## O que isso pede de um ambiente de produção de peças

- **A forma executa um sistema já escrito:** o design system da série, as rubricas, as medidas em código e uma lista de marcas de cara de IA na rubrica de design. Esse sistema é o "nomear os padrões a evitar" que a documentação recomenda. A skill `visual-form` trabalha a partir dele, e não de um pedido aberto de estética.
- **O modelo confere a própria renderização** antes de mostrar (o render e as conferências de tela). É o ponto em que a nota do Opus é explícita: a seta que liga a caixa e o que mudou entre versões.
- **Leitura não medida:** o Fable poderia fazer diferença numa direção de arte do zero (o design system de uma série nova). Para tirar a dúvida, um teste às cegas entre os dois modelos no mesmo briefing, na primeira direção de arte nova.

Liga com `niveis-de-esforco.md` (esforço não conserta abordagem errada) e com a rubrica de design do projeto (as marcas de cara de IA).
