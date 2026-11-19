# Finanças

> **Espaço sensível.** O que entra aqui é dado pessoal seu. Antes do primeiro registro, confira que o repositório é **privado** (Settings > General > Danger Zone > Change visibility, no GitHub): o histórico do git guarda o que foi commitado mesmo depois de apagado. Depois, o `scripts/confere_dados.py`, rodado antes do push e com o `gh` logado, para quando acha registro pessoal num repositório com remoto público.

As finanças se dividem **por natureza**, e não por assunto:

- [`personal/`](./personal/README.md): as finanças pessoais (o que entra e sai da pessoa física).
- `business/`: as finanças do negócio. **Não existe até o negócio faturar como empresa.** Enquanto toda receita de trabalho cai na pessoa física, ela é finança pessoal. Quando a empresa faturar, a pasta nasce no primeiro registro, espelhando o padrão de `personal/` (os arquivos vivos e o registro mensal), organizada por fonte de receita; o que passa da empresa para a pessoa entra em `personal/` pelo valor líquido.

**Número só aqui.** Os projetos, os clientes e os parceiros descritos em outras pastas não levam valores: o elo é pelo nome. O registro em `finance/` diz de que projeto ou cliente veio a receita (a empresa cliente pelo nome; o cliente pessoa física pelo papel, como "cliente da consultoria"); o arquivo do projeto não repete o valor, e o dado do cliente (contrato, contato) não entra.

**Os papéis no lugar dos nomes.** Quem paga, recebe ou divide uma conta com você (familiares, amigos, quem manda um Pix) entra pelo papel ("Mãe", "Sócio", "Inquilino"), e não pelo nome. O extrato, a fatura e o comprovante, se você quiser guardar, vão para uma pasta `originals/` ao lado do registro, que o `.gitignore` tira do git.

**O que o assistente faz aqui:** lança o que você relatar, confere se a abertura e o fechamento batem, e aponta o que não fecha. A leitura dele (por exemplo, "a fatura deste mês parece maior que a média") fica na conversa, e não vira registro, até você confirmar.
