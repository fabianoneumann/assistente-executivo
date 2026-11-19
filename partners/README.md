---
area: Parceiros e clientes
artefatos:
  - pasta: "*/proposals"
    tipo: proposta
  - pasta: "*/contracts"
    tipo: contrato
  - pasta: "*/reports"
    tipo: relatório
  - pasta: "*/deliveries"
    tipo: entrega
  - pasta: "*/workshops"
    tipo: workshop
---

# Parceiros e clientes

As empresas e as pessoas com quem você trabalha ou conversa sobre trabalho: um parceiro, um cliente, um prospect. Cada uma ganha uma pasta que acumula o que se levantou (quem é, o que quer, as dores) e os documentos que saíram (propostas, acordos, relatórios, entregas, reuniões).

> **Antes do primeiro parceiro, o repositório tem de ser privado.** O dossiê e os documentos guardam dado de terceiro (nomes, valores, condições comerciais). O `scripts/confere_dados.py` trata esta pasta como as de vida pessoal: com um arquivo aqui fora do modelo e o repositório público no GitHub, ele para com `[PARE]` e diz como deixá-lo privado. O modelo em branco (`partners/template/` e este README) passa. Porquê em [`decisions/parceiros-e-clientes.md`](../decisions/parceiros-e-clientes.md).

## Como abrir um parceiro

Copie do [`template/`](./template/README.md): crie `partners/<parceiro>/` (minúsculas, hífens, sem acento) com o dossiê do modelo renomeado para `<parceiro>-dossie.md`. Cada pasta de documento nasce com o primeiro documento dela, copiado do modelo daquela pasta. O README do modelo explica os marcadores, os nomes de arquivo, o PDF e onde fica a marca.

## O que cada pasta contém

- `<parceiro>-dossie.md`: o dossiê (contato e canais, o que a empresa é, o engajamento, os sistemas, as dores, os clientes em conjunto e as propostas).
- `proposals/`: **o que se vende**, `AAAA-MM-DD-<escopo>.html`.
- `contracts/`: **o que formaliza** um negócio fechado, no mesmo padrão de nome.
- `deliveries/`: **o que encerra**: a proposta comparada com o que foi feito.
- `reports/`: o acompanhamento recorrente, com o ritual no `README.md` de lá.
- `meetings/`: o que uma reunião produziu, `AAAA-MM-DD-<tema>.md`. A transcrição, quando guardada, vai a um `originals/` ao lado, fora do git.
- `workshops/`: o roteiro de um treinamento ou workshop.
- `clients/<cliente>/`: quando o parceiro é o canal e há um cliente final, o dossiê e o material de trabalho dele; a peça enviada continua no `proposals/` ou no `contracts/` do parceiro.

Separadas porque cada uma responde a uma pergunta diferente: vender o que ainda não existe, formalizar o que se fechou, mostrar o que foi feito.

## A marca

Os documentos HTML abrem com um bloco `:root` de tokens (cores, letras, largura). É o único lugar da marca: troque nos modelos de `template/`, uma vez, e todo documento novo nasce com a sua identidade. O padrão é um tema claro com Space Grotesk e JetBrains Mono.
