# Revisão (skill `review`)

Os caminhos sem `./` nem `../` (`scripts/...`, `references/...`) partem da pasta da skill.

- **Ponto de pausa:** no fim do Passo 5, antes de apresentar os achados e a lista de fontes a quem pediu; e de novo no Passo 7, com a síntese escrita, antes de pedir a validação.
- **Nível:** padrão; a ingestão em lote pode ir no modo por amostra (`review`, "Níveis"). Em fila ou loop, cada item chama esta skill pela ferramenta Skill, e o pedido do loop diz o nível da revisão de cada item ou declara que ela roda uma vez, sobre o bloco, antes do PR (`references/conferencias.md`).
- **Lentes:** régua (sempre) + fidelidade, fonte, busca, o que contraria ou falta, além da evidência, conteúdo próprio quando a ficha é de obra protegida, e números quando a síntese faz conta nossa (catálogo em `../../review/references/lentes.md`).
- **Conferir contra:** as fontes abertas no Passo 5 (ou os arquivos em `knowledge/sources/`), a base, `knowledge/README.md` e `knowledge/sources/README.md`.
- **Itens que de fato se esquecem aqui:**
  - cada número com a fonte, o ano e a condição em que foi medido;
  - primária ou resumo de terceiro, e a licença anotada;
  - a base consultada por várias formas da pergunta, com os termos do assunto vizinho, antes de "nada registrado";
  - número lido de gráfico marcado com "cerca de";
  - contradições entre fontes reconciliadas ou marcadas;
  - conteúdo sem citação marcado como não verificado, com quem afirma, e no rascunho o que ficou sem leva;
  - a variação em português e a variação por produto (Passo 2.5), e a saída da busca nativa no `qN-nativa.md`;
  - leitura do assistente com a marca;
  - a triagem rotulada no `rotulos.json` da rodada, com os valores da tabela de `references/rotulos.md`; e `scripts/confere_rodada.py` rodado sobre a pasta da rodada, com o que ele apontou resolvido ou explicado (`references/conferencias.md`, "Conferências automáticas").

**Antes de chamar a revisão,** quem fez o trabalho confere o rascunho contra esta lista, item por item, e corrige o que faltar; a revisão roda igual depois. Por quê: as regras desta skill reincidem juntas na mesma pesquisa, e sem a passada prévia só a revisão as pega; a lista também não substitui a revisão, porque quem a passa confia no próprio rascunho.

Os achados confirmados vão junto com o que se apresenta no fim do Passo 5. Com delegação de quem pediu, as correções de fato, de régua e de código entram no rascunho antes dessa entrega, ditas nela com o arquivo dos achados, e as que reescrevem trechos passam pela re-revisão antes dela; o que muda uma conclusão, uma regra ou o destino de uma fonte, ou reescreve texto que a pessoa já curou, espera a decisão dela (`review`, Etapa 3). O Passo 7 começa em seguida, com as correções que já entraram e sem as que esperam decisão, e a revisão do Passo 7, que leva os achados do Passo 5, cobre o que entrou na síntese. A correção aprovada, ou a fonte das exceções do Passo 6 aceita, depois dessa revisão entra antes do commit e, se reescreve trecho ou acrescenta ficha, passa por uma re-revisão antes dele: a aprovação conta como o pedido dessa rodada (`review`, "Re-revisão").
