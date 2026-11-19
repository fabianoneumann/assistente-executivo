---
titulo: "Data usage (Claude Code): treino, retenção, /feedback e pesquisa de satisfação"
tipo: artigo
autor: "Anthropic"
url: "https://code.claude.com/docs/en/data-usage.md"
capturado_em: 2026-10-30
licenca: "Documentação: todos os direitos reservados (texto da página Legal and compliance da documentação, registrado em 2026-10-29-claude-code-code-review-documentacao: '© Anthropic PBC. All rights reserved.'; a cópia em markdown lida não traz rodapé); entra só a ficha."
areas: [anthropic-claude]
tags: [claude-code, data-usage, model-training, feedback, privacy, retention]
---

Ficha de estudo, em palavras próprias, da página oficial de uso de dados do Claude Code, lida em markdown em 2026-10-30 (139 linhas). Lida, pela pergunta do que, das correções do usuário, sai da máquina e pode chegar ao modelo. Cobre a página inteira, na ordem dela.

## Treino

- **Contas de consumidor (Free, Pro e Max):** a pessoa escolhe se permite o uso dos dados para melhorar modelos futuros; com a opção ligada, a Anthropic treina modelos novos com os dados dessas contas, **inclusive o uso do Claude Code** a partir delas.
- **Contas comerciais (Team, Enterprise, API, plataformas de terceiros, Claude Gov):** a Anthropic não treina modelos generativos com código ou prompts enviados ao Claude Code nesses termos, salvo adesão do cliente (por exemplo o Development Partner Program, só na API própria da Anthropic, por decisão do administrador da organização).
- O ajuste da conta da curadoria não foi conferido.

## Retenção

- Consumidor com o treino ligado: 5 anos; desligado: 30 dias. Muda-se a qualquer momento nas configurações de privacidade do claude.ai.
- Comercial: 30 dias; retenção zero só para contas qualificadas no Enterprise, ligada pela equipe de conta.
- Na máquina: os transcritos de sessão ficam em texto puro em `~/.claude/projects/` por 30 dias por padrão (`cleanupPeriodDays`), para retomar sessões; os do Desktop e do Cowork ficam isentos por padrão.

## Feedback

- **`/feedback`** (e `/bug` e `/share`, que usam o mesmo caminho): o transcrito vai à Anthropic, e a doc diz que o retorno pode ser usado "to improve our products and services"; fica retido 5 anos. Na hora de enviar, escolhe-se quanto histórico vai junto (só a sessão atual, por padrão, ou também as do mesmo projeto nas últimas 24 horas ou 7 dias). Vai cifrado para o Google Cloud Storage e, opcionalmente, vira issue no repositório público. Com provedor de terceiros (Bedrock, Vertex, Foundry) ou sem credencial da Anthropic, o relatório fica num arquivo local em `~/.claude/feedback-bundles/`. Desliga-se com `DISABLE_FEEDBACK_COMMAND=1`.
- **Feedback redigido pelo Claude:** o Claude pode rascunhar um relatório e deixá-lo na fila da máquina para a pessoa revisar; nada sai até ela enviar, e o envio segue o mesmo caminho e retenção do `/feedback`.
- **Pesquisa "How is Claude doing this session?":** guarda só a nota, sem transcrito. Diferente do polegar para cima ou para baixo e do `/feedback`, é métrica de satisfação. Depois dela pode vir uma pergunta à parte, se a Anthropic pode ver o transcrito: "sim" envia o transcrito da conversa, dos subagentes e o log bruto (com chaves e tokens conhecidos mascarados; código e conteúdo vão como estão), retido até 6 meses; nada sai sem o "sim". Essas respostas, inclusive os transcritos enviados, **não podem ser usadas para treinar** os modelos e não mexem na preferência de treino. Desliga-se com `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1` ou com as variáveis gerais de telemetria; `feedbackSurveyRate` ajusta a frequência.

