# O modo só busca nativa

O modo em que a `research` roda desde o clone, sem a `PERPLEXITY_API_KEY` e a `GEMINI_API_KEY`. O Passo 0 diz quando ele vale (o `scripts/confere_ambiente.py --skill research` sai com 0 e o `[AVISO]`); aqui está o que muda na rodada. Com as chaves, nada disto se aplica: o modo nativo é o fallback, não substitui as frentes por API.

## O que roda

- **O raso** vai só pela ferramenta `WebSearch` da sessão (carregar o schema por `ToolSearch` se estiver adiada). Os scripts do Perplexity, do Gemini e do Codex não se chamam: sem a chave, eles param com `[PARE]` (`references/scripts.md`), e o Codex, mesmo instalado, fica de fora para a rodada ser a mesma em qualquer máquina sem chave.
- **Mais variações de query, desde a primeira leva**, porque um índice só acha menos: a pergunta curta com os termos exatos, a variação em português quando o público é brasileiro, uma por produto ou versão nomeado, uma com o ano explícito e uma com o termo de domínio ou de relatório (Passo 2.5). A regra de parada vale igual: 2 ou 3 reformulações batendo em fonte fraca é o sinal de lacuna.
- **A verificação** vai pelo `WebFetch` para triar e pela leitura da primária no texto bruto (curl e extração, ou o Chrome) para o que vira ficha ou sustenta um "a fonte não diz", como no Passo 5. As regras de verificação na primária valem iguais: a busca nativa é secundária, e o resumo dela erra como o de qualquer frente.
- **O profundo não existe neste modo.** Quando o tema pediria o profundo (amplo, técnico ou contestado, ou a regra de parada apontando para ele), diga isso à pessoa e ofereça configurar as chaves (o README da skill e o `.env.example`); até lá, a lacuna fica registrada como lacuna.
- **Com uma só das duas chaves**, o `confere_ambiente.py` diz "modo reduzido": roda a frente que tem chave, junto com a nativa, e o profundo só pelo motor dela.

## O que se registra

A triangulação é menor (um índice só, com o viés de fontes em inglês e dos Estados Unidos que a busca nativa tem), e quem lê a síntese depois precisa saber disso para pesar a cobertura.

- **No rótulo da rodada:** a `nota` do `rotulos.json` começa com "modo só busca nativa" (ou "modo reduzido, sem <frente>"), e as consultas levam `frente: nativa`. As saídas ficam nos `qN-nativa.md` da pasta da rodada, como no Passo 2; o `scripts/confere_rodada.py` lê a rodada só com elas.
- **Na síntese:** a seção das fontes diz "modo só busca nativa (sem Perplexity e Gemini): triangulação menor" e o que isso deixou de fora (o profundo não rodou; a lacuna que a regra de parada apontou).
- **Na apresentação dos achados** (Passo 5), a mesma linha no topo, para a pessoa decidir se vale rodar de novo com as chaves.

Uma rodada no modo nativo complementada depois com as chaves é rodada nova, em pasta nova, que diz na `nota` de qual é complemento (`references/rotulos.md`).
