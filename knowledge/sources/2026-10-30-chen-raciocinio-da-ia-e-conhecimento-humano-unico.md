---
titulo: "Revealing AI Reasoning Increases Trust but Crowds Out Unique Human Knowledge"
tipo: paper
autor: "Zenan Chen, Ruijiang Gao, Yingzhi Liang"
url: "https://arxiv.org/abs/2511.04050"
publicado_em: 2025-11-06
capturado_em: 2026-10-30
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [human-in-the-loop, trust-calibration, automation-bias, chain-of-thought, reasoning-models, unique-human-knowledge, information-asymmetry, human-ai-complementarity]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv 2511.04050 (cs.HC), v1 de 06/11/2025, a única versão (lida); 38 páginas: 9 de texto, as referências e um apêndice com telas da interface, questionários, prompts e exemplo de raciocínio. Naveen Jindal School of Management, Universidade do Texas em Dallas; autores em ordem alfabética. Nem o texto nem a página do arXiv dizem em que conferência ou revista o trabalho saiu. O pré-registro está em aspredicted.org (q2b2-9y9g), não aberto. O integral foi extraído do PDF; as Figuras 2 e 3 e as telas das Figuras 12 e 14 foram lidas como imagem; as demais telas (Figuras 4 a 16) não têm texto extraível. Lida (camadas flexíveis de avaliação).

## A pergunta

O desempenho de equipes humano-IA depende de a pessoa avaliar bem a capacidade da IA e saber quando aceitar e quando contrariar a recomendação. Para isso ela usa o que os autores chamam de **conhecimento humano único** (UHK, Unique Human Knowledge): informação privada, tácita ou de contexto que a IA "não consegue observar diretamente nem inferir com segurança". Quando a recomendação conflita com esse conhecimento, a pessoa precisa contrariar a IA para a equipe render o máximo.

A literatura registra apreciação de algoritmos e dependência excessiva: as pessoas tendem a seguir a IA mesmo quando ela erra, pela força persuasiva da recomendação de máquina e pela ancoragem na primeira saída. Isso pode deslocar o uso do conhecimento humano único e levar a delegação errada.

O raciocínio dos LLMs (pensar passo a passo, cadeia de pensamento; e os modelos de raciocínio, que exploram vários caminhos, se autoavaliam e são treinados por reforço) melhora o desempenho, e produtos como DeepSeek R1, GPT-5, Gemini 2.5 Pro e Claude Sonnet 4.5 mostram esse raciocínio ao usuário, com extensões variadas. Os autores o distinguem da explicação de IA explicável (XAI): o raciocínio reflete o processo de resolver o problema, com monitoramento metacognitivo e autochecagens que trazem sinais de inconsistência e incerteza; a XAI quer ajudar a entender o modelo, e o raciocínio quer melhorar o desempenho e não foi feito para persuadir.

Duas possibilidades: mostrar o raciocínio ajuda a pessoa a medir a acurácia da IA e a confiar menos em respostas erradas, efeito que seria maior para quem tem conhecimento próprio para avaliar o raciocínio; ou causa vieses, porque, pela literatura clássica de persuasão, mensagens mais longas e elaboradas aumentam a aceitação por atalho, e justificativas de LLM dadas depois da resposta já se mostraram capazes de atrapalhar a supervisão humana. Pergunta central: **mostrar o raciocínio da IA aumenta ou reduz o uso do conhecimento humano único?** Os autores variam a extensão do raciocínio exibido (nenhum, breve, extenso) e medem a confiança na IA e o ganho de desempenho vindo do conhecimento humano único.

## Método

