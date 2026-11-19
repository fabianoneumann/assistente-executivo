# O kit de projeto novo

Como um projeto de software novo nasce estruturado: a skill `project-kit`, o que ela traz pronto e o que se escolhe a cada projeto. O desenho está em `knowledge/software-engineering/kit-de-projeto-novo.md`, com a origem de cada parte: o processo de um CRM de atendimento em produção.

## 2026-11-17 — O processo de um CRM vira um kit, e a tecnologia fica à escolha de cada projeto

**Decisão (decidido na criação do kit):** o ambiente ganha a skill `project-kit`, que leva um projeto novo da discussão inicial até a primeira milestone com as specs: a arquitetura e o plano macro na base `knowledge/` do projeto, os ADRs 001 e 002, o repositório montado de modelos e conferido por script, o GitHub e um ponteiro de mão única do lado de cá. O processo vem do processo de um CRM de atendimento em produção (116 itens de processo dos 135 do inventário dele); a stack se escolhe a cada projeto, com duas variantes de partida (`python-fastapi` e `node-ts`) e a `outra`, com os comandos perguntados.

**As escolhas de gosto** (dez, numa mesa de escolhas, 7 de 10 iguais à sugestão):

| # | A escolha | O que o kit faz |
|---|---|---|
| q1 | (c) a base validada sem trava no hook | a regra escrita no `CLAUDE.md` do projeto: o agente commita a base depois do ok na conversa |
| q2 | (a) o agente corta a tag quando as portas passam | a tag anotada pelo agente; na conta pessoal privada, protegida pela regra escrita no `CLAUDE.md` do projeto (a regra de tag do GitHub pede o Pro) |
| q3 | (a) o ADR numerado | o `000-modelo.md` dos ADRs do projeto, com as cinco seções e o "Revê se" |
| q4 | (b) sem quadro | só as issues e a busca salva "o que pegar agora" |
| q5 | (a) a matriz de Eisenhower | o campo Priority na organização; os rótulos `prioridade:*` na conta pessoal |
| q6 | (a) milestones de cerca de duas semanas | fechadas por critério, duas em paralelo quando os relógios diferem |
| q7 | (b) sem rótulos de forma | a natureza no Type (ou no rótulo `defeito`, na conta pessoal) |
| q8 | (b) só HTML com SVG | os diagramas no repositório; o Mermaid sai; revista em 18/11: volta só como saída gerada do JSON (abaixo) |
| q9 | (b) o onboarding sempre em HTML | `onboarding/index.html`, que muda na mesma entrega que o processo |
| q10 | (b) sem o mod do fluxo | bastam o hook e o CI |

**As decididas D1 a D12, sem veto:** D1 o `--no-verify` em `deny` para o agente; D2 sem a caixa do aviso do Jev no PR; D3 o log com a entrada no fim e `merge=union`; D4 o "blocked by" nativo; D5 a branch `<issue>-<tema>`; D6 o Dependabot só de segurança, um PR por pacote, triagem pelo alcance; D7 as ações do CI fixadas pelo hash; D8 os "Requisitos" da spec só com o quê; D9 `eol=lf`; D10 o smoke em todo PR e a bateria antes da versão, com os tetos de 3 e 10 minutos; D11 as correções de uma revisão num commit por rodada; D12 perguntas e ideias na issue, sem as Discussions.

**A fronteira das travas:** sai toda pergunta de sim ou não, ou de 1 ou 2, que libera um comando do agente (os seis itens de interação do inventário: o `ask` antes de publicar e de pular os hooks, as variáveis da base e da tag, o "buscou antes de criar?" e a pergunta dos hooks desligados). Fica a trava que recusa e diz o que falta, o checklist do PR como declaração e a regra de conteúdo escrita. O projeto não leva `ask`, e o `conferir.py` recusa um `ask` no `settings.json`. A fronteira está escrita na página de travas da base que o projeto recebe (o modelo em `.claude/skills/project-kit/assets/projeto/knowledge/travas.md`), para nenhuma pergunta voltar.

**Motivo:** criar projetos novos bem estruturados, com a arquitetura pensada antes, um processo que já se provou com equipe e cliente, e a base no padrão LLM Wiki. A conferência contra as três fontes de referência sobre ambientes agênticos:
- **Anthropic:** o hook `PreToolUse` com `deny` roda antes da permissão e vale acima de qualquer modo (`knowledge/anthropic-claude/claude-code-sem-supervisao.md`); o `deny` do `.env` sozinho não barra um `grep -r` na pasta (`knowledge/anthropic-claude/distribuir-o-ambiente-a-uma-equipe.md`), limite escrito no `travas.md` do projeto. A skill segue as réguas de [`organizacao-das-skills.md`](./organizacao-das-skills.md) (um ofício, referência a um nível, o que é do ambiente num `references/projeto.md`).
- **Karpathy:** a base do projeto no padrão LLM Wiki; a regra que só mora numa página do wiki se segue pouco, e a regra num portão na hora da edição se segue quase sempre, que é a razão das travas em código; e nada de objetos de configuração gigantes: os comandos da stack são um JSON pequeno, e não um sistema de parâmetros.
- **Akita:** o CI como oráculo, sem o qual o ciclo gira no vazio; "o que uma máquina consegue conferir, ela confere", e o teste que falha sem o conserto, que é a regra dos testes das travas: cada recusa roda também sem a trava e deixa de recusar.

