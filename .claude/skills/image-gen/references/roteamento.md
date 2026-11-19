# O roteamento entre os dois geradores

Os dois geradores não se excluem: cada um faz o que mediu melhor, e onde os dois servem se gera nos dois. A tabela abaixo veio de comparações às cegas feitas antes deste projeto; por isso toda linha começa **provisória**, e a equipe a confirma ou a troca com as próprias escolhas (regra 4).

## A tabela de quem faz o quê

Cada linha só entra com a evidência ao lado. O estado de cada uma é **provisória** (menos de três escolhas no mesmo sentido, neste projeto) ou **fixa**.

| Tipo de pedido | Quem faz | Evidência | Estado |
|---|---|---|---|
| Texto dentro da imagem, tela de interface (mock) | Codex | numa comparação às cegas, foi o único sem texto inventado | provisória, 0 |
| Personagem em desenho ou animação | Nano Banana | segue melhor o desenho de referência | provisória, 0 |
| Personagem mais realista | Codex | segue melhor a foto de referência | provisória, 0 |
| Lápis de objeto | os dois | empate às cegas | provisória, 0 |
| Imagem larga em 4K, para mapa fatiado | Nano Banana | o Codex só entregou tamanhos fixos (1254 px quadrado, 1024 por 1536); a conferir | provisória, 0 |

## As regras

1. **Sem linha, ou com "os dois": gera nos dois.** As duas versões vão à parada da forma que a peça já tem, sem dizer quem fez e em ordem sorteada, e as duas entram no banco. Gerar nos dois e escolher é a votação entre alternativas; a ordem sorteada e o rótulo escondido protegem a escolha do viés de posição e de marca.
2. **A conferência por máquina vem antes da pessoa:** o `scripts/confere_imagem.py` (proporção, centro visual e, quando o pedido não tem texto, o texto inventado pelo Jev, opcional e em teste).
3. **A linhagem em toda imagem:** o gerador, a versão (no Codex, a do CLI e o `gpt-image-2`), a data, o tempo e o custo, no `.json` ao lado, no `prompts.md` da peça e no banco (a coluna Gerador do índice). Quando a versão do gerador muda, as linhas dele passam a "a reconferir" até a próxima escolha.
4. **Uma linha se fixa com três escolhas no mesmo sentido** de quem decide a forma das peças; daí em diante, só aquele gerador naquele tipo, e a escolha não se pergunta mais. Três repetições separam a preferência do acaso de uma rodada. Cada escolha se anota abaixo, com a data e a peça.
5. **O redesenho por outro gerador** (a folha de um refeita pelo outro) não é padrão: costuma trocar o acabamento, e não o estilo. Fica como recurso que a peça pede.

## O braço do Codex

Pela skill oficial `imagegen` do Codex (`openai/codex`, `codex-rs/skills/src/assets/samples/imagegen/`):
- **o prompt rotulado:** cenário, assunto, detalhes, restrições e intenção de saída; o texto que deve aparecer vai entre aspas, e a palavra rara, letra a letra;
- **as referências pelo papel** ("Imagem 1: referência de estilo"), sem supor que toda imagem dada é para editar; o `codex_imagem.py` monta isso a partir de `--papel-refs`;
- **na edição:** "mude só X; mantenha Y", repetindo o que não muda, uma mudança por volta;
- **o fundo transparente** se pede à ferramenta (`--fundo-transparente`). Ainda não foi comparado ao `so_traco.py`, que tira o papel por conta própria: quando os dois rodarem na mesma imagem, anote qual recortou melhor.

## As escolhas registradas

| Data | Peça | Tipo | Escolha | Linha |
|---|---|---|---|---|