- **Experimento** on-line, pré-registrado e com incentivo atrelado ao acerto, no Prolific, com 752 participantes (extenso 252, nenhum 250, breve 250).
- **Tarefa:** o participante faz o papel de gestor de contratação que tria currículos com um sistema de apoio baseado em LLM. Cada currículo tem notas de 1 a 5 em Formação, Experiência e Encaixe de personalidade. O encaixe de personalidade é o conhecimento humano único do desenho: representa o que se sabe em contato pessoal.
- **Gabarito:** a decisão verdadeira (contratar ou não) é gerada por um modelo logístico com coeficientes 1, 1,2 e 1,5 para as três características. Os pesos foram calibrados para que, com as mesmas 10 decisões históricas, a IA acerte mais que as pessoas quando elas não têm o encaixe e menos quando têm. A tarefa sintética tira confusões do mundo real.
- **Duas decisões por candidato:** com base nas 10 decisões históricas, a pessoa decide primeiro sozinha (decisão inicial) e depois de ver a recomendação da IA (decisão final). As duas valem US$ 0,075 por acerto. Segundo os autores, a decisão independente primeiro serve para descartar mecanismos comuns do viés de automação em que a explicação da IA vira atalho cognitivo.
- **Desenho 3 × 2:** entre sujeitos, o nível de raciocínio exibido; dentro do sujeito, ter ou não o conhecimento humano único. Fase I (20 rodadas): só Formação e Experiência. Fase II (20 rodadas): entra o Encaixe de personalidade. Nas duas fases a IA não tem essa característica.
- **O aviso:** antes da Fase II, os participantes são informados explicitamente de que a IA não tem a terceira característica. A tela de abertura da Fase II diz que a IA não tem informação sobre o encaixe de personalidade (Figura 12), e a tela de decisão traz a nota "a IA não tem acesso à informação de encaixe de personalidade" (Figura 14). Segundo os autores, isso descarta a falta de transparência sobre as características como fonte do efeito, o que separa este estudo de trabalhos anteriores sobre transparência de características (Balakrishnan et al.).
- **Sem retorno:** os participantes não recebem retorno sobre o acerto entre rodadas, para que o aprendizado não varie entre os níveis de raciocínio.
- **Treino:** antes da Fase I, identificar o resultado de 3 currículos tirados dos 10 históricos. Antes da Fase II, novo treino com os mesmos 10 casos, agora com o encaixe de personalidade revelado, para enfatizar a importância desse dado.
- **Recomendação e raciocínio:** gerados pelo gemini-2.5-pro-preview, pela interface web oficial, com os parâmetros padrão do Google; o prompt traz as 10 decisões históricas (só Formação e Experiência) e pede 0 ou 1.
- **Raciocínio extenso:** um prompt reescreve o raciocínio bruto, longo demais, num texto com três razões alternativas que sustentam a decisão final, em três parágrafos, em primeira pessoa e como narrativa de quem pensa no momento. É a versão resumida que produtos como ChatGPT e Gemini mostram.
- **Raciocínio breve:** um truncamento do extenso que guarda só o primeiro caminho até a decisão, num parágrafo, para ficar diretamente comparável (exemplo na Tabela A3: o breve é o primeiro parágrafo do extenso mais a decisão).
- **Sem raciocínio:** um indicador giratório com "AI is thinking", para que todos saibam que a IA raciocina e a diferença seja só se o raciocínio aparece; o tempo de espera iguala o do grupo breve.
- **Exibição:** o raciocínio aparece palavra a palavra, a 20 palavras por segundo, e a pessoa precisa esperar a conclusão da IA para decidir. Há uma contagem de 5 segundos que trava os botões de decisão.
- **Medidas:** confiança é a taxa de concordância da decisão final com a recomendação da IA. O efeito do raciocínio na confiança vem da comparação entre condições dentro de cada fase. O efeito no uso do conhecimento humano único vem da diferença de acurácia entre a Fase II e a Fase I.
- **Pagamento e checagens:** US$ 4 fixos mais até US$ 3 por fase (máximo de US$ 10). O questionário inicial traz demografia, experiência em contratação, um teste de conhecimento de IA (0 a 5), uma escala de confiança em IA (10 itens, 0 a 50) e duas perguntas de atenção.
- **Balanceamento (Tabela A1):** nenhuma diferença significativa entre os grupos antes do tratamento (todos os p > 0,17). Conhecimento de IA de 4,64 a 4,68 e confiança em IA de 30,27 a 30,89 nos três grupos.

## Resultados

### Mais confiança na IA (Figura 2a e 2b)

Mostrar o raciocínio aumentou a concordância com a IA na decisão final, com ou sem o conhecimento humano único.

- **Fase I** (sem o encaixe): 88,7% sem raciocínio, 90,0% com o breve (p = 0,053) e 90,7% com o extenso (p = 0,005).
- **Fase II** (com o encaixe): 77,3%, 81,3% (p < 0,001) e 81,7% (p < 0,001).
- **Breve contra extenso:** não diferem (p = 0,165 na Fase I; p = 0,363 na Fase II).

Os autores destacam que, mesmo avisados de que a IA não tinha o encaixe de personalidade, os participantes confiaram mais nela depois de ver o raciocínio: em vez de ajudar a calibrar quando seguir a IA, o raciocínio aumentou a concordância. A extensão não fez diferença, o que contradiz a literatura de persuasão, em que argumentos mais elaborados persuadem mais.

### Acurácia da decisão final (Figura 2c e 2d)

