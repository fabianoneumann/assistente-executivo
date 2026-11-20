# O kit de projeto novo: o processo de um CRM destilado para qualquer stack

O desenho da skill `project-kit` (17/11/2026): o que um projeto de software novo recebe pronto, de onde cada parte veio no processo de um CRM de atendimento em produção e o que mudou no caminho. A decisão, com as escolhas e o porquê, está em `decisions/kit-de-projeto-novo.md` (os códigos q1 a q10 e D1 a D12 abaixo são dela). A síntese da prática do CRM, com os números do projeto, não vem neste modelo. **Ler quando:** for criar um projeto novo, mudar um modelo do kit, ou explicar a alguém de onde veio uma regra do processo de um projeto.

## A ideia

O processo vem pronto, a tecnologia se escolhe. O processo do CRM foi inventariado item a item, em três classes: o que é processo (P) virou modelo, regra escrita ou trava; o que é interação, a pergunta de sim ou não que libera um comando do agente (T), saiu; o que só servia ao CRM (C) ficou de fora. Dos 135 itens, 116 eram de processo, 6 de interação e 13 só do CRM. O kit é uma árvore de modelos (`assets/projeto/`) com marcadores e blocos por stack e por conta, montada por um script e conferida por outro.

## O que o projeto recebe

| Parte | O que é | De onde veio no CRM |
|---|---|---|
| `CLAUDE.md` (cerca de 70 linhas) e `AGENTS.md` curto | o roteador: onde mora o quê, as regras, os comandos da stack, o fluxo em 8 passos, como abrir e fechar o PR, a versão | o `CLAUDE.md` do CRM, sem a stack e sem o produto |
| `knowledge/` | o LLM Wiki: `README`, `index`, `log`, `processo`, `metadados`, `travas`, `versao-e-dependencias`, `arquitetura`, `plano` e os ADRs | o processo de issues, os metadados da issue, as travas do processo e o modelo de ADR do CRM |
| Os modelos de issue | a spec (os "Requisitos" só com o quê, com a prioridade, a milestone e o "blocked by" na lateral) e o defeito (o primeiro critério é o teste que falha antes) | os modelos do CRM (D8) |
| O modelo de PR | o `Closes`/`Refs`, o checklist de declaração, a "Validação exploratória" e as "Divergências" | o modelo do CRM, sem a caixa do aviso do Jev (D2) |
| O CI | as travas e o log primeiro (só Python), depois o formato, o lint, o smoke e os testes, com as ações fixadas pelo hash, em até 3 minutos, no PR e no push ao `main` | o CI e o estudo do tempo do CI (D7, D10) |
| O Dependabot e as notas | só segurança, um PR por pacote; as notas em duas seções | a manutenção do CRM (D6) |
| As travas | o hook do agente (`fluxo.py`), os hooks do git (`hooks.py`) e o `deny`, com os testes em tabela | as travas em camadas do CRM (D1) |
| O onboarding | `onboarding/index.html`, com os diagramas em SVG e a busca "o que pegar agora" | o onboarding do CRM (q8b, q9b, q4b) |
| O esqueleto da stack | o `/health` (com a versão e o commit), um teste e o smoke que sobe o servidor de verdade, para o CI nascer verde | novo: o CRM nasceu antes do processo |
| A vigia e o método | "como se sabe que parou" na discussão e na arquitetura; o ADR vivo e o "O que ficou sem prova"; o spike; as regras de teste; o `concurrency` do CI; as armadilhas do Dependabot | a segunda leitura do processo do CRM |
| A imagem, opcional (`--docker`) | o `Dockerfile` da stack, o build no CI, a publicação imutável na tag e o vigia semanal da imagem base, com `knowledge/imagem-base.md` | o padrão de imagem do CRM, com uma imagem só e o vigia em Python |
| A spec, a revisão e a passagem | na spec, o teste do essencial, o bloqueio de cada pergunta, o que não pode acontecer e a alternativa descartada; o escopo que entra tira outro; o achado com a consequência, o PR com o que se pulou e o risco, a lente de tela; a passagem entre sessões como estado; a volta escrita antes de instalar; o passo de procedimento de `docs/` | leituras de plugins e de referências de mercado, e não o CRM |
| O roteador e a base sem deriva | o `.github/scripts/conferir_base.py` no CI: os caminhos e os comandos do `CLAUDE.md`, os passos do CI contra eles, as páginas do índice; aviso da órfã e do código que a base cita e saiu | o `claude-md-management` da Anthropic (a atualidade do `CLAUDE.md`), e não o CRM |

