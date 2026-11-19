---
titulo: "Os desenvolvedores da UE agora podem optar por treinar modelos de IA em seus projetos"
tipo: artigo
autor: "Epic Games"   # notícia no site da Unreal Engine, sem assinatura de pessoa no texto lido
url: "https://unrealengine.com/ue-devs-can-now-choose-to-train-ai-models-on-their-projects"
publicado_em: 2026-10-29   # data no topo do texto ("29 de outubro de 2026")
capturado_em: 2026-11-12
licenca: "protegido (notícia da Epic Games; sem licença de conteúdo declarada no texto lido); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [licensing, unreal-engine, eula, metahuman, ai-training-restriction, fab, noai]
---

# Epic, 29/10/2026: o EULA da Unreal deixa de vetar o treino de IA com a engine e com o MetaHuman

Nota de fato: tabelas do que o anúncio diz, juntadas por tema (o que deixa de ser vetado, quem fica com a versão nova e como, o que a mudança não alcança) e não na ordem da notícia, com cada resposta do FAQ no tema dela; prosa só para dizer o que a fonte é, o que ela afirma e o que falta. Não há integral: a notícia é protegida.

**Proveniência.** Notícia da Epic Games sobre o contrato da própria engine, na seção de notícias do site da Unreal, https://unrealengine.com/ue-devs-can-now-choose-to-train-ai-models-on-their-projects, lida pelo Chrome em 2026-11-12 (o curl dá 403 no domínio) e gravada em `.txt` a partir do `innerText`; o navegador a mostrou em português. sha256 (hash omitido), do texto gravado pelo Chrome; sem captura na Wayback. Título conferido no texto, logo abaixo da data. Formato: nota de fato de anúncio, porque o texto é curto (umas 500 palavras) e relata uma mudança de regra; reorganizada por tema em 2026-11-13, na revisão do Passo 7, porque a primeira versão seguia as seções da notícia e o FAQ na ordem dele. Cobertura: o texto inteiro (a abertura, "O que mudou no novo EULA", "Como aceitar o novo EULA" e as sete perguntas do FAQ). Não foram abertos a página de aceite do EULA, o EULA, as regras e os termos para desenvolvedores do Fortnite nem a página do Fab.

**Conferência lado a lado** (2026-11-13, pela régua do `README.md` desta pasta, item 2). Ficha e fonte em português, então a medida do `parafrase.py` contra o texto gravado pelo Chrome vale direto, com o cabeçalho da última saída: código 0, 29 unidades medidas (16 de prosa, 13 de célula com texto), 0 coladas e 0 trecho de 3 ou mais seguidas; fora da conta, 10 células de fato, 6 de cabeçalho e 4 frases curtas demais para medir. Pela conta lado a lado, 13 de 29 seguem uma frase da fonte, todas células: as duas restrições, o motivo, as três formas de aceite (contrato sob medida, usuário novo, usuário antigo) e as respostas do FAQ, cada uma dizendo de outro jeito o que uma frase da notícia diz; as duas perguntas do FAQ partidas em duas células (as três ferramentas do MetaHuman e o direito da Epic) contam duas vezes. A maior sequência na ordem da fonte é de 3, em dois lugares (o que o aceite permite seguido das três ferramentas do MetaHuman; o aceite do usuário novo e do antigo seguido das ilhas do Fortnite, já noutra tabela); a "Em uma frase" resume na ordem das seções da notícia (a 6e, a restrição da engine, a do MetaHuman, o usuário novo e o antigo), numa frase só, e a prosa de "O que a fonte afirma" e a da lacuna juntam lugares distantes da notícia, em outra ordem.

## Em uma frase

Anúncio da Epic, que licencia a engine e o MetaHuman: a seção 6e do EULA da Unreal perdeu os dois vetos ao treino de IA, o da engine com o código e o dos personagens e das curvas do MetaHuman; o usuário novo já recebe a versão sem eles, e quem já usa pode aceitá-la quando quiser.

## O que deixa de ser vetado

| Ponto | Fato |
|---|---|
| O que o licenciado passa a poder, se aceitar | pôr em treino de IA a engine, o código dela e o que produz com ela |
| As três ferramentas do MetaHuman (Creator, Animator, Mesh to MetaHuman) | o que sai delas também serve a treino de IA, já que o contrato da engine as cobre |
| Veto retirado, MetaHuman | usar os personagens e as curvas de animação, ou um render feito para imitar o que o MetaHuman faz, para montar ou ampliar base de dados ou para treinar e testar redes neurais e sistemas de IA, de *machine learning* e de aprendizado profundo |
| Veto retirado, engine | usar a engine e o código como material de treino de IA generativa, ou como entrada de prompt de que o programa aprenda |
| Lugar no contrato | seção 6e, a das Restrições gerais |
| Versões atingidas | todas as da engine |
| Motivo que a Epic dá | modelos de IA que entendam o conteúdo do desenvolvedor e o ajudem no trabalho |

## Quem fica com a versão nova, e como

| Quem | Como |
|---|---|
| Quem tem licença sob medida com a Epic | vale o próprio contrato; se houver nele veto parecido, o caminho é o representante da Epic |
| Usuário novo | recebe a versão nova, com o aceite pedido automaticamente |
| Quem já usa a engine ou o MetaHuman | aceita se e quando quiser, na página de aceite do EULA |

## O que a mudança não alcança

| Ponto | Fato |
|---|---|
| Ilhas do Fortnite | ficam de fora: o UEFN, o código em Verse e o conteúdo das ilhas seguem as regras e os termos de desenvolvedor do Fortnite |
| Conteúdo do Fab | sem mudança: o vendedor segue podendo usar a tag "NoAI" no que vende |
| Direito da Epic sobre o jogo, os assets ou o código do desenvolvedor | nenhum: a mudança só tira um veto que pesava sobre quem licencia a engine |

## O que a fonte afirma

A Epic diz que o MetaHuman, a engine e o código dela deixam de ter veto de uso em treino de IA, e que isso alcança as três ferramentas do MetaHuman por estarem sob o contrato da engine. Pelo texto, a Epic não ganha direito sobre o que o desenvolvedor faz, as ilhas do Fortnite ficam de fora e nada muda para os assets do Fab, onde o vendedor segue com a tag "NoAI"; a versão nova chega sozinha a quem começa agora e depende de aceite para quem já tinha licença.

## Citações

- "Excluímos duas restrições da Seção 6e (Restrições gerais) do EULA que se aplicam a todas as versões da Unreal Engine"
- "Se você já usa a Unreal Engine, pode optar por aceitar o novo EULA a qualquer momento"
- "Os vendedores ainda podem optar por permitir o treinamento de IA em seu conteúdo usando a tag "NoAI"."

## Lacuna

O anúncio não dá o texto das duas restrições como estavam no contrato, nem o número ou a data da versão nova do EULA, e não diz a partir de quando ela vale para quem aceita. Não diz se o aceite vale para projetos já feitos sob a versão antiga, nem o que acontece com quem não aceita e segue usando a engine. Sobre o Fab, a resposta diz que o vendedor pode "optar por permitir" o treino usando a tag "NoAI", sem explicar o que a tag faz, e o texto não remete ao contrato de conteúdo da Epic nem diz se ele mudou.
