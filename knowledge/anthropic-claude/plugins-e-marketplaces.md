# Plugins e marketplaces do Claude Code: como se distribui um conjunto de skills

O que a documentação oficial do Claude Code diz sobre empacotar skills num plugin e distribuí-lo por um marketplace: o que o plugin leva, como a equipe instala, as versões, os caminhos e as limitações. O uso numa equipe, com quem não programa, está em [`distribuir-o-ambiente-a-uma-equipe.md`](distribuir-o-ambiente-a-uma-equipe.md).

Páginas lidas: code.claude.com/docs/en/plugins, /plugin-marketplaces, /plugins-reference, /plugins/install, /plugins/loading, /plugins/host-marketplace, /plugins/relevance, /plugins/org, /plugins/create e a marketplace-reference (settings-reference só em parte); as quatro últimas estão fichadas em *Documentação do Claude Code: plugins na organização, carregamento, criação e referência do marketplace (leitura de 2026-11-17)*, de Anthropic (documentação do Claude Code) (https://code.claude.com/docs/en/plugins/org). Não lidas: components e troubleshooting. A documentação muda rápido: reler antes de decidir.

- **O que o plugin empacota:** skills, agentes, hooks, MCP, scripts. O manifesto, opcional, fica em `.claude-plugin/plugin.json`, e só o `name` é obrigatório. As skills ganham o prefixo do plugin (`/plugin:skill`). Um `CLAUDE.md` na raiz do plugin não é carregado.
- **O marketplace privado:** um repositório git com `.claude-plugin/marketplace.json`, instalado com `claude plugin marketplace add` e `claude plugin install nome@marketplace --scope project`.
  - O `enabledPlugins` e o `extraKnownMarketplaces` no `.claude/settings.json` do projeto ativam o plugin, mas cada pessoa ainda instala (`--scope project`), e o marketplace só se registra depois da confiança da pasta. A exceção: um marketplace local (`directory` ou `file`) com fonte relativa dispensa a instalação.
  - Sem marketplace: uma pasta com `.claude-plugin/plugin.json` dentro do `.claude/skills/` do projeto carrega como plugin (`@skills-dir`) depois da confiança, sem instalar.
  - Exigir a instalação em todas as máquinas só pelas managed settings do administrador.
- **Os caminhos:** `${CLAUDE_PLUGIN_ROOT}` aponta para a versão instalada, onde não se grava estado; `${CLAUDE_PLUGIN_DATA}` persiste entre versões; `${CLAUDE_PROJECT_DIR}` aponta para a raiz do projeto.
  - As três se resolvem no corpo das skills, mas não no Bash que o Claude roda.
  - Ler o `references/projeto.md` do repositório que usa o plugin é inferência, não documentado: está por testar.
- **As versões:** com `version` no manifesto, a versão fica fixa até mudar; sem ele, cada commit é uma versão nova.
  - Em marketplace de terceiro, a atualização automática vem desligada; atualiza-se com `claude plugin update`.
- **As limitações:**
  - o nome do plugin não pode começar com `claude-` nem `anthropic-`;
  - sessões na nuvem (claude.ai/code) não adicionam os marketplaces do repositório nem instalam os plugins que o `settings.json` dele declara;
  - o nome e a descrição de cada skill ativa entram no contexto a todo turno.
- **Sem plugin** (copiar `.claude/skills/` para o repositório): sem instalação e versionado com o commit, mas sem canal de atualização e com cópias que divergem. Serve para um repositório só.

**Vizinha:** [`complementos-do-claude-code.md`](complementos-do-claude-code.md), sobre o que ligar de plugin e de skill de terceiro.
