# Contrato de saída dos scripts

Os caminhos sem `./` nem `../` (`scripts/...`, `references/...`) partem da pasta da skill.

Cada script de busca imprime este JSON no stdout (uniforme entre fornecedores, para você triangular e reconciliar):

```json
{
  "contract_version": "1",
  "provider": "perplexity | gemini | codex",
  "mode": "shallow | deep",
  "model": "sonar-pro",
  "query": "texto da busca",
  "answer": "resposta sintetizada/aterrada (se houver)",
  "results": [
    {"title": "...", "url": "...", "snippet": "...", "published": "AAAA-MM-DD|null", "source_type": "web"}
  ],
  "citations": ["url1", "url2"],
  "error": null
}
```

`answer` (aterrado) vem separado de `results` (fontes cruas) de propósito: use os dois. Se `error` não for nulo, houve falha de rede ou de API (ou, no Codex, a ferramenta não está instalada): trate e avise. O raso do Gemini acrescenta `endpoint` (`aistudio` ou `vertex`), e o profundo, `interaction_id`, para recuperar o relatório sem rodar de novo. O Codex deixa `results` vazio (ele não devolve a lista crua) e põe em `citations` as URLs que citou.

**Sem a chave,** o script não imprime JSON: sai com o código 1 e a mensagem `[PARE]` no stderr (a variável, para que serve, onde se pega e como se põe). A pesquisa não para por isso: a frente dele fica de fora, a rodada segue no modo só busca nativa (ou no reduzido, com a frente que tem chave) e diz isso à pessoa, com a mensagem (`modo-nativo.md`). Não tente o script de novo sem a chave.

**No limite de taxa (429),** o script do Perplexity tenta até três vezes, com espera crescente e variação aleatória (sem as tentativas internas do SDK, dentro de 90 s de espera no raso), e só então devolve o erro; o 429 de cota ou saldo volta na hora. Levas grandes em paralelo ainda podem esgotar as três; o que voltar com 429 depois das três tentativas roda de novo em sequência.
