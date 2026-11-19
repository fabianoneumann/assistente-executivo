---
titulo: "Feasibility"
tipo: artigo
autor: "Google for Developers (Machine Learning, curso Managing ML Projects)"
url: "https://developers.google.com/machine-learning/managing-ml-projects/feasibility"
publicado_em: 2025-08-25
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [feasibility, ml-projects, data-availability, serving-features, human-benchmark, prediction-quality, technical-requirements, ml-cost, generative-ai, few-shot]
licenca: "CC BY 4.0, no rodapé da página"
---

# Google 2025, "Feasibility": como estimar se uma solução de ML é viável

Ficha em palavras próprias. Página do curso Managing ML Projects, em Machine Learning, Google for Developers; sem autor nomeado; o rodapé traz última atualização em 25/8/2025 (UTC), única data da página. Área: gestão de projetos de aprendizado de máquina. Material de curso, sem estudo citado: os números são exemplos ou estimativas da página.

## Onde o tema entra

Na fase de ideação e planejamento, depois de enquadrar o problema como ML, vem a tarefa de estimar a viabilidade, planejar abordagens e definir métricas de sucesso. Uma solução pode funcionar em tese e ainda ser impraticável de implementar. A página lista cinco fatores: dados disponíveis, dificuldade do problema, qualidade de predição, requisitos técnicos e custo. Os quatro primeiros trazem um bloco à parte sobre IA generativa.

## 1. Dados disponíveis

Modelo só é tão bom quanto os dados de treino, e precisa de muito dado de alta qualidade. Três perguntas:

- **Quantidade:** dá para conseguir dado bom o suficiente? Os exemplos rotulados são escassos, difíceis ou caros? Imagens médicas rotuladas e traduções de línguas raras servem de exemplo. Um classificador pede muitos exemplos de cada rótulo, e rótulos com poucos exemplos levam a predições ruins.
- **Atributo disponível na hora de servir:** tudo o que se usa no treino estará lá em produção? A página conta que equipes gastaram muito tempo treinando para só então notar que certos atributos chegavam dias depois de o modelo precisar deles. Exemplo: prever clique numa URL com `user_age` como atributo, quando esse dado não existe ao servir porque o usuário ainda não criou conta.
- **Regulação:** que leis e exigências valem para obter e usar o dado? Algumas limitam guardar e usar certos tipos de dado.

**Em IA generativa:** modelos pré-treinados costumam pedir conjuntos curados para ir bem em tarefas de um domínio, seja para engenharia de prompt, ajuste eficiente em parâmetros (parameter-efficient tuning) ou fine-tuning. Conforme o caso, de 10 a 10.000 exemplos de alta qualidade. Exemplo: fine-tuning para perguntas médicas pede um conjunto que represente as perguntas e as respostas esperadas.

| Técnica | Exemplos necessários (estimativa da página) |
|---|---|
| Zero-shot prompting | 0 |
| Few-shot prompting | ~10s a 100s |
| Parameter-efficient tuning (LoRA, Low-Rank Adaptation, e prompt tuning) | ~100s a 10.000s |
| Fine-tuning | ~1.000s a 10.000s, ou mais |

No fine-tuning, a página destaca que a qualidade dos dados pesa mais que a quantidade. Outra questão é a atualização: depois de pré-treinado, o modelo tem conhecimento fixo; se o domínio muda muito, precisa de estratégia, como fine-tuning, RAG (geração aumentada por recuperação) ou novo pré-treino periódico.

## 2. Dificuldade do problema

É difícil de estimar: o que parece plausível pode ser questão de pesquisa em aberto, e o que parece prático pode não funcionar. Três perguntas:

- **Já resolveram algo parecido?** Dentro da organização, com dados iguais ou semelhantes, ou fora dela (Kaggle, TensorFlow Hub). Se sim, é provável aproveitar partes do modelo. Problema novo pede muito tempo e recurso, pois equivale a projeto de pesquisa sem garantia de solução.
- **O problema é difícil por natureza?** O desempenho humano serve de referência. A página dá cerca de 95% de acurácia em classificar o animal numa imagem e cerca de 99% em classificar dígitos escritos à mão, e conclui daí que o primeiro modelo é mais difícil de criar que o segundo.
- **Há agentes mal-intencionados?** Se alguém vai tentar explorar o modelo, será uma corrida constante de atualização, como o filtro de spam diante de mensagens feitas para parecerem legítimas.

**Em IA generativa,** vulnerabilidades somam dificuldade:

- **Origem da entrada:** prompts adversários podem vazar dados de treino, preâmbulo, conteúdo de banco ou informação de ferramentas?
- **Uso da saída:** vai crua, ou passa por etapas que testam e verificam? Entregar a saída crua a plugins pode gerar problemas de segurança.
- **Fine-tuning:** um conjunto corrompido afeta os pesos e leva a conteúdo incorreto, tóxico ou enviesado, por isso o conjunto precisa estar verificado.

