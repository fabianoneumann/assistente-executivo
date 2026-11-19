---
titulo: "validate-data: conferir uma análise antes de compartilhar (skill do plugin data da Anthropic, versão 1.1.0)"
tipo: instrumento
autor: "Anthropic"
publicado_em: 2026-09-29   # data de atualização do plugin no manifest.json da cópia local; a skill não traz data própria
capturado_em: 2026-11-10
licenca: "Apache 2.0 (arquivo LICENSE na raiz da pasta do plugin data: o texto padrão da licença, versão 2.0, de janeiro de 2004; a linha de copyright do apêndice está no modelo, 'Copyright [yyyy] [name of copyright owner]', e a pasta não tem arquivo NOTICE; o autor declarado em .claude-plugin/plugin.json é Anthropic). Texto da licença: http://www.apache.org/licenses/LICENSE-2.0"
areas: [data-analysis]
tags: [data-validation, analytical-pitfalls, sanity-check, metrics, reporting]
---

# validate-data: a conferência de uma análise antes de ela sair

Ficha de estudo, em palavras próprias, da skill `validate-data` do plugin **data** da Anthropic (versão 1.1.0), sem o texto integral, que está no próprio plugin.

**Proveniência.** Não há url: o plugin veio sincronizado da conta do claude.ai (catálogo `anthropic-plugin-directory`) e foi desligado em 2026-11-10. O arquivo lido é `skills/validate-data/SKILL.md` (383 linhas) numa cópia local feita naquele dia. Os números de linha citados abaixo são os dessa cópia.

**O que a fonte é e o que não é.** É uma instrução escrita para um assistente revisar a análise de alguém antes de ela chegar a quem decide. Não cita estudo, autor nem medição: as regras valem como prática de ofício organizada, e os números soltos que ela traz não têm lastro (seção no fim desta ficha).

## O percurso da revisão (linhas 26 a 95)

Oito passos, nesta ordem: rever o método e as premissas (a pergunta é a certa? a população está bem definida, sem exclusão sem querer? as métricas estão definidas do jeito que quem lê entende? a comparação é justa em período, tamanho e contexto?); passar a lista de conferência; procurar as armadilhas conhecidas; refazer contas por amostragem (recalcular alguns números por conta própria, ver se os subtotais fecham com o total, se as porcentagens somam perto de 100% onde deviam, se a comparação com o período anterior usa a base certa, se os filtros são os mesmos em todas as métricas); olhar os gráficos; ver se a conclusão se sustenta no dado mostrado, se as explicações alternativas foram ditas e se a confiança declarada acompanha a força da evidência; sugerir melhorias; dar o veredito.

## O veredito em três níveis (linhas 87 a 95)

- **Pronta para compartilhar:** método sólido, contas conferidas, ressalvas ditas; só sugestões menores.
- **Compartilhar com ressalvas:** no geral certa, mas com limites ou premissas que precisam ir junto; a revisão lista as ressalvas obrigatórias.
- **Precisa de revisão:** erro, problema de método ou análise que falta; a revisão lista as mudanças em ordem de prioridade.

O relatório da revisão (linhas 97 a 125) tem campos fixos: veredito, método, problemas com gravidade (alta, média, baixa), contas refeitas (confere ou diverge), gráficos, melhorias e as ressalvas que quem lê precisa receber.

## A lista de conferência antes de entregar (linhas 129 a 165)

- **Qualidade do dado:** fonte certa para a pergunta; dado atual o bastante, com a data de referência anotada; série sem buraco e sem segmento faltando; taxa de vazio olhada nas colunas principais, e o vazio tratado de forma declarada (excluído, preenchido ou marcado); sem contagem dupla; filtros conferidos.
- **Cálculo:** o nível de agregação bate com o grão da análise; a taxa usa o denominador certo, que não é zero; comparações com o mesmo comprimento de período, e o período parcial fica de fora ou vem anotado; a definição da métrica é a que quem lê usa, e o desvio é dito; as partes somam o todo, ou se explica por que não (sobreposição, por exemplo).
- **Plausibilidade:** grandeza possível (porcentagem entre 0 e 100, receita não negativa); série sem salto sem explicação; número principal batendo com outra fonte conhecida; e os casos de borda: segmento vazio, período sem atividade, entidade nova.
- **Apresentação:** barra começando do zero, eixos rotulados e escalas iguais entre painéis; precisão adequada e formato consistente; título que diz o achado, não só o nome da métrica, com o período escrito; limites declarados; e a análise refazível por outra pessoa a partir do que está documentado.

