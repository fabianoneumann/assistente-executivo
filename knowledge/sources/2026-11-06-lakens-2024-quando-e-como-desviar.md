---
titulo: "When and How to Deviate From a Preregistration"
tipo: paper
autor: "Daniël Lakens"
url: "https://doi.org/10.1525/collabra.117094"
publicado_em: 2024-05-14
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [preregistration, deviations, severity, validity, falsificationism, type-1-error, statistical-analysis-plan, reporting, sensitivity-analysis]
licenca: "CC BY, na própria página"
---

# Lakens 2024 (Collabra: Psychology): quando desviar de um pré-registro e como relatar

Ficha em palavras próprias. Daniël Lakens, Eindhoven University of Technology; Collabra: Psychology, vol. 10, n. 1, artigo 117094, seção Methodology and Research Practice; submetido em 10/1/2024, aceito em 22/3/2024, publicado em 14/5/2024. Área: metodologia de pesquisa em psicologia. Lido no PDF da editora, baixado do portal da universidade. Artigo conceitual, sem dados próprios: todos os exemplos de relato são hipotéticos, e o autor avisa que omite neles os resultados e gráficos que um relato real traria.

## A pergunta

Com o pré-registro mais comum, os pesquisadores precisam de orientação para relatar quando se afastam do plano estatístico. A proposta é uma abordagem de princípios, apoiada na filosofia do erro estatístico e no falsificacionismo metodológico, que não trata todo desvio como problema: cada desvio se julga pelo efeito sobre a severidade do teste e sobre a validade da inferência.

## Os conceitos de base

- **Pré-registro:** documento com data que comunica de forma transparente que as análises não foram escolhidas a partir de informação nos dados que vai decidir o resultado. Deve fixar todas as decisões de análise, entre elas a quantidade de dados, as medidas, o pré-processamento e quando o resultado corrobora ou falsifica a predição.
- **Severidade** (Mayo, 2018): um teste é severo quando tende a apoiar a hipótese se ela está certa e tende a não apoiá-la se ela está errada. Quanto menores os erros de Tipo 1 e Tipo 2, mais severo o teste. É propriedade do teste.
- **Validade:** "the approximate truth of an inference" (Shadish e outros, 2001). É propriedade da inferência.
- **Contínuos:** severidade e validade são dimensões graduais, e nenhuma das duas se conhece com exatidão. Raramente dá para quantificar a severidade com precisão, mas dá para avaliar por alto quanto uma decisão analítica pode inflar o erro de Tipo 1. Da validade se avaliam os riscos.
- **Efeitos de seleção enviesados** (biasing selection effects): as práticas que reduzem a severidade, como formular a hipótese depois de ver os resultados (HARKing, Kerr 1998) ou relatar só as análises que ajudam. Se a hipótese nasceu dos dados, ela pode até ser verdadeira, mas os dados nunca teriam como contrariá-la.
- **Severidade independe da verdade da afirmação:** uma afirmação verdadeira pode vir de um teste sem severidade alguma. O exemplo do autor é a fraude: dados fabricados sustentam uma afirmação que pesquisa rigorosa depois confirma.
- **Quatro validades** (Shadish e outros; Vazire e outros, 2022): de constructo, externa, interna e de conclusão estatística. O desvio mexe sobretudo na de conclusão estatística (retirar dados que não vêm do mecanismo de interesse) e na de constructo (mudar os itens de uma escala conforme a confiabilidade). A externa e a interna sofrem menos, embora um erro possa atingi-las (uma covariável que por acidente não foi gravada).
- **Afirmação científica** (Popper, 1959): declaração dicotômica sobre a predição ter sido apoiada ou não. Nem todo teste de um artigo leva a uma afirmação. Quem testa teoria precisa dizer qual resultado conta como apoio e qual como falsificação.
- **Vale fora do frequentismo:** o foco é o teste de hipótese frequentista, e o autor registra que testes severos também são desejados na estatística bayesiana (checagem de modelo, testabilidade pela distribuição preditiva a priori, controle da probabilidade de evidência enganosa).

## O que conta como desvio, com um exemplo em três versões

O artigo cuida de afirmações apoiadas num teste diferente do que está no plano. Os motivos comuns de desvio, segundo a literatura citada: amostra diferente da registrada, exclusões não previstas, outro teste estatístico, mudança por erro na coleta. O autor separa três situações com o mesmo caso, em que se planejou analisar todos os dados e, ao olhar os dados, surge a ideia de tirar um subconjunto:

