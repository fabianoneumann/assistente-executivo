# A versão e as dependências

Como se corta uma versão e como se trata a atualização de dependência. **Ler quando:** for cortar uma versão, ou quando chegar um PR do Dependabot.

## A versão é uma tag anotada no `{{BASE}}`

- **Instala-se a versão, nunca a branch.** A versão é a tag anotada `vX.Y.Z` num commit do `{{BASE}}`, cortada quando vai ser instalada. Não há branch de release: a correção vai na versão seguinte.
- **Quem corta é o agente, quando as portas passam:** o CI verde no commit, a bateria inteira (`{{CMD_E2E}}`) rodada nele, e as notas conferidas na prévia. A pessoa não precisa liberar a tag; ela lê as notas.
- **Uma versão não se move.** [kit:conta=org]A regra de tag do GitHub (ruleset `tags-imutaveis`, nas tags `v*`) recusa mover e apagar a tag. Criar segue livre. Sem a regra (o plano do GitHub não a oferece), vale esta linha: a tag publicada não se move nem se apaga; o erro se corrige com a versão seguinte.[kit:fim][kit:conta=user]A tag publicada não se move nem se apaga; o erro se corrige com a versão seguinte. É regra escrita, também no `CLAUDE.md`: na conta pessoal, o repositório privado não tem a regra de tag do GitHub sem o plano Pro.[kit:fim]
- **O E2E:** o smoke roda em todo PR (`{{CMD_SMOKE}}`), e a bateria inteira antes de cada versão. Os tetos de partida são de 3 minutos para o CI do PR e de 10 para a bateria; o que passar disso se revê antes de subir o teto.
- **O teste de tela espera a resposta antes de ler o dado.** O teste que confere no banco (ou em outra fonte) o efeito de uma ação na tela espera primeiro um sinal que só a resposta produz (a mensagem de sucesso, o item novo na lista); sem sinal na tela, a leitura se repete até um prazo, em vez de ler uma vez logo depois do clique. Ler antes de a gravação terminar dá o teste que falha às vezes, até rodando sozinho.

**O passo a passo:**

1. `git fetch` e conferir que o `{{BASE}}` local é o remoto.
2. `{{CMD_E2E}}`, inteira, em código 0.
3. `gh api repos/{{REPO}}/releases/generate-notes -f tag_name=vX.Y.Z --jq .body` para a prévia das notas (o `.github/release.yml` separa as mudanças das dependências).
4. `git tag -a vX.Y.Z -m "vX.Y.Z"` e `git push origin vX.Y.Z`.
5. `gh release create vX.Y.Z --generate-notes --verify-tag`.
6. Uma entrada `versao` no `knowledge/log.md`.

Um passo precisa estar no roteiro que se executa: o passo que mora só na memória de alguém para de acontecer de uma versão à outra.

## Os testes

- **Testar o modo de falha, e não a porcentagem.** A cobertura alta vai às superfícies de risco, com o teste negativo explícito (afirma o que não pode acontecer); o buraco clássico é o caminho feliz verde com a autorização quebrada.
- **A verificação de um artefato transformado roda antes da transformação.** Depois de empacotar, ofuscar ou compilar, a conferência pode dizer "limpo" sobre o que já não consegue ler.
- **O teste negativo entra pela mesma porta que o defeito real.** O teste que planta o problema direto no resultado prova uma trava que, pelo caminho de verdade, pode não funcionar; e confere-se que ele falha sem o conserto.
- **A verificação que mora no build precisa do build no CI,** senão é decoração.

## As dependências: o Dependabot só de segurança

- **Só as atualizações de segurança.** O `.github/dependabot.yml` tem `open-pull-requests-limit: 0`, que desliga as de versão; as de segurança não contam nesse limite. A opção "Dependabot security updates" do repositório precisa estar ligada (o kit a liga ao criar o repositório).
- **Um PR por pacote,** sem `groups`: uma triagem, um commit de squash.
- **O PR do Dependabot é uma trilha à parte:** nasce de um alerta, sem issue e sem modelo, e passa pelo mesmo CI.
- **A dependência compilada se prova rodando.** Na dependência que vem pronta para executar (uma imagem de contêiner, um binário de terceiro), o alerta de segurança só fecha com a versão nova, e a troca se prova rodando o que ela faz (o serviço sobe e responde, a ferramenta executa a tarefa dela), e não só com o build verde.
- **A triagem é pelo alcance,** e não pelo `dev` ou `runtime` do arquivo de dependências. A pergunta é "isto chega a quem usa?": o pacote que só roda na máquina de quem desenvolve ou no CI não é a mesma urgência que o que vai no artefato instalado. O resultado da triagem vai no corpo do PR, numa frase.
- **As armadilhas do PR do Dependabot:** o PR pode corrigir só parte das cópias do pacote no arquivo travado (conferir todas antes do merge); o rebase dele regera o PR, e o commit à mão em cima se perde; o alerta dispensado não reabre sozinho e o motivo não se edita depois (a triagem seguinte começa pelos dispensados "sem correção ainda").
- **A imagem base, se o projeto publica imagem.** O Dependabot não a vigia: no contêiner, ele só propõe versão, sem alerta de segurança. O projeto que publica imagem ganha uma vigilância à parte, com o próprio workflow semanal.
<!-- [kit:docker=sim] -->
  Aqui ela existe: `imagem-base.md`. O push da tag (o passo 4 do roteiro acima) também publica a imagem, pelo `publicar-imagem.yml`, e a versão só está pronta com ela no registro.
<!-- [kit:fim] -->
- **As ações do CI** são só as oficiais (`actions/*`), fixadas pelo hash do commit, com a versão no comentário; o Dependabot de segurança avisa quando uma delas tem alerta. Ação de terceiros não entra: o passo que precisaria dela vai como comando, que se lê no próprio `ci.yml`.