## Acesso aos dados e sessões apagáveis

As sessões na nuvem podem ser apagadas uma a uma, o que remove de vez os eventos delas. O Remote Control segue o fluxo local (tudo roda na máquina), mas, enquanto conectado, o transcrito também fica nos servidores da Anthropic para sincronizar entre dispositivos. Os detalhes de retenção remetem à Central de Privacidade e aos termos (de consumidor ou comerciais) e à política de privacidade.

## Fluxo local

O Claude Code roda na máquina e manda pela rede os prompts e as saídas do modelo, cifrados em trânsito (TLS 1.2 ou superior); funciona com a maioria das VPNs e proxies de modelo. O diagrama separa o obrigatório (instalação e atualização, autenticação e a API) do opcional ou disparado pela pessoa (métricas, relatórios de erro, o `/feedback`). A cifra em repouso depende do provedor: na API da Anthropic, cifra de disco AES-256 na infraestrutura (com retenção zero, nada persiste no servidor); no Bedrock, AES-256 com chaves da AWS ou do cliente; no Google Cloud, chaves do Google ou do cliente; no Foundry, depende da hospedagem (hospedado no Azure, prompts e respostas ficam no Azure e só metadados de uso e conteúdo sinalizado pela segurança saem para a Anthropic).

## Fluxo na nuvem

As sessões na nuvem rodam, por padrão, em máquinas virtuais da Anthropic (ou em infraestrutura própria, quando a organização usa ambiente auto-hospedado): o repositório é clonado na máquina isolada da sessão; a Anthropic guarda o transcrito para a pessoa voltar depois, sob as mesmas regras de retenção e uso da conta; as credenciais do GitHub ficam cifradas nos servidores e nunca entram na máquina (um proxy as acrescenta do lado do servidor); todo tráfego de saída passa por um proxy de segurança, para auditoria e contra abuso.

## Telemetria

Dois tipos, desligáveis um a um, ou tudo o que não é essencial de uma vez (`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`; desligar a telemetria assim também desliga a avaliação de flags, o que pode deixar o Remote Control indisponível):
- **Métricas:** latência, confiabilidade e padrões de uso, para a Anthropic e para infraestrutura de log de terceiros; nunca incluem código, prompts nem caminhos de arquivo (`DISABLE_TELEMETRY=1`).
- **Relatórios de erro:** mensagens e pilhas de erro do próprio Claude Code, para um serviço de terceiros, com segredos, caminhos, e-mails e outros dados pessoais conhecidos mascarados antes de sair (`DISABLE_ERROR_REPORTING=1`). Só ligados quando a pessoa entra com Pro ou Max, na versão 2.1.198 ou posterior, conectada direto à API do Claude, e sem acordo de retenção zero ou HIPAA.

## Padrão por provedor

Com Bedrock, Google Cloud, Foundry ou a plataforma na AWS, relatórios de erro, telemetria e o `/feedback` vêm desligados por padrão; a pesquisa de satisfação e a checagem de domínio do WebFetch rodam em qualquer provedor. Numa sessão pelo gateway de apps do Claude, a própria credencial desliga análise de uso, erros e notas da pesquisa. Quando a plataforma hospedeira declara que gerencia o provedor, as métricas passam a vir ligadas nesses provedores. Todas as variáveis podem ir para o `settings.json`.

## Checagem de domínio do WebFetch

Antes de buscar uma URL, o WebFetch manda só o nome do host (não a URL, o caminho nem o conteúdo) à API da Anthropic para conferir contra uma lista de bloqueio; o host aprovado fica em cache por cinco minutos. Roda com qualquer provedor e não é afetada pela variável que corta o tráfego não essencial; se a rede bloqueia a API da Anthropic, o WebFetch falha até liberar o domínio ou desligar a checagem (`skipWebFetchPreflight`), e, desligada, convém restringir os domínios por regras de permissão.
