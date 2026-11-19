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

## A extração barata de PDF longo (`extrai_pdf.py`)

O PDF longo (livro, manual, revista escaneada) não se transcreve página a página: o script tira o texto de cada página, com `<!-- página N -->` e, com `--numerar`, a linha dentro da página, e marca só as páginas que pedem olho: sem camada de texto, imagem (na página escaneada com OCR, a que tem pouco texto, onde sobra figura ou tabela), tabela (a grade desenhada ou, sem ela, muitos números e fragmentos), texto estranho (caractere sem mapa, OCR com poucas palavras de verdade, hífen em fim de linha), colunas trocadas e a página que uma ficha cita. Só as marcadas viram imagem (`--dpi`, padrão 200; uma tabela miúda de revista escaneada pediu 400), e quem confere lê essas imagens contra o texto da página; o `.pontos.md` lista o que conferir, e o `.pontos.json` traz as medidas e o custo. Sai com código 1 quando há página marcada, que é o caso normal (há o que conferir, não é falha), e 2 em erro.

**Como rodar, sobre material baixado:** com `-I` (CLAUDE.md), pelo python de uma venv que tenha o PyMuPDF, porque o `-I` ignora o site do usuário, onde ele costuma estar: `<venv>/Scripts/python.exe -I -X utf8 .claude/skills/research/scripts/extrai_pdf.py <arquivo.pdf> --saida <o originals/ ao lado do que usa> --numerar [--citadas 3,15] [--fichas <fichas>]` (no macOS e no Linux, `<venv>/bin/python`; a venv se cria com `python -m venv <venv>` e `<venv>/Scripts/python.exe -m pip install pymupdf`). Sem o PyMuPDF, o `--motor auto` para com código 2 em vez de cair calado no `pdftotext`; com `--aceitar-pdftotext` ele segue, e o `.pontos.md` diz no topo que a lista não vale como conferência, porque o `pdftotext` dá o texto e as marcas que saem dele (`sem_texto`, a tabela pelos números, `estranho`, `colunas`), sem `imagem`, a tabela achada pelo PyMuPDF, a grade desenhada nem o render.

**Onde a saída fica:** o texto de obra protegida é cópia de trabalho, fora do git (`knowledge/sources/README.md`, "A cópia de trabalho"): na rodada, `knowledge/research-rounds/<rodada>/originals/`; no material curado fora de rodada, `knowledge/sources/originals/`, com o nome da ficha.

**A citação:** a "l. L" do `.md` é da extração (muda com o motor e a ordenação) e serve para achar o trecho no texto; não se acha no original. A ficha cita a página do PDF, "PDF p. N", como manda o ritual de ficha.

**A medida de custo e de marcas** (motor PyMuPDF): uma revista de 184 páginas escaneadas com OCR deu 73 páginas a conferir, em 32 s de extração e 20 s de render; um manual de 96 páginas, 32 em 4,5 s; um livro digital de 15 páginas, 1 em 2,7 s; um de 638 páginas, 29 em 130 s, quase todo na busca de tabela (`--sem-tabela` a pula). O teste sem rede é o `scripts/teste_extrai_pdf.py` (rodado pelo python da venv; sem o PyMuPDF, ele roda só os casos que não geram PDF).

**Ainda em teste:** a medida acima é de custo e de marcas, não de precisão. Até uma medida contra uma transcrição conferida à mão, o número ou a citação que vai a uma ficha se confere na imagem da página, marcada ou não (`--citadas` ou `--fichas` a marcam, e `--render-citadas` a renderiza).
