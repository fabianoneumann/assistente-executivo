# Organização das skills

Como as skills deste repositório se dividem, se ligam e crescem. O registro das lições está em [`licoes-das-skills.md`](./licoes-das-skills.md). Esta decisão é o mapa do conjunto: o que cada skill faz e as regras que valem para todas.

## Um ofício por skill, ligadas por arquivo com dono, e cada mudança fechada por teste

**Decisão:** o ambiente de skills se organiza por cinco regras.

1. **Uma skill por ofício.** Cada skill faz uma coisa e é a única dona dela, e as outras a chamam pelo nome, sem copiar os passos. Por quê: o passo copiado em vários lugares diverge, e a correção feita num não chega aos outros.
2. **Ligadas por arquivo, não por conversa.** O que passa de uma skill à outra é um arquivo com dono e com formato escrito: a escaleta da `piece-script`, a pasta `object/` da `object-anatomy`, o `slides.html` da `visual-form`, a `legenda.md` que a `slides-export` grava. Onde dá, quem recebe confere o arquivo por script antes de usar. Por quê: o que passa pela conversa se perde entre sessões e não se confere.
3. **O método separado do que é do projeto.** A skill guarda o método. O que é deste projeto (os caminhos das réguas, a série, o público, os nomes das pastas) fica num arquivo só da skill, o **`references/projeto.md`**, ou num dado da série, e nunca dentro do código. Por quê: é o que deixa a skill ir a outro projeto, ou ser instalada como plugin, trocando um arquivo só.
4. **As réguas da Anthropic:**
   - a descrição tem até 1.024 caracteres e diz o que a skill faz e quando usá-la (e quando não);
   - o `SKILL.md` fica abaixo de 15 KB, como roteiro;
   - a regra inteira, com o porquê, vai em `references/`, a um nível só, apontada no passo em que vale ("Leia ... antes de");
   - a variante (carrossel, Stories, Reel) também vai em referência.

   A skill que precisa de contexto limpo (a `object-anatomy`, a `base-enrichment`) roda num subagente (`context: fork`), com o agente em `.claude/agents/`.
5. **Mudança por passos, cada um fechado por teste.**
   - A rede de segurança vem antes de toda refatoração: a linha de base dos testes e o disparo medido (as frases que devem e as que não devem disparar a skill).
   - A refatoração muda o lugar, não o resultado: um passo prova que nada mudou (os mesmos resultados e os mesmos achados antes e depois), e a regra nova entra em outro passo.
   - Criar ou editar uma skill passa pela `skill-creator`, quando a mudança é de estrutura, e pela `review`, com a lente "efeito nas outras skills". O código passa pelo `/code-review`.

**O mapa:**

| Ofício | Skill | Chama ou é chamada por |
|---|---|---|
| Registrar a ideia crua | `idea-capture` | — |
| Apurar até a pauta | `story-angle` | chama a `research` |
| Pesquisar com fontes | `research` | chamada pela `story-angle`, pela `piece-creation` e direto |
| Revisar o que o assistente fez | `review` | chamada na etapa de revisão das de apuração, roteiro e criação, e em toda edição de skill |
| Levar a peça da ideia à prévia | `piece-creation` (orquestradora, sem ofício próprio) | chama a `story-angle`, a `research`, a `piece-script`, a `review`, a `visual-form` e a `slides-export` |
| Escrever o roteiro até a trava | `piece-script` | chama a `base-enrichment` |
| Montar a forma das telas e as conferências de forma | `visual-form` | chama a `image-gen`, a `object-anatomy` e a `base-enrichment` |
| O objeto que se move | `object-anatomy` (subagente) | chamada pela forma ou direto |
| A passada de método pela base | `base-enrichment` (subagente) | chamada pelo roteiro e pela forma |
| Gerar imagem | `image-gen` | chamada pela forma ou direto |
| Exportar e gravar a tela em vídeo | `slides-export` | chama as conferências da `visual-form` antes de subir |
| Guardar no bucket | `r2-storage` | chamada pela exportação e pela `image-gen` |
| Criar um projeto de software novo | `project-kit` | chama a `research` quando a escolha depende de dado de fora, e a `review` no texto da base de um projeto grande |

**Motivo:** alta coesão e baixo acoplamento, conferidos contra as fontes de referência sobre ambientes agênticos:
- **Anthropic:** uma skill, uma responsabilidade, e a orquestradora que combina blocos em vez de uma skill com tudo; a referência a um nível só do `SKILL.md`; e as avaliações antes da escrita (as boas práticas de skills).
- **Akita:** poucas skills, cada uma um procedimento que se repete, e cada regra nascida de um erro; "o que uma máquina consegue conferir, ela confere"; e o conserto começa por um teste que falha no código velho.
- **Karpathy:** nada de objetos de configuração gigantes. Por isso o que é do projeto fica num arquivo pequeno, e não num sistema de parâmetros.
