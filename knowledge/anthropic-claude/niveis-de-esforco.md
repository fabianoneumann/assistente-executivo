# Níveis de esforço no Claude Code: o que controlam, o padrão de cada modelo e quando subir

Síntese para uso diário e para explicar o tema. Os padrões por modelo mudam a cada lançamento: reverificar na documentação antes de citar (os padrões, o ultracode e o `effortLevel` foram reconferidos em 2026-11-18, na página de configuração de modelo do Claude Code). Fontes: *Using Claude Code: Spending your effort*, de Thariq Shihipar (time do Claude Code, Anthropic) (https://claude.dev/blog/spending-your-effort/) (dados e regra prática), *Anthropic: Effort (parâmetro de esforço na Claude API)*, de Anthropic (documentação oficial da Claude API) (https://platform.claude.com/docs/en/build-with-claude/effort) (definição e padrões na API), *Claude Code: configuração de modelo, seção de esforço (níveis, padrões, /effort, ultracode)*, de Anthropic (documentação oficial do Claude Code) (https://code.claude.com/docs/en/model-config) (comandos e padrões no Claude Code), *Anthropic Academy: Choosing the right effort level in Claude Code*, de Anthropic Academy (tutorial oficial, sem autor nomeado) (https://academy.claude.com/tutorials/choosing-the-right-effort-level-in-claude-code) (método de ajuste). O short que trouxe o tema, fiel à fonte em todos os números conferidos, está em *The Truth About Claude Code Effort Levels (short): explicador em motion graphics de 3 minutos, sem corte*, de DIY Smart Code (canal no YouTube); análise de quadros pelo assistente (https://www.youtube.com/shorts/JYyzYnvad50).

## O que é esforço

Um **sinal de comportamento, não um orçamento de tokens**: diz ao modelo quanto trabalho você quer que ele ponha na tarefa, e ele decide como gastar. Afeta tudo o que ele produz, não só o pensamento: quantas ferramentas chama, se lê mais arquivos, se testa, se verifica, se explica o plano. Em esforço baixo, ainda pensa em problema difícil, mas pensa menos.

A analogia do Thariq, do time do Claude Code, serve direto para explicar: esforço é um **prazo**. Com 12 horas para uma tarefa, você capricha; com 1 hora, entrega uma versão sólida e itera. Esforço maior não muda o que o modelo sabe (isso é a escolha do modelo); muda quanto **julgamento independente e verificação** ele aplica.

## Os níveis

| Nível | O que faz | Quando usar |
|---|---|---|
| `low` | o mais rápido e barato; uma passada, pouca checagem | esboço, brainstorming, mudança fácil, com você olhando de perto |
| `medium` | equilíbrio entre velocidade, custo e qualidade | a maior parte do trabalho diário de escopo claro, como implementar uma feature |
| `high` | gasta o que a tarefa pedir; testa e verifica | onde verificação importa ou há caso de borda, como corrigir bug em código existente |
| `xhigh` | raciocínio estendido para trabalho longo | tarefas agênticas de mais de 30 minutos |
| `max` | sem restrição de gasto | problema difícil para o Claude resolver sozinho, de ponta a ponta; a doc avisa que pode ter retorno decrescente e pensar demais |

**A escala é calibrada por modelo:** o mesmo nome não representa o mesmo trabalho em modelos diferentes. Ao trocar de modelo, voltar ao padrão em vez de carregar o nível antigo.

## O padrão de cada modelo (na leitura desta página)

| Onde | Padrão |
|---|---|
| Claude Code, maioria dos modelos (Fable 5.1, Fable 5, Opus 5, Sonnet 5, Opus 4.8) | `high` |
| Claude Code, Fable 5.2, Opus 5.5, Sonnet 5.5 e Haiku 5.5 | `medium` |
| Claude Code, Opus 4.7 | `xhigh` |
| API, maioria dos modelos, **inclusive Sonnet 5.5** | `high` |
| API, Opus 5.5 e Haiku 5.5 | `medium` |

O Sonnet 5.5 é o caso que confunde: `medium` no Claude Code, `high` na API. Opus 4.6 e Sonnet 4.6 não têm `xhigh`; nível não suportado cai para o mais alto abaixo dele.

## Como ajustar no Claude Code

- `/effort` abre um slider; `/effort <nível>` define direto; `/effort auto` volta ao padrão do modelo. Enter no slider salva como padrão daquele modelo; `s` aplica só à sessão. Dá para mudar com o Claude trabalhando, e nos modelos novos isso não quebra o cache do prompt.
- `--effort <nível>` para uma sessão; `CLAUDE_CODE_EFFORT_LEVEL` no ambiente; `effortLevel` nas configurações (não aceita `max`).
- Uma skill ou subagente pode fixar o próprio nível no frontmatter (`effort`), que vale enquanto ela está ativa.
- **Ultracode não é nível de esforço:** é uma configuração do Claude Code que faz o agente orquestrar workflows em tarefas grandes; liga em `xhigh`.
- **Pensamento e esforço são coisas diferentes.** Nos modelos novos (Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable) o pensamento não desliga, e esforço é o controle de quanto ele pensa. `ultrathink` no prompt pede mais raciocínio só naquele turno.

## O que os dados mostram

Testes do Thariq, publicados em 25/09/2026 (*Using Claude Code: Spending your effort*, de Thariq Shihipar (time do Claude Code, Anthropic)):

- **Sem especificação, esforço decide o produto.** O mesmo pedido ("um app pessoal de treino") levou 1,5 min em `low` (um log e um gráfico) e 67 min em `max` (com mapa de calor e várias escolhas próprias do modelo). **Com especificação feita por entrevista**, os quatro níveis levaram de 16 a 79 min e entregaram apps muito parecidos.
- **O salto é grande onde há caso de borda escondido.** Num sanitizador de HTML, o Fable 5.1 passou em 1 de 5 tentativas em `low` e em 5 de 5 em `xhigh`. A diferença é de processo: `low` escreveu numa passada e testou uma página em 2 min; `high` atacou o próprio rascunho, leu o código do parser, rodou uma suíte de XSS e escreveu um fuzzer em 33 min. Por categoria, de esforço baixo para alto: segurança 64% → 87%, hardware 34% → 75%, operações 12% → 22%.
- **Esforço tem limite.** Em 370 tentativas por nível, `max` derrubou os casos esquecidos de 59 para 24, mas as decisões erradas só caíram de 133 para 107, e **escolher a leitura errada da tarefa subiu de 25 para 47**: com mais autonomia, o modelo faz mais suposições por você. Custou cerca de 3 vezes os tokens.

A frase para guardar: **esforço pega o caso que você esqueceu, não conserta a abordagem errada.** Ambiguidade se resolve com especificação e com você no loop, não com mais esforço.

## A regra prática

Esforço baixo demais também sai caro: o modelo para cedo com trabalho inacabado (*Anthropic Academy: Choosing the right effort level in Claude Code*, de Anthropic Academy (tutorial oficial, sem autor nomeado)). O método é começar no padrão, olhar o resultado, mexer um nível por vez e parar quando atende.

O ciclo de feature do Thariq, que junta tudo:

1. Dar uma especificação e pedir ao Claude que **entreviste você** sobre o que falta.
2. **Construir em `low`** (ou `medium`).
3. **Você revisa** se ele pegou a essência, iterando em `low`.
4. **Verificar e testar em `high`.**

`max` fica para trabalho que o Claude faz sozinho de ponta a ponta. Em trabalho de feature, ele tira você do loop e aumenta as suposições.

## Ressalvas e o que não está verificado

- Os dados são testes internos da Anthropic: 5 tentativas por tarefa, categorias de 4 a 20 tarefas, benchmark comunitário (Terminal-Bench 3.0), exemplos de execução única. Percentual por categoria é ruidoso.
- O gráfico anota "mesma nota, metade dos tokens" sem dizer no texto quais pares empatam; o short leu como Opus 5.5 em `high` contra Fable 5.1 em `max`. Não citar o par sem abrir o gráfico.
