# Saída estruturada e raciocínio: o que a restrição de formato custa e como não pagar

Como pedir JSON tipado a um modelo generativo sem perder a qualidade do julgamento. Fontes: *Anthropic: Structured outputs (JSON outputs e strict tool use por decodificação restrita)*, de Anthropic (documentação oficial da Claude API) (https://platform.claude.com/docs/en/build-with-claude/structured-outputs), *OpenAI: Structured Outputs (json_schema com strict, function calling estrita, campo refusal)*, de OpenAI (documentação oficial para desenvolvedores) (https://developers.openai.com/api/docs/guides/structured-outputs), *Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models*, de Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin (Appier AI Research); Hung-yi Lee, Yun-Nung Chen (National Taiwan University) (https://aclanthology.org/2024.emnlp-industry.91.pdf), *Generating Structured Outputs from Language Models: Benchmark and Studies (JSONSchemaBench)*, de Saibo Geng, Hudson Cooper, Michał Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, Harsha Nori (Microsoft Research e EPFL) (https://arxiv.org/abs/2501.10868), *LLM-as-a-Judge for Human-AI Co-Creation: A Reliability-Aware Evaluation Framework for Coding*, de Md Faizul Ibne Amin, Yutaka Watanobe, Daniel M. Muepu, Haruto Suzuki, Kenta Nanaumi, Md Mostafizer Rahman (https://arxiv.org/abs/2604.27727), *Langfuse: LLM-as-a-judge (nota mais raciocínio em saída estruturada, e concordância com anotação humana)*, de Langfuse (documentação oficial) (https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge). Complementa [[classificacao-como-portao]] (o método do portão); a outra via, um modelo de decisão tipado que não gera texto (como o Jev, da TypeSafe), entra na tabela do fim.

## O que mudou: JSON válido é garantia, não pedido

Os três grandes fornecedores fazem hoje **decodificação restrita** a partir de um JSON Schema: a gramática é compilada e o modelo só consegue emitir tokens que o esquema permite. Anthropic (`output_config.format` na API e `output_format` nos SDKs, para a resposta e `strict: true` em tools, com gramática em cache por 24 h), OpenAI (`json_schema` com `strict: true` e function calling estrita) e Gemini (`responseSchema`; página oficial rasa, aqui só como citação: https://ai.google.dev/gemini-api/docs/structured-output). Retry por JSON quebrado deixou de ser problema de engenharia. As bibliotecas que faziam isso por conta própria (Instructor, Outlines, XGrammar, Guidance) continuam valendo para modelos abertos; no benchmark de 10 mil esquemas reais, Guidance cobriu mais e compilou mais rápido, Outlines falhou mais na compilação e XGrammar restringiu de menos.

## O custo: a restrição pode calar o raciocínio

Em GSM8K, o Claude 3 Haiku caiu de 86,5% para 23,4% ao responder em JSON mode; o GPT-3.5, de 76,6% para 49,3%; o Gemini 1.5 Flash não caiu. A causa encontrada foi a **ordem das chaves**: o modelo emitiu `answer` antes de `reason` em 100% das respostas e passou a responder direto, sem cadeia de pensamento. Erros de parse eram quase zero, logo a perda é de raciocínio, não de sintaxe. Na classificação, o efeito foi o inverso: JSON mode subiu o Gemini de 41,6% para 60,3% em diagnóstico médico.

O contraponto do JSONSchemaBench (ganho de até 4% em raciocínio sob restrição, 50% mais rápido) não contradiz: o esquema deles deixa espaço para pensar antes de responder. As duas fontes fecham na mesma regra.

## As regras que saem daqui

1. **Raciocínio antes do veredito, e a ordem fixada no esquema.** Campo `raciocinio` (ou `evidencia`: a citação do slide que sustenta) vem antes de `nota`. A OpenAI mostra o mesmo padrão com `steps` antes de `final_answer`. Com raciocínio estendido ligado, o modelo pensa fora do JSON e a regra pesa menos, mas custa nada manter.
2. **Classificação fechada aceita esquema apertado; julgamento aberto pede espaço.** Critério do tipo "há chamada única no último slide?" pode ser `enum` direto. Critério do tipo "a promessa da capa foi cumprida?" precisa de um campo livre antes.
3. **Níveis como `enum`, não como inteiro com faixa.** A Anthropic não aceita `minimum` e `maximum`; um `integer` de 0 a 2 não é garantido lá. `enum: ["0", "1", "2"]` ou `enum` com os nomes das situações é garantido em todos.
4. **`additionalProperties: false` e todos os campos em `required`**, nos dois fornecedores. Esquema recursivo só na OpenAI.
5. **Recusa e abstenção são campos, não exceções.** A OpenAI devolve `refusal` fora do esquema; no esquema do avaliador, cada critério leva a opção "não se aplica". Num modelo de decisão tipado como o Jev é diferente: o caso nulo vai como pergunta companheira à parte (`noul`), não como opção.
6. **Saída tipada resolve o parse, não a confiabilidade.** Quatro juízes de fronteira com rubrica tipada por critério concordaram pouco entre si (Fleiss κ 0,07; Cohen médio 0,16) e calibraram mal (melhor ECE 0,28). A concordância que importa é com o rótulo da pessoa, medida em Cohen's Kappa e matriz de confusão, como a Langfuse faz no Score Analytics. O limiar de kappa ≥ 0,6 de [[classificacao-como-portao]] continua.

## Onde isso entra no avaliador de conteúdo

Duas vias, por tipo de critério, no mesmo portão:

| Critério | Via | Por quê |
|---|---|---|
| Fechado e de alto volume (chamada única, tema em uma frase, legenda curta) | modelo de decisão tipado (o Jev: `choice` ou `noul`) | não precisa raciocinar; probabilidade calibrável; custo desprezível |
| Que exige leitura (promessa cumprida, tom na voz, contexto com valor) | modelo de fronteira com esquema `raciocinio` → `nota` | o julgamento precisa da cadeia; a evidência citada é o que a pessoa confere na revisão |

O código que fecha o portão não muda: falha crítica separada, mínimo por critério, dois limiares, abstenção. Muda só quem responde cada pergunta.

## O que não está verificado

Se a ordem dos campos ainda pesa nos modelos atuais com raciocínio estendido (os números são de 2024, com Haiku 3 e GPT-3.5); em modelos de 7 a 9 B, um preprint de 2026 (Galeone et al., Alomana, arXiv:2605.02363) mediu 3,6 a 8,2× de latência sob restrição e otimização de prompt batendo a gramática, mas está fora do caso de modelos de fronteira; e o "imposto de alinhamento" em reflexão (Zhou, arXiv:2604.06066) é preprint de autor único, sem os números abertos.