- **Fase I:** 0,540 sem raciocínio, 0,544 com o breve e 0,552 com o extenso. Nenhum contra breve, p = 0,225; nenhum contra extenso, p = 0,020; breve contra extenso, p = 0,088.
- **Fase II:** 0,722, 0,706 e 0,702. Nenhum contra breve, p = 0,036; nenhum contra extenso, p = 0,009; breve contra extenso, p = 0,314.

### Ganho com o conhecimento humano único (Figura 3)

- **Acurácia:** a da decisão final sobe com significância da Fase I para a Fase II em todas as condições (todos os p < 0,001). O texto escreve o ganho em porcentagem: 18,2% sem raciocínio, 16,2% com o breve e 15,0% com o extenso; na Figura 3a, são diferenças de 0,182, 0,162 e 0,150 na proporção de acertos.
- **Concordância com a IA:** cai da Fase I para a Fase II em 11,5% sem raciocínio, 8,7% com o breve e 9,0% com o extenso (Figura 3b: −0,115, −0,087 e −0,090). Segundo os autores, em todas as condições os participantes usam o conhecimento próprio para decidir melhor e reduzem a confiança na IA quando sabem que ela não tem a terceira característica.

### Mais confiança, menos ganho

- **Ganho de acurácia:** é maior sem raciocínio (18,2%) e significativamente menor com o breve (16,2%, p = 0,042) e com o extenso (15,0%, p = 0,002); breve contra extenso, p = 0,136.
- **Queda na concordância:** também é menor com raciocínio, 11,5% sem raciocínio contra 8,7% com o breve (p = 0,006) e 9,0% com o extenso (p = 0,015); breve contra extenso, p = 0,619.
- **A leitura dos autores:** os ganhos menores "parecem" vir de ajustes insuficientes na confiança. O texto diz que isso "sugere" que mostrar o raciocínio, de qualquer extensão, enviesa o julgamento da capacidade da IA mesmo quando a pessoa sabe que falta a ela uma característica crucial, levando a confiança excessiva e uso insuficiente do conhecimento humano único.

## Conclusões dos autores

**Com a mesma informação** (Fase I), mostrar o raciocínio leva a mais confiança e a ganhos modestos de acurácia, porque a pessoa se apoia, com razão, nos pontos fortes da IA. **Quando a pessoa tem conhecimento que falta à IA**, a mesma confiança vira passivo: mostrar o raciocínio a faz depender mais da IA e desloca o conhecimento humano único.

**Sobre o aviso e a decisão independente**, o texto afirma que a piora continua mesmo quando a pessoa tem de decidir sozinha antes de ver a recomendação da IA: "this degradation persists even when humans are explicitly told that the AI lacks key information." Segundo os autores, os recursos do desenho descartam a falta de transparência sobre as características e os efeitos de ancoragem como explicações.

No desenho, o aviso e a decisão inicial sem a IA valem para todos os participantes das três condições de raciocínio: o aviso vem antes de toda a Fase II, e a decisão inicial sem a IA vem em toda rodada das duas fases.

**Encurtar o raciocínio não resolve:** o breve e o extenso tiveram efeitos de tamanho parecido. Os autores pedem cautela ao mostrar o raciocínio dos LLMs: recursos bem-intencionados como "mostre seu raciocínio" podem corroer o uso de informação valiosa quando ela está nas mãos das pessoas.

## Limites declarados e trabalhos futuros

**Tarefa simplificada:** a contratação tem fórmula conhecida, o que permite isolar o conhecimento humano único escondendo uma característica da IA, mas decisões reais são mais complexas. Falta testar com especialistas em contexto real (por exemplo, médicos diagnosticando). Especialistas podem ser menos suscetíveis, pela confiança no próprio conhecimento, ou mais, se o raciocínio da IA usar o jargão de autoridade da área deles. Entender como especialidade e complexidade da tarefa moderam o efeito é o próximo passo.

**Conselho de uma rodada:** o estudo cobre o caso em que a IA recomenda e raciocina e a pessoa decide. Com assistentes mais interativos, os autores propõem estudar várias rodadas: a pessoa interrompendo o raciocínio para perguntar "você considerou este fator que eu sei?", ou a IA pedindo a contribuição do usuário antes de fechar a recomendação. Antes disso, seria preciso entender se as pessoas sabem que têm esse conhecimento, se reconhecem a assimetria de informação e se conseguem articulá-lo para o sistema.

**Fecho:** colaboração eficaz exige mais que tornar a IA transparente; exige desenho cuidadoso para preservar e ampliar o conhecimento e o julgamento humanos.

---
