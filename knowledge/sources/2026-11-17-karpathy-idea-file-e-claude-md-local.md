---
titulo: "LLM Wiki (gist) e o .gitignore do nanochat"
tipo: artigo
autor: "Andrej Karpathy"
url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
publicado_em: 2026-04-04
capturado_em: 2026-11-17
areas: [anthropic-claude]
entrada: pesquisa
tags: [andrej-karpathy, llm-wiki, claude-md, agents-md, primary-source]
licenca: "O gist LLM Wiki não declara licença; o .gitignore do nanochat é MIT, escrita no arquivo LICENSE da raiz do repositório karpathy/nanochat (https://github.com/karpathy/nanochat/blob/master/LICENSE). Nenhum dos dois vem copiado: os dois entram em palavras próprias, e o original se lê nos links."
---

# O idea file do LLM Wiki e o CLAUDE.md local do nanochat, lidos em 17/11/2026

Ficha de estudo, em palavras próprias, de duas fontes primárias do Karpathy em inglês, lidas inteiras em 17/11/2026: o gist "LLM Wiki" (sem licença declarada; a data de 04/04/2026 é a da página do gist, registrada na rodada, e a cópia de trabalho não a traz) e o `.gitignore` do repositório nanochat (https://github.com/karpathy/nanochat/blob/master/.gitignore, último commit do arquivo 64a651a6, de 29/01/2026; repositório MIT). A ficha não resume o padrão do wiki, que a base já descreve: junta, por ideia e numa ordem própria, só o que o gist diz sobre como deve ser usado e passado adiante.

## Em uma frase

Para o Karpathy, o texto é semente e não manual: cada pessoa o entrega ao próprio agente e monta com ele a sua versão; e no repositório dele o `CLAUDE.md` fica fora do git, no bloco de configuração local, separado do dos segredos.

## O esquema se escreve usando

O autor conta como ingere fontes, uma por vez e acompanhando, admite o lote com menos supervisão e não fixa nenhum dos dois: cada um acha o próprio fluxo e o anota no arquivo de esquema, para as sessões seguintes. O esquema mesmo (o `CLAUDE.md` no Claude Code, o `AGENTS.md` no Codex) também não chega pronto: a pessoa e o modelo o vão acertando juntos, à medida que descobrem o que funciona no domínio dela.

## O que se divide com os outros e o que fica com cada um

O gist põe pouca coisa no lado comum. Do git, fala uma vez, entre as dicas de ferramenta: como o wiki não passa de arquivos markdown num repositório, versão, ramos e trabalho a várias mãos vêm de graça. Equipe aparece uma vez também, como um dos usos possíveis do wiki (uma base interna de empresa, alimentada por conversas, reuniões e documentos, que o LLM mantém em dia, talvez com revisão humana), e não como gente que recebe a configuração de alguém. O `.gitignore` do nanochat, de 13 linhas, vai no mesmo sentido: separa o que ignora num bloco sem título (ambiente virtual, caches do Python, um relatório e os dados de avaliação), num bloco de segredos, só com o `.env`, e num de configuração local, onde estão o `CLAUDE.md` e a pasta do wandb, a única menção ao `CLAUDE.md` no arquivo.

## Por que o texto não fixa nada

O documento se dá uma tarefa só, passar o padrão adiante, e deixa o resto ao agente a que o leitor o entrega (Codex, Claude Code e OpenCode / Pi são os exemplos), para os dois construírem juntos a versão que serve. Daí a lista do que fica em aberto: estrutura de pastas, convenções, formato de página e ferramentas variam com o domínio, o gosto e o modelo de cada um, e qualquer peça pode sair. A nota que fecha o gist diz que essa falta de detalhe é de propósito.

## O que a fonte recomenda

Não tratar o gist como receita: dá-lo ao próprio agente, ficar com o que serve e registrar no esquema o jeito de trabalhar, que muda com o uso.

## Citações

- "This is an idea file, it is designed to be copy pasted to your own LLM Agent"
- "This document is intentionally abstract. It describes the idea, not a specific implementation."
- "The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs."

## Lacuna

O gist não fala de distribuir o arquivo de esquema, as skills ou qualquer configuração a outras pessoas nem a uma equipe: equipe aparece só como contexto de uso do wiki e o git, como meio de colaboração no próprio wiki. O `.gitignore` não explica por que o `CLAUDE.md` fica fora do git, e o repositório não diz, nesse arquivo, o que o `CLAUDE.md` local contém.

**Conta lado a lado** (contra a cópia de trabalho do gist; as linhas são as dela): 7 de 11 unidades do corpo retomam uma passagem da fonte, sempre com construção própria: pela ordem da ficha, a ingestão (linha 39), o esquema (35), a dica do git (64), o uso em equipe (24) e a nota final em três frases, na ordem inversa da do gist (77 com 7; 77; 77). Outras 2, "Em uma frase" e "O que a fonte recomenda", juntam várias passagens (7, 35, 39 e 77) sem seguir nenhuma; a abertura da segunda seção é própria e a frase do `.gitignore` é de fatos (nomes de bloco e de arquivo). A sequência mais longa de unidades seguidas que anda para a frente na fonte tem duas (35 para 64, e 24 para 77). As citações, a proveniência, a "Lacuna" e esta linha ficam fora da conta. O `parafrase.py`, contra o gist, saiu com o código 3 (ficha em português, fonte em inglês): "coladas: 0 de 19 (0%); trechos de 3 ou mais seguidas: 0".
