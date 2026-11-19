# Índice da base de conhecimento

Porta de entrada para o agente: **ler antes de consultar ou ingerir**, escolher a área (ou as áreas) e abrir o `index.md` dela, que diz quando ler cada página e com que termos ela é procurada. Na ingestão, a página nova entra no índice da área; área nova ou que mudou o que cobre entra aqui.

Convenções e rituais em [`README.md`](./README.md). Fontes brutas em [`sources/`](./sources/README.md). Rodadas de pesquisa em [`research-rounds/`](./research-rounds/README.md). Linha do tempo em [`log.md`](./log.md).

## Áreas

| Área | Ler quando | Termos-chave |
|---|---|---|
| [`content-design/`](./content-design/index.md) | Ao produzir, revisar ou avaliar carrossel, Stories, Reels ou imagem: tamanho e layout, área segura, gancho e texto, evidência de desempenho; testar a compreensão com leitores e escrever em linguagem simples; contar uma história, também com dados; antes de roteirizar um vídeo curto: o tempo de leitura de cada frase, a metáfora visual contra a demonstração literal, a fala escrita para o ouvido | safe zone, carrossel, Stories, gancho, proximidade, quebra de linha, detalhes sedutores, sinalização, nostalgia, ativo distintivo, teste com leitores, linguagem simples, caracteres por segundo, legenda, metáfora visual, escrever para o ouvido |
| [`agent-engineering/`](./agent-engineering/index.md) | Ao desenhar ou avaliar uma rubrica, um juiz por modelo, um portão ou um laço de avaliação; orquestração de skills e agentes; revisão por agentes e bajulação; lições e aprendizado contínuo de agentes; camadas de avaliação em série ou em paralelo e a pessoa depois da máquina; vieses do juiz e o juiz de visão julgando design; detecção de defeito raro, defeitos no lugar da nota, quem lê a saída do avaliador; gabarito na dúvida, gravidade, calibração, ponto de corte e validade de conteúdo | rubrica, veredito, juiz, LLM-as-a-judge, self-refine, Reflexion, avaliador-otimizador, painel de críticos, bajulação, sycophancy, lições aprendidas, ExpeL, cascata, viés de automação, viés de posição, autopreferência, reward hacking, prevalência, MQM, fadiga de alarme, gabarito, adjudicação, item plantado, gravidade, calibração, kappa, validade de conteúdo, viés de espectro, holdout |
| [`sales-and-offers/`](./sales-and-offers/index.md) | Ao decidir oferta, preço, tráfego, venda na conversa, lançamento ou prospecção | ticket, order bump, upsell, downsell, CPA, perpétuo, lançamento, SPIN, inbox, prospecção |
| [`psychology/`](./psychology/index.md) | Conteúdo com lastro em pesquisa de psicologia: a neurociência citada para defender histórias; as palavras que aproximam ou afastam quem lê, e o neuromarketing | oxitocina, acoplamento neural, storytelling, pronome, calor e competência, neuromarketing |
| [`generative-media/`](./generative-media/index.md) | Vídeo, som ou criativo feito ou editado por máquina: modelos de vídeo por API, vídeo em código, motion design (tempo, easing, transição), desenho de som e mixagem da voz, câmera virtual, cena em 2,5D ou 3D, personagem consistente entre imagens e planos, criativo de anúncio | Kling, Veo, Seedance, image-to-video, Remotion, HyperFrames, easing, doze princípios, match cut, trilha, efeito sonoro, ducking, paralaxe, multiplano, personagem consistente, Blender, Three.js, dolly, tempo de plano, 9:16 |
| [`journalism/`](./journalism/index.md) | Método de apuração e de fechar o ângulo de uma pauta (a skill `story-angle` abre a página direto); avaliar fonte, triar e parar uma busca (skill `research`); quem decide na checagem | hipótese, Story-Based Inquiry, ângulo, pauta, fonte, SIFT, CRAAP, PRISMA, snowballing, saturação, regra de parada |
| [`anthropic-claude/`](./anthropic-claude/index.md) | Como o Claude Code funciona no uso do ambiente: trabalho sem supervisão, ferramentas de terceiros e a assinatura, níveis de esforço, o que o Claude aprende entre sessões, o modelo no design e na leitura de imagem; antes de ligar plugin, skill de terceiro ou conector MCP; ao distribuir o ambiente a uma equipe e a quem não programa | headless, assinatura, OAuth, terceiros, /effort, memória, CLAUDE.md, plugin, marketplace, MCP, complementos, distribuir à equipe, Cowork |
| [`data-analysis/`](./data-analysis/index.md) | Antes de escrever uma leitura de métricas, comparar períodos ou peças, levar um número de pesquisa a um texto, ou definir uma métrica ou um relatório recorrente: armadilhas, cautelas de estatística, conferência e veredito | período parcial, denominador, média de médias, fuso, ausente não é zero, média e mediana, amostra pequena, comparações múltiplas, tamanho do efeito, outlier, definição de métrica |
| [`software-engineering/`](./software-engineering/index.md) | Ao planejar ou começar um sistema de software: o processo de issues e de PR, as travas em código (hooks, CI), os ADRs, a versão e as dependências; ao criar um projeto novo pela skill `project-kit` ou explicar de onde veio uma regra do processo dele | issue como spec, ADR, travas, hook, CI, Dependabot, versão, tag, Eisenhower, Type, Priority, LLM Wiki, kit de projeto, project-kit, onboarding |

## Temas que atravessam áreas

Quando a pergunta é de um destes temas, abrir o índice de todas as áreas indicadas.

- **Laços de avaliação, juiz e portão:** o método em `agent-engineering/`; as réguas em si ficam fora da base, em `marketing/social-media/` (rubricas e portão).
- **Direct e relacionamento:** responder e devolver em `content-design/`; vender em `sales-and-offers/`.
- **Imagem e vídeo:** imagem e roteiro curto em `content-design/`; vídeo gerado ou em código, movimento e som em `generative-media/`.
- **Números e métricas:** ler e conferir o número em `data-analysis/`; contar a história com o dado em `content-design/`; amostra, limiar e concordância ao medir um avaliador em `agent-engineering/`; a fonte de um número e os problemas dos próprios dados como pauta em `journalism/`; a regra "ausente não é zero" fora da base, em `decisions/dado-de-fora.md`.
- **Pesquisa e fonte:** avaliar fonte e parar a busca em `journalism/`; a régua do que é de terceiro em `sources/README.md`; a revisão da pesquisa por agentes em `agent-engineering/`.

## Formato do índice de área

Uma linha por página: `| \`<área>/<página>.md\` | Ler quando | Termos-chave | Fontes |`. "Ler quando" diz a situação de uso e, se houver vizinha que confunde, a diferença; termos-chave em português e em inglês, com nomes próprios e sinônimos; fontes como `N fichas + M citações`. Em torno de 250 caracteres entre "ler quando" e termos, até cerca de 350 quando aponta vizinha.