## As travas: uma versão só, em Python

O CRM tem as travas em TypeScript (o hook do fluxo tem cerca de mil linhas, e o mod mais as dele). O kit tem uma versão só, em Python com a biblioteca padrão, numa casca `sh`, para servir a qualquer stack: o `fluxo.py` com cerca de 390 linhas e o `hooks.py` com cerca de 190.

- **O que ficou da forma do CRM:** a casca fina sobre lógica testada; passar é não imprimir nada; sem rede, deixa passar e avisa; o Bash e o PowerShell gêmeos; o prazo de 25 s dentro dos 30 s; o `gh pr create` e o `gh pr merge` numa chamada própria; o formatador sobre o conteúdo do índice, sem reescrever; o `gh pr checks --json` lido pelo conteúdo, e não pelo código de saída.
- **O que saiu:** as perguntas (o `ask`, as variáveis da base e da tag, o "buscou antes?", a confirmação dos hooks desligados, que virou aviso); as revisões por área (são do produto); a trava da tag no `pre-push` (a q2a deixa o agente cortar a versão, e a regra de tag do GitHub protege a tag publicada).
- **O teste falhando sem a trava:** cada caso de recusa roda também com aquela trava desligada (`sem={trava}`) e precisa mudar de resultado: o teste que não falha sem o conserto não prova o conserto.

## O que difere do CRM, por escolha

- A base validada fica como regra escrita, sem trava (q1c); no CRM, uma variável que o `ask` perguntava.
- O log cresce pelo fim, com `merge=union` (D3); no CRM, pelo topo.
- Sem quadro, sem rótulos de forma e sem Discussions (q4b, q7b, D12); as perguntas e as ideias vão ao "A decidir" da issue.
- Só HTML com SVG nos diagramas (q8b); o Mermaid volta só como saída gerada do JSON, para o ADR e o README (18/11). Os diagramas seguem o padrão de `assets/diagramas/` da skill, com a conferência por script.
- Na conta pessoal do GitHub, a prioridade e o defeito vão por rótulo, porque o Type e a Priority nativos são de organização. Numa organização, eles já existem e o `--conta org` os usa (o `references/projeto.md` da skill diz o que trocar).

## Os limites conhecidos

- O `deny` lê o comando como texto: as flags curtas depois de outra (`git commit -m x -n`) escapam, e o `deny` do `.env` não barra um `grep -r` na pasta.
- O log não confere a ordem das datas, só que a entrada nova vai no fim (no `pre-commit`, fora do merge): com o `merge=union`, duas branches juntam as entradas na ordem do merge.
- Sem Python 3.9 ou mais novo, as travas avisam e deixam passar; o CI confere de novo.
- O `Dockerfile`, o job `imagem` e o vigia não rodaram contra um daemon nem um registro de verdade na entrega: o build se prova no CI do primeiro projeto com `--docker`; a lógica do aviso do vigia tem testes sem rede.
- A regra de tag pede o GitHub Pro em repositório privado de conta pessoal: num teste de 18/11, a criação devolveu 403 ("Upgrade to GitHub Pro or make this repository public"). Por isso, na conta pessoal com o repositório privado, o kit nem tenta: a tag fica protegida pela regra escrita no `CLAUDE.md` do projeto. No repositório público ou na organização, o `github.py` tenta criá-la e, se o plano não a oferece, avisa e segue.

## O que vem depois

- O primeiro projeto de verdade, que confere o que o `licoes.md` da skill lista ("O que conferir no primeiro uso real").
- O teste às cegas dos diagramas (Claude contra Codex), proposto em `decisions/kit-de-projeto-novo.md`.
