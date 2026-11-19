---
titulo: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"
tipo: paper
autor: "Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang"
url: "https://arxiv.org/abs/2406.01297"
publicado_em: 2024-06-03
capturado_em: 2026-10-28
licenca: "CC BY 4.0 (indicada na página do arXiv)"
areas: [agent-engineering]
tags: [self-correction, intrinsic-self-correction, external-feedback, evaluation-fairness, oracle-feedback, fine-tuning, survey]
---

Ficha em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. Revisão crítica publicada na *Transactions of the Association for Computational Linguistics* (TACL), 2024, vol. 12, p. 1417–1440. arXiv: v1 em 03/06/2024, v3 (lida) em 03/12/2024. Lido em 2026-10-28, na pesquisa.

## A pergunta e as três conclusões

Quando um modelo consegue melhorar a própria resposta durante o uso, com retorno dele mesmo ou de fora? Os resultados publicados se contradiziam; os autores atribuem parte da confusão a perguntas mal definidas, arranjos impraticáveis e avaliações injustas que inflam o ganho. Conclusões:

1. Nenhum trabalho anterior mostra autocorreção bem-sucedida com retorno de um modelo só instruído por prompt, em tarefas gerais. As exceções são tarefas com propriedade especial.
2. A autocorreção funciona bem quando há **retorno externo confiável**.
3. **Ajuste fino em larga escala** a torna possível, mas com muitos dados.

## Vocabulário

- **Autocorreção:** refinar a resposta com o próprio modelo durante a inferência, com ou sem ferramenta ou conhecimento externo. Três etapas: resposta inicial, retorno, refinamento. O **refinamento direto** pula o retorno explícito.
- **Pós-fato contra durante a geração:** corrigir a resposta pronta, ou dar retorno passo a passo no raciocínio.
- **Mesmo modelo contra modelo cruzado:** um modelo diferente (muitas vezes pequeno e treinado para isso) corrigindo um maior fica fora das categorias principais.
- **Fonte do retorno:** **intrínseca** (o modelo critica a si mesmo por prompt, por decomposição ou por estimativa de confiança); **informação externa** (interpretador de código, raciocinador simbólico, assistente de prova, métrica da tarefa, busca, Wikipédia, resposta certa de gabarito, retorno humano, modelo mais forte); **ajuste fino** (supervisionado ou por reforço).
- **Realismo e justiça:** **irrealista** usa informação que não existe na aplicação real, como o gabarito; **justa** refina a melhor resposta inicial possível (intrínseca, ou assimétrica quando o retorno usa informação extra mas a geração inicial também foi melhorada ao máximo); **assimétrica injusta** é prática, mas parte de uma geração inicial mais fraca do que poderia.

## Três perguntas de pesquisa que os trabalhos misturam

- **P1:** o modelo corrige a melhor resposta inicial só com a própria capacidade?
- **P2:** corrige com informação externa?
- **P3:** o resultado final é melhor do que outras abordagens com custo parecido (autoconsistência, gerar e escolher)?

## Avaliações injustas apontadas, com exemplos

- **Uso de gabarito:** o RCI só corrige quando a resposta inicial está errada, o que esconde o dano de trocar resposta certa por errada. O **Reflexion**, no HotpotQA, usa a comparação exata com o gabarito como retorno: irrealista nesse experimento. Nos jogos e no código, com o ambiente ou o interpretador, é assimétrico justo.
- **Resposta inicial enfraquecida:** o **Self-Refine** usa instruções ou exemplos piores na geração inicial do que na correção; revisões de toxicidade sem pedir ao gerador inicial que evite dano.
- **Busca só na correção:** usar a web só para o retorno, e não para a resposta inicial, é assimétrico injusto.
- **Linha de base fraca:** quase ninguém compara com autoconsistência ou com gerar várias e escolher.

## Onde a correção intrínseca funciona e onde não

- Resultados negativos: autocorreção sem retorno externo não melhora ou piora raciocínio (Huang et al. 2024, também na base) e o **CRITIC sem ferramentas** mostra o mesmo. O gargalo é o **retorno**: o modelo julga mal a própria resposta.
- Funciona onde **verificar é bem mais fácil do que gerar**: respostas que se decompõem em itens conferíveis um a um (o CoVe confere cada entidade separadamente) e geração com restrições checáveis.

## Retorno externo

- Execução de código (CRITIC, Self-Debug) e busca (CRITIC no HotpotQA) são os casos de sucesso; raciocinadores simbólicos e assistentes de prova também. O interpretador é assimétrico justo porque não teria como melhorar a geração inicial.

## Ajuste fino

Funciona, mas os métodos usam em geral mais de 100 mil exemplos (178 mil, 274 mil), muitas vezes gerados por modelo mais forte simulando anotação humana; há casos com 20 a 30 mil exemplos sintéticos. Fica aberto quanto dado basta.

## Lista de conferência para experimentos

Obrigatório: dizer a pergunta (P1, P2 ou P3) e a categoria do arranjo; não usar gabarito; reportar anotação e custo do ajuste fino; usar prompts fortes na resposta inicial; usar correção intrínseca para P1; com ferramenta externa, melhorar a geração inicial ao máximo; comparar com linhas de base fortes de custo comparável. Recomendado: medir a qualidade do retorno em si (acerto na detecção de erro); achar o mínimo de dados de treino; testar correção cruzada de modelos mais fortes. Para resultado negativo: dizer qual pergunta foi refutada, usar prompts fortes e declarar quando a avaliação não usou ferramentas reais.

## Caminhos abertos

Retorno melhor (avaliação sem referência, critérios escritos por pessoas, decomposição da resposta, checagem de confiança e de consistência lógica); tarefas abertas como diálogo e resumo, onde avaliar com modelo já é comum; ajuste fino com poucos dados; pré-treino que ensine a autocorrigir. A versão final cita a correção por reforço (o o1 da OpenAI) como desenvolvimento recente.

---
