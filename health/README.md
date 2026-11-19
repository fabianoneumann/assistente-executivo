# Saúde e bem-estar

> **Espaço sensível.** O que entra aqui é dado de saúde seu. Antes do primeiro registro, confira que o repositório é **privado**: o histórico do git guarda o que foi commitado mesmo depois de apagado. O assistente não diagnostica, não substitui médico, nutricionista, educador físico nem terapeuta, e sugere o profissional quando o assunto pede.

As subpastas, e nenhuma delas tem arquivo de registro antes do primeiro registro (o assistente cria o arquivo quando você relatar a primeira informação):

- [`training/`](./training/README.md): os treinos, por ciclo (o plano e o registro das sessões).
- [`nutrition/`](./nutrition/README.md): a alimentação, por ciclo (o plano, os objetivos e a adesão).
- [`medical/`](./medical/README.md): os exames e os laudos, um arquivo por exame.
- [`psychological/`](./psychological/README.md): as notas vivas e o diário.

## As quatro naturezas de arquivo

A forma de cada arquivo segue a natureza dele:

1. **Vivo:** atualizado no lugar, sem crescer sem fim. O plano de treino, os objetivos, as notas do psicológico.
2. **Registro de um ciclo:** cresce, mas só durante o ciclo, e arquiva junto com o plano que o gerou. O registro das sessões de treino, a adesão à dieta.
3. **Série contínua:** cresce sem ciclo natural e se divide pelo calendário. O diário, por trimestre.
4. **Registro datado imutável:** não se reescreve nem se arquiva; acumula por data e vale pela comparação com os anteriores. O exame.

## O padrão de ciclos (treino e alimentação)

O plano e o registro nascem e arquivam juntos, porque o registro só faz sentido lido com o plano que o gerou:

- **`current/`:** o ciclo em execução, e não o plano mais recente que se escreveu. Um plano só vai para `current/` quando começa a ser seguido.
- **`next/`** (opcional): o próximo ciclo em preparo, enquanto o atual ainda roda. Some quando é promovido.
- **`archive/AAAA-MM-DD-<descricao>/`:** os ciclos anteriores, cada um como pasta completa. A data é a do **início real**, a primeira sessão do registro, e não a do arquivamento.

**A virada tem ordem: arquivar o `current/` primeiro, promover o novo depois.** Ao contrário, o par plano e registro do ciclo que acabou se perde.

**Um nome de pessoa entra pelo papel.** O médico, o nutricionista, o professor e o familiar citados num registro entram como "a médica", "o nutricionista", "a irmã". O laudo em PDF, se você quiser guardar, vai para `originals/` ao lado do exame, fora do git.