- **Desvio:** a afirmação se apoia na análise do subconjunto, e a análise planejada fica de lado.
- **Geração de hipótese:** analisa-se o subconjunto, a afirmação segue na análise completa, e a ideia de excluir vira hipótese para um estudo futuro. Nesse uso, o teste não precisa seguir o pré-registro.
- **Análise de sensibilidade:** apresentam-se as duas análises, a afirmação segue na completa, e se diz se o resultado depende da decisão. Essas análises costumam ser variações pouco sistemáticas.

O autor evita "exploratório" e "confirmatório", porque a distinção que pesa é a severidade ou o controle dos erros: um teste "não confirmatório" pode ser mais severo que um "confirmatório". Por exemplo, o teste registrado pode não controlar o erro, ou a premissa de homogeneidade pode ser rejeitada e o teste não registrado controlar melhor.

## O critério central

O objetivo de um teste nessa filosofia é fazer afirmações válidas e severamente testadas. Fixar o plano antes serve para evitar efeitos de seleção, mas a severidade não é a única meta. Um motivo justificável para desviar é ganhar validade, mesmo pagando em severidade, quando se argumenta de forma convincente que o plano registrado leva a um teste de baixa validade. O autor lembra que, na prática, uma afirmação com desvio muitas vezes ainda foi mais severamente testada que uma sem pré-registro. E pede mais do que relatar o desvio: avaliar a consequência dele (apoiado em Hardwicke e Wagenmakers, 2023; Willroth e Atherton, 2024).

**Tabela 1 do artigo, quatro combinações:**

| | Validade menor | Validade maior |
|---|---|---|
| **Severidade menor** | Relatar só uma de cinco variáveis do constructo porque só ela deu p < .05 | Desviar para retirar observações que não vêm de processos ligados à pergunta |
| **Severidade maior** | Seguir a análise registrada de todos os dados, embora 15% dos respondentes não tenham seguido as instruções | Seguir um plano registrado com alta validade de constructo e estatística |

## As cinco categorias de motivo

As categorias vêm de uma revisão dos desvios relatados em metaciência (Akker e outros, 2023; Claesen e outros, 2021; Toth e outros, 2021; Willroth e Atherton, 2024) e da experiência pessoal do autor como revisor e como quem registra. Ele admite que podem não esgotar os casos e podem se sobrepor na prática. A Figura 1 resume o que cada uma pede em forma de perguntas; a pergunta da severidade está nas cinco, e a da validade, que o texto trata como opcional para alguns desvios, aparece em três:

| Categoria | Primeiro passo | Severidade | Validade |
|---|---|---|---|
| Evento imprevisto | Descrever o evento | Como o desvio afetou? | Não consta na figura |
| Erro no registro ou no estudo | Especificar e corrigir o erro | Como o desvio afetou? | O desvio aumentou? |
| Informação que faltava | Dizer o que faltava e acrescentar | Como o desvio afetou? | Não consta na figura |
| Premissa não testada violada | Dizer a premissa e como foi violada | Como o desvio afetou? | O desvio aumentou? |
| Hipótese auxiliar falsificada | Dizer a hipótese e como foi falsificada | Como o desvio afetou? | O desvio aumentou? |

### 1. Evento imprevisto

Exemplos: a pandemia de COVID-19 impediu coletas presenciais; a amostra final não bate com a planejada depois da limpeza, em geral porque não se previu a facilidade ou a dificuldade de coletar.

