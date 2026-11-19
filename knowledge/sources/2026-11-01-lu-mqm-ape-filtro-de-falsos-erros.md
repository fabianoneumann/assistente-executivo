---
titulo: "MQM-APE: Toward High-Quality Error Annotation Predictors with Automatic Post-Editing in LLM Translation Evaluators"
tipo: paper
autor: "Qingyu Lu, Liang Ding, Kanjian Zhang, Jinxia Zhang, Dacheng Tao"
url: "https://arxiv.org/abs/2409.14335"
publicado_em: 2024-09-22
capturado_em: 2026-11-01
licenca: "CC0 1.0, dedicação ao domínio público (indicada na página do arXiv, com link para http://creativecommons.org/publicdomain/zero/1.0/)"
areas: [agent-engineering]
tags: [mqm, llm-as-judge, error-annotation, false-alarm-filtering, defect-verification, post-editing, pairwise-verification, span-precision, over-flagging, style-errors, machine-translation]
---

Ficha em palavras próprias; o texto integral (domínio público, CC0 1.0) não vem neste repositório e se lê na url do frontmatter.

Ficha de estudo, em palavras próprias. arXiv 2409.14335, v1 em 22/09/2024 e v2 em 16/12/2024; lida a v2. Comentário do arXiv: "COLING 2025". Autores da Southeast University, da Universidade de Sydney e da Nanyang Technological University. Código em https://github.com/Coldmist-Lu/MQM_APE. Texto extraído do PDF da v2 com `pdftotext`; tabelas lidas no modo de layout, linha a linha. Lido para a rodada investigativa.

**Atenção:** só modelos abertos de 2024 (Llama 3 de 8 e 70 bilhões, Mixtral 8x7b e 8x22b, Qwen1.5 de 14 e 72 bilhões, Tower de 7 e 13 bilhões, este treinado para tradução); os autores excluíram modelos fechados por reprodutibilidade. Os ganhos são pequenos em valor absoluto; o interesse está no diagnóstico do que o avaliador marca a mais e no desenho do filtro.

## 1. O problema

Avaliadores como o GEMBA-MQM dão boa nota no agregado, mas os erros que apontam **não coincidem bem com os dos anotadores humanos**, o que reduz o valor deles como retorno para quem precisa corrigir. Treinar avaliadores específicos custa caro; a proposta é um filtro sem treino.

## 2. O método: três papéis, o mesmo modelo

1. **Avaliador:** o prompt do GEMBA-MQM, com três exemplos, lista os erros com trecho, categoria e gravidade (crítico, maior, menor). Tradução sem erro apontado pula as etapas seguintes.
2. **Pós-editor:** para **cada** erro apontado, o modelo reescreve a tradução corrigindo só aquele erro, usando o trecho e a categoria como guia.
3. **Verificador em pares:** o modelo compara a versão corrigida com a original e diz qual é melhor; a comparação é feita **duas vezes, com a ordem trocada**, para conter o viés de posição, e o resultado discordante conta meio ponto.

**Só fica o erro cuja correção melhora a tradução**; o resto é descartado como "sem impacto". A nota é a soma ponderada do MQM sobre os erros que restam, 25 por crítico, 5 por maior e 1 por menor, com piso de menos 25 para a nota não despencar quando o avaliador aponta erros demais. Subprodutos: os erros filtrados e as traduções corrigidas.

## 3. Resultados

- **WMT22** (106.758 segmentos de 54 sistemas, inglês para alemão, inglês para russo e chinês para inglês, com MQM de especialistas) e **IndicMT** (1.000 segmentos com MQM em quatro línguas indianas de poucos recursos).
- **Ordem de sistemas e nota por segmento:** o filtro melhora o GEMBA-MQM em todos os oito modelos, com uma exceção no nível de sistema (Mixtral 8x22b, que fica igual). Os ganhos no WMT22 vão de 0 a 5,8 pontos percentuais na acurácia por pares de sistemas e de 0,2 a 1,5 por segmento; no IndicMT, de 0,5 a 14,4 por segmento.
- **Qualidade dos trechos:** a precisão de trecho (fração do que o modelo marca que os humanos também marcaram) sobe em todos os modelos, mas continua baixa: de 9,0% a 21,2% antes do filtro e de 10,3% a 21,4% depois. A precisão nos erros maiores e críticos vai de 3,3% a 16,1% antes e sobe em sete dos oito.
- **Não é efeito de jogar fora erros ao acaso:** um filtro que descarta erros aleatoriamente piora o desempenho em todos os modelos.
- **As correções melhoram a tradução** em duas métricas automáticas, com confiança acima de 95% em sete dos oito modelos; o verificador concorda com uma métrica automática (CometKiwi), que pode substituí-lo com efeito parecido e custo menor.
- **Custo:** as etapas de correção e verificação geram cerca do dobro dos tokens do avaliador, com cerca de metade dos tokens de entrada.

## 4. O que o avaliador marca a mais (apêndice F)

- **Quantidade:** os anotadores humanos do WMT22 marcam em média **0,67 erro por segmento** (0,00 crítico, 0,26 maior, 0,41 menor). Os modelos marcam de 0,67 a 2,83 por segmento antes do filtro (Mixtral 8x7b, 2,83; Mixtral 8x22b, 2,20; Tower 7b, 2,00; Tower 13b, 1,75; Llama 3 8b, 1,49; Qwen 72b, 1,30; Llama 3 70b, 1,02; Qwen 14b, 0,67) e de 0,50 a 1,87 depois. **Os humanos quase não usam "crítico"; os modelos marcam de 0,06 a 0,85 crítico por segmento.** O Tower 7b tem a maior parte dos erros descartada pelo filtro.
- **Categoria:** 27% dos erros apontados pelo avaliador são de **estilo ou construção estranha**, enquanto os humanos se concentram em **má tradução**. Os erros descartados são, na maioria, de estilo. Os autores recomendam que o avaliador priorize a má tradução e trate os de estilo com cautela.
- **O que o modelo deixa passar:** erros que os humanos marcam, como **ortografia e inconsistência**, quase nunca aparecem nas listas dos modelos; a cauda longa dos erros miúdos escapa.
- **O filtro não conserta a distribuição:** depois dele, a proporção entre gravidades e categorias continua a do avaliador, desalinhada da humana (limite declarado).

## 5. Limites declarados

Custo de inferência cerca de duas vezes maior; a distribuição dos erros continua diferente da humana; quando o pós-editor corrige vários erros maiores de uma vez, o filtro perde a capacidade de separá-los (os autores sugerem aplicar o filtro só aos erros menores nesse caso); resposta fora do formato é refeita com temperatura um pouco mais alta.

## 6. Tudo o mais que ensina

- **Verificar o defeito pela correção:** um erro apontado vale se consertá-lo melhora a peça; se a versão corrigida não é melhor, o apontamento era ruído. É uma pergunta mais fácil (qual das duas é melhor?) que a original (o que está errado?).
- **Comparação em pares nas duas ordens** dentro do próprio filtro, com meio ponto para o resultado que muda com a ordem.
- **Piso na nota** para que um avaliador que aponta demais não domine a média.
- **O verificador pode ser trocado por uma métrica mais barata** quando ela concorda com ele.
- **Ranking de modelos como avaliadores** em três eixos (confiabilidade, interpretabilidade e custo, Tabela 8): o mais confiável pode gerar trechos imprecisos e redundantes; o mais barato pode bastar.
