# Médico

O histórico clínico: os exames, os laudos e o que está em acompanhamento. Um arquivo por exame, em `exams/AAAA-MM-DD-<exame>.md`, criado quando o primeiro exame chegar.

## O que entra num arquivo de exame

Três camadas, nesta ordem:

1. **Achados:** a leitura do laudo em palavras simples (o que foi encontrado e o que foi descartado). O laudo em PDF, se você quiser guardar, fica num `originals/` ao lado, fora do git; aqui mora a leitura, e não o documento.
2. **Correlação clínica:** o que você sente, desde quando e como evoluiu. O laudo não tem isso, e é o que o médico pergunta no retorno.
3. **Conduta:** o que foi decidido fazer (ou não fazer) a partir dali, e por quem.

**Um exame não se reescreve.** É registro datado imutável: vale pela comparação com o anterior. O exame novo é outro arquivo.

**O assistente lê, não diagnostica.** Ele explica termos e compara com o exame anterior; a interpretação clínica e a conduta são do profissional.

## O modelo

```markdown
# AAAA-MM-DD: <exame>

**Pedido por:** <o papel, por exemplo "a clínica geral">   **Laboratório ou clínica:** <opcional>

## Achados

## Correlação clínica

## Conduta
```

## Quando isto cresce

Com um acompanhamento só, a conduta vive no próprio arquivo do exame. Se passar a haver mais de uma condição em observação, ou exames de rotina recorrentes, aí nasce um arquivo vivo de acompanhamento (o estado atual e quando revisar), e os exames ficam com os achados e a correlação. **Não antecipar.**

## O roteiro do que preencher

Para cada exame, além do laudo: o que você sente e desde quando, o que mudou desde o último exame, os remédios em uso e o que o profissional disse na consulta.