- **Risco:** com pouco controle sobre a amostra final, sobra pouca flexibilidade e há pouco risco de efeito de seleção, desde que se evitem regras de parada dependentes dos dados. Se dá para argumentar que não houve parada oportunista nem relato seletivo, a amostra diferente não infla o erro de Tipo 1.
- **Direção:** menos observações reduzem a severidade principalmente pela perda de poder; mais observações, mantido o resto, aumentam. Com amostra bem menor, resultados inconclusivos ficam mais prováveis, a pergunta possível pode ter de ser revista, e com poder muito baixo pode nem fazer sentido testar.
- **Planejar a flexibilidade:** análise sequencial em grupos com gasto de alfa permite registrar um tamanho pretendido e já definir como calcular o alfa se vierem mais ou menos dados, mantendo o erro de Tipo 1 sob controle.
- **Antes de analisar:** dá para atualizar o registro (o Open Science Framework oferece a opção). Em Registered Report, costuma ser caso de contatar o editor, que pode consultar os revisores do estágio 1 e decidir se a mudança é grande o bastante para retirar a aceitação em princípio.
- **Exemplo de menos dados:** um incêndio fechou o laboratório de EEG com 100 participantes coletados, de 240 planejados. Rodou-se a análise planejada em todos os 100, e o registro dos arquivos mostra gravações até a véspera do fogo. O erro de Tipo 1 segue controlado; uma análise de poder de sensibilidade mostra o erro de Tipo 2 passando de 10% (poder de 90%) a 45% (poder de 55%), perda grande de valor informativo.
- **Exemplo de mais dados:** esperavam-se 500 participantes por redes sociais, o pedido viralizou e 5.124 responderam. Analisou-se uma só vez, com todos os que responderam antes do início da análise. A severidade subiu, com poder bem maior.

### 2. Erro no registro ou no estudo

O autor separa lapsos e má aplicação de regra. Lapsos: escrever que a condição experimental pontuaria mais quando a teoria diz menos; errar o nome de uma variável no código registrado; recrutar um participante a mais, 81 em vez de 80 (caso de Claesen e outros, 2021). Má aplicação de regra: registrar a falsificação pela diferença significativa e notar, com 56.000 observações, que diferenças minúsculas e sem importância prática dão significativas, quando o teste melhor seria contra uma diferença grande o bastante para importar.

- **Quando o erro só tem uma correção** (todos os pares concordam que a teoria prevê o contrário), o efeito na severidade é desprezível.
- **Quando a correção deixa folga,** como migrar de teste de nulidade para teste contra o menor efeito de interesse, nem fica claro que houve erro: a pergunta pode ter sido refeita por oportunismo, e há muita liberdade para escolher o que é grande o bastante. A severidade pode cair bastante, ainda mais com os dados já vistos. Mesmo assim, os pares podem concordar que a afirmação deve seguir a análise desviada.
- **Revisores que veem erro onde o autor não vê:** a troca entre modelo mais simples e mais complexo é desvio comum (Akker e outros, 2023), talvez porque se registra um plano que não é o melhor teste da pergunta, e a estatística avança. Apresentar várias abordagens como análise de sensibilidade é sempre possível, mas elas podem divergir e abrir disputa sobre qual é a mais válida. Revisar o plano antes, como em Registered Reports, evita essa conversa depois da coleta. Depois de um estudo só pode restar muita dúvida, que replicações e extensões devem examinar.
- **Exemplos de relato:** a soma de cinco itens sem dizer que os itens 2 e 5 se invertem, quando três estudos anteriores os invertem, deixa uma só soma válida, sem efeito na severidade e com ganho de validade. Um erro de programação que perde a variável "tem cachorro" obriga a tirar esse fator; sem alternativa, sem flexibilidade, o erro de Tipo 1 fica intacto, e a análise com o fator teria sido mais válida.

### 3. Informação que faltava

Omissão ou registro tão vago que dá no mesmo. A decisão é tomada com os dados à mão; formalmente pode nem ser desvio, mas ainda assim é preciso dizer como a análise final se afastou do plano. Existe a possibilidade de escolha oportunista, que reduziria severidade e validade, e o autor deixa claro que isso não torna todo desvio oportunista nem redutor de severidade. A preocupação dele é o que dá para comunicar de forma transparente sobre a severidade, sem julgar a intenção de quem pesquisa.

- **A folga depende do que falta:** acrescentar um alfa de 0,05 esquecido num teste único é seguro; não ter dito, com cinco variáveis dependentes, se basta uma significativa ou se precisam ser todas abre muita variação em corrigir ou não a multiplicidade e em como corrigir.
- **Como reduzir a dúvida:** mostrar que todas as análises plausíveis, e principalmente a mais conservadora, levam à mesma afirmação. Se dependem da escolha, é preciso comunicar que a afirmação foi menos severamente testada do que teria sido com o registro completo.
- **Teto:** esse tipo de desvio, no máximo, mantém a severidade; na prática, é bem possível que a reduza. Com certas lacunas, como a quantidade total de dados, nem dá para rodar todas as alternativas, pois isso pediria coletar mais ou usar dados que não existem.
- **Prevenção:** registrar o código de análise.
- **Exemplos:** direção do teste t não dita: planejava-se unilateral, p de 0,002, e o bilateral também passaria (0,002 × 2 < 0,05), logo a severidade não muda. Efeitos simples não ditos depois de uma ANOVA de três condições: o contraste previsto (A > B > C) deu p de 0,028, várias comparações eram possíveis, e com correção de multiplicidade o resultado deixa de confirmar, logo a afirmação ficou menos severamente testada.
- **Relato:** incluir os testes relevantes, gráficos e outros dados que ajudem a avaliar a severidade, marcar o desvio com clareza no texto e, com limite de palavras, pôr o detalhe em suplemento.

