---
titulo: "Human-in-the-Loop Artificial Intelligence: A Systematic Review of Concepts, Methods, and Applications"
tipo: paper
autor: "Konstantinos Lazaros, Aristidis G. Vrahatis, Sotiris Kotsiantis"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC13114286/"
publicado_em: 2026-03-26
capturado_em: 2026-10-28
licenca: "CC BY 4.0 (© 2026 dos autores, licenciado pela MDPI; indicada na página)"
areas: [agent-engineering]
tags: [human-in-the-loop, human-on-the-loop, oversight, trust-calibration, automation-bias, scapegoat-in-the-loop, escalation, systematic-review]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. *Entropy* (MDPI), vol. 28, n.º 4, artigo 377; DOI 10.3390/e28040377; recebido em 11/02/2026, publicado em 26/03/2026. Autores da Universidade Jônica (Corfu) e da Universidade de Patras. Lido em 2026-10-28, na pesquisa.

## Método

Revisão sistemática no formato PRISMA, em Scopus e Google Scholar, com rastreio de citações para frente e para trás; janeiro de 2018 a janeiro de 2026; termos como *human-in-the-loop*, *human oversight*, *human-on-the-loop*, aprendizado ativo, RLHF e governança, cruzados com domínios (saúde, sistemas autônomos, segurança, finanças, educação, indústria). Entra o estudo com papel humano explícito no treino, na inferência, na supervisão ou na governança; sai o que usa o termo sem definir o papel. Corpus central: **134 estudos**.

## Raízes

Cibernética e controle por realimentação nos anos 1940 e 1950 (Wiener: a pessoa precisa de meios para observar o sistema e agir sobre ele); sistemas de apoio à decisão nos anos 1960 e 1970; aprendizado ativo formalizado nos anos 1990; a opacidade do aprendizado profundo reforçando a supervisão; a racionalidade limitada de Simon; times humano-máquina (o "centauro" do xadrez livre). **A revisão não atribui a origem do termo a uma área ou autor.**

## Definições

- **IA com humano no laço:** o paradigma em que a contribuição humana tem **impacto operacional** no desenvolvimento, uso, supervisão ou governança do modelo.
- Colaboração humano-IA é mais ampla e pode não ter laço de controle. Aprendizado de máquina interativo e RLHF são famílias de método dentro do paradigma; explicabilidade é um apoio (confiança, auditoria), não um tipo de laço.

## Onde a pessoa está no laço

Taxonomia de Singh e Szajnfarber, adotada pela revisão:

| Posição | A pessoa | A IA | Exemplo |
|---|---|---|---|
| No laço (*in*) | decide cada passo | apoia | diagnóstico, decisão jurídica |
| Sobre o laço (*on*) | monitora e intervém quando precisa | opera supervisionada | vigilância por drone, negociação automática |
| Acima do laço (*over*) | define objetivos, restrições, regras | executa dentro dos limites | sistemas de política |
| Abaixo do laço (*under*) | executa a ação final | aconselha | apoio à decisão clínica |
| Ao lado do laço (*along*) | colabora em paralelo | coordena lateralmente | cocriação |

O texto e a tabela descrevem o "abaixo" de formas diferentes (no texto, a IA influenciando o comportamento da pessoa; na tabela, a IA aconselhando), sem conciliar. A contribuição própria dos autores soma duas dimensões à posição: a **granularidade** da interação (grossa: aceitar ou rejeitar; média: correções seletivas; fina: guiar passo a passo) e o **tempo** (síncrono ou assíncrono; contínuo ou episódico). Interação fina e síncrona para controle de alto risco; supervisão grossa e assíncrona para risco moderado; e sistemas de vazão alta com revisão por amostra e pontos de checagem síncronos onde importa.

## Achados

- **Calibração de confiança:** confiança demais (viés de automação, perda de habilidade), calibrada, de menos (perde o benefício, sobrecarga). Pessoas deixam passar erros da IA que poderiam pegar, e pegam menos à medida que se acostumam com uma IA que acerta muito. Cansaço piora a supervisão.
- **Supervisão de verdade contra de fachada:** só vale com **informação, tempo, competência e autoridade** suficientes para avaliar e reverter; a revisão aponta que essas condições muitas vezes faltam mesmo onde o desenho diz ter humano no laço.
- **Bode expiatório no laço** (*scapegoat-in-the-loop*): a pessoa incluída principalmente para absorver a culpa, cumprindo a norma sem tornar nada mais seguro.
- **IA generativa:** separar a verificação da geração, com triagem por nível de risco; verificação sem camadas leva à aprovação superficial.

## Desafios abertos

Escala (o volume de decisões passa da capacidade humana; respostas atuais: aprendizado ativo, supervisão em níveis, auditoria por amostra); limites cognitivos; retorno conflitante entre pessoas (voto da maioria não resolve: separar pluralidade de valores de erro); manipulação dirigida aos revisores humanos; revisores que normalizam o viés sob pressa ou regra vaga.

## Arquiteturas adaptativas e recomendações

- Supervisão que se ajusta ao risco e à confiança da IA é promissora, mas um sistema que regula a si mesmo pode **reduzir a própria supervisão por uma autoavaliação errada**. Por isso, salvaguardas fixas ao lado das adaptativas: supervisão obrigatória no alto risco, regras definidas de fora, auditorias aleatórias obrigatórias, modelos sentinela independentes, padrão conservador quando a incerteza é alta; e uma **meta-supervisão**, em que pessoas governam os gatilhos e revisam incidentes.
- Recomendações de desenho: critérios claros e tempo para o revisor; monitorar o caso e o resultado agregado, com gatilho de **escalada** quando divergem; papéis, direito de reverter e registro de decisões explícitos; aviso cedo e intervenção graduada em vez de "assuma agora" no fim; mecanismo contra o impasse em que pessoa e IA ficam deferindo uma à outra; a saída da IA no ponto de decisão que já existe, para evitar o carimbo automático; avaliar por um vetor de dimensões, não por uma nota só.
- Conclusão: o controle deve escalar com o risco e a incerteza, mantendo pontos de reversão e de responsabilidade inegociáveis nas decisões de alto impacto. Os autores propõem uma parceria "com o humano" (*human-with-the-loop*) como sucessora do paradigma atual. Agentes de IA generativa quase não aparecem na revisão.

---