## 3. Qualidade de predição

A qualidade exigida depende do impacto da predição nos usuários e do tipo de predição. Comparação da página: recomendar o vídeo errado pode dar má experiência; marcar um vídeo como violação sem que seja pode gerar custo de suporte ou, pior, despesa jurídica.

Quanto maior a qualidade exigida, mais difícil o problema, e os projetos costumam entrar em retornos decrescentes. Exemplo da página: subir a precisão de 99,9% para 99,99% pode multiplicar por dez o custo do projeto, ou mais. A Figura 2 mostra o recurso necessário crescendo com a qualidade exigida.

**Em IA generativa:**

- **Exatidão factual:** texto fluente e coerente não garante fato. As afirmações falsas se chamam confabulações, como resumos incorretos, respostas erradas de matemática e declarações falsas sobre o mundo. Muitos usos ainda pedem verificação humana antes de produção, como código gerado por LLM. Quanto maior a exigência de exatidão, maior o custo de desenvolver e manter, como no ML tradicional.
- **Qualidade da saída:** quais são as consequências legais, financeiras ou éticas de saídas ruins, como conteúdo enviesado, plagiado ou tóxico?

## 4. Requisitos técnicos

- **Latência:** com que rapidez a predição precisa sair?
- **Consultas por segundo (QPS).**
- **Uso de RAM,** no treino e ao servir.
- **Plataforma:** online (consultas a um servidor RPC), WebML (no navegador), ODML (em celular ou tablet) ou offline (predições guardadas em tabela).
- **Interpretabilidade:** o produto terá de responder por que um conteúdo virou spam ou por que um vídeo violou a política? Explicar predição é difícil e área ativa de pesquisa; a página cita Model Cards e What-if Tool como ajuda inicial.
- **Frequência de retreino:** dados que mudam rápido podem pedir retreino frequente ou contínuo, e esse custo pode superar o benefício de atualizar.

Na maioria dos casos, será preciso ceder em qualidade para caber nos requisitos, e então decidir se o modelo ainda basta para produção.

**Em IA generativa:**

- **Plataforma:** há modelos de escala de data center até os que cabem num celular, e a escolha pesa latência, privacidade e qualidade, que costumam conflitar. A privacidade pode pedir inferência no aparelho, onde a qualidade pode sair ruim por falta de recurso.
- **Latência:** o tamanho da saída pesa mais que o da entrada, porque entradas se processam em paralelo e saídas se geram em sequência. Ler 10 ou 500 palavras pode levar o mesmo tempo, ao passo que gerar um resumo de 500 palavras leva bem mais que um de 10.
- **Ferramentas e APIs:** busca na internet, calculadora, cliente de e-mail. Em geral, quanto mais ferramentas, mais chances de propagar erros e mais vulnerabilidades.

## 5. Custo

A implementação compensa? A maioria dos projetos não passa na aprovação se implementar e manter custa mais do que o dinheiro que gera ou economiza.

- **Custo humano:** quantas pessoas da prova de conceito à produção? As despesas tendem a crescer com a evolução do projeto, e pôr um sistema em produção pede mais gente que um protótipo. Estimar número e tipo de papéis por fase.
- **Custo de máquina:** treinar, implantar e manter pede muito processamento e memória, como cota de TPU e infraestrutura de pipeline de dados; pode haver pagamento por rotulagem ou licença de dados. Estimar antes de treinar, olhando o longo prazo.
- **Custo de inferência:** centenas ou milhares de inferências custarão mais que a receita gerada?

## O exercício de fixação

Uma empresa de preservação quer classificar 60 espécies de plantas invasoras. Existe código de exemplo para problema parecido, o custo cabe no orçamento, a liderança não exige interpretabilidade e não parecem existir consequências ruins de predição errada. O conjunto de dados é grande, mas tem poucos exemplos das cinco espécies mais invasoras. A resposta certa da página é que a solução não é viável: faltam exemplos por espécie, ainda que quase todo o resto atenda ao critério.

## Ressalvas da página

- Dificuldade é difícil de estimar a priori.
- Prazo apertado amplia qualquer um desses problemas: planejar o tempo pela dificuldade percebida e reservar ainda mais folga do que num projeto sem ML.
- Os números de exemplos da tabela são estimativas, e os de desempenho humano e de custo vêm sem fonte.

## Tudo o mais que ensina

- A página aponta o curso Introduction to Machine Learning Problem Framing para os passos de enquadrar o problema, e segue no curso com "Working with stakeholders" antes e "Planning" depois.
- Glossário ligado: classification model, confabulation, example, few-shot prompt, fine-tuning, inference, interpretability, label, labeled example, parameter-efficient tuning, precision, pre-trained model, prompt engineering, retrieval augmented generation, training, training set, zero-shot prompt.
- O resumo no topo da página repete os cinco fatores e diz que avaliá-los permite decidir com informação sobre a viabilidade e a implementação.
