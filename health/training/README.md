# Treinos

Organização por **ciclo** (o padrão está em [`../README.md`](../README.md)). Os arquivos nascem no primeiro plano:

- `current/plan.md`: o plano vigente, com a divisão, os exercícios, as séries e repetições, as cargas-alvo e a progressão.
- `current/log.md`: uma entrada por sessão, com a data, o treino feito, as cargas, a intensidade (por exemplo, a percepção de esforço de 1 a 10), a duração e as observações.
- `archive/AAAA-MM-DD-<descricao>/`: os ciclos encerrados, com o `plan.md` e o `log.md` de cada um.

## O frontmatter do `plan.md`

```yaml
---
ciclo: <nome do ciclo>
inicio_planejado: AAAA-MM-DD   # a previsão feita quando o plano nasceu; não se corrige depois
semanas: <duração prevista>
formato: <circuito, full body, ABC...>
meta_semanal: <sessões por semana que o ciclo pede>
meta_minima: <o piso que a semana não deveria furar>
---
```

Todos os campos são opcionais: o que falta fica em branco, e quem lê não inventa. **O início real é a primeira sessão do `log.md`**, que já está registrada ali; copiá-la para o frontmatter criaria duas fontes para o mesmo fato.

**A meta é do ciclo, não do momento.** Um ciclo de retomada pede uma banda larga (por exemplo, alvo 4 e piso 2), porque o que está em jogo é o hábito; um ciclo de pico pede uma banda estreita. Como cada ciclo arquiva com o seu plano, o histórico guarda a meta que valia na época.

**Frequência e recência são coisas diferentes:** a `meta_semanal` diz quantos treinos nesta semana; os dias desde o último treino dizem outra coisa. Os dois podem discordar, e a discordância é informação.

## O encerramento

Ao arquivar, e só ao arquivar, o `plan.md` ganha dois campos:

```yaml
encerrado: AAAA-MM-DD   # o dia em que o ciclo foi fechado, não o do último treino
desfecho: concluido     # concluido | abandonado | interrompido
```

- **`concluido`:** rodou as semanas previstas.
- **`abandonado`:** parou aos poucos, sem decisão. O hábito não pegou: o que se olha depois é a frequência e o desenho da sessão.
- **`interrompido`:** parou por causa externa ou decisão (lesão, viagem, mudança de objetivo). O plano pode continuar bom.

## O roteiro do que preencher

Para o assistente montar o primeiro plano, conte: o objetivo do ciclo (força, hipertrofia, resistência, recomposição, retomar o hábito); quantos dias por semana e quanto tempo por sessão; onde treina e com que equipamento; limitações, dores ou lesões; o nível atual. Se há orientação de um profissional, ela vem antes da sugestão do assistente.