**Como aplicar:**
- Projeto de software novo nasce pela skill `project-kit`. O lugar, o dono no GitHub e o ponteiro estão no `references/projeto.md` dela.
- O projeto não cita este repositório; do lado de cá fica só o `projects/<nome>.md`.
- Mudança nos modelos do kit passa pelos testes dele (`teste_montar.py`) e pelo `conferir.py`, e pelas revisões de skill (`review` e `/code-review`).

**Revê se:** o primeiro projeto de verdade precisar de uma pergunta de sim ou não para destravar o agente (a fronteira não fechou), ou se o CI do primeiro push não sair verde sem ajuste à mão.

## 2026-11-18 — A skill chega a este modelo, com o projeto.md da conta pessoal

**Decisão:** a skill vem com o método igual, e muda só o que é deste ambiente, no `references/projeto.md`: o dono é a conta pessoal de quem usa (`--conta user`), com a prioridade e o defeito por rótulo, porque o Type e o campo Priority nativos são de organização; a regra da tag vai escrita no `CLAUDE.md` do projeto, sem a regra de tag do GitHub (o ruleset), porque no repositório privado de conta pessoal ela pede o GitHub Pro (a criação devolve 403), e o `github.py` não tenta criá-la ali; o responsável dos PRs do Dependabot é opcional e não se pergunta, porque quem cria o projeto já o acompanha e recebe o alerta; o projeto nasce ao lado do clone deste repositório, como um repositório próprio; o ponteiro de mão única vai a `projects/`. O `conferir.py` recusa no projeto a menção ao `assistente-executivo`, o nome deste repositório.

**Motivo:** a regra 3 de [`organizacao-das-skills.md`](./organizacao-das-skills.md): o método separado do que é do projeto, para a skill ir a outro ambiente trocando um arquivo só. Quem leva a skill a uma organização troca a seção "O dono no GitHub" do `projeto.md` (o `--conta org` já existe no `montar.py`).

## Proposto, sem decisão: o teste às cegas dos diagramas

Na q8, a observação foi que os diagramas do CRM poderiam ser ainda mais bem desenhados, e que talvez os do Codex saiam melhores. O roteiro, para decidir se roda:

1. **As três figuras:** do projeto de exemplo do kit, o fluxo dos oito passos, as camadas das travas, e uma terceira de arquitetura (as partes e as fronteiras de um sistema com banco e uma integração).
2. **Os dois braços:** cada figura desenhada pelo Claude e pelo Codex, em HTML com SVG escrito à mão, com o mesmo pedido, os mesmos tokens de cor e a mesma fonte da regra que a figura desenha.
3. **A renderização:** cada figura no claro e no escuro, a 1280 px de largura, com o texto renderizado sem a franja de cor (`--disable-lcd-text` no navegador).
4. **A mesa às cegas, com a régua escrita antes:** as duas versões de cada figura lado a lado, em ordem sorteada, sem dizer quem desenhou; para cada figura, a escolha e um comentário. **O Codex passa a desenhar o onboarding do kit se ganhar 3 de 3, ou 2 de 3 com a terceira empatada;** senão, segue o Claude.
5. **O resultado** vai a `knowledge/`, com as figuras, a régua e a mesa.

## 2026-11-18 — O padrão de diagramas, dois refinamentos do CRM e o Mermaid como saída gerada

**O padrão de diagramas:** os diagramas do kit seguem um padrão próprio, em `assets/diagramas/` da skill (o `LEIA.md` diz como funciona): o conteúdo num JSON, o layout pelo motor ELK (fluxo e grafo) ou por grade CSS (sequência), o estilo em tokens, e uma conferência por script que pega seta atravessando cartão, rótulo sobreposto, texto que sai da caixa e contraste, no claro e no escuro. O projeto montado recebe as travas em camadas e a prioridade em `onboarding/diagramas/`, com o esquema conferido no CI. Porquê: o padrão se justifica pela conferência, que nenhuma ferramenta pronta de diagrama como código faz.

**Dois refinamentos do CRM entram no `.claude/skills/project-kit/assets/projeto/knowledge/versao-e-dependencias.md` do modelo,** escritos sem a ferramenta: o teste de tela espera a resposta antes de ler o dado (um sinal que só a resposta produz; sem sinal, a leitura se repete até um prazo); e a dependência compilada se prova rodando (na imagem ou no binário de terceiro, o alerta de segurança só fecha com a versão nova, e a troca se prova rodando o que ela faz, não só com o build).

**A q8b fica revista só neste ponto:** o Mermaid volta ao kit como saída gerada do JSON do diagrama (`.claude/skills/project-kit/scripts/diagrama_mermaid.py`), para o ADR e o README, onde o GitHub desenha o bloco sozinho; a fonte continua o JSON, o onboarding continua em HTML com SVG, e nenhum diagrama se escreve à mão em Mermaid.
