<!-- O fluxo por issue e o porquê de cada passo: knowledge/processo.md. Aqui fica o que se confere ao abrir.
     Os comentários são instrução: apagar todos antes de abrir; o hook do agente recusa o corpo que ainda os tem.
     Trocar "Closes" por "Refs" quando a entrega não encerra a issue (uma etapa, um follow-up de issue fechada), e dizer na linha seguinte o que ainda falta. PR sem issue própria (ferramental, documentação): apagar a linha. -->

Closes #

## O que muda

<!-- Uma frase. O detalhe está na issue. -->

## Antes de abrir este PR

- [ ] **Discussão inicial** feita, com as dúvidas fechadas antes do plano
- [ ] **Plano aceito** antes de implementar
- [ ] **`/code-review`** rodado sobre a branch, e os achados confirmados corrigidos
- [ ] **Validação da entrega** contra o "Pronto quando" da issue
- [ ] **Validação exploratória** feita, com o resultado abaixo
- [ ] **Branch sincronizada** com o `{{BASE}}` (`git merge origin/{{BASE}}`) depois do último commit
- [ ] **Base corrigida**, se a entrega contrariou o que ela afirma
- [ ] Linha no **`knowledge/log.md`**, se a entrega produziu conhecimento

> O item que não se aplica se marca com **N/A** (`- [x] N/A: ...`). A caixa em branco quer dizer "não feito", e não "não se aplicava".

## Validação exploratória

<!-- O "Pronto quando" como roteiro, contra o sistema rodando. Separar o achado de ambiente do defeito do sistema. -->

## Divergências

<!-- O que saiu diferente da spec, e por quê. Se a spec mudou, editar o corpo da issue. -->
