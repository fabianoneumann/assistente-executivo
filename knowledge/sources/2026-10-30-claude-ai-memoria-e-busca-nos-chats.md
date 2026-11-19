---
titulo: "Use Claude's chat search and memory to build on previous context (Central de Ajuda do Claude)"
tipo: artigo
autor: "Anthropic"
url: "https://support.claude.com/en/articles/11817273"
capturado_em: 2026-10-30
licenca: "Central de Ajuda da Anthropic: sem licença aberta (nenhuma licença declarada na página lida); tratada como protegida; entra só a ficha."
areas: [anthropic-claude]
tags: [claude-ai, memory, chat-search, rag, privacy, projects, continual-learning]
---

Ficha de estudo, em palavras próprias, do artigo da Central de Ajuda sobre a busca nos chats e a memória do app Claude (web, desktop e celular), lido em 2026-10-30 (a página dizia só "atualizado esta semana"). É a memória que não fica na máquina: vale no claude.ai, não no Claude Code. Lido, por um achado da revisão (a primeira rodada de buscas só perguntou pelo Claude Code).

## Busca nos chats

- Planos Pro, Max, Team e Enterprise, na web, no desktop e no celular. O Claude busca nas conversas passadas por recuperação (RAG), e cada busca aparece como chamada de ferramenta no chat atual.
- Alcance: todos os chats fora de projetos; dentro de um projeto, só as conversas daquele projeto.
- Ligada por padrão quando chega à conta; desliga-se em Configurações, "Your Claude", "Search and reference chats".
- Quando o Claude se apoia num chat passado, cita com link para a conversa original.

## Chats anônimos (incognito)

Em todos os planos, pelo ícone de fantasma num chat novo fora de projeto: não vão para o histórico nem para a memória, e o Claude não os busca.

## Memória

- **Como nasce:** a partir dos chats, salva como **tópicos individuais durante as conversas**, não como resumo gerado depois que o chat termina. O Claude salva por conta própria, e a pessoa pode pedir "lembre disto".
- **Padrão:** ligada nos planos Free, Pro e Max; no Team e no Enterprise, o dono da organização habilita, e cada membro liga a sua. Compartilhada com o Cowork só quando ele roda na nuvem.
- **Por projeto:** cada projeto tem memória própria; dentro dele, o Claude usa a do projeto mais a memória geral, nunca a de outros projetos. Para isolar um projeto, desliga-se "Use account memory" na página dele.
- **Ver e editar:** em Configurações, "Your Claude", "Manage" ao lado de "Your memory", com a lista de tópicos para editar ou apagar; ou no chat, pedindo para lembrar, mudar ou esquecer, o que vale a partir da conversa seguinte.
- **Desligar:** na conta ("Memory from chats"; "Pause memory" mantém o que existe mas para de usar e criar; "Reset memory" apaga tudo, inclusive a dos projetos, de vez); num chat só, pelo "+", antes da primeira mensagem (não muda depois).
- **O que lembra:** papel, projetos e contexto profissional; pessoas e lugares do trabalho; estilo de comunicação e de trabalho; preferências técnicas e de código; detalhes de projetos em andamento. Temas sensíveis (saúde, política, religião, identidade de gênero) não são salvos por padrão, a não ser que a pessoa ligue a opção, e aí vêm com aviso para revisar. Nunca salvos, nem a pedido: números de documento, antecedentes criminais, números de conta financeira e situação migratória.
- **Importar e exportar** memória de e para outros assistentes: experimental.

## Retenção

A memória se atualiza enquanto se conversa. Apagar uma conversa **não** apaga os tópicos que vieram dela (apagam-se um a um). Entra na exportação de dados. Com retenção personalizada da organização, a memória (exceto a de projeto) segue o prazo, e o que não for atualizado nele some; a de projeto some com o projeto. O artigo não trata do uso dos chats ou da memória para treinar modelos.

## Organizações e versão antiga

Donos habilitam a memória nas capacidades da organização, sem ver nem editar a memória dos membros; desligá-la na organização apaga tudo de todos. Indisponível com acordos de HIPAA ou de setor público. Algumas organizações Team e Enterprise ainda usam a versão antiga, um resumo sintetizado a cada 24 horas mais resumos por projeto.

## Limites

Não vale nas sessões locais do Cowork; chats anônimos não contribuem; chave de cifra gerida pelo cliente bloqueia a busca; a configuração por chat trava na primeira mensagem; importar e exportar é experimental.
