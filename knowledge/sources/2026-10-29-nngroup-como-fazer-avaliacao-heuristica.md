---
titulo: "How to Conduct a Heuristic Evaluation"
tipo: artigo
autor: "Kate Moran e Kelley Gordon (Nielsen Norman Group)"
url: "https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/"
publicado_em: 2023-06-25
capturado_em: 2026-10-29
licenca: "Rodapé do site: 'Copyright © 1998-2026 Nielsen Norman Group, All Rights Reserved', com política própria de cópia e reimpressão. A página das 10 heurísticas permite usar as heurísticas no próprio trabalho com crédito a Jakob Nielsen e link, mas reproduzir o conteúdo pede a política de copyright. Entra só a ficha."
areas: [agent-engineering, content-design]
tags: [heuristic-evaluation, usability, independent-review, evaluator-aggregation, checklist, review-scope, review-consolidation]
---

Ficha de estudo, em palavras próprias, do passo a passo da Nielsen Norman Group (NN/g) para a avaliação heurística, com a lista das 10 heurísticas da página complementar "10 Usability Heuristics for User Interface Design" (Jakob Nielsen, publicada em 24/04/1994, revista em 30/01/2024, https://www.nngroup.com/articles/ten-usability-heuristics/), que o artigo manda usar. Ambas lidas no HTML em 2026-10-29. O artigo é a versão de 2023 (substitui o texto antigo de Nielsen de 1994 no mesmo endereço) e traz um caderno de trabalho em PDF para baixar, não capturado. Citações literais só curtas.

## O que é

Um método para identificar problemas de desenho numa interface: avaliadores julgam o desenho contra um conjunto de diretrizes amplas (as heurísticas) que tornam um sistema fácil de usar. A origem do método está em Nielsen e Molich (1990) [[2026-10-29-nielsen-molich-avaliacao-heuristica]] e no capítulo de Nielsen de 1994 em *Usability Inspection Methods*; a recomendação de quantos avaliadores cita também Nielsen e Landauer (1993).

## Escolher o conjunto de heurísticas

Qualquer conjunto serve. Para usabilidade, a NN/g recomenda as 10 heurísticas de Nielsen, diretrizes de alto nível baseadas em comportamento humano, psicologia e processamento de informação. Em domínios especializados ou avaliações de outro tipo, vale somar heurísticas próprias do domínio, além das 10.

### As 10 heurísticas (página complementar), em palavras próprias

1. **Visibilidade do estado do sistema:** manter a pessoa informada do que está acontecendo, com retorno adequado e em tempo razoável. Nada com consequência para o usuário acontece sem avisá-lo; retorno o mais rápido possível.
2. **Correspondência entre o sistema e o mundo real:** falar a língua de quem usa, com palavras e conceitos familiares, não o jargão interno; seguir as convenções do mundo, em ordem natural e lógica. O que é claro para a equipe pode não ser para o usuário; a pesquisa revela o vocabulário dele.
3. **Controle e liberdade do usuário:** as pessoas erram a ação; precisam de uma "saída de emergência" visível para desfazer sem um processo longo. Desfazer e refazer, botão de cancelar, saída fácil de achar.
4. **Consistência e padrões:** a pessoa não deveria se perguntar se palavras, situações ou ações diferentes significam a mesma coisa. Consistência interna (dentro do produto e da família de produtos) e externa (convenções da plataforma e do setor).
5. **Prevenção de erros:** melhor que uma boa mensagem de erro é evitar o problema; eliminar as condições que levam ao erro ou pedir confirmação antes da ação. Dois tipos de erro: deslize (desatenção) e engano (modelo mental diferente do desenho). Prevenir primeiro os erros caros.
6. **Reconhecer em vez de lembrar:** reduzir a carga de memória deixando elementos, ações e opções visíveis; a pessoa não deveria precisar lembrar informação de uma parte da interface para outra.
7. **Flexibilidade e eficiência de uso:** atalhos, escondidos do iniciante, aceleram o experiente; permitir personalizar ações frequentes.
8. **Desenho estético e minimalista:** nada de informação irrelevante ou raramente necessária; cada unidade extra compete com as relevantes e reduz a visibilidade delas. Não significa desenho plano, e sim conteúdo e visual focados no essencial.
9. **Ajudar a reconhecer, diagnosticar e se recuperar de erros:** mensagem em linguagem simples, sem código de erro, dizendo com precisão o problema e sugerindo a solução, com tratamento visual que a faça ser notada.
10. **Ajuda e documentação:** o ideal é não precisar de explicação, mas, quando precisa, a ajuda deve ser fácil de buscar, focada na tarefa, curta, com passos concretos, e de preferência no contexto, na hora em que a pessoa precisa.

Na nota de Nielsen na mesma página: a primeira versão veio com Molich em 1990; em 1994 ele refinou a lista com uma análise fatorial de 249 problemas de usabilidade, buscando o conjunto de maior poder explicativo; em 2020 a NN/g refinou a redação e os exemplos, mas as 10 heurísticas seguem as mesmas desde 1994.

## Quando fazer

- Serve para achar problemas evidentes em praticamente qualquer coisa com que o usuário interage: protótipo, produto físico, jogo, realidade virtual, interface de voz. Ajuda especialmente cedo no processo de desenho.
- Estica um orçamento curto de pesquisa, porque acha problemas prováveis sem testar com participantes.
- **Não substitui a pesquisa com usuário:** a experiência depende de contexto e ainda é preciso testar com gente real. Complementa: feita antes de um teste de usabilidade, ajuda a escolher o que o teste deve mirar.
- É também um treino de instinto de UX: quem está começando pode praticar em muitos produtos, inclusive os que não são seus.

## Passo 1: preparar

**Escolher e treinar a equipe.** A avaliação funciona melhor em grupo do que com uma pessoa, porque cada indivíduo, por mais experiente, deixa passar parte dos problemas. O ideal são **três a cinco pessoas avaliando a mesma interface de forma independente**. Na primeira vez, cada um lê e entende as heurísticas, e vale uma rodada de treino em grupo com um desenho simples (o exemplo é um aplicativo de previsão do tempo) para todos entenderem o que se espera deles.

**Decidir onde registrar.** Três opções: o caderno de trabalho da NN/g (PDF interativo, impresso ou digital, com um lembrete de cada heurística e espaço para problemas e recomendações); uma planilha, com uma observação por linha e a heurística correspondente; um quadro branco digital (Miro, Mural) com área separada por avaliador, capturas de tela e notas adesivas sobre os elementos. Se o espaço for compartilhado, **ninguém vê a avaliação do outro antes de terminar a sua**: o motivo de ter vários avaliadores é colher observações independentes, sem influência mútua.

**Delimitar o escopo.** Quanto mais estreito, mais fácil e detalhada a avaliação. Na primeira vez, ou com produto grande e complexo, estreitar por: uma tarefa por vez; uma seção do site ou do aplicativo; um grupo de usuários, se houver vários com necessidades diferentes; um tipo de dispositivo (computador, tablet, celular).

## Passo 2: avaliar sozinho

- Cada pessoa avalia por conta própria, com tempo marcado: **cerca de 1 a 2 horas**.
- **Conhecer o produto:** registrar no topo do caderno o produto, o grupo de usuários, a tarefa e o dispositivo (no exemplo: o site da Banana Republic, compradores, comprar uma camisa, celular). Percorrer a interface como um usuário tentando cumprir a tarefa; se o produto for novo para o avaliador, fazer a tarefa uma vez só para aprender, sem avaliar nada.
- **Procurar problemas numa segunda passada:** buscar elementos, recursos ou decisões que violam alguma das 10 heurísticas, ou seja, que não cumprem aquele objetivo ou diretriz. Anotar o problema na heurística correspondente e, se uma correção vier à mente, anotá-la como recomendação.
- **Exemplo da heurística 8 (estético e minimalista):** as páginas de listagem põem nome, preço e desconto em texto branco direto sobre a foto do produto; a página fica poluída e o texto, difícil de ler. Problema: texto sobreposto às imagens. Recomendação: melhorar a visibilidade do detalhe, talvez com um fundo sólido ou semitransparente atrás do texto.
- **Exemplo da heurística 6 (reconhecer em vez de lembrar):** a navegação global fica atrás de um menu "hambúrguer"; as categorias ficam escondidas e a pessoa precisa lembrar de abrir o menu. É uma violação, mas não quer dizer que a escolha esteja errada: no celular, com pouca tela, essa troca costuma ser necessária.
- **A regra que sai do exemplo:** violar uma heurística **não significa necessariamente** que é preciso consertar; depende do contexto e das alternativas disponíveis. É também por isso que o método não substitui observar usuários de verdade.

## Passo 3: consolidar

Depois que todos terminaram as avaliações independentes, sintetizar os problemas. Diagrama de afinidade (agrupar problemas parecidos) num quadro físico ou virtual funciona bem. Perguntas para discutir em equipe:

- Onde concordamos e onde discordamos?
- Quais problemas parecem mais prejudiciais à experiência como um todo?
- Quais podem ser mais problemáticos para os objetivos da organização ou do negócio?
- Sobre quais precisamos de mais dados, e quais priorizar no próximo teste de usabilidade?
- Que passos tomar a curto e a longo prazo para resolver?

## Exceções

Há exceções às heurísticas, raras e dependentes do contexto: heurística é diretriz, não lei, e às vezes se viola uma em favor de outro objetivo (o caso do menu hambúrguer). Mas, citando Nielsen, "you should not bet that your design is one of the few exceptions". Antes de violar uma heurística de propósito, fazer pesquisa com usuário para justificar a quebra da regra.

## Conclusão do artigo

A avaliação fica mais fácil com a prática; com o tempo, depende-se menos da lista e se reconhece o problema pelo instinto.

## Limites declarados

O método acha problemas prováveis, não confirmados: não substitui a pesquisa com usuário, e uma violação pode ser uma troca aceitável no contexto. O artigo não traz números próprios; a recomendação de três a cinco avaliadores remete aos trabalhos de 1990 e 1993 citados nas referências.