### 4. Premissa não testada violada

Premissas sobre o comportamento dos participantes: que respondam a tudo, sigam a instrução, preencham uma vez só. Faltam modelos teóricos do que é resposta válida, então a decisão sobre outliers fica em parte subjetiva e se apoia em explorar os dados. Parte dos casos se prevê no registro, tudo não dá para prever, e pode até não valer o esforço criar uma teoria específica por estudo. Isso separa a premissa não testada da hipótese auxiliar, que costuma ter teste formal.

- **O dilema:** manter o plano com a premissa violada pode reduzir muito a validade; desviar pode ganhar validade, mas abre espaço para efeito de seleção se a análise escolhida inflar o erro de Tipo 1. Pode acontecer de o risco ser pequeno e o ganho, grande.
- **O relato:** dizer a premissa e como falhou, como a análise mudou, e avaliar severidade e, se couber, validade. Havendo várias saídas, relatar todas as defensáveis. Se são poucas e levam à mesma afirmação, pode-se argumentar que a severidade não mudou.
- **Exemplo, respostas em linha reta:** dois participantes marcaram "1" em tudo e um em 80% das questões, com tempo menor que o de todos os outros; a escala tinha itens invertidos, o que torna menos provável uma causa benigna. Definiu-se descuido como dar a mesma resposta em mais de 75% das questões e saíram três pessoas. Com todos os dados, nada significativo; removendo ou tratando como dado ausente, significativo. O relato admite o risco (talvez ninguém pensasse em remover se o registrado tivesse dado certo), considera as análises alternativas mais válidas e reconhece que foram menos severamente testadas do que com a triagem registrada.

### 5. Hipótese auxiliar falsificada

Toda teoria se testa junto com hipóteses auxiliares sobre medidas, instrumentos e condições (Hempel, 1966), como a cláusula ceteris paribus das replicações próximas: instrução em fonte com ou sem serifa pode ficar nessa cláusula se a teoria diz que a fonte não importa. A diferença para a premissa não testada é que a auxiliar se testa com os dados coletados, e, caindo, deixa de fazer sentido relatar a análise registrada; a premissa não testada nunca chega a ser rejeitada de todo.

- **Exemplos:** normalidade pelo teste de Jarque-Berra (grafia do artigo), com troca por teste robusto; confiabilidade pelo coeficiente ômega contra um mínimo, com retirada de um item ruim.
- **Registro condicional:** um bom registro traz análises do tipo "se X, então Y, senão Z", dependentes dos dados, sem custo em severidade.
- **Quando nem se deve testar:** quase todos falham na checagem de atenção, ou a checagem de manipulação mostra que ela não funcionou. O teste registrado perde validade, e a inferência não informa sobre a hipótese: é muito provável sair resultado nulo mesmo com a predição correta. Esses estudos ainda ensinam sobre método.
- **O relato:** dizer a hipótese e o procedimento que a derrubou, como a análise mudou, e avaliar se a severidade caiu ou subiu e o efeito na validade. Com poucas opções defensáveis, todas chegando à mesma afirmação, e ganho de validade, o desvio se justifica.
- **Exemplo:** desvios padrão muito diferentes; os testes de Levene e de Bartlett rejeitam a homogeneidade; o t de Student planejado poderia não controlar o erro de Tipo 1; troca pelo t de Welch, com melhor controle, e os testes não paramétricos usuais levam à mesma afirmação. O relato conclui que validade de conclusão estatística e severidade aumentaram.

## Como reduzir a necessidade de desviar