## As armadilhas (linhas 167 a 256)

Cada uma vem com o problema, exemplos e como evitar.

| Armadilha | O que acontece | Como evitar |
|---|---|---|
| Junção que multiplica linhas | uma junção de muitos para muitos infla contagens e somas sem avisar | contar as linhas antes e depois; contar entidades distintas |
| Viés de sobrevivência | olhar só o que existe hoje e esquecer quem saiu, cancelou ou falhou | perguntar quem não está no conjunto antes de concluir |
| Período incompleto | comparar um período parcial com um cheio (o mês que não acabou contra o anterior; a semana olhada na quarta contra a semana inteira) | filtrar para períodos completos, ou comparar o mesmo número de dias |
| Denominador que muda | a taxa melhora ou piora porque mudou a definição de quem entra na base, não o comportamento | mesma definição em todos os períodos comparados, e mudança de definição anotada |
| Média de médias | tirar a média de médias já calculadas dá errado quando os grupos têm tamanhos diferentes; no exemplo da fonte, 100 pessoas a 50 e 10 pessoas a 200 dão 125 pela média das médias e 63,64 pela média ponderada | agregar do dado bruto, nunca de médias prontas |
| Fuso que não bate | fontes em fusos diferentes (carimbo em UTC, data mostrada em hora local; fechamentos diários com horas de corte diferentes) | levar tudo a um fuso só antes de analisar, e escrever qual foi |
| Segmento definido pelo resultado | o grupo é formado pelo próprio desfecho que se mede, e a comparação vira círculo ("quem concluiu a entrada retém mais"; "os que mais usam geram mais receita") | definir o segmento por característica anterior ao que se mede |

**Outras, só nomeadas (linhas 248 a 256):** paradoxo de Simpson (a tendência se inverte entre o agregado e os segmentos), correlação apresentada como causa, amostra pequena, outlier puxando a média, muitos testes com escolha dos que deram resultado, uso de informação futura para explicar o passado, e janela de tempo escolhida para favorecer a história.

## Conferir o resultado (linhas 258 a 287)

- **Ordem de grandeza:** todo número principal passa pelo teste de bater com o que já se sabe (o total conhecido, o painel, a faixa possível, a soma dos segmentos perto de 100%).
- **Conferência cruzada, cinco técnicas:** calcular a mesma métrica por dois caminhos e ver se batem; seguir à mão alguns registros individuais; comparar com referência conhecida (painel publicado, relatório financeiro, análise anterior); fazer a conta inversa (se o total é X, o valor por pessoa vezes o número de pessoas dá perto de X?); e testar as bordas (um dia só, uma pessoa só, uma categoria só: o resultado miúdo faz sentido?).
- **Sinais que pedem investigação:** métrica que mudou muito de um período para o outro sem causa clara; contagem ou soma em número redondo exato (cheira a filtro ou valor padrão); taxa exatamente em 0% ou em 100% (pode ser dado incompleto); resultado que confirma a hipótese com perfeição ("reality is usually messier"); e valores idênticos entre períodos ou segmentos (a consulta pode estar ignorando uma dimensão).

## Documentar para poder refazer (linhas 289 a 362)

O molde de documentação de uma análise pede: a pergunta; as fontes com a data de referência de cada uma; as definições (como cada métrica é calculada, como se decide quem entra em cada segmento, e o período com início, fim e fuso); o método em passos; premissas e limites, com o efeito possível na conclusão; os achados com a evidência; as consultas usadas; e as ressalvas. Para código reaproveitado, um cabeçalho com propósito, premissas, fonte e a data da última validação. Guardar consultas e código em controle de versão, anotar a data do retrato do dado e, ao rodar de novo, dizer o que mudou.

## Números da fonte, sem lastro

A fonte não diz de onde vêm; entram aqui como número da fonte, sem medição própria nem referência.

- Mudança acima de **50%** de um período para o outro como sinal de alerta (linha 283), e crescimento de 50% ou mais ao mês como coisa a desconfiar (linha 269).
- "Bateu com o painel dentro de **2%**", no exemplo de cabeçalho de código (linha 341): é ilustração, não tolerância recomendada.
- Os valores dos exemplos (500 mil contra 800 mil, 1.000 e 3.500 linhas, 100 e 10 pessoas) são ilustrativos; a conta da média de médias confere (5.000 mais 2.000, divididos por 110, dá 63,64).
