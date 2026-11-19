# Parceiros e clientes

## A pasta `partners/`, com o modelo em branco, só em repositório privado

**Decisão:** o repositório tem uma pasta `partners/` para os parceiros e os clientes de quem usa, com um modelo em branco (`partners/template/`): o dossiê e os esqueletos da proposta, do acordo, da entrega, do relatório semanal, da reunião, do workshop e do dossiê do cliente final, com marcadores no lugar do conteúdo e a marca num bloco de tokens no topo de cada HTML. O dado de um parceiro ou cliente real só entra com o repositório privado, e o `scripts/confere_dados.py` confere isso como confere as pastas de vida pessoal: arquivo de `partners/` fora do modelo, com um remoto público no GitHub, é `[PARE]`.

**Motivo:** quem usa o assistente para trabalho prepara propostas, relatórios e entregas para outras empresas, e o que funciona é ter a forma pronta (as seções, a ordem, o estilo, o ritual do relatório) e escrever só o conteúdo. A forma vem de documentos que já foram a clientes de verdade, sem nada deles. Mas o que se escreve ali é dado de terceiro: nome, valor, condição comercial. Antes desta pasta, a regra era que dado de cliente não entrava no repositório; com ela, entra só onde não fica público, e a conferência por script é o que impede o esquecimento, como já impede nas finanças e na saúde.

**Como aplicar:** o README de `partners/` e o do modelo dizem como abrir um parceiro e onde fica a marca. O `CLAUDE.md` traz o gatilho. A marca de cada pessoa ou equipe vai nos tokens dos modelos, trocados uma vez.

**Revê se:** alguém precisar guardar parceiros num repositório público (aí o caminho é outro repositório, privado, só para eles), ou se a conferência deixar passar um arquivo de parceiro.