- Desvios devem ser esperados, mas o ideal é não precisar: há quem não desvie nenhuma vez.
- Atualizar o registro antes de ter os dados não custa severidade, desde que a atualização independa dos dados do teste.
- Experiência com registro e conhecimento dos dados reduzem a chance de desvio; dados piloto aumentam esse conhecimento.
- Registrar código sobre dados simulados, ou testes de hipótese legíveis por máquina (Lakens e DeBruine, 2021), elimina ambiguidade; listas de checagem (Wicherts e outros, 2016) reduzem lacunas.
- Não correr para o teste de hipótese sem o trabalho exploratório que alimenta um teste com sentido (Scheel e outros, 2021). Com pouca experiência nos métodos e medidas, vale registrar análises condicionais ou usar métodos que dão flexibilidade controlando o erro de Tipo 1.

## Como relatar

- Formulários em tabela: cada desvio é uma linha, e as colunas descrevem os aspectos dele (a nota 1 do artigo lista quatro modelos).
- Numerar as linhas do pré-registro para apontar a frase exata e citar a linha do código onde o desvio entrou; isso também evita esquecer de relatar análises registradas.
- A regra do autor: "For every deviation clearly specify when, where, and why a deviation from a preregistration occurred", seguida da avaliação do efeito na severidade e, quando couber, na validade.

## Como saber se o desvio melhorou mesmo

Só estudos seguintes testam se um desvio aumentou a validade. Se ele trocou severidade por validade, replicações e extensões com o plano atualizado em dados novos devem corroborar as predições, sinal de linha de pesquisa progressiva (Lakatos, 1978; Meehl, 1990). Se veio de efeito de seleção, a corroboração fica menos provável e a linha é degenerativa. No curto prazo, uma replicação direta bem-sucedida demonstra o progresso. O autor pede metaciência sobre quanto pesquisadores e pares conseguem avaliar a validade de uma inferência (Schiavone e Vazire, 2023).

## Conclusão do autor

Desvios são comuns, muitos têm efeito desprezível na severidade e alguns a aumentam. Onde a redução é mais forte, quem desviou deve justificar com argumentos de ganho substancial de validade. Severidade e validade precisam ser avaliadas juntas. Frase-regra do resumo: "A principled approach to the use of preregistration should not treat all deviations as problematic."

## Limites declarados

- As cinco categorias nascem de revisão da metaciência e de experiência anedótica, podem não ser exaustivas e se sobrepõem.
- Severidade raramente se quantifica com precisão, e a validade de uma inferência nunca se sabe ao certo.
- Os exemplos são hipotéticos e não mostram os resultados que um relato real traria.
- O foco é o teste de hipótese frequentista.

## Tudo o mais que ensina

- A prática do pré-registro nasceu, em várias disciplinas, da preocupação com o uso oportunista da flexibilidade de análise em pesquisa quantitativa (Chan e outros, 2013; Wiseman e outros, 2019).
- Quem conclui de forma dicotômica por p < α, ou faz análise de poder a priori, está aplicando a abordagem de erro de Neyman e Pearson (1933) mesmo sem saber, e ela repousa no falsificacionismo metodológico (Lakatos, 1978).
- As afirmações baseadas em testes formam o histórico de uma teoria (Meehl, 1990), e a pesquisa constrói sobre teorias com predições bem-sucedidas sob testes severos.
- Existem outras justificativas filosóficas do pré-registro (Peikert e outros, 2023), e o autor diz que ele decorre mais naturalmente de uma filosofia que valoriza predições sob controle estrito de afirmações erradas.
- Verisimilitude, ou proximidade da verdade (Niiniluoto 1998; Popper 1959): um teste menos severo e mais válido pode gerar uma afirmação com mais dela.
- A cláusula ceteris paribus se examina por replicações próximas ou "stability probes" (Uygun Tunç e Tunç, 2022).
- O excesso de amostra por engano pode não mudar nada: um participante a mais pode deixar a afirmação estatística igual, seja qual for o dado dele.
- No exemplo das respostas em linha reta, a alternativa à remoção é tratar o dado como ausente ao acaso; Reuning e Plutzer (2020) são a citação para a causa benigna ser menos provável com itens invertidos.
- Recomendação do t de Welch quando a homogeneidade falha: Delacre e outros, 2017.
- O autor agradece à inspiração em dois podcasts (Quantitude S3E07, "In Defense of Researcher Degrees of Freedom"; Within & Between S4E11), declara não ter conflito de interesse e financiamento do Ammodo Science Award 2023 for Social Sciences.
